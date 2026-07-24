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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-11.82%)</td><td>0.02 (-16.98%)</td><td>0.02 <b>(-22.63%)</b></td><td>0.01 <b>(-28.42%)</b></td><td>0.01 (+9.36%)</td><td>627.70 <b>(+39.71%)</b></td><td>406.88 <b>(+25.64%)</b></td><td>374.40 <b>(+29.28%)</b></td><td>261.40 (+13.41%)</td><td>144.93 <b>(+71.33%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.30 (n/a)</td><td>323.84 (n/a)</td><td>289.60 (n/a)</td><td>230.50 (n/a)</td><td>84.59 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-3.02%)</td><td>0.02 <b>(+26.70%)</b></td><td>0.03 <b>(+99.77%)</b></td><td>0.01 (-0.49%)</td><td>0.01 (-16.49%)</td><td>529.50 (+0.49%)</td><td>308.84 <b>(-23.84%)</b></td><td>244.00 <b>(-49.94%)</b></td><td>238.60 (+3.11%)</td><td>125.29 (-14.54%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>526.90 (n/a)</td><td>405.54 (n/a)</td><td>487.40 (n/a)</td><td>231.40 (n/a)</td><td>146.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 <b>(+29.35%)</b></td><td>0.02 (+17.86%)</td><td>0.02 <b>(+41.52%)</b></td><td>0.01 <b>(-42.98%)</b></td><td>0.01 <b>(+56.24%)</b></td><td>1073.50 <b>(+75.35%)</b></td><td>452.58 (+6.93%)</td><td>258.90 <b>(-29.34%)</b></td><td>199.80 <b>(-22.68%)</b></td><td>364.35 <b>(+109.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.20 (n/a)</td><td>423.26 (n/a)</td><td>366.40 (n/a)</td><td>258.40 (n/a)</td><td>173.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+19.76%)</td><td>0.02 (-9.56%)</td><td>0.01 (-18.29%)</td><td>0.01 (-0.07%)</td><td>0.01 <b>(+32.29%)</b></td><td>564.30 (+0.07%)</td><td>454.12 (+15.91%)</td><td>525.30 <b>(+22.39%)</b></td><td>200.10 (-16.49%)</td><td>151.76 (+12.14%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.90 (n/a)</td><td>391.80 (n/a)</td><td>429.20 (n/a)</td><td>239.60 (n/a)</td><td>135.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 <b>(+49.88%)</b></td><td>0.02 (+15.47%)</td><td>0.01 (+7.82%)</td><td>0.01 (-15.01%)</td><td>0.01 <b>(+97.06%)</b></td><td>694.80 (+17.66%)</td><td>446.20 (-4.89%)</td><td>482.50 (-7.25%)</td><td>231.70 <b>(-33.27%)</b></td><td>179.29 <b>(+58.02%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.50 (n/a)</td><td>469.14 (n/a)</td><td>520.20 (n/a)</td><td>347.20 (n/a)</td><td>113.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 <b>(+20.16%)</b></td><td>0.01 (-17.73%)</td><td>0.01 <b>(-31.47%)</b></td><td>0.01 <b>(-45.68%)</b></td><td>0.01 <b>(+82.48%)</b></td><td>978.60 <b>(+84.09%)</b></td><td>567.24 <b>(+47.92%)</b></td><td>492.40 <b>(+45.94%)</b></td><td>242.10 (-16.78%)</td><td>305.16 <b>(+187.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.60 (n/a)</td><td>383.48 (n/a)</td><td>337.40 (n/a)</td><td>290.90 (n/a)</td><td>106.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 <b>(+36.10%)</b></td><td>0.04 (-15.40%)</td><td>0.03 <b>(-41.75%)</b></td><td>0.01 <b>(-34.81%)</b></td><td>0.02 <b>(+87.26%)</b></td><td>831.40 <b>(+53.39%)</b></td><td>443.56 <b>(+40.61%)</b></td><td>450.50 <b>(+71.68%)</b></td><td>172.80 <b>(-26.50%)</b></td><td>246.81 <b>(+93.50%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.00 (n/a)</td><td>315.46 (n/a)</td><td>262.40 (n/a)</td><td>235.10 (n/a)</td><td>127.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 <b>(-26.70%)</b></td><td>0.03 <b>(-44.45%)</b></td><td>0.03 <b>(-46.62%)</b></td><td>0.02 <b>(-54.08%)</b></td><td>0.01 <b>(+84.40%)</b></td><td>593.20 <b>(+117.77%)</b></td><td>464.62 <b>(+92.44%)</b></td><td>448.50 <b>(+87.34%)</b></td><td>284.30 <b>(+36.42%)</b></td><td>131.27 <b>(+471.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>272.40 (n/a)</td><td>241.44 (n/a)</td><td>239.40 (n/a)</td><td>208.40 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (-2.20%)</td><td>0.03 (+5.10%)</td><td>0.03 (+7.51%)</td><td>0.02 (+19.14%)</td><td>0.01 <b>(-21.25%)</b></td><td>504.50 (-16.06%)</td><td>380.88 (-9.34%)</td><td>390.90 (-6.97%)</td><td>264.00 (+2.25%)</td><td>100.77 <b>(-32.26%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.00 (n/a)</td><td>420.14 (n/a)</td><td>420.20 (n/a)</td><td>258.20 (n/a)</td><td>148.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (-2.67%)</td><td>0.03 <b>(-34.88%)</b></td><td>0.02 <b>(-42.96%)</b></td><td>0.01 <b>(-74.82%)</b></td><td>0.02 <b>(+169.73%)</b></td><td>1355.20 <b>(+297.19%)</b></td><td>603.72 <b>(+116.53%)</b></td><td>495.50 <b>(+75.34%)</b></td><td>244.70 (+2.73%)</td><td>448.52 <b>(+994.44%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>341.20 (n/a)</td><td>278.82 (n/a)</td><td>282.60 (n/a)</td><td>238.20 (n/a)</td><td>40.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (-6.88%)</td><td>0.03 (-3.54%)</td><td>0.04 (+10.25%)</td><td>0.02 (-6.78%)</td><td>0.01 (-7.84%)</td><td>588.70 (+7.27%)</td><td>392.96 (+3.69%)</td><td>326.60 (-9.28%)</td><td>267.40 (+7.39%)</td><td>129.76 (+8.32%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.80 (n/a)</td><td>378.98 (n/a)</td><td>360.00 (n/a)</td><td>249.00 (n/a)</td><td>119.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 <b>(+25.71%)</b></td><td>0.04 (+13.98%)</td><td>0.04 <b>(+21.88%)</b></td><td>0.02 <b>(-26.04%)</b></td><td>0.02 <b>(+76.14%)</b></td><td>803.80 <b>(+35.21%)</b></td><td>429.62 (+1.48%)</td><td>312.10 (-17.93%)</td><td>241.60 <b>(-20.45%)</b></td><td>243.70 <b>(+83.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>423.36 (n/a)</td><td>380.30 (n/a)</td><td>303.70 (n/a)</td><td>132.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 <b>(+26.36%)</b></td><td>0.08 (-2.31%)</td><td>0.07 (-18.58%)</td><td>0.05 (-1.78%)</td><td>0.03 <b>(+63.55%)</b></td><td>545.80 (+1.81%)</td><td>361.96 (+9.65%)</td><td>368.40 <b>(+22.80%)</b></td><td>195.50 <b>(-20.85%)</b></td><td>145.08 <b>(+23.45%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>536.10 (n/a)</td><td>330.10 (n/a)</td><td>300.00 (n/a)</td><td>247.00 (n/a)</td><td>117.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 <b>(+20.80%)</b></td><td>0.08 <b>(+28.41%)</b></td><td>0.09 (+19.72%)</td><td>0.05 <b>(+268.61%)</b></td><td>0.03 (-12.39%)</td><td>522.90 <b>(-72.87%)</b></td><td>333.94 <b>(-49.09%)</b></td><td>274.10 (-16.48%)</td><td>201.60 (-17.24%)</td><td>130.63 <b>(-81.76%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1927.30 (n/a)</td><td>656.00 (n/a)</td><td>328.20 (n/a)</td><td>243.60 (n/a)</td><td>716.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (-13.78%)</td><td>0.06 <b>(-24.19%)</b></td><td>0.05 <b>(-36.66%)</b></td><td>0.04 (+17.71%)</td><td>0.02 <b>(-33.34%)</b></td><td>549.60 (-15.04%)</td><td>433.50 <b>(+22.89%)</b></td><td>455.50 <b>(+57.89%)</b></td><td>286.50 (+15.99%)</td><td>96.00 <b>(-42.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>646.90 (n/a)</td><td>352.76 (n/a)</td><td>288.50 (n/a)</td><td>247.00 (n/a)</td><td>165.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 <b>(+42.10%)</b></td><td>0.10 <b>(+30.72%)</b></td><td>0.09 (+16.10%)</td><td>0.06 <b>(+40.84%)</b></td><td>0.03 <b>(+28.98%)</b></td><td>405.60 <b>(-29.00%)</b></td><td>279.68 <b>(-25.08%)</b></td><td>259.00 (-13.87%)</td><td>170.50 <b>(-29.63%)</b></td><td>86.95 <b>(-37.37%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>571.30 (n/a)</td><td>373.30 (n/a)</td><td>300.70 (n/a)</td><td>242.30 (n/a)</td><td>138.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(-25.13%)</b></td><td>0.06 (-15.68%)</td><td>0.05 <b>(-28.05%)</b></td><td>0.05 (+14.61%)</td><td>0.02 <b>(-35.22%)</b></td><td>533.40 (-12.74%)</td><td>420.44 (+9.45%)</td><td>479.10 <b>(+38.95%)</b></td><td>237.20 <b>(+33.56%)</b></td><td>132.77 <b>(-22.00%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>611.30 (n/a)</td><td>384.14 (n/a)</td><td>344.80 (n/a)</td><td>177.60 (n/a)</td><td>170.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 <b>(-38.47%)</b></td><td>0.05 <b>(-28.55%)</b></td><td>0.05 <b>(-46.98%)</b></td><td>0.05 (+6.38%)</td><td>0.01 <b>(-70.34%)</b></td><td>532.90 (-6.00%)</td><td>473.96 <b>(+24.16%)</b></td><td>515.60 <b>(+88.59%)</b></td><td>391.10 <b>(+62.48%)</b></td><td>70.30 <b>(-57.14%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>566.90 (n/a)</td><td>381.72 (n/a)</td><td>273.40 (n/a)</td><td>240.70 (n/a)</td><td>164.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.23 (+14.26%)</td><td>0.19 <b>(+41.25%)</b></td><td>0.20 <b>(+96.20%)</b></td><td>0.11 (+19.64%)</td><td>0.05 (-10.34%)</td><td>449.90 (-16.41%)</td><td>275.36 <b>(-32.09%)</b></td><td>241.50 <b>(-49.02%)</b></td><td>211.40 (-12.50%)</td><td>98.55 <b>(-29.97%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>538.20 (n/a)</td><td>405.48 (n/a)</td><td>473.70 (n/a)</td><td>241.60 (n/a)</td><td>140.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.19 (-4.15%)</td><td>0.15 <b>(+25.13%)</b></td><td>0.17 <b>(+69.68%)</b></td><td>0.10 <b>(+41.54%)</b></td><td>0.04 (-14.55%)</td><td>482.60 <b>(-29.35%)</b></td><td>353.84 <b>(-24.20%)</b></td><td>292.30 <b>(-41.06%)</b></td><td>257.90 (+4.37%)</td><td>113.78 <b>(-34.51%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>683.10 (n/a)</td><td>466.82 (n/a)</td><td>495.90 (n/a)</td><td>247.10 (n/a)</td><td>173.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (-19.01%)</td><td>0.14 (-10.46%)</td><td>0.17 (+1.15%)</td><td>0.08 <b>(-20.99%)</b></td><td>0.05 (+2.43%)</td><td>584.00 <b>(+26.57%)</b></td><td>400.14 (+16.08%)</td><td>293.70 (-1.14%)</td><td>282.00 <b>(+23.47%)</b></td><td>155.48 <b>(+50.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>461.40 (n/a)</td><td>344.70 (n/a)</td><td>297.10 (n/a)</td><td>228.40 (n/a)</td><td>103.58 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (-15.75%)</td><td>0.12 <b>(-21.18%)</b></td><td>0.10 <b>(-41.06%)</b></td><td>0.09 <b>(+234.54%)</b></td><td>0.03 <b>(-50.98%)</b></td><td>570.90 <b>(-70.11%)</b></td><td>446.02 <b>(-26.03%)</b></td><td>469.40 <b>(+69.64%)</b></td><td>287.40 (+18.66%)</td><td>115.51 <b>(-84.20%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1909.90 (n/a)</td><td>602.94 (n/a)</td><td>276.70 (n/a)</td><td>242.20 (n/a)</td><td>731.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 (-14.29%)</td><td>0.13 (-8.18%)</td><td>0.11 (-15.33%)</td><td>0.08 (-14.19%)</td><td>0.04 (+0.90%)</td><td>587.80 (+16.53%)</td><td>411.98 (+11.11%)</td><td>439.60 (+18.11%)</td><td>277.40 (+16.70%)</td><td>134.00 <b>(+27.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>504.40 (n/a)</td><td>370.78 (n/a)</td><td>372.20 (n/a)</td><td>237.70 (n/a)</td><td>104.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.25 <b>(+50.19%)</b></td><td>0.17 <b>(+47.20%)</b></td><td>0.17 <b>(+50.01%)</b></td><td>0.08 (+7.65%)</td><td>0.06 <b>(+80.56%)</b></td><td>650.80 (-7.11%)</td><td>342.06 <b>(-26.29%)</b></td><td>294.70 <b>(-33.34%)</b></td><td>194.80 <b>(-33.42%)</b></td><td>178.84 (+18.97%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>700.60 (n/a)</td><td>464.06 (n/a)</td><td>442.10 (n/a)</td><td>292.60 (n/a)</td><td>150.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 <b>(+36.69%)</b></td><td>0.01 (-8.75%)</td><td>0.01 (-2.66%)</td><td>0.00 <b>(-75.06%)</b></td><td>0.00 <b>(+182.62%)</b></td><td>1944.20 <b>(+301.03%)</b></td><td>694.40 <b>(+73.57%)</b></td><td>422.40 (+2.72%)</td><td>237.80 <b>(-26.85%)</b></td><td>703.69 <b>(+892.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.80 (n/a)</td><td>400.08 (n/a)</td><td>411.20 (n/a)</td><td>325.10 (n/a)</td><td>70.87 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (-4.30%)</td><td>0.01 (+0.82%)</td><td>0.01 (+11.08%)</td><td>0.00 (+0.96%)</td><td>0.00 (+6.31%)</td><td>579.60 (-0.96%)</td><td>389.58 (+1.98%)</td><td>291.90 (-9.96%)</td><td>235.80 (+4.47%)</td><td>170.30 (+15.16%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>585.20 (n/a)</td><td>382.02 (n/a)</td><td>324.20 (n/a)</td><td>225.70 (n/a)</td><td>147.88 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (-2.82%)</td><td>0.01 (-3.43%)</td><td>0.01 (-18.55%)</td><td>0.00 (-1.51%)</td><td>0.00 (+6.52%)</td><td>574.80 (+1.54%)</td><td>425.18 (+5.32%)</td><td>477.00 <b>(+22.78%)</b></td><td>246.70 (+2.88%)</td><td>156.14 (+7.67%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>566.10 (n/a)</td><td>403.72 (n/a)</td><td>388.50 (n/a)</td><td>239.80 (n/a)</td><td>145.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 <b>(+22.45%)</b></td><td>0.01 (+16.25%)</td><td>0.01 <b>(+22.74%)</b></td><td>0.00 (+17.87%)</td><td>0.00 <b>(+39.65%)</b></td><td>569.70 (-15.17%)</td><td>358.02 (-8.97%)</td><td>248.30 (-18.54%)</td><td>190.20 (-18.33%)</td><td>179.12 (+1.86%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>671.60 (n/a)</td><td>393.32 (n/a)</td><td>304.80 (n/a)</td><td>232.90 (n/a)</td><td>175.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (-19.98%)</td><td>0.01 (-16.25%)</td><td>0.01 (-8.93%)</td><td>0.00 (-17.05%)</td><td>0.00 (-11.53%)</td><td>641.10 <b>(+20.55%)</b></td><td>430.72 <b>(+22.98%)</b></td><td>345.50 (+9.79%)</td><td>254.50 <b>(+24.94%)</b></td><td>193.94 <b>(+38.99%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>531.80 (n/a)</td><td>350.24 (n/a)</td><td>314.70 (n/a)</td><td>203.70 (n/a)</td><td>139.53 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 <b>(+29.57%)</b></td><td>0.01 <b>(+35.19%)</b></td><td>0.01 <b>(+51.73%)</b></td><td>0.01 (+10.30%)</td><td>0.00 <b>(+73.36%)</b></td><td>508.50 (-9.34%)</td><td>354.88 <b>(-24.41%)</b></td><td>317.30 <b>(-34.10%)</b></td><td>291.00 <b>(-22.81%)</b></td><td>88.92 <b>(+25.61%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>560.90 (n/a)</td><td>469.46 (n/a)</td><td>481.50 (n/a)</td><td>377.00 (n/a)</td><td>70.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-1.37%)</td><td>0.02 <b>(+21.88%)</b></td><td>0.02 (+16.37%)</td><td>0.02 <b>(+74.26%)</b></td><td>0.00 <b>(-50.87%)</b></td><td>307.10 <b>(-42.62%)</b></td><td>267.12 <b>(-23.59%)</b></td><td>252.90 (-14.07%)</td><td>235.30 (+1.42%)</td><td>33.57 <b>(-71.90%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.20 (n/a)</td><td>349.58 (n/a)</td><td>294.30 (n/a)</td><td>232.00 (n/a)</td><td>119.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-4.38%)</td><td>0.02 (-8.24%)</td><td>0.01 <b>(-35.80%)</b></td><td>0.01 <b>(+21.30%)</b></td><td>0.01 <b>(-23.15%)</b></td><td>468.20 (-17.56%)</td><td>354.66 (+0.93%)</td><td>371.30 <b>(+55.75%)</b></td><td>236.40 (+4.60%)</td><td>112.08 <b>(-32.91%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.90 (n/a)</td><td>351.40 (n/a)</td><td>238.40 (n/a)</td><td>226.00 (n/a)</td><td>167.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-6.65%)</td><td>0.02 (-6.24%)</td><td>0.02 (+16.84%)</td><td>0.01 <b>(-47.43%)</b></td><td>0.01 <b>(+80.51%)</b></td><td>561.70 <b>(+90.21%)</b></td><td>307.02 (+18.39%)</td><td>234.80 (-14.40%)</td><td>216.40 (+7.13%)</td><td>145.17 <b>(+283.88%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>295.30 (n/a)</td><td>259.34 (n/a)</td><td>274.30 (n/a)</td><td>202.00 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+8.75%)</td><td>0.02 (+8.12%)</td><td>0.02 (-0.31%)</td><td>0.01 <b>(+41.08%)</b></td><td>0.00 <b>(-22.21%)</b></td><td>498.80 <b>(-29.12%)</b></td><td>356.52 (-15.31%)</td><td>312.70 (+0.32%)</td><td>242.20 (-8.05%)</td><td>103.84 <b>(-47.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>703.70 (n/a)</td><td>420.98 (n/a)</td><td>311.70 (n/a)</td><td>263.40 (n/a)</td><td>196.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+5.44%)</td><td>0.01 (+10.36%)</td><td>0.01 (-11.26%)</td><td>0.01 <b>(+221.11%)</b></td><td>0.01 (-15.58%)</td><td>637.80 <b>(-68.86%)</b></td><td>473.60 <b>(-36.13%)</b></td><td>527.80 (+12.68%)</td><td>255.40 (-5.16%)</td><td>155.00 <b>(-78.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2047.90 (n/a)</td><td>741.52 (n/a)</td><td>468.40 (n/a)</td><td>269.30 (n/a)</td><td>735.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (-9.36%)</td><td>0.01 (+11.27%)</td><td>0.01 (+16.41%)</td><td>0.01 <b>(+23.84%)</b></td><td>0.00 <b>(-58.25%)</b></td><td>465.20 (-19.25%)</td><td>414.32 (-12.36%)</td><td>413.90 (-14.09%)</td><td>377.00 (+10.33%)</td><td>33.18 <b>(-61.41%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.10 (n/a)</td><td>472.74 (n/a)</td><td>481.80 (n/a)</td><td>341.70 (n/a)</td><td>85.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (+9.99%)</td><td>0.03 <b>(+63.89%)</b></td><td>0.04 <b>(+90.25%)</b></td><td>0.02 <b>(+440.82%)</b></td><td>0.01 <b>(-30.47%)</b></td><td>456.50 <b>(-81.51%)</b></td><td>330.00 <b>(-61.86%)</b></td><td>278.40 <b>(-47.44%)</b></td><td>245.80 (-9.10%)</td><td>92.27 <b>(-89.79%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2469.00 (n/a)</td><td>865.16 (n/a)</td><td>529.70 (n/a)</td><td>270.40 (n/a)</td><td>903.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 <b>(+25.75%)</b></td><td>0.03 <b>(+25.92%)</b></td><td>0.04 <b>(+88.38%)</b></td><td>0.01 <b>(-70.48%)</b></td><td>0.02 <b>(+134.61%)</b></td><td>2016.40 <b>(+238.72%)</b></td><td>671.58 <b>(+38.69%)</b></td><td>281.60 <b>(-46.91%)</b></td><td>246.70 <b>(-20.47%)</b></td><td>763.41 <b>(+496.58%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.30 (n/a)</td><td>484.22 (n/a)</td><td>530.40 (n/a)</td><td>310.20 (n/a)</td><td>127.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (+11.80%)</td><td>0.03 (+4.73%)</td><td>0.04 (+12.00%)</td><td>0.02 (-7.40%)</td><td>0.01 <b>(+33.95%)</b></td><td>543.80 (+8.00%)</td><td>357.84 (+2.57%)</td><td>243.40 (-10.74%)</td><td>219.90 (-10.57%)</td><td>169.36 <b>(+35.51%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.50 (n/a)</td><td>348.88 (n/a)</td><td>272.70 (n/a)</td><td>245.90 (n/a)</td><td>124.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (-7.55%)</td><td>0.03 (-18.02%)</td><td>0.02 <b>(-34.70%)</b></td><td>0.02 <b>(+26.33%)</b></td><td>0.01 <b>(-30.98%)</b></td><td>496.10 <b>(-20.84%)</b></td><td>426.76 (+10.94%)</td><td>461.60 <b>(+53.10%)</b></td><td>246.00 (+8.18%)</td><td>103.40 <b>(-42.54%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>626.70 (n/a)</td><td>384.68 (n/a)</td><td>301.50 (n/a)</td><td>227.40 (n/a)</td><td>179.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (+10.97%)</td><td>0.04 <b>(+58.17%)</b></td><td>0.04 <b>(+94.14%)</b></td><td>0.02 <b>(+55.03%)</b></td><td>0.01 (-12.05%)</td><td>438.20 <b>(-35.49%)</b></td><td>291.78 <b>(-39.55%)</b></td><td>253.50 <b>(-48.49%)</b></td><td>240.40 (-9.86%)</td><td>82.98 <b>(-44.23%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>679.30 (n/a)</td><td>482.68 (n/a)</td><td>492.10 (n/a)</td><td>266.70 (n/a)</td><td>148.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 <b>(+47.83%)</b></td><td>0.03 <b>(+43.80%)</b></td><td>0.03 <b>(+32.05%)</b></td><td>0.01 <b>(+41.61%)</b></td><td>0.01 <b>(+43.50%)</b></td><td>704.00 <b>(-29.38%)</b></td><td>418.80 <b>(-30.60%)</b></td><td>364.10 <b>(-24.26%)</b></td><td>258.50 <b>(-32.35%)</b></td><td>173.21 <b>(-30.48%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>996.90 (n/a)</td><td>603.42 (n/a)</td><td>480.70 (n/a)</td><td>382.10 (n/a)</td><td>249.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 <b>(-29.62%)</b></td><td>0.05 (-17.75%)</td><td>0.05 (-11.77%)</td><td>0.03 (-3.40%)</td><td>0.01 <b>(-58.44%)</b></td><td>650.20 (+3.52%)</td><td>457.78 (+9.52%)</td><td>424.90 (+13.34%)</td><td>355.10 <b>(+42.10%)</b></td><td>113.55 <b>(-35.62%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.10 (n/a)</td><td>417.98 (n/a)</td><td>374.90 (n/a)</td><td>249.90 (n/a)</td><td>176.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (+5.20%)</td><td>0.06 (+15.09%)</td><td>0.07 <b>(+52.74%)</b></td><td>0.04 (+11.72%)</td><td>0.02 (-0.57%)</td><td>507.20 (-10.48%)</td><td>359.74 (-13.99%)</td><td>292.10 <b>(-34.52%)</b></td><td>261.70 (-4.97%)</td><td>117.82 (-11.65%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>566.60 (n/a)</td><td>418.26 (n/a)</td><td>446.10 (n/a)</td><td>275.40 (n/a)</td><td>133.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (-17.15%)</td><td>0.07 <b>(+50.60%)</b></td><td>0.08 <b>(+90.43%)</b></td><td>0.04 <b>(+295.49%)</b></td><td>0.02 <b>(-46.42%)</b></td><td>487.30 <b>(-74.71%)</b></td><td>301.98 <b>(-57.79%)</b></td><td>249.40 <b>(-47.49%)</b></td><td>242.30 <b>(+20.67%)</b></td><td>104.99 <b>(-84.78%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1927.20 (n/a)</td><td>715.34 (n/a)</td><td>475.00 (n/a)</td><td>200.80 (n/a)</td><td>690.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (-10.75%)</td><td>0.06 (-15.59%)</td><td>0.05 <b>(-29.97%)</b></td><td>0.04 (-2.25%)</td><td>0.02 (+2.10%)</td><td>474.20 (+2.31%)</td><td>370.86 (+18.98%)</td><td>416.20 <b>(+42.78%)</b></td><td>271.50 (+12.05%)</td><td>92.11 (+5.50%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>463.50 (n/a)</td><td>311.70 (n/a)</td><td>291.50 (n/a)</td><td>242.30 (n/a)</td><td>87.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 <b>(+22.29%)</b></td><td>0.05 (+19.49%)</td><td>0.05 <b>(+23.82%)</b></td><td>0.04 (+4.65%)</td><td>0.01 <b>(+44.53%)</b></td><td>575.60 (-4.45%)</td><td>414.32 (-14.58%)</td><td>409.20 (-19.24%)</td><td>286.50 (-18.24%)</td><td>107.05 (+16.23%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>602.40 (n/a)</td><td>485.06 (n/a)</td><td>506.70 (n/a)</td><td>350.40 (n/a)</td><td>92.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (+12.79%)</td><td>0.05 <b>(+29.99%)</b></td><td>0.05 (+19.88%)</td><td>0.03 <b>(+303.86%)</b></td><td>0.01 <b>(-44.67%)</b></td><td>608.80 <b>(-75.24%)</b></td><td>437.02 <b>(-50.00%)</b></td><td>418.60 (-16.60%)</td><td>337.00 (-11.34%)</td><td>105.57 <b>(-88.17%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2458.60 (n/a)</td><td>873.96 (n/a)</td><td>501.90 (n/a)</td><td>380.10 (n/a)</td><td>892.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>444.90 (n/a)</td><td>327.34 (n/a)</td><td>307.20 (n/a)</td><td>229.20 (n/a)</td><td>86.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.50 (n/a)</td><td>436.48 (n/a)</td><td>455.20 (n/a)</td><td>287.10 (n/a)</td><td>146.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2392.50 (n/a)</td><td>778.96 (n/a)</td><td>479.50 (n/a)</td><td>180.30 (n/a)</td><td>916.58 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>445.40 (n/a)</td><td>313.72 (n/a)</td><td>296.80 (n/a)</td><td>159.40 (n/a)</td><td>106.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.40 (n/a)</td><td>477.96 (n/a)</td><td>520.60 (n/a)</td><td>239.10 (n/a)</td><td>139.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.10 (n/a)</td><td>419.54 (n/a)</td><td>384.20 (n/a)</td><td>296.40 (n/a)</td><td>124.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>592.00 (n/a)</td><td>328.94 (n/a)</td><td>297.30 (n/a)</td><td>179.30 (n/a)</td><td>155.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>527.60 (n/a)</td><td>336.78 (n/a)</td><td>293.20 (n/a)</td><td>239.20 (n/a)</td><td>118.90 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>819.20 (n/a)</td><td>478.40 (n/a)</td><td>354.50 (n/a)</td><td>242.30 (n/a)</td><td>246.81 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.16 (-19.61%)</td><td>0.14 (-15.31%)</td><td>0.15 (-10.53%)</td><td>0.08 (-11.66%)</td><td>0.03 <b>(-20.79%)</b></td><td>596.30 (+13.21%)</td><td>381.80 (+16.91%)</td><td>326.80 (+11.76%)</td><td>309.10 <b>(+24.44%)</b></td><td>121.91 (+7.40%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>526.70 (n/a)</td><td>326.58 (n/a)</td><td>292.40 (n/a)</td><td>248.40 (n/a)</td><td>113.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1962.70 (n/a)</td><td>687.92 (n/a)</td><td>432.40 (n/a)</td><td>267.20 (n/a)</td><td>717.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>574.20 (n/a)</td><td>418.34 (n/a)</td><td>458.40 (n/a)</td><td>248.70 (n/a)</td><td>147.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.10 (n/a)</td><td>400.94 (n/a)</td><td>338.10 (n/a)</td><td>296.40 (n/a)</td><td>122.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.40 (n/a)</td><td>447.68 (n/a)</td><td>395.50 (n/a)</td><td>295.50 (n/a)</td><td>140.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.80 (n/a)</td><td>464.06 (n/a)</td><td>486.30 (n/a)</td><td>367.20 (n/a)</td><td>70.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.60 (n/a)</td><td>486.30 (n/a)</td><td>467.20 (n/a)</td><td>269.80 (n/a)</td><td>149.53 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2008.60 (n/a)</td><td>721.56 (n/a)</td><td>544.00 (n/a)</td><td>186.90 (n/a)</td><td>739.23 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>623.40 (n/a)</td><td>431.50 (n/a)</td><td>524.80 (n/a)</td><td>147.60 (n/a)</td><td>197.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>461.80 (n/a)</td><td>340.00 (n/a)</td><td>276.30 (n/a)</td><td>260.70 (n/a)</td><td>99.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>595.80 (n/a)</td><td>458.76 (n/a)</td><td>454.20 (n/a)</td><td>250.50 (n/a)</td><td>134.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2070.10 (n/a)</td><td>1043.78 (n/a)</td><td>459.00 (n/a)</td><td>298.30 (n/a)</td><td>880.42 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1871.30 (n/a)</td><td>742.86 (n/a)</td><td>515.30 (n/a)</td><td>280.40 (n/a)</td><td>640.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1934.10 (n/a)</td><td>628.70 (n/a)</td><td>327.80 (n/a)</td><td>202.90 (n/a)</td><td>735.26 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>431.80 (n/a)</td><td>322.14 (n/a)</td><td>296.70 (n/a)</td><td>249.10 (n/a)</td><td>73.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.40 (n/a)</td><td>389.52 (n/a)</td><td>394.80 (n/a)</td><td>272.10 (n/a)</td><td>113.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.50 (n/a)</td><td>469.58 (n/a)</td><td>506.10 (n/a)</td><td>257.60 (n/a)</td><td>122.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>832.40 (n/a)</td><td>433.04 (n/a)</td><td>328.00 (n/a)</td><td>201.40 (n/a)</td><td>247.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>636.90 (n/a)</td><td>471.34 (n/a)</td><td>483.50 (n/a)</td><td>239.80 (n/a)</td><td>147.71 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>650.40 (n/a)</td><td>541.30 (n/a)</td><td>502.10 (n/a)</td><td>490.20 (n/a)</td><td>67.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.70 (n/a)</td><td>435.32 (n/a)</td><td>490.70 (n/a)</td><td>239.20 (n/a)</td><td>165.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.50 (n/a)</td><td>470.32 (n/a)</td><td>518.20 (n/a)</td><td>280.10 (n/a)</td><td>120.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.40 (n/a)</td><td>384.94 (n/a)</td><td>417.20 (n/a)</td><td>225.50 (n/a)</td><td>147.59 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.10 (n/a)</td><td>427.28 (n/a)</td><td>469.70 (n/a)</td><td>273.40 (n/a)</td><td>97.62 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.20 (n/a)</td><td>433.24 (n/a)</td><td>489.60 (n/a)</td><td>315.40 (n/a)</td><td>105.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.80 (n/a)</td><td>441.12 (n/a)</td><td>498.70 (n/a)</td><td>284.50 (n/a)</td><td>136.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>713.70 (n/a)</td><td>416.98 (n/a)</td><td>306.30 (n/a)</td><td>263.60 (n/a)</td><td>189.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>646.90 (n/a)</td><td>350.26 (n/a)</td><td>306.10 (n/a)</td><td>238.30 (n/a)</td><td>169.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>530.50 (n/a)</td><td>375.08 (n/a)</td><td>333.10 (n/a)</td><td>249.40 (n/a)</td><td>121.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.30 (n/a)</td><td>319.58 (n/a)</td><td>285.20 (n/a)</td><td>213.40 (n/a)</td><td>124.30 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>584.00 (n/a)</td><td>493.86 (n/a)</td><td>515.30 (n/a)</td><td>398.80 (n/a)</td><td>76.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>616.10 (n/a)</td><td>423.14 (n/a)</td><td>407.70 (n/a)</td><td>262.80 (n/a)</td><td>126.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>723.20 (n/a)</td><td>446.78 (n/a)</td><td>345.20 (n/a)</td><td>272.00 (n/a)</td><td>198.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1015.50 (n/a)</td><td>614.46 (n/a)</td><td>583.10 (n/a)</td><td>306.20 (n/a)</td><td>254.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>497.80 (n/a)</td><td>395.54 (n/a)</td><td>479.70 (n/a)</td><td>233.30 (n/a)</td><td>131.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>529.20 (n/a)</td><td>350.92 (n/a)</td><td>315.70 (n/a)</td><td>264.00 (n/a)</td><td>106.88 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>636.60 (n/a)</td><td>432.64 (n/a)</td><td>463.00 (n/a)</td><td>251.00 (n/a)</td><td>156.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.63 <b>(-28.01%)</b></td><td>0.46 (+10.34%)</td><td>0.42 (+19.88%)</td><td>0.33 <b>(+161.58%)</b></td><td>0.12 <b>(-55.08%)</b></td><td>664.90 <b>(-61.77%)</b></td><td>512.16 <b>(-33.56%)</b></td><td>521.00 (-16.59%)</td><td>352.60 <b>(+38.93%)</b></td><td>131.01 <b>(-76.79%)</b></td><td>26.77 <b>(-28.01%)</b></td><td>19.49 (+10.34%)</td><td>18.11 (+19.88%)</td><td>14.19 <b>(+161.58%)</b></td><td>5.27 <b>(-55.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.87 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.27 (n/a)</td><td>1739.10 (n/a)</td><td>770.86 (n/a)</td><td>624.60 (n/a)</td><td>253.80 (n/a)</td><td>564.52 (n/a)</td><td>37.18 (n/a)</td><td>17.66 (n/a)</td><td>15.11 (n/a)</td><td>5.43 (n/a)</td><td>11.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.60 (-1.31%)</td><td>0.41 (-1.15%)</td><td>0.42 (-9.76%)</td><td>0.11 (-14.27%)</td><td>0.19 (-0.50%)</td><td>1996.00 (+16.64%)</td><td>779.80 (+6.95%)</td><td>521.80 (+10.81%)</td><td>371.10 (+1.31%)</td><td>685.12 <b>(+22.07%)</b></td><td>25.43 (-1.31%)</td><td>17.33 (-1.15%)</td><td>18.09 (-9.76%)</td><td>4.73 (-14.27%)</td><td>7.94 (-0.50%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.60 (n/a)</td><td>0.41 (n/a)</td><td>0.47 (n/a)</td><td>0.13 (n/a)</td><td>0.19 (n/a)</td><td>1711.20 (n/a)</td><td>729.12 (n/a)</td><td>470.90 (n/a)</td><td>366.30 (n/a)</td><td>561.28 (n/a)</td><td>25.76 (n/a)</td><td>17.53 (n/a)</td><td>20.04 (n/a)</td><td>5.52 (n/a)</td><td>7.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.31 (-0.09%)</td><td>0.31 (+0.83%)</td><td>0.31 (-0.39%)</td><td>0.30 (+3.39%)</td><td>0.00 <b>(-64.68%)</b></td><td>82928.50 (-3.27%)</td><td>82016.36 (-0.87%)</td><td>81720.70 (+0.40%)</td><td>81393.50 (+0.09%)</td><td>684.15 <b>(-65.69%)</b></td><td>211.07 (-0.09%)</td><td>209.48 (+0.83%)</td><td>210.23 (-0.39%)</td><td>207.16 (+3.39%)</td><td>1.74 <b>(-64.68%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85736.30 (n/a)</td><td>82732.08 (n/a)</td><td>81398.50 (n/a)</td><td>81322.30 (n/a)</td><td>1994.19 (n/a)</td><td>211.26 (n/a)</td><td>207.75 (n/a)</td><td>211.06 (n/a)</td><td>200.38 (n/a)</td><td>4.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>1.03 (-0.28%)</td><td>1.01 (+0.08%)</td><td>1.01 (-0.83%)</td><td>1.00 (+0.42%)</td><td>0.01 (-6.85%)</td><td>25183.00 (-0.42%)</td><td>24848.72 (-0.08%)</td><td>25003.30 (+0.83%)</td><td>24477.30 (+0.28%)</td><td>307.87 (-7.13%)</td><td>701.87 (-0.28%)</td><td>691.46 (+0.08%)</td><td>687.10 (-0.83%)</td><td>682.20 (+0.42%)</td><td>8.59 (-6.85%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25290.00 (n/a)</td><td>24868.90 (n/a)</td><td>24796.90 (n/a)</td><td>24409.30 (n/a)</td><td>331.53 (n/a)</td><td>703.82 (n/a)</td><td>690.92 (n/a)</td><td>692.82 (n/a)</td><td>679.32 (n/a)</td><td>9.23 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.82 (-0.07%)</td><td>0.80 (-0.32%)</td><td>0.81 (-0.25%)</td><td>0.76 (-0.46%)</td><td>0.03 (+3.09%)</td><td>99738.80 (+0.46%)</td><td>94069.52 (+0.32%)</td><td>92837.30 (+0.25%)</td><td>91958.60 (+0.07%)</td><td>3228.92 (+3.71%)</td><td>747.29 (-0.07%)</td><td>731.18 (-0.32%)</td><td>740.21 (-0.25%)</td><td>688.99 (-0.46%)</td><td>24.09 (+3.09%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.76 (n/a)</td><td>0.03 (n/a)</td><td>99279.00 (n/a)</td><td>93766.82 (n/a)</td><td>92606.50 (n/a)</td><td>91890.40 (n/a)</td><td>3113.47 (n/a)</td><td>747.84 (n/a)</td><td>733.50 (n/a)</td><td>742.06 (n/a)</td><td>692.19 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.77 (-0.40%)</td><td>0.76 (-1.35%)</td><td>0.76 (-1.14%)</td><td>0.75 (-2.38%)</td><td>0.01 <b>(+134.60%)</b></td><td>100865.80 (+2.44%)</td><td>99005.60 (+1.38%)</td><td>98768.60 (+1.15%)</td><td>97489.40 (+0.41%)</td><td>1307.49 <b>(+141.47%)</b></td><td>704.89 (-0.40%)</td><td>694.19 (-1.35%)</td><td>695.76 (-1.14%)</td><td>681.30 (-2.38%)</td><td>9.13 <b>(+134.61%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.00 (n/a)</td><td>98463.00 (n/a)</td><td>97660.06 (n/a)</td><td>97647.30 (n/a)</td><td>97095.00 (n/a)</td><td>541.47 (n/a)</td><td>707.76 (n/a)</td><td>703.68 (n/a)</td><td>703.75 (n/a)</td><td>697.92 (n/a)</td><td>3.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.80 (+0.22%)</td><td>0.79 (-0.06%)</td><td>0.79 (+0.60%)</td><td>0.78 (-0.81%)</td><td>0.01 <b>(+51.49%)</b></td><td>96823.10 (+0.82%)</td><td>95529.10 (+0.06%)</td><td>95128.30 (-0.60%)</td><td>94556.50 (-0.22%)</td><td>907.33 <b>(+52.52%)</b></td><td>726.76 (+0.22%)</td><td>719.41 (-0.06%)</td><td>722.39 (+0.60%)</td><td>709.74 (-0.81%)</td><td>6.81 <b>(+51.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96037.50 (n/a)</td><td>95469.16 (n/a)</td><td>95698.20 (n/a)</td><td>94765.50 (n/a)</td><td>594.89 (n/a)</td><td>725.15 (n/a)</td><td>719.83 (n/a)</td><td>718.09 (n/a)</td><td>715.55 (n/a)</td><td>4.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.20 <b>(-27.82%)</b></td><td>3.45 <b>(-23.06%)</b></td><td>4.04 <b>(-23.83%)</b></td><td>1.95 (-10.57%)</td><td>0.97 <b>(-38.80%)</b></td><td>4575.90 (+11.83%)</td><td>2818.66 <b>(+23.01%)</b></td><td>2204.80 <b>(+31.28%)</b></td><td>2122.50 <b>(+38.54%)</b></td><td>1045.60 (-4.20%)</td><td>252.94 <b>(-27.82%)</b></td><td>207.54 <b>(-23.06%)</b></td><td>243.50 <b>(-23.83%)</b></td><td>117.33 (-10.57%)</td><td>58.51 <b>(-38.80%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.82 (n/a)</td><td>4.48 (n/a)</td><td>5.31 (n/a)</td><td>2.18 (n/a)</td><td>1.59 (n/a)</td><td>4092.00 (n/a)</td><td>2291.38 (n/a)</td><td>1679.50 (n/a)</td><td>1532.10 (n/a)</td><td>1091.43 (n/a)</td><td>350.42 (n/a)</td><td>269.76 (n/a)</td><td>319.67 (n/a)</td><td>131.20 (n/a)</td><td>95.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.77 (+4.12%)</td><td>3.97 (+9.45%)</td><td>4.29 <b>(+25.87%)</b></td><td>3.02 <b>(+33.45%)</b></td><td>0.85 (-10.95%)</td><td>2947.40 <b>(-25.07%)</b></td><td>2335.78 (-10.93%)</td><td>2077.30 <b>(-20.55%)</b></td><td>1869.90 (-3.96%)</td><td>535.43 <b>(-33.63%)</b></td><td>287.11 (+4.12%)</td><td>239.27 (+9.45%)</td><td>258.45 <b>(+25.87%)</b></td><td>182.15 <b>(+33.45%)</b></td><td>51.47 (-10.95%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>4.58 (n/a)</td><td>3.63 (n/a)</td><td>3.41 (n/a)</td><td>2.27 (n/a)</td><td>0.96 (n/a)</td><td>3933.40 (n/a)</td><td>2622.36 (n/a)</td><td>2614.60 (n/a)</td><td>1947.00 (n/a)</td><td>806.70 (n/a)</td><td>275.74 (n/a)</td><td>218.60 (n/a)</td><td>205.34 (n/a)</td><td>136.49 (n/a)</td><td>57.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.96 <b>(-29.14%)</b></td><td>2.78 <b>(-26.82%)</b></td><td>2.17 <b>(-44.79%)</b></td><td>1.92 <b>(-28.17%)</b></td><td>0.96 (-18.51%)</td><td>4635.30 <b>(+39.22%)</b></td><td>3507.28 <b>(+38.96%)</b></td><td>4106.30 <b>(+81.12%)</b></td><td>2250.00 <b>(+41.12%)</b></td><td>1093.39 <b>(+49.25%)</b></td><td>238.61 <b>(-29.14%)</b></td><td>167.46 <b>(-26.82%)</b></td><td>130.74 <b>(-44.79%)</b></td><td>115.82 <b>(-28.17%)</b></td><td>57.99 (-18.51%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.59 (n/a)</td><td>3.80 (n/a)</td><td>3.93 (n/a)</td><td>2.68 (n/a)</td><td>1.18 (n/a)</td><td>3329.40 (n/a)</td><td>2523.90 (n/a)</td><td>2267.20 (n/a)</td><td>1594.40 (n/a)</td><td>732.61 (n/a)</td><td>336.72 (n/a)</td><td>228.83 (n/a)</td><td>236.80 (n/a)</td><td>161.25 (n/a)</td><td>71.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.71 (+0.14%)</td><td>5.09 (-3.30%)</td><td>4.77 (-15.57%)</td><td>4.31 (+17.16%)</td><td>0.93 <b>(-34.62%)</b></td><td>8092.60 (-14.65%)</td><td>7004.30 (-0.85%)</td><td>7306.10 (+18.45%)</td><td>5193.60 (-0.13%)</td><td>1081.73 <b>(-47.38%)</b></td><td>413.49 (+0.14%)</td><td>313.66 (-3.30%)</td><td>293.93 (-15.57%)</td><td>265.36 (+17.16%)</td><td>57.57 <b>(-34.62%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>6.70 (n/a)</td><td>5.27 (n/a)</td><td>5.65 (n/a)</td><td>3.68 (n/a)</td><td>1.43 (n/a)</td><td>9481.50 (n/a)</td><td>7064.50 (n/a)</td><td>6168.30 (n/a)</td><td>5200.60 (n/a)</td><td>2055.82 (n/a)</td><td>412.93 (n/a)</td><td>324.37 (n/a)</td><td>348.15 (n/a)</td><td>226.49 (n/a)</td><td>88.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.09 (+16.91%)</td><td>5.48 <b>(+22.12%)</b></td><td>5.61 <b>(+20.33%)</b></td><td>4.32 (+17.42%)</td><td>0.69 (+17.06%)</td><td>8071.70 (-14.83%)</td><td>6455.20 (-18.10%)</td><td>6211.90 (-16.90%)</td><td>5724.10 (-14.46%)</td><td>935.14 (-13.53%)</td><td>375.17 (+16.91%)</td><td>337.58 <b>(+22.12%)</b></td><td>345.70 <b>(+20.33%)</b></td><td>266.05 (+17.42%)</td><td>42.44 (+17.06%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.21 (n/a)</td><td>4.49 (n/a)</td><td>4.66 (n/a)</td><td>3.68 (n/a)</td><td>0.59 (n/a)</td><td>9477.70 (n/a)</td><td>7881.62 (n/a)</td><td>7474.90 (n/a)</td><td>6692.00 (n/a)</td><td>1081.46 (n/a)</td><td>320.90 (n/a)</td><td>276.42 (n/a)</td><td>287.29 (n/a)</td><td>226.58 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.67 (+1.51%)</td><td>5.34 (-7.72%)</td><td>5.26 (-7.65%)</td><td>4.44 (-12.19%)</td><td>0.83 <b>(+38.49%)</b></td><td>7852.20 (+13.88%)</td><td>6644.36 (+9.39%)</td><td>6633.90 (+8.29%)</td><td>5230.90 (-1.49%)</td><td>961.75 <b>(+53.40%)</b></td><td>410.54 (+1.51%)</td><td>329.07 (-7.72%)</td><td>323.71 (-7.65%)</td><td>273.49 (-12.19%)</td><td>51.13 <b>(+38.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>6.57 (n/a)</td><td>5.79 (n/a)</td><td>5.69 (n/a)</td><td>5.06 (n/a)</td><td>0.60 (n/a)</td><td>6895.00 (n/a)</td><td>6074.06 (n/a)</td><td>6126.10 (n/a)</td><td>5310.10 (n/a)</td><td>626.97 (n/a)</td><td>404.42 (n/a)</td><td>356.59 (n/a)</td><td>350.55 (n/a)</td><td>311.45 (n/a)</td><td>36.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.79 (+0.90%)</td><td>0.78 (+1.94%)</td><td>0.78 (+2.37%)</td><td>0.75 (+1.31%)</td><td>0.01 (-0.57%)</td><td>100485.30 (-1.29%)</td><td>97346.86 (-1.90%)</td><td>96701.70 (-2.32%)</td><td>96033.90 (-0.89%)</td><td>1794.72 (-2.48%)</td><td>715.57 (+0.90%)</td><td>706.11 (+1.94%)</td><td>710.63 (+2.37%)</td><td>683.88 (+1.31%)</td><td>12.74 (-0.57%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101799.10 (n/a)</td><td>99236.74 (n/a)</td><td>98994.40 (n/a)</td><td>96899.50 (n/a)</td><td>1840.41 (n/a)</td><td>709.18 (n/a)</td><td>692.67 (n/a)</td><td>694.18 (n/a)</td><td>675.05 (n/a)</td><td>12.81 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.77 (-1.02%)</td><td>0.76 (-0.60%)</td><td>0.76 (+0.30%)</td><td>0.73 (-1.79%)</td><td>0.01 (+19.89%)</td><td>102870.90 (+1.83%)</td><td>99523.38 (+0.61%)</td><td>98926.30 (-0.30%)</td><td>97964.80 (+1.03%)</td><td>1917.35 <b>(+23.95%)</b></td><td>701.47 (-1.02%)</td><td>690.69 (-0.60%)</td><td>694.65 (+0.30%)</td><td>668.02 (-1.79%)</td><td>13.01 (+19.89%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101026.20 (n/a)</td><td>98919.30 (n/a)</td><td>99224.10 (n/a)</td><td>96965.60 (n/a)</td><td>1546.83 (n/a)</td><td>708.70 (n/a)</td><td>694.84 (n/a)</td><td>692.57 (n/a)</td><td>680.21 (n/a)</td><td>10.86 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.81 (+0.46%)</td><td>0.80 (+0.64%)</td><td>0.80 (-0.37%)</td><td>0.78 (+3.38%)</td><td>0.01 <b>(-41.08%)</b></td><td>96907.00 (-3.27%)</td><td>94860.40 (-0.67%)</td><td>94653.90 (+0.37%)</td><td>93415.30 (-0.46%)</td><td>1504.77 <b>(-43.50%)</b></td><td>735.63 (+0.46%)</td><td>724.57 (+0.64%)</td><td>726.01 (-0.37%)</td><td>709.13 (+3.38%)</td><td>11.44 <b>(-41.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>100177.90 (n/a)</td><td>95503.48 (n/a)</td><td>94303.30 (n/a)</td><td>93845.00 (n/a)</td><td>2663.43 (n/a)</td><td>732.27 (n/a)</td><td>719.98 (n/a)</td><td>728.71 (n/a)</td><td>685.97 (n/a)</td><td>19.42 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.68 <b>(+82.24%)</b></td><td>2.87 <b>(+56.49%)</b></td><td>3.51 <b>(+82.86%)</b></td><td>1.76 (+11.96%)</td><td>0.97 <b>(+430.16%)</b></td><td>4567.70 (-10.68%)</td><td>3130.94 <b>(-29.26%)</b></td><td>2296.00 <b>(-45.31%)</b></td><td>2192.10 <b>(-45.13%)</b></td><td>1207.73 <b>(+159.57%)</b></td><td>964.36 <b>(+82.24%)</b></td><td>753.71 <b>(+56.49%)</b></td><td>920.72 <b>(+82.86%)</b></td><td>462.80 (+11.96%)</td><td>254.76 <b>(+430.16%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.02 (n/a)</td><td>1.84 (n/a)</td><td>1.92 (n/a)</td><td>1.58 (n/a)</td><td>0.18 (n/a)</td><td>5114.00 (n/a)</td><td>4426.12 (n/a)</td><td>4198.40 (n/a)</td><td>3994.90 (n/a)</td><td>465.27 (n/a)</td><td>529.16 (n/a)</td><td>481.64 (n/a)</td><td>503.51 (n/a)</td><td>413.36 (n/a)</td><td>48.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.29 <b>(+37.00%)</b></td><td>0.22 (+8.85%)</td><td>0.19 (-3.91%)</td><td>0.17 (-14.89%)</td><td>0.05 <b>(+554.95%)</b></td><td>7537.90 (+17.50%)</td><td>5947.84 (-3.92%)</td><td>6422.20 (+4.07%)</td><td>4234.60 <b>(-27.01%)</b></td><td>1369.57 <b>(+453.38%)</b></td><td>15.85 <b>(+37.00%)</b></td><td>11.82 (+8.85%)</td><td>10.45 (-3.91%)</td><td>8.90 (-14.89%)</td><td>2.92 <b>(+554.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>6415.50 (n/a)</td><td>6190.44 (n/a)</td><td>6170.80 (n/a)</td><td>5801.50 (n/a)</td><td>247.49 (n/a)</td><td>11.57 (n/a)</td><td>10.85 (n/a)</td><td>10.88 (n/a)</td><td>10.46 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.16 (-7.00%)</td><td>0.14 (+19.75%)</td><td>0.15 <b>(+26.65%)</b></td><td>0.12 <b>(+57.23%)</b></td><td>0.02 <b>(-55.83%)</b></td><td>0.16 (-7.00%)</td><td>0.14 (+19.75%)</td><td>0.15 <b>(+26.65%)</b></td><td>0.12 <b>(+57.23%)</b></td><td>0.02 <b>(-55.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.81 (-1.28%)</td><td>3.68 (+3.87%)</td><td>3.76 (+7.46%)</td><td>3.31 (-2.19%)</td><td>0.21 (+11.50%)</td><td>3.81 (-1.28%)</td><td>3.67 (+3.87%)</td><td>3.76 (+7.46%)</td><td>3.30 (-2.19%)</td><td>0.21 (+11.50%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.86 (n/a)</td><td>3.54 (n/a)</td><td>3.50 (n/a)</td><td>3.38 (n/a)</td><td>0.19 (n/a)</td><td>3.86 (n/a)</td><td>3.54 (n/a)</td><td>3.50 (n/a)</td><td>3.38 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>7.55 (+2.68%)</td><td>6.68 (+0.56%)</td><td>7.18 (-1.54%)</td><td>5.62 (+0.71%)</td><td>0.96 (+1.79%)</td><td>7.55 (+2.68%)</td><td>6.67 (+0.56%)</td><td>7.18 (-1.54%)</td><td>5.61 (+0.71%)</td><td>0.96 (+1.79%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>7.35 (n/a)</td><td>6.64 (n/a)</td><td>7.30 (n/a)</td><td>5.58 (n/a)</td><td>0.95 (n/a)</td><td>7.35 (n/a)</td><td>6.64 (n/a)</td><td>7.29 (n/a)</td><td>5.58 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>8.73 <b>(-36.88%)</b></td><td>7.98 (-19.96%)</td><td>8.15 (-7.79%)</td><td>7.22 (-13.06%)</td><td>0.68 <b>(-70.22%)</b></td><td>8.73 <b>(-36.88%)</b></td><td>7.97 (-19.96%)</td><td>8.15 (-7.79%)</td><td>7.21 (-13.06%)</td><td>0.68 <b>(-70.22%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>13.84 (n/a)</td><td>9.97 (n/a)</td><td>8.84 (n/a)</td><td>8.30 (n/a)</td><td>2.30 (n/a)</td><td>13.83 (n/a)</td><td>9.96 (n/a)</td><td>8.83 (n/a)</td><td>8.29 (n/a)</td><td>2.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.90 (+1.95%)</td><td>3.75 (+1.11%)</td><td>3.77 (+0.84%)</td><td>3.52 (+0.39%)</td><td>0.14 (+15.44%)</td><td>3.90 (+1.95%)</td><td>3.75 (+1.11%)</td><td>3.77 (+0.84%)</td><td>3.52 (+0.39%)</td><td>0.14 (+15.44%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.82 (n/a)</td><td>3.71 (n/a)</td><td>3.74 (n/a)</td><td>3.51 (n/a)</td><td>0.12 (n/a)</td><td>3.82 (n/a)</td><td>3.71 (n/a)</td><td>3.74 (n/a)</td><td>3.51 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.93 (-7.30%)</td><td>6.15 (-13.98%)</td><td>6.48 (-9.14%)</td><td>4.68 <b>(-30.75%)</b></td><td>0.92 <b>(+218.28%)</b></td><td>6.93 (-7.30%)</td><td>6.15 (-13.98%)</td><td>6.47 (-9.14%)</td><td>4.68 <b>(-30.75%)</b></td><td>0.92 <b>(+218.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>7.48 (n/a)</td><td>7.15 (n/a)</td><td>7.13 (n/a)</td><td>6.76 (n/a)</td><td>0.29 (n/a)</td><td>7.47 (n/a)</td><td>7.15 (n/a)</td><td>7.12 (n/a)</td><td>6.75 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>14.10 (-0.32%)</td><td>12.91 (+15.32%)</td><td>13.88 <b>(+21.24%)</b></td><td>9.23 <b>(+30.91%)</b></td><td>2.07 <b>(-29.71%)</b></td><td>14.09 (-0.32%)</td><td>12.90 (+15.32%)</td><td>13.88 <b>(+21.24%)</b></td><td>9.22 <b>(+30.91%)</b></td><td>2.07 <b>(-29.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>14.14 (n/a)</td><td>11.19 (n/a)</td><td>11.45 (n/a)</td><td>7.05 (n/a)</td><td>2.95 (n/a)</td><td>14.13 (n/a)</td><td>11.19 (n/a)</td><td>11.45 (n/a)</td><td>7.05 (n/a)</td><td>2.95 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.03 (+4.34%)</td><td>2.04 (+1.72%)</td><td>2.05 <b>(+20.26%)</b></td><td>1.09 (+6.43%)</td><td>0.87 (+4.02%)</td><td>3.02 (+4.34%)</td><td>2.04 (+1.72%)</td><td>2.05 <b>(+20.26%)</b></td><td>1.09 (+6.43%)</td><td>0.87 (+4.02%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.90 (n/a)</td><td>2.01 (n/a)</td><td>1.71 (n/a)</td><td>1.03 (n/a)</td><td>0.84 (n/a)</td><td>2.89 (n/a)</td><td>2.01 (n/a)</td><td>1.70 (n/a)</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.35 <b>(-21.10%)</b></td><td>0.18 <b>(-34.04%)</b></td><td>0.09 <b>(-69.44%)</b></td><td>0.07 (-1.61%)</td><td>0.14 (-14.75%)</td><td>0.34 <b>(-21.10%)</b></td><td>0.18 <b>(-34.04%)</b></td><td>0.09 <b>(-69.44%)</b></td><td>0.07 (-1.61%)</td><td>0.13 (-14.75%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>0.43 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.64 (-6.11%)</td><td>0.49 (-11.41%)</td><td>0.42 <b>(-37.35%)</b></td><td>0.35 <b>(+37.12%)</b></td><td>0.13 <b>(-35.33%)</b></td><td>0.63 (-6.11%)</td><td>0.48 (-11.41%)</td><td>0.42 <b>(-37.35%)</b></td><td>0.35 <b>(+37.12%)</b></td><td>0.12 <b>(-35.33%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.68 (n/a)</td><td>0.55 (n/a)</td><td>0.68 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.68 (n/a)</td><td>0.54 (n/a)</td><td>0.67 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.34 (-19.26%)</td><td>1.82 (+9.30%)</td><td>2.30 <b>(+69.44%)</b></td><td>0.44 (-0.39%)</td><td>0.82 (-14.01%)</td><td>2.30 (-19.26%)</td><td>1.79 (+9.30%)</td><td>2.26 <b>(+69.44%)</b></td><td>0.44 (-0.39%)</td><td>0.81 (-14.01%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.90 (n/a)</td><td>1.67 (n/a)</td><td>1.36 (n/a)</td><td>0.44 (n/a)</td><td>0.95 (n/a)</td><td>2.85 (n/a)</td><td>1.64 (n/a)</td><td>1.34 (n/a)</td><td>0.44 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.70 (n/a)</td><td>403.00 (n/a)</td><td>408.70 (n/a)</td><td>245.10 (n/a)</td><td>145.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1857.50 (n/a)</td><td>642.06 (n/a)</td><td>302.40 (n/a)</td><td>239.10 (n/a)</td><td>687.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>841.60 (n/a)</td><td>478.68 (n/a)</td><td>454.00 (n/a)</td><td>285.10 (n/a)</td><td>217.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1112.60 (n/a)</td><td>521.78 (n/a)</td><td>475.30 (n/a)</td><td>263.70 (n/a)</td><td>347.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.40 (n/a)</td><td>412.20 (n/a)</td><td>435.30 (n/a)</td><td>256.60 (n/a)</td><td>127.88 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.50 (n/a)</td><td>422.52 (n/a)</td><td>369.80 (n/a)</td><td>255.70 (n/a)</td><td>145.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.80 (n/a)</td><td>342.72 (n/a)</td><td>302.80 (n/a)</td><td>213.70 (n/a)</td><td>115.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.50 (n/a)</td><td>409.22 (n/a)</td><td>464.30 (n/a)</td><td>248.90 (n/a)</td><td>145.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>446.80 (n/a)</td><td>343.44 (n/a)</td><td>378.00 (n/a)</td><td>236.60 (n/a)</td><td>85.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.30 (n/a)</td><td>380.24 (n/a)</td><td>363.80 (n/a)</td><td>264.30 (n/a)</td><td>122.62 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1962.40 (n/a)</td><td>636.68 (n/a)</td><td>282.50 (n/a)</td><td>273.10 (n/a)</td><td>742.59 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.50 (n/a)</td><td>417.32 (n/a)</td><td>441.80 (n/a)</td><td>216.60 (n/a)</td><td>120.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>553.00 (n/a)</td><td>392.94 (n/a)</td><td>306.10 (n/a)</td><td>290.10 (n/a)</td><td>130.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2001.40 (n/a)</td><td>701.10 (n/a)</td><td>400.40 (n/a)</td><td>270.50 (n/a)</td><td>729.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>699.10 (n/a)</td><td>504.36 (n/a)</td><td>489.00 (n/a)</td><td>340.00 (n/a)</td><td>130.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>629.40 (n/a)</td><td>474.52 (n/a)</td><td>487.60 (n/a)</td><td>284.40 (n/a)</td><td>123.20 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>807.60 (n/a)</td><td>480.08 (n/a)</td><td>462.10 (n/a)</td><td>261.60 (n/a)</td><td>213.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>792.50 (n/a)</td><td>476.86 (n/a)</td><td>445.70 (n/a)</td><td>227.80 (n/a)</td><td>203.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (-2.19%)</td><td>0.09 (-5.37%)</td><td>0.08 (-10.85%)</td><td>0.05 (-8.55%)</td><td>0.03 (+5.09%)</td><td>668.00 (+9.35%)</td><td>423.36 (+7.32%)</td><td>387.30 (+12.16%)</td><td>286.30 (+2.25%)</td><td>155.54 (+15.19%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>610.90 (n/a)</td><td>394.50 (n/a)</td><td>345.30 (n/a)</td><td>280.00 (n/a)</td><td>135.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2503.90 (n/a)</td><td>838.14 (n/a)</td><td>391.90 (n/a)</td><td>307.60 (n/a)</td><td>942.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>624.40 (n/a)</td><td>490.72 (n/a)</td><td>581.70 (n/a)</td><td>310.20 (n/a)</td><td>159.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>598.80 (n/a)</td><td>372.94 (n/a)</td><td>304.40 (n/a)</td><td>292.20 (n/a)</td><td>129.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>618.60 (n/a)</td><td>440.10 (n/a)</td><td>412.80 (n/a)</td><td>283.20 (n/a)</td><td>162.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>587.10 (n/a)</td><td>485.00 (n/a)</td><td>501.60 (n/a)</td><td>373.00 (n/a)</td><td>104.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+9.36%)</td><td>0.01 (+8.89%)</td><td>0.01 (-3.06%)</td><td>0.01 <b>(+24.70%)</b></td><td>0.00 (-3.37%)</td><td>411.90 (-19.80%)</td><td>304.98 (-10.35%)</td><td>314.90 (+3.18%)</td><td>217.50 (-8.54%)</td><td>77.12 <b>(-30.69%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.60 (n/a)</td><td>340.18 (n/a)</td><td>305.20 (n/a)</td><td>237.80 (n/a)</td><td>111.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-12.80%)</td><td>0.01 (-6.68%)</td><td>0.01 (-4.55%)</td><td>0.01 (-1.68%)</td><td>0.00 (-18.60%)</td><td>512.00 (+1.71%)</td><td>342.06 (+3.41%)</td><td>305.80 (+4.76%)</td><td>214.70 (+14.63%)</td><td>132.10 (-7.70%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>503.40 (n/a)</td><td>330.78 (n/a)</td><td>291.90 (n/a)</td><td>187.30 (n/a)</td><td>143.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+2.78%)</td><td>0.01 (-1.08%)</td><td>0.01 <b>(+24.58%)</b></td><td>0.01 (-17.83%)</td><td>0.01 (+17.65%)</td><td>595.00 <b>(+21.70%)</b></td><td>380.24 (+7.86%)</td><td>304.70 (-19.73%)</td><td>228.10 (-2.73%)</td><td>171.66 <b>(+50.31%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.90 (n/a)</td><td>352.54 (n/a)</td><td>379.60 (n/a)</td><td>234.50 (n/a)</td><td>114.20 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-2.92%)</td><td>0.01 (-19.11%)</td><td>0.01 <b>(-44.37%)</b></td><td>0.01 (-9.96%)</td><td>0.00 (-17.48%)</td><td>607.60 (+11.06%)</td><td>425.24 (+19.21%)</td><td>445.50 <b>(+79.78%)</b></td><td>238.40 (+3.03%)</td><td>148.79 (-7.25%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.10 (n/a)</td><td>356.72 (n/a)</td><td>247.80 (n/a)</td><td>231.40 (n/a)</td><td>160.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+4.22%)</td><td>0.01 (-3.57%)</td><td>0.01 (-5.54%)</td><td>0.00 <b>(-75.37%)</b></td><td>0.01 <b>(+42.27%)</b></td><td>2448.20 <b>(+306.00%)</b></td><td>781.34 <b>(+86.66%)</b></td><td>451.30 (+5.86%)</td><td>202.50 (-4.07%)</td><td>942.27 <b>(+493.18%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.00 (n/a)</td><td>418.58 (n/a)</td><td>426.30 (n/a)</td><td>211.10 (n/a)</td><td>158.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (+4.38%)</td><td>0.01 <b>(-20.73%)</b></td><td>0.01 <b>(-25.35%)</b></td><td>0.00 <b>(-73.39%)</b></td><td>0.00 <b>(+76.78%)</b></td><td>2206.20 <b>(+275.72%)</b></td><td>820.18 <b>(+88.16%)</b></td><td>536.50 <b>(+33.96%)</b></td><td>290.30 (-4.19%)</td><td>783.25 <b>(+623.09%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.20 (n/a)</td><td>435.90 (n/a)</td><td>400.50 (n/a)</td><td>303.00 (n/a)</td><td>108.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (-6.37%)</td><td>0.03 (-4.85%)</td><td>0.03 (-14.89%)</td><td>0.01 <b>(+20.46%)</b></td><td>0.01 (-19.59%)</td><td>574.90 (-16.98%)</td><td>343.82 (-2.60%)</td><td>291.90 (+17.46%)</td><td>228.20 (+6.84%)</td><td>142.12 <b>(-29.17%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>692.50 (n/a)</td><td>352.98 (n/a)</td><td>248.50 (n/a)</td><td>213.60 (n/a)</td><td>200.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 <b>(+21.26%)</b></td><td>0.02 (+16.14%)</td><td>0.02 (-0.15%)</td><td>0.01 <b>(-20.04%)</b></td><td>0.01 <b>(+65.39%)</b></td><td>746.40 <b>(+25.07%)</b></td><td>429.92 (-3.31%)</td><td>452.60 (+0.15%)</td><td>219.10 (-17.54%)</td><td>208.53 <b>(+72.54%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.80 (n/a)</td><td>444.64 (n/a)</td><td>451.90 (n/a)</td><td>265.70 (n/a)</td><td>120.86 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+1.22%)</td><td>0.03 (+19.69%)</td><td>0.03 <b>(+41.36%)</b></td><td>0.02 <b>(+60.21%)</b></td><td>0.01 <b>(-31.91%)</b></td><td>397.50 <b>(-37.59%)</b></td><td>315.88 <b>(-23.14%)</b></td><td>294.20 <b>(-29.24%)</b></td><td>242.10 (-1.18%)</td><td>71.60 <b>(-55.27%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.90 (n/a)</td><td>411.00 (n/a)</td><td>415.80 (n/a)</td><td>245.00 (n/a)</td><td>160.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (+8.68%)</td><td>0.02 (-9.11%)</td><td>0.02 <b>(-26.96%)</b></td><td>0.02 (+9.74%)</td><td>0.01 (+10.95%)</td><td>426.50 (-8.89%)</td><td>350.82 (+10.15%)</td><td>387.90 <b>(+36.92%)</b></td><td>229.60 (-8.01%)</td><td>82.60 (-7.73%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.10 (n/a)</td><td>318.48 (n/a)</td><td>283.30 (n/a)</td><td>249.60 (n/a)</td><td>89.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-19.13%)</td><td>0.02 (+0.40%)</td><td>0.03 <b>(+47.59%)</b></td><td>0.02 (+7.03%)</td><td>0.01 <b>(-24.69%)</b></td><td>536.70 (-6.56%)</td><td>378.06 (-4.64%)</td><td>287.40 <b>(-32.25%)</b></td><td>265.50 <b>(+23.66%)</b></td><td>141.69 (-10.11%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.40 (n/a)</td><td>396.44 (n/a)</td><td>424.20 (n/a)</td><td>214.70 (n/a)</td><td>157.62 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+1.25%)</td><td>0.02 (+4.75%)</td><td>0.03 (+14.95%)</td><td>0.02 (-0.37%)</td><td>0.01 (-0.89%)</td><td>526.20 (+0.36%)</td><td>376.14 (-4.60%)</td><td>322.60 (-13.00%)</td><td>301.60 (-1.24%)</td><td>96.04 (-0.52%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.30 (n/a)</td><td>394.26 (n/a)</td><td>370.80 (n/a)</td><td>305.40 (n/a)</td><td>96.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-8.11%)</td><td>0.02 (-4.30%)</td><td>0.02 (-2.72%)</td><td>0.02 (+13.07%)</td><td>0.01 (-18.75%)</td><td>540.30 (-11.56%)</td><td>392.80 (-0.18%)</td><td>342.30 (+2.79%)</td><td>241.60 (+8.83%)</td><td>136.30 (-18.60%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.90 (n/a)</td><td>393.50 (n/a)</td><td>333.00 (n/a)</td><td>222.00 (n/a)</td><td>167.44 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-16.91%)</td><td>0.02 (+10.95%)</td><td>0.02 (+12.00%)</td><td>0.01 <b>(+306.78%)</b></td><td>0.00 <b>(-55.50%)</b></td><td>595.00 <b>(-75.42%)</b></td><td>464.56 <b>(-44.05%)</b></td><td>437.30 (-10.72%)</td><td>368.00 <b>(+20.38%)</b></td><td>100.42 <b>(-88.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2420.40 (n/a)</td><td>830.30 (n/a)</td><td>489.80 (n/a)</td><td>305.70 (n/a)</td><td>892.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (+5.72%)</td><td>0.06 <b>(+36.19%)</b></td><td>0.06 <b>(+57.56%)</b></td><td>0.05 <b>(+60.98%)</b></td><td>0.00 <b>(-63.91%)</b></td><td>317.30 <b>(-37.88%)</b></td><td>292.62 <b>(-30.30%)</b></td><td>296.00 <b>(-36.52%)</b></td><td>261.40 (-5.39%)</td><td>21.26 <b>(-79.27%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>510.80 (n/a)</td><td>419.80 (n/a)</td><td>466.30 (n/a)</td><td>276.30 (n/a)</td><td>102.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (-0.53%)</td><td>0.06 (-3.53%)</td><td>0.06 (-14.20%)</td><td>0.03 (+4.13%)</td><td>0.02 (-9.10%)</td><td>490.00 (-3.96%)</td><td>309.30 (+1.76%)</td><td>296.00 (+16.54%)</td><td>215.10 (+0.56%)</td><td>106.69 (-11.47%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>510.20 (n/a)</td><td>303.96 (n/a)</td><td>254.00 (n/a)</td><td>213.90 (n/a)</td><td>120.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-8.35%)</td><td>0.04 (+14.82%)</td><td>0.04 (+15.02%)</td><td>0.03 <b>(+310.58%)</b></td><td>0.02 <b>(-27.92%)</b></td><td>592.00 <b>(-75.65%)</b></td><td>410.20 <b>(-48.16%)</b></td><td>413.30 (-13.06%)</td><td>241.90 (+9.11%)</td><td>151.40 <b>(-83.59%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2430.80 (n/a)</td><td>791.34 (n/a)</td><td>475.40 (n/a)</td><td>221.70 (n/a)</td><td>922.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (+7.21%)</td><td>0.04 (-11.25%)</td><td>0.03 <b>(-35.96%)</b></td><td>0.03 (-7.66%)</td><td>0.02 <b>(+31.50%)</b></td><td>540.10 (+8.30%)</td><td>413.62 (+17.63%)</td><td>483.50 <b>(+56.17%)</b></td><td>230.20 (-6.73%)</td><td>132.83 <b>(+31.62%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>498.70 (n/a)</td><td>351.64 (n/a)</td><td>309.60 (n/a)</td><td>246.80 (n/a)</td><td>100.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-2.80%)</td><td>0.04 (-11.15%)</td><td>0.03 <b>(-29.34%)</b></td><td>0.03 (-6.25%)</td><td>0.02 (+8.87%)</td><td>594.10 (+6.66%)</td><td>418.30 (+15.71%)</td><td>478.80 <b>(+41.53%)</b></td><td>237.20 (+2.91%)</td><td>153.72 (+17.10%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>557.00 (n/a)</td><td>361.50 (n/a)</td><td>338.30 (n/a)</td><td>230.50 (n/a)</td><td>131.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 <b>(+42.12%)</b></td><td>0.04 (+11.03%)</td><td>0.03 (-17.10%)</td><td>0.03 (-3.34%)</td><td>0.02 <b>(+237.24%)</b></td><td>532.30 (+3.46%)</td><td>412.18 (-1.27%)</td><td>473.20 <b>(+20.62%)</b></td><td>261.10 <b>(-29.64%)</b></td><td>138.02 <b>(+138.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>514.50 (n/a)</td><td>417.48 (n/a)</td><td>392.30 (n/a)</td><td>371.10 (n/a)</td><td>57.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 <b>(+28.01%)</b></td><td>0.11 <b>(+53.82%)</b></td><td>0.11 <b>(+50.00%)</b></td><td>0.07 <b>(+67.05%)</b></td><td>0.03 (+0.17%)</td><td>483.50 <b>(-40.14%)</b></td><td>318.14 <b>(-38.53%)</b></td><td>286.80 <b>(-33.32%)</b></td><td>238.10 <b>(-21.88%)</b></td><td>96.13 <b>(-51.74%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>807.70 (n/a)</td><td>517.54 (n/a)</td><td>430.10 (n/a)</td><td>304.80 (n/a)</td><td>199.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (+9.62%)</td><td>0.11 <b>(+27.05%)</b></td><td>0.11 <b>(+77.10%)</b></td><td>0.07 (+17.14%)</td><td>0.03 (-13.15%)</td><td>491.60 (-14.64%)</td><td>327.26 <b>(-24.36%)</b></td><td>285.20 <b>(-43.52%)</b></td><td>238.20 (-8.81%)</td><td>100.31 <b>(-29.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>575.90 (n/a)</td><td>432.68 (n/a)</td><td>505.00 (n/a)</td><td>261.20 (n/a)</td><td>142.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 <b>(-37.88%)</b></td><td>0.06 (-19.60%)</td><td>0.07 <b>(+30.82%)</b></td><td>0.02 <b>(-65.92%)</b></td><td>0.03 <b>(-29.39%)</b></td><td>2117.60 <b>(+193.46%)</b></td><td>771.92 <b>(+56.59%)</b></td><td>458.50 <b>(-23.56%)</b></td><td>365.70 <b>(+60.96%)</b></td><td>755.52 <b>(+258.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>721.60 (n/a)</td><td>492.96 (n/a)</td><td>599.80 (n/a)</td><td>227.20 (n/a)</td><td>210.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (-4.68%)</td><td>0.08 (-12.84%)</td><td>0.06 <b>(-37.71%)</b></td><td>0.06 (-16.53%)</td><td>0.03 <b>(+21.16%)</b></td><td>580.60 (+19.81%)</td><td>444.08 (+18.28%)</td><td>511.20 <b>(+60.55%)</b></td><td>306.20 (+4.93%)</td><td>128.73 <b>(+39.89%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>484.60 (n/a)</td><td>375.46 (n/a)</td><td>318.40 (n/a)</td><td>291.80 (n/a)</td><td>92.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 <b>(-21.44%)</b></td><td>0.07 (+4.89%)</td><td>0.06 (-12.99%)</td><td>0.05 <b>(+225.33%)</b></td><td>0.02 <b>(-47.54%)</b></td><td>619.70 <b>(-69.26%)</b></td><td>489.96 <b>(-34.69%)</b></td><td>543.90 (+14.92%)</td><td>358.50 <b>(+27.31%)</b></td><td>121.05 <b>(-83.04%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2015.90 (n/a)</td><td>750.24 (n/a)</td><td>473.30 (n/a)</td><td>281.60 (n/a)</td><td>713.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-5.75%)</td><td>0.01 (-0.55%)</td><td>0.01 (+17.52%)</td><td>0.01 (+5.85%)</td><td>0.00 <b>(-35.33%)</b></td><td>490.20 (-5.53%)</td><td>373.28 (-5.71%)</td><td>400.30 (-14.90%)</td><td>259.40 (+6.09%)</td><td>89.17 <b>(-34.47%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.90 (n/a)</td><td>395.90 (n/a)</td><td>470.40 (n/a)</td><td>244.50 (n/a)</td><td>136.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 <b>(-25.47%)</b></td><td>0.01 <b>(-27.25%)</b></td><td>0.01 <b>(-29.70%)</b></td><td>0.01 (-5.16%)</td><td>0.00 <b>(-38.98%)</b></td><td>566.20 (+5.44%)</td><td>416.40 <b>(+31.56%)</b></td><td>391.10 <b>(+42.27%)</b></td><td>308.60 <b>(+34.17%)</b></td><td>101.70 (-18.67%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.00 (n/a)</td><td>316.50 (n/a)</td><td>274.90 (n/a)</td><td>230.00 (n/a)</td><td>125.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 <b>(-37.90%)</b></td><td>0.01 <b>(-36.67%)</b></td><td>0.01 <b>(-40.61%)</b></td><td>0.00 <b>(-63.99%)</b></td><td>0.00 <b>(-38.76%)</b></td><td>2124.20 <b>(+177.71%)</b></td><td>801.44 <b>(+85.10%)</b></td><td>492.60 <b>(+68.35%)</b></td><td>386.60 <b>(+61.02%)</b></td><td>741.08 <b>(+213.09%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>764.90 (n/a)</td><td>432.98 (n/a)</td><td>292.60 (n/a)</td><td>240.10 (n/a)</td><td>236.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+0.15%)</td><td>0.01 (+0.38%)</td><td>0.01 (+0.50%)</td><td>0.01 (+13.12%)</td><td>0.00 (-2.05%)</td><td>527.20 (-11.60%)</td><td>365.08 (-1.72%)</td><td>326.10 (-0.49%)</td><td>244.80 (-0.16%)</td><td>119.03 (-14.41%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.40 (n/a)</td><td>371.48 (n/a)</td><td>327.70 (n/a)</td><td>245.20 (n/a)</td><td>139.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 <b>(-22.34%)</b></td><td>0.01 <b>(-40.43%)</b></td><td>0.01 <b>(-49.52%)</b></td><td>0.01 <b>(-39.70%)</b></td><td>0.00 (-1.09%)</td><td>616.20 <b>(+65.82%)</b></td><td>466.24 <b>(+74.49%)</b></td><td>480.40 <b>(+98.10%)</b></td><td>260.00 <b>(+28.78%)</b></td><td>129.66 <b>(+93.27%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>371.60 (n/a)</td><td>267.20 (n/a)</td><td>242.50 (n/a)</td><td>201.90 (n/a)</td><td>67.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (-17.37%)</td><td>0.01 <b>(-41.68%)</b></td><td>0.01 <b>(-45.38%)</b></td><td>0.00 <b>(-82.96%)</b></td><td>0.01 <b>(+216.03%)</b></td><td>1861.70 <b>(+487.10%)</b></td><td>716.72 <b>(+167.07%)</b></td><td>476.20 <b>(+83.08%)</b></td><td>292.80 <b>(+20.99%)</b></td><td>657.71 <b>(+2076.40%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>317.10 (n/a)</td><td>268.36 (n/a)</td><td>260.10 (n/a)</td><td>242.00 (n/a)</td><td>30.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+11.49%)</td><td>0.01 (-15.17%)</td><td>0.01 (-14.89%)</td><td>0.01 (+4.54%)</td><td>0.01 (+7.78%)</td><td>568.10 (-4.34%)</td><td>467.06 (+18.72%)</td><td>519.00 (+17.47%)</td><td>208.70 (-10.31%)</td><td>149.74 (-3.01%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.90 (n/a)</td><td>393.42 (n/a)</td><td>441.80 (n/a)</td><td>232.70 (n/a)</td><td>154.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-1.42%)</td><td>0.01 (-19.17%)</td><td>0.01 <b>(-31.84%)</b></td><td>0.01 (+7.87%)</td><td>0.00 (-9.83%)</td><td>637.90 (-7.30%)</td><td>454.94 (+19.08%)</td><td>452.30 <b>(+46.71%)</b></td><td>233.00 (+1.44%)</td><td>156.37 (-17.16%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>688.10 (n/a)</td><td>382.06 (n/a)</td><td>308.30 (n/a)</td><td>229.70 (n/a)</td><td>188.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-6.14%)</td><td>0.01 <b>(-25.39%)</b></td><td>0.01 (-17.48%)</td><td>0.01 <b>(-43.08%)</b></td><td>0.00 <b>(+158.80%)</b></td><td>536.60 <b>(+75.70%)</b></td><td>387.12 <b>(+43.22%)</b></td><td>330.00 <b>(+21.19%)</b></td><td>257.80 (+6.53%)</td><td>116.86 <b>(+398.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>305.40 (n/a)</td><td>270.30 (n/a)</td><td>272.30 (n/a)</td><td>242.00 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-1.44%)</td><td>0.01 (-11.51%)</td><td>0.01 (-14.74%)</td><td>0.01 (-17.29%)</td><td>0.00 (-0.44%)</td><td>642.70 <b>(+20.90%)</b></td><td>421.30 (+15.23%)</td><td>423.30 (+17.29%)</td><td>246.30 (+1.44%)</td><td>154.66 <b>(+25.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.60 (n/a)</td><td>365.62 (n/a)</td><td>360.90 (n/a)</td><td>242.80 (n/a)</td><td>123.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 <b>(-20.72%)</b></td><td>0.01 (-3.38%)</td><td>0.01 (-10.45%)</td><td>0.01 (+6.37%)</td><td>0.00 <b>(-31.78%)</b></td><td>616.70 (-5.99%)</td><td>433.16 (-2.39%)</td><td>472.40 (+11.65%)</td><td>274.90 <b>(+26.16%)</b></td><td>135.60 (-19.30%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>656.00 (n/a)</td><td>443.76 (n/a)</td><td>423.10 (n/a)</td><td>217.90 (n/a)</td><td>168.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 <b>(+20.55%)</b></td><td>0.01 <b>(+20.35%)</b></td><td>0.01 (+16.78%)</td><td>0.01 (-3.66%)</td><td>0.00 <b>(+41.38%)</b></td><td>649.60 (+3.80%)</td><td>448.66 (-13.05%)</td><td>490.40 (-14.37%)</td><td>252.90 (-17.05%)</td><td>156.81 <b>(+24.14%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>625.80 (n/a)</td><td>516.00 (n/a)</td><td>572.70 (n/a)</td><td>304.90 (n/a)</td><td>126.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-1.67%)</td><td>0.02 (-10.39%)</td><td>0.03 (-2.01%)</td><td>0.02 <b>(-24.69%)</b></td><td>0.01 <b>(+42.26%)</b></td><td>522.40 <b>(+32.79%)</b></td><td>359.72 (+17.34%)</td><td>313.80 (+2.08%)</td><td>234.70 (+1.69%)</td><td>115.24 <b>(+96.63%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>393.40 (n/a)</td><td>306.56 (n/a)</td><td>307.40 (n/a)</td><td>230.80 (n/a)</td><td>58.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-0.91%)</td><td>0.02 <b>(-22.06%)</b></td><td>0.02 <b>(-32.35%)</b></td><td>0.02 <b>(-37.84%)</b></td><td>0.01 <b>(+121.61%)</b></td><td>514.40 <b>(+60.85%)</b></td><td>400.42 <b>(+38.57%)</b></td><td>439.50 <b>(+47.83%)</b></td><td>239.70 (+0.93%)</td><td>121.59 <b>(+270.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>319.80 (n/a)</td><td>288.96 (n/a)</td><td>297.30 (n/a)</td><td>237.50 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-9.92%)</td><td>0.02 (+2.20%)</td><td>0.02 (-7.82%)</td><td>0.01 (+2.79%)</td><td>0.01 (-3.42%)</td><td>620.90 (-2.71%)</td><td>461.12 (-2.51%)</td><td>533.90 (+8.47%)</td><td>296.30 (+11.02%)</td><td>151.42 (-2.46%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.20 (n/a)</td><td>473.00 (n/a)</td><td>492.20 (n/a)</td><td>266.90 (n/a)</td><td>155.23 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-19.74%)</td><td>0.02 <b>(-25.95%)</b></td><td>0.02 <b>(-36.71%)</b></td><td>0.00 <b>(-69.33%)</b></td><td>0.01 (+6.38%)</td><td>1863.50 <b>(+226.01%)</b></td><td>686.18 <b>(+87.30%)</b></td><td>467.20 <b>(+58.00%)</b></td><td>282.20 <b>(+24.59%)</b></td><td>665.11 <b>(+352.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.60 (n/a)</td><td>366.36 (n/a)</td><td>295.70 (n/a)</td><td>226.50 (n/a)</td><td>147.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (-13.88%)</td><td>0.03 (-13.37%)</td><td>0.03 (-4.35%)</td><td>0.01 (-4.10%)</td><td>0.01 (+7.89%)</td><td>547.50 (+4.29%)</td><td>365.98 <b>(+20.71%)</b></td><td>270.40 (+4.52%)</td><td>226.10 (+16.13%)</td><td>165.57 <b>(+28.56%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.00 (n/a)</td><td>303.20 (n/a)</td><td>258.70 (n/a)</td><td>194.70 (n/a)</td><td>128.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+0.22%)</td><td>0.02 (-14.54%)</td><td>0.02 <b>(-36.78%)</b></td><td>0.01 (-3.56%)</td><td>0.01 (+9.98%)</td><td>546.70 (+3.68%)</td><td>416.94 (+19.48%)</td><td>462.40 <b>(+58.19%)</b></td><td>245.80 (-0.20%)</td><td>135.57 (+15.47%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.30 (n/a)</td><td>348.96 (n/a)</td><td>292.30 (n/a)</td><td>246.30 (n/a)</td><td>117.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-8.08%)</td><td>0.02 (-6.98%)</td><td>0.03 <b>(+40.32%)</b></td><td>0.01 <b>(-62.55%)</b></td><td>0.01 <b>(+34.91%)</b></td><td>1312.50 <b>(+167.04%)</b></td><td>549.84 <b>(+42.98%)</b></td><td>308.40 <b>(-28.74%)</b></td><td>246.80 (+8.82%)</td><td>447.38 <b>(+292.67%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.50 (n/a)</td><td>384.56 (n/a)</td><td>432.80 (n/a)</td><td>226.80 (n/a)</td><td>113.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-8.20%)</td><td>0.03 (+8.86%)</td><td>0.03 <b>(+39.11%)</b></td><td>0.02 (+11.24%)</td><td>0.00 <b>(-37.09%)</b></td><td>456.10 (-10.11%)</td><td>330.08 (-12.15%)</td><td>303.10 <b>(-28.11%)</b></td><td>265.50 (+8.95%)</td><td>73.48 <b>(-33.81%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.40 (n/a)</td><td>375.72 (n/a)</td><td>421.60 (n/a)</td><td>243.70 (n/a)</td><td>111.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 <b>(-25.52%)</b></td><td>0.02 (-7.60%)</td><td>0.02 (-14.68%)</td><td>0.01 (-10.15%)</td><td>0.01 (-19.59%)</td><td>602.60 (+11.30%)</td><td>431.52 (+7.93%)</td><td>493.20 (+17.21%)</td><td>265.00 <b>(+34.25%)</b></td><td>155.52 (+18.03%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.40 (n/a)</td><td>399.82 (n/a)</td><td>420.80 (n/a)</td><td>197.40 (n/a)</td><td>131.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+0.15%)</td><td>0.02 (+16.99%)</td><td>0.03 <b>(+46.00%)</b></td><td>0.02 (+4.80%)</td><td>0.01 (+12.60%)</td><td>518.10 (-4.59%)</td><td>366.18 (-12.28%)</td><td>286.90 <b>(-31.49%)</b></td><td>244.70 (-0.16%)</td><td>131.50 <b>(+20.27%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.00 (n/a)</td><td>417.42 (n/a)</td><td>418.80 (n/a)</td><td>245.10 (n/a)</td><td>109.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 <b>(-29.58%)</b></td><td>0.01 <b>(-39.54%)</b></td><td>0.01 <b>(-37.81%)</b></td><td>0.00 <b>(-78.76%)</b></td><td>0.01 <b>(+57.53%)</b></td><td>2102.40 <b>(+370.86%)</b></td><td>819.14 <b>(+130.43%)</b></td><td>550.20 <b>(+60.78%)</b></td><td>399.80 <b>(+42.02%)</b></td><td>721.80 <b>(+1047.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>446.50 (n/a)</td><td>355.48 (n/a)</td><td>342.20 (n/a)</td><td>281.50 (n/a)</td><td>62.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+11.96%)</td><td>0.02 (+0.90%)</td><td>0.02 (-18.28%)</td><td>0.01 (-6.62%)</td><td>0.01 (+14.53%)</td><td>664.40 (+7.09%)</td><td>415.40 (+1.54%)</td><td>358.60 <b>(+22.35%)</b></td><td>248.50 (-10.71%)</td><td>184.32 (+7.63%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.40 (n/a)</td><td>409.08 (n/a)</td><td>293.10 (n/a)</td><td>278.30 (n/a)</td><td>171.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 <b>(-25.96%)</b></td><td>0.05 (-4.25%)</td><td>0.05 <b>(+68.66%)</b></td><td>0.03 (-17.32%)</td><td>0.02 <b>(-44.33%)</b></td><td>650.10 <b>(+20.95%)</b></td><td>368.76 (-6.96%)</td><td>305.50 <b>(-40.71%)</b></td><td>232.10 <b>(+35.10%)</b></td><td>165.04 (-10.02%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>537.50 (n/a)</td><td>396.34 (n/a)</td><td>515.30 (n/a)</td><td>171.80 (n/a)</td><td>183.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (-18.00%)</td><td>0.05 (+11.44%)</td><td>0.05 <b>(+53.35%)</b></td><td>0.03 (+18.23%)</td><td>0.01 <b>(-40.76%)</b></td><td>497.70 (-15.43%)</td><td>361.48 (-17.19%)</td><td>314.80 <b>(-34.80%)</b></td><td>287.20 <b>(+21.95%)</b></td><td>91.86 <b>(-41.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.50 (n/a)</td><td>436.52 (n/a)</td><td>482.80 (n/a)</td><td>235.50 (n/a)</td><td>156.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (+0.57%)</td><td>0.05 (-15.47%)</td><td>0.05 (-6.59%)</td><td>0.03 <b>(-34.41%)</b></td><td>0.02 <b>(+56.85%)</b></td><td>618.70 <b>(+52.46%)</b></td><td>389.88 <b>(+27.71%)</b></td><td>318.00 (+7.07%)</td><td>241.50 (-0.58%)</td><td>149.69 <b>(+139.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>405.80 (n/a)</td><td>305.28 (n/a)</td><td>297.00 (n/a)</td><td>242.90 (n/a)</td><td>62.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-8.50%)</td><td>0.04 (-17.69%)</td><td>0.03 <b>(-35.83%)</b></td><td>0.02 (-13.02%)</td><td>0.02 (-11.45%)</td><td>737.90 (+14.97%)</td><td>452.16 <b>(+20.18%)</b></td><td>486.10 <b>(+55.85%)</b></td><td>223.60 (+9.29%)</td><td>196.62 (+8.02%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>641.80 (n/a)</td><td>376.24 (n/a)</td><td>311.90 (n/a)</td><td>204.60 (n/a)</td><td>182.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (-15.19%)</td><td>0.04 <b>(-26.25%)</b></td><td>0.03 <b>(-47.08%)</b></td><td>0.03 (-7.32%)</td><td>0.02 <b>(-24.14%)</b></td><td>607.60 (+7.90%)</td><td>453.70 <b>(+31.21%)</b></td><td>471.90 <b>(+88.99%)</b></td><td>259.60 (+17.95%)</td><td>153.54 (+0.14%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>563.10 (n/a)</td><td>345.78 (n/a)</td><td>249.70 (n/a)</td><td>220.10 (n/a)</td><td>153.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (-17.13%)</td><td>0.04 (-16.12%)</td><td>0.03 <b>(-27.73%)</b></td><td>0.03 (+0.11%)</td><td>0.01 <b>(-32.71%)</b></td><td>577.70 (-0.12%)</td><td>455.04 (+12.34%)</td><td>522.90 <b>(+38.37%)</b></td><td>294.00 <b>(+20.69%)</b></td><td>130.29 (-19.89%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>578.40 (n/a)</td><td>405.04 (n/a)</td><td>377.90 (n/a)</td><td>243.60 (n/a)</td><td>162.63 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (+18.04%)</td><td>0.04 (-12.16%)</td><td>0.03 <b>(-41.01%)</b></td><td>0.03 <b>(+22.46%)</b></td><td>0.02 (+5.95%)</td><td>513.80 (-18.35%)</td><td>422.80 (+10.68%)</td><td>486.90 <b>(+69.53%)</b></td><td>210.20 (-15.28%)</td><td>127.73 <b>(-25.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>629.30 (n/a)</td><td>382.00 (n/a)</td><td>287.20 (n/a)</td><td>248.10 (n/a)</td><td>170.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (-18.17%)</td><td>0.04 (-18.72%)</td><td>0.05 <b>(-27.47%)</b></td><td>0.02 (-18.67%)</td><td>0.01 <b>(-27.55%)</b></td><td>668.00 <b>(+22.95%)</b></td><td>417.12 <b>(+20.21%)</b></td><td>346.50 <b>(+37.88%)</b></td><td>292.40 <b>(+22.24%)</b></td><td>157.15 (+11.32%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>543.30 (n/a)</td><td>346.98 (n/a)</td><td>251.30 (n/a)</td><td>239.20 (n/a)</td><td>141.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (+0.27%)</td><td>0.04 <b>(-22.49%)</b></td><td>0.03 <b>(-39.55%)</b></td><td>0.03 (+3.15%)</td><td>0.02 (-7.47%)</td><td>623.20 (-3.05%)</td><td>516.04 <b>(+25.06%)</b></td><td>563.40 <b>(+65.41%)</b></td><td>242.00 (-0.29%)</td><td>155.34 (-15.92%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.80 (n/a)</td><td>412.62 (n/a)</td><td>340.60 (n/a)</td><td>242.70 (n/a)</td><td>184.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 <b>(-32.84%)</b></td><td>0.04 <b>(-33.49%)</b></td><td>0.03 <b>(-41.06%)</b></td><td>0.03 (+3.98%)</td><td>0.01 <b>(-63.56%)</b></td><td>553.70 (-3.82%)</td><td>464.12 <b>(+38.68%)</b></td><td>469.30 <b>(+69.67%)</b></td><td>361.20 <b>(+48.89%)</b></td><td>68.57 <b>(-50.53%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>575.70 (n/a)</td><td>334.66 (n/a)</td><td>276.60 (n/a)</td><td>242.60 (n/a)</td><td>138.59 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 <b>(-25.44%)</b></td><td>0.03 <b>(-34.56%)</b></td><td>0.03 <b>(-22.94%)</b></td><td>0.01 <b>(-68.56%)</b></td><td>0.01 (+4.05%)</td><td>1921.30 <b>(+218.04%)</b></td><td>830.56 <b>(+95.50%)</b></td><td>550.60 <b>(+29.77%)</b></td><td>352.10 <b>(+34.08%)</b></td><td>631.50 <b>(+386.64%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>604.10 (n/a)</td><td>424.84 (n/a)</td><td>424.30 (n/a)</td><td>262.60 (n/a)</td><td>129.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (-8.28%)</td><td>0.05 (-7.66%)</td><td>0.05 (-9.26%)</td><td>0.03 (-4.24%)</td><td>0.01 (-11.42%)</td><td>515.20 (+4.44%)</td><td>384.34 (+7.51%)</td><td>346.80 (+10.20%)</td><td>257.50 (+9.02%)</td><td>109.64 (+1.16%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>493.30 (n/a)</td><td>357.50 (n/a)</td><td>314.70 (n/a)</td><td>236.20 (n/a)</td><td>108.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (-17.19%)</td><td>0.10 (-7.73%)</td><td>0.11 (-10.16%)</td><td>0.07 <b>(+29.11%)</b></td><td>0.02 <b>(-43.07%)</b></td><td>496.00 <b>(-22.55%)</b></td><td>344.82 (-0.34%)</td><td>309.10 (+11.31%)</td><td>300.50 <b>(+20.78%)</b></td><td>84.66 <b>(-48.86%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>640.40 (n/a)</td><td>345.98 (n/a)</td><td>277.70 (n/a)</td><td>248.80 (n/a)</td><td>165.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (-11.18%)</td><td>0.09 (-2.21%)</td><td>0.09 (+17.72%)</td><td>0.05 (-13.83%)</td><td>0.02 (-19.82%)</td><td>643.40 (+16.03%)</td><td>401.04 (+1.17%)</td><td>345.20 (-15.06%)</td><td>293.10 (+12.60%)</td><td>143.94 (+10.44%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>554.50 (n/a)</td><td>396.42 (n/a)</td><td>406.40 (n/a)</td><td>260.30 (n/a)</td><td>130.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (-15.83%)</td><td>0.08 <b>(-21.69%)</b></td><td>0.07 (+7.66%)</td><td>0.02 <b>(-68.54%)</b></td><td>0.04 (-10.37%)</td><td>1952.30 <b>(+217.81%)</b></td><td>702.68 <b>(+72.69%)</b></td><td>440.10 (-7.13%)</td><td>241.40 (+18.80%)</td><td>704.17 <b>(+305.20%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>614.30 (n/a)</td><td>406.90 (n/a)</td><td>473.90 (n/a)</td><td>203.20 (n/a)</td><td>173.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (+16.69%)</td><td>0.09 (+0.83%)</td><td>0.08 (+17.85%)</td><td>0.05 (-16.13%)</td><td>0.03 (+4.80%)</td><td>636.40 (+19.22%)</td><td>410.68 (-0.32%)</td><td>410.40 (-15.14%)</td><td>224.00 (-14.27%)</td><td>148.17 (+7.55%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>533.80 (n/a)</td><td>412.00 (n/a)</td><td>483.60 (n/a)</td><td>261.30 (n/a)</td><td>137.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (-4.51%)</td><td>0.10 (-8.92%)</td><td>0.11 (-10.12%)</td><td>0.06 (-3.67%)</td><td>0.03 (-2.32%)</td><td>572.40 (+3.81%)</td><td>368.60 (+10.22%)</td><td>295.10 (+11.27%)</td><td>232.50 (+4.73%)</td><td>141.15 (+5.96%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.40 (n/a)</td><td>334.42 (n/a)</td><td>265.20 (n/a)</td><td>222.00 (n/a)</td><td>133.21 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (+7.97%)</td><td>0.08 (-14.88%)</td><td>0.08 (-1.53%)</td><td>0.02 <b>(-76.03%)</b></td><td>0.04 <b>(+76.43%)</b></td><td>1968.20 <b>(+317.17%)</b></td><td>705.84 <b>(+83.51%)</b></td><td>434.10 (+1.54%)</td><td>242.20 (-7.38%)</td><td>714.16 <b>(+657.29%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>471.80 (n/a)</td><td>384.64 (n/a)</td><td>427.50 (n/a)</td><td>261.50 (n/a)</td><td>94.30 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.21 <b>(+165.36%)</b></td><td>0.11 <b>(+62.33%)</b></td><td>0.10 <b>(+44.69%)</b></td><td>0.06 <b>(+45.19%)</b></td><td>0.06 <b>(+319.76%)</b></td><td>510.30 <b>(-31.12%)</b></td><td>358.44 <b>(-29.31%)</b></td><td>319.60 <b>(-30.88%)</b></td><td>157.60 <b>(-62.31%)</b></td><td>149.12 (+10.96%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>740.90 (n/a)</td><td>507.04 (n/a)</td><td>462.40 (n/a)</td><td>418.20 (n/a)</td><td>134.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (+8.66%)</td><td>0.07 (-2.40%)</td><td>0.07 (+19.65%)</td><td>0.05 (-12.29%)</td><td>0.03 (+16.05%)</td><td>712.30 (+14.02%)</td><td>519.90 (+5.89%)</td><td>457.40 (-16.43%)</td><td>286.50 (-7.97%)</td><td>184.61 <b>(+27.13%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>624.70 (n/a)</td><td>490.98 (n/a)</td><td>547.30 (n/a)</td><td>311.30 (n/a)</td><td>145.21 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 <b>(+21.41%)</b></td><td>0.07 (-15.16%)</td><td>0.06 (-17.82%)</td><td>0.02 <b>(-72.50%)</b></td><td>0.04 <b>(+131.90%)</b></td><td>1926.60 <b>(+263.65%)</b></td><td>757.90 <b>(+71.72%)</b></td><td>515.90 <b>(+21.70%)</b></td><td>265.60 (-17.64%)</td><td>664.31 <b>(+651.43%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>529.80 (n/a)</td><td>441.36 (n/a)</td><td>423.90 (n/a)</td><td>322.50 (n/a)</td><td>88.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (-10.57%)</td><td>0.07 (-15.55%)</td><td>0.06 <b>(-22.11%)</b></td><td>0.05 (-11.50%)</td><td>0.03 (-13.25%)</td><td>686.10 (+12.99%)</td><td>520.74 (+16.76%)</td><td>586.30 <b>(+28.41%)</b></td><td>267.40 (+11.84%)</td><td>164.82 (+1.46%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>607.20 (n/a)</td><td>446.00 (n/a)</td><td>456.60 (n/a)</td><td>239.10 (n/a)</td><td>162.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(-22.44%)</b></td><td>0.07 (-14.40%)</td><td>0.07 (-6.89%)</td><td>0.03 <b>(-48.71%)</b></td><td>0.03 (+4.65%)</td><td>1058.80 <b>(+94.99%)</b></td><td>562.10 <b>(+31.30%)</b></td><td>469.80 (+7.41%)</td><td>316.40 <b>(+28.93%)</b></td><td>307.52 <b>(+150.24%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>543.00 (n/a)</td><td>428.10 (n/a)</td><td>437.40 (n/a)</td><td>245.40 (n/a)</td><td>122.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (-18.02%)</td><td>0.08 (-8.67%)</td><td>0.07 (-5.20%)</td><td>0.06 (+17.14%)</td><td>0.02 <b>(-45.53%)</b></td><td>526.30 (-14.63%)</td><td>435.58 (+2.67%)</td><td>458.00 (+5.48%)</td><td>316.80 <b>(+21.99%)</b></td><td>80.56 <b>(-43.38%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>616.50 (n/a)</td><td>424.26 (n/a)</td><td>434.20 (n/a)</td><td>259.70 (n/a)</td><td>142.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+16.44%)</td><td>0.02 <b>(+24.40%)</b></td><td>0.02 <b>(+28.55%)</b></td><td>0.01 (-7.10%)</td><td>0.00 <b>(+27.09%)</b></td><td>545.90 (+7.63%)</td><td>303.86 (-16.24%)</td><td>244.40 <b>(-22.19%)</b></td><td>196.80 (-14.10%)</td><td>139.63 <b>(+22.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.20 (n/a)</td><td>362.78 (n/a)</td><td>314.10 (n/a)</td><td>229.10 (n/a)</td><td>114.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+9.32%)</td><td>0.02 (+15.79%)</td><td>0.01 (+5.45%)</td><td>0.01 <b>(+24.59%)</b></td><td>0.01 (+3.86%)</td><td>485.00 (-19.73%)</td><td>386.44 (-14.94%)</td><td>445.50 (-5.17%)</td><td>247.40 (-8.51%)</td><td>104.24 <b>(-23.09%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.20 (n/a)</td><td>454.32 (n/a)</td><td>469.80 (n/a)</td><td>270.40 (n/a)</td><td>135.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+4.63%)</td><td>0.01 (+13.96%)</td><td>0.01 <b>(+43.04%)</b></td><td>0.01 <b>(+31.14%)</b></td><td>0.00 (-8.55%)</td><td>455.00 <b>(-23.75%)</b></td><td>339.10 (-15.39%)</td><td>306.30 <b>(-30.08%)</b></td><td>217.50 (-4.44%)</td><td>103.74 <b>(-28.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.70 (n/a)</td><td>400.78 (n/a)</td><td>438.10 (n/a)</td><td>227.60 (n/a)</td><td>144.30 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 <b>(+62.63%)</b></td><td>0.01 (+13.66%)</td><td>0.01 (-4.31%)</td><td>0.01 (-0.12%)</td><td>0.00 <b>(+177.00%)</b></td><td>614.20 (+0.13%)</td><td>477.90 (-5.79%)</td><td>500.10 (+4.51%)</td><td>260.40 <b>(-38.51%)</b></td><td>134.75 <b>(+60.29%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.40 (n/a)</td><td>507.28 (n/a)</td><td>478.50 (n/a)</td><td>423.50 (n/a)</td><td>84.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-9.56%)</td><td>0.01 (-0.07%)</td><td>0.01 <b>(+20.48%)</b></td><td>0.00 (-0.26%)</td><td>0.01 (-11.90%)</td><td>1916.80 (+0.26%)</td><td>693.56 (-2.36%)</td><td>383.40 (-17.00%)</td><td>241.00 (+10.55%)</td><td>694.66 (+0.82%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1911.90 (n/a)</td><td>710.36 (n/a)</td><td>461.90 (n/a)</td><td>218.00 (n/a)</td><td>689.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (+16.42%)</td><td>0.01 (+5.47%)</td><td>0.01 <b>(-22.85%)</b></td><td>0.01 <b>(+113.12%)</b></td><td>0.01 (+6.72%)</td><td>636.80 <b>(-53.08%)</b></td><td>503.92 (-17.53%)</td><td>596.50 <b>(+29.62%)</b></td><td>240.40 (-14.11%)</td><td>167.23 <b>(-60.97%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1357.20 (n/a)</td><td>611.06 (n/a)</td><td>460.20 (n/a)</td><td>279.90 (n/a)</td><td>428.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 <b>(+108.47%)</b></td><td>0.01 <b>(+45.35%)</b></td><td>0.01 <b>(+35.21%)</b></td><td>0.01 <b>(+34.71%)</b></td><td>0.01 <b>(+150.04%)</b></td><td>504.20 <b>(-25.77%)</b></td><td>391.12 <b>(-23.25%)</b></td><td>441.70 <b>(-26.05%)</b></td><td>140.50 <b>(-52.03%)</b></td><td>146.09 (-16.85%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>679.20 (n/a)</td><td>509.58 (n/a)</td><td>597.30 (n/a)</td><td>292.90 (n/a)</td><td>175.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (-10.67%)</td><td>0.01 (-4.41%)</td><td>0.01 <b>(+23.95%)</b></td><td>0.01 (-14.62%)</td><td>0.01 (-9.86%)</td><td>672.50 (+17.12%)</td><td>433.56 (+6.13%)</td><td>355.80 (-19.32%)</td><td>232.30 (+11.95%)</td><td>191.30 <b>(+23.44%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.20 (n/a)</td><td>408.50 (n/a)</td><td>441.00 (n/a)</td><td>207.50 (n/a)</td><td>154.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 <b>(+89.97%)</b></td><td>0.01 <b>(+24.42%)</b></td><td>0.01 (+0.45%)</td><td>0.01 (-2.87%)</td><td>0.01 <b>(+121.08%)</b></td><td>614.70 (+2.95%)</td><td>409.10 (-6.78%)</td><td>447.50 (-0.44%)</td><td>144.90 <b>(-47.37%)</b></td><td>187.49 (+17.76%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.10 (n/a)</td><td>438.86 (n/a)</td><td>449.50 (n/a)</td><td>275.30 (n/a)</td><td>159.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (-13.50%)</td><td>0.01 (+0.03%)</td><td>0.01 (+11.13%)</td><td>0.01 (+8.26%)</td><td>0.00 <b>(-31.51%)</b></td><td>603.40 (-7.62%)</td><td>512.68 (-4.64%)</td><td>535.20 (-10.02%)</td><td>323.20 (+15.59%)</td><td>109.67 <b>(-26.81%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.20 (n/a)</td><td>537.60 (n/a)</td><td>594.80 (n/a)</td><td>279.60 (n/a)</td><td>149.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (-7.61%)</td><td>0.01 (+8.58%)</td><td>0.01 (+0.93%)</td><td>0.01 <b>(+197.36%)</b></td><td>0.00 <b>(-42.75%)</b></td><td>650.20 <b>(-66.37%)</b></td><td>493.42 <b>(-34.06%)</b></td><td>534.00 (-0.93%)</td><td>338.60 (+8.21%)</td><td>121.61 <b>(-81.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1933.30 (n/a)</td><td>748.28 (n/a)</td><td>539.00 (n/a)</td><td>312.90 (n/a)</td><td>669.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+6.16%)</td><td>0.02 (+9.40%)</td><td>0.02 (+19.36%)</td><td>0.01 (+1.25%)</td><td>0.01 (+8.85%)</td><td>610.40 (-1.25%)</td><td>421.98 (-7.99%)</td><td>448.70 (-16.22%)</td><td>235.80 (-5.79%)</td><td>171.88 (-2.94%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.10 (n/a)</td><td>458.64 (n/a)</td><td>535.60 (n/a)</td><td>250.30 (n/a)</td><td>177.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (+10.17%)</td><td>0.04 (+17.62%)</td><td>0.04 <b>(+67.13%)</b></td><td>0.02 (+15.12%)</td><td>0.01 (+3.89%)</td><td>588.70 (-13.13%)</td><td>397.64 (-15.53%)</td><td>303.30 <b>(-40.17%)</b></td><td>248.60 (-9.24%)</td><td>167.05 (-9.09%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>677.70 (n/a)</td><td>470.76 (n/a)</td><td>506.90 (n/a)</td><td>273.90 (n/a)</td><td>183.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-4.98%)</td><td>0.02 (-8.87%)</td><td>0.03 (-13.65%)</td><td>0.01 (-10.12%)</td><td>0.01 (+7.04%)</td><td>594.00 (+11.26%)</td><td>386.38 (+13.49%)</td><td>315.20 (+15.84%)</td><td>242.90 (+5.24%)</td><td>163.84 <b>(+25.54%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.90 (n/a)</td><td>340.46 (n/a)</td><td>272.10 (n/a)</td><td>230.80 (n/a)</td><td>130.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 <b>(+34.89%)</b></td><td>0.03 <b>(+35.42%)</b></td><td>0.02 (+15.86%)</td><td>0.02 (+9.35%)</td><td>0.01 <b>(+66.91%)</b></td><td>511.90 (-8.56%)</td><td>383.54 <b>(-20.88%)</b></td><td>457.30 (-13.68%)</td><td>201.50 <b>(-25.86%)</b></td><td>144.63 (+19.86%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.80 (n/a)</td><td>484.74 (n/a)</td><td>529.80 (n/a)</td><td>271.80 (n/a)</td><td>120.67 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-2.21%)</td><td>0.02 <b>(+23.61%)</b></td><td>0.02 <b>(+29.65%)</b></td><td>0.01 <b>(+136.66%)</b></td><td>0.01 (-14.74%)</td><td>1032.10 <b>(-57.75%)</b></td><td>473.96 <b>(-42.54%)</b></td><td>366.80 <b>(-22.86%)</b></td><td>246.80 (+2.28%)</td><td>317.89 <b>(-65.09%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2442.70 (n/a)</td><td>824.90 (n/a)</td><td>475.50 (n/a)</td><td>241.30 (n/a)</td><td>910.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (+11.18%)</td><td>0.02 (-6.93%)</td><td>0.02 <b>(-25.24%)</b></td><td>0.02 <b>(+79.80%)</b></td><td>0.01 (-8.86%)</td><td>614.10 <b>(-44.38%)</b></td><td>491.90 (-8.61%)</td><td>542.10 <b>(+33.75%)</b></td><td>219.30 (-10.05%)</td><td>162.04 <b>(-54.70%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1104.10 (n/a)</td><td>538.26 (n/a)</td><td>405.30 (n/a)</td><td>243.80 (n/a)</td><td>357.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 <b>(+25.93%)</b></td><td>0.03 <b>(+28.17%)</b></td><td>0.03 <b>(+60.21%)</b></td><td>0.02 (+17.07%)</td><td>0.01 <b>(+28.16%)</b></td><td>446.10 (-14.59%)</td><td>307.40 <b>(-21.09%)</b></td><td>276.40 <b>(-37.58%)</b></td><td>189.70 <b>(-20.59%)</b></td><td>104.90 (-9.92%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.30 (n/a)</td><td>389.58 (n/a)</td><td>442.80 (n/a)</td><td>238.90 (n/a)</td><td>116.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 <b>(-24.00%)</b></td><td>0.02 <b>(-23.18%)</b></td><td>0.02 (-8.58%)</td><td>0.01 <b>(-36.43%)</b></td><td>0.01 <b>(-26.49%)</b></td><td>1089.30 <b>(+57.30%)</b></td><td>571.10 <b>(+30.70%)</b></td><td>534.20 (+9.40%)</td><td>214.20 <b>(+31.57%)</b></td><td>319.43 <b>(+52.61%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>692.50 (n/a)</td><td>436.96 (n/a)</td><td>488.30 (n/a)</td><td>162.80 (n/a)</td><td>209.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (+6.40%)</td><td>0.02 (-12.96%)</td><td>0.02 <b>(-34.05%)</b></td><td>0.01 (+8.00%)</td><td>0.01 (-16.81%)</td><td>565.80 (-7.40%)</td><td>443.04 (+10.27%)</td><td>453.60 <b>(+51.65%)</b></td><td>271.60 (-5.99%)</td><td>111.70 <b>(-27.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.00 (n/a)</td><td>401.76 (n/a)</td><td>299.10 (n/a)</td><td>288.90 (n/a)</td><td>153.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (-0.48%)</td><td>0.02 (-6.69%)</td><td>0.02 (-1.31%)</td><td>0.01 (-19.01%)</td><td>0.00 <b>(+35.63%)</b></td><td>654.60 <b>(+23.49%)</b></td><td>503.64 (+9.90%)</td><td>484.50 (+1.34%)</td><td>363.00 (+0.50%)</td><td>118.34 <b>(+69.89%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>530.10 (n/a)</td><td>458.28 (n/a)</td><td>478.10 (n/a)</td><td>361.20 (n/a)</td><td>69.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 <b>(+42.45%)</b></td><td>0.02 <b>(+57.17%)</b></td><td>0.02 <b>(+40.29%)</b></td><td>0.02 <b>(+151.61%)</b></td><td>0.01 (+4.03%)</td><td>526.40 <b>(-60.25%)</b></td><td>413.34 <b>(-43.52%)</b></td><td>424.40 <b>(-28.73%)</b></td><td>260.50 <b>(-29.78%)</b></td><td>95.88 <b>(-73.59%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1324.40 (n/a)</td><td>731.80 (n/a)</td><td>595.50 (n/a)</td><td>371.00 (n/a)</td><td>363.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (-11.78%)</td><td>0.04 <b>(-27.57%)</b></td><td>0.03 <b>(-32.16%)</b></td><td>0.03 <b>(-33.90%)</b></td><td>0.01 <b>(+21.60%)</b></td><td>613.00 <b>(+51.28%)</b></td><td>479.82 <b>(+42.29%)</b></td><td>489.10 <b>(+47.41%)</b></td><td>304.60 (+13.36%)</td><td>110.99 <b>(+94.88%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>405.20 (n/a)</td><td>337.22 (n/a)</td><td>331.80 (n/a)</td><td>268.70 (n/a)</td><td>56.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (+0.05%)</td><td>0.06 <b>(-20.41%)</b></td><td>0.06 <b>(-36.81%)</b></td><td>0.05 (+12.59%)</td><td>0.02 (-3.87%)</td><td>536.30 (-11.18%)</td><td>419.92 <b>(+22.81%)</b></td><td>431.40 <b>(+58.25%)</b></td><td>243.50 (-0.04%)</td><td>121.29 (-18.57%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>603.80 (n/a)</td><td>341.92 (n/a)</td><td>272.60 (n/a)</td><td>243.60 (n/a)</td><td>148.95 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (+13.00%)</td><td>0.05 <b>(+27.80%)</b></td><td>0.07 <b>(+82.67%)</b></td><td>0.03 (+13.02%)</td><td>0.02 <b>(+37.45%)</b></td><td>495.90 (-11.51%)</td><td>339.20 (-18.86%)</td><td>248.10 <b>(-45.26%)</b></td><td>240.20 (-11.50%)</td><td>132.23 (+8.27%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>560.40 (n/a)</td><td>418.02 (n/a)</td><td>453.20 (n/a)</td><td>271.40 (n/a)</td><td>122.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (+9.67%)</td><td>0.05 (-1.86%)</td><td>0.04 (+6.95%)</td><td>0.04 (+9.93%)</td><td>0.02 (-6.92%)</td><td>571.90 (-9.03%)</td><td>435.32 (-1.30%)</td><td>456.10 (-6.50%)</td><td>249.20 (-8.82%)</td><td>116.46 <b>(-24.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.70 (n/a)</td><td>441.04 (n/a)</td><td>487.80 (n/a)</td><td>273.30 (n/a)</td><td>153.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 <b>(+69.20%)</b></td><td>0.04 <b>(+33.15%)</b></td><td>0.04 (+19.58%)</td><td>0.03 <b>(+45.44%)</b></td><td>0.02 <b>(+72.30%)</b></td><td>541.50 <b>(-31.25%)</b></td><td>427.54 <b>(-24.05%)</b></td><td>425.80 (-16.36%)</td><td>241.00 <b>(-40.90%)</b></td><td>116.62 <b>(-31.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>787.60 (n/a)</td><td>562.92 (n/a)</td><td>509.10 (n/a)</td><td>407.80 (n/a)</td><td>170.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(+27.93%)</b></td><td>0.06 <b>(+28.91%)</b></td><td>0.06 <b>(+31.79%)</b></td><td>0.03 (+13.29%)</td><td>0.03 <b>(+44.66%)</b></td><td>596.50 (-11.73%)</td><td>364.24 (-19.28%)</td><td>339.40 <b>(-24.11%)</b></td><td>211.20 <b>(-21.84%)</b></td><td>155.19 (-0.83%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>675.80 (n/a)</td><td>451.22 (n/a)</td><td>447.20 (n/a)</td><td>270.20 (n/a)</td><td>156.50 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (-6.77%)</td><td>0.05 (+8.10%)</td><td>0.05 <b>(-22.59%)</b></td><td>0.04 <b>(+310.45%)</b></td><td>0.01 <b>(-58.96%)</b></td><td>457.50 <b>(-75.64%)</b></td><td>363.48 <b>(-50.37%)</b></td><td>354.70 <b>(+29.17%)</b></td><td>256.20 (+7.29%)</td><td>87.64 <b>(-87.86%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1877.90 (n/a)</td><td>732.34 (n/a)</td><td>274.60 (n/a)</td><td>238.80 (n/a)</td><td>721.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-16.67%)</td><td>0.05 (-5.25%)</td><td>0.05 <b>(+33.26%)</b></td><td>0.01 <b>(-75.85%)</b></td><td>0.02 (+5.91%)</td><td>2385.20 <b>(+314.17%)</b></td><td>744.52 <b>(+74.25%)</b></td><td>357.60 <b>(-24.97%)</b></td><td>257.60 <b>(+20.04%)</b></td><td>919.08 <b>(+484.56%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>575.90 (n/a)</td><td>427.28 (n/a)</td><td>476.60 (n/a)</td><td>214.60 (n/a)</td><td>157.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-4.99%)</td><td>0.05 <b>(+26.08%)</b></td><td>0.05 <b>(+30.68%)</b></td><td>0.03 <b>(+235.84%)</b></td><td>0.02 <b>(-31.97%)</b></td><td>576.00 <b>(-70.22%)</b></td><td>376.00 <b>(-46.50%)</b></td><td>329.80 <b>(-23.46%)</b></td><td>244.40 (+5.25%)</td><td>131.47 <b>(-81.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1934.50 (n/a)</td><td>702.80 (n/a)</td><td>430.90 (n/a)</td><td>232.20 (n/a)</td><td>695.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-12.20%)</td><td>0.04 <b>(-22.24%)</b></td><td>0.03 <b>(-24.49%)</b></td><td>0.03 (-15.16%)</td><td>0.02 (-13.64%)</td><td>645.60 (+17.87%)</td><td>505.14 <b>(+28.36%)</b></td><td>576.60 <b>(+32.43%)</b></td><td>246.50 (+13.91%)</td><td>166.26 (+15.01%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>547.70 (n/a)</td><td>393.52 (n/a)</td><td>435.40 (n/a)</td><td>216.40 (n/a)</td><td>144.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (+7.95%)</td><td>0.04 (+5.15%)</td><td>0.04 <b>(+20.36%)</b></td><td>0.02 <b>(-30.27%)</b></td><td>0.01 <b>(+67.02%)</b></td><td>678.80 <b>(+43.42%)</b></td><td>421.32 (+1.72%)</td><td>380.20 (-16.91%)</td><td>288.30 (-7.36%)</td><td>158.40 <b>(+116.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.30 (n/a)</td><td>414.20 (n/a)</td><td>457.60 (n/a)</td><td>311.20 (n/a)</td><td>73.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (+5.06%)</td><td>0.09 <b>(+46.70%)</b></td><td>0.11 <b>(+67.97%)</b></td><td>0.02 (+3.82%)</td><td>0.04 (+19.66%)</td><td>1877.70 (-3.68%)</td><td>606.64 <b>(-20.47%)</b></td><td>307.10 <b>(-40.46%)</b></td><td>258.80 (-4.82%)</td><td>710.94 (+5.57%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1949.40 (n/a)</td><td>762.76 (n/a)</td><td>515.80 (n/a)</td><td>271.90 (n/a)</td><td>673.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (-5.03%)</td><td>0.10 (+14.77%)</td><td>0.11 <b>(+60.48%)</b></td><td>0.05 (+16.32%)</td><td>0.04 (-3.70%)</td><td>680.40 (-14.04%)</td><td>395.22 (-14.67%)</td><td>292.40 <b>(-37.69%)</b></td><td>252.20 (+5.26%)</td><td>185.81 (-13.58%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>791.50 (n/a)</td><td>463.14 (n/a)</td><td>469.30 (n/a)</td><td>239.60 (n/a)</td><td>215.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.16 <b>(+43.16%)</b></td><td>0.10 (+15.85%)</td><td>0.08 (-8.26%)</td><td>0.07 (-18.06%)</td><td>0.04 <b>(+243.84%)</b></td><td>617.20 <b>(+22.02%)</b></td><td>447.36 (-3.07%)</td><td>532.10 (+8.99%)</td><td>256.50 <b>(-30.15%)</b></td><td>164.30 <b>(+187.54%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>505.80 (n/a)</td><td>461.54 (n/a)</td><td>488.20 (n/a)</td><td>367.20 (n/a)</td><td>57.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (-10.07%)</td><td>0.09 (+1.45%)</td><td>0.08 <b>(+23.48%)</b></td><td>0.05 (-11.03%)</td><td>0.03 (-19.42%)</td><td>623.30 (+12.41%)</td><td>419.24 (-3.55%)</td><td>387.60 (-19.03%)</td><td>248.20 (+11.20%)</td><td>136.97 (+1.52%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>554.50 (n/a)</td><td>434.68 (n/a)</td><td>478.70 (n/a)</td><td>223.20 (n/a)</td><td>134.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.19 <b>(+113.45%)</b></td><td>0.09 <b>(+51.93%)</b></td><td>0.07 (-7.55%)</td><td>0.07 <b>(+220.07%)</b></td><td>0.05 <b>(+74.51%)</b></td><td>606.90 <b>(-68.76%)</b></td><td>505.94 <b>(-43.49%)</b></td><td>563.70 (+8.18%)</td><td>214.70 <b>(-53.14%)</b></td><td>163.97 <b>(-74.31%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1942.40 (n/a)</td><td>895.34 (n/a)</td><td>521.10 (n/a)</td><td>458.20 (n/a)</td><td>638.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (-1.33%)</td><td>0.11 (+6.86%)</td><td>0.13 (+14.12%)</td><td>0.07 (+2.03%)</td><td>0.03 (+10.56%)</td><td>477.40 (-1.99%)</td><td>335.96 (-5.34%)</td><td>250.60 (-12.35%)</td><td>244.30 (+1.37%)</td><td>122.28 (+2.29%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>487.10 (n/a)</td><td>354.90 (n/a)</td><td>285.90 (n/a)</td><td>241.00 (n/a)</td><td>119.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (-5.56%)</td><td>0.08 (-4.69%)</td><td>0.08 (-0.32%)</td><td>0.07 (-1.98%)</td><td>0.02 (-10.35%)</td><td>563.90 (+2.03%)</td><td>475.52 (+3.97%)</td><td>490.60 (+0.31%)</td><td>299.00 (+5.88%)</td><td>106.86 (-5.68%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>552.70 (n/a)</td><td>457.38 (n/a)</td><td>489.10 (n/a)</td><td>282.40 (n/a)</td><td>113.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (-18.71%)</td><td>0.09 (+4.74%)</td><td>0.09 (+15.32%)</td><td>0.07 <b>(+36.12%)</b></td><td>0.03 <b>(-34.28%)</b></td><td>467.00 <b>(-26.54%)</b></td><td>371.48 (-10.98%)</td><td>383.40 (-13.28%)</td><td>263.60 <b>(+23.01%)</b></td><td>96.13 <b>(-37.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>635.70 (n/a)</td><td>417.28 (n/a)</td><td>442.10 (n/a)</td><td>214.30 (n/a)</td><td>153.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.23 <b>(+111.55%)</b></td><td>0.10 <b>(+31.09%)</b></td><td>0.08 (+10.84%)</td><td>0.02 <b>(-70.76%)</b></td><td>0.08 <b>(+374.00%)</b></td><td>1895.10 <b>(+241.95%)</b></td><td>680.36 <b>(+41.85%)</b></td><td>468.90 (-9.77%)</td><td>161.80 <b>(-52.73%)</b></td><td>699.43 <b>(+714.66%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>554.20 (n/a)</td><td>479.64 (n/a)</td><td>519.70 (n/a)</td><td>342.30 (n/a)</td><td>85.86 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-19.88%)</td><td>0.06 (-14.57%)</td><td>0.06 (-13.17%)</td><td>0.05 (-14.50%)</td><td>0.01 <b>(-34.86%)</b></td><td>699.00 (+16.97%)</td><td>575.98 (+15.75%)</td><td>555.40 (+15.16%)</td><td>483.00 <b>(+24.81%)</b></td><td>86.61 (-7.21%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>597.60 (n/a)</td><td>497.62 (n/a)</td><td>482.30 (n/a)</td><td>387.00 (n/a)</td><td>93.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(+28.16%)</b></td><td>0.06 (+8.42%)</td><td>0.04 (+8.88%)</td><td>0.04 (+10.31%)</td><td>0.02 <b>(+25.40%)</b></td><td>521.90 (-9.36%)</td><td>400.44 (-6.51%)</td><td>459.20 (-8.16%)</td><td>214.80 <b>(-21.95%)</b></td><td>128.79 (-6.76%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>575.80 (n/a)</td><td>428.32 (n/a)</td><td>500.00 (n/a)</td><td>275.20 (n/a)</td><td>138.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (-14.80%)</td><td>0.06 (-12.47%)</td><td>0.07 (-3.29%)</td><td>0.04 (-15.25%)</td><td>0.02 (-14.62%)</td><td>549.40 (+18.00%)</td><td>385.60 (+14.35%)</td><td>308.10 (+3.42%)</td><td>249.90 (+17.38%)</td><td>138.93 (+17.58%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>465.60 (n/a)</td><td>337.22 (n/a)</td><td>297.90 (n/a)</td><td>212.90 (n/a)</td><td>118.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (-8.36%)</td><td>0.06 (-10.24%)</td><td>0.07 (+2.74%)</td><td>0.03 <b>(-27.68%)</b></td><td>0.02 (+4.76%)</td><td>802.30 <b>(+38.26%)</b></td><td>427.28 (+19.81%)</td><td>290.00 (-2.65%)</td><td>243.50 (+9.09%)</td><td>235.26 <b>(+58.36%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>580.30 (n/a)</td><td>356.62 (n/a)</td><td>297.90 (n/a)</td><td>223.20 (n/a)</td><td>148.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-18.60%)</td><td>0.06 (+19.82%)</td><td>0.07 <b>(+37.99%)</b></td><td>0.04 <b>(+108.51%)</b></td><td>0.01 <b>(-46.88%)</b></td><td>521.00 <b>(-52.04%)</b></td><td>359.80 <b>(-31.04%)</b></td><td>312.20 <b>(-27.53%)</b></td><td>290.70 <b>(+22.87%)</b></td><td>95.58 <b>(-70.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1086.30 (n/a)</td><td>521.74 (n/a)</td><td>430.80 (n/a)</td><td>236.60 (n/a)</td><td>326.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(+25.21%)</b></td><td>0.07 (+3.18%)</td><td>0.06 (-9.22%)</td><td>0.04 (+14.25%)</td><td>0.03 <b>(+48.43%)</b></td><td>509.60 (-12.47%)</td><td>350.58 (+0.58%)</td><td>349.50 (+10.15%)</td><td>196.10 <b>(-20.12%)</b></td><td>131.47 (-2.06%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.20 (n/a)</td><td>348.56 (n/a)</td><td>317.30 (n/a)</td><td>245.50 (n/a)</td><td>134.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(+20.87%)</b></td><td>0.06 (-5.18%)</td><td>0.04 <b>(-35.53%)</b></td><td>0.03 (-0.41%)</td><td>0.03 <b>(+45.67%)</b></td><td>586.50 (+0.41%)</td><td>422.66 (+13.09%)</td><td>508.30 <b>(+55.11%)</b></td><td>203.30 (-17.29%)</td><td>167.50 <b>(+21.98%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>584.10 (n/a)</td><td>373.74 (n/a)</td><td>327.70 (n/a)</td><td>245.80 (n/a)</td><td>137.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(+33.70%)</b></td><td>0.09 <b>(+64.16%)</b></td><td>0.09 <b>(+91.00%)</b></td><td>0.06 <b>(+46.92%)</b></td><td>0.02 <b>(+21.87%)</b></td><td>381.00 <b>(-31.94%)</b></td><td>291.62 <b>(-39.54%)</b></td><td>263.70 <b>(-47.65%)</b></td><td>246.30 <b>(-25.20%)</b></td><td>57.19 <b>(-35.62%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>559.80 (n/a)</td><td>482.30 (n/a)</td><td>503.70 (n/a)</td><td>329.30 (n/a)</td><td>88.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(+25.36%)</b></td><td>0.07 (+10.74%)</td><td>0.08 <b>(+43.86%)</b></td><td>0.02 <b>(-53.36%)</b></td><td>0.03 <b>(+120.68%)</b></td><td>1064.50 <b>(+114.40%)</b></td><td>478.14 (+16.34%)</td><td>306.70 <b>(-30.49%)</b></td><td>244.00 <b>(-20.24%)</b></td><td>345.11 <b>(+275.85%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>496.50 (n/a)</td><td>410.98 (n/a)</td><td>441.20 (n/a)</td><td>305.90 (n/a)</td><td>91.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (-18.58%)</td><td>0.07 <b>(-23.11%)</b></td><td>0.08 (-13.85%)</td><td>0.04 <b>(-38.72%)</b></td><td>0.02 <b>(+39.80%)</b></td><td>563.00 <b>(+63.19%)</b></td><td>372.60 <b>(+36.16%)</b></td><td>303.30 (+16.07%)</td><td>292.10 <b>(+22.83%)</b></td><td>115.56 <b>(+171.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>345.00 (n/a)</td><td>273.64 (n/a)</td><td>261.30 (n/a)</td><td>237.80 (n/a)</td><td>42.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 <b>(-30.79%)</b></td><td>0.05 <b>(-31.49%)</b></td><td>0.05 <b>(-39.73%)</b></td><td>0.05 (+14.81%)</td><td>0.01 <b>(-66.39%)</b></td><td>521.90 (-12.90%)</td><td>457.14 <b>(+34.09%)</b></td><td>458.60 <b>(+65.92%)</b></td><td>369.60 <b>(+44.49%)</b></td><td>57.28 <b>(-60.52%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>599.20 (n/a)</td><td>340.92 (n/a)</td><td>276.40 (n/a)</td><td>255.80 (n/a)</td><td>145.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (-1.76%)</td><td>0.07 (+8.21%)</td><td>0.06 (-12.30%)</td><td>0.04 (+1.66%)</td><td>0.02 (+7.37%)</td><td>570.40 (-1.64%)</td><td>389.98 (-7.53%)</td><td>422.60 (+14.00%)</td><td>253.70 (+1.81%)</td><td>135.51 (-7.09%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>579.90 (n/a)</td><td>421.74 (n/a)</td><td>370.70 (n/a)</td><td>249.20 (n/a)</td><td>145.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (+19.75%)</td><td>0.07 <b>(+20.60%)</b></td><td>0.07 <b>(+30.53%)</b></td><td>0.04 (-10.81%)</td><td>0.03 <b>(+76.82%)</b></td><td>609.30 (+12.13%)</td><td>421.82 (-9.26%)</td><td>370.30 <b>(-23.38%)</b></td><td>252.20 (-16.49%)</td><td>172.21 <b>(+78.85%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>543.40 (n/a)</td><td>464.86 (n/a)</td><td>483.30 (n/a)</td><td>302.00 (n/a)</td><td>96.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 <b>(-26.76%)</b></td><td>0.04 <b>(-27.70%)</b></td><td>0.03 <b>(-25.68%)</b></td><td>0.03 (-14.00%)</td><td>0.01 <b>(-45.21%)</b></td><td>544.50 (+16.27%)</td><td>495.86 <b>(+35.56%)</b></td><td>526.90 <b>(+34.55%)</b></td><td>374.70 <b>(+36.55%)</b></td><td>70.55 (-11.81%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>468.30 (n/a)</td><td>365.78 (n/a)</td><td>391.60 (n/a)</td><td>274.40 (n/a)</td><td>80.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(+37.01%)</b></td><td>0.06 (+16.28%)</td><td>0.06 (+0.83%)</td><td>0.03 (+9.51%)</td><td>0.02 <b>(+51.03%)</b></td><td>586.20 (-8.69%)</td><td>336.12 (-10.35%)</td><td>298.70 (-0.83%)</td><td>190.20 <b>(-27.04%)</b></td><td>153.61 (-1.07%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.00 (n/a)</td><td>374.94 (n/a)</td><td>301.20 (n/a)</td><td>260.70 (n/a)</td><td>155.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-10.08%)</td><td>0.06 <b>(+43.80%)</b></td><td>0.06 <b>(+68.32%)</b></td><td>0.03 <b>(+250.50%)</b></td><td>0.02 <b>(-41.93%)</b></td><td>533.10 <b>(-71.47%)</b></td><td>358.56 <b>(-52.41%)</b></td><td>302.00 <b>(-40.59%)</b></td><td>253.20 (+11.20%)</td><td>113.36 <b>(-82.37%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1868.70 (n/a)</td><td>753.40 (n/a)</td><td>508.30 (n/a)</td><td>227.70 (n/a)</td><td>642.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (+3.03%)</td><td>0.06 <b>(+34.16%)</b></td><td>0.07 <b>(+117.08%)</b></td><td>0.04 <b>(+36.54%)</b></td><td>0.02 (-9.38%)</td><td>477.80 <b>(-26.75%)</b></td><td>325.00 <b>(-30.06%)</b></td><td>253.50 <b>(-53.93%)</b></td><td>234.40 (-2.98%)</td><td>116.58 <b>(-36.80%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>652.30 (n/a)</td><td>464.66 (n/a)</td><td>550.20 (n/a)</td><td>241.60 (n/a)</td><td>184.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (-12.35%)</td><td>0.06 (+6.98%)</td><td>0.07 (+6.74%)</td><td>0.03 <b>(+199.92%)</b></td><td>0.02 <b>(-29.68%)</b></td><td>616.30 <b>(-66.66%)</b></td><td>384.54 <b>(-41.22%)</b></td><td>270.40 (-6.31%)</td><td>235.10 (+14.07%)</td><td>186.48 <b>(-73.17%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1848.40 (n/a)</td><td>654.18 (n/a)</td><td>288.60 (n/a)</td><td>206.10 (n/a)</td><td>695.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (-18.71%)</td><td>0.06 (-9.17%)</td><td>0.06 (+6.70%)</td><td>0.04 (-0.08%)</td><td>0.01 <b>(-40.10%)</b></td><td>495.10 (+0.08%)</td><td>348.82 (+4.29%)</td><td>298.60 (-6.28%)</td><td>271.30 <b>(+22.98%)</b></td><td>93.80 <b>(-22.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>494.70 (n/a)</td><td>334.46 (n/a)</td><td>318.60 (n/a)</td><td>220.60 (n/a)</td><td>120.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.39 (+14.41%)</td><td>0.21 (-18.68%)</td><td>0.20 <b>(-21.30%)</b></td><td>0.04 <b>(-76.86%)</b></td><td>0.13 <b>(+83.37%)</b></td><td>2528.00 <b>(+332.21%)</b></td><td>845.58 <b>(+110.90%)</b></td><td>490.70 <b>(+27.06%)</b></td><td>255.00 (-12.61%)</td><td>949.24 <b>(+697.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>584.90 (n/a)</td><td>400.94 (n/a)</td><td>386.20 (n/a)</td><td>291.80 (n/a)</td><td>119.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.26 <b>(-44.26%)</b></td><td>0.21 <b>(-48.60%)</b></td><td>0.20 <b>(-49.13%)</b></td><td>0.18 <b>(-52.71%)</b></td><td>0.03 (-12.35%)</td><td>559.40 <b>(+111.49%)</b></td><td>480.32 <b>(+96.58%)</b></td><td>490.00 <b>(+96.55%)</b></td><td>381.20 <b>(+79.39%)</b></td><td>64.75 <b>(+230.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.46 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.03 (n/a)</td><td>264.50 (n/a)</td><td>244.34 (n/a)</td><td>249.30 (n/a)</td><td>212.50 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.21 <b>(-43.09%)</b></td><td>0.20 <b>(-20.42%)</b></td><td>0.20 <b>(-22.41%)</b></td><td>0.18 (+13.40%)</td><td>0.01 <b>(-84.27%)</b></td><td>556.60 (-11.82%)</td><td>503.90 (+15.63%)</td><td>497.10 <b>(+28.88%)</b></td><td>464.70 <b>(+75.69%)</b></td><td>34.38 <b>(-75.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>631.20 (n/a)</td><td>435.78 (n/a)</td><td>385.70 (n/a)</td><td>264.50 (n/a)</td><td>140.71 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.28 (-2.71%)</td><td>0.19 (-5.85%)</td><td>0.22 (-8.53%)</td><td>0.04 <b>(-65.93%)</b></td><td>0.09 (+17.91%)</td><td>1920.50 <b>(+193.47%)</b></td><td>656.00 <b>(+52.57%)</b></td><td>342.20 (+9.33%)</td><td>263.80 (+2.77%)</td><td>709.85 <b>(+273.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>654.40 (n/a)</td><td>429.96 (n/a)</td><td>313.00 (n/a)</td><td>256.70 (n/a)</td><td>190.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.32 (-5.86%)</td><td>0.24 <b>(+28.50%)</b></td><td>0.25 <b>(+58.53%)</b></td><td>0.13 <b>(+41.14%)</b></td><td>0.07 <b>(-27.16%)</b></td><td>571.90 <b>(-29.15%)</b></td><td>340.26 <b>(-29.06%)</b></td><td>298.30 <b>(-36.91%)</b></td><td>233.00 (+6.20%)</td><td>132.91 <b>(-39.18%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>807.20 (n/a)</td><td>479.64 (n/a)</td><td>472.80 (n/a)</td><td>219.40 (n/a)</td><td>218.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.37 <b>(+23.96%)</b></td><td>0.25 <b>(+45.68%)</b></td><td>0.26 <b>(+57.32%)</b></td><td>0.14 <b>(+91.44%)</b></td><td>0.10 (+17.33%)</td><td>543.30 <b>(-47.76%)</b></td><td>343.92 <b>(-36.12%)</b></td><td>280.80 <b>(-36.44%)</b></td><td>201.30 (-19.32%)</td><td>145.59 <b>(-51.22%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.30 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>1040.00 (n/a)</td><td>538.36 (n/a)</td><td>441.80 (n/a)</td><td>249.50 (n/a)</td><td>298.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.16 (+1.29%)</td><td>0.12 <b>(+24.44%)</b></td><td>0.12 <b>(+73.51%)</b></td><td>0.07 (+13.30%)</td><td>0.03 <b>(-20.90%)</b></td><td>565.60 (-11.74%)</td><td>345.42 <b>(-24.45%)</b></td><td>306.40 <b>(-42.35%)</b></td><td>228.50 (-1.25%)</td><td>128.81 <b>(-26.58%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>640.80 (n/a)</td><td>457.22 (n/a)</td><td>531.50 (n/a)</td><td>231.40 (n/a)</td><td>175.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (-11.23%)</td><td>0.10 (-6.34%)</td><td>0.09 <b>(-27.80%)</b></td><td>0.07 (+13.16%)</td><td>0.03 <b>(-25.02%)</b></td><td>541.90 (-11.63%)</td><td>408.02 (+0.14%)</td><td>410.60 <b>(+38.48%)</b></td><td>285.50 (+12.67%)</td><td>120.29 <b>(-30.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>613.20 (n/a)</td><td>407.46 (n/a)</td><td>296.50 (n/a)</td><td>253.40 (n/a)</td><td>174.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (-2.41%)</td><td>0.11 (+4.22%)</td><td>0.12 (-3.37%)</td><td>0.08 <b>(+30.44%)</b></td><td>0.03 (-12.76%)</td><td>484.10 <b>(-23.34%)</b></td><td>349.38 (-8.28%)</td><td>305.90 (+3.48%)</td><td>245.20 (+2.47%)</td><td>108.66 <b>(-31.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>631.50 (n/a)</td><td>380.90 (n/a)</td><td>295.60 (n/a)</td><td>239.30 (n/a)</td><td>159.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (+6.08%)</td><td>0.09 (+10.96%)</td><td>0.10 <b>(+21.54%)</b></td><td>0.06 <b>(+198.21%)</b></td><td>0.03 <b>(-20.11%)</b></td><td>641.70 <b>(-66.46%)</b></td><td>444.78 <b>(-35.70%)</b></td><td>378.30 (-17.71%)</td><td>284.40 (-5.73%)</td><td>172.58 <b>(-74.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1913.50 (n/a)</td><td>691.74 (n/a)</td><td>459.70 (n/a)</td><td>301.70 (n/a)</td><td>688.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (-3.36%)</td><td>0.08 <b>(-21.41%)</b></td><td>0.08 <b>(-22.29%)</b></td><td>0.02 <b>(-77.36%)</b></td><td>0.04 <b>(+77.71%)</b></td><td>2447.70 <b>(+341.66%)</b></td><td>834.46 <b>(+111.63%)</b></td><td>485.70 <b>(+28.70%)</b></td><td>301.40 (+3.50%)</td><td>910.94 <b>(+756.90%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>554.20 (n/a)</td><td>394.30 (n/a)</td><td>377.40 (n/a)</td><td>291.20 (n/a)</td><td>106.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(-24.79%)</b></td><td>0.08 (-8.51%)</td><td>0.08 (-2.55%)</td><td>0.06 (+6.14%)</td><td>0.02 <b>(-45.68%)</b></td><td>625.20 (-5.79%)</td><td>478.34 (+3.81%)</td><td>481.00 (+2.62%)</td><td>351.50 <b>(+32.94%)</b></td><td>100.62 <b>(-29.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>663.60 (n/a)</td><td>460.78 (n/a)</td><td>468.70 (n/a)</td><td>264.40 (n/a)</td><td>141.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (+5.51%)</td><td>0.11 (-11.48%)</td><td>0.09 <b>(-43.25%)</b></td><td>0.07 (-0.91%)</td><td>0.05 (+13.57%)</td><td>551.20 (+0.92%)</td><td>413.24 (+15.88%)</td><td>478.10 <b>(+76.23%)</b></td><td>239.20 (-5.23%)</td><td>149.37 (+11.49%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>546.20 (n/a)</td><td>356.62 (n/a)</td><td>271.30 (n/a)</td><td>252.40 (n/a)</td><td>133.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (-3.89%)</td><td>0.12 (+5.85%)</td><td>0.13 (-1.84%)</td><td>0.07 (+16.67%)</td><td>0.03 <b>(-39.15%)</b></td><td>563.70 (-14.29%)</td><td>357.48 (-15.63%)</td><td>318.40 (+1.86%)</td><td>266.10 (+4.03%)</td><td>117.56 <b>(-42.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>657.70 (n/a)</td><td>423.70 (n/a)</td><td>312.60 (n/a)</td><td>255.80 (n/a)</td><td>205.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (-10.20%)</td><td>0.09 (-9.89%)</td><td>0.08 (-7.99%)</td><td>0.02 <b>(-46.43%)</b></td><td>0.05 (+6.82%)</td><td>2033.40 <b>(+86.69%)</b></td><td>737.40 <b>(+41.50%)</b></td><td>511.00 (+8.70%)</td><td>290.60 (+11.34%)</td><td>734.35 <b>(+120.76%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1089.20 (n/a)</td><td>521.12 (n/a)</td><td>470.10 (n/a)</td><td>261.00 (n/a)</td><td>332.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 <b>(+28.80%)</b></td><td>0.10 (-11.25%)</td><td>0.08 <b>(-33.94%)</b></td><td>0.07 (-10.68%)</td><td>0.05 <b>(+54.51%)</b></td><td>605.00 (+11.95%)</td><td>473.78 (+19.33%)</td><td>500.00 <b>(+51.38%)</b></td><td>232.20 <b>(-22.37%)</b></td><td>150.35 <b>(+29.55%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>540.40 (n/a)</td><td>397.04 (n/a)</td><td>330.30 (n/a)</td><td>299.10 (n/a)</td><td>116.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (+10.81%)</td><td>0.11 (-5.52%)</td><td>0.10 (+4.96%)</td><td>0.07 <b>(-27.57%)</b></td><td>0.04 <b>(+54.40%)</b></td><td>609.90 <b>(+38.08%)</b></td><td>430.24 (+15.55%)</td><td>408.90 (-4.73%)</td><td>240.90 (-9.78%)</td><td>168.98 <b>(+98.67%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>441.70 (n/a)</td><td>372.34 (n/a)</td><td>429.20 (n/a)</td><td>267.00 (n/a)</td><td>85.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (-11.57%)</td><td>0.11 (-15.94%)</td><td>0.10 <b>(-29.77%)</b></td><td>0.08 (-1.56%)</td><td>0.03 <b>(-32.91%)</b></td><td>538.30 (+1.59%)</td><td>404.70 (+12.84%)</td><td>408.70 <b>(+42.35%)</b></td><td>273.90 (+13.09%)</td><td>104.60 <b>(-23.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>529.90 (n/a)</td><td>358.64 (n/a)</td><td>287.10 (n/a)</td><td>242.20 (n/a)</td><td>137.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (+7.40%)</td><td>0.11 <b>(+31.03%)</b></td><td>0.11 <b>(+63.61%)</b></td><td>0.08 <b>(+58.93%)</b></td><td>0.02 <b>(-35.60%)</b></td><td>444.60 <b>(-37.09%)</b></td><td>329.46 <b>(-32.05%)</b></td><td>305.80 <b>(-38.88%)</b></td><td>256.50 (-6.90%)</td><td>78.68 <b>(-61.09%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>706.70 (n/a)</td><td>484.88 (n/a)</td><td>500.30 (n/a)</td><td>275.50 (n/a)</td><td>202.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 <b>(+57.54%)</b></td><td>0.13 <b>(+40.63%)</b></td><td>0.12 <b>(+38.43%)</b></td><td>0.08 <b>(+33.37%)</b></td><td>0.04 <b>(+48.04%)</b></td><td>432.00 <b>(-25.03%)</b></td><td>297.34 <b>(-28.65%)</b></td><td>289.10 <b>(-27.76%)</b></td><td>193.50 <b>(-36.54%)</b></td><td>87.04 <b>(-26.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>576.20 (n/a)</td><td>416.76 (n/a)</td><td>400.20 (n/a)</td><td>304.90 (n/a)</td><td>118.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 <b>(-46.38%)</b></td><td>0.06 <b>(-44.52%)</b></td><td>0.07 <b>(-39.64%)</b></td><td>0.02 (-2.88%)</td><td>0.03 <b>(-49.58%)</b></td><td>1955.80 (+2.96%)</td><td>805.88 <b>(+34.56%)</b></td><td>483.00 <b>(+65.69%)</b></td><td>443.40 <b>(+86.46%)</b></td><td>651.27 (-10.50%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1899.50 (n/a)</td><td>598.90 (n/a)</td><td>291.50 (n/a)</td><td>237.80 (n/a)</td><td>727.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (-11.66%)</td><td>0.09 (-16.00%)</td><td>0.09 <b>(-24.53%)</b></td><td>0.06 <b>(-25.43%)</b></td><td>0.03 (-0.08%)</td><td>597.30 <b>(+34.10%)</b></td><td>420.44 <b>(+21.57%)</b></td><td>408.50 <b>(+32.50%)</b></td><td>287.10 (+13.21%)</td><td>129.84 <b>(+41.35%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>445.40 (n/a)</td><td>345.84 (n/a)</td><td>308.30 (n/a)</td><td>253.60 (n/a)</td><td>91.86 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (-2.78%)</td><td>0.07 (-11.06%)</td><td>0.07 (-5.85%)</td><td>0.02 <b>(-65.18%)</b></td><td>0.04 <b>(+27.30%)</b></td><td>1862.70 <b>(+187.19%)</b></td><td>734.68 <b>(+53.35%)</b></td><td>510.30 (+6.22%)</td><td>268.20 (+2.88%)</td><td>645.26 <b>(+310.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>648.60 (n/a)</td><td>479.08 (n/a)</td><td>480.40 (n/a)</td><td>260.70 (n/a)</td><td>157.36 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 <b>(-20.32%)</b></td><td>0.07 (+0.64%)</td><td>0.06 (+12.63%)</td><td>0.06 (+14.13%)</td><td>0.02 <b>(-40.71%)</b></td><td>598.70 (-12.38%)</td><td>488.54 (-7.39%)</td><td>542.50 (-11.21%)</td><td>337.30 <b>(+25.53%)</b></td><td>113.49 <b>(-34.27%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>683.30 (n/a)</td><td>527.54 (n/a)</td><td>611.00 (n/a)</td><td>268.70 (n/a)</td><td>172.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.40 (-10.84%)</td><td>0.33 (+18.42%)</td><td>0.40 <b>(+86.79%)</b></td><td>0.21 <b>(+69.51%)</b></td><td>0.10 <b>(-30.31%)</b></td><td>628.70 <b>(-41.01%)</b></td><td>436.36 <b>(-26.64%)</b></td><td>329.80 <b>(-46.46%)</b></td><td>325.70 (+12.19%)</td><td>149.87 <b>(-52.23%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1065.70 (n/a)</td><td>594.80 (n/a)</td><td>616.00 (n/a)</td><td>290.30 (n/a)</td><td>313.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.44 (-7.20%)</td><td>0.35 (+9.48%)</td><td>0.38 <b>(+41.58%)</b></td><td>0.26 <b>(+31.04%)</b></td><td>0.08 <b>(-30.61%)</b></td><td>513.80 <b>(-23.69%)</b></td><td>387.98 (-13.92%)</td><td>340.90 <b>(-29.36%)</b></td><td>299.30 (+7.78%)</td><td>96.20 <b>(-40.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>673.30 (n/a)</td><td>450.72 (n/a)</td><td>482.60 (n/a)</td><td>277.70 (n/a)</td><td>160.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.42 (-8.53%)</td><td>0.35 (-1.26%)</td><td>0.42 (+5.18%)</td><td>0.22 (+3.62%)</td><td>0.10 (+0.34%)</td><td>606.70 (-3.50%)</td><td>412.20 (+1.43%)</td><td>311.30 (-4.92%)</td><td>309.00 (+9.34%)</td><td>142.91 (-0.03%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.40 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>628.70 (n/a)</td><td>406.38 (n/a)</td><td>327.40 (n/a)</td><td>282.60 (n/a)</td><td>142.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>20132.05 (-2.34%)</td><td>14370.03 (-2.36%)</td><td>18314.19 (+1.70%)</td><td>7160.57 (-2.79%)</td><td>6424.79 (+0.55%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20613.39 (n/a)</td><td>14717.90 (n/a)</td><td>18007.75 (n/a)</td><td>7365.93 (n/a)</td><td>6389.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.00 (-7.69%)</td><td>0.00 (+2.63%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.14%)</b></td><td>20477.80 (-3.12%)</td><td>12690.65 (-10.99%)</td><td>14092.58 <b>(-23.15%)</b></td><td>6811.57 (+10.38%)</td><td>5593.36 <b>(-23.89%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21137.62 (n/a)</td><td>14257.78 (n/a)</td><td>18336.91 (n/a)</td><td>6171.25 (n/a)</td><td>7349.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (+12.17%)</td><td>0.10 (+9.25%)</td><td>0.08 (+1.48%)</td><td>0.08 (+6.36%)</td><td>0.03 <b>(+22.68%)</b></td><td>27884.22 (-5.97%)</td><td>22721.62 (-6.94%)</td><td>25473.99 (-1.43%)</td><td>13546.16 (-10.87%)</td><td>5983.28 (+7.39%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29656.10 (n/a)</td><td>24416.13 (n/a)</td><td>25843.62 (n/a)</td><td>15197.67 (n/a)</td><td>5571.50 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>1.74 <b>(-33.47%)</b></td><td>1.36 (-16.08%)</td><td>1.52 <b>(-35.67%)</b></td><td>0.41 <b>(+37.55%)</b></td><td>0.54 <b>(-55.40%)</b></td><td>2529.20 <b>(-27.30%)</b></td><td>1034.18 <b>(-36.35%)</b></td><td>689.10 <b>(+55.45%)</b></td><td>602.40 <b>(+50.30%)</b></td><td>836.60 <b>(-49.23%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.62 (n/a)</td><td>1.62 (n/a)</td><td>2.37 (n/a)</td><td>0.30 (n/a)</td><td>1.20 (n/a)</td><td>3479.00 (n/a)</td><td>1624.68 (n/a)</td><td>443.30 (n/a)</td><td>400.80 (n/a)</td><td>1647.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.46 <b>(-28.28%)</b></td><td>1.84 (-4.29%)</td><td>1.72 <b>(-28.79%)</b></td><td>0.98 <b>(+220.97%)</b></td><td>0.60 <b>(-57.28%)</b></td><td>1070.00 <b>(-68.84%)</b></td><td>634.90 <b>(-50.70%)</b></td><td>608.80 <b>(+40.44%)</b></td><td>426.40 <b>(+39.44%)</b></td><td>260.54 <b>(-81.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.43 (n/a)</td><td>1.92 (n/a)</td><td>2.42 (n/a)</td><td>0.31 (n/a)</td><td>1.42 (n/a)</td><td>3434.40 (n/a)</td><td>1287.82 (n/a)</td><td>433.50 (n/a)</td><td>305.80 (n/a)</td><td>1373.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.60 (-5.53%)</td><td>2.18 <b>(+73.05%)</b></td><td>2.42 <b>(+87.19%)</b></td><td>1.60 <b>(+441.19%)</b></td><td>0.48 <b>(-52.58%)</b></td><td>653.90 <b>(-81.52%)</b></td><td>501.82 <b>(-70.70%)</b></td><td>434.00 <b>(-46.58%)</b></td><td>402.90 (+5.86%)</td><td>120.88 <b>(-92.05%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.75 (n/a)</td><td>1.26 (n/a)</td><td>1.29 (n/a)</td><td>0.30 (n/a)</td><td>1.02 (n/a)</td><td>3538.60 (n/a)</td><td>1712.76 (n/a)</td><td>812.40 (n/a)</td><td>380.60 (n/a)</td><td>1521.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.75 (-0.55%)</td><td>2.46 (+14.90%)</td><td>2.95 <b>(+42.21%)</b></td><td>0.56 <b>(-44.34%)</b></td><td>1.23 (+15.67%)</td><td>1869.60 <b>(+79.67%)</b></td><td>674.32 (+12.92%)</td><td>355.90 <b>(-29.68%)</b></td><td>279.40 (+0.54%)</td><td>674.06 <b>(+127.93%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.77 (n/a)</td><td>2.14 (n/a)</td><td>2.07 (n/a)</td><td>1.01 (n/a)</td><td>1.06 (n/a)</td><td>1040.60 (n/a)</td><td>597.14 (n/a)</td><td>506.10 (n/a)</td><td>277.90 (n/a)</td><td>295.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.87 (+0.44%)</td><td>2.96 <b>(+22.82%)</b></td><td>3.32 <b>(+40.37%)</b></td><td>0.58 <b>(-46.10%)</b></td><td>1.35 <b>(+37.60%)</b></td><td>3605.70 <b>(+85.54%)</b></td><td>1194.90 (+16.31%)</td><td>630.70 <b>(-28.77%)</b></td><td>541.60 (-0.44%)</td><td>1348.28 <b>(+153.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.86 (n/a)</td><td>2.41 (n/a)</td><td>2.37 (n/a)</td><td>1.08 (n/a)</td><td>0.98 (n/a)</td><td>1943.40 (n/a)</td><td>1027.36 (n/a)</td><td>885.40 (n/a)</td><td>544.00 (n/a)</td><td>532.90 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>5.86 (+7.16%)</td><td>4.09 <b>(+27.54%)</b></td><td>4.11 <b>(+57.63%)</b></td><td>2.63 (+16.82%)</td><td>1.40 (+6.78%)</td><td>795.90 (-14.40%)</td><td>565.80 <b>(-21.65%)</b></td><td>510.80 <b>(-36.57%)</b></td><td>357.60 (-6.68%)</td><td>197.36 (-7.64%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.47 (n/a)</td><td>3.21 (n/a)</td><td>2.60 (n/a)</td><td>2.26 (n/a)</td><td>1.31 (n/a)</td><td>929.80 (n/a)</td><td>722.16 (n/a)</td><td>805.30 (n/a)</td><td>383.20 (n/a)</td><td>213.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>5.54 (+3.67%)</td><td>4.08 <b>(+26.83%)</b></td><td>3.85 (+17.24%)</td><td>2.85 <b>(+374.11%)</b></td><td>1.01 <b>(-51.39%)</b></td><td>736.50 <b>(-78.91%)</b></td><td>539.86 <b>(-56.08%)</b></td><td>545.30 (-14.70%)</td><td>378.70 (-3.54%)</td><td>133.81 <b>(-89.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.34 (n/a)</td><td>3.22 (n/a)</td><td>3.28 (n/a)</td><td>0.60 (n/a)</td><td>2.08 (n/a)</td><td>3491.90 (n/a)</td><td>1229.28 (n/a)</td><td>639.30 (n/a)</td><td>392.60 (n/a)</td><td>1307.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>5.44 <b>(+25.81%)</b></td><td>3.16 (-12.40%)</td><td>3.01 <b>(-26.48%)</b></td><td>0.59 <b>(-76.89%)</b></td><td>1.84 <b>(+113.66%)</b></td><td>3541.20 <b>(+332.65%)</b></td><td>1191.52 <b>(+94.98%)</b></td><td>697.80 <b>(+36.02%)</b></td><td>385.30 <b>(-20.51%)</b></td><td>1325.73 <b>(+724.68%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>4.33 (n/a)</td><td>3.61 (n/a)</td><td>4.09 (n/a)</td><td>2.56 (n/a)</td><td>0.86 (n/a)</td><td>818.50 (n/a)</td><td>611.10 (n/a)</td><td>513.00 (n/a)</td><td>484.70 (n/a)</td><td>160.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.44 <b>(+28.19%)</b></td><td>3.27 (+14.10%)</td><td>2.89 (+0.45%)</td><td>0.60 (-0.73%)</td><td>2.20 <b>(+40.44%)</b></td><td>3500.30 (+0.74%)</td><td>1201.66 (-1.01%)</td><td>726.70 (-0.45%)</td><td>325.90 <b>(-21.98%)</b></td><td>1307.07 (+2.81%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.02 (n/a)</td><td>2.86 (n/a)</td><td>2.87 (n/a)</td><td>0.60 (n/a)</td><td>1.57 (n/a)</td><td>3474.70 (n/a)</td><td>1213.90 (n/a)</td><td>730.00 (n/a)</td><td>417.70 (n/a)</td><td>1271.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.98 <b>(-22.22%)</b></td><td>3.00 <b>(-27.88%)</b></td><td>3.24 (-13.52%)</td><td>0.58 <b>(-81.14%)</b></td><td>1.75 <b>(+35.16%)</b></td><td>3611.90 <b>(+430.30%)</b></td><td>1245.14 <b>(+132.48%)</b></td><td>646.40 (+15.64%)</td><td>421.40 <b>(+28.59%)</b></td><td>1344.86 <b>(+934.14%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>6.40 (n/a)</td><td>4.16 (n/a)</td><td>3.75 (n/a)</td><td>3.08 (n/a)</td><td>1.30 (n/a)</td><td>681.10 (n/a)</td><td>535.60 (n/a)</td><td>559.00 (n/a)</td><td>327.70 (n/a)</td><td>130.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.63 (-17.26%)</td><td>3.59 (-3.70%)</td><td>4.02 (-4.33%)</td><td>1.34 (+17.85%)</td><td>1.35 (-18.34%)</td><td>3129.60 (-15.15%)</td><td>1447.18 (-5.43%)</td><td>1044.60 (+4.52%)</td><td>906.60 <b>(+20.86%)</b></td><td>949.33 <b>(-22.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>5.59 (n/a)</td><td>3.72 (n/a)</td><td>4.20 (n/a)</td><td>1.14 (n/a)</td><td>1.65 (n/a)</td><td>3688.30 (n/a)</td><td>1530.32 (n/a)</td><td>999.40 (n/a)</td><td>750.10 (n/a)</td><td>1218.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>8.24 (-0.42%)</td><td>3.34 <b>(-39.51%)</b></td><td>1.73 <b>(-69.55%)</b></td><td>1.24 <b>(-41.27%)</b></td><td>2.91 (+13.56%)</td><td>3384.20 <b>(+70.26%)</b></td><td>1982.88 <b>(+103.93%)</b></td><td>2422.20 <b>(+228.43%)</b></td><td>509.20 (+0.41%)</td><td>1157.21 <b>(+89.48%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>8.27 (n/a)</td><td>5.52 (n/a)</td><td>5.69 (n/a)</td><td>2.11 (n/a)</td><td>2.56 (n/a)</td><td>1987.70 (n/a)</td><td>972.34 (n/a)</td><td>737.50 (n/a)</td><td>507.10 (n/a)</td><td>610.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>7.85 (-8.10%)</td><td>5.03 (-4.11%)</td><td>4.49 <b>(-24.30%)</b></td><td>1.73 <b>(+54.48%)</b></td><td>2.44 <b>(-30.35%)</b></td><td>2423.40 <b>(-35.27%)</b></td><td>1103.58 <b>(-25.76%)</b></td><td>934.80 <b>(+32.09%)</b></td><td>534.50 (+8.82%)</td><td>766.92 <b>(-45.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>8.54 (n/a)</td><td>5.24 (n/a)</td><td>5.93 (n/a)</td><td>1.12 (n/a)</td><td>3.50 (n/a)</td><td>3743.70 (n/a)</td><td>1486.44 (n/a)</td><td>707.70 (n/a)</td><td>491.20 (n/a)</td><td>1409.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>7.99 (-13.24%)</td><td>5.35 (+2.04%)</td><td>6.43 (+0.65%)</td><td>1.73 (-6.72%)</td><td>2.46 <b>(-23.72%)</b></td><td>2431.40 (+7.20%)</td><td>1055.62 (-13.74%)</td><td>651.90 (-0.66%)</td><td>525.00 (+15.26%)</td><td>791.70 (-11.12%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>9.21 (n/a)</td><td>5.24 (n/a)</td><td>6.39 (n/a)</td><td>1.85 (n/a)</td><td>3.22 (n/a)</td><td>2268.00 (n/a)</td><td>1223.72 (n/a)</td><td>656.20 (n/a)</td><td>455.50 (n/a)</td><td>890.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>9.15 <b>(+20.55%)</b></td><td>4.46 <b>(-27.64%)</b></td><td>3.93 <b>(-39.13%)</b></td><td>1.14 <b>(-67.85%)</b></td><td>3.54 <b>(+129.61%)</b></td><td>3686.80 <b>(+210.99%)</b></td><td>1876.32 <b>(+156.52%)</b></td><td>1067.80 <b>(+64.28%)</b></td><td>458.50 (-17.06%)</td><td>1611.66 <b>(+527.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>7.59 (n/a)</td><td>6.16 (n/a)</td><td>6.45 (n/a)</td><td>3.54 (n/a)</td><td>1.54 (n/a)</td><td>1185.50 (n/a)</td><td>731.44 (n/a)</td><td>650.00 (n/a)</td><td>552.80 (n/a)</td><td>257.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>9.85 (-6.78%)</td><td>6.27 (-15.46%)</td><td>7.44 (-1.08%)</td><td>1.24 <b>(-73.54%)</b></td><td>3.25 <b>(+40.67%)</b></td><td>3381.20 <b>(+277.91%)</b></td><td>1144.00 <b>(+86.64%)</b></td><td>563.50 (+1.09%)</td><td>425.70 (+7.28%)</td><td>1257.69 <b>(+535.88%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>10.57 (n/a)</td><td>7.42 (n/a)</td><td>7.52 (n/a)</td><td>4.69 (n/a)</td><td>2.31 (n/a)</td><td>894.70 (n/a)</td><td>612.94 (n/a)</td><td>557.40 (n/a)</td><td>396.80 (n/a)</td><td>197.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>1.96 <b>(+39.70%)</b></td><td>1.32 <b>(+54.67%)</b></td><td>1.07 <b>(+38.71%)</b></td><td>0.86 <b>(+440.31%)</b></td><td>0.48 (-0.66%)</td><td>606.80 <b>(-81.49%)</b></td><td>440.12 <b>(-60.01%)</b></td><td>491.20 <b>(-27.91%)</b></td><td>267.30 <b>(-28.43%)</b></td><td>145.41 <b>(-88.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>1.40 (n/a)</td><td>0.85 (n/a)</td><td>0.77 (n/a)</td><td>0.16 (n/a)</td><td>0.48 (n/a)</td><td>3278.80 (n/a)</td><td>1100.52 (n/a)</td><td>681.40 (n/a)</td><td>373.50 (n/a)</td><td>1227.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.66 <b>(+32.13%)</b></td><td>2.13 <b>(+185.41%)</b></td><td>2.58 <b>(+695.48%)</b></td><td>0.56 <b>(+85.38%)</b></td><td>0.89 <b>(+21.09%)</b></td><td>1856.50 <b>(-46.06%)</b></td><td>704.64 <b>(-70.23%)</b></td><td>406.70 <b>(-87.43%)</b></td><td>393.70 <b>(-24.30%)</b></td><td>644.51 <b>(-51.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>2.02 (n/a)</td><td>0.75 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.74 (n/a)</td><td>3441.60 (n/a)</td><td>2367.16 (n/a)</td><td>3234.80 (n/a)</td><td>520.10 (n/a)</td><td>1341.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.06 (+13.47%)</td><td>2.66 (+6.29%)</td><td>2.66 (-12.76%)</td><td>0.68 (+8.90%)</td><td>1.33 (+14.61%)</td><td>3098.60 (-8.18%)</td><td>1180.74 (-5.93%)</td><td>788.70 (+14.62%)</td><td>516.70 (-11.87%)</td><td>1084.76 (-8.99%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>3.58 (n/a)</td><td>2.51 (n/a)</td><td>3.05 (n/a)</td><td>0.62 (n/a)</td><td>1.16 (n/a)</td><td>3374.50 (n/a)</td><td>1255.22 (n/a)</td><td>688.10 (n/a)</td><td>586.30 (n/a)</td><td>1191.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.03 <b>(+24.35%)</b></td><td>1.56 <b>(+59.56%)</b></td><td>1.61 <b>(+74.51%)</b></td><td>1.02 <b>(+59.08%)</b></td><td>0.38 (-3.73%)</td><td>513.00 <b>(-37.15%)</b></td><td>354.56 <b>(-40.49%)</b></td><td>325.60 <b>(-42.69%)</b></td><td>258.10 (-19.57%)</td><td>98.15 <b>(-49.32%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>1.63 (n/a)</td><td>0.98 (n/a)</td><td>0.92 (n/a)</td><td>0.64 (n/a)</td><td>0.39 (n/a)</td><td>816.20 (n/a)</td><td>595.84 (n/a)</td><td>568.10 (n/a)</td><td>320.90 (n/a)</td><td>193.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (-3.02%)</td><td>0.13 <b>(+42.50%)</b></td><td>0.13 <b>(+61.14%)</b></td><td>0.13 <b>(+96.33%)</b></td><td>0.00 <b>(-87.45%)</b></td><td>261.80 <b>(-49.07%)</b></td><td>249.14 <b>(-35.77%)</b></td><td>248.40 <b>(-37.93%)</b></td><td>242.00 (+3.11%)</td><td>7.82 <b>(-93.55%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.00 (n/a)</td><td>387.88 (n/a)</td><td>400.20 (n/a)</td><td>234.70 (n/a)</td><td>121.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 <b>(+96.50%)</b></td><td>0.12 <b>(+102.31%)</b></td><td>0.11 <b>(+72.76%)</b></td><td>0.09 <b>(+281.96%)</b></td><td>0.02 (+1.54%)</td><td>369.70 <b>(-73.82%)</b></td><td>290.38 <b>(-57.45%)</b></td><td>294.70 <b>(-42.11%)</b></td><td>240.20 <b>(-49.10%)</b></td><td>51.98 <b>(-87.27%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1411.90 (n/a)</td><td>682.44 (n/a)</td><td>509.10 (n/a)</td><td>471.90 (n/a)</td><td>408.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.27 (+18.61%)</td><td>0.22 <b>(+43.20%)</b></td><td>0.23 <b>(+61.05%)</b></td><td>0.14 <b>(+96.30%)</b></td><td>0.05 (-15.35%)</td><td>468.90 <b>(-49.05%)</b></td><td>311.82 <b>(-37.45%)</b></td><td>282.90 <b>(-37.91%)</b></td><td>239.50 (-15.67%)</td><td>93.08 <b>(-63.29%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>920.40 (n/a)</td><td>498.50 (n/a)</td><td>455.60 (n/a)</td><td>284.00 (n/a)</td><td>253.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.29 <b>(+41.70%)</b></td><td>0.22 <b>(+44.58%)</b></td><td>0.22 <b>(+43.56%)</b></td><td>0.11 (+2.16%)</td><td>0.07 <b>(+92.55%)</b></td><td>582.00 (-2.12%)</td><td>331.18 <b>(-25.92%)</b></td><td>301.60 <b>(-30.33%)</b></td><td>223.40 <b>(-29.42%)</b></td><td>144.48 <b>(+40.53%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>594.60 (n/a)</td><td>447.08 (n/a)</td><td>432.90 (n/a)</td><td>316.50 (n/a)</td><td>102.81 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.27 (+19.60%)</td><td>0.19 <b>(+30.49%)</b></td><td>0.19 <b>(+53.64%)</b></td><td>0.11 (+0.32%)</td><td>0.07 <b>(+49.49%)</b></td><td>584.60 (-0.32%)</td><td>397.98 (-18.43%)</td><td>352.50 <b>(-34.92%)</b></td><td>238.60 (-16.40%)</td><td>160.08 <b>(+32.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>586.50 (n/a)</td><td>487.92 (n/a)</td><td>541.60 (n/a)</td><td>285.40 (n/a)</td><td>120.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.51 (-0.67%)</td><td>0.37 (+11.94%)</td><td>0.44 <b>(+71.26%)</b></td><td>0.22 (+1.03%)</td><td>0.14 (+11.36%)</td><td>605.60 (-1.03%)</td><td>404.22 (-7.64%)</td><td>294.60 <b>(-41.61%)</b></td><td>257.80 (+0.66%)</td><td>175.38 (+17.97%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>611.90 (n/a)</td><td>437.68 (n/a)</td><td>504.50 (n/a)</td><td>256.10 (n/a)</td><td>148.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.48 (-10.51%)</td><td>0.36 (-12.02%)</td><td>0.42 (-8.91%)</td><td>0.22 (+3.10%)</td><td>0.12 (-13.41%)</td><td>591.20 (-3.00%)</td><td>405.94 (+12.05%)</td><td>309.50 (+9.79%)</td><td>274.10 (+11.74%)</td><td>155.57 (-0.54%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>609.50 (n/a)</td><td>362.30 (n/a)</td><td>281.90 (n/a)</td><td>245.30 (n/a)</td><td>156.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.51 (+7.72%)</td><td>0.34 (-4.05%)</td><td>0.29 <b>(-33.27%)</b></td><td>0.24 (+13.50%)</td><td>0.11 (-17.13%)</td><td>550.50 (-11.89%)</td><td>410.90 (-1.91%)</td><td>445.30 <b>(+49.83%)</b></td><td>258.60 (-7.15%)</td><td>117.72 <b>(-34.25%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.44 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>624.80 (n/a)</td><td>418.88 (n/a)</td><td>297.20 (n/a)</td><td>278.50 (n/a)</td><td>179.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 <b>(+36.91%)</b></td><td>0.04 <b>(+21.26%)</b></td><td>0.03 (-17.06%)</td><td>0.03 <b>(+214.50%)</b></td><td>0.02 (+14.26%)</td><td>581.00 <b>(-68.20%)</b></td><td>426.06 <b>(-37.16%)</b></td><td>503.50 <b>(+20.57%)</b></td><td>225.40 <b>(-26.96%)</b></td><td>158.77 <b>(-75.44%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:05:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1827.20 (n/a)</td><td>678.00 (n/a)</td><td>417.60 (n/a)</td><td>308.60 (n/a)</td><td>646.47 (n/a)</td>
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
