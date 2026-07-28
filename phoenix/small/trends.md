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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (-13.11%)</td><td>0.03 (-10.26%)</td><td>0.03 (-16.37%)</td><td>0.02 <b>(-21.68%)</b></td><td>0.01 (+13.82%)</td><td>591.50 <b>(+27.67%)</b></td><td>431.76 (+16.69%)</td><td>474.40 (+19.59%)</td><td>273.50 (+15.06%)</td><td>143.86 <b>(+64.79%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>463.30 (n/a)</td><td>370.00 (n/a)</td><td>396.70 (n/a)</td><td>237.70 (n/a)</td><td>87.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.05 (+2.28%)</td><td>0.04 (+4.01%)</td><td>0.04 (-1.38%)</td><td>0.02 (-16.25%)</td><td>0.01 (+6.61%)</td><td>495.20 (+19.41%)</td><td>312.72 (-2.25%)</td><td>283.30 (+1.40%)</td><td>228.00 (-2.23%)</td><td>105.44 <b>(+25.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>414.70 (n/a)</td><td>319.92 (n/a)</td><td>279.40 (n/a)</td><td>233.20 (n/a)</td><td>84.06 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.05 <b>(+37.66%)</b></td><td>0.03 (+1.66%)</td><td>0.03 (+2.33%)</td><td>0.01 <b>(-71.46%)</b></td><td>0.02 <b>(+156.65%)</b></td><td>2032.80 <b>(+250.36%)</b></td><td>730.38 <b>(+55.72%)</b></td><td>438.90 (-2.27%)</td><td>240.20 <b>(-27.34%)</b></td><td>735.76 <b>(+643.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.20 (n/a)</td><td>469.02 (n/a)</td><td>449.10 (n/a)</td><td>330.60 (n/a)</td><td>98.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (+4.97%)</td><td>0.02 (+1.81%)</td><td>0.02 (-4.40%)</td><td>0.01 <b>(+56.04%)</b></td><td>0.00 <b>(-33.87%)</b></td><td>430.60 <b>(-35.91%)</b></td><td>320.20 (-10.42%)</td><td>306.30 (+4.61%)</td><td>250.80 (-4.75%)</td><td>69.63 <b>(-60.52%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>671.90 (n/a)</td><td>357.46 (n/a)</td><td>292.80 (n/a)</td><td>263.30 (n/a)</td><td>176.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (+8.86%)</td><td>0.02 <b>(+22.31%)</b></td><td>0.02 <b>(+69.87%)</b></td><td>0.01 (-13.02%)</td><td>0.01 <b>(+51.03%)</b></td><td>585.50 (+14.96%)</td><td>373.58 (-11.01%)</td><td>262.70 <b>(-41.14%)</b></td><td>237.20 (-8.13%)</td><td>166.30 <b>(+63.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.30 (n/a)</td><td>419.80 (n/a)</td><td>446.30 (n/a)</td><td>258.20 (n/a)</td><td>101.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+12.81%)</td><td>0.01 <b>(+20.22%)</b></td><td>0.01 <b>(+21.44%)</b></td><td>0.01 <b>(+29.54%)</b></td><td>0.01 (+6.73%)</td><td>598.90 <b>(-22.80%)</b></td><td>428.58 (-19.18%)</td><td>446.70 (-17.66%)</td><td>199.60 (-11.37%)</td><td>150.08 <b>(-24.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>775.80 (n/a)</td><td>530.28 (n/a)</td><td>542.50 (n/a)</td><td>225.20 (n/a)</td><td>197.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.01 (-4.86%)</td><td>0.01 (-4.19%)</td><td>0.01 (+3.01%)</td><td>0.01 (-19.02%)</td><td>0.00 <b>(+49.81%)</b></td><td>705.50 <b>(+23.49%)</b></td><td>526.94 (+6.95%)</td><td>477.00 (-2.93%)</td><td>423.60 (+5.11%)</td><td>119.20 <b>(+95.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.30 (n/a)</td><td>492.68 (n/a)</td><td>491.40 (n/a)</td><td>403.00 (n/a)</td><td>60.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+19.82%)</td><td>0.02 <b>(+40.65%)</b></td><td>0.01 <b>(+48.72%)</b></td><td>0.01 <b>(+26.79%)</b></td><td>0.01 (+7.49%)</td><td>470.20 <b>(-21.13%)</b></td><td>342.16 <b>(-30.90%)</b></td><td>362.30 <b>(-32.76%)</b></td><td>194.90 (-16.57%)</td><td>108.26 <b>(-27.52%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.20 (n/a)</td><td>495.18 (n/a)</td><td>538.80 (n/a)</td><td>233.60 (n/a)</td><td>149.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (+7.58%)</td><td>0.01 <b>(+24.46%)</b></td><td>0.01 <b>(+32.33%)</b></td><td>0.01 <b>(+58.40%)</b></td><td>0.00 <b>(-22.20%)</b></td><td>599.10 <b>(-36.88%)</b></td><td>478.30 <b>(-25.81%)</b></td><td>444.40 <b>(-24.43%)</b></td><td>326.50 (-7.03%)</td><td>112.37 <b>(-54.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>949.10 (n/a)</td><td>644.72 (n/a)</td><td>588.10 (n/a)</td><td>351.20 (n/a)</td><td>246.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>512.70 (n/a)</td><td>291.96 (n/a)</td><td>258.50 (n/a)</td><td>174.30 (n/a)</td><td>129.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.90 (n/a)</td><td>317.54 (n/a)</td><td>274.50 (n/a)</td><td>242.00 (n/a)</td><td>106.41 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>584.20 (n/a)</td><td>437.60 (n/a)</td><td>523.50 (n/a)</td><td>229.20 (n/a)</td><td>171.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>661.40 (n/a)</td><td>380.18 (n/a)</td><td>264.00 (n/a)</td><td>213.90 (n/a)</td><td>203.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>637.00 (n/a)</td><td>416.80 (n/a)</td><td>392.50 (n/a)</td><td>195.90 (n/a)</td><td>189.96 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>642.20 (n/a)</td><td>489.64 (n/a)</td><td>484.50 (n/a)</td><td>275.00 (n/a)</td><td>137.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.40 (n/a)</td><td>394.72 (n/a)</td><td>311.60 (n/a)</td><td>308.00 (n/a)</td><td>123.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.60 (n/a)</td><td>428.28 (n/a)</td><td>386.80 (n/a)</td><td>307.60 (n/a)</td><td>122.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.90 (n/a)</td><td>452.78 (n/a)</td><td>452.60 (n/a)</td><td>247.00 (n/a)</td><td>130.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.70 (n/a)</td><td>379.72 (n/a)</td><td>345.80 (n/a)</td><td>259.60 (n/a)</td><td>108.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.10 (n/a)</td><td>483.58 (n/a)</td><td>517.40 (n/a)</td><td>270.70 (n/a)</td><td>127.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>584.80 (n/a)</td><td>530.38 (n/a)</td><td>531.80 (n/a)</td><td>467.90 (n/a)</td><td>42.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.56 (-9.11%)</td><td>0.30 (-7.53%)</td><td>0.32 (-8.17%)</td><td>0.12 (-2.22%)</td><td>0.19 (-3.36%)</td><td>1806.40 (+2.26%)</td><td>1051.08 (+14.53%)</td><td>685.70 (+8.89%)</td><td>394.60 (+10.04%)</td><td>689.60 <b>(+21.10%)</b></td><td>23.92 (-9.11%)</td><td>12.89 (-7.53%)</td><td>13.76 (-8.17%)</td><td>5.22 (-2.22%)</td><td>7.92 (-3.36%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.62 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.19 (n/a)</td><td>1766.40 (n/a)</td><td>917.74 (n/a)</td><td>629.70 (n/a)</td><td>358.60 (n/a)</td><td>569.46 (n/a)</td><td>26.31 (n/a)</td><td>13.94 (n/a)</td><td>14.99 (n/a)</td><td>5.34 (n/a)</td><td>8.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.56 (+3.76%)</td><td>0.37 (-11.19%)</td><td>0.34 <b>(-24.78%)</b></td><td>0.13 <b>(-31.10%)</b></td><td>0.17 <b>(+22.48%)</b></td><td>1759.40 <b>(+45.13%)</b></td><td>782.30 <b>(+26.97%)</b></td><td>651.90 <b>(+32.93%)</b></td><td>391.50 (-3.62%)</td><td>558.74 <b>(+66.66%)</b></td><td>24.10 (+3.76%)</td><td>15.83 (-11.19%)</td><td>14.48 <b>(-24.78%)</b></td><td>5.36 <b>(-31.10%)</b></td><td>7.19 <b>(+22.48%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>1212.30 (n/a)</td><td>616.14 (n/a)</td><td>490.40 (n/a)</td><td>406.20 (n/a)</td><td>335.25 (n/a)</td><td>23.23 (n/a)</td><td>17.83 (n/a)</td><td>19.25 (n/a)</td><td>7.78 (n/a)</td><td>5.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.31 (-0.49%)</td><td>0.30 (+0.02%)</td><td>0.31 (+0.81%)</td><td>0.29 (-3.23%)</td><td>0.01 <b>(+47.69%)</b></td><td>87584.10 (+3.34%)</td><td>83152.12 (+0.02%)</td><td>82398.70 (-0.80%)</td><td>81289.30 (+0.49%)</td><td>2525.07 <b>(+53.82%)</b></td><td>211.34 (-0.49%)</td><td>206.75 (+0.02%)</td><td>208.50 (+0.81%)</td><td>196.15 (-3.23%)</td><td>6.06 <b>(+47.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84752.10 (n/a)</td><td>83136.20 (n/a)</td><td>83067.00 (n/a)</td><td>80892.80 (n/a)</td><td>1641.56 (n/a)</td><td>212.38 (n/a)</td><td>206.71 (n/a)</td><td>206.82 (n/a)</td><td>202.71 (n/a)</td><td>4.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>1.02 (-0.97%)</td><td>1.01 (+0.38%)</td><td>1.02 (+0.14%)</td><td>0.99 (+1.04%)</td><td>0.01 <b>(-47.42%)</b></td><td>25321.30 (-1.03%)</td><td>24836.22 (-0.41%)</td><td>24735.70 (-0.14%)</td><td>24605.20 (+0.98%)</td><td>293.85 <b>(-47.52%)</b></td><td>698.22 (-0.97%)</td><td>691.80 (+0.38%)</td><td>694.54 (+0.14%)</td><td>678.47 (+1.04%)</td><td>8.10 <b>(-47.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25585.90 (n/a)</td><td>24937.52 (n/a)</td><td>24771.20 (n/a)</td><td>24367.50 (n/a)</td><td>559.89 (n/a)</td><td>705.03 (n/a)</td><td>689.19 (n/a)</td><td>693.54 (n/a)</td><td>671.46 (n/a)</td><td>15.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>3.68 <b>(+90.22%)</b></td><td>2.34 <b>(+33.15%)</b></td><td>2.13 (+15.97%)</td><td>1.70 <b>(+26.08%)</b></td><td>0.77 <b>(+217.75%)</b></td><td>4745.00 <b>(-20.68%)</b></td><td>3684.52 <b>(-21.13%)</b></td><td>3792.20 (-13.77%)</td><td>2190.00 <b>(-47.43%)</b></td><td>926.25 <b>(+22.28%)</b></td><td>965.27 <b>(+90.22%)</b></td><td>613.47 <b>(+33.15%)</b></td><td>557.44 (+15.97%)</td><td>445.50 <b>(+26.08%)</b></td><td>202.15 <b>(+217.75%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>1.94 (n/a)</td><td>1.76 (n/a)</td><td>1.83 (n/a)</td><td>1.35 (n/a)</td><td>0.24 (n/a)</td><td>5982.40 (n/a)</td><td>4671.68 (n/a)</td><td>4397.70 (n/a)</td><td>4165.70 (n/a)</td><td>757.48 (n/a)</td><td>507.46 (n/a)</td><td>460.72 (n/a)</td><td>480.69 (n/a)</td><td>353.36 (n/a)</td><td>63.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.33 <b>(+31.03%)</b></td><td>0.22 (+5.40%)</td><td>0.18 (-17.18%)</td><td>0.16 (-2.88%)</td><td>0.07 <b>(+122.33%)</b></td><td>7654.00 (+2.97%)</td><td>6026.84 (-0.21%)</td><td>6845.70 <b>(+20.74%)</b></td><td>3822.70 <b>(-23.68%)</b></td><td>1625.82 <b>(+72.78%)</b></td><td>17.56 <b>(+31.03%)</b></td><td>11.93 (+5.40%)</td><td>9.80 (-17.18%)</td><td>8.77 (-2.88%)</td><td>3.73 <b>(+122.33%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>7433.30 (n/a)</td><td>6039.82 (n/a)</td><td>5669.70 (n/a)</td><td>5008.80 (n/a)</td><td>940.99 (n/a)</td><td>13.40 (n/a)</td><td>11.32 (n/a)</td><td>11.84 (n/a)</td><td>9.03 (n/a)</td><td>1.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>3.80 (n/a)</td><td>3.64 (n/a)</td><td>3.58 (n/a)</td><td>3.51 (n/a)</td><td>0.14 (n/a)</td><td>3.80 (n/a)</td><td>3.64 (n/a)</td><td>3.58 (n/a)</td><td>3.51 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>7.07 (-7.03%)</td><td>6.63 (+8.15%)</td><td>6.81 (+15.24%)</td><td>5.64 (+3.62%)</td><td>0.58 <b>(-31.58%)</b></td><td>7.06 (-7.03%)</td><td>6.63 (+8.15%)</td><td>6.81 (+15.24%)</td><td>5.63 (+3.62%)</td><td>0.58 <b>(-31.58%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>7.60 (n/a)</td><td>6.13 (n/a)</td><td>5.91 (n/a)</td><td>5.44 (n/a)</td><td>0.84 (n/a)</td><td>7.59 (n/a)</td><td>6.13 (n/a)</td><td>5.91 (n/a)</td><td>5.44 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>12.82 (-8.27%)</td><td>9.42 (-10.93%)</td><td>9.14 (-4.70%)</td><td>7.32 (-6.76%)</td><td>2.16 <b>(-20.78%)</b></td><td>12.81 (-8.27%)</td><td>9.41 (-10.93%)</td><td>9.14 (-4.70%)</td><td>7.32 (-6.76%)</td><td>2.16 <b>(-20.78%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>13.98 (n/a)</td><td>10.57 (n/a)</td><td>9.59 (n/a)</td><td>7.85 (n/a)</td><td>2.72 (n/a)</td><td>13.97 (n/a)</td><td>10.56 (n/a)</td><td>9.59 (n/a)</td><td>7.85 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>3.79 (n/a)</td><td>3.74 (n/a)</td><td>3.74 (n/a)</td><td>3.70 (n/a)</td><td>0.04 (n/a)</td><td>3.78 (n/a)</td><td>3.74 (n/a)</td><td>3.74 (n/a)</td><td>3.70 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>7.47 (+2.76%)</td><td>6.66 (+9.29%)</td><td>6.74 (+2.32%)</td><td>5.65 (+16.74%)</td><td>0.69 <b>(-36.15%)</b></td><td>7.47 (+2.76%)</td><td>6.65 (+9.29%)</td><td>6.74 (+2.32%)</td><td>5.65 (+16.74%)</td><td>0.69 <b>(-36.15%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>7.27 (n/a)</td><td>6.09 (n/a)</td><td>6.59 (n/a)</td><td>4.84 (n/a)</td><td>1.08 (n/a)</td><td>7.27 (n/a)</td><td>6.09 (n/a)</td><td>6.59 (n/a)</td><td>4.84 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>13.81 (-1.45%)</td><td>9.57 (-12.32%)</td><td>8.62 (-18.76%)</td><td>7.34 (-11.71%)</td><td>2.63 (+1.08%)</td><td>13.80 (-1.45%)</td><td>9.56 (-12.32%)</td><td>8.62 (-18.76%)</td><td>7.34 (-11.71%)</td><td>2.63 (+1.08%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>14.01 (n/a)</td><td>10.91 (n/a)</td><td>10.61 (n/a)</td><td>8.31 (n/a)</td><td>2.60 (n/a)</td><td>14.00 (n/a)</td><td>10.90 (n/a)</td><td>10.61 (n/a)</td><td>8.31 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>3.01 (+11.42%)</td><td>2.06 (+12.18%)</td><td>1.67 (+3.62%)</td><td>1.40 <b>(+34.76%)</b></td><td>0.76 (+17.48%)</td><td>3.00 (+11.42%)</td><td>2.06 (+12.18%)</td><td>1.67 (+3.62%)</td><td>1.40 <b>(+34.76%)</b></td><td>0.76 (+17.48%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.70 (n/a)</td><td>1.84 (n/a)</td><td>1.61 (n/a)</td><td>1.04 (n/a)</td><td>0.65 (n/a)</td><td>2.69 (n/a)</td><td>1.83 (n/a)</td><td>1.61 (n/a)</td><td>1.04 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.51 (+3.87%)</td><td>0.28 (+1.29%)</td><td>0.25 <b>(-22.81%)</b></td><td>0.08 (+1.02%)</td><td>0.21 <b>(+25.25%)</b></td><td>0.50 (+3.87%)</td><td>0.27 (+1.29%)</td><td>0.25 <b>(-22.80%)</b></td><td>0.07 (+1.02%)</td><td>0.21 <b>(+25.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.49 (n/a)</td><td>0.28 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>0.48 (n/a)</td><td>0.27 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.56 <b>(-23.25%)</b></td><td>0.37 (-19.58%)</td><td>0.35 <b>(-23.23%)</b></td><td>0.28 <b>(+270.87%)</b></td><td>0.11 <b>(-54.08%)</b></td><td>0.56 <b>(-23.25%)</b></td><td>0.37 (-19.58%)</td><td>0.34 <b>(-23.23%)</b></td><td>0.28 <b>(+270.87%)</b></td><td>0.11 <b>(-54.08%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.74 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.73 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>2.41 (+19.37%)</td><td>1.42 (+17.69%)</td><td>1.15 <b>(-22.06%)</b></td><td>0.44 (-1.95%)</td><td>0.92 <b>(+28.17%)</b></td><td>2.37 (+19.37%)</td><td>1.40 (+17.69%)</td><td>1.13 <b>(-22.06%)</b></td><td>0.43 (-1.95%)</td><td>0.90 <b>(+28.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.02 (n/a)</td><td>1.21 (n/a)</td><td>1.47 (n/a)</td><td>0.45 (n/a)</td><td>0.71 (n/a)</td><td>1.99 (n/a)</td><td>1.19 (n/a)</td><td>1.45 (n/a)</td><td>0.44 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.10 (n/a)</td><td>494.42 (n/a)</td><td>502.10 (n/a)</td><td>369.00 (n/a)</td><td>76.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1070.90 (n/a)</td><td>468.08 (n/a)</td><td>296.80 (n/a)</td><td>259.00 (n/a)</td><td>343.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>441.90 (n/a)</td><td>289.88 (n/a)</td><td>260.10 (n/a)</td><td>237.30 (n/a)</td><td>85.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.70 (n/a)</td><td>488.48 (n/a)</td><td>518.70 (n/a)</td><td>394.90 (n/a)</td><td>78.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.70 (n/a)</td><td>402.00 (n/a)</td><td>458.50 (n/a)</td><td>258.50 (n/a)</td><td>130.50 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.80 (n/a)</td><td>393.50 (n/a)</td><td>421.30 (n/a)</td><td>222.20 (n/a)</td><td>110.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 <b>(-22.54%)</b></td><td>0.02 (+16.29%)</td><td>0.03 <b>(+61.40%)</b></td><td>0.02 (+14.66%)</td><td>0.01 <b>(-29.92%)</b></td><td>539.30 (-12.78%)</td><td>378.38 (-18.95%)</td><td>298.60 <b>(-38.04%)</b></td><td>265.70 <b>(+29.11%)</b></td><td>136.84 (-16.61%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.30 (n/a)</td><td>466.86 (n/a)</td><td>481.90 (n/a)</td><td>205.80 (n/a)</td><td>164.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+16.26%)</td><td>0.03 (-0.10%)</td><td>0.03 (+7.80%)</td><td>0.01 <b>(-47.41%)</b></td><td>0.01 <b>(+662.59%)</b></td><td>572.80 <b>(+90.17%)</b></td><td>320.86 (+11.58%)</td><td>268.30 (-7.23%)</td><td>234.60 (-13.97%)</td><td>142.89 <b>(+1187.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>301.20 (n/a)</td><td>287.56 (n/a)</td><td>289.20 (n/a)</td><td>272.70 (n/a)</td><td>11.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (+18.78%)</td><td>0.03 <b>(+88.84%)</b></td><td>0.03 <b>(+93.08%)</b></td><td>0.03 <b>(+524.20%)</b></td><td>0.00 <b>(-66.68%)</b></td><td>301.30 <b>(-83.98%)</b></td><td>256.10 <b>(-73.11%)</b></td><td>242.20 <b>(-48.20%)</b></td><td>224.60 (-15.82%)</td><td>34.91 <b>(-95.86%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1880.90 (n/a)</td><td>952.52 (n/a)</td><td>467.60 (n/a)</td><td>266.80 (n/a)</td><td>843.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (-5.80%)</td><td>0.03 <b>(+24.01%)</b></td><td>0.03 <b>(+69.52%)</b></td><td>0.02 (+10.51%)</td><td>0.01 <b>(-28.22%)</b></td><td>534.70 (-9.51%)</td><td>323.08 <b>(-25.04%)</b></td><td>291.30 <b>(-41.01%)</b></td><td>247.80 (+6.17%)</td><td>120.27 <b>(-29.37%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>430.98 (n/a)</td><td>493.80 (n/a)</td><td>233.40 (n/a)</td><td>170.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 <b>(+54.65%)</b></td><td>0.03 <b>(+56.29%)</b></td><td>0.03 <b>(+63.98%)</b></td><td>0.02 (+17.72%)</td><td>0.01 <b>(+110.39%)</b></td><td>533.40 (-15.06%)</td><td>341.86 <b>(-33.52%)</b></td><td>312.70 <b>(-39.01%)</b></td><td>263.80 <b>(-35.34%)</b></td><td>110.97 (+17.95%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>628.00 (n/a)</td><td>514.26 (n/a)</td><td>512.70 (n/a)</td><td>408.00 (n/a)</td><td>94.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (-0.37%)</td><td>0.02 (+0.40%)</td><td>0.02 (+8.41%)</td><td>0.00 <b>(-57.64%)</b></td><td>0.01 (+10.38%)</td><td>2434.70 <b>(+136.08%)</b></td><td>847.94 <b>(+41.12%)</b></td><td>533.20 (-7.75%)</td><td>241.00 (+0.37%)</td><td>896.32 <b>(+218.37%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1031.30 (n/a)</td><td>600.86 (n/a)</td><td>578.00 (n/a)</td><td>240.10 (n/a)</td><td>281.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+13.68%)</td><td>0.02 (+5.81%)</td><td>0.03 (+1.56%)</td><td>0.02 (+13.58%)</td><td>0.01 (+2.95%)</td><td>543.90 (-11.95%)</td><td>368.12 (-6.78%)</td><td>294.30 (-1.54%)</td><td>242.70 (-12.03%)</td><td>131.48 (-15.31%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.70 (n/a)</td><td>394.90 (n/a)</td><td>298.90 (n/a)</td><td>275.90 (n/a)</td><td>155.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+4.95%)</td><td>0.01 <b>(-21.17%)</b></td><td>0.01 (-7.50%)</td><td>0.00 <b>(-73.84%)</b></td><td>0.01 <b>(+72.00%)</b></td><td>2447.50 <b>(+282.24%)</b></td><td>1016.94 <b>(+109.96%)</b></td><td>558.40 (+8.11%)</td><td>273.20 (-4.71%)</td><td>897.05 <b>(+587.31%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.30 (n/a)</td><td>484.36 (n/a)</td><td>516.50 (n/a)</td><td>286.70 (n/a)</td><td>130.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+1.77%)</td><td>0.02 (+9.37%)</td><td>0.02 (+1.87%)</td><td>0.01 <b>(+267.19%)</b></td><td>0.01 <b>(-41.82%)</b></td><td>580.40 <b>(-72.77%)</b></td><td>425.24 <b>(-42.27%)</b></td><td>416.40 (-1.84%)</td><td>282.70 (-1.74%)</td><td>114.21 <b>(-85.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2131.10 (n/a)</td><td>736.60 (n/a)</td><td>424.20 (n/a)</td><td>287.70 (n/a)</td><td>785.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (-5.51%)</td><td>0.03 (+8.47%)</td><td>0.03 (+0.43%)</td><td>0.02 <b>(+139.77%)</b></td><td>0.01 <b>(-50.63%)</b></td><td>425.70 <b>(-58.29%)</b></td><td>332.16 <b>(-27.54%)</b></td><td>290.90 (-0.44%)</td><td>260.90 (+5.84%)</td><td>72.25 <b>(-77.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1020.70 (n/a)</td><td>458.40 (n/a)</td><td>292.20 (n/a)</td><td>246.50 (n/a)</td><td>326.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (+7.12%)</td><td>0.03 <b>(+62.25%)</b></td><td>0.03 <b>(+60.04%)</b></td><td>0.01 <b>(+242.09%)</b></td><td>0.01 (-19.02%)</td><td>556.70 <b>(-70.77%)</b></td><td>343.74 <b>(-58.24%)</b></td><td>287.30 <b>(-37.53%)</b></td><td>223.70 (-6.68%)</td><td>141.29 <b>(-79.27%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1904.50 (n/a)</td><td>823.10 (n/a)</td><td>459.90 (n/a)</td><td>239.70 (n/a)</td><td>681.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+3.64%)</td><td>0.02 (-3.48%)</td><td>0.02 (-1.08%)</td><td>0.01 <b>(-50.10%)</b></td><td>0.01 <b>(+44.50%)</b></td><td>1070.40 <b>(+100.41%)</b></td><td>526.04 <b>(+24.73%)</b></td><td>481.70 (+1.09%)</td><td>243.40 (-3.49%)</td><td>329.58 <b>(+173.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.10 (n/a)</td><td>421.74 (n/a)</td><td>476.50 (n/a)</td><td>252.20 (n/a)</td><td>120.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 <b>(-34.93%)</b></td><td>0.01 (-17.85%)</td><td>0.02 (+14.13%)</td><td>0.01 <b>(-29.89%)</b></td><td>0.01 <b>(-23.34%)</b></td><td>1047.60 <b>(+42.63%)</b></td><td>669.48 <b>(+26.06%)</b></td><td>495.90 (-12.39%)</td><td>444.80 <b>(+53.70%)</b></td><td>284.49 <b>(+74.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>734.50 (n/a)</td><td>531.10 (n/a)</td><td>566.00 (n/a)</td><td>289.40 (n/a)</td><td>162.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 <b>(+30.11%)</b></td><td>0.02 <b>(+24.97%)</b></td><td>0.02 <b>(+32.37%)</b></td><td>0.02 <b>(+23.82%)</b></td><td>0.01 <b>(+31.28%)</b></td><td>532.10 (-19.23%)</td><td>402.86 (-19.69%)</td><td>404.20 <b>(-24.45%)</b></td><td>289.50 <b>(-23.13%)</b></td><td>95.27 (-16.77%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>658.80 (n/a)</td><td>501.62 (n/a)</td><td>535.00 (n/a)</td><td>376.60 (n/a)</td><td>114.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 <b>(-22.93%)</b></td><td>0.02 <b>(-42.47%)</b></td><td>0.02 <b>(-51.63%)</b></td><td>0.01 <b>(-46.13%)</b></td><td>0.01 (+17.87%)</td><td>676.10 <b>(+85.64%)</b></td><td>497.50 <b>(+83.96%)</b></td><td>534.80 <b>(+106.73%)</b></td><td>282.90 <b>(+29.77%)</b></td><td>145.44 <b>(+160.90%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.20 (n/a)</td><td>270.44 (n/a)</td><td>258.70 (n/a)</td><td>218.00 (n/a)</td><td>55.75 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (+3.67%)</td><td>0.03 (+14.21%)</td><td>0.03 (+17.45%)</td><td>0.02 <b>(-23.61%)</b></td><td>0.01 <b>(+32.36%)</b></td><td>709.40 <b>(+30.91%)</b></td><td>441.10 (-7.23%)</td><td>435.30 (-14.86%)</td><td>281.30 (-3.53%)</td><td>172.59 <b>(+66.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.90 (n/a)</td><td>475.48 (n/a)</td><td>511.30 (n/a)</td><td>291.60 (n/a)</td><td>103.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (+2.42%)</td><td>0.02 (-6.46%)</td><td>0.02 <b>(-35.15%)</b></td><td>0.01 (-12.84%)</td><td>0.01 (+16.42%)</td><td>599.70 (+14.73%)</td><td>390.60 (+10.56%)</td><td>430.00 <b>(+54.23%)</b></td><td>233.80 (-2.38%)</td><td>156.09 (+17.59%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.70 (n/a)</td><td>353.28 (n/a)</td><td>278.80 (n/a)</td><td>239.50 (n/a)</td><td>132.75 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 <b>(+51.68%)</b></td><td>0.03 <b>(+34.65%)</b></td><td>0.04 <b>(+68.91%)</b></td><td>0.01 <b>(-69.89%)</b></td><td>0.02 <b>(+280.98%)</b></td><td>1873.20 <b>(+232.07%)</b></td><td>625.30 <b>(+32.61%)</b></td><td>277.20 <b>(-40.81%)</b></td><td>229.30 <b>(-34.07%)</b></td><td>707.05 <b>(+737.49%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>564.10 (n/a)</td><td>471.52 (n/a)</td><td>468.30 (n/a)</td><td>347.80 (n/a)</td><td>84.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (-15.31%)</td><td>0.02 <b>(-22.36%)</b></td><td>0.02 <b>(-36.81%)</b></td><td>0.02 (+1.70%)</td><td>0.01 <b>(-39.52%)</b></td><td>519.40 (-1.68%)</td><td>414.18 <b>(+21.79%)</b></td><td>411.80 <b>(+58.26%)</b></td><td>282.60 (+18.09%)</td><td>88.58 <b>(-30.40%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.30 (n/a)</td><td>340.08 (n/a)</td><td>260.20 (n/a)</td><td>239.30 (n/a)</td><td>127.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.04 (+0.30%)</td><td>0.02 <b>(-20.34%)</b></td><td>0.02 <b>(-44.09%)</b></td><td>0.01 <b>(-68.67%)</b></td><td>0.01 <b>(+48.69%)</b></td><td>1909.00 <b>(+219.18%)</b></td><td>723.96 <b>(+84.77%)</b></td><td>545.90 <b>(+78.87%)</b></td><td>265.80 (-0.30%)</td><td>679.89 <b>(+366.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.10 (n/a)</td><td>391.82 (n/a)</td><td>305.20 (n/a)</td><td>266.60 (n/a)</td><td>145.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (-12.86%)</td><td>0.02 <b>(-28.48%)</b></td><td>0.02 <b>(-43.04%)</b></td><td>0.00 <b>(-76.39%)</b></td><td>0.01 <b>(+24.37%)</b></td><td>2461.60 <b>(+323.46%)</b></td><td>821.58 <b>(+127.89%)</b></td><td>508.80 <b>(+75.57%)</b></td><td>273.60 (+14.77%)</td><td>925.01 <b>(+542.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>360.52 (n/a)</td><td>289.80 (n/a)</td><td>238.40 (n/a)</td><td>143.97 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+10.71%)</td><td>0.02 (+6.94%)</td><td>0.02 (+4.98%)</td><td>0.01 (-11.68%)</td><td>0.01 <b>(+78.85%)</b></td><td>679.90 (+13.22%)</td><td>467.32 (+1.49%)</td><td>425.40 (-4.75%)</td><td>296.60 (-9.66%)</td><td>179.36 <b>(+83.34%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>600.50 (n/a)</td><td>460.44 (n/a)</td><td>446.60 (n/a)</td><td>328.30 (n/a)</td><td>97.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (-1.30%)</td><td>0.02 (-2.18%)</td><td>0.02 (+14.82%)</td><td>0.01 (-5.59%)</td><td>0.01 (-15.79%)</td><td>597.50 (+5.92%)</td><td>431.68 (+0.54%)</td><td>418.90 (-12.91%)</td><td>291.90 (+1.32%)</td><td>115.02 (-6.82%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.10 (n/a)</td><td>429.38 (n/a)</td><td>481.00 (n/a)</td><td>288.10 (n/a)</td><td>123.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.03 (+1.78%)</td><td>0.02 (-1.36%)</td><td>0.02 (+3.47%)</td><td>0.02 (+3.12%)</td><td>0.01 (-11.80%)</td><td>581.40 (-3.04%)</td><td>417.40 (-0.61%)</td><td>412.50 (-3.35%)</td><td>274.60 (-1.75%)</td><td>114.47 (-13.80%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.60 (n/a)</td><td>419.96 (n/a)</td><td>426.80 (n/a)</td><td>279.50 (n/a)</td><td>132.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.02 (-14.12%)</td><td>0.02 (+1.55%)</td><td>0.02 <b>(+23.68%)</b></td><td>0.01 (+3.03%)</td><td>0.00 <b>(-47.95%)</b></td><td>625.10 (-2.93%)</td><td>482.18 (-5.66%)</td><td>441.80 (-19.14%)</td><td>423.50 (+16.44%)</td><td>83.49 <b>(-39.26%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>644.00 (n/a)</td><td>511.12 (n/a)</td><td>546.40 (n/a)</td><td>363.70 (n/a)</td><td>137.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.41 (+17.01%)</td><td>0.27 (+0.96%)</td><td>0.21 <b>(-20.42%)</b></td><td>0.19 (+8.54%)</td><td>0.10 <b>(+27.64%)</b></td><td>524.50 (-7.87%)</td><td>400.60 (+1.60%)</td><td>477.30 <b>(+25.64%)</b></td><td>239.20 (-14.57%)</td><td>129.26 (+5.50%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>569.30 (n/a)</td><td>394.28 (n/a)</td><td>379.90 (n/a)</td><td>280.00 (n/a)</td><td>122.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.35 (-14.40%)</td><td>0.24 (-18.07%)</td><td>0.22 <b>(-27.75%)</b></td><td>0.16 <b>(-22.33%)</b></td><td>0.07 (-13.12%)</td><td>631.40 <b>(+28.75%)</b></td><td>433.28 <b>(+22.80%)</b></td><td>450.80 <b>(+38.41%)</b></td><td>279.40 (+16.81%)</td><td>133.41 <b>(+27.89%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>490.40 (n/a)</td><td>352.82 (n/a)</td><td>325.70 (n/a)</td><td>239.20 (n/a)</td><td>104.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.36 (+11.75%)</td><td>0.26 (+12.70%)</td><td>0.23 (+1.09%)</td><td>0.19 (+7.10%)</td><td>0.08 <b>(+30.11%)</b></td><td>526.40 (-6.63%)</td><td>400.56 (-9.66%)</td><td>432.60 (-1.07%)</td><td>274.20 (-10.51%)</td><td>117.26 (+1.09%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>563.80 (n/a)</td><td>443.40 (n/a)</td><td>437.30 (n/a)</td><td>306.40 (n/a)</td><td>116.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.28 (-3.70%)</td><td>0.20 (-3.61%)</td><td>0.17 (-17.17%)</td><td>0.13 (+1.97%)</td><td>0.06 (-12.34%)</td><td>554.60 (-1.93%)</td><td>401.54 (+1.42%)</td><td>429.40 <b>(+20.72%)</b></td><td>266.70 (+3.81%)</td><td>115.53 (-14.54%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>565.50 (n/a)</td><td>395.92 (n/a)</td><td>355.70 (n/a)</td><td>256.90 (n/a)</td><td>135.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.27 (-0.32%)</td><td>0.22 <b>(+23.83%)</b></td><td>0.27 <b>(+59.99%)</b></td><td>0.14 (+4.33%)</td><td>0.07 <b>(+20.16%)</b></td><td>521.40 (-4.15%)</td><td>364.66 (-17.43%)</td><td>275.20 <b>(-37.50%)</b></td><td>273.80 (+0.33%)</td><td>124.19 (+11.41%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>544.00 (n/a)</td><td>441.64 (n/a)</td><td>440.30 (n/a)</td><td>272.90 (n/a)</td><td>111.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.19 (+1.20%)</td><td>0.16 (+2.84%)</td><td>0.16 (-1.16%)</td><td>0.12 (-2.72%)</td><td>0.03 (-0.40%)</td><td>607.60 (+2.81%)</td><td>479.60 (-2.79%)</td><td>469.60 (+1.19%)</td><td>378.40 (-1.18%)</td><td>85.80 (-0.34%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>591.00 (n/a)</td><td>493.34 (n/a)</td><td>464.10 (n/a)</td><td>382.90 (n/a)</td><td>86.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.47 (+7.69%)</td><td>0.32 (-3.43%)</td><td>0.26 (-14.68%)</td><td>0.20 (+6.25%)</td><td>0.11 (+7.54%)</td><td>645.60 (-5.88%)</td><td>457.14 (+3.98%)</td><td>494.90 (+17.22%)</td><td>281.50 (-7.16%)</td><td>151.90 (-3.98%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>685.90 (n/a)</td><td>439.66 (n/a)</td><td>422.20 (n/a)</td><td>303.20 (n/a)</td><td>158.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.43 (-10.58%)</td><td>0.32 (-1.99%)</td><td>0.29 <b>(-31.30%)</b></td><td>0.27 <b>(+335.19%)</b></td><td>0.06 <b>(-63.08%)</b></td><td>478.10 <b>(-77.02%)</b></td><td>415.70 <b>(-40.32%)</b></td><td>449.60 <b>(+45.55%)</b></td><td>305.40 (+11.87%)</td><td>69.94 <b>(-91.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.48 (n/a)</td><td>0.33 (n/a)</td><td>0.42 (n/a)</td><td>0.06 (n/a)</td><td>0.17 (n/a)</td><td>2080.70 (n/a)</td><td>696.50 (n/a)</td><td>308.90 (n/a)</td><td>273.00 (n/a)</td><td>779.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.41 (-16.65%)</td><td>0.34 <b>(+31.18%)</b></td><td>0.40 <b>(+83.76%)</b></td><td>0.23 <b>(+237.51%)</b></td><td>0.08 <b>(-52.29%)</b></td><td>564.50 <b>(-70.37%)</b></td><td>401.02 <b>(-49.68%)</b></td><td>327.50 <b>(-45.59%)</b></td><td>319.40 (+19.98%)</td><td>110.24 <b>(-83.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.49 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>1905.40 (n/a)</td><td>796.98 (n/a)</td><td>601.90 (n/a)</td><td>266.20 (n/a)</td><td>663.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.00 (+20.00%)</td><td>0.00 (+7.69%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+33.33%)</b></td><td>22672.46 <b>(+29.93%)</b></td><td>17111.07 (+12.45%)</td><td>18519.71 (+9.21%)</td><td>6849.84 (-9.54%)</td><td>5995.55 <b>(+40.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17449.67 (n/a)</td><td>15216.24 (n/a)</td><td>16958.51 (n/a)</td><td>7572.09 (n/a)</td><td>4281.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-29.55%)</b></td><td>0.00 <b>(-44.44%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-15.54%)</td><td>19924.70 (+9.35%)</td><td>15348.30 <b>(+40.81%)</b></td><td>17371.91 <b>(+98.38%)</b></td><td>6701.35 (+10.68%)</td><td>5359.04 (+5.00%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18220.87 (n/a)</td><td>10899.98 (n/a)</td><td>8756.79 (n/a)</td><td>6054.58 (n/a)</td><td>5103.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>0.15 (+3.25%)</td><td>0.11 (+7.47%)</td><td>0.08 (+1.01%)</td><td>0.08 (+3.22%)</td><td>0.04 <b>(+24.10%)</b></td><td>27254.84 (-3.14%)</td><td>21807.44 (-4.56%)</td><td>26079.89 (-1.01%)</td><td>14355.15 (-3.14%)</td><td>6767.27 (+12.72%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28137.61 (n/a)</td><td>22850.01 (n/a)</td><td>26347.03 (n/a)</td><td>14820.53 (n/a)</td><td>6003.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>1.43 <b>(+24.44%)</b></td><td>0.98 (+2.86%)</td><td>1.08 (+14.75%)</td><td>0.26 <b>(-63.10%)</b></td><td>0.43 <b>(+130.66%)</b></td><td>2009.50 <b>(+171.04%)</b></td><td>772.24 <b>(+35.10%)</b></td><td>487.60 (-12.87%)</td><td>366.60 (-19.64%)</td><td>694.21 <b>(+485.91%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>1.15 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.71 (n/a)</td><td>0.19 (n/a)</td><td>741.40 (n/a)</td><td>571.60 (n/a)</td><td>559.60 (n/a)</td><td>456.20 (n/a)</td><td>118.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>2.76 (+10.62%)</td><td>1.54 (+6.11%)</td><td>1.74 (+10.12%)</td><td>0.32 (+7.73%)</td><td>1.08 <b>(+36.97%)</b></td><td>3307.30 (-7.17%)</td><td>1332.18 (+9.05%)</td><td>603.60 (-9.18%)</td><td>379.50 (-9.58%)</td><td>1272.69 (-3.31%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.50 (n/a)</td><td>1.45 (n/a)</td><td>1.58 (n/a)</td><td>0.29 (n/a)</td><td>0.79 (n/a)</td><td>3562.90 (n/a)</td><td>1221.64 (n/a)</td><td>664.60 (n/a)</td><td>419.70 (n/a)</td><td>1316.22 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:43:14</td><td>1.71 (-18.83%)</td><td>1.36 <b>(+35.30%)</b></td><td>1.47 <b>(+70.37%)</b></td><td>0.83 <b>(+79.59%)</b></td><td>0.34 <b>(-47.77%)</b></td><td>628.50 <b>(-44.31%)</b></td><td>411.42 <b>(-38.56%)</b></td><td>356.30 <b>(-41.31%)</b></td><td>306.80 <b>(+23.21%)</b></td><td>128.12 <b>(-60.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.11 (n/a)</td><td>1.00 (n/a)</td><td>0.86 (n/a)</td><td>0.46 (n/a)</td><td>0.64 (n/a)</td><td>1128.60 (n/a)</td><td>669.66 (n/a)</td><td>607.10 (n/a)</td><td>249.00 (n/a)</td><td>322.32 (n/a)</td>
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
