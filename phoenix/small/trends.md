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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (+5.17%)</td><td>0.04 (+18.89%)</td><td>0.04 <b>(+55.17%)</b></td><td>0.03 <b>(+24.95%)</b></td><td>0.01 <b>(-29.09%)</b></td><td>473.40 (-19.97%)</td><td>342.50 <b>(-20.67%)</b></td><td>305.70 <b>(-35.56%)</b></td><td>260.10 (-4.90%)</td><td>82.83 <b>(-42.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>431.76 (n/a)</td><td>474.40 (n/a)</td><td>273.50 (n/a)</td><td>143.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (-6.68%)</td><td>0.04 (-6.79%)</td><td>0.04 (-1.97%)</td><td>0.02 (-14.30%)</td><td>0.01 (+15.31%)</td><td>577.90 (+16.70%)</td><td>347.50 (+11.12%)</td><td>289.00 (+2.01%)</td><td>244.40 (+7.19%)</td><td>140.36 <b>(+33.12%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.20 (n/a)</td><td>312.72 (n/a)</td><td>283.30 (n/a)</td><td>228.00 (n/a)</td><td>105.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (-1.23%)</td><td>0.03 (-6.39%)</td><td>0.02 (-17.16%)</td><td>0.01 <b>(+88.64%)</b></td><td>0.01 (-9.63%)</td><td>1077.60 <b>(-46.99%)</b></td><td>592.14 (-18.93%)</td><td>529.80 <b>(+20.71%)</b></td><td>243.20 (+1.25%)</td><td>303.08 <b>(-58.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2032.80 (n/a)</td><td>730.38 (n/a)</td><td>438.90 (n/a)</td><td>240.20 (n/a)</td><td>735.76 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (+14.26%)</td><td>0.02 (+0.10%)</td><td>0.02 (+16.40%)</td><td>0.01 <b>(-25.55%)</b></td><td>0.01 <b>(+103.01%)</b></td><td>578.40 <b>(+34.32%)</b></td><td>361.76 (+12.98%)</td><td>263.10 (-14.10%)</td><td>219.50 (-12.48%)</td><td>166.82 <b>(+139.57%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>430.60 (n/a)</td><td>320.20 (n/a)</td><td>306.30 (n/a)</td><td>250.80 (n/a)</td><td>69.63 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (-1.47%)</td><td>0.01 (-9.55%)</td><td>0.01 <b>(-43.71%)</b></td><td>0.01 (+5.74%)</td><td>0.01 (+2.15%)</td><td>553.80 (-5.41%)</td><td>411.28 (+10.09%)</td><td>466.80 <b>(+77.69%)</b></td><td>240.70 (+1.48%)</td><td>157.79 (-5.11%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.50 (n/a)</td><td>373.58 (n/a)</td><td>262.70 (n/a)</td><td>237.20 (n/a)</td><td>166.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (-10.89%)</td><td>0.02 (+12.95%)</td><td>0.01 (+7.53%)</td><td>0.01 (+11.05%)</td><td>0.01 (-11.27%)</td><td>539.30 (-9.95%)</td><td>370.40 (-13.58%)</td><td>415.40 (-7.01%)</td><td>224.00 (+12.22%)</td><td>135.08 (-9.99%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.90 (n/a)</td><td>428.58 (n/a)</td><td>446.70 (n/a)</td><td>199.60 (n/a)</td><td>150.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 <b>(+72.30%)</b></td><td>0.01 <b>(+22.72%)</b></td><td>0.01 (+3.29%)</td><td>0.01 (+15.47%)</td><td>0.01 <b>(+142.84%)</b></td><td>611.00 (-13.39%)</td><td>458.24 (-13.04%)</td><td>461.80 (-3.19%)</td><td>245.90 <b>(-41.95%)</b></td><td>142.97 (+19.93%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>705.50 (n/a)</td><td>526.94 (n/a)</td><td>477.00 (n/a)</td><td>423.60 (n/a)</td><td>119.20 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 <b>(-27.03%)</b></td><td>0.01 (-13.02%)</td><td>0.02 (+3.80%)</td><td>0.01 (-12.50%)</td><td>0.00 <b>(-32.19%)</b></td><td>537.40 (+14.29%)</td><td>384.40 (+12.35%)</td><td>349.00 (-3.67%)</td><td>267.10 <b>(+37.04%)</b></td><td>117.77 (+8.78%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>470.20 (n/a)</td><td>342.16 (n/a)</td><td>362.30 (n/a)</td><td>194.90 (n/a)</td><td>108.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 <b>(+86.08%)</b></td><td>0.02 <b>(+49.42%)</b></td><td>0.01 (+6.71%)</td><td>0.01 (+10.13%)</td><td>0.01 <b>(+191.55%)</b></td><td>544.00 (-9.20%)</td><td>364.28 <b>(-23.84%)</b></td><td>416.50 (-6.28%)</td><td>175.40 <b>(-46.28%)</b></td><td>153.47 <b>(+36.57%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.10 (n/a)</td><td>478.30 (n/a)</td><td>444.40 (n/a)</td><td>326.50 (n/a)</td><td>112.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>414.40 (n/a)</td><td>307.64 (n/a)</td><td>268.30 (n/a)</td><td>260.20 (n/a)</td><td>67.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>553.50 (n/a)</td><td>396.46 (n/a)</td><td>430.30 (n/a)</td><td>187.20 (n/a)</td><td>167.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>579.30 (n/a)</td><td>485.80 (n/a)</td><td>509.20 (n/a)</td><td>376.90 (n/a)</td><td>75.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1849.40 (n/a)</td><td>652.12 (n/a)</td><td>363.50 (n/a)</td><td>233.00 (n/a)</td><td>677.82 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.00 (n/a)</td><td>408.64 (n/a)</td><td>430.70 (n/a)</td><td>253.00 (n/a)</td><td>89.20 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>587.70 (n/a)</td><td>425.10 (n/a)</td><td>491.20 (n/a)</td><td>223.20 (n/a)</td><td>167.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.30 (n/a)</td><td>325.74 (n/a)</td><td>273.00 (n/a)</td><td>204.50 (n/a)</td><td>169.20 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.10 (n/a)</td><td>334.10 (n/a)</td><td>281.00 (n/a)</td><td>252.30 (n/a)</td><td>113.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.90 (n/a)</td><td>340.62 (n/a)</td><td>267.00 (n/a)</td><td>184.30 (n/a)</td><td>153.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>662.00 (n/a)</td><td>354.44 (n/a)</td><td>272.70 (n/a)</td><td>192.30 (n/a)</td><td>186.90 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.60 (n/a)</td><td>392.72 (n/a)</td><td>311.20 (n/a)</td><td>189.90 (n/a)</td><td>181.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.40 (n/a)</td><td>520.42 (n/a)</td><td>546.30 (n/a)</td><td>323.40 (n/a)</td><td>122.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.55 (-1.07%)</td><td>0.39 <b>(+27.85%)</b></td><td>0.38 (+18.63%)</td><td>0.27 <b>(+117.30%)</b></td><td>0.11 <b>(-42.76%)</b></td><td>831.30 <b>(-53.98%)</b></td><td>605.80 <b>(-42.36%)</b></td><td>578.00 (-15.71%)</td><td>398.80 (+1.06%)</td><td>156.76 <b>(-77.27%)</b></td><td>23.66 (-1.07%)</td><td>16.48 <b>(+27.85%)</b></td><td>16.33 (+18.63%)</td><td>11.35 <b>(+117.30%)</b></td><td>4.53 <b>(-42.76%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.56 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>0.19 (n/a)</td><td>1806.40 (n/a)</td><td>1051.08 (n/a)</td><td>685.70 (n/a)</td><td>394.60 (n/a)</td><td>689.60 (n/a)</td><td>23.92 (n/a)</td><td>12.89 (n/a)</td><td>13.76 (n/a)</td><td>5.22 (n/a)</td><td>7.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.58 (+2.06%)</td><td>0.43 (+15.66%)</td><td>0.41 <b>(+20.87%)</b></td><td>0.35 <b>(+174.71%)</b></td><td>0.09 <b>(-46.92%)</b></td><td>640.40 <b>(-63.60%)</b></td><td>531.32 <b>(-32.08%)</b></td><td>539.30 (-17.27%)</td><td>383.60 (-2.02%)</td><td>97.01 <b>(-82.64%)</b></td><td>24.60 (+2.06%)</td><td>18.31 (+15.66%)</td><td>17.50 <b>(+20.87%)</b></td><td>14.74 <b>(+174.71%)</b></td><td>3.82 <b>(-46.92%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.56 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.13 (n/a)</td><td>0.17 (n/a)</td><td>1759.40 (n/a)</td><td>782.30 (n/a)</td><td>651.90 (n/a)</td><td>391.50 (n/a)</td><td>558.74 (n/a)</td><td>24.10 (n/a)</td><td>15.83 (n/a)</td><td>14.48 (n/a)</td><td>5.36 (n/a)</td><td>7.19 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.31 (+1.14%)</td><td>0.31 (+0.84%)</td><td>0.31 (+0.60%)</td><td>0.30 (+3.13%)</td><td>0.01 <b>(-21.71%)</b></td><td>84928.90 (-3.03%)</td><td>82433.06 (-0.86%)</td><td>81908.60 (-0.59%)</td><td>80371.30 (-1.13%)</td><td>1885.54 <b>(-25.33%)</b></td><td>213.76 (+1.14%)</td><td>208.50 (+0.84%)</td><td>209.74 (+0.60%)</td><td>202.29 (+3.13%)</td><td>4.74 <b>(-21.71%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>87584.10 (n/a)</td><td>83152.12 (n/a)</td><td>82398.70 (n/a)</td><td>81289.30 (n/a)</td><td>2525.07 (n/a)</td><td>211.34 (n/a)</td><td>206.75 (n/a)</td><td>208.50 (n/a)</td><td>196.15 (n/a)</td><td>6.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>1.03 (+0.71%)</td><td>1.02 (+0.51%)</td><td>1.03 (+1.08%)</td><td>1.00 (+0.18%)</td><td>0.02 <b>(+27.99%)</b></td><td>25275.20 (-0.18%)</td><td>24711.74 (-0.50%)</td><td>24470.90 (-1.07%)</td><td>24431.70 (-0.71%)</td><td>372.08 <b>(+26.62%)</b></td><td>703.18 (+0.71%)</td><td>695.34 (+0.51%)</td><td>702.05 (+1.08%)</td><td>679.71 (+0.18%)</td><td>10.37 <b>(+27.99%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.99 (n/a)</td><td>0.01 (n/a)</td><td>25321.30 (n/a)</td><td>24836.22 (n/a)</td><td>24735.70 (n/a)</td><td>24605.20 (n/a)</td><td>293.85 (n/a)</td><td>698.22 (n/a)</td><td>691.80 (n/a)</td><td>694.54 (n/a)</td><td>678.47 (n/a)</td><td>8.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>1.77 <b>(-51.87%)</b></td><td>1.60 <b>(-31.68%)</b></td><td>1.67 <b>(-21.42%)</b></td><td>1.33 <b>(-21.59%)</b></td><td>0.17 <b>(-77.70%)</b></td><td>6051.40 <b>(+27.53%)</b></td><td>5094.42 <b>(+38.27%)</b></td><td>4826.00 <b>(+27.26%)</b></td><td>4550.60 <b>(+107.79%)</b></td><td>593.74 <b>(-35.90%)</b></td><td>464.54 <b>(-51.87%)</b></td><td>419.14 <b>(-31.68%)</b></td><td>438.03 <b>(-21.42%)</b></td><td>349.33 <b>(-21.59%)</b></td><td>45.07 <b>(-77.70%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>3.68 (n/a)</td><td>2.34 (n/a)</td><td>2.13 (n/a)</td><td>1.70 (n/a)</td><td>0.77 (n/a)</td><td>4745.00 (n/a)</td><td>3684.52 (n/a)</td><td>3792.20 (n/a)</td><td>2190.00 (n/a)</td><td>926.25 (n/a)</td><td>965.27 (n/a)</td><td>613.47 (n/a)</td><td>557.44 (n/a)</td><td>445.50 (n/a)</td><td>202.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.29 (-12.18%)</td><td>0.20 (-7.56%)</td><td>0.20 (+8.63%)</td><td>0.15 (-9.48%)</td><td>0.05 <b>(-26.85%)</b></td><td>8455.20 (+10.47%)</td><td>6365.72 (+5.62%)</td><td>6301.70 (-7.95%)</td><td>4352.70 (+13.86%)</td><td>1462.54 (-10.04%)</td><td>15.42 (-12.18%)</td><td>11.03 (-7.56%)</td><td>10.65 (+8.63%)</td><td>7.94 (-9.48%)</td><td>2.73 <b>(-26.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>7654.00 (n/a)</td><td>6026.84 (n/a)</td><td>6845.70 (n/a)</td><td>3822.70 (n/a)</td><td>1625.82 (n/a)</td><td>17.56 (n/a)</td><td>11.93 (n/a)</td><td>9.80 (n/a)</td><td>8.77 (n/a)</td><td>3.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>3.76 (n/a)</td><td>3.63 (n/a)</td><td>3.71 (n/a)</td><td>3.37 (n/a)</td><td>0.17 (n/a)</td><td>3.76 (n/a)</td><td>3.63 (n/a)</td><td>3.71 (n/a)</td><td>3.37 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>7.62 (+7.85%)</td><td>6.12 (-7.75%)</td><td>5.70 (-16.26%)</td><td>5.63 (-0.11%)</td><td>0.85 <b>(+47.81%)</b></td><td>7.62 (+7.85%)</td><td>6.11 (-7.75%)</td><td>5.70 (-16.26%)</td><td>5.63 (-0.11%)</td><td>0.85 <b>(+47.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>7.07 (n/a)</td><td>6.63 (n/a)</td><td>6.81 (n/a)</td><td>5.64 (n/a)</td><td>0.58 (n/a)</td><td>7.06 (n/a)</td><td>6.63 (n/a)</td><td>6.81 (n/a)</td><td>5.63 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>13.37 (+4.31%)</td><td>9.48 (+0.72%)</td><td>8.52 (-6.81%)</td><td>8.46 (+15.55%)</td><td>2.17 (+0.79%)</td><td>13.36 (+4.31%)</td><td>9.48 (+0.72%)</td><td>8.52 (-6.81%)</td><td>8.45 (+15.55%)</td><td>2.17 (+0.79%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>12.82 (n/a)</td><td>9.42 (n/a)</td><td>9.14 (n/a)</td><td>7.32 (n/a)</td><td>2.16 (n/a)</td><td>12.81 (n/a)</td><td>9.41 (n/a)</td><td>9.14 (n/a)</td><td>7.32 (n/a)</td><td>2.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>3.73 (n/a)</td><td>3.44 (n/a)</td><td>3.42 (n/a)</td><td>3.27 (n/a)</td><td>0.17 (n/a)</td><td>3.73 (n/a)</td><td>3.44 (n/a)</td><td>3.41 (n/a)</td><td>3.27 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>7.54 (+0.86%)</td><td>6.89 (+3.45%)</td><td>7.01 (+3.95%)</td><td>5.95 (+5.26%)</td><td>0.61 (-11.04%)</td><td>7.53 (+0.86%)</td><td>6.88 (+3.45%)</td><td>7.01 (+3.95%)</td><td>5.95 (+5.26%)</td><td>0.61 (-11.04%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>7.47 (n/a)</td><td>6.66 (n/a)</td><td>6.74 (n/a)</td><td>5.65 (n/a)</td><td>0.69 (n/a)</td><td>7.47 (n/a)</td><td>6.65 (n/a)</td><td>6.74 (n/a)</td><td>5.65 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>14.15 (+2.47%)</td><td>10.89 (+13.87%)</td><td>9.35 (+8.49%)</td><td>8.51 (+16.00%)</td><td>2.88 (+9.43%)</td><td>14.14 (+2.47%)</td><td>10.89 (+13.87%)</td><td>9.35 (+8.49%)</td><td>8.51 (+16.00%)</td><td>2.87 (+9.43%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>13.81 (n/a)</td><td>9.57 (n/a)</td><td>8.62 (n/a)</td><td>7.34 (n/a)</td><td>2.63 (n/a)</td><td>13.80 (n/a)</td><td>9.56 (n/a)</td><td>8.62 (n/a)</td><td>7.34 (n/a)</td><td>2.63 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>3.38 (+12.51%)</td><td>2.11 (+2.15%)</td><td>1.52 (-9.14%)</td><td>1.17 (-16.49%)</td><td>1.11 <b>(+46.06%)</b></td><td>3.38 (+12.51%)</td><td>2.10 (+2.15%)</td><td>1.51 (-9.14%)</td><td>1.17 (-16.49%)</td><td>1.11 <b>(+46.06%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>3.01 (n/a)</td><td>2.06 (n/a)</td><td>1.67 (n/a)</td><td>1.40 (n/a)</td><td>0.76 (n/a)</td><td>3.00 (n/a)</td><td>2.06 (n/a)</td><td>1.67 (n/a)</td><td>1.40 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.61 (+19.88%)</td><td>0.36 <b>(+28.67%)</b></td><td>0.33 <b>(+31.90%)</b></td><td>0.08 (+0.31%)</td><td>0.20 (-4.49%)</td><td>0.60 (+19.88%)</td><td>0.35 <b>(+28.67%)</b></td><td>0.33 <b>(+31.90%)</b></td><td>0.07 (+0.31%)</td><td>0.20 (-4.49%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.51 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>0.50 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.76 <b>(+35.24%)</b></td><td>0.38 (+2.63%)</td><td>0.27 <b>(-21.37%)</b></td><td>0.07 <b>(-73.92%)</b></td><td>0.34 <b>(+198.34%)</b></td><td>0.75 <b>(+35.24%)</b></td><td>0.38 (+2.63%)</td><td>0.27 <b>(-21.37%)</b></td><td>0.07 <b>(-73.92%)</b></td><td>0.33 <b>(+198.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.56 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>0.56 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>2.46 (+1.97%)</td><td>1.48 (+4.26%)</td><td>1.31 (+14.29%)</td><td>0.45 (+1.77%)</td><td>0.90 (-2.00%)</td><td>2.42 (+1.97%)</td><td>1.46 (+4.26%)</td><td>1.29 (+14.29%)</td><td>0.44 (+1.77%)</td><td>0.88 (-2.00%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>2.41 (n/a)</td><td>1.42 (n/a)</td><td>1.15 (n/a)</td><td>0.44 (n/a)</td><td>0.92 (n/a)</td><td>2.37 (n/a)</td><td>1.40 (n/a)</td><td>1.13 (n/a)</td><td>0.43 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.60 (n/a)</td><td>469.60 (n/a)</td><td>562.50 (n/a)</td><td>270.50 (n/a)</td><td>156.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.40 (n/a)</td><td>375.66 (n/a)</td><td>371.80 (n/a)</td><td>265.00 (n/a)</td><td>99.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.40 (n/a)</td><td>393.66 (n/a)</td><td>425.60 (n/a)</td><td>216.50 (n/a)</td><td>160.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.30 (n/a)</td><td>468.40 (n/a)</td><td>487.20 (n/a)</td><td>346.20 (n/a)</td><td>87.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.70 (n/a)</td><td>369.66 (n/a)</td><td>339.70 (n/a)</td><td>272.90 (n/a)</td><td>93.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1538.00 (n/a)</td><td>688.54 (n/a)</td><td>490.50 (n/a)</td><td>356.20 (n/a)</td><td>482.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (+10.15%)</td><td>0.03 (+7.52%)</td><td>0.03 (+8.01%)</td><td>0.02 (+0.23%)</td><td>0.01 (+8.37%)</td><td>538.00 (-0.24%)</td><td>353.20 (-6.65%)</td><td>276.40 (-7.43%)</td><td>241.20 (-9.22%)</td><td>132.26 (-3.35%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.30 (n/a)</td><td>378.38 (n/a)</td><td>298.60 (n/a)</td><td>265.70 (n/a)</td><td>136.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (+3.66%)</td><td>0.03 (-3.27%)</td><td>0.03 (+4.26%)</td><td>0.02 <b>(+21.34%)</b></td><td>0.01 (+11.61%)</td><td>472.00 (-17.60%)</td><td>332.06 (+3.49%)</td><td>257.30 (-4.10%)</td><td>226.30 (-3.54%)</td><td>127.67 (-10.65%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.80 (n/a)</td><td>320.86 (n/a)</td><td>268.30 (n/a)</td><td>234.60 (n/a)</td><td>142.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (-18.40%)</td><td>0.02 <b>(-32.20%)</b></td><td>0.02 <b>(-42.53%)</b></td><td>0.02 <b>(-42.78%)</b></td><td>0.01 <b>(+66.38%)</b></td><td>526.70 <b>(+74.81%)</b></td><td>403.60 <b>(+57.59%)</b></td><td>421.40 <b>(+73.99%)</b></td><td>275.20 <b>(+22.53%)</b></td><td>122.43 <b>(+250.66%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>301.30 (n/a)</td><td>256.10 (n/a)</td><td>242.20 (n/a)</td><td>224.60 (n/a)</td><td>34.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 <b>(-49.20%)</b></td><td>0.02 <b>(-44.13%)</b></td><td>0.02 <b>(-44.66%)</b></td><td>0.01 (-10.63%)</td><td>0.00 <b>(-83.91%)</b></td><td>598.30 (+11.89%)</td><td>536.10 <b>(+65.93%)</b></td><td>526.40 <b>(+80.71%)</b></td><td>487.80 <b>(+96.85%)</b></td><td>41.65 <b>(-65.37%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.70 (n/a)</td><td>323.08 (n/a)</td><td>291.30 (n/a)</td><td>247.80 (n/a)</td><td>120.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 <b>(-45.36%)</b></td><td>0.01 <b>(-46.24%)</b></td><td>0.01 <b>(-44.01%)</b></td><td>0.01 <b>(-49.34%)</b></td><td>0.00 <b>(-45.10%)</b></td><td>1052.90 <b>(+97.39%)</b></td><td>642.18 <b>(+87.85%)</b></td><td>558.50 <b>(+78.61%)</b></td><td>482.90 <b>(+83.06%)</b></td><td>231.93 <b>(+109.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.40 (n/a)</td><td>341.86 (n/a)</td><td>312.70 (n/a)</td><td>263.80 (n/a)</td><td>110.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (-17.93%)</td><td>0.02 (-2.46%)</td><td>0.02 (+12.01%)</td><td>0.00 <b>(+25.86%)</b></td><td>0.01 <b>(-20.72%)</b></td><td>1934.50 <b>(-20.54%)</b></td><td>745.24 (-12.11%)</td><td>476.00 (-10.73%)</td><td>293.60 <b>(+21.83%)</b></td><td>675.15 <b>(-24.68%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2434.70 (n/a)</td><td>847.94 (n/a)</td><td>533.20 (n/a)</td><td>241.00 (n/a)</td><td>896.32 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 <b>(-32.99%)</b></td><td>0.02 <b>(-28.29%)</b></td><td>0.02 <b>(-37.78%)</b></td><td>0.01 (-1.74%)</td><td>0.00 <b>(-60.75%)</b></td><td>553.50 (+1.77%)</td><td>477.16 <b>(+29.62%)</b></td><td>472.90 <b>(+60.69%)</b></td><td>362.20 <b>(+49.24%)</b></td><td>76.05 <b>(-42.16%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.90 (n/a)</td><td>368.12 (n/a)</td><td>294.30 (n/a)</td><td>242.70 (n/a)</td><td>131.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (-7.78%)</td><td>0.02 <b>(+37.63%)</b></td><td>0.02 <b>(+22.65%)</b></td><td>0.01 <b>(+335.49%)</b></td><td>0.01 <b>(-50.12%)</b></td><td>562.00 <b>(-77.04%)</b></td><td>437.12 <b>(-57.02%)</b></td><td>455.20 (-18.48%)</td><td>296.20 (+8.42%)</td><td>105.91 <b>(-88.19%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2447.50 (n/a)</td><td>1016.94 (n/a)</td><td>558.40 (n/a)</td><td>273.20 (n/a)</td><td>897.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (+18.73%)</td><td>0.02 (-9.90%)</td><td>0.02 (-11.81%)</td><td>0.00 <b>(-71.50%)</b></td><td>0.01 <b>(+88.46%)</b></td><td>2036.40 <b>(+250.86%)</b></td><td>729.88 <b>(+71.64%)</b></td><td>472.20 (+13.40%)</td><td>238.10 (-15.78%)</td><td>736.82 <b>(+545.13%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.40 (n/a)</td><td>425.24 (n/a)</td><td>416.40 (n/a)</td><td>282.70 (n/a)</td><td>114.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (+12.84%)</td><td>0.02 (-16.93%)</td><td>0.02 <b>(-38.43%)</b></td><td>0.02 (-17.22%)</td><td>0.01 <b>(+55.06%)</b></td><td>514.20 <b>(+20.79%)</b></td><td>419.86 <b>(+26.40%)</b></td><td>472.50 <b>(+62.43%)</b></td><td>231.20 (-11.38%)</td><td>113.48 <b>(+57.06%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.70 (n/a)</td><td>332.16 (n/a)</td><td>290.90 (n/a)</td><td>260.90 (n/a)</td><td>72.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (-13.37%)</td><td>0.02 (-9.77%)</td><td>0.03 (-1.93%)</td><td>0.02 (+3.10%)</td><td>0.01 (-11.66%)</td><td>540.00 (-3.00%)</td><td>378.42 (+10.09%)</td><td>293.00 (+1.98%)</td><td>258.30 (+15.47%)</td><td>147.01 (+4.05%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.70 (n/a)</td><td>343.74 (n/a)</td><td>287.30 (n/a)</td><td>223.70 (n/a)</td><td>141.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (+13.88%)</td><td>0.02 (+10.99%)</td><td>0.02 (+2.83%)</td><td>0.01 <b>(+65.86%)</b></td><td>0.01 (+8.36%)</td><td>645.40 <b>(-39.70%)</b></td><td>439.24 (-16.50%)</td><td>468.40 (-2.76%)</td><td>213.70 (-12.20%)</td><td>193.83 <b>(-41.19%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1070.40 (n/a)</td><td>526.04 (n/a)</td><td>481.70 (n/a)</td><td>243.40 (n/a)</td><td>329.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 <b>(+61.34%)</b></td><td>0.02 <b>(+44.03%)</b></td><td>0.02 (+4.66%)</td><td>0.01 <b>(+67.09%)</b></td><td>0.01 <b>(+28.07%)</b></td><td>626.90 <b>(-40.16%)</b></td><td>441.52 <b>(-34.05%)</b></td><td>473.80 (-4.46%)</td><td>275.70 <b>(-38.02%)</b></td><td>135.13 <b>(-52.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1047.60 (n/a)</td><td>669.48 (n/a)</td><td>495.90 (n/a)</td><td>444.80 (n/a)</td><td>284.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 <b>(-26.90%)</b></td><td>0.02 (-19.48%)</td><td>0.02 (-10.25%)</td><td>0.01 <b>(-21.73%)</b></td><td>0.00 <b>(-31.26%)</b></td><td>679.90 <b>(+27.78%)</b></td><td>496.76 <b>(+23.31%)</b></td><td>450.30 (+11.41%)</td><td>396.00 <b>(+36.79%)</b></td><td>115.84 <b>(+21.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.10 (n/a)</td><td>402.86 (n/a)</td><td>404.20 (n/a)</td><td>289.50 (n/a)</td><td>95.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (+19.08%)</td><td>0.03 <b>(+48.18%)</b></td><td>0.03 <b>(+104.69%)</b></td><td>0.02 <b>(+31.38%)</b></td><td>0.01 <b>(+43.32%)</b></td><td>514.60 <b>(-23.89%)</b></td><td>347.40 <b>(-30.17%)</b></td><td>261.30 <b>(-51.14%)</b></td><td>237.60 (-16.01%)</td><td>139.66 (-3.98%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.10 (n/a)</td><td>497.50 (n/a)</td><td>534.80 (n/a)</td><td>282.90 (n/a)</td><td>145.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (+14.33%)</td><td>0.04 (+15.36%)</td><td>0.05 <b>(+62.79%)</b></td><td>0.01 <b>(-23.03%)</b></td><td>0.02 <b>(+54.17%)</b></td><td>921.60 <b>(+29.91%)</b></td><td>448.72 (+1.73%)</td><td>267.40 <b>(-38.57%)</b></td><td>246.10 (-12.51%)</td><td>294.49 <b>(+70.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>709.40 (n/a)</td><td>441.10 (n/a)</td><td>435.30 (n/a)</td><td>281.30 (n/a)</td><td>172.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (+2.05%)</td><td>0.02 (-12.98%)</td><td>0.02 (+2.49%)</td><td>0.00 <b>(-70.06%)</b></td><td>0.01 (+17.75%)</td><td>2003.00 <b>(+234.00%)</b></td><td>680.98 <b>(+74.34%)</b></td><td>419.60 (-2.42%)</td><td>229.20 (-1.97%)</td><td>744.59 <b>(+377.02%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.70 (n/a)</td><td>390.60 (n/a)</td><td>430.00 (n/a)</td><td>233.80 (n/a)</td><td>156.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 <b>(+20.58%)</b></td><td>0.03 (+2.53%)</td><td>0.03 <b>(-29.40%)</b></td><td>0.01 <b>(+167.78%)</b></td><td>0.02 (-6.98%)</td><td>699.50 <b>(-62.66%)</b></td><td>408.30 <b>(-34.70%)</b></td><td>392.70 <b>(+41.67%)</b></td><td>190.20 (-17.05%)</td><td>201.18 <b>(-71.55%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1873.20 (n/a)</td><td>625.30 (n/a)</td><td>277.20 (n/a)</td><td>229.30 (n/a)</td><td>707.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 <b>(+31.16%)</b></td><td>0.03 <b>(+26.79%)</b></td><td>0.03 <b>(+40.77%)</b></td><td>0.01 (-14.91%)</td><td>0.01 <b>(+111.43%)</b></td><td>610.50 (+17.54%)</td><td>368.20 (-11.10%)</td><td>292.60 <b>(-28.95%)</b></td><td>215.40 <b>(-23.78%)</b></td><td>172.01 <b>(+94.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.40 (n/a)</td><td>414.18 (n/a)</td><td>411.80 (n/a)</td><td>282.60 (n/a)</td><td>88.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (+13.99%)</td><td>0.03 <b>(+36.56%)</b></td><td>0.03 <b>(+75.43%)</b></td><td>0.02 <b>(+246.06%)</b></td><td>0.01 <b>(-27.57%)</b></td><td>551.60 <b>(-71.11%)</b></td><td>357.76 <b>(-50.58%)</b></td><td>311.20 <b>(-42.99%)</b></td><td>233.10 (-12.30%)</td><td>127.93 <b>(-81.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1909.00 (n/a)</td><td>723.96 (n/a)</td><td>545.90 (n/a)</td><td>265.80 (n/a)</td><td>679.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (+1.92%)</td><td>0.02 <b>(+33.08%)</b></td><td>0.03 <b>(+74.94%)</b></td><td>0.02 <b>(+367.04%)</b></td><td>0.01 <b>(-35.65%)</b></td><td>527.10 <b>(-78.59%)</b></td><td>365.30 <b>(-55.54%)</b></td><td>290.80 <b>(-42.85%)</b></td><td>268.50 (-1.86%)</td><td>116.77 <b>(-87.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2461.60 (n/a)</td><td>821.58 (n/a)</td><td>508.80 (n/a)</td><td>273.60 (n/a)</td><td>925.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 <b>(+55.17%)</b></td><td>0.02 (+12.11%)</td><td>0.02 (-13.83%)</td><td>0.01 (+8.38%)</td><td>0.01 <b>(+63.66%)</b></td><td>627.30 (-7.74%)</td><td>438.88 (-6.09%)</td><td>493.70 (+16.06%)</td><td>191.10 <b>(-35.57%)</b></td><td>166.58 (-7.12%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.90 (n/a)</td><td>467.32 (n/a)</td><td>425.40 (n/a)</td><td>296.60 (n/a)</td><td>179.36 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (+11.63%)</td><td>0.02 (+8.52%)</td><td>0.02 (+13.48%)</td><td>0.02 (+14.25%)</td><td>0.01 (+16.97%)</td><td>522.90 (-12.49%)</td><td>400.40 (-7.25%)</td><td>369.20 (-11.86%)</td><td>261.50 (-10.41%)</td><td>109.01 (-5.22%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.50 (n/a)</td><td>431.68 (n/a)</td><td>418.90 (n/a)</td><td>291.90 (n/a)</td><td>115.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (+19.81%)</td><td>0.02 (+4.03%)</td><td>0.02 (-6.98%)</td><td>0.02 (+17.38%)</td><td>0.01 <b>(+33.79%)</b></td><td>495.40 (-14.79%)</td><td>406.98 (-2.50%)</td><td>443.40 (+7.49%)</td><td>229.20 (-16.53%)</td><td>103.61 (-9.49%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.40 (n/a)</td><td>417.40 (n/a)</td><td>412.50 (n/a)</td><td>274.60 (n/a)</td><td>114.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 <b>(+57.69%)</b></td><td>0.02 (+15.74%)</td><td>0.02 (-1.47%)</td><td>0.02 (+17.50%)</td><td>0.01 <b>(+143.18%)</b></td><td>532.00 (-14.89%)</td><td>434.40 (-9.91%)</td><td>448.40 (+1.49%)</td><td>268.50 <b>(-36.60%)</b></td><td>108.19 <b>(+29.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>625.10 (n/a)</td><td>482.18 (n/a)</td><td>441.80 (n/a)</td><td>423.50 (n/a)</td><td>83.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.49 <b>(+20.38%)</b></td><td>0.33 <b>(+20.09%)</b></td><td>0.30 <b>(+47.40%)</b></td><td>0.21 (+14.31%)</td><td>0.10 (+3.43%)</td><td>458.80 (-12.53%)</td><td>324.92 (-18.89%)</td><td>323.80 <b>(-32.16%)</b></td><td>198.70 (-16.93%)</td><td>94.13 <b>(-27.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>524.50 (n/a)</td><td>400.60 (n/a)</td><td>477.30 (n/a)</td><td>239.20 (n/a)</td><td>129.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.41 (+16.38%)</td><td>0.27 (+11.71%)</td><td>0.27 <b>(+25.11%)</b></td><td>0.15 (-2.12%)</td><td>0.10 <b>(+33.53%)</b></td><td>645.00 (+2.15%)</td><td>404.32 (-6.68%)</td><td>360.30 <b>(-20.08%)</b></td><td>240.10 (-14.07%)</td><td>159.54 (+19.58%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>631.40 (n/a)</td><td>433.28 (n/a)</td><td>450.80 (n/a)</td><td>279.40 (n/a)</td><td>133.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.26 <b>(-27.59%)</b></td><td>0.22 (-15.95%)</td><td>0.21 (-7.47%)</td><td>0.19 (+3.86%)</td><td>0.03 <b>(-65.54%)</b></td><td>506.80 (-3.72%)</td><td>447.44 (+11.70%)</td><td>467.50 (+8.07%)</td><td>378.60 <b>(+38.07%)</b></td><td>55.55 <b>(-52.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>526.40 (n/a)</td><td>400.56 (n/a)</td><td>432.60 (n/a)</td><td>274.20 (n/a)</td><td>117.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.29 (+4.46%)</td><td>0.25 <b>(+28.72%)</b></td><td>0.25 <b>(+48.49%)</b></td><td>0.21 <b>(+56.54%)</b></td><td>0.04 <b>(-40.20%)</b></td><td>354.30 <b>(-36.12%)</b></td><td>295.58 <b>(-26.39%)</b></td><td>289.20 <b>(-32.65%)</b></td><td>255.40 (-4.24%)</td><td>42.54 <b>(-63.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>554.60 (n/a)</td><td>401.54 (n/a)</td><td>429.40 (n/a)</td><td>266.70 (n/a)</td><td>115.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.40 <b>(+49.00%)</b></td><td>0.26 (+19.75%)</td><td>0.26 (-2.65%)</td><td>0.14 (+0.57%)</td><td>0.09 <b>(+39.51%)</b></td><td>518.40 (-0.58%)</td><td>311.98 (-14.45%)</td><td>282.70 (+2.73%)</td><td>183.70 <b>(-32.91%)</b></td><td>124.05 (-0.11%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>521.40 (n/a)</td><td>364.66 (n/a)</td><td>275.20 (n/a)</td><td>273.80 (n/a)</td><td>124.19 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.31 <b>(+60.98%)</b></td><td>0.22 <b>(+38.29%)</b></td><td>0.24 <b>(+55.12%)</b></td><td>0.11 (-12.42%)</td><td>0.08 <b>(+196.79%)</b></td><td>693.70 (+14.17%)</td><td>391.06 (-18.46%)</td><td>302.70 <b>(-35.54%)</b></td><td>235.00 <b>(-37.90%)</b></td><td>185.06 <b>(+115.69%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>607.60 (n/a)</td><td>479.60 (n/a)</td><td>469.60 (n/a)</td><td>378.40 (n/a)</td><td>85.80 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.40 (-14.69%)</td><td>0.29 (-9.14%)</td><td>0.26 (-0.18%)</td><td>0.24 (+19.23%)</td><td>0.06 <b>(-44.73%)</b></td><td>541.50 (-16.12%)</td><td>470.38 (+2.90%)</td><td>495.80 (+0.18%)</td><td>330.00 (+17.23%)</td><td>81.33 <b>(-46.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>645.60 (n/a)</td><td>457.14 (n/a)</td><td>494.90 (n/a)</td><td>281.50 (n/a)</td><td>151.90 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.43 (+0.05%)</td><td>0.23 <b>(-27.90%)</b></td><td>0.25 (-13.23%)</td><td>0.06 <b>(-77.41%)</b></td><td>0.14 <b>(+113.00%)</b></td><td>2116.00 <b>(+342.59%)</b></td><td>847.44 <b>(+103.86%)</b></td><td>518.20 (+15.26%)</td><td>305.20 (-0.07%)</td><td>729.45 <b>(+943.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>478.10 (n/a)</td><td>415.70 (n/a)</td><td>449.60 (n/a)</td><td>305.40 (n/a)</td><td>69.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.58 <b>(+42.40%)</b></td><td>0.28 (-19.93%)</td><td>0.25 <b>(-36.52%)</b></td><td>0.07 <b>(-70.37%)</b></td><td>0.19 <b>(+130.08%)</b></td><td>1905.50 <b>(+237.56%)</b></td><td>756.44 <b>(+88.63%)</b></td><td>516.00 <b>(+57.56%)</b></td><td>224.30 <b>(-29.77%)</b></td><td>661.24 <b>(+499.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.40 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>564.50 (n/a)</td><td>401.02 (n/a)</td><td>327.50 (n/a)</td><td>319.40 (n/a)</td><td>110.24 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+57.14%)</b></td><td>0.00 <b>(+200.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+22.47%)</b></td><td>19902.07 (-12.22%)</td><td>11585.89 <b>(-32.29%)</b></td><td>6889.62 <b>(-62.80%)</b></td><td>6432.76 (-6.09%)</td><td>6768.42 (+12.89%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22672.46 (n/a)</td><td>17111.07 (n/a)</td><td>18519.71 (n/a)</td><td>6849.84 (n/a)</td><td>5995.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.00 (-8.33%)</td><td>0.00 <b>(+41.94%)</b></td><td>0.00 <b>(+80.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-14.43%)</td><td>18390.82 (-7.70%)</td><td>10461.10 <b>(-31.84%)</b></td><td>9225.85 <b>(-46.89%)</b></td><td>7514.47 (+12.13%)</td><td>4522.32 (-15.61%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19924.70 (n/a)</td><td>15348.30 (n/a)</td><td>17371.91 (n/a)</td><td>6701.35 (n/a)</td><td>5359.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.14 (-4.04%)</td><td>0.10 (-4.62%)</td><td>0.08 (-1.87%)</td><td>0.07 (-4.16%)</td><td>0.03 (-11.75%)</td><td>28464.85 (+4.44%)</td><td>22570.47 (+3.50%)</td><td>26564.40 (+1.86%)</td><td>14963.29 (+4.24%)</td><td>6535.06 (-3.43%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>27254.84 (n/a)</td><td>21807.44 (n/a)</td><td>26079.89 (n/a)</td><td>14355.15 (n/a)</td><td>6767.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>1.58 (+10.20%)</td><td>0.91 (-6.78%)</td><td>0.71 <b>(-33.65%)</b></td><td>0.60 <b>(+131.02%)</b></td><td>0.39 (-8.90%)</td><td>869.80 <b>(-56.72%)</b></td><td>646.82 (-16.24%)</td><td>734.90 <b>(+50.72%)</b></td><td>332.60 (-9.27%)</td><td>208.91 <b>(-69.91%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>1.43 (n/a)</td><td>0.98 (n/a)</td><td>1.08 (n/a)</td><td>0.26 (n/a)</td><td>0.43 (n/a)</td><td>2009.50 (n/a)</td><td>772.24 (n/a)</td><td>487.60 (n/a)</td><td>366.60 (n/a)</td><td>694.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>2.31 (-16.33%)</td><td>1.07 <b>(-30.77%)</b></td><td>0.73 <b>(-57.95%)</b></td><td>0.30 (-6.49%)</td><td>0.90 (-16.64%)</td><td>3536.90 (+6.94%)</td><td>1912.70 <b>(+43.58%)</b></td><td>1435.30 <b>(+137.79%)</b></td><td>453.50 (+19.50%)</td><td>1522.80 (+19.65%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>2.76 (n/a)</td><td>1.54 (n/a)</td><td>1.74 (n/a)</td><td>0.32 (n/a)</td><td>1.08 (n/a)</td><td>3307.30 (n/a)</td><td>1332.18 (n/a)</td><td>603.60 (n/a)</td><td>379.50 (n/a)</td><td>1272.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>2.47 <b>(+44.29%)</b></td><td>1.03 <b>(-23.75%)</b></td><td>0.74 <b>(-49.85%)</b></td><td>0.47 <b>(-43.12%)</b></td><td>0.81 <b>(+141.25%)</b></td><td>1104.80 <b>(+75.78%)</b></td><td>686.80 <b>(+66.93%)</b></td><td>710.50 <b>(+99.41%)</b></td><td>212.60 <b>(-30.70%)</b></td><td>316.74 <b>(+147.22%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>1.71 (n/a)</td><td>1.36 (n/a)</td><td>1.47 (n/a)</td><td>0.83 (n/a)</td><td>0.34 (n/a)</td><td>628.50 (n/a)</td><td>411.42 (n/a)</td><td>356.30 (n/a)</td><td>306.80 (n/a)</td><td>128.12 (n/a)</td>
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
