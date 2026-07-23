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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (+18.48%)</td><td>0.04 <b>(+28.22%)</b></td><td>0.04 <b>(+69.76%)</b></td><td>0.03 <b>(+32.24%)</b></td><td>0.01 (+1.32%)</td><td>457.60 <b>(-24.38%)</b></td><td>342.90 <b>(-24.26%)</b></td><td>289.10 <b>(-41.10%)</b></td><td>236.40 (-15.60%)</td><td>106.02 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.10 (n/a)</td><td>452.76 (n/a)</td><td>490.80 (n/a)</td><td>280.10 (n/a)</td><td>152.20 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 <b>(-46.46%)</b></td><td>0.03 <b>(-24.51%)</b></td><td>0.03 <b>(-27.43%)</b></td><td>0.02 (+4.12%)</td><td>0.01 <b>(-64.89%)</b></td><td>506.00 (-3.95%)</td><td>373.52 (+10.90%)</td><td>366.80 <b>(+37.79%)</b></td><td>259.00 <b>(+86.73%)</b></td><td>98.51 <b>(-40.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>526.80 (n/a)</td><td>336.82 (n/a)</td><td>266.20 (n/a)</td><td>138.70 (n/a)</td><td>166.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (-18.38%)</td><td>0.04 (-7.84%)</td><td>0.04 (+2.91%)</td><td>0.02 <b>(+26.63%)</b></td><td>0.01 (-10.23%)</td><td>524.90 <b>(-21.03%)</b></td><td>358.20 (+4.76%)</td><td>283.80 (-2.84%)</td><td>231.80 <b>(+22.52%)</b></td><td>150.82 (-18.78%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>664.70 (n/a)</td><td>341.92 (n/a)</td><td>292.10 (n/a)</td><td>189.20 (n/a)</td><td>185.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (-18.59%)</td><td>0.02 (+9.03%)</td><td>0.02 <b>(+42.96%)</b></td><td>0.01 (+0.32%)</td><td>0.00 <b>(-38.34%)</b></td><td>511.30 (-0.31%)</td><td>360.68 (-13.36%)</td><td>344.60 <b>(-30.04%)</b></td><td>267.10 <b>(+22.86%)</b></td><td>96.00 <b>(-25.38%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>512.90 (n/a)</td><td>416.30 (n/a)</td><td>492.60 (n/a)</td><td>217.40 (n/a)</td><td>128.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (-18.23%)</td><td>0.02 <b>(+39.71%)</b></td><td>0.02 <b>(+55.15%)</b></td><td>0.01 <b>(+354.41%)</b></td><td>0.00 <b>(-58.14%)</b></td><td>448.20 <b>(-77.99%)</b></td><td>322.88 <b>(-57.38%)</b></td><td>287.50 <b>(-35.54%)</b></td><td>260.40 <b>(+22.25%)</b></td><td>77.65 <b>(-89.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2036.60 (n/a)</td><td>757.66 (n/a)</td><td>446.00 (n/a)</td><td>213.00 (n/a)</td><td>738.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (+19.98%)</td><td>0.01 (-2.71%)</td><td>0.01 <b>(-24.17%)</b></td><td>0.01 <b>(-41.61%)</b></td><td>0.01 <b>(+143.37%)</b></td><td>830.90 <b>(+71.28%)</b></td><td>510.52 <b>(+20.64%)</b></td><td>574.00 <b>(+31.86%)</b></td><td>259.60 (-16.63%)</td><td>233.20 <b>(+230.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.10 (n/a)</td><td>423.18 (n/a)</td><td>435.30 (n/a)</td><td>311.40 (n/a)</td><td>70.57 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 <b>(+44.89%)</b></td><td>0.02 (-3.37%)</td><td>0.01 <b>(-43.26%)</b></td><td>0.01 <b>(-28.43%)</b></td><td>0.01 <b>(+201.08%)</b></td><td>588.90 <b>(+39.75%)</b></td><td>391.00 <b>(+28.69%)</b></td><td>486.20 <b>(+76.22%)</b></td><td>168.70 <b>(-30.97%)</b></td><td>189.13 <b>(+174.69%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>421.40 (n/a)</td><td>303.82 (n/a)</td><td>275.90 (n/a)</td><td>244.40 (n/a)</td><td>68.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (-4.42%)</td><td>0.02 (+17.90%)</td><td>0.02 <b>(+40.70%)</b></td><td>0.01 (+17.31%)</td><td>0.00 <b>(-22.14%)</b></td><td>470.60 (-14.76%)</td><td>327.62 (-17.63%)</td><td>301.30 <b>(-28.94%)</b></td><td>270.00 (+4.65%)</td><td>82.48 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.10 (n/a)</td><td>397.76 (n/a)</td><td>424.00 (n/a)</td><td>258.00 (n/a)</td><td>114.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.01 (-7.22%)</td><td>0.01 (-13.92%)</td><td>0.01 (-11.85%)</td><td>0.01 <b>(-25.76%)</b></td><td>0.00 <b>(+22.46%)</b></td><td>776.10 <b>(+34.69%)</b></td><td>560.88 (+19.20%)</td><td>529.60 (+13.43%)</td><td>396.30 (+7.78%)</td><td>140.81 <b>(+80.44%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.20 (n/a)</td><td>470.52 (n/a)</td><td>466.90 (n/a)</td><td>367.70 (n/a)</td><td>78.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.20 (n/a)</td><td>446.26 (n/a)</td><td>506.60 (n/a)</td><td>226.00 (n/a)</td><td>128.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>553.40 (n/a)</td><td>378.86 (n/a)</td><td>441.80 (n/a)</td><td>139.50 (n/a)</td><td>185.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1216.80 (n/a)</td><td>724.52 (n/a)</td><td>583.30 (n/a)</td><td>300.50 (n/a)</td><td>394.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>596.40 (n/a)</td><td>446.44 (n/a)</td><td>527.20 (n/a)</td><td>262.70 (n/a)</td><td>154.96 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>570.80 (n/a)</td><td>453.84 (n/a)</td><td>490.00 (n/a)</td><td>245.40 (n/a)</td><td>127.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>637.30 (n/a)</td><td>516.28 (n/a)</td><td>550.00 (n/a)</td><td>272.30 (n/a)</td><td>146.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>430.50 (n/a)</td><td>348.84 (n/a)</td><td>359.40 (n/a)</td><td>225.70 (n/a)</td><td>88.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>460.90 (n/a)</td><td>380.28 (n/a)</td><td>353.50 (n/a)</td><td>326.10 (n/a)</td><td>57.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.70 (n/a)</td><td>376.26 (n/a)</td><td>380.70 (n/a)</td><td>220.90 (n/a)</td><td>133.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1115.60 (n/a)</td><td>553.10 (n/a)</td><td>428.10 (n/a)</td><td>274.10 (n/a)</td><td>333.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.20 (n/a)</td><td>479.34 (n/a)</td><td>586.30 (n/a)</td><td>267.40 (n/a)</td><td>168.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.70 (n/a)</td><td>562.42 (n/a)</td><td>571.00 (n/a)</td><td>478.90 (n/a)</td><td>56.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.68 <b>(+83.23%)</b></td><td>0.42 <b>(+26.80%)</b></td><td>0.36 (-0.50%)</td><td>0.26 <b>(+21.53%)</b></td><td>0.16 <b>(+146.38%)</b></td><td>850.20 (-17.72%)</td><td>584.22 (-16.26%)</td><td>622.40 (+0.48%)</td><td>324.00 <b>(-45.43%)</b></td><td>195.50 (+3.97%)</td><td>29.12 <b>(+83.23%)</b></td><td>17.92 <b>(+26.80%)</b></td><td>15.16 (-0.50%)</td><td>11.10 <b>(+21.53%)</b></td><td>6.93 <b>(+146.38%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>1033.30 (n/a)</td><td>697.62 (n/a)</td><td>619.40 (n/a)</td><td>593.70 (n/a)</td><td>188.04 (n/a)</td><td>15.89 (n/a)</td><td>14.13 (n/a)</td><td>15.24 (n/a)</td><td>9.13 (n/a)</td><td>2.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.55 (+10.12%)</td><td>0.46 (+5.73%)</td><td>0.47 (+13.19%)</td><td>0.35 (-3.25%)</td><td>0.09 <b>(+51.68%)</b></td><td>636.10 (+3.36%)</td><td>500.66 (-3.78%)</td><td>472.80 (-11.66%)</td><td>398.90 (-9.18%)</td><td>101.69 <b>(+43.89%)</b></td><td>23.66 (+10.12%)</td><td>19.46 (+5.73%)</td><td>19.96 (+13.19%)</td><td>14.84 (-3.25%)</td><td>3.79 <b>(+51.68%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>615.40 (n/a)</td><td>520.34 (n/a)</td><td>535.20 (n/a)</td><td>439.20 (n/a)</td><td>70.67 (n/a)</td><td>21.49 (n/a)</td><td>18.41 (n/a)</td><td>17.63 (n/a)</td><td>15.34 (n/a)</td><td>2.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.31 (-1.23%)</td><td>0.30 (-0.66%)</td><td>0.30 (-0.75%)</td><td>0.30 (+0.36%)</td><td>0.00 <b>(-56.59%)</b></td><td>83435.40 (-0.36%)</td><td>82973.98 (+0.66%)</td><td>83034.70 (+0.75%)</td><td>82398.00 (+1.24%)</td><td>372.86 <b>(-56.28%)</b></td><td>208.50 (-1.23%)</td><td>207.05 (-0.66%)</td><td>206.90 (-0.75%)</td><td>205.91 (+0.36%)</td><td>0.93 <b>(-56.59%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83736.50 (n/a)</td><td>82433.08 (n/a)</td><td>82414.90 (n/a)</td><td>81386.30 (n/a)</td><td>852.92 (n/a)</td><td>211.09 (n/a)</td><td>208.43 (n/a)</td><td>208.46 (n/a)</td><td>205.17 (n/a)</td><td>2.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>1.02 (-0.57%)</td><td>1.00 (-1.82%)</td><td>1.00 (-2.50%)</td><td>0.98 (-2.15%)</td><td>0.02 <b>(+40.24%)</b></td><td>25740.70 (+2.20%)</td><td>25221.58 (+1.86%)</td><td>25284.20 (+2.56%)</td><td>24634.10 (+0.57%)</td><td>396.19 <b>(+43.84%)</b></td><td>697.40 (-0.57%)</td><td>681.29 (-1.82%)</td><td>679.47 (-2.50%)</td><td>667.42 (-2.15%)</td><td>10.75 <b>(+40.24%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25186.40 (n/a)</td><td>24761.20 (n/a)</td><td>24652.60 (n/a)</td><td>24493.90 (n/a)</td><td>275.44 (n/a)</td><td>701.39 (n/a)</td><td>693.89 (n/a)</td><td>696.88 (n/a)</td><td>682.11 (n/a)</td><td>7.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.91 (+2.43%)</td><td>2.82 (+7.52%)</td><td>3.38 <b>(+59.18%)</b></td><td>1.26 <b>(-21.02%)</b></td><td>1.10 (+12.21%)</td><td>6396.70 <b>(+26.61%)</b></td><td>3401.30 (-0.88%)</td><td>2381.70 <b>(-37.18%)</b></td><td>2063.60 (-2.37%)</td><td>1809.33 <b>(+47.58%)</b></td><td>1024.38 (+2.43%)</td><td>739.52 (+7.52%)</td><td>887.59 <b>(+59.18%)</b></td><td>330.47 <b>(-21.02%)</b></td><td>287.84 (+12.21%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>3.81 (n/a)</td><td>2.62 (n/a)</td><td>2.13 (n/a)</td><td>1.60 (n/a)</td><td>0.98 (n/a)</td><td>5052.20 (n/a)</td><td>3431.40 (n/a)</td><td>3791.10 (n/a)</td><td>2113.70 (n/a)</td><td>1225.96 (n/a)</td><td>1000.11 (n/a)</td><td>687.77 (n/a)</td><td>557.60 (n/a)</td><td>418.42 (n/a)</td><td>256.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.32 (+6.55%)</td><td>0.22 (-7.87%)</td><td>0.21 (-11.11%)</td><td>0.18 (+1.89%)</td><td>0.05 <b>(+20.26%)</b></td><td>6886.40 (-1.85%)</td><td>5836.70 (+9.41%)</td><td>6051.70 (+12.50%)</td><td>3929.40 (-6.15%)</td><td>1124.66 (+4.61%)</td><td>17.08 (+6.55%)</td><td>11.95 (-7.87%)</td><td>11.09 (-11.11%)</td><td>9.75 (+1.89%)</td><td>2.93 <b>(+20.26%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>7016.30 (n/a)</td><td>5334.86 (n/a)</td><td>5379.50 (n/a)</td><td>4187.00 (n/a)</td><td>1075.07 (n/a)</td><td>16.03 (n/a)</td><td>12.97 (n/a)</td><td>12.47 (n/a)</td><td>9.56 (n/a)</td><td>2.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.08 <b>(-44.38%)</b></td><td>0.06 <b>(-42.57%)</b></td><td>0.06 <b>(-45.20%)</b></td><td>0.06 (-10.57%)</td><td>0.01 <b>(-70.43%)</b></td><td>0.08 <b>(-44.38%)</b></td><td>0.06 <b>(-42.57%)</b></td><td>0.06 <b>(-45.20%)</b></td><td>0.06 (-10.57%)</td><td>0.01 <b>(-70.43%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.76 (+5.96%)</td><td>3.61 (+4.36%)</td><td>3.67 (+6.06%)</td><td>3.39 (+2.16%)</td><td>0.17 <b>(+85.98%)</b></td><td>3.76 (+5.96%)</td><td>3.60 (+4.36%)</td><td>3.66 (+6.06%)</td><td>3.39 (+2.16%)</td><td>0.17 <b>(+85.98%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>3.55 (n/a)</td><td>3.46 (n/a)</td><td>3.46 (n/a)</td><td>3.32 (n/a)</td><td>0.09 (n/a)</td><td>3.55 (n/a)</td><td>3.45 (n/a)</td><td>3.45 (n/a)</td><td>3.31 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>7.01 (-6.33%)</td><td>6.52 (+2.89%)</td><td>6.72 (+8.13%)</td><td>5.62 (-1.06%)</td><td>0.55 <b>(-25.51%)</b></td><td>7.00 (-6.33%)</td><td>6.51 (+2.89%)</td><td>6.71 (+8.13%)</td><td>5.62 (-1.06%)</td><td>0.55 <b>(-25.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>7.48 (n/a)</td><td>6.33 (n/a)</td><td>6.21 (n/a)</td><td>5.68 (n/a)</td><td>0.73 (n/a)</td><td>7.48 (n/a)</td><td>6.33 (n/a)</td><td>6.21 (n/a)</td><td>5.68 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>9.89 <b>(-28.63%)</b></td><td>8.16 <b>(-23.81%)</b></td><td>8.13 <b>(-22.97%)</b></td><td>6.23 (-17.68%)</td><td>1.47 <b>(-49.94%)</b></td><td>9.89 <b>(-28.63%)</b></td><td>8.16 <b>(-23.81%)</b></td><td>8.12 <b>(-22.97%)</b></td><td>6.22 (-17.68%)</td><td>1.46 <b>(-49.94%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>13.86 (n/a)</td><td>10.71 (n/a)</td><td>10.55 (n/a)</td><td>7.56 (n/a)</td><td>2.93 (n/a)</td><td>13.85 (n/a)</td><td>10.71 (n/a)</td><td>10.54 (n/a)</td><td>7.56 (n/a)</td><td>2.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.76 (-4.28%)</td><td>3.60 (-3.22%)</td><td>3.65 (-3.86%)</td><td>3.35 (+2.29%)</td><td>0.17 <b>(-35.02%)</b></td><td>3.76 (-4.28%)</td><td>3.60 (-3.22%)</td><td>3.65 (-3.86%)</td><td>3.35 (+2.29%)</td><td>0.17 <b>(-35.02%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>3.93 (n/a)</td><td>3.72 (n/a)</td><td>3.80 (n/a)</td><td>3.27 (n/a)</td><td>0.26 (n/a)</td><td>3.93 (n/a)</td><td>3.72 (n/a)</td><td>3.80 (n/a)</td><td>3.27 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>7.27 (-2.83%)</td><td>6.51 (-1.97%)</td><td>6.58 (-2.78%)</td><td>5.54 (-3.19%)</td><td>0.63 (-6.32%)</td><td>7.26 (-2.83%)</td><td>6.50 (-1.97%)</td><td>6.58 (-2.78%)</td><td>5.53 (-3.19%)</td><td>0.63 (-6.32%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>7.48 (n/a)</td><td>6.64 (n/a)</td><td>6.77 (n/a)</td><td>5.72 (n/a)</td><td>0.67 (n/a)</td><td>7.48 (n/a)</td><td>6.63 (n/a)</td><td>6.77 (n/a)</td><td>5.71 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>13.98 <b>(+25.02%)</b></td><td>8.99 (-8.70%)</td><td>7.74 <b>(-27.36%)</b></td><td>7.37 (-8.63%)</td><td>2.83 <b>(+99.76%)</b></td><td>13.97 <b>(+25.02%)</b></td><td>8.99 (-8.70%)</td><td>7.73 <b>(-27.36%)</b></td><td>7.36 (-8.63%)</td><td>2.82 <b>(+99.76%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>11.18 (n/a)</td><td>9.85 (n/a)</td><td>10.65 (n/a)</td><td>8.06 (n/a)</td><td>1.41 (n/a)</td><td>11.18 (n/a)</td><td>9.84 (n/a)</td><td>10.64 (n/a)</td><td>8.06 (n/a)</td><td>1.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.21 (+1.94%)</td><td>2.64 (+8.84%)</td><td>3.02 (+6.87%)</td><td>1.10 (-2.18%)</td><td>0.87 (+5.12%)</td><td>3.21 (+1.94%)</td><td>2.63 (+8.84%)</td><td>3.01 (+6.87%)</td><td>1.10 (-2.18%)</td><td>0.87 (+5.12%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>3.15 (n/a)</td><td>2.42 (n/a)</td><td>2.82 (n/a)</td><td>1.13 (n/a)</td><td>0.83 (n/a)</td><td>3.14 (n/a)</td><td>2.42 (n/a)</td><td>2.82 (n/a)</td><td>1.13 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.54 (+15.72%)</td><td>0.35 (+9.22%)</td><td>0.46 <b>(+31.23%)</b></td><td>0.08 <b>(-39.52%)</b></td><td>0.20 <b>(+38.32%)</b></td><td>0.53 (+15.72%)</td><td>0.35 (+9.22%)</td><td>0.45 <b>(+31.23%)</b></td><td>0.08 <b>(-39.52%)</b></td><td>0.19 <b>(+38.32%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.68 (+7.54%)</td><td>0.48 (-4.01%)</td><td>0.62 (+6.23%)</td><td>0.08 (+8.40%)</td><td>0.25 (+5.13%)</td><td>0.67 (+7.54%)</td><td>0.47 (-4.01%)</td><td>0.61 (+6.23%)</td><td>0.08 (+8.40%)</td><td>0.25 (+5.13%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.63 (n/a)</td><td>0.50 (n/a)</td><td>0.58 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.62 (n/a)</td><td>0.49 (n/a)</td><td>0.58 (n/a)</td><td>0.07 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>2.04 (-9.80%)</td><td>1.08 <b>(-37.03%)</b></td><td>0.80 <b>(-49.97%)</b></td><td>0.42 <b>(-62.43%)</b></td><td>0.66 <b>(+46.60%)</b></td><td>2.01 (-9.80%)</td><td>1.06 <b>(-37.03%)</b></td><td>0.79 <b>(-49.97%)</b></td><td>0.41 <b>(-62.43%)</b></td><td>0.65 <b>(+46.60%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>2.27 (n/a)</td><td>1.72 (n/a)</td><td>1.60 (n/a)</td><td>1.11 (n/a)</td><td>0.45 (n/a)</td><td>2.23 (n/a)</td><td>1.69 (n/a)</td><td>1.57 (n/a)</td><td>1.10 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.30 (n/a)</td><td>346.78 (n/a)</td><td>289.20 (n/a)</td><td>238.20 (n/a)</td><td>123.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.30 (n/a)</td><td>421.98 (n/a)</td><td>484.50 (n/a)</td><td>235.40 (n/a)</td><td>159.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1944.40 (n/a)</td><td>718.06 (n/a)</td><td>516.90 (n/a)</td><td>270.60 (n/a)</td><td>700.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.50 (n/a)</td><td>356.80 (n/a)</td><td>296.40 (n/a)</td><td>231.60 (n/a)</td><td>123.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.80 (n/a)</td><td>411.80 (n/a)</td><td>352.60 (n/a)</td><td>268.40 (n/a)</td><td>159.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2058.70 (n/a)</td><td>792.14 (n/a)</td><td>527.50 (n/a)</td><td>252.80 (n/a)</td><td>720.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (+5.00%)</td><td>0.03 (-3.68%)</td><td>0.03 (-6.74%)</td><td>0.02 (+10.66%)</td><td>0.01 (+0.79%)</td><td>520.90 (-9.63%)</td><td>344.28 (+2.42%)</td><td>288.50 (+7.21%)</td><td>234.60 (-4.79%)</td><td>117.18 (-14.86%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.40 (n/a)</td><td>336.14 (n/a)</td><td>269.10 (n/a)</td><td>246.40 (n/a)</td><td>137.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 <b>(+31.39%)</b></td><td>0.03 (+11.86%)</td><td>0.02 (-8.47%)</td><td>0.02 (-11.60%)</td><td>0.01 <b>(+142.65%)</b></td><td>490.90 (+13.11%)</td><td>356.54 (-0.17%)</td><td>408.70 (+9.25%)</td><td>199.70 <b>(-23.89%)</b></td><td>134.97 <b>(+111.98%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>434.00 (n/a)</td><td>357.16 (n/a)</td><td>374.10 (n/a)</td><td>262.40 (n/a)</td><td>63.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (-17.04%)</td><td>0.02 (-15.05%)</td><td>0.02 (-0.33%)</td><td>0.02 (+6.37%)</td><td>0.01 <b>(-44.86%)</b></td><td>512.40 (-5.98%)</td><td>443.90 (+8.63%)</td><td>482.00 (+0.33%)</td><td>290.50 <b>(+20.54%)</b></td><td>92.76 <b>(-37.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.00 (n/a)</td><td>408.62 (n/a)</td><td>480.40 (n/a)</td><td>241.00 (n/a)</td><td>147.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (-7.74%)</td><td>0.02 (+2.98%)</td><td>0.02 (+4.98%)</td><td>0.01 <b>(+238.26%)</b></td><td>0.01 <b>(-38.80%)</b></td><td>590.40 <b>(-70.44%)</b></td><td>448.14 <b>(-37.32%)</b></td><td>459.10 (-4.73%)</td><td>264.00 (+8.37%)</td><td>132.47 <b>(-81.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1997.20 (n/a)</td><td>714.94 (n/a)</td><td>481.90 (n/a)</td><td>243.60 (n/a)</td><td>727.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (+17.86%)</td><td>0.02 (+6.80%)</td><td>0.02 <b>(-20.79%)</b></td><td>0.01 (-7.66%)</td><td>0.01 <b>(+101.88%)</b></td><td>569.10 (+8.32%)</td><td>425.52 (+2.13%)</td><td>512.90 <b>(+26.27%)</b></td><td>258.60 (-15.16%)</td><td>151.37 <b>(+78.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>525.40 (n/a)</td><td>416.66 (n/a)</td><td>406.20 (n/a)</td><td>304.80 (n/a)</td><td>85.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (-2.52%)</td><td>0.03 <b>(+47.02%)</b></td><td>0.03 <b>(+78.20%)</b></td><td>0.01 <b>(+126.36%)</b></td><td>0.01 <b>(-29.13%)</b></td><td>578.50 <b>(-55.82%)</b></td><td>345.94 <b>(-44.75%)</b></td><td>302.30 <b>(-43.87%)</b></td><td>235.20 (+2.62%)</td><td>135.49 <b>(-66.52%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1309.50 (n/a)</td><td>626.08 (n/a)</td><td>538.60 (n/a)</td><td>229.20 (n/a)</td><td>404.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 <b>(+53.86%)</b></td><td>0.02 (+14.31%)</td><td>0.02 (-3.57%)</td><td>0.01 (-8.31%)</td><td>0.01 <b>(+169.01%)</b></td><td>699.20 (+9.06%)</td><td>484.96 (-5.30%)</td><td>510.60 (+3.72%)</td><td>263.70 <b>(-35.02%)</b></td><td>157.61 <b>(+80.01%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.10 (n/a)</td><td>512.08 (n/a)</td><td>492.30 (n/a)</td><td>405.80 (n/a)</td><td>87.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 <b>(+47.29%)</b></td><td>0.02 (+4.84%)</td><td>0.01 <b>(-29.80%)</b></td><td>0.01 <b>(-20.67%)</b></td><td>0.01 <b>(+171.86%)</b></td><td>675.20 <b>(+26.04%)</b></td><td>476.08 (+12.38%)</td><td>554.60 <b>(+42.46%)</b></td><td>225.70 <b>(-32.10%)</b></td><td>208.18 <b>(+133.18%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>535.70 (n/a)</td><td>423.62 (n/a)</td><td>389.30 (n/a)</td><td>332.40 (n/a)</td><td>89.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (-16.89%)</td><td>0.02 <b>(-22.37%)</b></td><td>0.02 <b>(-29.50%)</b></td><td>0.01 (-12.88%)</td><td>0.01 (-19.98%)</td><td>579.00 (+14.79%)</td><td>487.66 <b>(+27.06%)</b></td><td>510.50 <b>(+41.84%)</b></td><td>287.40 <b>(+20.35%)</b></td><td>115.83 (+0.54%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.40 (n/a)</td><td>383.80 (n/a)</td><td>359.90 (n/a)</td><td>238.80 (n/a)</td><td>115.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (-4.13%)</td><td>0.03 (+17.73%)</td><td>0.04 <b>(+60.56%)</b></td><td>0.02 (+2.76%)</td><td>0.01 (+3.12%)</td><td>477.10 (-2.69%)</td><td>304.80 (-14.64%)</td><td>233.60 <b>(-37.72%)</b></td><td>227.70 (+4.31%)</td><td>110.09 (+1.74%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.30 (n/a)</td><td>357.08 (n/a)</td><td>375.10 (n/a)</td><td>218.30 (n/a)</td><td>108.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (+12.68%)</td><td>0.02 (+7.19%)</td><td>0.03 <b>(+41.93%)</b></td><td>0.01 (-18.33%)</td><td>0.01 <b>(+61.24%)</b></td><td>587.60 <b>(+22.44%)</b></td><td>389.26 (+3.53%)</td><td>294.70 <b>(-29.53%)</b></td><td>227.90 (-11.25%)</td><td>176.90 <b>(+90.74%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.90 (n/a)</td><td>376.00 (n/a)</td><td>418.20 (n/a)</td><td>256.80 (n/a)</td><td>92.75 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 <b>(-25.44%)</b></td><td>0.02 <b>(-37.26%)</b></td><td>0.02 <b>(-45.39%)</b></td><td>0.01 <b>(-28.96%)</b></td><td>0.01 <b>(-35.07%)</b></td><td>724.50 <b>(+40.76%)</b></td><td>517.20 <b>(+53.11%)</b></td><td>528.30 <b>(+83.12%)</b></td><td>268.30 <b>(+34.08%)</b></td><td>166.33 (+13.54%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.70 (n/a)</td><td>337.80 (n/a)</td><td>288.50 (n/a)</td><td>200.10 (n/a)</td><td>146.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (-10.63%)</td><td>0.02 (+3.52%)</td><td>0.03 <b>(+41.23%)</b></td><td>0.01 (-4.89%)</td><td>0.01 (-9.01%)</td><td>597.80 (+5.14%)</td><td>385.58 (-3.71%)</td><td>313.80 <b>(-29.20%)</b></td><td>261.60 (+11.94%)</td><td>151.95 (+6.40%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.60 (n/a)</td><td>400.42 (n/a)</td><td>443.20 (n/a)</td><td>233.70 (n/a)</td><td>142.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (+0.04%)</td><td>0.01 (-12.72%)</td><td>0.01 (-1.21%)</td><td>0.00 <b>(-69.01%)</b></td><td>0.01 <b>(+77.08%)</b></td><td>2092.70 <b>(+222.75%)</b></td><td>820.92 <b>(+58.06%)</b></td><td>546.30 (+1.22%)</td><td>358.90 (-0.06%)</td><td>716.22 <b>(+588.24%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.40 (n/a)</td><td>519.36 (n/a)</td><td>539.70 (n/a)</td><td>359.10 (n/a)</td><td>104.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (-2.32%)</td><td>0.03 (-16.19%)</td><td>0.03 <b>(-20.27%)</b></td><td>0.01 <b>(-37.52%)</b></td><td>0.01 <b>(+50.64%)</b></td><td>591.90 <b>(+60.06%)</b></td><td>357.44 <b>(+27.31%)</b></td><td>326.70 <b>(+25.41%)</b></td><td>241.20 (+2.38%)</td><td>136.04 <b>(+157.18%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>369.80 (n/a)</td><td>280.76 (n/a)</td><td>260.50 (n/a)</td><td>235.60 (n/a)</td><td>52.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 <b>(-22.44%)</b></td><td>0.03 (-0.86%)</td><td>0.03 <b>(+25.37%)</b></td><td>0.02 (+14.27%)</td><td>0.01 <b>(-50.56%)</b></td><td>523.00 (-12.48%)</td><td>432.90 (-7.13%)</td><td>431.80 <b>(-20.23%)</b></td><td>324.50 <b>(+28.97%)</b></td><td>85.79 <b>(-45.08%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>597.60 (n/a)</td><td>466.14 (n/a)</td><td>541.30 (n/a)</td><td>251.60 (n/a)</td><td>156.20 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (+6.97%)</td><td>0.03 (+17.85%)</td><td>0.03 <b>(+66.87%)</b></td><td>0.01 (-2.62%)</td><td>0.01 (+14.03%)</td><td>562.80 (+2.68%)</td><td>363.32 (-13.26%)</td><td>295.80 <b>(-40.07%)</b></td><td>231.60 (-6.54%)</td><td>155.07 (+6.49%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.10 (n/a)</td><td>418.86 (n/a)</td><td>493.60 (n/a)</td><td>247.80 (n/a)</td><td>145.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 <b>(-50.44%)</b></td><td>0.02 <b>(-39.35%)</b></td><td>0.02 <b>(-42.10%)</b></td><td>0.02 (-10.79%)</td><td>0.01 <b>(-64.42%)</b></td><td>613.20 (+12.10%)</td><td>496.94 <b>(+44.23%)</b></td><td>516.70 <b>(+72.69%)</b></td><td>299.00 <b>(+101.75%)</b></td><td>118.05 <b>(-22.71%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>547.00 (n/a)</td><td>344.54 (n/a)</td><td>299.20 (n/a)</td><td>148.20 (n/a)</td><td>152.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (-0.36%)</td><td>0.02 (-10.72%)</td><td>0.02 <b>(-29.49%)</b></td><td>0.01 (+2.47%)</td><td>0.01 (+16.53%)</td><td>670.00 (-2.42%)</td><td>444.28 (+17.22%)</td><td>403.60 <b>(+41.81%)</b></td><td>236.00 (+0.38%)</td><td>209.58 (+13.70%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>686.60 (n/a)</td><td>379.02 (n/a)</td><td>284.60 (n/a)</td><td>235.10 (n/a)</td><td>184.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (-0.90%)</td><td>0.03 (-17.84%)</td><td>0.02 <b>(-44.55%)</b></td><td>0.02 (-11.47%)</td><td>0.01 (+14.63%)</td><td>663.30 (+12.96%)</td><td>477.22 <b>(+29.01%)</b></td><td>583.20 <b>(+80.33%)</b></td><td>236.30 (+0.90%)</td><td>195.13 <b>(+33.29%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>587.20 (n/a)</td><td>369.90 (n/a)</td><td>323.40 (n/a)</td><td>234.20 (n/a)</td><td>146.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (+18.43%)</td><td>0.03 <b>(+30.03%)</b></td><td>0.03 <b>(+33.96%)</b></td><td>0.02 <b>(+44.28%)</b></td><td>0.01 (+3.71%)</td><td>394.10 <b>(-30.69%)</b></td><td>274.00 <b>(-25.01%)</b></td><td>244.60 <b>(-25.36%)</b></td><td>219.10 (-15.54%)</td><td>70.55 <b>(-40.87%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.60 (n/a)</td><td>365.40 (n/a)</td><td>327.70 (n/a)</td><td>259.40 (n/a)</td><td>119.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (-14.29%)</td><td>0.02 (-14.30%)</td><td>0.02 (-9.58%)</td><td>0.01 <b>(-33.80%)</b></td><td>0.01 <b>(+29.45%)</b></td><td>973.70 <b>(+51.05%)</b></td><td>594.10 <b>(+24.18%)</b></td><td>514.10 (+10.58%)</td><td>417.40 (+16.66%)</td><td>230.23 <b>(+121.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>644.60 (n/a)</td><td>478.40 (n/a)</td><td>464.90 (n/a)</td><td>357.80 (n/a)</td><td>104.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (+9.24%)</td><td>0.03 (+14.60%)</td><td>0.03 <b>(+47.84%)</b></td><td>0.02 (+3.94%)</td><td>0.01 <b>(+25.56%)</b></td><td>457.20 (-3.81%)</td><td>336.22 (-10.59%)</td><td>287.30 <b>(-32.35%)</b></td><td>237.30 (-8.45%)</td><td>108.39 (+15.90%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.30 (n/a)</td><td>376.04 (n/a)</td><td>424.70 (n/a)</td><td>259.20 (n/a)</td><td>93.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 <b>(-33.40%)</b></td><td>0.02 <b>(-24.32%)</b></td><td>0.02 <b>(-29.96%)</b></td><td>0.02 <b>(+44.75%)</b></td><td>0.00 <b>(-72.15%)</b></td><td>465.30 <b>(-30.91%)</b></td><td>431.58 (+14.19%)</td><td>452.20 <b>(+42.78%)</b></td><td>337.50 <b>(+50.20%)</b></td><td>53.22 <b>(-71.14%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.50 (n/a)</td><td>377.96 (n/a)</td><td>316.70 (n/a)</td><td>224.70 (n/a)</td><td>184.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 <b>(+34.34%)</b></td><td>0.02 (+13.98%)</td><td>0.02 <b>(+30.34%)</b></td><td>0.00 <b>(-52.09%)</b></td><td>0.01 <b>(+79.50%)</b></td><td>2075.10 <b>(+108.70%)</b></td><td>747.12 <b>(+29.13%)</b></td><td>418.60 <b>(-23.28%)</b></td><td>241.10 <b>(-25.56%)</b></td><td>753.65 <b>(+201.84%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>994.30 (n/a)</td><td>578.58 (n/a)</td><td>545.60 (n/a)</td><td>323.90 (n/a)</td><td>249.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.41 <b>(+36.06%)</b></td><td>0.25 (+3.36%)</td><td>0.21 (-10.35%)</td><td>0.19 (+2.32%)</td><td>0.09 <b>(+89.39%)</b></td><td>530.20 (-2.27%)</td><td>425.94 (+1.07%)</td><td>458.80 (+11.55%)</td><td>241.90 <b>(-26.50%)</b></td><td>109.48 <b>(+27.96%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>542.50 (n/a)</td><td>421.44 (n/a)</td><td>411.30 (n/a)</td><td>329.10 (n/a)</td><td>85.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.20 <b>(-44.29%)</b></td><td>0.15 <b>(-42.64%)</b></td><td>0.16 <b>(-46.62%)</b></td><td>0.10 <b>(-40.78%)</b></td><td>0.04 <b>(-53.96%)</b></td><td>1030.10 <b>(+68.84%)</b></td><td>693.78 <b>(+66.77%)</b></td><td>598.70 <b>(+87.33%)</b></td><td>499.40 <b>(+79.51%)</b></td><td>225.05 <b>(+35.29%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.31 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>610.10 (n/a)</td><td>416.02 (n/a)</td><td>319.60 (n/a)</td><td>278.20 (n/a)</td><td>166.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.38 <b>(-20.73%)</b></td><td>0.24 (-10.85%)</td><td>0.19 (-9.93%)</td><td>0.18 (+13.39%)</td><td>0.09 <b>(-32.41%)</b></td><td>559.80 (-11.81%)</td><td>452.24 (+4.86%)</td><td>528.10 (+11.02%)</td><td>256.70 <b>(+26.14%)</b></td><td>134.21 <b>(-20.26%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.48 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>634.80 (n/a)</td><td>431.30 (n/a)</td><td>475.70 (n/a)</td><td>203.50 (n/a)</td><td>168.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.24 (+3.11%)</td><td>0.17 (+0.41%)</td><td>0.15 (+0.23%)</td><td>0.13 (+9.33%)</td><td>0.04 (-2.70%)</td><td>578.50 (-8.52%)</td><td>469.38 (-1.32%)</td><td>490.70 (-0.22%)</td><td>308.40 (-2.99%)</td><td>106.82 (-14.07%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>632.40 (n/a)</td><td>475.66 (n/a)</td><td>491.80 (n/a)</td><td>317.90 (n/a)</td><td>124.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.24 <b>(+28.31%)</b></td><td>0.18 (+11.28%)</td><td>0.15 (+1.42%)</td><td>0.12 (-2.72%)</td><td>0.05 <b>(+64.19%)</b></td><td>600.60 (+2.79%)</td><td>441.22 (-7.25%)</td><td>476.50 (-1.41%)</td><td>301.70 <b>(-22.06%)</b></td><td>117.93 <b>(+33.42%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>584.30 (n/a)</td><td>475.72 (n/a)</td><td>483.30 (n/a)</td><td>387.10 (n/a)</td><td>88.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.25 (-9.30%)</td><td>0.17 (-10.67%)</td><td>0.15 (+7.80%)</td><td>0.13 (+0.62%)</td><td>0.04 <b>(-37.57%)</b></td><td>562.80 (-0.62%)</td><td>456.10 (+5.24%)</td><td>481.10 (-7.23%)</td><td>298.80 (+10.26%)</td><td>96.67 <b>(-33.50%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>566.30 (n/a)</td><td>433.40 (n/a)</td><td>518.60 (n/a)</td><td>271.00 (n/a)</td><td>145.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.39 (-11.34%)</td><td>0.27 (+0.87%)</td><td>0.25 (-10.89%)</td><td>0.21 <b>(+282.60%)</b></td><td>0.07 <b>(-48.78%)</b></td><td>635.90 <b>(-73.86%)</b></td><td>503.70 <b>(-38.81%)</b></td><td>527.60 (+12.23%)</td><td>334.40 (+12.78%)</td><td>112.57 <b>(-87.54%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>0.14 (n/a)</td><td>2432.90 (n/a)</td><td>823.14 (n/a)</td><td>470.10 (n/a)</td><td>296.50 (n/a)</td><td>903.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.45 (-12.14%)</td><td>0.30 (-15.33%)</td><td>0.27 <b>(-22.99%)</b></td><td>0.22 (+17.58%)</td><td>0.09 <b>(-32.53%)</b></td><td>588.80 (-14.95%)</td><td>460.74 (+10.15%)</td><td>490.10 <b>(+29.86%)</b></td><td>291.70 (+13.81%)</td><td>114.15 <b>(-35.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>692.30 (n/a)</td><td>418.28 (n/a)</td><td>377.40 (n/a)</td><td>256.30 (n/a)</td><td>177.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.47 (+9.31%)</td><td>0.37 (+17.80%)</td><td>0.39 <b>(+52.45%)</b></td><td>0.22 (+2.82%)</td><td>0.09 (-5.43%)</td><td>602.60 (-2.73%)</td><td>384.02 (-15.98%)</td><td>336.10 <b>(-34.41%)</b></td><td>277.50 (-8.51%)</td><td>127.57 (-7.18%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>619.50 (n/a)</td><td>457.04 (n/a)</td><td>512.40 (n/a)</td><td>303.30 (n/a)</td><td>137.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.00 (+16.67%)</td><td>0.00 (+7.14%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+25.00%)</b></td><td>21898.35 (-4.37%)</td><td>16517.63 (-10.51%)</td><td>18739.14 (-15.89%)</td><td>5852.25 (-13.01%)</td><td>6204.37 (-9.57%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22899.76 (n/a)</td><td>18458.31 (n/a)</td><td>22279.89 (n/a)</td><td>6727.16 (n/a)</td><td>6860.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-33.96%)</b></td><td>0.00 <b>(-58.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+10.28%)</td><td>22545.35 (-1.20%)</td><td>14954.29 <b>(+49.04%)</b></td><td>17282.65 <b>(+151.08%)</b></td><td>5886.27 (-2.80%)</td><td>6918.08 (-3.51%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22818.84 (n/a)</td><td>10033.62 (n/a)</td><td>6883.34 (n/a)</td><td>6056.00 (n/a)</td><td>7169.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.14 (-7.42%)</td><td>0.09 (-13.65%)</td><td>0.09 (-10.60%)</td><td>0.07 (-2.76%)</td><td>0.03 (-10.97%)</td><td>28354.21 (+2.83%)</td><td>23571.54 (+14.91%)</td><td>23899.28 (+11.84%)</td><td>14871.63 (+8.02%)</td><td>5290.89 (-3.04%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27574.44 (n/a)</td><td>20512.79 (n/a)</td><td>21368.30 (n/a)</td><td>13767.47 (n/a)</td><td>5456.68 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>1.73 <b>(+59.42%)</b></td><td>1.22 <b>(+43.26%)</b></td><td>1.02 <b>(+29.64%)</b></td><td>0.81 <b>(+29.97%)</b></td><td>0.41 <b>(+126.55%)</b></td><td>647.80 <b>(-23.06%)</b></td><td>471.50 <b>(-26.50%)</b></td><td>514.30 <b>(-22.86%)</b></td><td>303.50 <b>(-37.27%)</b></td><td>149.75 (+6.68%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>1.08 (n/a)</td><td>0.85 (n/a)</td><td>0.79 (n/a)</td><td>0.62 (n/a)</td><td>0.18 (n/a)</td><td>842.00 (n/a)</td><td>641.50 (n/a)</td><td>666.70 (n/a)</td><td>483.80 (n/a)</td><td>140.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>2.85 (+15.83%)</td><td>1.37 <b>(-22.19%)</b></td><td>1.46 <b>(-34.88%)</b></td><td>0.29 (-6.84%)</td><td>1.02 (+9.88%)</td><td>3578.60 (+7.35%)</td><td>1435.54 <b>(+32.27%)</b></td><td>720.40 <b>(+53.57%)</b></td><td>368.10 (-13.65%)</td><td>1335.52 (+5.58%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>2.46 (n/a)</td><td>1.76 (n/a)</td><td>2.24 (n/a)</td><td>0.31 (n/a)</td><td>0.93 (n/a)</td><td>3333.70 (n/a)</td><td>1085.28 (n/a)</td><td>469.10 (n/a)</td><td>426.30 (n/a)</td><td>1264.95 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>1.66 (+9.98%)</td><td>1.19 (+10.29%)</td><td>1.01 (+6.61%)</td><td>0.78 <b>(+23.26%)</b></td><td>0.41 (+13.90%)</td><td>675.70 (-18.86%)</td><td>482.44 (-9.76%)</td><td>519.30 (-6.20%)</td><td>315.90 (-9.09%)</td><td>157.67 (-18.49%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>1.51 (n/a)</td><td>1.08 (n/a)</td><td>0.95 (n/a)</td><td>0.63 (n/a)</td><td>0.36 (n/a)</td><td>832.80 (n/a)</td><td>534.60 (n/a)</td><td>553.60 (n/a)</td><td>347.50 (n/a)</td><td>193.43 (n/a)</td>
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
