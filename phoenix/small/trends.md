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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (+15.59%)</td><td>0.04 (+11.18%)</td><td>0.04 (-12.21%)</td><td>0.02 (-0.70%)</td><td>0.01 (+13.00%)</td><td>611.60 (+0.71%)</td><td>366.94 (-9.90%)</td><td>336.70 (+13.90%)</td><td>235.10 (-13.47%)</td><td>154.48 (-6.80%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>607.30 (n/a)</td><td>407.28 (n/a)</td><td>295.60 (n/a)</td><td>271.70 (n/a)</td><td>165.76 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (-0.68%)</td><td>0.04 (-4.95%)</td><td>0.04 (-16.47%)</td><td>0.03 (+19.02%)</td><td>0.01 (-8.40%)</td><td>488.20 (-15.99%)</td><td>334.02 (+1.56%)</td><td>315.60 (+19.73%)</td><td>237.30 (+0.68%)</td><td>104.55 <b>(-27.51%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.10 (n/a)</td><td>328.90 (n/a)</td><td>263.60 (n/a)</td><td>235.70 (n/a)</td><td>144.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (-15.36%)</td><td>0.03 (+8.44%)</td><td>0.04 <b>(+58.59%)</b></td><td>0.02 (-1.63%)</td><td>0.01 (-6.52%)</td><td>657.20 (+1.64%)</td><td>410.92 (-7.17%)</td><td>294.40 <b>(-36.93%)</b></td><td>283.30 (+18.14%)</td><td>173.01 (+9.65%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>646.60 (n/a)</td><td>442.68 (n/a)</td><td>466.80 (n/a)</td><td>239.80 (n/a)</td><td>157.79 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (+1.36%)</td><td>0.02 <b>(+23.72%)</b></td><td>0.02 (+2.05%)</td><td>0.01 <b>(+81.25%)</b></td><td>0.01 <b>(-31.42%)</b></td><td>447.00 <b>(-44.82%)</b></td><td>294.24 <b>(-32.12%)</b></td><td>289.70 (-2.00%)</td><td>200.50 (-1.33%)</td><td>93.12 <b>(-62.88%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>810.10 (n/a)</td><td>433.48 (n/a)</td><td>295.60 (n/a)</td><td>203.20 (n/a)</td><td>250.85 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (-1.74%)</td><td>0.02 (+1.39%)</td><td>0.02 (+4.87%)</td><td>0.01 <b>(-24.54%)</b></td><td>0.01 <b>(+22.44%)</b></td><td>592.40 <b>(+32.53%)</b></td><td>349.10 (+4.33%)</td><td>287.60 (-4.64%)</td><td>230.30 (+1.77%)</td><td>152.52 <b>(+52.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>447.00 (n/a)</td><td>334.62 (n/a)</td><td>301.60 (n/a)</td><td>226.30 (n/a)</td><td>99.85 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (+4.55%)</td><td>0.02 (+4.26%)</td><td>0.02 (+9.55%)</td><td>0.01 (-19.37%)</td><td>0.01 <b>(+36.98%)</b></td><td>615.20 <b>(+24.03%)</b></td><td>348.88 (+4.24%)</td><td>265.40 (-8.70%)</td><td>214.30 (-4.37%)</td><td>171.70 <b>(+55.40%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>496.00 (n/a)</td><td>334.70 (n/a)</td><td>290.70 (n/a)</td><td>224.10 (n/a)</td><td>110.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 <b>(+31.83%)</b></td><td>0.02 (+14.04%)</td><td>0.02 (-3.62%)</td><td>0.01 (+8.51%)</td><td>0.01 <b>(+52.23%)</b></td><td>541.90 (-7.84%)</td><td>342.94 (-8.82%)</td><td>314.40 (+3.76%)</td><td>217.00 <b>(-24.15%)</b></td><td>132.98 (+4.69%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.00 (n/a)</td><td>376.12 (n/a)</td><td>303.00 (n/a)</td><td>286.10 (n/a)</td><td>127.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (-10.88%)</td><td>0.01 <b>(-23.29%)</b></td><td>0.01 <b>(-28.15%)</b></td><td>0.01 <b>(-37.77%)</b></td><td>0.01 <b>(+27.27%)</b></td><td>750.30 <b>(+60.70%)</b></td><td>451.38 <b>(+44.28%)</b></td><td>428.10 <b>(+39.17%)</b></td><td>248.80 (+12.22%)</td><td>205.75 <b>(+117.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>466.90 (n/a)</td><td>312.86 (n/a)</td><td>307.60 (n/a)</td><td>221.70 (n/a)</td><td>94.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (-1.45%)</td><td>0.01 (-0.40%)</td><td>0.01 (+19.20%)</td><td>0.01 <b>(-41.50%)</b></td><td>0.01 (+19.80%)</td><td>1008.00 <b>(+70.93%)</b></td><td>482.06 (+14.98%)</td><td>379.90 (-16.10%)</td><td>248.10 (+1.47%)</td><td>307.83 <b>(+118.61%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>419.24 (n/a)</td><td>452.80 (n/a)</td><td>244.50 (n/a)</td><td>140.81 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>410.50 (n/a)</td><td>316.32 (n/a)</td><td>274.00 (n/a)</td><td>261.20 (n/a)</td><td>67.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>380.88 (n/a)</td><td>376.80 (n/a)</td><td>236.30 (n/a)</td><td>135.98 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>668.50 (n/a)</td><td>431.72 (n/a)</td><td>419.60 (n/a)</td><td>232.00 (n/a)</td><td>156.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.70 (n/a)</td><td>336.74 (n/a)</td><td>293.60 (n/a)</td><td>270.50 (n/a)</td><td>107.79 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.70 (n/a)</td><td>411.82 (n/a)</td><td>453.90 (n/a)</td><td>246.10 (n/a)</td><td>156.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>622.00 (n/a)</td><td>466.04 (n/a)</td><td>430.30 (n/a)</td><td>323.80 (n/a)</td><td>112.45 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.10 (n/a)</td><td>418.98 (n/a)</td><td>400.30 (n/a)</td><td>320.70 (n/a)</td><td>92.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2081.30 (n/a)</td><td>705.10 (n/a)</td><td>371.70 (n/a)</td><td>255.60 (n/a)</td><td>775.85 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>388.90 (n/a)</td><td>282.46 (n/a)</td><td>266.90 (n/a)</td><td>231.70 (n/a)</td><td>62.03 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>520.70 (n/a)</td><td>399.20 (n/a)</td><td>394.80 (n/a)</td><td>303.60 (n/a)</td><td>91.55 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.50 (n/a)</td><td>461.34 (n/a)</td><td>478.20 (n/a)</td><td>294.20 (n/a)</td><td>117.58 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>528.00 (n/a)</td><td>464.98 (n/a)</td><td>488.30 (n/a)</td><td>345.30 (n/a)</td><td>70.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.47 (-11.00%)</td><td>0.31 <b>(-24.43%)</b></td><td>0.31 <b>(-23.46%)</b></td><td>0.13 <b>(-53.26%)</b></td><td>0.15 <b>(+58.36%)</b></td><td>1686.20 <b>(+113.96%)</b></td><td>902.06 <b>(+60.15%)</b></td><td>708.10 <b>(+30.65%)</b></td><td>469.30 (+12.35%)</td><td>517.56 <b>(+260.74%)</b></td><td>20.11 (-11.00%)</td><td>13.28 <b>(-24.43%)</b></td><td>13.33 <b>(-23.46%)</b></td><td>5.60 <b>(-53.26%)</b></td><td>6.45 <b>(+58.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>788.10 (n/a)</td><td>563.26 (n/a)</td><td>542.00 (n/a)</td><td>417.70 (n/a)</td><td>143.47 (n/a)</td><td>22.60 (n/a)</td><td>17.57 (n/a)</td><td>17.41 (n/a)</td><td>11.97 (n/a)</td><td>4.07 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.56 (+16.08%)</td><td>0.39 (+2.03%)</td><td>0.36 (+0.99%)</td><td>0.32 (+14.60%)</td><td>0.09 (+9.11%)</td><td>684.20 (-12.74%)</td><td>583.44 (-2.39%)</td><td>620.00 (-0.97%)</td><td>398.10 (-13.85%)</td><td>109.53 (-18.27%)</td><td>23.71 (+16.08%)</td><td>16.77 (+2.03%)</td><td>15.22 (+0.99%)</td><td>13.79 (+14.60%)</td><td>3.97 (+9.11%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>784.10 (n/a)</td><td>597.72 (n/a)</td><td>626.10 (n/a)</td><td>462.10 (n/a)</td><td>134.02 (n/a)</td><td>20.42 (n/a)</td><td>16.43 (n/a)</td><td>15.07 (n/a)</td><td>12.04 (n/a)</td><td>3.64 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.31 (+1.62%)</td><td>0.31 (+0.63%)</td><td>0.31 (+0.52%)</td><td>0.30 (+0.21%)</td><td>0.00 <b>(+100.32%)</b></td><td>83174.50 (-0.21%)</td><td>81961.74 (-0.61%)</td><td>81858.80 (-0.51%)</td><td>80803.80 (-1.60%)</td><td>985.57 <b>(+96.54%)</b></td><td>212.61 (+1.62%)</td><td>209.63 (+0.63%)</td><td>209.87 (+0.52%)</td><td>206.55 (+0.21%)</td><td>2.52 <b>(+100.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83350.90 (n/a)</td><td>82467.46 (n/a)</td><td>82282.50 (n/a)</td><td>82115.60 (n/a)</td><td>501.45 (n/a)</td><td>209.22 (n/a)</td><td>208.33 (n/a)</td><td>208.79 (n/a)</td><td>206.12 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>1.03 (+1.44%)</td><td>1.01 (+1.29%)</td><td>1.02 (+0.84%)</td><td>0.98 (+2.69%)</td><td>0.02 <b>(-21.99%)</b></td><td>25629.80 (-2.62%)</td><td>24842.64 (-1.30%)</td><td>24756.10 (-0.83%)</td><td>24347.10 (-1.42%)</td><td>493.54 <b>(-25.25%)</b></td><td>705.62 (+1.44%)</td><td>691.76 (+1.29%)</td><td>693.96 (+0.84%)</td><td>670.31 (+2.69%)</td><td>13.56 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.96 (n/a)</td><td>0.03 (n/a)</td><td>26319.80 (n/a)</td><td>25168.86 (n/a)</td><td>24964.50 (n/a)</td><td>24697.80 (n/a)</td><td>660.22 (n/a)</td><td>695.60 (n/a)</td><td>682.95 (n/a)</td><td>688.17 (n/a)</td><td>652.74 (n/a)</td><td>17.38 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>3.89 (+1.71%)</td><td>2.55 (+7.49%)</td><td>2.01 (-1.28%)</td><td>1.69 (+11.18%)</td><td>1.02 (+12.05%)</td><td>4767.00 (-10.06%)</td><td>3553.96 (-5.40%)</td><td>4008.00 (+1.29%)</td><td>2070.80 (-1.68%)</td><td>1250.18 (+2.00%)</td><td>1020.83 (+1.71%)</td><td>669.22 (+7.49%)</td><td>527.42 (-1.28%)</td><td>443.45 (+11.18%)</td><td>266.95 (+12.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>3.83 (n/a)</td><td>2.37 (n/a)</td><td>2.04 (n/a)</td><td>1.52 (n/a)</td><td>0.91 (n/a)</td><td>5300.10 (n/a)</td><td>3756.70 (n/a)</td><td>3956.90 (n/a)</td><td>2106.20 (n/a)</td><td>1225.67 (n/a)</td><td>1003.68 (n/a)</td><td>622.60 (n/a)</td><td>534.24 (n/a)</td><td>398.85 (n/a)</td><td>238.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.27 (-10.20%)</td><td>0.21 (-2.29%)</td><td>0.19 (-2.55%)</td><td>0.17 (-4.36%)</td><td>0.04 <b>(-21.49%)</b></td><td>7281.80 (+4.56%)</td><td>6147.48 (+1.44%)</td><td>6509.00 (+2.62%)</td><td>4656.00 (+11.36%)</td><td>1023.63 (-6.57%)</td><td>14.41 (-10.20%)</td><td>11.19 (-2.29%)</td><td>10.31 (-2.55%)</td><td>9.22 (-4.36%)</td><td>2.06 <b>(-21.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>6964.20 (n/a)</td><td>6059.96 (n/a)</td><td>6342.80 (n/a)</td><td>4180.90 (n/a)</td><td>1095.64 (n/a)</td><td>16.05 (n/a)</td><td>11.45 (n/a)</td><td>10.58 (n/a)</td><td>9.64 (n/a)</td><td>2.62 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>3.77 (n/a)</td><td>3.56 (n/a)</td><td>3.66 (n/a)</td><td>3.27 (n/a)</td><td>0.24 (n/a)</td><td>3.77 (n/a)</td><td>3.56 (n/a)</td><td>3.66 (n/a)</td><td>3.27 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>6.53 (+15.30%)</td><td>6.04 (+15.82%)</td><td>5.81 (+9.98%)</td><td>5.62 (+18.35%)</td><td>0.42 (-5.99%)</td><td>6.53 (+15.30%)</td><td>6.04 (+15.82%)</td><td>5.80 (+9.98%)</td><td>5.62 (+18.35%)</td><td>0.41 (-5.99%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>5.67 (n/a)</td><td>5.22 (n/a)</td><td>5.28 (n/a)</td><td>4.75 (n/a)</td><td>0.44 (n/a)</td><td>5.66 (n/a)</td><td>5.21 (n/a)</td><td>5.28 (n/a)</td><td>4.75 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>9.86 <b>(-23.67%)</b></td><td>8.82 (-10.90%)</td><td>8.32 (-16.37%)</td><td>8.10 <b>(+26.34%)</b></td><td>0.88 <b>(-64.52%)</b></td><td>9.86 <b>(-23.67%)</b></td><td>8.82 (-10.90%)</td><td>8.32 (-16.37%)</td><td>8.10 <b>(+26.34%)</b></td><td>0.88 <b>(-64.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>12.92 (n/a)</td><td>9.90 (n/a)</td><td>9.95 (n/a)</td><td>6.41 (n/a)</td><td>2.49 (n/a)</td><td>12.91 (n/a)</td><td>9.90 (n/a)</td><td>9.95 (n/a)</td><td>6.41 (n/a)</td><td>2.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>3.74 (n/a)</td><td>3.58 (n/a)</td><td>3.67 (n/a)</td><td>3.34 (n/a)</td><td>0.17 (n/a)</td><td>3.74 (n/a)</td><td>3.58 (n/a)</td><td>3.67 (n/a)</td><td>3.34 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>6.82 (-9.73%)</td><td>6.31 (-8.66%)</td><td>6.48 (-5.63%)</td><td>5.29 (-12.45%)</td><td>0.61 (-5.05%)</td><td>6.82 (-9.73%)</td><td>6.31 (-8.66%)</td><td>6.48 (-5.63%)</td><td>5.28 (-12.45%)</td><td>0.61 (-5.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>7.56 (n/a)</td><td>6.91 (n/a)</td><td>6.87 (n/a)</td><td>6.04 (n/a)</td><td>0.65 (n/a)</td><td>7.55 (n/a)</td><td>6.90 (n/a)</td><td>6.87 (n/a)</td><td>6.03 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>14.02 (+0.94%)</td><td>10.74 (-12.49%)</td><td>9.31 <b>(-25.63%)</b></td><td>8.04 (-15.47%)</td><td>2.99 <b>(+64.59%)</b></td><td>14.02 (+0.94%)</td><td>10.73 (-12.49%)</td><td>9.31 <b>(-25.63%)</b></td><td>8.03 (-15.47%)</td><td>2.99 <b>(+64.59%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>13.89 (n/a)</td><td>12.27 (n/a)</td><td>12.52 (n/a)</td><td>9.51 (n/a)</td><td>1.82 (n/a)</td><td>13.89 (n/a)</td><td>12.27 (n/a)</td><td>12.52 (n/a)</td><td>9.50 (n/a)</td><td>1.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>2.95 (+6.84%)</td><td>2.42 <b>(+64.04%)</b></td><td>2.79 <b>(+122.36%)</b></td><td>1.17 <b>(+20.82%)</b></td><td>0.75 (+1.78%)</td><td>2.95 (+6.84%)</td><td>2.41 <b>(+64.04%)</b></td><td>2.78 <b>(+122.36%)</b></td><td>1.17 <b>(+20.82%)</b></td><td>0.74 (+1.78%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>2.76 (n/a)</td><td>1.47 (n/a)</td><td>1.25 (n/a)</td><td>0.97 (n/a)</td><td>0.73 (n/a)</td><td>2.76 (n/a)</td><td>1.47 (n/a)</td><td>1.25 (n/a)</td><td>0.97 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.46 (+1.60%)</td><td>0.24 (+6.08%)</td><td>0.27 <b>(+46.61%)</b></td><td>0.07 (+0.09%)</td><td>0.17 (-1.01%)</td><td>0.45 (+1.60%)</td><td>0.24 (+6.08%)</td><td>0.26 <b>(+46.61%)</b></td><td>0.07 (+0.09%)</td><td>0.17 (-1.01%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.45 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>0.45 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.45 (+2.31%)</td><td>0.31 (+1.17%)</td><td>0.29 (+1.36%)</td><td>0.08 (-2.93%)</td><td>0.15 (+3.25%)</td><td>0.44 (+2.31%)</td><td>0.30 (+1.17%)</td><td>0.29 (+1.36%)</td><td>0.08 (-2.93%)</td><td>0.15 (+3.25%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>2.44 (-19.50%)</td><td>1.97 (+2.99%)</td><td>1.87 (+1.84%)</td><td>1.63 <b>(+58.51%)</b></td><td>0.33 <b>(-53.88%)</b></td><td>2.40 (-19.50%)</td><td>1.94 (+2.99%)</td><td>1.84 (+1.84%)</td><td>1.60 <b>(+58.51%)</b></td><td>0.33 <b>(-53.88%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>3.03 (n/a)</td><td>1.91 (n/a)</td><td>1.84 (n/a)</td><td>1.03 (n/a)</td><td>0.72 (n/a)</td><td>2.98 (n/a)</td><td>1.88 (n/a)</td><td>1.81 (n/a)</td><td>1.01 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.60 (n/a)</td><td>431.80 (n/a)</td><td>511.00 (n/a)</td><td>278.60 (n/a)</td><td>139.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.20 (n/a)</td><td>397.60 (n/a)</td><td>322.10 (n/a)</td><td>240.30 (n/a)</td><td>164.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.60 (n/a)</td><td>491.38 (n/a)</td><td>487.90 (n/a)</td><td>268.10 (n/a)</td><td>143.39 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>405.32 (n/a)</td><td>321.30 (n/a)</td><td>291.80 (n/a)</td><td>141.08 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.90 (n/a)</td><td>463.98 (n/a)</td><td>506.50 (n/a)</td><td>206.30 (n/a)</td><td>156.50 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.30 (n/a)</td><td>448.20 (n/a)</td><td>508.00 (n/a)</td><td>293.80 (n/a)</td><td>106.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (+16.71%)</td><td>0.03 <b>(+39.86%)</b></td><td>0.03 <b>(+90.28%)</b></td><td>0.02 <b>(+41.86%)</b></td><td>0.01 (-10.61%)</td><td>446.20 <b>(-29.51%)</b></td><td>332.62 <b>(-31.97%)</b></td><td>282.20 <b>(-47.45%)</b></td><td>256.70 (-14.32%)</td><td>84.07 <b>(-46.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.00 (n/a)</td><td>488.92 (n/a)</td><td>537.00 (n/a)</td><td>299.60 (n/a)</td><td>158.15 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-17.40%)</td><td>0.02 <b>(-25.35%)</b></td><td>0.02 <b>(-42.55%)</b></td><td>0.01 (-1.32%)</td><td>0.01 (-19.10%)</td><td>554.30 (+1.33%)</td><td>403.44 <b>(+30.39%)</b></td><td>444.10 <b>(+74.09%)</b></td><td>260.40 <b>(+21.06%)</b></td><td>124.07 (-8.83%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.00 (n/a)</td><td>309.42 (n/a)</td><td>255.10 (n/a)</td><td>215.10 (n/a)</td><td>136.08 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (+2.58%)</td><td>0.02 <b>(-27.06%)</b></td><td>0.02 <b>(-42.79%)</b></td><td>0.01 <b>(-28.56%)</b></td><td>0.01 <b>(+24.41%)</b></td><td>560.40 <b>(+39.96%)</b></td><td>440.86 <b>(+43.81%)</b></td><td>458.30 <b>(+74.79%)</b></td><td>232.00 (-2.48%)</td><td>129.73 <b>(+61.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>400.40 (n/a)</td><td>306.56 (n/a)</td><td>262.20 (n/a)</td><td>237.90 (n/a)</td><td>80.57 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-11.02%)</td><td>0.02 (-10.68%)</td><td>0.02 (-13.03%)</td><td>0.01 (-16.20%)</td><td>0.01 (-2.33%)</td><td>572.60 (+19.34%)</td><td>397.86 (+14.44%)</td><td>329.00 (+14.99%)</td><td>254.00 (+12.39%)</td><td>149.27 <b>(+29.18%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.80 (n/a)</td><td>347.66 (n/a)</td><td>286.10 (n/a)</td><td>226.00 (n/a)</td><td>115.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-17.76%)</td><td>0.02 (-15.10%)</td><td>0.03 (-3.41%)</td><td>0.01 (-17.84%)</td><td>0.01 (-17.95%)</td><td>559.40 <b>(+21.71%)</b></td><td>392.76 (+17.88%)</td><td>311.30 (+3.53%)</td><td>271.50 <b>(+21.59%)</b></td><td>139.80 <b>(+22.20%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.60 (n/a)</td><td>333.20 (n/a)</td><td>300.70 (n/a)</td><td>223.30 (n/a)</td><td>114.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-6.43%)</td><td>0.02 (-14.82%)</td><td>0.02 (+4.23%)</td><td>0.01 <b>(+22.33%)</b></td><td>0.01 <b>(-27.33%)</b></td><td>818.50 (-18.26%)</td><td>552.70 (+4.16%)</td><td>540.20 (-4.07%)</td><td>274.60 (+6.85%)</td><td>205.76 <b>(-32.15%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1001.30 (n/a)</td><td>530.62 (n/a)</td><td>563.10 (n/a)</td><td>257.00 (n/a)</td><td>303.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-9.19%)</td><td>0.02 (-17.05%)</td><td>0.02 (-19.62%)</td><td>0.01 (+0.15%)</td><td>0.00 <b>(-26.25%)</b></td><td>606.90 (-0.15%)</td><td>487.36 (+16.59%)</td><td>477.50 <b>(+24.38%)</b></td><td>315.40 (+10.13%)</td><td>114.35 (-18.06%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.80 (n/a)</td><td>418.02 (n/a)</td><td>383.90 (n/a)</td><td>286.40 (n/a)</td><td>139.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-8.29%)</td><td>0.02 (-6.17%)</td><td>0.02 (-0.78%)</td><td>0.01 (+14.57%)</td><td>0.01 (-18.71%)</td><td>589.50 (-12.72%)</td><td>475.56 (+2.87%)</td><td>487.80 (+0.79%)</td><td>283.70 (+9.03%)</td><td>117.73 <b>(-23.79%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.40 (n/a)</td><td>462.30 (n/a)</td><td>484.00 (n/a)</td><td>260.20 (n/a)</td><td>154.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 <b>(-23.58%)</b></td><td>0.02 (-6.86%)</td><td>0.02 (+9.51%)</td><td>0.01 <b>(+155.34%)</b></td><td>0.01 <b>(-36.06%)</b></td><td>774.30 <b>(-60.83%)</b></td><td>432.62 <b>(-33.53%)</b></td><td>386.70 (-8.67%)</td><td>243.50 <b>(+30.84%)</b></td><td>219.93 <b>(-70.69%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1977.00 (n/a)</td><td>650.86 (n/a)</td><td>423.40 (n/a)</td><td>186.10 (n/a)</td><td>750.31 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-1.64%)</td><td>0.02 (+2.50%)</td><td>0.02 (-2.07%)</td><td>0.01 (+9.51%)</td><td>0.01 (-12.76%)</td><td>549.80 (-8.69%)</td><td>392.24 (-6.99%)</td><td>424.70 (+2.12%)</td><td>245.20 (+1.66%)</td><td>135.71 <b>(-23.05%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.10 (n/a)</td><td>421.72 (n/a)</td><td>415.90 (n/a)</td><td>241.20 (n/a)</td><td>176.36 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-3.12%)</td><td>0.02 (+2.67%)</td><td>0.02 (-16.26%)</td><td>0.01 (-8.47%)</td><td>0.01 <b>(+23.09%)</b></td><td>600.20 (+9.25%)</td><td>446.38 (+2.93%)</td><td>519.80 (+19.44%)</td><td>259.90 (+3.22%)</td><td>162.62 <b>(+44.59%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.40 (n/a)</td><td>433.68 (n/a)</td><td>435.20 (n/a)</td><td>251.80 (n/a)</td><td>112.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (+18.50%)</td><td>0.03 (+8.11%)</td><td>0.03 <b>(+61.10%)</b></td><td>0.01 <b>(-43.09%)</b></td><td>0.01 <b>(+34.86%)</b></td><td>973.90 <b>(+75.73%)</b></td><td>454.50 (+12.21%)</td><td>289.30 <b>(-37.92%)</b></td><td>199.30 (-15.62%)</td><td>322.86 <b>(+110.37%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.20 (n/a)</td><td>405.06 (n/a)</td><td>466.00 (n/a)</td><td>236.20 (n/a)</td><td>153.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (+4.62%)</td><td>0.02 (+3.56%)</td><td>0.03 (+10.62%)</td><td>0.01 (+2.06%)</td><td>0.01 (+18.04%)</td><td>582.20 (-2.02%)</td><td>383.76 (-1.27%)</td><td>293.50 (-9.58%)</td><td>275.90 (-4.40%)</td><td>143.04 (+9.11%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.20 (n/a)</td><td>388.70 (n/a)</td><td>324.60 (n/a)</td><td>288.60 (n/a)</td><td>131.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (+15.71%)</td><td>0.02 <b>(+30.00%)</b></td><td>0.02 <b>(+66.28%)</b></td><td>0.02 <b>(+36.70%)</b></td><td>0.01 (-4.83%)</td><td>527.30 <b>(-26.85%)</b></td><td>360.28 <b>(-27.50%)</b></td><td>349.20 <b>(-39.86%)</b></td><td>246.10 (-13.59%)</td><td>120.18 <b>(-38.61%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>720.80 (n/a)</td><td>496.92 (n/a)</td><td>580.60 (n/a)</td><td>284.80 (n/a)</td><td>195.77 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (+9.32%)</td><td>0.03 (+19.04%)</td><td>0.03 <b>(+24.63%)</b></td><td>0.02 <b>(+48.74%)</b></td><td>0.01 <b>(-23.20%)</b></td><td>392.20 <b>(-32.77%)</b></td><td>318.78 <b>(-21.15%)</b></td><td>315.20 (-19.78%)</td><td>239.30 (-8.52%)</td><td>72.58 <b>(-49.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.40 (n/a)</td><td>404.30 (n/a)</td><td>392.90 (n/a)</td><td>261.60 (n/a)</td><td>144.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.06 <b>(+29.84%)</b></td><td>0.04 <b>(+34.17%)</b></td><td>0.03 (+16.34%)</td><td>0.02 <b>(+37.91%)</b></td><td>0.02 <b>(+40.91%)</b></td><td>502.90 <b>(-27.49%)</b></td><td>382.72 <b>(-23.66%)</b></td><td>429.50 (-14.07%)</td><td>207.50 <b>(-23.01%)</b></td><td>133.45 (-12.45%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>693.60 (n/a)</td><td>501.36 (n/a)</td><td>499.80 (n/a)</td><td>269.50 (n/a)</td><td>152.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (+9.04%)</td><td>0.02 (+6.27%)</td><td>0.02 <b>(+21.37%)</b></td><td>0.01 (-7.73%)</td><td>0.01 <b>(+20.88%)</b></td><td>596.40 (+8.38%)</td><td>413.18 (-2.29%)</td><td>370.20 (-17.61%)</td><td>249.50 (-8.31%)</td><td>159.61 <b>(+23.22%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.30 (n/a)</td><td>422.88 (n/a)</td><td>449.30 (n/a)</td><td>272.10 (n/a)</td><td>129.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 <b>(+29.58%)</b></td><td>0.03 (+14.09%)</td><td>0.02 (+4.50%)</td><td>0.02 (-2.06%)</td><td>0.01 <b>(+74.85%)</b></td><td>584.60 (+2.11%)</td><td>390.12 (-6.12%)</td><td>416.20 (-4.30%)</td><td>223.30 <b>(-22.81%)</b></td><td>146.17 <b>(+35.03%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.50 (n/a)</td><td>415.56 (n/a)</td><td>434.90 (n/a)</td><td>289.30 (n/a)</td><td>108.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 <b>(-32.38%)</b></td><td>0.02 <b>(-22.73%)</b></td><td>0.02 <b>(-34.77%)</b></td><td>0.02 <b>(+30.72%)</b></td><td>0.00 <b>(-64.83%)</b></td><td>481.10 <b>(-23.50%)</b></td><td>432.70 (+14.73%)</td><td>445.40 <b>(+53.27%)</b></td><td>324.10 <b>(+47.92%)</b></td><td>63.41 <b>(-62.03%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.90 (n/a)</td><td>377.14 (n/a)</td><td>290.60 (n/a)</td><td>219.10 (n/a)</td><td>167.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.05 (+16.84%)</td><td>0.03 <b>(+53.88%)</b></td><td>0.02 <b>(+28.83%)</b></td><td>0.02 <b>(+239.76%)</b></td><td>0.01 (+15.30%)</td><td>593.90 <b>(-70.57%)</b></td><td>411.14 <b>(-49.25%)</b></td><td>471.10 <b>(-22.38%)</b></td><td>224.10 (-14.43%)</td><td>173.72 <b>(-74.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2018.00 (n/a)</td><td>810.12 (n/a)</td><td>606.90 (n/a)</td><td>261.90 (n/a)</td><td>690.59 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.03 (-17.27%)</td><td>0.02 <b>(-24.69%)</b></td><td>0.02 <b>(-42.82%)</b></td><td>0.01 (-9.42%)</td><td>0.01 (-5.90%)</td><td>592.00 (+10.41%)</td><td>435.36 <b>(+34.79%)</b></td><td>479.50 <b>(+74.87%)</b></td><td>260.20 <b>(+20.85%)</b></td><td>153.80 <b>(+20.08%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.20 (n/a)</td><td>323.00 (n/a)</td><td>274.20 (n/a)</td><td>215.30 (n/a)</td><td>128.08 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (-16.44%)</td><td>0.02 (-12.18%)</td><td>0.02 (-16.44%)</td><td>0.01 (-3.75%)</td><td>0.01 <b>(-22.33%)</b></td><td>650.50 (+3.90%)</td><td>432.34 (+9.26%)</td><td>379.40 (+19.68%)</td><td>245.50 (+19.70%)</td><td>171.59 (-5.35%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.10 (n/a)</td><td>395.70 (n/a)</td><td>317.00 (n/a)</td><td>205.10 (n/a)</td><td>181.28 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 <b>(-36.79%)</b></td><td>0.02 (-13.06%)</td><td>0.02 (+8.88%)</td><td>0.01 (+0.73%)</td><td>0.00 <b>(-64.05%)</b></td><td>610.20 (-0.73%)</td><td>480.86 (+3.66%)</td><td>482.00 (-8.16%)</td><td>358.40 <b>(+58.23%)</b></td><td>89.72 <b>(-43.45%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.70 (n/a)</td><td>463.90 (n/a)</td><td>524.80 (n/a)</td><td>226.50 (n/a)</td><td>158.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.04 (-5.10%)</td><td>0.03 (-1.44%)</td><td>0.03 <b>(+34.63%)</b></td><td>0.01 (-13.68%)</td><td>0.01 (+13.84%)</td><td>652.30 (+15.84%)</td><td>423.66 (+8.50%)</td><td>301.40 <b>(-25.73%)</b></td><td>259.30 (+5.36%)</td><td>200.07 <b>(+49.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>563.10 (n/a)</td><td>390.46 (n/a)</td><td>405.80 (n/a)</td><td>246.10 (n/a)</td><td>133.62 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.02 <b>(-36.59%)</b></td><td>0.02 (-3.38%)</td><td>0.02 (+18.38%)</td><td>0.01 <b>(+36.22%)</b></td><td>0.00 <b>(-59.95%)</b></td><td>650.60 <b>(-26.59%)</b></td><td>484.80 (-10.31%)</td><td>437.40 (-15.53%)</td><td>371.30 <b>(+57.73%)</b></td><td>116.47 <b>(-50.85%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>886.20 (n/a)</td><td>540.54 (n/a)</td><td>517.80 (n/a)</td><td>235.40 (n/a)</td><td>236.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.40 (+11.45%)</td><td>0.27 (+0.35%)</td><td>0.24 <b>(-29.96%)</b></td><td>0.17 (+10.29%)</td><td>0.11 (+5.77%)</td><td>570.80 (-9.34%)</td><td>410.26 (-1.95%)</td><td>412.50 <b>(+42.78%)</b></td><td>246.20 (-10.28%)</td><td>158.07 (-15.35%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.34 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>629.60 (n/a)</td><td>418.44 (n/a)</td><td>288.90 (n/a)</td><td>274.40 (n/a)</td><td>186.73 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.51 (+7.50%)</td><td>0.25 <b>(-23.86%)</b></td><td>0.21 <b>(-41.33%)</b></td><td>0.12 <b>(-37.62%)</b></td><td>0.15 <b>(+24.92%)</b></td><td>809.00 <b>(+60.33%)</b></td><td>491.72 <b>(+44.09%)</b></td><td>468.70 <b>(+70.44%)</b></td><td>192.50 (-7.00%)</td><td>219.17 <b>(+61.22%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>504.60 (n/a)</td><td>341.26 (n/a)</td><td>275.00 (n/a)</td><td>207.00 (n/a)</td><td>135.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.27 <b>(-24.78%)</b></td><td>0.19 <b>(-23.65%)</b></td><td>0.17 (-12.17%)</td><td>0.13 (-19.95%)</td><td>0.05 <b>(-42.94%)</b></td><td>749.90 <b>(+24.94%)</b></td><td>561.72 <b>(+24.75%)</b></td><td>583.30 (+13.86%)</td><td>367.00 <b>(+32.97%)</b></td><td>142.00 (-5.99%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>600.20 (n/a)</td><td>450.26 (n/a)</td><td>512.30 (n/a)</td><td>276.00 (n/a)</td><td>151.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.31 (+8.84%)</td><td>0.21 (+13.93%)</td><td>0.15 (+0.08%)</td><td>0.12 (+13.13%)</td><td>0.09 (+14.29%)</td><td>620.90 (-11.60%)</td><td>422.88 (-12.43%)</td><td>493.20 (-0.08%)</td><td>235.20 (-8.13%)</td><td>174.30 (-14.71%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>702.40 (n/a)</td><td>482.92 (n/a)</td><td>493.60 (n/a)</td><td>256.00 (n/a)</td><td>204.36 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.41 <b>(+42.88%)</b></td><td>0.21 (+11.10%)</td><td>0.16 (+14.15%)</td><td>0.07 <b>(-49.04%)</b></td><td>0.13 <b>(+81.42%)</b></td><td>1120.00 <b>(+96.25%)</b></td><td>503.10 (+16.91%)</td><td>447.10 (-12.40%)</td><td>179.70 <b>(-30.02%)</b></td><td>367.89 <b>(+154.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>570.70 (n/a)</td><td>430.32 (n/a)</td><td>510.40 (n/a)</td><td>256.80 (n/a)</td><td>144.31 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.28 (-7.51%)</td><td>0.18 (-12.40%)</td><td>0.15 (-13.04%)</td><td>0.14 (-10.67%)</td><td>0.06 (-0.04%)</td><td>530.30 (+11.95%)</td><td>447.38 (+15.52%)</td><td>488.40 (+15.00%)</td><td>263.30 (+8.13%)</td><td>107.75 <b>(+21.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>473.70 (n/a)</td><td>387.28 (n/a)</td><td>424.70 (n/a)</td><td>243.50 (n/a)</td><td>88.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.43 (-17.24%)</td><td>0.30 (-18.72%)</td><td>0.26 <b>(-32.08%)</b></td><td>0.21 (-13.97%)</td><td>0.10 (-16.74%)</td><td>631.40 (+16.24%)</td><td>471.02 <b>(+22.27%)</b></td><td>508.00 <b>(+47.25%)</b></td><td>307.30 <b>(+20.84%)</b></td><td>147.80 (+11.38%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.52 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>543.20 (n/a)</td><td>385.22 (n/a)</td><td>345.00 (n/a)</td><td>254.30 (n/a)</td><td>132.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.48 <b>(+89.83%)</b></td><td>0.35 <b>(+46.78%)</b></td><td>0.40 <b>(+63.25%)</b></td><td>0.20 (-2.48%)</td><td>0.12 <b>(+535.21%)</b></td><td>642.10 (+2.54%)</td><td>423.88 <b>(-24.17%)</b></td><td>327.90 <b>(-38.74%)</b></td><td>271.50 <b>(-47.31%)</b></td><td>164.46 <b>(+252.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>626.20 (n/a)</td><td>559.00 (n/a)</td><td>535.30 (n/a)</td><td>515.30 (n/a)</td><td>46.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.46 (-10.60%)</td><td>0.36 <b>(+78.00%)</b></td><td>0.40 <b>(+127.40%)</b></td><td>0.25 <b>(+280.87%)</b></td><td>0.10 <b>(-46.70%)</b></td><td>527.70 <b>(-73.74%)</b></td><td>386.74 <b>(-65.54%)</b></td><td>326.80 <b>(-56.02%)</b></td><td>283.70 (+11.87%)</td><td>114.53 <b>(-85.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.52 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>0.18 (n/a)</td><td>2009.90 (n/a)</td><td>1122.34 (n/a)</td><td>743.10 (n/a)</td><td>253.60 (n/a)</td><td>791.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.00 <b>(+133.33%)</b></td><td>0.00 <b>(+90.91%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+478.79%)</b></td><td>19138.96 (-1.84%)</td><td>13206.03 <b>(-27.04%)</b></td><td>16157.60 (-11.32%)</td><td>5870.38 <b>(-64.16%)</b></td><td>6629.26 <b>(+443.27%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19497.20 (n/a)</td><td>18101.11 (n/a)</td><td>18219.31 (n/a)</td><td>16380.05 (n/a)</td><td>1220.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.00 (-8.33%)</td><td>0.00 <b>(+55.17%)</b></td><td>0.00 <b>(+150.00%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(-27.01%)</b></td><td>16525.98 <b>(-28.09%)</b></td><td>9873.17 <b>(-42.32%)</b></td><td>7919.23 <b>(-58.16%)</b></td><td>7173.89 (+5.56%)</td><td>3947.34 <b>(-37.69%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22980.49 (n/a)</td><td>17117.16 (n/a)</td><td>18929.10 (n/a)</td><td>6796.32 (n/a)</td><td>6335.01 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>0.15 (+13.72%)</td><td>0.11 (+7.45%)</td><td>0.10 (+11.73%)</td><td>0.07 (-4.03%)</td><td>0.03 <b>(+20.76%)</b></td><td>29359.24 (+4.15%)</td><td>21125.40 (-5.47%)</td><td>20765.14 (-10.54%)</td><td>13984.00 (-12.06%)</td><td>6125.36 (+10.09%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28189.10 (n/a)</td><td>22347.59 (n/a)</td><td>23211.24 (n/a)</td><td>15901.35 (n/a)</td><td>5564.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>1.58 (-10.01%)</td><td>1.18 (+5.29%)</td><td>1.41 <b>(+49.55%)</b></td><td>0.62 (-13.74%)</td><td>0.44 (-1.91%)</td><td>844.10 (+15.93%)</td><td>513.62 (-2.87%)</td><td>373.00 <b>(-33.13%)</b></td><td>332.20 (+11.10%)</td><td>230.66 <b>(+21.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>1.75 (n/a)</td><td>1.12 (n/a)</td><td>0.94 (n/a)</td><td>0.72 (n/a)</td><td>0.45 (n/a)</td><td>728.10 (n/a)</td><td>528.78 (n/a)</td><td>557.80 (n/a)</td><td>299.00 (n/a)</td><td>189.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>2.43 (-11.55%)</td><td>1.12 <b>(-41.23%)</b></td><td>1.18 <b>(-23.53%)</b></td><td>0.30 <b>(-76.62%)</b></td><td>0.88 <b>(+33.27%)</b></td><td>3546.80 <b>(+327.74%)</b></td><td>1795.90 <b>(+198.03%)</b></td><td>888.80 <b>(+30.76%)</b></td><td>431.20 (+13.06%)</td><td>1522.20 <b>(+689.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>2.75 (n/a)</td><td>1.91 (n/a)</td><td>1.54 (n/a)</td><td>1.26 (n/a)</td><td>0.66 (n/a)</td><td>829.20 (n/a)</td><td>602.60 (n/a)</td><td>679.70 (n/a)</td><td>381.40 (n/a)</td><td>192.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:45</td><td>1.40 <b>(-20.79%)</b></td><td>1.15 (+7.72%)</td><td>1.09 (+17.17%)</td><td>1.04 <b>(+31.66%)</b></td><td>0.14 <b>(-63.84%)</b></td><td>502.40 <b>(-24.05%)</b></td><td>459.12 (-13.40%)</td><td>479.40 (-14.65%)</td><td>374.80 <b>(+26.24%)</b></td><td>50.69 <b>(-63.98%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:32:08</td><td>1.77 (n/a)</td><td>1.07 (n/a)</td><td>0.93 (n/a)</td><td>0.79 (n/a)</td><td>0.40 (n/a)</td><td>661.50 (n/a)</td><td>530.14 (n/a)</td><td>561.70 (n/a)</td><td>296.90 (n/a)</td><td>140.75 (n/a)</td>
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
