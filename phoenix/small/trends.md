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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (-4.98%)</td><td>0.03 (-13.13%)</td><td>0.03 <b>(-22.04%)</b></td><td>0.02 (-18.82%)</td><td>0.01 (+5.34%)</td><td>632.20 <b>(+23.19%)</b></td><td>414.38 (+18.77%)</td><td>357.90 <b>(+28.28%)</b></td><td>265.70 (+5.27%)</td><td>156.54 <b>(+37.26%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.20 (n/a)</td><td>348.88 (n/a)</td><td>279.00 (n/a)</td><td>252.40 (n/a)</td><td>114.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (-3.54%)</td><td>0.04 (-8.45%)</td><td>0.04 (+0.55%)</td><td>0.02 <b>(-33.86%)</b></td><td>0.01 <b>(+24.13%)</b></td><td>627.30 <b>(+51.19%)</b></td><td>361.70 (+18.10%)</td><td>279.60 (-0.53%)</td><td>233.90 (+3.68%)</td><td>166.87 <b>(+92.78%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>414.90 (n/a)</td><td>306.26 (n/a)</td><td>281.10 (n/a)</td><td>225.60 (n/a)</td><td>86.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 <b>(-57.24%)</b></td><td>0.02 <b>(-34.68%)</b></td><td>0.02 (-15.42%)</td><td>0.02 (-8.18%)</td><td>0.00 <b>(-86.20%)</b></td><td>694.70 (+8.90%)</td><td>601.60 <b>(+33.69%)</b></td><td>601.00 (+18.24%)</td><td>538.20 <b>(+133.90%)</b></td><td>60.36 <b>(-64.49%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>637.90 (n/a)</td><td>450.00 (n/a)</td><td>508.30 (n/a)</td><td>230.10 (n/a)</td><td>169.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 <b>(+22.70%)</b></td><td>0.02 <b>(+28.10%)</b></td><td>0.02 <b>(+43.39%)</b></td><td>0.01 <b>(+44.93%)</b></td><td>0.01 <b>(+21.13%)</b></td><td>495.60 <b>(-30.99%)</b></td><td>338.76 <b>(-23.04%)</b></td><td>250.60 <b>(-30.25%)</b></td><td>219.80 (-18.47%)</td><td>137.42 <b>(-28.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>718.20 (n/a)</td><td>440.20 (n/a)</td><td>359.30 (n/a)</td><td>269.60 (n/a)</td><td>191.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (-8.11%)</td><td>0.02 (+8.17%)</td><td>0.02 <b>(+37.32%)</b></td><td>0.01 (+18.02%)</td><td>0.00 <b>(-36.81%)</b></td><td>525.60 (-15.27%)</td><td>365.48 (-15.62%)</td><td>347.50 <b>(-27.18%)</b></td><td>248.30 (+8.86%)</td><td>101.06 <b>(-40.56%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.30 (n/a)</td><td>433.14 (n/a)</td><td>477.20 (n/a)</td><td>228.10 (n/a)</td><td>170.01 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 <b>(+47.95%)</b></td><td>0.02 <b>(+34.36%)</b></td><td>0.02 <b>(+41.37%)</b></td><td>0.01 (-3.79%)</td><td>0.01 <b>(+106.57%)</b></td><td>479.30 (+3.95%)</td><td>279.50 (-19.68%)</td><td>245.10 <b>(-29.28%)</b></td><td>181.20 <b>(-32.39%)</b></td><td>119.19 <b>(+51.75%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.10 (n/a)</td><td>347.98 (n/a)</td><td>346.60 (n/a)</td><td>268.00 (n/a)</td><td>78.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.01 <b>(-23.76%)</b></td><td>0.01 (+1.16%)</td><td>0.01 (+16.14%)</td><td>0.01 (+14.22%)</td><td>0.00 <b>(-70.13%)</b></td><td>529.10 (-12.44%)</td><td>483.00 (-5.68%)</td><td>498.10 (-13.90%)</td><td>428.90 <b>(+31.20%)</b></td><td>39.70 <b>(-65.68%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.30 (n/a)</td><td>512.06 (n/a)</td><td>578.50 (n/a)</td><td>326.90 (n/a)</td><td>115.67 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 <b>(+25.59%)</b></td><td>0.02 <b>(+48.86%)</b></td><td>0.02 <b>(+95.85%)</b></td><td>0.01 <b>(+33.52%)</b></td><td>0.01 (+19.06%)</td><td>471.50 <b>(-25.10%)</b></td><td>326.70 <b>(-33.45%)</b></td><td>272.90 <b>(-48.95%)</b></td><td>178.60 <b>(-20.37%)</b></td><td>129.85 <b>(-21.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.50 (n/a)</td><td>490.92 (n/a)</td><td>534.60 (n/a)</td><td>224.30 (n/a)</td><td>164.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 <b>(+36.22%)</b></td><td>0.01 <b>(+24.88%)</b></td><td>0.01 (+2.19%)</td><td>0.01 <b>(+201.69%)</b></td><td>0.01 (+12.71%)</td><td>693.30 <b>(-66.85%)</b></td><td>507.64 <b>(-38.05%)</b></td><td>498.10 (-2.14%)</td><td>255.50 <b>(-26.58%)</b></td><td>164.23 <b>(-77.17%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2091.60 (n/a)</td><td>819.42 (n/a)</td><td>509.00 (n/a)</td><td>348.00 (n/a)</td><td>719.33 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.70 (n/a)</td><td>396.24 (n/a)</td><td>402.50 (n/a)</td><td>277.50 (n/a)</td><td>116.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.20 (n/a)</td><td>454.80 (n/a)</td><td>458.60 (n/a)</td><td>256.90 (n/a)</td><td>133.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.40 (n/a)</td><td>461.60 (n/a)</td><td>498.20 (n/a)</td><td>289.30 (n/a)</td><td>151.79 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2473.20 (n/a)</td><td>838.60 (n/a)</td><td>489.00 (n/a)</td><td>311.70 (n/a)</td><td>917.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.40 (n/a)</td><td>420.98 (n/a)</td><td>432.30 (n/a)</td><td>261.40 (n/a)</td><td>126.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1652.40 (n/a)</td><td>607.68 (n/a)</td><td>325.40 (n/a)</td><td>209.10 (n/a)</td><td>603.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.20 (n/a)</td><td>430.90 (n/a)</td><td>424.50 (n/a)</td><td>265.00 (n/a)</td><td>120.68 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.10 (n/a)</td><td>364.98 (n/a)</td><td>275.90 (n/a)</td><td>208.40 (n/a)</td><td>171.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.80 (n/a)</td><td>404.18 (n/a)</td><td>430.90 (n/a)</td><td>193.80 (n/a)</td><td>133.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1942.50 (n/a)</td><td>747.14 (n/a)</td><td>464.10 (n/a)</td><td>327.40 (n/a)</td><td>676.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>551.30 (n/a)</td><td>363.64 (n/a)</td><td>404.50 (n/a)</td><td>152.90 (n/a)</td><td>166.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>560.80 (n/a)</td><td>448.62 (n/a)</td><td>447.10 (n/a)</td><td>334.80 (n/a)</td><td>86.07 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.54 (+12.06%)</td><td>0.41 (+17.18%)</td><td>0.39 (+5.23%)</td><td>0.34 <b>(+179.84%)</b></td><td>0.08 <b>(-41.58%)</b></td><td>659.90 <b>(-64.27%)</b></td><td>554.54 <b>(-31.79%)</b></td><td>572.90 (-4.98%)</td><td>407.50 (-10.77%)</td><td>101.48 <b>(-82.63%)</b></td><td>23.16 (+12.06%)</td><td>17.54 (+17.18%)</td><td>16.47 (+5.23%)</td><td>14.30 <b>(+179.84%)</b></td><td>3.57 <b>(-41.58%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1846.80 (n/a)</td><td>813.00 (n/a)</td><td>602.90 (n/a)</td><td>456.70 (n/a)</td><td>584.24 (n/a)</td><td>20.67 (n/a)</td><td>14.96 (n/a)</td><td>15.65 (n/a)</td><td>5.11 (n/a)</td><td>6.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.63 (+1.18%)</td><td>0.44 (+9.86%)</td><td>0.42 <b>(+20.19%)</b></td><td>0.32 <b>(+22.97%)</b></td><td>0.13 (-7.15%)</td><td>688.70 (-18.67%)</td><td>540.78 (-10.78%)</td><td>531.90 (-16.80%)</td><td>351.20 (-1.15%)</td><td>147.48 (-19.83%)</td><td>26.87 (+1.18%)</td><td>18.63 (+9.86%)</td><td>17.74 <b>(+20.19%)</b></td><td>13.70 <b>(+22.97%)</b></td><td>5.53 (-7.15%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.62 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>846.80 (n/a)</td><td>606.14 (n/a)</td><td>639.30 (n/a)</td><td>355.30 (n/a)</td><td>183.96 (n/a)</td><td>26.56 (n/a)</td><td>16.96 (n/a)</td><td>14.76 (n/a)</td><td>11.14 (n/a)</td><td>5.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.31 (+1.24%)</td><td>0.31 (+0.16%)</td><td>0.31 (+0.89%)</td><td>0.30 (-1.78%)</td><td>0.01 <b>(+187.11%)</b></td><td>84611.30 (+1.81%)</td><td>82135.30 (-0.12%)</td><td>81566.10 (-0.88%)</td><td>80266.00 (-1.22%)</td><td>2002.97 <b>(+188.50%)</b></td><td>214.04 (+1.24%)</td><td>209.26 (+0.16%)</td><td>210.62 (+0.89%)</td><td>203.04 (-1.78%)</td><td>5.07 <b>(+187.11%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83104.60 (n/a)</td><td>82234.64 (n/a)</td><td>82290.90 (n/a)</td><td>81257.80 (n/a)</td><td>694.28 (n/a)</td><td>211.42 (n/a)</td><td>208.92 (n/a)</td><td>208.77 (n/a)</td><td>206.73 (n/a)</td><td>1.77 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>1.03 (-0.39%)</td><td>1.02 (+1.31%)</td><td>1.02 (+0.82%)</td><td>1.00 (+2.02%)</td><td>0.01 <b>(-47.71%)</b></td><td>25203.40 (-1.98%)</td><td>24737.36 (-1.33%)</td><td>24682.70 (-0.81%)</td><td>24419.10 (+0.39%)</td><td>288.84 <b>(-48.55%)</b></td><td>703.54 (-0.39%)</td><td>694.57 (+1.31%)</td><td>696.03 (+0.82%)</td><td>681.65 (+2.02%)</td><td>8.05 <b>(-47.71%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25712.10 (n/a)</td><td>25069.80 (n/a)</td><td>24884.80 (n/a)</td><td>24324.90 (n/a)</td><td>561.43 (n/a)</td><td>706.27 (n/a)</td><td>685.56 (n/a)</td><td>690.37 (n/a)</td><td>668.16 (n/a)</td><td>15.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>3.79 (+3.27%)</td><td>2.46 (+17.12%)</td><td>1.81 (-0.34%)</td><td>1.57 (+1.36%)</td><td>1.04 (+16.84%)</td><td>5134.70 (-1.34%)</td><td>3743.24 (-11.78%)</td><td>4442.90 (+0.34%)</td><td>2128.80 (-3.17%)</td><td>1377.98 (+15.32%)</td><td>992.99 (+3.27%)</td><td>644.07 (+17.12%)</td><td>475.80 (-0.34%)</td><td>411.70 (+1.36%)</td><td>271.52 (+16.84%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>3.67 (n/a)</td><td>2.10 (n/a)</td><td>1.82 (n/a)</td><td>1.55 (n/a)</td><td>0.89 (n/a)</td><td>5204.60 (n/a)</td><td>4243.26 (n/a)</td><td>4427.90 (n/a)</td><td>2198.50 (n/a)</td><td>1194.90 (n/a)</td><td>961.53 (n/a)</td><td>549.90 (n/a)</td><td>477.41 (n/a)</td><td>406.17 (n/a)</td><td>232.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.21 <b>(-31.26%)</b></td><td>0.20 (-7.84%)</td><td>0.20 (-5.21%)</td><td>0.18 <b>(+21.51%)</b></td><td>0.01 <b>(-79.56%)</b></td><td>6755.60 (-17.70%)</td><td>6181.38 (+3.26%)</td><td>6174.70 (+5.49%)</td><td>5818.90 <b>(+45.48%)</b></td><td>372.92 <b>(-75.17%)</b></td><td>11.53 <b>(-31.26%)</b></td><td>10.89 (-7.84%)</td><td>10.87 (-5.21%)</td><td>9.93 <b>(+21.51%)</b></td><td>0.64 <b>(-79.56%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>8208.80 (n/a)</td><td>5986.30 (n/a)</td><td>5853.10 (n/a)</td><td>3999.90 (n/a)</td><td>1501.95 (n/a)</td><td>16.78 (n/a)</td><td>11.81 (n/a)</td><td>11.47 (n/a)</td><td>8.18 (n/a)</td><td>3.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.12 (-12.24%)</td><td>0.07 <b>(-24.14%)</b></td><td>0.06 <b>(-37.61%)</b></td><td>0.06 (-5.12%)</td><td>0.03 <b>(-24.50%)</b></td><td>0.12 (-12.24%)</td><td>0.07 <b>(-24.14%)</b></td><td>0.06 <b>(-37.61%)</b></td><td>0.06 (-5.12%)</td><td>0.03 <b>(-24.50%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>3.94 (+1.70%)</td><td>3.78 (+5.10%)</td><td>3.89 (+11.22%)</td><td>3.32 (-0.37%)</td><td>0.26 (+15.49%)</td><td>3.94 (+1.70%)</td><td>3.78 (+5.10%)</td><td>3.89 (+11.22%)</td><td>3.32 (-0.37%)</td><td>0.26 (+15.49%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>3.87 (n/a)</td><td>3.60 (n/a)</td><td>3.50 (n/a)</td><td>3.34 (n/a)</td><td>0.22 (n/a)</td><td>3.87 (n/a)</td><td>3.60 (n/a)</td><td>3.50 (n/a)</td><td>3.33 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>7.55 (-0.02%)</td><td>6.82 (+8.33%)</td><td>7.06 (+6.00%)</td><td>5.65 (+10.98%)</td><td>0.73 <b>(-27.26%)</b></td><td>7.55 (-0.02%)</td><td>6.82 (+8.33%)</td><td>7.06 (+6.00%)</td><td>5.65 (+10.98%)</td><td>0.73 <b>(-27.26%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>7.56 (n/a)</td><td>6.30 (n/a)</td><td>6.66 (n/a)</td><td>5.09 (n/a)</td><td>1.00 (n/a)</td><td>7.55 (n/a)</td><td>6.29 (n/a)</td><td>6.66 (n/a)</td><td>5.09 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>13.81 <b>(+23.06%)</b></td><td>9.58 (+6.04%)</td><td>8.67 (+2.28%)</td><td>7.82 (+1.23%)</td><td>2.47 <b>(+65.27%)</b></td><td>13.80 <b>(+23.06%)</b></td><td>9.58 (+6.04%)</td><td>8.67 (+2.28%)</td><td>7.81 (+1.23%)</td><td>2.47 <b>(+65.27%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>11.22 (n/a)</td><td>9.04 (n/a)</td><td>8.48 (n/a)</td><td>7.72 (n/a)</td><td>1.50 (n/a)</td><td>11.21 (n/a)</td><td>9.03 (n/a)</td><td>8.48 (n/a)</td><td>7.72 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>3.97 (+3.38%)</td><td>3.78 (+3.42%)</td><td>3.83 (+6.18%)</td><td>3.45 (-1.13%)</td><td>0.21 <b>(+31.56%)</b></td><td>3.97 (+3.38%)</td><td>3.77 (+3.42%)</td><td>3.82 (+6.18%)</td><td>3.45 (-1.13%)</td><td>0.21 <b>(+31.56%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>3.84 (n/a)</td><td>3.65 (n/a)</td><td>3.60 (n/a)</td><td>3.49 (n/a)</td><td>0.16 (n/a)</td><td>3.84 (n/a)</td><td>3.65 (n/a)</td><td>3.60 (n/a)</td><td>3.49 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>7.13 (-5.22%)</td><td>6.06 (-4.76%)</td><td>6.10 (-13.88%)</td><td>4.50 (-6.92%)</td><td>1.09 (-19.00%)</td><td>7.13 (-5.22%)</td><td>6.06 (-4.76%)</td><td>6.09 (-13.88%)</td><td>4.50 (-6.92%)</td><td>1.09 (-19.00%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>7.52 (n/a)</td><td>6.37 (n/a)</td><td>7.08 (n/a)</td><td>4.84 (n/a)</td><td>1.34 (n/a)</td><td>7.52 (n/a)</td><td>6.36 (n/a)</td><td>7.08 (n/a)</td><td>4.84 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>13.88 (+2.75%)</td><td>10.86 (+12.31%)</td><td>9.39 (-1.94%)</td><td>8.18 (+13.75%)</td><td>2.68 (+10.37%)</td><td>13.88 (+2.75%)</td><td>10.86 (+12.31%)</td><td>9.38 (-1.94%)</td><td>8.18 (+13.75%)</td><td>2.68 (+10.37%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>13.51 (n/a)</td><td>9.67 (n/a)</td><td>9.57 (n/a)</td><td>7.19 (n/a)</td><td>2.43 (n/a)</td><td>13.50 (n/a)</td><td>9.67 (n/a)</td><td>9.57 (n/a)</td><td>7.19 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>280.70 (n/a)</td><td>251.96 (n/a)</td><td>247.40 (n/a)</td><td>225.10 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.20 (n/a)</td><td>430.16 (n/a)</td><td>425.60 (n/a)</td><td>241.40 (n/a)</td><td>167.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.30 (n/a)</td><td>368.30 (n/a)</td><td>297.50 (n/a)</td><td>240.60 (n/a)</td><td>162.33 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.20 (n/a)</td><td>493.12 (n/a)</td><td>588.20 (n/a)</td><td>201.60 (n/a)</td><td>177.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.00 (n/a)</td><td>433.44 (n/a)</td><td>472.50 (n/a)</td><td>283.60 (n/a)</td><td>139.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>958.10 (n/a)</td><td>578.86 (n/a)</td><td>459.90 (n/a)</td><td>305.30 (n/a)</td><td>294.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.50 (n/a)</td><td>320.46 (n/a)</td><td>295.70 (n/a)</td><td>253.90 (n/a)</td><td>78.67 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.60 (n/a)</td><td>323.56 (n/a)</td><td>294.40 (n/a)</td><td>244.80 (n/a)</td><td>98.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.60 (n/a)</td><td>435.86 (n/a)</td><td>481.20 (n/a)</td><td>230.40 (n/a)</td><td>196.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.60 (n/a)</td><td>495.52 (n/a)</td><td>546.70 (n/a)</td><td>313.50 (n/a)</td><td>116.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.30 (n/a)</td><td>489.94 (n/a)</td><td>550.10 (n/a)</td><td>270.00 (n/a)</td><td>157.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.50 (n/a)</td><td>376.12 (n/a)</td><td>276.60 (n/a)</td><td>235.70 (n/a)</td><td>175.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.40 (n/a)</td><td>398.64 (n/a)</td><td>386.70 (n/a)</td><td>264.90 (n/a)</td><td>147.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>662.70 (n/a)</td><td>440.96 (n/a)</td><td>383.10 (n/a)</td><td>259.60 (n/a)</td><td>182.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (+13.83%)</td><td>0.03 (-14.04%)</td><td>0.02 (-19.80%)</td><td>0.02 <b>(-43.40%)</b></td><td>0.01 <b>(+416.73%)</b></td><td>529.70 <b>(+76.68%)</b></td><td>360.02 <b>(+29.80%)</b></td><td>336.60 <b>(+24.67%)</b></td><td>226.50 (-12.14%)</td><td>133.92 <b>(+685.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>299.80 (n/a)</td><td>277.36 (n/a)</td><td>270.00 (n/a)</td><td>257.80 (n/a)</td><td>17.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (+6.39%)</td><td>0.02 (+4.43%)</td><td>0.02 (+15.81%)</td><td>0.01 (-7.32%)</td><td>0.01 (+6.57%)</td><td>589.70 (+7.90%)</td><td>394.12 (-3.20%)</td><td>399.30 (-13.65%)</td><td>245.50 (-6.01%)</td><td>134.81 (+9.28%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.50 (n/a)</td><td>407.14 (n/a)</td><td>462.40 (n/a)</td><td>261.20 (n/a)</td><td>123.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (-5.77%)</td><td>0.02 (+7.52%)</td><td>0.02 <b>(+41.27%)</b></td><td>0.02 (+14.06%)</td><td>0.00 <b>(-52.27%)</b></td><td>491.00 (-12.32%)</td><td>389.66 (-13.33%)</td><td>379.80 <b>(-29.22%)</b></td><td>315.10 (+6.13%)</td><td>63.92 <b>(-54.22%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.00 (n/a)</td><td>449.58 (n/a)</td><td>536.60 (n/a)</td><td>296.90 (n/a)</td><td>139.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 <b>(-26.18%)</b></td><td>0.02 <b>(-33.25%)</b></td><td>0.02 <b>(-47.51%)</b></td><td>0.01 <b>(-46.24%)</b></td><td>0.01 <b>(-24.49%)</b></td><td>1116.90 <b>(+86.00%)</b></td><td>574.36 <b>(+56.60%)</b></td><td>524.10 <b>(+90.51%)</b></td><td>243.60 <b>(+35.48%)</b></td><td>325.84 <b>(+84.13%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.50 (n/a)</td><td>366.76 (n/a)</td><td>275.10 (n/a)</td><td>179.80 (n/a)</td><td>176.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 <b>(+21.09%)</b></td><td>0.02 <b>(+27.13%)</b></td><td>0.02 <b>(+42.66%)</b></td><td>0.01 (+6.79%)</td><td>0.01 <b>(+52.26%)</b></td><td>599.40 (-6.36%)</td><td>399.54 (-18.82%)</td><td>346.00 <b>(-29.90%)</b></td><td>287.40 (-17.41%)</td><td>126.29 <b>(+21.94%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>640.10 (n/a)</td><td>492.16 (n/a)</td><td>493.60 (n/a)</td><td>348.00 (n/a)</td><td>103.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (+7.01%)</td><td>0.02 (-17.18%)</td><td>0.02 (-12.12%)</td><td>0.00 <b>(-74.23%)</b></td><td>0.01 <b>(+88.26%)</b></td><td>1995.00 <b>(+288.06%)</b></td><td>738.24 <b>(+80.97%)</b></td><td>468.00 (+13.79%)</td><td>270.90 (-6.52%)</td><td>709.78 <b>(+677.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>514.10 (n/a)</td><td>407.94 (n/a)</td><td>411.30 (n/a)</td><td>289.80 (n/a)</td><td>91.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (+9.34%)</td><td>0.03 <b>(+22.32%)</b></td><td>0.03 <b>(+45.32%)</b></td><td>0.02 (+11.17%)</td><td>0.01 <b>(+32.11%)</b></td><td>491.70 (-10.04%)</td><td>353.00 (-15.51%)</td><td>291.50 <b>(-31.19%)</b></td><td>241.90 (-8.54%)</td><td>121.70 (+18.48%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.60 (n/a)</td><td>417.78 (n/a)</td><td>423.60 (n/a)</td><td>264.50 (n/a)</td><td>102.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (-17.05%)</td><td>0.04 (-14.42%)</td><td>0.05 (+6.75%)</td><td>0.02 <b>(-24.91%)</b></td><td>0.01 (+10.68%)</td><td>562.00 <b>(+33.18%)</b></td><td>359.42 <b>(+23.52%)</b></td><td>269.90 (-6.35%)</td><td>241.40 <b>(+20.52%)</b></td><td>144.78 <b>(+73.82%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>422.00 (n/a)</td><td>290.98 (n/a)</td><td>288.20 (n/a)</td><td>200.30 (n/a)</td><td>83.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (+16.76%)</td><td>0.02 (+14.78%)</td><td>0.03 <b>(+37.25%)</b></td><td>0.01 (-6.62%)</td><td>0.01 <b>(+57.10%)</b></td><td>579.20 (+7.08%)</td><td>384.34 (-5.53%)</td><td>294.50 <b>(-27.14%)</b></td><td>233.60 (-14.34%)</td><td>166.75 <b>(+51.33%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.90 (n/a)</td><td>406.82 (n/a)</td><td>404.20 (n/a)</td><td>272.70 (n/a)</td><td>110.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 <b>(-32.47%)</b></td><td>0.03 <b>(-20.08%)</b></td><td>0.02 <b>(-31.46%)</b></td><td>0.02 (+13.84%)</td><td>0.01 <b>(-48.00%)</b></td><td>563.00 (-12.15%)</td><td>422.60 (+8.07%)</td><td>418.60 <b>(+45.90%)</b></td><td>284.60 <b>(+48.07%)</b></td><td>131.65 <b>(-37.24%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>640.90 (n/a)</td><td>391.04 (n/a)</td><td>286.90 (n/a)</td><td>192.20 (n/a)</td><td>209.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 <b>(-27.33%)</b></td><td>0.02 <b>(-34.35%)</b></td><td>0.02 <b>(-38.78%)</b></td><td>0.01 <b>(-52.93%)</b></td><td>0.01 <b>(-20.59%)</b></td><td>1049.10 <b>(+112.45%)</b></td><td>549.26 <b>(+64.58%)</b></td><td>484.50 <b>(+63.35%)</b></td><td>264.00 <b>(+37.64%)</b></td><td>297.02 <b>(+134.85%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.80 (n/a)</td><td>333.74 (n/a)</td><td>296.60 (n/a)</td><td>191.80 (n/a)</td><td>126.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 <b>(-32.29%)</b></td><td>0.03 (-16.54%)</td><td>0.03 <b>(+39.48%)</b></td><td>0.01 <b>(-74.00%)</b></td><td>0.01 (-16.01%)</td><td>2014.80 <b>(+284.58%)</b></td><td>683.68 <b>(+73.47%)</b></td><td>330.10 <b>(-28.29%)</b></td><td>272.60 <b>(+47.67%)</b></td><td>748.79 <b>(+395.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>523.90 (n/a)</td><td>394.12 (n/a)</td><td>460.30 (n/a)</td><td>184.60 (n/a)</td><td>151.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (+19.03%)</td><td>0.02 (+9.12%)</td><td>0.02 (+5.88%)</td><td>0.01 (-7.34%)</td><td>0.01 <b>(+27.39%)</b></td><td>573.80 (+7.90%)</td><td>387.28 (-5.15%)</td><td>424.70 (-5.56%)</td><td>201.50 (-15.97%)</td><td>147.11 (+9.39%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.80 (n/a)</td><td>408.32 (n/a)</td><td>449.70 (n/a)</td><td>239.80 (n/a)</td><td>134.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 <b>(-42.97%)</b></td><td>0.02 (+8.65%)</td><td>0.02 <b>(+36.71%)</b></td><td>0.02 <b>(+302.92%)</b></td><td>0.00 <b>(-84.81%)</b></td><td>495.70 <b>(-75.18%)</b></td><td>439.86 <b>(-43.65%)</b></td><td>434.20 <b>(-26.87%)</b></td><td>377.20 <b>(+75.36%)</b></td><td>43.39 <b>(-93.79%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1997.10 (n/a)</td><td>780.64 (n/a)</td><td>593.70 (n/a)</td><td>215.10 (n/a)</td><td>698.77 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 <b>(-59.13%)</b></td><td>0.01 <b>(-35.30%)</b></td><td>0.02 (-5.80%)</td><td>0.01 <b>(-47.71%)</b></td><td>0.00 <b>(-70.46%)</b></td><td>1026.60 <b>(+91.28%)</b></td><td>614.14 <b>(+39.05%)</b></td><td>529.40 (+6.16%)</td><td>411.30 <b>(+144.68%)</b></td><td>238.90 <b>(+54.63%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.70 (n/a)</td><td>441.66 (n/a)</td><td>498.70 (n/a)</td><td>168.10 (n/a)</td><td>154.50 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 <b>(+67.36%)</b></td><td>0.03 <b>(+66.31%)</b></td><td>0.03 <b>(+74.43%)</b></td><td>0.02 <b>(+90.70%)</b></td><td>0.01 <b>(+65.11%)</b></td><td>575.80 <b>(-47.56%)</b></td><td>369.04 <b>(-41.00%)</b></td><td>304.50 <b>(-42.68%)</b></td><td>263.50 <b>(-40.25%)</b></td><td>133.75 <b>(-50.81%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1098.00 (n/a)</td><td>625.46 (n/a)</td><td>531.20 (n/a)</td><td>441.00 (n/a)</td><td>271.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 <b>(-39.95%)</b></td><td>0.02 <b>(-38.84%)</b></td><td>0.01 <b>(-32.91%)</b></td><td>0.01 <b>(-55.91%)</b></td><td>0.01 <b>(-28.72%)</b></td><td>1088.10 <b>(+126.78%)</b></td><td>632.02 <b>(+77.05%)</b></td><td>567.80 <b>(+49.07%)</b></td><td>333.80 <b>(+66.57%)</b></td><td>315.84 <b>(+151.60%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.80 (n/a)</td><td>356.98 (n/a)</td><td>380.90 (n/a)</td><td>200.40 (n/a)</td><td>125.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.38 (-11.55%)</td><td>0.24 <b>(-22.99%)</b></td><td>0.20 <b>(-39.06%)</b></td><td>0.13 (-13.04%)</td><td>0.12 (+11.77%)</td><td>780.70 (+14.99%)</td><td>495.44 <b>(+37.11%)</b></td><td>482.00 <b>(+64.11%)</b></td><td>261.70 (+13.05%)</td><td>230.78 <b>(+27.80%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>678.90 (n/a)</td><td>361.34 (n/a)</td><td>293.70 (n/a)</td><td>231.50 (n/a)</td><td>180.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.29 <b>(-24.78%)</b></td><td>0.23 (-15.79%)</td><td>0.24 <b>(-24.70%)</b></td><td>0.19 <b>(+22.72%)</b></td><td>0.04 <b>(-59.87%)</b></td><td>511.90 (-18.51%)</td><td>431.24 (+8.02%)</td><td>414.00 <b>(+32.78%)</b></td><td>339.30 <b>(+32.90%)</b></td><td>69.21 <b>(-56.68%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.32 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>628.20 (n/a)</td><td>399.24 (n/a)</td><td>311.80 (n/a)</td><td>255.30 (n/a)</td><td>159.74 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.38 (-12.37%)</td><td>0.29 (+9.52%)</td><td>0.34 <b>(+66.85%)</b></td><td>0.16 (+7.93%)</td><td>0.11 (-8.60%)</td><td>603.10 (-7.34%)</td><td>398.38 (-9.62%)</td><td>291.50 <b>(-40.07%)</b></td><td>259.40 (+14.12%)</td><td>175.59 (-0.87%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.43 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>650.90 (n/a)</td><td>440.78 (n/a)</td><td>486.40 (n/a)</td><td>227.30 (n/a)</td><td>177.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.27 (+7.72%)</td><td>0.20 (+0.30%)</td><td>0.16 (-3.79%)</td><td>0.14 (-8.68%)</td><td>0.06 <b>(+28.48%)</b></td><td>518.70 (+9.52%)</td><td>399.16 (+2.46%)</td><td>453.20 (+3.94%)</td><td>269.80 (-7.16%)</td><td>111.58 <b>(+29.60%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>473.60 (n/a)</td><td>389.56 (n/a)</td><td>436.00 (n/a)</td><td>290.60 (n/a)</td><td>86.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.25 (+0.99%)</td><td>0.17 (-3.69%)</td><td>0.15 (-9.67%)</td><td>0.11 (-12.47%)</td><td>0.05 <b>(+20.42%)</b></td><td>648.80 (+14.25%)</td><td>456.40 (+6.79%)</td><td>486.80 (+10.71%)</td><td>299.50 (-0.99%)</td><td>138.44 <b>(+34.46%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>567.90 (n/a)</td><td>427.38 (n/a)</td><td>439.70 (n/a)</td><td>302.50 (n/a)</td><td>102.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.29 <b>(+76.24%)</b></td><td>0.22 <b>(+57.86%)</b></td><td>0.28 <b>(+86.12%)</b></td><td>0.10 (-11.57%)</td><td>0.09 <b>(+253.65%)</b></td><td>776.10 (+13.08%)</td><td>400.32 <b>(-25.33%)</b></td><td>262.00 <b>(-46.28%)</b></td><td>254.30 <b>(-43.26%)</b></td><td>226.37 <b>(+117.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>686.30 (n/a)</td><td>536.12 (n/a)</td><td>487.70 (n/a)</td><td>448.20 (n/a)</td><td>104.25 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.26 <b>(-43.16%)</b></td><td>0.23 <b>(-20.93%)</b></td><td>0.22 (-11.77%)</td><td>0.21 <b>(+72.70%)</b></td><td>0.02 <b>(-82.00%)</b></td><td>635.50 <b>(-42.10%)</b></td><td>574.58 (+2.66%)</td><td>587.60 (+13.35%)</td><td>501.40 <b>(+75.93%)</b></td><td>58.95 <b>(-81.72%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>1097.50 (n/a)</td><td>559.70 (n/a)</td><td>518.40 (n/a)</td><td>285.00 (n/a)</td><td>322.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.40 (-4.75%)</td><td>0.27 (-14.24%)</td><td>0.27 (-3.54%)</td><td>0.16 <b>(-28.77%)</b></td><td>0.09 (+3.31%)</td><td>827.30 <b>(+40.39%)</b></td><td>540.28 <b>(+20.28%)</b></td><td>491.40 (+3.67%)</td><td>327.30 (+4.97%)</td><td>184.62 <b>(+56.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>589.30 (n/a)</td><td>449.20 (n/a)</td><td>474.00 (n/a)</td><td>311.80 (n/a)</td><td>117.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.44 <b>(-24.81%)</b></td><td>0.33 (-14.29%)</td><td>0.39 (-7.10%)</td><td>0.12 <b>(-34.32%)</b></td><td>0.13 (-13.77%)</td><td>1069.10 <b>(+52.25%)</b></td><td>493.90 <b>(+25.44%)</b></td><td>337.20 (+7.63%)</td><td>301.00 <b>(+33.01%)</b></td><td>325.66 <b>(+75.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>0.42 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>702.20 (n/a)</td><td>393.74 (n/a)</td><td>313.30 (n/a)</td><td>226.30 (n/a)</td><td>185.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-30.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-34.68%)</b></td><td>21598.80 (-4.19%)</td><td>15813.49 (+9.92%)</td><td>17097.23 (-8.07%)</td><td>6695.96 <b>(+22.32%)</b></td><td>5491.52 <b>(-30.77%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22543.89 (n/a)</td><td>14386.52 (n/a)</td><td>18598.03 (n/a)</td><td>5474.14 (n/a)</td><td>7932.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+28.13%)</b></td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+6.44%)</td><td>21462.12 (+3.20%)</td><td>12263.19 <b>(-20.94%)</b></td><td>13292.95 <b>(-22.00%)</b></td><td>6279.46 (-0.66%)</td><td>6206.94 (+10.70%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20796.73 (n/a)</td><td>15511.98 (n/a)</td><td>17042.51 (n/a)</td><td>6321.14 (n/a)</td><td>5606.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.13 (-5.43%)</td><td>0.09 (-11.31%)</td><td>0.09 (-3.92%)</td><td>0.08 (+8.43%)</td><td>0.02 <b>(-28.70%)</b></td><td>27636.97 (-7.79%)</td><td>23625.81 (+8.75%)</td><td>24451.70 (+4.06%)</td><td>15844.81 (+5.80%)</td><td>4804.73 <b>(-26.50%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29970.72 (n/a)</td><td>21725.33 (n/a)</td><td>23497.02 (n/a)</td><td>14976.59 (n/a)</td><td>6536.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>1.78 (+17.81%)</td><td>1.47 <b>(+37.49%)</b></td><td>1.53 <b>(+62.49%)</b></td><td>0.99 <b>(+44.87%)</b></td><td>0.29 (-17.88%)</td><td>527.90 <b>(-30.97%)</b></td><td>371.84 <b>(-30.84%)</b></td><td>343.70 <b>(-38.45%)</b></td><td>294.70 (-15.12%)</td><td>91.18 <b>(-48.00%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>1.51 (n/a)</td><td>1.07 (n/a)</td><td>0.94 (n/a)</td><td>0.69 (n/a)</td><td>0.36 (n/a)</td><td>764.70 (n/a)</td><td>537.68 (n/a)</td><td>558.40 (n/a)</td><td>347.20 (n/a)</td><td>175.35 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>2.59 (+12.44%)</td><td>2.12 <b>(+46.45%)</b></td><td>1.96 <b>(+23.62%)</b></td><td>1.77 <b>(+497.53%)</b></td><td>0.34 <b>(-53.37%)</b></td><td>591.30 <b>(-83.26%)</b></td><td>504.64 <b>(-58.30%)</b></td><td>536.00 (-19.12%)</td><td>405.50 (-11.06%)</td><td>77.93 <b>(-94.03%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>2.30 (n/a)</td><td>1.45 (n/a)</td><td>1.58 (n/a)</td><td>0.30 (n/a)</td><td>0.74 (n/a)</td><td>3533.00 (n/a)</td><td>1210.16 (n/a)</td><td>662.70 (n/a)</td><td>455.90 (n/a)</td><td>1304.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>1.99 (+13.70%)</td><td>1.34 (+6.71%)</td><td>1.25 (-5.86%)</td><td>0.93 <b>(+28.84%)</b></td><td>0.43 (+2.54%)</td><td>566.30 <b>(-22.38%)</b></td><td>423.32 (-8.90%)</td><td>418.60 (+6.22%)</td><td>263.10 (-12.07%)</td><td>123.59 <b>(-30.05%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>1.75 (n/a)</td><td>1.25 (n/a)</td><td>1.33 (n/a)</td><td>0.72 (n/a)</td><td>0.42 (n/a)</td><td>729.60 (n/a)</td><td>464.70 (n/a)</td><td>394.10 (n/a)</td><td>299.20 (n/a)</td><td>176.70 (n/a)</td>
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
