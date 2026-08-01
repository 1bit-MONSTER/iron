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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (-19.36%)</td><td>0.03 (-10.05%)</td><td>0.03 (+12.79%)</td><td>0.02 (-13.72%)</td><td>0.01 <b>(-21.28%)</b></td><td>609.90 (+15.91%)</td><td>402.14 (+9.53%)</td><td>374.10 (-11.35%)</td><td>243.70 <b>(+23.96%)</b></td><td>158.57 (+13.24%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>526.20 (n/a)</td><td>367.14 (n/a)</td><td>422.00 (n/a)</td><td>196.60 (n/a)</td><td>140.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (-3.98%)</td><td>0.03 <b>(-20.17%)</b></td><td>0.04 (-17.85%)</td><td>0.01 <b>(-76.95%)</b></td><td>0.02 <b>(+27.29%)</b></td><td>2400.00 <b>(+333.84%)</b></td><td>744.42 <b>(+123.29%)</b></td><td>290.70 <b>(+21.73%)</b></td><td>231.80 (+4.13%)</td><td>932.11 <b>(+538.07%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>553.20 (n/a)</td><td>333.38 (n/a)</td><td>238.80 (n/a)</td><td>222.60 (n/a)</td><td>146.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 <b>(-29.26%)</b></td><td>0.03 <b>(-26.79%)</b></td><td>0.02 <b>(-42.02%)</b></td><td>0.02 (-13.45%)</td><td>0.01 (-15.34%)</td><td>654.20 (+15.54%)</td><td>467.36 <b>(+37.87%)</b></td><td>530.70 <b>(+72.47%)</b></td><td>291.20 <b>(+41.36%)</b></td><td>164.88 <b>(+22.40%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>566.20 (n/a)</td><td>338.98 (n/a)</td><td>307.70 (n/a)</td><td>206.00 (n/a)</td><td>134.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (+16.99%)</td><td>0.01 (+15.32%)</td><td>0.01 (+9.73%)</td><td>0.01 (+3.72%)</td><td>0.01 <b>(+39.86%)</b></td><td>515.60 (-3.59%)</td><td>393.38 (-10.29%)</td><td>455.40 (-8.87%)</td><td>245.10 (-14.51%)</td><td>127.52 (+10.53%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.80 (n/a)</td><td>438.50 (n/a)</td><td>499.70 (n/a)</td><td>286.70 (n/a)</td><td>115.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (-1.47%)</td><td>0.02 (+10.80%)</td><td>0.02 <b>(+46.94%)</b></td><td>0.01 (-10.13%)</td><td>0.01 (+1.54%)</td><td>516.80 (+11.28%)</td><td>333.94 (-8.94%)</td><td>285.50 <b>(-31.94%)</b></td><td>232.00 (+1.53%)</td><td>120.18 (+10.96%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>464.40 (n/a)</td><td>366.72 (n/a)</td><td>419.50 (n/a)</td><td>228.50 (n/a)</td><td>108.31 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 <b>(+27.04%)</b></td><td>0.02 <b>(+57.70%)</b></td><td>0.02 <b>(+68.25%)</b></td><td>0.01 <b>(+25.02%)</b></td><td>0.01 (+14.93%)</td><td>483.90 <b>(-20.02%)</b></td><td>299.38 <b>(-37.38%)</b></td><td>288.40 <b>(-40.56%)</b></td><td>194.50 <b>(-21.29%)</b></td><td>110.87 <b>(-22.42%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.00 (n/a)</td><td>478.08 (n/a)</td><td>485.20 (n/a)</td><td>247.10 (n/a)</td><td>142.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (+12.38%)</td><td>0.02 <b>(+22.65%)</b></td><td>0.02 <b>(+36.78%)</b></td><td>0.01 (-1.11%)</td><td>0.01 <b>(+26.05%)</b></td><td>480.30 (+1.14%)</td><td>322.80 (-16.06%)</td><td>274.10 <b>(-26.89%)</b></td><td>208.90 (-11.03%)</td><td>113.16 (+17.07%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.90 (n/a)</td><td>384.58 (n/a)</td><td>374.90 (n/a)</td><td>234.80 (n/a)</td><td>96.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (-0.02%)</td><td>0.01 (-13.20%)</td><td>0.01 <b>(-25.04%)</b></td><td>0.01 (-16.39%)</td><td>0.01 (+13.68%)</td><td>583.10 (+19.61%)</td><td>434.04 (+18.93%)</td><td>485.10 <b>(+33.42%)</b></td><td>238.40 (+0.00%)</td><td>136.15 <b>(+31.72%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.50 (n/a)</td><td>364.96 (n/a)</td><td>363.60 (n/a)</td><td>238.40 (n/a)</td><td>103.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.01 (+15.92%)</td><td>0.01 (+6.80%)</td><td>0.01 (-0.87%)</td><td>0.01 (+6.02%)</td><td>0.00 <b>(+22.90%)</b></td><td>627.40 (-5.68%)</td><td>503.42 (-5.65%)</td><td>497.70 (+0.87%)</td><td>377.80 (-13.74%)</td><td>110.12 (+1.79%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>665.20 (n/a)</td><td>533.56 (n/a)</td><td>493.40 (n/a)</td><td>438.00 (n/a)</td><td>108.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>500.60 (n/a)</td><td>328.20 (n/a)</td><td>287.20 (n/a)</td><td>201.80 (n/a)</td><td>129.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.40 (n/a)</td><td>356.34 (n/a)</td><td>271.10 (n/a)</td><td>247.00 (n/a)</td><td>135.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>793.90 (n/a)</td><td>455.54 (n/a)</td><td>403.70 (n/a)</td><td>271.90 (n/a)</td><td>201.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>562.00 (n/a)</td><td>405.50 (n/a)</td><td>437.40 (n/a)</td><td>265.20 (n/a)</td><td>127.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>463.40 (n/a)</td><td>324.60 (n/a)</td><td>270.10 (n/a)</td><td>195.10 (n/a)</td><td>124.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>698.60 (n/a)</td><td>449.18 (n/a)</td><td>430.50 (n/a)</td><td>253.20 (n/a)</td><td>167.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>410.10 (n/a)</td><td>335.98 (n/a)</td><td>315.90 (n/a)</td><td>278.50 (n/a)</td><td>62.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1058.20 (n/a)</td><td>561.70 (n/a)</td><td>505.30 (n/a)</td><td>249.00 (n/a)</td><td>298.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>937.20 (n/a)</td><td>497.74 (n/a)</td><td>419.50 (n/a)</td><td>254.80 (n/a)</td><td>285.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>505.50 (n/a)</td><td>431.20 (n/a)</td><td>440.30 (n/a)</td><td>353.10 (n/a)</td><td>58.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.60 (n/a)</td><td>488.08 (n/a)</td><td>428.00 (n/a)</td><td>390.30 (n/a)</td><td>119.41 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.60 (n/a)</td><td>441.92 (n/a)</td><td>400.20 (n/a)</td><td>271.50 (n/a)</td><td>139.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.44 (-14.81%)</td><td>0.35 (-11.53%)</td><td>0.37 (-4.21%)</td><td>0.17 <b>(-21.22%)</b></td><td>0.10 (-12.05%)</td><td>1286.90 <b>(+26.94%)</b></td><td>712.10 (+15.37%)</td><td>590.70 (+4.40%)</td><td>500.70 (+17.40%)</td><td>324.04 <b>(+38.16%)</b></td><td>18.85 (-14.81%)</td><td>14.83 (-11.53%)</td><td>15.98 (-4.21%)</td><td>7.33 <b>(-21.22%)</b></td><td>4.39 (-12.05%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>1013.80 (n/a)</td><td>617.22 (n/a)</td><td>565.80 (n/a)</td><td>426.50 (n/a)</td><td>234.55 (n/a)</td><td>22.12 (n/a)</td><td>16.76 (n/a)</td><td>16.68 (n/a)</td><td>9.31 (n/a)</td><td>4.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.57 (-8.48%)</td><td>0.48 <b>(+36.91%)</b></td><td>0.46 <b>(+33.16%)</b></td><td>0.41 <b>(+224.57%)</b></td><td>0.06 <b>(-65.05%)</b></td><td>537.70 <b>(-69.19%)</b></td><td>464.92 <b>(-42.94%)</b></td><td>478.90 <b>(-24.90%)</b></td><td>388.60 (+9.28%)</td><td>57.89 <b>(-89.22%)</b></td><td>24.29 (-8.48%)</td><td>20.56 <b>(+36.91%)</b></td><td>19.71 <b>(+33.16%)</b></td><td>17.55 <b>(+224.57%)</b></td><td>2.64 <b>(-65.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.62 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td><td>1745.30 (n/a)</td><td>814.80 (n/a)</td><td>637.70 (n/a)</td><td>355.60 (n/a)</td><td>537.06 (n/a)</td><td>26.54 (n/a)</td><td>15.02 (n/a)</td><td>14.80 (n/a)</td><td>5.41 (n/a)</td><td>7.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.31 (-0.18%)</td><td>0.30 (-1.59%)</td><td>0.30 (-0.46%)</td><td>0.29 (-3.25%)</td><td>0.01 <b>(+100.48%)</b></td><td>87207.00 (+3.36%)</td><td>84118.96 (+1.67%)</td><td>83330.40 (+0.46%)</td><td>81447.40 (+0.18%)</td><td>2497.14 <b>(+108.12%)</b></td><td>210.93 (-0.18%)</td><td>204.38 (-1.59%)</td><td>206.17 (-0.46%)</td><td>197.00 (-3.25%)</td><td>6.03 <b>(+100.48%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84368.80 (n/a)</td><td>82734.44 (n/a)</td><td>82946.40 (n/a)</td><td>81300.10 (n/a)</td><td>1199.83 (n/a)</td><td>211.31 (n/a)</td><td>207.69 (n/a)</td><td>207.12 (n/a)</td><td>203.63 (n/a)</td><td>3.01 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.03 (-0.25%)</td><td>1.01 (-0.17%)</td><td>1.02 (+0.12%)</td><td>0.99 (-0.64%)</td><td>0.02 (+14.86%)</td><td>25547.30 (+0.65%)</td><td>24818.40 (+0.17%)</td><td>24660.70 (-0.12%)</td><td>24485.40 (+0.25%)</td><td>440.09 (+15.81%)</td><td>701.64 (-0.25%)</td><td>692.39 (-0.17%)</td><td>696.65 (+0.12%)</td><td>672.47 (-0.64%)</td><td>12.08 (+14.86%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>0.99 (n/a)</td><td>0.02 (n/a)</td><td>25383.10 (n/a)</td><td>24775.26 (n/a)</td><td>24691.10 (n/a)</td><td>24424.60 (n/a)</td><td>380.00 (n/a)</td><td>703.38 (n/a)</td><td>693.56 (n/a)</td><td>695.79 (n/a)</td><td>676.82 (n/a)</td><td>10.52 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>3.88 <b>(+36.20%)</b></td><td>2.16 (+9.44%)</td><td>1.60 (-10.12%)</td><td>1.38 <b>(+29.90%)</b></td><td>1.03 <b>(+24.51%)</b></td><td>5828.60 <b>(-23.02%)</b></td><td>4292.96 (-9.69%)</td><td>5040.40 (+11.25%)</td><td>2078.30 <b>(-26.58%)</b></td><td>1510.56 <b>(-26.17%)</b></td><td>1017.12 <b>(+36.20%)</b></td><td>565.79 (+9.44%)</td><td>419.40 (-10.12%)</td><td>362.68 <b>(+29.90%)</b></td><td>269.54 <b>(+24.51%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>2.85 (n/a)</td><td>1.97 (n/a)</td><td>1.78 (n/a)</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>7571.40 (n/a)</td><td>4753.40 (n/a)</td><td>4530.50 (n/a)</td><td>2830.80 (n/a)</td><td>2046.05 (n/a)</td><td>746.77 (n/a)</td><td>517.00 (n/a)</td><td>466.60 (n/a)</td><td>279.20 (n/a)</td><td>216.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.26 <b>(-20.36%)</b></td><td>0.21 (-0.46%)</td><td>0.20 (+7.48%)</td><td>0.18 (+5.97%)</td><td>0.03 <b>(-54.00%)</b></td><td>6805.10 (-5.64%)</td><td>5997.92 (-3.56%)</td><td>6075.20 (-6.96%)</td><td>4807.90 <b>(+25.57%)</b></td><td>765.79 <b>(-44.68%)</b></td><td>13.96 <b>(-20.36%)</b></td><td>11.35 (-0.46%)</td><td>11.05 (+7.48%)</td><td>9.86 (+5.97%)</td><td>1.59 <b>(-54.00%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>7211.60 (n/a)</td><td>6219.64 (n/a)</td><td>6529.70 (n/a)</td><td>3828.90 (n/a)</td><td>1384.34 (n/a)</td><td>17.53 (n/a)</td><td>11.40 (n/a)</td><td>10.28 (n/a)</td><td>9.31 (n/a)</td><td>3.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>3.74 (n/a)</td><td>3.54 (n/a)</td><td>3.51 (n/a)</td><td>3.37 (n/a)</td><td>0.16 (n/a)</td><td>3.74 (n/a)</td><td>3.54 (n/a)</td><td>3.50 (n/a)</td><td>3.37 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>7.43 (+0.79%)</td><td>6.72 (+2.94%)</td><td>7.02 (+3.97%)</td><td>5.80 (+2.52%)</td><td>0.77 (-3.69%)</td><td>7.42 (+0.79%)</td><td>6.71 (+2.94%)</td><td>7.01 (+3.97%)</td><td>5.80 (+2.52%)</td><td>0.77 (-3.69%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>7.37 (n/a)</td><td>6.52 (n/a)</td><td>6.75 (n/a)</td><td>5.66 (n/a)</td><td>0.80 (n/a)</td><td>7.36 (n/a)</td><td>6.52 (n/a)</td><td>6.75 (n/a)</td><td>5.66 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>13.42 (-4.34%)</td><td>9.79 (-1.95%)</td><td>8.20 (+0.70%)</td><td>7.32 (-5.50%)</td><td>2.69 (-5.77%)</td><td>13.41 (-4.34%)</td><td>9.78 (-1.95%)</td><td>8.19 (+0.70%)</td><td>7.31 (-5.50%)</td><td>2.69 (-5.77%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>14.03 (n/a)</td><td>9.98 (n/a)</td><td>8.14 (n/a)</td><td>7.74 (n/a)</td><td>2.85 (n/a)</td><td>14.02 (n/a)</td><td>9.98 (n/a)</td><td>8.13 (n/a)</td><td>7.74 (n/a)</td><td>2.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>3.71 (n/a)</td><td>3.61 (n/a)</td><td>3.70 (n/a)</td><td>3.42 (n/a)</td><td>0.14 (n/a)</td><td>3.71 (n/a)</td><td>3.61 (n/a)</td><td>3.69 (n/a)</td><td>3.41 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>7.64 (+0.59%)</td><td>6.57 (-0.86%)</td><td>6.45 (-8.73%)</td><td>5.68 (+0.36%)</td><td>0.90 (+1.73%)</td><td>7.63 (+0.59%)</td><td>6.57 (-0.86%)</td><td>6.44 (-8.73%)</td><td>5.67 (+0.36%)</td><td>0.90 (+1.73%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>7.59 (n/a)</td><td>6.63 (n/a)</td><td>7.06 (n/a)</td><td>5.66 (n/a)</td><td>0.88 (n/a)</td><td>7.59 (n/a)</td><td>6.63 (n/a)</td><td>7.06 (n/a)</td><td>5.65 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>14.14 (-2.86%)</td><td>9.00 (-15.06%)</td><td>7.92 (-7.92%)</td><td>7.25 (-4.92%)</td><td>2.92 (-12.88%)</td><td>14.13 (-2.86%)</td><td>8.99 (-15.06%)</td><td>7.92 (-7.92%)</td><td>7.24 (-4.92%)</td><td>2.91 (-12.88%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>14.56 (n/a)</td><td>10.59 (n/a)</td><td>8.60 (n/a)</td><td>7.62 (n/a)</td><td>3.35 (n/a)</td><td>14.55 (n/a)</td><td>10.59 (n/a)</td><td>8.60 (n/a)</td><td>7.62 (n/a)</td><td>3.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.73 <b>(-44.23%)</b></td><td>1.29 <b>(-43.80%)</b></td><td>1.03 <b>(-62.35%)</b></td><td>1.01 (-13.01%)</td><td>0.37 <b>(-56.17%)</b></td><td>1.73 <b>(-44.23%)</b></td><td>1.28 <b>(-43.80%)</b></td><td>1.03 <b>(-62.35%)</b></td><td>1.00 (-13.01%)</td><td>0.37 <b>(-56.17%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>3.11 (n/a)</td><td>2.29 (n/a)</td><td>2.75 (n/a)</td><td>1.16 (n/a)</td><td>0.84 (n/a)</td><td>3.10 (n/a)</td><td>2.29 (n/a)</td><td>2.74 (n/a)</td><td>1.15 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.50 (+0.35%)</td><td>0.26 (-16.09%)</td><td>0.14 <b>(-56.79%)</b></td><td>0.08 (+2.19%)</td><td>0.22 <b>(+42.88%)</b></td><td>0.50 (+0.35%)</td><td>0.25 (-16.09%)</td><td>0.13 <b>(-56.79%)</b></td><td>0.07 (+2.19%)</td><td>0.22 <b>(+42.88%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.50 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>0.49 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.69 <b>(+51.66%)</b></td><td>0.34 (-7.39%)</td><td>0.32 <b>(-27.60%)</b></td><td>0.08 (+3.25%)</td><td>0.25 <b>(+55.34%)</b></td><td>0.69 <b>(+51.66%)</b></td><td>0.34 (-7.39%)</td><td>0.31 <b>(-27.60%)</b></td><td>0.08 (+3.25%)</td><td>0.25 <b>(+55.34%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>0.16 (n/a)</td><td>0.45 (n/a)</td><td>0.36 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>2.13 (-19.47%)</td><td>1.53 (+18.15%)</td><td>1.57 (+12.23%)</td><td>0.83 <b>(+87.32%)</b></td><td>0.49 <b>(-46.64%)</b></td><td>2.10 (-19.47%)</td><td>1.51 (+18.15%)</td><td>1.55 (+12.23%)</td><td>0.82 <b>(+87.32%)</b></td><td>0.48 <b>(-46.64%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>2.65 (n/a)</td><td>1.30 (n/a)</td><td>1.40 (n/a)</td><td>0.44 (n/a)</td><td>0.91 (n/a)</td><td>2.60 (n/a)</td><td>1.28 (n/a)</td><td>1.38 (n/a)</td><td>0.44 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.00 (n/a)</td><td>392.02 (n/a)</td><td>372.80 (n/a)</td><td>272.40 (n/a)</td><td>123.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2010.50 (n/a)</td><td>809.04 (n/a)</td><td>501.90 (n/a)</td><td>448.40 (n/a)</td><td>674.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1081.40 (n/a)</td><td>567.68 (n/a)</td><td>564.80 (n/a)</td><td>255.00 (n/a)</td><td>317.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.80 (n/a)</td><td>391.02 (n/a)</td><td>365.60 (n/a)</td><td>250.10 (n/a)</td><td>103.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>482.10 (n/a)</td><td>393.32 (n/a)</td><td>405.50 (n/a)</td><td>305.80 (n/a)</td><td>81.30 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.70 (n/a)</td><td>482.90 (n/a)</td><td>495.00 (n/a)</td><td>359.70 (n/a)</td><td>83.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (+14.31%)</td><td>0.03 (+14.93%)</td><td>0.03 (+3.79%)</td><td>0.02 <b>(+42.00%)</b></td><td>0.01 <b>(-20.15%)</b></td><td>454.30 <b>(-29.59%)</b></td><td>320.56 <b>(-20.43%)</b></td><td>300.60 (-3.65%)</td><td>213.70 (-12.53%)</td><td>88.06 <b>(-51.13%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.20 (n/a)</td><td>402.86 (n/a)</td><td>312.00 (n/a)</td><td>244.30 (n/a)</td><td>180.18 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (-0.42%)</td><td>0.03 <b>(+25.21%)</b></td><td>0.03 (+5.86%)</td><td>0.03 <b>(+606.64%)</b></td><td>0.00 <b>(-78.68%)</b></td><td>292.40 <b>(-85.85%)</b></td><td>266.58 <b>(-57.96%)</b></td><td>270.30 (-5.56%)</td><td>243.40 (+0.41%)</td><td>21.63 <b>(-97.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2066.00 (n/a)</td><td>634.10 (n/a)</td><td>286.20 (n/a)</td><td>242.40 (n/a)</td><td>800.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (-16.73%)</td><td>0.03 (-1.50%)</td><td>0.03 (+0.65%)</td><td>0.02 <b>(+26.99%)</b></td><td>0.01 <b>(-47.53%)</b></td><td>438.90 <b>(-21.25%)</b></td><td>333.08 (-8.10%)</td><td>303.20 (-0.66%)</td><td>253.60 <b>(+20.08%)</b></td><td>73.80 <b>(-51.17%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.30 (n/a)</td><td>362.42 (n/a)</td><td>305.20 (n/a)</td><td>211.20 (n/a)</td><td>151.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (-6.01%)</td><td>0.02 (-5.31%)</td><td>0.02 (-9.32%)</td><td>0.02 (-0.06%)</td><td>0.01 (-8.68%)</td><td>512.70 (+0.08%)</td><td>403.62 (+4.66%)</td><td>459.00 (+10.28%)</td><td>258.00 (+6.39%)</td><td>125.44 (-1.38%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.30 (n/a)</td><td>385.64 (n/a)</td><td>416.20 (n/a)</td><td>242.50 (n/a)</td><td>127.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (-8.62%)</td><td>0.03 <b>(+46.66%)</b></td><td>0.03 <b>(+76.18%)</b></td><td>0.01 <b>(+69.05%)</b></td><td>0.01 <b>(-24.38%)</b></td><td>646.20 <b>(-40.85%)</b></td><td>356.22 <b>(-39.49%)</b></td><td>287.20 <b>(-43.23%)</b></td><td>268.00 (+9.43%)</td><td>162.38 <b>(-48.19%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1092.50 (n/a)</td><td>588.68 (n/a)</td><td>505.90 (n/a)</td><td>244.90 (n/a)</td><td>313.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (+10.12%)</td><td>0.02 (+19.40%)</td><td>0.02 (+8.30%)</td><td>0.01 (+12.95%)</td><td>0.01 <b>(+22.75%)</b></td><td>567.10 (-11.47%)</td><td>444.16 (-14.41%)</td><td>515.90 (-7.68%)</td><td>272.50 (-9.20%)</td><td>138.30 (+7.15%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.60 (n/a)</td><td>518.94 (n/a)</td><td>558.80 (n/a)</td><td>300.10 (n/a)</td><td>129.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 <b>(-33.11%)</b></td><td>0.02 (+17.87%)</td><td>0.03 <b>(+82.42%)</b></td><td>0.01 <b>(+39.80%)</b></td><td>0.01 <b>(-59.33%)</b></td><td>559.20 <b>(-28.47%)</b></td><td>363.50 <b>(-31.18%)</b></td><td>326.20 <b>(-45.18%)</b></td><td>260.40 <b>(+49.48%)</b></td><td>115.10 <b>(-49.51%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>781.80 (n/a)</td><td>528.20 (n/a)</td><td>595.00 (n/a)</td><td>174.20 (n/a)</td><td>227.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.02 (-18.20%)</td><td>0.02 (-8.13%)</td><td>0.02 (+8.99%)</td><td>0.01 (-7.60%)</td><td>0.00 <b>(-29.04%)</b></td><td>624.20 (+8.22%)</td><td>483.34 (+5.74%)</td><td>495.30 (-8.24%)</td><td>357.50 <b>(+22.26%)</b></td><td>121.42 (-10.08%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.80 (n/a)</td><td>457.12 (n/a)</td><td>539.80 (n/a)</td><td>292.40 (n/a)</td><td>135.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (+1.31%)</td><td>0.02 (-8.39%)</td><td>0.02 (-0.44%)</td><td>0.01 (-6.40%)</td><td>0.01 (-5.80%)</td><td>635.80 (+6.84%)</td><td>456.88 (+8.47%)</td><td>465.00 (+0.45%)</td><td>270.10 (-1.32%)</td><td>134.60 (+0.41%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.10 (n/a)</td><td>421.20 (n/a)</td><td>462.90 (n/a)</td><td>273.70 (n/a)</td><td>134.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (-9.83%)</td><td>0.03 (+9.89%)</td><td>0.02 <b>(+29.41%)</b></td><td>0.02 <b>(+29.42%)</b></td><td>0.01 <b>(-29.03%)</b></td><td>422.30 <b>(-22.73%)</b></td><td>339.08 (-17.85%)</td><td>381.60 <b>(-22.72%)</b></td><td>194.50 (+10.89%)</td><td>97.48 <b>(-40.09%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.50 (n/a)</td><td>412.76 (n/a)</td><td>493.80 (n/a)</td><td>175.40 (n/a)</td><td>162.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (+9.44%)</td><td>0.03 <b>(+22.68%)</b></td><td>0.03 <b>(+56.60%)</b></td><td>0.02 <b>(+24.12%)</b></td><td>0.01 (+5.92%)</td><td>505.60 (-19.43%)</td><td>326.70 (-19.95%)</td><td>282.70 <b>(-36.13%)</b></td><td>207.40 (-8.63%)</td><td>128.90 <b>(-20.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.50 (n/a)</td><td>408.10 (n/a)</td><td>442.60 (n/a)</td><td>227.00 (n/a)</td><td>161.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (-9.36%)</td><td>0.02 (+9.92%)</td><td>0.03 <b>(+28.22%)</b></td><td>0.02 (+10.67%)</td><td>0.01 (-12.15%)</td><td>523.70 (-9.64%)</td><td>363.62 (-11.18%)</td><td>299.80 <b>(-21.99%)</b></td><td>256.60 (+10.32%)</td><td>123.54 (-14.50%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.60 (n/a)</td><td>409.40 (n/a)</td><td>384.30 (n/a)</td><td>232.60 (n/a)</td><td>144.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (+6.39%)</td><td>0.02 (+10.70%)</td><td>0.02 (+14.53%)</td><td>0.02 <b>(+27.79%)</b></td><td>0.01 (-13.01%)</td><td>507.30 <b>(-21.75%)</b></td><td>389.68 (-13.52%)</td><td>420.70 (-12.70%)</td><td>257.90 (-6.01%)</td><td>101.84 <b>(-34.65%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.30 (n/a)</td><td>450.58 (n/a)</td><td>481.90 (n/a)</td><td>274.40 (n/a)</td><td>155.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (+12.39%)</td><td>0.02 (+18.26%)</td><td>0.02 <b>(+30.14%)</b></td><td>0.01 (-2.74%)</td><td>0.01 <b>(+34.85%)</b></td><td>606.80 (+2.81%)</td><td>436.30 (-12.78%)</td><td>434.00 <b>(-23.16%)</b></td><td>287.70 (-11.01%)</td><td>137.19 <b>(+21.06%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.20 (n/a)</td><td>500.24 (n/a)</td><td>564.80 (n/a)</td><td>323.30 (n/a)</td><td>113.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 <b>(+27.92%)</b></td><td>0.02 (+2.85%)</td><td>0.02 (-16.85%)</td><td>0.01 <b>(-22.72%)</b></td><td>0.01 <b>(+145.73%)</b></td><td>671.60 <b>(+29.40%)</b></td><td>448.52 (+10.88%)</td><td>497.30 <b>(+20.27%)</b></td><td>254.40 <b>(-21.82%)</b></td><td>186.80 <b>(+134.44%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>519.00 (n/a)</td><td>404.50 (n/a)</td><td>413.50 (n/a)</td><td>325.40 (n/a)</td><td>79.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (-7.66%)</td><td>0.03 (-8.82%)</td><td>0.03 (-13.47%)</td><td>0.02 (+0.15%)</td><td>0.01 <b>(-26.07%)</b></td><td>608.30 (-0.15%)</td><td>406.36 (+3.05%)</td><td>390.70 (+15.59%)</td><td>253.80 (+8.28%)</td><td>141.77 (-19.37%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>609.20 (n/a)</td><td>394.32 (n/a)</td><td>338.00 (n/a)</td><td>234.40 (n/a)</td><td>175.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 <b>(-26.21%)</b></td><td>0.03 (+13.81%)</td><td>0.03 <b>(+72.87%)</b></td><td>0.02 <b>(+22.67%)</b></td><td>0.01 <b>(-36.55%)</b></td><td>495.20 (-18.49%)</td><td>352.06 (-18.68%)</td><td>275.60 <b>(-42.15%)</b></td><td>246.60 <b>(+35.49%)</b></td><td>124.89 <b>(-20.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.50 (n/a)</td><td>432.94 (n/a)</td><td>476.40 (n/a)</td><td>182.00 (n/a)</td><td>156.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (-0.60%)</td><td>0.03 <b>(+24.86%)</b></td><td>0.04 <b>(+68.30%)</b></td><td>0.02 (+0.20%)</td><td>0.01 (-12.41%)</td><td>631.00 (-0.21%)</td><td>337.72 <b>(-21.72%)</b></td><td>265.60 <b>(-40.59%)</b></td><td>249.80 (+0.60%)</td><td>164.79 (-5.51%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>632.30 (n/a)</td><td>431.40 (n/a)</td><td>447.10 (n/a)</td><td>248.30 (n/a)</td><td>174.40 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (+12.53%)</td><td>0.02 (-18.36%)</td><td>0.01 <b>(-22.11%)</b></td><td>0.01 <b>(-35.25%)</b></td><td>0.01 <b>(+68.39%)</b></td><td>808.40 <b>(+54.45%)</b></td><td>570.62 <b>(+37.94%)</b></td><td>562.10 <b>(+28.39%)</b></td><td>244.50 (-11.12%)</td><td>210.94 <b>(+118.15%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.40 (n/a)</td><td>413.68 (n/a)</td><td>437.80 (n/a)</td><td>275.10 (n/a)</td><td>96.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.05 (+13.36%)</td><td>0.03 (+9.36%)</td><td>0.02 (-0.55%)</td><td>0.02 (-5.33%)</td><td>0.01 <b>(+31.75%)</b></td><td>642.30 (+5.64%)</td><td>439.12 (-2.30%)</td><td>477.60 (+0.55%)</td><td>209.80 (-11.77%)</td><td>179.69 <b>(+29.18%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.00 (n/a)</td><td>449.44 (n/a)</td><td>475.00 (n/a)</td><td>237.80 (n/a)</td><td>139.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 <b>(+40.84%)</b></td><td>0.03 (+17.16%)</td><td>0.03 (+11.86%)</td><td>0.01 (+4.97%)</td><td>0.01 <b>(+58.46%)</b></td><td>567.90 (-4.73%)</td><td>360.90 (-7.06%)</td><td>266.60 (-10.60%)</td><td>182.70 <b>(-28.99%)</b></td><td>180.66 (+17.33%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.10 (n/a)</td><td>388.30 (n/a)</td><td>298.20 (n/a)</td><td>257.30 (n/a)</td><td>153.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (-19.15%)</td><td>0.02 (-18.54%)</td><td>0.02 (+2.58%)</td><td>0.01 (-6.68%)</td><td>0.01 <b>(-28.77%)</b></td><td>651.90 (+7.17%)</td><td>446.96 (+14.53%)</td><td>398.10 (-2.50%)</td><td>214.40 <b>(+23.72%)</b></td><td>171.73 (-6.28%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>608.30 (n/a)</td><td>390.24 (n/a)</td><td>408.30 (n/a)</td><td>173.30 (n/a)</td><td>183.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.04 (+13.98%)</td><td>0.02 (+8.41%)</td><td>0.02 (-7.90%)</td><td>0.02 (+16.64%)</td><td>0.01 (+18.01%)</td><td>487.30 (-14.27%)</td><td>387.08 (-7.13%)</td><td>455.50 (+8.56%)</td><td>221.40 (-12.25%)</td><td>120.18 (-9.41%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.40 (n/a)</td><td>416.80 (n/a)</td><td>419.60 (n/a)</td><td>252.30 (n/a)</td><td>132.67 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 (-3.45%)</td><td>0.02 (-5.01%)</td><td>0.02 (-5.61%)</td><td>0.02 (+7.57%)</td><td>0.01 (-6.43%)</td><td>550.00 (-7.03%)</td><td>469.62 (+4.04%)</td><td>499.60 (+5.96%)</td><td>265.70 (+3.59%)</td><td>116.94 (-10.46%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.60 (n/a)</td><td>451.38 (n/a)</td><td>471.50 (n/a)</td><td>256.50 (n/a)</td><td>130.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.03 <b>(+35.83%)</b></td><td>0.02 <b>(+24.74%)</b></td><td>0.02 (-0.74%)</td><td>0.01 (+16.08%)</td><td>0.01 <b>(+92.63%)</b></td><td>571.70 (-13.86%)</td><td>443.48 (-14.81%)</td><td>535.70 (+0.73%)</td><td>263.50 <b>(-26.38%)</b></td><td>145.42 <b>(+26.87%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.70 (n/a)</td><td>520.58 (n/a)</td><td>531.80 (n/a)</td><td>357.90 (n/a)</td><td>114.62 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.38 (-14.23%)</td><td>0.28 (+15.84%)</td><td>0.24 (+5.75%)</td><td>0.18 <b>(+97.70%)</b></td><td>0.09 <b>(-29.71%)</b></td><td>552.10 <b>(-49.42%)</b></td><td>388.86 <b>(-27.59%)</b></td><td>411.60 (-5.44%)</td><td>256.30 (+16.61%)</td><td>126.05 <b>(-61.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.45 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>0.13 (n/a)</td><td>1091.60 (n/a)</td><td>537.06 (n/a)</td><td>435.30 (n/a)</td><td>219.80 (n/a)</td><td>331.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.51 <b>(+27.52%)</b></td><td>0.38 <b>(+34.53%)</b></td><td>0.40 <b>(+87.57%)</b></td><td>0.22 (+14.12%)</td><td>0.11 (+3.89%)</td><td>449.80 (-12.37%)</td><td>283.88 <b>(-27.33%)</b></td><td>244.80 <b>(-46.70%)</b></td><td>191.70 <b>(-21.60%)</b></td><td>99.09 <b>(-23.16%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>513.30 (n/a)</td><td>390.62 (n/a)</td><td>459.30 (n/a)</td><td>244.50 (n/a)</td><td>128.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.53 <b>(+38.41%)</b></td><td>0.25 (+10.36%)</td><td>0.19 (-2.01%)</td><td>0.17 (+4.17%)</td><td>0.16 <b>(+71.46%)</b></td><td>595.50 (-4.00%)</td><td>470.48 (-1.00%)</td><td>513.80 (+2.05%)</td><td>185.60 <b>(-27.75%)</b></td><td>163.47 (+14.29%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.38 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>620.30 (n/a)</td><td>475.22 (n/a)</td><td>503.50 (n/a)</td><td>256.90 (n/a)</td><td>143.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.20 <b>(-25.65%)</b></td><td>0.16 (-17.74%)</td><td>0.17 (+3.92%)</td><td>0.13 (-11.34%)</td><td>0.03 <b>(-43.54%)</b></td><td>579.70 (+12.78%)</td><td>467.54 (+17.67%)</td><td>427.00 (-3.76%)</td><td>367.20 <b>(+34.51%)</b></td><td>100.72 (-8.52%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>514.00 (n/a)</td><td>397.34 (n/a)</td><td>443.70 (n/a)</td><td>273.00 (n/a)</td><td>110.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.31 (+15.90%)</td><td>0.22 (+13.59%)</td><td>0.26 <b>(+49.28%)</b></td><td>0.14 (-9.36%)</td><td>0.08 <b>(+62.18%)</b></td><td>533.50 (+10.32%)</td><td>365.92 (-6.16%)</td><td>287.40 <b>(-33.02%)</b></td><td>241.40 (-13.72%)</td><td>136.85 <b>(+62.02%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>483.60 (n/a)</td><td>389.92 (n/a)</td><td>429.10 (n/a)</td><td>279.80 (n/a)</td><td>84.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.41 <b>(+45.35%)</b></td><td>0.24 <b>(+54.70%)</b></td><td>0.31 <b>(+125.74%)</b></td><td>0.04 (-8.88%)</td><td>0.15 <b>(+39.87%)</b></td><td>2050.60 (+9.75%)</td><td>642.96 (-19.14%)</td><td>234.10 <b>(-55.70%)</b></td><td>178.20 <b>(-31.20%)</b></td><td>798.05 (+18.24%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>1868.50 (n/a)</td><td>795.20 (n/a)</td><td>528.40 (n/a)</td><td>259.00 (n/a)</td><td>674.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.49 (+15.73%)</td><td>0.25 (-18.17%)</td><td>0.24 (-13.16%)</td><td>0.06 <b>(-71.13%)</b></td><td>0.19 <b>(+127.71%)</b></td><td>2026.50 <b>(+246.41%)</b></td><td>993.42 <b>(+120.78%)</b></td><td>551.30 (+15.17%)</td><td>267.50 (-13.57%)</td><td>845.57 <b>(+644.42%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>585.00 (n/a)</td><td>449.96 (n/a)</td><td>478.70 (n/a)</td><td>309.50 (n/a)</td><td>113.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.72 <b>(+29.75%)</b></td><td>0.41 <b>(+22.98%)</b></td><td>0.43 <b>(+55.35%)</b></td><td>0.20 (-12.89%)</td><td>0.20 <b>(+57.17%)</b></td><td>644.50 (+14.78%)</td><td>388.44 (-9.68%)</td><td>305.10 <b>(-35.65%)</b></td><td>181.00 <b>(-22.95%)</b></td><td>187.08 <b>(+51.20%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.56 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>561.50 (n/a)</td><td>430.08 (n/a)</td><td>474.10 (n/a)</td><td>234.90 (n/a)</td><td>123.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.44 (-16.69%)</td><td>0.24 <b>(-20.49%)</b></td><td>0.23 (-6.80%)</td><td>0.07 <b>(+25.77%)</b></td><td>0.13 <b>(-31.31%)</b></td><td>1944.90 <b>(-20.49%)</b></td><td>799.14 (-4.04%)</td><td>579.80 (+7.31%)</td><td>296.80 <b>(+20.06%)</b></td><td>653.12 <b>(-28.80%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.53 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>0.19 (n/a)</td><td>2446.10 (n/a)</td><td>832.82 (n/a)</td><td>540.30 (n/a)</td><td>247.20 (n/a)</td><td>917.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.00 (+0.00%)</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-60.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+6.90%)</td><td>22278.50 (+3.91%)</td><td>15266.46 <b>(+25.35%)</b></td><td>17535.57 <b>(+103.61%)</b></td><td>7099.71 (+9.78%)</td><td>7590.31 (+9.16%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21440.62 (n/a)</td><td>12178.71 (n/a)</td><td>8612.22 (n/a)</td><td>6467.20 (n/a)</td><td>6953.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 (-3.03%)</td><td>0.00 (-16.67%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 <b>(+119.45%)</b></td><td>18804.51 (+6.18%)</td><td>15287.84 (+12.57%)</td><td>17356.37 <b>(+22.05%)</b></td><td>6003.55 <b>(-26.44%)</b></td><td>5337.04 <b>(+54.20%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17709.86 (n/a)</td><td>13580.99 (n/a)</td><td>14220.72 (n/a)</td><td>8161.88 (n/a)</td><td>3461.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>0.14 (+1.81%)</td><td>0.10 (+7.04%)</td><td>0.08 (-3.90%)</td><td>0.07 (-9.20%)</td><td>0.03 <b>(+30.48%)</b></td><td>30337.35 (+10.01%)</td><td>23736.39 (-3.11%)</td><td>27496.41 (+4.15%)</td><td>15521.41 (-1.76%)</td><td>7033.40 <b>(+42.32%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>27575.71 (n/a)</td><td>24499.12 (n/a)</td><td>26400.37 (n/a)</td><td>15799.27 (n/a)</td><td>4941.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.60 (-11.27%)</td><td>1.05 <b>(-22.43%)</b></td><td>0.95 <b>(-40.88%)</b></td><td>0.83 (+16.04%)</td><td>0.31 <b>(-31.71%)</b></td><td>633.90 (-13.84%)</td><td>524.70 <b>(+20.70%)</b></td><td>551.80 <b>(+69.16%)</b></td><td>327.10 (+12.72%)</td><td>116.61 <b>(-37.45%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>1.81 (n/a)</td><td>1.36 (n/a)</td><td>1.61 (n/a)</td><td>0.71 (n/a)</td><td>0.46 (n/a)</td><td>735.70 (n/a)</td><td>434.72 (n/a)</td><td>326.20 (n/a)</td><td>290.20 (n/a)</td><td>186.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>2.68 (-14.51%)</td><td>2.01 (+2.52%)</td><td>1.91 (+15.30%)</td><td>1.48 (+12.57%)</td><td>0.50 <b>(-34.57%)</b></td><td>707.90 (-11.17%)</td><td>546.86 (-7.96%)</td><td>549.00 (-13.28%)</td><td>391.00 (+16.96%)</td><td>132.01 <b>(-33.12%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>3.14 (n/a)</td><td>1.96 (n/a)</td><td>1.66 (n/a)</td><td>1.32 (n/a)</td><td>0.77 (n/a)</td><td>796.90 (n/a)</td><td>594.14 (n/a)</td><td>633.10 (n/a)</td><td>334.30 (n/a)</td><td>197.39 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:29:48</td><td>1.97 (-2.02%)</td><td>1.12 (-10.76%)</td><td>0.89 (-11.51%)</td><td>0.76 (-15.75%)</td><td>0.51 (+5.87%)</td><td>692.20 (+18.71%)</td><td>532.50 (+15.40%)</td><td>589.40 (+13.00%)</td><td>266.50 (+2.07%)</td><td>182.33 <b>(+25.87%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>2.01 (n/a)</td><td>1.25 (n/a)</td><td>1.01 (n/a)</td><td>0.90 (n/a)</td><td>0.48 (n/a)</td><td>583.10 (n/a)</td><td>461.42 (n/a)</td><td>521.60 (n/a)</td><td>261.10 (n/a)</td><td>144.85 (n/a)</td>
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
