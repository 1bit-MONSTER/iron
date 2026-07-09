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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (-17.03%)</td><td>0.04 (-2.88%)</td><td>0.03 <b>(-23.78%)</b></td><td>0.02 <b>(+256.60%)</b></td><td>0.01 <b>(-36.79%)</b></td><td>560.10 <b>(-71.96%)</b></td><td>393.78 <b>(-39.56%)</b></td><td>387.80 <b>(+31.19%)</b></td><td>224.80 <b>(+20.54%)</b></td><td>147.85 <b>(-80.57%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1997.30 (n/a)</td><td>651.54 (n/a)</td><td>295.60 (n/a)</td><td>186.50 (n/a)</td><td>760.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 <b>(+33.96%)</b></td><td>0.04 <b>(+79.77%)</b></td><td>0.04 <b>(+109.48%)</b></td><td>0.02 <b>(+275.91%)</b></td><td>0.01 (-1.58%)</td><td>529.40 <b>(-73.40%)</b></td><td>356.76 <b>(-56.91%)</b></td><td>300.80 <b>(-52.26%)</b></td><td>269.20 <b>(-25.37%)</b></td><td>111.96 <b>(-83.02%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1990.10 (n/a)</td><td>827.88 (n/a)</td><td>630.10 (n/a)</td><td>360.70 (n/a)</td><td>659.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (+0.34%)</td><td>0.04 (+19.34%)</td><td>0.05 <b>(+50.25%)</b></td><td>0.02 (+3.47%)</td><td>0.01 (-3.79%)</td><td>560.10 (-3.35%)</td><td>341.06 (-17.20%)</td><td>266.50 <b>(-33.44%)</b></td><td>236.40 (-0.34%)</td><td>133.57 (-8.32%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>579.50 (n/a)</td><td>411.90 (n/a)</td><td>400.40 (n/a)</td><td>237.20 (n/a)</td><td>145.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (-11.49%)</td><td>0.02 (-2.63%)</td><td>0.02 (+7.14%)</td><td>0.01 <b>(+23.31%)</b></td><td>0.00 <b>(-23.88%)</b></td><td>487.20 (-18.91%)</td><td>353.32 (-2.93%)</td><td>274.40 (-6.67%)</td><td>266.90 (+13.00%)</td><td>113.60 <b>(-28.12%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.80 (n/a)</td><td>364.00 (n/a)</td><td>294.00 (n/a)</td><td>236.20 (n/a)</td><td>158.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (+3.37%)</td><td>0.02 (+5.43%)</td><td>0.02 (+1.01%)</td><td>0.01 (+6.14%)</td><td>0.01 (+4.93%)</td><td>538.30 (-5.78%)</td><td>346.72 (-5.35%)</td><td>266.40 (-1.00%)</td><td>234.50 (-3.26%)</td><td>140.91 (-6.34%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.30 (n/a)</td><td>366.32 (n/a)</td><td>269.10 (n/a)</td><td>242.40 (n/a)</td><td>150.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (-12.28%)</td><td>0.02 (-1.29%)</td><td>0.02 (-6.04%)</td><td>0.01 <b>(+25.27%)</b></td><td>0.00 <b>(-37.73%)</b></td><td>455.70 <b>(-20.18%)</b></td><td>309.94 (-5.51%)</td><td>280.60 (+6.41%)</td><td>263.80 (+14.00%)</td><td>82.03 <b>(-42.34%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.90 (n/a)</td><td>328.02 (n/a)</td><td>263.70 (n/a)</td><td>231.40 (n/a)</td><td>142.26 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (+10.22%)</td><td>0.02 (-10.14%)</td><td>0.01 <b>(-23.46%)</b></td><td>0.01 <b>(-32.23%)</b></td><td>0.01 <b>(+137.51%)</b></td><td>559.20 <b>(+47.55%)</b></td><td>392.68 <b>(+25.83%)</b></td><td>387.00 <b>(+30.65%)</b></td><td>230.60 (-9.25%)</td><td>158.74 <b>(+212.80%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>379.00 (n/a)</td><td>312.08 (n/a)</td><td>296.20 (n/a)</td><td>254.10 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 <b>(-31.88%)</b></td><td>0.01 (-19.44%)</td><td>0.01 <b>(-26.74%)</b></td><td>0.01 <b>(+245.87%)</b></td><td>0.00 <b>(-53.94%)</b></td><td>527.50 <b>(-71.09%)</b></td><td>405.66 <b>(-29.53%)</b></td><td>420.00 <b>(+36.50%)</b></td><td>266.20 <b>(+46.83%)</b></td><td>118.07 <b>(-83.14%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1824.50 (n/a)</td><td>575.62 (n/a)</td><td>307.70 (n/a)</td><td>181.30 (n/a)</td><td>700.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (+10.29%)</td><td>0.01 (+12.53%)</td><td>0.02 <b>(+28.06%)</b></td><td>0.01 <b>(-20.57%)</b></td><td>0.00 <b>(+67.25%)</b></td><td>618.40 <b>(+25.90%)</b></td><td>381.84 (-6.32%)</td><td>314.50 <b>(-21.90%)</b></td><td>287.20 (-9.31%)</td><td>136.52 <b>(+96.90%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.20 (n/a)</td><td>407.58 (n/a)</td><td>402.70 (n/a)</td><td>316.70 (n/a)</td><td>69.34 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.70 (n/a)</td><td>321.32 (n/a)</td><td>283.00 (n/a)</td><td>227.60 (n/a)</td><td>100.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.00 (n/a)</td><td>382.64 (n/a)</td><td>432.00 (n/a)</td><td>270.80 (n/a)</td><td>99.98 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.50 (n/a)</td><td>401.02 (n/a)</td><td>380.50 (n/a)</td><td>327.00 (n/a)</td><td>83.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>397.00 (n/a)</td><td>305.78 (n/a)</td><td>297.20 (n/a)</td><td>249.60 (n/a)</td><td>54.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>583.60 (n/a)</td><td>327.80 (n/a)</td><td>290.10 (n/a)</td><td>197.40 (n/a)</td><td>151.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.80 (n/a)</td><td>366.06 (n/a)</td><td>328.40 (n/a)</td><td>236.60 (n/a)</td><td>134.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.20 (n/a)</td><td>513.72 (n/a)</td><td>502.60 (n/a)</td><td>404.30 (n/a)</td><td>84.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>430.20 (n/a)</td><td>285.48 (n/a)</td><td>268.70 (n/a)</td><td>176.60 (n/a)</td><td>92.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.60 (n/a)</td><td>300.00 (n/a)</td><td>238.40 (n/a)</td><td>201.30 (n/a)</td><td>150.96 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>446.00 (n/a)</td><td>288.02 (n/a)</td><td>276.90 (n/a)</td><td>187.40 (n/a)</td><td>96.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.50 (n/a)</td><td>434.74 (n/a)</td><td>415.10 (n/a)</td><td>254.80 (n/a)</td><td>132.96 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>674.60 (n/a)</td><td>508.90 (n/a)</td><td>530.10 (n/a)</td><td>335.80 (n/a)</td><td>128.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.61 <b>(-30.86%)</b></td><td>0.31 <b>(-29.50%)</b></td><td>0.22 <b>(-44.73%)</b></td><td>0.12 (-3.99%)</td><td>0.20 <b>(-28.10%)</b></td><td>1791.90 (+4.16%)</td><td>955.22 <b>(+32.16%)</b></td><td>1017.10 <b>(+80.91%)</b></td><td>361.70 <b>(+44.62%)</b></td><td>556.93 (-2.76%)</td><td>26.09 <b>(-30.86%)</b></td><td>13.39 <b>(-29.50%)</b></td><td>9.28 <b>(-44.73%)</b></td><td>5.27 (-3.99%)</td><td>8.39 <b>(-28.10%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.88 (n/a)</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.13 (n/a)</td><td>0.27 (n/a)</td><td>1720.40 (n/a)</td><td>722.80 (n/a)</td><td>562.20 (n/a)</td><td>250.10 (n/a)</td><td>572.72 (n/a)</td><td>37.73 (n/a)</td><td>19.00 (n/a)</td><td>16.79 (n/a)</td><td>5.49 (n/a)</td><td>11.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.58 (+11.27%)</td><td>0.41 (+8.14%)</td><td>0.41 (+4.25%)</td><td>0.13 (+1.05%)</td><td>0.18 (+13.34%)</td><td>1749.70 (-1.04%)</td><td>733.74 (-4.53%)</td><td>540.00 (-4.07%)</td><td>379.50 (-10.13%)</td><td>573.96 (+1.61%)</td><td>24.87 (+11.27%)</td><td>17.30 (+8.14%)</td><td>17.48 (+4.25%)</td><td>5.39 (+1.05%)</td><td>7.54 (+13.34%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>1768.00 (n/a)</td><td>768.56 (n/a)</td><td>562.90 (n/a)</td><td>422.30 (n/a)</td><td>564.89 (n/a)</td><td>22.35 (n/a)</td><td>16.00 (n/a)</td><td>16.76 (n/a)</td><td>5.34 (n/a)</td><td>6.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.31 (-0.89%)</td><td>0.31 (-0.74%)</td><td>0.30 (-0.82%)</td><td>0.30 (-0.64%)</td><td>0.00 (-3.45%)</td><td>83445.30 (+0.64%)</td><td>82408.10 (+0.74%)</td><td>82625.90 (+0.83%)</td><td>81500.30 (+0.90%)</td><td>776.60 (-2.03%)</td><td>210.80 (-0.89%)</td><td>208.49 (-0.74%)</td><td>207.92 (-0.82%)</td><td>205.88 (-0.64%)</td><td>1.96 (-3.45%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>82914.70 (n/a)</td><td>81799.30 (n/a)</td><td>81948.20 (n/a)</td><td>80771.70 (n/a)</td><td>792.71 (n/a)</td><td>212.70 (n/a)</td><td>210.04 (n/a)</td><td>209.64 (n/a)</td><td>207.20 (n/a)</td><td>2.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>1.03 (-3.05%)</td><td>1.01 (-1.95%)</td><td>1.01 (-1.29%)</td><td>1.00 (-1.53%)</td><td>0.01 <b>(-39.04%)</b></td><td>25047.00 (+1.56%)</td><td>24836.22 (+1.97%)</td><td>24865.80 (+1.31%)</td><td>24392.80 (+3.15%)</td><td>261.62 <b>(-36.07%)</b></td><td>704.30 (-3.05%)</td><td>691.79 (-1.95%)</td><td>690.90 (-1.29%)</td><td>685.91 (-1.53%)</td><td>7.37 <b>(-39.04%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>1.06 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.02 (n/a)</td><td>24663.00 (n/a)</td><td>24355.56 (n/a)</td><td>24544.70 (n/a)</td><td>23649.00 (n/a)</td><td>409.21 (n/a)</td><td>726.45 (n/a)</td><td>705.54 (n/a)</td><td>699.94 (n/a)</td><td>696.58 (n/a)</td><td>12.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>3.67 (-6.18%)</td><td>2.80 (-13.66%)</td><td>2.70 <b>(-27.37%)</b></td><td>1.36 (-17.44%)</td><td>0.95 (+1.61%)</td><td>5922.80 <b>(+21.13%)</b></td><td>3280.76 (+18.80%)</td><td>2987.20 <b>(+37.68%)</b></td><td>2194.00 (+6.59%)</td><td>1536.17 <b>(+27.51%)</b></td><td>963.49 (-6.18%)</td><td>733.96 (-13.66%)</td><td>707.66 <b>(-27.37%)</b></td><td>356.91 (-17.44%)</td><td>249.31 (+1.61%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>3.92 (n/a)</td><td>3.24 (n/a)</td><td>3.72 (n/a)</td><td>1.65 (n/a)</td><td>0.94 (n/a)</td><td>4889.60 (n/a)</td><td>2761.52 (n/a)</td><td>2169.70 (n/a)</td><td>2058.40 (n/a)</td><td>1204.71 (n/a)</td><td>1026.97 (n/a)</td><td>850.12 (n/a)</td><td>974.31 (n/a)</td><td>432.33 (n/a)</td><td>245.36 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.30 (+14.54%)</td><td>0.24 (+10.07%)</td><td>0.28 <b>(+30.71%)</b></td><td>0.16 (-19.31%)</td><td>0.06 <b>(+150.32%)</b></td><td>7675.20 <b>(+23.93%)</b></td><td>5459.92 (-4.06%)</td><td>4481.40 <b>(-23.49%)</b></td><td>4109.50 (-12.69%)</td><td>1615.56 <b>(+172.59%)</b></td><td>16.33 (+14.54%)</td><td>13.11 (+10.07%)</td><td>14.97 <b>(+30.71%)</b></td><td>8.74 (-19.31%)</td><td>3.46 <b>(+150.32%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>6193.30 (n/a)</td><td>5691.22 (n/a)</td><td>5857.50 (n/a)</td><td>4707.00 (n/a)</td><td>592.68 (n/a)</td><td>14.26 (n/a)</td><td>11.91 (n/a)</td><td>11.46 (n/a)</td><td>10.84 (n/a)</td><td>1.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.13 <b>(+32.05%)</b></td><td>0.08 (-0.59%)</td><td>0.06 (-11.36%)</td><td>0.06 (-6.57%)</td><td>0.03 <b>(+121.70%)</b></td><td>0.13 <b>(+32.05%)</b></td><td>0.08 (-0.59%)</td><td>0.06 (-11.36%)</td><td>0.06 (-6.57%)</td><td>0.03 <b>(+121.70%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>3.94 (-0.12%)</td><td>3.75 (-0.52%)</td><td>3.77 (+1.16%)</td><td>3.51 (-3.94%)</td><td>0.16 <b>(+30.27%)</b></td><td>3.94 (-0.12%)</td><td>3.74 (-0.52%)</td><td>3.77 (+1.16%)</td><td>3.51 (-3.94%)</td><td>0.16 <b>(+30.27%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>3.95 (n/a)</td><td>3.77 (n/a)</td><td>3.73 (n/a)</td><td>3.65 (n/a)</td><td>0.13 (n/a)</td><td>3.95 (n/a)</td><td>3.76 (n/a)</td><td>3.73 (n/a)</td><td>3.65 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>7.23 (+6.56%)</td><td>5.79 (+2.06%)</td><td>5.56 (-5.56%)</td><td>5.11 (+10.68%)</td><td>0.83 (-7.98%)</td><td>7.23 (+6.56%)</td><td>5.79 (+2.06%)</td><td>5.56 (-5.56%)</td><td>5.11 (+10.68%)</td><td>0.83 (-7.98%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>6.79 (n/a)</td><td>5.68 (n/a)</td><td>5.89 (n/a)</td><td>4.62 (n/a)</td><td>0.90 (n/a)</td><td>6.78 (n/a)</td><td>5.67 (n/a)</td><td>5.89 (n/a)</td><td>4.61 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>14.26 (+2.65%)</td><td>12.52 (+18.77%)</td><td>13.74 <b>(+54.09%)</b></td><td>9.31 (+15.67%)</td><td>2.12 <b>(-27.13%)</b></td><td>14.25 (+2.65%)</td><td>12.52 (+18.77%)</td><td>13.74 <b>(+54.09%)</b></td><td>9.30 (+15.67%)</td><td>2.12 <b>(-27.13%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>13.90 (n/a)</td><td>10.54 (n/a)</td><td>8.92 (n/a)</td><td>8.05 (n/a)</td><td>2.91 (n/a)</td><td>13.89 (n/a)</td><td>10.54 (n/a)</td><td>8.91 (n/a)</td><td>8.04 (n/a)</td><td>2.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>3.95 (+1.62%)</td><td>3.79 (+4.88%)</td><td>3.82 (+5.75%)</td><td>3.56 (+8.43%)</td><td>0.14 <b>(-37.74%)</b></td><td>3.95 (+1.62%)</td><td>3.79 (+4.88%)</td><td>3.82 (+5.75%)</td><td>3.56 (+8.43%)</td><td>0.14 <b>(-37.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>3.89 (n/a)</td><td>3.62 (n/a)</td><td>3.61 (n/a)</td><td>3.29 (n/a)</td><td>0.23 (n/a)</td><td>3.89 (n/a)</td><td>3.62 (n/a)</td><td>3.61 (n/a)</td><td>3.28 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>7.39 (+0.25%)</td><td>6.84 (+8.02%)</td><td>7.09 (+15.65%)</td><td>5.51 (-1.48%)</td><td>0.76 (+4.45%)</td><td>7.39 (+0.25%)</td><td>6.84 (+8.02%)</td><td>7.08 (+15.65%)</td><td>5.51 (-1.48%)</td><td>0.76 (+4.45%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>7.38 (n/a)</td><td>6.33 (n/a)</td><td>6.13 (n/a)</td><td>5.59 (n/a)</td><td>0.72 (n/a)</td><td>7.37 (n/a)</td><td>6.33 (n/a)</td><td>6.13 (n/a)</td><td>5.59 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>13.90 (+2.23%)</td><td>12.44 <b>(+23.61%)</b></td><td>11.92 <b>(+21.51%)</b></td><td>11.02 <b>(+29.45%)</b></td><td>1.30 <b>(-37.18%)</b></td><td>13.89 (+2.23%)</td><td>12.44 <b>(+23.61%)</b></td><td>11.91 <b>(+21.51%)</b></td><td>11.01 <b>(+29.45%)</b></td><td>1.30 <b>(-37.18%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>13.59 (n/a)</td><td>10.07 (n/a)</td><td>9.81 (n/a)</td><td>8.51 (n/a)</td><td>2.08 (n/a)</td><td>13.59 (n/a)</td><td>10.06 (n/a)</td><td>9.80 (n/a)</td><td>8.51 (n/a)</td><td>2.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>446.40 (n/a)</td><td>363.68 (n/a)</td><td>372.70 (n/a)</td><td>279.60 (n/a)</td><td>75.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.20 (n/a)</td><td>370.32 (n/a)</td><td>317.50 (n/a)</td><td>273.50 (n/a)</td><td>110.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2537.40 (n/a)</td><td>849.88 (n/a)</td><td>448.10 (n/a)</td><td>378.30 (n/a)</td><td>943.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2111.90 (n/a)</td><td>745.36 (n/a)</td><td>481.60 (n/a)</td><td>281.40 (n/a)</td><td>768.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.00 (n/a)</td><td>423.02 (n/a)</td><td>457.70 (n/a)</td><td>259.80 (n/a)</td><td>132.94 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>423.66 (n/a)</td><td>434.50 (n/a)</td><td>294.30 (n/a)</td><td>103.89 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (-13.37%)</td><td>0.02 <b>(-29.04%)</b></td><td>0.02 <b>(-37.11%)</b></td><td>0.01 <b>(-64.72%)</b></td><td>0.01 <b>(+33.71%)</b></td><td>1371.20 <b>(+183.42%)</b></td><td>620.16 <b>(+81.16%)</b></td><td>455.50 <b>(+58.99%)</b></td><td>297.00 (+15.43%)</td><td>448.04 <b>(+324.26%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.80 (n/a)</td><td>342.32 (n/a)</td><td>286.50 (n/a)</td><td>257.30 (n/a)</td><td>105.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 <b>(+52.22%)</b></td><td>0.02 <b>(+29.34%)</b></td><td>0.02 (+11.00%)</td><td>0.01 (-6.41%)</td><td>0.01 <b>(+118.91%)</b></td><td>684.90 (+6.85%)</td><td>415.90 (-10.44%)</td><td>425.10 (-9.92%)</td><td>194.30 <b>(-34.31%)</b></td><td>204.16 <b>(+50.27%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.00 (n/a)</td><td>464.38 (n/a)</td><td>471.90 (n/a)</td><td>295.80 (n/a)</td><td>135.86 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 <b>(-23.90%)</b></td><td>0.02 (-5.04%)</td><td>0.02 (-0.39%)</td><td>0.02 (+14.57%)</td><td>0.01 <b>(-35.30%)</b></td><td>508.40 (-12.72%)</td><td>391.44 (-1.63%)</td><td>418.60 (+0.38%)</td><td>229.80 <b>(+31.39%)</b></td><td>123.59 (-16.59%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.50 (n/a)</td><td>397.94 (n/a)</td><td>417.00 (n/a)</td><td>174.90 (n/a)</td><td>148.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 <b>(+135.06%)</b></td><td>0.02 <b>(+41.46%)</b></td><td>0.02 (+5.88%)</td><td>0.01 (-2.16%)</td><td>0.01 <b>(+623.59%)</b></td><td>589.60 (+2.22%)</td><td>404.58 (-15.91%)</td><td>437.20 (-5.55%)</td><td>187.00 <b>(-57.46%)</b></td><td>170.33 <b>(+210.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.80 (n/a)</td><td>481.14 (n/a)</td><td>462.90 (n/a)</td><td>439.60 (n/a)</td><td>54.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 <b>(+22.53%)</b></td><td>0.03 (-2.33%)</td><td>0.03 (-8.84%)</td><td>0.01 (-16.26%)</td><td>0.01 <b>(+31.80%)</b></td><td>577.00 (+19.44%)</td><td>371.82 (+9.56%)</td><td>294.20 (+9.69%)</td><td>189.00 (-18.39%)</td><td>170.50 <b>(+33.36%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.10 (n/a)</td><td>339.38 (n/a)</td><td>268.20 (n/a)</td><td>231.60 (n/a)</td><td>127.85 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (-8.63%)</td><td>0.02 (+0.23%)</td><td>0.02 (+14.57%)</td><td>0.02 (+13.15%)</td><td>0.00 <b>(-44.96%)</b></td><td>488.00 (-11.63%)</td><td>378.92 (-5.15%)</td><td>354.30 (-12.71%)</td><td>305.30 (+9.43%)</td><td>68.68 <b>(-42.75%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.20 (n/a)</td><td>399.50 (n/a)</td><td>405.90 (n/a)</td><td>279.00 (n/a)</td><td>119.96 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (+4.35%)</td><td>0.03 (+4.38%)</td><td>0.03 (+5.80%)</td><td>0.02 (-19.02%)</td><td>0.01 <b>(+48.50%)</b></td><td>462.20 <b>(+23.48%)</b></td><td>291.52 (-0.36%)</td><td>246.80 (-5.48%)</td><td>237.90 (-4.15%)</td><td>96.14 <b>(+80.43%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>374.30 (n/a)</td><td>292.58 (n/a)</td><td>261.10 (n/a)</td><td>248.20 (n/a)</td><td>53.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 (-9.53%)</td><td>0.05 (+16.14%)</td><td>0.05 (+17.03%)</td><td>0.04 <b>(+69.60%)</b></td><td>0.00 <b>(-76.55%)</b></td><td>286.00 <b>(-41.04%)</b></td><td>262.78 (-19.03%)</td><td>255.60 (-14.54%)</td><td>251.30 (+10.56%)</td><td>14.54 <b>(-85.22%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>485.10 (n/a)</td><td>324.54 (n/a)</td><td>299.10 (n/a)</td><td>227.30 (n/a)</td><td>98.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (+11.41%)</td><td>0.02 (+13.00%)</td><td>0.02 (+1.80%)</td><td>0.01 (-9.68%)</td><td>0.01 <b>(+56.52%)</b></td><td>619.20 (+10.71%)</td><td>444.10 (-1.91%)</td><td>523.30 (-1.76%)</td><td>235.50 (-10.25%)</td><td>191.59 <b>(+47.06%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.30 (n/a)</td><td>452.76 (n/a)</td><td>532.70 (n/a)</td><td>262.40 (n/a)</td><td>130.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (+7.16%)</td><td>0.04 <b>(+38.48%)</b></td><td>0.04 <b>(+54.19%)</b></td><td>0.03 <b>(+89.11%)</b></td><td>0.00 <b>(-61.92%)</b></td><td>300.50 <b>(-47.13%)</b></td><td>270.08 <b>(-35.55%)</b></td><td>284.60 <b>(-35.16%)</b></td><td>238.00 (-6.67%)</td><td>28.65 <b>(-81.47%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.40 (n/a)</td><td>419.06 (n/a)</td><td>438.90 (n/a)</td><td>255.00 (n/a)</td><td>154.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (+10.53%)</td><td>0.03 <b>(+37.71%)</b></td><td>0.03 <b>(+85.23%)</b></td><td>0.01 (-4.78%)</td><td>0.01 (+3.71%)</td><td>666.40 (+5.03%)</td><td>329.68 <b>(-26.53%)</b></td><td>245.50 <b>(-46.02%)</b></td><td>234.80 (-9.52%)</td><td>188.39 (+3.17%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.50 (n/a)</td><td>448.72 (n/a)</td><td>454.80 (n/a)</td><td>259.50 (n/a)</td><td>182.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 <b>(+61.82%)</b></td><td>0.04 <b>(+62.82%)</b></td><td>0.04 <b>(+83.03%)</b></td><td>0.02 (+4.73%)</td><td>0.01 <b>(+149.25%)</b></td><td>564.30 (-4.52%)</td><td>318.46 <b>(-33.68%)</b></td><td>267.40 <b>(-45.36%)</b></td><td>232.70 <b>(-38.21%)</b></td><td>139.08 <b>(+55.64%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>591.00 (n/a)</td><td>480.20 (n/a)</td><td>489.40 (n/a)</td><td>376.60 (n/a)</td><td>89.36 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.05 <b>(+29.44%)</b></td><td>0.03 <b>(+37.20%)</b></td><td>0.03 <b>(+97.21%)</b></td><td>0.02 <b>(+42.06%)</b></td><td>0.01 (+18.20%)</td><td>436.70 <b>(-29.60%)</b></td><td>299.02 <b>(-28.77%)</b></td><td>245.80 <b>(-49.29%)</b></td><td>173.70 <b>(-22.73%)</b></td><td>115.93 <b>(-29.49%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.30 (n/a)</td><td>419.78 (n/a)</td><td>484.70 (n/a)</td><td>224.80 (n/a)</td><td>164.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 (-12.56%)</td><td>0.03 (+19.89%)</td><td>0.03 <b>(+47.49%)</b></td><td>0.02 (+15.15%)</td><td>0.01 <b>(-29.92%)</b></td><td>551.20 (-13.16%)</td><td>341.06 <b>(-21.11%)</b></td><td>295.90 <b>(-32.20%)</b></td><td>269.00 (+14.32%)</td><td>118.02 <b>(-26.07%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.70 (n/a)</td><td>432.34 (n/a)</td><td>436.40 (n/a)</td><td>235.30 (n/a)</td><td>159.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 <b>(+54.32%)</b></td><td>0.03 <b>(+71.38%)</b></td><td>0.03 <b>(+76.84%)</b></td><td>0.03 <b>(+78.80%)</b></td><td>0.00 (+11.63%)</td><td>287.50 <b>(-44.07%)</b></td><td>263.50 <b>(-42.04%)</b></td><td>258.40 <b>(-43.46%)</b></td><td>241.60 <b>(-35.21%)</b></td><td>22.28 <b>(-58.90%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>514.00 (n/a)</td><td>454.60 (n/a)</td><td>457.00 (n/a)</td><td>372.90 (n/a)</td><td>54.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.04 (+16.81%)</td><td>0.03 (+11.73%)</td><td>0.03 <b>(+53.77%)</b></td><td>0.01 <b>(-33.10%)</b></td><td>0.01 <b>(+41.10%)</b></td><td>819.80 <b>(+49.46%)</b></td><td>426.36 (+3.44%)</td><td>294.10 <b>(-34.96%)</b></td><td>212.90 (-14.39%)</td><td>259.29 <b>(+79.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.50 (n/a)</td><td>412.18 (n/a)</td><td>452.20 (n/a)</td><td>248.70 (n/a)</td><td>144.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.03 <b>(-20.08%)</b></td><td>0.02 <b>(-26.99%)</b></td><td>0.02 <b>(-26.32%)</b></td><td>0.01 (-14.93%)</td><td>0.00 <b>(-38.17%)</b></td><td>598.40 (+17.54%)</td><td>477.60 <b>(+32.17%)</b></td><td>507.80 <b>(+35.74%)</b></td><td>309.10 <b>(+25.09%)</b></td><td>106.03 (-7.62%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.10 (n/a)</td><td>361.36 (n/a)</td><td>374.10 (n/a)</td><td>247.10 (n/a)</td><td>114.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.37 (-9.32%)</td><td>0.29 (-18.20%)</td><td>0.35 (-9.79%)</td><td>0.20 (-10.00%)</td><td>0.09 (+8.75%)</td><td>501.60 (+11.10%)</td><td>362.62 <b>(+25.32%)</b></td><td>281.80 (+10.86%)</td><td>264.00 (+10.28%)</td><td>120.85 <b>(+32.69%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.39 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>451.50 (n/a)</td><td>289.36 (n/a)</td><td>254.20 (n/a)</td><td>239.40 (n/a)</td><td>91.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.24 <b>(-44.34%)</b></td><td>0.18 <b>(-38.08%)</b></td><td>0.17 <b>(-51.08%)</b></td><td>0.15 (+1.72%)</td><td>0.03 <b>(-73.46%)</b></td><td>644.40 (-1.69%)</td><td>552.90 <b>(+38.94%)</b></td><td>580.20 <b>(+104.44%)</b></td><td>416.70 <b>(+79.61%)</b></td><td>86.28 <b>(-55.20%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.35 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>655.50 (n/a)</td><td>397.94 (n/a)</td><td>283.80 (n/a)</td><td>232.00 (n/a)</td><td>192.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.39 (-6.27%)</td><td>0.23 (-4.64%)</td><td>0.21 (-6.30%)</td><td>0.17 (+10.16%)</td><td>0.09 (-11.05%)</td><td>585.30 (-9.23%)</td><td>464.14 (+2.67%)</td><td>469.80 (+6.72%)</td><td>254.00 (+6.68%)</td><td>129.03 (-13.01%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>644.80 (n/a)</td><td>452.06 (n/a)</td><td>440.20 (n/a)</td><td>238.10 (n/a)</td><td>148.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.33 (+13.39%)</td><td>0.19 (-18.95%)</td><td>0.12 <b>(-50.16%)</b></td><td>0.10 (+13.51%)</td><td>0.10 <b>(+28.50%)</b></td><td>704.90 (-11.90%)</td><td>499.30 <b>(+28.94%)</b></td><td>623.80 <b>(+100.64%)</b></td><td>221.80 (-11.81%)</td><td>227.86 (-2.13%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>800.10 (n/a)</td><td>387.22 (n/a)</td><td>310.90 (n/a)</td><td>251.50 (n/a)</td><td>232.82 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.31 (+1.86%)</td><td>0.25 (+13.00%)</td><td>0.27 (+14.72%)</td><td>0.14 (+1.93%)</td><td>0.07 (-10.70%)</td><td>519.40 (-1.89%)</td><td>315.74 (-13.47%)</td><td>270.90 (-12.81%)</td><td>235.10 (-1.84%)</td><td>117.14 (-12.64%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>529.40 (n/a)</td><td>364.88 (n/a)</td><td>310.70 (n/a)</td><td>239.50 (n/a)</td><td>134.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.25 (-15.91%)</td><td>0.21 (-1.13%)</td><td>0.21 (+1.57%)</td><td>0.14 <b>(+21.24%)</b></td><td>0.05 <b>(-46.76%)</b></td><td>515.60 (-17.52%)</td><td>375.04 (-9.66%)</td><td>349.90 (-1.55%)</td><td>289.50 (+18.89%)</td><td>93.51 <b>(-49.20%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>625.10 (n/a)</td><td>415.12 (n/a)</td><td>355.40 (n/a)</td><td>243.50 (n/a)</td><td>184.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.53 (+7.76%)</td><td>0.37 (+2.51%)</td><td>0.28 (-12.80%)</td><td>0.26 (+4.99%)</td><td>0.14 <b>(+24.60%)</b></td><td>513.90 (-4.76%)</td><td>397.90 (+0.69%)</td><td>475.20 (+14.67%)</td><td>249.60 (-7.21%)</td><td>136.00 (+12.58%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.49 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>539.60 (n/a)</td><td>395.16 (n/a)</td><td>414.40 (n/a)</td><td>269.00 (n/a)</td><td>120.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.55 <b>(+112.00%)</b></td><td>0.35 <b>(+51.51%)</b></td><td>0.26 (+14.28%)</td><td>0.24 (+14.38%)</td><td>0.15 <b>(+641.71%)</b></td><td>551.00 (-12.57%)</td><td>424.50 <b>(-25.46%)</b></td><td>513.80 (-12.50%)</td><td>240.40 <b>(-52.84%)</b></td><td>152.42 <b>(+216.30%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>630.20 (n/a)</td><td>569.48 (n/a)</td><td>587.20 (n/a)</td><td>509.70 (n/a)</td><td>48.19 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.46 (+12.03%)</td><td>0.37 <b>(+40.05%)</b></td><td>0.43 <b>(+84.61%)</b></td><td>0.25 <b>(+21.09%)</b></td><td>0.10 <b>(+23.70%)</b></td><td>522.70 (-17.41%)</td><td>386.08 <b>(-27.77%)</b></td><td>305.40 <b>(-45.82%)</b></td><td>287.00 (-10.73%)</td><td>121.82 (-4.88%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>632.90 (n/a)</td><td>534.52 (n/a)</td><td>563.70 (n/a)</td><td>321.50 (n/a)</td><td>128.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.00 <b>(-50.00%)</b></td><td>0.00 <b>(-42.31%)</b></td><td>0.00 <b>(-57.14%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-66.10%)</b></td><td>19125.42 (-5.73%)</td><td>14016.71 <b>(+23.39%)</b></td><td>13832.56 <b>(+141.47%)</b></td><td>9515.98 <b>(+83.99%)</b></td><td>4152.22 <b>(-48.05%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20287.12 (n/a)</td><td>11360.06 (n/a)</td><td>5728.57 (n/a)</td><td>5172.09 (n/a)</td><td>7993.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.00 (-6.25%)</td><td>0.00 <b>(-36.36%)</b></td><td>0.00 <b>(-64.29%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-12.86%)</td><td>18919.43 (-7.50%)</td><td>14382.95 <b>(+44.49%)</b></td><td>16277.09 <b>(+176.66%)</b></td><td>5431.62 (+4.04%)</td><td>5411.98 (-17.73%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20453.07 (n/a)</td><td>9954.08 (n/a)</td><td>5883.50 (n/a)</td><td>5220.83 (n/a)</td><td>6578.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>0.15 (+9.91%)</td><td>0.10 (-0.48%)</td><td>0.09 (-6.05%)</td><td>0.08 (+2.10%)</td><td>0.03 (+14.05%)</td><td>25315.38 (-2.13%)</td><td>21079.90 (+0.94%)</td><td>22151.25 (+6.47%)</td><td>13806.81 (-9.03%)</td><td>4635.44 (-2.13%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>25866.42 (n/a)</td><td>20883.88 (n/a)</td><td>20805.40 (n/a)</td><td>15177.05 (n/a)</td><td>4736.50 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>1.63 (-10.12%)</td><td>1.38 (+0.67%)</td><td>1.44 (-2.23%)</td><td>0.95 (-5.92%)</td><td>0.28 <b>(-20.21%)</b></td><td>554.00 (+6.29%)</td><td>395.22 (-2.14%)</td><td>363.10 (+2.28%)</td><td>321.50 (+11.25%)</td><td>95.06 (-9.83%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>1.81 (n/a)</td><td>1.37 (n/a)</td><td>1.48 (n/a)</td><td>1.01 (n/a)</td><td>0.35 (n/a)</td><td>521.20 (n/a)</td><td>403.86 (n/a)</td><td>355.00 (n/a)</td><td>289.00 (n/a)</td><td>105.42 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>2.92 (+4.56%)</td><td>2.02 (+7.17%)</td><td>2.09 (-7.27%)</td><td>1.11 <b>(+271.78%)</b></td><td>0.71 <b>(-29.97%)</b></td><td>945.30 <b>(-73.10%)</b></td><td>581.50 <b>(-46.72%)</b></td><td>501.90 (+7.84%)</td><td>358.80 (-4.37%)</td><td>233.55 <b>(-82.83%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>2.79 (n/a)</td><td>1.89 (n/a)</td><td>2.25 (n/a)</td><td>0.30 (n/a)</td><td>1.01 (n/a)</td><td>3514.50 (n/a)</td><td>1091.44 (n/a)</td><td>465.40 (n/a)</td><td>375.20 (n/a)</td><td>1360.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:18:56</td><td>1.76 (+16.75%)</td><td>1.38 <b>(+32.08%)</b></td><td>1.42 <b>(+50.05%)</b></td><td>0.86 <b>(+83.00%)</b></td><td>0.36 <b>(-20.65%)</b></td><td>607.50 <b>(-45.35%)</b></td><td>406.46 <b>(-32.84%)</b></td><td>370.10 <b>(-33.35%)</b></td><td>297.20 (-14.33%)</td><td>124.31 <b>(-60.30%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>1.51 (n/a)</td><td>1.04 (n/a)</td><td>0.94 (n/a)</td><td>0.47 (n/a)</td><td>0.45 (n/a)</td><td>1111.70 (n/a)</td><td>605.24 (n/a)</td><td>555.30 (n/a)</td><td>346.90 (n/a)</td><td>313.14 (n/a)</td>
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
