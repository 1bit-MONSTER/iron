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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+14.72%)</td><td>0.02 <b>(-30.22%)</b></td><td>0.01 <b>(-47.96%)</b></td><td>0.01 <b>(-29.63%)</b></td><td>0.01 <b>(+68.14%)</b></td><td>583.50 <b>(+42.11%)</b></td><td>445.14 <b>(+58.60%)</b></td><td>459.00 <b>(+92.21%)</b></td><td>205.00 (-12.84%)</td><td>156.69 <b>(+107.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>410.60 (n/a)</td><td>280.66 (n/a)</td><td>238.80 (n/a)</td><td>235.20 (n/a)</td><td>75.35 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 <b>(-44.46%)</b></td><td>0.01 <b>(-29.64%)</b></td><td>0.01 (-16.79%)</td><td>0.01 (-3.60%)</td><td>0.00 <b>(-84.24%)</b></td><td>533.20 (+3.74%)</td><td>481.14 <b>(+30.34%)</b></td><td>478.60 <b>(+20.19%)</b></td><td>442.90 <b>(+80.04%)</b></td><td>37.47 <b>(-68.61%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>514.00 (n/a)</td><td>369.14 (n/a)</td><td>398.20 (n/a)</td><td>246.00 (n/a)</td><td>119.38 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (-2.57%)</td><td>0.02 (-1.10%)</td><td>0.02 (+10.48%)</td><td>0.01 (+10.05%)</td><td>0.01 (+4.71%)</td><td>502.30 (-9.12%)</td><td>347.78 (+1.99%)</td><td>276.70 (-9.49%)</td><td>236.90 (+2.64%)</td><td>134.12 (+1.23%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.70 (n/a)</td><td>340.98 (n/a)</td><td>305.70 (n/a)</td><td>230.80 (n/a)</td><td>132.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(-55.42%)</b></td><td>0.01 <b>(-46.67%)</b></td><td>0.01 <b>(-52.72%)</b></td><td>0.01 <b>(-20.58%)</b></td><td>0.00 <b>(-70.72%)</b></td><td>575.20 <b>(+25.92%)</b></td><td>484.60 <b>(+69.50%)</b></td><td>519.90 <b>(+111.51%)</b></td><td>334.00 <b>(+124.31%)</b></td><td>92.93 (-19.62%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>456.80 (n/a)</td><td>285.90 (n/a)</td><td>245.80 (n/a)</td><td>148.90 (n/a)</td><td>115.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+7.76%)</td><td>0.02 (-16.18%)</td><td>0.01 <b>(-39.99%)</b></td><td>0.01 <b>(-53.67%)</b></td><td>0.01 <b>(+152.65%)</b></td><td>808.00 <b>(+115.87%)</b></td><td>465.26 <b>(+47.92%)</b></td><td>506.60 <b>(+66.64%)</b></td><td>225.90 (-7.19%)</td><td>242.06 <b>(+349.97%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>374.30 (n/a)</td><td>314.54 (n/a)</td><td>304.00 (n/a)</td><td>243.40 (n/a)</td><td>53.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 <b>(+54.72%)</b></td><td>0.02 <b>(+29.41%)</b></td><td>0.01 (+1.10%)</td><td>0.01 (+17.99%)</td><td>0.01 <b>(+101.99%)</b></td><td>562.80 (-15.25%)</td><td>382.46 (-14.35%)</td><td>464.00 (-1.09%)</td><td>182.80 <b>(-35.36%)</b></td><td>165.53 (+11.14%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>664.10 (n/a)</td><td>446.52 (n/a)</td><td>469.10 (n/a)</td><td>282.80 (n/a)</td><td>148.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (-0.45%)</td><td>0.04 (+18.65%)</td><td>0.04 <b>(+43.98%)</b></td><td>0.02 (-8.57%)</td><td>0.01 (+5.80%)</td><td>612.00 (+9.36%)</td><td>395.68 (-13.66%)</td><td>349.70 <b>(-30.55%)</b></td><td>239.90 (+0.46%)</td><td>157.32 <b>(+20.44%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.60 (n/a)</td><td>458.28 (n/a)</td><td>503.50 (n/a)</td><td>238.80 (n/a)</td><td>130.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (-0.05%)</td><td>0.05 (+17.96%)</td><td>0.05 (+19.73%)</td><td>0.04 <b>(+31.27%)</b></td><td>0.00 <b>(-46.11%)</b></td><td>300.00 <b>(-23.80%)</b></td><td>268.54 (-17.04%)</td><td>262.50 (-16.51%)</td><td>245.80 (+0.04%)</td><td>23.90 <b>(-59.39%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>393.70 (n/a)</td><td>323.70 (n/a)</td><td>314.40 (n/a)</td><td>245.70 (n/a)</td><td>58.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 <b>(+44.01%)</b></td><td>0.04 <b>(+25.78%)</b></td><td>0.04 <b>(+32.55%)</b></td><td>0.02 (+5.25%)</td><td>0.02 <b>(+69.67%)</b></td><td>531.00 (-4.99%)</td><td>341.02 (-15.01%)</td><td>299.20 <b>(-24.56%)</b></td><td>185.60 <b>(-30.56%)</b></td><td>142.97 (+16.12%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.90 (n/a)</td><td>401.24 (n/a)</td><td>396.60 (n/a)</td><td>267.30 (n/a)</td><td>123.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (-2.29%)</td><td>0.04 (+5.10%)</td><td>0.05 <b>(+24.12%)</b></td><td>0.02 (-10.41%)</td><td>0.02 (+7.68%)</td><td>602.80 (+11.61%)</td><td>356.92 (-0.41%)</td><td>237.70 (-19.45%)</td><td>190.10 (+2.31%)</td><td>190.59 (+18.53%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>540.10 (n/a)</td><td>358.38 (n/a)</td><td>295.10 (n/a)</td><td>185.80 (n/a)</td><td>160.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (+7.25%)</td><td>0.04 (+4.55%)</td><td>0.04 (+10.94%)</td><td>0.03 (+14.68%)</td><td>0.01 (+11.45%)</td><td>476.40 (-12.80%)</td><td>352.60 (-4.39%)</td><td>318.00 (-9.84%)</td><td>252.90 (-6.78%)</td><td>92.36 (-11.91%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.30 (n/a)</td><td>368.78 (n/a)</td><td>352.70 (n/a)</td><td>271.30 (n/a)</td><td>104.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 <b>(+25.54%)</b></td><td>0.03 (-6.57%)</td><td>0.02 <b>(-25.33%)</b></td><td>0.01 <b>(-68.34%)</b></td><td>0.02 <b>(+93.28%)</b></td><td>1864.50 <b>(+215.80%)</b></td><td>701.86 <b>(+58.97%)</b></td><td>513.00 <b>(+33.91%)</b></td><td>248.40 <b>(-20.36%)</b></td><td>661.84 <b>(+403.68%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.40 (n/a)</td><td>441.50 (n/a)</td><td>383.10 (n/a)</td><td>311.90 (n/a)</td><td>131.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (+17.11%)</td><td>0.06 (-1.60%)</td><td>0.05 (-13.81%)</td><td>0.04 (+6.05%)</td><td>0.02 <b>(+36.72%)</b></td><td>616.10 (-5.71%)</td><td>479.20 (+4.18%)</td><td>504.10 (+16.02%)</td><td>267.90 (-14.60%)</td><td>133.53 (+4.10%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>653.40 (n/a)</td><td>459.96 (n/a)</td><td>434.50 (n/a)</td><td>313.70 (n/a)</td><td>128.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (-10.93%)</td><td>0.06 (-4.28%)</td><td>0.05 <b>(-23.47%)</b></td><td>0.04 <b>(+276.30%)</b></td><td>0.01 <b>(-53.36%)</b></td><td>553.60 <b>(-73.43%)</b></td><td>465.14 <b>(-35.46%)</b></td><td>498.20 <b>(+30.66%)</b></td><td>310.70 (+12.25%)</td><td>98.76 <b>(-87.16%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2083.30 (n/a)</td><td>720.74 (n/a)</td><td>381.30 (n/a)</td><td>276.80 (n/a)</td><td>768.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (-3.30%)</td><td>0.07 (-3.26%)</td><td>0.06 (-13.46%)</td><td>0.05 <b>(+33.92%)</b></td><td>0.02 <b>(-22.31%)</b></td><td>510.80 <b>(-25.32%)</b></td><td>394.20 (-3.31%)</td><td>429.50 (+15.55%)</td><td>258.00 (+3.41%)</td><td>109.60 <b>(-38.34%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>684.00 (n/a)</td><td>407.70 (n/a)</td><td>371.70 (n/a)</td><td>249.50 (n/a)</td><td>177.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 <b>(+51.60%)</b></td><td>0.07 (+9.07%)</td><td>0.05 <b>(-37.52%)</b></td><td>0.04 (+0.03%)</td><td>0.04 <b>(+88.43%)</b></td><td>589.90 (-0.03%)</td><td>400.34 (+2.34%)</td><td>485.10 <b>(+60.05%)</b></td><td>187.40 <b>(-34.04%)</b></td><td>175.86 <b>(+26.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>590.10 (n/a)</td><td>391.18 (n/a)</td><td>303.10 (n/a)</td><td>284.10 (n/a)</td><td>139.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (+1.11%)</td><td>0.07 (+10.12%)</td><td>0.08 <b>(+57.06%)</b></td><td>0.04 (-9.27%)</td><td>0.03 (+8.56%)</td><td>637.20 (+10.22%)</td><td>400.80 (-6.40%)</td><td>294.40 <b>(-36.33%)</b></td><td>249.30 (-1.11%)</td><td>175.52 (+19.00%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>578.10 (n/a)</td><td>428.22 (n/a)</td><td>462.40 (n/a)</td><td>252.10 (n/a)</td><td>147.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (+13.22%)</td><td>0.06 (-13.06%)</td><td>0.05 <b>(-20.57%)</b></td><td>0.03 <b>(-37.58%)</b></td><td>0.03 <b>(+105.28%)</b></td><td>812.60 <b>(+60.21%)</b></td><td>506.18 <b>(+36.78%)</b></td><td>462.00 <b>(+25.92%)</b></td><td>247.20 (-11.68%)</td><td>250.08 <b>(+189.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>507.20 (n/a)</td><td>370.08 (n/a)</td><td>366.90 (n/a)</td><td>279.90 (n/a)</td><td>86.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.21 (+2.50%)</td><td>0.16 (+7.59%)</td><td>0.18 (+0.47%)</td><td>0.09 <b>(+31.81%)</b></td><td>0.05 (-11.17%)</td><td>535.20 <b>(-24.13%)</b></td><td>342.74 (-13.42%)</td><td>269.30 (-0.44%)</td><td>233.30 (-2.47%)</td><td>135.98 <b>(-33.84%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>705.40 (n/a)</td><td>395.86 (n/a)</td><td>270.50 (n/a)</td><td>239.20 (n/a)</td><td>205.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.19 <b>(-22.57%)</b></td><td>0.12 <b>(-31.11%)</b></td><td>0.11 <b>(-45.46%)</b></td><td>0.03 <b>(-72.43%)</b></td><td>0.07 (+18.60%)</td><td>1933.70 <b>(+262.80%)</b></td><td>681.92 <b>(+118.45%)</b></td><td>457.10 <b>(+83.35%)</b></td><td>261.40 <b>(+29.15%)</b></td><td>707.83 <b>(+438.63%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>533.00 (n/a)</td><td>312.16 (n/a)</td><td>249.30 (n/a)</td><td>202.40 (n/a)</td><td>131.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.20 (+4.65%)</td><td>0.13 (+3.29%)</td><td>0.10 (-15.97%)</td><td>0.09 <b>(+31.73%)</b></td><td>0.05 (+0.94%)</td><td>531.50 <b>(-24.08%)</b></td><td>426.04 (-5.43%)</td><td>506.80 (+19.00%)</td><td>243.90 (-4.43%)</td><td>133.56 <b>(-23.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>700.10 (n/a)</td><td>450.50 (n/a)</td><td>425.90 (n/a)</td><td>255.20 (n/a)</td><td>174.46 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.20 (+4.08%)</td><td>0.13 <b>(-27.16%)</b></td><td>0.12 <b>(-35.36%)</b></td><td>0.05 <b>(-69.17%)</b></td><td>0.06 <b>(+328.73%)</b></td><td>980.40 <b>(+224.42%)</b></td><td>476.72 <b>(+73.49%)</b></td><td>411.30 <b>(+54.68%)</b></td><td>244.20 (-3.93%)</td><td>297.42 <b>(+1239.93%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>302.20 (n/a)</td><td>274.78 (n/a)</td><td>265.90 (n/a)</td><td>254.20 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.21 (-6.42%)</td><td>0.16 (-11.11%)</td><td>0.18 (-10.11%)</td><td>0.10 <b>(-28.68%)</b></td><td>0.04 (+15.03%)</td><td>496.50 <b>(+40.21%)</b></td><td>318.72 (+16.33%)</td><td>277.20 (+11.24%)</td><td>232.90 (+6.83%)</td><td>103.67 <b>(+80.51%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>354.10 (n/a)</td><td>273.98 (n/a)</td><td>249.20 (n/a)</td><td>218.00 (n/a)</td><td>57.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 <b>(-39.70%)</b></td><td>0.14 (-15.48%)</td><td>0.16 (-3.65%)</td><td>0.11 (+15.77%)</td><td>0.03 <b>(-58.99%)</b></td><td>448.10 (-13.61%)</td><td>355.42 (+7.72%)</td><td>310.50 (+3.81%)</td><td>280.30 <b>(+65.86%)</b></td><td>79.30 <b>(-37.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>518.70 (n/a)</td><td>329.96 (n/a)</td><td>299.10 (n/a)</td><td>169.00 (n/a)</td><td>127.46 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-2.65%)</td><td>0.01 (+10.91%)</td><td>0.01 (+3.76%)</td><td>0.01 <b>(+53.21%)</b></td><td>0.00 <b>(-46.81%)</b></td><td>360.30 <b>(-34.74%)</b></td><td>288.74 (-18.30%)</td><td>265.20 (-3.63%)</td><td>237.80 (+2.72%)</td><td>52.50 <b>(-63.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>552.10 (n/a)</td><td>353.42 (n/a)</td><td>275.20 (n/a)</td><td>231.50 (n/a)</td><td>145.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-4.62%)</td><td>0.01 <b>(+21.54%)</b></td><td>0.01 <b>(+46.01%)</b></td><td>0.00 (-9.51%)</td><td>0.00 (+4.58%)</td><td>618.50 (+10.51%)</td><td>349.94 (-14.94%)</td><td>291.10 <b>(-31.51%)</b></td><td>233.00 (+4.86%)</td><td>159.13 <b>(+31.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>559.70 (n/a)</td><td>411.40 (n/a)</td><td>425.00 (n/a)</td><td>222.20 (n/a)</td><td>120.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 <b>(+23.19%)</b></td><td>0.01 <b>(+24.69%)</b></td><td>0.01 <b>(+30.32%)</b></td><td>0.00 (+3.70%)</td><td>0.00 <b>(+35.03%)</b></td><td>597.30 (-3.57%)</td><td>413.64 (-17.57%)</td><td>421.20 <b>(-23.26%)</b></td><td>242.20 (-18.83%)</td><td>134.09 (+9.50%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>619.40 (n/a)</td><td>501.82 (n/a)</td><td>548.90 (n/a)</td><td>298.40 (n/a)</td><td>122.46 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-0.44%)</td><td>0.01 <b>(+24.64%)</b></td><td>0.01 <b>(+52.77%)</b></td><td>0.00 <b>(+34.55%)</b></td><td>0.00 (-14.59%)</td><td>527.10 <b>(-25.67%)</b></td><td>353.90 <b>(-23.56%)</b></td><td>315.20 <b>(-34.55%)</b></td><td>246.10 (+0.45%)</td><td>113.44 <b>(-33.67%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>709.10 (n/a)</td><td>462.98 (n/a)</td><td>481.60 (n/a)</td><td>245.00 (n/a)</td><td>171.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 <b>(+27.35%)</b></td><td>0.01 (+6.39%)</td><td>0.00 (-14.92%)</td><td>0.00 <b>(-68.39%)</b></td><td>0.01 <b>(+87.52%)</b></td><td>1837.10 <b>(+216.36%)</b></td><td>706.92 <b>(+53.06%)</b></td><td>566.90 (+17.54%)</td><td>187.30 <b>(-21.50%)</b></td><td>662.09 <b>(+391.95%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>580.70 (n/a)</td><td>461.86 (n/a)</td><td>482.30 (n/a)</td><td>238.60 (n/a)</td><td>134.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 <b>(-51.48%)</b></td><td>0.00 <b>(-28.01%)</b></td><td>0.00 (-6.67%)</td><td>0.00 <b>(-56.67%)</b></td><td>0.00 <b>(-43.93%)</b></td><td>1961.40 <b>(+130.81%)</b></td><td>808.82 <b>(+56.42%)</b></td><td>527.30 (+7.15%)</td><td>489.00 <b>(+106.07%)</b></td><td>644.80 <b>(+195.30%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>849.80 (n/a)</td><td>517.08 (n/a)</td><td>492.10 (n/a)</td><td>237.30 (n/a)</td><td>218.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+3.88%)</td><td>0.02 <b>(+22.45%)</b></td><td>0.02 <b>(+42.43%)</b></td><td>0.01 <b>(+24.27%)</b></td><td>0.01 (+8.24%)</td><td>547.20 (-19.53%)</td><td>348.34 (-18.63%)</td><td>270.40 <b>(-29.78%)</b></td><td>221.30 (-3.74%)</td><td>143.76 (-15.01%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>680.00 (n/a)</td><td>428.12 (n/a)</td><td>385.10 (n/a)</td><td>229.90 (n/a)</td><td>169.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+1.13%)</td><td>0.02 (+1.57%)</td><td>0.02 (+0.02%)</td><td>0.01 <b>(+25.29%)</b></td><td>0.00 <b>(-22.43%)</b></td><td>512.70 <b>(-20.18%)</b></td><td>372.86 (-8.90%)</td><td>333.60 (-0.03%)</td><td>236.10 (-1.13%)</td><td>109.83 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>642.30 (n/a)</td><td>409.30 (n/a)</td><td>333.70 (n/a)</td><td>238.80 (n/a)</td><td>180.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+16.61%)</td><td>0.02 <b>(-24.91%)</b></td><td>0.01 <b>(-51.08%)</b></td><td>0.01 <b>(-48.53%)</b></td><td>0.01 <b>(+364.85%)</b></td><td>572.30 <b>(+94.33%)</b></td><td>412.94 <b>(+59.31%)</b></td><td>518.20 <b>(+104.42%)</b></td><td>205.60 (-14.23%)</td><td>174.16 <b>(+681.59%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>294.50 (n/a)</td><td>259.20 (n/a)</td><td>253.50 (n/a)</td><td>239.70 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+6.30%)</td><td>0.01 (-1.55%)</td><td>0.01 (-16.04%)</td><td>0.01 (-13.43%)</td><td>0.01 <b>(+38.00%)</b></td><td>755.30 (+15.52%)</td><td>464.26 (+10.97%)</td><td>500.40 (+19.11%)</td><td>248.30 (-5.91%)</td><td>216.31 <b>(+39.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.80 (n/a)</td><td>418.36 (n/a)</td><td>420.10 (n/a)</td><td>263.90 (n/a)</td><td>155.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-2.39%)</td><td>0.02 (-3.57%)</td><td>0.01 <b>(-25.06%)</b></td><td>0.01 (-8.64%)</td><td>0.01 (+4.41%)</td><td>605.80 (+9.45%)</td><td>384.64 (+4.79%)</td><td>386.60 <b>(+33.45%)</b></td><td>230.10 (+2.45%)</td><td>155.30 (+6.22%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.50 (n/a)</td><td>367.06 (n/a)</td><td>289.70 (n/a)</td><td>224.60 (n/a)</td><td>146.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-12.14%)</td><td>0.01 <b>(-25.84%)</b></td><td>0.01 <b>(-39.63%)</b></td><td>0.01 <b>(-29.83%)</b></td><td>0.00 <b>(-20.04%)</b></td><td>801.80 <b>(+42.52%)</b></td><td>551.54 <b>(+34.97%)</b></td><td>533.40 <b>(+65.65%)</b></td><td>357.00 (+13.80%)</td><td>164.38 <b>(+31.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.60 (n/a)</td><td>408.64 (n/a)</td><td>322.00 (n/a)</td><td>313.70 (n/a)</td><td>124.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (-17.90%)</td><td>0.03 <b>(-26.10%)</b></td><td>0.03 <b>(-33.12%)</b></td><td>0.02 (-6.00%)</td><td>0.01 <b>(-31.70%)</b></td><td>522.80 (+6.37%)</td><td>425.64 <b>(+31.88%)</b></td><td>416.00 <b>(+49.53%)</b></td><td>295.50 <b>(+21.81%)</b></td><td>92.70 (-10.25%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.50 (n/a)</td><td>322.74 (n/a)</td><td>278.20 (n/a)</td><td>242.60 (n/a)</td><td>103.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (+2.58%)</td><td>0.03 (-18.80%)</td><td>0.04 (-16.11%)</td><td>0.01 <b>(-66.06%)</b></td><td>0.01 <b>(+118.06%)</b></td><td>1074.00 <b>(+194.57%)</b></td><td>446.30 <b>(+61.38%)</b></td><td>298.80 (+19.19%)</td><td>233.40 (-2.51%)</td><td>353.18 <b>(+586.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>364.60 (n/a)</td><td>276.56 (n/a)</td><td>250.70 (n/a)</td><td>239.40 (n/a)</td><td>51.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (+2.02%)</td><td>0.03 (-15.30%)</td><td>0.04 (-17.47%)</td><td>0.02 (-19.75%)</td><td>0.01 <b>(+24.41%)</b></td><td>576.40 <b>(+24.60%)</b></td><td>372.74 <b>(+25.13%)</b></td><td>295.90 <b>(+21.17%)</b></td><td>223.50 (-1.97%)</td><td>151.40 <b>(+55.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.60 (n/a)</td><td>297.88 (n/a)</td><td>244.20 (n/a)</td><td>228.00 (n/a)</td><td>97.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (-7.23%)</td><td>0.03 (-12.62%)</td><td>0.02 <b>(-24.49%)</b></td><td>0.02 (+19.24%)</td><td>0.01 <b>(-27.26%)</b></td><td>501.00 (-16.14%)</td><td>414.42 (+5.89%)</td><td>478.30 <b>(+32.42%)</b></td><td>237.80 (+7.80%)</td><td>110.14 <b>(-34.60%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>597.40 (n/a)</td><td>391.38 (n/a)</td><td>361.20 (n/a)</td><td>220.60 (n/a)</td><td>168.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (+6.10%)</td><td>0.03 (-7.24%)</td><td>0.03 (-16.12%)</td><td>0.02 (-6.82%)</td><td>0.01 (+9.62%)</td><td>579.90 (+7.33%)</td><td>409.50 (+10.91%)</td><td>418.50 (+19.20%)</td><td>228.10 (-5.74%)</td><td>157.08 (+17.86%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.30 (n/a)</td><td>369.22 (n/a)</td><td>351.10 (n/a)</td><td>242.00 (n/a)</td><td>133.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 <b>(+57.12%)</b></td><td>0.03 (+19.27%)</td><td>0.02 (+3.90%)</td><td>0.02 <b>(+21.68%)</b></td><td>0.01 <b>(+94.60%)</b></td><td>539.10 (-17.82%)</td><td>435.94 (-11.44%)</td><td>503.40 (-3.75%)</td><td>218.70 <b>(-36.35%)</b></td><td>133.21 (+2.76%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>656.00 (n/a)</td><td>492.24 (n/a)</td><td>523.00 (n/a)</td><td>343.60 (n/a)</td><td>129.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-14.77%)</td><td>0.06 <b>(-22.48%)</b></td><td>0.05 <b>(-37.28%)</b></td><td>0.04 (-11.58%)</td><td>0.01 (-7.22%)</td><td>506.10 (+13.09%)</td><td>396.12 <b>(+29.32%)</b></td><td>432.80 <b>(+59.41%)</b></td><td>291.30 (+17.32%)</td><td>91.93 (+14.06%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>447.50 (n/a)</td><td>306.32 (n/a)</td><td>271.50 (n/a)</td><td>248.30 (n/a)</td><td>80.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (-2.66%)</td><td>0.06 (-1.01%)</td><td>0.04 (-12.05%)</td><td>0.04 (+2.53%)</td><td>0.02 (+5.41%)</td><td>532.70 (-2.45%)</td><td>414.00 (+2.75%)</td><td>490.30 (+13.71%)</td><td>238.60 (+2.76%)</td><td>131.08 (+12.94%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.10 (n/a)</td><td>402.92 (n/a)</td><td>431.20 (n/a)</td><td>232.20 (n/a)</td><td>116.06 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-14.06%)</td><td>0.06 (-8.88%)</td><td>0.05 <b>(-26.81%)</b></td><td>0.04 (+15.37%)</td><td>0.02 <b>(-32.44%)</b></td><td>510.00 (-13.32%)</td><td>380.16 (+2.67%)</td><td>398.30 <b>(+36.64%)</b></td><td>281.20 (+16.39%)</td><td>98.86 <b>(-35.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>588.40 (n/a)</td><td>370.28 (n/a)</td><td>291.50 (n/a)</td><td>241.60 (n/a)</td><td>152.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (-4.24%)</td><td>0.05 (-18.29%)</td><td>0.05 (-7.27%)</td><td>0.04 (-8.50%)</td><td>0.02 (-16.29%)</td><td>592.20 (+9.28%)</td><td>459.80 (+19.86%)</td><td>458.30 (+7.84%)</td><td>245.00 (+4.39%)</td><td>139.26 (-0.06%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>541.90 (n/a)</td><td>383.60 (n/a)</td><td>425.00 (n/a)</td><td>234.70 (n/a)</td><td>139.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 <b>(+37.74%)</b></td><td>0.05 (-1.05%)</td><td>0.04 (-16.35%)</td><td>0.03 (-16.22%)</td><td>0.03 <b>(+116.30%)</b></td><td>653.30 (+19.37%)</td><td>500.32 (+13.05%)</td><td>564.90 (+19.56%)</td><td>224.70 <b>(-27.40%)</b></td><td>174.98 <b>(+85.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>547.30 (n/a)</td><td>442.58 (n/a)</td><td>472.50 (n/a)</td><td>309.50 (n/a)</td><td>94.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 <b>(-40.66%)</b></td><td>0.04 (-16.86%)</td><td>0.04 (-6.93%)</td><td>0.03 (-15.43%)</td><td>0.01 <b>(-67.08%)</b></td><td>609.90 (+18.24%)</td><td>487.38 (+14.49%)</td><td>477.00 (+7.46%)</td><td>427.60 <b>(+68.55%)</b></td><td>71.93 <b>(-30.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>515.80 (n/a)</td><td>425.68 (n/a)</td><td>443.90 (n/a)</td><td>253.70 (n/a)</td><td>103.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.50 (n/a)</td><td>385.24 (n/a)</td><td>343.80 (n/a)</td><td>246.80 (n/a)</td><td>162.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>474.00 (n/a)</td><td>380.10 (n/a)</td><td>452.00 (n/a)</td><td>246.10 (n/a)</td><td>118.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.20 (n/a)</td><td>435.82 (n/a)</td><td>477.60 (n/a)</td><td>150.80 (n/a)</td><td>172.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1991.30 (n/a)</td><td>964.28 (n/a)</td><td>403.80 (n/a)</td><td>229.50 (n/a)</td><td>909.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1944.40 (n/a)</td><td>676.16 (n/a)</td><td>481.20 (n/a)</td><td>186.80 (n/a)</td><td>724.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>676.10 (n/a)</td><td>444.46 (n/a)</td><td>497.20 (n/a)</td><td>163.50 (n/a)</td><td>210.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>575.50 (n/a)</td><td>369.80 (n/a)</td><td>387.20 (n/a)</td><td>203.80 (n/a)</td><td>152.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>803.00 (n/a)</td><td>453.34 (n/a)</td><td>448.10 (n/a)</td><td>220.60 (n/a)</td><td>242.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>674.80 (n/a)</td><td>610.98 (n/a)</td><td>605.90 (n/a)</td><td>502.50 (n/a)</td><td>69.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.24 (+8.35%)</td><td>0.13 (-4.15%)</td><td>0.10 (-8.92%)</td><td>0.09 (+18.81%)</td><td>0.06 (+10.38%)</td><td>517.80 (-15.83%)</td><td>426.68 (+4.08%)</td><td>483.60 (+9.81%)</td><td>208.80 (-7.69%)</td><td>129.84 (-13.70%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>615.20 (n/a)</td><td>409.94 (n/a)</td><td>440.40 (n/a)</td><td>226.20 (n/a)</td><td>150.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>466.20 (n/a)</td><td>375.26 (n/a)</td><td>361.60 (n/a)</td><td>282.50 (n/a)</td><td>78.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>2407.50 (n/a)</td><td>808.14 (n/a)</td><td>461.50 (n/a)</td><td>221.00 (n/a)</td><td>902.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>414.30 (n/a)</td><td>338.26 (n/a)</td><td>385.60 (n/a)</td><td>245.10 (n/a)</td><td>85.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>408.22 (n/a)</td><td>454.50 (n/a)</td><td>205.60 (n/a)</td><td>173.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>756.50 (n/a)</td><td>455.38 (n/a)</td><td>457.80 (n/a)</td><td>175.40 (n/a)</td><td>227.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>406.46 (n/a)</td><td>432.10 (n/a)</td><td>233.70 (n/a)</td><td>157.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.70 (n/a)</td><td>383.36 (n/a)</td><td>412.60 (n/a)</td><td>242.80 (n/a)</td><td>128.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>523.90 (n/a)</td><td>320.96 (n/a)</td><td>281.80 (n/a)</td><td>212.20 (n/a)</td><td>130.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>499.90 (n/a)</td><td>331.14 (n/a)</td><td>248.60 (n/a)</td><td>214.30 (n/a)</td><td>136.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>384.70 (n/a)</td><td>270.60 (n/a)</td><td>245.20 (n/a)</td><td>170.70 (n/a)</td><td>81.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.80 (n/a)</td><td>361.64 (n/a)</td><td>293.80 (n/a)</td><td>242.50 (n/a)</td><td>129.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>530.30 (n/a)</td><td>378.48 (n/a)</td><td>418.60 (n/a)</td><td>253.50 (n/a)</td><td>116.93 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>641.90 (n/a)</td><td>441.54 (n/a)</td><td>409.70 (n/a)</td><td>244.50 (n/a)</td><td>147.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.80 (n/a)</td><td>402.06 (n/a)</td><td>331.80 (n/a)</td><td>197.60 (n/a)</td><td>203.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.60 (n/a)</td><td>354.82 (n/a)</td><td>360.20 (n/a)</td><td>227.30 (n/a)</td><td>96.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.80 (n/a)</td><td>358.34 (n/a)</td><td>359.50 (n/a)</td><td>233.40 (n/a)</td><td>116.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.50 (n/a)</td><td>423.36 (n/a)</td><td>483.10 (n/a)</td><td>260.50 (n/a)</td><td>132.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>556.80 (n/a)</td><td>340.90 (n/a)</td><td>283.10 (n/a)</td><td>245.60 (n/a)</td><td>125.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.10 (n/a)</td><td>461.36 (n/a)</td><td>491.10 (n/a)</td><td>278.80 (n/a)</td><td>108.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>662.10 (n/a)</td><td>507.40 (n/a)</td><td>461.10 (n/a)</td><td>386.80 (n/a)</td><td>120.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.90 (n/a)</td><td>366.64 (n/a)</td><td>307.20 (n/a)</td><td>223.20 (n/a)</td><td>136.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>415.98 (n/a)</td><td>428.50 (n/a)</td><td>191.40 (n/a)</td><td>134.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>403.24 (n/a)</td><td>480.10 (n/a)</td><td>229.30 (n/a)</td><td>146.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.00 (n/a)</td><td>385.94 (n/a)</td><td>298.60 (n/a)</td><td>233.30 (n/a)</td><td>189.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>543.30 (n/a)</td><td>458.44 (n/a)</td><td>470.00 (n/a)</td><td>327.30 (n/a)</td><td>81.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>528.70 (n/a)</td><td>343.24 (n/a)</td><td>313.60 (n/a)</td><td>258.90 (n/a)</td><td>106.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1051.70 (n/a)</td><td>558.80 (n/a)</td><td>469.30 (n/a)</td><td>236.90 (n/a)</td><td>301.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.90 (n/a)</td><td>319.34 (n/a)</td><td>283.20 (n/a)</td><td>230.00 (n/a)</td><td>123.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1845.20 (n/a)</td><td>717.08 (n/a)</td><td>478.00 (n/a)</td><td>246.90 (n/a)</td><td>640.89 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>502.30 (n/a)</td><td>314.22 (n/a)</td><td>270.00 (n/a)</td><td>243.60 (n/a)</td><td>108.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>623.00 (n/a)</td><td>457.18 (n/a)</td><td>476.70 (n/a)</td><td>332.90 (n/a)</td><td>124.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>529.90 (n/a)</td><td>390.70 (n/a)</td><td>405.40 (n/a)</td><td>272.70 (n/a)</td><td>100.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>565.50 (n/a)</td><td>387.00 (n/a)</td><td>344.00 (n/a)</td><td>256.40 (n/a)</td><td>132.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2064.80 (n/a)</td><td>856.84 (n/a)</td><td>480.90 (n/a)</td><td>259.90 (n/a)</td><td>730.89 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1915.10 (n/a)</td><td>734.58 (n/a)</td><td>500.10 (n/a)</td><td>233.50 (n/a)</td><td>671.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>623.30 (n/a)</td><td>469.10 (n/a)</td><td>466.30 (n/a)</td><td>246.80 (n/a)</td><td>147.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>680.10 (n/a)</td><td>446.68 (n/a)</td><td>407.20 (n/a)</td><td>340.80 (n/a)</td><td>139.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.48 <b>(-26.66%)</b></td><td>0.40 (+3.15%)</td><td>0.39 (+4.75%)</td><td>0.33 <b>(+146.12%)</b></td><td>0.07 <b>(-62.11%)</b></td><td>675.20 <b>(-59.37%)</b></td><td>564.66 <b>(-24.48%)</b></td><td>567.50 (-4.53%)</td><td>457.80 <b>(+36.33%)</b></td><td>99.56 <b>(-81.01%)</b></td><td>20.61 <b>(-26.66%)</b></td><td>17.14 (+3.15%)</td><td>16.63 (+4.75%)</td><td>13.98 <b>(+146.13%)</b></td><td>3.06 <b>(-62.11%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.66 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.13 (n/a)</td><td>0.19 (n/a)</td><td>1661.90 (n/a)</td><td>747.72 (n/a)</td><td>594.40 (n/a)</td><td>335.80 (n/a)</td><td>524.36 (n/a)</td><td>28.11 (n/a)</td><td>16.62 (n/a)</td><td>15.88 (n/a)</td><td>5.68 (n/a)</td><td>8.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.37 (-12.76%)</td><td>0.28 (-2.35%)</td><td>0.35 (+8.29%)</td><td>0.13 (+2.60%)</td><td>0.11 (-4.64%)</td><td>1669.20 (-2.53%)</td><td>924.76 (+1.65%)</td><td>629.60 (-7.66%)</td><td>599.10 (+14.64%)</td><td>470.10 (-2.62%)</td><td>15.75 (-12.76%)</td><td>12.07 (-2.35%)</td><td>14.99 (+8.29%)</td><td>5.65 (+2.60%)</td><td>4.69 (-4.64%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>1712.50 (n/a)</td><td>909.78 (n/a)</td><td>681.80 (n/a)</td><td>522.60 (n/a)</td><td>482.74 (n/a)</td><td>18.06 (n/a)</td><td>12.36 (n/a)</td><td>13.84 (n/a)</td><td>5.51 (n/a)</td><td>4.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.31 (+1.30%)</td><td>0.30 (-0.42%)</td><td>0.30 (-1.36%)</td><td>0.30 (+0.02%)</td><td>0.00 <b>(+49.76%)</b></td><td>83897.80 (-0.02%)</td><td>82791.12 (+0.43%)</td><td>83225.40 (+1.38%)</td><td>80509.10 (-1.28%)</td><td>1317.42 <b>(+46.96%)</b></td><td>213.39 (+1.30%)</td><td>207.55 (-0.42%)</td><td>206.43 (-1.36%)</td><td>204.77 (+0.02%)</td><td>3.36 <b>(+49.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83916.10 (n/a)</td><td>82434.36 (n/a)</td><td>82095.40 (n/a)</td><td>81552.50 (n/a)</td><td>896.44 (n/a)</td><td>210.66 (n/a)</td><td>208.43 (n/a)</td><td>209.27 (n/a)</td><td>204.73 (n/a)</td><td>2.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>1.03 (+1.98%)</td><td>1.01 (+2.95%)</td><td>1.01 (+2.22%)</td><td>0.98 (+4.65%)</td><td>0.02 <b>(-37.17%)</b></td><td>25785.60 (-4.44%)</td><td>24932.68 (-2.92%)</td><td>24866.70 (-2.17%)</td><td>24483.00 (-1.94%)</td><td>503.19 <b>(-40.76%)</b></td><td>701.71 (+1.98%)</td><td>689.27 (+2.95%)</td><td>690.88 (+2.22%)</td><td>666.26 (+4.65%)</td><td>13.64 <b>(-37.17%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.99 (n/a)</td><td>0.93 (n/a)</td><td>0.03 (n/a)</td><td>26983.40 (n/a)</td><td>25682.72 (n/a)</td><td>25417.90 (n/a)</td><td>24968.20 (n/a)</td><td>849.47 (n/a)</td><td>688.07 (n/a)</td><td>669.50 (n/a)</td><td>675.90 (n/a)</td><td>636.68 (n/a)</td><td>21.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.83 (+0.39%)</td><td>0.79 (-2.60%)</td><td>0.81 (-1.39%)</td><td>0.73 (-7.09%)</td><td>0.04 <b>(+169.12%)</b></td><td>102941.30 (+7.63%)</td><td>95774.80 (+2.85%)</td><td>93757.60 (+1.41%)</td><td>91336.50 (-0.39%)</td><td>4841.71 <b>(+188.73%)</b></td><td>752.38 (+0.39%)</td><td>718.94 (-2.60%)</td><td>732.95 (-1.39%)</td><td>667.56 (-7.09%)</td><td>35.40 <b>(+169.12%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95642.00 (n/a)</td><td>93123.30 (n/a)</td><td>92451.70 (n/a)</td><td>91694.50 (n/a)</td><td>1676.92 (n/a)</td><td>749.44 (n/a)</td><td>738.13 (n/a)</td><td>743.30 (n/a)</td><td>718.51 (n/a)</td><td>13.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.77 (+0.24%)</td><td>0.77 (+1.31%)</td><td>0.77 (+1.56%)</td><td>0.76 (+2.12%)</td><td>0.01 <b>(-41.59%)</b></td><td>99992.10 (-2.08%)</td><td>98556.24 (-1.30%)</td><td>98270.90 (-1.54%)</td><td>97770.50 (-0.24%)</td><td>905.39 <b>(-42.95%)</b></td><td>702.86 (+0.24%)</td><td>697.31 (+1.31%)</td><td>699.29 (+1.56%)</td><td>687.25 (+2.12%)</td><td>6.36 <b>(-41.59%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>102114.60 (n/a)</td><td>99857.68 (n/a)</td><td>99803.10 (n/a)</td><td>98007.00 (n/a)</td><td>1586.92 (n/a)</td><td>701.17 (n/a)</td><td>688.31 (n/a)</td><td>688.55 (n/a)</td><td>672.96 (n/a)</td><td>10.89 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.80 (+0.85%)</td><td>0.80 (+0.84%)</td><td>0.80 (+0.85%)</td><td>0.79 (+0.93%)</td><td>0.00 (-16.78%)</td><td>95036.10 (-0.92%)</td><td>94436.52 (-0.83%)</td><td>94314.30 (-0.84%)</td><td>93854.50 (-0.84%)</td><td>453.43 (-18.21%)</td><td>732.19 (+0.85%)</td><td>727.69 (+0.84%)</td><td>728.62 (+0.85%)</td><td>723.09 (+0.93%)</td><td>3.49 (-16.78%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95917.40 (n/a)</td><td>95227.28 (n/a)</td><td>95117.60 (n/a)</td><td>94648.50 (n/a)</td><td>554.40 (n/a)</td><td>726.05 (n/a)</td><td>721.66 (n/a)</td><td>722.47 (n/a)</td><td>716.44 (n/a)</td><td>4.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>4.67 (-17.76%)</td><td>3.70 (-4.53%)</td><td>3.97 (-0.94%)</td><td>2.59 <b>(+22.61%)</b></td><td>0.89 <b>(-30.42%)</b></td><td>3442.70 (-18.44%)</td><td>2534.78 (-0.59%)</td><td>2242.70 (+0.95%)</td><td>1909.90 <b>(+21.60%)</b></td><td>663.87 <b>(-33.76%)</b></td><td>281.09 (-17.76%)</td><td>223.00 (-4.53%)</td><td>239.38 (-0.94%)</td><td>155.94 <b>(+22.61%)</b></td><td>53.89 <b>(-30.42%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.67 (n/a)</td><td>3.88 (n/a)</td><td>4.01 (n/a)</td><td>2.11 (n/a)</td><td>1.29 (n/a)</td><td>4221.30 (n/a)</td><td>2549.76 (n/a)</td><td>2221.60 (n/a)</td><td>1570.70 (n/a)</td><td>1002.21 (n/a)</td><td>341.81 (n/a)</td><td>233.58 (n/a)</td><td>241.66 (n/a)</td><td>127.18 (n/a)</td><td>77.46 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>4.75 (+3.63%)</td><td>2.86 (-0.64%)</td><td>2.48 (+1.15%)</td><td>2.18 (-5.12%)</td><td>1.08 (+11.17%)</td><td>4096.00 (+5.40%)</td><td>3386.44 (+2.24%)</td><td>3595.70 (-1.14%)</td><td>1878.00 (-3.50%)</td><td>908.87 (+12.61%)</td><td>285.88 (+3.63%)</td><td>172.26 (-0.64%)</td><td>149.31 (+1.15%)</td><td>131.07 (-5.12%)</td><td>64.91 (+11.17%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>4.58 (n/a)</td><td>2.88 (n/a)</td><td>2.45 (n/a)</td><td>2.29 (n/a)</td><td>0.97 (n/a)</td><td>3886.10 (n/a)</td><td>3312.28 (n/a)</td><td>3637.00 (n/a)</td><td>1946.20 (n/a)</td><td>807.07 (n/a)</td><td>275.86 (n/a)</td><td>173.36 (n/a)</td><td>147.61 (n/a)</td><td>138.15 (n/a)</td><td>58.38 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.77 (-0.95%)</td><td>4.11 (-17.95%)</td><td>4.04 <b>(-22.44%)</b></td><td>2.73 <b>(-33.71%)</b></td><td>1.37 <b>(+86.18%)</b></td><td>3265.70 <b>(+50.85%)</b></td><td>2378.34 <b>(+31.35%)</b></td><td>2204.60 <b>(+28.92%)</b></td><td>1545.40 (+0.95%)</td><td>801.48 <b>(+190.48%)</b></td><td>347.39 (-0.95%)</td><td>247.69 (-17.95%)</td><td>243.52 <b>(-22.44%)</b></td><td>164.40 <b>(-33.71%)</b></td><td>82.60 <b>(+86.18%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.82 (n/a)</td><td>5.01 (n/a)</td><td>5.21 (n/a)</td><td>4.12 (n/a)</td><td>0.74 (n/a)</td><td>2164.90 (n/a)</td><td>1810.74 (n/a)</td><td>1710.00 (n/a)</td><td>1530.80 (n/a)</td><td>275.92 (n/a)</td><td>350.71 (n/a)</td><td>301.88 (n/a)</td><td>313.96 (n/a)</td><td>247.99 (n/a)</td><td>44.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.80 (+7.08%)</td><td>5.86 (+5.77%)</td><td>6.53 <b>(+22.24%)</b></td><td>4.50 (+2.71%)</td><td>1.07 <b>(+30.56%)</b></td><td>7747.70 (-2.64%)</td><td>6130.84 (-4.45%)</td><td>5340.80 (-18.19%)</td><td>5128.20 (-6.61%)</td><td>1212.77 <b>(+20.25%)</b></td><td>418.76 (+7.08%)</td><td>360.70 (+5.77%)</td><td>402.09 <b>(+22.24%)</b></td><td>277.18 (+2.71%)</td><td>65.98 <b>(+30.56%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.35 (n/a)</td><td>5.54 (n/a)</td><td>5.34 (n/a)</td><td>4.38 (n/a)</td><td>0.82 (n/a)</td><td>7957.50 (n/a)</td><td>6416.20 (n/a)</td><td>6528.40 (n/a)</td><td>5491.20 (n/a)</td><td>1008.56 (n/a)</td><td>391.08 (n/a)</td><td>341.01 (n/a)</td><td>328.95 (n/a)</td><td>269.87 (n/a)</td><td>50.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.28 (-5.99%)</td><td>4.26 (-19.03%)</td><td>4.04 <b>(-24.72%)</b></td><td>3.75 (-18.27%)</td><td>0.63 <b>(+54.73%)</b></td><td>9299.40 <b>(+22.35%)</b></td><td>8307.66 <b>(+24.85%)</b></td><td>8632.80 <b>(+32.85%)</b></td><td>6600.10 (+6.37%)</td><td>1118.14 <b>(+99.91%)</b></td><td>325.37 (-5.99%)</td><td>262.68 (-19.03%)</td><td>248.76 <b>(-24.72%)</b></td><td>230.93 (-18.27%)</td><td>39.05 <b>(+54.73%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.62 (n/a)</td><td>5.27 (n/a)</td><td>5.37 (n/a)</td><td>4.59 (n/a)</td><td>0.41 (n/a)</td><td>7600.50 (n/a)</td><td>6654.34 (n/a)</td><td>6498.40 (n/a)</td><td>6204.70 (n/a)</td><td>559.32 (n/a)</td><td>346.10 (n/a)</td><td>324.41 (n/a)</td><td>330.46 (n/a)</td><td>282.54 (n/a)</td><td>25.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.80 (+4.20%)</td><td>6.19 (+3.26%)</td><td>5.90 (-3.75%)</td><td>5.71 (+11.98%)</td><td>0.52 (-6.45%)</td><td>6109.60 (-10.70%)</td><td>5663.22 (-3.35%)</td><td>5909.30 (+3.89%)</td><td>5130.90 (-4.03%)</td><td>464.68 <b>(-21.40%)</b></td><td>418.54 (+4.20%)</td><td>381.30 (+3.26%)</td><td>363.41 (-3.75%)</td><td>351.49 (+11.98%)</td><td>32.11 (-6.45%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.52 (n/a)</td><td>6.00 (n/a)</td><td>6.13 (n/a)</td><td>5.10 (n/a)</td><td>0.56 (n/a)</td><td>6841.40 (n/a)</td><td>5859.40 (n/a)</td><td>5687.90 (n/a)</td><td>5346.30 (n/a)</td><td>591.19 (n/a)</td><td>401.67 (n/a)</td><td>369.27 (n/a)</td><td>377.55 (n/a)</td><td>313.90 (n/a)</td><td>34.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.78 (-0.91%)</td><td>0.76 (-1.24%)</td><td>0.77 (-0.77%)</td><td>0.73 (-0.96%)</td><td>0.02 (+12.53%)</td><td>103310.10 (+0.96%)</td><td>99478.00 (+1.27%)</td><td>97677.90 (+0.77%)</td><td>96871.20 (+0.92%)</td><td>2919.36 (+14.43%)</td><td>709.39 (-0.91%)</td><td>691.27 (-1.24%)</td><td>703.53 (-0.77%)</td><td>665.18 (-0.96%)</td><td>20.05 (+12.53%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102323.40 (n/a)</td><td>98233.36 (n/a)</td><td>96928.40 (n/a)</td><td>95992.50 (n/a)</td><td>2551.21 (n/a)</td><td>715.88 (n/a)</td><td>699.92 (n/a)</td><td>708.97 (n/a)</td><td>671.59 (n/a)</td><td>17.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.77 (-1.90%)</td><td>0.76 (-1.47%)</td><td>0.76 (-0.42%)</td><td>0.74 (-2.44%)</td><td>0.01 <b>(+23.15%)</b></td><td>102145.80 (+2.51%)</td><td>99867.90 (+1.50%)</td><td>99245.20 (+0.43%)</td><td>98503.10 (+1.93%)</td><td>1510.28 <b>(+28.81%)</b></td><td>697.64 (-1.90%)</td><td>688.23 (-1.47%)</td><td>692.42 (-0.42%)</td><td>672.76 (-2.44%)</td><td>10.32 <b>(+23.15%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99648.90 (n/a)</td><td>98390.80 (n/a)</td><td>98824.50 (n/a)</td><td>96634.60 (n/a)</td><td>1172.53 (n/a)</td><td>711.13 (n/a)</td><td>698.51 (n/a)</td><td>695.37 (n/a)</td><td>689.62 (n/a)</td><td>8.38 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.82 (+0.59%)</td><td>0.81 (+0.96%)</td><td>0.81 (+1.27%)</td><td>0.80 (+1.45%)</td><td>0.01 <b>(-27.42%)</b></td><td>94487.40 (-1.43%)</td><td>93578.88 (-0.95%)</td><td>93530.60 (-1.26%)</td><td>92485.90 (-0.59%)</td><td>759.79 <b>(-28.86%)</b></td><td>743.03 (+0.59%)</td><td>734.39 (+0.96%)</td><td>734.73 (+1.27%)</td><td>727.29 (+1.45%)</td><td>5.98 <b>(-27.42%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95857.90 (n/a)</td><td>94477.70 (n/a)</td><td>94722.20 (n/a)</td><td>93031.70 (n/a)</td><td>1068.01 (n/a)</td><td>738.67 (n/a)</td><td>727.44 (n/a)</td><td>725.48 (n/a)</td><td>716.89 (n/a)</td><td>8.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.41 <b>(-31.32%)</b></td><td>1.76 <b>(-27.19%)</b></td><td>1.69 <b>(-22.57%)</b></td><td>1.34 <b>(-23.08%)</b></td><td>0.40 <b>(-40.48%)</b></td><td>6000.80 <b>(+30.01%)</b></td><td>4760.76 <b>(+35.07%)</b></td><td>4771.50 <b>(+29.14%)</b></td><td>3345.10 <b>(+45.60%)</b></td><td>950.14 (+13.04%)</td><td>631.95 <b>(-31.32%)</b></td><td>460.25 <b>(-27.19%)</b></td><td>443.03 <b>(-22.57%)</b></td><td>352.27 <b>(-23.08%)</b></td><td>103.65 <b>(-40.48%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.51 (n/a)</td><td>2.41 (n/a)</td><td>2.18 (n/a)</td><td>1.75 (n/a)</td><td>0.66 (n/a)</td><td>4615.60 (n/a)</td><td>3524.66 (n/a)</td><td>3694.80 (n/a)</td><td>2297.40 (n/a)</td><td>840.50 (n/a)</td><td>920.14 (n/a)</td><td>632.10 (n/a)</td><td>572.14 (n/a)</td><td>458.00 (n/a)</td><td>174.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.21 (+3.46%)</td><td>0.19 (+2.44%)</td><td>0.19 (+2.11%)</td><td>0.16 (-0.40%)</td><td>0.02 (+10.50%)</td><td>7807.90 (+0.40%)</td><td>6674.34 (-2.24%)</td><td>6402.90 (-2.06%)</td><td>5885.90 (-3.35%)</td><td>725.88 (+7.83%)</td><td>11.40 (+3.46%)</td><td>10.15 (+2.44%)</td><td>10.48 (+2.11%)</td><td>8.59 (-0.40%)</td><td>1.05 (+10.50%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>7777.10 (n/a)</td><td>6827.42 (n/a)</td><td>6537.80 (n/a)</td><td>6089.70 (n/a)</td><td>673.15 (n/a)</td><td>11.02 (n/a)</td><td>9.90 (n/a)</td><td>10.26 (n/a)</td><td>8.63 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.96 (n/a)</td><td>3.72 (n/a)</td><td>3.80 (n/a)</td><td>3.39 (n/a)</td><td>0.26 (n/a)</td><td>3.96 (n/a)</td><td>3.71 (n/a)</td><td>3.80 (n/a)</td><td>3.39 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>7.05 (+2.86%)</td><td>6.41 (+2.69%)</td><td>6.59 (+3.54%)</td><td>5.46 (-3.97%)</td><td>0.59 <b>(+21.97%)</b></td><td>7.05 (+2.86%)</td><td>6.41 (+2.69%)</td><td>6.58 (+3.54%)</td><td>5.46 (-3.97%)</td><td>0.59 <b>(+21.97%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.86 (n/a)</td><td>6.24 (n/a)</td><td>6.36 (n/a)</td><td>5.69 (n/a)</td><td>0.48 (n/a)</td><td>6.85 (n/a)</td><td>6.24 (n/a)</td><td>6.36 (n/a)</td><td>5.68 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>10.18 (+3.97%)</td><td>8.23 (-7.47%)</td><td>8.48 (-0.77%)</td><td>5.57 <b>(-31.13%)</b></td><td>1.66 <b>(+101.49%)</b></td><td>10.17 (+3.97%)</td><td>8.23 (-7.47%)</td><td>8.47 (-0.77%)</td><td>5.57 <b>(-31.13%)</b></td><td>1.66 <b>(+101.49%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>9.79 (n/a)</td><td>8.90 (n/a)</td><td>8.55 (n/a)</td><td>8.09 (n/a)</td><td>0.83 (n/a)</td><td>9.78 (n/a)</td><td>8.89 (n/a)</td><td>8.54 (n/a)</td><td>8.08 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.83 (n/a)</td><td>3.48 (n/a)</td><td>3.36 (n/a)</td><td>3.07 (n/a)</td><td>0.33 (n/a)</td><td>3.83 (n/a)</td><td>3.47 (n/a)</td><td>3.36 (n/a)</td><td>3.07 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>7.13 (+13.60%)</td><td>6.24 (+11.04%)</td><td>6.06 (+5.43%)</td><td>5.64 (+18.33%)</td><td>0.60 (+9.22%)</td><td>7.12 (+13.60%)</td><td>6.23 (+11.04%)</td><td>6.06 (+5.43%)</td><td>5.64 (+18.33%)</td><td>0.60 (+9.22%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.27 (n/a)</td><td>5.62 (n/a)</td><td>5.75 (n/a)</td><td>4.77 (n/a)</td><td>0.55 (n/a)</td><td>6.27 (n/a)</td><td>5.61 (n/a)</td><td>5.75 (n/a)</td><td>4.77 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>13.80 <b>(+27.52%)</b></td><td>10.20 (+11.45%)</td><td>8.86 (-0.14%)</td><td>6.93 (-9.97%)</td><td>3.12 <b>(+158.88%)</b></td><td>13.79 <b>(+27.52%)</b></td><td>10.20 (+11.45%)</td><td>8.85 (-0.14%)</td><td>6.93 (-9.97%)</td><td>3.12 <b>(+158.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>10.82 (n/a)</td><td>9.15 (n/a)</td><td>8.87 (n/a)</td><td>7.70 (n/a)</td><td>1.21 (n/a)</td><td>10.82 (n/a)</td><td>9.15 (n/a)</td><td>8.86 (n/a)</td><td>7.69 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.19 (+9.02%)</td><td>1.86 (-12.18%)</td><td>1.15 <b>(-57.45%)</b></td><td>1.04 (+1.25%)</td><td>1.06 (+5.41%)</td><td>3.19 (+9.02%)</td><td>1.86 (-12.18%)</td><td>1.15 <b>(-57.45%)</b></td><td>1.03 (+1.25%)</td><td>1.05 (+5.41%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.93 (n/a)</td><td>2.12 (n/a)</td><td>2.70 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>2.92 (n/a)</td><td>2.12 (n/a)</td><td>2.69 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.63 (+13.95%)</td><td>0.49 <b>(+23.11%)</b></td><td>0.53 (+3.80%)</td><td>0.35 <b>(+336.66%)</b></td><td>0.12 <b>(-41.57%)</b></td><td>0.62 (+13.95%)</td><td>0.48 <b>(+23.11%)</b></td><td>0.52 (+3.80%)</td><td>0.34 <b>(+336.66%)</b></td><td>0.11 <b>(-41.57%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.55 (n/a)</td><td>0.40 (n/a)</td><td>0.51 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.50 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.67 (-8.56%)</td><td>0.64 <b>(+32.08%)</b></td><td>0.65 (-0.87%)</td><td>0.61 <b>(+665.30%)</b></td><td>0.02 <b>(-92.49%)</b></td><td>0.66 (-8.56%)</td><td>0.63 <b>(+32.08%)</b></td><td>0.64 (-0.87%)</td><td>0.60 <b>(+665.30%)</b></td><td>0.02 <b>(-92.49%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.73 (n/a)</td><td>0.49 (n/a)</td><td>0.65 (n/a)</td><td>0.08 (n/a)</td><td>0.29 (n/a)</td><td>0.72 (n/a)</td><td>0.48 (n/a)</td><td>0.65 (n/a)</td><td>0.08 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.62 (+4.51%)</td><td>1.73 (+12.07%)</td><td>2.10 (+10.36%)</td><td>0.80 <b>(+77.06%)</b></td><td>0.86 (-15.92%)</td><td>2.57 (+4.51%)</td><td>1.71 (+12.07%)</td><td>2.07 (+10.36%)</td><td>0.79 <b>(+77.06%)</b></td><td>0.84 (-15.92%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.50 (n/a)</td><td>1.55 (n/a)</td><td>1.90 (n/a)</td><td>0.45 (n/a)</td><td>1.02 (n/a)</td><td>2.46 (n/a)</td><td>1.52 (n/a)</td><td>1.87 (n/a)</td><td>0.45 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>363.20 (n/a)</td><td>274.66 (n/a)</td><td>251.50 (n/a)</td><td>216.10 (n/a)</td><td>64.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.30 (n/a)</td><td>404.08 (n/a)</td><td>417.10 (n/a)</td><td>237.60 (n/a)</td><td>114.32 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>457.40 (n/a)</td><td>333.24 (n/a)</td><td>324.50 (n/a)</td><td>254.20 (n/a)</td><td>76.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2429.50 (n/a)</td><td>791.46 (n/a)</td><td>485.40 (n/a)</td><td>224.20 (n/a)</td><td>924.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1779.60 (n/a)</td><td>639.14 (n/a)</td><td>390.60 (n/a)</td><td>251.80 (n/a)</td><td>642.50 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>665.20 (n/a)</td><td>445.54 (n/a)</td><td>541.40 (n/a)</td><td>195.70 (n/a)</td><td>214.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.50 (n/a)</td><td>369.78 (n/a)</td><td>405.90 (n/a)</td><td>235.00 (n/a)</td><td>109.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.10 (n/a)</td><td>435.98 (n/a)</td><td>465.90 (n/a)</td><td>234.30 (n/a)</td><td>119.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>409.10 (n/a)</td><td>450.30 (n/a)</td><td>295.80 (n/a)</td><td>96.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2140.40 (n/a)</td><td>789.98 (n/a)</td><td>545.70 (n/a)</td><td>285.70 (n/a)</td><td>767.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.30 (n/a)</td><td>432.52 (n/a)</td><td>419.40 (n/a)</td><td>290.10 (n/a)</td><td>106.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.50 (n/a)</td><td>413.96 (n/a)</td><td>469.10 (n/a)</td><td>181.40 (n/a)</td><td>149.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.90 (n/a)</td><td>464.10 (n/a)</td><td>504.40 (n/a)</td><td>281.00 (n/a)</td><td>160.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>595.30 (n/a)</td><td>345.98 (n/a)</td><td>287.40 (n/a)</td><td>232.90 (n/a)</td><td>148.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>478.70 (n/a)</td><td>371.86 (n/a)</td><td>394.70 (n/a)</td><td>230.80 (n/a)</td><td>114.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1971.70 (n/a)</td><td>720.48 (n/a)</td><td>526.60 (n/a)</td><td>210.50 (n/a)</td><td>717.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>593.00 (n/a)</td><td>487.22 (n/a)</td><td>576.40 (n/a)</td><td>336.90 (n/a)</td><td>132.93 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.70 (n/a)</td><td>409.78 (n/a)</td><td>432.70 (n/a)</td><td>241.60 (n/a)</td><td>134.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>516.80 (n/a)</td><td>386.02 (n/a)</td><td>410.90 (n/a)</td><td>245.00 (n/a)</td><td>121.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>501.90 (n/a)</td><td>365.80 (n/a)</td><td>352.10 (n/a)</td><td>202.20 (n/a)</td><td>119.57 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1319.40 (n/a)</td><td>616.62 (n/a)</td><td>501.40 (n/a)</td><td>251.40 (n/a)</td><td>407.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>536.80 (n/a)</td><td>363.32 (n/a)</td><td>303.40 (n/a)</td><td>203.30 (n/a)</td><td>152.74 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>627.70 (n/a)</td><td>414.26 (n/a)</td><td>359.90 (n/a)</td><td>208.10 (n/a)</td><td>189.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>954.10 (n/a)</td><td>637.82 (n/a)</td><td>608.30 (n/a)</td><td>408.60 (n/a)</td><td>197.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+12.95%)</td><td>0.02 <b>(+40.79%)</b></td><td>0.02 <b>(+59.67%)</b></td><td>0.01 <b>(+66.54%)</b></td><td>0.00 <b>(-55.23%)</b></td><td>293.30 <b>(-39.96%)</b></td><td>254.48 <b>(-32.10%)</b></td><td>243.80 <b>(-37.37%)</b></td><td>239.20 (-11.44%)</td><td>22.55 <b>(-75.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.50 (n/a)</td><td>374.80 (n/a)</td><td>389.30 (n/a)</td><td>270.10 (n/a)</td><td>92.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-13.48%)</td><td>0.01 (-16.64%)</td><td>0.01 (-19.79%)</td><td>0.01 <b>(-40.02%)</b></td><td>0.00 (+13.24%)</td><td>785.70 <b>(+66.71%)</b></td><td>475.26 <b>(+27.27%)</b></td><td>444.90 <b>(+24.66%)</b></td><td>316.00 (+15.58%)</td><td>190.29 <b>(+107.33%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.30 (n/a)</td><td>373.42 (n/a)</td><td>356.90 (n/a)</td><td>273.40 (n/a)</td><td>91.78 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+1.37%)</td><td>0.01 <b>(+33.08%)</b></td><td>0.01 <b>(+87.24%)</b></td><td>0.01 (+1.89%)</td><td>0.00 (-1.47%)</td><td>650.00 (-1.86%)</td><td>381.82 <b>(-24.77%)</b></td><td>300.50 <b>(-46.60%)</b></td><td>261.40 (-1.36%)</td><td>158.76 (+2.81%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>662.30 (n/a)</td><td>507.52 (n/a)</td><td>562.70 (n/a)</td><td>265.00 (n/a)</td><td>154.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(+41.68%)</b></td><td>0.01 <b>(+32.53%)</b></td><td>0.01 <b>(+27.51%)</b></td><td>0.01 (+2.17%)</td><td>0.00 <b>(+110.29%)</b></td><td>642.20 (-2.12%)</td><td>398.34 (-16.78%)</td><td>353.90 <b>(-21.56%)</b></td><td>236.80 <b>(-29.44%)</b></td><td>176.87 <b>(+37.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>656.10 (n/a)</td><td>478.64 (n/a)</td><td>451.20 (n/a)</td><td>335.60 (n/a)</td><td>128.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (+12.31%)</td><td>0.01 (+8.98%)</td><td>0.01 (+8.23%)</td><td>0.01 (+17.35%)</td><td>0.00 (+10.05%)</td><td>464.70 (-14.80%)</td><td>367.12 (-8.44%)</td><td>347.00 (-7.59%)</td><td>281.20 (-10.98%)</td><td>81.18 (-14.36%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.40 (n/a)</td><td>400.98 (n/a)</td><td>375.50 (n/a)</td><td>315.90 (n/a)</td><td>94.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(+29.97%)</b></td><td>0.01 (+8.22%)</td><td>0.01 (+0.27%)</td><td>0.01 (-10.94%)</td><td>0.01 <b>(+64.11%)</b></td><td>670.40 (+12.28%)</td><td>470.32 (-0.31%)</td><td>503.30 (-0.28%)</td><td>213.70 <b>(-23.05%)</b></td><td>164.65 <b>(+34.73%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.10 (n/a)</td><td>471.78 (n/a)</td><td>504.70 (n/a)</td><td>277.70 (n/a)</td><td>122.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 <b>(-25.57%)</b></td><td>0.03 (-15.74%)</td><td>0.03 (-5.68%)</td><td>0.01 <b>(-20.88%)</b></td><td>0.01 (-12.20%)</td><td>593.20 <b>(+26.37%)</b></td><td>377.02 <b>(+22.77%)</b></td><td>242.70 (+6.03%)</td><td>235.70 <b>(+34.38%)</b></td><td>187.88 <b>(+39.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.40 (n/a)</td><td>307.10 (n/a)</td><td>228.90 (n/a)</td><td>175.40 (n/a)</td><td>134.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 <b>(+30.49%)</b></td><td>0.03 <b>(+22.07%)</b></td><td>0.03 <b>(+29.43%)</b></td><td>0.02 (+8.57%)</td><td>0.01 <b>(+63.00%)</b></td><td>423.20 (-7.88%)</td><td>277.86 (-15.84%)</td><td>239.40 <b>(-22.75%)</b></td><td>209.40 <b>(-23.38%)</b></td><td>84.86 (+14.97%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>459.40 (n/a)</td><td>330.16 (n/a)</td><td>309.90 (n/a)</td><td>273.30 (n/a)</td><td>73.81 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (-4.01%)</td><td>0.03 <b>(+21.17%)</b></td><td>0.03 <b>(+59.24%)</b></td><td>0.01 (-18.62%)</td><td>0.01 (+3.02%)</td><td>589.40 <b>(+22.87%)</b></td><td>326.60 (-14.87%)</td><td>277.10 <b>(-37.19%)</b></td><td>233.60 (+4.15%)</td><td>149.04 <b>(+35.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.70 (n/a)</td><td>383.64 (n/a)</td><td>441.20 (n/a)</td><td>224.30 (n/a)</td><td>109.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (+3.68%)</td><td>0.03 <b>(+42.84%)</b></td><td>0.03 <b>(+74.82%)</b></td><td>0.01 <b>(+289.78%)</b></td><td>0.01 (-16.94%)</td><td>551.90 <b>(-74.34%)</b></td><td>367.94 <b>(-52.64%)</b></td><td>293.30 <b>(-42.80%)</b></td><td>224.90 (-3.52%)</td><td>148.17 <b>(-80.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2151.20 (n/a)</td><td>776.96 (n/a)</td><td>512.80 (n/a)</td><td>233.10 (n/a)</td><td>777.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+11.60%)</td><td>0.02 (-8.50%)</td><td>0.02 <b>(-30.27%)</b></td><td>0.02 (+12.34%)</td><td>0.01 <b>(+32.58%)</b></td><td>494.30 (-10.99%)</td><td>371.32 (+11.96%)</td><td>402.50 <b>(+43.44%)</b></td><td>236.30 (-10.39%)</td><td>125.26 (-0.13%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.30 (n/a)</td><td>331.66 (n/a)</td><td>280.60 (n/a)</td><td>263.70 (n/a)</td><td>125.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 <b>(+42.46%)</b></td><td>0.02 (+11.07%)</td><td>0.02 (-5.41%)</td><td>0.01 (-18.98%)</td><td>0.01 <b>(+296.67%)</b></td><td>603.20 <b>(+23.43%)</b></td><td>435.64 (+0.21%)</td><td>462.40 (+5.72%)</td><td>256.30 <b>(-29.82%)</b></td><td>155.17 <b>(+249.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>488.70 (n/a)</td><td>434.72 (n/a)</td><td>437.40 (n/a)</td><td>365.20 (n/a)</td><td>44.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+14.92%)</td><td>0.03 <b>(+39.16%)</b></td><td>0.03 <b>(+91.08%)</b></td><td>0.01 (+13.70%)</td><td>0.01 <b>(+36.12%)</b></td><td>553.10 (-12.05%)</td><td>359.12 <b>(-25.46%)</b></td><td>276.90 <b>(-47.67%)</b></td><td>242.70 (-12.98%)</td><td>142.23 (+8.36%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.90 (n/a)</td><td>481.78 (n/a)</td><td>529.10 (n/a)</td><td>278.90 (n/a)</td><td>131.26 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-13.45%)</td><td>0.02 (-12.01%)</td><td>0.02 (-6.03%)</td><td>0.01 (-2.72%)</td><td>0.00 (-15.98%)</td><td>668.70 (+2.80%)</td><td>529.16 (+12.77%)</td><td>506.50 (+6.41%)</td><td>332.20 (+15.51%)</td><td>133.27 (+3.28%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.50 (n/a)</td><td>469.22 (n/a)</td><td>476.00 (n/a)</td><td>287.60 (n/a)</td><td>129.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-16.50%)</td><td>0.05 (-15.15%)</td><td>0.04 <b>(-40.11%)</b></td><td>0.03 <b>(+204.22%)</b></td><td>0.02 <b>(-37.93%)</b></td><td>595.80 <b>(-67.13%)</b></td><td>406.04 <b>(-29.38%)</b></td><td>453.30 <b>(+66.96%)</b></td><td>245.20 (+19.79%)</td><td>146.04 <b>(-78.96%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1812.40 (n/a)</td><td>574.94 (n/a)</td><td>271.50 (n/a)</td><td>204.70 (n/a)</td><td>694.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (-11.69%)</td><td>0.04 (-17.33%)</td><td>0.04 <b>(-39.22%)</b></td><td>0.03 (+2.87%)</td><td>0.01 <b>(-27.04%)</b></td><td>526.30 (-2.79%)</td><td>420.48 (+16.07%)</td><td>452.90 <b>(+64.51%)</b></td><td>286.60 (+13.24%)</td><td>114.00 (-17.53%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.40 (n/a)</td><td>362.26 (n/a)</td><td>275.30 (n/a)</td><td>253.10 (n/a)</td><td>138.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+11.05%)</td><td>0.05 (-6.82%)</td><td>0.05 (-15.59%)</td><td>0.03 <b>(-25.46%)</b></td><td>0.02 (+19.78%)</td><td>626.10 <b>(+34.15%)</b></td><td>377.42 (+12.92%)</td><td>308.50 (+18.47%)</td><td>227.20 (-9.95%)</td><td>159.22 <b>(+50.26%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>466.70 (n/a)</td><td>334.24 (n/a)</td><td>260.40 (n/a)</td><td>252.30 (n/a)</td><td>105.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 <b>(+28.09%)</b></td><td>0.05 <b>(+24.17%)</b></td><td>0.06 <b>(+46.98%)</b></td><td>0.03 (+8.96%)</td><td>0.02 <b>(+61.23%)</b></td><td>517.30 (-8.23%)</td><td>353.48 (-13.58%)</td><td>294.60 <b>(-31.96%)</b></td><td>206.90 <b>(-21.92%)</b></td><td>149.98 <b>(+26.08%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>563.70 (n/a)</td><td>409.04 (n/a)</td><td>433.00 (n/a)</td><td>265.00 (n/a)</td><td>118.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 <b>(-27.12%)</b></td><td>0.05 (-6.90%)</td><td>0.05 <b>(+51.86%)</b></td><td>0.03 (-17.68%)</td><td>0.02 <b>(-30.57%)</b></td><td>629.30 <b>(+21.49%)</b></td><td>391.46 (+3.82%)</td><td>300.50 <b>(-34.16%)</b></td><td>255.20 <b>(+37.20%)</b></td><td>166.59 (+11.70%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>518.00 (n/a)</td><td>377.06 (n/a)</td><td>456.40 (n/a)</td><td>186.00 (n/a)</td><td>149.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 <b>(+61.19%)</b></td><td>0.05 <b>(+29.11%)</b></td><td>0.04 (+11.23%)</td><td>0.02 (-5.81%)</td><td>0.02 <b>(+141.10%)</b></td><td>657.90 (+6.18%)</td><td>403.32 (-14.67%)</td><td>394.40 (-10.10%)</td><td>213.10 <b>(-37.96%)</b></td><td>166.09 <b>(+56.37%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>619.60 (n/a)</td><td>472.64 (n/a)</td><td>438.70 (n/a)</td><td>343.50 (n/a)</td><td>106.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (+0.84%)</td><td>0.09 (-4.34%)</td><td>0.09 (+19.63%)</td><td>0.05 (-15.29%)</td><td>0.04 (+8.01%)</td><td>644.20 (+18.05%)</td><td>430.48 (+8.12%)</td><td>374.10 (-16.40%)</td><td>232.80 (-0.85%)</td><td>165.20 <b>(+31.39%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>545.70 (n/a)</td><td>398.14 (n/a)</td><td>447.50 (n/a)</td><td>234.80 (n/a)</td><td>125.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (+14.89%)</td><td>0.11 <b>(+23.40%)</b></td><td>0.12 <b>(+52.72%)</b></td><td>0.06 (-13.42%)</td><td>0.03 <b>(+20.97%)</b></td><td>578.40 (+15.50%)</td><td>327.18 (-15.87%)</td><td>273.70 <b>(-34.51%)</b></td><td>236.70 (-12.98%)</td><td>141.66 <b>(+33.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>500.80 (n/a)</td><td>388.88 (n/a)</td><td>417.90 (n/a)</td><td>272.00 (n/a)</td><td>105.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.23 <b>(+132.42%)</b></td><td>0.13 <b>(+119.36%)</b></td><td>0.11 <b>(+97.84%)</b></td><td>0.08 <b>(+339.48%)</b></td><td>0.06 <b>(+98.05%)</b></td><td>422.40 <b>(-77.24%)</b></td><td>282.88 <b>(-62.96%)</b></td><td>287.60 <b>(-49.45%)</b></td><td>143.30 <b>(-56.99%)</b></td><td>99.13 <b>(-83.97%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1856.20 (n/a)</td><td>763.68 (n/a)</td><td>568.90 (n/a)</td><td>333.20 (n/a)</td><td>618.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (-1.34%)</td><td>0.09 (+16.78%)</td><td>0.09 <b>(+26.90%)</b></td><td>0.07 <b>(+41.46%)</b></td><td>0.03 <b>(-26.46%)</b></td><td>461.10 <b>(-29.31%)</b></td><td>376.68 <b>(-20.34%)</b></td><td>384.70 <b>(-21.18%)</b></td><td>240.30 (+1.35%)</td><td>82.97 <b>(-47.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>652.30 (n/a)</td><td>472.86 (n/a)</td><td>488.10 (n/a)</td><td>237.10 (n/a)</td><td>158.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 <b>(-31.70%)</b></td><td>0.07 (-7.50%)</td><td>0.07 (+12.90%)</td><td>0.05 <b>(+94.50%)</b></td><td>0.02 <b>(-59.28%)</b></td><td>704.90 <b>(-48.59%)</b></td><td>486.18 (-19.03%)</td><td>457.90 (-11.43%)</td><td>374.20 <b>(+46.40%)</b></td><td>135.98 <b>(-69.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1371.10 (n/a)</td><td>600.44 (n/a)</td><td>517.00 (n/a)</td><td>255.60 (n/a)</td><td>451.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(-24.99%)</b></td><td>0.01 <b>(-22.24%)</b></td><td>0.01 (-12.61%)</td><td>0.01 (-4.75%)</td><td>0.00 <b>(-42.30%)</b></td><td>559.40 (+4.97%)</td><td>384.46 (+17.28%)</td><td>312.10 (+14.45%)</td><td>241.50 <b>(+33.35%)</b></td><td>137.08 (-14.69%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>532.90 (n/a)</td><td>327.80 (n/a)</td><td>272.70 (n/a)</td><td>181.10 (n/a)</td><td>160.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-14.91%)</td><td>0.01 (-14.84%)</td><td>0.02 (-6.33%)</td><td>0.01 <b>(-26.99%)</b></td><td>0.00 (+15.75%)</td><td>489.70 <b>(+36.94%)</b></td><td>322.64 <b>(+22.43%)</b></td><td>271.00 (+6.73%)</td><td>227.80 (+17.54%)</td><td>108.75 <b>(+84.01%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>357.60 (n/a)</td><td>263.52 (n/a)</td><td>253.90 (n/a)</td><td>193.80 (n/a)</td><td>59.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(-22.34%)</b></td><td>0.01 <b>(-20.09%)</b></td><td>0.01 <b>(-33.70%)</b></td><td>0.01 (-12.87%)</td><td>0.00 <b>(-29.88%)</b></td><td>689.20 (+14.77%)</td><td>447.52 (+19.72%)</td><td>477.20 <b>(+50.82%)</b></td><td>268.00 <b>(+28.78%)</b></td><td>164.27 (-0.49%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.50 (n/a)</td><td>373.82 (n/a)</td><td>316.40 (n/a)</td><td>208.10 (n/a)</td><td>165.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-3.54%)</td><td>0.01 (+8.91%)</td><td>0.01 <b>(+32.48%)</b></td><td>0.01 (+0.72%)</td><td>0.00 (+2.17%)</td><td>505.00 (-0.71%)</td><td>358.42 (-7.81%)</td><td>292.20 <b>(-24.52%)</b></td><td>267.00 (+3.65%)</td><td>109.64 (+3.07%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.60 (n/a)</td><td>388.78 (n/a)</td><td>387.10 (n/a)</td><td>257.60 (n/a)</td><td>106.38 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 <b>(+28.16%)</b></td><td>0.01 (+16.42%)</td><td>0.01 (+4.11%)</td><td>0.01 (+13.44%)</td><td>0.00 <b>(+93.23%)</b></td><td>522.10 (-11.85%)</td><td>405.56 (-9.93%)</td><td>431.00 (-3.94%)</td><td>274.80 <b>(-21.98%)</b></td><td>121.33 <b>(+31.05%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.30 (n/a)</td><td>450.28 (n/a)</td><td>448.70 (n/a)</td><td>352.20 (n/a)</td><td>92.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-3.20%)</td><td>0.01 (-16.99%)</td><td>0.01 (-14.07%)</td><td>0.01 <b>(-34.01%)</b></td><td>0.00 <b>(+215.61%)</b></td><td>409.90 <b>(+51.53%)</b></td><td>317.90 <b>(+24.24%)</b></td><td>299.20 (+16.37%)</td><td>244.90 (+3.33%)</td><td>65.50 <b>(+399.15%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.50 (n/a)</td><td>255.88 (n/a)</td><td>257.10 (n/a)</td><td>237.00 (n/a)</td><td>13.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+8.42%)</td><td>0.01 (-4.54%)</td><td>0.01 (+3.39%)</td><td>0.00 <b>(-46.79%)</b></td><td>0.01 <b>(+58.85%)</b></td><td>1126.00 <b>(+87.95%)</b></td><td>501.38 <b>(+32.70%)</b></td><td>297.90 (-3.28%)</td><td>239.70 (-7.77%)</td><td>372.80 <b>(+170.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.10 (n/a)</td><td>377.82 (n/a)</td><td>308.00 (n/a)</td><td>259.90 (n/a)</td><td>137.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-2.13%)</td><td>0.01 (+12.29%)</td><td>0.01 <b>(+23.85%)</b></td><td>0.01 (+8.43%)</td><td>0.00 (+3.31%)</td><td>501.90 (-7.77%)</td><td>381.42 (-10.76%)</td><td>350.10 (-19.28%)</td><td>299.30 (+2.19%)</td><td>89.93 (+0.24%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.20 (n/a)</td><td>427.42 (n/a)</td><td>433.70 (n/a)</td><td>292.90 (n/a)</td><td>89.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-3.48%)</td><td>0.01 (+1.37%)</td><td>0.01 (+6.73%)</td><td>0.01 (+10.32%)</td><td>0.00 (-10.59%)</td><td>542.70 (-9.37%)</td><td>432.00 (-4.00%)</td><td>437.80 (-6.31%)</td><td>232.80 (+3.60%)</td><td>126.14 (-15.01%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.80 (n/a)</td><td>449.98 (n/a)</td><td>467.30 (n/a)</td><td>224.70 (n/a)</td><td>148.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (+0.97%)</td><td>0.01 (+0.83%)</td><td>0.01 <b>(-21.79%)</b></td><td>0.01 (+18.04%)</td><td>0.00 (-8.44%)</td><td>487.00 (-15.29%)</td><td>388.46 (-3.16%)</td><td>424.90 <b>(+27.87%)</b></td><td>276.80 (-0.97%)</td><td>95.50 <b>(-25.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.90 (n/a)</td><td>401.12 (n/a)</td><td>332.30 (n/a)</td><td>279.50 (n/a)</td><td>128.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-2.37%)</td><td>0.01 (-10.38%)</td><td>0.01 (+4.85%)</td><td>0.00 <b>(-72.73%)</b></td><td>0.00 <b>(+38.18%)</b></td><td>2238.60 <b>(+266.74%)</b></td><td>815.72 <b>(+64.39%)</b></td><td>514.20 (-4.64%)</td><td>290.40 (+2.43%)</td><td>801.92 <b>(+538.24%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.40 (n/a)</td><td>496.22 (n/a)</td><td>539.20 (n/a)</td><td>283.50 (n/a)</td><td>125.64 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (-0.85%)</td><td>0.01 (-4.22%)</td><td>0.01 (-1.07%)</td><td>0.01 <b>(+25.31%)</b></td><td>0.00 <b>(-29.17%)</b></td><td>585.70 <b>(-20.20%)</b></td><td>478.34 (-0.83%)</td><td>478.60 (+1.10%)</td><td>331.20 (+0.85%)</td><td>100.71 <b>(-40.10%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>734.00 (n/a)</td><td>482.34 (n/a)</td><td>473.40 (n/a)</td><td>328.40 (n/a)</td><td>168.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+15.98%)</td><td>0.03 (+4.30%)</td><td>0.03 (-1.49%)</td><td>0.01 (-15.36%)</td><td>0.01 <b>(+24.34%)</b></td><td>566.10 (+18.13%)</td><td>359.34 (-1.06%)</td><td>296.00 (+1.51%)</td><td>240.30 (-13.78%)</td><td>132.29 <b>(+26.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.20 (n/a)</td><td>363.18 (n/a)</td><td>291.60 (n/a)</td><td>278.70 (n/a)</td><td>104.93 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (-7.71%)</td><td>0.03 (-13.22%)</td><td>0.03 (-6.66%)</td><td>0.01 (-17.92%)</td><td>0.01 (+2.10%)</td><td>593.50 <b>(+21.84%)</b></td><td>356.30 (+18.40%)</td><td>291.30 (+7.10%)</td><td>237.00 (+8.32%)</td><td>144.98 <b>(+33.52%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.10 (n/a)</td><td>300.94 (n/a)</td><td>272.00 (n/a)</td><td>218.80 (n/a)</td><td>108.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+0.45%)</td><td>0.03 <b>(+60.04%)</b></td><td>0.03 <b>(+84.81%)</b></td><td>0.02 <b>(+348.79%)</b></td><td>0.01 <b>(-39.82%)</b></td><td>424.20 <b>(-77.72%)</b></td><td>284.20 <b>(-59.45%)</b></td><td>240.80 <b>(-45.89%)</b></td><td>234.70 (-0.47%)</td><td>81.21 <b>(-88.10%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1903.80 (n/a)</td><td>700.84 (n/a)</td><td>445.00 (n/a)</td><td>235.80 (n/a)</td><td>682.70 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+9.51%)</td><td>0.03 (-6.15%)</td><td>0.03 (-5.90%)</td><td>0.01 <b>(-41.02%)</b></td><td>0.01 <b>(+67.08%)</b></td><td>750.80 <b>(+69.56%)</b></td><td>381.00 <b>(+21.16%)</b></td><td>284.20 (+6.28%)</td><td>240.60 (-8.69%)</td><td>212.09 <b>(+174.64%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>442.80 (n/a)</td><td>314.46 (n/a)</td><td>267.40 (n/a)</td><td>263.50 (n/a)</td><td>77.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (-8.33%)</td><td>0.02 (+17.47%)</td><td>0.02 <b>(+50.11%)</b></td><td>0.01 (+7.34%)</td><td>0.01 (-10.40%)</td><td>623.00 (-6.83%)</td><td>393.44 (-16.38%)</td><td>330.10 <b>(-33.38%)</b></td><td>282.00 (+9.09%)</td><td>144.66 (-9.15%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.70 (n/a)</td><td>470.52 (n/a)</td><td>495.50 (n/a)</td><td>258.50 (n/a)</td><td>159.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+8.29%)</td><td>0.03 (+4.97%)</td><td>0.03 (-9.52%)</td><td>0.02 (+18.84%)</td><td>0.01 <b>(-23.61%)</b></td><td>462.20 (-15.86%)</td><td>335.72 (-9.49%)</td><td>319.10 (+10.49%)</td><td>242.90 (-7.68%)</td><td>82.07 <b>(-39.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.30 (n/a)</td><td>370.94 (n/a)</td><td>288.80 (n/a)</td><td>263.10 (n/a)</td><td>134.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 <b>(-22.57%)</b></td><td>0.02 (-15.66%)</td><td>0.02 (+6.45%)</td><td>0.00 <b>(-75.39%)</b></td><td>0.01 (-1.99%)</td><td>2417.80 <b>(+306.42%)</b></td><td>783.02 <b>(+95.10%)</b></td><td>377.90 (-6.07%)</td><td>233.00 <b>(+29.16%)</b></td><td>924.31 <b>(+471.63%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.90 (n/a)</td><td>401.34 (n/a)</td><td>402.30 (n/a)</td><td>180.40 (n/a)</td><td>161.70 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (-14.03%)</td><td>0.02 (-13.16%)</td><td>0.02 (+2.95%)</td><td>0.01 <b>(-31.09%)</b></td><td>0.01 (-2.82%)</td><td>790.50 <b>(+45.10%)</b></td><td>469.30 <b>(+20.92%)</b></td><td>399.00 (-2.87%)</td><td>279.30 (+16.33%)</td><td>204.29 <b>(+69.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.80 (n/a)</td><td>388.12 (n/a)</td><td>410.80 (n/a)</td><td>240.10 (n/a)</td><td>120.32 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 <b>(+34.32%)</b></td><td>0.02 (+0.48%)</td><td>0.02 <b>(-20.40%)</b></td><td>0.01 (-14.32%)</td><td>0.01 <b>(+66.74%)</b></td><td>572.30 (+16.70%)</td><td>424.78 (+11.16%)</td><td>528.50 <b>(+25.62%)</b></td><td>187.90 <b>(-25.55%)</b></td><td>175.17 <b>(+52.74%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.40 (n/a)</td><td>382.14 (n/a)</td><td>420.70 (n/a)</td><td>252.40 (n/a)</td><td>114.69 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 <b>(-21.42%)</b></td><td>0.02 (-15.57%)</td><td>0.03 (-0.90%)</td><td>0.02 (-6.06%)</td><td>0.01 <b>(-29.69%)</b></td><td>519.40 (+6.43%)</td><td>360.90 (+15.47%)</td><td>307.00 (+0.89%)</td><td>267.90 <b>(+27.27%)</b></td><td>102.88 (-4.78%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>488.00 (n/a)</td><td>312.56 (n/a)</td><td>304.30 (n/a)</td><td>210.50 (n/a)</td><td>108.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(+23.51%)</b></td><td>0.02 <b>(+20.89%)</b></td><td>0.02 (-2.27%)</td><td>0.02 <b>(+262.44%)</b></td><td>0.00 <b>(-50.08%)</b></td><td>530.00 <b>(-72.41%)</b></td><td>458.60 <b>(-39.09%)</b></td><td>477.00 (+2.32%)</td><td>358.90 (-19.04%)</td><td>70.25 <b>(-89.24%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1921.10 (n/a)</td><td>752.90 (n/a)</td><td>466.20 (n/a)</td><td>443.30 (n/a)</td><td>653.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+0.78%)</td><td>0.02 (-0.59%)</td><td>0.03 (-3.01%)</td><td>0.01 (-3.87%)</td><td>0.01 (-11.15%)</td><td>579.90 (+4.02%)</td><td>364.08 (-0.62%)</td><td>319.90 (+3.09%)</td><td>253.10 (-0.75%)</td><td>126.88 (-2.00%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.50 (n/a)</td><td>366.36 (n/a)</td><td>310.30 (n/a)</td><td>255.00 (n/a)</td><td>129.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+15.16%)</td><td>0.04 (-11.23%)</td><td>0.04 (-18.61%)</td><td>0.01 <b>(-74.85%)</b></td><td>0.02 <b>(+90.80%)</b></td><td>1909.70 <b>(+297.61%)</b></td><td>663.66 <b>(+82.05%)</b></td><td>401.80 <b>(+22.84%)</b></td><td>226.20 (-13.13%)</td><td>703.98 <b>(+600.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>480.30 (n/a)</td><td>364.54 (n/a)</td><td>327.10 (n/a)</td><td>260.40 (n/a)</td><td>100.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-3.71%)</td><td>0.06 (+6.17%)</td><td>0.06 (+4.58%)</td><td>0.03 (-2.06%)</td><td>0.01 (-18.41%)</td><td>539.00 (+2.12%)</td><td>321.72 (-8.10%)</td><td>275.30 (-4.38%)</td><td>243.00 (+3.85%)</td><td>122.35 (-7.42%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>527.80 (n/a)</td><td>350.06 (n/a)</td><td>287.90 (n/a)</td><td>234.00 (n/a)</td><td>132.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+8.05%)</td><td>0.05 (+16.20%)</td><td>0.03 (-5.70%)</td><td>0.03 <b>(+128.79%)</b></td><td>0.02 (-4.36%)</td><td>558.10 <b>(-56.29%)</b></td><td>414.26 <b>(-28.08%)</b></td><td>488.50 (+6.06%)</td><td>229.10 (-7.43%)</td><td>160.57 <b>(-61.39%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1276.80 (n/a)</td><td>576.00 (n/a)</td><td>460.60 (n/a)</td><td>247.50 (n/a)</td><td>415.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-1.13%)</td><td>0.05 (+14.57%)</td><td>0.05 <b>(+20.95%)</b></td><td>0.04 <b>(+354.26%)</b></td><td>0.01 <b>(-47.16%)</b></td><td>438.90 <b>(-77.99%)</b></td><td>348.42 <b>(-47.86%)</b></td><td>331.40 (-17.34%)</td><td>245.40 (+1.11%)</td><td>84.58 <b>(-88.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1993.80 (n/a)</td><td>668.30 (n/a)</td><td>400.90 (n/a)</td><td>242.70 (n/a)</td><td>745.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-14.04%)</td><td>0.06 (+0.99%)</td><td>0.06 (+3.02%)</td><td>0.04 <b>(+22.59%)</b></td><td>0.01 <b>(-55.90%)</b></td><td>378.80 (-18.41%)</td><td>298.40 (-8.56%)</td><td>286.50 (-2.91%)</td><td>247.30 (+16.32%)</td><td>48.79 <b>(-57.50%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>464.30 (n/a)</td><td>326.32 (n/a)</td><td>295.10 (n/a)</td><td>212.60 (n/a)</td><td>114.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+10.00%)</td><td>0.06 <b>(+22.35%)</b></td><td>0.06 (+12.35%)</td><td>0.05 <b>(+51.93%)</b></td><td>0.01 <b>(-48.25%)</b></td><td>311.80 <b>(-34.18%)</b></td><td>276.30 <b>(-22.74%)</b></td><td>272.40 (-11.01%)</td><td>230.90 (-9.09%)</td><td>30.50 <b>(-70.96%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.70 (n/a)</td><td>357.62 (n/a)</td><td>306.10 (n/a)</td><td>254.00 (n/a)</td><td>105.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (-12.25%)</td><td>0.05 <b>(-20.89%)</b></td><td>0.05 <b>(-24.84%)</b></td><td>0.03 (-8.57%)</td><td>0.01 (-8.62%)</td><td>549.50 (+9.38%)</td><td>390.88 <b>(+26.52%)</b></td><td>347.40 <b>(+33.05%)</b></td><td>276.20 (+13.94%)</td><td>122.17 (+11.10%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>502.40 (n/a)</td><td>308.94 (n/a)</td><td>261.10 (n/a)</td><td>242.40 (n/a)</td><td>109.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+4.67%)</td><td>0.05 (-14.78%)</td><td>0.05 <b>(-23.78%)</b></td><td>0.03 (-3.27%)</td><td>0.02 (+2.77%)</td><td>648.50 (+3.38%)</td><td>389.14 (+17.67%)</td><td>321.00 <b>(+31.18%)</b></td><td>229.60 (-4.45%)</td><td>170.88 (+1.91%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.30 (n/a)</td><td>330.70 (n/a)</td><td>244.70 (n/a)</td><td>240.30 (n/a)</td><td>167.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (-5.86%)</td><td>0.04 (-14.23%)</td><td>0.03 <b>(-35.15%)</b></td><td>0.03 (-0.43%)</td><td>0.01 (-14.05%)</td><td>547.00 (+0.42%)</td><td>430.04 (+14.06%)</td><td>489.10 <b>(+54.24%)</b></td><td>264.00 (+6.24%)</td><td>119.08 (-10.91%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.70 (n/a)</td><td>377.02 (n/a)</td><td>317.10 (n/a)</td><td>248.50 (n/a)</td><td>133.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (+13.50%)</td><td>0.05 (-15.26%)</td><td>0.04 <b>(-42.21%)</b></td><td>0.03 <b>(-35.41%)</b></td><td>0.02 <b>(+144.45%)</b></td><td>574.70 <b>(+54.82%)</b></td><td>385.64 <b>(+35.44%)</b></td><td>455.20 <b>(+73.01%)</b></td><td>215.60 (-11.89%)</td><td>159.17 <b>(+205.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>371.20 (n/a)</td><td>284.74 (n/a)</td><td>263.10 (n/a)</td><td>244.70 (n/a)</td><td>52.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+17.90%)</td><td>0.04 (+4.06%)</td><td>0.04 <b>(-32.44%)</b></td><td>0.03 <b>(+193.38%)</b></td><td>0.01 <b>(-29.54%)</b></td><td>488.40 <b>(-65.91%)</b></td><td>412.82 <b>(-28.87%)</b></td><td>456.80 <b>(+48.02%)</b></td><td>246.10 (-15.17%)</td><td>99.98 <b>(-79.59%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1432.80 (n/a)</td><td>580.34 (n/a)</td><td>308.60 (n/a)</td><td>290.10 (n/a)</td><td>489.89 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (-3.54%)</td><td>0.05 (-2.29%)</td><td>0.05 (-10.70%)</td><td>0.03 <b>(+315.20%)</b></td><td>0.01 <b>(-44.71%)</b></td><td>504.50 <b>(-75.92%)</b></td><td>362.56 <b>(-43.27%)</b></td><td>303.10 (+11.97%)</td><td>268.20 (+3.67%)</td><td>108.21 <b>(-86.71%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2094.80 (n/a)</td><td>639.12 (n/a)</td><td>270.70 (n/a)</td><td>258.70 (n/a)</td><td>813.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 <b>(-26.10%)</b></td><td>0.08 <b>(-29.51%)</b></td><td>0.07 <b>(-43.36%)</b></td><td>0.06 <b>(-30.20%)</b></td><td>0.03 (-15.56%)</td><td>583.40 <b>(+43.24%)</b></td><td>433.96 <b>(+44.61%)</b></td><td>489.70 <b>(+76.53%)</b></td><td>278.20 <b>(+35.31%)</b></td><td>127.39 <b>(+57.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>407.30 (n/a)</td><td>300.10 (n/a)</td><td>277.40 (n/a)</td><td>205.60 (n/a)</td><td>80.70 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (-9.14%)</td><td>0.09 (-11.43%)</td><td>0.09 <b>(-22.78%)</b></td><td>0.07 (+7.06%)</td><td>0.02 <b>(-31.18%)</b></td><td>446.50 (-6.59%)</td><td>366.76 (+8.62%)</td><td>381.50 <b>(+29.50%)</b></td><td>264.50 (+10.07%)</td><td>77.94 <b>(-28.05%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>478.00 (n/a)</td><td>337.66 (n/a)</td><td>294.60 (n/a)</td><td>240.30 (n/a)</td><td>108.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (-12.79%)</td><td>0.09 (-12.23%)</td><td>0.12 (+11.46%)</td><td>0.03 <b>(-38.99%)</b></td><td>0.05 (+15.98%)</td><td>947.10 <b>(+63.91%)</b></td><td>479.92 <b>(+35.02%)</b></td><td>272.10 (-10.29%)</td><td>246.00 (+14.63%)</td><td>318.67 <b>(+107.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>577.80 (n/a)</td><td>355.44 (n/a)</td><td>303.30 (n/a)</td><td>214.60 (n/a)</td><td>153.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (-4.45%)</td><td>0.08 <b>(-32.44%)</b></td><td>0.07 <b>(-42.78%)</b></td><td>0.06 <b>(-45.03%)</b></td><td>0.03 <b>(+133.39%)</b></td><td>569.80 <b>(+81.93%)</b></td><td>441.06 <b>(+60.92%)</b></td><td>485.20 <b>(+74.72%)</b></td><td>240.90 (+4.69%)</td><td>128.70 <b>(+334.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>313.20 (n/a)</td><td>274.08 (n/a)</td><td>277.70 (n/a)</td><td>230.10 (n/a)</td><td>29.65 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (-7.18%)</td><td>0.11 (+2.73%)</td><td>0.12 (-11.03%)</td><td>0.06 (+8.60%)</td><td>0.03 <b>(-32.09%)</b></td><td>523.40 (-7.92%)</td><td>316.36 (-11.58%)</td><td>270.00 (+12.36%)</td><td>231.80 (+7.71%)</td><td>120.01 <b>(-32.33%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>568.40 (n/a)</td><td>357.78 (n/a)</td><td>240.30 (n/a)</td><td>215.20 (n/a)</td><td>177.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (+13.03%)</td><td>0.10 (-11.57%)</td><td>0.09 (-19.49%)</td><td>0.06 <b>(-28.07%)</b></td><td>0.03 <b>(+167.09%)</b></td><td>511.90 <b>(+39.03%)</b></td><td>369.50 <b>(+21.66%)</b></td><td>360.00 <b>(+24.22%)</b></td><td>244.30 (-11.52%)</td><td>117.16 <b>(+218.63%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>368.20 (n/a)</td><td>303.72 (n/a)</td><td>289.80 (n/a)</td><td>276.10 (n/a)</td><td>36.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 <b>(-29.37%)</b></td><td>0.09 <b>(-21.59%)</b></td><td>0.07 <b>(-39.87%)</b></td><td>0.06 <b>(+28.21%)</b></td><td>0.03 <b>(-41.57%)</b></td><td>524.20 <b>(-22.01%)</b></td><td>416.30 (+13.51%)</td><td>496.50 <b>(+66.33%)</b></td><td>263.00 <b>(+41.55%)</b></td><td>125.77 <b>(-35.58%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>672.10 (n/a)</td><td>366.74 (n/a)</td><td>298.50 (n/a)</td><td>185.80 (n/a)</td><td>195.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (-11.26%)</td><td>0.09 <b>(-22.20%)</b></td><td>0.08 <b>(-35.05%)</b></td><td>0.05 (-15.42%)</td><td>0.04 (-2.51%)</td><td>652.10 (+18.22%)</td><td>418.80 <b>(+31.24%)</b></td><td>431.70 <b>(+53.96%)</b></td><td>243.90 (+12.71%)</td><td>167.59 <b>(+22.53%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>551.60 (n/a)</td><td>319.12 (n/a)</td><td>280.40 (n/a)</td><td>216.40 (n/a)</td><td>136.78 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 <b>(+24.99%)</b></td><td>0.06 <b>(-29.98%)</b></td><td>0.06 <b>(-28.68%)</b></td><td>0.02 <b>(-69.83%)</b></td><td>0.05 <b>(+86.47%)</b></td><td>2116.70 <b>(+231.46%)</b></td><td>1070.94 <b>(+149.46%)</b></td><td>545.50 <b>(+40.23%)</b></td><td>237.50 <b>(-20.01%)</b></td><td>879.32 <b>(+492.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>638.60 (n/a)</td><td>429.30 (n/a)</td><td>389.00 (n/a)</td><td>296.90 (n/a)</td><td>148.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (+10.18%)</td><td>0.09 (-3.49%)</td><td>0.08 <b>(-29.10%)</b></td><td>0.07 (+1.59%)</td><td>0.03 (+16.80%)</td><td>501.20 (-1.57%)</td><td>375.58 (+5.04%)</td><td>405.70 <b>(+41.06%)</b></td><td>251.30 (-9.25%)</td><td>112.88 (+4.21%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>509.20 (n/a)</td><td>357.56 (n/a)</td><td>287.60 (n/a)</td><td>276.90 (n/a)</td><td>108.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (+15.27%)</td><td>0.09 (+3.36%)</td><td>0.08 (+1.83%)</td><td>0.06 (+11.69%)</td><td>0.03 <b>(+22.27%)</b></td><td>532.80 (-10.47%)</td><td>411.96 (-2.24%)</td><td>429.80 (-1.78%)</td><td>226.80 (-13.24%)</td><td>117.59 (-7.63%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>595.10 (n/a)</td><td>421.40 (n/a)</td><td>437.60 (n/a)</td><td>261.40 (n/a)</td><td>127.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (-8.99%)</td><td>0.08 (-6.13%)</td><td>0.10 <b>(+39.41%)</b></td><td>0.03 <b>(-42.96%)</b></td><td>0.04 (-3.21%)</td><td>1079.90 <b>(+75.31%)</b></td><td>497.34 (+19.31%)</td><td>327.50 <b>(-28.26%)</b></td><td>269.30 (+9.87%)</td><td>337.46 <b>(+107.53%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>616.00 (n/a)</td><td>416.86 (n/a)</td><td>456.50 (n/a)</td><td>245.10 (n/a)</td><td>162.61 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+8.84%)</td><td>0.01 <b>(+43.82%)</b></td><td>0.02 <b>(+55.44%)</b></td><td>0.01 <b>(+381.29%)</b></td><td>0.00 <b>(-32.88%)</b></td><td>507.10 <b>(-79.22%)</b></td><td>302.96 <b>(-60.82%)</b></td><td>267.60 <b>(-35.67%)</b></td><td>227.80 (-8.11%)</td><td>115.49 <b>(-87.67%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2440.60 (n/a)</td><td>773.22 (n/a)</td><td>416.00 (n/a)</td><td>247.90 (n/a)</td><td>936.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(+60.16%)</b></td><td>0.01 (+11.58%)</td><td>0.01 (-11.42%)</td><td>0.01 (+7.93%)</td><td>0.01 <b>(+154.66%)</b></td><td>591.10 (-7.35%)</td><td>464.30 (-4.94%)</td><td>510.40 (+12.90%)</td><td>260.20 <b>(-37.57%)</b></td><td>127.66 <b>(+40.12%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>638.00 (n/a)</td><td>488.42 (n/a)</td><td>452.10 (n/a)</td><td>416.80 (n/a)</td><td>91.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+17.70%)</td><td>0.01 <b>(+35.62%)</b></td><td>0.01 <b>(+40.91%)</b></td><td>0.01 <b>(+257.93%)</b></td><td>0.01 (-3.16%)</td><td>520.50 <b>(-72.06%)</b></td><td>353.52 <b>(-48.14%)</b></td><td>345.40 <b>(-29.05%)</b></td><td>207.70 (-15.05%)</td><td>140.90 <b>(-78.99%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1863.00 (n/a)</td><td>681.72 (n/a)</td><td>486.80 (n/a)</td><td>244.50 (n/a)</td><td>670.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-0.01%)</td><td>0.01 (-10.62%)</td><td>0.01 <b>(-36.38%)</b></td><td>0.01 (+2.47%)</td><td>0.00 (-8.70%)</td><td>571.90 (-2.42%)</td><td>400.44 (+9.61%)</td><td>421.80 <b>(+57.21%)</b></td><td>255.90 (+0.04%)</td><td>131.33 (-10.83%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.10 (n/a)</td><td>365.34 (n/a)</td><td>268.30 (n/a)</td><td>255.80 (n/a)</td><td>147.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(-20.32%)</b></td><td>0.01 <b>(-26.92%)</b></td><td>0.01 <b>(-40.53%)</b></td><td>0.01 (-15.48%)</td><td>0.00 <b>(-35.88%)</b></td><td>641.60 (+18.31%)</td><td>454.50 <b>(+28.87%)</b></td><td>445.60 <b>(+68.15%)</b></td><td>271.20 <b>(+25.50%)</b></td><td>132.85 (-11.82%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>542.30 (n/a)</td><td>352.68 (n/a)</td><td>265.00 (n/a)</td><td>216.10 (n/a)</td><td>150.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+5.84%)</td><td>0.01 (+0.54%)</td><td>0.01 (-12.64%)</td><td>0.01 (+0.59%)</td><td>0.00 (+15.37%)</td><td>603.00 (-0.59%)</td><td>474.80 (+1.41%)</td><td>547.10 (+14.46%)</td><td>262.30 (-5.51%)</td><td>138.14 (+10.33%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.60 (n/a)</td><td>468.20 (n/a)</td><td>478.00 (n/a)</td><td>277.60 (n/a)</td><td>125.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 <b>(+76.25%)</b></td><td>0.01 <b>(+84.71%)</b></td><td>0.02 <b>(+117.26%)</b></td><td>0.01 <b>(+78.18%)</b></td><td>0.00 <b>(+137.60%)</b></td><td>560.70 <b>(-43.88%)</b></td><td>353.56 <b>(-43.06%)</b></td><td>254.00 <b>(-53.98%)</b></td><td>240.40 <b>(-43.28%)</b></td><td>151.00 <b>(-31.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>999.10 (n/a)</td><td>620.92 (n/a)</td><td>551.90 (n/a)</td><td>423.80 (n/a)</td><td>221.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+7.50%)</td><td>0.01 (-4.04%)</td><td>0.01 (-18.29%)</td><td>0.01 (+7.66%)</td><td>0.00 <b>(+20.34%)</b></td><td>609.80 (-7.11%)</td><td>497.00 (+5.83%)</td><td>562.80 <b>(+22.37%)</b></td><td>282.50 (-6.98%)</td><td>131.15 (+2.03%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>656.50 (n/a)</td><td>469.60 (n/a)</td><td>459.90 (n/a)</td><td>303.70 (n/a)</td><td>128.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-8.45%)</td><td>0.01 (+5.10%)</td><td>0.01 (+5.87%)</td><td>0.01 (+13.14%)</td><td>0.00 <b>(-25.35%)</b></td><td>538.30 (-11.61%)</td><td>434.26 (-9.21%)</td><td>466.30 (-5.55%)</td><td>266.50 (+9.22%)</td><td>101.97 <b>(-27.62%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.00 (n/a)</td><td>478.30 (n/a)</td><td>493.70 (n/a)</td><td>244.00 (n/a)</td><td>140.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (-14.85%)</td><td>0.01 (+0.51%)</td><td>0.01 (-15.56%)</td><td>0.01 <b>(+97.10%)</b></td><td>0.00 <b>(-49.24%)</b></td><td>510.30 <b>(-49.26%)</b></td><td>403.42 (-18.23%)</td><td>402.70 (+18.44%)</td><td>292.30 (+17.44%)</td><td>89.19 <b>(-70.92%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1005.70 (n/a)</td><td>493.36 (n/a)</td><td>340.00 (n/a)</td><td>248.90 (n/a)</td><td>306.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 <b>(-24.08%)</b></td><td>0.01 (-1.46%)</td><td>0.01 (+8.83%)</td><td>0.01 (+5.83%)</td><td>0.00 <b>(-44.87%)</b></td><td>632.60 (-5.51%)</td><td>491.54 (-4.13%)</td><td>485.00 (-8.11%)</td><td>364.00 <b>(+31.74%)</b></td><td>108.66 <b>(-28.80%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.50 (n/a)</td><td>512.72 (n/a)</td><td>527.80 (n/a)</td><td>276.30 (n/a)</td><td>152.61 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (-7.53%)</td><td>0.03 (-2.63%)</td><td>0.03 (-2.70%)</td><td>0.02 (-0.17%)</td><td>0.01 (-7.88%)</td><td>498.80 (+0.16%)</td><td>318.22 (+1.99%)</td><td>288.70 (+2.78%)</td><td>248.20 (+8.15%)</td><td>103.06 (-3.11%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.00 (n/a)</td><td>312.02 (n/a)</td><td>280.90 (n/a)</td><td>229.50 (n/a)</td><td>106.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (+5.79%)</td><td>0.04 <b>(+21.47%)</b></td><td>0.04 <b>(+39.73%)</b></td><td>0.03 (+8.23%)</td><td>0.01 (-13.45%)</td><td>467.00 (-7.62%)</td><td>307.04 <b>(-20.12%)</b></td><td>293.30 <b>(-28.45%)</b></td><td>227.50 (-5.48%)</td><td>94.32 <b>(-22.74%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.50 (n/a)</td><td>384.36 (n/a)</td><td>409.90 (n/a)</td><td>240.70 (n/a)</td><td>122.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (+18.16%)</td><td>0.02 (-17.43%)</td><td>0.02 (-10.16%)</td><td>0.00 <b>(-72.12%)</b></td><td>0.01 <b>(+61.72%)</b></td><td>1858.90 <b>(+258.65%)</b></td><td>723.02 <b>(+80.03%)</b></td><td>524.50 (+11.31%)</td><td>201.00 (-15.37%)</td><td>650.17 <b>(+414.58%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.30 (n/a)</td><td>401.62 (n/a)</td><td>471.20 (n/a)</td><td>237.50 (n/a)</td><td>126.35 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (-18.98%)</td><td>0.02 (-17.12%)</td><td>0.02 <b>(-23.33%)</b></td><td>0.01 <b>(-46.81%)</b></td><td>0.01 (-6.28%)</td><td>1095.10 <b>(+88.00%)</b></td><td>591.16 <b>(+32.30%)</b></td><td>586.10 <b>(+30.42%)</b></td><td>287.10 <b>(+23.43%)</b></td><td>313.24 <b>(+113.73%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>582.50 (n/a)</td><td>446.84 (n/a)</td><td>449.40 (n/a)</td><td>232.60 (n/a)</td><td>146.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 <b>(-35.87%)</b></td><td>0.02 <b>(-23.81%)</b></td><td>0.02 (-14.63%)</td><td>0.01 (+11.80%)</td><td>0.01 <b>(-50.44%)</b></td><td>574.30 (-10.55%)</td><td>469.10 (+12.05%)</td><td>506.30 (+17.14%)</td><td>245.20 <b>(+55.98%)</b></td><td>128.48 <b>(-34.82%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>642.00 (n/a)</td><td>418.64 (n/a)</td><td>432.20 (n/a)</td><td>157.20 (n/a)</td><td>197.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (-19.28%)</td><td>0.03 (-9.45%)</td><td>0.04 (-7.21%)</td><td>0.02 (+5.64%)</td><td>0.01 (-14.47%)</td><td>667.20 (-5.33%)</td><td>410.76 (+7.55%)</td><td>276.70 (+7.79%)</td><td>238.10 <b>(+23.88%)</b></td><td>218.48 (-0.80%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>704.80 (n/a)</td><td>381.94 (n/a)</td><td>256.70 (n/a)</td><td>192.20 (n/a)</td><td>220.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 <b>(-24.14%)</b></td><td>0.02 <b>(-24.07%)</b></td><td>0.02 (+8.51%)</td><td>0.00 <b>(-67.63%)</b></td><td>0.01 (-17.61%)</td><td>1896.70 <b>(+208.96%)</b></td><td>721.30 <b>(+68.20%)</b></td><td>425.20 (-7.85%)</td><td>322.00 <b>(+31.86%)</b></td><td>663.22 <b>(+285.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.90 (n/a)</td><td>428.84 (n/a)</td><td>461.40 (n/a)</td><td>244.20 (n/a)</td><td>171.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 <b>(-24.21%)</b></td><td>0.02 (-2.11%)</td><td>0.03 <b>(+42.39%)</b></td><td>0.00 <b>(-70.22%)</b></td><td>0.01 (-0.79%)</td><td>2019.70 <b>(+235.72%)</b></td><td>684.84 <b>(+52.74%)</b></td><td>323.20 <b>(-29.75%)</b></td><td>270.30 <b>(+31.92%)</b></td><td>752.06 <b>(+404.62%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.60 (n/a)</td><td>448.36 (n/a)</td><td>460.10 (n/a)</td><td>204.90 (n/a)</td><td>149.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (+3.66%)</td><td>0.02 (-8.19%)</td><td>0.02 (-6.53%)</td><td>0.01 <b>(-32.69%)</b></td><td>0.00 <b>(+64.35%)</b></td><td>798.00 <b>(+48.58%)</b></td><td>509.66 (+15.26%)</td><td>476.80 (+6.98%)</td><td>338.20 (-3.51%)</td><td>171.38 <b>(+149.23%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>537.10 (n/a)</td><td>442.20 (n/a)</td><td>445.70 (n/a)</td><td>350.50 (n/a)</td><td>68.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 <b>(+110.75%)</b></td><td>0.03 <b>(+91.88%)</b></td><td>0.02 <b>(+26.19%)</b></td><td>0.02 <b>(+130.94%)</b></td><td>0.01 <b>(+90.35%)</b></td><td>587.00 <b>(-56.70%)</b></td><td>392.00 <b>(-49.87%)</b></td><td>433.30 <b>(-20.74%)</b></td><td>242.00 <b>(-52.54%)</b></td><td>142.49 <b>(-61.62%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1355.70 (n/a)</td><td>782.02 (n/a)</td><td>546.70 (n/a)</td><td>509.90 (n/a)</td><td>371.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (+7.11%)</td><td>0.02 (+5.56%)</td><td>0.02 (-10.52%)</td><td>0.01 <b>(+250.06%)</b></td><td>0.01 <b>(-23.71%)</b></td><td>560.40 <b>(-71.43%)</b></td><td>464.36 <b>(-35.17%)</b></td><td>529.50 (+11.76%)</td><td>252.40 (-6.66%)</td><td>129.37 <b>(-81.64%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1961.80 (n/a)</td><td>716.26 (n/a)</td><td>473.80 (n/a)</td><td>270.40 (n/a)</td><td>704.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 <b>(-35.09%)</b></td><td>0.04 <b>(-29.97%)</b></td><td>0.03 <b>(-38.83%)</b></td><td>0.03 (-15.38%)</td><td>0.01 <b>(-53.36%)</b></td><td>574.30 (+18.19%)</td><td>470.02 <b>(+34.75%)</b></td><td>471.20 <b>(+63.50%)</b></td><td>368.00 <b>(+54.04%)</b></td><td>99.56 (-19.08%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>485.90 (n/a)</td><td>348.80 (n/a)</td><td>288.20 (n/a)</td><td>238.90 (n/a)</td><td>123.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.16 <b>(+46.15%)</b></td><td>0.09 <b>(+62.94%)</b></td><td>0.09 <b>(+95.03%)</b></td><td>0.04 <b>(+246.30%)</b></td><td>0.05 (+12.43%)</td><td>559.30 <b>(-71.13%)</b></td><td>339.86 <b>(-58.90%)</b></td><td>280.90 <b>(-48.72%)</b></td><td>150.80 <b>(-31.55%)</b></td><td>163.32 <b>(-77.17%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1937.00 (n/a)</td><td>826.82 (n/a)</td><td>547.80 (n/a)</td><td>220.30 (n/a)</td><td>715.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 <b>(+37.55%)</b></td><td>0.04 (+1.31%)</td><td>0.03 <b>(-29.54%)</b></td><td>0.03 (-3.61%)</td><td>0.01 <b>(+131.07%)</b></td><td>611.70 (+3.73%)</td><td>480.08 (+6.97%)</td><td>576.50 <b>(+41.93%)</b></td><td>275.00 <b>(-27.29%)</b></td><td>157.99 <b>(+80.18%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>448.78 (n/a)</td><td>406.20 (n/a)</td><td>378.20 (n/a)</td><td>87.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (-2.46%)</td><td>0.05 (+11.68%)</td><td>0.06 <b>(+45.04%)</b></td><td>0.02 <b>(-43.19%)</b></td><td>0.03 (+11.17%)</td><td>1035.00 <b>(+76.02%)</b></td><td>493.48 (+2.62%)</td><td>367.10 <b>(-31.05%)</b></td><td>234.90 (+2.53%)</td><td>320.79 <b>(+122.98%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.00 (n/a)</td><td>480.88 (n/a)</td><td>532.40 (n/a)</td><td>229.10 (n/a)</td><td>143.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (+0.11%)</td><td>0.04 <b>(-24.35%)</b></td><td>0.04 <b>(-32.09%)</b></td><td>0.01 <b>(-76.65%)</b></td><td>0.02 <b>(+53.37%)</b></td><td>1997.40 <b>(+328.26%)</b></td><td>711.86 <b>(+98.97%)</b></td><td>433.10 <b>(+47.21%)</b></td><td>271.10 (-0.15%)</td><td>722.31 <b>(+637.37%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>466.40 (n/a)</td><td>357.78 (n/a)</td><td>294.20 (n/a)</td><td>271.50 (n/a)</td><td>97.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (-13.61%)</td><td>0.05 (+1.20%)</td><td>0.05 (+9.53%)</td><td>0.03 (-16.95%)</td><td>0.02 (-14.76%)</td><td>599.00 <b>(+20.43%)</b></td><td>416.56 (-1.02%)</td><td>423.80 (-8.68%)</td><td>270.60 (+15.74%)</td><td>130.22 <b>(+22.51%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>497.40 (n/a)</td><td>420.84 (n/a)</td><td>464.10 (n/a)</td><td>233.80 (n/a)</td><td>106.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (-12.98%)</td><td>0.03 (-14.01%)</td><td>0.03 (+1.82%)</td><td>0.02 <b>(-44.73%)</b></td><td>0.01 <b>(+44.23%)</b></td><td>1080.70 <b>(+80.93%)</b></td><td>636.42 <b>(+26.61%)</b></td><td>507.20 (-1.80%)</td><td>427.80 (+14.94%)</td><td>267.29 <b>(+212.69%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>597.30 (n/a)</td><td>502.66 (n/a)</td><td>516.50 (n/a)</td><td>372.20 (n/a)</td><td>85.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (+15.84%)</td><td>0.05 <b>(+22.61%)</b></td><td>0.04 (+6.86%)</td><td>0.03 (+5.12%)</td><td>0.02 <b>(+45.50%)</b></td><td>582.70 (-4.88%)</td><td>400.82 (-13.59%)</td><td>429.80 (-6.42%)</td><td>230.00 (-13.70%)</td><td>156.12 (+19.78%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>612.60 (n/a)</td><td>463.84 (n/a)</td><td>459.30 (n/a)</td><td>266.50 (n/a)</td><td>130.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+0.71%)</td><td>0.05 <b>(+43.58%)</b></td><td>0.04 <b>(+57.26%)</b></td><td>0.03 <b>(+113.52%)</b></td><td>0.01 <b>(-27.50%)</b></td><td>479.40 <b>(-53.17%)</b></td><td>384.58 <b>(-40.37%)</b></td><td>425.00 <b>(-36.42%)</b></td><td>242.80 (-0.70%)</td><td>107.25 <b>(-62.30%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1023.70 (n/a)</td><td>644.90 (n/a)</td><td>668.40 (n/a)</td><td>244.50 (n/a)</td><td>284.51 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 <b>(+63.81%)</b></td><td>0.05 (+9.47%)</td><td>0.05 (+13.65%)</td><td>0.03 <b>(-23.17%)</b></td><td>0.03 <b>(+181.61%)</b></td><td>654.00 <b>(+30.15%)</b></td><td>447.74 (+7.22%)</td><td>403.70 (-12.01%)</td><td>184.10 <b>(-38.96%)</b></td><td>185.31 <b>(+118.53%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>502.50 (n/a)</td><td>417.60 (n/a)</td><td>458.80 (n/a)</td><td>301.60 (n/a)</td><td>84.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (+15.20%)</td><td>0.04 (+13.50%)</td><td>0.03 (+6.11%)</td><td>0.03 (+10.11%)</td><td>0.01 <b>(+20.43%)</b></td><td>537.30 (-9.18%)</td><td>426.48 (-11.25%)</td><td>472.20 (-5.75%)</td><td>266.20 (-13.21%)</td><td>112.56 (-6.88%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.60 (n/a)</td><td>480.56 (n/a)</td><td>501.00 (n/a)</td><td>306.70 (n/a)</td><td>120.87 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (-5.75%)</td><td>0.09 (-1.30%)</td><td>0.10 (+0.09%)</td><td>0.06 (+12.26%)</td><td>0.03 <b>(-20.57%)</b></td><td>517.40 (-10.92%)</td><td>388.88 (-2.92%)</td><td>341.20 (-0.09%)</td><td>276.70 (+6.10%)</td><td>119.16 <b>(-22.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.80 (n/a)</td><td>400.56 (n/a)</td><td>341.50 (n/a)</td><td>260.80 (n/a)</td><td>154.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (-6.37%)</td><td>0.10 (-12.74%)</td><td>0.10 <b>(-22.77%)</b></td><td>0.07 (-8.80%)</td><td>0.03 (-13.25%)</td><td>503.10 (+9.66%)</td><td>366.92 (+13.39%)</td><td>340.60 <b>(+29.46%)</b></td><td>241.50 (+6.76%)</td><td>103.06 (+0.22%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>458.80 (n/a)</td><td>323.60 (n/a)</td><td>263.10 (n/a)</td><td>226.20 (n/a)</td><td>102.83 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 (+3.12%)</td><td>0.11 (-14.07%)</td><td>0.09 <b>(-25.45%)</b></td><td>0.07 (-3.04%)</td><td>0.04 (+3.80%)</td><td>590.00 (+3.13%)</td><td>415.90 (+17.27%)</td><td>464.40 <b>(+34.14%)</b></td><td>233.50 (-3.03%)</td><td>139.31 (+3.95%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>572.10 (n/a)</td><td>354.66 (n/a)</td><td>346.20 (n/a)</td><td>240.80 (n/a)</td><td>134.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (+9.52%)</td><td>0.08 (-12.07%)</td><td>0.08 (-8.07%)</td><td>0.02 <b>(-69.24%)</b></td><td>0.04 <b>(+37.86%)</b></td><td>2008.40 <b>(+225.14%)</b></td><td>700.96 <b>(+70.46%)</b></td><td>417.50 (+8.78%)</td><td>248.90 (-8.69%)</td><td>735.87 <b>(+393.19%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>617.70 (n/a)</td><td>411.22 (n/a)</td><td>383.80 (n/a)</td><td>272.60 (n/a)</td><td>149.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.16 <b>(+24.06%)</b></td><td>0.12 (+12.77%)</td><td>0.14 (+18.38%)</td><td>0.08 (-3.94%)</td><td>0.04 <b>(+70.32%)</b></td><td>540.60 (+4.10%)</td><td>382.08 (-5.41%)</td><td>301.10 (-15.52%)</td><td>254.00 (-19.39%)</td><td>145.26 <b>(+48.58%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>519.30 (n/a)</td><td>403.92 (n/a)</td><td>356.40 (n/a)</td><td>315.10 (n/a)</td><td>97.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (-5.63%)</td><td>0.10 (+1.24%)</td><td>0.11 <b>(+23.42%)</b></td><td>0.06 <b>(-27.46%)</b></td><td>0.03 <b>(+25.60%)</b></td><td>594.30 <b>(+37.86%)</b></td><td>366.14 (+3.49%)</td><td>301.00 (-18.98%)</td><td>270.40 (+5.96%)</td><td>134.39 <b>(+86.63%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>431.10 (n/a)</td><td>353.80 (n/a)</td><td>371.50 (n/a)</td><td>255.20 (n/a)</td><td>72.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (+2.87%)</td><td>0.10 (+17.61%)</td><td>0.11 <b>(+45.28%)</b></td><td>0.06 (-3.52%)</td><td>0.03 (+12.41%)</td><td>581.00 (+3.66%)</td><td>407.16 (-13.22%)</td><td>348.40 <b>(-31.17%)</b></td><td>276.00 (-2.82%)</td><td>132.27 <b>(+21.02%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>560.50 (n/a)</td><td>469.18 (n/a)</td><td>506.20 (n/a)</td><td>284.00 (n/a)</td><td>109.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 <b>(+28.13%)</b></td><td>0.08 (+0.93%)</td><td>0.07 (-9.26%)</td><td>0.07 (+12.43%)</td><td>0.03 <b>(+70.41%)</b></td><td>487.40 (-11.06%)</td><td>424.26 (+2.71%)</td><td>462.20 (+10.21%)</td><td>240.10 <b>(-21.97%)</b></td><td>104.37 (+15.45%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>548.00 (n/a)</td><td>413.08 (n/a)</td><td>419.40 (n/a)</td><td>307.70 (n/a)</td><td>90.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.17 <b>(+29.77%)</b></td><td>0.09 (+8.89%)</td><td>0.08 (+11.62%)</td><td>0.02 <b>(-68.26%)</b></td><td>0.06 <b>(+101.82%)</b></td><td>1924.60 <b>(+215.04%)</b></td><td>706.30 <b>(+46.61%)</b></td><td>455.00 (-10.42%)</td><td>220.00 <b>(-22.94%)</b></td><td>700.25 <b>(+400.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>610.90 (n/a)</td><td>481.76 (n/a)</td><td>507.90 (n/a)</td><td>285.50 (n/a)</td><td>139.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (+8.05%)</td><td>0.07 (+1.79%)</td><td>0.06 (-12.83%)</td><td>0.05 (-13.59%)</td><td>0.02 <b>(+58.21%)</b></td><td>718.20 (+15.73%)</td><td>514.38 (+2.01%)</td><td>543.00 (+14.73%)</td><td>368.10 (-7.44%)</td><td>144.97 <b>(+58.67%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>504.24 (n/a)</td><td>473.30 (n/a)</td><td>397.70 (n/a)</td><td>91.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (+11.99%)</td><td>0.06 (+12.61%)</td><td>0.05 (+11.71%)</td><td>0.05 <b>(+31.77%)</b></td><td>0.02 (-6.85%)</td><td>436.90 <b>(-24.11%)</b></td><td>349.80 (-13.66%)</td><td>390.00 (-10.47%)</td><td>248.40 (-10.71%)</td><td>81.38 <b>(-34.14%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>575.70 (n/a)</td><td>405.14 (n/a)</td><td>435.60 (n/a)</td><td>278.20 (n/a)</td><td>123.57 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 <b>(+36.55%)</b></td><td>0.05 (+2.56%)</td><td>0.04 (-12.68%)</td><td>0.03 (-4.39%)</td><td>0.02 <b>(+59.21%)</b></td><td>662.70 (+4.59%)</td><td>465.84 (+2.11%)</td><td>472.30 (+14.52%)</td><td>236.60 <b>(-26.77%)</b></td><td>152.03 (+12.05%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>633.60 (n/a)</td><td>456.20 (n/a)</td><td>412.40 (n/a)</td><td>323.10 (n/a)</td><td>135.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-5.82%)</td><td>0.05 (-9.13%)</td><td>0.05 (-6.89%)</td><td>0.04 (-4.79%)</td><td>0.01 (-5.33%)</td><td>554.40 (+5.02%)</td><td>427.72 (+10.33%)</td><td>401.60 (+7.41%)</td><td>287.90 (+6.20%)</td><td>116.38 (+10.21%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>527.90 (n/a)</td><td>387.68 (n/a)</td><td>373.90 (n/a)</td><td>271.10 (n/a)</td><td>105.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (+8.25%)</td><td>0.06 <b>(+39.37%)</b></td><td>0.05 <b>(+22.68%)</b></td><td>0.04 <b>(+293.95%)</b></td><td>0.02 <b>(-22.16%)</b></td><td>499.70 <b>(-74.61%)</b></td><td>398.64 <b>(-48.57%)</b></td><td>441.50 (-18.48%)</td><td>250.00 (-7.61%)</td><td>114.03 <b>(-83.18%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1968.40 (n/a)</td><td>775.18 (n/a)</td><td>541.60 (n/a)</td><td>270.60 (n/a)</td><td>678.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (-8.50%)</td><td>0.05 (+4.16%)</td><td>0.05 (+11.70%)</td><td>0.04 (+14.82%)</td><td>0.00 <b>(-50.09%)</b></td><td>467.80 (-12.90%)</td><td>435.22 (-6.09%)</td><td>442.10 (-10.49%)</td><td>371.90 (+9.29%)</td><td>38.86 <b>(-52.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>537.10 (n/a)</td><td>463.46 (n/a)</td><td>493.90 (n/a)</td><td>340.30 (n/a)</td><td>82.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-9.06%)</td><td>0.05 (-11.35%)</td><td>0.05 (+0.20%)</td><td>0.03 <b>(-26.18%)</b></td><td>0.02 (-10.09%)</td><td>746.70 <b>(+35.47%)</b></td><td>454.48 (+15.15%)</td><td>421.30 (-0.19%)</td><td>295.00 (+9.95%)</td><td>174.66 <b>(+46.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.20 (n/a)</td><td>394.68 (n/a)</td><td>422.10 (n/a)</td><td>268.30 (n/a)</td><td>119.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (+9.24%)</td><td>0.07 (+4.43%)</td><td>0.05 (-0.95%)</td><td>0.05 (+1.12%)</td><td>0.02 <b>(+30.34%)</b></td><td>515.50 (-1.11%)</td><td>403.44 (-1.09%)</td><td>454.40 (+0.96%)</td><td>264.10 (-8.46%)</td><td>127.49 <b>(+20.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>521.30 (n/a)</td><td>407.90 (n/a)</td><td>450.10 (n/a)</td><td>288.50 (n/a)</td><td>106.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (+0.95%)</td><td>0.07 (-9.60%)</td><td>0.07 (-18.29%)</td><td>0.04 (-0.26%)</td><td>0.02 (-6.12%)</td><td>556.60 (+0.27%)</td><td>400.48 (+8.92%)</td><td>369.30 <b>(+22.41%)</b></td><td>237.80 (-0.96%)</td><td>123.24 (-8.78%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>555.10 (n/a)</td><td>367.68 (n/a)</td><td>301.70 (n/a)</td><td>240.10 (n/a)</td><td>135.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.11 <b>(+20.23%)</b></td><td>0.08 (+8.22%)</td><td>0.08 (-10.46%)</td><td>0.05 (+16.87%)</td><td>0.03 <b>(+21.24%)</b></td><td>509.80 (-14.43%)</td><td>347.70 (-6.64%)</td><td>306.70 (+11.69%)</td><td>217.30 (-16.81%)</td><td>136.34 (-9.27%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>595.80 (n/a)</td><td>372.44 (n/a)</td><td>274.60 (n/a)</td><td>261.20 (n/a)</td><td>150.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 <b>(+45.36%)</b></td><td>0.06 <b>(+40.38%)</b></td><td>0.05 (+19.69%)</td><td>0.04 <b>(+185.59%)</b></td><td>0.02 (-1.51%)</td><td>670.30 <b>(-64.99%)</b></td><td>461.40 <b>(-42.81%)</b></td><td>461.30 (-16.45%)</td><td>294.10 <b>(-31.20%)</b></td><td>136.55 <b>(-78.17%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1914.40 (n/a)</td><td>806.74 (n/a)</td><td>552.10 (n/a)</td><td>427.50 (n/a)</td><td>625.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 <b>(-39.35%)</b></td><td>0.05 (-12.18%)</td><td>0.06 (+9.45%)</td><td>0.04 (+0.24%)</td><td>0.01 <b>(-59.63%)</b></td><td>581.40 (-0.24%)</td><td>473.70 (+7.27%)</td><td>414.80 (-8.63%)</td><td>407.70 <b>(+64.86%)</b></td><td>86.64 <b>(-30.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.80 (n/a)</td><td>441.58 (n/a)</td><td>454.00 (n/a)</td><td>247.30 (n/a)</td><td>124.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (-15.07%)</td><td>0.06 (-2.90%)</td><td>0.05 (+1.10%)</td><td>0.03 (+10.95%)</td><td>0.02 <b>(-22.67%)</b></td><td>801.10 (-9.87%)</td><td>498.82 (-1.96%)</td><td>453.10 (-1.09%)</td><td>292.80 (+17.73%)</td><td>194.34 (-16.92%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>888.80 (n/a)</td><td>508.78 (n/a)</td><td>458.10 (n/a)</td><td>248.70 (n/a)</td><td>233.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-11.33%)</td><td>0.06 (-4.43%)</td><td>0.06 (-4.43%)</td><td>0.04 (+13.59%)</td><td>0.01 <b>(-35.89%)</b></td><td>499.70 (-11.96%)</td><td>353.90 (-2.54%)</td><td>306.10 (+4.65%)</td><td>267.80 (+12.76%)</td><td>97.47 <b>(-34.85%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>567.60 (n/a)</td><td>363.12 (n/a)</td><td>292.50 (n/a)</td><td>237.50 (n/a)</td><td>149.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-11.49%)</td><td>0.04 <b>(-22.29%)</b></td><td>0.05 <b>(-25.95%)</b></td><td>0.01 <b>(-73.92%)</b></td><td>0.02 <b>(+51.62%)</b></td><td>2004.90 <b>(+283.35%)</b></td><td>686.96 <b>(+101.61%)</b></td><td>401.30 <b>(+35.03%)</b></td><td>273.80 (+13.00%)</td><td>740.56 <b>(+582.25%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>523.00 (n/a)</td><td>340.74 (n/a)</td><td>297.20 (n/a)</td><td>242.30 (n/a)</td><td>108.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (+0.21%)</td><td>0.06 (+9.14%)</td><td>0.07 (+19.00%)</td><td>0.03 <b>(-28.16%)</b></td><td>0.02 <b>(+43.40%)</b></td><td>571.40 <b>(+39.20%)</b></td><td>326.88 (-2.57%)</td><td>269.10 (-15.96%)</td><td>251.50 (-0.24%)</td><td>137.00 <b>(+102.39%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>410.50 (n/a)</td><td>335.50 (n/a)</td><td>320.20 (n/a)</td><td>252.10 (n/a)</td><td>67.69 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 <b>(+20.26%)</b></td><td>0.05 (-11.63%)</td><td>0.04 (-17.17%)</td><td>0.02 <b>(-31.13%)</b></td><td>0.02 <b>(+50.30%)</b></td><td>742.60 <b>(+45.21%)</b></td><td>470.56 <b>(+22.91%)</b></td><td>454.30 <b>(+20.73%)</b></td><td>227.50 (-16.88%)</td><td>184.29 <b>(+75.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>511.40 (n/a)</td><td>382.86 (n/a)</td><td>376.30 (n/a)</td><td>273.70 (n/a)</td><td>105.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-5.77%)</td><td>0.05 (-2.13%)</td><td>0.04 (-3.45%)</td><td>0.03 (-6.34%)</td><td>0.02 (-0.50%)</td><td>605.10 (+6.76%)</td><td>427.92 (+2.86%)</td><td>477.60 (+3.58%)</td><td>278.40 (+6.14%)</td><td>139.44 (+8.74%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>566.80 (n/a)</td><td>416.04 (n/a)</td><td>461.10 (n/a)</td><td>262.30 (n/a)</td><td>128.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 <b>(+30.91%)</b></td><td>0.06 <b>(+21.96%)</b></td><td>0.06 <b>(+40.53%)</b></td><td>0.04 (-2.73%)</td><td>0.02 <b>(+96.99%)</b></td><td>514.60 (+2.82%)</td><td>361.02 (-12.60%)</td><td>296.50 <b>(-28.85%)</b></td><td>231.90 <b>(-23.62%)</b></td><td>125.34 <b>(+63.85%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>500.50 (n/a)</td><td>413.08 (n/a)</td><td>416.70 (n/a)</td><td>303.60 (n/a)</td><td>76.50 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.40 <b>(+21.47%)</b></td><td>0.30 (+10.08%)</td><td>0.31 <b>(+22.46%)</b></td><td>0.21 (-6.85%)</td><td>0.08 <b>(+65.89%)</b></td><td>472.30 (+7.37%)</td><td>345.14 (-6.02%)</td><td>315.10 (-18.33%)</td><td>245.30 (-17.68%)</td><td>93.72 <b>(+52.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>439.90 (n/a)</td><td>367.26 (n/a)</td><td>385.80 (n/a)</td><td>298.00 (n/a)</td><td>61.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.41 (-14.19%)</td><td>0.30 (-4.29%)</td><td>0.33 (-8.84%)</td><td>0.19 (+10.01%)</td><td>0.10 (-19.77%)</td><td>508.90 (-9.09%)</td><td>360.08 (-0.13%)</td><td>296.80 (+9.68%)</td><td>241.30 (+16.57%)</td><td>132.47 (-16.35%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.36 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>559.80 (n/a)</td><td>360.54 (n/a)</td><td>270.60 (n/a)</td><td>207.00 (n/a)</td><td>158.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.29 <b>(+38.12%)</b></td><td>0.22 <b>(+34.71%)</b></td><td>0.19 (-1.49%)</td><td>0.16 <b>(+234.13%)</b></td><td>0.06 (-11.44%)</td><td>614.10 <b>(-70.07%)</b></td><td>478.54 <b>(-42.24%)</b></td><td>528.30 (+1.52%)</td><td>341.20 <b>(-27.59%)</b></td><td>118.49 <b>(-82.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>2051.80 (n/a)</td><td>828.46 (n/a)</td><td>520.40 (n/a)</td><td>471.20 (n/a)</td><td>684.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.26 (+1.30%)</td><td>0.19 (+16.31%)</td><td>0.17 (-11.82%)</td><td>0.12 <b>(+207.37%)</b></td><td>0.06 <b>(-30.93%)</b></td><td>628.00 <b>(-67.47%)</b></td><td>422.62 <b>(-40.47%)</b></td><td>439.80 (+13.38%)</td><td>278.50 (-1.28%)</td><td>135.16 <b>(-80.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1930.30 (n/a)</td><td>709.88 (n/a)</td><td>387.90 (n/a)</td><td>282.10 (n/a)</td><td>689.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.29 (-3.12%)</td><td>0.19 (+2.73%)</td><td>0.17 (-16.39%)</td><td>0.07 <b>(-31.37%)</b></td><td>0.09 (+11.88%)</td><td>1099.60 <b>(+45.70%)</b></td><td>501.66 (+8.47%)</td><td>433.20 (+19.60%)</td><td>252.70 (+3.23%)</td><td>345.86 <b>(+65.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>754.70 (n/a)</td><td>462.48 (n/a)</td><td>362.20 (n/a)</td><td>244.80 (n/a)</td><td>209.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.28 (+0.37%)</td><td>0.18 (+0.69%)</td><td>0.14 (-10.78%)</td><td>0.12 (-17.64%)</td><td>0.07 (+19.09%)</td><td>623.30 <b>(+21.41%)</b></td><td>456.02 (+3.79%)</td><td>519.10 (+12.07%)</td><td>259.60 (-0.38%)</td><td>151.88 <b>(+48.44%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>513.40 (n/a)</td><td>439.38 (n/a)</td><td>463.20 (n/a)</td><td>260.60 (n/a)</td><td>102.32 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.17 (-10.60%)</td><td>0.13 <b>(+43.93%)</b></td><td>0.13 <b>(+104.22%)</b></td><td>0.08 <b>(+50.05%)</b></td><td>0.03 <b>(-44.96%)</b></td><td>446.70 <b>(-33.35%)</b></td><td>306.30 <b>(-39.83%)</b></td><td>289.50 <b>(-51.03%)</b></td><td>221.50 (+11.81%)</td><td>84.79 <b>(-54.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>670.20 (n/a)</td><td>509.02 (n/a)</td><td>591.20 (n/a)</td><td>198.10 (n/a)</td><td>185.93 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (-0.37%)</td><td>0.08 (-4.96%)</td><td>0.08 (-11.93%)</td><td>0.06 (+7.12%)</td><td>0.03 (-4.96%)</td><td>613.50 (-6.65%)</td><td>480.80 (+3.65%)</td><td>490.70 (+13.54%)</td><td>290.20 (+0.38%)</td><td>118.21 (-16.74%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>657.20 (n/a)</td><td>463.88 (n/a)</td><td>432.20 (n/a)</td><td>289.10 (n/a)</td><td>141.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 <b>(-20.24%)</b></td><td>0.09 <b>(-29.34%)</b></td><td>0.09 <b>(-38.56%)</b></td><td>0.02 <b>(-60.83%)</b></td><td>0.05 (+4.72%)</td><td>1903.30 <b>(+155.27%)</b></td><td>677.78 <b>(+92.58%)</b></td><td>431.70 <b>(+62.78%)</b></td><td>260.30 <b>(+25.39%)</b></td><td>693.92 <b>(+212.03%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>745.60 (n/a)</td><td>351.94 (n/a)</td><td>265.20 (n/a)</td><td>207.60 (n/a)</td><td>222.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (+2.30%)</td><td>0.10 (+19.91%)</td><td>0.09 (+13.46%)</td><td>0.08 (+19.78%)</td><td>0.03 (-4.95%)</td><td>447.90 (-16.51%)</td><td>374.06 (-17.71%)</td><td>431.90 (-11.86%)</td><td>257.90 (-2.24%)</td><td>90.76 (-16.42%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>536.50 (n/a)</td><td>454.58 (n/a)</td><td>490.00 (n/a)</td><td>263.80 (n/a)</td><td>108.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (-4.32%)</td><td>0.09 (-10.76%)</td><td>0.08 <b>(-33.85%)</b></td><td>0.05 <b>(-21.86%)</b></td><td>0.04 (-1.62%)</td><td>791.30 <b>(+27.98%)</b></td><td>474.00 (+13.84%)</td><td>476.20 <b>(+51.17%)</b></td><td>276.00 (+4.51%)</td><td>208.16 (+19.51%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>618.30 (n/a)</td><td>416.36 (n/a)</td><td>315.00 (n/a)</td><td>264.10 (n/a)</td><td>174.18 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (+1.16%)</td><td>0.07 (-8.06%)</td><td>0.06 <b>(-21.85%)</b></td><td>0.06 (-2.67%)</td><td>0.02 (+1.25%)</td><td>666.20 (+2.75%)</td><td>544.84 (+9.15%)</td><td>622.80 <b>(+27.94%)</b></td><td>357.80 (-1.16%)</td><td>139.08 (+4.91%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>648.40 (n/a)</td><td>499.18 (n/a)</td><td>486.80 (n/a)</td><td>362.00 (n/a)</td><td>132.57 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.17 (-1.00%)</td><td>0.13 (+12.43%)</td><td>0.14 (-3.04%)</td><td>0.09 <b>(+60.21%)</b></td><td>0.03 <b>(-39.76%)</b></td><td>463.10 <b>(-37.58%)</b></td><td>320.18 <b>(-22.10%)</b></td><td>298.50 (+3.14%)</td><td>239.80 (+1.01%)</td><td>84.10 <b>(-60.35%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>741.90 (n/a)</td><td>411.00 (n/a)</td><td>289.40 (n/a)</td><td>237.40 (n/a)</td><td>212.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 <b>(+29.16%)</b></td><td>0.11 (+16.03%)</td><td>0.09 (-3.16%)</td><td>0.07 (-5.98%)</td><td>0.05 <b>(+112.69%)</b></td><td>601.00 (+6.35%)</td><td>411.18 (-4.55%)</td><td>443.10 (+3.26%)</td><td>232.20 <b>(-22.57%)</b></td><td>162.02 <b>(+72.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>565.10 (n/a)</td><td>430.76 (n/a)</td><td>429.10 (n/a)</td><td>299.90 (n/a)</td><td>93.78 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.20 (+12.95%)</td><td>0.10 (-4.01%)</td><td>0.09 (+7.95%)</td><td>0.02 <b>(-68.38%)</b></td><td>0.06 <b>(+50.49%)</b></td><td>1853.60 <b>(+216.21%)</b></td><td>699.14 <b>(+54.15%)</b></td><td>441.40 (-7.37%)</td><td>208.00 (-11.45%)</td><td>657.73 <b>(+399.99%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>586.20 (n/a)</td><td>453.54 (n/a)</td><td>476.50 (n/a)</td><td>234.90 (n/a)</td><td>131.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 <b>(+20.85%)</b></td><td>0.12 (+12.91%)</td><td>0.15 <b>(+26.27%)</b></td><td>0.05 <b>(-25.05%)</b></td><td>0.06 <b>(+67.71%)</b></td><td>765.40 <b>(+33.44%)</b></td><td>416.28 (+2.47%)</td><td>277.40 <b>(-20.81%)</b></td><td>229.10 (-17.26%)</td><td>238.59 <b>(+76.58%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>573.60 (n/a)</td><td>406.24 (n/a)</td><td>350.30 (n/a)</td><td>276.90 (n/a)</td><td>135.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.19 (+18.35%)</td><td>0.10 (+4.21%)</td><td>0.08 (-6.42%)</td><td>0.02 <b>(-62.10%)</b></td><td>0.07 <b>(+53.48%)</b></td><td>1822.10 <b>(+163.84%)</b></td><td>670.42 <b>(+41.64%)</b></td><td>506.20 (+6.86%)</td><td>211.40 (-15.51%)</td><td>657.87 <b>(+261.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>690.60 (n/a)</td><td>473.32 (n/a)</td><td>473.70 (n/a)</td><td>250.20 (n/a)</td><td>182.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 (+4.44%)</td><td>0.11 (-1.46%)</td><td>0.10 (+7.67%)</td><td>0.08 (-3.54%)</td><td>0.04 (+9.42%)</td><td>483.50 (+3.67%)</td><td>386.62 (+2.60%)</td><td>393.70 (-7.12%)</td><td>228.20 (-4.24%)</td><td>106.30 (+8.68%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>466.40 (n/a)</td><td>376.82 (n/a)</td><td>423.90 (n/a)</td><td>238.30 (n/a)</td><td>97.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (-16.76%)</td><td>0.09 (-3.73%)</td><td>0.07 (-7.06%)</td><td>0.06 (+19.85%)</td><td>0.03 <b>(-25.93%)</b></td><td>567.70 (-16.56%)</td><td>428.10 (-1.95%)</td><td>468.20 (+7.58%)</td><td>286.60 <b>(+20.12%)</b></td><td>126.97 <b>(-27.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>680.40 (n/a)</td><td>436.60 (n/a)</td><td>435.20 (n/a)</td><td>238.60 (n/a)</td><td>174.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (-19.96%)</td><td>0.07 <b>(-20.71%)</b></td><td>0.06 (-11.60%)</td><td>0.06 (-1.49%)</td><td>0.03 <b>(-31.63%)</b></td><td>627.00 (+1.51%)</td><td>519.20 (+19.30%)</td><td>561.50 (+13.11%)</td><td>285.70 <b>(+24.92%)</b></td><td>136.15 (-16.30%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>617.70 (n/a)</td><td>435.20 (n/a)</td><td>496.40 (n/a)</td><td>228.70 (n/a)</td><td>162.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (-9.08%)</td><td>0.07 <b>(-33.38%)</b></td><td>0.07 <b>(-46.11%)</b></td><td>0.03 <b>(-39.72%)</b></td><td>0.04 (-7.37%)</td><td>1058.40 <b>(+65.89%)</b></td><td>606.86 <b>(+58.85%)</b></td><td>506.40 <b>(+85.56%)</b></td><td>256.60 (+9.99%)</td><td>299.93 <b>(+66.37%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>638.00 (n/a)</td><td>382.04 (n/a)</td><td>272.90 (n/a)</td><td>233.30 (n/a)</td><td>180.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.15 (-3.24%)</td><td>0.08 (-18.88%)</td><td>0.08 (-12.85%)</td><td>0.05 <b>(-29.37%)</b></td><td>0.04 (+19.09%)</td><td>725.40 <b>(+41.60%)</b></td><td>492.72 <b>(+33.33%)</b></td><td>457.20 (+14.73%)</td><td>238.30 (+3.34%)</td><td>198.23 <b>(+80.65%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>512.30 (n/a)</td><td>369.56 (n/a)</td><td>398.50 (n/a)</td><td>230.60 (n/a)</td><td>109.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (+8.70%)</td><td>0.09 (+3.61%)</td><td>0.06 <b>(-22.87%)</b></td><td>0.06 (+9.65%)</td><td>0.05 <b>(+40.08%)</b></td><td>618.60 (-8.80%)</td><td>461.62 (+4.16%)</td><td>588.40 <b>(+29.66%)</b></td><td>244.00 (-7.99%)</td><td>197.88 (+19.31%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>678.30 (n/a)</td><td>443.20 (n/a)</td><td>453.80 (n/a)</td><td>265.20 (n/a)</td><td>165.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 <b>(+51.39%)</b></td><td>0.08 (+19.57%)</td><td>0.07 (+7.30%)</td><td>0.06 (+15.87%)</td><td>0.03 <b>(+133.45%)</b></td><td>574.70 (-13.71%)</td><td>458.76 (-12.42%)</td><td>472.20 (-6.81%)</td><td>276.50 <b>(-33.95%)</b></td><td>120.75 <b>(+30.61%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>666.00 (n/a)</td><td>523.84 (n/a)</td><td>506.70 (n/a)</td><td>418.60 (n/a)</td><td>92.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.61 <b>(+47.12%)</b></td><td>0.40 <b>(+30.94%)</b></td><td>0.44 <b>(+61.98%)</b></td><td>0.22 (-0.16%)</td><td>0.16 <b>(+85.63%)</b></td><td>601.70 (+0.15%)</td><td>373.42 (-17.20%)</td><td>298.50 <b>(-38.26%)</b></td><td>215.30 <b>(-32.04%)</b></td><td>161.44 <b>(+34.56%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>600.80 (n/a)</td><td>451.00 (n/a)</td><td>483.50 (n/a)</td><td>316.80 (n/a)</td><td>119.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.47 (+11.88%)</td><td>0.35 <b>(+24.61%)</b></td><td>0.40 <b>(+61.88%)</b></td><td>0.13 <b>(-45.20%)</b></td><td>0.13 <b>(+71.09%)</b></td><td>1005.50 <b>(+82.49%)</b></td><td>460.50 (-4.92%)</td><td>328.00 <b>(-38.23%)</b></td><td>280.30 (-10.62%)</td><td>306.40 <b>(+209.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.08 (n/a)</td><td>551.00 (n/a)</td><td>484.32 (n/a)</td><td>531.00 (n/a)</td><td>313.60 (n/a)</td><td>98.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.43 (+8.78%)</td><td>0.34 (+0.35%)</td><td>0.41 (+19.46%)</td><td>0.20 <b>(-26.16%)</b></td><td>0.11 <b>(+98.16%)</b></td><td>655.80 <b>(+35.41%)</b></td><td>423.24 (+7.63%)</td><td>319.60 (-16.29%)</td><td>305.60 (-8.09%)</td><td>158.69 <b>(+142.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>484.30 (n/a)</td><td>393.22 (n/a)</td><td>381.80 (n/a)</td><td>332.50 (n/a)</td><td>65.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.00 <b>(-42.86%)</b></td><td>0.00 <b>(-44.00%)</b></td><td>0.00 <b>(-57.14%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-69.45%)</b></td><td>18429.39 (-5.20%)</td><td>15001.28 <b>(+32.89%)</b></td><td>14771.67 <b>(+149.88%)</b></td><td>10385.56 <b>(+78.65%)</b></td><td>3278.98 <b>(-55.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19441.00 (n/a)</td><td>11288.51 (n/a)</td><td>5911.49 (n/a)</td><td>5813.37 (n/a)</td><td>7441.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.00 (+7.69%)</td><td>0.00 <b>(-23.26%)</b></td><td>0.00 <b>(-37.50%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+9.99%)</td><td>19588.56 (+9.34%)</td><td>14929.13 <b>(+25.66%)</b></td><td>15933.62 <b>(+50.94%)</b></td><td>5974.46 (-6.81%)</td><td>5264.12 (-4.96%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17914.80 (n/a)</td><td>11880.14 (n/a)</td><td>10556.57 (n/a)</td><td>6410.90 (n/a)</td><td>5538.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (+2.11%)</td><td>0.10 (-1.71%)</td><td>0.08 (-2.02%)</td><td>0.07 (-5.83%)</td><td>0.03 (+12.59%)</td><td>30921.72 (+6.11%)</td><td>23220.15 (+3.61%)</td><td>25407.18 (+1.96%)</td><td>14951.41 (-2.03%)</td><td>6884.38 (+17.29%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29140.57 (n/a)</td><td>22410.87 (n/a)</td><td>24918.50 (n/a)</td><td>15260.49 (n/a)</td><td>5869.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.67 (+5.91%)</td><td>1.78 (-17.73%)</td><td>1.78 <b>(-22.65%)</b></td><td>0.52 <b>(-62.16%)</b></td><td>0.89 <b>(+87.67%)</b></td><td>2031.50 <b>(+164.24%)</b></td><td>838.14 <b>(+63.97%)</b></td><td>588.90 <b>(+29.29%)</b></td><td>392.20 (-5.58%)</td><td>684.03 <b>(+364.12%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.52 (n/a)</td><td>2.16 (n/a)</td><td>2.30 (n/a)</td><td>1.36 (n/a)</td><td>0.47 (n/a)</td><td>768.80 (n/a)</td><td>511.16 (n/a)</td><td>455.50 (n/a)</td><td>415.40 (n/a)</td><td>147.38 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.26 <b>(+24.59%)</b></td><td>1.97 (-3.05%)</td><td>1.64 (-16.69%)</td><td>1.13 <b>(-23.97%)</b></td><td>0.89 <b>(+61.05%)</b></td><td>925.90 <b>(+31.52%)</b></td><td>618.68 (+13.05%)</td><td>640.70 <b>(+20.03%)</b></td><td>321.30 (-19.76%)</td><td>250.34 <b>(+69.14%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.62 (n/a)</td><td>2.03 (n/a)</td><td>1.96 (n/a)</td><td>1.49 (n/a)</td><td>0.55 (n/a)</td><td>704.00 (n/a)</td><td>547.24 (n/a)</td><td>533.80 (n/a)</td><td>400.40 (n/a)</td><td>148.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.34 (+10.97%)</td><td>2.39 (+13.56%)</td><td>2.38 <b>(+33.59%)</b></td><td>1.63 (+5.53%)</td><td>0.68 (+12.44%)</td><td>642.60 (-5.24%)</td><td>468.76 (-11.45%)</td><td>439.70 <b>(-25.13%)</b></td><td>313.60 (-9.89%)</td><td>132.91 (-1.73%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.01 (n/a)</td><td>2.10 (n/a)</td><td>1.79 (n/a)</td><td>1.55 (n/a)</td><td>0.61 (n/a)</td><td>678.10 (n/a)</td><td>529.36 (n/a)</td><td>587.30 (n/a)</td><td>348.00 (n/a)</td><td>135.26 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>1.95 <b>(-29.22%)</b></td><td>1.64 (-19.70%)</td><td>1.80 (-7.50%)</td><td>1.02 <b>(-38.51%)</b></td><td>0.37 (-18.85%)</td><td>1031.60 <b>(+62.61%)</b></td><td>675.82 <b>(+26.95%)</b></td><td>582.90 (+8.10%)</td><td>538.70 <b>(+41.28%)</b></td><td>202.89 <b>(+90.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.75 (n/a)</td><td>2.04 (n/a)</td><td>1.94 (n/a)</td><td>1.65 (n/a)</td><td>0.45 (n/a)</td><td>634.40 (n/a)</td><td>532.34 (n/a)</td><td>539.20 (n/a)</td><td>381.30 (n/a)</td><td>106.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.94 (-3.63%)</td><td>2.53 (+8.49%)</td><td>2.50 (-15.64%)</td><td>0.58 (-0.41%)</td><td>1.31 (-10.31%)</td><td>3630.90 (+0.41%)</td><td>1316.52 (-12.44%)</td><td>838.70 (+18.54%)</td><td>532.50 (+3.76%)</td><td>1306.38 (-0.79%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>4.09 (n/a)</td><td>2.33 (n/a)</td><td>2.96 (n/a)</td><td>0.58 (n/a)</td><td>1.46 (n/a)</td><td>3616.00 (n/a)</td><td>1503.48 (n/a)</td><td>707.50 (n/a)</td><td>513.20 (n/a)</td><td>1316.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.78 (+1.87%)</td><td>2.74 <b>(-20.20%)</b></td><td>2.58 <b>(-31.47%)</b></td><td>0.58 <b>(-31.60%)</b></td><td>2.27 <b>(+27.97%)</b></td><td>3604.00 <b>(+46.20%)</b></td><td>1754.28 <b>(+88.72%)</b></td><td>813.20 <b>(+45.92%)</b></td><td>363.10 (-1.84%)</td><td>1644.71 <b>(+89.37%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.67 (n/a)</td><td>3.44 (n/a)</td><td>3.76 (n/a)</td><td>0.85 (n/a)</td><td>1.77 (n/a)</td><td>2465.20 (n/a)</td><td>929.58 (n/a)</td><td>557.30 (n/a)</td><td>369.90 (n/a)</td><td>868.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.17 (-3.40%)</td><td>3.62 (-7.51%)</td><td>3.36 (-5.74%)</td><td>2.61 (+6.21%)</td><td>0.96 <b>(-28.68%)</b></td><td>803.70 (-5.86%)</td><td>608.66 (+3.19%)</td><td>623.30 (+6.09%)</td><td>405.90 (+3.52%)</td><td>145.69 <b>(-28.05%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.35 (n/a)</td><td>3.92 (n/a)</td><td>3.57 (n/a)</td><td>2.46 (n/a)</td><td>1.35 (n/a)</td><td>853.70 (n/a)</td><td>589.84 (n/a)</td><td>587.50 (n/a)</td><td>392.10 (n/a)</td><td>202.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.59 (-4.95%)</td><td>4.00 <b>(+34.75%)</b></td><td>3.92 <b>(+91.55%)</b></td><td>2.05 <b>(+103.23%)</b></td><td>1.80 <b>(-22.17%)</b></td><td>1025.00 <b>(-50.79%)</b></td><td>621.22 <b>(-40.20%)</b></td><td>534.60 <b>(-47.80%)</b></td><td>318.20 (+5.19%)</td><td>284.59 <b>(-56.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.93 (n/a)</td><td>2.97 (n/a)</td><td>2.05 (n/a)</td><td>1.01 (n/a)</td><td>2.31 (n/a)</td><td>2083.10 (n/a)</td><td>1038.86 (n/a)</td><td>1024.10 (n/a)</td><td>302.50 (n/a)</td><td>656.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.82 (+12.79%)</td><td>3.98 (+4.82%)</td><td>3.24 (-8.57%)</td><td>2.84 <b>(+70.41%)</b></td><td>1.66 (-3.82%)</td><td>738.30 <b>(-41.32%)</b></td><td>584.10 (-13.25%)</td><td>646.70 (+9.37%)</td><td>307.60 (-11.35%)</td><td>176.92 <b>(-50.98%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.04 (n/a)</td><td>3.80 (n/a)</td><td>3.55 (n/a)</td><td>1.67 (n/a)</td><td>1.72 (n/a)</td><td>1258.10 (n/a)</td><td>673.30 (n/a)</td><td>591.30 (n/a)</td><td>347.00 (n/a)</td><td>360.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.28 (-14.96%)</td><td>2.73 <b>(-20.86%)</b></td><td>1.12 <b>(-62.00%)</b></td><td>0.57 (-2.60%)</td><td>2.74 (+10.62%)</td><td>3673.20 (+2.67%)</td><td>1979.16 <b>(+66.87%)</b></td><td>1875.10 <b>(+163.13%)</b></td><td>333.80 (+17.62%)</td><td>1634.23 <b>(+21.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>7.39 (n/a)</td><td>3.45 (n/a)</td><td>2.94 (n/a)</td><td>0.59 (n/a)</td><td>2.48 (n/a)</td><td>3577.60 (n/a)</td><td>1186.08 (n/a)</td><td>712.60 (n/a)</td><td>283.80 (n/a)</td><td>1350.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.22 (-11.16%)</td><td>3.00 <b>(-27.93%)</b></td><td>3.55 (-16.16%)</td><td>1.09 <b>(-35.15%)</b></td><td>1.83 (+18.07%)</td><td>3844.40 <b>(+54.21%)</b></td><td>2115.74 <b>(+74.20%)</b></td><td>1182.60 (+19.26%)</td><td>803.40 (+12.57%)</td><td>1518.57 <b>(+109.59%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>5.88 (n/a)</td><td>4.16 (n/a)</td><td>4.23 (n/a)</td><td>1.68 (n/a)</td><td>1.55 (n/a)</td><td>2493.00 (n/a)</td><td>1214.52 (n/a)</td><td>991.60 (n/a)</td><td>713.70 (n/a)</td><td>724.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>7.15 (+18.71%)</td><td>5.12 (+12.17%)</td><td>6.32 (+7.31%)</td><td>1.19 (+6.98%)</td><td>2.49 (+16.95%)</td><td>3523.20 (-6.53%)</td><td>1280.74 (-8.11%)</td><td>663.60 (-6.81%)</td><td>586.90 (-15.76%)</td><td>1265.27 (-5.44%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>6.02 (n/a)</td><td>4.56 (n/a)</td><td>5.89 (n/a)</td><td>1.11 (n/a)</td><td>2.13 (n/a)</td><td>3769.30 (n/a)</td><td>1393.78 (n/a)</td><td>712.10 (n/a)</td><td>696.70 (n/a)</td><td>1338.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>8.66 (-1.91%)</td><td>5.69 (+7.91%)</td><td>5.92 (+2.66%)</td><td>3.84 <b>(+252.33%)</b></td><td>1.94 <b>(-33.12%)</b></td><td>1091.70 <b>(-71.62%)</b></td><td>803.54 <b>(-40.12%)</b></td><td>708.90 (-2.60%)</td><td>484.30 (+1.96%)</td><td>252.98 <b>(-82.11%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>8.83 (n/a)</td><td>5.28 (n/a)</td><td>5.76 (n/a)</td><td>1.09 (n/a)</td><td>2.90 (n/a)</td><td>3846.40 (n/a)</td><td>1341.88 (n/a)</td><td>727.80 (n/a)</td><td>475.00 (n/a)</td><td>1414.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>9.67 (+8.82%)</td><td>6.64 (-10.62%)</td><td>6.39 (-12.81%)</td><td>4.40 <b>(-32.15%)</b></td><td>1.94 <b>(+96.21%)</b></td><td>954.30 <b>(+47.38%)</b></td><td>674.32 (+17.81%)</td><td>656.50 (+14.69%)</td><td>433.60 (-8.10%)</td><td>189.54 <b>(+160.16%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>8.89 (n/a)</td><td>7.43 (n/a)</td><td>7.33 (n/a)</td><td>6.48 (n/a)</td><td>0.99 (n/a)</td><td>647.50 (n/a)</td><td>572.36 (n/a)</td><td>572.40 (n/a)</td><td>471.80 (n/a)</td><td>72.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>9.44 (-2.15%)</td><td>5.28 <b>(-23.80%)</b></td><td>3.64 <b>(-52.39%)</b></td><td>1.17 <b>(-67.91%)</b></td><td>3.61 <b>(+27.36%)</b></td><td>3595.70 <b>(+211.59%)</b></td><td>1377.24 <b>(+93.52%)</b></td><td>1151.20 <b>(+110.00%)</b></td><td>444.10 (+2.19%)</td><td>1291.57 <b>(+288.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>9.65 (n/a)</td><td>6.93 (n/a)</td><td>7.65 (n/a)</td><td>3.63 (n/a)</td><td>2.83 (n/a)</td><td>1154.00 (n/a)</td><td>711.68 (n/a)</td><td>548.20 (n/a)</td><td>434.60 (n/a)</td><td>332.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.48 (-19.94%)</td><td>4.72 (+6.69%)</td><td>6.34 <b>(+49.98%)</b></td><td>1.08 (-7.62%)</td><td>2.43 <b>(-20.62%)</b></td><td>3884.70 (+8.25%)</td><td>1421.52 (-12.47%)</td><td>662.00 <b>(-33.32%)</b></td><td>647.20 <b>(+24.92%)</b></td><td>1401.31 (+4.90%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>8.09 (n/a)</td><td>4.43 (n/a)</td><td>4.22 (n/a)</td><td>1.17 (n/a)</td><td>3.06 (n/a)</td><td>3588.70 (n/a)</td><td>1624.10 (n/a)</td><td>992.80 (n/a)</td><td>518.10 (n/a)</td><td>1335.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>1.83 (+18.22%)</td><td>1.43 <b>(+31.69%)</b></td><td>1.45 <b>(+42.80%)</b></td><td>0.75 (-14.94%)</td><td>0.43 <b>(+61.91%)</b></td><td>699.50 (+17.56%)</td><td>404.96 (-19.05%)</td><td>362.60 <b>(-29.96%)</b></td><td>286.90 (-15.39%)</td><td>169.55 <b>(+71.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>1.55 (n/a)</td><td>1.09 (n/a)</td><td>1.01 (n/a)</td><td>0.88 (n/a)</td><td>0.27 (n/a)</td><td>595.00 (n/a)</td><td>500.24 (n/a)</td><td>517.70 (n/a)</td><td>339.10 (n/a)</td><td>99.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.45 (-7.19%)</td><td>1.55 (-11.05%)</td><td>2.32 <b>(+41.54%)</b></td><td>0.30 (-5.54%)</td><td>1.14 (+18.77%)</td><td>3512.70 (+5.86%)</td><td>1660.44 <b>(+52.01%)</b></td><td>451.50 <b>(-29.34%)</b></td><td>427.80 (+7.76%)</td><td>1669.62 <b>(+33.36%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>2.64 (n/a)</td><td>1.74 (n/a)</td><td>1.64 (n/a)</td><td>0.32 (n/a)</td><td>0.96 (n/a)</td><td>3318.10 (n/a)</td><td>1092.34 (n/a)</td><td>639.00 (n/a)</td><td>397.00 (n/a)</td><td>1251.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>4.07 (+3.89%)</td><td>2.49 (+0.05%)</td><td>2.36 <b>(-33.08%)</b></td><td>1.00 <b>(+78.30%)</b></td><td>1.14 <b>(-35.37%)</b></td><td>2097.30 <b>(-43.91%)</b></td><td>1044.76 <b>(-41.79%)</b></td><td>889.30 <b>(+49.44%)</b></td><td>514.90 (-3.76%)</td><td>618.13 <b>(-63.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>3.92 (n/a)</td><td>2.49 (n/a)</td><td>3.52 (n/a)</td><td>0.56 (n/a)</td><td>1.76 (n/a)</td><td>3739.40 (n/a)</td><td>1794.82 (n/a)</td><td>595.10 (n/a)</td><td>535.00 (n/a)</td><td>1695.50 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.42 <b>(+115.02%)</b></td><td>1.59 <b>(+51.61%)</b></td><td>1.57 <b>(+51.30%)</b></td><td>0.90 (-7.51%)</td><td>0.55 <b>(+859.54%)</b></td><td>581.30 (+8.11%)</td><td>365.12 <b>(-27.33%)</b></td><td>334.50 <b>(-33.91%)</b></td><td>216.30 <b>(-53.48%)</b></td><td>133.55 <b>(+392.20%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>1.13 (n/a)</td><td>1.05 (n/a)</td><td>1.04 (n/a)</td><td>0.98 (n/a)</td><td>0.06 (n/a)</td><td>537.70 (n/a)</td><td>502.46 (n/a)</td><td>506.10 (n/a)</td><td>465.00 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (-9.87%)</td><td>0.11 (-5.33%)</td><td>0.11 (-7.65%)</td><td>0.08 <b>(+24.25%)</b></td><td>0.02 <b>(-41.98%)</b></td><td>413.90 (-19.52%)</td><td>316.38 (-0.15%)</td><td>299.40 (+8.32%)</td><td>254.00 (+10.97%)</td><td>59.38 <b>(-48.51%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.30 (n/a)</td><td>316.86 (n/a)</td><td>276.40 (n/a)</td><td>228.90 (n/a)</td><td>115.32 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (+2.39%)</td><td>0.09 (+1.36%)</td><td>0.08 (-5.87%)</td><td>0.06 (+4.11%)</td><td>0.03 (+12.09%)</td><td>525.10 (-3.95%)</td><td>395.44 (+0.20%)</td><td>399.70 (+6.25%)</td><td>244.10 (-2.32%)</td><td>121.61 (+8.51%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>546.70 (n/a)</td><td>394.64 (n/a)</td><td>376.20 (n/a)</td><td>249.90 (n/a)</td><td>112.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.35 <b>(+36.71%)</b></td><td>0.17 (-6.23%)</td><td>0.13 (-18.25%)</td><td>0.04 <b>(-68.86%)</b></td><td>0.12 <b>(+110.41%)</b></td><td>1791.10 <b>(+221.16%)</b></td><td>676.18 <b>(+72.07%)</b></td><td>488.40 <b>(+22.31%)</b></td><td>187.30 <b>(-26.86%)</b></td><td>645.07 <b>(+427.16%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>557.70 (n/a)</td><td>392.96 (n/a)</td><td>399.30 (n/a)</td><td>256.10 (n/a)</td><td>122.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.27 <b>(+20.65%)</b></td><td>0.17 (+1.13%)</td><td>0.13 (-3.35%)</td><td>0.10 (-11.36%)</td><td>0.07 <b>(+31.52%)</b></td><td>649.50 (+12.82%)</td><td>439.44 (+3.55%)</td><td>486.50 (+3.47%)</td><td>243.00 (-17.12%)</td><td>160.81 <b>(+28.30%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>575.70 (n/a)</td><td>424.36 (n/a)</td><td>470.20 (n/a)</td><td>293.20 (n/a)</td><td>125.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.31 <b>(+22.74%)</b></td><td>0.17 (-2.46%)</td><td>0.14 (-3.56%)</td><td>0.12 (+4.59%)</td><td>0.08 <b>(+28.08%)</b></td><td>543.00 (-4.38%)</td><td>444.22 (+4.68%)</td><td>482.00 (+3.68%)</td><td>213.50 (-18.54%)</td><td>132.78 (-4.53%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>567.90 (n/a)</td><td>424.38 (n/a)</td><td>464.90 (n/a)</td><td>262.10 (n/a)</td><td>139.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.48 (+2.05%)</td><td>0.39 (+10.71%)</td><td>0.40 <b>(+38.71%)</b></td><td>0.27 (-2.37%)</td><td>0.07 <b>(-23.98%)</b></td><td>480.90 (+2.43%)</td><td>346.84 (-11.71%)</td><td>331.50 <b>(-27.92%)</b></td><td>274.80 (-2.00%)</td><td>78.56 <b>(-20.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>469.50 (n/a)</td><td>392.84 (n/a)</td><td>459.90 (n/a)</td><td>280.40 (n/a)</td><td>98.87 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.40 (-12.48%)</td><td>0.30 (+5.72%)</td><td>0.29 (+9.50%)</td><td>0.23 <b>(+222.21%)</b></td><td>0.06 <b>(-60.70%)</b></td><td>561.40 <b>(-68.96%)</b></td><td>444.96 <b>(-36.65%)</b></td><td>445.40 (-8.67%)</td><td>328.40 (+14.23%)</td><td>87.45 <b>(-86.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1808.80 (n/a)</td><td>702.40 (n/a)</td><td>487.70 (n/a)</td><td>287.50 (n/a)</td><td>633.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.54 <b>(+68.21%)</b></td><td>0.44 <b>(+52.39%)</b></td><td>0.46 <b>(+50.37%)</b></td><td>0.27 <b>(+21.12%)</b></td><td>0.10 <b>(+161.83%)</b></td><td>484.70 (-17.44%)</td><td>317.28 <b>(-31.68%)</b></td><td>287.10 <b>(-33.50%)</b></td><td>241.00 <b>(-40.54%)</b></td><td>96.17 <b>(+33.20%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>587.10 (n/a)</td><td>464.42 (n/a)</td><td>431.70 (n/a)</td><td>405.30 (n/a)</td><td>72.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (-18.78%)</td><td>0.05 (+2.49%)</td><td>0.05 <b>(+44.35%)</b></td><td>0.03 <b>(+82.42%)</b></td><td>0.01 <b>(-45.96%)</b></td><td>564.60 <b>(-45.18%)</b></td><td>367.16 <b>(-23.53%)</b></td><td>310.10 <b>(-30.73%)</b></td><td>242.20 <b>(+23.13%)</b></td><td>125.76 <b>(-62.03%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:53</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1030.00 (n/a)</td><td>480.12 (n/a)</td><td>447.70 (n/a)</td><td>196.70 (n/a)</td><td>331.24 (n/a)</td>
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
