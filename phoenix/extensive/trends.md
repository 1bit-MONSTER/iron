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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 <b>(+20.86%)</b></td><td>0.02 (-1.49%)</td><td>0.01 <b>(-29.50%)</b></td><td>0.01 (-5.55%)</td><td>0.01 <b>(+53.98%)</b></td><td>676.20 (+5.89%)</td><td>403.74 (+8.77%)</td><td>420.90 <b>(+41.86%)</b></td><td>231.20 (-17.25%)</td><td>182.86 <b>(+20.42%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.60 (n/a)</td><td>371.20 (n/a)</td><td>296.70 (n/a)</td><td>279.40 (n/a)</td><td>151.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 <b>(+31.36%)</b></td><td>0.02 <b>(+38.32%)</b></td><td>0.02 <b>(+57.96%)</b></td><td>0.01 (-16.55%)</td><td>0.01 <b>(+103.17%)</b></td><td>616.70 (+19.82%)</td><td>343.44 <b>(-21.38%)</b></td><td>294.60 <b>(-36.69%)</b></td><td>240.10 <b>(-23.85%)</b></td><td>154.86 <b>(+104.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.70 (n/a)</td><td>436.84 (n/a)</td><td>465.30 (n/a)</td><td>315.30 (n/a)</td><td>75.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (+12.41%)</td><td>0.02 (+8.68%)</td><td>0.01 (-5.49%)</td><td>0.01 (-8.28%)</td><td>0.01 <b>(+21.91%)</b></td><td>650.80 (+9.03%)</td><td>402.66 (-5.14%)</td><td>424.20 (+5.81%)</td><td>241.60 (-11.05%)</td><td>164.19 (+12.08%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.90 (n/a)</td><td>424.46 (n/a)</td><td>400.90 (n/a)</td><td>271.60 (n/a)</td><td>146.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (-6.46%)</td><td>0.02 (+7.57%)</td><td>0.02 <b>(+41.30%)</b></td><td>0.01 (+13.33%)</td><td>0.01 (-8.19%)</td><td>580.90 (-11.76%)</td><td>385.12 (-9.20%)</td><td>323.00 <b>(-29.21%)</b></td><td>240.40 (+6.89%)</td><td>161.29 (-9.85%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.30 (n/a)</td><td>424.12 (n/a)</td><td>456.30 (n/a)</td><td>224.90 (n/a)</td><td>178.92 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (+0.19%)</td><td>0.02 (-7.62%)</td><td>0.01 (-13.73%)</td><td>0.01 (-13.66%)</td><td>0.01 (+10.35%)</td><td>618.20 (+15.81%)</td><td>449.46 (+12.52%)</td><td>498.90 (+15.92%)</td><td>243.70 (-0.20%)</td><td>169.86 <b>(+28.78%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.80 (n/a)</td><td>399.46 (n/a)</td><td>430.40 (n/a)</td><td>244.20 (n/a)</td><td>131.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+0.33%)</td><td>0.02 (+18.05%)</td><td>0.02 (+16.61%)</td><td>0.01 (+6.47%)</td><td>0.01 (-6.34%)</td><td>530.60 (-6.09%)</td><td>328.62 (-16.67%)</td><td>295.40 (-14.23%)</td><td>252.20 (-0.36%)</td><td>115.96 (-13.45%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.00 (n/a)</td><td>394.36 (n/a)</td><td>344.40 (n/a)</td><td>253.10 (n/a)</td><td>133.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (+4.36%)</td><td>0.04 (+13.56%)</td><td>0.05 (+14.10%)</td><td>0.03 <b>(+21.60%)</b></td><td>0.01 (-4.46%)</td><td>488.20 (-17.77%)</td><td>315.04 (-14.68%)</td><td>245.70 (-12.34%)</td><td>239.40 (-4.16%)</td><td>108.70 <b>(-26.65%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.70 (n/a)</td><td>369.26 (n/a)</td><td>280.30 (n/a)</td><td>249.80 (n/a)</td><td>148.19 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (+0.40%)</td><td>0.04 (-2.34%)</td><td>0.05 (-1.39%)</td><td>0.02 <b>(-25.83%)</b></td><td>0.01 (+10.47%)</td><td>594.50 <b>(+34.81%)</b></td><td>343.30 (+6.90%)</td><td>269.60 (+1.39%)</td><td>228.90 (-0.39%)</td><td>153.70 <b>(+42.83%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>441.00 (n/a)</td><td>321.14 (n/a)</td><td>265.90 (n/a)</td><td>229.80 (n/a)</td><td>107.61 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (-12.41%)</td><td>0.04 (+18.79%)</td><td>0.05 <b>(+79.61%)</b></td><td>0.00 (-4.61%)</td><td>0.02 (+2.58%)</td><td>2508.10 (+4.84%)</td><td>737.80 (-5.37%)</td><td>239.00 <b>(-44.32%)</b></td><td>236.60 (+14.13%)</td><td>994.65 (+8.98%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2392.40 (n/a)</td><td>779.68 (n/a)</td><td>429.20 (n/a)</td><td>207.30 (n/a)</td><td>912.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (-6.23%)</td><td>0.03 (+13.52%)</td><td>0.04 <b>(+48.15%)</b></td><td>0.02 (+15.26%)</td><td>0.01 <b>(-22.58%)</b></td><td>598.40 (-13.24%)</td><td>389.40 (-16.64%)</td><td>339.40 <b>(-32.50%)</b></td><td>287.90 (+6.67%)</td><td>130.91 <b>(-27.00%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>689.70 (n/a)</td><td>467.14 (n/a)</td><td>502.80 (n/a)</td><td>269.90 (n/a)</td><td>179.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (+15.46%)</td><td>0.04 <b>(+44.53%)</b></td><td>0.04 <b>(+64.30%)</b></td><td>0.03 <b>(+330.08%)</b></td><td>0.01 <b>(-33.45%)</b></td><td>478.00 <b>(-76.75%)</b></td><td>347.74 <b>(-54.65%)</b></td><td>343.80 <b>(-39.13%)</b></td><td>240.60 (-13.39%)</td><td>93.57 <b>(-87.26%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2055.90 (n/a)</td><td>766.78 (n/a)</td><td>564.80 (n/a)</td><td>277.80 (n/a)</td><td>734.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (-3.46%)</td><td>0.04 <b>(+67.34%)</b></td><td>0.04 <b>(+89.65%)</b></td><td>0.03 <b>(+357.40%)</b></td><td>0.01 <b>(-42.38%)</b></td><td>421.90 <b>(-78.14%)</b></td><td>309.28 <b>(-60.31%)</b></td><td>290.70 <b>(-47.27%)</b></td><td>238.00 (+3.61%)</td><td>79.58 <b>(-88.03%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1929.70 (n/a)</td><td>779.18 (n/a)</td><td>551.30 (n/a)</td><td>229.70 (n/a)</td><td>664.71 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 <b>(+36.50%)</b></td><td>0.07 (+14.55%)</td><td>0.05 (-10.62%)</td><td>0.04 (-3.60%)</td><td>0.04 <b>(+72.71%)</b></td><td>579.60 (+3.74%)</td><td>410.04 (-2.96%)</td><td>516.80 (+11.89%)</td><td>201.00 <b>(-26.75%)</b></td><td>177.55 <b>(+33.77%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.70 (n/a)</td><td>422.54 (n/a)</td><td>461.90 (n/a)</td><td>274.40 (n/a)</td><td>132.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.11 <b>(+53.46%)</b></td><td>0.08 <b>(+68.39%)</b></td><td>0.08 <b>(+64.92%)</b></td><td>0.07 <b>(+91.80%)</b></td><td>0.02 <b>(+32.01%)</b></td><td>360.40 <b>(-47.86%)</b></td><td>302.20 <b>(-41.67%)</b></td><td>319.60 <b>(-39.37%)</b></td><td>232.30 <b>(-34.84%)</b></td><td>55.57 <b>(-54.60%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>691.20 (n/a)</td><td>518.06 (n/a)</td><td>527.10 (n/a)</td><td>356.50 (n/a)</td><td>122.38 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 <b>(+57.66%)</b></td><td>0.07 (+13.20%)</td><td>0.05 (-11.44%)</td><td>0.05 (+12.14%)</td><td>0.04 <b>(+123.35%)</b></td><td>528.10 (-10.84%)</td><td>408.30 (-2.40%)</td><td>457.40 (+12.91%)</td><td>175.50 <b>(-36.60%)</b></td><td>141.82 <b>(+20.90%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>592.30 (n/a)</td><td>418.34 (n/a)</td><td>405.10 (n/a)</td><td>276.80 (n/a)</td><td>117.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 <b>(+33.79%)</b></td><td>0.06 <b>(+26.27%)</b></td><td>0.06 (+14.77%)</td><td>0.05 (+5.68%)</td><td>0.02 <b>(+145.60%)</b></td><td>536.00 (-5.38%)</td><td>417.02 (-15.98%)</td><td>442.60 (-12.87%)</td><td>286.50 <b>(-25.27%)</b></td><td>124.21 <b>(+72.11%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>566.50 (n/a)</td><td>496.34 (n/a)</td><td>508.00 (n/a)</td><td>383.40 (n/a)</td><td>72.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (+4.13%)</td><td>0.07 <b>(+25.12%)</b></td><td>0.06 <b>(+36.58%)</b></td><td>0.05 <b>(+31.87%)</b></td><td>0.02 (-2.37%)</td><td>523.60 <b>(-24.16%)</b></td><td>381.94 <b>(-23.47%)</b></td><td>379.90 <b>(-26.79%)</b></td><td>257.20 (-3.99%)</td><td>124.69 <b>(-33.30%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>690.40 (n/a)</td><td>499.06 (n/a)</td><td>518.90 (n/a)</td><td>267.90 (n/a)</td><td>186.94 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 <b>(-37.24%)</b></td><td>0.04 <b>(-30.04%)</b></td><td>0.04 (+2.98%)</td><td>0.01 <b>(-73.19%)</b></td><td>0.02 <b>(-20.92%)</b></td><td>2439.10 <b>(+272.95%)</b></td><td>923.36 <b>(+86.16%)</b></td><td>548.30 (-2.90%)</td><td>464.50 <b>(+59.29%)</b></td><td>849.55 <b>(+412.18%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>654.00 (n/a)</td><td>496.00 (n/a)</td><td>564.70 (n/a)</td><td>291.60 (n/a)</td><td>165.87 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.28 <b>(+40.86%)</b></td><td>0.15 (+19.94%)</td><td>0.14 <b>(+32.43%)</b></td><td>0.08 (-8.83%)</td><td>0.08 <b>(+81.87%)</b></td><td>579.60 (+9.67%)</td><td>387.70 (-6.93%)</td><td>353.40 <b>(-24.49%)</b></td><td>173.10 <b>(-29.03%)</b></td><td>167.64 <b>(+48.88%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>528.50 (n/a)</td><td>416.56 (n/a)</td><td>468.00 (n/a)</td><td>243.90 (n/a)</td><td>112.60 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.19 (-4.60%)</td><td>0.14 (-19.16%)</td><td>0.16 (-5.27%)</td><td>0.08 <b>(-48.99%)</b></td><td>0.05 <b>(+261.76%)</b></td><td>601.80 <b>(+96.03%)</b></td><td>394.28 <b>(+40.74%)</b></td><td>302.50 (+5.58%)</td><td>259.20 (+4.81%)</td><td>167.16 <b>(+641.91%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>307.00 (n/a)</td><td>280.14 (n/a)</td><td>286.50 (n/a)</td><td>247.30 (n/a)</td><td>22.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.21 <b>(+29.60%)</b></td><td>0.17 <b>(+72.22%)</b></td><td>0.18 <b>(+103.99%)</b></td><td>0.10 <b>(+115.62%)</b></td><td>0.04 (+1.73%)</td><td>501.90 <b>(-53.62%)</b></td><td>313.04 <b>(-47.68%)</b></td><td>278.80 <b>(-50.98%)</b></td><td>237.60 <b>(-22.86%)</b></td><td>109.47 <b>(-63.41%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>1082.20 (n/a)</td><td>598.30 (n/a)</td><td>568.70 (n/a)</td><td>308.00 (n/a)</td><td>299.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.16 (-4.80%)</td><td>0.11 <b>(+33.66%)</b></td><td>0.10 (+16.09%)</td><td>0.09 <b>(+256.32%)</b></td><td>0.03 <b>(-51.02%)</b></td><td>555.30 <b>(-71.93%)</b></td><td>470.24 <b>(-55.13%)</b></td><td>476.70 (-13.86%)</td><td>307.40 (+5.02%)</td><td>100.42 <b>(-87.98%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1978.60 (n/a)</td><td>1048.10 (n/a)</td><td>553.40 (n/a)</td><td>292.70 (n/a)</td><td>835.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.20 (+9.73%)</td><td>0.14 <b>(+21.71%)</b></td><td>0.13 <b>(+24.26%)</b></td><td>0.09 (+12.44%)</td><td>0.05 (+17.10%)</td><td>529.00 (-11.05%)</td><td>392.56 (-16.64%)</td><td>375.30 (-19.52%)</td><td>250.10 (-8.86%)</td><td>127.05 (+2.28%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>594.70 (n/a)</td><td>470.90 (n/a)</td><td>466.30 (n/a)</td><td>274.40 (n/a)</td><td>124.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.19 (+6.26%)</td><td>0.14 (+17.50%)</td><td>0.17 <b>(+80.44%)</b></td><td>0.08 (-7.59%)</td><td>0.06 <b>(+22.91%)</b></td><td>615.30 (+8.21%)</td><td>397.24 (-10.68%)</td><td>292.40 <b>(-44.57%)</b></td><td>254.70 (-5.88%)</td><td>178.64 <b>(+22.84%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>568.60 (n/a)</td><td>444.74 (n/a)</td><td>527.50 (n/a)</td><td>270.60 (n/a)</td><td>145.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (-8.29%)</td><td>0.01 <b>(+25.85%)</b></td><td>0.01 <b>(+63.06%)</b></td><td>0.00 (-10.25%)</td><td>0.00 (-4.54%)</td><td>651.50 (+11.42%)</td><td>347.64 (-18.29%)</td><td>277.30 <b>(-38.68%)</b></td><td>250.10 (+9.02%)</td><td>170.37 <b>(+32.45%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>584.70 (n/a)</td><td>425.48 (n/a)</td><td>452.20 (n/a)</td><td>229.40 (n/a)</td><td>128.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (-5.24%)</td><td>0.00 <b>(-39.26%)</b></td><td>0.00 <b>(-50.10%)</b></td><td>0.00 <b>(-70.08%)</b></td><td>0.00 <b>(+20.30%)</b></td><td>2075.80 <b>(+234.21%)</b></td><td>862.12 <b>(+133.02%)</b></td><td>658.10 <b>(+100.40%)</b></td><td>237.50 (+5.56%)</td><td>713.69 <b>(+341.49%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>621.10 (n/a)</td><td>369.98 (n/a)</td><td>328.40 (n/a)</td><td>225.00 (n/a)</td><td>161.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (+6.88%)</td><td>0.01 (-5.26%)</td><td>0.01 <b>(-32.36%)</b></td><td>0.00 (+2.40%)</td><td>0.00 (+13.83%)</td><td>540.40 (-2.33%)</td><td>414.66 (+7.34%)</td><td>476.90 <b>(+47.83%)</b></td><td>224.40 (-6.42%)</td><td>146.79 (+2.17%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>553.30 (n/a)</td><td>386.30 (n/a)</td><td>322.60 (n/a)</td><td>239.80 (n/a)</td><td>143.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 <b>(-30.31%)</b></td><td>0.01 (-19.82%)</td><td>0.01 <b>(-24.46%)</b></td><td>0.01 <b>(+119.63%)</b></td><td>0.00 <b>(-66.55%)</b></td><td>475.50 <b>(-54.47%)</b></td><td>395.62 (-6.28%)</td><td>363.40 <b>(+32.39%)</b></td><td>318.10 <b>(+43.48%)</b></td><td>70.56 <b>(-79.79%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1044.30 (n/a)</td><td>422.14 (n/a)</td><td>274.50 (n/a)</td><td>221.70 (n/a)</td><td>349.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (-3.41%)</td><td>0.01 (+9.38%)</td><td>0.01 (+12.18%)</td><td>0.00 (+12.29%)</td><td>0.00 (-1.70%)</td><td>545.50 (-10.94%)</td><td>414.30 (-9.68%)</td><td>435.00 (-10.86%)</td><td>276.70 (+3.56%)</td><td>129.86 (-12.42%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>612.50 (n/a)</td><td>458.70 (n/a)</td><td>488.00 (n/a)</td><td>267.20 (n/a)</td><td>148.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 <b>(-21.77%)</b></td><td>0.01 (-4.96%)</td><td>0.01 (+3.51%)</td><td>0.00 (+16.63%)</td><td>0.00 <b>(-40.49%)</b></td><td>585.40 (-14.25%)</td><td>479.64 (-1.22%)</td><td>477.10 (-3.40%)</td><td>313.50 <b>(+27.80%)</b></td><td>112.54 <b>(-28.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>682.70 (n/a)</td><td>485.56 (n/a)</td><td>493.90 (n/a)</td><td>245.30 (n/a)</td><td>157.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+2.26%)</td><td>0.02 <b>(+40.22%)</b></td><td>0.02 <b>(+47.91%)</b></td><td>0.02 <b>(+90.70%)</b></td><td>0.00 <b>(-60.84%)</b></td><td>332.20 <b>(-47.56%)</b></td><td>287.62 <b>(-33.06%)</b></td><td>275.80 <b>(-32.39%)</b></td><td>270.40 (-2.21%)</td><td>25.82 <b>(-79.96%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.50 (n/a)</td><td>429.68 (n/a)</td><td>407.90 (n/a)</td><td>276.50 (n/a)</td><td>128.84 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+3.21%)</td><td>0.02 (-5.17%)</td><td>0.02 (-5.78%)</td><td>0.01 (+10.85%)</td><td>0.01 (+13.73%)</td><td>538.40 (-9.80%)</td><td>381.24 (+7.07%)</td><td>312.40 (+6.15%)</td><td>237.40 (-3.10%)</td><td>142.47 (+1.59%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.90 (n/a)</td><td>356.08 (n/a)</td><td>294.30 (n/a)</td><td>245.00 (n/a)</td><td>140.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-11.60%)</td><td>0.02 (+18.52%)</td><td>0.02 <b>(+72.58%)</b></td><td>0.01 <b>(+27.48%)</b></td><td>0.00 <b>(-45.36%)</b></td><td>519.00 <b>(-21.57%)</b></td><td>316.90 <b>(-28.04%)</b></td><td>268.50 <b>(-42.07%)</b></td><td>244.40 (+13.15%)</td><td>113.97 <b>(-47.05%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.70 (n/a)</td><td>440.36 (n/a)</td><td>463.50 (n/a)</td><td>216.00 (n/a)</td><td>215.26 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(+53.24%)</b></td><td>0.02 <b>(+74.20%)</b></td><td>0.02 <b>(+61.20%)</b></td><td>0.01 <b>(+273.24%)</b></td><td>0.01 (+15.44%)</td><td>541.70 <b>(-73.21%)</b></td><td>324.18 <b>(-57.21%)</b></td><td>294.80 <b>(-37.98%)</b></td><td>219.50 <b>(-34.73%)</b></td><td>127.98 <b>(-81.96%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2021.80 (n/a)</td><td>757.66 (n/a)</td><td>475.30 (n/a)</td><td>336.30 (n/a)</td><td>709.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-5.19%)</td><td>0.01 <b>(-20.13%)</b></td><td>0.01 (-6.53%)</td><td>0.00 <b>(-69.68%)</b></td><td>0.01 <b>(+30.62%)</b></td><td>1928.30 <b>(+229.74%)</b></td><td>751.50 <b>(+75.12%)</b></td><td>470.80 (+6.98%)</td><td>293.70 (+5.46%)</td><td>674.12 <b>(+394.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>584.80 (n/a)</td><td>429.14 (n/a)</td><td>440.10 (n/a)</td><td>278.50 (n/a)</td><td>136.24 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 <b>(-26.46%)</b></td><td>0.01 (-11.60%)</td><td>0.01 (-0.69%)</td><td>0.01 (-16.85%)</td><td>0.00 <b>(-45.86%)</b></td><td>615.50 <b>(+20.29%)</b></td><td>496.86 (+11.37%)</td><td>479.90 (+0.69%)</td><td>422.00 <b>(+36.00%)</b></td><td>73.84 (-6.49%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.70 (n/a)</td><td>446.14 (n/a)</td><td>476.60 (n/a)</td><td>310.30 (n/a)</td><td>78.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 <b>(-20.52%)</b></td><td>0.03 <b>(-25.94%)</b></td><td>0.02 <b>(-35.58%)</b></td><td>0.02 (-16.95%)</td><td>0.01 (-14.26%)</td><td>520.30 <b>(+20.41%)</b></td><td>392.04 <b>(+36.18%)</b></td><td>435.50 <b>(+55.20%)</b></td><td>263.00 <b>(+25.84%)</b></td><td>117.38 <b>(+28.61%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>432.10 (n/a)</td><td>287.88 (n/a)</td><td>280.60 (n/a)</td><td>209.00 (n/a)</td><td>91.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (-7.36%)</td><td>0.03 (-13.71%)</td><td>0.03 (-3.46%)</td><td>0.02 (-19.59%)</td><td>0.01 (+19.73%)</td><td>528.90 <b>(+24.39%)</b></td><td>364.56 <b>(+20.08%)</b></td><td>303.30 (+3.59%)</td><td>249.30 (+7.92%)</td><td>116.39 <b>(+58.75%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.20 (n/a)</td><td>303.60 (n/a)</td><td>292.80 (n/a)</td><td>231.00 (n/a)</td><td>73.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 <b>(-22.92%)</b></td><td>0.03 (-16.66%)</td><td>0.03 (-19.71%)</td><td>0.02 (-5.24%)</td><td>0.01 <b>(-36.16%)</b></td><td>523.70 (+5.52%)</td><td>370.44 (+14.42%)</td><td>300.60 <b>(+24.52%)</b></td><td>286.80 <b>(+29.77%)</b></td><td>108.07 (-14.04%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.30 (n/a)</td><td>323.76 (n/a)</td><td>241.40 (n/a)</td><td>221.00 (n/a)</td><td>125.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 <b>(-22.57%)</b></td><td>0.02 (-14.63%)</td><td>0.03 (+0.30%)</td><td>0.00 <b>(-74.44%)</b></td><td>0.01 <b>(+23.49%)</b></td><td>2442.00 <b>(+291.28%)</b></td><td>794.86 <b>(+90.81%)</b></td><td>388.50 (-0.31%)</td><td>316.40 <b>(+29.14%)</b></td><td>924.17 <b>(+557.77%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.10 (n/a)</td><td>416.58 (n/a)</td><td>389.70 (n/a)</td><td>245.00 (n/a)</td><td>140.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (+1.96%)</td><td>0.03 (+4.23%)</td><td>0.02 (+5.00%)</td><td>0.02 (-0.70%)</td><td>0.01 (+0.91%)</td><td>584.00 (+0.69%)</td><td>465.56 (-4.11%)</td><td>512.10 (-4.76%)</td><td>233.40 (-1.89%)</td><td>140.86 (+0.05%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.00 (n/a)</td><td>485.50 (n/a)</td><td>537.70 (n/a)</td><td>237.90 (n/a)</td><td>140.80 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (+0.99%)</td><td>0.02 (+18.09%)</td><td>0.02 (-4.56%)</td><td>0.02 <b>(+248.11%)</b></td><td>0.01 <b>(-35.73%)</b></td><td>560.00 <b>(-71.27%)</b></td><td>462.26 <b>(-38.39%)</b></td><td>508.10 (+4.78%)</td><td>346.50 (-1.00%)</td><td>105.07 <b>(-84.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1949.40 (n/a)</td><td>750.34 (n/a)</td><td>484.90 (n/a)</td><td>350.00 (n/a)</td><td>673.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (-16.07%)</td><td>0.06 (-2.15%)</td><td>0.05 (-10.21%)</td><td>0.04 <b>(+32.58%)</b></td><td>0.02 (-18.59%)</td><td>510.30 <b>(-24.57%)</b></td><td>392.50 (-2.68%)</td><td>445.20 (+11.38%)</td><td>246.50 (+19.20%)</td><td>126.41 <b>(-26.91%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>676.50 (n/a)</td><td>403.30 (n/a)</td><td>399.70 (n/a)</td><td>206.80 (n/a)</td><td>172.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (+9.08%)</td><td>0.05 (+1.40%)</td><td>0.05 (+17.61%)</td><td>0.01 <b>(-71.23%)</b></td><td>0.03 <b>(+84.19%)</b></td><td>1993.10 <b>(+247.59%)</b></td><td>704.38 <b>(+54.16%)</b></td><td>415.50 (-14.98%)</td><td>264.30 (-8.32%)</td><td>728.06 <b>(+554.99%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>573.40 (n/a)</td><td>456.92 (n/a)</td><td>488.70 (n/a)</td><td>288.30 (n/a)</td><td>111.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (-16.55%)</td><td>0.05 (-15.10%)</td><td>0.04 (-4.30%)</td><td>0.03 (-5.26%)</td><td>0.02 <b>(-29.27%)</b></td><td>606.00 (+5.56%)</td><td>467.36 (+13.16%)</td><td>491.50 (+4.51%)</td><td>282.70 (+19.84%)</td><td>121.04 (-12.95%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.10 (n/a)</td><td>413.02 (n/a)</td><td>470.30 (n/a)</td><td>235.90 (n/a)</td><td>139.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 <b>(-38.36%)</b></td><td>0.04 <b>(-24.65%)</b></td><td>0.04 (-8.30%)</td><td>0.01 <b>(-47.29%)</b></td><td>0.02 <b>(-38.37%)</b></td><td>1951.90 <b>(+89.73%)</b></td><td>758.40 <b>(+44.44%)</b></td><td>475.70 (+9.06%)</td><td>407.80 <b>(+62.21%)</b></td><td>667.87 <b>(+111.66%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1028.80 (n/a)</td><td>525.08 (n/a)</td><td>436.20 (n/a)</td><td>251.40 (n/a)</td><td>315.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (-15.87%)</td><td>0.05 (-8.17%)</td><td>0.05 (-5.21%)</td><td>0.04 (+0.36%)</td><td>0.01 <b>(-51.20%)</b></td><td>493.30 (-0.36%)</td><td>415.34 (+5.35%)</td><td>425.10 (+5.51%)</td><td>349.50 (+18.88%)</td><td>54.30 <b>(-41.58%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>495.10 (n/a)</td><td>394.26 (n/a)</td><td>402.90 (n/a)</td><td>294.00 (n/a)</td><td>92.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (-10.28%)</td><td>0.04 <b>(+24.81%)</b></td><td>0.04 <b>(+20.31%)</b></td><td>0.04 <b>(+238.14%)</b></td><td>0.01 <b>(-63.65%)</b></td><td>567.40 <b>(-70.43%)</b></td><td>485.10 <b>(-40.05%)</b></td><td>471.70 (-16.88%)</td><td>408.50 (+11.46%)</td><td>66.93 <b>(-89.35%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1918.80 (n/a)</td><td>809.14 (n/a)</td><td>567.50 (n/a)</td><td>366.50 (n/a)</td><td>628.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.50 (n/a)</td><td>406.12 (n/a)</td><td>357.40 (n/a)</td><td>282.00 (n/a)</td><td>138.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.20 (n/a)</td><td>427.74 (n/a)</td><td>466.10 (n/a)</td><td>245.30 (n/a)</td><td>164.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.30 (n/a)</td><td>430.78 (n/a)</td><td>415.90 (n/a)</td><td>309.90 (n/a)</td><td>126.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.40 (n/a)</td><td>451.36 (n/a)</td><td>555.30 (n/a)</td><td>269.50 (n/a)</td><td>164.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>429.70 (n/a)</td><td>300.60 (n/a)</td><td>269.20 (n/a)</td><td>261.40 (n/a)</td><td>72.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.00 (n/a)</td><td>503.58 (n/a)</td><td>538.30 (n/a)</td><td>349.50 (n/a)</td><td>109.79 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>544.90 (n/a)</td><td>335.94 (n/a)</td><td>312.70 (n/a)</td><td>249.60 (n/a)</td><td>120.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>491.00 (n/a)</td><td>402.90 (n/a)</td><td>407.60 (n/a)</td><td>269.70 (n/a)</td><td>84.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>570.20 (n/a)</td><td>391.70 (n/a)</td><td>374.70 (n/a)</td><td>278.10 (n/a)</td><td>113.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.21 <b>(+26.03%)</b></td><td>0.17 <b>(+30.35%)</b></td><td>0.17 <b>(+47.94%)</b></td><td>0.11 (+19.17%)</td><td>0.03 (+1.85%)</td><td>434.70 (-16.08%)</td><td>308.32 <b>(-24.32%)</b></td><td>295.40 <b>(-32.42%)</b></td><td>237.80 <b>(-20.65%)</b></td><td>75.00 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>518.00 (n/a)</td><td>407.42 (n/a)</td><td>437.10 (n/a)</td><td>299.70 (n/a)</td><td>101.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>572.60 (n/a)</td><td>394.64 (n/a)</td><td>373.10 (n/a)</td><td>247.30 (n/a)</td><td>120.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>566.50 (n/a)</td><td>412.34 (n/a)</td><td>468.50 (n/a)</td><td>223.00 (n/a)</td><td>139.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>540.30 (n/a)</td><td>326.58 (n/a)</td><td>269.20 (n/a)</td><td>237.50 (n/a)</td><td>127.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.10 (n/a)</td><td>460.80 (n/a)</td><td>446.10 (n/a)</td><td>268.70 (n/a)</td><td>135.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.10 (n/a)</td><td>408.16 (n/a)</td><td>340.80 (n/a)</td><td>280.40 (n/a)</td><td>158.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>450.50 (n/a)</td><td>332.32 (n/a)</td><td>335.30 (n/a)</td><td>261.40 (n/a)</td><td>77.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.30 (n/a)</td><td>362.24 (n/a)</td><td>332.10 (n/a)</td><td>222.60 (n/a)</td><td>124.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2391.20 (n/a)</td><td>771.42 (n/a)</td><td>353.30 (n/a)</td><td>316.50 (n/a)</td><td>907.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>411.00 (n/a)</td><td>307.90 (n/a)</td><td>300.10 (n/a)</td><td>258.00 (n/a)</td><td>60.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>580.90 (n/a)</td><td>410.86 (n/a)</td><td>436.60 (n/a)</td><td>247.40 (n/a)</td><td>123.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>560.50 (n/a)</td><td>447.86 (n/a)</td><td>443.40 (n/a)</td><td>299.20 (n/a)</td><td>111.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>483.60 (n/a)</td><td>313.94 (n/a)</td><td>260.70 (n/a)</td><td>245.50 (n/a)</td><td>100.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>406.40 (n/a)</td><td>326.94 (n/a)</td><td>295.10 (n/a)</td><td>237.70 (n/a)</td><td>74.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>422.70 (n/a)</td><td>305.50 (n/a)</td><td>299.30 (n/a)</td><td>235.60 (n/a)</td><td>71.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>330.40 (n/a)</td><td>268.52 (n/a)</td><td>248.20 (n/a)</td><td>239.30 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>404.80 (n/a)</td><td>311.88 (n/a)</td><td>276.60 (n/a)</td><td>238.90 (n/a)</td><td>80.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1942.10 (n/a)</td><td>635.70 (n/a)</td><td>231.40 (n/a)</td><td>169.90 (n/a)</td><td>755.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.50 (n/a)</td><td>355.46 (n/a)</td><td>297.00 (n/a)</td><td>244.20 (n/a)</td><td>121.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2017.50 (n/a)</td><td>793.42 (n/a)</td><td>494.30 (n/a)</td><td>365.60 (n/a)</td><td>691.84 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.20 (n/a)</td><td>340.68 (n/a)</td><td>281.40 (n/a)</td><td>228.40 (n/a)</td><td>123.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.90 (n/a)</td><td>458.90 (n/a)</td><td>419.10 (n/a)</td><td>291.30 (n/a)</td><td>152.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.80 (n/a)</td><td>345.40 (n/a)</td><td>279.30 (n/a)</td><td>235.20 (n/a)</td><td>117.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1067.00 (n/a)</td><td>585.72 (n/a)</td><td>520.10 (n/a)</td><td>352.30 (n/a)</td><td>278.47 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2455.20 (n/a)</td><td>833.46 (n/a)</td><td>511.90 (n/a)</td><td>334.10 (n/a)</td><td>910.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.30 (n/a)</td><td>490.68 (n/a)</td><td>491.00 (n/a)</td><td>312.60 (n/a)</td><td>129.93 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>693.10 (n/a)</td><td>487.02 (n/a)</td><td>553.20 (n/a)</td><td>245.30 (n/a)</td><td>202.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>754.70 (n/a)</td><td>468.78 (n/a)</td><td>404.50 (n/a)</td><td>296.40 (n/a)</td><td>187.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1965.40 (n/a)</td><td>659.62 (n/a)</td><td>411.00 (n/a)</td><td>219.20 (n/a)</td><td>737.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>565.30 (n/a)</td><td>364.42 (n/a)</td><td>294.10 (n/a)</td><td>241.70 (n/a)</td><td>139.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1052.30 (n/a)</td><td>539.14 (n/a)</td><td>562.70 (n/a)</td><td>244.50 (n/a)</td><td>328.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>606.40 (n/a)</td><td>500.30 (n/a)</td><td>542.10 (n/a)</td><td>354.40 (n/a)</td><td>104.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>793.40 (n/a)</td><td>542.76 (n/a)</td><td>537.20 (n/a)</td><td>243.70 (n/a)</td><td>197.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>666.20 (n/a)</td><td>405.02 (n/a)</td><td>288.80 (n/a)</td><td>259.20 (n/a)</td><td>186.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1814.70 (n/a)</td><td>773.24 (n/a)</td><td>539.00 (n/a)</td><td>451.30 (n/a)</td><td>583.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>581.10 (n/a)</td><td>341.74 (n/a)</td><td>283.90 (n/a)</td><td>182.20 (n/a)</td><td>157.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>658.00 (n/a)</td><td>479.48 (n/a)</td><td>485.60 (n/a)</td><td>301.40 (n/a)</td><td>154.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.55 <b>(+36.35%)</b></td><td>0.42 <b>(+34.30%)</b></td><td>0.35 (+1.11%)</td><td>0.33 <b>(+178.81%)</b></td><td>0.11 (-6.25%)</td><td>672.20 <b>(-64.13%)</b></td><td>552.32 <b>(-36.36%)</b></td><td>630.10 (-1.10%)</td><td>405.40 <b>(-26.66%)</b></td><td>128.41 <b>(-77.28%)</b></td><td>23.28 <b>(+36.35%)</b></td><td>17.93 <b>(+34.30%)</b></td><td>14.98 (+1.11%)</td><td>14.04 <b>(+178.81%)</b></td><td>4.53 (-6.25%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>1874.20 (n/a)</td><td>867.88 (n/a)</td><td>637.10 (n/a)</td><td>552.80 (n/a)</td><td>565.10 (n/a)</td><td>17.07 (n/a)</td><td>13.35 (n/a)</td><td>14.81 (n/a)</td><td>5.04 (n/a)</td><td>4.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.54 (-3.93%)</td><td>0.42 (-6.19%)</td><td>0.47 (+11.80%)</td><td>0.21 <b>(-37.50%)</b></td><td>0.14 <b>(+63.64%)</b></td><td>1044.30 <b>(+60.02%)</b></td><td>599.76 (+17.13%)</td><td>471.20 (-10.55%)</td><td>410.30 (+4.08%)</td><td>267.57 <b>(+170.11%)</b></td><td>23.00 (-3.93%)</td><td>17.81 (-6.19%)</td><td>20.03 (+11.80%)</td><td>9.04 <b>(-37.50%)</b></td><td>5.99 <b>(+63.64%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>652.60 (n/a)</td><td>512.04 (n/a)</td><td>526.80 (n/a)</td><td>394.20 (n/a)</td><td>99.06 (n/a)</td><td>23.94 (n/a)</td><td>18.99 (n/a)</td><td>17.91 (n/a)</td><td>14.46 (n/a)</td><td>3.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 (-0.84%)</td><td>0.31 (-1.22%)</td><td>0.31 (-1.59%)</td><td>0.30 (-2.35%)</td><td>0.01 <b>(+47.95%)</b></td><td>85030.00 (+2.41%)</td><td>82527.08 (+1.25%)</td><td>82365.30 (+1.62%)</td><td>81139.30 (+0.85%)</td><td>1575.03 <b>(+52.68%)</b></td><td>211.73 (-0.84%)</td><td>208.23 (-1.22%)</td><td>208.58 (-1.59%)</td><td>202.04 (-2.35%)</td><td>3.92 <b>(+47.95%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83028.50 (n/a)</td><td>81508.32 (n/a)</td><td>81053.40 (n/a)</td><td>80455.60 (n/a)</td><td>1031.61 (n/a)</td><td>213.53 (n/a)</td><td>210.80 (n/a)</td><td>211.96 (n/a)</td><td>206.92 (n/a)</td><td>2.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>1.05 (+2.44%)</td><td>1.00 (-1.56%)</td><td>1.00 (-1.46%)</td><td>0.96 (-4.05%)</td><td>0.04 <b>(+280.38%)</b></td><td>26176.90 (+4.22%)</td><td>25214.48 (+1.67%)</td><td>25100.50 (+1.48%)</td><td>23958.70 (-2.38%)</td><td>876.37 <b>(+287.36%)</b></td><td>717.06 (+2.44%)</td><td>682.02 (-1.56%)</td><td>684.44 (-1.46%)</td><td>656.30 (-4.05%)</td><td>23.98 <b>(+280.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25115.90 (n/a)</td><td>24799.58 (n/a)</td><td>24733.60 (n/a)</td><td>24542.80 (n/a)</td><td>226.24 (n/a)</td><td>700.00 (n/a)</td><td>692.79 (n/a)</td><td>694.60 (n/a)</td><td>684.02 (n/a)</td><td>6.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.82 (-0.35%)</td><td>0.81 (+0.39%)</td><td>0.81 (+1.13%)</td><td>0.79 (+0.25%)</td><td>0.01 (+1.75%)</td><td>95366.60 (-0.25%)</td><td>93260.06 (-0.39%)</td><td>92735.30 (-1.12%)</td><td>92041.60 (+0.35%)</td><td>1430.93 (+1.71%)</td><td>746.61 (-0.35%)</td><td>737.00 (+0.39%)</td><td>741.03 (+1.13%)</td><td>720.58 (+0.25%)</td><td>11.22 (+1.75%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95601.40 (n/a)</td><td>93622.86 (n/a)</td><td>93786.30 (n/a)</td><td>91722.80 (n/a)</td><td>1406.83 (n/a)</td><td>749.21 (n/a)</td><td>734.14 (n/a)</td><td>732.72 (n/a)</td><td>718.81 (n/a)</td><td>11.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.77 (+0.10%)</td><td>0.76 (-0.46%)</td><td>0.77 (+0.83%)</td><td>0.72 (-4.02%)</td><td>0.02 <b>(+182.26%)</b></td><td>104255.10 (+4.19%)</td><td>99339.70 (+0.52%)</td><td>98145.70 (-0.82%)</td><td>97568.40 (-0.10%)</td><td>2779.77 <b>(+195.01%)</b></td><td>704.32 (+0.10%)</td><td>692.18 (-0.46%)</td><td>700.18 (+0.83%)</td><td>659.15 (-4.02%)</td><td>18.71 <b>(+182.26%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100062.50 (n/a)</td><td>98828.46 (n/a)</td><td>98957.70 (n/a)</td><td>97670.10 (n/a)</td><td>942.27 (n/a)</td><td>703.59 (n/a)</td><td>695.39 (n/a)</td><td>694.43 (n/a)</td><td>686.77 (n/a)</td><td>6.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.80 (-0.24%)</td><td>0.79 (-0.36%)</td><td>0.79 (-0.54%)</td><td>0.78 (+0.31%)</td><td>0.01 (-14.65%)</td><td>96578.80 (-0.31%)</td><td>95686.26 (+0.35%)</td><td>95708.80 (+0.55%)</td><td>94428.90 (+0.24%)</td><td>821.24 (-14.92%)</td><td>727.74 (-0.24%)</td><td>718.22 (-0.36%)</td><td>718.01 (-0.54%)</td><td>711.54 (+0.31%)</td><td>6.19 (-14.65%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96881.50 (n/a)</td><td>95348.24 (n/a)</td><td>95188.00 (n/a)</td><td>94201.20 (n/a)</td><td>965.21 (n/a)</td><td>729.50 (n/a)</td><td>720.78 (n/a)</td><td>721.93 (n/a)</td><td>709.31 (n/a)</td><td>7.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.58 (+7.25%)</td><td>4.73 <b>(+20.89%)</b></td><td>5.35 <b>(+32.20%)</b></td><td>2.05 (-4.96%)</td><td>1.51 <b>(+29.97%)</b></td><td>4345.30 (+5.22%)</td><td>2190.02 (-12.31%)</td><td>1665.20 <b>(-24.36%)</b></td><td>1597.80 (-6.76%)</td><td>1206.22 <b>(+25.52%)</b></td><td>336.01 (+7.25%)</td><td>285.14 <b>(+20.89%)</b></td><td>322.40 <b>(+32.20%)</b></td><td>123.55 (-4.96%)</td><td>91.02 <b>(+29.97%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.20 (n/a)</td><td>3.92 (n/a)</td><td>4.05 (n/a)</td><td>2.16 (n/a)</td><td>1.16 (n/a)</td><td>4129.80 (n/a)</td><td>2497.36 (n/a)</td><td>2201.50 (n/a)</td><td>1713.60 (n/a)</td><td>960.98 (n/a)</td><td>313.29 (n/a)</td><td>235.87 (n/a)</td><td>243.87 (n/a)</td><td>130.00 (n/a)</td><td>70.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.78 (-3.76%)</td><td>3.34 (+0.35%)</td><td>3.18 (+17.22%)</td><td>2.27 (+4.06%)</td><td>0.93 <b>(-28.80%)</b></td><td>3926.60 (-3.90%)</td><td>2830.70 (-5.96%)</td><td>2801.30 (-14.69%)</td><td>1863.70 (+3.90%)</td><td>758.90 <b>(-29.19%)</b></td><td>288.06 (-3.76%)</td><td>201.33 (+0.35%)</td><td>191.65 (+17.22%)</td><td>136.73 (+4.06%)</td><td>56.27 <b>(-28.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>4.97 (n/a)</td><td>3.33 (n/a)</td><td>2.71 (n/a)</td><td>2.18 (n/a)</td><td>1.31 (n/a)</td><td>4086.10 (n/a)</td><td>3010.20 (n/a)</td><td>3283.50 (n/a)</td><td>1793.70 (n/a)</td><td>1071.82 (n/a)</td><td>299.31 (n/a)</td><td>200.63 (n/a)</td><td>163.50 (n/a)</td><td>131.39 (n/a)</td><td>79.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.23 (-19.26%)</td><td>3.66 (-1.48%)</td><td>4.02 (+12.78%)</td><td>2.88 <b>(+31.55%)</b></td><td>0.63 <b>(-42.24%)</b></td><td>3095.10 <b>(-23.99%)</b></td><td>2497.66 (-3.87%)</td><td>2217.10 (-11.33%)</td><td>2107.90 <b>(+23.85%)</b></td><td>463.61 <b>(-47.82%)</b></td><td>254.69 (-19.26%)</td><td>220.62 (-1.48%)</td><td>242.15 (+12.78%)</td><td>173.46 <b>(+31.55%)</b></td><td>38.24 <b>(-42.24%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.24 (n/a)</td><td>3.72 (n/a)</td><td>3.56 (n/a)</td><td>2.19 (n/a)</td><td>1.10 (n/a)</td><td>4071.70 (n/a)</td><td>2598.30 (n/a)</td><td>2500.50 (n/a)</td><td>1702.00 (n/a)</td><td>888.41 (n/a)</td><td>315.44 (n/a)</td><td>223.93 (n/a)</td><td>214.71 (n/a)</td><td>131.85 (n/a)</td><td>66.21 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.76 (-1.01%)</td><td>4.69 (-10.34%)</td><td>4.52 (-16.20%)</td><td>4.18 (-1.89%)</td><td>0.62 (-5.39%)</td><td>8340.50 (+1.93%)</td><td>7527.76 (+11.39%)</td><td>7719.10 (+19.33%)</td><td>6056.80 (+1.02%)</td><td>866.23 (-4.80%)</td><td>354.56 (-1.01%)</td><td>288.75 (-10.34%)</td><td>278.20 (-16.20%)</td><td>257.48 (-1.89%)</td><td>37.90 (-5.39%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.82 (n/a)</td><td>5.23 (n/a)</td><td>5.39 (n/a)</td><td>4.26 (n/a)</td><td>0.65 (n/a)</td><td>8182.80 (n/a)</td><td>6758.10 (n/a)</td><td>6468.60 (n/a)</td><td>5995.50 (n/a)</td><td>909.86 (n/a)</td><td>358.18 (n/a)</td><td>322.06 (n/a)</td><td>331.99 (n/a)</td><td>262.44 (n/a)</td><td>40.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.50 (-10.05%)</td><td>4.89 (-1.04%)</td><td>5.18 (+14.68%)</td><td>3.46 (-16.55%)</td><td>0.82 (-0.72%)</td><td>10088.50 (+19.84%)</td><td>7331.72 (+1.82%)</td><td>6732.10 (-12.80%)</td><td>6342.80 (+11.17%)</td><td>1556.84 <b>(+37.26%)</b></td><td>338.57 (-10.05%)</td><td>301.49 (-1.04%)</td><td>318.99 (+14.68%)</td><td>212.86 (-16.55%)</td><td>50.70 (-0.72%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>6.11 (n/a)</td><td>4.95 (n/a)</td><td>4.52 (n/a)</td><td>4.14 (n/a)</td><td>0.83 (n/a)</td><td>8418.50 (n/a)</td><td>7200.38 (n/a)</td><td>7720.20 (n/a)</td><td>5705.40 (n/a)</td><td>1134.23 (n/a)</td><td>376.40 (n/a)</td><td>304.66 (n/a)</td><td>278.17 (n/a)</td><td>255.09 (n/a)</td><td>51.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.72 (-15.21%)</td><td>5.20 (-12.35%)</td><td>5.05 (-16.80%)</td><td>4.84 (+0.58%)</td><td>0.37 <b>(-47.86%)</b></td><td>7205.70 (-0.58%)</td><td>6727.56 (+13.13%)</td><td>6904.10 <b>(+20.19%)</b></td><td>6090.00 (+17.94%)</td><td>461.78 <b>(-40.58%)</b></td><td>352.63 (-15.21%)</td><td>320.45 (-12.35%)</td><td>311.05 (-16.80%)</td><td>298.03 (+0.58%)</td><td>22.64 <b>(-47.86%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>6.75 (n/a)</td><td>5.94 (n/a)</td><td>6.07 (n/a)</td><td>4.81 (n/a)</td><td>0.70 (n/a)</td><td>7247.60 (n/a)</td><td>5947.00 (n/a)</td><td>5744.20 (n/a)</td><td>5163.70 (n/a)</td><td>777.20 (n/a)</td><td>415.88 (n/a)</td><td>365.62 (n/a)</td><td>373.85 (n/a)</td><td>296.30 (n/a)</td><td>43.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.78 (+1.70%)</td><td>0.77 (+3.17%)</td><td>0.77 (+3.58%)</td><td>0.75 (+3.80%)</td><td>0.01 <b>(-28.32%)</b></td><td>100111.40 (-3.66%)</td><td>98200.78 (-3.10%)</td><td>98010.50 (-3.46%)</td><td>96552.00 (-1.67%)</td><td>1701.87 <b>(-32.32%)</b></td><td>711.74 (+1.70%)</td><td>699.95 (+3.17%)</td><td>701.14 (+3.58%)</td><td>686.43 (+3.80%)</td><td>12.11 <b>(-28.32%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103914.60 (n/a)</td><td>101343.92 (n/a)</td><td>101522.90 (n/a)</td><td>98193.80 (n/a)</td><td>2514.48 (n/a)</td><td>699.84 (n/a)</td><td>678.42 (n/a)</td><td>676.89 (n/a)</td><td>661.31 (n/a)</td><td>16.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.76 (-1.15%)</td><td>0.75 (-1.49%)</td><td>0.75 (-1.25%)</td><td>0.73 (-1.78%)</td><td>0.01 (+10.90%)</td><td>103630.30 (+1.81%)</td><td>100764.74 (+1.51%)</td><td>100347.80 (+1.26%)</td><td>98759.40 (+1.16%)</td><td>1775.70 (+14.30%)</td><td>695.83 (-1.15%)</td><td>682.15 (-1.49%)</td><td>684.81 (-1.25%)</td><td>663.12 (-1.78%)</td><td>11.88 (+10.90%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101784.30 (n/a)</td><td>99262.74 (n/a)</td><td>99096.70 (n/a)</td><td>97623.20 (n/a)</td><td>1553.56 (n/a)</td><td>703.93 (n/a)</td><td>692.43 (n/a)</td><td>693.46 (n/a)</td><td>675.15 (n/a)</td><td>10.71 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.81 (+0.39%)</td><td>0.80 (+1.62%)</td><td>0.80 (+2.23%)</td><td>0.80 (+2.57%)</td><td>0.00 <b>(-55.57%)</b></td><td>94721.10 (-2.51%)</td><td>94018.50 (-1.61%)</td><td>93800.20 (-2.18%)</td><td>93343.90 (-0.39%)</td><td>554.17 <b>(-56.79%)</b></td><td>736.20 (+0.39%)</td><td>730.93 (+1.62%)</td><td>732.62 (+2.23%)</td><td>725.49 (+2.57%)</td><td>4.31 <b>(-55.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97156.90 (n/a)</td><td>95554.02 (n/a)</td><td>95892.30 (n/a)</td><td>93709.20 (n/a)</td><td>1282.46 (n/a)</td><td>733.33 (n/a)</td><td>719.27 (n/a)</td><td>716.63 (n/a)</td><td>707.30 (n/a)</td><td>9.69 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.91 (+13.91%)</td><td>2.32 (-18.20%)</td><td>1.80 <b>(-39.92%)</b></td><td>1.13 <b>(-40.22%)</b></td><td>1.25 <b>(+113.51%)</b></td><td>7131.50 <b>(+67.27%)</b></td><td>4392.18 <b>(+47.98%)</b></td><td>4480.20 <b>(+66.44%)</b></td><td>2060.80 (-12.21%)</td><td>2195.73 <b>(+190.02%)</b></td><td>1025.79 (+13.91%)</td><td>607.92 (-18.20%)</td><td>471.84 <b>(-39.92%)</b></td><td>296.42 <b>(-40.22%)</b></td><td>328.24 <b>(+113.51%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.43 (n/a)</td><td>2.83 (n/a)</td><td>2.99 (n/a)</td><td>1.89 (n/a)</td><td>0.59 (n/a)</td><td>4263.50 (n/a)</td><td>2968.16 (n/a)</td><td>2691.70 (n/a)</td><td>2347.40 (n/a)</td><td>757.09 (n/a)</td><td>900.54 (n/a)</td><td>743.18 (n/a)</td><td>785.36 (n/a)</td><td>495.82 (n/a)</td><td>153.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 (+6.39%)</td><td>0.21 (-1.27%)</td><td>0.19 (-2.19%)</td><td>0.18 (-6.63%)</td><td>0.05 <b>(+26.95%)</b></td><td>6977.10 (+7.10%)</td><td>6040.74 (+2.71%)</td><td>6553.20 (+2.24%)</td><td>4034.70 (-6.00%)</td><td>1166.84 <b>(+23.62%)</b></td><td>16.63 (+6.39%)</td><td>11.55 (-1.27%)</td><td>10.24 (-2.19%)</td><td>9.62 (-6.63%)</td><td>2.89 <b>(+26.95%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>6514.80 (n/a)</td><td>5881.10 (n/a)</td><td>6409.90 (n/a)</td><td>4292.40 (n/a)</td><td>943.86 (n/a)</td><td>15.63 (n/a)</td><td>11.70 (n/a)</td><td>10.47 (n/a)</td><td>10.30 (n/a)</td><td>2.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (+1.14%)</td><td>0.11 (+7.18%)</td><td>0.11 (+7.74%)</td><td>0.09 <b>(+23.81%)</b></td><td>0.02 <b>(-24.76%)</b></td><td>0.13 (+1.14%)</td><td>0.11 (+7.18%)</td><td>0.10 (+7.74%)</td><td>0.09 <b>(+23.81%)</b></td><td>0.02 <b>(-24.76%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.87 (+6.37%)</td><td>3.42 (-4.18%)</td><td>3.40 (-5.62%)</td><td>2.97 (-13.93%)</td><td>0.32 <b>(+290.75%)</b></td><td>3.87 (+6.37%)</td><td>3.41 (-4.18%)</td><td>3.40 (-5.62%)</td><td>2.96 (-13.93%)</td><td>0.32 <b>(+290.76%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.64 (n/a)</td><td>3.56 (n/a)</td><td>3.60 (n/a)</td><td>3.45 (n/a)</td><td>0.08 (n/a)</td><td>3.64 (n/a)</td><td>3.56 (n/a)</td><td>3.60 (n/a)</td><td>3.44 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.98 <b>(-21.41%)</b></td><td>5.84 (-9.82%)</td><td>5.96 (-14.53%)</td><td>5.54 (+12.25%)</td><td>0.19 <b>(-83.19%)</b></td><td>5.97 <b>(-21.41%)</b></td><td>5.83 (-9.82%)</td><td>5.96 (-14.53%)</td><td>5.54 (+12.25%)</td><td>0.19 <b>(-83.19%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.61 (n/a)</td><td>6.47 (n/a)</td><td>6.97 (n/a)</td><td>4.94 (n/a)</td><td>1.15 (n/a)</td><td>7.60 (n/a)</td><td>6.47 (n/a)</td><td>6.97 (n/a)</td><td>4.93 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>14.11 (+0.95%)</td><td>12.08 (+11.65%)</td><td>13.36 <b>(+37.49%)</b></td><td>8.01 (-2.74%)</td><td>2.54 (+2.80%)</td><td>14.10 (+0.95%)</td><td>12.07 (+11.65%)</td><td>13.35 <b>(+37.49%)</b></td><td>8.01 (-2.74%)</td><td>2.54 (+2.80%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>13.97 (n/a)</td><td>10.82 (n/a)</td><td>9.72 (n/a)</td><td>8.24 (n/a)</td><td>2.47 (n/a)</td><td>13.96 (n/a)</td><td>10.81 (n/a)</td><td>9.71 (n/a)</td><td>8.24 (n/a)</td><td>2.47 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.91 (+4.47%)</td><td>3.64 (+1.55%)</td><td>3.66 (+0.81%)</td><td>3.36 (+0.48%)</td><td>0.22 <b>(+38.32%)</b></td><td>3.91 (+4.47%)</td><td>3.64 (+1.55%)</td><td>3.66 (+0.81%)</td><td>3.36 (+0.48%)</td><td>0.22 <b>(+38.32%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.74 (n/a)</td><td>3.58 (n/a)</td><td>3.63 (n/a)</td><td>3.34 (n/a)</td><td>0.16 (n/a)</td><td>3.74 (n/a)</td><td>3.58 (n/a)</td><td>3.63 (n/a)</td><td>3.34 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>7.42 (+0.93%)</td><td>6.32 (+3.14%)</td><td>5.93 (-2.46%)</td><td>5.74 <b>(+21.60%)</b></td><td>0.71 <b>(-32.17%)</b></td><td>7.42 (+0.93%)</td><td>6.31 (+3.14%)</td><td>5.92 (-2.46%)</td><td>5.74 <b>(+21.60%)</b></td><td>0.71 <b>(-32.17%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.35 (n/a)</td><td>6.12 (n/a)</td><td>6.08 (n/a)</td><td>4.72 (n/a)</td><td>1.05 (n/a)</td><td>7.35 (n/a)</td><td>6.12 (n/a)</td><td>6.07 (n/a)</td><td>4.72 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>12.73 (-8.48%)</td><td>9.57 (-6.24%)</td><td>9.70 (-0.18%)</td><td>6.88 (-13.76%)</td><td>2.42 (+9.51%)</td><td>12.73 (-8.48%)</td><td>9.56 (-6.24%)</td><td>9.70 (-0.18%)</td><td>6.87 (-13.76%)</td><td>2.41 (+9.51%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>13.91 (n/a)</td><td>10.21 (n/a)</td><td>9.72 (n/a)</td><td>7.97 (n/a)</td><td>2.21 (n/a)</td><td>13.91 (n/a)</td><td>10.20 (n/a)</td><td>9.71 (n/a)</td><td>7.97 (n/a)</td><td>2.20 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>800.20 (n/a)</td><td>412.00 (n/a)</td><td>318.10 (n/a)</td><td>235.40 (n/a)</td><td>223.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>542.20 (n/a)</td><td>473.38 (n/a)</td><td>498.00 (n/a)</td><td>378.30 (n/a)</td><td>62.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1072.10 (n/a)</td><td>543.68 (n/a)</td><td>448.90 (n/a)</td><td>237.40 (n/a)</td><td>322.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>689.80 (n/a)</td><td>526.68 (n/a)</td><td>555.20 (n/a)</td><td>253.40 (n/a)</td><td>162.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.50 (n/a)</td><td>453.68 (n/a)</td><td>546.80 (n/a)</td><td>231.70 (n/a)</td><td>156.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.20 (n/a)</td><td>461.84 (n/a)</td><td>488.20 (n/a)</td><td>371.10 (n/a)</td><td>79.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>788.60 (n/a)</td><td>425.94 (n/a)</td><td>294.40 (n/a)</td><td>244.90 (n/a)</td><td>228.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.80 (n/a)</td><td>413.64 (n/a)</td><td>425.50 (n/a)</td><td>234.60 (n/a)</td><td>113.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.50 (n/a)</td><td>423.86 (n/a)</td><td>470.10 (n/a)</td><td>230.30 (n/a)</td><td>158.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.20 (n/a)</td><td>369.44 (n/a)</td><td>346.40 (n/a)</td><td>232.50 (n/a)</td><td>146.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.90 (n/a)</td><td>425.08 (n/a)</td><td>474.50 (n/a)</td><td>291.90 (n/a)</td><td>122.77 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>758.70 (n/a)</td><td>568.42 (n/a)</td><td>577.70 (n/a)</td><td>381.40 (n/a)</td><td>136.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>630.90 (n/a)</td><td>413.80 (n/a)</td><td>398.10 (n/a)</td><td>278.60 (n/a)</td><td>143.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>465.60 (n/a)</td><td>362.38 (n/a)</td><td>332.40 (n/a)</td><td>276.90 (n/a)</td><td>85.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.70 (n/a)</td><td>353.70 (n/a)</td><td>346.60 (n/a)</td><td>275.50 (n/a)</td><td>83.13 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.50 (n/a)</td><td>394.10 (n/a)</td><td>299.00 (n/a)</td><td>231.10 (n/a)</td><td>188.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.80 (n/a)</td><td>395.52 (n/a)</td><td>339.40 (n/a)</td><td>226.70 (n/a)</td><td>177.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>479.10 (n/a)</td><td>349.32 (n/a)</td><td>317.90 (n/a)</td><td>297.80 (n/a)</td><td>74.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (-1.16%)</td><td>0.09 (-8.29%)</td><td>0.08 <b>(-28.77%)</b></td><td>0.05 (-13.04%)</td><td>0.04 (+8.39%)</td><td>639.90 (+15.01%)</td><td>427.20 (+12.07%)</td><td>403.50 <b>(+40.40%)</b></td><td>254.10 (+1.19%)</td><td>176.85 (+17.32%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>556.40 (n/a)</td><td>381.18 (n/a)</td><td>287.40 (n/a)</td><td>251.10 (n/a)</td><td>150.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>641.60 (n/a)</td><td>372.28 (n/a)</td><td>284.20 (n/a)</td><td>235.50 (n/a)</td><td>176.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>674.00 (n/a)</td><td>503.70 (n/a)</td><td>524.40 (n/a)</td><td>235.20 (n/a)</td><td>165.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>497.90 (n/a)</td><td>394.46 (n/a)</td><td>403.90 (n/a)</td><td>274.90 (n/a)</td><td>90.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>537.00 (n/a)</td><td>437.80 (n/a)</td><td>487.50 (n/a)</td><td>220.40 (n/a)</td><td>127.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>617.80 (n/a)</td><td>470.32 (n/a)</td><td>446.80 (n/a)</td><td>318.60 (n/a)</td><td>111.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(+27.14%)</b></td><td>0.01 <b>(+21.00%)</b></td><td>0.01 (-1.57%)</td><td>0.01 <b>(+239.75%)</b></td><td>0.00 (-6.77%)</td><td>638.20 <b>(-70.56%)</b></td><td>409.82 <b>(-44.30%)</b></td><td>395.60 (+1.59%)</td><td>247.20 <b>(-21.35%)</b></td><td>158.23 <b>(-80.30%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2168.10 (n/a)</td><td>735.70 (n/a)</td><td>389.40 (n/a)</td><td>314.30 (n/a)</td><td>803.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+7.52%)</td><td>0.01 <b>(+29.12%)</b></td><td>0.01 <b>(+66.07%)</b></td><td>0.01 (-7.07%)</td><td>0.00 (+16.52%)</td><td>558.90 (+7.60%)</td><td>362.96 <b>(-20.49%)</b></td><td>300.80 <b>(-39.78%)</b></td><td>239.60 (-6.99%)</td><td>134.38 <b>(+20.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.40 (n/a)</td><td>456.48 (n/a)</td><td>499.50 (n/a)</td><td>257.60 (n/a)</td><td>111.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(+30.60%)</b></td><td>0.01 (+2.01%)</td><td>0.01 <b>(-26.30%)</b></td><td>0.01 (-8.35%)</td><td>0.01 <b>(+100.35%)</b></td><td>507.90 (+9.11%)</td><td>351.94 (+6.97%)</td><td>402.20 <b>(+35.70%)</b></td><td>195.40 <b>(-23.43%)</b></td><td>131.17 <b>(+58.49%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>465.50 (n/a)</td><td>329.00 (n/a)</td><td>296.40 (n/a)</td><td>255.20 (n/a)</td><td>82.77 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-22.80%)</b></td><td>0.01 <b>(-39.69%)</b></td><td>0.01 <b>(-38.29%)</b></td><td>0.01 <b>(-56.72%)</b></td><td>0.00 (+11.57%)</td><td>803.60 <b>(+131.05%)</b></td><td>455.38 <b>(+85.01%)</b></td><td>380.10 <b>(+62.02%)</b></td><td>236.90 <b>(+29.52%)</b></td><td>213.37 <b>(+236.97%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>347.80 (n/a)</td><td>246.14 (n/a)</td><td>234.60 (n/a)</td><td>182.90 (n/a)</td><td>63.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+1.50%)</td><td>0.01 (+5.11%)</td><td>0.01 <b>(+21.52%)</b></td><td>0.01 (-6.06%)</td><td>0.00 (-3.54%)</td><td>630.50 (+6.45%)</td><td>392.88 (-5.45%)</td><td>324.00 (-17.70%)</td><td>236.30 (-1.46%)</td><td>162.18 (-0.50%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.30 (n/a)</td><td>415.52 (n/a)</td><td>393.70 (n/a)</td><td>239.80 (n/a)</td><td>163.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-1.86%)</td><td>0.01 (+4.81%)</td><td>0.01 (+2.42%)</td><td>0.01 <b>(+20.67%)</b></td><td>0.00 (+6.82%)</td><td>483.70 (-17.12%)</td><td>332.44 (-5.42%)</td><td>292.20 (-2.37%)</td><td>234.90 (+1.91%)</td><td>112.22 (-17.64%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.60 (n/a)</td><td>351.48 (n/a)</td><td>299.30 (n/a)</td><td>230.50 (n/a)</td><td>136.26 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 <b>(-36.68%)</b></td><td>0.01 <b>(-25.30%)</b></td><td>0.01 <b>(-28.48%)</b></td><td>0.01 (+13.94%)</td><td>0.00 <b>(-77.96%)</b></td><td>525.00 (-12.24%)</td><td>467.26 <b>(+23.37%)</b></td><td>441.60 <b>(+39.79%)</b></td><td>433.90 <b>(+57.90%)</b></td><td>42.52 <b>(-69.02%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.20 (n/a)</td><td>378.76 (n/a)</td><td>315.90 (n/a)</td><td>274.80 (n/a)</td><td>137.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+19.74%)</td><td>0.01 (+5.87%)</td><td>0.01 (-3.78%)</td><td>0.01 (-11.26%)</td><td>0.00 <b>(+77.87%)</b></td><td>645.20 (+12.70%)</td><td>422.60 (+2.55%)</td><td>433.30 (+3.93%)</td><td>247.20 (-16.46%)</td><td>165.42 <b>(+59.52%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.50 (n/a)</td><td>412.10 (n/a)</td><td>416.90 (n/a)</td><td>295.90 (n/a)</td><td>103.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 <b>(-21.67%)</b></td><td>0.01 (+1.79%)</td><td>0.01 <b>(+64.68%)</b></td><td>0.00 <b>(-33.55%)</b></td><td>0.00 (-16.62%)</td><td>1013.30 <b>(+50.50%)</b></td><td>481.74 (+3.21%)</td><td>331.60 <b>(-39.28%)</b></td><td>294.70 <b>(+27.63%)</b></td><td>305.41 <b>(+62.38%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.30 (n/a)</td><td>466.76 (n/a)</td><td>546.10 (n/a)</td><td>230.90 (n/a)</td><td>188.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-12.02%)</td><td>0.01 <b>(-22.03%)</b></td><td>0.01 <b>(-40.14%)</b></td><td>0.01 (+1.90%)</td><td>0.00 <b>(-20.55%)</b></td><td>583.00 (-1.85%)</td><td>463.68 <b>(+21.13%)</b></td><td>502.00 <b>(+67.05%)</b></td><td>236.10 (+13.67%)</td><td>133.44 <b>(-22.45%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.00 (n/a)</td><td>382.80 (n/a)</td><td>300.50 (n/a)</td><td>207.70 (n/a)</td><td>172.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+11.13%)</td><td>0.01 (-13.56%)</td><td>0.01 <b>(-25.76%)</b></td><td>0.00 <b>(-64.75%)</b></td><td>0.01 <b>(+30.50%)</b></td><td>1973.30 <b>(+183.68%)</b></td><td>705.98 <b>(+69.19%)</b></td><td>438.00 <b>(+34.69%)</b></td><td>222.90 (-10.01%)</td><td>721.42 <b>(+266.19%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>695.60 (n/a)</td><td>417.28 (n/a)</td><td>325.20 (n/a)</td><td>247.70 (n/a)</td><td>197.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(+26.46%)</b></td><td>0.01 <b>(+71.62%)</b></td><td>0.02 <b>(+118.34%)</b></td><td>0.01 <b>(+252.93%)</b></td><td>0.00 (-11.70%)</td><td>539.90 <b>(-71.66%)</b></td><td>320.16 <b>(-57.44%)</b></td><td>260.40 <b>(-54.20%)</b></td><td>229.20 <b>(-20.91%)</b></td><td>126.59 <b>(-80.77%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1905.40 (n/a)</td><td>752.22 (n/a)</td><td>568.60 (n/a)</td><td>289.80 (n/a)</td><td>658.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (+13.33%)</td><td>0.02 (-5.13%)</td><td>0.02 <b>(-29.19%)</b></td><td>0.01 (-16.48%)</td><td>0.01 <b>(+55.90%)</b></td><td>633.50 (+19.73%)</td><td>422.74 (+14.64%)</td><td>458.60 <b>(+41.19%)</b></td><td>235.30 (-11.74%)</td><td>170.18 <b>(+56.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.10 (n/a)</td><td>368.74 (n/a)</td><td>324.80 (n/a)</td><td>266.60 (n/a)</td><td>108.77 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (+7.79%)</td><td>0.03 (+18.96%)</td><td>0.03 <b>(+28.37%)</b></td><td>0.02 (+6.99%)</td><td>0.01 <b>(+22.36%)</b></td><td>519.90 (-6.53%)</td><td>307.56 (-14.31%)</td><td>241.20 <b>(-22.09%)</b></td><td>230.80 (-7.23%)</td><td>123.54 (+2.13%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.20 (n/a)</td><td>358.92 (n/a)</td><td>309.60 (n/a)</td><td>248.80 (n/a)</td><td>120.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (+12.43%)</td><td>0.03 <b>(+60.51%)</b></td><td>0.03 <b>(+93.78%)</b></td><td>0.02 <b>(+344.71%)</b></td><td>0.01 <b>(-30.48%)</b></td><td>417.30 <b>(-77.51%)</b></td><td>272.20 <b>(-59.78%)</b></td><td>238.70 <b>(-48.39%)</b></td><td>202.60 (-11.02%)</td><td>87.11 <b>(-87.00%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1855.70 (n/a)</td><td>676.86 (n/a)</td><td>462.50 (n/a)</td><td>227.70 (n/a)</td><td>670.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (-5.79%)</td><td>0.03 <b>(+25.37%)</b></td><td>0.03 (+4.79%)</td><td>0.03 <b>(+562.89%)</b></td><td>0.00 <b>(-80.87%)</b></td><td>315.40 <b>(-84.92%)</b></td><td>284.50 <b>(-56.83%)</b></td><td>280.80 (-4.59%)</td><td>257.70 (+6.14%)</td><td>21.91 <b>(-97.27%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2090.90 (n/a)</td><td>659.04 (n/a)</td><td>294.30 (n/a)</td><td>242.80 (n/a)</td><td>801.84 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 <b>(-31.35%)</b></td><td>0.02 <b>(-22.78%)</b></td><td>0.02 (-11.58%)</td><td>0.00 (+0.87%)</td><td>0.01 <b>(-30.47%)</b></td><td>2463.80 (-0.86%)</td><td>845.54 (+8.85%)</td><td>536.60 (+13.09%)</td><td>286.50 <b>(+45.65%)</b></td><td>917.45 (-4.84%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2485.20 (n/a)</td><td>776.80 (n/a)</td><td>474.50 (n/a)</td><td>196.70 (n/a)</td><td>964.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (-10.17%)</td><td>0.02 <b>(-22.60%)</b></td><td>0.02 <b>(-46.67%)</b></td><td>0.01 <b>(-35.74%)</b></td><td>0.01 (+10.08%)</td><td>835.60 <b>(+55.61%)</b></td><td>466.34 <b>(+43.22%)</b></td><td>485.30 <b>(+87.52%)</b></td><td>221.60 (+11.30%)</td><td>247.96 <b>(+76.56%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.00 (n/a)</td><td>325.62 (n/a)</td><td>258.80 (n/a)</td><td>199.10 (n/a)</td><td>140.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 <b>(-37.18%)</b></td><td>0.02 <b>(-33.31%)</b></td><td>0.02 <b>(-31.43%)</b></td><td>0.01 (-7.62%)</td><td>0.01 <b>(-47.90%)</b></td><td>673.40 (+8.25%)</td><td>490.38 <b>(+38.53%)</b></td><td>476.30 <b>(+45.79%)</b></td><td>312.00 <b>(+59.18%)</b></td><td>156.50 (-7.74%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.10 (n/a)</td><td>354.00 (n/a)</td><td>326.70 (n/a)</td><td>196.00 (n/a)</td><td>169.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-33.50%)</b></td><td>0.02 <b>(-43.39%)</b></td><td>0.02 <b>(-43.47%)</b></td><td>0.00 <b>(-75.79%)</b></td><td>0.01 <b>(+24.92%)</b></td><td>1894.20 <b>(+312.95%)</b></td><td>748.86 <b>(+138.49%)</b></td><td>506.30 <b>(+76.90%)</b></td><td>380.60 <b>(+50.38%)</b></td><td>644.70 <b>(+684.79%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.70 (n/a)</td><td>314.00 (n/a)</td><td>286.20 (n/a)</td><td>253.10 (n/a)</td><td>82.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 <b>(-22.60%)</b></td><td>0.02 <b>(-29.36%)</b></td><td>0.02 <b>(-48.12%)</b></td><td>0.01 <b>(-23.89%)</b></td><td>0.01 <b>(-29.08%)</b></td><td>640.20 <b>(+31.38%)</b></td><td>490.28 <b>(+39.42%)</b></td><td>524.00 <b>(+92.79%)</b></td><td>327.10 <b>(+29.19%)</b></td><td>138.26 (+15.98%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.30 (n/a)</td><td>351.66 (n/a)</td><td>271.80 (n/a)</td><td>253.20 (n/a)</td><td>119.21 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-39.23%)</b></td><td>0.01 <b>(-26.04%)</b></td><td>0.02 (+3.48%)</td><td>0.00 <b>(-66.17%)</b></td><td>0.01 <b>(-21.71%)</b></td><td>1879.20 <b>(+195.61%)</b></td><td>765.04 <b>(+65.08%)</b></td><td>486.70 (-3.36%)</td><td>423.10 <b>(+64.57%)</b></td><td>626.95 <b>(+300.02%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.70 (n/a)</td><td>463.44 (n/a)</td><td>503.60 (n/a)</td><td>257.10 (n/a)</td><td>156.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (+18.71%)</td><td>0.02 (-3.88%)</td><td>0.02 (-10.97%)</td><td>0.01 <b>(-38.42%)</b></td><td>0.01 <b>(+52.34%)</b></td><td>816.20 <b>(+62.36%)</b></td><td>435.30 (+19.05%)</td><td>351.40 (+12.34%)</td><td>201.20 (-15.78%)</td><td>237.76 <b>(+102.50%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.70 (n/a)</td><td>365.64 (n/a)</td><td>312.80 (n/a)</td><td>238.90 (n/a)</td><td>117.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (+0.13%)</td><td>0.02 (+7.41%)</td><td>0.02 (+1.15%)</td><td>0.01 <b>(+49.84%)</b></td><td>0.01 (-17.26%)</td><td>610.30 <b>(-33.26%)</b></td><td>503.70 (-12.72%)</td><td>545.20 (-1.14%)</td><td>302.30 (-0.13%)</td><td>118.34 <b>(-46.69%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>914.50 (n/a)</td><td>577.14 (n/a)</td><td>551.50 (n/a)</td><td>302.70 (n/a)</td><td>221.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (-10.73%)</td><td>0.05 (-7.94%)</td><td>0.04 <b>(-24.77%)</b></td><td>0.04 (+15.27%)</td><td>0.01 <b>(-37.35%)</b></td><td>445.30 (-13.25%)</td><td>372.58 (+3.68%)</td><td>374.10 <b>(+32.94%)</b></td><td>297.50 (+12.01%)</td><td>71.69 <b>(-38.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>513.30 (n/a)</td><td>359.36 (n/a)</td><td>281.40 (n/a)</td><td>265.60 (n/a)</td><td>116.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (+2.45%)</td><td>0.05 (-7.21%)</td><td>0.06 (-7.23%)</td><td>0.03 (-15.69%)</td><td>0.02 (+13.68%)</td><td>607.10 (+18.62%)</td><td>377.76 (+11.45%)</td><td>297.70 (+7.78%)</td><td>252.90 (-2.39%)</td><td>145.69 <b>(+35.30%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.80 (n/a)</td><td>338.96 (n/a)</td><td>276.20 (n/a)</td><td>259.10 (n/a)</td><td>107.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 <b>(-36.74%)</b></td><td>0.04 <b>(-31.15%)</b></td><td>0.04 <b>(-29.31%)</b></td><td>0.03 (-2.07%)</td><td>0.01 <b>(-53.45%)</b></td><td>554.50 (+2.12%)</td><td>465.40 <b>(+36.60%)</b></td><td>462.90 <b>(+41.47%)</b></td><td>327.60 <b>(+58.11%)</b></td><td>92.36 <b>(-26.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>543.00 (n/a)</td><td>340.70 (n/a)</td><td>327.20 (n/a)</td><td>207.20 (n/a)</td><td>125.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (-17.79%)</td><td>0.04 (-18.55%)</td><td>0.04 <b>(-35.71%)</b></td><td>0.03 (+9.11%)</td><td>0.01 <b>(-22.30%)</b></td><td>549.30 (-8.36%)</td><td>421.42 (+18.17%)</td><td>466.00 <b>(+55.54%)</b></td><td>256.30 <b>(+21.64%)</b></td><td>129.82 (-14.85%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.40 (n/a)</td><td>356.62 (n/a)</td><td>299.60 (n/a)</td><td>210.70 (n/a)</td><td>152.45 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 <b>(-35.28%)</b></td><td>0.04 (-17.98%)</td><td>0.03 (-9.54%)</td><td>0.03 (+0.72%)</td><td>0.01 <b>(-50.71%)</b></td><td>591.80 (-0.72%)</td><td>427.28 (+6.07%)</td><td>477.90 (+10.55%)</td><td>288.80 <b>(+54.52%)</b></td><td>131.93 <b>(-30.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>596.10 (n/a)</td><td>402.84 (n/a)</td><td>432.30 (n/a)</td><td>186.90 (n/a)</td><td>190.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (-14.05%)</td><td>0.04 <b>(-23.23%)</b></td><td>0.04 <b>(-22.14%)</b></td><td>0.02 <b>(-26.80%)</b></td><td>0.01 (-3.84%)</td><td>693.70 <b>(+36.61%)</b></td><td>470.48 <b>(+32.72%)</b></td><td>437.40 <b>(+28.42%)</b></td><td>316.50 (+16.32%)</td><td>139.11 <b>(+51.86%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>507.80 (n/a)</td><td>354.48 (n/a)</td><td>340.60 (n/a)</td><td>272.10 (n/a)</td><td>91.61 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 <b>(-20.72%)</b></td><td>0.03 (-15.82%)</td><td>0.03 (-1.51%)</td><td>0.03 (+0.58%)</td><td>0.01 <b>(-46.78%)</b></td><td>634.90 (-0.58%)</td><td>500.88 (+12.42%)</td><td>483.80 (+1.55%)</td><td>367.70 <b>(+26.14%)</b></td><td>102.39 <b>(-29.65%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>638.60 (n/a)</td><td>445.56 (n/a)</td><td>476.40 (n/a)</td><td>291.50 (n/a)</td><td>145.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 <b>(+125.27%)</b></td><td>0.05 <b>(+60.28%)</b></td><td>0.04 <b>(+37.24%)</b></td><td>0.03 (-1.90%)</td><td>0.02 <b>(+675.82%)</b></td><td>612.20 (+1.93%)</td><td>404.06 <b>(-26.59%)</b></td><td>409.00 <b>(-27.15%)</b></td><td>208.30 <b>(-55.61%)</b></td><td>173.82 <b>(+257.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>600.60 (n/a)</td><td>550.44 (n/a)</td><td>561.40 (n/a)</td><td>469.20 (n/a)</td><td>48.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 <b>(-25.72%)</b></td><td>0.03 (-7.46%)</td><td>0.04 (+0.92%)</td><td>0.01 <b>(-38.01%)</b></td><td>0.02 (-11.51%)</td><td>1873.70 <b>(+61.32%)</b></td><td>740.14 <b>(+25.25%)</b></td><td>455.10 (-0.91%)</td><td>340.90 <b>(+34.64%)</b></td><td>648.49 <b>(+87.28%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1161.50 (n/a)</td><td>590.92 (n/a)</td><td>459.30 (n/a)</td><td>253.20 (n/a)</td><td>346.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (-2.49%)</td><td>0.05 (-8.99%)</td><td>0.04 <b>(-29.57%)</b></td><td>0.03 (-6.60%)</td><td>0.02 (+2.52%)</td><td>611.20 (+7.08%)</td><td>401.54 (+10.98%)</td><td>417.20 <b>(+42.00%)</b></td><td>233.30 (+2.55%)</td><td>155.99 (+6.92%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.80 (n/a)</td><td>361.82 (n/a)</td><td>293.80 (n/a)</td><td>227.50 (n/a)</td><td>145.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (+19.88%)</td><td>0.04 (-11.81%)</td><td>0.03 <b>(-24.11%)</b></td><td>0.02 <b>(-39.81%)</b></td><td>0.02 <b>(+90.04%)</b></td><td>850.00 <b>(+66.11%)</b></td><td>522.64 <b>(+28.07%)</b></td><td>529.90 <b>(+31.75%)</b></td><td>245.60 (-16.58%)</td><td>218.71 <b>(+150.79%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.70 (n/a)</td><td>408.08 (n/a)</td><td>402.20 (n/a)</td><td>294.40 (n/a)</td><td>87.21 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (+4.05%)</td><td>0.04 (-3.97%)</td><td>0.04 (-3.53%)</td><td>0.02 (-12.43%)</td><td>0.01 <b>(+44.47%)</b></td><td>685.10 (+14.18%)</td><td>447.22 (+10.36%)</td><td>378.80 (+3.67%)</td><td>295.70 (-3.90%)</td><td>172.10 <b>(+49.72%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>600.00 (n/a)</td><td>405.24 (n/a)</td><td>365.40 (n/a)</td><td>307.70 (n/a)</td><td>114.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (+8.01%)</td><td>0.10 (+6.87%)</td><td>0.11 <b>(+22.77%)</b></td><td>0.06 (+10.79%)</td><td>0.03 (-8.66%)</td><td>530.10 (-9.74%)</td><td>351.92 (-8.90%)</td><td>309.80 (-18.54%)</td><td>229.30 (-7.39%)</td><td>119.94 (-17.23%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.30 (n/a)</td><td>386.30 (n/a)</td><td>380.30 (n/a)</td><td>247.60 (n/a)</td><td>144.92 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (-16.55%)</td><td>0.08 <b>(-29.83%)</b></td><td>0.07 <b>(-47.26%)</b></td><td>0.06 (-10.89%)</td><td>0.03 (-18.83%)</td><td>583.40 (+12.21%)</td><td>424.04 <b>(+40.29%)</b></td><td>466.40 <b>(+89.59%)</b></td><td>269.70 (+19.81%)</td><td>126.90 (+2.62%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>519.90 (n/a)</td><td>302.26 (n/a)</td><td>246.00 (n/a)</td><td>225.10 (n/a)</td><td>123.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.11 <b>(-20.20%)</b></td><td>0.08 <b>(-26.41%)</b></td><td>0.07 <b>(-37.12%)</b></td><td>0.06 <b>(-20.47%)</b></td><td>0.02 (-19.89%)</td><td>591.50 <b>(+25.72%)</b></td><td>450.32 <b>(+36.20%)</b></td><td>455.60 <b>(+59.08%)</b></td><td>301.80 <b>(+25.33%)</b></td><td>132.27 <b>(+28.88%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>470.50 (n/a)</td><td>330.64 (n/a)</td><td>286.40 (n/a)</td><td>240.80 (n/a)</td><td>102.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (+3.45%)</td><td>0.09 (-14.97%)</td><td>0.09 <b>(-22.98%)</b></td><td>0.05 <b>(-31.95%)</b></td><td>0.03 <b>(+51.02%)</b></td><td>600.00 <b>(+46.95%)</b></td><td>400.74 <b>(+23.70%)</b></td><td>381.90 <b>(+29.85%)</b></td><td>258.90 (-3.36%)</td><td>126.76 <b>(+116.11%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>408.30 (n/a)</td><td>323.96 (n/a)</td><td>294.10 (n/a)</td><td>267.90 (n/a)</td><td>58.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 <b>(-39.88%)</b></td><td>0.06 <b>(-43.84%)</b></td><td>0.06 <b>(-49.63%)</b></td><td>0.05 (-16.60%)</td><td>0.01 <b>(-60.60%)</b></td><td>618.50 (+19.91%)</td><td>539.68 <b>(+69.25%)</b></td><td>559.70 <b>(+98.55%)</b></td><td>408.00 <b>(+66.33%)</b></td><td>83.90 <b>(-25.16%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>515.80 (n/a)</td><td>318.86 (n/a)</td><td>281.90 (n/a)</td><td>245.30 (n/a)</td><td>112.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (-7.14%)</td><td>0.10 (+9.83%)</td><td>0.11 (+3.73%)</td><td>0.06 <b>(+284.13%)</b></td><td>0.04 <b>(-28.94%)</b></td><td>546.10 <b>(-73.97%)</b></td><td>357.84 <b>(-46.29%)</b></td><td>286.40 (-3.60%)</td><td>235.20 (+7.69%)</td><td>143.20 <b>(-82.20%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2097.90 (n/a)</td><td>666.30 (n/a)</td><td>297.10 (n/a)</td><td>218.40 (n/a)</td><td>804.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (+1.65%)</td><td>0.08 <b>(-21.51%)</b></td><td>0.06 <b>(-45.31%)</b></td><td>0.05 (-17.24%)</td><td>0.03 (-6.43%)</td><td>666.60 <b>(+20.83%)</b></td><td>482.44 <b>(+26.00%)</b></td><td>519.90 <b>(+82.87%)</b></td><td>252.10 (-1.60%)</td><td>153.02 (-0.03%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.70 (n/a)</td><td>382.90 (n/a)</td><td>284.30 (n/a)</td><td>256.20 (n/a)</td><td>153.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 <b>(-40.05%)</b></td><td>0.08 <b>(-27.21%)</b></td><td>0.08 <b>(-31.07%)</b></td><td>0.07 (+11.42%)</td><td>0.00 <b>(-85.92%)</b></td><td>460.90 (-10.24%)</td><td>429.24 <b>(+28.40%)</b></td><td>419.40 <b>(+45.07%)</b></td><td>404.20 <b>(+66.82%)</b></td><td>22.38 <b>(-79.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>513.50 (n/a)</td><td>334.30 (n/a)</td><td>289.10 (n/a)</td><td>242.30 (n/a)</td><td>108.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (-4.26%)</td><td>0.10 (-3.47%)</td><td>0.12 (-5.10%)</td><td>0.07 (+11.55%)</td><td>0.03 <b>(-21.91%)</b></td><td>489.40 (-10.35%)</td><td>346.34 (-1.69%)</td><td>274.30 (+5.38%)</td><td>243.50 (+4.46%)</td><td>114.52 <b>(-23.93%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>545.90 (n/a)</td><td>352.28 (n/a)</td><td>260.30 (n/a)</td><td>233.10 (n/a)</td><td>150.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (-10.77%)</td><td>0.09 (+8.35%)</td><td>0.10 (+13.84%)</td><td>0.05 (-0.08%)</td><td>0.03 (-13.76%)</td><td>596.10 (+0.08%)</td><td>392.98 (-9.65%)</td><td>339.20 (-12.17%)</td><td>280.10 (+12.04%)</td><td>134.12 (-10.26%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>595.60 (n/a)</td><td>434.96 (n/a)</td><td>386.20 (n/a)</td><td>250.00 (n/a)</td><td>149.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 <b>(+97.09%)</b></td><td>0.09 <b>(+59.64%)</b></td><td>0.07 <b>(+39.71%)</b></td><td>0.05 (-6.25%)</td><td>0.04 <b>(+291.67%)</b></td><td>724.10 (+6.67%)</td><td>423.86 <b>(-28.21%)</b></td><td>438.20 <b>(-28.41%)</b></td><td>224.90 <b>(-49.27%)</b></td><td>192.05 <b>(+119.12%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>678.80 (n/a)</td><td>590.44 (n/a)</td><td>612.10 (n/a)</td><td>443.30 (n/a)</td><td>87.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 <b>(+26.99%)</b></td><td>0.08 <b>(+32.18%)</b></td><td>0.08 (+17.23%)</td><td>0.05 <b>(+191.52%)</b></td><td>0.03 (-4.90%)</td><td>627.30 <b>(-65.70%)</b></td><td>435.48 <b>(-41.11%)</b></td><td>396.10 (-14.71%)</td><td>264.20 <b>(-21.25%)</b></td><td>142.86 <b>(-76.83%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1828.70 (n/a)</td><td>739.46 (n/a)</td><td>464.40 (n/a)</td><td>335.50 (n/a)</td><td>616.71 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-20.12%)</b></td><td>0.01 <b>(-31.96%)</b></td><td>0.01 <b>(-45.67%)</b></td><td>0.01 <b>(-28.08%)</b></td><td>0.01 <b>(-26.15%)</b></td><td>677.30 <b>(+39.05%)</b></td><td>440.26 <b>(+45.76%)</b></td><td>440.30 <b>(+84.07%)</b></td><td>226.60 <b>(+25.19%)</b></td><td>187.09 <b>(+30.97%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>487.10 (n/a)</td><td>302.04 (n/a)</td><td>239.20 (n/a)</td><td>181.00 (n/a)</td><td>142.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-18.42%)</td><td>0.02 (-12.00%)</td><td>0.01 (-10.18%)</td><td>0.01 (-2.98%)</td><td>0.00 <b>(-36.39%)</b></td><td>545.60 (+3.08%)</td><td>429.20 (+8.03%)</td><td>470.20 (+11.34%)</td><td>305.40 <b>(+22.60%)</b></td><td>106.42 <b>(-21.24%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>529.30 (n/a)</td><td>397.30 (n/a)</td><td>422.30 (n/a)</td><td>249.10 (n/a)</td><td>135.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-14.99%)</td><td>0.01 (-3.54%)</td><td>0.01 (-17.43%)</td><td>0.01 (+9.93%)</td><td>0.00 <b>(-22.25%)</b></td><td>513.10 (-9.04%)</td><td>371.38 (-2.76%)</td><td>403.70 <b>(+21.12%)</b></td><td>240.60 (+17.65%)</td><td>122.26 <b>(-26.68%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.10 (n/a)</td><td>381.94 (n/a)</td><td>333.30 (n/a)</td><td>204.50 (n/a)</td><td>166.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-23.10%)</b></td><td>0.02 (-2.96%)</td><td>0.02 <b>(+40.87%)</b></td><td>0.01 (+12.28%)</td><td>0.01 <b>(-32.32%)</b></td><td>603.30 (-10.93%)</td><td>383.76 (-6.09%)</td><td>298.90 <b>(-29.00%)</b></td><td>233.70 <b>(+30.05%)</b></td><td>167.03 (-18.12%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.30 (n/a)</td><td>408.66 (n/a)</td><td>421.00 (n/a)</td><td>179.70 (n/a)</td><td>203.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(+43.25%)</b></td><td>0.02 <b>(+69.07%)</b></td><td>0.02 <b>(+96.56%)</b></td><td>0.01 <b>(+69.46%)</b></td><td>0.00 (+3.87%)</td><td>314.00 <b>(-40.98%)</b></td><td>259.08 <b>(-42.04%)</b></td><td>244.20 <b>(-49.14%)</b></td><td>212.20 <b>(-30.20%)</b></td><td>39.21 <b>(-55.19%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.00 (n/a)</td><td>446.98 (n/a)</td><td>480.10 (n/a)</td><td>304.00 (n/a)</td><td>87.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-28.22%)</b></td><td>0.01 <b>(-39.74%)</b></td><td>0.01 <b>(-40.36%)</b></td><td>0.00 <b>(-78.00%)</b></td><td>0.01 (+3.97%)</td><td>2076.50 <b>(+354.48%)</b></td><td>808.60 <b>(+131.20%)</b></td><td>556.70 <b>(+67.68%)</b></td><td>297.70 <b>(+39.31%)</b></td><td>717.75 <b>(+655.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>456.90 (n/a)</td><td>349.74 (n/a)</td><td>332.00 (n/a)</td><td>213.70 (n/a)</td><td>94.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (+4.61%)</td><td>0.01 (-5.15%)</td><td>0.01 (-4.72%)</td><td>0.00 <b>(-77.35%)</b></td><td>0.01 <b>(+87.35%)</b></td><td>2100.50 <b>(+341.47%)</b></td><td>703.48 <b>(+80.92%)</b></td><td>443.50 (+4.97%)</td><td>234.40 (-4.40%)</td><td>788.31 <b>(+750.97%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.80 (n/a)</td><td>388.84 (n/a)</td><td>422.50 (n/a)</td><td>245.20 (n/a)</td><td>92.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-2.08%)</td><td>0.01 (-8.44%)</td><td>0.01 <b>(-27.37%)</b></td><td>0.01 (+4.76%)</td><td>0.00 (+11.43%)</td><td>540.00 (-4.54%)</td><td>431.82 (+11.81%)</td><td>524.80 <b>(+37.71%)</b></td><td>251.80 (+2.11%)</td><td>139.96 (+14.39%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.70 (n/a)</td><td>386.20 (n/a)</td><td>381.10 (n/a)</td><td>246.60 (n/a)</td><td>122.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 (-14.64%)</td><td>0.01 <b>(+31.00%)</b></td><td>0.02 <b>(+118.11%)</b></td><td>0.01 <b>(+313.34%)</b></td><td>0.00 <b>(-36.68%)</b></td><td>477.50 <b>(-75.80%)</b></td><td>335.58 <b>(-52.96%)</b></td><td>246.50 <b>(-54.16%)</b></td><td>240.40 (+17.15%)</td><td>126.18 <b>(-82.54%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1973.50 (n/a)</td><td>713.46 (n/a)</td><td>537.70 (n/a)</td><td>205.20 (n/a)</td><td>722.69 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.01 <b>(-40.45%)</b></td><td>0.01 (-18.76%)</td><td>0.01 (-15.24%)</td><td>0.01 (+3.26%)</td><td>0.00 <b>(-61.29%)</b></td><td>583.80 (-3.17%)</td><td>476.66 (+12.41%)</td><td>498.10 (+17.98%)</td><td>367.10 <b>(+67.93%)</b></td><td>94.50 <b>(-36.73%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.90 (n/a)</td><td>424.02 (n/a)</td><td>422.20 (n/a)</td><td>218.60 (n/a)</td><td>149.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-28.98%)</b></td><td>0.01 (-11.28%)</td><td>0.01 (-13.05%)</td><td>0.01 (+4.66%)</td><td>0.00 <b>(-30.58%)</b></td><td>576.10 (-4.46%)</td><td>433.34 (+8.22%)</td><td>495.80 (+15.03%)</td><td>244.80 <b>(+40.77%)</b></td><td>161.30 (+1.98%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.00 (n/a)</td><td>400.44 (n/a)</td><td>431.00 (n/a)</td><td>173.90 (n/a)</td><td>158.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (+11.90%)</td><td>0.02 (-7.06%)</td><td>0.02 (+2.32%)</td><td>0.01 (+7.01%)</td><td>0.01 (+0.88%)</td><td>581.30 (-6.56%)</td><td>436.98 (+6.40%)</td><td>441.10 (-2.26%)</td><td>212.50 (-10.60%)</td><td>155.16 (-6.91%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.10 (n/a)</td><td>410.68 (n/a)</td><td>451.30 (n/a)</td><td>237.70 (n/a)</td><td>166.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (-10.26%)</td><td>0.04 (-2.46%)</td><td>0.04 (+5.09%)</td><td>0.02 <b>(-21.44%)</b></td><td>0.01 (-10.89%)</td><td>543.90 <b>(+27.29%)</b></td><td>327.72 (+3.61%)</td><td>291.00 (-4.84%)</td><td>244.50 (+11.44%)</td><td>124.41 <b>(+30.02%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>427.30 (n/a)</td><td>316.30 (n/a)</td><td>305.80 (n/a)</td><td>219.40 (n/a)</td><td>95.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 (-6.07%)</td><td>0.02 (-9.56%)</td><td>0.02 (-6.52%)</td><td>0.01 (+5.85%)</td><td>0.01 (-10.04%)</td><td>614.30 (-5.52%)</td><td>460.42 (+8.23%)</td><td>469.30 (+6.98%)</td><td>252.40 (+6.45%)</td><td>134.49 (-12.94%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.20 (n/a)</td><td>425.40 (n/a)</td><td>438.70 (n/a)</td><td>237.10 (n/a)</td><td>154.47 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (+2.42%)</td><td>0.03 <b>(+22.89%)</b></td><td>0.04 <b>(+88.69%)</b></td><td>0.01 <b>(-75.25%)</b></td><td>0.02 <b>(+71.69%)</b></td><td>2004.90 <b>(+303.97%)</b></td><td>619.50 <b>(+46.60%)</b></td><td>244.40 <b>(-47.01%)</b></td><td>231.00 (-2.37%)</td><td>776.64 <b>(+629.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.30 (n/a)</td><td>422.58 (n/a)</td><td>461.20 (n/a)</td><td>236.60 (n/a)</td><td>106.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.03 <b>(-26.91%)</b></td><td>0.02 (-17.55%)</td><td>0.02 <b>(-33.50%)</b></td><td>0.02 <b>(+23.43%)</b></td><td>0.01 <b>(-45.93%)</b></td><td>484.10 (-18.98%)</td><td>358.96 (+6.13%)</td><td>360.50 <b>(+50.33%)</b></td><td>240.70 <b>(+36.84%)</b></td><td>103.27 <b>(-42.10%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.50 (n/a)</td><td>338.22 (n/a)</td><td>239.80 (n/a)</td><td>175.90 (n/a)</td><td>178.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.05 (+10.51%)</td><td>0.03 <b>(+61.32%)</b></td><td>0.03 <b>(+76.98%)</b></td><td>0.02 <b>(+249.15%)</b></td><td>0.01 <b>(-22.03%)</b></td><td>549.90 <b>(-71.36%)</b></td><td>330.54 <b>(-55.95%)</b></td><td>304.50 <b>(-43.50%)</b></td><td>222.00 (-9.54%)</td><td>128.44 <b>(-80.72%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1919.80 (n/a)</td><td>750.38 (n/a)</td><td>538.90 (n/a)</td><td>245.40 (n/a)</td><td>666.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 <b>(-30.63%)</b></td><td>0.02 <b>(-27.29%)</b></td><td>0.02 <b>(-30.91%)</b></td><td>0.01 (+14.91%)</td><td>0.01 <b>(-32.19%)</b></td><td>598.00 (-12.97%)</td><td>403.12 <b>(+25.90%)</b></td><td>356.20 <b>(+44.74%)</b></td><td>207.00 <b>(+44.15%)</b></td><td>176.72 (-16.39%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>687.10 (n/a)</td><td>320.20 (n/a)</td><td>246.10 (n/a)</td><td>143.60 (n/a)</td><td>211.36 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 <b>(+25.00%)</b></td><td>0.02 (+19.69%)</td><td>0.02 <b>(+24.22%)</b></td><td>0.02 (-5.41%)</td><td>0.01 <b>(+71.56%)</b></td><td>604.90 (+5.71%)</td><td>427.60 (-10.08%)</td><td>423.80 (-19.51%)</td><td>245.80 <b>(-20.01%)</b></td><td>159.34 <b>(+52.21%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.20 (n/a)</td><td>475.52 (n/a)</td><td>526.50 (n/a)</td><td>307.30 (n/a)</td><td>104.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 (+16.28%)</td><td>0.02 (-9.69%)</td><td>0.02 (-14.51%)</td><td>0.01 (-10.43%)</td><td>0.01 <b>(+35.24%)</b></td><td>576.40 (+11.66%)</td><td>444.06 (+16.23%)</td><td>476.00 (+16.98%)</td><td>210.50 (-14.01%)</td><td>140.71 <b>(+22.99%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.20 (n/a)</td><td>382.04 (n/a)</td><td>406.90 (n/a)</td><td>244.80 (n/a)</td><td>114.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.04 <b>(-22.62%)</b></td><td>0.03 (-2.53%)</td><td>0.03 (-1.19%)</td><td>0.02 (+17.12%)</td><td>0.01 <b>(-45.11%)</b></td><td>475.00 (-14.63%)</td><td>338.60 (-7.30%)</td><td>302.70 (+1.20%)</td><td>244.30 <b>(+29.26%)</b></td><td>91.24 <b>(-41.61%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>556.40 (n/a)</td><td>365.28 (n/a)</td><td>299.10 (n/a)</td><td>189.00 (n/a)</td><td>156.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.02 <b>(-21.24%)</b></td><td>0.02 (-13.55%)</td><td>0.02 (-5.30%)</td><td>0.01 (-2.58%)</td><td>0.00 <b>(-37.67%)</b></td><td>645.10 (+2.66%)</td><td>528.62 (+12.13%)</td><td>493.90 (+5.60%)</td><td>390.10 <b>(+26.99%)</b></td><td>109.90 (-16.11%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.40 (n/a)</td><td>471.42 (n/a)</td><td>467.70 (n/a)</td><td>307.20 (n/a)</td><td>131.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (-11.57%)</td><td>0.05 (-6.99%)</td><td>0.05 (-14.99%)</td><td>0.03 (+18.15%)</td><td>0.01 <b>(-27.56%)</b></td><td>548.00 (-15.37%)</td><td>389.00 (+0.56%)</td><td>337.20 (+17.61%)</td><td>274.90 (+13.08%)</td><td>123.11 <b>(-29.73%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.50 (n/a)</td><td>386.84 (n/a)</td><td>286.70 (n/a)</td><td>243.10 (n/a)</td><td>175.20 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (+3.88%)</td><td>0.09 (+15.41%)</td><td>0.09 (+7.99%)</td><td>0.08 <b>(+83.27%)</b></td><td>0.01 <b>(-54.89%)</b></td><td>313.40 <b>(-45.44%)</b></td><td>278.10 (-19.60%)</td><td>276.00 (-7.38%)</td><td>240.40 (-3.72%)</td><td>29.06 <b>(-77.75%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.40 (n/a)</td><td>345.90 (n/a)</td><td>298.00 (n/a)</td><td>249.70 (n/a)</td><td>130.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 (-13.44%)</td><td>0.05 (+7.51%)</td><td>0.05 <b>(+40.12%)</b></td><td>0.03 (+4.21%)</td><td>0.01 <b>(-37.00%)</b></td><td>583.60 (-4.03%)</td><td>354.38 (-13.24%)</td><td>307.70 <b>(-28.62%)</b></td><td>272.70 (+15.50%)</td><td>128.96 <b>(-21.34%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.10 (n/a)</td><td>408.44 (n/a)</td><td>431.10 (n/a)</td><td>236.10 (n/a)</td><td>163.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (+17.71%)</td><td>0.07 <b>(+34.83%)</b></td><td>0.08 <b>(+95.38%)</b></td><td>0.04 (-3.38%)</td><td>0.02 (+9.36%)</td><td>546.10 (+3.51%)</td><td>309.06 <b>(-25.34%)</b></td><td>257.30 <b>(-48.82%)</b></td><td>203.90 (-15.04%)</td><td>136.30 (+0.14%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>527.60 (n/a)</td><td>413.94 (n/a)</td><td>502.70 (n/a)</td><td>240.00 (n/a)</td><td>136.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 <b>(+30.75%)</b></td><td>0.05 (+13.33%)</td><td>0.05 <b>(+35.35%)</b></td><td>0.03 (-17.13%)</td><td>0.02 <b>(+139.11%)</b></td><td>592.80 <b>(+20.66%)</b></td><td>386.92 (-2.19%)</td><td>299.00 <b>(-26.14%)</b></td><td>235.20 <b>(-23.51%)</b></td><td>158.49 <b>(+131.32%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.30 (n/a)</td><td>395.58 (n/a)</td><td>404.80 (n/a)</td><td>307.50 (n/a)</td><td>68.52 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (+6.43%)</td><td>0.06 (+3.89%)</td><td>0.06 (+1.85%)</td><td>0.03 (+4.60%)</td><td>0.02 <b>(+20.29%)</b></td><td>601.00 (-4.41%)</td><td>395.64 (-0.89%)</td><td>362.20 (-1.82%)</td><td>245.30 (-6.05%)</td><td>161.65 (+6.57%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.70 (n/a)</td><td>399.20 (n/a)</td><td>368.90 (n/a)</td><td>261.10 (n/a)</td><td>151.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 <b>(+30.50%)</b></td><td>0.06 (+9.45%)</td><td>0.06 <b>(+23.33%)</b></td><td>0.03 (+5.24%)</td><td>0.02 <b>(+52.19%)</b></td><td>518.60 (-4.97%)</td><td>345.90 (-2.21%)</td><td>266.20 (-18.92%)</td><td>192.10 <b>(-23.37%)</b></td><td>150.36 <b>(+23.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>545.70 (n/a)</td><td>353.72 (n/a)</td><td>328.30 (n/a)</td><td>250.70 (n/a)</td><td>121.39 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 <b>(+27.84%)</b></td><td>0.06 <b>(+59.51%)</b></td><td>0.06 <b>(+104.00%)</b></td><td>0.04 <b>(+42.46%)</b></td><td>0.02 <b>(+20.32%)</b></td><td>465.40 <b>(-29.80%)</b></td><td>325.70 <b>(-38.37%)</b></td><td>290.60 <b>(-50.99%)</b></td><td>229.70 <b>(-21.79%)</b></td><td>101.37 <b>(-33.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>663.00 (n/a)</td><td>528.46 (n/a)</td><td>592.90 (n/a)</td><td>293.70 (n/a)</td><td>152.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (-4.30%)</td><td>0.04 (-5.04%)</td><td>0.03 (-19.07%)</td><td>0.03 (+14.31%)</td><td>0.02 (-1.71%)</td><td>598.80 (-12.52%)</td><td>460.92 (+5.36%)</td><td>594.50 <b>(+23.57%)</b></td><td>235.10 (+4.49%)</td><td>185.66 (-1.01%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>684.50 (n/a)</td><td>437.48 (n/a)</td><td>481.10 (n/a)</td><td>225.00 (n/a)</td><td>187.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (-5.06%)</td><td>0.06 (+0.76%)</td><td>0.07 (+2.27%)</td><td>0.03 (-13.96%)</td><td>0.02 (+0.92%)</td><td>633.40 (+16.22%)</td><td>373.76 (+0.61%)</td><td>270.20 (-2.21%)</td><td>241.10 (+5.33%)</td><td>173.72 (+10.75%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>545.00 (n/a)</td><td>371.50 (n/a)</td><td>276.30 (n/a)</td><td>228.90 (n/a)</td><td>156.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (+14.21%)</td><td>0.04 (+12.20%)</td><td>0.04 <b>(+25.77%)</b></td><td>0.03 (+13.75%)</td><td>0.02 (+19.00%)</td><td>588.00 (-12.08%)</td><td>420.08 (-9.88%)</td><td>384.70 <b>(-20.48%)</b></td><td>247.70 (-12.47%)</td><td>137.76 (-4.71%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>668.80 (n/a)</td><td>466.14 (n/a)</td><td>483.80 (n/a)</td><td>283.00 (n/a)</td><td>144.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (+4.27%)</td><td>0.09 <b>(+30.63%)</b></td><td>0.12 <b>(+89.24%)</b></td><td>0.05 (-9.98%)</td><td>0.04 <b>(+41.64%)</b></td><td>612.30 (+11.08%)</td><td>399.82 (-17.46%)</td><td>279.40 <b>(-47.14%)</b></td><td>266.00 (-4.11%)</td><td>177.38 <b>(+52.15%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.20 (n/a)</td><td>484.42 (n/a)</td><td>528.60 (n/a)</td><td>277.40 (n/a)</td><td>116.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 <b>(+61.85%)</b></td><td>0.08 <b>(+43.49%)</b></td><td>0.10 <b>(+55.87%)</b></td><td>0.02 (-10.42%)</td><td>0.05 <b>(+103.63%)</b></td><td>2054.10 (+11.63%)</td><td>704.56 (-6.02%)</td><td>315.10 <b>(-35.84%)</b></td><td>258.10 <b>(-38.21%)</b></td><td>770.27 <b>(+25.97%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1840.10 (n/a)</td><td>749.68 (n/a)</td><td>491.10 (n/a)</td><td>417.70 (n/a)</td><td>611.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.17 (-4.82%)</td><td>0.13 <b>(+20.76%)</b></td><td>0.14 <b>(+64.41%)</b></td><td>0.07 (+7.92%)</td><td>0.04 (-13.05%)</td><td>563.10 (-7.34%)</td><td>343.88 (-19.50%)</td><td>286.50 <b>(-39.18%)</b></td><td>243.30 (+5.10%)</td><td>131.98 (-13.38%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>607.70 (n/a)</td><td>427.18 (n/a)</td><td>471.10 (n/a)</td><td>231.50 (n/a)</td><td>152.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 <b>(+97.92%)</b></td><td>0.11 <b>(+92.50%)</b></td><td>0.11 <b>(+82.44%)</b></td><td>0.07 <b>(+133.84%)</b></td><td>0.03 <b>(+89.25%)</b></td><td>473.40 <b>(-57.24%)</b></td><td>330.16 <b>(-49.32%)</b></td><td>303.90 <b>(-45.18%)</b></td><td>241.90 <b>(-49.48%)</b></td><td>97.96 <b>(-62.16%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1107.00 (n/a)</td><td>651.50 (n/a)</td><td>554.40 (n/a)</td><td>478.80 (n/a)</td><td>258.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.17 <b>(+22.78%)</b></td><td>0.14 <b>(+30.77%)</b></td><td>0.14 <b>(+40.75%)</b></td><td>0.08 (+2.89%)</td><td>0.04 <b>(+41.06%)</b></td><td>538.60 (-2.81%)</td><td>325.94 <b>(-21.13%)</b></td><td>288.60 <b>(-28.95%)</b></td><td>247.60 (-18.58%)</td><td>120.75 (+17.97%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>554.20 (n/a)</td><td>413.26 (n/a)</td><td>406.20 (n/a)</td><td>304.10 (n/a)</td><td>102.36 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 <b>(+20.59%)</b></td><td>0.09 (+12.98%)</td><td>0.06 (+0.59%)</td><td>0.05 (-7.55%)</td><td>0.05 <b>(+51.34%)</b></td><td>630.90 (+8.16%)</td><td>435.14 (-3.70%)</td><td>532.80 (-0.58%)</td><td>233.60 (-17.07%)</td><td>187.58 <b>(+26.49%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>583.30 (n/a)</td><td>451.86 (n/a)</td><td>535.90 (n/a)</td><td>281.70 (n/a)</td><td>148.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (-12.23%)</td><td>0.10 (+0.02%)</td><td>0.09 (-0.61%)</td><td>0.07 (+8.86%)</td><td>0.03 (-19.93%)</td><td>495.20 (-8.14%)</td><td>384.86 (-3.93%)</td><td>429.00 (+0.61%)</td><td>246.40 (+13.92%)</td><td>116.11 (-18.64%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>539.10 (n/a)</td><td>400.62 (n/a)</td><td>426.40 (n/a)</td><td>216.30 (n/a)</td><td>142.71 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (+7.93%)</td><td>0.11 <b>(+61.42%)</b></td><td>0.13 <b>(+106.41%)</b></td><td>0.05 <b>(+189.16%)</b></td><td>0.04 (-5.75%)</td><td>681.00 <b>(-65.42%)</b></td><td>350.76 <b>(-53.33%)</b></td><td>261.00 <b>(-51.55%)</b></td><td>243.30 (-7.35%)</td><td>187.64 <b>(-72.82%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1969.20 (n/a)</td><td>751.50 (n/a)</td><td>538.70 (n/a)</td><td>262.60 (n/a)</td><td>690.43 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.16 (+3.06%)</td><td>0.12 <b>(+44.33%)</b></td><td>0.12 <b>(+69.58%)</b></td><td>0.09 <b>(+57.00%)</b></td><td>0.02 <b>(-39.21%)</b></td><td>402.00 <b>(-36.31%)</b></td><td>308.78 <b>(-36.05%)</b></td><td>297.60 <b>(-41.03%)</b></td><td>237.50 (-2.98%)</td><td>59.48 <b>(-58.98%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>631.20 (n/a)</td><td>482.84 (n/a)</td><td>504.70 (n/a)</td><td>244.80 (n/a)</td><td>144.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 <b>(+36.30%)</b></td><td>0.08 (+6.72%)</td><td>0.07 (+14.95%)</td><td>0.05 (+4.95%)</td><td>0.03 <b>(+46.92%)</b></td><td>603.00 (-4.71%)</td><td>454.16 (-3.28%)</td><td>453.60 (-13.00%)</td><td>235.20 <b>(-26.64%)</b></td><td>137.67 (+1.13%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>632.80 (n/a)</td><td>469.58 (n/a)</td><td>521.40 (n/a)</td><td>320.60 (n/a)</td><td>136.13 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 <b>(+21.15%)</b></td><td>0.05 (-8.98%)</td><td>0.04 (-8.54%)</td><td>0.03 <b>(-25.71%)</b></td><td>0.02 <b>(+51.30%)</b></td><td>645.50 <b>(+34.62%)</b></td><td>458.50 (+17.12%)</td><td>485.30 (+9.33%)</td><td>235.70 (-17.47%)</td><td>150.77 <b>(+61.60%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>479.50 (n/a)</td><td>391.48 (n/a)</td><td>443.90 (n/a)</td><td>285.60 (n/a)</td><td>93.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (+3.94%)</td><td>0.06 (+8.26%)</td><td>0.07 (+7.99%)</td><td>0.03 (-3.18%)</td><td>0.02 (+13.67%)</td><td>594.40 (+3.28%)</td><td>346.30 (-5.70%)</td><td>289.40 (-7.39%)</td><td>267.70 (-3.81%)</td><td>139.10 (+14.65%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>575.50 (n/a)</td><td>367.22 (n/a)</td><td>312.50 (n/a)</td><td>278.30 (n/a)</td><td>121.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 <b>(+38.76%)</b></td><td>0.06 (+0.89%)</td><td>0.04 (+0.36%)</td><td>0.04 (+9.91%)</td><td>0.04 <b>(+34.16%)</b></td><td>535.70 (-9.00%)</td><td>421.92 (+1.32%)</td><td>470.00 (-0.36%)</td><td>167.80 <b>(-27.95%)</b></td><td>145.75 (-14.21%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>588.70 (n/a)</td><td>416.44 (n/a)</td><td>471.70 (n/a)</td><td>232.90 (n/a)</td><td>169.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (-11.78%)</td><td>0.05 (+1.37%)</td><td>0.04 (-9.04%)</td><td>0.04 (+8.86%)</td><td>0.02 (-8.60%)</td><td>560.00 (-8.14%)</td><td>425.64 (-2.17%)</td><td>492.70 (+9.93%)</td><td>263.60 (+13.33%)</td><td>139.41 (-2.99%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>609.60 (n/a)</td><td>435.08 (n/a)</td><td>448.20 (n/a)</td><td>232.60 (n/a)</td><td>143.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 <b>(+25.55%)</b></td><td>0.04 (-9.29%)</td><td>0.03 <b>(-32.10%)</b></td><td>0.03 <b>(-21.35%)</b></td><td>0.02 <b>(+75.89%)</b></td><td>798.30 <b>(+27.14%)</b></td><td>579.26 <b>(+23.85%)</b></td><td>666.70 <b>(+47.27%)</b></td><td>237.60 <b>(-20.35%)</b></td><td>216.20 <b>(+66.11%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>627.90 (n/a)</td><td>467.72 (n/a)</td><td>452.70 (n/a)</td><td>298.30 (n/a)</td><td>130.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 <b>(+27.98%)</b></td><td>0.06 <b>(+37.92%)</b></td><td>0.06 <b>(+64.34%)</b></td><td>0.04 (+2.92%)</td><td>0.02 <b>(+65.62%)</b></td><td>558.20 (-2.85%)</td><td>378.74 <b>(-24.77%)</b></td><td>324.20 <b>(-39.15%)</b></td><td>271.30 <b>(-21.86%)</b></td><td>119.93 <b>(+27.36%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>574.60 (n/a)</td><td>503.44 (n/a)</td><td>532.80 (n/a)</td><td>347.20 (n/a)</td><td>94.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 (-13.90%)</td><td>0.07 (-2.80%)</td><td>0.05 (-8.95%)</td><td>0.04 <b>(+51.38%)</b></td><td>0.02 <b>(-34.44%)</b></td><td>555.20 <b>(-33.94%)</b></td><td>407.70 (-10.40%)</td><td>458.00 (+9.83%)</td><td>277.40 (+16.16%)</td><td>124.65 <b>(-49.73%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>840.50 (n/a)</td><td>455.04 (n/a)</td><td>417.00 (n/a)</td><td>238.80 (n/a)</td><td>247.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (-16.45%)</td><td>0.05 <b>(-38.88%)</b></td><td>0.05 <b>(-41.24%)</b></td><td>0.01 <b>(-76.86%)</b></td><td>0.03 <b>(+34.06%)</b></td><td>2086.90 <b>(+332.25%)</b></td><td>757.80 <b>(+141.23%)</b></td><td>472.70 <b>(+70.16%)</b></td><td>299.60 (+19.70%)</td><td>747.69 <b>(+675.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>482.80 (n/a)</td><td>314.14 (n/a)</td><td>277.80 (n/a)</td><td>250.30 (n/a)</td><td>96.45 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (+12.90%)</td><td>0.07 (+14.30%)</td><td>0.06 <b>(+33.71%)</b></td><td>0.04 <b>(+71.59%)</b></td><td>0.03 (-17.24%)</td><td>611.20 <b>(-41.72%)</b></td><td>418.54 <b>(-24.68%)</b></td><td>440.10 <b>(-25.22%)</b></td><td>235.00 (-11.42%)</td><td>148.52 <b>(-53.55%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1048.80 (n/a)</td><td>555.66 (n/a)</td><td>588.50 (n/a)</td><td>265.30 (n/a)</td><td>319.71 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 <b>(+54.11%)</b></td><td>0.06 <b>(+29.27%)</b></td><td>0.05 (+17.82%)</td><td>0.04 <b>(+81.47%)</b></td><td>0.02 <b>(+38.74%)</b></td><td>564.50 <b>(-44.90%)</b></td><td>447.12 <b>(-25.57%)</b></td><td>467.10 (-15.13%)</td><td>253.50 <b>(-35.13%)</b></td><td>116.69 <b>(-54.04%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1024.50 (n/a)</td><td>600.74 (n/a)</td><td>550.40 (n/a)</td><td>390.80 (n/a)</td><td>253.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 (+0.84%)</td><td>0.06 (-7.23%)</td><td>0.05 (-6.16%)</td><td>0.04 (-6.23%)</td><td>0.02 (-4.18%)</td><td>586.40 (+6.64%)</td><td>433.12 (+7.59%)</td><td>486.40 (+6.57%)</td><td>242.10 (-0.82%)</td><td>143.22 (+3.72%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>549.90 (n/a)</td><td>402.58 (n/a)</td><td>456.40 (n/a)</td><td>244.10 (n/a)</td><td>138.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 <b>(-20.67%)</b></td><td>0.05 (-14.98%)</td><td>0.05 <b>(-24.09%)</b></td><td>0.02 <b>(+50.32%)</b></td><td>0.02 <b>(-35.35%)</b></td><td>1392.20 <b>(-33.47%)</b></td><td>627.32 (-12.01%)</td><td>458.00 <b>(+31.72%)</b></td><td>376.90 <b>(+26.05%)</b></td><td>428.98 <b>(-44.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2092.70 (n/a)</td><td>712.98 (n/a)</td><td>347.70 (n/a)</td><td>299.00 (n/a)</td><td>774.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (-9.74%)</td><td>0.06 (+8.38%)</td><td>0.06 <b>(+48.25%)</b></td><td>0.04 (+5.00%)</td><td>0.02 <b>(-27.06%)</b></td><td>526.10 (-4.76%)</td><td>343.36 (-13.75%)</td><td>302.40 <b>(-32.56%)</b></td><td>225.70 (+10.80%)</td><td>120.52 <b>(-23.61%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>552.40 (n/a)</td><td>398.10 (n/a)</td><td>448.40 (n/a)</td><td>203.70 (n/a)</td><td>157.77 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 <b>(-24.04%)</b></td><td>0.05 <b>(-20.68%)</b></td><td>0.04 <b>(-27.33%)</b></td><td>0.03 (-7.50%)</td><td>0.02 (-17.92%)</td><td>555.90 (+8.11%)</td><td>403.14 <b>(+24.89%)</b></td><td>424.70 <b>(+37.62%)</b></td><td>282.40 <b>(+31.66%)</b></td><td>119.59 (+4.67%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>514.20 (n/a)</td><td>322.80 (n/a)</td><td>308.60 (n/a)</td><td>214.50 (n/a)</td><td>114.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (+17.95%)</td><td>0.06 <b>(+38.36%)</b></td><td>0.07 <b>(+92.05%)</b></td><td>0.04 (+17.39%)</td><td>0.02 (-7.62%)</td><td>499.00 (-14.82%)</td><td>315.92 <b>(-30.33%)</b></td><td>279.30 <b>(-47.92%)</b></td><td>229.40 (-15.19%)</td><td>105.39 <b>(-29.72%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.80 (n/a)</td><td>453.48 (n/a)</td><td>536.30 (n/a)</td><td>270.50 (n/a)</td><td>149.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 (+16.62%)</td><td>0.04 <b>(-28.85%)</b></td><td>0.04 <b>(-48.87%)</b></td><td>0.02 <b>(-50.98%)</b></td><td>0.03 <b>(+47.31%)</b></td><td>1049.10 <b>(+103.99%)</b></td><td>559.90 <b>(+65.94%)</b></td><td>514.70 <b>(+95.55%)</b></td><td>218.80 (-14.23%)</td><td>302.99 <b>(+161.76%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>514.30 (n/a)</td><td>337.42 (n/a)</td><td>263.20 (n/a)</td><td>255.10 (n/a)</td><td>115.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.07 (-0.26%)</td><td>0.05 (+15.20%)</td><td>0.05 <b>(+31.32%)</b></td><td>0.04 <b>(+28.56%)</b></td><td>0.01 (-18.53%)</td><td>475.60 <b>(-22.21%)</b></td><td>373.94 (-16.65%)</td><td>381.00 <b>(-23.85%)</b></td><td>264.60 (+0.27%)</td><td>89.97 <b>(-34.96%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.40 (n/a)</td><td>448.66 (n/a)</td><td>500.30 (n/a)</td><td>263.90 (n/a)</td><td>138.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.06 <b>(-25.99%)</b></td><td>0.05 <b>(-21.87%)</b></td><td>0.05 <b>(-30.14%)</b></td><td>0.03 (-3.83%)</td><td>0.01 <b>(-42.55%)</b></td><td>595.50 (+3.98%)</td><td>428.64 <b>(+21.24%)</b></td><td>402.20 <b>(+43.13%)</b></td><td>318.80 <b>(+35.14%)</b></td><td>110.51 <b>(-20.19%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.70 (n/a)</td><td>353.56 (n/a)</td><td>281.00 (n/a)</td><td>235.90 (n/a)</td><td>138.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.34 (-9.14%)</td><td>0.18 <b>(-41.86%)</b></td><td>0.18 <b>(-44.24%)</b></td><td>0.05 <b>(-78.92%)</b></td><td>0.11 <b>(+126.45%)</b></td><td>1912.30 <b>(+374.28%)</b></td><td>789.78 <b>(+148.67%)</b></td><td>548.20 <b>(+79.33%)</b></td><td>287.50 (+10.03%)</td><td>647.92 <b>(+1144.50%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>403.20 (n/a)</td><td>317.60 (n/a)</td><td>305.70 (n/a)</td><td>261.30 (n/a)</td><td>52.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.29 (-18.80%)</td><td>0.21 (-6.98%)</td><td>0.20 (-0.85%)</td><td>0.15 <b>(-20.33%)</b></td><td>0.06 (-13.08%)</td><td>672.00 <b>(+25.51%)</b></td><td>506.48 (+8.82%)</td><td>502.90 (+0.86%)</td><td>341.70 <b>(+23.14%)</b></td><td>149.07 <b>(+39.86%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>535.40 (n/a)</td><td>465.44 (n/a)</td><td>498.60 (n/a)</td><td>277.50 (n/a)</td><td>106.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.37 (-7.49%)</td><td>0.26 (-7.62%)</td><td>0.23 <b>(-22.89%)</b></td><td>0.18 (-3.14%)</td><td>0.08 (-8.91%)</td><td>546.10 (+3.23%)</td><td>410.42 (+7.21%)</td><td>436.20 <b>(+29.67%)</b></td><td>268.30 (+8.10%)</td><td>117.94 (-3.93%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>529.00 (n/a)</td><td>382.82 (n/a)</td><td>336.40 (n/a)</td><td>248.20 (n/a)</td><td>122.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 (-0.74%)</td><td>0.19 (-11.22%)</td><td>0.20 (-15.34%)</td><td>0.09 <b>(-24.71%)</b></td><td>0.09 (+6.48%)</td><td>815.80 <b>(+32.84%)</b></td><td>469.40 <b>(+20.08%)</b></td><td>374.30 (+18.11%)</td><td>239.90 (+0.76%)</td><td>244.61 <b>(+43.68%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>614.10 (n/a)</td><td>390.92 (n/a)</td><td>316.90 (n/a)</td><td>238.10 (n/a)</td><td>170.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.43 <b>(+39.73%)</b></td><td>0.19 (-11.07%)</td><td>0.16 <b>(-32.52%)</b></td><td>0.07 <b>(-43.44%)</b></td><td>0.14 <b>(+94.65%)</b></td><td>1057.20 <b>(+76.82%)</b></td><td>542.72 <b>(+42.92%)</b></td><td>464.80 <b>(+48.17%)</b></td><td>171.20 <b>(-28.43%)</b></td><td>325.81 <b>(+128.48%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>597.90 (n/a)</td><td>379.74 (n/a)</td><td>313.70 (n/a)</td><td>239.20 (n/a)</td><td>142.60 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.31 <b>(+93.11%)</b></td><td>0.21 <b>(+52.40%)</b></td><td>0.23 <b>(+57.16%)</b></td><td>0.07 <b>(-35.91%)</b></td><td>0.11 <b>(+353.05%)</b></td><td>1064.80 <b>(+56.01%)</b></td><td>484.04 (-12.33%)</td><td>326.30 <b>(-36.38%)</b></td><td>236.60 <b>(-48.23%)</b></td><td>348.18 <b>(+252.44%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>682.50 (n/a)</td><td>552.10 (n/a)</td><td>512.90 (n/a)</td><td>457.00 (n/a)</td><td>98.79 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (+13.37%)</td><td>0.10 <b>(+30.31%)</b></td><td>0.12 <b>(+72.88%)</b></td><td>0.05 (-9.41%)</td><td>0.04 <b>(+52.27%)</b></td><td>734.80 (+10.38%)</td><td>418.74 (-16.63%)</td><td>303.10 <b>(-42.17%)</b></td><td>269.00 (-11.80%)</td><td>199.92 <b>(+52.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>665.70 (n/a)</td><td>502.28 (n/a)</td><td>524.10 (n/a)</td><td>305.00 (n/a)</td><td>130.84 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (-2.65%)</td><td>0.10 <b>(+29.53%)</b></td><td>0.11 <b>(+44.91%)</b></td><td>0.06 <b>(+26.69%)</b></td><td>0.02 <b>(-24.20%)</b></td><td>591.20 <b>(-21.07%)</b></td><td>384.32 <b>(-27.50%)</b></td><td>344.40 <b>(-31.00%)</b></td><td>291.60 (+2.71%)</td><td>120.42 <b>(-38.11%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>749.00 (n/a)</td><td>530.10 (n/a)</td><td>499.10 (n/a)</td><td>283.90 (n/a)</td><td>194.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 <b>(-22.95%)</b></td><td>0.10 (+4.49%)</td><td>0.08 (+1.08%)</td><td>0.06 <b>(+40.67%)</b></td><td>0.03 <b>(-34.40%)</b></td><td>582.00 <b>(-28.91%)</b></td><td>416.74 (-15.38%)</td><td>469.80 (-1.05%)</td><td>273.40 <b>(+29.82%)</b></td><td>135.52 <b>(-42.55%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>818.70 (n/a)</td><td>492.46 (n/a)</td><td>474.80 (n/a)</td><td>210.60 (n/a)</td><td>235.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.17 <b>(+53.36%)</b></td><td>0.10 <b>(+25.10%)</b></td><td>0.09 (+15.31%)</td><td>0.07 (-0.48%)</td><td>0.04 <b>(+170.99%)</b></td><td>499.80 (+0.48%)</td><td>388.74 (-13.79%)</td><td>421.10 (-13.28%)</td><td>221.40 <b>(-34.81%)</b></td><td>120.81 <b>(+83.77%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>497.40 (n/a)</td><td>450.92 (n/a)</td><td>485.60 (n/a)</td><td>339.60 (n/a)</td><td>65.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.11 (-19.01%)</td><td>0.08 (-14.45%)</td><td>0.09 (-9.78%)</td><td>0.05 (-13.07%)</td><td>0.02 (-13.54%)</td><td>675.90 (+15.03%)</td><td>487.90 (+17.59%)</td><td>432.80 (+10.83%)</td><td>341.10 <b>(+23.50%)</b></td><td>147.09 <b>(+24.42%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.60 (n/a)</td><td>414.90 (n/a)</td><td>390.50 (n/a)</td><td>276.20 (n/a)</td><td>118.23 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (-2.63%)</td><td>0.09 (-11.47%)</td><td>0.08 <b>(-22.40%)</b></td><td>0.06 (-9.81%)</td><td>0.03 (-3.64%)</td><td>589.80 (+10.89%)</td><td>435.76 (+12.25%)</td><td>457.50 <b>(+28.87%)</b></td><td>242.00 (+2.72%)</td><td>125.71 (-2.51%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>531.90 (n/a)</td><td>388.20 (n/a)</td><td>355.00 (n/a)</td><td>235.60 (n/a)</td><td>128.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (-17.69%)</td><td>0.11 (-1.30%)</td><td>0.13 <b>(+54.77%)</b></td><td>0.08 (-3.12%)</td><td>0.03 <b>(-30.16%)</b></td><td>512.30 (+3.22%)</td><td>383.74 (-2.48%)</td><td>307.80 <b>(-35.39%)</b></td><td>294.90 <b>(+21.46%)</b></td><td>110.75 (-13.04%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>496.30 (n/a)</td><td>393.50 (n/a)</td><td>476.40 (n/a)</td><td>242.80 (n/a)</td><td>127.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.09 <b>(-36.66%)</b></td><td>0.08 <b>(-33.52%)</b></td><td>0.07 <b>(-43.96%)</b></td><td>0.06 <b>(-25.66%)</b></td><td>0.01 <b>(-56.51%)</b></td><td>686.90 <b>(+34.53%)</b></td><td>556.96 <b>(+45.13%)</b></td><td>571.60 <b>(+78.40%)</b></td><td>460.10 <b>(+57.89%)</b></td><td>94.32 (-11.85%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>510.60 (n/a)</td><td>383.76 (n/a)</td><td>320.40 (n/a)</td><td>291.40 (n/a)</td><td>107.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.16 (+6.58%)</td><td>0.07 <b>(-22.02%)</b></td><td>0.07 <b>(-22.58%)</b></td><td>0.02 <b>(-75.10%)</b></td><td>0.05 <b>(+67.31%)</b></td><td>2496.40 <b>(+301.67%)</b></td><td>951.46 <b>(+104.35%)</b></td><td>595.60 <b>(+29.17%)</b></td><td>259.90 (-6.17%)</td><td>893.26 <b>(+602.20%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>621.50 (n/a)</td><td>465.60 (n/a)</td><td>461.10 (n/a)</td><td>277.00 (n/a)</td><td>127.21 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (-5.38%)</td><td>0.10 (-8.28%)</td><td>0.09 (-13.74%)</td><td>0.07 <b>(+47.95%)</b></td><td>0.03 <b>(-25.36%)</b></td><td>554.50 <b>(-32.41%)</b></td><td>452.60 (-1.08%)</td><td>468.80 (+15.92%)</td><td>265.30 (+5.70%)</td><td>110.93 <b>(-50.45%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>820.40 (n/a)</td><td>457.56 (n/a)</td><td>404.40 (n/a)</td><td>251.00 (n/a)</td><td>223.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.10 <b>(-42.98%)</b></td><td>0.08 <b>(-26.03%)</b></td><td>0.08 (+3.47%)</td><td>0.06 (-16.84%)</td><td>0.02 <b>(-64.47%)</b></td><td>728.90 <b>(+20.24%)</b></td><td>545.44 <b>(+20.89%)</b></td><td>509.10 (-3.36%)</td><td>402.50 <b>(+75.38%)</b></td><td>127.65 <b>(-27.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>606.20 (n/a)</td><td>451.20 (n/a)</td><td>526.80 (n/a)</td><td>229.50 (n/a)</td><td>174.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 <b>(-22.35%)</b></td><td>0.10 (-8.27%)</td><td>0.10 (+12.37%)</td><td>0.07 (+15.30%)</td><td>0.03 <b>(-44.35%)</b></td><td>607.80 (-13.27%)</td><td>445.38 (-2.73%)</td><td>429.60 (-11.02%)</td><td>281.20 <b>(+28.81%)</b></td><td>122.54 <b>(-38.09%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>700.80 (n/a)</td><td>457.90 (n/a)</td><td>482.80 (n/a)</td><td>218.30 (n/a)</td><td>197.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (-0.40%)</td><td>0.09 (-19.85%)</td><td>0.07 <b>(-44.12%)</b></td><td>0.07 <b>(+386.32%)</b></td><td>0.03 <b>(-41.11%)</b></td><td>509.90 <b>(-79.44%)</b></td><td>433.44 <b>(-38.78%)</b></td><td>495.30 <b>(+78.94%)</b></td><td>246.00 (+0.41%)</td><td>113.22 <b>(-88.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2479.60 (n/a)</td><td>707.98 (n/a)</td><td>276.80 (n/a)</td><td>245.00 (n/a)</td><td>990.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (-11.67%)</td><td>0.09 (+3.99%)</td><td>0.08 (+9.60%)</td><td>0.06 <b>(+102.52%)</b></td><td>0.03 <b>(-38.58%)</b></td><td>544.00 <b>(-50.62%)</b></td><td>426.76 <b>(-20.66%)</b></td><td>461.20 (-8.76%)</td><td>301.90 (+13.20%)</td><td>117.00 <b>(-65.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1101.70 (n/a)</td><td>537.88 (n/a)</td><td>505.50 (n/a)</td><td>266.70 (n/a)</td><td>338.05 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 <b>(-29.65%)</b></td><td>0.05 <b>(-37.73%)</b></td><td>0.07 (-9.78%)</td><td>0.02 <b>(-70.41%)</b></td><td>0.03 <b>(+25.52%)</b></td><td>2045.40 <b>(+237.92%)</b></td><td>1047.02 <b>(+145.12%)</b></td><td>481.30 (+10.82%)</td><td>416.20 <b>(+42.14%)</b></td><td>834.77 <b>(+531.83%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>605.30 (n/a)</td><td>427.14 (n/a)</td><td>434.30 (n/a)</td><td>292.80 (n/a)</td><td>132.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.15 (+16.54%)</td><td>0.07 (-19.42%)</td><td>0.07 (-9.91%)</td><td>0.02 <b>(-69.62%)</b></td><td>0.05 <b>(+50.88%)</b></td><td>1911.70 <b>(+229.15%)</b></td><td>747.68 <b>(+76.44%)</b></td><td>526.70 (+11.00%)</td><td>238.00 (-14.17%)</td><td>662.99 <b>(+394.19%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.80 (n/a)</td><td>423.76 (n/a)</td><td>474.50 (n/a)</td><td>277.30 (n/a)</td><td>134.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (+0.88%)</td><td>0.08 (+7.30%)</td><td>0.08 (+14.91%)</td><td>0.03 <b>(-55.10%)</b></td><td>0.04 <b>(+41.31%)</b></td><td>1378.70 <b>(+122.73%)</b></td><td>602.66 (+19.41%)</td><td>463.30 (-12.98%)</td><td>265.80 (-0.86%)</td><td>454.88 <b>(+231.98%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>619.00 (n/a)</td><td>504.68 (n/a)</td><td>532.40 (n/a)</td><td>268.10 (n/a)</td><td>137.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.12 (-13.59%)</td><td>0.09 (+9.00%)</td><td>0.08 (+11.09%)</td><td>0.06 (+5.06%)</td><td>0.03 (-16.61%)</td><td>576.00 (-4.82%)</td><td>420.52 (-9.82%)</td><td>427.60 (-10.00%)</td><td>296.40 (+15.74%)</td><td>121.80 (-5.68%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>605.20 (n/a)</td><td>466.30 (n/a)</td><td>475.10 (n/a)</td><td>256.10 (n/a)</td><td>129.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.46 <b>(+73.59%)</b></td><td>0.28 (+19.90%)</td><td>0.24 (+0.21%)</td><td>0.21 (+4.86%)</td><td>0.10 <b>(+313.12%)</b></td><td>635.30 (-4.64%)</td><td>505.62 (-10.36%)</td><td>556.70 (-0.20%)</td><td>284.60 <b>(-42.39%)</b></td><td>137.13 <b>(+114.56%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>666.20 (n/a)</td><td>564.08 (n/a)</td><td>557.80 (n/a)</td><td>494.00 (n/a)</td><td>63.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.39 (-12.50%)</td><td>0.28 (-4.46%)</td><td>0.22 (-0.39%)</td><td>0.20 (-1.57%)</td><td>0.10 (-11.37%)</td><td>643.30 (+1.60%)</td><td>510.52 (+3.47%)</td><td>598.20 (+0.39%)</td><td>336.10 (+14.28%)</td><td>159.30 (-0.94%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>633.20 (n/a)</td><td>493.42 (n/a)</td><td>595.90 (n/a)</td><td>294.10 (n/a)</td><td>160.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.44 (+6.31%)</td><td>0.27 (+3.35%)</td><td>0.24 (+0.85%)</td><td>0.21 (+4.63%)</td><td>0.09 (+10.45%)</td><td>612.30 (-4.43%)</td><td>515.18 (-2.60%)</td><td>553.00 (-0.84%)</td><td>297.90 (-5.94%)</td><td>128.89 (-0.08%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>640.70 (n/a)</td><td>528.92 (n/a)</td><td>557.70 (n/a)</td><td>316.70 (n/a)</td><td>128.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.00 <b>(-57.14%)</b></td><td>0.00 <b>(-45.00%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-80.93%)</b></td><td>17570.16 (-19.92%)</td><td>16801.02 <b>(+24.52%)</b></td><td>17395.01 <b>(+21.48%)</b></td><td>14761.21 <b>(+155.66%)</b></td><td>1170.51 <b>(-83.21%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21941.42 (n/a)</td><td>13493.07 (n/a)</td><td>14319.57 (n/a)</td><td>5773.77 (n/a)</td><td>6970.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.00 (+0.00%)</td><td>0.00 (-3.03%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+14.56%)</td><td>20931.46 (+9.33%)</td><td>14297.45 (+8.11%)</td><td>15063.24 (+15.63%)</td><td>7968.39 (+0.84%)</td><td>5387.25 <b>(+33.59%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19144.65 (n/a)</td><td>13224.53 (n/a)</td><td>13027.28 (n/a)</td><td>7901.79 (n/a)</td><td>4032.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (+12.14%)</td><td>0.09 (-0.88%)</td><td>0.09 (+4.71%)</td><td>0.07 (-13.93%)</td><td>0.03 <b>(+61.12%)</b></td><td>30553.66 (+16.08%)</td><td>23605.34 (+4.89%)</td><td>23005.57 (-4.49%)</td><td>15130.45 (-10.82%)</td><td>6201.44 <b>(+70.93%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>26321.51 (n/a)</td><td>22505.83 (n/a)</td><td>24086.19 (n/a)</td><td>16966.30 (n/a)</td><td>3628.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.10 (+17.23%)</td><td>1.46 (-15.33%)</td><td>0.55 <b>(-63.96%)</b></td><td>0.30 <b>(-71.97%)</b></td><td>1.43 <b>(+138.69%)</b></td><td>3444.80 <b>(+256.72%)</b></td><td>1703.94 <b>(+157.01%)</b></td><td>1904.10 <b>(+177.44%)</b></td><td>338.80 (-14.70%)</td><td>1355.57 <b>(+531.59%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.64 (n/a)</td><td>1.73 (n/a)</td><td>1.53 (n/a)</td><td>1.09 (n/a)</td><td>0.60 (n/a)</td><td>965.70 (n/a)</td><td>662.98 (n/a)</td><td>686.30 (n/a)</td><td>397.20 (n/a)</td><td>214.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.99 (-11.12%)</td><td>1.85 (+2.74%)</td><td>2.01 (+8.60%)</td><td>0.30 (+1.85%)</td><td>1.04 (-12.21%)</td><td>3490.50 (-1.82%)</td><td>1102.38 (-5.68%)</td><td>521.80 (-7.92%)</td><td>350.50 (+12.48%)</td><td>1342.66 (-1.06%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.37 (n/a)</td><td>1.80 (n/a)</td><td>1.85 (n/a)</td><td>0.29 (n/a)</td><td>1.18 (n/a)</td><td>3555.10 (n/a)</td><td>1168.82 (n/a)</td><td>566.70 (n/a)</td><td>311.60 (n/a)</td><td>1357.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.18 <b>(-36.73%)</b></td><td>1.40 <b>(-38.80%)</b></td><td>1.74 (-17.82%)</td><td>0.30 <b>(-79.84%)</b></td><td>0.75 (-0.61%)</td><td>3476.70 <b>(+395.96%)</b></td><td>1239.38 <b>(+149.59%)</b></td><td>602.80 <b>(+21.68%)</b></td><td>480.10 <b>(+58.03%)</b></td><td>1269.26 <b>(+743.69%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.45 (n/a)</td><td>2.29 (n/a)</td><td>2.12 (n/a)</td><td>1.50 (n/a)</td><td>0.75 (n/a)</td><td>701.00 (n/a)</td><td>496.56 (n/a)</td><td>495.40 (n/a)</td><td>303.80 (n/a)</td><td>150.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.71 <b>(+26.93%)</b></td><td>2.42 (+8.25%)</td><td>2.57 <b>(+20.64%)</b></td><td>1.46 (-17.36%)</td><td>0.90 <b>(+93.16%)</b></td><td>717.50 <b>(+21.02%)</b></td><td>484.64 (+0.01%)</td><td>407.30 (-17.11%)</td><td>282.40 <b>(-21.21%)</b></td><td>179.11 <b>(+90.53%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.93 (n/a)</td><td>2.24 (n/a)</td><td>2.13 (n/a)</td><td>1.77 (n/a)</td><td>0.46 (n/a)</td><td>592.90 (n/a)</td><td>484.58 (n/a)</td><td>491.40 (n/a)</td><td>358.40 (n/a)</td><td>94.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.91 (+8.88%)</td><td>3.13 <b>(+22.18%)</b></td><td>3.19 (-0.56%)</td><td>2.05 <b>(+251.71%)</b></td><td>0.79 <b>(-37.88%)</b></td><td>1023.50 <b>(-71.57%)</b></td><td>710.30 <b>(-45.42%)</b></td><td>656.60 (+0.57%)</td><td>537.00 (-8.14%)</td><td>203.15 <b>(-84.37%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.59 (n/a)</td><td>2.56 (n/a)</td><td>3.21 (n/a)</td><td>0.58 (n/a)</td><td>1.28 (n/a)</td><td>3599.60 (n/a)</td><td>1301.36 (n/a)</td><td>652.90 (n/a)</td><td>584.60 (n/a)</td><td>1299.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.34 (+8.10%)</td><td>2.93 (+13.03%)</td><td>2.96 (+6.64%)</td><td>1.90 <b>(+87.95%)</b></td><td>1.04 (-15.76%)</td><td>1105.50 <b>(-46.79%)</b></td><td>793.36 <b>(-23.59%)</b></td><td>708.40 (-6.22%)</td><td>483.50 (-7.48%)</td><td>282.48 <b>(-56.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>4.01 (n/a)</td><td>2.60 (n/a)</td><td>2.78 (n/a)</td><td>1.01 (n/a)</td><td>1.24 (n/a)</td><td>2077.70 (n/a)</td><td>1038.28 (n/a)</td><td>755.40 (n/a)</td><td>522.60 (n/a)</td><td>643.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.18 (-14.18%)</td><td>2.17 <b>(-34.03%)</b></td><td>2.21 <b>(-20.00%)</b></td><td>0.58 <b>(-70.80%)</b></td><td>1.58 <b>(+32.62%)</b></td><td>3604.20 <b>(+242.44%)</b></td><td>1788.48 <b>(+152.30%)</b></td><td>948.00 <b>(+25.00%)</b></td><td>502.10 (+16.52%)</td><td>1503.08 <b>(+503.50%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>4.87 (n/a)</td><td>3.28 (n/a)</td><td>2.77 (n/a)</td><td>1.99 (n/a)</td><td>1.19 (n/a)</td><td>1052.50 (n/a)</td><td>708.88 (n/a)</td><td>758.40 (n/a)</td><td>430.90 (n/a)</td><td>249.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>4.99 <b>(+39.41%)</b></td><td>3.47 <b>(+28.57%)</b></td><td>3.54 (+16.23%)</td><td>2.16 <b>(+78.33%)</b></td><td>1.04 (+4.30%)</td><td>971.80 <b>(-43.93%)</b></td><td>651.06 <b>(-28.72%)</b></td><td>591.70 (-13.96%)</td><td>420.00 <b>(-28.28%)</b></td><td>204.90 <b>(-57.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.58 (n/a)</td><td>2.70 (n/a)</td><td>3.05 (n/a)</td><td>1.21 (n/a)</td><td>0.99 (n/a)</td><td>1733.10 (n/a)</td><td>913.36 (n/a)</td><td>687.70 (n/a)</td><td>585.60 (n/a)</td><td>481.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>8.00 <b>(+37.42%)</b></td><td>3.23 (-17.48%)</td><td>2.82 (-16.04%)</td><td>0.58 <b>(-80.37%)</b></td><td>3.07 <b>(+162.82%)</b></td><td>3597.00 <b>(+409.49%)</b></td><td>1729.00 <b>(+204.11%)</b></td><td>744.50 (+19.10%)</td><td>262.10 <b>(-27.23%)</b></td><td>1686.95 <b>(+1102.97%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.82 (n/a)</td><td>3.92 (n/a)</td><td>3.35 (n/a)</td><td>2.97 (n/a)</td><td>1.17 (n/a)</td><td>706.00 (n/a)</td><td>568.54 (n/a)</td><td>625.10 (n/a)</td><td>360.20 (n/a)</td><td>140.23 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.51 <b>(-41.94%)</b></td><td>2.44 <b>(-37.82%)</b></td><td>2.75 <b>(-32.95%)</b></td><td>0.58 <b>(-76.94%)</b></td><td>1.11 <b>(-21.79%)</b></td><td>3608.90 <b>(+333.61%)</b></td><td>1307.28 <b>(+121.69%)</b></td><td>761.70 <b>(+49.15%)</b></td><td>596.70 <b>(+72.26%)</b></td><td>1289.60 <b>(+539.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>6.05 (n/a)</td><td>3.93 (n/a)</td><td>4.11 (n/a)</td><td>2.52 (n/a)</td><td>1.41 (n/a)</td><td>832.30 (n/a)</td><td>589.68 (n/a)</td><td>510.70 (n/a)</td><td>346.40 (n/a)</td><td>201.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.47 (+7.13%)</td><td>2.73 <b>(-30.08%)</b></td><td>1.75 <b>(-57.22%)</b></td><td>1.20 <b>(-40.58%)</b></td><td>1.91 <b>(+66.34%)</b></td><td>3501.30 <b>(+68.31%)</b></td><td>2205.20 <b>(+85.52%)</b></td><td>2390.10 <b>(+133.77%)</b></td><td>766.40 (-6.65%)</td><td>1258.54 <b>(+148.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.11 (n/a)</td><td>3.91 (n/a)</td><td>4.10 (n/a)</td><td>2.02 (n/a)</td><td>1.15 (n/a)</td><td>2080.30 (n/a)</td><td>1188.68 (n/a)</td><td>1022.40 (n/a)</td><td>821.00 (n/a)</td><td>506.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>5.75 <b>(-32.20%)</b></td><td>4.22 <b>(-21.30%)</b></td><td>4.73 (-18.62%)</td><td>2.05 <b>(+92.85%)</b></td><td>1.60 <b>(-46.00%)</b></td><td>2041.70 <b>(-48.15%)</b></td><td>1157.68 (-14.65%)</td><td>887.20 <b>(+22.88%)</b></td><td>729.50 <b>(+47.46%)</b></td><td>556.80 <b>(-61.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>8.48 (n/a)</td><td>5.36 (n/a)</td><td>5.81 (n/a)</td><td>1.07 (n/a)</td><td>2.97 (n/a)</td><td>3937.50 (n/a)</td><td>1356.42 (n/a)</td><td>722.00 (n/a)</td><td>494.70 (n/a)</td><td>1460.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>7.94 (+3.68%)</td><td>6.09 <b>(+48.53%)</b></td><td>5.97 <b>(+64.47%)</b></td><td>3.85 <b>(+225.03%)</b></td><td>1.56 <b>(-41.89%)</b></td><td>1090.40 <b>(-69.23%)</b></td><td>732.04 <b>(-54.01%)</b></td><td>702.50 <b>(-39.20%)</b></td><td>528.10 (-3.54%)</td><td>218.63 <b>(-82.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.66 (n/a)</td><td>4.10 (n/a)</td><td>3.63 (n/a)</td><td>1.18 (n/a)</td><td>2.69 (n/a)</td><td>3544.20 (n/a)</td><td>1591.78 (n/a)</td><td>1155.40 (n/a)</td><td>547.50 (n/a)</td><td>1229.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>6.97 <b>(-25.82%)</b></td><td>4.04 <b>(-32.53%)</b></td><td>4.72 <b>(-29.08%)</b></td><td>1.24 (+13.01%)</td><td>2.50 <b>(-21.92%)</b></td><td>3389.70 (-11.51%)</td><td>1633.62 <b>(+29.58%)</b></td><td>888.00 <b>(+41.00%)</b></td><td>601.40 <b>(+34.81%)</b></td><td>1255.78 (-13.11%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>9.40 (n/a)</td><td>5.98 (n/a)</td><td>6.66 (n/a)</td><td>1.09 (n/a)</td><td>3.21 (n/a)</td><td>3830.60 (n/a)</td><td>1260.68 (n/a)</td><td>629.80 (n/a)</td><td>446.10 (n/a)</td><td>1445.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>10.85 (+12.77%)</td><td>5.99 (-3.21%)</td><td>4.53 (-19.51%)</td><td>2.19 <b>(-51.86%)</b></td><td>3.51 <b>(+73.58%)</b></td><td>1911.10 <b>(+107.73%)</b></td><td>952.12 <b>(+31.20%)</b></td><td>926.20 <b>(+24.22%)</b></td><td>386.60 (-11.31%)</td><td>601.37 <b>(+221.10%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>9.62 (n/a)</td><td>6.19 (n/a)</td><td>5.63 (n/a)</td><td>4.56 (n/a)</td><td>2.02 (n/a)</td><td>920.00 (n/a)</td><td>725.70 (n/a)</td><td>745.60 (n/a)</td><td>435.90 (n/a)</td><td>187.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>9.81 <b>(+23.32%)</b></td><td>7.20 (+12.05%)</td><td>7.67 (+10.23%)</td><td>3.96 (-1.74%)</td><td>2.12 <b>(+24.14%)</b></td><td>1058.60 (+1.78%)</td><td>638.22 (-8.65%)</td><td>546.50 (-9.29%)</td><td>427.70 (-18.90%)</td><td>244.84 (+11.98%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.95 (n/a)</td><td>6.43 (n/a)</td><td>6.96 (n/a)</td><td>4.03 (n/a)</td><td>1.71 (n/a)</td><td>1040.10 (n/a)</td><td>698.64 (n/a)</td><td>602.50 (n/a)</td><td>527.40 (n/a)</td><td>218.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>1.64 (-0.92%)</td><td>1.19 (+12.70%)</td><td>1.58 <b>(+66.25%)</b></td><td>0.15 (-2.77%)</td><td>0.65 (+6.67%)</td><td>3383.90 (+2.84%)</td><td>984.04 (-2.84%)</td><td>331.00 <b>(-39.84%)</b></td><td>319.70 (+0.92%)</td><td>1345.54 (+5.21%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>1.65 (n/a)</td><td>1.05 (n/a)</td><td>0.95 (n/a)</td><td>0.16 (n/a)</td><td>0.61 (n/a)</td><td>3290.30 (n/a)</td><td>1012.80 (n/a)</td><td>550.20 (n/a)</td><td>316.80 (n/a)</td><td>1278.88 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.59 (-6.11%)</td><td>1.33 (-13.29%)</td><td>1.63 (-13.86%)</td><td>0.29 (-0.06%)</td><td>1.01 (-13.14%)</td><td>3562.20 (+0.06%)</td><td>1736.58 (+5.34%)</td><td>644.90 (+16.07%)</td><td>404.20 (+6.51%)</td><td>1637.56 (+0.26%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.76 (n/a)</td><td>1.53 (n/a)</td><td>1.89 (n/a)</td><td>0.29 (n/a)</td><td>1.16 (n/a)</td><td>3560.10 (n/a)</td><td>1648.58 (n/a)</td><td>555.60 (n/a)</td><td>379.50 (n/a)</td><td>1633.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>3.34 (-9.37%)</td><td>1.22 <b>(-22.53%)</b></td><td>0.67 (+5.73%)</td><td>0.60 (+3.44%)</td><td>1.19 (-15.57%)</td><td>3509.60 (-3.32%)</td><td>2613.22 (+10.33%)</td><td>3145.50 (-5.42%)</td><td>628.60 (+10.34%)</td><td>1211.47 (-19.77%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.68 (n/a)</td><td>1.58 (n/a)</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>1.41 (n/a)</td><td>3630.20 (n/a)</td><td>2368.52 (n/a)</td><td>3325.70 (n/a)</td><td>569.70 (n/a)</td><td>1509.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>2.19 (-4.31%)</td><td>1.40 (-0.80%)</td><td>1.47 (-1.71%)</td><td>0.83 (+16.73%)</td><td>0.53 <b>(-22.62%)</b></td><td>630.30 (-14.34%)</td><td>419.44 (-9.11%)</td><td>355.50 (+1.75%)</td><td>239.10 (+4.50%)</td><td>153.90 <b>(-35.53%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.29 (n/a)</td><td>1.41 (n/a)</td><td>1.50 (n/a)</td><td>0.71 (n/a)</td><td>0.68 (n/a)</td><td>735.80 (n/a)</td><td>461.48 (n/a)</td><td>349.40 (n/a)</td><td>228.80 (n/a)</td><td>238.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.14 (+6.91%)</td><td>0.08 (-9.35%)</td><td>0.07 (-13.93%)</td><td>0.05 (-17.11%)</td><td>0.03 (+13.27%)</td><td>659.70 <b>(+20.65%)</b></td><td>453.10 (+13.20%)</td><td>467.10 (+16.19%)</td><td>239.00 (-6.46%)</td><td>152.93 <b>(+20.99%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>546.80 (n/a)</td><td>400.26 (n/a)</td><td>402.00 (n/a)</td><td>255.50 (n/a)</td><td>126.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.13 (-1.33%)</td><td>0.07 <b>(-28.23%)</b></td><td>0.05 <b>(-51.51%)</b></td><td>0.05 (-7.30%)</td><td>0.03 (+0.76%)</td><td>652.30 (+7.89%)</td><td>542.04 <b>(+40.49%)</b></td><td>614.20 <b>(+106.18%)</b></td><td>255.00 (+1.35%)</td><td>165.43 (+6.15%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>604.60 (n/a)</td><td>385.82 (n/a)</td><td>297.90 (n/a)</td><td>251.60 (n/a)</td><td>155.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.23 (+10.44%)</td><td>0.14 <b>(+20.58%)</b></td><td>0.12 (+11.52%)</td><td>0.11 <b>(+235.56%)</b></td><td>0.05 (-19.96%)</td><td>614.00 <b>(-70.20%)</b></td><td>497.22 <b>(-39.39%)</b></td><td>561.00 (-10.34%)</td><td>279.20 (-9.47%)</td><td>132.78 <b>(-81.21%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>2060.30 (n/a)</td><td>820.34 (n/a)</td><td>625.70 (n/a)</td><td>308.40 (n/a)</td><td>706.52 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.29 <b>(+65.39%)</b></td><td>0.19 <b>(+32.17%)</b></td><td>0.15 (+11.97%)</td><td>0.14 <b>(+27.62%)</b></td><td>0.07 <b>(+133.98%)</b></td><td>483.80 <b>(-21.64%)</b></td><td>379.96 <b>(-20.13%)</b></td><td>443.90 (-10.68%)</td><td>223.00 <b>(-39.55%)</b></td><td>112.93 (+14.25%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>617.40 (n/a)</td><td>475.74 (n/a)</td><td>497.00 (n/a)</td><td>368.90 (n/a)</td><td>98.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.20 <b>(-42.83%)</b></td><td>0.13 <b>(-35.01%)</b></td><td>0.11 <b>(-36.69%)</b></td><td>0.09 <b>(-30.82%)</b></td><td>0.05 <b>(-47.90%)</b></td><td>735.20 <b>(+44.55%)</b></td><td>550.98 <b>(+48.71%)</b></td><td>596.10 <b>(+57.95%)</b></td><td>330.20 <b>(+74.89%)</b></td><td>169.86 <b>(+33.58%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>508.60 (n/a)</td><td>370.50 (n/a)</td><td>377.40 (n/a)</td><td>188.80 (n/a)</td><td>127.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.52 (-4.63%)</td><td>0.42 (+8.44%)</td><td>0.42 (-3.89%)</td><td>0.28 (+17.85%)</td><td>0.09 <b>(-32.90%)</b></td><td>462.80 (-15.14%)</td><td>327.40 (-13.04%)</td><td>313.10 (+4.05%)</td><td>251.40 (+4.84%)</td><td>80.25 <b>(-40.51%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.44 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>545.40 (n/a)</td><td>376.48 (n/a)</td><td>300.90 (n/a)</td><td>239.80 (n/a)</td><td>134.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.46 <b>(-20.41%)</b></td><td>0.32 (-15.38%)</td><td>0.27 <b>(-28.77%)</b></td><td>0.23 (+12.03%)</td><td>0.09 <b>(-38.59%)</b></td><td>558.50 (-10.74%)</td><td>439.42 (+9.80%)</td><td>476.80 <b>(+40.36%)</b></td><td>285.20 <b>(+25.64%)</b></td><td>105.82 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.58 (n/a)</td><td>0.37 (n/a)</td><td>0.39 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>625.70 (n/a)</td><td>400.20 (n/a)</td><td>339.70 (n/a)</td><td>227.00 (n/a)</td><td>161.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.49 (-0.37%)</td><td>0.38 <b>(+23.64%)</b></td><td>0.35 <b>(+27.94%)</b></td><td>0.28 <b>(+31.79%)</b></td><td>0.10 (-13.19%)</td><td>475.00 <b>(-24.11%)</b></td><td>366.30 <b>(-21.59%)</b></td><td>372.00 <b>(-21.85%)</b></td><td>265.30 (+0.38%)</td><td>91.49 <b>(-30.69%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.50 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>625.90 (n/a)</td><td>467.18 (n/a)</td><td>476.00 (n/a)</td><td>264.30 (n/a)</td><td>132.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:40:14</td><td>0.08 <b>(+48.16%)</b></td><td>0.05 <b>(+27.09%)</b></td><td>0.04 (+5.05%)</td><td>0.03 (+14.47%)</td><td>0.02 <b>(+80.18%)</b></td><td>561.20 (-12.64%)</td><td>402.50 (-16.17%)</td><td>460.40 (-4.82%)</td><td>200.20 <b>(-32.52%)</b></td><td>148.08 (+4.44%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>642.40 (n/a)</td><td>480.14 (n/a)</td><td>483.70 (n/a)</td><td>296.70 (n/a)</td><td>141.78 (n/a)</td>
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
