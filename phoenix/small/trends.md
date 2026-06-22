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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (+1.88%)</td><td>0.04 (+6.40%)</td><td>0.05 (+13.62%)</td><td>0.02 <b>(+21.47%)</b></td><td>0.01 (+1.35%)</td><td>524.90 (-17.68%)</td><td>364.88 (-7.40%)</td><td>265.90 (-11.98%)</td><td>246.80 (-1.83%)</td><td>145.71 (-14.29%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>637.60 (n/a)</td><td>394.04 (n/a)</td><td>302.10 (n/a)</td><td>251.40 (n/a)</td><td>170.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.06 (+19.15%)</td><td>0.04 (-9.59%)</td><td>0.03 <b>(-48.12%)</b></td><td>0.02 (+12.12%)</td><td>0.02 (+10.94%)</td><td>529.20 (-10.80%)</td><td>396.12 (+10.56%)</td><td>477.90 <b>(+92.78%)</b></td><td>198.30 (-16.08%)</td><td>150.84 (-9.42%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>593.30 (n/a)</td><td>358.30 (n/a)</td><td>247.90 (n/a)</td><td>236.30 (n/a)</td><td>166.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (+9.98%)</td><td>0.03 (+1.76%)</td><td>0.03 <b>(-24.13%)</b></td><td>0.02 (-5.91%)</td><td>0.02 (+16.64%)</td><td>676.50 (+6.28%)</td><td>433.18 (+0.34%)</td><td>463.10 <b>(+31.79%)</b></td><td>225.50 (-9.07%)</td><td>183.68 (+1.02%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>636.50 (n/a)</td><td>431.70 (n/a)</td><td>351.40 (n/a)</td><td>248.00 (n/a)</td><td>181.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (-13.86%)</td><td>0.02 (+8.80%)</td><td>0.02 <b>(+43.57%)</b></td><td>0.01 (+9.10%)</td><td>0.00 <b>(-46.82%)</b></td><td>440.80 (-8.34%)</td><td>317.50 (-14.25%)</td><td>287.40 <b>(-30.34%)</b></td><td>264.20 (+16.08%)</td><td>70.95 <b>(-42.04%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>480.90 (n/a)</td><td>370.26 (n/a)</td><td>412.60 (n/a)</td><td>227.60 (n/a)</td><td>122.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (+8.47%)</td><td>0.02 <b>(+20.90%)</b></td><td>0.02 <b>(+59.69%)</b></td><td>0.01 (+9.20%)</td><td>0.00 (+4.55%)</td><td>447.20 (-8.42%)</td><td>329.98 (-17.72%)</td><td>285.10 <b>(-37.37%)</b></td><td>261.40 (-7.80%)</td><td>85.37 (-13.74%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.30 (n/a)</td><td>401.06 (n/a)</td><td>455.20 (n/a)</td><td>283.50 (n/a)</td><td>98.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (+0.78%)</td><td>0.01 (-5.37%)</td><td>0.01 (-15.98%)</td><td>0.01 (-6.39%)</td><td>0.01 <b>(+26.89%)</b></td><td>578.30 (+6.84%)</td><td>423.02 (+11.05%)</td><td>438.80 (+19.05%)</td><td>261.80 (-0.80%)</td><td>156.39 <b>(+34.77%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.30 (n/a)</td><td>380.92 (n/a)</td><td>368.60 (n/a)</td><td>263.90 (n/a)</td><td>116.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (-4.92%)</td><td>0.01 (-11.08%)</td><td>0.01 (+0.05%)</td><td>0.00 <b>(-70.29%)</b></td><td>0.00 <b>(+52.31%)</b></td><td>2057.20 <b>(+236.53%)</b></td><td>777.02 <b>(+59.11%)</b></td><td>472.30 (-0.06%)</td><td>332.10 (+5.16%)</td><td>721.88 <b>(+502.72%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.30 (n/a)</td><td>488.34 (n/a)</td><td>472.60 (n/a)</td><td>315.80 (n/a)</td><td>119.77 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (+0.28%)</td><td>0.02 (+7.27%)</td><td>0.02 (+2.43%)</td><td>0.01 <b>(-22.67%)</b></td><td>0.01 (+5.42%)</td><td>632.30 <b>(+29.33%)</b></td><td>333.44 (-2.91%)</td><td>271.90 (-2.37%)</td><td>244.10 (-0.29%)</td><td>167.63 <b>(+40.90%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>488.90 (n/a)</td><td>343.44 (n/a)</td><td>278.50 (n/a)</td><td>244.80 (n/a)</td><td>118.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 <b>(-21.56%)</b></td><td>0.01 (+9.15%)</td><td>0.01 <b>(+38.76%)</b></td><td>0.01 (-0.85%)</td><td>0.00 <b>(-35.32%)</b></td><td>601.90 (+0.85%)</td><td>389.90 (-12.15%)</td><td>357.40 <b>(-27.93%)</b></td><td>305.70 <b>(+27.53%)</b></td><td>122.15 (-12.06%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.80 (n/a)</td><td>443.82 (n/a)</td><td>495.90 (n/a)</td><td>239.70 (n/a)</td><td>138.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1167.60 (n/a)</td><td>526.56 (n/a)</td><td>392.70 (n/a)</td><td>261.20 (n/a)</td><td>365.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2457.90 (n/a)</td><td>790.96 (n/a)</td><td>425.80 (n/a)</td><td>177.80 (n/a)</td><td>944.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>734.30 (n/a)</td><td>516.90 (n/a)</td><td>496.20 (n/a)</td><td>243.40 (n/a)</td><td>201.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.40 (n/a)</td><td>391.10 (n/a)</td><td>446.40 (n/a)</td><td>268.40 (n/a)</td><td>104.55 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>565.90 (n/a)</td><td>503.44 (n/a)</td><td>506.70 (n/a)</td><td>424.40 (n/a)</td><td>63.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>619.80 (n/a)</td><td>458.54 (n/a)</td><td>524.10 (n/a)</td><td>240.80 (n/a)</td><td>159.31 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>737.30 (n/a)</td><td>380.50 (n/a)</td><td>294.90 (n/a)</td><td>206.10 (n/a)</td><td>212.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.70 (n/a)</td><td>452.10 (n/a)</td><td>496.60 (n/a)</td><td>222.50 (n/a)</td><td>143.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.40 (n/a)</td><td>463.74 (n/a)</td><td>440.50 (n/a)</td><td>306.50 (n/a)</td><td>128.94 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.90 (n/a)</td><td>355.14 (n/a)</td><td>317.20 (n/a)</td><td>273.20 (n/a)</td><td>87.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.70 (n/a)</td><td>457.12 (n/a)</td><td>477.00 (n/a)</td><td>251.10 (n/a)</td><td>168.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>694.00 (n/a)</td><td>460.34 (n/a)</td><td>411.90 (n/a)</td><td>260.30 (n/a)</td><td>168.24 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.66 (+3.63%)</td><td>0.46 (+10.79%)</td><td>0.45 (+15.44%)</td><td>0.33 <b>(+74.66%)</b></td><td>0.12 <b>(-27.46%)</b></td><td>670.30 <b>(-42.75%)</b></td><td>504.30 (-19.82%)</td><td>490.50 (-13.39%)</td><td>334.70 (-3.52%)</td><td>123.36 <b>(-61.88%)</b></td><td>28.19 (+3.63%)</td><td>19.72 (+10.79%)</td><td>19.24 (+15.44%)</td><td>14.08 <b>(+74.66%)</b></td><td>5.29 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.64 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>1170.80 (n/a)</td><td>628.94 (n/a)</td><td>566.30 (n/a)</td><td>346.90 (n/a)</td><td>323.64 (n/a)</td><td>27.20 (n/a)</td><td>17.80 (n/a)</td><td>16.67 (n/a)</td><td>8.06 (n/a)</td><td>7.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.40 <b>(-24.83%)</b></td><td>0.36 (-4.02%)</td><td>0.36 (-3.90%)</td><td>0.32 <b>(+145.99%)</b></td><td>0.03 <b>(-80.89%)</b></td><td>695.10 <b>(-59.35%)</b></td><td>619.70 (-19.19%)</td><td>621.30 (+4.05%)</td><td>547.00 <b>(+33.03%)</b></td><td>53.61 <b>(-90.05%)</b></td><td>17.25 <b>(-24.83%)</b></td><td>15.32 (-4.02%)</td><td>15.19 (-3.90%)</td><td>13.58 <b>(+145.99%)</b></td><td>1.33 <b>(-80.89%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.54 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>1709.90 (n/a)</td><td>766.82 (n/a)</td><td>597.10 (n/a)</td><td>411.20 (n/a)</td><td>538.94 (n/a)</td><td>22.95 (n/a)</td><td>15.96 (n/a)</td><td>15.81 (n/a)</td><td>5.52 (n/a)</td><td>6.98 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.31 (+0.83%)</td><td>0.31 (+0.26%)</td><td>0.31 (+0.19%)</td><td>0.30 (-0.46%)</td><td>0.01 <b>(+79.22%)</b></td><td>83603.40 (+0.46%)</td><td>82023.64 (-0.24%)</td><td>81903.40 (-0.19%)</td><td>80454.70 (-0.82%)</td><td>1507.16 <b>(+78.59%)</b></td><td>213.53 (+0.83%)</td><td>209.51 (+0.26%)</td><td>209.76 (+0.19%)</td><td>205.49 (-0.46%)</td><td>3.85 <b>(+79.22%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83216.60 (n/a)</td><td>82225.06 (n/a)</td><td>82057.10 (n/a)</td><td>81121.80 (n/a)</td><td>843.94 (n/a)</td><td>211.78 (n/a)</td><td>208.95 (n/a)</td><td>209.36 (n/a)</td><td>206.45 (n/a)</td><td>2.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>1.03 (+2.37%)</td><td>1.02 (+3.03%)</td><td>1.02 (+3.09%)</td><td>1.00 (+3.22%)</td><td>0.01 <b>(-29.16%)</b></td><td>25057.80 (-3.12%)</td><td>24670.26 (-2.95%)</td><td>24626.20 (-3.00%)</td><td>24437.30 (-2.32%)</td><td>230.71 <b>(-32.81%)</b></td><td>703.02 (+2.37%)</td><td>696.43 (+3.03%)</td><td>697.63 (+3.09%)</td><td>685.61 (+3.22%)</td><td>6.46 <b>(-29.16%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>1.01 (n/a)</td><td>0.99 (n/a)</td><td>0.99 (n/a)</td><td>0.97 (n/a)</td><td>0.01 (n/a)</td><td>25863.90 (n/a)</td><td>25420.24 (n/a)</td><td>25386.80 (n/a)</td><td>25017.00 (n/a)</td><td>343.35 (n/a)</td><td>686.73 (n/a)</td><td>675.93 (n/a)</td><td>676.72 (n/a)</td><td>664.24 (n/a)</td><td>9.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>3.48 (-12.27%)</td><td>2.04 <b>(-25.71%)</b></td><td>1.68 <b>(-20.39%)</b></td><td>1.33 <b>(-27.39%)</b></td><td>0.84 <b>(-22.72%)</b></td><td>6061.80 <b>(+37.73%)</b></td><td>4393.58 <b>(+32.82%)</b></td><td>4798.00 <b>(+25.61%)</b></td><td>2314.70 (+13.99%)</td><td>1382.73 (+18.25%)</td><td>913.28 (-12.27%)</td><td>534.74 <b>(-25.71%)</b></td><td>440.59 <b>(-20.39%)</b></td><td>348.73 <b>(-27.39%)</b></td><td>221.49 <b>(-22.72%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>3.97 (n/a)</td><td>2.74 (n/a)</td><td>2.11 (n/a)</td><td>1.83 (n/a)</td><td>1.09 (n/a)</td><td>4401.30 (n/a)</td><td>3307.84 (n/a)</td><td>3819.90 (n/a)</td><td>2030.60 (n/a)</td><td>1169.34 (n/a)</td><td>1041.02 (n/a)</td><td>719.80 (n/a)</td><td>553.40 (n/a)</td><td>480.30 (n/a)</td><td>286.60 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.32 <b>(+24.54%)</b></td><td>0.23 (+8.63%)</td><td>0.21 (-9.19%)</td><td>0.18 (+17.97%)</td><td>0.06 <b>(+25.26%)</b></td><td>6990.80 (-15.24%)</td><td>5658.88 (-7.83%)</td><td>5869.50 (+10.12%)</td><td>3860.40 (-19.71%)</td><td>1207.19 (-17.00%)</td><td>17.38 <b>(+24.54%)</b></td><td>12.37 (+8.63%)</td><td>11.43 (-9.19%)</td><td>9.60 (+17.97%)</td><td>3.06 <b>(+25.26%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>8247.30 (n/a)</td><td>6139.54 (n/a)</td><td>5330.30 (n/a)</td><td>4807.80 (n/a)</td><td>1454.42 (n/a)</td><td>13.96 (n/a)</td><td>11.39 (n/a)</td><td>12.59 (n/a)</td><td>8.14 (n/a)</td><td>2.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.13 (+6.54%)</td><td>0.09 <b>(+28.19%)</b></td><td>0.09 <b>(+34.94%)</b></td><td>0.06 <b>(+82.71%)</b></td><td>0.03 (-19.39%)</td><td>0.13 (+6.54%)</td><td>0.09 <b>(+28.19%)</b></td><td>0.09 <b>(+34.94%)</b></td><td>0.06 <b>(+82.71%)</b></td><td>0.03 (-19.39%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>3.91 (+1.34%)</td><td>3.61 (+0.47%)</td><td>3.75 (+4.78%)</td><td>3.31 (-0.10%)</td><td>0.27 <b>(+39.06%)</b></td><td>3.91 (+1.34%)</td><td>3.61 (+0.47%)</td><td>3.74 (+4.78%)</td><td>3.31 (-0.10%)</td><td>0.27 <b>(+39.06%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>3.86 (n/a)</td><td>3.59 (n/a)</td><td>3.58 (n/a)</td><td>3.32 (n/a)</td><td>0.20 (n/a)</td><td>3.85 (n/a)</td><td>3.59 (n/a)</td><td>3.57 (n/a)</td><td>3.32 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>7.27 (-3.47%)</td><td>6.34 (-11.14%)</td><td>6.31 (-11.44%)</td><td>5.70 (-13.29%)</td><td>0.58 <b>(+54.94%)</b></td><td>7.27 (-3.47%)</td><td>6.34 (-11.14%)</td><td>6.30 (-11.44%)</td><td>5.70 (-13.29%)</td><td>0.58 <b>(+54.94%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>7.53 (n/a)</td><td>7.13 (n/a)</td><td>7.12 (n/a)</td><td>6.57 (n/a)</td><td>0.37 (n/a)</td><td>7.53 (n/a)</td><td>7.13 (n/a)</td><td>7.12 (n/a)</td><td>6.57 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>9.53 <b>(-31.20%)</b></td><td>8.44 (-19.24%)</td><td>8.56 (-12.75%)</td><td>7.26 (-8.32%)</td><td>0.98 <b>(-61.97%)</b></td><td>9.53 <b>(-31.20%)</b></td><td>8.43 (-19.24%)</td><td>8.55 (-12.75%)</td><td>7.25 (-8.32%)</td><td>0.98 <b>(-61.97%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>13.86 (n/a)</td><td>10.45 (n/a)</td><td>9.81 (n/a)</td><td>7.92 (n/a)</td><td>2.58 (n/a)</td><td>13.85 (n/a)</td><td>10.44 (n/a)</td><td>9.80 (n/a)</td><td>7.91 (n/a)</td><td>2.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>3.92 (+3.47%)</td><td>3.76 (+6.73%)</td><td>3.77 (+1.09%)</td><td>3.64 (+18.78%)</td><td>0.11 <b>(-68.18%)</b></td><td>3.92 (+3.47%)</td><td>3.76 (+6.73%)</td><td>3.77 (+1.09%)</td><td>3.64 (+18.78%)</td><td>0.11 <b>(-68.18%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>3.79 (n/a)</td><td>3.52 (n/a)</td><td>3.73 (n/a)</td><td>3.07 (n/a)</td><td>0.33 (n/a)</td><td>3.79 (n/a)</td><td>3.52 (n/a)</td><td>3.73 (n/a)</td><td>3.07 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>6.92 (-4.18%)</td><td>6.25 (-6.15%)</td><td>6.07 (-11.30%)</td><td>5.66 (-0.03%)</td><td>0.60 (+1.37%)</td><td>6.91 (-4.18%)</td><td>6.24 (-6.15%)</td><td>6.07 (-11.30%)</td><td>5.66 (-0.03%)</td><td>0.60 (+1.37%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>7.22 (n/a)</td><td>6.66 (n/a)</td><td>6.85 (n/a)</td><td>5.66 (n/a)</td><td>0.59 (n/a)</td><td>7.22 (n/a)</td><td>6.65 (n/a)</td><td>6.84 (n/a)</td><td>5.66 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>14.12 (-0.01%)</td><td>10.88 (+1.41%)</td><td>11.61 (+6.77%)</td><td>7.39 (+4.88%)</td><td>3.32 <b>(+30.50%)</b></td><td>14.11 (-0.01%)</td><td>10.88 (+1.41%)</td><td>11.60 (+6.77%)</td><td>7.38 (+4.88%)</td><td>3.32 <b>(+30.50%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>14.12 (n/a)</td><td>10.73 (n/a)</td><td>10.88 (n/a)</td><td>7.04 (n/a)</td><td>2.54 (n/a)</td><td>14.11 (n/a)</td><td>10.73 (n/a)</td><td>10.87 (n/a)</td><td>7.04 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>289.30 (n/a)</td><td>266.92 (n/a)</td><td>266.10 (n/a)</td><td>229.50 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.60 (n/a)</td><td>404.74 (n/a)</td><td>421.20 (n/a)</td><td>232.90 (n/a)</td><td>139.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>686.00 (n/a)</td><td>449.90 (n/a)</td><td>479.50 (n/a)</td><td>278.50 (n/a)</td><td>167.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.30 (n/a)</td><td>468.42 (n/a)</td><td>487.80 (n/a)</td><td>217.90 (n/a)</td><td>147.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.30 (n/a)</td><td>402.18 (n/a)</td><td>348.40 (n/a)</td><td>240.10 (n/a)</td><td>146.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.20 (n/a)</td><td>440.82 (n/a)</td><td>449.40 (n/a)</td><td>297.90 (n/a)</td><td>139.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (-7.52%)</td><td>0.02 (-14.17%)</td><td>0.02 (-5.81%)</td><td>0.01 (-9.85%)</td><td>0.01 (-13.19%)</td><td>591.90 (+10.93%)</td><td>478.24 (+14.89%)</td><td>535.10 (+6.17%)</td><td>257.90 (+8.13%)</td><td>142.02 (+1.45%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.60 (n/a)</td><td>416.26 (n/a)</td><td>504.00 (n/a)</td><td>238.50 (n/a)</td><td>139.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (+5.91%)</td><td>0.02 (-6.35%)</td><td>0.02 <b>(-30.24%)</b></td><td>0.02 (+17.68%)</td><td>0.01 <b>(-22.27%)</b></td><td>522.60 (-15.02%)</td><td>425.62 (+0.51%)</td><td>466.30 <b>(+43.34%)</b></td><td>272.10 (-5.55%)</td><td>100.88 <b>(-39.58%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.00 (n/a)</td><td>423.44 (n/a)</td><td>325.30 (n/a)</td><td>288.10 (n/a)</td><td>166.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (-6.78%)</td><td>0.02 (+3.15%)</td><td>0.02 (+8.57%)</td><td>0.02 (+16.34%)</td><td>0.01 (-8.77%)</td><td>504.20 (-14.03%)</td><td>398.76 (-4.64%)</td><td>415.00 (-7.90%)</td><td>285.30 (+7.30%)</td><td>108.64 (-15.08%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.50 (n/a)</td><td>418.16 (n/a)</td><td>450.60 (n/a)</td><td>265.90 (n/a)</td><td>127.92 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (+8.44%)</td><td>0.02 (-12.50%)</td><td>0.02 <b>(-23.04%)</b></td><td>0.01 (-17.78%)</td><td>0.01 <b>(+37.42%)</b></td><td>694.00 <b>(+21.63%)</b></td><td>514.00 (+19.89%)</td><td>523.10 <b>(+29.93%)</b></td><td>270.10 (-7.78%)</td><td>155.85 <b>(+42.32%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.60 (n/a)</td><td>428.74 (n/a)</td><td>402.60 (n/a)</td><td>292.90 (n/a)</td><td>109.50 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (-15.63%)</td><td>0.03 (-0.40%)</td><td>0.03 (+18.19%)</td><td>0.01 <b>(-23.21%)</b></td><td>0.01 (-17.07%)</td><td>558.50 <b>(+30.25%)</b></td><td>319.32 (+0.86%)</td><td>252.80 (-15.39%)</td><td>228.70 (+18.50%)</td><td>136.88 <b>(+26.07%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>428.80 (n/a)</td><td>316.60 (n/a)</td><td>298.80 (n/a)</td><td>193.00 (n/a)</td><td>108.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 <b>(-34.82%)</b></td><td>0.01 <b>(-22.78%)</b></td><td>0.01 (-1.91%)</td><td>0.01 <b>(-37.11%)</b></td><td>0.01 <b>(-38.16%)</b></td><td>992.80 <b>(+59.03%)</b></td><td>622.66 <b>(+28.48%)</b></td><td>573.30 (+1.94%)</td><td>381.20 <b>(+53.40%)</b></td><td>239.16 <b>(+53.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.30 (n/a)</td><td>484.62 (n/a)</td><td>562.40 (n/a)</td><td>248.50 (n/a)</td><td>156.26 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (-5.55%)</td><td>0.02 <b>(-22.39%)</b></td><td>0.02 <b>(-33.53%)</b></td><td>0.01 <b>(-40.43%)</b></td><td>0.01 <b>(+23.73%)</b></td><td>926.50 <b>(+67.91%)</b></td><td>536.26 <b>(+45.07%)</b></td><td>537.40 <b>(+50.45%)</b></td><td>251.70 (+5.85%)</td><td>263.01 <b>(+115.63%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.80 (n/a)</td><td>369.66 (n/a)</td><td>357.20 (n/a)</td><td>237.80 (n/a)</td><td>121.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 <b>(+46.89%)</b></td><td>0.03 <b>(+28.75%)</b></td><td>0.03 <b>(+54.84%)</b></td><td>0.02 <b>(-27.25%)</b></td><td>0.02 <b>(+125.81%)</b></td><td>809.00 <b>(+37.44%)</b></td><td>441.06 (-9.90%)</td><td>360.50 <b>(-35.43%)</b></td><td>233.10 <b>(-31.92%)</b></td><td>233.25 <b>(+110.20%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.60 (n/a)</td><td>489.52 (n/a)</td><td>558.30 (n/a)</td><td>342.40 (n/a)</td><td>110.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (+0.20%)</td><td>0.02 (+3.17%)</td><td>0.02 (+4.84%)</td><td>0.01 (-18.76%)</td><td>0.01 (+1.54%)</td><td>773.80 <b>(+23.08%)</b></td><td>499.60 (-1.16%)</td><td>497.20 (-4.60%)</td><td>255.60 (-0.20%)</td><td>185.21 <b>(+25.19%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.70 (n/a)</td><td>505.44 (n/a)</td><td>521.20 (n/a)</td><td>256.10 (n/a)</td><td>147.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 <b>(-46.02%)</b></td><td>0.02 <b>(-39.43%)</b></td><td>0.02 (-8.31%)</td><td>0.01 <b>(-68.57%)</b></td><td>0.01 <b>(-47.32%)</b></td><td>1851.60 <b>(+218.20%)</b></td><td>722.74 <b>(+90.61%)</b></td><td>478.40 (+9.07%)</td><td>262.30 <b>(+85.24%)</b></td><td>640.71 <b>(+254.45%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>581.90 (n/a)</td><td>379.18 (n/a)</td><td>438.60 (n/a)</td><td>141.60 (n/a)</td><td>180.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (+1.33%)</td><td>0.02 <b>(+25.64%)</b></td><td>0.02 <b>(+49.12%)</b></td><td>0.01 <b>(+305.79%)</b></td><td>0.01 <b>(-23.81%)</b></td><td>602.30 <b>(-75.36%)</b></td><td>412.64 <b>(-49.85%)</b></td><td>331.60 <b>(-32.94%)</b></td><td>275.60 (-1.32%)</td><td>155.83 <b>(-82.94%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2444.20 (n/a)</td><td>822.84 (n/a)</td><td>494.50 (n/a)</td><td>279.30 (n/a)</td><td>913.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 <b>(-37.20%)</b></td><td>0.03 (-16.53%)</td><td>0.02 (-17.77%)</td><td>0.02 (-6.48%)</td><td>0.01 <b>(-50.07%)</b></td><td>556.20 (+6.94%)</td><td>411.20 (+10.67%)</td><td>443.20 <b>(+21.59%)</b></td><td>269.90 <b>(+59.23%)</b></td><td>117.35 (-12.00%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>520.10 (n/a)</td><td>371.56 (n/a)</td><td>364.50 (n/a)</td><td>169.50 (n/a)</td><td>133.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (+16.86%)</td><td>0.02 <b>(+62.60%)</b></td><td>0.03 <b>(+109.00%)</b></td><td>0.01 <b>(+217.27%)</b></td><td>0.01 (-11.37%)</td><td>623.90 <b>(-68.48%)</b></td><td>377.46 <b>(-54.45%)</b></td><td>305.70 <b>(-52.14%)</b></td><td>229.30 (-14.41%)</td><td>157.43 <b>(-76.57%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1979.40 (n/a)</td><td>828.60 (n/a)</td><td>638.80 (n/a)</td><td>267.90 (n/a)</td><td>671.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 <b>(-62.94%)</b></td><td>0.02 <b>(-40.16%)</b></td><td>0.02 <b>(-39.55%)</b></td><td>0.01 (-7.27%)</td><td>0.00 <b>(-90.86%)</b></td><td>645.10 (+7.84%)</td><td>579.08 <b>(+41.78%)</b></td><td>581.00 <b>(+65.43%)</b></td><td>526.70 <b>(+169.83%)</b></td><td>43.73 <b>(-74.84%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.20 (n/a)</td><td>408.44 (n/a)</td><td>351.20 (n/a)</td><td>195.20 (n/a)</td><td>173.77 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (-3.28%)</td><td>0.02 (-7.13%)</td><td>0.02 (+1.04%)</td><td>0.00 <b>(-76.10%)</b></td><td>0.01 <b>(+29.36%)</b></td><td>2372.10 <b>(+318.43%)</b></td><td>789.76 <b>(+81.05%)</b></td><td>500.20 (-1.03%)</td><td>220.80 (+3.37%)</td><td>895.19 <b>(+528.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.90 (n/a)</td><td>436.22 (n/a)</td><td>505.40 (n/a)</td><td>213.60 (n/a)</td><td>142.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (+13.18%)</td><td>0.03 <b>(+60.01%)</b></td><td>0.03 <b>(+108.08%)</b></td><td>0.02 <b>(+45.97%)</b></td><td>0.01 (-15.64%)</td><td>430.70 <b>(-31.48%)</b></td><td>293.12 <b>(-40.45%)</b></td><td>266.10 <b>(-51.95%)</b></td><td>238.40 (-11.67%)</td><td>78.37 <b>(-45.27%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.60 (n/a)</td><td>492.22 (n/a)</td><td>553.80 (n/a)</td><td>269.90 (n/a)</td><td>143.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (-7.55%)</td><td>0.02 (-1.38%)</td><td>0.02 (-3.31%)</td><td>0.01 <b>(+46.53%)</b></td><td>0.01 (-17.01%)</td><td>651.30 <b>(-31.76%)</b></td><td>491.86 (-7.50%)</td><td>497.20 (+3.41%)</td><td>236.00 (+8.16%)</td><td>159.27 <b>(-40.19%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>954.40 (n/a)</td><td>531.76 (n/a)</td><td>480.80 (n/a)</td><td>218.20 (n/a)</td><td>266.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.42 <b>(+20.97%)</b></td><td>0.26 (+2.03%)</td><td>0.22 (-9.26%)</td><td>0.13 (-12.41%)</td><td>0.12 <b>(+39.38%)</b></td><td>776.70 (+14.17%)</td><td>464.78 (+6.12%)</td><td>439.60 (+10.20%)</td><td>231.60 (-17.34%)</td><td>220.81 <b>(+32.48%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>680.30 (n/a)</td><td>437.96 (n/a)</td><td>398.90 (n/a)</td><td>280.20 (n/a)</td><td>166.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.29 <b>(+21.58%)</b></td><td>0.18 (-9.57%)</td><td>0.20 (+0.67%)</td><td>0.05 <b>(-69.56%)</b></td><td>0.09 <b>(+220.36%)</b></td><td>1947.60 <b>(+228.49%)</b></td><td>780.52 <b>(+54.59%)</b></td><td>502.90 (-0.67%)</td><td>342.80 (-17.75%)</td><td>660.10 <b>(+883.42%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>592.90 (n/a)</td><td>504.90 (n/a)</td><td>506.30 (n/a)</td><td>416.80 (n/a)</td><td>67.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.27 (+6.91%)</td><td>0.19 (-5.74%)</td><td>0.17 (-12.12%)</td><td>0.15 (-10.95%)</td><td>0.05 <b>(+44.54%)</b></td><td>642.00 (+12.28%)</td><td>543.60 (+8.14%)</td><td>569.70 (+13.78%)</td><td>367.50 (-6.46%)</td><td>103.56 <b>(+44.10%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>571.80 (n/a)</td><td>502.68 (n/a)</td><td>500.70 (n/a)</td><td>392.90 (n/a)</td><td>71.87 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.19 (-17.48%)</td><td>0.16 (+13.86%)</td><td>0.17 (+13.25%)</td><td>0.14 <b>(+280.09%)</b></td><td>0.02 <b>(-71.02%)</b></td><td>513.70 <b>(-73.69%)</b></td><td>452.50 <b>(-39.33%)</b></td><td>431.40 (-11.71%)</td><td>387.40 <b>(+21.18%)</b></td><td>55.16 <b>(-91.87%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.07 (n/a)</td><td>1952.40 (n/a)</td><td>745.78 (n/a)</td><td>488.60 (n/a)</td><td>319.70 (n/a)</td><td>678.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.26 <b>(-27.34%)</b></td><td>0.15 <b>(-38.88%)</b></td><td>0.13 <b>(-24.17%)</b></td><td>0.04 <b>(-76.64%)</b></td><td>0.08 (-14.18%)</td><td>1947.80 <b>(+328.09%)</b></td><td>763.12 <b>(+120.40%)</b></td><td>557.40 <b>(+31.87%)</b></td><td>288.00 <b>(+37.60%)</b></td><td>675.98 <b>(+460.22%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>455.00 (n/a)</td><td>346.24 (n/a)</td><td>422.70 (n/a)</td><td>209.30 (n/a)</td><td>120.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.24 (-12.08%)</td><td>0.18 (-9.81%)</td><td>0.14 <b>(-30.04%)</b></td><td>0.13 (+8.44%)</td><td>0.05 <b>(-28.95%)</b></td><td>563.50 (-7.77%)</td><td>443.88 (+4.43%)</td><td>509.60 <b>(+42.95%)</b></td><td>309.50 (+13.74%)</td><td>118.40 <b>(-30.11%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>611.00 (n/a)</td><td>425.06 (n/a)</td><td>356.50 (n/a)</td><td>272.10 (n/a)</td><td>169.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.39 (-12.80%)</td><td>0.24 <b>(-21.52%)</b></td><td>0.26 (-10.53%)</td><td>0.06 <b>(-62.21%)</b></td><td>0.14 <b>(+33.38%)</b></td><td>2025.90 <b>(+164.62%)</b></td><td>861.80 <b>(+79.52%)</b></td><td>501.30 (+11.77%)</td><td>335.80 (+14.69%)</td><td>716.33 <b>(+289.27%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.45 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>765.60 (n/a)</td><td>480.06 (n/a)</td><td>448.50 (n/a)</td><td>292.80 (n/a)</td><td>184.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.44 (-6.34%)</td><td>0.29 (-11.52%)</td><td>0.28 <b>(-20.52%)</b></td><td>0.19 (+3.25%)</td><td>0.09 (-12.36%)</td><td>688.90 (-3.14%)</td><td>487.82 (+10.49%)</td><td>472.20 <b>(+25.82%)</b></td><td>300.10 (+6.80%)</td><td>148.59 (-12.35%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>711.20 (n/a)</td><td>441.52 (n/a)</td><td>375.30 (n/a)</td><td>281.00 (n/a)</td><td>169.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.51 <b>(-27.76%)</b></td><td>0.30 <b>(-31.14%)</b></td><td>0.25 <b>(-37.98%)</b></td><td>0.16 <b>(-41.68%)</b></td><td>0.15 (-10.38%)</td><td>824.00 <b>(+71.49%)</b></td><td>515.14 <b>(+57.70%)</b></td><td>517.40 <b>(+61.23%)</b></td><td>257.50 <b>(+38.44%)</b></td><td>230.46 <b>(+114.84%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.70 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>480.50 (n/a)</td><td>326.66 (n/a)</td><td>320.90 (n/a)</td><td>186.00 (n/a)</td><td>107.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.00 (+14.29%)</td><td>0.00 <b>(+29.41%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+21.04%)</b></td><td>17782.11 <b>(-22.13%)</b></td><td>11725.34 <b>(-23.69%)</b></td><td>13775.42 (-10.98%)</td><td>5176.26 (-17.19%)</td><td>5279.68 (-12.27%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22834.34 (n/a)</td><td>15364.62 (n/a)</td><td>15474.57 (n/a)</td><td>6250.44 (n/a)</td><td>6018.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.00 <b>(+133.33%)</b></td><td>0.00 <b>(+88.46%)</b></td><td>0.00 <b>(+140.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+437.19%)</b></td><td>18997.36 (-1.26%)</td><td>10218.74 <b>(-36.60%)</b></td><td>7013.58 <b>(-58.22%)</b></td><td>5985.05 <b>(-55.61%)</b></td><td>5646.66 <b>(+144.97%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19240.68 (n/a)</td><td>16117.52 (n/a)</td><td>16788.38 (n/a)</td><td>13481.94 (n/a)</td><td>2305.00 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.13 (-4.96%)</td><td>0.09 (-8.13%)</td><td>0.08 (-10.62%)</td><td>0.08 (-8.65%)</td><td>0.02 (+3.33%)</td><td>27199.35 (+9.42%)</td><td>23890.15 (+9.56%)</td><td>25953.98 (+11.91%)</td><td>16350.74 (+5.26%)</td><td>4391.76 (+19.54%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>24856.64 (n/a)</td><td>21805.69 (n/a)</td><td>23192.07 (n/a)</td><td>15534.00 (n/a)</td><td>3674.02 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>1.09 <b>(-32.64%)</b></td><td>1.03 (-5.64%)</td><td>1.04 (-5.85%)</td><td>0.97 <b>(+500.21%)</b></td><td>0.05 <b>(-91.52%)</b></td><td>541.80 <b>(-83.34%)</b></td><td>512.04 <b>(-48.01%)</b></td><td>502.10 (+6.22%)</td><td>481.70 <b>(+48.44%)</b></td><td>25.22 <b>(-98.01%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>1.62 (n/a)</td><td>1.09 (n/a)</td><td>1.11 (n/a)</td><td>0.16 (n/a)</td><td>0.59 (n/a)</td><td>3251.70 (n/a)</td><td>984.96 (n/a)</td><td>472.70 (n/a)</td><td>324.50 (n/a)</td><td>1270.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>2.09 <b>(+42.62%)</b></td><td>1.22 (+14.06%)</td><td>1.04 (+8.33%)</td><td>0.51 <b>(-40.85%)</b></td><td>0.59 <b>(+147.17%)</b></td><td>1018.50 <b>(+69.07%)</b></td><td>529.80 (+4.78%)</td><td>504.00 (-7.69%)</td><td>251.40 <b>(-29.87%)</b></td><td>294.28 <b>(+206.40%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:50:48</td><td>1.46 (n/a)</td><td>1.07 (n/a)</td><td>0.96 (n/a)</td><td>0.87 (n/a)</td><td>0.24 (n/a)</td><td>602.40 (n/a)</td><td>505.64 (n/a)</td><td>546.00 (n/a)</td><td>358.50 (n/a)</td><td>96.04 (n/a)</td>
</tr>
</tbody>
</table>


</details>
