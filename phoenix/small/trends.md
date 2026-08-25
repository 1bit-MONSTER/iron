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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (-9.64%)</td><td>0.04 (-7.52%)</td><td>0.03 <b>(-22.72%)</b></td><td>0.03 <b>(+28.84%)</b></td><td>0.01 (-19.12%)</td><td>474.70 <b>(-22.38%)</b></td><td>377.62 (+2.91%)</td><td>435.80 <b>(+29.43%)</b></td><td>260.20 (+10.68%)</td><td>107.84 <b>(-30.19%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.60 (n/a)</td><td>366.94 (n/a)</td><td>336.70 (n/a)</td><td>235.10 (n/a)</td><td>154.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (-12.70%)</td><td>0.03 <b>(-22.92%)</b></td><td>0.03 <b>(-26.78%)</b></td><td>0.02 (-7.56%)</td><td>0.01 <b>(-25.64%)</b></td><td>528.20 (+8.19%)</td><td>423.18 <b>(+26.69%)</b></td><td>431.00 <b>(+36.57%)</b></td><td>271.80 (+14.54%)</td><td>93.89 (-10.19%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>488.20 (n/a)</td><td>334.02 (n/a)</td><td>315.60 (n/a)</td><td>237.30 (n/a)</td><td>104.55 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (+10.31%)</td><td>0.03 (-9.75%)</td><td>0.03 <b>(-35.73%)</b></td><td>0.02 (-0.81%)</td><td>0.01 (-8.14%)</td><td>662.60 (+0.82%)</td><td>442.32 (+7.64%)</td><td>458.00 <b>(+55.57%)</b></td><td>256.80 (-9.35%)</td><td>149.40 (-13.65%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>657.20 (n/a)</td><td>410.92 (n/a)</td><td>294.40 (n/a)</td><td>283.30 (n/a)</td><td>173.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (+5.08%)</td><td>0.02 (-13.69%)</td><td>0.01 <b>(-20.65%)</b></td><td>0.01 (-8.30%)</td><td>0.01 <b>(+28.97%)</b></td><td>487.40 (+9.04%)</td><td>356.68 <b>(+21.22%)</b></td><td>365.10 <b>(+26.03%)</b></td><td>190.80 (-4.84%)</td><td>121.51 <b>(+30.49%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>447.00 (n/a)</td><td>294.24 (n/a)</td><td>289.70 (n/a)</td><td>200.50 (n/a)</td><td>93.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (-4.68%)</td><td>0.02 (-10.21%)</td><td>0.02 (-17.08%)</td><td>0.01 (-3.55%)</td><td>0.01 (-9.89%)</td><td>614.20 (+3.68%)</td><td>383.98 (+9.99%)</td><td>346.90 <b>(+20.62%)</b></td><td>241.60 (+4.91%)</td><td>152.07 (-0.30%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.40 (n/a)</td><td>349.10 (n/a)</td><td>287.60 (n/a)</td><td>230.30 (n/a)</td><td>152.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (-16.57%)</td><td>0.02 (-4.44%)</td><td>0.02 (-0.68%)</td><td>0.01 <b>(+42.71%)</b></td><td>0.00 <b>(-38.50%)</b></td><td>431.10 <b>(-29.93%)</b></td><td>328.62 (-5.81%)</td><td>267.20 (+0.68%)</td><td>256.90 (+19.88%)</td><td>92.31 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.20 (n/a)</td><td>348.88 (n/a)</td><td>265.40 (n/a)</td><td>214.30 (n/a)</td><td>171.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 <b>(-25.59%)</b></td><td>0.01 <b>(-33.72%)</b></td><td>0.01 <b>(-35.26%)</b></td><td>0.01 <b>(-27.91%)</b></td><td>0.00 <b>(-30.12%)</b></td><td>751.60 <b>(+38.70%)</b></td><td>512.10 <b>(+49.33%)</b></td><td>485.70 <b>(+54.48%)</b></td><td>291.70 <b>(+34.42%)</b></td><td>174.36 <b>(+31.12%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>541.90 (n/a)</td><td>342.94 (n/a)</td><td>314.40 (n/a)</td><td>217.00 (n/a)</td><td>132.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (+0.94%)</td><td>0.01 (+3.98%)</td><td>0.01 (-3.03%)</td><td>0.01 <b>(+42.70%)</b></td><td>0.01 (-13.73%)</td><td>525.80 <b>(-29.92%)</b></td><td>405.60 (-10.14%)</td><td>441.50 (+3.13%)</td><td>246.50 (-0.92%)</td><td>131.25 <b>(-36.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>750.30 (n/a)</td><td>451.38 (n/a)</td><td>428.10 (n/a)</td><td>248.80 (n/a)</td><td>205.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (-18.82%)</td><td>0.01 (-11.66%)</td><td>0.01 (-10.22%)</td><td>0.01 <b>(+45.95%)</b></td><td>0.00 <b>(-30.88%)</b></td><td>690.60 <b>(-31.49%)</b></td><td>478.84 (-0.67%)</td><td>423.10 (+11.37%)</td><td>305.70 <b>(+23.22%)</b></td><td>176.96 <b>(-42.51%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1008.00 (n/a)</td><td>482.06 (n/a)</td><td>379.90 (n/a)</td><td>248.10 (n/a)</td><td>307.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>465.10 (n/a)</td><td>353.66 (n/a)</td><td>416.00 (n/a)</td><td>193.40 (n/a)</td><td>124.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>443.30 (n/a)</td><td>332.74 (n/a)</td><td>383.20 (n/a)</td><td>177.30 (n/a)</td><td>116.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.90 (n/a)</td><td>358.96 (n/a)</td><td>330.60 (n/a)</td><td>269.30 (n/a)</td><td>110.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.30 (n/a)</td><td>412.52 (n/a)</td><td>394.10 (n/a)</td><td>292.70 (n/a)</td><td>105.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.90 (n/a)</td><td>476.24 (n/a)</td><td>465.90 (n/a)</td><td>235.20 (n/a)</td><td>158.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.60 (n/a)</td><td>354.10 (n/a)</td><td>320.50 (n/a)</td><td>254.50 (n/a)</td><td>137.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>436.00 (n/a)</td><td>311.96 (n/a)</td><td>301.00 (n/a)</td><td>246.60 (n/a)</td><td>74.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>410.50 (n/a)</td><td>298.36 (n/a)</td><td>298.50 (n/a)</td><td>222.70 (n/a)</td><td>74.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>414.48 (n/a)</td><td>489.10 (n/a)</td><td>244.70 (n/a)</td><td>147.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>776.60 (n/a)</td><td>516.68 (n/a)</td><td>483.40 (n/a)</td><td>243.20 (n/a)</td><td>201.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.90 (n/a)</td><td>445.24 (n/a)</td><td>439.50 (n/a)</td><td>265.20 (n/a)</td><td>141.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.20 (n/a)</td><td>443.66 (n/a)</td><td>471.40 (n/a)</td><td>290.30 (n/a)</td><td>144.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.44 (-7.58%)</td><td>0.36 (+15.17%)</td><td>0.42 <b>(+35.98%)</b></td><td>0.12 (-6.12%)</td><td>0.13 (-11.47%)</td><td>1796.10 (+6.52%)</td><td>785.02 (-12.97%)</td><td>520.70 <b>(-26.47%)</b></td><td>507.80 (+8.20%)</td><td>566.25 (+9.41%)</td><td>18.59 (-7.58%)</td><td>15.29 (+15.17%)</td><td>18.12 <b>(+35.98%)</b></td><td>5.25 (-6.12%)</td><td>5.71 (-11.47%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>1686.20 (n/a)</td><td>902.06 (n/a)</td><td>708.10 (n/a)</td><td>469.30 (n/a)</td><td>517.56 (n/a)</td><td>20.11 (n/a)</td><td>13.28 (n/a)</td><td>13.33 (n/a)</td><td>5.60 (n/a)</td><td>6.45 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.49 (-11.72%)</td><td>0.43 (+9.71%)</td><td>0.48 <b>(+33.66%)</b></td><td>0.32 (-1.14%)</td><td>0.08 (-18.22%)</td><td>692.10 (+1.15%)</td><td>527.82 (-9.53%)</td><td>463.80 <b>(-25.19%)</b></td><td>450.90 (+13.26%)</td><td>105.38 (-3.79%)</td><td>20.93 (-11.72%)</td><td>18.39 (+9.71%)</td><td>20.35 <b>(+33.66%)</b></td><td>13.64 (-1.14%)</td><td>3.25 (-18.22%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>684.20 (n/a)</td><td>583.44 (n/a)</td><td>620.00 (n/a)</td><td>398.10 (n/a)</td><td>109.53 (n/a)</td><td>23.71 (n/a)</td><td>16.77 (n/a)</td><td>15.22 (n/a)</td><td>13.79 (n/a)</td><td>3.97 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.31 (-0.30%)</td><td>0.30 (-0.95%)</td><td>0.31 (-0.13%)</td><td>0.29 (-4.23%)</td><td>0.01 <b>(+132.83%)</b></td><td>86849.40 (+4.42%)</td><td>82789.18 (+1.01%)</td><td>81963.50 (+0.13%)</td><td>81046.90 (+0.30%)</td><td>2405.44 <b>(+144.07%)</b></td><td>211.97 (-0.30%)</td><td>207.65 (-0.95%)</td><td>209.60 (-0.13%)</td><td>197.81 (-4.23%)</td><td>5.86 <b>(+132.83%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83174.50 (n/a)</td><td>81961.74 (n/a)</td><td>81858.80 (n/a)</td><td>80803.80 (n/a)</td><td>985.57 (n/a)</td><td>212.61 (n/a)</td><td>209.63 (n/a)</td><td>209.87 (n/a)</td><td>206.55 (n/a)</td><td>2.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>1.03 (+0.01%)</td><td>1.02 (+0.66%)</td><td>1.01 (-0.37%)</td><td>1.01 (+2.94%)</td><td>0.01 <b>(-42.42%)</b></td><td>24898.80 (-2.85%)</td><td>24674.80 (-0.68%)</td><td>24848.10 (+0.37%)</td><td>24343.70 (-0.01%)</td><td>275.46 <b>(-44.19%)</b></td><td>705.72 (+0.01%)</td><td>696.32 (+0.66%)</td><td>691.40 (-0.37%)</td><td>689.99 (+2.94%)</td><td>7.81 <b>(-42.42%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25629.80 (n/a)</td><td>24842.64 (n/a)</td><td>24756.10 (n/a)</td><td>24347.10 (n/a)</td><td>493.54 (n/a)</td><td>705.62 (n/a)</td><td>691.76 (n/a)</td><td>693.96 (n/a)</td><td>670.31 (n/a)</td><td>13.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>4.06 (+4.36%)</td><td>2.45 (-4.02%)</td><td>2.11 (+5.00%)</td><td>1.90 (+12.15%)</td><td>0.91 (-10.70%)</td><td>4250.40 (-10.84%)</td><td>3558.62 (+0.13%)</td><td>3817.10 (-4.76%)</td><td>1984.20 (-4.18%)</td><td>907.20 <b>(-27.43%)</b></td><td>1065.38 (+4.36%)</td><td>642.29 (-4.02%)</td><td>553.81 (+5.00%)</td><td>497.34 (+12.15%)</td><td>238.37 (-10.70%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>3.89 (n/a)</td><td>2.55 (n/a)</td><td>2.01 (n/a)</td><td>1.69 (n/a)</td><td>1.02 (n/a)</td><td>4767.00 (n/a)</td><td>3553.96 (n/a)</td><td>4008.00 (n/a)</td><td>2070.80 (n/a)</td><td>1250.18 (n/a)</td><td>1020.83 (n/a)</td><td>669.22 (n/a)</td><td>527.42 (n/a)</td><td>443.45 (n/a)</td><td>266.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.24 (-10.10%)</td><td>0.21 (+3.24%)</td><td>0.21 (+10.56%)</td><td>0.20 (+16.50%)</td><td>0.02 <b>(-57.77%)</b></td><td>6250.20 (-14.17%)</td><td>5835.22 (-5.08%)</td><td>5887.50 (-9.55%)</td><td>5179.10 (+11.23%)</td><td>415.79 <b>(-59.38%)</b></td><td>12.96 (-10.10%)</td><td>11.55 (+3.24%)</td><td>11.40 (+10.56%)</td><td>10.74 (+16.50%)</td><td>0.87 <b>(-57.77%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>7281.80 (n/a)</td><td>6147.48 (n/a)</td><td>6509.00 (n/a)</td><td>4656.00 (n/a)</td><td>1023.63 (n/a)</td><td>14.41 (n/a)</td><td>11.19 (n/a)</td><td>10.31 (n/a)</td><td>9.22 (n/a)</td><td>2.06 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>3.94 (n/a)</td><td>3.68 (n/a)</td><td>3.69 (n/a)</td><td>3.45 (n/a)</td><td>0.18 (n/a)</td><td>3.94 (n/a)</td><td>3.68 (n/a)</td><td>3.69 (n/a)</td><td>3.45 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>7.50 (+14.75%)</td><td>6.34 (+4.97%)</td><td>5.78 (-0.49%)</td><td>5.62 (-0.11%)</td><td>0.87 <b>(+108.94%)</b></td><td>7.49 (+14.75%)</td><td>6.34 (+4.97%)</td><td>5.78 (-0.49%)</td><td>5.61 (-0.11%)</td><td>0.87 <b>(+108.94%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>6.53 (n/a)</td><td>6.04 (n/a)</td><td>5.81 (n/a)</td><td>5.62 (n/a)</td><td>0.42 (n/a)</td><td>6.53 (n/a)</td><td>6.04 (n/a)</td><td>5.80 (n/a)</td><td>5.62 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>13.90 <b>(+40.89%)</b></td><td>9.73 (+10.21%)</td><td>8.49 (+1.98%)</td><td>7.41 (-8.53%)</td><td>2.60 <b>(+193.73%)</b></td><td>13.89 <b>(+40.89%)</b></td><td>9.72 (+10.21%)</td><td>8.48 (+1.98%)</td><td>7.41 (-8.53%)</td><td>2.60 <b>(+193.73%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>9.86 (n/a)</td><td>8.82 (n/a)</td><td>8.32 (n/a)</td><td>8.10 (n/a)</td><td>0.88 (n/a)</td><td>9.86 (n/a)</td><td>8.82 (n/a)</td><td>8.32 (n/a)</td><td>8.10 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>3.97 (n/a)</td><td>3.70 (n/a)</td><td>3.71 (n/a)</td><td>3.46 (n/a)</td><td>0.19 (n/a)</td><td>3.97 (n/a)</td><td>3.70 (n/a)</td><td>3.71 (n/a)</td><td>3.46 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>7.20 (+5.55%)</td><td>6.19 (-1.97%)</td><td>6.00 (-7.45%)</td><td>5.48 (+3.59%)</td><td>0.70 (+14.59%)</td><td>7.20 (+5.55%)</td><td>6.18 (-1.97%)</td><td>6.00 (-7.45%)</td><td>5.47 (+3.59%)</td><td>0.70 (+14.59%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>6.82 (n/a)</td><td>6.31 (n/a)</td><td>6.48 (n/a)</td><td>5.29 (n/a)</td><td>0.61 (n/a)</td><td>6.82 (n/a)</td><td>6.31 (n/a)</td><td>6.48 (n/a)</td><td>5.28 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>8.52 <b>(-39.24%)</b></td><td>8.26 <b>(-23.06%)</b></td><td>8.19 (-12.03%)</td><td>8.01 (-0.35%)</td><td>0.23 <b>(-92.26%)</b></td><td>8.52 <b>(-39.24%)</b></td><td>8.26 <b>(-23.06%)</b></td><td>8.19 (-12.03%)</td><td>8.01 (-0.35%)</td><td>0.23 <b>(-92.26%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>14.02 (n/a)</td><td>10.74 (n/a)</td><td>9.31 (n/a)</td><td>8.04 (n/a)</td><td>2.99 (n/a)</td><td>14.02 (n/a)</td><td>10.73 (n/a)</td><td>9.31 (n/a)</td><td>8.03 (n/a)</td><td>2.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>3.15 (+6.57%)</td><td>2.60 (+7.56%)</td><td>2.98 (+6.96%)</td><td>1.77 <b>(+50.45%)</b></td><td>0.64 (-14.43%)</td><td>3.14 (+6.57%)</td><td>2.59 (+7.56%)</td><td>2.98 (+6.96%)</td><td>1.76 <b>(+50.45%)</b></td><td>0.64 (-14.43%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>2.95 (n/a)</td><td>2.42 (n/a)</td><td>2.79 (n/a)</td><td>1.17 (n/a)</td><td>0.75 (n/a)</td><td>2.95 (n/a)</td><td>2.41 (n/a)</td><td>2.78 (n/a)</td><td>1.17 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.52 (+12.79%)</td><td>0.30 <b>(+22.41%)</b></td><td>0.32 <b>(+20.05%)</b></td><td>0.07 (+0.86%)</td><td>0.22 <b>(+28.21%)</b></td><td>0.51 (+12.79%)</td><td>0.29 <b>(+22.41%)</b></td><td>0.32 <b>(+20.05%)</b></td><td>0.07 (+0.86%)</td><td>0.21 <b>(+28.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.46 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>0.45 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.70 <b>(+56.78%)</b></td><td>0.45 <b>(+47.41%)</b></td><td>0.52 <b>(+79.53%)</b></td><td>0.08 (-2.92%)</td><td>0.25 <b>(+64.29%)</b></td><td>0.69 <b>(+56.78%)</b></td><td>0.45 <b>(+47.41%)</b></td><td>0.51 <b>(+79.53%)</b></td><td>0.07 (-2.92%)</td><td>0.25 <b>(+64.29%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>2.72 (+11.58%)</td><td>1.63 (-17.09%)</td><td>1.89 (+1.05%)</td><td>0.46 <b>(-71.88%)</b></td><td>1.12 <b>(+239.00%)</b></td><td>2.68 (+11.58%)</td><td>1.61 (-17.09%)</td><td>1.86 (+1.05%)</td><td>0.45 <b>(-71.88%)</b></td><td>1.10 <b>(+239.00%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>2.44 (n/a)</td><td>1.97 (n/a)</td><td>1.87 (n/a)</td><td>1.63 (n/a)</td><td>0.33 (n/a)</td><td>2.40 (n/a)</td><td>1.94 (n/a)</td><td>1.84 (n/a)</td><td>1.60 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.60 (n/a)</td><td>382.08 (n/a)</td><td>302.00 (n/a)</td><td>255.40 (n/a)</td><td>157.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1879.90 (n/a)</td><td>718.06 (n/a)</td><td>450.20 (n/a)</td><td>340.50 (n/a)</td><td>653.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.80 (n/a)</td><td>449.36 (n/a)</td><td>435.20 (n/a)</td><td>265.70 (n/a)</td><td>127.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.70 (n/a)</td><td>474.26 (n/a)</td><td>489.00 (n/a)</td><td>310.20 (n/a)</td><td>123.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.20 (n/a)</td><td>409.04 (n/a)</td><td>385.30 (n/a)</td><td>234.40 (n/a)</td><td>134.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>584.70 (n/a)</td><td>477.14 (n/a)</td><td>500.00 (n/a)</td><td>355.10 (n/a)</td><td>101.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (+11.24%)</td><td>0.02 (-14.10%)</td><td>0.02 <b>(-36.90%)</b></td><td>0.01 <b>(-28.18%)</b></td><td>0.01 <b>(+58.29%)</b></td><td>621.40 <b>(+39.26%)</b></td><td>423.20 <b>(+27.23%)</b></td><td>447.30 <b>(+58.50%)</b></td><td>230.80 (-10.09%)</td><td>162.94 <b>(+93.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>446.20 (n/a)</td><td>332.62 (n/a)</td><td>282.20 (n/a)</td><td>256.70 (n/a)</td><td>84.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (-1.63%)</td><td>0.02 (+6.20%)</td><td>0.03 <b>(+42.25%)</b></td><td>0.02 (+3.15%)</td><td>0.01 (-3.35%)</td><td>537.30 (-3.07%)</td><td>379.28 (-5.99%)</td><td>312.20 <b>(-29.70%)</b></td><td>264.70 (+1.65%)</td><td>125.02 (+0.77%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.30 (n/a)</td><td>403.44 (n/a)</td><td>444.10 (n/a)</td><td>260.40 (n/a)</td><td>124.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (-8.80%)</td><td>0.03 <b>(+25.05%)</b></td><td>0.03 <b>(+56.90%)</b></td><td>0.02 <b>(+28.93%)</b></td><td>0.01 <b>(-27.46%)</b></td><td>434.60 <b>(-22.45%)</b></td><td>335.44 <b>(-23.91%)</b></td><td>292.10 <b>(-36.26%)</b></td><td>254.40 (+9.66%)</td><td>85.93 <b>(-33.77%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.40 (n/a)</td><td>440.86 (n/a)</td><td>458.30 (n/a)</td><td>232.00 (n/a)</td><td>129.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (+6.09%)</td><td>0.02 (-4.59%)</td><td>0.02 <b>(-37.55%)</b></td><td>0.01 (-6.57%)</td><td>0.01 <b>(+32.30%)</b></td><td>612.90 (+7.04%)</td><td>445.38 (+11.94%)</td><td>526.80 <b>(+60.12%)</b></td><td>239.40 (-5.75%)</td><td>185.81 <b>(+24.48%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.60 (n/a)</td><td>397.86 (n/a)</td><td>329.00 (n/a)</td><td>254.00 (n/a)</td><td>149.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (+3.21%)</td><td>0.02 (-11.23%)</td><td>0.02 <b>(-30.86%)</b></td><td>0.01 (-2.92%)</td><td>0.01 (-11.99%)</td><td>576.20 (+3.00%)</td><td>430.40 (+9.58%)</td><td>450.20 <b>(+44.62%)</b></td><td>263.10 (-3.09%)</td><td>114.17 (-18.33%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.40 (n/a)</td><td>392.76 (n/a)</td><td>311.30 (n/a)</td><td>271.50 (n/a)</td><td>139.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 <b>(+26.30%)</b></td><td>0.02 (+13.44%)</td><td>0.02 (+2.28%)</td><td>0.01 (+1.63%)</td><td>0.01 <b>(+38.11%)</b></td><td>805.40 (-1.60%)</td><td>510.84 (-7.57%)</td><td>528.20 (-2.22%)</td><td>217.40 <b>(-20.83%)</b></td><td>211.62 (+2.85%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>818.50 (n/a)</td><td>552.70 (n/a)</td><td>540.20 (n/a)</td><td>274.60 (n/a)</td><td>205.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 <b>(+29.68%)</b></td><td>0.02 (+18.91%)</td><td>0.02 (-2.68%)</td><td>0.02 (+16.95%)</td><td>0.01 <b>(+55.68%)</b></td><td>519.00 (-14.48%)</td><td>424.08 (-12.98%)</td><td>490.70 (+2.76%)</td><td>243.20 <b>(-22.89%)</b></td><td>122.49 (+7.12%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.90 (n/a)</td><td>487.36 (n/a)</td><td>477.50 (n/a)</td><td>315.40 (n/a)</td><td>114.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (-4.13%)</td><td>0.02 (+3.70%)</td><td>0.02 <b>(+46.73%)</b></td><td>0.00 <b>(-73.30%)</b></td><td>0.01 <b>(+64.99%)</b></td><td>2208.10 <b>(+274.57%)</b></td><td>746.28 <b>(+56.93%)</b></td><td>332.50 <b>(-31.84%)</b></td><td>296.00 (+4.34%)</td><td>824.24 <b>(+600.09%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.50 (n/a)</td><td>475.56 (n/a)</td><td>487.80 (n/a)</td><td>283.70 (n/a)</td><td>117.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (+2.49%)</td><td>0.03 <b>(+26.04%)</b></td><td>0.03 <b>(+58.72%)</b></td><td>0.01 <b>(+31.21%)</b></td><td>0.01 (-13.30%)</td><td>590.10 <b>(-23.79%)</b></td><td>321.20 <b>(-25.75%)</b></td><td>243.60 <b>(-37.01%)</b></td><td>237.60 (-2.42%)</td><td>152.28 <b>(-30.76%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>774.30 (n/a)</td><td>432.62 (n/a)</td><td>386.70 (n/a)</td><td>243.50 (n/a)</td><td>219.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (+8.42%)</td><td>0.03 (+11.84%)</td><td>0.03 <b>(+58.02%)</b></td><td>0.02 (+7.42%)</td><td>0.01 (+6.02%)</td><td>511.80 (-6.91%)</td><td>353.66 (-9.84%)</td><td>268.80 <b>(-36.71%)</b></td><td>226.20 (-7.75%)</td><td>138.03 (+1.71%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.80 (n/a)</td><td>392.24 (n/a)</td><td>424.70 (n/a)</td><td>245.20 (n/a)</td><td>135.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (+13.56%)</td><td>0.03 <b>(+36.55%)</b></td><td>0.03 <b>(+119.10%)</b></td><td>0.02 <b>(+34.87%)</b></td><td>0.01 (+6.09%)</td><td>445.00 <b>(-25.86%)</b></td><td>317.44 <b>(-28.89%)</b></td><td>237.20 <b>(-54.37%)</b></td><td>228.90 (-11.93%)</td><td>115.80 <b>(-28.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.20 (n/a)</td><td>446.38 (n/a)</td><td>519.80 (n/a)</td><td>259.90 (n/a)</td><td>162.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (-13.52%)</td><td>0.02 (-14.23%)</td><td>0.02 <b>(-29.50%)</b></td><td>0.01 <b>(+59.62%)</b></td><td>0.01 <b>(-36.47%)</b></td><td>610.10 <b>(-37.35%)</b></td><td>423.32 (-6.86%)</td><td>410.40 <b>(+41.86%)</b></td><td>230.50 (+15.65%)</td><td>142.25 <b>(-55.94%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>973.90 (n/a)</td><td>454.50 (n/a)</td><td>289.30 (n/a)</td><td>199.30 (n/a)</td><td>322.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 <b>(+33.13%)</b></td><td>0.02 (-13.17%)</td><td>0.02 <b>(-37.93%)</b></td><td>0.01 (-8.44%)</td><td>0.01 <b>(+43.72%)</b></td><td>635.90 (+9.22%)</td><td>467.22 <b>(+21.75%)</b></td><td>472.80 <b>(+61.09%)</b></td><td>207.20 <b>(-24.90%)</b></td><td>164.97 (+15.33%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>383.76 (n/a)</td><td>293.50 (n/a)</td><td>275.90 (n/a)</td><td>143.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (+12.28%)</td><td>0.02 (-9.77%)</td><td>0.02 (-19.97%)</td><td>0.01 (-3.87%)</td><td>0.01 (+11.00%)</td><td>548.50 (+4.02%)</td><td>403.50 (+12.00%)</td><td>436.30 <b>(+24.94%)</b></td><td>219.20 (-10.93%)</td><td>123.71 (+2.94%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.30 (n/a)</td><td>360.28 (n/a)</td><td>349.20 (n/a)</td><td>246.10 (n/a)</td><td>120.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (+1.71%)</td><td>0.03 (+14.72%)</td><td>0.03 (+17.39%)</td><td>0.03 <b>(+33.91%)</b></td><td>0.00 <b>(-52.03%)</b></td><td>292.90 <b>(-25.32%)</b></td><td>268.22 (-15.86%)</td><td>268.50 (-14.82%)</td><td>235.30 (-1.67%)</td><td>25.36 <b>(-65.05%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>392.20 (n/a)</td><td>318.78 (n/a)</td><td>315.20 (n/a)</td><td>239.30 (n/a)</td><td>72.58 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 <b>(-30.82%)</b></td><td>0.03 (-13.95%)</td><td>0.03 (+10.13%)</td><td>0.02 (-9.32%)</td><td>0.01 <b>(-42.36%)</b></td><td>554.60 (+10.28%)</td><td>420.78 (+9.94%)</td><td>390.00 (-9.20%)</td><td>300.00 <b>(+44.58%)</b></td><td>121.20 (-9.18%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>502.90 (n/a)</td><td>382.72 (n/a)</td><td>429.50 (n/a)</td><td>207.50 (n/a)</td><td>133.45 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (+1.66%)</td><td>0.03 <b>(+27.01%)</b></td><td>0.03 <b>(+36.11%)</b></td><td>0.02 <b>(+34.57%)</b></td><td>0.01 <b>(-32.02%)</b></td><td>443.20 <b>(-25.69%)</b></td><td>300.96 <b>(-27.16%)</b></td><td>272.00 <b>(-26.53%)</b></td><td>245.50 (-1.60%)</td><td>80.45 <b>(-49.60%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.40 (n/a)</td><td>413.18 (n/a)</td><td>370.20 (n/a)</td><td>249.50 (n/a)</td><td>159.61 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (-15.49%)</td><td>0.03 (-10.29%)</td><td>0.02 (-17.89%)</td><td>0.02 (+1.54%)</td><td>0.01 (-12.24%)</td><td>575.70 (-1.52%)</td><td>430.74 (+10.41%)</td><td>506.90 <b>(+21.79%)</b></td><td>264.20 (+18.32%)</td><td>148.77 (+1.77%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>584.60 (n/a)</td><td>390.12 (n/a)</td><td>416.20 (n/a)</td><td>223.30 (n/a)</td><td>146.17 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 <b>(+37.57%)</b></td><td>0.02 (+19.64%)</td><td>0.02 (+9.78%)</td><td>0.01 (-14.08%)</td><td>0.01 <b>(+176.29%)</b></td><td>559.90 (+16.38%)</td><td>403.64 (-6.72%)</td><td>405.70 (-8.91%)</td><td>235.60 <b>(-27.31%)</b></td><td>154.67 <b>(+143.91%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>481.10 (n/a)</td><td>432.70 (n/a)</td><td>445.40 (n/a)</td><td>324.10 (n/a)</td><td>63.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (-18.14%)</td><td>0.03 (+11.93%)</td><td>0.04 <b>(+65.49%)</b></td><td>0.03 <b>(+59.28%)</b></td><td>0.00 <b>(-66.04%)</b></td><td>372.90 <b>(-37.21%)</b></td><td>314.02 <b>(-23.62%)</b></td><td>284.70 <b>(-39.57%)</b></td><td>273.80 <b>(+22.18%)</b></td><td>48.19 <b>(-72.26%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.90 (n/a)</td><td>411.14 (n/a)</td><td>471.10 (n/a)</td><td>224.10 (n/a)</td><td>173.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (+5.14%)</td><td>0.02 (+9.71%)</td><td>0.02 (+12.08%)</td><td>0.01 (+4.66%)</td><td>0.01 (-3.38%)</td><td>565.60 (-4.46%)</td><td>388.52 (-10.76%)</td><td>427.80 (-10.78%)</td><td>247.50 (-4.88%)</td><td>130.59 (-15.09%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.00 (n/a)</td><td>435.36 (n/a)</td><td>479.50 (n/a)</td><td>260.20 (n/a)</td><td>153.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (-6.12%)</td><td>0.03 (+12.55%)</td><td>0.03 <b>(+37.35%)</b></td><td>0.01 (-0.01%)</td><td>0.01 (-0.51%)</td><td>650.60 (+0.02%)</td><td>384.00 (-11.18%)</td><td>276.20 <b>(-27.20%)</b></td><td>261.50 (+6.52%)</td><td>169.73 (-1.08%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.50 (n/a)</td><td>432.34 (n/a)</td><td>379.40 (n/a)</td><td>245.50 (n/a)</td><td>171.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 <b>(+52.05%)</b></td><td>0.02 (+10.41%)</td><td>0.02 (+1.80%)</td><td>0.01 <b>(-22.37%)</b></td><td>0.01 <b>(+170.38%)</b></td><td>786.10 <b>(+28.83%)</b></td><td>492.62 (+2.45%)</td><td>473.40 (-1.78%)</td><td>235.70 <b>(-34.24%)</b></td><td>199.31 <b>(+122.14%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.20 (n/a)</td><td>480.86 (n/a)</td><td>482.00 (n/a)</td><td>358.40 (n/a)</td><td>89.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (+7.30%)</td><td>0.03 (+14.20%)</td><td>0.03 (+3.62%)</td><td>0.02 <b>(+53.30%)</b></td><td>0.01 <b>(-30.27%)</b></td><td>425.50 <b>(-34.77%)</b></td><td>331.08 <b>(-21.85%)</b></td><td>290.90 (-3.48%)</td><td>241.70 (-6.79%)</td><td>86.41 <b>(-56.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.30 (n/a)</td><td>423.66 (n/a)</td><td>301.40 (n/a)</td><td>259.30 (n/a)</td><td>200.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 <b>(+27.13%)</b></td><td>0.02 (+5.75%)</td><td>0.02 (-7.23%)</td><td>0.01 <b>(-49.43%)</b></td><td>0.01 <b>(+131.57%)</b></td><td>1286.60 <b>(+97.76%)</b></td><td>584.14 <b>(+20.49%)</b></td><td>471.50 (+7.80%)</td><td>292.10 <b>(-21.33%)</b></td><td>409.58 <b>(+251.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>650.60 (n/a)</td><td>484.80 (n/a)</td><td>437.40 (n/a)</td><td>371.30 (n/a)</td><td>116.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.35 (-11.64%)</td><td>0.23 (-14.25%)</td><td>0.22 (-6.44%)</td><td>0.15 (-11.45%)</td><td>0.09 <b>(-22.41%)</b></td><td>644.70 (+12.95%)</td><td>466.70 (+13.76%)</td><td>440.90 (+6.88%)</td><td>278.60 (+13.16%)</td><td>164.44 (+4.03%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>570.80 (n/a)</td><td>410.26 (n/a)</td><td>412.50 (n/a)</td><td>246.20 (n/a)</td><td>158.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.39 <b>(-24.49%)</b></td><td>0.29 (+17.98%)</td><td>0.35 <b>(+68.85%)</b></td><td>0.17 <b>(+42.14%)</b></td><td>0.10 <b>(-31.40%)</b></td><td>569.10 <b>(-29.65%)</b></td><td>379.28 <b>(-22.87%)</b></td><td>277.60 <b>(-40.77%)</b></td><td>255.00 <b>(+32.47%)</b></td><td>154.03 <b>(-29.72%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.51 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>809.00 (n/a)</td><td>491.72 (n/a)</td><td>468.70 (n/a)</td><td>192.50 (n/a)</td><td>219.17 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.34 <b>(+25.10%)</b></td><td>0.24 <b>(+31.05%)</b></td><td>0.23 <b>(+38.61%)</b></td><td>0.18 <b>(+37.36%)</b></td><td>0.06 (+11.99%)</td><td>545.90 <b>(-27.20%)</b></td><td>422.38 <b>(-24.81%)</b></td><td>420.80 <b>(-27.86%)</b></td><td>293.30 <b>(-20.08%)</b></td><td>93.09 <b>(-34.44%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>749.90 (n/a)</td><td>561.72 (n/a)</td><td>583.30 (n/a)</td><td>367.00 (n/a)</td><td>142.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.26 (-16.46%)</td><td>0.20 (-2.70%)</td><td>0.21 <b>(+40.24%)</b></td><td>0.12 (-0.40%)</td><td>0.06 <b>(-34.16%)</b></td><td>623.40 (+0.40%)</td><td>404.74 (-4.29%)</td><td>351.70 <b>(-28.69%)</b></td><td>281.50 (+19.69%)</td><td>145.10 (-16.75%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>620.90 (n/a)</td><td>422.88 (n/a)</td><td>493.20 (n/a)</td><td>235.20 (n/a)</td><td>174.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.30 <b>(-26.45%)</b></td><td>0.21 (-0.09%)</td><td>0.24 <b>(+48.25%)</b></td><td>0.09 <b>(+34.32%)</b></td><td>0.09 <b>(-32.03%)</b></td><td>833.80 <b>(-25.55%)</b></td><td>428.66 (-14.80%)</td><td>301.60 <b>(-32.54%)</b></td><td>244.40 <b>(+36.00%)</b></td><td>247.40 <b>(-32.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.41 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.13 (n/a)</td><td>1120.00 (n/a)</td><td>503.10 (n/a)</td><td>447.10 (n/a)</td><td>179.70 (n/a)</td><td>367.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.31 (+10.25%)</td><td>0.20 (+11.79%)</td><td>0.16 (+5.12%)</td><td>0.12 (-10.33%)</td><td>0.07 <b>(+26.89%)</b></td><td>591.40 (+11.52%)</td><td>415.98 (-7.02%)</td><td>464.60 (-4.87%)</td><td>238.80 (-9.30%)</td><td>140.12 <b>(+30.05%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>530.30 (n/a)</td><td>447.38 (n/a)</td><td>488.40 (n/a)</td><td>263.30 (n/a)</td><td>107.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.39 (-7.94%)</td><td>0.25 (-16.63%)</td><td>0.24 (-8.40%)</td><td>0.12 <b>(-42.72%)</b></td><td>0.10 (-1.03%)</td><td>1102.40 <b>(+74.60%)</b></td><td>605.84 <b>(+28.62%)</b></td><td>554.60 (+9.17%)</td><td>333.80 (+8.62%)</td><td>296.91 <b>(+100.89%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>631.40 (n/a)</td><td>471.02 (n/a)</td><td>508.00 (n/a)</td><td>307.30 (n/a)</td><td>147.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.39 (-18.75%)</td><td>0.25 <b>(-26.62%)</b></td><td>0.26 <b>(-35.76%)</b></td><td>0.10 <b>(-50.92%)</b></td><td>0.10 (-12.95%)</td><td>1308.40 <b>(+103.77%)</b></td><td>633.50 <b>(+49.45%)</b></td><td>510.50 <b>(+55.69%)</b></td><td>334.10 <b>(+23.06%)</b></td><td>385.89 <b>(+134.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.40 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>642.10 (n/a)</td><td>423.88 (n/a)</td><td>327.90 (n/a)</td><td>271.50 (n/a)</td><td>164.46 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.54 (+16.55%)</td><td>0.34 (-7.24%)</td><td>0.29 <b>(-26.48%)</b></td><td>0.26 (+4.65%)</td><td>0.12 (+18.28%)</td><td>504.30 (-4.43%)</td><td>419.48 (+8.47%)</td><td>444.40 <b>(+35.99%)</b></td><td>243.40 (-14.21%)</td><td>107.16 (-6.44%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>527.70 (n/a)</td><td>386.74 (n/a)</td><td>326.80 (n/a)</td><td>283.70 (n/a)</td><td>114.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-49.63%)</b></td><td>22348.53 (+16.77%)</td><td>17495.56 <b>(+32.48%)</b></td><td>19021.22 (+17.72%)</td><td>8097.78 <b>(+37.94%)</b></td><td>5863.26 (-11.55%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19138.96 (n/a)</td><td>13206.03 (n/a)</td><td>16157.60 (n/a)</td><td>5870.38 (n/a)</td><td>6629.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-37.78%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+19.61%)</td><td>22022.94 <b>(+33.26%)</b></td><td>17313.57 <b>(+75.36%)</b></td><td>19368.61 <b>(+144.58%)</b></td><td>7745.44 (+7.97%)</td><td>5582.57 <b>(+41.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16525.98 (n/a)</td><td>9873.17 (n/a)</td><td>7919.23 (n/a)</td><td>7173.89 (n/a)</td><td>3947.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.15 (+0.00%)</td><td>0.10 (-7.60%)</td><td>0.09 (-14.95%)</td><td>0.08 (+12.89%)</td><td>0.03 (-6.66%)</td><td>26022.77 (-11.36%)</td><td>22512.56 (+6.57%)</td><td>24405.59 (+17.53%)</td><td>13984.24 (+0.00%)</td><td>4966.26 (-18.92%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29359.24 (n/a)</td><td>21125.40 (n/a)</td><td>20765.14 (n/a)</td><td>13984.00 (n/a)</td><td>6125.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>1.60 (+1.43%)</td><td>1.03 (-12.40%)</td><td>1.03 <b>(-26.64%)</b></td><td>0.68 (+9.68%)</td><td>0.37 (-17.06%)</td><td>769.60 (-8.83%)</td><td>557.78 (+8.60%)</td><td>508.50 <b>(+36.33%)</b></td><td>327.60 (-1.38%)</td><td>180.11 <b>(-21.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>1.58 (n/a)</td><td>1.18 (n/a)</td><td>1.41 (n/a)</td><td>0.62 (n/a)</td><td>0.44 (n/a)</td><td>844.10 (n/a)</td><td>513.62 (n/a)</td><td>373.00 (n/a)</td><td>332.20 (n/a)</td><td>230.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>2.55 (+4.92%)</td><td>1.45 <b>(+29.02%)</b></td><td>1.40 (+18.52%)</td><td>0.32 (+6.70%)</td><td>0.80 (-9.90%)</td><td>3324.20 (-6.28%)</td><td>1181.76 <b>(-34.20%)</b></td><td>749.90 (-15.63%)</td><td>410.90 (-4.71%)</td><td>1206.24 <b>(-20.76%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>2.43 (n/a)</td><td>1.12 (n/a)</td><td>1.18 (n/a)</td><td>0.30 (n/a)</td><td>0.88 (n/a)</td><td>3546.80 (n/a)</td><td>1795.90 (n/a)</td><td>888.80 (n/a)</td><td>431.20 (n/a)</td><td>1522.20 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>1.63 (+16.20%)</td><td>1.03 (-10.42%)</td><td>1.01 (-7.65%)</td><td>0.61 <b>(-41.37%)</b></td><td>0.37 <b>(+157.78%)</b></td><td>857.00 <b>(+70.58%)</b></td><td>558.58 <b>(+21.66%)</b></td><td>519.10 (+8.28%)</td><td>322.50 (-13.95%)</td><td>192.93 <b>(+280.57%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>1.40 (n/a)</td><td>1.15 (n/a)</td><td>1.09 (n/a)</td><td>1.04 (n/a)</td><td>0.14 (n/a)</td><td>502.40 (n/a)</td><td>459.12 (n/a)</td><td>479.40 (n/a)</td><td>374.80 (n/a)</td><td>50.69 (n/a)</td>
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
