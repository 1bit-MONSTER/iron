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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-13.36%)</td><td>0.02 (-16.47%)</td><td>0.02 (-15.83%)</td><td>0.02 (-14.09%)</td><td>0.00 (-9.01%)</td><td>401.00 (+16.40%)</td><td>315.70 (+19.90%)</td><td>289.70 (+18.83%)</td><td>272.40 (+15.42%)</td><td>54.27 (+18.89%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>344.50 (n/a)</td><td>263.30 (n/a)</td><td>243.80 (n/a)</td><td>236.00 (n/a)</td><td>45.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-6.07%)</td><td>0.02 (-19.35%)</td><td>0.01 (-19.25%)</td><td>0.01 (-17.62%)</td><td>0.01 (-14.09%)</td><td>584.50 <b>(+21.39%)</b></td><td>421.02 <b>(+23.32%)</b></td><td>428.00 <b>(+23.84%)</b></td><td>248.30 (+6.43%)</td><td>120.29 (+11.52%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>481.50 (n/a)</td><td>341.40 (n/a)</td><td>345.60 (n/a)</td><td>233.30 (n/a)</td><td>107.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-16.14%)</td><td>0.02 (-14.46%)</td><td>0.02 <b>(-36.24%)</b></td><td>0.01 <b>(+85.91%)</b></td><td>0.00 <b>(-45.79%)</b></td><td>576.30 <b>(-46.21%)</b></td><td>395.86 (-10.01%)</td><td>384.80 <b>(+56.81%)</b></td><td>274.90 (+19.21%)</td><td>122.59 <b>(-65.98%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1071.40 (n/a)</td><td>439.88 (n/a)</td><td>245.40 (n/a)</td><td>230.60 (n/a)</td><td>360.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(-20.60%)</b></td><td>0.02 <b>(-23.86%)</b></td><td>0.01 <b>(-21.43%)</b></td><td>0.01 (-8.67%)</td><td>0.00 <b>(-39.27%)</b></td><td>459.10 (+9.49%)</td><td>410.82 <b>(+28.60%)</b></td><td>426.90 <b>(+27.28%)</b></td><td>302.20 <b>(+25.92%)</b></td><td>64.29 (-14.20%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>419.30 (n/a)</td><td>319.46 (n/a)</td><td>335.40 (n/a)</td><td>240.00 (n/a)</td><td>74.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (-4.49%)</td><td>0.01 (-16.84%)</td><td>0.01 (-8.92%)</td><td>0.01 (-14.47%)</td><td>0.01 (-16.03%)</td><td>624.40 (+16.91%)</td><td>467.00 (+16.61%)</td><td>511.00 (+9.80%)</td><td>235.50 (+4.71%)</td><td>144.04 (-5.75%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.10 (n/a)</td><td>400.48 (n/a)</td><td>465.40 (n/a)</td><td>224.90 (n/a)</td><td>152.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 <b>(+26.36%)</b></td><td>0.02 (+1.00%)</td><td>0.01 (-16.95%)</td><td>0.01 (-14.01%)</td><td>0.01 <b>(+55.25%)</b></td><td>635.20 (+16.29%)</td><td>468.76 (+11.64%)</td><td>605.20 <b>(+20.39%)</b></td><td>196.10 <b>(-20.86%)</b></td><td>207.00 <b>(+50.44%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.20 (n/a)</td><td>419.88 (n/a)</td><td>502.70 (n/a)</td><td>247.80 (n/a)</td><td>137.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (-19.25%)</td><td>0.03 <b>(-27.99%)</b></td><td>0.03 <b>(-52.35%)</b></td><td>0.02 <b>(-24.77%)</b></td><td>0.01 (-7.30%)</td><td>519.70 <b>(+32.92%)</b></td><td>401.38 <b>(+42.50%)</b></td><td>479.40 <b>(+109.89%)</b></td><td>251.90 <b>(+23.84%)</b></td><td>130.27 <b>(+47.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>391.00 (n/a)</td><td>281.68 (n/a)</td><td>228.40 (n/a)</td><td>203.40 (n/a)</td><td>88.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (+3.25%)</td><td>0.03 (+3.44%)</td><td>0.03 (-2.34%)</td><td>0.03 <b>(+25.20%)</b></td><td>0.01 (-7.11%)</td><td>491.30 <b>(-20.13%)</b></td><td>397.84 (-5.42%)</td><td>426.40 (+2.40%)</td><td>270.30 (-3.15%)</td><td>90.16 <b>(-28.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>615.10 (n/a)</td><td>420.62 (n/a)</td><td>416.40 (n/a)</td><td>279.10 (n/a)</td><td>126.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (-16.04%)</td><td>0.04 (-17.40%)</td><td>0.03 <b>(-22.65%)</b></td><td>0.02 <b>(+160.43%)</b></td><td>0.02 <b>(-31.39%)</b></td><td>715.70 <b>(-61.60%)</b></td><td>417.92 <b>(-26.75%)</b></td><td>351.90 <b>(+29.28%)</b></td><td>235.10 (+19.10%)</td><td>202.60 <b>(-72.03%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1863.90 (n/a)</td><td>570.52 (n/a)</td><td>272.20 (n/a)</td><td>197.40 (n/a)</td><td>724.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (-10.58%)</td><td>0.03 (-17.93%)</td><td>0.03 <b>(-31.28%)</b></td><td>0.02 (-13.89%)</td><td>0.01 (-19.03%)</td><td>583.10 (+16.13%)</td><td>422.10 (+19.67%)</td><td>422.50 <b>(+45.54%)</b></td><td>265.80 (+11.87%)</td><td>128.98 (+1.57%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.10 (n/a)</td><td>352.72 (n/a)</td><td>290.30 (n/a)</td><td>237.60 (n/a)</td><td>126.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(-31.06%)</b></td><td>0.03 <b>(-30.83%)</b></td><td>0.02 <b>(-43.29%)</b></td><td>0.02 (-4.06%)</td><td>0.01 <b>(-58.55%)</b></td><td>549.70 (+4.23%)</td><td>488.44 <b>(+33.17%)</b></td><td>503.80 <b>(+76.34%)</b></td><td>349.70 <b>(+45.04%)</b></td><td>82.09 <b>(-41.34%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.40 (n/a)</td><td>366.78 (n/a)</td><td>285.70 (n/a)</td><td>241.10 (n/a)</td><td>139.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 <b>(+68.01%)</b></td><td>0.02 (+2.43%)</td><td>0.02 (+7.76%)</td><td>0.01 <b>(-67.34%)</b></td><td>0.01 <b>(+258.22%)</b></td><td>1973.60 <b>(+206.22%)</b></td><td>798.46 <b>(+43.59%)</b></td><td>567.60 (-7.21%)</td><td>264.10 <b>(-40.48%)</b></td><td>672.11 <b>(+615.20%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>644.50 (n/a)</td><td>556.06 (n/a)</td><td>611.70 (n/a)</td><td>443.70 (n/a)</td><td>93.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 <b>(-22.82%)</b></td><td>0.08 (-16.82%)</td><td>0.09 (-6.17%)</td><td>0.06 (-4.60%)</td><td>0.02 <b>(-31.99%)</b></td><td>426.40 (+4.82%)</td><td>338.50 (+17.76%)</td><td>282.00 (+6.58%)</td><td>277.90 <b>(+29.56%)</b></td><td>79.66 (-3.89%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>406.80 (n/a)</td><td>287.44 (n/a)</td><td>264.60 (n/a)</td><td>214.50 (n/a)</td><td>82.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (+15.51%)</td><td>0.08 (+9.72%)</td><td>0.07 (-11.90%)</td><td>0.05 (+14.29%)</td><td>0.02 (+16.62%)</td><td>505.00 (-12.51%)</td><td>350.86 (-8.98%)</td><td>350.30 (+13.51%)</td><td>238.50 (-13.43%)</td><td>112.51 (-14.93%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.20 (n/a)</td><td>385.48 (n/a)</td><td>308.60 (n/a)</td><td>275.50 (n/a)</td><td>132.25 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 <b>(-24.62%)</b></td><td>0.06 (-17.94%)</td><td>0.05 (-18.95%)</td><td>0.04 (-10.51%)</td><td>0.02 <b>(-31.60%)</b></td><td>604.50 (+11.74%)</td><td>460.80 (+16.55%)</td><td>542.50 <b>(+23.38%)</b></td><td>246.90 <b>(+32.67%)</b></td><td>150.76 (+0.82%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>541.00 (n/a)</td><td>395.38 (n/a)</td><td>439.70 (n/a)</td><td>186.10 (n/a)</td><td>149.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (-17.56%)</td><td>0.06 (+2.02%)</td><td>0.06 <b>(+23.28%)</b></td><td>0.04 (-7.30%)</td><td>0.02 <b>(-30.96%)</b></td><td>577.60 (+7.86%)</td><td>413.00 (-5.65%)</td><td>409.60 (-18.88%)</td><td>271.70 <b>(+21.29%)</b></td><td>118.40 (-8.15%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>535.50 (n/a)</td><td>437.72 (n/a)</td><td>504.90 (n/a)</td><td>224.00 (n/a)</td><td>128.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 <b>(-23.49%)</b></td><td>0.06 <b>(-26.08%)</b></td><td>0.05 <b>(-41.62%)</b></td><td>0.04 (+2.72%)</td><td>0.01 <b>(-53.50%)</b></td><td>580.40 (-2.63%)</td><td>458.16 <b>(+24.10%)</b></td><td>463.90 <b>(+71.31%)</b></td><td>326.50 <b>(+30.70%)</b></td><td>90.20 <b>(-41.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>596.10 (n/a)</td><td>369.18 (n/a)</td><td>270.80 (n/a)</td><td>249.80 (n/a)</td><td>153.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(-45.74%)</b></td><td>0.06 (-11.64%)</td><td>0.06 (+19.45%)</td><td>0.04 (-2.02%)</td><td>0.01 <b>(-66.19%)</b></td><td>643.60 (+2.06%)</td><td>460.38 (-1.53%)</td><td>427.60 (-16.29%)</td><td>354.90 <b>(+84.27%)</b></td><td>116.32 <b>(-33.84%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>630.60 (n/a)</td><td>467.52 (n/a)</td><td>510.80 (n/a)</td><td>192.60 (n/a)</td><td>175.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 (+0.26%)</td><td>0.14 (+10.72%)</td><td>0.14 <b>(+36.19%)</b></td><td>0.10 <b>(+31.38%)</b></td><td>0.05 (-17.98%)</td><td>481.80 <b>(-23.87%)</b></td><td>366.44 (-14.75%)</td><td>349.60 <b>(-26.57%)</b></td><td>234.60 (-0.26%)</td><td>109.90 <b>(-32.90%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>632.90 (n/a)</td><td>429.82 (n/a)</td><td>476.10 (n/a)</td><td>235.20 (n/a)</td><td>163.78 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.19 <b>(-27.30%)</b></td><td>0.13 <b>(-26.50%)</b></td><td>0.12 <b>(-31.44%)</b></td><td>0.09 (-3.31%)</td><td>0.04 <b>(-27.45%)</b></td><td>528.30 (+3.41%)</td><td>402.96 <b>(+32.72%)</b></td><td>413.20 <b>(+45.85%)</b></td><td>260.70 <b>(+37.57%)</b></td><td>123.79 (+0.43%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>510.90 (n/a)</td><td>303.62 (n/a)</td><td>283.30 (n/a)</td><td>189.50 (n/a)</td><td>123.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.20 (-18.11%)</td><td>0.12 <b>(-34.64%)</b></td><td>0.11 <b>(-35.12%)</b></td><td>0.08 <b>(-20.44%)</b></td><td>0.05 <b>(-23.23%)</b></td><td>613.00 <b>(+25.69%)</b></td><td>447.84 <b>(+50.98%)</b></td><td>457.60 <b>(+54.13%)</b></td><td>241.80 <b>(+22.12%)</b></td><td>133.11 (+13.14%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>487.70 (n/a)</td><td>296.62 (n/a)</td><td>296.90 (n/a)</td><td>198.00 (n/a)</td><td>117.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.24 (+19.22%)</td><td>0.18 (+14.94%)</td><td>0.20 <b>(+23.61%)</b></td><td>0.10 (-1.32%)</td><td>0.07 <b>(+73.52%)</b></td><td>504.20 (+1.33%)</td><td>325.60 (-4.99%)</td><td>244.80 (-19.10%)</td><td>203.70 (-16.10%)</td><td>144.83 <b>(+46.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>497.60 (n/a)</td><td>342.70 (n/a)</td><td>302.60 (n/a)</td><td>242.80 (n/a)</td><td>99.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.22 (-0.14%)</td><td>0.14 (-18.86%)</td><td>0.12 <b>(-30.70%)</b></td><td>0.10 (+5.69%)</td><td>0.05 (-14.74%)</td><td>515.70 (-5.39%)</td><td>391.80 (+18.59%)</td><td>398.50 <b>(+44.28%)</b></td><td>221.00 (+0.14%)</td><td>107.57 <b>(-21.91%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>545.10 (n/a)</td><td>330.38 (n/a)</td><td>276.20 (n/a)</td><td>220.70 (n/a)</td><td>137.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 (-8.82%)</td><td>0.12 <b>(-32.59%)</b></td><td>0.11 <b>(-40.09%)</b></td><td>0.03 <b>(-81.63%)</b></td><td>0.07 <b>(+137.02%)</b></td><td>1833.80 <b>(+444.32%)</b></td><td>662.78 <b>(+142.95%)</b></td><td>457.50 <b>(+66.91%)</b></td><td>235.30 (+9.65%)</td><td>665.64 <b>(+1376.54%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>336.90 (n/a)</td><td>272.80 (n/a)</td><td>274.10 (n/a)</td><td>214.60 (n/a)</td><td>45.08 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (-19.39%)</td><td>0.01 <b>(-30.76%)</b></td><td>0.01 <b>(-37.80%)</b></td><td>0.01 <b>(-45.33%)</b></td><td>0.00 <b>(+131.71%)</b></td><td>487.60 <b>(+82.90%)</b></td><td>381.46 <b>(+53.34%)</b></td><td>410.70 <b>(+60.74%)</b></td><td>270.60 <b>(+24.07%)</b></td><td>104.23 <b>(+403.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>266.60 (n/a)</td><td>248.76 (n/a)</td><td>255.50 (n/a)</td><td>218.10 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (-7.15%)</td><td>0.01 (-18.76%)</td><td>0.01 <b>(-29.31%)</b></td><td>0.00 <b>(-53.97%)</b></td><td>0.00 <b>(+43.83%)</b></td><td>1054.70 <b>(+117.24%)</b></td><td>517.96 <b>(+52.05%)</b></td><td>411.30 <b>(+41.49%)</b></td><td>251.10 (+7.68%)</td><td>335.06 <b>(+207.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.50 (n/a)</td><td>340.64 (n/a)</td><td>290.70 (n/a)</td><td>233.20 (n/a)</td><td>108.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (-10.19%)</td><td>0.01 (-17.92%)</td><td>0.01 (+0.25%)</td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (-3.92%)</td><td>1851.60 <b>(+200.05%)</b></td><td>656.16 <b>(+67.70%)</b></td><td>409.60 (-0.24%)</td><td>228.10 (+11.38%)</td><td>673.68 <b>(+287.34%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>617.10 (n/a)</td><td>391.26 (n/a)</td><td>410.60 (n/a)</td><td>204.80 (n/a)</td><td>173.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 <b>(-24.91%)</b></td><td>0.01 (-14.64%)</td><td>0.01 (-1.38%)</td><td>0.00 (-19.85%)</td><td>0.00 <b>(-33.50%)</b></td><td>673.30 <b>(+24.75%)</b></td><td>429.20 (+14.19%)</td><td>410.70 (+1.41%)</td><td>257.80 <b>(+33.16%)</b></td><td>151.36 (+18.13%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>539.70 (n/a)</td><td>375.86 (n/a)</td><td>405.00 (n/a)</td><td>193.60 (n/a)</td><td>128.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 <b>(-45.03%)</b></td><td>0.01 <b>(-29.03%)</b></td><td>0.01 <b>(-38.17%)</b></td><td>0.00 (+3.59%)</td><td>0.00 <b>(-77.45%)</b></td><td>537.50 (-3.47%)</td><td>427.60 <b>(+20.78%)</b></td><td>411.80 <b>(+61.74%)</b></td><td>369.10 <b>(+81.91%)</b></td><td>64.63 <b>(-61.46%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>556.80 (n/a)</td><td>354.04 (n/a)</td><td>254.60 (n/a)</td><td>202.90 (n/a)</td><td>167.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (+5.41%)</td><td>0.01 (+0.80%)</td><td>0.00 (-9.31%)</td><td>0.00 (+1.49%)</td><td>0.00 (+16.70%)</td><td>614.80 (-1.47%)</td><td>501.12 (+0.76%)</td><td>559.80 (+10.26%)</td><td>304.80 (-5.14%)</td><td>126.98 (+12.52%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>624.00 (n/a)</td><td>497.32 (n/a)</td><td>507.70 (n/a)</td><td>321.30 (n/a)</td><td>112.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+22.80%)</b></td><td>0.02 <b>(+34.95%)</b></td><td>0.02 <b>(+33.61%)</b></td><td>0.02 <b>(+42.00%)</b></td><td>0.00 <b>(-27.62%)</b></td><td>290.20 <b>(-29.56%)</b></td><td>261.14 <b>(-26.59%)</b></td><td>257.10 <b>(-25.15%)</b></td><td>239.30 (-18.58%)</td><td>19.05 <b>(-58.27%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>412.00 (n/a)</td><td>355.74 (n/a)</td><td>343.50 (n/a)</td><td>293.90 (n/a)</td><td>45.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-2.24%)</td><td>0.02 <b>(+21.49%)</b></td><td>0.02 <b>(+57.14%)</b></td><td>0.01 <b>(+32.57%)</b></td><td>0.01 (-15.73%)</td><td>462.70 <b>(-24.57%)</b></td><td>329.26 <b>(-21.80%)</b></td><td>268.60 <b>(-36.37%)</b></td><td>228.50 (+2.28%)</td><td>105.36 <b>(-32.63%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.40 (n/a)</td><td>421.06 (n/a)</td><td>422.10 (n/a)</td><td>223.40 (n/a)</td><td>156.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+12.45%)</td><td>0.02 (+18.08%)</td><td>0.02 (+0.55%)</td><td>0.01 <b>(+25.89%)</b></td><td>0.00 (-16.98%)</td><td>373.70 <b>(-20.56%)</b></td><td>280.74 (-18.80%)</td><td>289.40 (-0.52%)</td><td>218.30 (-11.04%)</td><td>61.92 <b>(-44.50%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>470.40 (n/a)</td><td>345.76 (n/a)</td><td>290.90 (n/a)</td><td>245.40 (n/a)</td><td>111.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+2.29%)</td><td>0.02 (+18.92%)</td><td>0.01 <b>(+33.60%)</b></td><td>0.01 (-6.98%)</td><td>0.01 (+13.51%)</td><td>628.50 (+7.51%)</td><td>396.52 (-13.78%)</td><td>403.80 <b>(-25.15%)</b></td><td>237.10 (-2.27%)</td><td>162.07 (+10.83%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.60 (n/a)</td><td>459.90 (n/a)</td><td>539.50 (n/a)</td><td>242.60 (n/a)</td><td>146.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+17.74%)</td><td>0.01 (+3.31%)</td><td>0.01 (-11.03%)</td><td>0.01 (+4.41%)</td><td>0.00 (+12.73%)</td><td>550.60 (-4.23%)</td><td>388.42 (-3.11%)</td><td>381.80 (+12.39%)</td><td>247.30 (-15.08%)</td><td>116.90 (-8.01%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.90 (n/a)</td><td>400.90 (n/a)</td><td>339.70 (n/a)</td><td>291.20 (n/a)</td><td>127.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 <b>(-36.81%)</b></td><td>0.01 <b>(-44.74%)</b></td><td>0.01 <b>(-38.66%)</b></td><td>0.00 <b>(-68.38%)</b></td><td>0.00 <b>(-21.53%)</b></td><td>1780.90 <b>(+216.21%)</b></td><td>792.10 <b>(+116.68%)</b></td><td>534.00 <b>(+63.05%)</b></td><td>402.60 <b>(+58.25%)</b></td><td>567.21 <b>(+336.10%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.20 (n/a)</td><td>365.56 (n/a)</td><td>327.50 (n/a)</td><td>254.40 (n/a)</td><td>130.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (+5.39%)</td><td>0.03 (-10.47%)</td><td>0.02 (-17.92%)</td><td>0.01 <b>(-27.74%)</b></td><td>0.01 (+16.00%)</td><td>715.00 <b>(+38.38%)</b></td><td>433.40 (+17.41%)</td><td>428.70 <b>(+21.82%)</b></td><td>230.50 (-5.10%)</td><td>177.99 <b>(+51.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.70 (n/a)</td><td>369.12 (n/a)</td><td>351.90 (n/a)</td><td>242.90 (n/a)</td><td>117.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (-0.48%)</td><td>0.02 (-14.19%)</td><td>0.02 <b>(-36.32%)</b></td><td>0.02 (+8.98%)</td><td>0.01 (-7.61%)</td><td>574.50 (-8.24%)</td><td>463.62 (+14.67%)</td><td>523.50 <b>(+57.02%)</b></td><td>297.50 (+0.51%)</td><td>113.89 (-16.26%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>626.10 (n/a)</td><td>404.30 (n/a)</td><td>333.40 (n/a)</td><td>296.00 (n/a)</td><td>136.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (+7.38%)</td><td>0.03 (+8.35%)</td><td>0.02 (+1.79%)</td><td>0.02 <b>(+242.52%)</b></td><td>0.01 <b>(-28.58%)</b></td><td>564.50 <b>(-70.80%)</b></td><td>422.16 <b>(-38.11%)</b></td><td>436.40 (-1.76%)</td><td>263.60 (-6.86%)</td><td>131.05 <b>(-81.39%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1933.50 (n/a)</td><td>682.06 (n/a)</td><td>444.20 (n/a)</td><td>283.00 (n/a)</td><td>704.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(-28.84%)</b></td><td>0.02 (-12.25%)</td><td>0.02 (+1.78%)</td><td>0.02 (-11.03%)</td><td>0.01 <b>(-47.40%)</b></td><td>588.30 (+12.40%)</td><td>451.78 (+7.41%)</td><td>463.80 (-1.76%)</td><td>298.90 <b>(+40.53%)</b></td><td>103.39 (-16.29%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.40 (n/a)</td><td>420.60 (n/a)</td><td>472.10 (n/a)</td><td>212.70 (n/a)</td><td>123.51 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(+41.22%)</b></td><td>0.03 (+10.84%)</td><td>0.02 (-4.25%)</td><td>0.02 <b>(-22.14%)</b></td><td>0.01 <b>(+297.74%)</b></td><td>616.10 <b>(+28.43%)</b></td><td>441.66 (+0.98%)</td><td>474.00 (+4.43%)</td><td>257.90 <b>(-29.21%)</b></td><td>160.53 <b>(+265.44%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>479.70 (n/a)</td><td>437.38 (n/a)</td><td>453.90 (n/a)</td><td>364.30 (n/a)</td><td>43.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-17.77%)</td><td>0.02 (-3.61%)</td><td>0.02 (-6.04%)</td><td>0.02 (+6.68%)</td><td>0.00 <b>(-42.09%)</b></td><td>633.80 (-6.26%)</td><td>526.52 (+0.83%)</td><td>520.70 (+6.42%)</td><td>443.80 <b>(+21.62%)</b></td><td>79.35 <b>(-35.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>676.10 (n/a)</td><td>522.16 (n/a)</td><td>489.30 (n/a)</td><td>364.90 (n/a)</td><td>122.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (-9.03%)</td><td>0.05 <b>(-26.42%)</b></td><td>0.04 <b>(-48.27%)</b></td><td>0.04 (-9.66%)</td><td>0.02 (+5.89%)</td><td>577.00 (+10.68%)</td><td>440.14 <b>(+39.43%)</b></td><td>503.80 <b>(+93.32%)</b></td><td>270.20 (+9.93%)</td><td>147.21 <b>(+25.69%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>521.30 (n/a)</td><td>315.66 (n/a)</td><td>260.60 (n/a)</td><td>245.80 (n/a)</td><td>117.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (-15.81%)</td><td>0.06 (+16.67%)</td><td>0.05 (+9.38%)</td><td>0.04 <b>(+65.83%)</b></td><td>0.02 <b>(-32.62%)</b></td><td>576.40 <b>(-39.70%)</b></td><td>409.96 <b>(-24.30%)</b></td><td>444.70 (-8.57%)</td><td>281.30 (+18.74%)</td><td>122.96 <b>(-53.15%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>955.90 (n/a)</td><td>541.56 (n/a)</td><td>486.40 (n/a)</td><td>236.90 (n/a)</td><td>262.45 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(-35.25%)</b></td><td>0.06 <b>(-37.03%)</b></td><td>0.06 <b>(-27.49%)</b></td><td>0.03 <b>(-61.24%)</b></td><td>0.02 <b>(+20.88%)</b></td><td>774.40 <b>(+158.05%)</b></td><td>430.98 <b>(+77.47%)</b></td><td>338.30 <b>(+37.91%)</b></td><td>286.60 <b>(+54.42%)</b></td><td>204.07 <b>(+385.40%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>300.10 (n/a)</td><td>242.84 (n/a)</td><td>245.30 (n/a)</td><td>185.60 (n/a)</td><td>42.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (+10.46%)</td><td>0.06 (-4.82%)</td><td>0.05 (-17.33%)</td><td>0.04 (+0.03%)</td><td>0.02 (+15.82%)</td><td>554.00 (-0.04%)</td><td>403.28 (+6.52%)</td><td>426.00 <b>(+20.95%)</b></td><td>252.90 (-9.48%)</td><td>120.47 (+5.80%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.20 (n/a)</td><td>378.58 (n/a)</td><td>352.20 (n/a)</td><td>279.40 (n/a)</td><td>113.87 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (+3.42%)</td><td>0.04 (-12.55%)</td><td>0.05 (-1.50%)</td><td>0.01 <b>(-71.89%)</b></td><td>0.02 <b>(+124.58%)</b></td><td>2032.80 <b>(+255.70%)</b></td><td>773.14 <b>(+63.34%)</b></td><td>464.00 (+1.51%)</td><td>360.10 (-3.33%)</td><td>708.56 <b>(+745.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>571.50 (n/a)</td><td>473.34 (n/a)</td><td>457.10 (n/a)</td><td>372.50 (n/a)</td><td>83.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (-1.40%)</td><td>0.05 (-8.04%)</td><td>0.05 (-13.19%)</td><td>0.04 <b>(-20.62%)</b></td><td>0.02 <b>(+38.21%)</b></td><td>577.40 <b>(+25.99%)</b></td><td>416.44 (+13.06%)</td><td>429.50 (+15.21%)</td><td>278.30 (+1.42%)</td><td>118.32 <b>(+76.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>458.30 (n/a)</td><td>368.34 (n/a)</td><td>372.80 (n/a)</td><td>274.40 (n/a)</td><td>66.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>523.80 (n/a)</td><td>428.60 (n/a)</td><td>456.70 (n/a)</td><td>267.40 (n/a)</td><td>97.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.60 (n/a)</td><td>474.66 (n/a)</td><td>535.90 (n/a)</td><td>140.40 (n/a)</td><td>209.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.90 (n/a)</td><td>428.32 (n/a)</td><td>455.10 (n/a)</td><td>243.60 (n/a)</td><td>149.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.40 (n/a)</td><td>340.42 (n/a)</td><td>306.90 (n/a)</td><td>250.60 (n/a)</td><td>98.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1922.30 (n/a)</td><td>659.74 (n/a)</td><td>386.00 (n/a)</td><td>209.30 (n/a)</td><td>713.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.10 (n/a)</td><td>308.72 (n/a)</td><td>260.80 (n/a)</td><td>212.30 (n/a)</td><td>115.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>464.80 (n/a)</td><td>344.18 (n/a)</td><td>299.20 (n/a)</td><td>252.70 (n/a)</td><td>100.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>545.90 (n/a)</td><td>435.40 (n/a)</td><td>472.50 (n/a)</td><td>238.10 (n/a)</td><td>126.94 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>618.10 (n/a)</td><td>459.80 (n/a)</td><td>527.00 (n/a)</td><td>243.10 (n/a)</td><td>171.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 (+17.46%)</td><td>0.16 <b>(+23.36%)</b></td><td>0.16 <b>(+35.49%)</b></td><td>0.11 <b>(+37.45%)</b></td><td>0.05 (+0.73%)</td><td>459.60 <b>(-27.24%)</b></td><td>338.44 <b>(-21.97%)</b></td><td>302.10 <b>(-26.19%)</b></td><td>233.00 (-14.87%)</td><td>110.52 <b>(-33.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>631.70 (n/a)</td><td>433.74 (n/a)</td><td>409.30 (n/a)</td><td>273.70 (n/a)</td><td>166.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>586.80 (n/a)</td><td>376.38 (n/a)</td><td>299.20 (n/a)</td><td>203.40 (n/a)</td><td>165.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>614.40 (n/a)</td><td>433.50 (n/a)</td><td>423.80 (n/a)</td><td>283.70 (n/a)</td><td>150.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.40 (n/a)</td><td>412.12 (n/a)</td><td>427.30 (n/a)</td><td>306.80 (n/a)</td><td>111.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1966.40 (n/a)</td><td>863.88 (n/a)</td><td>636.70 (n/a)</td><td>271.90 (n/a)</td><td>676.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1910.50 (n/a)</td><td>875.32 (n/a)</td><td>633.20 (n/a)</td><td>261.80 (n/a)</td><td>648.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>480.40 (n/a)</td><td>316.56 (n/a)</td><td>297.70 (n/a)</td><td>239.10 (n/a)</td><td>95.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.10 (n/a)</td><td>351.74 (n/a)</td><td>300.70 (n/a)</td><td>220.90 (n/a)</td><td>129.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>437.44 (n/a)</td><td>466.80 (n/a)</td><td>269.40 (n/a)</td><td>116.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>482.40 (n/a)</td><td>334.40 (n/a)</td><td>275.60 (n/a)</td><td>219.40 (n/a)</td><td>114.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1086.60 (n/a)</td><td>529.86 (n/a)</td><td>515.80 (n/a)</td><td>234.30 (n/a)</td><td>340.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.30 (n/a)</td><td>400.00 (n/a)</td><td>354.20 (n/a)</td><td>271.00 (n/a)</td><td>123.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>626.20 (n/a)</td><td>363.94 (n/a)</td><td>307.70 (n/a)</td><td>241.80 (n/a)</td><td>151.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>592.80 (n/a)</td><td>461.40 (n/a)</td><td>514.40 (n/a)</td><td>218.80 (n/a)</td><td>143.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.60 (n/a)</td><td>389.72 (n/a)</td><td>381.90 (n/a)</td><td>238.50 (n/a)</td><td>144.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.20 (n/a)</td><td>363.06 (n/a)</td><td>425.70 (n/a)</td><td>215.80 (n/a)</td><td>120.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.50 (n/a)</td><td>306.20 (n/a)</td><td>247.70 (n/a)</td><td>205.30 (n/a)</td><td>139.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>800.30 (n/a)</td><td>514.80 (n/a)</td><td>441.50 (n/a)</td><td>201.80 (n/a)</td><td>235.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.90 (n/a)</td><td>410.88 (n/a)</td><td>435.40 (n/a)</td><td>188.50 (n/a)</td><td>138.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.30 (n/a)</td><td>465.12 (n/a)</td><td>491.30 (n/a)</td><td>314.20 (n/a)</td><td>122.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1929.90 (n/a)</td><td>660.86 (n/a)</td><td>399.10 (n/a)</td><td>259.30 (n/a)</td><td>712.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>443.24 (n/a)</td><td>453.00 (n/a)</td><td>271.70 (n/a)</td><td>127.06 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.60 (n/a)</td><td>468.36 (n/a)</td><td>467.00 (n/a)</td><td>250.30 (n/a)</td><td>144.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>573.20 (n/a)</td><td>435.06 (n/a)</td><td>488.40 (n/a)</td><td>161.40 (n/a)</td><td>164.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.50 (n/a)</td><td>420.86 (n/a)</td><td>445.70 (n/a)</td><td>252.30 (n/a)</td><td>121.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>678.80 (n/a)</td><td>486.60 (n/a)</td><td>486.90 (n/a)</td><td>388.30 (n/a)</td><td>118.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.60 (n/a)</td><td>430.32 (n/a)</td><td>441.60 (n/a)</td><td>305.10 (n/a)</td><td>106.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>755.10 (n/a)</td><td>384.40 (n/a)</td><td>311.90 (n/a)</td><td>151.90 (n/a)</td><td>233.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>591.50 (n/a)</td><td>316.42 (n/a)</td><td>247.70 (n/a)</td><td>217.80 (n/a)</td><td>156.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.30 (n/a)</td><td>372.64 (n/a)</td><td>313.50 (n/a)</td><td>209.80 (n/a)</td><td>164.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>526.60 (n/a)</td><td>392.82 (n/a)</td><td>334.00 (n/a)</td><td>281.90 (n/a)</td><td>121.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>679.60 (n/a)</td><td>504.42 (n/a)</td><td>486.80 (n/a)</td><td>377.70 (n/a)</td><td>132.49 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>522.20 (n/a)</td><td>378.82 (n/a)</td><td>360.50 (n/a)</td><td>301.40 (n/a)</td><td>83.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>826.10 (n/a)</td><td>423.58 (n/a)</td><td>360.00 (n/a)</td><td>246.90 (n/a)</td><td>230.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>647.50 (n/a)</td><td>440.68 (n/a)</td><td>490.10 (n/a)</td><td>247.30 (n/a)</td><td>162.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>565.10 (n/a)</td><td>406.64 (n/a)</td><td>411.10 (n/a)</td><td>259.10 (n/a)</td><td>133.87 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>510.30 (n/a)</td><td>420.68 (n/a)</td><td>451.20 (n/a)</td><td>210.80 (n/a)</td><td>120.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>546.00 (n/a)</td><td>451.08 (n/a)</td><td>503.90 (n/a)</td><td>299.60 (n/a)</td><td>102.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.62 <b>(+38.69%)</b></td><td>0.41 (+2.39%)</td><td>0.37 (-10.76%)</td><td>0.34 (-6.77%)</td><td>0.12 <b>(+242.66%)</b></td><td>654.20 (+7.28%)</td><td>562.98 (+1.85%)</td><td>600.10 (+12.06%)</td><td>358.90 <b>(-27.89%)</b></td><td>117.23 <b>(+151.60%)</b></td><td>26.30 <b>(+38.69%)</b></td><td>17.58 (+2.39%)</td><td>15.73 (-10.76%)</td><td>14.43 (-6.77%)</td><td>4.92 <b>(+242.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.44 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.03 (n/a)</td><td>609.80 (n/a)</td><td>552.76 (n/a)</td><td>535.50 (n/a)</td><td>497.70 (n/a)</td><td>46.59 (n/a)</td><td>18.96 (n/a)</td><td>17.17 (n/a)</td><td>17.62 (n/a)</td><td>15.47 (n/a)</td><td>1.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.49 (-17.45%)</td><td>0.35 <b>(-25.00%)</b></td><td>0.34 <b>(-27.77%)</b></td><td>0.12 <b>(-63.87%)</b></td><td>0.15 <b>(+34.87%)</b></td><td>1786.60 <b>(+176.78%)</b></td><td>807.02 <b>(+62.82%)</b></td><td>659.30 <b>(+38.45%)</b></td><td>453.10 <b>(+21.15%)</b></td><td>556.67 <b>(+374.22%)</b></td><td>20.83 (-17.45%)</td><td>14.93 <b>(-25.00%)</b></td><td>14.31 <b>(-27.77%)</b></td><td>5.28 <b>(-63.87%)</b></td><td>6.22 <b>(+34.87%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td><td>645.50 (n/a)</td><td>495.66 (n/a)</td><td>476.20 (n/a)</td><td>374.00 (n/a)</td><td>117.39 (n/a)</td><td>25.23 (n/a)</td><td>19.90 (n/a)</td><td>19.82 (n/a)</td><td>14.62 (n/a)</td><td>4.61 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.31 (+0.82%)</td><td>0.31 (+0.20%)</td><td>0.31 (+0.94%)</td><td>0.30 (-0.74%)</td><td>0.00 <b>(+53.91%)</b></td><td>83893.30 (+0.74%)</td><td>81978.16 (-0.18%)</td><td>81379.50 (-0.93%)</td><td>80588.50 (-0.81%)</td><td>1318.91 <b>(+54.14%)</b></td><td>213.18 (+0.82%)</td><td>209.61 (+0.20%)</td><td>211.11 (+0.94%)</td><td>204.78 (-0.74%)</td><td>3.35 <b>(+53.91%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83273.80 (n/a)</td><td>82128.88 (n/a)</td><td>82142.30 (n/a)</td><td>81250.00 (n/a)</td><td>855.65 (n/a)</td><td>211.44 (n/a)</td><td>209.20 (n/a)</td><td>209.15 (n/a)</td><td>206.31 (n/a)</td><td>2.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>1.02 (-0.71%)</td><td>1.01 (+2.07%)</td><td>1.01 (+0.41%)</td><td>1.00 (+10.52%)</td><td>0.01 <b>(-81.61%)</b></td><td>25244.00 (-9.52%)</td><td>24935.88 (-2.23%)</td><td>24845.20 (-0.41%)</td><td>24681.70 (+0.72%)</td><td>226.43 <b>(-83.40%)</b></td><td>696.06 (-0.71%)</td><td>689.01 (+2.07%)</td><td>691.48 (+0.41%)</td><td>680.55 (+10.52%)</td><td>6.24 <b>(-81.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.03 (n/a)</td><td>0.99 (n/a)</td><td>1.01 (n/a)</td><td>0.90 (n/a)</td><td>0.05 (n/a)</td><td>27900.10 (n/a)</td><td>25505.46 (n/a)</td><td>24947.40 (n/a)</td><td>24505.80 (n/a)</td><td>1364.21 (n/a)</td><td>701.05 (n/a)</td><td>675.03 (n/a)</td><td>688.64 (n/a)</td><td>615.76 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.83 (+0.86%)</td><td>0.81 (-0.23%)</td><td>0.81 (-0.31%)</td><td>0.79 (-1.19%)</td><td>0.02 <b>(+86.60%)</b></td><td>95975.80 (+1.20%)</td><td>93695.72 (+0.26%)</td><td>93761.90 (+0.31%)</td><td>91052.40 (-0.85%)</td><td>2090.20 <b>(+87.61%)</b></td><td>754.72 (+0.86%)</td><td>733.73 (-0.23%)</td><td>732.91 (-0.31%)</td><td>716.01 (-1.19%)</td><td>16.42 <b>(+86.60%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94836.80 (n/a)</td><td>93450.38 (n/a)</td><td>93471.90 (n/a)</td><td>91832.30 (n/a)</td><td>1114.15 (n/a)</td><td>748.31 (n/a)</td><td>735.44 (n/a)</td><td>735.19 (n/a)</td><td>724.61 (n/a)</td><td>8.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.78 (+0.23%)</td><td>0.77 (+0.72%)</td><td>0.77 (+0.62%)</td><td>0.75 (+0.79%)</td><td>0.01 (-11.39%)</td><td>100975.30 (-0.78%)</td><td>98166.04 (-0.72%)</td><td>97806.90 (-0.62%)</td><td>96859.60 (-0.23%)</td><td>1629.90 (-12.12%)</td><td>709.48 (+0.23%)</td><td>700.18 (+0.72%)</td><td>702.60 (+0.62%)</td><td>680.56 (+0.79%)</td><td>11.42 (-11.39%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101769.50 (n/a)</td><td>98877.68 (n/a)</td><td>98413.70 (n/a)</td><td>97086.50 (n/a)</td><td>1854.68 (n/a)</td><td>707.82 (n/a)</td><td>695.19 (n/a)</td><td>698.27 (n/a)</td><td>675.25 (n/a)</td><td>12.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.80 (+0.70%)</td><td>0.79 (+0.95%)</td><td>0.79 (+0.20%)</td><td>0.79 (+2.53%)</td><td>0.00 <b>(-53.47%)</b></td><td>95708.40 (-2.47%)</td><td>95081.36 (-0.95%)</td><td>95200.40 (-0.20%)</td><td>94143.10 (-0.70%)</td><td>586.64 <b>(-55.06%)</b></td><td>729.95 (+0.70%)</td><td>722.77 (+0.95%)</td><td>721.84 (+0.20%)</td><td>718.01 (+2.53%)</td><td>4.48 <b>(-53.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>98129.60 (n/a)</td><td>95997.50 (n/a)</td><td>95392.00 (n/a)</td><td>94804.10 (n/a)</td><td>1305.32 (n/a)</td><td>724.86 (n/a)</td><td>715.95 (n/a)</td><td>720.39 (n/a)</td><td>700.29 (n/a)</td><td>9.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.11 <b>(-27.00%)</b></td><td>3.64 (-9.74%)</td><td>3.63 (-11.24%)</td><td>2.74 <b>(+24.50%)</b></td><td>0.55 <b>(-54.56%)</b></td><td>3251.80 (-19.68%)</td><td>2504.40 (+3.07%)</td><td>2454.40 (+12.66%)</td><td>2167.60 <b>(+36.99%)</b></td><td>441.27 <b>(-53.09%)</b></td><td>247.68 <b>(-27.00%)</b></td><td>219.04 (-9.74%)</td><td>218.74 (-11.24%)</td><td>165.10 <b>(+24.50%)</b></td><td>33.35 <b>(-54.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.63 (n/a)</td><td>4.03 (n/a)</td><td>4.09 (n/a)</td><td>2.20 (n/a)</td><td>1.22 (n/a)</td><td>4048.60 (n/a)</td><td>2429.78 (n/a)</td><td>2178.50 (n/a)</td><td>1582.30 (n/a)</td><td>940.70 (n/a)</td><td>339.30 (n/a)</td><td>242.67 (n/a)</td><td>246.44 (n/a)</td><td>132.61 (n/a)</td><td>73.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.77 (-1.40%)</td><td>3.49 (-5.34%)</td><td>3.78 (-18.67%)</td><td>2.20 (+6.04%)</td><td>1.20 (-18.44%)</td><td>4059.60 (-5.70%)</td><td>2840.62 (+0.15%)</td><td>2354.90 <b>(+22.95%)</b></td><td>1868.90 (+1.42%)</td><td>1059.24 (-19.73%)</td><td>287.26 (-1.40%)</td><td>210.32 (-5.34%)</td><td>227.98 (-18.67%)</td><td>132.25 (+6.04%)</td><td>72.15 (-18.44%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.84 (n/a)</td><td>3.69 (n/a)</td><td>4.65 (n/a)</td><td>2.07 (n/a)</td><td>1.47 (n/a)</td><td>4304.90 (n/a)</td><td>2836.40 (n/a)</td><td>1915.30 (n/a)</td><td>1842.80 (n/a)</td><td>1319.65 (n/a)</td><td>291.34 (n/a)</td><td>222.19 (n/a)</td><td>280.30 (n/a)</td><td>124.71 (n/a)</td><td>88.46 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.61 (+5.56%)</td><td>4.48 <b>(+22.50%)</b></td><td>5.25 <b>(+34.86%)</b></td><td>2.18 (+18.83%)</td><td>1.41 (+10.80%)</td><td>4084.60 (-15.85%)</td><td>2251.52 (-18.59%)</td><td>1697.30 <b>(-25.85%)</b></td><td>1588.70 (-5.27%)</td><td>1051.95 (-14.73%)</td><td>337.94 (+5.56%)</td><td>269.56 <b>(+22.50%)</b></td><td>316.30 <b>(+34.86%)</b></td><td>131.44 (+18.83%)</td><td>85.03 (+10.80%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.31 (n/a)</td><td>3.65 (n/a)</td><td>3.89 (n/a)</td><td>1.84 (n/a)</td><td>1.27 (n/a)</td><td>4853.80 (n/a)</td><td>2765.62 (n/a)</td><td>2289.10 (n/a)</td><td>1677.00 (n/a)</td><td>1233.63 (n/a)</td><td>320.13 (n/a)</td><td>220.05 (n/a)</td><td>234.54 (n/a)</td><td>110.61 (n/a)</td><td>76.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>6.52 (-1.81%)</td><td>5.45 (+7.15%)</td><td>5.40 (+12.19%)</td><td>3.95 (+3.37%)</td><td>1.10 (-7.84%)</td><td>8822.80 (-3.26%)</td><td>6624.28 (-7.40%)</td><td>6452.00 (-10.86%)</td><td>5349.80 (+1.84%)</td><td>1445.09 (-11.25%)</td><td>401.41 (-1.81%)</td><td>335.85 (+7.15%)</td><td>332.84 (+12.19%)</td><td>243.40 (+3.37%)</td><td>67.62 (-7.84%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.64 (n/a)</td><td>5.09 (n/a)</td><td>4.82 (n/a)</td><td>3.82 (n/a)</td><td>1.19 (n/a)</td><td>9119.70 (n/a)</td><td>7153.54 (n/a)</td><td>7238.30 (n/a)</td><td>5253.10 (n/a)</td><td>1628.19 (n/a)</td><td>408.81 (n/a)</td><td>313.43 (n/a)</td><td>296.68 (n/a)</td><td>235.48 (n/a)</td><td>73.37 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.58 (-8.17%)</td><td>5.04 (-1.95%)</td><td>5.22 (+0.12%)</td><td>3.82 (+2.06%)</td><td>0.70 <b>(-26.33%)</b></td><td>9137.50 (-2.02%)</td><td>7052.52 (+0.76%)</td><td>6683.00 (-0.12%)</td><td>6245.90 (+8.90%)</td><td>1179.52 (-18.81%)</td><td>343.82 (-8.17%)</td><td>310.25 (-1.95%)</td><td>321.34 (+0.12%)</td><td>235.02 (+2.06%)</td><td>43.07 <b>(-26.33%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.08 (n/a)</td><td>5.14 (n/a)</td><td>5.21 (n/a)</td><td>3.74 (n/a)</td><td>0.95 (n/a)</td><td>9325.70 (n/a)</td><td>6999.16 (n/a)</td><td>6690.80 (n/a)</td><td>5735.50 (n/a)</td><td>1452.76 (n/a)</td><td>374.42 (n/a)</td><td>316.43 (n/a)</td><td>320.96 (n/a)</td><td>230.28 (n/a)</td><td>58.46 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>6.39 (+9.12%)</td><td>5.55 (+5.24%)</td><td>5.48 (+0.61%)</td><td>5.15 (+11.32%)</td><td>0.51 (+7.05%)</td><td>6773.50 (-10.17%)</td><td>6318.76 (-5.02%)</td><td>6366.90 (-0.60%)</td><td>5453.10 (-8.35%)</td><td>537.40 (-12.58%)</td><td>393.81 (+9.12%)</td><td>341.98 (+5.24%)</td><td>337.29 (+0.61%)</td><td>317.04 (+11.32%)</td><td>31.29 (+7.05%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.86 (n/a)</td><td>5.28 (n/a)</td><td>5.44 (n/a)</td><td>4.62 (n/a)</td><td>0.47 (n/a)</td><td>7540.50 (n/a)</td><td>6652.48 (n/a)</td><td>6405.50 (n/a)</td><td>5950.20 (n/a)</td><td>614.71 (n/a)</td><td>360.91 (n/a)</td><td>324.96 (n/a)</td><td>335.26 (n/a)</td><td>284.80 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.78 (-2.28%)</td><td>0.76 (-1.27%)</td><td>0.76 (-1.71%)</td><td>0.74 (-1.08%)</td><td>0.01 <b>(-23.40%)</b></td><td>102639.10 (+1.10%)</td><td>99341.16 (+1.27%)</td><td>99029.40 (+1.74%)</td><td>97381.20 (+2.33%)</td><td>1968.20 <b>(-20.52%)</b></td><td>705.67 (-2.28%)</td><td>691.97 (-1.27%)</td><td>693.93 (-1.71%)</td><td>669.53 (-1.08%)</td><td>13.47 <b>(-23.40%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101526.30 (n/a)</td><td>98098.44 (n/a)</td><td>97332.20 (n/a)</td><td>95164.60 (n/a)</td><td>2476.47 (n/a)</td><td>722.11 (n/a)</td><td>700.87 (n/a)</td><td>706.03 (n/a)</td><td>676.86 (n/a)</td><td>17.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.77 (-0.31%)</td><td>0.77 (+2.45%)</td><td>0.77 (+2.87%)</td><td>0.76 (+5.64%)</td><td>0.00 <b>(-84.36%)</b></td><td>98891.10 (-5.34%)</td><td>98383.70 (-2.44%)</td><td>98306.90 (-2.79%)</td><td>98043.70 (+0.31%)</td><td>367.83 <b>(-85.17%)</b></td><td>700.91 (-0.31%)</td><td>698.49 (+2.45%)</td><td>699.03 (+2.87%)</td><td>694.90 (+5.64%)</td><td>2.61 <b>(-84.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>104466.10 (n/a)</td><td>100839.40 (n/a)</td><td>101131.90 (n/a)</td><td>97743.10 (n/a)</td><td>2480.29 (n/a)</td><td>703.06 (n/a)</td><td>681.80 (n/a)</td><td>679.50 (n/a)</td><td>657.82 (n/a)</td><td>16.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.81 (+0.13%)</td><td>0.80 (+0.25%)</td><td>0.80 (+0.25%)</td><td>0.80 (+0.23%)</td><td>0.00 (-16.41%)</td><td>94533.80 (-0.23%)</td><td>93837.96 (-0.25%)</td><td>93854.20 (-0.25%)</td><td>93287.70 (-0.13%)</td><td>516.06 (-16.73%)</td><td>736.64 (+0.13%)</td><td>732.34 (+0.25%)</td><td>732.19 (+0.25%)</td><td>726.93 (+0.23%)</td><td>4.02 (-16.41%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94754.00 (n/a)</td><td>94072.42 (n/a)</td><td>94091.30 (n/a)</td><td>93404.60 (n/a)</td><td>619.76 (n/a)</td><td>735.72 (n/a)</td><td>730.52 (n/a)</td><td>730.35 (n/a)</td><td>725.24 (n/a)</td><td>4.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.00 <b>(+111.32%)</b></td><td>2.56 <b>(+58.36%)</b></td><td>1.89 <b>(+24.98%)</b></td><td>1.53 (+5.76%)</td><td>1.13 <b>(+505.53%)</b></td><td>5253.00 (-5.45%)</td><td>3650.26 <b>(-27.67%)</b></td><td>4270.00 (-19.99%)</td><td>2013.60 <b>(-52.68%)</b></td><td>1424.00 <b>(+161.00%)</b></td><td>1049.83 <b>(+111.32%)</b></td><td>670.05 <b>(+58.36%)</b></td><td>495.07 <b>(+24.98%)</b></td><td>402.43 (+5.76%)</td><td>295.47 <b>(+505.53%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.89 (n/a)</td><td>1.61 (n/a)</td><td>1.51 (n/a)</td><td>1.45 (n/a)</td><td>0.19 (n/a)</td><td>5555.50 (n/a)</td><td>5046.36 (n/a)</td><td>5336.70 (n/a)</td><td>4255.10 (n/a)</td><td>545.59 (n/a)</td><td>496.80 (n/a)</td><td>423.11 (n/a)</td><td>396.11 (n/a)</td><td>380.51 (n/a)</td><td>48.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.22 (-8.83%)</td><td>0.19 (-6.67%)</td><td>0.19 (-5.56%)</td><td>0.14 (-2.20%)</td><td>0.03 (-17.99%)</td><td>9059.20 (+2.25%)</td><td>6856.64 (+6.27%)</td><td>6657.20 (+5.88%)</td><td>5672.70 (+9.69%)</td><td>1318.84 (-8.27%)</td><td>11.83 (-8.83%)</td><td>10.04 (-6.67%)</td><td>10.08 (-5.56%)</td><td>7.41 (-2.20%)</td><td>1.68 (-17.99%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>8860.00 (n/a)</td><td>6452.14 (n/a)</td><td>6287.20 (n/a)</td><td>5171.70 (n/a)</td><td>1437.74 (n/a)</td><td>12.98 (n/a)</td><td>10.76 (n/a)</td><td>10.67 (n/a)</td><td>7.57 (n/a)</td><td>2.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.96 (n/a)</td><td>3.72 (n/a)</td><td>3.72 (n/a)</td><td>3.48 (n/a)</td><td>0.21 (n/a)</td><td>3.96 (n/a)</td><td>3.72 (n/a)</td><td>3.71 (n/a)</td><td>3.48 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>7.00 (-2.69%)</td><td>6.09 (-1.66%)</td><td>5.83 (+0.86%)</td><td>5.55 (-2.57%)</td><td>0.60 (-10.68%)</td><td>6.99 (-2.69%)</td><td>6.09 (-1.66%)</td><td>5.83 (+0.86%)</td><td>5.54 (-2.57%)</td><td>0.60 (-10.68%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>7.19 (n/a)</td><td>6.20 (n/a)</td><td>5.78 (n/a)</td><td>5.69 (n/a)</td><td>0.67 (n/a)</td><td>7.19 (n/a)</td><td>6.19 (n/a)</td><td>5.78 (n/a)</td><td>5.69 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>14.17 (+1.71%)</td><td>9.96 (+4.52%)</td><td>8.36 (-0.90%)</td><td>7.44 (+0.94%)</td><td>3.04 (+16.07%)</td><td>14.16 (+1.71%)</td><td>9.95 (+4.52%)</td><td>8.35 (-0.90%)</td><td>7.43 (+0.94%)</td><td>3.04 (+16.07%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>13.93 (n/a)</td><td>9.53 (n/a)</td><td>8.43 (n/a)</td><td>7.37 (n/a)</td><td>2.62 (n/a)</td><td>13.92 (n/a)</td><td>9.52 (n/a)</td><td>8.43 (n/a)</td><td>7.36 (n/a)</td><td>2.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.82 (n/a)</td><td>3.62 (n/a)</td><td>3.59 (n/a)</td><td>3.51 (n/a)</td><td>0.12 (n/a)</td><td>3.82 (n/a)</td><td>3.62 (n/a)</td><td>3.59 (n/a)</td><td>3.51 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>7.04 (+8.18%)</td><td>6.58 (+10.92%)</td><td>6.93 (+17.79%)</td><td>5.93 (+8.31%)</td><td>0.57 <b>(+45.46%)</b></td><td>7.04 (+8.18%)</td><td>6.58 (+10.92%)</td><td>6.93 (+17.79%)</td><td>5.93 (+8.31%)</td><td>0.57 <b>(+45.46%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.51 (n/a)</td><td>5.93 (n/a)</td><td>5.88 (n/a)</td><td>5.47 (n/a)</td><td>0.39 (n/a)</td><td>6.51 (n/a)</td><td>5.93 (n/a)</td><td>5.88 (n/a)</td><td>5.47 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.55 (-13.87%)</td><td>8.01 (-10.41%)</td><td>8.02 (-6.29%)</td><td>7.36 (-9.13%)</td><td>0.47 <b>(-48.45%)</b></td><td>8.54 (-13.87%)</td><td>8.01 (-10.41%)</td><td>8.02 (-6.29%)</td><td>7.35 (-9.13%)</td><td>0.47 <b>(-48.45%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>9.93 (n/a)</td><td>8.94 (n/a)</td><td>8.56 (n/a)</td><td>8.10 (n/a)</td><td>0.91 (n/a)</td><td>9.92 (n/a)</td><td>8.94 (n/a)</td><td>8.56 (n/a)</td><td>8.09 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.21 (+4.22%)</td><td>2.19 (+1.20%)</td><td>2.71 (+0.07%)</td><td>1.03 (+0.02%)</td><td>1.07 (+12.19%)</td><td>3.20 (+4.22%)</td><td>2.18 (+1.20%)</td><td>2.71 (+0.07%)</td><td>1.03 (+0.02%)</td><td>1.06 (+12.19%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>3.08 (n/a)</td><td>2.16 (n/a)</td><td>2.71 (n/a)</td><td>1.03 (n/a)</td><td>0.95 (n/a)</td><td>3.07 (n/a)</td><td>2.16 (n/a)</td><td>2.71 (n/a)</td><td>1.03 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.51 (+1.77%)</td><td>0.42 <b>(+27.39%)</b></td><td>0.49 <b>(+21.42%)</b></td><td>0.27 <b>(+258.16%)</b></td><td>0.11 <b>(-34.84%)</b></td><td>0.50 (+1.77%)</td><td>0.41 <b>(+27.39%)</b></td><td>0.48 <b>(+21.42%)</b></td><td>0.27 <b>(+258.16%)</b></td><td>0.11 <b>(-34.84%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.40 (n/a)</td><td>0.08 (n/a)</td><td>0.17 (n/a)</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.74 (+8.88%)</td><td>0.47 (+0.76%)</td><td>0.44 <b>(-30.51%)</b></td><td>0.08 (-1.74%)</td><td>0.26 (-5.94%)</td><td>0.73 (+8.88%)</td><td>0.46 (+0.76%)</td><td>0.43 <b>(-30.51%)</b></td><td>0.08 (-1.74%)</td><td>0.25 (-5.94%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.68 (n/a)</td><td>0.46 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td><td>0.67 (n/a)</td><td>0.46 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.37 (-8.53%)</td><td>1.90 <b>(+79.24%)</b></td><td>1.93 <b>(+148.82%)</b></td><td>1.50 <b>(+236.14%)</b></td><td>0.35 <b>(-59.68%)</b></td><td>2.33 (-8.53%)</td><td>1.87 <b>(+79.24%)</b></td><td>1.90 <b>(+148.82%)</b></td><td>1.47 <b>(+236.14%)</b></td><td>0.34 <b>(-59.68%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.59 (n/a)</td><td>1.06 (n/a)</td><td>0.78 (n/a)</td><td>0.45 (n/a)</td><td>0.87 (n/a)</td><td>2.55 (n/a)</td><td>1.04 (n/a)</td><td>0.76 (n/a)</td><td>0.44 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.10 (n/a)</td><td>360.60 (n/a)</td><td>288.00 (n/a)</td><td>198.60 (n/a)</td><td>162.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.70 (n/a)</td><td>422.54 (n/a)</td><td>433.90 (n/a)</td><td>242.00 (n/a)</td><td>178.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1912.60 (n/a)</td><td>890.56 (n/a)</td><td>585.30 (n/a)</td><td>411.10 (n/a)</td><td>617.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.40 (n/a)</td><td>408.62 (n/a)</td><td>429.50 (n/a)</td><td>277.20 (n/a)</td><td>124.29 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.70 (n/a)</td><td>382.84 (n/a)</td><td>378.30 (n/a)</td><td>251.00 (n/a)</td><td>126.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.00 (n/a)</td><td>462.92 (n/a)</td><td>496.30 (n/a)</td><td>289.90 (n/a)</td><td>103.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.50 (n/a)</td><td>346.62 (n/a)</td><td>375.70 (n/a)</td><td>240.40 (n/a)</td><td>98.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>338.90 (n/a)</td><td>262.12 (n/a)</td><td>270.70 (n/a)</td><td>171.90 (n/a)</td><td>60.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1000.30 (n/a)</td><td>453.24 (n/a)</td><td>303.10 (n/a)</td><td>253.30 (n/a)</td><td>316.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.80 (n/a)</td><td>303.84 (n/a)</td><td>258.70 (n/a)</td><td>244.30 (n/a)</td><td>114.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>543.40 (n/a)</td><td>422.44 (n/a)</td><td>393.50 (n/a)</td><td>327.00 (n/a)</td><td>83.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.40 (n/a)</td><td>488.72 (n/a)</td><td>513.90 (n/a)</td><td>273.70 (n/a)</td><td>141.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>578.70 (n/a)</td><td>428.58 (n/a)</td><td>460.60 (n/a)</td><td>244.30 (n/a)</td><td>134.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>531.90 (n/a)</td><td>360.82 (n/a)</td><td>306.50 (n/a)</td><td>215.10 (n/a)</td><td>131.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1884.60 (n/a)</td><td>657.02 (n/a)</td><td>287.90 (n/a)</td><td>237.90 (n/a)</td><td>703.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>516.70 (n/a)</td><td>385.50 (n/a)</td><td>408.70 (n/a)</td><td>226.70 (n/a)</td><td>120.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.20 (n/a)</td><td>369.04 (n/a)</td><td>276.80 (n/a)</td><td>237.60 (n/a)</td><td>149.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>680.70 (n/a)</td><td>472.78 (n/a)</td><td>455.00 (n/a)</td><td>277.00 (n/a)</td><td>144.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>644.80 (n/a)</td><td>355.86 (n/a)</td><td>281.70 (n/a)</td><td>271.70 (n/a)</td><td>161.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>433.40 (n/a)</td><td>338.02 (n/a)</td><td>319.30 (n/a)</td><td>269.10 (n/a)</td><td>64.08 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1036.10 (n/a)</td><td>455.94 (n/a)</td><td>301.80 (n/a)</td><td>203.40 (n/a)</td><td>341.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>546.80 (n/a)</td><td>424.00 (n/a)</td><td>439.70 (n/a)</td><td>255.30 (n/a)</td><td>126.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>496.90 (n/a)</td><td>360.36 (n/a)</td><td>372.60 (n/a)</td><td>239.30 (n/a)</td><td>100.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>699.90 (n/a)</td><td>453.80 (n/a)</td><td>389.60 (n/a)</td><td>305.40 (n/a)</td><td>163.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+29.26%)</b></td><td>0.01 <b>(+28.27%)</b></td><td>0.01 (+6.86%)</td><td>0.01 <b>(+295.46%)</b></td><td>0.01 (-0.09%)</td><td>472.70 <b>(-74.72%)</b></td><td>343.64 <b>(-47.65%)</b></td><td>381.60 (-6.42%)</td><td>178.20 <b>(-22.62%)</b></td><td>131.21 <b>(-80.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1869.50 (n/a)</td><td>656.46 (n/a)</td><td>407.80 (n/a)</td><td>230.30 (n/a)</td><td>687.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+78.03%)</b></td><td>0.01 <b>(+79.11%)</b></td><td>0.02 <b>(+125.87%)</b></td><td>0.01 (+9.05%)</td><td>0.01 <b>(+186.74%)</b></td><td>557.50 (-8.31%)</td><td>322.78 <b>(-38.50%)</b></td><td>246.90 <b>(-55.72%)</b></td><td>208.60 <b>(-43.83%)</b></td><td>144.13 <b>(+52.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.00 (n/a)</td><td>524.84 (n/a)</td><td>557.60 (n/a)</td><td>371.40 (n/a)</td><td>94.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+21.17%)</b></td><td>0.01 <b>(+34.78%)</b></td><td>0.01 <b>(+55.30%)</b></td><td>0.01 (+4.19%)</td><td>0.01 <b>(+46.31%)</b></td><td>607.20 (-4.03%)</td><td>371.40 <b>(-21.26%)</b></td><td>304.50 <b>(-35.61%)</b></td><td>222.70 (-17.49%)</td><td>165.73 (+17.09%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>632.70 (n/a)</td><td>471.70 (n/a)</td><td>472.90 (n/a)</td><td>269.90 (n/a)</td><td>141.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 <b>(-29.28%)</b></td><td>0.01 (+11.15%)</td><td>0.01 <b>(+25.79%)</b></td><td>0.01 <b>(+48.30%)</b></td><td>0.00 <b>(-50.33%)</b></td><td>537.40 <b>(-32.57%)</b></td><td>405.08 <b>(-22.05%)</b></td><td>424.30 <b>(-20.51%)</b></td><td>289.60 <b>(+41.41%)</b></td><td>107.11 <b>(-49.09%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>797.00 (n/a)</td><td>519.68 (n/a)</td><td>533.80 (n/a)</td><td>204.80 (n/a)</td><td>210.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (-16.10%)</td><td>0.01 (+12.20%)</td><td>0.01 (+15.10%)</td><td>0.01 <b>(+358.92%)</b></td><td>0.00 <b>(-58.79%)</b></td><td>440.60 <b>(-78.21%)</b></td><td>368.00 <b>(-47.31%)</b></td><td>379.80 (-13.11%)</td><td>277.70 (+19.18%)</td><td>75.75 <b>(-89.88%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2021.80 (n/a)</td><td>698.46 (n/a)</td><td>437.10 (n/a)</td><td>233.00 (n/a)</td><td>748.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+55.72%)</b></td><td>0.01 <b>(+37.85%)</b></td><td>0.01 <b>(+29.00%)</b></td><td>0.01 <b>(+50.64%)</b></td><td>0.00 <b>(+82.81%)</b></td><td>391.00 <b>(-33.62%)</b></td><td>335.22 <b>(-26.91%)</b></td><td>343.40 <b>(-22.47%)</b></td><td>241.00 <b>(-35.78%)</b></td><td>58.44 <b>(-26.03%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.00 (n/a)</td><td>458.64 (n/a)</td><td>442.90 (n/a)</td><td>375.30 (n/a)</td><td>79.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(+50.74%)</b></td><td>0.03 (+14.53%)</td><td>0.03 (+4.28%)</td><td>0.02 <b>(+30.08%)</b></td><td>0.01 <b>(+64.24%)</b></td><td>395.90 <b>(-23.13%)</b></td><td>298.30 (-11.13%)</td><td>281.10 (-4.09%)</td><td>189.50 <b>(-33.67%)</b></td><td>84.47 (-15.82%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.00 (n/a)</td><td>335.64 (n/a)</td><td>293.10 (n/a)</td><td>285.70 (n/a)</td><td>100.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (+19.99%)</td><td>0.03 <b>(+66.21%)</b></td><td>0.03 <b>(+93.59%)</b></td><td>0.02 <b>(+378.48%)</b></td><td>0.01 <b>(-28.14%)</b></td><td>397.80 <b>(-79.10%)</b></td><td>272.60 <b>(-60.36%)</b></td><td>241.60 <b>(-48.34%)</b></td><td>216.70 (-16.69%)</td><td>75.84 <b>(-88.94%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1903.50 (n/a)</td><td>687.70 (n/a)</td><td>467.70 (n/a)</td><td>260.10 (n/a)</td><td>685.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (-0.70%)</td><td>0.02 (+4.12%)</td><td>0.03 (+18.56%)</td><td>0.01 <b>(-34.03%)</b></td><td>0.01 <b>(+34.51%)</b></td><td>782.00 <b>(+51.58%)</b></td><td>407.96 (+7.41%)</td><td>271.30 (-15.64%)</td><td>245.90 (+0.70%)</td><td>228.51 <b>(+88.65%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.90 (n/a)</td><td>379.80 (n/a)</td><td>321.60 (n/a)</td><td>244.20 (n/a)</td><td>121.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(+41.50%)</b></td><td>0.02 (+5.61%)</td><td>0.02 <b>(-26.05%)</b></td><td>0.01 (-8.40%)</td><td>0.01 <b>(+82.77%)</b></td><td>644.10 (+9.17%)</td><td>397.72 (+5.79%)</td><td>398.20 <b>(+35.21%)</b></td><td>199.20 <b>(-29.34%)</b></td><td>185.69 <b>(+39.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.00 (n/a)</td><td>375.94 (n/a)</td><td>294.50 (n/a)</td><td>281.90 (n/a)</td><td>132.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (+11.77%)</td><td>0.03 <b>(+25.24%)</b></td><td>0.03 <b>(+50.89%)</b></td><td>0.01 (-7.92%)</td><td>0.01 <b>(+49.33%)</b></td><td>572.00 (+8.60%)</td><td>357.02 (-16.11%)</td><td>287.40 <b>(-33.73%)</b></td><td>256.50 (-10.53%)</td><td>134.35 <b>(+45.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.70 (n/a)</td><td>425.56 (n/a)</td><td>433.70 (n/a)</td><td>286.70 (n/a)</td><td>92.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (+3.10%)</td><td>0.02 (+3.17%)</td><td>0.02 <b>(+31.92%)</b></td><td>0.01 (-8.50%)</td><td>0.01 (-0.27%)</td><td>624.10 (+9.28%)</td><td>396.26 (-1.91%)</td><td>334.10 <b>(-24.21%)</b></td><td>240.80 (-2.98%)</td><td>163.25 (+12.63%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.10 (n/a)</td><td>403.98 (n/a)</td><td>440.80 (n/a)</td><td>248.20 (n/a)</td><td>144.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (+13.89%)</td><td>0.02 (+0.07%)</td><td>0.02 (-17.10%)</td><td>0.01 (+5.36%)</td><td>0.01 (+19.22%)</td><td>620.10 (-5.08%)</td><td>456.98 (+1.62%)</td><td>523.60 <b>(+20.62%)</b></td><td>231.70 (-12.17%)</td><td>158.65 (-2.53%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.30 (n/a)</td><td>449.68 (n/a)</td><td>434.10 (n/a)</td><td>263.80 (n/a)</td><td>162.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-11.76%)</td><td>0.02 (-13.21%)</td><td>0.02 (-0.79%)</td><td>0.01 <b>(-24.10%)</b></td><td>0.00 (+8.56%)</td><td>663.90 <b>(+31.75%)</b></td><td>476.82 (+17.69%)</td><td>414.80 (+0.80%)</td><td>362.20 (+13.33%)</td><td>123.78 <b>(+65.78%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>503.90 (n/a)</td><td>405.16 (n/a)</td><td>411.50 (n/a)</td><td>319.60 (n/a)</td><td>74.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (+7.66%)</td><td>0.06 <b>(+28.99%)</b></td><td>0.06 <b>(+64.83%)</b></td><td>0.04 (+15.83%)</td><td>0.01 (-14.82%)</td><td>438.20 (-13.66%)</td><td>295.06 <b>(-25.12%)</b></td><td>273.10 <b>(-39.32%)</b></td><td>228.80 (-7.14%)</td><td>83.87 <b>(-30.04%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>507.50 (n/a)</td><td>394.04 (n/a)</td><td>450.10 (n/a)</td><td>246.40 (n/a)</td><td>119.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(+30.72%)</b></td><td>0.04 <b>(+30.35%)</b></td><td>0.03 (+18.73%)</td><td>0.01 <b>(-23.33%)</b></td><td>0.03 <b>(+59.90%)</b></td><td>2488.60 <b>(+30.44%)</b></td><td>793.40 (+5.52%)</td><td>478.10 (-15.78%)</td><td>238.10 <b>(-23.49%)</b></td><td>956.32 <b>(+45.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1907.90 (n/a)</td><td>751.88 (n/a)</td><td>567.70 (n/a)</td><td>311.20 (n/a)</td><td>655.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (-7.80%)</td><td>0.05 (-6.72%)</td><td>0.05 (-6.88%)</td><td>0.03 (-4.29%)</td><td>0.02 (-5.72%)</td><td>600.00 (+4.48%)</td><td>395.90 (+7.55%)</td><td>308.10 (+7.39%)</td><td>243.00 (+8.43%)</td><td>161.34 (+8.18%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.30 (n/a)</td><td>368.10 (n/a)</td><td>286.90 (n/a)</td><td>224.10 (n/a)</td><td>149.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(+34.35%)</b></td><td>0.04 <b>(+28.68%)</b></td><td>0.03 (+15.87%)</td><td>0.02 (-2.41%)</td><td>0.02 <b>(+67.20%)</b></td><td>797.30 (+2.47%)</td><td>467.24 (-15.80%)</td><td>471.20 (-13.68%)</td><td>247.40 <b>(-25.57%)</b></td><td>210.34 <b>(+32.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>778.10 (n/a)</td><td>554.94 (n/a)</td><td>545.90 (n/a)</td><td>332.40 (n/a)</td><td>158.61 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (+11.12%)</td><td>0.05 <b>(+28.68%)</b></td><td>0.05 <b>(+57.63%)</b></td><td>0.03 (+5.08%)</td><td>0.01 (+15.25%)</td><td>542.80 (-4.84%)</td><td>364.86 <b>(-21.14%)</b></td><td>307.50 <b>(-36.57%)</b></td><td>243.20 (-10.03%)</td><td>122.22 (+7.25%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>570.40 (n/a)</td><td>462.68 (n/a)</td><td>484.80 (n/a)</td><td>270.30 (n/a)</td><td>113.96 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (+15.22%)</td><td>0.04 (+8.38%)</td><td>0.03 (-10.31%)</td><td>0.03 (+4.81%)</td><td>0.01 <b>(+46.02%)</b></td><td>600.90 (-4.59%)</td><td>479.66 (-3.15%)</td><td>566.40 (+11.50%)</td><td>274.10 (-13.20%)</td><td>152.49 <b>(+33.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>629.80 (n/a)</td><td>495.26 (n/a)</td><td>508.00 (n/a)</td><td>315.80 (n/a)</td><td>114.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 <b>(+31.16%)</b></td><td>0.12 <b>(+44.19%)</b></td><td>0.14 <b>(+87.44%)</b></td><td>0.05 (-14.01%)</td><td>0.04 <b>(+88.99%)</b></td><td>610.20 (+16.30%)</td><td>314.24 <b>(-23.21%)</b></td><td>232.40 <b>(-46.65%)</b></td><td>217.60 <b>(-23.76%)</b></td><td>167.76 <b>(+74.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>524.70 (n/a)</td><td>409.22 (n/a)</td><td>435.60 (n/a)</td><td>285.40 (n/a)</td><td>96.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 <b>(+24.59%)</b></td><td>0.12 <b>(+63.44%)</b></td><td>0.12 <b>(+78.03%)</b></td><td>0.09 <b>(+81.32%)</b></td><td>0.02 (-19.35%)</td><td>366.60 <b>(-44.85%)</b></td><td>288.32 <b>(-41.46%)</b></td><td>276.50 <b>(-43.82%)</b></td><td>250.60 (-19.73%)</td><td>47.80 <b>(-63.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>664.70 (n/a)</td><td>492.54 (n/a)</td><td>492.20 (n/a)</td><td>312.20 (n/a)</td><td>131.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (-11.58%)</td><td>0.08 <b>(-24.58%)</b></td><td>0.07 <b>(-41.58%)</b></td><td>0.06 (-15.58%)</td><td>0.03 (-19.00%)</td><td>580.90 (+18.45%)</td><td>428.94 <b>(+29.97%)</b></td><td>443.30 <b>(+71.16%)</b></td><td>242.50 (+13.11%)</td><td>131.91 (+3.06%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>490.40 (n/a)</td><td>330.04 (n/a)</td><td>259.00 (n/a)</td><td>214.40 (n/a)</td><td>128.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (-1.40%)</td><td>0.11 (+10.23%)</td><td>0.13 <b>(+29.02%)</b></td><td>0.06 <b>(+24.36%)</b></td><td>0.04 (+3.19%)</td><td>564.70 (-19.58%)</td><td>338.66 (-11.51%)</td><td>259.30 <b>(-22.50%)</b></td><td>239.50 (+1.44%)</td><td>140.49 <b>(-23.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>702.20 (n/a)</td><td>382.70 (n/a)</td><td>334.60 (n/a)</td><td>236.10 (n/a)</td><td>184.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (-17.88%)</td><td>0.07 <b>(-20.63%)</b></td><td>0.07 <b>(-28.05%)</b></td><td>0.02 (-5.35%)</td><td>0.04 <b>(-27.04%)</b></td><td>1965.00 (+5.65%)</td><td>745.92 (+12.31%)</td><td>477.30 <b>(+38.99%)</b></td><td>300.20 <b>(+21.78%)</b></td><td>693.27 (+1.26%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1859.90 (n/a)</td><td>664.16 (n/a)</td><td>343.40 (n/a)</td><td>246.50 (n/a)</td><td>684.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+49.53%)</b></td><td>0.01 <b>(+31.89%)</b></td><td>0.01 <b>(+39.65%)</b></td><td>0.01 <b>(+20.41%)</b></td><td>0.00 <b>(+105.46%)</b></td><td>454.40 (-16.94%)</td><td>332.32 (-19.62%)</td><td>291.10 <b>(-28.39%)</b></td><td>198.30 <b>(-33.14%)</b></td><td>113.78 <b>(+22.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.10 (n/a)</td><td>413.44 (n/a)</td><td>406.50 (n/a)</td><td>296.60 (n/a)</td><td>92.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+22.14%)</b></td><td>0.01 (+3.34%)</td><td>0.01 (-2.35%)</td><td>0.00 <b>(-73.82%)</b></td><td>0.01 <b>(+73.63%)</b></td><td>1890.60 <b>(+281.94%)</b></td><td>596.30 <b>(+64.45%)</b></td><td>286.80 (+2.43%)</td><td>223.90 (-18.14%)</td><td>724.20 <b>(+517.08%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.00 (n/a)</td><td>362.60 (n/a)</td><td>280.00 (n/a)</td><td>273.50 (n/a)</td><td>117.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+74.16%)</b></td><td>0.01 <b>(+88.71%)</b></td><td>0.01 <b>(+89.13%)</b></td><td>0.01 <b>(+114.84%)</b></td><td>0.00 <b>(+53.67%)</b></td><td>497.90 <b>(-53.45%)</b></td><td>326.08 <b>(-49.01%)</b></td><td>296.30 <b>(-47.13%)</b></td><td>235.50 <b>(-42.57%)</b></td><td>104.73 <b>(-59.65%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1069.70 (n/a)</td><td>639.46 (n/a)</td><td>560.40 (n/a)</td><td>410.10 (n/a)</td><td>259.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+2.32%)</td><td>0.01 (-12.40%)</td><td>0.01 <b>(-33.85%)</b></td><td>0.01 <b>(+25.87%)</b></td><td>0.00 (+0.96%)</td><td>519.40 <b>(-20.56%)</b></td><td>377.24 (+10.10%)</td><td>406.00 <b>(+51.15%)</b></td><td>228.50 (-2.27%)</td><td>125.06 <b>(-28.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.80 (n/a)</td><td>342.64 (n/a)</td><td>268.60 (n/a)</td><td>233.80 (n/a)</td><td>175.06 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 <b>(-31.30%)</b></td><td>0.01 (-14.94%)</td><td>0.01 (+3.04%)</td><td>0.01 (+6.65%)</td><td>0.00 <b>(-79.01%)</b></td><td>492.20 (-6.25%)</td><td>440.74 (+8.26%)</td><td>446.40 (-2.96%)</td><td>395.20 <b>(+45.56%)</b></td><td>37.32 <b>(-70.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.00 (n/a)</td><td>407.10 (n/a)</td><td>460.00 (n/a)</td><td>271.50 (n/a)</td><td>125.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 <b>(-30.52%)</b></td><td>0.01 (+17.99%)</td><td>0.01 <b>(+43.13%)</b></td><td>0.01 <b>(+367.78%)</b></td><td>0.00 <b>(-80.84%)</b></td><td>393.50 <b>(-78.62%)</b></td><td>344.20 <b>(-49.19%)</b></td><td>345.10 <b>(-30.14%)</b></td><td>307.60 <b>(+43.94%)</b></td><td>35.93 <b>(-94.59%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1840.90 (n/a)</td><td>677.40 (n/a)</td><td>494.00 (n/a)</td><td>213.70 (n/a)</td><td>663.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-10.91%)</td><td>0.01 (+9.36%)</td><td>0.02 <b>(+70.82%)</b></td><td>0.01 (+16.18%)</td><td>0.00 (-12.23%)</td><td>515.10 (-13.92%)</td><td>343.86 (-11.17%)</td><td>251.60 <b>(-41.46%)</b></td><td>243.20 (+12.23%)</td><td>133.89 (-13.69%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.40 (n/a)</td><td>387.08 (n/a)</td><td>429.80 (n/a)</td><td>216.70 (n/a)</td><td>155.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+1.55%)</td><td>0.01 (+14.28%)</td><td>0.01 <b>(+37.14%)</b></td><td>0.01 <b>(+29.11%)</b></td><td>0.00 <b>(-23.92%)</b></td><td>612.30 <b>(-22.53%)</b></td><td>378.98 <b>(-20.87%)</b></td><td>366.80 <b>(-27.09%)</b></td><td>248.50 (-1.55%)</td><td>145.41 <b>(-36.69%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>790.40 (n/a)</td><td>478.92 (n/a)</td><td>503.10 (n/a)</td><td>252.40 (n/a)</td><td>229.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-1.47%)</td><td>0.01 (-6.60%)</td><td>0.01 (-8.28%)</td><td>0.01 (-12.62%)</td><td>0.00 (+11.07%)</td><td>597.20 (+14.43%)</td><td>416.18 (+10.99%)</td><td>459.70 (+9.04%)</td><td>243.80 (+1.50%)</td><td>153.54 <b>(+29.03%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.90 (n/a)</td><td>374.98 (n/a)</td><td>421.60 (n/a)</td><td>240.20 (n/a)</td><td>119.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-3.53%)</td><td>0.01 (-17.69%)</td><td>0.01 <b>(-29.15%)</b></td><td>0.00 <b>(+70.26%)</b></td><td>0.00 (-16.02%)</td><td>1108.50 <b>(-41.27%)</b></td><td>595.18 (-9.37%)</td><td>525.80 <b>(+41.12%)</b></td><td>248.40 (+3.67%)</td><td>317.31 <b>(-54.29%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1887.40 (n/a)</td><td>656.74 (n/a)</td><td>372.60 (n/a)</td><td>239.60 (n/a)</td><td>694.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+56.33%)</b></td><td>0.01 <b>(+31.04%)</b></td><td>0.01 (+9.99%)</td><td>0.01 <b>(+33.76%)</b></td><td>0.01 <b>(+65.52%)</b></td><td>618.60 <b>(-25.24%)</b></td><td>410.06 <b>(-20.43%)</b></td><td>476.20 (-9.07%)</td><td>171.40 <b>(-36.04%)</b></td><td>175.82 <b>(-21.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>827.50 (n/a)</td><td>515.34 (n/a)</td><td>523.70 (n/a)</td><td>268.00 (n/a)</td><td>224.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (-8.37%)</td><td>0.01 (+15.96%)</td><td>0.01 (+4.49%)</td><td>0.01 <b>(+183.20%)</b></td><td>0.00 <b>(-37.07%)</b></td><td>655.60 <b>(-64.69%)</b></td><td>457.02 <b>(-37.74%)</b></td><td>468.20 (-4.29%)</td><td>298.20 (+9.15%)</td><td>137.22 <b>(-78.53%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1856.70 (n/a)</td><td>734.08 (n/a)</td><td>489.20 (n/a)</td><td>273.20 (n/a)</td><td>639.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (+8.49%)</td><td>0.03 (-2.90%)</td><td>0.02 <b>(-27.98%)</b></td><td>0.02 (+15.42%)</td><td>0.01 <b>(+34.90%)</b></td><td>465.10 (-13.36%)</td><td>352.16 (+5.40%)</td><td>404.30 <b>(+38.84%)</b></td><td>224.10 (-7.82%)</td><td>112.93 (-2.56%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.80 (n/a)</td><td>334.12 (n/a)</td><td>291.20 (n/a)</td><td>243.10 (n/a)</td><td>115.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (+15.62%)</td><td>0.02 (-12.06%)</td><td>0.02 <b>(-36.18%)</b></td><td>0.01 (-10.96%)</td><td>0.01 <b>(+37.46%)</b></td><td>703.90 (+12.30%)</td><td>409.46 <b>(+22.85%)</b></td><td>427.40 <b>(+56.67%)</b></td><td>195.60 (-13.53%)</td><td>204.29 <b>(+22.27%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.80 (n/a)</td><td>333.30 (n/a)</td><td>272.80 (n/a)</td><td>226.20 (n/a)</td><td>167.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (-12.60%)</td><td>0.02 <b>(+29.14%)</b></td><td>0.02 <b>(+37.31%)</b></td><td>0.02 <b>(+44.84%)</b></td><td>0.01 <b>(-33.73%)</b></td><td>460.90 <b>(-30.95%)</b></td><td>362.86 <b>(-29.85%)</b></td><td>387.10 <b>(-27.18%)</b></td><td>254.60 (+14.43%)</td><td>96.58 <b>(-45.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.50 (n/a)</td><td>517.26 (n/a)</td><td>531.60 (n/a)</td><td>222.50 (n/a)</td><td>178.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 <b>(-21.49%)</b></td><td>0.03 (+0.18%)</td><td>0.03 (+13.32%)</td><td>0.02 (-10.67%)</td><td>0.01 (-16.81%)</td><td>536.60 (+11.95%)</td><td>309.48 (+0.27%)</td><td>261.30 (-11.78%)</td><td>242.60 <b>(+27.35%)</b></td><td>127.28 <b>(+20.05%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.30 (n/a)</td><td>308.66 (n/a)</td><td>296.20 (n/a)</td><td>190.50 (n/a)</td><td>106.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (-4.54%)</td><td>0.02 <b>(+26.21%)</b></td><td>0.02 <b>(+38.83%)</b></td><td>0.02 <b>(+36.48%)</b></td><td>0.01 <b>(-21.13%)</b></td><td>459.70 <b>(-26.74%)</b></td><td>363.30 <b>(-25.24%)</b></td><td>397.90 <b>(-27.97%)</b></td><td>248.20 (+4.77%)</td><td>97.12 <b>(-36.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.50 (n/a)</td><td>485.98 (n/a)</td><td>552.40 (n/a)</td><td>236.90 (n/a)</td><td>153.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 <b>(+21.85%)</b></td><td>0.02 (+12.29%)</td><td>0.02 (+17.03%)</td><td>0.02 (-2.12%)</td><td>0.01 <b>(+35.72%)</b></td><td>514.40 (+2.16%)</td><td>369.96 (-8.23%)</td><td>392.00 (-14.54%)</td><td>235.80 (-17.93%)</td><td>118.43 (+14.07%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.50 (n/a)</td><td>403.14 (n/a)</td><td>458.70 (n/a)</td><td>287.30 (n/a)</td><td>103.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (-4.59%)</td><td>0.02 <b>(-24.37%)</b></td><td>0.02 (-11.66%)</td><td>0.00 <b>(-72.68%)</b></td><td>0.01 <b>(+28.32%)</b></td><td>1958.90 <b>(+266.08%)</b></td><td>731.76 <b>(+88.07%)</b></td><td>473.50 (+13.20%)</td><td>281.90 (+4.80%)</td><td>692.25 <b>(+500.54%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.10 (n/a)</td><td>389.08 (n/a)</td><td>418.30 (n/a)</td><td>269.00 (n/a)</td><td>115.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (+9.53%)</td><td>0.02 <b>(+20.43%)</b></td><td>0.02 (+19.68%)</td><td>0.01 <b>(+205.15%)</b></td><td>0.01 (-16.36%)</td><td>615.70 <b>(-67.23%)</b></td><td>415.86 <b>(-41.55%)</b></td><td>407.00 (-16.44%)</td><td>237.20 (-8.70%)</td><td>167.25 <b>(-75.09%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1878.90 (n/a)</td><td>711.42 (n/a)</td><td>487.10 (n/a)</td><td>259.80 (n/a)</td><td>671.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(-26.67%)</b></td><td>0.01 <b>(-28.91%)</b></td><td>0.01 <b>(-23.18%)</b></td><td>0.00 <b>(-76.66%)</b></td><td>0.01 (+9.48%)</td><td>2501.40 <b>(+328.40%)</b></td><td>891.62 <b>(+107.09%)</b></td><td>564.50 <b>(+30.19%)</b></td><td>370.20 <b>(+36.35%)</b></td><td>905.66 <b>(+593.14%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.90 (n/a)</td><td>430.54 (n/a)</td><td>433.60 (n/a)</td><td>271.50 (n/a)</td><td>130.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(+28.71%)</b></td><td>0.03 <b>(+22.19%)</b></td><td>0.03 <b>(+34.34%)</b></td><td>0.02 (+9.87%)</td><td>0.01 <b>(+51.20%)</b></td><td>513.10 (-8.98%)</td><td>358.74 (-14.93%)</td><td>308.80 <b>(-25.57%)</b></td><td>213.20 <b>(-22.30%)</b></td><td>123.35 (+11.53%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.70 (n/a)</td><td>421.70 (n/a)</td><td>414.90 (n/a)</td><td>274.40 (n/a)</td><td>110.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(+70.00%)</b></td><td>0.02 (+9.30%)</td><td>0.02 (-2.81%)</td><td>0.01 <b>(-25.53%)</b></td><td>0.01 <b>(+322.17%)</b></td><td>695.40 <b>(+34.27%)</b></td><td>489.80 (+5.55%)</td><td>486.70 (+2.90%)</td><td>217.90 <b>(-41.17%)</b></td><td>176.06 <b>(+216.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>517.90 (n/a)</td><td>464.04 (n/a)</td><td>473.00 (n/a)</td><td>370.40 (n/a)</td><td>55.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (-13.98%)</td><td>0.02 (+10.05%)</td><td>0.02 <b>(+27.02%)</b></td><td>0.01 <b>(+45.98%)</b></td><td>0.01 <b>(-32.88%)</b></td><td>548.20 <b>(-31.50%)</b></td><td>416.44 (-16.74%)</td><td>394.10 <b>(-21.27%)</b></td><td>280.20 (+16.22%)</td><td>117.71 <b>(-42.54%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>800.30 (n/a)</td><td>500.18 (n/a)</td><td>500.60 (n/a)</td><td>241.10 (n/a)</td><td>204.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (-12.31%)</td><td>0.04 <b>(-29.56%)</b></td><td>0.04 <b>(-33.95%)</b></td><td>0.03 <b>(-32.79%)</b></td><td>0.01 (+5.19%)</td><td>654.10 <b>(+48.79%)</b></td><td>463.58 <b>(+46.11%)</b></td><td>466.30 <b>(+51.40%)</b></td><td>296.50 (+14.04%)</td><td>129.73 <b>(+76.58%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>439.60 (n/a)</td><td>317.28 (n/a)</td><td>308.00 (n/a)</td><td>260.00 (n/a)</td><td>73.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 <b>(-26.85%)</b></td><td>0.04 (-10.25%)</td><td>0.04 <b>(-23.09%)</b></td><td>0.04 <b>(+59.50%)</b></td><td>0.01 <b>(-69.56%)</b></td><td>449.30 <b>(-37.30%)</b></td><td>379.12 (-6.27%)</td><td>395.80 <b>(+30.03%)</b></td><td>312.20 <b>(+36.69%)</b></td><td>54.48 <b>(-73.98%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>716.60 (n/a)</td><td>404.50 (n/a)</td><td>304.40 (n/a)</td><td>228.40 (n/a)</td><td>209.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (-15.57%)</td><td>0.04 (-12.69%)</td><td>0.04 (+3.70%)</td><td>0.03 (-12.01%)</td><td>0.01 <b>(-30.68%)</b></td><td>583.60 (+13.65%)</td><td>424.24 (+10.61%)</td><td>436.10 (-3.56%)</td><td>285.60 (+18.46%)</td><td>122.15 (-4.51%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>513.50 (n/a)</td><td>383.54 (n/a)</td><td>452.20 (n/a)</td><td>241.10 (n/a)</td><td>127.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (+16.67%)</td><td>0.05 (-12.58%)</td><td>0.05 (-17.12%)</td><td>0.02 <b>(-59.03%)</b></td><td>0.02 <b>(+68.00%)</b></td><td>1039.10 <b>(+144.09%)</b></td><td>465.78 <b>(+44.96%)</b></td><td>327.00 <b>(+20.66%)</b></td><td>197.10 (-14.30%)</td><td>333.11 <b>(+259.87%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>425.70 (n/a)</td><td>321.32 (n/a)</td><td>271.00 (n/a)</td><td>230.00 (n/a)</td><td>92.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 <b>(-21.42%)</b></td><td>0.04 (-3.79%)</td><td>0.03 (-1.57%)</td><td>0.02 (-5.71%)</td><td>0.01 <b>(-30.46%)</b></td><td>700.70 (+6.05%)</td><td>485.60 (-0.10%)</td><td>488.70 (+1.58%)</td><td>292.90 <b>(+27.24%)</b></td><td>161.56 (-1.34%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>660.70 (n/a)</td><td>486.08 (n/a)</td><td>481.10 (n/a)</td><td>230.20 (n/a)</td><td>163.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 <b>(+23.60%)</b></td><td>0.05 (+9.15%)</td><td>0.06 (+3.87%)</td><td>0.03 (+5.52%)</td><td>0.02 <b>(+35.96%)</b></td><td>617.50 (-5.23%)</td><td>362.32 (-4.26%)</td><td>295.60 (-3.71%)</td><td>181.20 (-19.07%)</td><td>171.20 (+2.30%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.60 (n/a)</td><td>378.46 (n/a)</td><td>307.00 (n/a)</td><td>223.90 (n/a)</td><td>167.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(-56.71%)</b></td><td>0.03 (-16.41%)</td><td>0.03 (+0.39%)</td><td>0.03 <b>(+201.81%)</b></td><td>0.01 <b>(-82.88%)</b></td><td>636.90 <b>(-66.87%)</b></td><td>525.38 <b>(-29.03%)</b></td><td>528.50 (-0.40%)</td><td>427.00 <b>(+131.06%)</b></td><td>84.64 <b>(-87.54%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1922.40 (n/a)</td><td>740.26 (n/a)</td><td>530.60 (n/a)</td><td>184.80 (n/a)</td><td>679.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (-2.49%)</td><td>0.04 (-2.42%)</td><td>0.03 (-18.20%)</td><td>0.03 (-7.17%)</td><td>0.01 (+19.95%)</td><td>574.30 (+7.73%)</td><td>424.78 (+6.13%)</td><td>488.30 <b>(+22.23%)</b></td><td>263.50 (+2.57%)</td><td>135.26 <b>(+33.23%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.10 (n/a)</td><td>400.24 (n/a)</td><td>399.50 (n/a)</td><td>256.90 (n/a)</td><td>101.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (-14.22%)</td><td>0.03 <b>(-33.10%)</b></td><td>0.03 <b>(-42.24%)</b></td><td>0.01 <b>(-65.94%)</b></td><td>0.01 (+0.35%)</td><td>2433.50 <b>(+193.65%)</b></td><td>908.96 <b>(+99.25%)</b></td><td>609.70 <b>(+73.11%)</b></td><td>363.20 (+16.56%)</td><td>859.63 <b>(+293.58%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>828.70 (n/a)</td><td>456.20 (n/a)</td><td>352.20 (n/a)</td><td>311.60 (n/a)</td><td>218.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (-17.42%)</td><td>0.04 (+7.11%)</td><td>0.04 (+9.51%)</td><td>0.03 <b>(+28.80%)</b></td><td>0.00 <b>(-57.92%)</b></td><td>516.70 <b>(-22.36%)</b></td><td>437.56 (-11.92%)</td><td>443.50 (-8.69%)</td><td>371.00 <b>(+21.12%)</b></td><td>55.23 <b>(-59.97%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.50 (n/a)</td><td>496.78 (n/a)</td><td>485.70 (n/a)</td><td>306.30 (n/a)</td><td>137.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (-18.66%)</td><td>0.04 (-2.81%)</td><td>0.05 <b>(+31.85%)</b></td><td>0.03 (+1.54%)</td><td>0.01 <b>(-34.75%)</b></td><td>646.00 (-1.52%)</td><td>431.14 (-3.46%)</td><td>357.30 <b>(-24.16%)</b></td><td>308.40 <b>(+22.92%)</b></td><td>143.20 (-18.80%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>656.00 (n/a)</td><td>446.58 (n/a)</td><td>471.10 (n/a)</td><td>250.90 (n/a)</td><td>176.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(+25.98%)</b></td><td>0.03 (-6.91%)</td><td>0.03 (+14.42%)</td><td>0.01 <b>(-66.42%)</b></td><td>0.02 <b>(+58.66%)</b></td><td>2038.60 <b>(+197.82%)</b></td><td>784.02 <b>(+55.46%)</b></td><td>507.30 (-12.59%)</td><td>236.50 <b>(-20.61%)</b></td><td>718.32 <b>(+314.20%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>684.50 (n/a)</td><td>504.32 (n/a)</td><td>580.40 (n/a)</td><td>297.90 (n/a)</td><td>173.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (-3.10%)</td><td>0.08 (-12.04%)</td><td>0.07 <b>(-32.84%)</b></td><td>0.06 (+3.97%)</td><td>0.03 (-12.87%)</td><td>537.60 (-3.83%)</td><td>420.64 (+8.97%)</td><td>455.90 <b>(+48.89%)</b></td><td>232.40 (+3.20%)</td><td>115.06 <b>(-25.29%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>559.00 (n/a)</td><td>386.00 (n/a)</td><td>306.20 (n/a)</td><td>225.20 (n/a)</td><td>154.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (+4.34%)</td><td>0.10 (-4.18%)</td><td>0.12 (+5.58%)</td><td>0.06 (-18.47%)</td><td>0.04 <b>(+35.21%)</b></td><td>557.10 <b>(+22.66%)</b></td><td>355.70 (+10.77%)</td><td>268.40 (-5.29%)</td><td>233.70 (-4.14%)</td><td>141.40 <b>(+60.45%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>454.20 (n/a)</td><td>321.12 (n/a)</td><td>283.40 (n/a)</td><td>243.80 (n/a)</td><td>88.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (-19.24%)</td><td>0.07 (-18.12%)</td><td>0.07 (-13.98%)</td><td>0.06 (-9.68%)</td><td>0.02 <b>(-36.76%)</b></td><td>567.60 (+10.73%)</td><td>464.42 (+19.11%)</td><td>478.50 (+16.25%)</td><td>341.10 <b>(+23.86%)</b></td><td>90.09 (-11.37%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>512.60 (n/a)</td><td>389.90 (n/a)</td><td>411.60 (n/a)</td><td>275.40 (n/a)</td><td>101.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (+18.95%)</td><td>0.10 <b>(+30.63%)</b></td><td>0.07 (+11.47%)</td><td>0.06 <b>(+50.78%)</b></td><td>0.04 <b>(+34.68%)</b></td><td>540.30 <b>(-33.68%)</b></td><td>384.04 <b>(-23.03%)</b></td><td>453.10 (-10.29%)</td><td>218.90 (-15.94%)</td><td>149.08 <b>(-27.76%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>814.70 (n/a)</td><td>498.96 (n/a)</td><td>505.10 (n/a)</td><td>260.40 (n/a)</td><td>206.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.18 <b>(+56.96%)</b></td><td>0.10 <b>(+36.08%)</b></td><td>0.11 <b>(+44.11%)</b></td><td>0.05 (-3.32%)</td><td>0.05 <b>(+111.82%)</b></td><td>632.90 (+3.43%)</td><td>396.58 (-14.61%)</td><td>297.80 <b>(-30.62%)</b></td><td>177.40 <b>(-36.30%)</b></td><td>206.15 <b>(+49.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>611.90 (n/a)</td><td>464.42 (n/a)</td><td>429.20 (n/a)</td><td>278.50 (n/a)</td><td>137.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.19 <b>(+48.67%)</b></td><td>0.09 (-9.10%)</td><td>0.07 <b>(-35.33%)</b></td><td>0.06 (-17.47%)</td><td>0.06 <b>(+116.59%)</b></td><td>545.80 <b>(+21.18%)</b></td><td>426.60 <b>(+24.45%)</b></td><td>459.30 <b>(+54.65%)</b></td><td>172.30 <b>(-32.75%)</b></td><td>147.88 <b>(+59.63%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>450.40 (n/a)</td><td>342.78 (n/a)</td><td>297.00 (n/a)</td><td>256.20 (n/a)</td><td>92.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 <b>(+36.50%)</b></td><td>0.11 <b>(+48.89%)</b></td><td>0.12 <b>(+88.09%)</b></td><td>0.07 (+12.69%)</td><td>0.04 <b>(+70.78%)</b></td><td>469.60 (-11.26%)</td><td>323.24 <b>(-29.66%)</b></td><td>273.80 <b>(-46.85%)</b></td><td>213.00 <b>(-26.75%)</b></td><td>115.59 (+13.99%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>529.20 (n/a)</td><td>459.54 (n/a)</td><td>515.10 (n/a)</td><td>290.80 (n/a)</td><td>101.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 <b>(+77.83%)</b></td><td>0.10 <b>(+20.05%)</b></td><td>0.07 (-6.74%)</td><td>0.06 (-8.32%)</td><td>0.06 <b>(+195.56%)</b></td><td>567.30 (+9.08%)</td><td>405.38 (-3.12%)</td><td>444.90 (+7.20%)</td><td>159.30 <b>(-43.75%)</b></td><td>150.77 <b>(+66.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>520.10 (n/a)</td><td>418.44 (n/a)</td><td>415.00 (n/a)</td><td>283.20 (n/a)</td><td>90.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 <b>(-25.22%)</b></td><td>0.07 (-9.87%)</td><td>0.07 (-2.95%)</td><td>0.04 <b>(-20.77%)</b></td><td>0.02 <b>(-32.03%)</b></td><td>792.10 <b>(+26.21%)</b></td><td>519.02 (+9.77%)</td><td>495.50 (+3.04%)</td><td>362.90 <b>(+33.71%)</b></td><td>164.32 <b>(+26.46%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>627.60 (n/a)</td><td>472.84 (n/a)</td><td>480.90 (n/a)</td><td>271.40 (n/a)</td><td>129.94 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (-0.24%)</td><td>0.09 (-2.80%)</td><td>0.08 (-4.04%)</td><td>0.01 <b>(-76.84%)</b></td><td>0.05 <b>(+52.34%)</b></td><td>2525.10 <b>(+331.79%)</b></td><td>777.24 <b>(+88.67%)</b></td><td>397.30 (+4.20%)</td><td>242.40 (+0.25%)</td><td>981.86 <b>(+570.89%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>584.80 (n/a)</td><td>411.96 (n/a)</td><td>381.30 (n/a)</td><td>241.80 (n/a)</td><td>146.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (+0.22%)</td><td>0.08 (+2.63%)</td><td>0.07 (-8.07%)</td><td>0.05 (-10.35%)</td><td>0.03 (+8.81%)</td><td>664.50 (+11.55%)</td><td>466.44 (-0.66%)</td><td>495.70 (+8.78%)</td><td>287.30 (-0.21%)</td><td>144.80 <b>(+22.08%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>595.70 (n/a)</td><td>469.54 (n/a)</td><td>455.70 (n/a)</td><td>287.90 (n/a)</td><td>118.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (+14.17%)</td><td>0.09 <b>(+44.81%)</b></td><td>0.07 <b>(+30.92%)</b></td><td>0.07 <b>(+288.63%)</b></td><td>0.03 <b>(-24.35%)</b></td><td>487.30 <b>(-74.27%)</b></td><td>400.56 <b>(-49.84%)</b></td><td>461.80 <b>(-23.63%)</b></td><td>264.80 (-12.40%)</td><td>108.04 <b>(-83.12%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1893.90 (n/a)</td><td>798.62 (n/a)</td><td>604.70 (n/a)</td><td>302.30 (n/a)</td><td>639.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+8.70%)</td><td>0.01 (+9.38%)</td><td>0.01 (-4.36%)</td><td>0.01 (-0.15%)</td><td>0.00 <b>(+32.35%)</b></td><td>532.20 (+0.15%)</td><td>393.66 (-5.28%)</td><td>451.70 (+4.56%)</td><td>243.20 (-8.02%)</td><td>125.33 <b>(+22.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.40 (n/a)</td><td>415.62 (n/a)</td><td>432.00 (n/a)</td><td>264.40 (n/a)</td><td>102.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-4.45%)</td><td>0.02 (+8.56%)</td><td>0.02 <b>(+24.63%)</b></td><td>0.01 (+11.28%)</td><td>0.01 (-7.77%)</td><td>505.10 (-10.14%)</td><td>361.26 (-9.76%)</td><td>284.80 (-19.77%)</td><td>265.00 (+4.62%)</td><td>116.36 (-16.43%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.10 (n/a)</td><td>400.32 (n/a)</td><td>355.00 (n/a)</td><td>253.30 (n/a)</td><td>139.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+22.07%)</b></td><td>0.01 (-8.52%)</td><td>0.01 <b>(-32.87%)</b></td><td>0.00 <b>(-45.56%)</b></td><td>0.01 <b>(+49.40%)</b></td><td>1027.60 <b>(+83.70%)</b></td><td>519.60 <b>(+34.52%)</b></td><td>546.90 <b>(+48.98%)</b></td><td>196.80 (-18.10%)</td><td>326.69 <b>(+121.07%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.40 (n/a)</td><td>386.26 (n/a)</td><td>367.10 (n/a)</td><td>240.30 (n/a)</td><td>147.78 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+21.21%)</b></td><td>0.01 (-15.26%)</td><td>0.01 <b>(-33.58%)</b></td><td>0.00 <b>(-76.67%)</b></td><td>0.01 <b>(+162.87%)</b></td><td>1956.90 <b>(+328.67%)</b></td><td>672.84 <b>(+106.53%)</b></td><td>458.90 <b>(+50.56%)</b></td><td>220.30 (-17.52%)</td><td>728.64 <b>(+833.54%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.50 (n/a)</td><td>325.78 (n/a)</td><td>304.80 (n/a)</td><td>267.10 (n/a)</td><td>78.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+19.56%)</td><td>0.02 (+6.99%)</td><td>0.02 (+2.79%)</td><td>0.01 <b>(-35.56%)</b></td><td>0.01 <b>(+44.42%)</b></td><td>796.90 <b>(+55.16%)</b></td><td>343.46 (+10.95%)</td><td>244.20 (-2.75%)</td><td>183.40 (-16.37%)</td><td>256.89 <b>(+105.73%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.60 (n/a)</td><td>309.56 (n/a)</td><td>251.10 (n/a)</td><td>219.30 (n/a)</td><td>124.87 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+15.92%)</td><td>0.02 <b>(+31.87%)</b></td><td>0.02 <b>(+58.79%)</b></td><td>0.01 (+12.06%)</td><td>0.01 (+14.86%)</td><td>489.00 (-10.77%)</td><td>337.82 <b>(-23.79%)</b></td><td>294.70 <b>(-37.02%)</b></td><td>212.90 (-13.74%)</td><td>112.97 (-7.00%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.00 (n/a)</td><td>443.30 (n/a)</td><td>467.90 (n/a)</td><td>246.80 (n/a)</td><td>121.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+18.27%)</td><td>0.01 (-5.92%)</td><td>0.01 <b>(-43.12%)</b></td><td>0.01 (-10.08%)</td><td>0.01 <b>(+71.74%)</b></td><td>563.20 (+11.22%)</td><td>414.66 (+19.61%)</td><td>523.90 <b>(+75.81%)</b></td><td>202.30 (-15.43%)</td><td>175.25 <b>(+63.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.40 (n/a)</td><td>346.68 (n/a)</td><td>298.00 (n/a)</td><td>239.20 (n/a)</td><td>107.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (-2.32%)</td><td>0.01 (+16.16%)</td><td>0.01 (+10.18%)</td><td>0.01 <b>(+241.33%)</b></td><td>0.00 <b>(-35.29%)</b></td><td>553.80 <b>(-70.70%)</b></td><td>396.24 <b>(-42.79%)</b></td><td>419.50 (-9.24%)</td><td>242.30 (+2.37%)</td><td>114.49 <b>(-83.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1890.40 (n/a)</td><td>692.58 (n/a)</td><td>462.20 (n/a)</td><td>236.70 (n/a)</td><td>678.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+6.73%)</td><td>0.01 (+8.97%)</td><td>0.01 <b>(+43.72%)</b></td><td>0.01 (-8.27%)</td><td>0.01 (+8.02%)</td><td>693.20 (+9.01%)</td><td>387.80 (-5.35%)</td><td>316.60 <b>(-30.40%)</b></td><td>221.20 (-6.31%)</td><td>191.88 (+17.38%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.90 (n/a)</td><td>409.74 (n/a)</td><td>454.90 (n/a)</td><td>236.10 (n/a)</td><td>163.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(+39.99%)</b></td><td>0.01 (+10.33%)</td><td>0.01 (+0.08%)</td><td>0.01 (-5.65%)</td><td>0.00 <b>(+132.74%)</b></td><td>545.00 (+5.99%)</td><td>423.10 (-4.22%)</td><td>426.80 (-0.09%)</td><td>264.00 <b>(-28.57%)</b></td><td>120.48 <b>(+77.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.20 (n/a)</td><td>441.72 (n/a)</td><td>427.20 (n/a)</td><td>369.60 (n/a)</td><td>67.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+10.88%)</td><td>0.01 (+1.30%)</td><td>0.01 (+10.46%)</td><td>0.01 (+7.01%)</td><td>0.00 (-1.38%)</td><td>643.60 (-6.55%)</td><td>471.72 (-3.31%)</td><td>488.10 (-9.46%)</td><td>254.90 (-9.83%)</td><td>160.11 (-13.36%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>688.70 (n/a)</td><td>487.88 (n/a)</td><td>539.10 (n/a)</td><td>282.70 (n/a)</td><td>184.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (-3.01%)</td><td>0.02 (-2.36%)</td><td>0.02 <b>(+22.24%)</b></td><td>0.01 (-8.39%)</td><td>0.01 (-8.85%)</td><td>591.40 (+9.15%)</td><td>420.60 (+1.10%)</td><td>432.80 (-18.20%)</td><td>232.30 (+3.11%)</td><td>166.61 (+1.77%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.80 (n/a)</td><td>416.04 (n/a)</td><td>529.10 (n/a)</td><td>225.30 (n/a)</td><td>163.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(+43.59%)</b></td><td>0.05 <b>(+59.94%)</b></td><td>0.05 <b>(+102.28%)</b></td><td>0.03 <b>(+30.17%)</b></td><td>0.02 <b>(+79.20%)</b></td><td>469.70 <b>(-23.19%)</b></td><td>309.30 <b>(-32.33%)</b></td><td>236.50 <b>(-50.56%)</b></td><td>178.20 <b>(-30.34%)</b></td><td>141.98 (+10.90%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.50 (n/a)</td><td>457.10 (n/a)</td><td>478.40 (n/a)</td><td>255.80 (n/a)</td><td>128.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(+22.88%)</b></td><td>0.02 (-5.85%)</td><td>0.01 (-9.70%)</td><td>0.01 (-2.16%)</td><td>0.01 <b>(+32.56%)</b></td><td>615.90 (+2.21%)</td><td>482.60 (+11.27%)</td><td>553.00 (+10.76%)</td><td>201.40 (-18.63%)</td><td>167.63 (+7.15%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.60 (n/a)</td><td>433.72 (n/a)</td><td>499.30 (n/a)</td><td>247.50 (n/a)</td><td>156.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (-5.10%)</td><td>0.03 (-8.79%)</td><td>0.03 (-13.89%)</td><td>0.02 (-2.93%)</td><td>0.01 (-16.80%)</td><td>482.50 (+3.03%)</td><td>356.44 (+6.58%)</td><td>352.40 (+16.15%)</td><td>222.00 (+5.36%)</td><td>101.58 (-13.69%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.30 (n/a)</td><td>334.42 (n/a)</td><td>303.40 (n/a)</td><td>210.70 (n/a)</td><td>117.69 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 <b>(-36.95%)</b></td><td>0.02 (-11.89%)</td><td>0.03 (-2.00%)</td><td>0.01 (-11.22%)</td><td>0.01 <b>(-48.60%)</b></td><td>668.80 (+12.63%)</td><td>378.94 (+2.68%)</td><td>301.90 (+2.03%)</td><td>259.10 <b>(+58.57%)</b></td><td>166.75 (-6.90%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.80 (n/a)</td><td>369.06 (n/a)</td><td>295.90 (n/a)</td><td>163.40 (n/a)</td><td>179.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(+182.79%)</b></td><td>0.04 <b>(+121.16%)</b></td><td>0.02 <b>(+35.36%)</b></td><td>0.02 <b>(+419.88%)</b></td><td>0.02 <b>(+166.10%)</b></td><td>473.70 <b>(-80.76%)</b></td><td>347.40 <b>(-62.86%)</b></td><td>420.20 <b>(-26.13%)</b></td><td>147.00 <b>(-64.65%)</b></td><td>139.41 <b>(-83.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2462.40 (n/a)</td><td>935.28 (n/a)</td><td>568.80 (n/a)</td><td>415.80 (n/a)</td><td>859.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (+6.67%)</td><td>0.02 (-3.00%)</td><td>0.02 (-9.83%)</td><td>0.01 (+9.61%)</td><td>0.00 (-8.22%)</td><td>984.70 (-8.76%)</td><td>552.44 (-0.29%)</td><td>474.00 (+10.90%)</td><td>387.90 (-6.24%)</td><td>244.40 (-16.81%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1079.30 (n/a)</td><td>554.02 (n/a)</td><td>427.40 (n/a)</td><td>413.70 (n/a)</td><td>293.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (+13.21%)</td><td>0.02 (+6.55%)</td><td>0.02 (-10.95%)</td><td>0.01 <b>(+66.35%)</b></td><td>0.01 (-7.36%)</td><td>634.30 <b>(-39.88%)</b></td><td>459.32 (-14.75%)</td><td>461.80 (+12.31%)</td><td>278.40 (-11.68%)</td><td>128.67 <b>(-56.55%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1055.10 (n/a)</td><td>538.82 (n/a)</td><td>411.20 (n/a)</td><td>315.20 (n/a)</td><td>296.17 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 <b>(+28.78%)</b></td><td>0.02 (+9.10%)</td><td>0.02 (-9.83%)</td><td>0.01 (-6.56%)</td><td>0.01 <b>(+182.36%)</b></td><td>585.60 (+7.04%)</td><td>456.92 (-0.74%)</td><td>522.90 (+10.90%)</td><td>299.20 <b>(-22.33%)</b></td><td>145.66 <b>(+130.00%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.10 (n/a)</td><td>460.34 (n/a)</td><td>471.50 (n/a)</td><td>385.20 (n/a)</td><td>63.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (-0.73%)</td><td>0.02 (-3.95%)</td><td>0.02 (+14.56%)</td><td>0.02 (-2.06%)</td><td>0.01 (-8.08%)</td><td>572.30 (+2.11%)</td><td>422.58 (+2.22%)</td><td>398.80 (-12.72%)</td><td>223.80 (+0.72%)</td><td>149.09 (-4.17%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.50 (n/a)</td><td>413.40 (n/a)</td><td>456.90 (n/a)</td><td>222.20 (n/a)</td><td>155.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 <b>(-41.20%)</b></td><td>0.02 (-17.33%)</td><td>0.02 (-18.89%)</td><td>0.01 (+12.97%)</td><td>0.00 <b>(-69.06%)</b></td><td>609.80 (-11.47%)</td><td>507.64 (+7.92%)</td><td>516.60 <b>(+23.29%)</b></td><td>424.00 <b>(+70.08%)</b></td><td>80.20 <b>(-56.10%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>688.80 (n/a)</td><td>470.38 (n/a)</td><td>419.00 (n/a)</td><td>249.30 (n/a)</td><td>182.69 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 <b>(-44.46%)</b></td><td>0.04 <b>(-27.62%)</b></td><td>0.03 (-3.11%)</td><td>0.03 (-6.34%)</td><td>0.01 <b>(-73.39%)</b></td><td>570.30 (+6.78%)</td><td>467.84 <b>(+22.06%)</b></td><td>470.30 (+3.23%)</td><td>377.40 <b>(+80.06%)</b></td><td>76.32 <b>(-48.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>534.10 (n/a)</td><td>383.28 (n/a)</td><td>455.60 (n/a)</td><td>209.60 (n/a)</td><td>147.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 <b>(-24.05%)</b></td><td>0.06 <b>(-27.78%)</b></td><td>0.06 <b>(-27.84%)</b></td><td>0.05 <b>(-33.77%)</b></td><td>0.01 (-2.44%)</td><td>470.00 <b>(+50.98%)</b></td><td>401.28 <b>(+39.67%)</b></td><td>417.80 <b>(+38.57%)</b></td><td>310.80 <b>(+31.64%)</b></td><td>58.74 <b>(+90.67%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>311.30 (n/a)</td><td>287.30 (n/a)</td><td>301.50 (n/a)</td><td>236.10 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (+5.26%)</td><td>0.03 <b>(-33.84%)</b></td><td>0.03 <b>(-50.15%)</b></td><td>0.01 <b>(-77.72%)</b></td><td>0.03 <b>(+65.75%)</b></td><td>2476.00 <b>(+348.79%)</b></td><td>1141.00 <b>(+195.66%)</b></td><td>608.80 <b>(+100.59%)</b></td><td>244.00 (-5.02%)</td><td>1034.37 <b>(+628.26%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>551.70 (n/a)</td><td>385.92 (n/a)</td><td>303.50 (n/a)</td><td>256.90 (n/a)</td><td>142.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 <b>(+23.94%)</b></td><td>0.05 (-0.72%)</td><td>0.04 (-2.49%)</td><td>0.03 (-4.25%)</td><td>0.02 <b>(+22.14%)</b></td><td>600.70 (+4.45%)</td><td>448.82 (+1.85%)</td><td>462.70 (+2.57%)</td><td>240.00 (-19.33%)</td><td>130.74 (-4.67%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>575.10 (n/a)</td><td>440.66 (n/a)</td><td>451.10 (n/a)</td><td>297.50 (n/a)</td><td>137.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (+0.76%)</td><td>0.05 (+14.07%)</td><td>0.06 <b>(+77.81%)</b></td><td>0.01 <b>(-73.86%)</b></td><td>0.03 <b>(+75.66%)</b></td><td>2032.50 <b>(+282.62%)</b></td><td>666.26 <b>(+54.03%)</b></td><td>264.30 <b>(-43.77%)</b></td><td>240.70 (-0.74%)</td><td>774.03 <b>(+598.84%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>531.20 (n/a)</td><td>432.54 (n/a)</td><td>470.00 (n/a)</td><td>242.50 (n/a)</td><td>110.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (-15.75%)</td><td>0.06 (-6.15%)</td><td>0.05 (-16.94%)</td><td>0.04 (+14.43%)</td><td>0.01 <b>(-33.18%)</b></td><td>549.00 (-12.62%)</td><td>380.72 (+0.09%)</td><td>379.10 <b>(+20.39%)</b></td><td>279.20 (+18.71%)</td><td>106.23 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.30 (n/a)</td><td>380.38 (n/a)</td><td>314.90 (n/a)</td><td>235.20 (n/a)</td><td>157.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (-13.83%)</td><td>0.05 <b>(+32.97%)</b></td><td>0.06 <b>(+114.79%)</b></td><td>0.01 <b>(-66.56%)</b></td><td>0.02 (+12.74%)</td><td>1845.90 <b>(+198.98%)</b></td><td>581.86 (+17.46%)</td><td>263.40 <b>(-53.44%)</b></td><td>246.70 (+16.09%)</td><td>707.00 <b>(+334.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>617.40 (n/a)</td><td>495.36 (n/a)</td><td>565.70 (n/a)</td><td>212.50 (n/a)</td><td>162.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 <b>(+29.10%)</b></td><td>0.05 (+13.40%)</td><td>0.05 (+5.91%)</td><td>0.03 (-0.25%)</td><td>0.02 <b>(+76.62%)</b></td><td>537.90 (+0.26%)</td><td>389.70 (-6.80%)</td><td>399.70 (-5.58%)</td><td>226.60 <b>(-22.53%)</b></td><td>125.04 <b>(+39.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>536.50 (n/a)</td><td>418.14 (n/a)</td><td>423.30 (n/a)</td><td>292.50 (n/a)</td><td>89.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (-17.67%)</td><td>0.04 (+3.11%)</td><td>0.04 (+9.25%)</td><td>0.03 (+16.93%)</td><td>0.01 <b>(-38.80%)</b></td><td>538.80 (-14.48%)</td><td>390.18 (-11.52%)</td><td>416.50 (-8.48%)</td><td>259.90 <b>(+21.45%)</b></td><td>106.89 <b>(-37.89%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>630.00 (n/a)</td><td>441.00 (n/a)</td><td>455.10 (n/a)</td><td>214.00 (n/a)</td><td>172.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (+9.24%)</td><td>0.05 (+17.49%)</td><td>0.05 <b>(+40.27%)</b></td><td>0.04 <b>(+35.80%)</b></td><td>0.01 <b>(-30.79%)</b></td><td>471.60 <b>(-26.37%)</b></td><td>356.58 (-19.60%)</td><td>343.60 <b>(-28.70%)</b></td><td>272.90 (-8.45%)</td><td>74.10 <b>(-48.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>640.50 (n/a)</td><td>443.48 (n/a)</td><td>481.90 (n/a)</td><td>298.10 (n/a)</td><td>145.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 <b>(+28.81%)</b></td><td>0.05 <b>(+35.91%)</b></td><td>0.05 <b>(+51.87%)</b></td><td>0.04 (+16.57%)</td><td>0.01 <b>(+54.11%)</b></td><td>461.80 (-14.21%)</td><td>339.16 <b>(-25.26%)</b></td><td>306.30 <b>(-34.17%)</b></td><td>261.80 <b>(-22.36%)</b></td><td>81.28 (+5.34%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.30 (n/a)</td><td>453.76 (n/a)</td><td>465.30 (n/a)</td><td>337.20 (n/a)</td><td>77.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (-1.55%)</td><td>0.09 (+2.58%)</td><td>0.12 <b>(+45.85%)</b></td><td>0.02 <b>(-66.30%)</b></td><td>0.05 <b>(+62.05%)</b></td><td>1899.30 <b>(+196.77%)</b></td><td>638.32 <b>(+56.83%)</b></td><td>269.20 <b>(-31.43%)</b></td><td>258.60 (+1.57%)</td><td>712.66 <b>(+375.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>640.00 (n/a)</td><td>407.02 (n/a)</td><td>392.60 (n/a)</td><td>254.60 (n/a)</td><td>150.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (+2.98%)</td><td>0.10 (+5.67%)</td><td>0.12 <b>(+57.19%)</b></td><td>0.05 <b>(-21.49%)</b></td><td>0.04 (+11.01%)</td><td>612.20 <b>(+27.38%)</b></td><td>371.04 (-0.72%)</td><td>278.00 <b>(-36.38%)</b></td><td>225.20 (-2.89%)</td><td>168.81 <b>(+38.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>480.60 (n/a)</td><td>373.74 (n/a)</td><td>437.00 (n/a)</td><td>231.90 (n/a)</td><td>122.08 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (+4.59%)</td><td>0.11 (-4.38%)</td><td>0.10 (-6.17%)</td><td>0.06 <b>(-29.73%)</b></td><td>0.05 <b>(+60.95%)</b></td><td>651.40 <b>(+42.32%)</b></td><td>436.52 (+16.67%)</td><td>415.50 (+6.57%)</td><td>247.50 (-4.37%)</td><td>187.82 <b>(+110.23%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>457.70 (n/a)</td><td>374.14 (n/a)</td><td>389.90 (n/a)</td><td>258.80 (n/a)</td><td>89.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (+2.83%)</td><td>0.11 (+13.67%)</td><td>0.12 (+5.55%)</td><td>0.06 (+7.43%)</td><td>0.03 (-17.52%)</td><td>529.50 (-6.91%)</td><td>314.16 (-15.73%)</td><td>275.90 (-5.25%)</td><td>236.10 (-2.76%)</td><td>121.66 <b>(-21.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>568.80 (n/a)</td><td>372.80 (n/a)</td><td>291.20 (n/a)</td><td>242.80 (n/a)</td><td>154.25 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.18 (+8.74%)</td><td>0.11 (+2.94%)</td><td>0.11 <b>(+26.21%)</b></td><td>0.06 <b>(-26.68%)</b></td><td>0.04 (+2.12%)</td><td>713.50 <b>(+36.40%)</b></td><td>408.16 (-0.33%)</td><td>383.70 <b>(-20.77%)</b></td><td>229.40 (-8.02%)</td><td>182.66 <b>(+31.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>523.10 (n/a)</td><td>409.50 (n/a)</td><td>484.30 (n/a)</td><td>249.40 (n/a)</td><td>138.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (+0.51%)</td><td>0.09 <b>(-21.31%)</b></td><td>0.08 <b>(-32.05%)</b></td><td>0.05 <b>(-27.05%)</b></td><td>0.03 <b>(+23.48%)</b></td><td>595.90 <b>(+37.08%)</b></td><td>402.20 <b>(+32.14%)</b></td><td>393.10 <b>(+47.17%)</b></td><td>241.10 (-0.54%)</td><td>127.23 <b>(+62.80%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>434.70 (n/a)</td><td>304.38 (n/a)</td><td>267.10 (n/a)</td><td>242.40 (n/a)</td><td>78.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (+2.73%)</td><td>0.10 (+3.00%)</td><td>0.10 <b>(+21.82%)</b></td><td>0.06 (-18.68%)</td><td>0.03 <b>(+36.04%)</b></td><td>585.10 <b>(+22.97%)</b></td><td>412.24 (+0.47%)</td><td>365.80 (-17.91%)</td><td>294.50 (-2.64%)</td><td>120.27 <b>(+63.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>475.80 (n/a)</td><td>410.32 (n/a)</td><td>445.60 (n/a)</td><td>302.50 (n/a)</td><td>73.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (+2.94%)</td><td>0.10 (-5.87%)</td><td>0.11 (-6.83%)</td><td>0.06 (-16.96%)</td><td>0.04 (+19.01%)</td><td>592.50 <b>(+20.40%)</b></td><td>365.46 (+12.43%)</td><td>299.40 (+7.35%)</td><td>198.40 (-2.84%)</td><td>160.57 <b>(+40.17%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>492.10 (n/a)</td><td>325.06 (n/a)</td><td>278.90 (n/a)</td><td>204.20 (n/a)</td><td>114.55 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 <b>(-36.02%)</b></td><td>0.08 (+7.80%)</td><td>0.07 <b>(+28.33%)</b></td><td>0.07 <b>(+276.26%)</b></td><td>0.01 <b>(-76.54%)</b></td><td>508.60 <b>(-73.42%)</b></td><td>471.06 <b>(-40.07%)</b></td><td>497.50 <b>(-22.07%)</b></td><td>364.60 <b>(+56.28%)</b></td><td>60.30 <b>(-90.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1913.50 (n/a)</td><td>786.08 (n/a)</td><td>638.40 (n/a)</td><td>233.30 (n/a)</td><td>654.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (-12.22%)</td><td>0.10 (+6.32%)</td><td>0.11 <b>(+39.12%)</b></td><td>0.07 (+14.23%)</td><td>0.02 <b>(-23.31%)</b></td><td>460.70 (-12.45%)</td><td>359.28 (-8.64%)</td><td>305.90 <b>(-28.13%)</b></td><td>278.70 (+13.89%)</td><td>92.40 <b>(-20.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>526.20 (n/a)</td><td>393.26 (n/a)</td><td>425.60 (n/a)</td><td>244.70 (n/a)</td><td>115.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (+11.13%)</td><td>0.06 (+15.89%)</td><td>0.05 (+10.48%)</td><td>0.04 <b>(+214.64%)</b></td><td>0.02 <b>(-24.05%)</b></td><td>550.30 <b>(-68.21%)</b></td><td>393.62 <b>(-39.74%)</b></td><td>424.00 (-9.50%)</td><td>231.30 (-10.04%)</td><td>129.33 <b>(-78.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1731.30 (n/a)</td><td>653.20 (n/a)</td><td>468.50 (n/a)</td><td>257.10 (n/a)</td><td>614.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (+19.55%)</td><td>0.07 <b>(+39.04%)</b></td><td>0.07 <b>(+50.23%)</b></td><td>0.06 <b>(+46.18%)</b></td><td>0.01 <b>(-25.59%)</b></td><td>369.30 <b>(-31.60%)</b></td><td>302.06 <b>(-30.53%)</b></td><td>297.90 <b>(-33.43%)</b></td><td>246.60 (-16.35%)</td><td>43.71 <b>(-57.76%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>539.90 (n/a)</td><td>434.80 (n/a)</td><td>447.50 (n/a)</td><td>294.80 (n/a)</td><td>103.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (+7.54%)</td><td>0.05 (+5.03%)</td><td>0.06 <b>(+46.96%)</b></td><td>0.01 <b>(-71.91%)</b></td><td>0.03 <b>(+79.27%)</b></td><td>1990.10 <b>(+256.07%)</b></td><td>704.06 <b>(+53.45%)</b></td><td>350.90 <b>(-31.96%)</b></td><td>254.30 (-7.02%)</td><td>734.04 <b>(+518.34%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.90 (n/a)</td><td>458.82 (n/a)</td><td>515.70 (n/a)</td><td>273.50 (n/a)</td><td>118.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (-1.43%)</td><td>0.06 (+7.83%)</td><td>0.07 <b>(+60.08%)</b></td><td>0.02 <b>(-42.61%)</b></td><td>0.03 <b>(+40.02%)</b></td><td>1033.50 <b>(+74.25%)</b></td><td>482.12 (+12.11%)</td><td>295.90 <b>(-37.53%)</b></td><td>252.50 (+1.49%)</td><td>330.28 <b>(+152.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.10 (n/a)</td><td>430.04 (n/a)</td><td>473.70 (n/a)</td><td>248.80 (n/a)</td><td>130.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (-5.54%)</td><td>0.06 (+3.20%)</td><td>0.05 <b>(+22.31%)</b></td><td>0.03 (-9.00%)</td><td>0.02 (-16.53%)</td><td>604.50 (+9.89%)</td><td>401.68 (-5.93%)</td><td>422.80 (-18.24%)</td><td>250.20 (+5.84%)</td><td>137.12 (-8.06%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>550.10 (n/a)</td><td>427.02 (n/a)</td><td>517.10 (n/a)</td><td>236.40 (n/a)</td><td>149.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (-8.80%)</td><td>0.07 <b>(+54.89%)</b></td><td>0.08 <b>(+117.49%)</b></td><td>0.05 <b>(+76.77%)</b></td><td>0.01 <b>(-53.62%)</b></td><td>380.60 <b>(-43.43%)</b></td><td>299.56 <b>(-42.39%)</b></td><td>267.30 <b>(-54.02%)</b></td><td>265.30 (+9.63%)</td><td>50.47 <b>(-69.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>672.80 (n/a)</td><td>519.96 (n/a)</td><td>581.30 (n/a)</td><td>242.00 (n/a)</td><td>167.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 <b>(+72.92%)</b></td><td>0.09 <b>(+70.10%)</b></td><td>0.08 <b>(+81.99%)</b></td><td>0.05 (+17.57%)</td><td>0.03 <b>(+130.94%)</b></td><td>512.60 (-14.95%)</td><td>314.54 <b>(-37.95%)</b></td><td>295.50 <b>(-45.04%)</b></td><td>214.20 <b>(-42.19%)</b></td><td>117.09 (+16.69%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>602.70 (n/a)</td><td>506.94 (n/a)</td><td>537.70 (n/a)</td><td>370.50 (n/a)</td><td>100.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 <b>(+28.65%)</b></td><td>0.08 <b>(+41.29%)</b></td><td>0.09 <b>(+65.56%)</b></td><td>0.04 (-14.16%)</td><td>0.03 <b>(+53.71%)</b></td><td>635.90 (+16.49%)</td><td>338.84 <b>(-23.49%)</b></td><td>275.00 <b>(-39.60%)</b></td><td>211.10 <b>(-22.25%)</b></td><td>169.21 <b>(+58.44%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>545.90 (n/a)</td><td>442.86 (n/a)</td><td>455.30 (n/a)</td><td>271.50 (n/a)</td><td>106.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (+6.21%)</td><td>0.07 (+17.60%)</td><td>0.06 (+10.66%)</td><td>0.05 (+0.56%)</td><td>0.02 (+18.84%)</td><td>543.00 (-0.55%)</td><td>396.38 (-13.07%)</td><td>439.80 (-9.64%)</td><td>251.80 (-5.87%)</td><td>124.11 (+14.20%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>546.00 (n/a)</td><td>456.00 (n/a)</td><td>486.70 (n/a)</td><td>267.50 (n/a)</td><td>108.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 <b>(+32.71%)</b></td><td>0.06 (+6.00%)</td><td>0.06 (-5.04%)</td><td>0.04 (-12.07%)</td><td>0.02 <b>(+69.61%)</b></td><td>654.50 (+13.75%)</td><td>442.14 (+0.44%)</td><td>418.70 (+5.31%)</td><td>242.80 <b>(-24.64%)</b></td><td>158.58 <b>(+39.97%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>575.40 (n/a)</td><td>440.20 (n/a)</td><td>397.60 (n/a)</td><td>322.20 (n/a)</td><td>113.29 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 <b>(+30.69%)</b></td><td>0.06 (+0.20%)</td><td>0.05 (-19.55%)</td><td>0.04 <b>(+208.42%)</b></td><td>0.03 (+5.08%)</td><td>603.80 <b>(-67.58%)</b></td><td>486.26 <b>(-27.76%)</b></td><td>532.70 <b>(+24.29%)</b></td><td>205.80 <b>(-23.49%)</b></td><td>161.08 <b>(-76.08%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1862.30 (n/a)</td><td>673.08 (n/a)</td><td>428.60 (n/a)</td><td>269.00 (n/a)</td><td>673.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 <b>(+20.42%)</b></td><td>0.06 (+12.01%)</td><td>0.07 <b>(+23.80%)</b></td><td>0.04 (-9.12%)</td><td>0.02 <b>(+62.63%)</b></td><td>631.10 (+10.04%)</td><td>421.78 (-5.18%)</td><td>348.50 (-19.22%)</td><td>259.40 (-16.94%)</td><td>153.33 <b>(+53.84%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>573.50 (n/a)</td><td>444.84 (n/a)</td><td>431.40 (n/a)</td><td>312.30 (n/a)</td><td>99.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(+49.75%)</b></td><td>0.06 <b>(+31.36%)</b></td><td>0.07 <b>(+51.41%)</b></td><td>0.03 (-11.17%)</td><td>0.02 <b>(+375.55%)</b></td><td>545.90 (+12.56%)</td><td>361.26 (-16.97%)</td><td>274.80 <b>(-33.94%)</b></td><td>265.90 <b>(-33.21%)</b></td><td>130.29 <b>(+240.34%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>485.00 (n/a)</td><td>435.12 (n/a)</td><td>416.00 (n/a)</td><td>398.10 (n/a)</td><td>38.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 <b>(-21.97%)</b></td><td>0.05 (+5.50%)</td><td>0.04 (-7.21%)</td><td>0.03 <b>(+201.45%)</b></td><td>0.02 <b>(-38.54%)</b></td><td>641.70 <b>(-66.83%)</b></td><td>455.36 <b>(-36.42%)</b></td><td>490.20 (+7.76%)</td><td>279.80 <b>(+28.17%)</b></td><td>158.10 <b>(-77.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1934.30 (n/a)</td><td>716.18 (n/a)</td><td>454.90 (n/a)</td><td>218.30 (n/a)</td><td>693.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (+1.52%)</td><td>0.04 (-15.83%)</td><td>0.04 <b>(-26.40%)</b></td><td>0.01 <b>(-69.18%)</b></td><td>0.02 <b>(+47.76%)</b></td><td>1959.80 <b>(+224.47%)</b></td><td>716.78 <b>(+77.13%)</b></td><td>433.60 <b>(+35.88%)</b></td><td>273.00 (-1.52%)</td><td>708.58 <b>(+380.27%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.00 (n/a)</td><td>404.66 (n/a)</td><td>319.10 (n/a)</td><td>277.20 (n/a)</td><td>147.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 <b>(-26.76%)</b></td><td>0.05 (-13.24%)</td><td>0.04 (+1.07%)</td><td>0.04 <b>(+27.69%)</b></td><td>0.01 <b>(-57.31%)</b></td><td>507.20 <b>(-21.68%)</b></td><td>419.60 (+1.80%)</td><td>431.70 (-1.08%)</td><td>296.70 <b>(+36.54%)</b></td><td>80.22 <b>(-53.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.60 (n/a)</td><td>412.20 (n/a)</td><td>436.40 (n/a)</td><td>217.30 (n/a)</td><td>174.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (+9.74%)</td><td>0.05 (+14.66%)</td><td>0.05 <b>(+39.66%)</b></td><td>0.03 (+15.03%)</td><td>0.01 (-14.15%)</td><td>534.70 (-13.06%)</td><td>375.64 (-16.39%)</td><td>343.30 <b>(-28.39%)</b></td><td>250.60 (-8.87%)</td><td>106.08 <b>(-30.59%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.00 (n/a)</td><td>449.30 (n/a)</td><td>479.40 (n/a)</td><td>275.00 (n/a)</td><td>152.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 <b>(-22.67%)</b></td><td>0.04 <b>(-21.77%)</b></td><td>0.04 (-10.91%)</td><td>0.02 <b>(-25.94%)</b></td><td>0.02 <b>(-30.41%)</b></td><td>803.10 <b>(+35.04%)</b></td><td>522.74 <b>(+24.44%)</b></td><td>480.00 (+12.23%)</td><td>292.80 <b>(+29.27%)</b></td><td>195.26 (+18.32%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.70 (n/a)</td><td>420.06 (n/a)</td><td>427.70 (n/a)</td><td>226.50 (n/a)</td><td>165.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.41 (+9.57%)</td><td>0.29 (+9.40%)</td><td>0.28 (+0.50%)</td><td>0.19 (+11.59%)</td><td>0.08 (-7.75%)</td><td>516.60 (-10.37%)</td><td>357.12 (-11.33%)</td><td>348.30 (-0.49%)</td><td>240.90 (-8.75%)</td><td>104.03 <b>(-26.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>576.40 (n/a)</td><td>402.76 (n/a)</td><td>350.00 (n/a)</td><td>264.00 (n/a)</td><td>140.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.41 (+18.79%)</td><td>0.27 (-11.48%)</td><td>0.22 <b>(-35.13%)</b></td><td>0.18 (-1.73%)</td><td>0.10 <b>(+47.19%)</b></td><td>551.00 (+1.75%)</td><td>405.56 (+18.18%)</td><td>450.50 <b>(+54.18%)</b></td><td>241.70 (-15.81%)</td><td>136.22 <b>(+22.69%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>541.50 (n/a)</td><td>343.18 (n/a)</td><td>292.20 (n/a)</td><td>287.10 (n/a)</td><td>111.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.51 <b>(+35.63%)</b></td><td>0.23 (+0.38%)</td><td>0.18 (-11.62%)</td><td>0.05 <b>(-67.43%)</b></td><td>0.17 <b>(+94.84%)</b></td><td>2050.90 <b>(+207.07%)</b></td><td>759.08 <b>(+59.77%)</b></td><td>552.20 (+13.16%)</td><td>191.00 <b>(-26.28%)</b></td><td>738.75 <b>(+397.87%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.38 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>667.90 (n/a)</td><td>475.10 (n/a)</td><td>488.00 (n/a)</td><td>259.10 (n/a)</td><td>148.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.27 (+5.81%)</td><td>0.17 (-8.05%)</td><td>0.17 (-4.64%)</td><td>0.03 <b>(-78.76%)</b></td><td>0.09 <b>(+79.76%)</b></td><td>2473.10 <b>(+370.71%)</b></td><td>791.64 <b>(+90.15%)</b></td><td>444.50 (+4.86%)</td><td>274.40 (-5.48%)</td><td>943.24 <b>(+775.51%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>525.40 (n/a)</td><td>416.32 (n/a)</td><td>423.90 (n/a)</td><td>290.30 (n/a)</td><td>107.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.33 <b>(+22.28%)</b></td><td>0.26 <b>(+65.20%)</b></td><td>0.26 <b>(+82.39%)</b></td><td>0.14 <b>(+266.41%)</b></td><td>0.08 (-10.27%)</td><td>538.20 <b>(-72.71%)</b></td><td>314.24 <b>(-57.42%)</b></td><td>279.40 <b>(-45.18%)</b></td><td>220.40 (-18.22%)</td><td>130.08 <b>(-81.42%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.09 (n/a)</td><td>1971.90 (n/a)</td><td>738.04 (n/a)</td><td>509.70 (n/a)</td><td>269.50 (n/a)</td><td>700.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.32 <b>(+23.19%)</b></td><td>0.24 <b>(+44.75%)</b></td><td>0.24 <b>(+54.72%)</b></td><td>0.17 <b>(+49.49%)</b></td><td>0.05 (-2.76%)</td><td>444.00 <b>(-33.10%)</b></td><td>319.70 <b>(-33.19%)</b></td><td>304.50 <b>(-35.38%)</b></td><td>231.50 (-18.80%)</td><td>77.08 <b>(-43.83%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>663.70 (n/a)</td><td>478.50 (n/a)</td><td>471.20 (n/a)</td><td>285.10 (n/a)</td><td>137.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (+6.77%)</td><td>0.14 <b>(+35.27%)</b></td><td>0.15 <b>(+80.58%)</b></td><td>0.10 <b>(+34.65%)</b></td><td>0.02 <b>(-34.46%)</b></td><td>369.00 <b>(-25.72%)</b></td><td>272.44 <b>(-30.29%)</b></td><td>244.70 <b>(-44.63%)</b></td><td>239.00 (-6.35%)</td><td>55.11 <b>(-53.69%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>496.80 (n/a)</td><td>390.84 (n/a)</td><td>441.90 (n/a)</td><td>255.20 (n/a)</td><td>119.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (-6.54%)</td><td>0.11 (+7.09%)</td><td>0.12 <b>(+25.10%)</b></td><td>0.08 (+6.32%)</td><td>0.02 <b>(-34.20%)</b></td><td>452.30 (-5.95%)</td><td>337.96 (-9.72%)</td><td>305.50 <b>(-20.07%)</b></td><td>281.60 (+6.99%)</td><td>68.27 <b>(-32.26%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>480.90 (n/a)</td><td>374.34 (n/a)</td><td>382.20 (n/a)</td><td>263.20 (n/a)</td><td>100.78 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (+5.95%)</td><td>0.11 (+4.23%)</td><td>0.11 <b>(+30.35%)</b></td><td>0.06 (-10.99%)</td><td>0.03 (-1.55%)</td><td>571.60 (+12.34%)</td><td>374.92 (-3.60%)</td><td>334.30 <b>(-23.29%)</b></td><td>251.70 (-5.62%)</td><td>122.66 (+11.92%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>508.80 (n/a)</td><td>388.92 (n/a)</td><td>435.80 (n/a)</td><td>266.70 (n/a)</td><td>109.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (-5.49%)</td><td>0.09 (-9.98%)</td><td>0.08 (-2.46%)</td><td>0.06 <b>(-20.43%)</b></td><td>0.03 (-5.44%)</td><td>643.60 <b>(+25.68%)</b></td><td>442.38 (+12.29%)</td><td>453.30 (+2.51%)</td><td>290.50 (+5.79%)</td><td>132.74 <b>(+29.38%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>512.10 (n/a)</td><td>393.96 (n/a)</td><td>442.20 (n/a)</td><td>274.60 (n/a)</td><td>102.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.18 <b>(+99.75%)</b></td><td>0.09 (+18.23%)</td><td>0.08 (+0.02%)</td><td>0.02 <b>(-71.93%)</b></td><td>0.06 <b>(+307.22%)</b></td><td>2424.10 <b>(+256.22%)</b></td><td>774.98 <b>(+61.60%)</b></td><td>444.70 (-0.02%)</td><td>200.30 <b>(-49.94%)</b></td><td>928.23 <b>(+708.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>680.50 (n/a)</td><td>479.58 (n/a)</td><td>444.80 (n/a)</td><td>400.10 (n/a)</td><td>114.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (-2.30%)</td><td>0.11 <b>(+45.11%)</b></td><td>0.09 <b>(+45.74%)</b></td><td>0.07 <b>(+290.65%)</b></td><td>0.05 <b>(-20.93%)</b></td><td>523.30 <b>(-74.40%)</b></td><td>379.58 <b>(-52.96%)</b></td><td>417.20 <b>(-31.37%)</b></td><td>211.30 (+2.37%)</td><td>143.75 <b>(-79.84%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2044.30 (n/a)</td><td>806.92 (n/a)</td><td>607.90 (n/a)</td><td>206.40 (n/a)</td><td>712.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.16 (-9.61%)</td><td>0.12 (+3.99%)</td><td>0.13 <b>(+50.67%)</b></td><td>0.08 (+16.42%)</td><td>0.04 <b>(-23.54%)</b></td><td>526.60 (-14.11%)</td><td>383.84 (-8.60%)</td><td>324.80 <b>(-33.63%)</b></td><td>262.60 (+10.61%)</td><td>129.85 (-19.85%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>613.10 (n/a)</td><td>419.96 (n/a)</td><td>489.40 (n/a)</td><td>237.40 (n/a)</td><td>162.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (-8.82%)</td><td>0.09 (-2.51%)</td><td>0.09 (-0.63%)</td><td>0.08 (+7.48%)</td><td>0.02 <b>(-25.33%)</b></td><td>508.40 (-6.95%)</td><td>442.42 (+0.99%)</td><td>449.20 (+0.63%)</td><td>330.20 (+9.70%)</td><td>68.19 <b>(-22.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>546.40 (n/a)</td><td>438.08 (n/a)</td><td>446.40 (n/a)</td><td>301.00 (n/a)</td><td>87.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.19 (+17.15%)</td><td>0.13 (+19.98%)</td><td>0.14 <b>(+65.17%)</b></td><td>0.02 <b>(-66.61%)</b></td><td>0.06 <b>(+53.32%)</b></td><td>1905.30 <b>(+199.48%)</b></td><td>595.68 <b>(+38.75%)</b></td><td>286.50 <b>(-39.45%)</b></td><td>213.80 (-14.65%)</td><td>732.82 <b>(+370.18%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>636.20 (n/a)</td><td>429.32 (n/a)</td><td>473.20 (n/a)</td><td>250.50 (n/a)</td><td>155.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (+0.01%)</td><td>0.07 <b>(-24.83%)</b></td><td>0.08 <b>(-20.63%)</b></td><td>0.02 <b>(-28.37%)</b></td><td>0.06 (+3.87%)</td><td>2482.90 <b>(+39.61%)</b></td><td>1125.36 <b>(+67.28%)</b></td><td>539.50 <b>(+25.99%)</b></td><td>273.50 (-0.04%)</td><td>1006.09 <b>(+59.03%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1778.50 (n/a)</td><td>672.74 (n/a)</td><td>428.20 (n/a)</td><td>273.60 (n/a)</td><td>632.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (-14.39%)</td><td>0.11 (-16.83%)</td><td>0.09 <b>(-28.51%)</b></td><td>0.07 (-18.89%)</td><td>0.05 (+15.76%)</td><td>604.50 <b>(+23.29%)</b></td><td>427.06 <b>(+28.47%)</b></td><td>454.10 <b>(+39.90%)</b></td><td>247.70 (+16.84%)</td><td>168.40 <b>(+61.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>490.30 (n/a)</td><td>332.42 (n/a)</td><td>324.60 (n/a)</td><td>212.00 (n/a)</td><td>104.45 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (+14.36%)</td><td>0.08 (-9.04%)</td><td>0.08 (-16.33%)</td><td>0.04 <b>(-47.83%)</b></td><td>0.03 <b>(+183.80%)</b></td><td>998.90 <b>(+91.69%)</b></td><td>568.44 <b>(+22.28%)</b></td><td>518.20 (+19.51%)</td><td>371.10 (-12.56%)</td><td>249.60 <b>(+400.09%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>521.10 (n/a)</td><td>464.86 (n/a)</td><td>433.60 (n/a)</td><td>424.40 (n/a)</td><td>49.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (-9.89%)</td><td>0.11 <b>(+24.69%)</b></td><td>0.12 <b>(+56.53%)</b></td><td>0.06 <b>(+83.02%)</b></td><td>0.03 <b>(-37.61%)</b></td><td>566.70 <b>(-45.36%)</b></td><td>339.22 <b>(-33.62%)</b></td><td>279.10 <b>(-36.10%)</b></td><td>269.10 (+10.97%)</td><td>128.11 <b>(-60.19%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1037.10 (n/a)</td><td>511.04 (n/a)</td><td>436.80 (n/a)</td><td>242.50 (n/a)</td><td>321.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (-5.94%)</td><td>0.09 (-8.10%)</td><td>0.08 (+0.56%)</td><td>0.05 <b>(-35.50%)</b></td><td>0.03 <b>(+26.23%)</b></td><td>747.70 <b>(+55.03%)</b></td><td>451.60 (+17.41%)</td><td>424.20 (-0.54%)</td><td>270.90 (+6.28%)</td><td>189.61 <b>(+109.09%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>482.30 (n/a)</td><td>384.62 (n/a)</td><td>426.50 (n/a)</td><td>254.90 (n/a)</td><td>90.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.16 (+6.54%)</td><td>0.13 <b>(+33.21%)</b></td><td>0.12 <b>(+46.04%)</b></td><td>0.11 <b>(+74.82%)</b></td><td>0.02 <b>(-49.85%)</b></td><td>313.40 <b>(-42.80%)</b></td><td>271.08 <b>(-32.50%)</b></td><td>289.40 <b>(-31.52%)</b></td><td>219.50 (-6.16%)</td><td>38.77 <b>(-73.70%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>547.90 (n/a)</td><td>401.58 (n/a)</td><td>422.60 (n/a)</td><td>233.90 (n/a)</td><td>147.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (+1.96%)</td><td>0.10 (+6.85%)</td><td>0.12 (+4.66%)</td><td>0.06 <b>(+33.41%)</b></td><td>0.04 (-12.96%)</td><td>563.70 <b>(-25.05%)</b></td><td>375.50 (-13.07%)</td><td>300.40 (-4.45%)</td><td>239.80 (-1.92%)</td><td>143.61 <b>(-34.51%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>752.10 (n/a)</td><td>431.94 (n/a)</td><td>314.40 (n/a)</td><td>244.50 (n/a)</td><td>219.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 <b>(-20.36%)</b></td><td>0.10 (+12.89%)</td><td>0.11 <b>(+51.94%)</b></td><td>0.07 (+9.00%)</td><td>0.03 <b>(-42.97%)</b></td><td>485.60 (-8.26%)</td><td>353.22 (-18.30%)</td><td>311.40 <b>(-34.18%)</b></td><td>245.40 <b>(+25.59%)</b></td><td>95.51 <b>(-29.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>529.30 (n/a)</td><td>432.36 (n/a)</td><td>473.10 (n/a)</td><td>195.40 (n/a)</td><td>135.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 <b>(+22.95%)</b></td><td>0.09 <b>(+20.36%)</b></td><td>0.08 <b>(+22.73%)</b></td><td>0.08 <b>(+26.74%)</b></td><td>0.02 <b>(+24.20%)</b></td><td>455.40 <b>(-21.10%)</b></td><td>409.28 (-16.92%)</td><td>425.60 (-18.53%)</td><td>301.30 (-18.68%)</td><td>62.96 (-19.76%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>577.20 (n/a)</td><td>492.64 (n/a)</td><td>522.40 (n/a)</td><td>370.50 (n/a)</td><td>78.46 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.46 (+4.02%)</td><td>0.34 (+16.81%)</td><td>0.37 <b>(+22.90%)</b></td><td>0.22 <b>(+53.05%)</b></td><td>0.10 (-11.82%)</td><td>593.30 <b>(-34.66%)</b></td><td>414.90 (-19.92%)</td><td>356.10 (-18.62%)</td><td>285.20 (-3.84%)</td><td>128.15 <b>(-45.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>908.00 (n/a)</td><td>518.12 (n/a)</td><td>437.60 (n/a)</td><td>296.60 (n/a)</td><td>236.21 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.49 (+13.17%)</td><td>0.41 <b>(+26.51%)</b></td><td>0.47 <b>(+23.68%)</b></td><td>0.19 (+16.97%)</td><td>0.13 (-0.95%)</td><td>681.40 (-14.52%)</td><td>360.24 <b>(-22.96%)</b></td><td>281.60 (-19.15%)</td><td>265.10 (-11.63%)</td><td>179.90 (-18.33%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.38 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>797.10 (n/a)</td><td>467.60 (n/a)</td><td>348.30 (n/a)</td><td>300.00 (n/a)</td><td>220.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.48 (+3.05%)</td><td>0.32 (+3.09%)</td><td>0.42 <b>(+32.12%)</b></td><td>0.07 <b>(-43.57%)</b></td><td>0.18 <b>(+35.69%)</b></td><td>1895.10 <b>(+77.19%)</b></td><td>687.86 <b>(+32.12%)</b></td><td>310.20 <b>(-24.32%)</b></td><td>274.50 (-2.97%)</td><td>693.60 <b>(+117.49%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>1069.50 (n/a)</td><td>520.62 (n/a)</td><td>409.90 (n/a)</td><td>282.90 (n/a)</td><td>318.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-37.50%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>21748.18 <b>(+54.95%)</b></td><td>17075.31 <b>(+77.35%)</b></td><td>19071.51 <b>(+123.51%)</b></td><td>5775.14 (-1.62%)</td><td>6453.48 <b>(+71.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>14035.81 (n/a)</td><td>9627.90 (n/a)</td><td>8532.56 (n/a)</td><td>5870.03 (n/a)</td><td>3752.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 <b>(-47.17%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (-16.70%)</td><td>23044.48 <b>(+66.66%)</b></td><td>17451.74 <b>(+105.18%)</b></td><td>21405.97 <b>(+172.63%)</b></td><td>7929.23 <b>(+33.97%)</b></td><td>6656.52 <b>(+112.14%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>13827.01 (n/a)</td><td>8505.76 (n/a)</td><td>7851.58 (n/a)</td><td>5918.64 (n/a)</td><td>3137.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (-2.94%)</td><td>0.09 (-3.62%)</td><td>0.08 (+2.47%)</td><td>0.08 (+1.87%)</td><td>0.03 (-7.39%)</td><td>27568.84 (-1.86%)</td><td>23772.59 (+2.90%)</td><td>25231.90 (-2.45%)</td><td>15121.81 (+3.05%)</td><td>5039.14 (-8.42%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28090.42 (n/a)</td><td>23103.50 (n/a)</td><td>25865.94 (n/a)</td><td>14674.80 (n/a)</td><td>5502.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.30 (-14.12%)</td><td>1.69 (-0.91%)</td><td>1.77 <b>(+26.12%)</b></td><td>1.04 <b>(-23.37%)</b></td><td>0.47 (-17.03%)</td><td>1013.10 <b>(+30.50%)</b></td><td>667.26 (+1.37%)</td><td>592.90 <b>(-20.70%)</b></td><td>455.50 (+16.44%)</td><td>212.76 <b>(+31.76%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.68 (n/a)</td><td>1.70 (n/a)</td><td>1.40 (n/a)</td><td>1.35 (n/a)</td><td>0.56 (n/a)</td><td>776.30 (n/a)</td><td>658.26 (n/a)</td><td>747.70 (n/a)</td><td>391.20 (n/a)</td><td>161.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.69 <b>(+44.42%)</b></td><td>2.27 (+11.67%)</td><td>1.68 <b>(-22.20%)</b></td><td>1.38 (+3.30%)</td><td>1.06 <b>(+112.44%)</b></td><td>759.00 (-3.20%)</td><td>542.68 (-0.49%)</td><td>623.30 <b>(+28.54%)</b></td><td>284.50 <b>(-30.74%)</b></td><td>219.08 <b>(+42.45%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.55 (n/a)</td><td>2.03 (n/a)</td><td>2.16 (n/a)</td><td>1.34 (n/a)</td><td>0.50 (n/a)</td><td>784.10 (n/a)</td><td>545.36 (n/a)</td><td>484.90 (n/a)</td><td>410.80 (n/a)</td><td>153.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.24 (+17.12%)</td><td>1.87 (+14.47%)</td><td>2.36 <b>(+69.82%)</b></td><td>0.33 <b>(-35.17%)</b></td><td>1.33 <b>(+52.97%)</b></td><td>3218.50 <b>(+54.24%)</b></td><td>1230.12 <b>(+36.82%)</b></td><td>444.10 <b>(-41.12%)</b></td><td>323.60 (-14.62%)</td><td>1269.93 <b>(+84.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.77 (n/a)</td><td>1.63 (n/a)</td><td>1.39 (n/a)</td><td>0.50 (n/a)</td><td>0.87 (n/a)</td><td>2086.70 (n/a)</td><td>899.06 (n/a)</td><td>754.20 (n/a)</td><td>379.00 (n/a)</td><td>687.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.65 <b>(-22.42%)</b></td><td>2.16 (-17.36%)</td><td>2.45 (-12.79%)</td><td>1.44 (+0.45%)</td><td>0.54 <b>(-27.21%)</b></td><td>730.60 (-0.44%)</td><td>514.52 (+17.29%)</td><td>428.20 (+14.68%)</td><td>395.70 <b>(+28.89%)</b></td><td>146.99 (-13.54%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>3.42 (n/a)</td><td>2.61 (n/a)</td><td>2.81 (n/a)</td><td>1.43 (n/a)</td><td>0.74 (n/a)</td><td>733.80 (n/a)</td><td>438.68 (n/a)</td><td>373.40 (n/a)</td><td>307.00 (n/a)</td><td>170.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.42 <b>(-27.01%)</b></td><td>1.75 <b>(-20.92%)</b></td><td>1.08 <b>(-46.38%)</b></td><td>0.56 (-0.35%)</td><td>1.38 <b>(-22.09%)</b></td><td>3743.40 (+0.35%)</td><td>2057.46 (+9.24%)</td><td>1937.00 <b>(+86.48%)</b></td><td>613.00 <b>(+37.01%)</b></td><td>1447.05 (-10.49%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.69 (n/a)</td><td>2.21 (n/a)</td><td>2.02 (n/a)</td><td>0.56 (n/a)</td><td>1.77 (n/a)</td><td>3730.40 (n/a)</td><td>1883.40 (n/a)</td><td>1038.70 (n/a)</td><td>447.40 (n/a)</td><td>1616.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.02 (-10.88%)</td><td>2.19 (-16.08%)</td><td>1.09 <b>(-57.54%)</b></td><td>0.59 (-6.03%)</td><td>2.03 (+2.04%)</td><td>3547.50 (+6.42%)</td><td>1997.54 <b>(+38.81%)</b></td><td>1923.70 <b>(+135.55%)</b></td><td>418.10 (+12.21%)</td><td>1523.52 <b>(+23.70%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.63 (n/a)</td><td>2.61 (n/a)</td><td>2.57 (n/a)</td><td>0.63 (n/a)</td><td>1.99 (n/a)</td><td>3333.50 (n/a)</td><td>1439.04 (n/a)</td><td>816.70 (n/a)</td><td>372.60 (n/a)</td><td>1231.58 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.01 <b>(+22.92%)</b></td><td>2.93 (-6.10%)</td><td>2.82 (-17.21%)</td><td>0.59 <b>(-61.50%)</b></td><td>1.67 <b>(+72.55%)</b></td><td>3530.20 <b>(+159.76%)</b></td><td>1226.80 <b>(+62.44%)</b></td><td>744.10 <b>(+20.80%)</b></td><td>418.60 (-18.64%)</td><td>1301.22 <b>(+277.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.08 (n/a)</td><td>3.12 (n/a)</td><td>3.40 (n/a)</td><td>1.54 (n/a)</td><td>0.97 (n/a)</td><td>1359.00 (n/a)</td><td>755.24 (n/a)</td><td>616.00 (n/a)</td><td>514.50 (n/a)</td><td>344.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>6.99 (-1.87%)</td><td>4.71 (+13.70%)</td><td>5.69 <b>(+64.82%)</b></td><td>0.85 <b>(-70.88%)</b></td><td>2.65 <b>(+51.42%)</b></td><td>2481.30 <b>(+243.43%)</b></td><td>823.30 <b>(+46.04%)</b></td><td>368.90 <b>(-39.33%)</b></td><td>299.80 (+1.90%)</td><td>938.66 <b>(+432.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>7.13 (n/a)</td><td>4.15 (n/a)</td><td>3.45 (n/a)</td><td>2.90 (n/a)</td><td>1.75 (n/a)</td><td>722.50 (n/a)</td><td>563.74 (n/a)</td><td>608.00 (n/a)</td><td>294.20 (n/a)</td><td>176.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.48 (-12.86%)</td><td>3.73 (+5.66%)</td><td>4.16 (+0.03%)</td><td>2.82 <b>(+372.95%)</b></td><td>0.80 <b>(-55.29%)</b></td><td>743.50 <b>(-78.86%)</b></td><td>586.28 <b>(-47.20%)</b></td><td>504.40 (-0.02%)</td><td>468.50 (+14.77%)</td><td>135.71 <b>(-89.94%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.14 (n/a)</td><td>3.53 (n/a)</td><td>4.16 (n/a)</td><td>0.60 (n/a)</td><td>1.79 (n/a)</td><td>3516.50 (n/a)</td><td>1110.32 (n/a)</td><td>504.50 (n/a)</td><td>408.20 (n/a)</td><td>1348.55 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.92 (-4.40%)</td><td>3.37 <b>(+38.09%)</b></td><td>3.53 <b>(+84.40%)</b></td><td>0.58 (-0.41%)</td><td>2.00 (-10.99%)</td><td>3592.00 (+0.41%)</td><td>1175.24 <b>(-28.18%)</b></td><td>593.50 <b>(-45.77%)</b></td><td>354.00 (+4.61%)</td><td>1363.35 (+3.31%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.20 (n/a)</td><td>2.44 (n/a)</td><td>1.92 (n/a)</td><td>0.59 (n/a)</td><td>2.25 (n/a)</td><td>3577.20 (n/a)</td><td>1636.40 (n/a)</td><td>1094.50 (n/a)</td><td>338.40 (n/a)</td><td>1319.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.06 (-14.11%)</td><td>4.42 <b>(+63.88%)</b></td><td>4.44 <b>(+240.05%)</b></td><td>3.98 <b>(+237.89%)</b></td><td>0.41 <b>(-80.47%)</b></td><td>1054.60 <b>(-70.40%)</b></td><td>955.44 <b>(-59.99%)</b></td><td>945.00 <b>(-70.59%)</b></td><td>829.10 (+16.45%)</td><td>85.78 <b>(-93.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.89 (n/a)</td><td>2.70 (n/a)</td><td>1.31 (n/a)</td><td>1.18 (n/a)</td><td>2.12 (n/a)</td><td>3563.30 (n/a)</td><td>2387.74 (n/a)</td><td>3213.60 (n/a)</td><td>712.00 (n/a)</td><td>1371.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.77 (-0.84%)</td><td>5.11 (-14.06%)</td><td>6.51 <b>(+30.84%)</b></td><td>1.17 <b>(-64.99%)</b></td><td>3.65 <b>(+36.45%)</b></td><td>3569.90 <b>(+185.59%)</b></td><td>1715.66 <b>(+106.64%)</b></td><td>643.90 <b>(-23.57%)</b></td><td>478.10 (+0.84%)</td><td>1595.76 <b>(+350.40%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>8.85 (n/a)</td><td>5.95 (n/a)</td><td>4.98 (n/a)</td><td>3.36 (n/a)</td><td>2.67 (n/a)</td><td>1250.00 (n/a)</td><td>830.28 (n/a)</td><td>842.50 (n/a)</td><td>474.10 (n/a)</td><td>354.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.94 (+3.69%)</td><td>7.66 <b>(+27.78%)</b></td><td>7.81 <b>(+30.15%)</b></td><td>5.97 <b>(+91.59%)</b></td><td>1.11 <b>(-44.08%)</b></td><td>702.40 <b>(-47.81%)</b></td><td>558.02 <b>(-28.73%)</b></td><td>537.20 <b>(-23.16%)</b></td><td>468.90 (-3.56%)</td><td>89.04 <b>(-73.03%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>8.63 (n/a)</td><td>5.99 (n/a)</td><td>6.00 (n/a)</td><td>3.12 (n/a)</td><td>1.99 (n/a)</td><td>1345.80 (n/a)</td><td>782.94 (n/a)</td><td>699.10 (n/a)</td><td>486.20 (n/a)</td><td>330.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>10.34 (+12.03%)</td><td>8.85 (+10.79%)</td><td>9.36 (+4.77%)</td><td>6.51 (+3.82%)</td><td>1.45 (-0.70%)</td><td>644.20 (-3.69%)</td><td>486.02 (-10.08%)</td><td>448.10 (-4.56%)</td><td>405.70 (-10.74%)</td><td>93.05 (-11.86%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>9.23 (n/a)</td><td>7.99 (n/a)</td><td>8.93 (n/a)</td><td>6.27 (n/a)</td><td>1.46 (n/a)</td><td>668.90 (n/a)</td><td>540.48 (n/a)</td><td>469.50 (n/a)</td><td>454.50 (n/a)</td><td>105.58 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>9.37 <b>(+30.26%)</b></td><td>6.07 <b>(+27.30%)</b></td><td>6.68 <b>(+55.91%)</b></td><td>3.18 <b>(+84.86%)</b></td><td>2.48 (+13.97%)</td><td>1321.00 <b>(-45.90%)</b></td><td>804.20 <b>(-29.01%)</b></td><td>627.80 <b>(-35.86%)</b></td><td>447.80 <b>(-23.23%)</b></td><td>360.69 <b>(-52.37%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>7.19 (n/a)</td><td>4.77 (n/a)</td><td>4.29 (n/a)</td><td>1.72 (n/a)</td><td>2.18 (n/a)</td><td>2442.00 (n/a)</td><td>1132.86 (n/a)</td><td>978.80 (n/a)</td><td>583.30 (n/a)</td><td>757.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.41 (-14.81%)</td><td>5.41 <b>(-29.78%)</b></td><td>6.46 (-12.09%)</td><td>1.09 <b>(-83.57%)</b></td><td>2.79 <b>(+116.93%)</b></td><td>3844.30 <b>(+508.56%)</b></td><td>1312.38 <b>(+136.45%)</b></td><td>648.80 (+13.74%)</td><td>498.70 (+17.37%)</td><td>1424.25 <b>(+1667.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>9.87 (n/a)</td><td>7.71 (n/a)</td><td>7.35 (n/a)</td><td>6.64 (n/a)</td><td>1.28 (n/a)</td><td>631.70 (n/a)</td><td>555.04 (n/a)</td><td>570.40 (n/a)</td><td>424.90 (n/a)</td><td>80.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>1.63 (+18.14%)</td><td>1.31 <b>(+23.58%)</b></td><td>1.42 <b>(+47.84%)</b></td><td>0.93 <b>(+20.10%)</b></td><td>0.30 <b>(+22.38%)</b></td><td>565.20 (-16.74%)</td><td>420.10 (-18.78%)</td><td>368.10 <b>(-32.36%)</b></td><td>321.80 (-15.34%)</td><td>103.76 (-11.56%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.38 (n/a)</td><td>1.06 (n/a)</td><td>0.96 (n/a)</td><td>0.77 (n/a)</td><td>0.24 (n/a)</td><td>678.80 (n/a)</td><td>517.24 (n/a)</td><td>544.20 (n/a)</td><td>380.10 (n/a)</td><td>117.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.70 (+7.05%)</td><td>2.05 <b>(+56.35%)</b></td><td>2.31 <b>(+45.40%)</b></td><td>0.43 <b>(+46.95%)</b></td><td>0.92 (-6.48%)</td><td>2412.80 <b>(-31.95%)</b></td><td>826.52 <b>(-51.69%)</b></td><td>454.50 <b>(-31.22%)</b></td><td>388.70 (-6.58%)</td><td>887.19 <b>(-44.31%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.52 (n/a)</td><td>1.31 (n/a)</td><td>1.59 (n/a)</td><td>0.30 (n/a)</td><td>0.98 (n/a)</td><td>3545.50 (n/a)</td><td>1710.74 (n/a)</td><td>660.80 (n/a)</td><td>416.10 (n/a)</td><td>1593.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.38 <b>(-24.93%)</b></td><td>2.11 (-8.99%)</td><td>2.35 (-4.33%)</td><td>0.60 (+7.49%)</td><td>1.12 <b>(-29.89%)</b></td><td>3499.00 (-6.97%)</td><td>1453.32 (-7.56%)</td><td>892.90 (+4.53%)</td><td>621.00 <b>(+33.20%)</b></td><td>1194.68 (-13.36%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.50 (n/a)</td><td>2.32 (n/a)</td><td>2.46 (n/a)</td><td>0.56 (n/a)</td><td>1.60 (n/a)</td><td>3761.20 (n/a)</td><td>1572.20 (n/a)</td><td>854.20 (n/a)</td><td>466.20 (n/a)</td><td>1378.94 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>1.40 (-19.29%)</td><td>0.96 (-7.91%)</td><td>0.91 (-8.08%)</td><td>0.74 (+8.44%)</td><td>0.26 <b>(-35.29%)</b></td><td>705.30 (-7.78%)</td><td>574.62 (+3.68%)</td><td>578.40 (+8.78%)</td><td>375.40 <b>(+23.89%)</b></td><td>131.33 <b>(-23.15%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.73 (n/a)</td><td>1.04 (n/a)</td><td>0.99 (n/a)</td><td>0.69 (n/a)</td><td>0.41 (n/a)</td><td>764.80 (n/a)</td><td>554.22 (n/a)</td><td>531.70 (n/a)</td><td>303.00 (n/a)</td><td>170.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 <b>(+23.05%)</b></td><td>0.09 (+8.49%)</td><td>0.07 (-16.28%)</td><td>0.07 <b>(+27.27%)</b></td><td>0.03 (+6.12%)</td><td>476.80 <b>(-21.42%)</b></td><td>378.38 (-10.43%)</td><td>442.30 (+19.44%)</td><td>226.70 (-18.75%)</td><td>108.62 <b>(-31.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>606.80 (n/a)</td><td>422.44 (n/a)</td><td>370.30 (n/a)</td><td>279.00 (n/a)</td><td>157.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (-15.19%)</td><td>0.08 (-13.37%)</td><td>0.07 (+4.38%)</td><td>0.05 <b>(-22.36%)</b></td><td>0.03 <b>(-23.19%)</b></td><td>662.00 <b>(+28.79%)</b></td><td>446.38 (+13.84%)</td><td>439.50 (-4.21%)</td><td>271.90 (+17.91%)</td><td>143.36 (+15.12%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.00 (n/a)</td><td>392.12 (n/a)</td><td>458.80 (n/a)</td><td>230.60 (n/a)</td><td>124.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.24 (-3.76%)</td><td>0.21 (+17.09%)</td><td>0.22 <b>(+48.16%)</b></td><td>0.15 (+9.09%)</td><td>0.04 <b>(-31.64%)</b></td><td>444.90 (-8.34%)</td><td>320.56 (-17.69%)</td><td>293.10 <b>(-32.50%)</b></td><td>275.60 (+3.92%)</td><td>70.94 <b>(-33.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>485.40 (n/a)</td><td>389.44 (n/a)</td><td>434.20 (n/a)</td><td>265.20 (n/a)</td><td>107.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.23 (-11.86%)</td><td>0.17 <b>(-26.53%)</b></td><td>0.17 <b>(-33.95%)</b></td><td>0.12 (-9.92%)</td><td>0.05 (-11.68%)</td><td>551.80 (+11.00%)</td><td>424.10 <b>(+36.29%)</b></td><td>396.70 <b>(+51.41%)</b></td><td>282.10 (+13.48%)</td><td>122.81 (+15.94%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>497.10 (n/a)</td><td>311.18 (n/a)</td><td>262.00 (n/a)</td><td>248.60 (n/a)</td><td>105.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.25 (-8.94%)</td><td>0.18 (-0.27%)</td><td>0.15 <b>(+20.81%)</b></td><td>0.11 (+1.26%)</td><td>0.06 <b>(-28.71%)</b></td><td>578.40 (-1.25%)</td><td>404.98 (-5.96%)</td><td>433.30 (-17.23%)</td><td>265.00 (+9.78%)</td><td>125.27 <b>(-23.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>585.70 (n/a)</td><td>430.66 (n/a)</td><td>523.50 (n/a)</td><td>241.40 (n/a)</td><td>164.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.44 (-19.94%)</td><td>0.29 <b>(-31.55%)</b></td><td>0.25 <b>(-41.28%)</b></td><td>0.07 <b>(-73.50%)</b></td><td>0.15 <b>(+36.96%)</b></td><td>1890.80 <b>(+277.25%)</b></td><td>710.22 <b>(+112.69%)</b></td><td>528.60 <b>(+70.30%)</b></td><td>296.60 <b>(+24.94%)</b></td><td>669.83 <b>(+545.77%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>501.20 (n/a)</td><td>333.92 (n/a)</td><td>310.40 (n/a)</td><td>237.40 (n/a)</td><td>103.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.63 (+10.29%)</td><td>0.29 (-13.92%)</td><td>0.27 (-5.29%)</td><td>0.06 <b>(-64.96%)</b></td><td>0.21 <b>(+41.39%)</b></td><td>2076.40 <b>(+185.34%)</b></td><td>777.54 <b>(+72.21%)</b></td><td>487.80 (+5.58%)</td><td>207.60 (-9.31%)</td><td>742.21 <b>(+303.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.57 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>727.70 (n/a)</td><td>451.50 (n/a)</td><td>462.00 (n/a)</td><td>228.90 (n/a)</td><td>184.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.53 (+8.90%)</td><td>0.32 <b>(-20.16%)</b></td><td>0.27 <b>(-36.86%)</b></td><td>0.21 <b>(-26.76%)</b></td><td>0.13 <b>(+70.31%)</b></td><td>622.00 <b>(+36.52%)</b></td><td>461.98 <b>(+35.57%)</b></td><td>487.90 <b>(+58.36%)</b></td><td>245.50 (-8.16%)</td><td>153.29 <b>(+108.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>455.60 (n/a)</td><td>340.76 (n/a)</td><td>308.10 (n/a)</td><td>267.30 (n/a)</td><td>73.46 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 <b>(-21.70%)</b></td><td>0.04 <b>(-21.85%)</b></td><td>0.04 <b>(-40.92%)</b></td><td>0.03 <b>(+48.42%)</b></td><td>0.01 <b>(-44.15%)</b></td><td>538.40 <b>(-32.62%)</b></td><td>419.80 (+8.78%)</td><td>439.90 <b>(+69.26%)</b></td><td>272.00 <b>(+27.70%)</b></td><td>118.55 <b>(-51.53%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>799.10 (n/a)</td><td>385.92 (n/a)</td><td>259.90 (n/a)</td><td>213.00 (n/a)</td><td>244.59 (n/a)</td>
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
