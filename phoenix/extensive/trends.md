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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-11.54%)</td><td>0.02 (-0.65%)</td><td>0.02 <b>(+50.15%)</b></td><td>0.01 (-9.96%)</td><td>0.01 (-15.43%)</td><td>524.20 (+11.06%)</td><td>356.48 (-0.31%)</td><td>270.30 <b>(-33.39%)</b></td><td>247.10 (+13.04%)</td><td>138.52 (+8.22%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.00 (n/a)</td><td>357.58 (n/a)</td><td>405.80 (n/a)</td><td>218.60 (n/a)</td><td>128.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-11.60%)</td><td>0.02 (-19.89%)</td><td>0.02 <b>(-22.81%)</b></td><td>0.01 <b>(-24.49%)</b></td><td>0.01 (-3.00%)</td><td>638.90 <b>(+32.44%)</b></td><td>421.22 <b>(+28.08%)</b></td><td>361.80 <b>(+29.54%)</b></td><td>257.70 (+13.13%)</td><td>148.64 <b>(+45.14%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>482.40 (n/a)</td><td>328.86 (n/a)</td><td>279.30 (n/a)</td><td>227.80 (n/a)</td><td>102.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (-0.20%)</td><td>0.02 (-15.48%)</td><td>0.01 <b>(-40.98%)</b></td><td>0.01 (-9.01%)</td><td>0.01 (-4.21%)</td><td>526.20 (+9.90%)</td><td>375.88 (+17.56%)</td><td>417.10 <b>(+69.42%)</b></td><td>210.40 (+0.19%)</td><td>123.31 (+0.38%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>478.80 (n/a)</td><td>319.74 (n/a)</td><td>246.20 (n/a)</td><td>210.00 (n/a)</td><td>122.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (+10.32%)</td><td>0.02 <b>(-23.35%)</b></td><td>0.01 <b>(-34.48%)</b></td><td>0.01 <b>(-42.80%)</b></td><td>0.01 <b>(+79.37%)</b></td><td>1010.80 <b>(+74.85%)</b></td><td>585.30 <b>(+75.64%)</b></td><td>426.60 <b>(+52.63%)</b></td><td>237.40 (-9.35%)</td><td>393.52 <b>(+186.92%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.10 (n/a)</td><td>333.24 (n/a)</td><td>279.50 (n/a)</td><td>261.90 (n/a)</td><td>137.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 <b>(+38.71%)</b></td><td>0.02 (+9.97%)</td><td>0.02 (-1.58%)</td><td>0.01 (-13.58%)</td><td>0.01 <b>(+124.61%)</b></td><td>562.20 (+15.70%)</td><td>373.80 (+1.83%)</td><td>354.80 (+1.60%)</td><td>211.20 <b>(-27.89%)</b></td><td>156.96 <b>(+91.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.90 (n/a)</td><td>367.10 (n/a)</td><td>349.20 (n/a)</td><td>292.90 (n/a)</td><td>82.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-13.10%)</td><td>0.02 (-4.39%)</td><td>0.01 (-6.56%)</td><td>0.01 (+8.00%)</td><td>0.01 <b>(-23.79%)</b></td><td>497.20 (-7.39%)</td><td>383.28 (+0.10%)</td><td>420.90 (+7.02%)</td><td>263.20 (+15.03%)</td><td>108.79 <b>(-21.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>536.90 (n/a)</td><td>382.88 (n/a)</td><td>393.30 (n/a)</td><td>228.80 (n/a)</td><td>137.97 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (-13.99%)</td><td>0.04 (+1.47%)</td><td>0.04 (+0.72%)</td><td>0.03 <b>(+35.77%)</b></td><td>0.01 <b>(-30.21%)</b></td><td>426.30 <b>(-26.33%)</b></td><td>324.60 (-8.92%)</td><td>349.90 (-0.74%)</td><td>229.60 (+16.25%)</td><td>87.18 <b>(-41.77%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>578.70 (n/a)</td><td>356.38 (n/a)</td><td>352.50 (n/a)</td><td>197.50 (n/a)</td><td>149.73 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (+11.62%)</td><td>0.04 (-17.51%)</td><td>0.04 (-13.68%)</td><td>0.02 (-11.67%)</td><td>0.02 <b>(+31.82%)</b></td><td>625.10 (+13.22%)</td><td>401.04 <b>(+32.63%)</b></td><td>280.20 (+15.83%)</td><td>210.70 (-10.42%)</td><td>204.28 <b>(+46.25%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>552.10 (n/a)</td><td>302.38 (n/a)</td><td>241.90 (n/a)</td><td>235.20 (n/a)</td><td>139.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (-5.57%)</td><td>0.02 <b>(-27.07%)</b></td><td>0.02 <b>(-20.73%)</b></td><td>0.01 <b>(-67.64%)</b></td><td>0.02 (+11.23%)</td><td>1855.90 <b>(+209.01%)</b></td><td>766.58 <b>(+79.12%)</b></td><td>584.90 <b>(+26.16%)</b></td><td>255.20 (+5.89%)</td><td>624.64 <b>(+293.92%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.60 (n/a)</td><td>427.96 (n/a)</td><td>463.60 (n/a)</td><td>241.00 (n/a)</td><td>158.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (+4.49%)</td><td>0.04 <b>(+40.38%)</b></td><td>0.05 <b>(+61.44%)</b></td><td>0.02 <b>(+277.12%)</b></td><td>0.01 (-11.74%)</td><td>645.80 <b>(-73.48%)</b></td><td>380.12 <b>(-53.69%)</b></td><td>272.90 <b>(-38.06%)</b></td><td>245.00 (-4.30%)</td><td>172.56 <b>(-81.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2435.40 (n/a)</td><td>820.74 (n/a)</td><td>440.60 (n/a)</td><td>256.00 (n/a)</td><td>908.63 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (-10.68%)</td><td>0.02 (-0.25%)</td><td>0.03 (-1.78%)</td><td>0.02 <b>(+132.50%)</b></td><td>0.01 <b>(-41.98%)</b></td><td>797.30 <b>(-56.99%)</b></td><td>526.60 <b>(-25.81%)</b></td><td>443.30 (+1.79%)</td><td>386.20 (+11.97%)</td><td>164.79 <b>(-74.34%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1853.70 (n/a)</td><td>709.76 (n/a)</td><td>435.50 (n/a)</td><td>344.90 (n/a)</td><td>642.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (-12.32%)</td><td>0.03 (+5.71%)</td><td>0.03 <b>(+30.81%)</b></td><td>0.02 <b>(+200.93%)</b></td><td>0.01 <b>(-39.32%)</b></td><td>648.60 <b>(-66.77%)</b></td><td>457.04 <b>(-40.23%)</b></td><td>484.60 <b>(-23.55%)</b></td><td>237.60 (+14.07%)</td><td>156.67 <b>(-77.61%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1951.90 (n/a)</td><td>764.64 (n/a)</td><td>633.90 (n/a)</td><td>208.30 (n/a)</td><td>699.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 <b>(-21.19%)</b></td><td>0.09 (+1.14%)</td><td>0.09 (+14.47%)</td><td>0.05 (+11.53%)</td><td>0.02 <b>(-37.12%)</b></td><td>449.70 (-10.33%)</td><td>301.54 (-6.19%)</td><td>269.70 (-12.66%)</td><td>241.40 <b>(+26.92%)</b></td><td>85.68 <b>(-26.93%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>501.50 (n/a)</td><td>321.42 (n/a)</td><td>308.80 (n/a)</td><td>190.20 (n/a)</td><td>117.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 <b>(+24.58%)</b></td><td>0.09 (+17.07%)</td><td>0.09 (+9.42%)</td><td>0.05 (+14.45%)</td><td>0.03 (+0.49%)</td><td>493.20 (-12.62%)</td><td>307.22 (-18.64%)</td><td>274.90 (-8.64%)</td><td>183.50 (-19.69%)</td><td>115.35 <b>(-30.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>564.40 (n/a)</td><td>377.62 (n/a)</td><td>300.90 (n/a)</td><td>228.50 (n/a)</td><td>166.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 <b>(+67.73%)</b></td><td>0.08 <b>(+58.01%)</b></td><td>0.09 <b>(+81.98%)</b></td><td>0.05 <b>(+25.13%)</b></td><td>0.03 <b>(+168.12%)</b></td><td>466.60 <b>(-20.09%)</b></td><td>321.50 <b>(-32.36%)</b></td><td>269.20 <b>(-45.05%)</b></td><td>212.60 <b>(-40.38%)</b></td><td>112.61 <b>(+33.60%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>583.90 (n/a)</td><td>475.28 (n/a)</td><td>489.90 (n/a)</td><td>356.60 (n/a)</td><td>84.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (-3.93%)</td><td>0.08 (+14.65%)</td><td>0.09 <b>(+54.37%)</b></td><td>0.04 (+13.81%)</td><td>0.03 (-0.69%)</td><td>550.40 (-12.12%)</td><td>362.66 (-13.49%)</td><td>274.30 <b>(-35.21%)</b></td><td>233.90 (+4.09%)</td><td>156.14 (-7.75%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>626.30 (n/a)</td><td>419.22 (n/a)</td><td>423.40 (n/a)</td><td>224.70 (n/a)</td><td>169.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (-13.17%)</td><td>0.07 <b>(+21.79%)</b></td><td>0.08 <b>(+69.72%)</b></td><td>0.05 (+16.40%)</td><td>0.02 <b>(-29.58%)</b></td><td>539.40 (-14.09%)</td><td>364.52 <b>(-23.69%)</b></td><td>302.10 <b>(-41.08%)</b></td><td>235.30 (+15.12%)</td><td>126.51 <b>(-24.60%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>627.90 (n/a)</td><td>477.68 (n/a)</td><td>512.70 (n/a)</td><td>204.40 (n/a)</td><td>167.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(-33.66%)</b></td><td>0.05 <b>(-21.32%)</b></td><td>0.05 (-14.43%)</td><td>0.04 (+3.17%)</td><td>0.01 <b>(-65.86%)</b></td><td>549.70 (-3.07%)</td><td>456.00 (+18.20%)</td><td>468.10 (+16.88%)</td><td>376.70 <b>(+50.74%)</b></td><td>65.81 <b>(-48.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.10 (n/a)</td><td>385.80 (n/a)</td><td>400.50 (n/a)</td><td>249.90 (n/a)</td><td>128.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.20 (-0.90%)</td><td>0.15 (+2.35%)</td><td>0.17 (-0.72%)</td><td>0.10 (+6.93%)</td><td>0.04 (-12.18%)</td><td>486.90 (-6.47%)</td><td>342.22 (-5.13%)</td><td>281.00 (+0.72%)</td><td>242.80 (+0.91%)</td><td>108.96 (-19.21%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>520.60 (n/a)</td><td>360.74 (n/a)</td><td>279.00 (n/a)</td><td>240.60 (n/a)</td><td>134.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.19 (-0.71%)</td><td>0.16 (+12.04%)</td><td>0.16 (-3.95%)</td><td>0.12 <b>(+55.09%)</b></td><td>0.03 <b>(-43.85%)</b></td><td>417.60 <b>(-35.52%)</b></td><td>320.28 <b>(-21.07%)</b></td><td>307.60 (+4.09%)</td><td>256.80 (+0.75%)</td><td>67.54 <b>(-63.89%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>647.60 (n/a)</td><td>405.76 (n/a)</td><td>295.50 (n/a)</td><td>254.90 (n/a)</td><td>187.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.21 (+0.49%)</td><td>0.18 (+16.66%)</td><td>0.20 <b>(+20.51%)</b></td><td>0.13 <b>(+38.60%)</b></td><td>0.03 <b>(-37.18%)</b></td><td>376.70 <b>(-27.85%)</b></td><td>284.06 <b>(-20.97%)</b></td><td>248.30 (-17.01%)</td><td>234.90 (-0.47%)</td><td>60.89 <b>(-56.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>522.10 (n/a)</td><td>359.44 (n/a)</td><td>299.20 (n/a)</td><td>236.00 (n/a)</td><td>138.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.20 (+0.88%)</td><td>0.16 <b>(+25.30%)</b></td><td>0.16 <b>(+46.71%)</b></td><td>0.09 (+3.70%)</td><td>0.04 (-6.06%)</td><td>529.80 (-3.57%)</td><td>329.32 <b>(-20.70%)</b></td><td>302.40 <b>(-31.85%)</b></td><td>243.10 (-0.86%)</td><td>115.06 (-2.99%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>549.40 (n/a)</td><td>415.28 (n/a)</td><td>443.70 (n/a)</td><td>245.20 (n/a)</td><td>118.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.19 (-13.25%)</td><td>0.17 <b>(+34.53%)</b></td><td>0.17 <b>(+57.44%)</b></td><td>0.14 <b>(+475.46%)</b></td><td>0.02 <b>(-76.13%)</b></td><td>340.90 <b>(-82.62%)</b></td><td>291.24 <b>(-57.33%)</b></td><td>293.70 <b>(-36.48%)</b></td><td>261.30 (+15.31%)</td><td>32.58 <b>(-95.51%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1961.40 (n/a)</td><td>682.48 (n/a)</td><td>462.40 (n/a)</td><td>226.60 (n/a)</td><td>724.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.19 <b>(-28.65%)</b></td><td>0.14 (-0.41%)</td><td>0.17 <b>(+74.95%)</b></td><td>0.08 (+11.00%)</td><td>0.05 <b>(-42.28%)</b></td><td>631.40 (-9.92%)</td><td>385.74 (-11.84%)</td><td>291.80 <b>(-42.83%)</b></td><td>264.70 <b>(+40.20%)</b></td><td>158.31 <b>(-26.11%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>700.90 (n/a)</td><td>437.54 (n/a)</td><td>510.40 (n/a)</td><td>188.80 (n/a)</td><td>214.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (-16.30%)</td><td>0.01 (-19.85%)</td><td>0.01 <b>(-40.79%)</b></td><td>0.00 <b>(-33.77%)</b></td><td>0.00 (+1.93%)</td><td>737.40 <b>(+50.98%)</b></td><td>461.44 <b>(+31.33%)</b></td><td>491.40 <b>(+68.87%)</b></td><td>270.30 (+19.44%)</td><td>192.57 <b>(+60.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.40 (n/a)</td><td>351.36 (n/a)</td><td>291.00 (n/a)</td><td>226.30 (n/a)</td><td>120.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (-17.61%)</td><td>0.01 <b>(-21.51%)</b></td><td>0.01 <b>(-27.96%)</b></td><td>0.01 (-1.62%)</td><td>0.00 <b>(-33.68%)</b></td><td>472.90 (+1.63%)</td><td>387.62 <b>(+24.31%)</b></td><td>403.80 <b>(+38.81%)</b></td><td>293.30 <b>(+21.35%)</b></td><td>67.29 <b>(-23.74%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>465.30 (n/a)</td><td>311.82 (n/a)</td><td>290.90 (n/a)</td><td>241.70 (n/a)</td><td>88.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (-12.45%)</td><td>0.01 (+5.22%)</td><td>0.01 <b>(+53.63%)</b></td><td>0.00 (-1.12%)</td><td>0.00 (-13.31%)</td><td>565.20 (+1.13%)</td><td>380.40 (-5.58%)</td><td>300.70 <b>(-34.91%)</b></td><td>229.20 (+14.20%)</td><td>158.02 (+7.68%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>558.90 (n/a)</td><td>402.90 (n/a)</td><td>462.00 (n/a)</td><td>200.70 (n/a)</td><td>146.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (+4.23%)</td><td>0.01 (-3.30%)</td><td>0.01 <b>(-27.88%)</b></td><td>0.00 (-3.95%)</td><td>0.00 <b>(+39.40%)</b></td><td>539.60 (+4.11%)</td><td>423.60 (+8.32%)</td><td>490.90 <b>(+38.67%)</b></td><td>262.70 (-4.05%)</td><td>135.47 <b>(+38.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.30 (n/a)</td><td>391.08 (n/a)</td><td>354.00 (n/a)</td><td>273.80 (n/a)</td><td>97.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 <b>(+62.47%)</b></td><td>0.01 <b>(+41.00%)</b></td><td>0.01 <b>(+65.05%)</b></td><td>0.00 (-2.33%)</td><td>0.00 <b>(+350.73%)</b></td><td>569.10 (+2.37%)</td><td>370.32 <b>(-20.78%)</b></td><td>277.40 <b>(-39.42%)</b></td><td>250.70 <b>(-38.45%)</b></td><td>150.73 <b>(+174.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>555.90 (n/a)</td><td>467.46 (n/a)</td><td>457.90 (n/a)</td><td>407.30 (n/a)</td><td>54.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 <b>(+26.50%)</b></td><td>0.01 (+4.47%)</td><td>0.01 (+4.50%)</td><td>0.00 <b>(-26.75%)</b></td><td>0.00 <b>(+67.19%)</b></td><td>802.40 <b>(+36.51%)</b></td><td>504.20 (+2.87%)</td><td>503.60 (-4.29%)</td><td>292.20 <b>(-20.94%)</b></td><td>192.57 <b>(+80.88%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>587.80 (n/a)</td><td>490.12 (n/a)</td><td>526.20 (n/a)</td><td>369.60 (n/a)</td><td>106.46 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+13.74%)</td><td>0.02 (+14.76%)</td><td>0.02 <b>(+43.08%)</b></td><td>0.01 (+2.63%)</td><td>0.01 (+6.18%)</td><td>511.00 (-2.56%)</td><td>340.24 (-13.00%)</td><td>289.50 <b>(-30.12%)</b></td><td>217.90 (-12.10%)</td><td>122.36 (-6.06%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.40 (n/a)</td><td>391.06 (n/a)</td><td>414.30 (n/a)</td><td>247.90 (n/a)</td><td>130.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(-20.44%)</b></td><td>0.02 (-4.93%)</td><td>0.02 <b>(+25.29%)</b></td><td>0.01 (+14.11%)</td><td>0.00 <b>(-44.91%)</b></td><td>476.60 (-12.37%)</td><td>362.54 (-3.26%)</td><td>322.20 <b>(-20.19%)</b></td><td>270.40 <b>(+25.71%)</b></td><td>92.43 <b>(-35.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.90 (n/a)</td><td>374.76 (n/a)</td><td>403.70 (n/a)</td><td>215.10 (n/a)</td><td>143.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-9.17%)</td><td>0.01 (-7.60%)</td><td>0.01 (-15.73%)</td><td>0.01 (-12.96%)</td><td>0.01 (+3.97%)</td><td>609.90 (+14.90%)</td><td>428.86 (+11.18%)</td><td>446.20 (+18.67%)</td><td>259.70 (+10.09%)</td><td>152.60 <b>(+27.21%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.80 (n/a)</td><td>385.72 (n/a)</td><td>376.00 (n/a)</td><td>235.90 (n/a)</td><td>119.95 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 <b>(-34.03%)</b></td><td>0.01 (-19.26%)</td><td>0.01 <b>(-21.80%)</b></td><td>0.01 (+2.25%)</td><td>0.00 <b>(-64.50%)</b></td><td>603.70 (-2.20%)</td><td>476.56 (+13.70%)</td><td>464.30 <b>(+27.87%)</b></td><td>392.20 <b>(+51.60%)</b></td><td>79.81 <b>(-48.07%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.30 (n/a)</td><td>419.12 (n/a)</td><td>363.10 (n/a)</td><td>258.70 (n/a)</td><td>153.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+1.81%)</td><td>0.01 <b>(-29.40%)</b></td><td>0.01 <b>(-52.12%)</b></td><td>0.00 <b>(-44.35%)</b></td><td>0.01 (+1.50%)</td><td>2398.60 <b>(+79.70%)</b></td><td>906.30 <b>(+65.22%)</b></td><td>619.10 <b>(+108.87%)</b></td><td>230.10 (-1.79%)</td><td>855.42 <b>(+85.57%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1334.80 (n/a)</td><td>548.54 (n/a)</td><td>296.40 (n/a)</td><td>234.30 (n/a)</td><td>460.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+1.41%)</td><td>0.01 (+15.22%)</td><td>0.02 <b>(+59.78%)</b></td><td>0.00 <b>(-68.15%)</b></td><td>0.01 <b>(+46.31%)</b></td><td>1856.30 <b>(+213.99%)</b></td><td>639.78 <b>(+32.21%)</b></td><td>337.30 <b>(-37.41%)</b></td><td>256.40 (-1.38%)</td><td>684.15 <b>(+425.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.20 (n/a)</td><td>483.90 (n/a)</td><td>538.90 (n/a)</td><td>260.00 (n/a)</td><td>130.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (-8.52%)</td><td>0.04 (+10.07%)</td><td>0.04 (+17.55%)</td><td>0.02 (+5.11%)</td><td>0.01 <b>(-27.43%)</b></td><td>469.20 (-4.87%)</td><td>302.74 (-13.58%)</td><td>268.50 (-14.92%)</td><td>231.50 (+9.30%)</td><td>96.26 <b>(-25.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.20 (n/a)</td><td>350.32 (n/a)</td><td>315.60 (n/a)</td><td>211.80 (n/a)</td><td>129.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 <b>(+30.81%)</b></td><td>0.04 <b>(+50.78%)</b></td><td>0.04 <b>(+71.99%)</b></td><td>0.04 <b>(+62.05%)</b></td><td>0.01 (-4.84%)</td><td>299.50 <b>(-38.30%)</b></td><td>259.50 <b>(-36.17%)</b></td><td>267.40 <b>(-41.87%)</b></td><td>186.90 <b>(-23.56%)</b></td><td>45.26 <b>(-55.75%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.40 (n/a)</td><td>406.52 (n/a)</td><td>460.00 (n/a)</td><td>244.50 (n/a)</td><td>102.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 <b>(-45.09%)</b></td><td>0.03 (-16.86%)</td><td>0.02 (+2.33%)</td><td>0.02 <b>(+216.78%)</b></td><td>0.01 <b>(-69.66%)</b></td><td>643.10 <b>(-68.43%)</b></td><td>440.56 <b>(-34.78%)</b></td><td>433.40 (-2.28%)</td><td>335.30 <b>(+82.13%)</b></td><td>124.20 <b>(-83.89%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2037.20 (n/a)</td><td>675.52 (n/a)</td><td>443.50 (n/a)</td><td>184.10 (n/a)</td><td>771.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (-10.84%)</td><td>0.03 <b>(+26.79%)</b></td><td>0.04 <b>(+82.32%)</b></td><td>0.02 <b>(+33.61%)</b></td><td>0.01 <b>(-38.38%)</b></td><td>478.60 <b>(-25.15%)</b></td><td>318.16 <b>(-28.98%)</b></td><td>291.20 <b>(-45.16%)</b></td><td>243.80 (+12.14%)</td><td>94.43 <b>(-46.55%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>639.40 (n/a)</td><td>448.00 (n/a)</td><td>531.00 (n/a)</td><td>217.40 (n/a)</td><td>176.67 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 <b>(+25.23%)</b></td><td>0.03 (+3.55%)</td><td>0.02 <b>(-30.65%)</b></td><td>0.02 (-15.72%)</td><td>0.01 <b>(+55.86%)</b></td><td>645.40 (+18.66%)</td><td>400.16 (+4.28%)</td><td>433.20 <b>(+44.21%)</b></td><td>228.10 <b>(-20.16%)</b></td><td>171.49 <b>(+39.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.90 (n/a)</td><td>383.74 (n/a)</td><td>300.40 (n/a)</td><td>285.70 (n/a)</td><td>123.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (+15.49%)</td><td>0.03 <b>(+26.43%)</b></td><td>0.02 (+19.58%)</td><td>0.02 (+8.30%)</td><td>0.01 <b>(+33.81%)</b></td><td>499.80 (-7.65%)</td><td>387.76 (-19.25%)</td><td>441.60 (-16.36%)</td><td>260.20 (-13.41%)</td><td>108.92 (+6.47%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.20 (n/a)</td><td>480.18 (n/a)</td><td>528.00 (n/a)</td><td>300.50 (n/a)</td><td>102.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 <b>(-53.09%)</b></td><td>0.04 <b>(-28.54%)</b></td><td>0.04 (-3.32%)</td><td>0.04 <b>(+210.75%)</b></td><td>0.01 <b>(-80.81%)</b></td><td>598.00 <b>(-67.82%)</b></td><td>511.98 <b>(-21.89%)</b></td><td>507.30 (+3.43%)</td><td>391.70 <b>(+113.11%)</b></td><td>88.15 <b>(-87.16%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1858.30 (n/a)</td><td>655.44 (n/a)</td><td>490.50 (n/a)</td><td>183.80 (n/a)</td><td>686.61 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (+0.34%)</td><td>0.07 <b>(+29.50%)</b></td><td>0.07 <b>(+60.47%)</b></td><td>0.05 <b>(+61.20%)</b></td><td>0.01 <b>(-43.97%)</b></td><td>423.50 <b>(-37.96%)</b></td><td>303.36 <b>(-31.93%)</b></td><td>287.30 <b>(-37.69%)</b></td><td>249.20 (-0.36%)</td><td>71.00 <b>(-62.68%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>682.60 (n/a)</td><td>445.64 (n/a)</td><td>461.10 (n/a)</td><td>250.10 (n/a)</td><td>190.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(-29.24%)</b></td><td>0.05 (-6.22%)</td><td>0.05 (+16.24%)</td><td>0.03 <b>(+222.44%)</b></td><td>0.02 <b>(-54.26%)</b></td><td>634.00 <b>(-68.99%)</b></td><td>451.84 <b>(-37.09%)</b></td><td>441.60 (-13.97%)</td><td>303.30 <b>(+41.33%)</b></td><td>147.22 <b>(-80.57%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2044.30 (n/a)</td><td>718.20 (n/a)</td><td>513.30 (n/a)</td><td>214.60 (n/a)</td><td>757.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (+10.11%)</td><td>0.06 (-12.52%)</td><td>0.05 <b>(-23.66%)</b></td><td>0.03 <b>(-30.81%)</b></td><td>0.03 <b>(+35.72%)</b></td><td>691.50 <b>(+44.51%)</b></td><td>450.82 <b>(+24.51%)</b></td><td>460.90 <b>(+31.01%)</b></td><td>191.50 (-9.20%)</td><td>177.14 <b>(+56.40%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>478.50 (n/a)</td><td>362.08 (n/a)</td><td>351.80 (n/a)</td><td>210.90 (n/a)</td><td>113.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (+13.17%)</td><td>0.06 (+15.09%)</td><td>0.05 (+1.54%)</td><td>0.04 (+3.31%)</td><td>0.03 <b>(+21.30%)</b></td><td>530.10 (-3.21%)</td><td>390.68 (-10.94%)</td><td>444.80 (-1.53%)</td><td>208.60 (-11.65%)</td><td>132.40 (+6.32%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.70 (n/a)</td><td>438.68 (n/a)</td><td>451.70 (n/a)</td><td>236.10 (n/a)</td><td>124.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (-12.04%)</td><td>0.05 (+10.95%)</td><td>0.06 <b>(+48.75%)</b></td><td>0.03 (-0.63%)</td><td>0.01 <b>(-25.83%)</b></td><td>600.90 (+0.64%)</td><td>429.64 (-12.55%)</td><td>380.20 <b>(-32.77%)</b></td><td>305.80 (+13.68%)</td><td>119.36 (-12.33%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>597.10 (n/a)</td><td>491.28 (n/a)</td><td>565.50 (n/a)</td><td>269.00 (n/a)</td><td>136.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>463.30 (n/a)</td><td>296.74 (n/a)</td><td>268.70 (n/a)</td><td>226.60 (n/a)</td><td>95.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.60 (n/a)</td><td>404.44 (n/a)</td><td>364.20 (n/a)</td><td>269.80 (n/a)</td><td>130.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.70 (n/a)</td><td>493.12 (n/a)</td><td>488.00 (n/a)</td><td>452.50 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2454.50 (n/a)</td><td>768.12 (n/a)</td><td>393.90 (n/a)</td><td>263.10 (n/a)</td><td>945.56 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.10 (n/a)</td><td>347.76 (n/a)</td><td>302.30 (n/a)</td><td>231.10 (n/a)</td><td>124.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.80 (n/a)</td><td>457.12 (n/a)</td><td>541.20 (n/a)</td><td>276.90 (n/a)</td><td>139.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>737.90 (n/a)</td><td>473.54 (n/a)</td><td>504.80 (n/a)</td><td>272.60 (n/a)</td><td>189.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>284.90 (n/a)</td><td>266.76 (n/a)</td><td>270.70 (n/a)</td><td>230.30 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>536.40 (n/a)</td><td>423.20 (n/a)</td><td>527.80 (n/a)</td><td>227.30 (n/a)</td><td>149.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 <b>(-23.03%)</b></td><td>0.09 <b>(-43.10%)</b></td><td>0.10 <b>(-37.68%)</b></td><td>0.03 <b>(-82.38%)</b></td><td>0.04 <b>(+221.33%)</b></td><td>1897.20 <b>(+467.51%)</b></td><td>749.06 <b>(+145.02%)</b></td><td>497.10 <b>(+60.46%)</b></td><td>360.50 <b>(+29.91%)</b></td><td>644.52 <b>(+2637.26%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>334.30 (n/a)</td><td>305.72 (n/a)</td><td>309.80 (n/a)</td><td>277.50 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>496.60 (n/a)</td><td>425.34 (n/a)</td><td>442.30 (n/a)</td><td>313.80 (n/a)</td><td>69.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>495.70 (n/a)</td><td>398.24 (n/a)</td><td>427.70 (n/a)</td><td>271.60 (n/a)</td><td>86.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>496.60 (n/a)</td><td>354.84 (n/a)</td><td>409.30 (n/a)</td><td>223.80 (n/a)</td><td>121.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>502.90 (n/a)</td><td>326.22 (n/a)</td><td>269.40 (n/a)</td><td>246.20 (n/a)</td><td>106.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.50 (n/a)</td><td>432.58 (n/a)</td><td>398.70 (n/a)</td><td>288.60 (n/a)</td><td>146.97 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.20 (n/a)</td><td>328.12 (n/a)</td><td>331.00 (n/a)</td><td>229.40 (n/a)</td><td>103.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.80 (n/a)</td><td>387.14 (n/a)</td><td>449.90 (n/a)</td><td>242.10 (n/a)</td><td>136.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.40 (n/a)</td><td>329.36 (n/a)</td><td>294.50 (n/a)</td><td>249.50 (n/a)</td><td>110.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>553.30 (n/a)</td><td>372.86 (n/a)</td><td>291.10 (n/a)</td><td>233.10 (n/a)</td><td>162.00 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>434.90 (n/a)</td><td>320.94 (n/a)</td><td>273.50 (n/a)</td><td>244.30 (n/a)</td><td>92.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>689.40 (n/a)</td><td>401.58 (n/a)</td><td>298.50 (n/a)</td><td>251.10 (n/a)</td><td>181.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>527.60 (n/a)</td><td>365.00 (n/a)</td><td>292.80 (n/a)</td><td>227.90 (n/a)</td><td>141.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>407.80 (n/a)</td><td>333.14 (n/a)</td><td>337.80 (n/a)</td><td>280.30 (n/a)</td><td>50.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2443.70 (n/a)</td><td>727.80 (n/a)</td><td>264.40 (n/a)</td><td>211.00 (n/a)</td><td>964.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.90 (n/a)</td><td>318.30 (n/a)</td><td>248.80 (n/a)</td><td>228.20 (n/a)</td><td>141.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.20 (n/a)</td><td>482.86 (n/a)</td><td>485.60 (n/a)</td><td>386.70 (n/a)</td><td>77.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>541.70 (n/a)</td><td>392.80 (n/a)</td><td>455.30 (n/a)</td><td>190.40 (n/a)</td><td>168.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>424.70 (n/a)</td><td>303.86 (n/a)</td><td>287.50 (n/a)</td><td>240.60 (n/a)</td><td>70.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>454.30 (n/a)</td><td>375.36 (n/a)</td><td>437.50 (n/a)</td><td>259.10 (n/a)</td><td>95.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.90 (n/a)</td><td>350.82 (n/a)</td><td>259.80 (n/a)</td><td>237.40 (n/a)</td><td>148.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.60 (n/a)</td><td>359.20 (n/a)</td><td>358.30 (n/a)</td><td>245.50 (n/a)</td><td>94.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.00 (n/a)</td><td>286.08 (n/a)</td><td>278.40 (n/a)</td><td>189.90 (n/a)</td><td>87.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.10 (n/a)</td><td>377.78 (n/a)</td><td>424.60 (n/a)</td><td>233.10 (n/a)</td><td>134.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.30 (n/a)</td><td>342.72 (n/a)</td><td>321.80 (n/a)</td><td>253.20 (n/a)</td><td>95.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.10 (n/a)</td><td>466.38 (n/a)</td><td>513.10 (n/a)</td><td>307.50 (n/a)</td><td>133.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>555.60 (n/a)</td><td>380.20 (n/a)</td><td>284.90 (n/a)</td><td>279.70 (n/a)</td><td>135.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>638.70 (n/a)</td><td>422.40 (n/a)</td><td>476.80 (n/a)</td><td>221.50 (n/a)</td><td>190.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>481.40 (n/a)</td><td>315.86 (n/a)</td><td>286.60 (n/a)</td><td>257.70 (n/a)</td><td>93.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.10 (n/a)</td><td>354.64 (n/a)</td><td>280.80 (n/a)</td><td>235.00 (n/a)</td><td>146.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>514.50 (n/a)</td><td>312.44 (n/a)</td><td>252.20 (n/a)</td><td>234.30 (n/a)</td><td>117.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>480.70 (n/a)</td><td>408.52 (n/a)</td><td>409.60 (n/a)</td><td>294.00 (n/a)</td><td>77.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>632.40 (n/a)</td><td>473.20 (n/a)</td><td>526.80 (n/a)</td><td>273.80 (n/a)</td><td>169.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1825.90 (n/a)</td><td>689.10 (n/a)</td><td>488.20 (n/a)</td><td>260.70 (n/a)</td><td>651.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2537.60 (n/a)</td><td>812.52 (n/a)</td><td>457.60 (n/a)</td><td>235.20 (n/a)</td><td>969.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>518.70 (n/a)</td><td>392.32 (n/a)</td><td>433.20 (n/a)</td><td>249.80 (n/a)</td><td>106.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.90 (n/a)</td><td>455.92 (n/a)</td><td>508.90 (n/a)</td><td>260.90 (n/a)</td><td>120.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>643.70 (n/a)</td><td>471.48 (n/a)</td><td>462.80 (n/a)</td><td>286.30 (n/a)</td><td>132.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.50 (+1.25%)</td><td>0.44 (+11.37%)</td><td>0.45 <b>(+28.64%)</b></td><td>0.37 (+15.04%)</td><td>0.06 <b>(-30.59%)</b></td><td>601.00 (-13.07%)</td><td>512.18 (-11.92%)</td><td>493.00 <b>(-22.26%)</b></td><td>446.40 (-1.22%)</td><td>68.86 <b>(-39.69%)</b></td><td>21.14 (+1.25%)</td><td>18.69 (+11.37%)</td><td>19.14 <b>(+28.64%)</b></td><td>15.70 (+15.04%)</td><td>2.44 <b>(-30.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>691.40 (n/a)</td><td>581.48 (n/a)</td><td>634.20 (n/a)</td><td>451.90 (n/a)</td><td>114.17 (n/a)</td><td>20.88 (n/a)</td><td>16.78 (n/a)</td><td>14.88 (n/a)</td><td>13.65 (n/a)</td><td>3.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.47 (-0.54%)</td><td>0.35 (-6.15%)</td><td>0.38 (-4.79%)</td><td>0.19 (-9.54%)</td><td>0.11 (+6.08%)</td><td>1173.20 (+10.53%)</td><td>703.58 (+8.63%)</td><td>585.80 (+5.02%)</td><td>465.70 (+0.54%)</td><td>284.93 (+17.36%)</td><td>20.26 (-0.54%)</td><td>14.92 (-6.15%)</td><td>16.11 (-4.79%)</td><td>8.04 (-9.54%)</td><td>4.80 (+6.08%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.40 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>1061.40 (n/a)</td><td>647.66 (n/a)</td><td>557.80 (n/a)</td><td>463.20 (n/a)</td><td>242.79 (n/a)</td><td>20.37 (n/a)</td><td>15.90 (n/a)</td><td>16.92 (n/a)</td><td>8.89 (n/a)</td><td>4.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.31 (+2.59%)</td><td>0.30 (+0.65%)</td><td>0.30 (+0.46%)</td><td>0.29 (-1.74%)</td><td>0.01 <b>(+189.64%)</b></td><td>86361.50 (+1.77%)</td><td>83076.40 (-0.59%)</td><td>83106.40 (-0.46%)</td><td>80752.00 (-2.53%)</td><td>2211.14 <b>(+186.73%)</b></td><td>212.75 (+2.59%)</td><td>206.91 (+0.65%)</td><td>206.72 (+0.46%)</td><td>198.93 (-1.74%)</td><td>5.45 <b>(+189.64%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84858.20 (n/a)</td><td>83572.40 (n/a)</td><td>83487.00 (n/a)</td><td>82846.80 (n/a)</td><td>771.15 (n/a)</td><td>207.37 (n/a)</td><td>205.58 (n/a)</td><td>205.78 (n/a)</td><td>202.45 (n/a)</td><td>1.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.04 (+0.48%)</td><td>1.02 (+2.12%)</td><td>1.02 (+2.19%)</td><td>0.99 (+4.95%)</td><td>0.02 <b>(-44.94%)</b></td><td>25363.30 (-4.72%)</td><td>24692.70 (-2.14%)</td><td>24629.60 (-2.15%)</td><td>24233.20 (-0.48%)</td><td>440.87 <b>(-48.05%)</b></td><td>708.94 (+0.48%)</td><td>695.92 (+2.12%)</td><td>697.53 (+2.19%)</td><td>677.35 (+4.95%)</td><td>12.31 <b>(-44.94%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.95 (n/a)</td><td>0.03 (n/a)</td><td>26618.80 (n/a)</td><td>25231.72 (n/a)</td><td>25169.80 (n/a)</td><td>24349.70 (n/a)</td><td>848.72 (n/a)</td><td>705.55 (n/a)</td><td>681.49 (n/a)</td><td>682.56 (n/a)</td><td>645.40 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.82 (-0.47%)</td><td>0.81 (-1.06%)</td><td>0.80 (-1.59%)</td><td>0.79 (-0.81%)</td><td>0.01 (+19.87%)</td><td>95020.30 (+0.82%)</td><td>93495.86 (+1.07%)</td><td>93848.20 (+1.61%)</td><td>91613.80 (+0.47%)</td><td>1337.69 <b>(+21.08%)</b></td><td>750.10 (-0.47%)</td><td>735.12 (-1.06%)</td><td>732.24 (-1.59%)</td><td>723.21 (-0.81%)</td><td>10.57 (+19.87%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.83 (n/a)</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94249.70 (n/a)</td><td>92502.54 (n/a)</td><td>92360.30 (n/a)</td><td>91183.90 (n/a)</td><td>1104.81 (n/a)</td><td>753.64 (n/a)</td><td>742.98 (n/a)</td><td>744.04 (n/a)</td><td>729.12 (n/a)</td><td>8.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.78 (-0.30%)</td><td>0.76 (-0.43%)</td><td>0.77 (+0.04%)</td><td>0.74 (-2.40%)</td><td>0.02 <b>(+76.48%)</b></td><td>102601.50 (+2.45%)</td><td>98812.52 (+0.46%)</td><td>98091.30 (-0.04%)</td><td>97269.50 (+0.30%)</td><td>2155.58 <b>(+81.88%)</b></td><td>706.49 (-0.30%)</td><td>695.71 (-0.43%)</td><td>700.57 (+0.04%)</td><td>669.77 (-2.40%)</td><td>14.78 <b>(+76.48%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100143.30 (n/a)</td><td>98362.62 (n/a)</td><td>98129.90 (n/a)</td><td>96975.70 (n/a)</td><td>1185.14 (n/a)</td><td>708.63 (n/a)</td><td>698.71 (n/a)</td><td>700.29 (n/a)</td><td>686.21 (n/a)</td><td>8.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.81 (+0.50%)</td><td>0.80 (+0.06%)</td><td>0.80 (+0.01%)</td><td>0.79 (-0.10%)</td><td>0.01 <b>(+56.47%)</b></td><td>95311.70 (+0.10%)</td><td>94578.72 (-0.06%)</td><td>94545.30 (-0.01%)</td><td>93748.50 (-0.50%)</td><td>637.08 <b>(+55.92%)</b></td><td>733.02 (+0.50%)</td><td>726.61 (+0.06%)</td><td>726.84 (+0.01%)</td><td>721.00 (-0.10%)</td><td>4.90 <b>(+56.47%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95216.00 (n/a)</td><td>94634.46 (n/a)</td><td>94550.50 (n/a)</td><td>94221.00 (n/a)</td><td>408.60 (n/a)</td><td>729.34 (n/a)</td><td>726.17 (n/a)</td><td>726.80 (n/a)</td><td>721.72 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.32 (-0.21%)</td><td>3.66 (+10.98%)</td><td>4.06 <b>(+48.07%)</b></td><td>2.18 (-2.54%)</td><td>1.37 (+2.60%)</td><td>4091.00 (+2.61%)</td><td>2760.08 (-8.80%)</td><td>2193.60 <b>(-32.47%)</b></td><td>1674.90 (+0.21%)</td><td>1115.41 (+7.61%)</td><td>320.54 (-0.21%)</td><td>220.74 (+10.98%)</td><td>244.74 <b>(+48.07%)</b></td><td>131.23 (-2.54%)</td><td>82.43 (+2.60%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.33 (n/a)</td><td>3.30 (n/a)</td><td>2.74 (n/a)</td><td>2.24 (n/a)</td><td>1.33 (n/a)</td><td>3987.00 (n/a)</td><td>3026.48 (n/a)</td><td>3248.10 (n/a)</td><td>1671.40 (n/a)</td><td>1036.52 (n/a)</td><td>321.21 (n/a)</td><td>198.90 (n/a)</td><td>165.29 (n/a)</td><td>134.65 (n/a)</td><td>80.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>4.89 (+10.32%)</td><td>3.29 (+14.99%)</td><td>2.30 (-19.00%)</td><td>2.22 <b>(+21.30%)</b></td><td>1.40 <b>(+42.65%)</b></td><td>4007.70 (-17.56%)</td><td>3099.04 (-8.68%)</td><td>3879.50 <b>(+23.46%)</b></td><td>1821.00 (-9.35%)</td><td>1142.23 (+8.14%)</td><td>294.81 (+10.32%)</td><td>198.10 (+14.99%)</td><td>138.39 (-19.00%)</td><td>133.96 <b>(+21.30%)</b></td><td>84.35 <b>(+42.65%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>4.44 (n/a)</td><td>2.86 (n/a)</td><td>2.84 (n/a)</td><td>1.83 (n/a)</td><td>0.98 (n/a)</td><td>4861.10 (n/a)</td><td>3393.64 (n/a)</td><td>3142.40 (n/a)</td><td>2008.90 (n/a)</td><td>1056.25 (n/a)</td><td>267.25 (n/a)</td><td>172.27 (n/a)</td><td>170.85 (n/a)</td><td>110.44 (n/a)</td><td>59.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.49 (-1.87%)</td><td>3.79 (+10.99%)</td><td>3.53 (+16.97%)</td><td>2.06 (-6.28%)</td><td>1.45 (+6.73%)</td><td>4326.70 (+6.70%)</td><td>2678.10 (-7.99%)</td><td>2526.10 (-14.51%)</td><td>1623.50 (+1.91%)</td><td>1108.02 (+12.89%)</td><td>330.69 (-1.87%)</td><td>228.41 (+10.99%)</td><td>212.53 (+16.97%)</td><td>124.08 (-6.28%)</td><td>87.63 (+6.73%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.59 (n/a)</td><td>3.42 (n/a)</td><td>3.02 (n/a)</td><td>2.20 (n/a)</td><td>1.36 (n/a)</td><td>4055.10 (n/a)</td><td>2910.68 (n/a)</td><td>2954.70 (n/a)</td><td>1593.10 (n/a)</td><td>981.51 (n/a)</td><td>337.00 (n/a)</td><td>205.80 (n/a)</td><td>181.70 (n/a)</td><td>132.39 (n/a)</td><td>82.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.50 (-4.35%)</td><td>5.19 (-16.19%)</td><td>4.85 <b>(-26.68%)</b></td><td>4.52 (+1.58%)</td><td>0.78 <b>(-20.95%)</b></td><td>7707.70 (-1.56%)</td><td>6818.98 (+18.15%)</td><td>7194.00 <b>(+36.39%)</b></td><td>5361.70 (+4.55%)</td><td>901.08 <b>(-21.97%)</b></td><td>400.52 (-4.35%)</td><td>319.97 (-16.19%)</td><td>298.51 <b>(-26.68%)</b></td><td>278.61 (+1.58%)</td><td>47.88 <b>(-20.95%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.80 (n/a)</td><td>6.20 (n/a)</td><td>6.61 (n/a)</td><td>4.45 (n/a)</td><td>0.98 (n/a)</td><td>7829.50 (n/a)</td><td>5771.24 (n/a)</td><td>5274.70 (n/a)</td><td>5128.50 (n/a)</td><td>1154.74 (n/a)</td><td>418.74 (n/a)</td><td>381.79 (n/a)</td><td>407.13 (n/a)</td><td>274.28 (n/a)</td><td>60.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.42 (-1.86%)</td><td>4.69 (-0.44%)</td><td>4.72 (+4.62%)</td><td>3.75 (-8.03%)</td><td>0.63 (+14.30%)</td><td>9292.60 (+8.73%)</td><td>7553.58 (+0.95%)</td><td>7382.10 (-4.41%)</td><td>6435.80 (+1.90%)</td><td>1099.09 <b>(+29.08%)</b></td><td>333.68 (-1.86%)</td><td>288.81 (-0.44%)</td><td>290.90 (+4.62%)</td><td>231.10 (-8.03%)</td><td>39.04 (+14.30%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.52 (n/a)</td><td>4.71 (n/a)</td><td>4.51 (n/a)</td><td>4.08 (n/a)</td><td>0.55 (n/a)</td><td>8546.30 (n/a)</td><td>7482.86 (n/a)</td><td>7723.00 (n/a)</td><td>6316.00 (n/a)</td><td>851.49 (n/a)</td><td>340.01 (n/a)</td><td>290.08 (n/a)</td><td>278.06 (n/a)</td><td>251.28 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.72 (+5.45%)</td><td>5.65 (+6.02%)</td><td>5.72 (+10.27%)</td><td>4.35 (-4.94%)</td><td>0.86 (+15.42%)</td><td>8016.40 (+5.20%)</td><td>6293.86 (-5.18%)</td><td>6099.50 (-9.32%)</td><td>5190.40 (-5.17%)</td><td>1054.64 (+17.49%)</td><td>413.74 (+5.45%)</td><td>348.25 (+6.02%)</td><td>352.07 (+10.27%)</td><td>267.89 (-4.94%)</td><td>53.11 (+15.42%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.37 (n/a)</td><td>5.33 (n/a)</td><td>5.18 (n/a)</td><td>4.58 (n/a)</td><td>0.75 (n/a)</td><td>7620.00 (n/a)</td><td>6637.90 (n/a)</td><td>6726.20 (n/a)</td><td>5473.40 (n/a)</td><td>897.63 (n/a)</td><td>392.35 (n/a)</td><td>328.48 (n/a)</td><td>319.27 (n/a)</td><td>281.82 (n/a)</td><td>46.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.78 (-1.64%)</td><td>0.77 (+0.12%)</td><td>0.77 (-0.32%)</td><td>0.77 (+3.96%)</td><td>0.00 <b>(-80.87%)</b></td><td>98410.20 (-3.81%)</td><td>97928.78 (-0.16%)</td><td>98001.90 (+0.32%)</td><td>97354.80 (+1.67%)</td><td>465.25 <b>(-81.39%)</b></td><td>705.87 (-1.64%)</td><td>701.74 (+0.12%)</td><td>701.21 (-0.32%)</td><td>698.30 (+3.96%)</td><td>3.34 <b>(-80.87%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102303.00 (n/a)</td><td>98090.16 (n/a)</td><td>97688.30 (n/a)</td><td>95758.00 (n/a)</td><td>2499.69 (n/a)</td><td>717.64 (n/a)</td><td>700.93 (n/a)</td><td>703.46 (n/a)</td><td>671.73 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.78 (+1.56%)</td><td>0.76 (+2.15%)</td><td>0.76 (+0.36%)</td><td>0.75 (+5.69%)</td><td>0.01 <b>(-45.25%)</b></td><td>100884.70 (-5.38%)</td><td>99326.82 (-2.15%)</td><td>99926.70 (-0.36%)</td><td>97131.20 (-1.53%)</td><td>1557.76 <b>(-49.28%)</b></td><td>707.49 (+1.56%)</td><td>691.99 (+2.15%)</td><td>687.70 (+0.36%)</td><td>681.17 (+5.69%)</td><td>10.93 <b>(-45.25%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.02 (n/a)</td><td>106622.20 (n/a)</td><td>101511.48 (n/a)</td><td>100285.30 (n/a)</td><td>98644.80 (n/a)</td><td>3071.14 (n/a)</td><td>696.64 (n/a)</td><td>677.45 (n/a)</td><td>685.24 (n/a)</td><td>644.51 (n/a)</td><td>19.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.81 (-0.05%)</td><td>0.80 (-0.80%)</td><td>0.81 (-0.50%)</td><td>0.78 (-1.93%)</td><td>0.01 <b>(+95.85%)</b></td><td>96276.60 (+1.97%)</td><td>94308.80 (+0.82%)</td><td>93760.40 (+0.50%)</td><td>92872.70 (+0.05%)</td><td>1414.04 <b>(+99.83%)</b></td><td>739.93 (-0.05%)</td><td>728.79 (-0.80%)</td><td>732.93 (-0.50%)</td><td>713.77 (-1.93%)</td><td>10.86 <b>(+95.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94416.60 (n/a)</td><td>93540.50 (n/a)</td><td>93290.70 (n/a)</td><td>92828.30 (n/a)</td><td>707.62 (n/a)</td><td>740.29 (n/a)</td><td>734.68 (n/a)</td><td>736.62 (n/a)</td><td>727.83 (n/a)</td><td>5.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.89 (+18.00%)</td><td>2.71 <b>(+25.31%)</b></td><td>2.72 <b>(+31.24%)</b></td><td>1.36 <b>(+23.56%)</b></td><td>1.00 <b>(+26.68%)</b></td><td>5946.90 (-19.07%)</td><td>3406.18 (-19.38%)</td><td>2959.90 <b>(-23.81%)</b></td><td>2071.30 (-15.25%)</td><td>1548.68 (-16.30%)</td><td>1020.56 (+18.00%)</td><td>711.35 <b>(+25.31%)</b></td><td>714.18 <b>(+31.24%)</b></td><td>355.47 <b>(+23.56%)</b></td><td>261.84 <b>(+26.68%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.30 (n/a)</td><td>2.16 (n/a)</td><td>2.08 (n/a)</td><td>1.10 (n/a)</td><td>0.79 (n/a)</td><td>7348.10 (n/a)</td><td>4225.00 (n/a)</td><td>3884.70 (n/a)</td><td>2444.10 (n/a)</td><td>1850.38 (n/a)</td><td>864.90 (n/a)</td><td>567.66 (n/a)</td><td>544.17 (n/a)</td><td>287.69 (n/a)</td><td>206.69 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.30 <b>(+40.40%)</b></td><td>0.21 (+7.10%)</td><td>0.21 (+7.14%)</td><td>0.14 (-0.32%)</td><td>0.06 <b>(+118.78%)</b></td><td>8659.40 (+0.33%)</td><td>6449.86 (-2.12%)</td><td>5830.30 (-6.66%)</td><td>4180.40 <b>(-28.78%)</b></td><td>1824.69 <b>(+57.47%)</b></td><td>16.05 <b>(+40.40%)</b></td><td>11.13 (+7.10%)</td><td>11.51 (+7.14%)</td><td>7.75 (-0.32%)</td><td>3.30 <b>(+118.78%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>8631.30 (n/a)</td><td>6589.36 (n/a)</td><td>6246.60 (n/a)</td><td>5869.30 (n/a)</td><td>1158.78 (n/a)</td><td>11.43 (n/a)</td><td>10.40 (n/a)</td><td>10.74 (n/a)</td><td>7.78 (n/a)</td><td>1.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.81 (n/a)</td><td>3.65 (n/a)</td><td>3.64 (n/a)</td><td>3.41 (n/a)</td><td>0.16 (n/a)</td><td>3.81 (n/a)</td><td>3.64 (n/a)</td><td>3.64 (n/a)</td><td>3.41 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.82 (-6.86%)</td><td>6.10 (-5.36%)</td><td>5.85 (-11.09%)</td><td>5.71 (+13.22%)</td><td>0.46 <b>(-45.50%)</b></td><td>6.81 (-6.86%)</td><td>6.10 (-5.36%)</td><td>5.85 (-11.09%)</td><td>5.70 (+13.22%)</td><td>0.46 <b>(-45.50%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>7.32 (n/a)</td><td>6.45 (n/a)</td><td>6.58 (n/a)</td><td>5.04 (n/a)</td><td>0.85 (n/a)</td><td>7.32 (n/a)</td><td>6.44 (n/a)</td><td>6.58 (n/a)</td><td>5.04 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>12.08 (-15.72%)</td><td>9.44 (-0.94%)</td><td>8.48 (+2.51%)</td><td>8.26 (+11.28%)</td><td>1.62 <b>(-41.77%)</b></td><td>12.07 (-15.72%)</td><td>9.43 (-0.94%)</td><td>8.47 (+2.51%)</td><td>8.25 (+11.28%)</td><td>1.61 <b>(-41.77%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>14.33 (n/a)</td><td>9.53 (n/a)</td><td>8.27 (n/a)</td><td>7.42 (n/a)</td><td>2.77 (n/a)</td><td>14.32 (n/a)</td><td>9.52 (n/a)</td><td>8.27 (n/a)</td><td>7.41 (n/a)</td><td>2.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.73 (n/a)</td><td>3.59 (n/a)</td><td>3.59 (n/a)</td><td>3.39 (n/a)</td><td>0.14 (n/a)</td><td>3.73 (n/a)</td><td>3.58 (n/a)</td><td>3.59 (n/a)</td><td>3.39 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.84 (-2.10%)</td><td>5.58 (-8.02%)</td><td>5.65 (-2.44%)</td><td>4.32 <b>(-22.84%)</b></td><td>0.91 <b>(+64.17%)</b></td><td>6.83 (-2.10%)</td><td>5.58 (-8.02%)</td><td>5.65 (-2.44%)</td><td>4.32 <b>(-22.84%)</b></td><td>0.91 <b>(+64.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.98 (n/a)</td><td>6.07 (n/a)</td><td>5.79 (n/a)</td><td>5.60 (n/a)</td><td>0.56 (n/a)</td><td>6.98 (n/a)</td><td>6.07 (n/a)</td><td>5.79 (n/a)</td><td>5.60 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>13.47 <b>(+42.04%)</b></td><td>9.27 (+11.79%)</td><td>8.42 (+0.86%)</td><td>7.75 (+10.33%)</td><td>2.36 <b>(+146.22%)</b></td><td>13.46 <b>(+42.04%)</b></td><td>9.26 (+11.79%)</td><td>8.42 (+0.86%)</td><td>7.74 (+10.33%)</td><td>2.36 <b>(+146.22%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.48 (n/a)</td><td>8.29 (n/a)</td><td>8.35 (n/a)</td><td>7.02 (n/a)</td><td>0.96 (n/a)</td><td>9.48 (n/a)</td><td>8.29 (n/a)</td><td>8.34 (n/a)</td><td>7.02 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.19 (+4.01%)</td><td>2.47 <b>(+52.65%)</b></td><td>2.72 <b>(+129.16%)</b></td><td>0.94 (-9.07%)</td><td>0.89 (+2.74%)</td><td>3.18 (+4.01%)</td><td>2.47 <b>(+52.65%)</b></td><td>2.71 <b>(+129.16%)</b></td><td>0.93 (-9.07%)</td><td>0.89 (+2.74%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.06 (n/a)</td><td>1.62 (n/a)</td><td>1.19 (n/a)</td><td>1.03 (n/a)</td><td>0.87 (n/a)</td><td>3.06 (n/a)</td><td>1.62 (n/a)</td><td>1.18 (n/a)</td><td>1.03 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.57 (-1.36%)</td><td>0.45 <b>(+20.03%)</b></td><td>0.42 (+17.87%)</td><td>0.38 <b>(+383.17%)</b></td><td>0.08 <b>(-59.40%)</b></td><td>0.56 (-1.36%)</td><td>0.45 <b>(+20.03%)</b></td><td>0.42 (+17.87%)</td><td>0.37 <b>(+383.17%)</b></td><td>0.08 <b>(-59.40%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.57 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.62 (-12.00%)</td><td>0.30 <b>(-42.38%)</b></td><td>0.35 <b>(-26.35%)</b></td><td>0.08 <b>(-74.61%)</b></td><td>0.23 <b>(+26.09%)</b></td><td>0.62 (-12.00%)</td><td>0.29 <b>(-42.38%)</b></td><td>0.34 <b>(-26.35%)</b></td><td>0.08 <b>(-74.61%)</b></td><td>0.22 <b>(+26.09%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.71 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>0.70 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.90 <b>(-28.11%)</b></td><td>1.33 <b>(-30.84%)</b></td><td>1.71 <b>(-26.30%)</b></td><td>0.45 (+5.59%)</td><td>0.65 <b>(-27.23%)</b></td><td>1.87 <b>(-28.11%)</b></td><td>1.31 <b>(-30.84%)</b></td><td>1.69 <b>(-26.30%)</b></td><td>0.44 (+5.59%)</td><td>0.64 <b>(-27.23%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.65 (n/a)</td><td>1.93 (n/a)</td><td>2.33 (n/a)</td><td>0.43 (n/a)</td><td>0.90 (n/a)</td><td>2.60 (n/a)</td><td>1.89 (n/a)</td><td>2.29 (n/a)</td><td>0.42 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.00 (n/a)</td><td>402.52 (n/a)</td><td>481.60 (n/a)</td><td>212.80 (n/a)</td><td>167.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.80 (n/a)</td><td>423.92 (n/a)</td><td>488.80 (n/a)</td><td>193.50 (n/a)</td><td>190.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.40 (n/a)</td><td>474.94 (n/a)</td><td>451.30 (n/a)</td><td>361.60 (n/a)</td><td>94.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.70 (n/a)</td><td>443.46 (n/a)</td><td>492.60 (n/a)</td><td>238.80 (n/a)</td><td>116.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.70 (n/a)</td><td>372.24 (n/a)</td><td>321.00 (n/a)</td><td>230.90 (n/a)</td><td>152.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1906.90 (n/a)</td><td>755.38 (n/a)</td><td>565.90 (n/a)</td><td>239.30 (n/a)</td><td>658.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.00 (n/a)</td><td>434.94 (n/a)</td><td>411.20 (n/a)</td><td>287.00 (n/a)</td><td>151.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1930.70 (n/a)</td><td>781.82 (n/a)</td><td>555.90 (n/a)</td><td>264.60 (n/a)</td><td>656.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>521.70 (n/a)</td><td>357.00 (n/a)</td><td>321.50 (n/a)</td><td>293.10 (n/a)</td><td>93.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2024.00 (n/a)</td><td>843.94 (n/a)</td><td>672.90 (n/a)</td><td>235.80 (n/a)</td><td>689.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.80 (n/a)</td><td>374.46 (n/a)</td><td>302.70 (n/a)</td><td>230.80 (n/a)</td><td>145.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.90 (n/a)</td><td>387.96 (n/a)</td><td>376.00 (n/a)</td><td>233.40 (n/a)</td><td>110.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1903.50 (n/a)</td><td>694.22 (n/a)</td><td>387.80 (n/a)</td><td>230.20 (n/a)</td><td>689.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>468.40 (n/a)</td><td>374.86 (n/a)</td><td>433.30 (n/a)</td><td>238.70 (n/a)</td><td>103.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.00 (n/a)</td><td>370.20 (n/a)</td><td>302.40 (n/a)</td><td>240.80 (n/a)</td><td>154.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>768.30 (n/a)</td><td>418.20 (n/a)</td><td>387.60 (n/a)</td><td>228.10 (n/a)</td><td>208.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1893.20 (n/a)</td><td>647.86 (n/a)</td><td>423.10 (n/a)</td><td>170.80 (n/a)</td><td>707.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.40 (n/a)</td><td>425.58 (n/a)</td><td>456.30 (n/a)</td><td>225.90 (n/a)</td><td>131.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2460.30 (n/a)</td><td>1080.36 (n/a)</td><td>482.90 (n/a)</td><td>297.40 (n/a)</td><td>993.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>858.50 (n/a)</td><td>482.76 (n/a)</td><td>478.70 (n/a)</td><td>277.20 (n/a)</td><td>232.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>623.30 (n/a)</td><td>414.20 (n/a)</td><td>312.30 (n/a)</td><td>274.20 (n/a)</td><td>160.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>531.70 (n/a)</td><td>406.38 (n/a)</td><td>372.50 (n/a)</td><td>279.10 (n/a)</td><td>108.22 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.50 (n/a)</td><td>412.94 (n/a)</td><td>487.90 (n/a)</td><td>230.10 (n/a)</td><td>130.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>530.30 (n/a)</td><td>409.76 (n/a)</td><td>394.80 (n/a)</td><td>238.40 (n/a)</td><td>113.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(+45.17%)</b></td><td>0.02 <b>(+45.82%)</b></td><td>0.02 <b>(+65.36%)</b></td><td>0.01 <b>(+37.45%)</b></td><td>0.00 <b>(+66.40%)</b></td><td>420.40 <b>(-27.24%)</b></td><td>296.58 <b>(-29.63%)</b></td><td>247.20 <b>(-39.52%)</b></td><td>199.50 <b>(-31.11%)</b></td><td>98.86 (-13.55%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.80 (n/a)</td><td>421.46 (n/a)</td><td>408.70 (n/a)</td><td>289.60 (n/a)</td><td>114.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+5.84%)</td><td>0.01 (+17.75%)</td><td>0.01 (+9.79%)</td><td>0.01 (+0.69%)</td><td>0.00 <b>(+24.03%)</b></td><td>516.90 (-0.67%)</td><td>358.98 (-12.81%)</td><td>401.10 (-8.90%)</td><td>232.20 (-5.53%)</td><td>120.94 (+11.63%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.40 (n/a)</td><td>411.74 (n/a)</td><td>440.30 (n/a)</td><td>245.80 (n/a)</td><td>108.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+14.41%)</td><td>0.02 <b>(+27.21%)</b></td><td>0.02 <b>(+45.42%)</b></td><td>0.01 (-3.71%)</td><td>0.00 <b>(+35.06%)</b></td><td>454.20 (+3.84%)</td><td>286.82 (-19.41%)</td><td>246.30 <b>(-31.24%)</b></td><td>235.50 (-12.58%)</td><td>94.04 <b>(+24.72%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>437.40 (n/a)</td><td>355.88 (n/a)</td><td>358.20 (n/a)</td><td>269.40 (n/a)</td><td>75.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+18.85%)</td><td>0.01 <b>(+30.51%)</b></td><td>0.01 <b>(+33.12%)</b></td><td>0.01 <b>(+27.92%)</b></td><td>0.00 (+11.10%)</td><td>472.70 <b>(-21.82%)</b></td><td>361.42 <b>(-24.32%)</b></td><td>375.10 <b>(-24.87%)</b></td><td>245.00 (-15.87%)</td><td>92.38 <b>(-26.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.60 (n/a)</td><td>477.58 (n/a)</td><td>499.30 (n/a)</td><td>291.20 (n/a)</td><td>126.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-0.11%)</td><td>0.01 (+14.01%)</td><td>0.01 (+17.40%)</td><td>0.01 (+10.27%)</td><td>0.00 (-14.84%)</td><td>475.30 (-9.31%)</td><td>310.78 (-15.01%)</td><td>286.90 (-14.82%)</td><td>229.60 (+0.09%)</td><td>97.83 <b>(-22.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.10 (n/a)</td><td>365.68 (n/a)</td><td>336.80 (n/a)</td><td>229.40 (n/a)</td><td>125.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (+12.09%)</td><td>0.01 (-2.02%)</td><td>0.01 (+16.94%)</td><td>0.00 <b>(-74.70%)</b></td><td>0.00 <b>(+155.27%)</b></td><td>2119.70 <b>(+295.32%)</b></td><td>762.54 <b>(+60.85%)</b></td><td>445.00 (-14.49%)</td><td>308.90 (-10.80%)</td><td>768.06 <b>(+826.49%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.20 (n/a)</td><td>474.08 (n/a)</td><td>520.40 (n/a)</td><td>346.30 (n/a)</td><td>82.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 <b>(-20.31%)</b></td><td>0.03 (+12.44%)</td><td>0.03 <b>(+55.62%)</b></td><td>0.01 (-17.16%)</td><td>0.01 (-19.30%)</td><td>548.70 <b>(+20.73%)</b></td><td>336.84 (-11.21%)</td><td>260.60 <b>(-35.73%)</b></td><td>235.60 <b>(+25.45%)</b></td><td>135.64 <b>(+23.10%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>454.50 (n/a)</td><td>379.36 (n/a)</td><td>405.50 (n/a)</td><td>187.80 (n/a)</td><td>110.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (+0.30%)</td><td>0.03 (-3.76%)</td><td>0.03 (+8.11%)</td><td>0.02 (-15.92%)</td><td>0.01 <b>(+40.06%)</b></td><td>526.80 (+18.94%)</td><td>351.86 (+9.61%)</td><td>295.50 (-7.51%)</td><td>239.30 (-0.29%)</td><td>126.69 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>442.90 (n/a)</td><td>321.02 (n/a)</td><td>319.50 (n/a)</td><td>240.00 (n/a)</td><td>77.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+48.76%)</b></td><td>0.03 <b>(+36.37%)</b></td><td>0.03 <b>(+44.37%)</b></td><td>0.02 (-0.57%)</td><td>0.01 <b>(+96.88%)</b></td><td>524.40 (+0.56%)</td><td>318.52 <b>(-21.66%)</b></td><td>262.80 <b>(-30.73%)</b></td><td>199.20 <b>(-32.77%)</b></td><td>128.34 <b>(+33.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>521.50 (n/a)</td><td>406.58 (n/a)</td><td>379.40 (n/a)</td><td>296.30 (n/a)</td><td>95.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+38.12%)</b></td><td>0.03 <b>(+39.37%)</b></td><td>0.03 <b>(+83.32%)</b></td><td>0.02 <b>(+42.18%)</b></td><td>0.01 (+19.25%)</td><td>431.30 <b>(-29.66%)</b></td><td>336.74 <b>(-29.66%)</b></td><td>301.30 <b>(-45.46%)</b></td><td>221.50 <b>(-27.59%)</b></td><td>91.10 <b>(-36.02%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.20 (n/a)</td><td>478.74 (n/a)</td><td>552.40 (n/a)</td><td>305.90 (n/a)</td><td>142.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(-37.95%)</b></td><td>0.02 <b>(-23.57%)</b></td><td>0.02 (-15.87%)</td><td>0.01 <b>(+79.30%)</b></td><td>0.00 <b>(-58.12%)</b></td><td>1058.40 <b>(-44.22%)</b></td><td>593.62 (-12.92%)</td><td>478.40 (+18.86%)</td><td>396.70 <b>(+61.19%)</b></td><td>267.59 <b>(-61.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1897.60 (n/a)</td><td>681.68 (n/a)</td><td>402.50 (n/a)</td><td>246.10 (n/a)</td><td>692.67 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 <b>(-31.27%)</b></td><td>0.02 (-6.42%)</td><td>0.03 <b>(+33.46%)</b></td><td>0.02 (+6.80%)</td><td>0.01 <b>(-40.52%)</b></td><td>534.10 (-6.36%)</td><td>391.98 (+0.27%)</td><td>313.70 <b>(-25.08%)</b></td><td>290.70 <b>(+45.50%)</b></td><td>123.63 (-15.82%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.40 (n/a)</td><td>390.94 (n/a)</td><td>418.70 (n/a)</td><td>199.80 (n/a)</td><td>146.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+35.59%)</b></td><td>0.02 (+1.30%)</td><td>0.02 (-18.47%)</td><td>0.01 (-9.17%)</td><td>0.01 <b>(+39.21%)</b></td><td>656.30 (+10.10%)</td><td>413.24 (+4.59%)</td><td>368.20 <b>(+22.65%)</b></td><td>194.40 <b>(-26.25%)</b></td><td>186.25 (+14.87%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.10 (n/a)</td><td>395.10 (n/a)</td><td>300.20 (n/a)</td><td>263.60 (n/a)</td><td>162.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (-2.85%)</td><td>0.02 (+17.47%)</td><td>0.02 <b>(+36.83%)</b></td><td>0.02 <b>(+24.72%)</b></td><td>0.00 <b>(-32.99%)</b></td><td>505.90 (-19.81%)</td><td>383.08 (-19.44%)</td><td>389.80 <b>(-26.92%)</b></td><td>301.50 (+2.94%)</td><td>80.91 <b>(-44.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.90 (n/a)</td><td>475.54 (n/a)</td><td>533.40 (n/a)</td><td>292.90 (n/a)</td><td>146.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (-6.61%)</td><td>0.04 (-12.44%)</td><td>0.04 <b>(-25.38%)</b></td><td>0.01 <b>(-78.17%)</b></td><td>0.02 <b>(+51.55%)</b></td><td>2441.40 <b>(+358.05%)</b></td><td>760.64 <b>(+108.23%)</b></td><td>428.90 <b>(+33.99%)</b></td><td>241.90 (+7.08%)</td><td>944.31 <b>(+663.99%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.00 (n/a)</td><td>365.28 (n/a)</td><td>320.10 (n/a)</td><td>225.90 (n/a)</td><td>123.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(+46.44%)</b></td><td>0.06 <b>(+88.28%)</b></td><td>0.06 <b>(+126.91%)</b></td><td>0.03 <b>(+61.84%)</b></td><td>0.01 <b>(+37.53%)</b></td><td>502.10 <b>(-38.21%)</b></td><td>309.02 <b>(-47.27%)</b></td><td>269.50 <b>(-55.94%)</b></td><td>239.00 <b>(-31.71%)</b></td><td>108.71 <b>(-36.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>812.60 (n/a)</td><td>586.00 (n/a)</td><td>611.60 (n/a)</td><td>350.00 (n/a)</td><td>170.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(+24.65%)</b></td><td>0.04 (+18.55%)</td><td>0.03 (-12.56%)</td><td>0.01 (-18.62%)</td><td>0.03 (+10.97%)</td><td>2397.10 <b>(+22.87%)</b></td><td>785.60 (-18.81%)</td><td>471.60 (+14.35%)</td><td>194.30 (-19.78%)</td><td>914.82 (+2.11%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1950.90 (n/a)</td><td>967.64 (n/a)</td><td>412.40 (n/a)</td><td>242.20 (n/a)</td><td>895.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (+4.59%)</td><td>0.04 (-4.34%)</td><td>0.03 (-3.02%)</td><td>0.01 <b>(-67.77%)</b></td><td>0.02 <b>(+59.80%)</b></td><td>1848.90 <b>(+210.22%)</b></td><td>698.64 <b>(+55.21%)</b></td><td>489.10 (+3.12%)</td><td>248.10 (-4.39%)</td><td>657.45 <b>(+434.26%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>596.00 (n/a)</td><td>450.14 (n/a)</td><td>474.30 (n/a)</td><td>259.50 (n/a)</td><td>123.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(+40.69%)</b></td><td>0.05 <b>(+59.51%)</b></td><td>0.07 <b>(+55.99%)</b></td><td>0.03 <b>(+243.57%)</b></td><td>0.02 (+16.15%)</td><td>573.30 <b>(-70.90%)</b></td><td>344.36 <b>(-53.31%)</b></td><td>249.10 <b>(-35.90%)</b></td><td>222.10 <b>(-28.93%)</b></td><td>154.10 <b>(-77.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1969.80 (n/a)</td><td>737.60 (n/a)</td><td>388.60 (n/a)</td><td>312.50 (n/a)</td><td>699.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(+28.95%)</b></td><td>0.05 (+16.34%)</td><td>0.04 (+6.28%)</td><td>0.03 (+14.39%)</td><td>0.02 <b>(+37.94%)</b></td><td>506.30 (-12.59%)</td><td>393.92 (-12.09%)</td><td>452.10 (-5.91%)</td><td>216.70 <b>(-22.47%)</b></td><td>126.84 (-6.46%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>579.20 (n/a)</td><td>448.12 (n/a)</td><td>480.50 (n/a)</td><td>279.50 (n/a)</td><td>135.59 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 <b>(+37.28%)</b></td><td>0.11 <b>(+57.85%)</b></td><td>0.11 <b>(+82.64%)</b></td><td>0.07 <b>(+33.96%)</b></td><td>0.03 <b>(+57.56%)</b></td><td>440.40 <b>(-25.36%)</b></td><td>323.36 <b>(-35.51%)</b></td><td>299.80 <b>(-45.25%)</b></td><td>232.10 <b>(-27.15%)</b></td><td>95.89 (-13.87%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>590.00 (n/a)</td><td>501.38 (n/a)</td><td>547.60 (n/a)</td><td>318.60 (n/a)</td><td>111.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.17 <b>(+43.47%)</b></td><td>0.14 <b>(+74.65%)</b></td><td>0.13 <b>(+97.35%)</b></td><td>0.11 <b>(+111.86%)</b></td><td>0.03 <b>(-20.25%)</b></td><td>307.40 <b>(-52.79%)</b></td><td>238.64 <b>(-48.29%)</b></td><td>247.30 <b>(-49.32%)</b></td><td>193.30 <b>(-30.29%)</b></td><td>46.68 <b>(-73.38%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>651.20 (n/a)</td><td>461.46 (n/a)</td><td>488.00 (n/a)</td><td>277.30 (n/a)</td><td>175.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 <b>(+107.72%)</b></td><td>0.09 <b>(+50.84%)</b></td><td>0.09 <b>(+27.87%)</b></td><td>0.02 <b>(-47.02%)</b></td><td>0.06 <b>(+224.82%)</b></td><td>1928.50 <b>(+88.77%)</b></td><td>652.14 (+11.04%)</td><td>366.50 <b>(-21.80%)</b></td><td>210.90 <b>(-51.87%)</b></td><td>724.03 <b>(+194.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1021.60 (n/a)</td><td>587.28 (n/a)</td><td>468.70 (n/a)</td><td>438.20 (n/a)</td><td>246.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (-0.81%)</td><td>0.07 <b>(-26.99%)</b></td><td>0.06 <b>(-21.17%)</b></td><td>0.02 <b>(-69.18%)</b></td><td>0.06 <b>(+27.70%)</b></td><td>1983.30 <b>(+224.49%)</b></td><td>829.02 <b>(+109.97%)</b></td><td>515.00 <b>(+26.85%)</b></td><td>200.50 (+0.80%)</td><td>714.74 <b>(+335.81%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>611.20 (n/a)</td><td>394.82 (n/a)</td><td>406.00 (n/a)</td><td>198.90 (n/a)</td><td>164.00 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (-1.93%)</td><td>0.08 (+4.17%)</td><td>0.06 (-8.08%)</td><td>0.05 <b>(+112.95%)</b></td><td>0.03 (-17.93%)</td><td>616.00 <b>(-53.05%)</b></td><td>471.94 <b>(-20.54%)</b></td><td>534.00 (+8.80%)</td><td>245.00 (+1.96%)</td><td>153.68 <b>(-63.23%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1311.90 (n/a)</td><td>593.96 (n/a)</td><td>490.80 (n/a)</td><td>240.30 (n/a)</td><td>417.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(+29.56%)</b></td><td>0.01 (+18.29%)</td><td>0.01 (+14.86%)</td><td>0.01 (+16.59%)</td><td>0.00 <b>(+31.96%)</b></td><td>463.80 (-14.24%)</td><td>349.94 (-14.39%)</td><td>394.10 (-12.94%)</td><td>205.70 <b>(-22.81%)</b></td><td>108.56 (-10.97%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.80 (n/a)</td><td>408.78 (n/a)</td><td>452.70 (n/a)</td><td>266.50 (n/a)</td><td>121.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+17.75%)</td><td>0.01 (+14.02%)</td><td>0.01 (+17.60%)</td><td>0.01 (+3.37%)</td><td>0.00 <b>(+40.60%)</b></td><td>490.70 (-3.27%)</td><td>379.48 (-9.32%)</td><td>414.70 (-14.97%)</td><td>248.10 (-15.06%)</td><td>121.30 (+13.24%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.30 (n/a)</td><td>418.50 (n/a)</td><td>487.70 (n/a)</td><td>292.10 (n/a)</td><td>107.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 <b>(+91.73%)</b></td><td>0.02 <b>(+46.11%)</b></td><td>0.01 <b>(+64.31%)</b></td><td>0.01 <b>(+38.23%)</b></td><td>0.01 <b>(+112.90%)</b></td><td>430.00 <b>(-27.67%)</b></td><td>313.46 <b>(-27.06%)</b></td><td>291.30 <b>(-39.15%)</b></td><td>146.50 <b>(-47.83%)</b></td><td>118.58 (-13.27%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.50 (n/a)</td><td>429.74 (n/a)</td><td>478.70 (n/a)</td><td>280.80 (n/a)</td><td>136.73 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-7.64%)</td><td>0.01 (-6.45%)</td><td>0.01 (-7.72%)</td><td>0.01 (+14.26%)</td><td>0.00 (-18.91%)</td><td>443.00 (-12.47%)</td><td>334.12 (+4.09%)</td><td>313.10 (+8.34%)</td><td>268.90 (+8.25%)</td><td>74.80 <b>(-28.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.10 (n/a)</td><td>320.98 (n/a)</td><td>289.00 (n/a)</td><td>248.40 (n/a)</td><td>105.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(+20.94%)</b></td><td>0.01 (+6.90%)</td><td>0.01 (+7.02%)</td><td>0.01 (+10.32%)</td><td>0.01 <b>(+25.39%)</b></td><td>519.30 (-9.36%)</td><td>385.88 (-3.70%)</td><td>426.00 (-6.56%)</td><td>197.30 (-17.31%)</td><td>145.86 (+2.22%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.90 (n/a)</td><td>400.70 (n/a)</td><td>455.90 (n/a)</td><td>238.60 (n/a)</td><td>142.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+0.60%)</td><td>0.01 (+1.81%)</td><td>0.01 (-2.87%)</td><td>0.01 <b>(+38.98%)</b></td><td>0.00 <b>(-31.50%)</b></td><td>418.10 <b>(-28.04%)</b></td><td>301.08 (-8.17%)</td><td>277.50 (+2.93%)</td><td>240.40 (-0.62%)</td><td>68.44 <b>(-51.88%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.00 (n/a)</td><td>327.88 (n/a)</td><td>269.60 (n/a)</td><td>241.90 (n/a)</td><td>142.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(+73.60%)</b></td><td>0.02 <b>(+128.74%)</b></td><td>0.02 <b>(+127.06%)</b></td><td>0.01 <b>(+463.48%)</b></td><td>0.00 (+6.75%)</td><td>437.50 <b>(-82.25%)</b></td><td>284.12 <b>(-69.20%)</b></td><td>251.50 <b>(-55.95%)</b></td><td>224.60 <b>(-42.40%)</b></td><td>86.97 <b>(-89.98%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2465.00 (n/a)</td><td>922.50 (n/a)</td><td>571.00 (n/a)</td><td>389.90 (n/a)</td><td>867.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (+11.09%)</td><td>0.01 (-9.08%)</td><td>0.01 <b>(+28.93%)</b></td><td>0.00 <b>(-67.21%)</b></td><td>0.01 <b>(+118.11%)</b></td><td>1914.40 <b>(+204.94%)</b></td><td>935.66 <b>(+117.84%)</b></td><td>319.60 <b>(-22.43%)</b></td><td>275.20 (-10.01%)</td><td>883.36 <b>(+550.43%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.80 (n/a)</td><td>429.52 (n/a)</td><td>412.00 (n/a)</td><td>305.80 (n/a)</td><td>135.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (+3.50%)</td><td>0.01 (+10.72%)</td><td>0.01 (+8.98%)</td><td>0.01 <b>(-20.42%)</b></td><td>0.00 <b>(+36.15%)</b></td><td>779.00 <b>(+25.67%)</b></td><td>457.30 (-2.54%)</td><td>423.30 (-8.24%)</td><td>276.90 (-3.38%)</td><td>203.98 <b>(+67.92%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.90 (n/a)</td><td>469.20 (n/a)</td><td>461.30 (n/a)</td><td>286.60 (n/a)</td><td>121.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 <b>(+50.20%)</b></td><td>0.01 <b>(+40.57%)</b></td><td>0.01 <b>(+38.57%)</b></td><td>0.01 (+9.44%)</td><td>0.00 <b>(+144.34%)</b></td><td>569.10 (-8.62%)</td><td>386.64 <b>(-25.51%)</b></td><td>384.00 <b>(-27.83%)</b></td><td>284.70 <b>(-33.42%)</b></td><td>116.00 <b>(+45.66%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.80 (n/a)</td><td>519.08 (n/a)</td><td>532.10 (n/a)</td><td>427.60 (n/a)</td><td>79.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(+36.15%)</b></td><td>0.01 <b>(+27.66%)</b></td><td>0.01 (+10.48%)</td><td>0.01 <b>(+36.47%)</b></td><td>0.00 <b>(+33.04%)</b></td><td>437.70 <b>(-26.72%)</b></td><td>365.44 <b>(-21.74%)</b></td><td>406.10 (-9.47%)</td><td>267.90 <b>(-26.54%)</b></td><td>77.28 <b>(-27.02%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.30 (n/a)</td><td>466.98 (n/a)</td><td>448.60 (n/a)</td><td>364.70 (n/a)</td><td>105.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 <b>(+66.21%)</b></td><td>0.01 <b>(+38.67%)</b></td><td>0.01 (+7.57%)</td><td>0.01 <b>(+177.65%)</b></td><td>0.00 <b>(+32.41%)</b></td><td>688.50 <b>(-63.98%)</b></td><td>490.86 <b>(-39.12%)</b></td><td>504.50 (-7.04%)</td><td>282.60 <b>(-39.83%)</b></td><td>161.40 <b>(-73.93%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1911.60 (n/a)</td><td>806.34 (n/a)</td><td>542.70 (n/a)</td><td>469.70 (n/a)</td><td>619.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+51.62%)</b></td><td>0.03 (+15.36%)</td><td>0.02 (-13.21%)</td><td>0.02 (+10.20%)</td><td>0.01 <b>(+104.47%)</b></td><td>515.60 (-9.26%)</td><td>383.90 (-3.67%)</td><td>467.30 (+15.21%)</td><td>191.40 <b>(-34.05%)</b></td><td>155.38 <b>(+34.44%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.20 (n/a)</td><td>398.52 (n/a)</td><td>405.60 (n/a)</td><td>290.20 (n/a)</td><td>115.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (+9.44%)</td><td>0.03 (-7.77%)</td><td>0.03 (+9.14%)</td><td>0.00 <b>(-78.87%)</b></td><td>0.01 <b>(+99.59%)</b></td><td>2067.00 <b>(+373.21%)</b></td><td>649.34 <b>(+105.02%)</b></td><td>262.90 (-8.37%)</td><td>199.80 (-8.64%)</td><td>799.11 <b>(+821.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>436.80 (n/a)</td><td>316.72 (n/a)</td><td>286.90 (n/a)</td><td>218.70 (n/a)</td><td>86.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (+11.75%)</td><td>0.03 <b>(+25.77%)</b></td><td>0.03 <b>(+46.48%)</b></td><td>0.02 (+17.87%)</td><td>0.00 <b>(-20.35%)</b></td><td>392.30 (-15.16%)</td><td>304.30 <b>(-22.10%)</b></td><td>292.50 <b>(-31.74%)</b></td><td>264.00 (-10.54%)</td><td>51.58 <b>(-38.43%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.40 (n/a)</td><td>390.64 (n/a)</td><td>428.50 (n/a)</td><td>295.10 (n/a)</td><td>83.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (-0.99%)</td><td>0.02 (+6.91%)</td><td>0.02 (+13.44%)</td><td>0.02 (+8.41%)</td><td>0.01 (-13.40%)</td><td>488.50 (-7.76%)</td><td>382.74 (-8.48%)</td><td>414.60 (-11.84%)</td><td>278.60 (+0.98%)</td><td>90.18 <b>(-21.62%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.60 (n/a)</td><td>418.22 (n/a)</td><td>470.30 (n/a)</td><td>275.90 (n/a)</td><td>115.05 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (+1.04%)</td><td>0.02 (+3.26%)</td><td>0.02 (+2.56%)</td><td>0.02 (+8.25%)</td><td>0.01 (-6.21%)</td><td>507.50 (-7.63%)</td><td>404.94 (-4.83%)</td><td>479.70 (-2.48%)</td><td>259.80 (-1.07%)</td><td>117.11 (-13.60%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.40 (n/a)</td><td>425.50 (n/a)</td><td>491.90 (n/a)</td><td>262.60 (n/a)</td><td>135.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (+6.76%)</td><td>0.02 (-1.66%)</td><td>0.02 (-7.92%)</td><td>0.01 <b>(-51.06%)</b></td><td>0.01 <b>(+69.24%)</b></td><td>1028.90 <b>(+104.31%)</b></td><td>514.82 <b>(+24.44%)</b></td><td>477.00 (+8.61%)</td><td>244.40 (-6.32%)</td><td>315.30 <b>(+208.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.60 (n/a)</td><td>413.70 (n/a)</td><td>439.20 (n/a)</td><td>260.90 (n/a)</td><td>102.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+53.03%)</b></td><td>0.02 (-10.47%)</td><td>0.02 <b>(-26.50%)</b></td><td>0.01 <b>(-56.49%)</b></td><td>0.01 <b>(+116.22%)</b></td><td>1306.00 <b>(+129.85%)</b></td><td>627.18 <b>(+48.42%)</b></td><td>492.10 <b>(+36.05%)</b></td><td>201.00 <b>(-34.66%)</b></td><td>415.55 <b>(+213.43%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.20 (n/a)</td><td>422.56 (n/a)</td><td>361.70 (n/a)</td><td>307.60 (n/a)</td><td>132.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 <b>(+22.38%)</b></td><td>0.02 <b>(+23.85%)</b></td><td>0.02 (+1.87%)</td><td>0.02 <b>(+41.39%)</b></td><td>0.01 (+13.26%)</td><td>469.60 <b>(-29.28%)</b></td><td>391.64 <b>(-20.37%)</b></td><td>435.70 (-1.83%)</td><td>277.70 (-18.30%)</td><td>83.55 <b>(-35.20%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>664.00 (n/a)</td><td>491.84 (n/a)</td><td>443.80 (n/a)</td><td>339.90 (n/a)</td><td>128.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+62.21%)</b></td><td>0.02 (-6.97%)</td><td>0.01 (-12.19%)</td><td>0.00 <b>(-68.81%)</b></td><td>0.01 <b>(+298.88%)</b></td><td>1904.90 <b>(+220.58%)</b></td><td>915.48 <b>(+79.32%)</b></td><td>618.90 (+13.87%)</td><td>232.70 <b>(-38.34%)</b></td><td>695.39 <b>(+743.16%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.20 (n/a)</td><td>510.54 (n/a)</td><td>543.50 (n/a)</td><td>377.40 (n/a)</td><td>82.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 <b>(+23.43%)</b></td><td>0.03 (+15.84%)</td><td>0.03 (+19.16%)</td><td>0.01 (+8.51%)</td><td>0.01 <b>(+50.41%)</b></td><td>564.70 (-7.85%)</td><td>362.42 (-8.41%)</td><td>255.00 (-16.09%)</td><td>240.60 (-18.96%)</td><td>161.12 (+14.62%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.80 (n/a)</td><td>395.70 (n/a)</td><td>303.90 (n/a)</td><td>296.90 (n/a)</td><td>140.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(-33.52%)</b></td><td>0.02 (-19.44%)</td><td>0.02 <b>(-20.78%)</b></td><td>0.02 (+1.22%)</td><td>0.00 <b>(-53.98%)</b></td><td>544.00 (-1.20%)</td><td>462.66 (+17.94%)</td><td>482.50 <b>(+26.24%)</b></td><td>377.90 <b>(+50.44%)</b></td><td>79.29 <b>(-32.93%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.60 (n/a)</td><td>392.28 (n/a)</td><td>382.20 (n/a)</td><td>251.20 (n/a)</td><td>118.22 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-15.66%)</td><td>0.02 <b>(-29.82%)</b></td><td>0.01 <b>(-43.24%)</b></td><td>0.00 <b>(-71.54%)</b></td><td>0.01 <b>(+23.60%)</b></td><td>1894.80 <b>(+251.41%)</b></td><td>747.32 <b>(+92.84%)</b></td><td>559.90 <b>(+76.18%)</b></td><td>342.10 (+18.58%)</td><td>650.73 <b>(+438.06%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.20 (n/a)</td><td>387.54 (n/a)</td><td>317.80 (n/a)</td><td>288.50 (n/a)</td><td>120.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 <b>(+54.43%)</b></td><td>0.06 <b>(+32.65%)</b></td><td>0.06 <b>(+27.98%)</b></td><td>0.03 (-10.33%)</td><td>0.02 <b>(+87.13%)</b></td><td>553.00 (+11.51%)</td><td>314.30 (-18.76%)</td><td>282.20 <b>(-21.87%)</b></td><td>184.10 <b>(-35.24%)</b></td><td>141.29 <b>(+38.40%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>495.90 (n/a)</td><td>386.88 (n/a)</td><td>361.20 (n/a)</td><td>284.30 (n/a)</td><td>102.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (+18.98%)</td><td>0.05 <b>(+20.52%)</b></td><td>0.04 (-11.81%)</td><td>0.03 <b>(+271.51%)</b></td><td>0.02 (-8.91%)</td><td>484.20 <b>(-73.08%)</b></td><td>367.96 <b>(-42.99%)</b></td><td>427.30 (+13.40%)</td><td>203.30 (-15.92%)</td><td>126.18 <b>(-80.68%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1798.90 (n/a)</td><td>645.44 (n/a)</td><td>376.80 (n/a)</td><td>241.80 (n/a)</td><td>653.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 <b>(-26.78%)</b></td><td>0.04 (-2.50%)</td><td>0.04 (-9.25%)</td><td>0.03 (+16.61%)</td><td>0.01 <b>(-40.13%)</b></td><td>495.40 (-14.25%)</td><td>387.78 (-4.23%)</td><td>436.20 (+10.21%)</td><td>276.00 <b>(+36.57%)</b></td><td>99.64 <b>(-29.30%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.70 (n/a)</td><td>404.90 (n/a)</td><td>395.80 (n/a)</td><td>202.10 (n/a)</td><td>140.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(+20.35%)</b></td><td>0.05 <b>(+28.19%)</b></td><td>0.06 <b>(+37.37%)</b></td><td>0.04 <b>(+31.55%)</b></td><td>0.01 (-1.15%)</td><td>384.70 <b>(-23.97%)</b></td><td>307.42 <b>(-23.03%)</b></td><td>296.70 <b>(-27.23%)</b></td><td>241.40 (-16.93%)</td><td>52.26 <b>(-36.65%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>506.00 (n/a)</td><td>399.40 (n/a)</td><td>407.70 (n/a)</td><td>290.60 (n/a)</td><td>82.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(+26.30%)</b></td><td>0.05 (-1.51%)</td><td>0.04 <b>(-31.77%)</b></td><td>0.03 (-6.78%)</td><td>0.02 <b>(+51.85%)</b></td><td>559.50 (+7.29%)</td><td>399.72 (+7.52%)</td><td>438.10 <b>(+46.57%)</b></td><td>223.90 <b>(-20.83%)</b></td><td>143.52 <b>(+29.79%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>521.50 (n/a)</td><td>371.76 (n/a)</td><td>298.90 (n/a)</td><td>282.80 (n/a)</td><td>110.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (-17.19%)</td><td>0.05 (-0.14%)</td><td>0.05 <b>(+44.21%)</b></td><td>0.03 (-19.90%)</td><td>0.01 <b>(-20.66%)</b></td><td>643.10 <b>(+24.83%)</b></td><td>397.76 (-0.72%)</td><td>320.00 <b>(-30.66%)</b></td><td>270.50 <b>(+20.76%)</b></td><td>154.27 (+16.41%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>515.20 (n/a)</td><td>400.66 (n/a)</td><td>461.50 (n/a)</td><td>224.00 (n/a)</td><td>132.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(+124.79%)</b></td><td>0.04 <b>(+24.07%)</b></td><td>0.03 (+4.87%)</td><td>0.03 (-11.08%)</td><td>0.02 <b>(+778.74%)</b></td><td>613.50 (+12.47%)</td><td>472.16 (-6.53%)</td><td>495.70 (-4.65%)</td><td>206.40 <b>(-55.51%)</b></td><td>157.19 <b>(+312.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>545.50 (n/a)</td><td>505.14 (n/a)</td><td>519.90 (n/a)</td><td>463.90 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (+4.21%)</td><td>0.04 (-6.92%)</td><td>0.04 (-2.19%)</td><td>0.01 <b>(-57.90%)</b></td><td>0.02 (+11.09%)</td><td>2391.70 <b>(+137.51%)</b></td><td>800.22 <b>(+54.54%)</b></td><td>458.30 (+2.25%)</td><td>244.40 (-4.04%)</td><td>900.59 <b>(+190.63%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1007.00 (n/a)</td><td>517.82 (n/a)</td><td>448.20 (n/a)</td><td>254.70 (n/a)</td><td>309.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (-17.90%)</td><td>0.06 <b>(+23.38%)</b></td><td>0.06 <b>(+40.76%)</b></td><td>0.04 <b>(+52.98%)</b></td><td>0.02 <b>(-49.28%)</b></td><td>402.90 <b>(-34.63%)</b></td><td>278.02 <b>(-31.57%)</b></td><td>262.10 <b>(-28.97%)</b></td><td>197.50 <b>(+21.84%)</b></td><td>76.45 <b>(-58.55%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>616.30 (n/a)</td><td>406.26 (n/a)</td><td>369.00 (n/a)</td><td>162.10 (n/a)</td><td>184.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 <b>(+34.32%)</b></td><td>0.07 <b>(+52.16%)</b></td><td>0.07 <b>(+111.72%)</b></td><td>0.05 <b>(+57.15%)</b></td><td>0.02 (-14.02%)</td><td>360.10 <b>(-36.38%)</b></td><td>258.68 <b>(-39.87%)</b></td><td>247.60 <b>(-52.78%)</b></td><td>181.00 <b>(-25.58%)</b></td><td>65.37 <b>(-59.26%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>566.00 (n/a)</td><td>430.18 (n/a)</td><td>524.30 (n/a)</td><td>243.20 (n/a)</td><td>160.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(+56.30%)</b></td><td>0.04 <b>(+26.82%)</b></td><td>0.04 <b>(+20.90%)</b></td><td>0.02 (+7.43%)</td><td>0.02 <b>(+111.83%)</b></td><td>656.30 (-6.92%)</td><td>423.40 (-15.94%)</td><td>390.50 (-17.28%)</td><td>233.60 <b>(-36.00%)</b></td><td>153.50 <b>(+21.29%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>705.10 (n/a)</td><td>503.66 (n/a)</td><td>472.10 (n/a)</td><td>365.00 (n/a)</td><td>126.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (+10.41%)</td><td>0.05 <b>(+66.17%)</b></td><td>0.05 <b>(+89.17%)</b></td><td>0.01 (-4.24%)</td><td>0.02 (+13.45%)</td><td>2003.00 (+4.43%)</td><td>650.82 <b>(-36.19%)</b></td><td>300.90 <b>(-47.15%)</b></td><td>252.50 (-9.43%)</td><td>759.34 (-2.93%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1918.00 (n/a)</td><td>1019.86 (n/a)</td><td>569.30 (n/a)</td><td>278.80 (n/a)</td><td>782.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.17 <b>(+32.22%)</b></td><td>0.12 <b>(+20.56%)</b></td><td>0.13 <b>(+20.36%)</b></td><td>0.06 (-13.51%)</td><td>0.05 <b>(+93.05%)</b></td><td>529.60 (+15.63%)</td><td>327.10 (-7.37%)</td><td>251.30 (-16.90%)</td><td>189.90 <b>(-24.37%)</b></td><td>154.18 <b>(+61.84%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>458.00 (n/a)</td><td>353.12 (n/a)</td><td>302.40 (n/a)</td><td>251.10 (n/a)</td><td>95.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.20 <b>(+68.46%)</b></td><td>0.16 <b>(+67.06%)</b></td><td>0.15 <b>(+44.24%)</b></td><td>0.13 <b>(+198.13%)</b></td><td>0.03 (+7.24%)</td><td>246.50 <b>(-66.46%)</b></td><td>207.96 <b>(-45.98%)</b></td><td>213.10 <b>(-30.65%)</b></td><td>162.90 <b>(-40.66%)</b></td><td>39.74 <b>(-79.74%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>734.90 (n/a)</td><td>384.96 (n/a)</td><td>307.30 (n/a)</td><td>274.50 (n/a)</td><td>196.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (-5.16%)</td><td>0.07 (-6.15%)</td><td>0.07 (-7.66%)</td><td>0.05 <b>(+21.43%)</b></td><td>0.03 (-14.19%)</td><td>629.60 (-17.66%)</td><td>485.96 (+1.75%)</td><td>493.40 (+8.30%)</td><td>269.20 (+5.44%)</td><td>138.08 <b>(-28.29%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>764.60 (n/a)</td><td>477.62 (n/a)</td><td>455.60 (n/a)</td><td>255.30 (n/a)</td><td>192.56 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (-16.06%)</td><td>0.10 (-13.95%)</td><td>0.11 (-7.20%)</td><td>0.07 (+4.54%)</td><td>0.02 <b>(-27.58%)</b></td><td>495.50 (-4.34%)</td><td>343.00 (+11.92%)</td><td>285.80 (+7.77%)</td><td>268.60 (+19.11%)</td><td>97.88 (-19.83%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>518.00 (n/a)</td><td>306.48 (n/a)</td><td>265.20 (n/a)</td><td>225.50 (n/a)</td><td>122.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 <b>(+49.41%)</b></td><td>0.07 (+4.45%)</td><td>0.06 (+1.60%)</td><td>0.02 <b>(-67.72%)</b></td><td>0.04 <b>(+310.48%)</b></td><td>1845.50 <b>(+209.75%)</b></td><td>731.62 <b>(+39.32%)</b></td><td>535.60 (-1.58%)</td><td>296.10 <b>(-33.07%)</b></td><td>634.45 <b>(+827.86%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>595.80 (n/a)</td><td>525.12 (n/a)</td><td>544.20 (n/a)</td><td>442.40 (n/a)</td><td>68.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(-26.20%)</b></td><td>0.06 <b>(-20.33%)</b></td><td>0.06 <b>(-26.03%)</b></td><td>0.03 <b>(+78.16%)</b></td><td>0.02 <b>(-52.45%)</b></td><td>1059.60 <b>(-43.87%)</b></td><td>595.80 (-12.45%)</td><td>506.50 <b>(+35.17%)</b></td><td>399.10 <b>(+35.47%)</b></td><td>263.61 <b>(-61.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1887.70 (n/a)</td><td>680.50 (n/a)</td><td>374.70 (n/a)</td><td>294.60 (n/a)</td><td>682.45 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (-3.40%)</td><td>0.11 <b>(+47.89%)</b></td><td>0.12 <b>(+93.33%)</b></td><td>0.07 <b>(+30.35%)</b></td><td>0.02 <b>(-32.96%)</b></td><td>473.60 <b>(-23.28%)</b></td><td>316.60 <b>(-37.46%)</b></td><td>281.40 <b>(-48.27%)</b></td><td>243.10 (+3.53%)</td><td>91.25 <b>(-41.84%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>617.30 (n/a)</td><td>506.26 (n/a)</td><td>544.00 (n/a)</td><td>234.80 (n/a)</td><td>156.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(-27.64%)</b></td><td>0.07 <b>(-27.92%)</b></td><td>0.07 <b>(-36.27%)</b></td><td>0.07 (-3.82%)</td><td>0.01 <b>(-65.69%)</b></td><td>487.40 (+3.97%)</td><td>449.30 <b>(+34.86%)</b></td><td>462.80 <b>(+56.88%)</b></td><td>396.80 <b>(+38.21%)</b></td><td>37.21 <b>(-51.68%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>468.80 (n/a)</td><td>333.16 (n/a)</td><td>295.00 (n/a)</td><td>287.10 (n/a)</td><td>77.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (+9.12%)</td><td>0.10 (+10.52%)</td><td>0.09 (-9.84%)</td><td>0.06 (+2.43%)</td><td>0.04 <b>(+27.16%)</b></td><td>545.70 (-2.38%)</td><td>359.38 (-7.00%)</td><td>377.70 (+10.93%)</td><td>221.00 (-8.34%)</td><td>137.78 (+2.39%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>559.00 (n/a)</td><td>386.44 (n/a)</td><td>340.50 (n/a)</td><td>241.10 (n/a)</td><td>134.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 <b>(-21.58%)</b></td><td>0.09 <b>(+27.40%)</b></td><td>0.09 <b>(+35.41%)</b></td><td>0.08 <b>(+342.06%)</b></td><td>0.01 <b>(-69.20%)</b></td><td>412.30 <b>(-77.38%)</b></td><td>358.20 <b>(-48.81%)</b></td><td>345.50 <b>(-26.14%)</b></td><td>294.30 <b>(+27.57%)</b></td><td>52.39 <b>(-91.79%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1822.50 (n/a)</td><td>699.68 (n/a)</td><td>467.80 (n/a)</td><td>230.70 (n/a)</td><td>637.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 <b>(-31.24%)</b></td><td>0.08 (-10.45%)</td><td>0.07 (-16.24%)</td><td>0.06 (+14.03%)</td><td>0.02 <b>(-44.00%)</b></td><td>547.10 (-12.31%)</td><td>428.20 (+4.57%)</td><td>464.20 (+19.39%)</td><td>317.00 <b>(+45.41%)</b></td><td>103.62 <b>(-29.57%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>623.90 (n/a)</td><td>409.48 (n/a)</td><td>388.80 (n/a)</td><td>218.00 (n/a)</td><td>147.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 <b>(-24.32%)</b></td><td>0.08 (-16.97%)</td><td>0.08 (+15.14%)</td><td>0.02 <b>(-75.68%)</b></td><td>0.04 <b>(+20.78%)</b></td><td>1933.80 <b>(+311.18%)</b></td><td>687.68 <b>(+76.75%)</b></td><td>390.00 (-13.14%)</td><td>315.90 <b>(+32.12%)</b></td><td>699.87 <b>(+563.65%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>470.30 (n/a)</td><td>389.08 (n/a)</td><td>449.00 (n/a)</td><td>239.10 (n/a)</td><td>105.46 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/repeat</summary>


### test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]

_No metrics available._


### test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (-10.74%)</td><td>0.07 (-8.62%)</td><td>0.09 (+8.15%)</td><td>0.05 (-2.54%)</td><td>0.02 (-6.19%)</td><td>526.90 (+2.61%)</td><td>354.80 (+9.29%)</td><td>287.20 (-7.53%)</td><td>270.00 (+12.03%)</td><td>114.54 (+3.19%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>513.50 (n/a)</td><td>324.64 (n/a)</td><td>310.60 (n/a)</td><td>241.00 (n/a)</td><td>111.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.18 (-9.39%)</td><td>0.13 (-16.92%)</td><td>0.16 (-9.04%)</td><td>0.03 <b>(-68.04%)</b></td><td>0.07 <b>(+28.66%)</b></td><td>1906.60 <b>(+212.87%)</b></td><td>657.72 <b>(+82.27%)</b></td><td>301.30 (+9.92%)</td><td>274.20 (+10.34%)</td><td>706.44 <b>(+353.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>609.40 (n/a)</td><td>360.84 (n/a)</td><td>274.10 (n/a)</td><td>248.50 (n/a)</td><td>155.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.94 (-0.99%)</td><td>3.05 (+2.65%)</td><td>2.66 (+2.54%)</td><td>2.61 (+6.69%)</td><td>0.60 (-8.32%)</td><td>4024.80 (-6.27%)</td><td>3529.46 (-3.20%)</td><td>3937.50 (-2.47%)</td><td>2662.10 (+1.00%)</td><td>622.07 (-11.77%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.98 (n/a)</td><td>2.98 (n/a)</td><td>2.60 (n/a)</td><td>2.44 (n/a)</td><td>0.65 (n/a)</td><td>4293.90 (n/a)</td><td>3646.00 (n/a)</td><td>4037.40 (n/a)</td><td>2635.80 (n/a)</td><td>705.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (-18.45%)</td><td>0.10 <b>(-25.23%)</b></td><td>0.09 <b>(-23.81%)</b></td><td>0.08 <b>(-20.75%)</b></td><td>0.03 (-17.91%)</td><td>505.50 <b>(+26.19%)</b></td><td>428.86 <b>(+33.77%)</b></td><td>435.40 <b>(+31.26%)</b></td><td>267.40 <b>(+22.60%)</b></td><td>97.14 <b>(+22.30%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>400.60 (n/a)</td><td>320.60 (n/a)</td><td>331.70 (n/a)</td><td>218.10 (n/a)</td><td>79.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-10.64%)</td><td>0.02 (+7.49%)</td><td>0.02 (+6.98%)</td><td>0.01 <b>(+24.60%)</b></td><td>0.00 <b>(-36.10%)</b></td><td>406.90 (-19.73%)</td><td>288.72 (-12.14%)</td><td>266.60 (-6.52%)</td><td>235.70 (+11.87%)</td><td>68.59 <b>(-41.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.90 (n/a)</td><td>328.62 (n/a)</td><td>285.20 (n/a)</td><td>210.70 (n/a)</td><td>117.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-7.77%)</td><td>0.01 (-11.29%)</td><td>0.01 (-3.43%)</td><td>0.01 <b>(-23.72%)</b></td><td>0.00 <b>(+23.97%)</b></td><td>517.30 <b>(+31.09%)</b></td><td>371.62 (+17.68%)</td><td>291.50 (+3.55%)</td><td>265.40 (+8.42%)</td><td>122.73 <b>(+74.03%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>394.60 (n/a)</td><td>315.80 (n/a)</td><td>281.50 (n/a)</td><td>244.80 (n/a)</td><td>70.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-19.40%)</td><td>0.02 (+6.98%)</td><td>0.02 (+16.43%)</td><td>0.01 <b>(+382.84%)</b></td><td>0.00 <b>(-54.81%)</b></td><td>512.10 <b>(-79.29%)</b></td><td>379.22 <b>(-51.45%)</b></td><td>403.70 (-14.12%)</td><td>266.30 <b>(+24.03%)</b></td><td>99.51 <b>(-89.56%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2472.60 (n/a)</td><td>781.14 (n/a)</td><td>470.10 (n/a)</td><td>214.70 (n/a)</td><td>953.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 <b>(-33.78%)</b></td><td>0.01 <b>(-24.52%)</b></td><td>0.01 <b>(-39.32%)</b></td><td>0.01 (-11.52%)</td><td>0.00 <b>(-34.11%)</b></td><td>618.00 (+13.02%)</td><td>454.24 <b>(+27.33%)</b></td><td>467.20 <b>(+64.80%)</b></td><td>280.90 <b>(+51.02%)</b></td><td>162.78 (+6.65%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.80 (n/a)</td><td>356.74 (n/a)</td><td>283.50 (n/a)</td><td>186.00 (n/a)</td><td>152.63 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-7.83%)</td><td>0.01 <b>(-31.53%)</b></td><td>0.01 (-13.63%)</td><td>0.00 <b>(-79.32%)</b></td><td>0.01 <b>(+77.39%)</b></td><td>2453.80 <b>(+383.60%)</b></td><td>1105.44 <b>(+178.34%)</b></td><td>495.70 (+15.79%)</td><td>279.30 (+8.51%)</td><td>1005.97 <b>(+918.56%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.40 (n/a)</td><td>397.16 (n/a)</td><td>428.10 (n/a)</td><td>257.40 (n/a)</td><td>98.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-1.35%)</td><td>0.01 (-13.12%)</td><td>0.01 <b>(-39.64%)</b></td><td>0.01 (+1.70%)</td><td>0.00 (-15.18%)</td><td>525.00 (-1.67%)</td><td>394.98 (+10.14%)</td><td>430.90 <b>(+65.67%)</b></td><td>230.00 (+1.37%)</td><td>129.39 (-18.39%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.90 (n/a)</td><td>358.62 (n/a)</td><td>260.10 (n/a)</td><td>226.90 (n/a)</td><td>158.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(+22.55%)</b></td><td>0.02 <b>(+34.95%)</b></td><td>0.02 <b>(+42.44%)</b></td><td>0.01 <b>(+21.88%)</b></td><td>0.00 <b>(+24.90%)</b></td><td>456.60 (-17.97%)</td><td>323.36 <b>(-25.55%)</b></td><td>301.00 <b>(-29.79%)</b></td><td>238.50 (-18.38%)</td><td>84.49 (-11.78%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>556.60 (n/a)</td><td>434.36 (n/a)</td><td>428.70 (n/a)</td><td>292.20 (n/a)</td><td>95.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (-13.03%)</td><td>0.01 <b>(-23.51%)</b></td><td>0.01 <b>(-44.04%)</b></td><td>0.01 (+3.72%)</td><td>0.00 <b>(-38.96%)</b></td><td>498.80 (-3.58%)</td><td>440.46 <b>(+24.03%)</b></td><td>482.10 <b>(+78.69%)</b></td><td>295.70 (+14.97%)</td><td>85.31 <b>(-32.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.30 (n/a)</td><td>355.12 (n/a)</td><td>269.80 (n/a)</td><td>257.20 (n/a)</td><td>125.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 <b>(-20.34%)</b></td><td>0.01 (+14.45%)</td><td>0.01 (+14.09%)</td><td>0.01 <b>(+195.18%)</b></td><td>0.00 <b>(-38.50%)</b></td><td>781.30 <b>(-66.12%)</b></td><td>469.02 <b>(-42.70%)</b></td><td>433.60 (-12.35%)</td><td>311.80 <b>(+25.52%)</b></td><td>190.62 <b>(-77.34%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2306.20 (n/a)</td><td>818.56 (n/a)</td><td>494.70 (n/a)</td><td>248.40 (n/a)</td><td>841.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-10.62%)</td><td>0.01 (-13.19%)</td><td>0.01 (-9.53%)</td><td>0.01 (-3.65%)</td><td>0.00 (-18.72%)</td><td>528.00 (+3.79%)</td><td>427.90 (+12.17%)</td><td>438.50 (+10.54%)</td><td>246.40 (+11.90%)</td><td>112.08 (-10.71%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.70 (n/a)</td><td>381.46 (n/a)</td><td>396.70 (n/a)</td><td>220.20 (n/a)</td><td>125.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-3.64%)</td><td>0.01 (-13.55%)</td><td>0.01 (+12.79%)</td><td>0.00 <b>(-32.36%)</b></td><td>0.01 (+3.17%)</td><td>964.30 <b>(+47.85%)</b></td><td>595.60 <b>(+25.69%)</b></td><td>515.50 (-11.33%)</td><td>202.70 (+3.74%)</td><td>299.32 <b>(+52.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.20 (n/a)</td><td>473.88 (n/a)</td><td>581.40 (n/a)</td><td>195.40 (n/a)</td><td>196.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (-16.78%)</td><td>0.01 (+6.92%)</td><td>0.01 (+3.98%)</td><td>0.01 <b>(+37.23%)</b></td><td>0.00 <b>(-39.28%)</b></td><td>523.60 <b>(-27.13%)</b></td><td>431.56 (-13.11%)</td><td>470.60 (-3.82%)</td><td>300.70 <b>(+20.18%)</b></td><td>96.60 <b>(-42.21%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>718.50 (n/a)</td><td>496.68 (n/a)</td><td>489.30 (n/a)</td><td>250.20 (n/a)</td><td>167.17 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (+1.88%)</td><td>0.02 <b>(-23.50%)</b></td><td>0.02 <b>(-34.29%)</b></td><td>0.02 (+2.92%)</td><td>0.01 (+1.85%)</td><td>492.20 (-2.84%)</td><td>400.92 <b>(+30.06%)</b></td><td>401.60 <b>(+52.18%)</b></td><td>231.10 (-1.87%)</td><td>104.51 (-7.85%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.60 (n/a)</td><td>308.26 (n/a)</td><td>263.90 (n/a)</td><td>235.50 (n/a)</td><td>113.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (-18.80%)</td><td>0.03 (-18.75%)</td><td>0.03 <b>(-33.62%)</b></td><td>0.02 (-7.59%)</td><td>0.01 <b>(-29.43%)</b></td><td>511.80 (+8.23%)</td><td>396.22 (+19.57%)</td><td>422.20 <b>(+50.62%)</b></td><td>289.60 <b>(+23.18%)</b></td><td>98.77 (-9.68%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.90 (n/a)</td><td>331.38 (n/a)</td><td>280.30 (n/a)</td><td>235.10 (n/a)</td><td>109.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (-5.74%)</td><td>0.02 (+3.15%)</td><td>0.02 <b>(+31.59%)</b></td><td>0.01 (-10.85%)</td><td>0.01 (-10.15%)</td><td>592.40 (+12.18%)</td><td>413.96 (-3.18%)</td><td>367.90 <b>(-24.00%)</b></td><td>295.90 (+6.10%)</td><td>113.69 (+9.79%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.10 (n/a)</td><td>427.56 (n/a)</td><td>484.10 (n/a)</td><td>278.90 (n/a)</td><td>103.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(-44.11%)</b></td><td>0.02 <b>(-27.97%)</b></td><td>0.02 <b>(-20.34%)</b></td><td>0.02 (+14.72%)</td><td>0.00 <b>(-79.00%)</b></td><td>533.30 (-12.83%)</td><td>477.52 <b>(+25.78%)</b></td><td>474.50 <b>(+25.53%)</b></td><td>426.10 <b>(+78.96%)</b></td><td>48.01 <b>(-67.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.80 (n/a)</td><td>379.64 (n/a)</td><td>378.00 (n/a)</td><td>238.10 (n/a)</td><td>146.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+26.91%)</b></td><td>0.02 (+13.49%)</td><td>0.03 (+10.35%)</td><td>0.02 <b>(+28.53%)</b></td><td>0.01 <b>(+30.00%)</b></td><td>497.10 <b>(-22.19%)</b></td><td>361.98 (-11.16%)</td><td>303.70 (-9.40%)</td><td>221.20 <b>(-21.20%)</b></td><td>124.12 (-15.36%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.90 (n/a)</td><td>407.46 (n/a)</td><td>335.20 (n/a)</td><td>280.70 (n/a)</td><td>146.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (-3.87%)</td><td>0.03 (-11.37%)</td><td>0.02 <b>(-29.46%)</b></td><td>0.02 <b>(-20.64%)</b></td><td>0.01 (+6.53%)</td><td>653.40 <b>(+26.02%)</b></td><td>423.34 (+16.10%)</td><td>414.30 <b>(+41.79%)</b></td><td>271.50 (+4.02%)</td><td>160.46 <b>(+30.39%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.50 (n/a)</td><td>364.64 (n/a)</td><td>292.20 (n/a)</td><td>261.00 (n/a)</td><td>123.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+26.23%)</b></td><td>0.02 (-0.15%)</td><td>0.02 (+2.65%)</td><td>0.00 <b>(-72.97%)</b></td><td>0.01 <b>(+133.24%)</b></td><td>1859.70 <b>(+269.94%)</b></td><td>683.34 <b>(+55.87%)</b></td><td>451.20 (-2.59%)</td><td>231.60 <b>(-20.77%)</b></td><td>666.76 <b>(+696.76%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>502.70 (n/a)</td><td>438.40 (n/a)</td><td>463.20 (n/a)</td><td>292.30 (n/a)</td><td>83.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (-6.51%)</td><td>0.03 (-0.98%)</td><td>0.03 (-1.16%)</td><td>0.02 (+11.35%)</td><td>0.01 <b>(-31.28%)</b></td><td>613.90 (-10.20%)</td><td>401.40 (-9.27%)</td><td>365.80 (+1.19%)</td><td>258.80 (+6.94%)</td><td>140.81 <b>(-35.79%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>683.60 (n/a)</td><td>442.42 (n/a)</td><td>361.50 (n/a)</td><td>242.00 (n/a)</td><td>219.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+31.11%)</b></td><td>0.03 <b>(+47.10%)</b></td><td>0.03 <b>(+92.43%)</b></td><td>0.02 <b>(+23.85%)</b></td><td>0.01 <b>(+36.16%)</b></td><td>489.10 (-19.26%)</td><td>349.12 <b>(-30.47%)</b></td><td>300.40 <b>(-48.03%)</b></td><td>201.80 <b>(-23.71%)</b></td><td>132.24 (-7.04%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.80 (n/a)</td><td>502.08 (n/a)</td><td>578.00 (n/a)</td><td>264.50 (n/a)</td><td>142.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (-19.24%)</td><td>0.02 <b>(-37.34%)</b></td><td>0.02 <b>(-59.46%)</b></td><td>0.00 <b>(-65.96%)</b></td><td>0.01 (-15.72%)</td><td>1977.60 <b>(+193.76%)</b></td><td>767.08 <b>(+101.40%)</b></td><td>604.90 <b>(+146.70%)</b></td><td>251.40 <b>(+23.84%)</b></td><td>693.73 <b>(+225.07%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.20 (n/a)</td><td>380.88 (n/a)</td><td>245.20 (n/a)</td><td>203.00 (n/a)</td><td>213.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(+72.25%)</b></td><td>0.02 <b>(+33.28%)</b></td><td>0.02 (+13.41%)</td><td>0.02 <b>(+34.57%)</b></td><td>0.01 <b>(+162.96%)</b></td><td>497.50 <b>(-25.69%)</b></td><td>417.10 <b>(-20.80%)</b></td><td>462.30 (-11.83%)</td><td>229.20 <b>(-41.93%)</b></td><td>109.83 (+10.63%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.50 (n/a)</td><td>526.66 (n/a)</td><td>524.30 (n/a)</td><td>394.70 (n/a)</td><td>99.28 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (+8.95%)</td><td>0.06 (+19.07%)</td><td>0.05 <b>(+63.09%)</b></td><td>0.03 (-0.26%)</td><td>0.02 (-11.45%)</td><td>529.70 (+0.27%)</td><td>319.38 <b>(-20.19%)</b></td><td>307.90 <b>(-38.68%)</b></td><td>189.00 (-8.21%)</td><td>128.47 (-19.64%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>528.30 (n/a)</td><td>400.18 (n/a)</td><td>502.10 (n/a)</td><td>205.90 (n/a)</td><td>159.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (-1.45%)</td><td>0.07 (-11.49%)</td><td>0.06 <b>(-26.52%)</b></td><td>0.04 (-12.95%)</td><td>0.02 (-7.53%)</td><td>554.80 (+14.89%)</td><td>388.30 (+12.63%)</td><td>394.40 <b>(+36.09%)</b></td><td>252.00 (+1.45%)</td><td>118.82 (+6.03%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>482.90 (n/a)</td><td>344.76 (n/a)</td><td>289.80 (n/a)</td><td>248.40 (n/a)</td><td>112.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (-8.59%)</td><td>0.05 (-13.76%)</td><td>0.05 (-15.07%)</td><td>0.03 (-16.75%)</td><td>0.02 <b>(-21.86%)</b></td><td>563.60 <b>(+20.12%)</b></td><td>381.56 (+13.33%)</td><td>357.10 (+17.74%)</td><td>242.60 (+9.38%)</td><td>126.91 (+2.11%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>469.20 (n/a)</td><td>336.68 (n/a)</td><td>303.30 (n/a)</td><td>221.80 (n/a)</td><td>124.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (-12.03%)</td><td>0.06 (-18.13%)</td><td>0.04 <b>(-42.29%)</b></td><td>0.04 (-11.72%)</td><td>0.02 (-15.37%)</td><td>573.10 (+13.26%)</td><td>413.90 (+19.50%)</td><td>457.90 <b>(+73.25%)</b></td><td>233.80 (+13.72%)</td><td>145.24 (-1.15%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>506.00 (n/a)</td><td>346.36 (n/a)</td><td>264.30 (n/a)</td><td>205.60 (n/a)</td><td>146.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (+4.88%)</td><td>0.05 (+0.02%)</td><td>0.04 (-5.42%)</td><td>0.03 (-5.59%)</td><td>0.02 (+17.47%)</td><td>537.80 (+5.93%)</td><td>393.10 (+3.85%)</td><td>433.90 (+5.75%)</td><td>223.00 (-4.62%)</td><td>149.97 (+19.51%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>507.70 (n/a)</td><td>378.54 (n/a)</td><td>410.30 (n/a)</td><td>233.80 (n/a)</td><td>125.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(+35.62%)</b></td><td>0.05 (+12.04%)</td><td>0.04 <b>(-20.33%)</b></td><td>0.03 (-4.85%)</td><td>0.02 <b>(+101.93%)</b></td><td>693.10 (+5.11%)</td><td>485.98 (-0.23%)</td><td>548.40 <b>(+25.52%)</b></td><td>245.40 <b>(-26.26%)</b></td><td>199.63 <b>(+54.67%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>659.40 (n/a)</td><td>487.12 (n/a)</td><td>436.90 (n/a)</td><td>332.80 (n/a)</td><td>129.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (+10.12%)</td><td>0.06 <b>(+24.04%)</b></td><td>0.06 <b>(+23.96%)</b></td><td>0.03 (-9.23%)</td><td>0.02 <b>(+23.96%)</b></td><td>542.40 (+10.18%)</td><td>307.82 (-16.21%)</td><td>268.30 (-19.31%)</td><td>216.80 (-9.21%)</td><td>133.16 <b>(+29.71%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>492.30 (n/a)</td><td>367.36 (n/a)</td><td>332.50 (n/a)</td><td>238.80 (n/a)</td><td>102.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (-0.77%)</td><td>0.05 (-12.11%)</td><td>0.05 (+18.11%)</td><td>0.01 <b>(-78.47%)</b></td><td>0.03 <b>(+40.31%)</b></td><td>2486.40 <b>(+364.57%)</b></td><td>792.24 <b>(+104.23%)</b></td><td>352.80 (-15.31%)</td><td>247.90 (+0.77%)</td><td>957.37 <b>(+616.03%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.20 (n/a)</td><td>387.92 (n/a)</td><td>416.60 (n/a)</td><td>246.00 (n/a)</td><td>133.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 <b>(-24.43%)</b></td><td>0.04 (+1.61%)</td><td>0.05 <b>(+30.25%)</b></td><td>0.03 (-1.34%)</td><td>0.01 <b>(-46.07%)</b></td><td>478.30 (+1.36%)</td><td>380.36 (-5.20%)</td><td>344.50 <b>(-23.22%)</b></td><td>319.60 <b>(+32.28%)</b></td><td>69.98 <b>(-26.89%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.90 (n/a)</td><td>401.22 (n/a)</td><td>448.70 (n/a)</td><td>241.60 (n/a)</td><td>95.73 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(+59.46%)</b></td><td>0.05 <b>(+40.22%)</b></td><td>0.06 <b>(+79.20%)</b></td><td>0.02 <b>(-37.13%)</b></td><td>0.03 <b>(+240.50%)</b></td><td>1000.30 <b>(+59.08%)</b></td><td>477.72 (-6.64%)</td><td>293.90 <b>(-44.20%)</b></td><td>235.00 <b>(-37.30%)</b></td><td>326.23 <b>(+239.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>628.80 (n/a)</td><td>511.72 (n/a)</td><td>526.70 (n/a)</td><td>374.80 (n/a)</td><td>95.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 <b>(-29.49%)</b></td><td>0.03 (-18.86%)</td><td>0.03 (-14.91%)</td><td>0.02 <b>(-40.66%)</b></td><td>0.01 (-18.59%)</td><td>1018.00 <b>(+68.54%)</b></td><td>617.36 <b>(+27.45%)</b></td><td>560.90 (+17.52%)</td><td>444.70 <b>(+41.85%)</b></td><td>231.89 <b>(+106.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>604.00 (n/a)</td><td>484.40 (n/a)</td><td>477.30 (n/a)</td><td>313.50 (n/a)</td><td>112.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (-15.63%)</td><td>0.08 (-3.83%)</td><td>0.09 (+16.14%)</td><td>0.06 (+8.74%)</td><td>0.02 <b>(-32.34%)</b></td><td>578.10 (-8.03%)</td><td>417.26 (-2.00%)</td><td>366.30 (-13.89%)</td><td>286.40 (+18.54%)</td><td>124.53 <b>(-23.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>628.60 (n/a)</td><td>425.76 (n/a)</td><td>425.40 (n/a)</td><td>241.60 (n/a)</td><td>163.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (-16.23%)</td><td>0.09 (-6.27%)</td><td>0.07 (-7.99%)</td><td>0.06 (+17.81%)</td><td>0.03 <b>(-24.98%)</b></td><td>508.90 (-15.11%)</td><td>408.72 (+1.93%)</td><td>480.00 (+8.70%)</td><td>270.40 (+19.38%)</td><td>116.56 <b>(-21.38%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>599.50 (n/a)</td><td>400.98 (n/a)</td><td>441.60 (n/a)</td><td>226.50 (n/a)</td><td>148.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (-6.94%)</td><td>0.10 (-5.00%)</td><td>0.09 <b>(-25.56%)</b></td><td>0.08 <b>(+47.72%)</b></td><td>0.04 <b>(-22.97%)</b></td><td>523.00 <b>(-32.30%)</b></td><td>428.46 (-3.35%)</td><td>480.30 <b>(+34.35%)</b></td><td>251.10 (+7.45%)</td><td>109.47 <b>(-46.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>772.50 (n/a)</td><td>443.30 (n/a)</td><td>357.50 (n/a)</td><td>233.70 (n/a)</td><td>206.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(-51.85%)</b></td><td>0.07 <b>(-31.41%)</b></td><td>0.06 <b>(-20.61%)</b></td><td>0.06 <b>(-22.27%)</b></td><td>0.01 <b>(-76.33%)</b></td><td>566.80 <b>(+28.64%)</b></td><td>501.70 <b>(+34.77%)</b></td><td>525.70 <b>(+25.95%)</b></td><td>405.10 <b>(+107.74%)</b></td><td>66.29 <b>(-34.46%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>440.60 (n/a)</td><td>372.26 (n/a)</td><td>417.40 (n/a)</td><td>195.00 (n/a)</td><td>101.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 <b>(+43.41%)</b></td><td>0.10 <b>(+32.65%)</b></td><td>0.10 <b>(+65.25%)</b></td><td>0.02 <b>(-62.29%)</b></td><td>0.05 <b>(+117.69%)</b></td><td>1905.80 <b>(+165.17%)</b></td><td>669.04 (+16.20%)</td><td>400.40 <b>(-39.48%)</b></td><td>251.90 <b>(-30.26%)</b></td><td>697.82 <b>(+328.89%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>718.70 (n/a)</td><td>575.78 (n/a)</td><td>661.60 (n/a)</td><td>361.20 (n/a)</td><td>162.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (+5.37%)</td><td>0.10 <b>(+34.56%)</b></td><td>0.11 <b>(+93.13%)</b></td><td>0.05 (+2.15%)</td><td>0.04 (+1.78%)</td><td>672.70 (-2.11%)</td><td>377.38 <b>(-25.32%)</b></td><td>285.20 <b>(-48.22%)</b></td><td>213.90 (-5.10%)</td><td>184.68 (+2.69%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>687.20 (n/a)</td><td>505.32 (n/a)</td><td>550.80 (n/a)</td><td>225.40 (n/a)</td><td>179.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.17 <b>(+21.53%)</b></td><td>0.09 (+2.21%)</td><td>0.07 (+2.72%)</td><td>0.06 (+2.16%)</td><td>0.04 <b>(+36.44%)</b></td><td>598.90 (-2.12%)</td><td>455.76 (+1.05%)</td><td>491.90 (-2.65%)</td><td>221.90 (-17.69%)</td><td>139.88 (+2.32%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>611.90 (n/a)</td><td>451.04 (n/a)</td><td>505.30 (n/a)</td><td>269.60 (n/a)</td><td>136.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (-15.52%)</td><td>0.08 (-16.61%)</td><td>0.07 <b>(-25.24%)</b></td><td>0.06 (+1.86%)</td><td>0.03 <b>(-23.02%)</b></td><td>540.30 (-1.82%)</td><td>428.64 (+15.51%)</td><td>472.40 <b>(+33.79%)</b></td><td>239.50 (+18.33%)</td><td>119.70 (-13.41%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>550.30 (n/a)</td><td>371.08 (n/a)</td><td>353.10 (n/a)</td><td>202.40 (n/a)</td><td>138.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (+16.47%)</td><td>0.08 (+8.75%)</td><td>0.08 (+6.79%)</td><td>0.06 <b>(+42.61%)</b></td><td>0.02 (-5.32%)</td><td>569.60 <b>(-29.87%)</b></td><td>465.90 (-11.05%)</td><td>467.00 (-6.36%)</td><td>324.90 (-14.14%)</td><td>90.62 <b>(-46.84%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>812.20 (n/a)</td><td>523.76 (n/a)</td><td>498.70 (n/a)</td><td>378.40 (n/a)</td><td>170.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 <b>(-29.60%)</b></td><td>0.09 <b>(+23.84%)</b></td><td>0.08 <b>(+40.56%)</b></td><td>0.07 <b>(+264.80%)</b></td><td>0.02 <b>(-63.34%)</b></td><td>475.10 <b>(-72.59%)</b></td><td>386.66 <b>(-49.70%)</b></td><td>408.10 <b>(-28.85%)</b></td><td>253.90 <b>(+42.00%)</b></td><td>83.24 <b>(-85.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1733.10 (n/a)</td><td>768.68 (n/a)</td><td>573.60 (n/a)</td><td>178.80 (n/a)</td><td>582.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (-7.56%)</td><td>0.06 <b>(+51.26%)</b></td><td>0.05 <b>(+34.54%)</b></td><td>0.04 <b>(+402.28%)</b></td><td>0.02 <b>(-42.62%)</b></td><td>489.90 <b>(-80.09%)</b></td><td>373.44 <b>(-59.94%)</b></td><td>413.50 <b>(-25.67%)</b></td><td>272.00 (+8.19%)</td><td>96.85 <b>(-89.09%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2460.80 (n/a)</td><td>932.26 (n/a)</td><td>556.30 (n/a)</td><td>251.40 (n/a)</td><td>887.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 <b>(-36.06%)</b></td><td>0.06 <b>(-20.38%)</b></td><td>0.05 <b>(-35.27%)</b></td><td>0.05 (+19.41%)</td><td>0.01 <b>(-58.75%)</b></td><td>424.80 (-16.26%)</td><td>348.26 (+10.97%)</td><td>378.00 <b>(+54.47%)</b></td><td>259.70 <b>(+56.45%)</b></td><td>72.83 <b>(-48.67%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>507.30 (n/a)</td><td>313.82 (n/a)</td><td>244.70 (n/a)</td><td>166.00 (n/a)</td><td>141.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (+11.66%)</td><td>0.07 <b>(+32.16%)</b></td><td>0.07 <b>(+53.24%)</b></td><td>0.04 (+16.95%)</td><td>0.02 (+6.59%)</td><td>554.70 (-14.49%)</td><td>336.82 <b>(-24.41%)</b></td><td>299.20 <b>(-34.73%)</b></td><td>238.90 (-10.42%)</td><td>124.56 (-9.92%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>648.70 (n/a)</td><td>445.60 (n/a)</td><td>458.40 (n/a)</td><td>266.70 (n/a)</td><td>138.28 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (-4.83%)</td><td>0.06 (+16.08%)</td><td>0.07 <b>(+79.40%)</b></td><td>0.02 <b>(-38.16%)</b></td><td>0.03 (+6.38%)</td><td>1021.60 <b>(+61.72%)</b></td><td>438.64 (-1.90%)</td><td>290.90 <b>(-44.25%)</b></td><td>240.40 (+5.07%)</td><td>329.92 <b>(+93.90%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>631.70 (n/a)</td><td>447.14 (n/a)</td><td>521.80 (n/a)</td><td>228.80 (n/a)</td><td>170.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (-15.96%)</td><td>0.06 (+4.48%)</td><td>0.07 <b>(+41.33%)</b></td><td>0.04 (+9.82%)</td><td>0.02 <b>(-39.22%)</b></td><td>542.20 (-8.95%)</td><td>342.16 (-11.44%)</td><td>306.20 <b>(-29.25%)</b></td><td>249.70 (+19.02%)</td><td>114.81 <b>(-26.65%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>595.50 (n/a)</td><td>386.34 (n/a)</td><td>432.80 (n/a)</td><td>209.80 (n/a)</td><td>156.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 <b>(-23.07%)</b></td><td>0.05 (+3.92%)</td><td>0.05 (+10.74%)</td><td>0.03 <b>(+40.80%)</b></td><td>0.01 <b>(-44.04%)</b></td><td>676.20 <b>(-28.98%)</b></td><td>425.38 (-16.66%)</td><td>389.60 (-9.69%)</td><td>325.40 <b>(+29.95%)</b></td><td>145.07 <b>(-48.07%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>952.10 (n/a)</td><td>510.44 (n/a)</td><td>431.40 (n/a)</td><td>250.40 (n/a)</td><td>279.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (+11.07%)</td><td>0.07 (-4.16%)</td><td>0.08 (+9.34%)</td><td>0.01 <b>(-65.62%)</b></td><td>0.04 <b>(+40.23%)</b></td><td>1909.00 <b>(+190.87%)</b></td><td>648.82 <b>(+61.67%)</b></td><td>291.30 (-8.54%)</td><td>222.60 (-9.99%)</td><td>714.42 <b>(+299.30%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>656.30 (n/a)</td><td>401.32 (n/a)</td><td>318.50 (n/a)</td><td>247.30 (n/a)</td><td>178.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (+17.35%)</td><td>0.08 <b>(+20.70%)</b></td><td>0.08 <b>(+37.55%)</b></td><td>0.04 (+10.03%)</td><td>0.02 (+8.33%)</td><td>551.50 (-9.11%)</td><td>349.62 (-17.37%)</td><td>306.00 <b>(-27.30%)</b></td><td>245.10 (-14.81%)</td><td>122.19 (-9.99%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>606.80 (n/a)</td><td>423.14 (n/a)</td><td>420.90 (n/a)</td><td>287.70 (n/a)</td><td>135.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (+14.43%)</td><td>0.05 (-16.03%)</td><td>0.04 <b>(-31.25%)</b></td><td>0.04 (-15.92%)</td><td>0.02 <b>(+52.18%)</b></td><td>677.30 (+18.93%)</td><td>548.72 <b>(+27.34%)</b></td><td>589.30 <b>(+45.43%)</b></td><td>260.40 (-12.59%)</td><td>167.42 <b>(+46.78%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>569.50 (n/a)</td><td>430.92 (n/a)</td><td>405.20 (n/a)</td><td>297.90 (n/a)</td><td>114.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (-14.29%)</td><td>0.07 (-1.30%)</td><td>0.05 (+9.57%)</td><td>0.04 (-5.40%)</td><td>0.03 (-10.86%)</td><td>614.60 (+5.71%)</td><td>420.18 (+0.92%)</td><td>458.70 (-8.72%)</td><td>213.60 (+16.66%)</td><td>183.13 (+7.78%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>581.40 (n/a)</td><td>416.34 (n/a)</td><td>502.50 (n/a)</td><td>183.10 (n/a)</td><td>169.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (-15.04%)</td><td>0.08 (+10.86%)</td><td>0.09 <b>(+71.78%)</b></td><td>0.04 (+14.21%)</td><td>0.02 <b>(-28.07%)</b></td><td>556.10 (-12.44%)</td><td>352.72 (-15.93%)</td><td>278.70 <b>(-41.78%)</b></td><td>243.90 (+17.71%)</td><td>132.05 <b>(-24.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>635.10 (n/a)</td><td>419.56 (n/a)</td><td>478.70 (n/a)</td><td>207.20 (n/a)</td><td>173.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (+12.99%)</td><td>0.08 <b>(+36.63%)</b></td><td>0.08 <b>(+62.99%)</b></td><td>0.05 (+18.19%)</td><td>0.02 (+7.18%)</td><td>526.60 (-15.38%)</td><td>353.40 <b>(-27.36%)</b></td><td>307.30 <b>(-38.65%)</b></td><td>237.90 (-11.50%)</td><td>116.65 (-15.20%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>622.30 (n/a)</td><td>486.54 (n/a)</td><td>500.90 (n/a)</td><td>268.80 (n/a)</td><td>137.56 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 <b>(-34.46%)</b></td><td>0.04 <b>(-20.39%)</b></td><td>0.04 (+1.58%)</td><td>0.01 <b>(-72.74%)</b></td><td>0.02 (-17.91%)</td><td>2067.20 <b>(+266.78%)</b></td><td>718.62 <b>(+78.01%)</b></td><td>464.10 (-1.55%)</td><td>278.00 <b>(+52.58%)</b></td><td>760.51 <b>(+377.39%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>563.60 (n/a)</td><td>403.70 (n/a)</td><td>471.40 (n/a)</td><td>182.20 (n/a)</td><td>159.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 <b>(-24.03%)</b></td><td>0.05 <b>(-23.66%)</b></td><td>0.04 <b>(-36.94%)</b></td><td>0.04 <b>(+25.04%)</b></td><td>0.01 <b>(-50.01%)</b></td><td>473.40 <b>(-20.03%)</b></td><td>399.78 <b>(+20.52%)</b></td><td>428.90 <b>(+58.62%)</b></td><td>308.80 <b>(+31.63%)</b></td><td>75.51 <b>(-49.32%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.00 (n/a)</td><td>331.70 (n/a)</td><td>270.40 (n/a)</td><td>234.60 (n/a)</td><td>148.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (-1.35%)</td><td>0.07 <b>(+28.81%)</b></td><td>0.08 <b>(+75.38%)</b></td><td>0.03 (-7.26%)</td><td>0.02 (-0.80%)</td><td>586.20 (+7.82%)</td><td>321.12 <b>(-21.03%)</b></td><td>244.90 <b>(-42.98%)</b></td><td>215.40 (+1.36%)</td><td>152.63 (+16.55%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>543.70 (n/a)</td><td>406.66 (n/a)</td><td>429.50 (n/a)</td><td>212.50 (n/a)</td><td>130.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (-1.66%)</td><td>0.05 (-6.52%)</td><td>0.04 <b>(-21.57%)</b></td><td>0.03 (+8.07%)</td><td>0.02 (+2.49%)</td><td>558.30 (-7.46%)</td><td>429.56 (+7.10%)</td><td>459.30 <b>(+27.51%)</b></td><td>274.00 (+1.67%)</td><td>132.50 (-2.51%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.30 (n/a)</td><td>401.10 (n/a)</td><td>360.20 (n/a)</td><td>269.50 (n/a)</td><td>135.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 <b>(+27.66%)</b></td><td>0.05 (-13.52%)</td><td>0.03 <b>(-44.72%)</b></td><td>0.02 <b>(-34.48%)</b></td><td>0.03 <b>(+129.39%)</b></td><td>776.80 <b>(+52.61%)</b></td><td>484.88 <b>(+42.58%)</b></td><td>534.00 <b>(+80.89%)</b></td><td>210.90 <b>(-21.66%)</b></td><td>246.31 <b>(+153.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>509.00 (n/a)</td><td>340.08 (n/a)</td><td>295.20 (n/a)</td><td>269.20 (n/a)</td><td>97.09 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 <b>(+20.68%)</b></td><td>0.05 (+19.26%)</td><td>0.04 (+9.48%)</td><td>0.03 (+6.29%)</td><td>0.02 <b>(+29.62%)</b></td><td>560.90 (-5.92%)</td><td>413.14 (-13.35%)</td><td>475.80 (-8.66%)</td><td>201.60 (-17.14%)</td><td>144.32 (+5.44%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>596.20 (n/a)</td><td>476.80 (n/a)</td><td>520.90 (n/a)</td><td>243.30 (n/a)</td><td>136.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.36 <b>(-21.53%)</b></td><td>0.30 (+7.62%)</td><td>0.33 <b>(+58.23%)</b></td><td>0.21 (+3.44%)</td><td>0.07 <b>(-37.85%)</b></td><td>467.10 (-3.33%)</td><td>344.76 (-11.76%)</td><td>294.70 <b>(-36.79%)</b></td><td>272.50 <b>(+27.46%)</b></td><td>87.53 <b>(-26.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.46 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>483.20 (n/a)</td><td>390.70 (n/a)</td><td>466.20 (n/a)</td><td>213.80 (n/a)</td><td>118.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.37 (-17.00%)</td><td>0.28 (-6.48%)</td><td>0.35 <b>(+34.29%)</b></td><td>0.14 <b>(-21.67%)</b></td><td>0.12 (-4.06%)</td><td>681.80 <b>(+27.65%)</b></td><td>420.24 (+12.09%)</td><td>277.30 <b>(-25.54%)</b></td><td>263.40 <b>(+20.49%)</b></td><td>206.19 <b>(+43.46%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.45 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>534.10 (n/a)</td><td>374.92 (n/a)</td><td>372.40 (n/a)</td><td>218.60 (n/a)</td><td>143.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.43 <b>(+23.99%)</b></td><td>0.32 <b>(+37.07%)</b></td><td>0.35 <b>(+69.96%)</b></td><td>0.21 <b>(+59.28%)</b></td><td>0.10 (+3.59%)</td><td>472.30 <b>(-37.22%)</b></td><td>333.86 <b>(-30.92%)</b></td><td>277.50 <b>(-41.17%)</b></td><td>229.30 (-19.35%)</td><td>113.60 <b>(-43.26%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>752.30 (n/a)</td><td>483.32 (n/a)</td><td>471.70 (n/a)</td><td>284.30 (n/a)</td><td>200.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.23 <b>(-23.86%)</b></td><td>0.19 <b>(+23.89%)</b></td><td>0.22 <b>(+65.41%)</b></td><td>0.15 <b>(+54.81%)</b></td><td>0.04 <b>(-52.93%)</b></td><td>502.30 <b>(-35.41%)</b></td><td>393.86 <b>(-28.45%)</b></td><td>338.70 <b>(-39.55%)</b></td><td>318.80 <b>(+31.30%)</b></td><td>86.31 <b>(-55.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>777.70 (n/a)</td><td>550.50 (n/a)</td><td>560.30 (n/a)</td><td>242.80 (n/a)</td><td>195.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.32 <b>(+86.49%)</b></td><td>0.23 <b>(+49.12%)</b></td><td>0.26 <b>(+66.77%)</b></td><td>0.14 (+2.11%)</td><td>0.08 <b>(+381.83%)</b></td><td>519.40 (-2.07%)</td><td>349.08 <b>(-26.36%)</b></td><td>279.00 <b>(-40.04%)</b></td><td>226.90 <b>(-46.37%)</b></td><td>128.74 <b>(+159.67%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>530.40 (n/a)</td><td>474.04 (n/a)</td><td>465.30 (n/a)</td><td>423.10 (n/a)</td><td>49.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.21 (-12.96%)</td><td>0.14 <b>(-23.50%)</b></td><td>0.14 (-19.28%)</td><td>0.09 <b>(-35.74%)</b></td><td>0.04 (-7.10%)</td><td>778.10 <b>(+55.62%)</b></td><td>548.30 <b>(+33.31%)</b></td><td>544.60 <b>(+23.89%)</b></td><td>353.20 (+14.90%)</td><td>151.40 <b>(+65.25%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>500.00 (n/a)</td><td>411.30 (n/a)</td><td>439.60 (n/a)</td><td>307.40 (n/a)</td><td>91.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (-5.81%)</td><td>0.08 <b>(-27.84%)</b></td><td>0.07 <b>(-38.93%)</b></td><td>0.07 <b>(-21.13%)</b></td><td>0.03 <b>(+22.35%)</b></td><td>550.80 <b>(+26.80%)</b></td><td>461.96 <b>(+42.05%)</b></td><td>491.70 <b>(+63.74%)</b></td><td>286.50 (+6.15%)</td><td>101.79 <b>(+53.68%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>434.40 (n/a)</td><td>325.20 (n/a)</td><td>300.30 (n/a)</td><td>269.90 (n/a)</td><td>66.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (-9.09%)</td><td>0.11 (+6.74%)</td><td>0.11 <b>(+46.50%)</b></td><td>0.07 (-2.40%)</td><td>0.03 <b>(-29.37%)</b></td><td>556.00 (+2.45%)</td><td>370.92 (-10.10%)</td><td>322.40 <b>(-31.74%)</b></td><td>289.80 (+10.02%)</td><td>110.99 (-17.75%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>542.70 (n/a)</td><td>412.58 (n/a)</td><td>472.30 (n/a)</td><td>263.40 (n/a)</td><td>134.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 <b>(-46.48%)</b></td><td>0.06 <b>(-34.86%)</b></td><td>0.06 (-10.67%)</td><td>0.03 <b>(-45.32%)</b></td><td>0.02 <b>(-55.07%)</b></td><td>1072.10 <b>(+82.89%)</b></td><td>633.66 <b>(+47.29%)</b></td><td>573.30 (+11.93%)</td><td>411.00 <b>(+86.82%)</b></td><td>257.60 <b>(+59.76%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>586.20 (n/a)</td><td>430.20 (n/a)</td><td>512.20 (n/a)</td><td>220.00 (n/a)</td><td>161.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 <b>(-36.26%)</b></td><td>0.08 <b>(-23.08%)</b></td><td>0.07 (-4.93%)</td><td>0.07 (-7.97%)</td><td>0.03 <b>(-52.54%)</b></td><td>567.00 (+8.66%)</td><td>463.82 (+18.62%)</td><td>495.20 (+5.21%)</td><td>287.30 <b>(+56.91%)</b></td><td>114.90 (-19.95%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>521.80 (n/a)</td><td>391.02 (n/a)</td><td>470.70 (n/a)</td><td>183.10 (n/a)</td><td>143.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 <b>(-57.04%)</b></td><td>0.07 <b>(-41.24%)</b></td><td>0.07 (-5.68%)</td><td>0.03 <b>(+24.93%)</b></td><td>0.03 <b>(-65.99%)</b></td><td>1321.10 (-19.95%)</td><td>684.76 (+9.86%)</td><td>564.70 (+6.01%)</td><td>353.60 <b>(+132.78%)</b></td><td>389.68 <b>(-35.33%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.09 (n/a)</td><td>1650.30 (n/a)</td><td>623.30 (n/a)</td><td>532.70 (n/a)</td><td>151.90 (n/a)</td><td>602.59 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (+2.73%)</td><td>0.13 <b>(+48.83%)</b></td><td>0.12 <b>(+86.36%)</b></td><td>0.10 <b>(+55.87%)</b></td><td>0.02 <b>(-39.06%)</b></td><td>379.70 <b>(-35.85%)</b></td><td>299.08 <b>(-38.32%)</b></td><td>297.70 <b>(-46.34%)</b></td><td>236.70 (-2.63%)</td><td>56.33 <b>(-61.90%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>591.90 (n/a)</td><td>484.88 (n/a)</td><td>554.80 (n/a)</td><td>243.10 (n/a)</td><td>147.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (+10.08%)</td><td>0.11 (-1.37%)</td><td>0.08 (-11.09%)</td><td>0.08 (-3.10%)</td><td>0.04 <b>(+21.95%)</b></td><td>534.00 (+3.21%)</td><td>420.36 (+4.86%)</td><td>502.00 (+12.46%)</td><td>253.00 (-9.16%)</td><td>138.89 <b>(+22.60%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>517.40 (n/a)</td><td>400.86 (n/a)</td><td>446.40 (n/a)</td><td>278.50 (n/a)</td><td>113.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (+17.10%)</td><td>0.12 <b>(+33.08%)</b></td><td>0.13 <b>(+41.02%)</b></td><td>0.08 <b>(+104.99%)</b></td><td>0.04 (+6.02%)</td><td>540.80 <b>(-51.22%)</b></td><td>364.48 <b>(-32.31%)</b></td><td>305.90 <b>(-29.09%)</b></td><td>259.70 (-14.60%)</td><td>125.38 <b>(-61.25%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1108.60 (n/a)</td><td>538.42 (n/a)</td><td>431.40 (n/a)</td><td>304.10 (n/a)</td><td>323.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (-3.78%)</td><td>0.08 (-12.18%)</td><td>0.08 (+5.97%)</td><td>0.02 <b>(-75.61%)</b></td><td>0.05 <b>(+36.34%)</b></td><td>2441.60 <b>(+310.01%)</b></td><td>842.68 <b>(+80.31%)</b></td><td>493.50 (-5.62%)</td><td>272.30 (+3.93%)</td><td>901.86 <b>(+586.11%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>595.50 (n/a)</td><td>467.36 (n/a)</td><td>522.90 (n/a)</td><td>262.00 (n/a)</td><td>131.45 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (-19.57%)</td><td>0.10 (-9.97%)</td><td>0.09 (-13.84%)</td><td>0.08 (-4.56%)</td><td>0.02 <b>(-33.89%)</b></td><td>530.60 (+4.78%)</td><td>433.32 (+8.40%)</td><td>437.40 (+16.05%)</td><td>335.50 <b>(+24.31%)</b></td><td>83.86 (-17.40%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>506.40 (n/a)</td><td>399.76 (n/a)</td><td>376.90 (n/a)</td><td>269.90 (n/a)</td><td>101.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 <b>(-30.95%)</b></td><td>0.10 (-15.53%)</td><td>0.10 (-4.97%)</td><td>0.08 <b>(+22.92%)</b></td><td>0.01 <b>(-74.44%)</b></td><td>482.70 (-18.66%)</td><td>414.84 (+5.51%)</td><td>415.20 (+5.25%)</td><td>350.20 <b>(+44.83%)</b></td><td>48.72 <b>(-68.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>593.40 (n/a)</td><td>393.18 (n/a)</td><td>394.50 (n/a)</td><td>241.80 (n/a)</td><td>152.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.23 (+17.47%)</td><td>0.15 (+11.33%)</td><td>0.14 (-8.48%)</td><td>0.07 (+16.19%)</td><td>0.05 (+0.43%)</td><td>568.00 (-13.94%)</td><td>321.98 (-14.08%)</td><td>286.40 (+9.27%)</td><td>181.80 (-14.85%)</td><td>145.40 <b>(-23.31%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>660.00 (n/a)</td><td>374.76 (n/a)</td><td>262.10 (n/a)</td><td>213.50 (n/a)</td><td>189.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (-3.30%)</td><td>0.08 (+11.82%)</td><td>0.07 (+11.91%)</td><td>0.06 <b>(+300.12%)</b></td><td>0.03 <b>(-36.03%)</b></td><td>608.10 <b>(-75.01%)</b></td><td>471.58 <b>(-44.90%)</b></td><td>516.80 (-10.65%)</td><td>273.60 (+3.40%)</td><td>138.52 <b>(-84.55%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2433.00 (n/a)</td><td>855.84 (n/a)</td><td>578.40 (n/a)</td><td>264.60 (n/a)</td><td>896.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (-18.08%)</td><td>0.09 (-14.07%)</td><td>0.08 <b>(-30.74%)</b></td><td>0.06 (+18.13%)</td><td>0.03 (-17.45%)</td><td>571.10 (-15.35%)</td><td>417.80 (+11.65%)</td><td>435.50 <b>(+44.35%)</b></td><td>255.80 <b>(+22.04%)</b></td><td>144.78 (-19.26%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>674.70 (n/a)</td><td>374.22 (n/a)</td><td>301.70 (n/a)</td><td>209.60 (n/a)</td><td>179.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 <b>(+32.56%)</b></td><td>0.11 <b>(+54.71%)</b></td><td>0.12 <b>(+70.13%)</b></td><td>0.06 <b>(+220.29%)</b></td><td>0.05 <b>(+21.81%)</b></td><td>590.90 <b>(-68.78%)</b></td><td>389.78 <b>(-48.07%)</b></td><td>300.30 <b>(-41.22%)</b></td><td>216.40 <b>(-24.57%)</b></td><td>180.81 <b>(-72.14%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1892.60 (n/a)</td><td>750.62 (n/a)</td><td>510.90 (n/a)</td><td>286.90 (n/a)</td><td>648.95 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 <b>(+39.15%)</b></td><td>0.08 (+9.77%)</td><td>0.07 (-1.34%)</td><td>0.06 (+1.52%)</td><td>0.03 <b>(+96.56%)</b></td><td>570.40 (-1.50%)</td><td>470.02 (-3.98%)</td><td>527.80 (+1.36%)</td><td>263.80 <b>(-28.14%)</b></td><td>130.76 <b>(+38.46%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>579.10 (n/a)</td><td>489.52 (n/a)</td><td>520.70 (n/a)</td><td>367.10 (n/a)</td><td>94.44 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 <b>(-33.66%)</b></td><td>0.10 (+4.17%)</td><td>0.11 <b>(+48.63%)</b></td><td>0.08 <b>(+41.00%)</b></td><td>0.02 <b>(-66.66%)</b></td><td>451.00 <b>(-29.08%)</b></td><td>344.48 (-17.62%)</td><td>309.10 <b>(-32.72%)</b></td><td>295.20 <b>(+50.77%)</b></td><td>64.51 <b>(-63.36%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>635.90 (n/a)</td><td>418.14 (n/a)</td><td>459.40 (n/a)</td><td>195.80 (n/a)</td><td>176.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 <b>(+76.02%)</b></td><td>0.09 <b>(+41.15%)</b></td><td>0.08 <b>(+27.87%)</b></td><td>0.04 <b>(-22.54%)</b></td><td>0.04 <b>(+294.40%)</b></td><td>805.20 <b>(+29.10%)</b></td><td>463.40 (-15.53%)</td><td>444.40 <b>(-21.79%)</b></td><td>238.40 <b>(-43.18%)</b></td><td>230.02 <b>(+180.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>623.70 (n/a)</td><td>548.58 (n/a)</td><td>568.20 (n/a)</td><td>419.60 (n/a)</td><td>82.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.27 <b>(-42.01%)</b></td><td>0.18 <b>(-45.41%)</b></td><td>0.22 <b>(-42.14%)</b></td><td>0.07 <b>(+25.59%)</b></td><td>0.08 <b>(-49.95%)</b></td><td>1964.00 <b>(-20.37%)</b></td><td>918.58 <b>(+22.02%)</b></td><td>601.10 <b>(+72.83%)</b></td><td>482.20 <b>(+72.46%)</b></td><td>615.04 <b>(-35.84%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.38 (n/a)</td><td>0.05 (n/a)</td><td>0.17 (n/a)</td><td>2466.50 (n/a)</td><td>752.80 (n/a)</td><td>347.80 (n/a)</td><td>279.60 (n/a)</td><td>958.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.52 (-5.81%)</td><td>0.30 <b>(-32.61%)</b></td><td>0.25 <b>(-41.03%)</b></td><td>0.23 <b>(-33.93%)</b></td><td>0.13 <b>(+53.47%)</b></td><td>579.70 <b>(+51.36%)</b></td><td>479.64 <b>(+58.74%)</b></td><td>517.30 <b>(+69.55%)</b></td><td>250.50 (+6.14%)</td><td>130.83 <b>(+133.46%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>383.00 (n/a)</td><td>302.16 (n/a)</td><td>305.10 (n/a)</td><td>236.00 (n/a)</td><td>56.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.48 <b>(+23.78%)</b></td><td>0.27 (-7.24%)</td><td>0.25 (-10.68%)</td><td>0.17 <b>(-21.61%)</b></td><td>0.12 <b>(+81.83%)</b></td><td>780.30 <b>(+27.56%)</b></td><td>548.62 (+17.55%)</td><td>526.10 (+11.96%)</td><td>274.10 (-19.22%)</td><td>193.21 <b>(+82.49%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>611.70 (n/a)</td><td>466.72 (n/a)</td><td>469.90 (n/a)</td><td>339.30 (n/a)</td><td>105.87 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/strided_copy</summary>


### test_strided_copy[chunked_transfer]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+11.24%)</td><td>0.01 (-1.76%)</td><td>0.01 (-2.92%)</td><td>0.01 (-18.04%)</td><td>0.00 <b>(+61.81%)</b></td><td>541.50 <b>(+22.01%)</b></td><td>377.62 (+9.77%)</td><td>319.60 (+3.03%)</td><td>245.40 (-10.11%)</td><td>146.14 <b>(+82.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>443.80 (n/a)</td><td>344.00 (n/a)</td><td>310.20 (n/a)</td><td>273.00 (n/a)</td><td>80.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[contiguous]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+9.26%)</td><td>0.01 (+11.24%)</td><td>0.01 (-6.78%)</td><td>0.01 <b>(+62.67%)</b></td><td>0.00 <b>(-20.44%)</b></td><td>393.70 <b>(-38.53%)</b></td><td>286.14 (-17.49%)</td><td>291.80 (+7.28%)</td><td>206.10 (-8.48%)</td><td>70.34 <b>(-58.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>640.50 (n/a)</td><td>346.80 (n/a)</td><td>272.00 (n/a)</td><td>225.20 (n/a)</td><td>168.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 <b>(+20.07%)</b></td><td>0.01 (+8.97%)</td><td>0.01 (+6.05%)</td><td>0.01 (+6.84%)</td><td>0.00 <b>(+23.01%)</b></td><td>449.80 (-6.39%)</td><td>346.54 (-7.33%)</td><td>299.40 (-5.70%)</td><td>251.70 (-16.74%)</td><td>90.63 (+0.69%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.50 (n/a)</td><td>373.96 (n/a)</td><td>317.50 (n/a)</td><td>302.30 (n/a)</td><td>90.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_llama_full]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>10.06 <b>(+38.25%)</b></td><td>6.42 <b>(+28.49%)</b></td><td>4.91 (-3.02%)</td><td>4.09 <b>(+297.62%)</b></td><td>2.65 (+3.34%)</td><td>512.70 <b>(-74.85%)</b></td><td>370.08 <b>(-47.27%)</b></td><td>427.10 (+3.11%)</td><td>208.50 <b>(-27.68%)</b></td><td>133.47 <b>(-82.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>7.28 (n/a)</td><td>5.00 (n/a)</td><td>5.07 (n/a)</td><td>1.03 (n/a)</td><td>2.57 (n/a)</td><td>2038.50 (n/a)</td><td>701.86 (n/a)</td><td>414.20 (n/a)</td><td>288.30 (n/a)</td><td>751.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.53 (+12.82%)</td><td>0.41 (+6.46%)</td><td>0.43 (-6.70%)</td><td>0.27 (+3.95%)</td><td>0.11 (+5.42%)</td><td>490.60 (-3.79%)</td><td>347.28 (-6.50%)</td><td>310.00 (+7.16%)</td><td>249.40 (-11.34%)</td><td>104.91 (-10.31%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.47 (n/a)</td><td>0.38 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>509.90 (n/a)</td><td>371.42 (n/a)</td><td>289.30 (n/a)</td><td>281.30 (n/a)</td><td>116.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.52 (+13.92%)</td><td>0.35 (-2.16%)</td><td>0.28 <b>(-24.01%)</b></td><td>0.24 (-7.35%)</td><td>0.12 <b>(+67.14%)</b></td><td>541.90 (+7.93%)</td><td>408.94 (+7.63%)</td><td>464.00 <b>(+31.59%)</b></td><td>255.30 (-12.24%)</td><td>124.31 <b>(+54.21%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.45 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>502.10 (n/a)</td><td>379.96 (n/a)</td><td>352.60 (n/a)</td><td>290.90 (n/a)</td><td>80.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.51 (-2.84%)</td><td>0.34 (-14.65%)</td><td>0.28 <b>(-28.73%)</b></td><td>0.22 (-13.93%)</td><td>0.12 <b>(+23.37%)</b></td><td>599.60 (+16.18%)</td><td>427.12 <b>(+22.08%)</b></td><td>479.40 <b>(+40.30%)</b></td><td>260.90 (+2.92%)</td><td>142.04 <b>(+39.95%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>516.10 (n/a)</td><td>349.86 (n/a)</td><td>341.70 (n/a)</td><td>253.50 (n/a)</td><td>101.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.56 <b>(+25.67%)</b></td><td>0.43 <b>(+24.42%)</b></td><td>0.45 <b>(+27.70%)</b></td><td>0.25 (+6.07%)</td><td>0.12 (+14.87%)</td><td>528.20 (-5.71%)</td><td>332.62 (-19.56%)</td><td>292.80 <b>(-21.69%)</b></td><td>235.30 <b>(-20.43%)</b></td><td>115.96 (-10.38%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>560.20 (n/a)</td><td>413.50 (n/a)</td><td>373.90 (n/a)</td><td>295.70 (n/a)</td><td>129.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot_last]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.55 (+15.99%)</td><td>0.44 (+6.76%)</td><td>0.45 (-1.07%)</td><td>0.27 (-8.80%)</td><td>0.12 <b>(+44.33%)</b></td><td>491.60 (+9.66%)</td><td>320.34 (-3.19%)</td><td>292.20 (+1.07%)</td><td>239.70 (-13.78%)</td><td>102.80 <b>(+39.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>448.30 (n/a)</td><td>330.90 (n/a)</td><td>289.10 (n/a)</td><td>278.00 (n/a)</td><td>73.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (-5.15%)</td><td>0.01 (-14.61%)</td><td>0.01 (+0.89%)</td><td>0.01 <b>(-33.37%)</b></td><td>0.00 <b>(+82.07%)</b></td><td>480.10 <b>(+50.08%)</b></td><td>345.36 <b>(+25.92%)</b></td><td>288.50 (-0.89%)</td><td>237.70 (+5.41%)</td><td>118.19 <b>(+202.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>319.90 (n/a)</td><td>274.28 (n/a)</td><td>291.10 (n/a)</td><td>225.50 (n/a)</td><td>39.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels_chunked]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (+12.61%)</td><td>0.01 (-5.64%)</td><td>0.01 <b>(-37.03%)</b></td><td>0.01 (-16.99%)</td><td>0.00 <b>(+44.33%)</b></td><td>612.90 <b>(+20.46%)</b></td><td>425.90 (+14.01%)</td><td>492.80 <b>(+58.81%)</b></td><td>235.00 (-11.19%)</td><td>167.91 <b>(+42.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.80 (n/a)</td><td>373.58 (n/a)</td><td>310.30 (n/a)</td><td>264.60 (n/a)</td><td>118.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-53.29%)</b></td><td>17985.96 (-17.09%)</td><td>14201.71 (+7.58%)</td><td>15887.83 (+9.87%)</td><td>7633.89 <b>(+26.67%)</b></td><td>4005.09 <b>(-40.34%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21693.04 (n/a)</td><td>13200.60 (n/a)</td><td>14460.33 (n/a)</td><td>6026.43 (n/a)</td><td>6713.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.00 (+0.00%)</td><td>0.00 (-3.45%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+5.13%)</td><td>20530.42 (+6.61%)</td><td>16616.43 (+3.57%)</td><td>17241.04 (-1.14%)</td><td>8165.72 (+0.57%)</td><td>5031.60 (+11.89%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19257.90 (n/a)</td><td>16043.83 (n/a)</td><td>17439.10 (n/a)</td><td>8119.11 (n/a)</td><td>4496.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (-0.14%)</td><td>0.10 (+12.83%)</td><td>0.09 (+8.51%)</td><td>0.07 (-1.99%)</td><td>0.03 (+17.17%)</td><td>28430.84 (+2.09%)</td><td>21848.04 (-9.39%)</td><td>24195.90 (-7.76%)</td><td>14747.17 (+0.13%)</td><td>6419.87 <b>(+20.72%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27848.51 (n/a)</td><td>24111.21 (n/a)</td><td>26231.06 (n/a)</td><td>14728.32 (n/a)</td><td>5317.83 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.71 (+3.59%)</td><td>1.85 <b>(+46.45%)</b></td><td>2.38 <b>(+142.65%)</b></td><td>0.30 (-0.03%)</td><td>1.05 (-0.38%)</td><td>3514.50 (+0.03%)</td><td>1117.64 <b>(-36.08%)</b></td><td>440.60 <b>(-58.79%)</b></td><td>386.80 (-3.44%)</td><td>1353.26 (-10.92%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.62 (n/a)</td><td>1.26 (n/a)</td><td>0.98 (n/a)</td><td>0.30 (n/a)</td><td>1.05 (n/a)</td><td>3513.50 (n/a)</td><td>1748.44 (n/a)</td><td>1069.10 (n/a)</td><td>400.60 (n/a)</td><td>1519.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.98 (-16.55%)</td><td>1.52 <b>(-20.05%)</b></td><td>1.81 (+10.46%)</td><td>0.33 <b>(-68.82%)</b></td><td>1.07 (+9.47%)</td><td>3196.20 <b>(+220.71%)</b></td><td>1278.26 <b>(+96.91%)</b></td><td>579.30 (-9.47%)</td><td>351.70 (+19.83%)</td><td>1193.91 <b>(+372.39%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.57 (n/a)</td><td>1.90 (n/a)</td><td>1.64 (n/a)</td><td>1.05 (n/a)</td><td>0.97 (n/a)</td><td>996.60 (n/a)</td><td>649.16 (n/a)</td><td>639.90 (n/a)</td><td>293.50 (n/a)</td><td>252.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.11 (-11.98%)</td><td>1.49 (-15.43%)</td><td>1.43 (-4.69%)</td><td>0.30 <b>(-67.49%)</b></td><td>1.02 (-2.46%)</td><td>3447.00 <b>(+207.55%)</b></td><td>1227.48 <b>(+67.01%)</b></td><td>735.60 (+4.92%)</td><td>336.80 (+13.59%)</td><td>1257.31 <b>(+291.48%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.54 (n/a)</td><td>1.76 (n/a)</td><td>1.50 (n/a)</td><td>0.94 (n/a)</td><td>1.04 (n/a)</td><td>1120.80 (n/a)</td><td>734.98 (n/a)</td><td>701.10 (n/a)</td><td>296.50 (n/a)</td><td>321.17 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.73 <b>(+41.49%)</b></td><td>2.44 <b>(+32.19%)</b></td><td>2.43 <b>(+37.46%)</b></td><td>1.67 <b>(+47.11%)</b></td><td>0.84 <b>(+44.07%)</b></td><td>626.40 <b>(-32.02%)</b></td><td>468.28 <b>(-24.09%)</b></td><td>430.80 <b>(-27.25%)</b></td><td>281.10 <b>(-29.32%)</b></td><td>146.47 <b>(-27.94%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.64 (n/a)</td><td>1.85 (n/a)</td><td>1.77 (n/a)</td><td>1.14 (n/a)</td><td>0.58 (n/a)</td><td>921.50 (n/a)</td><td>616.92 (n/a)</td><td>592.20 (n/a)</td><td>397.70 (n/a)</td><td>203.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>4.33 (+5.90%)</td><td>1.78 (+17.42%)</td><td>0.96 (-4.06%)</td><td>0.59 (-5.03%)</td><td>1.61 (+10.52%)</td><td>3525.20 (+5.30%)</td><td>2094.38 (-2.52%)</td><td>2175.20 (+4.23%)</td><td>484.10 (-5.58%)</td><td>1405.38 <b>(+25.78%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>4.09 (n/a)</td><td>1.52 (n/a)</td><td>1.00 (n/a)</td><td>0.63 (n/a)</td><td>1.45 (n/a)</td><td>3347.80 (n/a)</td><td>2148.42 (n/a)</td><td>2086.90 (n/a)</td><td>512.70 (n/a)</td><td>1117.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.01 (-14.04%)</td><td>3.22 <b>(-26.11%)</b></td><td>3.79 (-16.54%)</td><td>0.60 <b>(-77.44%)</b></td><td>1.70 <b>(+22.26%)</b></td><td>3485.20 <b>(+343.35%)</b></td><td>1154.86 <b>(+118.97%)</b></td><td>553.00 (+19.83%)</td><td>418.20 (+16.33%)</td><td>1310.58 <b>(+609.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.83 (n/a)</td><td>4.36 (n/a)</td><td>4.54 (n/a)</td><td>2.67 (n/a)</td><td>1.39 (n/a)</td><td>786.10 (n/a)</td><td>527.40 (n/a)</td><td>461.50 (n/a)</td><td>359.50 (n/a)</td><td>184.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.86 (-3.18%)</td><td>3.39 (-13.29%)</td><td>2.83 <b>(-24.50%)</b></td><td>1.00 <b>(-57.64%)</b></td><td>2.05 <b>(+52.98%)</b></td><td>2102.10 <b>(+136.08%)</b></td><td>920.28 <b>(+56.78%)</b></td><td>740.20 <b>(+32.46%)</b></td><td>357.80 (+3.29%)</td><td>709.49 <b>(+262.90%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.05 (n/a)</td><td>3.91 (n/a)</td><td>3.75 (n/a)</td><td>2.36 (n/a)</td><td>1.34 (n/a)</td><td>890.40 (n/a)</td><td>587.00 (n/a)</td><td>558.80 (n/a)</td><td>346.40 (n/a)</td><td>195.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.67 (-1.22%)</td><td>3.84 <b>(+22.18%)</b></td><td>4.83 <b>(+78.33%)</b></td><td>0.59 (-0.69%)</td><td>2.52 (+8.23%)</td><td>3576.70 (+0.69%)</td><td>1168.18 (-7.27%)</td><td>434.60 <b>(-43.93%)</b></td><td>314.40 (+1.26%)</td><td>1384.10 (+5.28%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.75 (n/a)</td><td>3.15 (n/a)</td><td>2.71 (n/a)</td><td>0.59 (n/a)</td><td>2.33 (n/a)</td><td>3552.20 (n/a)</td><td>1259.70 (n/a)</td><td>775.10 (n/a)</td><td>310.50 (n/a)</td><td>1314.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.09 <b>(+60.37%)</b></td><td>3.49 <b>(+23.69%)</b></td><td>3.33 (+19.10%)</td><td>0.60 <b>(-70.47%)</b></td><td>2.08 <b>(+230.13%)</b></td><td>3476.80 <b>(+238.64%)</b></td><td>1133.56 <b>(+46.83%)</b></td><td>629.30 (-16.04%)</td><td>344.20 <b>(-37.64%)</b></td><td>1320.36 <b>(+680.35%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.80 (n/a)</td><td>2.82 (n/a)</td><td>2.80 (n/a)</td><td>2.04 (n/a)</td><td>0.63 (n/a)</td><td>1026.70 (n/a)</td><td>772.00 (n/a)</td><td>749.50 (n/a)</td><td>552.00 (n/a)</td><td>169.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.02 <b>(-20.43%)</b></td><td>2.79 <b>(-26.93%)</b></td><td>2.82 <b>(-21.68%)</b></td><td>0.58 <b>(-65.56%)</b></td><td>2.04 (+15.64%)</td><td>3594.10 <b>(+190.39%)</b></td><td>1502.50 <b>(+124.46%)</b></td><td>742.50 <b>(+27.69%)</b></td><td>418.00 <b>(+25.68%)</b></td><td>1402.26 <b>(+297.44%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.31 (n/a)</td><td>3.82 (n/a)</td><td>3.61 (n/a)</td><td>1.69 (n/a)</td><td>1.76 (n/a)</td><td>1237.70 (n/a)</td><td>669.38 (n/a)</td><td>581.50 (n/a)</td><td>332.60 (n/a)</td><td>352.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.38 (+4.29%)</td><td>4.88 (+16.25%)</td><td>4.94 <b>(+27.24%)</b></td><td>4.03 (+18.56%)</td><td>0.52 <b>(-26.85%)</b></td><td>1041.00 (-15.65%)</td><td>867.98 (-15.02%)</td><td>848.70 <b>(-21.41%)</b></td><td>779.20 (-4.12%)</td><td>102.15 <b>(-38.94%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.16 (n/a)</td><td>4.20 (n/a)</td><td>3.88 (n/a)</td><td>3.40 (n/a)</td><td>0.71 (n/a)</td><td>1234.20 (n/a)</td><td>1021.42 (n/a)</td><td>1079.90 (n/a)</td><td>812.70 (n/a)</td><td>167.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>7.57 (-1.65%)</td><td>4.83 (+17.47%)</td><td>4.34 <b>(+21.09%)</b></td><td>1.68 <b>(+30.42%)</b></td><td>2.33 (-13.63%)</td><td>2496.30 <b>(-23.32%)</b></td><td>1143.62 <b>(-26.38%)</b></td><td>966.60 (-17.42%)</td><td>554.00 (+1.67%)</td><td>786.38 <b>(-30.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>7.70 (n/a)</td><td>4.11 (n/a)</td><td>3.58 (n/a)</td><td>1.29 (n/a)</td><td>2.69 (n/a)</td><td>3255.60 (n/a)</td><td>1553.34 (n/a)</td><td>1170.50 (n/a)</td><td>544.90 (n/a)</td><td>1126.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>8.52 (-0.62%)</td><td>5.31 <b>(+36.58%)</b></td><td>4.07 (+4.77%)</td><td>3.81 <b>(+201.29%)</b></td><td>2.05 <b>(-29.46%)</b></td><td>1099.80 <b>(-66.81%)</b></td><td>873.14 <b>(-48.23%)</b></td><td>1031.70 (-4.54%)</td><td>492.20 (+0.61%)</td><td>273.06 <b>(-76.82%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>8.57 (n/a)</td><td>3.89 (n/a)</td><td>3.88 (n/a)</td><td>1.27 (n/a)</td><td>2.91 (n/a)</td><td>3313.60 (n/a)</td><td>1686.46 (n/a)</td><td>1080.80 (n/a)</td><td>489.20 (n/a)</td><td>1177.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>7.99 (-12.74%)</td><td>6.07 <b>(+21.74%)</b></td><td>7.27 <b>(+66.28%)</b></td><td>3.53 <b>(+110.33%)</b></td><td>2.11 <b>(-24.52%)</b></td><td>1187.40 <b>(-52.46%)</b></td><td>777.18 <b>(-32.27%)</b></td><td>576.60 <b>(-39.86%)</b></td><td>525.20 (+14.60%)</td><td>311.66 <b>(-60.84%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.15 (n/a)</td><td>4.99 (n/a)</td><td>4.37 (n/a)</td><td>1.68 (n/a)</td><td>2.79 (n/a)</td><td>2497.60 (n/a)</td><td>1147.54 (n/a)</td><td>958.70 (n/a)</td><td>458.30 (n/a)</td><td>795.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>10.31 (+4.53%)</td><td>5.26 <b>(-26.62%)</b></td><td>5.00 <b>(-24.49%)</b></td><td>1.16 <b>(-76.35%)</b></td><td>3.95 <b>(+109.53%)</b></td><td>3606.10 <b>(+322.80%)</b></td><td>1546.32 <b>(+150.28%)</b></td><td>838.80 <b>(+32.43%)</b></td><td>406.70 (-4.35%)</td><td>1392.57 <b>(+760.99%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.87 (n/a)</td><td>7.17 (n/a)</td><td>6.62 (n/a)</td><td>4.92 (n/a)</td><td>1.88 (n/a)</td><td>852.90 (n/a)</td><td>617.84 (n/a)</td><td>633.40 (n/a)</td><td>425.20 (n/a)</td><td>161.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>9.48 (+0.06%)</td><td>6.94 (-3.04%)</td><td>8.02 (+14.30%)</td><td>3.52 (-14.60%)</td><td>2.52 <b>(+27.10%)</b></td><td>1193.10 (+17.09%)</td><td>693.62 (+9.39%)</td><td>522.70 (-12.50%)</td><td>442.30 (-0.05%)</td><td>316.23 <b>(+40.64%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.48 (n/a)</td><td>7.16 (n/a)</td><td>7.02 (n/a)</td><td>4.12 (n/a)</td><td>1.98 (n/a)</td><td>1019.00 (n/a)</td><td>634.10 (n/a)</td><td>597.40 (n/a)</td><td>442.50 (n/a)</td><td>224.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.64 (-12.83%)</td><td>1.43 (+17.58%)</td><td>1.56 <b>(+36.60%)</b></td><td>0.87 <b>(+21.75%)</b></td><td>0.32 <b>(-37.17%)</b></td><td>600.10 (-17.86%)</td><td>388.52 <b>(-21.90%)</b></td><td>336.10 <b>(-26.78%)</b></td><td>319.70 (+14.75%)</td><td>119.20 <b>(-41.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>1.88 (n/a)</td><td>1.21 (n/a)</td><td>1.14 (n/a)</td><td>0.72 (n/a)</td><td>0.50 (n/a)</td><td>730.60 (n/a)</td><td>497.46 (n/a)</td><td>459.00 (n/a)</td><td>278.60 (n/a)</td><td>202.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.53 (+12.93%)</td><td>1.89 <b>(+60.55%)</b></td><td>1.76 (+17.56%)</td><td>1.61 <b>(+424.02%)</b></td><td>0.37 <b>(-55.64%)</b></td><td>650.20 <b>(-80.92%)</b></td><td>571.04 <b>(-66.80%)</b></td><td>595.20 (-14.93%)</td><td>413.80 (-11.45%)</td><td>93.68 <b>(-93.79%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.24 (n/a)</td><td>1.17 (n/a)</td><td>1.50 (n/a)</td><td>0.31 (n/a)</td><td>0.84 (n/a)</td><td>3407.10 (n/a)</td><td>1720.08 (n/a)</td><td>699.70 (n/a)</td><td>467.30 (n/a)</td><td>1507.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.71 <b>(-27.57%)</b></td><td>2.04 (-7.58%)</td><td>2.30 (-3.88%)</td><td>0.59 (-3.78%)</td><td>0.83 <b>(-37.97%)</b></td><td>3548.10 (+3.93%)</td><td>1412.52 (-5.03%)</td><td>913.60 (+4.04%)</td><td>772.70 <b>(+38.06%)</b></td><td>1195.46 (-0.94%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.75 (n/a)</td><td>2.21 (n/a)</td><td>2.39 (n/a)</td><td>0.61 (n/a)</td><td>1.34 (n/a)</td><td>3414.00 (n/a)</td><td>1487.28 (n/a)</td><td>878.10 (n/a)</td><td>559.70 (n/a)</td><td>1206.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.78 (+7.72%)</td><td>1.25 (+2.08%)</td><td>1.63 <b>(+60.66%)</b></td><td>0.27 <b>(-70.88%)</b></td><td>0.66 <b>(+85.31%)</b></td><td>1921.30 <b>(+243.46%)</b></td><td>688.80 <b>(+51.38%)</b></td><td>321.60 <b>(-37.76%)</b></td><td>295.30 (-7.17%)</td><td>700.40 <b>(+486.26%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>1.65 (n/a)</td><td>1.23 (n/a)</td><td>1.01 (n/a)</td><td>0.94 (n/a)</td><td>0.35 (n/a)</td><td>559.40 (n/a)</td><td>455.02 (n/a)</td><td>516.70 (n/a)</td><td>318.10 (n/a)</td><td>119.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (-13.19%)</td><td>0.08 (-1.02%)</td><td>0.09 <b>(+21.90%)</b></td><td>0.02 <b>(-65.20%)</b></td><td>0.04 <b>(+21.20%)</b></td><td>1907.10 <b>(+187.39%)</b></td><td>667.24 <b>(+47.18%)</b></td><td>366.90 (-17.97%)</td><td>281.00 (+15.21%)</td><td>696.60 <b>(+363.74%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>663.60 (n/a)</td><td>453.34 (n/a)</td><td>447.30 (n/a)</td><td>243.90 (n/a)</td><td>150.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (+2.92%)</td><td>0.08 <b>(-25.38%)</b></td><td>0.07 <b>(-37.02%)</b></td><td>0.03 <b>(-58.41%)</b></td><td>0.05 <b>(+64.04%)</b></td><td>1107.00 <b>(+140.50%)</b></td><td>528.08 <b>(+69.38%)</b></td><td>471.00 <b>(+58.75%)</b></td><td>222.70 (-2.84%)</td><td>347.38 <b>(+282.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>460.30 (n/a)</td><td>311.78 (n/a)</td><td>296.70 (n/a)</td><td>229.20 (n/a)</td><td>90.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.25 (-9.32%)</td><td>0.21 (-5.16%)</td><td>0.21 (-4.20%)</td><td>0.14 (-5.78%)</td><td>0.04 (-13.58%)</td><td>456.10 (+6.12%)</td><td>320.46 (+4.96%)</td><td>304.90 (+4.38%)</td><td>257.50 (+10.28%)</td><td>79.13 (+2.90%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>429.80 (n/a)</td><td>305.32 (n/a)</td><td>292.10 (n/a)</td><td>233.50 (n/a)</td><td>76.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.25 (-5.63%)</td><td>0.18 (-6.68%)</td><td>0.21 (-8.53%)</td><td>0.09 (-12.88%)</td><td>0.07 (+1.56%)</td><td>706.40 (+14.79%)</td><td>411.12 (+9.96%)</td><td>306.40 (+9.31%)</td><td>263.00 (+5.96%)</td><td>190.93 <b>(+21.74%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>615.40 (n/a)</td><td>373.88 (n/a)</td><td>280.30 (n/a)</td><td>248.20 (n/a)</td><td>156.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.33 <b>(+47.41%)</b></td><td>0.17 (-0.74%)</td><td>0.14 <b>(-28.61%)</b></td><td>0.11 (-9.93%)</td><td>0.09 <b>(+83.97%)</b></td><td>623.90 (+11.03%)</td><td>435.02 (+8.89%)</td><td>465.80 <b>(+40.09%)</b></td><td>198.30 <b>(-32.16%)</b></td><td>153.21 <b>(+25.47%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>561.90 (n/a)</td><td>399.50 (n/a)</td><td>332.50 (n/a)</td><td>292.30 (n/a)</td><td>122.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.51 (+0.54%)</td><td>0.38 (-1.04%)</td><td>0.46 (+8.88%)</td><td>0.21 (-19.85%)</td><td>0.16 <b>(+46.05%)</b></td><td>631.60 <b>(+24.77%)</b></td><td>405.68 (+11.72%)</td><td>287.30 (-8.15%)</td><td>254.70 (-0.55%)</td><td>192.51 <b>(+78.02%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>506.20 (n/a)</td><td>363.12 (n/a)</td><td>312.80 (n/a)</td><td>256.10 (n/a)</td><td>108.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.59 (+7.62%)</td><td>0.39 <b>(+20.32%)</b></td><td>0.38 <b>(+39.41%)</b></td><td>0.25 (+11.64%)</td><td>0.13 (+0.95%)</td><td>531.50 (-10.42%)</td><td>366.92 (-17.75%)</td><td>340.70 <b>(-28.27%)</b></td><td>223.20 (-7.08%)</td><td>118.33 (-11.23%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.55 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>593.30 (n/a)</td><td>446.08 (n/a)</td><td>475.00 (n/a)</td><td>240.20 (n/a)</td><td>133.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.54 (+1.11%)</td><td>0.36 (+9.90%)</td><td>0.35 <b>(+31.82%)</b></td><td>0.24 (+12.92%)</td><td>0.12 (-7.18%)</td><td>556.40 (-11.43%)</td><td>396.18 (-10.99%)</td><td>371.00 <b>(-24.15%)</b></td><td>241.30 (-1.07%)</td><td>125.82 (-15.45%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.54 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>628.20 (n/a)</td><td>445.10 (n/a)</td><td>489.10 (n/a)</td><td>243.90 (n/a)</td><td>148.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (+6.22%)</td><td>0.04 (-18.44%)</td><td>0.04 <b>(-31.38%)</b></td><td>0.03 <b>(-27.69%)</b></td><td>0.02 <b>(+35.16%)</b></td><td>622.10 <b>(+38.31%)</b></td><td>423.70 <b>(+32.16%)</b></td><td>394.80 <b>(+45.74%)</b></td><td>229.20 (-5.87%)</td><td>164.62 <b>(+81.80%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>449.80 (n/a)</td><td>320.60 (n/a)</td><td>270.90 (n/a)</td><td>243.50 (n/a)</td><td>90.55 (n/a)</td>
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
