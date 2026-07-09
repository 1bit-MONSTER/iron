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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.07 (+12.04%)</td><td>0.04 (-3.55%)</td><td>0.04 (+5.87%)</td><td>0.01 <b>(-71.41%)</b></td><td>0.02 <b>(+51.84%)</b></td><td>1997.30 <b>(+249.73%)</b></td><td>651.54 <b>(+76.28%)</b></td><td>295.60 (-5.56%)</td><td>186.50 (-10.77%)</td><td>760.75 <b>(+418.25%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.10 (n/a)</td><td>369.60 (n/a)</td><td>313.00 (n/a)</td><td>209.00 (n/a)</td><td>146.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 <b>(-38.11%)</b></td><td>0.02 <b>(-38.09%)</b></td><td>0.02 (-17.20%)</td><td>0.01 <b>(-72.31%)</b></td><td>0.01 <b>(-31.66%)</b></td><td>1990.10 <b>(+261.05%)</b></td><td>827.88 <b>(+95.22%)</b></td><td>630.10 <b>(+20.78%)</b></td><td>360.70 <b>(+61.60%)</b></td><td>659.22 <b>(+331.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.20 (n/a)</td><td>424.08 (n/a)</td><td>521.70 (n/a)</td><td>223.20 (n/a)</td><td>152.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (+0.51%)</td><td>0.03 (-14.37%)</td><td>0.03 <b>(-36.81%)</b></td><td>0.02 (-6.19%)</td><td>0.01 (-13.57%)</td><td>579.50 (+6.58%)</td><td>411.90 (+13.24%)</td><td>400.40 <b>(+58.26%)</b></td><td>237.20 (-0.50%)</td><td>145.69 (-8.37%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.70 (n/a)</td><td>363.74 (n/a)</td><td>253.00 (n/a)</td><td>238.40 (n/a)</td><td>159.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (+4.34%)</td><td>0.02 (-3.55%)</td><td>0.02 (+4.13%)</td><td>0.01 (-17.49%)</td><td>0.01 <b>(+35.69%)</b></td><td>600.80 <b>(+21.20%)</b></td><td>364.00 (+10.91%)</td><td>294.00 (-3.95%)</td><td>236.20 (-4.18%)</td><td>158.04 <b>(+54.49%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.70 (n/a)</td><td>328.18 (n/a)</td><td>306.10 (n/a)</td><td>246.50 (n/a)</td><td>102.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (+8.74%)</td><td>0.02 (+16.04%)</td><td>0.02 <b>(+54.71%)</b></td><td>0.01 (+11.47%)</td><td>0.01 (+4.08%)</td><td>571.30 (-10.30%)</td><td>366.32 (-14.36%)</td><td>269.10 <b>(-35.37%)</b></td><td>242.40 (-8.04%)</td><td>150.45 (-9.98%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.90 (n/a)</td><td>427.76 (n/a)</td><td>416.40 (n/a)</td><td>263.60 (n/a)</td><td>167.14 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (+8.77%)</td><td>0.02 (+8.55%)</td><td>0.02 <b>(+28.39%)</b></td><td>0.01 <b>(-35.21%)</b></td><td>0.01 <b>(+98.90%)</b></td><td>570.90 <b>(+54.34%)</b></td><td>328.02 (+0.89%)</td><td>263.70 <b>(-22.10%)</b></td><td>231.40 (-8.07%)</td><td>142.26 <b>(+179.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>369.90 (n/a)</td><td>325.14 (n/a)</td><td>338.50 (n/a)</td><td>251.70 (n/a)</td><td>50.96 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (+3.41%)</td><td>0.02 <b>(+26.19%)</b></td><td>0.02 <b>(+27.39%)</b></td><td>0.01 <b>(+43.63%)</b></td><td>0.00 <b>(-32.56%)</b></td><td>379.00 <b>(-30.37%)</b></td><td>312.08 <b>(-24.16%)</b></td><td>296.20 <b>(-21.49%)</b></td><td>254.10 (-3.31%)</td><td>50.75 <b>(-54.41%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.30 (n/a)</td><td>411.50 (n/a)</td><td>377.30 (n/a)</td><td>262.80 (n/a)</td><td>111.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 <b>(+30.44%)</b></td><td>0.02 (+17.92%)</td><td>0.02 <b>(+29.93%)</b></td><td>0.00 <b>(-75.56%)</b></td><td>0.01 <b>(+122.56%)</b></td><td>1824.50 <b>(+309.08%)</b></td><td>575.62 <b>(+53.02%)</b></td><td>307.70 <b>(-23.04%)</b></td><td>181.30 <b>(-23.34%)</b></td><td>700.17 <b>(+768.09%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>446.00 (n/a)</td><td>376.18 (n/a)</td><td>399.80 (n/a)</td><td>236.50 (n/a)</td><td>80.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 <b>(-27.02%)</b></td><td>0.01 (-14.43%)</td><td>0.01 (+3.19%)</td><td>0.01 (-2.37%)</td><td>0.00 <b>(-56.32%)</b></td><td>491.20 (+2.42%)</td><td>407.58 (+9.64%)</td><td>402.70 (-3.08%)</td><td>316.70 <b>(+37.04%)</b></td><td>69.34 <b>(-39.21%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>479.60 (n/a)</td><td>371.74 (n/a)</td><td>415.50 (n/a)</td><td>231.10 (n/a)</td><td>114.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>604.80 (n/a)</td><td>328.60 (n/a)</td><td>271.50 (n/a)</td><td>223.90 (n/a)</td><td>156.64 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1074.90 (n/a)</td><td>522.70 (n/a)</td><td>412.40 (n/a)</td><td>302.30 (n/a)</td><td>320.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.10 (n/a)</td><td>384.06 (n/a)</td><td>295.80 (n/a)</td><td>228.80 (n/a)</td><td>162.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.10 (n/a)</td><td>295.48 (n/a)</td><td>271.20 (n/a)</td><td>197.00 (n/a)</td><td>116.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>526.40 (n/a)</td><td>388.34 (n/a)</td><td>429.00 (n/a)</td><td>222.20 (n/a)</td><td>149.58 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>597.90 (n/a)</td><td>382.92 (n/a)</td><td>326.80 (n/a)</td><td>229.00 (n/a)</td><td>152.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.50 (n/a)</td><td>514.14 (n/a)</td><td>523.80 (n/a)</td><td>397.10 (n/a)</td><td>77.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.70 (n/a)</td><td>429.62 (n/a)</td><td>445.50 (n/a)</td><td>266.40 (n/a)</td><td>140.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>449.40 (n/a)</td><td>410.22 (n/a)</td><td>426.90 (n/a)</td><td>350.20 (n/a)</td><td>38.80 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1010.50 (n/a)</td><td>556.30 (n/a)</td><td>534.00 (n/a)</td><td>190.40 (n/a)</td><td>298.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.80 (n/a)</td><td>443.58 (n/a)</td><td>465.20 (n/a)</td><td>268.50 (n/a)</td><td>109.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>628.30 (n/a)</td><td>471.78 (n/a)</td><td>460.10 (n/a)</td><td>361.90 (n/a)</td><td>96.70 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.88 <b>(+43.32%)</b></td><td>0.45 (+7.14%)</td><td>0.39 (-1.21%)</td><td>0.13 <b>(-27.62%)</b></td><td>0.27 <b>(+67.19%)</b></td><td>1720.40 <b>(+38.15%)</b></td><td>722.80 (+13.67%)</td><td>562.20 (+1.22%)</td><td>250.10 <b>(-30.22%)</b></td><td>572.72 <b>(+62.47%)</b></td><td>37.73 <b>(+43.32%)</b></td><td>19.00 (+7.14%)</td><td>16.79 (-1.21%)</td><td>5.49 <b>(-27.62%)</b></td><td>11.67 <b>(+67.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.62 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>1245.30 (n/a)</td><td>635.90 (n/a)</td><td>555.40 (n/a)</td><td>358.40 (n/a)</td><td>352.52 (n/a)</td><td>26.33 (n/a)</td><td>17.73 (n/a)</td><td>16.99 (n/a)</td><td>7.58 (n/a)</td><td>6.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.52 (-6.43%)</td><td>0.38 (-5.70%)</td><td>0.39 (+12.48%)</td><td>0.13 <b>(-35.95%)</b></td><td>0.16 (+2.25%)</td><td>1768.00 <b>(+56.13%)</b></td><td>768.56 (+19.56%)</td><td>562.90 (-11.10%)</td><td>422.30 (+6.88%)</td><td>564.89 <b>(+89.40%)</b></td><td>22.35 (-6.43%)</td><td>16.00 (-5.70%)</td><td>16.76 (+12.48%)</td><td>5.34 <b>(-35.95%)</b></td><td>6.65 (+2.25%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>1132.40 (n/a)</td><td>642.84 (n/a)</td><td>633.20 (n/a)</td><td>395.10 (n/a)</td><td>298.25 (n/a)</td><td>23.88 (n/a)</td><td>16.97 (n/a)</td><td>14.90 (n/a)</td><td>8.33 (n/a)</td><td>6.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.31 (+1.76%)</td><td>0.31 (+3.23%)</td><td>0.31 (+3.91%)</td><td>0.30 (+3.61%)</td><td>0.00 <b>(-50.25%)</b></td><td>82914.70 (-3.49%)</td><td>81799.30 (-3.16%)</td><td>81948.20 (-3.77%)</td><td>80771.70 (-1.73%)</td><td>792.71 <b>(-52.90%)</b></td><td>212.70 (+1.76%)</td><td>210.04 (+3.23%)</td><td>209.64 (+3.91%)</td><td>207.20 (+3.61%)</td><td>2.03 <b>(-50.25%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85909.50 (n/a)</td><td>84466.00 (n/a)</td><td>85155.20 (n/a)</td><td>82194.40 (n/a)</td><td>1682.98 (n/a)</td><td>209.02 (n/a)</td><td>203.46 (n/a)</td><td>201.75 (n/a)</td><td>199.98 (n/a)</td><td>4.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>1.06 (+2.46%)</td><td>1.03 (+1.85%)</td><td>1.03 (-0.78%)</td><td>1.02 (+8.66%)</td><td>0.02 <b>(-58.43%)</b></td><td>24663.00 (-7.97%)</td><td>24355.56 (-1.94%)</td><td>24544.70 (+0.79%)</td><td>23649.00 (-2.40%)</td><td>409.21 <b>(-62.89%)</b></td><td>726.45 (+2.46%)</td><td>705.54 (+1.85%)</td><td>699.94 (-0.78%)</td><td>696.58 (+8.66%)</td><td>12.08 <b>(-58.43%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>1.04 (n/a)</td><td>1.01 (n/a)</td><td>1.03 (n/a)</td><td>0.94 (n/a)</td><td>0.04 (n/a)</td><td>26798.50 (n/a)</td><td>24836.36 (n/a)</td><td>24352.00 (n/a)</td><td>24229.80 (n/a)</td><td>1102.58 (n/a)</td><td>709.04 (n/a)</td><td>692.75 (n/a)</td><td>705.48 (n/a)</td><td>641.08 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>3.92 (-0.92%)</td><td>3.24 (+5.65%)</td><td>3.72 (+8.85%)</td><td>1.65 (-5.53%)</td><td>0.94 (+9.53%)</td><td>4889.60 (+5.85%)</td><td>2761.52 (-3.22%)</td><td>2169.70 (-8.13%)</td><td>2058.40 (+0.93%)</td><td>1204.71 (+16.00%)</td><td>1026.97 (-0.92%)</td><td>850.12 (+5.65%)</td><td>974.31 (+8.85%)</td><td>432.33 (-5.53%)</td><td>245.36 (+9.53%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>3.95 (n/a)</td><td>3.07 (n/a)</td><td>3.41 (n/a)</td><td>1.75 (n/a)</td><td>0.85 (n/a)</td><td>4619.20 (n/a)</td><td>2853.28 (n/a)</td><td>2361.60 (n/a)</td><td>2039.50 (n/a)</td><td>1038.58 (n/a)</td><td>1036.52 (n/a)</td><td>804.63 (n/a)</td><td>895.11 (n/a)</td><td>457.64 (n/a)</td><td>224.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.26 (-16.32%)</td><td>0.22 (-12.86%)</td><td>0.21 <b>(-26.29%)</b></td><td>0.20 (+12.00%)</td><td>0.03 <b>(-59.07%)</b></td><td>6193.30 (-10.71%)</td><td>5691.22 (+9.73%)</td><td>5857.50 <b>(+35.67%)</b></td><td>4707.00 (+19.50%)</td><td>592.68 <b>(-57.58%)</b></td><td>14.26 (-16.32%)</td><td>11.91 (-12.86%)</td><td>11.46 <b>(-26.29%)</b></td><td>10.84 (+12.00%)</td><td>1.38 <b>(-59.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>6936.30 (n/a)</td><td>5186.80 (n/a)</td><td>4317.60 (n/a)</td><td>3938.80 (n/a)</td><td>1397.04 (n/a)</td><td>17.04 (n/a)</td><td>13.66 (n/a)</td><td>15.54 (n/a)</td><td>9.68 (n/a)</td><td>3.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.10 <b>(-26.31%)</b></td><td>0.08 <b>(-25.89%)</b></td><td>0.07 <b>(-35.09%)</b></td><td>0.07 (+4.12%)</td><td>0.01 <b>(-50.29%)</b></td><td>0.10 <b>(-26.31%)</b></td><td>0.08 <b>(-25.89%)</b></td><td>0.07 <b>(-35.09%)</b></td><td>0.07 (+4.12%)</td><td>0.01 <b>(-50.29%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>3.95 (-0.55%)</td><td>3.77 (+2.07%)</td><td>3.73 (+1.52%)</td><td>3.65 (+5.71%)</td><td>0.13 <b>(-31.90%)</b></td><td>3.95 (-0.55%)</td><td>3.76 (+2.07%)</td><td>3.73 (+1.52%)</td><td>3.65 (+5.71%)</td><td>0.13 <b>(-31.90%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>3.97 (n/a)</td><td>3.69 (n/a)</td><td>3.67 (n/a)</td><td>3.45 (n/a)</td><td>0.18 (n/a)</td><td>3.97 (n/a)</td><td>3.69 (n/a)</td><td>3.67 (n/a)</td><td>3.45 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>6.79 (-12.01%)</td><td>5.68 (-8.30%)</td><td>5.89 (+4.72%)</td><td>4.62 (-7.03%)</td><td>0.90 <b>(-21.15%)</b></td><td>6.78 (-12.01%)</td><td>5.67 (-8.30%)</td><td>5.89 (+4.72%)</td><td>4.61 (-7.03%)</td><td>0.90 <b>(-21.15%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>7.72 (n/a)</td><td>6.19 (n/a)</td><td>5.63 (n/a)</td><td>4.96 (n/a)</td><td>1.14 (n/a)</td><td>7.71 (n/a)</td><td>6.19 (n/a)</td><td>5.62 (n/a)</td><td>4.96 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>13.90 <b>(+43.15%)</b></td><td>10.54 <b>(+32.13%)</b></td><td>8.92 <b>(+20.10%)</b></td><td>8.05 (+10.96%)</td><td>2.91 <b>(+180.91%)</b></td><td>13.89 <b>(+43.15%)</b></td><td>10.54 <b>(+32.13%)</b></td><td>8.91 <b>(+20.10%)</b></td><td>8.04 (+10.96%)</td><td>2.91 <b>(+180.91%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>9.71 (n/a)</td><td>7.98 (n/a)</td><td>7.43 (n/a)</td><td>7.25 (n/a)</td><td>1.04 (n/a)</td><td>9.70 (n/a)</td><td>7.98 (n/a)</td><td>7.42 (n/a)</td><td>7.25 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>3.89 (-1.54%)</td><td>3.62 (-3.93%)</td><td>3.61 (-5.31%)</td><td>3.29 (-5.74%)</td><td>0.23 <b>(+28.67%)</b></td><td>3.89 (-1.54%)</td><td>3.62 (-3.93%)</td><td>3.61 (-5.31%)</td><td>3.28 (-5.74%)</td><td>0.23 <b>(+28.67%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>3.95 (n/a)</td><td>3.77 (n/a)</td><td>3.82 (n/a)</td><td>3.49 (n/a)</td><td>0.18 (n/a)</td><td>3.95 (n/a)</td><td>3.76 (n/a)</td><td>3.81 (n/a)</td><td>3.49 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>7.38 (-2.61%)</td><td>6.33 (-4.47%)</td><td>6.13 (-15.96%)</td><td>5.59 <b>(+22.02%)</b></td><td>0.72 <b>(-43.61%)</b></td><td>7.37 (-2.61%)</td><td>6.33 (-4.47%)</td><td>6.13 (-15.96%)</td><td>5.59 <b>(+22.02%)</b></td><td>0.72 <b>(-43.61%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>7.57 (n/a)</td><td>6.63 (n/a)</td><td>7.29 (n/a)</td><td>4.58 (n/a)</td><td>1.29 (n/a)</td><td>7.57 (n/a)</td><td>6.62 (n/a)</td><td>7.29 (n/a)</td><td>4.58 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>13.59 (-0.91%)</td><td>10.07 (-0.42%)</td><td>9.81 (+6.29%)</td><td>8.51 (-0.82%)</td><td>2.08 (-1.30%)</td><td>13.59 (-0.91%)</td><td>10.06 (-0.42%)</td><td>9.80 (+6.29%)</td><td>8.51 (-0.82%)</td><td>2.08 (-1.30%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>13.72 (n/a)</td><td>10.11 (n/a)</td><td>9.23 (n/a)</td><td>8.58 (n/a)</td><td>2.10 (n/a)</td><td>13.71 (n/a)</td><td>10.10 (n/a)</td><td>9.22 (n/a)</td><td>8.58 (n/a)</td><td>2.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1934.30 (n/a)</td><td>947.62 (n/a)</td><td>301.90 (n/a)</td><td>282.80 (n/a)</td><td>894.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.40 (n/a)</td><td>360.38 (n/a)</td><td>289.10 (n/a)</td><td>229.60 (n/a)</td><td>133.14 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.00 (n/a)</td><td>431.26 (n/a)</td><td>433.70 (n/a)</td><td>294.80 (n/a)</td><td>123.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1081.50 (n/a)</td><td>636.24 (n/a)</td><td>516.90 (n/a)</td><td>465.00 (n/a)</td><td>255.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.70 (n/a)</td><td>471.34 (n/a)</td><td>514.20 (n/a)</td><td>291.90 (n/a)</td><td>103.94 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1929.40 (n/a)</td><td>781.94 (n/a)</td><td>605.20 (n/a)</td><td>283.70 (n/a)</td><td>655.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 <b>(-43.73%)</b></td><td>0.03 (-9.73%)</td><td>0.03 <b>(+37.01%)</b></td><td>0.02 (-14.28%)</td><td>0.01 <b>(-55.11%)</b></td><td>483.80 (+16.66%)</td><td>342.32 (+1.49%)</td><td>286.50 <b>(-27.01%)</b></td><td>257.30 <b>(+77.69%)</b></td><td>105.60 (-5.77%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>414.70 (n/a)</td><td>337.28 (n/a)</td><td>392.50 (n/a)</td><td>144.80 (n/a)</td><td>112.07 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 <b>(-32.58%)</b></td><td>0.02 <b>(-38.85%)</b></td><td>0.02 <b>(-43.03%)</b></td><td>0.01 <b>(-32.47%)</b></td><td>0.01 <b>(-26.45%)</b></td><td>641.00 <b>(+48.07%)</b></td><td>464.38 <b>(+64.84%)</b></td><td>471.90 <b>(+75.56%)</b></td><td>295.80 <b>(+48.35%)</b></td><td>135.86 <b>(+52.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>432.90 (n/a)</td><td>281.72 (n/a)</td><td>268.80 (n/a)</td><td>199.40 (n/a)</td><td>89.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 <b>(+30.41%)</b></td><td>0.02 (+9.42%)</td><td>0.02 (+0.93%)</td><td>0.01 (-14.35%)</td><td>0.01 <b>(+65.56%)</b></td><td>582.50 (+16.76%)</td><td>397.94 (-0.12%)</td><td>417.00 (-0.93%)</td><td>174.90 <b>(-23.32%)</b></td><td>148.17 <b>(+44.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.90 (n/a)</td><td>398.42 (n/a)</td><td>420.90 (n/a)</td><td>228.10 (n/a)</td><td>102.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 <b>(-44.25%)</b></td><td>0.02 (-14.97%)</td><td>0.02 (+2.11%)</td><td>0.01 <b>(+136.81%)</b></td><td>0.00 <b>(-85.25%)</b></td><td>576.80 <b>(-57.77%)</b></td><td>481.14 (-18.94%)</td><td>462.90 (-2.07%)</td><td>439.60 <b>(+79.36%)</b></td><td>54.81 <b>(-88.05%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1365.90 (n/a)</td><td>593.54 (n/a)</td><td>472.70 (n/a)</td><td>245.10 (n/a)</td><td>458.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (+15.61%)</td><td>0.03 (+19.01%)</td><td>0.03 <b>(+36.85%)</b></td><td>0.02 <b>(+20.72%)</b></td><td>0.01 <b>(+30.16%)</b></td><td>483.10 (-17.16%)</td><td>339.38 (-13.98%)</td><td>268.20 <b>(-26.92%)</b></td><td>231.60 (-13.49%)</td><td>127.85 (-2.23%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.20 (n/a)</td><td>394.52 (n/a)</td><td>367.00 (n/a)</td><td>267.70 (n/a)</td><td>130.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (+10.73%)</td><td>0.02 <b>(+26.61%)</b></td><td>0.02 (+17.70%)</td><td>0.01 (+18.66%)</td><td>0.01 (+17.80%)</td><td>552.20 (-15.72%)</td><td>399.50 <b>(-21.10%)</b></td><td>405.90 (-15.03%)</td><td>279.00 (-9.68%)</td><td>119.96 (-17.58%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.20 (n/a)</td><td>506.34 (n/a)</td><td>477.70 (n/a)</td><td>308.90 (n/a)</td><td>145.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (+11.11%)</td><td>0.03 <b>(+46.05%)</b></td><td>0.03 <b>(+88.89%)</b></td><td>0.02 <b>(+79.86%)</b></td><td>0.00 <b>(-34.75%)</b></td><td>374.30 <b>(-44.39%)</b></td><td>292.58 <b>(-36.77%)</b></td><td>261.10 <b>(-47.05%)</b></td><td>248.20 (-10.01%)</td><td>53.28 <b>(-66.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.10 (n/a)</td><td>462.70 (n/a)</td><td>493.10 (n/a)</td><td>275.80 (n/a)</td><td>159.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.05 (+2.98%)</td><td>0.04 (+12.96%)</td><td>0.04 (+12.06%)</td><td>0.03 <b>(+22.19%)</b></td><td>0.01 (-18.21%)</td><td>485.10 (-18.15%)</td><td>324.54 (-15.93%)</td><td>299.10 (-10.77%)</td><td>227.30 (-2.90%)</td><td>98.38 <b>(-34.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>592.70 (n/a)</td><td>386.04 (n/a)</td><td>335.20 (n/a)</td><td>234.10 (n/a)</td><td>149.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (-5.88%)</td><td>0.02 (-19.79%)</td><td>0.02 <b>(-44.53%)</b></td><td>0.01 (-8.37%)</td><td>0.01 (-2.76%)</td><td>559.30 (+9.13%)</td><td>452.76 <b>(+25.45%)</b></td><td>532.70 <b>(+80.27%)</b></td><td>262.40 (+6.23%)</td><td>130.29 (+11.79%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.50 (n/a)</td><td>360.92 (n/a)</td><td>295.50 (n/a)</td><td>247.00 (n/a)</td><td>116.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (+4.92%)</td><td>0.03 (+19.33%)</td><td>0.02 (+18.65%)</td><td>0.02 <b>(+43.66%)</b></td><td>0.01 (+10.47%)</td><td>568.40 <b>(-30.39%)</b></td><td>419.06 (-17.70%)</td><td>438.90 (-15.71%)</td><td>255.00 (-4.71%)</td><td>154.59 <b>(-25.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>816.50 (n/a)</td><td>509.18 (n/a)</td><td>520.70 (n/a)</td><td>267.60 (n/a)</td><td>208.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 (-6.31%)</td><td>0.02 (-7.67%)</td><td>0.02 <b>(-35.33%)</b></td><td>0.01 <b>(+296.97%)</b></td><td>0.01 <b>(-23.38%)</b></td><td>634.50 <b>(-74.81%)</b></td><td>448.72 <b>(-39.88%)</b></td><td>454.80 <b>(+54.59%)</b></td><td>259.50 (+6.75%)</td><td>182.60 <b>(-81.60%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2519.00 (n/a)</td><td>746.32 (n/a)</td><td>294.20 (n/a)</td><td>243.10 (n/a)</td><td>992.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 <b>(-30.47%)</b></td><td>0.02 <b>(-22.42%)</b></td><td>0.02 <b>(-37.88%)</b></td><td>0.02 (+14.10%)</td><td>0.00 <b>(-60.86%)</b></td><td>591.00 (-12.35%)</td><td>480.20 (+15.28%)</td><td>489.40 <b>(+60.99%)</b></td><td>376.60 <b>(+43.80%)</b></td><td>89.36 <b>(-51.36%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>674.30 (n/a)</td><td>416.56 (n/a)</td><td>304.00 (n/a)</td><td>261.90 (n/a)</td><td>183.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (+3.10%)</td><td>0.02 (+1.03%)</td><td>0.02 (-14.25%)</td><td>0.01 (-5.87%)</td><td>0.01 <b>(+21.14%)</b></td><td>620.30 (+6.23%)</td><td>419.78 (+3.83%)</td><td>484.70 (+16.63%)</td><td>224.80 (-3.02%)</td><td>164.43 <b>(+24.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.90 (n/a)</td><td>404.28 (n/a)</td><td>415.60 (n/a)</td><td>231.80 (n/a)</td><td>132.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 <b>(+48.69%)</b></td><td>0.02 (+18.50%)</td><td>0.02 (+0.28%)</td><td>0.01 (+9.53%)</td><td>0.01 <b>(+102.75%)</b></td><td>634.70 (-8.70%)</td><td>432.34 (-9.46%)</td><td>436.40 (-0.30%)</td><td>235.30 <b>(-32.73%)</b></td><td>159.65 (+19.92%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>695.20 (n/a)</td><td>477.50 (n/a)</td><td>437.70 (n/a)</td><td>349.80 (n/a)</td><td>133.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.02 <b>(-30.61%)</b></td><td>0.02 <b>(-25.43%)</b></td><td>0.02 <b>(-35.90%)</b></td><td>0.02 (+1.58%)</td><td>0.00 <b>(-68.42%)</b></td><td>514.00 (-1.55%)</td><td>454.60 <b>(+24.72%)</b></td><td>457.00 <b>(+56.03%)</b></td><td>372.90 <b>(+44.09%)</b></td><td>54.21 <b>(-55.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.10 (n/a)</td><td>364.50 (n/a)</td><td>292.90 (n/a)</td><td>258.80 (n/a)</td><td>123.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.04 (+0.89%)</td><td>0.03 (+10.54%)</td><td>0.02 (+7.01%)</td><td>0.02 (+7.68%)</td><td>0.01 (+11.52%)</td><td>548.50 (-7.13%)</td><td>412.18 (-8.12%)</td><td>452.20 (-6.55%)</td><td>248.70 (-0.88%)</td><td>144.32 (+2.85%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.60 (n/a)</td><td>448.60 (n/a)</td><td>483.90 (n/a)</td><td>250.90 (n/a)</td><td>140.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.03 <b>(+44.78%)</b></td><td>0.02 <b>(+60.41%)</b></td><td>0.02 <b>(+36.41%)</b></td><td>0.02 <b>(+382.00%)</b></td><td>0.01 (+9.25%)</td><td>509.10 <b>(-79.25%)</b></td><td>361.36 <b>(-57.75%)</b></td><td>374.10 <b>(-26.70%)</b></td><td>247.10 <b>(-30.92%)</b></td><td>114.77 <b>(-87.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2453.70 (n/a)</td><td>855.38 (n/a)</td><td>510.40 (n/a)</td><td>357.70 (n/a)</td><td>895.94 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.41 (-8.11%)</td><td>0.36 <b>(+48.12%)</b></td><td>0.39 <b>(+58.62%)</b></td><td>0.22 <b>(+325.82%)</b></td><td>0.08 <b>(-47.17%)</b></td><td>451.50 <b>(-76.51%)</b></td><td>289.36 <b>(-58.72%)</b></td><td>254.20 <b>(-36.97%)</b></td><td>239.40 (+8.82%)</td><td>91.08 <b>(-87.03%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.45 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>1922.40 (n/a)</td><td>701.04 (n/a)</td><td>403.30 (n/a)</td><td>220.00 (n/a)</td><td>702.07 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.42 (+5.52%)</td><td>0.29 (+13.80%)</td><td>0.35 <b>(+71.29%)</b></td><td>0.15 (-4.59%)</td><td>0.12 (+4.63%)</td><td>655.50 (+4.81%)</td><td>397.94 (-10.66%)</td><td>283.80 <b>(-41.62%)</b></td><td>232.00 (-5.23%)</td><td>192.61 (+6.85%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.40 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>625.40 (n/a)</td><td>445.40 (n/a)</td><td>486.10 (n/a)</td><td>244.80 (n/a)</td><td>180.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.41 (-4.47%)</td><td>0.24 (+1.52%)</td><td>0.22 (+19.35%)</td><td>0.15 <b>(+210.54%)</b></td><td>0.10 <b>(-35.48%)</b></td><td>644.80 <b>(-67.80%)</b></td><td>452.06 <b>(-37.66%)</b></td><td>440.20 (-16.22%)</td><td>238.10 (+4.71%)</td><td>148.32 <b>(-79.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.43 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>0.16 (n/a)</td><td>2002.40 (n/a)</td><td>725.14 (n/a)</td><td>525.40 (n/a)</td><td>227.40 (n/a)</td><td>731.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.29 <b>(+61.98%)</b></td><td>0.23 <b>(+51.77%)</b></td><td>0.24 <b>(+66.76%)</b></td><td>0.09 <b>(-20.02%)</b></td><td>0.08 <b>(+196.77%)</b></td><td>800.10 <b>(+25.04%)</b></td><td>387.22 <b>(-23.05%)</b></td><td>310.90 <b>(-40.03%)</b></td><td>251.50 <b>(-38.27%)</b></td><td>232.82 <b>(+146.22%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>639.90 (n/a)</td><td>503.24 (n/a)</td><td>518.40 (n/a)</td><td>407.40 (n/a)</td><td>94.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.31 <b>(+104.78%)</b></td><td>0.22 <b>(+87.68%)</b></td><td>0.24 <b>(+94.72%)</b></td><td>0.14 <b>(+100.82%)</b></td><td>0.08 <b>(+151.32%)</b></td><td>529.40 <b>(-50.21%)</b></td><td>364.88 <b>(-44.95%)</b></td><td>310.70 <b>(-48.65%)</b></td><td>239.50 <b>(-51.17%)</b></td><td>134.09 <b>(-41.44%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>1063.20 (n/a)</td><td>662.82 (n/a)</td><td>605.10 (n/a)</td><td>490.50 (n/a)</td><td>228.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.30 (-5.56%)</td><td>0.21 (-1.56%)</td><td>0.21 <b>(+36.38%)</b></td><td>0.12 <b>(-20.04%)</b></td><td>0.09 (+2.88%)</td><td>625.10 <b>(+25.07%)</b></td><td>415.12 (+5.71%)</td><td>355.40 <b>(-26.69%)</b></td><td>243.50 (+5.92%)</td><td>184.08 <b>(+34.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>499.80 (n/a)</td><td>392.70 (n/a)</td><td>484.80 (n/a)</td><td>229.90 (n/a)</td><td>136.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.49 (+1.42%)</td><td>0.36 <b>(+49.78%)</b></td><td>0.32 <b>(+51.32%)</b></td><td>0.24 <b>(+352.12%)</b></td><td>0.11 <b>(-25.44%)</b></td><td>539.60 <b>(-77.88%)</b></td><td>395.16 <b>(-56.08%)</b></td><td>414.40 <b>(-33.92%)</b></td><td>269.00 (-1.39%)</td><td>120.81 <b>(-86.16%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.48 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>2439.40 (n/a)</td><td>899.78 (n/a)</td><td>627.10 (n/a)</td><td>272.80 (n/a)</td><td>873.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.26 <b>(-47.14%)</b></td><td>0.23 <b>(-29.64%)</b></td><td>0.22 (-17.57%)</td><td>0.21 (-12.89%)</td><td>0.02 <b>(-82.06%)</b></td><td>630.20 (+14.79%)</td><td>569.48 <b>(+31.78%)</b></td><td>587.20 <b>(+21.32%)</b></td><td>509.70 <b>(+89.13%)</b></td><td>48.19 <b>(-62.05%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>549.00 (n/a)</td><td>432.16 (n/a)</td><td>484.00 (n/a)</td><td>269.50 (n/a)</td><td>126.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.41 <b>(-21.89%)</b></td><td>0.26 <b>(-24.86%)</b></td><td>0.23 <b>(-37.62%)</b></td><td>0.21 (+2.41%)</td><td>0.08 <b>(-38.56%)</b></td><td>632.90 (-2.36%)</td><td>534.52 <b>(+23.54%)</b></td><td>563.70 <b>(+60.28%)</b></td><td>321.50 <b>(+28.04%)</b></td><td>128.06 <b>(-28.93%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.52 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>648.20 (n/a)</td><td>432.66 (n/a)</td><td>351.70 (n/a)</td><td>251.10 (n/a)</td><td>180.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+250.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+229.77%)</b></td><td>20287.12 (+4.96%)</td><td>11360.06 <b>(-28.86%)</b></td><td>5728.57 <b>(-66.10%)</b></td><td>5172.09 <b>(-52.62%)</b></td><td>7993.13 <b>(+148.22%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19328.08 (n/a)</td><td>15968.12 (n/a)</td><td>16896.51 (n/a)</td><td>10916.30 (n/a)</td><td>3220.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.00 <b>(+23.08%)</b></td><td>0.00 (-5.17%)</td><td>0.00 (+7.69%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(+65.99%)</b></td><td>20453.07 <b>(+45.25%)</b></td><td>9954.08 <b>(+27.15%)</b></td><td>5883.50 (-6.42%)</td><td>5220.83 (-14.69%)</td><td>6578.59 <b>(+88.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>14081.45 (n/a)</td><td>7828.86 (n/a)</td><td>6287.46 (n/a)</td><td>6119.72 (n/a)</td><td>3497.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>0.14 (-0.07%)</td><td>0.10 (+11.62%)</td><td>0.10 <b>(+21.30%)</b></td><td>0.08 (+1.50%)</td><td>0.02 (-1.04%)</td><td>25866.42 (-1.43%)</td><td>20883.88 (-10.39%)</td><td>20805.40 (-17.51%)</td><td>15177.05 (+0.09%)</td><td>4736.50 (+2.08%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>26241.28 (n/a)</td><td>23305.43 (n/a)</td><td>25221.66 (n/a)</td><td>15163.43 (n/a)</td><td>4639.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>1.81 (+10.52%)</td><td>1.37 (+8.18%)</td><td>1.48 (-0.62%)</td><td>1.01 <b>(+25.64%)</b></td><td>0.35 (-9.48%)</td><td>521.20 <b>(-20.42%)</b></td><td>403.86 (-10.49%)</td><td>355.00 (+0.62%)</td><td>289.00 (-9.52%)</td><td>105.42 <b>(-31.69%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>1.64 (n/a)</td><td>1.27 (n/a)</td><td>1.49 (n/a)</td><td>0.80 (n/a)</td><td>0.38 (n/a)</td><td>654.90 (n/a)</td><td>451.18 (n/a)</td><td>352.80 (n/a)</td><td>319.40 (n/a)</td><td>154.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>2.79 (+13.81%)</td><td>1.89 <b>(+27.33%)</b></td><td>2.25 <b>(+80.33%)</b></td><td>0.30 (+1.13%)</td><td>1.01 (+13.83%)</td><td>3514.50 (-1.12%)</td><td>1091.44 (-12.11%)</td><td>465.40 <b>(-44.54%)</b></td><td>375.20 (-12.13%)</td><td>1360.37 (+3.70%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>2.46 (n/a)</td><td>1.48 (n/a)</td><td>1.25 (n/a)</td><td>0.30 (n/a)</td><td>0.89 (n/a)</td><td>3554.20 (n/a)</td><td>1241.76 (n/a)</td><td>839.20 (n/a)</td><td>427.00 (n/a)</td><td>1311.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:22:08</td><td>1.51 <b>(-25.41%)</b></td><td>1.04 <b>(-25.01%)</b></td><td>0.94 <b>(-36.25%)</b></td><td>0.47 <b>(-37.03%)</b></td><td>0.45 (-7.30%)</td><td>1111.70 <b>(+58.79%)</b></td><td>605.24 <b>(+42.79%)</b></td><td>555.30 <b>(+56.86%)</b></td><td>346.90 <b>(+34.04%)</b></td><td>313.14 <b>(+80.94%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>2.03 (n/a)</td><td>1.39 (n/a)</td><td>1.48 (n/a)</td><td>0.75 (n/a)</td><td>0.49 (n/a)</td><td>700.10 (n/a)</td><td>423.86 (n/a)</td><td>354.00 (n/a)</td><td>258.80 (n/a)</td><td>173.06 (n/a)</td>
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
