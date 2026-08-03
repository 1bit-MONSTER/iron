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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (-10.31%)</td><td>0.03 (-1.60%)</td><td>0.04 <b>(+26.56%)</b></td><td>0.02 (+0.42%)</td><td>0.01 (-9.04%)</td><td>607.30 (-0.43%)</td><td>407.28 (+1.28%)</td><td>295.60 <b>(-20.98%)</b></td><td>271.70 (+11.49%)</td><td>165.76 (+4.53%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.90 (n/a)</td><td>402.14 (n/a)</td><td>374.10 (n/a)</td><td>243.70 (n/a)</td><td>158.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (-1.63%)</td><td>0.04 <b>(+24.10%)</b></td><td>0.05 (+10.27%)</td><td>0.02 <b>(+312.99%)</b></td><td>0.01 <b>(-34.74%)</b></td><td>581.10 <b>(-75.79%)</b></td><td>328.90 <b>(-55.82%)</b></td><td>263.60 (-9.32%)</td><td>235.70 (+1.68%)</td><td>144.22 <b>(-84.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2400.00 (n/a)</td><td>744.42 (n/a)</td><td>290.70 (n/a)</td><td>231.80 (n/a)</td><td>932.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 <b>(+21.45%)</b></td><td>0.03 (+6.04%)</td><td>0.03 (+13.67%)</td><td>0.02 (+1.18%)</td><td>0.01 (+12.22%)</td><td>646.60 (-1.16%)</td><td>442.68 (-5.28%)</td><td>466.80 (-12.04%)</td><td>239.80 (-17.65%)</td><td>157.79 (-4.30%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>654.20 (n/a)</td><td>467.36 (n/a)</td><td>530.70 (n/a)</td><td>291.20 (n/a)</td><td>164.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 <b>(+20.63%)</b></td><td>0.02 (+4.98%)</td><td>0.02 <b>(+54.03%)</b></td><td>0.01 <b>(-36.36%)</b></td><td>0.01 <b>(+43.77%)</b></td><td>810.10 <b>(+57.12%)</b></td><td>433.48 (+10.19%)</td><td>295.60 <b>(-35.09%)</b></td><td>203.20 (-17.10%)</td><td>250.85 <b>(+96.71%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>515.60 (n/a)</td><td>393.38 (n/a)</td><td>455.40 (n/a)</td><td>245.10 (n/a)</td><td>127.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (+2.49%)</td><td>0.02 (-2.18%)</td><td>0.02 (-5.34%)</td><td>0.01 (+15.62%)</td><td>0.00 (-7.57%)</td><td>447.00 (-13.51%)</td><td>334.62 (+0.20%)</td><td>301.60 (+5.64%)</td><td>226.30 (-2.46%)</td><td>99.85 (-16.91%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>516.80 (n/a)</td><td>333.94 (n/a)</td><td>285.50 (n/a)</td><td>232.00 (n/a)</td><td>120.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (-13.21%)</td><td>0.02 (-11.53%)</td><td>0.02 (-0.81%)</td><td>0.01 (-2.45%)</td><td>0.01 (-13.89%)</td><td>496.00 (+2.50%)</td><td>334.70 (+11.80%)</td><td>290.70 (+0.80%)</td><td>224.10 (+15.22%)</td><td>110.49 (-0.34%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>483.90 (n/a)</td><td>299.38 (n/a)</td><td>288.40 (n/a)</td><td>194.50 (n/a)</td><td>110.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 <b>(-26.98%)</b></td><td>0.02 (-15.89%)</td><td>0.02 (-9.55%)</td><td>0.01 (-18.32%)</td><td>0.00 <b>(-31.47%)</b></td><td>588.00 <b>(+22.42%)</b></td><td>376.12 (+16.52%)</td><td>303.00 (+10.54%)</td><td>286.10 <b>(+36.96%)</b></td><td>127.02 (+12.25%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>480.30 (n/a)</td><td>322.80 (n/a)</td><td>274.10 (n/a)</td><td>208.90 (n/a)</td><td>113.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (+7.52%)</td><td>0.02 <b>(+33.67%)</b></td><td>0.02 <b>(+57.69%)</b></td><td>0.01 <b>(+24.88%)</b></td><td>0.00 (-10.70%)</td><td>466.90 (-19.93%)</td><td>312.86 <b>(-27.92%)</b></td><td>307.60 <b>(-36.59%)</b></td><td>221.70 (-7.01%)</td><td>94.56 <b>(-30.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>434.04 (n/a)</td><td>485.10 (n/a)</td><td>238.40 (n/a)</td><td>136.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 <b>(+54.51%)</b></td><td>0.01 <b>(+28.03%)</b></td><td>0.01 (+9.92%)</td><td>0.01 (+6.40%)</td><td>0.01 <b>(+115.91%)</b></td><td>589.70 (-6.01%)</td><td>419.24 (-16.72%)</td><td>452.80 (-9.02%)</td><td>244.50 <b>(-35.28%)</b></td><td>140.81 <b>(+27.86%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.40 (n/a)</td><td>503.42 (n/a)</td><td>497.70 (n/a)</td><td>377.80 (n/a)</td><td>110.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.60 (n/a)</td><td>430.32 (n/a)</td><td>499.60 (n/a)</td><td>267.50 (n/a)</td><td>138.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.60 (n/a)</td><td>365.68 (n/a)</td><td>292.40 (n/a)</td><td>269.70 (n/a)</td><td>115.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>687.10 (n/a)</td><td>482.44 (n/a)</td><td>541.70 (n/a)</td><td>262.10 (n/a)</td><td>168.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>613.90 (n/a)</td><td>425.18 (n/a)</td><td>423.50 (n/a)</td><td>267.00 (n/a)</td><td>147.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.00 (n/a)</td><td>463.54 (n/a)</td><td>508.20 (n/a)</td><td>293.40 (n/a)</td><td>123.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>615.70 (n/a)</td><td>508.70 (n/a)</td><td>507.00 (n/a)</td><td>436.80 (n/a)</td><td>67.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.50 (n/a)</td><td>337.04 (n/a)</td><td>296.20 (n/a)</td><td>231.70 (n/a)</td><td>115.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.50 (n/a)</td><td>378.90 (n/a)</td><td>293.10 (n/a)</td><td>239.90 (n/a)</td><td>165.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>460.50 (n/a)</td><td>290.98 (n/a)</td><td>243.10 (n/a)</td><td>213.50 (n/a)</td><td>99.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.40 (n/a)</td><td>367.10 (n/a)</td><td>303.80 (n/a)</td><td>288.60 (n/a)</td><td>107.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.10 (n/a)</td><td>372.12 (n/a)</td><td>384.10 (n/a)</td><td>243.60 (n/a)</td><td>80.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1963.00 (n/a)</td><td>795.04 (n/a)</td><td>531.80 (n/a)</td><td>337.00 (n/a)</td><td>662.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.53 (+19.88%)</td><td>0.41 (+18.49%)</td><td>0.41 (+8.99%)</td><td>0.28 <b>(+63.29%)</b></td><td>0.10 (-7.15%)</td><td>788.10 <b>(-38.76%)</b></td><td>563.26 <b>(-20.90%)</b></td><td>542.00 (-8.24%)</td><td>417.70 (-16.58%)</td><td>143.47 <b>(-55.72%)</b></td><td>22.60 (+19.88%)</td><td>17.57 (+18.49%)</td><td>17.41 (+8.99%)</td><td>11.97 <b>(+63.29%)</b></td><td>4.07 (-7.15%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>1286.90 (n/a)</td><td>712.10 (n/a)</td><td>590.70 (n/a)</td><td>500.70 (n/a)</td><td>324.04 (n/a)</td><td>18.85 (n/a)</td><td>14.83 (n/a)</td><td>15.98 (n/a)</td><td>7.33 (n/a)</td><td>4.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.48 (-15.91%)</td><td>0.39 <b>(-20.07%)</b></td><td>0.35 <b>(-23.51%)</b></td><td>0.28 <b>(-31.42%)</b></td><td>0.09 <b>(+37.96%)</b></td><td>784.10 <b>(+45.82%)</b></td><td>597.72 <b>(+28.56%)</b></td><td>626.10 <b>(+30.74%)</b></td><td>462.10 (+18.91%)</td><td>134.02 <b>(+131.49%)</b></td><td>20.42 (-15.91%)</td><td>16.43 <b>(-20.07%)</b></td><td>15.07 <b>(-23.51%)</b></td><td>12.04 <b>(-31.42%)</b></td><td>3.64 <b>(+37.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.57 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.06 (n/a)</td><td>537.70 (n/a)</td><td>464.92 (n/a)</td><td>478.90 (n/a)</td><td>388.60 (n/a)</td><td>57.89 (n/a)</td><td>24.29 (n/a)</td><td>20.56 (n/a)</td><td>19.71 (n/a)</td><td>17.55 (n/a)</td><td>2.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.31 (-0.81%)</td><td>0.31 (+1.93%)</td><td>0.31 (+1.27%)</td><td>0.30 (+4.63%)</td><td>0.00 <b>(-79.14%)</b></td><td>83350.90 (-4.42%)</td><td>82467.46 (-1.96%)</td><td>82282.50 (-1.26%)</td><td>82115.60 (+0.82%)</td><td>501.45 <b>(-79.92%)</b></td><td>209.22 (-0.81%)</td><td>208.33 (+1.93%)</td><td>208.79 (+1.27%)</td><td>206.12 (+4.63%)</td><td>1.26 <b>(-79.14%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>87207.00 (n/a)</td><td>84118.96 (n/a)</td><td>83330.40 (n/a)</td><td>81447.40 (n/a)</td><td>2497.14 (n/a)</td><td>210.93 (n/a)</td><td>204.38 (n/a)</td><td>206.17 (n/a)</td><td>197.00 (n/a)</td><td>6.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>1.02 (-0.86%)</td><td>1.00 (-1.36%)</td><td>1.01 (-1.22%)</td><td>0.96 (-2.93%)</td><td>0.03 <b>(+43.86%)</b></td><td>26319.80 (+3.02%)</td><td>25168.86 (+1.41%)</td><td>24964.50 (+1.23%)</td><td>24697.80 (+0.87%)</td><td>660.22 <b>(+50.02%)</b></td><td>695.60 (-0.86%)</td><td>682.95 (-1.36%)</td><td>688.17 (-1.22%)</td><td>652.74 (-2.93%)</td><td>17.38 <b>(+43.86%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.99 (n/a)</td><td>0.02 (n/a)</td><td>25547.30 (n/a)</td><td>24818.40 (n/a)</td><td>24660.70 (n/a)</td><td>24485.40 (n/a)</td><td>440.09 (n/a)</td><td>701.64 (n/a)</td><td>692.39 (n/a)</td><td>696.65 (n/a)</td><td>672.47 (n/a)</td><td>12.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>3.83 (-1.32%)</td><td>2.37 (+10.04%)</td><td>2.04 <b>(+27.38%)</b></td><td>1.52 (+9.97%)</td><td>0.91 (-11.61%)</td><td>5300.10 (-9.07%)</td><td>3756.70 (-12.49%)</td><td>3956.90 <b>(-21.50%)</b></td><td>2106.20 (+1.34%)</td><td>1225.67 (-18.86%)</td><td>1003.68 (-1.32%)</td><td>622.60 (+10.04%)</td><td>534.24 <b>(+27.38%)</b></td><td>398.85 (+9.97%)</td><td>238.25 (-11.61%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>3.88 (n/a)</td><td>2.16 (n/a)</td><td>1.60 (n/a)</td><td>1.38 (n/a)</td><td>1.03 (n/a)</td><td>5828.60 (n/a)</td><td>4292.96 (n/a)</td><td>5040.40 (n/a)</td><td>2078.30 (n/a)</td><td>1510.56 (n/a)</td><td>1017.12 (n/a)</td><td>565.79 (n/a)</td><td>419.40 (n/a)</td><td>362.68 (n/a)</td><td>269.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.30 (+15.00%)</td><td>0.21 (+0.88%)</td><td>0.20 (-4.22%)</td><td>0.18 (-2.28%)</td><td>0.05 <b>(+64.31%)</b></td><td>6964.20 (+2.34%)</td><td>6059.96 (+1.03%)</td><td>6342.80 (+4.40%)</td><td>4180.90 (-13.04%)</td><td>1095.64 <b>(+43.07%)</b></td><td>16.05 (+15.00%)</td><td>11.45 (+0.88%)</td><td>10.58 (-4.22%)</td><td>9.64 (-2.28%)</td><td>2.62 <b>(+64.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>6805.10 (n/a)</td><td>5997.92 (n/a)</td><td>6075.20 (n/a)</td><td>4807.90 (n/a)</td><td>765.79 (n/a)</td><td>13.96 (n/a)</td><td>11.35 (n/a)</td><td>11.05 (n/a)</td><td>9.86 (n/a)</td><td>1.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.55 (n/a)</td><td>3.41 (n/a)</td><td>0.16 (n/a)</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.54 (n/a)</td><td>3.41 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>5.67 <b>(-23.68%)</b></td><td>5.22 <b>(-22.32%)</b></td><td>5.28 <b>(-24.77%)</b></td><td>4.75 (-18.09%)</td><td>0.44 <b>(-42.56%)</b></td><td>5.66 <b>(-23.68%)</b></td><td>5.21 <b>(-22.32%)</b></td><td>5.28 <b>(-24.77%)</b></td><td>4.75 (-18.09%)</td><td>0.44 <b>(-42.56%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>7.43 (n/a)</td><td>6.72 (n/a)</td><td>7.02 (n/a)</td><td>5.80 (n/a)</td><td>0.77 (n/a)</td><td>7.42 (n/a)</td><td>6.71 (n/a)</td><td>7.01 (n/a)</td><td>5.80 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>12.92 (-3.70%)</td><td>9.90 (+1.17%)</td><td>9.95 <b>(+21.42%)</b></td><td>6.41 (-12.34%)</td><td>2.49 (-7.30%)</td><td>12.91 (-3.70%)</td><td>9.90 (+1.17%)</td><td>9.95 <b>(+21.42%)</b></td><td>6.41 (-12.34%)</td><td>2.49 (-7.30%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>13.42 (n/a)</td><td>9.79 (n/a)</td><td>8.20 (n/a)</td><td>7.32 (n/a)</td><td>2.69 (n/a)</td><td>13.41 (n/a)</td><td>9.78 (n/a)</td><td>8.19 (n/a)</td><td>7.31 (n/a)</td><td>2.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>3.83 (n/a)</td><td>3.57 (n/a)</td><td>3.66 (n/a)</td><td>2.97 (n/a)</td><td>0.34 (n/a)</td><td>3.83 (n/a)</td><td>3.56 (n/a)</td><td>3.66 (n/a)</td><td>2.97 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>7.56 (-1.07%)</td><td>6.91 (+5.07%)</td><td>6.87 (+6.58%)</td><td>6.04 (+6.33%)</td><td>0.65 <b>(-28.10%)</b></td><td>7.55 (-1.07%)</td><td>6.90 (+5.07%)</td><td>6.87 (+6.58%)</td><td>6.03 (+6.33%)</td><td>0.65 <b>(-28.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>7.64 (n/a)</td><td>6.57 (n/a)</td><td>6.45 (n/a)</td><td>5.68 (n/a)</td><td>0.90 (n/a)</td><td>7.63 (n/a)</td><td>6.57 (n/a)</td><td>6.44 (n/a)</td><td>5.67 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>13.89 (-1.74%)</td><td>12.27 <b>(+36.39%)</b></td><td>12.52 <b>(+58.04%)</b></td><td>9.51 <b>(+31.19%)</b></td><td>1.82 <b>(-37.64%)</b></td><td>13.89 (-1.74%)</td><td>12.27 <b>(+36.39%)</b></td><td>12.52 <b>(+58.04%)</b></td><td>9.50 <b>(+31.19%)</b></td><td>1.82 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>14.14 (n/a)</td><td>9.00 (n/a)</td><td>7.92 (n/a)</td><td>7.25 (n/a)</td><td>2.92 (n/a)</td><td>14.13 (n/a)</td><td>8.99 (n/a)</td><td>7.92 (n/a)</td><td>7.24 (n/a)</td><td>2.91 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>2.76 <b>(+59.46%)</b></td><td>1.47 (+14.38%)</td><td>1.25 <b>(+21.19%)</b></td><td>0.97 (-3.41%)</td><td>0.73 <b>(+99.81%)</b></td><td>2.76 <b>(+59.46%)</b></td><td>1.47 (+14.38%)</td><td>1.25 <b>(+21.19%)</b></td><td>0.97 (-3.41%)</td><td>0.73 <b>(+99.81%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.73 (n/a)</td><td>1.29 (n/a)</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>0.37 (n/a)</td><td>1.73 (n/a)</td><td>1.28 (n/a)</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.45 (-9.66%)</td><td>0.23 (-11.77%)</td><td>0.18 <b>(+33.77%)</b></td><td>0.07 (-1.75%)</td><td>0.17 <b>(-23.74%)</b></td><td>0.45 (-9.66%)</td><td>0.22 (-11.77%)</td><td>0.18 <b>(+33.77%)</b></td><td>0.07 (-1.75%)</td><td>0.17 <b>(-23.74%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.50 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td><td>0.50 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.44 <b>(-37.27%)</b></td><td>0.30 (-11.01%)</td><td>0.29 (-10.32%)</td><td>0.08 (-4.31%)</td><td>0.15 <b>(-41.67%)</b></td><td>0.43 <b>(-37.27%)</b></td><td>0.30 (-11.01%)</td><td>0.28 (-10.32%)</td><td>0.08 (-4.31%)</td><td>0.14 <b>(-41.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.69 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.69 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>3.03 <b>(+42.38%)</b></td><td>1.91 <b>(+24.78%)</b></td><td>1.84 (+16.88%)</td><td>1.03 <b>(+23.19%)</b></td><td>0.72 <b>(+47.15%)</b></td><td>2.98 <b>(+42.38%)</b></td><td>1.88 <b>(+24.78%)</b></td><td>1.81 (+16.88%)</td><td>1.01 <b>(+23.19%)</b></td><td>0.71 <b>(+47.15%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>2.13 (n/a)</td><td>1.53 (n/a)</td><td>1.57 (n/a)</td><td>0.83 (n/a)</td><td>0.49 (n/a)</td><td>2.10 (n/a)</td><td>1.51 (n/a)</td><td>1.55 (n/a)</td><td>0.82 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.70 (n/a)</td><td>412.24 (n/a)</td><td>456.70 (n/a)</td><td>274.00 (n/a)</td><td>117.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.40 (n/a)</td><td>427.26 (n/a)</td><td>416.90 (n/a)</td><td>206.30 (n/a)</td><td>180.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2475.90 (n/a)</td><td>798.30 (n/a)</td><td>414.60 (n/a)</td><td>273.80 (n/a)</td><td>944.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.30 (n/a)</td><td>435.38 (n/a)</td><td>472.00 (n/a)</td><td>267.80 (n/a)</td><td>150.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.60 (n/a)</td><td>383.38 (n/a)</td><td>280.90 (n/a)</td><td>246.50 (n/a)</td><td>159.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.10 (n/a)</td><td>478.92 (n/a)</td><td>501.90 (n/a)</td><td>346.60 (n/a)</td><td>89.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 <b>(-28.66%)</b></td><td>0.02 <b>(-31.91%)</b></td><td>0.02 <b>(-44.03%)</b></td><td>0.01 <b>(-28.23%)</b></td><td>0.01 (-9.87%)</td><td>633.00 <b>(+39.34%)</b></td><td>488.92 <b>(+52.52%)</b></td><td>537.00 <b>(+78.64%)</b></td><td>299.60 <b>(+40.20%)</b></td><td>158.15 <b>(+79.59%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>454.30 (n/a)</td><td>320.56 (n/a)</td><td>300.60 (n/a)</td><td>213.70 (n/a)</td><td>88.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (+13.18%)</td><td>0.03 (-4.29%)</td><td>0.03 (+5.97%)</td><td>0.01 <b>(-46.55%)</b></td><td>0.01 <b>(+256.85%)</b></td><td>547.00 <b>(+87.07%)</b></td><td>309.42 (+16.07%)</td><td>255.10 (-5.62%)</td><td>215.10 (-11.63%)</td><td>136.08 <b>(+529.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>292.40 (n/a)</td><td>266.58 (n/a)</td><td>270.30 (n/a)</td><td>243.40 (n/a)</td><td>21.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (+6.60%)</td><td>0.03 (+10.27%)</td><td>0.03 (+15.61%)</td><td>0.02 (+9.62%)</td><td>0.01 <b>(+27.52%)</b></td><td>400.40 (-8.77%)</td><td>306.56 (-7.96%)</td><td>262.20 (-13.52%)</td><td>237.90 (-6.19%)</td><td>80.57 (+9.18%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.90 (n/a)</td><td>333.08 (n/a)</td><td>303.20 (n/a)</td><td>253.60 (n/a)</td><td>73.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (+14.15%)</td><td>0.03 (+15.77%)</td><td>0.03 <b>(+60.44%)</b></td><td>0.02 (+6.85%)</td><td>0.01 (+6.21%)</td><td>479.80 (-6.42%)</td><td>347.66 (-13.86%)</td><td>286.10 <b>(-37.67%)</b></td><td>226.00 (-12.40%)</td><td>115.56 (-7.88%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.70 (n/a)</td><td>403.62 (n/a)</td><td>459.00 (n/a)</td><td>258.00 (n/a)</td><td>125.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 <b>(+20.01%)</b></td><td>0.03 (+5.27%)</td><td>0.03 (-4.49%)</td><td>0.02 <b>(+40.61%)</b></td><td>0.01 <b>(+21.97%)</b></td><td>459.60 <b>(-28.88%)</b></td><td>333.20 (-6.46%)</td><td>300.70 (+4.70%)</td><td>223.30 (-16.68%)</td><td>114.40 <b>(-29.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.20 (n/a)</td><td>356.22 (n/a)</td><td>287.20 (n/a)</td><td>268.00 (n/a)</td><td>162.38 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (+6.04%)</td><td>0.02 (-1.36%)</td><td>0.01 (-8.38%)</td><td>0.01 <b>(-43.36%)</b></td><td>0.01 <b>(+47.71%)</b></td><td>1001.30 <b>(+76.56%)</b></td><td>530.62 (+19.47%)</td><td>563.10 (+9.15%)</td><td>257.00 (-5.69%)</td><td>303.27 <b>(+119.28%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>444.16 (n/a)</td><td>515.90 (n/a)</td><td>272.50 (n/a)</td><td>138.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (-9.10%)</td><td>0.02 (-11.19%)</td><td>0.02 (-15.02%)</td><td>0.01 (-7.99%)</td><td>0.01 (+9.40%)</td><td>607.80 (+8.69%)</td><td>418.02 (+15.00%)</td><td>383.90 (+17.69%)</td><td>286.40 (+9.98%)</td><td>139.56 <b>(+21.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.20 (n/a)</td><td>363.50 (n/a)</td><td>326.20 (n/a)</td><td>260.40 (n/a)</td><td>115.10 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 <b>(+37.37%)</b></td><td>0.02 (+9.73%)</td><td>0.02 (+2.32%)</td><td>0.01 (-7.58%)</td><td>0.01 <b>(+60.75%)</b></td><td>675.40 (+8.20%)</td><td>462.30 (-4.35%)</td><td>484.00 (-2.28%)</td><td>260.20 <b>(-27.22%)</b></td><td>154.49 <b>(+27.23%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>624.20 (n/a)</td><td>483.34 (n/a)</td><td>495.30 (n/a)</td><td>357.50 (n/a)</td><td>121.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 <b>(+45.17%)</b></td><td>0.02 <b>(+26.21%)</b></td><td>0.02 (+9.81%)</td><td>0.00 <b>(-67.84%)</b></td><td>0.02 <b>(+138.86%)</b></td><td>1977.00 <b>(+210.95%)</b></td><td>650.86 <b>(+42.46%)</b></td><td>423.40 (-8.95%)</td><td>186.10 <b>(-31.10%)</b></td><td>750.31 <b>(+457.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.80 (n/a)</td><td>456.88 (n/a)</td><td>465.00 (n/a)</td><td>270.10 (n/a)</td><td>134.60 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (-19.37%)</td><td>0.02 (-13.84%)</td><td>0.02 (-8.25%)</td><td>0.01 <b>(-29.86%)</b></td><td>0.01 (+3.29%)</td><td>602.10 <b>(+42.58%)</b></td><td>421.72 <b>(+24.37%)</b></td><td>415.90 (+8.99%)</td><td>241.20 <b>(+24.01%)</b></td><td>176.36 <b>(+80.93%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>422.30 (n/a)</td><td>339.08 (n/a)</td><td>381.60 (n/a)</td><td>194.50 (n/a)</td><td>97.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (-17.62%)</td><td>0.02 <b>(-28.00%)</b></td><td>0.02 <b>(-35.06%)</b></td><td>0.01 (-7.97%)</td><td>0.01 <b>(-30.92%)</b></td><td>549.40 (+8.66%)</td><td>433.68 <b>(+32.75%)</b></td><td>435.20 <b>(+53.94%)</b></td><td>251.80 <b>(+21.41%)</b></td><td>112.47 (-12.75%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.60 (n/a)</td><td>326.70 (n/a)</td><td>282.70 (n/a)</td><td>207.40 (n/a)</td><td>128.90 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (+8.63%)</td><td>0.02 (-5.43%)</td><td>0.02 <b>(-35.68%)</b></td><td>0.01 (-5.50%)</td><td>0.01 <b>(+32.49%)</b></td><td>554.20 (+5.82%)</td><td>405.06 (+11.40%)</td><td>466.00 <b>(+55.44%)</b></td><td>236.20 (-7.95%)</td><td>153.47 <b>(+24.23%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.70 (n/a)</td><td>363.62 (n/a)</td><td>299.80 (n/a)</td><td>256.60 (n/a)</td><td>123.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (-10.64%)</td><td>0.02 (+1.92%)</td><td>0.03 <b>(+29.60%)</b></td><td>0.01 (-14.62%)</td><td>0.01 (-0.53%)</td><td>594.20 (+17.13%)</td><td>388.70 (-0.25%)</td><td>324.60 <b>(-22.84%)</b></td><td>288.60 (+11.90%)</td><td>131.10 <b>(+28.73%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.30 (n/a)</td><td>389.68 (n/a)</td><td>420.70 (n/a)</td><td>257.90 (n/a)</td><td>101.84 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (+1.01%)</td><td>0.02 (-6.37%)</td><td>0.01 <b>(-25.25%)</b></td><td>0.01 (-15.82%)</td><td>0.01 <b>(+28.25%)</b></td><td>720.80 (+18.79%)</td><td>496.92 (+13.89%)</td><td>580.60 <b>(+33.78%)</b></td><td>284.80 (-1.01%)</td><td>195.77 <b>(+42.70%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.80 (n/a)</td><td>436.30 (n/a)</td><td>434.00 (n/a)</td><td>287.70 (n/a)</td><td>137.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (-2.76%)</td><td>0.02 (+4.95%)</td><td>0.02 <b>(+26.59%)</b></td><td>0.01 (+15.12%)</td><td>0.01 (-17.53%)</td><td>583.40 (-13.13%)</td><td>404.30 (-9.86%)</td><td>392.90 <b>(-20.99%)</b></td><td>261.60 (+2.83%)</td><td>144.43 <b>(-22.68%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>671.60 (n/a)</td><td>448.52 (n/a)</td><td>497.30 (n/a)</td><td>254.40 (n/a)</td><td>186.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (-5.80%)</td><td>0.03 (-18.88%)</td><td>0.02 <b>(-21.83%)</b></td><td>0.02 (-12.30%)</td><td>0.01 (-5.22%)</td><td>693.60 (+14.02%)</td><td>501.36 <b>(+23.38%)</b></td><td>499.80 <b>(+27.92%)</b></td><td>269.50 (+6.19%)</td><td>152.43 (+7.52%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.30 (n/a)</td><td>406.36 (n/a)</td><td>390.70 (n/a)</td><td>253.80 (n/a)</td><td>141.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (-9.36%)</td><td>0.02 (-17.57%)</td><td>0.02 <b>(-38.66%)</b></td><td>0.01 (-10.02%)</td><td>0.01 (-13.60%)</td><td>550.30 (+11.13%)</td><td>422.88 <b>(+20.12%)</b></td><td>449.30 <b>(+63.03%)</b></td><td>272.10 (+10.34%)</td><td>129.54 (+3.73%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.20 (n/a)</td><td>352.06 (n/a)</td><td>275.60 (n/a)</td><td>246.60 (n/a)</td><td>124.89 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (-13.66%)</td><td>0.03 <b>(-24.26%)</b></td><td>0.02 <b>(-38.92%)</b></td><td>0.02 (+10.21%)</td><td>0.01 <b>(-35.00%)</b></td><td>572.50 (-9.27%)</td><td>415.56 <b>(+23.05%)</b></td><td>434.90 <b>(+63.74%)</b></td><td>289.30 (+15.81%)</td><td>108.25 <b>(-34.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>631.00 (n/a)</td><td>337.72 (n/a)</td><td>265.60 (n/a)</td><td>249.80 (n/a)</td><td>164.79 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (+11.57%)</td><td>0.03 <b>(+47.07%)</b></td><td>0.03 <b>(+93.44%)</b></td><td>0.01 <b>(+28.54%)</b></td><td>0.01 (+2.47%)</td><td>628.90 <b>(-22.20%)</b></td><td>377.14 <b>(-33.91%)</b></td><td>290.60 <b>(-48.30%)</b></td><td>219.10 (-10.39%)</td><td>167.00 <b>(-20.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>808.40 (n/a)</td><td>570.62 (n/a)</td><td>562.10 (n/a)</td><td>244.50 (n/a)</td><td>210.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (-19.88%)</td><td>0.02 <b>(-30.24%)</b></td><td>0.02 <b>(-21.31%)</b></td><td>0.01 <b>(-68.17%)</b></td><td>0.01 (-9.96%)</td><td>2018.00 <b>(+214.18%)</b></td><td>810.12 <b>(+84.49%)</b></td><td>606.90 <b>(+27.07%)</b></td><td>261.90 <b>(+24.83%)</b></td><td>690.59 <b>(+284.33%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>642.30 (n/a)</td><td>439.12 (n/a)</td><td>477.60 (n/a)</td><td>209.80 (n/a)</td><td>179.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (-15.17%)</td><td>0.03 (+1.18%)</td><td>0.03 (-2.75%)</td><td>0.02 (+5.92%)</td><td>0.01 <b>(-32.18%)</b></td><td>536.20 (-5.58%)</td><td>323.00 (-10.50%)</td><td>274.20 (+2.85%)</td><td>215.30 (+17.84%)</td><td>128.08 <b>(-29.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.90 (n/a)</td><td>360.90 (n/a)</td><td>266.60 (n/a)</td><td>182.70 (n/a)</td><td>180.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (+4.49%)</td><td>0.03 (+15.45%)</td><td>0.03 <b>(+25.59%)</b></td><td>0.01 (+4.12%)</td><td>0.01 (+7.91%)</td><td>626.10 (-3.96%)</td><td>395.70 (-11.47%)</td><td>317.00 <b>(-20.37%)</b></td><td>205.10 (-4.34%)</td><td>181.28 (+5.56%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.90 (n/a)</td><td>446.96 (n/a)</td><td>398.10 (n/a)</td><td>214.40 (n/a)</td><td>171.73 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (-2.27%)</td><td>0.02 (-13.54%)</td><td>0.02 (-13.19%)</td><td>0.01 <b>(-20.73%)</b></td><td>0.01 (+7.13%)</td><td>614.70 <b>(+26.14%)</b></td><td>463.90 (+19.85%)</td><td>524.80 (+15.21%)</td><td>226.50 (+2.30%)</td><td>158.65 <b>(+32.01%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.30 (n/a)</td><td>387.08 (n/a)</td><td>455.50 (n/a)</td><td>221.40 (n/a)</td><td>120.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (+7.96%)</td><td>0.03 <b>(+23.40%)</b></td><td>0.02 <b>(+23.10%)</b></td><td>0.02 (-2.32%)</td><td>0.01 <b>(+21.06%)</b></td><td>563.10 (+2.38%)</td><td>390.46 (-16.86%)</td><td>405.80 (-18.78%)</td><td>246.10 (-7.38%)</td><td>133.62 (+14.26%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>469.62 (n/a)</td><td>499.60 (n/a)</td><td>265.70 (n/a)</td><td>116.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (+11.93%)</td><td>0.02 (-10.92%)</td><td>0.02 (+3.46%)</td><td>0.01 <b>(-35.48%)</b></td><td>0.01 <b>(+25.86%)</b></td><td>886.20 <b>(+55.01%)</b></td><td>540.54 <b>(+21.89%)</b></td><td>517.80 (-3.34%)</td><td>235.40 (-10.66%)</td><td>236.94 <b>(+62.94%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.70 (n/a)</td><td>443.48 (n/a)</td><td>535.70 (n/a)</td><td>263.50 (n/a)</td><td>145.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.36 (-6.59%)</td><td>0.27 (-1.48%)</td><td>0.34 <b>(+42.47%)</b></td><td>0.16 (-12.30%)</td><td>0.10 (+13.20%)</td><td>629.60 (+14.04%)</td><td>418.44 (+7.61%)</td><td>288.90 <b>(-29.81%)</b></td><td>274.40 (+7.06%)</td><td>186.73 <b>(+48.14%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>552.10 (n/a)</td><td>388.86 (n/a)</td><td>411.60 (n/a)</td><td>256.30 (n/a)</td><td>126.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.47 (-7.37%)</td><td>0.33 (-13.14%)</td><td>0.36 (-10.96%)</td><td>0.19 (-10.86%)</td><td>0.12 (+12.38%)</td><td>504.60 (+12.18%)</td><td>341.26 <b>(+20.21%)</b></td><td>275.00 (+12.34%)</td><td>207.00 (+7.98%)</td><td>135.94 <b>(+37.19%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>449.80 (n/a)</td><td>283.88 (n/a)</td><td>244.80 (n/a)</td><td>191.70 (n/a)</td><td>99.09 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.36 <b>(-32.76%)</b></td><td>0.24 (-3.63%)</td><td>0.19 (+0.29%)</td><td>0.16 (-0.79%)</td><td>0.09 <b>(-41.50%)</b></td><td>600.20 (+0.79%)</td><td>450.26 (-4.30%)</td><td>512.30 (-0.29%)</td><td>276.00 <b>(+48.71%)</b></td><td>151.05 (-7.60%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.53 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>595.50 (n/a)</td><td>470.48 (n/a)</td><td>513.80 (n/a)</td><td>185.60 (n/a)</td><td>163.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.29 <b>(+43.44%)</b></td><td>0.18 (+10.19%)</td><td>0.15 (-13.49%)</td><td>0.10 (-17.47%)</td><td>0.08 <b>(+145.84%)</b></td><td>702.40 <b>(+21.17%)</b></td><td>482.92 (+3.29%)</td><td>493.60 (+15.60%)</td><td>256.00 <b>(-30.28%)</b></td><td>204.36 <b>(+102.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>579.70 (n/a)</td><td>467.54 (n/a)</td><td>427.00 (n/a)</td><td>367.20 (n/a)</td><td>100.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.29 (-6.00%)</td><td>0.19 (-14.78%)</td><td>0.14 <b>(-43.68%)</b></td><td>0.13 (-6.52%)</td><td>0.07 (-3.19%)</td><td>570.70 (+6.97%)</td><td>430.32 (+17.60%)</td><td>510.40 <b>(+77.59%)</b></td><td>256.80 (+6.38%)</td><td>144.31 (+5.45%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>533.50 (n/a)</td><td>365.92 (n/a)</td><td>287.40 (n/a)</td><td>241.40 (n/a)</td><td>136.85 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.30 <b>(-26.81%)</b></td><td>0.20 (-17.76%)</td><td>0.17 <b>(-44.89%)</b></td><td>0.16 <b>(+332.92%)</b></td><td>0.06 <b>(-61.19%)</b></td><td>473.70 <b>(-76.90%)</b></td><td>387.28 <b>(-39.77%)</b></td><td>424.70 <b>(+81.42%)</b></td><td>243.50 <b>(+36.64%)</b></td><td>88.43 <b>(-88.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.31 (n/a)</td><td>0.04 (n/a)</td><td>0.15 (n/a)</td><td>2050.60 (n/a)</td><td>642.96 (n/a)</td><td>234.10 (n/a)</td><td>178.20 (n/a)</td><td>798.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.52 (+5.16%)</td><td>0.37 <b>(+48.36%)</b></td><td>0.38 <b>(+59.77%)</b></td><td>0.24 <b>(+273.05%)</b></td><td>0.12 <b>(-34.93%)</b></td><td>543.20 <b>(-73.20%)</b></td><td>385.22 <b>(-61.22%)</b></td><td>345.00 <b>(-37.42%)</b></td><td>254.30 (-4.93%)</td><td>132.70 <b>(-84.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.49 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>0.19 (n/a)</td><td>2026.50 (n/a)</td><td>993.42 (n/a)</td><td>551.30 (n/a)</td><td>267.50 (n/a)</td><td>845.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.25 <b>(-64.87%)</b></td><td>0.24 <b>(-42.60%)</b></td><td>0.24 <b>(-42.99%)</b></td><td>0.21 (+2.93%)</td><td>0.02 <b>(-90.74%)</b></td><td>626.20 (-2.84%)</td><td>559.00 <b>(+43.91%)</b></td><td>535.30 <b>(+75.45%)</b></td><td>515.30 <b>(+184.70%)</b></td><td>46.65 <b>(-75.07%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.72 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>644.50 (n/a)</td><td>388.44 (n/a)</td><td>305.10 (n/a)</td><td>181.00 (n/a)</td><td>187.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.52 (+17.01%)</td><td>0.20 (-14.06%)</td><td>0.18 <b>(-21.98%)</b></td><td>0.07 (-3.23%)</td><td>0.18 <b>(+38.09%)</b></td><td>2009.90 (+3.34%)</td><td>1122.34 <b>(+40.44%)</b></td><td>743.10 <b>(+28.16%)</b></td><td>253.60 (-14.56%)</td><td>791.49 <b>(+21.19%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.44 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>0.13 (n/a)</td><td>1944.90 (n/a)</td><td>799.14 (n/a)</td><td>579.80 (n/a)</td><td>296.80 (n/a)</td><td>653.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.00 <b>(-50.00%)</b></td><td>0.00 <b>(-38.89%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-79.59%)</b></td><td>19497.20 (-12.48%)</td><td>18101.11 (+18.57%)</td><td>18219.31 (+3.90%)</td><td>16380.05 <b>(+130.71%)</b></td><td>1220.24 <b>(-83.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22278.50 (n/a)</td><td>15266.46 (n/a)</td><td>17535.57 (n/a)</td><td>7099.71 (n/a)</td><td>7590.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.00 (-14.29%)</td><td>0.00 (-9.38%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-18.35%)</td><td>22980.49 <b>(+22.21%)</b></td><td>17117.16 (+11.97%)</td><td>18929.10 (+9.06%)</td><td>6796.32 (+13.21%)</td><td>6335.01 (+18.70%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18804.51 (n/a)</td><td>15287.84 (n/a)</td><td>17356.37 (n/a)</td><td>6003.55 (n/a)</td><td>5337.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.13 (-2.37%)</td><td>0.10 (+3.32%)</td><td>0.09 (+18.48%)</td><td>0.07 (+7.67%)</td><td>0.03 (-17.87%)</td><td>28189.10 (-7.08%)</td><td>22347.59 (-5.85%)</td><td>23211.24 (-15.58%)</td><td>15901.35 (+2.45%)</td><td>5564.14 <b>(-20.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30337.35 (n/a)</td><td>23736.39 (n/a)</td><td>27496.41 (n/a)</td><td>15521.41 (n/a)</td><td>7033.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>1.75 (+9.41%)</td><td>1.12 (+6.07%)</td><td>0.94 (-1.09%)</td><td>0.72 (-12.94%)</td><td>0.45 <b>(+44.25%)</b></td><td>728.10 (+14.86%)</td><td>528.78 (+0.78%)</td><td>557.80 (+1.09%)</td><td>299.00 (-8.59%)</td><td>189.82 <b>(+62.77%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.60 (n/a)</td><td>1.05 (n/a)</td><td>0.95 (n/a)</td><td>0.83 (n/a)</td><td>0.31 (n/a)</td><td>633.90 (n/a)</td><td>524.70 (n/a)</td><td>551.80 (n/a)</td><td>327.10 (n/a)</td><td>116.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>2.75 (+2.53%)</td><td>1.91 (-5.22%)</td><td>1.54 (-19.22%)</td><td>1.26 (-14.62%)</td><td>0.66 <b>(+32.47%)</b></td><td>829.20 (+17.14%)</td><td>602.60 (+10.19%)</td><td>679.70 <b>(+23.81%)</b></td><td>381.40 (-2.46%)</td><td>192.80 <b>(+46.05%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>2.68 (n/a)</td><td>2.01 (n/a)</td><td>1.91 (n/a)</td><td>1.48 (n/a)</td><td>0.50 (n/a)</td><td>707.90 (n/a)</td><td>546.86 (n/a)</td><td>549.00 (n/a)</td><td>391.00 (n/a)</td><td>132.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>1.77 (-10.24%)</td><td>1.07 (-4.30%)</td><td>0.93 (+4.93%)</td><td>0.79 (+4.64%)</td><td>0.40 <b>(-22.17%)</b></td><td>661.50 (-4.44%)</td><td>530.14 (-0.44%)</td><td>561.70 (-4.70%)</td><td>296.90 (+11.41%)</td><td>140.75 <b>(-22.80%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.97 (n/a)</td><td>1.12 (n/a)</td><td>0.89 (n/a)</td><td>0.76 (n/a)</td><td>0.51 (n/a)</td><td>692.20 (n/a)</td><td>532.50 (n/a)</td><td>589.40 (n/a)</td><td>266.50 (n/a)</td><td>182.33 (n/a)</td>
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
