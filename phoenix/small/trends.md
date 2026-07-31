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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (-5.42%)</td><td>0.03 <b>(-24.63%)</b></td><td>0.03 <b>(-33.81%)</b></td><td>0.02 (-3.95%)</td><td>0.01 (-10.34%)</td><td>592.60 (+4.11%)</td><td>420.68 <b>(+30.60%)</b></td><td>416.60 <b>(+51.11%)</b></td><td>243.10 (+5.70%)</td><td>136.14 (-3.97%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>569.20 (n/a)</td><td>322.12 (n/a)</td><td>275.70 (n/a)</td><td>230.00 (n/a)</td><td>141.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.06 <b>(+32.45%)</b></td><td>0.03 (-7.93%)</td><td>0.02 <b>(-44.32%)</b></td><td>0.02 (-4.62%)</td><td>0.02 <b>(+69.37%)</b></td><td>603.00 (+4.83%)</td><td>444.76 <b>(+20.43%)</b></td><td>540.20 <b>(+79.59%)</b></td><td>199.60 <b>(-24.51%)</b></td><td>182.41 <b>(+39.89%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.20 (n/a)</td><td>369.30 (n/a)</td><td>300.80 (n/a)</td><td>264.40 (n/a)</td><td>130.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 <b>(+69.29%)</b></td><td>0.04 <b>(+56.58%)</b></td><td>0.04 <b>(+81.12%)</b></td><td>0.03 (+18.29%)</td><td>0.01 <b>(+248.94%)</b></td><td>488.90 (-15.46%)</td><td>354.10 <b>(-32.76%)</b></td><td>299.30 <b>(-44.78%)</b></td><td>255.50 <b>(-40.94%)</b></td><td>100.98 <b>(+82.95%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>578.30 (n/a)</td><td>526.66 (n/a)</td><td>542.00 (n/a)</td><td>432.60 (n/a)</td><td>55.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (-7.75%)</td><td>0.02 (-11.32%)</td><td>0.02 (-1.83%)</td><td>0.01 <b>(-29.78%)</b></td><td>0.00 <b>(+72.91%)</b></td><td>463.40 <b>(+42.41%)</b></td><td>316.24 (+18.99%)</td><td>270.20 (+1.89%)</td><td>237.80 (+8.39%)</td><td>98.95 <b>(+156.09%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>325.40 (n/a)</td><td>265.76 (n/a)</td><td>265.20 (n/a)</td><td>219.40 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (+15.27%)</td><td>0.02 (+12.91%)</td><td>0.02 (+15.14%)</td><td>0.01 (-8.75%)</td><td>0.01 (+19.20%)</td><td>597.40 (+9.57%)</td><td>340.38 (-8.48%)</td><td>292.60 (-13.15%)</td><td>231.60 (-13.23%)</td><td>145.98 <b>(+25.64%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.20 (n/a)</td><td>371.92 (n/a)</td><td>336.90 (n/a)</td><td>266.90 (n/a)</td><td>116.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (+12.06%)</td><td>0.02 <b>(+23.37%)</b></td><td>0.02 <b>(+31.93%)</b></td><td>0.01 (-9.73%)</td><td>0.01 (+18.39%)</td><td>574.60 (+10.78%)</td><td>323.84 (-16.57%)</td><td>271.30 <b>(-24.20%)</b></td><td>235.10 (-10.78%)</td><td>141.95 (+18.16%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.70 (n/a)</td><td>388.18 (n/a)</td><td>357.90 (n/a)</td><td>263.50 (n/a)</td><td>120.14 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 <b>(-22.45%)</b></td><td>0.01 (-0.21%)</td><td>0.01 (+9.24%)</td><td>0.01 <b>(-22.46%)</b></td><td>0.01 (-17.51%)</td><td>803.80 <b>(+28.96%)</b></td><td>455.02 (+2.71%)</td><td>387.30 (-8.46%)</td><td>242.50 <b>(+28.92%)</b></td><td>235.43 <b>(+38.81%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.30 (n/a)</td><td>443.00 (n/a)</td><td>423.10 (n/a)</td><td>188.10 (n/a)</td><td>169.60 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (-3.52%)</td><td>0.01 (-13.26%)</td><td>0.01 <b>(-22.28%)</b></td><td>0.00 <b>(-77.75%)</b></td><td>0.01 <b>(+64.22%)</b></td><td>2002.10 <b>(+349.51%)</b></td><td>645.36 <b>(+95.42%)</b></td><td>355.30 <b>(+28.69%)</b></td><td>250.40 (+3.64%)</td><td>760.46 <b>(+689.76%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>445.40 (n/a)</td><td>330.24 (n/a)</td><td>276.10 (n/a)</td><td>241.60 (n/a)</td><td>96.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (-7.55%)</td><td>0.02 (-6.72%)</td><td>0.02 (+2.48%)</td><td>0.01 <b>(-24.99%)</b></td><td>0.00 (+5.27%)</td><td>582.40 <b>(+33.30%)</b></td><td>357.66 (+10.84%)</td><td>307.80 (-2.44%)</td><td>243.10 (+8.14%)</td><td>131.24 <b>(+61.80%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>436.90 (n/a)</td><td>322.68 (n/a)</td><td>315.50 (n/a)</td><td>224.80 (n/a)</td><td>81.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.30 (n/a)</td><td>412.76 (n/a)</td><td>354.20 (n/a)</td><td>240.20 (n/a)</td><td>176.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>740.00 (n/a)</td><td>465.28 (n/a)</td><td>410.10 (n/a)</td><td>250.40 (n/a)</td><td>185.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>613.50 (n/a)</td><td>470.56 (n/a)</td><td>469.10 (n/a)</td><td>202.20 (n/a)</td><td>167.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>295.40 (n/a)</td><td>275.00 (n/a)</td><td>280.80 (n/a)</td><td>233.60 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>419.50 (n/a)</td><td>311.08 (n/a)</td><td>287.20 (n/a)</td><td>267.00 (n/a)</td><td>61.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>467.00 (n/a)</td><td>349.66 (n/a)</td><td>302.20 (n/a)</td><td>261.40 (n/a)</td><td>91.16 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.80 (n/a)</td><td>380.32 (n/a)</td><td>284.60 (n/a)</td><td>241.60 (n/a)</td><td>169.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.40 (n/a)</td><td>406.40 (n/a)</td><td>446.50 (n/a)</td><td>234.50 (n/a)</td><td>140.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.40 (n/a)</td><td>371.80 (n/a)</td><td>262.00 (n/a)</td><td>234.10 (n/a)</td><td>173.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.10 (n/a)</td><td>374.30 (n/a)</td><td>299.60 (n/a)</td><td>245.90 (n/a)</td><td>163.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>678.80 (n/a)</td><td>458.00 (n/a)</td><td>415.60 (n/a)</td><td>246.10 (n/a)</td><td>169.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.20 (n/a)</td><td>453.72 (n/a)</td><td>495.80 (n/a)</td><td>248.90 (n/a)</td><td>164.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.78 (-4.79%)</td><td>0.51 <b>(+49.69%)</b></td><td>0.50 <b>(+99.04%)</b></td><td>0.31 <b>(+161.27%)</b></td><td>0.18 <b>(-38.04%)</b></td><td>721.10 <b>(-61.73%)</b></td><td>481.18 <b>(-54.99%)</b></td><td>440.90 <b>(-49.76%)</b></td><td>282.10 (+5.03%)</td><td>164.96 <b>(-76.58%)</b></td><td>33.46 (-4.79%)</td><td>21.61 <b>(+49.69%)</b></td><td>21.40 <b>(+99.04%)</b></td><td>13.09 <b>(+161.27%)</b></td><td>7.67 <b>(-38.04%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.82 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.29 (n/a)</td><td>1884.10 (n/a)</td><td>1069.00 (n/a)</td><td>877.60 (n/a)</td><td>268.60 (n/a)</td><td>704.30 (n/a)</td><td>35.14 (n/a)</td><td>14.44 (n/a)</td><td>10.75 (n/a)</td><td>5.01 (n/a)</td><td>12.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.49 <b>(-21.94%)</b></td><td>0.33 <b>(-27.77%)</b></td><td>0.37 <b>(-22.06%)</b></td><td>0.09 <b>(-72.72%)</b></td><td>0.16 <b>(+37.63%)</b></td><td>2439.10 <b>(+266.56%)</b></td><td>968.62 <b>(+90.52%)</b></td><td>599.00 <b>(+28.29%)</b></td><td>450.80 <b>(+28.10%)</b></td><td>836.68 <b>(+569.93%)</b></td><td>20.94 <b>(-21.94%)</b></td><td>14.10 <b>(-27.77%)</b></td><td>15.75 <b>(-22.06%)</b></td><td>3.87 <b>(-72.72%)</b></td><td>6.83 <b>(+37.63%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.63 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.12 (n/a)</td><td>665.40 (n/a)</td><td>508.40 (n/a)</td><td>466.90 (n/a)</td><td>351.90 (n/a)</td><td>124.89 (n/a)</td><td>26.82 (n/a)</td><td>19.52 (n/a)</td><td>20.21 (n/a)</td><td>14.18 (n/a)</td><td>4.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.31 (-0.36%)</td><td>0.30 (+0.50%)</td><td>0.31 (+1.77%)</td><td>0.30 (-0.56%)</td><td>0.00 <b>(+21.15%)</b></td><td>85145.40 (+0.57%)</td><td>82955.38 (-0.49%)</td><td>82231.70 (-1.74%)</td><td>82184.20 (+0.36%)</td><td>1275.94 <b>(+22.38%)</b></td><td>209.04 (-0.36%)</td><td>207.14 (+0.50%)</td><td>208.92 (+1.77%)</td><td>201.77 (-0.56%)</td><td>3.13 <b>(+21.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84666.20 (n/a)</td><td>83367.74 (n/a)</td><td>83688.50 (n/a)</td><td>81885.80 (n/a)</td><td>1042.58 (n/a)</td><td>209.80 (n/a)</td><td>206.10 (n/a)</td><td>205.28 (n/a)</td><td>202.91 (n/a)</td><td>2.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>1.03 (+0.12%)</td><td>1.01 (+1.70%)</td><td>1.01 (+0.90%)</td><td>0.99 (+6.15%)</td><td>0.01 <b>(-61.32%)</b></td><td>25345.50 (-5.79%)</td><td>24888.94 (-1.76%)</td><td>24889.20 (-0.89%)</td><td>24403.30 (-0.12%)</td><td>335.25 <b>(-63.94%)</b></td><td>704.00 (+0.12%)</td><td>690.36 (+1.70%)</td><td>690.25 (+0.90%)</td><td>677.83 (+6.15%)</td><td>9.32 <b>(-61.32%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>1.03 (n/a)</td><td>0.99 (n/a)</td><td>1.00 (n/a)</td><td>0.94 (n/a)</td><td>0.04 (n/a)</td><td>26904.20 (n/a)</td><td>25333.66 (n/a)</td><td>25113.10 (n/a)</td><td>24432.70 (n/a)</td><td>929.67 (n/a)</td><td>703.15 (n/a)</td><td>678.85 (n/a)</td><td>684.10 (n/a)</td><td>638.56 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.14 <b>(-35.32%)</b></td><td>1.65 <b>(-35.99%)</b></td><td>1.58 <b>(-50.08%)</b></td><td>1.42 (-8.65%)</td><td>0.29 <b>(-67.76%)</b></td><td>5692.10 (+9.47%)</td><td>4986.06 <b>(+41.83%)</b></td><td>5109.20 <b>(+100.33%)</b></td><td>3769.00 <b>(+54.62%)</b></td><td>762.59 <b>(-45.80%)</b></td><td>560.88 <b>(-35.32%)</b></td><td>433.22 <b>(-35.99%)</b></td><td>413.75 <b>(-50.08%)</b></td><td>371.38 (-8.65%)</td><td>76.12 <b>(-67.76%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>3.31 (n/a)</td><td>2.58 (n/a)</td><td>3.16 (n/a)</td><td>1.55 (n/a)</td><td>0.90 (n/a)</td><td>5199.60 (n/a)</td><td>3515.62 (n/a)</td><td>2550.40 (n/a)</td><td>2437.60 (n/a)</td><td>1407.09 (n/a)</td><td>867.21 (n/a)</td><td>676.81 (n/a)</td><td>828.88 (n/a)</td><td>406.55 (n/a)</td><td>236.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.33 <b>(+53.15%)</b></td><td>0.22 <b>(+23.97%)</b></td><td>0.19 (+15.86%)</td><td>0.18 (+17.18%)</td><td>0.06 <b>(+139.10%)</b></td><td>6954.80 (-14.66%)</td><td>5997.28 (-16.78%)</td><td>6469.50 (-13.69%)</td><td>3830.40 <b>(-34.71%)</b></td><td>1239.42 <b>(+26.68%)</b></td><td>17.52 <b>(+53.15%)</b></td><td>11.73 <b>(+23.97%)</b></td><td>10.37 (+15.86%)</td><td>9.65 (+17.18%)</td><td>3.26 <b>(+139.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>8149.80 (n/a)</td><td>7206.60 (n/a)</td><td>7495.40 (n/a)</td><td>5866.30 (n/a)</td><td>978.39 (n/a)</td><td>11.44 (n/a)</td><td>9.46 (n/a)</td><td>8.95 (n/a)</td><td>8.23 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>3.82 (n/a)</td><td>3.63 (n/a)</td><td>3.65 (n/a)</td><td>3.40 (n/a)</td><td>0.18 (n/a)</td><td>3.81 (n/a)</td><td>3.63 (n/a)</td><td>3.65 (n/a)</td><td>3.40 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>6.82 (-0.18%)</td><td>6.18 (-1.32%)</td><td>6.15 (-4.25%)</td><td>5.48 (+0.10%)</td><td>0.56 (-0.91%)</td><td>6.82 (-0.18%)</td><td>6.17 (-1.32%)</td><td>6.14 (-4.25%)</td><td>5.48 (+0.10%)</td><td>0.56 (-0.91%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>6.84 (n/a)</td><td>6.26 (n/a)</td><td>6.42 (n/a)</td><td>5.48 (n/a)</td><td>0.57 (n/a)</td><td>6.83 (n/a)</td><td>6.26 (n/a)</td><td>6.42 (n/a)</td><td>5.48 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>9.63 <b>(-31.54%)</b></td><td>8.49 <b>(-26.93%)</b></td><td>8.26 <b>(-35.93%)</b></td><td>8.08 (+9.28%)</td><td>0.64 <b>(-77.44%)</b></td><td>9.62 <b>(-31.54%)</b></td><td>8.49 <b>(-26.93%)</b></td><td>8.26 <b>(-35.93%)</b></td><td>8.07 (+9.28%)</td><td>0.64 <b>(-77.44%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>14.07 (n/a)</td><td>11.63 (n/a)</td><td>12.90 (n/a)</td><td>7.39 (n/a)</td><td>2.86 (n/a)</td><td>14.06 (n/a)</td><td>11.62 (n/a)</td><td>12.89 (n/a)</td><td>7.39 (n/a)</td><td>2.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>3.87 (n/a)</td><td>3.68 (n/a)</td><td>3.71 (n/a)</td><td>3.44 (n/a)</td><td>0.17 (n/a)</td><td>3.87 (n/a)</td><td>3.68 (n/a)</td><td>3.71 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>6.45 (-14.45%)</td><td>6.01 (-9.58%)</td><td>5.98 (-11.10%)</td><td>5.66 (+1.45%)</td><td>0.33 <b>(-52.84%)</b></td><td>6.45 (-14.45%)</td><td>6.00 (-9.58%)</td><td>5.98 (-11.10%)</td><td>5.66 (+1.45%)</td><td>0.33 <b>(-52.84%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>7.54 (n/a)</td><td>6.64 (n/a)</td><td>6.73 (n/a)</td><td>5.58 (n/a)</td><td>0.70 (n/a)</td><td>7.53 (n/a)</td><td>6.64 (n/a)</td><td>6.73 (n/a)</td><td>5.58 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>9.78 <b>(-29.04%)</b></td><td>8.59 (-13.98%)</td><td>8.46 (-8.37%)</td><td>7.02 (-15.51%)</td><td>1.12 <b>(-50.47%)</b></td><td>9.77 <b>(-29.04%)</b></td><td>8.58 (-13.98%)</td><td>8.46 (-8.37%)</td><td>7.02 (-15.51%)</td><td>1.12 <b>(-50.47%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>13.78 (n/a)</td><td>9.98 (n/a)</td><td>9.24 (n/a)</td><td>8.31 (n/a)</td><td>2.25 (n/a)</td><td>13.77 (n/a)</td><td>9.98 (n/a)</td><td>9.23 (n/a)</td><td>8.31 (n/a)</td><td>2.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.91 (-8.83%)</td><td>1.77 <b>(-38.41%)</b></td><td>1.06 <b>(-62.91%)</b></td><td>1.02 <b>(-58.13%)</b></td><td>1.01 <b>(+236.04%)</b></td><td>2.91 (-8.83%)</td><td>1.77 <b>(-38.41%)</b></td><td>1.05 <b>(-62.91%)</b></td><td>1.02 <b>(-58.13%)</b></td><td>1.01 <b>(+236.04%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>3.20 (n/a)</td><td>2.87 (n/a)</td><td>2.85 (n/a)</td><td>2.43 (n/a)</td><td>0.30 (n/a)</td><td>3.19 (n/a)</td><td>2.87 (n/a)</td><td>2.84 (n/a)</td><td>2.43 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.46 (-12.33%)</td><td>0.27 (+4.73%)</td><td>0.31 (+13.72%)</td><td>0.07 (-4.43%)</td><td>0.16 (-15.06%)</td><td>0.46 (-12.33%)</td><td>0.26 (+4.73%)</td><td>0.30 (+13.72%)</td><td>0.07 (-4.43%)</td><td>0.16 (-15.06%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.53 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td><td>0.52 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.74 (+15.81%)</td><td>0.62 <b>(+47.43%)</b></td><td>0.63 <b>(+69.93%)</b></td><td>0.49 <b>(+40.54%)</b></td><td>0.10 (-19.80%)</td><td>0.73 (+15.81%)</td><td>0.62 <b>(+47.43%)</b></td><td>0.62 <b>(+69.93%)</b></td><td>0.48 <b>(+40.54%)</b></td><td>0.10 (-19.80%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.64 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>0.63 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.66 (+12.32%)</td><td>2.14 <b>(+76.54%)</b></td><td>2.40 <b>(+196.92%)</b></td><td>0.80 <b>(+75.57%)</b></td><td>0.76 (-8.08%)</td><td>2.62 (+12.32%)</td><td>2.10 <b>(+76.54%)</b></td><td>2.36 <b>(+196.92%)</b></td><td>0.79 <b>(+75.57%)</b></td><td>0.74 (-8.08%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>2.37 (n/a)</td><td>1.21 (n/a)</td><td>0.81 (n/a)</td><td>0.46 (n/a)</td><td>0.82 (n/a)</td><td>2.33 (n/a)</td><td>1.19 (n/a)</td><td>0.80 (n/a)</td><td>0.45 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2518.50 (n/a)</td><td>912.72 (n/a)</td><td>533.20 (n/a)</td><td>438.50 (n/a)</td><td>899.16 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>439.50 (n/a)</td><td>340.96 (n/a)</td><td>290.60 (n/a)</td><td>265.80 (n/a)</td><td>87.51 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.10 (n/a)</td><td>407.08 (n/a)</td><td>435.80 (n/a)</td><td>235.40 (n/a)</td><td>142.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.50 (n/a)</td><td>393.36 (n/a)</td><td>327.60 (n/a)</td><td>272.40 (n/a)</td><td>145.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2541.90 (n/a)</td><td>1180.90 (n/a)</td><td>571.10 (n/a)</td><td>240.60 (n/a)</td><td>1066.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>687.90 (n/a)</td><td>478.44 (n/a)</td><td>470.30 (n/a)</td><td>319.10 (n/a)</td><td>133.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (+19.40%)</td><td>0.03 <b>(+29.71%)</b></td><td>0.03 <b>(+37.43%)</b></td><td>0.02 <b>(+26.38%)</b></td><td>0.01 <b>(+48.66%)</b></td><td>496.40 <b>(-20.87%)</b></td><td>351.74 <b>(-20.31%)</b></td><td>298.70 <b>(-27.24%)</b></td><td>240.70 (-16.25%)</td><td>126.20 (-0.36%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.30 (n/a)</td><td>441.40 (n/a)</td><td>410.50 (n/a)</td><td>287.40 (n/a)</td><td>126.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (-4.58%)</td><td>0.02 (-13.84%)</td><td>0.02 <b>(-39.24%)</b></td><td>0.02 (+1.51%)</td><td>0.01 (-9.47%)</td><td>506.60 (-1.50%)</td><td>399.26 (+14.36%)</td><td>466.30 <b>(+64.60%)</b></td><td>244.30 (+4.80%)</td><td>125.34 (-5.47%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.30 (n/a)</td><td>349.12 (n/a)</td><td>283.30 (n/a)</td><td>233.10 (n/a)</td><td>132.60 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (-5.39%)</td><td>0.02 (-3.85%)</td><td>0.02 <b>(-22.79%)</b></td><td>0.01 <b>(+247.75%)</b></td><td>0.01 <b>(-51.62%)</b></td><td>588.90 <b>(-71.24%)</b></td><td>434.78 <b>(-36.55%)</b></td><td>394.90 <b>(+29.52%)</b></td><td>305.60 (+5.67%)</td><td>111.52 <b>(-85.44%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2047.90 (n/a)</td><td>685.28 (n/a)</td><td>304.90 (n/a)</td><td>289.20 (n/a)</td><td>765.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (-6.95%)</td><td>0.03 (+5.64%)</td><td>0.03 (+0.16%)</td><td>0.02 (+16.16%)</td><td>0.00 <b>(-39.13%)</b></td><td>446.60 (-13.92%)</td><td>321.22 (-10.46%)</td><td>290.40 (-0.14%)</td><td>271.20 (+7.45%)</td><td>71.41 <b>(-41.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.80 (n/a)</td><td>358.74 (n/a)</td><td>290.80 (n/a)</td><td>252.40 (n/a)</td><td>123.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (+15.33%)</td><td>0.02 (-2.22%)</td><td>0.02 (+0.37%)</td><td>0.00 <b>(-70.37%)</b></td><td>0.01 <b>(+65.90%)</b></td><td>1897.90 <b>(+237.46%)</b></td><td>699.36 <b>(+52.65%)</b></td><td>457.90 (-0.37%)</td><td>228.70 (-13.31%)</td><td>677.82 <b>(+466.99%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.40 (n/a)</td><td>458.14 (n/a)</td><td>459.60 (n/a)</td><td>263.80 (n/a)</td><td>119.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 <b>(+23.81%)</b></td><td>0.02 (+9.96%)</td><td>0.02 (+7.47%)</td><td>0.01 (+3.25%)</td><td>0.01 <b>(+68.94%)</b></td><td>567.10 (-3.14%)</td><td>456.78 (-6.14%)</td><td>469.70 (-6.95%)</td><td>299.90 (-19.23%)</td><td>113.68 <b>(+36.35%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.50 (n/a)</td><td>486.64 (n/a)</td><td>504.80 (n/a)</td><td>371.30 (n/a)</td><td>83.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 <b>(-20.83%)</b></td><td>0.02 (+0.14%)</td><td>0.02 (-12.47%)</td><td>0.02 <b>(+297.75%)</b></td><td>0.01 <b>(-56.95%)</b></td><td>515.10 <b>(-74.86%)</b></td><td>439.08 <b>(-39.39%)</b></td><td>474.80 (+14.24%)</td><td>289.10 <b>(+26.30%)</b></td><td>88.17 <b>(-88.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2048.80 (n/a)</td><td>724.46 (n/a)</td><td>415.60 (n/a)</td><td>228.90 (n/a)</td><td>751.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.01 <b>(-48.90%)</b></td><td>0.01 <b>(-21.28%)</b></td><td>0.01 (-0.72%)</td><td>0.01 (-6.55%)</td><td>0.00 <b>(-83.35%)</b></td><td>663.80 (+7.01%)</td><td>604.96 (+16.66%)</td><td>613.70 (+0.74%)</td><td>553.70 <b>(+95.65%)</b></td><td>49.69 <b>(-65.96%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.30 (n/a)</td><td>518.58 (n/a)</td><td>609.20 (n/a)</td><td>283.00 (n/a)</td><td>145.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (+0.43%)</td><td>0.02 <b>(+33.95%)</b></td><td>0.02 <b>(+34.85%)</b></td><td>0.02 <b>(+46.96%)</b></td><td>0.00 <b>(-36.71%)</b></td><td>449.00 <b>(-31.95%)</b></td><td>360.26 <b>(-29.91%)</b></td><td>371.50 <b>(-25.85%)</b></td><td>282.80 (-0.42%)</td><td>64.54 <b>(-56.21%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>659.80 (n/a)</td><td>513.96 (n/a)</td><td>501.00 (n/a)</td><td>284.00 (n/a)</td><td>147.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (-4.51%)</td><td>0.02 (-1.82%)</td><td>0.02 (-8.66%)</td><td>0.02 (+11.16%)</td><td>0.01 <b>(-24.80%)</b></td><td>531.60 (-10.04%)</td><td>379.36 (-3.40%)</td><td>368.00 (+9.46%)</td><td>266.30 (+4.72%)</td><td>107.84 <b>(-29.32%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>392.70 (n/a)</td><td>336.20 (n/a)</td><td>254.30 (n/a)</td><td>152.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 <b>(-42.81%)</b></td><td>0.02 <b>(-27.66%)</b></td><td>0.02 (-17.32%)</td><td>0.01 (+2.52%)</td><td>0.00 <b>(-83.27%)</b></td><td>575.90 (-2.47%)</td><td>514.04 <b>(+21.34%)</b></td><td>514.50 <b>(+20.94%)</b></td><td>445.90 <b>(+74.86%)</b></td><td>47.82 <b>(-71.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.50 (n/a)</td><td>423.64 (n/a)</td><td>425.40 (n/a)</td><td>255.00 (n/a)</td><td>166.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (+8.88%)</td><td>0.02 (-5.64%)</td><td>0.02 (-0.06%)</td><td>0.01 <b>(-39.88%)</b></td><td>0.01 <b>(+54.52%)</b></td><td>1063.40 <b>(+66.34%)</b></td><td>587.00 (+17.32%)</td><td>524.40 (+0.06%)</td><td>331.00 (-8.16%)</td><td>278.67 <b>(+155.66%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>639.30 (n/a)</td><td>500.36 (n/a)</td><td>524.10 (n/a)</td><td>360.40 (n/a)</td><td>109.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 <b>(-28.00%)</b></td><td>0.02 <b>(-20.89%)</b></td><td>0.02 (-5.81%)</td><td>0.01 <b>(-20.85%)</b></td><td>0.01 <b>(-40.75%)</b></td><td>823.20 <b>(+26.34%)</b></td><td>521.62 <b>(+20.60%)</b></td><td>478.60 (+6.17%)</td><td>326.40 <b>(+38.89%)</b></td><td>183.63 (+9.43%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.60 (n/a)</td><td>432.52 (n/a)</td><td>450.80 (n/a)</td><td>235.00 (n/a)</td><td>167.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (-15.22%)</td><td>0.02 (+6.55%)</td><td>0.02 (+14.84%)</td><td>0.01 (+13.37%)</td><td>0.00 <b>(-45.68%)</b></td><td>600.10 (-11.80%)</td><td>470.18 (-10.73%)</td><td>463.90 (-12.93%)</td><td>365.90 (+17.96%)</td><td>83.83 <b>(-41.23%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>680.40 (n/a)</td><td>526.68 (n/a)</td><td>532.80 (n/a)</td><td>310.20 (n/a)</td><td>142.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (+3.22%)</td><td>0.03 (+7.32%)</td><td>0.03 (-1.83%)</td><td>0.01 (-1.10%)</td><td>0.01 (-12.54%)</td><td>567.10 (+1.12%)</td><td>344.28 (-8.72%)</td><td>294.80 (+1.87%)</td><td>253.30 (-3.14%)</td><td>127.13 (-8.99%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.80 (n/a)</td><td>377.16 (n/a)</td><td>289.40 (n/a)</td><td>261.50 (n/a)</td><td>139.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 <b>(+38.19%)</b></td><td>0.04 <b>(+41.12%)</b></td><td>0.04 <b>(+23.22%)</b></td><td>0.02 <b>(+40.42%)</b></td><td>0.01 <b>(+24.33%)</b></td><td>499.30 <b>(-28.79%)</b></td><td>330.42 <b>(-30.52%)</b></td><td>304.50 (-18.84%)</td><td>245.00 <b>(-27.64%)</b></td><td>105.10 <b>(-36.91%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>701.20 (n/a)</td><td>475.58 (n/a)</td><td>375.20 (n/a)</td><td>338.60 (n/a)</td><td>166.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (+18.36%)</td><td>0.02 (+9.77%)</td><td>0.02 (+2.36%)</td><td>0.01 (+4.91%)</td><td>0.01 <b>(+33.93%)</b></td><td>591.80 (-4.69%)</td><td>401.52 (-3.79%)</td><td>394.50 (-2.30%)</td><td>212.70 (-15.53%)</td><td>177.10 (+11.56%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.90 (n/a)</td><td>417.32 (n/a)</td><td>403.80 (n/a)</td><td>251.80 (n/a)</td><td>158.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (+4.40%)</td><td>0.02 (+0.80%)</td><td>0.02 (+15.13%)</td><td>0.01 <b>(-41.83%)</b></td><td>0.01 <b>(+36.25%)</b></td><td>1043.40 <b>(+71.92%)</b></td><td>550.98 (+16.55%)</td><td>449.50 (-13.14%)</td><td>250.00 (-4.21%)</td><td>321.05 <b>(+129.11%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.90 (n/a)</td><td>472.74 (n/a)</td><td>517.50 (n/a)</td><td>261.00 (n/a)</td><td>140.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (-16.40%)</td><td>0.02 (-11.03%)</td><td>0.03 (+0.86%)</td><td>0.02 <b>(-24.84%)</b></td><td>0.01 (+0.87%)</td><td>539.80 <b>(+33.05%)</b></td><td>365.28 (+16.46%)</td><td>305.60 (-0.84%)</td><td>245.80 (+19.61%)</td><td>127.27 <b>(+64.42%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>405.70 (n/a)</td><td>313.66 (n/a)</td><td>308.20 (n/a)</td><td>205.50 (n/a)</td><td>77.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (+13.39%)</td><td>0.03 (+0.83%)</td><td>0.03 (-1.52%)</td><td>0.02 (+8.46%)</td><td>0.01 <b>(+22.70%)</b></td><td>494.40 (-7.80%)</td><td>352.34 (+0.49%)</td><td>308.10 (+1.55%)</td><td>241.70 (-11.82%)</td><td>108.50 (+0.20%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.20 (n/a)</td><td>350.62 (n/a)</td><td>303.40 (n/a)</td><td>274.10 (n/a)</td><td>108.28 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (+0.01%)</td><td>0.02 (-3.88%)</td><td>0.02 (-3.72%)</td><td>0.01 <b>(-33.95%)</b></td><td>0.01 <b>(+40.48%)</b></td><td>1007.80 <b>(+51.39%)</b></td><td>586.94 <b>(+23.05%)</b></td><td>500.20 (+3.86%)</td><td>269.40 (+0.00%)</td><td>323.65 <b>(+123.77%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>665.70 (n/a)</td><td>477.00 (n/a)</td><td>481.60 (n/a)</td><td>269.40 (n/a)</td><td>144.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 <b>(-32.38%)</b></td><td>0.02 (-10.00%)</td><td>0.02 (+3.46%)</td><td>0.01 <b>(-28.32%)</b></td><td>0.01 <b>(-31.20%)</b></td><td>828.40 <b>(+39.51%)</b></td><td>504.48 (+11.20%)</td><td>471.00 (-3.34%)</td><td>288.20 <b>(+47.87%)</b></td><td>225.83 <b>(+49.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.80 (n/a)</td><td>453.66 (n/a)</td><td>487.30 (n/a)</td><td>194.90 (n/a)</td><td>151.47 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (+11.10%)</td><td>0.02 <b>(+35.01%)</b></td><td>0.03 <b>(+90.19%)</b></td><td>0.01 (+9.60%)</td><td>0.01 <b>(+25.22%)</b></td><td>561.40 (-8.76%)</td><td>380.16 <b>(-23.03%)</b></td><td>282.50 <b>(-47.42%)</b></td><td>236.90 (-9.99%)</td><td>160.86 (+12.20%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.30 (n/a)</td><td>493.92 (n/a)</td><td>537.30 (n/a)</td><td>263.20 (n/a)</td><td>143.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (-14.91%)</td><td>0.02 (-15.33%)</td><td>0.02 (-19.17%)</td><td>0.01 <b>(-54.32%)</b></td><td>0.01 (+18.09%)</td><td>1354.80 <b>(+118.90%)</b></td><td>615.98 <b>(+39.68%)</b></td><td>462.20 <b>(+23.72%)</b></td><td>343.40 (+17.52%)</td><td>422.03 <b>(+203.58%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.90 (n/a)</td><td>440.98 (n/a)</td><td>373.60 (n/a)</td><td>292.20 (n/a)</td><td>139.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 <b>(+26.95%)</b></td><td>0.02 (+14.07%)</td><td>0.02 (-5.96%)</td><td>0.01 <b>(+75.48%)</b></td><td>0.01 (+4.68%)</td><td>555.80 <b>(-43.01%)</b></td><td>464.22 (-18.08%)</td><td>524.80 (+6.34%)</td><td>269.50 <b>(-21.24%)</b></td><td>116.50 <b>(-54.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>975.30 (n/a)</td><td>566.66 (n/a)</td><td>493.50 (n/a)</td><td>342.20 (n/a)</td><td>255.15 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.35 (-8.08%)</td><td>0.33 (+14.59%)</td><td>0.33 (+2.14%)</td><td>0.31 <b>(+61.33%)</b></td><td>0.01 <b>(-82.42%)</b></td><td>315.40 <b>(-38.01%)</b></td><td>302.48 (-18.81%)</td><td>299.60 (-2.12%)</td><td>283.70 (+8.78%)</td><td>13.19 <b>(-88.60%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>508.80 (n/a)</td><td>372.56 (n/a)</td><td>306.10 (n/a)</td><td>260.80 (n/a)</td><td>115.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.33 (-12.04%)</td><td>0.24 (-15.71%)</td><td>0.22 <b>(-29.13%)</b></td><td>0.17 (+4.14%)</td><td>0.06 <b>(-37.52%)</b></td><td>575.30 (-3.97%)</td><td>435.68 (+11.55%)</td><td>443.50 <b>(+41.06%)</b></td><td>299.00 (+13.69%)</td><td>101.68 <b>(-32.35%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.31 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>599.10 (n/a)</td><td>390.58 (n/a)</td><td>314.40 (n/a)</td><td>263.00 (n/a)</td><td>150.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.19 <b>(-36.92%)</b></td><td>0.17 <b>(-20.66%)</b></td><td>0.17 (-18.23%)</td><td>0.15 (+0.56%)</td><td>0.01 <b>(-76.42%)</b></td><td>637.90 (-0.55%)</td><td>577.30 <b>(+20.23%)</b></td><td>568.30 <b>(+22.29%)</b></td><td>525.80 <b>(+58.52%)</b></td><td>44.85 <b>(-62.77%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>641.40 (n/a)</td><td>480.18 (n/a)</td><td>464.70 (n/a)</td><td>331.70 (n/a)</td><td>120.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.26 (-10.75%)</td><td>0.23 (+8.47%)</td><td>0.24 (-0.06%)</td><td>0.15 <b>(+29.76%)</b></td><td>0.04 <b>(-42.78%)</b></td><td>481.80 <b>(-22.94%)</b></td><td>336.22 (-15.37%)</td><td>311.20 (+0.06%)</td><td>280.10 (+12.04%)</td><td>82.49 <b>(-49.35%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>625.20 (n/a)</td><td>397.28 (n/a)</td><td>311.00 (n/a)</td><td>250.00 (n/a)</td><td>162.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.31 <b>(+106.70%)</b></td><td>0.22 <b>(+85.13%)</b></td><td>0.25 <b>(+99.53%)</b></td><td>0.13 <b>(+143.16%)</b></td><td>0.08 <b>(+101.48%)</b></td><td>547.30 <b>(-58.87%)</b></td><td>374.20 <b>(-47.21%)</b></td><td>297.80 <b>(-49.87%)</b></td><td>239.70 <b>(-51.63%)</b></td><td>141.43 <b>(-59.79%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>1330.70 (n/a)</td><td>708.80 (n/a)</td><td>594.10 (n/a)</td><td>495.60 (n/a)</td><td>351.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.27 (-12.13%)</td><td>0.18 (+6.62%)</td><td>0.16 (+19.29%)</td><td>0.13 (+5.92%)</td><td>0.06 <b>(-26.36%)</b></td><td>555.70 (-5.59%)</td><td>437.02 (-9.98%)</td><td>452.90 (-16.16%)</td><td>272.80 (+13.81%)</td><td>119.01 (-15.17%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>588.60 (n/a)</td><td>485.46 (n/a)</td><td>540.20 (n/a)</td><td>239.70 (n/a)</td><td>140.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.47 <b>(+83.29%)</b></td><td>0.31 <b>(+43.86%)</b></td><td>0.30 <b>(+29.45%)</b></td><td>0.20 <b>(+63.29%)</b></td><td>0.10 <b>(+87.43%)</b></td><td>644.70 <b>(-38.76%)</b></td><td>460.02 <b>(-30.07%)</b></td><td>441.10 <b>(-22.76%)</b></td><td>278.80 <b>(-45.45%)</b></td><td>134.93 <b>(-40.31%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>1052.70 (n/a)</td><td>657.86 (n/a)</td><td>571.10 (n/a)</td><td>511.10 (n/a)</td><td>226.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.50 (+11.39%)</td><td>0.35 <b>(+41.29%)</b></td><td>0.34 <b>(+34.11%)</b></td><td>0.17 <b>(+145.17%)</b></td><td>0.14 (-2.28%)</td><td>764.50 <b>(-59.21%)</b></td><td>442.70 <b>(-44.01%)</b></td><td>386.80 <b>(-25.43%)</b></td><td>261.20 (-10.21%)</td><td>207.70 <b>(-67.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.45 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>1874.40 (n/a)</td><td>790.66 (n/a)</td><td>518.70 (n/a)</td><td>290.90 (n/a)</td><td>636.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.46 (-7.54%)</td><td>0.27 (-13.57%)</td><td>0.22 <b>(-25.01%)</b></td><td>0.06 <b>(-70.18%)</b></td><td>0.16 <b>(+33.21%)</b></td><td>2120.10 <b>(+235.30%)</b></td><td>785.22 <b>(+70.07%)</b></td><td>592.20 <b>(+33.38%)</b></td><td>284.00 (+8.15%)</td><td>760.95 <b>(+376.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>632.30 (n/a)</td><td>461.70 (n/a)</td><td>444.00 (n/a)</td><td>262.60 (n/a)</td><td>159.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.00 (+0.00%)</td><td>0.00 (-10.53%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+1.06%)</td><td>19872.73 (-10.72%)</td><td>13935.32 (-1.26%)</td><td>16694.63 (+6.41%)</td><td>5628.59 (-1.52%)</td><td>5991.37 (-15.84%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22259.61 (n/a)</td><td>14112.98 (n/a)</td><td>15688.28 (n/a)</td><td>5715.50 (n/a)</td><td>7119.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.00 (+7.69%)</td><td>0.00 <b>(+30.30%)</b></td><td>0.00 (+20.00%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(+23.54%)</b></td><td>18126.97 <b>(-21.65%)</b></td><td>12485.75 (-18.20%)</td><td>14667.55 (-5.82%)</td><td>5964.32 (-7.76%)</td><td>5944.01 (-0.03%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23137.13 (n/a)</td><td>15264.12 (n/a)</td><td>15574.33 (n/a)</td><td>6465.86 (n/a)</td><td>5945.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.16 (+5.85%)</td><td>0.10 (+16.57%)</td><td>0.09 <b>(+27.24%)</b></td><td>0.07 (+4.36%)</td><td>0.03 (+3.90%)</td><td>28260.78 (-4.16%)</td><td>21642.72 (-14.21%)</td><td>22328.66 <b>(-21.46%)</b></td><td>13476.33 (-5.55%)</td><td>6173.99 (-2.21%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29487.39 (n/a)</td><td>25227.76 (n/a)</td><td>28429.38 (n/a)</td><td>14268.63 (n/a)</td><td>6313.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>1.84 (+8.55%)</td><td>1.40 (-13.02%)</td><td>1.42 (-13.98%)</td><td>0.83 <b>(-41.25%)</b></td><td>0.38 <b>(+236.67%)</b></td><td>630.10 <b>(+70.21%)</b></td><td>402.62 <b>(+23.19%)</b></td><td>370.10 (+16.27%)</td><td>285.70 (-7.87%)</td><td>135.09 <b>(+442.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>1.69 (n/a)</td><td>1.61 (n/a)</td><td>1.65 (n/a)</td><td>1.42 (n/a)</td><td>0.11 (n/a)</td><td>370.20 (n/a)</td><td>326.84 (n/a)</td><td>318.30 (n/a)</td><td>310.10 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.59 (-0.09%)</td><td>1.69 (-14.75%)</td><td>1.70 <b>(-30.08%)</b></td><td>0.31 <b>(-71.51%)</b></td><td>0.93 <b>(+30.05%)</b></td><td>3360.70 <b>(+251.06%)</b></td><td>1116.82 <b>(+84.89%)</b></td><td>617.50 <b>(+43.01%)</b></td><td>404.90 (+0.10%)</td><td>1263.74 <b>(+390.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>2.59 (n/a)</td><td>1.98 (n/a)</td><td>2.43 (n/a)</td><td>1.10 (n/a)</td><td>0.72 (n/a)</td><td>957.30 (n/a)</td><td>604.06 (n/a)</td><td>431.80 (n/a)</td><td>404.50 (n/a)</td><td>257.51 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>1.62 (-18.27%)</td><td>1.16 (-18.71%)</td><td>1.05 <b>(-28.34%)</b></td><td>0.80 (-15.70%)</td><td>0.34 <b>(-25.42%)</b></td><td>653.80 (+18.61%)</td><td>484.90 <b>(+20.54%)</b></td><td>498.50 <b>(+39.56%)</b></td><td>324.10 <b>(+22.35%)</b></td><td>135.12 (+1.90%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>1.98 (n/a)</td><td>1.42 (n/a)</td><td>1.47 (n/a)</td><td>0.95 (n/a)</td><td>0.45 (n/a)</td><td>551.20 (n/a)</td><td>402.26 (n/a)</td><td>357.20 (n/a)</td><td>264.90 (n/a)</td><td>132.59 (n/a)</td>
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
