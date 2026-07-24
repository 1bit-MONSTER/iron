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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (-5.74%)</td><td>0.04 (-3.47%)</td><td>0.03 <b>(-21.92%)</b></td><td>0.03 <b>(+25.57%)</b></td><td>0.01 <b>(-32.81%)</b></td><td>463.30 <b>(-20.35%)</b></td><td>370.00 (-6.12%)</td><td>396.70 <b>(+28.05%)</b></td><td>237.70 (+6.12%)</td><td>87.30 <b>(-49.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.70 (n/a)</td><td>394.14 (n/a)</td><td>309.80 (n/a)</td><td>224.00 (n/a)</td><td>173.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (+18.18%)</td><td>0.04 <b>(+41.15%)</b></td><td>0.04 <b>(+66.23%)</b></td><td>0.03 <b>(+52.40%)</b></td><td>0.01 (+1.53%)</td><td>414.70 <b>(-34.38%)</b></td><td>319.92 <b>(-31.38%)</b></td><td>279.40 <b>(-39.85%)</b></td><td>233.20 (-15.38%)</td><td>84.06 <b>(-40.58%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>632.00 (n/a)</td><td>466.24 (n/a)</td><td>464.50 (n/a)</td><td>275.60 (n/a)</td><td>141.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (-11.82%)</td><td>0.03 (+5.91%)</td><td>0.03 <b>(+21.11%)</b></td><td>0.02 (+3.67%)</td><td>0.01 <b>(-31.76%)</b></td><td>580.20 (-3.54%)</td><td>469.02 (-8.78%)</td><td>449.10 (-17.44%)</td><td>330.60 (+13.41%)</td><td>98.90 <b>(-22.46%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.50 (n/a)</td><td>514.14 (n/a)</td><td>544.00 (n/a)</td><td>291.50 (n/a)</td><td>127.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (-11.58%)</td><td>0.02 (-7.77%)</td><td>0.02 (+3.96%)</td><td>0.01 <b>(-49.16%)</b></td><td>0.01 <b>(+83.88%)</b></td><td>671.90 <b>(+96.69%)</b></td><td>357.46 <b>(+21.00%)</b></td><td>292.80 (-3.81%)</td><td>263.30 (+13.10%)</td><td>176.40 <b>(+333.16%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>341.60 (n/a)</td><td>295.42 (n/a)</td><td>304.40 (n/a)</td><td>232.80 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (-18.69%)</td><td>0.01 <b>(-27.38%)</b></td><td>0.01 <b>(-45.30%)</b></td><td>0.01 (+13.63%)</td><td>0.00 <b>(-36.31%)</b></td><td>509.30 (-11.99%)</td><td>419.80 <b>(+27.77%)</b></td><td>446.30 <b>(+82.83%)</b></td><td>258.20 <b>(+22.95%)</b></td><td>101.71 <b>(-33.18%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.70 (n/a)</td><td>328.56 (n/a)</td><td>244.10 (n/a)</td><td>210.00 (n/a)</td><td>152.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (-4.78%)</td><td>0.01 <b>(-30.66%)</b></td><td>0.01 <b>(-50.77%)</b></td><td>0.01 (-19.65%)</td><td>0.01 (-11.15%)</td><td>775.80 <b>(+24.47%)</b></td><td>530.28 <b>(+41.14%)</b></td><td>542.50 <b>(+103.11%)</b></td><td>225.20 (+5.04%)</td><td>197.80 (+3.38%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.30 (n/a)</td><td>375.72 (n/a)</td><td>267.10 (n/a)</td><td>214.40 (n/a)</td><td>191.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.01 <b>(-45.11%)</b></td><td>0.01 <b>(-21.79%)</b></td><td>0.01 (-6.76%)</td><td>0.01 (-8.40%)</td><td>0.00 <b>(-74.99%)</b></td><td>571.30 (+9.17%)</td><td>492.68 (+17.90%)</td><td>491.40 (+7.25%)</td><td>403.00 <b>(+82.19%)</b></td><td>60.82 <b>(-47.78%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.30 (n/a)</td><td>417.88 (n/a)</td><td>458.20 (n/a)</td><td>221.20 (n/a)</td><td>116.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (-19.10%)</td><td>0.01 <b>(-33.26%)</b></td><td>0.01 <b>(-48.87%)</b></td><td>0.01 (+11.85%)</td><td>0.01 <b>(-29.29%)</b></td><td>596.20 (-10.59%)</td><td>495.18 <b>(+36.77%)</b></td><td>538.80 <b>(+95.57%)</b></td><td>233.60 <b>(+23.60%)</b></td><td>149.36 <b>(-25.24%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.80 (n/a)</td><td>362.06 (n/a)</td><td>275.50 (n/a)</td><td>189.00 (n/a)</td><td>199.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.01 <b>(-22.81%)</b></td><td>0.01 <b>(-46.50%)</b></td><td>0.01 <b>(-48.12%)</b></td><td>0.01 <b>(-64.58%)</b></td><td>0.00 <b>(+169.20%)</b></td><td>949.10 <b>(+182.30%)</b></td><td>644.72 <b>(+111.37%)</b></td><td>588.10 <b>(+92.76%)</b></td><td>351.20 <b>(+29.55%)</b></td><td>246.78 <b>(+913.73%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>336.20 (n/a)</td><td>305.02 (n/a)</td><td>305.10 (n/a)</td><td>271.10 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.10 (n/a)</td><td>375.74 (n/a)</td><td>420.40 (n/a)</td><td>266.40 (n/a)</td><td>98.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>574.20 (n/a)</td><td>461.76 (n/a)</td><td>447.10 (n/a)</td><td>360.50 (n/a)</td><td>77.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.60 (n/a)</td><td>417.48 (n/a)</td><td>491.00 (n/a)</td><td>272.60 (n/a)</td><td>120.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.40 (n/a)</td><td>435.94 (n/a)</td><td>423.10 (n/a)</td><td>249.00 (n/a)</td><td>123.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1898.50 (n/a)</td><td>709.50 (n/a)</td><td>527.30 (n/a)</td><td>268.50 (n/a)</td><td>679.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>676.40 (n/a)</td><td>448.34 (n/a)</td><td>541.40 (n/a)</td><td>192.60 (n/a)</td><td>211.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.40 (n/a)</td><td>410.84 (n/a)</td><td>393.10 (n/a)</td><td>271.90 (n/a)</td><td>139.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.60 (n/a)</td><td>373.02 (n/a)</td><td>401.30 (n/a)</td><td>263.70 (n/a)</td><td>103.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.30 (n/a)</td><td>368.92 (n/a)</td><td>296.60 (n/a)</td><td>240.60 (n/a)</td><td>128.63 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.80 (n/a)</td><td>413.12 (n/a)</td><td>359.50 (n/a)</td><td>299.20 (n/a)</td><td>137.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.20 (n/a)</td><td>410.34 (n/a)</td><td>352.30 (n/a)</td><td>232.00 (n/a)</td><td>160.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1970.80 (n/a)</td><td>788.32 (n/a)</td><td>574.10 (n/a)</td><td>379.40 (n/a)</td><td>667.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.62 (+1.70%)</td><td>0.33 <b>(-32.97%)</b></td><td>0.35 <b>(-20.84%)</b></td><td>0.13 <b>(-66.88%)</b></td><td>0.19 <b>(+100.45%)</b></td><td>1766.40 <b>(+201.95%)</b></td><td>917.74 <b>(+96.19%)</b></td><td>629.70 <b>(+26.32%)</b></td><td>358.60 (-1.67%)</td><td>569.46 <b>(+530.80%)</b></td><td>26.31 (+1.70%)</td><td>13.94 <b>(-32.97%)</b></td><td>14.99 <b>(-20.84%)</b></td><td>5.34 <b>(-66.88%)</b></td><td>8.19 <b>(+100.45%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.61 (n/a)</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.10 (n/a)</td><td>585.00 (n/a)</td><td>467.78 (n/a)</td><td>498.50 (n/a)</td><td>364.70 (n/a)</td><td>90.28 (n/a)</td><td>25.87 (n/a)</td><td>20.80 (n/a)</td><td>18.93 (n/a)</td><td>16.13 (n/a)</td><td>4.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.54 (+8.91%)</td><td>0.42 (-4.71%)</td><td>0.45 (-3.62%)</td><td>0.18 <b>(-48.20%)</b></td><td>0.14 <b>(+126.12%)</b></td><td>1212.30 <b>(+93.04%)</b></td><td>616.14 <b>(+20.12%)</b></td><td>490.40 (+3.77%)</td><td>406.20 (-8.18%)</td><td>335.25 <b>(+336.77%)</b></td><td>23.23 (+8.91%)</td><td>17.83 (-4.71%)</td><td>19.25 (-3.62%)</td><td>7.78 <b>(-48.20%)</b></td><td>5.87 <b>(+126.12%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>628.00 (n/a)</td><td>512.92 (n/a)</td><td>472.60 (n/a)</td><td>442.40 (n/a)</td><td>76.76 (n/a)</td><td>21.33 (n/a)</td><td>18.71 (n/a)</td><td>19.97 (n/a)</td><td>15.03 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.31 (+0.79%)</td><td>0.30 (-1.15%)</td><td>0.30 (-1.42%)</td><td>0.30 (-2.18%)</td><td>0.01 <b>(+154.09%)</b></td><td>84752.10 (+2.23%)</td><td>83136.20 (+1.19%)</td><td>83067.00 (+1.44%)</td><td>80892.80 (-0.78%)</td><td>1641.56 <b>(+158.32%)</b></td><td>212.38 (+0.79%)</td><td>206.71 (-1.15%)</td><td>206.82 (-1.42%)</td><td>202.71 (-2.18%)</td><td>4.10 <b>(+154.09%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>82902.30 (n/a)</td><td>82161.88 (n/a)</td><td>81887.00 (n/a)</td><td>81532.80 (n/a)</td><td>635.48 (n/a)</td><td>210.71 (n/a)</td><td>209.11 (n/a)</td><td>209.80 (n/a)</td><td>207.23 (n/a)</td><td>1.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>1.03 (-3.17%)</td><td>1.01 (-1.64%)</td><td>1.02 (-0.58%)</td><td>0.98 (-1.70%)</td><td>0.02 (-8.29%)</td><td>25585.90 (+1.73%)</td><td>24937.52 (+1.67%)</td><td>24771.20 (+0.58%)</td><td>24367.50 (+3.28%)</td><td>559.89 (-3.05%)</td><td>705.03 (-3.17%)</td><td>689.19 (-1.64%)</td><td>693.54 (-0.58%)</td><td>671.46 (-1.70%)</td><td>15.40 (-8.29%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>1.07 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.02 (n/a)</td><td>25150.90 (n/a)</td><td>24528.92 (n/a)</td><td>24628.10 (n/a)</td><td>23594.10 (n/a)</td><td>577.48 (n/a)</td><td>728.14 (n/a)</td><td>700.71 (n/a)</td><td>697.57 (n/a)</td><td>683.07 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>1.94 <b>(-30.37%)</b></td><td>1.76 (-12.44%)</td><td>1.83 (-11.71%)</td><td>1.35 (-0.69%)</td><td>0.24 <b>(-54.89%)</b></td><td>5982.40 (+0.70%)</td><td>4671.68 (+9.67%)</td><td>4397.70 (+13.26%)</td><td>4165.70 <b>(+43.63%)</b></td><td>757.48 <b>(-34.77%)</b></td><td>507.46 <b>(-30.37%)</b></td><td>460.72 (-12.44%)</td><td>480.69 (-11.71%)</td><td>353.36 (-0.69%)</td><td>63.62 <b>(-54.89%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>2.78 (n/a)</td><td>2.01 (n/a)</td><td>2.08 (n/a)</td><td>1.36 (n/a)</td><td>0.54 (n/a)</td><td>5941.10 (n/a)</td><td>4259.74 (n/a)</td><td>3882.70 (n/a)</td><td>2900.40 (n/a)</td><td>1161.30 (n/a)</td><td>728.83 (n/a)</td><td>526.19 (n/a)</td><td>544.45 (n/a)</td><td>355.81 (n/a)</td><td>141.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.25 (+8.50%)</td><td>0.21 (+1.05%)</td><td>0.22 (+10.25%)</td><td>0.17 (-12.52%)</td><td>0.03 <b>(+77.10%)</b></td><td>7433.30 (+14.31%)</td><td>6039.82 (+0.25%)</td><td>5669.70 (-9.30%)</td><td>5008.80 (-7.83%)</td><td>940.99 <b>(+89.60%)</b></td><td>13.40 (+8.50%)</td><td>11.32 (+1.05%)</td><td>11.84 (+10.25%)</td><td>9.03 (-12.52%)</td><td>1.68 <b>(+77.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>6502.90 (n/a)</td><td>6024.82 (n/a)</td><td>6250.90 (n/a)</td><td>5434.40 (n/a)</td><td>496.30 (n/a)</td><td>12.35 (n/a)</td><td>11.20 (n/a)</td><td>10.74 (n/a)</td><td>10.32 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.14 (+19.48%)</td><td>0.11 <b>(+41.19%)</b></td><td>0.12 <b>(+30.04%)</b></td><td>0.06 <b>(+246.79%)</b></td><td>0.03 <b>(-24.07%)</b></td><td>0.14 (+19.48%)</td><td>0.11 <b>(+41.19%)</b></td><td>0.11 <b>(+30.04%)</b></td><td>0.06 <b>(+246.79%)</b></td><td>0.03 <b>(-24.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>3.91 (+1.12%)</td><td>3.64 (-1.49%)</td><td>3.73 (-1.52%)</td><td>3.24 (-5.09%)</td><td>0.27 <b>(+43.94%)</b></td><td>3.91 (+1.12%)</td><td>3.64 (-1.49%)</td><td>3.73 (-1.52%)</td><td>3.24 (-5.09%)</td><td>0.27 <b>(+43.94%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>3.86 (n/a)</td><td>3.70 (n/a)</td><td>3.79 (n/a)</td><td>3.41 (n/a)</td><td>0.19 (n/a)</td><td>3.86 (n/a)</td><td>3.70 (n/a)</td><td>3.79 (n/a)</td><td>3.41 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>7.60 (+0.02%)</td><td>6.13 (-4.58%)</td><td>5.91 (-11.56%)</td><td>5.44 (+12.56%)</td><td>0.84 <b>(-28.74%)</b></td><td>7.59 (+0.02%)</td><td>6.13 (-4.58%)</td><td>5.91 (-11.56%)</td><td>5.44 (+12.56%)</td><td>0.84 <b>(-28.74%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>7.60 (n/a)</td><td>6.42 (n/a)</td><td>6.68 (n/a)</td><td>4.83 (n/a)</td><td>1.19 (n/a)</td><td>7.59 (n/a)</td><td>6.42 (n/a)</td><td>6.68 (n/a)</td><td>4.83 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>13.98 (+2.04%)</td><td>10.57 (+8.18%)</td><td>9.59 (+16.69%)</td><td>7.85 (-1.40%)</td><td>2.72 (+9.60%)</td><td>13.97 (+2.04%)</td><td>10.56 (+8.18%)</td><td>9.59 (+16.69%)</td><td>7.85 (-1.40%)</td><td>2.72 (+9.60%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>13.70 (n/a)</td><td>9.77 (n/a)</td><td>8.22 (n/a)</td><td>7.96 (n/a)</td><td>2.48 (n/a)</td><td>13.69 (n/a)</td><td>9.77 (n/a)</td><td>8.22 (n/a)</td><td>7.96 (n/a)</td><td>2.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>3.93 (-0.12%)</td><td>3.77 (-0.77%)</td><td>3.77 (-2.88%)</td><td>3.61 (+2.34%)</td><td>0.12 <b>(-30.11%)</b></td><td>3.93 (-0.12%)</td><td>3.76 (-0.77%)</td><td>3.77 (-2.88%)</td><td>3.61 (+2.34%)</td><td>0.12 <b>(-30.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>3.93 (n/a)</td><td>3.79 (n/a)</td><td>3.88 (n/a)</td><td>3.53 (n/a)</td><td>0.16 (n/a)</td><td>3.93 (n/a)</td><td>3.79 (n/a)</td><td>3.88 (n/a)</td><td>3.53 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>7.27 (-3.61%)</td><td>6.09 (-3.31%)</td><td>6.59 (-0.70%)</td><td>4.84 (+0.10%)</td><td>1.08 (+0.01%)</td><td>7.27 (-3.61%)</td><td>6.09 (-3.31%)</td><td>6.59 (-0.70%)</td><td>4.84 (+0.10%)</td><td>1.08 (+0.01%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>7.55 (n/a)</td><td>6.30 (n/a)</td><td>6.64 (n/a)</td><td>4.84 (n/a)</td><td>1.08 (n/a)</td><td>7.54 (n/a)</td><td>6.30 (n/a)</td><td>6.63 (n/a)</td><td>4.84 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>14.01 (+5.02%)</td><td>10.91 (+18.25%)</td><td>10.61 <b>(+23.88%)</b></td><td>8.31 (+16.02%)</td><td>2.60 (+7.89%)</td><td>14.00 (+5.02%)</td><td>10.90 (+18.25%)</td><td>10.61 <b>(+23.88%)</b></td><td>8.31 (+16.02%)</td><td>2.60 (+7.89%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>13.34 (n/a)</td><td>9.23 (n/a)</td><td>8.57 (n/a)</td><td>7.17 (n/a)</td><td>2.41 (n/a)</td><td>13.33 (n/a)</td><td>9.22 (n/a)</td><td>8.56 (n/a)</td><td>7.16 (n/a)</td><td>2.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.70 (-13.72%)</td><td>1.84 (-18.17%)</td><td>1.61 <b>(-42.62%)</b></td><td>1.04 (-5.48%)</td><td>0.65 <b>(-36.72%)</b></td><td>2.69 (-13.72%)</td><td>1.83 (-18.17%)</td><td>1.61 <b>(-42.62%)</b></td><td>1.04 (-5.48%)</td><td>0.65 <b>(-36.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>3.13 (n/a)</td><td>2.25 (n/a)</td><td>2.81 (n/a)</td><td>1.10 (n/a)</td><td>1.02 (n/a)</td><td>3.12 (n/a)</td><td>2.24 (n/a)</td><td>2.80 (n/a)</td><td>1.10 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.49 (+7.79%)</td><td>0.28 (-14.63%)</td><td>0.33 (-14.49%)</td><td>0.07 (-0.27%)</td><td>0.17 (+15.11%)</td><td>0.48 (+7.79%)</td><td>0.27 (-14.63%)</td><td>0.32 (-14.49%)</td><td>0.07 (-0.27%)</td><td>0.17 (+15.11%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.38 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.74 (+0.90%)</td><td>0.46 <b>(-23.94%)</b></td><td>0.45 <b>(-28.66%)</b></td><td>0.08 <b>(-77.96%)</b></td><td>0.25 <b>(+63.84%)</b></td><td>0.73 (+0.90%)</td><td>0.46 <b>(-23.94%)</b></td><td>0.45 <b>(-28.66%)</b></td><td>0.08 <b>(-77.96%)</b></td><td>0.24 <b>(+63.84%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.73 (n/a)</td><td>0.61 (n/a)</td><td>0.63 (n/a)</td><td>0.35 (n/a)</td><td>0.15 (n/a)</td><td>0.72 (n/a)</td><td>0.60 (n/a)</td><td>0.63 (n/a)</td><td>0.34 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.02 (-16.10%)</td><td>1.21 <b>(-24.36%)</b></td><td>1.47 <b>(-32.12%)</b></td><td>0.45 (+7.09%)</td><td>0.71 <b>(-27.14%)</b></td><td>1.99 (-16.10%)</td><td>1.19 <b>(-24.36%)</b></td><td>1.45 <b>(-32.12%)</b></td><td>0.44 (+7.09%)</td><td>0.70 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>2.41 (n/a)</td><td>1.60 (n/a)</td><td>2.17 (n/a)</td><td>0.42 (n/a)</td><td>0.98 (n/a)</td><td>2.37 (n/a)</td><td>1.57 (n/a)</td><td>2.14 (n/a)</td><td>0.41 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>447.30 (n/a)</td><td>336.28 (n/a)</td><td>278.80 (n/a)</td><td>232.60 (n/a)</td><td>102.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.50 (n/a)</td><td>372.80 (n/a)</td><td>280.90 (n/a)</td><td>248.70 (n/a)</td><td>148.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>662.70 (n/a)</td><td>486.84 (n/a)</td><td>472.40 (n/a)</td><td>268.20 (n/a)</td><td>152.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.50 (n/a)</td><td>395.40 (n/a)</td><td>444.40 (n/a)</td><td>239.00 (n/a)</td><td>145.36 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.20 (n/a)</td><td>450.02 (n/a)</td><td>428.20 (n/a)</td><td>377.00 (n/a)</td><td>76.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.10 (n/a)</td><td>410.78 (n/a)</td><td>421.90 (n/a)</td><td>257.90 (n/a)</td><td>101.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (+17.08%)</td><td>0.02 (-19.68%)</td><td>0.02 <b>(-48.04%)</b></td><td>0.01 (+2.60%)</td><td>0.01 (+3.93%)</td><td>618.30 (-2.54%)</td><td>466.86 <b>(+21.81%)</b></td><td>481.90 <b>(+92.45%)</b></td><td>205.80 (-14.61%)</td><td>164.10 (-13.78%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.40 (n/a)</td><td>383.26 (n/a)</td><td>250.40 (n/a)</td><td>241.00 (n/a)</td><td>190.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-19.24%)</td><td>0.03 (+16.98%)</td><td>0.03 (-14.00%)</td><td>0.03 <b>(+531.79%)</b></td><td>0.00 <b>(-92.44%)</b></td><td>301.20 <b>(-84.17%)</b></td><td>287.56 <b>(-55.47%)</b></td><td>289.20 (+16.28%)</td><td>272.70 <b>(+23.84%)</b></td><td>11.10 <b>(-98.46%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1903.20 (n/a)</td><td>645.76 (n/a)</td><td>248.70 (n/a)</td><td>220.20 (n/a)</td><td>722.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-16.02%)</td><td>0.02 <b>(-30.75%)</b></td><td>0.02 <b>(-32.81%)</b></td><td>0.00 (+0.28%)</td><td>0.01 (-1.56%)</td><td>1880.90 (-0.28%)</td><td>952.52 <b>(+57.21%)</b></td><td>467.60 <b>(+48.82%)</b></td><td>266.80 (+19.05%)</td><td>843.63 (+17.47%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1886.10 (n/a)</td><td>605.90 (n/a)</td><td>314.20 (n/a)</td><td>224.10 (n/a)</td><td>718.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (-2.93%)</td><td>0.02 <b>(-20.11%)</b></td><td>0.02 <b>(-40.21%)</b></td><td>0.01 <b>(-27.28%)</b></td><td>0.01 <b>(+56.30%)</b></td><td>590.90 <b>(+37.51%)</b></td><td>430.98 <b>(+39.29%)</b></td><td>493.80 <b>(+67.28%)</b></td><td>233.40 (+3.00%)</td><td>170.29 <b>(+119.53%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>429.70 (n/a)</td><td>309.42 (n/a)</td><td>295.20 (n/a)</td><td>226.60 (n/a)</td><td>77.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 <b>(-42.92%)</b></td><td>0.02 (-12.32%)</td><td>0.02 (-7.81%)</td><td>0.01 <b>(+77.97%)</b></td><td>0.00 <b>(-70.33%)</b></td><td>628.00 <b>(-43.81%)</b></td><td>514.26 (-8.39%)</td><td>512.70 (+8.46%)</td><td>408.00 <b>(+75.18%)</b></td><td>94.09 <b>(-71.55%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1117.60 (n/a)</td><td>561.34 (n/a)</td><td>472.70 (n/a)</td><td>232.90 (n/a)</td><td>330.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-2.10%)</td><td>0.02 <b>(-29.79%)</b></td><td>0.01 <b>(-47.54%)</b></td><td>0.01 <b>(-40.85%)</b></td><td>0.01 (+1.38%)</td><td>1031.30 <b>(+69.07%)</b></td><td>600.86 <b>(+50.71%)</b></td><td>578.00 <b>(+90.63%)</b></td><td>240.10 (+2.13%)</td><td>281.54 <b>(+54.64%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.00 (n/a)</td><td>398.68 (n/a)</td><td>303.20 (n/a)</td><td>235.10 (n/a)</td><td>182.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-10.75%)</td><td>0.02 (+7.55%)</td><td>0.03 <b>(+22.70%)</b></td><td>0.01 (+6.41%)</td><td>0.01 (-10.14%)</td><td>617.70 (-6.02%)</td><td>394.90 (-9.32%)</td><td>298.90 (-18.49%)</td><td>275.90 (+12.06%)</td><td>155.26 (-12.53%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.30 (n/a)</td><td>435.48 (n/a)</td><td>366.70 (n/a)</td><td>246.20 (n/a)</td><td>177.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-12.99%)</td><td>0.02 (-11.52%)</td><td>0.02 (-10.31%)</td><td>0.01 (-19.37%)</td><td>0.01 (-11.86%)</td><td>640.30 <b>(+24.02%)</b></td><td>484.36 (+13.69%)</td><td>516.50 (+11.48%)</td><td>286.70 (+14.91%)</td><td>130.52 <b>(+26.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.30 (n/a)</td><td>426.02 (n/a)</td><td>463.30 (n/a)</td><td>249.50 (n/a)</td><td>103.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-16.18%)</td><td>0.02 <b>(-25.89%)</b></td><td>0.02 <b>(-25.20%)</b></td><td>0.00 <b>(-77.97%)</b></td><td>0.01 <b>(+33.79%)</b></td><td>2131.10 <b>(+354.01%)</b></td><td>736.60 <b>(+111.25%)</b></td><td>424.20 <b>(+33.69%)</b></td><td>287.70 (+19.33%)</td><td>785.59 <b>(+649.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.40 (n/a)</td><td>348.68 (n/a)</td><td>317.30 (n/a)</td><td>241.10 (n/a)</td><td>104.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-6.41%)</td><td>0.02 (-1.09%)</td><td>0.03 (+0.02%)</td><td>0.01 <b>(+138.92%)</b></td><td>0.01 <b>(-21.04%)</b></td><td>1020.70 <b>(-58.14%)</b></td><td>458.40 <b>(-37.35%)</b></td><td>292.20 (+0.00%)</td><td>246.50 (+6.85%)</td><td>326.68 <b>(-65.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2438.50 (n/a)</td><td>731.64 (n/a)</td><td>292.20 (n/a)</td><td>230.70 (n/a)</td><td>958.58 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (+10.51%)</td><td>0.02 (-14.94%)</td><td>0.02 (+0.47%)</td><td>0.00 <b>(-68.62%)</b></td><td>0.01 <b>(+76.16%)</b></td><td>1904.50 <b>(+218.69%)</b></td><td>823.10 <b>(+81.84%)</b></td><td>459.90 (-0.48%)</td><td>239.70 (-9.48%)</td><td>681.66 <b>(+467.04%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.60 (n/a)</td><td>452.66 (n/a)</td><td>462.10 (n/a)</td><td>264.80 (n/a)</td><td>120.21 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 <b>(+59.61%)</b></td><td>0.02 <b>(+22.31%)</b></td><td>0.02 (+1.32%)</td><td>0.02 (+16.81%)</td><td>0.01 <b>(+135.27%)</b></td><td>534.10 (-14.39%)</td><td>421.74 (-13.74%)</td><td>476.50 (-1.30%)</td><td>252.20 <b>(-37.36%)</b></td><td>120.66 <b>(+30.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>623.90 (n/a)</td><td>488.90 (n/a)</td><td>482.80 (n/a)</td><td>402.60 (n/a)</td><td>92.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 <b>(-21.16%)</b></td><td>0.02 (-17.10%)</td><td>0.01 (-15.69%)</td><td>0.01 (-0.01%)</td><td>0.01 <b>(-31.67%)</b></td><td>734.50 (+0.01%)</td><td>531.10 (+13.21%)</td><td>566.00 (+18.61%)</td><td>289.40 <b>(+26.82%)</b></td><td>162.89 (-16.28%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>734.40 (n/a)</td><td>469.14 (n/a)</td><td>477.20 (n/a)</td><td>228.20 (n/a)</td><td>194.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 <b>(-32.97%)</b></td><td>0.02 (-19.44%)</td><td>0.02 (-9.65%)</td><td>0.01 (-11.50%)</td><td>0.00 <b>(-49.24%)</b></td><td>658.80 (+12.98%)</td><td>501.62 (+17.78%)</td><td>535.00 (+10.67%)</td><td>376.60 <b>(+49.15%)</b></td><td>114.46 (-15.35%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>425.88 (n/a)</td><td>483.40 (n/a)</td><td>252.50 (n/a)</td><td>135.21 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (+3.93%)</td><td>0.03 <b>(+23.28%)</b></td><td>0.03 (+14.08%)</td><td>0.02 <b>(+70.01%)</b></td><td>0.01 <b>(-49.45%)</b></td><td>364.20 <b>(-41.19%)</b></td><td>270.44 <b>(-30.47%)</b></td><td>258.70 (-12.33%)</td><td>218.00 (-3.80%)</td><td>55.75 <b>(-70.70%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.30 (n/a)</td><td>388.94 (n/a)</td><td>295.10 (n/a)</td><td>226.60 (n/a)</td><td>190.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 <b>(-21.52%)</b></td><td>0.03 (-11.88%)</td><td>0.02 (+1.63%)</td><td>0.02 <b>(+250.74%)</b></td><td>0.01 <b>(-58.68%)</b></td><td>541.90 <b>(-71.49%)</b></td><td>475.48 <b>(-31.60%)</b></td><td>511.30 (-1.60%)</td><td>291.60 <b>(+27.39%)</b></td><td>103.91 <b>(-84.99%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1900.70 (n/a)</td><td>695.12 (n/a)</td><td>519.60 (n/a)</td><td>228.90 (n/a)</td><td>692.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (+0.40%)</td><td>0.03 (+15.97%)</td><td>0.03 (+12.76%)</td><td>0.02 <b>(+285.90%)</b></td><td>0.01 <b>(-33.06%)</b></td><td>522.70 <b>(-74.09%)</b></td><td>353.28 <b>(-48.07%)</b></td><td>278.80 (-11.32%)</td><td>239.50 (-0.42%)</td><td>132.75 <b>(-82.53%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2017.20 (n/a)</td><td>680.36 (n/a)</td><td>314.40 (n/a)</td><td>240.50 (n/a)</td><td>759.87 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 <b>(-32.10%)</b></td><td>0.02 (+10.69%)</td><td>0.02 <b>(+21.66%)</b></td><td>0.02 <b>(+240.47%)</b></td><td>0.00 <b>(-68.60%)</b></td><td>564.10 <b>(-70.63%)</b></td><td>471.52 <b>(-40.40%)</b></td><td>468.30 (-17.81%)</td><td>347.80 <b>(+47.25%)</b></td><td>84.43 <b>(-87.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1920.60 (n/a)</td><td>791.14 (n/a)</td><td>569.80 (n/a)</td><td>236.20 (n/a)</td><td>654.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (-11.95%)</td><td>0.03 (+9.84%)</td><td>0.03 <b>(+68.73%)</b></td><td>0.02 (+1.32%)</td><td>0.01 <b>(-20.64%)</b></td><td>528.30 (-1.29%)</td><td>340.08 (-12.63%)</td><td>260.20 <b>(-40.74%)</b></td><td>239.30 (+13.57%)</td><td>127.27 (-13.39%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.20 (n/a)</td><td>389.24 (n/a)</td><td>439.10 (n/a)</td><td>210.70 (n/a)</td><td>146.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.04 (-13.27%)</td><td>0.03 (-4.95%)</td><td>0.03 (+5.24%)</td><td>0.02 (+0.40%)</td><td>0.01 (-16.31%)</td><td>598.10 (-0.40%)</td><td>391.82 (+2.90%)</td><td>305.20 (-4.98%)</td><td>266.60 (+15.31%)</td><td>145.60 (-5.03%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.50 (n/a)</td><td>380.78 (n/a)</td><td>321.20 (n/a)</td><td>231.20 (n/a)</td><td>153.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (+8.47%)</td><td>0.03 <b>(+39.81%)</b></td><td>0.03 <b>(+79.10%)</b></td><td>0.01 <b>(+119.41%)</b></td><td>0.01 (-13.85%)</td><td>581.30 <b>(-54.42%)</b></td><td>360.52 <b>(-40.56%)</b></td><td>289.80 <b>(-44.16%)</b></td><td>238.40 (-7.81%)</td><td>143.97 <b>(-64.23%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1275.30 (n/a)</td><td>606.56 (n/a)</td><td>519.00 (n/a)</td><td>258.60 (n/a)</td><td>402.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 <b>(-21.13%)</b></td><td>0.02 (-15.83%)</td><td>0.02 (-14.41%)</td><td>0.02 (+11.95%)</td><td>0.00 <b>(-42.53%)</b></td><td>600.50 (-10.68%)</td><td>460.44 (+11.65%)</td><td>446.60 (+16.85%)</td><td>328.30 <b>(+26.81%)</b></td><td>97.83 <b>(-37.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.30 (n/a)</td><td>412.40 (n/a)</td><td>382.20 (n/a)</td><td>258.90 (n/a)</td><td>157.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 <b>(-24.73%)</b></td><td>0.02 <b>(-22.30%)</b></td><td>0.02 <b>(-37.16%)</b></td><td>0.01 (-7.75%)</td><td>0.01 <b>(-31.97%)</b></td><td>564.10 (+8.40%)</td><td>429.38 <b>(+23.87%)</b></td><td>481.00 <b>(+59.11%)</b></td><td>288.10 <b>(+32.89%)</b></td><td>123.43 (-6.24%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.40 (n/a)</td><td>346.64 (n/a)</td><td>302.30 (n/a)</td><td>216.80 (n/a)</td><td>131.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.03 (+3.23%)</td><td>0.02 (-1.73%)</td><td>0.02 (-5.14%)</td><td>0.02 (-7.43%)</td><td>0.01 <b>(+22.29%)</b></td><td>599.60 (+8.02%)</td><td>419.96 (+4.62%)</td><td>426.80 (+5.43%)</td><td>279.50 (-3.15%)</td><td>132.79 <b>(+25.64%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>555.10 (n/a)</td><td>401.42 (n/a)</td><td>404.80 (n/a)</td><td>288.60 (n/a)</td><td>105.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.02 (-12.64%)</td><td>0.02 (-13.84%)</td><td>0.01 <b>(-23.28%)</b></td><td>0.01 (-0.11%)</td><td>0.00 (-3.05%)</td><td>644.00 (+0.11%)</td><td>511.12 (+16.51%)</td><td>546.40 <b>(+30.34%)</b></td><td>363.70 (+14.48%)</td><td>137.45 (+7.79%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.30 (n/a)</td><td>438.70 (n/a)</td><td>419.20 (n/a)</td><td>317.70 (n/a)</td><td>127.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.35 (-17.43%)</td><td>0.27 (-3.18%)</td><td>0.26 <b>(+25.32%)</b></td><td>0.17 (+5.81%)</td><td>0.08 <b>(-36.05%)</b></td><td>569.30 (-5.48%)</td><td>394.28 (-4.34%)</td><td>379.90 <b>(-20.19%)</b></td><td>280.00 <b>(+21.11%)</b></td><td>122.52 <b>(-25.61%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.43 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>602.30 (n/a)</td><td>412.18 (n/a)</td><td>476.00 (n/a)</td><td>231.20 (n/a)</td><td>164.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.41 (+8.34%)</td><td>0.30 <b>(+41.60%)</b></td><td>0.30 <b>(+74.63%)</b></td><td>0.20 <b>(+294.64%)</b></td><td>0.09 <b>(-43.64%)</b></td><td>490.40 <b>(-74.66%)</b></td><td>352.82 <b>(-57.45%)</b></td><td>325.70 <b>(-42.74%)</b></td><td>239.20 (-7.68%)</td><td>104.32 <b>(-85.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.38 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>1935.40 (n/a)</td><td>829.18 (n/a)</td><td>568.80 (n/a)</td><td>259.10 (n/a)</td><td>708.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.32 (-17.64%)</td><td>0.23 (+3.57%)</td><td>0.22 <b>(+26.09%)</b></td><td>0.17 (+13.59%)</td><td>0.06 <b>(-35.86%)</b></td><td>563.80 (-11.96%)</td><td>443.40 (-9.57%)</td><td>437.30 <b>(-20.68%)</b></td><td>306.40 <b>(+21.39%)</b></td><td>116.00 <b>(-30.33%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.39 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>640.40 (n/a)</td><td>490.34 (n/a)</td><td>551.30 (n/a)</td><td>252.40 (n/a)</td><td>166.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.29 (+9.15%)</td><td>0.20 (+6.23%)</td><td>0.21 <b>(+28.82%)</b></td><td>0.13 (-10.03%)</td><td>0.07 <b>(+21.22%)</b></td><td>565.50 (+11.14%)</td><td>395.92 (-2.96%)</td><td>355.70 <b>(-22.37%)</b></td><td>256.90 (-8.38%)</td><td>135.18 <b>(+26.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>508.80 (n/a)</td><td>408.00 (n/a)</td><td>458.20 (n/a)</td><td>280.40 (n/a)</td><td>107.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.27 (-8.76%)</td><td>0.18 (-12.00%)</td><td>0.17 (-5.94%)</td><td>0.14 (+8.55%)</td><td>0.06 <b>(-24.19%)</b></td><td>544.00 (-7.87%)</td><td>441.64 (+9.18%)</td><td>440.30 (+6.30%)</td><td>272.90 (+9.60%)</td><td>111.46 <b>(-21.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>590.50 (n/a)</td><td>404.50 (n/a)</td><td>414.20 (n/a)</td><td>249.00 (n/a)</td><td>141.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.19 <b>(-28.13%)</b></td><td>0.15 (+0.81%)</td><td>0.16 (+12.93%)</td><td>0.12 <b>(+194.64%)</b></td><td>0.03 <b>(-66.91%)</b></td><td>591.00 <b>(-66.06%)</b></td><td>493.34 <b>(-30.22%)</b></td><td>464.10 (-11.47%)</td><td>382.90 <b>(+39.14%)</b></td><td>86.09 <b>(-85.44%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1741.40 (n/a)</td><td>706.96 (n/a)</td><td>524.20 (n/a)</td><td>275.20 (n/a)</td><td>591.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.43 <b>(+47.35%)</b></td><td>0.33 <b>(+29.91%)</b></td><td>0.31 <b>(+27.23%)</b></td><td>0.19 (-5.55%)</td><td>0.10 <b>(+176.39%)</b></td><td>685.90 (+5.87%)</td><td>439.66 (-17.04%)</td><td>422.20 <b>(-21.41%)</b></td><td>303.20 <b>(-32.14%)</b></td><td>158.19 <b>(+92.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>647.90 (n/a)</td><td>529.96 (n/a)</td><td>537.20 (n/a)</td><td>446.80 (n/a)</td><td>82.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.48 (-17.30%)</td><td>0.33 (-1.09%)</td><td>0.42 <b>(+51.05%)</b></td><td>0.06 <b>(-75.57%)</b></td><td>0.17 <b>(+24.51%)</b></td><td>2080.70 <b>(+309.26%)</b></td><td>696.50 <b>(+61.72%)</b></td><td>308.90 <b>(-33.80%)</b></td><td>273.00 <b>(+20.90%)</b></td><td>779.73 <b>(+572.02%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.58 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>508.40 (n/a)</td><td>430.68 (n/a)</td><td>466.60 (n/a)</td><td>225.80 (n/a)</td><td>116.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.49 <b>(+91.84%)</b></td><td>0.26 <b>(+25.74%)</b></td><td>0.22 (-3.45%)</td><td>0.07 <b>(-44.57%)</b></td><td>0.17 <b>(+229.84%)</b></td><td>1905.40 <b>(+80.42%)</b></td><td>796.98 (+18.77%)</td><td>601.90 (+3.58%)</td><td>266.20 <b>(-47.88%)</b></td><td>663.78 <b>(+197.50%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>1056.10 (n/a)</td><td>671.00 (n/a)</td><td>581.10 (n/a)</td><td>510.70 (n/a)</td><td>223.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 (-18.75%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-38.11%)</b></td><td>17449.67 <b>(-22.34%)</b></td><td>15216.24 (-8.88%)</td><td>16958.51 (+1.10%)</td><td>7572.09 <b>(+21.18%)</b></td><td>4281.55 <b>(-33.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22467.92 (n/a)</td><td>16698.71 (n/a)</td><td>16773.64 (n/a)</td><td>6248.54 (n/a)</td><td>6463.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.00 <b>(+180.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+125.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+623.42%)</b></td><td>18220.87 (-18.49%)</td><td>10899.98 <b>(-43.49%)</b></td><td>8756.79 <b>(-52.93%)</b></td><td>6054.58 <b>(-62.34%)</b></td><td>5103.70 <b>(+104.05%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22354.73 (n/a)</td><td>19287.32 (n/a)</td><td>18602.01 (n/a)</td><td>16075.85 (n/a)</td><td>2501.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>0.14 (-11.67%)</td><td>0.10 (-4.65%)</td><td>0.08 (-5.46%)</td><td>0.07 (-3.50%)</td><td>0.03 (-13.46%)</td><td>28137.61 (+3.55%)</td><td>22850.01 (+4.27%)</td><td>26347.03 (+5.76%)</td><td>14820.53 (+13.19%)</td><td>6003.43 (+4.95%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27172.73 (n/a)</td><td>21913.98 (n/a)</td><td>24912.62 (n/a)</td><td>13093.31 (n/a)</td><td>5720.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>1.15 <b>(-28.38%)</b></td><td>0.95 (+10.21%)</td><td>0.94 <b>(+20.48%)</b></td><td>0.71 <b>(+154.40%)</b></td><td>0.19 <b>(-62.04%)</b></td><td>741.40 <b>(-60.69%)</b></td><td>571.60 <b>(-32.55%)</b></td><td>559.60 (-17.00%)</td><td>456.20 <b>(+39.64%)</b></td><td>118.48 <b>(-80.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>1.60 (n/a)</td><td>0.86 (n/a)</td><td>0.78 (n/a)</td><td>0.28 (n/a)</td><td>0.49 (n/a)</td><td>1886.20 (n/a)</td><td>847.50 (n/a)</td><td>674.20 (n/a)</td><td>326.70 (n/a)</td><td>609.95 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.50 (-5.90%)</td><td>1.45 <b>(-30.89%)</b></td><td>1.58 <b>(-28.11%)</b></td><td>0.29 <b>(-78.73%)</b></td><td>0.79 <b>(+43.75%)</b></td><td>3562.90 <b>(+370.23%)</b></td><td>1221.64 <b>(+130.56%)</b></td><td>664.60 <b>(+39.10%)</b></td><td>419.70 (+6.25%)</td><td>1316.22 <b>(+754.87%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>2.65 (n/a)</td><td>2.11 (n/a)</td><td>2.19 (n/a)</td><td>1.38 (n/a)</td><td>0.55 (n/a)</td><td>757.70 (n/a)</td><td>529.86 (n/a)</td><td>477.80 (n/a)</td><td>395.00 (n/a)</td><td>153.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:42:03</td><td>2.11 (+8.53%)</td><td>1.00 (-19.50%)</td><td>0.86 <b>(-27.57%)</b></td><td>0.46 <b>(-33.67%)</b></td><td>0.64 <b>(+42.17%)</b></td><td>1128.60 <b>(+50.76%)</b></td><td>669.66 <b>(+42.87%)</b></td><td>607.10 <b>(+38.07%)</b></td><td>249.00 (-7.88%)</td><td>322.32 <b>(+83.23%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>1.94 (n/a)</td><td>1.25 (n/a)</td><td>1.19 (n/a)</td><td>0.70 (n/a)</td><td>0.45 (n/a)</td><td>748.60 (n/a)</td><td>468.72 (n/a)</td><td>439.70 (n/a)</td><td>270.30 (n/a)</td><td>175.91 (n/a)</td>
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
