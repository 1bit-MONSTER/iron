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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-0.98%)</td><td>0.02 <b>(+26.84%)</b></td><td>0.03 <b>(+61.33%)</b></td><td>0.01 <b>(+38.36%)</b></td><td>0.00 <b>(-35.82%)</b></td><td>410.60 <b>(-27.72%)</b></td><td>280.66 <b>(-28.26%)</b></td><td>238.80 <b>(-38.02%)</b></td><td>235.20 (+0.99%)</td><td>75.35 <b>(-51.98%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>391.24 (n/a)</td><td>385.30 (n/a)</td><td>232.90 (n/a)</td><td>156.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-0.18%)</td><td>0.02 (-7.02%)</td><td>0.02 <b>(-21.79%)</b></td><td>0.01 (-9.97%)</td><td>0.01 <b>(+48.73%)</b></td><td>514.00 (+11.09%)</td><td>369.14 (+12.97%)</td><td>398.20 <b>(+27.87%)</b></td><td>246.00 (+0.20%)</td><td>119.38 <b>(+47.54%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.70 (n/a)</td><td>326.76 (n/a)</td><td>311.40 (n/a)</td><td>245.50 (n/a)</td><td>80.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (+13.23%)</td><td>0.02 (+15.70%)</td><td>0.02 <b>(+24.77%)</b></td><td>0.01 (-9.11%)</td><td>0.01 <b>(+23.87%)</b></td><td>552.70 (+10.01%)</td><td>340.98 (-11.02%)</td><td>305.70 (-19.85%)</td><td>230.80 (-11.67%)</td><td>132.49 (+16.40%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>502.40 (n/a)</td><td>383.20 (n/a)</td><td>381.40 (n/a)</td><td>261.30 (n/a)</td><td>113.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 <b>(+81.59%)</b></td><td>0.02 <b>(+63.92%)</b></td><td>0.02 <b>(+79.05%)</b></td><td>0.01 <b>(+38.77%)</b></td><td>0.01 <b>(+116.09%)</b></td><td>456.80 <b>(-27.94%)</b></td><td>285.90 <b>(-35.24%)</b></td><td>245.80 <b>(-44.15%)</b></td><td>148.90 <b>(-44.93%)</b></td><td>115.62 (-13.02%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.90 (n/a)</td><td>441.46 (n/a)</td><td>440.10 (n/a)</td><td>270.40 (n/a)</td><td>132.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 <b>(+22.92%)</b></td><td>0.02 <b>(+53.64%)</b></td><td>0.02 <b>(+77.16%)</b></td><td>0.02 <b>(+112.91%)</b></td><td>0.00 <b>(-25.71%)</b></td><td>374.30 <b>(-53.04%)</b></td><td>314.54 <b>(-39.82%)</b></td><td>304.00 <b>(-43.56%)</b></td><td>243.40 (-18.65%)</td><td>53.79 <b>(-70.69%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>797.00 (n/a)</td><td>522.70 (n/a)</td><td>538.60 (n/a)</td><td>299.20 (n/a)</td><td>183.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-11.37%)</td><td>0.02 (-4.10%)</td><td>0.01 (+1.89%)</td><td>0.01 (-19.45%)</td><td>0.00 (-11.11%)</td><td>664.10 <b>(+24.15%)</b></td><td>446.52 (+4.62%)</td><td>469.10 (-1.86%)</td><td>282.80 (+12.80%)</td><td>148.94 (+19.03%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.90 (n/a)</td><td>426.82 (n/a)</td><td>478.00 (n/a)</td><td>250.70 (n/a)</td><td>125.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (-3.06%)</td><td>0.03 <b>(-29.22%)</b></td><td>0.02 <b>(-40.90%)</b></td><td>0.02 <b>(-37.68%)</b></td><td>0.01 <b>(+79.29%)</b></td><td>559.60 <b>(+60.48%)</b></td><td>458.28 <b>(+52.92%)</b></td><td>503.50 <b>(+69.19%)</b></td><td>238.80 (+3.15%)</td><td>130.63 <b>(+190.76%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>348.70 (n/a)</td><td>299.68 (n/a)</td><td>297.60 (n/a)</td><td>231.50 (n/a)</td><td>44.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (-0.35%)</td><td>0.04 (+17.42%)</td><td>0.04 <b>(+49.59%)</b></td><td>0.03 <b>(+31.95%)</b></td><td>0.01 <b>(-38.38%)</b></td><td>393.70 <b>(-24.22%)</b></td><td>323.70 <b>(-20.33%)</b></td><td>314.40 <b>(-33.13%)</b></td><td>245.70 (+0.37%)</td><td>58.84 <b>(-53.82%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.50 (n/a)</td><td>406.28 (n/a)</td><td>470.20 (n/a)</td><td>244.80 (n/a)</td><td>127.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (+10.28%)</td><td>0.03 (+12.12%)</td><td>0.03 (+10.39%)</td><td>0.02 (-1.27%)</td><td>0.01 <b>(+41.22%)</b></td><td>558.90 (+1.29%)</td><td>401.24 (-7.55%)</td><td>396.60 (-9.43%)</td><td>267.30 (-9.33%)</td><td>123.12 <b>(+33.39%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.80 (n/a)</td><td>434.02 (n/a)</td><td>437.90 (n/a)</td><td>294.80 (n/a)</td><td>92.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 <b>(+58.66%)</b></td><td>0.04 <b>(+60.98%)</b></td><td>0.04 <b>(+66.95%)</b></td><td>0.02 <b>(+85.58%)</b></td><td>0.02 <b>(+68.75%)</b></td><td>540.10 <b>(-46.11%)</b></td><td>358.38 <b>(-37.15%)</b></td><td>295.10 <b>(-40.11%)</b></td><td>185.80 <b>(-36.97%)</b></td><td>160.79 <b>(-39.36%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1002.20 (n/a)</td><td>570.24 (n/a)</td><td>492.70 (n/a)</td><td>294.80 (n/a)</td><td>265.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (-9.11%)</td><td>0.04 (+10.56%)</td><td>0.03 <b>(+37.76%)</b></td><td>0.02 <b>(+20.71%)</b></td><td>0.01 <b>(-37.06%)</b></td><td>546.30 (-17.15%)</td><td>368.78 (-16.30%)</td><td>352.70 <b>(-27.41%)</b></td><td>271.30 (+10.06%)</td><td>104.84 <b>(-37.77%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>659.40 (n/a)</td><td>440.58 (n/a)</td><td>485.90 (n/a)</td><td>246.50 (n/a)</td><td>168.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (-1.54%)</td><td>0.03 (+2.71%)</td><td>0.03 <b>(+24.92%)</b></td><td>0.02 (+5.41%)</td><td>0.01 (+1.55%)</td><td>590.40 (-5.13%)</td><td>441.50 (-2.18%)</td><td>383.10 (-19.94%)</td><td>311.90 (+1.56%)</td><td>131.40 (+4.84%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>622.30 (n/a)</td><td>451.32 (n/a)</td><td>478.50 (n/a)</td><td>307.10 (n/a)</td><td>125.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 <b>(-21.56%)</b></td><td>0.06 <b>(-28.48%)</b></td><td>0.06 <b>(-32.39%)</b></td><td>0.04 <b>(-22.83%)</b></td><td>0.02 <b>(-25.21%)</b></td><td>653.40 <b>(+29.59%)</b></td><td>459.96 <b>(+39.00%)</b></td><td>434.50 <b>(+47.89%)</b></td><td>313.70 <b>(+27.47%)</b></td><td>128.27 <b>(+22.83%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>504.20 (n/a)</td><td>330.90 (n/a)</td><td>293.80 (n/a)</td><td>246.10 (n/a)</td><td>104.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 <b>(-24.80%)</b></td><td>0.06 <b>(-30.75%)</b></td><td>0.06 <b>(-34.99%)</b></td><td>0.01 <b>(-74.57%)</b></td><td>0.03 (-2.87%)</td><td>2083.30 <b>(+293.30%)</b></td><td>720.74 <b>(+113.07%)</b></td><td>381.30 <b>(+53.81%)</b></td><td>276.80 <b>(+33.01%)</b></td><td>768.94 <b>(+429.37%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>529.70 (n/a)</td><td>338.26 (n/a)</td><td>247.90 (n/a)</td><td>208.10 (n/a)</td><td>145.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (-6.46%)</td><td>0.07 (-5.33%)</td><td>0.07 (-18.92%)</td><td>0.04 (-5.52%)</td><td>0.03 (-8.65%)</td><td>684.00 (+5.83%)</td><td>407.70 (+3.95%)</td><td>371.70 <b>(+23.32%)</b></td><td>249.50 (+6.90%)</td><td>177.75 (-0.91%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>646.30 (n/a)</td><td>392.20 (n/a)</td><td>301.40 (n/a)</td><td>233.40 (n/a)</td><td>179.39 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (-18.57%)</td><td>0.07 (+4.01%)</td><td>0.08 <b>(+64.98%)</b></td><td>0.04 (+2.46%)</td><td>0.02 <b>(-33.11%)</b></td><td>590.10 (-2.40%)</td><td>391.18 (-11.09%)</td><td>303.10 <b>(-39.38%)</b></td><td>284.10 <b>(+22.83%)</b></td><td>139.13 <b>(-23.36%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>604.60 (n/a)</td><td>439.96 (n/a)</td><td>500.00 (n/a)</td><td>231.30 (n/a)</td><td>181.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (-11.61%)</td><td>0.06 <b>(-28.94%)</b></td><td>0.05 <b>(-42.64%)</b></td><td>0.04 <b>(-37.57%)</b></td><td>0.02 <b>(+55.63%)</b></td><td>578.10 <b>(+60.18%)</b></td><td>428.22 <b>(+53.06%)</b></td><td>462.40 <b>(+74.36%)</b></td><td>252.10 (+13.15%)</td><td>147.49 <b>(+180.58%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>360.90 (n/a)</td><td>279.78 (n/a)</td><td>265.20 (n/a)</td><td>222.80 (n/a)</td><td>52.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (-11.20%)</td><td>0.07 (-10.26%)</td><td>0.07 (-18.73%)</td><td>0.05 (+13.93%)</td><td>0.01 <b>(-32.64%)</b></td><td>507.20 (-12.23%)</td><td>370.08 (+6.11%)</td><td>366.90 <b>(+23.04%)</b></td><td>279.90 (+12.59%)</td><td>86.42 <b>(-35.17%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.90 (n/a)</td><td>348.78 (n/a)</td><td>298.20 (n/a)</td><td>248.60 (n/a)</td><td>133.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.21 (-3.05%)</td><td>0.15 (-17.74%)</td><td>0.18 (+1.49%)</td><td>0.07 <b>(-54.73%)</b></td><td>0.06 <b>(+164.18%)</b></td><td>705.40 <b>(+120.85%)</b></td><td>395.86 <b>(+44.22%)</b></td><td>270.50 (-1.49%)</td><td>239.20 (+3.15%)</td><td>205.53 <b>(+484.65%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>319.40 (n/a)</td><td>274.48 (n/a)</td><td>274.60 (n/a)</td><td>231.90 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.24 (+17.56%)</td><td>0.18 (-2.03%)</td><td>0.20 (-0.17%)</td><td>0.09 (-12.42%)</td><td>0.06 <b>(+35.10%)</b></td><td>533.00 (+14.18%)</td><td>312.16 (+6.89%)</td><td>249.30 (+0.16%)</td><td>202.40 (-14.92%)</td><td>131.41 <b>(+33.76%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>466.80 (n/a)</td><td>292.04 (n/a)</td><td>248.90 (n/a)</td><td>237.90 (n/a)</td><td>98.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.19 (-1.73%)</td><td>0.12 (-3.02%)</td><td>0.12 (+16.87%)</td><td>0.07 (-6.72%)</td><td>0.05 (-8.77%)</td><td>700.10 (+7.20%)</td><td>450.50 (+2.16%)</td><td>425.90 (-14.43%)</td><td>255.20 (+1.75%)</td><td>174.46 (+3.81%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>653.10 (n/a)</td><td>440.96 (n/a)</td><td>497.70 (n/a)</td><td>250.80 (n/a)</td><td>168.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.19 (-1.53%)</td><td>0.18 <b>(+65.26%)</b></td><td>0.18 <b>(+96.63%)</b></td><td>0.16 <b>(+211.82%)</b></td><td>0.01 <b>(-73.60%)</b></td><td>302.20 <b>(-67.93%)</b></td><td>274.78 <b>(-49.27%)</b></td><td>265.90 <b>(-49.14%)</b></td><td>254.20 (+1.56%)</td><td>22.20 <b>(-91.26%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>942.30 (n/a)</td><td>541.66 (n/a)</td><td>522.80 (n/a)</td><td>250.30 (n/a)</td><td>254.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.23 (+13.56%)</td><td>0.19 <b>(+37.58%)</b></td><td>0.20 <b>(+69.99%)</b></td><td>0.14 <b>(+40.06%)</b></td><td>0.04 (-10.82%)</td><td>354.10 <b>(-28.59%)</b></td><td>273.98 <b>(-29.50%)</b></td><td>249.20 <b>(-41.17%)</b></td><td>218.00 (-11.92%)</td><td>57.43 <b>(-43.03%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>495.90 (n/a)</td><td>388.62 (n/a)</td><td>423.60 (n/a)</td><td>247.50 (n/a)</td><td>100.81 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.29 <b>(+34.83%)</b></td><td>0.17 <b>(+34.21%)</b></td><td>0.16 <b>(+81.10%)</b></td><td>0.09 <b>(+25.08%)</b></td><td>0.07 (+18.61%)</td><td>518.70 <b>(-20.05%)</b></td><td>329.96 <b>(-28.30%)</b></td><td>299.10 <b>(-44.80%)</b></td><td>169.00 <b>(-25.84%)</b></td><td>127.46 <b>(-32.03%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>648.80 (n/a)</td><td>460.18 (n/a)</td><td>541.80 (n/a)</td><td>227.90 (n/a)</td><td>187.53 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (+13.76%)</td><td>0.01 (-6.15%)</td><td>0.01 (+2.87%)</td><td>0.00 <b>(-28.25%)</b></td><td>0.00 <b>(+119.83%)</b></td><td>552.10 <b>(+39.38%)</b></td><td>353.42 (+17.89%)</td><td>275.20 (-2.79%)</td><td>231.50 (-12.08%)</td><td>145.31 <b>(+163.19%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>396.10 (n/a)</td><td>299.78 (n/a)</td><td>283.10 (n/a)</td><td>263.30 (n/a)</td><td>55.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (+6.52%)</td><td>0.01 (-3.08%)</td><td>0.01 (+4.13%)</td><td>0.00 (-5.19%)</td><td>0.00 (-0.23%)</td><td>559.70 (+5.48%)</td><td>411.40 (+1.74%)</td><td>425.00 (-3.98%)</td><td>222.20 (-6.13%)</td><td>120.97 (-11.42%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>530.60 (n/a)</td><td>404.38 (n/a)</td><td>442.60 (n/a)</td><td>236.70 (n/a)</td><td>136.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (-14.73%)</td><td>0.01 (-12.04%)</td><td>0.00 <b>(-21.67%)</b></td><td>0.00 (+3.40%)</td><td>0.00 <b>(-26.45%)</b></td><td>619.40 (-3.29%)</td><td>501.82 (+8.75%)</td><td>548.90 <b>(+27.65%)</b></td><td>298.40 (+17.30%)</td><td>122.46 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>640.50 (n/a)</td><td>461.44 (n/a)</td><td>430.00 (n/a)</td><td>254.40 (n/a)</td><td>158.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (+5.45%)</td><td>0.01 (-7.42%)</td><td>0.01 (-9.04%)</td><td>0.00 (+15.10%)</td><td>0.00 (-13.38%)</td><td>709.10 (-13.12%)</td><td>462.98 (+1.57%)</td><td>481.60 (+9.95%)</td><td>245.00 (-5.15%)</td><td>171.02 <b>(-25.29%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>816.20 (n/a)</td><td>455.84 (n/a)</td><td>438.00 (n/a)</td><td>258.30 (n/a)</td><td>228.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 <b>(+25.21%)</b></td><td>0.01 (+1.34%)</td><td>0.01 (-14.64%)</td><td>0.00 (+0.96%)</td><td>0.00 <b>(+51.54%)</b></td><td>580.70 (-0.96%)</td><td>461.86 (+2.64%)</td><td>482.30 (+17.15%)</td><td>238.60 <b>(-20.12%)</b></td><td>134.59 (+9.40%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>586.30 (n/a)</td><td>450.00 (n/a)</td><td>411.70 (n/a)</td><td>298.70 (n/a)</td><td>123.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (-8.14%)</td><td>0.01 (+2.52%)</td><td>0.01 (-1.35%)</td><td>0.00 <b>(+122.98%)</b></td><td>0.00 <b>(-23.23%)</b></td><td>849.80 <b>(-55.15%)</b></td><td>517.08 <b>(-28.96%)</b></td><td>492.10 (+1.36%)</td><td>237.30 (+8.85%)</td><td>218.36 <b>(-67.28%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1894.90 (n/a)</td><td>727.84 (n/a)</td><td>485.50 (n/a)</td><td>218.00 (n/a)</td><td>667.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+4.38%)</td><td>0.01 (-13.02%)</td><td>0.01 <b>(-22.89%)</b></td><td>0.01 <b>(-22.45%)</b></td><td>0.01 (+7.52%)</td><td>680.00 <b>(+28.96%)</b></td><td>428.12 (+18.36%)</td><td>385.10 <b>(+29.71%)</b></td><td>229.90 (-4.21%)</td><td>169.15 <b>(+29.12%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>527.30 (n/a)</td><td>361.70 (n/a)</td><td>296.90 (n/a)</td><td>240.00 (n/a)</td><td>130.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-1.74%)</td><td>0.01 (+5.78%)</td><td>0.02 <b>(+38.22%)</b></td><td>0.01 (+1.66%)</td><td>0.01 (-0.27%)</td><td>642.30 (-1.64%)</td><td>409.30 (-4.66%)</td><td>333.70 <b>(-27.65%)</b></td><td>238.80 (+1.79%)</td><td>180.86 (+5.56%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.00 (n/a)</td><td>429.32 (n/a)</td><td>461.20 (n/a)</td><td>234.60 (n/a)</td><td>171.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-12.23%)</td><td>0.02 <b>(+20.56%)</b></td><td>0.02 (+9.75%)</td><td>0.02 <b>(+513.90%)</b></td><td>0.00 <b>(-80.04%)</b></td><td>294.50 <b>(-83.71%)</b></td><td>259.20 <b>(-54.63%)</b></td><td>253.50 (-8.88%)</td><td>239.70 (+13.93%)</td><td>22.28 <b>(-96.78%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1808.20 (n/a)</td><td>571.24 (n/a)</td><td>278.20 (n/a)</td><td>210.40 (n/a)</td><td>692.28 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+11.86%)</td><td>0.01 (+18.62%)</td><td>0.01 (+11.68%)</td><td>0.01 (-7.26%)</td><td>0.00 <b>(+36.74%)</b></td><td>653.80 (+7.83%)</td><td>418.36 (-11.77%)</td><td>420.10 (-10.46%)</td><td>263.90 (-10.60%)</td><td>155.48 <b>(+33.58%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.30 (n/a)</td><td>474.18 (n/a)</td><td>469.20 (n/a)</td><td>295.20 (n/a)</td><td>116.39 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+26.77%)</b></td><td>0.02 (+12.97%)</td><td>0.02 (+9.85%)</td><td>0.01 (+1.70%)</td><td>0.01 <b>(+33.04%)</b></td><td>553.50 (-1.67%)</td><td>367.06 (-8.61%)</td><td>289.70 (-8.96%)</td><td>224.60 <b>(-21.14%)</b></td><td>146.21 (+5.16%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.90 (n/a)</td><td>401.64 (n/a)</td><td>318.20 (n/a)</td><td>284.80 (n/a)</td><td>139.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-10.14%)</td><td>0.01 (+5.05%)</td><td>0.02 <b>(+56.18%)</b></td><td>0.01 (+13.59%)</td><td>0.00 <b>(-21.51%)</b></td><td>562.60 (-11.97%)</td><td>408.64 (-8.15%)</td><td>322.00 <b>(-35.97%)</b></td><td>313.70 (+11.32%)</td><td>124.59 (-18.90%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>639.10 (n/a)</td><td>444.90 (n/a)</td><td>502.90 (n/a)</td><td>281.80 (n/a)</td><td>153.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (-14.60%)</td><td>0.03 (+2.10%)</td><td>0.04 (+9.53%)</td><td>0.02 (+0.60%)</td><td>0.01 <b>(-29.99%)</b></td><td>491.50 (-0.59%)</td><td>322.74 (-7.39%)</td><td>278.20 (-8.70%)</td><td>242.60 (+17.08%)</td><td>103.29 <b>(-24.09%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.40 (n/a)</td><td>348.48 (n/a)</td><td>304.70 (n/a)</td><td>207.20 (n/a)</td><td>136.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 <b>(+27.00%)</b></td><td>0.04 <b>(+83.62%)</b></td><td>0.04 <b>(+147.89%)</b></td><td>0.03 <b>(+106.62%)</b></td><td>0.01 <b>(-26.91%)</b></td><td>364.60 <b>(-51.60%)</b></td><td>276.56 <b>(-49.74%)</b></td><td>250.70 <b>(-59.66%)</b></td><td>239.40 <b>(-21.28%)</b></td><td>51.43 <b>(-71.00%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>753.30 (n/a)</td><td>550.22 (n/a)</td><td>621.40 (n/a)</td><td>304.10 (n/a)</td><td>177.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (+1.45%)</td><td>0.04 <b>(+51.21%)</b></td><td>0.04 <b>(+114.40%)</b></td><td>0.02 <b>(+30.01%)</b></td><td>0.01 (-17.22%)</td><td>462.60 <b>(-23.08%)</b></td><td>297.88 <b>(-37.04%)</b></td><td>244.20 <b>(-53.36%)</b></td><td>228.00 (-1.43%)</td><td>97.44 <b>(-31.96%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.40 (n/a)</td><td>473.14 (n/a)</td><td>523.60 (n/a)</td><td>231.30 (n/a)</td><td>143.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 <b>(+29.94%)</b></td><td>0.03 <b>(+23.37%)</b></td><td>0.03 <b>(+46.12%)</b></td><td>0.02 (-3.73%)</td><td>0.01 <b>(+57.87%)</b></td><td>597.40 (+3.88%)</td><td>391.38 (-12.81%)</td><td>361.20 <b>(-31.56%)</b></td><td>220.60 <b>(-23.03%)</b></td><td>168.42 <b>(+26.19%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.10 (n/a)</td><td>448.90 (n/a)</td><td>527.80 (n/a)</td><td>286.60 (n/a)</td><td>133.46 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 <b>(+34.47%)</b></td><td>0.03 <b>(+42.92%)</b></td><td>0.03 <b>(+47.90%)</b></td><td>0.02 (+15.41%)</td><td>0.01 <b>(+73.65%)</b></td><td>540.30 (-13.36%)</td><td>369.22 <b>(-26.74%)</b></td><td>351.10 <b>(-32.38%)</b></td><td>242.00 <b>(-25.65%)</b></td><td>133.27 (+4.34%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>623.60 (n/a)</td><td>503.96 (n/a)</td><td>519.20 (n/a)</td><td>325.50 (n/a)</td><td>127.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (+10.63%)</td><td>0.02 (-1.41%)</td><td>0.02 (-16.86%)</td><td>0.02 (-12.27%)</td><td>0.01 <b>(+40.69%)</b></td><td>656.00 (+13.99%)</td><td>492.24 (+4.27%)</td><td>523.00 <b>(+20.29%)</b></td><td>343.60 (-9.60%)</td><td>129.63 <b>(+37.04%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>575.50 (n/a)</td><td>472.10 (n/a)</td><td>434.80 (n/a)</td><td>380.10 (n/a)</td><td>94.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (-5.10%)</td><td>0.07 (+14.99%)</td><td>0.08 (+10.29%)</td><td>0.05 <b>(+58.26%)</b></td><td>0.01 <b>(-42.51%)</b></td><td>447.50 <b>(-36.80%)</b></td><td>306.32 <b>(-23.50%)</b></td><td>271.50 (-9.32%)</td><td>248.30 (+5.39%)</td><td>80.60 <b>(-59.77%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>708.10 (n/a)</td><td>400.42 (n/a)</td><td>299.40 (n/a)</td><td>235.60 (n/a)</td><td>200.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 <b>(+22.12%)</b></td><td>0.06 (+10.17%)</td><td>0.05 (+14.98%)</td><td>0.04 (-3.19%)</td><td>0.02 <b>(+34.75%)</b></td><td>546.10 (+3.29%)</td><td>402.92 (-7.11%)</td><td>431.20 (-13.03%)</td><td>232.20 (-18.12%)</td><td>116.06 (+6.81%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>528.70 (n/a)</td><td>433.78 (n/a)</td><td>495.80 (n/a)</td><td>283.60 (n/a)</td><td>108.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 <b>(-20.30%)</b></td><td>0.06 (+4.72%)</td><td>0.07 <b>(+54.15%)</b></td><td>0.04 (+15.52%)</td><td>0.02 <b>(-28.93%)</b></td><td>588.40 (-13.43%)</td><td>370.28 (-11.81%)</td><td>291.50 <b>(-35.14%)</b></td><td>241.60 <b>(+25.44%)</b></td><td>152.60 <b>(-21.36%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>679.70 (n/a)</td><td>419.86 (n/a)</td><td>449.40 (n/a)</td><td>192.60 (n/a)</td><td>194.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 <b>(+79.18%)</b></td><td>0.06 <b>(+60.07%)</b></td><td>0.05 (+19.99%)</td><td>0.04 <b>(+91.47%)</b></td><td>0.02 <b>(+115.47%)</b></td><td>541.90 <b>(-47.77%)</b></td><td>383.60 <b>(-36.23%)</b></td><td>425.00 (-16.67%)</td><td>234.70 <b>(-44.19%)</b></td><td>139.34 <b>(-44.30%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1037.60 (n/a)</td><td>601.58 (n/a)</td><td>510.00 (n/a)</td><td>420.50 (n/a)</td><td>250.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (-16.51%)</td><td>0.05 (-11.79%)</td><td>0.04 (-16.58%)</td><td>0.04 (+10.17%)</td><td>0.01 <b>(-44.94%)</b></td><td>547.30 (-9.24%)</td><td>442.58 (+4.39%)</td><td>472.50 (+19.86%)</td><td>309.50 (+19.78%)</td><td>94.52 <b>(-42.14%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.00 (n/a)</td><td>423.96 (n/a)</td><td>394.20 (n/a)</td><td>258.40 (n/a)</td><td>163.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (-14.51%)</td><td>0.05 (-14.12%)</td><td>0.05 (+8.05%)</td><td>0.04 (-4.41%)</td><td>0.02 <b>(-31.90%)</b></td><td>515.80 (+4.62%)</td><td>425.68 (+10.04%)</td><td>443.90 (-7.44%)</td><td>253.70 (+16.97%)</td><td>103.15 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>493.00 (n/a)</td><td>386.84 (n/a)</td><td>479.60 (n/a)</td><td>216.90 (n/a)</td><td>134.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2032.40 (n/a)</td><td>878.94 (n/a)</td><td>529.00 (n/a)</td><td>308.80 (n/a)</td><td>708.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.00 (n/a)</td><td>424.82 (n/a)</td><td>540.60 (n/a)</td><td>227.10 (n/a)</td><td>170.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>766.80 (n/a)</td><td>444.42 (n/a)</td><td>442.00 (n/a)</td><td>257.50 (n/a)</td><td>206.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>624.40 (n/a)</td><td>523.68 (n/a)</td><td>519.00 (n/a)</td><td>418.00 (n/a)</td><td>75.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>526.60 (n/a)</td><td>386.90 (n/a)</td><td>469.60 (n/a)</td><td>191.00 (n/a)</td><td>155.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>654.80 (n/a)</td><td>515.92 (n/a)</td><td>528.60 (n/a)</td><td>416.90 (n/a)</td><td>95.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.70 (n/a)</td><td>365.88 (n/a)</td><td>303.10 (n/a)</td><td>273.40 (n/a)</td><td>113.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>493.40 (n/a)</td><td>330.02 (n/a)</td><td>249.70 (n/a)</td><td>196.90 (n/a)</td><td>141.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.40 (n/a)</td><td>429.36 (n/a)</td><td>469.60 (n/a)</td><td>277.40 (n/a)</td><td>104.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.22 <b>(+22.45%)</b></td><td>0.14 (-14.89%)</td><td>0.11 <b>(-32.44%)</b></td><td>0.08 <b>(-32.42%)</b></td><td>0.05 <b>(+133.09%)</b></td><td>615.20 <b>(+47.96%)</b></td><td>409.94 <b>(+29.71%)</b></td><td>440.40 <b>(+48.03%)</b></td><td>226.20 (-18.34%)</td><td>150.45 <b>(+166.19%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>415.80 (n/a)</td><td>316.04 (n/a)</td><td>297.50 (n/a)</td><td>277.00 (n/a)</td><td>56.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1866.30 (n/a)</td><td>729.20 (n/a)</td><td>524.80 (n/a)</td><td>196.80 (n/a)</td><td>652.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>542.70 (n/a)</td><td>377.82 (n/a)</td><td>331.90 (n/a)</td><td>274.30 (n/a)</td><td>105.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>468.80 (n/a)</td><td>344.74 (n/a)</td><td>326.70 (n/a)</td><td>163.40 (n/a)</td><td>126.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.20 (n/a)</td><td>418.00 (n/a)</td><td>483.50 (n/a)</td><td>161.50 (n/a)</td><td>162.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.00 (n/a)</td><td>385.16 (n/a)</td><td>343.90 (n/a)</td><td>270.00 (n/a)</td><td>117.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1154.20 (n/a)</td><td>561.96 (n/a)</td><td>462.90 (n/a)</td><td>237.50 (n/a)</td><td>347.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.60 (n/a)</td><td>319.26 (n/a)</td><td>259.20 (n/a)</td><td>223.60 (n/a)</td><td>129.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>973.10 (n/a)</td><td>497.62 (n/a)</td><td>459.80 (n/a)</td><td>260.80 (n/a)</td><td>283.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2089.60 (n/a)</td><td>794.60 (n/a)</td><td>522.30 (n/a)</td><td>368.80 (n/a)</td><td>731.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>539.00 (n/a)</td><td>445.96 (n/a)</td><td>523.80 (n/a)</td><td>250.20 (n/a)</td><td>125.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>539.40 (n/a)</td><td>365.22 (n/a)</td><td>350.50 (n/a)</td><td>187.50 (n/a)</td><td>133.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>585.30 (n/a)</td><td>490.76 (n/a)</td><td>536.10 (n/a)</td><td>337.00 (n/a)</td><td>98.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>675.80 (n/a)</td><td>504.58 (n/a)</td><td>548.80 (n/a)</td><td>247.20 (n/a)</td><td>168.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>672.30 (n/a)</td><td>398.78 (n/a)</td><td>382.10 (n/a)</td><td>235.40 (n/a)</td><td>178.37 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.60 (n/a)</td><td>322.02 (n/a)</td><td>269.70 (n/a)</td><td>228.80 (n/a)</td><td>117.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1124.00 (n/a)</td><td>497.74 (n/a)</td><td>263.70 (n/a)</td><td>222.30 (n/a)</td><td>393.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>647.50 (n/a)</td><td>434.84 (n/a)</td><td>421.90 (n/a)</td><td>222.70 (n/a)</td><td>186.53 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.40 (n/a)</td><td>451.28 (n/a)</td><td>572.70 (n/a)</td><td>226.60 (n/a)</td><td>178.50 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1971.70 (n/a)</td><td>786.20 (n/a)</td><td>534.60 (n/a)</td><td>300.80 (n/a)</td><td>673.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1924.40 (n/a)</td><td>590.96 (n/a)</td><td>273.00 (n/a)</td><td>235.60 (n/a)</td><td>745.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.50 (n/a)</td><td>368.50 (n/a)</td><td>240.20 (n/a)</td><td>224.00 (n/a)</td><td>185.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1904.50 (n/a)</td><td>633.38 (n/a)</td><td>313.70 (n/a)</td><td>213.40 (n/a)</td><td>717.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.20 (n/a)</td><td>408.02 (n/a)</td><td>450.00 (n/a)</td><td>234.70 (n/a)</td><td>161.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1995.30 (n/a)</td><td>654.94 (n/a)</td><td>292.40 (n/a)</td><td>194.30 (n/a)</td><td>762.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.70 (n/a)</td><td>381.06 (n/a)</td><td>419.70 (n/a)</td><td>228.10 (n/a)</td><td>117.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>452.20 (n/a)</td><td>312.40 (n/a)</td><td>309.30 (n/a)</td><td>231.10 (n/a)</td><td>86.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.80 (n/a)</td><td>337.70 (n/a)</td><td>275.80 (n/a)</td><td>206.20 (n/a)</td><td>149.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>990.50 (n/a)</td><td>514.04 (n/a)</td><td>420.30 (n/a)</td><td>303.70 (n/a)</td><td>271.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>740.00 (n/a)</td><td>409.64 (n/a)</td><td>437.60 (n/a)</td><td>191.00 (n/a)</td><td>216.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>630.20 (n/a)</td><td>428.74 (n/a)</td><td>453.10 (n/a)</td><td>239.30 (n/a)</td><td>161.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>660.60 (n/a)</td><td>542.56 (n/a)</td><td>568.70 (n/a)</td><td>352.80 (n/a)</td><td>113.81 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>602.90 (n/a)</td><td>382.80 (n/a)</td><td>304.10 (n/a)</td><td>295.00 (n/a)</td><td>132.53 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1077.80 (n/a)</td><td>543.10 (n/a)</td><td>448.70 (n/a)</td><td>261.60 (n/a)</td><td>312.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>776.80 (n/a)</td><td>401.72 (n/a)</td><td>315.50 (n/a)</td><td>205.50 (n/a)</td><td>229.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>511.60 (n/a)</td><td>396.50 (n/a)</td><td>437.70 (n/a)</td><td>244.10 (n/a)</td><td>123.37 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>584.20 (n/a)</td><td>332.46 (n/a)</td><td>290.80 (n/a)</td><td>236.50 (n/a)</td><td>143.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1893.40 (n/a)</td><td>730.60 (n/a)</td><td>498.80 (n/a)</td><td>341.60 (n/a)</td><td>655.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.66 (+3.73%)</td><td>0.39 <b>(+27.68%)</b></td><td>0.37 <b>(+23.33%)</b></td><td>0.13 (+7.33%)</td><td>0.19 (-9.22%)</td><td>1661.90 (-6.83%)</td><td>747.72 <b>(-28.70%)</b></td><td>594.40 (-18.92%)</td><td>335.80 (-3.59%)</td><td>524.36 <b>(-20.36%)</b></td><td>28.11 (+3.73%)</td><td>16.62 <b>(+27.68%)</b></td><td>15.88 <b>(+23.33%)</b></td><td>5.68 (+7.33%)</td><td>8.07 (-9.22%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.64 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.12 (n/a)</td><td>0.21 (n/a)</td><td>1783.80 (n/a)</td><td>1048.76 (n/a)</td><td>733.10 (n/a)</td><td>348.30 (n/a)</td><td>658.45 (n/a)</td><td>27.10 (n/a)</td><td>13.02 (n/a)</td><td>12.87 (n/a)</td><td>5.29 (n/a)</td><td>8.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.42 (-10.75%)</td><td>0.29 <b>(-26.11%)</b></td><td>0.32 (-16.39%)</td><td>0.13 <b>(-60.57%)</b></td><td>0.12 <b>(+89.50%)</b></td><td>1712.50 <b>(+153.63%)</b></td><td>909.78 <b>(+58.20%)</b></td><td>681.80 (+19.59%)</td><td>522.60 (+12.05%)</td><td>482.74 <b>(+451.70%)</b></td><td>18.06 (-10.75%)</td><td>12.36 <b>(-26.11%)</b></td><td>13.84 (-16.39%)</td><td>5.51 <b>(-60.57%)</b></td><td>4.92 <b>(+89.50%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>675.20 (n/a)</td><td>575.08 (n/a)</td><td>570.10 (n/a)</td><td>466.40 (n/a)</td><td>87.50 (n/a)</td><td>20.23 (n/a)</td><td>16.72 (n/a)</td><td>16.55 (n/a)</td><td>13.98 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.31 (+1.29%)</td><td>0.31 (+1.37%)</td><td>0.31 (+1.72%)</td><td>0.30 (+0.57%)</td><td>0.00 <b>(+25.27%)</b></td><td>83916.10 (-0.57%)</td><td>82434.36 (-1.34%)</td><td>82095.40 (-1.69%)</td><td>81552.50 (-1.27%)</td><td>896.44 <b>(+23.17%)</b></td><td>210.66 (+1.29%)</td><td>208.43 (+1.37%)</td><td>209.27 (+1.72%)</td><td>204.73 (+0.57%)</td><td>2.25 <b>(+25.27%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84396.70 (n/a)</td><td>83557.40 (n/a)</td><td>83505.60 (n/a)</td><td>82602.20 (n/a)</td><td>727.84 (n/a)</td><td>207.98 (n/a)</td><td>205.62 (n/a)</td><td>205.73 (n/a)</td><td>203.56 (n/a)</td><td>1.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>1.01 (-2.35%)</td><td>0.98 (-2.13%)</td><td>0.99 (-1.53%)</td><td>0.93 (-4.16%)</td><td>0.03 (+14.65%)</td><td>26983.40 (+4.34%)</td><td>25682.72 (+2.20%)</td><td>25417.90 (+1.56%)</td><td>24968.20 (+2.41%)</td><td>849.47 <b>(+21.86%)</b></td><td>688.07 (-2.35%)</td><td>669.50 (-2.13%)</td><td>675.90 (-1.53%)</td><td>636.68 (-4.16%)</td><td>21.71 (+14.65%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.03 (n/a)</td><td>25861.10 (n/a)</td><td>25129.42 (n/a)</td><td>25028.70 (n/a)</td><td>24381.20 (n/a)</td><td>697.11 (n/a)</td><td>704.64 (n/a)</td><td>684.08 (n/a)</td><td>686.41 (n/a)</td><td>664.31 (n/a)</td><td>18.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.82 (+0.94%)</td><td>0.81 (+0.65%)</td><td>0.82 (+1.44%)</td><td>0.79 (-0.50%)</td><td>0.01 <b>(+45.93%)</b></td><td>95642.00 (+0.50%)</td><td>93123.30 (-0.63%)</td><td>92451.70 (-1.42%)</td><td>91694.50 (-0.93%)</td><td>1676.92 <b>(+45.46%)</b></td><td>749.44 (+0.94%)</td><td>738.13 (+0.65%)</td><td>743.30 (+1.44%)</td><td>718.51 (-0.50%)</td><td>13.15 <b>(+45.93%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95164.70 (n/a)</td><td>93716.06 (n/a)</td><td>93785.20 (n/a)</td><td>92559.40 (n/a)</td><td>1152.82 (n/a)</td><td>742.44 (n/a)</td><td>733.36 (n/a)</td><td>732.73 (n/a)</td><td>722.11 (n/a)</td><td>9.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.77 (+0.22%)</td><td>0.76 (-0.22%)</td><td>0.76 (-0.26%)</td><td>0.74 (-1.08%)</td><td>0.01 <b>(+50.92%)</b></td><td>102114.60 (+1.09%)</td><td>99857.68 (+0.23%)</td><td>99803.10 (+0.26%)</td><td>98007.00 (-0.22%)</td><td>1586.92 <b>(+52.25%)</b></td><td>701.17 (+0.22%)</td><td>688.31 (-0.22%)</td><td>688.55 (-0.26%)</td><td>672.96 (-1.08%)</td><td>10.89 <b>(+50.92%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101015.50 (n/a)</td><td>99626.98 (n/a)</td><td>99545.80 (n/a)</td><td>98224.70 (n/a)</td><td>1042.29 (n/a)</td><td>699.62 (n/a)</td><td>689.83 (n/a)</td><td>690.33 (n/a)</td><td>680.29 (n/a)</td><td>7.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.80 (-0.34%)</td><td>0.79 (-0.82%)</td><td>0.79 (-0.81%)</td><td>0.79 (-1.29%)</td><td>0.00 <b>(+240.93%)</b></td><td>95917.40 (+1.31%)</td><td>95227.28 (+0.83%)</td><td>95117.60 (+0.82%)</td><td>94648.50 (+0.34%)</td><td>554.40 <b>(+246.65%)</b></td><td>726.05 (-0.34%)</td><td>721.66 (-0.82%)</td><td>722.47 (-0.81%)</td><td>716.44 (-1.29%)</td><td>4.20 <b>(+240.92%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94677.50 (n/a)</td><td>94447.16 (n/a)</td><td>94343.10 (n/a)</td><td>94327.70 (n/a)</td><td>159.93 (n/a)</td><td>728.52 (n/a)</td><td>727.60 (n/a)</td><td>728.40 (n/a)</td><td>725.83 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.67 (+3.95%)</td><td>3.88 (-13.77%)</td><td>4.01 (-1.90%)</td><td>2.11 <b>(-41.58%)</b></td><td>1.29 <b>(+57.47%)</b></td><td>4221.30 <b>(+71.17%)</b></td><td>2549.76 <b>(+25.36%)</b></td><td>2221.60 (+1.93%)</td><td>1570.70 (-3.80%)</td><td>1002.21 <b>(+179.58%)</b></td><td>341.81 (+3.95%)</td><td>233.58 (-13.77%)</td><td>241.66 (-1.90%)</td><td>127.18 <b>(-41.58%)</b></td><td>77.46 <b>(+57.47%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>5.46 (n/a)</td><td>4.50 (n/a)</td><td>4.09 (n/a)</td><td>3.61 (n/a)</td><td>0.82 (n/a)</td><td>2466.20 (n/a)</td><td>2033.94 (n/a)</td><td>2179.50 (n/a)</td><td>1632.80 (n/a)</td><td>358.47 (n/a)</td><td>328.81 (n/a)</td><td>270.86 (n/a)</td><td>246.33 (n/a)</td><td>217.69 (n/a)</td><td>49.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>4.58 (+6.52%)</td><td>2.88 (-11.11%)</td><td>2.45 (-11.92%)</td><td>2.29 (+6.20%)</td><td>0.97 (+2.61%)</td><td>3886.10 (-5.84%)</td><td>3312.28 (+12.29%)</td><td>3637.00 (+13.53%)</td><td>1946.20 (-6.12%)</td><td>807.07 (-5.89%)</td><td>275.86 (+6.52%)</td><td>173.36 (-11.11%)</td><td>147.61 (-11.92%)</td><td>138.15 (+6.20%)</td><td>58.38 (+2.61%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>4.30 (n/a)</td><td>3.24 (n/a)</td><td>2.78 (n/a)</td><td>2.16 (n/a)</td><td>0.94 (n/a)</td><td>4127.10 (n/a)</td><td>2949.76 (n/a)</td><td>3203.60 (n/a)</td><td>2073.00 (n/a)</td><td>857.57 (n/a)</td><td>258.99 (n/a)</td><td>195.02 (n/a)</td><td>167.59 (n/a)</td><td>130.08 (n/a)</td><td>56.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.82 <b>(+47.12%)</b></td><td>5.01 <b>(+57.32%)</b></td><td>5.21 <b>(+80.09%)</b></td><td>4.12 <b>(+68.46%)</b></td><td>0.74 (+9.44%)</td><td>2164.90 <b>(-40.64%)</b></td><td>1810.74 <b>(-37.52%)</b></td><td>1710.00 <b>(-44.47%)</b></td><td>1530.80 <b>(-32.03%)</b></td><td>275.92 <b>(-53.84%)</b></td><td>350.71 <b>(+47.12%)</b></td><td>301.88 <b>(+57.32%)</b></td><td>313.96 <b>(+80.09%)</b></td><td>247.99 <b>(+68.46%)</b></td><td>44.36 (+9.44%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.96 (n/a)</td><td>3.19 (n/a)</td><td>2.89 (n/a)</td><td>2.44 (n/a)</td><td>0.67 (n/a)</td><td>3647.10 (n/a)</td><td>2898.22 (n/a)</td><td>3079.50 (n/a)</td><td>2252.10 (n/a)</td><td>597.72 (n/a)</td><td>238.39 (n/a)</td><td>191.89 (n/a)</td><td>174.34 (n/a)</td><td>147.21 (n/a)</td><td>40.54 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.35 (+9.68%)</td><td>5.54 (+4.98%)</td><td>5.34 (-2.50%)</td><td>4.38 (-2.12%)</td><td>0.82 <b>(+42.73%)</b></td><td>7957.50 (+2.16%)</td><td>6416.20 (-3.92%)</td><td>6528.40 (+2.56%)</td><td>5491.20 (-8.82%)</td><td>1008.56 <b>(+31.50%)</b></td><td>391.08 (+9.68%)</td><td>341.01 (+4.98%)</td><td>328.95 (-2.50%)</td><td>269.87 (-2.12%)</td><td>50.54 <b>(+42.73%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>5.79 (n/a)</td><td>5.27 (n/a)</td><td>5.48 (n/a)</td><td>4.48 (n/a)</td><td>0.57 (n/a)</td><td>7789.10 (n/a)</td><td>6678.08 (n/a)</td><td>6365.40 (n/a)</td><td>6022.70 (n/a)</td><td>766.96 (n/a)</td><td>356.56 (n/a)</td><td>324.82 (n/a)</td><td>337.37 (n/a)</td><td>275.70 (n/a)</td><td>35.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.62 (-7.76%)</td><td>5.27 (+1.30%)</td><td>5.37 (+0.32%)</td><td>4.59 (+4.61%)</td><td>0.41 <b>(-43.37%)</b></td><td>7600.50 (-4.41%)</td><td>6654.34 (-2.32%)</td><td>6498.40 (-0.32%)</td><td>6204.70 (+8.42%)</td><td>559.32 <b>(-41.74%)</b></td><td>346.10 (-7.76%)</td><td>324.41 (+1.30%)</td><td>330.46 (+0.32%)</td><td>282.54 (+4.61%)</td><td>25.23 <b>(-43.37%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.09 (n/a)</td><td>5.20 (n/a)</td><td>5.35 (n/a)</td><td>4.39 (n/a)</td><td>0.72 (n/a)</td><td>7951.00 (n/a)</td><td>6812.46 (n/a)</td><td>6519.40 (n/a)</td><td>5723.00 (n/a)</td><td>960.09 (n/a)</td><td>375.23 (n/a)</td><td>320.24 (n/a)</td><td>329.40 (n/a)</td><td>270.09 (n/a)</td><td>44.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.52 (-3.07%)</td><td>6.00 (+9.83%)</td><td>6.13 (+12.61%)</td><td>5.10 (+12.29%)</td><td>0.56 <b>(-33.67%)</b></td><td>6841.40 (-10.94%)</td><td>5859.40 (-9.91%)</td><td>5687.90 (-11.20%)</td><td>5346.30 (+3.17%)</td><td>591.19 <b>(-38.21%)</b></td><td>401.67 (-3.07%)</td><td>369.27 (+9.83%)</td><td>377.55 (+12.61%)</td><td>313.90 (+12.29%)</td><td>34.33 <b>(-33.67%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.73 (n/a)</td><td>5.46 (n/a)</td><td>5.44 (n/a)</td><td>4.54 (n/a)</td><td>0.84 (n/a)</td><td>7682.00 (n/a)</td><td>6504.12 (n/a)</td><td>6405.00 (n/a)</td><td>5182.20 (n/a)</td><td>956.73 (n/a)</td><td>414.40 (n/a)</td><td>336.21 (n/a)</td><td>335.28 (n/a)</td><td>279.55 (n/a)</td><td>51.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.79 (+1.75%)</td><td>0.77 (+0.57%)</td><td>0.78 (+2.02%)</td><td>0.74 (-2.87%)</td><td>0.02 <b>(+292.23%)</b></td><td>102323.40 (+2.95%)</td><td>98233.36 (-0.52%)</td><td>96928.40 (-1.98%)</td><td>95992.50 (-1.72%)</td><td>2551.21 <b>(+298.26%)</b></td><td>715.88 (+1.75%)</td><td>699.92 (+0.57%)</td><td>708.97 (+2.02%)</td><td>671.59 (-2.87%)</td><td>17.82 <b>(+292.23%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.00 (n/a)</td><td>99388.00 (n/a)</td><td>98749.26 (n/a)</td><td>98887.30 (n/a)</td><td>97668.70 (n/a)</td><td>640.58 (n/a)</td><td>703.60 (n/a)</td><td>695.92 (n/a)</td><td>694.93 (n/a)</td><td>691.43 (n/a)</td><td>4.54 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.78 (+1.42%)</td><td>0.77 (+1.76%)</td><td>0.76 (+0.65%)</td><td>0.76 (+3.98%)</td><td>0.01 <b>(-44.47%)</b></td><td>99648.90 (-3.83%)</td><td>98390.80 (-1.76%)</td><td>98824.50 (-0.65%)</td><td>96634.60 (-1.40%)</td><td>1172.53 <b>(-47.46%)</b></td><td>711.13 (+1.42%)</td><td>698.51 (+1.76%)</td><td>695.37 (+0.65%)</td><td>689.62 (+3.98%)</td><td>8.38 <b>(-44.47%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103614.10 (n/a)</td><td>100152.54 (n/a)</td><td>99467.40 (n/a)</td><td>98002.80 (n/a)</td><td>2231.67 (n/a)</td><td>701.20 (n/a)</td><td>686.42 (n/a)</td><td>690.87 (n/a)</td><td>663.23 (n/a)</td><td>15.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.81 (+0.18%)</td><td>0.80 (-0.32%)</td><td>0.80 (-0.85%)</td><td>0.79 (+0.05%)</td><td>0.01 (+5.61%)</td><td>95857.90 (-0.05%)</td><td>94477.70 (+0.32%)</td><td>94722.20 (+0.86%)</td><td>93031.70 (-0.18%)</td><td>1068.01 (+5.03%)</td><td>738.67 (+0.18%)</td><td>727.44 (-0.32%)</td><td>725.48 (-0.85%)</td><td>716.89 (+0.05%)</td><td>8.23 (+5.61%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95905.80 (n/a)</td><td>94177.64 (n/a)</td><td>93914.60 (n/a)</td><td>93200.60 (n/a)</td><td>1016.90 (n/a)</td><td>737.33 (n/a)</td><td>729.75 (n/a)</td><td>731.72 (n/a)</td><td>716.53 (n/a)</td><td>7.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.51 (-8.10%)</td><td>2.41 (-13.07%)</td><td>2.18 (-11.06%)</td><td>1.75 (-4.28%)</td><td>0.66 (-18.62%)</td><td>4615.60 (+4.47%)</td><td>3524.66 (+13.00%)</td><td>3694.80 (+12.44%)</td><td>2297.40 (+8.82%)</td><td>840.50 (-8.61%)</td><td>920.14 (-8.10%)</td><td>632.10 (-13.07%)</td><td>572.14 (-11.06%)</td><td>458.00 (-4.28%)</td><td>174.14 (-18.62%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.82 (n/a)</td><td>2.77 (n/a)</td><td>2.45 (n/a)</td><td>1.82 (n/a)</td><td>0.82 (n/a)</td><td>4418.10 (n/a)</td><td>3119.04 (n/a)</td><td>3286.10 (n/a)</td><td>2111.20 (n/a)</td><td>919.66 (n/a)</td><td>1001.28 (n/a)</td><td>727.11 (n/a)</td><td>643.28 (n/a)</td><td>478.47 (n/a)</td><td>213.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.20 (-5.16%)</td><td>0.18 (-9.87%)</td><td>0.19 (-8.01%)</td><td>0.16 (-17.25%)</td><td>0.02 <b>(+94.05%)</b></td><td>7777.10 <b>(+20.84%)</b></td><td>6827.42 (+11.62%)</td><td>6537.80 (+8.71%)</td><td>6089.70 (+5.44%)</td><td>673.15 <b>(+147.57%)</b></td><td>11.02 (-5.16%)</td><td>9.90 (-9.87%)</td><td>10.26 (-8.01%)</td><td>8.63 (-17.25%)</td><td>0.95 <b>(+94.05%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>6435.70 (n/a)</td><td>6116.78 (n/a)</td><td>6013.80 (n/a)</td><td>5775.30 (n/a)</td><td>271.91 (n/a)</td><td>11.62 (n/a)</td><td>10.99 (n/a)</td><td>11.16 (n/a)</td><td>10.43 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.83 (n/a)</td><td>3.52 (n/a)</td><td>3.47 (n/a)</td><td>3.20 (n/a)</td><td>0.26 (n/a)</td><td>3.82 (n/a)</td><td>3.52 (n/a)</td><td>3.47 (n/a)</td><td>3.20 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.86 (-0.92%)</td><td>6.24 (-3.72%)</td><td>6.36 (-3.49%)</td><td>5.69 (-1.09%)</td><td>0.48 (+1.79%)</td><td>6.85 (-0.92%)</td><td>6.24 (-3.72%)</td><td>6.36 (-3.49%)</td><td>5.68 (-1.09%)</td><td>0.48 (+1.79%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.92 (n/a)</td><td>6.49 (n/a)</td><td>6.59 (n/a)</td><td>5.75 (n/a)</td><td>0.47 (n/a)</td><td>6.92 (n/a)</td><td>6.48 (n/a)</td><td>6.59 (n/a)</td><td>5.75 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>9.79 (-10.16%)</td><td>8.90 (+2.87%)</td><td>8.55 (+3.03%)</td><td>8.09 (+7.13%)</td><td>0.83 <b>(-36.81%)</b></td><td>9.78 (-10.16%)</td><td>8.89 (+2.87%)</td><td>8.54 (+3.03%)</td><td>8.08 (+7.13%)</td><td>0.82 <b>(-36.81%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>10.90 (n/a)</td><td>8.65 (n/a)</td><td>8.29 (n/a)</td><td>7.55 (n/a)</td><td>1.31 (n/a)</td><td>10.89 (n/a)</td><td>8.65 (n/a)</td><td>8.29 (n/a)</td><td>7.55 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.83 (n/a)</td><td>3.52 (n/a)</td><td>3.42 (n/a)</td><td>3.24 (n/a)</td><td>0.25 (n/a)</td><td>3.83 (n/a)</td><td>3.52 (n/a)</td><td>3.41 (n/a)</td><td>3.24 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.27 (-9.27%)</td><td>5.62 (-13.49%)</td><td>5.75 (-13.85%)</td><td>4.77 (-15.51%)</td><td>0.55 (+10.90%)</td><td>6.27 (-9.27%)</td><td>5.61 (-13.49%)</td><td>5.75 (-13.85%)</td><td>4.77 (-15.51%)</td><td>0.55 (+10.90%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>6.92 (n/a)</td><td>6.49 (n/a)</td><td>6.67 (n/a)</td><td>5.64 (n/a)</td><td>0.50 (n/a)</td><td>6.91 (n/a)</td><td>6.49 (n/a)</td><td>6.67 (n/a)</td><td>5.64 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>10.82 (-6.67%)</td><td>9.15 (-0.50%)</td><td>8.87 (+3.51%)</td><td>7.70 (-3.06%)</td><td>1.21 <b>(-21.28%)</b></td><td>10.82 (-6.67%)</td><td>9.15 (-0.50%)</td><td>8.86 (+3.51%)</td><td>7.69 (-3.06%)</td><td>1.21 <b>(-21.28%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>11.60 (n/a)</td><td>9.20 (n/a)</td><td>8.57 (n/a)</td><td>7.94 (n/a)</td><td>1.53 (n/a)</td><td>11.59 (n/a)</td><td>9.20 (n/a)</td><td>8.56 (n/a)</td><td>7.94 (n/a)</td><td>1.53 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.93 (-1.09%)</td><td>2.12 (-9.38%)</td><td>2.70 (-0.53%)</td><td>1.02 (-13.06%)</td><td>1.00 <b>(+37.51%)</b></td><td>2.92 (-1.09%)</td><td>2.12 (-9.38%)</td><td>2.69 (-0.53%)</td><td>1.02 (-13.06%)</td><td>1.00 <b>(+37.51%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.96 (n/a)</td><td>2.34 (n/a)</td><td>2.71 (n/a)</td><td>1.18 (n/a)</td><td>0.73 (n/a)</td><td>2.96 (n/a)</td><td>2.34 (n/a)</td><td>2.71 (n/a)</td><td>1.17 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.55 (-2.08%)</td><td>0.40 <b>(+22.39%)</b></td><td>0.51 <b>(+62.40%)</b></td><td>0.08 (+2.35%)</td><td>0.20 (+12.69%)</td><td>0.54 (-2.08%)</td><td>0.39 <b>(+22.39%)</b></td><td>0.50 <b>(+62.40%)</b></td><td>0.08 (+2.35%)</td><td>0.19 (+12.69%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.56 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>0.18 (n/a)</td><td>0.55 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.73 (-10.01%)</td><td>0.49 <b>(+50.94%)</b></td><td>0.65 <b>(+122.29%)</b></td><td>0.08 (+2.88%)</td><td>0.29 (-3.81%)</td><td>0.72 (-10.01%)</td><td>0.48 <b>(+50.94%)</b></td><td>0.65 <b>(+122.29%)</b></td><td>0.08 (+2.88%)</td><td>0.28 (-3.81%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.81 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>0.30 (n/a)</td><td>0.80 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.50 <b>(+22.86%)</b></td><td>1.55 (+5.85%)</td><td>1.90 <b>(+20.48%)</b></td><td>0.45 (+7.69%)</td><td>1.02 <b>(+57.22%)</b></td><td>2.46 <b>(+22.86%)</b></td><td>1.52 (+5.85%)</td><td>1.87 <b>(+20.48%)</b></td><td>0.45 (+7.69%)</td><td>1.00 <b>(+57.22%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.04 (n/a)</td><td>1.46 (n/a)</td><td>1.58 (n/a)</td><td>0.42 (n/a)</td><td>0.65 (n/a)</td><td>2.00 (n/a)</td><td>1.44 (n/a)</td><td>1.55 (n/a)</td><td>0.41 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.30 (n/a)</td><td>378.64 (n/a)</td><td>263.00 (n/a)</td><td>262.50 (n/a)</td><td>159.37 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.10 (n/a)</td><td>428.32 (n/a)</td><td>469.00 (n/a)</td><td>238.50 (n/a)</td><td>168.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.60 (n/a)</td><td>389.94 (n/a)</td><td>372.50 (n/a)</td><td>288.50 (n/a)</td><td>87.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.60 (n/a)</td><td>385.56 (n/a)</td><td>336.10 (n/a)</td><td>283.20 (n/a)</td><td>121.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.80 (n/a)</td><td>429.08 (n/a)</td><td>475.80 (n/a)</td><td>290.60 (n/a)</td><td>98.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.50 (n/a)</td><td>342.16 (n/a)</td><td>347.40 (n/a)</td><td>199.40 (n/a)</td><td>92.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.80 (n/a)</td><td>359.76 (n/a)</td><td>273.40 (n/a)</td><td>248.10 (n/a)</td><td>146.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.30 (n/a)</td><td>373.94 (n/a)</td><td>312.70 (n/a)</td><td>230.30 (n/a)</td><td>162.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.90 (n/a)</td><td>498.18 (n/a)</td><td>480.40 (n/a)</td><td>350.90 (n/a)</td><td>110.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1106.90 (n/a)</td><td>599.84 (n/a)</td><td>541.40 (n/a)</td><td>275.20 (n/a)</td><td>306.39 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2483.90 (n/a)</td><td>803.00 (n/a)</td><td>479.90 (n/a)</td><td>241.10 (n/a)</td><td>946.63 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.80 (n/a)</td><td>455.98 (n/a)</td><td>468.30 (n/a)</td><td>352.50 (n/a)</td><td>94.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>487.90 (n/a)</td><td>308.28 (n/a)</td><td>262.50 (n/a)</td><td>220.60 (n/a)</td><td>105.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.50 (n/a)</td><td>405.50 (n/a)</td><td>368.20 (n/a)</td><td>263.70 (n/a)</td><td>135.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>565.70 (n/a)</td><td>431.26 (n/a)</td><td>419.90 (n/a)</td><td>292.40 (n/a)</td><td>110.54 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>646.80 (n/a)</td><td>472.84 (n/a)</td><td>534.30 (n/a)</td><td>208.00 (n/a)</td><td>177.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.20 (n/a)</td><td>329.16 (n/a)</td><td>272.50 (n/a)</td><td>237.00 (n/a)</td><td>124.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>512.20 (n/a)</td><td>412.34 (n/a)</td><td>432.60 (n/a)</td><td>284.70 (n/a)</td><td>102.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>611.60 (n/a)</td><td>428.58 (n/a)</td><td>489.00 (n/a)</td><td>249.90 (n/a)</td><td>166.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>601.80 (n/a)</td><td>435.74 (n/a)</td><td>446.90 (n/a)</td><td>254.00 (n/a)</td><td>147.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>539.80 (n/a)</td><td>369.46 (n/a)</td><td>308.40 (n/a)</td><td>280.90 (n/a)</td><td>113.04 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>578.60 (n/a)</td><td>469.72 (n/a)</td><td>469.00 (n/a)</td><td>313.80 (n/a)</td><td>99.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1861.30 (n/a)</td><td>649.32 (n/a)</td><td>295.10 (n/a)</td><td>267.90 (n/a)</td><td>686.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>562.90 (n/a)</td><td>462.80 (n/a)</td><td>513.50 (n/a)</td><td>241.00 (n/a)</td><td>134.72 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(-28.24%)</b></td><td>0.01 (-9.07%)</td><td>0.01 (-6.92%)</td><td>0.01 (+13.69%)</td><td>0.00 <b>(-44.55%)</b></td><td>488.50 (-12.03%)</td><td>374.80 (+2.31%)</td><td>389.30 (+7.42%)</td><td>270.10 <b>(+39.37%)</b></td><td>92.19 <b>(-31.74%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.30 (n/a)</td><td>366.34 (n/a)</td><td>362.40 (n/a)</td><td>193.80 (n/a)</td><td>135.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (+13.70%)</td><td>0.01 <b>(+20.48%)</b></td><td>0.01 <b>(+32.62%)</b></td><td>0.01 (+18.79%)</td><td>0.00 (+10.41%)</td><td>471.30 (-15.82%)</td><td>373.42 (-17.36%)</td><td>356.90 <b>(-24.59%)</b></td><td>273.40 (-12.03%)</td><td>91.78 (-17.32%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.90 (n/a)</td><td>451.88 (n/a)</td><td>473.30 (n/a)</td><td>310.80 (n/a)</td><td>111.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-9.35%)</td><td>0.01 (-19.96%)</td><td>0.01 (-19.13%)</td><td>0.01 <b>(-21.62%)</b></td><td>0.00 (-9.13%)</td><td>662.30 <b>(+27.59%)</b></td><td>507.52 <b>(+25.66%)</b></td><td>562.70 <b>(+23.64%)</b></td><td>265.00 (+10.32%)</td><td>154.42 (+18.70%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.10 (n/a)</td><td>403.88 (n/a)</td><td>455.10 (n/a)</td><td>240.20 (n/a)</td><td>130.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (-17.41%)</td><td>0.01 (-13.39%)</td><td>0.01 (-16.94%)</td><td>0.01 (-9.84%)</td><td>0.00 <b>(-31.15%)</b></td><td>656.10 (+10.90%)</td><td>478.64 (+11.37%)</td><td>451.20 <b>(+20.38%)</b></td><td>335.60 <b>(+21.11%)</b></td><td>128.29 (-12.45%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.60 (n/a)</td><td>429.76 (n/a)</td><td>374.80 (n/a)</td><td>277.10 (n/a)</td><td>146.54 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (-14.93%)</td><td>0.01 (+6.02%)</td><td>0.01 <b>(+53.64%)</b></td><td>0.01 <b>(+23.14%)</b></td><td>0.00 <b>(-51.42%)</b></td><td>545.40 (-18.79%)</td><td>400.98 (-16.59%)</td><td>375.50 <b>(-34.92%)</b></td><td>315.90 (+17.57%)</td><td>94.79 <b>(-51.43%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>671.60 (n/a)</td><td>480.72 (n/a)</td><td>577.00 (n/a)</td><td>268.70 (n/a)</td><td>195.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (+7.20%)</td><td>0.01 (+1.38%)</td><td>0.01 (-0.66%)</td><td>0.01 (-3.26%)</td><td>0.00 (+18.89%)</td><td>597.10 (+3.38%)</td><td>471.78 (+0.44%)</td><td>504.70 (+0.68%)</td><td>277.70 (-6.75%)</td><td>122.21 (+14.35%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.60 (n/a)</td><td>469.72 (n/a)</td><td>501.30 (n/a)</td><td>297.80 (n/a)</td><td>106.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (+18.05%)</td><td>0.03 (+13.73%)</td><td>0.04 <b>(+33.69%)</b></td><td>0.02 (-3.46%)</td><td>0.01 <b>(+49.19%)</b></td><td>469.40 (+3.60%)</td><td>307.10 (-5.18%)</td><td>228.90 <b>(-25.20%)</b></td><td>175.40 (-15.31%)</td><td>134.96 <b>(+39.38%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>453.10 (n/a)</td><td>323.86 (n/a)</td><td>306.00 (n/a)</td><td>207.10 (n/a)</td><td>96.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-4.53%)</td><td>0.03 (+13.99%)</td><td>0.03 <b>(+31.64%)</b></td><td>0.02 (+16.54%)</td><td>0.00 <b>(-33.50%)</b></td><td>459.40 (-14.19%)</td><td>330.16 (-15.85%)</td><td>309.90 <b>(-24.03%)</b></td><td>273.30 (+4.75%)</td><td>73.81 <b>(-36.03%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.40 (n/a)</td><td>392.34 (n/a)</td><td>407.90 (n/a)</td><td>260.90 (n/a)</td><td>115.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (+8.14%)</td><td>0.02 (+7.93%)</td><td>0.02 (+0.16%)</td><td>0.02 <b>(+63.75%)</b></td><td>0.01 (-17.46%)</td><td>479.70 <b>(-38.93%)</b></td><td>383.64 (-16.52%)</td><td>441.20 (-0.18%)</td><td>224.30 (-7.51%)</td><td>109.77 <b>(-50.62%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>785.50 (n/a)</td><td>459.56 (n/a)</td><td>442.00 (n/a)</td><td>242.50 (n/a)</td><td>222.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (-2.69%)</td><td>0.02 <b>(-28.48%)</b></td><td>0.02 <b>(-40.96%)</b></td><td>0.00 <b>(-76.04%)</b></td><td>0.01 <b>(+29.15%)</b></td><td>2151.20 <b>(+317.30%)</b></td><td>776.96 <b>(+110.46%)</b></td><td>512.80 <b>(+69.41%)</b></td><td>233.10 (+2.78%)</td><td>777.37 <b>(+474.95%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.50 (n/a)</td><td>369.18 (n/a)</td><td>302.70 (n/a)</td><td>226.80 (n/a)</td><td>135.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-9.02%)</td><td>0.03 (+13.17%)</td><td>0.03 (+19.60%)</td><td>0.01 (-6.86%)</td><td>0.01 (-11.96%)</td><td>555.30 (+7.37%)</td><td>331.66 (-12.31%)</td><td>280.60 (-16.39%)</td><td>263.70 (+9.92%)</td><td>125.42 (+1.47%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.20 (n/a)</td><td>378.22 (n/a)</td><td>335.60 (n/a)</td><td>239.90 (n/a)</td><td>123.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(-24.19%)</b></td><td>0.02 (-13.44%)</td><td>0.02 (-12.01%)</td><td>0.02 (+12.70%)</td><td>0.00 <b>(-64.27%)</b></td><td>488.70 (-11.27%)</td><td>434.72 (+9.96%)</td><td>437.40 (+13.64%)</td><td>365.20 <b>(+31.94%)</b></td><td>44.36 <b>(-58.92%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.80 (n/a)</td><td>395.36 (n/a)</td><td>384.90 (n/a)</td><td>276.80 (n/a)</td><td>108.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (+4.07%)</td><td>0.02 (-7.40%)</td><td>0.02 (-16.56%)</td><td>0.01 <b>(-20.99%)</b></td><td>0.01 <b>(+34.01%)</b></td><td>628.90 <b>(+26.56%)</b></td><td>481.78 (+12.36%)</td><td>529.10 (+19.84%)</td><td>278.90 (-3.89%)</td><td>131.26 <b>(+58.94%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>496.90 (n/a)</td><td>428.78 (n/a)</td><td>441.50 (n/a)</td><td>290.20 (n/a)</td><td>82.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 <b>(+21.06%)</b></td><td>0.02 <b>(+20.87%)</b></td><td>0.02 (-4.21%)</td><td>0.01 <b>(+193.07%)</b></td><td>0.01 (-18.62%)</td><td>650.50 <b>(-65.88%)</b></td><td>469.22 <b>(-37.88%)</b></td><td>476.00 (+4.41%)</td><td>287.60 (-17.38%)</td><td>129.03 <b>(-80.17%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1906.40 (n/a)</td><td>755.34 (n/a)</td><td>455.90 (n/a)</td><td>348.10 (n/a)</td><td>650.81 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (+7.83%)</td><td>0.05 (+19.32%)</td><td>0.06 <b>(+76.32%)</b></td><td>0.01 <b>(-62.80%)</b></td><td>0.03 <b>(+35.27%)</b></td><td>1812.40 <b>(+168.78%)</b></td><td>574.94 <b>(+33.60%)</b></td><td>271.50 <b>(-43.28%)</b></td><td>204.70 (-7.29%)</td><td>694.05 <b>(+284.95%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>674.30 (n/a)</td><td>430.36 (n/a)</td><td>478.70 (n/a)</td><td>220.80 (n/a)</td><td>180.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-3.91%)</td><td>0.05 <b>(+27.55%)</b></td><td>0.06 <b>(+72.28%)</b></td><td>0.03 (+9.47%)</td><td>0.02 (+5.35%)</td><td>541.40 (-8.66%)</td><td>362.26 <b>(-20.61%)</b></td><td>275.30 <b>(-41.96%)</b></td><td>253.10 (+4.07%)</td><td>138.22 (+6.22%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.70 (n/a)</td><td>456.28 (n/a)</td><td>474.30 (n/a)</td><td>243.20 (n/a)</td><td>130.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-16.62%)</td><td>0.05 (-11.39%)</td><td>0.06 (+8.33%)</td><td>0.04 (-12.93%)</td><td>0.01 (+6.93%)</td><td>466.70 (+14.84%)</td><td>334.24 (+15.85%)</td><td>260.40 (-7.69%)</td><td>252.30 (+19.97%)</td><td>105.96 <b>(+42.98%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>406.40 (n/a)</td><td>288.52 (n/a)</td><td>282.10 (n/a)</td><td>210.30 (n/a)</td><td>74.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (+0.42%)</td><td>0.04 (+0.92%)</td><td>0.04 (+3.66%)</td><td>0.03 <b>(+21.87%)</b></td><td>0.01 (-18.53%)</td><td>563.70 (-17.95%)</td><td>409.04 (-5.86%)</td><td>433.00 (-3.52%)</td><td>265.00 (-0.41%)</td><td>118.95 <b>(-30.81%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>687.00 (n/a)</td><td>434.50 (n/a)</td><td>448.80 (n/a)</td><td>266.10 (n/a)</td><td>171.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 <b>(+28.21%)</b></td><td>0.05 (-8.04%)</td><td>0.04 <b>(-41.14%)</b></td><td>0.03 (-9.52%)</td><td>0.02 <b>(+92.58%)</b></td><td>518.00 (+10.52%)</td><td>377.06 <b>(+21.16%)</b></td><td>456.40 <b>(+69.85%)</b></td><td>186.00 <b>(-22.01%)</b></td><td>149.14 <b>(+62.30%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>468.70 (n/a)</td><td>311.20 (n/a)</td><td>268.70 (n/a)</td><td>238.50 (n/a)</td><td>91.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (+9.46%)</td><td>0.04 (-6.05%)</td><td>0.04 (+1.67%)</td><td>0.03 <b>(-22.24%)</b></td><td>0.01 <b>(+74.45%)</b></td><td>619.60 <b>(+28.60%)</b></td><td>472.64 (+9.57%)</td><td>438.70 (-1.64%)</td><td>343.50 (-8.64%)</td><td>106.22 <b>(+108.87%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>481.80 (n/a)</td><td>431.36 (n/a)</td><td>446.00 (n/a)</td><td>376.00 (n/a)</td><td>50.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (+13.30%)</td><td>0.09 (-7.70%)</td><td>0.07 <b>(-36.08%)</b></td><td>0.06 (+9.67%)</td><td>0.03 (+6.46%)</td><td>545.70 (-8.81%)</td><td>398.14 (+7.52%)</td><td>447.50 <b>(+56.41%)</b></td><td>234.80 (-11.73%)</td><td>125.73 (-12.95%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>598.40 (n/a)</td><td>370.30 (n/a)</td><td>286.10 (n/a)</td><td>266.00 (n/a)</td><td>144.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 <b>(-40.43%)</b></td><td>0.09 <b>(-21.02%)</b></td><td>0.08 <b>(-33.22%)</b></td><td>0.07 <b>(+277.61%)</b></td><td>0.03 <b>(-60.39%)</b></td><td>500.80 <b>(-73.52%)</b></td><td>388.88 <b>(-33.03%)</b></td><td>417.90 <b>(+49.73%)</b></td><td>272.00 <b>(+67.90%)</b></td><td>105.90 <b>(-85.59%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>1891.10 (n/a)</td><td>580.64 (n/a)</td><td>279.10 (n/a)</td><td>162.00 (n/a)</td><td>734.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 <b>(-36.87%)</b></td><td>0.06 <b>(-32.95%)</b></td><td>0.06 <b>(-23.95%)</b></td><td>0.02 <b>(-71.99%)</b></td><td>0.03 <b>(-24.08%)</b></td><td>1856.20 <b>(+257.03%)</b></td><td>763.68 <b>(+86.88%)</b></td><td>568.90 <b>(+31.48%)</b></td><td>333.20 <b>(+58.44%)</b></td><td>618.59 <b>(+414.29%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>519.90 (n/a)</td><td>408.64 (n/a)</td><td>432.70 (n/a)</td><td>210.30 (n/a)</td><td>120.28 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 <b>(+66.93%)</b></td><td>0.08 (+13.35%)</td><td>0.07 (-3.58%)</td><td>0.05 (-9.49%)</td><td>0.04 <b>(+233.41%)</b></td><td>652.30 (+10.48%)</td><td>472.86 (-2.16%)</td><td>488.10 (+3.72%)</td><td>237.10 <b>(-40.10%)</b></td><td>158.53 <b>(+110.10%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>590.40 (n/a)</td><td>483.28 (n/a)</td><td>470.60 (n/a)</td><td>395.80 (n/a)</td><td>75.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (-17.54%)</td><td>0.08 (-17.06%)</td><td>0.06 (-11.84%)</td><td>0.02 <b>(-62.20%)</b></td><td>0.04 (+10.76%)</td><td>1371.10 <b>(+164.54%)</b></td><td>600.44 <b>(+52.58%)</b></td><td>517.00 (+13.43%)</td><td>255.60 <b>(+21.31%)</b></td><td>451.23 <b>(+259.01%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>518.30 (n/a)</td><td>393.52 (n/a)</td><td>455.80 (n/a)</td><td>210.70 (n/a)</td><td>125.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+36.14%)</b></td><td>0.02 (+16.22%)</td><td>0.02 (-3.89%)</td><td>0.01 (-5.19%)</td><td>0.01 <b>(+68.08%)</b></td><td>532.90 (+5.48%)</td><td>327.80 (-5.20%)</td><td>272.70 (+4.04%)</td><td>181.10 <b>(-26.56%)</b></td><td>160.68 <b>(+29.46%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.20 (n/a)</td><td>345.78 (n/a)</td><td>262.10 (n/a)</td><td>246.60 (n/a)</td><td>124.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+37.69%)</b></td><td>0.02 <b>(+57.50%)</b></td><td>0.02 <b>(+61.90%)</b></td><td>0.01 <b>(+409.63%)</b></td><td>0.00 <b>(-35.47%)</b></td><td>357.60 <b>(-80.38%)</b></td><td>263.52 <b>(-59.32%)</b></td><td>253.90 <b>(-38.22%)</b></td><td>193.80 <b>(-27.39%)</b></td><td>59.10 <b>(-91.07%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1822.30 (n/a)</td><td>647.84 (n/a)</td><td>411.00 (n/a)</td><td>266.90 (n/a)</td><td>662.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+1.39%)</td><td>0.01 (-4.77%)</td><td>0.01 (-10.73%)</td><td>0.01 (-15.74%)</td><td>0.01 (+18.46%)</td><td>600.50 (+18.68%)</td><td>373.82 (+11.04%)</td><td>316.40 (+12.04%)</td><td>208.10 (-1.37%)</td><td>165.07 <b>(+37.86%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.00 (n/a)</td><td>336.64 (n/a)</td><td>282.40 (n/a)</td><td>211.00 (n/a)</td><td>119.74 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+8.63%)</td><td>0.01 <b>(+23.96%)</b></td><td>0.01 <b>(+38.07%)</b></td><td>0.01 (+8.61%)</td><td>0.00 (+4.74%)</td><td>508.60 (-7.93%)</td><td>388.78 (-19.57%)</td><td>387.10 <b>(-27.56%)</b></td><td>257.60 (-7.93%)</td><td>106.38 (-7.73%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.40 (n/a)</td><td>483.40 (n/a)</td><td>534.40 (n/a)</td><td>279.80 (n/a)</td><td>115.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 <b>(-36.76%)</b></td><td>0.01 <b>(-29.02%)</b></td><td>0.01 <b>(-26.38%)</b></td><td>0.01 (-6.58%)</td><td>0.00 <b>(-61.70%)</b></td><td>592.30 (+7.05%)</td><td>450.28 <b>(+29.66%)</b></td><td>448.70 <b>(+35.81%)</b></td><td>352.20 <b>(+58.15%)</b></td><td>92.58 <b>(-32.02%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.30 (n/a)</td><td>347.28 (n/a)</td><td>330.40 (n/a)</td><td>222.70 (n/a)</td><td>136.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+12.38%)</td><td>0.02 <b>(+21.29%)</b></td><td>0.02 (+12.64%)</td><td>0.02 <b>(+80.83%)</b></td><td>0.00 <b>(-69.73%)</b></td><td>270.50 <b>(-44.71%)</b></td><td>255.88 <b>(-21.30%)</b></td><td>257.10 (-11.22%)</td><td>237.00 (-11.04%)</td><td>13.12 <b>(-85.79%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.20 (n/a)</td><td>325.14 (n/a)</td><td>289.60 (n/a)</td><td>266.40 (n/a)</td><td>92.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-6.26%)</td><td>0.01 (+15.32%)</td><td>0.01 <b>(+38.32%)</b></td><td>0.01 (-6.34%)</td><td>0.00 (-6.66%)</td><td>599.10 (+6.75%)</td><td>377.82 (-12.95%)</td><td>308.00 <b>(-27.70%)</b></td><td>259.90 (+6.65%)</td><td>137.94 (+11.68%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.20 (n/a)</td><td>434.02 (n/a)</td><td>426.00 (n/a)</td><td>243.70 (n/a)</td><td>123.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 <b>(+38.02%)</b></td><td>0.01 (+17.52%)</td><td>0.01 (+3.81%)</td><td>0.01 (+8.31%)</td><td>0.00 <b>(+69.77%)</b></td><td>544.20 (-7.68%)</td><td>427.42 (-13.44%)</td><td>433.70 (-3.67%)</td><td>292.90 <b>(-27.55%)</b></td><td>89.71 (+5.55%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.50 (n/a)</td><td>493.78 (n/a)</td><td>450.20 (n/a)</td><td>404.30 (n/a)</td><td>84.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+66.14%)</b></td><td>0.01 <b>(+30.34%)</b></td><td>0.01 (+19.47%)</td><td>0.01 (+3.08%)</td><td>0.00 <b>(+162.66%)</b></td><td>598.80 (-2.98%)</td><td>449.98 (-16.09%)</td><td>467.30 (-16.28%)</td><td>224.70 <b>(-39.81%)</b></td><td>148.42 <b>(+53.87%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.20 (n/a)</td><td>536.26 (n/a)</td><td>558.20 (n/a)</td><td>373.30 (n/a)</td><td>96.46 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (-15.61%)</td><td>0.01 (-14.72%)</td><td>0.01 <b>(-23.95%)</b></td><td>0.01 (+6.72%)</td><td>0.00 <b>(-38.98%)</b></td><td>574.90 (-6.29%)</td><td>401.12 (+6.71%)</td><td>332.30 <b>(+31.50%)</b></td><td>279.50 (+18.48%)</td><td>128.82 <b>(-29.35%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.50 (n/a)</td><td>375.90 (n/a)</td><td>252.70 (n/a)</td><td>235.90 (n/a)</td><td>182.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (-3.75%)</td><td>0.01 (+1.69%)</td><td>0.01 (-14.89%)</td><td>0.01 <b>(+75.38%)</b></td><td>0.00 <b>(-23.37%)</b></td><td>610.40 <b>(-42.98%)</b></td><td>496.22 (-13.16%)</td><td>539.20 (+17.50%)</td><td>283.50 (+3.88%)</td><td>125.64 <b>(-58.61%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1070.50 (n/a)</td><td>571.44 (n/a)</td><td>458.90 (n/a)</td><td>272.90 (n/a)</td><td>303.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 <b>(-22.27%)</b></td><td>0.01 (-5.35%)</td><td>0.01 (+3.47%)</td><td>0.01 <b>(-26.59%)</b></td><td>0.00 (-14.46%)</td><td>734.00 <b>(+36.23%)</b></td><td>482.34 (+7.49%)</td><td>473.40 (-3.37%)</td><td>328.40 <b>(+28.68%)</b></td><td>168.14 <b>(+47.55%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.80 (n/a)</td><td>448.74 (n/a)</td><td>489.90 (n/a)</td><td>255.20 (n/a)</td><td>113.95 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-18.48%)</td><td>0.02 <b>(-24.36%)</b></td><td>0.03 <b>(-20.52%)</b></td><td>0.02 (-3.56%)</td><td>0.01 <b>(-20.15%)</b></td><td>479.20 (+3.70%)</td><td>363.18 <b>(+30.41%)</b></td><td>291.60 <b>(+25.80%)</b></td><td>278.70 <b>(+22.67%)</b></td><td>104.93 (+2.08%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.10 (n/a)</td><td>278.50 (n/a)</td><td>231.80 (n/a)</td><td>227.20 (n/a)</td><td>102.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (+6.22%)</td><td>0.03 (+18.85%)</td><td>0.03 (+4.67%)</td><td>0.02 (+12.13%)</td><td>0.01 (-11.65%)</td><td>487.10 (-10.82%)</td><td>300.94 (-19.72%)</td><td>272.00 (-4.46%)</td><td>218.80 (-5.85%)</td><td>108.58 <b>(-29.11%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.20 (n/a)</td><td>374.84 (n/a)</td><td>284.70 (n/a)</td><td>232.40 (n/a)</td><td>153.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-2.28%)</td><td>0.02 <b>(-29.44%)</b></td><td>0.02 <b>(-34.27%)</b></td><td>0.00 <b>(-76.95%)</b></td><td>0.01 <b>(+66.23%)</b></td><td>1903.80 <b>(+333.87%)</b></td><td>700.84 <b>(+118.09%)</b></td><td>445.00 <b>(+52.14%)</b></td><td>235.80 (+2.34%)</td><td>682.70 <b>(+713.74%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.80 (n/a)</td><td>321.36 (n/a)</td><td>292.50 (n/a)</td><td>230.40 (n/a)</td><td>83.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-11.92%)</td><td>0.03 (-4.31%)</td><td>0.03 (-2.84%)</td><td>0.02 (+17.29%)</td><td>0.01 <b>(-28.04%)</b></td><td>442.80 (-14.75%)</td><td>314.46 (+0.13%)</td><td>267.40 (+2.93%)</td><td>263.50 (+13.53%)</td><td>77.23 <b>(-34.45%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.40 (n/a)</td><td>314.04 (n/a)</td><td>259.80 (n/a)</td><td>232.10 (n/a)</td><td>117.81 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-12.91%)</td><td>0.02 (-11.19%)</td><td>0.02 (-5.06%)</td><td>0.01 (-11.98%)</td><td>0.01 <b>(-21.44%)</b></td><td>668.70 (+13.61%)</td><td>470.52 (+8.78%)</td><td>495.50 (+5.34%)</td><td>258.50 (+14.79%)</td><td>159.23 (-3.55%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.60 (n/a)</td><td>432.56 (n/a)</td><td>470.40 (n/a)</td><td>225.20 (n/a)</td><td>165.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 <b>(-31.22%)</b></td><td>0.02 <b>(-24.21%)</b></td><td>0.03 (-5.99%)</td><td>0.01 (-13.71%)</td><td>0.01 <b>(-28.28%)</b></td><td>549.30 (+15.89%)</td><td>370.94 <b>(+30.23%)</b></td><td>288.80 (+6.37%)</td><td>263.10 <b>(+45.36%)</b></td><td>134.55 (+17.22%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>474.00 (n/a)</td><td>284.84 (n/a)</td><td>271.50 (n/a)</td><td>181.00 (n/a)</td><td>114.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 <b>(+25.47%)</b></td><td>0.02 (-2.84%)</td><td>0.02 (-6.22%)</td><td>0.01 (-13.31%)</td><td>0.01 <b>(+37.53%)</b></td><td>594.90 (+15.36%)</td><td>401.34 (+9.84%)</td><td>402.30 (+6.63%)</td><td>180.40 <b>(-20.32%)</b></td><td>161.70 <b>(+26.55%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.70 (n/a)</td><td>365.40 (n/a)</td><td>377.30 (n/a)</td><td>226.40 (n/a)</td><td>127.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-4.07%)</td><td>0.02 (-9.73%)</td><td>0.02 <b>(-30.84%)</b></td><td>0.02 (-6.96%)</td><td>0.01 (-9.12%)</td><td>544.80 (+7.50%)</td><td>388.12 (+9.20%)</td><td>410.80 <b>(+44.60%)</b></td><td>240.10 (+4.21%)</td><td>120.32 (-5.36%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.80 (n/a)</td><td>355.42 (n/a)</td><td>284.10 (n/a)</td><td>230.40 (n/a)</td><td>127.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 <b>(-22.17%)</b></td><td>0.02 (-1.39%)</td><td>0.02 (+3.08%)</td><td>0.02 (+10.48%)</td><td>0.01 <b>(-31.85%)</b></td><td>490.40 (-9.49%)</td><td>382.14 (-5.09%)</td><td>420.70 (-2.98%)</td><td>252.40 <b>(+28.45%)</b></td><td>114.69 <b>(-24.00%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.80 (n/a)</td><td>402.64 (n/a)</td><td>433.60 (n/a)</td><td>196.50 (n/a)</td><td>150.92 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (-1.96%)</td><td>0.03 (-3.22%)</td><td>0.03 (-16.88%)</td><td>0.02 <b>(+39.94%)</b></td><td>0.01 (-18.83%)</td><td>488.00 <b>(-28.53%)</b></td><td>312.56 (-6.14%)</td><td>304.30 <b>(+20.32%)</b></td><td>210.50 (+2.04%)</td><td>108.05 <b>(-45.28%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.80 (n/a)</td><td>333.00 (n/a)</td><td>252.90 (n/a)</td><td>206.30 (n/a)</td><td>197.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(-45.72%)</b></td><td>0.02 (-2.33%)</td><td>0.02 <b>(+33.97%)</b></td><td>0.00 (+1.85%)</td><td>0.01 <b>(-45.30%)</b></td><td>1921.10 (-1.81%)</td><td>752.90 (-7.96%)</td><td>466.20 <b>(-25.35%)</b></td><td>443.30 <b>(+84.25%)</b></td><td>653.13 (-0.84%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1956.50 (n/a)</td><td>818.00 (n/a)</td><td>624.50 (n/a)</td><td>240.60 (n/a)</td><td>658.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (+10.00%)</td><td>0.02 (+4.69%)</td><td>0.03 (+8.05%)</td><td>0.01 (-6.90%)</td><td>0.01 <b>(+54.91%)</b></td><td>557.50 (+7.42%)</td><td>366.36 (+0.23%)</td><td>310.30 (-7.46%)</td><td>255.00 (-9.09%)</td><td>129.47 <b>(+42.76%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>519.00 (n/a)</td><td>365.52 (n/a)</td><td>335.30 (n/a)</td><td>280.50 (n/a)</td><td>90.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-16.37%)</td><td>0.05 (+1.70%)</td><td>0.05 <b>(+27.66%)</b></td><td>0.03 (+0.09%)</td><td>0.01 <b>(-23.47%)</b></td><td>480.30 (-0.08%)</td><td>364.54 (-3.36%)</td><td>327.10 <b>(-21.65%)</b></td><td>260.40 (+19.56%)</td><td>100.47 (-0.71%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>480.70 (n/a)</td><td>377.20 (n/a)</td><td>417.50 (n/a)</td><td>217.80 (n/a)</td><td>101.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (-5.67%)</td><td>0.05 (+9.50%)</td><td>0.06 <b>(+37.80%)</b></td><td>0.03 (+11.74%)</td><td>0.02 (-9.63%)</td><td>527.80 (-10.51%)</td><td>350.06 (-10.93%)</td><td>287.90 <b>(-27.43%)</b></td><td>234.00 (+6.03%)</td><td>132.15 (-13.21%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.80 (n/a)</td><td>393.02 (n/a)</td><td>396.70 (n/a)</td><td>220.70 (n/a)</td><td>152.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 <b>(+48.18%)</b></td><td>0.04 (+17.31%)</td><td>0.04 (+1.77%)</td><td>0.01 <b>(-44.18%)</b></td><td>0.02 <b>(+162.20%)</b></td><td>1276.80 <b>(+79.15%)</b></td><td>576.00 (+12.50%)</td><td>460.60 (-1.75%)</td><td>247.50 <b>(-32.52%)</b></td><td>415.94 <b>(+213.21%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>712.70 (n/a)</td><td>512.00 (n/a)</td><td>468.80 (n/a)</td><td>366.80 (n/a)</td><td>132.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (-1.10%)</td><td>0.04 (+0.22%)</td><td>0.04 (+6.64%)</td><td>0.01 <b>(-66.27%)</b></td><td>0.02 <b>(+32.39%)</b></td><td>1993.80 <b>(+196.48%)</b></td><td>668.30 <b>(+53.58%)</b></td><td>400.90 (-6.22%)</td><td>242.70 (+1.12%)</td><td>745.71 <b>(+332.68%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>672.50 (n/a)</td><td>435.14 (n/a)</td><td>427.50 (n/a)</td><td>240.00 (n/a)</td><td>172.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (+16.59%)</td><td>0.06 <b>(+24.57%)</b></td><td>0.06 <b>(+31.99%)</b></td><td>0.04 (+0.70%)</td><td>0.02 <b>(+51.08%)</b></td><td>464.30 (-0.71%)</td><td>326.32 (-15.66%)</td><td>295.10 <b>(-24.24%)</b></td><td>212.60 (-14.21%)</td><td>114.82 <b>(+35.49%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>467.60 (n/a)</td><td>386.92 (n/a)</td><td>389.50 (n/a)</td><td>247.80 (n/a)</td><td>84.74 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-18.43%)</td><td>0.05 (+2.78%)</td><td>0.05 <b>(+47.83%)</b></td><td>0.03 <b>(+34.92%)</b></td><td>0.01 <b>(-45.28%)</b></td><td>473.70 <b>(-25.88%)</b></td><td>357.62 (-15.55%)</td><td>306.10 <b>(-32.35%)</b></td><td>254.00 <b>(+22.59%)</b></td><td>105.00 <b>(-46.46%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>639.10 (n/a)</td><td>423.46 (n/a)</td><td>452.50 (n/a)</td><td>207.20 (n/a)</td><td>196.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (-18.23%)</td><td>0.06 <b>(+20.46%)</b></td><td>0.06 <b>(+86.27%)</b></td><td>0.03 <b>(+20.20%)</b></td><td>0.01 <b>(-43.51%)</b></td><td>502.40 (-16.81%)</td><td>308.94 <b>(-27.77%)</b></td><td>261.10 <b>(-46.32%)</b></td><td>242.40 <b>(+22.30%)</b></td><td>109.97 <b>(-43.36%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>603.90 (n/a)</td><td>427.72 (n/a)</td><td>486.40 (n/a)</td><td>198.20 (n/a)</td><td>194.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (+18.52%)</td><td>0.06 <b>(+51.08%)</b></td><td>0.07 <b>(+91.07%)</b></td><td>0.03 (-1.92%)</td><td>0.02 <b>(+49.58%)</b></td><td>627.30 (+1.95%)</td><td>330.70 <b>(-29.25%)</b></td><td>244.70 <b>(-47.66%)</b></td><td>240.30 (-15.62%)</td><td>167.68 <b>(+33.59%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>615.30 (n/a)</td><td>467.44 (n/a)</td><td>467.50 (n/a)</td><td>284.80 (n/a)</td><td>125.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 <b>(+65.56%)</b></td><td>0.05 <b>(+43.47%)</b></td><td>0.05 <b>(+72.97%)</b></td><td>0.03 (+6.89%)</td><td>0.02 <b>(+178.56%)</b></td><td>544.70 (-6.44%)</td><td>377.02 <b>(-24.91%)</b></td><td>317.10 <b>(-42.20%)</b></td><td>248.50 <b>(-39.60%)</b></td><td>133.67 <b>(+65.66%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>502.10 (n/a)</td><td>548.60 (n/a)</td><td>411.40 (n/a)</td><td>80.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 <b>(-28.37%)</b></td><td>0.06 (+8.96%)</td><td>0.06 (+14.86%)</td><td>0.04 <b>(+44.95%)</b></td><td>0.01 <b>(-63.37%)</b></td><td>371.20 <b>(-31.00%)</b></td><td>284.74 <b>(-20.62%)</b></td><td>263.10 (-12.91%)</td><td>244.70 <b>(+39.59%)</b></td><td>52.11 <b>(-66.52%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>538.00 (n/a)</td><td>358.72 (n/a)</td><td>302.10 (n/a)</td><td>175.30 (n/a)</td><td>155.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-15.84%)</td><td>0.04 (-13.73%)</td><td>0.05 (+7.66%)</td><td>0.01 <b>(-58.88%)</b></td><td>0.02 (+17.46%)</td><td>1432.80 <b>(+143.22%)</b></td><td>580.34 <b>(+49.19%)</b></td><td>308.60 (-7.13%)</td><td>290.10 (+18.80%)</td><td>489.89 <b>(+227.77%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.10 (n/a)</td><td>389.00 (n/a)</td><td>332.30 (n/a)</td><td>244.20 (n/a)</td><td>149.46 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 <b>(+23.51%)</b></td><td>0.05 (+16.44%)</td><td>0.06 <b>(+40.96%)</b></td><td>0.01 <b>(-76.97%)</b></td><td>0.02 <b>(+259.84%)</b></td><td>2094.80 <b>(+334.16%)</b></td><td>639.12 <b>(+62.36%)</b></td><td>270.70 <b>(-29.06%)</b></td><td>258.70 (-19.03%)</td><td>813.98 <b>(+1211.77%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>482.50 (n/a)</td><td>393.64 (n/a)</td><td>381.60 (n/a)</td><td>319.50 (n/a)</td><td>62.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.16 <b>(+21.87%)</b></td><td>0.12 <b>(+23.50%)</b></td><td>0.12 <b>(+25.99%)</b></td><td>0.08 (+17.80%)</td><td>0.03 (+17.57%)</td><td>407.30 (-15.09%)</td><td>300.10 (-19.39%)</td><td>277.40 <b>(-20.63%)</b></td><td>205.60 (-17.92%)</td><td>80.70 <b>(-20.99%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>479.70 (n/a)</td><td>372.30 (n/a)</td><td>349.50 (n/a)</td><td>250.50 (n/a)</td><td>102.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (+12.07%)</td><td>0.10 (+17.02%)</td><td>0.11 <b>(+33.47%)</b></td><td>0.07 <b>(+28.77%)</b></td><td>0.03 (+5.30%)</td><td>478.00 <b>(-22.34%)</b></td><td>337.66 (-15.97%)</td><td>294.60 <b>(-25.08%)</b></td><td>240.30 (-10.77%)</td><td>108.33 <b>(-24.01%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>615.50 (n/a)</td><td>401.82 (n/a)</td><td>393.20 (n/a)</td><td>269.30 (n/a)</td><td>142.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 <b>(+24.22%)</b></td><td>0.11 <b>(+47.46%)</b></td><td>0.11 <b>(+49.92%)</b></td><td>0.06 <b>(+219.56%)</b></td><td>0.04 (+10.00%)</td><td>577.80 <b>(-68.71%)</b></td><td>355.44 <b>(-48.69%)</b></td><td>303.30 <b>(-33.30%)</b></td><td>214.60 (-19.50%)</td><td>153.33 <b>(-76.41%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1846.50 (n/a)</td><td>692.74 (n/a)</td><td>454.70 (n/a)</td><td>266.60 (n/a)</td><td>649.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (+2.63%)</td><td>0.12 (+0.44%)</td><td>0.12 (+2.16%)</td><td>0.10 (-6.54%)</td><td>0.01 <b>(+27.47%)</b></td><td>313.20 (+7.00%)</td><td>274.08 (-0.04%)</td><td>277.70 (-2.11%)</td><td>230.10 (-2.58%)</td><td>29.65 <b>(+33.16%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>292.70 (n/a)</td><td>274.20 (n/a)</td><td>283.70 (n/a)</td><td>236.20 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 <b>(+27.06%)</b></td><td>0.11 <b>(+25.58%)</b></td><td>0.14 <b>(+75.40%)</b></td><td>0.06 (-1.75%)</td><td>0.05 <b>(+63.38%)</b></td><td>568.40 (+1.79%)</td><td>357.78 (-12.06%)</td><td>240.30 <b>(-42.98%)</b></td><td>215.20 <b>(-21.29%)</b></td><td>177.34 <b>(+39.74%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>558.40 (n/a)</td><td>406.84 (n/a)</td><td>421.40 (n/a)</td><td>273.40 (n/a)</td><td>126.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (+3.05%)</td><td>0.11 <b>(+29.44%)</b></td><td>0.11 <b>(+53.69%)</b></td><td>0.09 <b>(+42.46%)</b></td><td>0.01 <b>(-49.87%)</b></td><td>368.20 <b>(-29.80%)</b></td><td>303.72 <b>(-26.23%)</b></td><td>289.80 <b>(-34.93%)</b></td><td>276.10 (-2.95%)</td><td>36.77 <b>(-64.63%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>524.50 (n/a)</td><td>411.70 (n/a)</td><td>445.40 (n/a)</td><td>284.50 (n/a)</td><td>103.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.18 <b>(+40.24%)</b></td><td>0.11 (+18.58%)</td><td>0.11 (+6.73%)</td><td>0.05 (-13.29%)</td><td>0.05 <b>(+74.73%)</b></td><td>672.10 (+15.32%)</td><td>366.74 (-5.61%)</td><td>298.50 (-6.31%)</td><td>185.80 <b>(-28.70%)</b></td><td>195.24 <b>(+43.53%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>582.80 (n/a)</td><td>388.54 (n/a)</td><td>318.60 (n/a)</td><td>260.60 (n/a)</td><td>136.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 <b>(+48.49%)</b></td><td>0.11 <b>(+47.01%)</b></td><td>0.12 <b>(+47.63%)</b></td><td>0.06 (-7.15%)</td><td>0.04 <b>(+136.80%)</b></td><td>551.60 (+7.71%)</td><td>319.12 <b>(-26.11%)</b></td><td>280.40 <b>(-32.25%)</b></td><td>216.40 <b>(-32.67%)</b></td><td>136.78 <b>(+68.65%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>512.10 (n/a)</td><td>431.88 (n/a)</td><td>413.90 (n/a)</td><td>321.40 (n/a)</td><td>81.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.11 (+6.44%)</td><td>0.08 (+6.48%)</td><td>0.08 (+8.67%)</td><td>0.05 (-17.50%)</td><td>0.03 <b>(+61.94%)</b></td><td>638.60 <b>(+21.20%)</b></td><td>429.30 (-0.50%)</td><td>389.00 (-7.97%)</td><td>296.90 (-6.04%)</td><td>148.52 <b>(+76.33%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>526.90 (n/a)</td><td>431.44 (n/a)</td><td>422.70 (n/a)</td><td>316.00 (n/a)</td><td>84.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (-5.35%)</td><td>0.10 (+2.10%)</td><td>0.11 <b>(+25.77%)</b></td><td>0.06 (-4.64%)</td><td>0.03 <b>(+21.40%)</b></td><td>509.20 (+4.86%)</td><td>357.56 (+0.35%)</td><td>287.60 <b>(-20.49%)</b></td><td>276.90 (+5.69%)</td><td>108.31 <b>(+29.00%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>485.60 (n/a)</td><td>356.32 (n/a)</td><td>361.70 (n/a)</td><td>262.00 (n/a)</td><td>83.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (+7.95%)</td><td>0.08 (-7.80%)</td><td>0.07 <b>(-22.37%)</b></td><td>0.06 (-17.03%)</td><td>0.03 <b>(+25.01%)</b></td><td>595.10 <b>(+20.51%)</b></td><td>421.40 (+11.74%)</td><td>437.60 <b>(+28.78%)</b></td><td>261.40 (-7.37%)</td><td>127.29 <b>(+34.24%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>493.80 (n/a)</td><td>377.12 (n/a)</td><td>339.80 (n/a)</td><td>282.20 (n/a)</td><td>94.82 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (+14.21%)</td><td>0.09 (+3.22%)</td><td>0.07 <b>(-29.28%)</b></td><td>0.05 (+7.39%)</td><td>0.04 <b>(+23.41%)</b></td><td>616.00 (-6.88%)</td><td>416.86 (-1.41%)</td><td>456.50 <b>(+41.38%)</b></td><td>245.10 (-12.43%)</td><td>162.61 (-5.62%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>661.50 (n/a)</td><td>422.82 (n/a)</td><td>322.90 (n/a)</td><td>279.90 (n/a)</td><td>172.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+16.45%)</td><td>0.01 <b>(-21.07%)</b></td><td>0.01 <b>(-29.00%)</b></td><td>0.00 <b>(-81.01%)</b></td><td>0.01 <b>(+151.49%)</b></td><td>2440.60 <b>(+426.67%)</b></td><td>773.22 <b>(+136.20%)</b></td><td>416.00 <b>(+40.87%)</b></td><td>247.90 (-14.13%)</td><td>936.84 <b>(+1130.86%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.40 (n/a)</td><td>327.36 (n/a)</td><td>295.30 (n/a)</td><td>288.70 (n/a)</td><td>76.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 <b>(-26.73%)</b></td><td>0.01 (-2.59%)</td><td>0.01 (+7.69%)</td><td>0.01 (-1.22%)</td><td>0.00 <b>(-50.42%)</b></td><td>638.00 (+1.24%)</td><td>488.42 (-1.93%)</td><td>452.10 (-7.15%)</td><td>416.80 <b>(+36.52%)</b></td><td>91.11 <b>(-32.66%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>630.20 (n/a)</td><td>498.04 (n/a)</td><td>486.90 (n/a)</td><td>305.30 (n/a)</td><td>135.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+23.88%)</b></td><td>0.01 (-2.13%)</td><td>0.01 (-13.05%)</td><td>0.00 <b>(-69.12%)</b></td><td>0.01 <b>(+112.78%)</b></td><td>1863.00 <b>(+223.83%)</b></td><td>681.72 <b>(+57.58%)</b></td><td>486.80 (+15.03%)</td><td>244.50 (-19.28%)</td><td>670.49 <b>(+495.68%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.30 (n/a)</td><td>432.62 (n/a)</td><td>423.20 (n/a)</td><td>302.90 (n/a)</td><td>112.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+29.16%)</b></td><td>0.02 <b>(+38.22%)</b></td><td>0.02 <b>(+79.89%)</b></td><td>0.01 (+2.06%)</td><td>0.01 <b>(+101.63%)</b></td><td>586.10 (-2.01%)</td><td>365.34 <b>(-22.08%)</b></td><td>268.30 <b>(-44.42%)</b></td><td>255.80 <b>(-22.58%)</b></td><td>147.27 <b>(+51.14%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.10 (n/a)</td><td>468.86 (n/a)</td><td>482.70 (n/a)</td><td>330.40 (n/a)</td><td>97.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+33.01%)</b></td><td>0.01 (+17.68%)</td><td>0.02 <b>(+30.71%)</b></td><td>0.01 (+10.06%)</td><td>0.01 <b>(+71.42%)</b></td><td>542.30 (-9.15%)</td><td>352.68 (-8.96%)</td><td>265.00 <b>(-23.50%)</b></td><td>216.10 <b>(-24.81%)</b></td><td>150.66 <b>(+20.10%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.90 (n/a)</td><td>387.40 (n/a)</td><td>346.40 (n/a)</td><td>287.40 (n/a)</td><td>125.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(+33.12%)</b></td><td>0.01 (+14.16%)</td><td>0.01 (+2.89%)</td><td>0.01 (+5.10%)</td><td>0.00 <b>(+73.58%)</b></td><td>606.60 (-4.85%)</td><td>468.20 (-9.14%)</td><td>478.00 (-2.81%)</td><td>277.60 <b>(-24.87%)</b></td><td>125.20 (+19.44%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>637.50 (n/a)</td><td>515.30 (n/a)</td><td>491.80 (n/a)</td><td>369.50 (n/a)</td><td>104.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 <b>(-34.20%)</b></td><td>0.01 <b>(-35.71%)</b></td><td>0.01 <b>(-37.64%)</b></td><td>0.00 <b>(-46.72%)</b></td><td>0.00 <b>(-27.63%)</b></td><td>999.10 <b>(+87.69%)</b></td><td>620.92 <b>(+59.82%)</b></td><td>551.90 <b>(+60.34%)</b></td><td>423.80 <b>(+51.95%)</b></td><td>221.07 <b>(+115.71%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.30 (n/a)</td><td>388.50 (n/a)</td><td>344.20 (n/a)</td><td>278.90 (n/a)</td><td>102.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (-4.74%)</td><td>0.01 <b>(+20.84%)</b></td><td>0.01 (+13.67%)</td><td>0.01 <b>(+184.96%)</b></td><td>0.00 <b>(-37.79%)</b></td><td>656.50 <b>(-64.91%)</b></td><td>469.60 <b>(-38.98%)</b></td><td>459.90 (-12.01%)</td><td>303.70 (+4.98%)</td><td>128.53 <b>(-79.57%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1870.70 (n/a)</td><td>769.58 (n/a)</td><td>522.70 (n/a)</td><td>289.30 (n/a)</td><td>629.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+19.74%)</td><td>0.01 (+1.36%)</td><td>0.01 (-6.78%)</td><td>0.01 (+4.70%)</td><td>0.00 <b>(+47.18%)</b></td><td>609.00 (-4.49%)</td><td>478.30 (+2.97%)</td><td>493.70 (+7.28%)</td><td>244.00 (-16.47%)</td><td>140.88 (+14.46%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>637.60 (n/a)</td><td>464.50 (n/a)</td><td>460.20 (n/a)</td><td>292.10 (n/a)</td><td>123.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (+17.98%)</td><td>0.01 (+1.58%)</td><td>0.01 (+10.09%)</td><td>0.00 <b>(-38.55%)</b></td><td>0.01 <b>(+33.46%)</b></td><td>1005.70 <b>(+62.71%)</b></td><td>493.36 (+11.98%)</td><td>340.00 (-9.16%)</td><td>248.90 (-15.22%)</td><td>306.77 <b>(+86.36%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.10 (n/a)</td><td>440.56 (n/a)</td><td>374.30 (n/a)</td><td>293.60 (n/a)</td><td>164.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (-15.45%)</td><td>0.01 <b>(-20.64%)</b></td><td>0.01 <b>(-29.47%)</b></td><td>0.01 (-8.09%)</td><td>0.00 <b>(-23.38%)</b></td><td>669.50 (+8.81%)</td><td>512.72 <b>(+20.82%)</b></td><td>527.80 <b>(+41.81%)</b></td><td>276.30 (+18.28%)</td><td>152.61 (-11.21%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>615.30 (n/a)</td><td>424.38 (n/a)</td><td>372.20 (n/a)</td><td>233.60 (n/a)</td><td>171.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (-9.95%)</td><td>0.03 <b>(+32.19%)</b></td><td>0.03 <b>(+52.71%)</b></td><td>0.02 <b>(+37.97%)</b></td><td>0.01 <b>(-33.53%)</b></td><td>498.00 <b>(-27.51%)</b></td><td>312.02 <b>(-30.59%)</b></td><td>280.90 <b>(-34.52%)</b></td><td>229.50 (+11.08%)</td><td>106.37 <b>(-38.94%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.00 (n/a)</td><td>449.52 (n/a)</td><td>429.00 (n/a)</td><td>206.60 (n/a)</td><td>174.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (+11.67%)</td><td>0.04 (-3.07%)</td><td>0.03 <b>(-20.58%)</b></td><td>0.02 (+0.19%)</td><td>0.01 <b>(+21.25%)</b></td><td>505.50 (-0.18%)</td><td>384.36 (+5.61%)</td><td>409.90 <b>(+25.93%)</b></td><td>240.70 (-10.45%)</td><td>122.09 (+12.38%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.40 (n/a)</td><td>363.94 (n/a)</td><td>325.50 (n/a)</td><td>268.80 (n/a)</td><td>108.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 <b>(+26.30%)</b></td><td>0.02 <b>(+26.06%)</b></td><td>0.02 <b>(-20.09%)</b></td><td>0.02 <b>(+254.04%)</b></td><td>0.01 (-7.05%)</td><td>518.30 <b>(-71.75%)</b></td><td>401.62 <b>(-42.38%)</b></td><td>471.20 <b>(+25.15%)</b></td><td>237.50 <b>(-20.81%)</b></td><td>126.35 <b>(-80.44%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1835.00 (n/a)</td><td>696.96 (n/a)</td><td>376.50 (n/a)</td><td>299.90 (n/a)</td><td>645.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 <b>(+80.47%)</b></td><td>0.03 <b>(+35.43%)</b></td><td>0.02 <b>(+21.48%)</b></td><td>0.02 <b>(+24.84%)</b></td><td>0.01 <b>(+193.31%)</b></td><td>582.50 (-19.90%)</td><td>446.84 (-19.81%)</td><td>449.40 (-17.68%)</td><td>232.60 <b>(-44.58%)</b></td><td>146.56 <b>(+31.38%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>727.20 (n/a)</td><td>557.22 (n/a)</td><td>545.90 (n/a)</td><td>419.70 (n/a)</td><td>111.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 <b>(+64.49%)</b></td><td>0.03 (-2.10%)</td><td>0.02 <b>(-33.58%)</b></td><td>0.01 <b>(-26.75%)</b></td><td>0.02 <b>(+157.28%)</b></td><td>642.00 <b>(+36.51%)</b></td><td>418.64 <b>(+24.57%)</b></td><td>432.20 <b>(+50.54%)</b></td><td>157.20 <b>(-39.21%)</b></td><td>197.10 <b>(+113.78%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.30 (n/a)</td><td>336.06 (n/a)</td><td>287.10 (n/a)</td><td>258.60 (n/a)</td><td>92.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 <b>(+47.31%)</b></td><td>0.03 <b>(+54.33%)</b></td><td>0.04 <b>(+113.78%)</b></td><td>0.01 (-5.62%)</td><td>0.02 <b>(+97.57%)</b></td><td>704.80 (+5.95%)</td><td>381.94 <b>(-24.53%)</b></td><td>256.70 <b>(-53.23%)</b></td><td>192.20 <b>(-32.11%)</b></td><td>220.25 <b>(+53.07%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.20 (n/a)</td><td>506.10 (n/a)</td><td>548.80 (n/a)</td><td>283.10 (n/a)</td><td>143.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (+17.23%)</td><td>0.02 <b>(+29.65%)</b></td><td>0.02 <b>(+23.76%)</b></td><td>0.01 (+7.59%)</td><td>0.01 <b>(+46.81%)</b></td><td>613.90 (-7.06%)</td><td>428.84 (-18.11%)</td><td>461.40 (-19.19%)</td><td>244.20 (-14.70%)</td><td>171.95 (+16.12%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.50 (n/a)</td><td>523.66 (n/a)</td><td>571.00 (n/a)</td><td>286.30 (n/a)</td><td>148.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 <b>(+29.80%)</b></td><td>0.02 (-17.57%)</td><td>0.02 <b>(-34.07%)</b></td><td>0.02 (-0.04%)</td><td>0.01 <b>(+56.91%)</b></td><td>601.60 (+0.05%)</td><td>448.36 <b>(+27.77%)</b></td><td>460.10 <b>(+51.65%)</b></td><td>204.90 <b>(-22.94%)</b></td><td>149.03 (+5.77%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.30 (n/a)</td><td>350.92 (n/a)</td><td>303.40 (n/a)</td><td>265.90 (n/a)</td><td>140.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(-32.33%)</b></td><td>0.02 (-14.43%)</td><td>0.02 (+1.12%)</td><td>0.02 (+3.62%)</td><td>0.00 <b>(-64.33%)</b></td><td>537.10 (-3.50%)</td><td>442.20 (+7.34%)</td><td>445.70 (-1.11%)</td><td>350.50 <b>(+47.77%)</b></td><td>68.76 <b>(-49.65%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.60 (n/a)</td><td>411.98 (n/a)</td><td>450.70 (n/a)</td><td>237.20 (n/a)</td><td>136.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 <b>(-45.86%)</b></td><td>0.01 <b>(-41.34%)</b></td><td>0.02 (-13.71%)</td><td>0.01 <b>(-62.15%)</b></td><td>0.01 <b>(-24.27%)</b></td><td>1355.70 <b>(+164.17%)</b></td><td>782.02 <b>(+86.55%)</b></td><td>546.70 (+15.88%)</td><td>509.90 <b>(+84.68%)</b></td><td>371.22 <b>(+248.74%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.20 (n/a)</td><td>419.20 (n/a)</td><td>471.80 (n/a)</td><td>276.10 (n/a)</td><td>106.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (-12.32%)</td><td>0.02 (-7.06%)</td><td>0.02 (+5.56%)</td><td>0.00 <b>(-71.24%)</b></td><td>0.01 (+18.64%)</td><td>1961.80 <b>(+247.65%)</b></td><td>716.26 <b>(+55.92%)</b></td><td>473.80 (-5.26%)</td><td>270.40 (+14.04%)</td><td>704.59 <b>(+452.43%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.30 (n/a)</td><td>459.38 (n/a)</td><td>500.10 (n/a)</td><td>237.10 (n/a)</td><td>127.54 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (+1.84%)</td><td>0.05 (-9.01%)</td><td>0.06 (-8.66%)</td><td>0.03 (+0.96%)</td><td>0.02 <b>(+20.78%)</b></td><td>485.90 (-0.96%)</td><td>348.80 (+13.01%)</td><td>288.20 (+9.46%)</td><td>238.90 (-1.81%)</td><td>123.04 (+18.75%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>490.60 (n/a)</td><td>308.64 (n/a)</td><td>263.30 (n/a)</td><td>243.30 (n/a)</td><td>103.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.11 (+6.09%)</td><td>0.05 (-0.87%)</td><td>0.04 (-0.82%)</td><td>0.01 <b>(-61.04%)</b></td><td>0.04 <b>(+42.73%)</b></td><td>1937.00 <b>(+156.69%)</b></td><td>826.82 <b>(+57.19%)</b></td><td>547.80 (+0.83%)</td><td>220.30 (-5.77%)</td><td>715.44 <b>(+260.90%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>754.60 (n/a)</td><td>526.00 (n/a)</td><td>543.30 (n/a)</td><td>233.80 (n/a)</td><td>198.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 <b>(-32.64%)</b></td><td>0.04 (-5.65%)</td><td>0.04 <b>(+20.06%)</b></td><td>0.03 (-10.95%)</td><td>0.01 <b>(-53.62%)</b></td><td>589.70 (+12.30%)</td><td>448.78 (+1.51%)</td><td>406.20 (-16.69%)</td><td>378.20 <b>(+48.43%)</b></td><td>87.68 (-19.02%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>525.10 (n/a)</td><td>442.12 (n/a)</td><td>487.60 (n/a)</td><td>254.80 (n/a)</td><td>108.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (+14.11%)</td><td>0.05 (-7.02%)</td><td>0.04 (+2.22%)</td><td>0.03 (-2.48%)</td><td>0.02 (+13.06%)</td><td>588.00 (+2.55%)</td><td>480.88 (+8.29%)</td><td>532.40 (-2.19%)</td><td>229.10 (-12.36%)</td><td>143.86 (-5.60%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>573.40 (n/a)</td><td>444.06 (n/a)</td><td>544.30 (n/a)</td><td>261.40 (n/a)</td><td>152.39 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-9.95%)</td><td>0.05 (-6.16%)</td><td>0.06 (-9.42%)</td><td>0.04 (+8.14%)</td><td>0.01 <b>(-26.57%)</b></td><td>466.40 (-7.52%)</td><td>357.78 (+2.30%)</td><td>294.20 (+10.44%)</td><td>271.50 (+11.09%)</td><td>97.96 <b>(-22.80%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>504.30 (n/a)</td><td>349.74 (n/a)</td><td>266.40 (n/a)</td><td>244.40 (n/a)</td><td>126.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 <b>(+23.16%)</b></td><td>0.05 (+11.97%)</td><td>0.04 (-1.79%)</td><td>0.04 <b>(+284.06%)</b></td><td>0.02 (-19.43%)</td><td>497.40 <b>(-73.96%)</b></td><td>420.84 <b>(-39.24%)</b></td><td>464.10 (+1.82%)</td><td>233.80 (-18.79%)</td><td>106.29 <b>(-84.54%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1910.50 (n/a)</td><td>692.64 (n/a)</td><td>455.80 (n/a)</td><td>287.90 (n/a)</td><td>687.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (+13.03%)</td><td>0.03 (+2.03%)</td><td>0.03 (-6.61%)</td><td>0.03 <b>(+26.65%)</b></td><td>0.01 (-2.21%)</td><td>597.30 <b>(-21.04%)</b></td><td>502.66 (-3.51%)</td><td>516.50 (+7.09%)</td><td>372.20 (-11.53%)</td><td>85.48 <b>(-36.38%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>756.50 (n/a)</td><td>520.94 (n/a)</td><td>482.30 (n/a)</td><td>420.70 (n/a)</td><td>134.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (-15.75%)</td><td>0.04 (-13.24%)</td><td>0.04 (+5.75%)</td><td>0.03 <b>(+24.42%)</b></td><td>0.02 <b>(-42.62%)</b></td><td>612.60 (-19.63%)</td><td>463.84 (-1.04%)</td><td>459.30 (-5.44%)</td><td>266.50 (+18.71%)</td><td>130.34 <b>(-44.32%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>762.20 (n/a)</td><td>468.72 (n/a)</td><td>485.70 (n/a)</td><td>224.50 (n/a)</td><td>234.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (-0.85%)</td><td>0.03 (-17.71%)</td><td>0.02 <b>(-26.64%)</b></td><td>0.02 <b>(-44.38%)</b></td><td>0.02 <b>(+24.51%)</b></td><td>1023.70 <b>(+79.79%)</b></td><td>644.90 <b>(+38.52%)</b></td><td>668.40 <b>(+36.30%)</b></td><td>244.50 (+0.87%)</td><td>284.51 <b>(+117.66%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>569.40 (n/a)</td><td>465.56 (n/a)</td><td>490.40 (n/a)</td><td>242.40 (n/a)</td><td>130.71 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 <b>(-37.19%)</b></td><td>0.05 (-13.30%)</td><td>0.04 (-2.54%)</td><td>0.04 (+18.01%)</td><td>0.01 <b>(-62.43%)</b></td><td>502.50 (-15.25%)</td><td>417.60 (+0.33%)</td><td>458.80 (+2.62%)</td><td>301.60 <b>(+59.16%)</b></td><td>84.80 <b>(-49.85%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>592.90 (n/a)</td><td>416.22 (n/a)</td><td>447.10 (n/a)</td><td>189.50 (n/a)</td><td>169.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (-15.79%)</td><td>0.04 (-15.86%)</td><td>0.03 <b>(-26.38%)</b></td><td>0.03 <b>(+34.02%)</b></td><td>0.01 <b>(-35.55%)</b></td><td>591.60 <b>(-25.39%)</b></td><td>480.56 (+8.43%)</td><td>501.00 <b>(+35.85%)</b></td><td>306.70 (+18.74%)</td><td>120.87 <b>(-43.32%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>792.90 (n/a)</td><td>443.20 (n/a)</td><td>368.80 (n/a)</td><td>258.30 (n/a)</td><td>213.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (+10.63%)</td><td>0.09 <b>(+28.49%)</b></td><td>0.10 <b>(+52.11%)</b></td><td>0.06 (-1.09%)</td><td>0.03 <b>(+38.23%)</b></td><td>580.80 (+1.11%)</td><td>400.56 (-18.15%)</td><td>341.50 <b>(-34.25%)</b></td><td>260.80 (-9.60%)</td><td>154.08 <b>(+32.01%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>574.40 (n/a)</td><td>489.38 (n/a)</td><td>519.40 (n/a)</td><td>288.50 (n/a)</td><td>116.72 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (+13.24%)</td><td>0.11 <b>(+55.95%)</b></td><td>0.12 <b>(+82.33%)</b></td><td>0.07 <b>(+316.06%)</b></td><td>0.03 (-19.62%)</td><td>458.80 <b>(-75.97%)</b></td><td>323.60 <b>(-55.17%)</b></td><td>263.10 <b>(-45.14%)</b></td><td>226.20 (-11.68%)</td><td>102.83 <b>(-84.68%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1908.90 (n/a)</td><td>721.80 (n/a)</td><td>479.60 (n/a)</td><td>256.10 (n/a)</td><td>671.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 (+0.52%)</td><td>0.13 <b>(+25.24%)</b></td><td>0.12 <b>(+28.93%)</b></td><td>0.07 (-2.80%)</td><td>0.04 (+6.32%)</td><td>572.10 (+2.90%)</td><td>354.66 (-18.99%)</td><td>346.20 <b>(-22.45%)</b></td><td>240.80 (-0.54%)</td><td>134.02 (+13.17%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>556.00 (n/a)</td><td>437.78 (n/a)</td><td>446.40 (n/a)</td><td>242.10 (n/a)</td><td>118.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (+0.74%)</td><td>0.09 (+11.23%)</td><td>0.09 <b>(+44.79%)</b></td><td>0.05 (+7.03%)</td><td>0.03 (-8.58%)</td><td>617.70 (-6.58%)</td><td>411.22 (-12.68%)</td><td>383.80 <b>(-30.93%)</b></td><td>272.60 (-0.73%)</td><td>149.20 (-14.95%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>661.20 (n/a)</td><td>470.92 (n/a)</td><td>555.70 (n/a)</td><td>274.60 (n/a)</td><td>175.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (-18.07%)</td><td>0.11 (+19.47%)</td><td>0.11 <b>(+52.24%)</b></td><td>0.08 <b>(+34.39%)</b></td><td>0.02 <b>(-39.56%)</b></td><td>519.30 <b>(-25.58%)</b></td><td>403.92 <b>(-21.85%)</b></td><td>356.40 <b>(-34.32%)</b></td><td>315.10 <b>(+22.04%)</b></td><td>97.76 <b>(-38.73%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>697.80 (n/a)</td><td>516.84 (n/a)</td><td>542.60 (n/a)</td><td>258.20 (n/a)</td><td>159.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 <b>(+38.12%)</b></td><td>0.10 <b>(+42.91%)</b></td><td>0.09 (+16.79%)</td><td>0.08 <b>(+348.93%)</b></td><td>0.02 <b>(-27.47%)</b></td><td>431.10 <b>(-77.72%)</b></td><td>353.80 <b>(-50.87%)</b></td><td>371.50 (-14.38%)</td><td>255.20 <b>(-27.60%)</b></td><td>72.01 <b>(-89.43%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1935.30 (n/a)</td><td>720.08 (n/a)</td><td>433.90 (n/a)</td><td>352.50 (n/a)</td><td>681.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 <b>(-25.13%)</b></td><td>0.08 <b>(-23.31%)</b></td><td>0.07 <b>(-31.97%)</b></td><td>0.07 (+1.04%)</td><td>0.03 <b>(-41.73%)</b></td><td>560.50 (-1.04%)</td><td>469.18 <b>(+20.48%)</b></td><td>506.20 <b>(+47.02%)</b></td><td>284.00 <b>(+33.58%)</b></td><td>109.30 <b>(-30.54%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>566.40 (n/a)</td><td>389.44 (n/a)</td><td>344.30 (n/a)</td><td>212.60 (n/a)</td><td>157.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.11 (+3.23%)</td><td>0.08 (+18.18%)</td><td>0.08 (+13.22%)</td><td>0.06 <b>(+29.09%)</b></td><td>0.02 (-18.11%)</td><td>548.00 <b>(-22.54%)</b></td><td>413.08 (-18.19%)</td><td>419.40 (-11.67%)</td><td>307.70 (-3.12%)</td><td>90.41 <b>(-38.02%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>707.50 (n/a)</td><td>504.92 (n/a)</td><td>474.80 (n/a)</td><td>317.60 (n/a)</td><td>145.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (+8.36%)</td><td>0.08 (+11.51%)</td><td>0.07 (-5.55%)</td><td>0.06 <b>(+206.65%)</b></td><td>0.03 <b>(-24.14%)</b></td><td>610.90 <b>(-67.39%)</b></td><td>481.76 <b>(-34.25%)</b></td><td>507.90 (+5.88%)</td><td>285.50 (-7.72%)</td><td>139.79 <b>(-78.44%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1873.20 (n/a)</td><td>732.72 (n/a)</td><td>479.70 (n/a)</td><td>309.40 (n/a)</td><td>648.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 <b>(-23.29%)</b></td><td>0.07 (-12.80%)</td><td>0.07 (-8.03%)</td><td>0.05 (+1.14%)</td><td>0.01 <b>(-42.73%)</b></td><td>620.60 (-1.12%)</td><td>504.24 (+11.03%)</td><td>473.30 (+8.73%)</td><td>397.70 <b>(+30.35%)</b></td><td>91.37 <b>(-24.96%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>627.60 (n/a)</td><td>454.16 (n/a)</td><td>435.30 (n/a)</td><td>305.10 (n/a)</td><td>121.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (+1.29%)</td><td>0.05 <b>(-21.45%)</b></td><td>0.05 <b>(-31.50%)</b></td><td>0.04 <b>(-46.58%)</b></td><td>0.02 <b>(+599.30%)</b></td><td>575.70 <b>(+87.16%)</b></td><td>405.14 <b>(+37.24%)</b></td><td>435.60 <b>(+45.98%)</b></td><td>278.20 (-1.28%)</td><td>123.57 <b>(+1129.08%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>307.60 (n/a)</td><td>295.20 (n/a)</td><td>298.40 (n/a)</td><td>281.80 (n/a)</td><td>10.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-10.03%)</td><td>0.05 (-15.39%)</td><td>0.05 <b>(-24.71%)</b></td><td>0.03 (-6.75%)</td><td>0.01 (-18.10%)</td><td>633.60 (+7.24%)</td><td>456.20 (+16.59%)</td><td>412.40 <b>(+32.82%)</b></td><td>323.10 (+11.15%)</td><td>135.68 (+1.41%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.80 (n/a)</td><td>391.28 (n/a)</td><td>310.50 (n/a)</td><td>290.70 (n/a)</td><td>133.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (-12.50%)</td><td>0.06 (-10.04%)</td><td>0.05 <b>(-21.53%)</b></td><td>0.04 (-2.39%)</td><td>0.02 <b>(-22.31%)</b></td><td>527.90 (+2.45%)</td><td>387.68 (+8.25%)</td><td>373.90 <b>(+27.44%)</b></td><td>271.10 (+14.29%)</td><td>105.60 (-12.10%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>515.30 (n/a)</td><td>358.14 (n/a)</td><td>293.40 (n/a)</td><td>237.20 (n/a)</td><td>120.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (-11.09%)</td><td>0.04 <b>(-39.63%)</b></td><td>0.04 <b>(-46.65%)</b></td><td>0.01 <b>(-73.69%)</b></td><td>0.02 <b>(+32.80%)</b></td><td>1968.40 <b>(+280.15%)</b></td><td>775.18 <b>(+132.42%)</b></td><td>541.60 <b>(+87.40%)</b></td><td>270.60 (+12.47%)</td><td>678.15 <b>(+514.22%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>517.80 (n/a)</td><td>333.52 (n/a)</td><td>289.00 (n/a)</td><td>240.60 (n/a)</td><td>110.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 <b>(-27.28%)</b></td><td>0.05 (-11.95%)</td><td>0.04 (-4.48%)</td><td>0.04 (+18.40%)</td><td>0.01 <b>(-59.34%)</b></td><td>537.10 (-15.54%)</td><td>463.46 (+1.08%)</td><td>493.90 (+4.71%)</td><td>340.30 <b>(+37.49%)</b></td><td>82.39 <b>(-54.57%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>635.90 (n/a)</td><td>458.50 (n/a)</td><td>471.70 (n/a)</td><td>247.50 (n/a)</td><td>181.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (-9.26%)</td><td>0.06 (-5.17%)</td><td>0.05 (-12.35%)</td><td>0.04 (+4.83%)</td><td>0.02 (-11.03%)</td><td>551.20 (-4.62%)</td><td>394.68 (+3.69%)</td><td>422.10 (+14.08%)</td><td>268.30 (+10.23%)</td><td>119.19 (-10.10%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.90 (n/a)</td><td>380.62 (n/a)</td><td>370.00 (n/a)</td><td>243.40 (n/a)</td><td>132.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (-12.18%)</td><td>0.06 (-11.36%)</td><td>0.05 <b>(-32.72%)</b></td><td>0.05 <b>(+25.85%)</b></td><td>0.02 <b>(-32.40%)</b></td><td>521.30 <b>(-20.53%)</b></td><td>407.90 (+4.41%)</td><td>450.10 <b>(+48.65%)</b></td><td>288.50 (+13.90%)</td><td>106.24 <b>(-39.06%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>656.00 (n/a)</td><td>390.66 (n/a)</td><td>302.80 (n/a)</td><td>253.30 (n/a)</td><td>174.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 <b>(+24.53%)</b></td><td>0.07 <b>(+32.19%)</b></td><td>0.08 <b>(+55.37%)</b></td><td>0.04 <b>(+52.31%)</b></td><td>0.02 (+9.17%)</td><td>555.10 <b>(-34.35%)</b></td><td>367.68 <b>(-27.66%)</b></td><td>301.70 <b>(-35.64%)</b></td><td>240.10 (-19.67%)</td><td>135.11 <b>(-39.57%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>845.50 (n/a)</td><td>508.28 (n/a)</td><td>468.80 (n/a)</td><td>298.90 (n/a)</td><td>223.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (+5.13%)</td><td>0.07 (+11.45%)</td><td>0.09 <b>(+64.52%)</b></td><td>0.04 (-10.70%)</td><td>0.02 (+17.76%)</td><td>595.80 (+11.99%)</td><td>372.44 (-6.96%)</td><td>274.60 <b>(-39.22%)</b></td><td>261.20 (-4.88%)</td><td>150.28 <b>(+28.02%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>532.00 (n/a)</td><td>400.32 (n/a)</td><td>451.80 (n/a)</td><td>274.60 (n/a)</td><td>117.39 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 <b>(-30.39%)</b></td><td>0.04 (-2.08%)</td><td>0.04 (-0.35%)</td><td>0.01 (+7.28%)</td><td>0.02 <b>(-36.16%)</b></td><td>1914.40 (-6.79%)</td><td>806.74 (-10.96%)</td><td>552.10 (+0.36%)</td><td>427.50 <b>(+43.65%)</b></td><td>625.56 (-11.31%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2053.80 (n/a)</td><td>906.08 (n/a)</td><td>550.10 (n/a)</td><td>297.60 (n/a)</td><td>705.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (-1.25%)</td><td>0.06 (-15.35%)</td><td>0.05 <b>(-27.03%)</b></td><td>0.04 <b>(+24.00%)</b></td><td>0.02 <b>(-23.24%)</b></td><td>582.80 (-19.36%)</td><td>441.58 (+8.51%)</td><td>454.00 <b>(+37.04%)</b></td><td>247.30 (+1.27%)</td><td>124.48 <b>(-38.39%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>722.70 (n/a)</td><td>406.96 (n/a)</td><td>331.30 (n/a)</td><td>244.20 (n/a)</td><td>202.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (+1.93%)</td><td>0.06 <b>(-29.09%)</b></td><td>0.05 <b>(-34.52%)</b></td><td>0.03 <b>(-51.57%)</b></td><td>0.03 <b>(+71.64%)</b></td><td>888.80 <b>(+106.46%)</b></td><td>508.78 <b>(+60.58%)</b></td><td>458.10 <b>(+52.75%)</b></td><td>248.70 (-1.89%)</td><td>233.94 <b>(+240.13%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>430.50 (n/a)</td><td>316.84 (n/a)</td><td>299.90 (n/a)</td><td>253.50 (n/a)</td><td>68.78 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (+3.78%)</td><td>0.06 (+7.25%)</td><td>0.06 (+2.07%)</td><td>0.03 (+14.41%)</td><td>0.02 (+10.84%)</td><td>567.60 (-12.60%)</td><td>363.12 (-6.63%)</td><td>292.50 (-2.04%)</td><td>237.50 (-3.61%)</td><td>149.60 (-10.03%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>649.40 (n/a)</td><td>388.90 (n/a)</td><td>298.60 (n/a)</td><td>246.40 (n/a)</td><td>166.28 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (+12.68%)</td><td>0.06 (+3.45%)</td><td>0.06 (+1.61%)</td><td>0.04 (+19.22%)</td><td>0.02 (+0.09%)</td><td>523.00 (-16.12%)</td><td>340.74 (-5.68%)</td><td>297.20 (-1.59%)</td><td>242.30 (-11.25%)</td><td>108.55 <b>(-26.33%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.50 (n/a)</td><td>361.26 (n/a)</td><td>302.00 (n/a)</td><td>273.00 (n/a)</td><td>147.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (+12.87%)</td><td>0.06 <b>(+26.34%)</b></td><td>0.06 <b>(+64.08%)</b></td><td>0.04 <b>(+42.93%)</b></td><td>0.01 <b>(-29.79%)</b></td><td>410.50 <b>(-30.03%)</b></td><td>335.50 <b>(-26.14%)</b></td><td>320.20 <b>(-39.06%)</b></td><td>252.10 (-11.39%)</td><td>67.69 <b>(-54.85%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.70 (n/a)</td><td>454.24 (n/a)</td><td>525.40 (n/a)</td><td>284.50 (n/a)</td><td>149.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (+7.53%)</td><td>0.05 (-7.61%)</td><td>0.05 (-19.67%)</td><td>0.04 (+9.96%)</td><td>0.01 (+10.77%)</td><td>511.40 (-9.05%)</td><td>382.86 (+8.16%)</td><td>376.30 <b>(+24.48%)</b></td><td>273.70 (-7.00%)</td><td>105.13 (-9.84%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>562.30 (n/a)</td><td>353.96 (n/a)</td><td>302.30 (n/a)</td><td>294.30 (n/a)</td><td>116.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (+4.71%)</td><td>0.05 (-3.81%)</td><td>0.04 <b>(-33.44%)</b></td><td>0.03 (+19.14%)</td><td>0.02 (-11.54%)</td><td>566.80 (-16.05%)</td><td>416.04 (-1.00%)</td><td>461.10 <b>(+50.24%)</b></td><td>262.30 (-4.48%)</td><td>128.23 <b>(-29.60%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>675.20 (n/a)</td><td>420.26 (n/a)</td><td>306.90 (n/a)</td><td>274.60 (n/a)</td><td>182.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (-2.90%)</td><td>0.05 (-9.09%)</td><td>0.04 (-11.92%)</td><td>0.04 (+1.08%)</td><td>0.01 (-19.15%)</td><td>500.50 (-1.07%)</td><td>413.08 (+8.47%)</td><td>416.70 (+13.54%)</td><td>303.60 (+2.99%)</td><td>76.50 (-15.89%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>505.90 (n/a)</td><td>380.84 (n/a)</td><td>367.00 (n/a)</td><td>294.80 (n/a)</td><td>90.95 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.33 (-2.64%)</td><td>0.27 (+10.30%)</td><td>0.25 (+15.48%)</td><td>0.22 <b>(+34.42%)</b></td><td>0.05 <b>(-42.49%)</b></td><td>439.90 <b>(-25.62%)</b></td><td>367.26 (-14.91%)</td><td>385.80 (-13.42%)</td><td>298.00 (+2.72%)</td><td>61.54 <b>(-55.08%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>591.40 (n/a)</td><td>431.60 (n/a)</td><td>445.60 (n/a)</td><td>290.10 (n/a)</td><td>137.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.47 (+19.43%)</td><td>0.32 (+15.27%)</td><td>0.36 (+8.63%)</td><td>0.18 <b>(+236.05%)</b></td><td>0.13 (-14.52%)</td><td>559.80 <b>(-70.24%)</b></td><td>360.54 <b>(-43.25%)</b></td><td>270.60 (-7.96%)</td><td>207.00 (-16.26%)</td><td>158.36 <b>(-77.52%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>1881.30 (n/a)</td><td>635.32 (n/a)</td><td>294.00 (n/a)</td><td>247.20 (n/a)</td><td>704.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.21 <b>(-41.87%)</b></td><td>0.16 <b>(-33.80%)</b></td><td>0.19 (-11.98%)</td><td>0.05 <b>(-72.90%)</b></td><td>0.06 (-15.73%)</td><td>2051.80 <b>(+268.96%)</b></td><td>828.46 <b>(+90.69%)</b></td><td>520.40 (+13.62%)</td><td>471.20 <b>(+72.03%)</b></td><td>684.94 <b>(+467.86%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>556.10 (n/a)</td><td>434.46 (n/a)</td><td>458.00 (n/a)</td><td>273.90 (n/a)</td><td>120.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.26 (-5.91%)</td><td>0.16 (+1.00%)</td><td>0.19 <b>(+40.88%)</b></td><td>0.04 (+0.08%)</td><td>0.08 (-14.58%)</td><td>1930.30 (-0.08%)</td><td>709.88 (-4.26%)</td><td>387.90 <b>(-29.01%)</b></td><td>282.10 (+6.29%)</td><td>689.55 (+0.65%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1931.80 (n/a)</td><td>741.48 (n/a)</td><td>546.40 (n/a)</td><td>265.40 (n/a)</td><td>685.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.30 (+0.78%)</td><td>0.19 (-13.79%)</td><td>0.20 <b>(-23.18%)</b></td><td>0.10 (-9.93%)</td><td>0.08 (-6.51%)</td><td>754.70 (+11.02%)</td><td>462.48 (+15.67%)</td><td>362.20 <b>(+30.19%)</b></td><td>244.80 (-0.77%)</td><td>209.25 (+8.40%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>679.80 (n/a)</td><td>399.82 (n/a)</td><td>278.20 (n/a)</td><td>246.70 (n/a)</td><td>193.04 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.28 (+2.48%)</td><td>0.18 (-2.86%)</td><td>0.16 (-1.75%)</td><td>0.14 (+12.98%)</td><td>0.06 (+1.28%)</td><td>513.40 (-11.48%)</td><td>439.38 (+2.21%)</td><td>463.20 (+1.78%)</td><td>260.60 (-2.40%)</td><td>102.32 (-13.74%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>580.00 (n/a)</td><td>429.88 (n/a)</td><td>455.10 (n/a)</td><td>267.00 (n/a)</td><td>118.63 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.19 <b>(+49.76%)</b></td><td>0.09 <b>(-20.25%)</b></td><td>0.06 <b>(-47.59%)</b></td><td>0.06 <b>(-26.95%)</b></td><td>0.06 <b>(+169.81%)</b></td><td>670.20 <b>(+36.89%)</b></td><td>509.02 <b>(+47.31%)</b></td><td>591.20 <b>(+90.83%)</b></td><td>198.10 <b>(-33.21%)</b></td><td>185.93 <b>(+126.91%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>489.60 (n/a)</td><td>345.54 (n/a)</td><td>309.80 (n/a)</td><td>296.60 (n/a)</td><td>81.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (+6.01%)</td><td>0.09 (-11.78%)</td><td>0.09 (-5.69%)</td><td>0.06 <b>(-25.43%)</b></td><td>0.03 <b>(+38.49%)</b></td><td>657.20 <b>(+34.10%)</b></td><td>463.88 (+18.65%)</td><td>432.20 (+6.04%)</td><td>289.10 (-5.68%)</td><td>141.98 <b>(+81.29%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>490.10 (n/a)</td><td>390.98 (n/a)</td><td>407.60 (n/a)</td><td>306.50 (n/a)</td><td>78.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.18 (+12.61%)</td><td>0.13 (+14.03%)</td><td>0.14 (+8.95%)</td><td>0.05 <b>(+226.83%)</b></td><td>0.05 (-13.76%)</td><td>745.60 <b>(-69.41%)</b></td><td>351.94 <b>(-50.06%)</b></td><td>265.20 (-8.24%)</td><td>207.60 (-11.21%)</td><td>222.39 <b>(-77.04%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2437.00 (n/a)</td><td>704.78 (n/a)</td><td>289.00 (n/a)</td><td>233.80 (n/a)</td><td>968.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (-10.71%)</td><td>0.09 (-18.69%)</td><td>0.08 (-19.56%)</td><td>0.07 (-0.27%)</td><td>0.03 (-17.86%)</td><td>536.50 (+0.26%)</td><td>454.58 <b>(+20.35%)</b></td><td>490.00 <b>(+24.33%)</b></td><td>263.80 (+11.97%)</td><td>108.60 (-10.60%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>535.10 (n/a)</td><td>377.72 (n/a)</td><td>394.10 (n/a)</td><td>235.60 (n/a)</td><td>121.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (+6.57%)</td><td>0.10 (+0.60%)</td><td>0.12 (+11.91%)</td><td>0.06 (-14.72%)</td><td>0.04 <b>(+59.14%)</b></td><td>618.30 (+17.26%)</td><td>416.36 (+8.17%)</td><td>315.00 (-10.66%)</td><td>264.10 (-6.15%)</td><td>174.18 <b>(+80.92%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>527.30 (n/a)</td><td>384.90 (n/a)</td><td>352.60 (n/a)</td><td>281.40 (n/a)</td><td>96.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (-16.34%)</td><td>0.08 (-7.38%)</td><td>0.08 (-7.13%)</td><td>0.06 <b>(+54.44%)</b></td><td>0.02 <b>(-35.17%)</b></td><td>648.40 <b>(-35.26%)</b></td><td>499.18 (-3.41%)</td><td>486.80 (+7.68%)</td><td>362.00 (+19.55%)</td><td>132.57 <b>(-52.67%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>1001.50 (n/a)</td><td>516.82 (n/a)</td><td>452.10 (n/a)</td><td>302.80 (n/a)</td><td>280.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 (+9.26%)</td><td>0.12 (+10.79%)</td><td>0.14 <b>(+32.60%)</b></td><td>0.06 (+14.02%)</td><td>0.05 (+6.36%)</td><td>741.90 (-12.29%)</td><td>411.00 (-10.41%)</td><td>289.40 <b>(-24.60%)</b></td><td>237.40 (-8.48%)</td><td>212.10 (-11.96%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>845.90 (n/a)</td><td>458.78 (n/a)</td><td>383.80 (n/a)</td><td>259.40 (n/a)</td><td>240.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 <b>(-22.13%)</b></td><td>0.10 (-18.40%)</td><td>0.10 <b>(-27.73%)</b></td><td>0.07 (-10.93%)</td><td>0.02 <b>(-40.32%)</b></td><td>565.10 (+12.26%)</td><td>430.76 (+17.33%)</td><td>429.10 <b>(+38.37%)</b></td><td>299.90 <b>(+28.44%)</b></td><td>93.78 <b>(-20.53%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>503.40 (n/a)</td><td>367.12 (n/a)</td><td>310.10 (n/a)</td><td>233.50 (n/a)</td><td>118.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 (+19.22%)</td><td>0.10 (-5.73%)</td><td>0.09 (-2.58%)</td><td>0.07 (-1.89%)</td><td>0.04 <b>(+23.14%)</b></td><td>586.20 (+1.93%)</td><td>453.54 (+8.18%)</td><td>476.50 (+2.65%)</td><td>234.90 (-16.14%)</td><td>131.55 (+2.82%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>575.10 (n/a)</td><td>419.24 (n/a)</td><td>464.20 (n/a)</td><td>280.10 (n/a)</td><td>127.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (-7.33%)</td><td>0.11 (+2.85%)</td><td>0.12 <b>(+32.15%)</b></td><td>0.07 (-0.88%)</td><td>0.03 (-15.01%)</td><td>573.60 (+0.88%)</td><td>406.24 (-4.76%)</td><td>350.30 <b>(-24.34%)</b></td><td>276.90 (+7.91%)</td><td>135.12 (-6.27%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>568.60 (n/a)</td><td>426.54 (n/a)</td><td>463.00 (n/a)</td><td>256.60 (n/a)</td><td>144.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.16 (-0.96%)</td><td>0.10 (-11.05%)</td><td>0.09 <b>(-26.48%)</b></td><td>0.06 <b>(+61.50%)</b></td><td>0.04 (-10.33%)</td><td>690.60 <b>(-38.08%)</b></td><td>473.32 (-1.87%)</td><td>473.70 <b>(+36.00%)</b></td><td>250.20 (+0.97%)</td><td>182.09 <b>(-49.15%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1115.30 (n/a)</td><td>482.32 (n/a)</td><td>348.30 (n/a)</td><td>247.80 (n/a)</td><td>358.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 <b>(+30.76%)</b></td><td>0.12 <b>(+40.90%)</b></td><td>0.10 (+10.63%)</td><td>0.09 <b>(+306.92%)</b></td><td>0.04 (-9.04%)</td><td>466.40 <b>(-75.43%)</b></td><td>376.82 <b>(-48.17%)</b></td><td>423.90 (-9.60%)</td><td>238.30 <b>(-23.55%)</b></td><td>97.80 <b>(-85.15%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1897.90 (n/a)</td><td>727.08 (n/a)</td><td>468.90 (n/a)</td><td>311.70 (n/a)</td><td>658.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (-0.51%)</td><td>0.09 (-7.47%)</td><td>0.08 (-5.78%)</td><td>0.05 <b>(-22.29%)</b></td><td>0.04 (+10.46%)</td><td>680.40 <b>(+28.69%)</b></td><td>436.60 (+13.03%)</td><td>435.20 (+6.12%)</td><td>238.60 (+0.51%)</td><td>174.59 <b>(+42.14%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>528.70 (n/a)</td><td>386.28 (n/a)</td><td>410.10 (n/a)</td><td>237.40 (n/a)</td><td>122.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 <b>(+27.20%)</b></td><td>0.09 (+1.45%)</td><td>0.07 (-5.99%)</td><td>0.06 (-19.76%)</td><td>0.04 <b>(+68.87%)</b></td><td>617.70 <b>(+24.64%)</b></td><td>435.20 (+7.33%)</td><td>496.40 (+6.36%)</td><td>228.70 <b>(-21.38%)</b></td><td>162.66 <b>(+65.44%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>495.60 (n/a)</td><td>405.48 (n/a)</td><td>466.70 (n/a)</td><td>290.90 (n/a)</td><td>98.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (+0.12%)</td><td>0.11 (-4.26%)</td><td>0.13 (+10.26%)</td><td>0.05 <b>(-33.38%)</b></td><td>0.04 <b>(+60.67%)</b></td><td>638.00 <b>(+50.12%)</b></td><td>382.04 (+17.15%)</td><td>272.90 (-9.31%)</td><td>233.30 (-0.13%)</td><td>180.28 <b>(+136.85%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>425.00 (n/a)</td><td>326.12 (n/a)</td><td>300.90 (n/a)</td><td>233.60 (n/a)</td><td>76.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (+14.45%)</td><td>0.10 (+16.08%)</td><td>0.09 (+17.67%)</td><td>0.07 (+17.89%)</td><td>0.03 (-0.39%)</td><td>512.30 (-15.18%)</td><td>369.56 (-16.41%)</td><td>398.50 (-15.01%)</td><td>230.60 (-12.62%)</td><td>109.73 <b>(-27.87%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>604.00 (n/a)</td><td>442.10 (n/a)</td><td>468.90 (n/a)</td><td>263.90 (n/a)</td><td>152.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (+7.36%)</td><td>0.09 (-9.32%)</td><td>0.08 (-14.21%)</td><td>0.05 <b>(-29.42%)</b></td><td>0.03 <b>(+58.83%)</b></td><td>678.30 <b>(+41.70%)</b></td><td>443.20 (+19.23%)</td><td>453.80 (+16.57%)</td><td>265.20 (-6.88%)</td><td>165.85 <b>(+109.04%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>478.70 (n/a)</td><td>371.72 (n/a)</td><td>389.30 (n/a)</td><td>284.80 (n/a)</td><td>79.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 <b>(-38.96%)</b></td><td>0.07 <b>(-26.74%)</b></td><td>0.07 <b>(-35.71%)</b></td><td>0.05 (+5.99%)</td><td>0.01 <b>(-67.89%)</b></td><td>666.00 (-5.65%)</td><td>523.84 <b>(+21.61%)</b></td><td>506.70 <b>(+55.57%)</b></td><td>418.60 <b>(+63.84%)</b></td><td>92.45 <b>(-50.96%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>705.90 (n/a)</td><td>430.74 (n/a)</td><td>325.70 (n/a)</td><td>255.50 (n/a)</td><td>188.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.41 (-18.34%)</td><td>0.31 (+7.86%)</td><td>0.27 (+16.32%)</td><td>0.22 (+4.08%)</td><td>0.09 <b>(-32.02%)</b></td><td>600.80 (-3.92%)</td><td>451.00 (-11.69%)</td><td>483.50 (-14.03%)</td><td>316.80 <b>(+22.46%)</b></td><td>119.97 <b>(-21.31%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.51 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>625.30 (n/a)</td><td>510.72 (n/a)</td><td>562.40 (n/a)</td><td>258.70 (n/a)</td><td>152.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.42 <b>(-21.90%)</b></td><td>0.28 (-19.64%)</td><td>0.25 (-14.53%)</td><td>0.24 (-10.50%)</td><td>0.08 <b>(-32.81%)</b></td><td>551.00 (+11.72%)</td><td>484.32 <b>(+21.37%)</b></td><td>531.00 (+17.01%)</td><td>313.60 <b>(+28.05%)</b></td><td>98.90 (-6.49%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.54 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>493.20 (n/a)</td><td>399.04 (n/a)</td><td>453.80 (n/a)</td><td>244.90 (n/a)</td><td>105.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.39 (-7.57%)</td><td>0.34 <b>(+29.76%)</b></td><td>0.34 <b>(+26.05%)</b></td><td>0.27 <b>(+111.91%)</b></td><td>0.05 <b>(-59.47%)</b></td><td>484.30 <b>(-52.81%)</b></td><td>393.22 <b>(-38.65%)</b></td><td>381.80 <b>(-20.67%)</b></td><td>332.50 (+8.20%)</td><td>65.54 <b>(-81.59%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.43 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>1026.20 (n/a)</td><td>640.98 (n/a)</td><td>481.30 (n/a)</td><td>307.30 (n/a)</td><td>356.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+66.67%)</b></td><td>0.00 <b>(+250.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+22.47%)</b></td><td>19441.00 (+5.38%)</td><td>11288.51 <b>(-27.03%)</b></td><td>5911.49 <b>(-65.91%)</b></td><td>5813.37 (-5.40%)</td><td>7441.85 <b>(+41.66%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18448.59 (n/a)</td><td>15470.64 (n/a)</td><td>17338.69 (n/a)</td><td>6145.00 (n/a)</td><td>5253.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.00 <b>(+160.00%)</b></td><td>0.00 <b>(+95.45%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(+590.41%)</b></td><td>17914.80 <b>(-22.29%)</b></td><td>11880.14 <b>(-39.03%)</b></td><td>10556.57 <b>(-42.20%)</b></td><td>6410.90 <b>(-61.51%)</b></td><td>5538.59 <b>(+81.75%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23053.21 (n/a)</td><td>19483.80 (n/a)</td><td>18263.09 (n/a)</td><td>16655.72 (n/a)</td><td>3047.37 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (-2.28%)</td><td>0.10 (+5.34%)</td><td>0.08 (-1.06%)</td><td>0.07 (-4.38%)</td><td>0.03 (+7.67%)</td><td>29140.57 (+4.65%)</td><td>22410.87 (-3.76%)</td><td>24918.50 (+1.15%)</td><td>15260.49 (+2.34%)</td><td>5869.30 (+19.89%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27846.86 (n/a)</td><td>23287.16 (n/a)</td><td>24635.63 (n/a)</td><td>14911.68 (n/a)</td><td>4895.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.52 (+13.70%)</td><td>2.16 <b>(+49.10%)</b></td><td>2.30 <b>(+73.24%)</b></td><td>1.36 <b>(+324.71%)</b></td><td>0.47 <b>(-37.20%)</b></td><td>768.80 <b>(-76.45%)</b></td><td>511.16 <b>(-56.18%)</b></td><td>455.50 <b>(-42.28%)</b></td><td>415.40 (-12.05%)</td><td>147.38 <b>(-87.54%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.22 (n/a)</td><td>1.45 (n/a)</td><td>1.33 (n/a)</td><td>0.32 (n/a)</td><td>0.75 (n/a)</td><td>3265.00 (n/a)</td><td>1166.56 (n/a)</td><td>789.10 (n/a)</td><td>472.30 (n/a)</td><td>1182.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.62 (+9.38%)</td><td>2.03 (+9.18%)</td><td>1.96 (+12.83%)</td><td>1.49 (-0.42%)</td><td>0.55 <b>(+49.27%)</b></td><td>704.00 (+0.43%)</td><td>547.24 (-5.59%)</td><td>533.80 (-11.36%)</td><td>400.40 (-8.56%)</td><td>148.00 <b>(+37.06%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.39 (n/a)</td><td>1.86 (n/a)</td><td>1.74 (n/a)</td><td>1.50 (n/a)</td><td>0.37 (n/a)</td><td>701.00 (n/a)</td><td>579.62 (n/a)</td><td>602.20 (n/a)</td><td>437.90 (n/a)</td><td>107.98 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.01 (-3.75%)</td><td>2.10 (-3.66%)</td><td>1.79 (+5.53%)</td><td>1.55 (+4.26%)</td><td>0.61 <b>(-22.99%)</b></td><td>678.10 (-4.09%)</td><td>529.36 (-0.06%)</td><td>587.30 (-5.24%)</td><td>348.00 (+3.91%)</td><td>135.26 <b>(-21.29%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.13 (n/a)</td><td>2.18 (n/a)</td><td>1.69 (n/a)</td><td>1.48 (n/a)</td><td>0.79 (n/a)</td><td>707.00 (n/a)</td><td>529.70 (n/a)</td><td>619.80 (n/a)</td><td>334.90 (n/a)</td><td>171.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.75 (+9.08%)</td><td>2.04 <b>(+23.26%)</b></td><td>1.94 <b>(+30.00%)</b></td><td>1.65 <b>(+47.87%)</b></td><td>0.45 (-14.27%)</td><td>634.40 <b>(-32.37%)</b></td><td>532.34 <b>(-21.70%)</b></td><td>539.20 <b>(-23.08%)</b></td><td>381.30 (-8.32%)</td><td>106.34 <b>(-44.02%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.52 (n/a)</td><td>1.66 (n/a)</td><td>1.50 (n/a)</td><td>1.12 (n/a)</td><td>0.53 (n/a)</td><td>938.00 (n/a)</td><td>679.88 (n/a)</td><td>701.00 (n/a)</td><td>415.90 (n/a)</td><td>189.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>4.09 (+6.45%)</td><td>2.33 (+2.12%)</td><td>2.96 <b>(+23.26%)</b></td><td>0.58 (-0.09%)</td><td>1.46 <b>(+23.97%)</b></td><td>3616.00 (+0.09%)</td><td>1503.48 (+8.98%)</td><td>707.50 (-18.87%)</td><td>513.20 (-6.06%)</td><td>1316.82 (+4.29%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.84 (n/a)</td><td>2.28 (n/a)</td><td>2.40 (n/a)</td><td>0.58 (n/a)</td><td>1.18 (n/a)</td><td>3612.70 (n/a)</td><td>1379.62 (n/a)</td><td>872.10 (n/a)</td><td>546.30 (n/a)</td><td>1262.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.67 <b>(+60.01%)</b></td><td>3.44 <b>(+52.10%)</b></td><td>3.76 <b>(+50.48%)</b></td><td>0.85 <b>(+30.46%)</b></td><td>1.77 <b>(+65.41%)</b></td><td>2465.20 <b>(-23.35%)</b></td><td>929.58 <b>(-28.72%)</b></td><td>557.30 <b>(-33.55%)</b></td><td>369.90 <b>(-37.51%)</b></td><td>868.53 (-19.85%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.54 (n/a)</td><td>2.26 (n/a)</td><td>2.50 (n/a)</td><td>0.65 (n/a)</td><td>1.07 (n/a)</td><td>3216.00 (n/a)</td><td>1304.12 (n/a)</td><td>838.70 (n/a)</td><td>591.90 (n/a)</td><td>1083.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.35 <b>(+40.55%)</b></td><td>3.92 <b>(+58.56%)</b></td><td>3.57 (+11.46%)</td><td>2.46 <b>(+313.08%)</b></td><td>1.35 (-10.69%)</td><td>853.70 <b>(-75.79%)</b></td><td>589.84 <b>(-59.09%)</b></td><td>587.50 (-10.28%)</td><td>392.10 <b>(-28.85%)</b></td><td>202.48 <b>(-84.38%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.81 (n/a)</td><td>2.47 (n/a)</td><td>3.20 (n/a)</td><td>0.59 (n/a)</td><td>1.51 (n/a)</td><td>3526.30 (n/a)</td><td>1441.92 (n/a)</td><td>654.80 (n/a)</td><td>551.10 (n/a)</td><td>1296.53 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.93 <b>(+74.93%)</b></td><td>2.97 (-14.73%)</td><td>2.05 <b>(-41.19%)</b></td><td>1.01 <b>(-66.30%)</b></td><td>2.31 <b>(+431.97%)</b></td><td>2083.10 <b>(+196.74%)</b></td><td>1038.86 <b>(+70.24%)</b></td><td>1024.10 <b>(+70.03%)</b></td><td>302.50 <b>(-42.83%)</b></td><td>656.71 <b>(+755.23%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.96 (n/a)</td><td>3.48 (n/a)</td><td>3.48 (n/a)</td><td>2.99 (n/a)</td><td>0.43 (n/a)</td><td>702.00 (n/a)</td><td>610.22 (n/a)</td><td>602.30 (n/a)</td><td>529.10 (n/a)</td><td>76.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.04 <b>(+21.64%)</b></td><td>3.80 (+3.87%)</td><td>3.55 (-1.82%)</td><td>1.67 <b>(-38.78%)</b></td><td>1.72 <b>(+93.91%)</b></td><td>1258.10 <b>(+63.37%)</b></td><td>673.30 (+12.24%)</td><td>591.30 (+1.84%)</td><td>347.00 (-17.79%)</td><td>360.92 <b>(+160.38%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>4.97 (n/a)</td><td>3.66 (n/a)</td><td>3.61 (n/a)</td><td>2.72 (n/a)</td><td>0.89 (n/a)</td><td>770.10 (n/a)</td><td>599.86 (n/a)</td><td>580.60 (n/a)</td><td>422.10 (n/a)</td><td>138.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>7.39 <b>(+111.05%)</b></td><td>3.45 <b>(+44.63%)</b></td><td>2.94 (+12.84%)</td><td>0.59 (-1.99%)</td><td>2.48 <b>(+131.31%)</b></td><td>3577.60 (+2.03%)</td><td>1186.08 (-8.99%)</td><td>712.60 (-11.38%)</td><td>283.80 <b>(-52.63%)</b></td><td>1350.58 (+9.37%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>3.50 (n/a)</td><td>2.39 (n/a)</td><td>2.61 (n/a)</td><td>0.60 (n/a)</td><td>1.07 (n/a)</td><td>3506.30 (n/a)</td><td>1303.18 (n/a)</td><td>804.10 (n/a)</td><td>599.10 (n/a)</td><td>1234.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.88 (+12.17%)</td><td>4.16 <b>(+32.23%)</b></td><td>4.23 (+5.27%)</td><td>1.68 <b>(+40.55%)</b></td><td>1.55 (-16.08%)</td><td>2493.00 <b>(-28.85%)</b></td><td>1214.52 <b>(-38.53%)</b></td><td>991.60 (-5.00%)</td><td>713.70 (-10.85%)</td><td>724.53 <b>(-48.15%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>5.24 (n/a)</td><td>3.15 (n/a)</td><td>4.02 (n/a)</td><td>1.20 (n/a)</td><td>1.84 (n/a)</td><td>3504.00 (n/a)</td><td>1975.86 (n/a)</td><td>1043.80 (n/a)</td><td>800.60 (n/a)</td><td>1397.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.02 <b>(-23.91%)</b></td><td>4.56 (-8.04%)</td><td>5.89 (+4.29%)</td><td>1.11 (-6.18%)</td><td>2.13 (-15.18%)</td><td>3769.30 (+6.59%)</td><td>1393.78 (+6.65%)</td><td>712.10 (-4.12%)</td><td>696.70 <b>(+31.43%)</b></td><td>1338.00 (+6.29%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>7.91 (n/a)</td><td>4.96 (n/a)</td><td>5.65 (n/a)</td><td>1.19 (n/a)</td><td>2.51 (n/a)</td><td>3536.30 (n/a)</td><td>1306.90 (n/a)</td><td>742.70 (n/a)</td><td>530.10 (n/a)</td><td>1258.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>8.83 (+17.25%)</td><td>5.28 (-3.03%)</td><td>5.76 (-4.75%)</td><td>1.09 (-16.64%)</td><td>2.90 <b>(+20.22%)</b></td><td>3846.40 (+19.96%)</td><td>1341.88 (+15.17%)</td><td>727.80 (+4.99%)</td><td>475.00 (-14.72%)</td><td>1414.31 <b>(+23.74%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>7.53 (n/a)</td><td>5.44 (n/a)</td><td>6.05 (n/a)</td><td>1.31 (n/a)</td><td>2.41 (n/a)</td><td>3206.30 (n/a)</td><td>1165.08 (n/a)</td><td>693.20 (n/a)</td><td>557.00 (n/a)</td><td>1142.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>8.89 (-2.24%)</td><td>7.43 (+15.69%)</td><td>7.33 (+7.08%)</td><td>6.48 <b>(+57.73%)</b></td><td>0.99 <b>(-53.61%)</b></td><td>647.50 <b>(-36.59%)</b></td><td>572.36 <b>(-20.37%)</b></td><td>572.40 (-6.62%)</td><td>471.80 (+2.28%)</td><td>72.86 <b>(-70.94%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>9.09 (n/a)</td><td>6.42 (n/a)</td><td>6.84 (n/a)</td><td>4.11 (n/a)</td><td>2.13 (n/a)</td><td>1021.20 (n/a)</td><td>718.78 (n/a)</td><td>613.00 (n/a)</td><td>461.30 (n/a)</td><td>250.72 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>9.65 <b>(+26.09%)</b></td><td>6.93 <b>(+33.32%)</b></td><td>7.65 <b>(+46.64%)</b></td><td>3.63 <b>(+108.05%)</b></td><td>2.83 (+17.71%)</td><td>1154.00 <b>(-51.94%)</b></td><td>711.68 <b>(-33.38%)</b></td><td>548.20 <b>(-31.80%)</b></td><td>434.60 <b>(-20.68%)</b></td><td>332.23 <b>(-56.74%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>7.65 (n/a)</td><td>5.20 (n/a)</td><td>5.22 (n/a)</td><td>1.75 (n/a)</td><td>2.41 (n/a)</td><td>2401.00 (n/a)</td><td>1068.26 (n/a)</td><td>803.80 (n/a)</td><td>547.90 (n/a)</td><td>767.92 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>8.09 (-19.38%)</td><td>4.43 <b>(-30.35%)</b></td><td>4.22 <b>(-38.09%)</b></td><td>1.17 (-1.29%)</td><td>3.06 (-4.50%)</td><td>3588.70 (+1.30%)</td><td>1624.10 <b>(+40.06%)</b></td><td>992.80 <b>(+61.51%)</b></td><td>518.10 <b>(+24.04%)</b></td><td>1335.88 (+0.08%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>10.04 (n/a)</td><td>6.35 (n/a)</td><td>6.82 (n/a)</td><td>1.18 (n/a)</td><td>3.21 (n/a)</td><td>3542.60 (n/a)</td><td>1159.54 (n/a)</td><td>614.70 (n/a)</td><td>417.70 (n/a)</td><td>1334.87 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>1.55 (-12.95%)</td><td>1.09 (+4.47%)</td><td>1.01 (-3.16%)</td><td>0.88 <b>(+303.57%)</b></td><td>0.27 <b>(-54.89%)</b></td><td>595.00 <b>(-75.22%)</b></td><td>500.24 <b>(-40.94%)</b></td><td>517.70 (+3.25%)</td><td>339.10 (+14.87%)</td><td>99.03 <b>(-88.74%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>1.78 (n/a)</td><td>1.04 (n/a)</td><td>1.05 (n/a)</td><td>0.22 (n/a)</td><td>0.59 (n/a)</td><td>2401.30 (n/a)</td><td>847.00 (n/a)</td><td>501.40 (n/a)</td><td>295.20 (n/a)</td><td>879.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.64 (+7.73%)</td><td>1.74 (+16.40%)</td><td>1.64 (-0.94%)</td><td>0.32 <b>(-41.05%)</b></td><td>0.96 <b>(+30.96%)</b></td><td>3318.10 <b>(+69.64%)</b></td><td>1092.34 (+18.52%)</td><td>639.00 (+0.95%)</td><td>397.00 (-7.18%)</td><td>1251.96 <b>(+103.47%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.45 (n/a)</td><td>1.49 (n/a)</td><td>1.66 (n/a)</td><td>0.54 (n/a)</td><td>0.73 (n/a)</td><td>1956.00 (n/a)</td><td>921.64 (n/a)</td><td>633.00 (n/a)</td><td>427.70 (n/a)</td><td>615.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.92 <b>(+31.48%)</b></td><td>2.49 <b>(+89.31%)</b></td><td>3.52 <b>(+254.86%)</b></td><td>0.56 (-6.47%)</td><td>1.76 <b>(+85.47%)</b></td><td>3739.40 (+6.92%)</td><td>1794.82 (-14.49%)</td><td>595.10 <b>(-71.82%)</b></td><td>535.00 <b>(-23.94%)</b></td><td>1695.50 <b>(+71.55%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>2.98 (n/a)</td><td>1.32 (n/a)</td><td>0.99 (n/a)</td><td>0.60 (n/a)</td><td>0.95 (n/a)</td><td>3497.40 (n/a)</td><td>2098.90 (n/a)</td><td>2111.80 (n/a)</td><td>703.40 (n/a)</td><td>988.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>1.13 <b>(-34.54%)</b></td><td>1.05 <b>(-20.75%)</b></td><td>1.04 <b>(-26.92%)</b></td><td>0.98 <b>(+27.52%)</b></td><td>0.06 <b>(-83.83%)</b></td><td>537.70 <b>(-21.57%)</b></td><td>502.46 (+17.31%)</td><td>506.10 <b>(+36.86%)</b></td><td>465.00 <b>(+52.76%)</b></td><td>27.13 <b>(-81.82%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>1.72 (n/a)</td><td>1.32 (n/a)</td><td>1.42 (n/a)</td><td>0.76 (n/a)</td><td>0.35 (n/a)</td><td>685.60 (n/a)</td><td>428.30 (n/a)</td><td>369.80 (n/a)</td><td>304.40 (n/a)</td><td>149.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 <b>(-31.64%)</b></td><td>0.11 <b>(+25.77%)</b></td><td>0.12 <b>(+72.62%)</b></td><td>0.06 <b>(+283.01%)</b></td><td>0.03 <b>(-56.94%)</b></td><td>514.30 <b>(-73.89%)</b></td><td>316.86 <b>(-54.54%)</b></td><td>276.40 <b>(-42.08%)</b></td><td>228.90 <b>(+46.26%)</b></td><td>115.32 <b>(-84.08%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>1969.70 (n/a)</td><td>696.96 (n/a)</td><td>477.20 (n/a)</td><td>156.50 (n/a)</td><td>724.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (+6.93%)</td><td>0.09 (+4.67%)</td><td>0.09 (+4.48%)</td><td>0.06 <b>(+21.35%)</b></td><td>0.03 (-12.62%)</td><td>546.70 (-17.59%)</td><td>394.64 (-8.81%)</td><td>376.20 (-4.30%)</td><td>249.90 (-6.47%)</td><td>112.07 <b>(-32.70%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>663.40 (n/a)</td><td>432.78 (n/a)</td><td>393.10 (n/a)</td><td>267.20 (n/a)</td><td>166.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.26 (+17.36%)</td><td>0.18 (+1.85%)</td><td>0.16 <b>(-22.61%)</b></td><td>0.12 (+7.48%)</td><td>0.06 (+9.69%)</td><td>557.70 (-6.96%)</td><td>392.96 (-2.13%)</td><td>399.30 <b>(+29.22%)</b></td><td>256.10 (-14.80%)</td><td>122.37 (-11.08%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>599.40 (n/a)</td><td>401.50 (n/a)</td><td>309.00 (n/a)</td><td>300.60 (n/a)</td><td>137.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.22 (-18.44%)</td><td>0.17 (-6.49%)</td><td>0.14 (-18.60%)</td><td>0.11 <b>(+39.97%)</b></td><td>0.05 <b>(-40.84%)</b></td><td>575.70 <b>(-28.56%)</b></td><td>424.36 (-8.23%)</td><td>470.20 <b>(+22.83%)</b></td><td>293.20 <b>(+22.63%)</b></td><td>125.34 <b>(-49.64%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>805.80 (n/a)</td><td>462.40 (n/a)</td><td>382.80 (n/a)</td><td>239.10 (n/a)</td><td>248.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.25 (-10.25%)</td><td>0.17 (-3.11%)</td><td>0.14 (+2.83%)</td><td>0.12 (-2.17%)</td><td>0.06 (-15.07%)</td><td>567.90 (+2.21%)</td><td>424.38 (+0.75%)</td><td>464.90 (-2.74%)</td><td>262.10 (+11.44%)</td><td>139.08 (-6.91%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>555.60 (n/a)</td><td>421.24 (n/a)</td><td>478.00 (n/a)</td><td>235.20 (n/a)</td><td>149.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.47 <b>(-21.93%)</b></td><td>0.35 (-3.43%)</td><td>0.29 (-0.83%)</td><td>0.28 <b>(+36.64%)</b></td><td>0.10 <b>(-42.71%)</b></td><td>469.50 <b>(-26.81%)</b></td><td>392.84 (-7.12%)</td><td>459.90 (+0.83%)</td><td>280.40 <b>(+28.10%)</b></td><td>98.87 <b>(-44.56%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>641.50 (n/a)</td><td>422.96 (n/a)</td><td>456.10 (n/a)</td><td>218.90 (n/a)</td><td>178.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.46 (-3.86%)</td><td>0.29 <b>(-21.75%)</b></td><td>0.27 <b>(-36.07%)</b></td><td>0.07 <b>(-69.39%)</b></td><td>0.16 <b>(+44.77%)</b></td><td>1808.80 <b>(+226.68%)</b></td><td>702.40 <b>(+81.34%)</b></td><td>487.70 <b>(+56.41%)</b></td><td>287.50 (+4.02%)</td><td>633.96 <b>(+388.84%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.47 (n/a)</td><td>0.37 (n/a)</td><td>0.42 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>553.70 (n/a)</td><td>387.34 (n/a)</td><td>311.80 (n/a)</td><td>276.40 (n/a)</td><td>129.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.32 <b>(-26.23%)</b></td><td>0.29 (-12.19%)</td><td>0.30 (+1.00%)</td><td>0.22 (-13.51%)</td><td>0.04 <b>(-44.04%)</b></td><td>587.10 (+15.62%)</td><td>464.42 (+12.13%)</td><td>431.70 (-0.99%)</td><td>405.30 <b>(+35.55%)</b></td><td>72.20 (-8.23%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>507.80 (n/a)</td><td>414.18 (n/a)</td><td>436.00 (n/a)</td><td>299.00 (n/a)</td><td>78.67 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 <b>(+25.14%)</b></td><td>0.05 (+1.25%)</td><td>0.04 (-18.48%)</td><td>0.02 <b>(-49.97%)</b></td><td>0.03 <b>(+93.11%)</b></td><td>1030.00 <b>(+99.84%)</b></td><td>480.12 <b>(+27.57%)</b></td><td>447.70 <b>(+22.66%)</b></td><td>196.70 <b>(-20.11%)</b></td><td>331.24 <b>(+202.23%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 21:04:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>515.40 (n/a)</td><td>376.36 (n/a)</td><td>365.00 (n/a)</td><td>246.20 (n/a)</td><td>109.60 (n/a)</td>
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
