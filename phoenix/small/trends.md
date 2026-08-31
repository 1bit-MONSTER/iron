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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (-18.30%)</td><td>0.04 (+3.73%)</td><td>0.04 <b>(+70.43%)</b></td><td>0.02 (+14.43%)</td><td>0.01 <b>(-49.00%)</b></td><td>537.30 (-12.61%)</td><td>365.40 (-15.73%)</td><td>318.90 <b>(-41.32%)</b></td><td>275.50 <b>(+22.39%)</b></td><td>108.14 <b>(-42.71%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>614.80 (n/a)</td><td>433.62 (n/a)</td><td>543.50 (n/a)</td><td>225.10 (n/a)</td><td>188.75 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (+0.11%)</td><td>0.03 (+7.84%)</td><td>0.03 (+15.76%)</td><td>0.02 (-4.67%)</td><td>0.01 (+7.88%)</td><td>599.70 (+4.90%)</td><td>445.02 (-5.90%)</td><td>451.80 (-13.61%)</td><td>291.00 (-0.10%)</td><td>128.86 (+17.50%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.70 (n/a)</td><td>472.94 (n/a)</td><td>523.00 (n/a)</td><td>291.30 (n/a)</td><td>109.67 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.06 <b>(+84.27%)</b></td><td>0.04 <b>(+75.87%)</b></td><td>0.04 <b>(+93.34%)</b></td><td>0.02 (+7.29%)</td><td>0.02 <b>(+207.73%)</b></td><td>617.70 (-6.79%)</td><td>369.14 <b>(-33.22%)</b></td><td>307.00 <b>(-48.28%)</b></td><td>194.90 <b>(-45.73%)</b></td><td>188.30 <b>(+59.53%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>662.70 (n/a)</td><td>552.74 (n/a)</td><td>593.60 (n/a)</td><td>359.10 (n/a)</td><td>118.03 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 <b>(-27.98%)</b></td><td>0.02 (-12.34%)</td><td>0.02 (-7.33%)</td><td>0.01 (+13.46%)</td><td>0.01 <b>(-29.34%)</b></td><td>674.60 (-11.86%)</td><td>387.84 (+3.66%)</td><td>267.20 (+7.92%)</td><td>263.00 <b>(+38.86%)</b></td><td>183.50 <b>(-22.05%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>765.40 (n/a)</td><td>374.14 (n/a)</td><td>247.60 (n/a)</td><td>189.40 (n/a)</td><td>235.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 <b>(+23.43%)</b></td><td>0.01 (+2.28%)</td><td>0.01 (-6.41%)</td><td>0.01 (+18.91%)</td><td>0.00 <b>(+31.66%)</b></td><td>554.30 (-15.90%)</td><td>445.34 (-1.54%)</td><td>422.60 (+6.85%)</td><td>290.50 (-18.99%)</td><td>107.64 (-11.57%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.10 (n/a)</td><td>452.30 (n/a)</td><td>395.50 (n/a)</td><td>358.60 (n/a)</td><td>121.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (+3.87%)</td><td>0.02 (-10.04%)</td><td>0.02 (-0.31%)</td><td>0.00 <b>(-80.45%)</b></td><td>0.01 <b>(+90.85%)</b></td><td>2472.60 <b>(+411.40%)</b></td><td>730.70 <b>(+122.77%)</b></td><td>285.00 (+0.32%)</td><td>230.90 (-3.71%)</td><td>976.04 <b>(+905.75%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.50 (n/a)</td><td>328.00 (n/a)</td><td>284.10 (n/a)</td><td>239.80 (n/a)</td><td>97.05 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (-0.50%)</td><td>0.02 (-1.69%)</td><td>0.01 (-7.34%)</td><td>0.01 (+15.49%)</td><td>0.01 (+5.06%)</td><td>522.60 (-13.41%)</td><td>383.62 (+1.76%)</td><td>376.50 (+7.94%)</td><td>247.20 (+0.49%)</td><td>136.71 (-6.39%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.50 (n/a)</td><td>376.98 (n/a)</td><td>348.80 (n/a)</td><td>246.00 (n/a)</td><td>146.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (+12.96%)</td><td>0.01 (-15.28%)</td><td>0.01 <b>(-35.23%)</b></td><td>0.01 (-7.99%)</td><td>0.01 (+7.68%)</td><td>630.00 (+8.70%)</td><td>431.48 (+18.07%)</td><td>447.00 <b>(+54.40%)</b></td><td>210.60 (-11.48%)</td><td>148.98 (-2.74%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.60 (n/a)</td><td>365.44 (n/a)</td><td>289.50 (n/a)</td><td>237.90 (n/a)</td><td>153.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 <b>(+45.51%)</b></td><td>0.01 (+14.83%)</td><td>0.01 (-11.32%)</td><td>0.01 <b>(+41.17%)</b></td><td>0.00 <b>(+52.69%)</b></td><td>488.90 <b>(-29.17%)</b></td><td>420.02 (-12.35%)</td><td>468.60 (+12.78%)</td><td>244.90 <b>(-31.27%)</b></td><td>100.64 <b>(-27.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>690.20 (n/a)</td><td>479.22 (n/a)</td><td>415.50 (n/a)</td><td>356.30 (n/a)</td><td>139.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>523.80 (n/a)</td><td>341.16 (n/a)</td><td>305.50 (n/a)</td><td>183.70 (n/a)</td><td>160.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>549.20 (n/a)</td><td>412.70 (n/a)</td><td>421.40 (n/a)</td><td>243.20 (n/a)</td><td>113.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>505.60 (n/a)</td><td>403.70 (n/a)</td><td>379.70 (n/a)</td><td>340.20 (n/a)</td><td>65.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>627.70 (n/a)</td><td>389.30 (n/a)</td><td>303.00 (n/a)</td><td>238.00 (n/a)</td><td>170.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>418.50 (n/a)</td><td>284.74 (n/a)</td><td>258.90 (n/a)</td><td>236.50 (n/a)</td><td>75.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.10 (n/a)</td><td>471.94 (n/a)</td><td>489.90 (n/a)</td><td>272.00 (n/a)</td><td>127.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1934.10 (n/a)</td><td>730.28 (n/a)</td><td>496.90 (n/a)</td><td>249.20 (n/a)</td><td>684.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.50 (n/a)</td><td>443.54 (n/a)</td><td>448.00 (n/a)</td><td>209.20 (n/a)</td><td>161.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.70 (n/a)</td><td>425.82 (n/a)</td><td>497.30 (n/a)</td><td>236.60 (n/a)</td><td>174.97 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.50 (n/a)</td><td>411.70 (n/a)</td><td>465.10 (n/a)</td><td>221.00 (n/a)</td><td>134.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1040.20 (n/a)</td><td>572.96 (n/a)</td><td>445.90 (n/a)</td><td>407.50 (n/a)</td><td>267.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>678.90 (n/a)</td><td>533.94 (n/a)</td><td>504.40 (n/a)</td><td>423.40 (n/a)</td><td>97.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.69 (+6.16%)</td><td>0.39 <b>(-22.24%)</b></td><td>0.33 <b>(-36.54%)</b></td><td>0.30 (-12.01%)</td><td>0.16 <b>(+50.88%)</b></td><td>726.70 (+13.65%)</td><td>617.20 <b>(+35.52%)</b></td><td>675.30 <b>(+57.56%)</b></td><td>322.00 (-5.79%)</td><td>167.08 <b>(+49.93%)</b></td><td>29.31 (+6.16%)</td><td>16.80 <b>(-22.24%)</b></td><td>13.97 <b>(-36.54%)</b></td><td>12.99 (-12.01%)</td><td>7.01 <b>(+50.88%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.65 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>0.35 (n/a)</td><td>0.11 (n/a)</td><td>639.40 (n/a)</td><td>455.44 (n/a)</td><td>428.60 (n/a)</td><td>341.80 (n/a)</td><td>111.43 (n/a)</td><td>27.61 (n/a)</td><td>21.61 (n/a)</td><td>22.02 (n/a)</td><td>14.76 (n/a)</td><td>4.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.53 (+6.10%)</td><td>0.46 (+19.71%)</td><td>0.47 <b>(+25.06%)</b></td><td>0.34 <b>(+67.33%)</b></td><td>0.08 <b>(-37.44%)</b></td><td>643.90 <b>(-40.24%)</b></td><td>492.64 <b>(-22.86%)</b></td><td>474.20 <b>(-20.03%)</b></td><td>416.30 (-5.75%)</td><td>92.27 <b>(-64.49%)</b></td><td>22.67 (+6.10%)</td><td>19.64 (+19.71%)</td><td>19.90 <b>(+25.06%)</b></td><td>14.66 <b>(+67.33%)</b></td><td>3.25 <b>(-37.44%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>1077.40 (n/a)</td><td>638.66 (n/a)</td><td>593.00 (n/a)</td><td>441.70 (n/a)</td><td>259.83 (n/a)</td><td>21.36 (n/a)</td><td>16.41 (n/a)</td><td>15.92 (n/a)</td><td>8.76 (n/a)</td><td>5.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.31 (-0.74%)</td><td>0.30 (-1.31%)</td><td>0.30 (-1.51%)</td><td>0.29 (-2.09%)</td><td>0.01 <b>(+24.16%)</b></td><td>85569.90 (+2.13%)</td><td>83085.36 (+1.34%)</td><td>82863.00 (+1.53%)</td><td>80906.70 (+0.75%)</td><td>1820.16 <b>(+27.67%)</b></td><td>212.34 (-0.74%)</td><td>206.85 (-1.31%)</td><td>207.33 (-1.51%)</td><td>200.77 (-2.09%)</td><td>4.51 <b>(+24.16%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>83783.80 (n/a)</td><td>81983.54 (n/a)</td><td>81611.20 (n/a)</td><td>80305.80 (n/a)</td><td>1425.64 (n/a)</td><td>213.93 (n/a)</td><td>209.60 (n/a)</td><td>210.51 (n/a)</td><td>205.05 (n/a)</td><td>3.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>1.04 (+0.80%)</td><td>1.02 (+0.35%)</td><td>1.02 (+0.68%)</td><td>0.99 (-0.88%)</td><td>0.02 <b>(+50.57%)</b></td><td>25380.20 (+0.89%)</td><td>24764.18 (-0.33%)</td><td>24691.80 (-0.67%)</td><td>24176.40 (-0.79%)</td><td>449.22 <b>(+51.02%)</b></td><td>710.61 (+0.80%)</td><td>693.92 (+0.35%)</td><td>695.77 (+0.68%)</td><td>676.90 (-0.88%)</td><td>12.57 <b>(+50.57%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25155.80 (n/a)</td><td>24846.00 (n/a)</td><td>24858.90 (n/a)</td><td>24369.90 (n/a)</td><td>297.47 (n/a)</td><td>704.96 (n/a)</td><td>691.53 (n/a)</td><td>691.09 (n/a)</td><td>682.94 (n/a)</td><td>8.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>3.74 (-0.97%)</td><td>2.49 (+15.30%)</td><td>2.12 (+14.63%)</td><td>1.32 (-12.99%)</td><td>1.02 (+10.60%)</td><td>6101.60 (+14.94%)</td><td>3734.00 (-9.69%)</td><td>3796.00 (-12.76%)</td><td>2153.60 (+0.98%)</td><td>1589.10 <b>(+31.79%)</b></td><td>981.56 (-0.97%)</td><td>653.07 (+15.30%)</td><td>556.88 (+14.63%)</td><td>346.46 (-12.99%)</td><td>266.92 (+10.60%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>3.78 (n/a)</td><td>2.16 (n/a)</td><td>1.85 (n/a)</td><td>1.52 (n/a)</td><td>0.92 (n/a)</td><td>5308.70 (n/a)</td><td>4134.84 (n/a)</td><td>4351.30 (n/a)</td><td>2132.70 (n/a)</td><td>1205.81 (n/a)</td><td>991.18 (n/a)</td><td>566.40 (n/a)</td><td>485.82 (n/a)</td><td>398.20 (n/a)</td><td>241.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.20 <b>(-29.02%)</b></td><td>0.18 (-14.13%)</td><td>0.19 (-11.82%)</td><td>0.17 (-0.66%)</td><td>0.01 <b>(-74.48%)</b></td><td>7336.20 (+0.67%)</td><td>6811.00 (+13.47%)</td><td>6724.90 (+13.40%)</td><td>6383.60 <b>(+40.88%)</b></td><td>397.33 <b>(-63.97%)</b></td><td>10.51 <b>(-29.02%)</b></td><td>9.88 (-14.13%)</td><td>9.98 (-11.82%)</td><td>9.15 (-0.66%)</td><td>0.57 <b>(-74.48%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>7287.50 (n/a)</td><td>6002.22 (n/a)</td><td>5930.00 (n/a)</td><td>4531.10 (n/a)</td><td>1102.87 (n/a)</td><td>14.81 (n/a)</td><td>11.51 (n/a)</td><td>11.32 (n/a)</td><td>9.21 (n/a)</td><td>2.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>3.63 (n/a)</td><td>3.54 (n/a)</td><td>3.58 (n/a)</td><td>3.34 (n/a)</td><td>0.12 (n/a)</td><td>3.63 (n/a)</td><td>3.54 (n/a)</td><td>3.58 (n/a)</td><td>3.34 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>7.57 (+5.56%)</td><td>6.35 (+1.82%)</td><td>5.97 (+0.94%)</td><td>5.69 (+3.90%)</td><td>0.81 (+11.61%)</td><td>7.57 (+5.56%)</td><td>6.35 (+1.82%)</td><td>5.96 (+0.94%)</td><td>5.69 (+3.90%)</td><td>0.81 (+11.61%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>7.17 (n/a)</td><td>6.24 (n/a)</td><td>5.91 (n/a)</td><td>5.48 (n/a)</td><td>0.72 (n/a)</td><td>7.17 (n/a)</td><td>6.23 (n/a)</td><td>5.91 (n/a)</td><td>5.47 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>10.84 (+9.69%)</td><td>8.91 (+10.76%)</td><td>8.61 (+7.01%)</td><td>7.42 (+8.92%)</td><td>1.27 (+9.41%)</td><td>10.83 (+9.69%)</td><td>8.90 (+10.76%)</td><td>8.60 (+7.01%)</td><td>7.42 (+8.92%)</td><td>1.27 (+9.41%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>9.88 (n/a)</td><td>8.04 (n/a)</td><td>8.04 (n/a)</td><td>6.81 (n/a)</td><td>1.16 (n/a)</td><td>9.87 (n/a)</td><td>8.04 (n/a)</td><td>8.04 (n/a)</td><td>6.81 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>3.83 (n/a)</td><td>3.61 (n/a)</td><td>3.77 (n/a)</td><td>3.09 (n/a)</td><td>0.30 (n/a)</td><td>3.82 (n/a)</td><td>3.61 (n/a)</td><td>3.76 (n/a)</td><td>3.09 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>7.70 (+1.50%)</td><td>6.24 (+2.64%)</td><td>6.00 (+3.37%)</td><td>4.81 (+0.20%)</td><td>1.09 (-10.53%)</td><td>7.69 (+1.50%)</td><td>6.23 (+2.64%)</td><td>6.00 (+3.37%)</td><td>4.81 (+0.20%)</td><td>1.09 (-10.53%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>7.58 (n/a)</td><td>6.07 (n/a)</td><td>5.81 (n/a)</td><td>4.80 (n/a)</td><td>1.21 (n/a)</td><td>7.58 (n/a)</td><td>6.07 (n/a)</td><td>5.81 (n/a)</td><td>4.80 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>13.99 (+4.47%)</td><td>10.03 (+0.85%)</td><td>9.47 (-2.07%)</td><td>7.92 (-4.86%)</td><td>2.31 (+12.24%)</td><td>13.98 (+4.47%)</td><td>10.02 (+0.85%)</td><td>9.47 (-2.07%)</td><td>7.92 (-4.86%)</td><td>2.31 (+12.24%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>13.39 (n/a)</td><td>9.94 (n/a)</td><td>9.67 (n/a)</td><td>8.33 (n/a)</td><td>2.06 (n/a)</td><td>13.38 (n/a)</td><td>9.94 (n/a)</td><td>9.67 (n/a)</td><td>8.32 (n/a)</td><td>2.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>2.96 (+4.08%)</td><td>1.99 (-5.30%)</td><td>2.23 (+0.37%)</td><td>1.05 (+3.87%)</td><td>0.87 (+13.99%)</td><td>2.95 (+4.08%)</td><td>1.98 (-5.30%)</td><td>2.23 (+0.37%)</td><td>1.05 (+3.87%)</td><td>0.87 (+13.99%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>2.84 (n/a)</td><td>2.10 (n/a)</td><td>2.22 (n/a)</td><td>1.01 (n/a)</td><td>0.77 (n/a)</td><td>2.84 (n/a)</td><td>2.09 (n/a)</td><td>2.22 (n/a)</td><td>1.01 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.52 (+10.27%)</td><td>0.31 <b>(-22.58%)</b></td><td>0.38 (-7.48%)</td><td>0.11 <b>(-65.98%)</b></td><td>0.17 <b>(+208.73%)</b></td><td>0.51 (+10.27%)</td><td>0.31 <b>(-22.58%)</b></td><td>0.37 (-7.48%)</td><td>0.11 <b>(-65.98%)</b></td><td>0.17 <b>(+208.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.62 <b>(-20.25%)</b></td><td>0.38 <b>(-32.96%)</b></td><td>0.45 <b>(-27.02%)</b></td><td>0.13 <b>(-66.48%)</b></td><td>0.23 <b>(+43.79%)</b></td><td>0.61 <b>(-20.25%)</b></td><td>0.38 <b>(-32.96%)</b></td><td>0.44 <b>(-27.02%)</b></td><td>0.13 <b>(-66.48%)</b></td><td>0.23 <b>(+43.79%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.78 (n/a)</td><td>0.57 (n/a)</td><td>0.61 (n/a)</td><td>0.38 (n/a)</td><td>0.16 (n/a)</td><td>0.77 (n/a)</td><td>0.56 (n/a)</td><td>0.61 (n/a)</td><td>0.37 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>2.39 (+19.14%)</td><td>1.86 <b>(+44.50%)</b></td><td>2.34 <b>(+53.56%)</b></td><td>0.45 (+0.76%)</td><td>0.83 (+5.43%)</td><td>2.35 (+19.14%)</td><td>1.83 <b>(+44.50%)</b></td><td>2.30 <b>(+53.56%)</b></td><td>0.44 (+0.76%)</td><td>0.82 (+5.43%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>2.01 (n/a)</td><td>1.29 (n/a)</td><td>1.52 (n/a)</td><td>0.44 (n/a)</td><td>0.79 (n/a)</td><td>1.97 (n/a)</td><td>1.26 (n/a)</td><td>1.50 (n/a)</td><td>0.44 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.60 (n/a)</td><td>433.36 (n/a)</td><td>545.90 (n/a)</td><td>250.30 (n/a)</td><td>163.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.70 (n/a)</td><td>459.68 (n/a)</td><td>439.40 (n/a)</td><td>286.30 (n/a)</td><td>135.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.40 (n/a)</td><td>379.94 (n/a)</td><td>407.90 (n/a)</td><td>237.70 (n/a)</td><td>144.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.50 (n/a)</td><td>425.00 (n/a)</td><td>407.70 (n/a)</td><td>286.00 (n/a)</td><td>109.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>429.26 (n/a)</td><td>473.40 (n/a)</td><td>240.00 (n/a)</td><td>128.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>501.50 (n/a)</td><td>418.74 (n/a)</td><td>396.20 (n/a)</td><td>323.60 (n/a)</td><td>77.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (+14.16%)</td><td>0.02 (+4.90%)</td><td>0.02 (-13.60%)</td><td>0.02 (+0.74%)</td><td>0.01 <b>(+22.94%)</b></td><td>522.20 (-0.74%)</td><td>383.94 (-3.22%)</td><td>412.80 (+15.73%)</td><td>247.60 (-12.42%)</td><td>117.43 (+0.90%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.10 (n/a)</td><td>396.72 (n/a)</td><td>356.70 (n/a)</td><td>282.70 (n/a)</td><td>116.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (+8.00%)</td><td>0.03 (+10.61%)</td><td>0.03 (+13.80%)</td><td>0.02 (+13.44%)</td><td>0.01 (-12.57%)</td><td>473.70 (-11.84%)</td><td>327.48 (-11.48%)</td><td>306.80 (-12.14%)</td><td>248.90 (-7.40%)</td><td>85.57 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>369.94 (n/a)</td><td>349.20 (n/a)</td><td>268.80 (n/a)</td><td>110.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 <b>(+31.28%)</b></td><td>0.02 (-0.63%)</td><td>0.02 <b>(-23.28%)</b></td><td>0.02 (-8.78%)</td><td>0.01 <b>(+71.99%)</b></td><td>503.10 (+9.61%)</td><td>367.86 (+6.29%)</td><td>380.60 <b>(+30.34%)</b></td><td>219.90 <b>(-23.80%)</b></td><td>117.46 <b>(+48.49%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.00 (n/a)</td><td>346.08 (n/a)</td><td>292.00 (n/a)</td><td>288.60 (n/a)</td><td>79.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.05 <b>(+41.47%)</b></td><td>0.02 (-10.33%)</td><td>0.02 <b>(-35.14%)</b></td><td>0.01 <b>(-33.22%)</b></td><td>0.01 <b>(+89.20%)</b></td><td>780.90 <b>(+49.77%)</b></td><td>484.52 <b>(+33.02%)</b></td><td>530.70 <b>(+54.18%)</b></td><td>178.00 <b>(-29.31%)</b></td><td>230.19 <b>(+96.22%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>364.24 (n/a)</td><td>344.20 (n/a)</td><td>251.80 (n/a)</td><td>117.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 <b>(+25.32%)</b></td><td>0.03 (+14.22%)</td><td>0.03 <b>(+46.68%)</b></td><td>0.01 (+8.26%)</td><td>0.01 <b>(+26.52%)</b></td><td>549.00 (-7.62%)</td><td>363.36 (-9.05%)</td><td>304.90 <b>(-31.82%)</b></td><td>184.10 <b>(-20.20%)</b></td><td>162.75 (+5.92%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.30 (n/a)</td><td>399.50 (n/a)</td><td>447.20 (n/a)</td><td>230.70 (n/a)</td><td>153.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 <b>(-36.32%)</b></td><td>0.02 <b>(-23.11%)</b></td><td>0.02 (-6.98%)</td><td>0.02 (+10.72%)</td><td>0.00 <b>(-72.53%)</b></td><td>541.30 (-9.68%)</td><td>468.48 (+14.59%)</td><td>476.00 (+7.50%)</td><td>371.10 <b>(+57.05%)</b></td><td>66.57 <b>(-58.92%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.30 (n/a)</td><td>408.82 (n/a)</td><td>442.80 (n/a)</td><td>236.30 (n/a)</td><td>162.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (-12.44%)</td><td>0.02 (+12.76%)</td><td>0.02 (+14.84%)</td><td>0.01 (+1.26%)</td><td>0.01 (-11.60%)</td><td>557.80 (-1.26%)</td><td>410.14 (-12.27%)</td><td>439.40 (-12.90%)</td><td>244.10 (+14.23%)</td><td>150.23 (+3.84%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.90 (n/a)</td><td>467.50 (n/a)</td><td>504.50 (n/a)</td><td>213.70 (n/a)</td><td>144.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 <b>(+37.88%)</b></td><td>0.02 <b>(+22.58%)</b></td><td>0.02 <b>(+30.51%)</b></td><td>0.01 (+2.46%)</td><td>0.01 <b>(+101.89%)</b></td><td>587.50 (-2.41%)</td><td>441.76 (-13.79%)</td><td>403.60 <b>(-23.37%)</b></td><td>277.00 <b>(-27.49%)</b></td><td>139.52 <b>(+50.54%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.00 (n/a)</td><td>512.42 (n/a)</td><td>526.70 (n/a)</td><td>382.00 (n/a)</td><td>92.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (-17.84%)</td><td>0.02 <b>(-23.63%)</b></td><td>0.03 (-9.30%)</td><td>0.01 <b>(-52.14%)</b></td><td>0.01 <b>(+95.10%)</b></td><td>623.30 <b>(+108.95%)</b></td><td>392.66 <b>(+45.27%)</b></td><td>297.60 (+10.26%)</td><td>264.80 <b>(+21.69%)</b></td><td>159.50 <b>(+391.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>298.30 (n/a)</td><td>270.30 (n/a)</td><td>269.90 (n/a)</td><td>217.60 (n/a)</td><td>32.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (-15.67%)</td><td>0.02 (-18.35%)</td><td>0.02 (-16.92%)</td><td>0.01 (-3.89%)</td><td>0.01 <b>(-23.65%)</b></td><td>764.70 (+4.05%)</td><td>506.50 (+16.71%)</td><td>509.90 <b>(+20.34%)</b></td><td>264.90 (+18.58%)</td><td>177.28 (-9.96%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>734.90 (n/a)</td><td>434.00 (n/a)</td><td>423.70 (n/a)</td><td>223.40 (n/a)</td><td>196.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (+3.31%)</td><td>0.02 (+2.69%)</td><td>0.03 <b>(+42.39%)</b></td><td>0.01 <b>(-25.09%)</b></td><td>0.01 <b>(+26.45%)</b></td><td>608.70 <b>(+33.49%)</b></td><td>391.10 (+2.93%)</td><td>308.10 <b>(-29.79%)</b></td><td>252.40 (-3.18%)</td><td>154.22 <b>(+61.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>456.00 (n/a)</td><td>379.96 (n/a)</td><td>438.80 (n/a)</td><td>260.70 (n/a)</td><td>95.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (-1.27%)</td><td>0.02 <b>(+31.99%)</b></td><td>0.02 (+17.68%)</td><td>0.01 <b>(+57.72%)</b></td><td>0.01 (-3.56%)</td><td>631.00 <b>(-36.60%)</b></td><td>432.48 <b>(-29.07%)</b></td><td>506.70 (-15.03%)</td><td>231.80 (+1.31%)</td><td>178.04 <b>(-34.83%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>995.20 (n/a)</td><td>609.72 (n/a)</td><td>596.30 (n/a)</td><td>228.80 (n/a)</td><td>273.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 <b>(+26.17%)</b></td><td>0.03 <b>(+65.72%)</b></td><td>0.03 <b>(+90.76%)</b></td><td>0.02 <b>(+246.36%)</b></td><td>0.01 (+14.44%)</td><td>529.50 <b>(-71.13%)</b></td><td>359.72 <b>(-51.98%)</b></td><td>285.10 <b>(-47.58%)</b></td><td>225.50 <b>(-20.74%)</b></td><td>151.25 <b>(-75.49%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1833.90 (n/a)</td><td>749.06 (n/a)</td><td>543.90 (n/a)</td><td>284.50 (n/a)</td><td>617.00 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 <b>(+44.11%)</b></td><td>0.02 <b>(+23.38%)</b></td><td>0.01 (-5.56%)</td><td>0.01 <b>(+83.93%)</b></td><td>0.01 <b>(+41.43%)</b></td><td>679.30 <b>(-45.63%)</b></td><td>476.28 <b>(-22.44%)</b></td><td>566.40 (+5.89%)</td><td>250.10 <b>(-30.60%)</b></td><td>188.11 <b>(-48.60%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1249.50 (n/a)</td><td>614.10 (n/a)</td><td>534.90 (n/a)</td><td>360.40 (n/a)</td><td>365.95 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/repeat</summary>


### test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]

_No metrics available._


### test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.09 (+4.11%)</td><td>0.09 <b>(+26.21%)</b></td><td>0.09 (+10.34%)</td><td>0.09 <b>(+95.05%)</b></td><td>0.00 <b>(-93.22%)</b></td><td>273.80 <b>(-48.74%)</b></td><td>269.48 <b>(-26.65%)</b></td><td>268.60 (-9.38%)</td><td>263.60 (-3.94%)</td><td>4.11 <b>(-96.57%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>534.10 (n/a)</td><td>367.38 (n/a)</td><td>296.40 (n/a)</td><td>274.40 (n/a)</td><td>119.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.17 (-7.12%)</td><td>0.12 (-7.63%)</td><td>0.10 <b>(-36.42%)</b></td><td>0.08 (+13.81%)</td><td>0.04 <b>(-23.63%)</b></td><td>500.90 (-12.14%)</td><td>367.84 (+0.14%)</td><td>405.10 <b>(+57.26%)</b></td><td>241.90 (+7.65%)</td><td>114.74 <b>(-33.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>570.10 (n/a)</td><td>367.34 (n/a)</td><td>257.60 (n/a)</td><td>224.70 (n/a)</td><td>172.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (-2.00%)</td><td>0.01 (+6.55%)</td><td>0.02 (+17.70%)</td><td>0.01 (+10.64%)</td><td>0.00 (-5.41%)</td><td>518.70 (-9.62%)</td><td>379.24 (-7.09%)</td><td>333.90 (-15.04%)</td><td>278.40 (+2.05%)</td><td>104.98 (-11.82%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.90 (n/a)</td><td>408.20 (n/a)</td><td>393.00 (n/a)</td><td>272.80 (n/a)</td><td>119.05 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (+9.76%)</td><td>0.03 <b>(+22.48%)</b></td><td>0.03 (+14.39%)</td><td>0.01 (+12.49%)</td><td>0.01 (-3.06%)</td><td>552.00 (-11.10%)</td><td>308.98 <b>(-20.24%)</b></td><td>252.70 (-12.59%)</td><td>228.00 (-8.91%)</td><td>136.71 (-16.86%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.90 (n/a)</td><td>387.38 (n/a)</td><td>289.10 (n/a)</td><td>250.30 (n/a)</td><td>164.44 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.06 (+9.19%)</td><td>0.04 (+9.17%)</td><td>0.03 (-3.31%)</td><td>0.02 (+18.26%)</td><td>0.02 (+5.33%)</td><td>493.70 (-15.43%)</td><td>349.44 (-10.19%)</td><td>389.40 (+3.43%)</td><td>205.00 (-8.44%)</td><td>126.73 (-19.88%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>583.80 (n/a)</td><td>389.08 (n/a)</td><td>376.50 (n/a)</td><td>223.90 (n/a)</td><td>158.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (+16.48%)</td><td>0.03 <b>(+30.69%)</b></td><td>0.03 <b>(+64.39%)</b></td><td>0.02 (+3.91%)</td><td>0.01 <b>(+30.32%)</b></td><td>528.00 (-3.77%)</td><td>342.08 <b>(-21.28%)</b></td><td>293.70 <b>(-39.17%)</b></td><td>219.80 (-14.14%)</td><td>134.12 (+3.41%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.70 (n/a)</td><td>434.58 (n/a)</td><td>482.80 (n/a)</td><td>256.00 (n/a)</td><td>129.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (+6.71%)</td><td>0.03 (+9.54%)</td><td>0.04 <b>(+65.01%)</b></td><td>0.01 <b>(-49.11%)</b></td><td>0.02 <b>(+70.00%)</b></td><td>1008.00 <b>(+96.49%)</b></td><td>464.78 (+17.19%)</td><td>270.10 <b>(-39.40%)</b></td><td>235.10 (-6.30%)</td><td>335.65 <b>(+191.61%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.00 (n/a)</td><td>396.62 (n/a)</td><td>445.70 (n/a)</td><td>250.90 (n/a)</td><td>115.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (+6.83%)</td><td>0.03 (-11.73%)</td><td>0.03 (+4.20%)</td><td>0.00 <b>(-80.72%)</b></td><td>0.01 <b>(+106.53%)</b></td><td>2471.30 <b>(+418.53%)</b></td><td>726.16 <b>(+136.00%)</b></td><td>270.30 (-4.01%)</td><td>217.40 (-6.37%)</td><td>979.47 <b>(+906.65%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.60 (n/a)</td><td>307.70 (n/a)</td><td>281.60 (n/a)</td><td>232.20 (n/a)</td><td>97.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 <b>(-28.25%)</b></td><td>0.03 (+4.15%)</td><td>0.02 (+0.76%)</td><td>0.02 <b>(+254.09%)</b></td><td>0.01 <b>(-50.89%)</b></td><td>530.20 <b>(-71.76%)</b></td><td>389.28 <b>(-43.47%)</b></td><td>440.10 (-0.74%)</td><td>247.10 <b>(+39.37%)</b></td><td>123.30 <b>(-82.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1877.40 (n/a)</td><td>688.66 (n/a)</td><td>443.40 (n/a)</td><td>177.30 (n/a)</td><td>689.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (-1.80%)</td><td>0.02 (-16.22%)</td><td>0.02 (-6.74%)</td><td>0.00 <b>(-65.13%)</b></td><td>0.01 <b>(+22.84%)</b></td><td>1800.50 <b>(+186.80%)</b></td><td>688.68 <b>(+64.50%)</b></td><td>491.40 (+7.25%)</td><td>249.00 (+1.80%)</td><td>632.45 <b>(+309.75%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.80 (n/a)</td><td>418.66 (n/a)</td><td>458.20 (n/a)</td><td>244.60 (n/a)</td><td>154.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (-0.63%)</td><td>0.02 (-10.59%)</td><td>0.02 <b>(-24.74%)</b></td><td>0.02 (+0.83%)</td><td>0.01 (-8.92%)</td><td>559.30 (-0.83%)</td><td>418.58 (+8.48%)</td><td>418.00 <b>(+32.87%)</b></td><td>233.40 (+0.65%)</td><td>121.54 (-18.71%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.00 (n/a)</td><td>385.86 (n/a)</td><td>314.60 (n/a)</td><td>231.90 (n/a)</td><td>149.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 <b>(-25.06%)</b></td><td>0.02 <b>(-26.04%)</b></td><td>0.02 (-12.28%)</td><td>0.01 <b>(-38.64%)</b></td><td>0.01 <b>(-22.66%)</b></td><td>887.40 <b>(+62.98%)</b></td><td>538.62 <b>(+38.95%)</b></td><td>479.60 (+14.00%)</td><td>316.10 <b>(+33.43%)</b></td><td>218.98 <b>(+76.02%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.50 (n/a)</td><td>387.64 (n/a)</td><td>420.70 (n/a)</td><td>236.90 (n/a)</td><td>124.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (-0.96%)</td><td>0.02 (-9.40%)</td><td>0.02 <b>(-27.46%)</b></td><td>0.02 (+8.58%)</td><td>0.01 (-15.79%)</td><td>528.40 (-7.90%)</td><td>407.52 (+5.01%)</td><td>424.30 <b>(+37.89%)</b></td><td>237.60 (+0.98%)</td><td>106.01 <b>(-31.05%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>573.70 (n/a)</td><td>388.06 (n/a)</td><td>307.70 (n/a)</td><td>235.30 (n/a)</td><td>153.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (+7.08%)</td><td>0.02 (+5.52%)</td><td>0.03 <b>(+48.94%)</b></td><td>0.00 <b>(-59.12%)</b></td><td>0.01 <b>(+51.16%)</b></td><td>1652.90 <b>(+144.58%)</b></td><td>612.22 <b>(+39.27%)</b></td><td>289.10 <b>(-32.86%)</b></td><td>229.70 (-6.63%)</td><td>599.70 <b>(+259.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.80 (n/a)</td><td>439.58 (n/a)</td><td>430.60 (n/a)</td><td>246.00 (n/a)</td><td>166.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.35 (-4.65%)</td><td>0.25 (+2.68%)</td><td>0.19 (+5.84%)</td><td>0.18 (+16.43%)</td><td>0.09 (-18.04%)</td><td>545.80 (-14.11%)</td><td>436.72 (-7.65%)</td><td>522.60 (-5.51%)</td><td>279.90 (+4.87%)</td><td>135.83 <b>(-25.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>635.50 (n/a)</td><td>472.88 (n/a)</td><td>553.10 (n/a)</td><td>266.90 (n/a)</td><td>181.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.33 (-13.55%)</td><td>0.16 <b>(-47.88%)</b></td><td>0.17 <b>(-46.62%)</b></td><td>0.04 <b>(-81.93%)</b></td><td>0.12 <b>(+89.46%)</b></td><td>2421.90 <b>(+453.45%)</b></td><td>1107.32 <b>(+239.86%)</b></td><td>569.60 <b>(+87.37%)</b></td><td>297.20 (+15.69%)</td><td>945.06 <b>(+1197.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>437.60 (n/a)</td><td>325.82 (n/a)</td><td>304.00 (n/a)</td><td>256.90 (n/a)</td><td>72.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.37 (-7.02%)</td><td>0.25 <b>(-23.39%)</b></td><td>0.24 <b>(-37.34%)</b></td><td>0.16 <b>(-22.58%)</b></td><td>0.08 (-13.97%)</td><td>612.20 <b>(+29.18%)</b></td><td>433.20 <b>(+30.68%)</b></td><td>408.10 <b>(+59.60%)</b></td><td>262.60 (+7.53%)</td><td>137.04 <b>(+21.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.38 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>473.90 (n/a)</td><td>331.50 (n/a)</td><td>255.70 (n/a)</td><td>244.20 (n/a)</td><td>112.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.32 (-10.50%)</td><td>0.23 (-8.46%)</td><td>0.24 (-8.48%)</td><td>0.16 (+1.10%)</td><td>0.07 <b>(-23.24%)</b></td><td>469.90 (-1.09%)</td><td>351.72 (+5.09%)</td><td>311.30 (+9.27%)</td><td>229.10 (+11.76%)</td><td>104.67 (-16.46%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>475.10 (n/a)</td><td>334.68 (n/a)</td><td>284.90 (n/a)</td><td>205.00 (n/a)</td><td>125.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.28 (-2.86%)</td><td>0.20 (-8.42%)</td><td>0.16 <b>(-30.48%)</b></td><td>0.13 (-4.13%)</td><td>0.08 (+5.70%)</td><td>568.80 (+4.33%)</td><td>420.60 (+10.70%)</td><td>459.80 <b>(+43.82%)</b></td><td>259.00 (+2.94%)</td><td>151.18 (+7.33%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>545.20 (n/a)</td><td>379.96 (n/a)</td><td>319.70 (n/a)</td><td>251.60 (n/a)</td><td>140.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.36 (+19.14%)</td><td>0.19 <b>(-20.29%)</b></td><td>0.15 <b>(-43.20%)</b></td><td>0.12 <b>(-25.34%)</b></td><td>0.10 <b>(+58.50%)</b></td><td>591.00 <b>(+33.95%)</b></td><td>445.38 <b>(+35.99%)</b></td><td>478.70 <b>(+76.06%)</b></td><td>203.30 (-16.06%)</td><td>145.38 <b>(+59.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>441.20 (n/a)</td><td>327.50 (n/a)</td><td>271.90 (n/a)</td><td>242.20 (n/a)</td><td>91.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.40 (-16.64%)</td><td>0.25 <b>(-32.10%)</b></td><td>0.23 <b>(-39.57%)</b></td><td>0.17 (-12.65%)</td><td>0.09 (-18.34%)</td><td>775.00 (+14.48%)</td><td>562.68 <b>(+44.48%)</b></td><td>569.50 <b>(+65.50%)</b></td><td>327.90 (+19.98%)</td><td>163.01 (-0.27%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>677.00 (n/a)</td><td>389.46 (n/a)</td><td>344.10 (n/a)</td><td>273.30 (n/a)</td><td>163.46 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.31 <b>(-37.30%)</b></td><td>0.21 <b>(-39.60%)</b></td><td>0.19 <b>(-40.97%)</b></td><td>0.10 <b>(-51.23%)</b></td><td>0.08 <b>(-35.44%)</b></td><td>1300.20 <b>(+105.05%)</b></td><td>726.98 <b>(+71.98%)</b></td><td>676.20 <b>(+69.39%)</b></td><td>420.30 <b>(+59.51%)</b></td><td>349.42 <b>(+117.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>634.10 (n/a)</td><td>422.70 (n/a)</td><td>399.20 (n/a)</td><td>263.50 (n/a)</td><td>160.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.38 <b>(-25.43%)</b></td><td>0.27 (-9.33%)</td><td>0.27 (-8.93%)</td><td>0.08 (+16.03%)</td><td>0.12 <b>(-29.83%)</b></td><td>1617.80 (-13.81%)</td><td>666.54 (-5.61%)</td><td>477.90 (+9.81%)</td><td>344.90 <b>(+34.10%)</b></td><td>536.92 (-19.71%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.51 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>1877.10 (n/a)</td><td>706.14 (n/a)</td><td>435.20 (n/a)</td><td>257.20 (n/a)</td><td>668.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (+14.72%)</td><td>0.01 (+17.45%)</td><td>0.01 <b>(+45.74%)</b></td><td>0.01 (+2.99%)</td><td>0.00 (+17.39%)</td><td>554.10 (-2.91%)</td><td>364.62 (-13.65%)</td><td>297.90 <b>(-31.38%)</b></td><td>235.10 (-12.86%)</td><td>130.23 (+1.84%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.70 (n/a)</td><td>422.28 (n/a)</td><td>434.10 (n/a)</td><td>269.80 (n/a)</td><td>127.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (+10.85%)</td><td>0.01 (-10.21%)</td><td>0.01 (+2.77%)</td><td>0.00 <b>(-75.45%)</b></td><td>0.01 <b>(+71.99%)</b></td><td>1893.30 <b>(+307.34%)</b></td><td>639.28 <b>(+85.71%)</b></td><td>289.70 (-2.69%)</td><td>221.70 (-9.80%)</td><td>710.18 <b>(+556.35%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.80 (n/a)</td><td>344.24 (n/a)</td><td>297.70 (n/a)</td><td>245.80 (n/a)</td><td>108.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (-5.04%)</td><td>0.01 <b>(+29.17%)</b></td><td>0.01 <b>(+74.40%)</b></td><td>0.01 (+8.69%)</td><td>0.01 (-0.98%)</td><td>543.60 (-8.00%)</td><td>355.68 <b>(-22.31%)</b></td><td>278.60 <b>(-42.66%)</b></td><td>215.40 (+5.28%)</td><td>159.81 (+1.47%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>457.84 (n/a)</td><td>485.90 (n/a)</td><td>204.60 (n/a)</td><td>157.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.55 (-18.07%)</td><td>0.46 (+7.20%)</td><td>0.50 (+18.75%)</td><td>0.23 (-4.66%)</td><td>0.14 <b>(-29.83%)</b></td><td>585.80 (+4.91%)</td><td>321.64 (-12.30%)</td><td>263.90 (-15.79%)</td><td>239.80 <b>(+22.04%)</b></td><td>148.57 (-12.08%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.67 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>558.40 (n/a)</td><td>366.76 (n/a)</td><td>313.40 (n/a)</td><td>196.50 (n/a)</td><td>168.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.60 <b>(+22.67%)</b></td><td>0.53 <b>(+59.74%)</b></td><td>0.52 <b>(+29.26%)</b></td><td>0.46 <b>(+571.69%)</b></td><td>0.05 <b>(-69.86%)</b></td><td>288.80 <b>(-85.11%)</b></td><td>253.14 <b>(-62.57%)</b></td><td>255.10 <b>(-22.65%)</b></td><td>219.30 (-18.48%)</td><td>25.00 <b>(-96.50%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>1939.80 (n/a)</td><td>676.28 (n/a)</td><td>329.80 (n/a)</td><td>269.00 (n/a)</td><td>714.69 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.43 <b>(-21.87%)</b></td><td>0.31 (-17.75%)</td><td>0.30 (-9.60%)</td><td>0.26 (+5.84%)</td><td>0.07 <b>(-51.09%)</b></td><td>505.80 (-5.53%)</td><td>436.48 (+13.34%)</td><td>445.90 (+10.62%)</td><td>310.00 <b>(+27.99%)</b></td><td>77.47 <b>(-40.48%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>535.40 (n/a)</td><td>385.10 (n/a)</td><td>403.10 (n/a)</td><td>242.20 (n/a)</td><td>130.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.47 (-17.78%)</td><td>0.33 <b>(-21.91%)</b></td><td>0.25 <b>(-49.37%)</b></td><td>0.24 (-4.71%)</td><td>0.12 (-11.49%)</td><td>543.20 (+4.95%)</td><td>435.82 <b>(+28.14%)</b></td><td>527.10 <b>(+97.49%)</b></td><td>279.20 <b>(+21.66%)</b></td><td>139.73 (+12.19%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.49 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>517.60 (n/a)</td><td>340.12 (n/a)</td><td>266.90 (n/a)</td><td>229.50 (n/a)</td><td>124.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.62 <b>(-29.16%)</b></td><td>0.45 (-8.58%)</td><td>0.42 (-10.98%)</td><td>0.34 <b>(+39.07%)</b></td><td>0.11 <b>(-54.91%)</b></td><td>384.60 <b>(-28.10%)</b></td><td>304.84 (-4.84%)</td><td>314.00 (+12.34%)</td><td>214.00 <b>(+41.16%)</b></td><td>67.01 <b>(-54.76%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.87 (n/a)</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>534.90 (n/a)</td><td>320.34 (n/a)</td><td>279.50 (n/a)</td><td>151.60 (n/a)</td><td>148.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (+18.25%)</td><td>0.01 (+2.29%)</td><td>0.01 (-1.26%)</td><td>0.01 <b>(+43.83%)</b></td><td>0.01 (-0.38%)</td><td>728.90 <b>(-30.47%)</b></td><td>411.80 (-11.90%)</td><td>296.30 (+1.26%)</td><td>201.60 (-15.44%)</td><td>217.07 <b>(-36.92%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1048.30 (n/a)</td><td>467.44 (n/a)</td><td>292.60 (n/a)</td><td>238.40 (n/a)</td><td>344.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 <b>(-38.14%)</b></td><td>0.01 (-8.63%)</td><td>0.01 (+1.10%)</td><td>0.01 <b>(+22.93%)</b></td><td>0.00 <b>(-55.13%)</b></td><td>525.30 (-18.65%)</td><td>361.68 (-8.56%)</td><td>292.80 (-1.08%)</td><td>258.40 <b>(+61.70%)</b></td><td>116.12 <b>(-44.31%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.70 (n/a)</td><td>395.52 (n/a)</td><td>296.00 (n/a)</td><td>159.80 (n/a)</td><td>208.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 <b>(+20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (n/a)</td><td>20786.53 (-2.99%)</td><td>17346.57 (-12.77%)</td><td>17558.44 (-15.46%)</td><td>14720.43 (-12.49%)</td><td>2539.98 <b>(+33.52%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21427.35 (n/a)</td><td>19885.82 (n/a)</td><td>20769.78 (n/a)</td><td>16821.89 (n/a)</td><td>1902.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.00 <b>(+116.67%)</b></td><td>0.00 <b>(+56.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+573.80%)</b></td><td>18473.88 (-2.20%)</td><td>13158.86 <b>(-21.64%)</b></td><td>16512.32 (-0.77%)</td><td>6111.54 <b>(-57.39%)</b></td><td>6329.32 <b>(+262.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18890.03 (n/a)</td><td>16792.67 (n/a)</td><td>16640.05 (n/a)</td><td>14342.14 (n/a)</td><td>1743.73 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.15 <b>(+37.91%)</b></td><td>0.10 (+13.88%)</td><td>0.09 (+3.05%)</td><td>0.07 (-8.24%)</td><td>0.03 <b>(+121.40%)</b></td><td>31935.69 (+9.09%)</td><td>22189.18 (-6.48%)</td><td>23011.36 (-3.01%)</td><td>13562.18 <b>(-27.53%)</b></td><td>7072.47 <b>(+72.99%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>29274.86 (n/a)</td><td>23727.88 (n/a)</td><td>23726.25 (n/a)</td><td>18714.51 (n/a)</td><td>4088.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>1.95 <b>(+27.54%)</b></td><td>1.13 (-9.08%)</td><td>0.98 <b>(-33.75%)</b></td><td>0.25 <b>(-66.41%)</b></td><td>0.69 <b>(+94.18%)</b></td><td>2104.40 <b>(+197.69%)</b></td><td>782.18 <b>(+70.05%)</b></td><td>536.90 <b>(+50.94%)</b></td><td>269.00 <b>(-21.62%)</b></td><td>758.94 <b>(+374.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.53 (n/a)</td><td>1.24 (n/a)</td><td>1.47 (n/a)</td><td>0.74 (n/a)</td><td>0.36 (n/a)</td><td>706.90 (n/a)</td><td>459.98 (n/a)</td><td>355.70 (n/a)</td><td>343.20 (n/a)</td><td>160.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>3.02 <b>(+78.88%)</b></td><td>1.92 <b>(+101.25%)</b></td><td>2.56 <b>(+126.20%)</b></td><td>0.33 (+3.91%)</td><td>1.14 <b>(+87.07%)</b></td><td>3188.30 (-3.76%)</td><td>1059.16 <b>(-40.31%)</b></td><td>410.10 <b>(-55.79%)</b></td><td>347.60 <b>(-44.10%)</b></td><td>1214.20 (-10.66%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.69 (n/a)</td><td>0.95 (n/a)</td><td>1.13 (n/a)</td><td>0.32 (n/a)</td><td>0.61 (n/a)</td><td>3313.00 (n/a)</td><td>1774.42 (n/a)</td><td>927.60 (n/a)</td><td>621.80 (n/a)</td><td>1359.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>1.64 <b>(+30.92%)</b></td><td>0.87 (-4.94%)</td><td>0.62 <b>(-41.92%)</b></td><td>0.46 <b>(+201.14%)</b></td><td>0.48 (+10.50%)</td><td>1136.80 <b>(-66.79%)</b></td><td>735.64 <b>(-30.89%)</b></td><td>845.70 <b>(+72.17%)</b></td><td>319.30 <b>(-23.63%)</b></td><td>324.12 <b>(-75.43%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.25 (n/a)</td><td>0.92 (n/a)</td><td>1.07 (n/a)</td><td>0.15 (n/a)</td><td>0.44 (n/a)</td><td>3423.30 (n/a)</td><td>1064.42 (n/a)</td><td>491.20 (n/a)</td><td>418.10 (n/a)</td><td>1319.07 (n/a)</td>
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
