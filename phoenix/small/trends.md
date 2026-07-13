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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (-6.94%)</td><td>0.03 (-14.91%)</td><td>0.03 <b>(-36.15%)</b></td><td>0.02 (-18.09%)</td><td>0.01 (+16.13%)</td><td>605.10 <b>(+22.09%)</b></td><td>452.76 <b>(+22.41%)</b></td><td>490.80 <b>(+56.60%)</b></td><td>280.10 (+7.48%)</td><td>152.20 <b>(+44.99%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.60 (n/a)</td><td>369.86 (n/a)</td><td>313.40 (n/a)</td><td>260.60 (n/a)</td><td>104.97 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.09 <b>(+120.77%)</b></td><td>0.05 <b>(+41.61%)</b></td><td>0.05 <b>(+28.09%)</b></td><td>0.02 (-4.55%)</td><td>0.03 <b>(+250.73%)</b></td><td>526.80 (+4.77%)</td><td>336.82 (-14.81%)</td><td>266.20 <b>(-21.94%)</b></td><td>138.70 <b>(-54.70%)</b></td><td>166.86 <b>(+70.44%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.80 (n/a)</td><td>395.36 (n/a)</td><td>341.00 (n/a)</td><td>306.20 (n/a)</td><td>97.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.06 <b>(+57.72%)</b></td><td>0.04 <b>(+49.46%)</b></td><td>0.04 <b>(+81.52%)</b></td><td>0.02 (-10.62%)</td><td>0.02 <b>(+82.56%)</b></td><td>664.70 (+11.88%)</td><td>341.92 <b>(-26.33%)</b></td><td>292.10 <b>(-44.91%)</b></td><td>189.20 <b>(-36.62%)</b></td><td>185.69 <b>(+41.73%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>594.10 (n/a)</td><td>464.10 (n/a)</td><td>530.20 (n/a)</td><td>298.50 (n/a)</td><td>131.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 <b>(+47.26%)</b></td><td>0.01 (+12.79%)</td><td>0.01 (-13.44%)</td><td>0.01 (+7.46%)</td><td>0.01 <b>(+137.76%)</b></td><td>512.90 (-6.95%)</td><td>416.30 (-4.18%)</td><td>492.60 (+15.50%)</td><td>217.40 <b>(-32.10%)</b></td><td>128.66 <b>(+55.13%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.20 (n/a)</td><td>434.46 (n/a)</td><td>426.50 (n/a)</td><td>320.20 (n/a)</td><td>82.94 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (+0.24%)</td><td>0.01 <b>(-39.05%)</b></td><td>0.01 <b>(-41.17%)</b></td><td>0.00 <b>(-78.78%)</b></td><td>0.01 <b>(+60.93%)</b></td><td>2036.60 <b>(+371.22%)</b></td><td>757.66 <b>(+168.24%)</b></td><td>446.00 <b>(+69.97%)</b></td><td>213.00 (-0.23%)</td><td>738.89 <b>(+721.73%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>432.20 (n/a)</td><td>282.46 (n/a)</td><td>262.40 (n/a)</td><td>213.50 (n/a)</td><td>89.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 <b>(-25.67%)</b></td><td>0.01 <b>(-29.74%)</b></td><td>0.01 <b>(-45.46%)</b></td><td>0.01 (+8.28%)</td><td>0.00 <b>(-59.21%)</b></td><td>485.10 (-7.65%)</td><td>423.18 <b>(+30.39%)</b></td><td>435.30 <b>(+83.36%)</b></td><td>311.40 <b>(+34.51%)</b></td><td>70.57 <b>(-46.69%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>525.30 (n/a)</td><td>324.56 (n/a)</td><td>237.40 (n/a)</td><td>231.50 (n/a)</td><td>132.36 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (+10.82%)</td><td>0.02 <b>(+53.57%)</b></td><td>0.02 <b>(+95.95%)</b></td><td>0.01 <b>(+406.51%)</b></td><td>0.00 <b>(-51.74%)</b></td><td>421.40 <b>(-80.26%)</b></td><td>303.82 <b>(-60.40%)</b></td><td>275.90 <b>(-48.96%)</b></td><td>244.40 (-9.75%)</td><td>68.85 <b>(-91.15%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2134.60 (n/a)</td><td>767.30 (n/a)</td><td>540.60 (n/a)</td><td>270.80 (n/a)</td><td>777.94 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (-7.09%)</td><td>0.01 (+5.22%)</td><td>0.01 (+13.75%)</td><td>0.01 (+9.64%)</td><td>0.00 <b>(-25.67%)</b></td><td>552.10 (-8.79%)</td><td>397.76 (-10.62%)</td><td>424.00 (-12.07%)</td><td>258.00 (+7.59%)</td><td>114.03 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.30 (n/a)</td><td>445.04 (n/a)</td><td>482.20 (n/a)</td><td>239.80 (n/a)</td><td>163.64 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.01 (-3.68%)</td><td>0.01 (+2.77%)</td><td>0.01 (+3.98%)</td><td>0.01 (-0.35%)</td><td>0.00 (-14.19%)</td><td>576.20 (+0.35%)</td><td>470.52 (-3.34%)</td><td>466.90 (-3.81%)</td><td>367.70 (+3.81%)</td><td>78.04 (-10.40%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.20 (n/a)</td><td>486.80 (n/a)</td><td>485.40 (n/a)</td><td>354.20 (n/a)</td><td>87.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1886.60 (n/a)</td><td>545.88 (n/a)</td><td>220.20 (n/a)</td><td>176.80 (n/a)</td><td>749.75 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1961.50 (n/a)</td><td>588.26 (n/a)</td><td>264.40 (n/a)</td><td>192.30 (n/a)</td><td>768.54 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.10 (n/a)</td><td>363.16 (n/a)</td><td>363.70 (n/a)</td><td>217.10 (n/a)</td><td>134.70 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>594.40 (n/a)</td><td>427.48 (n/a)</td><td>434.20 (n/a)</td><td>263.60 (n/a)</td><td>158.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.00 (n/a)</td><td>365.98 (n/a)</td><td>288.20 (n/a)</td><td>230.00 (n/a)</td><td>143.64 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.20 (n/a)</td><td>454.04 (n/a)</td><td>479.50 (n/a)</td><td>263.30 (n/a)</td><td>115.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.70 (n/a)</td><td>434.20 (n/a)</td><td>451.40 (n/a)</td><td>205.70 (n/a)</td><td>182.82 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.60 (n/a)</td><td>402.46 (n/a)</td><td>449.70 (n/a)</td><td>272.60 (n/a)</td><td>117.58 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>299.50 (n/a)</td><td>279.36 (n/a)</td><td>273.00 (n/a)</td><td>267.10 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.20 (n/a)</td><td>335.32 (n/a)</td><td>310.60 (n/a)</td><td>236.70 (n/a)</td><td>110.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>314.30 (n/a)</td><td>273.64 (n/a)</td><td>285.80 (n/a)</td><td>225.90 (n/a)</td><td>37.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>814.30 (n/a)</td><td>513.30 (n/a)</td><td>393.10 (n/a)</td><td>389.20 (n/a)</td><td>187.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.37 <b>(-30.81%)</b></td><td>0.33 (-15.42%)</td><td>0.36 (-19.89%)</td><td>0.21 <b>(+139.53%)</b></td><td>0.07 <b>(-64.39%)</b></td><td>1033.30 <b>(-58.25%)</b></td><td>697.62 <b>(-21.17%)</b></td><td>619.40 <b>(+24.83%)</b></td><td>593.70 <b>(+44.52%)</b></td><td>188.04 <b>(-78.95%)</b></td><td>15.89 <b>(-30.81%)</b></td><td>14.13 (-15.42%)</td><td>15.24 (-19.89%)</td><td>9.13 <b>(+139.53%)</b></td><td>2.81 <b>(-64.39%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.45 (n/a)</td><td>0.09 (n/a)</td><td>0.19 (n/a)</td><td>2475.00 (n/a)</td><td>884.98 (n/a)</td><td>496.20 (n/a)</td><td>410.80 (n/a)</td><td>893.13 (n/a)</td><td>22.97 (n/a)</td><td>16.71 (n/a)</td><td>19.02 (n/a)</td><td>3.81 (n/a)</td><td>7.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.50 (-5.78%)</td><td>0.43 (-6.40%)</td><td>0.41 (-11.63%)</td><td>0.36 (-7.25%)</td><td>0.06 (+1.37%)</td><td>615.40 (+7.83%)</td><td>520.34 (+7.06%)</td><td>535.20 (+13.17%)</td><td>439.20 (+6.14%)</td><td>70.67 (+14.12%)</td><td>21.49 (-5.78%)</td><td>18.41 (-6.40%)</td><td>17.63 (-11.63%)</td><td>15.34 (-7.25%)</td><td>2.50 (+1.37%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.06 (n/a)</td><td>570.70 (n/a)</td><td>486.04 (n/a)</td><td>472.90 (n/a)</td><td>413.80 (n/a)</td><td>61.93 (n/a)</td><td>22.80 (n/a)</td><td>19.67 (n/a)</td><td>19.96 (n/a)</td><td>16.54 (n/a)</td><td>2.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.31 (-0.54%)</td><td>0.31 (-0.76%)</td><td>0.31 (-0.92%)</td><td>0.30 (-1.21%)</td><td>0.00 (+15.52%)</td><td>83736.50 (+1.23%)</td><td>82433.08 (+0.77%)</td><td>82414.90 (+0.93%)</td><td>81386.30 (+0.54%)</td><td>852.92 (+17.65%)</td><td>211.09 (-0.54%)</td><td>208.43 (-0.76%)</td><td>208.46 (-0.92%)</td><td>205.17 (-1.21%)</td><td>2.15 (+15.52%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>82720.30 (n/a)</td><td>81805.12 (n/a)</td><td>81655.50 (n/a)</td><td>80946.20 (n/a)</td><td>724.99 (n/a)</td><td>212.24 (n/a)</td><td>210.02 (n/a)</td><td>210.39 (n/a)</td><td>207.69 (n/a)</td><td>1.86 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>1.03 (+0.52%)</td><td>1.02 (+1.41%)</td><td>1.02 (+2.00%)</td><td>1.00 (+0.83%)</td><td>0.01 (-9.64%)</td><td>25186.40 (-0.83%)</td><td>24761.20 (-1.39%)</td><td>24652.60 (-1.96%)</td><td>24493.90 (-0.52%)</td><td>275.44 (-10.74%)</td><td>701.39 (+0.52%)</td><td>693.89 (+1.41%)</td><td>696.88 (+2.00%)</td><td>682.11 (+0.83%)</td><td>7.66 (-9.64%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.99 (n/a)</td><td>0.01 (n/a)</td><td>25396.10 (n/a)</td><td>25110.42 (n/a)</td><td>25146.30 (n/a)</td><td>24622.10 (n/a)</td><td>308.60 (n/a)</td><td>697.74 (n/a)</td><td>684.26 (n/a)</td><td>683.20 (n/a)</td><td>676.48 (n/a)</td><td>8.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>3.81 (+0.57%)</td><td>2.62 <b>(+20.53%)</b></td><td>2.13 <b>(+28.00%)</b></td><td>1.60 (-0.95%)</td><td>0.98 (+4.59%)</td><td>5052.20 (+0.96%)</td><td>3431.40 (-16.79%)</td><td>3791.10 <b>(-21.88%)</b></td><td>2113.70 (-0.56%)</td><td>1225.96 (-1.41%)</td><td>1000.11 (+0.57%)</td><td>687.77 <b>(+20.53%)</b></td><td>557.60 <b>(+28.00%)</b></td><td>418.42 (-0.95%)</td><td>256.51 (+4.59%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>3.79 (n/a)</td><td>2.18 (n/a)</td><td>1.66 (n/a)</td><td>1.61 (n/a)</td><td>0.94 (n/a)</td><td>5004.40 (n/a)</td><td>4124.02 (n/a)</td><td>4852.70 (n/a)</td><td>2125.70 (n/a)</td><td>1243.53 (n/a)</td><td>994.47 (n/a)</td><td>570.65 (n/a)</td><td>435.62 (n/a)</td><td>422.42 (n/a)</td><td>245.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.30 (+13.23%)</td><td>0.24 (+14.77%)</td><td>0.23 (+10.42%)</td><td>0.18 (+6.27%)</td><td>0.05 <b>(+26.28%)</b></td><td>7016.30 (-5.90%)</td><td>5334.86 (-12.21%)</td><td>5379.50 (-9.44%)</td><td>4187.00 (-11.69%)</td><td>1075.07 (+6.17%)</td><td>16.03 (+13.23%)</td><td>12.97 (+14.77%)</td><td>12.47 (+10.42%)</td><td>9.56 (+6.27%)</td><td>2.43 <b>(+26.28%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>7456.50 (n/a)</td><td>6076.94 (n/a)</td><td>5940.20 (n/a)</td><td>4741.00 (n/a)</td><td>1012.61 (n/a)</td><td>14.15 (n/a)</td><td>11.30 (n/a)</td><td>11.30 (n/a)</td><td>9.00 (n/a)</td><td>1.93 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.14 (+4.73%)</td><td>0.11 <b>(+47.58%)</b></td><td>0.12 <b>(+103.45%)</b></td><td>0.06 <b>(+22.08%)</b></td><td>0.03 (-15.10%)</td><td>0.14 (+4.73%)</td><td>0.11 <b>(+47.58%)</b></td><td>0.12 <b>(+103.45%)</b></td><td>0.06 <b>(+22.08%)</b></td><td>0.03 (-15.10%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>3.55 (-6.56%)</td><td>3.46 (-5.19%)</td><td>3.46 (-4.81%)</td><td>3.32 (-2.87%)</td><td>0.09 <b>(-41.03%)</b></td><td>3.55 (-6.56%)</td><td>3.45 (-5.19%)</td><td>3.45 (-4.81%)</td><td>3.31 (-2.87%)</td><td>0.09 <b>(-41.03%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>3.80 (n/a)</td><td>3.64 (n/a)</td><td>3.63 (n/a)</td><td>3.41 (n/a)</td><td>0.16 (n/a)</td><td>3.80 (n/a)</td><td>3.64 (n/a)</td><td>3.63 (n/a)</td><td>3.41 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>7.48 (-1.04%)</td><td>6.33 (-4.22%)</td><td>6.21 (-5.78%)</td><td>5.68 (+0.10%)</td><td>0.73 (+10.08%)</td><td>7.48 (-1.04%)</td><td>6.33 (-4.22%)</td><td>6.21 (-5.78%)</td><td>5.68 (+0.10%)</td><td>0.73 (+10.08%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>7.56 (n/a)</td><td>6.61 (n/a)</td><td>6.59 (n/a)</td><td>5.68 (n/a)</td><td>0.67 (n/a)</td><td>7.56 (n/a)</td><td>6.61 (n/a)</td><td>6.59 (n/a)</td><td>5.67 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>13.86 (-0.26%)</td><td>10.71 <b>(+23.59%)</b></td><td>10.55 <b>(+33.04%)</b></td><td>7.56 <b>(+35.34%)</b></td><td>2.93 (-6.34%)</td><td>13.85 (-0.26%)</td><td>10.71 <b>(+23.59%)</b></td><td>10.54 <b>(+33.04%)</b></td><td>7.56 <b>(+35.34%)</b></td><td>2.93 (-6.34%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>13.90 (n/a)</td><td>8.67 (n/a)</td><td>7.93 (n/a)</td><td>5.59 (n/a)</td><td>3.13 (n/a)</td><td>13.89 (n/a)</td><td>8.66 (n/a)</td><td>7.93 (n/a)</td><td>5.59 (n/a)</td><td>3.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>3.93 (+0.08%)</td><td>3.72 (+1.71%)</td><td>3.80 (+4.18%)</td><td>3.27 (-3.84%)</td><td>0.26 <b>(+36.55%)</b></td><td>3.93 (+0.08%)</td><td>3.72 (+1.71%)</td><td>3.80 (+4.18%)</td><td>3.27 (-3.84%)</td><td>0.26 <b>(+36.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>3.93 (n/a)</td><td>3.66 (n/a)</td><td>3.65 (n/a)</td><td>3.40 (n/a)</td><td>0.19 (n/a)</td><td>3.93 (n/a)</td><td>3.66 (n/a)</td><td>3.65 (n/a)</td><td>3.40 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>7.48 (-0.83%)</td><td>6.64 (+1.93%)</td><td>6.77 (-0.65%)</td><td>5.72 (+0.72%)</td><td>0.67 (-17.38%)</td><td>7.48 (-0.83%)</td><td>6.63 (+1.93%)</td><td>6.77 (-0.65%)</td><td>5.71 (+0.72%)</td><td>0.67 (-17.38%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>7.54 (n/a)</td><td>6.51 (n/a)</td><td>6.82 (n/a)</td><td>5.68 (n/a)</td><td>0.81 (n/a)</td><td>7.54 (n/a)</td><td>6.51 (n/a)</td><td>6.81 (n/a)</td><td>5.67 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>11.18 (-16.86%)</td><td>9.85 (-4.48%)</td><td>10.65 (+4.36%)</td><td>8.06 (-2.79%)</td><td>1.41 <b>(-27.19%)</b></td><td>11.18 (-16.86%)</td><td>9.84 (-4.48%)</td><td>10.64 (+4.36%)</td><td>8.06 (-2.79%)</td><td>1.41 <b>(-27.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>13.45 (n/a)</td><td>10.31 (n/a)</td><td>10.20 (n/a)</td><td>8.29 (n/a)</td><td>1.94 (n/a)</td><td>13.44 (n/a)</td><td>10.30 (n/a)</td><td>10.20 (n/a)</td><td>8.29 (n/a)</td><td>1.94 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.10 (n/a)</td><td>351.60 (n/a)</td><td>303.50 (n/a)</td><td>258.40 (n/a)</td><td>100.81 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.10 (n/a)</td><td>444.80 (n/a)</td><td>458.00 (n/a)</td><td>292.50 (n/a)</td><td>131.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.50 (n/a)</td><td>424.12 (n/a)</td><td>462.30 (n/a)</td><td>286.90 (n/a)</td><td>120.71 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.30 (n/a)</td><td>323.82 (n/a)</td><td>300.80 (n/a)</td><td>243.60 (n/a)</td><td>86.64 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>486.10 (n/a)</td><td>429.68 (n/a)</td><td>456.50 (n/a)</td><td>294.10 (n/a)</td><td>77.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.90 (n/a)</td><td>529.08 (n/a)</td><td>578.40 (n/a)</td><td>380.10 (n/a)</td><td>96.54 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-4.27%)</td><td>0.03 (+4.62%)</td><td>0.03 <b>(+25.30%)</b></td><td>0.01 (-18.01%)</td><td>0.01 (-3.98%)</td><td>576.40 <b>(+21.96%)</b></td><td>336.14 (-2.74%)</td><td>269.10 <b>(-20.17%)</b></td><td>246.40 (+4.45%)</td><td>137.63 <b>(+28.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>472.60 (n/a)</td><td>345.62 (n/a)</td><td>337.10 (n/a)</td><td>235.90 (n/a)</td><td>107.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 <b>(-31.35%)</b></td><td>0.02 (-13.61%)</td><td>0.02 <b>(-21.68%)</b></td><td>0.02 (+8.22%)</td><td>0.00 <b>(-58.85%)</b></td><td>434.00 (-7.60%)</td><td>357.16 (+5.11%)</td><td>374.10 <b>(+27.68%)</b></td><td>262.40 <b>(+45.62%)</b></td><td>63.67 <b>(-48.96%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.70 (n/a)</td><td>339.80 (n/a)</td><td>293.00 (n/a)</td><td>180.20 (n/a)</td><td>124.74 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-5.97%)</td><td>0.02 (-19.62%)</td><td>0.02 <b>(-37.96%)</b></td><td>0.02 <b>(-30.53%)</b></td><td>0.01 <b>(+75.57%)</b></td><td>545.00 <b>(+43.95%)</b></td><td>408.62 <b>(+37.16%)</b></td><td>480.40 <b>(+61.21%)</b></td><td>241.00 (+6.35%)</td><td>147.32 <b>(+165.47%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>378.60 (n/a)</td><td>297.92 (n/a)</td><td>298.00 (n/a)</td><td>226.60 (n/a)</td><td>55.49 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-2.64%)</td><td>0.02 <b>(-25.11%)</b></td><td>0.02 <b>(-41.35%)</b></td><td>0.00 <b>(-73.61%)</b></td><td>0.01 <b>(+20.04%)</b></td><td>1997.20 <b>(+278.90%)</b></td><td>714.94 <b>(+97.98%)</b></td><td>481.90 <b>(+70.46%)</b></td><td>243.60 (+2.74%)</td><td>727.43 <b>(+390.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.10 (n/a)</td><td>361.12 (n/a)</td><td>282.70 (n/a)</td><td>237.10 (n/a)</td><td>148.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 <b>(-25.55%)</b></td><td>0.02 <b>(-29.54%)</b></td><td>0.02 <b>(-26.98%)</b></td><td>0.02 (-19.43%)</td><td>0.00 <b>(-33.52%)</b></td><td>525.40 <b>(+24.12%)</b></td><td>416.66 <b>(+40.19%)</b></td><td>406.20 <b>(+36.95%)</b></td><td>304.80 <b>(+34.33%)</b></td><td>85.01 (+9.93%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>423.30 (n/a)</td><td>297.22 (n/a)</td><td>296.60 (n/a)</td><td>226.90 (n/a)</td><td>77.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (+5.01%)</td><td>0.02 <b>(-28.71%)</b></td><td>0.02 <b>(-34.98%)</b></td><td>0.01 <b>(-58.56%)</b></td><td>0.01 <b>(+26.27%)</b></td><td>1309.50 <b>(+141.29%)</b></td><td>626.08 <b>(+71.27%)</b></td><td>538.60 <b>(+53.80%)</b></td><td>229.20 (-4.78%)</td><td>404.72 <b>(+209.38%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.70 (n/a)</td><td>365.56 (n/a)</td><td>350.20 (n/a)</td><td>240.70 (n/a)</td><td>130.81 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 <b>(-41.98%)</b></td><td>0.02 <b>(-25.24%)</b></td><td>0.02 (-1.51%)</td><td>0.01 (-18.73%)</td><td>0.00 <b>(-67.56%)</b></td><td>641.10 <b>(+23.05%)</b></td><td>512.08 <b>(+23.63%)</b></td><td>492.30 (+1.53%)</td><td>405.80 <b>(+72.39%)</b></td><td>87.55 <b>(-33.52%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.00 (n/a)</td><td>414.22 (n/a)</td><td>484.90 (n/a)</td><td>235.40 (n/a)</td><td>131.71 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 (-2.90%)</td><td>0.02 (+12.87%)</td><td>0.02 <b>(+25.80%)</b></td><td>0.02 (+9.80%)</td><td>0.00 (-9.80%)</td><td>535.70 (-8.91%)</td><td>423.62 (-12.08%)</td><td>389.30 <b>(-20.52%)</b></td><td>332.40 (+3.01%)</td><td>89.28 (-10.58%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.10 (n/a)</td><td>481.80 (n/a)</td><td>489.80 (n/a)</td><td>322.70 (n/a)</td><td>99.84 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-7.78%)</td><td>0.02 <b>(-23.37%)</b></td><td>0.02 <b>(-25.93%)</b></td><td>0.02 <b>(-27.54%)</b></td><td>0.01 <b>(+41.84%)</b></td><td>504.40 <b>(+38.00%)</b></td><td>383.80 <b>(+37.49%)</b></td><td>359.90 <b>(+35.00%)</b></td><td>238.80 (+8.40%)</td><td>115.21 <b>(+117.05%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>365.50 (n/a)</td><td>279.14 (n/a)</td><td>266.60 (n/a)</td><td>220.30 (n/a)</td><td>53.08 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 <b>(+22.20%)</b></td><td>0.02 <b>(+20.36%)</b></td><td>0.02 (+9.64%)</td><td>0.02 <b>(+22.08%)</b></td><td>0.01 <b>(+34.83%)</b></td><td>490.30 (-18.08%)</td><td>357.08 (-15.58%)</td><td>375.10 (-8.80%)</td><td>218.30 (-18.18%)</td><td>108.21 (-9.03%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.50 (n/a)</td><td>422.98 (n/a)</td><td>411.30 (n/a)</td><td>266.80 (n/a)</td><td>118.94 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-11.88%)</td><td>0.02 (-13.72%)</td><td>0.02 <b>(-35.69%)</b></td><td>0.02 (+4.52%)</td><td>0.01 <b>(-26.30%)</b></td><td>479.90 (-4.33%)</td><td>376.00 (+11.49%)</td><td>418.20 <b>(+55.52%)</b></td><td>256.80 (+13.48%)</td><td>92.75 <b>(-22.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.60 (n/a)</td><td>337.26 (n/a)</td><td>268.90 (n/a)</td><td>226.30 (n/a)</td><td>119.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (+8.37%)</td><td>0.03 (+3.20%)</td><td>0.03 (-4.80%)</td><td>0.02 (+18.52%)</td><td>0.01 <b>(+26.82%)</b></td><td>514.70 (-15.64%)</td><td>337.80 (-0.68%)</td><td>288.50 (+5.02%)</td><td>200.10 (-7.70%)</td><td>146.49 (-6.50%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.10 (n/a)</td><td>340.12 (n/a)</td><td>274.70 (n/a)</td><td>216.80 (n/a)</td><td>156.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (-12.19%)</td><td>0.02 (-17.80%)</td><td>0.02 <b>(-41.75%)</b></td><td>0.01 (-6.26%)</td><td>0.01 (-8.20%)</td><td>568.60 (+6.68%)</td><td>400.42 <b>(+21.46%)</b></td><td>443.20 <b>(+71.65%)</b></td><td>233.70 (+13.83%)</td><td>142.81 (+6.18%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.00 (n/a)</td><td>329.68 (n/a)</td><td>258.20 (n/a)</td><td>205.30 (n/a)</td><td>134.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.02 <b>(-36.89%)</b></td><td>0.02 (-18.19%)</td><td>0.02 (-14.25%)</td><td>0.01 (+6.23%)</td><td>0.00 <b>(-59.05%)</b></td><td>648.40 (-5.88%)</td><td>519.36 (+11.26%)</td><td>539.70 (+16.62%)</td><td>359.10 <b>(+58.47%)</b></td><td>104.07 <b>(-36.65%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>688.90 (n/a)</td><td>466.78 (n/a)</td><td>462.80 (n/a)</td><td>226.60 (n/a)</td><td>164.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (+10.43%)</td><td>0.03 <b>(+38.71%)</b></td><td>0.03 <b>(+64.32%)</b></td><td>0.02 <b>(+59.01%)</b></td><td>0.00 <b>(-40.66%)</b></td><td>369.80 <b>(-37.11%)</b></td><td>280.76 <b>(-34.07%)</b></td><td>260.50 <b>(-39.14%)</b></td><td>235.60 (-9.45%)</td><td>52.90 <b>(-65.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.00 (n/a)</td><td>425.86 (n/a)</td><td>428.00 (n/a)</td><td>260.20 (n/a)</td><td>153.56 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.05 (-3.72%)</td><td>0.03 (-9.46%)</td><td>0.02 (-12.61%)</td><td>0.02 (+2.48%)</td><td>0.01 (-4.69%)</td><td>597.60 (-2.42%)</td><td>466.14 (+10.30%)</td><td>541.30 (+14.44%)</td><td>251.60 (+3.84%)</td><td>156.20 (+3.12%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>612.40 (n/a)</td><td>422.60 (n/a)</td><td>473.00 (n/a)</td><td>242.30 (n/a)</td><td>151.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-18.26%)</td><td>0.02 (-5.37%)</td><td>0.02 (-8.28%)</td><td>0.01 <b>(+22.62%)</b></td><td>0.01 <b>(-23.05%)</b></td><td>548.10 (-18.45%)</td><td>418.86 (-0.39%)</td><td>493.60 (+9.03%)</td><td>247.80 <b>(+22.37%)</b></td><td>145.61 <b>(-20.66%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.10 (n/a)</td><td>420.52 (n/a)</td><td>452.70 (n/a)</td><td>202.50 (n/a)</td><td>183.53 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.07 <b>(+52.07%)</b></td><td>0.04 <b>(+53.25%)</b></td><td>0.03 <b>(+89.34%)</b></td><td>0.02 (+8.83%)</td><td>0.02 <b>(+61.03%)</b></td><td>547.00 (-8.13%)</td><td>344.54 <b>(-30.85%)</b></td><td>299.20 <b>(-47.18%)</b></td><td>148.20 <b>(-34.22%)</b></td><td>152.73 (-1.52%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.40 (n/a)</td><td>498.28 (n/a)</td><td>566.40 (n/a)</td><td>225.30 (n/a)</td><td>155.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (+15.78%)</td><td>0.03 (+3.21%)</td><td>0.03 (+5.53%)</td><td>0.01 <b>(-22.93%)</b></td><td>0.01 <b>(+39.55%)</b></td><td>686.60 <b>(+29.74%)</b></td><td>379.02 (+4.72%)</td><td>284.60 (-5.23%)</td><td>235.10 (-13.63%)</td><td>184.33 <b>(+64.01%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.20 (n/a)</td><td>361.94 (n/a)</td><td>300.30 (n/a)</td><td>272.20 (n/a)</td><td>112.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 (+6.60%)</td><td>0.03 <b>(+42.12%)</b></td><td>0.03 <b>(+67.17%)</b></td><td>0.02 <b>(+83.73%)</b></td><td>0.01 (-6.38%)</td><td>587.20 <b>(-45.57%)</b></td><td>369.90 <b>(-36.58%)</b></td><td>323.40 <b>(-40.17%)</b></td><td>234.20 (-6.21%)</td><td>146.40 <b>(-52.23%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1078.80 (n/a)</td><td>583.30 (n/a)</td><td>540.50 (n/a)</td><td>249.70 (n/a)</td><td>306.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 <b>(+21.58%)</b></td><td>0.02 <b>(+54.40%)</b></td><td>0.03 <b>(+50.61%)</b></td><td>0.01 <b>(+249.05%)</b></td><td>0.01 (-19.63%)</td><td>568.60 <b>(-71.35%)</b></td><td>365.40 <b>(-52.63%)</b></td><td>327.70 <b>(-33.60%)</b></td><td>259.40 (-17.76%)</td><td>119.32 <b>(-82.58%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1984.80 (n/a)</td><td>771.40 (n/a)</td><td>493.50 (n/a)</td><td>315.40 (n/a)</td><td>685.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-18.75%)</td><td>0.02 (+2.25%)</td><td>0.02 <b>(+23.53%)</b></td><td>0.01 (+1.50%)</td><td>0.00 <b>(-43.06%)</b></td><td>644.60 (-1.48%)</td><td>478.40 (-6.79%)</td><td>464.90 (-19.05%)</td><td>357.80 <b>(+23.08%)</b></td><td>104.07 <b>(-27.25%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>654.30 (n/a)</td><td>513.26 (n/a)</td><td>574.30 (n/a)</td><td>290.70 (n/a)</td><td>143.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-18.21%)</td><td>0.02 (+2.11%)</td><td>0.02 (+16.48%)</td><td>0.02 (+8.46%)</td><td>0.01 <b>(-36.35%)</b></td><td>475.30 (-7.80%)</td><td>376.04 (-8.38%)</td><td>424.70 (-14.15%)</td><td>259.20 <b>(+22.26%)</b></td><td>93.53 <b>(-31.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.50 (n/a)</td><td>410.42 (n/a)</td><td>494.70 (n/a)</td><td>212.00 (n/a)</td><td>137.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.04 <b>(+67.47%)</b></td><td>0.03 <b>(+48.98%)</b></td><td>0.03 <b>(+63.07%)</b></td><td>0.01 (-17.84%)</td><td>0.01 <b>(+267.70%)</b></td><td>673.50 <b>(+21.72%)</b></td><td>377.96 <b>(-22.60%)</b></td><td>316.70 <b>(-38.68%)</b></td><td>224.70 <b>(-40.30%)</b></td><td>184.43 <b>(+169.89%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>553.30 (n/a)</td><td>488.32 (n/a)</td><td>516.50 (n/a)</td><td>376.40 (n/a)</td><td>68.33 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.03 (-12.87%)</td><td>0.02 <b>(-20.14%)</b></td><td>0.02 (-17.56%)</td><td>0.01 <b>(-34.82%)</b></td><td>0.01 <b>(-22.85%)</b></td><td>994.30 <b>(+53.44%)</b></td><td>578.58 <b>(+25.57%)</b></td><td>545.60 <b>(+21.30%)</b></td><td>323.90 (+14.78%)</td><td>249.69 <b>(+41.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.00 (n/a)</td><td>460.76 (n/a)</td><td>449.80 (n/a)</td><td>282.20 (n/a)</td><td>176.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.30 <b>(-21.50%)</b></td><td>0.24 (-2.04%)</td><td>0.24 <b>(+21.76%)</b></td><td>0.18 (+19.64%)</td><td>0.05 <b>(-52.96%)</b></td><td>542.50 (-16.42%)</td><td>421.44 (-7.04%)</td><td>411.30 (-17.87%)</td><td>329.10 <b>(+27.41%)</b></td><td>85.56 <b>(-48.77%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.38 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>649.10 (n/a)</td><td>453.38 (n/a)</td><td>500.80 (n/a)</td><td>258.30 (n/a)</td><td>166.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.35 (-15.38%)</td><td>0.27 (-3.23%)</td><td>0.31 <b>(+36.90%)</b></td><td>0.16 (-14.89%)</td><td>0.09 (-0.86%)</td><td>610.10 (+17.49%)</td><td>416.02 (+6.95%)</td><td>319.60 <b>(-26.97%)</b></td><td>278.20 (+18.13%)</td><td>166.35 <b>(+42.25%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>519.30 (n/a)</td><td>388.98 (n/a)</td><td>437.60 (n/a)</td><td>235.50 (n/a)</td><td>116.94 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.48 <b>(+97.59%)</b></td><td>0.27 <b>(+47.35%)</b></td><td>0.21 (+15.94%)</td><td>0.15 <b>(+73.85%)</b></td><td>0.13 <b>(+122.21%)</b></td><td>634.80 <b>(-42.48%)</b></td><td>431.30 <b>(-29.69%)</b></td><td>475.70 (-13.74%)</td><td>203.50 <b>(-49.38%)</b></td><td>168.32 <b>(-40.46%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>1103.60 (n/a)</td><td>613.44 (n/a)</td><td>551.50 (n/a)</td><td>402.00 (n/a)</td><td>282.69 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.23 (-17.52%)</td><td>0.16 <b>(-20.70%)</b></td><td>0.15 <b>(-27.50%)</b></td><td>0.12 <b>(-20.78%)</b></td><td>0.05 <b>(-24.43%)</b></td><td>632.40 <b>(+26.23%)</b></td><td>475.66 <b>(+24.53%)</b></td><td>491.80 <b>(+37.91%)</b></td><td>317.90 <b>(+21.24%)</b></td><td>124.31 (+9.42%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>501.00 (n/a)</td><td>381.96 (n/a)</td><td>356.60 (n/a)</td><td>262.20 (n/a)</td><td>113.61 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.19 <b>(-33.97%)</b></td><td>0.16 <b>(-32.25%)</b></td><td>0.15 <b>(-42.63%)</b></td><td>0.13 (-17.36%)</td><td>0.03 <b>(-48.69%)</b></td><td>584.30 <b>(+21.00%)</b></td><td>475.72 <b>(+43.16%)</b></td><td>483.30 <b>(+74.29%)</b></td><td>387.10 <b>(+51.45%)</b></td><td>88.40 (-8.50%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>482.90 (n/a)</td><td>332.30 (n/a)</td><td>277.30 (n/a)</td><td>255.60 (n/a)</td><td>96.61 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.27 (+6.27%)</td><td>0.19 (+3.92%)</td><td>0.14 <b>(-21.02%)</b></td><td>0.13 (+1.75%)</td><td>0.07 <b>(+34.23%)</b></td><td>566.30 (-1.74%)</td><td>433.40 (+0.00%)</td><td>518.60 <b>(+26.61%)</b></td><td>271.00 (-5.90%)</td><td>145.36 (+17.03%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>576.30 (n/a)</td><td>433.38 (n/a)</td><td>409.60 (n/a)</td><td>288.00 (n/a)</td><td>124.22 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.44 (-8.00%)</td><td>0.27 (-16.87%)</td><td>0.28 (+5.72%)</td><td>0.05 <b>(-75.55%)</b></td><td>0.14 <b>(+23.53%)</b></td><td>2432.90 <b>(+309.03%)</b></td><td>823.14 <b>(+86.70%)</b></td><td>470.10 (-5.41%)</td><td>296.50 (+8.69%)</td><td>903.28 <b>(+554.50%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.48 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>594.80 (n/a)</td><td>440.90 (n/a)</td><td>497.00 (n/a)</td><td>272.80 (n/a)</td><td>138.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.51 (+17.46%)</td><td>0.36 (+18.55%)</td><td>0.35 (+17.07%)</td><td>0.19 (-6.42%)</td><td>0.13 <b>(+42.90%)</b></td><td>692.30 (+6.85%)</td><td>418.28 (-10.94%)</td><td>377.40 (-14.60%)</td><td>256.30 (-14.88%)</td><td>177.01 <b>(+26.29%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>647.90 (n/a)</td><td>469.64 (n/a)</td><td>441.90 (n/a)</td><td>301.10 (n/a)</td><td>140.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.43 (-12.08%)</td><td>0.31 (-8.71%)</td><td>0.26 <b>(-36.36%)</b></td><td>0.21 <b>(+66.08%)</b></td><td>0.10 <b>(-34.31%)</b></td><td>619.50 <b>(-39.79%)</b></td><td>457.04 (-7.45%)</td><td>512.40 <b>(+57.13%)</b></td><td>303.30 (+13.77%)</td><td>137.43 <b>(-57.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.40 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>1028.90 (n/a)</td><td>493.84 (n/a)</td><td>326.10 (n/a)</td><td>266.60 (n/a)</td><td>319.61 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-30.00%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-23.72%)</b></td><td>22899.76 (+6.79%)</td><td>18458.31 <b>(+39.94%)</b></td><td>22279.89 <b>(+42.24%)</b></td><td>6727.16 (+18.40%)</td><td>6860.73 (+0.09%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21443.72 (n/a)</td><td>13189.90 (n/a)</td><td>15663.38 (n/a)</td><td>5681.54 (n/a)</td><td>6854.89 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+32.50%)</b></td><td>0.00 <b>(+33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+1.03%)</td><td>22818.84 (+18.44%)</td><td>10033.62 (-18.19%)</td><td>6883.34 <b>(-22.78%)</b></td><td>6056.00 (-14.86%)</td><td>7169.71 (+16.44%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19265.52 (n/a)</td><td>12265.28 (n/a)</td><td>8914.40 (n/a)</td><td>7112.82 (n/a)</td><td>6157.45 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>0.15 (-3.30%)</td><td>0.11 (+2.07%)</td><td>0.10 <b>(+24.81%)</b></td><td>0.08 (+4.53%)</td><td>0.03 <b>(-26.56%)</b></td><td>27574.44 (-4.24%)</td><td>20512.79 (-7.03%)</td><td>21368.30 (-19.90%)</td><td>13767.47 (+3.37%)</td><td>5456.68 <b>(-27.75%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>28796.81 (n/a)</td><td>22064.41 (n/a)</td><td>26678.69 (n/a)</td><td>13318.89 (n/a)</td><td>7552.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>1.08 (+8.05%)</td><td>0.85 <b>(+53.62%)</b></td><td>0.79 <b>(+71.29%)</b></td><td>0.62 <b>(+287.98%)</b></td><td>0.18 <b>(-56.28%)</b></td><td>842.00 <b>(-74.22%)</b></td><td>641.50 <b>(-63.27%)</b></td><td>666.70 <b>(-41.63%)</b></td><td>483.80 (-7.44%)</td><td>140.38 <b>(-90.04%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>1.00 (n/a)</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.16 (n/a)</td><td>0.42 (n/a)</td><td>3266.60 (n/a)</td><td>1746.34 (n/a)</td><td>1142.10 (n/a)</td><td>522.70 (n/a)</td><td>1409.58 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>2.46 (-10.73%)</td><td>1.76 <b>(-21.62%)</b></td><td>2.24 (-8.93%)</td><td>0.31 <b>(-79.81%)</b></td><td>0.93 <b>(+76.99%)</b></td><td>3333.70 <b>(+395.42%)</b></td><td>1085.28 <b>(+121.76%)</b></td><td>469.10 (+9.81%)</td><td>426.30 (+12.01%)</td><td>1264.95 <b>(+897.96%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>2.76 (n/a)</td><td>2.25 (n/a)</td><td>2.45 (n/a)</td><td>1.56 (n/a)</td><td>0.52 (n/a)</td><td>672.90 (n/a)</td><td>489.40 (n/a)</td><td>427.20 (n/a)</td><td>380.60 (n/a)</td><td>126.75 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 21:54:42</td><td>1.51 (-12.01%)</td><td>1.08 (-4.52%)</td><td>0.95 (-14.28%)</td><td>0.63 (+9.56%)</td><td>0.36 <b>(-20.47%)</b></td><td>832.80 (-8.73%)</td><td>534.60 (-0.38%)</td><td>553.60 (+16.65%)</td><td>347.50 (+13.67%)</td><td>193.43 <b>(-20.16%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>1.71 (n/a)</td><td>1.13 (n/a)</td><td>1.10 (n/a)</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>912.50 (n/a)</td><td>536.64 (n/a)</td><td>474.60 (n/a)</td><td>305.70 (n/a)</td><td>242.26 (n/a)</td>
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
