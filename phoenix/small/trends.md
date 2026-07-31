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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.05 (-15.50%)</td><td>0.04 (-1.93%)</td><td>0.04 (-14.54%)</td><td>0.02 (-0.93%)</td><td>0.01 <b>(-29.65%)</b></td><td>569.20 (+0.94%)</td><td>322.12 (-5.23%)</td><td>275.70 (+17.02%)</td><td>230.00 (+18.37%)</td><td>141.76 (-16.49%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>563.90 (n/a)</td><td>339.88 (n/a)</td><td>235.60 (n/a)</td><td>194.30 (n/a)</td><td>169.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.05 (-5.43%)</td><td>0.04 (-13.01%)</td><td>0.04 (-8.09%)</td><td>0.02 <b>(-34.21%)</b></td><td>0.01 <b>(+57.99%)</b></td><td>575.20 <b>(+52.01%)</b></td><td>369.30 <b>(+22.34%)</b></td><td>300.80 (+8.83%)</td><td>264.40 (+5.76%)</td><td>130.40 <b>(+150.91%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>378.40 (n/a)</td><td>301.86 (n/a)</td><td>276.40 (n/a)</td><td>250.00 (n/a)</td><td>51.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 <b>(-24.11%)</b></td><td>0.02 (+6.70%)</td><td>0.02 (+18.92%)</td><td>0.02 <b>(+136.30%)</b></td><td>0.00 <b>(-73.75%)</b></td><td>578.30 <b>(-57.68%)</b></td><td>526.66 <b>(-24.14%)</b></td><td>542.00 (-15.92%)</td><td>432.60 <b>(+31.77%)</b></td><td>55.19 <b>(-86.23%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1366.60 (n/a)</td><td>694.28 (n/a)</td><td>644.60 (n/a)</td><td>328.30 (n/a)</td><td>400.95 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (-10.00%)</td><td>0.02 <b>(+29.27%)</b></td><td>0.02 <b>(+64.10%)</b></td><td>0.02 <b>(+74.59%)</b></td><td>0.00 <b>(-61.88%)</b></td><td>325.40 <b>(-42.72%)</b></td><td>265.76 <b>(-32.98%)</b></td><td>265.20 <b>(-39.08%)</b></td><td>219.40 (+11.09%)</td><td>38.64 <b>(-75.61%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>396.54 (n/a)</td><td>435.30 (n/a)</td><td>197.50 (n/a)</td><td>158.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (+1.17%)</td><td>0.02 <b>(+23.10%)</b></td><td>0.02 <b>(+41.78%)</b></td><td>0.01 (-0.78%)</td><td>0.00 (+5.40%)</td><td>545.20 (+0.79%)</td><td>371.92 (-18.13%)</td><td>336.90 <b>(-29.46%)</b></td><td>266.90 (-1.18%)</td><td>116.18 (+7.97%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.90 (n/a)</td><td>454.28 (n/a)</td><td>477.60 (n/a)</td><td>270.10 (n/a)</td><td>107.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 <b>(+54.89%)</b></td><td>0.01 <b>(+26.54%)</b></td><td>0.01 <b>(+24.43%)</b></td><td>0.01 (+6.49%)</td><td>0.00 <b>(+240.82%)</b></td><td>518.70 (-6.10%)</td><td>388.18 (-15.57%)</td><td>357.90 (-19.65%)</td><td>263.50 <b>(-35.43%)</b></td><td>120.14 <b>(+112.23%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.40 (n/a)</td><td>459.74 (n/a)</td><td>445.40 (n/a)</td><td>408.10 (n/a)</td><td>56.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 <b>(+45.55%)</b></td><td>0.01 (+3.96%)</td><td>0.01 (+16.05%)</td><td>0.01 (-5.36%)</td><td>0.01 <b>(+55.39%)</b></td><td>623.30 (+5.66%)</td><td>443.00 (+3.20%)</td><td>423.10 (-13.83%)</td><td>188.10 <b>(-31.28%)</b></td><td>169.60 (+15.97%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.90 (n/a)</td><td>429.26 (n/a)</td><td>491.00 (n/a)</td><td>273.70 (n/a)</td><td>146.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (+19.47%)</td><td>0.02 <b>(+59.08%)</b></td><td>0.02 <b>(+100.91%)</b></td><td>0.01 <b>(+57.14%)</b></td><td>0.00 (+5.26%)</td><td>445.40 <b>(-36.36%)</b></td><td>330.24 <b>(-39.14%)</b></td><td>276.10 <b>(-50.23%)</b></td><td>241.60 (-16.29%)</td><td>96.29 <b>(-39.07%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>699.90 (n/a)</td><td>542.60 (n/a)</td><td>554.80 (n/a)</td><td>288.60 (n/a)</td><td>158.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 <b>(+62.25%)</b></td><td>0.02 <b>(+57.83%)</b></td><td>0.02 <b>(+64.46%)</b></td><td>0.01 <b>(+29.11%)</b></td><td>0.00 <b>(+110.03%)</b></td><td>436.90 <b>(-22.55%)</b></td><td>322.68 <b>(-34.93%)</b></td><td>315.50 <b>(-39.19%)</b></td><td>224.80 <b>(-38.36%)</b></td><td>81.11 (+2.14%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.10 (n/a)</td><td>495.88 (n/a)</td><td>518.80 (n/a)</td><td>364.70 (n/a)</td><td>79.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1870.90 (n/a)</td><td>682.86 (n/a)</td><td>521.50 (n/a)</td><td>209.90 (n/a)</td><td>679.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>824.70 (n/a)</td><td>491.80 (n/a)</td><td>429.80 (n/a)</td><td>350.80 (n/a)</td><td>194.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1922.60 (n/a)</td><td>779.02 (n/a)</td><td>572.70 (n/a)</td><td>229.70 (n/a)</td><td>657.35 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>630.90 (n/a)</td><td>435.24 (n/a)</td><td>439.60 (n/a)</td><td>222.20 (n/a)</td><td>153.87 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.30 (n/a)</td><td>402.44 (n/a)</td><td>338.00 (n/a)</td><td>276.30 (n/a)</td><td>148.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.70 (n/a)</td><td>429.32 (n/a)</td><td>409.50 (n/a)</td><td>294.50 (n/a)</td><td>99.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2253.00 (n/a)</td><td>780.82 (n/a)</td><td>526.80 (n/a)</td><td>201.20 (n/a)</td><td>840.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.50 (n/a)</td><td>467.10 (n/a)</td><td>485.80 (n/a)</td><td>308.90 (n/a)</td><td>127.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.70 (n/a)</td><td>430.00 (n/a)</td><td>433.30 (n/a)</td><td>268.90 (n/a)</td><td>147.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.80 (n/a)</td><td>487.50 (n/a)</td><td>462.60 (n/a)</td><td>229.40 (n/a)</td><td>172.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.10 (n/a)</td><td>415.76 (n/a)</td><td>382.70 (n/a)</td><td>263.40 (n/a)</td><td>118.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.40 (n/a)</td><td>444.86 (n/a)</td><td>334.20 (n/a)</td><td>307.20 (n/a)</td><td>172.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.82 <b>(+74.10%)</b></td><td>0.34 (+0.25%)</td><td>0.25 <b>(-24.43%)</b></td><td>0.12 (-3.80%)</td><td>0.29 <b>(+114.78%)</b></td><td>1884.10 (+3.95%)</td><td>1069.00 <b>(+29.50%)</b></td><td>877.60 <b>(+32.33%)</b></td><td>268.60 <b>(-42.55%)</b></td><td>704.30 <b>(+26.05%)</b></td><td>35.14 <b>(+74.10%)</b></td><td>14.44 (+0.25%)</td><td>10.75 <b>(-24.43%)</b></td><td>5.01 (-3.80%)</td><td>12.38 <b>(+114.78%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1812.50 (n/a)</td><td>825.48 (n/a)</td><td>663.20 (n/a)</td><td>467.50 (n/a)</td><td>558.76 (n/a)</td><td>20.18 (n/a)</td><td>14.40 (n/a)</td><td>14.23 (n/a)</td><td>5.21 (n/a)</td><td>5.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.63 (-8.56%)</td><td>0.46 (+19.11%)</td><td>0.47 <b>(+31.57%)</b></td><td>0.33 <b>(+87.46%)</b></td><td>0.12 <b>(-37.47%)</b></td><td>665.40 <b>(-46.65%)</b></td><td>508.40 <b>(-26.46%)</b></td><td>466.90 <b>(-23.99%)</b></td><td>351.90 (+9.39%)</td><td>124.89 <b>(-63.12%)</b></td><td>26.82 (-8.56%)</td><td>19.52 (+19.11%)</td><td>20.21 <b>(+31.57%)</b></td><td>14.18 <b>(+87.46%)</b></td><td>4.96 <b>(-37.47%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.69 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>1247.30 (n/a)</td><td>691.36 (n/a)</td><td>614.30 (n/a)</td><td>321.70 (n/a)</td><td>338.62 (n/a)</td><td>29.33 (n/a)</td><td>16.39 (n/a)</td><td>15.36 (n/a)</td><td>7.57 (n/a)</td><td>7.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.31 (-1.66%)</td><td>0.30 (-1.65%)</td><td>0.30 (-3.24%)</td><td>0.30 (+0.09%)</td><td>0.00 <b>(-43.20%)</b></td><td>84666.20 (-0.09%)</td><td>83367.74 (+1.65%)</td><td>83688.50 (+3.34%)</td><td>81885.80 (+1.68%)</td><td>1042.58 <b>(-42.29%)</b></td><td>209.80 (-1.66%)</td><td>206.10 (-1.65%)</td><td>205.28 (-3.24%)</td><td>202.91 (+0.09%)</td><td>2.59 <b>(-43.20%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84742.00 (n/a)</td><td>82012.86 (n/a)</td><td>80980.30 (n/a)</td><td>80529.20 (n/a)</td><td>1806.57 (n/a)</td><td>213.34 (n/a)</td><td>209.56 (n/a)</td><td>212.15 (n/a)</td><td>202.73 (n/a)</td><td>4.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>1.03 (-0.35%)</td><td>0.99 (-1.66%)</td><td>1.00 (-0.99%)</td><td>0.94 (-4.07%)</td><td>0.04 <b>(+54.39%)</b></td><td>26904.20 (+4.25%)</td><td>25333.66 (+1.75%)</td><td>25113.10 (+1.00%)</td><td>24432.70 (+0.35%)</td><td>929.67 <b>(+62.68%)</b></td><td>703.15 (-0.35%)</td><td>678.85 (-1.66%)</td><td>684.10 (-0.99%)</td><td>638.56 (-4.07%)</td><td>24.09 <b>(+54.39%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25808.10 (n/a)</td><td>24897.86 (n/a)</td><td>24864.60 (n/a)</td><td>24346.50 (n/a)</td><td>571.48 (n/a)</td><td>705.64 (n/a)</td><td>690.30 (n/a)</td><td>690.94 (n/a)</td><td>665.68 (n/a)</td><td>15.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>3.31 (-2.64%)</td><td>2.58 <b>(+23.34%)</b></td><td>3.16 <b>(+69.28%)</b></td><td>1.55 (+12.93%)</td><td>0.90 (+16.42%)</td><td>5199.60 (-11.45%)</td><td>3515.62 (-16.53%)</td><td>2550.40 <b>(-40.92%)</b></td><td>2437.60 (+2.71%)</td><td>1407.09 (+10.92%)</td><td>867.21 (-2.64%)</td><td>676.81 <b>(+23.34%)</b></td><td>828.88 <b>(+69.28%)</b></td><td>406.55 (+12.93%)</td><td>236.10 (+16.42%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>3.40 (n/a)</td><td>2.09 (n/a)</td><td>1.87 (n/a)</td><td>1.37 (n/a)</td><td>0.77 (n/a)</td><td>5872.20 (n/a)</td><td>4211.72 (n/a)</td><td>4317.10 (n/a)</td><td>2373.20 (n/a)</td><td>1268.53 (n/a)</td><td>890.75 (n/a)</td><td>548.72 (n/a)</td><td>489.66 (n/a)</td><td>359.99 (n/a)</td><td>202.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.21 (-15.34%)</td><td>0.18 (-12.62%)</td><td>0.17 (-13.38%)</td><td>0.15 (-0.17%)</td><td>0.03 <b>(-40.75%)</b></td><td>8149.80 (+0.17%)</td><td>7206.60 (+12.10%)</td><td>7495.40 (+15.44%)</td><td>5866.30 (+18.12%)</td><td>978.39 <b>(-28.03%)</b></td><td>11.44 (-15.34%)</td><td>9.46 (-12.62%)</td><td>8.95 (-13.38%)</td><td>8.23 (-0.17%)</td><td>1.36 <b>(-40.75%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>8135.70 (n/a)</td><td>6428.68 (n/a)</td><td>6492.90 (n/a)</td><td>4966.40 (n/a)</td><td>1359.46 (n/a)</td><td>13.51 (n/a)</td><td>10.83 (n/a)</td><td>10.34 (n/a)</td><td>8.25 (n/a)</td><td>2.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>3.81 (n/a)</td><td>3.61 (n/a)</td><td>3.73 (n/a)</td><td>3.37 (n/a)</td><td>0.20 (n/a)</td><td>3.81 (n/a)</td><td>3.61 (n/a)</td><td>3.72 (n/a)</td><td>3.37 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>6.84 (-6.61%)</td><td>6.26 (-1.28%)</td><td>6.42 (+6.08%)</td><td>5.48 (-3.34%)</td><td>0.57 <b>(-26.64%)</b></td><td>6.83 (-6.61%)</td><td>6.26 (-1.28%)</td><td>6.42 (+6.08%)</td><td>5.48 (-3.34%)</td><td>0.56 <b>(-26.64%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>7.32 (n/a)</td><td>6.34 (n/a)</td><td>6.05 (n/a)</td><td>5.67 (n/a)</td><td>0.77 (n/a)</td><td>7.32 (n/a)</td><td>6.34 (n/a)</td><td>6.05 (n/a)</td><td>5.67 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>14.07 (+7.41%)</td><td>11.63 <b>(+29.92%)</b></td><td>12.90 <b>(+59.24%)</b></td><td>7.39 (-0.43%)</td><td>2.86 <b>(+22.08%)</b></td><td>14.06 (+7.41%)</td><td>11.62 <b>(+29.92%)</b></td><td>12.89 <b>(+59.24%)</b></td><td>7.39 (-0.43%)</td><td>2.86 <b>(+22.08%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>13.10 (n/a)</td><td>8.95 (n/a)</td><td>8.10 (n/a)</td><td>7.43 (n/a)</td><td>2.34 (n/a)</td><td>13.09 (n/a)</td><td>8.94 (n/a)</td><td>8.10 (n/a)</td><td>7.42 (n/a)</td><td>2.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>3.90 (n/a)</td><td>3.80 (n/a)</td><td>3.86 (n/a)</td><td>3.59 (n/a)</td><td>0.12 (n/a)</td><td>3.90 (n/a)</td><td>3.80 (n/a)</td><td>3.86 (n/a)</td><td>3.59 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>7.54 (+4.25%)</td><td>6.64 (+1.19%)</td><td>6.73 (-4.00%)</td><td>5.58 (-0.79%)</td><td>0.70 (-5.55%)</td><td>7.53 (+4.25%)</td><td>6.64 (+1.19%)</td><td>6.73 (-4.00%)</td><td>5.58 (-0.79%)</td><td>0.70 (-5.55%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>7.23 (n/a)</td><td>6.57 (n/a)</td><td>7.01 (n/a)</td><td>5.63 (n/a)</td><td>0.74 (n/a)</td><td>7.23 (n/a)</td><td>6.56 (n/a)</td><td>7.01 (n/a)</td><td>5.62 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>13.78 (-2.32%)</td><td>9.98 (-17.93%)</td><td>9.24 <b>(-31.01%)</b></td><td>8.31 (+11.14%)</td><td>2.25 (-16.05%)</td><td>13.77 (-2.32%)</td><td>9.98 (-17.93%)</td><td>9.23 <b>(-31.01%)</b></td><td>8.31 (+11.14%)</td><td>2.25 (-16.05%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>14.11 (n/a)</td><td>12.17 (n/a)</td><td>13.39 (n/a)</td><td>7.48 (n/a)</td><td>2.68 (n/a)</td><td>14.10 (n/a)</td><td>12.16 (n/a)</td><td>13.38 (n/a)</td><td>7.48 (n/a)</td><td>2.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>3.20 (+9.73%)</td><td>2.87 <b>(+37.85%)</b></td><td>2.85 (+3.94%)</td><td>2.43 <b>(+145.43%)</b></td><td>0.30 <b>(-69.46%)</b></td><td>3.19 (+9.73%)</td><td>2.87 <b>(+37.85%)</b></td><td>2.84 (+3.94%)</td><td>2.43 <b>(+145.43%)</b></td><td>0.30 <b>(-69.46%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.91 (n/a)</td><td>2.09 (n/a)</td><td>2.74 (n/a)</td><td>0.99 (n/a)</td><td>0.98 (n/a)</td><td>2.91 (n/a)</td><td>2.08 (n/a)</td><td>2.74 (n/a)</td><td>0.99 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.53 (+5.98%)</td><td>0.25 <b>(-40.17%)</b></td><td>0.27 <b>(-42.61%)</b></td><td>0.08 <b>(-77.31%)</b></td><td>0.19 <b>(+148.98%)</b></td><td>0.52 (+5.98%)</td><td>0.25 <b>(-40.17%)</b></td><td>0.26 <b>(-42.61%)</b></td><td>0.08 <b>(-77.31%)</b></td><td>0.18 <b>(+148.98%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.64 (+6.46%)</td><td>0.42 <b>(+24.22%)</b></td><td>0.37 (+0.64%)</td><td>0.35 <b>(+359.99%)</b></td><td>0.12 <b>(-47.22%)</b></td><td>0.63 (+6.46%)</td><td>0.42 <b>(+24.22%)</b></td><td>0.37 (+0.64%)</td><td>0.34 <b>(+359.99%)</b></td><td>0.12 <b>(-47.22%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.60 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>0.23 (n/a)</td><td>0.59 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>2.37 (-0.84%)</td><td>1.21 (-18.89%)</td><td>0.81 <b>(-55.78%)</b></td><td>0.46 (-9.06%)</td><td>0.82 (-0.05%)</td><td>2.33 (-0.84%)</td><td>1.19 (-18.89%)</td><td>0.80 <b>(-55.78%)</b></td><td>0.45 (-9.06%)</td><td>0.81 (-0.05%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.39 (n/a)</td><td>1.49 (n/a)</td><td>1.83 (n/a)</td><td>0.50 (n/a)</td><td>0.82 (n/a)</td><td>2.35 (n/a)</td><td>1.47 (n/a)</td><td>1.80 (n/a)</td><td>0.49 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.80 (n/a)</td><td>405.64 (n/a)</td><td>412.60 (n/a)</td><td>249.50 (n/a)</td><td>127.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>430.98 (n/a)</td><td>425.30 (n/a)</td><td>228.40 (n/a)</td><td>142.54 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.10 (n/a)</td><td>535.86 (n/a)</td><td>594.70 (n/a)</td><td>276.10 (n/a)</td><td>145.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.70 (n/a)</td><td>422.70 (n/a)</td><td>515.10 (n/a)</td><td>256.00 (n/a)</td><td>134.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.10 (n/a)</td><td>453.20 (n/a)</td><td>434.90 (n/a)</td><td>290.00 (n/a)</td><td>125.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.20 (n/a)</td><td>422.94 (n/a)</td><td>451.00 (n/a)</td><td>279.90 (n/a)</td><td>125.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-19.71%)</td><td>0.02 <b>(-26.54%)</b></td><td>0.02 <b>(-39.36%)</b></td><td>0.01 (-9.98%)</td><td>0.01 <b>(-43.13%)</b></td><td>627.30 (+11.09%)</td><td>441.40 <b>(+26.24%)</b></td><td>410.50 <b>(+64.86%)</b></td><td>287.40 <b>(+24.58%)</b></td><td>126.66 (-18.56%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.70 (n/a)</td><td>349.64 (n/a)</td><td>249.00 (n/a)</td><td>230.70 (n/a)</td><td>155.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (+10.61%)</td><td>0.03 (+18.30%)</td><td>0.03 <b>(+70.10%)</b></td><td>0.02 (+12.50%)</td><td>0.01 (+1.59%)</td><td>514.30 (-11.11%)</td><td>349.12 (-16.45%)</td><td>283.30 <b>(-41.21%)</b></td><td>233.10 (-9.62%)</td><td>132.60 (-11.45%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.60 (n/a)</td><td>417.84 (n/a)</td><td>481.90 (n/a)</td><td>257.90 (n/a)</td><td>149.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 <b>(-20.55%)</b></td><td>0.02 (-17.06%)</td><td>0.03 (-2.09%)</td><td>0.00 <b>(-74.13%)</b></td><td>0.01 <b>(+25.96%)</b></td><td>2047.90 <b>(+286.54%)</b></td><td>685.28 <b>(+89.47%)</b></td><td>304.90 (+2.11%)</td><td>289.20 <b>(+25.90%)</b></td><td>765.79 <b>(+507.37%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.80 (n/a)</td><td>361.68 (n/a)</td><td>298.60 (n/a)</td><td>229.70 (n/a)</td><td>126.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-8.77%)</td><td>0.02 <b>(-23.52%)</b></td><td>0.03 (-13.27%)</td><td>0.02 <b>(-47.02%)</b></td><td>0.01 <b>(+263.49%)</b></td><td>518.80 <b>(+88.72%)</b></td><td>358.74 <b>(+42.23%)</b></td><td>290.80 (+15.31%)</td><td>252.40 (+9.60%)</td><td>123.04 <b>(+657.02%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>274.90 (n/a)</td><td>252.22 (n/a)</td><td>252.20 (n/a)</td><td>230.30 (n/a)</td><td>16.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (+4.25%)</td><td>0.02 <b>(-26.62%)</b></td><td>0.02 <b>(-38.38%)</b></td><td>0.01 (-5.10%)</td><td>0.01 (+10.57%)</td><td>562.40 (+5.38%)</td><td>458.14 <b>(+37.62%)</b></td><td>459.60 <b>(+62.29%)</b></td><td>263.80 (-4.07%)</td><td>119.55 (+6.34%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>332.90 (n/a)</td><td>283.20 (n/a)</td><td>275.00 (n/a)</td><td>112.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 <b>(-34.67%)</b></td><td>0.02 (-6.16%)</td><td>0.02 (-0.38%)</td><td>0.01 <b>(+37.58%)</b></td><td>0.00 <b>(-64.63%)</b></td><td>585.50 <b>(-27.31%)</b></td><td>486.64 (-5.87%)</td><td>504.80 (+0.40%)</td><td>371.30 <b>(+53.05%)</b></td><td>83.38 <b>(-58.31%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>805.50 (n/a)</td><td>516.98 (n/a)</td><td>502.80 (n/a)</td><td>242.60 (n/a)</td><td>199.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (+2.08%)</td><td>0.02 (-8.77%)</td><td>0.02 <b>(+25.55%)</b></td><td>0.00 <b>(-70.54%)</b></td><td>0.01 <b>(+27.38%)</b></td><td>2048.80 <b>(+239.49%)</b></td><td>724.46 <b>(+65.28%)</b></td><td>415.60 <b>(-20.35%)</b></td><td>228.90 (-2.05%)</td><td>751.26 <b>(+374.35%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.50 (n/a)</td><td>438.32 (n/a)</td><td>521.80 (n/a)</td><td>233.70 (n/a)</td><td>158.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-3.74%)</td><td>0.02 (-7.74%)</td><td>0.01 <b>(-20.82%)</b></td><td>0.01 (-2.35%)</td><td>0.01 (+3.38%)</td><td>620.30 (+2.41%)</td><td>518.58 (+10.15%)</td><td>609.20 <b>(+26.29%)</b></td><td>283.00 (+3.89%)</td><td>145.98 (+17.68%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.70 (n/a)</td><td>470.80 (n/a)</td><td>482.40 (n/a)</td><td>272.40 (n/a)</td><td>124.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 <b>(-21.03%)</b></td><td>0.02 <b>(-20.64%)</b></td><td>0.02 <b>(-32.51%)</b></td><td>0.01 <b>(+64.20%)</b></td><td>0.01 <b>(-42.82%)</b></td><td>659.80 <b>(-39.10%)</b></td><td>513.96 (+0.60%)</td><td>501.00 <b>(+48.18%)</b></td><td>284.00 <b>(+26.62%)</b></td><td>147.39 <b>(-58.31%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1083.40 (n/a)</td><td>510.92 (n/a)</td><td>338.10 (n/a)</td><td>224.30 (n/a)</td><td>353.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-5.53%)</td><td>0.02 (-0.71%)</td><td>0.02 (+8.28%)</td><td>0.01 (-4.30%)</td><td>0.01 (+8.85%)</td><td>590.90 (+4.47%)</td><td>392.70 (+3.49%)</td><td>336.20 (-7.64%)</td><td>254.30 (+5.87%)</td><td>152.57 (+19.50%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>379.44 (n/a)</td><td>364.00 (n/a)</td><td>240.20 (n/a)</td><td>127.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-5.52%)</td><td>0.02 (-17.45%)</td><td>0.02 <b>(-31.98%)</b></td><td>0.01 <b>(-22.81%)</b></td><td>0.01 <b>(+44.42%)</b></td><td>590.50 <b>(+29.55%)</b></td><td>423.64 <b>(+32.04%)</b></td><td>425.40 <b>(+46.99%)</b></td><td>255.00 (+5.85%)</td><td>166.86 <b>(+93.53%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.80 (n/a)</td><td>320.84 (n/a)</td><td>289.40 (n/a)</td><td>240.90 (n/a)</td><td>86.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 <b>(-32.93%)</b></td><td>0.02 <b>(-30.54%)</b></td><td>0.02 <b>(-39.83%)</b></td><td>0.01 <b>(-20.73%)</b></td><td>0.00 <b>(-43.08%)</b></td><td>639.30 <b>(+26.17%)</b></td><td>500.36 <b>(+40.22%)</b></td><td>524.10 <b>(+66.17%)</b></td><td>360.40 <b>(+49.11%)</b></td><td>109.00 (+3.80%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.70 (n/a)</td><td>356.84 (n/a)</td><td>315.40 (n/a)</td><td>241.70 (n/a)</td><td>105.02 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-13.69%)</td><td>0.02 (-13.38%)</td><td>0.02 (-8.51%)</td><td>0.01 <b>(-30.73%)</b></td><td>0.01 (-2.63%)</td><td>651.60 <b>(+44.38%)</b></td><td>432.52 <b>(+20.62%)</b></td><td>450.80 (+9.31%)</td><td>235.00 (+15.88%)</td><td>167.81 <b>(+58.27%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>451.30 (n/a)</td><td>358.58 (n/a)</td><td>412.40 (n/a)</td><td>202.80 (n/a)</td><td>106.03 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-2.06%)</td><td>0.02 (-9.26%)</td><td>0.02 (-1.15%)</td><td>0.01 (-7.02%)</td><td>0.01 (-10.24%)</td><td>680.40 (+7.56%)</td><td>526.68 (+8.68%)</td><td>532.80 (+1.18%)</td><td>310.20 (+2.11%)</td><td>142.64 (-5.29%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.60 (n/a)</td><td>484.60 (n/a)</td><td>526.60 (n/a)</td><td>303.80 (n/a)</td><td>150.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-5.47%)</td><td>0.02 (+4.57%)</td><td>0.03 <b>(+21.73%)</b></td><td>0.01 (+13.55%)</td><td>0.01 (-11.30%)</td><td>560.80 (-11.93%)</td><td>377.16 (-7.33%)</td><td>289.40 (-17.85%)</td><td>261.50 (+5.78%)</td><td>139.68 (-17.02%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.80 (n/a)</td><td>406.98 (n/a)</td><td>352.30 (n/a)</td><td>247.20 (n/a)</td><td>168.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 <b>(-29.41%)</b></td><td>0.03 (-12.78%)</td><td>0.03 <b>(+44.80%)</b></td><td>0.02 (-19.46%)</td><td>0.01 <b>(-38.89%)</b></td><td>701.20 <b>(+24.17%)</b></td><td>475.58 (+9.08%)</td><td>375.20 <b>(-30.95%)</b></td><td>338.60 <b>(+41.67%)</b></td><td>166.57 (+2.68%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.70 (n/a)</td><td>435.98 (n/a)</td><td>543.40 (n/a)</td><td>239.00 (n/a)</td><td>162.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-2.93%)</td><td>0.02 (-2.48%)</td><td>0.02 <b>(-30.18%)</b></td><td>0.01 <b>(+66.25%)</b></td><td>0.01 <b>(-26.06%)</b></td><td>620.90 <b>(-39.85%)</b></td><td>417.32 (-15.32%)</td><td>403.80 <b>(+43.24%)</b></td><td>251.80 (+3.03%)</td><td>158.75 <b>(-53.49%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1032.30 (n/a)</td><td>492.82 (n/a)</td><td>281.90 (n/a)</td><td>244.40 (n/a)</td><td>341.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (+18.48%)</td><td>0.02 (+8.23%)</td><td>0.02 (-19.63%)</td><td>0.02 <b>(+295.39%)</b></td><td>0.01 (-16.88%)</td><td>606.90 <b>(-74.71%)</b></td><td>472.74 <b>(-41.03%)</b></td><td>517.50 <b>(+24.43%)</b></td><td>261.00 (-15.59%)</td><td>140.13 <b>(-84.37%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2399.80 (n/a)</td><td>801.70 (n/a)</td><td>415.90 (n/a)</td><td>309.20 (n/a)</td><td>896.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 <b>(+34.15%)</b></td><td>0.03 <b>(+44.73%)</b></td><td>0.03 <b>(+50.79%)</b></td><td>0.02 <b>(+41.21%)</b></td><td>0.01 <b>(+24.27%)</b></td><td>405.70 <b>(-29.18%)</b></td><td>313.66 <b>(-31.62%)</b></td><td>308.20 <b>(-33.69%)</b></td><td>205.50 <b>(-25.44%)</b></td><td>77.41 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.90 (n/a)</td><td>458.72 (n/a)</td><td>464.80 (n/a)</td><td>275.60 (n/a)</td><td>114.66 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.04 (+2.19%)</td><td>0.03 (+3.63%)</td><td>0.03 (+0.06%)</td><td>0.02 (-10.70%)</td><td>0.01 (+3.00%)</td><td>536.20 (+11.99%)</td><td>350.62 (-2.70%)</td><td>303.40 (-0.07%)</td><td>274.10 (-2.14%)</td><td>108.28 (+14.49%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.80 (n/a)</td><td>360.34 (n/a)</td><td>303.60 (n/a)</td><td>280.10 (n/a)</td><td>94.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 <b>(+33.95%)</b></td><td>0.02 (+13.39%)</td><td>0.02 (-6.79%)</td><td>0.01 <b>(+196.98%)</b></td><td>0.01 (-3.75%)</td><td>665.70 <b>(-66.33%)</b></td><td>477.00 <b>(-34.79%)</b></td><td>481.60 (+7.28%)</td><td>269.40 <b>(-25.33%)</b></td><td>144.64 <b>(-79.26%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1977.00 (n/a)</td><td>731.48 (n/a)</td><td>448.90 (n/a)</td><td>360.80 (n/a)</td><td>697.31 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.05 <b>(+52.49%)</b></td><td>0.02 (+7.50%)</td><td>0.02 <b>(-22.34%)</b></td><td>0.02 (+7.34%)</td><td>0.01 <b>(+81.02%)</b></td><td>593.80 (-6.84%)</td><td>453.66 (-1.07%)</td><td>487.30 <b>(+28.78%)</b></td><td>194.90 <b>(-34.40%)</b></td><td>151.47 (-5.96%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.40 (n/a)</td><td>458.58 (n/a)</td><td>378.40 (n/a)</td><td>297.10 (n/a)</td><td>161.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-6.77%)</td><td>0.02 (-5.45%)</td><td>0.02 (-12.78%)</td><td>0.01 <b>(+72.05%)</b></td><td>0.01 <b>(-21.43%)</b></td><td>615.30 <b>(-41.88%)</b></td><td>493.92 (-7.16%)</td><td>537.30 (+14.66%)</td><td>263.20 (+7.25%)</td><td>143.37 <b>(-54.11%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1058.60 (n/a)</td><td>532.02 (n/a)</td><td>468.60 (n/a)</td><td>245.40 (n/a)</td><td>312.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.03 (-5.53%)</td><td>0.02 (+12.32%)</td><td>0.02 <b>(+24.40%)</b></td><td>0.01 <b>(+228.03%)</b></td><td>0.01 <b>(-37.01%)</b></td><td>618.90 <b>(-69.52%)</b></td><td>440.98 <b>(-40.09%)</b></td><td>373.60 (-19.60%)</td><td>292.20 (+5.87%)</td><td>139.02 <b>(-81.00%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2030.30 (n/a)</td><td>736.12 (n/a)</td><td>464.70 (n/a)</td><td>276.00 (n/a)</td><td>731.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.02 (-11.09%)</td><td>0.02 (-12.94%)</td><td>0.02 (-0.47%)</td><td>0.01 <b>(-37.99%)</b></td><td>0.01 (+2.58%)</td><td>975.30 <b>(+61.26%)</b></td><td>566.66 <b>(+22.07%)</b></td><td>493.50 (+0.47%)</td><td>342.20 (+12.49%)</td><td>255.15 <b>(+85.53%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.80 (n/a)</td><td>464.20 (n/a)</td><td>491.20 (n/a)</td><td>304.20 (n/a)</td><td>137.52 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.38 (-5.89%)</td><td>0.28 (+16.82%)</td><td>0.32 <b>(+88.43%)</b></td><td>0.19 <b>(+32.72%)</b></td><td>0.08 <b>(-32.72%)</b></td><td>508.80 <b>(-24.66%)</b></td><td>372.56 <b>(-23.39%)</b></td><td>306.10 <b>(-46.92%)</b></td><td>260.80 (+6.23%)</td><td>115.67 <b>(-44.04%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.40 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>675.30 (n/a)</td><td>486.30 (n/a)</td><td>576.70 (n/a)</td><td>245.50 (n/a)</td><td>206.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.37 (-7.28%)</td><td>0.28 <b>(+25.46%)</b></td><td>0.31 <b>(+31.41%)</b></td><td>0.16 <b>(+249.13%)</b></td><td>0.09 <b>(-27.71%)</b></td><td>599.10 <b>(-71.36%)</b></td><td>390.58 <b>(-47.42%)</b></td><td>314.40 <b>(-23.89%)</b></td><td>263.00 (+7.83%)</td><td>150.29 <b>(-80.34%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>2091.60 (n/a)</td><td>742.82 (n/a)</td><td>413.10 (n/a)</td><td>243.90 (n/a)</td><td>764.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.30 <b>(-20.71%)</b></td><td>0.22 <b>(-20.42%)</b></td><td>0.21 <b>(-30.78%)</b></td><td>0.15 (+8.63%)</td><td>0.06 <b>(-43.09%)</b></td><td>641.40 (-7.95%)</td><td>480.18 (+16.01%)</td><td>464.70 <b>(+44.45%)</b></td><td>331.70 <b>(+26.12%)</b></td><td>120.49 <b>(-33.86%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.31 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>696.80 (n/a)</td><td>413.90 (n/a)</td><td>321.70 (n/a)</td><td>263.00 (n/a)</td><td>182.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.29 <b>(+23.62%)</b></td><td>0.21 (+17.57%)</td><td>0.24 <b>(+49.80%)</b></td><td>0.12 (-18.51%)</td><td>0.08 <b>(+94.80%)</b></td><td>625.20 <b>(+22.71%)</b></td><td>397.28 (-6.98%)</td><td>311.00 <b>(-33.23%)</b></td><td>250.00 (-19.12%)</td><td>162.86 <b>(+97.48%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>509.50 (n/a)</td><td>427.10 (n/a)</td><td>465.80 (n/a)</td><td>309.10 (n/a)</td><td>82.47 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.15 <b>(-51.64%)</b></td><td>0.12 <b>(-48.05%)</b></td><td>0.12 <b>(-51.11%)</b></td><td>0.06 <b>(-58.55%)</b></td><td>0.04 <b>(-47.60%)</b></td><td>1330.70 <b>(+141.24%)</b></td><td>708.80 <b>(+99.75%)</b></td><td>594.10 <b>(+104.51%)</b></td><td>495.60 <b>(+106.76%)</b></td><td>351.76 <b>(+170.53%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>551.60 (n/a)</td><td>354.84 (n/a)</td><td>290.50 (n/a)</td><td>239.70 (n/a)</td><td>130.03 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.31 (+10.83%)</td><td>0.17 (-9.20%)</td><td>0.14 (-18.70%)</td><td>0.13 (-2.22%)</td><td>0.08 <b>(+27.13%)</b></td><td>588.60 (+2.26%)</td><td>485.46 (+13.76%)</td><td>540.20 <b>(+23.00%)</b></td><td>239.70 (-9.79%)</td><td>140.29 (+11.38%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>575.60 (n/a)</td><td>426.74 (n/a)</td><td>439.20 (n/a)</td><td>265.70 (n/a)</td><td>125.95 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.26 <b>(-39.07%)</b></td><td>0.21 <b>(-33.28%)</b></td><td>0.23 <b>(-20.87%)</b></td><td>0.12 <b>(-43.18%)</b></td><td>0.05 <b>(-43.41%)</b></td><td>1052.70 <b>(+76.01%)</b></td><td>657.86 <b>(+49.95%)</b></td><td>571.10 <b>(+26.38%)</b></td><td>511.10 <b>(+64.13%)</b></td><td>226.06 <b>(+77.87%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>598.10 (n/a)</td><td>438.72 (n/a)</td><td>451.90 (n/a)</td><td>311.40 (n/a)</td><td>127.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.45 (-1.54%)</td><td>0.25 <b>(-41.81%)</b></td><td>0.25 <b>(-43.35%)</b></td><td>0.07 <b>(-78.95%)</b></td><td>0.14 <b>(+180.64%)</b></td><td>1874.40 <b>(+375.13%)</b></td><td>790.66 <b>(+150.73%)</b></td><td>518.70 <b>(+76.55%)</b></td><td>290.90 (+1.54%)</td><td>636.05 <b>(+1314.82%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.46 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>394.50 (n/a)</td><td>315.34 (n/a)</td><td>293.80 (n/a)</td><td>286.50 (n/a)</td><td>44.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.50 (+18.13%)</td><td>0.32 (-4.26%)</td><td>0.30 <b>(-21.49%)</b></td><td>0.21 (-5.63%)</td><td>0.12 <b>(+26.23%)</b></td><td>632.30 (+5.97%)</td><td>461.70 (+7.76%)</td><td>444.00 <b>(+27.37%)</b></td><td>262.60 (-15.34%)</td><td>159.75 (+16.16%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.38 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>596.70 (n/a)</td><td>428.46 (n/a)</td><td>348.60 (n/a)</td><td>310.20 (n/a)</td><td>137.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+26.67%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+25.17%)</b></td><td>22259.61 (+2.52%)</td><td>14112.98 (-12.58%)</td><td>15688.28 (-7.89%)</td><td>5715.50 (-14.52%)</td><td>7119.30 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21712.14 (n/a)</td><td>16144.40 (n/a)</td><td>17033.02 (n/a)</td><td>6686.30 (n/a)</td><td>5703.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.79%)</b></td><td>0.00 <b>(-44.44%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 <b>(+22.94%)</b></td><td>23137.13 <b>(+28.13%)</b></td><td>15264.12 <b>(+53.99%)</b></td><td>15574.33 <b>(+80.34%)</b></td><td>6465.86 (-1.06%)</td><td>5945.61 <b>(+27.91%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18057.08 (n/a)</td><td>9912.12 (n/a)</td><td>8636.04 (n/a)</td><td>6534.86 (n/a)</td><td>4648.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>0.15 (+3.01%)</td><td>0.09 (-14.05%)</td><td>0.07 (-18.00%)</td><td>0.07 (+2.89%)</td><td>0.03 (-2.65%)</td><td>29487.39 (-2.78%)</td><td>25227.76 (+15.69%)</td><td>28429.38 <b>(+21.98%)</b></td><td>14268.63 (-2.90%)</td><td>6313.81 (-5.78%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30330.61 (n/a)</td><td>21806.08 (n/a)</td><td>23305.98 (n/a)</td><td>14694.18 (n/a)</td><td>6701.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>1.69 (+5.66%)</td><td>1.61 <b>(+33.63%)</b></td><td>1.65 <b>(+26.52%)</b></td><td>1.42 <b>(+125.94%)</b></td><td>0.11 <b>(-73.05%)</b></td><td>370.20 <b>(-55.74%)</b></td><td>326.84 <b>(-33.63%)</b></td><td>318.30 <b>(-20.98%)</b></td><td>310.10 (-5.37%)</td><td>24.88 <b>(-88.36%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>1.60 (n/a)</td><td>1.21 (n/a)</td><td>1.30 (n/a)</td><td>0.63 (n/a)</td><td>0.42 (n/a)</td><td>836.40 (n/a)</td><td>492.46 (n/a)</td><td>402.80 (n/a)</td><td>327.70 (n/a)</td><td>213.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>2.59 (-7.81%)</td><td>1.98 <b>(+37.43%)</b></td><td>2.43 <b>(+94.34%)</b></td><td>1.10 <b>(+263.00%)</b></td><td>0.72 <b>(-21.00%)</b></td><td>957.30 <b>(-72.45%)</b></td><td>604.06 <b>(-51.22%)</b></td><td>431.80 <b>(-48.54%)</b></td><td>404.50 (+8.47%)</td><td>257.51 <b>(-79.64%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.81 (n/a)</td><td>1.44 (n/a)</td><td>1.25 (n/a)</td><td>0.30 (n/a)</td><td>0.91 (n/a)</td><td>3475.00 (n/a)</td><td>1238.24 (n/a)</td><td>839.10 (n/a)</td><td>372.90 (n/a)</td><td>1265.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:18:22</td><td>1.98 (-8.30%)</td><td>1.42 (-0.69%)</td><td>1.47 (+4.57%)</td><td>0.95 (+6.00%)</td><td>0.45 (-5.53%)</td><td>551.20 (-5.65%)</td><td>402.26 (+0.63%)</td><td>357.20 (-4.36%)</td><td>264.90 (+9.06%)</td><td>132.59 (+2.12%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.16 (n/a)</td><td>1.43 (n/a)</td><td>1.40 (n/a)</td><td>0.90 (n/a)</td><td>0.48 (n/a)</td><td>584.20 (n/a)</td><td>399.76 (n/a)</td><td>373.50 (n/a)</td><td>242.90 (n/a)</td><td>129.84 (n/a)</td>
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
