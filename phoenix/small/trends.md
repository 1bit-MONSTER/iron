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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (+1.93%)</td><td>0.04 (+7.07%)</td><td>0.04 (+14.21%)</td><td>0.02 <b>(+27.56%)</b></td><td>0.01 (-16.35%)</td><td>495.60 <b>(-21.61%)</b></td><td>369.86 (-10.74%)</td><td>313.40 (-12.43%)</td><td>260.60 (-1.92%)</td><td>104.97 <b>(-32.94%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>632.20 (n/a)</td><td>414.38 (n/a)</td><td>357.90 (n/a)</td><td>265.70 (n/a)</td><td>156.54 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 <b>(-23.61%)</b></td><td>0.03 (-16.69%)</td><td>0.04 (-18.01%)</td><td>0.02 <b>(+24.76%)</b></td><td>0.01 <b>(-47.33%)</b></td><td>502.80 (-19.85%)</td><td>395.36 (+9.31%)</td><td>341.00 <b>(+21.96%)</b></td><td>306.20 <b>(+30.91%)</b></td><td>97.90 <b>(-41.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>627.30 (n/a)</td><td>361.70 (n/a)</td><td>279.60 (n/a)</td><td>233.90 (n/a)</td><td>166.87 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 <b>(+80.32%)</b></td><td>0.03 <b>(+38.53%)</b></td><td>0.02 (+13.35%)</td><td>0.02 (+16.95%)</td><td>0.01 <b>(+359.53%)</b></td><td>594.10 (-14.48%)</td><td>464.10 <b>(-22.86%)</b></td><td>530.20 (-11.78%)</td><td>298.50 <b>(-44.54%)</b></td><td>131.02 <b>(+117.05%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>694.70 (n/a)</td><td>601.60 (n/a)</td><td>601.00 (n/a)</td><td>538.20 (n/a)</td><td>60.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 <b>(-31.36%)</b></td><td>0.01 <b>(-28.94%)</b></td><td>0.01 <b>(-41.25%)</b></td><td>0.01 (-10.09%)</td><td>0.00 <b>(-60.25%)</b></td><td>551.20 (+11.22%)</td><td>434.46 <b>(+28.25%)</b></td><td>426.50 <b>(+70.19%)</b></td><td>320.20 <b>(+45.68%)</b></td><td>82.94 <b>(-39.65%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>495.60 (n/a)</td><td>338.76 (n/a)</td><td>250.60 (n/a)</td><td>219.80 (n/a)</td><td>137.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (+16.30%)</td><td>0.02 <b>(+30.61%)</b></td><td>0.02 <b>(+32.43%)</b></td><td>0.01 <b>(+21.61%)</b></td><td>0.01 <b>(+29.13%)</b></td><td>432.20 (-17.77%)</td><td>282.46 <b>(-22.72%)</b></td><td>262.40 <b>(-24.49%)</b></td><td>213.50 (-14.02%)</td><td>89.92 (-11.02%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.60 (n/a)</td><td>365.48 (n/a)</td><td>347.50 (n/a)</td><td>248.30 (n/a)</td><td>101.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 <b>(-21.74%)</b></td><td>0.02 (-14.06%)</td><td>0.02 (+3.27%)</td><td>0.01 (-8.75%)</td><td>0.01 (-14.00%)</td><td>525.30 (+9.60%)</td><td>324.56 (+16.12%)</td><td>237.40 (-3.14%)</td><td>231.50 <b>(+27.76%)</b></td><td>132.36 (+11.05%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>479.30 (n/a)</td><td>279.50 (n/a)</td><td>245.10 (n/a)</td><td>181.20 (n/a)</td><td>119.19 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 <b>(+58.34%)</b></td><td>0.01 (+6.54%)</td><td>0.01 (-7.85%)</td><td>0.00 <b>(-75.21%)</b></td><td>0.01 <b>(+655.57%)</b></td><td>2134.60 <b>(+303.44%)</b></td><td>767.30 <b>(+58.86%)</b></td><td>540.60 (+8.53%)</td><td>270.80 <b>(-36.86%)</b></td><td>777.94 <b>(+1859.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.10 (n/a)</td><td>483.00 (n/a)</td><td>498.10 (n/a)</td><td>428.90 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 <b>(-25.51%)</b></td><td>0.01 <b>(-26.77%)</b></td><td>0.01 <b>(-43.40%)</b></td><td>0.01 <b>(-22.10%)</b></td><td>0.01 <b>(-23.44%)</b></td><td>605.30 <b>(+28.38%)</b></td><td>445.04 <b>(+36.22%)</b></td><td>482.20 <b>(+76.69%)</b></td><td>239.80 <b>(+34.27%)</b></td><td>163.64 <b>(+26.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>471.50 (n/a)</td><td>326.70 (n/a)</td><td>272.90 (n/a)</td><td>178.60 (n/a)</td><td>129.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.01 <b>(-27.87%)</b></td><td>0.01 (-4.48%)</td><td>0.01 (+2.60%)</td><td>0.01 <b>(+20.75%)</b></td><td>0.00 <b>(-56.14%)</b></td><td>574.20 (-17.18%)</td><td>486.80 (-4.11%)</td><td>485.40 (-2.55%)</td><td>354.20 <b>(+38.63%)</b></td><td>87.09 <b>(-46.97%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>693.30 (n/a)</td><td>507.64 (n/a)</td><td>498.10 (n/a)</td><td>255.50 (n/a)</td><td>164.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>683.40 (n/a)</td><td>381.80 (n/a)</td><td>287.00 (n/a)</td><td>245.20 (n/a)</td><td>184.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>717.10 (n/a)</td><td>511.30 (n/a)</td><td>488.30 (n/a)</td><td>336.40 (n/a)</td><td>142.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>376.06 (n/a)</td><td>329.00 (n/a)</td><td>290.00 (n/a)</td><td>116.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>581.60 (n/a)</td><td>452.12 (n/a)</td><td>433.90 (n/a)</td><td>384.90 (n/a)</td><td>77.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.90 (n/a)</td><td>461.30 (n/a)</td><td>581.80 (n/a)</td><td>263.80 (n/a)</td><td>180.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>645.90 (n/a)</td><td>556.18 (n/a)</td><td>544.10 (n/a)</td><td>514.30 (n/a)</td><td>52.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2109.30 (n/a)</td><td>803.90 (n/a)</td><td>476.90 (n/a)</td><td>385.70 (n/a)</td><td>737.56 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.50 (n/a)</td><td>423.68 (n/a)</td><td>402.30 (n/a)</td><td>240.00 (n/a)</td><td>171.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1084.20 (n/a)</td><td>535.66 (n/a)</td><td>480.50 (n/a)</td><td>294.00 (n/a)</td><td>322.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.40 (n/a)</td><td>321.82 (n/a)</td><td>295.80 (n/a)</td><td>227.50 (n/a)</td><td>92.77 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.40 (n/a)</td><td>361.78 (n/a)</td><td>312.00 (n/a)</td><td>278.90 (n/a)</td><td>120.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2053.40 (n/a)</td><td>805.98 (n/a)</td><td>543.50 (n/a)</td><td>381.10 (n/a)</td><td>701.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.54 (-0.79%)</td><td>0.39 (-4.71%)</td><td>0.45 (+15.47%)</td><td>0.09 <b>(-73.34%)</b></td><td>0.19 <b>(+121.04%)</b></td><td>2475.00 <b>(+275.06%)</b></td><td>884.98 <b>(+59.59%)</b></td><td>496.20 (-13.39%)</td><td>410.80 (+0.81%)</td><td>893.13 <b>(+780.10%)</b></td><td>22.97 (-0.79%)</td><td>16.71 (-4.71%)</td><td>19.02 (+15.47%)</td><td>3.81 <b>(-73.34%)</b></td><td>7.90 <b>(+121.04%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>659.90 (n/a)</td><td>554.54 (n/a)</td><td>572.90 (n/a)</td><td>407.50 (n/a)</td><td>101.48 (n/a)</td><td>23.16 (n/a)</td><td>17.54 (n/a)</td><td>16.47 (n/a)</td><td>14.30 (n/a)</td><td>3.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.53 (-15.14%)</td><td>0.46 (+5.53%)</td><td>0.47 (+12.48%)</td><td>0.39 <b>(+20.67%)</b></td><td>0.06 <b>(-55.45%)</b></td><td>570.70 (-17.13%)</td><td>486.04 (-10.12%)</td><td>472.90 (-11.09%)</td><td>413.80 (+17.82%)</td><td>61.93 <b>(-58.01%)</b></td><td>22.80 (-15.14%)</td><td>19.67 (+5.53%)</td><td>19.96 (+12.48%)</td><td>16.54 <b>(+20.67%)</b></td><td>2.46 <b>(-55.45%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.63 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.13 (n/a)</td><td>688.70 (n/a)</td><td>540.78 (n/a)</td><td>531.90 (n/a)</td><td>351.20 (n/a)</td><td>147.48 (n/a)</td><td>26.87 (n/a)</td><td>18.63 (n/a)</td><td>17.74 (n/a)</td><td>13.70 (n/a)</td><td>5.53 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.31 (-0.84%)</td><td>0.31 (+0.36%)</td><td>0.31 (-0.11%)</td><td>0.30 (+2.29%)</td><td>0.00 <b>(-63.35%)</b></td><td>82720.30 (-2.23%)</td><td>81805.12 (-0.40%)</td><td>81655.50 (+0.11%)</td><td>80946.20 (+0.85%)</td><td>724.99 <b>(-63.80%)</b></td><td>212.24 (-0.84%)</td><td>210.02 (+0.36%)</td><td>210.39 (-0.11%)</td><td>207.69 (+2.29%)</td><td>1.86 <b>(-63.35%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84611.30 (n/a)</td><td>82135.30 (n/a)</td><td>81566.10 (n/a)</td><td>80266.00 (n/a)</td><td>2002.97 (n/a)</td><td>214.04 (n/a)</td><td>209.26 (n/a)</td><td>210.62 (n/a)</td><td>203.04 (n/a)</td><td>5.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>1.02 (-0.82%)</td><td>1.00 (-1.48%)</td><td>1.00 (-1.84%)</td><td>0.99 (-0.76%)</td><td>0.01 (+5.43%)</td><td>25396.10 (+0.76%)</td><td>25110.42 (+1.51%)</td><td>25146.30 (+1.88%)</td><td>24622.10 (+0.83%)</td><td>308.60 (+6.84%)</td><td>697.74 (-0.82%)</td><td>684.26 (-1.48%)</td><td>683.20 (-1.84%)</td><td>676.48 (-0.76%)</td><td>8.48 (+5.43%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25203.40 (n/a)</td><td>24737.36 (n/a)</td><td>24682.70 (n/a)</td><td>24419.10 (n/a)</td><td>288.84 (n/a)</td><td>703.54 (n/a)</td><td>694.57 (n/a)</td><td>696.03 (n/a)</td><td>681.65 (n/a)</td><td>8.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>3.79 (+0.15%)</td><td>2.18 (-11.40%)</td><td>1.66 (-8.44%)</td><td>1.61 (+2.60%)</td><td>0.94 (-9.68%)</td><td>5004.40 (-2.54%)</td><td>4124.02 (+10.17%)</td><td>4852.70 (+9.22%)</td><td>2125.70 (-0.15%)</td><td>1243.53 (-9.76%)</td><td>994.47 (+0.15%)</td><td>570.65 (-11.40%)</td><td>435.62 (-8.44%)</td><td>422.42 (+2.60%)</td><td>245.25 (-9.68%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>3.79 (n/a)</td><td>2.46 (n/a)</td><td>1.81 (n/a)</td><td>1.57 (n/a)</td><td>1.04 (n/a)</td><td>5134.70 (n/a)</td><td>3743.24 (n/a)</td><td>4442.90 (n/a)</td><td>2128.80 (n/a)</td><td>1377.98 (n/a)</td><td>992.99 (n/a)</td><td>644.07 (n/a)</td><td>475.80 (n/a)</td><td>411.70 (n/a)</td><td>271.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.26 <b>(+22.74%)</b></td><td>0.21 (+3.76%)</td><td>0.21 (+3.95%)</td><td>0.17 (-9.40%)</td><td>0.04 <b>(+202.49%)</b></td><td>7456.50 (+10.38%)</td><td>6076.94 (-1.69%)</td><td>5940.20 (-3.80%)</td><td>4741.00 (-18.52%)</td><td>1012.61 <b>(+171.54%)</b></td><td>14.15 <b>(+22.74%)</b></td><td>11.30 (+3.76%)</td><td>11.30 (+3.95%)</td><td>9.00 (-9.40%)</td><td>1.93 <b>(+202.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>6755.60 (n/a)</td><td>6181.38 (n/a)</td><td>6174.70 (n/a)</td><td>5818.90 (n/a)</td><td>372.92 (n/a)</td><td>11.53 (n/a)</td><td>10.89 (n/a)</td><td>10.87 (n/a)</td><td>9.93 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.13 (+9.94%)</td><td>0.08 (+0.43%)</td><td>0.06 (-8.61%)</td><td>0.05 (-13.16%)</td><td>0.03 <b>(+31.02%)</b></td><td>0.13 (+9.94%)</td><td>0.07 (+0.43%)</td><td>0.06 (-8.61%)</td><td>0.05 (-13.16%)</td><td>0.03 <b>(+31.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>3.80 (-3.58%)</td><td>3.64 (-3.66%)</td><td>3.63 (-6.73%)</td><td>3.41 (+2.73%)</td><td>0.16 <b>(-40.15%)</b></td><td>3.80 (-3.58%)</td><td>3.64 (-3.66%)</td><td>3.63 (-6.73%)</td><td>3.41 (+2.73%)</td><td>0.16 <b>(-40.15%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>3.94 (n/a)</td><td>3.78 (n/a)</td><td>3.89 (n/a)</td><td>3.32 (n/a)</td><td>0.26 (n/a)</td><td>3.94 (n/a)</td><td>3.78 (n/a)</td><td>3.89 (n/a)</td><td>3.32 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>7.56 (+0.09%)</td><td>6.61 (-3.05%)</td><td>6.59 (-6.67%)</td><td>5.68 (+0.46%)</td><td>0.67 (-8.21%)</td><td>7.56 (+0.09%)</td><td>6.61 (-3.05%)</td><td>6.59 (-6.67%)</td><td>5.67 (+0.46%)</td><td>0.67 (-8.21%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>7.55 (n/a)</td><td>6.82 (n/a)</td><td>7.06 (n/a)</td><td>5.65 (n/a)</td><td>0.73 (n/a)</td><td>7.55 (n/a)</td><td>6.82 (n/a)</td><td>7.06 (n/a)</td><td>5.65 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>13.90 (+0.67%)</td><td>8.67 (-9.53%)</td><td>7.93 (-8.58%)</td><td>5.59 <b>(-28.48%)</b></td><td>3.13 <b>(+26.48%)</b></td><td>13.89 (+0.67%)</td><td>8.66 (-9.52%)</td><td>7.93 (-8.58%)</td><td>5.59 <b>(-28.48%)</b></td><td>3.12 <b>(+26.48%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>13.81 (n/a)</td><td>9.58 (n/a)</td><td>8.67 (n/a)</td><td>7.82 (n/a)</td><td>2.47 (n/a)</td><td>13.80 (n/a)</td><td>9.58 (n/a)</td><td>8.67 (n/a)</td><td>7.81 (n/a)</td><td>2.47 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>3.93 (-0.99%)</td><td>3.66 (-3.12%)</td><td>3.65 (-4.65%)</td><td>3.40 (-1.29%)</td><td>0.19 (-7.37%)</td><td>3.93 (-0.99%)</td><td>3.66 (-3.12%)</td><td>3.65 (-4.65%)</td><td>3.40 (-1.29%)</td><td>0.19 (-7.37%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>3.97 (n/a)</td><td>3.78 (n/a)</td><td>3.83 (n/a)</td><td>3.45 (n/a)</td><td>0.21 (n/a)</td><td>3.97 (n/a)</td><td>3.77 (n/a)</td><td>3.82 (n/a)</td><td>3.45 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>7.54 (+5.75%)</td><td>6.51 (+7.40%)</td><td>6.82 (+11.80%)</td><td>5.68 <b>(+26.06%)</b></td><td>0.81 <b>(-25.38%)</b></td><td>7.54 (+5.75%)</td><td>6.51 (+7.40%)</td><td>6.81 (+11.80%)</td><td>5.67 <b>(+26.06%)</b></td><td>0.81 <b>(-25.38%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>7.13 (n/a)</td><td>6.06 (n/a)</td><td>6.10 (n/a)</td><td>4.50 (n/a)</td><td>1.09 (n/a)</td><td>7.13 (n/a)</td><td>6.06 (n/a)</td><td>6.09 (n/a)</td><td>4.50 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>13.45 (-3.11%)</td><td>10.31 (-5.09%)</td><td>10.20 (+8.69%)</td><td>8.29 (+1.35%)</td><td>1.94 <b>(-27.44%)</b></td><td>13.44 (-3.11%)</td><td>10.30 (-5.09%)</td><td>10.20 (+8.69%)</td><td>8.29 (+1.35%)</td><td>1.94 <b>(-27.44%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>13.88 (n/a)</td><td>10.86 (n/a)</td><td>9.39 (n/a)</td><td>8.18 (n/a)</td><td>2.68 (n/a)</td><td>13.88 (n/a)</td><td>10.86 (n/a)</td><td>9.38 (n/a)</td><td>8.18 (n/a)</td><td>2.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>452.00 (n/a)</td><td>339.80 (n/a)</td><td>305.00 (n/a)</td><td>229.30 (n/a)</td><td>90.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.80 (n/a)</td><td>445.56 (n/a)</td><td>514.00 (n/a)</td><td>272.00 (n/a)</td><td>150.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.80 (n/a)</td><td>486.06 (n/a)</td><td>516.80 (n/a)</td><td>272.60 (n/a)</td><td>151.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.50 (n/a)</td><td>433.16 (n/a)</td><td>452.00 (n/a)</td><td>251.90 (n/a)</td><td>133.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.40 (n/a)</td><td>397.98 (n/a)</td><td>438.90 (n/a)</td><td>270.10 (n/a)</td><td>98.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>697.20 (n/a)</td><td>511.06 (n/a)</td><td>416.50 (n/a)</td><td>406.00 (n/a)</td><td>139.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (+7.63%)</td><td>0.03 (-3.53%)</td><td>0.02 (-12.29%)</td><td>0.02 (-3.62%)</td><td>0.01 <b>(+49.86%)</b></td><td>472.60 (+3.75%)</td><td>345.62 (+7.85%)</td><td>337.10 (+14.00%)</td><td>235.90 (-7.09%)</td><td>107.02 <b>(+36.04%)</b></td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 <b>(+35.86%)</b></td><td>0.03 (+1.55%)</td><td>0.03 (+0.46%)</td><td>0.02 (+3.82%)</td><td>0.01 <b>(+72.17%)</b></td><td>469.70 (-3.67%)</td><td>339.80 (+5.02%)</td><td>293.00 (-0.48%)</td><td>180.20 <b>(-26.39%)</b></td><td>124.74 <b>(+27.22%)</b></td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (+1.68%)</td><td>0.03 <b>(+23.34%)</b></td><td>0.03 <b>(+61.48%)</b></td><td>0.02 <b>(+68.39%)</b></td><td>0.01 <b>(-54.26%)</b></td><td>378.60 <b>(-40.62%)</b></td><td>297.92 <b>(-31.65%)</b></td><td>298.00 <b>(-38.07%)</b></td><td>226.60 (-1.65%)</td><td>55.49 <b>(-71.71%)</b></td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 <b>(+32.22%)</b></td><td>0.03 <b>(+47.43%)</b></td><td>0.03 <b>(+93.41%)</b></td><td>0.02 (+12.44%)</td><td>0.01 <b>(+84.13%)</b></td><td>527.10 (-11.05%)</td><td>361.12 <b>(-27.12%)</b></td><td>282.70 <b>(-48.29%)</b></td><td>237.10 <b>(-24.37%)</b></td><td>148.35 <b>(+27.69%)</b></td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (+18.97%)</td><td>0.03 <b>(+55.60%)</b></td><td>0.03 <b>(+85.46%)</b></td><td>0.02 <b>(+55.02%)</b></td><td>0.01 (-11.13%)</td><td>423.30 <b>(-35.50%)</b></td><td>297.22 <b>(-39.34%)</b></td><td>296.60 <b>(-46.08%)</b></td><td>226.90 (-15.96%)</td><td>77.34 <b>(-51.00%)</b></td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (-2.09%)</td><td>0.02 (-3.11%)</td><td>0.02 <b>(-21.01%)</b></td><td>0.02 (+10.65%)</td><td>0.01 (-16.83%)</td><td>542.70 (-9.63%)</td><td>365.56 (-2.81%)</td><td>350.20 <b>(+26.61%)</b></td><td>240.70 (+2.12%)</td><td>130.81 <b>(-25.64%)</b></td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (+12.51%)</td><td>0.02 (-3.57%)</td><td>0.02 <b>(-20.25%)</b></td><td>0.02 <b>(+20.62%)</b></td><td>0.01 (+12.09%)</td><td>521.00 (-17.09%)</td><td>414.22 (+3.91%)</td><td>484.90 <b>(+25.39%)</b></td><td>235.40 (-11.14%)</td><td>131.71 (-10.79%)</td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (-19.57%)</td><td>0.02 (-16.85%)</td><td>0.02 <b>(-21.78%)</b></td><td>0.01 (+12.68%)</td><td>0.00 <b>(-47.13%)</b></td><td>588.10 (-11.26%)</td><td>481.80 (+9.26%)</td><td>489.80 <b>(+27.85%)</b></td><td>322.70 <b>(+24.31%)</b></td><td>99.84 <b>(-45.36%)</b></td>
</tr>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (+2.83%)</td><td>0.03 (+18.33%)</td><td>0.03 <b>(+26.26%)</b></td><td>0.02 <b>(+44.92%)</b></td><td>0.01 <b>(-43.34%)</b></td><td>365.50 <b>(-31.00%)</b></td><td>279.14 <b>(-22.47%)</b></td><td>266.60 <b>(-20.80%)</b></td><td>220.30 (-2.74%)</td><td>53.08 <b>(-60.36%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.70 (n/a)</td><td>360.02 (n/a)</td><td>336.60 (n/a)</td><td>226.50 (n/a)</td><td>133.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (-7.98%)</td><td>0.02 (-9.31%)</td><td>0.02 (-2.91%)</td><td>0.01 (-1.47%)</td><td>0.01 (-19.68%)</td><td>598.50 (+1.49%)</td><td>422.98 (+7.32%)</td><td>411.30 (+3.01%)</td><td>266.80 (+8.68%)</td><td>118.94 (-11.77%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>394.12 (n/a)</td><td>399.30 (n/a)</td><td>245.50 (n/a)</td><td>134.81 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 <b>(+39.23%)</b></td><td>0.03 <b>(+24.29%)</b></td><td>0.03 <b>(+41.24%)</b></td><td>0.02 (-2.11%)</td><td>0.01 <b>(+154.57%)</b></td><td>501.60 (+2.16%)</td><td>337.26 (-13.45%)</td><td>268.90 <b>(-29.20%)</b></td><td>226.30 <b>(-28.18%)</b></td><td>119.73 <b>(+87.31%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>389.66 (n/a)</td><td>379.80 (n/a)</td><td>315.10 (n/a)</td><td>63.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (+12.36%)</td><td>0.03 <b>(+51.43%)</b></td><td>0.03 <b>(+90.80%)</b></td><td>0.01 <b>(+83.08%)</b></td><td>0.01 (-5.83%)</td><td>610.10 <b>(-45.38%)</b></td><td>340.12 <b>(-40.78%)</b></td><td>274.70 <b>(-47.59%)</b></td><td>216.80 (-11.00%)</td><td>156.67 <b>(-51.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1116.90 (n/a)</td><td>574.36 (n/a)</td><td>524.10 (n/a)</td><td>243.60 (n/a)</td><td>325.84 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 <b>(+40.00%)</b></td><td>0.03 <b>(+27.31%)</b></td><td>0.03 <b>(+34.00%)</b></td><td>0.02 (+12.46%)</td><td>0.01 <b>(+66.33%)</b></td><td>533.00 (-11.08%)</td><td>329.68 (-17.49%)</td><td>258.20 <b>(-25.38%)</b></td><td>205.30 <b>(-28.57%)</b></td><td>134.50 (+6.50%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.40 (n/a)</td><td>399.54 (n/a)</td><td>346.00 (n/a)</td><td>287.40 (n/a)</td><td>126.29 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (+19.52%)</td><td>0.02 (+15.29%)</td><td>0.02 (+1.13%)</td><td>0.01 <b>(+189.61%)</b></td><td>0.01 (-0.81%)</td><td>688.90 <b>(-65.47%)</b></td><td>466.78 <b>(-36.77%)</b></td><td>462.80 (-1.11%)</td><td>226.60 (-16.35%)</td><td>164.26 <b>(-76.86%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1995.00 (n/a)</td><td>738.24 (n/a)</td><td>468.00 (n/a)</td><td>270.90 (n/a)</td><td>709.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (-7.02%)</td><td>0.02 (-15.15%)</td><td>0.02 <b>(-31.90%)</b></td><td>0.01 (-16.38%)</td><td>0.01 (+1.69%)</td><td>588.00 (+19.59%)</td><td>425.86 <b>(+20.64%)</b></td><td>428.00 <b>(+46.83%)</b></td><td>260.20 (+7.57%)</td><td>153.56 <b>(+26.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.70 (n/a)</td><td>353.00 (n/a)</td><td>291.50 (n/a)</td><td>241.90 (n/a)</td><td>121.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 (-0.35%)</td><td>0.03 (-14.90%)</td><td>0.03 <b>(-42.93%)</b></td><td>0.02 (-8.24%)</td><td>0.01 (-2.50%)</td><td>612.40 (+8.97%)</td><td>422.60 (+17.58%)</td><td>473.00 <b>(+75.25%)</b></td><td>242.30 (+0.37%)</td><td>151.48 (+4.63%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>562.00 (n/a)</td><td>359.42 (n/a)</td><td>269.90 (n/a)</td><td>241.40 (n/a)</td><td>144.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (+15.34%)</td><td>0.02 (-5.60%)</td><td>0.02 <b>(-34.96%)</b></td><td>0.01 (-13.82%)</td><td>0.01 (+18.69%)</td><td>672.10 (+16.04%)</td><td>420.52 (+9.41%)</td><td>452.70 <b>(+53.72%)</b></td><td>202.50 (-13.31%)</td><td>183.53 (+10.06%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.20 (n/a)</td><td>384.34 (n/a)</td><td>294.50 (n/a)</td><td>233.60 (n/a)</td><td>166.75 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.05 <b>(+26.29%)</b></td><td>0.02 (-10.33%)</td><td>0.02 <b>(-26.09%)</b></td><td>0.02 (-5.44%)</td><td>0.01 <b>(+45.91%)</b></td><td>595.40 (+5.75%)</td><td>498.28 (+17.91%)</td><td>566.40 <b>(+35.31%)</b></td><td>225.30 <b>(-20.84%)</b></td><td>155.09 (+17.81%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>563.00 (n/a)</td><td>422.60 (n/a)</td><td>418.60 (n/a)</td><td>284.60 (n/a)</td><td>131.65 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (-3.01%)</td><td>0.02 <b>(+33.51%)</b></td><td>0.03 <b>(+61.36%)</b></td><td>0.02 <b>(+98.26%)</b></td><td>0.01 <b>(-22.70%)</b></td><td>529.20 <b>(-49.56%)</b></td><td>361.94 <b>(-34.10%)</b></td><td>300.30 <b>(-38.02%)</b></td><td>272.20 (+3.11%)</td><td>112.39 <b>(-62.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1049.10 (n/a)</td><td>549.26 (n/a)</td><td>484.50 (n/a)</td><td>264.00 (n/a)</td><td>297.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 (+9.19%)</td><td>0.02 (-14.34%)</td><td>0.02 <b>(-38.94%)</b></td><td>0.01 <b>(+86.76%)</b></td><td>0.01 (-9.46%)</td><td>1078.80 <b>(-46.46%)</b></td><td>583.30 (-14.68%)</td><td>540.50 <b>(+63.74%)</b></td><td>249.70 (-8.40%)</td><td>306.47 <b>(-59.07%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2014.80 (n/a)</td><td>683.68 (n/a)</td><td>330.10 (n/a)</td><td>272.60 (n/a)</td><td>748.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 <b>(-36.12%)</b></td><td>0.02 <b>(-35.92%)</b></td><td>0.02 (-13.94%)</td><td>0.00 <b>(-71.09%)</b></td><td>0.01 <b>(-26.86%)</b></td><td>1984.80 <b>(+245.90%)</b></td><td>771.40 <b>(+99.18%)</b></td><td>493.50 (+16.20%)</td><td>315.40 <b>(+56.53%)</b></td><td>685.01 <b>(+365.63%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.80 (n/a)</td><td>387.28 (n/a)</td><td>424.70 (n/a)</td><td>201.50 (n/a)</td><td>147.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 <b>(+29.75%)</b></td><td>0.02 (-7.58%)</td><td>0.02 <b>(-24.38%)</b></td><td>0.01 <b>(-24.25%)</b></td><td>0.01 <b>(+232.56%)</b></td><td>654.30 <b>(+32.00%)</b></td><td>513.26 (+16.69%)</td><td>574.30 <b>(+32.27%)</b></td><td>290.70 <b>(-22.93%)</b></td><td>143.06 <b>(+229.73%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>495.70 (n/a)</td><td>439.86 (n/a)</td><td>434.20 (n/a)</td><td>377.20 (n/a)</td><td>43.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.04 <b>(+94.03%)</b></td><td>0.02 <b>(+54.11%)</b></td><td>0.02 (+7.01%)</td><td>0.02 <b>(+99.15%)</b></td><td>0.01 <b>(+128.93%)</b></td><td>515.50 <b>(-49.79%)</b></td><td>410.42 <b>(-33.17%)</b></td><td>494.70 (-6.55%)</td><td>212.00 <b>(-48.46%)</b></td><td>137.43 <b>(-42.47%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1026.60 (n/a)</td><td>614.14 (n/a)</td><td>529.40 (n/a)</td><td>411.30 (n/a)</td><td>238.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.02 <b>(-29.99%)</b></td><td>0.02 <b>(-29.71%)</b></td><td>0.02 <b>(-41.03%)</b></td><td>0.02 (+4.05%)</td><td>0.00 <b>(-62.67%)</b></td><td>553.30 (-3.91%)</td><td>488.32 <b>(+32.32%)</b></td><td>516.50 <b>(+69.62%)</b></td><td>376.40 <b>(+42.85%)</b></td><td>68.33 <b>(-48.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.80 (n/a)</td><td>369.04 (n/a)</td><td>304.50 (n/a)</td><td>263.50 (n/a)</td><td>133.75 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.03 (+18.27%)</td><td>0.02 <b>(+27.77%)</b></td><td>0.02 <b>(+26.23%)</b></td><td>0.01 <b>(+67.91%)</b></td><td>0.01 (+7.21%)</td><td>648.00 <b>(-40.45%)</b></td><td>460.76 <b>(-27.10%)</b></td><td>449.80 <b>(-20.78%)</b></td><td>282.20 (-15.46%)</td><td>176.25 <b>(-44.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1088.10 (n/a)</td><td>632.02 (n/a)</td><td>567.80 (n/a)</td><td>333.80 (n/a)</td><td>315.84 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.38 (+1.31%)</td><td>0.25 (+2.33%)</td><td>0.20 (-3.75%)</td><td>0.15 <b>(+20.28%)</b></td><td>0.10 (-13.11%)</td><td>649.10 (-16.86%)</td><td>453.38 (-8.49%)</td><td>500.80 (+3.90%)</td><td>258.30 (-1.30%)</td><td>166.99 <b>(-27.64%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.38 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>780.70 (n/a)</td><td>495.44 (n/a)</td><td>482.00 (n/a)</td><td>261.70 (n/a)</td><td>230.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.42 <b>(+44.13%)</b></td><td>0.28 (+18.19%)</td><td>0.22 (-5.39%)</td><td>0.19 (-1.42%)</td><td>0.10 <b>(+145.73%)</b></td><td>519.30 (+1.45%)</td><td>388.98 (-9.80%)</td><td>437.60 (+5.70%)</td><td>235.50 <b>(-30.59%)</b></td><td>116.94 <b>(+68.98%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>511.90 (n/a)</td><td>431.24 (n/a)</td><td>414.00 (n/a)</td><td>339.30 (n/a)</td><td>69.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.24 <b>(-35.47%)</b></td><td>0.18 <b>(-36.41%)</b></td><td>0.18 <b>(-47.14%)</b></td><td>0.09 <b>(-45.35%)</b></td><td>0.06 <b>(-45.65%)</b></td><td>1103.60 <b>(+82.99%)</b></td><td>613.44 <b>(+53.98%)</b></td><td>551.50 <b>(+89.19%)</b></td><td>402.00 <b>(+54.97%)</b></td><td>282.69 <b>(+60.99%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.34 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>603.10 (n/a)</td><td>398.38 (n/a)</td><td>291.50 (n/a)</td><td>259.40 (n/a)</td><td>175.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.28 (+2.88%)</td><td>0.21 (+4.65%)</td><td>0.21 <b>(+27.10%)</b></td><td>0.15 (+3.53%)</td><td>0.06 (+0.85%)</td><td>501.00 (-3.41%)</td><td>381.96 (-4.31%)</td><td>356.60 <b>(-21.32%)</b></td><td>262.20 (-2.82%)</td><td>113.61 (+1.82%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>518.70 (n/a)</td><td>399.16 (n/a)</td><td>453.20 (n/a)</td><td>269.80 (n/a)</td><td>111.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.29 (+17.18%)</td><td>0.24 <b>(+34.98%)</b></td><td>0.27 <b>(+75.56%)</b></td><td>0.15 <b>(+34.37%)</b></td><td>0.06 (+8.00%)</td><td>482.90 <b>(-25.57%)</b></td><td>332.30 <b>(-27.19%)</b></td><td>277.30 <b>(-43.04%)</b></td><td>255.60 (-14.66%)</td><td>96.61 <b>(-30.22%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>648.80 (n/a)</td><td>456.40 (n/a)</td><td>486.80 (n/a)</td><td>299.50 (n/a)</td><td>138.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.26 (-11.69%)</td><td>0.18 (-18.40%)</td><td>0.18 <b>(-36.03%)</b></td><td>0.13 <b>(+34.68%)</b></td><td>0.05 <b>(-40.16%)</b></td><td>576.30 <b>(-25.74%)</b></td><td>433.38 (+8.26%)</td><td>409.60 <b>(+56.34%)</b></td><td>288.00 (+13.25%)</td><td>124.22 <b>(-45.13%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>776.10 (n/a)</td><td>400.32 (n/a)</td><td>262.00 (n/a)</td><td>254.30 (n/a)</td><td>226.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.48 <b>(+83.82%)</b></td><td>0.33 <b>(+41.39%)</b></td><td>0.26 (+18.21%)</td><td>0.22 (+6.84%)</td><td>0.11 <b>(+368.76%)</b></td><td>594.80 (-6.40%)</td><td>440.90 <b>(-23.27%)</b></td><td>497.00 (-15.42%)</td><td>272.80 <b>(-45.59%)</b></td><td>138.01 <b>(+134.10%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>635.50 (n/a)</td><td>574.58 (n/a)</td><td>587.60 (n/a)</td><td>501.40 (n/a)</td><td>58.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.44 (+8.72%)</td><td>0.30 (+13.26%)</td><td>0.30 (+11.21%)</td><td>0.20 <b>(+27.70%)</b></td><td>0.09 (+4.81%)</td><td>647.90 <b>(-21.68%)</b></td><td>469.64 (-13.07%)</td><td>441.90 (-10.07%)</td><td>301.10 (-8.00%)</td><td>140.16 <b>(-24.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>827.30 (n/a)</td><td>540.28 (n/a)</td><td>491.40 (n/a)</td><td>327.30 (n/a)</td><td>184.62 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.49 (+12.88%)</td><td>0.34 (+3.15%)</td><td>0.40 (+3.42%)</td><td>0.13 (+3.90%)</td><td>0.15 <b>(+20.89%)</b></td><td>1028.90 (-3.76%)</td><td>493.84 (-0.01%)</td><td>326.10 (-3.29%)</td><td>266.60 (-11.43%)</td><td>319.61 (-1.86%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.39 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>1069.10 (n/a)</td><td>493.90 (n/a)</td><td>337.20 (n/a)</td><td>301.00 (n/a)</td><td>325.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+42.86%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+31.10%)</b></td><td>21443.72 (-0.72%)</td><td>13189.90 (-16.59%)</td><td>15663.38 (-8.39%)</td><td>5681.54 (-15.15%)</td><td>6854.89 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21598.80 (n/a)</td><td>15813.49 (n/a)</td><td>17097.23 (n/a)</td><td>6695.96 (n/a)</td><td>5491.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.00 (-7.69%)</td><td>0.00 (-2.44%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-5.39%)</td><td>19265.52 (-10.23%)</td><td>12265.28 (+0.02%)</td><td>8914.40 <b>(-32.94%)</b></td><td>7112.82 (+13.27%)</td><td>6157.45 (-0.80%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21462.12 (n/a)</td><td>12263.19 (n/a)</td><td>13292.95 (n/a)</td><td>6279.46 (n/a)</td><td>6206.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>0.16 (+18.96%)</td><td>0.11 (+15.00%)</td><td>0.08 (-8.39%)</td><td>0.07 (-4.08%)</td><td>0.04 <b>(+78.71%)</b></td><td>28796.81 (+4.20%)</td><td>22064.41 (-6.61%)</td><td>26678.69 (+9.11%)</td><td>13318.89 (-15.94%)</td><td>7552.47 <b>(+57.19%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>27636.97 (n/a)</td><td>23625.81 (n/a)</td><td>24451.70 (n/a)</td><td>15844.81 (n/a)</td><td>4804.73 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>1.00 <b>(-43.62%)</b></td><td>0.55 <b>(-62.33%)</b></td><td>0.46 <b>(-69.91%)</b></td><td>0.16 <b>(-83.84%)</b></td><td>0.42 <b>(+42.14%)</b></td><td>3266.60 <b>(+518.79%)</b></td><td>1746.34 <b>(+369.65%)</b></td><td>1142.10 <b>(+232.30%)</b></td><td>522.70 <b>(+77.37%)</b></td><td>1409.58 <b>(+1445.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>1.78 (n/a)</td><td>1.47 (n/a)</td><td>1.53 (n/a)</td><td>0.99 (n/a)</td><td>0.29 (n/a)</td><td>527.90 (n/a)</td><td>371.84 (n/a)</td><td>343.70 (n/a)</td><td>294.70 (n/a)</td><td>91.18 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>2.76 (+6.55%)</td><td>2.25 (+6.13%)</td><td>2.45 <b>(+25.47%)</b></td><td>1.56 (-12.13%)</td><td>0.52 <b>(+52.04%)</b></td><td>672.90 (+13.80%)</td><td>489.40 (-3.02%)</td><td>427.20 <b>(-20.30%)</b></td><td>380.60 (-6.14%)</td><td>126.75 <b>(+62.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>2.59 (n/a)</td><td>2.12 (n/a)</td><td>1.96 (n/a)</td><td>1.77 (n/a)</td><td>0.34 (n/a)</td><td>591.30 (n/a)</td><td>504.64 (n/a)</td><td>536.00 (n/a)</td><td>405.50 (n/a)</td><td>77.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:23:11</td><td>1.71 (-13.93%)</td><td>1.13 (-15.25%)</td><td>1.10 (-11.79%)</td><td>0.57 <b>(-37.94%)</b></td><td>0.45 (+5.37%)</td><td>912.50 <b>(+61.13%)</b></td><td>536.64 <b>(+26.77%)</b></td><td>474.60 (+13.38%)</td><td>305.70 (+16.19%)</td><td>242.26 <b>(+96.01%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:38:30</td><td>1.99 (n/a)</td><td>1.34 (n/a)</td><td>1.25 (n/a)</td><td>0.93 (n/a)</td><td>0.43 (n/a)</td><td>566.30 (n/a)</td><td>423.32 (n/a)</td><td>418.60 (n/a)</td><td>263.10 (n/a)</td><td>123.59 (n/a)</td>
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
