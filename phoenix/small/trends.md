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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (-10.95%)</td><td>0.04 (+7.59%)</td><td>0.04 <b>(+39.00%)</b></td><td>0.02 (+9.13%)</td><td>0.01 <b>(-23.25%)</b></td><td>513.20 (-8.37%)</td><td>348.88 (-11.40%)</td><td>279.00 <b>(-28.06%)</b></td><td>252.40 (+12.28%)</td><td>114.05 <b>(-22.86%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.10 (n/a)</td><td>393.78 (n/a)</td><td>387.80 (n/a)</td><td>224.80 (n/a)</td><td>147.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (+19.34%)</td><td>0.04 (+15.76%)</td><td>0.04 (+6.99%)</td><td>0.03 <b>(+27.59%)</b></td><td>0.01 (+16.67%)</td><td>414.90 <b>(-21.63%)</b></td><td>306.26 (-14.16%)</td><td>281.10 (-6.55%)</td><td>225.60 (-16.20%)</td><td>86.56 <b>(-22.68%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.40 (n/a)</td><td>356.76 (n/a)</td><td>300.80 (n/a)</td><td>269.20 (n/a)</td><td>111.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (+2.73%)</td><td>0.03 <b>(-20.77%)</b></td><td>0.02 <b>(-47.57%)</b></td><td>0.02 (-12.20%)</td><td>0.01 (+17.10%)</td><td>637.90 (+13.89%)</td><td>450.00 <b>(+31.94%)</b></td><td>508.30 <b>(+90.73%)</b></td><td>230.10 (-2.66%)</td><td>169.97 <b>(+27.25%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.10 (n/a)</td><td>341.06 (n/a)</td><td>266.50 (n/a)</td><td>236.40 (n/a)</td><td>133.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (-1.02%)</td><td>0.01 (-14.69%)</td><td>0.01 <b>(-23.62%)</b></td><td>0.01 <b>(-32.16%)</b></td><td>0.01 (+12.74%)</td><td>718.20 <b>(+47.41%)</b></td><td>440.20 <b>(+24.59%)</b></td><td>359.30 <b>(+30.94%)</b></td><td>269.60 (+1.01%)</td><td>191.27 <b>(+68.37%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.20 (n/a)</td><td>353.32 (n/a)</td><td>274.40 (n/a)</td><td>266.90 (n/a)</td><td>113.60 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (+2.78%)</td><td>0.01 (-17.62%)</td><td>0.01 <b>(-44.17%)</b></td><td>0.01 (-13.22%)</td><td>0.01 (+5.60%)</td><td>620.30 (+15.23%)</td><td>433.14 <b>(+24.93%)</b></td><td>477.20 <b>(+79.13%)</b></td><td>228.10 (-2.73%)</td><td>170.01 <b>(+20.65%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.30 (n/a)</td><td>346.72 (n/a)</td><td>266.40 (n/a)</td><td>234.50 (n/a)</td><td>140.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (-1.59%)</td><td>0.02 (-11.24%)</td><td>0.02 (-19.03%)</td><td>0.01 (-1.18%)</td><td>0.00 (-2.98%)</td><td>461.10 (+1.18%)</td><td>347.98 (+12.27%)</td><td>346.60 <b>(+23.52%)</b></td><td>268.00 (+1.59%)</td><td>78.55 (-4.25%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.70 (n/a)</td><td>309.94 (n/a)</td><td>280.60 (n/a)</td><td>263.80 (n/a)</td><td>82.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 <b>(-29.47%)</b></td><td>0.01 <b>(-29.99%)</b></td><td>0.01 <b>(-33.11%)</b></td><td>0.01 (-7.46%)</td><td>0.00 <b>(-52.39%)</b></td><td>604.30 (+8.07%)</td><td>512.06 <b>(+30.40%)</b></td><td>578.50 <b>(+49.48%)</b></td><td>326.90 <b>(+41.76%)</b></td><td>115.67 <b>(-27.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.20 (n/a)</td><td>392.68 (n/a)</td><td>387.00 (n/a)</td><td>230.60 (n/a)</td><td>158.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (+18.67%)</td><td>0.01 (-11.48%)</td><td>0.01 <b>(-21.43%)</b></td><td>0.01 (-16.20%)</td><td>0.01 <b>(+45.13%)</b></td><td>629.50 (+19.34%)</td><td>490.92 <b>(+21.02%)</b></td><td>534.60 <b>(+27.29%)</b></td><td>224.30 (-15.74%)</td><td>164.62 <b>(+39.42%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.50 (n/a)</td><td>405.66 (n/a)</td><td>420.00 (n/a)</td><td>266.20 (n/a)</td><td>118.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (-17.49%)</td><td>0.01 <b>(-37.30%)</b></td><td>0.01 <b>(-38.22%)</b></td><td>0.00 <b>(-70.43%)</b></td><td>0.00 (+17.43%)</td><td>2091.60 <b>(+238.23%)</b></td><td>819.42 <b>(+114.60%)</b></td><td>509.00 <b>(+61.84%)</b></td><td>348.00 <b>(+21.17%)</b></td><td>719.33 <b>(+426.90%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.40 (n/a)</td><td>381.84 (n/a)</td><td>314.50 (n/a)</td><td>287.20 (n/a)</td><td>136.52 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1862.30 (n/a)</td><td>697.66 (n/a)</td><td>452.70 (n/a)</td><td>233.80 (n/a)</td><td>668.43 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>610.90 (n/a)</td><td>417.90 (n/a)</td><td>409.70 (n/a)</td><td>295.80 (n/a)</td><td>132.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.60 (n/a)</td><td>383.78 (n/a)</td><td>324.40 (n/a)</td><td>230.40 (n/a)</td><td>137.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>653.90 (n/a)</td><td>454.16 (n/a)</td><td>481.20 (n/a)</td><td>245.20 (n/a)</td><td>155.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.90 (n/a)</td><td>484.12 (n/a)</td><td>519.30 (n/a)</td><td>298.30 (n/a)</td><td>119.93 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>717.30 (n/a)</td><td>493.76 (n/a)</td><td>482.50 (n/a)</td><td>331.30 (n/a)</td><td>165.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.50 (n/a)</td><td>411.88 (n/a)</td><td>398.40 (n/a)</td><td>310.30 (n/a)</td><td>101.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>640.40 (n/a)</td><td>518.82 (n/a)</td><td>504.40 (n/a)</td><td>446.00 (n/a)</td><td>72.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.20 (n/a)</td><td>374.26 (n/a)</td><td>361.80 (n/a)</td><td>251.00 (n/a)</td><td>115.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1365.70 (n/a)</td><td>678.00 (n/a)</td><td>505.90 (n/a)</td><td>333.50 (n/a)</td><td>427.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.70 (n/a)</td><td>314.78 (n/a)</td><td>278.50 (n/a)</td><td>164.00 (n/a)</td><td>168.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.60 (n/a)</td><td>559.52 (n/a)</td><td>593.10 (n/a)</td><td>392.90 (n/a)</td><td>106.60 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.48 <b>(-20.79%)</b></td><td>0.35 (+11.73%)</td><td>0.37 <b>(+68.71%)</b></td><td>0.12 (-2.97%)</td><td>0.14 <b>(-27.09%)</b></td><td>1846.80 (+3.06%)</td><td>813.00 (-14.89%)</td><td>602.90 <b>(-40.72%)</b></td><td>456.70 <b>(+26.26%)</b></td><td>584.24 (+4.90%)</td><td>20.67 <b>(-20.79%)</b></td><td>14.96 (+11.73%)</td><td>15.65 <b>(+68.71%)</b></td><td>5.11 (-2.97%)</td><td>6.12 <b>(-27.09%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.61 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.20 (n/a)</td><td>1791.90 (n/a)</td><td>955.22 (n/a)</td><td>1017.10 (n/a)</td><td>361.70 (n/a)</td><td>556.93 (n/a)</td><td>26.09 (n/a)</td><td>13.39 (n/a)</td><td>9.28 (n/a)</td><td>5.27 (n/a)</td><td>8.39 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.62 (+6.81%)</td><td>0.40 (-1.98%)</td><td>0.35 (-15.54%)</td><td>0.26 <b>(+106.62%)</b></td><td>0.14 <b>(-21.04%)</b></td><td>846.80 <b>(-51.60%)</b></td><td>606.14 (-17.39%)</td><td>639.30 (+18.39%)</td><td>355.30 (-6.38%)</td><td>183.96 <b>(-67.95%)</b></td><td>26.56 (+6.81%)</td><td>16.96 (-1.98%)</td><td>14.76 (-15.54%)</td><td>11.14 <b>(+106.62%)</b></td><td>5.95 <b>(-21.04%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.58 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td><td>1749.70 (n/a)</td><td>733.74 (n/a)</td><td>540.00 (n/a)</td><td>379.50 (n/a)</td><td>573.96 (n/a)</td><td>24.87 (n/a)</td><td>17.30 (n/a)</td><td>17.48 (n/a)</td><td>5.39 (n/a)</td><td>7.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.31 (+0.30%)</td><td>0.31 (+0.21%)</td><td>0.31 (+0.41%)</td><td>0.30 (+0.41%)</td><td>0.00 (-10.00%)</td><td>83104.60 (-0.41%)</td><td>82234.64 (-0.21%)</td><td>82290.90 (-0.41%)</td><td>81257.80 (-0.30%)</td><td>694.28 (-10.60%)</td><td>211.42 (+0.30%)</td><td>208.92 (+0.21%)</td><td>208.77 (+0.41%)</td><td>206.73 (+0.41%)</td><td>1.77 (-10.00%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83445.30 (n/a)</td><td>82408.10 (n/a)</td><td>82625.90 (n/a)</td><td>81500.30 (n/a)</td><td>776.60 (n/a)</td><td>210.80 (n/a)</td><td>208.49 (n/a)</td><td>207.92 (n/a)</td><td>205.88 (n/a)</td><td>1.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>1.03 (+0.28%)</td><td>1.00 (-0.90%)</td><td>1.01 (-0.08%)</td><td>0.98 (-2.59%)</td><td>0.02 <b>(+108.87%)</b></td><td>25712.10 (+2.66%)</td><td>25069.80 (+0.94%)</td><td>24884.80 (+0.08%)</td><td>24324.90 (-0.28%)</td><td>561.43 <b>(+114.60%)</b></td><td>706.27 (+0.28%)</td><td>685.56 (-0.90%)</td><td>690.37 (-0.08%)</td><td>668.16 (-2.59%)</td><td>15.39 <b>(+108.88%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25047.00 (n/a)</td><td>24836.22 (n/a)</td><td>24865.80 (n/a)</td><td>24392.80 (n/a)</td><td>261.62 (n/a)</td><td>704.30 (n/a)</td><td>691.79 (n/a)</td><td>690.90 (n/a)</td><td>685.91 (n/a)</td><td>7.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>3.67 (-0.20%)</td><td>2.10 <b>(-25.08%)</b></td><td>1.82 <b>(-32.54%)</b></td><td>1.55 (+13.80%)</td><td>0.89 (-6.79%)</td><td>5204.60 (-12.13%)</td><td>4243.26 <b>(+29.34%)</b></td><td>4427.90 <b>(+48.23%)</b></td><td>2198.50 (+0.21%)</td><td>1194.90 <b>(-22.22%)</b></td><td>961.53 (-0.20%)</td><td>549.90 <b>(-25.08%)</b></td><td>477.41 <b>(-32.54%)</b></td><td>406.17 (+13.80%)</td><td>232.38 (-6.79%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>3.67 (n/a)</td><td>2.80 (n/a)</td><td>2.70 (n/a)</td><td>1.36 (n/a)</td><td>0.95 (n/a)</td><td>5922.80 (n/a)</td><td>3280.76 (n/a)</td><td>2987.20 (n/a)</td><td>2194.00 (n/a)</td><td>1536.17 (n/a)</td><td>963.49 (n/a)</td><td>733.96 (n/a)</td><td>707.66 (n/a)</td><td>356.91 (n/a)</td><td>249.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.31 (+2.74%)</td><td>0.22 (-9.85%)</td><td>0.21 <b>(-23.43%)</b></td><td>0.15 (-6.50%)</td><td>0.06 (-9.82%)</td><td>8208.80 (+6.95%)</td><td>5986.30 (+9.64%)</td><td>5853.10 <b>(+30.61%)</b></td><td>3999.90 (-2.67%)</td><td>1501.95 (-7.03%)</td><td>16.78 (+2.74%)</td><td>11.81 (-9.85%)</td><td>11.47 <b>(-23.43%)</b></td><td>8.18 (-6.50%)</td><td>3.12 (-9.82%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>7675.20 (n/a)</td><td>5459.92 (n/a)</td><td>4481.40 (n/a)</td><td>4109.50 (n/a)</td><td>1615.56 (n/a)</td><td>16.33 (n/a)</td><td>13.11 (n/a)</td><td>14.97 (n/a)</td><td>8.74 (n/a)</td><td>3.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.14 (+3.39%)</td><td>0.10 <b>(+27.01%)</b></td><td>0.10 <b>(+57.65%)</b></td><td>0.06 (-0.36%)</td><td>0.03 (+11.61%)</td><td>0.13 (+3.39%)</td><td>0.10 <b>(+27.01%)</b></td><td>0.10 <b>(+57.65%)</b></td><td>0.06 (-0.36%)</td><td>0.03 (+11.61%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>3.87 (-1.79%)</td><td>3.60 (-3.89%)</td><td>3.50 (-7.22%)</td><td>3.34 (-4.91%)</td><td>0.22 <b>(+37.43%)</b></td><td>3.87 (-1.79%)</td><td>3.60 (-3.89%)</td><td>3.50 (-7.22%)</td><td>3.33 (-4.91%)</td><td>0.22 <b>(+37.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>3.94 (n/a)</td><td>3.75 (n/a)</td><td>3.77 (n/a)</td><td>3.51 (n/a)</td><td>0.16 (n/a)</td><td>3.94 (n/a)</td><td>3.74 (n/a)</td><td>3.77 (n/a)</td><td>3.51 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>7.56 (+4.46%)</td><td>6.30 (+8.69%)</td><td>6.66 (+19.75%)</td><td>5.09 (-0.34%)</td><td>1.00 <b>(+20.38%)</b></td><td>7.55 (+4.46%)</td><td>6.29 (+8.69%)</td><td>6.66 (+19.75%)</td><td>5.09 (-0.34%)</td><td>1.00 <b>(+20.38%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>7.23 (n/a)</td><td>5.79 (n/a)</td><td>5.56 (n/a)</td><td>5.11 (n/a)</td><td>0.83 (n/a)</td><td>7.23 (n/a)</td><td>5.79 (n/a)</td><td>5.56 (n/a)</td><td>5.11 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>11.22 <b>(-21.35%)</b></td><td>9.04 <b>(-27.84%)</b></td><td>8.48 <b>(-38.29%)</b></td><td>7.72 (-17.06%)</td><td>1.50 <b>(-29.47%)</b></td><td>11.21 <b>(-21.35%)</b></td><td>9.03 <b>(-27.84%)</b></td><td>8.48 <b>(-38.29%)</b></td><td>7.72 (-17.06%)</td><td>1.49 <b>(-29.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>14.26 (n/a)</td><td>12.52 (n/a)</td><td>13.74 (n/a)</td><td>9.31 (n/a)</td><td>2.12 (n/a)</td><td>14.25 (n/a)</td><td>12.52 (n/a)</td><td>13.74 (n/a)</td><td>9.30 (n/a)</td><td>2.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>3.84 (-2.87%)</td><td>3.65 (-3.75%)</td><td>3.60 (-5.71%)</td><td>3.49 (-2.15%)</td><td>0.16 (+7.79%)</td><td>3.84 (-2.87%)</td><td>3.65 (-3.75%)</td><td>3.60 (-5.71%)</td><td>3.49 (-2.15%)</td><td>0.16 (+7.79%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>3.95 (n/a)</td><td>3.79 (n/a)</td><td>3.82 (n/a)</td><td>3.56 (n/a)</td><td>0.14 (n/a)</td><td>3.95 (n/a)</td><td>3.79 (n/a)</td><td>3.82 (n/a)</td><td>3.56 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>7.52 (+1.76%)</td><td>6.37 (-6.91%)</td><td>7.08 (-0.13%)</td><td>4.84 (-12.16%)</td><td>1.34 <b>(+77.25%)</b></td><td>7.52 (+1.76%)</td><td>6.36 (-6.91%)</td><td>7.08 (-0.13%)</td><td>4.84 (-12.16%)</td><td>1.34 <b>(+77.25%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>7.39 (n/a)</td><td>6.84 (n/a)</td><td>7.09 (n/a)</td><td>5.51 (n/a)</td><td>0.76 (n/a)</td><td>7.39 (n/a)</td><td>6.84 (n/a)</td><td>7.08 (n/a)</td><td>5.51 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>13.51 (-2.77%)</td><td>9.67 <b>(-22.27%)</b></td><td>9.57 (-19.68%)</td><td>7.19 <b>(-34.72%)</b></td><td>2.43 <b>(+85.91%)</b></td><td>13.50 (-2.77%)</td><td>9.67 <b>(-22.27%)</b></td><td>9.57 (-19.68%)</td><td>7.19 <b>(-34.72%)</b></td><td>2.42 <b>(+85.91%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>13.90 (n/a)</td><td>12.44 (n/a)</td><td>11.92 (n/a)</td><td>11.02 (n/a)</td><td>1.30 (n/a)</td><td>13.89 (n/a)</td><td>12.44 (n/a)</td><td>11.91 (n/a)</td><td>11.01 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.60 (n/a)</td><td>468.68 (n/a)</td><td>497.10 (n/a)</td><td>286.00 (n/a)</td><td>123.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2102.40 (n/a)</td><td>1058.92 (n/a)</td><td>580.50 (n/a)</td><td>269.80 (n/a)</td><td>859.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.80 (n/a)</td><td>417.10 (n/a)</td><td>520.70 (n/a)</td><td>228.40 (n/a)</td><td>168.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>440.60 (n/a)</td><td>336.10 (n/a)</td><td>333.70 (n/a)</td><td>265.10 (n/a)</td><td>72.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.30 (n/a)</td><td>468.60 (n/a)</td><td>459.30 (n/a)</td><td>403.60 (n/a)</td><td>53.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>722.90 (n/a)</td><td>513.54 (n/a)</td><td>537.70 (n/a)</td><td>300.50 (n/a)</td><td>162.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (+15.21%)</td><td>0.03 <b>(+62.60%)</b></td><td>0.03 <b>(+68.72%)</b></td><td>0.03 <b>(+357.35%)</b></td><td>0.00 <b>(-81.09%)</b></td><td>299.80 <b>(-78.14%)</b></td><td>277.36 <b>(-55.28%)</b></td><td>270.00 <b>(-40.72%)</b></td><td>257.80 (-13.20%)</td><td>17.05 <b>(-96.19%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1371.20 (n/a)</td><td>620.16 (n/a)</td><td>455.50 (n/a)</td><td>297.00 (n/a)</td><td>448.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 <b>(-25.59%)</b></td><td>0.02 (-10.99%)</td><td>0.02 (-8.07%)</td><td>0.01 <b>(+25.32%)</b></td><td>0.01 <b>(-43.96%)</b></td><td>546.50 <b>(-20.21%)</b></td><td>407.14 (-2.11%)</td><td>462.40 (+8.77%)</td><td>261.20 <b>(+34.43%)</b></td><td>123.36 <b>(-39.58%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>684.90 (n/a)</td><td>415.90 (n/a)</td><td>425.10 (n/a)</td><td>194.30 (n/a)</td><td>204.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 <b>(-22.59%)</b></td><td>0.02 (-13.29%)</td><td>0.02 <b>(-21.99%)</b></td><td>0.01 (-9.21%)</td><td>0.01 (-17.04%)</td><td>560.00 (+10.15%)</td><td>449.58 (+14.85%)</td><td>536.60 <b>(+28.19%)</b></td><td>296.90 <b>(+29.20%)</b></td><td>139.63 (+12.97%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.40 (n/a)</td><td>391.44 (n/a)</td><td>418.60 (n/a)</td><td>229.80 (n/a)</td><td>123.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 (+3.98%)</td><td>0.03 (+11.12%)</td><td>0.03 <b>(+58.92%)</b></td><td>0.01 (-1.82%)</td><td>0.01 (+1.89%)</td><td>600.50 (+1.85%)</td><td>366.76 (-9.35%)</td><td>275.10 <b>(-37.08%)</b></td><td>179.80 (-3.85%)</td><td>176.96 (+3.89%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.60 (n/a)</td><td>404.58 (n/a)</td><td>437.20 (n/a)</td><td>187.00 (n/a)</td><td>170.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 <b>(-45.69%)</b></td><td>0.02 <b>(-34.12%)</b></td><td>0.02 <b>(-40.40%)</b></td><td>0.01 (-9.87%)</td><td>0.00 <b>(-67.44%)</b></td><td>640.10 (+10.94%)</td><td>492.16 <b>(+32.37%)</b></td><td>493.60 <b>(+67.78%)</b></td><td>348.00 <b>(+84.13%)</b></td><td>103.56 <b>(-39.26%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.00 (n/a)</td><td>371.82 (n/a)</td><td>294.20 (n/a)</td><td>189.00 (n/a)</td><td>170.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (+5.35%)</td><td>0.02 (-5.35%)</td><td>0.02 (-13.88%)</td><td>0.02 (-5.08%)</td><td>0.00 <b>(+35.19%)</b></td><td>514.10 (+5.35%)</td><td>407.94 (+7.66%)</td><td>411.30 (+16.09%)</td><td>289.80 (-5.08%)</td><td>91.24 <b>(+32.86%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>488.00 (n/a)</td><td>378.92 (n/a)</td><td>354.30 (n/a)</td><td>305.30 (n/a)</td><td>68.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (-10.08%)</td><td>0.02 <b>(-30.63%)</b></td><td>0.02 <b>(-41.75%)</b></td><td>0.01 (-15.45%)</td><td>0.01 (-13.05%)</td><td>546.60 (+18.26%)</td><td>417.78 <b>(+43.31%)</b></td><td>423.60 <b>(+71.64%)</b></td><td>264.50 (+11.18%)</td><td>102.72 (+6.85%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.20 (n/a)</td><td>291.52 (n/a)</td><td>246.80 (n/a)</td><td>237.90 (n/a)</td><td>96.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.06 <b>(+25.47%)</b></td><td>0.04 (-4.25%)</td><td>0.04 (-11.31%)</td><td>0.03 <b>(-32.22%)</b></td><td>0.01 <b>(+380.15%)</b></td><td>422.00 <b>(+47.55%)</b></td><td>290.98 (+10.73%)</td><td>288.20 (+12.75%)</td><td>200.30 <b>(-20.29%)</b></td><td>83.29 <b>(+472.92%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>286.00 (n/a)</td><td>262.78 (n/a)</td><td>255.60 (n/a)</td><td>251.30 (n/a)</td><td>14.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 (-13.64%)</td><td>0.02 (-3.74%)</td><td>0.02 <b>(+29.48%)</b></td><td>0.02 (+14.48%)</td><td>0.01 <b>(-45.29%)</b></td><td>540.90 (-12.65%)</td><td>406.82 (-8.39%)</td><td>404.20 <b>(-22.76%)</b></td><td>272.70 (+15.80%)</td><td>110.19 <b>(-42.49%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.20 (n/a)</td><td>444.10 (n/a)</td><td>523.30 (n/a)</td><td>235.50 (n/a)</td><td>191.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 <b>(+23.82%)</b></td><td>0.03 (-14.01%)</td><td>0.04 (-0.81%)</td><td>0.02 <b>(-53.11%)</b></td><td>0.02 <b>(+286.53%)</b></td><td>640.90 <b>(+113.28%)</b></td><td>391.04 <b>(+44.79%)</b></td><td>286.90 (+0.81%)</td><td>192.20 (-19.24%)</td><td>209.78 <b>(+632.24%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>300.50 (n/a)</td><td>270.08 (n/a)</td><td>284.60 (n/a)</td><td>238.00 (n/a)</td><td>28.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 <b>(+22.38%)</b></td><td>0.03 (-5.24%)</td><td>0.03 (-17.22%)</td><td>0.02 <b>(+34.95%)</b></td><td>0.01 (+11.63%)</td><td>493.80 <b>(-25.90%)</b></td><td>333.74 (+1.23%)</td><td>296.60 <b>(+20.81%)</b></td><td>191.80 (-18.31%)</td><td>126.47 <b>(-32.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.40 (n/a)</td><td>329.68 (n/a)</td><td>245.50 (n/a)</td><td>234.80 (n/a)</td><td>188.39 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.06 <b>(+26.09%)</b></td><td>0.03 (-14.42%)</td><td>0.02 <b>(-41.91%)</b></td><td>0.02 (+7.72%)</td><td>0.02 <b>(+48.88%)</b></td><td>523.90 (-7.16%)</td><td>394.12 <b>(+23.76%)</b></td><td>460.30 <b>(+72.14%)</b></td><td>184.60 <b>(-20.67%)</b></td><td>151.00 (+8.57%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.30 (n/a)</td><td>318.46 (n/a)</td><td>267.40 (n/a)</td><td>232.70 (n/a)</td><td>139.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.03 <b>(-27.57%)</b></td><td>0.02 <b>(-28.13%)</b></td><td>0.02 <b>(-45.34%)</b></td><td>0.02 (-17.88%)</td><td>0.01 <b>(-28.77%)</b></td><td>531.80 <b>(+21.78%)</b></td><td>408.32 <b>(+36.55%)</b></td><td>449.70 <b>(+82.95%)</b></td><td>239.80 <b>(+38.05%)</b></td><td>134.49 (+16.00%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>436.70 (n/a)</td><td>299.02 (n/a)</td><td>245.80 (n/a)</td><td>173.70 (n/a)</td><td>115.93 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 <b>(+25.07%)</b></td><td>0.02 <b>(-32.82%)</b></td><td>0.02 <b>(-50.15%)</b></td><td>0.00 <b>(-72.40%)</b></td><td>0.01 <b>(+103.85%)</b></td><td>1997.10 <b>(+262.32%)</b></td><td>780.64 <b>(+128.89%)</b></td><td>593.70 <b>(+100.64%)</b></td><td>215.10 <b>(-20.04%)</b></td><td>698.77 <b>(+492.07%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.20 (n/a)</td><td>341.06 (n/a)</td><td>295.90 (n/a)</td><td>269.00 (n/a)</td><td>118.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.05 <b>(+43.74%)</b></td><td>0.02 <b>(-27.65%)</b></td><td>0.02 <b>(-48.18%)</b></td><td>0.02 <b>(-46.44%)</b></td><td>0.01 <b>(+460.05%)</b></td><td>536.70 <b>(+86.68%)</b></td><td>441.66 <b>(+67.61%)</b></td><td>498.70 <b>(+93.00%)</b></td><td>168.10 <b>(-30.42%)</b></td><td>154.50 <b>(+593.54%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>287.50 (n/a)</td><td>263.50 (n/a)</td><td>258.40 (n/a)</td><td>241.60 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.02 <b>(-51.72%)</b></td><td>0.02 <b>(-41.29%)</b></td><td>0.02 <b>(-44.63%)</b></td><td>0.01 <b>(-25.34%)</b></td><td>0.01 <b>(-63.35%)</b></td><td>1098.00 <b>(+33.94%)</b></td><td>625.46 <b>(+46.70%)</b></td><td>531.20 <b>(+80.62%)</b></td><td>441.00 <b>(+107.14%)</b></td><td>271.90 (+4.86%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>819.80 (n/a)</td><td>426.36 (n/a)</td><td>294.10 (n/a)</td><td>212.90 (n/a)</td><td>259.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.04 <b>(+54.22%)</b></td><td>0.03 <b>(+43.26%)</b></td><td>0.02 <b>(+33.30%)</b></td><td>0.02 <b>(+24.73%)</b></td><td>0.01 <b>(+109.71%)</b></td><td>479.80 (-19.82%)</td><td>356.98 <b>(-25.26%)</b></td><td>380.90 <b>(-24.99%)</b></td><td>200.40 <b>(-35.17%)</b></td><td>125.53 (+18.39%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.40 (n/a)</td><td>477.60 (n/a)</td><td>507.80 (n/a)</td><td>309.10 (n/a)</td><td>106.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.42 (+14.06%)</td><td>0.31 (+5.96%)</td><td>0.33 (-4.05%)</td><td>0.14 <b>(-26.11%)</b></td><td>0.10 (+17.75%)</td><td>678.90 <b>(+35.35%)</b></td><td>361.34 (-0.35%)</td><td>293.70 (+4.22%)</td><td>231.50 (-12.31%)</td><td>180.58 <b>(+49.42%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>501.60 (n/a)</td><td>362.62 (n/a)</td><td>281.80 (n/a)</td><td>264.00 (n/a)</td><td>120.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.39 <b>(+63.26%)</b></td><td>0.28 <b>(+52.11%)</b></td><td>0.32 <b>(+86.09%)</b></td><td>0.16 (+2.58%)</td><td>0.10 <b>(+197.75%)</b></td><td>628.20 (-2.51%)</td><td>399.24 <b>(-27.79%)</b></td><td>311.80 <b>(-46.26%)</b></td><td>255.30 <b>(-38.73%)</b></td><td>159.74 <b>(+85.14%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>644.40 (n/a)</td><td>552.90 (n/a)</td><td>580.20 (n/a)</td><td>416.70 (n/a)</td><td>86.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.43 (+11.74%)</td><td>0.26 (+12.62%)</td><td>0.20 (-3.42%)</td><td>0.15 (-10.08%)</td><td>0.12 <b>(+34.19%)</b></td><td>650.90 (+11.21%)</td><td>440.78 (-5.03%)</td><td>486.40 (+3.53%)</td><td>227.30 (-10.51%)</td><td>177.12 <b>(+37.28%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.39 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>585.30 (n/a)</td><td>464.14 (n/a)</td><td>469.80 (n/a)</td><td>254.00 (n/a)</td><td>129.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.25 <b>(-23.67%)</b></td><td>0.20 (+6.65%)</td><td>0.17 <b>(+43.07%)</b></td><td>0.16 <b>(+48.82%)</b></td><td>0.05 <b>(-54.94%)</b></td><td>473.60 <b>(-32.81%)</b></td><td>389.56 <b>(-21.98%)</b></td><td>436.00 <b>(-30.11%)</b></td><td>290.60 <b>(+31.02%)</b></td><td>86.09 <b>(-62.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.33 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>704.90 (n/a)</td><td>499.30 (n/a)</td><td>623.80 (n/a)</td><td>221.80 (n/a)</td><td>227.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.24 <b>(-22.26%)</b></td><td>0.18 <b>(-28.60%)</b></td><td>0.17 <b>(-38.40%)</b></td><td>0.13 (-8.54%)</td><td>0.04 <b>(-34.57%)</b></td><td>567.90 (+9.34%)</td><td>427.38 <b>(+35.36%)</b></td><td>439.70 <b>(+62.31%)</b></td><td>302.50 <b>(+28.67%)</b></td><td>102.96 (-12.11%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>519.40 (n/a)</td><td>315.74 (n/a)</td><td>270.90 (n/a)</td><td>235.10 (n/a)</td><td>117.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.16 <b>(-35.40%)</b></td><td>0.14 <b>(-31.27%)</b></td><td>0.15 <b>(-28.24%)</b></td><td>0.11 <b>(-24.87%)</b></td><td>0.03 <b>(-45.84%)</b></td><td>686.30 <b>(+33.11%)</b></td><td>536.12 <b>(+42.95%)</b></td><td>487.70 <b>(+39.38%)</b></td><td>448.20 <b>(+54.82%)</b></td><td>104.25 (+11.49%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>515.60 (n/a)</td><td>375.04 (n/a)</td><td>349.90 (n/a)</td><td>289.50 (n/a)</td><td>93.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.46 (-12.43%)</td><td>0.29 <b>(-21.02%)</b></td><td>0.25 (-8.33%)</td><td>0.12 <b>(-53.17%)</b></td><td>0.13 (-5.99%)</td><td>1097.50 <b>(+113.56%)</b></td><td>559.70 <b>(+40.66%)</b></td><td>518.40 (+9.09%)</td><td>285.00 (+14.18%)</td><td>322.52 <b>(+137.14%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.53 (n/a)</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>513.90 (n/a)</td><td>397.90 (n/a)</td><td>475.20 (n/a)</td><td>249.60 (n/a)</td><td>136.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.42 <b>(-22.88%)</b></td><td>0.31 (-11.72%)</td><td>0.28 (+8.40%)</td><td>0.22 (-6.50%)</td><td>0.09 <b>(-41.58%)</b></td><td>589.30 (+6.95%)</td><td>449.20 (+5.82%)</td><td>474.00 (-7.75%)</td><td>311.80 <b>(+29.70%)</b></td><td>117.95 <b>(-22.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.55 (n/a)</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>551.00 (n/a)</td><td>424.50 (n/a)</td><td>513.80 (n/a)</td><td>240.40 (n/a)</td><td>152.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.58 <b>(+26.81%)</b></td><td>0.38 (+5.25%)</td><td>0.42 (-2.52%)</td><td>0.19 <b>(-25.57%)</b></td><td>0.15 <b>(+40.88%)</b></td><td>702.20 <b>(+34.34%)</b></td><td>393.74 (+1.98%)</td><td>313.30 (+2.59%)</td><td>226.30 <b>(-21.15%)</b></td><td>185.96 <b>(+52.65%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>522.70 (n/a)</td><td>386.08 (n/a)</td><td>305.40 (n/a)</td><td>287.00 (n/a)</td><td>121.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.00 <b>(+75.00%)</b></td><td>0.00 <b>(+33.33%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+173.86%)</b></td><td>22543.89 (+17.87%)</td><td>14386.52 (+2.64%)</td><td>18598.03 <b>(+34.45%)</b></td><td>5474.14 <b>(-42.47%)</b></td><td>7932.04 <b>(+91.03%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19125.42 (n/a)</td><td>14016.71 (n/a)</td><td>13832.56 (n/a)</td><td>9515.98 (n/a)</td><td>4152.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.00 (-13.33%)</td><td>0.00 (-8.57%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-16.48%)</td><td>20796.73 (+9.92%)</td><td>15511.98 (+7.85%)</td><td>17042.51 (+4.70%)</td><td>6321.14 (+16.38%)</td><td>5606.75 (+3.60%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18919.43 (n/a)</td><td>14382.95 (n/a)</td><td>16277.09 (n/a)</td><td>5431.62 (n/a)</td><td>5411.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>0.14 (-7.83%)</td><td>0.10 (-0.04%)</td><td>0.09 (-5.70%)</td><td>0.07 (-15.46%)</td><td>0.03 (+15.82%)</td><td>29970.72 (+18.39%)</td><td>21725.33 (+3.06%)</td><td>23497.02 (+6.08%)</td><td>14976.59 (+8.47%)</td><td>6536.98 <b>(+41.02%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>25315.38 (n/a)</td><td>21079.90 (n/a)</td><td>22151.25 (n/a)</td><td>13806.81 (n/a)</td><td>4635.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>1.51 (-7.40%)</td><td>1.07 <b>(-22.65%)</b></td><td>0.94 <b>(-34.98%)</b></td><td>0.69 <b>(-27.55%)</b></td><td>0.36 <b>(+29.25%)</b></td><td>764.70 <b>(+38.03%)</b></td><td>537.68 <b>(+36.05%)</b></td><td>558.40 <b>(+53.79%)</b></td><td>347.20 (+7.99%)</td><td>175.35 <b>(+84.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>1.63 (n/a)</td><td>1.38 (n/a)</td><td>1.44 (n/a)</td><td>0.95 (n/a)</td><td>0.28 (n/a)</td><td>554.00 (n/a)</td><td>395.22 (n/a)</td><td>363.10 (n/a)</td><td>321.50 (n/a)</td><td>95.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>2.30 <b>(-21.30%)</b></td><td>1.45 <b>(-28.42%)</b></td><td>1.58 <b>(-24.27%)</b></td><td>0.30 <b>(-73.24%)</b></td><td>0.74 (+3.88%)</td><td>3533.00 <b>(+273.74%)</b></td><td>1210.16 <b>(+108.11%)</b></td><td>662.70 <b>(+32.04%)</b></td><td>455.90 <b>(+27.06%)</b></td><td>1304.36 <b>(+458.49%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>2.92 (n/a)</td><td>2.02 (n/a)</td><td>2.09 (n/a)</td><td>1.11 (n/a)</td><td>0.71 (n/a)</td><td>945.30 (n/a)</td><td>581.50 (n/a)</td><td>501.90 (n/a)</td><td>358.80 (n/a)</td><td>233.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:21</td><td>1.75 (-0.68%)</td><td>1.25 (-8.93%)</td><td>1.33 (-6.09%)</td><td>0.72 (-16.74%)</td><td>0.42 (+17.49%)</td><td>729.60 <b>(+20.10%)</b></td><td>464.70 (+14.33%)</td><td>394.10 (+6.48%)</td><td>299.20 (+0.67%)</td><td>176.70 <b>(+42.14%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>1.76 (n/a)</td><td>1.38 (n/a)</td><td>1.42 (n/a)</td><td>0.86 (n/a)</td><td>0.36 (n/a)</td><td>607.50 (n/a)</td><td>406.46 (n/a)</td><td>370.10 (n/a)</td><td>297.20 (n/a)</td><td>124.31 (n/a)</td>
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
