# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (-4.71%)</td><td>0.04 (-7.28%)</td><td>0.04 (-2.20%)</td><td>0.02 (-3.09%)</td><td>0.01 (+7.12%)</td><td>520.10 (+3.19%)</td><td>363.14 (+8.71%)</td><td>300.10 (+2.25%)</td><td>282.20 (+4.95%)</td><td>104.44 (+8.43%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.00 (n/a)</td><td>334.06 (n/a)</td><td>293.50 (n/a)</td><td>268.90 (n/a)</td><td>96.32 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (+13.05%)</td><td>0.05 <b>(+58.67%)</b></td><td>0.05 <b>(+111.74%)</b></td><td>0.03 (+10.95%)</td><td>0.01 (+13.89%)</td><td>482.20 (-9.87%)</td><td>291.02 <b>(-36.56%)</b></td><td>236.50 <b>(-52.77%)</b></td><td>231.30 (-11.51%)</td><td>107.91 (-3.64%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.00 (n/a)</td><td>458.76 (n/a)</td><td>500.70 (n/a)</td><td>261.40 (n/a)</td><td>111.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.06 <b>(+53.21%)</b></td><td>0.04 <b>(+50.91%)</b></td><td>0.04 <b>(+78.52%)</b></td><td>0.02 <b>(+20.76%)</b></td><td>0.02 <b>(+87.55%)</b></td><td>541.40 (-17.19%)</td><td>357.62 <b>(-29.48%)</b></td><td>315.30 <b>(-43.99%)</b></td><td>205.80 <b>(-34.73%)</b></td><td>144.16 (+5.37%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>653.80 (n/a)</td><td>507.10 (n/a)</td><td>562.90 (n/a)</td><td>315.30 (n/a)</td><td>136.82 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (+16.58%)</td><td>0.01 (+18.11%)</td><td>0.01 (+11.48%)</td><td>0.01 <b>(+26.13%)</b></td><td>0.01 (+12.82%)</td><td>548.40 <b>(-20.72%)</b></td><td>414.42 (-17.19%)</td><td>426.60 (-10.28%)</td><td>191.60 (-14.20%)</td><td>135.07 <b>(-26.33%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>691.70 (n/a)</td><td>500.44 (n/a)</td><td>475.50 (n/a)</td><td>223.30 (n/a)</td><td>183.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (+6.90%)</td><td>0.02 (+2.98%)</td><td>0.01 <b>(-31.66%)</b></td><td>0.01 <b>(+49.38%)</b></td><td>0.01 (+17.05%)</td><td>536.40 <b>(-33.05%)</b></td><td>392.56 (-5.67%)</td><td>476.30 <b>(+46.33%)</b></td><td>227.40 (-6.46%)</td><td>149.43 <b>(-33.55%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>801.20 (n/a)</td><td>416.16 (n/a)</td><td>325.50 (n/a)</td><td>243.10 (n/a)</td><td>224.87 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (+14.91%)</td><td>0.02 (+1.02%)</td><td>0.01 (-6.80%)</td><td>0.01 (-9.69%)</td><td>0.01 <b>(+37.89%)</b></td><td>504.60 (+10.73%)</td><td>382.14 (+3.94%)</td><td>430.20 (+7.28%)</td><td>226.20 (-12.97%)</td><td>129.66 <b>(+35.14%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.70 (n/a)</td><td>367.66 (n/a)</td><td>401.00 (n/a)</td><td>259.90 (n/a)</td><td>95.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (-1.19%)</td><td>0.02 <b>(+22.94%)</b></td><td>0.02 <b>(+60.25%)</b></td><td>0.01 <b>(+72.07%)</b></td><td>0.00 <b>(-50.63%)</b></td><td>365.70 <b>(-41.88%)</b></td><td>296.44 <b>(-29.37%)</b></td><td>301.70 <b>(-37.60%)</b></td><td>224.20 (+1.22%)</td><td>53.07 <b>(-69.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.20 (n/a)</td><td>419.68 (n/a)</td><td>483.50 (n/a)</td><td>221.50 (n/a)</td><td>176.16 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (-15.46%)</td><td>0.01 <b>(-38.26%)</b></td><td>0.01 <b>(-47.66%)</b></td><td>0.00 <b>(-83.90%)</b></td><td>0.01 <b>(+123.89%)</b></td><td>1854.70 <b>(+521.13%)</b></td><td>702.10 <b>(+158.71%)</b></td><td>532.60 <b>(+91.03%)</b></td><td>243.30 (+18.28%)</td><td>660.50 <b>(+1630.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>298.60 (n/a)</td><td>271.38 (n/a)</td><td>278.80 (n/a)</td><td>205.70 (n/a)</td><td>38.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.01 <b>(-44.94%)</b></td><td>0.01 <b>(-24.80%)</b></td><td>0.01 (-3.93%)</td><td>0.01 (-17.78%)</td><td>0.00 <b>(-56.43%)</b></td><td>871.00 <b>(+21.61%)</b></td><td>552.90 (+18.38%)</td><td>489.70 (+4.10%)</td><td>373.50 <b>(+81.66%)</b></td><td>202.95 (-5.55%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>716.20 (n/a)</td><td>467.04 (n/a)</td><td>470.40 (n/a)</td><td>205.60 (n/a)</td><td>214.87 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>614.90 (n/a)</td><td>453.20 (n/a)</td><td>468.90 (n/a)</td><td>247.40 (n/a)</td><td>158.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.90 (n/a)</td><td>332.26 (n/a)</td><td>288.40 (n/a)</td><td>225.90 (n/a)</td><td>116.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>371.40 (n/a)</td><td>298.96 (n/a)</td><td>301.90 (n/a)</td><td>248.60 (n/a)</td><td>52.26 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1069.50 (n/a)</td><td>524.78 (n/a)</td><td>483.90 (n/a)</td><td>274.30 (n/a)</td><td>321.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.00 (n/a)</td><td>397.06 (n/a)</td><td>466.70 (n/a)</td><td>243.20 (n/a)</td><td>130.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>742.90 (n/a)</td><td>509.04 (n/a)</td><td>471.80 (n/a)</td><td>353.70 (n/a)</td><td>150.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.50 (n/a)</td><td>374.16 (n/a)</td><td>388.30 (n/a)</td><td>250.70 (n/a)</td><td>111.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.90 (n/a)</td><td>344.26 (n/a)</td><td>295.00 (n/a)</td><td>216.80 (n/a)</td><td>140.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.30 (n/a)</td><td>402.38 (n/a)</td><td>384.70 (n/a)</td><td>244.00 (n/a)</td><td>131.64 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2071.20 (n/a)</td><td>749.38 (n/a)</td><td>407.30 (n/a)</td><td>324.50 (n/a)</td><td>746.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2431.00 (n/a)</td><td>881.08 (n/a)</td><td>545.60 (n/a)</td><td>367.70 (n/a)</td><td>869.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.40 (n/a)</td><td>433.26 (n/a)</td><td>432.40 (n/a)</td><td>280.80 (n/a)</td><td>113.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.70 <b>(+44.31%)</b></td><td>0.45 <b>(+28.61%)</b></td><td>0.37 (-4.66%)</td><td>0.34 <b>(+53.66%)</b></td><td>0.15 <b>(+40.40%)</b></td><td>653.00 <b>(-34.92%)</b></td><td>524.90 <b>(-22.98%)</b></td><td>596.60 (+4.89%)</td><td>318.00 <b>(-30.70%)</b></td><td>144.04 <b>(-37.19%)</b></td><td>29.68 <b>(+44.31%)</b></td><td>19.38 <b>(+28.61%)</b></td><td>15.82 (-4.66%)</td><td>14.45 <b>(+53.66%)</b></td><td>6.47 <b>(+40.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.39 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>1003.40 (n/a)</td><td>681.48 (n/a)</td><td>568.80 (n/a)</td><td>458.90 (n/a)</td><td>229.31 (n/a)</td><td>20.57 (n/a)</td><td>15.07 (n/a)</td><td>16.59 (n/a)</td><td>9.40 (n/a)</td><td>4.61 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.44 <b>(-22.47%)</b></td><td>0.30 <b>(-26.58%)</b></td><td>0.35 (-8.69%)</td><td>0.09 <b>(-69.21%)</b></td><td>0.13 <b>(+34.30%)</b></td><td>2367.70 <b>(+224.74%)</b></td><td>997.10 <b>(+76.17%)</b></td><td>632.80 (+9.50%)</td><td>501.80 <b>(+28.96%)</b></td><td>776.90 <b>(+537.07%)</b></td><td>18.81 <b>(-22.47%)</b></td><td>12.76 <b>(-26.58%)</b></td><td>14.91 (-8.69%)</td><td>3.99 <b>(-69.21%)</b></td><td>5.63 <b>(+34.30%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.57 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.10 (n/a)</td><td>729.10 (n/a)</td><td>565.98 (n/a)</td><td>577.90 (n/a)</td><td>389.10 (n/a)</td><td>121.95 (n/a)</td><td>24.26 (n/a)</td><td>17.38 (n/a)</td><td>16.33 (n/a)</td><td>12.94 (n/a)</td><td>4.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.31 (+1.05%)</td><td>0.30 (-0.10%)</td><td>0.31 (+0.15%)</td><td>0.29 (-2.38%)</td><td>0.01 <b>(+79.56%)</b></td><td>86854.60 (+2.43%)</td><td>83088.32 (+0.15%)</td><td>82506.20 (-0.15%)</td><td>80455.40 (-1.04%)</td><td>2384.65 <b>(+82.62%)</b></td><td>213.53 (+1.05%)</td><td>206.90 (-0.10%)</td><td>208.23 (+0.15%)</td><td>197.80 (-2.38%)</td><td>5.84 <b>(+79.55%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84790.80 (n/a)</td><td>82965.44 (n/a)</td><td>82633.30 (n/a)</td><td>81299.40 (n/a)</td><td>1305.76 (n/a)</td><td>211.32 (n/a)</td><td>207.11 (n/a)</td><td>207.90 (n/a)</td><td>202.61 (n/a)</td><td>3.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>1.02 (-1.41%)</td><td>0.99 (-3.40%)</td><td>1.01 (-0.85%)</td><td>0.93 (-7.78%)</td><td>0.04 <b>(+270.35%)</b></td><td>27032.40 (+8.43%)</td><td>25565.84 (+3.65%)</td><td>24953.90 (+0.86%)</td><td>24643.50 (+1.43%)</td><td>1066.75 <b>(+306.69%)</b></td><td>697.14 (-1.41%)</td><td>672.90 (-3.40%)</td><td>688.46 (-0.85%)</td><td>635.53 (-7.78%)</td><td>27.55 <b>(+270.34%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>0.01 (n/a)</td><td>24930.10 (n/a)</td><td>24664.64 (n/a)</td><td>24740.90 (n/a)</td><td>24295.30 (n/a)</td><td>262.30 (n/a)</td><td>707.13 (n/a)</td><td>696.60 (n/a)</td><td>694.39 (n/a)</td><td>689.12 (n/a)</td><td>7.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>3.37 (-15.20%)</td><td>2.68 (+1.99%)</td><td>2.77 (-3.96%)</td><td>1.89 <b>(+35.91%)</b></td><td>0.67 <b>(-38.74%)</b></td><td>4264.20 <b>(-26.42%)</b></td><td>3177.78 (-11.97%)</td><td>2913.00 (+4.13%)</td><td>2393.70 (+17.93%)</td><td>841.13 <b>(-49.32%)</b></td><td>883.10 (-15.20%)</td><td>702.16 (+1.99%)</td><td>725.70 (-3.96%)</td><td>495.74 <b>(+35.91%)</b></td><td>175.84 <b>(-38.74%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>3.97 (n/a)</td><td>2.63 (n/a)</td><td>2.88 (n/a)</td><td>1.39 (n/a)</td><td>1.09 (n/a)</td><td>5795.60 (n/a)</td><td>3610.06 (n/a)</td><td>2797.50 (n/a)</td><td>2029.80 (n/a)</td><td>1659.70 (n/a)</td><td>1041.45 (n/a)</td><td>688.50 (n/a)</td><td>755.64 (n/a)</td><td>364.75 (n/a)</td><td>287.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.19 (-14.71%)</td><td>0.18 (-9.87%)</td><td>0.19 (-4.26%)</td><td>0.15 (-19.03%)</td><td>0.02 (+3.88%)</td><td>8521.70 <b>(+23.50%)</b></td><td>7040.34 (+11.37%)</td><td>6727.30 (+4.44%)</td><td>6484.40 (+17.25%)</td><td>840.47 <b>(+53.36%)</b></td><td>10.35 (-14.71%)</td><td>9.63 (-9.87%)</td><td>9.98 (-4.26%)</td><td>7.88 (-19.03%)</td><td>1.00 (+3.88%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>6900.30 (n/a)</td><td>6321.66 (n/a)</td><td>6441.00 (n/a)</td><td>5530.30 (n/a)</td><td>548.04 (n/a)</td><td>12.13 (n/a)</td><td>10.68 (n/a)</td><td>10.42 (n/a)</td><td>9.73 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>3.83 (n/a)</td><td>3.68 (n/a)</td><td>3.72 (n/a)</td><td>3.54 (n/a)</td><td>0.13 (n/a)</td><td>3.83 (n/a)</td><td>3.68 (n/a)</td><td>3.72 (n/a)</td><td>3.54 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>7.41 (+9.58%)</td><td>6.99 (+11.36%)</td><td>7.15 (+9.68%)</td><td>6.21 (+9.48%)</td><td>0.49 (+2.09%)</td><td>7.41 (+9.58%)</td><td>6.99 (+11.36%)</td><td>7.14 (+9.68%)</td><td>6.21 (+9.48%)</td><td>0.49 (+2.09%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>6.76 (n/a)</td><td>6.28 (n/a)</td><td>6.52 (n/a)</td><td>5.67 (n/a)</td><td>0.48 (n/a)</td><td>6.76 (n/a)</td><td>6.27 (n/a)</td><td>6.51 (n/a)</td><td>5.67 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>13.15 <b>(+33.56%)</b></td><td>9.54 (+15.05%)</td><td>8.75 (+5.86%)</td><td>7.34 (+11.11%)</td><td>2.21 <b>(+74.25%)</b></td><td>13.14 <b>(+33.56%)</b></td><td>9.53 (+15.05%)</td><td>8.74 (+5.86%)</td><td>7.34 (+11.11%)</td><td>2.21 <b>(+74.25%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>9.84 (n/a)</td><td>8.29 (n/a)</td><td>8.26 (n/a)</td><td>6.61 (n/a)</td><td>1.27 (n/a)</td><td>9.84 (n/a)</td><td>8.28 (n/a)</td><td>8.26 (n/a)</td><td>6.61 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>3.77 (n/a)</td><td>3.50 (n/a)</td><td>3.76 (n/a)</td><td>2.91 (n/a)</td><td>0.39 (n/a)</td><td>3.77 (n/a)</td><td>3.50 (n/a)</td><td>3.75 (n/a)</td><td>2.90 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>7.16 (+0.25%)</td><td>5.99 (+6.27%)</td><td>5.76 (+1.89%)</td><td>5.37 (+16.49%)</td><td>0.69 <b>(-27.64%)</b></td><td>7.15 (+0.25%)</td><td>5.99 (+6.27%)</td><td>5.75 (+1.89%)</td><td>5.37 (+16.49%)</td><td>0.69 <b>(-27.64%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>7.14 (n/a)</td><td>5.64 (n/a)</td><td>5.65 (n/a)</td><td>4.61 (n/a)</td><td>0.96 (n/a)</td><td>7.14 (n/a)</td><td>5.64 (n/a)</td><td>5.65 (n/a)</td><td>4.61 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>9.80 <b>(-31.92%)</b></td><td>8.46 (-9.56%)</td><td>8.13 (-3.42%)</td><td>7.73 (+5.17%)</td><td>0.80 <b>(-71.83%)</b></td><td>9.80 <b>(-31.92%)</b></td><td>8.45 (-9.56%)</td><td>8.12 (-3.42%)</td><td>7.73 (+5.17%)</td><td>0.80 <b>(-71.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>14.40 (n/a)</td><td>9.35 (n/a)</td><td>8.42 (n/a)</td><td>7.35 (n/a)</td><td>2.86 (n/a)</td><td>14.39 (n/a)</td><td>9.34 (n/a)</td><td>8.41 (n/a)</td><td>7.35 (n/a)</td><td>2.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>3.05 (-6.23%)</td><td>1.90 <b>(-25.63%)</b></td><td>1.99 <b>(-25.59%)</b></td><td>1.17 <b>(-30.35%)</b></td><td>0.78 (+16.41%)</td><td>3.05 (-6.23%)</td><td>1.90 <b>(-25.63%)</b></td><td>1.98 <b>(-25.59%)</b></td><td>1.17 <b>(-30.35%)</b></td><td>0.78 (+16.41%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>3.26 (n/a)</td><td>2.56 (n/a)</td><td>2.67 (n/a)</td><td>1.68 (n/a)</td><td>0.67 (n/a)</td><td>3.25 (n/a)</td><td>2.55 (n/a)</td><td>2.67 (n/a)</td><td>1.68 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.64 <b>(+26.68%)</b></td><td>0.38 <b>(+27.45%)</b></td><td>0.35 <b>(+33.38%)</b></td><td>0.07 (-2.96%)</td><td>0.21 (+6.13%)</td><td>0.63 <b>(+26.68%)</b></td><td>0.37 <b>(+27.45%)</b></td><td>0.34 <b>(+33.38%)</b></td><td>0.07 (-2.96%)</td><td>0.21 (+6.13%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.51 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.50 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.52 (-15.05%)</td><td>0.40 (+1.69%)</td><td>0.47 (+8.74%)</td><td>0.08 (+7.69%)</td><td>0.18 (-16.31%)</td><td>0.52 (-15.05%)</td><td>0.39 (+1.69%)</td><td>0.47 (+8.74%)</td><td>0.08 (+7.68%)</td><td>0.18 (-16.31%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.62 (n/a)</td><td>0.39 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td><td>0.61 (n/a)</td><td>0.39 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>2.68 <b>(+51.96%)</b></td><td>1.62 <b>(+27.98%)</b></td><td>1.91 <b>(+27.53%)</b></td><td>0.45 <b>(-29.77%)</b></td><td>1.11 <b>(+99.60%)</b></td><td>2.64 <b>(+51.96%)</b></td><td>1.59 <b>(+27.98%)</b></td><td>1.88 <b>(+27.53%)</b></td><td>0.44 <b>(-29.77%)</b></td><td>1.09 <b>(+99.60%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>1.76 (n/a)</td><td>1.26 (n/a)</td><td>1.49 (n/a)</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>1.74 (n/a)</td><td>1.24 (n/a)</td><td>1.47 (n/a)</td><td>0.63 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>491.70 (n/a)</td><td>431.30 (n/a)</td><td>457.30 (n/a)</td><td>297.80 (n/a)</td><td>79.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.20 (n/a)</td><td>450.64 (n/a)</td><td>493.80 (n/a)</td><td>264.70 (n/a)</td><td>117.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1859.30 (n/a)</td><td>735.96 (n/a)</td><td>532.50 (n/a)</td><td>264.90 (n/a)</td><td>637.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.40 (n/a)</td><td>487.64 (n/a)</td><td>539.00 (n/a)</td><td>228.70 (n/a)</td><td>150.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.50 (n/a)</td><td>388.66 (n/a)</td><td>368.00 (n/a)</td><td>267.70 (n/a)</td><td>111.83 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>469.80 (n/a)</td><td>418.48 (n/a)</td><td>410.20 (n/a)</td><td>336.20 (n/a)</td><td>54.73 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-17.61%)</td><td>0.02 (+8.92%)</td><td>0.03 <b>(+83.32%)</b></td><td>0.02 (+10.89%)</td><td>0.01 <b>(-36.29%)</b></td><td>520.90 (-9.82%)</td><td>363.30 (-17.08%)</td><td>307.30 <b>(-45.45%)</b></td><td>263.40 <b>(+21.38%)</b></td><td>118.15 <b>(-34.95%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.60 (n/a)</td><td>438.14 (n/a)</td><td>563.30 (n/a)</td><td>217.00 (n/a)</td><td>181.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-11.46%)</td><td>0.02 (-16.04%)</td><td>0.03 (-14.61%)</td><td>0.02 <b>(-28.49%)</b></td><td>0.01 <b>(+28.90%)</b></td><td>513.10 <b>(+39.85%)</b></td><td>364.06 <b>(+23.65%)</b></td><td>313.50 (+17.11%)</td><td>274.30 (+12.93%)</td><td>106.03 <b>(+98.95%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>366.90 (n/a)</td><td>294.42 (n/a)</td><td>267.70 (n/a)</td><td>242.90 (n/a)</td><td>53.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (-11.93%)</td><td>0.02 (-12.09%)</td><td>0.02 <b>(-35.11%)</b></td><td>0.02 (+6.28%)</td><td>0.01 <b>(-23.14%)</b></td><td>544.40 (-5.91%)</td><td>403.10 (+6.49%)</td><td>444.10 <b>(+54.09%)</b></td><td>228.90 (+13.54%)</td><td>128.02 <b>(-25.18%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.60 (n/a)</td><td>378.54 (n/a)</td><td>288.20 (n/a)</td><td>201.60 (n/a)</td><td>171.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (+12.86%)</td><td>0.02 (-0.55%)</td><td>0.02 (-3.85%)</td><td>0.01 (-14.27%)</td><td>0.01 <b>(+36.53%)</b></td><td>612.10 (+16.66%)</td><td>426.44 (+6.29%)</td><td>467.40 (+4.01%)</td><td>242.40 (-11.40%)</td><td>154.05 <b>(+41.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.70 (n/a)</td><td>401.20 (n/a)</td><td>449.40 (n/a)</td><td>273.60 (n/a)</td><td>108.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 <b>(+20.32%)</b></td><td>0.02 (-4.25%)</td><td>0.02 (-10.34%)</td><td>0.01 (-4.73%)</td><td>0.01 <b>(+46.04%)</b></td><td>574.60 (+4.95%)</td><td>476.20 (+6.76%)</td><td>506.50 (+11.54%)</td><td>301.20 (-16.91%)</td><td>102.97 <b>(+24.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.50 (n/a)</td><td>446.04 (n/a)</td><td>454.10 (n/a)</td><td>362.50 (n/a)</td><td>82.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 <b>(-59.36%)</b></td><td>0.01 <b>(-39.37%)</b></td><td>0.02 (-10.08%)</td><td>0.01 <b>(-22.78%)</b></td><td>0.00 <b>(-71.65%)</b></td><td>1008.60 <b>(+29.49%)</b></td><td>618.36 <b>(+40.84%)</b></td><td>527.00 (+11.20%)</td><td>474.40 <b>(+146.06%)</b></td><td>221.65 (-2.73%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>778.90 (n/a)</td><td>439.06 (n/a)</td><td>473.90 (n/a)</td><td>192.80 (n/a)</td><td>227.87 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (+6.74%)</td><td>0.02 (+7.58%)</td><td>0.02 (+5.05%)</td><td>0.01 (+8.36%)</td><td>0.01 <b>(+21.92%)</b></td><td>638.80 (-7.71%)</td><td>446.80 (-4.39%)</td><td>428.70 (-4.80%)</td><td>266.30 (-6.33%)</td><td>164.18 (+7.58%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>692.20 (n/a)</td><td>467.32 (n/a)</td><td>450.30 (n/a)</td><td>284.30 (n/a)</td><td>152.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-9.67%)</td><td>0.02 (-10.62%)</td><td>0.02 (-3.79%)</td><td>0.01 (-17.52%)</td><td>0.01 (-9.98%)</td><td>649.80 <b>(+21.23%)</b></td><td>482.60 (+11.91%)</td><td>481.00 (+3.93%)</td><td>270.70 (+10.72%)</td><td>138.17 (+12.83%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.00 (n/a)</td><td>431.24 (n/a)</td><td>462.80 (n/a)</td><td>244.50 (n/a)</td><td>122.46 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-17.66%)</td><td>0.03 (+4.60%)</td><td>0.03 <b>(+53.92%)</b></td><td>0.02 <b>(+20.32%)</b></td><td>0.01 <b>(-47.79%)</b></td><td>536.20 (-16.89%)</td><td>349.22 (-17.37%)</td><td>316.10 <b>(-35.04%)</b></td><td>258.70 <b>(+21.46%)</b></td><td>112.80 <b>(-42.57%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.20 (n/a)</td><td>422.64 (n/a)</td><td>486.60 (n/a)</td><td>213.00 (n/a)</td><td>196.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (+0.36%)</td><td>0.03 (+13.92%)</td><td>0.03 <b>(+68.79%)</b></td><td>0.01 (-10.58%)</td><td>0.01 (-13.34%)</td><td>554.30 (+11.84%)</td><td>317.80 (-14.88%)</td><td>266.30 <b>(-40.76%)</b></td><td>183.30 (-0.33%)</td><td>141.37 (-3.26%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.60 (n/a)</td><td>373.36 (n/a)</td><td>449.50 (n/a)</td><td>183.90 (n/a)</td><td>146.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 <b>(-20.88%)</b></td><td>0.03 (-5.32%)</td><td>0.03 (+14.76%)</td><td>0.02 (+4.59%)</td><td>0.01 <b>(-28.49%)</b></td><td>540.60 (-4.39%)</td><td>327.20 (-1.81%)</td><td>245.80 (-12.87%)</td><td>194.60 <b>(+26.45%)</b></td><td>146.43 (-13.76%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>565.40 (n/a)</td><td>333.24 (n/a)</td><td>282.10 (n/a)</td><td>153.90 (n/a)</td><td>169.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-17.90%)</td><td>0.02 (-16.41%)</td><td>0.02 (-1.94%)</td><td>0.01 <b>(-25.84%)</b></td><td>0.01 (-9.14%)</td><td>628.50 <b>(+34.84%)</b></td><td>485.16 <b>(+21.97%)</b></td><td>460.80 (+1.97%)</td><td>316.70 <b>(+21.81%)</b></td><td>140.21 <b>(+54.23%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>466.10 (n/a)</td><td>397.76 (n/a)</td><td>451.90 (n/a)</td><td>260.00 (n/a)</td><td>90.91 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 <b>(-36.40%)</b></td><td>0.02 (-19.41%)</td><td>0.02 (+5.43%)</td><td>0.01 <b>(+35.21%)</b></td><td>0.00 <b>(-73.49%)</b></td><td>588.30 <b>(-26.04%)</b></td><td>504.12 (+0.21%)</td><td>518.60 (-5.16%)</td><td>382.80 <b>(+57.21%)</b></td><td>82.20 <b>(-66.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>795.40 (n/a)</td><td>503.08 (n/a)</td><td>546.80 (n/a)</td><td>243.50 (n/a)</td><td>247.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-18.33%)</td><td>0.02 (-12.11%)</td><td>0.02 <b>(-23.94%)</b></td><td>0.02 (+8.71%)</td><td>0.01 <b>(-31.09%)</b></td><td>540.70 (-8.01%)</td><td>447.36 (+9.26%)</td><td>502.90 <b>(+31.48%)</b></td><td>298.10 <b>(+22.42%)</b></td><td>105.67 <b>(-21.75%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.80 (n/a)</td><td>409.44 (n/a)</td><td>382.50 (n/a)</td><td>243.50 (n/a)</td><td>135.04 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (+4.34%)</td><td>0.03 (+14.14%)</td><td>0.03 <b>(+45.69%)</b></td><td>0.01 (-9.40%)</td><td>0.01 (+17.39%)</td><td>575.60 (+10.40%)</td><td>344.88 (-9.07%)</td><td>259.70 <b>(-31.37%)</b></td><td>224.90 (-4.18%)</td><td>153.04 (+19.69%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>379.30 (n/a)</td><td>378.40 (n/a)</td><td>234.70 (n/a)</td><td>127.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (-0.32%)</td><td>0.04 (-6.98%)</td><td>0.04 (-10.24%)</td><td>0.02 (-8.36%)</td><td>0.01 (+4.96%)</td><td>529.00 (+9.12%)</td><td>341.06 (+8.56%)</td><td>308.90 (+11.40%)</td><td>248.50 (+0.28%)</td><td>110.26 (+14.00%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>484.80 (n/a)</td><td>314.16 (n/a)</td><td>277.30 (n/a)</td><td>247.80 (n/a)</td><td>96.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-9.47%)</td><td>0.03 (+7.60%)</td><td>0.03 (-3.75%)</td><td>0.02 (+10.11%)</td><td>0.01 <b>(-34.14%)</b></td><td>462.10 (-9.18%)</td><td>307.70 (-12.68%)</td><td>282.90 (+3.89%)</td><td>247.20 (+10.46%)</td><td>87.64 <b>(-34.95%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.80 (n/a)</td><td>352.40 (n/a)</td><td>272.30 (n/a)</td><td>223.80 (n/a)</td><td>134.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 <b>(-42.22%)</b></td><td>0.03 <b>(-25.84%)</b></td><td>0.03 <b>(-20.96%)</b></td><td>0.02 <b>(-23.10%)</b></td><td>0.01 <b>(-44.60%)</b></td><td>560.20 <b>(+30.04%)</b></td><td>400.82 <b>(+29.53%)</b></td><td>360.80 <b>(+26.55%)</b></td><td>267.70 <b>(+73.04%)</b></td><td>141.31 <b>(+21.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>430.80 (n/a)</td><td>309.44 (n/a)</td><td>285.10 (n/a)</td><td>154.70 (n/a)</td><td>116.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-14.70%)</td><td>0.03 (+15.45%)</td><td>0.03 <b>(+39.21%)</b></td><td>0.02 <b>(+42.64%)</b></td><td>0.00 <b>(-56.54%)</b></td><td>393.20 <b>(-29.90%)</b></td><td>291.14 <b>(-23.79%)</b></td><td>279.30 <b>(-28.16%)</b></td><td>246.40 (+17.28%)</td><td>58.85 <b>(-62.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.90 (n/a)</td><td>382.02 (n/a)</td><td>388.80 (n/a)</td><td>210.10 (n/a)</td><td>158.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (-16.92%)</td><td>0.04 (-6.68%)</td><td>0.04 (-0.01%)</td><td>0.02 <b>(-21.39%)</b></td><td>0.01 (-4.77%)</td><td>545.90 <b>(+27.22%)</b></td><td>298.18 (+10.96%)</td><td>241.50 (+0.00%)</td><td>213.00 <b>(+20.41%)</b></td><td>139.49 <b>(+47.11%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>429.10 (n/a)</td><td>268.72 (n/a)</td><td>241.50 (n/a)</td><td>176.90 (n/a)</td><td>94.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (+17.26%)</td><td>0.03 (+8.92%)</td><td>0.03 (+0.02%)</td><td>0.01 <b>(-21.64%)</b></td><td>0.01 <b>(+26.75%)</b></td><td>697.90 <b>(+27.61%)</b></td><td>357.14 (-1.42%)</td><td>287.00 (+0.00%)</td><td>233.30 (-14.70%)</td><td>192.05 <b>(+57.06%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.90 (n/a)</td><td>362.30 (n/a)</td><td>287.00 (n/a)</td><td>273.50 (n/a)</td><td>122.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-1.03%)</td><td>0.02 (-4.24%)</td><td>0.03 (-0.01%)</td><td>0.01 <b>(-33.21%)</b></td><td>0.01 <b>(+25.39%)</b></td><td>813.60 <b>(+49.70%)</b></td><td>439.30 (+13.90%)</td><td>299.80 (+0.00%)</td><td>291.90 (+1.04%)</td><td>226.93 <b>(+82.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.50 (n/a)</td><td>385.70 (n/a)</td><td>299.80 (n/a)</td><td>288.90 (n/a)</td><td>124.64 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (+13.65%)</td><td>0.02 (-6.87%)</td><td>0.02 (-17.02%)</td><td>0.01 (+3.32%)</td><td>0.01 (+7.58%)</td><td>627.20 (-3.21%)</td><td>472.80 (+5.41%)</td><td>528.00 <b>(+20.49%)</b></td><td>207.90 (-11.98%)</td><td>163.34 (-17.22%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.00 (n/a)</td><td>448.54 (n/a)</td><td>438.20 (n/a)</td><td>236.20 (n/a)</td><td>197.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (+11.29%)</td><td>0.03 <b>(+20.29%)</b></td><td>0.03 <b>(+34.56%)</b></td><td>0.02 (-0.47%)</td><td>0.01 <b>(+42.90%)</b></td><td>530.00 (+0.47%)</td><td>372.84 (-14.20%)</td><td>324.70 <b>(-25.70%)</b></td><td>271.20 (-10.14%)</td><td>112.99 <b>(+31.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.50 (n/a)</td><td>434.54 (n/a)</td><td>437.00 (n/a)</td><td>301.80 (n/a)</td><td>85.69 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (-19.76%)</td><td>0.02 (-18.83%)</td><td>0.02 <b>(-48.18%)</b></td><td>0.01 <b>(+183.20%)</b></td><td>0.01 <b>(-47.50%)</b></td><td>683.30 <b>(-64.69%)</b></td><td>461.46 <b>(-28.09%)</b></td><td>478.30 <b>(+93.02%)</b></td><td>284.60 <b>(+24.66%)</b></td><td>169.50 <b>(-76.99%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1935.20 (n/a)</td><td>641.72 (n/a)</td><td>247.80 (n/a)</td><td>228.30 (n/a)</td><td>736.77 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.34 (-16.56%)</td><td>0.23 (-2.97%)</td><td>0.20 (+4.14%)</td><td>0.16 (-1.63%)</td><td>0.07 <b>(-25.15%)</b></td><td>620.80 (+1.65%)</td><td>470.72 (+0.21%)</td><td>502.90 (-3.97%)</td><td>290.00 (+19.83%)</td><td>136.18 (-3.68%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.41 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>610.70 (n/a)</td><td>469.72 (n/a)</td><td>523.70 (n/a)</td><td>242.00 (n/a)</td><td>141.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.37 (-9.20%)</td><td>0.27 (+10.71%)</td><td>0.30 <b>(+57.93%)</b></td><td>0.15 (+6.44%)</td><td>0.09 (-14.68%)</td><td>655.30 (-6.05%)</td><td>413.52 (-11.95%)</td><td>327.60 <b>(-36.68%)</b></td><td>265.40 (+10.17%)</td><td>163.67 (-7.87%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>697.50 (n/a)</td><td>469.62 (n/a)</td><td>517.40 (n/a)</td><td>240.90 (n/a)</td><td>177.65 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.29 <b>(-20.20%)</b></td><td>0.21 (-10.20%)</td><td>0.20 (-4.26%)</td><td>0.17 (+3.71%)</td><td>0.05 <b>(-37.07%)</b></td><td>585.50 (-3.57%)</td><td>491.24 (+7.53%)</td><td>501.70 (+4.43%)</td><td>341.80 <b>(+25.34%)</b></td><td>97.84 <b>(-20.89%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>607.20 (n/a)</td><td>456.84 (n/a)</td><td>480.40 (n/a)</td><td>272.70 (n/a)</td><td>123.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.26 (-10.68%)</td><td>0.17 (-12.21%)</td><td>0.15 (-10.89%)</td><td>0.14 (+18.23%)</td><td>0.05 <b>(-36.11%)</b></td><td>527.70 (-15.43%)</td><td>446.48 (+6.14%)</td><td>486.40 (+12.20%)</td><td>285.80 (+11.95%)</td><td>99.55 <b>(-37.11%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>624.00 (n/a)</td><td>420.64 (n/a)</td><td>433.50 (n/a)</td><td>255.30 (n/a)</td><td>158.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.29 (+8.46%)</td><td>0.24 <b>(+33.41%)</b></td><td>0.25 <b>(+62.22%)</b></td><td>0.15 (+5.27%)</td><td>0.06 (+7.31%)</td><td>504.90 (-5.00%)</td><td>322.16 <b>(-24.91%)</b></td><td>297.00 <b>(-38.37%)</b></td><td>252.10 (-7.82%)</td><td>104.70 (-3.93%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>531.50 (n/a)</td><td>429.06 (n/a)</td><td>481.90 (n/a)</td><td>273.50 (n/a)</td><td>108.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.30 (+18.71%)</td><td>0.18 (-4.63%)</td><td>0.15 (-15.55%)</td><td>0.10 (-7.91%)</td><td>0.09 <b>(+35.59%)</b></td><td>773.90 (+8.60%)</td><td>484.46 (+12.54%)</td><td>496.20 (+18.42%)</td><td>243.10 (-15.77%)</td><td>217.71 <b>(+25.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>712.60 (n/a)</td><td>430.46 (n/a)</td><td>419.00 (n/a)</td><td>288.60 (n/a)</td><td>173.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.37 <b>(-48.69%)</b></td><td>0.26 <b>(-25.77%)</b></td><td>0.25 (-6.61%)</td><td>0.20 (+10.08%)</td><td>0.06 <b>(-71.28%)</b></td><td>641.40 (-9.15%)</td><td>523.18 (+8.56%)</td><td>533.10 (+7.07%)</td><td>352.10 <b>(+94.85%)</b></td><td>105.98 <b>(-53.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.73 (n/a)</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.23 (n/a)</td><td>706.00 (n/a)</td><td>481.94 (n/a)</td><td>497.90 (n/a)</td><td>180.70 (n/a)</td><td>227.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.43 (+3.66%)</td><td>0.26 (-18.91%)</td><td>0.22 <b>(-43.36%)</b></td><td>0.17 <b>(+213.54%)</b></td><td>0.11 <b>(-26.83%)</b></td><td>790.50 <b>(-68.11%)</b></td><td>577.08 <b>(-24.93%)</b></td><td>590.60 <b>(+76.56%)</b></td><td>307.80 (-3.51%)</td><td>213.62 <b>(-77.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.39 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>2478.50 (n/a)</td><td>768.68 (n/a)</td><td>334.50 (n/a)</td><td>319.00 (n/a)</td><td>956.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.43 <b>(-40.69%)</b></td><td>0.29 (-5.75%)</td><td>0.40 <b>(+86.41%)</b></td><td>0.07 <b>(-55.74%)</b></td><td>0.16 <b>(-30.04%)</b></td><td>1839.60 <b>(+125.94%)</b></td><td>725.98 <b>(+29.16%)</b></td><td>331.70 <b>(-46.36%)</b></td><td>307.40 <b>(+68.53%)</b></td><td>658.64 <b>(+179.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.72 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.23 (n/a)</td><td>814.20 (n/a)</td><td>562.08 (n/a)</td><td>618.40 (n/a)</td><td>182.40 (n/a)</td><td>236.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+26.67%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+18.32%)</td><td>22648.63 (-0.14%)</td><td>13884.09 <b>(-20.43%)</b></td><td>15557.60 <b>(-24.59%)</b></td><td>6506.70 (-8.12%)</td><td>6850.41 (+4.03%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22679.90 (n/a)</td><td>17449.61 (n/a)</td><td>20630.46 (n/a)</td><td>7081.85 (n/a)</td><td>6585.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.00 <b>(+57.14%)</b></td><td>0.00 <b>(+82.61%)</b></td><td>0.00 <b>(+175.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+166.67%)</b></td><td>22356.06 (-0.83%)</td><td>12456.27 <b>(-35.76%)</b></td><td>7609.99 <b>(-64.77%)</b></td><td>7424.25 <b>(-38.91%)</b></td><td>7012.19 <b>(+64.19%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22543.16 (n/a)</td><td>19389.33 (n/a)</td><td>21599.96 (n/a)</td><td>12152.16 (n/a)</td><td>4270.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.15 (+9.36%)</td><td>0.12 <b>(+32.88%)</b></td><td>0.13 <b>(+40.88%)</b></td><td>0.07 (+0.74%)</td><td>0.03 (+13.59%)</td><td>30665.29 (-0.74%)</td><td>18295.30 <b>(-23.52%)</b></td><td>15881.58 <b>(-29.07%)</b></td><td>13695.18 (-8.61%)</td><td>6982.78 (+9.01%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30892.46 (n/a)</td><td>23920.24 (n/a)</td><td>22389.67 (n/a)</td><td>14984.81 (n/a)</td><td>6405.75 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>1.71 <b>(-23.78%)</b></td><td>1.09 <b>(-28.90%)</b></td><td>1.01 <b>(-34.65%)</b></td><td>0.72 (+8.21%)</td><td>0.37 <b>(-34.43%)</b></td><td>724.10 (-7.58%)</td><td>519.18 <b>(+29.23%)</b></td><td>520.10 <b>(+53.02%)</b></td><td>307.40 <b>(+31.20%)</b></td><td>150.60 <b>(-30.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>2.24 (n/a)</td><td>1.54 (n/a)</td><td>1.54 (n/a)</td><td>0.67 (n/a)</td><td>0.56 (n/a)</td><td>783.50 (n/a)</td><td>401.74 (n/a)</td><td>339.90 (n/a)</td><td>234.30 (n/a)</td><td>217.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>2.38 (-14.02%)</td><td>1.36 <b>(-25.09%)</b></td><td>1.37 <b>(-22.61%)</b></td><td>0.30 (-0.32%)</td><td>0.78 <b>(-20.01%)</b></td><td>3504.30 (+0.31%)</td><td>1273.28 (+15.51%)</td><td>766.80 <b>(+29.22%)</b></td><td>441.30 (+16.28%)</td><td>1267.21 (-5.52%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>2.76 (n/a)</td><td>1.81 (n/a)</td><td>1.77 (n/a)</td><td>0.30 (n/a)</td><td>0.97 (n/a)</td><td>3493.30 (n/a)</td><td>1102.30 (n/a)</td><td>593.40 (n/a)</td><td>379.50 (n/a)</td><td>1341.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.58 (-2.67%)</td><td>1.21 (+5.65%)</td><td>1.29 <b>(+41.89%)</b></td><td>0.66 <b>(-20.05%)</b></td><td>0.38 (-2.53%)</td><td>792.90 <b>(+25.08%)</b></td><td>479.12 (-3.80%)</td><td>406.80 <b>(-29.52%)</b></td><td>331.10 (+2.76%)</td><td>189.18 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.63 (n/a)</td><td>1.14 (n/a)</td><td>0.91 (n/a)</td><td>0.83 (n/a)</td><td>0.38 (n/a)</td><td>633.90 (n/a)</td><td>498.02 (n/a)</td><td>577.20 (n/a)</td><td>322.20 (n/a)</td><td>149.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>1.99 <b>(-22.97%)</b></td><td>1.24 (-18.34%)</td><td>1.01 <b>(-30.41%)</b></td><td>0.76 (+0.43%)</td><td>0.49 <b>(-28.97%)</b></td><td>688.00 (-0.43%)</td><td>474.58 (+16.07%)</td><td>520.40 <b>(+43.72%)</b></td><td>264.00 <b>(+29.79%)</b></td><td>166.68 (-10.79%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>2.58 (n/a)</td><td>1.52 (n/a)</td><td>1.45 (n/a)</td><td>0.76 (n/a)</td><td>0.69 (n/a)</td><td>691.00 (n/a)</td><td>408.86 (n/a)</td><td>362.10 (n/a)</td><td>203.40 (n/a)</td><td>186.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.75 (-15.44%)</td><td>1.32 (-0.50%)</td><td>1.36 <b>(+22.47%)</b></td><td>0.77 (-19.20%)</td><td>0.36 <b>(-21.75%)</b></td><td>678.10 <b>(+23.76%)</b></td><td>430.02 (-0.09%)</td><td>385.10 (-18.34%)</td><td>300.10 (+18.29%)</td><td>146.96 (+19.46%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.07 (n/a)</td><td>1.32 (n/a)</td><td>1.11 (n/a)</td><td>0.96 (n/a)</td><td>0.46 (n/a)</td><td>547.90 (n/a)</td><td>430.40 (n/a)</td><td>471.60 (n/a)</td><td>253.70 (n/a)</td><td>123.02 (n/a)</td>
</tr>
</tbody>
</table>


</details>
