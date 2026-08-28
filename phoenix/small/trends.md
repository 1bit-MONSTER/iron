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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (-7.82%)</td><td>0.04 (-13.88%)</td><td>0.04 (-7.32%)</td><td>0.02 <b>(-37.27%)</b></td><td>0.01 <b>(+99.06%)</b></td><td>504.00 <b>(+59.44%)</b></td><td>334.06 <b>(+21.26%)</b></td><td>293.50 (+7.90%)</td><td>268.90 (+8.47%)</td><td>96.32 <b>(+260.42%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>316.10 (n/a)</td><td>275.50 (n/a)</td><td>272.00 (n/a)</td><td>247.90 (n/a)</td><td>26.72 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (-7.09%)</td><td>0.03 <b>(-23.41%)</b></td><td>0.02 <b>(-40.11%)</b></td><td>0.02 (+9.38%)</td><td>0.01 (-14.88%)</td><td>535.00 (-8.58%)</td><td>458.76 <b>(+26.72%)</b></td><td>500.70 <b>(+67.01%)</b></td><td>261.40 (+7.62%)</td><td>111.98 <b>(-20.19%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.20 (n/a)</td><td>362.02 (n/a)</td><td>299.80 (n/a)</td><td>242.90 (n/a)</td><td>140.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (-12.21%)</td><td>0.03 (-16.49%)</td><td>0.02 <b>(-20.13%)</b></td><td>0.02 (-10.42%)</td><td>0.01 <b>(-25.60%)</b></td><td>653.80 (+11.65%)</td><td>507.10 (+16.23%)</td><td>562.90 <b>(+25.20%)</b></td><td>315.30 (+13.91%)</td><td>136.82 (-6.69%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.60 (n/a)</td><td>436.28 (n/a)</td><td>449.60 (n/a)</td><td>276.80 (n/a)</td><td>146.63 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (-2.95%)</td><td>0.01 <b>(-22.11%)</b></td><td>0.01 <b>(-26.04%)</b></td><td>0.01 <b>(-28.31%)</b></td><td>0.01 (+16.29%)</td><td>691.70 <b>(+39.51%)</b></td><td>500.44 <b>(+37.24%)</b></td><td>475.50 <b>(+35.20%)</b></td><td>223.30 (+3.05%)</td><td>183.34 <b>(+56.83%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>495.80 (n/a)</td><td>364.64 (n/a)</td><td>351.70 (n/a)</td><td>216.70 (n/a)</td><td>116.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (+0.07%)</td><td>0.01 (-14.16%)</td><td>0.02 (-12.34%)</td><td>0.01 <b>(-36.04%)</b></td><td>0.01 <b>(+35.36%)</b></td><td>801.20 <b>(+56.33%)</b></td><td>416.16 <b>(+29.27%)</b></td><td>325.50 (+14.05%)</td><td>243.10 (-0.08%)</td><td>224.87 <b>(+108.15%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.50 (n/a)</td><td>321.92 (n/a)</td><td>285.40 (n/a)</td><td>243.30 (n/a)</td><td>108.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (-13.21%)</td><td>0.02 (-4.64%)</td><td>0.01 <b>(-32.46%)</b></td><td>0.01 <b>(+309.09%)</b></td><td>0.00 <b>(-49.79%)</b></td><td>455.70 <b>(-75.56%)</b></td><td>367.66 <b>(-39.44%)</b></td><td>401.00 <b>(+48.08%)</b></td><td>259.90 (+15.20%)</td><td>95.94 <b>(-86.45%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1864.40 (n/a)</td><td>607.12 (n/a)</td><td>270.80 (n/a)</td><td>225.60 (n/a)</td><td>707.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (+2.52%)</td><td>0.01 (+18.88%)</td><td>0.01 (-1.85%)</td><td>0.01 <b>(+22.28%)</b></td><td>0.01 (+11.52%)</td><td>629.20 (-18.22%)</td><td>419.68 (-14.97%)</td><td>483.50 (+1.88%)</td><td>221.50 (-2.47%)</td><td>176.16 (-9.58%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>769.40 (n/a)</td><td>493.56 (n/a)</td><td>474.60 (n/a)</td><td>227.10 (n/a)</td><td>194.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (+6.68%)</td><td>0.02 <b>(+37.23%)</b></td><td>0.02 <b>(+61.55%)</b></td><td>0.02 <b>(+273.91%)</b></td><td>0.00 <b>(-57.29%)</b></td><td>298.60 <b>(-73.26%)</b></td><td>271.38 <b>(-46.10%)</b></td><td>278.80 <b>(-38.09%)</b></td><td>205.70 (-6.24%)</td><td>38.17 <b>(-89.43%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1116.70 (n/a)</td><td>503.48 (n/a)</td><td>450.30 (n/a)</td><td>219.40 (n/a)</td><td>361.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 <b>(+23.34%)</b></td><td>0.01 (+13.23%)</td><td>0.01 (-5.09%)</td><td>0.01 (+12.57%)</td><td>0.01 <b>(+45.20%)</b></td><td>716.20 (-11.16%)</td><td>467.04 (-4.78%)</td><td>470.40 (+5.35%)</td><td>205.60 (-18.93%)</td><td>214.87 (+7.25%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>806.20 (n/a)</td><td>490.50 (n/a)</td><td>446.50 (n/a)</td><td>253.60 (n/a)</td><td>200.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>440.50 (n/a)</td><td>323.48 (n/a)</td><td>300.80 (n/a)</td><td>204.90 (n/a)</td><td>107.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.60 (n/a)</td><td>384.40 (n/a)</td><td>319.50 (n/a)</td><td>237.90 (n/a)</td><td>165.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>636.60 (n/a)</td><td>465.24 (n/a)</td><td>527.70 (n/a)</td><td>289.60 (n/a)</td><td>159.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>759.60 (n/a)</td><td>430.74 (n/a)</td><td>408.20 (n/a)</td><td>265.00 (n/a)</td><td>196.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>582.40 (n/a)</td><td>423.80 (n/a)</td><td>431.80 (n/a)</td><td>196.50 (n/a)</td><td>145.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>651.60 (n/a)</td><td>463.88 (n/a)</td><td>532.50 (n/a)</td><td>239.70 (n/a)</td><td>175.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.20 (n/a)</td><td>410.68 (n/a)</td><td>421.70 (n/a)</td><td>273.60 (n/a)</td><td>127.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.00 (n/a)</td><td>459.94 (n/a)</td><td>455.40 (n/a)</td><td>348.80 (n/a)</td><td>109.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.10 (n/a)</td><td>366.90 (n/a)</td><td>304.50 (n/a)</td><td>239.60 (n/a)</td><td>140.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.50 (n/a)</td><td>426.44 (n/a)</td><td>390.00 (n/a)</td><td>294.50 (n/a)</td><td>132.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>683.10 (n/a)</td><td>446.28 (n/a)</td><td>463.20 (n/a)</td><td>233.70 (n/a)</td><td>181.65 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1878.40 (n/a)</td><td>683.06 (n/a)</td><td>455.20 (n/a)</td><td>264.70 (n/a)</td><td>673.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.48 <b>(-38.35%)</b></td><td>0.35 <b>(-34.26%)</b></td><td>0.39 <b>(-20.63%)</b></td><td>0.22 <b>(-45.54%)</b></td><td>0.11 <b>(-29.82%)</b></td><td>1003.40 <b>(+83.64%)</b></td><td>681.48 <b>(+56.28%)</b></td><td>568.80 <b>(+25.98%)</b></td><td>458.90 <b>(+62.21%)</b></td><td>229.31 <b>(+112.52%)</b></td><td>20.57 <b>(-38.35%)</b></td><td>15.07 <b>(-34.26%)</b></td><td>16.59 <b>(-20.63%)</b></td><td>9.40 <b>(-45.54%)</b></td><td>4.61 <b>(-29.82%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.78 (n/a)</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.15 (n/a)</td><td>546.40 (n/a)</td><td>436.06 (n/a)</td><td>451.50 (n/a)</td><td>282.90 (n/a)</td><td>107.90 (n/a)</td><td>33.36 (n/a)</td><td>22.92 (n/a)</td><td>20.90 (n/a)</td><td>17.27 (n/a)</td><td>6.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.57 (+15.81%)</td><td>0.41 (+0.57%)</td><td>0.38 (-9.22%)</td><td>0.30 (+16.41%)</td><td>0.10 (+7.53%)</td><td>729.10 (-14.09%)</td><td>565.98 (-1.53%)</td><td>577.90 (+10.16%)</td><td>389.10 (-13.65%)</td><td>121.95 <b>(-24.37%)</b></td><td>24.26 (+15.81%)</td><td>17.38 (+0.57%)</td><td>16.33 (-9.22%)</td><td>12.94 (+16.41%)</td><td>4.19 (+7.53%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.49 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>848.70 (n/a)</td><td>574.76 (n/a)</td><td>524.60 (n/a)</td><td>450.60 (n/a)</td><td>161.24 (n/a)</td><td>20.95 (n/a)</td><td>17.28 (n/a)</td><td>17.99 (n/a)</td><td>11.12 (n/a)</td><td>3.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.31 (+0.35%)</td><td>0.30 (-0.71%)</td><td>0.30 (-0.73%)</td><td>0.30 (-0.94%)</td><td>0.00 <b>(+38.52%)</b></td><td>84790.80 (+0.95%)</td><td>82965.44 (+0.72%)</td><td>82633.30 (+0.74%)</td><td>81299.40 (-0.35%)</td><td>1305.76 <b>(+39.10%)</b></td><td>211.32 (+0.35%)</td><td>207.11 (-0.71%)</td><td>207.90 (-0.73%)</td><td>202.61 (-0.94%)</td><td>3.25 <b>(+38.52%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83994.30 (n/a)</td><td>82368.58 (n/a)</td><td>82028.40 (n/a)</td><td>81585.10 (n/a)</td><td>938.75 (n/a)</td><td>210.58 (n/a)</td><td>208.59 (n/a)</td><td>209.44 (n/a)</td><td>204.54 (n/a)</td><td>2.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>1.04 (-0.22%)</td><td>1.02 (+0.02%)</td><td>1.02 (-0.32%)</td><td>1.01 (+0.15%)</td><td>0.01 (-7.33%)</td><td>24930.10 (-0.15%)</td><td>24664.64 (-0.03%)</td><td>24740.90 (+0.32%)</td><td>24295.30 (+0.22%)</td><td>262.30 (-7.24%)</td><td>707.13 (-0.22%)</td><td>696.60 (+0.02%)</td><td>694.39 (-0.32%)</td><td>689.12 (+0.15%)</td><td>7.44 (-7.33%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>0.01 (n/a)</td><td>24968.20 (n/a)</td><td>24670.94 (n/a)</td><td>24660.90 (n/a)</td><td>24241.70 (n/a)</td><td>282.79 (n/a)</td><td>708.69 (n/a)</td><td>696.43 (n/a)</td><td>696.65 (n/a)</td><td>688.07 (n/a)</td><td>8.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>3.97 (+13.35%)</td><td>2.63 (+9.30%)</td><td>2.88 <b>(+42.99%)</b></td><td>1.39 (-2.01%)</td><td>1.09 (+8.39%)</td><td>5795.60 (+2.05%)</td><td>3610.06 (-6.55%)</td><td>2797.50 <b>(-30.07%)</b></td><td>2029.80 (-11.78%)</td><td>1659.70 (+8.16%)</td><td>1041.45 (+13.35%)</td><td>688.50 (+9.30%)</td><td>755.64 <b>(+42.99%)</b></td><td>364.75 (-2.01%)</td><td>287.05 (+8.39%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>3.50 (n/a)</td><td>2.40 (n/a)</td><td>2.02 (n/a)</td><td>1.42 (n/a)</td><td>1.01 (n/a)</td><td>5679.00 (n/a)</td><td>3862.90 (n/a)</td><td>4000.30 (n/a)</td><td>2300.90 (n/a)</td><td>1534.53 (n/a)</td><td>918.75 (n/a)</td><td>629.93 (n/a)</td><td>528.44 (n/a)</td><td>372.24 (n/a)</td><td>264.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.23 (-16.50%)</td><td>0.20 (+2.60%)</td><td>0.19 (+8.12%)</td><td>0.18 <b>(+28.70%)</b></td><td>0.02 <b>(-67.62%)</b></td><td>6900.30 <b>(-22.30%)</b></td><td>6321.66 (-7.89%)</td><td>6441.00 (-7.51%)</td><td>5530.30 (+19.77%)</td><td>548.04 <b>(-70.34%)</b></td><td>12.13 (-16.50%)</td><td>10.68 (+2.60%)</td><td>10.42 (+8.12%)</td><td>9.73 <b>(+28.70%)</b></td><td>0.97 <b>(-67.62%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>8880.50 (n/a)</td><td>6863.32 (n/a)</td><td>6963.80 (n/a)</td><td>4617.60 (n/a)</td><td>1847.59 (n/a)</td><td>14.53 (n/a)</td><td>10.41 (n/a)</td><td>9.64 (n/a)</td><td>7.56 (n/a)</td><td>2.98 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>3.83 (n/a)</td><td>3.55 (n/a)</td><td>3.49 (n/a)</td><td>3.39 (n/a)</td><td>0.19 (n/a)</td><td>3.83 (n/a)</td><td>3.55 (n/a)</td><td>3.49 (n/a)</td><td>3.39 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>6.76 (-11.38%)</td><td>6.28 (-9.89%)</td><td>6.52 (-5.58%)</td><td>5.67 (-7.52%)</td><td>0.48 (-15.24%)</td><td>6.76 (-11.38%)</td><td>6.27 (-9.89%)</td><td>6.51 (-5.58%)</td><td>5.67 (-7.52%)</td><td>0.48 (-15.24%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>7.63 (n/a)</td><td>6.97 (n/a)</td><td>6.90 (n/a)</td><td>6.13 (n/a)</td><td>0.57 (n/a)</td><td>7.63 (n/a)</td><td>6.96 (n/a)</td><td>6.90 (n/a)</td><td>6.13 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>9.84 (+17.95%)</td><td>8.29 (+4.29%)</td><td>8.26 (+2.26%)</td><td>6.61 (-10.42%)</td><td>1.27 <b>(+235.41%)</b></td><td>9.84 (+17.95%)</td><td>8.28 (+4.29%)</td><td>8.26 (+2.26%)</td><td>6.61 (-10.42%)</td><td>1.27 <b>(+235.41%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>8.34 (n/a)</td><td>7.95 (n/a)</td><td>8.08 (n/a)</td><td>7.38 (n/a)</td><td>0.38 (n/a)</td><td>8.34 (n/a)</td><td>7.94 (n/a)</td><td>8.08 (n/a)</td><td>7.37 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>3.83 (n/a)</td><td>3.67 (n/a)</td><td>3.79 (n/a)</td><td>3.19 (n/a)</td><td>0.27 (n/a)</td><td>3.83 (n/a)</td><td>3.67 (n/a)</td><td>3.79 (n/a)</td><td>3.19 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>7.14 (+3.25%)</td><td>5.64 (-16.20%)</td><td>5.65 (-16.05%)</td><td>4.61 <b>(-28.47%)</b></td><td>0.96 <b>(+445.54%)</b></td><td>7.14 (+3.25%)</td><td>5.64 (-16.20%)</td><td>5.65 (-16.05%)</td><td>4.61 <b>(-28.47%)</b></td><td>0.96 <b>(+445.54%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>6.92 (n/a)</td><td>6.73 (n/a)</td><td>6.73 (n/a)</td><td>6.45 (n/a)</td><td>0.18 (n/a)</td><td>6.91 (n/a)</td><td>6.73 (n/a)</td><td>6.73 (n/a)</td><td>6.45 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>14.40 (+1.96%)</td><td>9.35 (-6.81%)</td><td>8.42 (+1.42%)</td><td>7.35 (-1.02%)</td><td>2.86 (-10.82%)</td><td>14.39 (+1.96%)</td><td>9.34 (-6.81%)</td><td>8.41 (+1.42%)</td><td>7.35 (-1.02%)</td><td>2.86 (-10.82%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>14.12 (n/a)</td><td>10.03 (n/a)</td><td>8.30 (n/a)</td><td>7.43 (n/a)</td><td>3.20 (n/a)</td><td>14.11 (n/a)</td><td>10.03 (n/a)</td><td>8.29 (n/a)</td><td>7.42 (n/a)</td><td>3.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>3.26 (+8.66%)</td><td>2.56 <b>(+24.92%)</b></td><td>2.67 <b>(+28.96%)</b></td><td>1.68 <b>(+64.71%)</b></td><td>0.67 <b>(-23.95%)</b></td><td>3.25 (+8.66%)</td><td>2.55 <b>(+24.92%)</b></td><td>2.67 <b>(+28.96%)</b></td><td>1.68 <b>(+64.71%)</b></td><td>0.67 <b>(-23.95%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>3.00 (n/a)</td><td>2.05 (n/a)</td><td>2.07 (n/a)</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td><td>2.99 (n/a)</td><td>2.04 (n/a)</td><td>2.07 (n/a)</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.51 (-5.60%)</td><td>0.30 (+12.66%)</td><td>0.26 <b>(+89.40%)</b></td><td>0.08 (+1.53%)</td><td>0.20 (-11.18%)</td><td>0.50 (-5.60%)</td><td>0.29 (+12.66%)</td><td>0.26 <b>(+89.40%)</b></td><td>0.07 (+1.53%)</td><td>0.20 (-11.18%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.54 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.23 (n/a)</td><td>0.53 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.62 (+18.63%)</td><td>0.39 <b>(+32.87%)</b></td><td>0.44 <b>(+30.66%)</b></td><td>0.08 (-5.84%)</td><td>0.22 (+13.21%)</td><td>0.61 (+18.63%)</td><td>0.39 <b>(+32.87%)</b></td><td>0.43 <b>(+30.66%)</b></td><td>0.07 (-5.84%)</td><td>0.21 (+13.21%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.52 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td><td>0.51 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>1.76 <b>(-22.34%)</b></td><td>1.26 (-10.07%)</td><td>1.49 (+7.71%)</td><td>0.64 <b>(+42.48%)</b></td><td>0.55 <b>(-35.44%)</b></td><td>1.74 <b>(-22.34%)</b></td><td>1.24 (-10.07%)</td><td>1.47 (+7.71%)</td><td>0.63 <b>(+42.48%)</b></td><td>0.55 <b>(-35.44%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>2.27 (n/a)</td><td>1.41 (n/a)</td><td>1.39 (n/a)</td><td>0.45 (n/a)</td><td>0.86 (n/a)</td><td>2.24 (n/a)</td><td>1.38 (n/a)</td><td>1.37 (n/a)</td><td>0.44 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.30 (n/a)</td><td>370.86 (n/a)</td><td>307.80 (n/a)</td><td>293.10 (n/a)</td><td>106.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.90 (n/a)</td><td>310.62 (n/a)</td><td>261.00 (n/a)</td><td>239.60 (n/a)</td><td>122.87 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.70 (n/a)</td><td>358.46 (n/a)</td><td>319.00 (n/a)</td><td>238.50 (n/a)</td><td>118.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.80 (n/a)</td><td>430.62 (n/a)</td><td>513.30 (n/a)</td><td>225.40 (n/a)</td><td>162.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.70 (n/a)</td><td>435.82 (n/a)</td><td>396.70 (n/a)</td><td>290.50 (n/a)</td><td>144.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1322.30 (n/a)</td><td>607.80 (n/a)</td><td>488.00 (n/a)</td><td>279.90 (n/a)</td><td>411.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (+8.19%)</td><td>0.02 (-14.17%)</td><td>0.01 <b>(-44.80%)</b></td><td>0.01 (-11.62%)</td><td>0.01 <b>(+66.75%)</b></td><td>577.60 (+13.14%)</td><td>438.14 <b>(+30.91%)</b></td><td>563.30 <b>(+81.18%)</b></td><td>217.00 (-7.58%)</td><td>181.63 <b>(+74.76%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.50 (n/a)</td><td>334.68 (n/a)</td><td>310.90 (n/a)</td><td>234.80 (n/a)</td><td>103.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (+8.99%)</td><td>0.03 (+9.28%)</td><td>0.03 (+6.01%)</td><td>0.02 <b>(+79.65%)</b></td><td>0.00 <b>(-37.39%)</b></td><td>366.90 <b>(-44.33%)</b></td><td>294.42 (-16.89%)</td><td>267.70 (-5.67%)</td><td>242.90 (-8.24%)</td><td>53.29 <b>(-68.81%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>659.10 (n/a)</td><td>354.26 (n/a)</td><td>283.80 (n/a)</td><td>264.70 (n/a)</td><td>170.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 <b>(+24.99%)</b></td><td>0.03 (+15.35%)</td><td>0.03 <b>(+35.55%)</b></td><td>0.01 <b>(-20.62%)</b></td><td>0.01 <b>(+84.17%)</b></td><td>578.60 <b>(+25.97%)</b></td><td>378.54 (-2.49%)</td><td>288.20 <b>(-26.22%)</b></td><td>201.60 <b>(-20.00%)</b></td><td>171.10 <b>(+105.38%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.30 (n/a)</td><td>388.22 (n/a)</td><td>390.60 (n/a)</td><td>252.00 (n/a)</td><td>83.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (-16.18%)</td><td>0.02 (-2.58%)</td><td>0.02 (-4.17%)</td><td>0.02 (+3.45%)</td><td>0.01 <b>(-25.83%)</b></td><td>524.70 (-3.33%)</td><td>401.20 (-1.12%)</td><td>449.40 (+4.34%)</td><td>273.60 (+19.32%)</td><td>108.59 (-17.62%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.80 (n/a)</td><td>405.76 (n/a)</td><td>430.70 (n/a)</td><td>229.30 (n/a)</td><td>131.82 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.02 (+17.63%)</td><td>0.02 <b>(+23.56%)</b></td><td>0.02 <b>(+25.91%)</b></td><td>0.01 <b>(+38.54%)</b></td><td>0.00 (+0.48%)</td><td>547.50 <b>(-27.81%)</b></td><td>446.04 <b>(-20.40%)</b></td><td>454.10 <b>(-20.58%)</b></td><td>362.50 (-14.97%)</td><td>82.86 <b>(-38.65%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>758.40 (n/a)</td><td>560.32 (n/a)</td><td>571.80 (n/a)</td><td>426.30 (n/a)</td><td>135.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (+10.00%)</td><td>0.02 (-11.50%)</td><td>0.02 <b>(-37.10%)</b></td><td>0.01 <b>(-32.52%)</b></td><td>0.01 <b>(+29.41%)</b></td><td>778.90 <b>(+48.19%)</b></td><td>439.06 <b>(+26.16%)</b></td><td>473.90 <b>(+58.97%)</b></td><td>192.80 (-9.10%)</td><td>227.87 <b>(+65.54%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.60 (n/a)</td><td>348.02 (n/a)</td><td>298.10 (n/a)</td><td>212.10 (n/a)</td><td>137.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 <b>(-32.21%)</b></td><td>0.02 <b>(-23.49%)</b></td><td>0.02 (+3.71%)</td><td>0.01 <b>(-24.15%)</b></td><td>0.01 <b>(-48.13%)</b></td><td>692.20 <b>(+31.85%)</b></td><td>467.32 <b>(+20.08%)</b></td><td>450.30 (-3.58%)</td><td>284.30 <b>(+47.54%)</b></td><td>152.62 (-3.52%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.00 (n/a)</td><td>389.18 (n/a)</td><td>467.00 (n/a)</td><td>192.70 (n/a)</td><td>158.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (-8.37%)</td><td>0.02 (-9.73%)</td><td>0.02 <b>(-20.02%)</b></td><td>0.02 (+6.11%)</td><td>0.01 (-16.95%)</td><td>536.00 (-5.75%)</td><td>431.24 (+6.76%)</td><td>462.80 <b>(+25.05%)</b></td><td>244.50 (+9.10%)</td><td>122.46 (-18.54%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.70 (n/a)</td><td>403.92 (n/a)</td><td>370.10 (n/a)</td><td>224.10 (n/a)</td><td>150.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (+15.42%)</td><td>0.02 (-14.07%)</td><td>0.02 <b>(-39.68%)</b></td><td>0.01 <b>(-35.69%)</b></td><td>0.01 <b>(+147.61%)</b></td><td>645.20 <b>(+55.51%)</b></td><td>422.64 <b>(+39.72%)</b></td><td>486.60 <b>(+65.79%)</b></td><td>213.00 (-13.34%)</td><td>196.42 <b>(+197.49%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>414.90 (n/a)</td><td>302.50 (n/a)</td><td>293.50 (n/a)</td><td>245.80 (n/a)</td><td>66.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 <b>(+27.27%)</b></td><td>0.03 (-1.91%)</td><td>0.02 <b>(-35.33%)</b></td><td>0.02 (+3.84%)</td><td>0.01 <b>(+36.57%)</b></td><td>495.60 (-3.69%)</td><td>373.36 (+7.19%)</td><td>449.50 <b>(+54.63%)</b></td><td>183.90 <b>(-21.44%)</b></td><td>146.14 (+9.82%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.60 (n/a)</td><td>348.30 (n/a)</td><td>290.70 (n/a)</td><td>234.10 (n/a)</td><td>133.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 <b>(+50.44%)</b></td><td>0.03 <b>(+33.56%)</b></td><td>0.03 (+3.99%)</td><td>0.01 <b>(+330.41%)</b></td><td>0.02 <b>(+20.34%)</b></td><td>565.40 <b>(-76.77%)</b></td><td>333.24 <b>(-55.19%)</b></td><td>282.10 (-3.82%)</td><td>153.90 <b>(-33.55%)</b></td><td>169.79 <b>(-82.13%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2433.40 (n/a)</td><td>743.60 (n/a)</td><td>293.30 (n/a)</td><td>231.60 (n/a)</td><td>950.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (-7.11%)</td><td>0.02 (+0.79%)</td><td>0.02 (+1.24%)</td><td>0.02 (+12.31%)</td><td>0.01 (-19.39%)</td><td>466.10 (-10.96%)</td><td>397.76 (-3.34%)</td><td>451.90 (-1.22%)</td><td>260.00 (+7.66%)</td><td>90.91 (-19.56%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.50 (n/a)</td><td>411.52 (n/a)</td><td>457.50 (n/a)</td><td>241.50 (n/a)</td><td>113.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (+3.58%)</td><td>0.02 <b>(+23.58%)</b></td><td>0.01 (-7.75%)</td><td>0.01 <b>(+216.97%)</b></td><td>0.01 (+7.74%)</td><td>795.40 <b>(-68.45%)</b></td><td>503.08 <b>(-42.01%)</b></td><td>546.80 (+8.41%)</td><td>243.50 (-3.45%)</td><td>247.99 <b>(-73.43%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2521.10 (n/a)</td><td>867.56 (n/a)</td><td>504.40 (n/a)</td><td>252.20 (n/a)</td><td>933.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (+14.88%)</td><td>0.02 (+14.44%)</td><td>0.02 <b>(+25.06%)</b></td><td>0.01 (-8.56%)</td><td>0.01 <b>(+34.84%)</b></td><td>587.80 (+9.36%)</td><td>409.44 (-9.04%)</td><td>382.50 <b>(-20.03%)</b></td><td>243.50 (-12.94%)</td><td>135.04 <b>(+36.70%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.50 (n/a)</td><td>450.14 (n/a)</td><td>478.30 (n/a)</td><td>279.70 (n/a)</td><td>98.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (-17.70%)</td><td>0.02 (-10.77%)</td><td>0.02 <b>(-21.46%)</b></td><td>0.02 <b>(+51.45%)</b></td><td>0.01 <b>(-34.35%)</b></td><td>521.40 <b>(-33.97%)</b></td><td>379.30 (-3.63%)</td><td>378.40 <b>(+27.32%)</b></td><td>234.70 <b>(+21.48%)</b></td><td>127.86 <b>(-47.37%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>789.70 (n/a)</td><td>393.60 (n/a)</td><td>297.20 (n/a)</td><td>193.20 (n/a)</td><td>242.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.05 (-16.67%)</td><td>0.04 <b>(+26.34%)</b></td><td>0.04 <b>(+73.10%)</b></td><td>0.03 <b>(+37.90%)</b></td><td>0.01 <b>(-47.24%)</b></td><td>484.80 <b>(-27.48%)</b></td><td>314.16 <b>(-32.18%)</b></td><td>277.30 <b>(-42.23%)</b></td><td>247.80 <b>(+20.00%)</b></td><td>96.72 <b>(-54.35%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>668.50 (n/a)</td><td>463.20 (n/a)</td><td>480.00 (n/a)</td><td>206.50 (n/a)</td><td>211.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (-2.25%)</td><td>0.03 <b>(+21.66%)</b></td><td>0.03 <b>(+74.25%)</b></td><td>0.02 (+16.58%)</td><td>0.01 (-2.79%)</td><td>508.80 (-14.23%)</td><td>352.40 (-18.10%)</td><td>272.30 <b>(-42.61%)</b></td><td>223.80 (+2.29%)</td><td>134.73 (-3.24%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.20 (n/a)</td><td>430.28 (n/a)</td><td>474.50 (n/a)</td><td>218.80 (n/a)</td><td>139.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.07 <b>(+31.98%)</b></td><td>0.04 <b>(+20.42%)</b></td><td>0.04 (+11.25%)</td><td>0.02 <b>(+26.31%)</b></td><td>0.02 <b>(+37.45%)</b></td><td>430.80 <b>(-20.84%)</b></td><td>309.44 (-15.76%)</td><td>285.10 (-10.12%)</td><td>154.70 <b>(-24.24%)</b></td><td>116.67 (-17.43%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.20 (n/a)</td><td>367.32 (n/a)</td><td>317.20 (n/a)</td><td>204.20 (n/a)</td><td>141.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 (+19.04%)</td><td>0.03 (+6.14%)</td><td>0.02 (-19.94%)</td><td>0.01 (-1.77%)</td><td>0.01 <b>(+48.09%)</b></td><td>560.90 (+1.80%)</td><td>382.02 (+0.57%)</td><td>388.80 <b>(+24.90%)</b></td><td>210.10 (-16.03%)</td><td>158.14 <b>(+21.32%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.00 (n/a)</td><td>379.84 (n/a)</td><td>311.30 (n/a)</td><td>250.20 (n/a)</td><td>130.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.06 (+14.47%)</td><td>0.04 <b>(+55.59%)</b></td><td>0.04 <b>(+112.81%)</b></td><td>0.02 <b>(+25.48%)</b></td><td>0.01 (-10.70%)</td><td>429.10 <b>(-20.32%)</b></td><td>268.72 <b>(-39.17%)</b></td><td>241.50 <b>(-53.00%)</b></td><td>176.90 (-12.64%)</td><td>94.82 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.50 (n/a)</td><td>441.78 (n/a)</td><td>513.80 (n/a)</td><td>202.50 (n/a)</td><td>141.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (-9.87%)</td><td>0.02 (+1.66%)</td><td>0.03 <b>(+26.66%)</b></td><td>0.01 (+4.22%)</td><td>0.01 (-17.90%)</td><td>546.90 (-4.05%)</td><td>362.30 (-4.26%)</td><td>287.00 <b>(-21.07%)</b></td><td>273.50 (+10.95%)</td><td>122.28 (-11.63%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.00 (n/a)</td><td>378.42 (n/a)</td><td>363.60 (n/a)</td><td>246.50 (n/a)</td><td>138.37 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (+7.57%)</td><td>0.03 <b>(+25.98%)</b></td><td>0.03 <b>(+58.54%)</b></td><td>0.02 (+12.57%)</td><td>0.01 <b>(+35.30%)</b></td><td>543.50 (-11.16%)</td><td>385.70 (-18.37%)</td><td>299.80 <b>(-36.92%)</b></td><td>288.90 (-7.05%)</td><td>124.64 (+14.97%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.80 (n/a)</td><td>472.52 (n/a)</td><td>475.30 (n/a)</td><td>310.80 (n/a)</td><td>108.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (-9.36%)</td><td>0.02 (-8.99%)</td><td>0.02 (-19.51%)</td><td>0.01 (-17.66%)</td><td>0.01 (+8.80%)</td><td>648.00 <b>(+21.44%)</b></td><td>448.54 (+16.91%)</td><td>438.20 <b>(+24.24%)</b></td><td>236.20 (+10.32%)</td><td>197.33 <b>(+45.46%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.60 (n/a)</td><td>383.66 (n/a)</td><td>352.70 (n/a)</td><td>214.10 (n/a)</td><td>135.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.03 (-4.34%)</td><td>0.02 (-7.42%)</td><td>0.02 (-0.49%)</td><td>0.02 (-2.91%)</td><td>0.01 (-9.21%)</td><td>527.50 (+3.01%)</td><td>434.54 (+7.46%)</td><td>437.00 (+0.51%)</td><td>301.80 (+4.54%)</td><td>85.69 (-3.42%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.10 (n/a)</td><td>404.36 (n/a)</td><td>434.80 (n/a)</td><td>288.70 (n/a)</td><td>88.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.04 <b>(+64.13%)</b></td><td>0.02 <b>(+43.93%)</b></td><td>0.03 <b>(+111.04%)</b></td><td>0.00 <b>(-65.91%)</b></td><td>0.01 <b>(+248.12%)</b></td><td>1935.20 <b>(+193.35%)</b></td><td>641.72 <b>(+27.44%)</b></td><td>247.80 <b>(-52.63%)</b></td><td>228.30 <b>(-39.09%)</b></td><td>736.77 <b>(+513.53%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.70 (n/a)</td><td>503.56 (n/a)</td><td>523.10 (n/a)</td><td>374.80 (n/a)</td><td>120.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.41 (+19.91%)</td><td>0.23 (+14.71%)</td><td>0.19 (-9.78%)</td><td>0.16 <b>(+70.84%)</b></td><td>0.10 (+11.65%)</td><td>610.70 <b>(-41.47%)</b></td><td>469.72 (-18.33%)</td><td>523.70 (+10.84%)</td><td>242.00 (-16.61%)</td><td>141.37 <b>(-50.24%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.34 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>1043.40 (n/a)</td><td>575.14 (n/a)</td><td>472.50 (n/a)</td><td>290.20 (n/a)</td><td>284.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.41 (+1.14%)</td><td>0.24 (-19.86%)</td><td>0.19 <b>(-40.89%)</b></td><td>0.14 <b>(-23.04%)</b></td><td>0.11 (+3.35%)</td><td>697.50 <b>(+29.94%)</b></td><td>469.62 <b>(+28.46%)</b></td><td>517.40 <b>(+69.20%)</b></td><td>240.90 (-1.15%)</td><td>177.65 <b>(+28.86%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>536.80 (n/a)</td><td>365.58 (n/a)</td><td>305.80 (n/a)</td><td>243.70 (n/a)</td><td>137.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.36 (+5.24%)</td><td>0.23 (+6.52%)</td><td>0.20 (+6.92%)</td><td>0.16 (-6.55%)</td><td>0.08 (+8.36%)</td><td>607.20 (+7.01%)</td><td>456.84 (-5.23%)</td><td>480.40 (-6.46%)</td><td>272.70 (-4.98%)</td><td>123.67 (+9.02%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>567.40 (n/a)</td><td>482.06 (n/a)</td><td>513.60 (n/a)</td><td>287.00 (n/a)</td><td>113.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.29 (+18.37%)</td><td>0.20 <b>(+26.84%)</b></td><td>0.17 (-3.71%)</td><td>0.12 <b>(+209.10%)</b></td><td>0.08 (-0.89%)</td><td>624.00 <b>(-67.65%)</b></td><td>420.64 <b>(-41.64%)</b></td><td>433.50 (+3.86%)</td><td>255.30 (-15.49%)</td><td>158.28 <b>(-76.81%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1928.70 (n/a)</td><td>720.76 (n/a)</td><td>417.40 (n/a)</td><td>302.10 (n/a)</td><td>682.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.27 (+10.49%)</td><td>0.18 <b>(+20.07%)</b></td><td>0.15 (+1.35%)</td><td>0.14 <b>(+105.40%)</b></td><td>0.06 (-13.80%)</td><td>531.50 <b>(-51.31%)</b></td><td>429.06 <b>(-25.62%)</b></td><td>481.90 (-1.33%)</td><td>273.50 (-9.47%)</td><td>108.98 <b>(-64.06%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>1091.60 (n/a)</td><td>576.88 (n/a)</td><td>488.40 (n/a)</td><td>302.10 (n/a)</td><td>303.28 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.26 (-15.53%)</td><td>0.19 (-4.80%)</td><td>0.18 (+10.12%)</td><td>0.10 (-9.22%)</td><td>0.06 <b>(-20.05%)</b></td><td>712.60 (+10.16%)</td><td>430.46 (+2.94%)</td><td>419.00 (-9.19%)</td><td>288.60 (+18.38%)</td><td>173.12 (+5.44%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>646.90 (n/a)</td><td>418.18 (n/a)</td><td>461.40 (n/a)</td><td>243.80 (n/a)</td><td>164.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.73 (+19.74%)</td><td>0.35 (-5.72%)</td><td>0.26 <b>(-43.96%)</b></td><td>0.19 <b>(+247.63%)</b></td><td>0.23 (+1.31%)</td><td>706.00 <b>(-71.23%)</b></td><td>481.94 <b>(-35.91%)</b></td><td>497.90 <b>(+78.46%)</b></td><td>180.70 (-16.46%)</td><td>227.67 <b>(-76.29%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.61 (n/a)</td><td>0.37 (n/a)</td><td>0.47 (n/a)</td><td>0.05 (n/a)</td><td>0.22 (n/a)</td><td>2454.20 (n/a)</td><td>751.96 (n/a)</td><td>279.00 (n/a)</td><td>216.30 (n/a)</td><td>960.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.41 (-4.88%)</td><td>0.32 (+2.06%)</td><td>0.39 <b>(+40.55%)</b></td><td>0.05 <b>(-72.62%)</b></td><td>0.15 <b>(+34.56%)</b></td><td>2478.50 <b>(+265.18%)</b></td><td>768.68 <b>(+65.14%)</b></td><td>334.50 <b>(-28.86%)</b></td><td>319.00 (+5.11%)</td><td>956.11 <b>(+480.28%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>678.70 (n/a)</td><td>465.46 (n/a)</td><td>470.20 (n/a)</td><td>303.50 (n/a)</td><td>164.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.72 <b>(+79.84%)</b></td><td>0.31 (+11.01%)</td><td>0.21 (-16.37%)</td><td>0.16 (-16.34%)</td><td>0.23 <b>(+203.46%)</b></td><td>814.20 (+19.52%)</td><td>562.08 (+12.25%)</td><td>618.40 (+19.59%)</td><td>182.40 <b>(-44.37%)</b></td><td>236.07 <b>(+85.56%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>681.20 (n/a)</td><td>500.74 (n/a)</td><td>517.10 (n/a)</td><td>327.90 (n/a)</td><td>127.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.00 (+0.00%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.94%)</b></td><td>22679.90 (+0.77%)</td><td>17449.61 <b>(+20.64%)</b></td><td>20630.46 (+18.47%)</td><td>7081.85 (+10.97%)</td><td>6585.30 (-12.36%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22505.83 (n/a)</td><td>14463.65 (n/a)</td><td>17413.63 (n/a)</td><td>6381.66 (n/a)</td><td>7513.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.00 <b>(-41.67%)</b></td><td>0.00 <b>(-23.33%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-60.44%)</b></td><td>22543.16 (+7.44%)</td><td>19389.33 (+18.90%)</td><td>21599.96 (+19.21%)</td><td>12152.16 <b>(+78.73%)</b></td><td>4270.66 <b>(-26.95%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20981.17 (n/a)</td><td>16306.88 (n/a)</td><td>18118.56 (n/a)</td><td>6799.03 (n/a)</td><td>5846.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>0.14 (+6.87%)</td><td>0.09 (+9.41%)</td><td>0.09 <b>(+25.27%)</b></td><td>0.07 (-5.83%)</td><td>0.03 (+13.05%)</td><td>30892.46 (+6.17%)</td><td>23920.24 (-7.33%)</td><td>22389.67 <b>(-20.17%)</b></td><td>14984.81 (-6.37%)</td><td>6405.75 (+15.79%)</td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29097.79 (n/a)</td><td>25810.92 (n/a)</td><td>28045.21 (n/a)</td><td>16003.70 (n/a)</td><td>5532.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>2.24 <b>(+38.58%)</b></td><td>1.54 <b>(+86.87%)</b></td><td>1.54 <b>(+106.28%)</b></td><td>0.67 <b>(+337.62%)</b></td><td>0.56 (+4.92%)</td><td>783.50 <b>(-77.15%)</b></td><td>401.74 <b>(-65.66%)</b></td><td>339.90 <b>(-51.52%)</b></td><td>234.30 <b>(-27.82%)</b></td><td>217.84 <b>(-82.96%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>1.61 (n/a)</td><td>0.82 (n/a)</td><td>0.75 (n/a)</td><td>0.15 (n/a)</td><td>0.54 (n/a)</td><td>3429.00 (n/a)</td><td>1169.80 (n/a)</td><td>701.10 (n/a)</td><td>324.60 (n/a)</td><td>1278.65 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>2.76 (+6.13%)</td><td>1.81 (-1.59%)</td><td>1.77 (+3.96%)</td><td>0.30 <b>(-69.33%)</b></td><td>0.97 <b>(+35.08%)</b></td><td>3493.30 <b>(+226.02%)</b></td><td>1102.30 <b>(+68.37%)</b></td><td>593.40 (-3.81%)</td><td>379.50 (-5.76%)</td><td>1341.32 <b>(+380.66%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>2.60 (n/a)</td><td>1.84 (n/a)</td><td>1.70 (n/a)</td><td>0.98 (n/a)</td><td>0.72 (n/a)</td><td>1071.50 (n/a)</td><td>654.68 (n/a)</td><td>616.90 (n/a)</td><td>402.70 (n/a)</td><td>279.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:53:11</td><td>2.58 <b>(+56.46%)</b></td><td>1.52 <b>(+31.65%)</b></td><td>1.45 <b>(+37.76%)</b></td><td>0.76 (+1.42%)</td><td>0.69 <b>(+88.69%)</b></td><td>691.00 (-1.40%)</td><td>408.86 (-17.15%)</td><td>362.10 <b>(-27.42%)</b></td><td>203.40 <b>(-36.08%)</b></td><td>186.83 <b>(+21.30%)</b></td>
</tr>
<tr>
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>1.65 (n/a)</td><td>1.15 (n/a)</td><td>1.05 (n/a)</td><td>0.75 (n/a)</td><td>0.37 (n/a)</td><td>700.80 (n/a)</td><td>493.48 (n/a)</td><td>498.90 (n/a)</td><td>318.20 (n/a)</td><td>154.03 (n/a)</td>
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
