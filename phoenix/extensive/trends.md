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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-11.07%)</td><td>0.02 <b>(-24.90%)</b></td><td>0.02 <b>(-25.98%)</b></td><td>0.01 <b>(-42.89%)</b></td><td>0.01 <b>(+53.82%)</b></td><td>568.10 <b>(+75.07%)</b></td><td>391.24 <b>(+48.37%)</b></td><td>385.30 <b>(+35.10%)</b></td><td>232.90 (+12.46%)</td><td>156.91 <b>(+204.98%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>324.50 (n/a)</td><td>263.70 (n/a)</td><td>285.20 (n/a)</td><td>207.10 (n/a)</td><td>51.45 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-15.91%)</td><td>0.02 (-0.60%)</td><td>0.02 (+0.23%)</td><td>0.01 (+13.10%)</td><td>0.00 <b>(-48.24%)</b></td><td>462.70 (-11.60%)</td><td>326.76 (-9.29%)</td><td>311.40 (-0.26%)</td><td>245.50 (+18.89%)</td><td>80.91 <b>(-46.79%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.40 (n/a)</td><td>360.22 (n/a)</td><td>312.20 (n/a)</td><td>206.50 (n/a)</td><td>152.07 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(-31.14%)</b></td><td>0.02 (-16.31%)</td><td>0.02 <b>(-26.95%)</b></td><td>0.01 (+19.16%)</td><td>0.01 <b>(-47.47%)</b></td><td>502.40 (-16.08%)</td><td>383.20 (+3.92%)</td><td>381.40 <b>(+36.90%)</b></td><td>261.30 <b>(+45.17%)</b></td><td>113.83 <b>(-40.05%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.70 (n/a)</td><td>368.76 (n/a)</td><td>278.60 (n/a)</td><td>180.00 (n/a)</td><td>189.86 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-6.57%)</td><td>0.02 (-5.64%)</td><td>0.01 (+10.41%)</td><td>0.01 (-3.61%)</td><td>0.00 (-19.16%)</td><td>633.90 (+3.73%)</td><td>441.46 (+2.94%)</td><td>440.10 (-9.43%)</td><td>270.40 (+7.05%)</td><td>132.93 (-9.46%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.10 (n/a)</td><td>428.84 (n/a)</td><td>485.90 (n/a)</td><td>252.60 (n/a)</td><td>146.83 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-19.39%)</td><td>0.01 <b>(-35.64%)</b></td><td>0.01 <b>(-47.54%)</b></td><td>0.01 <b>(-30.75%)</b></td><td>0.00 (-14.70%)</td><td>797.00 <b>(+44.41%)</b></td><td>522.70 <b>(+57.81%)</b></td><td>538.60 <b>(+90.65%)</b></td><td>299.20 <b>(+24.05%)</b></td><td>183.55 <b>(+44.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.90 (n/a)</td><td>331.22 (n/a)</td><td>282.50 (n/a)</td><td>241.20 (n/a)</td><td>127.10 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(+22.51%)</b></td><td>0.02 (-3.71%)</td><td>0.01 <b>(-25.98%)</b></td><td>0.01 (+6.85%)</td><td>0.01 <b>(+44.08%)</b></td><td>534.90 (-6.42%)</td><td>426.82 (+7.26%)</td><td>478.00 <b>(+35.10%)</b></td><td>250.70 (-18.37%)</td><td>125.13 (+13.68%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.60 (n/a)</td><td>397.92 (n/a)</td><td>353.80 (n/a)</td><td>307.10 (n/a)</td><td>110.08 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (+6.84%)</td><td>0.04 (+7.05%)</td><td>0.04 (-1.54%)</td><td>0.04 <b>(+66.88%)</b></td><td>0.01 <b>(-36.59%)</b></td><td>348.70 <b>(-40.09%)</b></td><td>299.68 (-12.95%)</td><td>297.60 (+1.57%)</td><td>231.50 (-6.39%)</td><td>44.93 <b>(-66.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>582.00 (n/a)</td><td>344.28 (n/a)</td><td>293.00 (n/a)</td><td>247.30 (n/a)</td><td>135.83 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (+1.22%)</td><td>0.03 (-6.19%)</td><td>0.03 (-15.69%)</td><td>0.02 (-8.90%)</td><td>0.01 <b>(+23.83%)</b></td><td>519.50 (+9.76%)</td><td>406.28 (+10.81%)</td><td>470.20 (+18.59%)</td><td>244.80 (-1.21%)</td><td>127.40 <b>(+38.98%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.30 (n/a)</td><td>366.66 (n/a)</td><td>396.50 (n/a)</td><td>247.80 (n/a)</td><td>91.67 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (-15.15%)</td><td>0.03 (-16.12%)</td><td>0.03 <b>(-32.00%)</b></td><td>0.02 (+10.09%)</td><td>0.01 <b>(-42.71%)</b></td><td>551.80 (-9.17%)</td><td>434.02 (+9.88%)</td><td>437.90 <b>(+47.09%)</b></td><td>294.80 (+17.83%)</td><td>92.30 <b>(-42.65%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>607.50 (n/a)</td><td>394.98 (n/a)</td><td>297.70 (n/a)</td><td>250.20 (n/a)</td><td>160.95 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (-17.58%)</td><td>0.03 <b>(-36.39%)</b></td><td>0.02 <b>(-40.14%)</b></td><td>0.01 <b>(-45.00%)</b></td><td>0.01 (+3.36%)</td><td>1002.20 <b>(+81.79%)</b></td><td>570.24 <b>(+69.98%)</b></td><td>492.70 <b>(+67.07%)</b></td><td>294.80 <b>(+21.37%)</b></td><td>265.16 <b>(+116.10%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.30 (n/a)</td><td>335.48 (n/a)</td><td>294.90 (n/a)</td><td>242.90 (n/a)</td><td>122.70 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 <b>(+74.20%)</b></td><td>0.03 <b>(+53.28%)</b></td><td>0.03 <b>(+24.62%)</b></td><td>0.02 <b>(+56.02%)</b></td><td>0.01 <b>(+117.04%)</b></td><td>659.40 <b>(-35.91%)</b></td><td>440.58 <b>(-31.55%)</b></td><td>485.90 (-19.77%)</td><td>246.50 <b>(-42.61%)</b></td><td>168.48 <b>(-26.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1028.90 (n/a)</td><td>643.68 (n/a)</td><td>605.60 (n/a)</td><td>429.50 (n/a)</td><td>228.89 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+10.16%)</td><td>0.03 (+11.20%)</td><td>0.03 (+8.93%)</td><td>0.02 (-7.38%)</td><td>0.01 <b>(+37.22%)</b></td><td>622.30 (+7.96%)</td><td>451.32 (-7.46%)</td><td>478.50 (-8.21%)</td><td>307.10 (-9.22%)</td><td>125.34 <b>(+35.31%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.40 (n/a)</td><td>487.72 (n/a)</td><td>521.30 (n/a)</td><td>338.30 (n/a)</td><td>92.63 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (-4.07%)</td><td>0.08 <b>(+20.08%)</b></td><td>0.08 <b>(+59.09%)</b></td><td>0.05 (+10.89%)</td><td>0.02 <b>(-22.11%)</b></td><td>504.20 (-9.82%)</td><td>330.90 <b>(-20.48%)</b></td><td>293.80 <b>(-37.13%)</b></td><td>246.10 (+4.24%)</td><td>104.43 <b>(-26.20%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>559.10 (n/a)</td><td>416.14 (n/a)</td><td>467.30 (n/a)</td><td>236.10 (n/a)</td><td>141.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (+12.57%)</td><td>0.08 (+0.43%)</td><td>0.10 <b>(+21.88%)</b></td><td>0.05 (-2.35%)</td><td>0.03 <b>(+35.55%)</b></td><td>529.70 (+2.40%)</td><td>338.26 (+5.26%)</td><td>247.90 (-17.94%)</td><td>208.10 (-11.18%)</td><td>145.26 <b>(+26.00%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>517.30 (n/a)</td><td>321.36 (n/a)</td><td>302.10 (n/a)</td><td>234.30 (n/a)</td><td>115.29 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (+12.74%)</td><td>0.07 (+9.91%)</td><td>0.08 <b>(+23.44%)</b></td><td>0.04 (-2.05%)</td><td>0.03 <b>(+31.11%)</b></td><td>646.30 (+2.10%)</td><td>392.20 (-3.96%)</td><td>301.40 (-18.98%)</td><td>233.40 (-11.29%)</td><td>179.39 <b>(+20.20%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>633.00 (n/a)</td><td>408.38 (n/a)</td><td>372.00 (n/a)</td><td>263.10 (n/a)</td><td>149.23 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (+14.71%)</td><td>0.07 (+17.73%)</td><td>0.05 (+1.85%)</td><td>0.04 (-2.66%)</td><td>0.03 <b>(+51.55%)</b></td><td>604.60 (+2.72%)</td><td>439.96 (-7.12%)</td><td>500.00 (-1.81%)</td><td>231.30 (-12.85%)</td><td>181.52 <b>(+46.74%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>588.60 (n/a)</td><td>473.70 (n/a)</td><td>509.20 (n/a)</td><td>265.40 (n/a)</td><td>123.71 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (+19.48%)</td><td>0.09 <b>(+58.77%)</b></td><td>0.09 <b>(+92.88%)</b></td><td>0.07 <b>(+49.67%)</b></td><td>0.02 <b>(-20.74%)</b></td><td>360.90 <b>(-33.19%)</b></td><td>279.78 <b>(-39.75%)</b></td><td>265.20 <b>(-48.15%)</b></td><td>222.80 (-16.30%)</td><td>52.57 <b>(-53.55%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>540.20 (n/a)</td><td>464.34 (n/a)</td><td>511.50 (n/a)</td><td>266.20 (n/a)</td><td>113.18 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 <b>(-30.42%)</b></td><td>0.08 (+2.67%)</td><td>0.08 <b>(+55.11%)</b></td><td>0.04 (-5.78%)</td><td>0.02 <b>(-45.35%)</b></td><td>577.90 (+6.13%)</td><td>348.78 (-10.44%)</td><td>298.20 <b>(-35.52%)</b></td><td>248.60 <b>(+43.70%)</b></td><td>133.30 (-11.43%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>544.50 (n/a)</td><td>389.44 (n/a)</td><td>462.50 (n/a)</td><td>173.00 (n/a)</td><td>150.51 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.21 (-0.29%)</td><td>0.18 (+9.36%)</td><td>0.18 (-3.55%)</td><td>0.15 <b>(+153.63%)</b></td><td>0.02 <b>(-62.10%)</b></td><td>319.40 <b>(-60.57%)</b></td><td>274.48 <b>(-25.52%)</b></td><td>274.60 (+3.70%)</td><td>231.90 (+0.30%)</td><td>35.15 <b>(-85.83%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>810.00 (n/a)</td><td>368.52 (n/a)</td><td>264.80 (n/a)</td><td>231.20 (n/a)</td><td>248.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.21 <b>(+21.03%)</b></td><td>0.18 <b>(+59.87%)</b></td><td>0.20 <b>(+125.67%)</b></td><td>0.11 <b>(+32.96%)</b></td><td>0.04 (+5.43%)</td><td>466.80 <b>(-24.79%)</b></td><td>292.04 <b>(-39.03%)</b></td><td>248.90 <b>(-55.69%)</b></td><td>237.90 (-17.37%)</td><td>98.25 <b>(-33.22%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>620.70 (n/a)</td><td>479.00 (n/a)</td><td>561.70 (n/a)</td><td>287.90 (n/a)</td><td>147.11 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 (+0.44%)</td><td>0.13 (+8.55%)</td><td>0.10 (-0.28%)</td><td>0.08 (-16.81%)</td><td>0.05 <b>(+20.19%)</b></td><td>653.10 <b>(+20.21%)</b></td><td>440.96 (-2.86%)</td><td>497.70 (+0.28%)</td><td>250.80 (-0.44%)</td><td>168.06 <b>(+45.76%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>543.30 (n/a)</td><td>453.92 (n/a)</td><td>496.30 (n/a)</td><td>251.90 (n/a)</td><td>115.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 (-8.10%)</td><td>0.11 <b>(-20.95%)</b></td><td>0.09 (-18.22%)</td><td>0.05 <b>(-29.60%)</b></td><td>0.05 (-19.42%)</td><td>942.30 <b>(+42.04%)</b></td><td>541.66 <b>(+25.17%)</b></td><td>522.80 <b>(+22.29%)</b></td><td>250.30 (+8.83%)</td><td>254.07 <b>(+27.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>663.40 (n/a)</td><td>432.74 (n/a)</td><td>427.50 (n/a)</td><td>230.00 (n/a)</td><td>199.66 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 (-15.13%)</td><td>0.13 (-4.50%)</td><td>0.12 (+10.22%)</td><td>0.10 (+0.55%)</td><td>0.04 <b>(-29.97%)</b></td><td>495.90 (-0.56%)</td><td>388.62 (-0.17%)</td><td>423.60 (-9.27%)</td><td>247.50 (+17.80%)</td><td>100.81 <b>(-20.51%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>498.70 (n/a)</td><td>389.28 (n/a)</td><td>466.90 (n/a)</td><td>210.10 (n/a)</td><td>126.82 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.22 (+18.88%)</td><td>0.13 (+7.53%)</td><td>0.09 (-11.15%)</td><td>0.08 (-3.90%)</td><td>0.06 <b>(+38.21%)</b></td><td>648.80 (+4.06%)</td><td>460.18 (-1.02%)</td><td>541.80 (+12.57%)</td><td>227.90 (-15.90%)</td><td>187.53 (+17.72%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>623.50 (n/a)</td><td>464.92 (n/a)</td><td>481.30 (n/a)</td><td>271.00 (n/a)</td><td>159.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (+4.93%)</td><td>0.01 <b>(+39.21%)</b></td><td>0.01 <b>(+59.88%)</b></td><td>0.01 <b>(+34.44%)</b></td><td>0.00 <b>(-27.15%)</b></td><td>396.10 <b>(-25.62%)</b></td><td>299.78 <b>(-30.64%)</b></td><td>283.10 <b>(-37.45%)</b></td><td>263.30 (-4.71%)</td><td>55.21 <b>(-47.66%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>532.50 (n/a)</td><td>432.20 (n/a)</td><td>452.60 (n/a)</td><td>276.30 (n/a)</td><td>105.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (-1.95%)</td><td>0.01 (-6.90%)</td><td>0.01 <b>(-22.70%)</b></td><td>0.00 (-3.74%)</td><td>0.00 (+10.39%)</td><td>530.60 (+3.90%)</td><td>404.38 (+10.12%)</td><td>442.60 <b>(+29.38%)</b></td><td>236.70 (+1.98%)</td><td>136.57 (+17.87%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.70 (n/a)</td><td>367.22 (n/a)</td><td>342.10 (n/a)</td><td>232.10 (n/a)</td><td>115.86 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (+2.72%)</td><td>0.01 (-16.05%)</td><td>0.01 <b>(-32.72%)</b></td><td>0.00 (+4.85%)</td><td>0.00 (-13.02%)</td><td>640.50 (-4.63%)</td><td>461.44 (+14.62%)</td><td>430.00 <b>(+48.63%)</b></td><td>254.40 (-2.68%)</td><td>158.79 (-14.24%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>671.60 (n/a)</td><td>402.58 (n/a)</td><td>289.30 (n/a)</td><td>261.40 (n/a)</td><td>185.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (-2.30%)</td><td>0.01 <b>(-20.04%)</b></td><td>0.01 <b>(-33.79%)</b></td><td>0.00 <b>(-40.19%)</b></td><td>0.00 <b>(+57.91%)</b></td><td>816.20 <b>(+67.19%)</b></td><td>455.84 <b>(+42.33%)</b></td><td>438.00 <b>(+51.03%)</b></td><td>258.30 (+2.34%)</td><td>228.91 <b>(+138.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.20 (n/a)</td><td>320.26 (n/a)</td><td>290.00 (n/a)</td><td>252.40 (n/a)</td><td>95.81 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (-13.47%)</td><td>0.01 (-14.71%)</td><td>0.01 <b>(-22.19%)</b></td><td>0.00 <b>(+20.37%)</b></td><td>0.00 <b>(-30.96%)</b></td><td>586.30 (-16.92%)</td><td>450.00 (+9.80%)</td><td>411.70 <b>(+28.50%)</b></td><td>298.70 (+15.55%)</td><td>123.02 <b>(-32.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>705.70 (n/a)</td><td>409.82 (n/a)</td><td>320.40 (n/a)</td><td>258.50 (n/a)</td><td>181.97 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (+10.89%)</td><td>0.01 (-3.16%)</td><td>0.01 (+15.14%)</td><td>0.00 <b>(-68.16%)</b></td><td>0.00 <b>(+42.14%)</b></td><td>1894.90 <b>(+214.04%)</b></td><td>727.84 <b>(+49.20%)</b></td><td>485.50 (-13.15%)</td><td>218.00 (-9.81%)</td><td>667.31 <b>(+355.05%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>603.40 (n/a)</td><td>487.84 (n/a)</td><td>559.00 (n/a)</td><td>241.70 (n/a)</td><td>146.65 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+5.27%)</td><td>0.02 (+5.33%)</td><td>0.02 (+0.53%)</td><td>0.01 (+12.45%)</td><td>0.01 (+6.13%)</td><td>527.30 (-11.08%)</td><td>361.70 (-5.33%)</td><td>296.90 (-0.54%)</td><td>240.00 (-5.03%)</td><td>130.99 (-9.14%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.00 (n/a)</td><td>382.08 (n/a)</td><td>298.50 (n/a)</td><td>252.70 (n/a)</td><td>144.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+8.17%)</td><td>0.01 (-3.34%)</td><td>0.01 <b>(-34.94%)</b></td><td>0.01 <b>(+73.39%)</b></td><td>0.01 (-11.27%)</td><td>653.00 <b>(-42.32%)</b></td><td>429.32 (-12.51%)</td><td>461.20 <b>(+53.73%)</b></td><td>234.60 (-7.57%)</td><td>171.32 <b>(-53.97%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1132.20 (n/a)</td><td>490.72 (n/a)</td><td>300.00 (n/a)</td><td>253.80 (n/a)</td><td>372.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(+23.69%)</b></td><td>0.02 (+2.37%)</td><td>0.02 (-1.20%)</td><td>0.00 <b>(-71.47%)</b></td><td>0.01 <b>(+81.93%)</b></td><td>1808.20 <b>(+250.49%)</b></td><td>571.24 <b>(+66.61%)</b></td><td>278.20 (+1.20%)</td><td>210.40 (-19.14%)</td><td>692.28 <b>(+513.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.90 (n/a)</td><td>342.86 (n/a)</td><td>274.90 (n/a)</td><td>260.20 (n/a)</td><td>112.90 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(-20.85%)</b></td><td>0.01 (-16.53%)</td><td>0.01 (-0.77%)</td><td>0.01 (-10.51%)</td><td>0.00 <b>(-33.41%)</b></td><td>606.30 (+11.74%)</td><td>474.18 (+15.36%)</td><td>469.20 (+0.77%)</td><td>295.20 <b>(+26.32%)</b></td><td>116.39 (-9.41%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>542.60 (n/a)</td><td>411.04 (n/a)</td><td>465.60 (n/a)</td><td>233.70 (n/a)</td><td>128.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-4.37%)</td><td>0.01 (-7.20%)</td><td>0.02 (-7.71%)</td><td>0.01 (+5.81%)</td><td>0.00 (-6.10%)</td><td>562.90 (-5.49%)</td><td>401.64 (+7.14%)</td><td>318.20 (+8.34%)</td><td>284.80 (+4.59%)</td><td>139.03 (-1.47%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.60 (n/a)</td><td>374.88 (n/a)</td><td>293.70 (n/a)</td><td>272.30 (n/a)</td><td>141.10 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(+28.76%)</b></td><td>0.01 (+19.91%)</td><td>0.01 (-4.76%)</td><td>0.01 <b>(+24.61%)</b></td><td>0.00 <b>(+57.55%)</b></td><td>639.10 (-19.75%)</td><td>444.90 (-14.01%)</td><td>502.90 (+4.99%)</td><td>281.80 <b>(-22.35%)</b></td><td>153.62 (-9.94%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>796.40 (n/a)</td><td>517.40 (n/a)</td><td>479.00 (n/a)</td><td>362.90 (n/a)</td><td>170.57 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 <b>(+21.89%)</b></td><td>0.03 <b>(+24.13%)</b></td><td>0.03 (+4.71%)</td><td>0.02 <b>(+392.42%)</b></td><td>0.01 (-9.50%)</td><td>494.40 <b>(-79.69%)</b></td><td>348.48 <b>(-53.49%)</b></td><td>304.70 (-4.51%)</td><td>207.20 (-17.94%)</td><td>136.08 <b>(-85.59%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2434.40 (n/a)</td><td>749.32 (n/a)</td><td>319.10 (n/a)</td><td>252.50 (n/a)</td><td>944.41 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(-20.17%)</b></td><td>0.02 <b>(-26.40%)</b></td><td>0.02 <b>(-27.82%)</b></td><td>0.01 <b>(-27.48%)</b></td><td>0.01 <b>(-21.31%)</b></td><td>753.30 <b>(+37.92%)</b></td><td>550.22 <b>(+36.37%)</b></td><td>621.40 <b>(+38.52%)</b></td><td>304.10 <b>(+25.30%)</b></td><td>177.32 <b>(+34.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.20 (n/a)</td><td>403.48 (n/a)</td><td>448.60 (n/a)</td><td>242.70 (n/a)</td><td>132.27 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (+12.04%)</td><td>0.02 <b>(-27.86%)</b></td><td>0.02 <b>(-46.05%)</b></td><td>0.02 (-13.08%)</td><td>0.01 <b>(+40.31%)</b></td><td>601.40 (+15.06%)</td><td>473.14 <b>(+45.69%)</b></td><td>523.60 <b>(+85.35%)</b></td><td>231.30 (-10.73%)</td><td>143.20 <b>(+28.80%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.70 (n/a)</td><td>324.76 (n/a)</td><td>282.50 (n/a)</td><td>259.10 (n/a)</td><td>111.18 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+5.19%)</td><td>0.03 (-11.02%)</td><td>0.02 <b>(-32.89%)</b></td><td>0.02 <b>(-21.60%)</b></td><td>0.01 <b>(+67.28%)</b></td><td>575.10 <b>(+27.54%)</b></td><td>448.90 (+18.92%)</td><td>527.80 <b>(+49.01%)</b></td><td>286.60 (-4.94%)</td><td>133.46 <b>(+95.09%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>450.90 (n/a)</td><td>377.48 (n/a)</td><td>354.20 (n/a)</td><td>301.50 (n/a)</td><td>68.41 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(+27.51%)</b></td><td>0.02 (+6.14%)</td><td>0.02 (-5.01%)</td><td>0.02 (+1.59%)</td><td>0.01 <b>(+77.83%)</b></td><td>623.60 (-1.56%)</td><td>503.96 (-2.43%)</td><td>519.20 (+5.27%)</td><td>325.50 <b>(-21.57%)</b></td><td>127.73 <b>(+39.29%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>633.50 (n/a)</td><td>516.52 (n/a)</td><td>493.20 (n/a)</td><td>415.00 (n/a)</td><td>91.70 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(-33.23%)</b></td><td>0.02 <b>(-31.41%)</b></td><td>0.02 <b>(-27.82%)</b></td><td>0.02 (-19.41%)</td><td>0.00 <b>(-36.57%)</b></td><td>575.50 <b>(+24.08%)</b></td><td>472.10 <b>(+44.33%)</b></td><td>434.80 <b>(+38.52%)</b></td><td>380.10 <b>(+49.76%)</b></td><td>94.60 (+16.88%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>463.80 (n/a)</td><td>327.10 (n/a)</td><td>313.90 (n/a)</td><td>253.80 (n/a)</td><td>80.93 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (+1.46%)</td><td>0.06 (-7.61%)</td><td>0.07 (+0.47%)</td><td>0.03 <b>(-24.12%)</b></td><td>0.03 <b>(+40.74%)</b></td><td>708.10 <b>(+31.76%)</b></td><td>400.42 (+19.20%)</td><td>299.40 (-0.47%)</td><td>235.60 (-1.46%)</td><td>200.36 <b>(+71.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>537.40 (n/a)</td><td>335.92 (n/a)</td><td>300.80 (n/a)</td><td>239.10 (n/a)</td><td>116.89 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-10.34%)</td><td>0.05 (-18.03%)</td><td>0.04 <b>(-42.98%)</b></td><td>0.04 <b>(+21.07%)</b></td><td>0.01 <b>(-32.08%)</b></td><td>528.70 (-17.42%)</td><td>433.78 (+13.85%)</td><td>495.80 <b>(+75.38%)</b></td><td>283.60 (+11.52%)</td><td>108.66 <b>(-34.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>640.20 (n/a)</td><td>381.00 (n/a)</td><td>282.70 (n/a)</td><td>254.30 (n/a)</td><td>166.81 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 <b>(+50.17%)</b></td><td>0.06 <b>(+55.85%)</b></td><td>0.05 <b>(+20.54%)</b></td><td>0.03 <b>(+187.13%)</b></td><td>0.03 <b>(+45.08%)</b></td><td>679.70 <b>(-65.17%)</b></td><td>419.86 <b>(-46.44%)</b></td><td>449.40 (-17.04%)</td><td>192.60 <b>(-33.40%)</b></td><td>194.05 <b>(-70.77%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1951.50 (n/a)</td><td>783.86 (n/a)</td><td>541.70 (n/a)</td><td>289.20 (n/a)</td><td>663.77 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 <b>(-36.04%)</b></td><td>0.04 <b>(-20.18%)</b></td><td>0.04 (-7.08%)</td><td>0.02 <b>(-27.79%)</b></td><td>0.01 <b>(-37.92%)</b></td><td>1037.60 <b>(+38.49%)</b></td><td>601.58 <b>(+24.57%)</b></td><td>510.00 (+7.62%)</td><td>420.50 <b>(+56.38%)</b></td><td>250.16 <b>(+44.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>749.20 (n/a)</td><td>482.94 (n/a)</td><td>473.90 (n/a)</td><td>268.90 (n/a)</td><td>172.61 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (+10.10%)</td><td>0.06 (-15.13%)</td><td>0.05 <b>(-23.72%)</b></td><td>0.03 <b>(-28.87%)</b></td><td>0.02 <b>(+114.17%)</b></td><td>603.00 <b>(+40.59%)</b></td><td>423.96 <b>(+30.39%)</b></td><td>394.20 <b>(+31.09%)</b></td><td>258.40 (-9.17%)</td><td>163.36 <b>(+174.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>428.90 (n/a)</td><td>325.14 (n/a)</td><td>300.70 (n/a)</td><td>284.50 (n/a)</td><td>59.61 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 <b>(+32.61%)</b></td><td>0.06 <b>(+34.73%)</b></td><td>0.04 (+6.10%)</td><td>0.04 <b>(+36.15%)</b></td><td>0.03 <b>(+56.04%)</b></td><td>493.00 <b>(-26.56%)</b></td><td>386.84 <b>(-22.76%)</b></td><td>479.60 (-5.76%)</td><td>216.90 <b>(-24.61%)</b></td><td>134.73 (-5.01%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>671.30 (n/a)</td><td>500.82 (n/a)</td><td>508.90 (n/a)</td><td>287.70 (n/a)</td><td>141.84 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>323.40 (n/a)</td><td>281.80 (n/a)</td><td>259.80 (n/a)</td><td>94.92 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.20 (n/a)</td><td>419.10 (n/a)</td><td>493.40 (n/a)</td><td>203.00 (n/a)</td><td>176.70 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1048.00 (n/a)</td><td>627.96 (n/a)</td><td>659.50 (n/a)</td><td>198.70 (n/a)</td><td>304.18 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.50 (n/a)</td><td>465.84 (n/a)</td><td>431.50 (n/a)</td><td>289.80 (n/a)</td><td>127.20 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.90 (n/a)</td><td>391.08 (n/a)</td><td>454.40 (n/a)</td><td>228.90 (n/a)</td><td>126.45 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1934.60 (n/a)</td><td>729.64 (n/a)</td><td>450.40 (n/a)</td><td>369.20 (n/a)</td><td>675.54 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>591.20 (n/a)</td><td>405.98 (n/a)</td><td>357.10 (n/a)</td><td>269.80 (n/a)</td><td>146.58 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>692.20 (n/a)</td><td>442.94 (n/a)</td><td>405.30 (n/a)</td><td>230.40 (n/a)</td><td>180.93 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>617.00 (n/a)</td><td>447.30 (n/a)</td><td>495.80 (n/a)</td><td>213.40 (n/a)</td><td>159.26 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.18 <b>(-25.21%)</b></td><td>0.16 (+9.22%)</td><td>0.17 <b>(+29.98%)</b></td><td>0.12 <b>(+50.12%)</b></td><td>0.02 <b>(-67.51%)</b></td><td>415.80 <b>(-33.38%)</b></td><td>316.04 <b>(-23.51%)</b></td><td>297.50 <b>(-23.07%)</b></td><td>277.00 <b>(+33.69%)</b></td><td>56.52 <b>(-71.19%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>624.10 (n/a)</td><td>413.18 (n/a)</td><td>386.70 (n/a)</td><td>207.20 (n/a)</td><td>196.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>601.30 (n/a)</td><td>438.06 (n/a)</td><td>483.40 (n/a)</td><td>252.30 (n/a)</td><td>158.59 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>652.10 (n/a)</td><td>553.76 (n/a)</td><td>624.60 (n/a)</td><td>403.70 (n/a)</td><td>121.77 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>369.70 (n/a)</td><td>288.44 (n/a)</td><td>274.30 (n/a)</td><td>245.80 (n/a)</td><td>51.51 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.40 (n/a)</td><td>307.84 (n/a)</td><td>276.60 (n/a)</td><td>234.80 (n/a)</td><td>113.35 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>501.80 (n/a)</td><td>361.86 (n/a)</td><td>361.00 (n/a)</td><td>245.20 (n/a)</td><td>113.99 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.70 (n/a)</td><td>329.58 (n/a)</td><td>289.60 (n/a)</td><td>221.70 (n/a)</td><td>116.89 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.00 (n/a)</td><td>401.92 (n/a)</td><td>457.20 (n/a)</td><td>238.60 (n/a)</td><td>138.38 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1115.70 (n/a)</td><td>629.38 (n/a)</td><td>562.00 (n/a)</td><td>249.70 (n/a)</td><td>339.59 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>412.90 (n/a)</td><td>307.14 (n/a)</td><td>298.30 (n/a)</td><td>258.30 (n/a)</td><td>62.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>476.50 (n/a)</td><td>365.48 (n/a)</td><td>435.20 (n/a)</td><td>215.80 (n/a)</td><td>125.32 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1941.50 (n/a)</td><td>634.90 (n/a)</td><td>271.00 (n/a)</td><td>243.40 (n/a)</td><td>735.11 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>484.70 (n/a)</td><td>317.30 (n/a)</td><td>290.40 (n/a)</td><td>232.90 (n/a)</td><td>97.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1967.40 (n/a)</td><td>823.64 (n/a)</td><td>549.80 (n/a)</td><td>504.80 (n/a)</td><td>639.76 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>453.10 (n/a)</td><td>348.74 (n/a)</td><td>330.40 (n/a)</td><td>268.20 (n/a)</td><td>80.66 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>482.90 (n/a)</td><td>376.74 (n/a)</td><td>407.60 (n/a)</td><td>231.00 (n/a)</td><td>110.43 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.80 (n/a)</td><td>325.60 (n/a)</td><td>291.40 (n/a)</td><td>223.40 (n/a)</td><td>108.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.80 (n/a)</td><td>418.44 (n/a)</td><td>449.60 (n/a)</td><td>248.40 (n/a)</td><td>146.61 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.50 (n/a)</td><td>400.16 (n/a)</td><td>376.90 (n/a)</td><td>260.30 (n/a)</td><td>127.25 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>703.70 (n/a)</td><td>510.38 (n/a)</td><td>532.80 (n/a)</td><td>304.50 (n/a)</td><td>169.15 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>417.10 (n/a)</td><td>312.76 (n/a)</td><td>311.10 (n/a)</td><td>187.00 (n/a)</td><td>86.51 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.40 (n/a)</td><td>422.10 (n/a)</td><td>394.60 (n/a)</td><td>252.10 (n/a)</td><td>158.57 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.10 (n/a)</td><td>390.26 (n/a)</td><td>423.00 (n/a)</td><td>189.30 (n/a)</td><td>151.38 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.20 (n/a)</td><td>378.88 (n/a)</td><td>433.80 (n/a)</td><td>165.40 (n/a)</td><td>146.95 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.10 (n/a)</td><td>419.52 (n/a)</td><td>427.60 (n/a)</td><td>270.40 (n/a)</td><td>132.73 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1792.80 (n/a)</td><td>727.12 (n/a)</td><td>550.20 (n/a)</td><td>223.30 (n/a)</td><td>612.40 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.60 (n/a)</td><td>433.28 (n/a)</td><td>432.70 (n/a)</td><td>245.80 (n/a)</td><td>154.26 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>593.30 (n/a)</td><td>413.60 (n/a)</td><td>395.20 (n/a)</td><td>301.60 (n/a)</td><td>123.24 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>452.50 (n/a)</td><td>306.74 (n/a)</td><td>297.90 (n/a)</td><td>191.00 (n/a)</td><td>93.52 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1093.10 (n/a)</td><td>485.66 (n/a)</td><td>319.50 (n/a)</td><td>181.00 (n/a)</td><td>371.10 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>685.20 (n/a)</td><td>354.98 (n/a)</td><td>272.90 (n/a)</td><td>185.50 (n/a)</td><td>199.57 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>586.40 (n/a)</td><td>433.72 (n/a)</td><td>380.20 (n/a)</td><td>328.10 (n/a)</td><td>115.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>688.50 (n/a)</td><td>441.16 (n/a)</td><td>472.50 (n/a)</td><td>270.00 (n/a)</td><td>167.66 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>682.10 (n/a)</td><td>407.54 (n/a)</td><td>356.10 (n/a)</td><td>258.40 (n/a)</td><td>171.23 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>318.60 (n/a)</td><td>279.26 (n/a)</td><td>287.50 (n/a)</td><td>250.70 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>618.40 (n/a)</td><td>455.42 (n/a)</td><td>467.90 (n/a)</td><td>290.00 (n/a)</td><td>135.52 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>582.30 (n/a)</td><td>408.80 (n/a)</td><td>419.50 (n/a)</td><td>241.20 (n/a)</td><td>153.11 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>539.60 (n/a)</td><td>436.24 (n/a)</td><td>392.40 (n/a)</td><td>336.40 (n/a)</td><td>95.03 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.64 (+9.91%)</td><td>0.31 <b>(-23.29%)</b></td><td>0.30 (-17.90%)</td><td>0.12 <b>(-27.23%)</b></td><td>0.21 <b>(+26.55%)</b></td><td>1783.80 <b>(+37.43%)</b></td><td>1048.76 <b>(+56.35%)</b></td><td>733.10 <b>(+21.80%)</b></td><td>348.30 (-9.01%)</td><td>658.45 <b>(+77.81%)</b></td><td>27.10 (+9.91%)</td><td>13.02 <b>(-23.29%)</b></td><td>12.87 (-17.90%)</td><td>5.29 <b>(-27.23%)</b></td><td>8.89 <b>(+26.55%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.58 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>1298.00 (n/a)</td><td>670.78 (n/a)</td><td>601.90 (n/a)</td><td>382.80 (n/a)</td><td>370.31 (n/a)</td><td>24.65 (n/a)</td><td>16.97 (n/a)</td><td>15.68 (n/a)</td><td>7.27 (n/a)</td><td>7.03 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.47 <b>(-28.39%)</b></td><td>0.39 (-16.24%)</td><td>0.39 (-13.41%)</td><td>0.33 (-6.12%)</td><td>0.06 <b>(-47.83%)</b></td><td>675.20 (+6.52%)</td><td>575.08 (+16.52%)</td><td>570.10 (+15.50%)</td><td>466.40 <b>(+39.64%)</b></td><td>87.50 (-18.54%)</td><td>20.23 <b>(-28.39%)</b></td><td>16.72 (-16.24%)</td><td>16.55 (-13.41%)</td><td>13.98 (-6.12%)</td><td>2.60 <b>(-47.83%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.66 (n/a)</td><td>0.47 (n/a)</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>633.90 (n/a)</td><td>493.56 (n/a)</td><td>493.60 (n/a)</td><td>334.00 (n/a)</td><td>107.41 (n/a)</td><td>28.25 (n/a)</td><td>19.97 (n/a)</td><td>19.12 (n/a)</td><td>14.89 (n/a)</td><td>4.98 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.30 (-0.63%)</td><td>0.30 (+0.19%)</td><td>0.30 (-0.39%)</td><td>0.30 (+1.80%)</td><td>0.00 <b>(-56.03%)</b></td><td>84396.70 (-1.77%)</td><td>83557.40 (-0.22%)</td><td>83505.60 (+0.39%)</td><td>82602.20 (+0.64%)</td><td>727.84 <b>(-56.51%)</b></td><td>207.98 (-0.63%)</td><td>205.62 (+0.19%)</td><td>205.73 (-0.39%)</td><td>203.56 (+1.80%)</td><td>1.79 <b>(-56.03%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85918.90 (n/a)</td><td>83740.02 (n/a)</td><td>83180.90 (n/a)</td><td>82078.30 (n/a)</td><td>1673.53 (n/a)</td><td>209.31 (n/a)</td><td>205.22 (n/a)</td><td>206.54 (n/a)</td><td>199.95 (n/a)</td><td>4.08 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>1.03 (-0.09%)</td><td>1.00 (-0.35%)</td><td>1.01 (+0.14%)</td><td>0.97 (-0.82%)</td><td>0.03 <b>(+50.40%)</b></td><td>25861.10 (+0.82%)</td><td>25129.42 (+0.38%)</td><td>25028.70 (-0.14%)</td><td>24381.20 (+0.09%)</td><td>697.11 <b>(+52.45%)</b></td><td>704.64 (-0.09%)</td><td>684.08 (-0.35%)</td><td>686.41 (+0.14%)</td><td>664.31 (-0.82%)</td><td>18.94 <b>(+50.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25649.70 (n/a)</td><td>25033.34 (n/a)</td><td>25064.20 (n/a)</td><td>24359.40 (n/a)</td><td>457.29 (n/a)</td><td>705.27 (n/a)</td><td>686.46 (n/a)</td><td>685.43 (n/a)</td><td>669.79 (n/a)</td><td>12.59 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.82 (-1.14%)</td><td>0.81 (-1.03%)</td><td>0.81 (-2.18%)</td><td>0.79 (+0.43%)</td><td>0.01 <b>(-35.02%)</b></td><td>95164.70 (-0.42%)</td><td>93716.06 (+1.02%)</td><td>93785.20 (+2.23%)</td><td>92559.40 (+1.15%)</td><td>1152.82 <b>(-34.60%)</b></td><td>742.44 (-1.14%)</td><td>733.36 (-1.03%)</td><td>732.73 (-2.18%)</td><td>722.11 (+0.43%)</td><td>9.01 <b>(-35.02%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.02 (n/a)</td><td>95569.70 (n/a)</td><td>92768.46 (n/a)</td><td>91742.00 (n/a)</td><td>91507.00 (n/a)</td><td>1762.71 (n/a)</td><td>750.98 (n/a)</td><td>740.97 (n/a)</td><td>749.05 (n/a)</td><td>719.05 (n/a)</td><td>13.87 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.77 (-0.71%)</td><td>0.76 (-1.24%)</td><td>0.76 (-1.46%)</td><td>0.75 (-0.53%)</td><td>0.01 (-14.94%)</td><td>101015.50 (+0.53%)</td><td>99626.98 (+1.25%)</td><td>99545.80 (+1.48%)</td><td>98224.70 (+0.71%)</td><td>1042.29 (-13.98%)</td><td>699.62 (-0.71%)</td><td>689.83 (-1.24%)</td><td>690.33 (-1.46%)</td><td>680.29 (-0.53%)</td><td>7.22 (-14.94%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100482.70 (n/a)</td><td>98393.80 (n/a)</td><td>98093.30 (n/a)</td><td>97531.00 (n/a)</td><td>1211.70 (n/a)</td><td>704.59 (n/a)</td><td>698.50 (n/a)</td><td>700.55 (n/a)</td><td>683.89 (n/a)</td><td>8.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.80 (-0.51%)</td><td>0.80 (+0.84%)</td><td>0.80 (+0.39%)</td><td>0.80 (+2.31%)</td><td>0.00 <b>(-88.48%)</b></td><td>94677.50 (-2.26%)</td><td>94447.16 (-0.85%)</td><td>94343.10 (-0.38%)</td><td>94327.70 (+0.51%)</td><td>159.93 <b>(-88.70%)</b></td><td>728.52 (-0.51%)</td><td>727.60 (+0.84%)</td><td>728.40 (+0.39%)</td><td>725.83 (+2.31%)</td><td>1.23 <b>(-88.48%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96866.20 (n/a)</td><td>95261.30 (n/a)</td><td>94707.40 (n/a)</td><td>93847.80 (n/a)</td><td>1415.60 (n/a)</td><td>732.24 (n/a)</td><td>721.51 (n/a)</td><td>725.60 (n/a)</td><td>709.43 (n/a)</td><td>10.68 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>5.46 <b>(+30.04%)</b></td><td>4.50 <b>(+33.18%)</b></td><td>4.09 (+6.14%)</td><td>3.61 <b>(+65.18%)</b></td><td>0.82 (-6.94%)</td><td>2466.20 <b>(-39.46%)</b></td><td>2033.94 <b>(-27.71%)</b></td><td>2179.50 (-5.78%)</td><td>1632.80 <b>(-23.10%)</b></td><td>358.47 <b>(-57.52%)</b></td><td>328.81 <b>(+30.04%)</b></td><td>270.86 <b>(+33.18%)</b></td><td>246.33 (+6.14%)</td><td>217.69 <b>(+65.18%)</b></td><td>49.19 (-6.94%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.20 (n/a)</td><td>3.38 (n/a)</td><td>3.85 (n/a)</td><td>2.19 (n/a)</td><td>0.88 (n/a)</td><td>4073.80 (n/a)</td><td>2813.62 (n/a)</td><td>2313.30 (n/a)</td><td>2123.20 (n/a)</td><td>843.94 (n/a)</td><td>252.86 (n/a)</td><td>203.38 (n/a)</td><td>232.08 (n/a)</td><td>131.78 (n/a)</td><td>52.85 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>4.30 (-17.22%)</td><td>3.24 (-10.41%)</td><td>2.78 (-4.57%)</td><td>2.16 (-12.59%)</td><td>0.94 <b>(-21.69%)</b></td><td>4127.10 (+14.40%)</td><td>2949.76 (+9.99%)</td><td>3203.60 (+4.79%)</td><td>2073.00 <b>(+20.81%)</b></td><td>857.57 (+5.16%)</td><td>258.99 (-17.22%)</td><td>195.02 (-10.41%)</td><td>167.59 (-4.57%)</td><td>130.08 (-12.59%)</td><td>56.90 <b>(-21.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.19 (n/a)</td><td>3.61 (n/a)</td><td>2.92 (n/a)</td><td>2.47 (n/a)</td><td>1.21 (n/a)</td><td>3607.50 (n/a)</td><td>2681.74 (n/a)</td><td>3057.30 (n/a)</td><td>1715.90 (n/a)</td><td>815.51 (n/a)</td><td>312.88 (n/a)</td><td>217.69 (n/a)</td><td>175.60 (n/a)</td><td>148.82 (n/a)</td><td>72.66 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.96 <b>(-28.74%)</b></td><td>3.19 <b>(-22.55%)</b></td><td>2.89 (-14.89%)</td><td>2.44 (-17.01%)</td><td>0.67 <b>(-48.26%)</b></td><td>3647.10 <b>(+20.50%)</b></td><td>2898.22 <b>(+23.99%)</b></td><td>3079.50 (+17.50%)</td><td>2252.10 <b>(+40.34%)</b></td><td>597.72 (-11.72%)</td><td>238.39 <b>(-28.74%)</b></td><td>191.89 <b>(-22.55%)</b></td><td>174.34 (-14.89%)</td><td>147.21 (-17.01%)</td><td>40.54 <b>(-48.26%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.55 (n/a)</td><td>4.11 (n/a)</td><td>3.40 (n/a)</td><td>2.94 (n/a)</td><td>1.30 (n/a)</td><td>3026.70 (n/a)</td><td>2337.48 (n/a)</td><td>2620.80 (n/a)</td><td>1604.80 (n/a)</td><td>677.05 (n/a)</td><td>334.54 (n/a)</td><td>247.76 (n/a)</td><td>204.85 (n/a)</td><td>177.38 (n/a)</td><td>78.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>5.79 (-11.13%)</td><td>5.27 (-5.82%)</td><td>5.48 (-12.77%)</td><td>4.48 (+5.17%)</td><td>0.57 <b>(-46.66%)</b></td><td>7789.10 (-4.92%)</td><td>6678.08 (+3.82%)</td><td>6365.40 (+14.64%)</td><td>6022.70 (+12.52%)</td><td>766.96 <b>(-42.88%)</b></td><td>356.56 (-11.13%)</td><td>324.82 (-5.82%)</td><td>337.37 (-12.77%)</td><td>275.70 (+5.17%)</td><td>35.41 <b>(-46.66%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.51 (n/a)</td><td>5.60 (n/a)</td><td>6.28 (n/a)</td><td>4.26 (n/a)</td><td>1.08 (n/a)</td><td>8192.00 (n/a)</td><td>6432.66 (n/a)</td><td>5552.40 (n/a)</td><td>5352.50 (n/a)</td><td>1342.60 (n/a)</td><td>401.21 (n/a)</td><td>344.91 (n/a)</td><td>386.77 (n/a)</td><td>262.14 (n/a)</td><td>66.38 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.09 <b>(+31.51%)</b></td><td>5.20 <b>(+35.38%)</b></td><td>5.35 <b>(+30.56%)</b></td><td>4.39 <b>(+45.84%)</b></td><td>0.72 (+11.00%)</td><td>7951.00 <b>(-31.43%)</b></td><td>6812.46 <b>(-26.76%)</b></td><td>6519.40 <b>(-23.41%)</b></td><td>5723.00 <b>(-23.96%)</b></td><td>960.09 <b>(-41.89%)</b></td><td>375.23 <b>(+31.51%)</b></td><td>320.24 <b>(+35.38%)</b></td><td>329.40 <b>(+30.56%)</b></td><td>270.09 <b>(+45.84%)</b></td><td>44.56 (+11.00%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.63 (n/a)</td><td>3.84 (n/a)</td><td>4.10 (n/a)</td><td>3.01 (n/a)</td><td>0.65 (n/a)</td><td>11595.90 (n/a)</td><td>9301.48 (n/a)</td><td>8511.90 (n/a)</td><td>7526.20 (n/a)</td><td>1652.06 (n/a)</td><td>285.33 (n/a)</td><td>236.54 (n/a)</td><td>252.29 (n/a)</td><td>185.19 (n/a)</td><td>40.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.73 (-0.87%)</td><td>5.46 (-8.11%)</td><td>5.44 (-15.21%)</td><td>4.54 (-6.82%)</td><td>0.84 (-6.75%)</td><td>7682.00 (+7.32%)</td><td>6504.12 (+8.67%)</td><td>6405.00 (+17.94%)</td><td>5182.20 (+0.87%)</td><td>956.73 (-0.08%)</td><td>414.40 (-0.87%)</td><td>336.21 (-8.11%)</td><td>335.28 (-15.21%)</td><td>279.55 (-6.82%)</td><td>51.76 (-6.75%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.79 (n/a)</td><td>5.94 (n/a)</td><td>6.42 (n/a)</td><td>4.87 (n/a)</td><td>0.90 (n/a)</td><td>7158.20 (n/a)</td><td>5985.08 (n/a)</td><td>5430.90 (n/a)</td><td>5137.40 (n/a)</td><td>957.46 (n/a)</td><td>418.01 (n/a)</td><td>365.90 (n/a)</td><td>395.42 (n/a)</td><td>300.00 (n/a)</td><td>55.50 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.77 (-1.15%)</td><td>0.76 (-0.13%)</td><td>0.76 (-0.05%)</td><td>0.76 (+0.56%)</td><td>0.00 <b>(-54.81%)</b></td><td>99388.00 (-0.56%)</td><td>98749.26 (+0.12%)</td><td>98887.30 (+0.05%)</td><td>97668.70 (+1.16%)</td><td>640.58 <b>(-54.66%)</b></td><td>703.60 (-1.15%)</td><td>695.92 (-0.13%)</td><td>694.93 (-0.05%)</td><td>691.43 (+0.56%)</td><td>4.54 <b>(-54.81%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99947.00 (n/a)</td><td>98629.16 (n/a)</td><td>98835.00 (n/a)</td><td>96545.80 (n/a)</td><td>1412.77 (n/a)</td><td>711.78 (n/a)</td><td>696.86 (n/a)</td><td>695.30 (n/a)</td><td>687.56 (n/a)</td><td>10.05 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.77 (-0.15%)</td><td>0.75 (-0.18%)</td><td>0.76 (-0.58%)</td><td>0.73 (+1.11%)</td><td>0.02 (-19.05%)</td><td>103614.10 (-1.10%)</td><td>100152.54 (+0.16%)</td><td>99467.40 (+0.59%)</td><td>98002.80 (+0.15%)</td><td>2231.67 <b>(-20.01%)</b></td><td>701.20 (-0.15%)</td><td>686.42 (-0.18%)</td><td>690.87 (-0.58%)</td><td>663.23 (+1.11%)</td><td>15.08 (-19.05%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>104762.80 (n/a)</td><td>99995.42 (n/a)</td><td>98887.20 (n/a)</td><td>97853.70 (n/a)</td><td>2789.77 (n/a)</td><td>702.27 (n/a)</td><td>687.64 (n/a)</td><td>694.93 (n/a)</td><td>655.95 (n/a)</td><td>18.63 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.81 (-0.44%)</td><td>0.80 (-0.29%)</td><td>0.80 (-0.17%)</td><td>0.79 (-0.52%)</td><td>0.01 (+3.34%)</td><td>95905.80 (+0.52%)</td><td>94177.64 (+0.29%)</td><td>93914.60 (+0.17%)</td><td>93200.60 (+0.44%)</td><td>1016.90 (+4.48%)</td><td>737.33 (-0.44%)</td><td>729.75 (-0.29%)</td><td>731.72 (-0.17%)</td><td>716.53 (-0.52%)</td><td>7.80 (+3.34%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95411.00 (n/a)</td><td>93904.70 (n/a)</td><td>93751.30 (n/a)</td><td>92794.20 (n/a)</td><td>973.34 (n/a)</td><td>740.56 (n/a)</td><td>731.86 (n/a)</td><td>733.00 (n/a)</td><td>720.25 (n/a)</td><td>7.55 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.82 (+1.91%)</td><td>2.77 <b>(+24.51%)</b></td><td>2.45 <b>(+41.01%)</b></td><td>1.82 (+16.89%)</td><td>0.82 (-9.95%)</td><td>4418.10 (-14.45%)</td><td>3119.04 <b>(-22.26%)</b></td><td>3286.10 <b>(-29.09%)</b></td><td>2111.20 (-1.88%)</td><td>919.66 <b>(-25.38%)</b></td><td>1001.28 (+1.91%)</td><td>727.11 <b>(+24.51%)</b></td><td>643.28 <b>(+41.01%)</b></td><td>478.47 (+16.89%)</td><td>213.99 (-9.95%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.75 (n/a)</td><td>2.23 (n/a)</td><td>1.74 (n/a)</td><td>1.56 (n/a)</td><td>0.91 (n/a)</td><td>5164.40 (n/a)</td><td>4011.94 (n/a)</td><td>4634.00 (n/a)</td><td>2151.60 (n/a)</td><td>1232.42 (n/a)</td><td>982.49 (n/a)</td><td>583.97 (n/a)</td><td>456.18 (n/a)</td><td>409.33 (n/a)</td><td>237.65 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.22 <b>(-22.74%)</b></td><td>0.20 (+4.46%)</td><td>0.21 (+0.62%)</td><td>0.19 <b>(+69.01%)</b></td><td>0.01 <b>(-84.94%)</b></td><td>6435.70 <b>(-40.83%)</b></td><td>6116.78 (-11.99%)</td><td>6013.80 (-0.61%)</td><td>5775.30 <b>(+29.43%)</b></td><td>271.91 <b>(-88.77%)</b></td><td>11.62 <b>(-22.74%)</b></td><td>10.99 (+4.46%)</td><td>11.16 (+0.62%)</td><td>10.43 <b>(+69.01%)</b></td><td>0.49 <b>(-84.94%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>10876.70 (n/a)</td><td>6950.02 (n/a)</td><td>6050.90 (n/a)</td><td>4462.10 (n/a)</td><td>2422.28 (n/a)</td><td>15.04 (n/a)</td><td>10.52 (n/a)</td><td>11.09 (n/a)</td><td>6.17 (n/a)</td><td>3.24 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.79 (n/a)</td><td>3.53 (n/a)</td><td>3.38 (n/a)</td><td>3.35 (n/a)</td><td>0.23 (n/a)</td><td>3.79 (n/a)</td><td>3.53 (n/a)</td><td>3.37 (n/a)</td><td>3.34 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.92 (-8.67%)</td><td>6.49 (-2.53%)</td><td>6.59 (+0.14%)</td><td>5.75 (-1.07%)</td><td>0.47 <b>(-29.75%)</b></td><td>6.92 (-8.67%)</td><td>6.48 (-2.53%)</td><td>6.59 (+0.14%)</td><td>5.75 (-1.07%)</td><td>0.47 <b>(-29.75%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>7.58 (n/a)</td><td>6.65 (n/a)</td><td>6.58 (n/a)</td><td>5.81 (n/a)</td><td>0.68 (n/a)</td><td>7.57 (n/a)</td><td>6.65 (n/a)</td><td>6.58 (n/a)</td><td>5.81 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>10.90 <b>(-20.62%)</b></td><td>8.65 <b>(-21.90%)</b></td><td>8.29 <b>(-29.14%)</b></td><td>7.55 (-11.96%)</td><td>1.31 <b>(-40.67%)</b></td><td>10.89 <b>(-20.62%)</b></td><td>8.65 <b>(-21.90%)</b></td><td>8.29 <b>(-29.14%)</b></td><td>7.55 (-11.96%)</td><td>1.30 <b>(-40.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>13.73 (n/a)</td><td>11.08 (n/a)</td><td>11.70 (n/a)</td><td>8.58 (n/a)</td><td>2.20 (n/a)</td><td>13.72 (n/a)</td><td>11.07 (n/a)</td><td>11.70 (n/a)</td><td>8.57 (n/a)</td><td>2.20 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.86 (n/a)</td><td>3.68 (n/a)</td><td>3.66 (n/a)</td><td>3.55 (n/a)</td><td>0.12 (n/a)</td><td>3.86 (n/a)</td><td>3.68 (n/a)</td><td>3.66 (n/a)</td><td>3.54 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.92 (+1.39%)</td><td>6.49 (+10.82%)</td><td>6.67 (+14.67%)</td><td>5.64 (+18.72%)</td><td>0.50 <b>(-33.35%)</b></td><td>6.91 (+1.39%)</td><td>6.49 (+10.82%)</td><td>6.67 (+14.67%)</td><td>5.64 (+18.72%)</td><td>0.50 <b>(-33.35%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.82 (n/a)</td><td>5.86 (n/a)</td><td>5.82 (n/a)</td><td>4.75 (n/a)</td><td>0.75 (n/a)</td><td>6.82 (n/a)</td><td>5.86 (n/a)</td><td>5.82 (n/a)</td><td>4.75 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>11.60 (-17.94%)</td><td>9.20 (-3.44%)</td><td>8.57 (+1.02%)</td><td>7.94 (+7.83%)</td><td>1.53 <b>(-45.32%)</b></td><td>11.59 (-17.94%)</td><td>9.20 (-3.44%)</td><td>8.56 (+1.02%)</td><td>7.94 (+7.83%)</td><td>1.53 <b>(-45.32%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>14.13 (n/a)</td><td>9.53 (n/a)</td><td>8.48 (n/a)</td><td>7.36 (n/a)</td><td>2.80 (n/a)</td><td>14.13 (n/a)</td><td>9.52 (n/a)</td><td>8.48 (n/a)</td><td>7.36 (n/a)</td><td>2.80 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.96 (-0.96%)</td><td>2.34 (-4.19%)</td><td>2.71 (-1.88%)</td><td>1.18 (+6.12%)</td><td>0.73 (-4.00%)</td><td>2.96 (-0.96%)</td><td>2.34 (-4.19%)</td><td>2.71 (-1.88%)</td><td>1.17 (+6.12%)</td><td>0.73 (-4.00%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.99 (n/a)</td><td>2.44 (n/a)</td><td>2.76 (n/a)</td><td>1.11 (n/a)</td><td>0.76 (n/a)</td><td>2.98 (n/a)</td><td>2.44 (n/a)</td><td>2.76 (n/a)</td><td>1.11 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.56 (+5.19%)</td><td>0.32 (+11.28%)</td><td>0.32 (-12.62%)</td><td>0.08 (-2.63%)</td><td>0.18 (-13.77%)</td><td>0.55 (+5.19%)</td><td>0.32 (+11.28%)</td><td>0.31 (-12.62%)</td><td>0.08 (-2.63%)</td><td>0.17 (-13.77%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.53 (n/a)</td><td>0.29 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.52 (n/a)</td><td>0.29 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.81 (+12.82%)</td><td>0.32 <b>(-37.74%)</b></td><td>0.29 <b>(-41.53%)</b></td><td>0.08 <b>(-77.28%)</b></td><td>0.30 <b>(+75.14%)</b></td><td>0.80 (+12.82%)</td><td>0.32 <b>(-37.74%)</b></td><td>0.29 <b>(-41.53%)</b></td><td>0.08 <b>(-77.28%)</b></td><td>0.29 <b>(+75.14%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.72 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td><td>0.71 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.04 (-18.00%)</td><td>1.46 (+10.28%)</td><td>1.58 <b>(+105.50%)</b></td><td>0.42 (-3.14%)</td><td>0.65 <b>(-30.33%)</b></td><td>2.00 (-18.00%)</td><td>1.44 (+10.28%)</td><td>1.55 <b>(+105.50%)</b></td><td>0.41 (-3.14%)</td><td>0.64 <b>(-30.33%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.48 (n/a)</td><td>1.33 (n/a)</td><td>0.77 (n/a)</td><td>0.43 (n/a)</td><td>0.93 (n/a)</td><td>2.44 (n/a)</td><td>1.30 (n/a)</td><td>0.76 (n/a)</td><td>0.43 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.00 (n/a)</td><td>375.02 (n/a)</td><td>303.50 (n/a)</td><td>281.50 (n/a)</td><td>113.33 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.90 (n/a)</td><td>311.84 (n/a)</td><td>254.60 (n/a)</td><td>236.00 (n/a)</td><td>133.72 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>642.10 (n/a)</td><td>436.32 (n/a)</td><td>479.10 (n/a)</td><td>215.60 (n/a)</td><td>197.27 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2427.80 (n/a)</td><td>855.70 (n/a)</td><td>501.70 (n/a)</td><td>311.50 (n/a)</td><td>885.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.50 (n/a)</td><td>490.98 (n/a)</td><td>534.10 (n/a)</td><td>264.60 (n/a)</td><td>133.86 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.60 (n/a)</td><td>437.96 (n/a)</td><td>465.60 (n/a)</td><td>295.40 (n/a)</td><td>104.38 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.20 (n/a)</td><td>375.78 (n/a)</td><td>278.90 (n/a)</td><td>250.30 (n/a)</td><td>149.84 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2450.80 (n/a)</td><td>783.56 (n/a)</td><td>388.10 (n/a)</td><td>255.30 (n/a)</td><td>938.27 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.70 (n/a)</td><td>317.92 (n/a)</td><td>265.00 (n/a)</td><td>162.60 (n/a)</td><td>167.66 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>411.46 (n/a)</td><td>458.50 (n/a)</td><td>268.70 (n/a)</td><td>121.38 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.20 (n/a)</td><td>347.64 (n/a)</td><td>307.00 (n/a)</td><td>214.80 (n/a)</td><td>128.75 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2401.00 (n/a)</td><td>878.48 (n/a)</td><td>617.30 (n/a)</td><td>309.40 (n/a)</td><td>861.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>505.60 (n/a)</td><td>400.96 (n/a)</td><td>462.40 (n/a)</td><td>263.30 (n/a)</td><td>114.39 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>610.60 (n/a)</td><td>494.48 (n/a)</td><td>470.00 (n/a)</td><td>382.80 (n/a)</td><td>92.40 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>536.60 (n/a)</td><td>395.00 (n/a)</td><td>437.20 (n/a)</td><td>235.70 (n/a)</td><td>119.95 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>721.20 (n/a)</td><td>422.82 (n/a)</td><td>318.90 (n/a)</td><td>248.00 (n/a)</td><td>197.73 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.00 (n/a)</td><td>397.52 (n/a)</td><td>453.00 (n/a)</td><td>222.40 (n/a)</td><td>154.88 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.30 (n/a)</td><td>441.38 (n/a)</td><td>556.30 (n/a)</td><td>211.20 (n/a)</td><td>185.53 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1921.50 (n/a)</td><td>636.12 (n/a)</td><td>324.80 (n/a)</td><td>302.40 (n/a)</td><td>718.65 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2493.90 (n/a)</td><td>853.44 (n/a)</td><td>441.10 (n/a)</td><td>304.70 (n/a)</td><td>927.64 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>290.50 (n/a)</td><td>268.52 (n/a)</td><td>273.30 (n/a)</td><td>233.20 (n/a)</td><td>22.47 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>600.90 (n/a)</td><td>419.86 (n/a)</td><td>393.60 (n/a)</td><td>317.50 (n/a)</td><td>116.29 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1904.90 (n/a)</td><td>676.28 (n/a)</td><td>303.80 (n/a)</td><td>233.90 (n/a)</td><td>711.33 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>688.40 (n/a)</td><td>464.08 (n/a)</td><td>389.00 (n/a)</td><td>258.40 (n/a)</td><td>186.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(+24.39%)</b></td><td>0.01 (-2.89%)</td><td>0.01 (-16.44%)</td><td>0.01 (-18.54%)</td><td>0.01 <b>(+62.83%)</b></td><td>555.30 <b>(+22.75%)</b></td><td>366.34 (+10.46%)</td><td>362.40 (+19.68%)</td><td>193.80 (-19.62%)</td><td>135.06 <b>(+54.98%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>452.40 (n/a)</td><td>331.64 (n/a)</td><td>302.80 (n/a)</td><td>241.10 (n/a)</td><td>87.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(+29.24%)</b></td><td>0.01 <b>(+28.51%)</b></td><td>0.01 (+18.86%)</td><td>0.01 <b>(+93.80%)</b></td><td>0.00 (+7.48%)</td><td>559.90 <b>(-48.40%)</b></td><td>451.88 <b>(-26.76%)</b></td><td>473.30 (-15.86%)</td><td>310.80 <b>(-22.63%)</b></td><td>111.00 <b>(-58.95%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1085.10 (n/a)</td><td>616.98 (n/a)</td><td>562.50 (n/a)</td><td>401.70 (n/a)</td><td>270.44 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-0.41%)</td><td>0.01 (-16.03%)</td><td>0.01 <b>(-35.53%)</b></td><td>0.01 (-8.17%)</td><td>0.00 (+12.09%)</td><td>519.10 (+8.89%)</td><td>403.88 <b>(+22.66%)</b></td><td>455.10 <b>(+55.11%)</b></td><td>240.20 (+0.42%)</td><td>130.09 <b>(+28.30%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.70 (n/a)</td><td>329.28 (n/a)</td><td>293.40 (n/a)</td><td>239.20 (n/a)</td><td>101.39 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (-8.58%)</td><td>0.01 (-2.40%)</td><td>0.01 (+14.97%)</td><td>0.01 (-14.24%)</td><td>0.00 (+5.02%)</td><td>591.60 (+16.62%)</td><td>429.76 (+5.68%)</td><td>374.80 (-13.02%)</td><td>277.10 (+9.35%)</td><td>146.54 <b>(+44.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.30 (n/a)</td><td>406.66 (n/a)</td><td>430.90 (n/a)</td><td>253.40 (n/a)</td><td>101.22 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-2.74%)</td><td>0.01 (+5.36%)</td><td>0.01 (-5.83%)</td><td>0.01 (-11.00%)</td><td>0.00 <b>(+27.46%)</b></td><td>671.60 (+12.36%)</td><td>480.72 (+1.80%)</td><td>577.00 (+6.20%)</td><td>268.70 (+2.83%)</td><td>195.15 <b>(+39.84%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.70 (n/a)</td><td>472.22 (n/a)</td><td>543.30 (n/a)</td><td>261.30 (n/a)</td><td>139.55 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(+22.71%)</b></td><td>0.01 (+6.97%)</td><td>0.01 (-3.21%)</td><td>0.01 (+0.63%)</td><td>0.00 <b>(+68.68%)</b></td><td>577.60 (-0.64%)</td><td>469.72 (-3.73%)</td><td>501.30 (+3.30%)</td><td>297.80 (-18.50%)</td><td>106.88 <b>(+34.72%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.30 (n/a)</td><td>487.94 (n/a)</td><td>485.30 (n/a)</td><td>365.40 (n/a)</td><td>79.33 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (-18.73%)</td><td>0.03 (+6.17%)</td><td>0.03 <b>(+44.75%)</b></td><td>0.02 <b>(+27.27%)</b></td><td>0.01 <b>(-42.42%)</b></td><td>453.10 <b>(-21.43%)</b></td><td>323.86 (-18.18%)</td><td>306.00 <b>(-30.91%)</b></td><td>207.10 <b>(+23.05%)</b></td><td>96.83 <b>(-44.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.70 (n/a)</td><td>395.84 (n/a)</td><td>442.90 (n/a)</td><td>168.30 (n/a)</td><td>175.83 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-13.40%)</td><td>0.02 (-16.31%)</td><td>0.02 <b>(-29.13%)</b></td><td>0.02 (-19.02%)</td><td>0.01 (+1.00%)</td><td>535.40 <b>(+23.48%)</b></td><td>392.34 <b>(+21.99%)</b></td><td>407.90 <b>(+41.09%)</b></td><td>260.90 (+15.49%)</td><td>115.40 <b>(+38.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>433.60 (n/a)</td><td>321.62 (n/a)</td><td>289.10 (n/a)</td><td>225.90 (n/a)</td><td>83.40 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-5.65%)</td><td>0.02 (+4.99%)</td><td>0.02 (+9.60%)</td><td>0.01 <b>(-27.72%)</b></td><td>0.01 (+12.93%)</td><td>785.50 <b>(+38.37%)</b></td><td>459.56 (+3.01%)</td><td>442.00 (-8.75%)</td><td>242.50 (+5.99%)</td><td>222.29 <b>(+62.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.70 (n/a)</td><td>446.12 (n/a)</td><td>484.40 (n/a)</td><td>228.80 (n/a)</td><td>137.00 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+4.26%)</td><td>0.02 (+12.78%)</td><td>0.03 <b>(+48.85%)</b></td><td>0.02 (+3.39%)</td><td>0.01 (+9.03%)</td><td>515.50 (-3.28%)</td><td>369.18 (-9.78%)</td><td>302.70 <b>(-32.82%)</b></td><td>226.80 (-4.10%)</td><td>135.21 (+10.32%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.00 (n/a)</td><td>409.22 (n/a)</td><td>450.60 (n/a)</td><td>236.50 (n/a)</td><td>122.56 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-17.70%)</td><td>0.02 (-14.15%)</td><td>0.02 (-10.69%)</td><td>0.02 (+17.23%)</td><td>0.01 <b>(-22.19%)</b></td><td>517.20 (-14.70%)</td><td>378.22 (+11.48%)</td><td>335.60 (+11.94%)</td><td>239.90 <b>(+21.53%)</b></td><td>123.60 <b>(-20.56%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.30 (n/a)</td><td>339.28 (n/a)</td><td>299.80 (n/a)</td><td>197.40 (n/a)</td><td>155.59 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(-29.84%)</b></td><td>0.02 (-14.87%)</td><td>0.02 (-18.39%)</td><td>0.01 (-8.88%)</td><td>0.01 <b>(-44.08%)</b></td><td>550.80 (+9.76%)</td><td>395.36 (+10.65%)</td><td>384.90 <b>(+22.54%)</b></td><td>276.80 <b>(+42.53%)</b></td><td>108.00 (-16.17%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.80 (n/a)</td><td>357.32 (n/a)</td><td>314.10 (n/a)</td><td>194.20 (n/a)</td><td>128.83 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-9.38%)</td><td>0.02 (-9.30%)</td><td>0.02 (-17.24%)</td><td>0.02 (+14.13%)</td><td>0.00 <b>(-31.13%)</b></td><td>496.90 (-12.38%)</td><td>428.78 (+5.20%)</td><td>441.50 <b>(+20.83%)</b></td><td>290.20 (+10.34%)</td><td>82.58 <b>(-37.44%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>407.60 (n/a)</td><td>365.40 (n/a)</td><td>263.00 (n/a)</td><td>132.00 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-10.82%)</td><td>0.02 <b>(-21.74%)</b></td><td>0.02 (+4.54%)</td><td>0.00 <b>(-70.24%)</b></td><td>0.01 (+18.88%)</td><td>1906.40 <b>(+235.99%)</b></td><td>755.34 <b>(+69.47%)</b></td><td>455.90 (-4.34%)</td><td>348.10 (+12.11%)</td><td>650.81 <b>(+408.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.40 (n/a)</td><td>445.70 (n/a)</td><td>476.60 (n/a)</td><td>310.50 (n/a)</td><td>128.01 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 <b>(+24.62%)</b></td><td>0.04 (-19.53%)</td><td>0.03 <b>(-38.07%)</b></td><td>0.02 <b>(-53.16%)</b></td><td>0.02 <b>(+627.73%)</b></td><td>674.30 <b>(+113.52%)</b></td><td>430.36 <b>(+45.42%)</b></td><td>478.70 <b>(+61.50%)</b></td><td>220.80 (-19.74%)</td><td>180.30 <b>(+1110.49%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>315.80 (n/a)</td><td>295.94 (n/a)</td><td>296.40 (n/a)</td><td>275.10 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-1.04%)</td><td>0.04 <b>(-20.43%)</b></td><td>0.03 <b>(-37.19%)</b></td><td>0.03 (-3.84%)</td><td>0.02 (-0.08%)</td><td>592.70 (+3.98%)</td><td>456.28 <b>(+25.19%)</b></td><td>474.30 <b>(+59.21%)</b></td><td>243.20 (+1.04%)</td><td>130.13 (-3.96%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.00 (n/a)</td><td>364.46 (n/a)</td><td>297.90 (n/a)</td><td>240.70 (n/a)</td><td>135.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 <b>(+22.04%)</b></td><td>0.06 <b>(+33.74%)</b></td><td>0.06 <b>(+57.14%)</b></td><td>0.04 (+13.59%)</td><td>0.01 (+13.91%)</td><td>406.40 (-11.96%)</td><td>288.52 <b>(-25.53%)</b></td><td>282.10 <b>(-36.36%)</b></td><td>210.30 (-18.08%)</td><td>74.11 (-17.97%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>461.60 (n/a)</td><td>387.44 (n/a)</td><td>443.30 (n/a)</td><td>256.70 (n/a)</td><td>90.35 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (+14.68%)</td><td>0.04 (+1.25%)</td><td>0.04 <b>(-20.48%)</b></td><td>0.02 (-12.35%)</td><td>0.02 <b>(+46.66%)</b></td><td>687.00 (+14.10%)</td><td>434.50 (+4.80%)</td><td>448.80 <b>(+25.75%)</b></td><td>266.10 (-12.78%)</td><td>171.91 <b>(+37.79%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>602.10 (n/a)</td><td>414.58 (n/a)</td><td>356.90 (n/a)</td><td>305.10 (n/a)</td><td>124.77 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-3.45%)</td><td>0.06 <b>(+45.40%)</b></td><td>0.06 <b>(+93.86%)</b></td><td>0.03 <b>(+44.63%)</b></td><td>0.01 <b>(-32.79%)</b></td><td>468.70 <b>(-30.86%)</b></td><td>311.20 <b>(-37.35%)</b></td><td>268.70 <b>(-48.41%)</b></td><td>238.50 (+3.56%)</td><td>91.89 <b>(-48.51%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>677.90 (n/a)</td><td>496.70 (n/a)</td><td>520.80 (n/a)</td><td>230.30 (n/a)</td><td>178.47 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 <b>(-44.23%)</b></td><td>0.04 (-4.91%)</td><td>0.04 (+16.72%)</td><td>0.03 <b>(+28.17%)</b></td><td>0.00 <b>(-78.29%)</b></td><td>481.80 <b>(-21.98%)</b></td><td>431.36 (-8.43%)</td><td>446.00 (-14.33%)</td><td>376.00 <b>(+79.30%)</b></td><td>50.86 <b>(-67.96%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>617.50 (n/a)</td><td>471.08 (n/a)</td><td>520.60 (n/a)</td><td>209.70 (n/a)</td><td>158.75 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-18.18%)</td><td>0.10 <b>(+21.84%)</b></td><td>0.11 <b>(+68.63%)</b></td><td>0.05 (-2.23%)</td><td>0.03 <b>(-22.64%)</b></td><td>598.40 (+2.27%)</td><td>370.30 <b>(-20.37%)</b></td><td>286.10 <b>(-40.69%)</b></td><td>266.00 <b>(+22.24%)</b></td><td>144.44 (-2.48%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>585.10 (n/a)</td><td>465.04 (n/a)</td><td>482.40 (n/a)</td><td>217.60 (n/a)</td><td>148.11 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 <b>(+33.69%)</b></td><td>0.11 (+13.88%)</td><td>0.12 <b>(+31.92%)</b></td><td>0.02 <b>(-71.43%)</b></td><td>0.07 <b>(+88.87%)</b></td><td>1891.10 <b>(+249.94%)</b></td><td>580.64 <b>(+60.91%)</b></td><td>279.10 <b>(-24.20%)</b></td><td>162.00 <b>(-25.21%)</b></td><td>734.79 <b>(+495.03%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>540.40 (n/a)</td><td>360.84 (n/a)</td><td>368.20 (n/a)</td><td>216.60 (n/a)</td><td>123.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 <b>(+29.91%)</b></td><td>0.09 (+13.38%)</td><td>0.08 (+13.05%)</td><td>0.06 (+3.34%)</td><td>0.04 <b>(+55.73%)</b></td><td>519.90 (-3.24%)</td><td>408.64 (-8.01%)</td><td>432.70 (-11.53%)</td><td>210.30 <b>(-23.05%)</b></td><td>120.28 (+11.12%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>537.30 (n/a)</td><td>444.22 (n/a)</td><td>489.10 (n/a)</td><td>273.30 (n/a)</td><td>108.24 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 <b>(-40.15%)</b></td><td>0.07 <b>(-24.40%)</b></td><td>0.07 (-12.27%)</td><td>0.06 (-1.42%)</td><td>0.01 <b>(-70.87%)</b></td><td>590.40 (+1.44%)</td><td>483.28 (+19.28%)</td><td>470.60 (+13.97%)</td><td>395.80 <b>(+67.07%)</b></td><td>75.45 <b>(-49.92%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>582.00 (n/a)</td><td>405.18 (n/a)</td><td>412.90 (n/a)</td><td>236.90 (n/a)</td><td>150.67 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 <b>(+48.10%)</b></td><td>0.09 <b>(+32.82%)</b></td><td>0.07 (+14.10%)</td><td>0.06 (+14.05%)</td><td>0.04 <b>(+91.32%)</b></td><td>518.30 (-12.33%)</td><td>393.52 <b>(-20.21%)</b></td><td>455.80 (-12.36%)</td><td>210.70 <b>(-32.49%)</b></td><td>125.69 (+18.50%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>591.20 (n/a)</td><td>493.18 (n/a)</td><td>520.10 (n/a)</td><td>312.10 (n/a)</td><td>106.07 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+7.55%)</td><td>0.01 (-7.00%)</td><td>0.02 (+9.18%)</td><td>0.01 <b>(-31.35%)</b></td><td>0.00 <b>(+167.12%)</b></td><td>505.20 <b>(+45.67%)</b></td><td>345.78 (+17.00%)</td><td>262.10 (-8.42%)</td><td>246.60 (-7.01%)</td><td>124.12 <b>(+262.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>346.80 (n/a)</td><td>295.54 (n/a)</td><td>286.20 (n/a)</td><td>265.20 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-16.15%)</td><td>0.01 (-5.01%)</td><td>0.01 (+1.93%)</td><td>0.00 <b>(-71.86%)</b></td><td>0.01 <b>(+24.03%)</b></td><td>1822.30 <b>(+255.36%)</b></td><td>647.84 <b>(+55.75%)</b></td><td>411.00 (-1.89%)</td><td>266.90 (+19.26%)</td><td>662.01 <b>(+467.45%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.80 (n/a)</td><td>415.96 (n/a)</td><td>418.90 (n/a)</td><td>223.80 (n/a)</td><td>116.66 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+9.99%)</td><td>0.01 (+3.96%)</td><td>0.01 (-5.32%)</td><td>0.01 (+16.90%)</td><td>0.00 (-5.43%)</td><td>506.00 (-14.45%)</td><td>336.64 (-7.38%)</td><td>282.40 (+5.61%)</td><td>211.00 (-9.09%)</td><td>119.74 <b>(-24.38%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.50 (n/a)</td><td>363.48 (n/a)</td><td>267.40 (n/a)</td><td>232.10 (n/a)</td><td>158.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (-12.54%)</td><td>0.01 <b>(-26.82%)</b></td><td>0.01 <b>(-45.61%)</b></td><td>0.01 (-5.20%)</td><td>0.00 (-19.18%)</td><td>552.40 (+5.48%)</td><td>483.40 <b>(+33.82%)</b></td><td>534.40 <b>(+83.83%)</b></td><td>279.80 (+14.34%)</td><td>115.29 (-7.25%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>523.70 (n/a)</td><td>361.24 (n/a)</td><td>290.70 (n/a)</td><td>244.70 (n/a)</td><td>124.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+19.29%)</td><td>0.01 <b>(+20.47%)</b></td><td>0.01 (+6.87%)</td><td>0.01 (+16.01%)</td><td>0.00 (+13.33%)</td><td>553.30 (-13.79%)</td><td>347.28 (-18.45%)</td><td>330.40 (-6.43%)</td><td>222.70 (-16.18%)</td><td>136.18 <b>(-22.72%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.80 (n/a)</td><td>425.86 (n/a)</td><td>353.10 (n/a)</td><td>265.70 (n/a)</td><td>176.21 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-14.28%)</td><td>0.01 (+17.32%)</td><td>0.01 <b>(+27.88%)</b></td><td>0.01 (+9.31%)</td><td>0.00 <b>(-31.77%)</b></td><td>489.20 (-8.51%)</td><td>325.14 (-18.08%)</td><td>289.60 <b>(-21.81%)</b></td><td>266.40 (+16.69%)</td><td>92.36 <b>(-23.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.70 (n/a)</td><td>396.88 (n/a)</td><td>370.40 (n/a)</td><td>228.30 (n/a)</td><td>120.52 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+3.54%)</td><td>0.01 (-8.27%)</td><td>0.01 (+0.14%)</td><td>0.01 (+8.61%)</td><td>0.00 (-18.25%)</td><td>561.20 (-7.92%)</td><td>434.02 (+3.37%)</td><td>426.00 (-0.14%)</td><td>243.70 (-3.41%)</td><td>123.51 <b>(-25.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.50 (n/a)</td><td>419.86 (n/a)</td><td>426.60 (n/a)</td><td>252.30 (n/a)</td><td>166.20 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(-40.30%)</b></td><td>0.01 <b>(-25.35%)</b></td><td>0.01 (-0.27%)</td><td>0.01 (-16.59%)</td><td>0.00 <b>(-64.01%)</b></td><td>589.50 (+19.89%)</td><td>493.78 <b>(+25.83%)</b></td><td>450.20 (+0.27%)</td><td>404.30 <b>(+67.55%)</b></td><td>84.99 <b>(-27.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.70 (n/a)</td><td>392.42 (n/a)</td><td>449.00 (n/a)</td><td>241.30 (n/a)</td><td>117.53 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(-34.45%)</b></td><td>0.01 <b>(-21.97%)</b></td><td>0.01 <b>(-20.43%)</b></td><td>0.01 (+10.99%)</td><td>0.00 <b>(-56.27%)</b></td><td>617.20 (-9.90%)</td><td>536.26 (+18.37%)</td><td>558.20 <b>(+25.66%)</b></td><td>373.30 <b>(+52.55%)</b></td><td>96.46 <b>(-39.75%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>685.00 (n/a)</td><td>453.02 (n/a)</td><td>444.20 (n/a)</td><td>244.70 (n/a)</td><td>160.09 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+6.16%)</td><td>0.01 (+14.76%)</td><td>0.02 <b>(+73.27%)</b></td><td>0.01 (-9.40%)</td><td>0.01 <b>(+37.30%)</b></td><td>613.50 (+10.36%)</td><td>375.90 (-5.41%)</td><td>252.70 <b>(-42.29%)</b></td><td>235.90 (-5.79%)</td><td>182.33 <b>(+44.08%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.90 (n/a)</td><td>397.38 (n/a)</td><td>437.90 (n/a)</td><td>250.40 (n/a)</td><td>126.55 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+11.33%)</td><td>0.01 (-7.88%)</td><td>0.01 (+1.60%)</td><td>0.00 <b>(-41.45%)</b></td><td>0.00 <b>(+50.83%)</b></td><td>1070.50 <b>(+70.79%)</b></td><td>571.44 <b>(+24.20%)</b></td><td>458.90 (-1.57%)</td><td>272.90 (-10.17%)</td><td>303.58 <b>(+141.47%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.80 (n/a)</td><td>460.08 (n/a)</td><td>466.20 (n/a)</td><td>303.80 (n/a)</td><td>125.73 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-9.98%)</td><td>0.01 <b>(-21.19%)</b></td><td>0.01 <b>(-23.99%)</b></td><td>0.01 (-4.39%)</td><td>0.00 (-11.73%)</td><td>538.80 (+4.58%)</td><td>448.74 <b>(+25.93%)</b></td><td>489.90 <b>(+31.55%)</b></td><td>255.20 (+11.05%)</td><td>113.95 (+0.93%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.20 (n/a)</td><td>356.34 (n/a)</td><td>372.40 (n/a)</td><td>229.80 (n/a)</td><td>112.90 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+16.36%)</td><td>0.03 <b>(+28.03%)</b></td><td>0.04 <b>(+27.06%)</b></td><td>0.02 (+11.03%)</td><td>0.01 (+19.35%)</td><td>462.10 (-9.94%)</td><td>278.50 <b>(-21.16%)</b></td><td>231.80 <b>(-21.29%)</b></td><td>227.20 (-14.07%)</td><td>102.79 (-4.87%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.10 (n/a)</td><td>353.26 (n/a)</td><td>294.50 (n/a)</td><td>264.40 (n/a)</td><td>108.05 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+13.82%)</td><td>0.02 (-2.88%)</td><td>0.03 (+2.96%)</td><td>0.01 (-9.62%)</td><td>0.01 <b>(+56.22%)</b></td><td>546.20 (+10.63%)</td><td>374.84 (+11.02%)</td><td>284.70 (-2.87%)</td><td>232.40 (-12.14%)</td><td>153.17 <b>(+62.15%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.70 (n/a)</td><td>337.62 (n/a)</td><td>293.10 (n/a)</td><td>264.50 (n/a)</td><td>94.46 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+8.95%)</td><td>0.03 <b>(+23.77%)</b></td><td>0.03 <b>(+64.42%)</b></td><td>0.02 <b>(+20.37%)</b></td><td>0.01 (-15.22%)</td><td>438.80 (-16.93%)</td><td>321.36 <b>(-22.63%)</b></td><td>292.50 <b>(-39.18%)</b></td><td>230.40 (-8.21%)</td><td>83.90 <b>(-36.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.20 (n/a)</td><td>415.36 (n/a)</td><td>480.90 (n/a)</td><td>251.00 (n/a)</td><td>131.41 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+8.99%)</td><td>0.03 (+12.71%)</td><td>0.03 (+19.88%)</td><td>0.02 (-3.66%)</td><td>0.01 <b>(+26.76%)</b></td><td>519.40 (+3.80%)</td><td>314.04 (-8.65%)</td><td>259.80 (-16.57%)</td><td>232.10 (-8.22%)</td><td>117.81 <b>(+22.71%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.40 (n/a)</td><td>343.76 (n/a)</td><td>311.40 (n/a)</td><td>252.90 (n/a)</td><td>96.01 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (-13.72%)</td><td>0.02 (-14.28%)</td><td>0.02 <b>(-36.34%)</b></td><td>0.01 (+12.19%)</td><td>0.01 (-15.67%)</td><td>588.60 (-10.86%)</td><td>432.56 (+12.14%)</td><td>470.40 <b>(+57.06%)</b></td><td>225.20 (+15.90%)</td><td>165.10 (-12.16%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.30 (n/a)</td><td>385.74 (n/a)</td><td>299.50 (n/a)</td><td>194.30 (n/a)</td><td>187.96 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 <b>(+100.17%)</b></td><td>0.03 <b>(+66.40%)</b></td><td>0.03 <b>(+54.78%)</b></td><td>0.02 (+1.20%)</td><td>0.01 <b>(+397.49%)</b></td><td>474.00 (-1.19%)</td><td>284.84 <b>(-33.60%)</b></td><td>271.50 <b>(-35.37%)</b></td><td>181.00 <b>(-50.03%)</b></td><td>114.79 <b>(+149.50%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>479.70 (n/a)</td><td>428.98 (n/a)</td><td>420.10 (n/a)</td><td>362.20 (n/a)</td><td>46.01 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 <b>(+30.81%)</b></td><td>0.02 <b>(+35.03%)</b></td><td>0.02 <b>(+29.09%)</b></td><td>0.02 (+17.13%)</td><td>0.01 <b>(+61.12%)</b></td><td>515.70 (-14.62%)</td><td>365.40 <b>(-22.82%)</b></td><td>377.30 <b>(-22.54%)</b></td><td>226.40 <b>(-23.54%)</b></td><td>127.77 (+2.51%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.00 (n/a)</td><td>473.46 (n/a)</td><td>487.10 (n/a)</td><td>296.10 (n/a)</td><td>124.65 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+8.41%)</td><td>0.03 (-3.78%)</td><td>0.03 (+2.98%)</td><td>0.02 (+13.85%)</td><td>0.01 (+17.94%)</td><td>506.80 (-12.17%)</td><td>355.42 (+4.94%)</td><td>284.10 (-2.90%)</td><td>230.40 (-7.73%)</td><td>127.13 (-5.55%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.00 (n/a)</td><td>338.68 (n/a)</td><td>292.60 (n/a)</td><td>249.70 (n/a)</td><td>134.60 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 <b>(+32.89%)</b></td><td>0.02 (+7.66%)</td><td>0.02 (+13.56%)</td><td>0.02 (+0.49%)</td><td>0.01 <b>(+30.60%)</b></td><td>541.80 (-0.48%)</td><td>402.64 (-3.97%)</td><td>433.60 (-11.94%)</td><td>196.50 <b>(-24.74%)</b></td><td>150.92 (+3.97%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>419.28 (n/a)</td><td>492.40 (n/a)</td><td>261.10 (n/a)</td><td>145.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+15.80%)</td><td>0.03 (+16.80%)</td><td>0.03 (+18.17%)</td><td>0.01 <b>(-29.96%)</b></td><td>0.01 <b>(+46.45%)</b></td><td>682.80 <b>(+42.79%)</b></td><td>333.00 (-4.40%)</td><td>252.90 (-15.39%)</td><td>206.30 (-13.65%)</td><td>197.45 <b>(+90.63%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.20 (n/a)</td><td>348.34 (n/a)</td><td>298.90 (n/a)</td><td>238.90 (n/a)</td><td>103.58 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(+22.06%)</b></td><td>0.02 <b>(-21.44%)</b></td><td>0.01 <b>(-28.77%)</b></td><td>0.00 <b>(-71.89%)</b></td><td>0.01 <b>(+117.45%)</b></td><td>1956.50 <b>(+255.73%)</b></td><td>818.00 <b>(+87.24%)</b></td><td>624.50 <b>(+40.40%)</b></td><td>240.60 (-18.08%)</td><td>658.64 <b>(+566.66%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>436.88 (n/a)</td><td>444.80 (n/a)</td><td>293.70 (n/a)</td><td>98.80 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(+35.96%)</b></td><td>0.02 <b>(+30.84%)</b></td><td>0.02 <b>(+38.22%)</b></td><td>0.02 (+1.32%)</td><td>0.00 <b>(+120.70%)</b></td><td>519.00 (-1.29%)</td><td>365.52 <b>(-21.22%)</b></td><td>335.30 <b>(-27.64%)</b></td><td>280.50 <b>(-26.46%)</b></td><td>90.69 <b>(+70.98%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>525.80 (n/a)</td><td>463.98 (n/a)</td><td>463.40 (n/a)</td><td>381.40 (n/a)</td><td>53.04 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (+14.75%)</td><td>0.05 (-0.70%)</td><td>0.04 (+5.67%)</td><td>0.03 (+3.83%)</td><td>0.02 (+0.49%)</td><td>480.70 (-3.71%)</td><td>377.20 (-0.73%)</td><td>417.50 (-5.37%)</td><td>217.80 (-12.85%)</td><td>101.19 (-15.19%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>499.20 (n/a)</td><td>379.96 (n/a)</td><td>441.20 (n/a)</td><td>249.90 (n/a)</td><td>119.31 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (+10.84%)</td><td>0.05 (-13.35%)</td><td>0.04 <b>(-29.69%)</b></td><td>0.03 (+2.21%)</td><td>0.02 <b>(+22.43%)</b></td><td>589.80 (-2.16%)</td><td>393.02 (+17.86%)</td><td>396.70 <b>(+42.24%)</b></td><td>220.70 (-9.77%)</td><td>152.27 (+0.61%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.80 (n/a)</td><td>333.46 (n/a)</td><td>278.90 (n/a)</td><td>244.60 (n/a)</td><td>151.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 <b>(-37.41%)</b></td><td>0.03 <b>(-30.25%)</b></td><td>0.03 <b>(-32.94%)</b></td><td>0.02 <b>(+46.09%)</b></td><td>0.01 <b>(-59.41%)</b></td><td>712.70 <b>(-31.54%)</b></td><td>512.00 (+14.90%)</td><td>468.80 <b>(+49.11%)</b></td><td>366.80 <b>(+59.76%)</b></td><td>132.80 <b>(-60.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1041.10 (n/a)</td><td>445.62 (n/a)</td><td>314.40 (n/a)</td><td>229.60 (n/a)</td><td>335.27 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (+2.08%)</td><td>0.04 (-18.22%)</td><td>0.04 <b>(-33.93%)</b></td><td>0.02 (+16.72%)</td><td>0.02 (-4.87%)</td><td>672.50 (-14.32%)</td><td>435.14 (+15.92%)</td><td>427.50 <b>(+51.38%)</b></td><td>240.00 (-2.04%)</td><td>172.35 <b>(-25.18%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>784.90 (n/a)</td><td>375.38 (n/a)</td><td>282.40 (n/a)</td><td>245.00 (n/a)</td><td>230.36 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-9.34%)</td><td>0.04 (-10.54%)</td><td>0.04 (-7.54%)</td><td>0.04 (+5.97%)</td><td>0.01 <b>(-25.35%)</b></td><td>467.60 (-5.63%)</td><td>386.92 (+7.69%)</td><td>389.50 (+8.16%)</td><td>247.80 (+10.28%)</td><td>84.74 <b>(-25.54%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>495.50 (n/a)</td><td>359.30 (n/a)</td><td>360.10 (n/a)</td><td>224.70 (n/a)</td><td>113.81 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 <b>(+38.06%)</b></td><td>0.05 (+15.21%)</td><td>0.04 (-4.90%)</td><td>0.03 <b>(-25.49%)</b></td><td>0.02 <b>(+167.93%)</b></td><td>639.10 <b>(+34.21%)</b></td><td>423.46 (+3.44%)</td><td>452.50 (+5.16%)</td><td>207.20 <b>(-27.55%)</b></td><td>196.12 <b>(+163.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.20 (n/a)</td><td>409.38 (n/a)</td><td>430.30 (n/a)</td><td>286.00 (n/a)</td><td>74.46 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 <b>(+39.44%)</b></td><td>0.05 (+13.15%)</td><td>0.03 (-10.93%)</td><td>0.03 <b>(-21.56%)</b></td><td>0.03 <b>(+156.82%)</b></td><td>603.90 <b>(+27.49%)</b></td><td>427.72 (+5.50%)</td><td>486.40 (+12.28%)</td><td>198.20 <b>(-28.27%)</b></td><td>194.16 <b>(+154.14%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.70 (n/a)</td><td>405.44 (n/a)</td><td>433.20 (n/a)</td><td>276.30 (n/a)</td><td>76.40 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (+4.62%)</td><td>0.04 (-0.85%)</td><td>0.04 (-8.88%)</td><td>0.03 (+1.75%)</td><td>0.01 (+3.05%)</td><td>615.30 (-1.71%)</td><td>467.44 (+0.37%)</td><td>467.50 (+9.77%)</td><td>284.80 (-4.40%)</td><td>125.52 (-9.06%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>626.00 (n/a)</td><td>465.72 (n/a)</td><td>425.90 (n/a)</td><td>297.90 (n/a)</td><td>138.02 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 <b>(-49.52%)</b></td><td>0.03 <b>(-22.16%)</b></td><td>0.03 (-19.60%)</td><td>0.03 (+2.07%)</td><td>0.01 <b>(-72.54%)</b></td><td>582.20 (-2.04%)</td><td>502.10 (+15.46%)</td><td>548.60 <b>(+24.40%)</b></td><td>411.40 <b>(+98.07%)</b></td><td>80.69 <b>(-43.15%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.30 (n/a)</td><td>434.86 (n/a)</td><td>441.00 (n/a)</td><td>207.70 (n/a)</td><td>141.94 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 <b>(+56.75%)</b></td><td>0.05 <b>(+26.13%)</b></td><td>0.05 <b>(+26.92%)</b></td><td>0.03 (+4.83%)</td><td>0.03 <b>(+116.39%)</b></td><td>538.00 (-4.61%)</td><td>358.72 (-11.72%)</td><td>302.10 <b>(-21.23%)</b></td><td>175.30 <b>(-36.21%)</b></td><td>155.66 <b>(+38.79%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>564.00 (n/a)</td><td>406.36 (n/a)</td><td>383.50 (n/a)</td><td>274.80 (n/a)</td><td>112.15 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (+15.57%)</td><td>0.05 <b>(+25.07%)</b></td><td>0.05 <b>(+37.82%)</b></td><td>0.03 <b>(+24.84%)</b></td><td>0.02 <b>(+30.57%)</b></td><td>589.10 (-19.89%)</td><td>389.00 (-18.27%)</td><td>332.30 <b>(-27.43%)</b></td><td>244.20 (-13.47%)</td><td>149.46 (-8.40%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>735.40 (n/a)</td><td>475.98 (n/a)</td><td>457.90 (n/a)</td><td>282.20 (n/a)</td><td>163.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (-16.69%)</td><td>0.04 (-11.93%)</td><td>0.04 (-18.92%)</td><td>0.03 (+15.63%)</td><td>0.01 <b>(-55.54%)</b></td><td>482.50 (-13.51%)</td><td>393.64 (+6.00%)</td><td>381.60 <b>(+23.34%)</b></td><td>319.50 <b>(+20.02%)</b></td><td>62.05 <b>(-52.17%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>557.90 (n/a)</td><td>371.36 (n/a)</td><td>309.40 (n/a)</td><td>266.20 (n/a)</td><td>129.72 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (-17.22%)</td><td>0.09 (-14.40%)</td><td>0.09 (-13.63%)</td><td>0.07 (+4.41%)</td><td>0.03 <b>(-27.97%)</b></td><td>479.70 (-4.23%)</td><td>372.30 (+12.91%)</td><td>349.50 (+15.81%)</td><td>250.50 <b>(+20.78%)</b></td><td>102.14 (-12.85%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>500.90 (n/a)</td><td>329.72 (n/a)</td><td>301.80 (n/a)</td><td>207.40 (n/a)</td><td>117.19 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-15.17%)</td><td>0.09 <b>(-22.68%)</b></td><td>0.08 <b>(-31.02%)</b></td><td>0.05 (-14.78%)</td><td>0.03 (-5.91%)</td><td>615.50 (+17.35%)</td><td>401.82 <b>(+30.22%)</b></td><td>393.20 <b>(+44.99%)</b></td><td>269.30 (+17.91%)</td><td>142.56 (+16.78%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>524.50 (n/a)</td><td>308.56 (n/a)</td><td>271.20 (n/a)</td><td>228.40 (n/a)</td><td>122.08 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-7.38%)</td><td>0.07 <b>(-26.31%)</b></td><td>0.07 <b>(-31.35%)</b></td><td>0.02 <b>(-71.34%)</b></td><td>0.04 (+10.85%)</td><td>1846.50 <b>(+248.86%)</b></td><td>692.74 <b>(+84.99%)</b></td><td>454.70 <b>(+45.64%)</b></td><td>266.60 (+7.98%)</td><td>649.89 <b>(+364.57%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>529.30 (n/a)</td><td>374.48 (n/a)</td><td>312.20 (n/a)</td><td>246.90 (n/a)</td><td>139.89 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (+14.67%)</td><td>0.12 <b>(+41.27%)</b></td><td>0.12 <b>(+66.76%)</b></td><td>0.11 <b>(+68.23%)</b></td><td>0.01 <b>(-55.74%)</b></td><td>292.70 <b>(-40.57%)</b></td><td>274.20 <b>(-32.78%)</b></td><td>283.70 <b>(-40.02%)</b></td><td>236.20 (-12.78%)</td><td>22.26 <b>(-77.94%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>492.50 (n/a)</td><td>407.94 (n/a)</td><td>473.00 (n/a)</td><td>270.80 (n/a)</td><td>100.94 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 <b>(+37.90%)</b></td><td>0.09 <b>(+23.74%)</b></td><td>0.08 (+9.18%)</td><td>0.06 (-1.88%)</td><td>0.03 <b>(+172.51%)</b></td><td>558.40 (+1.90%)</td><td>406.84 (-13.59%)</td><td>421.40 (-8.41%)</td><td>273.40 <b>(-27.48%)</b></td><td>126.91 <b>(+93.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>548.00 (n/a)</td><td>470.80 (n/a)</td><td>460.10 (n/a)</td><td>377.00 (n/a)</td><td>65.48 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 <b>(-36.62%)</b></td><td>0.08 <b>(-23.06%)</b></td><td>0.07 <b>(-26.86%)</b></td><td>0.06 (-10.18%)</td><td>0.02 <b>(-49.06%)</b></td><td>524.50 (+11.34%)</td><td>411.70 <b>(+22.09%)</b></td><td>445.40 <b>(+36.71%)</b></td><td>284.50 <b>(+57.79%)</b></td><td>103.96 (-12.76%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>471.10 (n/a)</td><td>337.22 (n/a)</td><td>325.80 (n/a)</td><td>180.30 (n/a)</td><td>119.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (-8.60%)</td><td>0.09 (+8.31%)</td><td>0.10 <b>(+61.02%)</b></td><td>0.06 <b>(+73.79%)</b></td><td>0.03 <b>(-37.94%)</b></td><td>582.80 <b>(-42.46%)</b></td><td>388.54 <b>(-23.79%)</b></td><td>318.60 <b>(-37.91%)</b></td><td>260.60 (+9.40%)</td><td>136.03 <b>(-56.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1012.90 (n/a)</td><td>509.84 (n/a)</td><td>513.10 (n/a)</td><td>238.20 (n/a)</td><td>314.18 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 <b>(+58.87%)</b></td><td>0.08 <b>(+33.04%)</b></td><td>0.08 <b>(+35.31%)</b></td><td>0.06 (+17.88%)</td><td>0.02 <b>(+338.79%)</b></td><td>512.10 (-15.17%)</td><td>431.88 <b>(-22.75%)</b></td><td>413.90 <b>(-26.09%)</b></td><td>321.40 <b>(-37.05%)</b></td><td>81.10 <b>(+142.66%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>603.70 (n/a)</td><td>559.10 (n/a)</td><td>560.00 (n/a)</td><td>510.60 (n/a)</td><td>33.42 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 <b>(-21.48%)</b></td><td>0.08 (-17.44%)</td><td>0.08 <b>(-31.43%)</b></td><td>0.06 (+17.15%)</td><td>0.02 <b>(-55.49%)</b></td><td>526.90 (-14.63%)</td><td>431.44 (+7.87%)</td><td>422.70 <b>(+45.81%)</b></td><td>316.00 <b>(+27.37%)</b></td><td>84.23 <b>(-52.83%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>617.20 (n/a)</td><td>399.96 (n/a)</td><td>289.90 (n/a)</td><td>248.10 (n/a)</td><td>178.56 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (-9.42%)</td><td>0.10 (-19.00%)</td><td>0.09 <b>(-26.91%)</b></td><td>0.07 <b>(-23.31%)</b></td><td>0.02 (+0.84%)</td><td>485.60 <b>(+30.40%)</b></td><td>356.32 <b>(+25.11%)</b></td><td>361.70 <b>(+36.80%)</b></td><td>262.00 (+10.36%)</td><td>83.96 <b>(+47.85%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>372.40 (n/a)</td><td>284.80 (n/a)</td><td>264.40 (n/a)</td><td>237.40 (n/a)</td><td>56.79 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-9.76%)</td><td>0.09 (-3.62%)</td><td>0.10 (+10.26%)</td><td>0.07 (-6.66%)</td><td>0.02 (-13.92%)</td><td>493.80 (+7.14%)</td><td>377.12 (+3.13%)</td><td>339.80 (-9.29%)</td><td>282.20 (+10.80%)</td><td>94.82 (+2.66%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>460.90 (n/a)</td><td>365.68 (n/a)</td><td>374.60 (n/a)</td><td>254.70 (n/a)</td><td>92.37 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-17.03%)</td><td>0.09 (+5.17%)</td><td>0.10 (+5.44%)</td><td>0.05 <b>(+279.11%)</b></td><td>0.03 <b>(-47.77%)</b></td><td>661.50 <b>(-73.62%)</b></td><td>422.82 <b>(-51.85%)</b></td><td>322.90 (-5.14%)</td><td>279.90 <b>(+20.54%)</b></td><td>172.29 <b>(-82.32%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>2507.70 (n/a)</td><td>878.06 (n/a)</td><td>340.40 (n/a)</td><td>232.20 (n/a)</td><td>974.63 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(-27.01%)</b></td><td>0.01 (-4.02%)</td><td>0.01 (+6.53%)</td><td>0.01 (-1.09%)</td><td>0.00 <b>(-39.08%)</b></td><td>463.40 (+1.11%)</td><td>327.36 (+1.44%)</td><td>295.30 (-6.13%)</td><td>288.70 <b>(+37.02%)</b></td><td>76.11 (-13.76%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>458.30 (n/a)</td><td>322.70 (n/a)</td><td>314.60 (n/a)</td><td>210.70 (n/a)</td><td>88.26 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-17.87%)</td><td>0.01 <b>(-20.41%)</b></td><td>0.01 (-14.69%)</td><td>0.01 (-10.26%)</td><td>0.00 <b>(-27.21%)</b></td><td>630.20 (+11.42%)</td><td>498.04 <b>(+22.63%)</b></td><td>486.90 (+17.21%)</td><td>305.30 <b>(+21.73%)</b></td><td>135.30 (+1.37%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>406.14 (n/a)</td><td>415.40 (n/a)</td><td>250.80 (n/a)</td><td>133.47 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (-13.56%)</td><td>0.01 (-4.39%)</td><td>0.01 (+0.41%)</td><td>0.01 (-8.67%)</td><td>0.00 (-18.91%)</td><td>575.30 (+9.50%)</td><td>432.62 (+3.36%)</td><td>423.20 (-0.42%)</td><td>302.90 (+15.70%)</td><td>112.56 (+0.44%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.40 (n/a)</td><td>418.54 (n/a)</td><td>425.00 (n/a)</td><td>261.80 (n/a)</td><td>112.07 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-16.24%)</td><td>0.01 (-18.33%)</td><td>0.01 (-19.57%)</td><td>0.01 (-4.09%)</td><td>0.00 <b>(-37.89%)</b></td><td>598.10 (+4.25%)</td><td>468.86 (+17.80%)</td><td>482.70 <b>(+24.34%)</b></td><td>330.40 (+19.36%)</td><td>97.44 <b>(-21.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.70 (n/a)</td><td>398.00 (n/a)</td><td>388.20 (n/a)</td><td>276.80 (n/a)</td><td>124.45 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(-21.03%)</b></td><td>0.01 (-2.94%)</td><td>0.01 (-12.54%)</td><td>0.01 <b>(+73.69%)</b></td><td>0.00 <b>(-46.07%)</b></td><td>596.90 <b>(-42.42%)</b></td><td>387.40 (-16.96%)</td><td>346.40 (+14.36%)</td><td>287.40 <b>(+26.61%)</b></td><td>125.45 <b>(-62.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1036.70 (n/a)</td><td>466.54 (n/a)</td><td>302.90 (n/a)</td><td>227.00 (n/a)</td><td>332.21 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(-30.39%)</b></td><td>0.01 (-18.19%)</td><td>0.01 (-4.95%)</td><td>0.01 <b>(-23.41%)</b></td><td>0.00 <b>(-44.42%)</b></td><td>637.50 <b>(+30.55%)</b></td><td>515.30 (+19.24%)</td><td>491.80 (+5.22%)</td><td>369.50 <b>(+43.66%)</b></td><td>104.83 (+6.66%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.30 (n/a)</td><td>432.16 (n/a)</td><td>467.40 (n/a)</td><td>257.20 (n/a)</td><td>98.28 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(-29.36%)</b></td><td>0.01 (+10.23%)</td><td>0.01 <b>(+64.64%)</b></td><td>0.01 <b>(+21.67%)</b></td><td>0.00 <b>(-54.81%)</b></td><td>532.30 (-17.80%)</td><td>388.50 <b>(-21.58%)</b></td><td>344.20 <b>(-39.25%)</b></td><td>278.90 <b>(+41.57%)</b></td><td>102.48 <b>(-46.28%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>647.60 (n/a)</td><td>495.38 (n/a)</td><td>566.60 (n/a)</td><td>197.00 (n/a)</td><td>190.79 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (+15.98%)</td><td>0.01 (-11.11%)</td><td>0.01 (-10.49%)</td><td>0.00 <b>(-67.43%)</b></td><td>0.00 <b>(+92.58%)</b></td><td>1870.70 <b>(+207.02%)</b></td><td>769.58 <b>(+54.86%)</b></td><td>522.70 (+11.71%)</td><td>289.30 (-13.77%)</td><td>629.00 <b>(+450.28%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.30 (n/a)</td><td>496.96 (n/a)</td><td>467.90 (n/a)</td><td>335.50 (n/a)</td><td>114.31 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 <b>(-28.56%)</b></td><td>0.01 <b>(-33.86%)</b></td><td>0.01 <b>(-34.10%)</b></td><td>0.01 (-10.18%)</td><td>0.00 <b>(-42.43%)</b></td><td>637.60 (+11.33%)</td><td>464.50 <b>(+42.21%)</b></td><td>460.20 <b>(+51.73%)</b></td><td>292.10 <b>(+39.96%)</b></td><td>123.08 (-15.35%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.70 (n/a)</td><td>326.64 (n/a)</td><td>303.30 (n/a)</td><td>208.70 (n/a)</td><td>145.40 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (-9.66%)</td><td>0.01 (+8.97%)</td><td>0.01 (+19.31%)</td><td>0.01 (+16.69%)</td><td>0.00 (-1.03%)</td><td>618.10 (-14.30%)</td><td>440.56 (-7.89%)</td><td>374.30 (-16.19%)</td><td>293.60 (+10.67%)</td><td>164.61 (-0.65%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>721.20 (n/a)</td><td>478.32 (n/a)</td><td>446.60 (n/a)</td><td>265.30 (n/a)</td><td>165.70 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(+75.97%)</b></td><td>0.01 <b>(+56.91%)</b></td><td>0.01 <b>(+27.53%)</b></td><td>0.01 <b>(+66.86%)</b></td><td>0.00 <b>(+62.70%)</b></td><td>615.30 <b>(-40.07%)</b></td><td>424.38 <b>(-37.34%)</b></td><td>372.20 <b>(-21.59%)</b></td><td>233.60 <b>(-43.18%)</b></td><td>171.88 <b>(-44.26%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1026.70 (n/a)</td><td>677.26 (n/a)</td><td>474.70 (n/a)</td><td>411.10 (n/a)</td><td>308.37 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 <b>(-24.53%)</b></td><td>0.02 <b>(-41.49%)</b></td><td>0.02 <b>(-42.41%)</b></td><td>0.01 <b>(-40.61%)</b></td><td>0.01 (-19.68%)</td><td>687.00 <b>(+68.38%)</b></td><td>449.52 <b>(+77.37%)</b></td><td>429.00 <b>(+73.61%)</b></td><td>206.60 <b>(+32.44%)</b></td><td>174.19 <b>(+72.53%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>408.00 (n/a)</td><td>253.44 (n/a)</td><td>247.10 (n/a)</td><td>156.00 (n/a)</td><td>100.96 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 <b>(+55.32%)</b></td><td>0.04 <b>(+37.81%)</b></td><td>0.04 <b>(+41.57%)</b></td><td>0.02 (+15.70%)</td><td>0.01 <b>(+204.48%)</b></td><td>506.40 (-13.57%)</td><td>363.94 <b>(-23.42%)</b></td><td>325.50 <b>(-29.36%)</b></td><td>268.80 <b>(-35.62%)</b></td><td>108.64 <b>(+63.18%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>585.90 (n/a)</td><td>475.22 (n/a)</td><td>460.80 (n/a)</td><td>417.50 (n/a)</td><td>66.57 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(-23.54%)</b></td><td>0.02 <b>(-44.47%)</b></td><td>0.02 <b>(-35.08%)</b></td><td>0.00 <b>(-82.96%)</b></td><td>0.01 <b>(+138.97%)</b></td><td>1835.00 <b>(+487.01%)</b></td><td>696.96 <b>(+169.80%)</b></td><td>376.50 <b>(+54.05%)</b></td><td>299.90 <b>(+30.79%)</b></td><td>645.96 <b>(+1853.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>312.60 (n/a)</td><td>258.32 (n/a)</td><td>244.40 (n/a)</td><td>229.30 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 <b>(-30.94%)</b></td><td>0.02 <b>(-26.59%)</b></td><td>0.02 (-14.53%)</td><td>0.01 <b>(-21.24%)</b></td><td>0.00 <b>(-53.51%)</b></td><td>727.20 <b>(+26.98%)</b></td><td>557.22 <b>(+30.50%)</b></td><td>545.90 (+17.00%)</td><td>419.70 <b>(+44.77%)</b></td><td>111.55 (-10.16%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.70 (n/a)</td><td>426.98 (n/a)</td><td>466.60 (n/a)</td><td>289.90 (n/a)</td><td>124.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(-26.86%)</b></td><td>0.03 (-6.95%)</td><td>0.03 (-13.38%)</td><td>0.02 <b>(+58.85%)</b></td><td>0.01 <b>(-52.66%)</b></td><td>470.30 <b>(-37.05%)</b></td><td>336.06 (-11.72%)</td><td>287.10 (+15.44%)</td><td>258.60 <b>(+36.68%)</b></td><td>92.20 <b>(-60.41%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>747.10 (n/a)</td><td>380.66 (n/a)</td><td>248.70 (n/a)</td><td>189.20 (n/a)</td><td>232.89 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (+3.32%)</td><td>0.02 <b>(-21.59%)</b></td><td>0.02 <b>(-33.32%)</b></td><td>0.02 <b>(-30.31%)</b></td><td>0.01 <b>(+53.17%)</b></td><td>665.20 <b>(+43.49%)</b></td><td>506.10 <b>(+35.00%)</b></td><td>548.80 <b>(+49.99%)</b></td><td>283.10 (-3.21%)</td><td>143.89 <b>(+100.58%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>463.60 (n/a)</td><td>374.90 (n/a)</td><td>365.90 (n/a)</td><td>292.50 (n/a)</td><td>71.74 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(-25.08%)</b></td><td>0.02 <b>(-43.85%)</b></td><td>0.01 <b>(-55.20%)</b></td><td>0.01 <b>(-27.51%)</b></td><td>0.01 (-16.21%)</td><td>660.50 <b>(+37.95%)</b></td><td>523.66 <b>(+80.20%)</b></td><td>571.00 <b>(+123.22%)</b></td><td>286.30 <b>(+33.47%)</b></td><td>148.08 <b>(+38.73%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.80 (n/a)</td><td>290.60 (n/a)</td><td>255.80 (n/a)</td><td>214.50 (n/a)</td><td>106.74 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-11.80%)</td><td>0.03 <b>(+38.16%)</b></td><td>0.03 <b>(+56.81%)</b></td><td>0.02 <b>(+215.11%)</b></td><td>0.01 <b>(-37.40%)</b></td><td>601.30 <b>(-68.27%)</b></td><td>350.92 <b>(-50.24%)</b></td><td>303.40 <b>(-36.22%)</b></td><td>265.90 (+13.34%)</td><td>140.90 <b>(-79.07%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1894.90 (n/a)</td><td>705.24 (n/a)</td><td>475.70 (n/a)</td><td>234.60 (n/a)</td><td>673.29 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (-6.96%)</td><td>0.02 (+8.19%)</td><td>0.02 (+13.67%)</td><td>0.01 (+5.43%)</td><td>0.01 (-11.57%)</td><td>556.60 (-5.15%)</td><td>411.98 (-9.18%)</td><td>450.70 (-12.02%)</td><td>237.20 (+7.48%)</td><td>136.56 (-4.43%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.80 (n/a)</td><td>453.62 (n/a)</td><td>512.30 (n/a)</td><td>220.70 (n/a)</td><td>142.89 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(-25.64%)</b></td><td>0.02 (-0.38%)</td><td>0.02 (+13.13%)</td><td>0.02 (+17.99%)</td><td>0.01 <b>(-45.75%)</b></td><td>513.20 (-15.24%)</td><td>419.20 (-9.44%)</td><td>471.80 (-11.60%)</td><td>276.10 <b>(+34.49%)</b></td><td>106.44 <b>(-37.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.50 (n/a)</td><td>462.92 (n/a)</td><td>533.70 (n/a)</td><td>205.30 (n/a)</td><td>169.07 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 <b>(+25.52%)</b></td><td>0.02 (-2.18%)</td><td>0.02 (-8.26%)</td><td>0.01 (+12.74%)</td><td>0.01 <b>(+33.16%)</b></td><td>564.30 (-11.30%)</td><td>459.38 (+4.11%)</td><td>500.10 (+9.00%)</td><td>237.10 <b>(-20.33%)</b></td><td>127.54 (-8.21%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.20 (n/a)</td><td>441.24 (n/a)</td><td>458.80 (n/a)</td><td>297.60 (n/a)</td><td>138.96 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (+0.28%)</td><td>0.06 <b>(+34.93%)</b></td><td>0.06 <b>(+33.12%)</b></td><td>0.03 <b>(+312.71%)</b></td><td>0.01 <b>(-38.17%)</b></td><td>490.60 <b>(-75.77%)</b></td><td>308.64 <b>(-54.57%)</b></td><td>263.30 <b>(-24.88%)</b></td><td>243.30 (-0.29%)</td><td>103.61 <b>(-86.31%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2024.90 (n/a)</td><td>679.36 (n/a)</td><td>350.50 (n/a)</td><td>244.00 (n/a)</td><td>756.80 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (+5.27%)</td><td>0.06 (-14.67%)</td><td>0.05 (-7.17%)</td><td>0.03 <b>(-29.74%)</b></td><td>0.03 (+18.76%)</td><td>754.60 <b>(+42.32%)</b></td><td>526.00 <b>(+24.63%)</b></td><td>543.30 (+7.71%)</td><td>233.80 (-5.00%)</td><td>198.24 <b>(+45.74%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>530.20 (n/a)</td><td>422.06 (n/a)</td><td>504.40 (n/a)</td><td>246.10 (n/a)</td><td>136.02 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (+13.73%)</td><td>0.04 (+1.55%)</td><td>0.03 (-3.28%)</td><td>0.03 (+3.36%)</td><td>0.01 <b>(+33.88%)</b></td><td>525.10 (-3.26%)</td><td>442.12 (+0.82%)</td><td>487.60 (+3.37%)</td><td>254.80 (-12.05%)</td><td>108.27 (+12.89%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>542.80 (n/a)</td><td>438.52 (n/a)</td><td>471.70 (n/a)</td><td>289.70 (n/a)</td><td>95.91 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (-9.15%)</td><td>0.05 (+0.82%)</td><td>0.04 (-5.47%)</td><td>0.04 <b>(+227.32%)</b></td><td>0.02 <b>(-37.48%)</b></td><td>573.40 <b>(-69.45%)</b></td><td>444.06 <b>(-35.62%)</b></td><td>544.30 (+5.79%)</td><td>261.40 (+10.06%)</td><td>152.39 <b>(-77.63%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1877.00 (n/a)</td><td>689.72 (n/a)</td><td>514.50 (n/a)</td><td>237.50 (n/a)</td><td>681.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-3.04%)</td><td>0.05 (+2.38%)</td><td>0.06 (+5.69%)</td><td>0.03 (+6.48%)</td><td>0.02 (-9.79%)</td><td>504.30 (-6.09%)</td><td>349.74 (-5.12%)</td><td>266.40 (-5.40%)</td><td>244.40 (+3.12%)</td><td>126.88 (-16.00%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.00 (n/a)</td><td>368.62 (n/a)</td><td>281.60 (n/a)</td><td>237.00 (n/a)</td><td>151.05 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-9.03%)</td><td>0.05 (-17.79%)</td><td>0.04 <b>(-33.79%)</b></td><td>0.01 <b>(-60.91%)</b></td><td>0.02 (+0.55%)</td><td>1910.50 <b>(+155.79%)</b></td><td>692.64 <b>(+60.15%)</b></td><td>455.80 <b>(+51.03%)</b></td><td>287.90 (+9.93%)</td><td>687.40 <b>(+209.45%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>746.90 (n/a)</td><td>432.50 (n/a)</td><td>301.80 (n/a)</td><td>261.90 (n/a)</td><td>222.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 <b>(-51.13%)</b></td><td>0.03 <b>(-22.20%)</b></td><td>0.03 (-6.01%)</td><td>0.02 <b>(-20.88%)</b></td><td>0.01 <b>(-69.52%)</b></td><td>756.50 <b>(+26.40%)</b></td><td>520.94 (+15.55%)</td><td>482.30 (+6.40%)</td><td>420.70 <b>(+104.62%)</b></td><td>134.36 (-15.05%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.50 (n/a)</td><td>450.84 (n/a)</td><td>453.30 (n/a)</td><td>205.60 (n/a)</td><td>158.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 <b>(+59.91%)</b></td><td>0.05 <b>(+20.07%)</b></td><td>0.04 (-13.20%)</td><td>0.02 <b>(-26.80%)</b></td><td>0.03 <b>(+237.94%)</b></td><td>762.20 <b>(+36.62%)</b></td><td>468.72 (+2.05%)</td><td>485.70 (+15.20%)</td><td>224.50 <b>(-37.47%)</b></td><td>234.08 <b>(+161.46%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>557.90 (n/a)</td><td>459.30 (n/a)</td><td>421.60 (n/a)</td><td>359.00 (n/a)</td><td>89.53 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (+11.62%)</td><td>0.04 <b>(-22.35%)</b></td><td>0.03 <b>(-34.62%)</b></td><td>0.03 (-13.65%)</td><td>0.02 <b>(+53.79%)</b></td><td>569.40 (+15.80%)</td><td>465.56 <b>(+35.88%)</b></td><td>490.40 <b>(+52.96%)</b></td><td>242.40 (-10.42%)</td><td>130.71 <b>(+48.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.70 (n/a)</td><td>342.62 (n/a)</td><td>320.60 (n/a)</td><td>270.60 (n/a)</td><td>88.08 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 <b>(+36.81%)</b></td><td>0.05 <b>(+25.45%)</b></td><td>0.04 <b>(+20.39%)</b></td><td>0.03 <b>(+223.71%)</b></td><td>0.03 (+8.61%)</td><td>592.90 <b>(-69.11%)</b></td><td>416.22 <b>(-42.05%)</b></td><td>447.10 (-16.94%)</td><td>189.50 <b>(-26.89%)</b></td><td>169.08 <b>(-75.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1919.40 (n/a)</td><td>718.22 (n/a)</td><td>538.30 (n/a)</td><td>259.20 (n/a)</td><td>687.20 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (-2.51%)</td><td>0.04 (+14.24%)</td><td>0.04 <b>(+38.62%)</b></td><td>0.02 (-1.67%)</td><td>0.02 (-3.48%)</td><td>792.90 (+1.71%)</td><td>443.20 (-12.12%)</td><td>368.80 <b>(-27.87%)</b></td><td>258.30 (+2.58%)</td><td>213.27 (+5.83%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>779.60 (n/a)</td><td>504.32 (n/a)</td><td>511.30 (n/a)</td><td>251.80 (n/a)</td><td>201.52 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 <b>(-29.62%)</b></td><td>0.07 <b>(-25.38%)</b></td><td>0.06 (-9.28%)</td><td>0.06 (-9.76%)</td><td>0.02 <b>(-43.87%)</b></td><td>574.40 (+10.80%)</td><td>489.38 <b>(+25.33%)</b></td><td>519.40 (+10.23%)</td><td>288.50 <b>(+42.05%)</b></td><td>116.72 (-16.02%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>518.40 (n/a)</td><td>390.46 (n/a)</td><td>471.20 (n/a)</td><td>203.10 (n/a)</td><td>138.99 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (-12.46%)</td><td>0.07 <b>(-38.24%)</b></td><td>0.07 <b>(-39.75%)</b></td><td>0.02 <b>(-78.69%)</b></td><td>0.04 <b>(+63.21%)</b></td><td>1908.90 <b>(+369.36%)</b></td><td>721.80 <b>(+140.39%)</b></td><td>479.60 <b>(+65.95%)</b></td><td>256.10 (+14.23%)</td><td>671.33 <b>(+883.57%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>406.70 (n/a)</td><td>300.26 (n/a)</td><td>289.00 (n/a)</td><td>224.20 (n/a)</td><td>68.25 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.17 (+7.11%)</td><td>0.10 <b>(+26.01%)</b></td><td>0.09 (+17.30%)</td><td>0.07 <b>(+96.97%)</b></td><td>0.04 <b>(-21.84%)</b></td><td>556.00 <b>(-49.24%)</b></td><td>437.78 <b>(-35.17%)</b></td><td>446.40 (-14.74%)</td><td>242.10 (-6.63%)</td><td>118.43 <b>(-68.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1095.30 (n/a)</td><td>675.30 (n/a)</td><td>523.60 (n/a)</td><td>259.30 (n/a)</td><td>374.83 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (+5.40%)</td><td>0.08 (+7.27%)</td><td>0.06 (-13.36%)</td><td>0.05 (-6.11%)</td><td>0.03 <b>(+41.46%)</b></td><td>661.20 (+6.51%)</td><td>470.92 (-0.53%)</td><td>555.70 (+15.41%)</td><td>274.60 (-5.11%)</td><td>175.43 <b>(+41.08%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>620.80 (n/a)</td><td>473.42 (n/a)</td><td>481.50 (n/a)</td><td>289.40 (n/a)</td><td>124.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (+5.98%)</td><td>0.09 (-17.09%)</td><td>0.08 (-19.87%)</td><td>0.06 <b>(-20.44%)</b></td><td>0.04 (+11.52%)</td><td>697.80 <b>(+25.68%)</b></td><td>516.84 <b>(+23.92%)</b></td><td>542.60 <b>(+24.82%)</b></td><td>258.20 (-5.63%)</td><td>159.57 <b>(+22.07%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>555.20 (n/a)</td><td>417.08 (n/a)</td><td>434.70 (n/a)</td><td>273.60 (n/a)</td><td>130.72 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (-1.00%)</td><td>0.07 (-11.79%)</td><td>0.08 (+0.74%)</td><td>0.02 <b>(-72.16%)</b></td><td>0.03 <b>(+132.43%)</b></td><td>1935.30 <b>(+259.12%)</b></td><td>720.08 <b>(+63.80%)</b></td><td>433.90 (-0.73%)</td><td>352.50 (+1.00%)</td><td>681.07 <b>(+832.05%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>538.90 (n/a)</td><td>439.60 (n/a)</td><td>437.10 (n/a)</td><td>349.00 (n/a)</td><td>73.07 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.17 <b>(+67.68%)</b></td><td>0.11 <b>(+27.40%)</b></td><td>0.11 (+19.97%)</td><td>0.07 (-5.60%)</td><td>0.05 <b>(+189.81%)</b></td><td>566.40 (+5.95%)</td><td>389.44 (-12.25%)</td><td>344.30 (-16.65%)</td><td>212.60 <b>(-40.36%)</b></td><td>157.36 <b>(+88.14%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>534.60 (n/a)</td><td>443.80 (n/a)</td><td>413.10 (n/a)</td><td>356.50 (n/a)</td><td>83.64 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (-8.38%)</td><td>0.07 (-14.97%)</td><td>0.07 <b>(-36.90%)</b></td><td>0.05 <b>(+162.67%)</b></td><td>0.02 <b>(-49.22%)</b></td><td>707.50 <b>(-61.93%)</b></td><td>504.92 <b>(-23.38%)</b></td><td>474.80 <b>(+58.48%)</b></td><td>317.60 (+9.14%)</td><td>145.86 <b>(-78.53%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1858.30 (n/a)</td><td>659.00 (n/a)</td><td>299.60 (n/a)</td><td>291.00 (n/a)</td><td>679.37 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (+8.32%)</td><td>0.07 (-6.92%)</td><td>0.08 (+3.09%)</td><td>0.02 <b>(-70.37%)</b></td><td>0.04 <b>(+111.84%)</b></td><td>1873.20 <b>(+237.45%)</b></td><td>732.72 <b>(+53.70%)</b></td><td>479.70 (-2.99%)</td><td>309.40 (-7.70%)</td><td>648.48 <b>(+616.80%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>555.10 (n/a)</td><td>476.72 (n/a)</td><td>494.50 (n/a)</td><td>335.20 (n/a)</td><td>90.47 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 <b>(+24.93%)</b></td><td>0.08 (+11.51%)</td><td>0.08 (+7.25%)</td><td>0.05 (+4.00%)</td><td>0.02 <b>(+62.80%)</b></td><td>627.60 (-3.85%)</td><td>454.16 (-7.74%)</td><td>435.30 (-6.77%)</td><td>305.10 (-19.96%)</td><td>121.76 <b>(+22.30%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>652.70 (n/a)</td><td>492.28 (n/a)</td><td>466.90 (n/a)</td><td>381.20 (n/a)</td><td>99.56 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-17.68%)</td><td>0.07 (-0.48%)</td><td>0.07 (-7.72%)</td><td>0.07 <b>(+58.78%)</b></td><td>0.00 <b>(-86.08%)</b></td><td>307.60 <b>(-37.02%)</b></td><td>295.20 (-5.67%)</td><td>298.40 (+8.35%)</td><td>281.80 <b>(+21.52%)</b></td><td>10.05 <b>(-90.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>488.40 (n/a)</td><td>312.96 (n/a)</td><td>275.40 (n/a)</td><td>231.90 (n/a)</td><td>100.95 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (+6.21%)</td><td>0.06 (+19.34%)</td><td>0.07 <b>(+45.17%)</b></td><td>0.03 (+5.34%)</td><td>0.02 <b>(+37.43%)</b></td><td>590.80 (-5.06%)</td><td>391.28 (-13.44%)</td><td>310.50 <b>(-31.11%)</b></td><td>290.70 (-5.86%)</td><td>133.80 (+19.53%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>622.30 (n/a)</td><td>452.02 (n/a)</td><td>450.70 (n/a)</td><td>308.80 (n/a)</td><td>111.94 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (+4.70%)</td><td>0.06 (+13.49%)</td><td>0.07 <b>(+64.97%)</b></td><td>0.04 (+3.80%)</td><td>0.02 (-4.34%)</td><td>515.30 (-3.65%)</td><td>358.14 (-13.09%)</td><td>293.40 <b>(-39.38%)</b></td><td>237.20 (-4.51%)</td><td>120.14 (-9.69%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>534.80 (n/a)</td><td>412.08 (n/a)</td><td>484.00 (n/a)</td><td>248.40 (n/a)</td><td>133.03 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (-5.15%)</td><td>0.07 <b>(+35.66%)</b></td><td>0.07 <b>(+76.08%)</b></td><td>0.04 (+10.87%)</td><td>0.02 <b>(-24.04%)</b></td><td>517.80 (-9.81%)</td><td>333.52 <b>(-29.79%)</b></td><td>289.00 <b>(-43.20%)</b></td><td>240.60 (+5.43%)</td><td>110.41 <b>(-22.76%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.10 (n/a)</td><td>475.06 (n/a)</td><td>508.80 (n/a)</td><td>228.20 (n/a)</td><td>142.94 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (+14.59%)</td><td>0.05 (-7.49%)</td><td>0.04 <b>(-35.48%)</b></td><td>0.03 (+2.03%)</td><td>0.02 (+17.52%)</td><td>635.90 (-2.00%)</td><td>458.50 (+11.12%)</td><td>471.70 <b>(+54.96%)</b></td><td>247.50 (-12.73%)</td><td>181.35 (+8.09%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>648.90 (n/a)</td><td>412.62 (n/a)</td><td>304.40 (n/a)</td><td>283.60 (n/a)</td><td>167.78 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 <b>(+23.32%)</b></td><td>0.06 <b>(+31.25%)</b></td><td>0.06 <b>(+40.62%)</b></td><td>0.04 (+4.46%)</td><td>0.02 <b>(+40.71%)</b></td><td>577.90 (-4.26%)</td><td>380.62 <b>(-21.38%)</b></td><td>370.00 <b>(-28.87%)</b></td><td>243.40 (-18.92%)</td><td>132.57 (+10.39%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>603.60 (n/a)</td><td>484.12 (n/a)</td><td>520.20 (n/a)</td><td>300.20 (n/a)</td><td>120.10 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (+7.08%)</td><td>0.07 (-6.63%)</td><td>0.08 (-0.75%)</td><td>0.04 (-14.87%)</td><td>0.03 <b>(+39.37%)</b></td><td>656.00 (+17.46%)</td><td>390.66 (+14.27%)</td><td>302.80 (+0.73%)</td><td>253.30 (-6.63%)</td><td>174.33 <b>(+43.08%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.50 (n/a)</td><td>341.88 (n/a)</td><td>300.60 (n/a)</td><td>271.30 (n/a)</td><td>121.84 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (+0.11%)</td><td>0.06 (-9.78%)</td><td>0.05 (-11.16%)</td><td>0.03 <b>(-23.56%)</b></td><td>0.02 (+13.87%)</td><td>845.50 <b>(+30.82%)</b></td><td>508.28 (+17.39%)</td><td>468.80 (+12.56%)</td><td>298.90 (-0.13%)</td><td>223.58 <b>(+52.54%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>646.30 (n/a)</td><td>433.00 (n/a)</td><td>416.50 (n/a)</td><td>299.30 (n/a)</td><td>146.57 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (-12.91%)</td><td>0.07 (+8.77%)</td><td>0.05 (-4.43%)</td><td>0.05 (+18.45%)</td><td>0.02 (-14.67%)</td><td>532.00 (-15.58%)</td><td>400.32 (-10.49%)</td><td>451.80 (+4.63%)</td><td>274.60 (+14.80%)</td><td>117.39 (-17.67%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>630.20 (n/a)</td><td>447.24 (n/a)</td><td>431.80 (n/a)</td><td>239.20 (n/a)</td><td>142.57 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 <b>(+65.08%)</b></td><td>0.04 (-6.80%)</td><td>0.04 (-5.00%)</td><td>0.01 <b>(-68.04%)</b></td><td>0.03 <b>(+436.61%)</b></td><td>2053.80 <b>(+212.89%)</b></td><td>906.08 <b>(+62.61%)</b></td><td>550.10 (+5.26%)</td><td>297.60 <b>(-39.41%)</b></td><td>705.36 <b>(+954.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>656.40 (n/a)</td><td>557.20 (n/a)</td><td>522.60 (n/a)</td><td>491.20 (n/a)</td><td>66.90 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (+1.54%)</td><td>0.07 (-0.29%)</td><td>0.07 (-7.04%)</td><td>0.03 <b>(-23.00%)</b></td><td>0.03 (+13.72%)</td><td>722.70 <b>(+29.87%)</b></td><td>406.96 (+5.43%)</td><td>331.30 (+7.56%)</td><td>244.20 (-1.53%)</td><td>202.03 <b>(+32.13%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>556.50 (n/a)</td><td>386.00 (n/a)</td><td>308.00 (n/a)</td><td>248.00 (n/a)</td><td>152.90 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (+3.82%)</td><td>0.08 <b>(+26.61%)</b></td><td>0.08 (-2.31%)</td><td>0.06 <b>(+318.21%)</b></td><td>0.02 <b>(-57.55%)</b></td><td>430.50 <b>(-76.09%)</b></td><td>316.84 <b>(-51.85%)</b></td><td>299.90 (+2.35%)</td><td>253.50 (-3.65%)</td><td>68.78 <b>(-89.57%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1800.40 (n/a)</td><td>658.02 (n/a)</td><td>293.00 (n/a)</td><td>263.10 (n/a)</td><td>659.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-16.77%)</td><td>0.05 (-8.22%)</td><td>0.06 (+17.64%)</td><td>0.03 <b>(-22.98%)</b></td><td>0.02 (-19.16%)</td><td>649.40 <b>(+29.85%)</b></td><td>388.90 (+8.92%)</td><td>298.60 (-14.98%)</td><td>246.40 <b>(+20.14%)</b></td><td>166.28 <b>(+23.99%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>500.10 (n/a)</td><td>357.06 (n/a)</td><td>351.20 (n/a)</td><td>205.10 (n/a)</td><td>134.11 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-16.46%)</td><td>0.06 (+11.31%)</td><td>0.06 <b>(+54.63%)</b></td><td>0.03 (-3.09%)</td><td>0.02 <b>(-35.59%)</b></td><td>623.50 (+3.19%)</td><td>361.26 (-16.47%)</td><td>302.00 <b>(-35.32%)</b></td><td>273.00 (+19.68%)</td><td>147.33 (-17.60%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.20 (n/a)</td><td>432.48 (n/a)</td><td>466.90 (n/a)</td><td>228.10 (n/a)</td><td>178.81 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (-15.50%)</td><td>0.04 (-12.36%)</td><td>0.04 (-17.98%)</td><td>0.03 (-10.80%)</td><td>0.02 (-8.58%)</td><td>586.70 (+12.09%)</td><td>454.24 (+15.17%)</td><td>525.40 <b>(+21.93%)</b></td><td>284.50 (+18.34%)</td><td>149.93 (+19.83%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>523.40 (n/a)</td><td>394.40 (n/a)</td><td>430.90 (n/a)</td><td>240.40 (n/a)</td><td>125.12 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 <b>(-21.74%)</b></td><td>0.06 (-1.05%)</td><td>0.06 (-0.69%)</td><td>0.03 (-3.69%)</td><td>0.01 <b>(-33.22%)</b></td><td>562.30 (+3.82%)</td><td>353.96 (-2.91%)</td><td>302.30 (+0.70%)</td><td>294.30 <b>(+27.79%)</b></td><td>116.61 (-12.40%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.60 (n/a)</td><td>364.56 (n/a)</td><td>300.20 (n/a)</td><td>230.30 (n/a)</td><td>133.11 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-10.40%)</td><td>0.05 (+1.16%)</td><td>0.06 <b>(+32.35%)</b></td><td>0.03 (-19.11%)</td><td>0.02 (+6.94%)</td><td>675.20 <b>(+23.62%)</b></td><td>420.26 (+3.38%)</td><td>306.90 <b>(-24.45%)</b></td><td>274.60 (+11.58%)</td><td>182.15 <b>(+41.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>546.20 (n/a)</td><td>406.50 (n/a)</td><td>406.20 (n/a)</td><td>246.10 (n/a)</td><td>128.44 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (-17.12%)</td><td>0.05 (-1.86%)</td><td>0.05 (+5.63%)</td><td>0.04 (+11.69%)</td><td>0.01 <b>(-40.79%)</b></td><td>505.90 (-10.46%)</td><td>380.84 (-5.24%)</td><td>367.00 (-5.34%)</td><td>294.80 <b>(+20.67%)</b></td><td>90.95 <b>(-38.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>565.00 (n/a)</td><td>401.92 (n/a)</td><td>387.70 (n/a)</td><td>244.30 (n/a)</td><td>148.75 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.34 (-17.15%)</td><td>0.25 (-14.96%)</td><td>0.22 <b>(-31.00%)</b></td><td>0.17 (-10.06%)</td><td>0.08 <b>(-20.07%)</b></td><td>591.40 (+11.19%)</td><td>431.60 (+14.62%)</td><td>445.60 <b>(+44.96%)</b></td><td>290.10 <b>(+20.67%)</b></td><td>137.02 (-4.56%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>531.90 (n/a)</td><td>376.54 (n/a)</td><td>307.40 (n/a)</td><td>240.40 (n/a)</td><td>143.57 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.40 (+19.22%)</td><td>0.27 (+3.19%)</td><td>0.33 (+10.00%)</td><td>0.05 <b>(-68.84%)</b></td><td>0.15 <b>(+101.98%)</b></td><td>1881.30 <b>(+220.88%)</b></td><td>635.32 <b>(+59.77%)</b></td><td>294.00 (-9.09%)</td><td>247.20 (-16.15%)</td><td>704.48 <b>(+452.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>586.30 (n/a)</td><td>397.64 (n/a)</td><td>323.40 (n/a)</td><td>294.80 (n/a)</td><td>127.59 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.36 <b>(+59.51%)</b></td><td>0.24 <b>(+21.47%)</b></td><td>0.21 (+2.95%)</td><td>0.18 (+10.31%)</td><td>0.08 <b>(+176.63%)</b></td><td>556.10 (-9.34%)</td><td>434.46 (-13.04%)</td><td>458.00 (-2.86%)</td><td>273.90 <b>(-37.32%)</b></td><td>120.62 <b>(+61.19%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>613.40 (n/a)</td><td>499.62 (n/a)</td><td>471.50 (n/a)</td><td>437.00 (n/a)</td><td>74.83 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.28 (-17.55%)</td><td>0.16 <b>(-34.83%)</b></td><td>0.13 <b>(-42.76%)</b></td><td>0.04 <b>(-76.82%)</b></td><td>0.10 <b>(+42.98%)</b></td><td>1931.80 <b>(+331.30%)</b></td><td>741.48 <b>(+132.69%)</b></td><td>546.40 <b>(+74.68%)</b></td><td>265.40 <b>(+21.30%)</b></td><td>685.06 <b>(+660.03%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>447.90 (n/a)</td><td>318.66 (n/a)</td><td>312.80 (n/a)</td><td>218.80 (n/a)</td><td>90.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.30 <b>(-31.76%)</b></td><td>0.22 (+1.21%)</td><td>0.26 <b>(+98.74%)</b></td><td>0.11 (+6.25%)</td><td>0.09 <b>(-41.54%)</b></td><td>679.80 (-5.88%)</td><td>399.82 (-16.34%)</td><td>278.20 <b>(-49.69%)</b></td><td>246.70 <b>(+46.50%)</b></td><td>193.04 <b>(-24.23%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.44 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.15 (n/a)</td><td>722.30 (n/a)</td><td>477.92 (n/a)</td><td>553.00 (n/a)</td><td>168.40 (n/a)</td><td>254.78 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.28 <b>(-24.10%)</b></td><td>0.18 (-18.11%)</td><td>0.16 (-4.54%)</td><td>0.13 (-2.15%)</td><td>0.06 <b>(-43.18%)</b></td><td>580.00 (+2.20%)</td><td>429.88 (+12.25%)</td><td>455.10 (+4.77%)</td><td>267.00 <b>(+31.72%)</b></td><td>118.63 <b>(-23.07%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>567.50 (n/a)</td><td>382.96 (n/a)</td><td>434.40 (n/a)</td><td>202.70 (n/a)</td><td>154.21 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-12.20%)</td><td>0.11 (+15.72%)</td><td>0.12 (+3.31%)</td><td>0.08 <b>(+118.99%)</b></td><td>0.02 <b>(-55.26%)</b></td><td>489.60 <b>(-54.33%)</b></td><td>345.54 <b>(-32.35%)</b></td><td>309.80 (-3.22%)</td><td>296.60 (+13.90%)</td><td>81.94 <b>(-76.13%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1072.10 (n/a)</td><td>510.74 (n/a)</td><td>320.10 (n/a)</td><td>260.40 (n/a)</td><td>343.25 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 <b>(-24.67%)</b></td><td>0.10 (-6.06%)</td><td>0.09 (-19.46%)</td><td>0.08 <b>(+22.24%)</b></td><td>0.02 <b>(-53.08%)</b></td><td>490.10 (-18.19%)</td><td>390.98 (-4.88%)</td><td>407.60 <b>(+24.15%)</b></td><td>306.50 <b>(+32.74%)</b></td><td>78.32 <b>(-55.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>599.10 (n/a)</td><td>411.02 (n/a)</td><td>328.30 (n/a)</td><td>230.90 (n/a)</td><td>174.97 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (+4.05%)</td><td>0.11 (-1.28%)</td><td>0.13 (+3.65%)</td><td>0.02 <b>(-76.72%)</b></td><td>0.06 <b>(+49.79%)</b></td><td>2437.00 <b>(+329.65%)</b></td><td>704.78 <b>(+96.34%)</b></td><td>289.00 (-3.51%)</td><td>233.80 (-3.87%)</td><td>968.61 <b>(+604.79%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>567.20 (n/a)</td><td>358.96 (n/a)</td><td>299.50 (n/a)</td><td>243.20 (n/a)</td><td>137.43 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (+2.41%)</td><td>0.11 (-8.13%)</td><td>0.09 <b>(-27.08%)</b></td><td>0.07 (-8.54%)</td><td>0.04 (+0.06%)</td><td>535.10 (+9.34%)</td><td>377.72 (+8.93%)</td><td>394.10 <b>(+37.13%)</b></td><td>235.60 (-2.36%)</td><td>121.47 (+2.53%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>489.40 (n/a)</td><td>346.76 (n/a)</td><td>287.40 (n/a)</td><td>241.30 (n/a)</td><td>118.48 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (-19.76%)</td><td>0.10 (+11.95%)</td><td>0.10 <b>(+57.11%)</b></td><td>0.07 (+9.81%)</td><td>0.02 <b>(-44.65%)</b></td><td>527.30 (-8.93%)</td><td>384.90 (-17.68%)</td><td>352.60 <b>(-36.34%)</b></td><td>281.40 <b>(+24.62%)</b></td><td>96.27 <b>(-36.83%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>579.00 (n/a)</td><td>467.54 (n/a)</td><td>553.90 (n/a)</td><td>225.80 (n/a)</td><td>152.39 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-19.53%)</td><td>0.08 (-11.26%)</td><td>0.08 (+1.98%)</td><td>0.04 <b>(-47.94%)</b></td><td>0.03 (-2.74%)</td><td>1001.50 <b>(+92.12%)</b></td><td>516.82 <b>(+23.75%)</b></td><td>452.10 (-1.93%)</td><td>302.80 <b>(+24.25%)</b></td><td>280.11 <b>(+151.68%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>521.30 (n/a)</td><td>417.62 (n/a)</td><td>461.00 (n/a)</td><td>243.70 (n/a)</td><td>111.29 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (-1.59%)</td><td>0.11 (-13.70%)</td><td>0.11 (-17.15%)</td><td>0.05 <b>(-26.96%)</b></td><td>0.05 <b>(+30.28%)</b></td><td>845.90 <b>(+36.92%)</b></td><td>458.78 <b>(+27.07%)</b></td><td>383.80 <b>(+20.69%)</b></td><td>259.40 (+1.61%)</td><td>240.91 <b>(+64.89%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>617.80 (n/a)</td><td>361.04 (n/a)</td><td>318.00 (n/a)</td><td>255.30 (n/a)</td><td>146.10 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.18 (+9.62%)</td><td>0.12 (-7.42%)</td><td>0.13 (-5.03%)</td><td>0.08 (-6.89%)</td><td>0.04 <b>(+42.80%)</b></td><td>503.40 (+7.40%)</td><td>367.12 (+12.57%)</td><td>310.10 (+5.30%)</td><td>233.50 (-8.79%)</td><td>118.01 <b>(+41.61%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>468.70 (n/a)</td><td>326.12 (n/a)</td><td>294.50 (n/a)</td><td>256.00 (n/a)</td><td>83.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.15 (-7.25%)</td><td>0.11 (-12.22%)</td><td>0.09 <b>(-35.73%)</b></td><td>0.07 <b>(+33.49%)</b></td><td>0.03 <b>(-20.20%)</b></td><td>575.10 <b>(-25.08%)</b></td><td>419.24 (+5.33%)</td><td>464.20 <b>(+55.62%)</b></td><td>280.10 (+7.81%)</td><td>127.94 <b>(-40.00%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>767.60 (n/a)</td><td>398.04 (n/a)</td><td>298.30 (n/a)</td><td>259.80 (n/a)</td><td>213.24 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (-4.10%)</td><td>0.11 (-8.07%)</td><td>0.09 (-8.09%)</td><td>0.07 (-6.15%)</td><td>0.04 (+1.84%)</td><td>568.60 (+6.56%)</td><td>426.54 (+10.71%)</td><td>463.00 (+8.81%)</td><td>256.60 (+4.27%)</td><td>144.15 (+18.45%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>533.60 (n/a)</td><td>385.28 (n/a)</td><td>425.50 (n/a)</td><td>246.10 (n/a)</td><td>121.70 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.17 (+9.36%)</td><td>0.11 <b>(+20.54%)</b></td><td>0.12 <b>(+53.41%)</b></td><td>0.04 <b>(-45.71%)</b></td><td>0.05 <b>(+39.41%)</b></td><td>1115.30 <b>(+84.19%)</b></td><td>482.32 (+0.20%)</td><td>348.30 <b>(-34.81%)</b></td><td>247.80 (-8.56%)</td><td>358.11 <b>(+167.68%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>605.50 (n/a)</td><td>481.38 (n/a)</td><td>534.30 (n/a)</td><td>271.00 (n/a)</td><td>133.78 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 <b>(-21.97%)</b></td><td>0.08 <b>(-33.90%)</b></td><td>0.09 <b>(-35.91%)</b></td><td>0.02 <b>(-71.34%)</b></td><td>0.04 (-7.33%)</td><td>1897.90 <b>(+248.94%)</b></td><td>727.08 <b>(+98.73%)</b></td><td>468.90 <b>(+56.04%)</b></td><td>311.70 <b>(+28.17%)</b></td><td>658.41 <b>(+377.81%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>543.90 (n/a)</td><td>365.86 (n/a)</td><td>300.50 (n/a)</td><td>243.20 (n/a)</td><td>137.80 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.15 <b>(+20.71%)</b></td><td>0.10 (+9.50%)</td><td>0.08 (+13.23%)</td><td>0.07 (-5.23%)</td><td>0.03 <b>(+33.66%)</b></td><td>528.70 (+5.51%)</td><td>386.28 (-5.88%)</td><td>410.10 (-11.67%)</td><td>237.40 (-17.17%)</td><td>122.83 (+15.33%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.10 (n/a)</td><td>410.40 (n/a)</td><td>464.30 (n/a)</td><td>286.60 (n/a)</td><td>106.51 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-11.35%)</td><td>0.09 (+10.35%)</td><td>0.07 (-0.25%)</td><td>0.07 (+18.47%)</td><td>0.02 <b>(-21.64%)</b></td><td>495.60 (-15.60%)</td><td>405.48 (-12.21%)</td><td>466.70 (+0.26%)</td><td>290.90 (+12.80%)</td><td>98.32 <b>(-23.43%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.20 (n/a)</td><td>461.90 (n/a)</td><td>465.50 (n/a)</td><td>257.90 (n/a)</td><td>128.40 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.15 <b>(+23.51%)</b></td><td>0.11 <b>(+44.28%)</b></td><td>0.12 <b>(+70.32%)</b></td><td>0.08 <b>(+40.58%)</b></td><td>0.03 (+5.10%)</td><td>425.00 <b>(-28.87%)</b></td><td>326.12 <b>(-32.09%)</b></td><td>300.90 <b>(-41.29%)</b></td><td>233.60 (-19.03%)</td><td>76.12 <b>(-35.61%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>597.50 (n/a)</td><td>480.24 (n/a)</td><td>512.50 (n/a)</td><td>288.50 (n/a)</td><td>118.21 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 <b>(+30.45%)</b></td><td>0.09 <b>(+46.57%)</b></td><td>0.07 (-7.53%)</td><td>0.06 <b>(+309.64%)</b></td><td>0.03 (-18.57%)</td><td>604.00 <b>(-75.59%)</b></td><td>442.10 <b>(-60.40%)</b></td><td>468.90 (+8.14%)</td><td>263.90 <b>(-23.33%)</b></td><td>152.12 <b>(-84.90%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2474.10 (n/a)</td><td>1116.30 (n/a)</td><td>433.60 (n/a)</td><td>344.20 (n/a)</td><td>1007.66 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-18.29%)</td><td>0.10 (-7.33%)</td><td>0.09 (-9.22%)</td><td>0.07 (-6.94%)</td><td>0.02 <b>(-22.44%)</b></td><td>478.70 (+7.45%)</td><td>371.72 (+7.02%)</td><td>389.30 (+10.16%)</td><td>284.80 <b>(+22.39%)</b></td><td>79.34 (+3.38%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>445.50 (n/a)</td><td>347.34 (n/a)</td><td>353.40 (n/a)</td><td>232.70 (n/a)</td><td>76.74 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (-13.81%)</td><td>0.09 (-12.94%)</td><td>0.11 <b>(+23.29%)</b></td><td>0.05 (-18.98%)</td><td>0.04 <b>(-22.91%)</b></td><td>705.90 <b>(+23.43%)</b></td><td>430.74 (+13.84%)</td><td>325.70 (-18.90%)</td><td>255.50 (+16.03%)</td><td>188.52 <b>(+22.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>571.90 (n/a)</td><td>378.38 (n/a)</td><td>401.60 (n/a)</td><td>220.20 (n/a)</td><td>154.22 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.51 <b>(+26.26%)</b></td><td>0.29 (-7.52%)</td><td>0.23 (-8.74%)</td><td>0.21 (-14.90%)</td><td>0.13 <b>(+55.77%)</b></td><td>625.30 (+17.52%)</td><td>510.72 (+14.55%)</td><td>562.40 (+9.57%)</td><td>258.70 <b>(-20.79%)</b></td><td>152.47 <b>(+43.29%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>532.10 (n/a)</td><td>445.86 (n/a)</td><td>513.30 (n/a)</td><td>326.60 (n/a)</td><td>106.41 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.54 (+19.09%)</td><td>0.35 (+12.17%)</td><td>0.29 (+11.68%)</td><td>0.27 <b>(+40.25%)</b></td><td>0.11 (-0.88%)</td><td>493.20 <b>(-28.70%)</b></td><td>399.04 (-14.16%)</td><td>453.80 (-10.46%)</td><td>244.90 (-16.02%)</td><td>105.76 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>691.70 (n/a)</td><td>464.84 (n/a)</td><td>506.80 (n/a)</td><td>291.60 (n/a)</td><td>166.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.43 (-9.48%)</td><td>0.26 (-17.82%)</td><td>0.27 (-7.28%)</td><td>0.13 <b>(-23.41%)</b></td><td>0.13 (+15.80%)</td><td>1026.20 <b>(+30.56%)</b></td><td>640.98 <b>(+37.99%)</b></td><td>481.30 (+7.87%)</td><td>307.30 (+10.46%)</td><td>356.06 <b>(+80.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>786.00 (n/a)</td><td>464.52 (n/a)</td><td>446.20 (n/a)</td><td>278.20 (n/a)</td><td>196.87 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.00 (+16.67%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+2.06%)</td><td>18448.59 (+2.66%)</td><td>15470.64 <b>(+20.30%)</b></td><td>17338.69 (+5.16%)</td><td>6145.00 (-5.83%)</td><td>5253.32 (-8.61%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17970.45 (n/a)</td><td>12860.09 (n/a)</td><td>16487.71 (n/a)</td><td>6525.30 (n/a)</td><td>5748.02 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.00 <b>(-54.55%)</b></td><td>0.00 <b>(-31.25%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-80.39%)</b></td><td>23053.21 <b>(+25.48%)</b></td><td>19483.80 <b>(+34.06%)</b></td><td>18263.09 (+5.26%)</td><td>16655.72 <b>(+129.99%)</b></td><td>3047.37 <b>(-35.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18371.92 (n/a)</td><td>14533.95 (n/a)</td><td>17350.31 (n/a)</td><td>7241.89 (n/a)</td><td>4744.93 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (+1.44%)</td><td>0.09 (-8.22%)</td><td>0.09 (-6.28%)</td><td>0.08 (+6.36%)</td><td>0.03 (-17.43%)</td><td>27846.86 (-5.98%)</td><td>23287.16 (+6.00%)</td><td>24635.63 (+6.71%)</td><td>14911.68 (-1.44%)</td><td>4895.43 <b>(-24.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29619.26 (n/a)</td><td>21969.03 (n/a)</td><td>23085.78 (n/a)</td><td>15129.46 (n/a)</td><td>6477.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.22 <b>(-20.13%)</b></td><td>1.45 <b>(-31.11%)</b></td><td>1.33 <b>(-47.91%)</b></td><td>0.32 (+6.80%)</td><td>0.75 <b>(-26.30%)</b></td><td>3265.00 (-6.37%)</td><td>1166.56 (+13.53%)</td><td>789.10 <b>(+92.00%)</b></td><td>472.30 <b>(+25.18%)</b></td><td>1182.77 (-14.00%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.78 (n/a)</td><td>2.10 (n/a)</td><td>2.55 (n/a)</td><td>0.30 (n/a)</td><td>1.02 (n/a)</td><td>3487.20 (n/a)</td><td>1027.50 (n/a)</td><td>411.00 (n/a)</td><td>377.30 (n/a)</td><td>1375.29 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.39 (-10.87%)</td><td>1.86 (+5.09%)</td><td>1.74 (+6.23%)</td><td>1.50 <b>(+49.36%)</b></td><td>0.37 <b>(-42.51%)</b></td><td>701.00 <b>(-33.05%)</b></td><td>579.62 (-12.26%)</td><td>602.20 (-5.88%)</td><td>437.90 (+12.20%)</td><td>107.98 <b>(-57.03%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.69 (n/a)</td><td>1.77 (n/a)</td><td>1.64 (n/a)</td><td>1.00 (n/a)</td><td>0.64 (n/a)</td><td>1047.10 (n/a)</td><td>660.60 (n/a)</td><td>639.80 (n/a)</td><td>390.30 (n/a)</td><td>251.28 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.13 (+17.00%)</td><td>2.18 <b>(+29.03%)</b></td><td>1.69 <b>(+34.31%)</b></td><td>1.48 <b>(+30.23%)</b></td><td>0.79 (+16.30%)</td><td>707.00 <b>(-23.22%)</b></td><td>529.70 <b>(-23.71%)</b></td><td>619.80 <b>(-25.55%)</b></td><td>334.90 (-14.54%)</td><td>171.84 <b>(-27.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.68 (n/a)</td><td>1.69 (n/a)</td><td>1.26 (n/a)</td><td>1.14 (n/a)</td><td>0.68 (n/a)</td><td>920.80 (n/a)</td><td>694.34 (n/a)</td><td>832.50 (n/a)</td><td>391.90 (n/a)</td><td>235.52 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.52 <b>(-33.05%)</b></td><td>1.66 <b>(-33.52%)</b></td><td>1.50 <b>(-35.07%)</b></td><td>1.12 <b>(-40.30%)</b></td><td>0.53 <b>(-32.13%)</b></td><td>938.00 <b>(+67.50%)</b></td><td>679.88 <b>(+51.16%)</b></td><td>701.00 <b>(+54.00%)</b></td><td>415.90 <b>(+49.34%)</b></td><td>189.97 <b>(+61.44%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.77 (n/a)</td><td>2.49 (n/a)</td><td>2.30 (n/a)</td><td>1.87 (n/a)</td><td>0.78 (n/a)</td><td>560.00 (n/a)</td><td>449.78 (n/a)</td><td>455.20 (n/a)</td><td>278.50 (n/a)</td><td>117.67 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.84 (+3.79%)</td><td>2.28 (-15.76%)</td><td>2.40 (-16.94%)</td><td>0.58 <b>(-47.43%)</b></td><td>1.18 (+10.27%)</td><td>3612.70 <b>(+90.20%)</b></td><td>1379.62 <b>(+46.75%)</b></td><td>872.10 <b>(+20.41%)</b></td><td>546.30 (-3.65%)</td><td>1262.59 <b>(+127.31%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.70 (n/a)</td><td>2.71 (n/a)</td><td>2.90 (n/a)</td><td>1.10 (n/a)</td><td>1.07 (n/a)</td><td>1899.40 (n/a)</td><td>940.12 (n/a)</td><td>724.30 (n/a)</td><td>567.00 (n/a)</td><td>555.46 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.54 <b>(-33.69%)</b></td><td>2.26 <b>(-20.42%)</b></td><td>2.50 <b>(-28.87%)</b></td><td>0.65 (+13.09%)</td><td>1.07 <b>(-50.53%)</b></td><td>3216.00 (-11.58%)</td><td>1304.12 <b>(-25.23%)</b></td><td>838.70 <b>(+40.60%)</b></td><td>591.90 <b>(+50.80%)</b></td><td>1083.62 <b>(-36.61%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.34 (n/a)</td><td>2.84 (n/a)</td><td>3.52 (n/a)</td><td>0.58 (n/a)</td><td>2.16 (n/a)</td><td>3637.00 (n/a)</td><td>1744.20 (n/a)</td><td>596.50 (n/a)</td><td>392.50 (n/a)</td><td>1709.44 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.81 (-19.40%)</td><td>2.47 (+11.10%)</td><td>3.20 <b>(+51.55%)</b></td><td>0.59 (-5.70%)</td><td>1.51 (-1.88%)</td><td>3526.30 (+6.05%)</td><td>1441.92 (+0.33%)</td><td>654.80 <b>(-34.01%)</b></td><td>551.10 <b>(+24.07%)</b></td><td>1296.53 (+15.86%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.72 (n/a)</td><td>2.22 (n/a)</td><td>2.11 (n/a)</td><td>0.63 (n/a)</td><td>1.54 (n/a)</td><td>3325.20 (n/a)</td><td>1437.16 (n/a)</td><td>992.30 (n/a)</td><td>444.20 (n/a)</td><td>1119.05 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.96 <b>(-40.24%)</b></td><td>3.48 (-5.79%)</td><td>3.48 <b>(+21.72%)</b></td><td>2.99 <b>(+41.11%)</b></td><td>0.43 <b>(-75.71%)</b></td><td>702.00 <b>(-29.13%)</b></td><td>610.22 (-7.77%)</td><td>602.30 (-17.84%)</td><td>529.10 <b>(+67.33%)</b></td><td>76.79 <b>(-70.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.63 (n/a)</td><td>3.69 (n/a)</td><td>2.86 (n/a)</td><td>2.12 (n/a)</td><td>1.79 (n/a)</td><td>990.50 (n/a)</td><td>661.66 (n/a)</td><td>733.10 (n/a)</td><td>316.20 (n/a)</td><td>256.49 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>4.97 (-17.65%)</td><td>3.66 <b>(+118.32%)</b></td><td>3.61 <b>(+516.73%)</b></td><td>2.72 <b>(+368.60%)</b></td><td>0.89 <b>(-63.56%)</b></td><td>770.10 <b>(-78.66%)</b></td><td>599.86 <b>(-79.56%)</b></td><td>580.60 <b>(-83.78%)</b></td><td>422.10 <b>(+21.43%)</b></td><td>138.61 <b>(-90.41%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.03 (n/a)</td><td>1.68 (n/a)</td><td>0.59 (n/a)</td><td>0.58 (n/a)</td><td>2.44 (n/a)</td><td>3608.90 (n/a)</td><td>2934.08 (n/a)</td><td>3580.50 (n/a)</td><td>347.60 (n/a)</td><td>1446.05 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.50 <b>(-39.86%)</b></td><td>2.39 <b>(-22.11%)</b></td><td>2.61 <b>(-33.86%)</b></td><td>0.60 (+1.67%)</td><td>1.07 <b>(-54.57%)</b></td><td>3506.30 (-1.64%)</td><td>1303.18 <b>(-22.89%)</b></td><td>804.10 <b>(+51.18%)</b></td><td>599.10 <b>(+66.28%)</b></td><td>1234.86 <b>(-26.89%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.82 (n/a)</td><td>3.06 (n/a)</td><td>3.94 (n/a)</td><td>0.59 (n/a)</td><td>2.36 (n/a)</td><td>3564.80 (n/a)</td><td>1690.00 (n/a)</td><td>531.90 (n/a)</td><td>360.30 (n/a)</td><td>1689.10 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>5.24 (-0.48%)</td><td>3.15 <b>(-31.49%)</b></td><td>4.02 <b>(-23.18%)</b></td><td>1.20 <b>(-65.84%)</b></td><td>1.84 <b>(+103.14%)</b></td><td>3504.00 <b>(+192.71%)</b></td><td>1975.86 <b>(+108.98%)</b></td><td>1043.80 <b>(+30.18%)</b></td><td>800.60 (+0.49%)</td><td>1397.32 <b>(+590.27%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.26 (n/a)</td><td>4.59 (n/a)</td><td>5.23 (n/a)</td><td>3.50 (n/a)</td><td>0.91 (n/a)</td><td>1197.10 (n/a)</td><td>945.48 (n/a)</td><td>801.80 (n/a)</td><td>796.70 (n/a)</td><td>202.43 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>7.91 (+8.96%)</td><td>4.96 (-11.23%)</td><td>5.65 (-4.55%)</td><td>1.19 <b>(-68.96%)</b></td><td>2.51 <b>(+48.76%)</b></td><td>3536.30 <b>(+222.21%)</b></td><td>1306.90 <b>(+60.76%)</b></td><td>742.70 (+4.77%)</td><td>530.10 (-8.22%)</td><td>1258.76 <b>(+380.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>7.26 (n/a)</td><td>5.59 (n/a)</td><td>5.92 (n/a)</td><td>3.82 (n/a)</td><td>1.69 (n/a)</td><td>1097.50 (n/a)</td><td>812.96 (n/a)</td><td>708.90 (n/a)</td><td>577.60 (n/a)</td><td>261.82 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>7.53 (-2.46%)</td><td>5.44 (-11.85%)</td><td>6.05 (-7.56%)</td><td>1.31 <b>(-65.81%)</b></td><td>2.41 <b>(+63.50%)</b></td><td>3206.30 <b>(+192.44%)</b></td><td>1165.08 <b>(+61.67%)</b></td><td>693.20 (+8.18%)</td><td>557.00 (+2.52%)</td><td>1142.97 <b>(+421.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>7.72 (n/a)</td><td>6.17 (n/a)</td><td>6.55 (n/a)</td><td>3.83 (n/a)</td><td>1.47 (n/a)</td><td>1096.40 (n/a)</td><td>720.66 (n/a)</td><td>640.80 (n/a)</td><td>543.30 (n/a)</td><td>219.05 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>9.09 (-16.00%)</td><td>6.42 (-16.52%)</td><td>6.84 (-1.16%)</td><td>4.11 (+0.70%)</td><td>2.13 <b>(-25.28%)</b></td><td>1021.20 (-0.69%)</td><td>718.78 (+16.11%)</td><td>613.00 (+1.19%)</td><td>461.30 (+19.05%)</td><td>250.72 (-3.44%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>10.83 (n/a)</td><td>7.69 (n/a)</td><td>6.92 (n/a)</td><td>4.08 (n/a)</td><td>2.86 (n/a)</td><td>1028.30 (n/a)</td><td>619.04 (n/a)</td><td>605.80 (n/a)</td><td>387.50 (n/a)</td><td>259.64 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>7.65 <b>(-20.92%)</b></td><td>5.20 <b>(-31.77%)</b></td><td>5.22 <b>(-39.00%)</b></td><td>1.75 <b>(-55.85%)</b></td><td>2.41 (-0.68%)</td><td>2401.00 <b>(+126.49%)</b></td><td>1068.26 <b>(+73.57%)</b></td><td>803.80 <b>(+63.94%)</b></td><td>547.90 <b>(+26.45%)</b></td><td>767.92 <b>(+191.22%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>9.68 (n/a)</td><td>7.62 (n/a)</td><td>8.55 (n/a)</td><td>3.96 (n/a)</td><td>2.42 (n/a)</td><td>1060.10 (n/a)</td><td>615.48 (n/a)</td><td>490.30 (n/a)</td><td>433.30 (n/a)</td><td>263.69 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>10.04 (+5.86%)</td><td>6.35 <b>(+23.02%)</b></td><td>6.82 <b>(+55.09%)</b></td><td>1.18 <b>(-30.10%)</b></td><td>3.21 (+8.89%)</td><td>3542.60 <b>(+43.07%)</b></td><td>1159.54 (+3.15%)</td><td>614.70 <b>(-35.53%)</b></td><td>417.70 (-5.54%)</td><td>1334.87 <b>(+67.35%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>9.48 (n/a)</td><td>5.17 (n/a)</td><td>4.40 (n/a)</td><td>1.69 (n/a)</td><td>2.94 (n/a)</td><td>2476.20 (n/a)</td><td>1124.10 (n/a)</td><td>953.40 (n/a)</td><td>442.20 (n/a)</td><td>797.65 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>1.78 (+5.25%)</td><td>1.04 <b>(-32.80%)</b></td><td>1.05 <b>(-34.41%)</b></td><td>0.22 <b>(-83.58%)</b></td><td>0.59 <b>(+337.78%)</b></td><td>2401.30 <b>(+509.00%)</b></td><td>847.00 <b>(+149.13%)</b></td><td>501.40 <b>(+52.49%)</b></td><td>295.20 (-4.99%)</td><td>879.41 <b>(+2642.72%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>1.69 (n/a)</td><td>1.55 (n/a)</td><td>1.59 (n/a)</td><td>1.33 (n/a)</td><td>0.13 (n/a)</td><td>394.30 (n/a)</td><td>339.98 (n/a)</td><td>328.80 (n/a)</td><td>310.70 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.45 (-9.75%)</td><td>1.49 <b>(-35.23%)</b></td><td>1.66 <b>(-31.22%)</b></td><td>0.54 <b>(-64.59%)</b></td><td>0.73 <b>(+58.74%)</b></td><td>1956.00 <b>(+182.37%)</b></td><td>921.64 <b>(+94.36%)</b></td><td>633.00 <b>(+45.38%)</b></td><td>427.70 (+10.80%)</td><td>615.32 <b>(+396.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.72 (n/a)</td><td>2.31 (n/a)</td><td>2.41 (n/a)</td><td>1.51 (n/a)</td><td>0.46 (n/a)</td><td>692.70 (n/a)</td><td>474.20 (n/a)</td><td>435.40 (n/a)</td><td>386.00 (n/a)</td><td>123.82 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.98 <b>(-27.43%)</b></td><td>1.32 <b>(-52.59%)</b></td><td>0.99 <b>(-66.76%)</b></td><td>0.60 <b>(-38.58%)</b></td><td>0.95 <b>(-27.40%)</b></td><td>3497.40 <b>(+62.82%)</b></td><td>2098.90 <b>(+111.22%)</b></td><td>2111.80 <b>(+200.83%)</b></td><td>703.40 <b>(+37.81%)</b></td><td>988.35 <b>(+45.15%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.11 (n/a)</td><td>2.78 (n/a)</td><td>2.99 (n/a)</td><td>0.98 (n/a)</td><td>1.30 (n/a)</td><td>2148.00 (n/a)</td><td>993.68 (n/a)</td><td>702.00 (n/a)</td><td>510.40 (n/a)</td><td>680.91 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>1.72 <b>(-22.65%)</b></td><td>1.32 <b>(+22.45%)</b></td><td>1.42 <b>(+69.59%)</b></td><td>0.76 <b>(+27.93%)</b></td><td>0.35 <b>(-46.24%)</b></td><td>685.60 <b>(-21.83%)</b></td><td>428.30 <b>(-27.87%)</b></td><td>369.80 <b>(-41.04%)</b></td><td>304.40 <b>(+29.31%)</b></td><td>149.25 <b>(-36.41%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.23 (n/a)</td><td>1.08 (n/a)</td><td>0.84 (n/a)</td><td>0.60 (n/a)</td><td>0.66 (n/a)</td><td>877.10 (n/a)</td><td>593.76 (n/a)</td><td>627.20 (n/a)</td><td>235.40 (n/a)</td><td>234.68 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.21 <b>(+99.48%)</b></td><td>0.09 (+9.68%)</td><td>0.07 (-15.43%)</td><td>0.02 <b>(-75.66%)</b></td><td>0.07 <b>(+389.85%)</b></td><td>1969.70 <b>(+310.78%)</b></td><td>696.96 <b>(+68.98%)</b></td><td>477.20 (+18.24%)</td><td>156.50 <b>(-49.86%)</b></td><td>724.31 <b>(+975.74%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>479.50 (n/a)</td><td>412.46 (n/a)</td><td>403.60 (n/a)</td><td>312.10 (n/a)</td><td>67.33 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (-7.03%)</td><td>0.09 (-8.28%)</td><td>0.08 (-15.74%)</td><td>0.05 <b>(-21.13%)</b></td><td>0.03 (+4.13%)</td><td>663.40 <b>(+26.80%)</b></td><td>432.78 (+12.23%)</td><td>393.10 (+18.69%)</td><td>267.20 (+7.57%)</td><td>166.52 <b>(+31.13%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>523.20 (n/a)</td><td>385.62 (n/a)</td><td>331.20 (n/a)</td><td>248.40 (n/a)</td><td>126.99 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.22 (-11.60%)</td><td>0.18 (-8.26%)</td><td>0.21 (+11.38%)</td><td>0.11 <b>(-25.42%)</b></td><td>0.05 <b>(+34.84%)</b></td><td>599.40 <b>(+34.09%)</b></td><td>401.50 (+14.75%)</td><td>309.00 (-10.23%)</td><td>300.60 (+13.14%)</td><td>137.62 <b>(+96.19%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>447.00 (n/a)</td><td>349.90 (n/a)</td><td>344.20 (n/a)</td><td>265.70 (n/a)</td><td>70.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.27 (-14.42%)</td><td>0.18 (-16.33%)</td><td>0.17 <b>(-21.11%)</b></td><td>0.08 <b>(-40.68%)</b></td><td>0.09 <b>(+27.70%)</b></td><td>805.80 <b>(+68.58%)</b></td><td>462.40 <b>(+38.78%)</b></td><td>382.80 <b>(+26.80%)</b></td><td>239.10 (+16.81%)</td><td>248.89 <b>(+142.94%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>478.00 (n/a)</td><td>333.20 (n/a)</td><td>301.90 (n/a)</td><td>204.70 (n/a)</td><td>102.45 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.28 (+9.22%)</td><td>0.18 (-1.33%)</td><td>0.14 (-8.33%)</td><td>0.12 (+7.43%)</td><td>0.07 (+14.33%)</td><td>555.60 (-6.92%)</td><td>421.24 (+3.52%)</td><td>478.00 (+9.08%)</td><td>235.20 (-8.45%)</td><td>149.40 (+5.83%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>596.90 (n/a)</td><td>406.92 (n/a)</td><td>438.20 (n/a)</td><td>256.90 (n/a)</td><td>141.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.60 (+3.05%)</td><td>0.37 <b>(-23.36%)</b></td><td>0.29 <b>(-45.36%)</b></td><td>0.20 <b>(-29.52%)</b></td><td>0.17 <b>(+37.85%)</b></td><td>641.50 <b>(+41.89%)</b></td><td>422.96 <b>(+43.83%)</b></td><td>456.10 <b>(+83.03%)</b></td><td>218.90 (-2.97%)</td><td>178.32 <b>(+86.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.53 (n/a)</td><td>0.29 (n/a)</td><td>0.12 (n/a)</td><td>452.10 (n/a)</td><td>294.06 (n/a)</td><td>249.20 (n/a)</td><td>225.60 (n/a)</td><td>95.52 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.47 (-3.29%)</td><td>0.37 (+15.83%)</td><td>0.42 <b>(+60.20%)</b></td><td>0.24 (+19.60%)</td><td>0.11 (-15.59%)</td><td>553.70 (-16.38%)</td><td>387.34 (-17.49%)</td><td>311.80 <b>(-37.57%)</b></td><td>276.40 (+3.40%)</td><td>129.69 <b>(-25.98%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>662.20 (n/a)</td><td>469.44 (n/a)</td><td>499.40 (n/a)</td><td>267.30 (n/a)</td><td>175.20 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.44 (-0.40%)</td><td>0.33 (-0.21%)</td><td>0.30 (-14.81%)</td><td>0.26 <b>(+29.22%)</b></td><td>0.07 <b>(-29.33%)</b></td><td>507.80 <b>(-22.60%)</b></td><td>414.18 (-4.77%)</td><td>436.00 (+17.39%)</td><td>299.00 (+0.40%)</td><td>78.67 <b>(-46.81%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>656.10 (n/a)</td><td>434.94 (n/a)</td><td>371.40 (n/a)</td><td>297.80 (n/a)</td><td>147.92 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (-1.35%)</td><td>0.05 (-2.90%)</td><td>0.04 (+2.63%)</td><td>0.03 (+18.62%)</td><td>0.01 <b>(-24.13%)</b></td><td>515.40 (-15.69%)</td><td>376.36 (-2.73%)</td><td>365.00 (-2.56%)</td><td>246.20 (+1.36%)</td><td>109.60 <b>(-29.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.30 (n/a)</td><td>386.92 (n/a)</td><td>374.60 (n/a)</td><td>242.90 (n/a)</td><td>156.08 (n/a)</td>
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
