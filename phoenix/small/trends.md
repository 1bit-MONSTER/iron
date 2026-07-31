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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.06 <b>(+33.83%)</b></td><td>0.04 (+16.19%)</td><td>0.05 <b>(+29.74%)</b></td><td>0.02 (-16.05%)</td><td>0.02 <b>(+129.82%)</b></td><td>563.90 (+19.12%)</td><td>339.88 (-0.76%)</td><td>235.60 <b>(-22.93%)</b></td><td>194.30 <b>(-25.30%)</b></td><td>169.74 <b>(+104.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.40 (n/a)</td><td>342.50 (n/a)</td><td>305.70 (n/a)</td><td>260.10 (n/a)</td><td>82.83 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.05 (-2.26%)</td><td>0.04 (+5.93%)</td><td>0.04 (+4.56%)</td><td>0.03 <b>(+52.71%)</b></td><td>0.01 <b>(-46.50%)</b></td><td>378.40 <b>(-34.52%)</b></td><td>301.86 (-13.13%)</td><td>276.40 (-4.36%)</td><td>250.00 (+2.29%)</td><td>51.97 <b>(-62.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.90 (n/a)</td><td>347.50 (n/a)</td><td>289.00 (n/a)</td><td>244.40 (n/a)</td><td>140.36 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 <b>(-25.93%)</b></td><td>0.02 (-14.82%)</td><td>0.02 (-17.80%)</td><td>0.01 <b>(-21.15%)</b></td><td>0.01 <b>(-27.46%)</b></td><td>1366.60 <b>(+26.82%)</b></td><td>694.28 (+17.25%)</td><td>644.60 <b>(+21.67%)</b></td><td>328.30 <b>(+34.99%)</b></td><td>400.95 <b>(+32.29%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1077.60 (n/a)</td><td>592.14 (n/a)</td><td>529.80 (n/a)</td><td>243.20 (n/a)</td><td>303.08 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (+11.15%)</td><td>0.02 (-8.58%)</td><td>0.01 <b>(-39.55%)</b></td><td>0.01 (+1.81%)</td><td>0.01 (+8.84%)</td><td>568.10 (-1.78%)</td><td>396.54 (+9.61%)</td><td>435.30 <b>(+65.45%)</b></td><td>197.50 (-10.02%)</td><td>158.42 (-5.04%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.40 (n/a)</td><td>361.76 (n/a)</td><td>263.10 (n/a)</td><td>219.50 (n/a)</td><td>166.82 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (-10.86%)</td><td>0.01 (-16.25%)</td><td>0.01 (-2.27%)</td><td>0.01 (+2.38%)</td><td>0.00 <b>(-36.56%)</b></td><td>540.90 (-2.33%)</td><td>454.28 (+10.46%)</td><td>477.60 (+2.31%)</td><td>270.10 (+12.21%)</td><td>107.61 <b>(-31.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.80 (n/a)</td><td>411.28 (n/a)</td><td>466.80 (n/a)</td><td>240.70 (n/a)</td><td>157.79 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.01 <b>(-45.10%)</b></td><td>0.01 <b>(-27.65%)</b></td><td>0.01 (-6.73%)</td><td>0.01 (-2.37%)</td><td>0.00 <b>(-79.12%)</b></td><td>552.40 (+2.43%)</td><td>459.74 <b>(+24.12%)</b></td><td>445.40 (+7.22%)</td><td>408.10 <b>(+82.19%)</b></td><td>56.61 <b>(-58.09%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>539.30 (n/a)</td><td>370.40 (n/a)</td><td>415.40 (n/a)</td><td>224.00 (n/a)</td><td>135.08 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (-10.18%)</td><td>0.01 (+7.25%)</td><td>0.01 (-5.93%)</td><td>0.01 (+3.57%)</td><td>0.01 (-0.34%)</td><td>589.90 (-3.45%)</td><td>429.26 (-6.32%)</td><td>491.00 (+6.32%)</td><td>273.70 (+11.31%)</td><td>146.24 (+2.29%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.00 (n/a)</td><td>458.24 (n/a)</td><td>461.80 (n/a)</td><td>245.90 (n/a)</td><td>142.97 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (-7.45%)</td><td>0.01 <b>(-27.46%)</b></td><td>0.01 <b>(-37.09%)</b></td><td>0.01 <b>(-23.22%)</b></td><td>0.00 (+1.03%)</td><td>699.90 <b>(+30.24%)</b></td><td>542.60 <b>(+41.16%)</b></td><td>554.80 <b>(+58.97%)</b></td><td>288.60 (+8.05%)</td><td>158.04 <b>(+34.19%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.40 (n/a)</td><td>384.40 (n/a)</td><td>349.00 (n/a)</td><td>267.10 (n/a)</td><td>117.77 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.01 <b>(-51.89%)</b></td><td>0.01 <b>(-36.96%)</b></td><td>0.01 (-19.72%)</td><td>0.01 (-3.55%)</td><td>0.00 <b>(-75.94%)</b></td><td>564.10 (+3.69%)</td><td>495.88 <b>(+36.13%)</b></td><td>518.80 <b>(+24.56%)</b></td><td>364.70 <b>(+107.92%)</b></td><td>79.41 <b>(-48.26%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.00 (n/a)</td><td>364.28 (n/a)</td><td>416.50 (n/a)</td><td>175.40 (n/a)</td><td>153.47 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1938.00 (n/a)</td><td>719.22 (n/a)</td><td>464.50 (n/a)</td><td>285.50 (n/a)</td><td>690.25 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>797.00 (n/a)</td><td>536.38 (n/a)</td><td>502.70 (n/a)</td><td>336.80 (n/a)</td><td>166.23 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.30 (n/a)</td><td>405.74 (n/a)</td><td>477.70 (n/a)</td><td>237.90 (n/a)</td><td>133.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>467.30 (n/a)</td><td>366.20 (n/a)</td><td>370.90 (n/a)</td><td>273.80 (n/a)</td><td>75.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>630.60 (n/a)</td><td>410.34 (n/a)</td><td>382.20 (n/a)</td><td>294.60 (n/a)</td><td>135.69 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>586.50 (n/a)</td><td>488.44 (n/a)</td><td>534.90 (n/a)</td><td>247.90 (n/a)</td><td>137.64 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>541.80 (n/a)</td><td>436.70 (n/a)</td><td>427.60 (n/a)</td><td>305.80 (n/a)</td><td>94.33 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.00 (n/a)</td><td>442.48 (n/a)</td><td>482.60 (n/a)</td><td>302.00 (n/a)</td><td>108.31 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.20 (n/a)</td><td>369.96 (n/a)</td><td>318.90 (n/a)</td><td>235.80 (n/a)</td><td>145.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.80 (n/a)</td><td>423.70 (n/a)</td><td>485.60 (n/a)</td><td>243.70 (n/a)</td><td>133.40 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1401.20 (n/a)</td><td>619.40 (n/a)</td><td>502.90 (n/a)</td><td>317.10 (n/a)</td><td>446.33 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.60 (n/a)</td><td>477.08 (n/a)</td><td>512.50 (n/a)</td><td>307.10 (n/a)</td><td>151.74 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.47 (-14.69%)</td><td>0.34 (-12.62%)</td><td>0.33 (-12.84%)</td><td>0.12 <b>(-54.14%)</b></td><td>0.14 <b>(+27.20%)</b></td><td>1812.50 <b>(+118.03%)</b></td><td>825.48 <b>(+36.26%)</b></td><td>663.20 (+14.74%)</td><td>467.50 (+17.23%)</td><td>558.76 <b>(+256.45%)</b></td><td>20.18 (-14.69%)</td><td>14.40 (-12.62%)</td><td>14.23 (-12.84%)</td><td>5.21 <b>(-54.14%)</b></td><td>5.76 <b>(+27.20%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.55 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>831.30 (n/a)</td><td>605.80 (n/a)</td><td>578.00 (n/a)</td><td>398.80 (n/a)</td><td>156.76 (n/a)</td><td>23.66 (n/a)</td><td>16.48 (n/a)</td><td>16.33 (n/a)</td><td>11.35 (n/a)</td><td>4.53 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.69 (+19.23%)</td><td>0.38 (-10.50%)</td><td>0.36 (-12.20%)</td><td>0.18 <b>(-48.65%)</b></td><td>0.19 <b>(+107.93%)</b></td><td>1247.30 <b>(+94.77%)</b></td><td>691.36 <b>(+30.12%)</b></td><td>614.30 (+13.91%)</td><td>321.70 (-16.14%)</td><td>338.62 <b>(+249.07%)</b></td><td>29.33 (+19.23%)</td><td>16.39 (-10.50%)</td><td>15.36 (-12.20%)</td><td>7.57 <b>(-48.65%)</b></td><td>7.93 <b>(+107.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>640.40 (n/a)</td><td>531.32 (n/a)</td><td>539.30 (n/a)</td><td>383.60 (n/a)</td><td>97.01 (n/a)</td><td>24.60 (n/a)</td><td>18.31 (n/a)</td><td>17.50 (n/a)</td><td>14.74 (n/a)</td><td>3.82 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.31 (-0.20%)</td><td>0.31 (+0.51%)</td><td>0.31 (+1.15%)</td><td>0.30 (+0.22%)</td><td>0.01 (-3.99%)</td><td>84742.00 (-0.22%)</td><td>82012.86 (-0.51%)</td><td>80980.30 (-1.13%)</td><td>80529.20 (+0.20%)</td><td>1806.57 (-4.19%)</td><td>213.34 (-0.20%)</td><td>209.56 (+0.51%)</td><td>212.15 (+1.15%)</td><td>202.73 (+0.22%)</td><td>4.55 (-3.99%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84928.90 (n/a)</td><td>82433.06 (n/a)</td><td>81908.60 (n/a)</td><td>80371.30 (n/a)</td><td>1885.54 (n/a)</td><td>213.76 (n/a)</td><td>208.50 (n/a)</td><td>209.74 (n/a)</td><td>202.29 (n/a)</td><td>4.74 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>1.03 (+0.35%)</td><td>1.01 (-0.72%)</td><td>1.01 (-1.58%)</td><td>0.98 (-2.06%)</td><td>0.02 <b>(+50.51%)</b></td><td>25808.10 (+2.11%)</td><td>24897.86 (+0.75%)</td><td>24864.60 (+1.61%)</td><td>24346.50 (-0.35%)</td><td>571.48 <b>(+53.59%)</b></td><td>705.64 (+0.35%)</td><td>690.30 (-0.72%)</td><td>690.94 (-1.58%)</td><td>665.68 (-2.06%)</td><td>15.60 <b>(+50.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>0.02 (n/a)</td><td>25275.20 (n/a)</td><td>24711.74 (n/a)</td><td>24470.90 (n/a)</td><td>24431.70 (n/a)</td><td>372.08 (n/a)</td><td>703.18 (n/a)</td><td>695.34 (n/a)</td><td>702.05 (n/a)</td><td>679.71 (n/a)</td><td>10.37 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>3.40 <b>(+91.75%)</b></td><td>2.09 <b>(+30.91%)</b></td><td>1.87 (+11.79%)</td><td>1.37 (+3.05%)</td><td>0.77 <b>(+349.94%)</b></td><td>5872.20 (-2.96%)</td><td>4211.72 (-17.33%)</td><td>4317.10 (-10.54%)</td><td>2373.20 <b>(-47.85%)</b></td><td>1268.53 <b>(+113.65%)</b></td><td>890.75 <b>(+91.75%)</b></td><td>548.72 <b>(+30.91%)</b></td><td>489.66 (+11.79%)</td><td>359.99 (+3.05%)</td><td>202.80 <b>(+349.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>1.77 (n/a)</td><td>1.60 (n/a)</td><td>1.67 (n/a)</td><td>1.33 (n/a)</td><td>0.17 (n/a)</td><td>6051.40 (n/a)</td><td>5094.42 (n/a)</td><td>4826.00 (n/a)</td><td>4550.60 (n/a)</td><td>593.74 (n/a)</td><td>464.54 (n/a)</td><td>419.14 (n/a)</td><td>438.03 (n/a)</td><td>349.33 (n/a)</td><td>45.07 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.25 (-12.36%)</td><td>0.20 (-1.84%)</td><td>0.19 (-2.94%)</td><td>0.15 (+3.93%)</td><td>0.04 (-15.54%)</td><td>8135.70 (-3.78%)</td><td>6428.68 (+0.99%)</td><td>6492.90 (+3.03%)</td><td>4966.40 (+14.10%)</td><td>1359.46 (-7.05%)</td><td>13.51 (-12.36%)</td><td>10.83 (-1.84%)</td><td>10.34 (-2.94%)</td><td>8.25 (+3.93%)</td><td>2.30 (-15.54%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>8455.20 (n/a)</td><td>6365.72 (n/a)</td><td>6301.70 (n/a)</td><td>4352.70 (n/a)</td><td>1462.54 (n/a)</td><td>15.42 (n/a)</td><td>11.03 (n/a)</td><td>10.65 (n/a)</td><td>7.94 (n/a)</td><td>2.73 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>3.70 (n/a)</td><td>3.52 (n/a)</td><td>3.54 (n/a)</td><td>3.40 (n/a)</td><td>0.12 (n/a)</td><td>3.69 (n/a)</td><td>3.52 (n/a)</td><td>3.54 (n/a)</td><td>3.40 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>7.32 (-3.93%)</td><td>6.34 (+3.68%)</td><td>6.05 (+6.12%)</td><td>5.67 (+0.70%)</td><td>0.77 (-9.84%)</td><td>7.32 (-3.93%)</td><td>6.34 (+3.68%)</td><td>6.05 (+6.12%)</td><td>5.67 (+0.70%)</td><td>0.77 (-9.84%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>7.62 (n/a)</td><td>6.12 (n/a)</td><td>5.70 (n/a)</td><td>5.63 (n/a)</td><td>0.85 (n/a)</td><td>7.62 (n/a)</td><td>6.11 (n/a)</td><td>5.70 (n/a)</td><td>5.63 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>13.10 (-2.06%)</td><td>8.95 (-5.65%)</td><td>8.10 (-4.93%)</td><td>7.43 (-12.22%)</td><td>2.34 (+7.62%)</td><td>13.09 (-2.06%)</td><td>8.94 (-5.65%)</td><td>8.10 (-4.93%)</td><td>7.42 (-12.22%)</td><td>2.34 (+7.62%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>13.37 (n/a)</td><td>9.48 (n/a)</td><td>8.52 (n/a)</td><td>8.46 (n/a)</td><td>2.17 (n/a)</td><td>13.36 (n/a)</td><td>9.48 (n/a)</td><td>8.52 (n/a)</td><td>8.45 (n/a)</td><td>2.17 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>3.79 (n/a)</td><td>3.60 (n/a)</td><td>3.57 (n/a)</td><td>3.36 (n/a)</td><td>0.19 (n/a)</td><td>3.79 (n/a)</td><td>3.60 (n/a)</td><td>3.57 (n/a)</td><td>3.35 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>7.23 (-4.09%)</td><td>6.57 (-4.68%)</td><td>7.01 (+0.01%)</td><td>5.63 (-5.49%)</td><td>0.74 <b>(+21.55%)</b></td><td>7.23 (-4.09%)</td><td>6.56 (-4.68%)</td><td>7.01 (+0.01%)</td><td>5.62 (-5.49%)</td><td>0.74 <b>(+21.55%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>7.54 (n/a)</td><td>6.89 (n/a)</td><td>7.01 (n/a)</td><td>5.95 (n/a)</td><td>0.61 (n/a)</td><td>7.53 (n/a)</td><td>6.88 (n/a)</td><td>7.01 (n/a)</td><td>5.95 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>14.11 (-0.29%)</td><td>12.17 (+11.69%)</td><td>13.39 <b>(+43.15%)</b></td><td>7.48 (-12.14%)</td><td>2.68 (-6.65%)</td><td>14.10 (-0.29%)</td><td>12.16 (+11.69%)</td><td>13.38 <b>(+43.15%)</b></td><td>7.48 (-12.14%)</td><td>2.68 (-6.65%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>14.15 (n/a)</td><td>10.89 (n/a)</td><td>9.35 (n/a)</td><td>8.51 (n/a)</td><td>2.88 (n/a)</td><td>14.14 (n/a)</td><td>10.89 (n/a)</td><td>9.35 (n/a)</td><td>8.51 (n/a)</td><td>2.87 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.91 (-13.92%)</td><td>2.09 (-0.94%)</td><td>2.74 <b>(+80.61%)</b></td><td>0.99 (-15.16%)</td><td>0.98 (-11.54%)</td><td>2.91 (-13.92%)</td><td>2.08 (-0.94%)</td><td>2.74 <b>(+80.61%)</b></td><td>0.99 (-15.16%)</td><td>0.98 (-11.54%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>3.38 (n/a)</td><td>2.11 (n/a)</td><td>1.52 (n/a)</td><td>1.17 (n/a)</td><td>1.11 (n/a)</td><td>3.38 (n/a)</td><td>2.10 (n/a)</td><td>1.51 (n/a)</td><td>1.17 (n/a)</td><td>1.11 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.50 (-18.01%)</td><td>0.43 (+18.31%)</td><td>0.47 <b>(+41.14%)</b></td><td>0.34 <b>(+347.36%)</b></td><td>0.08 <b>(-62.57%)</b></td><td>0.49 (-18.01%)</td><td>0.42 (+18.31%)</td><td>0.46 <b>(+41.14%)</b></td><td>0.33 <b>(+347.36%)</b></td><td>0.07 <b>(-62.57%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.61 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.60 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.60 <b>(-21.70%)</b></td><td>0.34 (-10.37%)</td><td>0.37 <b>(+35.45%)</b></td><td>0.08 (+2.29%)</td><td>0.23 <b>(-32.52%)</b></td><td>0.59 <b>(-21.70%)</b></td><td>0.34 (-10.37%)</td><td>0.37 <b>(+35.45%)</b></td><td>0.07 (+2.29%)</td><td>0.23 <b>(-32.52%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.76 (n/a)</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>0.34 (n/a)</td><td>0.75 (n/a)</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.39 (-2.83%)</td><td>1.49 (+0.59%)</td><td>1.83 <b>(+39.27%)</b></td><td>0.50 (+11.79%)</td><td>0.82 (-8.17%)</td><td>2.35 (-2.83%)</td><td>1.47 (+0.59%)</td><td>1.80 <b>(+39.27%)</b></td><td>0.49 (+11.79%)</td><td>0.81 (-8.17%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>2.46 (n/a)</td><td>1.48 (n/a)</td><td>1.31 (n/a)</td><td>0.45 (n/a)</td><td>0.90 (n/a)</td><td>2.42 (n/a)</td><td>1.46 (n/a)</td><td>1.29 (n/a)</td><td>0.44 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.80 (n/a)</td><td>391.34 (n/a)</td><td>411.90 (n/a)</td><td>232.90 (n/a)</td><td>124.78 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.30 (n/a)</td><td>431.68 (n/a)</td><td>497.60 (n/a)</td><td>296.00 (n/a)</td><td>125.65 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.00 (n/a)</td><td>419.28 (n/a)</td><td>471.40 (n/a)</td><td>280.20 (n/a)</td><td>126.09 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.20 (n/a)</td><td>366.22 (n/a)</td><td>287.90 (n/a)</td><td>262.30 (n/a)</td><td>125.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>993.00 (n/a)</td><td>474.68 (n/a)</td><td>410.70 (n/a)</td><td>233.00 (n/a)</td><td>305.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2440.20 (n/a)</td><td>918.80 (n/a)</td><td>616.90 (n/a)</td><td>433.80 (n/a)</td><td>854.39 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (+4.54%)</td><td>0.03 (+5.16%)</td><td>0.03 (+11.04%)</td><td>0.01 (-4.73%)</td><td>0.01 <b>(+20.88%)</b></td><td>564.70 (+4.96%)</td><td>349.64 (-1.01%)</td><td>249.00 (-9.91%)</td><td>230.70 (-4.35%)</td><td>155.53 (+17.59%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.00 (n/a)</td><td>353.20 (n/a)</td><td>276.40 (n/a)</td><td>241.20 (n/a)</td><td>132.26 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (-12.25%)</td><td>0.02 (-19.76%)</td><td>0.02 <b>(-46.61%)</b></td><td>0.01 (-18.41%)</td><td>0.01 (-6.50%)</td><td>578.60 <b>(+22.58%)</b></td><td>417.84 <b>(+25.83%)</b></td><td>481.90 <b>(+87.29%)</b></td><td>257.90 (+13.96%)</td><td>149.74 (+17.29%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>472.00 (n/a)</td><td>332.06 (n/a)</td><td>257.30 (n/a)</td><td>226.30 (n/a)</td><td>127.67 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (+19.81%)</td><td>0.02 (+13.14%)</td><td>0.03 <b>(+41.13%)</b></td><td>0.02 (-0.59%)</td><td>0.01 (+16.24%)</td><td>529.80 (+0.59%)</td><td>361.68 (-10.39%)</td><td>298.60 <b>(-29.14%)</b></td><td>229.70 (-16.53%)</td><td>126.08 (+2.99%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.70 (n/a)</td><td>403.60 (n/a)</td><td>421.40 (n/a)</td><td>275.20 (n/a)</td><td>122.43 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 <b>(+111.83%)</b></td><td>0.03 <b>(+112.25%)</b></td><td>0.03 <b>(+108.69%)</b></td><td>0.03 <b>(+117.66%)</b></td><td>0.00 <b>(+81.08%)</b></td><td>274.90 <b>(-54.05%)</b></td><td>252.22 <b>(-52.95%)</b></td><td>252.20 <b>(-52.09%)</b></td><td>230.30 <b>(-52.79%)</b></td><td>16.25 <b>(-60.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.30 (n/a)</td><td>536.10 (n/a)</td><td>526.40 (n/a)</td><td>487.80 (n/a)</td><td>41.65 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 <b>(+75.58%)</b></td><td>0.03 <b>(+90.96%)</b></td><td>0.03 <b>(+97.20%)</b></td><td>0.02 <b>(+97.29%)</b></td><td>0.01 <b>(+76.00%)</b></td><td>533.70 <b>(-49.31%)</b></td><td>332.90 <b>(-48.16%)</b></td><td>283.20 <b>(-49.29%)</b></td><td>275.00 <b>(-43.05%)</b></td><td>112.42 <b>(-51.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1052.90 (n/a)</td><td>642.18 (n/a)</td><td>558.50 (n/a)</td><td>482.90 (n/a)</td><td>231.93 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 <b>(+21.05%)</b></td><td>0.02 (+11.02%)</td><td>0.02 (-5.34%)</td><td>0.01 <b>(+140.16%)</b></td><td>0.01 (+2.71%)</td><td>805.50 <b>(-58.36%)</b></td><td>516.98 <b>(-30.63%)</b></td><td>502.80 (+5.63%)</td><td>242.60 (-17.37%)</td><td>199.97 <b>(-70.38%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1934.50 (n/a)</td><td>745.24 (n/a)</td><td>476.00 (n/a)</td><td>293.60 (n/a)</td><td>675.15 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 <b>(+54.99%)</b></td><td>0.02 <b>(+21.30%)</b></td><td>0.02 (-9.37%)</td><td>0.01 (-8.29%)</td><td>0.01 <b>(+195.94%)</b></td><td>603.50 (+9.03%)</td><td>438.32 (-8.14%)</td><td>521.80 (+10.34%)</td><td>233.70 <b>(-35.48%)</b></td><td>158.38 <b>(+108.26%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.50 (n/a)</td><td>477.16 (n/a)</td><td>472.90 (n/a)</td><td>362.20 (n/a)</td><td>76.05 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (+8.76%)</td><td>0.02 (-5.05%)</td><td>0.02 (-5.63%)</td><td>0.01 (-7.22%)</td><td>0.01 <b>(+24.38%)</b></td><td>605.70 (+7.78%)</td><td>470.80 (+7.70%)</td><td>482.40 (+5.98%)</td><td>272.40 (-8.04%)</td><td>124.05 (+17.13%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.00 (n/a)</td><td>437.12 (n/a)</td><td>455.20 (n/a)</td><td>296.20 (n/a)</td><td>105.91 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (+6.15%)</td><td>0.02 (+19.06%)</td><td>0.02 <b>(+39.65%)</b></td><td>0.01 <b>(+87.96%)</b></td><td>0.01 (+7.58%)</td><td>1083.40 <b>(-46.80%)</b></td><td>510.92 <b>(-30.00%)</b></td><td>338.10 <b>(-28.40%)</b></td><td>224.30 (-5.80%)</td><td>353.53 <b>(-52.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2036.40 (n/a)</td><td>729.88 (n/a)</td><td>472.20 (n/a)</td><td>238.10 (n/a)</td><td>736.82 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (-3.75%)</td><td>0.02 (+11.10%)</td><td>0.02 <b>(+29.81%)</b></td><td>0.01 (-9.07%)</td><td>0.01 (-4.94%)</td><td>565.60 (+10.00%)</td><td>379.44 (-9.63%)</td><td>364.00 <b>(-22.96%)</b></td><td>240.20 (+3.89%)</td><td>127.67 (+12.51%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.20 (n/a)</td><td>419.86 (n/a)</td><td>472.50 (n/a)</td><td>231.20 (n/a)</td><td>113.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (+7.20%)</td><td>0.03 (+10.87%)</td><td>0.03 (+1.26%)</td><td>0.02 (+18.47%)</td><td>0.01 <b>(-24.06%)</b></td><td>455.80 (-15.59%)</td><td>320.84 (-15.22%)</td><td>289.40 (-1.23%)</td><td>240.90 (-6.74%)</td><td>86.22 <b>(-41.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.00 (n/a)</td><td>378.42 (n/a)</td><td>293.00 (n/a)</td><td>258.30 (n/a)</td><td>147.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (-11.58%)</td><td>0.02 (+8.79%)</td><td>0.03 <b>(+48.53%)</b></td><td>0.02 <b>(+27.36%)</b></td><td>0.01 <b>(-39.34%)</b></td><td>506.70 <b>(-21.49%)</b></td><td>356.84 (-18.76%)</td><td>315.40 <b>(-32.66%)</b></td><td>241.70 (+13.10%)</td><td>105.02 <b>(-45.82%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.40 (n/a)</td><td>439.24 (n/a)</td><td>468.40 (n/a)</td><td>213.70 (n/a)</td><td>193.83 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 <b>(+35.91%)</b></td><td>0.03 <b>(+24.48%)</b></td><td>0.02 (+14.89%)</td><td>0.02 <b>(+38.90%)</b></td><td>0.01 <b>(+43.86%)</b></td><td>451.30 <b>(-28.01%)</b></td><td>358.58 (-18.79%)</td><td>412.40 (-12.96%)</td><td>202.80 <b>(-26.44%)</b></td><td>106.03 <b>(-21.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.90 (n/a)</td><td>441.52 (n/a)</td><td>473.80 (n/a)</td><td>275.70 (n/a)</td><td>135.13 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 <b>(+30.33%)</b></td><td>0.02 (+7.77%)</td><td>0.02 (-14.48%)</td><td>0.01 (+7.47%)</td><td>0.01 <b>(+81.37%)</b></td><td>632.60 (-6.96%)</td><td>484.60 (-2.45%)</td><td>526.60 (+16.94%)</td><td>303.80 <b>(-23.28%)</b></td><td>150.60 <b>(+30.01%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>679.90 (n/a)</td><td>496.76 (n/a)</td><td>450.30 (n/a)</td><td>396.00 (n/a)</td><td>115.84 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (-3.89%)</td><td>0.02 (-13.61%)</td><td>0.02 <b>(-25.83%)</b></td><td>0.01 (-19.18%)</td><td>0.01 (-6.20%)</td><td>636.80 <b>(+23.75%)</b></td><td>406.98 (+17.15%)</td><td>352.30 <b>(+34.83%)</b></td><td>247.20 (+4.04%)</td><td>168.34 <b>(+20.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.60 (n/a)</td><td>347.40 (n/a)</td><td>261.30 (n/a)</td><td>237.60 (n/a)</td><td>139.66 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.05 (+2.96%)</td><td>0.03 (-9.91%)</td><td>0.02 <b>(-50.79%)</b></td><td>0.02 <b>(+63.19%)</b></td><td>0.01 (-16.27%)</td><td>564.70 <b>(-38.73%)</b></td><td>435.98 (-2.84%)</td><td>543.40 <b>(+103.22%)</b></td><td>239.00 (-2.89%)</td><td>162.23 <b>(-44.91%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>921.60 (n/a)</td><td>448.72 (n/a)</td><td>267.40 (n/a)</td><td>246.10 (n/a)</td><td>294.49 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (-6.23%)</td><td>0.02 (+8.36%)</td><td>0.03 <b>(+48.83%)</b></td><td>0.01 <b>(+94.03%)</b></td><td>0.01 (-2.69%)</td><td>1032.30 <b>(-48.46%)</b></td><td>492.82 <b>(-27.63%)</b></td><td>281.90 <b>(-32.82%)</b></td><td>244.40 (+6.63%)</td><td>341.30 <b>(-54.16%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2003.00 (n/a)</td><td>680.98 (n/a)</td><td>419.60 (n/a)</td><td>229.20 (n/a)</td><td>744.59 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 <b>(-38.49%)</b></td><td>0.02 <b>(-28.74%)</b></td><td>0.02 (-5.58%)</td><td>0.00 <b>(-70.85%)</b></td><td>0.01 <b>(-29.58%)</b></td><td>2399.80 <b>(+243.07%)</b></td><td>801.70 <b>(+96.35%)</b></td><td>415.90 (+5.91%)</td><td>309.20 <b>(+62.57%)</b></td><td>896.79 <b>(+345.76%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>699.50 (n/a)</td><td>408.30 (n/a)</td><td>392.70 (n/a)</td><td>190.20 (n/a)</td><td>201.18 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 <b>(-21.84%)</b></td><td>0.02 <b>(-27.10%)</b></td><td>0.02 <b>(-37.06%)</b></td><td>0.01 (+6.56%)</td><td>0.01 <b>(-42.41%)</b></td><td>572.90 (-6.16%)</td><td>458.72 <b>(+24.58%)</b></td><td>464.80 <b>(+58.85%)</b></td><td>275.60 <b>(+27.95%)</b></td><td>114.66 <b>(-33.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.50 (n/a)</td><td>368.20 (n/a)</td><td>292.60 (n/a)</td><td>215.40 (n/a)</td><td>172.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.04 (-16.77%)</td><td>0.03 (-4.74%)</td><td>0.03 (+2.51%)</td><td>0.02 (+15.20%)</td><td>0.01 <b>(-28.43%)</b></td><td>478.80 (-13.20%)</td><td>360.34 (+0.72%)</td><td>303.60 (-2.44%)</td><td>280.10 <b>(+20.16%)</b></td><td>94.58 <b>(-26.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.60 (n/a)</td><td>357.76 (n/a)</td><td>311.20 (n/a)</td><td>233.10 (n/a)</td><td>127.93 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.02 <b>(-25.59%)</b></td><td>0.02 <b>(-31.42%)</b></td><td>0.02 <b>(-35.22%)</b></td><td>0.00 <b>(-73.34%)</b></td><td>0.01 (+5.79%)</td><td>1977.00 <b>(+275.07%)</b></td><td>731.48 <b>(+100.24%)</b></td><td>448.90 <b>(+54.37%)</b></td><td>360.80 <b>(+34.38%)</b></td><td>697.31 <b>(+497.15%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.10 (n/a)</td><td>365.30 (n/a)</td><td>290.80 (n/a)</td><td>268.50 (n/a)</td><td>116.77 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 <b>(-35.68%)</b></td><td>0.02 (-11.21%)</td><td>0.02 <b>(+30.47%)</b></td><td>0.01 (-1.57%)</td><td>0.01 <b>(-46.16%)</b></td><td>637.40 (+1.61%)</td><td>458.58 (+4.49%)</td><td>378.40 <b>(-23.35%)</b></td><td>297.10 <b>(+55.47%)</b></td><td>161.07 (-3.31%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.30 (n/a)</td><td>438.88 (n/a)</td><td>493.70 (n/a)</td><td>191.10 (n/a)</td><td>166.58 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (+6.58%)</td><td>0.02 (-11.38%)</td><td>0.02 <b>(-21.22%)</b></td><td>0.01 <b>(-50.60%)</b></td><td>0.01 <b>(+49.23%)</b></td><td>1058.60 <b>(+102.45%)</b></td><td>532.02 <b>(+32.87%)</b></td><td>468.60 <b>(+26.92%)</b></td><td>245.40 (-6.16%)</td><td>312.43 <b>(+186.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.90 (n/a)</td><td>400.40 (n/a)</td><td>369.20 (n/a)</td><td>261.50 (n/a)</td><td>109.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (-16.96%)</td><td>0.02 (-17.70%)</td><td>0.02 (-4.58%)</td><td>0.00 <b>(-75.60%)</b></td><td>0.01 <b>(+21.83%)</b></td><td>2030.30 <b>(+309.83%)</b></td><td>736.12 <b>(+80.87%)</b></td><td>464.70 (+4.80%)</td><td>276.00 <b>(+20.42%)</b></td><td>731.56 <b>(+606.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.40 (n/a)</td><td>406.98 (n/a)</td><td>443.40 (n/a)</td><td>229.20 (n/a)</td><td>103.61 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.03 (-11.73%)</td><td>0.02 (-4.95%)</td><td>0.02 (-8.72%)</td><td>0.01 (-12.04%)</td><td>0.01 (-1.74%)</td><td>604.80 (+13.68%)</td><td>464.20 (+6.86%)</td><td>491.20 (+9.55%)</td><td>304.20 (+13.30%)</td><td>137.52 <b>(+27.11%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.00 (n/a)</td><td>434.40 (n/a)</td><td>448.40 (n/a)</td><td>268.50 (n/a)</td><td>108.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.40 (-19.03%)</td><td>0.24 <b>(-25.34%)</b></td><td>0.17 <b>(-43.85%)</b></td><td>0.15 <b>(-32.06%)</b></td><td>0.12 (+16.61%)</td><td>675.30 <b>(+47.19%)</b></td><td>486.30 <b>(+49.67%)</b></td><td>576.70 <b>(+78.10%)</b></td><td>245.50 <b>(+23.55%)</b></td><td>206.72 <b>(+119.61%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>458.80 (n/a)</td><td>324.92 (n/a)</td><td>323.80 (n/a)</td><td>198.70 (n/a)</td><td>94.13 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.40 (-1.56%)</td><td>0.22 (-18.22%)</td><td>0.24 (-12.78%)</td><td>0.05 <b>(-69.16%)</b></td><td>0.13 <b>(+30.84%)</b></td><td>2091.60 <b>(+224.28%)</b></td><td>742.82 <b>(+83.72%)</b></td><td>413.10 (+14.65%)</td><td>243.90 (+1.58%)</td><td>764.26 <b>(+379.05%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>645.00 (n/a)</td><td>404.32 (n/a)</td><td>360.30 (n/a)</td><td>240.10 (n/a)</td><td>159.54 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.37 <b>(+43.97%)</b></td><td>0.27 <b>(+21.78%)</b></td><td>0.31 <b>(+45.34%)</b></td><td>0.14 <b>(-27.26%)</b></td><td>0.10 <b>(+241.03%)</b></td><td>696.80 <b>(+37.49%)</b></td><td>413.90 (-7.50%)</td><td>321.70 <b>(-31.19%)</b></td><td>263.00 <b>(-30.53%)</b></td><td>182.17 <b>(+227.95%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>506.80 (n/a)</td><td>447.44 (n/a)</td><td>467.50 (n/a)</td><td>378.60 (n/a)</td><td>55.55 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.24 (-17.38%)</td><td>0.18 <b>(-29.55%)</b></td><td>0.16 <b>(-37.92%)</b></td><td>0.14 <b>(-30.47%)</b></td><td>0.04 (+10.03%)</td><td>509.50 <b>(+43.80%)</b></td><td>427.10 <b>(+44.50%)</b></td><td>465.80 <b>(+61.07%)</b></td><td>309.10 <b>(+21.03%)</b></td><td>82.47 <b>(+93.88%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>354.30 (n/a)</td><td>295.58 (n/a)</td><td>289.20 (n/a)</td><td>255.40 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.31 <b>(-23.34%)</b></td><td>0.23 (-13.37%)</td><td>0.25 (-2.68%)</td><td>0.13 (-6.01%)</td><td>0.07 <b>(-22.15%)</b></td><td>551.60 (+6.40%)</td><td>354.84 (+13.74%)</td><td>290.50 (+2.76%)</td><td>239.70 <b>(+30.48%)</b></td><td>130.03 (+4.82%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.40 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>518.40 (n/a)</td><td>311.98 (n/a)</td><td>282.70 (n/a)</td><td>183.70 (n/a)</td><td>124.05 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.28 (-11.52%)</td><td>0.19 (-14.26%)</td><td>0.17 <b>(-31.07%)</b></td><td>0.13 <b>(+20.53%)</b></td><td>0.06 <b>(-24.94%)</b></td><td>575.60 (-17.02%)</td><td>426.74 (+9.12%)</td><td>439.20 <b>(+45.09%)</b></td><td>265.70 (+13.06%)</td><td>125.95 <b>(-31.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>693.70 (n/a)</td><td>391.06 (n/a)</td><td>302.70 (n/a)</td><td>235.00 (n/a)</td><td>185.06 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.42 (+5.97%)</td><td>0.32 (+11.57%)</td><td>0.29 (+9.71%)</td><td>0.22 (-9.47%)</td><td>0.09 <b>(+52.15%)</b></td><td>598.10 (+10.45%)</td><td>438.72 (-6.73%)</td><td>451.90 (-8.85%)</td><td>311.40 (-5.64%)</td><td>127.09 <b>(+56.27%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>541.50 (n/a)</td><td>470.38 (n/a)</td><td>495.80 (n/a)</td><td>330.00 (n/a)</td><td>81.33 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.46 (+6.53%)</td><td>0.42 <b>(+80.53%)</b></td><td>0.45 <b>(+76.37%)</b></td><td>0.33 <b>(+436.39%)</b></td><td>0.05 <b>(-62.13%)</b></td><td>394.50 <b>(-81.36%)</b></td><td>315.34 <b>(-62.79%)</b></td><td>293.80 <b>(-43.30%)</b></td><td>286.50 (-6.13%)</td><td>44.96 <b>(-93.84%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.43 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>0.14 (n/a)</td><td>2116.00 (n/a)</td><td>847.44 (n/a)</td><td>518.20 (n/a)</td><td>305.20 (n/a)</td><td>729.45 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.42 <b>(-27.71%)</b></td><td>0.33 (+19.64%)</td><td>0.38 <b>(+48.01%)</b></td><td>0.22 <b>(+219.34%)</b></td><td>0.10 <b>(-49.58%)</b></td><td>596.70 <b>(-68.69%)</b></td><td>428.46 <b>(-43.36%)</b></td><td>348.60 <b>(-32.44%)</b></td><td>310.20 <b>(+38.30%)</b></td><td>137.53 <b>(-79.20%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.58 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.19 (n/a)</td><td>1905.50 (n/a)</td><td>756.44 (n/a)</td><td>516.00 (n/a)</td><td>224.30 (n/a)</td><td>661.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-31.82%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.94%)</b></td><td>21712.14 (+9.09%)</td><td>16144.40 <b>(+39.35%)</b></td><td>17033.02 <b>(+147.23%)</b></td><td>6686.30 (+3.94%)</td><td>5703.09 (-15.74%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19902.07 (n/a)</td><td>11585.89 (n/a)</td><td>6889.62 (n/a)</td><td>6432.76 (n/a)</td><td>6768.42 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.00 (+18.18%)</td><td>0.00 (+6.82%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 (+3.59%)</td><td>18057.08 (-1.81%)</td><td>9912.12 (-5.25%)</td><td>8636.04 (-6.39%)</td><td>6534.86 (-13.04%)</td><td>4648.17 (+2.78%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18390.82 (n/a)</td><td>10461.10 (n/a)</td><td>9225.85 (n/a)</td><td>7514.47 (n/a)</td><td>4522.32 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>0.14 (+1.78%)</td><td>0.10 (+3.78%)</td><td>0.09 (+14.07%)</td><td>0.07 (-6.24%)</td><td>0.03 (+2.49%)</td><td>30330.61 (+6.55%)</td><td>21806.08 (-3.39%)</td><td>23305.98 (-12.27%)</td><td>14694.18 (-1.80%)</td><td>6701.26 (+2.54%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28464.85 (n/a)</td><td>22570.47 (n/a)</td><td>26564.40 (n/a)</td><td>14963.29 (n/a)</td><td>6535.06 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>1.60 (+1.51%)</td><td>1.21 <b>(+32.60%)</b></td><td>1.30 <b>(+82.47%)</b></td><td>0.63 (+3.99%)</td><td>0.42 (+6.19%)</td><td>836.40 (-3.84%)</td><td>492.46 <b>(-23.86%)</b></td><td>402.80 <b>(-45.19%)</b></td><td>327.70 (-1.47%)</td><td>213.70 (+2.29%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>1.58 (n/a)</td><td>0.91 (n/a)</td><td>0.71 (n/a)</td><td>0.60 (n/a)</td><td>0.39 (n/a)</td><td>869.80 (n/a)</td><td>646.82 (n/a)</td><td>734.90 (n/a)</td><td>332.60 (n/a)</td><td>208.91 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.81 <b>(+21.61%)</b></td><td>1.44 <b>(+34.67%)</b></td><td>1.25 <b>(+71.06%)</b></td><td>0.30 (+1.78%)</td><td>0.91 (+0.31%)</td><td>3475.00 (-1.75%)</td><td>1238.24 <b>(-35.26%)</b></td><td>839.10 <b>(-41.54%)</b></td><td>372.90 (-17.77%)</td><td>1265.09 (-16.92%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>2.31 (n/a)</td><td>1.07 (n/a)</td><td>0.73 (n/a)</td><td>0.30 (n/a)</td><td>0.90 (n/a)</td><td>3536.90 (n/a)</td><td>1912.70 (n/a)</td><td>1435.30 (n/a)</td><td>453.50 (n/a)</td><td>1522.80 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:50:28</td><td>2.16 (-12.46%)</td><td>1.43 <b>(+38.39%)</b></td><td>1.40 <b>(+90.19%)</b></td><td>0.90 <b>(+89.12%)</b></td><td>0.48 <b>(-40.67%)</b></td><td>584.20 <b>(-47.12%)</b></td><td>399.76 <b>(-41.79%)</b></td><td>373.50 <b>(-47.43%)</b></td><td>242.90 (+14.25%)</td><td>129.84 <b>(-59.01%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:23:15</td><td>2.47 (n/a)</td><td>1.03 (n/a)</td><td>0.74 (n/a)</td><td>0.47 (n/a)</td><td>0.81 (n/a)</td><td>1104.80 (n/a)</td><td>686.80 (n/a)</td><td>710.50 (n/a)</td><td>212.60 (n/a)</td><td>316.74 (n/a)</td>
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
