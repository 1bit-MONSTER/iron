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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (+17.41%)</td><td>0.04 <b>(+43.11%)</b></td><td>0.05 <b>(+60.31%)</b></td><td>0.04 <b>(+62.84%)</b></td><td>0.00 <b>(-45.56%)</b></td><td>316.10 <b>(-38.60%)</b></td><td>275.50 <b>(-32.71%)</b></td><td>272.00 <b>(-37.61%)</b></td><td>247.90 (-14.81%)</td><td>26.72 <b>(-71.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.80 (n/a)</td><td>409.44 (n/a)</td><td>436.00 (n/a)</td><td>291.00 (n/a)</td><td>92.91 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 <b>(+61.62%)</b></td><td>0.04 <b>(+58.76%)</b></td><td>0.04 <b>(+85.70%)</b></td><td>0.02 (+1.35%)</td><td>0.01 <b>(+178.03%)</b></td><td>585.20 (-1.33%)</td><td>362.02 <b>(-31.80%)</b></td><td>299.80 <b>(-46.16%)</b></td><td>242.90 <b>(-38.13%)</b></td><td>140.31 <b>(+76.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>593.10 (n/a)</td><td>530.82 (n/a)</td><td>556.80 (n/a)</td><td>392.60 (n/a)</td><td>79.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (-3.60%)</td><td>0.03 (-1.62%)</td><td>0.03 (+5.73%)</td><td>0.02 (+0.91%)</td><td>0.01 (-8.84%)</td><td>585.60 (-0.91%)</td><td>436.28 (+0.27%)</td><td>449.60 (-5.43%)</td><td>276.80 (+3.75%)</td><td>146.63 (-3.85%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.00 (n/a)</td><td>435.10 (n/a)</td><td>475.40 (n/a)</td><td>266.80 (n/a)</td><td>152.51 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (+2.43%)</td><td>0.02 (-3.28%)</td><td>0.01 (+17.25%)</td><td>0.01 (-4.60%)</td><td>0.01 (-7.74%)</td><td>495.80 (+4.82%)</td><td>364.64 (+2.33%)</td><td>351.70 (-14.72%)</td><td>216.70 (-2.39%)</td><td>116.90 (-0.58%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>473.00 (n/a)</td><td>356.32 (n/a)</td><td>412.40 (n/a)</td><td>222.00 (n/a)</td><td>117.58 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (-18.95%)</td><td>0.02 <b>(+23.99%)</b></td><td>0.02 <b>(+69.63%)</b></td><td>0.01 (+4.50%)</td><td>0.00 <b>(-40.09%)</b></td><td>512.50 (-4.30%)</td><td>321.92 <b>(-24.53%)</b></td><td>285.40 <b>(-41.05%)</b></td><td>243.30 <b>(+23.38%)</b></td><td>108.03 (-19.33%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>535.50 (n/a)</td><td>426.56 (n/a)</td><td>484.10 (n/a)</td><td>197.20 (n/a)</td><td>133.93 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (+16.22%)</td><td>0.02 (+15.43%)</td><td>0.02 <b>(+68.85%)</b></td><td>0.00 <b>(-70.56%)</b></td><td>0.01 <b>(+78.16%)</b></td><td>1864.40 <b>(+239.66%)</b></td><td>607.12 <b>(+45.61%)</b></td><td>270.80 <b>(-40.78%)</b></td><td>225.60 (-13.96%)</td><td>707.93 <b>(+441.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.90 (n/a)</td><td>416.94 (n/a)</td><td>457.30 (n/a)</td><td>262.20 (n/a)</td><td>130.80 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (+19.50%)</td><td>0.01 (-19.15%)</td><td>0.01 <b>(-30.86%)</b></td><td>0.01 <b>(-31.00%)</b></td><td>0.01 <b>(+72.78%)</b></td><td>769.40 <b>(+44.92%)</b></td><td>493.56 <b>(+37.21%)</b></td><td>474.60 <b>(+44.65%)</b></td><td>227.10 (-16.32%)</td><td>194.83 <b>(+90.50%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.90 (n/a)</td><td>359.72 (n/a)</td><td>328.10 (n/a)</td><td>271.40 (n/a)</td><td>102.27 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 <b>(+24.93%)</b></td><td>0.01 <b>(+28.32%)</b></td><td>0.01 (+14.52%)</td><td>0.00 (-8.98%)</td><td>0.01 <b>(+51.04%)</b></td><td>1116.70 (+9.87%)</td><td>503.48 (-10.17%)</td><td>450.30 (-12.68%)</td><td>219.40 (-19.96%)</td><td>361.10 <b>(+29.88%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1016.40 (n/a)</td><td>560.50 (n/a)</td><td>515.70 (n/a)</td><td>274.10 (n/a)</td><td>278.02 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 <b>(+21.92%)</b></td><td>0.01 <b>(+24.92%)</b></td><td>0.01 <b>(+45.45%)</b></td><td>0.01 <b>(+49.04%)</b></td><td>0.01 (+4.13%)</td><td>806.20 <b>(-32.90%)</b></td><td>490.50 <b>(-26.27%)</b></td><td>446.50 <b>(-31.25%)</b></td><td>253.60 (-17.98%)</td><td>200.35 <b>(-42.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1201.50 (n/a)</td><td>665.28 (n/a)</td><td>649.50 (n/a)</td><td>309.20 (n/a)</td><td>347.85 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>392.70 (n/a)</td><td>303.16 (n/a)</td><td>292.70 (n/a)</td><td>230.10 (n/a)</td><td>60.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>550.40 (n/a)</td><td>380.24 (n/a)</td><td>399.60 (n/a)</td><td>231.20 (n/a)</td><td>139.27 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>477.10 (n/a)</td><td>351.06 (n/a)</td><td>334.60 (n/a)</td><td>229.30 (n/a)</td><td>117.74 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>396.52 (n/a)</td><td>445.90 (n/a)</td><td>233.40 (n/a)</td><td>153.56 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2029.70 (n/a)</td><td>949.10 (n/a)</td><td>307.20 (n/a)</td><td>240.50 (n/a)</td><td>940.04 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>632.10 (n/a)</td><td>392.60 (n/a)</td><td>295.40 (n/a)</td><td>247.20 (n/a)</td><td>167.79 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>260.70 (n/a)</td><td>249.22 (n/a)</td><td>249.60 (n/a)</td><td>234.70 (n/a)</td><td>9.51 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>299.40 (n/a)</td><td>254.28 (n/a)</td><td>247.10 (n/a)</td><td>231.30 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>450.20 (n/a)</td><td>318.06 (n/a)</td><td>250.70 (n/a)</td><td>239.70 (n/a)</td><td>101.34 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1054.80 (n/a)</td><td>610.64 (n/a)</td><td>574.80 (n/a)</td><td>279.70 (n/a)</td><td>279.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>454.80 (n/a)</td><td>333.96 (n/a)</td><td>274.80 (n/a)</td><td>249.10 (n/a)</td><td>98.79 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1853.70 (n/a)</td><td>683.26 (n/a)</td><td>433.00 (n/a)</td><td>293.80 (n/a)</td><td>661.47 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.78 <b>(+52.26%)</b></td><td>0.54 <b>(+24.17%)</b></td><td>0.49 (+0.96%)</td><td>0.40 <b>(+29.88%)</b></td><td>0.15 <b>(+72.87%)</b></td><td>546.40 <b>(-23.01%)</b></td><td>436.06 (-17.92%)</td><td>451.50 (-0.94%)</td><td>282.90 <b>(-34.32%)</b></td><td>107.90 (-11.54%)</td><td>33.36 <b>(+52.26%)</b></td><td>22.92 <b>(+24.17%)</b></td><td>20.90 (+0.96%)</td><td>17.27 <b>(+29.88%)</b></td><td>6.57 <b>(+72.87%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.49 (n/a)</td><td>0.31 (n/a)</td><td>0.09 (n/a)</td><td>709.70 (n/a)</td><td>531.24 (n/a)</td><td>455.80 (n/a)</td><td>430.70 (n/a)</td><td>121.97 (n/a)</td><td>21.91 (n/a)</td><td>18.46 (n/a)</td><td>20.70 (n/a)</td><td>13.30 (n/a)</td><td>3.80 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.49 <b>(-35.41%)</b></td><td>0.41 (-14.31%)</td><td>0.42 (+11.37%)</td><td>0.26 <b>(-22.74%)</b></td><td>0.09 <b>(-49.42%)</b></td><td>848.70 <b>(+29.43%)</b></td><td>574.76 (+11.44%)</td><td>524.60 (-10.20%)</td><td>450.60 <b>(+54.85%)</b></td><td>161.24 (+1.22%)</td><td>20.95 <b>(-35.41%)</b></td><td>17.28 (-14.31%)</td><td>17.99 (+11.37%)</td><td>11.12 <b>(-22.74%)</b></td><td>3.90 <b>(-49.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.76 (n/a)</td><td>0.47 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>655.70 (n/a)</td><td>515.74 (n/a)</td><td>584.20 (n/a)</td><td>291.00 (n/a)</td><td>159.30 (n/a)</td><td>32.43 (n/a)</td><td>20.17 (n/a)</td><td>16.15 (n/a)</td><td>14.39 (n/a)</td><td>7.71 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.31 (-1.49%)</td><td>0.31 (+0.28%)</td><td>0.31 (-0.84%)</td><td>0.30 (+3.27%)</td><td>0.00 <b>(-62.94%)</b></td><td>83994.30 (-3.16%)</td><td>82368.58 (-0.34%)</td><td>82028.40 (+0.85%)</td><td>81585.10 (+1.51%)</td><td>938.75 <b>(-63.54%)</b></td><td>210.58 (-1.49%)</td><td>208.59 (+0.28%)</td><td>209.44 (-0.84%)</td><td>204.54 (+3.27%)</td><td>2.35 <b>(-62.94%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86737.70 (n/a)</td><td>82653.04 (n/a)</td><td>81337.30 (n/a)</td><td>80369.00 (n/a)</td><td>2574.98 (n/a)</td><td>213.76 (n/a)</td><td>208.01 (n/a)</td><td>211.22 (n/a)</td><td>198.07 (n/a)</td><td>6.33 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>1.04 (+1.75%)</td><td>1.02 (+2.37%)</td><td>1.02 (+1.57%)</td><td>1.01 (+4.14%)</td><td>0.01 <b>(-51.49%)</b></td><td>24968.20 (-3.98%)</td><td>24670.94 (-2.35%)</td><td>24660.90 (-1.55%)</td><td>24241.70 (-1.72%)</td><td>282.79 <b>(-54.27%)</b></td><td>708.69 (+1.75%)</td><td>696.43 (+2.37%)</td><td>696.65 (+1.57%)</td><td>688.07 (+4.14%)</td><td>8.03 <b>(-51.49%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.02 (n/a)</td><td>26002.20 (n/a)</td><td>25265.40 (n/a)</td><td>25048.10 (n/a)</td><td>24665.20 (n/a)</td><td>618.42 (n/a)</td><td>696.52 (n/a)</td><td>680.30 (n/a)</td><td>685.87 (n/a)</td><td>660.71 (n/a)</td><td>16.55 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>3.50 <b>(+49.84%)</b></td><td>2.40 <b>(+26.05%)</b></td><td>2.02 (+12.70%)</td><td>1.42 (-13.27%)</td><td>1.01 <b>(+237.36%)</b></td><td>5679.00 (+15.30%)</td><td>3862.90 (-10.36%)</td><td>4000.30 (-11.27%)</td><td>2300.90 <b>(-33.26%)</b></td><td>1534.53 <b>(+142.01%)</b></td><td>918.75 <b>(+49.84%)</b></td><td>629.93 <b>(+26.05%)</b></td><td>528.44 (+12.70%)</td><td>372.24 (-13.27%)</td><td>264.83 <b>(+237.36%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>2.34 (n/a)</td><td>1.91 (n/a)</td><td>1.79 (n/a)</td><td>1.64 (n/a)</td><td>0.30 (n/a)</td><td>4925.50 (n/a)</td><td>4309.28 (n/a)</td><td>4508.30 (n/a)</td><td>3447.50 (n/a)</td><td>634.07 (n/a)</td><td>613.17 (n/a)</td><td>499.76 (n/a)</td><td>468.90 (n/a)</td><td>429.18 (n/a)</td><td>78.50 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.27 (-3.93%)</td><td>0.19 (-6.77%)</td><td>0.18 (-10.66%)</td><td>0.14 (-16.41%)</td><td>0.06 <b>(+26.88%)</b></td><td>8880.50 (+19.63%)</td><td>6863.32 (+10.79%)</td><td>6963.80 (+11.93%)</td><td>4617.60 (+4.09%)</td><td>1847.59 <b>(+65.22%)</b></td><td>14.53 (-3.93%)</td><td>10.41 (-6.77%)</td><td>9.64 (-10.66%)</td><td>7.56 (-16.41%)</td><td>2.98 <b>(+26.88%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>7423.20 (n/a)</td><td>6194.88 (n/a)</td><td>6221.60 (n/a)</td><td>4436.10 (n/a)</td><td>1118.26 (n/a)</td><td>15.13 (n/a)</td><td>11.17 (n/a)</td><td>10.79 (n/a)</td><td>9.04 (n/a)</td><td>2.35 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>3.95 (n/a)</td><td>3.65 (n/a)</td><td>3.59 (n/a)</td><td>3.50 (n/a)</td><td>0.18 (n/a)</td><td>3.94 (n/a)</td><td>3.65 (n/a)</td><td>3.59 (n/a)</td><td>3.49 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>7.63 (+0.91%)</td><td>6.97 (-3.13%)</td><td>6.90 (-6.71%)</td><td>6.13 (-7.98%)</td><td>0.57 <b>(+36.77%)</b></td><td>7.63 (+0.91%)</td><td>6.96 (-3.13%)</td><td>6.90 (-6.71%)</td><td>6.13 (-7.98%)</td><td>0.57 <b>(+36.77%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>7.56 (n/a)</td><td>7.19 (n/a)</td><td>7.40 (n/a)</td><td>6.67 (n/a)</td><td>0.41 (n/a)</td><td>7.56 (n/a)</td><td>7.19 (n/a)</td><td>7.39 (n/a)</td><td>6.66 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>8.34 <b>(-35.83%)</b></td><td>7.95 (-18.68%)</td><td>8.08 (-17.71%)</td><td>7.38 (+3.84%)</td><td>0.38 <b>(-85.12%)</b></td><td>8.34 <b>(-35.83%)</b></td><td>7.94 (-18.68%)</td><td>8.08 (-17.71%)</td><td>7.37 (+3.84%)</td><td>0.38 <b>(-85.12%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>13.00 (n/a)</td><td>9.77 (n/a)</td><td>9.82 (n/a)</td><td>7.11 (n/a)</td><td>2.54 (n/a)</td><td>13.00 (n/a)</td><td>9.77 (n/a)</td><td>9.81 (n/a)</td><td>7.10 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>3.91 (n/a)</td><td>3.74 (n/a)</td><td>3.70 (n/a)</td><td>3.56 (n/a)</td><td>0.14 (n/a)</td><td>3.91 (n/a)</td><td>3.74 (n/a)</td><td>3.70 (n/a)</td><td>3.55 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>6.92 (-6.21%)</td><td>6.73 (-2.76%)</td><td>6.73 (-2.33%)</td><td>6.45 (-2.62%)</td><td>0.18 <b>(-36.37%)</b></td><td>6.91 (-6.21%)</td><td>6.73 (-2.76%)</td><td>6.73 (-2.33%)</td><td>6.45 (-2.62%)</td><td>0.18 <b>(-36.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>7.37 (n/a)</td><td>6.92 (n/a)</td><td>6.89 (n/a)</td><td>6.62 (n/a)</td><td>0.28 (n/a)</td><td>7.37 (n/a)</td><td>6.92 (n/a)</td><td>6.89 (n/a)</td><td>6.62 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>14.12 (+5.74%)</td><td>10.03 (-5.08%)</td><td>8.30 (-16.89%)</td><td>7.43 (-9.44%)</td><td>3.20 <b>(+65.61%)</b></td><td>14.11 (+5.74%)</td><td>10.03 (-5.08%)</td><td>8.29 (-16.89%)</td><td>7.42 (-9.44%)</td><td>3.20 <b>(+65.61%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>13.36 (n/a)</td><td>10.57 (n/a)</td><td>9.99 (n/a)</td><td>8.20 (n/a)</td><td>1.93 (n/a)</td><td>13.35 (n/a)</td><td>10.56 (n/a)</td><td>9.98 (n/a)</td><td>8.20 (n/a)</td><td>1.93 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>3.00 (-3.03%)</td><td>2.05 (+7.95%)</td><td>2.07 <b>(+38.41%)</b></td><td>1.02 (-14.46%)</td><td>0.88 (+4.09%)</td><td>2.99 (-3.03%)</td><td>2.04 (+7.95%)</td><td>2.07 <b>(+38.41%)</b></td><td>1.02 (-14.46%)</td><td>0.88 (+4.09%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>3.09 (n/a)</td><td>1.89 (n/a)</td><td>1.50 (n/a)</td><td>1.20 (n/a)</td><td>0.84 (n/a)</td><td>3.08 (n/a)</td><td>1.89 (n/a)</td><td>1.49 (n/a)</td><td>1.19 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.54 (-8.08%)</td><td>0.26 <b>(-39.64%)</b></td><td>0.14 <b>(-75.16%)</b></td><td>0.07 <b>(-48.26%)</b></td><td>0.23 (+16.10%)</td><td>0.53 (-8.08%)</td><td>0.26 <b>(-39.64%)</b></td><td>0.14 <b>(-75.16%)</b></td><td>0.07 <b>(-48.26%)</b></td><td>0.22 (+16.10%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.56 (n/a)</td><td>0.14 (n/a)</td><td>0.20 (n/a)</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.55 (n/a)</td><td>0.14 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.52 <b>(-21.87%)</b></td><td>0.29 <b>(-35.75%)</b></td><td>0.33 <b>(-27.09%)</b></td><td>0.08 (+3.95%)</td><td>0.19 <b>(-20.81%)</b></td><td>0.51 <b>(-21.87%)</b></td><td>0.29 <b>(-35.75%)</b></td><td>0.33 <b>(-27.09%)</b></td><td>0.08 (+3.95%)</td><td>0.19 <b>(-20.81%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.67 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.66 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>2.27 (-6.78%)</td><td>1.41 (+14.56%)</td><td>1.39 <b>(+223.41%)</b></td><td>0.45 (+5.87%)</td><td>0.86 <b>(-21.63%)</b></td><td>2.24 (-6.78%)</td><td>1.38 (+14.56%)</td><td>1.37 <b>(+223.41%)</b></td><td>0.44 (+5.87%)</td><td>0.85 <b>(-21.63%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>2.44 (n/a)</td><td>1.23 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>1.10 (n/a)</td><td>2.40 (n/a)</td><td>1.21 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.80 (n/a)</td><td>388.40 (n/a)</td><td>399.90 (n/a)</td><td>256.90 (n/a)</td><td>126.29 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>396.00 (n/a)</td><td>294.24 (n/a)</td><td>248.20 (n/a)</td><td>212.90 (n/a)</td><td>87.41 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>403.40 (n/a)</td><td>301.84 (n/a)</td><td>296.30 (n/a)</td><td>233.10 (n/a)</td><td>71.21 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.40 (n/a)</td><td>354.46 (n/a)</td><td>270.60 (n/a)</td><td>224.70 (n/a)</td><td>141.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.20 (n/a)</td><td>432.70 (n/a)</td><td>426.40 (n/a)</td><td>245.60 (n/a)</td><td>127.92 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.00 (n/a)</td><td>407.56 (n/a)</td><td>423.00 (n/a)</td><td>216.10 (n/a)</td><td>159.45 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (+10.46%)</td><td>0.03 <b>(+34.40%)</b></td><td>0.03 <b>(+64.00%)</b></td><td>0.02 (+14.79%)</td><td>0.01 (-9.63%)</td><td>510.50 (-12.87%)</td><td>334.68 <b>(-27.94%)</b></td><td>310.90 <b>(-39.03%)</b></td><td>234.80 (-9.45%)</td><td>103.93 <b>(-26.73%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.90 (n/a)</td><td>464.46 (n/a)</td><td>509.90 (n/a)</td><td>259.30 (n/a)</td><td>141.85 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (-14.98%)</td><td>0.03 <b>(+36.42%)</b></td><td>0.03 <b>(+45.12%)</b></td><td>0.01 <b>(+274.67%)</b></td><td>0.01 <b>(-34.75%)</b></td><td>659.10 <b>(-73.31%)</b></td><td>354.26 <b>(-56.11%)</b></td><td>283.80 <b>(-31.10%)</b></td><td>264.70 (+17.59%)</td><td>170.88 <b>(-81.74%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2469.60 (n/a)</td><td>807.16 (n/a)</td><td>411.90 (n/a)</td><td>225.10 (n/a)</td><td>935.82 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (+10.75%)</td><td>0.02 (-18.82%)</td><td>0.02 <b>(-24.20%)</b></td><td>0.02 <b>(-29.16%)</b></td><td>0.01 <b>(+279.27%)</b></td><td>459.30 <b>(+41.15%)</b></td><td>388.22 <b>(+28.78%)</b></td><td>390.60 <b>(+31.91%)</b></td><td>252.00 (-9.71%)</td><td>83.31 <b>(+372.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>325.40 (n/a)</td><td>301.46 (n/a)</td><td>296.10 (n/a)</td><td>279.10 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (-1.84%)</td><td>0.02 (-3.50%)</td><td>0.02 (-13.25%)</td><td>0.02 (-8.71%)</td><td>0.01 (+7.25%)</td><td>542.80 (+9.52%)</td><td>405.76 (+5.99%)</td><td>430.70 (+15.28%)</td><td>229.30 (+1.87%)</td><td>131.82 <b>(+20.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.60 (n/a)</td><td>382.84 (n/a)</td><td>373.60 (n/a)</td><td>225.10 (n/a)</td><td>109.46 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 <b>(-52.59%)</b></td><td>0.02 <b>(-40.22%)</b></td><td>0.01 <b>(-29.64%)</b></td><td>0.01 <b>(-32.19%)</b></td><td>0.00 <b>(-68.83%)</b></td><td>758.40 <b>(+47.46%)</b></td><td>560.32 <b>(+51.01%)</b></td><td>571.80 <b>(+42.13%)</b></td><td>426.30 <b>(+110.94%)</b></td><td>135.06 (-7.34%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.30 (n/a)</td><td>371.04 (n/a)</td><td>402.30 (n/a)</td><td>202.10 (n/a)</td><td>145.76 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (+13.43%)</td><td>0.03 <b>(+24.72%)</b></td><td>0.03 <b>(+42.66%)</b></td><td>0.02 (+6.27%)</td><td>0.01 <b>(+33.91%)</b></td><td>525.60 (-5.89%)</td><td>348.02 (-16.01%)</td><td>298.10 <b>(-29.89%)</b></td><td>212.10 (-11.85%)</td><td>137.66 <b>(+21.48%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.50 (n/a)</td><td>414.34 (n/a)</td><td>425.20 (n/a)</td><td>240.60 (n/a)</td><td>113.32 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 <b>(+28.06%)</b></td><td>0.02 (-3.57%)</td><td>0.02 <b>(-22.79%)</b></td><td>0.02 (-16.55%)</td><td>0.01 <b>(+83.49%)</b></td><td>525.00 (+19.84%)</td><td>389.18 (+16.81%)</td><td>467.00 <b>(+29.51%)</b></td><td>192.70 <b>(-21.92%)</b></td><td>158.18 <b>(+89.54%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.10 (n/a)</td><td>333.16 (n/a)</td><td>360.60 (n/a)</td><td>246.80 (n/a)</td><td>83.46 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 <b>(+73.06%)</b></td><td>0.02 <b>(+59.79%)</b></td><td>0.02 <b>(+32.24%)</b></td><td>0.01 <b>(+229.83%)</b></td><td>0.01 <b>(+43.87%)</b></td><td>568.70 <b>(-69.68%)</b></td><td>403.92 <b>(-48.12%)</b></td><td>370.10 <b>(-24.39%)</b></td><td>224.10 <b>(-42.20%)</b></td><td>150.34 <b>(-75.80%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1875.80 (n/a)</td><td>778.52 (n/a)</td><td>489.50 (n/a)</td><td>387.70 (n/a)</td><td>621.16 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 <b>(-29.05%)</b></td><td>0.03 <b>(-21.31%)</b></td><td>0.03 (-12.80%)</td><td>0.02 <b>(-29.27%)</b></td><td>0.01 <b>(-39.78%)</b></td><td>414.90 <b>(+41.36%)</b></td><td>302.50 <b>(+25.65%)</b></td><td>293.50 (+14.69%)</td><td>245.80 <b>(+40.94%)</b></td><td>66.03 <b>(+23.18%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.50 (n/a)</td><td>240.74 (n/a)</td><td>255.90 (n/a)</td><td>174.40 (n/a)</td><td>53.60 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 <b>(-24.20%)</b></td><td>0.03 (-14.58%)</td><td>0.03 (-10.60%)</td><td>0.02 (-1.43%)</td><td>0.01 <b>(-21.87%)</b></td><td>514.60 (+1.44%)</td><td>348.30 (+14.46%)</td><td>290.70 (+11.85%)</td><td>234.10 <b>(+31.96%)</b></td><td>133.07 (+1.46%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.30 (n/a)</td><td>304.30 (n/a)</td><td>259.90 (n/a)</td><td>177.40 (n/a)</td><td>131.15 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (+2.68%)</td><td>0.02 (+14.90%)</td><td>0.03 <b>(+67.78%)</b></td><td>0.00 (+0.04%)</td><td>0.01 (+1.87%)</td><td>2433.40 (-0.04%)</td><td>743.60 (-7.20%)</td><td>293.30 <b>(-40.40%)</b></td><td>231.60 (-2.61%)</td><td>950.36 (+2.81%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2434.30 (n/a)</td><td>801.28 (n/a)</td><td>492.10 (n/a)</td><td>237.80 (n/a)</td><td>924.35 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (+1.71%)</td><td>0.02 (-3.80%)</td><td>0.02 (-2.66%)</td><td>0.02 (+0.37%)</td><td>0.01 (+2.18%)</td><td>523.50 (-0.36%)</td><td>411.52 (+4.09%)</td><td>457.50 (+2.74%)</td><td>241.50 (-1.71%)</td><td>113.01 (-0.25%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.40 (n/a)</td><td>395.36 (n/a)</td><td>445.30 (n/a)</td><td>245.70 (n/a)</td><td>113.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (+3.82%)</td><td>0.02 <b>(-33.18%)</b></td><td>0.02 <b>(-38.89%)</b></td><td>0.00 <b>(-82.45%)</b></td><td>0.01 <b>(+74.08%)</b></td><td>2521.10 <b>(+469.61%)</b></td><td>867.56 <b>(+151.77%)</b></td><td>504.40 <b>(+63.66%)</b></td><td>252.20 (-3.67%)</td><td>933.30 <b>(+960.43%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>442.60 (n/a)</td><td>344.58 (n/a)</td><td>308.20 (n/a)</td><td>261.80 (n/a)</td><td>88.01 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 <b>(-23.95%)</b></td><td>0.02 (-0.57%)</td><td>0.02 (+4.20%)</td><td>0.02 <b>(+27.30%)</b></td><td>0.01 <b>(-47.78%)</b></td><td>537.50 <b>(-21.44%)</b></td><td>450.14 (-10.61%)</td><td>478.30 (-4.03%)</td><td>279.70 <b>(+31.50%)</b></td><td>98.79 <b>(-45.72%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>684.20 (n/a)</td><td>503.56 (n/a)</td><td>498.40 (n/a)</td><td>212.70 (n/a)</td><td>181.99 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 <b>(+22.92%)</b></td><td>0.03 (-6.22%)</td><td>0.03 (-14.27%)</td><td>0.01 <b>(-35.23%)</b></td><td>0.01 <b>(+69.25%)</b></td><td>789.70 <b>(+54.39%)</b></td><td>393.60 <b>(+26.23%)</b></td><td>297.20 (+16.64%)</td><td>193.20 (-18.65%)</td><td>242.96 <b>(+111.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.50 (n/a)</td><td>311.82 (n/a)</td><td>254.80 (n/a)</td><td>237.50 (n/a)</td><td>115.01 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.06 (+19.01%)</td><td>0.03 (-2.35%)</td><td>0.03 (-12.47%)</td><td>0.02 (-14.23%)</td><td>0.02 <b>(+37.45%)</b></td><td>668.50 (+16.59%)</td><td>463.20 (+12.63%)</td><td>480.00 (+14.26%)</td><td>206.50 (-15.95%)</td><td>211.86 <b>(+42.49%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>573.40 (n/a)</td><td>411.24 (n/a)</td><td>420.10 (n/a)</td><td>245.70 (n/a)</td><td>148.69 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 <b>(+35.03%)</b></td><td>0.02 (-0.43%)</td><td>0.02 (-19.19%)</td><td>0.01 (+3.72%)</td><td>0.01 <b>(+58.10%)</b></td><td>593.20 (-3.59%)</td><td>430.28 (+5.02%)</td><td>474.50 <b>(+23.73%)</b></td><td>218.80 <b>(-25.93%)</b></td><td>139.24 (+7.30%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.30 (n/a)</td><td>409.70 (n/a)</td><td>383.50 (n/a)</td><td>295.40 (n/a)</td><td>129.76 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (-2.38%)</td><td>0.03 (+2.29%)</td><td>0.03 (-8.12%)</td><td>0.02 <b>(+253.88%)</b></td><td>0.01 <b>(-33.65%)</b></td><td>544.20 <b>(-71.74%)</b></td><td>367.32 <b>(-42.76%)</b></td><td>317.20 (+8.82%)</td><td>204.20 (+2.46%)</td><td>141.29 <b>(-80.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1925.70 (n/a)</td><td>641.72 (n/a)</td><td>291.50 (n/a)</td><td>199.30 (n/a)</td><td>731.82 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (+0.22%)</td><td>0.02 (+14.10%)</td><td>0.03 <b>(+53.07%)</b></td><td>0.01 <b>(+77.47%)</b></td><td>0.01 <b>(-27.10%)</b></td><td>551.00 <b>(-43.65%)</b></td><td>379.84 <b>(-24.56%)</b></td><td>311.30 <b>(-34.67%)</b></td><td>250.20 (-0.20%)</td><td>130.35 <b>(-55.54%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>977.90 (n/a)</td><td>503.50 (n/a)</td><td>476.50 (n/a)</td><td>250.70 (n/a)</td><td>293.19 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.05 (+18.78%)</td><td>0.03 (+3.38%)</td><td>0.02 (+16.06%)</td><td>0.02 <b>(+86.75%)</b></td><td>0.01 (-12.43%)</td><td>538.50 <b>(-46.46%)</b></td><td>441.78 (-18.45%)</td><td>513.80 (-13.84%)</td><td>202.50 (-15.84%)</td><td>141.12 <b>(-55.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1005.70 (n/a)</td><td>541.72 (n/a)</td><td>596.30 (n/a)</td><td>240.60 (n/a)</td><td>318.32 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (+7.59%)</td><td>0.02 (-5.35%)</td><td>0.02 (-18.06%)</td><td>0.01 (-3.58%)</td><td>0.01 <b>(+33.79%)</b></td><td>570.00 (+3.71%)</td><td>378.42 (+9.64%)</td><td>363.60 <b>(+22.05%)</b></td><td>246.50 (-7.05%)</td><td>138.37 (+18.09%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.60 (n/a)</td><td>345.16 (n/a)</td><td>297.90 (n/a)</td><td>265.20 (n/a)</td><td>117.18 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (-12.06%)</td><td>0.02 (-5.55%)</td><td>0.02 (+12.36%)</td><td>0.02 (+11.12%)</td><td>0.01 <b>(-42.99%)</b></td><td>611.80 (-10.00%)</td><td>472.52 (-4.27%)</td><td>475.30 (-10.99%)</td><td>310.80 (+13.72%)</td><td>108.41 <b>(-44.79%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.80 (n/a)</td><td>493.60 (n/a)</td><td>534.00 (n/a)</td><td>273.30 (n/a)</td><td>196.36 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.04 (+12.27%)</td><td>0.02 (+9.52%)</td><td>0.02 <b>(+52.36%)</b></td><td>0.02 (+18.32%)</td><td>0.01 (-13.11%)</td><td>533.60 (-15.49%)</td><td>383.66 (-14.78%)</td><td>352.70 <b>(-34.36%)</b></td><td>214.10 (-10.94%)</td><td>135.66 <b>(-28.91%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.40 (n/a)</td><td>450.18 (n/a)</td><td>537.30 (n/a)</td><td>240.40 (n/a)</td><td>190.83 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.03 (-6.85%)</td><td>0.02 <b>(+32.20%)</b></td><td>0.02 <b>(+33.37%)</b></td><td>0.02 <b>(+101.42%)</b></td><td>0.01 <b>(-41.31%)</b></td><td>512.10 <b>(-50.35%)</b></td><td>404.36 <b>(-34.37%)</b></td><td>434.80 <b>(-25.02%)</b></td><td>288.70 (+7.32%)</td><td>88.73 <b>(-67.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1031.50 (n/a)</td><td>616.10 (n/a)</td><td>579.90 (n/a)</td><td>269.00 (n/a)</td><td>272.20 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.02 (-3.94%)</td><td>0.02 (-2.70%)</td><td>0.02 (-11.96%)</td><td>0.01 (-5.89%)</td><td>0.00 (+4.20%)</td><td>659.70 (+6.25%)</td><td>503.56 (+3.35%)</td><td>523.10 (+13.59%)</td><td>374.80 (+4.11%)</td><td>120.09 (+9.16%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.90 (n/a)</td><td>487.26 (n/a)</td><td>460.50 (n/a)</td><td>360.00 (n/a)</td><td>110.01 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.34 (-2.14%)</td><td>0.20 <b>(-22.37%)</b></td><td>0.21 (-12.75%)</td><td>0.09 <b>(-45.27%)</b></td><td>0.09 <b>(+26.11%)</b></td><td>1043.40 <b>(+82.73%)</b></td><td>575.14 <b>(+43.65%)</b></td><td>472.50 (+14.60%)</td><td>290.20 (+2.18%)</td><td>284.12 <b>(+148.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>571.00 (n/a)</td><td>400.38 (n/a)</td><td>412.30 (n/a)</td><td>284.00 (n/a)</td><td>114.17 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.40 <b>(+21.55%)</b></td><td>0.30 <b>(+50.28%)</b></td><td>0.32 <b>(+70.55%)</b></td><td>0.18 <b>(+44.11%)</b></td><td>0.10 <b>(+30.52%)</b></td><td>536.80 <b>(-30.61%)</b></td><td>365.58 <b>(-33.14%)</b></td><td>305.80 <b>(-41.37%)</b></td><td>243.70 (-17.72%)</td><td>137.86 <b>(-22.58%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>773.60 (n/a)</td><td>546.76 (n/a)</td><td>521.60 (n/a)</td><td>296.20 (n/a)</td><td>178.07 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.34 (+16.70%)</td><td>0.22 (+1.32%)</td><td>0.19 (-5.68%)</td><td>0.17 (+3.23%)</td><td>0.07 <b>(+50.13%)</b></td><td>567.40 (-3.14%)</td><td>482.06 (+1.62%)</td><td>513.60 (+6.03%)</td><td>287.00 (-14.30%)</td><td>113.44 <b>(+25.02%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>585.80 (n/a)</td><td>474.36 (n/a)</td><td>484.40 (n/a)</td><td>334.90 (n/a)</td><td>90.74 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.24 (+6.27%)</td><td>0.16 (-16.02%)</td><td>0.18 (+0.64%)</td><td>0.04 <b>(-75.17%)</b></td><td>0.08 <b>(+139.27%)</b></td><td>1928.70 <b>(+302.74%)</b></td><td>720.76 <b>(+77.50%)</b></td><td>417.40 (-0.62%)</td><td>302.10 (-5.92%)</td><td>682.45 <b>(+906.46%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>478.90 (n/a)</td><td>406.06 (n/a)</td><td>420.00 (n/a)</td><td>321.10 (n/a)</td><td>67.81 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.24 <b>(-23.41%)</b></td><td>0.15 <b>(-20.36%)</b></td><td>0.15 (-17.79%)</td><td>0.07 <b>(+72.53%)</b></td><td>0.06 <b>(-38.08%)</b></td><td>1091.60 <b>(-42.04%)</b></td><td>576.88 (-11.24%)</td><td>488.40 <b>(+21.64%)</b></td><td>302.10 <b>(+30.55%)</b></td><td>303.28 <b>(-56.31%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1883.40 (n/a)</td><td>649.96 (n/a)</td><td>401.50 (n/a)</td><td>231.40 (n/a)</td><td>694.10 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.30 (-4.04%)</td><td>0.20 <b>(+22.56%)</b></td><td>0.16 <b>(+26.63%)</b></td><td>0.11 (+1.11%)</td><td>0.08 (-5.36%)</td><td>646.90 (-1.10%)</td><td>418.18 (-19.34%)</td><td>461.40 <b>(-21.03%)</b></td><td>243.80 (+4.23%)</td><td>164.18 (-1.95%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.32 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>654.10 (n/a)</td><td>518.46 (n/a)</td><td>584.30 (n/a)</td><td>233.90 (n/a)</td><td>167.45 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.61 <b>(+22.71%)</b></td><td>0.37 (+1.72%)</td><td>0.47 <b>(+23.51%)</b></td><td>0.05 <b>(-79.37%)</b></td><td>0.22 <b>(+147.41%)</b></td><td>2454.20 <b>(+384.83%)</b></td><td>751.96 <b>(+100.20%)</b></td><td>279.00 (-19.04%)</td><td>216.30 (-18.50%)</td><td>960.20 <b>(+930.48%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.49 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>506.20 (n/a)</td><td>375.60 (n/a)</td><td>344.60 (n/a)</td><td>265.40 (n/a)</td><td>93.18 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.43 (-16.39%)</td><td>0.31 (-7.91%)</td><td>0.28 (+4.71%)</td><td>0.19 (+6.35%)</td><td>0.11 <b>(-25.21%)</b></td><td>678.70 (-5.97%)</td><td>465.46 (+2.92%)</td><td>470.20 (-4.49%)</td><td>303.50 (+19.63%)</td><td>164.77 (-15.27%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>721.80 (n/a)</td><td>452.26 (n/a)</td><td>492.30 (n/a)</td><td>253.70 (n/a)</td><td>194.47 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.40 <b>(-29.67%)</b></td><td>0.28 (-15.80%)</td><td>0.25 (-2.13%)</td><td>0.19 (-15.56%)</td><td>0.08 <b>(-45.15%)</b></td><td>681.20 (+18.43%)</td><td>500.74 (+12.84%)</td><td>517.10 (+2.17%)</td><td>327.90 <b>(+42.13%)</b></td><td>127.22 (-6.43%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.57 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>575.20 (n/a)</td><td>443.76 (n/a)</td><td>506.10 (n/a)</td><td>230.70 (n/a)</td><td>135.96 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+63.64%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+389.90%)</b></td><td>22505.83 (+9.92%)</td><td>14463.65 (-19.30%)</td><td>17413.63 (+2.59%)</td><td>6381.66 <b>(-59.05%)</b></td><td>7513.75 <b>(+267.91%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20474.01 (n/a)</td><td>17921.90 (n/a)</td><td>16973.57 (n/a)</td><td>15584.75 (n/a)</td><td>2042.26 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+20.00%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+95.79%)</b></td><td>20981.17 (+0.19%)</td><td>16306.88 (-6.30%)</td><td>18118.56 (-5.95%)</td><td>6799.03 <b>(-32.50%)</b></td><td>5846.48 <b>(+36.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20941.47 (n/a)</td><td>17402.61 (n/a)</td><td>19265.13 (n/a)</td><td>10072.64 (n/a)</td><td>4293.97 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>0.13 (-3.82%)</td><td>0.09 (-6.71%)</td><td>0.07 (-8.56%)</td><td>0.07 (-2.70%)</td><td>0.03 (-1.22%)</td><td>29097.79 (+2.79%)</td><td>25810.92 (+7.46%)</td><td>28045.21 (+9.38%)</td><td>16003.70 (+3.96%)</td><td>5532.07 (+5.05%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28309.06 (n/a)</td><td>24018.04 (n/a)</td><td>25639.76 (n/a)</td><td>15394.14 (n/a)</td><td>5266.30 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>1.61 (+0.57%)</td><td>0.82 <b>(-37.94%)</b></td><td>0.75 <b>(-50.49%)</b></td><td>0.15 <b>(-81.90%)</b></td><td>0.54 <b>(+66.59%)</b></td><td>3429.00 <b>(+452.44%)</b></td><td>1169.80 <b>(+178.70%)</b></td><td>701.10 <b>(+101.99%)</b></td><td>324.60 (-0.58%)</td><td>1278.65 <b>(+930.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>1.61 (n/a)</td><td>1.32 (n/a)</td><td>1.51 (n/a)</td><td>0.84 (n/a)</td><td>0.32 (n/a)</td><td>620.70 (n/a)</td><td>419.74 (n/a)</td><td>347.10 (n/a)</td><td>326.50 (n/a)</td><td>124.06 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>2.60 (+1.14%)</td><td>1.84 (+1.24%)</td><td>1.70 (-16.42%)</td><td>0.98 <b>(+207.83%)</b></td><td>0.72 <b>(-20.13%)</b></td><td>1071.50 <b>(-67.51%)</b></td><td>654.68 <b>(-37.79%)</b></td><td>616.90 (+19.65%)</td><td>402.70 (-1.13%)</td><td>279.06 <b>(-77.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>2.57 (n/a)</td><td>1.82 (n/a)</td><td>2.03 (n/a)</td><td>0.32 (n/a)</td><td>0.90 (n/a)</td><td>3298.30 (n/a)</td><td>1052.42 (n/a)</td><td>515.60 (n/a)</td><td>407.30 (n/a)</td><td>1258.02 (n/a)</td>
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
<td><code>4d5b214</code> — 2026-08-28 20:52:08</td><td>1.65 (-15.96%)</td><td>1.15 (-5.19%)</td><td>1.05 (+8.22%)</td><td>0.75 (-16.91%)</td><td>0.37 (-17.07%)</td><td>700.80 <b>(+20.37%)</b></td><td>493.48 (+5.23%)</td><td>498.90 (-7.59%)</td><td>318.20 (+19.00%)</td><td>154.03 (+17.70%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>1.96 (n/a)</td><td>1.22 (n/a)</td><td>0.97 (n/a)</td><td>0.90 (n/a)</td><td>0.44 (n/a)</td><td>582.20 (n/a)</td><td>468.96 (n/a)</td><td>539.90 (n/a)</td><td>267.40 (n/a)</td><td>130.87 (n/a)</td>
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
