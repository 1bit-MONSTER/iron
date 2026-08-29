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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (-13.94%)</td><td>0.02 <b>(+40.05%)</b></td><td>0.02 <b>(+76.38%)</b></td><td>0.02 <b>(+48.45%)</b></td><td>0.00 <b>(-50.90%)</b></td><td>393.10 <b>(-32.63%)</b></td><td>283.20 <b>(-36.38%)</b></td><td>260.20 <b>(-43.31%)</b></td><td>238.20 (+16.20%)</td><td>62.78 <b>(-59.94%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.50 (n/a)</td><td>445.14 (n/a)</td><td>459.00 (n/a)</td><td>205.00 (n/a)</td><td>156.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(+87.62%)</b></td><td>0.02 <b>(+53.62%)</b></td><td>0.02 <b>(+72.18%)</b></td><td>0.01 (+3.91%)</td><td>0.01 <b>(+478.48%)</b></td><td>513.10 (-3.77%)</td><td>337.34 <b>(-29.89%)</b></td><td>277.90 <b>(-41.93%)</b></td><td>236.00 <b>(-46.71%)</b></td><td>113.54 <b>(+203.04%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.20 (n/a)</td><td>481.14 (n/a)</td><td>478.60 (n/a)</td><td>442.90 (n/a)</td><td>37.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+0.70%)</td><td>0.02 (-0.22%)</td><td>0.02 (-5.54%)</td><td>0.01 (+16.00%)</td><td>0.01 <b>(-25.02%)</b></td><td>433.00 (-13.80%)</td><td>329.78 (-5.18%)</td><td>292.90 (+5.85%)</td><td>235.20 (-0.72%)</td><td>88.78 <b>(-33.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>502.30 (n/a)</td><td>347.78 (n/a)</td><td>276.70 (n/a)</td><td>236.90 (n/a)</td><td>134.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(+71.60%)</b></td><td>0.02 <b>(+45.49%)</b></td><td>0.02 <b>(+56.04%)</b></td><td>0.01 (+3.71%)</td><td>0.01 <b>(+155.18%)</b></td><td>554.60 (-3.58%)</td><td>363.48 <b>(-24.99%)</b></td><td>333.20 <b>(-35.91%)</b></td><td>194.70 <b>(-41.71%)</b></td><td>136.52 <b>(+46.91%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.20 (n/a)</td><td>484.60 (n/a)</td><td>519.90 (n/a)</td><td>334.00 (n/a)</td><td>92.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(-22.09%)</b></td><td>0.02 (-9.30%)</td><td>0.01 (+8.53%)</td><td>0.01 <b>(+26.50%)</b></td><td>0.01 <b>(-41.95%)</b></td><td>638.70 <b>(-20.95%)</b></td><td>443.92 (-4.59%)</td><td>466.80 (-7.86%)</td><td>289.90 <b>(+28.33%)</b></td><td>148.74 <b>(-38.55%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>808.00 (n/a)</td><td>465.26 (n/a)</td><td>506.60 (n/a)</td><td>225.90 (n/a)</td><td>242.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(-24.42%)</b></td><td>0.02 <b>(-20.21%)</b></td><td>0.01 (-7.29%)</td><td>0.01 <b>(-25.71%)</b></td><td>0.01 <b>(-23.46%)</b></td><td>757.70 <b>(+34.63%)</b></td><td>479.90 <b>(+25.48%)</b></td><td>500.50 (+7.87%)</td><td>241.80 <b>(+32.28%)</b></td><td>220.15 <b>(+33.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.80 (n/a)</td><td>382.46 (n/a)</td><td>464.00 (n/a)</td><td>182.80 (n/a)</td><td>165.53 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(+22.81%)</b></td><td>0.03 (-6.62%)</td><td>0.03 <b>(-27.14%)</b></td><td>0.02 (+1.19%)</td><td>0.02 <b>(+32.95%)</b></td><td>604.80 (-1.18%)</td><td>440.44 (+11.31%)</td><td>480.00 <b>(+37.26%)</b></td><td>195.30 (-18.59%)</td><td>161.16 (+2.44%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>612.00 (n/a)</td><td>395.68 (n/a)</td><td>349.70 (n/a)</td><td>239.90 (n/a)</td><td>157.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (+4.08%)</td><td>0.03 <b>(-29.61%)</b></td><td>0.03 <b>(-43.89%)</b></td><td>0.02 <b>(-42.12%)</b></td><td>0.01 <b>(+193.30%)</b></td><td>518.20 <b>(+72.73%)</b></td><td>412.00 <b>(+53.42%)</b></td><td>467.90 <b>(+78.25%)</b></td><td>236.10 (-3.95%)</td><td>115.57 <b>(+383.63%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>300.00 (n/a)</td><td>268.54 (n/a)</td><td>262.50 (n/a)</td><td>245.80 (n/a)</td><td>23.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (-19.64%)</td><td>0.04 (-14.77%)</td><td>0.03 (-15.82%)</td><td>0.02 (-7.22%)</td><td>0.01 <b>(-30.56%)</b></td><td>572.40 (+7.80%)</td><td>380.40 (+11.55%)</td><td>355.50 (+18.82%)</td><td>231.00 <b>(+24.46%)</b></td><td>130.59 (-8.66%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>531.00 (n/a)</td><td>341.02 (n/a)</td><td>299.20 (n/a)</td><td>185.60 (n/a)</td><td>142.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (-0.85%)</td><td>0.03 (-19.39%)</td><td>0.02 <b>(-56.03%)</b></td><td>0.02 (-11.46%)</td><td>0.02 (-0.29%)</td><td>680.90 (+12.96%)</td><td>446.68 <b>(+25.15%)</b></td><td>540.70 <b>(+127.47%)</b></td><td>191.80 (+0.89%)</td><td>204.16 (+7.12%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>602.80 (n/a)</td><td>356.92 (n/a)</td><td>237.70 (n/a)</td><td>190.10 (n/a)</td><td>190.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (-13.38%)</td><td>0.03 <b>(-29.48%)</b></td><td>0.02 <b>(-37.01%)</b></td><td>0.02 <b>(-40.39%)</b></td><td>0.01 (+6.12%)</td><td>799.10 <b>(+67.74%)</b></td><td>525.06 <b>(+48.91%)</b></td><td>504.80 <b>(+58.74%)</b></td><td>292.00 (+15.46%)</td><td>180.92 <b>(+95.88%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.40 (n/a)</td><td>352.60 (n/a)</td><td>318.00 (n/a)</td><td>252.90 (n/a)</td><td>92.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (-19.42%)</td><td>0.03 (+12.85%)</td><td>0.03 <b>(+22.89%)</b></td><td>0.03 <b>(+292.36%)</b></td><td>0.01 <b>(-62.03%)</b></td><td>475.20 <b>(-74.51%)</b></td><td>402.52 <b>(-42.65%)</b></td><td>417.50 (-18.62%)</td><td>308.30 <b>(+24.11%)</b></td><td>74.24 <b>(-88.78%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1864.50 (n/a)</td><td>701.86 (n/a)</td><td>513.00 (n/a)</td><td>248.40 (n/a)</td><td>661.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (+14.02%)</td><td>0.07 <b>(+34.17%)</b></td><td>0.06 <b>(+28.55%)</b></td><td>0.05 <b>(+24.07%)</b></td><td>0.03 <b>(+24.73%)</b></td><td>496.60 (-19.40%)</td><td>360.24 <b>(-24.82%)</b></td><td>392.20 <b>(-22.20%)</b></td><td>235.00 (-12.28%)</td><td>116.77 (-12.55%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>616.10 (n/a)</td><td>479.20 (n/a)</td><td>504.10 (n/a)</td><td>267.90 (n/a)</td><td>133.53 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (+19.15%)</td><td>0.08 <b>(+41.97%)</b></td><td>0.08 <b>(+71.25%)</b></td><td>0.04 (-0.05%)</td><td>0.02 <b>(+37.28%)</b></td><td>553.90 (+0.05%)</td><td>337.58 <b>(-27.42%)</b></td><td>290.90 <b>(-41.61%)</b></td><td>260.80 (-16.06%)</td><td>121.78 <b>(+23.31%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>553.60 (n/a)</td><td>465.14 (n/a)</td><td>498.20 (n/a)</td><td>310.70 (n/a)</td><td>98.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.11 (+12.99%)</td><td>0.08 (+17.53%)</td><td>0.09 <b>(+55.92%)</b></td><td>0.04 (-16.29%)</td><td>0.03 <b>(+55.79%)</b></td><td>610.20 (+19.46%)</td><td>369.10 (-6.37%)</td><td>275.50 <b>(-35.86%)</b></td><td>228.40 (-11.47%)</td><td>175.66 <b>(+60.27%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>510.80 (n/a)</td><td>394.20 (n/a)</td><td>429.50 (n/a)</td><td>258.00 (n/a)</td><td>109.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+3.06%)</td><td>0.09 <b>(+23.12%)</b></td><td>0.09 <b>(+77.79%)</b></td><td>0.05 (+12.06%)</td><td>0.03 (-19.95%)</td><td>526.50 (-10.75%)</td><td>300.28 <b>(-24.99%)</b></td><td>272.80 <b>(-43.76%)</b></td><td>181.80 (-2.99%)</td><td>132.05 <b>(-24.91%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>589.90 (n/a)</td><td>400.34 (n/a)</td><td>485.10 (n/a)</td><td>187.40 (n/a)</td><td>175.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 <b>(+26.66%)</b></td><td>0.09 <b>(+32.93%)</b></td><td>0.10 (+17.70%)</td><td>0.05 <b>(+36.87%)</b></td><td>0.03 (-0.71%)</td><td>465.60 <b>(-26.93%)</b></td><td>285.04 <b>(-28.88%)</b></td><td>250.10 (-15.05%)</td><td>196.80 <b>(-21.06%)</b></td><td>105.17 <b>(-40.08%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>637.20 (n/a)</td><td>400.80 (n/a)</td><td>294.40 (n/a)</td><td>249.30 (n/a)</td><td>175.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (+2.74%)</td><td>0.07 (+10.93%)</td><td>0.05 (-3.68%)</td><td>0.04 <b>(+26.60%)</b></td><td>0.03 (+1.85%)</td><td>641.80 <b>(-21.02%)</b></td><td>435.18 (-14.03%)</td><td>479.60 (+3.81%)</td><td>240.60 (-2.67%)</td><td>182.22 <b>(-27.13%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>812.60 (n/a)</td><td>506.18 (n/a)</td><td>462.00 (n/a)</td><td>247.20 (n/a)</td><td>250.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.19 (-9.19%)</td><td>0.10 <b>(-37.31%)</b></td><td>0.09 <b>(-50.09%)</b></td><td>0.02 <b>(-78.57%)</b></td><td>0.06 (+13.65%)</td><td>2497.70 <b>(+366.69%)</b></td><td>860.88 <b>(+151.18%)</b></td><td>539.50 <b>(+100.33%)</b></td><td>256.90 (+10.12%)</td><td>924.34 <b>(+579.77%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>535.20 (n/a)</td><td>342.74 (n/a)</td><td>269.30 (n/a)</td><td>233.30 (n/a)</td><td>135.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.18 (-5.14%)</td><td>0.14 (+14.04%)</td><td>0.13 (+18.26%)</td><td>0.11 <b>(+347.47%)</b></td><td>0.03 <b>(-62.70%)</b></td><td>432.10 <b>(-77.65%)</b></td><td>364.20 <b>(-46.59%)</b></td><td>386.60 (-15.42%)</td><td>275.50 (+5.39%)</td><td>60.29 <b>(-91.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1933.70 (n/a)</td><td>681.92 (n/a)</td><td>457.10 (n/a)</td><td>261.40 (n/a)</td><td>707.83 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.17 (-17.72%)</td><td>0.13 (+0.05%)</td><td>0.13 <b>(+36.57%)</b></td><td>0.09 (-5.60%)</td><td>0.03 <b>(-33.67%)</b></td><td>563.00 (+5.93%)</td><td>407.58 (-4.33%)</td><td>371.10 <b>(-26.78%)</b></td><td>296.40 <b>(+21.53%)</b></td><td>110.02 (-17.62%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>531.50 (n/a)</td><td>426.04 (n/a)</td><td>506.80 (n/a)</td><td>243.90 (n/a)</td><td>133.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.19 (-3.74%)</td><td>0.11 (-17.53%)</td><td>0.09 <b>(-22.05%)</b></td><td>0.02 <b>(-53.29%)</b></td><td>0.06 (+5.03%)</td><td>2098.80 <b>(+114.08%)</b></td><td>757.72 <b>(+58.94%)</b></td><td>527.60 <b>(+28.28%)</b></td><td>253.70 (+3.89%)</td><td>760.54 <b>(+155.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>980.40 (n/a)</td><td>476.72 (n/a)</td><td>411.30 (n/a)</td><td>244.20 (n/a)</td><td>297.42 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.21 (+0.57%)</td><td>0.18 (+6.66%)</td><td>0.19 (+9.39%)</td><td>0.09 (-10.07%)</td><td>0.05 <b>(+20.57%)</b></td><td>552.00 (+11.18%)</td><td>310.44 (-2.60%)</td><td>253.40 (-8.59%)</td><td>231.60 (-0.56%)</td><td>136.20 <b>(+31.38%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>496.50 (n/a)</td><td>318.72 (n/a)</td><td>277.20 (n/a)</td><td>232.90 (n/a)</td><td>103.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.27 <b>(+54.02%)</b></td><td>0.17 (+17.60%)</td><td>0.18 (+10.77%)</td><td>0.11 (-2.85%)</td><td>0.07 <b>(+118.98%)</b></td><td>461.20 (+2.92%)</td><td>326.44 (-8.15%)</td><td>280.30 (-9.73%)</td><td>182.00 <b>(-35.07%)</b></td><td>118.13 <b>(+48.97%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>448.10 (n/a)</td><td>355.42 (n/a)</td><td>310.50 (n/a)</td><td>280.30 (n/a)</td><td>79.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (+2.03%)</td><td>0.01 (-10.83%)</td><td>0.01 (-10.62%)</td><td>0.00 <b>(-52.81%)</b></td><td>0.00 <b>(+81.88%)</b></td><td>763.60 <b>(+111.93%)</b></td><td>375.28 <b>(+29.97%)</b></td><td>296.70 (+11.88%)</td><td>233.00 (-2.02%)</td><td>218.72 <b>(+316.58%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>360.30 (n/a)</td><td>288.74 (n/a)</td><td>265.20 (n/a)</td><td>237.80 (n/a)</td><td>52.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (-16.47%)</td><td>0.01 (-13.80%)</td><td>0.01 (-15.01%)</td><td>0.01 <b>(+27.55%)</b></td><td>0.00 <b>(-40.07%)</b></td><td>484.90 <b>(-21.60%)</b></td><td>374.74 (+7.09%)</td><td>342.50 (+17.66%)</td><td>278.90 (+19.70%)</td><td>91.60 <b>(-42.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>618.50 (n/a)</td><td>349.94 (n/a)</td><td>291.10 (n/a)</td><td>233.00 (n/a)</td><td>159.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (-15.67%)</td><td>0.01 (-5.30%)</td><td>0.01 (-5.18%)</td><td>0.00 <b>(-20.43%)</b></td><td>0.00 (-6.85%)</td><td>750.70 <b>(+25.68%)</b></td><td>447.90 (+8.28%)</td><td>444.20 (+5.46%)</td><td>287.20 (+18.58%)</td><td>185.96 <b>(+38.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>597.30 (n/a)</td><td>413.64 (n/a)</td><td>421.20 (n/a)</td><td>242.20 (n/a)</td><td>134.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-31.01%)</b></td><td>0.01 <b>(-31.45%)</b></td><td>0.01 <b>(-37.17%)</b></td><td>0.00 (-16.46%)</td><td>0.00 <b>(-47.01%)</b></td><td>630.90 (+19.69%)</td><td>496.94 <b>(+40.42%)</b></td><td>501.70 <b>(+59.17%)</b></td><td>356.70 <b>(+44.94%)</b></td><td>101.78 (-10.28%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>527.10 (n/a)</td><td>353.90 (n/a)</td><td>315.20 (n/a)</td><td>246.10 (n/a)</td><td>113.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-38.69%)</b></td><td>0.01 (-15.78%)</td><td>0.01 <b>(+23.88%)</b></td><td>0.00 (-1.25%)</td><td>0.00 <b>(-45.45%)</b></td><td>1860.40 (+1.27%)</td><td>699.22 (-1.09%)</td><td>457.60 (-19.28%)</td><td>305.60 <b>(+63.16%)</b></td><td>654.45 (-1.15%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1837.10 (n/a)</td><td>706.92 (n/a)</td><td>566.90 (n/a)</td><td>187.30 (n/a)</td><td>662.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (+14.58%)</td><td>0.00 (+7.26%)</td><td>0.00 (-7.44%)</td><td>0.00 <b>(+89.95%)</b></td><td>0.00 (-18.41%)</td><td>1032.60 <b>(-47.35%)</b></td><td>622.84 <b>(-22.99%)</b></td><td>569.60 (+8.02%)</td><td>426.80 (-12.72%)</td><td>239.97 <b>(-62.78%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1961.40 (n/a)</td><td>808.82 (n/a)</td><td>527.30 (n/a)</td><td>489.00 (n/a)</td><td>644.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (-0.82%)</td><td>0.01 (-12.47%)</td><td>0.01 <b>(-24.69%)</b></td><td>0.01 (-9.37%)</td><td>0.01 (-6.84%)</td><td>603.80 (+10.34%)</td><td>394.70 (+13.31%)</td><td>359.00 <b>(+32.77%)</b></td><td>223.20 (+0.86%)</td><td>148.27 (+3.14%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.20 (n/a)</td><td>348.34 (n/a)</td><td>270.40 (n/a)</td><td>221.30 (n/a)</td><td>143.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(+28.92%)</b></td><td>0.02 (+10.89%)</td><td>0.02 (+11.87%)</td><td>0.01 (-15.27%)</td><td>0.01 <b>(+76.66%)</b></td><td>605.10 (+18.02%)</td><td>384.32 (+3.07%)</td><td>298.20 (-10.61%)</td><td>183.10 <b>(-22.45%)</b></td><td>191.12 <b>(+74.01%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.70 (n/a)</td><td>372.86 (n/a)</td><td>333.60 (n/a)</td><td>236.10 (n/a)</td><td>109.83 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (-2.40%)</td><td>0.01 (-7.86%)</td><td>0.01 (-5.13%)</td><td>0.01 (-9.50%)</td><td>0.01 (-6.59%)</td><td>632.30 (+10.48%)</td><td>445.84 (+7.97%)</td><td>546.20 (+5.40%)</td><td>210.60 (+2.43%)</td><td>183.76 (+5.52%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.30 (n/a)</td><td>412.94 (n/a)</td><td>518.20 (n/a)</td><td>205.60 (n/a)</td><td>174.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (-2.60%)</td><td>0.02 (+14.09%)</td><td>0.01 <b>(+33.34%)</b></td><td>0.01 <b>(+81.19%)</b></td><td>0.00 <b>(-47.54%)</b></td><td>416.80 <b>(-44.82%)</b></td><td>348.08 <b>(-25.02%)</b></td><td>375.30 <b>(-25.00%)</b></td><td>254.90 (+2.66%)</td><td>71.73 <b>(-66.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>755.30 (n/a)</td><td>464.26 (n/a)</td><td>500.40 (n/a)</td><td>248.30 (n/a)</td><td>216.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (-5.10%)</td><td>0.02 (+4.28%)</td><td>0.02 <b>(+27.31%)</b></td><td>0.01 (+2.06%)</td><td>0.01 (-8.67%)</td><td>593.60 (-2.01%)</td><td>363.68 (-5.45%)</td><td>303.60 <b>(-21.47%)</b></td><td>242.50 (+5.39%)</td><td>149.53 (-3.72%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.80 (n/a)</td><td>384.64 (n/a)</td><td>386.60 (n/a)</td><td>230.10 (n/a)</td><td>155.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(+64.53%)</b></td><td>0.01 <b>(+43.80%)</b></td><td>0.01 <b>(+26.09%)</b></td><td>0.01 <b>(+44.48%)</b></td><td>0.01 <b>(+89.80%)</b></td><td>555.00 <b>(-30.78%)</b></td><td>394.92 <b>(-28.40%)</b></td><td>423.00 <b>(-20.70%)</b></td><td>217.00 <b>(-39.22%)</b></td><td>124.97 <b>(-23.98%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>801.80 (n/a)</td><td>551.54 (n/a)</td><td>533.40 (n/a)</td><td>357.00 (n/a)</td><td>164.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 <b>(+22.88%)</b></td><td>0.03 <b>(+35.38%)</b></td><td>0.04 <b>(+46.96%)</b></td><td>0.02 (+5.31%)</td><td>0.01 <b>(+38.86%)</b></td><td>496.50 (-5.03%)</td><td>321.30 <b>(-24.51%)</b></td><td>283.10 <b>(-31.95%)</b></td><td>240.40 (-18.65%)</td><td>102.36 (+10.42%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.80 (n/a)</td><td>425.64 (n/a)</td><td>416.00 (n/a)</td><td>295.50 (n/a)</td><td>92.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(+44.18%)</b></td><td>0.04 (+13.59%)</td><td>0.04 (+2.71%)</td><td>0.02 <b>(+99.48%)</b></td><td>0.02 <b>(+38.55%)</b></td><td>538.40 <b>(-49.87%)</b></td><td>355.60 <b>(-20.32%)</b></td><td>290.90 (-2.64%)</td><td>161.90 <b>(-30.63%)</b></td><td>163.17 <b>(-53.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1074.00 (n/a)</td><td>446.30 (n/a)</td><td>298.80 (n/a)</td><td>233.40 (n/a)</td><td>353.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (+16.27%)</td><td>0.03 (-18.98%)</td><td>0.02 <b>(-46.05%)</b></td><td>0.02 (-7.40%)</td><td>0.02 <b>(+35.76%)</b></td><td>622.40 (+7.98%)</td><td>491.80 <b>(+31.94%)</b></td><td>548.50 <b>(+85.37%)</b></td><td>192.20 (-14.00%)</td><td>175.65 (+16.02%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.40 (n/a)</td><td>372.74 (n/a)</td><td>295.90 (n/a)</td><td>223.50 (n/a)</td><td>151.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(+38.38%)</b></td><td>0.03 <b>(+27.44%)</b></td><td>0.03 <b>(+47.53%)</b></td><td>0.02 (-2.18%)</td><td>0.02 <b>(+71.21%)</b></td><td>512.10 (+2.22%)</td><td>355.38 (-14.25%)</td><td>324.20 <b>(-32.22%)</b></td><td>171.80 <b>(-27.75%)</b></td><td>149.73 <b>(+35.94%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.00 (n/a)</td><td>414.42 (n/a)</td><td>478.30 (n/a)</td><td>237.80 (n/a)</td><td>110.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (-3.23%)</td><td>0.03 (-0.80%)</td><td>0.03 (+1.95%)</td><td>0.02 (+11.39%)</td><td>0.01 (-19.04%)</td><td>520.60 (-10.23%)</td><td>391.88 (-4.30%)</td><td>410.50 (-1.91%)</td><td>235.80 (+3.38%)</td><td>115.85 <b>(-26.24%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>579.90 (n/a)</td><td>409.50 (n/a)</td><td>418.50 (n/a)</td><td>228.10 (n/a)</td><td>157.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (-1.39%)</td><td>0.03 (-6.99%)</td><td>0.02 (+1.21%)</td><td>0.01 <b>(-61.09%)</b></td><td>0.02 <b>(+30.21%)</b></td><td>1385.40 <b>(+156.98%)</b></td><td>618.30 <b>(+41.83%)</b></td><td>497.30 (-1.21%)</td><td>221.80 (+1.42%)</td><td>463.49 <b>(+247.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.10 (n/a)</td><td>435.94 (n/a)</td><td>503.40 (n/a)</td><td>218.70 (n/a)</td><td>133.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (-0.91%)</td><td>0.06 (+5.37%)</td><td>0.06 (+19.63%)</td><td>0.04 (-7.41%)</td><td>0.01 (-2.05%)</td><td>546.60 (+8.00%)</td><td>377.22 (-4.77%)</td><td>361.80 (-16.40%)</td><td>294.00 (+0.93%)</td><td>101.78 (+10.71%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>506.10 (n/a)</td><td>396.12 (n/a)</td><td>432.80 (n/a)</td><td>291.30 (n/a)</td><td>91.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (+19.20%)</td><td>0.07 (+19.18%)</td><td>0.07 <b>(+64.64%)</b></td><td>0.04 (+3.42%)</td><td>0.03 <b>(+22.08%)</b></td><td>515.00 (-3.32%)</td><td>354.56 (-14.36%)</td><td>297.80 <b>(-39.26%)</b></td><td>200.20 (-16.09%)</td><td>133.79 (+2.06%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>532.70 (n/a)</td><td>414.00 (n/a)</td><td>490.30 (n/a)</td><td>238.60 (n/a)</td><td>131.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (+6.28%)</td><td>0.05 <b>(-20.58%)</b></td><td>0.04 <b>(-22.87%)</b></td><td>0.01 <b>(-73.99%)</b></td><td>0.03 <b>(+88.46%)</b></td><td>1960.60 <b>(+284.43%)</b></td><td>751.12 <b>(+97.58%)</b></td><td>516.40 <b>(+29.65%)</b></td><td>264.60 (-5.90%)</td><td>701.23 <b>(+609.35%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>510.00 (n/a)</td><td>380.16 (n/a)</td><td>398.30 (n/a)</td><td>281.20 (n/a)</td><td>98.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (+18.59%)</td><td>0.07 <b>(+30.11%)</b></td><td>0.06 <b>(+29.70%)</b></td><td>0.04 (+17.65%)</td><td>0.02 (+18.10%)</td><td>503.40 (-14.99%)</td><td>353.98 <b>(-23.01%)</b></td><td>353.40 <b>(-22.89%)</b></td><td>206.60 (-15.67%)</td><td>119.88 (-13.92%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>592.20 (n/a)</td><td>459.80 (n/a)</td><td>458.30 (n/a)</td><td>245.00 (n/a)</td><td>139.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (+9.77%)</td><td>0.07 <b>(+36.73%)</b></td><td>0.07 <b>(+89.57%)</b></td><td>0.04 <b>(+33.92%)</b></td><td>0.02 (-7.78%)</td><td>487.80 <b>(-25.33%)</b></td><td>345.60 <b>(-30.92%)</b></td><td>298.00 <b>(-47.25%)</b></td><td>204.70 (-8.90%)</td><td>115.91 <b>(-33.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>653.30 (n/a)</td><td>500.32 (n/a)</td><td>564.90 (n/a)</td><td>224.70 (n/a)</td><td>174.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(+28.78%)</b></td><td>0.04 (+0.68%)</td><td>0.04 (-11.73%)</td><td>0.04 (+3.80%)</td><td>0.01 <b>(+97.97%)</b></td><td>587.60 (-3.66%)</td><td>497.32 (+2.04%)</td><td>540.40 (+13.29%)</td><td>332.10 <b>(-22.33%)</b></td><td>101.88 <b>(+41.63%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>609.90 (n/a)</td><td>487.38 (n/a)</td><td>477.00 (n/a)</td><td>427.60 (n/a)</td><td>71.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>531.00 (n/a)</td><td>410.76 (n/a)</td><td>454.10 (n/a)</td><td>274.50 (n/a)</td><td>117.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.60 (n/a)</td><td>444.10 (n/a)</td><td>449.80 (n/a)</td><td>238.70 (n/a)</td><td>132.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1004.50 (n/a)</td><td>542.76 (n/a)</td><td>435.80 (n/a)</td><td>298.40 (n/a)</td><td>275.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.60 (n/a)</td><td>332.44 (n/a)</td><td>291.90 (n/a)</td><td>264.90 (n/a)</td><td>104.62 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>780.60 (n/a)</td><td>473.78 (n/a)</td><td>504.80 (n/a)</td><td>231.60 (n/a)</td><td>218.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>604.60 (n/a)</td><td>423.20 (n/a)</td><td>421.70 (n/a)</td><td>294.20 (n/a)</td><td>128.96 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1858.30 (n/a)</td><td>643.52 (n/a)</td><td>394.60 (n/a)</td><td>238.90 (n/a)</td><td>686.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>619.80 (n/a)</td><td>456.58 (n/a)</td><td>561.00 (n/a)</td><td>235.30 (n/a)</td><td>175.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1927.30 (n/a)</td><td>636.38 (n/a)</td><td>297.30 (n/a)</td><td>290.20 (n/a)</td><td>722.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.20 (-14.46%)</td><td>0.13 (-0.71%)</td><td>0.11 (+5.01%)</td><td>0.05 <b>(-50.70%)</b></td><td>0.07 (+16.00%)</td><td>1050.10 <b>(+102.80%)</b></td><td>512.40 <b>(+20.09%)</b></td><td>460.50 (-4.78%)</td><td>244.10 (+16.91%)</td><td>330.97 <b>(+154.90%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>517.80 (n/a)</td><td>426.68 (n/a)</td><td>483.60 (n/a)</td><td>208.80 (n/a)</td><td>129.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>1065.80 (n/a)</td><td>508.42 (n/a)</td><td>390.40 (n/a)</td><td>244.80 (n/a)</td><td>326.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>550.20 (n/a)</td><td>401.24 (n/a)</td><td>428.90 (n/a)</td><td>233.40 (n/a)</td><td>134.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.80 (n/a)</td><td>396.14 (n/a)</td><td>380.40 (n/a)</td><td>278.40 (n/a)</td><td>113.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.30 (n/a)</td><td>441.50 (n/a)</td><td>454.90 (n/a)</td><td>281.10 (n/a)</td><td>157.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.60 (n/a)</td><td>462.14 (n/a)</td><td>478.20 (n/a)</td><td>289.10 (n/a)</td><td>138.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.20 (n/a)</td><td>363.44 (n/a)</td><td>295.50 (n/a)</td><td>244.50 (n/a)</td><td>135.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>554.90 (n/a)</td><td>422.52 (n/a)</td><td>448.10 (n/a)</td><td>192.60 (n/a)</td><td>147.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>539.60 (n/a)</td><td>395.90 (n/a)</td><td>423.30 (n/a)</td><td>192.10 (n/a)</td><td>154.39 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>623.60 (n/a)</td><td>428.58 (n/a)</td><td>467.40 (n/a)</td><td>236.10 (n/a)</td><td>146.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>693.00 (n/a)</td><td>448.12 (n/a)</td><td>467.40 (n/a)</td><td>200.70 (n/a)</td><td>217.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>664.80 (n/a)</td><td>442.00 (n/a)</td><td>447.60 (n/a)</td><td>242.50 (n/a)</td><td>166.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1850.00 (n/a)</td><td>730.48 (n/a)</td><td>548.80 (n/a)</td><td>239.90 (n/a)</td><td>642.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>647.40 (n/a)</td><td>435.14 (n/a)</td><td>490.30 (n/a)</td><td>241.00 (n/a)</td><td>162.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.10 (n/a)</td><td>484.96 (n/a)</td><td>496.50 (n/a)</td><td>371.20 (n/a)</td><td>97.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.40 (n/a)</td><td>343.74 (n/a)</td><td>292.90 (n/a)</td><td>202.90 (n/a)</td><td>153.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.30 (n/a)</td><td>426.74 (n/a)</td><td>487.50 (n/a)</td><td>259.40 (n/a)</td><td>127.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.70 (n/a)</td><td>406.48 (n/a)</td><td>413.30 (n/a)</td><td>239.30 (n/a)</td><td>150.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.70 (n/a)</td><td>450.56 (n/a)</td><td>437.20 (n/a)</td><td>244.90 (n/a)</td><td>168.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>523.10 (n/a)</td><td>389.60 (n/a)</td><td>366.30 (n/a)</td><td>260.90 (n/a)</td><td>126.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.80 (n/a)</td><td>414.40 (n/a)</td><td>446.20 (n/a)</td><td>245.90 (n/a)</td><td>161.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.50 (n/a)</td><td>366.94 (n/a)</td><td>282.50 (n/a)</td><td>240.20 (n/a)</td><td>138.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>441.90 (n/a)</td><td>335.28 (n/a)</td><td>381.10 (n/a)</td><td>222.50 (n/a)</td><td>101.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.90 (n/a)</td><td>399.16 (n/a)</td><td>355.20 (n/a)</td><td>276.70 (n/a)</td><td>116.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1068.90 (n/a)</td><td>580.62 (n/a)</td><td>528.50 (n/a)</td><td>246.20 (n/a)</td><td>299.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.30 (n/a)</td><td>454.50 (n/a)</td><td>466.50 (n/a)</td><td>340.70 (n/a)</td><td>105.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.40 (n/a)</td><td>428.26 (n/a)</td><td>462.30 (n/a)</td><td>269.90 (n/a)</td><td>136.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>655.30 (n/a)</td><td>451.60 (n/a)</td><td>456.00 (n/a)</td><td>284.50 (n/a)</td><td>159.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>564.10 (n/a)</td><td>458.24 (n/a)</td><td>539.40 (n/a)</td><td>219.00 (n/a)</td><td>147.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.90 (n/a)</td><td>413.04 (n/a)</td><td>427.30 (n/a)</td><td>241.80 (n/a)</td><td>127.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>716.90 (n/a)</td><td>495.72 (n/a)</td><td>559.90 (n/a)</td><td>286.50 (n/a)</td><td>186.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>990.10 (n/a)</td><td>499.88 (n/a)</td><td>423.10 (n/a)</td><td>295.50 (n/a)</td><td>285.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>608.60 (n/a)</td><td>400.64 (n/a)</td><td>298.40 (n/a)</td><td>268.80 (n/a)</td><td>163.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>641.20 (n/a)</td><td>427.36 (n/a)</td><td>358.50 (n/a)</td><td>256.70 (n/a)</td><td>177.58 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>666.40 (n/a)</td><td>355.94 (n/a)</td><td>286.00 (n/a)</td><td>262.90 (n/a)</td><td>174.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2349.20 (n/a)</td><td>768.50 (n/a)</td><td>435.60 (n/a)</td><td>239.40 (n/a)</td><td>893.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>446.28 (n/a)</td><td>473.20 (n/a)</td><td>341.00 (n/a)</td><td>69.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>560.00 (n/a)</td><td>447.56 (n/a)</td><td>476.00 (n/a)</td><td>271.20 (n/a)</td><td>123.37 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.64 <b>(+32.55%)</b></td><td>0.30 <b>(-25.39%)</b></td><td>0.32 (-19.14%)</td><td>0.09 <b>(-73.05%)</b></td><td>0.22 <b>(+205.87%)</b></td><td>2505.10 <b>(+271.02%)</b></td><td>1198.34 <b>(+112.22%)</b></td><td>701.90 <b>(+23.68%)</b></td><td>345.40 <b>(-24.55%)</b></td><td>906.44 <b>(+810.40%)</b></td><td>27.32 <b>(+32.55%)</b></td><td>12.79 <b>(-25.39%)</b></td><td>13.45 (-19.14%)</td><td>3.77 <b>(-73.05%)</b></td><td>9.36 <b>(+205.87%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>675.20 (n/a)</td><td>564.66 (n/a)</td><td>567.50 (n/a)</td><td>457.80 (n/a)</td><td>99.56 (n/a)</td><td>20.61 (n/a)</td><td>17.14 (n/a)</td><td>16.63 (n/a)</td><td>13.98 (n/a)</td><td>3.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.49 <b>(+33.03%)</b></td><td>0.39 <b>(+36.99%)</b></td><td>0.42 (+18.14%)</td><td>0.18 <b>(+36.36%)</b></td><td>0.12 (+9.16%)</td><td>1224.10 <b>(-26.67%)</b></td><td>649.82 <b>(-29.73%)</b></td><td>532.90 (-15.36%)</td><td>450.30 <b>(-24.84%)</b></td><td>323.00 <b>(-31.29%)</b></td><td>20.96 <b>(+33.03%)</b></td><td>16.53 <b>(+36.99%)</b></td><td>17.71 (+18.14%)</td><td>7.71 <b>(+36.36%)</b></td><td>5.12 (+9.16%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>1669.20 (n/a)</td><td>924.76 (n/a)</td><td>629.60 (n/a)</td><td>599.10 (n/a)</td><td>470.10 (n/a)</td><td>15.75 (n/a)</td><td>12.07 (n/a)</td><td>14.99 (n/a)</td><td>5.65 (n/a)</td><td>4.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.31 (+0.16%)</td><td>0.31 (+1.63%)</td><td>0.31 (+2.79%)</td><td>0.30 (+0.98%)</td><td>0.00 (-16.39%)</td><td>83086.80 (-0.97%)</td><td>81454.48 (-1.61%)</td><td>80963.80 (-2.72%)</td><td>80379.50 (-0.16%)</td><td>1093.77 (-16.98%)</td><td>213.73 (+0.16%)</td><td>210.94 (+1.63%)</td><td>212.19 (+2.79%)</td><td>206.77 (+0.98%)</td><td>2.81 (-16.39%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83897.80 (n/a)</td><td>82791.12 (n/a)</td><td>83225.40 (n/a)</td><td>80509.10 (n/a)</td><td>1317.42 (n/a)</td><td>213.39 (n/a)</td><td>207.55 (n/a)</td><td>206.43 (n/a)</td><td>204.77 (n/a)</td><td>3.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>1.01 (-1.37%)</td><td>1.01 (+0.27%)</td><td>1.01 (+0.03%)</td><td>1.01 (+3.63%)</td><td>0.00 <b>(-95.02%)</b></td><td>24882.60 (-3.50%)</td><td>24857.24 (-0.30%)</td><td>24860.10 (-0.03%)</td><td>24824.10 (+1.39%)</td><td>24.43 <b>(-95.14%)</b></td><td>692.07 (-1.37%)</td><td>691.14 (+0.27%)</td><td>691.06 (+0.03%)</td><td>690.44 (+3.63%)</td><td>0.68 <b>(-95.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25785.60 (n/a)</td><td>24932.68 (n/a)</td><td>24866.70 (n/a)</td><td>24483.00 (n/a)</td><td>503.19 (n/a)</td><td>701.71 (n/a)</td><td>689.27 (n/a)</td><td>690.88 (n/a)</td><td>666.26 (n/a)</td><td>13.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.83 (+0.44%)</td><td>0.81 (+2.91%)</td><td>0.83 (+2.55%)</td><td>0.79 (+7.32%)</td><td>0.02 <b>(-45.91%)</b></td><td>95919.10 (-6.82%)</td><td>92930.88 (-2.97%)</td><td>91430.40 (-2.48%)</td><td>90938.80 (-0.44%)</td><td>2428.37 <b>(-49.84%)</b></td><td>755.67 (+0.44%)</td><td>739.87 (+2.91%)</td><td>751.60 (+2.55%)</td><td>716.43 (+7.32%)</td><td>19.14 <b>(-45.91%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.83 (n/a)</td><td>0.79 (n/a)</td><td>0.81 (n/a)</td><td>0.73 (n/a)</td><td>0.04 (n/a)</td><td>102941.30 (n/a)</td><td>95774.80 (n/a)</td><td>93757.60 (n/a)</td><td>91336.50 (n/a)</td><td>4841.71 (n/a)</td><td>752.38 (n/a)</td><td>718.94 (n/a)</td><td>732.95 (n/a)</td><td>667.56 (n/a)</td><td>35.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.78 (+1.25%)</td><td>0.78 (+1.54%)</td><td>0.78 (+1.49%)</td><td>0.77 (+2.25%)</td><td>0.00 <b>(-37.04%)</b></td><td>97795.40 (-2.20%)</td><td>97057.12 (-1.52%)</td><td>96828.80 (-1.47%)</td><td>96561.40 (-1.24%)</td><td>550.37 <b>(-39.21%)</b></td><td>711.67 (+1.25%)</td><td>708.05 (+1.54%)</td><td>709.70 (+1.49%)</td><td>702.69 (+2.25%)</td><td>4.01 <b>(-37.04%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99992.10 (n/a)</td><td>98556.24 (n/a)</td><td>98270.90 (n/a)</td><td>97770.50 (n/a)</td><td>905.39 (n/a)</td><td>702.86 (n/a)</td><td>697.31 (n/a)</td><td>699.29 (n/a)</td><td>687.25 (n/a)</td><td>6.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.79 (-1.38%)</td><td>0.79 (-1.10%)</td><td>0.79 (-1.17%)</td><td>0.79 (-1.05%)</td><td>0.00 <b>(-27.22%)</b></td><td>96041.00 (+1.06%)</td><td>95483.90 (+1.11%)</td><td>95427.90 (+1.18%)</td><td>95171.00 (+1.40%)</td><td>338.24 <b>(-25.40%)</b></td><td>722.06 (-1.38%)</td><td>719.70 (-1.10%)</td><td>720.12 (-1.17%)</td><td>715.52 (-1.05%)</td><td>2.54 <b>(-27.22%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95036.10 (n/a)</td><td>94436.52 (n/a)</td><td>94314.30 (n/a)</td><td>93854.50 (n/a)</td><td>453.43 (n/a)</td><td>732.19 (n/a)</td><td>727.69 (n/a)</td><td>728.62 (n/a)</td><td>723.09 (n/a)</td><td>3.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.62 <b>(+20.49%)</b></td><td>3.60 (-2.77%)</td><td>3.92 (-1.40%)</td><td>2.17 (-16.26%)</td><td>1.45 <b>(+62.46%)</b></td><td>4111.20 (+19.42%)</td><td>2841.04 (+12.08%)</td><td>2274.50 (+1.42%)</td><td>1585.20 (-17.00%)</td><td>1164.69 <b>(+75.44%)</b></td><td>338.68 <b>(+20.49%)</b></td><td>216.82 (-2.77%)</td><td>236.04 (-1.40%)</td><td>130.59 (-16.26%)</td><td>87.56 <b>(+62.46%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>4.67 (n/a)</td><td>3.70 (n/a)</td><td>3.97 (n/a)</td><td>2.59 (n/a)</td><td>0.89 (n/a)</td><td>3442.70 (n/a)</td><td>2534.78 (n/a)</td><td>2242.70 (n/a)</td><td>1909.90 (n/a)</td><td>663.87 (n/a)</td><td>281.09 (n/a)</td><td>223.00 (n/a)</td><td>239.38 (n/a)</td><td>155.94 (n/a)</td><td>53.89 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>4.72 (-0.60%)</td><td>3.38 (+18.03%)</td><td>3.13 <b>(+26.46%)</b></td><td>2.10 (-3.43%)</td><td>0.98 (-9.38%)</td><td>4241.60 (+3.55%)</td><td>2838.50 (-16.18%)</td><td>2843.40 <b>(-20.92%)</b></td><td>1889.30 (+0.60%)</td><td>888.04 (-2.29%)</td><td>284.17 (-0.60%)</td><td>203.32 (+18.03%)</td><td>188.82 <b>(+26.46%)</b></td><td>126.57 (-3.43%)</td><td>58.82 (-9.38%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>4.75 (n/a)</td><td>2.86 (n/a)</td><td>2.48 (n/a)</td><td>2.18 (n/a)</td><td>1.08 (n/a)</td><td>4096.00 (n/a)</td><td>3386.44 (n/a)</td><td>3595.70 (n/a)</td><td>1878.00 (n/a)</td><td>908.87 (n/a)</td><td>285.88 (n/a)</td><td>172.26 (n/a)</td><td>149.31 (n/a)</td><td>131.07 (n/a)</td><td>64.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.65 (-1.98%)</td><td>4.51 (+9.58%)</td><td>5.23 <b>(+29.35%)</b></td><td>1.99 <b>(-26.93%)</b></td><td>1.48 (+8.03%)</td><td>4469.00 <b>(+36.85%)</b></td><td>2295.38 (-3.49%)</td><td>1704.40 <b>(-22.69%)</b></td><td>1576.60 (+2.02%)</td><td>1227.48 <b>(+53.15%)</b></td><td>340.52 (-1.98%)</td><td>271.43 (+9.58%)</td><td>315.00 <b>(+29.35%)</b></td><td>120.13 <b>(-26.93%)</b></td><td>89.23 (+8.03%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.77 (n/a)</td><td>4.11 (n/a)</td><td>4.04 (n/a)</td><td>2.73 (n/a)</td><td>1.37 (n/a)</td><td>3265.70 (n/a)</td><td>2378.34 (n/a)</td><td>2204.60 (n/a)</td><td>1545.40 (n/a)</td><td>801.48 (n/a)</td><td>347.39 (n/a)</td><td>247.69 (n/a)</td><td>243.52 (n/a)</td><td>164.40 (n/a)</td><td>82.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.88 (-13.49%)</td><td>5.18 (-11.62%)</td><td>5.42 (-16.94%)</td><td>4.16 (-7.45%)</td><td>0.70 <b>(-35.02%)</b></td><td>8371.30 (+8.05%)</td><td>6843.02 (+11.62%)</td><td>6429.90 <b>(+20.39%)</b></td><td>5928.10 (+15.60%)</td><td>995.06 (-17.95%)</td><td>362.26 (-13.49%)</td><td>318.79 (-11.62%)</td><td>333.98 (-16.94%)</td><td>256.53 (-7.45%)</td><td>42.87 <b>(-35.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.80 (n/a)</td><td>5.86 (n/a)</td><td>6.53 (n/a)</td><td>4.50 (n/a)</td><td>1.07 (n/a)</td><td>7747.70 (n/a)</td><td>6130.84 (n/a)</td><td>5340.80 (n/a)</td><td>5128.20 (n/a)</td><td>1212.77 (n/a)</td><td>418.76 (n/a)</td><td>360.70 (n/a)</td><td>402.09 (n/a)</td><td>277.18 (n/a)</td><td>65.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.72 (+8.25%)</td><td>5.24 <b>(+22.76%)</b></td><td>5.55 <b>(+37.43%)</b></td><td>4.47 (+19.26%)</td><td>0.58 (-7.84%)</td><td>7797.20 (-16.15%)</td><td>6729.66 (-18.99%)</td><td>6281.70 <b>(-27.23%)</b></td><td>6097.30 (-7.62%)</td><td>788.71 <b>(-29.46%)</b></td><td>352.20 (+8.25%)</td><td>322.48 <b>(+22.76%)</b></td><td>341.87 <b>(+37.43%)</b></td><td>275.42 (+19.26%)</td><td>35.99 (-7.84%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.28 (n/a)</td><td>4.26 (n/a)</td><td>4.04 (n/a)</td><td>3.75 (n/a)</td><td>0.63 (n/a)</td><td>9299.40 (n/a)</td><td>8307.66 (n/a)</td><td>8632.80 (n/a)</td><td>6600.10 (n/a)</td><td>1118.14 (n/a)</td><td>325.37 (n/a)</td><td>262.68 (n/a)</td><td>248.76 (n/a)</td><td>230.93 (n/a)</td><td>39.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.44 (-5.19%)</td><td>5.29 (-14.55%)</td><td>5.10 (-13.49%)</td><td>4.69 (-17.88%)</td><td>0.68 <b>(+29.67%)</b></td><td>7439.50 <b>(+21.77%)</b></td><td>6668.16 (+17.75%)</td><td>6830.70 (+15.59%)</td><td>5411.70 (+5.47%)</td><td>760.79 <b>(+63.72%)</b></td><td>396.82 (-5.19%)</td><td>325.84 (-14.55%)</td><td>314.39 (-13.49%)</td><td>288.66 (-17.88%)</td><td>41.64 <b>(+29.67%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.80 (n/a)</td><td>6.19 (n/a)</td><td>5.90 (n/a)</td><td>5.71 (n/a)</td><td>0.52 (n/a)</td><td>6109.60 (n/a)</td><td>5663.22 (n/a)</td><td>5909.30 (n/a)</td><td>5130.90 (n/a)</td><td>464.68 (n/a)</td><td>418.54 (n/a)</td><td>381.30 (n/a)</td><td>363.41 (n/a)</td><td>351.49 (n/a)</td><td>32.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.79 (+1.39%)</td><td>0.76 (+0.33%)</td><td>0.76 (-1.47%)</td><td>0.73 (+0.03%)</td><td>0.02 (-1.56%)</td><td>103274.90 (-0.03%)</td><td>99149.72 (-0.33%)</td><td>99133.60 (+1.49%)</td><td>95540.50 (-1.37%)</td><td>2837.47 (-2.80%)</td><td>719.27 (+1.39%)</td><td>693.54 (+0.33%)</td><td>693.20 (-1.47%)</td><td>665.40 (+0.03%)</td><td>19.74 (-1.56%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103310.10 (n/a)</td><td>99478.00 (n/a)</td><td>97677.90 (n/a)</td><td>96871.20 (n/a)</td><td>2919.36 (n/a)</td><td>709.39 (n/a)</td><td>691.27 (n/a)</td><td>703.53 (n/a)</td><td>665.18 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.78 (+2.15%)</td><td>0.76 (+0.96%)</td><td>0.76 (+0.55%)</td><td>0.75 (+1.22%)</td><td>0.01 (+14.68%)</td><td>100911.60 (-1.21%)</td><td>98921.78 (-0.95%)</td><td>98703.40 (-0.55%)</td><td>96434.40 (-2.10%)</td><td>1673.35 (+10.80%)</td><td>712.60 (+2.15%)</td><td>694.85 (+0.96%)</td><td>696.22 (+0.55%)</td><td>680.99 (+1.22%)</td><td>11.83 (+14.68%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>102145.80 (n/a)</td><td>99867.90 (n/a)</td><td>99245.20 (n/a)</td><td>98503.10 (n/a)</td><td>1510.28 (n/a)</td><td>697.64 (n/a)</td><td>688.23 (n/a)</td><td>692.42 (n/a)</td><td>672.76 (n/a)</td><td>10.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.81 (-0.37%)</td><td>0.81 (-0.19%)</td><td>0.80 (-0.37%)</td><td>0.80 (-0.33%)</td><td>0.01 (+18.44%)</td><td>94797.30 (+0.33%)</td><td>93757.62 (+0.19%)</td><td>93882.40 (+0.38%)</td><td>92826.40 (+0.37%)</td><td>904.90 (+19.10%)</td><td>740.30 (-0.37%)</td><td>733.00 (-0.19%)</td><td>731.97 (-0.37%)</td><td>724.91 (-0.33%)</td><td>7.08 (+18.44%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94487.40 (n/a)</td><td>93578.88 (n/a)</td><td>93530.60 (n/a)</td><td>92485.90 (n/a)</td><td>759.79 (n/a)</td><td>743.03 (n/a)</td><td>734.39 (n/a)</td><td>734.73 (n/a)</td><td>727.29 (n/a)</td><td>5.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.60 <b>(+49.41%)</b></td><td>2.31 <b>(+31.56%)</b></td><td>2.05 <b>(+21.35%)</b></td><td>1.87 <b>(+39.05%)</b></td><td>0.73 <b>(+84.84%)</b></td><td>4315.70 <b>(-28.08%)</b></td><td>3704.86 <b>(-22.18%)</b></td><td>3932.00 (-17.59%)</td><td>2238.90 <b>(-33.07%)</b></td><td>850.41 (-10.50%)</td><td>944.19 <b>(+49.41%)</b></td><td>605.52 <b>(+31.56%)</b></td><td>537.62 <b>(+21.35%)</b></td><td>489.82 <b>(+39.05%)</b></td><td>191.58 <b>(+84.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.41 (n/a)</td><td>1.76 (n/a)</td><td>1.69 (n/a)</td><td>1.34 (n/a)</td><td>0.40 (n/a)</td><td>6000.80 (n/a)</td><td>4760.76 (n/a)</td><td>4771.50 (n/a)</td><td>3345.10 (n/a)</td><td>950.14 (n/a)</td><td>631.95 (n/a)</td><td>460.25 (n/a)</td><td>443.03 (n/a)</td><td>352.27 (n/a)</td><td>103.65 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.31 <b>(+44.22%)</b></td><td>0.22 (+14.33%)</td><td>0.22 (+12.77%)</td><td>0.15 (-4.77%)</td><td>0.06 <b>(+211.88%)</b></td><td>8199.40 (+5.01%)</td><td>6150.74 (-7.84%)</td><td>5678.10 (-11.32%)</td><td>4081.40 <b>(-30.66%)</b></td><td>1657.05 <b>(+128.28%)</b></td><td>16.44 <b>(+44.22%)</b></td><td>11.60 (+14.33%)</td><td>11.82 (+12.77%)</td><td>8.18 (-4.77%)</td><td>3.27 <b>(+211.88%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>7807.90 (n/a)</td><td>6674.34 (n/a)</td><td>6402.90 (n/a)</td><td>5885.90 (n/a)</td><td>725.88 (n/a)</td><td>11.40 (n/a)</td><td>10.15 (n/a)</td><td>10.48 (n/a)</td><td>8.59 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.80 (n/a)</td><td>3.53 (n/a)</td><td>3.53 (n/a)</td><td>3.13 (n/a)</td><td>0.28 (n/a)</td><td>3.79 (n/a)</td><td>3.52 (n/a)</td><td>3.53 (n/a)</td><td>3.13 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>7.42 (+5.13%)</td><td>6.80 (+6.07%)</td><td>6.68 (+1.45%)</td><td>5.94 (+8.75%)</td><td>0.62 (+5.66%)</td><td>7.41 (+5.13%)</td><td>6.80 (+6.07%)</td><td>6.68 (+1.45%)</td><td>5.93 (+8.75%)</td><td>0.62 (+5.66%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>7.05 (n/a)</td><td>6.41 (n/a)</td><td>6.59 (n/a)</td><td>5.46 (n/a)</td><td>0.59 (n/a)</td><td>7.05 (n/a)</td><td>6.41 (n/a)</td><td>6.58 (n/a)</td><td>5.46 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>13.75 <b>(+35.13%)</b></td><td>11.32 <b>(+37.47%)</b></td><td>13.32 <b>(+57.13%)</b></td><td>7.65 <b>(+37.41%)</b></td><td>2.99 <b>(+80.11%)</b></td><td>13.75 <b>(+35.13%)</b></td><td>11.31 <b>(+37.47%)</b></td><td>13.32 <b>(+57.13%)</b></td><td>7.65 <b>(+37.41%)</b></td><td>2.99 <b>(+80.11%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>10.18 (n/a)</td><td>8.23 (n/a)</td><td>8.48 (n/a)</td><td>5.57 (n/a)</td><td>1.66 (n/a)</td><td>10.17 (n/a)</td><td>8.23 (n/a)</td><td>8.47 (n/a)</td><td>5.57 (n/a)</td><td>1.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.91 (n/a)</td><td>3.58 (n/a)</td><td>3.61 (n/a)</td><td>3.08 (n/a)</td><td>0.30 (n/a)</td><td>3.91 (n/a)</td><td>3.58 (n/a)</td><td>3.61 (n/a)</td><td>3.08 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.87 (-3.58%)</td><td>5.79 (-7.23%)</td><td>5.72 (-5.70%)</td><td>4.98 (-11.74%)</td><td>0.68 (+13.24%)</td><td>6.87 (-3.58%)</td><td>5.78 (-7.23%)</td><td>5.71 (-5.70%)</td><td>4.98 (-11.74%)</td><td>0.68 (+13.24%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>7.13 (n/a)</td><td>6.24 (n/a)</td><td>6.06 (n/a)</td><td>5.64 (n/a)</td><td>0.60 (n/a)</td><td>7.12 (n/a)</td><td>6.23 (n/a)</td><td>6.06 (n/a)</td><td>5.64 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>13.53 (-2.01%)</td><td>10.07 (-1.34%)</td><td>9.18 (+3.59%)</td><td>7.03 (+1.46%)</td><td>3.19 (+2.25%)</td><td>13.52 (-2.01%)</td><td>10.06 (-1.34%)</td><td>9.17 (+3.59%)</td><td>7.03 (+1.46%)</td><td>3.19 (+2.25%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>13.80 (n/a)</td><td>10.20 (n/a)</td><td>8.86 (n/a)</td><td>6.93 (n/a)</td><td>3.12 (n/a)</td><td>13.79 (n/a)</td><td>10.20 (n/a)</td><td>8.85 (n/a)</td><td>6.93 (n/a)</td><td>3.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.23 (+1.02%)</td><td>2.60 <b>(+39.55%)</b></td><td>3.04 <b>(+164.39%)</b></td><td>1.28 <b>(+23.54%)</b></td><td>0.83 <b>(-21.27%)</b></td><td>3.22 (+1.02%)</td><td>2.60 <b>(+39.55%)</b></td><td>3.03 <b>(+164.39%)</b></td><td>1.28 <b>(+23.54%)</b></td><td>0.83 <b>(-21.27%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.19 (n/a)</td><td>1.86 (n/a)</td><td>1.15 (n/a)</td><td>1.04 (n/a)</td><td>1.06 (n/a)</td><td>3.19 (n/a)</td><td>1.86 (n/a)</td><td>1.15 (n/a)</td><td>1.03 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.57 (-8.92%)</td><td>0.42 (-13.71%)</td><td>0.57 (+7.13%)</td><td>0.08 <b>(-77.78%)</b></td><td>0.22 <b>(+90.65%)</b></td><td>0.56 (-8.92%)</td><td>0.42 (-13.71%)</td><td>0.56 (+7.13%)</td><td>0.08 <b>(-77.78%)</b></td><td>0.22 <b>(+90.65%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.63 (n/a)</td><td>0.49 (n/a)</td><td>0.53 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>0.62 (n/a)</td><td>0.48 (n/a)</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.72 (+7.61%)</td><td>0.46 <b>(-28.46%)</b></td><td>0.47 <b>(-27.54%)</b></td><td>0.08 <b>(-86.67%)</b></td><td>0.27 <b>(+1143.35%)</b></td><td>0.71 (+7.61%)</td><td>0.45 <b>(-28.46%)</b></td><td>0.46 <b>(-27.54%)</b></td><td>0.08 <b>(-86.67%)</b></td><td>0.26 <b>(+1143.35%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.67 (n/a)</td><td>0.64 (n/a)</td><td>0.65 (n/a)</td><td>0.61 (n/a)</td><td>0.02 (n/a)</td><td>0.66 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.60 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.54 (-2.77%)</td><td>1.77 (+2.04%)</td><td>1.94 (-7.42%)</td><td>0.45 <b>(-43.93%)</b></td><td>0.78 (-8.84%)</td><td>2.50 (-2.77%)</td><td>1.74 (+2.04%)</td><td>1.91 (-7.42%)</td><td>0.44 <b>(-43.93%)</b></td><td>0.77 (-8.84%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.62 (n/a)</td><td>1.73 (n/a)</td><td>2.10 (n/a)</td><td>0.80 (n/a)</td><td>0.86 (n/a)</td><td>2.57 (n/a)</td><td>1.71 (n/a)</td><td>2.07 (n/a)</td><td>0.79 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>545.60 (n/a)</td><td>400.20 (n/a)</td><td>471.00 (n/a)</td><td>228.50 (n/a)</td><td>151.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2010.90 (n/a)</td><td>719.20 (n/a)</td><td>426.30 (n/a)</td><td>268.80 (n/a)</td><td>726.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.40 (n/a)</td><td>359.74 (n/a)</td><td>276.30 (n/a)</td><td>191.90 (n/a)</td><td>178.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>742.20 (n/a)</td><td>456.12 (n/a)</td><td>363.00 (n/a)</td><td>229.60 (n/a)</td><td>234.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.90 (n/a)</td><td>432.24 (n/a)</td><td>474.70 (n/a)</td><td>279.00 (n/a)</td><td>90.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.90 (n/a)</td><td>451.52 (n/a)</td><td>481.40 (n/a)</td><td>279.30 (n/a)</td><td>104.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.90 (n/a)</td><td>325.92 (n/a)</td><td>295.00 (n/a)</td><td>249.80 (n/a)</td><td>78.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.50 (n/a)</td><td>305.94 (n/a)</td><td>269.60 (n/a)</td><td>231.30 (n/a)</td><td>99.82 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1896.50 (n/a)</td><td>816.52 (n/a)</td><td>560.80 (n/a)</td><td>494.90 (n/a)</td><td>604.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.30 (n/a)</td><td>435.58 (n/a)</td><td>476.40 (n/a)</td><td>237.00 (n/a)</td><td>145.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1871.80 (n/a)</td><td>702.12 (n/a)</td><td>542.90 (n/a)</td><td>253.50 (n/a)</td><td>669.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.50 (n/a)</td><td>501.30 (n/a)</td><td>542.10 (n/a)</td><td>298.20 (n/a)</td><td>118.43 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.70 (n/a)</td><td>398.98 (n/a)</td><td>257.80 (n/a)</td><td>245.70 (n/a)</td><td>200.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>632.40 (n/a)</td><td>460.40 (n/a)</td><td>550.60 (n/a)</td><td>187.70 (n/a)</td><td>203.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.20 (n/a)</td><td>313.24 (n/a)</td><td>268.70 (n/a)</td><td>250.60 (n/a)</td><td>111.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>495.40 (n/a)</td><td>326.50 (n/a)</td><td>244.60 (n/a)</td><td>236.10 (n/a)</td><td>120.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>543.60 (n/a)</td><td>364.70 (n/a)</td><td>302.30 (n/a)</td><td>242.10 (n/a)</td><td>141.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.10 (n/a)</td><td>376.56 (n/a)</td><td>304.80 (n/a)</td><td>254.70 (n/a)</td><td>128.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>716.80 (n/a)</td><td>511.58 (n/a)</td><td>610.40 (n/a)</td><td>244.40 (n/a)</td><td>216.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>555.10 (n/a)</td><td>437.08 (n/a)</td><td>497.70 (n/a)</td><td>300.10 (n/a)</td><td>120.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.80 (n/a)</td><td>377.86 (n/a)</td><td>359.10 (n/a)</td><td>246.30 (n/a)</td><td>109.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1957.30 (n/a)</td><td>771.50 (n/a)</td><td>558.00 (n/a)</td><td>285.70 (n/a)</td><td>672.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2029.90 (n/a)</td><td>800.04 (n/a)</td><td>627.30 (n/a)</td><td>243.20 (n/a)</td><td>706.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>598.50 (n/a)</td><td>457.94 (n/a)</td><td>494.40 (n/a)</td><td>325.10 (n/a)</td><td>124.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+5.68%)</td><td>0.01 <b>(-21.60%)</b></td><td>0.01 <b>(-22.96%)</b></td><td>0.01 <b>(-53.51%)</b></td><td>0.01 <b>(+285.15%)</b></td><td>630.90 <b>(+115.10%)</b></td><td>375.26 <b>(+47.46%)</b></td><td>316.50 <b>(+29.82%)</b></td><td>226.30 (-5.39%)</td><td>170.97 <b>(+658.20%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>293.30 (n/a)</td><td>254.48 (n/a)</td><td>243.80 (n/a)</td><td>239.20 (n/a)</td><td>22.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(+107.90%)</b></td><td>0.02 <b>(+66.21%)</b></td><td>0.01 <b>(+49.79%)</b></td><td>0.01 <b>(+66.37%)</b></td><td>0.01 <b>(+114.15%)</b></td><td>472.30 <b>(-39.89%)</b></td><td>293.96 <b>(-38.15%)</b></td><td>297.00 <b>(-33.24%)</b></td><td>152.00 <b>(-51.90%)</b></td><td>117.64 <b>(-38.18%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>785.70 (n/a)</td><td>475.26 (n/a)</td><td>444.90 (n/a)</td><td>316.00 (n/a)</td><td>190.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(+49.94%)</b></td><td>0.01 (+13.21%)</td><td>0.01 (+9.50%)</td><td>0.00 <b>(-66.50%)</b></td><td>0.01 <b>(+116.81%)</b></td><td>1940.30 <b>(+198.51%)</b></td><td>609.24 <b>(+59.56%)</b></td><td>274.50 (-8.65%)</td><td>174.40 <b>(-33.28%)</b></td><td>749.50 <b>(+372.10%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>650.00 (n/a)</td><td>381.82 (n/a)</td><td>300.50 (n/a)</td><td>261.40 (n/a)</td><td>158.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(+21.40%)</b></td><td>0.01 <b>(+23.52%)</b></td><td>0.01 (+17.77%)</td><td>0.01 <b>(+26.68%)</b></td><td>0.01 (+12.89%)</td><td>506.90 <b>(-21.07%)</b></td><td>314.02 <b>(-21.17%)</b></td><td>300.50 (-15.09%)</td><td>195.10 (-17.61%)</td><td>128.88 <b>(-27.13%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>642.20 (n/a)</td><td>398.34 (n/a)</td><td>353.90 (n/a)</td><td>236.80 (n/a)</td><td>176.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(+34.63%)</b></td><td>0.01 (-1.06%)</td><td>0.01 <b>(-29.13%)</b></td><td>0.01 (-17.68%)</td><td>0.01 <b>(+114.79%)</b></td><td>564.50 <b>(+21.48%)</b></td><td>415.28 (+13.12%)</td><td>489.60 <b>(+41.10%)</b></td><td>208.90 <b>(-25.71%)</b></td><td>158.46 <b>(+95.19%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.70 (n/a)</td><td>367.12 (n/a)</td><td>347.00 (n/a)</td><td>281.20 (n/a)</td><td>81.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (-16.31%)</td><td>0.01 (+6.62%)</td><td>0.01 (+19.10%)</td><td>0.01 <b>(+24.40%)</b></td><td>0.00 <b>(-34.93%)</b></td><td>538.90 (-19.62%)</td><td>408.20 (-13.21%)</td><td>422.60 (-16.03%)</td><td>255.30 (+19.47%)</td><td>112.08 <b>(-31.93%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.40 (n/a)</td><td>470.32 (n/a)</td><td>503.30 (n/a)</td><td>213.70 (n/a)</td><td>164.65 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 <b>(+43.18%)</b></td><td>0.03 <b>(+28.57%)</b></td><td>0.03 (-13.67%)</td><td>0.03 <b>(+100.85%)</b></td><td>0.01 (-15.05%)</td><td>295.30 <b>(-50.22%)</b></td><td>256.16 <b>(-32.06%)</b></td><td>281.10 (+15.82%)</td><td>164.60 <b>(-30.17%)</b></td><td>55.19 <b>(-70.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.20 (n/a)</td><td>377.02 (n/a)</td><td>242.70 (n/a)</td><td>235.70 (n/a)</td><td>187.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (-17.57%)</td><td>0.02 <b>(-20.54%)</b></td><td>0.03 <b>(-20.12%)</b></td><td>0.02 (-7.98%)</td><td>0.01 (-12.24%)</td><td>459.90 (+8.67%)</td><td>350.36 <b>(+26.09%)</b></td><td>299.70 <b>(+25.19%)</b></td><td>254.10 <b>(+21.35%)</b></td><td>98.87 (+16.50%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>423.20 (n/a)</td><td>277.86 (n/a)</td><td>239.40 (n/a)</td><td>209.40 (n/a)</td><td>84.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (+7.89%)</td><td>0.03 (-10.67%)</td><td>0.03 (-7.65%)</td><td>0.01 (+7.63%)</td><td>0.01 (+6.63%)</td><td>547.60 (-7.09%)</td><td>363.80 (+11.39%)</td><td>300.00 (+8.26%)</td><td>216.60 (-7.28%)</td><td>135.31 (-9.21%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.40 (n/a)</td><td>326.60 (n/a)</td><td>277.10 (n/a)</td><td>233.60 (n/a)</td><td>149.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(-26.31%)</b></td><td>0.02 <b>(-30.51%)</b></td><td>0.02 <b>(-44.89%)</b></td><td>0.01 (-17.55%)</td><td>0.01 <b>(-37.96%)</b></td><td>669.40 <b>(+21.29%)</b></td><td>503.74 <b>(+36.91%)</b></td><td>532.20 <b>(+81.45%)</b></td><td>305.10 <b>(+35.66%)</b></td><td>141.24 (-4.68%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.90 (n/a)</td><td>367.94 (n/a)</td><td>293.30 (n/a)</td><td>224.90 (n/a)</td><td>148.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(-21.93%)</b></td><td>0.02 <b>(-20.70%)</b></td><td>0.02 (-7.53%)</td><td>0.02 (-5.73%)</td><td>0.00 <b>(-48.06%)</b></td><td>524.40 (+6.09%)</td><td>439.50 (+18.36%)</td><td>435.20 (+8.12%)</td><td>302.60 <b>(+28.06%)</b></td><td>91.64 <b>(-26.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.30 (n/a)</td><td>371.32 (n/a)</td><td>402.50 (n/a)</td><td>236.30 (n/a)</td><td>125.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (-7.15%)</td><td>0.02 (+5.62%)</td><td>0.02 (+6.67%)</td><td>0.02 <b>(+28.98%)</b></td><td>0.01 <b>(-30.57%)</b></td><td>467.60 <b>(-22.48%)</b></td><td>385.80 (-11.44%)</td><td>433.50 (-6.25%)</td><td>276.10 (+7.73%)</td><td>90.40 <b>(-41.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.20 (n/a)</td><td>435.64 (n/a)</td><td>462.40 (n/a)</td><td>256.30 (n/a)</td><td>155.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 <b>(+20.95%)</b></td><td>0.02 (-6.60%)</td><td>0.02 (-17.52%)</td><td>0.01 <b>(-47.21%)</b></td><td>0.01 <b>(+38.37%)</b></td><td>1047.60 <b>(+89.41%)</b></td><td>464.22 <b>(+29.27%)</b></td><td>335.80 <b>(+21.27%)</b></td><td>200.60 (-17.35%)</td><td>337.54 <b>(+137.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.10 (n/a)</td><td>359.12 (n/a)</td><td>276.90 (n/a)</td><td>242.70 (n/a)</td><td>142.23 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+18.71%)</td><td>0.02 <b>(+41.73%)</b></td><td>0.02 <b>(+42.94%)</b></td><td>0.02 <b>(+37.10%)</b></td><td>0.01 (+13.75%)</td><td>487.70 <b>(-27.07%)</b></td><td>368.82 <b>(-30.30%)</b></td><td>354.40 <b>(-30.03%)</b></td><td>279.90 (-15.74%)</td><td>91.61 <b>(-31.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>668.70 (n/a)</td><td>529.16 (n/a)</td><td>506.50 (n/a)</td><td>332.20 (n/a)</td><td>133.27 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (+0.41%)</td><td>0.05 (+12.23%)</td><td>0.06 <b>(+52.51%)</b></td><td>0.03 (+1.18%)</td><td>0.01 (-15.81%)</td><td>588.80 (-1.17%)</td><td>353.22 (-13.01%)</td><td>297.20 <b>(-34.44%)</b></td><td>244.20 (-0.41%)</td><td>135.98 (-6.89%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>595.80 (n/a)</td><td>406.04 (n/a)</td><td>453.30 (n/a)</td><td>245.20 (n/a)</td><td>146.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (+4.91%)</td><td>0.04 (-3.55%)</td><td>0.04 (+4.10%)</td><td>0.03 (-9.28%)</td><td>0.01 (-2.79%)</td><td>580.20 (+10.24%)</td><td>433.64 (+3.13%)</td><td>435.10 (-3.93%)</td><td>273.20 (-4.68%)</td><td>110.26 (-3.28%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>526.30 (n/a)</td><td>420.48 (n/a)</td><td>452.90 (n/a)</td><td>286.60 (n/a)</td><td>114.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (-9.61%)</td><td>0.05 (-4.26%)</td><td>0.04 (-16.00%)</td><td>0.03 (+6.89%)</td><td>0.02 (-14.18%)</td><td>585.80 (-6.44%)</td><td>381.94 (+1.20%)</td><td>367.30 (+19.06%)</td><td>251.30 (+10.61%)</td><td>134.97 (-15.23%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>626.10 (n/a)</td><td>377.42 (n/a)</td><td>308.50 (n/a)</td><td>227.20 (n/a)</td><td>159.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (+13.11%)</td><td>0.06 (+11.62%)</td><td>0.06 (+10.75%)</td><td>0.03 (+7.16%)</td><td>0.02 (+8.66%)</td><td>482.70 (-6.69%)</td><td>313.58 (-11.29%)</td><td>266.00 (-9.71%)</td><td>182.90 (-11.60%)</td><td>129.06 (-13.95%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>517.30 (n/a)</td><td>353.48 (n/a)</td><td>294.60 (n/a)</td><td>206.90 (n/a)</td><td>149.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (+7.98%)</td><td>0.04 (-7.80%)</td><td>0.03 <b>(-40.89%)</b></td><td>0.03 (+7.12%)</td><td>0.02 (+14.67%)</td><td>587.50 (-6.64%)</td><td>433.34 (+10.70%)</td><td>508.40 <b>(+69.18%)</b></td><td>236.40 (-7.37%)</td><td>168.69 (+1.26%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>629.30 (n/a)</td><td>391.46 (n/a)</td><td>300.50 (n/a)</td><td>255.20 (n/a)</td><td>166.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (-12.14%)</td><td>0.05 (+2.68%)</td><td>0.05 <b>(+21.85%)</b></td><td>0.03 <b>(+27.97%)</b></td><td>0.01 <b>(-27.83%)</b></td><td>514.10 <b>(-21.86%)</b></td><td>367.72 (-8.83%)</td><td>323.70 (-17.93%)</td><td>242.60 (+13.84%)</td><td>109.90 <b>(-33.83%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>657.90 (n/a)</td><td>403.32 (n/a)</td><td>394.40 (n/a)</td><td>213.10 (n/a)</td><td>166.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (-3.13%)</td><td>0.11 <b>(+29.76%)</b></td><td>0.13 <b>(+50.84%)</b></td><td>0.07 <b>(+31.39%)</b></td><td>0.03 (-12.91%)</td><td>490.30 <b>(-23.89%)</b></td><td>315.44 <b>(-26.72%)</b></td><td>248.00 <b>(-33.71%)</b></td><td>240.30 (+3.22%)</td><td>107.93 <b>(-34.67%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>644.20 (n/a)</td><td>430.48 (n/a)</td><td>374.10 (n/a)</td><td>232.80 (n/a)</td><td>165.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 (+18.84%)</td><td>0.12 (+5.40%)</td><td>0.12 (-1.91%)</td><td>0.07 (+19.81%)</td><td>0.04 <b>(+37.18%)</b></td><td>482.80 (-16.53%)</td><td>316.72 (-3.20%)</td><td>279.00 (+1.94%)</td><td>199.20 (-15.84%)</td><td>125.61 (-11.33%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>578.40 (n/a)</td><td>327.18 (n/a)</td><td>273.70 (n/a)</td><td>236.70 (n/a)</td><td>141.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 <b>(-38.60%)</b></td><td>0.11 (-12.91%)</td><td>0.12 (+4.89%)</td><td>0.08 (+5.80%)</td><td>0.02 <b>(-57.06%)</b></td><td>399.20 (-5.49%)</td><td>299.48 (+5.87%)</td><td>274.10 (-4.69%)</td><td>233.50 <b>(+62.94%)</b></td><td>69.84 <b>(-29.55%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>422.40 (n/a)</td><td>282.88 (n/a)</td><td>287.60 (n/a)</td><td>143.30 (n/a)</td><td>99.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (+13.05%)</td><td>0.11 (+16.16%)</td><td>0.11 <b>(+31.56%)</b></td><td>0.06 (-9.38%)</td><td>0.04 <b>(+55.99%)</b></td><td>508.80 (+10.34%)</td><td>350.58 (-6.93%)</td><td>292.40 <b>(-23.99%)</b></td><td>212.60 (-11.53%)</td><td>141.38 <b>(+70.40%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>461.10 (n/a)</td><td>376.68 (n/a)</td><td>384.70 (n/a)</td><td>240.30 (n/a)</td><td>82.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 <b>(+49.37%)</b></td><td>0.07 (+1.50%)</td><td>0.07 (-4.57%)</td><td>0.04 (-8.03%)</td><td>0.04 <b>(+106.74%)</b></td><td>766.50 (+8.74%)</td><td>533.16 (+9.66%)</td><td>479.90 (+4.80%)</td><td>250.50 <b>(-33.06%)</b></td><td>214.41 <b>(+57.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>704.90 (n/a)</td><td>486.18 (n/a)</td><td>457.90 (n/a)</td><td>374.20 (n/a)</td><td>135.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (-5.98%)</td><td>0.01 (-12.02%)</td><td>0.01 <b>(-28.54%)</b></td><td>0.01 (+9.27%)</td><td>0.00 <b>(-20.15%)</b></td><td>512.00 (-8.47%)</td><td>418.96 (+8.97%)</td><td>436.70 <b>(+39.92%)</b></td><td>256.80 (+6.34%)</td><td>95.93 <b>(-30.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.40 (n/a)</td><td>384.46 (n/a)</td><td>312.10 (n/a)</td><td>241.50 (n/a)</td><td>137.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-22.45%)</b></td><td>0.01 (-12.39%)</td><td>0.01 (-19.60%)</td><td>0.01 (+0.66%)</td><td>0.00 <b>(-43.14%)</b></td><td>486.50 (-0.65%)</td><td>351.84 (+9.05%)</td><td>337.10 <b>(+24.39%)</b></td><td>293.80 <b>(+28.97%)</b></td><td>79.20 <b>(-27.17%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.70 (n/a)</td><td>322.64 (n/a)</td><td>271.00 (n/a)</td><td>227.80 (n/a)</td><td>108.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-31.49%)</b></td><td>0.01 (-8.39%)</td><td>0.01 (+9.92%)</td><td>0.01 <b>(+28.98%)</b></td><td>0.00 <b>(-69.69%)</b></td><td>534.40 <b>(-22.46%)</b></td><td>443.80 (-0.83%)</td><td>434.20 (-9.01%)</td><td>391.20 <b>(+45.97%)</b></td><td>57.55 <b>(-64.97%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>689.20 (n/a)</td><td>447.52 (n/a)</td><td>477.20 (n/a)</td><td>268.00 (n/a)</td><td>164.27 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+7.10%)</td><td>0.01 (+4.94%)</td><td>0.01 (+0.48%)</td><td>0.01 (-14.50%)</td><td>0.00 (+7.14%)</td><td>590.60 (+16.95%)</td><td>348.96 (-2.64%)</td><td>290.80 (-0.48%)</td><td>249.30 (-6.63%)</td><td>137.83 <b>(+25.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.00 (n/a)</td><td>358.42 (n/a)</td><td>292.20 (n/a)</td><td>267.00 (n/a)</td><td>109.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+10.63%)</td><td>0.01 (+7.58%)</td><td>0.01 <b>(+53.72%)</b></td><td>0.01 (-19.06%)</td><td>0.00 <b>(+38.14%)</b></td><td>645.00 <b>(+23.54%)</b></td><td>412.86 (+1.80%)</td><td>280.40 <b>(-34.94%)</b></td><td>248.40 (-9.61%)</td><td>197.18 <b>(+62.52%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.10 (n/a)</td><td>405.56 (n/a)</td><td>431.00 (n/a)</td><td>274.80 (n/a)</td><td>121.33 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+6.78%)</td><td>0.01 (+5.74%)</td><td>0.02 <b>(+23.84%)</b></td><td>0.01 (-17.69%)</td><td>0.00 <b>(+67.40%)</b></td><td>498.00 <b>(+21.49%)</b></td><td>320.82 (+0.92%)</td><td>241.60 (-19.25%)</td><td>229.30 (-6.37%)</td><td>120.02 <b>(+83.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>409.90 (n/a)</td><td>317.90 (n/a)</td><td>299.20 (n/a)</td><td>244.90 (n/a)</td><td>65.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (-12.50%)</td><td>0.01 (+3.08%)</td><td>0.01 (+0.65%)</td><td>0.01 <b>(+88.34%)</b></td><td>0.00 <b>(-30.07%)</b></td><td>597.90 <b>(-46.90%)</b></td><td>392.62 <b>(-21.69%)</b></td><td>296.00 (-0.64%)</td><td>274.00 (+14.31%)</td><td>153.85 <b>(-58.73%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1126.00 (n/a)</td><td>501.38 (n/a)</td><td>297.90 (n/a)</td><td>239.70 (n/a)</td><td>372.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (-7.68%)</td><td>0.01 <b>(-21.28%)</b></td><td>0.01 <b>(-27.51%)</b></td><td>0.01 <b>(-20.66%)</b></td><td>0.00 (-3.79%)</td><td>632.70 <b>(+26.06%)</b></td><td>489.40 <b>(+28.31%)</b></td><td>483.10 <b>(+37.99%)</b></td><td>324.20 (+8.32%)</td><td>117.78 <b>(+30.97%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.90 (n/a)</td><td>381.42 (n/a)</td><td>350.10 (n/a)</td><td>299.30 (n/a)</td><td>89.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (-16.36%)</td><td>0.01 (-10.79%)</td><td>0.01 (-10.89%)</td><td>0.01 (-9.44%)</td><td>0.00 <b>(-21.86%)</b></td><td>599.30 (+10.43%)</td><td>476.52 (+10.31%)</td><td>491.30 (+12.22%)</td><td>278.30 (+19.54%)</td><td>132.62 (+5.14%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>542.70 (n/a)</td><td>432.00 (n/a)</td><td>437.80 (n/a)</td><td>232.80 (n/a)</td><td>126.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+12.52%)</td><td>0.01 (-1.55%)</td><td>0.01 (-12.00%)</td><td>0.01 (-10.87%)</td><td>0.00 <b>(+39.32%)</b></td><td>546.40 (+12.20%)</td><td>414.26 (+6.64%)</td><td>482.80 (+13.63%)</td><td>246.00 (-11.13%)</td><td>135.08 <b>(+41.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.00 (n/a)</td><td>388.46 (n/a)</td><td>424.90 (n/a)</td><td>276.80 (n/a)</td><td>95.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (+0.32%)</td><td>0.01 <b>(+33.00%)</b></td><td>0.01 (+10.33%)</td><td>0.01 <b>(+321.49%)</b></td><td>0.00 <b>(-27.23%)</b></td><td>531.10 <b>(-76.28%)</b></td><td>413.92 <b>(-49.26%)</b></td><td>466.10 (-9.35%)</td><td>289.40 (-0.34%)</td><td>114.04 <b>(-85.78%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2238.60 (n/a)</td><td>815.72 (n/a)</td><td>514.20 (n/a)</td><td>290.40 (n/a)</td><td>801.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(+21.23%)</b></td><td>0.01 <b>(+20.45%)</b></td><td>0.01 (+15.37%)</td><td>0.01 (+13.89%)</td><td>0.00 <b>(+31.05%)</b></td><td>514.30 (-12.19%)</td><td>400.86 (-16.20%)</td><td>414.80 (-13.33%)</td><td>273.20 (-17.51%)</td><td>95.17 (-5.50%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.70 (n/a)</td><td>478.34 (n/a)</td><td>478.60 (n/a)</td><td>331.20 (n/a)</td><td>100.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (+15.01%)</td><td>0.02 (-5.67%)</td><td>0.02 <b>(-38.67%)</b></td><td>0.02 (+5.93%)</td><td>0.01 <b>(+38.27%)</b></td><td>534.40 (-5.60%)</td><td>401.96 (+11.86%)</td><td>482.70 <b>(+63.07%)</b></td><td>209.00 (-13.03%)</td><td>152.62 (+15.37%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.10 (n/a)</td><td>359.34 (n/a)</td><td>296.00 (n/a)</td><td>240.30 (n/a)</td><td>132.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (+2.01%)</td><td>0.02 (-14.91%)</td><td>0.02 <b>(-40.83%)</b></td><td>0.02 (+13.41%)</td><td>0.01 (+1.44%)</td><td>523.30 (-11.83%)</td><td>414.56 (+16.35%)</td><td>492.40 <b>(+69.04%)</b></td><td>232.40 (-1.94%)</td><td>127.22 (-12.25%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.50 (n/a)</td><td>356.30 (n/a)</td><td>291.30 (n/a)</td><td>237.00 (n/a)</td><td>144.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(-39.38%)</b></td><td>0.02 <b>(-43.67%)</b></td><td>0.02 <b>(-54.12%)</b></td><td>0.01 <b>(-34.27%)</b></td><td>0.00 <b>(-43.48%)</b></td><td>645.40 <b>(+52.15%)</b></td><td>498.58 <b>(+75.43%)</b></td><td>524.80 <b>(+117.94%)</b></td><td>387.10 <b>(+64.93%)</b></td><td>110.10 <b>(+35.57%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>424.20 (n/a)</td><td>284.20 (n/a)</td><td>240.80 (n/a)</td><td>234.70 (n/a)</td><td>81.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (-2.93%)</td><td>0.03 (+10.33%)</td><td>0.03 (+0.04%)</td><td>0.02 <b>(+72.09%)</b></td><td>0.01 <b>(-40.19%)</b></td><td>436.30 <b>(-41.89%)</b></td><td>303.46 <b>(-20.35%)</b></td><td>284.00 (-0.07%)</td><td>247.90 (+3.03%)</td><td>75.85 <b>(-64.24%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>750.80 (n/a)</td><td>381.00 (n/a)</td><td>284.20 (n/a)</td><td>240.60 (n/a)</td><td>212.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+18.38%)</td><td>0.02 (-5.78%)</td><td>0.02 <b>(-34.04%)</b></td><td>0.01 <b>(-20.36%)</b></td><td>0.01 <b>(+68.27%)</b></td><td>782.20 <b>(+25.55%)</b></td><td>483.08 <b>(+22.78%)</b></td><td>500.40 <b>(+51.59%)</b></td><td>238.20 (-15.53%)</td><td>242.66 <b>(+67.75%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.00 (n/a)</td><td>393.44 (n/a)</td><td>330.10 (n/a)</td><td>282.00 (n/a)</td><td>144.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (+9.85%)</td><td>0.03 (+12.06%)</td><td>0.03 (+14.54%)</td><td>0.02 (-2.24%)</td><td>0.01 <b>(+20.99%)</b></td><td>472.80 (+2.29%)</td><td>305.30 (-9.06%)</td><td>278.60 (-12.69%)</td><td>221.10 (-8.97%)</td><td>97.13 (+18.35%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.20 (n/a)</td><td>335.72 (n/a)</td><td>319.10 (n/a)</td><td>242.90 (n/a)</td><td>82.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (-6.84%)</td><td>0.02 (-5.51%)</td><td>0.02 <b>(-24.22%)</b></td><td>0.01 <b>(+304.83%)</b></td><td>0.01 <b>(-38.19%)</b></td><td>597.20 <b>(-75.30%)</b></td><td>464.60 <b>(-40.67%)</b></td><td>498.70 <b>(+31.97%)</b></td><td>250.10 (+7.34%)</td><td>130.77 <b>(-85.85%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2417.80 (n/a)</td><td>783.02 (n/a)</td><td>377.90 (n/a)</td><td>233.00 (n/a)</td><td>924.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+3.11%)</td><td>0.02 (+13.24%)</td><td>0.02 (-2.96%)</td><td>0.02 <b>(+65.54%)</b></td><td>0.01 (-16.57%)</td><td>477.60 <b>(-39.58%)</b></td><td>384.50 (-18.07%)</td><td>411.20 (+3.06%)</td><td>270.90 (-3.01%)</td><td>98.76 <b>(-51.66%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>790.50 (n/a)</td><td>469.30 (n/a)</td><td>399.00 (n/a)</td><td>279.30 (n/a)</td><td>204.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (-8.64%)</td><td>0.02 (+0.92%)</td><td>0.02 (+19.53%)</td><td>0.01 (-8.57%)</td><td>0.01 (-13.98%)</td><td>625.90 (+9.37%)</td><td>407.12 (-4.16%)</td><td>442.10 (-16.35%)</td><td>205.70 (+9.47%)</td><td>168.00 (-4.10%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.30 (n/a)</td><td>424.78 (n/a)</td><td>528.50 (n/a)</td><td>187.90 (n/a)</td><td>175.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 <b>(+48.09%)</b></td><td>0.03 (+11.86%)</td><td>0.03 (+7.59%)</td><td>0.00 <b>(-72.83%)</b></td><td>0.02 <b>(+196.06%)</b></td><td>1911.60 <b>(+268.04%)</b></td><td>631.72 <b>(+75.04%)</b></td><td>285.40 (-7.04%)</td><td>180.90 <b>(-32.47%)</b></td><td>733.99 <b>(+613.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.40 (n/a)</td><td>360.90 (n/a)</td><td>307.00 (n/a)</td><td>267.90 (n/a)</td><td>102.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(+45.11%)</b></td><td>0.02 (+19.94%)</td><td>0.02 (-4.84%)</td><td>0.01 (-18.78%)</td><td>0.01 <b>(+227.78%)</b></td><td>652.60 <b>(+23.13%)</b></td><td>439.04 (-4.27%)</td><td>501.30 (+5.09%)</td><td>247.30 <b>(-31.10%)</b></td><td>180.35 <b>(+156.73%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>530.00 (n/a)</td><td>458.60 (n/a)</td><td>477.00 (n/a)</td><td>358.90 (n/a)</td><td>70.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+1.01%)</td><td>0.02 (-18.37%)</td><td>0.01 <b>(-41.66%)</b></td><td>0.01 <b>(-43.67%)</b></td><td>0.01 <b>(+64.79%)</b></td><td>1029.50 <b>(+77.53%)</b></td><td>544.08 <b>(+49.44%)</b></td><td>548.30 <b>(+71.40%)</b></td><td>250.50 (-1.03%)</td><td>317.82 <b>(+150.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.90 (n/a)</td><td>364.08 (n/a)</td><td>319.90 (n/a)</td><td>253.10 (n/a)</td><td>126.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (+10.77%)</td><td>0.05 <b>(+25.66%)</b></td><td>0.05 <b>(+34.63%)</b></td><td>0.03 <b>(+299.06%)</b></td><td>0.02 <b>(-24.26%)</b></td><td>478.60 <b>(-74.94%)</b></td><td>337.74 <b>(-49.11%)</b></td><td>298.50 <b>(-25.71%)</b></td><td>204.20 (-9.73%)</td><td>112.10 <b>(-84.08%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1909.70 (n/a)</td><td>663.66 (n/a)</td><td>401.80 (n/a)</td><td>226.20 (n/a)</td><td>703.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 <b>(+22.58%)</b></td><td>0.05 (-2.37%)</td><td>0.05 (-10.49%)</td><td>0.03 (+10.20%)</td><td>0.02 <b>(+43.26%)</b></td><td>489.10 (-9.26%)</td><td>341.46 (+6.14%)</td><td>307.60 (+11.73%)</td><td>198.20 (-18.44%)</td><td>127.43 (+4.16%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.00 (n/a)</td><td>321.72 (n/a)</td><td>275.30 (n/a)</td><td>243.00 (n/a)</td><td>122.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (+5.29%)</td><td>0.05 (+15.26%)</td><td>0.04 <b>(+25.46%)</b></td><td>0.04 <b>(+21.60%)</b></td><td>0.02 (-4.78%)</td><td>458.90 (-17.77%)</td><td>343.50 (-17.08%)</td><td>389.40 <b>(-20.29%)</b></td><td>217.60 (-5.02%)</td><td>114.53 <b>(-28.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.10 (n/a)</td><td>414.26 (n/a)</td><td>488.50 (n/a)</td><td>229.10 (n/a)</td><td>160.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (-16.46%)</td><td>0.04 <b>(-23.93%)</b></td><td>0.03 <b>(-32.72%)</b></td><td>0.03 <b>(-24.06%)</b></td><td>0.01 (-7.08%)</td><td>578.00 <b>(+31.69%)</b></td><td>465.24 <b>(+33.53%)</b></td><td>492.60 <b>(+48.64%)</b></td><td>293.80 (+19.72%)</td><td>121.10 <b>(+43.18%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>438.90 (n/a)</td><td>348.42 (n/a)</td><td>331.40 (n/a)</td><td>245.40 (n/a)</td><td>84.58 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 <b>(-21.29%)</b></td><td>0.04 <b>(-37.40%)</b></td><td>0.04 <b>(-28.52%)</b></td><td>0.01 <b>(-80.96%)</b></td><td>0.02 <b>(+104.00%)</b></td><td>1989.20 <b>(+425.13%)</b></td><td>724.44 <b>(+142.77%)</b></td><td>400.80 <b>(+39.90%)</b></td><td>314.10 <b>(+27.01%)</b></td><td>712.08 <b>(+1359.38%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>378.80 (n/a)</td><td>298.40 (n/a)</td><td>286.50 (n/a)</td><td>247.30 (n/a)</td><td>48.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (-19.58%)</td><td>0.04 <b>(-30.74%)</b></td><td>0.04 <b>(-37.34%)</b></td><td>0.03 <b>(-48.50%)</b></td><td>0.01 <b>(+98.58%)</b></td><td>605.40 <b>(+94.16%)</b></td><td>432.24 <b>(+56.44%)</b></td><td>434.70 <b>(+59.58%)</b></td><td>287.10 <b>(+24.34%)</b></td><td>141.70 <b>(+364.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>311.80 (n/a)</td><td>276.30 (n/a)</td><td>272.40 (n/a)</td><td>230.90 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 <b>(+26.24%)</b></td><td>0.05 (+19.51%)</td><td>0.06 <b>(+25.52%)</b></td><td>0.03 (+6.95%)</td><td>0.02 <b>(+36.23%)</b></td><td>513.80 (-6.50%)</td><td>336.20 (-13.99%)</td><td>276.80 <b>(-20.32%)</b></td><td>218.80 <b>(-20.78%)</b></td><td>125.23 (+2.50%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.50 (n/a)</td><td>390.88 (n/a)</td><td>347.40 (n/a)</td><td>276.20 (n/a)</td><td>122.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (-9.27%)</td><td>0.04 (-7.45%)</td><td>0.04 <b>(-26.12%)</b></td><td>0.03 (+19.49%)</td><td>0.02 (-12.00%)</td><td>542.70 (-16.31%)</td><td>405.14 (+4.11%)</td><td>434.40 <b>(+35.33%)</b></td><td>253.00 (+10.19%)</td><td>135.63 <b>(-20.63%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>648.50 (n/a)</td><td>389.14 (n/a)</td><td>321.00 (n/a)</td><td>229.60 (n/a)</td><td>170.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (+11.76%)</td><td>0.04 (-7.94%)</td><td>0.03 (-2.56%)</td><td>0.02 <b>(-29.99%)</b></td><td>0.02 <b>(+36.26%)</b></td><td>781.40 <b>(+42.85%)</b></td><td>502.78 (+16.91%)</td><td>501.90 (+2.62%)</td><td>236.20 (-10.53%)</td><td>193.16 <b>(+62.20%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>547.00 (n/a)</td><td>430.04 (n/a)</td><td>489.10 (n/a)</td><td>264.00 (n/a)</td><td>119.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(-22.06%)</b></td><td>0.05 (-3.43%)</td><td>0.06 <b>(+55.66%)</b></td><td>0.03 (+3.84%)</td><td>0.01 <b>(-41.56%)</b></td><td>553.40 (-3.71%)</td><td>366.48 (-4.97%)</td><td>292.40 <b>(-35.76%)</b></td><td>276.70 <b>(+28.34%)</b></td><td>121.24 <b>(-23.83%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.70 (n/a)</td><td>385.64 (n/a)</td><td>455.20 (n/a)</td><td>215.60 (n/a)</td><td>159.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 <b>(-38.71%)</b></td><td>0.03 (-17.94%)</td><td>0.03 (-5.04%)</td><td>0.03 (-6.82%)</td><td>0.00 <b>(-73.22%)</b></td><td>524.10 (+7.31%)</td><td>475.46 (+15.17%)</td><td>481.10 (+5.32%)</td><td>401.50 <b>(+63.15%)</b></td><td>47.31 <b>(-52.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>488.40 (n/a)</td><td>412.82 (n/a)</td><td>456.80 (n/a)</td><td>246.10 (n/a)</td><td>99.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (-0.43%)</td><td>0.05 (-4.35%)</td><td>0.05 (-10.61%)</td><td>0.03 (+0.98%)</td><td>0.01 (-5.33%)</td><td>499.70 (-0.95%)</td><td>376.98 (+3.98%)</td><td>339.10 (+11.88%)</td><td>269.40 (+0.45%)</td><td>104.89 (-3.06%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>504.50 (n/a)</td><td>362.56 (n/a)</td><td>303.10 (n/a)</td><td>268.20 (n/a)</td><td>108.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+14.77%)</td><td>0.11 <b>(+31.09%)</b></td><td>0.11 <b>(+64.36%)</b></td><td>0.08 <b>(+34.90%)</b></td><td>0.02 (-13.80%)</td><td>432.50 <b>(-25.87%)</b></td><td>318.58 <b>(-26.59%)</b></td><td>297.90 <b>(-39.17%)</b></td><td>242.40 (-12.87%)</td><td>73.59 <b>(-42.24%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>583.40 (n/a)</td><td>433.96 (n/a)</td><td>489.70 (n/a)</td><td>278.20 (n/a)</td><td>127.39 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+14.09%)</td><td>0.12 <b>(+24.77%)</b></td><td>0.12 <b>(+40.36%)</b></td><td>0.07 (-5.60%)</td><td>0.03 <b>(+28.41%)</b></td><td>472.90 (+5.91%)</td><td>300.82 (-17.98%)</td><td>271.80 <b>(-28.75%)</b></td><td>231.80 (-12.36%)</td><td>97.63 <b>(+25.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>446.50 (n/a)</td><td>366.76 (n/a)</td><td>381.50 (n/a)</td><td>264.50 (n/a)</td><td>77.94 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+6.08%)</td><td>0.09 (-8.35%)</td><td>0.06 <b>(-50.23%)</b></td><td>0.06 <b>(+63.49%)</b></td><td>0.04 (-19.38%)</td><td>579.30 <b>(-38.83%)</b></td><td>442.72 (-7.75%)</td><td>546.80 <b>(+100.96%)</b></td><td>231.90 (-5.73%)</td><td>163.55 <b>(-48.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>947.10 (n/a)</td><td>479.92 (n/a)</td><td>272.10 (n/a)</td><td>246.00 (n/a)</td><td>318.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (-11.75%)</td><td>0.08 (-5.01%)</td><td>0.08 <b>(+23.03%)</b></td><td>0.02 <b>(-69.69%)</b></td><td>0.04 <b>(+33.84%)</b></td><td>1879.70 <b>(+229.89%)</b></td><td>689.40 <b>(+56.31%)</b></td><td>394.40 (-18.71%)</td><td>272.90 (+13.28%)</td><td>678.86 <b>(+427.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>569.80 (n/a)</td><td>441.06 (n/a)</td><td>485.20 (n/a)</td><td>240.90 (n/a)</td><td>128.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (-2.37%)</td><td>0.08 <b>(-26.47%)</b></td><td>0.06 <b>(-47.03%)</b></td><td>0.02 <b>(-75.18%)</b></td><td>0.05 <b>(+66.19%)</b></td><td>2108.50 <b>(+302.85%)</b></td><td>723.98 <b>(+128.85%)</b></td><td>509.80 <b>(+88.81%)</b></td><td>237.40 (+2.42%)</td><td>786.08 <b>(+555.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>523.40 (n/a)</td><td>316.36 (n/a)</td><td>270.00 (n/a)</td><td>231.80 (n/a)</td><td>120.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+5.00%)</td><td>0.10 (+6.14%)</td><td>0.11 (+15.55%)</td><td>0.07 (+10.22%)</td><td>0.03 (-3.14%)</td><td>464.40 (-9.28%)</td><td>343.82 (-6.95%)</td><td>311.60 (-13.44%)</td><td>232.60 (-4.79%)</td><td>102.27 (-12.71%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>511.90 (n/a)</td><td>369.50 (n/a)</td><td>360.00 (n/a)</td><td>244.30 (n/a)</td><td>117.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (+16.75%)</td><td>0.12 <b>(+38.19%)</b></td><td>0.13 <b>(+101.75%)</b></td><td>0.05 <b>(-21.37%)</b></td><td>0.04 <b>(+33.01%)</b></td><td>666.70 <b>(+27.18%)</b></td><td>326.48 <b>(-21.58%)</b></td><td>246.10 <b>(-50.43%)</b></td><td>225.30 (-14.33%)</td><td>190.42 <b>(+51.40%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>524.20 (n/a)</td><td>416.30 (n/a)</td><td>496.50 (n/a)</td><td>263.00 (n/a)</td><td>125.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (-2.07%)</td><td>0.08 (-11.16%)</td><td>0.07 (-3.71%)</td><td>0.05 (+0.71%)</td><td>0.03 (-12.59%)</td><td>647.50 (-0.71%)</td><td>458.48 (+9.47%)</td><td>448.30 (+3.85%)</td><td>249.10 (+2.13%)</td><td>151.54 (-9.58%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>652.10 (n/a)</td><td>418.80 (n/a)</td><td>431.70 (n/a)</td><td>243.90 (n/a)</td><td>167.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (-2.80%)</td><td>0.09 <b>(+50.53%)</b></td><td>0.07 <b>(+22.33%)</b></td><td>0.07 <b>(+372.74%)</b></td><td>0.03 <b>(-47.08%)</b></td><td>447.80 <b>(-78.84%)</b></td><td>392.86 <b>(-63.32%)</b></td><td>445.90 (-18.26%)</td><td>244.30 (+2.86%)</td><td>88.04 <b>(-89.99%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2116.70 (n/a)</td><td>1070.94 (n/a)</td><td>545.50 (n/a)</td><td>237.50 (n/a)</td><td>879.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (-8.42%)</td><td>0.10 (+2.17%)</td><td>0.11 <b>(+34.67%)</b></td><td>0.07 (+2.10%)</td><td>0.03 (-15.54%)</td><td>490.90 (-2.06%)</td><td>361.88 (-3.65%)</td><td>301.20 <b>(-25.76%)</b></td><td>274.40 (+9.19%)</td><td>105.98 (-6.11%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.20 (n/a)</td><td>375.58 (n/a)</td><td>405.70 (n/a)</td><td>251.30 (n/a)</td><td>112.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (-13.29%)</td><td>0.07 <b>(-22.30%)</b></td><td>0.06 <b>(-21.26%)</b></td><td>0.04 <b>(-32.85%)</b></td><td>0.03 (-0.33%)</td><td>793.50 <b>(+48.93%)</b></td><td>558.10 <b>(+35.47%)</b></td><td>545.80 <b>(+26.99%)</b></td><td>261.60 (+15.34%)</td><td>195.59 <b>(+66.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>532.80 (n/a)</td><td>411.96 (n/a)</td><td>429.80 (n/a)</td><td>226.80 (n/a)</td><td>117.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (-14.00%)</td><td>0.08 (-6.31%)</td><td>0.07 <b>(-34.16%)</b></td><td>0.06 <b>(+87.74%)</b></td><td>0.02 <b>(-37.58%)</b></td><td>575.20 <b>(-46.74%)</b></td><td>440.20 (-11.49%)</td><td>497.40 <b>(+51.88%)</b></td><td>313.10 (+16.26%)</td><td>118.77 <b>(-64.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1079.90 (n/a)</td><td>497.34 (n/a)</td><td>327.50 (n/a)</td><td>269.30 (n/a)</td><td>337.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (-12.05%)</td><td>0.01 <b>(-22.18%)</b></td><td>0.01 (-8.43%)</td><td>0.01 <b>(-35.54%)</b></td><td>0.00 (+19.38%)</td><td>786.70 <b>(+55.14%)</b></td><td>429.52 <b>(+41.77%)</b></td><td>292.20 (+9.19%)</td><td>259.00 (+13.70%)</td><td>226.14 <b>(+95.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.10 (n/a)</td><td>302.96 (n/a)</td><td>267.60 (n/a)</td><td>227.80 (n/a)</td><td>115.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+4.76%)</td><td>0.02 <b>(+44.22%)</b></td><td>0.02 <b>(+78.39%)</b></td><td>0.01 <b>(+36.21%)</b></td><td>0.00 <b>(-25.01%)</b></td><td>434.00 <b>(-26.58%)</b></td><td>307.40 <b>(-33.79%)</b></td><td>286.10 <b>(-43.95%)</b></td><td>248.40 (-4.53%)</td><td>73.30 <b>(-42.58%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.10 (n/a)</td><td>464.30 (n/a)</td><td>510.40 (n/a)</td><td>260.20 (n/a)</td><td>127.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-47.82%)</b></td><td>0.01 <b>(-41.53%)</b></td><td>0.01 <b>(-32.59%)</b></td><td>0.01 <b>(-27.60%)</b></td><td>0.00 <b>(-62.24%)</b></td><td>718.90 <b>(+38.12%)</b></td><td>559.02 <b>(+58.13%)</b></td><td>512.50 <b>(+48.38%)</b></td><td>398.10 <b>(+91.67%)</b></td><td>151.13 (+7.26%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>520.50 (n/a)</td><td>353.52 (n/a)</td><td>345.40 (n/a)</td><td>207.70 (n/a)</td><td>140.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-41.24%)</b></td><td>0.01 <b>(-31.24%)</b></td><td>0.01 (-16.79%)</td><td>0.00 <b>(-47.26%)</b></td><td>0.00 <b>(-39.57%)</b></td><td>1084.30 <b>(+89.60%)</b></td><td>596.36 <b>(+48.93%)</b></td><td>506.90 <b>(+20.18%)</b></td><td>435.40 <b>(+70.14%)</b></td><td>275.38 <b>(+109.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.90 (n/a)</td><td>400.44 (n/a)</td><td>421.80 (n/a)</td><td>255.90 (n/a)</td><td>131.33 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+11.63%)</td><td>0.01 (+18.89%)</td><td>0.01 <b>(+51.39%)</b></td><td>0.01 (-11.36%)</td><td>0.00 <b>(+47.39%)</b></td><td>723.80 (+12.81%)</td><td>420.92 (-7.39%)</td><td>294.30 <b>(-33.95%)</b></td><td>242.90 (-10.44%)</td><td>208.00 <b>(+56.56%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.60 (n/a)</td><td>454.50 (n/a)</td><td>445.60 (n/a)</td><td>271.20 (n/a)</td><td>132.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(+53.27%)</b></td><td>0.01 (+15.89%)</td><td>0.01 (+3.80%)</td><td>0.01 (-0.22%)</td><td>0.01 <b>(+100.01%)</b></td><td>604.30 (+0.22%)</td><td>462.82 (-2.52%)</td><td>527.10 (-3.66%)</td><td>171.10 <b>(-34.77%)</b></td><td>170.90 <b>(+23.72%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.00 (n/a)</td><td>474.80 (n/a)</td><td>547.10 (n/a)</td><td>262.30 (n/a)</td><td>138.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-20.76%)</b></td><td>0.01 (-16.10%)</td><td>0.01 <b>(-29.13%)</b></td><td>0.01 (+8.24%)</td><td>0.00 <b>(-47.96%)</b></td><td>518.00 (-7.62%)</td><td>386.28 (+9.25%)</td><td>358.50 <b>(+41.14%)</b></td><td>303.40 <b>(+26.21%)</b></td><td>93.20 <b>(-38.27%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>560.70 (n/a)</td><td>353.56 (n/a)</td><td>254.00 (n/a)</td><td>240.40 (n/a)</td><td>151.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (-9.14%)</td><td>0.01 (+6.44%)</td><td>0.01 <b>(+34.92%)</b></td><td>0.01 (-4.91%)</td><td>0.00 (-11.00%)</td><td>641.20 (+5.15%)</td><td>466.18 (-6.20%)</td><td>417.10 <b>(-25.89%)</b></td><td>310.90 (+10.05%)</td><td>144.49 (+10.17%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.80 (n/a)</td><td>497.00 (n/a)</td><td>562.80 (n/a)</td><td>282.50 (n/a)</td><td>131.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (+9.52%)</td><td>0.01 (-14.03%)</td><td>0.01 (-15.00%)</td><td>0.00 <b>(-48.05%)</b></td><td>0.00 <b>(+57.28%)</b></td><td>1036.10 <b>(+92.48%)</b></td><td>588.60 <b>(+35.54%)</b></td><td>548.70 (+17.67%)</td><td>243.30 (-8.71%)</td><td>285.04 <b>(+179.54%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.30 (n/a)</td><td>434.26 (n/a)</td><td>466.30 (n/a)</td><td>266.50 (n/a)</td><td>101.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(+22.92%)</b></td><td>0.01 (-2.47%)</td><td>0.01 (-18.36%)</td><td>0.01 (-1.95%)</td><td>0.00 <b>(+63.21%)</b></td><td>520.40 (+1.98%)</td><td>433.34 (+7.42%)</td><td>493.20 <b>(+22.47%)</b></td><td>237.80 (-18.65%)</td><td>119.71 <b>(+34.21%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.30 (n/a)</td><td>403.42 (n/a)</td><td>402.70 (n/a)</td><td>292.30 (n/a)</td><td>89.19 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 <b>(-21.45%)</b></td><td>0.01 (-18.71%)</td><td>0.01 (-12.19%)</td><td>0.00 <b>(-38.81%)</b></td><td>0.00 (-5.49%)</td><td>1033.90 <b>(+63.44%)</b></td><td>628.14 <b>(+27.79%)</b></td><td>552.30 (+13.88%)</td><td>463.40 <b>(+27.31%)</b></td><td>229.95 <b>(+111.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>632.60 (n/a)</td><td>491.54 (n/a)</td><td>485.00 (n/a)</td><td>364.00 (n/a)</td><td>108.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (-12.96%)</td><td>0.02 <b>(-23.15%)</b></td><td>0.02 <b>(-27.86%)</b></td><td>0.01 <b>(-24.06%)</b></td><td>0.01 (+8.94%)</td><td>656.80 <b>(+31.68%)</b></td><td>430.32 <b>(+35.23%)</b></td><td>400.20 <b>(+38.62%)</b></td><td>285.10 (+14.87%)</td><td>157.11 <b>(+52.45%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.80 (n/a)</td><td>318.22 (n/a)</td><td>288.70 (n/a)</td><td>248.20 (n/a)</td><td>103.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (-1.36%)</td><td>0.04 (-15.98%)</td><td>0.03 <b>(-35.73%)</b></td><td>0.02 (-17.98%)</td><td>0.02 <b>(+52.33%)</b></td><td>569.40 <b>(+21.93%)</b></td><td>400.70 <b>(+30.50%)</b></td><td>456.40 <b>(+55.61%)</b></td><td>230.70 (+1.41%)</td><td>160.12 <b>(+69.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>467.00 (n/a)</td><td>307.04 (n/a)</td><td>293.30 (n/a)</td><td>227.50 (n/a)</td><td>94.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (-11.59%)</td><td>0.03 <b>(+47.04%)</b></td><td>0.03 <b>(+115.02%)</b></td><td>0.01 <b>(+175.57%)</b></td><td>0.01 <b>(-20.52%)</b></td><td>674.60 <b>(-63.71%)</b></td><td>358.58 <b>(-50.41%)</b></td><td>243.90 <b>(-53.50%)</b></td><td>227.30 (+13.08%)</td><td>192.27 <b>(-70.43%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1858.90 (n/a)</td><td>723.02 (n/a)</td><td>524.50 (n/a)</td><td>201.00 (n/a)</td><td>650.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 <b>(+21.33%)</b></td><td>0.03 <b>(+30.21%)</b></td><td>0.03 <b>(+52.50%)</b></td><td>0.02 <b>(+82.30%)</b></td><td>0.01 (+0.73%)</td><td>600.70 <b>(-45.15%)</b></td><td>410.60 <b>(-30.54%)</b></td><td>384.30 <b>(-34.43%)</b></td><td>236.60 (-17.59%)</td><td>143.80 <b>(-54.09%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1095.10 (n/a)</td><td>591.16 (n/a)</td><td>586.10 (n/a)</td><td>287.10 (n/a)</td><td>313.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(-35.14%)</b></td><td>0.02 (-11.64%)</td><td>0.02 (+6.14%)</td><td>0.01 (-9.26%)</td><td>0.00 <b>(-60.22%)</b></td><td>632.90 (+10.20%)</td><td>496.52 (+5.85%)</td><td>477.00 (-5.79%)</td><td>378.00 <b>(+54.16%)</b></td><td>92.89 <b>(-27.70%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.30 (n/a)</td><td>469.10 (n/a)</td><td>506.30 (n/a)</td><td>245.20 (n/a)</td><td>128.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (-8.80%)</td><td>0.02 <b>(-20.41%)</b></td><td>0.02 <b>(-41.05%)</b></td><td>0.02 <b>(+26.89%)</b></td><td>0.01 <b>(-40.57%)</b></td><td>525.80 <b>(-21.19%)</b></td><td>445.94 (+8.56%)</td><td>469.30 <b>(+69.61%)</b></td><td>261.10 (+9.66%)</td><td>106.33 <b>(-51.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>667.20 (n/a)</td><td>410.76 (n/a)</td><td>276.70 (n/a)</td><td>238.10 (n/a)</td><td>218.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+9.95%)</td><td>0.02 (+4.39%)</td><td>0.01 <b>(-24.79%)</b></td><td>0.01 <b>(+204.12%)</b></td><td>0.01 <b>(-23.86%)</b></td><td>623.70 <b>(-67.12%)</b></td><td>502.34 <b>(-30.36%)</b></td><td>565.30 <b>(+32.95%)</b></td><td>292.80 (-9.07%)</td><td>133.93 <b>(-79.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1896.70 (n/a)</td><td>721.30 (n/a)</td><td>425.20 (n/a)</td><td>322.00 (n/a)</td><td>663.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+0.86%)</td><td>0.02 (+0.87%)</td><td>0.02 <b>(-26.83%)</b></td><td>0.02 <b>(+318.71%)</b></td><td>0.01 <b>(-47.73%)</b></td><td>482.40 <b>(-76.12%)</b></td><td>412.30 <b>(-39.80%)</b></td><td>441.60 <b>(+36.63%)</b></td><td>268.00 (-0.85%)</td><td>84.68 <b>(-88.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2019.70 (n/a)</td><td>684.84 (n/a)</td><td>323.20 (n/a)</td><td>270.30 (n/a)</td><td>752.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (+16.95%)</td><td>0.02 (+5.67%)</td><td>0.02 (-6.24%)</td><td>0.01 <b>(+42.87%)</b></td><td>0.01 (+14.15%)</td><td>558.60 <b>(-30.00%)</b></td><td>472.96 (-7.20%)</td><td>508.50 (+6.65%)</td><td>289.20 (-14.49%)</td><td>106.26 <b>(-38.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>798.00 (n/a)</td><td>509.66 (n/a)</td><td>476.80 (n/a)</td><td>338.20 (n/a)</td><td>171.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 <b>(-21.15%)</b></td><td>0.02 <b>(-33.73%)</b></td><td>0.02 (-18.46%)</td><td>0.00 <b>(-69.63%)</b></td><td>0.01 (-8.75%)</td><td>1932.60 <b>(+229.23%)</b></td><td>765.10 <b>(+95.18%)</b></td><td>531.40 <b>(+22.64%)</b></td><td>306.90 <b>(+26.82%)</b></td><td>659.70 <b>(+362.97%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>587.00 (n/a)</td><td>392.00 (n/a)</td><td>433.30 (n/a)</td><td>242.00 (n/a)</td><td>142.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 <b>(-46.00%)</b></td><td>0.01 <b>(-33.58%)</b></td><td>0.01 (-14.31%)</td><td>0.00 <b>(-76.92%)</b></td><td>0.01 <b>(-24.97%)</b></td><td>2428.00 <b>(+333.26%)</b></td><td>925.58 <b>(+99.32%)</b></td><td>617.90 (+16.69%)</td><td>467.50 <b>(+85.22%)</b></td><td>843.26 <b>(+551.83%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.40 (n/a)</td><td>464.36 (n/a)</td><td>529.50 (n/a)</td><td>252.40 (n/a)</td><td>129.37 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(+34.39%)</b></td><td>0.05 <b>(+27.09%)</b></td><td>0.05 <b>(+32.74%)</b></td><td>0.03 (-4.41%)</td><td>0.01 <b>(+72.12%)</b></td><td>600.70 (+4.60%)</td><td>386.56 (-17.76%)</td><td>354.90 <b>(-24.68%)</b></td><td>273.80 <b>(-25.60%)</b></td><td>132.96 <b>(+33.56%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>574.30 (n/a)</td><td>470.02 (n/a)</td><td>471.20 (n/a)</td><td>368.00 (n/a)</td><td>99.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 <b>(-42.39%)</b></td><td>0.06 <b>(-29.45%)</b></td><td>0.05 <b>(-38.76%)</b></td><td>0.05 (+8.87%)</td><td>0.02 <b>(-60.29%)</b></td><td>513.70 (-8.15%)</td><td>414.80 <b>(+22.05%)</b></td><td>458.70 <b>(+63.30%)</b></td><td>261.70 <b>(+73.54%)</b></td><td>98.78 <b>(-39.52%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>559.30 (n/a)</td><td>339.86 (n/a)</td><td>280.90 (n/a)</td><td>150.80 (n/a)</td><td>163.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 <b>(-35.65%)</b></td><td>0.03 (-10.54%)</td><td>0.03 <b>(+21.48%)</b></td><td>0.03 (-2.55%)</td><td>0.01 <b>(-66.22%)</b></td><td>627.80 (+2.63%)</td><td>491.58 (+2.40%)</td><td>474.60 (-17.68%)</td><td>427.30 <b>(+55.38%)</b></td><td>82.15 <b>(-48.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>611.70 (n/a)</td><td>480.08 (n/a)</td><td>576.50 (n/a)</td><td>275.00 (n/a)</td><td>157.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (-8.42%)</td><td>0.05 (-0.25%)</td><td>0.05 (-8.36%)</td><td>0.04 <b>(+82.14%)</b></td><td>0.02 <b>(-31.15%)</b></td><td>568.30 <b>(-45.09%)</b></td><td>415.36 (-15.83%)</td><td>400.60 (+9.13%)</td><td>256.50 (+9.20%)</td><td>128.26 <b>(-60.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1035.00 (n/a)</td><td>493.48 (n/a)</td><td>367.10 (n/a)</td><td>234.90 (n/a)</td><td>320.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 <b>(+40.86%)</b></td><td>0.06 <b>(+67.31%)</b></td><td>0.06 <b>(+59.28%)</b></td><td>0.04 <b>(+357.75%)</b></td><td>0.02 (-8.51%)</td><td>436.40 <b>(-78.15%)</b></td><td>286.56 <b>(-59.74%)</b></td><td>271.90 <b>(-37.22%)</b></td><td>192.50 <b>(-28.99%)</b></td><td>90.92 <b>(-87.41%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1997.40 (n/a)</td><td>711.86 (n/a)</td><td>433.10 (n/a)</td><td>271.10 (n/a)</td><td>722.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 <b>(+31.65%)</b></td><td>0.06 (+11.03%)</td><td>0.06 (+18.29%)</td><td>0.03 (-12.19%)</td><td>0.03 <b>(+62.68%)</b></td><td>682.10 (+13.87%)</td><td>411.60 (-1.19%)</td><td>358.20 (-15.48%)</td><td>205.50 <b>(-24.06%)</b></td><td>188.77 <b>(+44.97%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.00 (n/a)</td><td>416.56 (n/a)</td><td>423.80 (n/a)</td><td>270.60 (n/a)</td><td>130.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 <b>(+107.75%)</b></td><td>0.06 <b>(+91.45%)</b></td><td>0.06 <b>(+85.02%)</b></td><td>0.03 <b>(+119.83%)</b></td><td>0.02 <b>(+113.33%)</b></td><td>491.60 <b>(-54.51%)</b></td><td>333.60 <b>(-47.58%)</b></td><td>274.10 <b>(-45.96%)</b></td><td>205.90 <b>(-51.87%)</b></td><td>128.18 <b>(-52.05%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1080.70 (n/a)</td><td>636.42 (n/a)</td><td>507.20 (n/a)</td><td>427.80 (n/a)</td><td>267.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 <b>(-33.46%)</b></td><td>0.04 <b>(-21.96%)</b></td><td>0.04 (-11.58%)</td><td>0.03 (-6.36%)</td><td>0.01 <b>(-57.76%)</b></td><td>622.30 (+6.80%)</td><td>466.68 (+16.43%)</td><td>486.10 (+13.10%)</td><td>345.70 <b>(+50.30%)</b></td><td>108.50 <b>(-30.50%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>582.70 (n/a)</td><td>400.82 (n/a)</td><td>429.80 (n/a)</td><td>230.00 (n/a)</td><td>156.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (+1.14%)</td><td>0.04 (-6.62%)</td><td>0.04 (+2.26%)</td><td>0.03 (-11.91%)</td><td>0.02 (+2.92%)</td><td>544.30 (+13.54%)</td><td>414.80 (+7.86%)</td><td>415.60 (-2.21%)</td><td>240.10 (-1.11%)</td><td>117.00 (+9.09%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>479.40 (n/a)</td><td>384.58 (n/a)</td><td>425.00 (n/a)</td><td>242.80 (n/a)</td><td>107.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 <b>(-23.15%)</b></td><td>0.05 (+5.33%)</td><td>0.05 (+13.82%)</td><td>0.03 (+13.28%)</td><td>0.02 <b>(-28.01%)</b></td><td>577.30 (-11.73%)</td><td>399.86 (-10.69%)</td><td>354.70 (-12.14%)</td><td>239.60 <b>(+30.15%)</b></td><td>163.27 (-11.89%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>654.00 (n/a)</td><td>447.74 (n/a)</td><td>403.70 (n/a)</td><td>184.10 (n/a)</td><td>185.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (+4.43%)</td><td>0.04 (-5.70%)</td><td>0.03 (-12.89%)</td><td>0.03 (-6.75%)</td><td>0.02 (+17.82%)</td><td>576.20 (+7.24%)</td><td>465.14 (+9.06%)</td><td>542.00 (+14.78%)</td><td>254.90 (-4.24%)</td><td>137.82 <b>(+22.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>426.48 (n/a)</td><td>472.20 (n/a)</td><td>266.20 (n/a)</td><td>112.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+14.51%)</td><td>0.10 (+14.55%)</td><td>0.12 <b>(+29.11%)</b></td><td>0.05 (-15.90%)</td><td>0.04 <b>(+38.53%)</b></td><td>615.10 (+18.88%)</td><td>359.42 (-7.58%)</td><td>264.20 <b>(-22.57%)</b></td><td>241.70 (-12.65%)</td><td>160.39 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.40 (n/a)</td><td>388.88 (n/a)</td><td>341.20 (n/a)</td><td>276.70 (n/a)</td><td>119.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (-3.28%)</td><td>0.09 (-6.19%)</td><td>0.08 (-11.77%)</td><td>0.06 (-6.06%)</td><td>0.03 (-6.25%)</td><td>535.50 (+6.44%)</td><td>389.16 (+6.06%)</td><td>386.10 (+13.36%)</td><td>249.70 (+3.40%)</td><td>102.47 (-0.57%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>503.10 (n/a)</td><td>366.92 (n/a)</td><td>340.60 (n/a)</td><td>241.50 (n/a)</td><td>103.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.11 <b>(-38.90%)</b></td><td>0.07 <b>(-35.68%)</b></td><td>0.08 (-12.24%)</td><td>0.02 <b>(-71.11%)</b></td><td>0.03 <b>(-25.66%)</b></td><td>2042.00 <b>(+246.10%)</b></td><td>813.42 <b>(+95.58%)</b></td><td>529.20 (+13.95%)</td><td>382.20 <b>(+63.68%)</b></td><td>690.91 <b>(+395.93%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>590.00 (n/a)</td><td>415.90 (n/a)</td><td>464.40 (n/a)</td><td>233.50 (n/a)</td><td>139.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (-5.49%)</td><td>0.08 (+2.04%)</td><td>0.07 (-8.94%)</td><td>0.05 <b>(+204.08%)</b></td><td>0.03 <b>(-34.05%)</b></td><td>660.50 <b>(-67.11%)</b></td><td>451.12 <b>(-35.64%)</b></td><td>458.50 (+9.82%)</td><td>263.40 (+5.83%)</td><td>142.27 <b>(-80.67%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2008.40 (n/a)</td><td>700.96 (n/a)</td><td>417.50 (n/a)</td><td>248.90 (n/a)</td><td>735.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 (+1.10%)</td><td>0.09 <b>(-24.74%)</b></td><td>0.07 <b>(-47.85%)</b></td><td>0.06 <b>(-21.33%)</b></td><td>0.04 (+2.82%)</td><td>687.20 <b>(+27.12%)</b></td><td>515.86 <b>(+35.01%)</b></td><td>577.30 <b>(+91.73%)</b></td><td>251.30 (-1.06%)</td><td>167.34 (+15.20%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>540.60 (n/a)</td><td>382.08 (n/a)</td><td>301.10 (n/a)</td><td>254.00 (n/a)</td><td>145.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+13.08%)</td><td>0.07 <b>(-25.17%)</b></td><td>0.06 <b>(-45.34%)</b></td><td>0.04 <b>(-20.08%)</b></td><td>0.04 <b>(+37.24%)</b></td><td>743.50 <b>(+25.11%)</b></td><td>522.50 <b>(+42.70%)</b></td><td>550.70 <b>(+82.96%)</b></td><td>239.20 (-11.54%)</td><td>186.69 <b>(+38.92%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>594.30 (n/a)</td><td>366.14 (n/a)</td><td>301.00 (n/a)</td><td>270.40 (n/a)</td><td>134.39 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+5.79%)</td><td>0.09 (-6.05%)</td><td>0.08 <b>(-23.01%)</b></td><td>0.06 (+2.20%)</td><td>0.03 (+8.07%)</td><td>568.50 (-2.15%)</td><td>435.74 (+7.02%)</td><td>452.50 <b>(+29.88%)</b></td><td>260.90 (-5.47%)</td><td>131.99 (-0.21%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>581.00 (n/a)</td><td>407.16 (n/a)</td><td>348.40 (n/a)</td><td>276.00 (n/a)</td><td>132.27 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+2.07%)</td><td>0.07 (-13.49%)</td><td>0.06 (-18.38%)</td><td>0.05 <b>(-28.03%)</b></td><td>0.04 <b>(+26.77%)</b></td><td>677.30 <b>(+38.96%)</b></td><td>526.70 <b>(+24.15%)</b></td><td>566.20 <b>(+22.50%)</b></td><td>235.30 (-2.00%)</td><td>170.93 <b>(+63.77%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>487.40 (n/a)</td><td>424.26 (n/a)</td><td>462.20 (n/a)</td><td>240.10 (n/a)</td><td>104.37 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (-17.59%)</td><td>0.09 (-3.14%)</td><td>0.06 <b>(-24.69%)</b></td><td>0.06 <b>(+201.34%)</b></td><td>0.04 <b>(-32.64%)</b></td><td>638.70 <b>(-66.81%)</b></td><td>487.00 <b>(-31.05%)</b></td><td>604.20 <b>(+32.79%)</b></td><td>267.00 <b>(+21.36%)</b></td><td>185.76 <b>(-73.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1924.60 (n/a)</td><td>706.30 (n/a)</td><td>455.00 (n/a)</td><td>220.00 (n/a)</td><td>700.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (+6.57%)</td><td>0.06 (-4.56%)</td><td>0.07 (+8.88%)</td><td>0.02 <b>(-62.74%)</b></td><td>0.03 <b>(+55.41%)</b></td><td>1927.40 <b>(+168.37%)</b></td><td>735.30 <b>(+42.95%)</b></td><td>498.70 (-8.16%)</td><td>345.40 (-6.17%)</td><td>669.60 <b>(+361.88%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>718.20 (n/a)</td><td>514.38 (n/a)</td><td>543.00 (n/a)</td><td>368.10 (n/a)</td><td>144.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (+1.38%)</td><td>0.07 (+11.97%)</td><td>0.08 <b>(+43.26%)</b></td><td>0.04 (-10.11%)</td><td>0.02 (+2.49%)</td><td>486.10 (+11.26%)</td><td>315.62 (-9.77%)</td><td>272.20 <b>(-30.21%)</b></td><td>245.00 (-1.37%)</td><td>97.49 (+19.80%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>436.90 (n/a)</td><td>349.80 (n/a)</td><td>390.00 (n/a)</td><td>248.40 (n/a)</td><td>81.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (-7.03%)</td><td>0.05 (+1.44%)</td><td>0.05 (+11.39%)</td><td>0.03 (+6.10%)</td><td>0.02 (-13.81%)</td><td>624.60 (-5.75%)</td><td>449.70 (-3.46%)</td><td>424.00 (-10.23%)</td><td>254.50 (+7.57%)</td><td>141.17 (-7.14%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>662.70 (n/a)</td><td>465.84 (n/a)</td><td>472.30 (n/a)</td><td>236.60 (n/a)</td><td>152.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (+8.10%)</td><td>0.06 (+12.96%)</td><td>0.05 (-3.82%)</td><td>0.04 (+4.50%)</td><td>0.02 <b>(+24.20%)</b></td><td>530.50 (-4.31%)</td><td>383.74 (-10.28%)</td><td>417.50 (+3.96%)</td><td>266.30 (-7.50%)</td><td>114.42 (-1.68%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>554.40 (n/a)</td><td>427.72 (n/a)</td><td>401.60 (n/a)</td><td>287.90 (n/a)</td><td>116.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (-5.08%)</td><td>0.05 (-6.67%)</td><td>0.05 (-2.36%)</td><td>0.04 (-7.46%)</td><td>0.02 (-14.16%)</td><td>539.90 (+8.04%)</td><td>420.06 (+5.37%)</td><td>452.20 (+2.42%)</td><td>263.40 (+5.36%)</td><td>104.38 (-8.47%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>499.70 (n/a)</td><td>398.64 (n/a)</td><td>441.50 (n/a)</td><td>250.00 (n/a)</td><td>114.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 <b>(+23.65%)</b></td><td>0.05 (-4.41%)</td><td>0.04 (-3.01%)</td><td>0.03 <b>(-30.54%)</b></td><td>0.01 <b>(+211.17%)</b></td><td>673.40 <b>(+43.95%)</b></td><td>486.00 (+11.67%)</td><td>455.80 (+3.10%)</td><td>300.80 (-19.12%)</td><td>139.21 <b>(+258.25%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>467.80 (n/a)</td><td>435.22 (n/a)</td><td>442.10 (n/a)</td><td>371.90 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 <b>(+31.26%)</b></td><td>0.06 (+13.47%)</td><td>0.07 <b>(+40.97%)</b></td><td>0.01 <b>(-60.33%)</b></td><td>0.03 <b>(+97.45%)</b></td><td>1882.50 <b>(+152.11%)</b></td><td>638.10 <b>(+40.40%)</b></td><td>298.80 <b>(-29.08%)</b></td><td>224.70 <b>(-23.83%)</b></td><td>702.52 <b>(+302.22%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>746.70 (n/a)</td><td>454.48 (n/a)</td><td>421.30 (n/a)</td><td>295.00 (n/a)</td><td>174.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (-8.20%)</td><td>0.07 (+9.65%)</td><td>0.08 <b>(+49.65%)</b></td><td>0.05 (+11.49%)</td><td>0.01 <b>(-36.38%)</b></td><td>462.30 (-10.32%)</td><td>348.20 (-13.69%)</td><td>303.70 <b>(-33.16%)</b></td><td>287.60 (+8.90%)</td><td>78.57 <b>(-38.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>515.50 (n/a)</td><td>403.44 (n/a)</td><td>454.40 (n/a)</td><td>264.10 (n/a)</td><td>127.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (+13.41%)</td><td>0.07 (+7.02%)</td><td>0.06 (-11.09%)</td><td>0.04 (+1.36%)</td><td>0.03 <b>(+24.43%)</b></td><td>549.10 (-1.35%)</td><td>383.58 (-4.22%)</td><td>415.40 (+12.48%)</td><td>209.70 (-11.82%)</td><td>129.87 (+5.38%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>556.60 (n/a)</td><td>400.48 (n/a)</td><td>369.30 (n/a)</td><td>237.80 (n/a)</td><td>123.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (-16.16%)</td><td>0.07 (-17.71%)</td><td>0.06 <b>(-26.48%)</b></td><td>0.04 (-7.36%)</td><td>0.02 <b>(-34.35%)</b></td><td>550.30 (+7.94%)</td><td>399.78 (+14.98%)</td><td>417.20 <b>(+36.03%)</b></td><td>259.10 (+19.24%)</td><td>112.28 (-17.65%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>509.80 (n/a)</td><td>347.70 (n/a)</td><td>306.70 (n/a)</td><td>217.30 (n/a)</td><td>136.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(-28.55%)</b></td><td>0.04 <b>(-32.69%)</b></td><td>0.04 <b>(-24.44%)</b></td><td>0.01 <b>(-64.94%)</b></td><td>0.02 (-2.13%)</td><td>1912.00 <b>(+185.25%)</b></td><td>834.68 <b>(+80.90%)</b></td><td>610.40 <b>(+32.32%)</b></td><td>411.60 <b>(+39.95%)</b></td><td>609.05 <b>(+346.03%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>670.30 (n/a)</td><td>461.40 (n/a)</td><td>461.30 (n/a)</td><td>294.10 (n/a)</td><td>136.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 <b>(+99.60%)</b></td><td>0.07 <b>(+24.62%)</b></td><td>0.05 (-8.09%)</td><td>0.04 (-10.32%)</td><td>0.03 <b>(+253.51%)</b></td><td>648.30 (+11.51%)</td><td>430.28 (-9.17%)</td><td>451.30 (+8.80%)</td><td>204.30 <b>(-49.89%)</b></td><td>164.22 <b>(+89.54%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>581.40 (n/a)</td><td>473.70 (n/a)</td><td>414.80 (n/a)</td><td>407.70 (n/a)</td><td>86.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 <b>(+50.03%)</b></td><td>0.06 (+16.37%)</td><td>0.05 (-0.36%)</td><td>0.01 <b>(-56.71%)</b></td><td>0.04 <b>(+118.34%)</b></td><td>1850.50 <b>(+130.99%)</b></td><td>679.56 <b>(+36.23%)</b></td><td>454.80 (+0.38%)</td><td>195.20 <b>(-33.33%)</b></td><td>674.65 <b>(+247.14%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>801.10 (n/a)</td><td>498.82 (n/a)</td><td>453.10 (n/a)</td><td>292.80 (n/a)</td><td>194.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 <b>(+22.78%)</b></td><td>0.06 (+6.78%)</td><td>0.07 (+12.31%)</td><td>0.03 (-6.09%)</td><td>0.02 <b>(+68.90%)</b></td><td>532.10 (+6.48%)</td><td>360.80 (+1.95%)</td><td>272.60 (-10.94%)</td><td>218.10 (-18.56%)</td><td>154.12 <b>(+58.12%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>499.70 (n/a)</td><td>353.90 (n/a)</td><td>306.10 (n/a)</td><td>267.80 (n/a)</td><td>97.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (+12.55%)</td><td>0.05 (+7.21%)</td><td>0.04 <b>(-20.76%)</b></td><td>0.03 <b>(+232.92%)</b></td><td>0.02 (-11.98%)</td><td>602.20 <b>(-69.96%)</b></td><td>434.58 <b>(-36.74%)</b></td><td>506.40 <b>(+26.19%)</b></td><td>243.30 (-11.14%)</td><td>157.84 <b>(-78.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2004.90 (n/a)</td><td>686.96 (n/a)</td><td>401.30 (n/a)</td><td>273.80 (n/a)</td><td>740.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (-13.70%)</td><td>0.05 <b>(-24.40%)</b></td><td>0.05 <b>(-24.46%)</b></td><td>0.03 (-16.10%)</td><td>0.02 (+3.09%)</td><td>681.10 (+19.20%)</td><td>447.46 <b>(+36.89%)</b></td><td>356.20 <b>(+32.37%)</b></td><td>291.50 (+15.90%)</td><td>185.26 <b>(+35.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.40 (n/a)</td><td>326.88 (n/a)</td><td>269.10 (n/a)</td><td>251.50 (n/a)</td><td>137.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 <b>(-21.66%)</b></td><td>0.05 (+0.04%)</td><td>0.05 (+13.13%)</td><td>0.02 <b>(-31.53%)</b></td><td>0.02 (-10.61%)</td><td>1084.60 <b>(+46.05%)</b></td><td>510.76 (+8.54%)</td><td>401.60 (-11.60%)</td><td>290.40 <b>(+27.65%)</b></td><td>329.81 <b>(+78.96%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>742.60 (n/a)</td><td>470.56 (n/a)</td><td>454.30 (n/a)</td><td>227.50 (n/a)</td><td>184.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 <b>(+24.91%)</b></td><td>0.05 (+3.12%)</td><td>0.04 (+11.71%)</td><td>0.03 (+1.00%)</td><td>0.02 <b>(+25.97%)</b></td><td>599.10 (-0.99%)</td><td>424.08 (-0.90%)</td><td>427.50 (-10.49%)</td><td>222.80 (-19.97%)</td><td>142.72 (+2.35%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.10 (n/a)</td><td>427.92 (n/a)</td><td>477.60 (n/a)</td><td>278.40 (n/a)</td><td>139.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 <b>(-49.18%)</b></td><td>0.03 <b>(-37.68%)</b></td><td>0.03 <b>(-43.94%)</b></td><td>0.03 (-15.47%)</td><td>0.00 <b>(-79.37%)</b></td><td>608.80 (+18.31%)</td><td>532.26 <b>(+47.43%)</b></td><td>528.90 <b>(+78.38%)</b></td><td>456.40 <b>(+96.81%)</b></td><td>57.24 <b>(-54.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>514.60 (n/a)</td><td>361.02 (n/a)</td><td>296.50 (n/a)</td><td>231.90 (n/a)</td><td>125.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.35 (-12.75%)</td><td>0.25 (-16.16%)</td><td>0.24 <b>(-24.30%)</b></td><td>0.18 (-14.98%)</td><td>0.07 (-12.51%)</td><td>555.50 (+17.62%)</td><td>411.74 (+19.30%)</td><td>416.20 <b>(+32.09%)</b></td><td>281.20 (+14.64%)</td><td>108.05 (+15.29%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>472.30 (n/a)</td><td>345.14 (n/a)</td><td>315.10 (n/a)</td><td>245.30 (n/a)</td><td>93.72 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.32 <b>(-20.59%)</b></td><td>0.17 <b>(-44.58%)</b></td><td>0.16 <b>(-50.43%)</b></td><td>0.05 <b>(-71.94%)</b></td><td>0.11 (+3.45%)</td><td>1813.50 <b>(+256.36%)</b></td><td>854.44 <b>(+137.29%)</b></td><td>598.80 <b>(+101.75%)</b></td><td>303.80 <b>(+25.90%)</b></td><td>608.44 <b>(+359.31%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>508.90 (n/a)</td><td>360.08 (n/a)</td><td>296.80 (n/a)</td><td>241.30 (n/a)</td><td>132.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.36 <b>(+23.45%)</b></td><td>0.26 (+19.09%)</td><td>0.27 <b>(+47.66%)</b></td><td>0.16 (+1.16%)</td><td>0.09 <b>(+56.66%)</b></td><td>607.00 (-1.16%)</td><td>424.58 (-11.28%)</td><td>357.80 <b>(-32.27%)</b></td><td>276.40 (-18.99%)</td><td>158.75 <b>(+33.98%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>614.10 (n/a)</td><td>478.54 (n/a)</td><td>528.30 (n/a)</td><td>341.20 (n/a)</td><td>118.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.37 <b>(+40.87%)</b></td><td>0.23 <b>(+21.68%)</b></td><td>0.23 <b>(+39.90%)</b></td><td>0.12 (+3.39%)</td><td>0.10 <b>(+71.31%)</b></td><td>607.40 (-3.28%)</td><td>374.42 (-11.41%)</td><td>314.40 <b>(-28.51%)</b></td><td>197.70 <b>(-29.01%)</b></td><td>163.97 <b>(+21.32%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>628.00 (n/a)</td><td>422.62 (n/a)</td><td>439.80 (n/a)</td><td>278.50 (n/a)</td><td>135.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.29 (-0.07%)</td><td>0.18 (-4.62%)</td><td>0.14 (-18.84%)</td><td>0.11 <b>(+60.86%)</b></td><td>0.09 (-4.80%)</td><td>683.60 <b>(-37.83%)</b></td><td>474.36 (-5.44%)</td><td>533.80 <b>(+23.22%)</b></td><td>252.90 (+0.08%)</td><td>196.06 <b>(-43.31%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>1099.60 (n/a)</td><td>501.66 (n/a)</td><td>433.20 (n/a)</td><td>252.70 (n/a)</td><td>345.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.37 <b>(+29.44%)</b></td><td>0.18 (-1.39%)</td><td>0.13 (-5.81%)</td><td>0.11 (-8.93%)</td><td>0.11 <b>(+54.86%)</b></td><td>684.40 (+9.80%)</td><td>504.86 (+10.71%)</td><td>551.20 (+6.18%)</td><td>200.50 <b>(-22.77%)</b></td><td>190.41 <b>(+25.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>623.30 (n/a)</td><td>456.02 (n/a)</td><td>519.10 (n/a)</td><td>259.60 (n/a)</td><td>151.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.17 (+2.68%)</td><td>0.11 (-9.74%)</td><td>0.12 (-8.85%)</td><td>0.08 (-8.44%)</td><td>0.04 <b>(+21.03%)</b></td><td>487.80 (+9.20%)</td><td>348.14 (+13.66%)</td><td>317.60 (+9.71%)</td><td>215.80 (-2.57%)</td><td>105.72 <b>(+24.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>446.70 (n/a)</td><td>306.30 (n/a)</td><td>289.50 (n/a)</td><td>221.50 (n/a)</td><td>84.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+8.71%)</td><td>0.12 <b>(+41.51%)</b></td><td>0.13 <b>(+75.02%)</b></td><td>0.06 (+5.77%)</td><td>0.03 (+19.75%)</td><td>580.00 (-5.46%)</td><td>347.28 <b>(-27.77%)</b></td><td>280.40 <b>(-42.86%)</b></td><td>266.90 (-8.03%)</td><td>133.14 (+12.63%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>613.50 (n/a)</td><td>480.80 (n/a)</td><td>490.70 (n/a)</td><td>290.20 (n/a)</td><td>118.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (-0.93%)</td><td>0.09 (-6.03%)</td><td>0.08 (-10.99%)</td><td>0.05 <b>(+157.76%)</b></td><td>0.03 <b>(-31.55%)</b></td><td>738.40 <b>(-61.20%)</b></td><td>487.26 <b>(-28.11%)</b></td><td>485.00 (+12.35%)</td><td>262.70 (+0.92%)</td><td>177.11 <b>(-74.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1903.30 (n/a)</td><td>677.78 (n/a)</td><td>431.70 (n/a)</td><td>260.30 (n/a)</td><td>693.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.22 <b>(+52.41%)</b></td><td>0.12 (+17.95%)</td><td>0.13 <b>(+51.94%)</b></td><td>0.07 <b>(-20.32%)</b></td><td>0.06 <b>(+120.76%)</b></td><td>562.10 <b>(+25.50%)</b></td><td>368.48 (-1.49%)</td><td>284.20 <b>(-34.20%)</b></td><td>169.20 <b>(-34.39%)</b></td><td>177.46 <b>(+95.52%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>447.90 (n/a)</td><td>374.06 (n/a)</td><td>431.90 (n/a)</td><td>257.90 (n/a)</td><td>90.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 <b>(+22.91%)</b></td><td>0.09 (+1.60%)</td><td>0.07 (-9.22%)</td><td>0.03 <b>(-27.21%)</b></td><td>0.05 <b>(+41.08%)</b></td><td>1087.10 <b>(+37.38%)</b></td><td>539.94 (+13.91%)</td><td>524.60 (+10.16%)</td><td>224.60 (-18.62%)</td><td>338.93 <b>(+62.82%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>791.30 (n/a)</td><td>474.00 (n/a)</td><td>476.20 (n/a)</td><td>276.00 (n/a)</td><td>208.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (-16.41%)</td><td>0.08 (+6.88%)</td><td>0.08 <b>(+31.50%)</b></td><td>0.07 <b>(+23.52%)</b></td><td>0.01 <b>(-69.06%)</b></td><td>539.40 (-19.03%)</td><td>482.26 (-11.49%)</td><td>473.70 <b>(-23.94%)</b></td><td>428.10 (+19.65%)</td><td>40.92 <b>(-70.58%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>666.20 (n/a)</td><td>544.84 (n/a)</td><td>622.80 (n/a)</td><td>357.80 (n/a)</td><td>139.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.18 (+5.24%)</td><td>0.11 (-16.80%)</td><td>0.09 <b>(-32.22%)</b></td><td>0.05 <b>(-41.07%)</b></td><td>0.06 <b>(+103.27%)</b></td><td>785.90 <b>(+69.70%)</b></td><td>470.12 <b>(+46.83%)</b></td><td>440.40 <b>(+47.54%)</b></td><td>227.90 (-4.96%)</td><td>248.08 <b>(+195.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>463.10 (n/a)</td><td>320.18 (n/a)</td><td>298.50 (n/a)</td><td>239.80 (n/a)</td><td>84.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (-18.49%)</td><td>0.13 (+9.63%)</td><td>0.13 <b>(+45.30%)</b></td><td>0.11 <b>(+54.43%)</b></td><td>0.02 <b>(-66.09%)</b></td><td>389.20 <b>(-35.24%)</b></td><td>330.08 (-19.72%)</td><td>305.00 <b>(-31.17%)</b></td><td>284.90 <b>(+22.70%)</b></td><td>45.75 <b>(-71.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>601.00 (n/a)</td><td>411.18 (n/a)</td><td>443.10 (n/a)</td><td>232.20 (n/a)</td><td>162.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 (-19.11%)</td><td>0.11 (+15.49%)</td><td>0.08 (-8.47%)</td><td>0.07 <b>(+237.05%)</b></td><td>0.04 <b>(-33.52%)</b></td><td>550.00 <b>(-70.33%)</b></td><td>412.46 <b>(-41.00%)</b></td><td>482.20 (+9.24%)</td><td>257.10 <b>(+23.61%)</b></td><td>140.22 <b>(-78.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1853.60 (n/a)</td><td>699.14 (n/a)</td><td>441.40 (n/a)</td><td>208.00 (n/a)</td><td>657.73 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.19 (+4.75%)</td><td>0.10 (-19.49%)</td><td>0.08 <b>(-44.92%)</b></td><td>0.02 <b>(-58.71%)</b></td><td>0.06 (+12.90%)</td><td>1853.70 <b>(+142.19%)</b></td><td>693.68 <b>(+66.64%)</b></td><td>503.70 <b>(+81.58%)</b></td><td>218.70 (-4.54%)</td><td>666.55 <b>(+179.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>765.40 (n/a)</td><td>416.28 (n/a)</td><td>277.40 (n/a)</td><td>229.10 (n/a)</td><td>238.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.17 (-13.10%)</td><td>0.11 (+8.30%)</td><td>0.09 (+11.44%)</td><td>0.07 <b>(+216.87%)</b></td><td>0.04 <b>(-37.16%)</b></td><td>575.00 <b>(-68.44%)</b></td><td>405.30 <b>(-39.55%)</b></td><td>454.20 (-10.27%)</td><td>243.30 (+15.09%)</td><td>137.08 <b>(-79.16%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>1822.10 (n/a)</td><td>670.42 (n/a)</td><td>506.20 (n/a)</td><td>211.40 (n/a)</td><td>657.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (-16.30%)</td><td>0.10 (-10.90%)</td><td>0.09 (-13.20%)</td><td>0.08 (-11.07%)</td><td>0.03 <b>(-26.16%)</b></td><td>543.70 (+12.45%)</td><td>424.28 (+9.74%)</td><td>453.60 (+15.21%)</td><td>272.70 (+19.50%)</td><td>100.01 (-5.91%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>483.50 (n/a)</td><td>386.62 (n/a)</td><td>393.70 (n/a)</td><td>228.20 (n/a)</td><td>106.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+17.92%)</td><td>0.08 (-13.11%)</td><td>0.06 (-18.56%)</td><td>0.05 (-10.78%)</td><td>0.04 <b>(+34.09%)</b></td><td>636.20 (+12.07%)</td><td>518.60 <b>(+21.14%)</b></td><td>575.00 <b>(+22.81%)</b></td><td>243.10 (-15.18%)</td><td>161.97 <b>(+27.56%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>567.70 (n/a)</td><td>428.10 (n/a)</td><td>468.20 (n/a)</td><td>286.60 (n/a)</td><td>126.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (-0.68%)</td><td>0.09 (+18.47%)</td><td>0.09 <b>(+44.71%)</b></td><td>0.06 (+9.36%)</td><td>0.02 (-13.73%)</td><td>573.30 (-8.56%)</td><td>428.74 (-17.42%)</td><td>388.00 <b>(-30.90%)</b></td><td>287.70 (+0.70%)</td><td>115.80 (-14.95%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>627.00 (n/a)</td><td>519.20 (n/a)</td><td>561.50 (n/a)</td><td>285.70 (n/a)</td><td>136.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (-3.53%)</td><td>0.07 (+3.09%)</td><td>0.07 (-0.33%)</td><td>0.02 <b>(-45.25%)</b></td><td>0.04 (+3.93%)</td><td>1933.00 <b>(+82.63%)</b></td><td>731.70 <b>(+20.57%)</b></td><td>508.10 (+0.34%)</td><td>266.00 (+3.66%)</td><td>680.14 <b>(+126.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1058.40 (n/a)</td><td>606.86 (n/a)</td><td>506.40 (n/a)</td><td>256.60 (n/a)</td><td>299.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (+0.26%)</td><td>0.10 (+15.16%)</td><td>0.07 (-3.57%)</td><td>0.06 <b>(+35.26%)</b></td><td>0.04 (-10.02%)</td><td>536.30 <b>(-26.07%)</b></td><td>403.86 (-18.03%)</td><td>474.20 (+3.72%)</td><td>237.70 (-0.25%)</td><td>129.30 <b>(-34.77%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>725.40 (n/a)</td><td>492.72 (n/a)</td><td>457.20 (n/a)</td><td>238.30 (n/a)</td><td>198.23 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (-9.42%)</td><td>0.08 (-7.94%)</td><td>0.06 (+1.00%)</td><td>0.04 <b>(-22.20%)</b></td><td>0.04 (-10.10%)</td><td>795.00 <b>(+28.52%)</b></td><td>502.54 (+8.86%)</td><td>582.50 (-1.00%)</td><td>269.40 (+10.41%)</td><td>228.68 (+15.57%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>618.60 (n/a)</td><td>461.62 (n/a)</td><td>588.40 (n/a)</td><td>244.00 (n/a)</td><td>197.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (+0.14%)</td><td>0.09 (+14.90%)</td><td>0.10 <b>(+30.89%)</b></td><td>0.06 (-5.78%)</td><td>0.03 (+15.54%)</td><td>610.00 (+6.14%)</td><td>410.30 (-10.56%)</td><td>360.70 <b>(-23.61%)</b></td><td>276.10 (-0.14%)</td><td>146.54 <b>(+21.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>574.70 (n/a)</td><td>458.76 (n/a)</td><td>472.20 (n/a)</td><td>276.50 (n/a)</td><td>120.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.44 <b>(-27.19%)</b></td><td>0.33 (-17.50%)</td><td>0.35 (-19.20%)</td><td>0.20 (-9.55%)</td><td>0.10 <b>(-39.11%)</b></td><td>665.30 (+10.57%)</td><td>426.60 (+14.24%)</td><td>369.40 <b>(+23.75%)</b></td><td>295.70 <b>(+37.34%)</b></td><td>148.02 (-8.31%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.61 (n/a)</td><td>0.40 (n/a)</td><td>0.44 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>601.70 (n/a)</td><td>373.42 (n/a)</td><td>298.50 (n/a)</td><td>215.30 (n/a)</td><td>161.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.40 (-15.50%)</td><td>0.30 (-14.46%)</td><td>0.27 <b>(-31.38%)</b></td><td>0.20 <b>(+52.83%)</b></td><td>0.08 <b>(-39.55%)</b></td><td>657.90 <b>(-34.57%)</b></td><td>460.90 (+0.09%)</td><td>478.00 <b>(+45.73%)</b></td><td>331.70 (+18.34%)</td><td>129.30 <b>(-57.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.40 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>1005.50 (n/a)</td><td>460.50 (n/a)</td><td>328.00 (n/a)</td><td>280.30 (n/a)</td><td>306.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.45 (+6.04%)</td><td>0.34 (+0.31%)</td><td>0.41 (-0.55%)</td><td>0.07 <b>(-65.90%)</b></td><td>0.16 <b>(+46.36%)</b></td><td>1923.00 <b>(+193.23%)</b></td><td>641.68 <b>(+51.61%)</b></td><td>321.40 (+0.56%)</td><td>288.20 (-5.69%)</td><td>716.95 <b>(+351.78%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.41 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>655.80 (n/a)</td><td>423.24 (n/a)</td><td>319.60 (n/a)</td><td>305.60 (n/a)</td><td>158.69 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/strided_copy</summary>


### test_strided_copy[chunked_transfer]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>311.30 (n/a)</td><td>286.90 (n/a)</td><td>304.10 (n/a)</td><td>245.30 (n/a)</td><td>30.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[contiguous]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.00 (n/a)</td><td>394.74 (n/a)</td><td>438.90 (n/a)</td><td>278.70 (n/a)</td><td>103.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.70 (n/a)</td><td>456.70 (n/a)</td><td>478.60 (n/a)</td><td>298.30 (n/a)</td><td>111.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_llama_full]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>9.03 (n/a)</td><td>6.36 (n/a)</td><td>7.11 (n/a)</td><td>3.82 (n/a)</td><td>2.22 (n/a)</td><td>549.80 (n/a)</td><td>368.38 (n/a)</td><td>295.10 (n/a)</td><td>232.30 (n/a)</td><td>140.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.64 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>648.20 (n/a)</td><td>369.06 (n/a)</td><td>310.10 (n/a)</td><td>204.90 (n/a)</td><td>175.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.53 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>468.60 (n/a)</td><td>335.94 (n/a)</td><td>287.90 (n/a)</td><td>247.40 (n/a)</td><td>104.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.52 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>496.10 (n/a)</td><td>308.70 (n/a)</td><td>252.80 (n/a)</td><td>237.40 (n/a)</td><td>108.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>501.10 (n/a)</td><td>405.14 (n/a)</td><td>434.20 (n/a)</td><td>283.60 (n/a)</td><td>103.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot_last]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>481.70 (n/a)</td><td>304.54 (n/a)</td><td>287.20 (n/a)</td><td>228.20 (n/a)</td><td>103.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.40 (n/a)</td><td>423.00 (n/a)</td><td>484.20 (n/a)</td><td>240.70 (n/a)</td><td>116.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels_chunked]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1918.60 (n/a)</td><td>764.28 (n/a)</td><td>524.90 (n/a)</td><td>328.60 (n/a)</td><td>656.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 <b>(+35.71%)</b></td><td>0.00 <b>(+33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+113.81%)</b></td><td>18893.06 (+2.52%)</td><td>12192.50 (-18.72%)</td><td>10283.14 <b>(-30.39%)</b></td><td>7017.00 <b>(-32.44%)</b></td><td>5530.10 <b>(+68.65%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18429.39 (n/a)</td><td>15001.28 (n/a)</td><td>14771.67 (n/a)</td><td>10385.56 (n/a)</td><td>3278.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.00 <b>(-21.43%)</b></td><td>0.00 (+6.06%)</td><td>0.00 (+20.00%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(-38.70%)</b></td><td>17130.83 (-12.55%)</td><td>13233.35 (-11.36%)</td><td>14123.64 (-11.36%)</td><td>7567.52 <b>(+26.66%)</b></td><td>4187.24 <b>(-20.46%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19588.56 (n/a)</td><td>14929.13 (n/a)</td><td>15933.62 (n/a)</td><td>5974.46 (n/a)</td><td>5264.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (+4.63%)</td><td>0.12 <b>(+22.55%)</b></td><td>0.14 <b>(+66.91%)</b></td><td>0.09 <b>(+27.29%)</b></td><td>0.03 (-5.05%)</td><td>24300.26 <b>(-21.41%)</b></td><td>18532.32 <b>(-20.19%)</b></td><td>15224.72 <b>(-40.08%)</b></td><td>14282.91 (-4.47%)</td><td>5108.41 <b>(-25.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30921.72 (n/a)</td><td>23220.15 (n/a)</td><td>25407.18 (n/a)</td><td>14951.41 (n/a)</td><td>6884.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.42 (-9.36%)</td><td>1.75 (-1.63%)</td><td>1.94 (+8.84%)</td><td>0.98 <b>(+89.92%)</b></td><td>0.66 <b>(-25.87%)</b></td><td>1069.70 <b>(-47.34%)</b></td><td>686.60 (-18.08%)</td><td>541.00 (-8.13%)</td><td>432.70 (+10.33%)</td><td>291.60 <b>(-57.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.67 (n/a)</td><td>1.78 (n/a)</td><td>1.78 (n/a)</td><td>0.52 (n/a)</td><td>0.89 (n/a)</td><td>2031.50 (n/a)</td><td>838.14 (n/a)</td><td>588.90 (n/a)</td><td>392.20 (n/a)</td><td>684.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.15 (-3.40%)</td><td>1.62 (-17.76%)</td><td>1.80 (+10.06%)</td><td>0.30 <b>(-73.92%)</b></td><td>1.07 <b>(+20.27%)</b></td><td>3551.10 <b>(+283.53%)</b></td><td>1215.48 <b>(+96.46%)</b></td><td>582.10 (-9.15%)</td><td>332.60 (+3.52%)</td><td>1331.32 <b>(+431.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.26 (n/a)</td><td>1.97 (n/a)</td><td>1.64 (n/a)</td><td>1.13 (n/a)</td><td>0.89 (n/a)</td><td>925.90 (n/a)</td><td>618.68 (n/a)</td><td>640.70 (n/a)</td><td>321.30 (n/a)</td><td>250.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.02 (-9.78%)</td><td>2.17 (-8.96%)</td><td>2.59 (+8.64%)</td><td>1.14 <b>(-30.28%)</b></td><td>0.83 <b>(+21.22%)</b></td><td>921.70 <b>(+43.43%)</b></td><td>557.90 (+19.02%)</td><td>404.70 (-7.96%)</td><td>347.60 (+10.84%)</td><td>252.75 <b>(+90.16%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.34 (n/a)</td><td>2.39 (n/a)</td><td>2.38 (n/a)</td><td>1.63 (n/a)</td><td>0.68 (n/a)</td><td>642.60 (n/a)</td><td>468.76 (n/a)</td><td>439.70 (n/a)</td><td>313.60 (n/a)</td><td>132.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.60 <b>(+33.66%)</b></td><td>1.67 (+2.01%)</td><td>1.82 (+1.44%)</td><td>0.42 <b>(-58.83%)</b></td><td>0.80 <b>(+116.11%)</b></td><td>2505.60 <b>(+142.88%)</b></td><td>937.40 <b>(+38.71%)</b></td><td>574.60 (-1.42%)</td><td>403.00 <b>(-25.19%)</b></td><td>881.47 <b>(+334.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>1.95 (n/a)</td><td>1.64 (n/a)</td><td>1.80 (n/a)</td><td>1.02 (n/a)</td><td>0.37 (n/a)</td><td>1031.60 (n/a)</td><td>675.82 (n/a)</td><td>582.90 (n/a)</td><td>538.70 (n/a)</td><td>202.89 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>4.39 (+11.49%)</td><td>3.39 <b>(+33.84%)</b></td><td>3.05 <b>(+22.01%)</b></td><td>2.38 <b>(+312.17%)</b></td><td>0.90 <b>(-31.14%)</b></td><td>880.90 <b>(-75.74%)</b></td><td>655.48 <b>(-50.21%)</b></td><td>687.40 (-18.04%)</td><td>477.60 (-10.31%)</td><td>172.42 <b>(-86.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>3.94 (n/a)</td><td>2.53 (n/a)</td><td>2.50 (n/a)</td><td>0.58 (n/a)</td><td>1.31 (n/a)</td><td>3630.90 (n/a)</td><td>1316.52 (n/a)</td><td>838.70 (n/a)</td><td>532.50 (n/a)</td><td>1306.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.30 (+9.08%)</td><td>3.43 <b>(+24.96%)</b></td><td>3.74 <b>(+44.94%)</b></td><td>0.58 (-0.86%)</td><td>2.20 (-2.99%)</td><td>3635.20 (+0.87%)</td><td>1201.98 <b>(-31.48%)</b></td><td>561.10 <b>(-31.00%)</b></td><td>332.90 (-8.32%)</td><td>1383.57 (-15.88%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.78 (n/a)</td><td>2.74 (n/a)</td><td>2.58 (n/a)</td><td>0.58 (n/a)</td><td>2.27 (n/a)</td><td>3604.00 (n/a)</td><td>1754.28 (n/a)</td><td>813.20 (n/a)</td><td>363.10 (n/a)</td><td>1644.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.42 (+4.84%)</td><td>2.85 <b>(-21.24%)</b></td><td>2.48 <b>(-26.32%)</b></td><td>0.65 <b>(-75.11%)</b></td><td>1.93 <b>(+100.88%)</b></td><td>3228.70 <b>(+301.73%)</b></td><td>1260.24 <b>(+107.05%)</b></td><td>845.90 <b>(+35.71%)</b></td><td>387.10 (-4.63%)</td><td>1160.36 <b>(+696.46%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.17 (n/a)</td><td>3.62 (n/a)</td><td>3.36 (n/a)</td><td>2.61 (n/a)</td><td>0.96 (n/a)</td><td>803.70 (n/a)</td><td>608.66 (n/a)</td><td>623.30 (n/a)</td><td>405.90 (n/a)</td><td>145.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.62 (+0.39%)</td><td>3.37 (-15.61%)</td><td>3.81 (-2.80%)</td><td>0.60 <b>(-70.72%)</b></td><td>2.26 <b>(+25.82%)</b></td><td>3501.10 <b>(+241.57%)</b></td><td>1192.02 <b>(+91.88%)</b></td><td>550.00 (+2.88%)</td><td>317.00 (-0.38%)</td><td>1317.98 <b>(+363.12%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.59 (n/a)</td><td>4.00 (n/a)</td><td>3.92 (n/a)</td><td>2.05 (n/a)</td><td>1.80 (n/a)</td><td>1025.00 (n/a)</td><td>621.22 (n/a)</td><td>534.60 (n/a)</td><td>318.20 (n/a)</td><td>284.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.05 <b>(-25.94%)</b></td><td>3.96 (-0.53%)</td><td>4.19 <b>(+29.18%)</b></td><td>2.63 (-7.43%)</td><td>0.92 <b>(-44.55%)</b></td><td>797.60 (+8.03%)</td><td>556.54 (-4.72%)</td><td>500.70 <b>(-22.58%)</b></td><td>415.40 <b>(+35.05%)</b></td><td>148.94 (-15.81%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.82 (n/a)</td><td>3.98 (n/a)</td><td>3.24 (n/a)</td><td>2.84 (n/a)</td><td>1.66 (n/a)</td><td>738.30 (n/a)</td><td>584.10 (n/a)</td><td>646.70 (n/a)</td><td>307.60 (n/a)</td><td>176.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>4.70 <b>(-25.18%)</b></td><td>2.28 (-16.53%)</td><td>2.18 <b>(+95.16%)</b></td><td>0.60 (+4.47%)</td><td>1.77 <b>(-35.41%)</b></td><td>3516.00 (-4.28%)</td><td>1801.56 (-8.97%)</td><td>960.80 <b>(-48.76%)</b></td><td>446.10 <b>(+33.64%)</b></td><td>1546.94 (-5.34%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.28 (n/a)</td><td>2.73 (n/a)</td><td>1.12 (n/a)</td><td>0.57 (n/a)</td><td>2.74 (n/a)</td><td>3673.20 (n/a)</td><td>1979.16 (n/a)</td><td>1875.10 (n/a)</td><td>333.80 (n/a)</td><td>1634.23 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.26 (+0.82%)</td><td>4.34 <b>(+44.82%)</b></td><td>4.11 (+15.78%)</td><td>3.46 <b>(+217.53%)</b></td><td>0.71 <b>(-61.23%)</b></td><td>1210.70 <b>(-68.51%)</b></td><td>986.98 <b>(-53.35%)</b></td><td>1021.40 (-13.63%)</td><td>796.80 (-0.82%)</td><td>161.37 <b>(-89.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>5.22 (n/a)</td><td>3.00 (n/a)</td><td>3.55 (n/a)</td><td>1.09 (n/a)</td><td>1.83 (n/a)</td><td>3844.40 (n/a)</td><td>2115.74 (n/a)</td><td>1182.60 (n/a)</td><td>803.40 (n/a)</td><td>1518.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>7.69 (+7.64%)</td><td>4.87 (-4.84%)</td><td>5.68 (-10.06%)</td><td>1.17 (-1.34%)</td><td>3.02 <b>(+21.25%)</b></td><td>3571.10 (+1.36%)</td><td>1455.50 (+13.65%)</td><td>737.90 (+11.20%)</td><td>545.20 (-7.11%)</td><td>1304.03 (+3.06%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>7.15 (n/a)</td><td>5.12 (n/a)</td><td>6.32 (n/a)</td><td>1.19 (n/a)</td><td>2.49 (n/a)</td><td>3523.20 (n/a)</td><td>1280.74 (n/a)</td><td>663.60 (n/a)</td><td>586.90 (n/a)</td><td>1265.27 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>8.77 (+1.27%)</td><td>6.27 (+10.10%)</td><td>8.41 <b>(+42.13%)</b></td><td>1.70 <b>(-55.65%)</b></td><td>3.26 <b>(+68.18%)</b></td><td>2461.80 <b>(+125.50%)</b></td><td>1000.48 <b>(+24.51%)</b></td><td>498.80 <b>(-29.64%)</b></td><td>478.20 (-1.26%)</td><td>855.14 <b>(+238.03%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>8.66 (n/a)</td><td>5.69 (n/a)</td><td>5.92 (n/a)</td><td>3.84 (n/a)</td><td>1.94 (n/a)</td><td>1091.70 (n/a)</td><td>803.54 (n/a)</td><td>708.90 (n/a)</td><td>484.30 (n/a)</td><td>252.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>9.36 (-3.29%)</td><td>8.07 <b>(+21.60%)</b></td><td>7.85 <b>(+22.84%)</b></td><td>6.37 <b>(+44.90%)</b></td><td>1.26 <b>(-34.95%)</b></td><td>658.60 <b>(-30.99%)</b></td><td>530.28 <b>(-21.36%)</b></td><td>534.50 (-18.58%)</td><td>448.30 (+3.39%)</td><td>86.84 <b>(-54.18%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>9.67 (n/a)</td><td>6.64 (n/a)</td><td>6.39 (n/a)</td><td>4.40 (n/a)</td><td>1.94 (n/a)</td><td>954.30 (n/a)</td><td>674.32 (n/a)</td><td>656.50 (n/a)</td><td>433.60 (n/a)</td><td>189.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>10.33 (+9.34%)</td><td>5.55 (+4.95%)</td><td>6.98 <b>(+91.69%)</b></td><td>1.10 (-5.98%)</td><td>4.22 (+17.11%)</td><td>3824.20 (+6.35%)</td><td>1818.38 <b>(+32.03%)</b></td><td>600.60 <b>(-47.83%)</b></td><td>406.20 (-8.53%)</td><td>1798.56 <b>(+39.25%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>9.44 (n/a)</td><td>5.28 (n/a)</td><td>3.64 (n/a)</td><td>1.17 (n/a)</td><td>3.61 (n/a)</td><td>3595.70 (n/a)</td><td>1377.24 (n/a)</td><td>1151.20 (n/a)</td><td>444.10 (n/a)</td><td>1291.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>9.71 <b>(+49.81%)</b></td><td>7.21 <b>(+52.66%)</b></td><td>8.20 <b>(+29.49%)</b></td><td>1.19 (+9.88%)</td><td>3.50 <b>(+43.90%)</b></td><td>3535.40 (-8.99%)</td><td>1096.74 <b>(-22.85%)</b></td><td>511.20 <b>(-22.78%)</b></td><td>432.00 <b>(-33.25%)</b></td><td>1364.33 (-2.64%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>6.48 (n/a)</td><td>4.72 (n/a)</td><td>6.34 (n/a)</td><td>1.08 (n/a)</td><td>2.43 (n/a)</td><td>3884.70 (n/a)</td><td>1421.52 (n/a)</td><td>662.00 (n/a)</td><td>647.20 (n/a)</td><td>1401.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>1.97 (+7.66%)</td><td>0.92 <b>(-35.91%)</b></td><td>0.78 <b>(-45.82%)</b></td><td>0.25 <b>(-67.06%)</b></td><td>0.64 <b>(+49.14%)</b></td><td>2123.60 <b>(+203.59%)</b></td><td>884.20 <b>(+118.34%)</b></td><td>669.10 <b>(+84.53%)</b></td><td>266.50 (-7.11%)</td><td>721.41 <b>(+325.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>1.83 (n/a)</td><td>1.43 (n/a)</td><td>1.45 (n/a)</td><td>0.75 (n/a)</td><td>0.43 (n/a)</td><td>699.50 (n/a)</td><td>404.96 (n/a)</td><td>362.60 (n/a)</td><td>286.90 (n/a)</td><td>169.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.60 (+6.04%)</td><td>1.91 <b>(+23.78%)</b></td><td>2.43 (+4.47%)</td><td>0.33 (+9.76%)</td><td>0.96 (-15.98%)</td><td>3200.20 (-8.90%)</td><td>1013.70 <b>(-38.95%)</b></td><td>432.20 (-4.27%)</td><td>403.40 (-5.70%)</td><td>1225.38 <b>(-26.61%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.45 (n/a)</td><td>1.55 (n/a)</td><td>2.32 (n/a)</td><td>0.30 (n/a)</td><td>1.14 (n/a)</td><td>3512.70 (n/a)</td><td>1660.44 (n/a)</td><td>451.50 (n/a)</td><td>427.80 (n/a)</td><td>1669.62 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.70 (-9.14%)</td><td>2.68 (+7.31%)</td><td>3.36 <b>(+42.37%)</b></td><td>0.96 (-4.05%)</td><td>1.16 (+2.42%)</td><td>2185.80 (+4.22%)</td><td>1010.62 (-3.27%)</td><td>624.60 <b>(-29.76%)</b></td><td>566.70 (+10.06%)</td><td>685.46 (+10.89%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>4.07 (n/a)</td><td>2.49 (n/a)</td><td>2.36 (n/a)</td><td>1.00 (n/a)</td><td>1.14 (n/a)</td><td>2097.30 (n/a)</td><td>1044.76 (n/a)</td><td>889.30 (n/a)</td><td>514.90 (n/a)</td><td>618.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>1.75 <b>(-27.98%)</b></td><td>1.19 <b>(-25.06%)</b></td><td>1.05 <b>(-33.05%)</b></td><td>0.80 (-11.83%)</td><td>0.41 <b>(-24.71%)</b></td><td>659.30 (+13.42%)</td><td>483.64 <b>(+32.46%)</b></td><td>499.60 <b>(+49.36%)</b></td><td>300.30 <b>(+38.83%)</b></td><td>155.66 (+16.55%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>2.42 (n/a)</td><td>1.59 (n/a)</td><td>1.57 (n/a)</td><td>0.90 (n/a)</td><td>0.55 (n/a)</td><td>581.30 (n/a)</td><td>365.12 (n/a)</td><td>334.50 (n/a)</td><td>216.30 (n/a)</td><td>133.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (-1.06%)</td><td>0.08 <b>(-24.43%)</b></td><td>0.08 <b>(-30.09%)</b></td><td>0.05 <b>(-32.81%)</b></td><td>0.03 <b>(+60.86%)</b></td><td>615.90 <b>(+48.80%)</b></td><td>446.04 <b>(+40.98%)</b></td><td>428.20 <b>(+43.02%)</b></td><td>256.70 (+1.06%)</td><td>136.68 <b>(+130.16%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>413.90 (n/a)</td><td>316.38 (n/a)</td><td>299.40 (n/a)</td><td>254.00 (n/a)</td><td>59.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (+6.18%)</td><td>0.12 <b>(+30.24%)</b></td><td>0.12 <b>(+46.19%)</b></td><td>0.08 <b>(+22.43%)</b></td><td>0.03 (-15.57%)</td><td>428.90 (-18.32%)</td><td>292.66 <b>(-25.99%)</b></td><td>273.40 <b>(-31.60%)</b></td><td>229.90 (-5.82%)</td><td>79.56 <b>(-34.57%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>525.10 (n/a)</td><td>395.44 (n/a)</td><td>399.70 (n/a)</td><td>244.10 (n/a)</td><td>121.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.27 <b>(-24.02%)</b></td><td>0.23 <b>(+36.26%)</b></td><td>0.25 <b>(+89.23%)</b></td><td>0.13 <b>(+247.55%)</b></td><td>0.06 <b>(-51.33%)</b></td><td>515.30 <b>(-71.23%)</b></td><td>307.42 <b>(-54.54%)</b></td><td>258.10 <b>(-47.15%)</b></td><td>246.60 <b>(+31.66%)</b></td><td>116.53 <b>(-81.93%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.35 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>1791.10 (n/a)</td><td>676.18 (n/a)</td><td>488.40 (n/a)</td><td>187.30 (n/a)</td><td>645.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.32 (+17.08%)</td><td>0.17 (+1.60%)</td><td>0.13 (-2.35%)</td><td>0.10 (+3.95%)</td><td>0.09 <b>(+25.78%)</b></td><td>624.80 (-3.80%)</td><td>446.96 (+1.71%)</td><td>498.20 (+2.40%)</td><td>207.60 (-14.57%)</td><td>166.06 (+3.26%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>649.50 (n/a)</td><td>439.44 (n/a)</td><td>486.50 (n/a)</td><td>243.00 (n/a)</td><td>160.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.30 (-2.82%)</td><td>0.22 <b>(+30.80%)</b></td><td>0.20 <b>(+43.92%)</b></td><td>0.14 (+16.21%)</td><td>0.06 (-19.60%)</td><td>467.30 (-13.94%)</td><td>323.60 <b>(-27.15%)</b></td><td>334.90 <b>(-30.52%)</b></td><td>219.70 (+2.90%)</td><td>97.64 <b>(-26.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>543.00 (n/a)</td><td>444.22 (n/a)</td><td>482.00 (n/a)</td><td>213.50 (n/a)</td><td>132.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.54 (+13.42%)</td><td>0.38 (-2.79%)</td><td>0.44 (+12.34%)</td><td>0.19 <b>(-30.28%)</b></td><td>0.15 <b>(+99.66%)</b></td><td>689.80 <b>(+43.44%)</b></td><td>402.76 (+16.12%)</td><td>295.10 (-10.98%)</td><td>242.20 (-11.86%)</td><td>190.69 <b>(+142.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>480.90 (n/a)</td><td>346.84 (n/a)</td><td>331.50 (n/a)</td><td>274.80 (n/a)</td><td>78.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.45 (+11.89%)</td><td>0.29 (-6.18%)</td><td>0.27 (-8.60%)</td><td>0.12 <b>(-50.25%)</b></td><td>0.14 <b>(+131.12%)</b></td><td>1128.50 <b>(+101.02%)</b></td><td>592.12 <b>(+33.07%)</b></td><td>487.30 (+9.41%)</td><td>293.60 (-10.60%)</td><td>348.76 <b>(+298.82%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>561.40 (n/a)</td><td>444.96 (n/a)</td><td>445.40 (n/a)</td><td>328.40 (n/a)</td><td>87.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.53 (-2.51%)</td><td>0.43 (-0.70%)</td><td>0.46 (+0.68%)</td><td>0.21 <b>(-22.16%)</b></td><td>0.13 <b>(+28.60%)</b></td><td>622.70 <b>(+28.47%)</b></td><td>339.72 (+7.07%)</td><td>285.10 (-0.70%)</td><td>247.20 (+2.57%)</td><td>159.60 <b>(+65.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>484.70 (n/a)</td><td>317.28 (n/a)</td><td>287.10 (n/a)</td><td>241.00 (n/a)</td><td>96.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (-1.45%)</td><td>0.05 (-2.05%)</td><td>0.04 <b>(-22.50%)</b></td><td>0.03 (-3.39%)</td><td>0.02 (+12.29%)</td><td>584.50 (+3.52%)</td><td>381.78 (+3.98%)</td><td>400.20 <b>(+29.06%)</b></td><td>245.80 (+1.49%)</td><td>137.50 (+9.33%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:11:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>564.60 (n/a)</td><td>367.16 (n/a)</td><td>310.10 (n/a)</td><td>242.20 (n/a)</td><td>125.76 (n/a)</td>
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
