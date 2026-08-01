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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-5.14%)</td><td>0.02 <b>(-33.75%)</b></td><td>0.01 <b>(-43.47%)</b></td><td>0.01 <b>(-55.72%)</b></td><td>0.01 <b>(+343.93%)</b></td><td>609.40 <b>(+125.79%)</b></td><td>430.50 <b>(+69.58%)</b></td><td>459.00 <b>(+76.88%)</b></td><td>250.50 (+5.43%)</td><td>155.56 <b>(+949.86%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>269.90 (n/a)</td><td>253.86 (n/a)</td><td>259.50 (n/a)</td><td>237.60 (n/a)</td><td>14.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (+4.90%)</td><td>0.02 (-16.65%)</td><td>0.01 <b>(-40.26%)</b></td><td>0.01 (+12.55%)</td><td>0.01 (-15.15%)</td><td>538.60 (-11.15%)</td><td>435.30 (+13.83%)</td><td>456.80 <b>(+67.39%)</b></td><td>243.20 (-4.70%)</td><td>114.77 <b>(-30.09%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.20 (n/a)</td><td>382.40 (n/a)</td><td>272.90 (n/a)</td><td>255.20 (n/a)</td><td>164.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (+7.14%)</td><td>0.02 (-3.33%)</td><td>0.02 (-5.88%)</td><td>0.01 <b>(-29.00%)</b></td><td>0.01 <b>(+45.68%)</b></td><td>595.80 <b>(+40.82%)</b></td><td>317.10 (+12.38%)</td><td>263.70 (+6.24%)</td><td>221.70 (-6.65%)</td><td>157.31 <b>(+97.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>423.10 (n/a)</td><td>282.18 (n/a)</td><td>248.20 (n/a)</td><td>237.50 (n/a)</td><td>79.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-7.77%)</td><td>0.02 <b>(-26.00%)</b></td><td>0.01 <b>(-34.96%)</b></td><td>0.01 (+5.63%)</td><td>0.01 (-11.19%)</td><td>563.30 (-5.33%)</td><td>438.98 <b>(+31.61%)</b></td><td>441.00 <b>(+53.77%)</b></td><td>255.50 (+8.40%)</td><td>125.44 (-15.08%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.00 (n/a)</td><td>333.54 (n/a)</td><td>286.80 (n/a)</td><td>235.70 (n/a)</td><td>147.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(-26.93%)</b></td><td>0.01 <b>(-32.82%)</b></td><td>0.01 <b>(-32.41%)</b></td><td>0.01 <b>(-39.75%)</b></td><td>0.01 <b>(-28.42%)</b></td><td>1015.60 <b>(+65.97%)</b></td><td>618.48 <b>(+51.52%)</b></td><td>632.10 <b>(+47.96%)</b></td><td>320.70 <b>(+36.88%)</b></td><td>265.51 <b>(+66.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.90 (n/a)</td><td>408.18 (n/a)</td><td>427.20 (n/a)</td><td>234.30 (n/a)</td><td>159.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (+5.12%)</td><td>0.02 (+11.16%)</td><td>0.02 (+15.41%)</td><td>0.01 <b>(+22.75%)</b></td><td>0.00 <b>(-26.54%)</b></td><td>465.10 (-18.55%)</td><td>339.80 (-15.05%)</td><td>306.40 (-13.35%)</td><td>252.40 (-4.86%)</td><td>82.37 <b>(-42.46%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.00 (n/a)</td><td>399.98 (n/a)</td><td>353.60 (n/a)</td><td>265.30 (n/a)</td><td>143.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (-16.13%)</td><td>0.04 (+0.34%)</td><td>0.04 (+1.26%)</td><td>0.03 <b>(+48.58%)</b></td><td>0.01 <b>(-44.11%)</b></td><td>379.90 <b>(-32.70%)</b></td><td>287.48 (-9.27%)</td><td>287.30 (-1.24%)</td><td>233.00 (+19.24%)</td><td>59.52 <b>(-58.70%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>564.50 (n/a)</td><td>316.86 (n/a)</td><td>290.90 (n/a)</td><td>195.40 (n/a)</td><td>144.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(-29.52%)</b></td><td>0.03 <b>(-20.27%)</b></td><td>0.03 <b>(-25.37%)</b></td><td>0.02 (-15.89%)</td><td>0.01 <b>(-32.35%)</b></td><td>676.50 (+18.89%)</td><td>415.30 (+19.86%)</td><td>397.70 <b>(+34.00%)</b></td><td>234.80 <b>(+41.87%)</b></td><td>179.32 (+8.48%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>569.00 (n/a)</td><td>346.48 (n/a)</td><td>296.80 (n/a)</td><td>165.50 (n/a)</td><td>165.30 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (-14.84%)</td><td>0.03 (-17.58%)</td><td>0.03 (-19.56%)</td><td>0.01 <b>(-47.70%)</b></td><td>0.01 (-1.34%)</td><td>991.20 <b>(+91.20%)</b></td><td>497.34 <b>(+34.35%)</b></td><td>433.50 <b>(+24.32%)</b></td><td>269.50 (+17.43%)</td><td>294.16 <b>(+111.82%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.40 (n/a)</td><td>370.18 (n/a)</td><td>348.70 (n/a)</td><td>229.50 (n/a)</td><td>138.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(-39.44%)</b></td><td>0.03 <b>(-24.14%)</b></td><td>0.03 <b>(-32.94%)</b></td><td>0.02 (-1.94%)</td><td>0.01 <b>(-52.23%)</b></td><td>589.60 (+1.99%)</td><td>421.24 (+14.11%)</td><td>432.50 <b>(+49.14%)</b></td><td>277.40 <b>(+65.12%)</b></td><td>133.97 <b>(-30.12%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>578.10 (n/a)</td><td>369.16 (n/a)</td><td>290.00 (n/a)</td><td>168.00 (n/a)</td><td>191.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 <b>(-46.47%)</b></td><td>0.02 <b>(-38.17%)</b></td><td>0.02 <b>(-31.67%)</b></td><td>0.01 <b>(-48.07%)</b></td><td>0.01 <b>(-53.67%)</b></td><td>991.70 <b>(+92.60%)</b></td><td>586.68 <b>(+57.45%)</b></td><td>534.10 <b>(+46.33%)</b></td><td>383.00 <b>(+86.83%)</b></td><td>235.40 <b>(+69.64%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>514.90 (n/a)</td><td>372.62 (n/a)</td><td>365.00 (n/a)</td><td>205.00 (n/a)</td><td>138.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(-30.45%)</b></td><td>0.03 <b>(-20.77%)</b></td><td>0.03 (-15.09%)</td><td>0.02 (-2.99%)</td><td>0.01 <b>(-46.48%)</b></td><td>518.30 (+3.08%)</td><td>383.78 (+19.93%)</td><td>351.40 (+17.76%)</td><td>295.10 <b>(+43.81%)</b></td><td>90.37 <b>(-21.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.80 (n/a)</td><td>320.00 (n/a)</td><td>298.40 (n/a)</td><td>205.20 (n/a)</td><td>114.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (-19.62%)</td><td>0.07 (-3.88%)</td><td>0.07 <b>(+39.96%)</b></td><td>0.04 <b>(+33.62%)</b></td><td>0.03 <b>(-36.35%)</b></td><td>567.10 <b>(-25.16%)</b></td><td>374.56 (-10.22%)</td><td>332.60 <b>(-28.57%)</b></td><td>230.60 <b>(+24.38%)</b></td><td>148.91 <b>(-36.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>757.70 (n/a)</td><td>417.22 (n/a)</td><td>465.60 (n/a)</td><td>185.40 (n/a)</td><td>232.78 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (-1.84%)</td><td>0.07 (-18.52%)</td><td>0.06 <b>(-42.36%)</b></td><td>0.05 (-5.03%)</td><td>0.02 (-5.48%)</td><td>531.30 (+5.29%)</td><td>387.98 <b>(+22.21%)</b></td><td>430.80 <b>(+73.50%)</b></td><td>232.40 (+1.84%)</td><td>120.41 (+1.50%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>504.60 (n/a)</td><td>317.46 (n/a)</td><td>248.30 (n/a)</td><td>228.20 (n/a)</td><td>118.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (+0.07%)</td><td>0.06 (-2.89%)</td><td>0.05 <b>(-22.48%)</b></td><td>0.04 (-8.98%)</td><td>0.03 <b>(+29.55%)</b></td><td>592.70 (+9.86%)</td><td>429.28 (+9.02%)</td><td>485.60 <b>(+29.01%)</b></td><td>246.60 (-0.04%)</td><td>155.84 <b>(+42.26%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>539.50 (n/a)</td><td>393.78 (n/a)</td><td>376.40 (n/a)</td><td>246.70 (n/a)</td><td>109.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 <b>(+25.97%)</b></td><td>0.06 (+0.73%)</td><td>0.04 (-15.49%)</td><td>0.01 <b>(-67.65%)</b></td><td>0.04 <b>(+57.89%)</b></td><td>2098.90 <b>(+209.12%)</b></td><td>749.12 <b>(+56.39%)</b></td><td>564.60 (+18.34%)</td><td>192.10 <b>(-20.62%)</b></td><td>771.66 <b>(+293.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>679.00 (n/a)</td><td>479.02 (n/a)</td><td>477.10 (n/a)</td><td>242.00 (n/a)</td><td>196.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 <b>(-38.78%)</b></td><td>0.06 (+2.40%)</td><td>0.06 <b>(+51.47%)</b></td><td>0.04 (-1.49%)</td><td>0.01 <b>(-58.21%)</b></td><td>635.30 (+1.52%)</td><td>434.96 (-12.62%)</td><td>382.00 <b>(-33.99%)</b></td><td>347.60 <b>(+63.35%)</b></td><td>121.00 <b>(-28.97%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>625.80 (n/a)</td><td>497.76 (n/a)</td><td>578.70 (n/a)</td><td>212.80 (n/a)</td><td>170.35 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 <b>(-24.69%)</b></td><td>0.06 (-4.21%)</td><td>0.05 (+14.72%)</td><td>0.04 (-10.28%)</td><td>0.02 <b>(-35.81%)</b></td><td>634.60 (+11.47%)</td><td>464.62 (+0.12%)</td><td>457.50 (-12.82%)</td><td>301.80 <b>(+32.78%)</b></td><td>138.64 (-1.56%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>569.30 (n/a)</td><td>464.06 (n/a)</td><td>524.80 (n/a)</td><td>227.30 (n/a)</td><td>140.84 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.23 (-6.26%)</td><td>0.16 (+15.85%)</td><td>0.16 <b>(+40.15%)</b></td><td>0.09 (+10.67%)</td><td>0.06 (-5.86%)</td><td>565.70 (-9.63%)</td><td>356.82 (-14.01%)</td><td>298.80 <b>(-28.65%)</b></td><td>211.90 (+6.70%)</td><td>150.81 (-1.33%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>626.00 (n/a)</td><td>414.96 (n/a)</td><td>418.80 (n/a)</td><td>198.60 (n/a)</td><td>152.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.20 (-10.04%)</td><td>0.11 (-19.01%)</td><td>0.11 (+11.83%)</td><td>0.02 <b>(-72.42%)</b></td><td>0.06 (+6.82%)</td><td>2066.10 <b>(+262.60%)</b></td><td>747.08 <b>(+75.86%)</b></td><td>449.40 (-10.57%)</td><td>249.30 (+11.20%)</td><td>744.63 <b>(+386.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>569.80 (n/a)</td><td>424.82 (n/a)</td><td>502.50 (n/a)</td><td>224.20 (n/a)</td><td>153.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.20 (+9.64%)</td><td>0.16 <b>(+45.61%)</b></td><td>0.16 <b>(+75.33%)</b></td><td>0.12 <b>(+73.48%)</b></td><td>0.04 (-16.05%)</td><td>419.50 <b>(-42.35%)</b></td><td>332.34 <b>(-35.62%)</b></td><td>308.40 <b>(-42.97%)</b></td><td>248.50 (-8.81%)</td><td>82.22 <b>(-52.36%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>727.70 (n/a)</td><td>516.20 (n/a)</td><td>540.80 (n/a)</td><td>272.50 (n/a)</td><td>172.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.25 (+14.74%)</td><td>0.16 <b>(+20.05%)</b></td><td>0.17 <b>(+68.28%)</b></td><td>0.09 (+1.40%)</td><td>0.07 <b>(+23.86%)</b></td><td>545.60 (-1.37%)</td><td>356.14 (-12.98%)</td><td>288.90 <b>(-40.58%)</b></td><td>193.60 (-12.83%)</td><td>160.95 (+13.51%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>553.20 (n/a)</td><td>409.24 (n/a)</td><td>486.20 (n/a)</td><td>222.10 (n/a)</td><td>141.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.19 (+2.42%)</td><td>0.14 (-3.36%)</td><td>0.16 (+2.09%)</td><td>0.08 (-17.64%)</td><td>0.05 (+11.80%)</td><td>634.00 <b>(+21.41%)</b></td><td>406.78 (+7.01%)</td><td>314.40 (-2.06%)</td><td>260.20 (-2.36%)</td><td>160.98 <b>(+30.22%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>522.20 (n/a)</td><td>380.14 (n/a)</td><td>321.00 (n/a)</td><td>266.50 (n/a)</td><td>123.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.21 (+16.44%)</td><td>0.14 <b>(+67.09%)</b></td><td>0.16 <b>(+96.40%)</b></td><td>0.08 <b>(+320.34%)</b></td><td>0.06 (-4.14%)</td><td>596.60 <b>(-76.21%)</b></td><td>395.56 <b>(-59.23%)</b></td><td>298.60 <b>(-49.09%)</b></td><td>239.10 (-14.12%)</td><td>176.07 <b>(-80.42%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2507.70 (n/a)</td><td>970.14 (n/a)</td><td>586.50 (n/a)</td><td>278.40 (n/a)</td><td>899.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (+15.67%)</td><td>0.01 (-16.12%)</td><td>0.01 <b>(-29.48%)</b></td><td>0.01 (-13.98%)</td><td>0.00 <b>(+57.40%)</b></td><td>522.60 (+16.24%)</td><td>382.54 <b>(+26.56%)</b></td><td>390.90 <b>(+41.78%)</b></td><td>204.50 (-13.57%)</td><td>125.59 <b>(+48.20%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.60 (n/a)</td><td>302.26 (n/a)</td><td>275.70 (n/a)</td><td>236.60 (n/a)</td><td>84.74 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(+23.84%)</b></td><td>0.01 <b>(+65.18%)</b></td><td>0.01 <b>(+90.58%)</b></td><td>0.01 <b>(+291.22%)</b></td><td>0.00 (-12.48%)</td><td>488.80 <b>(-74.44%)</b></td><td>311.76 <b>(-57.23%)</b></td><td>271.70 <b>(-47.54%)</b></td><td>207.50 (-19.26%)</td><td>110.32 <b>(-83.55%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1912.30 (n/a)</td><td>728.86 (n/a)</td><td>517.90 (n/a)</td><td>257.00 (n/a)</td><td>670.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (-7.46%)</td><td>0.01 (-5.04%)</td><td>0.01 (-1.48%)</td><td>0.00 (+2.86%)</td><td>0.00 (-7.56%)</td><td>577.50 (-2.78%)</td><td>405.00 (+4.33%)</td><td>427.10 (+1.50%)</td><td>242.70 (+8.06%)</td><td>149.83 (-1.41%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>594.00 (n/a)</td><td>388.20 (n/a)</td><td>420.80 (n/a)</td><td>224.60 (n/a)</td><td>151.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-36.32%)</b></td><td>0.00 (-14.71%)</td><td>0.01 (-6.26%)</td><td>0.00 (-7.20%)</td><td>0.00 <b>(-59.80%)</b></td><td>650.50 (+7.75%)</td><td>535.96 (+12.28%)</td><td>502.70 (+6.66%)</td><td>465.70 <b>(+57.01%)</b></td><td>81.67 <b>(-30.91%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>603.70 (n/a)</td><td>477.36 (n/a)</td><td>471.30 (n/a)</td><td>296.60 (n/a)</td><td>118.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (+3.09%)</td><td>0.01 (+14.56%)</td><td>0.01 <b>(+35.11%)</b></td><td>0.00 (-1.33%)</td><td>0.00 <b>(+20.62%)</b></td><td>548.90 (+1.35%)</td><td>395.66 (-10.36%)</td><td>359.00 <b>(-25.99%)</b></td><td>268.20 (-2.97%)</td><td>133.27 (+18.49%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>541.60 (n/a)</td><td>441.40 (n/a)</td><td>485.10 (n/a)</td><td>276.40 (n/a)</td><td>112.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(+39.00%)</b></td><td>0.01 (-1.71%)</td><td>0.00 (-4.90%)</td><td>0.00 (-16.34%)</td><td>0.00 <b>(+130.16%)</b></td><td>648.90 (+19.55%)</td><td>521.26 (+10.30%)</td><td>547.50 (+5.15%)</td><td>262.50 <b>(-28.06%)</b></td><td>152.08 <b>(+84.62%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>542.80 (n/a)</td><td>472.60 (n/a)</td><td>520.70 (n/a)</td><td>364.90 (n/a)</td><td>82.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (+13.56%)</td><td>0.02 <b>(+23.51%)</b></td><td>0.02 <b>(+50.17%)</b></td><td>0.01 (-5.93%)</td><td>0.01 <b>(+56.90%)</b></td><td>652.10 (+6.29%)</td><td>391.32 (-13.29%)</td><td>313.50 <b>(-33.41%)</b></td><td>261.50 (-11.92%)</td><td>167.65 <b>(+44.88%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.50 (n/a)</td><td>451.32 (n/a)</td><td>470.80 (n/a)</td><td>296.90 (n/a)</td><td>115.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-7.36%)</td><td>0.02 (-17.38%)</td><td>0.02 (-5.69%)</td><td>0.01 <b>(-25.26%)</b></td><td>0.01 <b>(+39.80%)</b></td><td>543.90 <b>(+33.80%)</b></td><td>368.24 <b>(+29.89%)</b></td><td>284.70 (+6.03%)</td><td>247.40 (+7.94%)</td><td>142.66 <b>(+99.68%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>406.50 (n/a)</td><td>283.50 (n/a)</td><td>268.50 (n/a)</td><td>229.20 (n/a)</td><td>71.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (+1.77%)</td><td>0.02 (-7.66%)</td><td>0.01 (-17.17%)</td><td>0.01 (-11.26%)</td><td>0.01 (+2.17%)</td><td>563.40 (+12.68%)</td><td>384.46 (+9.30%)</td><td>377.50 <b>(+20.72%)</b></td><td>228.20 (-1.76%)</td><td>133.16 (+10.48%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>500.00 (n/a)</td><td>351.76 (n/a)</td><td>312.70 (n/a)</td><td>232.30 (n/a)</td><td>120.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-4.15%)</td><td>0.01 (+0.23%)</td><td>0.01 <b>(-30.69%)</b></td><td>0.01 <b>(+280.75%)</b></td><td>0.01 <b>(-32.94%)</b></td><td>548.20 <b>(-73.74%)</b></td><td>411.30 <b>(-40.10%)</b></td><td>444.20 <b>(+44.27%)</b></td><td>262.70 (+4.33%)</td><td>140.16 <b>(-82.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2087.30 (n/a)</td><td>686.66 (n/a)</td><td>307.90 (n/a)</td><td>251.80 (n/a)</td><td>791.18 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-0.24%)</td><td>0.01 (-0.44%)</td><td>0.02 <b>(+35.91%)</b></td><td>0.01 (+1.75%)</td><td>0.00 (-10.21%)</td><td>544.20 (-1.72%)</td><td>386.24 (-0.63%)</td><td>324.50 <b>(-26.42%)</b></td><td>245.10 (+0.25%)</td><td>134.00 (-0.12%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.70 (n/a)</td><td>388.70 (n/a)</td><td>441.00 (n/a)</td><td>244.50 (n/a)</td><td>134.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(-21.18%)</b></td><td>0.01 (-17.26%)</td><td>0.01 (+1.39%)</td><td>0.00 <b>(-70.27%)</b></td><td>0.00 (+3.50%)</td><td>1983.80 <b>(+236.35%)</b></td><td>758.64 <b>(+62.54%)</b></td><td>481.80 (-1.37%)</td><td>326.80 <b>(+26.86%)</b></td><td>689.05 <b>(+440.52%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.80 (n/a)</td><td>466.74 (n/a)</td><td>488.50 (n/a)</td><td>257.60 (n/a)</td><td>127.48 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (+16.05%)</td><td>0.03 (+5.96%)</td><td>0.02 (+1.86%)</td><td>0.02 (+18.32%)</td><td>0.01 (-3.23%)</td><td>523.00 (-15.48%)</td><td>408.60 (-8.26%)</td><td>464.10 (-1.82%)</td><td>248.50 (-13.83%)</td><td>111.91 <b>(-26.01%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>618.80 (n/a)</td><td>445.40 (n/a)</td><td>472.70 (n/a)</td><td>288.40 (n/a)</td><td>151.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (-18.00%)</td><td>0.02 (-7.95%)</td><td>0.02 (-4.29%)</td><td>0.02 (-0.78%)</td><td>0.01 <b>(-20.66%)</b></td><td>607.70 (+0.80%)</td><td>472.98 (+7.53%)</td><td>467.80 (+4.49%)</td><td>315.10 <b>(+21.94%)</b></td><td>132.96 (+6.35%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>602.90 (n/a)</td><td>439.86 (n/a)</td><td>447.70 (n/a)</td><td>258.40 (n/a)</td><td>125.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(-50.14%)</b></td><td>0.02 <b>(-33.42%)</b></td><td>0.02 <b>(-53.57%)</b></td><td>0.02 <b>(+259.88%)</b></td><td>0.00 <b>(-88.99%)</b></td><td>532.30 <b>(-72.21%)</b></td><td>489.28 <b>(-21.52%)</b></td><td>513.50 <b>(+115.39%)</b></td><td>439.70 <b>(+100.59%)</b></td><td>44.87 <b>(-93.87%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1915.60 (n/a)</td><td>623.46 (n/a)</td><td>238.40 (n/a)</td><td>219.20 (n/a)</td><td>732.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (-15.72%)</td><td>0.03 (-8.91%)</td><td>0.02 <b>(-30.88%)</b></td><td>0.02 <b>(+387.92%)</b></td><td>0.01 <b>(-63.13%)</b></td><td>499.50 <b>(-79.51%)</b></td><td>422.18 <b>(-43.12%)</b></td><td>436.60 <b>(+44.67%)</b></td><td>301.60 (+18.65%)</td><td>73.83 <b>(-92.22%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2437.20 (n/a)</td><td>742.28 (n/a)</td><td>301.80 (n/a)</td><td>254.20 (n/a)</td><td>949.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (-16.44%)</td><td>0.02 (-11.24%)</td><td>0.02 (-8.92%)</td><td>0.02 (-4.48%)</td><td>0.01 <b>(-26.61%)</b></td><td>637.70 (+4.70%)</td><td>491.44 (+8.53%)</td><td>510.60 (+9.78%)</td><td>288.30 (+19.68%)</td><td>131.44 (-12.04%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.10 (n/a)</td><td>452.82 (n/a)</td><td>465.10 (n/a)</td><td>240.90 (n/a)</td><td>149.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (-0.12%)</td><td>0.02 (-6.33%)</td><td>0.02 (-19.93%)</td><td>0.02 <b>(+128.66%)</b></td><td>0.01 <b>(-33.45%)</b></td><td>596.80 <b>(-56.27%)</b></td><td>470.46 (-17.11%)</td><td>511.50 <b>(+24.88%)</b></td><td>279.70 (+0.14%)</td><td>120.67 <b>(-73.39%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1364.60 (n/a)</td><td>567.60 (n/a)</td><td>409.60 (n/a)</td><td>279.30 (n/a)</td><td>453.39 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (+12.47%)</td><td>0.06 (+1.68%)</td><td>0.05 (-0.46%)</td><td>0.04 (+15.97%)</td><td>0.02 (-2.39%)</td><td>539.50 (-13.78%)</td><td>397.14 (-4.09%)</td><td>457.30 (+0.46%)</td><td>227.00 (-11.08%)</td><td>127.73 (-19.21%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>625.70 (n/a)</td><td>414.06 (n/a)</td><td>455.20 (n/a)</td><td>255.30 (n/a)</td><td>158.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 <b>(-20.15%)</b></td><td>0.05 (-7.18%)</td><td>0.05 (+8.56%)</td><td>0.04 (+10.41%)</td><td>0.01 <b>(-38.34%)</b></td><td>568.20 (-9.44%)</td><td>442.38 (+3.59%)</td><td>399.20 (-7.87%)</td><td>345.80 <b>(+25.24%)</b></td><td>92.48 <b>(-29.14%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.40 (n/a)</td><td>427.04 (n/a)</td><td>433.30 (n/a)</td><td>276.10 (n/a)</td><td>130.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (+1.57%)</td><td>0.06 (-6.10%)</td><td>0.05 <b>(-31.35%)</b></td><td>0.05 (+10.51%)</td><td>0.02 (+2.45%)</td><td>459.50 (-9.51%)</td><td>379.52 (+6.20%)</td><td>436.50 <b>(+45.69%)</b></td><td>255.50 (-1.54%)</td><td>96.11 (-7.74%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>507.80 (n/a)</td><td>357.36 (n/a)</td><td>299.60 (n/a)</td><td>259.50 (n/a)</td><td>104.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 <b>(+21.71%)</b></td><td>0.05 (+13.91%)</td><td>0.04 (+1.38%)</td><td>0.04 <b>(+93.88%)</b></td><td>0.01 <b>(-30.18%)</b></td><td>551.00 <b>(-48.42%)</b></td><td>472.50 (-19.81%)</td><td>494.70 (-1.36%)</td><td>354.50 (-17.83%)</td><td>75.37 <b>(-72.12%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1068.30 (n/a)</td><td>589.24 (n/a)</td><td>501.50 (n/a)</td><td>431.40 (n/a)</td><td>270.31 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (-1.55%)</td><td>0.04 <b>(-28.70%)</b></td><td>0.04 <b>(-34.00%)</b></td><td>0.02 <b>(-54.03%)</b></td><td>0.03 (+5.69%)</td><td>1333.70 <b>(+117.53%)</b></td><td>649.54 <b>(+62.91%)</b></td><td>578.50 <b>(+51.52%)</b></td><td>250.70 (+1.58%)</td><td>407.21 <b>(+153.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>613.10 (n/a)</td><td>398.72 (n/a)</td><td>381.80 (n/a)</td><td>246.80 (n/a)</td><td>160.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (-4.11%)</td><td>0.06 (-7.79%)</td><td>0.06 (-16.15%)</td><td>0.03 (-8.46%)</td><td>0.02 (-5.35%)</td><td>611.50 (+9.25%)</td><td>385.30 (+8.61%)</td><td>357.50 (+19.25%)</td><td>262.80 (+4.29%)</td><td>140.16 (+8.72%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.70 (n/a)</td><td>354.76 (n/a)</td><td>299.80 (n/a)</td><td>252.00 (n/a)</td><td>128.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.80 (n/a)</td><td>339.46 (n/a)</td><td>284.30 (n/a)</td><td>261.20 (n/a)</td><td>130.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.10 (n/a)</td><td>452.52 (n/a)</td><td>438.20 (n/a)</td><td>274.70 (n/a)</td><td>128.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.00 (n/a)</td><td>510.68 (n/a)</td><td>571.20 (n/a)</td><td>270.40 (n/a)</td><td>152.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.50 (n/a)</td><td>345.04 (n/a)</td><td>306.40 (n/a)</td><td>218.10 (n/a)</td><td>126.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>857.20 (n/a)</td><td>505.32 (n/a)</td><td>417.90 (n/a)</td><td>265.10 (n/a)</td><td>235.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.70 (n/a)</td><td>449.32 (n/a)</td><td>457.70 (n/a)</td><td>254.50 (n/a)</td><td>124.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>582.20 (n/a)</td><td>362.38 (n/a)</td><td>268.50 (n/a)</td><td>238.40 (n/a)</td><td>158.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>503.70 (n/a)</td><td>394.10 (n/a)</td><td>434.20 (n/a)</td><td>275.60 (n/a)</td><td>102.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1012.00 (n/a)</td><td>490.94 (n/a)</td><td>454.70 (n/a)</td><td>237.20 (n/a)</td><td>307.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.20 (-4.62%)</td><td>0.13 (+12.29%)</td><td>0.13 <b>(+35.62%)</b></td><td>0.08 <b>(+207.64%)</b></td><td>0.05 <b>(-33.88%)</b></td><td>630.60 <b>(-67.50%)</b></td><td>413.58 <b>(-41.44%)</b></td><td>377.20 <b>(-26.26%)</b></td><td>250.20 (+4.86%)</td><td>155.52 <b>(-77.91%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1940.10 (n/a)</td><td>706.30 (n/a)</td><td>511.50 (n/a)</td><td>238.60 (n/a)</td><td>704.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1879.90 (n/a)</td><td>695.42 (n/a)</td><td>439.10 (n/a)</td><td>283.80 (n/a)</td><td>673.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>564.30 (n/a)</td><td>392.10 (n/a)</td><td>374.70 (n/a)</td><td>207.00 (n/a)</td><td>155.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.10 (n/a)</td><td>366.68 (n/a)</td><td>300.20 (n/a)</td><td>255.80 (n/a)</td><td>145.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>420.80 (n/a)</td><td>320.34 (n/a)</td><td>318.10 (n/a)</td><td>244.10 (n/a)</td><td>69.31 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.90 (n/a)</td><td>418.86 (n/a)</td><td>306.50 (n/a)</td><td>295.40 (n/a)</td><td>162.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.10 (n/a)</td><td>381.06 (n/a)</td><td>379.40 (n/a)</td><td>233.70 (n/a)</td><td>130.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>631.10 (n/a)</td><td>323.98 (n/a)</td><td>260.70 (n/a)</td><td>185.70 (n/a)</td><td>176.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>489.00 (n/a)</td><td>363.46 (n/a)</td><td>326.80 (n/a)</td><td>249.80 (n/a)</td><td>104.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>610.70 (n/a)</td><td>390.50 (n/a)</td><td>303.20 (n/a)</td><td>246.40 (n/a)</td><td>160.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>484.80 (n/a)</td><td>334.64 (n/a)</td><td>315.70 (n/a)</td><td>232.20 (n/a)</td><td>92.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>725.50 (n/a)</td><td>481.30 (n/a)</td><td>537.60 (n/a)</td><td>251.60 (n/a)</td><td>203.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>633.00 (n/a)</td><td>418.02 (n/a)</td><td>328.20 (n/a)</td><td>254.20 (n/a)</td><td>189.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>480.40 (n/a)</td><td>332.08 (n/a)</td><td>274.00 (n/a)</td><td>245.60 (n/a)</td><td>108.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.70 (n/a)</td><td>445.08 (n/a)</td><td>445.70 (n/a)</td><td>247.50 (n/a)</td><td>127.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>717.10 (n/a)</td><td>397.12 (n/a)</td><td>295.30 (n/a)</td><td>169.30 (n/a)</td><td>228.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>751.50 (n/a)</td><td>410.60 (n/a)</td><td>297.10 (n/a)</td><td>228.60 (n/a)</td><td>216.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.10 (n/a)</td><td>405.12 (n/a)</td><td>466.20 (n/a)</td><td>186.20 (n/a)</td><td>181.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.10 (n/a)</td><td>467.10 (n/a)</td><td>547.00 (n/a)</td><td>263.20 (n/a)</td><td>150.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>672.00 (n/a)</td><td>496.04 (n/a)</td><td>443.20 (n/a)</td><td>342.20 (n/a)</td><td>143.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>777.70 (n/a)</td><td>577.50 (n/a)</td><td>623.70 (n/a)</td><td>267.30 (n/a)</td><td>188.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.80 (n/a)</td><td>426.38 (n/a)</td><td>456.00 (n/a)</td><td>259.10 (n/a)</td><td>128.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.30 (n/a)</td><td>410.68 (n/a)</td><td>465.40 (n/a)</td><td>263.30 (n/a)</td><td>135.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.10 (n/a)</td><td>382.26 (n/a)</td><td>320.90 (n/a)</td><td>250.20 (n/a)</td><td>142.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1896.00 (n/a)</td><td>758.36 (n/a)</td><td>560.10 (n/a)</td><td>285.30 (n/a)</td><td>648.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>486.60 (n/a)</td><td>421.16 (n/a)</td><td>456.80 (n/a)</td><td>312.40 (n/a)</td><td>77.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>695.00 (n/a)</td><td>568.90 (n/a)</td><td>632.70 (n/a)</td><td>408.90 (n/a)</td><td>121.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>574.30 (n/a)</td><td>463.74 (n/a)</td><td>460.50 (n/a)</td><td>346.60 (n/a)</td><td>86.26 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>734.10 (n/a)</td><td>459.94 (n/a)</td><td>458.60 (n/a)</td><td>288.10 (n/a)</td><td>180.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1097.80 (n/a)</td><td>628.80 (n/a)</td><td>587.40 (n/a)</td><td>388.70 (n/a)</td><td>276.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>574.50 (n/a)</td><td>491.14 (n/a)</td><td>482.80 (n/a)</td><td>398.80 (n/a)</td><td>80.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.10 (n/a)</td><td>477.60 (n/a)</td><td>483.40 (n/a)</td><td>361.30 (n/a)</td><td>110.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>700.40 (n/a)</td><td>416.46 (n/a)</td><td>348.50 (n/a)</td><td>303.90 (n/a)</td><td>164.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>483.50 (n/a)</td><td>346.20 (n/a)</td><td>347.50 (n/a)</td><td>232.20 (n/a)</td><td>91.35 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>566.70 (n/a)</td><td>484.44 (n/a)</td><td>519.10 (n/a)</td><td>314.20 (n/a)</td><td>98.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>592.70 (n/a)</td><td>396.06 (n/a)</td><td>353.60 (n/a)</td><td>271.10 (n/a)</td><td>125.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>409.40 (n/a)</td><td>353.30 (n/a)</td><td>339.30 (n/a)</td><td>295.90 (n/a)</td><td>53.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>647.90 (n/a)</td><td>471.12 (n/a)</td><td>516.00 (n/a)</td><td>276.20 (n/a)</td><td>176.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.54 (+10.17%)</td><td>0.42 (+7.51%)</td><td>0.45 <b>(+28.26%)</b></td><td>0.21 <b>(-32.87%)</b></td><td>0.12 <b>(+48.79%)</b></td><td>1032.20 <b>(+48.97%)</b></td><td>582.36 (-0.04%)</td><td>487.60 <b>(-22.03%)</b></td><td>407.60 (-9.24%)</td><td>254.97 <b>(+118.29%)</b></td><td>23.15 (+10.17%)</td><td>18.03 (+7.51%)</td><td>19.35 <b>(+28.26%)</b></td><td>9.14 <b>(-32.87%)</b></td><td>5.31 <b>(+48.79%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>692.90 (n/a)</td><td>582.60 (n/a)</td><td>625.40 (n/a)</td><td>449.10 (n/a)</td><td>116.80 (n/a)</td><td>21.02 (n/a)</td><td>16.77 (n/a)</td><td>15.09 (n/a)</td><td>13.62 (n/a)</td><td>3.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.58 (+1.61%)</td><td>0.39 (-9.19%)</td><td>0.39 (+1.66%)</td><td>0.09 <b>(-74.14%)</b></td><td>0.20 <b>(+108.60%)</b></td><td>2473.60 <b>(+286.74%)</b></td><td>887.72 <b>(+68.36%)</b></td><td>568.80 (-1.63%)</td><td>381.70 (-1.57%)</td><td>892.49 <b>(+750.91%)</b></td><td>24.72 (+1.61%)</td><td>16.83 (-9.19%)</td><td>16.59 (+1.66%)</td><td>3.82 <b>(-74.14%)</b></td><td>8.39 <b>(+108.60%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>639.60 (n/a)</td><td>527.28 (n/a)</td><td>578.20 (n/a)</td><td>387.80 (n/a)</td><td>104.89 (n/a)</td><td>24.33 (n/a)</td><td>18.53 (n/a)</td><td>16.32 (n/a)</td><td>14.75 (n/a)</td><td>4.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.31 (-0.36%)</td><td>0.31 (+0.79%)</td><td>0.31 (+0.44%)</td><td>0.30 (+2.15%)</td><td>0.00 <b>(-56.36%)</b></td><td>83201.60 (-2.10%)</td><td>82162.64 (-0.80%)</td><td>81914.70 (-0.43%)</td><td>81840.20 (+0.37%)</td><td>584.19 <b>(-57.16%)</b></td><td>209.92 (-0.36%)</td><td>209.10 (+0.79%)</td><td>209.73 (+0.44%)</td><td>206.48 (+2.15%)</td><td>1.47 <b>(-56.36%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84988.20 (n/a)</td><td>82823.00 (n/a)</td><td>82271.30 (n/a)</td><td>81542.50 (n/a)</td><td>1363.78 (n/a)</td><td>210.69 (n/a)</td><td>207.47 (n/a)</td><td>208.82 (n/a)</td><td>202.14 (n/a)</td><td>3.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>1.04 (+1.40%)</td><td>1.02 (+1.70%)</td><td>1.02 (+0.16%)</td><td>0.98 (+1.94%)</td><td>0.02 (-18.38%)</td><td>25641.50 (-1.90%)</td><td>24780.04 (-1.69%)</td><td>24782.50 (-0.16%)</td><td>24198.10 (-1.38%)</td><td>547.43 <b>(-20.92%)</b></td><td>709.97 (+1.40%)</td><td>693.56 (+1.70%)</td><td>693.23 (+0.16%)</td><td>670.00 (+1.94%)</td><td>15.12 (-18.38%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.96 (n/a)</td><td>0.03 (n/a)</td><td>26139.40 (n/a)</td><td>25206.74 (n/a)</td><td>24823.10 (n/a)</td><td>24536.30 (n/a)</td><td>692.30 (n/a)</td><td>700.18 (n/a)</td><td>681.97 (n/a)</td><td>692.09 (n/a)</td><td>657.24 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.81 (-0.37%)</td><td>0.80 (-0.67%)</td><td>0.81 (+0.22%)</td><td>0.77 (-3.32%)</td><td>0.02 <b>(+94.53%)</b></td><td>98244.40 (+3.43%)</td><td>94439.38 (+0.70%)</td><td>93530.60 (-0.22%)</td><td>92874.90 (+0.37%)</td><td>2194.88 <b>(+102.44%)</b></td><td>739.91 (-0.37%)</td><td>727.96 (-0.67%)</td><td>734.73 (+0.22%)</td><td>699.48 (-3.32%)</td><td>16.48 <b>(+94.53%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>94985.50 (n/a)</td><td>93781.50 (n/a)</td><td>93734.60 (n/a)</td><td>92533.90 (n/a)</td><td>1084.22 (n/a)</td><td>742.64 (n/a)</td><td>732.84 (n/a)</td><td>733.13 (n/a)</td><td>723.47 (n/a)</td><td>8.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.77 (-0.45%)</td><td>0.77 (+0.68%)</td><td>0.77 (+1.05%)</td><td>0.76 (+1.53%)</td><td>0.00 <b>(-61.80%)</b></td><td>99085.40 (-1.50%)</td><td>98390.54 (-0.68%)</td><td>98421.80 (-1.04%)</td><td>97914.20 (+0.45%)</td><td>483.42 <b>(-62.19%)</b></td><td>701.83 (-0.45%)</td><td>698.45 (+0.68%)</td><td>698.21 (+1.05%)</td><td>693.54 (+1.53%)</td><td>3.43 <b>(-61.80%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100599.40 (n/a)</td><td>99067.64 (n/a)</td><td>99451.80 (n/a)</td><td>97475.30 (n/a)</td><td>1278.53 (n/a)</td><td>704.99 (n/a)</td><td>693.75 (n/a)</td><td>690.98 (n/a)</td><td>683.10 (n/a)</td><td>8.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.80 (+0.00%)</td><td>0.79 (-0.16%)</td><td>0.79 (-0.48%)</td><td>0.78 (-0.55%)</td><td>0.01 <b>(+22.10%)</b></td><td>97025.10 (+0.55%)</td><td>95634.34 (+0.17%)</td><td>95742.20 (+0.48%)</td><td>94343.40 (-0.00%)</td><td>1126.67 <b>(+22.49%)</b></td><td>728.40 (+0.00%)</td><td>718.64 (-0.16%)</td><td>717.76 (-0.48%)</td><td>708.26 (-0.55%)</td><td>8.47 <b>(+22.10%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96491.10 (n/a)</td><td>95475.22 (n/a)</td><td>95287.30 (n/a)</td><td>94347.30 (n/a)</td><td>919.77 (n/a)</td><td>728.37 (n/a)</td><td>719.82 (n/a)</td><td>721.18 (n/a)</td><td>712.18 (n/a)</td><td>6.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.36 (-4.55%)</td><td>4.12 (-15.01%)</td><td>4.05 <b>(-23.21%)</b></td><td>1.97 <b>(-50.62%)</b></td><td>1.35 <b>(+75.56%)</b></td><td>4517.30 <b>(+102.52%)</b></td><td>2461.16 <b>(+31.06%)</b></td><td>2198.90 <b>(+30.23%)</b></td><td>1662.70 (+4.77%)</td><td>1177.39 <b>(+276.89%)</b></td><td>322.89 (-4.55%)</td><td>248.22 (-15.01%)</td><td>244.16 <b>(-23.21%)</b></td><td>118.85 <b>(-50.62%)</b></td><td>81.19 <b>(+75.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.62 (n/a)</td><td>4.85 (n/a)</td><td>5.28 (n/a)</td><td>4.00 (n/a)</td><td>0.77 (n/a)</td><td>2230.60 (n/a)</td><td>1877.88 (n/a)</td><td>1688.50 (n/a)</td><td>1587.00 (n/a)</td><td>312.39 (n/a)</td><td>338.29 (n/a)</td><td>292.04 (n/a)</td><td>317.96 (n/a)</td><td>240.69 (n/a)</td><td>46.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.82 (-6.87%)</td><td>3.17 (-8.36%)</td><td>2.80 (-6.30%)</td><td>2.15 <b>(+28.90%)</b></td><td>1.16 <b>(-21.88%)</b></td><td>4137.80 <b>(-22.42%)</b></td><td>3104.80 (+1.89%)</td><td>3188.70 (+6.73%)</td><td>1847.90 (+7.37%)</td><td>1026.74 <b>(-29.51%)</b></td><td>290.53 (-6.87%)</td><td>191.02 (-8.36%)</td><td>168.37 (-6.30%)</td><td>129.75 <b>(+28.90%)</b></td><td>69.75 <b>(-21.88%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.18 (n/a)</td><td>3.46 (n/a)</td><td>2.98 (n/a)</td><td>1.67 (n/a)</td><td>1.48 (n/a)</td><td>5333.50 (n/a)</td><td>3047.10 (n/a)</td><td>2987.70 (n/a)</td><td>1721.00 (n/a)</td><td>1456.62 (n/a)</td><td>311.95 (n/a)</td><td>208.45 (n/a)</td><td>179.69 (n/a)</td><td>100.66 (n/a)</td><td>89.30 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.17 (+0.40%)</td><td>4.01 (+18.58%)</td><td>4.15 (+7.31%)</td><td>2.75 <b>(+57.28%)</b></td><td>1.17 (-16.37%)</td><td>3241.00 <b>(-36.42%)</b></td><td>2391.20 <b>(-22.74%)</b></td><td>2145.70 (-6.81%)</td><td>1725.00 (-0.39%)</td><td>735.48 <b>(-48.83%)</b></td><td>311.23 (+0.40%)</td><td>241.76 (+18.58%)</td><td>250.21 (+7.31%)</td><td>165.65 <b>(+57.28%)</b></td><td>70.61 (-16.37%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.15 (n/a)</td><td>3.38 (n/a)</td><td>3.87 (n/a)</td><td>1.75 (n/a)</td><td>1.40 (n/a)</td><td>5097.30 (n/a)</td><td>3095.06 (n/a)</td><td>2302.60 (n/a)</td><td>1731.80 (n/a)</td><td>1437.32 (n/a)</td><td>310.01 (n/a)</td><td>203.88 (n/a)</td><td>233.15 (n/a)</td><td>105.32 (n/a)</td><td>84.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.40 (+14.34%)</td><td>5.55 (+8.51%)</td><td>5.46 (+6.51%)</td><td>4.55 (+6.62%)</td><td>0.74 <b>(+40.84%)</b></td><td>7664.20 (-6.21%)</td><td>6373.92 (-7.33%)</td><td>6388.10 (-6.11%)</td><td>5449.00 (-12.54%)</td><td>881.32 (+13.80%)</td><td>394.11 (+14.34%)</td><td>341.94 (+8.51%)</td><td>336.17 (+6.51%)</td><td>280.20 (+6.62%)</td><td>45.63 <b>(+40.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.60 (n/a)</td><td>5.12 (n/a)</td><td>5.12 (n/a)</td><td>4.27 (n/a)</td><td>0.53 (n/a)</td><td>8171.30 (n/a)</td><td>6878.00 (n/a)</td><td>6803.90 (n/a)</td><td>6230.20 (n/a)</td><td>774.46 (n/a)</td><td>344.69 (n/a)</td><td>315.13 (n/a)</td><td>315.62 (n/a)</td><td>262.81 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.56 (+1.33%)</td><td>4.69 (-1.55%)</td><td>4.76 (+6.92%)</td><td>3.81 (-7.50%)</td><td>0.64 (+3.81%)</td><td>9149.30 (+8.11%)</td><td>7551.58 (+1.80%)</td><td>7323.20 (-6.47%)</td><td>6274.90 (-1.31%)</td><td>1055.28 (+13.85%)</td><td>342.23 (+1.33%)</td><td>288.71 (-1.55%)</td><td>293.24 (+6.92%)</td><td>234.71 (-7.50%)</td><td>39.13 (+3.81%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.48 (n/a)</td><td>4.76 (n/a)</td><td>4.45 (n/a)</td><td>4.12 (n/a)</td><td>0.61 (n/a)</td><td>8463.20 (n/a)</td><td>7418.14 (n/a)</td><td>7829.80 (n/a)</td><td>6358.40 (n/a)</td><td>926.91 (n/a)</td><td>337.74 (n/a)</td><td>293.25 (n/a)</td><td>274.27 (n/a)</td><td>253.74 (n/a)</td><td>37.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.29 (-3.61%)</td><td>5.55 (+14.67%)</td><td>5.32 (+18.61%)</td><td>4.87 (+17.83%)</td><td>0.57 <b>(-40.60%)</b></td><td>7154.00 (-15.13%)</td><td>6339.10 (-14.32%)</td><td>6549.30 (-15.69%)</td><td>5545.00 (+3.75%)</td><td>645.85 <b>(-46.38%)</b></td><td>387.28 (-3.61%)</td><td>341.64 (+14.67%)</td><td>327.90 (+18.61%)</td><td>300.18 (+17.83%)</td><td>35.27 <b>(-40.60%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.52 (n/a)</td><td>4.84 (n/a)</td><td>4.49 (n/a)</td><td>4.14 (n/a)</td><td>0.96 (n/a)</td><td>8429.50 (n/a)</td><td>7398.88 (n/a)</td><td>7768.20 (n/a)</td><td>5344.70 (n/a)</td><td>1204.42 (n/a)</td><td>401.80 (n/a)</td><td>297.94 (n/a)</td><td>276.44 (n/a)</td><td>254.76 (n/a)</td><td>59.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.79 (+0.28%)</td><td>0.77 (-0.15%)</td><td>0.77 (+0.13%)</td><td>0.75 (-1.83%)</td><td>0.02 <b>(+54.19%)</b></td><td>100701.50 (+1.86%)</td><td>97469.16 (+0.17%)</td><td>97501.90 (-0.13%)</td><td>95218.70 (-0.28%)</td><td>2053.46 <b>(+57.14%)</b></td><td>721.70 (+0.28%)</td><td>705.29 (-0.15%)</td><td>704.80 (+0.13%)</td><td>682.41 (-1.83%)</td><td>14.68 <b>(+54.19%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>98863.50 (n/a)</td><td>97306.04 (n/a)</td><td>97633.50 (n/a)</td><td>95482.20 (n/a)</td><td>1306.77 (n/a)</td><td>719.71 (n/a)</td><td>706.32 (n/a)</td><td>703.85 (n/a)</td><td>695.09 (n/a)</td><td>9.52 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.78 (-0.58%)</td><td>0.76 (-1.06%)</td><td>0.76 (-0.78%)</td><td>0.75 (-1.42%)</td><td>0.01 (+18.16%)</td><td>101258.40 (+1.44%)</td><td>99464.08 (+1.08%)</td><td>99580.70 (+0.79%)</td><td>97113.20 (+0.59%)</td><td>1495.31 <b>(+20.40%)</b></td><td>707.62 (-0.58%)</td><td>691.02 (-1.06%)</td><td>690.09 (-0.78%)</td><td>678.65 (-1.42%)</td><td>10.48 (+18.16%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99825.20 (n/a)</td><td>98400.04 (n/a)</td><td>98803.20 (n/a)</td><td>96547.70 (n/a)</td><td>1241.93 (n/a)</td><td>711.77 (n/a)</td><td>698.46 (n/a)</td><td>695.52 (n/a)</td><td>688.40 (n/a)</td><td>8.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.81 (+1.20%)</td><td>0.80 (-0.42%)</td><td>0.80 (+0.12%)</td><td>0.78 (-2.11%)</td><td>0.01 <b>(+314.72%)</b></td><td>96936.40 (+2.15%)</td><td>94765.02 (+0.44%)</td><td>94325.30 (-0.12%)</td><td>92789.10 (-1.18%)</td><td>1635.57 <b>(+319.16%)</b></td><td>740.60 (+1.20%)</td><td>725.33 (-0.42%)</td><td>728.54 (+0.12%)</td><td>708.91 (-2.11%)</td><td>12.48 <b>(+314.72%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94891.60 (n/a)</td><td>94346.90 (n/a)</td><td>94435.80 (n/a)</td><td>93900.10 (n/a)</td><td>390.21 (n/a)</td><td>731.84 (n/a)</td><td>728.38 (n/a)</td><td>727.68 (n/a)</td><td>724.19 (n/a)</td><td>3.01 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.42 (-0.01%)</td><td>2.48 (+12.32%)</td><td>3.11 <b>(+90.02%)</b></td><td>1.13 <b>(-28.67%)</b></td><td>1.14 <b>(+35.82%)</b></td><td>7149.60 <b>(+40.19%)</b></td><td>4086.66 (+1.09%)</td><td>2589.60 <b>(-47.37%)</b></td><td>2355.80 (+0.01%)</td><td>2294.06 <b>(+76.20%)</b></td><td>897.34 (-0.01%)</td><td>650.61 (+12.32%)</td><td>816.33 <b>(+90.02%)</b></td><td>295.67 <b>(-28.67%)</b></td><td>299.49 <b>(+35.82%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.42 (n/a)</td><td>2.21 (n/a)</td><td>1.64 (n/a)</td><td>1.58 (n/a)</td><td>0.84 (n/a)</td><td>5099.90 (n/a)</td><td>4042.70 (n/a)</td><td>4920.70 (n/a)</td><td>2355.60 (n/a)</td><td>1301.95 (n/a)</td><td>897.39 (n/a)</td><td>579.23 (n/a)</td><td>429.60 (n/a)</td><td>414.51 (n/a)</td><td>220.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.32 (+12.21%)</td><td>0.24 (+10.59%)</td><td>0.24 <b>(+22.72%)</b></td><td>0.15 (+0.37%)</td><td>0.06 (+13.31%)</td><td>8179.70 (-0.37%)</td><td>5519.64 (-8.77%)</td><td>5113.60 (-18.51%)</td><td>3881.10 (-10.88%)</td><td>1599.89 (+6.29%)</td><td>17.29 (+12.21%)</td><td>12.89 (+10.59%)</td><td>13.12 <b>(+22.72%)</b></td><td>8.20 (+0.37%)</td><td>3.25 (+13.31%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>8210.20 (n/a)</td><td>6050.08 (n/a)</td><td>6275.30 (n/a)</td><td>4355.00 (n/a)</td><td>1505.28 (n/a)</td><td>15.41 (n/a)</td><td>11.65 (n/a)</td><td>10.69 (n/a)</td><td>8.17 (n/a)</td><td>2.86 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.80 (n/a)</td><td>3.66 (n/a)</td><td>3.67 (n/a)</td><td>3.56 (n/a)</td><td>0.09 (n/a)</td><td>3.79 (n/a)</td><td>3.66 (n/a)</td><td>3.67 (n/a)</td><td>3.56 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.94 (+1.43%)</td><td>6.50 (+9.35%)</td><td>6.57 (+14.66%)</td><td>5.63 (+7.01%)</td><td>0.53 (-16.42%)</td><td>6.93 (+1.43%)</td><td>6.49 (+9.35%)</td><td>6.57 (+14.66%)</td><td>5.62 (+7.01%)</td><td>0.53 (-16.42%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.84 (n/a)</td><td>5.94 (n/a)</td><td>5.73 (n/a)</td><td>5.26 (n/a)</td><td>0.64 (n/a)</td><td>6.84 (n/a)</td><td>5.94 (n/a)</td><td>5.73 (n/a)</td><td>5.25 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>10.93 <b>(-23.19%)</b></td><td>8.45 (-14.15%)</td><td>8.51 (-6.22%)</td><td>5.64 <b>(-29.48%)</b></td><td>2.02 (-18.93%)</td><td>10.92 <b>(-23.19%)</b></td><td>8.45 (-14.15%)</td><td>8.51 (-6.22%)</td><td>5.64 <b>(-29.48%)</b></td><td>2.02 (-18.93%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>14.23 (n/a)</td><td>9.84 (n/a)</td><td>9.08 (n/a)</td><td>8.00 (n/a)</td><td>2.50 (n/a)</td><td>14.22 (n/a)</td><td>9.84 (n/a)</td><td>9.07 (n/a)</td><td>8.00 (n/a)</td><td>2.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.89 (n/a)</td><td>3.63 (n/a)</td><td>3.64 (n/a)</td><td>3.36 (n/a)</td><td>0.22 (n/a)</td><td>3.88 (n/a)</td><td>3.63 (n/a)</td><td>3.63 (n/a)</td><td>3.36 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.21 (+11.37%)</td><td>6.58 (+10.40%)</td><td>6.95 <b>(+20.62%)</b></td><td>5.74 (+1.22%)</td><td>0.74 <b>(+108.08%)</b></td><td>7.21 (+11.37%)</td><td>6.58 (+10.40%)</td><td>6.94 <b>(+20.62%)</b></td><td>5.74 (+1.22%)</td><td>0.74 <b>(+108.08%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.47 (n/a)</td><td>5.96 (n/a)</td><td>5.76 (n/a)</td><td>5.67 (n/a)</td><td>0.36 (n/a)</td><td>6.47 (n/a)</td><td>5.96 (n/a)</td><td>5.76 (n/a)</td><td>5.67 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>13.61 (+0.22%)</td><td>10.29 (+0.58%)</td><td>9.17 (-5.07%)</td><td>7.06 (-15.44%)</td><td>3.12 <b>(+58.34%)</b></td><td>13.60 (+0.22%)</td><td>10.28 (+0.58%)</td><td>9.17 (-5.07%)</td><td>7.05 (-15.44%)</td><td>3.12 <b>(+58.34%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>13.58 (n/a)</td><td>10.23 (n/a)</td><td>9.66 (n/a)</td><td>8.35 (n/a)</td><td>1.97 (n/a)</td><td>13.57 (n/a)</td><td>10.22 (n/a)</td><td>9.66 (n/a)</td><td>8.34 (n/a)</td><td>1.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.95 (-0.40%)</td><td>1.59 <b>(-28.20%)</b></td><td>1.27 <b>(-55.95%)</b></td><td>1.05 (-1.59%)</td><td>0.78 <b>(-20.22%)</b></td><td>2.95 (-0.40%)</td><td>1.59 <b>(-28.20%)</b></td><td>1.27 <b>(-55.95%)</b></td><td>1.04 (-1.59%)</td><td>0.78 <b>(-20.22%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.96 (n/a)</td><td>2.22 (n/a)</td><td>2.88 (n/a)</td><td>1.06 (n/a)</td><td>0.98 (n/a)</td><td>2.96 (n/a)</td><td>2.22 (n/a)</td><td>2.87 (n/a)</td><td>1.06 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.48 (+1.48%)</td><td>0.33 <b>(+23.40%)</b></td><td>0.35 <b>(+51.15%)</b></td><td>0.08 (-3.69%)</td><td>0.17 (+16.39%)</td><td>0.47 (+1.48%)</td><td>0.32 <b>(+23.40%)</b></td><td>0.35 <b>(+51.15%)</b></td><td>0.07 (-3.69%)</td><td>0.16 (+16.39%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.47 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>0.14 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.67 (-0.66%)</td><td>0.59 <b>(+59.46%)</b></td><td>0.61 <b>(+87.55%)</b></td><td>0.42 <b>(+437.43%)</b></td><td>0.10 <b>(-63.65%)</b></td><td>0.66 (-0.66%)</td><td>0.58 <b>(+59.46%)</b></td><td>0.61 <b>(+87.55%)</b></td><td>0.41 <b>(+437.43%)</b></td><td>0.10 <b>(-63.65%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.67 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td><td>0.66 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.62 (+7.15%)</td><td>1.53 (+7.08%)</td><td>1.85 <b>(+26.93%)</b></td><td>0.43 <b>(-40.52%)</b></td><td>1.03 <b>(+42.42%)</b></td><td>2.58 (+7.15%)</td><td>1.50 (+7.08%)</td><td>1.82 <b>(+26.93%)</b></td><td>0.42 <b>(-40.52%)</b></td><td>1.01 <b>(+42.42%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.44 (n/a)</td><td>1.43 (n/a)</td><td>1.45 (n/a)</td><td>0.72 (n/a)</td><td>0.72 (n/a)</td><td>2.40 (n/a)</td><td>1.40 (n/a)</td><td>1.43 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.60 (n/a)</td><td>323.60 (n/a)</td><td>285.10 (n/a)</td><td>234.90 (n/a)</td><td>89.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>446.90 (n/a)</td><td>318.50 (n/a)</td><td>313.90 (n/a)</td><td>234.30 (n/a)</td><td>79.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.50 (n/a)</td><td>355.94 (n/a)</td><td>346.70 (n/a)</td><td>245.70 (n/a)</td><td>126.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>636.20 (n/a)</td><td>434.00 (n/a)</td><td>439.40 (n/a)</td><td>222.00 (n/a)</td><td>146.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2035.50 (n/a)</td><td>977.20 (n/a)</td><td>428.20 (n/a)</td><td>225.70 (n/a)</td><td>931.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.80 (n/a)</td><td>498.42 (n/a)</td><td>524.70 (n/a)</td><td>407.20 (n/a)</td><td>81.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.30 (n/a)</td><td>335.48 (n/a)</td><td>294.10 (n/a)</td><td>259.40 (n/a)</td><td>96.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.50 (n/a)</td><td>441.96 (n/a)</td><td>473.40 (n/a)</td><td>256.00 (n/a)</td><td>176.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.90 (n/a)</td><td>448.20 (n/a)</td><td>504.00 (n/a)</td><td>201.30 (n/a)</td><td>142.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.00 (n/a)</td><td>434.36 (n/a)</td><td>499.10 (n/a)</td><td>240.10 (n/a)</td><td>128.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1093.30 (n/a)</td><td>606.70 (n/a)</td><td>496.20 (n/a)</td><td>419.00 (n/a)</td><td>275.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>684.90 (n/a)</td><td>452.24 (n/a)</td><td>438.90 (n/a)</td><td>280.10 (n/a)</td><td>148.42 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>656.20 (n/a)</td><td>509.52 (n/a)</td><td>534.80 (n/a)</td><td>262.80 (n/a)</td><td>162.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>656.90 (n/a)</td><td>439.98 (n/a)</td><td>466.80 (n/a)</td><td>233.50 (n/a)</td><td>195.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>602.50 (n/a)</td><td>400.80 (n/a)</td><td>385.20 (n/a)</td><td>274.30 (n/a)</td><td>134.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1962.30 (n/a)</td><td>737.40 (n/a)</td><td>575.20 (n/a)</td><td>266.40 (n/a)</td><td>700.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>568.50 (n/a)</td><td>467.08 (n/a)</td><td>515.80 (n/a)</td><td>272.70 (n/a)</td><td>120.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>649.00 (n/a)</td><td>465.98 (n/a)</td><td>469.40 (n/a)</td><td>272.60 (n/a)</td><td>133.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>659.50 (n/a)</td><td>366.44 (n/a)</td><td>315.70 (n/a)</td><td>261.00 (n/a)</td><td>166.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1948.10 (n/a)</td><td>704.84 (n/a)</td><td>494.50 (n/a)</td><td>211.20 (n/a)</td><td>708.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>533.10 (n/a)</td><td>354.92 (n/a)</td><td>313.70 (n/a)</td><td>257.80 (n/a)</td><td>108.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1007.80 (n/a)</td><td>529.00 (n/a)</td><td>474.90 (n/a)</td><td>255.70 (n/a)</td><td>308.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>588.40 (n/a)</td><td>430.16 (n/a)</td><td>477.00 (n/a)</td><td>227.90 (n/a)</td><td>167.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>452.10 (n/a)</td><td>378.56 (n/a)</td><td>430.90 (n/a)</td><td>257.20 (n/a)</td><td>90.86 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-7.16%)</td><td>0.01 (+19.75%)</td><td>0.01 <b>(+56.02%)</b></td><td>0.01 (+3.24%)</td><td>0.00 <b>(-20.72%)</b></td><td>549.20 (-3.14%)</td><td>333.92 (-19.35%)</td><td>282.40 <b>(-35.89%)</b></td><td>255.60 (+7.71%)</td><td>122.47 (-15.02%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>567.00 (n/a)</td><td>414.06 (n/a)</td><td>440.50 (n/a)</td><td>237.30 (n/a)</td><td>144.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(+32.37%)</b></td><td>0.01 (+18.38%)</td><td>0.01 (+16.07%)</td><td>0.01 <b>(-25.75%)</b></td><td>0.01 <b>(+72.68%)</b></td><td>722.50 <b>(+34.67%)</b></td><td>411.20 (-5.09%)</td><td>414.90 (-13.83%)</td><td>194.50 <b>(-24.47%)</b></td><td>197.81 <b>(+80.90%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.50 (n/a)</td><td>433.24 (n/a)</td><td>481.50 (n/a)</td><td>257.50 (n/a)</td><td>109.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(+21.80%)</b></td><td>0.01 <b>(+20.45%)</b></td><td>0.01 <b>(+24.32%)</b></td><td>0.01 (+19.62%)</td><td>0.01 <b>(+20.14%)</b></td><td>427.50 (-16.41%)</td><td>312.42 (-16.98%)</td><td>287.80 (-19.54%)</td><td>193.80 (-17.92%)</td><td>106.83 (-16.57%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.40 (n/a)</td><td>376.32 (n/a)</td><td>357.70 (n/a)</td><td>236.10 (n/a)</td><td>128.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(+55.69%)</b></td><td>0.01 (-12.96%)</td><td>0.01 (-12.43%)</td><td>0.00 <b>(-73.48%)</b></td><td>0.01 <b>(+105.06%)</b></td><td>2009.20 <b>(+277.10%)</b></td><td>767.76 <b>(+89.76%)</b></td><td>546.50 (+14.21%)</td><td>165.80 <b>(-35.76%)</b></td><td>714.48 <b>(+428.92%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.80 (n/a)</td><td>404.60 (n/a)</td><td>478.50 (n/a)</td><td>258.10 (n/a)</td><td>135.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-0.07%)</td><td>0.01 <b>(+33.84%)</b></td><td>0.01 <b>(+52.36%)</b></td><td>0.01 <b>(+229.73%)</b></td><td>0.00 <b>(-20.29%)</b></td><td>610.20 <b>(-69.67%)</b></td><td>390.20 <b>(-47.78%)</b></td><td>320.60 <b>(-34.37%)</b></td><td>232.20 (+0.04%)</td><td>158.74 <b>(-77.86%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2012.10 (n/a)</td><td>747.16 (n/a)</td><td>488.50 (n/a)</td><td>232.10 (n/a)</td><td>716.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(+37.46%)</b></td><td>0.01 <b>(+20.13%)</b></td><td>0.01 (-1.27%)</td><td>0.01 (+11.43%)</td><td>0.00 <b>(+66.17%)</b></td><td>655.00 (-10.26%)</td><td>455.12 (-11.19%)</td><td>513.10 (+1.28%)</td><td>241.70 <b>(-27.24%)</b></td><td>180.28 (+8.38%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>729.90 (n/a)</td><td>512.44 (n/a)</td><td>506.60 (n/a)</td><td>332.20 (n/a)</td><td>166.35 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+34.46%)</b></td><td>0.02 (+5.17%)</td><td>0.03 (-2.81%)</td><td>0.01 (-0.96%)</td><td>0.01 <b>(+47.71%)</b></td><td>591.00 (+0.96%)</td><td>399.90 (+1.80%)</td><td>309.80 (+2.92%)</td><td>203.60 <b>(-25.64%)</b></td><td>177.71 <b>(+22.98%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.40 (n/a)</td><td>392.84 (n/a)</td><td>301.00 (n/a)</td><td>273.80 (n/a)</td><td>144.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+39.23%)</b></td><td>0.02 (+13.53%)</td><td>0.02 (-16.61%)</td><td>0.02 (-4.00%)</td><td>0.01 <b>(+116.53%)</b></td><td>524.60 (+4.17%)</td><td>400.90 (-0.51%)</td><td>515.90 (+19.92%)</td><td>210.10 <b>(-28.20%)</b></td><td>163.47 <b>(+70.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.60 (n/a)</td><td>402.94 (n/a)</td><td>430.20 (n/a)</td><td>292.60 (n/a)</td><td>95.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 <b>(-21.12%)</b></td><td>0.02 (-5.61%)</td><td>0.03 (+9.80%)</td><td>0.02 (-0.03%)</td><td>0.01 <b>(-22.92%)</b></td><td>485.30 (+0.04%)</td><td>357.58 (+4.35%)</td><td>289.80 (-8.93%)</td><td>248.10 <b>(+26.78%)</b></td><td>117.16 (+4.68%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.10 (n/a)</td><td>342.68 (n/a)</td><td>318.20 (n/a)</td><td>195.70 (n/a)</td><td>111.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+47.98%)</b></td><td>0.02 <b>(+24.22%)</b></td><td>0.02 (-18.37%)</td><td>0.02 <b>(+100.67%)</b></td><td>0.01 <b>(+23.61%)</b></td><td>527.70 <b>(-50.17%)</b></td><td>382.48 <b>(-27.38%)</b></td><td>442.60 <b>(+22.50%)</b></td><td>194.30 <b>(-32.42%)</b></td><td>144.11 <b>(-56.21%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1059.00 (n/a)</td><td>526.72 (n/a)</td><td>361.30 (n/a)</td><td>287.50 (n/a)</td><td>329.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (+9.54%)</td><td>0.02 <b>(+24.69%)</b></td><td>0.03 <b>(+60.97%)</b></td><td>0.01 (-13.75%)</td><td>0.01 <b>(+47.20%)</b></td><td>616.70 (+15.94%)</td><td>376.14 (-14.89%)</td><td>293.90 <b>(-37.88%)</b></td><td>261.80 (-8.72%)</td><td>151.03 <b>(+59.59%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.90 (n/a)</td><td>441.92 (n/a)</td><td>473.10 (n/a)</td><td>286.80 (n/a)</td><td>94.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+21.67%)</b></td><td>0.03 <b>(+42.30%)</b></td><td>0.03 <b>(+62.96%)</b></td><td>0.01 (-7.51%)</td><td>0.01 <b>(+29.92%)</b></td><td>564.50 (+8.12%)</td><td>320.30 <b>(-26.64%)</b></td><td>292.80 <b>(-38.64%)</b></td><td>200.10 (-17.79%)</td><td>142.87 <b>(+26.24%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.10 (n/a)</td><td>436.60 (n/a)</td><td>477.20 (n/a)</td><td>243.40 (n/a)</td><td>113.18 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 <b>(+23.18%)</b></td><td>0.02 <b>(-21.63%)</b></td><td>0.02 <b>(-31.81%)</b></td><td>0.00 <b>(-69.06%)</b></td><td>0.01 <b>(+75.29%)</b></td><td>1899.80 <b>(+223.21%)</b></td><td>712.04 <b>(+90.33%)</b></td><td>437.10 <b>(+46.63%)</b></td><td>236.10 (-18.81%)</td><td>676.48 <b>(+426.19%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.80 (n/a)</td><td>374.10 (n/a)</td><td>298.10 (n/a)</td><td>290.80 (n/a)</td><td>128.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-16.03%)</td><td>0.01 (-13.91%)</td><td>0.01 (-14.39%)</td><td>0.01 (-19.72%)</td><td>0.00 (-16.42%)</td><td>703.00 <b>(+24.56%)</b></td><td>571.74 (+16.26%)</td><td>603.50 (+16.80%)</td><td>388.60 (+19.09%)</td><td>118.82 <b>(+23.59%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.40 (n/a)</td><td>491.78 (n/a)</td><td>516.70 (n/a)</td><td>326.30 (n/a)</td><td>96.14 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+11.59%)</td><td>0.04 (+12.10%)</td><td>0.03 (-7.18%)</td><td>0.03 <b>(+228.97%)</b></td><td>0.02 (-6.48%)</td><td>600.60 <b>(-69.60%)</b></td><td>428.62 <b>(-37.94%)</b></td><td>475.60 (+7.72%)</td><td>231.70 (-10.37%)</td><td>173.51 <b>(-76.08%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1975.60 (n/a)</td><td>690.64 (n/a)</td><td>441.50 (n/a)</td><td>258.50 (n/a)</td><td>725.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(-37.28%)</b></td><td>0.04 <b>(-30.52%)</b></td><td>0.04 <b>(-39.99%)</b></td><td>0.03 (+13.24%)</td><td>0.01 <b>(-69.23%)</b></td><td>513.20 (-11.70%)</td><td>452.90 <b>(+30.53%)</b></td><td>462.90 <b>(+66.63%)</b></td><td>355.50 <b>(+59.42%)</b></td><td>58.39 <b>(-59.38%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.20 (n/a)</td><td>346.96 (n/a)</td><td>277.80 (n/a)</td><td>223.00 (n/a)</td><td>143.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (-4.26%)</td><td>0.04 (-11.17%)</td><td>0.03 (-2.73%)</td><td>0.03 (-15.45%)</td><td>0.01 (-14.39%)</td><td>591.50 (+18.28%)</td><td>457.64 (+11.61%)</td><td>489.50 (+2.81%)</td><td>298.10 (+4.45%)</td><td>109.71 (+2.38%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>500.10 (n/a)</td><td>410.02 (n/a)</td><td>476.10 (n/a)</td><td>285.40 (n/a)</td><td>107.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (-9.74%)</td><td>0.03 (-6.61%)</td><td>0.04 (+0.63%)</td><td>0.02 <b>(-25.94%)</b></td><td>0.01 (+10.48%)</td><td>1079.40 <b>(+35.03%)</b></td><td>560.80 (+15.04%)</td><td>429.50 (-0.62%)</td><td>349.20 (+10.79%)</td><td>305.07 <b>(+60.38%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>799.40 (n/a)</td><td>487.50 (n/a)</td><td>432.20 (n/a)</td><td>315.20 (n/a)</td><td>190.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 <b>(+35.76%)</b></td><td>0.05 <b>(+39.11%)</b></td><td>0.04 <b>(+21.17%)</b></td><td>0.04 <b>(+44.36%)</b></td><td>0.01 <b>(+45.84%)</b></td><td>458.60 <b>(-30.74%)</b></td><td>378.12 <b>(-27.36%)</b></td><td>441.80 (-17.48%)</td><td>240.70 <b>(-26.35%)</b></td><td>99.89 (-19.34%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>662.10 (n/a)</td><td>520.54 (n/a)</td><td>535.40 (n/a)</td><td>326.80 (n/a)</td><td>123.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(-41.79%)</b></td><td>0.03 <b>(-21.44%)</b></td><td>0.03 (-3.79%)</td><td>0.03 (-14.40%)</td><td>0.01 <b>(-63.77%)</b></td><td>654.90 (+16.82%)</td><td>516.12 <b>(+20.21%)</b></td><td>487.10 (+3.93%)</td><td>429.90 <b>(+71.82%)</b></td><td>90.72 <b>(-24.74%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>560.60 (n/a)</td><td>429.34 (n/a)</td><td>468.70 (n/a)</td><td>250.20 (n/a)</td><td>120.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (+6.30%)</td><td>0.08 (-17.39%)</td><td>0.06 <b>(-21.50%)</b></td><td>0.04 <b>(-39.59%)</b></td><td>0.04 <b>(+46.63%)</b></td><td>760.50 <b>(+65.54%)</b></td><td>497.26 <b>(+35.66%)</b></td><td>506.80 <b>(+27.37%)</b></td><td>225.00 (-5.94%)</td><td>205.52 <b>(+119.73%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>459.40 (n/a)</td><td>366.54 (n/a)</td><td>397.90 (n/a)</td><td>239.20 (n/a)</td><td>93.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (-1.99%)</td><td>0.10 <b>(+23.38%)</b></td><td>0.10 <b>(+65.54%)</b></td><td>0.08 <b>(+47.52%)</b></td><td>0.02 <b>(-41.01%)</b></td><td>422.10 <b>(-32.20%)</b></td><td>350.80 <b>(-24.82%)</b></td><td>316.60 <b>(-39.58%)</b></td><td>293.30 (+2.05%)</td><td>65.36 <b>(-57.66%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>622.60 (n/a)</td><td>466.60 (n/a)</td><td>524.00 (n/a)</td><td>287.40 (n/a)</td><td>154.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (+4.03%)</td><td>0.06 <b>(-21.28%)</b></td><td>0.06 <b>(-22.99%)</b></td><td>0.02 <b>(-68.20%)</b></td><td>0.04 <b>(+55.97%)</b></td><td>1903.30 <b>(+214.44%)</b></td><td>782.26 <b>(+80.59%)</b></td><td>545.80 <b>(+29.86%)</b></td><td>290.00 (-3.88%)</td><td>657.91 <b>(+396.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>605.30 (n/a)</td><td>433.18 (n/a)</td><td>420.30 (n/a)</td><td>301.70 (n/a)</td><td>132.39 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 <b>(+78.55%)</b></td><td>0.08 (+16.78%)</td><td>0.08 <b>(+24.76%)</b></td><td>0.03 <b>(-45.28%)</b></td><td>0.04 <b>(+409.04%)</b></td><td>1052.60 <b>(+82.74%)</b></td><td>546.00 (+6.49%)</td><td>429.50 (-19.85%)</td><td>241.00 <b>(-44.01%)</b></td><td>308.41 <b>(+439.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>576.00 (n/a)</td><td>512.72 (n/a)</td><td>535.90 (n/a)</td><td>430.40 (n/a)</td><td>57.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 <b>(+23.33%)</b></td><td>0.08 (+19.02%)</td><td>0.06 (-2.82%)</td><td>0.05 (-1.93%)</td><td>0.03 <b>(+85.18%)</b></td><td>629.60 (+1.98%)</td><td>456.82 (-10.14%)</td><td>520.60 (+2.91%)</td><td>283.30 (-18.92%)</td><td>156.54 <b>(+46.04%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>617.40 (n/a)</td><td>508.38 (n/a)</td><td>505.90 (n/a)</td><td>349.40 (n/a)</td><td>107.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-22.60%)</b></td><td>0.01 (-5.11%)</td><td>0.01 (+15.29%)</td><td>0.01 (+4.26%)</td><td>0.00 <b>(-27.91%)</b></td><td>604.10 (-4.10%)</td><td>389.74 (+1.12%)</td><td>315.70 (-13.27%)</td><td>293.20 <b>(+29.22%)</b></td><td>134.52 (-13.80%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.90 (n/a)</td><td>385.42 (n/a)</td><td>364.00 (n/a)</td><td>226.90 (n/a)</td><td>156.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-8.57%)</td><td>0.01 (+2.43%)</td><td>0.01 (+1.55%)</td><td>0.01 <b>(+31.67%)</b></td><td>0.00 <b>(-45.84%)</b></td><td>333.40 <b>(-24.05%)</b></td><td>293.40 (-5.61%)</td><td>293.40 (-1.51%)</td><td>248.60 (+9.37%)</td><td>33.96 <b>(-56.39%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>439.00 (n/a)</td><td>310.84 (n/a)</td><td>297.90 (n/a)</td><td>227.30 (n/a)</td><td>77.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-26.44%)</b></td><td>0.01 (-19.05%)</td><td>0.01 <b>(-38.65%)</b></td><td>0.01 (+12.62%)</td><td>0.00 <b>(-44.69%)</b></td><td>496.80 (-11.21%)</td><td>392.90 (+11.50%)</td><td>434.20 <b>(+62.99%)</b></td><td>283.90 <b>(+35.90%)</b></td><td>101.71 <b>(-37.69%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.50 (n/a)</td><td>352.38 (n/a)</td><td>266.40 (n/a)</td><td>208.90 (n/a)</td><td>163.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-8.66%)</td><td>0.01 (-6.17%)</td><td>0.01 (-12.67%)</td><td>0.01 (+0.52%)</td><td>0.00 (-13.26%)</td><td>530.80 (-0.51%)</td><td>389.00 (+4.60%)</td><td>337.00 (+14.51%)</td><td>251.20 (+9.50%)</td><td>132.64 (-5.38%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.50 (n/a)</td><td>371.88 (n/a)</td><td>294.30 (n/a)</td><td>229.40 (n/a)</td><td>140.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-41.48%)</b></td><td>0.01 <b>(-25.56%)</b></td><td>0.01 (+14.81%)</td><td>0.00 <b>(-44.16%)</b></td><td>0.00 <b>(-48.63%)</b></td><td>1882.90 <b>(+79.07%)</b></td><td>695.06 <b>(+34.15%)</b></td><td>422.70 (-12.90%)</td><td>280.00 <b>(+70.84%)</b></td><td>667.96 <b>(+88.45%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1051.50 (n/a)</td><td>518.14 (n/a)</td><td>485.30 (n/a)</td><td>163.90 (n/a)</td><td>354.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-25.42%)</b></td><td>0.01 <b>(-27.88%)</b></td><td>0.01 <b>(-42.69%)</b></td><td>0.01 <b>(+20.13%)</b></td><td>0.00 <b>(-54.64%)</b></td><td>562.30 (-16.76%)</td><td>444.72 (+16.30%)</td><td>464.30 <b>(+74.48%)</b></td><td>280.10 <b>(+34.08%)</b></td><td>109.33 <b>(-49.27%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.50 (n/a)</td><td>382.40 (n/a)</td><td>266.10 (n/a)</td><td>208.90 (n/a)</td><td>215.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(+22.16%)</b></td><td>0.01 <b>(+35.13%)</b></td><td>0.01 (+14.71%)</td><td>0.01 <b>(+345.31%)</b></td><td>0.00 <b>(-48.26%)</b></td><td>539.70 <b>(-77.55%)</b></td><td>449.96 <b>(-49.27%)</b></td><td>460.10 (-12.83%)</td><td>365.60 (-18.14%)</td><td>75.28 <b>(-91.15%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2403.50 (n/a)</td><td>887.04 (n/a)</td><td>527.80 (n/a)</td><td>446.60 (n/a)</td><td>850.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-30.70%)</b></td><td>0.01 (-14.98%)</td><td>0.01 <b>(-29.68%)</b></td><td>0.01 (+14.02%)</td><td>0.00 <b>(-44.81%)</b></td><td>482.60 (-12.29%)</td><td>397.66 (+9.22%)</td><td>438.00 <b>(+42.21%)</b></td><td>290.90 <b>(+44.30%)</b></td><td>94.83 <b>(-32.45%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.20 (n/a)</td><td>364.08 (n/a)</td><td>308.00 (n/a)</td><td>201.60 (n/a)</td><td>140.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (-11.42%)</td><td>0.01 (+14.63%)</td><td>0.01 <b>(+21.24%)</b></td><td>0.01 <b>(+211.09%)</b></td><td>0.00 <b>(-61.30%)</b></td><td>598.00 <b>(-67.85%)</b></td><td>493.42 <b>(-40.36%)</b></td><td>482.90 (-17.51%)</td><td>359.50 (+12.87%)</td><td>91.17 <b>(-85.72%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1860.20 (n/a)</td><td>827.30 (n/a)</td><td>585.40 (n/a)</td><td>318.50 (n/a)</td><td>638.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(+28.24%)</b></td><td>0.01 <b>(+25.49%)</b></td><td>0.01 <b>(+31.75%)</b></td><td>0.01 (+19.64%)</td><td>0.00 (+10.25%)</td><td>407.70 (-16.42%)</td><td>303.28 <b>(-20.97%)</b></td><td>290.90 <b>(-24.09%)</b></td><td>226.60 <b>(-22.02%)</b></td><td>65.57 <b>(-25.75%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.80 (n/a)</td><td>383.76 (n/a)</td><td>383.20 (n/a)</td><td>290.60 (n/a)</td><td>88.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(+21.34%)</b></td><td>0.01 (-8.85%)</td><td>0.01 (-13.62%)</td><td>0.01 (-18.48%)</td><td>0.00 <b>(+52.88%)</b></td><td>800.10 <b>(+22.66%)</b></td><td>579.64 (+19.04%)</td><td>636.60 (+15.77%)</td><td>251.00 (-17.60%)</td><td>202.07 <b>(+42.40%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>652.30 (n/a)</td><td>486.92 (n/a)</td><td>549.90 (n/a)</td><td>304.60 (n/a)</td><td>141.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (-4.82%)</td><td>0.01 (+14.36%)</td><td>0.01 <b>(+36.46%)</b></td><td>0.01 <b>(+72.00%)</b></td><td>0.00 (-19.98%)</td><td>616.40 <b>(-41.86%)</b></td><td>429.48 <b>(-21.96%)</b></td><td>371.90 <b>(-26.72%)</b></td><td>298.50 (+5.07%)</td><td>145.80 <b>(-52.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1060.20 (n/a)</td><td>550.34 (n/a)</td><td>507.50 (n/a)</td><td>284.10 (n/a)</td><td>305.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (+4.02%)</td><td>0.02 (+10.49%)</td><td>0.03 <b>(+39.97%)</b></td><td>0.02 (-8.73%)</td><td>0.01 <b>(+28.14%)</b></td><td>520.20 (+9.56%)</td><td>368.34 (-4.88%)</td><td>294.60 <b>(-28.55%)</b></td><td>232.80 (-3.84%)</td><td>135.34 <b>(+51.97%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>474.80 (n/a)</td><td>387.22 (n/a)</td><td>412.30 (n/a)</td><td>242.10 (n/a)</td><td>89.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (+15.27%)</td><td>0.03 (-1.53%)</td><td>0.03 (-8.38%)</td><td>0.02 (-0.32%)</td><td>0.01 <b>(+48.14%)</b></td><td>483.40 (+0.33%)</td><td>341.20 (+5.59%)</td><td>303.60 (+9.17%)</td><td>237.20 (-13.27%)</td><td>113.64 <b>(+26.42%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.80 (n/a)</td><td>323.14 (n/a)</td><td>278.10 (n/a)</td><td>273.50 (n/a)</td><td>89.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (-14.95%)</td><td>0.02 <b>(+21.11%)</b></td><td>0.02 <b>(+46.57%)</b></td><td>0.02 <b>(+52.52%)</b></td><td>0.01 <b>(-31.66%)</b></td><td>476.30 <b>(-34.44%)</b></td><td>355.50 <b>(-24.82%)</b></td><td>332.50 <b>(-31.78%)</b></td><td>242.90 (+17.57%)</td><td>109.40 <b>(-41.27%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>726.50 (n/a)</td><td>472.86 (n/a)</td><td>487.40 (n/a)</td><td>206.60 (n/a)</td><td>186.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(-33.45%)</b></td><td>0.02 <b>(-30.23%)</b></td><td>0.02 <b>(-33.07%)</b></td><td>0.01 (-5.92%)</td><td>0.00 <b>(-52.12%)</b></td><td>558.90 (+6.30%)</td><td>453.64 <b>(+35.23%)</b></td><td>435.40 <b>(+49.42%)</b></td><td>339.60 <b>(+50.27%)</b></td><td>98.97 <b>(-20.22%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.80 (n/a)</td><td>335.46 (n/a)</td><td>291.40 (n/a)</td><td>226.00 (n/a)</td><td>124.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 <b>(+30.71%)</b></td><td>0.02 (+5.88%)</td><td>0.02 (+4.13%)</td><td>0.01 (-16.01%)</td><td>0.01 <b>(+113.30%)</b></td><td>602.50 (+19.07%)</td><td>449.16 (+0.37%)</td><td>444.50 (-3.95%)</td><td>257.10 <b>(-23.48%)</b></td><td>128.21 <b>(+88.06%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>506.00 (n/a)</td><td>447.52 (n/a)</td><td>462.80 (n/a)</td><td>336.00 (n/a)</td><td>68.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (+9.48%)</td><td>0.03 (+7.05%)</td><td>0.03 (+2.82%)</td><td>0.02 (-1.15%)</td><td>0.01 (+3.18%)</td><td>526.50 (+1.15%)</td><td>343.12 (-6.31%)</td><td>300.00 (-2.72%)</td><td>263.00 (-8.65%)</td><td>105.74 (+2.74%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.50 (n/a)</td><td>366.24 (n/a)</td><td>308.40 (n/a)</td><td>287.90 (n/a)</td><td>102.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(+23.02%)</b></td><td>0.03 <b>(+59.27%)</b></td><td>0.03 <b>(+113.88%)</b></td><td>0.02 <b>(+114.99%)</b></td><td>0.01 (-0.25%)</td><td>510.30 <b>(-53.48%)</b></td><td>316.82 <b>(-46.54%)</b></td><td>277.50 <b>(-53.24%)</b></td><td>161.80 (-18.73%)</td><td>130.74 <b>(-60.11%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1097.00 (n/a)</td><td>592.66 (n/a)</td><td>593.40 (n/a)</td><td>199.10 (n/a)</td><td>327.75 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 <b>(-23.39%)</b></td><td>0.02 <b>(-24.95%)</b></td><td>0.02 (-1.57%)</td><td>0.00 <b>(-77.70%)</b></td><td>0.01 (-2.87%)</td><td>2394.30 <b>(+348.54%)</b></td><td>807.70 <b>(+103.16%)</b></td><td>470.30 (+1.60%)</td><td>303.30 <b>(+30.56%)</b></td><td>891.58 <b>(+533.16%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.80 (n/a)</td><td>397.56 (n/a)</td><td>462.90 (n/a)</td><td>232.30 (n/a)</td><td>140.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 <b>(-22.72%)</b></td><td>0.02 (-6.77%)</td><td>0.02 <b>(+42.04%)</b></td><td>0.00 <b>(-77.94%)</b></td><td>0.01 (-0.78%)</td><td>2456.30 <b>(+353.36%)</b></td><td>788.28 <b>(+77.60%)</b></td><td>365.80 <b>(-29.60%)</b></td><td>254.10 <b>(+29.44%)</b></td><td>939.99 <b>(+549.71%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.80 (n/a)</td><td>443.84 (n/a)</td><td>519.60 (n/a)</td><td>196.30 (n/a)</td><td>144.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (+3.06%)</td><td>0.02 (-15.17%)</td><td>0.02 (-18.42%)</td><td>0.01 <b>(-27.77%)</b></td><td>0.01 <b>(+38.93%)</b></td><td>658.30 <b>(+38.47%)</b></td><td>502.58 <b>(+24.77%)</b></td><td>534.20 <b>(+22.58%)</b></td><td>265.80 (-2.96%)</td><td>149.00 <b>(+75.18%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.40 (n/a)</td><td>402.80 (n/a)</td><td>435.80 (n/a)</td><td>273.90 (n/a)</td><td>85.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-16.82%)</td><td>0.02 (+8.56%)</td><td>0.02 (+9.29%)</td><td>0.01 <b>(+41.90%)</b></td><td>0.00 <b>(-49.09%)</b></td><td>553.40 <b>(-29.53%)</b></td><td>461.34 (-15.21%)</td><td>484.20 (-8.50%)</td><td>365.20 <b>(+20.21%)</b></td><td>80.54 <b>(-57.20%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>785.30 (n/a)</td><td>544.10 (n/a)</td><td>529.20 (n/a)</td><td>303.80 (n/a)</td><td>188.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-8.26%)</td><td>0.01 (+16.69%)</td><td>0.01 <b>(+36.77%)</b></td><td>0.01 <b>(+88.64%)</b></td><td>0.01 <b>(-32.17%)</b></td><td>1035.80 <b>(-46.99%)</b></td><td>645.08 <b>(-40.73%)</b></td><td>563.50 <b>(-26.88%)</b></td><td>333.50 (+8.99%)</td><td>281.06 <b>(-65.19%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1953.80 (n/a)</td><td>1088.36 (n/a)</td><td>770.60 (n/a)</td><td>306.00 (n/a)</td><td>807.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+15.48%)</td><td>0.04 (-9.24%)</td><td>0.03 <b>(-33.17%)</b></td><td>0.03 (+8.21%)</td><td>0.02 <b>(+40.68%)</b></td><td>516.40 (-7.59%)</td><td>412.44 (+14.12%)</td><td>480.90 <b>(+49.63%)</b></td><td>235.70 (-13.41%)</td><td>128.82 (+12.33%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.80 (n/a)</td><td>361.42 (n/a)</td><td>321.40 (n/a)</td><td>272.20 (n/a)</td><td>114.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (-9.12%)</td><td>0.05 (-7.67%)</td><td>0.05 (-4.62%)</td><td>0.02 <b>(-34.99%)</b></td><td>0.02 (+19.85%)</td><td>722.10 <b>(+53.83%)</b></td><td>408.90 (+17.01%)</td><td>338.90 (+4.86%)</td><td>259.70 (+10.04%)</td><td>191.71 <b>(+93.80%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>469.40 (n/a)</td><td>349.46 (n/a)</td><td>323.20 (n/a)</td><td>236.00 (n/a)</td><td>98.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+0.80%)</td><td>0.04 (+19.70%)</td><td>0.03 (+8.09%)</td><td>0.03 <b>(+130.50%)</b></td><td>0.02 (-16.63%)</td><td>587.00 <b>(-56.62%)</b></td><td>436.08 <b>(-31.18%)</b></td><td>502.60 (-7.49%)</td><td>229.00 (-0.78%)</td><td>146.76 <b>(-65.36%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1353.10 (n/a)</td><td>633.64 (n/a)</td><td>543.30 (n/a)</td><td>230.80 (n/a)</td><td>423.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (+19.16%)</td><td>0.05 (-5.00%)</td><td>0.05 (-10.30%)</td><td>0.01 <b>(-55.90%)</b></td><td>0.03 <b>(+51.85%)</b></td><td>1113.30 <b>(+126.74%)</b></td><td>471.70 <b>(+34.73%)</b></td><td>307.30 (+11.46%)</td><td>204.10 (-16.08%)</td><td>371.40 <b>(+197.23%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>491.00 (n/a)</td><td>350.10 (n/a)</td><td>275.70 (n/a)</td><td>243.20 (n/a)</td><td>124.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 <b>(-47.79%)</b></td><td>0.04 <b>(-34.84%)</b></td><td>0.04 (+0.12%)</td><td>0.03 (-14.07%)</td><td>0.01 <b>(-70.19%)</b></td><td>592.40 (+16.36%)</td><td>448.22 <b>(+25.78%)</b></td><td>452.50 (-0.11%)</td><td>295.20 <b>(+91.56%)</b></td><td>106.29 <b>(-37.31%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>509.10 (n/a)</td><td>356.34 (n/a)</td><td>453.00 (n/a)</td><td>154.10 (n/a)</td><td>169.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (+1.56%)</td><td>0.05 <b>(+21.02%)</b></td><td>0.06 (+15.12%)</td><td>0.03 <b>(+257.71%)</b></td><td>0.01 <b>(-42.03%)</b></td><td>512.70 <b>(-72.05%)</b></td><td>332.88 <b>(-48.11%)</b></td><td>272.30 (-13.14%)</td><td>253.40 (-1.52%)</td><td>108.54 <b>(-83.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1834.10 (n/a)</td><td>641.50 (n/a)</td><td>313.50 (n/a)</td><td>257.30 (n/a)</td><td>676.78 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+5.93%)</td><td>0.05 (+0.50%)</td><td>0.05 (-17.44%)</td><td>0.03 (-9.70%)</td><td>0.02 (+2.68%)</td><td>571.70 (+10.75%)</td><td>350.32 (+0.01%)</td><td>320.70 <b>(+21.11%)</b></td><td>231.20 (-5.59%)</td><td>138.03 (+5.91%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>516.20 (n/a)</td><td>350.28 (n/a)</td><td>264.80 (n/a)</td><td>244.90 (n/a)</td><td>130.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(-44.70%)</b></td><td>0.03 <b>(-47.35%)</b></td><td>0.03 <b>(-48.98%)</b></td><td>0.01 <b>(-48.30%)</b></td><td>0.01 <b>(-44.32%)</b></td><td>1106.40 <b>(+93.43%)</b></td><td>640.68 <b>(+91.42%)</b></td><td>538.80 <b>(+96.00%)</b></td><td>456.60 <b>(+80.83%)</b></td><td>265.38 <b>(+97.82%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>334.70 (n/a)</td><td>274.90 (n/a)</td><td>252.50 (n/a)</td><td>134.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (-13.18%)</td><td>0.04 <b>(-20.30%)</b></td><td>0.03 <b>(-38.62%)</b></td><td>0.03 (-19.93%)</td><td>0.02 (-4.42%)</td><td>619.90 <b>(+24.90%)</b></td><td>440.30 <b>(+28.01%)</b></td><td>473.90 <b>(+62.91%)</b></td><td>279.90 (+15.19%)</td><td>152.50 <b>(+30.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>496.30 (n/a)</td><td>343.96 (n/a)</td><td>290.90 (n/a)</td><td>243.00 (n/a)</td><td>116.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 <b>(+25.63%)</b></td><td>0.04 <b>(-23.14%)</b></td><td>0.04 <b>(-43.35%)</b></td><td>0.01 <b>(-72.69%)</b></td><td>0.03 <b>(+54.24%)</b></td><td>1927.20 <b>(+266.18%)</b></td><td>701.02 <b>(+98.58%)</b></td><td>461.40 <b>(+76.51%)</b></td><td>192.80 <b>(-20.40%)</b></td><td>695.57 <b>(+397.69%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>526.30 (n/a)</td><td>353.02 (n/a)</td><td>261.40 (n/a)</td><td>242.20 (n/a)</td><td>139.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(-27.00%)</b></td><td>0.04 <b>(-29.16%)</b></td><td>0.03 <b>(-42.75%)</b></td><td>0.03 (-1.60%)</td><td>0.01 <b>(-42.29%)</b></td><td>625.30 (+1.63%)</td><td>482.68 <b>(+33.22%)</b></td><td>516.10 <b>(+74.65%)</b></td><td>340.10 <b>(+36.97%)</b></td><td>118.44 <b>(-21.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.30 (n/a)</td><td>362.32 (n/a)</td><td>295.50 (n/a)</td><td>248.30 (n/a)</td><td>151.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(-36.78%)</b></td><td>0.03 <b>(-23.88%)</b></td><td>0.03 (+1.93%)</td><td>0.02 (-15.59%)</td><td>0.01 <b>(-60.00%)</b></td><td>699.90 (+18.49%)</td><td>506.10 (+17.79%)</td><td>494.80 (-1.88%)</td><td>350.80 <b>(+58.16%)</b></td><td>125.55 <b>(-25.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.70 (n/a)</td><td>429.68 (n/a)</td><td>504.30 (n/a)</td><td>221.80 (n/a)</td><td>169.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (-13.47%)</td><td>0.08 (-14.42%)</td><td>0.07 (+8.38%)</td><td>0.05 (-6.91%)</td><td>0.04 <b>(-27.51%)</b></td><td>628.00 (+7.42%)</td><td>449.80 (+8.73%)</td><td>463.80 (-7.74%)</td><td>229.70 (+15.60%)</td><td>149.70 (-15.12%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>584.60 (n/a)</td><td>413.70 (n/a)</td><td>502.70 (n/a)</td><td>198.70 (n/a)</td><td>176.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.17 (+2.50%)</td><td>0.12 (+5.99%)</td><td>0.11 (-17.34%)</td><td>0.08 <b>(+43.70%)</b></td><td>0.04 <b>(-20.94%)</b></td><td>432.90 <b>(-30.41%)</b></td><td>306.38 (-15.22%)</td><td>304.90 <b>(+20.99%)</b></td><td>196.60 (-2.43%)</td><td>96.47 <b>(-47.81%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>622.10 (n/a)</td><td>361.40 (n/a)</td><td>252.00 (n/a)</td><td>201.50 (n/a)</td><td>184.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 <b>(-26.36%)</b></td><td>0.10 <b>(-23.67%)</b></td><td>0.12 (-0.36%)</td><td>0.06 <b>(-45.59%)</b></td><td>0.04 <b>(+22.06%)</b></td><td>578.10 <b>(+83.82%)</b></td><td>391.14 <b>(+45.28%)</b></td><td>281.80 (+0.36%)</td><td>250.80 <b>(+35.79%)</b></td><td>169.53 <b>(+226.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>314.50 (n/a)</td><td>269.24 (n/a)</td><td>280.80 (n/a)</td><td>184.70 (n/a)</td><td>51.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (-9.02%)</td><td>0.09 (-9.73%)</td><td>0.08 (-8.49%)</td><td>0.06 (-4.07%)</td><td>0.03 (-18.12%)</td><td>554.80 (+4.25%)</td><td>411.10 (+8.48%)</td><td>423.30 (+9.30%)</td><td>265.10 (+9.91%)</td><td>129.47 (-2.83%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>532.20 (n/a)</td><td>378.96 (n/a)</td><td>387.30 (n/a)</td><td>241.20 (n/a)</td><td>133.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.17 <b>(+25.14%)</b></td><td>0.10 (-5.52%)</td><td>0.08 <b>(-38.76%)</b></td><td>0.07 (+15.52%)</td><td>0.04 (+11.73%)</td><td>471.60 (-13.44%)</td><td>363.28 (+4.50%)</td><td>406.80 <b>(+63.31%)</b></td><td>195.10 <b>(-20.11%)</b></td><td>114.30 (-19.24%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>544.80 (n/a)</td><td>347.64 (n/a)</td><td>249.10 (n/a)</td><td>244.20 (n/a)</td><td>141.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (-11.64%)</td><td>0.10 (-7.34%)</td><td>0.11 (-8.86%)</td><td>0.07 (+12.10%)</td><td>0.03 <b>(-20.62%)</b></td><td>488.30 (-10.80%)</td><td>365.12 (+4.53%)</td><td>302.50 (+9.72%)</td><td>277.80 (+13.16%)</td><td>108.03 (-17.56%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.40 (n/a)</td><td>349.30 (n/a)</td><td>275.70 (n/a)</td><td>245.50 (n/a)</td><td>131.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (-18.66%)</td><td>0.08 (+3.39%)</td><td>0.07 (+6.13%)</td><td>0.06 (+0.98%)</td><td>0.03 <b>(-23.08%)</b></td><td>591.60 (-0.95%)</td><td>427.66 (-5.80%)</td><td>455.60 (-5.77%)</td><td>290.00 <b>(+22.93%)</b></td><td>129.49 (-5.50%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>597.30 (n/a)</td><td>454.00 (n/a)</td><td>483.50 (n/a)</td><td>235.90 (n/a)</td><td>137.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 <b>(+33.93%)</b></td><td>0.09 (+0.36%)</td><td>0.07 <b>(-40.92%)</b></td><td>0.05 (-15.13%)</td><td>0.05 <b>(+83.34%)</b></td><td>609.90 (+17.81%)</td><td>418.82 (+12.01%)</td><td>502.70 <b>(+69.26%)</b></td><td>214.70 <b>(-25.32%)</b></td><td>180.12 <b>(+58.13%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.70 (n/a)</td><td>373.90 (n/a)</td><td>297.00 (n/a)</td><td>287.50 (n/a)</td><td>113.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 <b>(-46.50%)</b></td><td>0.07 <b>(-23.49%)</b></td><td>0.07 (-1.15%)</td><td>0.06 (+9.61%)</td><td>0.01 <b>(-77.28%)</b></td><td>552.20 (-8.77%)</td><td>465.78 (+14.06%)</td><td>437.30 (+1.16%)</td><td>399.60 <b>(+86.90%)</b></td><td>64.80 <b>(-60.48%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>605.30 (n/a)</td><td>408.36 (n/a)</td><td>432.30 (n/a)</td><td>213.80 (n/a)</td><td>163.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (+18.39%)</td><td>0.08 (-10.57%)</td><td>0.07 <b>(-30.71%)</b></td><td>0.06 <b>(+45.40%)</b></td><td>0.03 (+7.92%)</td><td>524.50 <b>(-31.23%)</b></td><td>429.46 (+6.29%)</td><td>462.70 <b>(+44.32%)</b></td><td>228.20 (-15.51%)</td><td>116.68 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>762.70 (n/a)</td><td>404.06 (n/a)</td><td>320.60 (n/a)</td><td>270.10 (n/a)</td><td>205.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (+13.20%)</td><td>0.08 (-1.36%)</td><td>0.06 <b>(-21.45%)</b></td><td>0.05 <b>(+29.36%)</b></td><td>0.03 (+9.56%)</td><td>596.00 <b>(-22.70%)</b></td><td>464.38 (-0.54%)</td><td>525.10 <b>(+27.33%)</b></td><td>273.00 (-11.65%)</td><td>131.43 <b>(-28.16%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>771.00 (n/a)</td><td>466.92 (n/a)</td><td>412.40 (n/a)</td><td>309.00 (n/a)</td><td>182.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 <b>(-29.01%)</b></td><td>0.08 (-7.64%)</td><td>0.07 (+10.53%)</td><td>0.05 (+1.57%)</td><td>0.03 <b>(-43.96%)</b></td><td>635.90 (-1.55%)</td><td>452.96 (-3.11%)</td><td>460.30 (-9.53%)</td><td>248.90 <b>(+40.86%)</b></td><td>147.43 (-19.14%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>645.90 (n/a)</td><td>467.52 (n/a)</td><td>508.80 (n/a)</td><td>176.70 (n/a)</td><td>182.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 <b>(+70.69%)</b></td><td>0.01 <b>(+59.93%)</b></td><td>0.01 <b>(+70.27%)</b></td><td>0.01 <b>(+20.39%)</b></td><td>0.00 <b>(+177.09%)</b></td><td>500.50 (-16.94%)</td><td>329.40 <b>(-34.09%)</b></td><td>299.20 <b>(-41.28%)</b></td><td>236.10 <b>(-41.41%)</b></td><td>106.92 <b>(+35.86%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.60 (n/a)</td><td>499.80 (n/a)</td><td>509.50 (n/a)</td><td>403.00 (n/a)</td><td>78.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-10.98%)</td><td>0.01 (-11.99%)</td><td>0.01 <b>(-25.42%)</b></td><td>0.01 <b>(-54.91%)</b></td><td>0.01 <b>(+30.66%)</b></td><td>1088.70 <b>(+121.78%)</b></td><td>551.42 <b>(+39.64%)</b></td><td>546.50 <b>(+34.08%)</b></td><td>245.90 (+12.33%)</td><td>339.45 <b>(+217.47%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>490.90 (n/a)</td><td>394.90 (n/a)</td><td>407.60 (n/a)</td><td>218.90 (n/a)</td><td>106.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-10.17%)</td><td>0.01 <b>(-26.79%)</b></td><td>0.01 <b>(-40.71%)</b></td><td>0.01 <b>(-22.59%)</b></td><td>0.00 (+0.22%)</td><td>632.40 <b>(+29.19%)</b></td><td>475.76 <b>(+39.64%)</b></td><td>498.00 <b>(+68.70%)</b></td><td>268.50 (+11.32%)</td><td>138.68 <b>(+36.57%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.50 (n/a)</td><td>340.70 (n/a)</td><td>295.20 (n/a)</td><td>241.20 (n/a)</td><td>101.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-3.85%)</td><td>0.01 (-15.95%)</td><td>0.01 (-9.60%)</td><td>0.00 <b>(-67.06%)</b></td><td>0.01 <b>(+41.66%)</b></td><td>2055.90 <b>(+203.59%)</b></td><td>788.64 <b>(+65.69%)</b></td><td>529.20 (+10.62%)</td><td>312.40 (+4.03%)</td><td>716.33 <b>(+415.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>677.20 (n/a)</td><td>475.96 (n/a)</td><td>478.40 (n/a)</td><td>300.30 (n/a)</td><td>139.01 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-21.11%)</b></td><td>0.01 <b>(-28.90%)</b></td><td>0.01 <b>(-48.85%)</b></td><td>0.01 (-15.49%)</td><td>0.00 <b>(-36.39%)</b></td><td>746.30 (+18.33%)</td><td>499.66 <b>(+29.16%)</b></td><td>530.10 <b>(+95.54%)</b></td><td>273.20 <b>(+26.72%)</b></td><td>173.71 (-11.62%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.70 (n/a)</td><td>386.84 (n/a)</td><td>271.10 (n/a)</td><td>215.60 (n/a)</td><td>196.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-41.75%)</b></td><td>0.01 <b>(-30.53%)</b></td><td>0.01 <b>(-28.96%)</b></td><td>0.01 (-16.98%)</td><td>0.00 <b>(-66.13%)</b></td><td>610.50 <b>(+20.44%)</b></td><td>546.20 <b>(+39.58%)</b></td><td>573.30 <b>(+40.76%)</b></td><td>474.10 <b>(+71.71%)</b></td><td>60.35 <b>(-29.59%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.90 (n/a)</td><td>391.32 (n/a)</td><td>407.30 (n/a)</td><td>276.10 (n/a)</td><td>85.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(+28.33%)</b></td><td>0.01 (+1.92%)</td><td>0.01 (+6.83%)</td><td>0.01 (-18.37%)</td><td>0.00 <b>(+102.57%)</b></td><td>597.50 <b>(+22.51%)</b></td><td>446.96 (+2.22%)</td><td>440.60 (-6.39%)</td><td>289.20 <b>(-22.07%)</b></td><td>112.10 <b>(+89.29%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.70 (n/a)</td><td>437.26 (n/a)</td><td>470.70 (n/a)</td><td>371.10 (n/a)</td><td>59.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (+3.85%)</td><td>0.01 <b>(+29.94%)</b></td><td>0.02 <b>(+50.95%)</b></td><td>0.01 <b>(+42.23%)</b></td><td>0.00 <b>(-28.16%)</b></td><td>444.10 <b>(-29.70%)</b></td><td>318.76 <b>(-27.68%)</b></td><td>281.80 <b>(-33.74%)</b></td><td>263.70 (-3.72%)</td><td>74.46 <b>(-50.87%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>631.70 (n/a)</td><td>440.78 (n/a)</td><td>425.30 (n/a)</td><td>273.90 (n/a)</td><td>151.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (-13.05%)</td><td>0.01 (+2.64%)</td><td>0.01 <b>(+37.07%)</b></td><td>0.01 (+6.46%)</td><td>0.00 <b>(-27.63%)</b></td><td>513.40 (-6.07%)</td><td>379.22 (-7.88%)</td><td>352.90 <b>(-27.04%)</b></td><td>268.90 (+15.01%)</td><td>115.82 <b>(-23.00%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.60 (n/a)</td><td>411.66 (n/a)</td><td>483.70 (n/a)</td><td>233.80 (n/a)</td><td>150.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (-13.99%)</td><td>0.01 (-19.57%)</td><td>0.01 (-16.13%)</td><td>0.00 <b>(-72.08%)</b></td><td>0.00 (+16.63%)</td><td>2449.40 <b>(+258.20%)</b></td><td>881.66 <b>(+81.76%)</b></td><td>572.70 (+19.24%)</td><td>316.00 (+16.30%)</td><td>882.80 <b>(+493.78%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>683.80 (n/a)</td><td>485.08 (n/a)</td><td>480.30 (n/a)</td><td>271.70 (n/a)</td><td>148.67 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 <b>(-26.02%)</b></td><td>0.01 (-10.27%)</td><td>0.01 (+0.29%)</td><td>0.00 <b>(-38.84%)</b></td><td>0.00 (-15.81%)</td><td>1109.50 <b>(+63.52%)</b></td><td>602.86 (+17.77%)</td><td>558.90 (-0.30%)</td><td>372.50 <b>(+35.16%)</b></td><td>298.82 <b>(+97.06%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>678.50 (n/a)</td><td>511.90 (n/a)</td><td>560.60 (n/a)</td><td>275.60 (n/a)</td><td>151.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+24.73%)</b></td><td>0.03 (-10.47%)</td><td>0.03 (-4.23%)</td><td>0.01 <b>(-48.85%)</b></td><td>0.01 <b>(+617.80%)</b></td><td>548.00 <b>(+95.50%)</b></td><td>337.86 <b>(+25.47%)</b></td><td>284.00 (+4.41%)</td><td>200.00 (-19.84%)</td><td>135.80 <b>(+1065.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>280.30 (n/a)</td><td>269.28 (n/a)</td><td>272.00 (n/a)</td><td>249.50 (n/a)</td><td>11.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (-6.03%)</td><td>0.04 (+2.26%)</td><td>0.04 (-3.21%)</td><td>0.02 (+3.94%)</td><td>0.01 (-11.02%)</td><td>496.50 (-3.80%)</td><td>344.10 (-4.15%)</td><td>299.10 (+3.32%)</td><td>259.00 (+6.41%)</td><td>104.43 (-14.25%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>359.00 (n/a)</td><td>289.50 (n/a)</td><td>243.40 (n/a)</td><td>121.78 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+43.83%)</b></td><td>0.02 <b>(+28.58%)</b></td><td>0.02 <b>(+29.59%)</b></td><td>0.02 <b>(+27.98%)</b></td><td>0.01 <b>(+58.40%)</b></td><td>479.90 <b>(-21.87%)</b></td><td>355.04 <b>(-20.99%)</b></td><td>339.50 <b>(-22.84%)</b></td><td>228.90 <b>(-30.49%)</b></td><td>95.83 (-14.24%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.20 (n/a)</td><td>449.36 (n/a)</td><td>440.00 (n/a)</td><td>329.30 (n/a)</td><td>111.75 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(+23.26%)</b></td><td>0.03 (+8.10%)</td><td>0.04 (+3.36%)</td><td>0.02 (-0.66%)</td><td>0.01 <b>(+31.45%)</b></td><td>627.70 (+0.67%)</td><td>367.32 (-2.79%)</td><td>271.10 (-3.25%)</td><td>195.60 (-18.87%)</td><td>179.61 (+10.48%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>623.50 (n/a)</td><td>377.88 (n/a)</td><td>280.20 (n/a)</td><td>241.10 (n/a)</td><td>162.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (-2.37%)</td><td>0.02 (+8.57%)</td><td>0.02 (+7.29%)</td><td>0.01 <b>(+32.10%)</b></td><td>0.01 (-12.62%)</td><td>568.00 <b>(-24.30%)</b></td><td>412.42 (-12.80%)</td><td>427.40 (-6.80%)</td><td>254.10 (+2.42%)</td><td>134.60 <b>(-31.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>750.30 (n/a)</td><td>472.94 (n/a)</td><td>458.60 (n/a)</td><td>248.10 (n/a)</td><td>197.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(-41.32%)</b></td><td>0.03 (-1.71%)</td><td>0.04 <b>(+59.32%)</b></td><td>0.02 (-12.90%)</td><td>0.01 <b>(-45.05%)</b></td><td>628.30 (+14.82%)</td><td>392.50 (-5.35%)</td><td>284.10 <b>(-37.23%)</b></td><td>264.60 <b>(+70.38%)</b></td><td>170.51 (+13.19%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>547.20 (n/a)</td><td>414.68 (n/a)</td><td>452.60 (n/a)</td><td>155.30 (n/a)</td><td>150.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+64.83%)</b></td><td>0.02 (+19.89%)</td><td>0.02 (-11.00%)</td><td>0.01 (-3.27%)</td><td>0.01 <b>(+139.46%)</b></td><td>622.60 (+3.39%)</td><td>422.04 (-5.07%)</td><td>459.40 (+12.35%)</td><td>193.90 <b>(-39.33%)</b></td><td>179.93 <b>(+48.89%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.20 (n/a)</td><td>444.58 (n/a)</td><td>408.90 (n/a)</td><td>319.60 (n/a)</td><td>120.84 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (-7.87%)</td><td>0.03 (+6.14%)</td><td>0.03 <b>(+45.11%)</b></td><td>0.01 (-14.03%)</td><td>0.01 (-9.63%)</td><td>667.60 (+16.31%)</td><td>389.44 (-5.59%)</td><td>294.60 <b>(-31.09%)</b></td><td>209.90 (+8.53%)</td><td>188.36 (+12.36%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.00 (n/a)</td><td>412.52 (n/a)</td><td>427.50 (n/a)</td><td>193.40 (n/a)</td><td>167.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(+26.75%)</b></td><td>0.03 <b>(+36.07%)</b></td><td>0.03 <b>(+51.64%)</b></td><td>0.02 <b>(+106.07%)</b></td><td>0.01 (+14.55%)</td><td>531.00 <b>(-51.47%)</b></td><td>356.04 <b>(-33.52%)</b></td><td>311.00 <b>(-34.07%)</b></td><td>200.60 <b>(-21.12%)</b></td><td>137.06 <b>(-57.79%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1094.20 (n/a)</td><td>535.58 (n/a)</td><td>471.70 (n/a)</td><td>254.30 (n/a)</td><td>324.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 <b>(-29.07%)</b></td><td>0.03 (-1.63%)</td><td>0.03 <b>(+87.35%)</b></td><td>0.01 (-8.25%)</td><td>0.01 <b>(-35.78%)</b></td><td>622.50 (+9.00%)</td><td>402.34 (-6.07%)</td><td>294.60 <b>(-46.61%)</b></td><td>229.90 <b>(+40.96%)</b></td><td>187.55 (-1.32%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>571.10 (n/a)</td><td>428.34 (n/a)</td><td>551.80 (n/a)</td><td>163.10 (n/a)</td><td>190.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 <b>(+43.96%)</b></td><td>0.02 (+9.62%)</td><td>0.02 (-3.17%)</td><td>0.02 (-5.17%)</td><td>0.01 <b>(+179.14%)</b></td><td>521.90 (+5.46%)</td><td>430.36 (-3.62%)</td><td>484.20 (+3.28%)</td><td>264.60 <b>(-30.55%)</b></td><td>110.97 <b>(+106.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>494.90 (n/a)</td><td>446.52 (n/a)</td><td>468.80 (n/a)</td><td>381.00 (n/a)</td><td>53.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+11.91%)</td><td>0.04 (+7.62%)</td><td>0.04 (+12.05%)</td><td>0.02 <b>(+24.32%)</b></td><td>0.02 (+9.45%)</td><td>660.50 (-19.56%)</td><td>423.34 (-8.59%)</td><td>410.10 (-10.75%)</td><td>250.90 (-10.65%)</td><td>172.40 <b>(-21.25%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>821.10 (n/a)</td><td>463.12 (n/a)</td><td>459.50 (n/a)</td><td>280.80 (n/a)</td><td>218.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (+11.49%)</td><td>0.06 (+10.64%)</td><td>0.05 (-19.30%)</td><td>0.05 <b>(+103.59%)</b></td><td>0.02 (-7.94%)</td><td>514.40 <b>(-50.88%)</b></td><td>420.66 (-19.05%)</td><td>486.50 <b>(+23.92%)</b></td><td>274.60 (-10.32%)</td><td>115.21 <b>(-61.71%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1047.20 (n/a)</td><td>519.64 (n/a)</td><td>392.60 (n/a)</td><td>306.20 (n/a)</td><td>300.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(-27.61%)</b></td><td>0.03 <b>(-24.32%)</b></td><td>0.03 (-8.05%)</td><td>0.03 (-3.17%)</td><td>0.01 <b>(-55.70%)</b></td><td>608.10 (+3.28%)</td><td>510.04 <b>(+21.87%)</b></td><td>525.70 (+8.77%)</td><td>353.70 <b>(+38.11%)</b></td><td>94.16 <b>(-36.27%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.80 (n/a)</td><td>418.50 (n/a)</td><td>483.30 (n/a)</td><td>256.10 (n/a)</td><td>147.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (-4.93%)</td><td>0.06 (-9.45%)</td><td>0.06 (-14.94%)</td><td>0.04 (-12.08%)</td><td>0.02 (-18.49%)</td><td>570.00 (+13.75%)</td><td>383.88 (+8.07%)</td><td>326.10 (+17.56%)</td><td>263.00 (+5.16%)</td><td>126.64 (-3.07%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>501.10 (n/a)</td><td>355.22 (n/a)</td><td>277.40 (n/a)</td><td>250.10 (n/a)</td><td>130.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (-1.73%)</td><td>0.04 (+0.37%)</td><td>0.04 (+5.40%)</td><td>0.03 (+1.05%)</td><td>0.01 (-7.57%)</td><td>605.70 (-1.03%)</td><td>460.74 (-1.34%)</td><td>457.80 (-5.14%)</td><td>303.80 (+1.74%)</td><td>120.61 (-7.10%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>612.00 (n/a)</td><td>466.98 (n/a)</td><td>482.60 (n/a)</td><td>298.60 (n/a)</td><td>129.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (+4.78%)</td><td>0.06 (+19.64%)</td><td>0.07 <b>(+57.83%)</b></td><td>0.03 <b>(-26.08%)</b></td><td>0.02 (+19.33%)</td><td>664.90 <b>(+35.28%)</b></td><td>368.88 (-11.63%)</td><td>302.20 <b>(-36.65%)</b></td><td>244.00 (-4.58%)</td><td>168.55 <b>(+67.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>491.50 (n/a)</td><td>417.44 (n/a)</td><td>477.00 (n/a)</td><td>255.70 (n/a)</td><td>100.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+2.40%)</td><td>0.04 (+4.85%)</td><td>0.04 <b>(+22.82%)</b></td><td>0.03 (+0.67%)</td><td>0.02 (-4.56%)</td><td>592.60 (-0.67%)</td><td>436.66 (-6.68%)</td><td>450.10 (-18.58%)</td><td>235.70 (-2.32%)</td><td>128.23 (-14.87%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>596.60 (n/a)</td><td>467.90 (n/a)</td><td>552.80 (n/a)</td><td>241.30 (n/a)</td><td>150.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 <b>(+20.80%)</b></td><td>0.05 (+12.55%)</td><td>0.04 (-6.48%)</td><td>0.03 <b>(+20.37%)</b></td><td>0.02 <b>(+46.93%)</b></td><td>535.20 (-16.92%)</td><td>411.86 (-7.94%)</td><td>466.90 (+6.94%)</td><td>238.50 (-17.22%)</td><td>132.41 (+3.59%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>644.20 (n/a)</td><td>447.36 (n/a)</td><td>436.60 (n/a)</td><td>288.10 (n/a)</td><td>127.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 <b>(-45.82%)</b></td><td>0.04 <b>(-25.50%)</b></td><td>0.04 <b>(-29.04%)</b></td><td>0.03 (+5.81%)</td><td>0.01 <b>(-68.65%)</b></td><td>554.30 (-5.49%)</td><td>431.30 (+12.75%)</td><td>451.90 <b>(+40.91%)</b></td><td>317.80 <b>(+84.55%)</b></td><td>92.14 <b>(-50.36%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>586.50 (n/a)</td><td>382.54 (n/a)</td><td>320.70 (n/a)</td><td>172.20 (n/a)</td><td>185.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (-0.38%)</td><td>0.05 (-2.04%)</td><td>0.05 (+17.92%)</td><td>0.03 <b>(-21.28%)</b></td><td>0.02 <b>(+25.79%)</b></td><td>599.30 <b>(+27.02%)</b></td><td>415.98 (+6.51%)</td><td>355.30 (-15.20%)</td><td>294.00 (+0.38%)</td><td>141.37 <b>(+59.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>471.80 (n/a)</td><td>390.56 (n/a)</td><td>419.00 (n/a)</td><td>292.90 (n/a)</td><td>88.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (-19.70%)</td><td>0.04 <b>(-21.68%)</b></td><td>0.03 <b>(-31.39%)</b></td><td>0.03 (+2.73%)</td><td>0.01 <b>(-28.93%)</b></td><td>575.70 (-2.65%)</td><td>491.18 <b>(+23.85%)</b></td><td>520.50 <b>(+45.76%)</b></td><td>313.40 <b>(+24.51%)</b></td><td>104.90 (-17.60%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.40 (n/a)</td><td>396.58 (n/a)</td><td>357.10 (n/a)</td><td>251.70 (n/a)</td><td>127.30 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (-11.52%)</td><td>0.07 (-14.87%)</td><td>0.07 (-1.55%)</td><td>0.05 (-1.50%)</td><td>0.02 <b>(-32.28%)</b></td><td>677.60 (+1.53%)</td><td>500.10 (+11.82%)</td><td>480.60 (+1.59%)</td><td>318.20 (+13.00%)</td><td>131.64 (-18.99%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>667.40 (n/a)</td><td>447.24 (n/a)</td><td>473.10 (n/a)</td><td>281.60 (n/a)</td><td>162.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (-9.25%)</td><td>0.07 <b>(-31.53%)</b></td><td>0.06 <b>(-46.96%)</b></td><td>0.04 <b>(-34.49%)</b></td><td>0.02 (-2.69%)</td><td>843.80 <b>(+52.67%)</b></td><td>555.32 <b>(+51.49%)</b></td><td>551.00 <b>(+88.57%)</b></td><td>312.80 (+10.18%)</td><td>196.79 <b>(+66.72%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>552.70 (n/a)</td><td>366.56 (n/a)</td><td>292.20 (n/a)</td><td>283.90 (n/a)</td><td>118.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (-6.25%)</td><td>0.08 <b>(-31.76%)</b></td><td>0.08 <b>(-29.47%)</b></td><td>0.02 <b>(-76.15%)</b></td><td>0.06 <b>(+64.77%)</b></td><td>2089.10 <b>(+319.33%)</b></td><td>858.88 <b>(+140.91%)</b></td><td>519.60 <b>(+41.77%)</b></td><td>262.20 (+6.67%)</td><td>763.52 <b>(+645.63%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>498.20 (n/a)</td><td>356.52 (n/a)</td><td>366.50 (n/a)</td><td>245.80 (n/a)</td><td>102.40 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (+4.63%)</td><td>0.10 <b>(+34.05%)</b></td><td>0.12 <b>(+73.83%)</b></td><td>0.06 (+11.28%)</td><td>0.03 (+1.39%)</td><td>552.40 (-10.14%)</td><td>346.82 <b>(-26.09%)</b></td><td>283.80 <b>(-42.47%)</b></td><td>256.40 (-4.40%)</td><td>123.64 (-12.70%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>614.70 (n/a)</td><td>469.22 (n/a)</td><td>493.30 (n/a)</td><td>268.20 (n/a)</td><td>141.62 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (+5.88%)</td><td>0.11 (-6.52%)</td><td>0.12 (-2.89%)</td><td>0.06 (+2.24%)</td><td>0.05 <b>(+25.97%)</b></td><td>679.50 (-2.20%)</td><td>422.84 (+11.40%)</td><td>332.10 (+2.98%)</td><td>256.40 (-5.56%)</td><td>194.16 (+9.18%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>694.80 (n/a)</td><td>379.58 (n/a)</td><td>322.50 (n/a)</td><td>271.50 (n/a)</td><td>177.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (-7.79%)</td><td>0.08 (+5.88%)</td><td>0.07 (+4.14%)</td><td>0.07 (+18.31%)</td><td>0.03 <b>(-24.63%)</b></td><td>503.60 (-15.47%)</td><td>420.00 (-10.57%)</td><td>453.50 (-3.98%)</td><td>249.60 (+8.43%)</td><td>100.94 <b>(-31.02%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>595.80 (n/a)</td><td>469.64 (n/a)</td><td>472.30 (n/a)</td><td>230.20 (n/a)</td><td>146.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 <b>(-35.23%)</b></td><td>0.10 (+7.10%)</td><td>0.11 <b>(+41.14%)</b></td><td>0.06 <b>(+301.27%)</b></td><td>0.03 <b>(-63.11%)</b></td><td>596.70 <b>(-75.08%)</b></td><td>379.62 <b>(-51.68%)</b></td><td>344.80 <b>(-29.14%)</b></td><td>289.90 <b>(+54.37%)</b></td><td>125.07 <b>(-86.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>2394.40 (n/a)</td><td>785.70 (n/a)</td><td>486.60 (n/a)</td><td>187.80 (n/a)</td><td>913.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (-12.50%)</td><td>0.09 (+1.78%)</td><td>0.07 (+0.88%)</td><td>0.06 (-1.46%)</td><td>0.03 (-11.15%)</td><td>514.80 (+1.48%)</td><td>393.50 (-2.99%)</td><td>452.30 (-0.88%)</td><td>272.30 (+14.32%)</td><td>112.95 (-5.69%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>507.30 (n/a)</td><td>405.62 (n/a)</td><td>456.30 (n/a)</td><td>238.20 (n/a)</td><td>119.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 <b>(-45.80%)</b></td><td>0.07 <b>(-41.03%)</b></td><td>0.07 <b>(-42.48%)</b></td><td>0.05 <b>(-21.28%)</b></td><td>0.01 <b>(-58.97%)</b></td><td>695.80 <b>(+27.04%)</b></td><td>571.44 <b>(+62.82%)</b></td><td>547.10 <b>(+73.85%)</b></td><td>464.90 <b>(+84.48%)</b></td><td>103.20 (-9.39%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>547.70 (n/a)</td><td>350.96 (n/a)</td><td>314.70 (n/a)</td><td>252.00 (n/a)</td><td>113.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (-12.90%)</td><td>0.07 <b>(-24.69%)</b></td><td>0.06 <b>(-36.73%)</b></td><td>0.05 <b>(-38.45%)</b></td><td>0.02 <b>(+96.88%)</b></td><td>649.00 <b>(+62.49%)</b></td><td>507.12 <b>(+39.93%)</b></td><td>568.20 <b>(+58.05%)</b></td><td>350.70 (+14.80%)</td><td>132.98 <b>(+260.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>399.40 (n/a)</td><td>362.40 (n/a)</td><td>359.50 (n/a)</td><td>305.50 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+4.63%)</td><td>0.05 (-10.02%)</td><td>0.04 (-10.20%)</td><td>0.03 (-4.60%)</td><td>0.02 (-1.24%)</td><td>615.30 (+4.80%)</td><td>475.58 (+10.97%)</td><td>516.50 (+11.34%)</td><td>273.90 (-4.40%)</td><td>132.75 (+0.73%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>587.10 (n/a)</td><td>428.56 (n/a)</td><td>463.90 (n/a)</td><td>286.50 (n/a)</td><td>131.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (-3.19%)</td><td>0.05 (-18.68%)</td><td>0.05 <b>(-37.32%)</b></td><td>0.03 (-0.82%)</td><td>0.02 (-0.89%)</td><td>623.50 (+0.82%)</td><td>430.26 <b>(+22.21%)</b></td><td>448.40 <b>(+59.57%)</b></td><td>278.00 (+3.31%)</td><td>143.18 (-4.40%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.40 (n/a)</td><td>352.08 (n/a)</td><td>281.00 (n/a)</td><td>269.10 (n/a)</td><td>149.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (+14.65%)</td><td>0.07 <b>(+28.04%)</b></td><td>0.07 <b>(+44.09%)</b></td><td>0.05 <b>(+31.03%)</b></td><td>0.01 (-11.62%)</td><td>426.50 <b>(-23.68%)</b></td><td>304.24 <b>(-23.88%)</b></td><td>279.70 <b>(-30.61%)</b></td><td>250.50 (-12.78%)</td><td>70.06 <b>(-36.65%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>558.80 (n/a)</td><td>399.66 (n/a)</td><td>403.10 (n/a)</td><td>287.20 (n/a)</td><td>110.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 <b>(+60.62%)</b></td><td>0.06 <b>(+54.83%)</b></td><td>0.06 <b>(+52.75%)</b></td><td>0.04 <b>(+56.11%)</b></td><td>0.03 <b>(+70.94%)</b></td><td>542.70 <b>(-35.93%)</b></td><td>356.50 <b>(-34.27%)</b></td><td>324.10 <b>(-34.54%)</b></td><td>198.20 <b>(-37.73%)</b></td><td>136.34 <b>(-31.75%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>847.10 (n/a)</td><td>542.38 (n/a)</td><td>495.10 (n/a)</td><td>318.30 (n/a)</td><td>199.75 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 <b>(+40.25%)</b></td><td>0.04 (-1.47%)</td><td>0.04 (+1.92%)</td><td>0.01 <b>(-72.82%)</b></td><td>0.02 <b>(+265.62%)</b></td><td>2088.10 <b>(+267.95%)</b></td><td>778.20 <b>(+54.10%)</b></td><td>511.20 (-1.88%)</td><td>287.60 <b>(-28.69%)</b></td><td>738.50 <b>(+1014.22%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>567.50 (n/a)</td><td>505.00 (n/a)</td><td>521.00 (n/a)</td><td>403.30 (n/a)</td><td>66.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (-18.79%)</td><td>0.05 (-17.03%)</td><td>0.03 <b>(-52.00%)</b></td><td>0.03 <b>(+216.07%)</b></td><td>0.02 <b>(-34.14%)</b></td><td>642.40 <b>(-68.36%)</b></td><td>489.70 <b>(-25.35%)</b></td><td>607.10 <b>(+108.34%)</b></td><td>293.60 <b>(+23.15%)</b></td><td>177.77 <b>(-76.98%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2030.50 (n/a)</td><td>655.96 (n/a)</td><td>291.40 (n/a)</td><td>238.40 (n/a)</td><td>772.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (-7.83%)</td><td>0.05 <b>(-34.78%)</b></td><td>0.05 <b>(-42.47%)</b></td><td>0.04 <b>(-25.52%)</b></td><td>0.02 (+13.66%)</td><td>637.80 <b>(+34.27%)</b></td><td>498.38 <b>(+59.35%)</b></td><td>501.60 <b>(+73.86%)</b></td><td>271.30 (+8.52%)</td><td>144.62 <b>(+55.89%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>475.00 (n/a)</td><td>312.76 (n/a)</td><td>288.50 (n/a)</td><td>250.00 (n/a)</td><td>92.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (-1.76%)</td><td>0.08 (-2.01%)</td><td>0.09 (+8.69%)</td><td>0.05 <b>(-20.18%)</b></td><td>0.02 <b>(+31.17%)</b></td><td>468.90 <b>(+25.27%)</b></td><td>314.46 (+4.85%)</td><td>282.30 (-8.02%)</td><td>253.40 (+1.81%)</td><td>87.84 <b>(+76.67%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>374.30 (n/a)</td><td>299.92 (n/a)</td><td>306.90 (n/a)</td><td>248.90 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (+18.77%)</td><td>0.08 <b>(+25.01%)</b></td><td>0.10 <b>(+68.24%)</b></td><td>0.04 (+4.61%)</td><td>0.03 <b>(+41.06%)</b></td><td>573.10 (-4.42%)</td><td>347.56 (-15.95%)</td><td>250.20 <b>(-40.56%)</b></td><td>230.70 (-15.80%)</td><td>152.67 (+14.16%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>599.60 (n/a)</td><td>413.54 (n/a)</td><td>420.90 (n/a)</td><td>274.00 (n/a)</td><td>133.74 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (+14.27%)</td><td>0.07 (+7.63%)</td><td>0.07 <b>(+23.19%)</b></td><td>0.03 (-19.96%)</td><td>0.02 <b>(+23.36%)</b></td><td>756.50 <b>(+24.94%)</b></td><td>405.84 (-1.22%)</td><td>339.50 (-18.84%)</td><td>244.30 (-12.50%)</td><td>200.81 <b>(+52.90%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>605.50 (n/a)</td><td>410.86 (n/a)</td><td>418.30 (n/a)</td><td>279.20 (n/a)</td><td>131.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 <b>(-34.38%)</b></td><td>0.05 <b>(-23.76%)</b></td><td>0.05 (-8.41%)</td><td>0.04 (-8.34%)</td><td>0.01 <b>(-59.17%)</b></td><td>599.80 (+9.09%)</td><td>494.32 <b>(+20.94%)</b></td><td>525.70 (+9.18%)</td><td>364.00 <b>(+52.43%)</b></td><td>95.74 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>549.80 (n/a)</td><td>408.74 (n/a)</td><td>481.50 (n/a)</td><td>238.80 (n/a)</td><td>140.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 <b>(-26.92%)</b></td><td>0.05 (-13.92%)</td><td>0.05 (-13.48%)</td><td>0.04 (+13.55%)</td><td>0.01 <b>(-64.39%)</b></td><td>593.10 (-11.94%)</td><td>487.20 (+6.40%)</td><td>483.30 (+15.57%)</td><td>397.80 <b>(+36.84%)</b></td><td>71.53 <b>(-56.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>673.50 (n/a)</td><td>457.90 (n/a)</td><td>418.20 (n/a)</td><td>290.70 (n/a)</td><td>166.09 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (-4.34%)</td><td>0.04 <b>(-33.21%)</b></td><td>0.04 <b>(-44.35%)</b></td><td>0.03 <b>(-24.15%)</b></td><td>0.02 <b>(+25.94%)</b></td><td>593.10 <b>(+31.86%)</b></td><td>468.60 <b>(+57.87%)</b></td><td>489.90 <b>(+79.71%)</b></td><td>241.10 (+4.55%)</td><td>142.91 <b>(+62.44%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>449.80 (n/a)</td><td>296.82 (n/a)</td><td>272.60 (n/a)</td><td>230.60 (n/a)</td><td>87.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (-0.35%)</td><td>0.06 (+7.33%)</td><td>0.06 (+14.14%)</td><td>0.04 (-0.08%)</td><td>0.01 (-9.14%)</td><td>499.30 (+0.08%)</td><td>344.52 (-7.90%)</td><td>304.30 (-12.38%)</td><td>254.60 (+0.35%)</td><td>96.25 (-9.37%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>498.90 (n/a)</td><td>374.06 (n/a)</td><td>347.30 (n/a)</td><td>253.70 (n/a)</td><td>106.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+2.11%)</td><td>0.06 (+16.53%)</td><td>0.07 <b>(+48.59%)</b></td><td>0.04 (-1.42%)</td><td>0.01 (-13.83%)</td><td>509.90 (+1.43%)</td><td>324.02 (-15.83%)</td><td>269.50 <b>(-32.69%)</b></td><td>256.00 (-2.07%)</td><td>106.81 (-10.92%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>502.70 (n/a)</td><td>384.94 (n/a)</td><td>400.40 (n/a)</td><td>261.40 (n/a)</td><td>119.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (-7.11%)</td><td>0.06 <b>(+24.46%)</b></td><td>0.07 <b>(+46.30%)</b></td><td>0.04 <b>(+426.17%)</b></td><td>0.02 <b>(-48.55%)</b></td><td>483.60 <b>(-80.99%)</b></td><td>308.14 <b>(-59.62%)</b></td><td>259.50 <b>(-31.66%)</b></td><td>244.70 (+7.66%)</td><td>100.01 <b>(-89.99%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2544.30 (n/a)</td><td>763.10 (n/a)</td><td>379.70 (n/a)</td><td>227.30 (n/a)</td><td>999.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 <b>(+24.60%)</b></td><td>0.04 (-12.25%)</td><td>0.03 <b>(-25.39%)</b></td><td>0.03 (-5.94%)</td><td>0.02 <b>(+34.71%)</b></td><td>654.40 (+6.32%)</td><td>508.48 (+19.98%)</td><td>566.20 <b>(+34.04%)</b></td><td>213.80 (-19.74%)</td><td>171.00 (+10.58%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.50 (n/a)</td><td>423.82 (n/a)</td><td>422.40 (n/a)</td><td>266.40 (n/a)</td><td>154.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (-7.65%)</td><td>0.04 (-12.30%)</td><td>0.04 (-7.57%)</td><td>0.03 (+13.71%)</td><td>0.02 <b>(-24.29%)</b></td><td>535.50 (-12.07%)</td><td>446.74 (+8.47%)</td><td>497.00 (+8.18%)</td><td>262.80 (+8.28%)</td><td>113.05 <b>(-25.53%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>609.00 (n/a)</td><td>411.86 (n/a)</td><td>459.40 (n/a)</td><td>242.70 (n/a)</td><td>151.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.39 (+3.99%)</td><td>0.26 (-9.36%)</td><td>0.25 <b>(-23.15%)</b></td><td>0.14 <b>(-29.26%)</b></td><td>0.10 <b>(+27.12%)</b></td><td>683.70 <b>(+41.35%)</b></td><td>421.24 (+17.18%)</td><td>392.50 <b>(+30.14%)</b></td><td>251.50 (-3.82%)</td><td>170.63 <b>(+66.71%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>483.70 (n/a)</td><td>359.48 (n/a)</td><td>301.60 (n/a)</td><td>261.50 (n/a)</td><td>102.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.30 <b>(-23.07%)</b></td><td>0.24 (-1.29%)</td><td>0.26 <b>(+26.96%)</b></td><td>0.17 (+8.65%)</td><td>0.06 <b>(-41.69%)</b></td><td>591.50 (-7.97%)</td><td>431.62 (-5.40%)</td><td>374.20 <b>(-21.24%)</b></td><td>331.90 <b>(+30.00%)</b></td><td>113.43 <b>(-30.70%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.38 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>642.70 (n/a)</td><td>456.26 (n/a)</td><td>475.10 (n/a)</td><td>255.30 (n/a)</td><td>163.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.30 (-19.11%)</td><td>0.24 (+1.27%)</td><td>0.26 (+17.33%)</td><td>0.14 (-7.54%)</td><td>0.06 <b>(-22.36%)</b></td><td>690.90 (+8.16%)</td><td>441.88 (-2.42%)</td><td>373.10 (-14.78%)</td><td>331.90 <b>(+23.61%)</b></td><td>148.25 (+7.34%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>638.80 (n/a)</td><td>452.82 (n/a)</td><td>437.80 (n/a)</td><td>268.50 (n/a)</td><td>138.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.26 (+5.98%)</td><td>0.23 <b>(+39.62%)</b></td><td>0.24 <b>(+66.68%)</b></td><td>0.15 (+16.39%)</td><td>0.04 (-7.28%)</td><td>489.20 (-14.09%)</td><td>339.04 <b>(-29.33%)</b></td><td>304.60 <b>(-39.99%)</b></td><td>288.60 (-5.66%)</td><td>84.46 <b>(-21.19%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>569.40 (n/a)</td><td>479.72 (n/a)</td><td>507.60 (n/a)</td><td>305.90 (n/a)</td><td>107.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.27 (+7.94%)</td><td>0.19 (+2.61%)</td><td>0.17 (-2.01%)</td><td>0.16 <b>(+29.06%)</b></td><td>0.05 (-10.21%)</td><td>474.20 <b>(-22.52%)</b></td><td>395.84 (-5.05%)</td><td>425.10 (+2.06%)</td><td>275.80 (-7.33%)</td><td>80.54 <b>(-35.31%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>612.00 (n/a)</td><td>416.90 (n/a)</td><td>416.50 (n/a)</td><td>297.60 (n/a)</td><td>124.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.28 (-6.67%)</td><td>0.17 <b>(-25.94%)</b></td><td>0.15 <b>(-43.65%)</b></td><td>0.14 (-18.33%)</td><td>0.06 (-2.73%)</td><td>543.80 <b>(+22.45%)</b></td><td>454.12 <b>(+36.21%)</b></td><td>503.20 <b>(+77.43%)</b></td><td>264.00 (+7.14%)</td><td>112.06 (+18.96%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>444.10 (n/a)</td><td>333.40 (n/a)</td><td>283.60 (n/a)</td><td>246.40 (n/a)</td><td>94.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (+5.56%)</td><td>0.11 (+14.92%)</td><td>0.12 <b>(+51.54%)</b></td><td>0.05 (-12.32%)</td><td>0.04 (-6.02%)</td><td>675.40 (+14.07%)</td><td>374.14 (-12.69%)</td><td>302.60 <b>(-34.02%)</b></td><td>250.40 (-5.26%)</td><td>173.27 (+11.75%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>592.10 (n/a)</td><td>428.50 (n/a)</td><td>458.60 (n/a)</td><td>264.30 (n/a)</td><td>155.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (+0.85%)</td><td>0.08 <b>(-31.03%)</b></td><td>0.07 <b>(-37.80%)</b></td><td>0.02 <b>(-71.08%)</b></td><td>0.04 <b>(+45.94%)</b></td><td>1945.60 <b>(+245.76%)</b></td><td>749.64 <b>(+106.01%)</b></td><td>498.60 <b>(+60.79%)</b></td><td>274.20 (-0.83%)</td><td>679.34 <b>(+465.55%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>562.70 (n/a)</td><td>363.88 (n/a)</td><td>310.10 (n/a)</td><td>276.50 (n/a)</td><td>120.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (+1.90%)</td><td>0.10 (-18.11%)</td><td>0.08 <b>(-40.96%)</b></td><td>0.06 (-12.37%)</td><td>0.04 (-1.98%)</td><td>604.20 (+14.11%)</td><td>409.24 <b>(+22.78%)</b></td><td>438.20 <b>(+69.39%)</b></td><td>236.50 (-1.87%)</td><td>140.01 (+11.03%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>529.50 (n/a)</td><td>333.32 (n/a)</td><td>258.70 (n/a)</td><td>241.00 (n/a)</td><td>126.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 <b>(+36.31%)</b></td><td>0.12 <b>(+64.01%)</b></td><td>0.11 <b>(+83.05%)</b></td><td>0.07 <b>(+43.77%)</b></td><td>0.04 <b>(+25.81%)</b></td><td>556.50 <b>(-30.45%)</b></td><td>348.42 <b>(-40.55%)</b></td><td>326.80 <b>(-45.37%)</b></td><td>234.80 <b>(-26.62%)</b></td><td>128.66 <b>(-37.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>800.20 (n/a)</td><td>586.10 (n/a)</td><td>598.20 (n/a)</td><td>320.00 (n/a)</td><td>207.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (-3.84%)</td><td>0.09 (+2.47%)</td><td>0.08 (+0.95%)</td><td>0.06 (-15.75%)</td><td>0.03 <b>(+33.15%)</b></td><td>647.30 (+18.68%)</td><td>470.32 (+3.31%)</td><td>467.10 (-0.93%)</td><td>303.60 (+4.01%)</td><td>167.50 <b>(+61.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>545.40 (n/a)</td><td>455.24 (n/a)</td><td>471.50 (n/a)</td><td>291.90 (n/a)</td><td>103.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (-15.93%)</td><td>0.07 <b>(-35.93%)</b></td><td>0.07 <b>(-43.95%)</b></td><td>0.03 <b>(-55.82%)</b></td><td>0.03 <b>(+23.63%)</b></td><td>1057.20 <b>(+126.33%)</b></td><td>583.02 <b>(+75.86%)</b></td><td>537.70 <b>(+78.40%)</b></td><td>301.00 (+18.93%)</td><td>285.00 <b>(+237.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>467.10 (n/a)</td><td>331.52 (n/a)</td><td>301.40 (n/a)</td><td>253.10 (n/a)</td><td>84.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (-1.58%)</td><td>0.11 (-3.65%)</td><td>0.13 (+3.37%)</td><td>0.02 <b>(-63.86%)</b></td><td>0.06 <b>(+41.57%)</b></td><td>2019.70 <b>(+176.67%)</b></td><td>663.10 <b>(+62.19%)</b></td><td>320.20 (-3.23%)</td><td>255.90 (+1.59%)</td><td>762.32 <b>(+300.64%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>730.00 (n/a)</td><td>408.84 (n/a)</td><td>330.90 (n/a)</td><td>251.90 (n/a)</td><td>190.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (+9.62%)</td><td>0.12 <b>(+49.82%)</b></td><td>0.14 <b>(+69.61%)</b></td><td>0.08 <b>(+121.27%)</b></td><td>0.03 <b>(-21.31%)</b></td><td>501.90 <b>(-54.81%)</b></td><td>349.46 <b>(-42.53%)</b></td><td>294.10 <b>(-41.03%)</b></td><td>274.10 (-8.79%)</td><td>100.45 <b>(-69.01%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1110.60 (n/a)</td><td>608.04 (n/a)</td><td>498.70 (n/a)</td><td>300.50 (n/a)</td><td>324.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.18 (+12.28%)</td><td>0.10 (-11.83%)</td><td>0.08 (-19.29%)</td><td>0.07 (-0.39%)</td><td>0.05 <b>(+23.16%)</b></td><td>568.30 (+0.39%)</td><td>480.56 (+16.77%)</td><td>541.00 <b>(+23.91%)</b></td><td>230.50 (-10.94%)</td><td>140.80 (+7.83%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>566.10 (n/a)</td><td>411.54 (n/a)</td><td>436.60 (n/a)</td><td>258.80 (n/a)</td><td>130.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (-19.95%)</td><td>0.10 (+3.62%)</td><td>0.09 (+11.39%)</td><td>0.08 <b>(+124.72%)</b></td><td>0.02 <b>(-60.73%)</b></td><td>496.10 <b>(-55.50%)</b></td><td>430.52 <b>(-23.16%)</b></td><td>471.00 (-10.23%)</td><td>322.50 <b>(+24.90%)</b></td><td>75.28 <b>(-77.77%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1114.90 (n/a)</td><td>560.30 (n/a)</td><td>524.70 (n/a)</td><td>258.20 (n/a)</td><td>338.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (-11.36%)</td><td>0.09 <b>(-20.08%)</b></td><td>0.08 <b>(-27.89%)</b></td><td>0.07 (-12.50%)</td><td>0.03 (-6.30%)</td><td>579.20 (+14.29%)</td><td>464.82 <b>(+26.02%)</b></td><td>505.40 <b>(+38.66%)</b></td><td>270.30 (+12.81%)</td><td>122.02 (+17.55%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>506.80 (n/a)</td><td>368.84 (n/a)</td><td>364.50 (n/a)</td><td>239.60 (n/a)</td><td>103.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (-9.03%)</td><td>0.12 (+3.07%)</td><td>0.13 (+14.71%)</td><td>0.09 (+12.85%)</td><td>0.03 (-18.23%)</td><td>440.00 (-11.38%)</td><td>347.82 (-5.12%)</td><td>312.40 (-12.83%)</td><td>272.80 (+9.91%)</td><td>85.50 (-19.04%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>496.50 (n/a)</td><td>366.58 (n/a)</td><td>358.40 (n/a)</td><td>248.20 (n/a)</td><td>105.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (-5.51%)</td><td>0.08 <b>(-34.21%)</b></td><td>0.10 (-14.67%)</td><td>0.02 <b>(-75.14%)</b></td><td>0.06 <b>(+92.13%)</b></td><td>2021.40 <b>(+302.27%)</b></td><td>980.84 <b>(+209.67%)</b></td><td>334.40 (+17.21%)</td><td>262.20 (+5.81%)</td><td>933.18 <b>(+778.85%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>502.50 (n/a)</td><td>316.74 (n/a)</td><td>285.30 (n/a)</td><td>247.80 (n/a)</td><td>106.18 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (-3.34%)</td><td>0.09 (+1.90%)</td><td>0.07 (-10.10%)</td><td>0.05 <b>(+167.42%)</b></td><td>0.04 <b>(-28.06%)</b></td><td>737.50 <b>(-62.60%)</b></td><td>451.92 <b>(-34.40%)</b></td><td>473.30 (+11.23%)</td><td>258.50 (+3.48%)</td><td>188.79 <b>(-74.01%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1972.10 (n/a)</td><td>688.94 (n/a)</td><td>425.50 (n/a)</td><td>249.80 (n/a)</td><td>726.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.17 <b>(+41.03%)</b></td><td>0.11 <b>(+22.93%)</b></td><td>0.11 <b>(+51.21%)</b></td><td>0.07 (-2.11%)</td><td>0.05 <b>(+72.32%)</b></td><td>531.20 (+2.15%)</td><td>359.38 (-12.11%)</td><td>305.60 <b>(-33.88%)</b></td><td>202.60 <b>(-29.09%)</b></td><td>149.18 <b>(+37.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>520.00 (n/a)</td><td>408.90 (n/a)</td><td>462.20 (n/a)</td><td>285.70 (n/a)</td><td>108.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (+0.68%)</td><td>0.09 (+16.09%)</td><td>0.07 (-7.57%)</td><td>0.06 (+9.97%)</td><td>0.04 (+19.84%)</td><td>619.80 (-9.08%)</td><td>443.34 (-11.39%)</td><td>525.40 (+8.20%)</td><td>257.30 (-0.69%)</td><td>172.68 (+0.99%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>681.70 (n/a)</td><td>500.32 (n/a)</td><td>485.60 (n/a)</td><td>259.10 (n/a)</td><td>170.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (-8.68%)</td><td>0.08 (-14.61%)</td><td>0.07 (-15.16%)</td><td>0.06 (-4.53%)</td><td>0.03 (-12.70%)</td><td>554.40 (+4.74%)</td><td>456.72 (+16.05%)</td><td>495.30 (+17.87%)</td><td>277.60 (+9.51%)</td><td>111.02 (-0.86%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>529.30 (n/a)</td><td>393.56 (n/a)</td><td>420.20 (n/a)</td><td>253.50 (n/a)</td><td>111.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (+7.36%)</td><td>0.08 <b>(-24.05%)</b></td><td>0.07 <b>(-37.06%)</b></td><td>0.03 <b>(-57.53%)</b></td><td>0.04 <b>(+43.12%)</b></td><td>1386.30 <b>(+135.44%)</b></td><td>603.42 <b>(+66.44%)</b></td><td>466.20 <b>(+58.90%)</b></td><td>248.90 (-6.85%)</td><td>451.00 <b>(+236.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>588.80 (n/a)</td><td>362.54 (n/a)</td><td>293.40 (n/a)</td><td>267.20 (n/a)</td><td>133.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.39 (-9.77%)</td><td>0.30 (-3.84%)</td><td>0.26 (-3.46%)</td><td>0.23 (+1.46%)</td><td>0.07 <b>(-28.83%)</b></td><td>575.30 (-1.44%)</td><td>460.72 (+0.59%)</td><td>497.50 (+3.60%)</td><td>333.00 (+10.82%)</td><td>97.97 <b>(-25.17%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>583.70 (n/a)</td><td>458.04 (n/a)</td><td>480.20 (n/a)</td><td>300.50 (n/a)</td><td>130.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.45 (+8.67%)</td><td>0.26 <b>(-21.32%)</b></td><td>0.23 <b>(-39.95%)</b></td><td>0.14 <b>(-29.68%)</b></td><td>0.12 (+16.57%)</td><td>905.10 <b>(+42.22%)</b></td><td>575.38 <b>(+33.95%)</b></td><td>558.60 <b>(+66.55%)</b></td><td>288.70 (-8.00%)</td><td>226.11 <b>(+51.69%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.39 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>636.40 (n/a)</td><td>429.54 (n/a)</td><td>335.40 (n/a)</td><td>313.80 (n/a)</td><td>149.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.46 (+10.58%)</td><td>0.27 (-4.03%)</td><td>0.22 (+4.57%)</td><td>0.17 (-7.07%)</td><td>0.11 (+1.55%)</td><td>777.80 (+7.62%)</td><td>554.20 (+3.30%)</td><td>583.20 (-4.38%)</td><td>286.30 (-9.57%)</td><td>182.09 (-5.39%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>722.70 (n/a)</td><td>536.48 (n/a)</td><td>609.90 (n/a)</td><td>316.60 (n/a)</td><td>192.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.29%)</b></td><td>20384.69 (-1.06%)</td><td>15567.08 (-1.53%)</td><td>14979.64 (-16.97%)</td><td>8770.42 <b>(+34.21%)</b></td><td>4507.54 (-19.46%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20603.53 (n/a)</td><td>15809.03 (n/a)</td><td>18042.25 (n/a)</td><td>6534.82 (n/a)</td><td>5596.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.00 <b>(+30.00%)</b></td><td>0.00 (+3.03%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 <b>(+71.86%)</b></td><td>21935.83 <b>(+39.00%)</b></td><td>14619.84 (+13.41%)</td><td>14276.29 (+4.21%)</td><td>6208.41 <b>(-27.82%)</b></td><td>5653.20 <b>(+95.45%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>15780.96 (n/a)</td><td>12890.78 (n/a)</td><td>13699.66 (n/a)</td><td>8600.74 (n/a)</td><td>2892.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 <b>(+22.22%)</b></td><td>0.09 (+3.47%)</td><td>0.07 (-8.82%)</td><td>0.07 (-7.52%)</td><td>0.04 <b>(+66.94%)</b></td><td>31031.62 (+8.13%)</td><td>25893.77 (+1.95%)</td><td>29819.45 (+9.67%)</td><td>13917.06 (-18.16%)</td><td>7181.21 <b>(+49.15%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>28699.45 (n/a)</td><td>25398.59 (n/a)</td><td>27191.22 (n/a)</td><td>17004.26 (n/a)</td><td>4814.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.93 (+15.26%)</td><td>2.64 <b>(+80.05%)</b></td><td>2.81 <b>(+64.38%)</b></td><td>2.03 <b>(+545.29%)</b></td><td>0.38 <b>(-55.99%)</b></td><td>516.60 <b>(-84.50%)</b></td><td>404.22 <b>(-66.49%)</b></td><td>372.70 <b>(-39.17%)</b></td><td>357.80 (-13.24%)</td><td>66.54 <b>(-94.53%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.54 (n/a)</td><td>1.47 (n/a)</td><td>1.71 (n/a)</td><td>0.31 (n/a)</td><td>0.86 (n/a)</td><td>3333.70 (n/a)</td><td>1206.34 (n/a)</td><td>612.70 (n/a)</td><td>412.40 (n/a)</td><td>1216.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.71 <b>(+22.84%)</b></td><td>2.72 (-11.00%)</td><td>2.77 (-8.99%)</td><td>1.39 <b>(-41.10%)</b></td><td>1.32 <b>(+129.27%)</b></td><td>753.10 <b>(+69.81%)</b></td><td>464.88 <b>(+31.67%)</b></td><td>379.10 (+9.88%)</td><td>222.50 (-18.59%)</td><td>217.87 <b>(+227.47%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.84 (n/a)</td><td>3.06 (n/a)</td><td>3.04 (n/a)</td><td>2.36 (n/a)</td><td>0.57 (n/a)</td><td>443.50 (n/a)</td><td>353.06 (n/a)</td><td>345.00 (n/a)</td><td>273.30 (n/a)</td><td>66.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.61 (-2.86%)</td><td>2.05 (+8.63%)</td><td>2.10 (+6.52%)</td><td>1.42 <b>(+154.59%)</b></td><td>0.54 <b>(-37.63%)</b></td><td>740.40 <b>(-60.72%)</b></td><td>543.32 <b>(-29.60%)</b></td><td>498.70 (-6.14%)</td><td>401.20 (+2.95%)</td><td>151.22 <b>(-76.04%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.69 (n/a)</td><td>1.89 (n/a)</td><td>1.97 (n/a)</td><td>0.56 (n/a)</td><td>0.87 (n/a)</td><td>1885.10 (n/a)</td><td>771.78 (n/a)</td><td>531.30 (n/a)</td><td>389.70 (n/a)</td><td>631.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.45 <b>(-24.49%)</b></td><td>1.91 (-14.36%)</td><td>2.12 (-3.85%)</td><td>1.28 <b>(+22.52%)</b></td><td>0.50 <b>(-40.61%)</b></td><td>816.60 (-18.38%)</td><td>585.10 (+6.85%)</td><td>493.80 (+4.00%)</td><td>428.80 <b>(+32.43%)</b></td><td>168.15 <b>(-37.36%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.24 (n/a)</td><td>2.23 (n/a)</td><td>2.21 (n/a)</td><td>1.05 (n/a)</td><td>0.84 (n/a)</td><td>1000.50 (n/a)</td><td>547.58 (n/a)</td><td>474.80 (n/a)</td><td>323.80 (n/a)</td><td>268.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.13 (+14.97%)</td><td>2.69 (+5.99%)</td><td>3.65 (+14.62%)</td><td>0.57 (-6.40%)</td><td>1.70 <b>(+37.01%)</b></td><td>3651.90 (+6.84%)</td><td>1430.06 (+12.41%)</td><td>574.30 (-12.76%)</td><td>508.20 (-13.02%)</td><td>1372.97 (+12.98%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.59 (n/a)</td><td>2.53 (n/a)</td><td>3.19 (n/a)</td><td>0.61 (n/a)</td><td>1.24 (n/a)</td><td>3418.10 (n/a)</td><td>1272.16 (n/a)</td><td>658.30 (n/a)</td><td>584.30 (n/a)</td><td>1215.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.21 <b>(+33.47%)</b></td><td>2.95 (+6.91%)</td><td>2.45 <b>(-20.86%)</b></td><td>0.63 (-4.83%)</td><td>1.84 <b>(+49.33%)</b></td><td>3351.50 (+5.07%)</td><td>1218.74 (+5.53%)</td><td>855.10 <b>(+26.36%)</b></td><td>402.20 <b>(-25.07%)</b></td><td>1218.37 (+6.93%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.91 (n/a)</td><td>2.76 (n/a)</td><td>3.10 (n/a)</td><td>0.66 (n/a)</td><td>1.23 (n/a)</td><td>3189.80 (n/a)</td><td>1154.88 (n/a)</td><td>676.70 (n/a)</td><td>536.80 (n/a)</td><td>1139.42 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.74 (-13.65%)</td><td>3.09 <b>(-28.50%)</b></td><td>3.70 (-12.02%)</td><td>0.99 <b>(-57.34%)</b></td><td>2.06 (+5.88%)</td><td>2109.50 <b>(+134.44%)</b></td><td>1129.92 <b>(+94.87%)</b></td><td>566.60 (+13.66%)</td><td>365.40 (+15.82%)</td><td>887.05 <b>(+227.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.65 (n/a)</td><td>4.33 (n/a)</td><td>4.21 (n/a)</td><td>2.33 (n/a)</td><td>1.95 (n/a)</td><td>899.80 (n/a)</td><td>579.84 (n/a)</td><td>498.50 (n/a)</td><td>315.50 (n/a)</td><td>270.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.49 (-2.23%)</td><td>4.62 (+15.40%)</td><td>5.19 (+19.72%)</td><td>1.74 <b>(+195.08%)</b></td><td>1.78 (-18.25%)</td><td>1208.60 <b>(-66.11%)</b></td><td>562.64 <b>(-47.59%)</b></td><td>403.80 (-16.48%)</td><td>323.30 (+2.28%)</td><td>365.62 <b>(-73.81%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.63 (n/a)</td><td>4.00 (n/a)</td><td>4.34 (n/a)</td><td>0.59 (n/a)</td><td>2.18 (n/a)</td><td>3566.40 (n/a)</td><td>1073.48 (n/a)</td><td>483.50 (n/a)</td><td>316.10 (n/a)</td><td>1396.09 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.92 <b>(-48.75%)</b></td><td>3.41 <b>(-21.36%)</b></td><td>3.52 (-19.24%)</td><td>2.92 <b>(+59.15%)</b></td><td>0.41 <b>(-81.02%)</b></td><td>717.10 <b>(-37.17%)</b></td><td>621.66 (+3.76%)</td><td>596.00 <b>(+23.83%)</b></td><td>535.40 <b>(+95.12%)</b></td><td>75.35 <b>(-77.17%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>7.64 (n/a)</td><td>4.34 (n/a)</td><td>4.36 (n/a)</td><td>1.84 (n/a)</td><td>2.14 (n/a)</td><td>1141.30 (n/a)</td><td>599.16 (n/a)</td><td>481.30 (n/a)</td><td>274.40 (n/a)</td><td>330.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.44 <b>(+21.48%)</b></td><td>3.12 (-2.51%)</td><td>2.44 <b>(-22.47%)</b></td><td>0.60 (+3.45%)</td><td>2.57 <b>(+26.96%)</b></td><td>3489.80 (-3.34%)</td><td>1265.14 (+4.36%)</td><td>858.90 <b>(+28.98%)</b></td><td>281.90 (-17.69%)</td><td>1272.38 (-6.09%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.12 (n/a)</td><td>3.20 (n/a)</td><td>3.15 (n/a)</td><td>0.58 (n/a)</td><td>2.03 (n/a)</td><td>3610.30 (n/a)</td><td>1212.26 (n/a)</td><td>665.90 (n/a)</td><td>342.50 (n/a)</td><td>1354.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.76 (-9.56%)</td><td>3.60 (-13.70%)</td><td>4.00 (-17.18%)</td><td>1.25 (+0.40%)</td><td>1.45 (-13.25%)</td><td>3361.60 (-0.40%)</td><td>1492.76 (+9.52%)</td><td>1048.50 <b>(+20.75%)</b></td><td>881.80 (+10.57%)</td><td>1057.19 (-6.14%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.26 (n/a)</td><td>4.17 (n/a)</td><td>4.83 (n/a)</td><td>1.24 (n/a)</td><td>1.67 (n/a)</td><td>3375.00 (n/a)</td><td>1362.94 (n/a)</td><td>868.30 (n/a)</td><td>797.50 (n/a)</td><td>1126.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.26 (-12.04%)</td><td>4.73 (-10.57%)</td><td>4.07 <b>(-22.13%)</b></td><td>1.70 <b>(+51.14%)</b></td><td>2.29 (-17.04%)</td><td>2472.20 <b>(-33.84%)</b></td><td>1158.04 (-11.47%)</td><td>1030.10 <b>(+28.41%)</b></td><td>577.70 (+13.68%)</td><td>770.52 <b>(-43.65%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>8.25 (n/a)</td><td>5.29 (n/a)</td><td>5.23 (n/a)</td><td>1.12 (n/a)</td><td>2.76 (n/a)</td><td>3736.50 (n/a)</td><td>1308.10 (n/a)</td><td>802.20 (n/a)</td><td>508.20 (n/a)</td><td>1367.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.03 (-15.52%)</td><td>5.14 (+6.75%)</td><td>5.28 (-5.23%)</td><td>3.69 <b>(+217.14%)</b></td><td>1.39 <b>(-60.13%)</b></td><td>1136.60 <b>(-68.47%)</b></td><td>865.64 <b>(-51.88%)</b></td><td>794.00 (+5.51%)</td><td>596.30 (+18.38%)</td><td>233.66 <b>(-85.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>8.33 (n/a)</td><td>4.82 (n/a)</td><td>5.57 (n/a)</td><td>1.16 (n/a)</td><td>3.49 (n/a)</td><td>3604.70 (n/a)</td><td>1799.04 (n/a)</td><td>752.50 (n/a)</td><td>503.70 (n/a)</td><td>1649.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.86 <b>(-43.17%)</b></td><td>3.92 <b>(-42.32%)</b></td><td>3.98 <b>(-51.99%)</b></td><td>1.70 <b>(+52.42%)</b></td><td>1.48 <b>(-60.61%)</b></td><td>2464.60 <b>(-34.39%)</b></td><td>1262.18 (+5.93%)</td><td>1053.40 <b>(+108.26%)</b></td><td>715.60 <b>(+75.95%)</b></td><td>687.20 <b>(-52.41%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>10.31 (n/a)</td><td>6.80 (n/a)</td><td>8.29 (n/a)</td><td>1.12 (n/a)</td><td>3.75 (n/a)</td><td>3756.60 (n/a)</td><td>1191.56 (n/a)</td><td>505.80 (n/a)</td><td>406.70 (n/a)</td><td>1443.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>12.36 <b>(+30.76%)</b></td><td>8.63 <b>(+22.47%)</b></td><td>8.03 (+2.51%)</td><td>6.44 <b>(+104.60%)</b></td><td>2.34 (-12.40%)</td><td>650.90 <b>(-51.13%)</b></td><td>511.90 <b>(-27.25%)</b></td><td>522.10 (-2.45%)</td><td>339.30 <b>(-23.53%)</b></td><td>121.83 <b>(-67.29%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>9.45 (n/a)</td><td>7.05 (n/a)</td><td>7.84 (n/a)</td><td>3.15 (n/a)</td><td>2.67 (n/a)</td><td>1331.80 (n/a)</td><td>703.68 (n/a)</td><td>535.20 (n/a)</td><td>443.70 (n/a)</td><td>372.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.92 (-3.47%)</td><td>5.57 <b>(-27.94%)</b></td><td>5.59 <b>(-28.08%)</b></td><td>1.68 <b>(-75.79%)</b></td><td>2.56 <b>(+439.52%)</b></td><td>2494.20 <b>(+313.08%)</b></td><td>1035.10 <b>(+90.23%)</b></td><td>750.50 <b>(+39.06%)</b></td><td>529.40 (+3.58%)</td><td>828.17 <b>(+2240.60%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>8.21 (n/a)</td><td>7.73 (n/a)</td><td>7.77 (n/a)</td><td>6.95 (n/a)</td><td>0.47 (n/a)</td><td>603.80 (n/a)</td><td>544.14 (n/a)</td><td>539.70 (n/a)</td><td>511.10 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>1.87 (-1.16%)</td><td>1.48 (+17.90%)</td><td>1.52 <b>(+59.21%)</b></td><td>1.01 <b>(+20.36%)</b></td><td>0.33 <b>(-32.72%)</b></td><td>520.40 (-16.92%)</td><td>370.52 <b>(-20.61%)</b></td><td>344.50 <b>(-37.19%)</b></td><td>279.70 (+1.16%)</td><td>93.02 <b>(-41.47%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>1.90 (n/a)</td><td>1.25 (n/a)</td><td>0.96 (n/a)</td><td>0.84 (n/a)</td><td>0.49 (n/a)</td><td>626.40 (n/a)</td><td>466.72 (n/a)</td><td>548.50 (n/a)</td><td>276.50 (n/a)</td><td>158.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.52 (-6.63%)</td><td>1.62 (-14.90%)</td><td>2.26 (+0.28%)</td><td>0.42 <b>(+36.27%)</b></td><td>1.04 (+6.78%)</td><td>2495.90 <b>(-26.62%)</b></td><td>1143.90 (+8.26%)</td><td>463.30 (-0.28%)</td><td>415.80 (+7.11%)</td><td>984.71 <b>(-25.06%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.70 (n/a)</td><td>1.91 (n/a)</td><td>2.26 (n/a)</td><td>0.31 (n/a)</td><td>0.98 (n/a)</td><td>3401.30 (n/a)</td><td>1056.62 (n/a)</td><td>464.60 (n/a)</td><td>388.20 (n/a)</td><td>1313.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.82 (-5.12%)</td><td>1.78 (-6.07%)</td><td>1.77 <b>(+105.87%)</b></td><td>0.56 (-3.27%)</td><td>1.34 <b>(-20.35%)</b></td><td>3717.10 (+3.38%)</td><td>2008.72 (-6.59%)</td><td>1186.50 <b>(-51.43%)</b></td><td>549.60 (+5.39%)</td><td>1536.14 (+1.05%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>4.02 (n/a)</td><td>1.90 (n/a)</td><td>0.86 (n/a)</td><td>0.58 (n/a)</td><td>1.69 (n/a)</td><td>3595.70 (n/a)</td><td>2150.46 (n/a)</td><td>2442.70 (n/a)</td><td>521.50 (n/a)</td><td>1520.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>1.77 (+17.55%)</td><td>1.05 (-0.18%)</td><td>0.94 <b>(-29.24%)</b></td><td>0.46 <b>(+70.50%)</b></td><td>0.56 (-0.09%)</td><td>1130.20 <b>(-41.35%)</b></td><td>644.40 (-16.00%)</td><td>555.90 <b>(+41.34%)</b></td><td>296.40 (-14.93%)</td><td>354.71 <b>(-47.64%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>1.50 (n/a)</td><td>1.05 (n/a)</td><td>1.33 (n/a)</td><td>0.27 (n/a)</td><td>0.56 (n/a)</td><td>1927.10 (n/a)</td><td>767.18 (n/a)</td><td>393.30 (n/a)</td><td>348.40 (n/a)</td><td>677.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 <b>(-24.87%)</b></td><td>0.09 <b>(-24.82%)</b></td><td>0.08 <b>(-25.15%)</b></td><td>0.06 <b>(-24.55%)</b></td><td>0.03 <b>(-22.87%)</b></td><td>553.70 <b>(+32.53%)</b></td><td>392.26 <b>(+33.42%)</b></td><td>399.70 <b>(+33.59%)</b></td><td>256.70 <b>(+33.07%)</b></td><td>110.75 <b>(+35.51%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>417.80 (n/a)</td><td>294.00 (n/a)</td><td>299.20 (n/a)</td><td>192.90 (n/a)</td><td>81.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (+2.89%)</td><td>0.08 <b>(-22.42%)</b></td><td>0.06 <b>(-48.75%)</b></td><td>0.04 <b>(-33.42%)</b></td><td>0.04 <b>(+24.04%)</b></td><td>742.60 <b>(+50.17%)</b></td><td>482.28 <b>(+43.75%)</b></td><td>508.30 <b>(+95.12%)</b></td><td>231.80 (-2.81%)</td><td>225.62 <b>(+81.48%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>494.50 (n/a)</td><td>335.50 (n/a)</td><td>260.50 (n/a)</td><td>238.50 (n/a)</td><td>124.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.25 <b>(-29.81%)</b></td><td>0.18 (-19.69%)</td><td>0.14 <b>(-36.94%)</b></td><td>0.12 (-2.88%)</td><td>0.06 <b>(-29.00%)</b></td><td>540.80 (+2.97%)</td><td>411.62 <b>(+21.07%)</b></td><td>480.40 <b>(+58.60%)</b></td><td>257.10 <b>(+42.52%)</b></td><td>134.59 (+2.42%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>525.20 (n/a)</td><td>339.98 (n/a)</td><td>302.90 (n/a)</td><td>180.40 (n/a)</td><td>131.41 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.28 (+6.60%)</td><td>0.16 <b>(-23.82%)</b></td><td>0.14 <b>(-37.98%)</b></td><td>0.13 (-0.68%)</td><td>0.07 <b>(+27.99%)</b></td><td>515.40 (+0.70%)</td><td>442.04 <b>(+34.93%)</b></td><td>484.40 <b>(+61.20%)</b></td><td>232.30 (-6.18%)</td><td>118.12 (+11.39%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>511.80 (n/a)</td><td>327.60 (n/a)</td><td>300.50 (n/a)</td><td>247.60 (n/a)</td><td>106.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.29 (+10.20%)</td><td>0.20 (+12.42%)</td><td>0.23 <b>(+26.23%)</b></td><td>0.11 (-5.59%)</td><td>0.09 <b>(+53.02%)</b></td><td>602.60 (+5.92%)</td><td>384.38 (-1.69%)</td><td>286.20 <b>(-20.79%)</b></td><td>222.50 (-9.26%)</td><td>185.26 <b>(+53.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>568.90 (n/a)</td><td>391.00 (n/a)</td><td>361.30 (n/a)</td><td>245.20 (n/a)</td><td>120.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.50 (-15.02%)</td><td>0.42 <b>(+23.37%)</b></td><td>0.43 <b>(+41.66%)</b></td><td>0.29 <b>(+33.96%)</b></td><td>0.08 <b>(-49.62%)</b></td><td>446.50 <b>(-25.35%)</b></td><td>322.90 <b>(-26.62%)</b></td><td>305.30 <b>(-29.39%)</b></td><td>264.60 (+17.65%)</td><td>71.28 <b>(-55.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.58 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>598.10 (n/a)</td><td>440.04 (n/a)</td><td>432.40 (n/a)</td><td>224.90 (n/a)</td><td>160.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.49 (+2.88%)</td><td>0.34 (-2.63%)</td><td>0.29 <b>(-36.25%)</b></td><td>0.23 <b>(+86.57%)</b></td><td>0.13 (-18.93%)</td><td>570.50 <b>(-46.40%)</b></td><td>423.18 (-12.82%)</td><td>447.50 <b>(+56.85%)</b></td><td>269.10 (-2.78%)</td><td>146.44 <b>(-56.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.46 (n/a)</td><td>0.12 (n/a)</td><td>0.16 (n/a)</td><td>1064.30 (n/a)</td><td>485.42 (n/a)</td><td>285.30 (n/a)</td><td>276.80 (n/a)</td><td>339.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.54 (-2.88%)</td><td>0.35 (+15.54%)</td><td>0.34 <b>(+31.96%)</b></td><td>0.20 (-0.51%)</td><td>0.12 (-13.32%)</td><td>647.00 (+0.51%)</td><td>410.60 (-15.21%)</td><td>386.80 <b>(-24.23%)</b></td><td>242.30 (+2.97%)</td><td>149.71 (-1.89%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.56 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>643.70 (n/a)</td><td>484.26 (n/a)</td><td>510.50 (n/a)</td><td>235.30 (n/a)</td><td>152.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (+6.19%)</td><td>0.05 (-8.61%)</td><td>0.04 <b>(-35.34%)</b></td><td>0.03 (-15.59%)</td><td>0.02 <b>(+24.87%)</b></td><td>568.80 (+18.48%)</td><td>399.50 (+14.50%)</td><td>441.70 <b>(+54.66%)</b></td><td>225.90 (-5.84%)</td><td>146.67 <b>(+29.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>480.10 (n/a)</td><td>348.90 (n/a)</td><td>285.60 (n/a)</td><td>239.90 (n/a)</td><td>113.21 (n/a)</td>
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
