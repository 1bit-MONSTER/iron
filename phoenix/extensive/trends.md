# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 <b>(+54.12%)</b></td><td>0.02 <b>(+51.11%)</b></td><td>0.02 <b>(+81.14%)</b></td><td>0.01 (+19.84%)</td><td>0.00 <b>(+96.57%)</b></td><td>449.30 (-16.56%)</td><td>323.84 <b>(-32.05%)</b></td><td>289.60 <b>(-44.80%)</b></td><td>230.50 <b>(-35.13%)</b></td><td>84.59 (+7.24%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.50 (n/a)</td><td>476.56 (n/a)</td><td>524.60 (n/a)</td><td>355.30 (n/a)</td><td>78.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+12.41%)</td><td>0.02 (-8.97%)</td><td>0.01 <b>(-37.47%)</b></td><td>0.01 (+0.42%)</td><td>0.01 <b>(+47.65%)</b></td><td>526.90 (-0.42%)</td><td>405.54 (+16.88%)</td><td>487.40 <b>(+59.91%)</b></td><td>231.40 (-11.03%)</td><td>146.61 <b>(+32.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.10 (n/a)</td><td>346.98 (n/a)</td><td>304.80 (n/a)</td><td>260.10 (n/a)</td><td>110.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+5.63%)</td><td>0.02 (+3.70%)</td><td>0.02 (+17.66%)</td><td>0.01 (-13.31%)</td><td>0.01 <b>(+54.41%)</b></td><td>612.20 (+15.36%)</td><td>423.26 (+4.91%)</td><td>366.40 (-15.01%)</td><td>258.40 (-5.31%)</td><td>173.73 <b>(+78.76%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.70 (n/a)</td><td>403.44 (n/a)</td><td>431.10 (n/a)</td><td>272.90 (n/a)</td><td>97.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-4.16%)</td><td>0.02 (-14.21%)</td><td>0.01 <b>(-35.47%)</b></td><td>0.01 (-19.06%)</td><td>0.01 (+0.17%)</td><td>563.90 <b>(+23.55%)</b></td><td>391.80 (+18.34%)</td><td>429.20 <b>(+55.00%)</b></td><td>239.60 (+4.31%)</td><td>135.33 (+19.30%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>456.40 (n/a)</td><td>331.08 (n/a)</td><td>276.90 (n/a)</td><td>229.70 (n/a)</td><td>113.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-30.03%)</b></td><td>0.01 (-10.88%)</td><td>0.01 (-10.51%)</td><td>0.01 (-15.49%)</td><td>0.00 <b>(-35.25%)</b></td><td>590.50 (+18.31%)</td><td>469.14 (+9.92%)</td><td>520.20 (+11.73%)</td><td>347.20 <b>(+42.94%)</b></td><td>113.46 (+9.05%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>499.10 (n/a)</td><td>426.82 (n/a)</td><td>465.60 (n/a)</td><td>242.90 (n/a)</td><td>104.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-24.42%)</b></td><td>0.02 (+14.21%)</td><td>0.02 <b>(+33.38%)</b></td><td>0.01 <b>(+101.12%)</b></td><td>0.00 <b>(-48.09%)</b></td><td>531.60 <b>(-50.28%)</b></td><td>383.48 <b>(-28.43%)</b></td><td>337.40 <b>(-25.02%)</b></td><td>290.90 <b>(+32.29%)</b></td><td>106.05 <b>(-66.97%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1069.10 (n/a)</td><td>535.78 (n/a)</td><td>450.00 (n/a)</td><td>219.90 (n/a)</td><td>321.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (-14.71%)</td><td>0.04 (-0.08%)</td><td>0.05 (-2.17%)</td><td>0.02 (-4.69%)</td><td>0.01 <b>(-31.94%)</b></td><td>542.00 (+4.92%)</td><td>315.46 (-5.69%)</td><td>262.40 (+2.22%)</td><td>235.10 (+17.26%)</td><td>127.55 (-14.17%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>516.60 (n/a)</td><td>334.50 (n/a)</td><td>256.70 (n/a)</td><td>200.50 (n/a)</td><td>148.61 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (+14.94%)</td><td>0.05 <b>(+59.84%)</b></td><td>0.05 <b>(+128.56%)</b></td><td>0.05 <b>(+109.73%)</b></td><td>0.01 <b>(-64.41%)</b></td><td>272.40 <b>(-52.33%)</b></td><td>241.44 <b>(-45.12%)</b></td><td>239.40 <b>(-56.25%)</b></td><td>208.40 (-12.99%)</td><td>22.95 <b>(-85.92%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.40 (n/a)</td><td>439.94 (n/a)</td><td>547.20 (n/a)</td><td>239.50 (n/a)</td><td>162.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (-11.89%)</td><td>0.03 (-15.47%)</td><td>0.03 <b>(-28.17%)</b></td><td>0.02 (-12.20%)</td><td>0.01 (-16.81%)</td><td>601.00 (+13.89%)</td><td>420.14 (+16.13%)</td><td>420.20 <b>(+39.19%)</b></td><td>258.20 (+13.49%)</td><td>148.76 (+2.29%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.70 (n/a)</td><td>361.78 (n/a)</td><td>301.90 (n/a)</td><td>227.50 (n/a)</td><td>145.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (-3.39%)</td><td>0.04 <b>(+40.20%)</b></td><td>0.04 <b>(+101.03%)</b></td><td>0.04 <b>(+120.68%)</b></td><td>0.01 <b>(-63.24%)</b></td><td>341.20 <b>(-54.69%)</b></td><td>278.82 <b>(-41.65%)</b></td><td>282.60 <b>(-50.26%)</b></td><td>238.20 (+3.52%)</td><td>40.98 <b>(-81.78%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>753.10 (n/a)</td><td>477.86 (n/a)</td><td>568.20 (n/a)</td><td>230.10 (n/a)</td><td>224.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (-3.66%)</td><td>0.04 <b>(+34.10%)</b></td><td>0.03 <b>(+83.36%)</b></td><td>0.02 <b>(+27.67%)</b></td><td>0.01 <b>(-24.87%)</b></td><td>548.80 <b>(-21.67%)</b></td><td>378.98 <b>(-31.39%)</b></td><td>360.00 <b>(-45.47%)</b></td><td>249.00 (+3.79%)</td><td>119.79 <b>(-38.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>700.60 (n/a)</td><td>552.36 (n/a)</td><td>660.20 (n/a)</td><td>239.90 (n/a)</td><td>193.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (-19.47%)</td><td>0.03 (+10.23%)</td><td>0.03 <b>(+37.43%)</b></td><td>0.02 (-3.80%)</td><td>0.01 <b>(-24.90%)</b></td><td>594.50 (+3.95%)</td><td>423.36 (-11.51%)</td><td>380.30 <b>(-27.24%)</b></td><td>303.70 <b>(+24.16%)</b></td><td>132.65 (-0.51%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.90 (n/a)</td><td>478.44 (n/a)</td><td>522.70 (n/a)</td><td>244.60 (n/a)</td><td>133.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (+2.81%)</td><td>0.08 (+11.65%)</td><td>0.08 (-1.36%)</td><td>0.05 (+14.91%)</td><td>0.02 <b>(-21.01%)</b></td><td>536.10 (-12.97%)</td><td>330.10 (-15.25%)</td><td>300.00 (+1.39%)</td><td>247.00 (-2.76%)</td><td>117.52 <b>(-28.74%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>616.00 (n/a)</td><td>389.50 (n/a)</td><td>295.90 (n/a)</td><td>254.00 (n/a)</td><td>164.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (-2.08%)</td><td>0.06 (-12.03%)</td><td>0.07 (-8.98%)</td><td>0.01 <b>(-68.45%)</b></td><td>0.03 <b>(+37.80%)</b></td><td>1927.30 <b>(+216.94%)</b></td><td>656.00 <b>(+74.97%)</b></td><td>328.20 (+9.88%)</td><td>243.60 (+2.14%)</td><td>716.08 <b>(+381.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>608.10 (n/a)</td><td>374.92 (n/a)</td><td>298.70 (n/a)</td><td>238.50 (n/a)</td><td>148.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (-3.91%)</td><td>0.08 (+7.48%)</td><td>0.09 (+13.06%)</td><td>0.04 (-5.98%)</td><td>0.02 <b>(-20.07%)</b></td><td>646.90 (+6.36%)</td><td>352.76 (-9.86%)</td><td>288.50 (-11.56%)</td><td>247.00 (+4.04%)</td><td>165.55 (-3.39%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>608.20 (n/a)</td><td>391.34 (n/a)</td><td>326.20 (n/a)</td><td>237.40 (n/a)</td><td>171.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 <b>(-38.77%)</b></td><td>0.07 <b>(-25.32%)</b></td><td>0.08 (-7.45%)</td><td>0.04 <b>(-22.50%)</b></td><td>0.02 <b>(-40.65%)</b></td><td>571.30 <b>(+29.02%)</b></td><td>373.30 <b>(+31.43%)</b></td><td>300.70 (+8.05%)</td><td>242.30 <b>(+63.27%)</b></td><td>138.84 <b>(+32.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>442.80 (n/a)</td><td>284.04 (n/a)</td><td>278.30 (n/a)</td><td>148.40 (n/a)</td><td>104.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 <b>(+35.12%)</b></td><td>0.08 <b>(+21.76%)</b></td><td>0.07 <b>(+37.01%)</b></td><td>0.04 (-13.93%)</td><td>0.04 <b>(+65.68%)</b></td><td>611.30 (+16.19%)</td><td>384.14 (-9.54%)</td><td>344.80 <b>(-27.00%)</b></td><td>177.60 <b>(-26.00%)</b></td><td>170.22 <b>(+43.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>526.10 (n/a)</td><td>424.64 (n/a)</td><td>472.30 (n/a)</td><td>240.00 (n/a)</td><td>118.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (+9.96%)</td><td>0.07 <b>(+23.01%)</b></td><td>0.09 <b>(+53.25%)</b></td><td>0.04 (+5.21%)</td><td>0.03 <b>(+36.05%)</b></td><td>566.90 (-4.95%)</td><td>381.72 (-14.03%)</td><td>273.40 <b>(-34.75%)</b></td><td>240.70 (-9.03%)</td><td>164.03 <b>(+23.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>596.40 (n/a)</td><td>444.04 (n/a)</td><td>419.00 (n/a)</td><td>264.60 (n/a)</td><td>133.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 (+15.59%)</td><td>0.14 (+19.49%)</td><td>0.10 (+2.68%)</td><td>0.09 <b>(+110.60%)</b></td><td>0.05 (-3.67%)</td><td>538.20 <b>(-52.52%)</b></td><td>405.48 <b>(-27.09%)</b></td><td>473.70 (-2.61%)</td><td>241.60 (-13.47%)</td><td>140.73 <b>(-59.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>1133.50 (n/a)</td><td>556.10 (n/a)</td><td>486.40 (n/a)</td><td>279.20 (n/a)</td><td>347.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 (+1.22%)</td><td>0.12 <b>(-28.25%)</b></td><td>0.10 <b>(-42.15%)</b></td><td>0.07 <b>(-40.99%)</b></td><td>0.05 <b>(+77.90%)</b></td><td>683.10 <b>(+69.46%)</b></td><td>466.82 <b>(+54.51%)</b></td><td>495.90 <b>(+72.85%)</b></td><td>247.10 (-1.24%)</td><td>173.74 <b>(+187.19%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>403.10 (n/a)</td><td>302.12 (n/a)</td><td>286.90 (n/a)</td><td>250.20 (n/a)</td><td>60.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.22 <b>(+21.66%)</b></td><td>0.15 <b>(+23.23%)</b></td><td>0.17 <b>(+38.00%)</b></td><td>0.11 (+10.41%)</td><td>0.05 <b>(+37.57%)</b></td><td>461.40 (-9.42%)</td><td>344.70 (-17.03%)</td><td>297.10 <b>(-27.54%)</b></td><td>228.40 (-17.81%)</td><td>103.58 (+5.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>509.40 (n/a)</td><td>415.46 (n/a)</td><td>410.00 (n/a)</td><td>277.90 (n/a)</td><td>98.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 <b>(+25.56%)</b></td><td>0.15 <b>(+26.42%)</b></td><td>0.18 <b>(+80.05%)</b></td><td>0.03 <b>(-72.03%)</b></td><td>0.07 <b>(+121.98%)</b></td><td>1909.90 <b>(+257.46%)</b></td><td>602.94 <b>(+36.79%)</b></td><td>276.70 <b>(-44.46%)</b></td><td>242.20 <b>(-20.36%)</b></td><td>731.07 <b>(+583.41%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>534.30 (n/a)</td><td>440.78 (n/a)</td><td>498.20 (n/a)</td><td>304.10 (n/a)</td><td>106.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.21 <b>(+22.70%)</b></td><td>0.14 (+10.60%)</td><td>0.13 (+15.94%)</td><td>0.10 (+6.07%)</td><td>0.04 <b>(+22.11%)</b></td><td>504.40 (-5.72%)</td><td>370.78 (-8.68%)</td><td>372.20 (-13.76%)</td><td>237.70 (-18.51%)</td><td>104.72 (-2.36%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>535.00 (n/a)</td><td>406.04 (n/a)</td><td>431.60 (n/a)</td><td>291.70 (n/a)</td><td>107.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 (-12.83%)</td><td>0.11 (-4.52%)</td><td>0.11 (+0.98%)</td><td>0.07 (-13.19%)</td><td>0.04 <b>(-21.76%)</b></td><td>700.60 (+15.19%)</td><td>464.06 (+2.64%)</td><td>442.10 (-0.96%)</td><td>292.60 (+14.70%)</td><td>150.33 (+2.63%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>608.20 (n/a)</td><td>452.14 (n/a)</td><td>446.40 (n/a)</td><td>255.10 (n/a)</td><td>146.47 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (-16.93%)</td><td>0.01 (+3.79%)</td><td>0.01 <b>(+35.55%)</b></td><td>0.01 <b>(+34.34%)</b></td><td>0.00 <b>(-56.93%)</b></td><td>484.80 <b>(-25.56%)</b></td><td>400.08 (-14.19%)</td><td>411.20 <b>(-26.23%)</b></td><td>325.10 <b>(+20.36%)</b></td><td>70.87 <b>(-60.28%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>651.30 (n/a)</td><td>466.26 (n/a)</td><td>557.40 (n/a)</td><td>270.10 (n/a)</td><td>178.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (+8.07%)</td><td>0.01 (+13.46%)</td><td>0.01 <b>(+38.40%)</b></td><td>0.00 <b>(+43.11%)</b></td><td>0.00 (-6.80%)</td><td>585.20 <b>(-30.13%)</b></td><td>382.02 (-17.71%)</td><td>324.20 <b>(-27.75%)</b></td><td>225.70 (-7.46%)</td><td>147.88 <b>(-36.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>837.50 (n/a)</td><td>464.22 (n/a)</td><td>448.70 (n/a)</td><td>243.90 (n/a)</td><td>234.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (-5.87%)</td><td>0.01 <b>(-22.64%)</b></td><td>0.01 <b>(-26.63%)</b></td><td>0.00 <b>(-37.06%)</b></td><td>0.00 <b>(+78.70%)</b></td><td>566.10 <b>(+58.88%)</b></td><td>403.72 <b>(+41.46%)</b></td><td>388.50 <b>(+36.32%)</b></td><td>239.80 (+6.25%)</td><td>145.01 <b>(+209.56%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>356.30 (n/a)</td><td>285.40 (n/a)</td><td>285.00 (n/a)</td><td>225.70 (n/a)</td><td>46.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (-0.35%)</td><td>0.01 (+7.68%)</td><td>0.01 <b>(+42.16%)</b></td><td>0.00 (-16.06%)</td><td>0.00 (+10.27%)</td><td>671.60 (+19.14%)</td><td>393.32 (-2.78%)</td><td>304.80 <b>(-29.64%)</b></td><td>232.90 (+0.34%)</td><td>175.85 <b>(+40.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>563.70 (n/a)</td><td>404.58 (n/a)</td><td>433.20 (n/a)</td><td>232.10 (n/a)</td><td>125.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 <b>(+34.38%)</b></td><td>0.01 <b>(+44.43%)</b></td><td>0.01 <b>(+44.79%)</b></td><td>0.00 <b>(+364.73%)</b></td><td>0.00 (+1.19%)</td><td>531.80 <b>(-78.48%)</b></td><td>350.24 <b>(-56.83%)</b></td><td>314.70 <b>(-30.93%)</b></td><td>203.70 <b>(-25.58%)</b></td><td>139.53 <b>(-85.06%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2471.50 (n/a)</td><td>811.28 (n/a)</td><td>455.60 (n/a)</td><td>273.70 (n/a)</td><td>933.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 <b>(+21.53%)</b></td><td>0.01 <b>(+21.68%)</b></td><td>0.01 <b>(+28.06%)</b></td><td>0.00 <b>(+21.09%)</b></td><td>0.00 (+0.27%)</td><td>560.90 (-17.41%)</td><td>469.46 (-18.52%)</td><td>481.50 <b>(-21.91%)</b></td><td>377.00 (-17.72%)</td><td>70.78 <b>(-31.35%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>679.10 (n/a)</td><td>576.14 (n/a)</td><td>616.60 (n/a)</td><td>458.20 (n/a)</td><td>103.11 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+6.04%)</td><td>0.02 (+11.50%)</td><td>0.02 <b>(+52.78%)</b></td><td>0.01 (-7.59%)</td><td>0.00 (+0.87%)</td><td>535.20 (+8.21%)</td><td>349.58 (-10.11%)</td><td>294.30 <b>(-34.54%)</b></td><td>232.00 (-5.73%)</td><td>119.45 (+4.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.60 (n/a)</td><td>388.90 (n/a)</td><td>449.60 (n/a)</td><td>246.10 (n/a)</td><td>114.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+17.88%)</td><td>0.02 <b>(+39.05%)</b></td><td>0.02 <b>(+78.11%)</b></td><td>0.01 (+2.94%)</td><td>0.01 <b>(+62.09%)</b></td><td>567.90 (-2.86%)</td><td>351.40 <b>(-21.90%)</b></td><td>238.40 <b>(-43.85%)</b></td><td>226.00 (-15.17%)</td><td>167.07 <b>(+25.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>584.60 (n/a)</td><td>449.92 (n/a)</td><td>424.60 (n/a)</td><td>266.40 (n/a)</td><td>133.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-16.82%)</td><td>0.02 (+12.84%)</td><td>0.02 (+15.14%)</td><td>0.02 <b>(+86.91%)</b></td><td>0.00 <b>(-64.14%)</b></td><td>295.30 <b>(-46.50%)</b></td><td>259.34 <b>(-27.09%)</b></td><td>274.30 (-13.17%)</td><td>202.00 <b>(+20.24%)</b></td><td>37.82 <b>(-78.39%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.00 (n/a)</td><td>355.70 (n/a)</td><td>315.90 (n/a)</td><td>168.00 (n/a)</td><td>174.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-21.22%)</b></td><td>0.01 (-1.44%)</td><td>0.02 <b>(+46.66%)</b></td><td>0.01 <b>(-21.34%)</b></td><td>0.01 (-14.83%)</td><td>703.70 <b>(+27.14%)</b></td><td>420.98 (+3.34%)</td><td>311.70 <b>(-31.82%)</b></td><td>263.40 <b>(+26.94%)</b></td><td>196.22 <b>(+33.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.50 (n/a)</td><td>407.36 (n/a)</td><td>457.20 (n/a)</td><td>207.50 (n/a)</td><td>147.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(+45.36%)</b></td><td>0.01 (-5.24%)</td><td>0.01 (-1.65%)</td><td>0.00 <b>(-75.31%)</b></td><td>0.01 <b>(+367.67%)</b></td><td>2047.90 <b>(+305.04%)</b></td><td>741.52 <b>(+65.57%)</b></td><td>468.40 (+1.69%)</td><td>269.30 <b>(-31.21%)</b></td><td>735.16 <b>(+1438.02%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.60 (n/a)</td><td>447.86 (n/a)</td><td>460.60 (n/a)</td><td>391.50 (n/a)</td><td>47.80 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-32.48%)</b></td><td>0.01 (-19.36%)</td><td>0.01 (-1.71%)</td><td>0.01 (+3.19%)</td><td>0.00 <b>(-60.41%)</b></td><td>576.10 (-3.08%)</td><td>472.74 (+12.36%)</td><td>481.80 (+1.73%)</td><td>341.70 <b>(+48.11%)</b></td><td>85.97 <b>(-44.18%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.40 (n/a)</td><td>420.72 (n/a)</td><td>473.60 (n/a)</td><td>230.70 (n/a)</td><td>154.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 <b>(-21.37%)</b></td><td>0.02 <b>(-40.00%)</b></td><td>0.02 <b>(-42.08%)</b></td><td>0.00 <b>(-77.92%)</b></td><td>0.01 (-11.44%)</td><td>2469.00 <b>(+352.94%)</b></td><td>865.16 <b>(+143.98%)</b></td><td>529.70 <b>(+72.65%)</b></td><td>270.40 <b>(+27.19%)</b></td><td>903.91 <b>(+493.86%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.10 (n/a)</td><td>354.60 (n/a)</td><td>306.80 (n/a)</td><td>212.60 (n/a)</td><td>152.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-17.02%)</td><td>0.02 (-11.90%)</td><td>0.02 (-16.24%)</td><td>0.02 (-16.09%)</td><td>0.01 (-14.52%)</td><td>595.30 (+19.16%)</td><td>484.22 (+14.21%)</td><td>530.40 (+19.38%)</td><td>310.20 <b>(+20.51%)</b></td><td>127.96 <b>(+29.60%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.60 (n/a)</td><td>423.98 (n/a)</td><td>444.30 (n/a)</td><td>257.40 (n/a)</td><td>98.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (-12.31%)</td><td>0.03 (+9.93%)</td><td>0.04 <b>(+58.09%)</b></td><td>0.02 (+18.84%)</td><td>0.01 <b>(-22.42%)</b></td><td>503.50 (-15.86%)</td><td>348.88 (-14.22%)</td><td>272.70 <b>(-36.74%)</b></td><td>245.90 (+14.05%)</td><td>124.98 <b>(-24.27%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.40 (n/a)</td><td>406.72 (n/a)</td><td>431.10 (n/a)</td><td>215.60 (n/a)</td><td>165.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (-5.15%)</td><td>0.03 <b>(+20.39%)</b></td><td>0.03 <b>(+55.13%)</b></td><td>0.02 <b>(+205.66%)</b></td><td>0.01 (-18.66%)</td><td>626.70 <b>(-67.28%)</b></td><td>384.68 <b>(-43.25%)</b></td><td>301.50 <b>(-35.52%)</b></td><td>227.40 (+5.42%)</td><td>179.96 <b>(-74.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1915.50 (n/a)</td><td>677.86 (n/a)</td><td>467.60 (n/a)</td><td>215.70 (n/a)</td><td>701.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (-15.98%)</td><td>0.02 (-18.48%)</td><td>0.02 (-13.37%)</td><td>0.02 (-11.03%)</td><td>0.01 <b>(-28.34%)</b></td><td>679.30 (+12.39%)</td><td>482.68 (+16.68%)</td><td>492.10 (+15.44%)</td><td>266.70 (+19.01%)</td><td>148.78 (-9.28%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>604.40 (n/a)</td><td>413.68 (n/a)</td><td>426.30 (n/a)</td><td>224.10 (n/a)</td><td>163.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-7.20%)</td><td>0.02 (-16.80%)</td><td>0.02 (-7.40%)</td><td>0.01 <b>(-37.36%)</b></td><td>0.01 (+15.44%)</td><td>996.90 <b>(+59.63%)</b></td><td>603.42 <b>(+28.21%)</b></td><td>480.70 (+7.97%)</td><td>382.10 (+7.76%)</td><td>249.16 <b>(+106.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.50 (n/a)</td><td>470.66 (n/a)</td><td>445.20 (n/a)</td><td>354.60 (n/a)</td><td>120.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (-2.38%)</td><td>0.06 (+4.11%)</td><td>0.06 (-18.41%)</td><td>0.03 <b>(+202.42%)</b></td><td>0.02 <b>(-22.56%)</b></td><td>628.10 <b>(-66.93%)</b></td><td>417.98 <b>(-36.29%)</b></td><td>374.90 <b>(+22.56%)</b></td><td>249.90 (+2.42%)</td><td>176.38 <b>(-75.00%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1899.50 (n/a)</td><td>656.10 (n/a)</td><td>305.90 (n/a)</td><td>244.00 (n/a)</td><td>705.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (-7.23%)</td><td>0.05 <b>(-20.03%)</b></td><td>0.05 <b>(-37.07%)</b></td><td>0.04 (-5.38%)</td><td>0.02 (+10.63%)</td><td>566.60 (+5.69%)</td><td>418.26 <b>(+27.32%)</b></td><td>446.10 <b>(+58.92%)</b></td><td>275.40 (+7.83%)</td><td>133.34 (+14.20%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>536.10 (n/a)</td><td>328.50 (n/a)</td><td>280.70 (n/a)</td><td>255.40 (n/a)</td><td>116.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 <b>(+27.79%)</b></td><td>0.05 <b>(-20.83%)</b></td><td>0.04 <b>(-37.47%)</b></td><td>0.01 <b>(-71.87%)</b></td><td>0.03 <b>(+67.24%)</b></td><td>1927.20 <b>(+255.57%)</b></td><td>715.34 <b>(+92.80%)</b></td><td>475.00 <b>(+59.93%)</b></td><td>200.80 <b>(-21.75%)</b></td><td>690.06 <b>(+407.75%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>542.00 (n/a)</td><td>371.02 (n/a)</td><td>297.00 (n/a)</td><td>256.60 (n/a)</td><td>135.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 <b>(+53.81%)</b></td><td>0.07 <b>(+53.23%)</b></td><td>0.07 <b>(+56.03%)</b></td><td>0.05 <b>(+23.73%)</b></td><td>0.02 <b>(+98.21%)</b></td><td>463.50 (-19.18%)</td><td>311.70 <b>(-33.01%)</b></td><td>291.50 <b>(-35.91%)</b></td><td>242.30 <b>(-34.99%)</b></td><td>87.31 (+9.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>573.50 (n/a)</td><td>465.26 (n/a)</td><td>454.80 (n/a)</td><td>372.70 (n/a)</td><td>79.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 <b>(-36.09%)</b></td><td>0.04 <b>(-30.31%)</b></td><td>0.04 <b>(-30.51%)</b></td><td>0.03 (-3.62%)</td><td>0.01 <b>(-59.67%)</b></td><td>602.40 (+3.77%)</td><td>485.06 <b>(+32.08%)</b></td><td>506.70 <b>(+43.91%)</b></td><td>350.40 <b>(+56.50%)</b></td><td>92.11 <b>(-35.29%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>580.50 (n/a)</td><td>367.26 (n/a)</td><td>352.10 (n/a)</td><td>223.90 (n/a)</td><td>142.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 <b>(-32.60%)</b></td><td>0.04 (-17.45%)</td><td>0.04 (+3.52%)</td><td>0.01 <b>(-75.16%)</b></td><td>0.02 (-4.34%)</td><td>2458.60 <b>(+302.59%)</b></td><td>873.96 <b>(+75.10%)</b></td><td>501.90 (-3.39%)</td><td>380.10 <b>(+48.36%)</b></td><td>892.22 <b>(+514.99%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>610.70 (n/a)</td><td>499.12 (n/a)</td><td>519.50 (n/a)</td><td>256.20 (n/a)</td><td>145.08 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.40 (n/a)</td><td>411.24 (n/a)</td><td>447.40 (n/a)</td><td>284.40 (n/a)</td><td>104.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.10 (n/a)</td><td>420.74 (n/a)</td><td>349.40 (n/a)</td><td>261.40 (n/a)</td><td>156.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>695.70 (n/a)</td><td>408.74 (n/a)</td><td>358.10 (n/a)</td><td>243.40 (n/a)</td><td>187.45 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>564.30 (n/a)</td><td>368.20 (n/a)</td><td>299.20 (n/a)</td><td>221.60 (n/a)</td><td>165.78 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.90 (n/a)</td><td>388.72 (n/a)</td><td>369.80 (n/a)</td><td>269.20 (n/a)</td><td>116.35 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>665.70 (n/a)</td><td>488.90 (n/a)</td><td>507.30 (n/a)</td><td>204.60 (n/a)</td><td>192.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>628.70 (n/a)</td><td>406.22 (n/a)</td><td>440.90 (n/a)</td><td>242.60 (n/a)</td><td>162.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1036.10 (n/a)</td><td>562.66 (n/a)</td><td>480.10 (n/a)</td><td>276.00 (n/a)</td><td>283.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.10 (n/a)</td><td>373.38 (n/a)</td><td>324.10 (n/a)</td><td>274.70 (n/a)</td><td>116.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 (-3.25%)</td><td>0.16 <b>(+21.70%)</b></td><td>0.17 <b>(+50.86%)</b></td><td>0.09 (+9.97%)</td><td>0.04 (-14.83%)</td><td>526.70 (-9.06%)</td><td>326.58 (-19.61%)</td><td>292.40 <b>(-33.71%)</b></td><td>248.40 (+3.33%)</td><td>113.51 (-13.16%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>579.20 (n/a)</td><td>406.24 (n/a)</td><td>441.10 (n/a)</td><td>240.40 (n/a)</td><td>130.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>514.90 (n/a)</td><td>418.18 (n/a)</td><td>494.20 (n/a)</td><td>281.70 (n/a)</td><td>117.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>612.50 (n/a)</td><td>493.44 (n/a)</td><td>497.80 (n/a)</td><td>316.20 (n/a)</td><td>111.03 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.80 (n/a)</td><td>431.24 (n/a)</td><td>447.10 (n/a)</td><td>176.60 (n/a)</td><td>151.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1075.00 (n/a)</td><td>601.46 (n/a)</td><td>562.50 (n/a)</td><td>300.00 (n/a)</td><td>288.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1078.60 (n/a)</td><td>683.46 (n/a)</td><td>617.70 (n/a)</td><td>525.30 (n/a)</td><td>224.50 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>622.40 (n/a)</td><td>516.18 (n/a)</td><td>534.70 (n/a)</td><td>390.20 (n/a)</td><td>86.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>777.00 (n/a)</td><td>478.56 (n/a)</td><td>488.80 (n/a)</td><td>276.40 (n/a)</td><td>192.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.40 (n/a)</td><td>450.78 (n/a)</td><td>475.60 (n/a)</td><td>245.70 (n/a)</td><td>122.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1814.40 (n/a)</td><td>682.52 (n/a)</td><td>434.90 (n/a)</td><td>277.10 (n/a)</td><td>643.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1058.70 (n/a)</td><td>478.48 (n/a)</td><td>285.70 (n/a)</td><td>245.80 (n/a)</td><td>342.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1302.80 (n/a)</td><td>596.64 (n/a)</td><td>479.10 (n/a)</td><td>295.40 (n/a)</td><td>404.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>509.40 (n/a)</td><td>372.78 (n/a)</td><td>340.30 (n/a)</td><td>252.40 (n/a)</td><td>109.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>546.70 (n/a)</td><td>451.74 (n/a)</td><td>462.60 (n/a)</td><td>264.20 (n/a)</td><td>113.11 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>465.70 (n/a)</td><td>351.16 (n/a)</td><td>294.10 (n/a)</td><td>268.10 (n/a)</td><td>91.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.70 (n/a)</td><td>407.92 (n/a)</td><td>359.20 (n/a)</td><td>225.20 (n/a)</td><td>164.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.10 (n/a)</td><td>342.24 (n/a)</td><td>277.60 (n/a)</td><td>205.40 (n/a)</td><td>153.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1095.10 (n/a)</td><td>574.50 (n/a)</td><td>464.20 (n/a)</td><td>320.10 (n/a)</td><td>301.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.30 (n/a)</td><td>434.36 (n/a)</td><td>487.70 (n/a)</td><td>243.00 (n/a)</td><td>171.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.20 (n/a)</td><td>394.38 (n/a)</td><td>337.50 (n/a)</td><td>188.80 (n/a)</td><td>176.90 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1848.70 (n/a)</td><td>705.28 (n/a)</td><td>460.30 (n/a)</td><td>299.90 (n/a)</td><td>644.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>711.90 (n/a)</td><td>384.78 (n/a)</td><td>298.60 (n/a)</td><td>228.70 (n/a)</td><td>199.47 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.40 (n/a)</td><td>409.58 (n/a)</td><td>490.70 (n/a)</td><td>227.20 (n/a)</td><td>165.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.30 (n/a)</td><td>325.50 (n/a)</td><td>314.50 (n/a)</td><td>230.20 (n/a)</td><td>120.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>549.60 (n/a)</td><td>344.34 (n/a)</td><td>279.30 (n/a)</td><td>149.30 (n/a)</td><td>172.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.30 (n/a)</td><td>418.56 (n/a)</td><td>463.60 (n/a)</td><td>278.70 (n/a)</td><td>130.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>462.80 (n/a)</td><td>328.76 (n/a)</td><td>293.90 (n/a)</td><td>240.50 (n/a)</td><td>90.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>621.00 (n/a)</td><td>457.46 (n/a)</td><td>441.40 (n/a)</td><td>277.20 (n/a)</td><td>125.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>501.10 (n/a)</td><td>355.20 (n/a)</td><td>281.50 (n/a)</td><td>252.60 (n/a)</td><td>116.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>600.00 (n/a)</td><td>438.64 (n/a)</td><td>431.60 (n/a)</td><td>288.50 (n/a)</td><td>149.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>400.00 (n/a)</td><td>308.38 (n/a)</td><td>270.20 (n/a)</td><td>257.70 (n/a)</td><td>63.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>562.30 (n/a)</td><td>453.00 (n/a)</td><td>445.30 (n/a)</td><td>304.80 (n/a)</td><td>96.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>602.40 (n/a)</td><td>447.40 (n/a)</td><td>445.30 (n/a)</td><td>260.80 (n/a)</td><td>146.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>763.80 (n/a)</td><td>572.98 (n/a)</td><td>531.50 (n/a)</td><td>418.80 (n/a)</td><td>136.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>637.20 (n/a)</td><td>441.88 (n/a)</td><td>475.40 (n/a)</td><td>268.00 (n/a)</td><td>160.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>592.60 (n/a)</td><td>449.52 (n/a)</td><td>535.10 (n/a)</td><td>270.10 (n/a)</td><td>150.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>587.00 (n/a)</td><td>452.52 (n/a)</td><td>455.10 (n/a)</td><td>321.20 (n/a)</td><td>117.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.87 <b>(+40.29%)</b></td><td>0.41 (-7.55%)</td><td>0.35 (-16.62%)</td><td>0.13 <b>(-63.56%)</b></td><td>0.27 <b>(+160.93%)</b></td><td>1739.10 <b>(+174.44%)</b></td><td>770.86 <b>(+50.17%)</b></td><td>624.60 (+19.93%)</td><td>253.80 <b>(-28.71%)</b></td><td>564.52 <b>(+438.87%)</b></td><td>37.18 <b>(+40.29%)</b></td><td>17.66 (-7.55%)</td><td>15.11 (-16.62%)</td><td>5.43 <b>(-63.56%)</b></td><td>11.72 <b>(+160.93%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.62 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.11 (n/a)</td><td>633.70 (n/a)</td><td>513.32 (n/a)</td><td>520.80 (n/a)</td><td>356.00 (n/a)</td><td>104.76 (n/a)</td><td>26.51 (n/a)</td><td>19.11 (n/a)</td><td>18.12 (n/a)</td><td>14.89 (n/a)</td><td>4.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.60 <b>(-23.95%)</b></td><td>0.41 <b>(-27.03%)</b></td><td>0.47 (-17.55%)</td><td>0.13 <b>(-66.11%)</b></td><td>0.19 <b>(+23.31%)</b></td><td>1711.20 <b>(+195.09%)</b></td><td>729.12 <b>(+75.35%)</b></td><td>470.90 <b>(+21.30%)</b></td><td>366.30 <b>(+31.48%)</b></td><td>561.28 <b>(+407.34%)</b></td><td>25.76 <b>(-23.95%)</b></td><td>17.53 <b>(-27.03%)</b></td><td>20.04 (-17.55%)</td><td>5.52 <b>(-66.11%)</b></td><td>7.98 <b>(+23.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.79 (n/a)</td><td>0.56 (n/a)</td><td>0.57 (n/a)</td><td>0.38 (n/a)</td><td>0.15 (n/a)</td><td>579.90 (n/a)</td><td>415.80 (n/a)</td><td>388.20 (n/a)</td><td>278.60 (n/a)</td><td>110.63 (n/a)</td><td>33.88 (n/a)</td><td>24.03 (n/a)</td><td>24.31 (n/a)</td><td>16.27 (n/a)</td><td>6.47 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.31 (+1.26%)</td><td>0.30 (+1.81%)</td><td>0.31 (+2.88%)</td><td>0.29 (+0.61%)</td><td>0.01 <b>(+31.96%)</b></td><td>85736.30 (-0.61%)</td><td>82732.08 (-1.76%)</td><td>81398.50 (-2.80%)</td><td>81322.30 (-1.24%)</td><td>1994.19 <b>(+28.92%)</b></td><td>211.26 (+1.26%)</td><td>207.75 (+1.81%)</td><td>211.06 (+2.88%)</td><td>200.38 (+0.61%)</td><td>4.93 <b>(+31.96%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86261.50 (n/a)</td><td>84211.84 (n/a)</td><td>83746.20 (n/a)</td><td>82343.10 (n/a)</td><td>1546.82 (n/a)</td><td>208.64 (n/a)</td><td>204.06 (n/a)</td><td>205.14 (n/a)</td><td>199.16 (n/a)</td><td>3.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>1.03 (-1.05%)</td><td>1.01 (+0.23%)</td><td>1.01 (+1.38%)</td><td>1.00 (+1.00%)</td><td>0.01 <b>(-45.52%)</b></td><td>25290.00 (-0.99%)</td><td>24868.90 (-0.27%)</td><td>24796.90 (-1.36%)</td><td>24409.30 (+1.06%)</td><td>331.53 <b>(-45.47%)</b></td><td>703.82 (-1.05%)</td><td>690.92 (+0.23%)</td><td>692.82 (+1.38%)</td><td>679.32 (+1.00%)</td><td>9.23 <b>(-45.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>1.04 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.99 (n/a)</td><td>0.02 (n/a)</td><td>25542.70 (n/a)</td><td>24934.98 (n/a)</td><td>25139.70 (n/a)</td><td>24152.20 (n/a)</td><td>607.91 (n/a)</td><td>711.32 (n/a)</td><td>689.32 (n/a)</td><td>683.38 (n/a)</td><td>672.59 (n/a)</td><td>16.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.82 (+0.13%)</td><td>0.81 (-1.30%)</td><td>0.82 (-0.19%)</td><td>0.76 (-6.18%)</td><td>0.03 <b>(+563.23%)</b></td><td>99279.00 (+6.59%)</td><td>93766.82 (+1.41%)</td><td>92606.50 (+0.19%)</td><td>91890.40 (-0.13%)</td><td>3113.47 <b>(+608.32%)</b></td><td>747.84 (+0.13%)</td><td>733.50 (-1.30%)</td><td>742.06 (-0.19%)</td><td>692.19 (-6.18%)</td><td>23.37 <b>(+563.23%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.00 (n/a)</td><td>93141.20 (n/a)</td><td>92467.24 (n/a)</td><td>92432.60 (n/a)</td><td>92008.00 (n/a)</td><td>439.56 (n/a)</td><td>746.89 (n/a)</td><td>743.19 (n/a)</td><td>743.46 (n/a)</td><td>737.80 (n/a)</td><td>3.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.78 (+0.11%)</td><td>0.77 (+1.30%)</td><td>0.77 (+0.99%)</td><td>0.77 (+2.70%)</td><td>0.00 <b>(-61.61%)</b></td><td>98463.00 (-2.63%)</td><td>97660.06 (-1.30%)</td><td>97647.30 (-0.98%)</td><td>97095.00 (-0.11%)</td><td>541.47 <b>(-62.72%)</b></td><td>707.76 (+0.11%)</td><td>703.68 (+1.30%)</td><td>703.75 (+0.99%)</td><td>697.92 (+2.70%)</td><td>3.89 <b>(-61.61%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101119.50 (n/a)</td><td>98948.36 (n/a)</td><td>98618.30 (n/a)</td><td>97201.90 (n/a)</td><td>1452.36 (n/a)</td><td>706.98 (n/a)</td><td>694.62 (n/a)</td><td>696.82 (n/a)</td><td>679.59 (n/a)</td><td>10.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.80 (-0.75%)</td><td>0.79 (-0.96%)</td><td>0.79 (-1.52%)</td><td>0.79 (-0.63%)</td><td>0.00 (+1.05%)</td><td>96037.50 (+0.64%)</td><td>95469.16 (+0.97%)</td><td>95698.20 (+1.54%)</td><td>94765.50 (+0.76%)</td><td>594.89 (+2.44%)</td><td>725.15 (-0.75%)</td><td>719.83 (-0.96%)</td><td>718.09 (-1.52%)</td><td>715.55 (-0.63%)</td><td>4.49 (+1.05%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95429.40 (n/a)</td><td>94555.08 (n/a)</td><td>94247.20 (n/a)</td><td>94051.60 (n/a)</td><td>580.71 (n/a)</td><td>730.66 (n/a)</td><td>726.79 (n/a)</td><td>729.14 (n/a)</td><td>720.11 (n/a)</td><td>4.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.82 (+3.91%)</td><td>4.48 (-16.60%)</td><td>5.31 (+0.58%)</td><td>2.18 <b>(-58.07%)</b></td><td>1.59 <b>(+720.08%)</b></td><td>4092.00 <b>(+138.46%)</b></td><td>2291.38 <b>(+37.91%)</b></td><td>1679.50 (-0.57%)</td><td>1532.10 (-3.76%)</td><td>1091.43 <b>(+1742.76%)</b></td><td>350.42 (+3.91%)</td><td>269.76 (-16.60%)</td><td>319.67 (+0.58%)</td><td>131.20 <b>(-58.07%)</b></td><td>95.60 <b>(+720.08%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.60 (n/a)</td><td>5.37 (n/a)</td><td>5.28 (n/a)</td><td>5.19 (n/a)</td><td>0.19 (n/a)</td><td>1716.00 (n/a)</td><td>1661.56 (n/a)</td><td>1689.20 (n/a)</td><td>1592.00 (n/a)</td><td>59.23 (n/a)</td><td>337.24 (n/a)</td><td>323.45 (n/a)</td><td>317.82 (n/a)</td><td>312.87 (n/a)</td><td>11.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>4.58 (-6.05%)</td><td>3.63 (+5.37%)</td><td>3.41 (+18.90%)</td><td>2.27 (+4.81%)</td><td>0.96 (-19.53%)</td><td>3933.40 (-4.59%)</td><td>2622.36 (-7.90%)</td><td>2614.60 (-15.90%)</td><td>1947.00 (+6.44%)</td><td>806.70 (-15.60%)</td><td>275.74 (-6.05%)</td><td>218.60 (+5.37%)</td><td>205.34 (+18.90%)</td><td>136.49 (+4.81%)</td><td>57.80 (-19.53%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.87 (n/a)</td><td>3.44 (n/a)</td><td>2.87 (n/a)</td><td>2.16 (n/a)</td><td>1.19 (n/a)</td><td>4122.50 (n/a)</td><td>2847.28 (n/a)</td><td>3108.80 (n/a)</td><td>1829.20 (n/a)</td><td>955.80 (n/a)</td><td>293.51 (n/a)</td><td>207.46 (n/a)</td><td>172.69 (n/a)</td><td>130.23 (n/a)</td><td>71.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.59 (+7.71%)</td><td>3.80 (-7.46%)</td><td>3.93 (-4.50%)</td><td>2.68 (-13.27%)</td><td>1.18 <b>(+58.35%)</b></td><td>3329.40 (+15.30%)</td><td>2523.90 (+13.12%)</td><td>2267.20 (+4.71%)</td><td>1594.40 (-7.16%)</td><td>732.61 <b>(+74.52%)</b></td><td>336.72 (+7.71%)</td><td>228.83 (-7.46%)</td><td>236.80 (-4.50%)</td><td>161.25 (-13.27%)</td><td>71.16 <b>(+58.35%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.19 (n/a)</td><td>4.10 (n/a)</td><td>4.12 (n/a)</td><td>3.09 (n/a)</td><td>0.75 (n/a)</td><td>2887.60 (n/a)</td><td>2231.14 (n/a)</td><td>2165.30 (n/a)</td><td>1717.40 (n/a)</td><td>419.78 (n/a)</td><td>312.61 (n/a)</td><td>247.26 (n/a)</td><td>247.94 (n/a)</td><td>185.92 (n/a)</td><td>44.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>6.70 (-0.41%)</td><td>5.27 (-3.84%)</td><td>5.65 (-0.61%)</td><td>3.68 (-11.29%)</td><td>1.43 <b>(+45.11%)</b></td><td>9481.50 (+12.72%)</td><td>7064.50 (+7.96%)</td><td>6168.30 (+0.62%)</td><td>5200.60 (+0.41%)</td><td>2055.82 <b>(+64.88%)</b></td><td>412.93 (-0.41%)</td><td>324.37 (-3.84%)</td><td>348.15 (-0.61%)</td><td>226.49 (-11.29%)</td><td>88.06 <b>(+45.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>6.73 (n/a)</td><td>5.48 (n/a)</td><td>5.69 (n/a)</td><td>4.14 (n/a)</td><td>0.99 (n/a)</td><td>8411.40 (n/a)</td><td>6543.46 (n/a)</td><td>6130.50 (n/a)</td><td>5179.50 (n/a)</td><td>1246.89 (n/a)</td><td>414.61 (n/a)</td><td>337.33 (n/a)</td><td>350.29 (n/a)</td><td>255.31 (n/a)</td><td>60.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.21 (-8.91%)</td><td>4.49 (-12.42%)</td><td>4.66 (-9.66%)</td><td>3.68 (-10.88%)</td><td>0.59 (-2.68%)</td><td>9477.70 (+12.21%)</td><td>7881.62 (+14.39%)</td><td>7474.90 (+10.69%)</td><td>6692.00 (+9.78%)</td><td>1081.46 (+18.29%)</td><td>320.90 (-8.91%)</td><td>276.42 (-12.42%)</td><td>287.29 (-9.66%)</td><td>226.58 (-10.88%)</td><td>36.26 (-2.68%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.72 (n/a)</td><td>5.12 (n/a)</td><td>5.16 (n/a)</td><td>4.13 (n/a)</td><td>0.60 (n/a)</td><td>8446.70 (n/a)</td><td>6889.94 (n/a)</td><td>6753.20 (n/a)</td><td>6096.10 (n/a)</td><td>914.24 (n/a)</td><td>352.27 (n/a)</td><td>315.62 (n/a)</td><td>318.00 (n/a)</td><td>254.24 (n/a)</td><td>37.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>6.57 (-1.67%)</td><td>5.79 (-2.33%)</td><td>5.69 (-7.63%)</td><td>5.06 (+2.08%)</td><td>0.60 <b>(-25.22%)</b></td><td>6895.00 (-2.03%)</td><td>6074.06 (+1.70%)</td><td>6126.10 (+8.26%)</td><td>5310.10 (+1.69%)</td><td>626.97 <b>(-25.32%)</b></td><td>404.42 (-1.67%)</td><td>356.59 (-2.33%)</td><td>350.55 (-7.63%)</td><td>311.45 (+2.08%)</td><td>36.92 <b>(-25.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>6.68 (n/a)</td><td>5.93 (n/a)</td><td>6.16 (n/a)</td><td>4.95 (n/a)</td><td>0.80 (n/a)</td><td>7038.10 (n/a)</td><td>5972.56 (n/a)</td><td>5658.50 (n/a)</td><td>5221.60 (n/a)</td><td>839.53 (n/a)</td><td>411.27 (n/a)</td><td>365.10 (n/a)</td><td>379.51 (n/a)</td><td>305.12 (n/a)</td><td>49.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.78 (-0.13%)</td><td>0.76 (-0.99%)</td><td>0.76 (-0.31%)</td><td>0.74 (-2.53%)</td><td>0.01 <b>(+69.11%)</b></td><td>101799.10 (+2.60%)</td><td>99236.74 (+1.01%)</td><td>98994.40 (+0.31%)</td><td>96899.50 (+0.13%)</td><td>1840.41 <b>(+73.79%)</b></td><td>709.18 (-0.13%)</td><td>692.67 (-0.99%)</td><td>694.18 (-0.31%)</td><td>675.05 (-2.53%)</td><td>12.81 <b>(+69.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99219.10 (n/a)</td><td>98240.20 (n/a)</td><td>98692.10 (n/a)</td><td>96776.90 (n/a)</td><td>1058.96 (n/a)</td><td>710.08 (n/a)</td><td>699.57 (n/a)</td><td>696.30 (n/a)</td><td>692.60 (n/a)</td><td>7.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.78 (+2.02%)</td><td>0.76 (+2.02%)</td><td>0.76 (+1.61%)</td><td>0.75 (+2.50%)</td><td>0.01 (-6.14%)</td><td>101026.20 (-2.44%)</td><td>98919.30 (-1.98%)</td><td>99224.10 (-1.59%)</td><td>96965.60 (-1.98%)</td><td>1546.83 (-10.42%)</td><td>708.70 (+2.02%)</td><td>694.84 (+2.02%)</td><td>692.57 (+1.61%)</td><td>680.21 (+2.50%)</td><td>10.86 (-6.14%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.01 (n/a)</td><td>103556.90 (n/a)</td><td>100916.64 (n/a)</td><td>100825.60 (n/a)</td><td>98921.50 (n/a)</td><td>1726.81 (n/a)</td><td>694.69 (n/a)</td><td>681.11 (n/a)</td><td>681.57 (n/a)</td><td>663.59 (n/a)</td><td>11.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.80 (-0.46%)</td><td>0.79 (-1.13%)</td><td>0.80 (+0.24%)</td><td>0.75 (-5.38%)</td><td>0.02 <b>(+350.07%)</b></td><td>100177.90 (+5.69%)</td><td>95503.48 (+1.20%)</td><td>94303.30 (-0.24%)</td><td>93845.00 (+0.47%)</td><td>2663.43 <b>(+379.50%)</b></td><td>732.27 (-0.46%)</td><td>719.98 (-1.13%)</td><td>728.71 (+0.24%)</td><td>685.97 (-5.38%)</td><td>19.42 <b>(+350.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94785.50 (n/a)</td><td>94368.88 (n/a)</td><td>94530.80 (n/a)</td><td>93409.70 (n/a)</td><td>555.46 (n/a)</td><td>735.68 (n/a)</td><td>728.22 (n/a)</td><td>726.95 (n/a)</td><td>725.00 (n/a)</td><td>4.31 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.02 <b>(-46.97%)</b></td><td>1.84 <b>(-29.09%)</b></td><td>1.92 <b>(-29.05%)</b></td><td>1.58 (-3.14%)</td><td>0.18 <b>(-77.65%)</b></td><td>5114.00 (+3.24%)</td><td>4426.12 <b>(+31.17%)</b></td><td>4198.40 <b>(+40.95%)</b></td><td>3994.90 <b>(+88.56%)</b></td><td>465.27 <b>(-56.80%)</b></td><td>529.16 <b>(-46.97%)</b></td><td>481.64 <b>(-29.09%)</b></td><td>503.51 <b>(-29.05%)</b></td><td>413.36 (-3.14%)</td><td>48.05 <b>(-77.65%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.80 (n/a)</td><td>2.59 (n/a)</td><td>2.71 (n/a)</td><td>1.63 (n/a)</td><td>0.82 (n/a)</td><td>4953.30 (n/a)</td><td>3374.34 (n/a)</td><td>2978.60 (n/a)</td><td>2118.60 (n/a)</td><td>1076.91 (n/a)</td><td>997.81 (n/a)</td><td>679.23 (n/a)</td><td>709.71 (n/a)</td><td>426.78 (n/a)</td><td>214.97 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.21 <b>(-28.82%)</b></td><td>0.20 (-10.39%)</td><td>0.20 (-5.66%)</td><td>0.19 (+8.51%)</td><td>0.01 <b>(-81.89%)</b></td><td>6415.50 (-7.84%)</td><td>6190.44 (+8.56%)</td><td>6170.80 (+6.00%)</td><td>5801.50 <b>(+40.49%)</b></td><td>247.49 <b>(-75.61%)</b></td><td>11.57 <b>(-28.82%)</b></td><td>10.85 (-10.39%)</td><td>10.88 (-5.66%)</td><td>10.46 (+8.51%)</td><td>0.45 <b>(-81.89%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>6961.40 (n/a)</td><td>5702.46 (n/a)</td><td>5821.30 (n/a)</td><td>4129.50 (n/a)</td><td>1014.76 (n/a)</td><td>16.25 (n/a)</td><td>12.11 (n/a)</td><td>11.53 (n/a)</td><td>9.64 (n/a)</td><td>2.46 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 <b>(+25.37%)</b></td><td>0.12 <b>(+26.83%)</b></td><td>0.12 (+5.97%)</td><td>0.07 <b>(+317.45%)</b></td><td>0.04 (-10.96%)</td><td>0.17 <b>(+25.37%)</b></td><td>0.11 <b>(+26.83%)</b></td><td>0.12 (+5.97%)</td><td>0.07 <b>(+317.45%)</b></td><td>0.04 (-10.96%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.86 (-2.47%)</td><td>3.54 (-1.89%)</td><td>3.50 (-6.53%)</td><td>3.38 (+10.70%)</td><td>0.19 <b>(-47.47%)</b></td><td>3.86 (-2.47%)</td><td>3.54 (-1.89%)</td><td>3.50 (-6.53%)</td><td>3.38 (+10.70%)</td><td>0.19 <b>(-47.47%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.96 (n/a)</td><td>3.61 (n/a)</td><td>3.75 (n/a)</td><td>3.05 (n/a)</td><td>0.36 (n/a)</td><td>3.95 (n/a)</td><td>3.61 (n/a)</td><td>3.74 (n/a)</td><td>3.05 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>7.35 (+0.18%)</td><td>6.64 (+6.26%)</td><td>7.30 <b>(+26.84%)</b></td><td>5.58 (+2.57%)</td><td>0.95 (+4.29%)</td><td>7.35 (+0.18%)</td><td>6.64 (+6.26%)</td><td>7.29 <b>(+26.84%)</b></td><td>5.58 (+2.57%)</td><td>0.95 (+4.29%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>7.34 (n/a)</td><td>6.25 (n/a)</td><td>5.75 (n/a)</td><td>5.44 (n/a)</td><td>0.91 (n/a)</td><td>7.34 (n/a)</td><td>6.24 (n/a)</td><td>5.75 (n/a)</td><td>5.44 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>13.84 (-0.97%)</td><td>9.97 (+4.54%)</td><td>8.84 (+2.60%)</td><td>8.30 (+11.34%)</td><td>2.30 (-10.31%)</td><td>13.83 (-0.97%)</td><td>9.96 (+4.54%)</td><td>8.83 (+2.60%)</td><td>8.29 (+11.34%)</td><td>2.29 (-10.31%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>13.97 (n/a)</td><td>9.54 (n/a)</td><td>8.62 (n/a)</td><td>7.45 (n/a)</td><td>2.56 (n/a)</td><td>13.96 (n/a)</td><td>9.53 (n/a)</td><td>8.61 (n/a)</td><td>7.45 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.82 (+0.12%)</td><td>3.71 (+2.45%)</td><td>3.74 (+3.80%)</td><td>3.51 (+0.32%)</td><td>0.12 (-0.42%)</td><td>3.82 (+0.12%)</td><td>3.71 (+2.45%)</td><td>3.74 (+3.80%)</td><td>3.51 (+0.32%)</td><td>0.12 (-0.42%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.82 (n/a)</td><td>3.62 (n/a)</td><td>3.60 (n/a)</td><td>3.50 (n/a)</td><td>0.12 (n/a)</td><td>3.82 (n/a)</td><td>3.62 (n/a)</td><td>3.60 (n/a)</td><td>3.50 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>7.48 (+12.81%)</td><td>7.15 (+17.32%)</td><td>7.13 (+17.41%)</td><td>6.76 (+17.34%)</td><td>0.29 (-17.91%)</td><td>7.47 (+12.81%)</td><td>7.15 (+17.32%)</td><td>7.12 (+17.41%)</td><td>6.75 (+17.34%)</td><td>0.29 (-17.91%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>6.63 (n/a)</td><td>6.10 (n/a)</td><td>6.07 (n/a)</td><td>5.76 (n/a)</td><td>0.35 (n/a)</td><td>6.62 (n/a)</td><td>6.09 (n/a)</td><td>6.07 (n/a)</td><td>5.76 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>14.14 (+18.84%)</td><td>11.19 <b>(+22.32%)</b></td><td>11.45 <b>(+40.26%)</b></td><td>7.05 (-3.77%)</td><td>2.95 <b>(+55.22%)</b></td><td>14.13 (+18.84%)</td><td>11.19 <b>(+22.32%)</b></td><td>11.45 <b>(+40.26%)</b></td><td>7.05 (-3.77%)</td><td>2.95 <b>(+55.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>11.90 (n/a)</td><td>9.15 (n/a)</td><td>8.17 (n/a)</td><td>7.33 (n/a)</td><td>1.90 (n/a)</td><td>11.89 (n/a)</td><td>9.14 (n/a)</td><td>8.16 (n/a)</td><td>7.32 (n/a)</td><td>1.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.90 (-7.39%)</td><td>2.01 (-7.10%)</td><td>1.71 <b>(-35.79%)</b></td><td>1.03 (-2.99%)</td><td>0.84 (-16.43%)</td><td>2.89 (-7.39%)</td><td>2.01 (-7.10%)</td><td>1.70 <b>(-35.79%)</b></td><td>1.02 (-2.99%)</td><td>0.84 (-16.43%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.13 (n/a)</td><td>2.16 (n/a)</td><td>2.66 (n/a)</td><td>1.06 (n/a)</td><td>1.01 (n/a)</td><td>3.12 (n/a)</td><td>2.16 (n/a)</td><td>2.65 (n/a)</td><td>1.06 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.44 (-18.79%)</td><td>0.27 <b>(-31.06%)</b></td><td>0.30 <b>(-40.27%)</b></td><td>0.07 (-1.33%)</td><td>0.16 (-15.68%)</td><td>0.43 (-18.79%)</td><td>0.27 <b>(-31.06%)</b></td><td>0.29 <b>(-40.27%)</b></td><td>0.07 (-1.33%)</td><td>0.16 (-15.68%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.49 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.49 (n/a)</td><td>0.07 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.68 (+12.31%)</td><td>0.55 <b>(+23.46%)</b></td><td>0.68 <b>(+61.75%)</b></td><td>0.26 (+4.90%)</td><td>0.19 <b>(+24.41%)</b></td><td>0.68 (+12.31%)</td><td>0.54 <b>(+23.46%)</b></td><td>0.67 <b>(+61.75%)</b></td><td>0.25 (+4.90%)</td><td>0.19 <b>(+24.41%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.61 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.60 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.90 (+10.97%)</td><td>1.67 <b>(+30.91%)</b></td><td>1.36 <b>(+195.13%)</b></td><td>0.44 (+1.33%)</td><td>0.95 (-15.73%)</td><td>2.85 (+10.97%)</td><td>1.64 <b>(+30.91%)</b></td><td>1.34 <b>(+195.13%)</b></td><td>0.44 (+1.33%)</td><td>0.94 (-15.73%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.61 (n/a)</td><td>1.27 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>1.13 (n/a)</td><td>2.57 (n/a)</td><td>1.25 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>1.11 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/layer_norm</summary>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.90 (n/a)</td><td>390.26 (n/a)</td><td>419.20 (n/a)</td><td>261.70 (n/a)</td><td>118.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.30 (n/a)</td><td>423.56 (n/a)</td><td>384.30 (n/a)</td><td>268.90 (n/a)</td><td>163.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.30 (n/a)</td><td>364.36 (n/a)</td><td>311.30 (n/a)</td><td>223.00 (n/a)</td><td>135.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.90 (n/a)</td><td>438.06 (n/a)</td><td>459.00 (n/a)</td><td>281.80 (n/a)</td><td>104.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.40 (n/a)</td><td>363.76 (n/a)</td><td>288.10 (n/a)</td><td>237.00 (n/a)</td><td>151.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1990.90 (n/a)</td><td>810.92 (n/a)</td><td>550.20 (n/a)</td><td>473.90 (n/a)</td><td>660.60 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.40 (n/a)</td><td>405.78 (n/a)</td><td>419.60 (n/a)</td><td>231.50 (n/a)</td><td>145.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.60 (n/a)</td><td>394.72 (n/a)</td><td>341.40 (n/a)</td><td>286.40 (n/a)</td><td>110.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.70 (n/a)</td><td>417.86 (n/a)</td><td>351.80 (n/a)</td><td>297.10 (n/a)</td><td>141.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.90 (n/a)</td><td>411.44 (n/a)</td><td>387.80 (n/a)</td><td>238.00 (n/a)</td><td>160.64 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.00 (n/a)</td><td>442.70 (n/a)</td><td>470.30 (n/a)</td><td>228.80 (n/a)</td><td>179.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.60 (n/a)</td><td>494.82 (n/a)</td><td>482.80 (n/a)</td><td>337.60 (n/a)</td><td>104.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>647.70 (n/a)</td><td>368.36 (n/a)</td><td>306.00 (n/a)</td><td>277.80 (n/a)</td><td>156.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>625.70 (n/a)</td><td>469.16 (n/a)</td><td>510.20 (n/a)</td><td>157.70 (n/a)</td><td>183.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>536.60 (n/a)</td><td>367.92 (n/a)</td><td>322.00 (n/a)</td><td>228.70 (n/a)</td><td>126.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>499.20 (n/a)</td><td>352.36 (n/a)</td><td>299.40 (n/a)</td><td>237.20 (n/a)</td><td>118.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>596.20 (n/a)</td><td>428.20 (n/a)</td><td>372.90 (n/a)</td><td>303.10 (n/a)</td><td>140.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.10 (n/a)</td><td>443.78 (n/a)</td><td>450.10 (n/a)</td><td>237.50 (n/a)</td><td>161.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (-0.98%)</td><td>0.09 (-3.16%)</td><td>0.09 (-10.16%)</td><td>0.05 (-14.90%)</td><td>0.03 (-6.20%)</td><td>610.90 (+17.53%)</td><td>394.50 (+3.21%)</td><td>345.30 (+11.32%)</td><td>280.00 (+0.97%)</td><td>135.03 (+8.07%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>519.80 (n/a)</td><td>382.22 (n/a)</td><td>310.20 (n/a)</td><td>277.30 (n/a)</td><td>124.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.30 (n/a)</td><td>450.94 (n/a)</td><td>485.30 (n/a)</td><td>278.60 (n/a)</td><td>129.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>690.60 (n/a)</td><td>457.88 (n/a)</td><td>486.70 (n/a)</td><td>283.20 (n/a)</td><td>164.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>556.70 (n/a)</td><td>475.76 (n/a)</td><td>486.40 (n/a)</td><td>346.50 (n/a)</td><td>78.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>616.80 (n/a)</td><td>424.64 (n/a)</td><td>485.90 (n/a)</td><td>190.70 (n/a)</td><td>181.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>615.30 (n/a)</td><td>433.56 (n/a)</td><td>403.70 (n/a)</td><td>310.10 (n/a)</td><td>127.65 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (-10.66%)</td><td>0.01 (+3.44%)</td><td>0.01 (-3.55%)</td><td>0.01 (+3.30%)</td><td>0.00 <b>(-23.27%)</b></td><td>513.60 (-3.20%)</td><td>340.18 (-7.94%)</td><td>305.20 (+3.67%)</td><td>237.80 (+11.91%)</td><td>111.27 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.60 (n/a)</td><td>369.50 (n/a)</td><td>294.40 (n/a)</td><td>212.50 (n/a)</td><td>144.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+18.51%)</td><td>0.01 <b>(+21.69%)</b></td><td>0.01 <b>(+55.00%)</b></td><td>0.01 (-4.05%)</td><td>0.01 <b>(+34.66%)</b></td><td>503.40 (+4.22%)</td><td>330.78 (-13.47%)</td><td>291.90 <b>(-35.49%)</b></td><td>187.30 (-15.59%)</td><td>143.12 (+16.38%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.00 (n/a)</td><td>382.28 (n/a)</td><td>452.50 (n/a)</td><td>221.90 (n/a)</td><td>122.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+17.89%)</td><td>0.01 <b>(+21.71%)</b></td><td>0.01 (-8.51%)</td><td>0.01 <b>(+96.80%)</b></td><td>0.00 (-8.06%)</td><td>488.90 <b>(-49.18%)</b></td><td>352.54 <b>(-28.59%)</b></td><td>379.60 (+9.27%)</td><td>234.50 (-15.16%)</td><td>114.20 <b>(-61.18%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>962.10 (n/a)</td><td>493.70 (n/a)</td><td>347.40 (n/a)</td><td>276.40 (n/a)</td><td>294.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(+21.57%)</b></td><td>0.01 (+10.57%)</td><td>0.02 <b>(+21.72%)</b></td><td>0.01 <b>(+48.43%)</b></td><td>0.01 <b>(+29.17%)</b></td><td>547.10 <b>(-32.63%)</b></td><td>356.72 (-10.90%)</td><td>247.80 (-17.84%)</td><td>231.40 (-17.77%)</td><td>160.43 <b>(-30.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>812.10 (n/a)</td><td>400.38 (n/a)</td><td>301.60 (n/a)</td><td>281.40 (n/a)</td><td>230.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(+27.55%)</b></td><td>0.01 (+4.09%)</td><td>0.01 (+4.08%)</td><td>0.01 (-12.28%)</td><td>0.01 <b>(+62.27%)</b></td><td>603.00 (+14.01%)</td><td>418.58 (+3.87%)</td><td>426.30 (-3.92%)</td><td>211.10 <b>(-21.58%)</b></td><td>158.85 <b>(+47.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.90 (n/a)</td><td>403.00 (n/a)</td><td>443.70 (n/a)</td><td>269.20 (n/a)</td><td>107.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (-16.67%)</td><td>0.01 (-17.34%)</td><td>0.01 (-18.83%)</td><td>0.01 <b>(+81.22%)</b></td><td>0.00 <b>(-49.02%)</b></td><td>587.20 <b>(-44.81%)</b></td><td>435.90 (-3.37%)</td><td>400.50 <b>(+23.19%)</b></td><td>303.00 <b>(+20.00%)</b></td><td>108.32 <b>(-68.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1064.00 (n/a)</td><td>451.08 (n/a)</td><td>325.10 (n/a)</td><td>252.50 (n/a)</td><td>344.69 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+15.84%)</td><td>0.03 (+4.65%)</td><td>0.03 (+18.12%)</td><td>0.01 <b>(-32.18%)</b></td><td>0.01 <b>(+90.77%)</b></td><td>692.50 <b>(+47.47%)</b></td><td>352.98 (+10.11%)</td><td>248.50 (-15.33%)</td><td>213.60 (-13.70%)</td><td>200.65 <b>(+131.96%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.60 (n/a)</td><td>320.56 (n/a)</td><td>293.50 (n/a)</td><td>247.50 (n/a)</td><td>86.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+2.27%)</td><td>0.02 (-6.34%)</td><td>0.02 (-4.96%)</td><td>0.01 (+6.98%)</td><td>0.01 <b>(-22.40%)</b></td><td>596.80 (-6.53%)</td><td>444.64 (+0.67%)</td><td>451.90 (+5.22%)</td><td>265.70 (-2.21%)</td><td>120.86 <b>(-29.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.50 (n/a)</td><td>441.68 (n/a)</td><td>429.50 (n/a)</td><td>271.70 (n/a)</td><td>172.61 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-4.04%)</td><td>0.02 (+1.05%)</td><td>0.02 (+9.77%)</td><td>0.01 (-8.62%)</td><td>0.01 (-7.55%)</td><td>636.90 (+9.43%)</td><td>411.00 (-2.06%)</td><td>415.80 (-8.90%)</td><td>245.00 (+4.21%)</td><td>160.06 (+1.11%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.00 (n/a)</td><td>419.66 (n/a)</td><td>456.40 (n/a)</td><td>235.10 (n/a)</td><td>158.30 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-6.26%)</td><td>0.03 (+13.84%)</td><td>0.03 <b>(+35.17%)</b></td><td>0.02 (+19.88%)</td><td>0.01 (-18.41%)</td><td>468.10 (-16.57%)</td><td>318.48 (-14.83%)</td><td>283.30 <b>(-26.03%)</b></td><td>249.60 (+6.71%)</td><td>89.52 <b>(-26.60%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.10 (n/a)</td><td>373.92 (n/a)</td><td>383.00 (n/a)</td><td>233.90 (n/a)</td><td>121.97 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+7.18%)</td><td>0.02 (-15.72%)</td><td>0.02 <b>(-31.43%)</b></td><td>0.01 (-9.83%)</td><td>0.01 <b>(+32.51%)</b></td><td>574.40 (+10.91%)</td><td>396.44 <b>(+26.23%)</b></td><td>424.20 <b>(+45.82%)</b></td><td>214.70 (-6.69%)</td><td>157.62 <b>(+33.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.90 (n/a)</td><td>314.06 (n/a)</td><td>290.90 (n/a)</td><td>230.10 (n/a)</td><td>118.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 <b>(-23.70%)</b></td><td>0.02 (+10.91%)</td><td>0.02 (+7.19%)</td><td>0.02 <b>(+296.74%)</b></td><td>0.01 <b>(-54.94%)</b></td><td>524.30 <b>(-74.79%)</b></td><td>394.26 <b>(-44.98%)</b></td><td>370.80 (-6.69%)</td><td>305.40 <b>(+31.07%)</b></td><td>96.54 <b>(-87.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2080.00 (n/a)</td><td>716.52 (n/a)</td><td>397.40 (n/a)</td><td>233.00 (n/a)</td><td>768.15 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+16.43%)</td><td>0.02 (+4.77%)</td><td>0.02 (-5.20%)</td><td>0.01 <b>(+233.76%)</b></td><td>0.01 (-10.04%)</td><td>610.90 <b>(-70.04%)</b></td><td>393.50 <b>(-39.12%)</b></td><td>333.00 (+5.48%)</td><td>222.00 (-14.12%)</td><td>167.44 <b>(-78.50%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2039.00 (n/a)</td><td>646.38 (n/a)</td><td>315.70 (n/a)</td><td>258.50 (n/a)</td><td>778.94 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+5.28%)</td><td>0.02 (-17.07%)</td><td>0.02 (-17.38%)</td><td>0.00 <b>(-73.70%)</b></td><td>0.01 <b>(+68.91%)</b></td><td>2420.40 <b>(+280.27%)</b></td><td>830.30 <b>(+89.84%)</b></td><td>489.80 <b>(+21.03%)</b></td><td>305.70 (-5.03%)</td><td>892.77 <b>(+607.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.50 (n/a)</td><td>437.36 (n/a)</td><td>404.70 (n/a)</td><td>321.90 (n/a)</td><td>126.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (-13.23%)</td><td>0.04 (-15.02%)</td><td>0.04 <b>(-36.39%)</b></td><td>0.03 <b>(+388.82%)</b></td><td>0.01 <b>(-51.45%)</b></td><td>510.80 <b>(-79.54%)</b></td><td>419.80 <b>(-41.93%)</b></td><td>466.30 <b>(+57.22%)</b></td><td>276.30 (+15.22%)</td><td>102.55 <b>(-89.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2496.80 (n/a)</td><td>722.90 (n/a)</td><td>296.60 (n/a)</td><td>239.80 (n/a)</td><td>991.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(+82.53%)</b></td><td>0.06 <b>(+70.90%)</b></td><td>0.06 <b>(+78.47%)</b></td><td>0.03 (+17.50%)</td><td>0.02 <b>(+219.02%)</b></td><td>510.20 (-14.90%)</td><td>303.96 <b>(-36.94%)</b></td><td>254.00 <b>(-43.97%)</b></td><td>213.90 <b>(-45.22%)</b></td><td>120.51 <b>(+52.47%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>599.50 (n/a)</td><td>482.02 (n/a)</td><td>453.30 (n/a)</td><td>390.50 (n/a)</td><td>79.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 <b>(+56.27%)</b></td><td>0.04 <b>(+24.68%)</b></td><td>0.03 (-1.83%)</td><td>0.01 (-19.53%)</td><td>0.02 <b>(+68.70%)</b></td><td>2430.80 <b>(+24.27%)</b></td><td>791.34 (+5.02%)</td><td>475.40 (+1.86%)</td><td>221.70 <b>(-36.02%)</b></td><td>922.46 <b>(+36.42%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1956.10 (n/a)</td><td>753.54 (n/a)</td><td>466.70 (n/a)</td><td>346.50 (n/a)</td><td>676.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (-5.13%)</td><td>0.05 (-2.92%)</td><td>0.05 (-2.06%)</td><td>0.03 (-1.43%)</td><td>0.01 (-10.11%)</td><td>498.70 (+1.44%)</td><td>351.64 (+2.03%)</td><td>309.60 (+2.08%)</td><td>246.80 (+5.43%)</td><td>100.92 (-4.02%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.60 (n/a)</td><td>344.64 (n/a)</td><td>303.30 (n/a)</td><td>234.10 (n/a)</td><td>105.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+16.83%)</td><td>0.05 (+17.22%)</td><td>0.05 <b>(+37.97%)</b></td><td>0.03 (-5.92%)</td><td>0.02 <b>(+20.97%)</b></td><td>557.00 (+6.30%)</td><td>361.50 (-12.93%)</td><td>338.30 <b>(-27.53%)</b></td><td>230.50 (-14.41%)</td><td>131.27 (+7.88%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>524.00 (n/a)</td><td>415.18 (n/a)</td><td>466.80 (n/a)</td><td>269.30 (n/a)</td><td>121.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 <b>(-42.46%)</b></td><td>0.04 (-2.06%)</td><td>0.04 <b>(+37.09%)</b></td><td>0.03 <b>(+65.62%)</b></td><td>0.00 <b>(-78.69%)</b></td><td>514.50 <b>(-39.62%)</b></td><td>417.48 (-17.76%)</td><td>392.30 <b>(-27.05%)</b></td><td>371.10 <b>(+73.82%)</b></td><td>57.99 <b>(-76.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>852.10 (n/a)</td><td>507.64 (n/a)</td><td>537.80 (n/a)</td><td>213.50 (n/a)</td><td>248.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (-18.93%)</td><td>0.07 <b>(-20.65%)</b></td><td>0.08 (-10.93%)</td><td>0.04 (-19.79%)</td><td>0.03 <b>(-20.44%)</b></td><td>807.70 <b>(+24.68%)</b></td><td>517.54 <b>(+25.97%)</b></td><td>430.10 (+12.27%)</td><td>304.80 <b>(+23.35%)</b></td><td>199.17 <b>(+25.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>647.80 (n/a)</td><td>410.84 (n/a)</td><td>383.10 (n/a)</td><td>247.10 (n/a)</td><td>158.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (-9.67%)</td><td>0.08 (-0.87%)</td><td>0.06 (-9.63%)</td><td>0.06 <b>(+249.43%)</b></td><td>0.03 <b>(-37.13%)</b></td><td>575.90 <b>(-71.38%)</b></td><td>432.68 <b>(-37.15%)</b></td><td>505.00 (+10.65%)</td><td>261.20 (+10.72%)</td><td>142.70 <b>(-80.94%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2012.50 (n/a)</td><td>688.42 (n/a)</td><td>456.40 (n/a)</td><td>235.90 (n/a)</td><td>748.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (+17.55%)</td><td>0.08 (+2.34%)</td><td>0.05 (-19.48%)</td><td>0.05 (-18.54%)</td><td>0.04 <b>(+53.99%)</b></td><td>721.60 <b>(+22.76%)</b></td><td>492.96 (+8.99%)</td><td>599.80 <b>(+24.18%)</b></td><td>227.20 (-14.91%)</td><td>210.98 <b>(+59.75%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.80 (n/a)</td><td>452.28 (n/a)</td><td>483.00 (n/a)</td><td>267.00 (n/a)</td><td>132.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (-2.13%)</td><td>0.09 (+5.05%)</td><td>0.10 <b>(+33.03%)</b></td><td>0.07 (-5.73%)</td><td>0.02 (+12.66%)</td><td>484.60 (+6.09%)</td><td>375.46 (-3.57%)</td><td>318.40 <b>(-24.83%)</b></td><td>291.80 (+2.17%)</td><td>92.02 <b>(+24.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>456.80 (n/a)</td><td>389.38 (n/a)</td><td>423.60 (n/a)</td><td>285.60 (n/a)</td><td>74.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 <b>(+40.61%)</b></td><td>0.07 (+3.74%)</td><td>0.07 (+11.65%)</td><td>0.02 <b>(-69.84%)</b></td><td>0.04 <b>(+211.24%)</b></td><td>2015.90 <b>(+231.56%)</b></td><td>750.24 <b>(+45.11%)</b></td><td>473.30 (-10.43%)</td><td>281.60 <b>(-28.89%)</b></td><td>713.51 <b>(+754.29%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>608.00 (n/a)</td><td>517.02 (n/a)</td><td>528.40 (n/a)</td><td>396.00 (n/a)</td><td>83.52 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (-1.99%)</td><td>0.01 (-16.14%)</td><td>0.01 <b>(-38.19%)</b></td><td>0.01 (+1.34%)</td><td>0.00 <b>(+25.07%)</b></td><td>518.90 (-1.31%)</td><td>395.90 <b>(+23.49%)</b></td><td>470.40 <b>(+61.76%)</b></td><td>244.50 (+2.00%)</td><td>136.08 (+16.41%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.80 (n/a)</td><td>320.58 (n/a)</td><td>290.80 (n/a)</td><td>239.70 (n/a)</td><td>116.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (-7.54%)</td><td>0.01 (-3.93%)</td><td>0.01 (-4.53%)</td><td>0.01 (-7.79%)</td><td>0.00 (-5.69%)</td><td>537.00 (+8.46%)</td><td>316.50 (+4.64%)</td><td>274.90 (+4.72%)</td><td>230.00 (+8.13%)</td><td>125.05 (+11.82%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.10 (n/a)</td><td>302.48 (n/a)</td><td>262.50 (n/a)</td><td>212.70 (n/a)</td><td>111.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (-2.27%)</td><td>0.01 (-6.98%)</td><td>0.01 (-7.76%)</td><td>0.01 (-18.02%)</td><td>0.01 (-4.56%)</td><td>764.90 <b>(+21.97%)</b></td><td>432.98 (+9.23%)</td><td>292.60 (+8.41%)</td><td>240.10 (+2.34%)</td><td>236.70 (+15.70%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.10 (n/a)</td><td>396.38 (n/a)</td><td>269.90 (n/a)</td><td>234.60 (n/a)</td><td>204.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-35.73%)</b></td><td>0.01 (-13.66%)</td><td>0.01 <b>(+27.69%)</b></td><td>0.01 (-18.81%)</td><td>0.00 <b>(-49.73%)</b></td><td>596.40 <b>(+23.17%)</b></td><td>371.48 (+5.18%)</td><td>327.70 <b>(-21.70%)</b></td><td>245.20 <b>(+55.58%)</b></td><td>139.07 (-5.37%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>484.20 (n/a)</td><td>353.20 (n/a)</td><td>418.50 (n/a)</td><td>157.60 (n/a)</td><td>146.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+15.29%)</td><td>0.02 (+14.98%)</td><td>0.02 (+4.33%)</td><td>0.01 <b>(+24.63%)</b></td><td>0.00 (-11.88%)</td><td>371.60 (-19.76%)</td><td>267.20 (-16.06%)</td><td>242.50 (-4.15%)</td><td>201.90 (-13.27%)</td><td>67.09 <b>(-36.80%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.10 (n/a)</td><td>318.34 (n/a)</td><td>253.00 (n/a)</td><td>232.80 (n/a)</td><td>106.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (-4.05%)</td><td>0.02 (+5.34%)</td><td>0.02 (+5.49%)</td><td>0.01 <b>(+52.83%)</b></td><td>0.00 <b>(-56.33%)</b></td><td>317.10 <b>(-34.58%)</b></td><td>268.36 (-10.80%)</td><td>260.10 (-5.21%)</td><td>242.00 (+4.22%)</td><td>30.22 <b>(-71.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.70 (n/a)</td><td>300.86 (n/a)</td><td>274.40 (n/a)</td><td>232.20 (n/a)</td><td>104.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+6.21%)</td><td>0.01 (+5.33%)</td><td>0.01 (-14.45%)</td><td>0.01 (-8.92%)</td><td>0.00 <b>(+46.80%)</b></td><td>593.90 (+9.78%)</td><td>393.42 (+1.76%)</td><td>441.80 (+16.91%)</td><td>232.70 (-5.87%)</td><td>154.39 <b>(+41.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.00 (n/a)</td><td>386.62 (n/a)</td><td>377.90 (n/a)</td><td>247.20 (n/a)</td><td>108.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+8.90%)</td><td>0.01 (+5.25%)</td><td>0.01 (+6.39%)</td><td>0.01 <b>(-26.27%)</b></td><td>0.00 <b>(+49.27%)</b></td><td>688.10 <b>(+35.64%)</b></td><td>382.06 (+4.63%)</td><td>308.30 (-6.01%)</td><td>229.70 (-8.19%)</td><td>188.75 <b>(+81.91%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.30 (n/a)</td><td>365.14 (n/a)</td><td>328.00 (n/a)</td><td>250.20 (n/a)</td><td>103.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-24.99%)</b></td><td>0.02 <b>(+25.89%)</b></td><td>0.02 <b>(+74.47%)</b></td><td>0.01 <b>(+98.92%)</b></td><td>0.00 <b>(-81.17%)</b></td><td>305.40 <b>(-49.74%)</b></td><td>270.30 <b>(-36.00%)</b></td><td>272.30 <b>(-42.69%)</b></td><td>242.00 <b>(+33.33%)</b></td><td>23.42 <b>(-87.79%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.60 (n/a)</td><td>422.32 (n/a)</td><td>475.10 (n/a)</td><td>181.50 (n/a)</td><td>191.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+0.81%)</td><td>0.01 (+2.09%)</td><td>0.01 (+1.89%)</td><td>0.01 (+7.80%)</td><td>0.00 (-6.99%)</td><td>531.60 (-7.24%)</td><td>365.62 (-4.05%)</td><td>360.90 (-1.85%)</td><td>242.80 (-0.82%)</td><td>123.03 (-13.40%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.10 (n/a)</td><td>381.04 (n/a)</td><td>367.70 (n/a)</td><td>244.80 (n/a)</td><td>142.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(+40.68%)</b></td><td>0.01 (+16.36%)</td><td>0.01 (+9.44%)</td><td>0.01 (-3.09%)</td><td>0.00 <b>(+86.84%)</b></td><td>656.00 (+3.19%)</td><td>443.76 (-6.71%)</td><td>423.10 (-8.62%)</td><td>217.90 <b>(-28.93%)</b></td><td>168.01 <b>(+36.34%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.70 (n/a)</td><td>475.68 (n/a)</td><td>463.00 (n/a)</td><td>306.60 (n/a)</td><td>123.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (-12.40%)</td><td>0.01 <b>(-34.93%)</b></td><td>0.01 <b>(-50.06%)</b></td><td>0.01 (-11.51%)</td><td>0.00 (-13.27%)</td><td>625.80 (+13.00%)</td><td>516.00 <b>(+52.55%)</b></td><td>572.70 <b>(+100.24%)</b></td><td>304.90 (+14.15%)</td><td>126.32 (+3.82%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.80 (n/a)</td><td>338.26 (n/a)</td><td>286.00 (n/a)</td><td>267.10 (n/a)</td><td>121.67 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (-9.53%)</td><td>0.03 (-6.51%)</td><td>0.03 (-7.93%)</td><td>0.02 (+17.79%)</td><td>0.01 <b>(-32.98%)</b></td><td>393.40 (-15.11%)</td><td>306.56 (+2.63%)</td><td>307.40 (+8.58%)</td><td>230.80 (+10.54%)</td><td>58.61 <b>(-40.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>463.40 (n/a)</td><td>298.70 (n/a)</td><td>283.10 (n/a)</td><td>208.80 (n/a)</td><td>97.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+3.69%)</td><td>0.03 (+18.14%)</td><td>0.03 (+2.01%)</td><td>0.03 <b>(+76.45%)</b></td><td>0.00 <b>(-53.10%)</b></td><td>319.80 <b>(-43.32%)</b></td><td>288.96 <b>(-21.84%)</b></td><td>297.30 (-1.98%)</td><td>237.50 (-3.53%)</td><td>32.79 <b>(-75.00%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.20 (n/a)</td><td>369.70 (n/a)</td><td>303.30 (n/a)</td><td>246.20 (n/a)</td><td>131.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 <b>(-28.05%)</b></td><td>0.02 <b>(-31.30%)</b></td><td>0.02 <b>(-45.09%)</b></td><td>0.01 (-15.52%)</td><td>0.01 <b>(-34.82%)</b></td><td>638.20 (+18.36%)</td><td>473.00 <b>(+39.21%)</b></td><td>492.20 <b>(+82.16%)</b></td><td>266.90 <b>(+39.01%)</b></td><td>155.23 (+4.40%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.20 (n/a)</td><td>339.78 (n/a)</td><td>270.20 (n/a)</td><td>192.00 (n/a)</td><td>148.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+4.16%)</td><td>0.03 (-17.35%)</td><td>0.03 (-18.48%)</td><td>0.01 (-19.28%)</td><td>0.01 <b>(+25.34%)</b></td><td>571.60 <b>(+23.88%)</b></td><td>366.36 <b>(+27.63%)</b></td><td>295.70 <b>(+22.70%)</b></td><td>226.50 (-3.98%)</td><td>147.11 <b>(+50.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.40 (n/a)</td><td>287.04 (n/a)</td><td>241.00 (n/a)</td><td>235.90 (n/a)</td><td>98.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+19.62%)</td><td>0.03 (+9.36%)</td><td>0.03 (+1.87%)</td><td>0.02 (+6.66%)</td><td>0.01 (+18.50%)</td><td>525.00 (-6.25%)</td><td>303.20 (-7.59%)</td><td>258.70 (-1.82%)</td><td>194.70 (-16.40%)</td><td>128.79 (-4.12%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.00 (n/a)</td><td>328.12 (n/a)</td><td>263.50 (n/a)</td><td>232.90 (n/a)</td><td>134.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-16.06%)</td><td>0.03 (-13.64%)</td><td>0.03 (-19.79%)</td><td>0.02 <b>(+25.40%)</b></td><td>0.01 <b>(-38.46%)</b></td><td>527.30 <b>(-20.25%)</b></td><td>348.96 (+2.95%)</td><td>292.30 <b>(+24.65%)</b></td><td>246.30 (+19.10%)</td><td>117.40 <b>(-39.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.20 (n/a)</td><td>338.96 (n/a)</td><td>234.50 (n/a)</td><td>206.80 (n/a)</td><td>193.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+6.14%)</td><td>0.02 (-3.25%)</td><td>0.02 (-9.05%)</td><td>0.02 (+10.81%)</td><td>0.01 (-10.22%)</td><td>491.50 (-9.75%)</td><td>384.56 (+0.26%)</td><td>432.80 (+9.96%)</td><td>226.80 (-5.77%)</td><td>113.93 (-18.71%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.60 (n/a)</td><td>383.56 (n/a)</td><td>393.60 (n/a)</td><td>240.70 (n/a)</td><td>140.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+7.20%)</td><td>0.02 (+7.04%)</td><td>0.02 (+14.51%)</td><td>0.02 (+12.86%)</td><td>0.01 (-10.91%)</td><td>507.40 (-11.40%)</td><td>375.72 (-9.76%)</td><td>421.60 (-12.68%)</td><td>243.70 (-6.74%)</td><td>111.01 <b>(-23.26%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.70 (n/a)</td><td>416.36 (n/a)</td><td>482.80 (n/a)</td><td>261.30 (n/a)</td><td>144.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 <b>(+21.90%)</b></td><td>0.02 (-13.85%)</td><td>0.02 <b>(-37.86%)</b></td><td>0.02 (-11.90%)</td><td>0.01 <b>(+30.71%)</b></td><td>541.40 (+13.50%)</td><td>399.82 <b>(+20.59%)</b></td><td>420.80 <b>(+60.92%)</b></td><td>197.40 (-17.96%)</td><td>131.76 (+16.63%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.00 (n/a)</td><td>331.54 (n/a)</td><td>261.50 (n/a)</td><td>240.60 (n/a)</td><td>112.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+0.38%)</td><td>0.02 (-11.91%)</td><td>0.02 <b>(-26.23%)</b></td><td>0.02 (+2.98%)</td><td>0.01 (-5.89%)</td><td>543.00 (-2.88%)</td><td>417.42 (+11.40%)</td><td>418.80 <b>(+35.53%)</b></td><td>245.10 (-0.37%)</td><td>109.33 (-16.25%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.10 (n/a)</td><td>374.72 (n/a)</td><td>309.00 (n/a)</td><td>246.00 (n/a)</td><td>130.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+3.88%)</td><td>0.02 <b>(+30.91%)</b></td><td>0.02 <b>(+46.55%)</b></td><td>0.02 <b>(+38.23%)</b></td><td>0.00 <b>(-29.89%)</b></td><td>446.50 <b>(-27.66%)</b></td><td>355.48 <b>(-26.68%)</b></td><td>342.20 <b>(-31.75%)</b></td><td>281.50 (-3.76%)</td><td>62.93 <b>(-48.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.20 (n/a)</td><td>484.84 (n/a)</td><td>501.40 (n/a)</td><td>292.50 (n/a)</td><td>121.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+14.76%)</td><td>0.02 <b>(+49.72%)</b></td><td>0.03 <b>(+76.99%)</b></td><td>0.01 <b>(+302.68%)</b></td><td>0.01 (+3.85%)</td><td>620.40 <b>(-75.17%)</b></td><td>409.08 <b>(-53.32%)</b></td><td>293.10 <b>(-43.49%)</b></td><td>278.30 (-12.84%)</td><td>171.25 <b>(-81.20%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2498.20 (n/a)</td><td>876.26 (n/a)</td><td>518.70 (n/a)</td><td>319.30 (n/a)</td><td>910.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 <b>(+49.58%)</b></td><td>0.05 (+2.77%)</td><td>0.03 <b>(-42.39%)</b></td><td>0.03 (+11.00%)</td><td>0.03 <b>(+114.07%)</b></td><td>537.50 (-9.91%)</td><td>396.34 (+12.73%)</td><td>515.30 <b>(+73.62%)</b></td><td>171.80 <b>(-33.15%)</b></td><td>183.43 <b>(+31.28%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>596.60 (n/a)</td><td>351.58 (n/a)</td><td>296.80 (n/a)</td><td>257.00 (n/a)</td><td>139.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+0.40%)</td><td>0.04 (-11.55%)</td><td>0.03 <b>(-20.82%)</b></td><td>0.03 (-13.06%)</td><td>0.02 <b>(+25.72%)</b></td><td>588.50 (+15.03%)</td><td>436.52 (+19.82%)</td><td>482.80 <b>(+26.29%)</b></td><td>235.50 (-0.42%)</td><td>156.49 <b>(+49.62%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.60 (n/a)</td><td>364.32 (n/a)</td><td>382.30 (n/a)</td><td>236.50 (n/a)</td><td>104.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+17.68%)</td><td>0.06 <b>(+66.22%)</b></td><td>0.06 <b>(+99.47%)</b></td><td>0.04 <b>(+61.01%)</b></td><td>0.01 <b>(-24.61%)</b></td><td>405.80 <b>(-37.89%)</b></td><td>305.28 <b>(-43.41%)</b></td><td>297.00 <b>(-49.87%)</b></td><td>242.90 (-15.01%)</td><td>62.43 <b>(-57.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>653.40 (n/a)</td><td>539.48 (n/a)</td><td>592.50 (n/a)</td><td>285.80 (n/a)</td><td>146.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(+27.86%)</b></td><td>0.05 <b>(+20.82%)</b></td><td>0.05 <b>(+30.88%)</b></td><td>0.03 (-3.09%)</td><td>0.02 <b>(+59.20%)</b></td><td>641.80 (+3.18%)</td><td>376.24 (-9.76%)</td><td>311.90 <b>(-23.59%)</b></td><td>204.60 <b>(-21.79%)</b></td><td>182.02 <b>(+29.80%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>622.00 (n/a)</td><td>416.94 (n/a)</td><td>408.20 (n/a)</td><td>261.60 (n/a)</td><td>140.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 <b>(+34.05%)</b></td><td>0.05 <b>(+73.57%)</b></td><td>0.07 <b>(+106.12%)</b></td><td>0.03 <b>(+338.04%)</b></td><td>0.02 (+17.38%)</td><td>563.10 <b>(-77.17%)</b></td><td>345.78 <b>(-60.00%)</b></td><td>249.70 <b>(-51.49%)</b></td><td>220.10 <b>(-25.42%)</b></td><td>153.31 <b>(-82.99%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2466.80 (n/a)</td><td>864.40 (n/a)</td><td>514.70 (n/a)</td><td>295.10 (n/a)</td><td>901.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (-3.26%)</td><td>0.05 (-16.95%)</td><td>0.04 <b>(-28.33%)</b></td><td>0.03 <b>(-24.16%)</b></td><td>0.02 <b>(+35.74%)</b></td><td>578.40 <b>(+31.87%)</b></td><td>405.04 <b>(+30.47%)</b></td><td>377.90 <b>(+39.55%)</b></td><td>243.60 (+3.35%)</td><td>162.63 <b>(+88.83%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>438.60 (n/a)</td><td>310.44 (n/a)</td><td>270.80 (n/a)</td><td>235.70 (n/a)</td><td>86.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (-3.31%)</td><td>0.05 (-1.77%)</td><td>0.06 <b>(+27.54%)</b></td><td>0.03 <b>(-26.39%)</b></td><td>0.02 (+13.22%)</td><td>629.30 <b>(+35.86%)</b></td><td>382.00 (+7.96%)</td><td>287.20 <b>(-21.59%)</b></td><td>248.10 (+3.42%)</td><td>170.99 <b>(+56.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>463.20 (n/a)</td><td>353.82 (n/a)</td><td>366.30 (n/a)</td><td>239.90 (n/a)</td><td>109.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (-1.08%)</td><td>0.05 (+1.03%)</td><td>0.07 (+6.32%)</td><td>0.03 (-1.26%)</td><td>0.02 (+3.39%)</td><td>543.30 (+1.27%)</td><td>346.98 (-0.25%)</td><td>251.30 (-5.95%)</td><td>239.20 (+1.06%)</td><td>141.17 (+3.74%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>536.50 (n/a)</td><td>347.86 (n/a)</td><td>267.20 (n/a)</td><td>236.70 (n/a)</td><td>136.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+13.03%)</td><td>0.05 <b>(+22.56%)</b></td><td>0.05 <b>(+36.83%)</b></td><td>0.03 (-2.44%)</td><td>0.02 <b>(+40.27%)</b></td><td>642.80 (+2.49%)</td><td>412.62 (-12.82%)</td><td>340.60 <b>(-26.91%)</b></td><td>242.70 (-11.52%)</td><td>184.75 <b>(+26.06%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>627.20 (n/a)</td><td>473.32 (n/a)</td><td>466.00 (n/a)</td><td>274.30 (n/a)</td><td>146.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (-0.26%)</td><td>0.05 (+0.91%)</td><td>0.06 (+3.92%)</td><td>0.03 <b>(-20.14%)</b></td><td>0.02 (+9.88%)</td><td>575.70 <b>(+25.23%)</b></td><td>334.66 (+2.64%)</td><td>276.60 (-3.76%)</td><td>242.60 (+0.29%)</td><td>138.59 <b>(+44.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>459.70 (n/a)</td><td>326.04 (n/a)</td><td>287.40 (n/a)</td><td>241.90 (n/a)</td><td>96.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (+3.61%)</td><td>0.04 (-12.28%)</td><td>0.04 <b>(-27.28%)</b></td><td>0.03 (-10.86%)</td><td>0.01 (+7.19%)</td><td>604.10 (+12.18%)</td><td>424.84 (+15.48%)</td><td>424.30 <b>(+37.49%)</b></td><td>262.60 (-3.46%)</td><td>129.77 (+14.88%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.50 (n/a)</td><td>367.88 (n/a)</td><td>308.60 (n/a)</td><td>272.00 (n/a)</td><td>112.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+12.11%)</td><td>0.05 (+10.55%)</td><td>0.05 <b>(+24.96%)</b></td><td>0.03 (+16.65%)</td><td>0.01 (-6.98%)</td><td>493.30 (-14.28%)</td><td>357.50 (-12.24%)</td><td>314.70 (-19.96%)</td><td>236.20 (-10.80%)</td><td>108.38 <b>(-24.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>575.50 (n/a)</td><td>407.34 (n/a)</td><td>393.20 (n/a)</td><td>264.80 (n/a)</td><td>143.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (+6.85%)</td><td>0.11 (+12.09%)</td><td>0.12 (+9.52%)</td><td>0.05 <b>(-20.55%)</b></td><td>0.03 (+13.28%)</td><td>640.40 <b>(+25.86%)</b></td><td>345.98 (-7.12%)</td><td>277.70 (-8.68%)</td><td>248.80 (-6.43%)</td><td>165.54 <b>(+35.95%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>508.80 (n/a)</td><td>372.52 (n/a)</td><td>304.10 (n/a)</td><td>265.90 (n/a)</td><td>121.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (-1.71%)</td><td>0.09 (-16.11%)</td><td>0.08 <b>(-31.21%)</b></td><td>0.06 (-0.94%)</td><td>0.03 (+11.89%)</td><td>554.50 (+0.97%)</td><td>396.42 <b>(+20.71%)</b></td><td>406.40 <b>(+45.35%)</b></td><td>260.30 (+1.76%)</td><td>130.34 (+5.11%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>549.20 (n/a)</td><td>328.40 (n/a)</td><td>279.60 (n/a)</td><td>255.80 (n/a)</td><td>124.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (+16.43%)</td><td>0.10 (-7.72%)</td><td>0.07 <b>(-45.84%)</b></td><td>0.05 (-11.93%)</td><td>0.05 <b>(+24.53%)</b></td><td>614.30 (+13.55%)</td><td>406.90 (+13.83%)</td><td>473.90 <b>(+84.68%)</b></td><td>203.20 (-14.12%)</td><td>173.78 (+16.42%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>541.00 (n/a)</td><td>357.46 (n/a)</td><td>256.60 (n/a)</td><td>236.60 (n/a)</td><td>149.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 <b>(+22.34%)</b></td><td>0.09 <b>(+20.83%)</b></td><td>0.07 (+1.95%)</td><td>0.06 (+0.84%)</td><td>0.03 <b>(+98.69%)</b></td><td>533.80 (-0.84%)</td><td>412.00 (-11.06%)</td><td>483.60 (-1.93%)</td><td>261.30 (-18.27%)</td><td>137.77 <b>(+62.47%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>538.30 (n/a)</td><td>463.22 (n/a)</td><td>493.10 (n/a)</td><td>319.70 (n/a)</td><td>84.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 <b>(+39.98%)</b></td><td>0.11 <b>(+51.16%)</b></td><td>0.12 <b>(+80.40%)</b></td><td>0.06 (+14.37%)</td><td>0.03 <b>(+59.93%)</b></td><td>551.40 (-12.56%)</td><td>334.42 <b>(-31.31%)</b></td><td>265.20 <b>(-44.58%)</b></td><td>222.00 <b>(-28.57%)</b></td><td>133.21 (+0.65%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>630.60 (n/a)</td><td>486.82 (n/a)</td><td>478.50 (n/a)</td><td>310.80 (n/a)</td><td>132.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (-10.74%)</td><td>0.09 (-5.41%)</td><td>0.08 (-13.22%)</td><td>0.07 (+4.26%)</td><td>0.02 (-17.01%)</td><td>471.80 (-4.09%)</td><td>384.64 (+3.93%)</td><td>427.50 (+15.23%)</td><td>261.50 (+12.04%)</td><td>94.30 (-10.20%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>491.90 (n/a)</td><td>370.08 (n/a)</td><td>371.00 (n/a)</td><td>233.40 (n/a)</td><td>105.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(-25.81%)</b></td><td>0.07 (-4.88%)</td><td>0.07 (+11.83%)</td><td>0.04 <b>(-24.33%)</b></td><td>0.01 <b>(-29.02%)</b></td><td>740.90 <b>(+32.14%)</b></td><td>507.04 (+4.82%)</td><td>462.40 (-10.56%)</td><td>418.20 <b>(+34.77%)</b></td><td>134.39 <b>(+32.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>560.70 (n/a)</td><td>483.72 (n/a)</td><td>517.00 (n/a)</td><td>310.30 (n/a)</td><td>101.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (-7.72%)</td><td>0.07 <b>(-23.36%)</b></td><td>0.06 <b>(-42.77%)</b></td><td>0.05 (-2.66%)</td><td>0.02 (-1.69%)</td><td>624.70 (+2.73%)</td><td>490.98 <b>(+31.15%)</b></td><td>547.30 <b>(+74.74%)</b></td><td>311.30 (+8.35%)</td><td>145.21 (+8.32%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>608.10 (n/a)</td><td>374.36 (n/a)</td><td>313.20 (n/a)</td><td>287.30 (n/a)</td><td>134.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (-16.65%)</td><td>0.08 (+10.07%)</td><td>0.08 <b>(+26.49%)</b></td><td>0.06 <b>(+27.33%)</b></td><td>0.02 <b>(-44.96%)</b></td><td>529.80 <b>(-21.46%)</b></td><td>441.36 (-15.35%)</td><td>423.90 <b>(-20.94%)</b></td><td>322.50 (+19.98%)</td><td>88.41 <b>(-43.40%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>674.60 (n/a)</td><td>521.40 (n/a)</td><td>536.20 (n/a)</td><td>268.80 (n/a)</td><td>156.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 <b>(+56.84%)</b></td><td>0.08 (+13.02%)</td><td>0.07 (-8.94%)</td><td>0.05 (+11.31%)</td><td>0.04 <b>(+129.79%)</b></td><td>607.20 (-10.16%)</td><td>446.00 (-3.90%)</td><td>456.60 (+9.81%)</td><td>239.10 <b>(-36.24%)</b></td><td>162.46 <b>(+32.76%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>675.90 (n/a)</td><td>464.10 (n/a)</td><td>415.80 (n/a)</td><td>375.00 (n/a)</td><td>122.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (-1.74%)</td><td>0.08 (+11.41%)</td><td>0.07 (+8.75%)</td><td>0.06 <b>(+108.94%)</b></td><td>0.03 <b>(-24.71%)</b></td><td>543.00 <b>(-52.14%)</b></td><td>428.10 <b>(-24.44%)</b></td><td>437.40 (-8.05%)</td><td>245.40 (+1.78%)</td><td>122.89 <b>(-64.18%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1134.60 (n/a)</td><td>566.60 (n/a)</td><td>475.70 (n/a)</td><td>241.10 (n/a)</td><td>343.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 <b>(+78.63%)</b></td><td>0.08 <b>(+98.51%)</b></td><td>0.08 <b>(+41.58%)</b></td><td>0.05 <b>(+212.44%)</b></td><td>0.03 <b>(+22.13%)</b></td><td>616.50 <b>(-68.00%)</b></td><td>424.26 <b>(-61.21%)</b></td><td>434.20 <b>(-29.36%)</b></td><td>259.70 <b>(-44.02%)</b></td><td>142.29 <b>(-80.73%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1926.30 (n/a)</td><td>1093.66 (n/a)</td><td>614.70 (n/a)</td><td>463.90 (n/a)</td><td>738.40 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+3.65%)</td><td>0.01 (-14.91%)</td><td>0.01 (-9.14%)</td><td>0.01 <b>(-32.89%)</b></td><td>0.00 <b>(+105.31%)</b></td><td>507.20 <b>(+49.00%)</b></td><td>362.78 <b>(+25.79%)</b></td><td>314.10 (+10.06%)</td><td>229.10 (-3.54%)</td><td>114.43 <b>(+205.79%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>340.40 (n/a)</td><td>288.40 (n/a)</td><td>285.40 (n/a)</td><td>237.50 (n/a)</td><td>37.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (-1.75%)</td><td>0.01 (-8.92%)</td><td>0.01 (+3.32%)</td><td>0.01 (-0.41%)</td><td>0.01 (-17.74%)</td><td>604.20 (+0.42%)</td><td>454.32 (+6.64%)</td><td>469.80 (-3.21%)</td><td>270.40 (+1.77%)</td><td>135.54 (-9.71%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.70 (n/a)</td><td>426.02 (n/a)</td><td>485.40 (n/a)</td><td>265.70 (n/a)</td><td>150.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+0.29%)</td><td>0.01 (-18.35%)</td><td>0.01 <b>(-33.95%)</b></td><td>0.01 <b>(-24.73%)</b></td><td>0.00 <b>(+32.24%)</b></td><td>596.70 <b>(+32.87%)</b></td><td>400.78 <b>(+30.08%)</b></td><td>438.10 <b>(+51.43%)</b></td><td>227.60 (-0.31%)</td><td>144.30 <b>(+67.34%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.10 (n/a)</td><td>308.10 (n/a)</td><td>289.30 (n/a)</td><td>228.30 (n/a)</td><td>86.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 <b>(-35.46%)</b></td><td>0.01 <b>(-24.70%)</b></td><td>0.01 (-12.59%)</td><td>0.01 (-17.00%)</td><td>0.00 <b>(-59.05%)</b></td><td>613.40 <b>(+20.49%)</b></td><td>507.28 <b>(+26.95%)</b></td><td>478.50 (+14.39%)</td><td>423.50 <b>(+54.96%)</b></td><td>84.07 <b>(-23.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.10 (n/a)</td><td>399.58 (n/a)</td><td>418.30 (n/a)</td><td>273.30 (n/a)</td><td>110.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (+0.94%)</td><td>0.01 <b>(-38.89%)</b></td><td>0.01 <b>(-41.67%)</b></td><td>0.00 <b>(-84.58%)</b></td><td>0.01 <b>(+190.73%)</b></td><td>1911.90 <b>(+548.54%)</b></td><td>710.36 <b>(+172.59%)</b></td><td>461.90 <b>(+71.46%)</b></td><td>218.00 (-0.91%)</td><td>689.01 <b>(+1912.97%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>294.80 (n/a)</td><td>260.60 (n/a)</td><td>269.40 (n/a)</td><td>220.00 (n/a)</td><td>34.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-27.06%)</b></td><td>0.01 (-16.12%)</td><td>0.01 (+2.67%)</td><td>0.00 <b>(-55.03%)</b></td><td>0.01 <b>(-23.00%)</b></td><td>1357.20 <b>(+122.35%)</b></td><td>611.06 <b>(+34.89%)</b></td><td>460.20 (-2.60%)</td><td>279.90 <b>(+37.07%)</b></td><td>428.45 <b>(+172.89%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.40 (n/a)</td><td>453.02 (n/a)</td><td>472.50 (n/a)</td><td>204.20 (n/a)</td><td>157.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 <b>(-23.36%)</b></td><td>0.01 (-10.24%)</td><td>0.01 (-11.57%)</td><td>0.01 <b>(+183.42%)</b></td><td>0.00 <b>(-43.80%)</b></td><td>679.20 <b>(-64.72%)</b></td><td>509.58 <b>(-27.41%)</b></td><td>597.30 (+13.10%)</td><td>292.90 <b>(+30.53%)</b></td><td>175.69 <b>(-74.88%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1925.10 (n/a)</td><td>702.02 (n/a)</td><td>528.10 (n/a)</td><td>224.40 (n/a)</td><td>699.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(+27.98%)</b></td><td>0.01 (+12.25%)</td><td>0.01 (+10.44%)</td><td>0.01 (-9.45%)</td><td>0.01 <b>(+59.96%)</b></td><td>574.20 (+10.44%)</td><td>408.50 (-4.14%)</td><td>441.00 (-9.46%)</td><td>207.50 <b>(-21.88%)</b></td><td>154.97 <b>(+35.06%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.90 (n/a)</td><td>426.14 (n/a)</td><td>487.10 (n/a)</td><td>265.60 (n/a)</td><td>114.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 <b>(-27.61%)</b></td><td>0.01 (-11.49%)</td><td>0.01 (+17.24%)</td><td>0.01 (-3.47%)</td><td>0.00 <b>(-36.18%)</b></td><td>597.10 (+3.59%)</td><td>438.86 (+3.60%)</td><td>449.50 (-14.71%)</td><td>275.30 <b>(+38.13%)</b></td><td>159.22 (-13.89%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.40 (n/a)</td><td>423.62 (n/a)</td><td>527.00 (n/a)</td><td>199.30 (n/a)</td><td>184.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 <b>(-26.44%)</b></td><td>0.01 <b>(-29.09%)</b></td><td>0.01 <b>(-31.05%)</b></td><td>0.01 <b>(-20.29%)</b></td><td>0.00 <b>(-25.08%)</b></td><td>653.20 <b>(+25.45%)</b></td><td>537.60 <b>(+41.01%)</b></td><td>594.80 <b>(+45.04%)</b></td><td>279.60 <b>(+35.93%)</b></td><td>149.84 <b>(+29.74%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>520.70 (n/a)</td><td>381.26 (n/a)</td><td>410.10 (n/a)</td><td>205.70 (n/a)</td><td>115.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (-10.36%)</td><td>0.01 <b>(-27.54%)</b></td><td>0.01 <b>(-30.90%)</b></td><td>0.00 <b>(-71.41%)</b></td><td>0.00 <b>(+30.52%)</b></td><td>1933.30 <b>(+249.73%)</b></td><td>748.28 <b>(+90.18%)</b></td><td>539.00 <b>(+44.74%)</b></td><td>312.90 (+11.59%)</td><td>669.40 <b>(+483.95%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.80 (n/a)</td><td>393.46 (n/a)</td><td>372.40 (n/a)</td><td>280.40 (n/a)</td><td>114.63 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-15.77%)</td><td>0.02 (-17.56%)</td><td>0.02 <b>(-34.75%)</b></td><td>0.01 <b>(-23.95%)</b></td><td>0.01 (+5.92%)</td><td>618.10 <b>(+31.48%)</b></td><td>458.64 <b>(+28.98%)</b></td><td>535.60 <b>(+53.25%)</b></td><td>250.30 (+18.68%)</td><td>177.10 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.10 (n/a)</td><td>355.60 (n/a)</td><td>349.50 (n/a)</td><td>210.90 (n/a)</td><td>108.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 <b>(-23.52%)</b></td><td>0.03 <b>(-34.15%)</b></td><td>0.02 <b>(-52.16%)</b></td><td>0.02 (-13.52%)</td><td>0.01 (-11.54%)</td><td>677.70 (+15.63%)</td><td>470.76 <b>(+52.67%)</b></td><td>506.90 <b>(+109.03%)</b></td><td>273.90 <b>(+30.74%)</b></td><td>183.75 (+17.48%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>586.10 (n/a)</td><td>308.36 (n/a)</td><td>242.50 (n/a)</td><td>209.50 (n/a)</td><td>156.41 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+5.77%)</td><td>0.03 (+13.48%)</td><td>0.03 (+16.30%)</td><td>0.02 (+15.82%)</td><td>0.01 (-5.03%)</td><td>533.90 (-13.66%)</td><td>340.46 (-15.33%)</td><td>272.10 (-14.03%)</td><td>230.80 (-5.45%)</td><td>130.51 <b>(-25.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.40 (n/a)</td><td>402.08 (n/a)</td><td>316.50 (n/a)</td><td>244.10 (n/a)</td><td>174.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 <b>(-24.95%)</b></td><td>0.02 <b>(-27.63%)</b></td><td>0.02 <b>(-34.12%)</b></td><td>0.02 (-4.99%)</td><td>0.01 <b>(-26.65%)</b></td><td>559.80 (+5.27%)</td><td>484.74 <b>(+35.74%)</b></td><td>529.80 <b>(+51.81%)</b></td><td>271.80 <b>(+33.24%)</b></td><td>120.67 (+3.05%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.80 (n/a)</td><td>357.10 (n/a)</td><td>349.00 (n/a)</td><td>204.00 (n/a)</td><td>117.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+6.18%)</td><td>0.02 (-2.24%)</td><td>0.02 (+3.80%)</td><td>0.00 <b>(-68.17%)</b></td><td>0.01 <b>(+33.35%)</b></td><td>2442.70 <b>(+214.21%)</b></td><td>824.90 <b>(+60.28%)</b></td><td>475.50 (-3.67%)</td><td>241.30 (-5.82%)</td><td>910.49 <b>(+386.96%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>777.40 (n/a)</td><td>514.66 (n/a)</td><td>493.60 (n/a)</td><td>256.20 (n/a)</td><td>186.97 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (+9.02%)</td><td>0.03 (-12.41%)</td><td>0.03 <b>(-32.27%)</b></td><td>0.01 <b>(-41.81%)</b></td><td>0.01 <b>(+25.12%)</b></td><td>1104.10 <b>(+71.87%)</b></td><td>538.26 <b>(+34.49%)</b></td><td>405.30 <b>(+47.65%)</b></td><td>243.80 (-8.28%)</td><td>357.70 <b>(+99.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>642.40 (n/a)</td><td>400.22 (n/a)</td><td>274.50 (n/a)</td><td>265.80 (n/a)</td><td>179.60 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (+7.85%)</td><td>0.02 (-2.81%)</td><td>0.02 (-6.54%)</td><td>0.02 (-10.08%)</td><td>0.01 (+14.55%)</td><td>522.30 (+11.20%)</td><td>389.58 (+5.03%)</td><td>442.80 (+6.98%)</td><td>238.90 (-7.30%)</td><td>116.45 (+18.74%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.70 (n/a)</td><td>370.94 (n/a)</td><td>413.90 (n/a)</td><td>257.70 (n/a)</td><td>98.07 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 <b>(+60.23%)</b></td><td>0.03 <b>(+33.28%)</b></td><td>0.02 (+10.91%)</td><td>0.01 (-17.08%)</td><td>0.02 <b>(+112.94%)</b></td><td>692.50 <b>(+20.60%)</b></td><td>436.96 (-10.95%)</td><td>488.30 (-9.84%)</td><td>162.80 <b>(-37.60%)</b></td><td>209.31 <b>(+59.89%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.20 (n/a)</td><td>490.68 (n/a)</td><td>541.60 (n/a)</td><td>260.90 (n/a)</td><td>130.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-19.64%)</td><td>0.02 (-2.17%)</td><td>0.03 <b>(+47.56%)</b></td><td>0.01 (-6.52%)</td><td>0.01 (-16.66%)</td><td>611.00 (+6.99%)</td><td>401.76 (+1.45%)</td><td>299.10 <b>(-32.24%)</b></td><td>288.90 <b>(+24.42%)</b></td><td>153.25 (+9.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.10 (n/a)</td><td>396.02 (n/a)</td><td>441.40 (n/a)</td><td>232.20 (n/a)</td><td>139.81 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (-5.52%)</td><td>0.02 (-6.31%)</td><td>0.02 (-19.40%)</td><td>0.02 <b>(+21.34%)</b></td><td>0.00 <b>(-30.83%)</b></td><td>530.10 (-17.58%)</td><td>458.28 (+3.74%)</td><td>478.10 <b>(+24.09%)</b></td><td>361.20 (+5.83%)</td><td>69.66 <b>(-41.74%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>643.20 (n/a)</td><td>441.74 (n/a)</td><td>385.30 (n/a)</td><td>341.30 (n/a)</td><td>119.57 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (-17.98%)</td><td>0.01 <b>(-31.23%)</b></td><td>0.01 <b>(-24.44%)</b></td><td>0.01 <b>(-49.63%)</b></td><td>0.01 (+9.63%)</td><td>1324.40 <b>(+98.53%)</b></td><td>731.80 <b>(+61.98%)</b></td><td>595.50 <b>(+32.36%)</b></td><td>371.00 <b>(+21.92%)</b></td><td>363.07 <b>(+169.21%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.10 (n/a)</td><td>451.78 (n/a)</td><td>449.90 (n/a)</td><td>304.30 (n/a)</td><td>134.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (+0.53%)</td><td>0.05 (+10.52%)</td><td>0.05 (+4.82%)</td><td>0.04 <b>(+38.27%)</b></td><td>0.01 <b>(-43.34%)</b></td><td>405.20 <b>(-27.67%)</b></td><td>337.22 (-16.09%)</td><td>331.80 (-4.60%)</td><td>268.70 (-0.52%)</td><td>56.96 <b>(-60.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>560.20 (n/a)</td><td>401.86 (n/a)</td><td>347.80 (n/a)</td><td>270.10 (n/a)</td><td>142.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (+17.47%)</td><td>0.08 (+7.68%)</td><td>0.09 (+10.89%)</td><td>0.04 (-4.34%)</td><td>0.02 <b>(+29.27%)</b></td><td>603.80 (+4.54%)</td><td>341.92 (-3.82%)</td><td>272.60 (-9.82%)</td><td>243.60 (-14.88%)</td><td>148.95 (+18.99%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.60 (n/a)</td><td>355.50 (n/a)</td><td>302.30 (n/a)</td><td>286.20 (n/a)</td><td>125.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (-10.74%)</td><td>0.04 (-17.36%)</td><td>0.04 <b>(-37.27%)</b></td><td>0.03 (-13.44%)</td><td>0.01 (-7.45%)</td><td>560.40 (+15.52%)</td><td>418.02 <b>(+21.51%)</b></td><td>453.20 <b>(+59.41%)</b></td><td>271.40 (+12.06%)</td><td>122.13 (+14.91%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>485.10 (n/a)</td><td>344.02 (n/a)</td><td>284.30 (n/a)</td><td>242.20 (n/a)</td><td>106.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+6.07%)</td><td>0.05 (+8.21%)</td><td>0.04 (-15.83%)</td><td>0.03 <b>(+60.39%)</b></td><td>0.02 (-0.24%)</td><td>628.70 <b>(-37.65%)</b></td><td>441.04 (-14.60%)</td><td>487.80 (+18.80%)</td><td>273.30 (-5.73%)</td><td>153.85 <b>(-46.82%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1008.30 (n/a)</td><td>516.42 (n/a)</td><td>410.60 (n/a)</td><td>289.90 (n/a)</td><td>289.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 <b>(-41.62%)</b></td><td>0.03 <b>(-31.36%)</b></td><td>0.03 (-17.07%)</td><td>0.02 <b>(-27.54%)</b></td><td>0.01 <b>(-43.40%)</b></td><td>787.60 <b>(+38.01%)</b></td><td>562.92 <b>(+42.92%)</b></td><td>509.10 <b>(+20.58%)</b></td><td>407.80 <b>(+71.27%)</b></td><td>170.22 <b>(+33.99%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.70 (n/a)</td><td>393.86 (n/a)</td><td>422.20 (n/a)</td><td>238.10 (n/a)</td><td>127.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (-9.58%)</td><td>0.05 (-9.43%)</td><td>0.05 (+14.13%)</td><td>0.03 (-14.50%)</td><td>0.02 <b>(-24.69%)</b></td><td>675.80 (+16.96%)</td><td>451.22 (+6.57%)</td><td>447.20 (-12.38%)</td><td>270.20 (+10.60%)</td><td>156.50 (-0.56%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.80 (n/a)</td><td>423.42 (n/a)</td><td>510.40 (n/a)</td><td>244.30 (n/a)</td><td>157.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+14.18%)</td><td>0.04 (-6.25%)</td><td>0.06 <b>(+24.19%)</b></td><td>0.01 <b>(-73.64%)</b></td><td>0.03 <b>(+181.66%)</b></td><td>1877.90 <b>(+279.30%)</b></td><td>732.34 <b>(+100.33%)</b></td><td>274.60 (-19.47%)</td><td>238.80 (-12.43%)</td><td>721.72 <b>(+740.05%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>495.10 (n/a)</td><td>365.56 (n/a)</td><td>341.00 (n/a)</td><td>272.70 (n/a)</td><td>85.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (-3.60%)</td><td>0.05 (-17.65%)</td><td>0.04 <b>(-40.27%)</b></td><td>0.03 (+2.02%)</td><td>0.02 (-2.23%)</td><td>575.90 (-1.97%)</td><td>427.28 <b>(+21.21%)</b></td><td>476.60 <b>(+67.40%)</b></td><td>214.60 (+3.72%)</td><td>157.22 (+0.23%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>587.50 (n/a)</td><td>352.52 (n/a)</td><td>284.70 (n/a)</td><td>206.90 (n/a)</td><td>156.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (+7.42%)</td><td>0.04 (-13.08%)</td><td>0.04 (-12.26%)</td><td>0.01 <b>(-45.32%)</b></td><td>0.02 (+16.24%)</td><td>1934.50 <b>(+82.86%)</b></td><td>702.80 <b>(+45.41%)</b></td><td>430.90 (+13.96%)</td><td>232.20 (-6.90%)</td><td>695.45 <b>(+111.35%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1057.90 (n/a)</td><td>483.32 (n/a)</td><td>378.10 (n/a)</td><td>249.40 (n/a)</td><td>329.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (-7.49%)</td><td>0.05 (+4.78%)</td><td>0.04 (+15.72%)</td><td>0.03 (+3.05%)</td><td>0.02 (-10.26%)</td><td>547.70 (-2.96%)</td><td>393.52 (-6.59%)</td><td>435.40 (-13.58%)</td><td>216.40 (+8.09%)</td><td>144.56 (-6.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>564.40 (n/a)</td><td>421.30 (n/a)</td><td>503.80 (n/a)</td><td>200.20 (n/a)</td><td>154.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (+6.74%)</td><td>0.04 (+0.73%)</td><td>0.04 (-8.03%)</td><td>0.03 (+2.00%)</td><td>0.01 <b>(+41.16%)</b></td><td>473.30 (-1.97%)</td><td>414.20 (+0.59%)</td><td>457.60 (+8.75%)</td><td>311.20 (-6.32%)</td><td>73.08 <b>(+34.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>482.80 (n/a)</td><td>411.78 (n/a)</td><td>420.80 (n/a)</td><td>332.20 (n/a)</td><td>54.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (+3.72%)</td><td>0.06 <b>(-21.45%)</b></td><td>0.06 (-7.88%)</td><td>0.02 <b>(-68.11%)</b></td><td>0.04 (+19.82%)</td><td>1949.40 <b>(+213.51%)</b></td><td>762.76 <b>(+71.68%)</b></td><td>515.80 (+8.54%)</td><td>271.90 (-3.58%)</td><td>673.43 <b>(+332.88%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>621.80 (n/a)</td><td>444.28 (n/a)</td><td>475.20 (n/a)</td><td>282.00 (n/a)</td><td>155.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (+3.68%)</td><td>0.08 (-16.08%)</td><td>0.07 <b>(-20.88%)</b></td><td>0.04 <b>(-41.93%)</b></td><td>0.04 <b>(+41.13%)</b></td><td>791.50 <b>(+72.21%)</b></td><td>463.14 <b>(+33.56%)</b></td><td>469.30 <b>(+26.39%)</b></td><td>239.60 (-3.54%)</td><td>215.02 <b>(+139.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>459.60 (n/a)</td><td>346.76 (n/a)</td><td>371.30 (n/a)</td><td>248.40 (n/a)</td><td>89.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 <b>(-21.00%)</b></td><td>0.09 (-13.40%)</td><td>0.08 (-8.10%)</td><td>0.08 (+9.95%)</td><td>0.01 <b>(-59.43%)</b></td><td>505.80 (-9.05%)</td><td>461.54 (+9.17%)</td><td>488.20 (+8.83%)</td><td>367.20 <b>(+26.58%)</b></td><td>57.14 <b>(-52.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>556.10 (n/a)</td><td>422.76 (n/a)</td><td>448.60 (n/a)</td><td>290.10 (n/a)</td><td>119.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (+0.47%)</td><td>0.08 (-14.17%)</td><td>0.07 <b>(-39.50%)</b></td><td>0.06 (+4.76%)</td><td>0.04 (-6.80%)</td><td>554.50 (-4.54%)</td><td>434.68 (+12.45%)</td><td>478.70 <b>(+65.30%)</b></td><td>223.20 (-0.45%)</td><td>134.92 (-19.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>580.90 (n/a)</td><td>386.56 (n/a)</td><td>289.60 (n/a)</td><td>224.20 (n/a)</td><td>167.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 <b>(-41.25%)</b></td><td>0.06 <b>(-32.38%)</b></td><td>0.08 (+2.05%)</td><td>0.02 (+6.34%)</td><td>0.03 <b>(-44.79%)</b></td><td>1942.40 (-5.96%)</td><td>895.34 (+19.26%)</td><td>521.10 (-2.01%)</td><td>458.20 <b>(+70.21%)</b></td><td>638.15 (-14.89%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2065.50 (n/a)</td><td>750.74 (n/a)</td><td>531.80 (n/a)</td><td>269.20 (n/a)</td><td>749.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 <b>(+79.95%)</b></td><td>0.10 <b>(+72.40%)</b></td><td>0.11 <b>(+81.82%)</b></td><td>0.07 <b>(+132.31%)</b></td><td>0.03 <b>(+65.63%)</b></td><td>487.10 <b>(-56.95%)</b></td><td>354.90 <b>(-43.98%)</b></td><td>285.90 <b>(-45.01%)</b></td><td>241.00 <b>(-44.44%)</b></td><td>119.54 <b>(-58.62%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1131.50 (n/a)</td><td>633.56 (n/a)</td><td>519.90 (n/a)</td><td>433.80 (n/a)</td><td>288.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (+3.81%)</td><td>0.09 (-0.52%)</td><td>0.08 (+8.66%)</td><td>0.07 (+9.36%)</td><td>0.03 (-10.69%)</td><td>552.70 (-8.55%)</td><td>457.38 (-2.05%)</td><td>489.10 (-7.96%)</td><td>282.40 (-3.68%)</td><td>113.29 <b>(-21.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>604.40 (n/a)</td><td>466.94 (n/a)</td><td>531.40 (n/a)</td><td>293.20 (n/a)</td><td>143.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 <b>(+41.31%)</b></td><td>0.09 (+9.06%)</td><td>0.07 (-5.72%)</td><td>0.05 (-14.77%)</td><td>0.04 <b>(+103.14%)</b></td><td>635.70 (+17.31%)</td><td>417.28 (-0.18%)</td><td>442.10 (+6.07%)</td><td>214.30 <b>(-29.23%)</b></td><td>153.96 <b>(+62.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>541.90 (n/a)</td><td>418.04 (n/a)</td><td>416.80 (n/a)</td><td>302.80 (n/a)</td><td>94.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 <b>(-36.79%)</b></td><td>0.08 <b>(-28.81%)</b></td><td>0.07 <b>(-43.34%)</b></td><td>0.07 (+5.97%)</td><td>0.02 <b>(-61.66%)</b></td><td>554.20 (-5.62%)</td><td>479.64 <b>(+26.20%)</b></td><td>519.70 <b>(+76.47%)</b></td><td>342.30 <b>(+58.18%)</b></td><td>85.86 <b>(-46.10%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>587.20 (n/a)</td><td>380.06 (n/a)</td><td>294.50 (n/a)</td><td>216.40 (n/a)</td><td>159.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(-24.13%)</b></td><td>0.07 (-14.95%)</td><td>0.07 (-10.29%)</td><td>0.05 (+2.20%)</td><td>0.01 <b>(-52.08%)</b></td><td>597.60 (-2.16%)</td><td>497.62 (+10.28%)</td><td>482.30 (+11.46%)</td><td>387.00 <b>(+31.81%)</b></td><td>93.34 <b>(-37.96%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>610.80 (n/a)</td><td>451.24 (n/a)</td><td>432.70 (n/a)</td><td>293.60 (n/a)</td><td>150.44 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 <b>(-23.54%)</b></td><td>0.05 <b>(-21.40%)</b></td><td>0.04 <b>(-40.42%)</b></td><td>0.04 <b>(-22.28%)</b></td><td>0.02 (-4.80%)</td><td>575.80 <b>(+28.67%)</b></td><td>428.32 <b>(+31.18%)</b></td><td>500.00 <b>(+67.84%)</b></td><td>275.20 <b>(+30.80%)</b></td><td>138.13 <b>(+52.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>447.50 (n/a)</td><td>326.52 (n/a)</td><td>297.90 (n/a)</td><td>210.40 (n/a)</td><td>90.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 <b>(+33.45%)</b></td><td>0.07 <b>(+24.18%)</b></td><td>0.07 <b>(+42.54%)</b></td><td>0.04 (+12.34%)</td><td>0.02 <b>(+46.70%)</b></td><td>465.60 (-10.99%)</td><td>337.22 (-16.71%)</td><td>297.90 <b>(-29.86%)</b></td><td>212.90 <b>(-25.09%)</b></td><td>118.15 (+6.42%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>523.10 (n/a)</td><td>404.86 (n/a)</td><td>424.70 (n/a)</td><td>284.20 (n/a)</td><td>111.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (+5.63%)</td><td>0.07 (-3.68%)</td><td>0.07 (-7.62%)</td><td>0.04 <b>(-26.24%)</b></td><td>0.02 <b>(+31.09%)</b></td><td>580.30 <b>(+35.58%)</b></td><td>356.62 (+10.49%)</td><td>297.90 (+8.25%)</td><td>223.20 (-5.30%)</td><td>148.57 <b>(+61.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>428.00 (n/a)</td><td>322.76 (n/a)</td><td>275.20 (n/a)</td><td>235.70 (n/a)</td><td>92.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 <b>(+21.96%)</b></td><td>0.05 (+11.56%)</td><td>0.05 (+13.81%)</td><td>0.02 (-2.87%)</td><td>0.02 <b>(+29.15%)</b></td><td>1086.30 (+2.96%)</td><td>521.74 (-5.04%)</td><td>430.80 (-12.14%)</td><td>236.60 (-17.99%)</td><td>326.39 (+10.37%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1055.10 (n/a)</td><td>549.44 (n/a)</td><td>490.30 (n/a)</td><td>288.50 (n/a)</td><td>295.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(+27.75%)</b></td><td>0.06 <b>(+34.62%)</b></td><td>0.06 <b>(+40.32%)</b></td><td>0.04 (-5.23%)</td><td>0.02 <b>(+64.59%)</b></td><td>582.20 (+5.51%)</td><td>348.56 <b>(-21.88%)</b></td><td>317.30 <b>(-28.73%)</b></td><td>245.50 <b>(-21.74%)</b></td><td>134.24 <b>(+46.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>551.80 (n/a)</td><td>446.18 (n/a)</td><td>445.20 (n/a)</td><td>313.70 (n/a)</td><td>91.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(+49.43%)</b></td><td>0.06 <b>(+78.22%)</b></td><td>0.06 <b>(+88.91%)</b></td><td>0.04 <b>(+234.68%)</b></td><td>0.02 (+10.99%)</td><td>584.10 <b>(-70.12%)</b></td><td>373.74 <b>(-55.68%)</b></td><td>327.70 <b>(-47.07%)</b></td><td>245.80 <b>(-33.08%)</b></td><td>137.32 <b>(-78.71%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1954.70 (n/a)</td><td>843.36 (n/a)</td><td>619.10 (n/a)</td><td>367.30 (n/a)</td><td>644.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 <b>(-24.09%)</b></td><td>0.05 <b>(-30.08%)</b></td><td>0.05 <b>(-45.09%)</b></td><td>0.04 (+0.49%)</td><td>0.01 <b>(-50.10%)</b></td><td>559.80 (-0.48%)</td><td>482.30 <b>(+33.21%)</b></td><td>503.70 <b>(+82.10%)</b></td><td>329.30 <b>(+31.72%)</b></td><td>88.84 <b>(-36.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>562.50 (n/a)</td><td>362.06 (n/a)</td><td>276.60 (n/a)</td><td>250.00 (n/a)</td><td>139.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(-34.47%)</b></td><td>0.06 <b>(-27.27%)</b></td><td>0.06 <b>(-40.99%)</b></td><td>0.05 (+3.57%)</td><td>0.01 <b>(-47.74%)</b></td><td>496.50 (-3.44%)</td><td>410.98 <b>(+29.39%)</b></td><td>441.20 <b>(+69.50%)</b></td><td>305.90 <b>(+52.64%)</b></td><td>91.82 <b>(-25.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>514.20 (n/a)</td><td>317.62 (n/a)</td><td>260.30 (n/a)</td><td>200.40 (n/a)</td><td>123.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (+4.34%)</td><td>0.09 <b>(+79.08%)</b></td><td>0.09 <b>(+133.59%)</b></td><td>0.07 <b>(+626.48%)</b></td><td>0.01 <b>(-70.84%)</b></td><td>345.00 <b>(-86.23%)</b></td><td>273.64 <b>(-75.39%)</b></td><td>261.30 <b>(-57.19%)</b></td><td>237.80 (-4.15%)</td><td>42.52 <b>(-95.91%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2506.10 (n/a)</td><td>1111.74 (n/a)</td><td>610.40 (n/a)</td><td>248.10 (n/a)</td><td>1040.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (-15.80%)</td><td>0.08 (+12.69%)</td><td>0.09 <b>(+67.02%)</b></td><td>0.04 (-13.76%)</td><td>0.02 <b>(-25.41%)</b></td><td>599.20 (+15.97%)</td><td>340.92 (-13.38%)</td><td>276.40 <b>(-40.12%)</b></td><td>255.80 (+18.76%)</td><td>145.11 (+5.51%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>516.70 (n/a)</td><td>393.60 (n/a)</td><td>461.60 (n/a)</td><td>215.40 (n/a)</td><td>137.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (-11.09%)</td><td>0.06 (-6.59%)</td><td>0.07 <b>(+23.68%)</b></td><td>0.04 (+3.99%)</td><td>0.02 <b>(-20.58%)</b></td><td>579.90 (-3.83%)</td><td>421.74 (+3.71%)</td><td>370.70 (-19.13%)</td><td>249.20 (+12.45%)</td><td>145.85 (-5.65%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>603.00 (n/a)</td><td>406.64 (n/a)</td><td>458.40 (n/a)</td><td>221.60 (n/a)</td><td>154.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (-11.67%)</td><td>0.06 (-9.83%)</td><td>0.05 (+11.09%)</td><td>0.05 (+5.74%)</td><td>0.01 <b>(-36.44%)</b></td><td>543.40 (-5.43%)</td><td>464.86 (+4.34%)</td><td>483.30 (-9.98%)</td><td>302.00 (+13.19%)</td><td>96.29 <b>(-34.86%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.60 (n/a)</td><td>445.54 (n/a)</td><td>536.90 (n/a)</td><td>266.80 (n/a)</td><td>147.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (-13.35%)</td><td>0.05 <b>(-21.60%)</b></td><td>0.05 <b>(-29.61%)</b></td><td>0.04 (-16.39%)</td><td>0.01 (-3.37%)</td><td>468.30 (+19.62%)</td><td>365.78 <b>(+28.51%)</b></td><td>391.60 <b>(+42.04%)</b></td><td>274.40 (+15.39%)</td><td>80.00 <b>(+28.03%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>391.50 (n/a)</td><td>284.64 (n/a)</td><td>275.70 (n/a)</td><td>237.80 (n/a)</td><td>62.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (-1.56%)</td><td>0.05 (+3.87%)</td><td>0.06 <b>(+29.32%)</b></td><td>0.03 <b>(-20.95%)</b></td><td>0.02 (-1.04%)</td><td>642.00 <b>(+26.50%)</b></td><td>374.94 (-1.42%)</td><td>301.20 <b>(-22.67%)</b></td><td>260.70 (+1.60%)</td><td>155.27 <b>(+35.01%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>507.50 (n/a)</td><td>380.36 (n/a)</td><td>389.50 (n/a)</td><td>256.60 (n/a)</td><td>115.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (-1.39%)</td><td>0.04 <b>(-44.43%)</b></td><td>0.04 <b>(-51.78%)</b></td><td>0.01 <b>(-79.81%)</b></td><td>0.03 <b>(+93.46%)</b></td><td>1868.70 <b>(+395.41%)</b></td><td>753.40 <b>(+172.32%)</b></td><td>508.30 <b>(+107.38%)</b></td><td>227.70 (+1.43%)</td><td>642.99 <b>(+925.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>377.20 (n/a)</td><td>276.66 (n/a)</td><td>245.10 (n/a)</td><td>224.50 (n/a)</td><td>62.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (+2.57%)</td><td>0.05 <b>(-23.74%)</b></td><td>0.03 <b>(-51.51%)</b></td><td>0.03 (-7.97%)</td><td>0.02 (+18.02%)</td><td>652.30 (+8.66%)</td><td>464.66 <b>(+37.43%)</b></td><td>550.20 <b>(+106.22%)</b></td><td>241.60 (-2.50%)</td><td>184.47 <b>(+22.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>600.30 (n/a)</td><td>338.10 (n/a)</td><td>266.80 (n/a)</td><td>247.80 (n/a)</td><td>150.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 <b>(+27.56%)</b></td><td>0.05 (+18.73%)</td><td>0.06 <b>(+54.86%)</b></td><td>0.01 <b>(-68.59%)</b></td><td>0.03 <b>(+127.18%)</b></td><td>1848.40 <b>(+218.36%)</b></td><td>654.18 <b>(+48.61%)</b></td><td>288.60 <b>(-35.42%)</b></td><td>206.10 <b>(-21.61%)</b></td><td>695.13 <b>(+495.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>580.60 (n/a)</td><td>440.20 (n/a)</td><td>446.90 (n/a)</td><td>262.90 (n/a)</td><td>116.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 <b>(+22.20%)</b></td><td>0.06 <b>(+37.34%)</b></td><td>0.06 <b>(+47.71%)</b></td><td>0.04 <b>(+110.38%)</b></td><td>0.02 (-6.61%)</td><td>494.70 <b>(-52.46%)</b></td><td>334.46 <b>(-37.65%)</b></td><td>318.60 <b>(-32.30%)</b></td><td>220.60 (-18.14%)</td><td>120.68 <b>(-62.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1040.70 (n/a)</td><td>536.42 (n/a)</td><td>470.60 (n/a)</td><td>269.50 (n/a)</td><td>320.19 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.34 <b>(-23.66%)</b></td><td>0.26 <b>(-26.65%)</b></td><td>0.25 <b>(-30.42%)</b></td><td>0.17 <b>(-24.82%)</b></td><td>0.07 <b>(-23.64%)</b></td><td>584.90 <b>(+33.02%)</b></td><td>400.94 <b>(+36.43%)</b></td><td>386.20 <b>(+43.73%)</b></td><td>291.80 <b>(+31.03%)</b></td><td>119.09 <b>(+32.56%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.44 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>439.70 (n/a)</td><td>293.88 (n/a)</td><td>268.70 (n/a)</td><td>222.70 (n/a)</td><td>89.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.46 <b>(+29.80%)</b></td><td>0.40 <b>(+87.11%)</b></td><td>0.39 <b>(+112.62%)</b></td><td>0.37 <b>(+169.44%)</b></td><td>0.03 <b>(-58.99%)</b></td><td>264.50 <b>(-62.89%)</b></td><td>244.34 <b>(-51.51%)</b></td><td>249.30 <b>(-52.96%)</b></td><td>212.50 <b>(-22.95%)</b></td><td>19.62 <b>(-87.99%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>712.80 (n/a)</td><td>503.88 (n/a)</td><td>530.00 (n/a)</td><td>275.80 (n/a)</td><td>163.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.37 <b>(-37.75%)</b></td><td>0.25 (-11.26%)</td><td>0.25 <b>(+51.15%)</b></td><td>0.16 (+4.79%)</td><td>0.08 <b>(-56.60%)</b></td><td>631.20 (-4.57%)</td><td>435.78 (-6.36%)</td><td>385.70 <b>(-33.84%)</b></td><td>264.50 <b>(+60.69%)</b></td><td>140.71 <b>(-33.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.60 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.19 (n/a)</td><td>661.40 (n/a)</td><td>465.38 (n/a)</td><td>583.00 (n/a)</td><td>164.60 (n/a)</td><td>213.13 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.29 <b>(-25.02%)</b></td><td>0.20 (-11.79%)</td><td>0.24 <b>(+23.34%)</b></td><td>0.11 (-6.10%)</td><td>0.08 <b>(-29.92%)</b></td><td>654.40 (+6.51%)</td><td>429.96 (+8.54%)</td><td>313.00 (-18.93%)</td><td>256.70 <b>(+33.42%)</b></td><td>190.27 (+4.87%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.38 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>614.40 (n/a)</td><td>396.12 (n/a)</td><td>386.10 (n/a)</td><td>192.40 (n/a)</td><td>181.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.34 (+5.31%)</td><td>0.18 (-14.36%)</td><td>0.16 (-6.47%)</td><td>0.09 <b>(-34.27%)</b></td><td>0.09 (+13.42%)</td><td>807.20 <b>(+52.13%)</b></td><td>479.64 <b>(+25.66%)</b></td><td>472.80 (+6.90%)</td><td>219.40 (-5.02%)</td><td>218.52 <b>(+65.93%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>530.60 (n/a)</td><td>381.70 (n/a)</td><td>442.30 (n/a)</td><td>231.00 (n/a)</td><td>131.69 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.30 <b>(+50.91%)</b></td><td>0.17 (+12.08%)</td><td>0.17 (+19.23%)</td><td>0.07 <b>(-35.61%)</b></td><td>0.08 <b>(+150.05%)</b></td><td>1040.00 <b>(+55.29%)</b></td><td>538.36 (+5.87%)</td><td>441.80 (-16.12%)</td><td>249.50 <b>(-33.73%)</b></td><td>298.46 <b>(+169.19%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>669.70 (n/a)</td><td>508.50 (n/a)</td><td>526.70 (n/a)</td><td>376.50 (n/a)</td><td>110.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (+11.38%)</td><td>0.09 (-0.28%)</td><td>0.07 <b>(-36.85%)</b></td><td>0.06 <b>(+188.94%)</b></td><td>0.04 (-13.58%)</td><td>640.80 <b>(-65.39%)</b></td><td>457.22 <b>(-30.28%)</b></td><td>531.50 <b>(+58.33%)</b></td><td>231.40 (-10.24%)</td><td>175.45 <b>(-74.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1851.60 (n/a)</td><td>655.84 (n/a)</td><td>335.70 (n/a)</td><td>257.80 (n/a)</td><td>678.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (+2.12%)</td><td>0.10 (-9.81%)</td><td>0.12 (-1.16%)</td><td>0.06 <b>(-22.65%)</b></td><td>0.04 <b>(+54.35%)</b></td><td>613.20 <b>(+29.29%)</b></td><td>407.46 <b>(+21.51%)</b></td><td>296.50 (+1.19%)</td><td>253.40 (-2.09%)</td><td>174.24 <b>(+101.82%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>474.30 (n/a)</td><td>335.34 (n/a)</td><td>293.00 (n/a)</td><td>258.80 (n/a)</td><td>86.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (-4.37%)</td><td>0.11 (-1.63%)</td><td>0.12 (-5.91%)</td><td>0.06 (-4.38%)</td><td>0.04 (-14.92%)</td><td>631.50 (+4.59%)</td><td>380.90 (-1.97%)</td><td>295.60 (+6.29%)</td><td>239.30 (+4.54%)</td><td>159.27 (-9.75%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>603.80 (n/a)</td><td>388.56 (n/a)</td><td>278.10 (n/a)</td><td>228.90 (n/a)</td><td>176.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 <b>(-22.39%)</b></td><td>0.08 (-10.28%)</td><td>0.08 (+0.28%)</td><td>0.02 <b>(-62.13%)</b></td><td>0.04 (+1.52%)</td><td>1913.50 <b>(+164.04%)</b></td><td>691.74 <b>(+51.44%)</b></td><td>459.70 (-0.28%)</td><td>301.70 <b>(+28.82%)</b></td><td>688.24 <b>(+265.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>724.70 (n/a)</td><td>456.76 (n/a)</td><td>461.00 (n/a)</td><td>234.20 (n/a)</td><td>188.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (-15.51%)</td><td>0.10 (-3.36%)</td><td>0.10 (+12.96%)</td><td>0.07 (-6.78%)</td><td>0.02 <b>(-28.87%)</b></td><td>554.20 (+7.28%)</td><td>394.30 (+0.36%)</td><td>377.40 (-11.49%)</td><td>291.20 (+18.33%)</td><td>106.31 (-10.87%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>516.60 (n/a)</td><td>392.88 (n/a)</td><td>426.40 (n/a)</td><td>246.10 (n/a)</td><td>119.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (-8.76%)</td><td>0.09 (-11.98%)</td><td>0.08 <b>(-24.29%)</b></td><td>0.06 (-6.77%)</td><td>0.03 <b>(-21.80%)</b></td><td>663.60 (+7.26%)</td><td>460.78 (+7.97%)</td><td>468.70 <b>(+32.10%)</b></td><td>264.40 (+9.62%)</td><td>141.84 (-19.31%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>618.70 (n/a)</td><td>426.78 (n/a)</td><td>354.80 (n/a)</td><td>241.20 (n/a)</td><td>175.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (-18.32%)</td><td>0.13 (-7.04%)</td><td>0.15 (+12.35%)</td><td>0.07 (-16.00%)</td><td>0.04 (+1.20%)</td><td>546.20 (+19.05%)</td><td>356.62 (+11.17%)</td><td>271.30 (-10.99%)</td><td>252.40 <b>(+22.46%)</b></td><td>133.97 <b>(+44.27%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>458.80 (n/a)</td><td>320.78 (n/a)</td><td>304.80 (n/a)</td><td>206.10 (n/a)</td><td>92.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (-17.27%)</td><td>0.12 <b>(-22.99%)</b></td><td>0.13 (-10.04%)</td><td>0.06 <b>(-30.96%)</b></td><td>0.05 <b>(+21.27%)</b></td><td>657.70 <b>(+44.84%)</b></td><td>423.70 <b>(+44.48%)</b></td><td>312.60 (+11.17%)</td><td>255.80 <b>(+20.89%)</b></td><td>205.25 <b>(+112.92%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>454.10 (n/a)</td><td>293.26 (n/a)</td><td>281.20 (n/a)</td><td>211.60 (n/a)</td><td>96.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (-18.54%)</td><td>0.10 (+5.79%)</td><td>0.09 (+14.86%)</td><td>0.04 <b>(-25.23%)</b></td><td>0.05 (-16.88%)</td><td>1089.20 <b>(+33.74%)</b></td><td>521.12 (-1.41%)</td><td>470.10 (-12.94%)</td><td>261.00 <b>(+22.77%)</b></td><td>332.64 <b>(+50.63%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>814.40 (n/a)</td><td>528.56 (n/a)</td><td>540.00 (n/a)</td><td>212.60 (n/a)</td><td>220.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (-0.73%)</td><td>0.11 (+1.33%)</td><td>0.12 (+19.22%)</td><td>0.08 (+5.00%)</td><td>0.03 (+3.02%)</td><td>540.40 (-4.76%)</td><td>397.04 (-0.84%)</td><td>330.30 (-16.12%)</td><td>299.10 (+0.74%)</td><td>116.06 (+3.49%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>567.40 (n/a)</td><td>400.40 (n/a)</td><td>393.80 (n/a)</td><td>296.90 (n/a)</td><td>112.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (-11.51%)</td><td>0.12 (-8.76%)</td><td>0.10 <b>(-31.30%)</b></td><td>0.09 <b>(+46.97%)</b></td><td>0.03 <b>(-37.67%)</b></td><td>441.70 <b>(-31.96%)</b></td><td>372.34 (-0.31%)</td><td>429.20 <b>(+45.54%)</b></td><td>267.00 (+13.04%)</td><td>85.05 <b>(-50.78%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>649.20 (n/a)</td><td>373.50 (n/a)</td><td>294.90 (n/a)</td><td>236.20 (n/a)</td><td>172.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 (-0.46%)</td><td>0.13 (+14.27%)</td><td>0.14 <b>(+46.75%)</b></td><td>0.08 (+17.03%)</td><td>0.04 (-10.65%)</td><td>529.90 (-14.55%)</td><td>358.64 (-16.34%)</td><td>287.10 <b>(-31.85%)</b></td><td>242.20 (+0.46%)</td><td>137.11 <b>(-23.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>620.10 (n/a)</td><td>428.70 (n/a)</td><td>421.30 (n/a)</td><td>241.10 (n/a)</td><td>179.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (-12.99%)</td><td>0.08 <b>(-28.99%)</b></td><td>0.07 <b>(-47.76%)</b></td><td>0.05 <b>(-23.63%)</b></td><td>0.04 (+15.25%)</td><td>706.70 <b>(+30.94%)</b></td><td>484.88 <b>(+51.06%)</b></td><td>500.30 <b>(+91.39%)</b></td><td>275.50 (+14.94%)</td><td>202.22 <b>(+61.44%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>539.70 (n/a)</td><td>320.98 (n/a)</td><td>261.40 (n/a)</td><td>239.70 (n/a)</td><td>125.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (-17.86%)</td><td>0.09 (-12.94%)</td><td>0.09 <b>(-26.80%)</b></td><td>0.06 (-0.07%)</td><td>0.02 <b>(-35.24%)</b></td><td>576.20 (+0.09%)</td><td>416.76 (+7.45%)</td><td>400.20 <b>(+36.63%)</b></td><td>304.90 <b>(+21.77%)</b></td><td>118.41 <b>(-26.75%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>575.70 (n/a)</td><td>387.88 (n/a)</td><td>292.90 (n/a)</td><td>250.40 (n/a)</td><td>161.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (-13.85%)</td><td>0.11 (-6.82%)</td><td>0.12 (-4.45%)</td><td>0.02 <b>(-73.96%)</b></td><td>0.05 <b>(+26.90%)</b></td><td>1899.50 <b>(+283.97%)</b></td><td>598.90 <b>(+77.21%)</b></td><td>291.50 (+4.67%)</td><td>237.80 (+16.11%)</td><td>727.66 <b>(+494.01%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>494.70 (n/a)</td><td>337.96 (n/a)</td><td>278.50 (n/a)</td><td>204.80 (n/a)</td><td>122.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (-18.89%)</td><td>0.11 (-2.10%)</td><td>0.11 <b>(+33.31%)</b></td><td>0.08 <b>(+24.58%)</b></td><td>0.03 <b>(-42.48%)</b></td><td>445.40 (-19.73%)</td><td>345.84 (-6.51%)</td><td>308.30 <b>(-24.99%)</b></td><td>253.60 <b>(+23.29%)</b></td><td>91.86 <b>(-37.42%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>554.90 (n/a)</td><td>369.94 (n/a)</td><td>411.00 (n/a)</td><td>205.70 (n/a)</td><td>146.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 <b>(+32.27%)</b></td><td>0.08 <b>(+23.45%)</b></td><td>0.07 <b>(+21.24%)</b></td><td>0.05 <b>(+164.23%)</b></td><td>0.03 (+0.88%)</td><td>648.60 <b>(-62.16%)</b></td><td>479.08 <b>(-34.44%)</b></td><td>480.40 (-17.53%)</td><td>260.70 <b>(-24.39%)</b></td><td>157.36 <b>(-72.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1713.90 (n/a)</td><td>730.70 (n/a)</td><td>582.50 (n/a)</td><td>344.80 (n/a)</td><td>563.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (+5.84%)</td><td>0.07 (-12.59%)</td><td>0.06 <b>(-25.01%)</b></td><td>0.05 (-11.32%)</td><td>0.03 <b>(+30.07%)</b></td><td>683.30 (+12.76%)</td><td>527.54 <b>(+20.54%)</b></td><td>611.00 <b>(+33.35%)</b></td><td>268.70 (-5.52%)</td><td>172.66 <b>(+40.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>606.00 (n/a)</td><td>437.64 (n/a)</td><td>458.20 (n/a)</td><td>284.40 (n/a)</td><td>123.14 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.45 (-11.63%)</td><td>0.28 (-15.54%)</td><td>0.21 <b>(-25.56%)</b></td><td>0.12 <b>(-41.91%)</b></td><td>0.14 (+15.24%)</td><td>1065.70 <b>(+72.14%)</b></td><td>594.80 <b>(+33.96%)</b></td><td>616.00 <b>(+34.35%)</b></td><td>290.30 (+13.13%)</td><td>313.72 <b>(+110.00%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>619.10 (n/a)</td><td>444.00 (n/a)</td><td>458.50 (n/a)</td><td>256.60 (n/a)</td><td>149.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.47 (+8.64%)</td><td>0.32 <b>(+39.54%)</b></td><td>0.27 <b>(+30.40%)</b></td><td>0.19 <b>(+148.29%)</b></td><td>0.12 (-10.22%)</td><td>673.30 <b>(-59.72%)</b></td><td>450.72 <b>(-41.26%)</b></td><td>482.60 <b>(-23.31%)</b></td><td>277.70 (-7.95%)</td><td>160.48 <b>(-69.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.43 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>0.13 (n/a)</td><td>1671.70 (n/a)</td><td>767.32 (n/a)</td><td>629.30 (n/a)</td><td>301.70 (n/a)</td><td>529.25 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.46 (+10.17%)</td><td>0.35 (+10.70%)</td><td>0.40 <b>(+48.57%)</b></td><td>0.21 (-11.97%)</td><td>0.10 (+14.14%)</td><td>628.70 (+13.59%)</td><td>406.38 (-7.59%)</td><td>327.40 <b>(-32.69%)</b></td><td>282.60 (-9.25%)</td><td>142.96 <b>(+22.49%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>553.50 (n/a)</td><td>439.78 (n/a)</td><td>486.40 (n/a)</td><td>311.40 (n/a)</td><td>116.71 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.00 (-14.29%)</td><td>0.00 (-10.53%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-21.71%)</b></td><td>20613.39 (-3.95%)</td><td>14717.90 (+6.65%)</td><td>18007.75 (+9.80%)</td><td>7365.93 (+18.77%)</td><td>6389.84 (-6.09%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21462.15 (n/a)</td><td>13799.88 (n/a)</td><td>16400.32 (n/a)</td><td>6201.76 (n/a)</td><td>6804.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.00 (-7.14%)</td><td>0.00 (+5.56%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+7.06%)</td><td>21137.62 (-4.71%)</td><td>14257.78 (-5.09%)</td><td>18336.91 (-3.76%)</td><td>6171.25 (+3.78%)</td><td>7349.06 (+1.07%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22182.98 (n/a)</td><td>15023.07 (n/a)</td><td>19052.88 (n/a)</td><td>5946.29 (n/a)</td><td>7271.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 <b>(+51.98%)</b></td><td>0.09 (+11.80%)</td><td>0.08 (+5.46%)</td><td>0.07 (-1.67%)</td><td>0.03 <b>(+207.38%)</b></td><td>29656.10 (+1.66%)</td><td>24416.13 (-6.35%)</td><td>25843.62 (-5.29%)</td><td>15197.67 <b>(-34.23%)</b></td><td>5571.50 <b>(+101.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>29170.75 (n/a)</td><td>26072.67 (n/a)</td><td>27287.51 (n/a)</td><td>23106.04 (n/a)</td><td>2767.51 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.62 (+3.29%)</td><td>1.62 (+7.06%)</td><td>2.37 <b>(+74.74%)</b></td><td>0.30 (-5.61%)</td><td>1.20 <b>(+30.07%)</b></td><td>3479.00 (+5.95%)</td><td>1624.68 <b>(+36.44%)</b></td><td>443.30 <b>(-42.77%)</b></td><td>400.80 (-3.19%)</td><td>1647.96 <b>(+37.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.53 (n/a)</td><td>1.51 (n/a)</td><td>1.35 (n/a)</td><td>0.32 (n/a)</td><td>0.92 (n/a)</td><td>3283.60 (n/a)</td><td>1190.80 (n/a)</td><td>774.60 (n/a)</td><td>414.00 (n/a)</td><td>1196.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>2.72 (-5.32%)</td><td>1.79 (-2.96%)</td><td>1.83 (+9.94%)</td><td>1.17 (+0.84%)</td><td>0.64 (+0.92%)</td><td>893.10 (-0.83%)</td><td>648.00 (+4.66%)</td><td>572.10 (-9.05%)</td><td>385.80 (+5.61%)</td><td>222.03 (+15.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.87 (n/a)</td><td>1.84 (n/a)</td><td>1.67 (n/a)</td><td>1.16 (n/a)</td><td>0.63 (n/a)</td><td>900.60 (n/a)</td><td>619.16 (n/a)</td><td>629.00 (n/a)</td><td>365.30 (n/a)</td><td>192.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.43 <b>(+61.40%)</b></td><td>1.92 (+11.80%)</td><td>2.42 <b>(+42.97%)</b></td><td>0.31 <b>(-78.40%)</b></td><td>1.42 <b>(+415.81%)</b></td><td>3434.40 <b>(+362.92%)</b></td><td>1287.82 <b>(+107.34%)</b></td><td>433.50 <b>(-30.06%)</b></td><td>305.80 <b>(-38.05%)</b></td><td>1373.65 <b>(+1337.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.12 (n/a)</td><td>1.72 (n/a)</td><td>1.69 (n/a)</td><td>1.41 (n/a)</td><td>0.27 (n/a)</td><td>741.90 (n/a)</td><td>621.12 (n/a)</td><td>619.80 (n/a)</td><td>493.60 (n/a)</td><td>95.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.20 (-4.35%)</td><td>2.02 (+1.57%)</td><td>2.01 (+13.57%)</td><td>1.35 (+14.36%)</td><td>0.74 (-9.77%)</td><td>777.00 (-12.55%)</td><td>569.10 (-3.57%)</td><td>522.10 (-11.96%)</td><td>327.30 (+4.54%)</td><td>180.13 (-12.93%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.35 (n/a)</td><td>1.99 (n/a)</td><td>1.77 (n/a)</td><td>1.18 (n/a)</td><td>0.81 (n/a)</td><td>888.50 (n/a)</td><td>590.16 (n/a)</td><td>593.00 (n/a)</td><td>313.10 (n/a)</td><td>206.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.75 (+9.01%)</td><td>1.26 <b>(-29.89%)</b></td><td>1.29 <b>(-28.77%)</b></td><td>0.30 <b>(-69.74%)</b></td><td>1.02 <b>(+59.60%)</b></td><td>3538.60 <b>(+230.52%)</b></td><td>1712.76 <b>(+160.84%)</b></td><td>812.40 <b>(+40.41%)</b></td><td>380.60 (-8.29%)</td><td>1521.02 <b>(+466.94%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.53 (n/a)</td><td>1.80 (n/a)</td><td>1.81 (n/a)</td><td>0.98 (n/a)</td><td>0.64 (n/a)</td><td>1070.60 (n/a)</td><td>656.64 (n/a)</td><td>578.60 (n/a)</td><td>415.00 (n/a)</td><td>268.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.00 <b>(-20.24%)</b></td><td>2.12 (-0.61%)</td><td>1.78 (-1.19%)</td><td>1.26 (-19.13%)</td><td>0.76 (-17.59%)</td><td>835.20 <b>(+23.66%)</b></td><td>549.46 (+1.09%)</td><td>588.30 (+1.20%)</td><td>349.00 <b>(+25.36%)</b></td><td>198.89 <b>(+29.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.77 (n/a)</td><td>2.13 (n/a)</td><td>1.80 (n/a)</td><td>1.55 (n/a)</td><td>0.92 (n/a)</td><td>675.40 (n/a)</td><td>543.54 (n/a)</td><td>581.30 (n/a)</td><td>278.40 (n/a)</td><td>153.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.77 (+7.51%)</td><td>2.14 (+16.50%)</td><td>2.07 <b>(+43.09%)</b></td><td>1.01 (-11.62%)</td><td>1.06 (+10.75%)</td><td>1040.60 (+13.15%)</td><td>597.14 (-10.07%)</td><td>506.10 <b>(-30.12%)</b></td><td>277.90 (-6.99%)</td><td>295.74 <b>(+26.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.51 (n/a)</td><td>1.84 (n/a)</td><td>1.45 (n/a)</td><td>1.14 (n/a)</td><td>0.96 (n/a)</td><td>919.70 (n/a)</td><td>664.04 (n/a)</td><td>724.20 (n/a)</td><td>298.80 (n/a)</td><td>233.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.42 (+15.72%)</td><td>2.00 (-15.76%)</td><td>1.92 (-16.79%)</td><td>0.30 <b>(-83.18%)</b></td><td>1.19 <b>(+164.52%)</b></td><td>3483.00 <b>(+494.67%)</b></td><td>1075.72 <b>(+136.07%)</b></td><td>546.40 <b>(+20.19%)</b></td><td>307.00 (-13.57%)</td><td>1352.93 <b>(+1418.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.95 (n/a)</td><td>2.37 (n/a)</td><td>2.31 (n/a)</td><td>1.79 (n/a)</td><td>0.45 (n/a)</td><td>585.70 (n/a)</td><td>455.68 (n/a)</td><td>454.60 (n/a)</td><td>355.20 (n/a)</td><td>89.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.86 (-9.09%)</td><td>2.41 (-15.95%)</td><td>2.37 (-18.63%)</td><td>1.08 (-1.17%)</td><td>0.98 (-17.40%)</td><td>1943.40 (+1.18%)</td><td>1027.36 (+12.84%)</td><td>885.40 <b>(+22.90%)</b></td><td>544.00 (+9.99%)</td><td>532.90 (-7.98%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.24 (n/a)</td><td>2.87 (n/a)</td><td>2.91 (n/a)</td><td>1.09 (n/a)</td><td>1.19 (n/a)</td><td>1920.70 (n/a)</td><td>910.48 (n/a)</td><td>720.40 (n/a)</td><td>494.60 (n/a)</td><td>579.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.27 (+5.01%)</td><td>2.38 (-0.41%)</td><td>2.30 <b>(-23.02%)</b></td><td>0.85 <b>(+44.01%)</b></td><td>1.22 <b>(-27.53%)</b></td><td>2480.30 <b>(-30.56%)</b></td><td>1151.68 <b>(-35.14%)</b></td><td>912.40 <b>(+29.90%)</b></td><td>491.60 (-4.77%)</td><td>766.82 <b>(-52.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.06 (n/a)</td><td>2.39 (n/a)</td><td>2.99 (n/a)</td><td>0.59 (n/a)</td><td>1.69 (n/a)</td><td>3572.00 (n/a)</td><td>1775.74 (n/a)</td><td>702.40 (n/a)</td><td>516.20 (n/a)</td><td>1618.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.47 (+3.76%)</td><td>3.21 (+7.22%)</td><td>2.60 (-1.97%)</td><td>2.26 <b>(+136.82%)</b></td><td>1.31 (-18.57%)</td><td>929.80 <b>(-57.77%)</b></td><td>722.16 <b>(-25.42%)</b></td><td>805.30 (+2.01%)</td><td>383.20 (-3.62%)</td><td>213.69 <b>(-70.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.27 (n/a)</td><td>2.99 (n/a)</td><td>2.66 (n/a)</td><td>0.95 (n/a)</td><td>1.61 (n/a)</td><td>2202.00 (n/a)</td><td>968.36 (n/a)</td><td>789.40 (n/a)</td><td>397.60 (n/a)</td><td>715.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.35 <b>(+62.04%)</b></td><td>3.73 <b>(+74.69%)</b></td><td>3.84 <b>(+33.01%)</b></td><td>1.65 <b>(+179.02%)</b></td><td>1.65 (+16.55%)</td><td>1269.90 <b>(-64.16%)</b></td><td>687.54 <b>(-61.85%)</b></td><td>545.90 <b>(-24.82%)</b></td><td>392.20 <b>(-38.29%)</b></td><td>371.48 <b>(-76.12%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.30 (n/a)</td><td>2.13 (n/a)</td><td>2.89 (n/a)</td><td>0.59 (n/a)</td><td>1.41 (n/a)</td><td>3543.40 (n/a)</td><td>1802.06 (n/a)</td><td>726.10 (n/a)</td><td>635.60 (n/a)</td><td>1555.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.34 (+9.33%)</td><td>3.22 <b>(+24.58%)</b></td><td>3.28 <b>(+26.99%)</b></td><td>0.60 (+1.02%)</td><td>2.08 <b>(+35.16%)</b></td><td>3491.90 (-1.01%)</td><td>1229.28 (-5.73%)</td><td>639.30 <b>(-21.25%)</b></td><td>392.60 (-8.53%)</td><td>1307.79 (+3.91%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.89 (n/a)</td><td>2.58 (n/a)</td><td>2.58 (n/a)</td><td>0.59 (n/a)</td><td>1.54 (n/a)</td><td>3527.60 (n/a)</td><td>1304.04 (n/a)</td><td>811.80 (n/a)</td><td>429.20 (n/a)</td><td>1258.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.95 (-15.99%)</td><td>4.07 <b>(+21.39%)</b></td><td>4.13 <b>(+23.08%)</b></td><td>3.21 <b>(+439.17%)</b></td><td>0.83 <b>(-56.43%)</b></td><td>652.90 <b>(-81.45%)</b></td><td>533.80 <b>(-53.45%)</b></td><td>507.60 (-18.76%)</td><td>423.60 (+19.02%)</td><td>110.95 <b>(-91.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.89 (n/a)</td><td>3.35 (n/a)</td><td>3.36 (n/a)</td><td>0.60 (n/a)</td><td>1.90 (n/a)</td><td>3520.50 (n/a)</td><td>1146.74 (n/a)</td><td>624.80 (n/a)</td><td>355.90 (n/a)</td><td>1332.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>4.33 (+14.66%)</td><td>3.61 (+17.43%)</td><td>4.09 <b>(+23.15%)</b></td><td>2.56 <b>(+47.48%)</b></td><td>0.86 (+2.16%)</td><td>818.50 <b>(-32.19%)</b></td><td>611.10 (-17.45%)</td><td>513.00 (-18.80%)</td><td>484.70 (-12.79%)</td><td>160.76 <b>(-40.93%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.77 (n/a)</td><td>3.08 (n/a)</td><td>3.32 (n/a)</td><td>1.74 (n/a)</td><td>0.84 (n/a)</td><td>1207.10 (n/a)</td><td>740.24 (n/a)</td><td>631.80 (n/a)</td><td>555.80 (n/a)</td><td>272.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.47 (-3.67%)</td><td>3.39 (-10.38%)</td><td>2.67 <b>(-49.85%)</b></td><td>1.75 <b>(+199.68%)</b></td><td>1.54 <b>(-37.16%)</b></td><td>1197.20 <b>(-66.63%)</b></td><td>729.76 <b>(-38.72%)</b></td><td>786.90 <b>(+99.42%)</b></td><td>383.50 (+3.82%)</td><td>323.98 <b>(-76.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.68 (n/a)</td><td>3.79 (n/a)</td><td>5.31 (n/a)</td><td>0.58 (n/a)</td><td>2.45 (n/a)</td><td>3587.70 (n/a)</td><td>1190.90 (n/a)</td><td>394.60 (n/a)</td><td>369.40 (n/a)</td><td>1389.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.02 (+6.02%)</td><td>2.86 <b>(+27.26%)</b></td><td>2.87 <b>(+41.65%)</b></td><td>0.60 (+3.56%)</td><td>1.57 (+2.94%)</td><td>3474.70 (-3.44%)</td><td>1213.90 (-16.32%)</td><td>730.00 <b>(-29.40%)</b></td><td>417.70 (-5.69%)</td><td>1271.32 (+2.97%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.74 (n/a)</td><td>2.25 (n/a)</td><td>2.03 (n/a)</td><td>0.58 (n/a)</td><td>1.52 (n/a)</td><td>3598.50 (n/a)</td><td>1450.56 (n/a)</td><td>1034.00 (n/a)</td><td>442.90 (n/a)</td><td>1234.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.96 <b>(+23.76%)</b></td><td>3.51 (+6.96%)</td><td>2.99 <b>(-26.20%)</b></td><td>1.55 <b>(+163.99%)</b></td><td>1.64 (-1.15%)</td><td>1350.70 <b>(-62.12%)</b></td><td>726.38 <b>(-37.04%)</b></td><td>702.50 <b>(+35.51%)</b></td><td>352.00 (-19.21%)</td><td>379.90 <b>(-71.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.81 (n/a)</td><td>3.28 (n/a)</td><td>4.05 (n/a)</td><td>0.59 (n/a)</td><td>1.66 (n/a)</td><td>3565.60 (n/a)</td><td>1153.72 (n/a)</td><td>518.40 (n/a)</td><td>435.70 (n/a)</td><td>1352.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>6.40 <b>(+77.96%)</b></td><td>4.16 <b>(+104.57%)</b></td><td>3.75 <b>(+149.20%)</b></td><td>3.08 <b>(+422.70%)</b></td><td>1.30 (-6.07%)</td><td>681.10 <b>(-80.87%)</b></td><td>535.60 <b>(-66.94%)</b></td><td>559.00 <b>(-59.87%)</b></td><td>327.70 <b>(-43.81%)</b></td><td>130.05 <b>(-89.39%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.60 (n/a)</td><td>2.03 (n/a)</td><td>1.51 (n/a)</td><td>0.59 (n/a)</td><td>1.38 (n/a)</td><td>3559.90 (n/a)</td><td>1620.30 (n/a)</td><td>1393.00 (n/a)</td><td>583.20 (n/a)</td><td>1225.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.28 <b>(+28.71%)</b></td><td>3.36 (+19.70%)</td><td>3.13 (-12.45%)</td><td>0.60 (+2.21%)</td><td>1.86 (+17.42%)</td><td>3522.30 (-2.17%)</td><td>1147.98 (-11.03%)</td><td>670.40 (+14.21%)</td><td>396.90 <b>(-22.31%)</b></td><td>1334.91 (+0.60%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.10 (n/a)</td><td>2.81 (n/a)</td><td>3.57 (n/a)</td><td>0.58 (n/a)</td><td>1.59 (n/a)</td><td>3600.30 (n/a)</td><td>1290.32 (n/a)</td><td>587.00 (n/a)</td><td>510.90 (n/a)</td><td>1326.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.59 <b>(+37.67%)</b></td><td>3.72 <b>(+20.93%)</b></td><td>4.20 (+7.50%)</td><td>1.14 <b>(-32.41%)</b></td><td>1.65 <b>(+30.07%)</b></td><td>3688.30 <b>(+47.96%)</b></td><td>1530.32 (-5.54%)</td><td>999.40 (-6.98%)</td><td>750.10 <b>(-27.37%)</b></td><td>1218.80 <b>(+55.56%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.06 (n/a)</td><td>3.08 (n/a)</td><td>3.90 (n/a)</td><td>1.68 (n/a)</td><td>1.27 (n/a)</td><td>2492.70 (n/a)</td><td>1620.08 (n/a)</td><td>1074.40 (n/a)</td><td>1032.70 (n/a)</td><td>783.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.37 (+1.85%)</td><td>3.79 (-0.55%)</td><td>4.04 (-3.64%)</td><td>1.21 (-1.35%)</td><td>1.55 (+0.44%)</td><td>3452.90 (+1.37%)</td><td>1457.76 (+0.94%)</td><td>1037.80 (+3.78%)</td><td>781.10 (-1.81%)</td><td>1120.90 (+1.67%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.27 (n/a)</td><td>3.82 (n/a)</td><td>4.19 (n/a)</td><td>1.23 (n/a)</td><td>1.54 (n/a)</td><td>3406.10 (n/a)</td><td>1444.20 (n/a)</td><td>1000.00 (n/a)</td><td>795.50 (n/a)</td><td>1102.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>8.27 (+10.85%)</td><td>5.52 <b>(+76.69%)</b></td><td>5.69 <b>(+240.32%)</b></td><td>2.11 <b>(+92.26%)</b></td><td>2.56 (-6.47%)</td><td>1987.70 <b>(-47.99%)</b></td><td>972.34 <b>(-57.71%)</b></td><td>737.50 <b>(-70.62%)</b></td><td>507.10 (-9.78%)</td><td>610.73 <b>(-58.81%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>7.46 (n/a)</td><td>3.12 (n/a)</td><td>1.67 (n/a)</td><td>1.10 (n/a)</td><td>2.74 (n/a)</td><td>3821.70 (n/a)</td><td>2299.32 (n/a)</td><td>2509.90 (n/a)</td><td>562.10 (n/a)</td><td>1482.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.72 (+12.22%)</td><td>5.54 (-13.52%)</td><td>4.21 <b>(-37.76%)</b></td><td>2.86 <b>(-24.46%)</b></td><td>2.53 <b>(+57.48%)</b></td><td>1466.70 <b>(+32.37%)</b></td><td>897.28 <b>(+28.02%)</b></td><td>995.70 <b>(+60.67%)</b></td><td>480.80 (-10.90%)</td><td>401.00 <b>(+70.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.77 (n/a)</td><td>6.41 (n/a)</td><td>6.77 (n/a)</td><td>3.79 (n/a)</td><td>1.61 (n/a)</td><td>1108.00 (n/a)</td><td>700.90 (n/a)</td><td>619.70 (n/a)</td><td>539.60 (n/a)</td><td>234.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>8.54 (+10.96%)</td><td>5.24 <b>(+31.94%)</b></td><td>5.93 <b>(+50.64%)</b></td><td>1.12 (-4.44%)</td><td>3.50 <b>(+47.46%)</b></td><td>3743.70 (+4.64%)</td><td>1486.44 (-2.28%)</td><td>707.70 <b>(-33.61%)</b></td><td>491.20 (-9.87%)</td><td>1409.11 (+18.72%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>7.70 (n/a)</td><td>3.97 (n/a)</td><td>3.93 (n/a)</td><td>1.17 (n/a)</td><td>2.37 (n/a)</td><td>3577.70 (n/a)</td><td>1521.12 (n/a)</td><td>1066.00 (n/a)</td><td>545.00 (n/a)</td><td>1186.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.21 <b>(-20.35%)</b></td><td>4.99 (-10.67%)</td><td>4.41 <b>(-29.75%)</b></td><td>3.49 <b>(+84.64%)</b></td><td>1.46 <b>(-56.57%)</b></td><td>1200.90 <b>(-45.84%)</b></td><td>895.24 <b>(-21.47%)</b></td><td>950.80 <b>(+42.36%)</b></td><td>581.60 <b>(+25.56%)</b></td><td>239.06 <b>(-71.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.05 (n/a)</td><td>5.59 (n/a)</td><td>6.28 (n/a)</td><td>1.89 (n/a)</td><td>3.37 (n/a)</td><td>2217.30 (n/a)</td><td>1139.96 (n/a)</td><td>667.90 (n/a)</td><td>463.20 (n/a)</td><td>831.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>9.21 (+2.47%)</td><td>5.24 (-7.30%)</td><td>6.39 (-13.56%)</td><td>1.85 <b>(+59.91%)</b></td><td>3.22 (-16.97%)</td><td>2268.00 <b>(-37.47%)</b></td><td>1223.72 (-18.30%)</td><td>656.20 (+15.69%)</td><td>455.50 (-2.42%)</td><td>890.74 <b>(-38.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>8.99 (n/a)</td><td>5.65 (n/a)</td><td>7.39 (n/a)</td><td>1.16 (n/a)</td><td>3.88 (n/a)</td><td>3626.90 (n/a)</td><td>1497.88 (n/a)</td><td>567.20 (n/a)</td><td>466.80 (n/a)</td><td>1437.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>11.34 <b>(+46.16%)</b></td><td>4.97 (-6.08%)</td><td>3.94 <b>(-42.29%)</b></td><td>1.67 <b>(+45.76%)</b></td><td>3.70 <b>(+33.91%)</b></td><td>2516.70 <b>(-31.40%)</b></td><td>1216.70 (-6.92%)</td><td>1063.80 <b>(+73.29%)</b></td><td>369.70 <b>(-31.59%)</b></td><td>787.40 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.76 (n/a)</td><td>5.29 (n/a)</td><td>6.83 (n/a)</td><td>1.14 (n/a)</td><td>2.76 (n/a)</td><td>3668.40 (n/a)</td><td>1307.10 (n/a)</td><td>613.90 (n/a)</td><td>540.40 (n/a)</td><td>1339.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>7.59 <b>(-27.57%)</b></td><td>6.16 (-13.02%)</td><td>6.45 (-4.34%)</td><td>3.54 <b>(+187.02%)</b></td><td>1.54 <b>(-59.40%)</b></td><td>1185.50 <b>(-65.16%)</b></td><td>731.44 <b>(-33.14%)</b></td><td>650.00 (+4.54%)</td><td>552.80 <b>(+38.06%)</b></td><td>257.01 <b>(-80.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>10.48 (n/a)</td><td>7.08 (n/a)</td><td>6.75 (n/a)</td><td>1.23 (n/a)</td><td>3.79 (n/a)</td><td>3402.50 (n/a)</td><td>1094.04 (n/a)</td><td>621.80 (n/a)</td><td>400.40 (n/a)</td><td>1295.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.78 <b>(-24.93%)</b></td><td>5.95 (+16.74%)</td><td>6.18 (+9.78%)</td><td>3.89 <b>(+182.61%)</b></td><td>1.55 <b>(-56.33%)</b></td><td>1079.20 <b>(-64.61%)</b></td><td>749.56 <b>(-44.63%)</b></td><td>678.20 (-8.92%)</td><td>539.00 <b>(+33.22%)</b></td><td>217.01 <b>(-80.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>10.37 (n/a)</td><td>5.10 (n/a)</td><td>5.63 (n/a)</td><td>1.38 (n/a)</td><td>3.55 (n/a)</td><td>3049.80 (n/a)</td><td>1353.78 (n/a)</td><td>744.60 (n/a)</td><td>404.60 (n/a)</td><td>1095.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>10.57 (-6.60%)</td><td>7.42 <b>(+28.93%)</b></td><td>7.52 <b>(+96.91%)</b></td><td>4.69 <b>(+39.33%)</b></td><td>2.31 <b>(-31.53%)</b></td><td>894.70 <b>(-28.23%)</b></td><td>612.94 <b>(-31.77%)</b></td><td>557.40 <b>(-49.22%)</b></td><td>396.80 (+7.07%)</td><td>197.79 <b>(-47.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>11.32 (n/a)</td><td>5.76 (n/a)</td><td>3.82 (n/a)</td><td>3.36 (n/a)</td><td>3.37 (n/a)</td><td>1246.60 (n/a)</td><td>898.28 (n/a)</td><td>1097.60 (n/a)</td><td>370.60 (n/a)</td><td>376.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.34 (-15.31%)</td><td>5.95 (+5.52%)</td><td>7.42 <b>(+69.24%)</b></td><td>1.15 <b>(-66.33%)</b></td><td>3.09 (+16.03%)</td><td>3646.90 <b>(+196.98%)</b></td><td>1228.06 <b>(+42.12%)</b></td><td>564.90 <b>(-40.92%)</b></td><td>502.70 (+18.06%)</td><td>1363.09 <b>(+313.37%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.85 (n/a)</td><td>5.64 (n/a)</td><td>4.39 (n/a)</td><td>3.42 (n/a)</td><td>2.66 (n/a)</td><td>1228.00 (n/a)</td><td>864.10 (n/a)</td><td>956.10 (n/a)</td><td>425.80 (n/a)</td><td>329.75 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>1.40 (-7.54%)</td><td>0.85 <b>(-26.38%)</b></td><td>0.77 <b>(-29.00%)</b></td><td>0.16 <b>(-82.01%)</b></td><td>0.48 <b>(+69.11%)</b></td><td>3278.80 <b>(+455.82%)</b></td><td>1100.52 <b>(+131.36%)</b></td><td>681.40 <b>(+40.84%)</b></td><td>373.50 (+8.17%)</td><td>1227.56 <b>(+985.05%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>1.52 (n/a)</td><td>1.16 (n/a)</td><td>1.08 (n/a)</td><td>0.89 (n/a)</td><td>0.29 (n/a)</td><td>589.90 (n/a)</td><td>475.68 (n/a)</td><td>483.80 (n/a)</td><td>345.30 (n/a)</td><td>113.13 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.02 <b>(-27.07%)</b></td><td>0.75 <b>(-54.35%)</b></td><td>0.32 <b>(-81.23%)</b></td><td>0.30 (+1.13%)</td><td>0.74 (-16.03%)</td><td>3441.60 (-1.12%)</td><td>2367.16 <b>(+107.59%)</b></td><td>3234.80 <b>(+432.65%)</b></td><td>520.10 <b>(+37.08%)</b></td><td>1341.60 (+2.24%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.76 (n/a)</td><td>1.64 (n/a)</td><td>1.73 (n/a)</td><td>0.30 (n/a)</td><td>0.88 (n/a)</td><td>3480.60 (n/a)</td><td>1140.32 (n/a)</td><td>607.30 (n/a)</td><td>379.40 (n/a)</td><td>1312.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.58 (-0.51%)</td><td>2.51 <b>(+40.80%)</b></td><td>3.05 <b>(+409.88%)</b></td><td>0.62 (+10.04%)</td><td>1.16 <b>(-29.12%)</b></td><td>3374.50 (-9.13%)</td><td>1255.22 <b>(-47.31%)</b></td><td>688.10 <b>(-80.39%)</b></td><td>586.30 (+0.51%)</td><td>1191.91 <b>(-27.34%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.60 (n/a)</td><td>1.78 (n/a)</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>1.63 (n/a)</td><td>3713.40 (n/a)</td><td>2382.18 (n/a)</td><td>3508.40 (n/a)</td><td>583.30 (n/a)</td><td>1640.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.97 (+19.29%)</td><td>1.41 <b>(+26.75%)</b></td><td>1.28 <b>(+31.21%)</b></td><td>0.79 <b>(+38.25%)</b></td><td>0.48 (-2.22%)</td><td>660.60 <b>(-27.67%)</b></td><td>412.38 <b>(-25.88%)</b></td><td>410.70 <b>(-23.79%)</b></td><td>265.60 (-16.16%)</td><td>157.56 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.66 (n/a)</td><td>1.11 (n/a)</td><td>0.97 (n/a)</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>913.30 (n/a)</td><td>556.40 (n/a)</td><td>538.90 (n/a)</td><td>316.80 (n/a)</td><td>252.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>1.63 (+1.22%)</td><td>0.98 (-12.67%)</td><td>0.92 <b>(-35.84%)</b></td><td>0.64 <b>(+150.96%)</b></td><td>0.39 <b>(-32.34%)</b></td><td>816.20 <b>(-60.15%)</b></td><td>595.84 <b>(-20.62%)</b></td><td>568.10 <b>(+55.86%)</b></td><td>320.90 (-1.20%)</td><td>193.69 <b>(-73.78%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>1.61 (n/a)</td><td>1.12 (n/a)</td><td>1.44 (n/a)</td><td>0.26 (n/a)</td><td>0.58 (n/a)</td><td>2048.30 (n/a)</td><td>750.62 (n/a)</td><td>364.50 (n/a)</td><td>324.80 (n/a)</td><td>738.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.59 (-19.93%)</td><td>1.24 (-13.53%)</td><td>1.30 (-11.39%)</td><td>0.90 (-2.42%)</td><td>0.31 <b>(-21.60%)</b></td><td>579.40 (+2.48%)</td><td>447.26 (+14.39%)</td><td>401.80 (+12.83%)</td><td>329.80 <b>(+24.88%)</b></td><td>116.43 (+2.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.99 (n/a)</td><td>1.43 (n/a)</td><td>1.47 (n/a)</td><td>0.93 (n/a)</td><td>0.39 (n/a)</td><td>565.40 (n/a)</td><td>390.98 (n/a)</td><td>356.10 (n/a)</td><td>264.10 (n/a)</td><td>113.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (+0.50%)</td><td>0.09 (+3.68%)</td><td>0.08 (+16.31%)</td><td>0.06 (+4.01%)</td><td>0.03 (-3.30%)</td><td>514.00 (-3.85%)</td><td>387.88 (-4.39%)</td><td>400.20 (-14.03%)</td><td>234.70 (-0.47%)</td><td>121.22 (-5.78%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>534.60 (n/a)</td><td>405.68 (n/a)</td><td>465.50 (n/a)</td><td>235.80 (n/a)</td><td>128.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (+0.75%)</td><td>0.12 <b>(+25.51%)</b></td><td>0.12 <b>(+36.03%)</b></td><td>0.10 <b>(+67.75%)</b></td><td>0.01 <b>(-56.00%)</b></td><td>322.90 <b>(-40.38%)</b></td><td>280.66 <b>(-26.79%)</b></td><td>278.40 <b>(-26.49%)</b></td><td>240.50 (-0.78%)</td><td>34.05 <b>(-73.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>541.60 (n/a)</td><td>383.36 (n/a)</td><td>378.70 (n/a)</td><td>242.40 (n/a)</td><td>129.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 <b>(-50.83%)</b></td><td>0.06 <b>(-35.02%)</b></td><td>0.06 (-15.73%)</td><td>0.02 <b>(-57.64%)</b></td><td>0.02 <b>(-47.39%)</b></td><td>1411.90 <b>(+136.06%)</b></td><td>682.44 <b>(+61.27%)</b></td><td>509.10 (+18.67%)</td><td>471.90 <b>(+103.32%)</b></td><td>408.27 <b>(+160.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>598.10 (n/a)</td><td>423.16 (n/a)</td><td>429.00 (n/a)</td><td>232.10 (n/a)</td><td>156.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+12.42%)</td><td>0.09 (+6.12%)</td><td>0.09 <b>(+32.18%)</b></td><td>0.05 (-19.76%)</td><td>0.04 <b>(+26.65%)</b></td><td>658.70 <b>(+24.61%)</b></td><td>423.32 (+0.01%)</td><td>375.60 <b>(-24.35%)</b></td><td>222.20 (-11.05%)</td><td>180.07 <b>(+38.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.60 (n/a)</td><td>423.26 (n/a)</td><td>496.50 (n/a)</td><td>249.80 (n/a)</td><td>130.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.23 (-17.49%)</td><td>0.16 <b>(-28.33%)</b></td><td>0.14 <b>(-35.39%)</b></td><td>0.07 <b>(-49.11%)</b></td><td>0.06 <b>(+25.19%)</b></td><td>920.40 <b>(+96.50%)</b></td><td>498.50 <b>(+56.72%)</b></td><td>455.60 <b>(+54.76%)</b></td><td>284.00 <b>(+21.16%)</b></td><td>253.55 <b>(+185.71%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>468.40 (n/a)</td><td>318.08 (n/a)</td><td>294.40 (n/a)</td><td>234.40 (n/a)</td><td>88.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.29 (+10.69%)</td><td>0.18 (+9.40%)</td><td>0.12 (-5.48%)</td><td>0.12 (+8.59%)</td><td>0.09 <b>(+30.24%)</b></td><td>567.10 (-7.91%)</td><td>430.14 (-3.32%)</td><td>556.40 (+5.80%)</td><td>222.80 (-9.69%)</td><td>180.68 (+12.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>615.80 (n/a)</td><td>444.90 (n/a)</td><td>525.90 (n/a)</td><td>246.70 (n/a)</td><td>160.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.21 (-12.52%)</td><td>0.15 (-3.44%)</td><td>0.15 (+14.63%)</td><td>0.11 (-12.67%)</td><td>0.04 <b>(-22.96%)</b></td><td>594.60 (+14.50%)</td><td>447.08 (+2.22%)</td><td>432.90 (-12.77%)</td><td>316.50 (+14.30%)</td><td>102.81 (+0.33%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>519.30 (n/a)</td><td>437.38 (n/a)</td><td>496.30 (n/a)</td><td>276.90 (n/a)</td><td>102.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.27 (+14.48%)</td><td>0.16 <b>(-20.48%)</b></td><td>0.13 <b>(-41.15%)</b></td><td>0.10 <b>(-23.64%)</b></td><td>0.07 <b>(+65.25%)</b></td><td>644.20 <b>(+30.96%)</b></td><td>476.14 <b>(+36.29%)</b></td><td>513.00 <b>(+69.92%)</b></td><td>242.90 (-12.66%)</td><td>162.21 <b>(+84.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>491.90 (n/a)</td><td>349.36 (n/a)</td><td>301.90 (n/a)</td><td>278.10 (n/a)</td><td>87.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.23 <b>(+54.42%)</b></td><td>0.14 <b>(+38.54%)</b></td><td>0.12 (+7.48%)</td><td>0.11 <b>(+260.41%)</b></td><td>0.05 (+11.63%)</td><td>586.50 <b>(-72.25%)</b></td><td>487.92 <b>(-43.21%)</b></td><td>541.60 (-6.94%)</td><td>285.40 <b>(-35.24%)</b></td><td>120.52 <b>(-82.89%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>2113.70 (n/a)</td><td>859.24 (n/a)</td><td>582.00 (n/a)</td><td>440.70 (n/a)</td><td>704.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.26 (-13.49%)</td><td>0.20 (+7.41%)</td><td>0.18 <b>(+23.46%)</b></td><td>0.13 (+6.95%)</td><td>0.06 <b>(-24.32%)</b></td><td>491.00 (-6.49%)</td><td>354.42 (-10.52%)</td><td>354.40 (-18.99%)</td><td>249.10 (+15.59%)</td><td>101.36 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>525.10 (n/a)</td><td>396.10 (n/a)</td><td>437.50 (n/a)</td><td>215.50 (n/a)</td><td>126.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.51 (+12.65%)</td><td>0.33 (+4.03%)</td><td>0.26 (-15.85%)</td><td>0.21 (+17.83%)</td><td>0.13 (+17.19%)</td><td>611.90 (-15.13%)</td><td>437.68 (-3.54%)</td><td>504.50 (+18.85%)</td><td>256.10 (-11.23%)</td><td>148.66 (-13.38%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>721.00 (n/a)</td><td>453.74 (n/a)</td><td>424.50 (n/a)</td><td>288.50 (n/a)</td><td>171.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.44 (-3.31%)</td><td>0.34 (+7.72%)</td><td>0.31 (+19.91%)</td><td>0.23 (+4.85%)</td><td>0.09 (-14.01%)</td><td>569.00 (-4.63%)</td><td>406.64 (-9.41%)</td><td>422.50 (-16.60%)</td><td>295.50 (+3.43%)</td><td>112.84 (-17.49%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>596.60 (n/a)</td><td>448.86 (n/a)</td><td>506.60 (n/a)</td><td>285.70 (n/a)</td><td>136.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.53 (-1.80%)</td><td>0.41 <b>(+26.91%)</b></td><td>0.46 <b>(+60.70%)</b></td><td>0.22 (-5.52%)</td><td>0.14 (+8.54%)</td><td>609.50 (+5.83%)</td><td>362.30 (-19.39%)</td><td>281.90 <b>(-37.78%)</b></td><td>245.30 (+1.83%)</td><td>156.40 (+13.33%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.54 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>575.90 (n/a)</td><td>449.46 (n/a)</td><td>453.10 (n/a)</td><td>240.90 (n/a)</td><td>138.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.37 (-17.09%)</td><td>0.27 (-11.22%)</td><td>0.25 <b>(-26.39%)</b></td><td>0.20 <b>(+189.58%)</b></td><td>0.07 <b>(-53.11%)</b></td><td>646.10 <b>(-65.47%)</b></td><td>506.90 <b>(-25.38%)</b></td><td>524.90 <b>(+35.84%)</b></td><td>350.80 <b>(+20.59%)</b></td><td>130.20 <b>(-80.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1871.10 (n/a)</td><td>679.34 (n/a)</td><td>386.40 (n/a)</td><td>290.90 (n/a)</td><td>674.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.47 (-6.64%)</td><td>0.36 (-2.31%)</td><td>0.44 <b>(+21.56%)</b></td><td>0.21 (-9.05%)</td><td>0.13 (+16.72%)</td><td>624.80 (+9.96%)</td><td>418.88 (+7.86%)</td><td>297.20 (-17.72%)</td><td>278.50 (+7.12%)</td><td>179.02 <b>(+40.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>568.20 (n/a)</td><td>388.34 (n/a)</td><td>361.20 (n/a)</td><td>260.00 (n/a)</td><td>127.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.54 (-13.61%)</td><td>0.37 (-2.01%)</td><td>0.30 (+4.69%)</td><td>0.25 (+11.13%)</td><td>0.12 <b>(-30.23%)</b></td><td>519.80 (-10.01%)</td><td>390.46 (-5.87%)</td><td>433.60 (-4.49%)</td><td>244.10 (+15.74%)</td><td>118.23 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.62 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>577.60 (n/a)</td><td>414.82 (n/a)</td><td>454.00 (n/a)</td><td>210.90 (n/a)</td><td>169.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (-11.31%)</td><td>0.04 <b>(-28.88%)</b></td><td>0.04 <b>(-28.39%)</b></td><td>0.01 <b>(-69.41%)</b></td><td>0.02 <b>(+37.54%)</b></td><td>1827.20 <b>(+226.93%)</b></td><td>678.00 <b>(+97.66%)</b></td><td>417.60 <b>(+39.62%)</b></td><td>308.60 (+12.75%)</td><td>646.47 <b>(+433.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.90 (n/a)</td><td>343.02 (n/a)</td><td>299.10 (n/a)</td><td>273.70 (n/a)</td><td>121.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 <b>(+53.54%)</b></td><td>0.06 <b>(+34.40%)</b></td><td>0.06 <b>(+46.03%)</b></td><td>0.03 (-6.25%)</td><td>0.03 <b>(+108.82%)</b></td><td>608.00 (+6.69%)</td><td>347.14 (-16.43%)</td><td>276.80 <b>(-31.50%)</b></td><td>171.70 <b>(-34.86%)</b></td><td>168.16 <b>(+52.39%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.90 (n/a)</td><td>415.38 (n/a)</td><td>404.10 (n/a)</td><td>263.60 (n/a)</td><td>110.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>
