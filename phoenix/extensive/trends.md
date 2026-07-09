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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (-3.40%)</td><td>0.02 (-10.08%)</td><td>0.01 (-8.85%)</td><td>0.01 (+16.19%)</td><td>0.01 (-15.03%)</td><td>581.90 (-13.95%)</td><td>431.34 (+6.84%)</td><td>461.80 (+9.72%)</td><td>239.30 (+3.50%)</td><td>155.09 (-15.19%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.20 (n/a)</td><td>403.74 (n/a)</td><td>420.90 (n/a)</td><td>231.20 (n/a)</td><td>182.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-3.17%)</td><td>0.02 (-15.40%)</td><td>0.01 <b>(-37.71%)</b></td><td>0.01 (+18.88%)</td><td>0.01 (+4.32%)</td><td>518.70 (-15.89%)</td><td>401.56 (+16.92%)</td><td>472.90 <b>(+60.52%)</b></td><td>247.90 (+3.25%)</td><td>131.16 (-15.30%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.70 (n/a)</td><td>343.44 (n/a)</td><td>294.60 (n/a)</td><td>240.10 (n/a)</td><td>154.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-16.15%)</td><td>0.01 <b>(-21.25%)</b></td><td>0.01 (-18.45%)</td><td>0.00 <b>(-65.17%)</b></td><td>0.01 (+13.92%)</td><td>1868.90 <b>(+187.17%)</b></td><td>707.44 <b>(+75.69%)</b></td><td>520.20 <b>(+22.63%)</b></td><td>288.10 (+19.25%)</td><td>661.94 <b>(+303.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.80 (n/a)</td><td>402.66 (n/a)</td><td>424.20 (n/a)</td><td>241.60 (n/a)</td><td>164.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (-0.26%)</td><td>0.01 <b>(-20.18%)</b></td><td>0.01 <b>(-37.92%)</b></td><td>0.01 (-5.74%)</td><td>0.01 (-8.10%)</td><td>616.20 (+6.08%)</td><td>476.16 <b>(+23.64%)</b></td><td>520.30 <b>(+61.08%)</b></td><td>241.00 (+0.25%)</td><td>160.23 (-0.66%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.90 (n/a)</td><td>385.12 (n/a)</td><td>323.00 (n/a)</td><td>240.40 (n/a)</td><td>161.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (+6.83%)</td><td>0.02 (+11.26%)</td><td>0.02 <b>(+52.75%)</b></td><td>0.01 (+12.86%)</td><td>0.01 (-4.09%)</td><td>547.80 (-11.39%)</td><td>393.90 (-12.36%)</td><td>326.60 <b>(-34.54%)</b></td><td>228.10 (-6.40%)</td><td>145.01 (-14.63%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.20 (n/a)</td><td>449.46 (n/a)</td><td>498.90 (n/a)</td><td>243.70 (n/a)</td><td>169.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (+12.37%)</td><td>0.02 (-7.33%)</td><td>0.02 <b>(-22.48%)</b></td><td>0.01 (-7.75%)</td><td>0.01 <b>(+32.03%)</b></td><td>575.20 (+8.41%)</td><td>369.00 (+12.29%)</td><td>381.00 <b>(+28.98%)</b></td><td>224.40 (-11.02%)</td><td>140.15 <b>(+20.87%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>530.60 (n/a)</td><td>328.62 (n/a)</td><td>295.40 (n/a)</td><td>252.20 (n/a)</td><td>115.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 <b>(+20.96%)</b></td><td>0.04 (+1.06%)</td><td>0.04 <b>(-27.06%)</b></td><td>0.02 (-5.94%)</td><td>0.02 <b>(+35.99%)</b></td><td>519.10 (+6.33%)</td><td>325.34 (+3.27%)</td><td>336.90 <b>(+37.12%)</b></td><td>197.90 (-17.34%)</td><td>128.96 (+18.64%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>488.20 (n/a)</td><td>315.04 (n/a)</td><td>245.70 (n/a)</td><td>239.40 (n/a)</td><td>108.70 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (-15.33%)</td><td>0.03 <b>(-35.50%)</b></td><td>0.02 <b>(-52.39%)</b></td><td>0.02 (-14.06%)</td><td>0.01 (-19.11%)</td><td>691.80 (+16.37%)</td><td>525.56 <b>(+53.09%)</b></td><td>566.40 <b>(+110.09%)</b></td><td>270.40 (+18.13%)</td><td>170.45 (+10.90%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>343.30 (n/a)</td><td>269.60 (n/a)</td><td>228.90 (n/a)</td><td>153.70 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (+8.90%)</td><td>0.03 (-17.47%)</td><td>0.02 <b>(-52.24%)</b></td><td>0.02 <b>(+305.01%)</b></td><td>0.01 <b>(-30.17%)</b></td><td>619.30 <b>(-75.31%)</b></td><td>455.56 <b>(-38.25%)</b></td><td>500.30 <b>(+109.33%)</b></td><td>217.30 (-8.16%)</td><td>150.65 <b>(-84.85%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2508.10 (n/a)</td><td>737.80 (n/a)</td><td>239.00 (n/a)</td><td>236.60 (n/a)</td><td>994.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 <b>(+24.15%)</b></td><td>0.04 <b>(+24.36%)</b></td><td>0.04 (+16.50%)</td><td>0.03 <b>(+43.66%)</b></td><td>0.01 (-10.98%)</td><td>416.50 <b>(-30.40%)</b></td><td>300.88 <b>(-22.73%)</b></td><td>291.30 (-14.17%)</td><td>231.90 (-19.45%)</td><td>69.44 <b>(-46.95%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.40 (n/a)</td><td>389.40 (n/a)</td><td>339.40 (n/a)</td><td>287.90 (n/a)</td><td>130.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (+15.41%)</td><td>0.03 <b>(-20.20%)</b></td><td>0.02 <b>(-39.65%)</b></td><td>0.01 <b>(-74.94%)</b></td><td>0.02 <b>(+105.16%)</b></td><td>1907.80 <b>(+299.12%)</b></td><td>716.04 <b>(+105.91%)</b></td><td>569.60 <b>(+65.68%)</b></td><td>208.50 (-13.34%)</td><td>687.76 <b>(+635.05%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.00 (n/a)</td><td>347.74 (n/a)</td><td>343.80 (n/a)</td><td>240.60 (n/a)</td><td>93.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (+13.98%)</td><td>0.03 <b>(-27.60%)</b></td><td>0.03 <b>(-40.19%)</b></td><td>0.02 <b>(-29.55%)</b></td><td>0.02 <b>(+60.65%)</b></td><td>598.90 <b>(+41.95%)</b></td><td>471.76 <b>(+52.53%)</b></td><td>486.10 <b>(+67.22%)</b></td><td>208.80 (-12.27%)</td><td>156.65 <b>(+96.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>421.90 (n/a)</td><td>309.28 (n/a)</td><td>290.70 (n/a)</td><td>238.00 (n/a)</td><td>79.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (-17.33%)</td><td>0.08 (+5.41%)</td><td>0.09 <b>(+86.71%)</b></td><td>0.04 (-2.48%)</td><td>0.02 <b>(-34.90%)</b></td><td>594.30 (+2.54%)</td><td>356.22 (-13.13%)</td><td>276.80 <b>(-46.44%)</b></td><td>243.20 <b>(+21.00%)</b></td><td>145.42 (-18.09%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>579.60 (n/a)</td><td>410.04 (n/a)</td><td>516.80 (n/a)</td><td>201.00 (n/a)</td><td>177.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (+11.54%)</td><td>0.09 (+7.69%)</td><td>0.09 (+16.11%)</td><td>0.06 (-15.56%)</td><td>0.02 <b>(+39.57%)</b></td><td>426.80 (+18.42%)</td><td>289.26 (-4.28%)</td><td>275.30 (-13.86%)</td><td>208.30 (-10.33%)</td><td>84.41 <b>(+51.91%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>360.40 (n/a)</td><td>302.20 (n/a)</td><td>319.60 (n/a)</td><td>232.30 (n/a)</td><td>55.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 <b>(-27.87%)</b></td><td>0.09 <b>(+31.05%)</b></td><td>0.10 <b>(+79.52%)</b></td><td>0.07 <b>(+55.55%)</b></td><td>0.01 <b>(-69.80%)</b></td><td>339.50 <b>(-35.71%)</b></td><td>268.92 <b>(-34.14%)</b></td><td>254.80 <b>(-44.29%)</b></td><td>243.40 <b>(+38.69%)</b></td><td>40.34 <b>(-71.56%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>528.10 (n/a)</td><td>408.30 (n/a)</td><td>457.40 (n/a)</td><td>175.50 (n/a)</td><td>141.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 <b>(+24.54%)</b></td><td>0.08 <b>(+28.79%)</b></td><td>0.08 <b>(+49.33%)</b></td><td>0.06 <b>(+22.20%)</b></td><td>0.02 (+8.69%)</td><td>438.60 (-18.17%)</td><td>318.48 <b>(-23.63%)</b></td><td>296.40 <b>(-33.03%)</b></td><td>230.10 (-19.69%)</td><td>89.84 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>536.00 (n/a)</td><td>417.02 (n/a)</td><td>442.60 (n/a)</td><td>286.50 (n/a)</td><td>124.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (-12.19%)</td><td>0.08 (+6.94%)</td><td>0.08 <b>(+23.79%)</b></td><td>0.06 <b>(+27.91%)</b></td><td>0.01 <b>(-55.50%)</b></td><td>409.30 <b>(-21.83%)</b></td><td>331.96 (-13.09%)</td><td>306.90 (-19.22%)</td><td>293.00 (+13.92%)</td><td>50.41 <b>(-59.58%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>523.60 (n/a)</td><td>381.94 (n/a)</td><td>379.90 (n/a)</td><td>257.20 (n/a)</td><td>124.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 <b>(+162.02%)</b></td><td>0.09 <b>(+122.69%)</b></td><td>0.10 <b>(+127.81%)</b></td><td>0.04 <b>(+300.13%)</b></td><td>0.04 <b>(+158.19%)</b></td><td>609.60 <b>(-75.01%)</b></td><td>368.42 <b>(-60.10%)</b></td><td>240.70 <b>(-56.10%)</b></td><td>177.30 <b>(-61.83%)</b></td><td>209.94 <b>(-75.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2439.10 (n/a)</td><td>923.36 (n/a)</td><td>548.30 (n/a)</td><td>464.50 (n/a)</td><td>849.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.18 <b>(-38.09%)</b></td><td>0.14 (-9.55%)</td><td>0.17 (+18.96%)</td><td>0.08 (-7.93%)</td><td>0.04 <b>(-45.18%)</b></td><td>629.50 (+8.61%)</td><td>394.20 (+1.68%)</td><td>297.10 (-15.93%)</td><td>279.60 <b>(+61.53%)</b></td><td>153.11 (-8.67%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.28 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>579.60 (n/a)</td><td>387.70 (n/a)</td><td>353.40 (n/a)</td><td>173.10 (n/a)</td><td>167.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.22 (+15.12%)</td><td>0.19 <b>(+30.30%)</b></td><td>0.19 (+19.71%)</td><td>0.13 <b>(+62.15%)</b></td><td>0.03 <b>(-37.12%)</b></td><td>371.10 <b>(-38.33%)</b></td><td>272.84 <b>(-30.80%)</b></td><td>252.70 (-16.46%)</td><td>225.10 (-13.16%)</td><td>58.25 <b>(-65.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>601.80 (n/a)</td><td>394.28 (n/a)</td><td>302.50 (n/a)</td><td>259.20 (n/a)</td><td>167.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.21 (+1.76%)</td><td>0.13 <b>(-24.03%)</b></td><td>0.11 <b>(-40.20%)</b></td><td>0.08 <b>(-20.91%)</b></td><td>0.06 <b>(+31.13%)</b></td><td>634.60 <b>(+26.44%)</b></td><td>445.92 <b>(+42.45%)</b></td><td>466.20 <b>(+67.22%)</b></td><td>233.50 (-1.73%)</td><td>179.61 <b>(+64.08%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>501.90 (n/a)</td><td>313.04 (n/a)</td><td>278.80 (n/a)</td><td>237.60 (n/a)</td><td>109.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.19 (+19.41%)</td><td>0.14 <b>(+27.95%)</b></td><td>0.12 (+12.48%)</td><td>0.10 (+16.96%)</td><td>0.04 <b>(+47.72%)</b></td><td>474.80 (-14.50%)</td><td>377.08 (-19.81%)</td><td>423.80 (-11.10%)</td><td>257.50 (-16.23%)</td><td>106.09 (+5.65%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>555.30 (n/a)</td><td>470.24 (n/a)</td><td>476.70 (n/a)</td><td>307.40 (n/a)</td><td>100.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.20 (+1.85%)</td><td>0.12 (-8.96%)</td><td>0.10 <b>(-21.44%)</b></td><td>0.06 <b>(-36.72%)</b></td><td>0.06 <b>(+23.97%)</b></td><td>835.80 <b>(+58.00%)</b></td><td>472.52 <b>(+20.37%)</b></td><td>477.70 <b>(+27.28%)</b></td><td>245.50 (-1.84%)</td><td>230.99 <b>(+81.81%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>529.00 (n/a)</td><td>392.56 (n/a)</td><td>375.30 (n/a)</td><td>250.10 (n/a)</td><td>127.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.19 (-2.21%)</td><td>0.13 (-8.02%)</td><td>0.13 <b>(-22.65%)</b></td><td>0.09 (+8.62%)</td><td>0.05 (-19.18%)</td><td>566.40 (-7.95%)</td><td>409.80 (+3.16%)</td><td>378.00 <b>(+29.27%)</b></td><td>260.40 (+2.24%)</td><td>141.79 <b>(-20.63%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>615.30 (n/a)</td><td>397.24 (n/a)</td><td>292.40 (n/a)</td><td>254.70 (n/a)</td><td>178.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (+1.93%)</td><td>0.01 (-3.59%)</td><td>0.01 (-5.65%)</td><td>0.01 <b>(+32.84%)</b></td><td>0.00 (-13.94%)</td><td>490.40 <b>(-24.73%)</b></td><td>339.96 (-2.21%)</td><td>293.90 (+5.99%)</td><td>245.40 (-1.88%)</td><td>102.31 <b>(-39.95%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>651.50 (n/a)</td><td>347.64 (n/a)</td><td>277.30 (n/a)</td><td>250.10 (n/a)</td><td>170.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (+13.08%)</td><td>0.01 <b>(+60.98%)</b></td><td>0.01 <b>(+88.90%)</b></td><td>0.00 <b>(+273.23%)</b></td><td>0.00 (-19.49%)</td><td>556.20 <b>(-73.21%)</b></td><td>368.18 <b>(-57.29%)</b></td><td>348.40 <b>(-47.06%)</b></td><td>210.00 (-11.58%)</td><td>132.62 <b>(-81.42%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2075.80 (n/a)</td><td>862.12 (n/a)</td><td>658.10 (n/a)</td><td>237.50 (n/a)</td><td>713.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 <b>(+20.20%)</b></td><td>0.01 (+13.96%)</td><td>0.01 <b>(+28.89%)</b></td><td>0.00 (-5.52%)</td><td>0.00 <b>(+25.59%)</b></td><td>571.90 (+5.83%)</td><td>376.26 (-9.26%)</td><td>370.00 <b>(-22.42%)</b></td><td>186.70 (-16.80%)</td><td>155.69 (+6.06%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>540.40 (n/a)</td><td>414.66 (n/a)</td><td>476.90 (n/a)</td><td>224.40 (n/a)</td><td>146.79 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 <b>(+21.84%)</b></td><td>0.01 (+13.45%)</td><td>0.01 <b>(+37.16%)</b></td><td>0.00 <b>(-41.81%)</b></td><td>0.00 <b>(+168.68%)</b></td><td>817.10 <b>(+71.84%)</b></td><td>417.24 (+5.46%)</td><td>265.00 <b>(-27.08%)</b></td><td>261.10 (-17.92%)</td><td>242.23 <b>(+243.31%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.50 (n/a)</td><td>395.62 (n/a)</td><td>363.40 (n/a)</td><td>318.10 (n/a)</td><td>70.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 <b>(-23.14%)</b></td><td>0.01 (-15.12%)</td><td>0.01 (-5.60%)</td><td>0.00 (-9.43%)</td><td>0.00 <b>(-51.06%)</b></td><td>602.30 (+10.41%)</td><td>461.74 (+11.45%)</td><td>460.80 (+5.93%)</td><td>360.00 <b>(+30.10%)</b></td><td>93.26 <b>(-28.19%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>545.50 (n/a)</td><td>414.30 (n/a)</td><td>435.00 (n/a)</td><td>276.70 (n/a)</td><td>129.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (-14.41%)</td><td>0.01 (+10.74%)</td><td>0.01 <b>(+20.21%)</b></td><td>0.00 (+7.81%)</td><td>0.00 <b>(-41.71%)</b></td><td>543.00 (-7.24%)</td><td>419.38 (-12.56%)</td><td>396.90 (-16.81%)</td><td>366.30 (+16.84%)</td><td>71.66 <b>(-36.32%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>585.40 (n/a)</td><td>479.64 (n/a)</td><td>477.10 (n/a)</td><td>313.50 (n/a)</td><td>112.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 <b>(-39.85%)</b></td><td>0.01 <b>(-42.02%)</b></td><td>0.01 <b>(-40.83%)</b></td><td>0.01 <b>(-45.72%)</b></td><td>0.00 (-16.76%)</td><td>612.00 <b>(+84.23%)</b></td><td>499.42 <b>(+73.64%)</b></td><td>466.10 <b>(+69.00%)</b></td><td>449.50 <b>(+66.24%)</b></td><td>66.27 <b>(+156.63%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>332.20 (n/a)</td><td>287.62 (n/a)</td><td>275.80 (n/a)</td><td>270.40 (n/a)</td><td>25.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-5.89%)</td><td>0.01 <b>(-22.25%)</b></td><td>0.01 <b>(-46.28%)</b></td><td>0.00 <b>(-72.07%)</b></td><td>0.01 <b>(+38.48%)</b></td><td>1927.70 <b>(+258.04%)</b></td><td>729.78 <b>(+91.42%)</b></td><td>581.50 <b>(+86.14%)</b></td><td>252.30 (+6.28%)</td><td>689.11 <b>(+383.68%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.40 (n/a)</td><td>381.24 (n/a)</td><td>312.40 (n/a)</td><td>237.40 (n/a)</td><td>142.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (+5.30%)</td><td>0.02 (-7.70%)</td><td>0.02 (-3.43%)</td><td>0.01 <b>(-29.99%)</b></td><td>0.01 <b>(+52.24%)</b></td><td>741.40 <b>(+42.85%)</b></td><td>387.46 <b>(+22.27%)</b></td><td>278.10 (+3.58%)</td><td>232.10 (-5.03%)</td><td>216.27 <b>(+89.75%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.00 (n/a)</td><td>316.90 (n/a)</td><td>268.50 (n/a)</td><td>244.40 (n/a)</td><td>113.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (+2.44%)</td><td>0.02 (+0.12%)</td><td>0.02 (+2.13%)</td><td>0.01 (+6.12%)</td><td>0.01 (+1.53%)</td><td>510.40 (-5.78%)</td><td>321.70 (-0.77%)</td><td>288.70 (-2.07%)</td><td>214.20 (-2.41%)</td><td>117.16 (-8.45%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>541.70 (n/a)</td><td>324.18 (n/a)</td><td>294.80 (n/a)</td><td>219.50 (n/a)</td><td>127.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 <b>(+22.55%)</b></td><td>0.01 <b>(+33.31%)</b></td><td>0.02 <b>(+47.18%)</b></td><td>0.00 <b>(+80.31%)</b></td><td>0.01 (+15.04%)</td><td>1069.50 <b>(-44.54%)</b></td><td>488.46 <b>(-35.00%)</b></td><td>319.90 <b>(-32.05%)</b></td><td>239.60 (-18.42%)</td><td>341.10 <b>(-49.40%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1928.30 (n/a)</td><td>751.50 (n/a)</td><td>470.80 (n/a)</td><td>293.70 (n/a)</td><td>674.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 <b>(+27.58%)</b></td><td>0.01 (+1.78%)</td><td>0.01 (+17.94%)</td><td>0.00 <b>(-69.23%)</b></td><td>0.01 <b>(+247.13%)</b></td><td>1999.90 <b>(+224.92%)</b></td><td>731.92 <b>(+47.31%)</b></td><td>406.90 (-15.21%)</td><td>330.80 <b>(-21.61%)</b></td><td>712.37 <b>(+864.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>615.50 (n/a)</td><td>496.86 (n/a)</td><td>479.90 (n/a)</td><td>422.00 (n/a)</td><td>73.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (-1.58%)</td><td>0.03 (-2.97%)</td><td>0.03 <b>(+30.15%)</b></td><td>0.02 (-15.54%)</td><td>0.01 (+3.41%)</td><td>616.10 (+18.41%)</td><td>416.04 (+6.12%)</td><td>334.60 <b>(-23.17%)</b></td><td>267.20 (+1.60%)</td><td>158.07 <b>(+34.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.30 (n/a)</td><td>392.04 (n/a)</td><td>435.50 (n/a)</td><td>263.00 (n/a)</td><td>117.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (-3.59%)</td><td>0.02 <b>(-26.94%)</b></td><td>0.02 <b>(-35.42%)</b></td><td>0.01 <b>(-52.60%)</b></td><td>0.01 <b>(+25.43%)</b></td><td>1115.70 <b>(+110.95%)</b></td><td>575.74 <b>(+57.93%)</b></td><td>469.60 <b>(+54.83%)</b></td><td>258.60 (+3.73%)</td><td>323.19 <b>(+177.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.90 (n/a)</td><td>364.56 (n/a)</td><td>303.30 (n/a)</td><td>249.30 (n/a)</td><td>116.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (+8.79%)</td><td>0.03 (+5.62%)</td><td>0.03 (-1.54%)</td><td>0.02 (-8.83%)</td><td>0.01 (+16.49%)</td><td>574.40 (+9.68%)</td><td>358.50 (-3.22%)</td><td>305.30 (+1.56%)</td><td>263.60 (-8.09%)</td><td>129.46 (+19.79%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.70 (n/a)</td><td>370.44 (n/a)</td><td>300.60 (n/a)</td><td>286.80 (n/a)</td><td>108.07 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 <b>(+47.26%)</b></td><td>0.03 <b>(+33.66%)</b></td><td>0.03 <b>(+23.53%)</b></td><td>0.01 <b>(+197.87%)</b></td><td>0.02 <b>(+28.54%)</b></td><td>819.80 <b>(-66.43%)</b></td><td>426.90 <b>(-46.29%)</b></td><td>314.50 (-19.05%)</td><td>214.90 <b>(-32.08%)</b></td><td>255.18 <b>(-72.39%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2442.00 (n/a)</td><td>794.86 (n/a)</td><td>388.50 (n/a)</td><td>316.40 (n/a)</td><td>924.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 <b>(-26.82%)</b></td><td>0.02 <b>(-21.55%)</b></td><td>0.02 (-5.72%)</td><td>0.01 <b>(-71.67%)</b></td><td>0.01 (-8.25%)</td><td>2061.90 <b>(+253.07%)</b></td><td>795.72 <b>(+70.92%)</b></td><td>543.10 (+6.05%)</td><td>318.90 <b>(+36.63%)</b></td><td>718.05 <b>(+409.75%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>584.00 (n/a)</td><td>465.56 (n/a)</td><td>512.10 (n/a)</td><td>233.40 (n/a)</td><td>140.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 <b>(+97.71%)</b></td><td>0.03 <b>(+36.90%)</b></td><td>0.03 <b>(+36.85%)</b></td><td>0.02 (-8.60%)</td><td>0.02 <b>(+181.79%)</b></td><td>612.70 (+9.41%)</td><td>381.68 (-17.43%)</td><td>371.30 <b>(-26.92%)</b></td><td>175.30 <b>(-49.41%)</b></td><td>160.08 <b>(+52.35%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.00 (n/a)</td><td>462.26 (n/a)</td><td>508.10 (n/a)</td><td>346.50 (n/a)</td><td>105.07 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (+1.40%)</td><td>0.07 (+15.59%)</td><td>0.08 <b>(+78.92%)</b></td><td>0.03 <b>(-22.06%)</b></td><td>0.02 (+15.34%)</td><td>654.70 <b>(+28.30%)</b></td><td>357.96 (-8.80%)</td><td>248.80 <b>(-44.12%)</b></td><td>243.10 (-1.38%)</td><td>177.93 <b>(+40.76%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>510.30 (n/a)</td><td>392.50 (n/a)</td><td>445.20 (n/a)</td><td>246.50 (n/a)</td><td>126.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (+8.93%)</td><td>0.06 (+11.43%)</td><td>0.05 (-0.24%)</td><td>0.03 <b>(+221.29%)</b></td><td>0.02 <b>(-25.57%)</b></td><td>620.30 <b>(-68.88%)</b></td><td>419.64 <b>(-40.42%)</b></td><td>416.50 (+0.24%)</td><td>242.60 (-8.21%)</td><td>139.59 <b>(-80.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1993.10 (n/a)</td><td>704.38 (n/a)</td><td>415.50 (n/a)</td><td>264.30 (n/a)</td><td>728.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 <b>(+62.16%)</b></td><td>0.07 <b>(+50.39%)</b></td><td>0.07 <b>(+72.74%)</b></td><td>0.04 (+4.05%)</td><td>0.03 <b>(+122.21%)</b></td><td>582.40 (-3.89%)</td><td>353.68 <b>(-24.32%)</b></td><td>284.50 <b>(-42.12%)</b></td><td>174.30 <b>(-38.34%)</b></td><td>173.91 <b>(+43.68%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.00 (n/a)</td><td>467.36 (n/a)</td><td>491.50 (n/a)</td><td>282.70 (n/a)</td><td>121.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 <b>(+69.70%)</b></td><td>0.05 <b>(+29.56%)</b></td><td>0.04 (-4.39%)</td><td>0.04 <b>(+242.70%)</b></td><td>0.02 <b>(+30.56%)</b></td><td>569.60 <b>(-70.82%)</b></td><td>459.44 <b>(-39.42%)</b></td><td>497.50 (+4.58%)</td><td>240.30 <b>(-41.07%)</b></td><td>128.27 <b>(-80.79%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1951.90 (n/a)</td><td>758.40 (n/a)</td><td>475.70 (n/a)</td><td>407.80 (n/a)</td><td>667.87 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 <b>(+28.60%)</b></td><td>0.06 <b>(+22.72%)</b></td><td>0.08 <b>(+52.35%)</b></td><td>0.01 <b>(-73.87%)</b></td><td>0.03 <b>(+337.15%)</b></td><td>1887.90 <b>(+282.71%)</b></td><td>599.20 <b>(+44.27%)</b></td><td>279.00 <b>(-34.37%)</b></td><td>271.80 <b>(-22.23%)</b></td><td>720.42 <b>(+1226.62%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>493.30 (n/a)</td><td>415.34 (n/a)</td><td>425.10 (n/a)</td><td>349.50 (n/a)</td><td>54.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (+8.52%)</td><td>0.04 (-6.57%)</td><td>0.04 (-16.12%)</td><td>0.04 (-1.22%)</td><td>0.01 <b>(+37.40%)</b></td><td>574.50 (+1.25%)</td><td>524.88 (+8.20%)</td><td>562.30 (+19.21%)</td><td>376.40 (-7.86%)</td><td>83.64 <b>(+24.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>567.40 (n/a)</td><td>485.10 (n/a)</td><td>471.70 (n/a)</td><td>408.50 (n/a)</td><td>66.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>271.40 (n/a)</td><td>255.10 (n/a)</td><td>261.60 (n/a)</td><td>235.20 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>306.10 (n/a)</td><td>264.20 (n/a)</td><td>267.70 (n/a)</td><td>214.20 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>453.40 (n/a)</td><td>398.42 (n/a)</td><td>410.30 (n/a)</td><td>313.70 (n/a)</td><td>52.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>448.80 (n/a)</td><td>307.56 (n/a)</td><td>270.50 (n/a)</td><td>250.70 (n/a)</td><td>80.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1901.20 (n/a)</td><td>734.18 (n/a)</td><td>457.20 (n/a)</td><td>331.70 (n/a)</td><td>657.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.40 (n/a)</td><td>411.88 (n/a)</td><td>435.10 (n/a)</td><td>258.60 (n/a)</td><td>87.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>527.10 (n/a)</td><td>351.18 (n/a)</td><td>279.40 (n/a)</td><td>250.00 (n/a)</td><td>123.14 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>447.80 (n/a)</td><td>363.68 (n/a)</td><td>441.20 (n/a)</td><td>223.60 (n/a)</td><td>110.31 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>542.30 (n/a)</td><td>453.92 (n/a)</td><td>522.70 (n/a)</td><td>251.20 (n/a)</td><td>122.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.23 (+12.74%)</td><td>0.16 (-5.02%)</td><td>0.17 (+2.13%)</td><td>0.09 <b>(-24.58%)</b></td><td>0.06 <b>(+77.71%)</b></td><td>576.30 <b>(+32.57%)</b></td><td>357.94 (+16.09%)</td><td>289.30 (-2.06%)</td><td>210.90 (-11.31%)</td><td>153.74 <b>(+104.99%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>434.70 (n/a)</td><td>308.32 (n/a)</td><td>295.40 (n/a)</td><td>237.80 (n/a)</td><td>75.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2417.40 (n/a)</td><td>799.16 (n/a)</td><td>457.20 (n/a)</td><td>267.70 (n/a)</td><td>911.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1955.70 (n/a)</td><td>667.20 (n/a)</td><td>326.20 (n/a)</td><td>255.50 (n/a)</td><td>726.31 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>531.40 (n/a)</td><td>360.16 (n/a)</td><td>302.90 (n/a)</td><td>215.40 (n/a)</td><td>136.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.00 (n/a)</td><td>310.10 (n/a)</td><td>241.90 (n/a)</td><td>229.30 (n/a)</td><td>133.45 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2492.50 (n/a)</td><td>889.40 (n/a)</td><td>530.00 (n/a)</td><td>402.10 (n/a)</td><td>897.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>294.70 (n/a)</td><td>278.00 (n/a)</td><td>281.50 (n/a)</td><td>259.60 (n/a)</td><td>16.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.20 (n/a)</td><td>436.70 (n/a)</td><td>505.60 (n/a)</td><td>238.50 (n/a)</td><td>123.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1827.20 (n/a)</td><td>744.62 (n/a)</td><td>529.80 (n/a)</td><td>243.40 (n/a)</td><td>620.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>560.90 (n/a)</td><td>371.94 (n/a)</td><td>301.80 (n/a)</td><td>205.60 (n/a)</td><td>167.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>621.80 (n/a)</td><td>435.02 (n/a)</td><td>504.40 (n/a)</td><td>244.10 (n/a)</td><td>174.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.70 (n/a)</td><td>448.44 (n/a)</td><td>485.80 (n/a)</td><td>272.40 (n/a)</td><td>106.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>538.00 (n/a)</td><td>383.16 (n/a)</td><td>323.90 (n/a)</td><td>264.30 (n/a)</td><td>134.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>565.60 (n/a)</td><td>427.82 (n/a)</td><td>493.00 (n/a)</td><td>233.60 (n/a)</td><td>151.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.00 (n/a)</td><td>374.58 (n/a)</td><td>301.00 (n/a)</td><td>268.30 (n/a)</td><td>119.67 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.10 (n/a)</td><td>415.90 (n/a)</td><td>414.90 (n/a)</td><td>237.00 (n/a)</td><td>157.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.20 (n/a)</td><td>479.72 (n/a)</td><td>533.20 (n/a)</td><td>177.50 (n/a)</td><td>173.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1063.50 (n/a)</td><td>518.28 (n/a)</td><td>347.90 (n/a)</td><td>238.10 (n/a)</td><td>346.03 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1938.60 (n/a)</td><td>658.26 (n/a)</td><td>446.70 (n/a)</td><td>182.70 (n/a)</td><td>727.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.80 (n/a)</td><td>430.66 (n/a)</td><td>357.60 (n/a)</td><td>304.80 (n/a)</td><td>139.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.30 (n/a)</td><td>376.38 (n/a)</td><td>404.90 (n/a)</td><td>271.30 (n/a)</td><td>101.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2505.20 (n/a)</td><td>757.92 (n/a)</td><td>345.80 (n/a)</td><td>247.70 (n/a)</td><td>979.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>734.50 (n/a)</td><td>382.34 (n/a)</td><td>273.50 (n/a)</td><td>241.70 (n/a)</td><td>204.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.80 (n/a)</td><td>323.90 (n/a)</td><td>243.70 (n/a)</td><td>197.50 (n/a)</td><td>135.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.00 (n/a)</td><td>383.36 (n/a)</td><td>443.20 (n/a)</td><td>229.80 (n/a)</td><td>138.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.50 (n/a)</td><td>458.32 (n/a)</td><td>409.20 (n/a)</td><td>392.90 (n/a)</td><td>90.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.20 (n/a)</td><td>389.46 (n/a)</td><td>397.10 (n/a)</td><td>223.10 (n/a)</td><td>131.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>969.40 (n/a)</td><td>479.58 (n/a)</td><td>418.90 (n/a)</td><td>265.30 (n/a)</td><td>286.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>531.80 (n/a)</td><td>382.40 (n/a)</td><td>374.00 (n/a)</td><td>221.20 (n/a)</td><td>130.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>530.00 (n/a)</td><td>309.74 (n/a)</td><td>271.70 (n/a)</td><td>226.10 (n/a)</td><td>125.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2163.60 (n/a)</td><td>871.74 (n/a)</td><td>617.60 (n/a)</td><td>440.10 (n/a)</td><td>726.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>516.60 (n/a)</td><td>411.32 (n/a)</td><td>376.60 (n/a)</td><td>307.30 (n/a)</td><td>88.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>664.20 (n/a)</td><td>425.22 (n/a)</td><td>377.30 (n/a)</td><td>261.50 (n/a)</td><td>165.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.60 (n/a)</td><td>388.42 (n/a)</td><td>393.50 (n/a)</td><td>262.50 (n/a)</td><td>118.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>495.10 (n/a)</td><td>339.64 (n/a)</td><td>313.70 (n/a)</td><td>156.00 (n/a)</td><td>132.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>619.80 (n/a)</td><td>469.86 (n/a)</td><td>504.80 (n/a)</td><td>291.60 (n/a)</td><td>154.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>686.30 (n/a)</td><td>496.84 (n/a)</td><td>485.90 (n/a)</td><td>304.60 (n/a)</td><td>174.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.54 (-0.40%)</td><td>0.45 (+6.71%)</td><td>0.46 <b>(+30.76%)</b></td><td>0.37 (+11.17%)</td><td>0.07 <b>(-35.76%)</b></td><td>604.70 (-10.04%)</td><td>502.54 (-9.01%)</td><td>481.90 <b>(-23.52%)</b></td><td>407.00 (+0.39%)</td><td>76.34 <b>(-40.55%)</b></td><td>23.19 (-0.40%)</td><td>19.13 (+6.71%)</td><td>19.58 <b>(+30.76%)</b></td><td>15.61 (+11.17%)</td><td>2.91 <b>(-35.76%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.11 (n/a)</td><td>672.20 (n/a)</td><td>552.32 (n/a)</td><td>630.10 (n/a)</td><td>405.40 (n/a)</td><td>128.41 (n/a)</td><td>23.28 (n/a)</td><td>17.93 (n/a)</td><td>14.98 (n/a)</td><td>14.04 (n/a)</td><td>4.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.57 (+5.59%)</td><td>0.47 (+11.62%)</td><td>0.50 (+7.04%)</td><td>0.23 (+8.19%)</td><td>0.14 (-2.71%)</td><td>965.20 (-7.57%)</td><td>531.30 (-11.41%)</td><td>440.20 (-6.58%)</td><td>388.60 (-5.29%)</td><td>244.03 (-8.80%)</td><td>24.29 (+5.59%)</td><td>19.88 (+11.62%)</td><td>21.44 (+7.04%)</td><td>9.78 (+8.19%)</td><td>5.83 (-2.71%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.47 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>1044.30 (n/a)</td><td>599.76 (n/a)</td><td>471.20 (n/a)</td><td>410.30 (n/a)</td><td>267.57 (n/a)</td><td>23.00 (n/a)</td><td>17.81 (n/a)</td><td>20.03 (n/a)</td><td>9.04 (n/a)</td><td>5.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.31 (+0.54%)</td><td>0.31 (+0.29%)</td><td>0.31 (+0.80%)</td><td>0.29 (-0.81%)</td><td>0.01 <b>(+23.65%)</b></td><td>85725.20 (+0.82%)</td><td>82304.54 (-0.27%)</td><td>81708.70 (-0.80%)</td><td>80699.90 (-0.54%)</td><td>1964.10 <b>(+24.70%)</b></td><td>212.89 (+0.54%)</td><td>208.83 (+0.29%)</td><td>210.26 (+0.80%)</td><td>200.41 (-0.81%)</td><td>4.85 <b>(+23.65%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>85030.00 (n/a)</td><td>82527.08 (n/a)</td><td>82365.30 (n/a)</td><td>81139.30 (n/a)</td><td>1575.03 (n/a)</td><td>211.73 (n/a)</td><td>208.23 (n/a)</td><td>208.58 (n/a)</td><td>202.04 (n/a)</td><td>3.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.03 (-2.08%)</td><td>1.00 (+0.21%)</td><td>1.00 (-0.30%)</td><td>0.98 (+1.83%)</td><td>0.02 <b>(-47.11%)</b></td><td>25707.00 (-1.80%)</td><td>25144.14 (-0.28%)</td><td>25175.60 (+0.30%)</td><td>24466.90 (+2.12%)</td><td>463.70 <b>(-47.09%)</b></td><td>702.17 (-2.08%)</td><td>683.44 (+0.21%)</td><td>682.40 (-0.30%)</td><td>668.29 (+1.83%)</td><td>12.68 <b>(-47.11%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>1.05 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.96 (n/a)</td><td>0.04 (n/a)</td><td>26176.90 (n/a)</td><td>25214.48 (n/a)</td><td>25100.50 (n/a)</td><td>23958.70 (n/a)</td><td>876.37 (n/a)</td><td>717.06 (n/a)</td><td>682.02 (n/a)</td><td>684.44 (n/a)</td><td>656.30 (n/a)</td><td>23.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.83 (+0.92%)</td><td>0.81 (-0.25%)</td><td>0.81 (-0.69%)</td><td>0.78 (-1.28%)</td><td>0.02 <b>(+45.04%)</b></td><td>96599.20 (+1.29%)</td><td>93509.58 (+0.27%)</td><td>93383.50 (+0.70%)</td><td>91205.00 (-0.91%)</td><td>2087.05 <b>(+45.85%)</b></td><td>753.46 (+0.92%)</td><td>735.18 (-0.25%)</td><td>735.88 (-0.69%)</td><td>711.39 (-1.28%)</td><td>16.27 <b>(+45.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95366.60 (n/a)</td><td>93260.06 (n/a)</td><td>92735.30 (n/a)</td><td>92041.60 (n/a)</td><td>1430.93 (n/a)</td><td>746.61 (n/a)</td><td>737.00 (n/a)</td><td>741.03 (n/a)</td><td>720.58 (n/a)</td><td>11.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.78 (+0.94%)</td><td>0.77 (+1.36%)</td><td>0.77 (+0.21%)</td><td>0.76 (+5.09%)</td><td>0.01 <b>(-58.29%)</b></td><td>99207.70 (-4.84%)</td><td>97959.44 (-1.39%)</td><td>97936.80 (-0.21%)</td><td>96662.80 (-0.93%)</td><td>1089.31 <b>(-60.81%)</b></td><td>710.92 (+0.94%)</td><td>701.58 (+1.36%)</td><td>701.67 (+0.21%)</td><td>692.68 (+5.09%)</td><td>7.80 <b>(-58.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>104255.10 (n/a)</td><td>99339.70 (n/a)</td><td>98145.70 (n/a)</td><td>97568.40 (n/a)</td><td>2779.77 (n/a)</td><td>704.32 (n/a)</td><td>692.18 (n/a)</td><td>700.18 (n/a)</td><td>659.15 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.80 (+0.35%)</td><td>0.79 (+0.34%)</td><td>0.79 (+0.78%)</td><td>0.78 (-0.27%)</td><td>0.01 <b>(+36.19%)</b></td><td>96840.60 (+0.27%)</td><td>95370.44 (-0.33%)</td><td>94970.20 (-0.77%)</td><td>94102.00 (-0.35%)</td><td>1119.20 <b>(+36.28%)</b></td><td>730.27 (+0.35%)</td><td>720.63 (+0.34%)</td><td>723.59 (+0.78%)</td><td>709.61 (-0.27%)</td><td>8.43 <b>(+36.19%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96578.80 (n/a)</td><td>95686.26 (n/a)</td><td>95708.80 (n/a)</td><td>94428.90 (n/a)</td><td>821.24 (n/a)</td><td>727.74 (n/a)</td><td>718.22 (n/a)</td><td>718.01 (n/a)</td><td>711.54 (n/a)</td><td>6.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.76 (+3.22%)</td><td>4.56 (-3.57%)</td><td>5.33 (-0.49%)</td><td>2.78 <b>(+35.75%)</b></td><td>1.33 (-11.93%)</td><td>3200.90 <b>(-26.34%)</b></td><td>2120.10 (-3.19%)</td><td>1673.40 (+0.49%)</td><td>1548.00 (-3.12%)</td><td>726.20 <b>(-39.80%)</b></td><td>346.82 (+3.22%)</td><td>274.97 (-3.57%)</td><td>320.83 (-0.49%)</td><td>167.72 <b>(+35.75%)</b></td><td>80.16 (-11.93%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.58 (n/a)</td><td>4.73 (n/a)</td><td>5.35 (n/a)</td><td>2.05 (n/a)</td><td>1.51 (n/a)</td><td>4345.30 (n/a)</td><td>2190.02 (n/a)</td><td>1665.20 (n/a)</td><td>1597.80 (n/a)</td><td>1206.22 (n/a)</td><td>336.01 (n/a)</td><td>285.14 (n/a)</td><td>322.40 (n/a)</td><td>123.55 (n/a)</td><td>91.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.53 <b>(-26.12%)</b></td><td>2.62 <b>(-21.52%)</b></td><td>2.27 <b>(-28.73%)</b></td><td>2.20 (-3.04%)</td><td>0.59 <b>(-36.99%)</b></td><td>4049.80 (+3.14%)</td><td>3521.64 <b>(+24.41%)</b></td><td>3930.50 <b>(+40.31%)</b></td><td>2522.80 <b>(+35.37%)</b></td><td>692.46 (-8.75%)</td><td>212.81 <b>(-26.12%)</b></td><td>157.99 <b>(-21.52%)</b></td><td>136.59 <b>(-28.73%)</b></td><td>132.57 (-3.04%)</td><td>35.46 <b>(-36.99%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.78 (n/a)</td><td>3.34 (n/a)</td><td>3.18 (n/a)</td><td>2.27 (n/a)</td><td>0.93 (n/a)</td><td>3926.60 (n/a)</td><td>2830.70 (n/a)</td><td>2801.30 (n/a)</td><td>1863.70 (n/a)</td><td>758.90 (n/a)</td><td>288.06 (n/a)</td><td>201.33 (n/a)</td><td>191.65 (n/a)</td><td>136.73 (n/a)</td><td>56.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.27 <b>(+24.73%)</b></td><td>3.67 (+0.09%)</td><td>3.97 (-1.15%)</td><td>2.20 <b>(-23.55%)</b></td><td>1.20 <b>(+89.66%)</b></td><td>4048.70 <b>(+30.81%)</b></td><td>2672.38 (+7.00%)</td><td>2242.90 (+1.16%)</td><td>1690.00 (-19.83%)</td><td>945.73 <b>(+103.99%)</b></td><td>317.68 <b>(+24.73%)</b></td><td>220.81 (+0.09%)</td><td>239.37 (-1.15%)</td><td>132.60 <b>(-23.55%)</b></td><td>72.53 <b>(+89.66%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.23 (n/a)</td><td>3.66 (n/a)</td><td>4.02 (n/a)</td><td>2.88 (n/a)</td><td>0.63 (n/a)</td><td>3095.10 (n/a)</td><td>2497.66 (n/a)</td><td>2217.10 (n/a)</td><td>2107.90 (n/a)</td><td>463.61 (n/a)</td><td>254.69 (n/a)</td><td>220.62 (n/a)</td><td>242.15 (n/a)</td><td>173.46 (n/a)</td><td>38.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>6.59 (+14.55%)</td><td>5.24 (+11.69%)</td><td>5.22 (+15.65%)</td><td>3.56 (-14.89%)</td><td>1.13 <b>(+83.67%)</b></td><td>9800.10 (+17.50%)</td><td>6951.28 (-7.66%)</td><td>6674.70 (-13.53%)</td><td>5287.30 (-12.70%)</td><td>1727.86 <b>(+99.47%)</b></td><td>406.16 (+14.55%)</td><td>322.51 (+11.69%)</td><td>321.74 (+15.65%)</td><td>219.13 (-14.89%)</td><td>69.62 <b>(+83.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.76 (n/a)</td><td>4.69 (n/a)</td><td>4.52 (n/a)</td><td>4.18 (n/a)</td><td>0.62 (n/a)</td><td>8340.50 (n/a)</td><td>7527.76 (n/a)</td><td>7719.10 (n/a)</td><td>6056.80 (n/a)</td><td>866.23 (n/a)</td><td>354.56 (n/a)</td><td>288.75 (n/a)</td><td>278.20 (n/a)</td><td>257.48 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.38 (-2.13%)</td><td>5.02 (+2.52%)</td><td>5.23 (+1.04%)</td><td>4.10 (+18.64%)</td><td>0.52 <b>(-36.60%)</b></td><td>8503.50 (-15.71%)</td><td>7017.34 (-4.29%)</td><td>6662.60 (-1.03%)</td><td>6480.80 (+2.18%)</td><td>839.39 <b>(-46.08%)</b></td><td>331.36 (-2.13%)</td><td>309.10 (+2.52%)</td><td>322.32 (+1.04%)</td><td>252.54 (+18.64%)</td><td>32.15 <b>(-36.60%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.50 (n/a)</td><td>4.89 (n/a)</td><td>5.18 (n/a)</td><td>3.46 (n/a)</td><td>0.82 (n/a)</td><td>10088.50 (n/a)</td><td>7331.72 (n/a)</td><td>6732.10 (n/a)</td><td>6342.80 (n/a)</td><td>1556.84 (n/a)</td><td>338.57 (n/a)</td><td>301.49 (n/a)</td><td>318.99 (n/a)</td><td>212.86 (n/a)</td><td>50.70 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>6.42 (+12.21%)</td><td>5.89 (+13.29%)</td><td>5.93 (+17.44%)</td><td>4.83 (-0.19%)</td><td>0.64 <b>(+74.54%)</b></td><td>7219.20 (+0.19%)</td><td>5978.58 (-11.13%)</td><td>5878.60 (-14.85%)</td><td>5427.30 (-10.88%)</td><td>727.75 <b>(+57.60%)</b></td><td>395.68 (+12.21%)</td><td>363.03 (+13.29%)</td><td>365.30 (+17.44%)</td><td>297.47 (-0.19%)</td><td>39.52 <b>(+74.54%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.72 (n/a)</td><td>5.20 (n/a)</td><td>5.05 (n/a)</td><td>4.84 (n/a)</td><td>0.37 (n/a)</td><td>7205.70 (n/a)</td><td>6727.56 (n/a)</td><td>6904.10 (n/a)</td><td>6090.00 (n/a)</td><td>461.78 (n/a)</td><td>352.63 (n/a)</td><td>320.45 (n/a)</td><td>311.05 (n/a)</td><td>298.03 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.79 (+0.77%)</td><td>0.77 (-0.23%)</td><td>0.77 (-0.55%)</td><td>0.75 (-0.75%)</td><td>0.01 (+5.67%)</td><td>100864.70 (+0.75%)</td><td>98429.32 (+0.23%)</td><td>98552.00 (+0.55%)</td><td>95814.00 (-0.76%)</td><td>1797.99 (+5.65%)</td><td>717.22 (+0.77%)</td><td>698.35 (-0.23%)</td><td>697.29 (-0.55%)</td><td>681.30 (-0.75%)</td><td>12.80 (+5.67%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100111.40 (n/a)</td><td>98200.78 (n/a)</td><td>98010.50 (n/a)</td><td>96552.00 (n/a)</td><td>1701.87 (n/a)</td><td>711.74 (n/a)</td><td>699.95 (n/a)</td><td>701.14 (n/a)</td><td>686.43 (n/a)</td><td>12.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.77 (+0.78%)</td><td>0.74 (-0.69%)</td><td>0.73 (-2.44%)</td><td>0.72 (-0.95%)</td><td>0.02 <b>(+59.25%)</b></td><td>104619.70 (+0.95%)</td><td>101507.38 (+0.74%)</td><td>102852.30 (+2.50%)</td><td>97995.30 (-0.77%)</td><td>2815.60 <b>(+58.56%)</b></td><td>701.25 (+0.78%)</td><td>677.41 (-0.69%)</td><td>668.14 (-2.44%)</td><td>656.85 (-0.95%)</td><td>18.92 <b>(+59.25%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.01 (n/a)</td><td>103630.30 (n/a)</td><td>100764.74 (n/a)</td><td>100347.80 (n/a)</td><td>98759.40 (n/a)</td><td>1775.70 (n/a)</td><td>695.83 (n/a)</td><td>682.15 (n/a)</td><td>684.81 (n/a)</td><td>663.12 (n/a)</td><td>11.88 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.81 (+0.36%)</td><td>0.80 (-0.10%)</td><td>0.80 (-0.44%)</td><td>0.80 (-0.19%)</td><td>0.01 <b>(+24.23%)</b></td><td>94902.20 (+0.19%)</td><td>94109.98 (+0.10%)</td><td>94210.20 (+0.44%)</td><td>93012.30 (-0.36%)</td><td>686.02 <b>(+23.79%)</b></td><td>738.82 (+0.36%)</td><td>730.24 (-0.10%)</td><td>729.43 (-0.44%)</td><td>724.11 (-0.19%)</td><td>5.35 <b>(+24.23%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94721.10 (n/a)</td><td>94018.50 (n/a)</td><td>93800.20 (n/a)</td><td>93343.90 (n/a)</td><td>554.17 (n/a)</td><td>736.20 (n/a)</td><td>730.93 (n/a)</td><td>732.62 (n/a)</td><td>725.49 (n/a)</td><td>4.31 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.83 (-1.98%)</td><td>3.28 <b>(+41.60%)</b></td><td>3.71 <b>(+106.05%)</b></td><td>1.67 <b>(+47.76%)</b></td><td>0.91 <b>(-27.06%)</b></td><td>4826.30 <b>(-32.32%)</b></td><td>2717.84 <b>(-38.12%)</b></td><td>2174.30 <b>(-51.47%)</b></td><td>2102.40 (+2.02%)</td><td>1182.08 <b>(-46.16%)</b></td><td>1005.50 (-1.98%)</td><td>860.81 <b>(+41.60%)</b></td><td>972.22 <b>(+106.05%)</b></td><td>438.00 <b>(+47.76%)</b></td><td>239.43 <b>(-27.06%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.91 (n/a)</td><td>2.32 (n/a)</td><td>1.80 (n/a)</td><td>1.13 (n/a)</td><td>1.25 (n/a)</td><td>7131.50 (n/a)</td><td>4392.18 (n/a)</td><td>4480.20 (n/a)</td><td>2060.80 (n/a)</td><td>2195.73 (n/a)</td><td>1025.79 (n/a)</td><td>607.92 (n/a)</td><td>471.84 (n/a)</td><td>296.42 (n/a)</td><td>328.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.25 (-18.20%)</td><td>0.21 (+0.16%)</td><td>0.22 (+17.67%)</td><td>0.17 (-4.54%)</td><td>0.03 <b>(-38.05%)</b></td><td>7308.90 (+4.76%)</td><td>5918.48 (-2.02%)</td><td>5569.10 (-15.02%)</td><td>4932.10 <b>(+22.24%)</b></td><td>966.41 (-17.18%)</td><td>13.61 (-18.20%)</td><td>11.57 (+0.16%)</td><td>12.05 (+17.67%)</td><td>9.18 (-4.54%)</td><td>1.79 <b>(-38.05%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>6977.10 (n/a)</td><td>6040.74 (n/a)</td><td>6553.20 (n/a)</td><td>4034.70 (n/a)</td><td>1166.84 (n/a)</td><td>16.63 (n/a)</td><td>11.55 (n/a)</td><td>10.24 (n/a)</td><td>9.62 (n/a)</td><td>2.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (-0.97%)</td><td>0.10 (-10.43%)</td><td>0.08 <b>(-22.93%)</b></td><td>0.08 (-14.59%)</td><td>0.03 <b>(+39.29%)</b></td><td>0.13 (-0.97%)</td><td>0.10 (-10.43%)</td><td>0.08 <b>(-22.93%)</b></td><td>0.07 (-14.59%)</td><td>0.03 <b>(+39.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.79 (-2.22%)</td><td>3.70 (+8.38%)</td><td>3.73 (+9.72%)</td><td>3.50 (+18.10%)</td><td>0.11 <b>(-64.65%)</b></td><td>3.79 (-2.22%)</td><td>3.70 (+8.38%)</td><td>3.73 (+9.72%)</td><td>3.50 (+18.10%)</td><td>0.11 <b>(-64.65%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.87 (n/a)</td><td>3.42 (n/a)</td><td>3.40 (n/a)</td><td>2.97 (n/a)</td><td>0.32 (n/a)</td><td>3.87 (n/a)</td><td>3.41 (n/a)</td><td>3.40 (n/a)</td><td>2.96 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.55 <b>(+26.35%)</b></td><td>6.46 (+10.74%)</td><td>6.25 (+4.87%)</td><td>5.46 (-1.40%)</td><td>0.97 <b>(+403.48%)</b></td><td>7.55 <b>(+26.35%)</b></td><td>6.46 (+10.74%)</td><td>6.25 (+4.87%)</td><td>5.46 (-1.40%)</td><td>0.97 <b>(+403.48%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.98 (n/a)</td><td>5.84 (n/a)</td><td>5.96 (n/a)</td><td>5.54 (n/a)</td><td>0.19 (n/a)</td><td>5.97 (n/a)</td><td>5.83 (n/a)</td><td>5.96 (n/a)</td><td>5.54 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>9.82 <b>(-30.39%)</b></td><td>8.47 <b>(-29.86%)</b></td><td>8.39 <b>(-37.18%)</b></td><td>7.41 (-7.48%)</td><td>0.89 <b>(-65.15%)</b></td><td>9.81 <b>(-30.39%)</b></td><td>8.47 <b>(-29.86%)</b></td><td>8.39 <b>(-37.18%)</b></td><td>7.41 (-7.48%)</td><td>0.89 <b>(-65.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>14.11 (n/a)</td><td>12.08 (n/a)</td><td>13.36 (n/a)</td><td>8.01 (n/a)</td><td>2.54 (n/a)</td><td>14.10 (n/a)</td><td>12.07 (n/a)</td><td>13.35 (n/a)</td><td>8.01 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.78 (-3.19%)</td><td>3.60 (-1.12%)</td><td>3.58 (-2.38%)</td><td>3.30 (-1.61%)</td><td>0.20 (-8.82%)</td><td>3.78 (-3.19%)</td><td>3.59 (-1.12%)</td><td>3.57 (-2.38%)</td><td>3.30 (-1.61%)</td><td>0.20 (-8.82%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.91 (n/a)</td><td>3.64 (n/a)</td><td>3.66 (n/a)</td><td>3.36 (n/a)</td><td>0.22 (n/a)</td><td>3.91 (n/a)</td><td>3.64 (n/a)</td><td>3.66 (n/a)</td><td>3.36 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.06 (-4.93%)</td><td>6.16 (-2.41%)</td><td>5.86 (-1.03%)</td><td>5.25 (-8.50%)</td><td>0.75 (+6.01%)</td><td>7.05 (-4.93%)</td><td>6.16 (-2.41%)</td><td>5.86 (-1.03%)</td><td>5.25 (-8.50%)</td><td>0.75 (+6.01%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>7.42 (n/a)</td><td>6.32 (n/a)</td><td>5.93 (n/a)</td><td>5.74 (n/a)</td><td>0.71 (n/a)</td><td>7.42 (n/a)</td><td>6.31 (n/a)</td><td>5.92 (n/a)</td><td>5.74 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>13.45 (+5.58%)</td><td>10.89 (+13.78%)</td><td>12.40 <b>(+27.77%)</b></td><td>6.89 (+0.17%)</td><td>2.80 (+15.75%)</td><td>13.44 (+5.58%)</td><td>10.88 (+13.78%)</td><td>12.39 <b>(+27.77%)</b></td><td>6.88 (+0.17%)</td><td>2.79 (+15.75%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>12.73 (n/a)</td><td>9.57 (n/a)</td><td>9.70 (n/a)</td><td>6.88 (n/a)</td><td>2.42 (n/a)</td><td>12.73 (n/a)</td><td>9.56 (n/a)</td><td>9.70 (n/a)</td><td>6.87 (n/a)</td><td>2.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.20 (n/a)</td><td>398.38 (n/a)</td><td>473.30 (n/a)</td><td>181.90 (n/a)</td><td>150.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.10 (n/a)</td><td>396.14 (n/a)</td><td>382.50 (n/a)</td><td>265.30 (n/a)</td><td>117.32 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.60 (n/a)</td><td>326.52 (n/a)</td><td>280.50 (n/a)</td><td>236.80 (n/a)</td><td>95.46 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>469.80 (n/a)</td><td>353.36 (n/a)</td><td>290.20 (n/a)</td><td>273.80 (n/a)</td><td>101.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1008.80 (n/a)</td><td>497.70 (n/a)</td><td>417.50 (n/a)</td><td>235.70 (n/a)</td><td>297.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>691.80 (n/a)</td><td>517.22 (n/a)</td><td>482.70 (n/a)</td><td>377.90 (n/a)</td><td>120.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2589.90 (n/a)</td><td>821.64 (n/a)</td><td>392.00 (n/a)</td><td>275.10 (n/a)</td><td>994.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.80 (n/a)</td><td>338.72 (n/a)</td><td>283.90 (n/a)</td><td>214.70 (n/a)</td><td>165.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.00 (n/a)</td><td>448.72 (n/a)</td><td>461.80 (n/a)</td><td>228.30 (n/a)</td><td>156.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.90 (n/a)</td><td>387.74 (n/a)</td><td>320.20 (n/a)</td><td>249.40 (n/a)</td><td>147.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.60 (n/a)</td><td>444.18 (n/a)</td><td>508.40 (n/a)</td><td>296.90 (n/a)</td><td>106.77 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1021.30 (n/a)</td><td>585.28 (n/a)</td><td>517.40 (n/a)</td><td>358.30 (n/a)</td><td>259.83 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>312.80 (n/a)</td><td>266.94 (n/a)</td><td>255.60 (n/a)</td><td>208.10 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.00 (n/a)</td><td>390.26 (n/a)</td><td>329.20 (n/a)</td><td>235.90 (n/a)</td><td>172.94 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.00 (n/a)</td><td>370.32 (n/a)</td><td>294.00 (n/a)</td><td>240.10 (n/a)</td><td>151.45 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>458.20 (n/a)</td><td>341.28 (n/a)</td><td>323.60 (n/a)</td><td>265.10 (n/a)</td><td>84.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1010.70 (n/a)</td><td>537.64 (n/a)</td><td>507.00 (n/a)</td><td>300.20 (n/a)</td><td>281.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>516.80 (n/a)</td><td>470.90 (n/a)</td><td>460.70 (n/a)</td><td>416.90 (n/a)</td><td>39.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (-6.19%)</td><td>0.07 <b>(-20.40%)</b></td><td>0.06 <b>(-27.15%)</b></td><td>0.05 (-9.70%)</td><td>0.03 (-15.78%)</td><td>708.60 (+10.74%)</td><td>526.78 <b>(+23.31%)</b></td><td>553.80 <b>(+37.25%)</b></td><td>270.80 (+6.57%)</td><td>183.92 (+4.00%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>639.90 (n/a)</td><td>427.20 (n/a)</td><td>403.50 (n/a)</td><td>254.10 (n/a)</td><td>176.85 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>513.40 (n/a)</td><td>386.78 (n/a)</td><td>382.30 (n/a)</td><td>228.20 (n/a)</td><td>117.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>564.10 (n/a)</td><td>468.96 (n/a)</td><td>540.20 (n/a)</td><td>233.90 (n/a)</td><td>137.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>554.20 (n/a)</td><td>411.38 (n/a)</td><td>514.50 (n/a)</td><td>204.00 (n/a)</td><td>169.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>578.80 (n/a)</td><td>492.60 (n/a)</td><td>470.50 (n/a)</td><td>402.40 (n/a)</td><td>77.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>518.90 (n/a)</td><td>380.82 (n/a)</td><td>317.80 (n/a)</td><td>290.30 (n/a)</td><td>110.43 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.50 (n/a)</td><td>338.02 (n/a)</td><td>297.00 (n/a)</td><td>244.90 (n/a)</td><td>108.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1887.10 (n/a)</td><td>702.20 (n/a)</td><td>505.80 (n/a)</td><td>255.50 (n/a)</td><td>679.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.20 (n/a)</td><td>367.20 (n/a)</td><td>365.90 (n/a)</td><td>240.40 (n/a)</td><td>123.80 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>380.94 (n/a)</td><td>445.40 (n/a)</td><td>147.90 (n/a)</td><td>164.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.70 (n/a)</td><td>398.14 (n/a)</td><td>412.40 (n/a)</td><td>240.00 (n/a)</td><td>148.35 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>692.70 (n/a)</td><td>481.62 (n/a)</td><td>430.40 (n/a)</td><td>324.00 (n/a)</td><td>157.83 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>421.60 (n/a)</td><td>464.90 (n/a)</td><td>265.60 (n/a)</td><td>147.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>837.50 (n/a)</td><td>453.52 (n/a)</td><td>448.70 (n/a)</td><td>225.00 (n/a)</td><td>241.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>416.50 (n/a)</td><td>318.24 (n/a)</td><td>273.70 (n/a)</td><td>244.20 (n/a)</td><td>79.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.80 (n/a)</td><td>298.40 (n/a)</td><td>264.10 (n/a)</td><td>223.30 (n/a)</td><td>115.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.20 (n/a)</td><td>405.64 (n/a)</td><td>473.80 (n/a)</td><td>190.10 (n/a)</td><td>179.40 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.00 (n/a)</td><td>361.30 (n/a)</td><td>299.50 (n/a)</td><td>230.90 (n/a)</td><td>157.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>474.10 (n/a)</td><td>320.86 (n/a)</td><td>270.90 (n/a)</td><td>213.80 (n/a)</td><td>113.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.00 (n/a)</td><td>471.64 (n/a)</td><td>523.50 (n/a)</td><td>175.50 (n/a)</td><td>178.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>563.70 (n/a)</td><td>367.74 (n/a)</td><td>295.80 (n/a)</td><td>245.60 (n/a)</td><td>139.73 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>524.00 (n/a)</td><td>372.38 (n/a)</td><td>415.80 (n/a)</td><td>230.80 (n/a)</td><td>131.67 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>667.80 (n/a)</td><td>416.22 (n/a)</td><td>284.20 (n/a)</td><td>263.40 (n/a)</td><td>196.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>988.30 (n/a)</td><td>484.00 (n/a)</td><td>362.60 (n/a)</td><td>298.80 (n/a)</td><td>286.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.60 (n/a)</td><td>450.90 (n/a)</td><td>470.80 (n/a)</td><td>196.90 (n/a)</td><td>156.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>639.80 (n/a)</td><td>521.38 (n/a)</td><td>582.40 (n/a)</td><td>252.90 (n/a)</td><td>161.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>482.70 (n/a)</td><td>306.96 (n/a)</td><td>241.80 (n/a)</td><td>229.40 (n/a)</td><td>107.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>599.50 (n/a)</td><td>409.98 (n/a)</td><td>350.10 (n/a)</td><td>243.30 (n/a)</td><td>172.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>536.30 (n/a)</td><td>393.50 (n/a)</td><td>422.10 (n/a)</td><td>283.40 (n/a)</td><td>104.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>544.00 (n/a)</td><td>395.52 (n/a)</td><td>393.40 (n/a)</td><td>269.20 (n/a)</td><td>126.46 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>546.80 (n/a)</td><td>384.34 (n/a)</td><td>311.60 (n/a)</td><td>228.90 (n/a)</td><td>150.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (+4.37%)</td><td>0.01 <b>(+20.74%)</b></td><td>0.02 <b>(+61.44%)</b></td><td>0.01 <b>(+28.92%)</b></td><td>0.00 (+13.43%)</td><td>495.00 <b>(-22.44%)</b></td><td>339.88 (-17.07%)</td><td>245.10 <b>(-38.04%)</b></td><td>236.90 (-4.17%)</td><td>136.36 (-13.82%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>638.20 (n/a)</td><td>409.82 (n/a)</td><td>395.60 (n/a)</td><td>247.20 (n/a)</td><td>158.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (-12.85%)</td><td>0.01 (-17.53%)</td><td>0.01 <b>(-42.29%)</b></td><td>0.01 (-2.31%)</td><td>0.00 (-6.53%)</td><td>572.10 (+2.36%)</td><td>441.04 <b>(+21.51%)</b></td><td>521.20 <b>(+73.27%)</b></td><td>274.90 (+14.73%)</td><td>144.41 (+7.46%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.90 (n/a)</td><td>362.96 (n/a)</td><td>300.80 (n/a)</td><td>239.60 (n/a)</td><td>134.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-0.12%)</td><td>0.01 (+9.57%)</td><td>0.01 <b>(+35.28%)</b></td><td>0.01 (+14.74%)</td><td>0.01 (-9.25%)</td><td>442.60 (-12.86%)</td><td>311.10 (-11.60%)</td><td>297.30 <b>(-26.08%)</b></td><td>195.70 (+0.15%)</td><td>107.19 (-18.28%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>507.90 (n/a)</td><td>351.94 (n/a)</td><td>402.20 (n/a)</td><td>195.40 (n/a)</td><td>131.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-11.92%)</td><td>0.01 (+15.21%)</td><td>0.01 <b>(+22.60%)</b></td><td>0.01 <b>(+68.11%)</b></td><td>0.00 <b>(-32.82%)</b></td><td>478.00 <b>(-40.52%)</b></td><td>356.58 <b>(-21.70%)</b></td><td>310.00 (-18.44%)</td><td>268.90 (+13.51%)</td><td>95.26 <b>(-55.36%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>803.60 (n/a)</td><td>455.38 (n/a)</td><td>380.10 (n/a)</td><td>236.90 (n/a)</td><td>213.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 <b>(+23.81%)</b></td><td>0.01 (+3.71%)</td><td>0.01 <b>(-29.82%)</b></td><td>0.01 (+8.13%)</td><td>0.01 <b>(+43.40%)</b></td><td>583.10 (-7.52%)</td><td>402.12 (+2.35%)</td><td>461.60 <b>(+42.47%)</b></td><td>190.80 (-19.26%)</td><td>170.79 (+5.31%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>630.50 (n/a)</td><td>392.88 (n/a)</td><td>324.00 (n/a)</td><td>236.30 (n/a)</td><td>162.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (-19.39%)</td><td>0.01 <b>(-25.88%)</b></td><td>0.01 <b>(-36.84%)</b></td><td>0.01 (-14.67%)</td><td>0.00 <b>(-25.77%)</b></td><td>566.80 (+17.18%)</td><td>442.82 <b>(+33.20%)</b></td><td>462.70 <b>(+58.35%)</b></td><td>291.40 <b>(+24.05%)</b></td><td>127.64 (+13.74%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.70 (n/a)</td><td>332.44 (n/a)</td><td>292.20 (n/a)</td><td>234.90 (n/a)</td><td>112.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 <b>(+59.88%)</b></td><td>0.01 <b>(+20.43%)</b></td><td>0.01 (+5.10%)</td><td>0.01 (-13.07%)</td><td>0.00 <b>(+389.47%)</b></td><td>604.00 (+15.05%)</td><td>427.16 (-8.58%)</td><td>420.20 (-4.85%)</td><td>271.40 <b>(-37.45%)</b></td><td>148.75 <b>(+249.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.00 (n/a)</td><td>467.26 (n/a)</td><td>441.60 (n/a)</td><td>433.90 (n/a)</td><td>42.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (+14.70%)</td><td>0.02 <b>(+45.80%)</b></td><td>0.02 <b>(+70.13%)</b></td><td>0.01 <b>(+126.92%)</b></td><td>0.00 <b>(-59.15%)</b></td><td>284.30 <b>(-55.94%)</b></td><td>256.88 <b>(-39.21%)</b></td><td>254.70 <b>(-41.22%)</b></td><td>215.50 (-12.82%)</td><td>26.90 <b>(-83.74%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.20 (n/a)</td><td>422.60 (n/a)</td><td>433.30 (n/a)</td><td>247.20 (n/a)</td><td>165.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 <b>(+49.72%)</b></td><td>0.02 <b>(+46.72%)</b></td><td>0.02 <b>(+31.52%)</b></td><td>0.01 <b>(+127.80%)</b></td><td>0.00 (+1.88%)</td><td>444.80 <b>(-56.10%)</b></td><td>285.34 <b>(-40.77%)</b></td><td>252.20 <b>(-23.94%)</b></td><td>196.90 <b>(-33.19%)</b></td><td>95.15 <b>(-68.84%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1013.30 (n/a)</td><td>481.74 (n/a)</td><td>331.60 (n/a)</td><td>294.70 (n/a)</td><td>305.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-5.25%)</td><td>0.01 <b>(+30.61%)</b></td><td>0.02 <b>(+88.28%)</b></td><td>0.01 (+10.69%)</td><td>0.00 (+1.85%)</td><td>526.70 (-9.66%)</td><td>357.40 <b>(-22.92%)</b></td><td>266.60 <b>(-46.89%)</b></td><td>249.10 (+5.51%)</td><td>138.38 (+3.70%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.00 (n/a)</td><td>463.68 (n/a)</td><td>502.00 (n/a)</td><td>236.10 (n/a)</td><td>133.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-14.24%)</td><td>0.01 (-3.68%)</td><td>0.01 (-4.20%)</td><td>0.01 <b>(+180.95%)</b></td><td>0.00 <b>(-40.42%)</b></td><td>702.40 <b>(-64.40%)</b></td><td>470.52 <b>(-33.35%)</b></td><td>457.20 (+4.38%)</td><td>259.90 (+16.60%)</td><td>157.16 <b>(-78.21%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1973.30 (n/a)</td><td>705.98 (n/a)</td><td>438.00 (n/a)</td><td>222.90 (n/a)</td><td>721.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (+3.62%)</td><td>0.01 (-12.31%)</td><td>0.01 (-8.56%)</td><td>0.01 (-11.40%)</td><td>0.01 <b>(+27.51%)</b></td><td>609.40 (+12.87%)</td><td>390.74 <b>(+22.05%)</b></td><td>284.80 (+9.37%)</td><td>221.20 (-3.49%)</td><td>178.23 <b>(+40.80%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.90 (n/a)</td><td>320.16 (n/a)</td><td>260.40 (n/a)</td><td>229.20 (n/a)</td><td>126.59 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (-9.50%)</td><td>0.02 (-13.54%)</td><td>0.02 (-9.78%)</td><td>0.01 (+7.21%)</td><td>0.01 <b>(-23.83%)</b></td><td>590.90 (-6.72%)</td><td>464.80 (+9.95%)</td><td>508.40 (+10.86%)</td><td>260.00 (+10.50%)</td><td>143.01 (-15.97%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.50 (n/a)</td><td>422.74 (n/a)</td><td>458.60 (n/a)</td><td>235.30 (n/a)</td><td>170.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (-13.95%)</td><td>0.02 <b>(-29.64%)</b></td><td>0.02 <b>(-43.77%)</b></td><td>0.01 (-19.89%)</td><td>0.01 <b>(-20.43%)</b></td><td>649.00 <b>(+24.83%)</b></td><td>433.12 <b>(+40.82%)</b></td><td>428.90 <b>(+77.82%)</b></td><td>268.20 (+16.20%)</td><td>143.35 (+16.03%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.90 (n/a)</td><td>307.56 (n/a)</td><td>241.20 (n/a)</td><td>230.80 (n/a)</td><td>123.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 <b>(-48.70%)</b></td><td>0.02 <b>(-48.42%)</b></td><td>0.02 <b>(-54.05%)</b></td><td>0.01 <b>(-33.38%)</b></td><td>0.00 <b>(-58.35%)</b></td><td>626.40 <b>(+50.11%)</b></td><td>510.66 <b>(+87.60%)</b></td><td>519.50 <b>(+117.64%)</b></td><td>394.90 <b>(+94.92%)</b></td><td>103.67 (+19.01%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>417.30 (n/a)</td><td>272.20 (n/a)</td><td>238.70 (n/a)</td><td>202.60 (n/a)</td><td>87.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (+14.25%)</td><td>0.03 (+6.45%)</td><td>0.03 (+17.47%)</td><td>0.02 <b>(-31.70%)</b></td><td>0.01 <b>(+252.24%)</b></td><td>461.80 <b>(+46.42%)</b></td><td>286.02 (+0.53%)</td><td>239.10 (-14.85%)</td><td>225.60 (-12.46%)</td><td>100.28 <b>(+357.71%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>315.40 (n/a)</td><td>284.50 (n/a)</td><td>280.80 (n/a)</td><td>257.70 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 <b>(+29.61%)</b></td><td>0.02 <b>(+22.21%)</b></td><td>0.01 (-9.53%)</td><td>0.01 <b>(+305.74%)</b></td><td>0.01 (+3.42%)</td><td>607.20 <b>(-75.36%)</b></td><td>461.68 <b>(-45.40%)</b></td><td>593.20 (+10.55%)</td><td>221.10 <b>(-22.83%)</b></td><td>191.94 <b>(-79.08%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2463.80 (n/a)</td><td>845.54 (n/a)</td><td>536.60 (n/a)</td><td>286.50 (n/a)</td><td>917.45 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (-3.89%)</td><td>0.03 <b>(+25.15%)</b></td><td>0.03 <b>(+76.44%)</b></td><td>0.01 <b>(+41.49%)</b></td><td>0.01 <b>(-22.85%)</b></td><td>590.60 <b>(-29.32%)</b></td><td>332.32 <b>(-28.74%)</b></td><td>275.00 <b>(-43.33%)</b></td><td>230.60 (+4.06%)</td><td>150.37 <b>(-39.36%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>835.60 (n/a)</td><td>466.34 (n/a)</td><td>485.30 (n/a)</td><td>221.60 (n/a)</td><td>247.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 <b>(+34.56%)</b></td><td>0.02 (+1.10%)</td><td>0.02 (-9.86%)</td><td>0.01 <b>(-22.78%)</b></td><td>0.01 <b>(+64.29%)</b></td><td>872.00 <b>(+29.49%)</b></td><td>532.76 (+8.64%)</td><td>528.40 (+10.94%)</td><td>231.90 <b>(-25.67%)</b></td><td>227.57 <b>(+45.41%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.40 (n/a)</td><td>490.38 (n/a)</td><td>476.30 (n/a)</td><td>312.00 (n/a)</td><td>156.50 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 <b>(+62.81%)</b></td><td>0.03 <b>(+74.14%)</b></td><td>0.03 <b>(+73.88%)</b></td><td>0.02 <b>(+324.61%)</b></td><td>0.01 (-9.20%)</td><td>446.10 <b>(-76.45%)</b></td><td>319.90 <b>(-57.28%)</b></td><td>291.20 <b>(-42.48%)</b></td><td>233.80 <b>(-38.57%)</b></td><td>80.82 <b>(-87.46%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1894.20 (n/a)</td><td>748.86 (n/a)</td><td>506.30 (n/a)</td><td>380.60 (n/a)</td><td>644.70 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 <b>(+26.01%)</b></td><td>0.02 (+18.26%)</td><td>0.02 (+3.71%)</td><td>0.01 (+13.96%)</td><td>0.01 <b>(+42.52%)</b></td><td>561.80 (-12.25%)</td><td>426.50 (-13.01%)</td><td>505.20 (-3.59%)</td><td>259.50 <b>(-20.67%)</b></td><td>137.66 (-0.44%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.20 (n/a)</td><td>490.28 (n/a)</td><td>524.00 (n/a)</td><td>327.10 (n/a)</td><td>138.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 <b>(+103.94%)</b></td><td>0.02 <b>(+66.72%)</b></td><td>0.03 <b>(+60.75%)</b></td><td>0.01 <b>(+204.44%)</b></td><td>0.01 <b>(+73.24%)</b></td><td>617.30 <b>(-67.15%)</b></td><td>396.22 <b>(-48.21%)</b></td><td>302.80 <b>(-37.79%)</b></td><td>207.50 <b>(-50.96%)</b></td><td>177.63 <b>(-71.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1879.20 (n/a)</td><td>765.04 (n/a)</td><td>486.70 (n/a)</td><td>423.10 (n/a)</td><td>626.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 <b>(-20.09%)</b></td><td>0.02 (-13.10%)</td><td>0.02 <b>(-20.06%)</b></td><td>0.01 (+0.98%)</td><td>0.01 <b>(-29.91%)</b></td><td>808.30 (-0.97%)</td><td>464.04 (+6.60%)</td><td>439.60 <b>(+25.10%)</b></td><td>251.80 <b>(+25.15%)</b></td><td>207.82 (-12.59%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>816.20 (n/a)</td><td>435.30 (n/a)</td><td>351.40 (n/a)</td><td>201.20 (n/a)</td><td>237.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (+16.37%)</td><td>0.03 <b>(+50.29%)</b></td><td>0.03 <b>(+83.34%)</b></td><td>0.02 (+11.92%)</td><td>0.01 (+16.95%)</td><td>545.30 (-10.65%)</td><td>338.38 <b>(-32.82%)</b></td><td>297.40 <b>(-45.45%)</b></td><td>259.80 (-14.06%)</td><td>117.68 (-0.56%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.30 (n/a)</td><td>503.70 (n/a)</td><td>545.20 (n/a)</td><td>302.30 (n/a)</td><td>118.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 <b>(+26.37%)</b></td><td>0.06 <b>(+25.27%)</b></td><td>0.06 <b>(+31.83%)</b></td><td>0.04 (+5.97%)</td><td>0.01 <b>(+39.23%)</b></td><td>420.20 (-5.64%)</td><td>301.24 (-19.15%)</td><td>283.80 <b>(-24.14%)</b></td><td>235.40 <b>(-20.87%)</b></td><td>74.44 (+3.83%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>445.30 (n/a)</td><td>372.58 (n/a)</td><td>374.10 (n/a)</td><td>297.50 (n/a)</td><td>71.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (+0.20%)</td><td>0.06 (+15.52%)</td><td>0.05 (-2.68%)</td><td>0.05 <b>(+72.19%)</b></td><td>0.01 <b>(-54.46%)</b></td><td>352.60 <b>(-41.92%)</b></td><td>299.32 <b>(-20.76%)</b></td><td>305.90 (+2.75%)</td><td>252.40 (-0.20%)</td><td>37.80 <b>(-74.06%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>607.10 (n/a)</td><td>377.76 (n/a)</td><td>297.70 (n/a)</td><td>252.90 (n/a)</td><td>145.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 <b>(+31.08%)</b></td><td>0.04 <b>(+22.52%)</b></td><td>0.04 (+17.55%)</td><td>0.03 (-13.42%)</td><td>0.02 <b>(+88.80%)</b></td><td>640.50 (+15.51%)</td><td>407.20 (-12.51%)</td><td>393.80 (-14.93%)</td><td>249.90 <b>(-23.72%)</b></td><td>152.34 <b>(+64.95%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.50 (n/a)</td><td>465.40 (n/a)</td><td>462.90 (n/a)</td><td>327.60 (n/a)</td><td>92.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (-1.92%)</td><td>0.04 (-6.24%)</td><td>0.04 (+3.00%)</td><td>0.03 (-7.90%)</td><td>0.01 (-10.40%)</td><td>596.40 (+8.57%)</td><td>442.12 (+4.91%)</td><td>452.40 (-2.92%)</td><td>261.30 (+1.95%)</td><td>119.95 (-7.60%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.30 (n/a)</td><td>421.42 (n/a)</td><td>466.00 (n/a)</td><td>256.30 (n/a)</td><td>129.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (-9.51%)</td><td>0.03 <b>(-21.96%)</b></td><td>0.03 (-6.48%)</td><td>0.01 <b>(-69.34%)</b></td><td>0.02 (+16.46%)</td><td>1930.10 <b>(+226.14%)</b></td><td>741.16 <b>(+73.46%)</b></td><td>511.00 (+6.93%)</td><td>319.10 (+10.49%)</td><td>670.28 <b>(+408.05%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.80 (n/a)</td><td>427.28 (n/a)</td><td>477.90 (n/a)</td><td>288.80 (n/a)</td><td>131.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 <b>(+57.19%)</b></td><td>0.05 <b>(+22.46%)</b></td><td>0.04 (-4.94%)</td><td>0.01 <b>(-64.19%)</b></td><td>0.03 <b>(+201.16%)</b></td><td>1937.20 <b>(+179.26%)</b></td><td>675.96 <b>(+43.67%)</b></td><td>460.20 (+5.21%)</td><td>201.40 <b>(-36.37%)</b></td><td>720.99 <b>(+418.28%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>693.70 (n/a)</td><td>470.48 (n/a)</td><td>437.40 (n/a)</td><td>316.50 (n/a)</td><td>139.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 <b>(+43.02%)</b></td><td>0.04 <b>(+20.07%)</b></td><td>0.04 (+13.45%)</td><td>0.03 (+10.35%)</td><td>0.01 <b>(+93.07%)</b></td><td>575.30 (-9.39%)</td><td>435.34 (-13.08%)</td><td>426.40 (-11.86%)</td><td>257.10 <b>(-30.08%)</b></td><td>122.53 (+19.68%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>634.90 (n/a)</td><td>500.88 (n/a)</td><td>483.80 (n/a)</td><td>367.70 (n/a)</td><td>102.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (-12.16%)</td><td>0.03 <b>(-39.78%)</b></td><td>0.03 <b>(-25.45%)</b></td><td>0.01 <b>(-75.36%)</b></td><td>0.03 (+12.26%)</td><td>2484.60 <b>(+305.85%)</b></td><td>1152.58 <b>(+185.25%)</b></td><td>548.70 <b>(+34.16%)</b></td><td>237.10 (+13.83%)</td><td>1001.43 <b>(+476.14%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>612.20 (n/a)</td><td>404.06 (n/a)</td><td>409.00 (n/a)</td><td>208.30 (n/a)</td><td>173.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (-7.28%)</td><td>0.04 (+10.63%)</td><td>0.04 (-2.75%)</td><td>0.03 <b>(+247.68%)</b></td><td>0.01 <b>(-67.20%)</b></td><td>538.90 <b>(-71.24%)</b></td><td>459.86 <b>(-37.87%)</b></td><td>468.00 (+2.83%)</td><td>367.70 (+7.86%)</td><td>65.12 <b>(-89.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1873.70 (n/a)</td><td>740.14 (n/a)</td><td>455.10 (n/a)</td><td>340.90 (n/a)</td><td>648.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (-0.58%)</td><td>0.05 (+6.63%)</td><td>0.05 <b>(+34.74%)</b></td><td>0.03 <b>(+22.57%)</b></td><td>0.01 <b>(-21.36%)</b></td><td>498.60 (-18.42%)</td><td>355.78 (-11.40%)</td><td>309.60 <b>(-25.79%)</b></td><td>234.70 (+0.60%)</td><td>107.29 <b>(-31.22%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.20 (n/a)</td><td>401.54 (n/a)</td><td>417.20 (n/a)</td><td>233.30 (n/a)</td><td>155.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (+6.64%)</td><td>0.04 (+6.11%)</td><td>0.03 (-4.42%)</td><td>0.03 <b>(+36.74%)</b></td><td>0.02 (+5.81%)</td><td>621.70 <b>(-26.86%)</b></td><td>482.64 (-7.65%)</td><td>554.40 (+4.62%)</td><td>230.30 (-6.23%)</td><td>167.63 <b>(-23.36%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>850.00 (n/a)</td><td>522.64 (n/a)</td><td>529.90 (n/a)</td><td>245.60 (n/a)</td><td>218.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (+6.81%)</td><td>0.04 (+5.37%)</td><td>0.04 (-12.91%)</td><td>0.03 (+15.00%)</td><td>0.01 (+1.43%)</td><td>595.80 (-13.03%)</td><td>415.56 (-7.08%)</td><td>434.90 (+14.81%)</td><td>276.80 (-6.39%)</td><td>136.07 <b>(-20.93%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>685.10 (n/a)</td><td>447.22 (n/a)</td><td>378.80 (n/a)</td><td>295.70 (n/a)</td><td>172.10 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.17 <b>(+21.40%)</b></td><td>0.09 (-14.59%)</td><td>0.06 <b>(-45.19%)</b></td><td>0.02 <b>(-73.13%)</b></td><td>0.06 <b>(+100.15%)</b></td><td>1972.60 <b>(+272.12%)</b></td><td>715.06 <b>(+103.19%)</b></td><td>565.20 <b>(+82.44%)</b></td><td>188.90 (-17.62%)</td><td>726.32 <b>(+505.55%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>530.10 (n/a)</td><td>351.92 (n/a)</td><td>309.80 (n/a)</td><td>229.30 (n/a)</td><td>119.94 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 <b>(+29.06%)</b></td><td>0.13 <b>(+56.75%)</b></td><td>0.13 <b>(+82.05%)</b></td><td>0.11 <b>(+92.14%)</b></td><td>0.02 <b>(-25.94%)</b></td><td>303.60 <b>(-47.96%)</b></td><td>254.68 <b>(-39.94%)</b></td><td>256.20 <b>(-45.07%)</b></td><td>209.00 <b>(-22.51%)</b></td><td>38.61 <b>(-69.58%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>583.40 (n/a)</td><td>424.04 (n/a)</td><td>466.40 (n/a)</td><td>269.70 (n/a)</td><td>126.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 <b>(+45.86%)</b></td><td>0.12 <b>(+59.13%)</b></td><td>0.14 <b>(+90.87%)</b></td><td>0.06 (+15.10%)</td><td>0.04 <b>(+50.23%)</b></td><td>513.90 (-13.12%)</td><td>291.48 <b>(-35.27%)</b></td><td>238.70 <b>(-47.61%)</b></td><td>206.90 <b>(-31.44%)</b></td><td>125.93 (-4.80%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>591.50 (n/a)</td><td>450.32 (n/a)</td><td>455.60 (n/a)</td><td>301.80 (n/a)</td><td>132.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (+18.67%)</td><td>0.13 <b>(+43.49%)</b></td><td>0.11 <b>(+33.68%)</b></td><td>0.11 <b>(+99.57%)</b></td><td>0.02 <b>(-25.26%)</b></td><td>300.70 <b>(-49.88%)</b></td><td>263.90 <b>(-34.15%)</b></td><td>285.60 <b>(-25.22%)</b></td><td>218.20 (-15.72%)</td><td>39.08 <b>(-69.17%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>600.00 (n/a)</td><td>400.74 (n/a)</td><td>381.90 (n/a)</td><td>258.90 (n/a)</td><td>126.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 <b>(+73.31%)</b></td><td>0.11 <b>(+83.85%)</b></td><td>0.12 <b>(+112.32%)</b></td><td>0.05 (+2.16%)</td><td>0.03 <b>(+216.37%)</b></td><td>605.40 (-2.12%)</td><td>325.18 <b>(-39.75%)</b></td><td>263.60 <b>(-52.90%)</b></td><td>235.40 <b>(-42.30%)</b></td><td>157.79 <b>(+88.07%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>618.50 (n/a)</td><td>539.68 (n/a)</td><td>559.70 (n/a)</td><td>408.00 (n/a)</td><td>83.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (-0.99%)</td><td>0.11 (+8.74%)</td><td>0.12 (+3.75%)</td><td>0.06 (-2.18%)</td><td>0.03 (-12.93%)</td><td>558.30 (+2.23%)</td><td>322.10 (-9.99%)</td><td>276.00 (-3.63%)</td><td>237.60 (+1.02%)</td><td>134.17 (-6.31%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>546.10 (n/a)</td><td>357.84 (n/a)</td><td>286.40 (n/a)</td><td>235.20 (n/a)</td><td>143.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+0.54%)</td><td>0.10 <b>(+38.07%)</b></td><td>0.11 <b>(+73.14%)</b></td><td>0.07 <b>(+51.35%)</b></td><td>0.03 (-14.16%)</td><td>440.40 <b>(-33.93%)</b></td><td>332.68 <b>(-31.04%)</b></td><td>300.30 <b>(-42.24%)</b></td><td>250.70 (-0.56%)</td><td>91.57 <b>(-40.16%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>666.60 (n/a)</td><td>482.44 (n/a)</td><td>519.90 (n/a)</td><td>252.10 (n/a)</td><td>153.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 <b>(+68.90%)</b></td><td>0.08 (+5.94%)</td><td>0.07 (-8.14%)</td><td>0.01 <b>(-81.52%)</b></td><td>0.05 <b>(+1230.46%)</b></td><td>2494.60 <b>(+441.25%)</b></td><td>810.22 <b>(+88.76%)</b></td><td>456.50 (+8.85%)</td><td>239.30 <b>(-40.80%)</b></td><td>953.89 <b>(+4162.94%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>460.90 (n/a)</td><td>429.24 (n/a)</td><td>419.40 (n/a)</td><td>404.20 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (+19.74%)</td><td>0.09 (-9.29%)</td><td>0.06 <b>(-46.35%)</b></td><td>0.05 <b>(-26.29%)</b></td><td>0.05 <b>(+64.49%)</b></td><td>663.90 <b>(+35.66%)</b></td><td>437.64 <b>(+26.36%)</b></td><td>511.30 <b>(+86.40%)</b></td><td>203.40 (-16.47%)</td><td>202.34 <b>(+76.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>489.40 (n/a)</td><td>346.34 (n/a)</td><td>274.30 (n/a)</td><td>243.50 (n/a)</td><td>114.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (+3.25%)</td><td>0.07 <b>(-25.09%)</b></td><td>0.07 <b>(-32.40%)</b></td><td>0.02 <b>(-68.28%)</b></td><td>0.04 <b>(+38.64%)</b></td><td>1879.00 <b>(+215.22%)</b></td><td>727.38 <b>(+85.09%)</b></td><td>501.80 <b>(+47.94%)</b></td><td>271.30 (-3.14%)</td><td>652.89 <b>(+386.79%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>596.10 (n/a)</td><td>392.98 (n/a)</td><td>339.20 (n/a)</td><td>280.10 (n/a)</td><td>134.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 <b>(-26.85%)</b></td><td>0.07 <b>(-20.90%)</b></td><td>0.06 (-13.63%)</td><td>0.05 (+17.43%)</td><td>0.02 <b>(-46.45%)</b></td><td>616.60 (-14.85%)</td><td>484.40 (+14.28%)</td><td>507.30 (+15.77%)</td><td>307.50 <b>(+36.73%)</b></td><td>116.08 <b>(-39.56%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>724.10 (n/a)</td><td>423.86 (n/a)</td><td>438.20 (n/a)</td><td>224.90 (n/a)</td><td>192.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+1.09%)</td><td>0.10 <b>(+24.15%)</b></td><td>0.11 <b>(+35.95%)</b></td><td>0.06 (+13.39%)</td><td>0.03 (-7.98%)</td><td>553.20 (-11.81%)</td><td>344.34 <b>(-20.93%)</b></td><td>291.40 <b>(-26.43%)</b></td><td>261.40 (-1.06%)</td><td>119.24 (-16.54%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>627.30 (n/a)</td><td>435.48 (n/a)</td><td>396.10 (n/a)</td><td>264.20 (n/a)</td><td>142.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-8.17%)</td><td>0.01 (+5.05%)</td><td>0.01 (+15.94%)</td><td>0.01 (+4.43%)</td><td>0.00 (-3.02%)</td><td>648.60 (-4.24%)</td><td>416.26 (-5.45%)</td><td>379.80 (-13.74%)</td><td>246.80 (+8.91%)</td><td>181.55 (-2.96%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.30 (n/a)</td><td>440.26 (n/a)</td><td>440.30 (n/a)</td><td>226.60 (n/a)</td><td>187.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (+19.70%)</td><td>0.02 (+2.84%)</td><td>0.01 (+6.86%)</td><td>0.01 (+2.13%)</td><td>0.00 <b>(+23.79%)</b></td><td>534.20 (-2.09%)</td><td>421.84 (-1.71%)</td><td>440.00 (-6.42%)</td><td>255.10 (-16.47%)</td><td>105.16 (-1.19%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.60 (n/a)</td><td>429.20 (n/a)</td><td>470.20 (n/a)</td><td>305.40 (n/a)</td><td>106.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (-13.70%)</td><td>0.01 (-19.59%)</td><td>0.01 (-15.29%)</td><td>0.01 (-7.70%)</td><td>0.00 <b>(-32.73%)</b></td><td>555.90 (+8.34%)</td><td>443.50 (+19.42%)</td><td>476.50 (+18.03%)</td><td>278.70 (+15.84%)</td><td>104.24 (-14.74%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.10 (n/a)</td><td>371.38 (n/a)</td><td>403.70 (n/a)</td><td>240.60 (n/a)</td><td>122.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (+15.72%)</td><td>0.01 (-14.44%)</td><td>0.01 <b>(-39.54%)</b></td><td>0.01 (+6.52%)</td><td>0.01 (+15.28%)</td><td>566.30 (-6.13%)</td><td>447.62 (+16.64%)</td><td>494.30 <b>(+65.37%)</b></td><td>202.00 (-13.56%)</td><td>142.39 (-14.75%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.30 (n/a)</td><td>383.76 (n/a)</td><td>298.90 (n/a)</td><td>233.70 (n/a)</td><td>167.03 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-11.97%)</td><td>0.01 (-12.21%)</td><td>0.02 (-9.70%)</td><td>0.01 <b>(-36.39%)</b></td><td>0.00 <b>(+44.98%)</b></td><td>493.60 <b>(+57.20%)</b></td><td>310.14 (+19.71%)</td><td>270.50 (+10.77%)</td><td>241.00 (+13.57%)</td><td>104.57 <b>(+166.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>314.00 (n/a)</td><td>259.08 (n/a)</td><td>244.20 (n/a)</td><td>212.20 (n/a)</td><td>39.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-2.66%)</td><td>0.01 <b>(+25.87%)</b></td><td>0.01 <b>(+20.34%)</b></td><td>0.01 <b>(+207.59%)</b></td><td>0.00 <b>(-28.66%)</b></td><td>675.10 <b>(-67.49%)</b></td><td>466.06 <b>(-42.36%)</b></td><td>462.60 (-16.90%)</td><td>305.80 (+2.72%)</td><td>148.05 <b>(-79.37%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2076.50 (n/a)</td><td>808.60 (n/a)</td><td>556.70 (n/a)</td><td>297.70 (n/a)</td><td>717.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 <b>(-43.51%)</b></td><td>0.01 <b>(-23.69%)</b></td><td>0.01 <b>(-21.78%)</b></td><td>0.01 <b>(+258.95%)</b></td><td>0.00 <b>(-78.31%)</b></td><td>585.20 <b>(-72.14%)</b></td><td>518.02 <b>(-26.36%)</b></td><td>566.90 <b>(+27.82%)</b></td><td>414.90 <b>(+77.01%)</b></td><td>80.59 <b>(-89.78%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2100.50 (n/a)</td><td>703.48 (n/a)</td><td>443.50 (n/a)</td><td>234.40 (n/a)</td><td>788.31 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-4.35%)</td><td>0.01 (-1.16%)</td><td>0.01 (+13.03%)</td><td>0.01 (-8.63%)</td><td>0.00 (-15.88%)</td><td>591.00 (+9.44%)</td><td>425.66 (-1.43%)</td><td>464.20 (-11.55%)</td><td>263.20 (+4.53%)</td><td>125.66 (-10.22%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.00 (n/a)</td><td>431.82 (n/a)</td><td>524.80 (n/a)</td><td>251.80 (n/a)</td><td>139.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (-2.81%)</td><td>0.01 (-18.80%)</td><td>0.01 <b>(-43.20%)</b></td><td>0.01 (+1.57%)</td><td>0.00 <b>(-27.97%)</b></td><td>470.10 (-1.55%)</td><td>392.92 (+17.09%)</td><td>434.10 <b>(+76.11%)</b></td><td>247.40 (+2.91%)</td><td>89.39 <b>(-29.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.50 (n/a)</td><td>335.58 (n/a)</td><td>246.50 (n/a)</td><td>240.40 (n/a)</td><td>126.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 <b>(+51.83%)</b></td><td>0.01 (+13.85%)</td><td>0.01 (+14.75%)</td><td>0.01 (-4.97%)</td><td>0.00 <b>(+117.81%)</b></td><td>614.40 (+5.24%)</td><td>446.52 (-6.32%)</td><td>434.00 (-12.87%)</td><td>241.80 <b>(-34.13%)</b></td><td>136.69 <b>(+44.64%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.80 (n/a)</td><td>476.66 (n/a)</td><td>498.10 (n/a)</td><td>367.10 (n/a)</td><td>94.50 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 <b>(-21.01%)</b></td><td>0.01 (-8.94%)</td><td>0.01 <b>(+20.07%)</b></td><td>0.01 (+1.03%)</td><td>0.00 <b>(-52.38%)</b></td><td>570.20 (-1.02%)</td><td>432.38 (-0.22%)</td><td>412.90 (-16.72%)</td><td>309.90 <b>(+26.59%)</b></td><td>93.99 <b>(-41.73%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.10 (n/a)</td><td>433.34 (n/a)</td><td>495.80 (n/a)</td><td>244.80 (n/a)</td><td>161.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (-7.68%)</td><td>0.03 <b>(+33.59%)</b></td><td>0.03 <b>(+77.00%)</b></td><td>0.01 (+0.43%)</td><td>0.01 (-14.52%)</td><td>578.80 (-0.43%)</td><td>320.02 <b>(-26.77%)</b></td><td>249.20 <b>(-43.50%)</b></td><td>230.10 (+8.28%)</td><td>146.75 (-5.42%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>436.98 (n/a)</td><td>441.10 (n/a)</td><td>212.50 (n/a)</td><td>155.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (+4.30%)</td><td>0.04 (-9.42%)</td><td>0.04 (-1.00%)</td><td>0.02 (-8.61%)</td><td>0.01 (+11.96%)</td><td>595.10 (+9.41%)</td><td>370.94 (+13.19%)</td><td>293.90 (+1.00%)</td><td>234.40 (-4.13%)</td><td>146.70 (+17.92%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.90 (n/a)</td><td>327.72 (n/a)</td><td>291.00 (n/a)</td><td>244.50 (n/a)</td><td>124.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (+4.76%)</td><td>0.03 <b>(+34.74%)</b></td><td>0.03 <b>(+77.18%)</b></td><td>0.01 <b>(-45.32%)</b></td><td>0.01 <b>(+44.21%)</b></td><td>1123.40 <b>(+82.87%)</b></td><td>437.20 (-5.04%)</td><td>264.90 <b>(-43.55%)</b></td><td>240.90 (-4.56%)</td><td>384.14 <b>(+185.63%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.30 (n/a)</td><td>460.42 (n/a)</td><td>469.30 (n/a)</td><td>252.40 (n/a)</td><td>134.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (+10.37%)</td><td>0.03 (-18.93%)</td><td>0.02 <b>(-46.44%)</b></td><td>0.01 (+1.08%)</td><td>0.02 (+3.18%)</td><td>1983.50 (-1.07%)</td><td>705.16 (+13.83%)</td><td>456.30 <b>(+86.70%)</b></td><td>209.30 (-9.39%)</td><td>730.57 (-5.93%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2004.90 (n/a)</td><td>619.50 (n/a)</td><td>244.40 (n/a)</td><td>231.00 (n/a)</td><td>776.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (+0.50%)</td><td>0.02 (-0.45%)</td><td>0.02 (-0.87%)</td><td>0.01 (-17.59%)</td><td>0.01 <b>(+23.69%)</b></td><td>587.50 <b>(+21.36%)</b></td><td>378.42 (+5.42%)</td><td>363.70 (+0.89%)</td><td>239.50 (-0.50%)</td><td>146.72 <b>(+42.07%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.10 (n/a)</td><td>358.96 (n/a)</td><td>360.50 (n/a)</td><td>240.70 (n/a)</td><td>103.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (+0.09%)</td><td>0.03 (-8.76%)</td><td>0.03 <b>(-22.63%)</b></td><td>0.02 (-19.10%)</td><td>0.01 <b>(+38.54%)</b></td><td>679.70 <b>(+23.60%)</b></td><td>395.76 (+19.73%)</td><td>393.60 <b>(+29.26%)</b></td><td>221.80 (-0.09%)</td><td>190.21 <b>(+48.09%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>549.90 (n/a)</td><td>330.54 (n/a)</td><td>304.50 (n/a)</td><td>222.00 (n/a)</td><td>128.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (-11.91%)</td><td>0.02 (-6.50%)</td><td>0.02 (-0.14%)</td><td>0.01 (-6.56%)</td><td>0.01 (-12.32%)</td><td>640.00 (+7.02%)</td><td>427.68 (+6.09%)</td><td>356.70 (+0.14%)</td><td>234.90 (+13.48%)</td><td>188.90 (+6.89%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.00 (n/a)</td><td>403.12 (n/a)</td><td>356.20 (n/a)</td><td>207.00 (n/a)</td><td>176.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (+2.87%)</td><td>0.03 (+10.56%)</td><td>0.03 (+19.62%)</td><td>0.02 <b>(+29.08%)</b></td><td>0.01 <b>(-25.26%)</b></td><td>468.70 <b>(-22.52%)</b></td><td>360.14 (-15.78%)</td><td>354.30 (-16.40%)</td><td>239.00 (-2.77%)</td><td>86.35 <b>(-45.81%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>604.90 (n/a)</td><td>427.60 (n/a)</td><td>423.80 (n/a)</td><td>245.80 (n/a)</td><td>159.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (-7.25%)</td><td>0.03 <b>(+31.06%)</b></td><td>0.03 <b>(+64.28%)</b></td><td>0.02 <b>(+23.77%)</b></td><td>0.01 <b>(-23.74%)</b></td><td>465.70 (-19.21%)</td><td>320.18 <b>(-27.90%)</b></td><td>289.80 <b>(-39.12%)</b></td><td>227.00 (+7.84%)</td><td>99.37 <b>(-29.38%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.40 (n/a)</td><td>444.06 (n/a)</td><td>476.00 (n/a)</td><td>210.50 (n/a)</td><td>140.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (+12.41%)</td><td>0.03 (-8.37%)</td><td>0.02 <b>(-35.79%)</b></td><td>0.02 (-8.29%)</td><td>0.01 <b>(+58.21%)</b></td><td>518.00 (+9.05%)</td><td>398.88 (+17.80%)</td><td>471.40 <b>(+55.73%)</b></td><td>217.30 (-11.05%)</td><td>143.79 <b>(+57.60%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.00 (n/a)</td><td>338.60 (n/a)</td><td>302.70 (n/a)</td><td>244.30 (n/a)</td><td>91.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 <b>(+50.33%)</b></td><td>0.02 <b>(+44.48%)</b></td><td>0.03 <b>(+53.04%)</b></td><td>0.02 <b>(+21.85%)</b></td><td>0.01 <b>(+100.46%)</b></td><td>529.40 (-17.94%)</td><td>381.32 <b>(-27.87%)</b></td><td>322.80 <b>(-34.64%)</b></td><td>259.50 <b>(-33.48%)</b></td><td>120.45 (+9.60%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.10 (n/a)</td><td>528.62 (n/a)</td><td>493.90 (n/a)</td><td>390.10 (n/a)</td><td>109.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (+11.38%)</td><td>0.06 <b>(+23.04%)</b></td><td>0.06 <b>(+32.10%)</b></td><td>0.03 (+7.48%)</td><td>0.01 (+8.84%)</td><td>509.90 (-6.95%)</td><td>315.84 (-18.81%)</td><td>255.30 <b>(-24.29%)</b></td><td>246.80 (-10.22%)</td><td>111.88 (-9.13%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>548.00 (n/a)</td><td>389.00 (n/a)</td><td>337.20 (n/a)</td><td>274.90 (n/a)</td><td>123.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (-2.68%)</td><td>0.06 <b>(-36.81%)</b></td><td>0.05 <b>(-46.25%)</b></td><td>0.04 <b>(-50.11%)</b></td><td>0.03 <b>(+164.94%)</b></td><td>628.30 <b>(+100.48%)</b></td><td>490.24 <b>(+76.28%)</b></td><td>513.40 <b>(+86.01%)</b></td><td>247.00 (+2.75%)</td><td>156.68 <b>(+439.21%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>313.40 (n/a)</td><td>278.10 (n/a)</td><td>276.00 (n/a)</td><td>240.40 (n/a)</td><td>29.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (+12.84%)</td><td>0.05 (+2.20%)</td><td>0.07 <b>(+22.16%)</b></td><td>0.02 (-12.95%)</td><td>0.02 <b>(+74.41%)</b></td><td>670.40 (+14.87%)</td><td>390.84 (+10.29%)</td><td>251.90 (-18.13%)</td><td>241.70 (-11.37%)</td><td>203.79 <b>(+58.02%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>583.60 (n/a)</td><td>354.38 (n/a)</td><td>307.70 (n/a)</td><td>272.70 (n/a)</td><td>128.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 <b>(-28.44%)</b></td><td>0.05 <b>(-35.12%)</b></td><td>0.05 <b>(-41.34%)</b></td><td>0.03 (-13.58%)</td><td>0.01 <b>(-37.72%)</b></td><td>631.90 (+15.71%)</td><td>453.96 <b>(+46.88%)</b></td><td>438.60 <b>(+70.46%)</b></td><td>284.90 <b>(+39.73%)</b></td><td>123.88 (-9.11%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.10 (n/a)</td><td>309.06 (n/a)</td><td>257.30 (n/a)</td><td>203.90 (n/a)</td><td>136.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (-3.16%)</td><td>0.05 (+7.00%)</td><td>0.06 (+6.38%)</td><td>0.03 (+17.33%)</td><td>0.02 (-3.16%)</td><td>505.20 (-14.78%)</td><td>353.92 (-8.53%)</td><td>281.10 (-5.99%)</td><td>242.80 (+3.23%)</td><td>132.78 (-16.22%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.80 (n/a)</td><td>386.92 (n/a)</td><td>299.00 (n/a)</td><td>235.20 (n/a)</td><td>158.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (+4.43%)</td><td>0.05 (-15.77%)</td><td>0.04 <b>(-26.35%)</b></td><td>0.04 (+6.75%)</td><td>0.02 (-9.88%)</td><td>563.00 (-6.32%)</td><td>453.68 (+14.67%)</td><td>491.70 <b>(+35.75%)</b></td><td>234.90 (-4.24%)</td><td>130.37 (-19.35%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>601.00 (n/a)</td><td>395.64 (n/a)</td><td>362.20 (n/a)</td><td>245.30 (n/a)</td><td>161.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (-15.81%)</td><td>0.05 (-18.10%)</td><td>0.03 <b>(-43.21%)</b></td><td>0.03 (-6.46%)</td><td>0.02 (-15.91%)</td><td>554.40 (+6.90%)</td><td>413.84 (+19.64%)</td><td>468.70 <b>(+76.07%)</b></td><td>228.10 (+18.74%)</td><td>151.18 (+0.55%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>518.60 (n/a)</td><td>345.90 (n/a)</td><td>266.20 (n/a)</td><td>192.10 (n/a)</td><td>150.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (-13.98%)</td><td>0.05 (-13.18%)</td><td>0.05 (-17.06%)</td><td>0.03 <b>(-22.07%)</b></td><td>0.02 (-12.20%)</td><td>597.20 <b>(+28.32%)</b></td><td>378.72 (+16.28%)</td><td>350.40 <b>(+20.58%)</b></td><td>267.00 (+16.24%)</td><td>133.08 <b>(+31.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>465.40 (n/a)</td><td>325.70 (n/a)</td><td>290.60 (n/a)</td><td>229.70 (n/a)</td><td>101.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (+3.81%)</td><td>0.04 (-6.69%)</td><td>0.04 <b>(+30.26%)</b></td><td>0.02 <b>(-43.15%)</b></td><td>0.02 (+1.47%)</td><td>1053.10 <b>(+75.87%)</b></td><td>529.68 (+14.92%)</td><td>456.40 <b>(-23.23%)</b></td><td>226.50 (-3.66%)</td><td>310.58 <b>(+67.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.80 (n/a)</td><td>460.92 (n/a)</td><td>594.50 (n/a)</td><td>235.10 (n/a)</td><td>185.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (-16.56%)</td><td>0.04 <b>(-26.46%)</b></td><td>0.04 <b>(-42.49%)</b></td><td>0.03 (+12.45%)</td><td>0.01 <b>(-42.29%)</b></td><td>563.30 (-11.07%)</td><td>462.72 <b>(+23.80%)</b></td><td>469.80 <b>(+73.87%)</b></td><td>288.90 (+19.83%)</td><td>106.15 <b>(-38.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>633.40 (n/a)</td><td>373.76 (n/a)</td><td>270.20 (n/a)</td><td>241.10 (n/a)</td><td>173.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (+2.70%)</td><td>0.05 (+5.02%)</td><td>0.04 (-13.01%)</td><td>0.03 (+18.15%)</td><td>0.02 (+1.50%)</td><td>497.60 (-15.37%)</td><td>395.58 (-5.83%)</td><td>442.20 (+14.95%)</td><td>241.20 (-2.62%)</td><td>116.40 (-15.50%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.00 (n/a)</td><td>420.08 (n/a)</td><td>384.70 (n/a)</td><td>247.70 (n/a)</td><td>137.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+7.45%)</td><td>0.07 <b>(-21.30%)</b></td><td>0.07 <b>(-39.35%)</b></td><td>0.04 <b>(-20.72%)</b></td><td>0.03 (-4.34%)</td><td>772.40 <b>(+26.15%)</b></td><td>506.62 <b>(+26.71%)</b></td><td>460.60 <b>(+64.85%)</b></td><td>247.60 (-6.92%)</td><td>194.59 (+9.70%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>612.30 (n/a)</td><td>399.82 (n/a)</td><td>279.40 (n/a)</td><td>266.00 (n/a)</td><td>177.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (-8.76%)</td><td>0.09 (+10.94%)</td><td>0.11 (+3.09%)</td><td>0.06 <b>(+297.65%)</b></td><td>0.02 <b>(-53.06%)</b></td><td>516.60 <b>(-74.85%)</b></td><td>368.36 <b>(-47.72%)</b></td><td>305.60 (-3.01%)</td><td>282.90 (+9.61%)</td><td>101.98 <b>(-86.76%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2054.10 (n/a)</td><td>704.56 (n/a)</td><td>315.10 (n/a)</td><td>258.10 (n/a)</td><td>770.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (-5.36%)</td><td>0.09 <b>(-30.32%)</b></td><td>0.09 <b>(-34.65%)</b></td><td>0.02 <b>(-73.50%)</b></td><td>0.05 <b>(+26.73%)</b></td><td>2124.60 <b>(+277.30%)</b></td><td>742.74 <b>(+115.99%)</b></td><td>438.40 <b>(+53.02%)</b></td><td>257.10 (+5.67%)</td><td>776.91 <b>(+488.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>563.10 (n/a)</td><td>343.88 (n/a)</td><td>286.50 (n/a)</td><td>243.30 (n/a)</td><td>131.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (-12.12%)</td><td>0.05 <b>(-55.09%)</b></td><td>0.02 <b>(-77.72%)</b></td><td>0.02 <b>(-75.29%)</b></td><td>0.04 <b>(+52.26%)</b></td><td>1915.80 <b>(+304.69%)</b></td><td>1193.40 <b>(+261.46%)</b></td><td>1363.80 <b>(+348.77%)</b></td><td>275.30 (+13.81%)</td><td>753.63 <b>(+669.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>473.40 (n/a)</td><td>330.16 (n/a)</td><td>303.90 (n/a)</td><td>241.90 (n/a)</td><td>97.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (-4.10%)</td><td>0.12 (-12.95%)</td><td>0.13 (-4.95%)</td><td>0.07 (-1.87%)</td><td>0.04 (+13.61%)</td><td>548.90 (+1.91%)</td><td>385.52 (+18.28%)</td><td>303.60 (+5.20%)</td><td>258.20 (+4.28%)</td><td>146.33 <b>(+21.18%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>538.60 (n/a)</td><td>325.94 (n/a)</td><td>288.60 (n/a)</td><td>247.60 (n/a)</td><td>120.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (-12.08%)</td><td>0.08 (-16.77%)</td><td>0.07 (+7.82%)</td><td>0.02 <b>(-65.65%)</b></td><td>0.04 (-8.79%)</td><td>1837.00 <b>(+191.17%)</b></td><td>683.64 <b>(+57.11%)</b></td><td>494.10 (-7.26%)</td><td>265.60 (+13.70%)</td><td>654.03 <b>(+248.66%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>630.90 (n/a)</td><td>435.14 (n/a)</td><td>532.80 (n/a)</td><td>233.60 (n/a)</td><td>187.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.18 <b>(+22.26%)</b></td><td>0.13 <b>(+20.45%)</b></td><td>0.12 <b>(+43.72%)</b></td><td>0.07 (-9.93%)</td><td>0.05 <b>(+38.88%)</b></td><td>549.80 (+11.03%)</td><td>336.76 (-12.50%)</td><td>298.50 <b>(-30.42%)</b></td><td>201.50 (-18.22%)</td><td>143.89 <b>(+23.93%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>495.20 (n/a)</td><td>384.86 (n/a)</td><td>429.00 (n/a)</td><td>246.40 (n/a)</td><td>116.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (-10.33%)</td><td>0.07 <b>(-34.02%)</b></td><td>0.06 <b>(-53.28%)</b></td><td>0.05 (+10.18%)</td><td>0.03 <b>(-23.35%)</b></td><td>618.10 (-9.24%)</td><td>499.16 <b>(+42.31%)</b></td><td>558.70 <b>(+114.06%)</b></td><td>271.30 (+11.51%)</td><td>137.90 <b>(-26.51%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>681.00 (n/a)</td><td>350.76 (n/a)</td><td>261.00 (n/a)</td><td>243.30 (n/a)</td><td>187.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (-6.39%)</td><td>0.09 <b>(-25.37%)</b></td><td>0.09 <b>(-28.39%)</b></td><td>0.04 <b>(-61.25%)</b></td><td>0.05 <b>(+99.91%)</b></td><td>1037.40 <b>(+158.06%)</b></td><td>519.14 <b>(+68.13%)</b></td><td>415.60 <b>(+39.65%)</b></td><td>253.70 (+6.82%)</td><td>319.70 <b>(+437.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>402.00 (n/a)</td><td>308.78 (n/a)</td><td>297.60 (n/a)</td><td>237.50 (n/a)</td><td>59.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 <b>(-33.45%)</b></td><td>0.07 (-7.05%)</td><td>0.07 (+0.73%)</td><td>0.05 (-3.47%)</td><td>0.02 <b>(-55.72%)</b></td><td>624.60 (+3.58%)</td><td>456.36 (+0.48%)</td><td>450.30 (-0.73%)</td><td>353.50 <b>(+50.30%)</b></td><td>103.45 <b>(-24.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>603.00 (n/a)</td><td>454.16 (n/a)</td><td>453.60 (n/a)</td><td>235.20 (n/a)</td><td>137.67 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (+1.18%)</td><td>0.08 <b>(+51.04%)</b></td><td>0.08 <b>(+97.25%)</b></td><td>0.04 <b>(+29.84%)</b></td><td>0.02 (-10.16%)</td><td>497.10 <b>(-22.99%)</b></td><td>293.98 <b>(-35.88%)</b></td><td>246.00 <b>(-49.31%)</b></td><td>233.00 (-1.15%)</td><td>113.70 <b>(-24.58%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>645.50 (n/a)</td><td>458.50 (n/a)</td><td>485.30 (n/a)</td><td>235.70 (n/a)</td><td>150.77 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 <b>(+30.68%)</b></td><td>0.06 (-2.51%)</td><td>0.07 (-2.67%)</td><td>0.03 (-5.41%)</td><td>0.03 <b>(+63.91%)</b></td><td>628.40 (+5.72%)</td><td>389.00 (+12.33%)</td><td>297.30 (+2.73%)</td><td>204.90 <b>(-23.46%)</b></td><td>185.73 <b>(+33.52%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.40 (n/a)</td><td>346.30 (n/a)</td><td>289.40 (n/a)</td><td>267.70 (n/a)</td><td>139.10 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 <b>(-30.75%)</b></td><td>0.06 (-0.26%)</td><td>0.06 <b>(+35.47%)</b></td><td>0.04 (-4.96%)</td><td>0.02 <b>(-45.79%)</b></td><td>563.60 (+5.21%)</td><td>386.32 (-8.44%)</td><td>346.90 <b>(-26.19%)</b></td><td>242.40 <b>(+44.46%)</b></td><td>131.58 (-9.72%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>535.70 (n/a)</td><td>421.92 (n/a)</td><td>470.00 (n/a)</td><td>167.80 (n/a)</td><td>145.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (+1.93%)</td><td>0.06 (+3.96%)</td><td>0.04 (+7.23%)</td><td>0.04 (+7.82%)</td><td>0.02 (-0.41%)</td><td>519.40 (-7.25%)</td><td>406.22 (-4.56%)</td><td>459.40 (-6.76%)</td><td>258.60 (-1.90%)</td><td>128.64 (-7.73%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>560.00 (n/a)</td><td>425.64 (n/a)</td><td>492.70 (n/a)</td><td>263.60 (n/a)</td><td>139.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (+0.34%)</td><td>0.06 <b>(+45.27%)</b></td><td>0.07 <b>(+112.80%)</b></td><td>0.03 <b>(+28.49%)</b></td><td>0.02 (-11.04%)</td><td>621.30 <b>(-22.17%)</b></td><td>376.00 <b>(-35.09%)</b></td><td>313.30 <b>(-53.01%)</b></td><td>236.80 (-0.34%)</td><td>159.21 <b>(-26.36%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>798.30 (n/a)</td><td>579.26 (n/a)</td><td>666.70 (n/a)</td><td>237.60 (n/a)</td><td>216.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (+15.60%)</td><td>0.06 (-1.39%)</td><td>0.05 <b>(-23.75%)</b></td><td>0.04 (+17.16%)</td><td>0.02 (+13.43%)</td><td>476.40 (-14.65%)</td><td>382.50 (+0.99%)</td><td>425.20 <b>(+31.15%)</b></td><td>234.70 (-13.49%)</td><td>99.53 (-17.01%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.20 (n/a)</td><td>378.74 (n/a)</td><td>324.20 (n/a)</td><td>271.30 (n/a)</td><td>119.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (-12.06%)</td><td>0.06 (-14.71%)</td><td>0.05 (-14.10%)</td><td>0.04 (-7.50%)</td><td>0.02 (-19.75%)</td><td>600.30 (+8.12%)</td><td>472.30 (+15.84%)</td><td>533.20 (+16.42%)</td><td>315.40 (+13.70%)</td><td>131.32 (+5.36%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>555.20 (n/a)</td><td>407.70 (n/a)</td><td>458.00 (n/a)</td><td>277.40 (n/a)</td><td>124.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 <b>(+23.72%)</b></td><td>0.09 <b>(+73.93%)</b></td><td>0.08 <b>(+56.48%)</b></td><td>0.08 <b>(+549.43%)</b></td><td>0.01 <b>(-52.64%)</b></td><td>321.30 <b>(-84.60%)</b></td><td>283.10 <b>(-62.64%)</b></td><td>302.10 <b>(-36.09%)</b></td><td>242.20 (-19.16%)</td><td>37.39 <b>(-95.00%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2086.90 (n/a)</td><td>757.80 (n/a)</td><td>472.70 (n/a)</td><td>299.60 (n/a)</td><td>747.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (-14.32%)</td><td>0.07 (+7.43%)</td><td>0.07 <b>(+30.52%)</b></td><td>0.05 (+18.49%)</td><td>0.02 <b>(-30.37%)</b></td><td>515.80 (-15.61%)</td><td>368.20 (-12.03%)</td><td>337.20 <b>(-23.38%)</b></td><td>274.30 (+16.72%)</td><td>102.27 <b>(-31.14%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>611.20 (n/a)</td><td>418.54 (n/a)</td><td>440.10 (n/a)</td><td>235.00 (n/a)</td><td>148.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (+4.14%)</td><td>0.07 <b>(+21.50%)</b></td><td>0.06 (+7.76%)</td><td>0.05 (+9.72%)</td><td>0.03 <b>(+22.40%)</b></td><td>514.50 (-8.86%)</td><td>376.82 (-15.72%)</td><td>433.50 (-7.19%)</td><td>243.50 (-3.94%)</td><td>124.79 (+6.94%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.50 (n/a)</td><td>447.12 (n/a)</td><td>467.10 (n/a)</td><td>253.50 (n/a)</td><td>116.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (-14.41%)</td><td>0.05 <b>(-20.91%)</b></td><td>0.04 (-16.67%)</td><td>0.01 <b>(-69.93%)</b></td><td>0.03 (+15.17%)</td><td>1950.10 <b>(+232.55%)</b></td><td>759.58 <b>(+75.37%)</b></td><td>583.60 (+19.98%)</td><td>282.80 (+16.81%)</td><td>681.25 <b>(+375.65%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>586.40 (n/a)</td><td>433.12 (n/a)</td><td>486.40 (n/a)</td><td>242.10 (n/a)</td><td>143.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 <b>(+70.78%)</b></td><td>0.06 <b>(+27.41%)</b></td><td>0.06 (+4.36%)</td><td>0.01 <b>(-29.80%)</b></td><td>0.04 <b>(+98.55%)</b></td><td>1983.10 <b>(+42.44%)</b></td><td>681.76 (+8.68%)</td><td>438.90 (-4.17%)</td><td>220.70 <b>(-41.44%)</b></td><td>733.40 <b>(+70.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1392.20 (n/a)</td><td>627.32 (n/a)</td><td>458.00 (n/a)</td><td>376.90 (n/a)</td><td>428.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 <b>(+37.38%)</b></td><td>0.07 (+18.57%)</td><td>0.06 (+1.18%)</td><td>0.04 (+4.84%)</td><td>0.03 <b>(+50.67%)</b></td><td>501.80 (-4.62%)</td><td>301.82 (-12.10%)</td><td>298.90 (-1.16%)</td><td>164.30 <b>(-27.20%)</b></td><td>125.41 (+4.05%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>526.10 (n/a)</td><td>343.36 (n/a)</td><td>302.40 (n/a)</td><td>225.70 (n/a)</td><td>120.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (+10.39%)</td><td>0.04 (-13.44%)</td><td>0.04 (-16.74%)</td><td>0.01 <b>(-72.88%)</b></td><td>0.02 <b>(+62.84%)</b></td><td>2049.70 <b>(+268.72%)</b></td><td>727.30 <b>(+80.41%)</b></td><td>510.00 <b>(+20.08%)</b></td><td>255.80 (-9.42%)</td><td>748.41 <b>(+525.82%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>555.90 (n/a)</td><td>403.14 (n/a)</td><td>424.70 (n/a)</td><td>282.40 (n/a)</td><td>119.59 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (-15.13%)</td><td>0.05 <b>(-26.12%)</b></td><td>0.04 <b>(-37.58%)</b></td><td>0.03 (-19.66%)</td><td>0.02 (+12.52%)</td><td>621.20 <b>(+24.49%)</b></td><td>449.80 <b>(+42.38%)</b></td><td>447.40 <b>(+60.19%)</b></td><td>270.30 (+17.83%)</td><td>166.01 <b>(+57.51%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>499.00 (n/a)</td><td>315.92 (n/a)</td><td>279.30 (n/a)</td><td>229.40 (n/a)</td><td>105.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (-10.22%)</td><td>0.05 <b>(+28.75%)</b></td><td>0.06 <b>(+55.74%)</b></td><td>0.04 <b>(+122.85%)</b></td><td>0.02 <b>(-39.90%)</b></td><td>470.80 <b>(-55.12%)</b></td><td>360.92 <b>(-35.54%)</b></td><td>330.50 <b>(-35.79%)</b></td><td>243.70 (+11.38%)</td><td>97.46 <b>(-67.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1049.10 (n/a)</td><td>559.90 (n/a)</td><td>514.70 (n/a)</td><td>218.80 (n/a)</td><td>302.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 <b>(+43.24%)</b></td><td>0.07 <b>(+36.76%)</b></td><td>0.07 <b>(+51.12%)</b></td><td>0.03 <b>(-33.83%)</b></td><td>0.03 <b>(+116.68%)</b></td><td>718.80 <b>(+51.14%)</b></td><td>327.90 (-12.31%)</td><td>252.10 <b>(-33.83%)</b></td><td>184.70 <b>(-30.20%)</b></td><td>221.51 <b>(+146.20%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>475.60 (n/a)</td><td>373.94 (n/a)</td><td>381.00 (n/a)</td><td>264.60 (n/a)</td><td>89.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 <b>(+27.93%)</b></td><td>0.05 (+15.33%)</td><td>0.04 (-9.30%)</td><td>0.04 <b>(+31.09%)</b></td><td>0.02 <b>(+44.03%)</b></td><td>454.30 <b>(-23.71%)</b></td><td>376.82 (-12.09%)</td><td>443.40 (+10.24%)</td><td>249.20 <b>(-21.83%)</b></td><td>97.76 (-11.54%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>595.50 (n/a)</td><td>428.64 (n/a)</td><td>402.20 (n/a)</td><td>318.80 (n/a)</td><td>110.51 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.39 (+14.49%)</td><td>0.28 <b>(+50.70%)</b></td><td>0.32 <b>(+80.23%)</b></td><td>0.15 <b>(+196.93%)</b></td><td>0.11 (-0.10%)</td><td>644.00 <b>(-66.32%)</b></td><td>410.80 <b>(-47.99%)</b></td><td>304.20 <b>(-44.51%)</b></td><td>251.10 (-12.66%)</td><td>181.06 <b>(-72.05%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>0.11 (n/a)</td><td>1912.30 (n/a)</td><td>789.78 (n/a)</td><td>548.20 (n/a)</td><td>287.50 (n/a)</td><td>647.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.53 <b>(+82.68%)</b></td><td>0.33 <b>(+58.58%)</b></td><td>0.36 <b>(+82.05%)</b></td><td>0.16 (+6.89%)</td><td>0.16 <b>(+156.83%)</b></td><td>628.70 (-6.44%)</td><td>375.04 <b>(-25.95%)</b></td><td>276.20 <b>(-45.08%)</b></td><td>187.10 <b>(-45.24%)</b></td><td>204.64 <b>(+37.28%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>672.00 (n/a)</td><td>506.48 (n/a)</td><td>502.90 (n/a)</td><td>341.70 (n/a)</td><td>149.07 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.35 (-5.69%)</td><td>0.21 (-19.47%)</td><td>0.18 <b>(-21.96%)</b></td><td>0.16 (-8.48%)</td><td>0.08 (-3.08%)</td><td>596.70 (+9.27%)</td><td>512.40 <b>(+24.85%)</b></td><td>559.00 <b>(+28.15%)</b></td><td>284.50 (+6.04%)</td><td>130.00 (+10.23%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>546.10 (n/a)</td><td>410.42 (n/a)</td><td>436.20 (n/a)</td><td>268.30 (n/a)</td><td>117.94 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.34 (+10.98%)</td><td>0.26 <b>(+31.87%)</b></td><td>0.29 <b>(+45.35%)</b></td><td>0.14 <b>(+56.94%)</b></td><td>0.08 (-13.45%)</td><td>519.80 <b>(-36.28%)</b></td><td>318.62 <b>(-32.12%)</b></td><td>257.50 <b>(-31.20%)</b></td><td>216.10 (-9.92%)</td><td>123.04 <b>(-49.70%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>815.80 (n/a)</td><td>469.40 (n/a)</td><td>374.30 (n/a)</td><td>239.90 (n/a)</td><td>244.61 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.26 <b>(-40.42%)</b></td><td>0.13 <b>(-34.57%)</b></td><td>0.14 (-9.15%)</td><td>0.03 <b>(-57.14%)</b></td><td>0.09 <b>(-32.97%)</b></td><td>2466.40 <b>(+133.30%)</b></td><td>1124.46 <b>(+107.19%)</b></td><td>511.60 (+10.07%)</td><td>287.40 <b>(+67.87%)</b></td><td>984.48 <b>(+202.16%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.43 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>1057.20 (n/a)</td><td>542.72 (n/a)</td><td>464.80 (n/a)</td><td>171.20 (n/a)</td><td>325.81 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.32 (+1.66%)</td><td>0.20 (-3.04%)</td><td>0.17 <b>(-25.23%)</b></td><td>0.16 <b>(+137.93%)</b></td><td>0.06 <b>(-38.43%)</b></td><td>447.50 <b>(-57.97%)</b></td><td>387.54 (-19.94%)</td><td>436.50 <b>(+33.77%)</b></td><td>232.80 (-1.61%)</td><td>89.98 <b>(-74.16%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>0.11 (n/a)</td><td>1064.80 (n/a)</td><td>484.04 (n/a)</td><td>326.30 (n/a)</td><td>236.60 (n/a)</td><td>348.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (+9.09%)</td><td>0.10 (+0.18%)</td><td>0.11 (-7.70%)</td><td>0.06 <b>(+20.07%)</b></td><td>0.04 (-0.82%)</td><td>611.90 (-16.73%)</td><td>406.72 (-2.87%)</td><td>328.40 (+8.35%)</td><td>246.60 (-8.33%)</td><td>161.68 (-19.13%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>734.80 (n/a)</td><td>418.74 (n/a)</td><td>303.10 (n/a)</td><td>269.00 (n/a)</td><td>199.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+3.07%)</td><td>0.09 (-9.32%)</td><td>0.12 (+15.74%)</td><td>0.02 <b>(-69.64%)</b></td><td>0.05 <b>(+99.38%)</b></td><td>1947.60 <b>(+229.43%)</b></td><td>680.26 <b>(+77.00%)</b></td><td>297.60 (-13.59%)</td><td>282.90 (-2.98%)</td><td>719.49 <b>(+497.49%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>591.20 (n/a)</td><td>384.32 (n/a)</td><td>344.40 (n/a)</td><td>291.60 (n/a)</td><td>120.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (+15.87%)</td><td>0.11 (+16.08%)</td><td>0.12 <b>(+50.44%)</b></td><td>0.07 (+8.05%)</td><td>0.04 <b>(+21.63%)</b></td><td>538.70 (-7.44%)</td><td>368.30 (-11.62%)</td><td>312.30 <b>(-33.52%)</b></td><td>235.90 (-13.72%)</td><td>143.82 (+6.12%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>582.00 (n/a)</td><td>416.74 (n/a)</td><td>469.80 (n/a)</td><td>273.40 (n/a)</td><td>135.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (-9.13%)</td><td>0.10 (-2.58%)</td><td>0.08 (-5.81%)</td><td>0.06 (-12.58%)</td><td>0.04 (-0.57%)</td><td>571.80 (+14.41%)</td><td>405.68 (+4.36%)</td><td>447.00 (+6.15%)</td><td>243.70 (+10.07%)</td><td>142.51 (+17.97%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>499.80 (n/a)</td><td>388.74 (n/a)</td><td>421.10 (n/a)</td><td>221.40 (n/a)</td><td>120.81 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (-7.10%)</td><td>0.07 (-13.54%)</td><td>0.08 (-7.69%)</td><td>0.03 <b>(-40.18%)</b></td><td>0.03 (+10.50%)</td><td>1129.80 <b>(+67.15%)</b></td><td>610.34 <b>(+25.10%)</b></td><td>468.90 (+8.34%)</td><td>367.10 (+7.62%)</td><td>304.46 <b>(+106.98%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>675.90 (n/a)</td><td>487.90 (n/a)</td><td>432.80 (n/a)</td><td>341.10 (n/a)</td><td>147.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (+1.51%)</td><td>0.10 (+8.73%)</td><td>0.07 (-7.68%)</td><td>0.06 (-2.39%)</td><td>0.05 <b>(+34.11%)</b></td><td>604.20 (+2.44%)</td><td>432.24 (-0.81%)</td><td>495.60 (+8.33%)</td><td>238.40 (-1.49%)</td><td>176.38 <b>(+40.31%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>589.80 (n/a)</td><td>435.76 (n/a)</td><td>457.50 (n/a)</td><td>242.00 (n/a)</td><td>125.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (+16.93%)</td><td>0.12 (+9.35%)</td><td>0.13 (+0.54%)</td><td>0.07 (-12.25%)</td><td>0.04 <b>(+32.85%)</b></td><td>583.80 (+13.96%)</td><td>364.38 (-5.05%)</td><td>306.20 (-0.52%)</td><td>252.20 (-14.48%)</td><td>139.36 <b>(+25.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>512.30 (n/a)</td><td>383.74 (n/a)</td><td>307.80 (n/a)</td><td>294.90 (n/a)</td><td>110.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 <b>(+71.91%)</b></td><td>0.12 <b>(+59.20%)</b></td><td>0.15 <b>(+103.74%)</b></td><td>0.02 <b>(-66.64%)</b></td><td>0.06 <b>(+352.46%)</b></td><td>2058.90 <b>(+199.74%)</b></td><td>639.50 (+14.82%)</td><td>280.60 <b>(-50.91%)</b></td><td>267.60 <b>(-41.84%)</b></td><td>793.79 <b>(+741.62%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>686.90 (n/a)</td><td>556.96 (n/a)</td><td>571.60 (n/a)</td><td>460.10 (n/a)</td><td>94.32 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (+4.47%)</td><td>0.10 <b>(+36.76%)</b></td><td>0.09 <b>(+30.10%)</b></td><td>0.07 <b>(+328.06%)</b></td><td>0.04 <b>(-30.30%)</b></td><td>583.20 <b>(-76.64%)</b></td><td>440.36 <b>(-53.72%)</b></td><td>457.80 <b>(-23.14%)</b></td><td>248.80 (-4.27%)</td><td>122.18 <b>(-86.32%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2496.40 (n/a)</td><td>951.46 (n/a)</td><td>595.60 (n/a)</td><td>259.90 (n/a)</td><td>893.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.20 <b>(+30.67%)</b></td><td>0.12 (+19.08%)</td><td>0.08 (-12.98%)</td><td>0.07 (-6.65%)</td><td>0.06 <b>(+86.86%)</b></td><td>594.00 (+7.12%)</td><td>433.52 (-4.22%)</td><td>538.80 (+14.93%)</td><td>203.00 <b>(-23.48%)</b></td><td>187.14 <b>(+68.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>554.50 (n/a)</td><td>452.60 (n/a)</td><td>468.80 (n/a)</td><td>265.30 (n/a)</td><td>110.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 <b>(+43.13%)</b></td><td>0.11 <b>(+36.65%)</b></td><td>0.10 <b>(+21.36%)</b></td><td>0.06 (+4.39%)</td><td>0.04 <b>(+113.47%)</b></td><td>698.20 (-4.21%)</td><td>428.76 <b>(-21.39%)</b></td><td>419.50 (-17.60%)</td><td>281.20 <b>(-30.14%)</b></td><td>170.80 <b>(+33.81%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>728.90 (n/a)</td><td>545.44 (n/a)</td><td>509.10 (n/a)</td><td>402.50 (n/a)</td><td>127.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (+0.08%)</td><td>0.10 (+6.50%)</td><td>0.09 (-4.63%)</td><td>0.07 (+2.10%)</td><td>0.04 (+19.14%)</td><td>595.30 (-2.06%)</td><td>428.28 (-3.84%)</td><td>450.50 (+4.86%)</td><td>280.90 (-0.11%)</td><td>138.50 (+13.02%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>607.80 (n/a)</td><td>445.38 (n/a)</td><td>429.60 (n/a)</td><td>281.20 (n/a)</td><td>122.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (+1.82%)</td><td>0.10 (+17.76%)</td><td>0.11 <b>(+60.83%)</b></td><td>0.06 (-15.87%)</td><td>0.04 (+18.99%)</td><td>606.10 (+18.87%)</td><td>386.40 (-10.85%)</td><td>308.00 <b>(-37.82%)</b></td><td>241.60 (-1.79%)</td><td>159.47 <b>(+40.85%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>509.90 (n/a)</td><td>433.44 (n/a)</td><td>495.30 (n/a)</td><td>246.00 (n/a)</td><td>113.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+9.57%)</td><td>0.10 (+9.29%)</td><td>0.11 <b>(+45.31%)</b></td><td>0.06 (-6.36%)</td><td>0.03 <b>(+21.85%)</b></td><td>580.90 (+6.78%)</td><td>404.06 (-5.32%)</td><td>317.40 <b>(-31.18%)</b></td><td>275.50 (-8.74%)</td><td>148.05 <b>(+26.54%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>544.00 (n/a)</td><td>426.76 (n/a)</td><td>461.20 (n/a)</td><td>301.90 (n/a)</td><td>117.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.20 <b>(+140.34%)</b></td><td>0.09 <b>(+58.31%)</b></td><td>0.06 (-11.54%)</td><td>0.03 <b>(+100.32%)</b></td><td>0.07 <b>(+92.37%)</b></td><td>1021.10 <b>(-50.08%)</b></td><td>557.32 <b>(-46.77%)</b></td><td>544.20 (+13.07%)</td><td>173.20 <b>(-58.39%)</b></td><td>306.09 <b>(-63.33%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2045.40 (n/a)</td><td>1047.02 (n/a)</td><td>481.30 (n/a)</td><td>416.20 (n/a)</td><td>834.77 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 <b>(-20.79%)</b></td><td>0.09 <b>(+21.97%)</b></td><td>0.10 <b>(+55.91%)</b></td><td>0.02 (-0.66%)</td><td>0.04 (-13.09%)</td><td>1924.50 (+0.67%)</td><td>649.84 (-13.09%)</td><td>337.80 <b>(-35.86%)</b></td><td>300.40 <b>(+26.22%)</b></td><td>713.09 (+7.56%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1911.70 (n/a)</td><td>747.68 (n/a)</td><td>526.70 (n/a)</td><td>238.00 (n/a)</td><td>662.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+0.17%)</td><td>0.09 (+12.87%)</td><td>0.08 (+1.87%)</td><td>0.06 <b>(+149.31%)</b></td><td>0.03 <b>(-32.09%)</b></td><td>553.00 <b>(-59.89%)</b></td><td>411.06 <b>(-31.79%)</b></td><td>454.80 (-1.83%)</td><td>265.30 (-0.19%)</td><td>120.95 <b>(-73.41%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1378.70 (n/a)</td><td>602.66 (n/a)</td><td>463.30 (n/a)</td><td>265.80 (n/a)</td><td>454.88 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+9.71%)</td><td>0.09 (+0.19%)</td><td>0.09 (+6.18%)</td><td>0.06 (+7.26%)</td><td>0.03 (-3.84%)</td><td>537.00 (-6.77%)</td><td>414.28 (-1.48%)</td><td>402.70 (-5.82%)</td><td>270.10 (-8.87%)</td><td>103.41 (-15.10%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>576.00 (n/a)</td><td>420.52 (n/a)</td><td>427.60 (n/a)</td><td>296.40 (n/a)</td><td>121.80 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.53 (+15.68%)</td><td>0.35 <b>(+22.90%)</b></td><td>0.26 (+10.85%)</td><td>0.22 (+8.46%)</td><td>0.15 <b>(+42.30%)</b></td><td>585.80 (-7.79%)</td><td>433.94 (-14.18%)</td><td>502.20 (-9.79%)</td><td>246.00 (-13.56%)</td><td>161.80 (+17.99%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.46 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>635.30 (n/a)</td><td>505.62 (n/a)</td><td>556.70 (n/a)</td><td>284.60 (n/a)</td><td>137.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.29 <b>(-25.24%)</b></td><td>0.24 (-14.44%)</td><td>0.23 (+4.22%)</td><td>0.21 (+0.97%)</td><td>0.03 <b>(-65.50%)</b></td><td>637.10 (-0.96%)</td><td>552.86 (+8.29%)</td><td>573.90 (-4.06%)</td><td>449.60 <b>(+33.77%)</b></td><td>73.55 <b>(-53.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>643.30 (n/a)</td><td>510.52 (n/a)</td><td>598.20 (n/a)</td><td>336.10 (n/a)</td><td>159.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.46 (+5.30%)</td><td>0.29 (+5.05%)</td><td>0.26 (+10.76%)</td><td>0.16 <b>(-26.67%)</b></td><td>0.13 <b>(+31.63%)</b></td><td>835.00 <b>(+36.37%)</b></td><td>532.06 (+3.28%)</td><td>499.30 (-9.71%)</td><td>282.90 (-5.04%)</td><td>225.82 <b>(+75.20%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>612.30 (n/a)</td><td>515.18 (n/a)</td><td>553.00 (n/a)</td><td>297.90 (n/a)</td><td>128.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.00 <b>(+166.67%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+461.25%)</b></td><td>20937.02 (+19.16%)</td><td>12378.30 <b>(-26.32%)</b></td><td>14429.78 (-17.05%)</td><td>5300.67 <b>(-64.09%)</b></td><td>6527.12 <b>(+457.63%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17570.16 (n/a)</td><td>16801.02 (n/a)</td><td>17395.01 (n/a)</td><td>14761.21 (n/a)</td><td>1170.51 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.00 (+0.00%)</td><td>0.00 (+9.37%)</td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+12.69%)</td><td>18892.26 (-9.74%)</td><td>12938.64 (-9.50%)</td><td>14232.17 (-5.52%)</td><td>8124.65 (+1.96%)</td><td>4635.26 (-13.96%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20931.46 (n/a)</td><td>14297.45 (n/a)</td><td>15063.24 (n/a)</td><td>7968.39 (n/a)</td><td>5387.25 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (-8.08%)</td><td>0.10 (+2.66%)</td><td>0.09 (-6.25%)</td><td>0.07 (+2.48%)</td><td>0.03 (-9.15%)</td><td>29848.17 (-2.31%)</td><td>22786.95 (-3.47%)</td><td>24525.94 (+6.61%)</td><td>16461.40 (+8.80%)</td><td>5726.25 (-7.66%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30553.66 (n/a)</td><td>23605.34 (n/a)</td><td>23005.57 (n/a)</td><td>15130.45 (n/a)</td><td>6201.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.84 <b>(-40.58%)</b></td><td>1.36 (-7.40%)</td><td>1.57 <b>(+185.47%)</b></td><td>0.30 (-2.56%)</td><td>0.62 <b>(-56.61%)</b></td><td>3535.30 (+2.63%)</td><td>1231.00 <b>(-27.76%)</b></td><td>667.00 <b>(-64.97%)</b></td><td>570.10 <b>(+68.27%)</b></td><td>1290.35 (-4.81%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.10 (n/a)</td><td>1.46 (n/a)</td><td>0.55 (n/a)</td><td>0.30 (n/a)</td><td>1.43 (n/a)</td><td>3444.80 (n/a)</td><td>1703.94 (n/a)</td><td>1904.10 (n/a)</td><td>338.80 (n/a)</td><td>1355.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.20 (+7.04%)</td><td>1.78 (-3.48%)</td><td>1.13 <b>(-43.77%)</b></td><td>0.50 <b>(+66.40%)</b></td><td>1.29 <b>(+24.19%)</b></td><td>2097.60 <b>(-39.91%)</b></td><td>961.10 (-12.82%)</td><td>927.90 <b>(+77.83%)</b></td><td>327.50 (-6.56%)</td><td>726.94 <b>(-45.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.99 (n/a)</td><td>1.85 (n/a)</td><td>2.01 (n/a)</td><td>0.30 (n/a)</td><td>1.04 (n/a)</td><td>3490.50 (n/a)</td><td>1102.38 (n/a)</td><td>521.80 (n/a)</td><td>350.50 (n/a)</td><td>1342.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.43 <b>(+56.92%)</b></td><td>2.42 <b>(+73.17%)</b></td><td>2.78 <b>(+59.67%)</b></td><td>1.38 <b>(+357.91%)</b></td><td>0.85 (+13.18%)</td><td>759.30 <b>(-78.16%)</b></td><td>484.84 <b>(-60.88%)</b></td><td>377.60 <b>(-37.36%)</b></td><td>306.00 <b>(-36.26%)</b></td><td>191.42 <b>(-84.92%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.18 (n/a)</td><td>1.40 (n/a)</td><td>1.74 (n/a)</td><td>0.30 (n/a)</td><td>0.75 (n/a)</td><td>3476.70 (n/a)</td><td>1239.38 (n/a)</td><td>602.80 (n/a)</td><td>480.10 (n/a)</td><td>1269.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.79 (+2.06%)</td><td>2.54 (+4.77%)</td><td>2.62 (+1.75%)</td><td>1.58 (+8.06%)</td><td>0.84 (-6.47%)</td><td>664.00 (-7.46%)</td><td>451.26 (-6.89%)</td><td>400.40 (-1.69%)</td><td>276.70 (-2.02%)</td><td>148.05 (-17.34%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.71 (n/a)</td><td>2.42 (n/a)</td><td>2.57 (n/a)</td><td>1.46 (n/a)</td><td>0.90 (n/a)</td><td>717.50 (n/a)</td><td>484.64 (n/a)</td><td>407.30 (n/a)</td><td>282.40 (n/a)</td><td>179.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>4.34 (+11.04%)</td><td>3.31 (+5.69%)</td><td>3.35 (+4.91%)</td><td>1.91 (-6.67%)</td><td>0.89 (+11.51%)</td><td>1096.60 (+7.14%)</td><td>683.48 (-3.78%)</td><td>625.90 (-4.68%)</td><td>483.60 (-9.94%)</td><td>239.01 (+17.65%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.91 (n/a)</td><td>3.13 (n/a)</td><td>3.19 (n/a)</td><td>2.05 (n/a)</td><td>0.79 (n/a)</td><td>1023.50 (n/a)</td><td>710.30 (n/a)</td><td>656.60 (n/a)</td><td>537.00 (n/a)</td><td>203.15 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.05 (+16.48%)</td><td>3.11 (+6.13%)</td><td>3.59 <b>(+21.42%)</b></td><td>0.58 <b>(-69.25%)</b></td><td>1.65 <b>(+58.13%)</b></td><td>3595.10 <b>(+225.20%)</b></td><td>1190.12 <b>(+50.01%)</b></td><td>583.40 (-17.65%)</td><td>415.10 (-14.15%)</td><td>1350.87 <b>(+378.22%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.34 (n/a)</td><td>2.93 (n/a)</td><td>2.96 (n/a)</td><td>1.90 (n/a)</td><td>1.04 (n/a)</td><td>1105.50 (n/a)</td><td>793.36 (n/a)</td><td>708.40 (n/a)</td><td>483.50 (n/a)</td><td>282.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.31 <b>(+27.20%)</b></td><td>3.67 <b>(+69.33%)</b></td><td>3.95 <b>(+78.61%)</b></td><td>2.43 <b>(+318.23%)</b></td><td>1.22 <b>(-22.33%)</b></td><td>861.80 <b>(-76.09%)</b></td><td>628.00 <b>(-64.89%)</b></td><td>530.80 <b>(-44.01%)</b></td><td>394.70 <b>(-21.39%)</b></td><td>214.04 <b>(-85.76%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.18 (n/a)</td><td>2.17 (n/a)</td><td>2.21 (n/a)</td><td>0.58 (n/a)</td><td>1.58 (n/a)</td><td>3604.20 (n/a)</td><td>1788.48 (n/a)</td><td>948.00 (n/a)</td><td>502.10 (n/a)</td><td>1503.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.73 (+14.68%)</td><td>3.40 (-2.16%)</td><td>3.44 (-2.91%)</td><td>0.61 <b>(-71.80%)</b></td><td>1.85 <b>(+78.96%)</b></td><td>3446.70 <b>(+254.67%)</b></td><td>1121.70 <b>(+72.29%)</b></td><td>609.50 (+3.01%)</td><td>366.30 (-12.79%)</td><td>1304.85 <b>(+536.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.99 (n/a)</td><td>3.47 (n/a)</td><td>3.54 (n/a)</td><td>2.16 (n/a)</td><td>1.04 (n/a)</td><td>971.80 (n/a)</td><td>651.06 (n/a)</td><td>591.70 (n/a)</td><td>420.00 (n/a)</td><td>204.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.36 <b>(-32.97%)</b></td><td>3.53 (+9.25%)</td><td>2.53 (-10.21%)</td><td>2.32 <b>(+297.26%)</b></td><td>1.49 <b>(-51.44%)</b></td><td>905.40 <b>(-74.83%)</b></td><td>677.88 <b>(-60.79%)</b></td><td>829.20 (+11.38%)</td><td>391.00 <b>(+49.18%)</b></td><td>248.82 <b>(-85.25%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>8.00 (n/a)</td><td>3.23 (n/a)</td><td>2.82 (n/a)</td><td>0.58 (n/a)</td><td>3.07 (n/a)</td><td>3597.00 (n/a)</td><td>1729.00 (n/a)</td><td>744.50 (n/a)</td><td>262.10 (n/a)</td><td>1686.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>6.25 <b>(+77.88%)</b></td><td>4.28 <b>(+75.15%)</b></td><td>4.81 <b>(+74.70%)</b></td><td>2.16 <b>(+272.51%)</b></td><td>1.59 <b>(+43.64%)</b></td><td>968.80 <b>(-73.16%)</b></td><td>562.10 <b>(-57.00%)</b></td><td>436.00 <b>(-42.76%)</b></td><td>335.40 <b>(-43.79%)</b></td><td>253.89 <b>(-80.31%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.51 (n/a)</td><td>2.44 (n/a)</td><td>2.75 (n/a)</td><td>0.58 (n/a)</td><td>1.11 (n/a)</td><td>3608.90 (n/a)</td><td>1307.28 (n/a)</td><td>761.70 (n/a)</td><td>596.70 (n/a)</td><td>1289.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.06 (-7.55%)</td><td>3.81 <b>(+39.56%)</b></td><td>4.10 <b>(+133.62%)</b></td><td>1.16 (-3.10%)</td><td>1.56 (-18.19%)</td><td>3613.20 (+3.20%)</td><td>1480.48 <b>(-32.86%)</b></td><td>1023.10 <b>(-57.19%)</b></td><td>829.00 (+8.17%)</td><td>1196.49 (-4.93%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.47 (n/a)</td><td>2.73 (n/a)</td><td>1.75 (n/a)</td><td>1.20 (n/a)</td><td>1.91 (n/a)</td><td>3501.30 (n/a)</td><td>2205.20 (n/a)</td><td>2390.10 (n/a)</td><td>766.40 (n/a)</td><td>1258.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.91 <b>(+37.63%)</b></td><td>5.42 <b>(+28.39%)</b></td><td>4.06 (-14.04%)</td><td>3.51 <b>(+70.68%)</b></td><td>2.23 <b>(+39.03%)</b></td><td>1196.30 <b>(-41.41%)</b></td><td>878.76 <b>(-24.09%)</b></td><td>1032.10 (+16.33%)</td><td>530.10 <b>(-27.33%)</b></td><td>319.99 <b>(-42.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.75 (n/a)</td><td>4.22 (n/a)</td><td>4.73 (n/a)</td><td>2.05 (n/a)</td><td>1.60 (n/a)</td><td>2041.70 (n/a)</td><td>1157.68 (n/a)</td><td>887.20 (n/a)</td><td>729.50 (n/a)</td><td>556.80 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>8.18 (+3.05%)</td><td>6.40 (+5.00%)</td><td>6.10 (+2.16%)</td><td>5.35 <b>(+39.02%)</b></td><td>1.07 <b>(-31.69%)</b></td><td>784.40 <b>(-28.06%)</b></td><td>668.68 (-8.66%)</td><td>687.60 (-2.12%)</td><td>512.50 (-2.95%)</td><td>98.97 <b>(-54.73%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>7.94 (n/a)</td><td>6.09 (n/a)</td><td>5.97 (n/a)</td><td>3.85 (n/a)</td><td>1.56 (n/a)</td><td>1090.40 (n/a)</td><td>732.04 (n/a)</td><td>702.50 (n/a)</td><td>528.10 (n/a)</td><td>218.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>9.16 <b>(+31.33%)</b></td><td>5.70 <b>(+41.10%)</b></td><td>4.54 (-3.90%)</td><td>1.68 <b>(+35.79%)</b></td><td>3.24 <b>(+29.56%)</b></td><td>2496.30 <b>(-26.36%)</b></td><td>1070.02 <b>(-34.50%)</b></td><td>924.00 (+4.05%)</td><td>457.90 <b>(-23.86%)</b></td><td>835.79 <b>(-33.44%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>6.97 (n/a)</td><td>4.04 (n/a)</td><td>4.72 (n/a)</td><td>1.24 (n/a)</td><td>2.50 (n/a)</td><td>3389.70 (n/a)</td><td>1633.62 (n/a)</td><td>888.00 (n/a)</td><td>601.40 (n/a)</td><td>1255.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>9.26 (-14.65%)</td><td>4.33 <b>(-27.79%)</b></td><td>3.85 (-15.04%)</td><td>1.24 <b>(-43.34%)</b></td><td>3.17 (-9.68%)</td><td>3373.00 <b>(+76.50%)</b></td><td>1555.94 <b>(+63.42%)</b></td><td>1090.20 (+17.71%)</td><td>452.90 (+17.15%)</td><td>1179.40 <b>(+96.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>10.85 (n/a)</td><td>5.99 (n/a)</td><td>4.53 (n/a)</td><td>2.19 (n/a)</td><td>3.51 (n/a)</td><td>1911.10 (n/a)</td><td>952.12 (n/a)</td><td>926.20 (n/a)</td><td>386.60 (n/a)</td><td>601.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.53 <b>(-23.20%)</b></td><td>4.66 <b>(-35.31%)</b></td><td>4.10 <b>(-46.53%)</b></td><td>3.17 (-19.98%)</td><td>1.67 <b>(-21.27%)</b></td><td>1322.90 <b>(+24.97%)</b></td><td>976.66 <b>(+53.03%)</b></td><td>1022.10 <b>(+87.03%)</b></td><td>556.90 <b>(+30.21%)</b></td><td>274.74 (+12.21%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>9.81 (n/a)</td><td>7.20 (n/a)</td><td>7.67 (n/a)</td><td>3.96 (n/a)</td><td>2.12 (n/a)</td><td>1058.60 (n/a)</td><td>638.22 (n/a)</td><td>546.50 (n/a)</td><td>427.70 (n/a)</td><td>244.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.62 (-1.27%)</td><td>1.14 (-3.84%)</td><td>1.20 <b>(-24.37%)</b></td><td>0.49 <b>(+219.09%)</b></td><td>0.45 <b>(-31.40%)</b></td><td>1060.50 <b>(-68.66%)</b></td><td>548.16 <b>(-44.29%)</b></td><td>437.60 <b>(+32.21%)</b></td><td>323.80 (+1.28%)</td><td>300.39 <b>(-77.68%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>1.64 (n/a)</td><td>1.19 (n/a)</td><td>1.58 (n/a)</td><td>0.15 (n/a)</td><td>0.65 (n/a)</td><td>3383.90 (n/a)</td><td>984.04 (n/a)</td><td>331.00 (n/a)</td><td>319.70 (n/a)</td><td>1345.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>2.55 (-1.78%)</td><td>1.43 (+8.10%)</td><td>1.74 (+6.91%)</td><td>0.42 <b>(+43.43%)</b></td><td>0.91 (-9.21%)</td><td>2483.60 <b>(-30.28%)</b></td><td>1186.08 <b>(-31.70%)</b></td><td>603.20 (-6.47%)</td><td>411.50 (+1.81%)</td><td>936.14 <b>(-42.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.59 (n/a)</td><td>1.33 (n/a)</td><td>1.63 (n/a)</td><td>0.29 (n/a)</td><td>1.01 (n/a)</td><td>3562.20 (n/a)</td><td>1736.58 (n/a)</td><td>644.90 (n/a)</td><td>404.20 (n/a)</td><td>1637.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.57 (+6.98%)</td><td>2.89 <b>(+136.38%)</b></td><td>2.99 <b>(+348.81%)</b></td><td>2.15 <b>(+260.28%)</b></td><td>0.56 <b>(-52.91%)</b></td><td>974.10 <b>(-72.24%)</b></td><td>749.20 <b>(-71.33%)</b></td><td>700.90 <b>(-77.72%)</b></td><td>587.60 (-6.52%)</td><td>154.07 <b>(-87.28%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.34 (n/a)</td><td>1.22 (n/a)</td><td>0.67 (n/a)</td><td>0.60 (n/a)</td><td>1.19 (n/a)</td><td>3509.60 (n/a)</td><td>2613.22 (n/a)</td><td>3145.50 (n/a)</td><td>628.60 (n/a)</td><td>1211.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.63 <b>(-25.68%)</b></td><td>1.17 (-16.39%)</td><td>0.97 <b>(-34.48%)</b></td><td>0.91 (+9.51%)</td><td>0.32 <b>(-38.37%)</b></td><td>575.60 (-8.68%)</td><td>474.42 (+13.11%)</td><td>542.60 <b>(+52.63%)</b></td><td>321.70 <b>(+34.55%)</b></td><td>116.85 <b>(-24.07%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.19 (n/a)</td><td>1.40 (n/a)</td><td>1.47 (n/a)</td><td>0.83 (n/a)</td><td>0.53 (n/a)</td><td>630.30 (n/a)</td><td>419.44 (n/a)</td><td>355.50 (n/a)</td><td>239.10 (n/a)</td><td>153.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (+4.10%)</td><td>0.11 <b>(+33.29%)</b></td><td>0.12 <b>(+77.29%)</b></td><td>0.06 <b>(+22.00%)</b></td><td>0.04 (+15.90%)</td><td>540.70 (-18.04%)</td><td>345.00 <b>(-23.86%)</b></td><td>263.40 <b>(-43.61%)</b></td><td>229.60 (-3.93%)</td><td>143.88 (-5.92%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>659.70 (n/a)</td><td>453.10 (n/a)</td><td>467.10 (n/a)</td><td>239.00 (n/a)</td><td>152.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (+2.56%)</td><td>0.08 <b>(+23.36%)</b></td><td>0.07 <b>(+35.93%)</b></td><td>0.05 (+5.46%)</td><td>0.03 (+1.14%)</td><td>618.50 (-5.18%)</td><td>437.88 (-19.22%)</td><td>451.90 <b>(-26.42%)</b></td><td>248.70 (-2.47%)</td><td>160.86 (-2.77%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>652.30 (n/a)</td><td>542.04 (n/a)</td><td>614.20 (n/a)</td><td>255.00 (n/a)</td><td>165.43 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.22 (-6.46%)</td><td>0.15 (+1.71%)</td><td>0.16 <b>(+33.43%)</b></td><td>0.06 <b>(-42.89%)</b></td><td>0.06 (+10.66%)</td><td>1075.20 <b>(+75.11%)</b></td><td>543.34 (+9.28%)</td><td>420.50 <b>(-25.04%)</b></td><td>298.50 (+6.91%)</td><td>308.42 <b>(+132.28%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>614.00 (n/a)</td><td>497.22 (n/a)</td><td>561.00 (n/a)</td><td>279.20 (n/a)</td><td>132.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 <b>(-44.28%)</b></td><td>0.14 <b>(-25.60%)</b></td><td>0.14 (-7.40%)</td><td>0.11 (-17.09%)</td><td>0.02 <b>(-66.03%)</b></td><td>583.50 <b>(+20.61%)</b></td><td>478.10 <b>(+25.83%)</b></td><td>479.40 (+8.00%)</td><td>400.30 <b>(+79.51%)</b></td><td>79.58 <b>(-29.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>483.80 (n/a)</td><td>379.96 (n/a)</td><td>443.90 (n/a)</td><td>223.00 (n/a)</td><td>112.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.29 <b>(+47.81%)</b></td><td>0.19 <b>(+42.58%)</b></td><td>0.15 <b>(+40.35%)</b></td><td>0.12 <b>(+35.89%)</b></td><td>0.07 <b>(+63.40%)</b></td><td>541.00 <b>(-26.41%)</b></td><td>398.28 <b>(-27.71%)</b></td><td>424.70 <b>(-28.75%)</b></td><td>223.40 <b>(-32.34%)</b></td><td>141.47 (-16.71%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>735.20 (n/a)</td><td>550.98 (n/a)</td><td>596.10 (n/a)</td><td>330.20 (n/a)</td><td>169.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.66 <b>(+26.52%)</b></td><td>0.40 (-3.06%)</td><td>0.42 (-0.18%)</td><td>0.20 <b>(-29.37%)</b></td><td>0.19 <b>(+116.91%)</b></td><td>655.20 <b>(+41.57%)</b></td><td>393.00 <b>(+20.04%)</b></td><td>313.70 (+0.19%)</td><td>198.70 <b>(-20.96%)</b></td><td>193.48 <b>(+141.10%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>462.80 (n/a)</td><td>327.40 (n/a)</td><td>313.10 (n/a)</td><td>251.40 (n/a)</td><td>80.25 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.59 <b>(+29.30%)</b></td><td>0.42 <b>(+33.82%)</b></td><td>0.43 <b>(+54.71%)</b></td><td>0.22 (-6.86%)</td><td>0.13 <b>(+50.39%)</b></td><td>599.70 (+7.38%)</td><td>346.32 <b>(-21.19%)</b></td><td>308.20 <b>(-35.36%)</b></td><td>220.60 <b>(-22.65%)</b></td><td>146.42 <b>(+38.37%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>558.50 (n/a)</td><td>439.42 (n/a)</td><td>476.80 (n/a)</td><td>285.20 (n/a)</td><td>105.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.50 (+0.45%)</td><td>0.32 (-15.72%)</td><td>0.24 <b>(-32.54%)</b></td><td>0.22 <b>(-21.40%)</b></td><td>0.13 <b>(+29.91%)</b></td><td>604.30 <b>(+27.22%)</b></td><td>461.02 <b>(+25.86%)</b></td><td>551.50 <b>(+48.25%)</b></td><td>264.10 (-0.45%)</td><td>154.97 <b>(+69.39%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>475.00 (n/a)</td><td>366.30 (n/a)</td><td>372.00 (n/a)</td><td>265.30 (n/a)</td><td>91.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 <b>(-43.96%)</b></td><td>0.04 <b>(-23.13%)</b></td><td>0.03 (-3.26%)</td><td>0.03 (+4.00%)</td><td>0.01 <b>(-70.40%)</b></td><td>539.60 (-3.85%)</td><td>465.26 (+15.59%)</td><td>476.00 (+3.39%)</td><td>357.30 <b>(+78.47%)</b></td><td>76.93 <b>(-48.05%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>561.20 (n/a)</td><td>402.50 (n/a)</td><td>460.40 (n/a)</td><td>200.20 (n/a)</td><td>148.08 (n/a)</td>
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
