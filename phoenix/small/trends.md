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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (+10.78%)</td><td>0.03 (+1.59%)</td><td>0.04 (+12.80%)</td><td>0.02 (-9.43%)</td><td>0.01 <b>(+52.15%)</b></td><td>588.50 (+10.41%)</td><td>393.98 (+3.16%)</td><td>329.50 (-11.33%)</td><td>273.20 (-9.75%)</td><td>135.02 <b>(+49.05%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.00 (n/a)</td><td>381.92 (n/a)</td><td>371.60 (n/a)</td><td>302.70 (n/a)</td><td>90.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.05 <b>(-20.11%)</b></td><td>0.03 <b>(-27.56%)</b></td><td>0.03 <b>(-37.80%)</b></td><td>0.02 (-4.86%)</td><td>0.01 <b>(-22.15%)</b></td><td>528.80 (+5.11%)</td><td>424.42 <b>(+36.01%)</b></td><td>485.70 <b>(+60.77%)</b></td><td>271.60 <b>(+25.16%)</b></td><td>117.71 (+3.15%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.10 (n/a)</td><td>312.04 (n/a)</td><td>302.10 (n/a)</td><td>217.00 (n/a)</td><td>114.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 <b>(-31.19%)</b></td><td>0.02 (-18.16%)</td><td>0.02 (-19.99%)</td><td>0.01 <b>(+83.62%)</b></td><td>0.01 <b>(-47.89%)</b></td><td>1074.70 <b>(-45.54%)</b></td><td>672.54 (-11.20%)</td><td>654.20 <b>(+24.99%)</b></td><td>383.70 <b>(+45.34%)</b></td><td>252.90 <b>(-63.30%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1973.40 (n/a)</td><td>757.34 (n/a)</td><td>523.40 (n/a)</td><td>264.00 (n/a)</td><td>689.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 <b>(-27.13%)</b></td><td>0.02 (-13.12%)</td><td>0.02 (-8.99%)</td><td>0.01 (-0.49%)</td><td>0.00 <b>(-50.15%)</b></td><td>485.10 (+0.50%)</td><td>343.56 (+7.69%)</td><td>299.50 (+9.87%)</td><td>289.40 <b>(+37.29%)</b></td><td>82.65 <b>(-30.48%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>482.70 (n/a)</td><td>319.02 (n/a)</td><td>272.60 (n/a)</td><td>210.80 (n/a)</td><td>118.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 <b>(-24.31%)</b></td><td>0.01 (-17.85%)</td><td>0.01 (+11.81%)</td><td>0.00 <b>(-60.43%)</b></td><td>0.01 (+7.85%)</td><td>1211.40 <b>(+152.74%)</b></td><td>581.16 <b>(+48.62%)</b></td><td>380.50 (-10.58%)</td><td>289.30 <b>(+32.16%)</b></td><td>385.98 <b>(+284.35%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>479.30 (n/a)</td><td>391.04 (n/a)</td><td>425.50 (n/a)</td><td>218.90 (n/a)</td><td>100.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 <b>(-22.72%)</b></td><td>0.01 (-3.90%)</td><td>0.01 (+1.10%)</td><td>0.00 (-0.19%)</td><td>0.01 <b>(-24.11%)</b></td><td>1120.30 (+0.20%)</td><td>593.36 (-0.58%)</td><td>585.70 (-1.08%)</td><td>290.20 <b>(+29.44%)</b></td><td>327.86 (-0.46%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1118.10 (n/a)</td><td>596.80 (n/a)</td><td>592.10 (n/a)</td><td>224.20 (n/a)</td><td>329.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (+8.91%)</td><td>0.02 <b>(+22.97%)</b></td><td>0.02 <b>(+71.21%)</b></td><td>0.00 <b>(-44.02%)</b></td><td>0.01 <b>(+80.60%)</b></td><td>1061.60 <b>(+78.66%)</b></td><td>469.68 (+4.08%)</td><td>262.30 <b>(-41.61%)</b></td><td>249.10 (-8.18%)</td><td>350.71 <b>(+186.33%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.20 (n/a)</td><td>451.28 (n/a)</td><td>449.20 (n/a)</td><td>271.30 (n/a)</td><td>122.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (-13.60%)</td><td>0.01 (-17.94%)</td><td>0.01 <b>(-33.17%)</b></td><td>0.01 (-3.16%)</td><td>0.01 <b>(-20.25%)</b></td><td>512.90 (+3.26%)</td><td>405.06 (+19.07%)</td><td>481.80 <b>(+49.63%)</b></td><td>240.90 (+15.71%)</td><td>128.25 (-0.94%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>496.70 (n/a)</td><td>340.18 (n/a)</td><td>322.00 (n/a)</td><td>208.20 (n/a)</td><td>129.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (-18.09%)</td><td>0.01 (-11.23%)</td><td>0.01 (-12.75%)</td><td>0.01 (-7.87%)</td><td>0.00 <b>(-22.12%)</b></td><td>564.00 (+8.55%)</td><td>453.06 (+11.10%)</td><td>517.90 (+14.61%)</td><td>286.40 <b>(+22.08%)</b></td><td>124.05 (+5.58%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>519.60 (n/a)</td><td>407.78 (n/a)</td><td>451.90 (n/a)</td><td>234.60 (n/a)</td><td>117.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>285.80 (n/a)</td><td>251.16 (n/a)</td><td>245.60 (n/a)</td><td>233.90 (n/a)</td><td>20.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.70 (n/a)</td><td>345.32 (n/a)</td><td>288.40 (n/a)</td><td>260.50 (n/a)</td><td>107.75 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>470.20 (n/a)</td><td>321.74 (n/a)</td><td>278.40 (n/a)</td><td>229.90 (n/a)</td><td>95.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>596.50 (n/a)</td><td>350.34 (n/a)</td><td>299.30 (n/a)</td><td>159.90 (n/a)</td><td>192.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.10 (n/a)</td><td>456.16 (n/a)</td><td>485.60 (n/a)</td><td>276.10 (n/a)</td><td>116.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.20 (n/a)</td><td>485.06 (n/a)</td><td>497.80 (n/a)</td><td>272.30 (n/a)</td><td>126.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.80 (n/a)</td><td>351.42 (n/a)</td><td>304.00 (n/a)</td><td>201.60 (n/a)</td><td>167.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.90 (n/a)</td><td>408.58 (n/a)</td><td>339.90 (n/a)</td><td>238.00 (n/a)</td><td>173.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.60 (n/a)</td><td>307.60 (n/a)</td><td>265.80 (n/a)</td><td>249.10 (n/a)</td><td>99.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.50 (n/a)</td><td>395.22 (n/a)</td><td>442.90 (n/a)</td><td>238.70 (n/a)</td><td>153.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.00 (n/a)</td><td>368.32 (n/a)</td><td>316.20 (n/a)</td><td>201.40 (n/a)</td><td>171.70 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.10 (n/a)</td><td>414.78 (n/a)</td><td>386.70 (n/a)</td><td>278.30 (n/a)</td><td>131.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.53 <b>(+31.03%)</b></td><td>0.46 <b>(+34.22%)</b></td><td>0.49 <b>(+30.06%)</b></td><td>0.33 <b>(+44.96%)</b></td><td>0.08 (+10.94%)</td><td>673.60 <b>(-31.01%)</b></td><td>491.46 <b>(-26.62%)</b></td><td>452.20 <b>(-23.11%)</b></td><td>418.70 <b>(-23.69%)</b></td><td>104.22 <b>(-41.18%)</b></td><td>22.54 <b>(+31.03%)</b></td><td>19.77 <b>(+34.22%)</b></td><td>20.87 <b>(+30.06%)</b></td><td>14.01 <b>(+44.96%)</b></td><td>3.39 (+10.94%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>976.40 (n/a)</td><td>669.72 (n/a)</td><td>588.10 (n/a)</td><td>548.70 (n/a)</td><td>177.17 (n/a)</td><td>17.20 (n/a)</td><td>14.73 (n/a)</td><td>16.05 (n/a)</td><td>9.67 (n/a)</td><td>3.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.47 (-9.42%)</td><td>0.36 (-19.17%)</td><td>0.43 (+4.92%)</td><td>0.09 <b>(-76.36%)</b></td><td>0.15 <b>(+140.36%)</b></td><td>2468.50 <b>(+323.05%)</b></td><td>914.00 <b>(+79.57%)</b></td><td>519.00 (-4.68%)</td><td>473.60 (+10.40%)</td><td>870.07 <b>(+1131.17%)</b></td><td>19.93 (-9.42%)</td><td>15.23 (-19.17%)</td><td>18.18 (+4.92%)</td><td>3.82 <b>(-76.36%)</b></td><td>6.54 <b>(+140.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>583.50 (n/a)</td><td>509.00 (n/a)</td><td>544.50 (n/a)</td><td>429.00 (n/a)</td><td>70.67 (n/a)</td><td>22.00 (n/a)</td><td>18.84 (n/a)</td><td>17.33 (n/a)</td><td>16.17 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.31 (+1.24%)</td><td>0.30 (-1.38%)</td><td>0.30 (-1.74%)</td><td>0.29 (-2.72%)</td><td>0.01 <b>(+147.35%)</b></td><td>85954.00 (+2.79%)</td><td>83637.32 (+1.44%)</td><td>83724.00 (+1.77%)</td><td>80641.80 (-1.22%)</td><td>2017.03 <b>(+150.81%)</b></td><td>213.04 (+1.24%)</td><td>205.51 (-1.38%)</td><td>205.20 (-1.74%)</td><td>199.87 (-2.72%)</td><td>5.01 <b>(+147.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83618.80 (n/a)</td><td>82451.88 (n/a)</td><td>82269.00 (n/a)</td><td>81638.70 (n/a)</td><td>804.21 (n/a)</td><td>210.44 (n/a)</td><td>208.38 (n/a)</td><td>208.83 (n/a)</td><td>205.45 (n/a)</td><td>2.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.03 (-0.01%)</td><td>1.03 (+1.97%)</td><td>1.03 (+2.08%)</td><td>1.02 (+3.05%)</td><td>0.00 <b>(-82.50%)</b></td><td>24577.70 (-2.96%)</td><td>24532.28 (-1.95%)</td><td>24546.30 (-2.04%)</td><td>24430.80 (+0.01%)</td><td>60.44 <b>(-82.98%)</b></td><td>703.20 (-0.01%)</td><td>700.30 (+1.97%)</td><td>699.90 (+2.08%)</td><td>699.00 (+3.05%)</td><td>1.73 <b>(-82.50%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.99 (n/a)</td><td>0.01 (n/a)</td><td>25326.60 (n/a)</td><td>25019.68 (n/a)</td><td>25057.00 (n/a)</td><td>24428.10 (n/a)</td><td>355.16 (n/a)</td><td>703.28 (n/a)</td><td>686.77 (n/a)</td><td>685.63 (n/a)</td><td>678.33 (n/a)</td><td>9.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>3.80 <b>(+64.67%)</b></td><td>2.94 <b>(+50.22%)</b></td><td>3.50 <b>(+81.22%)</b></td><td>1.50 (-11.34%)</td><td>1.05 <b>(+372.17%)</b></td><td>5366.40 (+12.79%)</td><td>3138.64 <b>(-24.52%)</b></td><td>2303.20 <b>(-44.82%)</b></td><td>2122.30 <b>(-39.27%)</b></td><td>1420.14 <b>(+212.91%)</b></td><td>996.08 <b>(+64.67%)</b></td><td>771.31 <b>(+50.22%)</b></td><td>917.81 <b>(+81.22%)</b></td><td>393.92 (-11.34%)</td><td>275.75 <b>(+372.17%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.31 (n/a)</td><td>1.96 (n/a)</td><td>1.93 (n/a)</td><td>1.69 (n/a)</td><td>0.22 (n/a)</td><td>4758.00 (n/a)</td><td>4158.24 (n/a)</td><td>4174.00 (n/a)</td><td>3494.60 (n/a)</td><td>453.85 (n/a)</td><td>604.91 (n/a)</td><td>513.44 (n/a)</td><td>506.45 (n/a)</td><td>444.29 (n/a)</td><td>58.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.33 (-4.97%)</td><td>0.23 (-9.67%)</td><td>0.21 (-18.28%)</td><td>0.18 (+1.92%)</td><td>0.06 (-0.10%)</td><td>7014.20 (-1.88%)</td><td>5790.04 (+11.01%)</td><td>6040.20 <b>(+22.37%)</b></td><td>3811.60 (+5.23%)</td><td>1350.01 (+4.35%)</td><td>17.61 (-4.97%)</td><td>12.20 (-9.67%)</td><td>11.11 (-18.28%)</td><td>9.57 (+1.92%)</td><td>3.34 (-0.10%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>7148.80 (n/a)</td><td>5215.98 (n/a)</td><td>4935.90 (n/a)</td><td>3622.00 (n/a)</td><td>1293.71 (n/a)</td><td>18.53 (n/a)</td><td>13.51 (n/a)</td><td>13.60 (n/a)</td><td>9.39 (n/a)</td><td>3.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.14 (-6.52%)</td><td>0.10 <b>(+23.35%)</b></td><td>0.11 <b>(+55.68%)</b></td><td>0.06 (+4.81%)</td><td>0.04 (-4.08%)</td><td>0.14 (-6.52%)</td><td>0.10 <b>(+23.35%)</b></td><td>0.11 <b>(+55.68%)</b></td><td>0.06 (+4.81%)</td><td>0.04 (-4.08%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>3.73 (-4.55%)</td><td>3.61 (-1.41%)</td><td>3.61 (-0.02%)</td><td>3.38 (-4.07%)</td><td>0.14 (-2.54%)</td><td>3.73 (-4.55%)</td><td>3.61 (-1.41%)</td><td>3.61 (-0.02%)</td><td>3.37 (-4.07%)</td><td>0.14 (-2.54%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>3.91 (n/a)</td><td>3.66 (n/a)</td><td>3.61 (n/a)</td><td>3.52 (n/a)</td><td>0.15 (n/a)</td><td>3.91 (n/a)</td><td>3.66 (n/a)</td><td>3.61 (n/a)</td><td>3.52 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>7.49 (+1.20%)</td><td>7.01 (+10.19%)</td><td>7.12 (+7.84%)</td><td>6.53 (+18.46%)</td><td>0.44 <b>(-44.53%)</b></td><td>7.48 (+1.20%)</td><td>7.01 (+10.19%)</td><td>7.12 (+7.84%)</td><td>6.52 (+18.46%)</td><td>0.44 <b>(-44.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>7.40 (n/a)</td><td>6.36 (n/a)</td><td>6.60 (n/a)</td><td>5.51 (n/a)</td><td>0.80 (n/a)</td><td>7.39 (n/a)</td><td>6.36 (n/a)</td><td>6.60 (n/a)</td><td>5.51 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>13.98 (+0.33%)</td><td>10.45 (+2.76%)</td><td>9.75 (+18.57%)</td><td>7.25 (+1.44%)</td><td>3.08 (-5.05%)</td><td>13.97 (+0.33%)</td><td>10.44 (+2.76%)</td><td>9.74 (+18.57%)</td><td>7.24 (+1.44%)</td><td>3.08 (-5.05%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>13.94 (n/a)</td><td>10.17 (n/a)</td><td>8.22 (n/a)</td><td>7.15 (n/a)</td><td>3.24 (n/a)</td><td>13.93 (n/a)</td><td>10.16 (n/a)</td><td>8.22 (n/a)</td><td>7.14 (n/a)</td><td>3.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>3.92 (+1.59%)</td><td>3.69 (+0.95%)</td><td>3.76 (+3.46%)</td><td>3.34 (-2.12%)</td><td>0.25 <b>(+51.36%)</b></td><td>3.92 (+1.59%)</td><td>3.68 (+0.95%)</td><td>3.76 (+3.46%)</td><td>3.34 (-2.12%)</td><td>0.25 <b>(+51.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>3.86 (n/a)</td><td>3.65 (n/a)</td><td>3.64 (n/a)</td><td>3.41 (n/a)</td><td>0.17 (n/a)</td><td>3.86 (n/a)</td><td>3.65 (n/a)</td><td>3.63 (n/a)</td><td>3.41 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>7.53 (+0.00%)</td><td>6.96 (-3.50%)</td><td>6.83 (-4.25%)</td><td>6.20 (-8.74%)</td><td>0.57 <b>(+78.83%)</b></td><td>7.53 (+0.00%)</td><td>6.95 (-3.50%)</td><td>6.83 (-4.25%)</td><td>6.19 (-8.74%)</td><td>0.57 <b>(+78.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>7.53 (n/a)</td><td>7.21 (n/a)</td><td>7.14 (n/a)</td><td>6.79 (n/a)</td><td>0.32 (n/a)</td><td>7.53 (n/a)</td><td>7.20 (n/a)</td><td>7.13 (n/a)</td><td>6.79 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>10.83 <b>(-21.52%)</b></td><td>8.64 (-6.38%)</td><td>8.11 (-0.82%)</td><td>8.00 (+7.85%)</td><td>1.23 <b>(-52.66%)</b></td><td>10.82 <b>(-21.52%)</b></td><td>8.64 (-6.38%)</td><td>8.10 (-0.82%)</td><td>8.00 (+7.85%)</td><td>1.22 <b>(-52.66%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>13.80 (n/a)</td><td>9.23 (n/a)</td><td>8.18 (n/a)</td><td>7.42 (n/a)</td><td>2.59 (n/a)</td><td>13.79 (n/a)</td><td>9.22 (n/a)</td><td>8.17 (n/a)</td><td>7.41 (n/a)</td><td>2.59 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.80 (n/a)</td><td>432.92 (n/a)</td><td>530.70 (n/a)</td><td>226.80 (n/a)</td><td>149.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.60 (n/a)</td><td>409.04 (n/a)</td><td>482.60 (n/a)</td><td>231.70 (n/a)</td><td>149.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.80 (n/a)</td><td>388.88 (n/a)</td><td>362.70 (n/a)</td><td>220.40 (n/a)</td><td>168.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.40 (n/a)</td><td>347.50 (n/a)</td><td>287.30 (n/a)</td><td>233.60 (n/a)</td><td>131.30 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.20 (n/a)</td><td>471.42 (n/a)</td><td>484.90 (n/a)</td><td>254.30 (n/a)</td><td>133.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>497.00 (n/a)</td><td>444.94 (n/a)</td><td>435.20 (n/a)</td><td>421.00 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (-18.37%)</td><td>0.03 (+0.87%)</td><td>0.03 (+4.08%)</td><td>0.02 (+5.72%)</td><td>0.01 <b>(-34.65%)</b></td><td>502.60 (-5.42%)</td><td>336.74 (-5.21%)</td><td>297.60 (-3.91%)</td><td>266.90 <b>(+22.49%)</b></td><td>95.55 <b>(-22.67%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.40 (n/a)</td><td>355.24 (n/a)</td><td>309.70 (n/a)</td><td>217.90 (n/a)</td><td>123.57 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (-1.13%)</td><td>0.03 (-5.79%)</td><td>0.03 (-2.57%)</td><td>0.02 (+15.05%)</td><td>0.01 (-10.03%)</td><td>475.70 (-13.08%)</td><td>329.06 (+3.14%)</td><td>299.10 (+2.64%)</td><td>226.80 (+1.11%)</td><td>104.03 <b>(-21.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.30 (n/a)</td><td>319.04 (n/a)</td><td>291.40 (n/a)</td><td>224.30 (n/a)</td><td>132.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (-16.67%)</td><td>0.02 (+0.36%)</td><td>0.03 <b>(+46.76%)</b></td><td>0.01 (+7.95%)</td><td>0.01 (-16.86%)</td><td>583.10 (-7.36%)</td><td>396.68 (-2.54%)</td><td>297.30 <b>(-31.87%)</b></td><td>277.70 <b>(+20.01%)</b></td><td>150.89 (-4.85%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.40 (n/a)</td><td>407.00 (n/a)</td><td>436.40 (n/a)</td><td>231.40 (n/a)</td><td>158.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (+14.75%)</td><td>0.02 (-3.69%)</td><td>0.02 <b>(-28.26%)</b></td><td>0.01 <b>(-26.81%)</b></td><td>0.01 <b>(+88.33%)</b></td><td>676.10 <b>(+36.61%)</b></td><td>457.24 (+19.18%)</td><td>509.60 <b>(+39.39%)</b></td><td>243.50 (-12.85%)</td><td>202.44 <b>(+105.35%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.90 (n/a)</td><td>383.66 (n/a)</td><td>365.60 (n/a)</td><td>279.40 (n/a)</td><td>98.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 <b>(-29.93%)</b></td><td>0.02 (-14.15%)</td><td>0.02 (-1.27%)</td><td>0.01 <b>(+67.09%)</b></td><td>0.00 <b>(-52.64%)</b></td><td>630.30 <b>(-40.15%)</b></td><td>503.78 (-2.90%)</td><td>479.80 (+1.29%)</td><td>336.60 <b>(+42.75%)</b></td><td>126.30 <b>(-59.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1053.20 (n/a)</td><td>518.82 (n/a)</td><td>473.70 (n/a)</td><td>235.80 (n/a)</td><td>314.74 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (-1.27%)</td><td>0.01 (+9.16%)</td><td>0.01 (+18.28%)</td><td>0.01 <b>(+42.18%)</b></td><td>0.00 <b>(-41.87%)</b></td><td>831.10 <b>(-29.66%)</b></td><td>594.98 (-19.28%)</td><td>576.20 (-15.45%)</td><td>421.40 (+1.27%)</td><td>149.95 <b>(-55.66%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1181.60 (n/a)</td><td>737.06 (n/a)</td><td>681.50 (n/a)</td><td>416.10 (n/a)</td><td>338.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (-16.86%)</td><td>0.02 <b>(-33.76%)</b></td><td>0.03 (-18.45%)</td><td>0.01 <b>(-73.64%)</b></td><td>0.01 <b>(+172.69%)</b></td><td>1122.90 <b>(+279.36%)</b></td><td>507.02 <b>(+99.76%)</b></td><td>305.40 <b>(+22.65%)</b></td><td>262.10 <b>(+20.28%)</b></td><td>362.77 <b>(+1139.48%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>296.00 (n/a)</td><td>253.82 (n/a)</td><td>249.00 (n/a)</td><td>217.90 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (-15.90%)</td><td>0.03 <b>(-40.90%)</b></td><td>0.02 <b>(-55.75%)</b></td><td>0.02 (-16.75%)</td><td>0.01 (-12.43%)</td><td>620.00 <b>(+20.13%)</b></td><td>526.94 <b>(+69.49%)</b></td><td>578.50 <b>(+125.98%)</b></td><td>289.90 (+18.91%)</td><td>134.84 (+16.38%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>310.90 (n/a)</td><td>256.00 (n/a)</td><td>243.80 (n/a)</td><td>115.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (-7.76%)</td><td>0.02 <b>(-20.35%)</b></td><td>0.02 <b>(-36.70%)</b></td><td>0.01 <b>(-26.30%)</b></td><td>0.01 (+18.48%)</td><td>639.90 <b>(+35.69%)</b></td><td>430.46 <b>(+33.68%)</b></td><td>442.00 <b>(+57.97%)</b></td><td>250.10 (+8.41%)</td><td>167.03 <b>(+67.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.60 (n/a)</td><td>322.00 (n/a)</td><td>279.80 (n/a)</td><td>230.70 (n/a)</td><td>99.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 <b>(-29.36%)</b></td><td>0.02 (-17.13%)</td><td>0.02 (+7.76%)</td><td>0.02 (+1.19%)</td><td>0.00 <b>(-58.56%)</b></td><td>613.20 (-1.18%)</td><td>492.92 (+7.33%)</td><td>488.60 (-7.20%)</td><td>345.40 <b>(+41.56%)</b></td><td>99.72 <b>(-44.95%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>620.50 (n/a)</td><td>459.24 (n/a)</td><td>526.50 (n/a)</td><td>244.00 (n/a)</td><td>181.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (-12.41%)</td><td>0.02 (+1.26%)</td><td>0.02 (-13.64%)</td><td>0.02 <b>(+36.92%)</b></td><td>0.01 <b>(-43.21%)</b></td><td>416.60 <b>(-26.96%)</b></td><td>349.32 (-10.60%)</td><td>375.90 (+15.80%)</td><td>245.90 (+14.16%)</td><td>68.78 <b>(-56.37%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.40 (n/a)</td><td>390.74 (n/a)</td><td>324.60 (n/a)</td><td>215.40 (n/a)</td><td>157.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (-12.97%)</td><td>0.03 (-17.16%)</td><td>0.02 <b>(-30.14%)</b></td><td>0.02 (-11.17%)</td><td>0.01 (-18.37%)</td><td>606.50 (+12.56%)</td><td>435.42 (+18.35%)</td><td>423.80 <b>(+43.13%)</b></td><td>273.50 (+14.92%)</td><td>156.71 (+3.42%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.80 (n/a)</td><td>367.92 (n/a)</td><td>296.10 (n/a)</td><td>238.00 (n/a)</td><td>151.53 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (+8.21%)</td><td>0.02 (+16.36%)</td><td>0.02 <b>(+38.97%)</b></td><td>0.01 (+3.04%)</td><td>0.01 (-4.93%)</td><td>591.50 (-2.95%)</td><td>393.32 (-16.79%)</td><td>420.70 <b>(-28.04%)</b></td><td>240.60 (-7.57%)</td><td>136.60 (-19.83%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.50 (n/a)</td><td>472.70 (n/a)</td><td>584.60 (n/a)</td><td>260.30 (n/a)</td><td>170.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 <b>(-22.83%)</b></td><td>0.02 (-17.76%)</td><td>0.02 (-0.61%)</td><td>0.02 (+10.29%)</td><td>0.01 <b>(-51.71%)</b></td><td>557.40 (-9.34%)</td><td>450.40 (+9.80%)</td><td>457.20 (+0.62%)</td><td>302.80 <b>(+29.57%)</b></td><td>96.54 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.80 (n/a)</td><td>410.20 (n/a)</td><td>454.40 (n/a)</td><td>233.70 (n/a)</td><td>164.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (+19.84%)</td><td>0.02 <b>(+30.25%)</b></td><td>0.02 <b>(+26.52%)</b></td><td>0.01 <b>(+228.64%)</b></td><td>0.01 (-2.54%)</td><td>623.80 <b>(-69.57%)</b></td><td>416.16 <b>(-45.26%)</b></td><td>411.20 <b>(-20.95%)</b></td><td>209.50 (-16.53%)</td><td>152.11 <b>(-79.15%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2049.90 (n/a)</td><td>760.20 (n/a)</td><td>520.20 (n/a)</td><td>251.00 (n/a)</td><td>729.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (-15.14%)</td><td>0.02 (-8.76%)</td><td>0.02 (-7.64%)</td><td>0.02 <b>(+26.26%)</b></td><td>0.01 <b>(-38.77%)</b></td><td>496.70 <b>(-20.79%)</b></td><td>443.90 (+2.22%)</td><td>481.80 (+8.27%)</td><td>291.70 (+17.86%)</td><td>85.77 <b>(-43.66%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.10 (n/a)</td><td>434.24 (n/a)</td><td>445.00 (n/a)</td><td>247.50 (n/a)</td><td>152.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 <b>(+46.77%)</b></td><td>0.02 <b>(+31.01%)</b></td><td>0.02 <b>(+30.47%)</b></td><td>0.02 (+12.84%)</td><td>0.01 <b>(+105.18%)</b></td><td>511.30 (-11.39%)</td><td>385.76 <b>(-21.54%)</b></td><td>399.40 <b>(-23.35%)</b></td><td>268.00 <b>(-31.86%)</b></td><td>90.56 <b>(+23.32%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.00 (n/a)</td><td>491.68 (n/a)</td><td>521.10 (n/a)</td><td>393.30 (n/a)</td><td>73.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.37 (+2.43%)</td><td>0.24 (-1.97%)</td><td>0.20 <b>(-31.97%)</b></td><td>0.17 <b>(+252.99%)</b></td><td>0.09 <b>(-26.76%)</b></td><td>593.90 <b>(-71.67%)</b></td><td>448.32 <b>(-35.37%)</b></td><td>482.10 <b>(+46.98%)</b></td><td>265.60 (-2.39%)</td><td>153.60 <b>(-80.51%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>2096.50 (n/a)</td><td>693.70 (n/a)</td><td>328.00 (n/a)</td><td>272.10 (n/a)</td><td>788.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.58 <b>(+46.97%)</b></td><td>0.23 (-19.61%)</td><td>0.19 <b>(-39.94%)</b></td><td>0.05 <b>(-72.49%)</b></td><td>0.20 <b>(+111.59%)</b></td><td>1983.30 <b>(+263.44%)</b></td><td>759.48 <b>(+104.77%)</b></td><td>522.80 <b>(+66.50%)</b></td><td>170.10 <b>(-31.96%)</b></td><td>705.76 <b>(+432.86%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>545.70 (n/a)</td><td>370.90 (n/a)</td><td>314.00 (n/a)</td><td>250.00 (n/a)</td><td>132.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.27 <b>(-35.60%)</b></td><td>0.20 <b>(-31.08%)</b></td><td>0.18 <b>(-45.02%)</b></td><td>0.16 (-5.26%)</td><td>0.05 <b>(-60.18%)</b></td><td>605.80 (+5.56%)</td><td>498.08 <b>(+31.22%)</b></td><td>540.10 <b>(+81.85%)</b></td><td>358.40 <b>(+55.29%)</b></td><td>98.26 <b>(-38.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>573.90 (n/a)</td><td>379.58 (n/a)</td><td>297.00 (n/a)</td><td>230.80 (n/a)</td><td>159.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.38 <b>(+36.33%)</b></td><td>0.29 <b>(+22.89%)</b></td><td>0.29 (+14.42%)</td><td>0.23 <b>(+80.46%)</b></td><td>0.05 (-9.93%)</td><td>315.40 <b>(-44.59%)</b></td><td>259.64 <b>(-23.02%)</b></td><td>251.00 (-12.60%)</td><td>196.20 <b>(-26.65%)</b></td><td>45.85 <b>(-64.71%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>569.20 (n/a)</td><td>337.30 (n/a)</td><td>287.20 (n/a)</td><td>267.50 (n/a)</td><td>129.91 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.30 (+11.68%)</td><td>0.21 (+0.19%)</td><td>0.17 (-8.04%)</td><td>0.12 <b>(-27.03%)</b></td><td>0.08 <b>(+97.88%)</b></td><td>618.70 <b>(+37.06%)</b></td><td>410.00 (+10.48%)</td><td>431.60 (+8.74%)</td><td>247.70 (-10.45%)</td><td>160.61 <b>(+126.58%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>451.40 (n/a)</td><td>371.12 (n/a)</td><td>396.90 (n/a)</td><td>276.60 (n/a)</td><td>70.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.30 <b>(+30.22%)</b></td><td>0.16 (-8.00%)</td><td>0.13 <b>(-25.96%)</b></td><td>0.11 (+4.28%)</td><td>0.08 <b>(+71.54%)</b></td><td>650.70 (-4.11%)</td><td>508.96 (+15.66%)</td><td>558.80 <b>(+35.07%)</b></td><td>246.80 <b>(-23.21%)</b></td><td>165.35 (+18.31%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>678.60 (n/a)</td><td>440.04 (n/a)</td><td>413.70 (n/a)</td><td>321.40 (n/a)</td><td>139.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.42 (-15.45%)</td><td>0.27 (-2.75%)</td><td>0.26 (-5.75%)</td><td>0.19 (+18.63%)</td><td>0.09 <b>(-33.12%)</b></td><td>691.20 (-15.71%)</td><td>519.06 (-5.28%)</td><td>502.90 (+6.12%)</td><td>313.80 (+18.24%)</td><td>141.35 <b>(-35.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.49 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>820.00 (n/a)</td><td>548.02 (n/a)</td><td>473.90 (n/a)</td><td>265.40 (n/a)</td><td>219.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.60 <b>(+75.46%)</b></td><td>0.30 <b>(+44.82%)</b></td><td>0.25 (-0.71%)</td><td>0.15 <b>(+137.92%)</b></td><td>0.17 <b>(+52.32%)</b></td><td>867.80 <b>(-57.97%)</b></td><td>525.76 <b>(-41.64%)</b></td><td>515.40 (+0.72%)</td><td>219.90 <b>(-43.02%)</b></td><td>231.89 <b>(-66.80%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>0.11 (n/a)</td><td>2064.80 (n/a)</td><td>900.82 (n/a)</td><td>511.70 (n/a)</td><td>385.90 (n/a)</td><td>698.50 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.44 (-7.54%)</td><td>0.28 (-11.85%)</td><td>0.26 (-13.40%)</td><td>0.20 (+17.67%)</td><td>0.09 <b>(-22.94%)</b></td><td>653.40 (-15.02%)</td><td>501.94 (+7.07%)</td><td>494.80 (+15.47%)</td><td>299.20 (+8.17%)</td><td>134.75 <b>(-31.30%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>768.90 (n/a)</td><td>468.80 (n/a)</td><td>428.50 (n/a)</td><td>276.60 (n/a)</td><td>196.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.00 <b>(+33.33%)</b></td><td>0.00 <b>(+72.22%)</b></td><td>0.00 <b>(+200.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(-32.30%)</b></td><td>10302.30 <b>(-44.76%)</b></td><td>6924.09 <b>(-48.97%)</b></td><td>6503.73 <b>(-61.43%)</b></td><td>5308.59 <b>(-25.21%)</b></td><td>1952.55 <b>(-67.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18650.65 (n/a)</td><td>13567.80 (n/a)</td><td>16862.69 (n/a)</td><td>7098.01 (n/a)</td><td>5934.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.00 (-18.75%)</td><td>0.00 (-6.06%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-27.28%)</b></td><td>21600.47 (+2.00%)</td><td>16419.12 (+0.91%)</td><td>17377.31 (-5.77%)</td><td>6258.70 (+18.44%)</td><td>6164.95 (-6.21%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21177.89 (n/a)</td><td>16270.58 (n/a)</td><td>18440.41 (n/a)</td><td>5284.27 (n/a)</td><td>6572.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.15 (+8.92%)</td><td>0.10 (-5.24%)</td><td>0.08 (-12.79%)</td><td>0.07 (-2.39%)</td><td>0.03 (+16.00%)</td><td>28479.25 (+2.33%)</td><td>22758.06 (+6.82%)</td><td>25219.72 (+14.68%)</td><td>14198.62 (-8.17%)</td><td>5702.61 (+9.32%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27830.72 (n/a)</td><td>21305.12 (n/a)</td><td>21990.48 (n/a)</td><td>15462.39 (n/a)</td><td>5216.31 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
