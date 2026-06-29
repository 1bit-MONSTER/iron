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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.06 <b>(+22.56%)</b></td><td>0.04 (+3.42%)</td><td>0.04 (+12.69%)</td><td>0.02 <b>(-20.08%)</b></td><td>0.01 <b>(+90.77%)</b></td><td>571.10 <b>(+25.13%)</b></td><td>369.60 (+5.93%)</td><td>313.00 (-11.26%)</td><td>209.00 (-18.39%)</td><td>146.79 <b>(+100.61%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>456.40 (n/a)</td><td>348.90 (n/a)</td><td>352.70 (n/a)</td><td>256.10 (n/a)</td><td>73.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.06 <b>(+53.14%)</b></td><td>0.03 <b>(+34.21%)</b></td><td>0.02 (-14.63%)</td><td>0.02 <b>(+143.00%)</b></td><td>0.01 <b>(+38.57%)</b></td><td>551.20 <b>(-58.84%)</b></td><td>424.08 <b>(-32.70%)</b></td><td>521.70 (+17.16%)</td><td>223.20 <b>(-34.70%)</b></td><td>152.88 <b>(-62.83%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1339.30 (n/a)</td><td>630.14 (n/a)</td><td>445.30 (n/a)</td><td>341.80 (n/a)</td><td>411.31 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.05 <b>(+98.26%)</b></td><td>0.04 <b>(+87.57%)</b></td><td>0.05 <b>(+101.39%)</b></td><td>0.02 <b>(+299.40%)</b></td><td>0.01 <b>(+72.74%)</b></td><td>543.70 <b>(-74.96%)</b></td><td>363.74 <b>(-56.49%)</b></td><td>253.00 <b>(-50.34%)</b></td><td>238.40 <b>(-49.57%)</b></td><td>159.01 <b>(-78.71%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2171.60 (n/a)</td><td>836.08 (n/a)</td><td>509.50 (n/a)</td><td>472.70 (n/a)</td><td>746.98 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 <b>(-24.67%)</b></td><td>0.02 (-14.06%)</td><td>0.02 (-10.90%)</td><td>0.01 (-0.46%)</td><td>0.00 <b>(-30.25%)</b></td><td>495.70 (+0.45%)</td><td>328.18 (+12.00%)</td><td>306.10 (+12.21%)</td><td>246.50 <b>(+32.74%)</b></td><td>102.30 (-13.39%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>493.50 (n/a)</td><td>293.02 (n/a)</td><td>272.80 (n/a)</td><td>185.70 (n/a)</td><td>118.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 <b>(-37.39%)</b></td><td>0.01 (+3.72%)</td><td>0.01 <b>(+20.43%)</b></td><td>0.01 <b>(+68.35%)</b></td><td>0.01 <b>(-47.76%)</b></td><td>636.90 <b>(-40.60%)</b></td><td>427.76 <b>(-23.24%)</b></td><td>416.40 (-16.95%)</td><td>263.60 <b>(+59.66%)</b></td><td>167.14 <b>(-48.79%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1072.20 (n/a)</td><td>557.28 (n/a)</td><td>501.40 (n/a)</td><td>165.10 (n/a)</td><td>326.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 <b>(-45.19%)</b></td><td>0.02 <b>(-35.36%)</b></td><td>0.02 <b>(-30.58%)</b></td><td>0.01 <b>(-28.60%)</b></td><td>0.00 <b>(-62.09%)</b></td><td>369.90 <b>(+40.06%)</b></td><td>325.14 <b>(+49.49%)</b></td><td>338.50 <b>(+44.04%)</b></td><td>251.70 <b>(+82.39%)</b></td><td>50.96 (-0.42%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>264.10 (n/a)</td><td>217.50 (n/a)</td><td>235.00 (n/a)</td><td>138.00 (n/a)</td><td>51.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 <b>(-37.56%)</b></td><td>0.01 <b>(-40.93%)</b></td><td>0.01 <b>(-40.61%)</b></td><td>0.01 <b>(-38.50%)</b></td><td>0.00 <b>(-41.40%)</b></td><td>544.30 <b>(+62.57%)</b></td><td>411.50 <b>(+67.60%)</b></td><td>377.30 <b>(+68.36%)</b></td><td>262.80 <b>(+60.15%)</b></td><td>111.30 <b>(+48.82%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>334.80 (n/a)</td><td>245.52 (n/a)</td><td>224.10 (n/a)</td><td>164.10 (n/a)</td><td>74.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (+7.46%)</td><td>0.01 (-2.49%)</td><td>0.01 <b>(-23.51%)</b></td><td>0.01 <b>(+33.81%)</b></td><td>0.00 <b>(-22.21%)</b></td><td>446.00 <b>(-25.27%)</b></td><td>376.18 (-4.80%)</td><td>399.80 <b>(+30.74%)</b></td><td>236.50 (-6.93%)</td><td>80.66 <b>(-50.02%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.80 (n/a)</td><td>395.14 (n/a)</td><td>305.80 (n/a)</td><td>254.10 (n/a)</td><td>161.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 <b>(+166.35%)</b></td><td>0.02 <b>(+119.26%)</b></td><td>0.01 <b>(+53.43%)</b></td><td>0.01 <b>(+286.71%)</b></td><td>0.01 <b>(+122.15%)</b></td><td>479.60 <b>(-74.14%)</b></td><td>371.74 <b>(-58.36%)</b></td><td>415.50 <b>(-34.82%)</b></td><td>231.10 <b>(-62.46%)</b></td><td>114.05 <b>(-78.86%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1854.70 (n/a)</td><td>892.66 (n/a)</td><td>637.50 (n/a)</td><td>615.60 (n/a)</td><td>539.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>582.70 (n/a)</td><td>399.54 (n/a)</td><td>417.30 (n/a)</td><td>249.70 (n/a)</td><td>132.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>581.30 (n/a)</td><td>357.48 (n/a)</td><td>250.90 (n/a)</td><td>183.10 (n/a)</td><td>186.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2440.70 (n/a)</td><td>800.44 (n/a)</td><td>483.80 (n/a)</td><td>251.00 (n/a)</td><td>925.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>680.10 (n/a)</td><td>425.30 (n/a)</td><td>397.00 (n/a)</td><td>288.10 (n/a)</td><td>153.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>416.28 (n/a)</td><td>444.10 (n/a)</td><td>236.20 (n/a)</td><td>147.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>590.90 (n/a)</td><td>468.90 (n/a)</td><td>464.60 (n/a)</td><td>396.00 (n/a)</td><td>80.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>354.02 (n/a)</td><td>309.90 (n/a)</td><td>244.30 (n/a)</td><td>135.05 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.00 (n/a)</td><td>427.38 (n/a)</td><td>524.10 (n/a)</td><td>225.60 (n/a)</td><td>179.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.10 (n/a)</td><td>406.94 (n/a)</td><td>385.80 (n/a)</td><td>248.10 (n/a)</td><td>112.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.90 (n/a)</td><td>331.72 (n/a)</td><td>311.10 (n/a)</td><td>234.60 (n/a)</td><td>90.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.40 (n/a)</td><td>448.38 (n/a)</td><td>510.30 (n/a)</td><td>213.30 (n/a)</td><td>138.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>816.50 (n/a)</td><td>558.96 (n/a)</td><td>492.20 (n/a)</td><td>399.50 (n/a)</td><td>175.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.62 (-4.53%)</td><td>0.42 (-3.53%)</td><td>0.40 (+5.92%)</td><td>0.18 <b>(-49.28%)</b></td><td>0.16 <b>(+33.30%)</b></td><td>1245.30 <b>(+97.13%)</b></td><td>635.90 (+17.85%)</td><td>555.40 (-5.58%)</td><td>358.40 (+4.73%)</td><td>352.52 <b>(+204.52%)</b></td><td>26.33 (-4.53%)</td><td>17.73 (-3.53%)</td><td>16.99 (+5.92%)</td><td>7.58 <b>(-49.28%)</b></td><td>6.98 <b>(+33.30%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.65 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>631.70 (n/a)</td><td>539.58 (n/a)</td><td>588.20 (n/a)</td><td>342.20 (n/a)</td><td>115.76 (n/a)</td><td>27.58 (n/a)</td><td>18.38 (n/a)</td><td>16.04 (n/a)</td><td>14.94 (n/a)</td><td>5.23 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.56 (+2.90%)</td><td>0.40 (-10.58%)</td><td>0.35 (-18.32%)</td><td>0.20 <b>(-45.19%)</b></td><td>0.15 <b>(+85.25%)</b></td><td>1132.40 <b>(+82.47%)</b></td><td>642.84 <b>(+25.80%)</b></td><td>633.20 <b>(+22.43%)</b></td><td>395.10 (-2.83%)</td><td>298.25 <b>(+220.49%)</b></td><td>23.88 (+2.90%)</td><td>16.97 (-10.58%)</td><td>14.90 (-18.32%)</td><td>8.33 <b>(-45.19%)</b></td><td>6.51 <b>(+85.25%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>620.60 (n/a)</td><td>511.02 (n/a)</td><td>517.20 (n/a)</td><td>406.60 (n/a)</td><td>93.06 (n/a)</td><td>23.21 (n/a)</td><td>18.98 (n/a)</td><td>18.25 (n/a)</td><td>15.21 (n/a)</td><td>3.51 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.31 (-1.48%)</td><td>0.30 (-2.69%)</td><td>0.30 (-4.09%)</td><td>0.29 (-1.42%)</td><td>0.01 (+7.73%)</td><td>85909.50 (+1.44%)</td><td>84466.00 (+2.77%)</td><td>85155.20 (+4.27%)</td><td>82194.40 (+1.50%)</td><td>1682.98 (+11.04%)</td><td>209.02 (-1.48%)</td><td>203.46 (-2.69%)</td><td>201.75 (-4.09%)</td><td>199.98 (-1.42%)</td><td>4.09 (+7.73%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84687.50 (n/a)</td><td>82190.72 (n/a)</td><td>81670.10 (n/a)</td><td>80980.40 (n/a)</td><td>1515.67 (n/a)</td><td>212.15 (n/a)</td><td>209.08 (n/a)</td><td>210.36 (n/a)</td><td>202.86 (n/a)</td><td>3.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>1.04 (+1.77%)</td><td>1.01 (+3.27%)</td><td>1.03 (+2.37%)</td><td>0.94 (+3.34%)</td><td>0.04 (-10.66%)</td><td>26798.50 (-3.23%)</td><td>24836.36 (-3.21%)</td><td>24352.00 (-2.31%)</td><td>24229.80 (-1.74%)</td><td>1102.58 (-14.60%)</td><td>709.04 (+1.77%)</td><td>692.75 (+3.27%)</td><td>705.48 (+2.37%)</td><td>641.08 (+3.34%)</td><td>29.07 (-10.66%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>1.02 (n/a)</td><td>0.98 (n/a)</td><td>1.01 (n/a)</td><td>0.91 (n/a)</td><td>0.05 (n/a)</td><td>27693.90 (n/a)</td><td>25659.76 (n/a)</td><td>24928.50 (n/a)</td><td>24658.50 (n/a)</td><td>1291.06 (n/a)</td><td>696.71 (n/a)</td><td>670.84 (n/a)</td><td>689.16 (n/a)</td><td>620.35 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>3.95 <b>(+74.03%)</b></td><td>3.07 <b>(+76.78%)</b></td><td>3.41 <b>(+112.08%)</b></td><td>1.75 <b>(+31.00%)</b></td><td>0.85 <b>(+109.26%)</b></td><td>4619.20 <b>(-23.67%)</b></td><td>2853.28 <b>(-41.13%)</b></td><td>2361.60 <b>(-52.85%)</b></td><td>2039.50 <b>(-42.54%)</b></td><td>1038.58 (-4.33%)</td><td>1036.52 <b>(+74.03%)</b></td><td>804.63 <b>(+76.78%)</b></td><td>895.11 <b>(+112.08%)</b></td><td>457.64 <b>(+31.00%)</b></td><td>224.01 <b>(+109.26%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>2.27 (n/a)</td><td>1.74 (n/a)</td><td>1.61 (n/a)</td><td>1.33 (n/a)</td><td>0.41 (n/a)</td><td>6051.30 (n/a)</td><td>4847.08 (n/a)</td><td>5008.50 (n/a)</td><td>3549.20 (n/a)</td><td>1085.54 (n/a)</td><td>595.60 (n/a)</td><td>455.16 (n/a)</td><td>422.07 (n/a)</td><td>349.34 (n/a)</td><td>107.05 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.32 (+9.22%)</td><td>0.25 (+15.02%)</td><td>0.29 <b>(+39.49%)</b></td><td>0.18 (+0.73%)</td><td>0.06 <b>(+45.54%)</b></td><td>6936.30 (-0.72%)</td><td>5186.80 (-10.67%)</td><td>4317.60 <b>(-28.31%)</b></td><td>3938.80 (-8.44%)</td><td>1397.04 <b>(+37.18%)</b></td><td>17.04 (+9.22%)</td><td>13.66 (+15.02%)</td><td>15.54 <b>(+39.49%)</b></td><td>9.68 (+0.73%)</td><td>3.37 <b>(+45.54%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>6986.90 (n/a)</td><td>5806.54 (n/a)</td><td>6022.80 (n/a)</td><td>4302.00 (n/a)</td><td>1018.41 (n/a)</td><td>15.60 (n/a)</td><td>11.88 (n/a)</td><td>11.14 (n/a)</td><td>9.60 (n/a)</td><td>2.32 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.14 (+4.03%)</td><td>0.11 <b>(+42.53%)</b></td><td>0.11 <b>(+57.74%)</b></td><td>0.06 <b>(+60.53%)</b></td><td>0.03 (-19.57%)</td><td>0.13 (+4.03%)</td><td>0.10 <b>(+42.53%)</b></td><td>0.11 <b>(+57.74%)</b></td><td>0.06 <b>(+60.53%)</b></td><td>0.03 (-19.57%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>3.97 (+5.75%)</td><td>3.69 (+2.62%)</td><td>3.67 (-0.69%)</td><td>3.45 (+2.18%)</td><td>0.18 (+3.10%)</td><td>3.97 (+5.75%)</td><td>3.69 (+2.62%)</td><td>3.67 (-0.69%)</td><td>3.45 (+2.18%)</td><td>0.18 (+3.10%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>3.76 (n/a)</td><td>3.59 (n/a)</td><td>3.70 (n/a)</td><td>3.38 (n/a)</td><td>0.18 (n/a)</td><td>3.75 (n/a)</td><td>3.59 (n/a)</td><td>3.70 (n/a)</td><td>3.38 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>7.72 (+4.93%)</td><td>6.19 (-0.76%)</td><td>5.63 (-4.08%)</td><td>4.96 (-11.19%)</td><td>1.14 <b>(+44.77%)</b></td><td>7.71 (+4.93%)</td><td>6.19 (-0.76%)</td><td>5.62 (-4.08%)</td><td>4.96 (-11.19%)</td><td>1.14 <b>(+44.77%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>7.35 (n/a)</td><td>6.24 (n/a)</td><td>5.87 (n/a)</td><td>5.59 (n/a)</td><td>0.79 (n/a)</td><td>7.35 (n/a)</td><td>6.23 (n/a)</td><td>5.86 (n/a)</td><td>5.59 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>9.71 <b>(-23.99%)</b></td><td>7.98 (-15.54%)</td><td>7.43 (-11.22%)</td><td>7.25 (-9.96%)</td><td>1.04 <b>(-48.44%)</b></td><td>9.70 <b>(-23.99%)</b></td><td>7.98 (-15.54%)</td><td>7.42 (-11.22%)</td><td>7.25 (-9.96%)</td><td>1.04 <b>(-48.44%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>12.77 (n/a)</td><td>9.45 (n/a)</td><td>8.36 (n/a)</td><td>8.06 (n/a)</td><td>2.01 (n/a)</td><td>12.76 (n/a)</td><td>9.44 (n/a)</td><td>8.36 (n/a)</td><td>8.05 (n/a)</td><td>2.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>3.95 (+3.33%)</td><td>3.77 (+1.21%)</td><td>3.82 (+0.20%)</td><td>3.49 (+1.68%)</td><td>0.18 (+8.47%)</td><td>3.95 (+3.33%)</td><td>3.76 (+1.21%)</td><td>3.81 (+0.20%)</td><td>3.49 (+1.68%)</td><td>0.18 (+8.47%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>3.82 (n/a)</td><td>3.72 (n/a)</td><td>3.81 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td><td>3.82 (n/a)</td><td>3.72 (n/a)</td><td>3.81 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>7.57 (+12.40%)</td><td>6.63 (+5.09%)</td><td>7.29 (+8.65%)</td><td>4.58 (-18.48%)</td><td>1.29 <b>(+125.70%)</b></td><td>7.57 (+12.40%)</td><td>6.62 (+5.09%)</td><td>7.29 (+8.65%)</td><td>4.58 (-18.48%)</td><td>1.28 <b>(+125.70%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>6.74 (n/a)</td><td>6.31 (n/a)</td><td>6.71 (n/a)</td><td>5.62 (n/a)</td><td>0.57 (n/a)</td><td>6.73 (n/a)</td><td>6.30 (n/a)</td><td>6.71 (n/a)</td><td>5.62 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>13.72 (-2.27%)</td><td>10.11 (-3.80%)</td><td>9.23 (+8.35%)</td><td>8.58 (+5.84%)</td><td>2.10 <b>(-28.72%)</b></td><td>13.71 (-2.27%)</td><td>10.10 (-3.80%)</td><td>9.22 (+8.35%)</td><td>8.58 (+5.84%)</td><td>2.10 <b>(-28.72%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>14.04 (n/a)</td><td>10.51 (n/a)</td><td>8.52 (n/a)</td><td>8.11 (n/a)</td><td>2.95 (n/a)</td><td>14.03 (n/a)</td><td>10.50 (n/a)</td><td>8.51 (n/a)</td><td>8.10 (n/a)</td><td>2.95 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>422.70 (n/a)</td><td>323.24 (n/a)</td><td>309.80 (n/a)</td><td>266.40 (n/a)</td><td>59.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.80 (n/a)</td><td>402.22 (n/a)</td><td>377.60 (n/a)</td><td>266.70 (n/a)</td><td>141.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.90 (n/a)</td><td>406.38 (n/a)</td><td>423.10 (n/a)</td><td>299.90 (n/a)</td><td>94.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.30 (n/a)</td><td>411.58 (n/a)</td><td>503.90 (n/a)</td><td>210.50 (n/a)</td><td>169.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1095.90 (n/a)</td><td>599.66 (n/a)</td><td>469.90 (n/a)</td><td>356.50 (n/a)</td><td>293.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.50 (n/a)</td><td>439.78 (n/a)</td><td>456.90 (n/a)</td><td>212.30 (n/a)</td><td>182.53 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.06 <b>(+103.42%)</b></td><td>0.03 <b>(+26.23%)</b></td><td>0.02 (-17.94%)</td><td>0.02 <b>(+60.11%)</b></td><td>0.02 <b>(+138.16%)</b></td><td>414.70 <b>(-37.54%)</b></td><td>337.28 (-15.64%)</td><td>392.50 <b>(+21.86%)</b></td><td>144.80 <b>(-50.83%)</b></td><td>112.07 <b>(-28.49%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>663.90 (n/a)</td><td>399.80 (n/a)</td><td>322.10 (n/a)</td><td>294.50 (n/a)</td><td>156.72 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (+18.39%)</td><td>0.03 <b>(+34.44%)</b></td><td>0.03 (+9.48%)</td><td>0.02 <b>(+334.43%)</b></td><td>0.01 <b>(-33.72%)</b></td><td>432.90 <b>(-76.98%)</b></td><td>281.72 <b>(-55.05%)</b></td><td>268.80 (-8.66%)</td><td>199.40 (-15.54%)</td><td>89.26 <b>(-87.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1880.50 (n/a)</td><td>626.76 (n/a)</td><td>294.30 (n/a)</td><td>236.10 (n/a)</td><td>705.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (+16.77%)</td><td>0.02 <b>(+22.78%)</b></td><td>0.02 <b>(+37.93%)</b></td><td>0.02 <b>(+290.23%)</b></td><td>0.01 <b>(-33.01%)</b></td><td>498.90 <b>(-74.37%)</b></td><td>398.42 <b>(-47.41%)</b></td><td>420.90 <b>(-27.49%)</b></td><td>228.10 (-14.34%)</td><td>102.19 <b>(-85.25%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1946.90 (n/a)</td><td>757.54 (n/a)</td><td>580.50 (n/a)</td><td>266.30 (n/a)</td><td>692.98 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (+11.79%)</td><td>0.02 (+2.25%)</td><td>0.02 (+0.71%)</td><td>0.01 <b>(-61.78%)</b></td><td>0.01 <b>(+103.05%)</b></td><td>1365.90 <b>(+161.62%)</b></td><td>593.54 <b>(+35.85%)</b></td><td>472.70 (-0.69%)</td><td>245.10 (-10.55%)</td><td>458.86 <b>(+375.24%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.10 (n/a)</td><td>436.90 (n/a)</td><td>476.00 (n/a)</td><td>274.00 (n/a)</td><td>96.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (-12.78%)</td><td>0.02 (+12.20%)</td><td>0.02 <b>(+29.38%)</b></td><td>0.01 (+7.10%)</td><td>0.01 <b>(-21.06%)</b></td><td>583.20 (-6.64%)</td><td>394.52 (-13.97%)</td><td>367.00 <b>(-22.72%)</b></td><td>267.70 (+14.65%)</td><td>130.76 (-14.04%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.70 (n/a)</td><td>458.58 (n/a)</td><td>474.90 (n/a)</td><td>233.50 (n/a)</td><td>152.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (+0.19%)</td><td>0.02 (+1.91%)</td><td>0.02 (+17.39%)</td><td>0.01 (-2.86%)</td><td>0.01 (+2.64%)</td><td>655.20 (+2.95%)</td><td>506.34 (-1.06%)</td><td>477.70 (-14.82%)</td><td>308.90 (-0.19%)</td><td>145.54 (+11.12%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.40 (n/a)</td><td>511.74 (n/a)</td><td>560.80 (n/a)</td><td>309.50 (n/a)</td><td>130.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 <b>(-35.98%)</b></td><td>0.02 <b>(-26.58%)</b></td><td>0.02 <b>(-34.35%)</b></td><td>0.01 <b>(-27.29%)</b></td><td>0.01 <b>(-39.37%)</b></td><td>673.10 <b>(+37.54%)</b></td><td>462.70 <b>(+32.53%)</b></td><td>493.10 <b>(+52.33%)</b></td><td>275.80 <b>(+56.17%)</b></td><td>159.50 <b>(+25.89%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.40 (n/a)</td><td>349.14 (n/a)</td><td>323.70 (n/a)</td><td>176.60 (n/a)</td><td>126.69 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.05 <b>(+62.02%)</b></td><td>0.04 <b>(+29.89%)</b></td><td>0.04 <b>(+33.32%)</b></td><td>0.02 (-13.51%)</td><td>0.01 <b>(+269.55%)</b></td><td>592.70 (+15.63%)</td><td>386.04 (-14.68%)</td><td>335.20 <b>(-24.98%)</b></td><td>234.10 <b>(-38.28%)</b></td><td>149.09 <b>(+163.96%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>512.60 (n/a)</td><td>452.44 (n/a)</td><td>446.80 (n/a)</td><td>379.30 (n/a)</td><td>56.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (-4.23%)</td><td>0.02 (+13.09%)</td><td>0.03 <b>(+37.60%)</b></td><td>0.02 (+17.19%)</td><td>0.01 (-18.26%)</td><td>512.50 (-14.67%)</td><td>360.92 (-16.05%)</td><td>295.50 <b>(-27.32%)</b></td><td>247.00 (+4.44%)</td><td>116.55 <b>(-29.44%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.60 (n/a)</td><td>429.92 (n/a)</td><td>406.60 (n/a)</td><td>236.50 (n/a)</td><td>165.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (+2.80%)</td><td>0.02 (-14.95%)</td><td>0.02 <b>(-20.16%)</b></td><td>0.01 <b>(-22.37%)</b></td><td>0.01 (+5.99%)</td><td>816.50 <b>(+28.81%)</b></td><td>509.18 <b>(+22.36%)</b></td><td>520.70 <b>(+25.26%)</b></td><td>267.60 (-2.73%)</td><td>208.27 <b>(+39.10%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>633.90 (n/a)</td><td>416.14 (n/a)</td><td>415.70 (n/a)</td><td>275.10 (n/a)</td><td>149.72 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (-7.09%)</td><td>0.02 (+1.89%)</td><td>0.03 <b>(+50.68%)</b></td><td>0.00 <b>(-77.53%)</b></td><td>0.01 <b>(+28.38%)</b></td><td>2519.00 <b>(+344.97%)</b></td><td>746.32 <b>(+81.52%)</b></td><td>294.20 <b>(-33.62%)</b></td><td>243.10 (+7.61%)</td><td>992.55 <b>(+575.68%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.10 (n/a)</td><td>411.16 (n/a)</td><td>443.20 (n/a)</td><td>225.90 (n/a)</td><td>146.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (-18.78%)</td><td>0.03 (+13.57%)</td><td>0.03 <b>(+69.76%)</b></td><td>0.02 (-8.36%)</td><td>0.01 (-19.26%)</td><td>674.30 (+9.11%)</td><td>416.56 (-12.60%)</td><td>304.00 <b>(-41.10%)</b></td><td>261.90 <b>(+23.13%)</b></td><td>183.72 (+16.07%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>618.00 (n/a)</td><td>476.62 (n/a)</td><td>516.10 (n/a)</td><td>212.70 (n/a)</td><td>158.28 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 (-7.02%)</td><td>0.02 (-1.76%)</td><td>0.02 (-0.33%)</td><td>0.01 <b>(+30.24%)</b></td><td>0.01 <b>(-25.79%)</b></td><td>583.90 <b>(-23.22%)</b></td><td>404.28 (-8.18%)</td><td>415.60 (+0.31%)</td><td>231.80 (+7.56%)</td><td>132.53 <b>(-39.25%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>760.50 (n/a)</td><td>440.30 (n/a)</td><td>414.30 (n/a)</td><td>215.50 (n/a)</td><td>218.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 <b>(-30.47%)</b></td><td>0.02 (-0.74%)</td><td>0.02 <b>(+25.91%)</b></td><td>0.01 (-2.23%)</td><td>0.00 <b>(-50.22%)</b></td><td>695.20 (+2.28%)</td><td>477.50 (-6.21%)</td><td>437.70 <b>(-20.58%)</b></td><td>349.80 <b>(+43.83%)</b></td><td>133.12 (-17.26%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.70 (n/a)</td><td>509.14 (n/a)</td><td>551.10 (n/a)</td><td>243.20 (n/a)</td><td>160.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.03 (+6.46%)</td><td>0.02 (+10.28%)</td><td>0.03 <b>(+32.24%)</b></td><td>0.02 (+6.93%)</td><td>0.01 (+2.01%)</td><td>522.10 (-6.48%)</td><td>364.50 (-9.67%)</td><td>292.90 <b>(-24.39%)</b></td><td>258.80 (-6.06%)</td><td>123.16 (-6.97%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.30 (n/a)</td><td>403.50 (n/a)</td><td>387.40 (n/a)</td><td>275.50 (n/a)</td><td>132.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.04 <b>(+36.55%)</b></td><td>0.02 (+1.30%)</td><td>0.02 <b>(-22.30%)</b></td><td>0.02 (+6.44%)</td><td>0.01 <b>(+68.33%)</b></td><td>590.60 (-6.06%)</td><td>448.60 (+3.41%)</td><td>483.90 <b>(+28.70%)</b></td><td>250.90 <b>(-26.77%)</b></td><td>140.32 (+16.69%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.70 (n/a)</td><td>433.80 (n/a)</td><td>376.00 (n/a)</td><td>342.60 (n/a)</td><td>120.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.02 (-18.33%)</td><td>0.02 (-14.38%)</td><td>0.02 (+1.53%)</td><td>0.00 <b>(-76.68%)</b></td><td>0.01 <b>(+29.07%)</b></td><td>2453.70 <b>(+328.89%)</b></td><td>855.38 <b>(+76.86%)</b></td><td>510.40 (-1.51%)</td><td>357.70 <b>(+22.46%)</b></td><td>895.94 <b>(+716.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.10 (n/a)</td><td>483.64 (n/a)</td><td>518.20 (n/a)</td><td>292.10 (n/a)</td><td>109.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.45 (+16.71%)</td><td>0.24 (-7.63%)</td><td>0.24 <b>(-22.12%)</b></td><td>0.05 (+6.28%)</td><td>0.15 (+6.89%)</td><td>1922.40 (-5.91%)</td><td>701.04 (+3.53%)</td><td>403.30 <b>(+28.40%)</b></td><td>220.00 (-14.33%)</td><td>702.07 (-8.92%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.31 (n/a)</td><td>0.05 (n/a)</td><td>0.14 (n/a)</td><td>2043.20 (n/a)</td><td>677.16 (n/a)</td><td>314.10 (n/a)</td><td>256.80 (n/a)</td><td>770.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.40 <b>(-20.70%)</b></td><td>0.26 <b>(-30.68%)</b></td><td>0.20 <b>(-49.10%)</b></td><td>0.16 (-19.59%)</td><td>0.12 (+2.89%)</td><td>625.40 <b>(+24.38%)</b></td><td>445.40 <b>(+52.22%)</b></td><td>486.10 <b>(+96.48%)</b></td><td>244.80 <b>(+26.12%)</b></td><td>180.26 <b>(+48.68%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.40 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>502.80 (n/a)</td><td>292.60 (n/a)</td><td>247.40 (n/a)</td><td>194.10 (n/a)</td><td>121.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.43 (-2.57%)</td><td>0.24 <b>(-20.56%)</b></td><td>0.19 <b>(-42.46%)</b></td><td>0.05 <b>(-70.43%)</b></td><td>0.16 <b>(+26.40%)</b></td><td>2002.40 <b>(+238.24%)</b></td><td>725.14 <b>(+89.83%)</b></td><td>525.40 <b>(+73.80%)</b></td><td>227.40 (+2.62%)</td><td>731.54 <b>(+327.13%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>592.00 (n/a)</td><td>382.00 (n/a)</td><td>302.30 (n/a)</td><td>221.60 (n/a)</td><td>171.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.18 <b>(-36.05%)</b></td><td>0.15 <b>(-30.90%)</b></td><td>0.14 <b>(-40.93%)</b></td><td>0.12 (-17.63%)</td><td>0.03 <b>(-61.78%)</b></td><td>639.90 <b>(+21.40%)</b></td><td>503.24 <b>(+34.66%)</b></td><td>518.40 <b>(+69.25%)</b></td><td>407.40 <b>(+56.39%)</b></td><td>94.56 <b>(-30.08%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>527.10 (n/a)</td><td>373.70 (n/a)</td><td>306.30 (n/a)</td><td>260.50 (n/a)</td><td>135.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.15 <b>(-53.05%)</b></td><td>0.12 <b>(-49.05%)</b></td><td>0.12 <b>(-58.41%)</b></td><td>0.07 <b>(-46.62%)</b></td><td>0.03 <b>(-68.04%)</b></td><td>1063.20 <b>(+87.32%)</b></td><td>662.82 <b>(+78.47%)</b></td><td>605.10 <b>(+140.41%)</b></td><td>490.50 <b>(+112.98%)</b></td><td>228.99 <b>(+30.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.29 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>567.60 (n/a)</td><td>371.40 (n/a)</td><td>251.70 (n/a)</td><td>230.30 (n/a)</td><td>175.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.32 (+7.43%)</td><td>0.21 (+5.09%)</td><td>0.15 <b>(-26.91%)</b></td><td>0.15 (+19.72%)</td><td>0.09 (+11.19%)</td><td>499.80 (-16.48%)</td><td>392.70 (-5.49%)</td><td>484.80 <b>(+36.83%)</b></td><td>229.90 (-6.92%)</td><td>136.77 (-16.73%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>598.40 (n/a)</td><td>415.52 (n/a)</td><td>354.30 (n/a)</td><td>247.00 (n/a)</td><td>164.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.48 (-13.16%)</td><td>0.24 <b>(-34.34%)</b></td><td>0.21 <b>(-34.84%)</b></td><td>0.05 <b>(-76.10%)</b></td><td>0.15 (+11.83%)</td><td>2439.40 <b>(+318.42%)</b></td><td>899.78 <b>(+124.65%)</b></td><td>627.10 <b>(+53.48%)</b></td><td>272.80 (+15.15%)</td><td>873.13 <b>(+511.11%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.55 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>583.00 (n/a)</td><td>400.52 (n/a)</td><td>408.60 (n/a)</td><td>236.90 (n/a)</td><td>142.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.49 (-1.10%)</td><td>0.33 (-6.12%)</td><td>0.27 (-5.15%)</td><td>0.24 (+3.95%)</td><td>0.11 (-10.68%)</td><td>549.00 (-3.80%)</td><td>432.16 (+4.98%)</td><td>484.00 (+5.42%)</td><td>269.50 (+1.13%)</td><td>126.99 (-5.86%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>570.70 (n/a)</td><td>411.66 (n/a)</td><td>459.10 (n/a)</td><td>266.50 (n/a)</td><td>134.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.52 <b>(+51.53%)</b></td><td>0.35 (+18.56%)</td><td>0.37 <b>(+35.08%)</b></td><td>0.20 (-16.96%)</td><td>0.14 <b>(+226.67%)</b></td><td>648.20 <b>(+20.44%)</b></td><td>432.66 (-4.80%)</td><td>351.70 <b>(-25.96%)</b></td><td>251.10 <b>(-34.01%)</b></td><td>180.18 <b>(+180.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>538.20 (n/a)</td><td>454.48 (n/a)</td><td>475.00 (n/a)</td><td>380.50 (n/a)</td><td>64.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.00 <b>(-42.86%)</b></td><td>0.00 <b>(-31.58%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-64.08%)</b></td><td>19328.08 (-13.44%)</td><td>15968.12 (+3.17%)</td><td>16896.51 (-19.28%)</td><td>10916.30 <b>(+90.92%)</b></td><td>3220.18 <b>(-61.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22329.93 (n/a)</td><td>15477.94 (n/a)</td><td>20933.44 (n/a)</td><td>5717.79 (n/a)</td><td>8304.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.00 (+18.18%)</td><td>0.00 <b>(+61.11%)</b></td><td>0.00 <b>(+116.67%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.51%)</td><td>14081.45 <b>(-33.58%)</b></td><td>7828.86 <b>(-42.46%)</b></td><td>6287.46 <b>(-55.73%)</b></td><td>6119.72 (-18.77%)</td><td>3497.88 <b>(-41.11%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21199.65 (n/a)</td><td>13604.77 (n/a)</td><td>14204.05 (n/a)</td><td>7534.07 (n/a)</td><td>5939.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>0.14 (+0.88%)</td><td>0.09 (-17.07%)</td><td>0.08 <b>(-31.44%)</b></td><td>0.08 (-5.22%)</td><td>0.02 (+1.48%)</td><td>26241.28 (+5.49%)</td><td>23305.43 <b>(+20.84%)</b></td><td>25221.66 <b>(+45.81%)</b></td><td>15163.43 (-0.85%)</td><td>4639.82 (+3.66%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>24876.33 (n/a)</td><td>19286.40 (n/a)</td><td>17297.26 (n/a)</td><td>15293.44 (n/a)</td><td>4476.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>1.64 (+13.61%)</td><td>1.27 <b>(+26.64%)</b></td><td>1.49 <b>(+67.21%)</b></td><td>0.80 (-3.74%)</td><td>0.38 <b>(+50.55%)</b></td><td>654.90 (+3.89%)</td><td>451.18 (-17.42%)</td><td>352.80 <b>(-40.18%)</b></td><td>319.40 (-11.99%)</td><td>154.32 <b>(+41.56%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>1.44 (n/a)</td><td>1.00 (n/a)</td><td>0.89 (n/a)</td><td>0.83 (n/a)</td><td>0.26 (n/a)</td><td>630.40 (n/a)</td><td>546.34 (n/a)</td><td>589.80 (n/a)</td><td>362.90 (n/a)</td><td>109.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>2.46 (+0.52%)</td><td>1.48 (+12.33%)</td><td>1.25 (-19.35%)</td><td>0.30 (+0.34%)</td><td>0.89 (-9.63%)</td><td>3554.20 (-0.34%)</td><td>1241.76 <b>(-28.66%)</b></td><td>839.20 <b>(+24.00%)</b></td><td>427.00 (-0.51%)</td><td>1311.77 <b>(-20.17%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>2.44 (n/a)</td><td>1.32 (n/a)</td><td>1.55 (n/a)</td><td>0.29 (n/a)</td><td>0.99 (n/a)</td><td>3566.50 (n/a)</td><td>1740.52 (n/a)</td><td>676.80 (n/a)</td><td>429.20 (n/a)</td><td>1643.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:15</td><td>2.03 <b>(+57.70%)</b></td><td>1.39 <b>(+34.11%)</b></td><td>1.48 <b>(+38.91%)</b></td><td>0.75 (-1.45%)</td><td>0.49 <b>(+153.90%)</b></td><td>700.10 (+1.48%)</td><td>423.86 (-18.74%)</td><td>354.00 <b>(-28.00%)</b></td><td>258.80 <b>(-36.58%)</b></td><td>173.06 <b>(+64.55%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>1.28 (n/a)</td><td>1.04 (n/a)</td><td>1.07 (n/a)</td><td>0.76 (n/a)</td><td>0.19 (n/a)</td><td>689.90 (n/a)</td><td>521.62 (n/a)</td><td>491.70 (n/a)</td><td>408.10 (n/a)</td><td>105.17 (n/a)</td>
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
