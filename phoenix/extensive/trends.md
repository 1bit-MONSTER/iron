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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-24.76%)</b></td><td>0.02 <b>(+22.15%)</b></td><td>0.02 <b>(+85.33%)</b></td><td>0.02 <b>(+109.75%)</b></td><td>0.00 <b>(-87.59%)</b></td><td>269.90 <b>(-52.32%)</b></td><td>253.86 <b>(-36.21%)</b></td><td>259.50 <b>(-46.04%)</b></td><td>237.60 <b>(+32.89%)</b></td><td>14.82 <b>(-92.31%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.10 (n/a)</td><td>397.96 (n/a)</td><td>480.90 (n/a)</td><td>178.80 (n/a)</td><td>192.63 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(+26.49%)</b></td><td>0.02 <b>(+22.44%)</b></td><td>0.02 <b>(+65.18%)</b></td><td>0.01 (-10.33%)</td><td>0.01 <b>(+96.36%)</b></td><td>606.20 (+11.52%)</td><td>382.40 (-10.45%)</td><td>272.90 <b>(-39.46%)</b></td><td>255.20 <b>(-20.94%)</b></td><td>164.16 <b>(+74.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.60 (n/a)</td><td>427.02 (n/a)</td><td>450.80 (n/a)</td><td>322.80 (n/a)</td><td>94.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-5.37%)</td><td>0.02 (+19.77%)</td><td>0.02 <b>(+45.59%)</b></td><td>0.01 (+6.83%)</td><td>0.00 <b>(-21.50%)</b></td><td>423.10 (-6.37%)</td><td>282.18 (-18.87%)</td><td>248.20 <b>(-31.32%)</b></td><td>237.50 (+5.65%)</td><td>79.47 <b>(-22.19%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>451.90 (n/a)</td><td>347.82 (n/a)</td><td>361.40 (n/a)</td><td>224.80 (n/a)</td><td>102.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-1.70%)</td><td>0.02 (+7.49%)</td><td>0.02 (-0.72%)</td><td>0.01 (-5.55%)</td><td>0.01 (-9.28%)</td><td>595.00 (+5.89%)</td><td>333.54 (-7.56%)</td><td>286.80 (+0.74%)</td><td>235.70 (+1.73%)</td><td>147.72 (+3.60%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.90 (n/a)</td><td>360.80 (n/a)</td><td>284.70 (n/a)</td><td>231.70 (n/a)</td><td>142.58 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(+48.89%)</b></td><td>0.02 <b>(+24.04%)</b></td><td>0.01 (+0.96%)</td><td>0.01 (-0.55%)</td><td>0.01 <b>(+151.75%)</b></td><td>611.90 (+0.54%)</td><td>408.18 (-10.95%)</td><td>427.20 (-0.95%)</td><td>234.30 <b>(-32.83%)</b></td><td>159.59 <b>(+61.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.60 (n/a)</td><td>458.36 (n/a)</td><td>431.30 (n/a)</td><td>348.80 (n/a)</td><td>98.94 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-18.16%)</td><td>0.02 <b>(-23.93%)</b></td><td>0.02 (-19.94%)</td><td>0.01 <b>(-35.38%)</b></td><td>0.01 <b>(+28.66%)</b></td><td>571.00 <b>(+54.74%)</b></td><td>399.98 <b>(+40.69%)</b></td><td>353.60 <b>(+24.90%)</b></td><td>265.30 <b>(+22.20%)</b></td><td>143.13 <b>(+145.20%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>369.00 (n/a)</td><td>284.30 (n/a)</td><td>283.10 (n/a)</td><td>217.10 (n/a)</td><td>58.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-18.94%)</td><td>0.04 <b>(-20.49%)</b></td><td>0.04 (-15.61%)</td><td>0.02 <b>(-54.76%)</b></td><td>0.02 <b>(+20.40%)</b></td><td>564.50 <b>(+121.03%)</b></td><td>316.86 <b>(+38.10%)</b></td><td>290.90 (+18.49%)</td><td>195.40 <b>(+23.36%)</b></td><td>144.11 <b>(+259.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>255.40 (n/a)</td><td>229.44 (n/a)</td><td>245.50 (n/a)</td><td>158.40 (n/a)</td><td>40.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 <b>(+39.31%)</b></td><td>0.04 (+4.90%)</td><td>0.04 (-17.61%)</td><td>0.02 (+1.20%)</td><td>0.02 <b>(+41.02%)</b></td><td>569.00 (-1.18%)</td><td>346.48 (+0.77%)</td><td>296.80 <b>(+21.39%)</b></td><td>165.50 <b>(-28.20%)</b></td><td>165.30 (+7.14%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.80 (n/a)</td><td>343.84 (n/a)</td><td>244.50 (n/a)</td><td>230.50 (n/a)</td><td>154.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (-7.74%)</td><td>0.04 (+3.53%)</td><td>0.04 <b>(+28.89%)</b></td><td>0.02 (+15.74%)</td><td>0.01 (-15.96%)</td><td>518.40 (-13.60%)</td><td>370.18 (-7.69%)</td><td>348.70 <b>(-22.41%)</b></td><td>229.50 (+8.41%)</td><td>138.87 (-16.58%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>600.00 (n/a)</td><td>401.00 (n/a)</td><td>449.40 (n/a)</td><td>211.70 (n/a)</td><td>166.46 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (+17.57%)</td><td>0.04 (+4.85%)</td><td>0.04 (-4.76%)</td><td>0.02 (+9.97%)</td><td>0.02 (+14.58%)</td><td>578.10 (-9.08%)</td><td>369.16 (-3.93%)</td><td>290.00 (+5.00%)</td><td>168.00 (-14.94%)</td><td>191.72 (-6.94%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>635.80 (n/a)</td><td>384.28 (n/a)</td><td>276.20 (n/a)</td><td>197.50 (n/a)</td><td>206.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (+5.62%)</td><td>0.04 (-0.10%)</td><td>0.03 (-19.70%)</td><td>0.02 (+11.76%)</td><td>0.02 (-1.58%)</td><td>514.90 (-10.53%)</td><td>372.62 (-3.21%)</td><td>365.00 <b>(+24.53%)</b></td><td>205.00 (-5.36%)</td><td>138.77 <b>(-20.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>575.50 (n/a)</td><td>384.98 (n/a)</td><td>293.10 (n/a)</td><td>216.60 (n/a)</td><td>174.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 <b>(+21.36%)</b></td><td>0.04 <b>(+65.30%)</b></td><td>0.04 <b>(+109.35%)</b></td><td>0.02 <b>(+174.69%)</b></td><td>0.01 <b>(-23.78%)</b></td><td>502.80 <b>(-63.59%)</b></td><td>320.00 <b>(-56.48%)</b></td><td>298.40 <b>(-52.23%)</b></td><td>205.20 (-17.59%)</td><td>114.90 <b>(-76.69%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1381.10 (n/a)</td><td>735.36 (n/a)</td><td>624.70 (n/a)</td><td>249.00 (n/a)</td><td>492.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (+19.28%)</td><td>0.08 (-9.34%)</td><td>0.05 <b>(-46.90%)</b></td><td>0.03 <b>(-32.39%)</b></td><td>0.04 <b>(+60.22%)</b></td><td>757.70 <b>(+47.90%)</b></td><td>417.22 <b>(+30.45%)</b></td><td>465.60 <b>(+88.35%)</b></td><td>185.40 (-16.15%)</td><td>232.78 <b>(+85.88%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>512.30 (n/a)</td><td>319.82 (n/a)</td><td>247.20 (n/a)</td><td>221.10 (n/a)</td><td>125.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (+8.86%)</td><td>0.09 (+4.63%)</td><td>0.10 (+0.44%)</td><td>0.05 (-6.61%)</td><td>0.03 (+7.60%)</td><td>504.60 (+7.07%)</td><td>317.46 (-3.33%)</td><td>248.30 (-0.44%)</td><td>228.20 (-8.13%)</td><td>118.64 (+7.83%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>471.30 (n/a)</td><td>328.40 (n/a)</td><td>249.40 (n/a)</td><td>248.40 (n/a)</td><td>110.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (-6.27%)</td><td>0.07 (-7.48%)</td><td>0.07 <b>(-29.05%)</b></td><td>0.05 <b>(+270.31%)</b></td><td>0.02 <b>(-48.76%)</b></td><td>539.50 <b>(-73.00%)</b></td><td>393.78 <b>(-39.08%)</b></td><td>376.40 <b>(+40.92%)</b></td><td>246.70 (+6.66%)</td><td>109.55 <b>(-85.64%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1998.00 (n/a)</td><td>646.34 (n/a)</td><td>267.10 (n/a)</td><td>231.30 (n/a)</td><td>763.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (+1.81%)</td><td>0.06 (-19.70%)</td><td>0.05 <b>(-44.08%)</b></td><td>0.04 <b>(+59.23%)</b></td><td>0.03 (-16.39%)</td><td>679.00 <b>(-37.19%)</b></td><td>479.02 (+6.51%)</td><td>477.10 <b>(+78.82%)</b></td><td>242.00 (-1.79%)</td><td>196.34 <b>(-45.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1081.10 (n/a)</td><td>449.74 (n/a)</td><td>266.80 (n/a)</td><td>246.40 (n/a)</td><td>359.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 <b>(+38.15%)</b></td><td>0.06 (+1.52%)</td><td>0.04 <b>(-32.14%)</b></td><td>0.04 <b>(+53.22%)</b></td><td>0.03 <b>(+32.37%)</b></td><td>625.80 <b>(-34.74%)</b></td><td>497.76 (-4.54%)</td><td>578.70 <b>(+47.36%)</b></td><td>212.80 <b>(-27.62%)</b></td><td>170.35 <b>(-38.98%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>958.90 (n/a)</td><td>521.44 (n/a)</td><td>392.70 (n/a)</td><td>294.00 (n/a)</td><td>279.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 <b>(-29.04%)</b></td><td>0.06 <b>(-32.14%)</b></td><td>0.05 <b>(-46.66%)</b></td><td>0.04 (-3.07%)</td><td>0.03 <b>(-35.44%)</b></td><td>569.30 (+3.17%)</td><td>464.06 <b>(+37.21%)</b></td><td>524.80 <b>(+87.43%)</b></td><td>227.30 <b>(+40.92%)</b></td><td>140.84 (-11.56%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>551.80 (n/a)</td><td>338.20 (n/a)</td><td>280.00 (n/a)</td><td>161.30 (n/a)</td><td>159.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.25 (+17.01%)</td><td>0.14 (-19.43%)</td><td>0.12 <b>(-35.29%)</b></td><td>0.08 (-11.43%)</td><td>0.06 <b>(+38.58%)</b></td><td>626.00 (+12.89%)</td><td>414.96 <b>(+29.83%)</b></td><td>418.80 <b>(+54.54%)</b></td><td>198.60 (-14.54%)</td><td>152.85 (+15.49%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>554.50 (n/a)</td><td>319.62 (n/a)</td><td>271.00 (n/a)</td><td>232.40 (n/a)</td><td>132.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.22 (+11.88%)</td><td>0.13 <b>(-21.38%)</b></td><td>0.10 <b>(-46.16%)</b></td><td>0.09 <b>(-25.48%)</b></td><td>0.06 <b>(+79.84%)</b></td><td>569.80 <b>(+34.20%)</b></td><td>424.82 <b>(+40.05%)</b></td><td>502.50 <b>(+85.70%)</b></td><td>224.20 (-10.64%)</td><td>153.11 <b>(+115.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>424.60 (n/a)</td><td>303.34 (n/a)</td><td>270.60 (n/a)</td><td>250.90 (n/a)</td><td>71.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 <b>(-21.66%)</b></td><td>0.11 <b>(-37.36%)</b></td><td>0.09 <b>(-48.30%)</b></td><td>0.07 <b>(-27.37%)</b></td><td>0.04 (-19.58%)</td><td>727.70 <b>(+37.67%)</b></td><td>516.20 <b>(+60.87%)</b></td><td>540.80 <b>(+93.42%)</b></td><td>272.50 <b>(+27.63%)</b></td><td>172.58 <b>(+35.28%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>528.60 (n/a)</td><td>320.88 (n/a)</td><td>279.60 (n/a)</td><td>213.50 (n/a)</td><td>127.57 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.22 (+5.26%)</td><td>0.14 (-8.97%)</td><td>0.10 <b>(-48.70%)</b></td><td>0.09 <b>(+285.83%)</b></td><td>0.06 <b>(-31.74%)</b></td><td>553.20 <b>(-74.08%)</b></td><td>409.24 <b>(-38.41%)</b></td><td>486.20 <b>(+94.95%)</b></td><td>222.10 (-5.00%)</td><td>141.79 <b>(-82.87%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2134.50 (n/a)</td><td>664.44 (n/a)</td><td>249.40 (n/a)</td><td>233.80 (n/a)</td><td>827.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 (-4.15%)</td><td>0.14 <b>(+24.21%)</b></td><td>0.15 <b>(+71.23%)</b></td><td>0.09 (+13.72%)</td><td>0.04 (-8.56%)</td><td>522.20 (-12.06%)</td><td>380.14 <b>(-20.86%)</b></td><td>321.00 <b>(-41.60%)</b></td><td>266.50 (+4.35%)</td><td>123.63 (-11.64%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>593.80 (n/a)</td><td>480.34 (n/a)</td><td>549.70 (n/a)</td><td>255.40 (n/a)</td><td>139.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 (-12.20%)</td><td>0.09 <b>(-31.52%)</b></td><td>0.08 <b>(-32.08%)</b></td><td>0.02 <b>(-77.14%)</b></td><td>0.06 <b>(+32.67%)</b></td><td>2507.70 <b>(+337.49%)</b></td><td>970.14 <b>(+128.90%)</b></td><td>586.50 <b>(+47.25%)</b></td><td>278.40 (+13.87%)</td><td>899.33 <b>(+617.82%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>573.20 (n/a)</td><td>423.82 (n/a)</td><td>398.30 (n/a)</td><td>244.50 (n/a)</td><td>125.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (-1.03%)</td><td>0.01 (+1.31%)</td><td>0.01 (+1.22%)</td><td>0.01 (+5.06%)</td><td>0.00 (-4.95%)</td><td>449.60 (-4.81%)</td><td>302.26 (-2.05%)</td><td>275.70 (-1.18%)</td><td>236.60 (+1.02%)</td><td>84.74 (-9.70%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.30 (n/a)</td><td>308.58 (n/a)</td><td>279.00 (n/a)</td><td>234.20 (n/a)</td><td>93.85 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (+11.31%)</td><td>0.01 (-7.61%)</td><td>0.01 (-6.32%)</td><td>0.00 <b>(-62.38%)</b></td><td>0.00 <b>(+50.92%)</b></td><td>1912.30 <b>(+165.78%)</b></td><td>728.86 <b>(+51.85%)</b></td><td>517.90 (+6.76%)</td><td>257.00 (-10.17%)</td><td>670.77 <b>(+311.09%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>719.50 (n/a)</td><td>479.98 (n/a)</td><td>485.10 (n/a)</td><td>286.10 (n/a)</td><td>163.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (-1.64%)</td><td>0.01 (-10.52%)</td><td>0.01 <b>(-28.50%)</b></td><td>0.00 (-13.28%)</td><td>0.00 (-3.39%)</td><td>594.00 (+15.32%)</td><td>388.20 (+12.37%)</td><td>420.80 <b>(+39.85%)</b></td><td>224.60 (+1.63%)</td><td>151.97 (+9.85%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.10 (n/a)</td><td>345.48 (n/a)</td><td>300.90 (n/a)</td><td>221.00 (n/a)</td><td>138.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (-18.03%)</td><td>0.01 <b>(-25.42%)</b></td><td>0.01 <b>(-27.70%)</b></td><td>0.00 (+7.79%)</td><td>0.00 <b>(-31.33%)</b></td><td>603.70 (-7.22%)</td><td>477.36 <b>(+26.95%)</b></td><td>471.30 <b>(+38.33%)</b></td><td>296.60 <b>(+22.01%)</b></td><td>118.20 <b>(-26.98%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>650.70 (n/a)</td><td>376.02 (n/a)</td><td>340.70 (n/a)</td><td>243.10 (n/a)</td><td>161.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (-8.89%)</td><td>0.01 (+9.72%)</td><td>0.01 (+3.29%)</td><td>0.00 <b>(+261.81%)</b></td><td>0.00 <b>(-47.70%)</b></td><td>541.60 <b>(-72.36%)</b></td><td>441.40 <b>(-42.20%)</b></td><td>485.10 (-3.17%)</td><td>276.40 (+9.73%)</td><td>112.47 <b>(-83.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1959.70 (n/a)</td><td>763.66 (n/a)</td><td>501.00 (n/a)</td><td>251.90 (n/a)</td><td>702.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(-30.67%)</b></td><td>0.01 (-17.74%)</td><td>0.01 (-17.83%)</td><td>0.00 (+3.59%)</td><td>0.00 <b>(-53.13%)</b></td><td>542.80 (-3.47%)</td><td>472.60 (+15.15%)</td><td>520.70 <b>(+21.72%)</b></td><td>364.90 <b>(+44.23%)</b></td><td>82.37 <b>(-33.13%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>562.30 (n/a)</td><td>410.42 (n/a)</td><td>427.80 (n/a)</td><td>253.00 (n/a)</td><td>123.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+4.14%)</td><td>0.01 (-17.16%)</td><td>0.01 <b>(-27.29%)</b></td><td>0.01 <b>(-22.95%)</b></td><td>0.00 <b>(+39.64%)</b></td><td>613.50 <b>(+29.79%)</b></td><td>451.32 <b>(+24.63%)</b></td><td>470.80 <b>(+37.54%)</b></td><td>296.90 (-3.98%)</td><td>115.72 <b>(+71.20%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.70 (n/a)</td><td>362.12 (n/a)</td><td>342.30 (n/a)</td><td>309.20 (n/a)</td><td>67.59 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+1.11%)</td><td>0.02 (+2.72%)</td><td>0.02 (-2.17%)</td><td>0.01 (+16.60%)</td><td>0.00 (-14.46%)</td><td>406.50 (-14.24%)</td><td>283.50 (-5.08%)</td><td>268.50 (+2.21%)</td><td>229.20 (-1.08%)</td><td>71.45 <b>(-28.46%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.00 (n/a)</td><td>298.66 (n/a)</td><td>262.70 (n/a)</td><td>231.70 (n/a)</td><td>99.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-15.23%)</td><td>0.02 <b>(-22.22%)</b></td><td>0.02 (-16.38%)</td><td>0.01 <b>(-42.06%)</b></td><td>0.01 <b>(+55.26%)</b></td><td>500.00 <b>(+72.59%)</b></td><td>351.76 <b>(+38.34%)</b></td><td>312.70 (+19.58%)</td><td>232.30 (+17.98%)</td><td>120.53 <b>(+223.97%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>289.70 (n/a)</td><td>254.28 (n/a)</td><td>261.50 (n/a)</td><td>196.90 (n/a)</td><td>37.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-4.05%)</td><td>0.01 (-0.42%)</td><td>0.02 (-5.93%)</td><td>0.00 (+15.21%)</td><td>0.01 (+0.29%)</td><td>2087.30 (-13.20%)</td><td>686.66 (-7.48%)</td><td>307.90 (+6.32%)</td><td>251.80 (+4.22%)</td><td>791.18 (-15.32%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2404.80 (n/a)</td><td>742.18 (n/a)</td><td>289.60 (n/a)</td><td>241.60 (n/a)</td><td>934.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+10.46%)</td><td>0.02 (+13.43%)</td><td>0.01 (-13.38%)</td><td>0.01 <b>(+105.33%)</b></td><td>0.01 (-4.96%)</td><td>553.70 <b>(-51.30%)</b></td><td>388.70 <b>(-24.39%)</b></td><td>441.00 (+15.45%)</td><td>244.50 (-9.48%)</td><td>134.16 <b>(-62.50%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1137.00 (n/a)</td><td>514.10 (n/a)</td><td>382.00 (n/a)</td><td>270.10 (n/a)</td><td>357.72 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+17.95%)</td><td>0.01 (+16.54%)</td><td>0.01 (+6.71%)</td><td>0.01 <b>(+66.70%)</b></td><td>0.00 (+0.47%)</td><td>589.80 <b>(-40.02%)</b></td><td>466.74 <b>(-20.56%)</b></td><td>488.50 (-6.27%)</td><td>257.60 (-15.21%)</td><td>127.48 <b>(-52.06%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>983.30 (n/a)</td><td>587.54 (n/a)</td><td>521.20 (n/a)</td><td>303.80 (n/a)</td><td>265.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (-17.16%)</td><td>0.03 <b>(-24.12%)</b></td><td>0.02 <b>(-35.70%)</b></td><td>0.02 (-9.04%)</td><td>0.01 (-5.28%)</td><td>618.80 (+9.95%)</td><td>445.40 <b>(+32.99%)</b></td><td>472.70 <b>(+55.54%)</b></td><td>288.40 <b>(+20.72%)</b></td><td>151.25 (+14.76%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>562.80 (n/a)</td><td>334.90 (n/a)</td><td>303.90 (n/a)</td><td>238.90 (n/a)</td><td>131.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (-7.91%)</td><td>0.03 (-8.83%)</td><td>0.02 (+0.41%)</td><td>0.02 (-0.31%)</td><td>0.01 <b>(-27.00%)</b></td><td>602.90 (+0.30%)</td><td>439.86 (+3.08%)</td><td>447.70 (-0.40%)</td><td>258.40 (+8.57%)</td><td>125.02 <b>(-24.58%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.10 (n/a)</td><td>426.72 (n/a)</td><td>449.50 (n/a)</td><td>238.00 (n/a)</td><td>165.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (+6.67%)</td><td>0.03 (+13.25%)</td><td>0.04 <b>(+90.81%)</b></td><td>0.01 <b>(-65.34%)</b></td><td>0.02 <b>(+44.41%)</b></td><td>1915.60 <b>(+188.49%)</b></td><td>623.46 <b>(+45.22%)</b></td><td>238.40 <b>(-47.59%)</b></td><td>219.20 (-6.24%)</td><td>732.06 <b>(+304.55%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>664.00 (n/a)</td><td>429.32 (n/a)</td><td>454.90 (n/a)</td><td>233.80 (n/a)</td><td>180.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 <b>(+22.74%)</b></td><td>0.03 (+17.73%)</td><td>0.03 <b>(+75.07%)</b></td><td>0.00 <b>(-78.02%)</b></td><td>0.01 <b>(+133.32%)</b></td><td>2437.20 <b>(+354.96%)</b></td><td>742.28 <b>(+61.06%)</b></td><td>301.80 <b>(-42.88%)</b></td><td>254.20 (-18.53%)</td><td>949.47 <b>(+825.94%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.70 (n/a)</td><td>460.86 (n/a)</td><td>528.40 (n/a)</td><td>312.00 (n/a)</td><td>102.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (+9.18%)</td><td>0.03 (+10.16%)</td><td>0.02 (+4.52%)</td><td>0.02 <b>(+306.17%)</b></td><td>0.01 <b>(-20.65%)</b></td><td>609.10 <b>(-75.38%)</b></td><td>452.82 <b>(-44.50%)</b></td><td>465.10 (-4.32%)</td><td>240.90 (-8.40%)</td><td>149.43 <b>(-83.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2474.00 (n/a)</td><td>815.94 (n/a)</td><td>486.10 (n/a)</td><td>263.00 (n/a)</td><td>933.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (+4.06%)</td><td>0.03 (+7.32%)</td><td>0.03 (+11.81%)</td><td>0.01 <b>(+40.60%)</b></td><td>0.01 (+2.01%)</td><td>1364.60 <b>(-28.88%)</b></td><td>567.60 (-17.94%)</td><td>409.60 (-10.57%)</td><td>279.30 (-3.92%)</td><td>453.39 <b>(-34.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1918.70 (n/a)</td><td>691.70 (n/a)</td><td>458.00 (n/a)</td><td>290.70 (n/a)</td><td>689.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (-17.92%)</td><td>0.06 (-2.30%)</td><td>0.05 (+0.81%)</td><td>0.03 <b>(+36.62%)</b></td><td>0.02 <b>(-26.34%)</b></td><td>625.70 <b>(-26.80%)</b></td><td>414.06 (-8.97%)</td><td>455.20 (-0.81%)</td><td>255.30 <b>(+21.86%)</b></td><td>158.10 <b>(-37.98%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>854.80 (n/a)</td><td>454.88 (n/a)</td><td>458.90 (n/a)</td><td>209.50 (n/a)</td><td>254.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 <b>(-28.64%)</b></td><td>0.05 <b>(-27.41%)</b></td><td>0.05 <b>(-34.31%)</b></td><td>0.03 (-8.92%)</td><td>0.02 <b>(-38.89%)</b></td><td>627.40 (+9.80%)</td><td>427.04 <b>(+30.49%)</b></td><td>433.30 <b>(+52.20%)</b></td><td>276.10 <b>(+40.08%)</b></td><td>130.51 (-10.21%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>571.40 (n/a)</td><td>327.26 (n/a)</td><td>284.70 (n/a)</td><td>197.10 (n/a)</td><td>145.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (+16.00%)</td><td>0.06 <b>(+44.55%)</b></td><td>0.07 <b>(+49.34%)</b></td><td>0.04 <b>(+381.98%)</b></td><td>0.02 <b>(-25.50%)</b></td><td>507.80 <b>(-79.25%)</b></td><td>357.36 <b>(-56.63%)</b></td><td>299.60 <b>(-33.05%)</b></td><td>259.50 (-13.82%)</td><td>104.17 <b>(-88.55%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2447.40 (n/a)</td><td>824.02 (n/a)</td><td>447.50 (n/a)</td><td>301.10 (n/a)</td><td>910.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 <b>(-38.96%)</b></td><td>0.04 <b>(-34.20%)</b></td><td>0.04 <b>(-41.90%)</b></td><td>0.02 <b>(-41.62%)</b></td><td>0.01 <b>(-40.64%)</b></td><td>1068.30 <b>(+71.28%)</b></td><td>589.24 <b>(+52.62%)</b></td><td>501.50 <b>(+72.10%)</b></td><td>431.40 <b>(+63.84%)</b></td><td>270.31 <b>(+74.69%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.70 (n/a)</td><td>386.08 (n/a)</td><td>291.40 (n/a)</td><td>263.30 (n/a)</td><td>154.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (+15.59%)</td><td>0.06 (+8.51%)</td><td>0.05 (-2.10%)</td><td>0.03 (-2.75%)</td><td>0.02 <b>(+41.83%)</b></td><td>613.10 (+2.83%)</td><td>398.72 (-2.92%)</td><td>381.80 (+2.14%)</td><td>246.80 (-13.46%)</td><td>160.43 <b>(+20.27%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>596.20 (n/a)</td><td>410.70 (n/a)</td><td>373.80 (n/a)</td><td>285.20 (n/a)</td><td>133.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (+0.55%)</td><td>0.06 <b>(+22.41%)</b></td><td>0.07 <b>(+42.30%)</b></td><td>0.04 <b>(+25.14%)</b></td><td>0.02 (+1.16%)</td><td>559.70 <b>(-20.10%)</b></td><td>354.76 (-19.63%)</td><td>299.80 <b>(-29.72%)</b></td><td>252.00 (-0.55%)</td><td>128.92 <b>(-21.03%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>700.50 (n/a)</td><td>441.42 (n/a)</td><td>426.60 (n/a)</td><td>253.40 (n/a)</td><td>163.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.10 (n/a)</td><td>357.10 (n/a)</td><td>286.10 (n/a)</td><td>274.80 (n/a)</td><td>107.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.10 (n/a)</td><td>469.74 (n/a)</td><td>476.70 (n/a)</td><td>281.40 (n/a)</td><td>123.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>632.00 (n/a)</td><td>518.92 (n/a)</td><td>511.20 (n/a)</td><td>430.00 (n/a)</td><td>72.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.30 (n/a)</td><td>362.82 (n/a)</td><td>259.40 (n/a)</td><td>250.10 (n/a)</td><td>159.79 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>626.90 (n/a)</td><td>423.22 (n/a)</td><td>485.00 (n/a)</td><td>201.90 (n/a)</td><td>171.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.30 (n/a)</td><td>471.72 (n/a)</td><td>501.90 (n/a)</td><td>224.20 (n/a)</td><td>146.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1900.80 (n/a)</td><td>660.66 (n/a)</td><td>362.20 (n/a)</td><td>280.90 (n/a)</td><td>695.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>679.60 (n/a)</td><td>471.20 (n/a)</td><td>460.80 (n/a)</td><td>247.80 (n/a)</td><td>155.40 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2367.20 (n/a)</td><td>1143.56 (n/a)</td><td>532.90 (n/a)</td><td>247.50 (n/a)</td><td>995.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.21 (+14.70%)</td><td>0.12 (-7.69%)</td><td>0.10 (-12.98%)</td><td>0.03 <b>(-70.01%)</b></td><td>0.07 <b>(+86.15%)</b></td><td>1940.10 <b>(+233.41%)</b></td><td>706.30 <b>(+71.07%)</b></td><td>511.50 (+14.92%)</td><td>238.60 (-12.82%)</td><td>704.13 <b>(+470.72%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>581.90 (n/a)</td><td>412.88 (n/a)</td><td>445.10 (n/a)</td><td>273.70 (n/a)</td><td>123.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>746.10 (n/a)</td><td>483.00 (n/a)</td><td>472.70 (n/a)</td><td>231.30 (n/a)</td><td>183.11 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>550.00 (n/a)</td><td>417.72 (n/a)</td><td>412.50 (n/a)</td><td>290.50 (n/a)</td><td>128.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.10 (n/a)</td><td>385.36 (n/a)</td><td>453.10 (n/a)</td><td>166.20 (n/a)</td><td>174.98 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.50 (n/a)</td><td>385.70 (n/a)</td><td>331.50 (n/a)</td><td>214.40 (n/a)</td><td>162.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.50 (n/a)</td><td>436.44 (n/a)</td><td>448.20 (n/a)</td><td>309.50 (n/a)</td><td>83.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>424.00 (n/a)</td><td>285.26 (n/a)</td><td>247.70 (n/a)</td><td>239.70 (n/a)</td><td>78.63 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2499.70 (n/a)</td><td>871.62 (n/a)</td><td>546.20 (n/a)</td><td>244.70 (n/a)</td><td>919.45 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.90 (n/a)</td><td>383.84 (n/a)</td><td>332.50 (n/a)</td><td>289.60 (n/a)</td><td>126.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>538.70 (n/a)</td><td>304.28 (n/a)</td><td>250.10 (n/a)</td><td>220.90 (n/a)</td><td>131.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>521.50 (n/a)</td><td>311.24 (n/a)</td><td>245.30 (n/a)</td><td>238.70 (n/a)</td><td>121.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1923.10 (n/a)</td><td>715.50 (n/a)</td><td>516.80 (n/a)</td><td>289.10 (n/a)</td><td>685.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>589.70 (n/a)</td><td>353.30 (n/a)</td><td>255.30 (n/a)</td><td>235.60 (n/a)</td><td>155.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>533.00 (n/a)</td><td>348.28 (n/a)</td><td>321.70 (n/a)</td><td>249.10 (n/a)</td><td>109.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>469.60 (n/a)</td><td>335.68 (n/a)</td><td>314.70 (n/a)</td><td>253.90 (n/a)</td><td>89.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.50 (n/a)</td><td>350.96 (n/a)</td><td>273.90 (n/a)</td><td>192.30 (n/a)</td><td>148.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.70 (n/a)</td><td>367.98 (n/a)</td><td>348.50 (n/a)</td><td>217.00 (n/a)</td><td>137.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.40 (n/a)</td><td>501.44 (n/a)</td><td>595.80 (n/a)</td><td>155.80 (n/a)</td><td>206.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.80 (n/a)</td><td>476.28 (n/a)</td><td>488.40 (n/a)</td><td>334.20 (n/a)</td><td>85.58 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.50 (n/a)</td><td>422.48 (n/a)</td><td>451.40 (n/a)</td><td>241.80 (n/a)</td><td>132.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.60 (n/a)</td><td>423.50 (n/a)</td><td>363.30 (n/a)</td><td>283.50 (n/a)</td><td>155.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.00 (n/a)</td><td>334.26 (n/a)</td><td>290.80 (n/a)</td><td>231.50 (n/a)</td><td>99.90 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1954.70 (n/a)</td><td>639.36 (n/a)</td><td>378.00 (n/a)</td><td>226.10 (n/a)</td><td>739.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.20 (n/a)</td><td>460.00 (n/a)</td><td>497.90 (n/a)</td><td>316.50 (n/a)</td><td>123.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>432.60 (n/a)</td><td>338.00 (n/a)</td><td>331.70 (n/a)</td><td>254.20 (n/a)</td><td>65.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>791.40 (n/a)</td><td>541.38 (n/a)</td><td>528.70 (n/a)</td><td>373.00 (n/a)</td><td>154.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>572.50 (n/a)</td><td>423.74 (n/a)</td><td>478.90 (n/a)</td><td>277.90 (n/a)</td><td>125.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1908.20 (n/a)</td><td>727.78 (n/a)</td><td>524.40 (n/a)</td><td>186.20 (n/a)</td><td>696.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>674.20 (n/a)</td><td>457.68 (n/a)</td><td>491.70 (n/a)</td><td>252.80 (n/a)</td><td>193.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>400.80 (n/a)</td><td>277.06 (n/a)</td><td>263.50 (n/a)</td><td>225.40 (n/a)</td><td>71.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.90 (n/a)</td><td>455.16 (n/a)</td><td>473.70 (n/a)</td><td>219.60 (n/a)</td><td>139.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>503.86 (n/a)</td><td>550.30 (n/a)</td><td>310.90 (n/a)</td><td>115.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1124.60 (n/a)</td><td>629.42 (n/a)</td><td>344.60 (n/a)</td><td>311.60 (n/a)</td><td>411.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>635.30 (n/a)</td><td>413.04 (n/a)</td><td>338.50 (n/a)</td><td>307.70 (n/a)</td><td>135.48 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>579.40 (n/a)</td><td>476.76 (n/a)</td><td>514.60 (n/a)</td><td>306.90 (n/a)</td><td>112.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>576.00 (n/a)</td><td>434.54 (n/a)</td><td>478.50 (n/a)</td><td>278.20 (n/a)</td><td>140.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>952.80 (n/a)</td><td>560.70 (n/a)</td><td>548.60 (n/a)</td><td>314.50 (n/a)</td><td>239.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>471.90 (n/a)</td><td>423.68 (n/a)</td><td>469.80 (n/a)</td><td>237.40 (n/a)</td><td>104.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.49 (-13.70%)</td><td>0.39 <b>(-20.80%)</b></td><td>0.35 <b>(-34.84%)</b></td><td>0.32 (-10.18%)</td><td>0.08 (-9.02%)</td><td>692.90 (+11.33%)</td><td>582.60 <b>(+26.55%)</b></td><td>625.40 <b>(+53.47%)</b></td><td>449.10 (+15.90%)</td><td>116.80 (+17.31%)</td><td>21.02 (-13.70%)</td><td>16.77 <b>(-20.80%)</b></td><td>15.09 <b>(-34.84%)</b></td><td>13.62 (-10.18%)</td><td>3.57 (-9.02%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.09 (n/a)</td><td>622.40 (n/a)</td><td>460.38 (n/a)</td><td>407.50 (n/a)</td><td>387.50 (n/a)</td><td>99.56 (n/a)</td><td>24.35 (n/a)</td><td>21.17 (n/a)</td><td>23.16 (n/a)</td><td>15.16 (n/a)</td><td>3.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.57 (-6.45%)</td><td>0.43 (-1.46%)</td><td>0.38 (+4.57%)</td><td>0.35 (+1.08%)</td><td>0.09 <b>(-24.27%)</b></td><td>639.60 (-1.08%)</td><td>527.28 (-0.90%)</td><td>578.20 (-4.38%)</td><td>387.80 (+6.89%)</td><td>104.89 <b>(-22.01%)</b></td><td>24.33 (-6.45%)</td><td>18.53 (-1.46%)</td><td>16.32 (+4.57%)</td><td>14.75 (+1.08%)</td><td>4.02 <b>(-24.27%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.61 (n/a)</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>646.60 (n/a)</td><td>532.06 (n/a)</td><td>604.70 (n/a)</td><td>362.80 (n/a)</td><td>134.48 (n/a)</td><td>26.01 (n/a)</td><td>18.81 (n/a)</td><td>15.61 (n/a)</td><td>14.60 (n/a)</td><td>5.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.31 (-0.92%)</td><td>0.30 (-1.33%)</td><td>0.31 (-0.79%)</td><td>0.30 (-2.23%)</td><td>0.00 <b>(+35.30%)</b></td><td>84988.20 (+2.28%)</td><td>82823.00 (+1.36%)</td><td>82271.30 (+0.80%)</td><td>81542.50 (+0.93%)</td><td>1363.78 <b>(+40.08%)</b></td><td>210.69 (-0.92%)</td><td>207.47 (-1.33%)</td><td>208.82 (-0.79%)</td><td>202.14 (-2.23%)</td><td>3.38 <b>(+35.30%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83093.10 (n/a)</td><td>81709.36 (n/a)</td><td>81620.70 (n/a)</td><td>80794.60 (n/a)</td><td>973.57 (n/a)</td><td>212.64 (n/a)</td><td>210.28 (n/a)</td><td>210.48 (n/a)</td><td>206.75 (n/a)</td><td>2.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>1.03 (-0.73%)</td><td>1.00 (-1.87%)</td><td>1.01 (-0.04%)</td><td>0.96 (-4.24%)</td><td>0.03 <b>(+99.23%)</b></td><td>26139.40 (+4.43%)</td><td>25206.74 (+1.96%)</td><td>24823.10 (+0.04%)</td><td>24536.30 (+0.74%)</td><td>692.30 <b>(+109.80%)</b></td><td>700.18 (-0.73%)</td><td>681.97 (-1.87%)</td><td>692.09 (-0.04%)</td><td>657.24 (-4.24%)</td><td>18.53 <b>(+99.23%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.01 (n/a)</td><td>25031.70 (n/a)</td><td>24723.36 (n/a)</td><td>24812.50 (n/a)</td><td>24357.10 (n/a)</td><td>329.98 (n/a)</td><td>705.33 (n/a)</td><td>694.98 (n/a)</td><td>692.39 (n/a)</td><td>686.32 (n/a)</td><td>9.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.82 (-0.08%)</td><td>0.81 (+0.35%)</td><td>0.81 (+0.29%)</td><td>0.79 (+2.02%)</td><td>0.01 <b>(-36.54%)</b></td><td>94985.50 (-1.98%)</td><td>93781.50 (-0.37%)</td><td>93734.60 (-0.29%)</td><td>92533.90 (+0.08%)</td><td>1084.22 <b>(-37.79%)</b></td><td>742.64 (-0.08%)</td><td>732.84 (+0.35%)</td><td>733.13 (+0.29%)</td><td>723.47 (+2.02%)</td><td>8.47 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96908.60 (n/a)</td><td>94128.12 (n/a)</td><td>94004.00 (n/a)</td><td>92457.40 (n/a)</td><td>1742.76 (n/a)</td><td>743.26 (n/a)</td><td>730.26 (n/a)</td><td>731.03 (n/a)</td><td>709.12 (n/a)</td><td>13.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.77 (+0.27%)</td><td>0.76 (+1.19%)</td><td>0.76 (+1.53%)</td><td>0.75 (+2.30%)</td><td>0.01 <b>(-38.85%)</b></td><td>100599.40 (-2.25%)</td><td>99067.64 (-1.20%)</td><td>99451.80 (-1.51%)</td><td>97475.30 (-0.27%)</td><td>1278.53 <b>(-40.30%)</b></td><td>704.99 (+0.27%)</td><td>693.75 (+1.19%)</td><td>690.98 (+1.53%)</td><td>683.10 (+2.30%)</td><td>8.97 <b>(-38.85%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102910.70 (n/a)</td><td>100273.96 (n/a)</td><td>100971.50 (n/a)</td><td>97741.70 (n/a)</td><td>2141.60 (n/a)</td><td>703.07 (n/a)</td><td>685.57 (n/a)</td><td>680.58 (n/a)</td><td>667.76 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.80 (+0.12%)</td><td>0.79 (-0.64%)</td><td>0.79 (-0.67%)</td><td>0.78 (-0.48%)</td><td>0.01 <b>(+38.76%)</b></td><td>96491.10 (+0.48%)</td><td>95475.22 (+0.65%)</td><td>95287.30 (+0.67%)</td><td>94347.30 (-0.12%)</td><td>919.77 <b>(+39.34%)</b></td><td>728.37 (+0.12%)</td><td>719.82 (-0.64%)</td><td>721.18 (-0.67%)</td><td>712.18 (-0.48%)</td><td>6.93 <b>(+38.76%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>96028.40 (n/a)</td><td>94860.02 (n/a)</td><td>94650.60 (n/a)</td><td>94459.60 (n/a)</td><td>660.07 (n/a)</td><td>727.50 (n/a)</td><td>724.46 (n/a)</td><td>726.03 (n/a)</td><td>715.62 (n/a)</td><td>5.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.62 <b>(+20.67%)</b></td><td>4.85 <b>(+20.93%)</b></td><td>5.28 <b>(+28.67%)</b></td><td>4.00 <b>(+35.97%)</b></td><td>0.77 (+18.72%)</td><td>2230.60 <b>(-26.45%)</b></td><td>1877.88 (-17.61%)</td><td>1688.50 <b>(-22.29%)</b></td><td>1587.00 (-17.13%)</td><td>312.39 <b>(-28.54%)</b></td><td>338.29 <b>(+20.67%)</b></td><td>292.04 <b>(+20.93%)</b></td><td>317.96 <b>(+28.67%)</b></td><td>240.69 <b>(+35.97%)</b></td><td>46.24 (+18.72%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.65 (n/a)</td><td>4.01 (n/a)</td><td>4.10 (n/a)</td><td>2.94 (n/a)</td><td>0.65 (n/a)</td><td>3032.90 (n/a)</td><td>2279.14 (n/a)</td><td>2172.70 (n/a)</td><td>1915.10 (n/a)</td><td>437.18 (n/a)</td><td>280.33 (n/a)</td><td>241.49 (n/a)</td><td>247.10 (n/a)</td><td>177.02 (n/a)</td><td>38.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.18 (+16.07%)</td><td>3.46 <b>(+23.40%)</b></td><td>2.98 <b>(+31.70%)</b></td><td>1.67 <b>(-21.52%)</b></td><td>1.48 <b>(+50.70%)</b></td><td>5333.50 <b>(+27.42%)</b></td><td>3047.10 (-11.25%)</td><td>2987.70 <b>(-24.07%)</b></td><td>1721.00 (-13.85%)</td><td>1456.62 <b>(+57.65%)</b></td><td>311.95 (+16.07%)</td><td>208.45 <b>(+23.40%)</b></td><td>179.69 <b>(+31.70%)</b></td><td>100.66 <b>(-21.52%)</b></td><td>89.30 <b>(+50.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.46 (n/a)</td><td>2.80 (n/a)</td><td>2.27 (n/a)</td><td>2.13 (n/a)</td><td>0.98 (n/a)</td><td>4185.70 (n/a)</td><td>3433.54 (n/a)</td><td>3934.60 (n/a)</td><td>1997.60 (n/a)</td><td>923.93 (n/a)</td><td>268.76 (n/a)</td><td>168.92 (n/a)</td><td>136.45 (n/a)</td><td>128.26 (n/a)</td><td>59.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.15 (-4.24%)</td><td>3.38 <b>(-23.18%)</b></td><td>3.87 <b>(-25.19%)</b></td><td>1.75 <b>(-20.60%)</b></td><td>1.40 (+4.92%)</td><td>5097.30 <b>(+25.95%)</b></td><td>3095.06 <b>(+36.60%)</b></td><td>2302.60 <b>(+33.67%)</b></td><td>1731.80 (+4.43%)</td><td>1437.32 <b>(+41.11%)</b></td><td>310.01 (-4.24%)</td><td>203.88 <b>(-23.18%)</b></td><td>233.15 <b>(-25.19%)</b></td><td>105.32 <b>(-20.60%)</b></td><td>84.43 (+4.92%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.37 (n/a)</td><td>4.41 (n/a)</td><td>5.17 (n/a)</td><td>2.20 (n/a)</td><td>1.34 (n/a)</td><td>4047.10 (n/a)</td><td>2265.78 (n/a)</td><td>1722.60 (n/a)</td><td>1658.30 (n/a)</td><td>1018.61 (n/a)</td><td>323.74 (n/a)</td><td>265.39 (n/a)</td><td>311.67 (n/a)</td><td>132.66 (n/a)</td><td>80.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.60 (-0.46%)</td><td>5.12 (+12.42%)</td><td>5.12 (+16.98%)</td><td>4.27 <b>(+20.57%)</b></td><td>0.53 <b>(-33.88%)</b></td><td>8171.30 (-17.06%)</td><td>6878.00 (-12.41%)</td><td>6803.90 (-14.51%)</td><td>6230.20 (+0.46%)</td><td>774.46 <b>(-44.28%)</b></td><td>344.69 (-0.46%)</td><td>315.13 (+12.42%)</td><td>315.62 (+16.98%)</td><td>262.81 <b>(+20.57%)</b></td><td>32.40 <b>(-33.88%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.62 (n/a)</td><td>4.55 (n/a)</td><td>4.38 (n/a)</td><td>3.54 (n/a)</td><td>0.80 (n/a)</td><td>9852.50 (n/a)</td><td>7852.72 (n/a)</td><td>7959.10 (n/a)</td><td>6201.80 (n/a)</td><td>1390.02 (n/a)</td><td>346.27 (n/a)</td><td>280.33 (n/a)</td><td>269.82 (n/a)</td><td>217.96 (n/a)</td><td>49.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.48 (-2.37%)</td><td>4.76 (-4.28%)</td><td>4.45 (-13.93%)</td><td>4.12 (+2.75%)</td><td>0.61 (-9.88%)</td><td>8463.20 (-2.67%)</td><td>7418.14 (+4.14%)</td><td>7829.80 (+16.18%)</td><td>6358.40 (+2.43%)</td><td>926.91 (-11.31%)</td><td>337.74 (-2.37%)</td><td>293.25 (-4.28%)</td><td>274.27 (-13.93%)</td><td>253.74 (+2.75%)</td><td>37.69 (-9.88%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.62 (n/a)</td><td>4.97 (n/a)</td><td>5.17 (n/a)</td><td>4.01 (n/a)</td><td>0.68 (n/a)</td><td>8695.70 (n/a)</td><td>7123.04 (n/a)</td><td>6739.40 (n/a)</td><td>6207.40 (n/a)</td><td>1045.09 (n/a)</td><td>345.95 (n/a)</td><td>306.37 (n/a)</td><td>318.64 (n/a)</td><td>246.96 (n/a)</td><td>41.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.52 (+5.78%)</td><td>4.84 (-8.04%)</td><td>4.49 (-14.69%)</td><td>4.14 (-3.96%)</td><td>0.96 <b>(+46.06%)</b></td><td>8429.50 (+4.12%)</td><td>7398.88 (+10.17%)</td><td>7768.20 (+17.22%)</td><td>5344.70 (-5.47%)</td><td>1204.42 <b>(+37.20%)</b></td><td>401.80 (+5.78%)</td><td>297.94 (-8.04%)</td><td>276.44 (-14.69%)</td><td>254.76 (-3.96%)</td><td>59.37 <b>(+46.06%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>6.17 (n/a)</td><td>5.26 (n/a)</td><td>5.26 (n/a)</td><td>4.31 (n/a)</td><td>0.66 (n/a)</td><td>8095.90 (n/a)</td><td>6715.78 (n/a)</td><td>6627.20 (n/a)</td><td>5653.80 (n/a)</td><td>877.86 (n/a)</td><td>379.83 (n/a)</td><td>323.98 (n/a)</td><td>324.04 (n/a)</td><td>265.26 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.79 (+0.84%)</td><td>0.78 (+2.16%)</td><td>0.77 (+1.37%)</td><td>0.76 (+4.84%)</td><td>0.01 <b>(-51.61%)</b></td><td>98863.50 (-4.62%)</td><td>97306.04 (-2.17%)</td><td>97633.50 (-1.35%)</td><td>95482.20 (-0.83%)</td><td>1306.77 <b>(-54.33%)</b></td><td>719.71 (+0.84%)</td><td>706.32 (+2.16%)</td><td>703.85 (+1.37%)</td><td>695.09 (+4.84%)</td><td>9.52 <b>(-51.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103649.10 (n/a)</td><td>99461.72 (n/a)</td><td>98967.50 (n/a)</td><td>96284.40 (n/a)</td><td>2861.11 (n/a)</td><td>713.71 (n/a)</td><td>691.37 (n/a)</td><td>694.36 (n/a)</td><td>663.00 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.78 (+0.10%)</td><td>0.77 (+1.81%)</td><td>0.76 (+0.64%)</td><td>0.76 (+6.29%)</td><td>0.01 <b>(-64.83%)</b></td><td>99825.20 (-5.92%)</td><td>98400.04 (-1.87%)</td><td>98803.20 (-0.64%)</td><td>96547.70 (-0.10%)</td><td>1241.93 <b>(-67.02%)</b></td><td>711.77 (+0.10%)</td><td>698.46 (+1.81%)</td><td>695.52 (+0.64%)</td><td>688.40 (+6.29%)</td><td>8.87 <b>(-64.83%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.03 (n/a)</td><td>106103.40 (n/a)</td><td>100277.20 (n/a)</td><td>99440.10 (n/a)</td><td>96645.80 (n/a)</td><td>3765.85 (n/a)</td><td>711.04 (n/a)</td><td>686.05 (n/a)</td><td>691.06 (n/a)</td><td>647.66 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.80 (-0.15%)</td><td>0.80 (-0.34%)</td><td>0.80 (-0.66%)</td><td>0.80 (-0.25%)</td><td>0.00 (+2.00%)</td><td>94891.60 (+0.25%)</td><td>94346.90 (+0.34%)</td><td>94435.80 (+0.66%)</td><td>93900.10 (+0.15%)</td><td>390.21 (+2.39%)</td><td>731.84 (-0.15%)</td><td>728.38 (-0.34%)</td><td>727.68 (-0.66%)</td><td>724.19 (-0.25%)</td><td>3.01 (+2.00%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94656.40 (n/a)</td><td>94023.98 (n/a)</td><td>93814.80 (n/a)</td><td>93759.00 (n/a)</td><td>381.09 (n/a)</td><td>732.94 (n/a)</td><td>730.88 (n/a)</td><td>732.50 (n/a)</td><td>725.99 (n/a)</td><td>2.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.42 (-12.96%)</td><td>2.21 <b>(-26.83%)</b></td><td>1.64 <b>(-56.61%)</b></td><td>1.58 (-11.07%)</td><td>0.84 <b>(-25.36%)</b></td><td>5099.90 (+12.44%)</td><td>4042.70 <b>(+31.89%)</b></td><td>4920.70 <b>(+130.48%)</b></td><td>2355.60 (+14.88%)</td><td>1301.95 (-1.56%)</td><td>897.39 (-12.96%)</td><td>579.23 <b>(-26.83%)</b></td><td>429.60 <b>(-56.61%)</b></td><td>414.51 (-11.07%)</td><td>220.50 <b>(-25.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.93 (n/a)</td><td>3.02 (n/a)</td><td>3.78 (n/a)</td><td>1.78 (n/a)</td><td>1.13 (n/a)</td><td>4535.60 (n/a)</td><td>3065.24 (n/a)</td><td>2135.00 (n/a)</td><td>2050.40 (n/a)</td><td>1322.53 (n/a)</td><td>1030.97 (n/a)</td><td>791.58 (n/a)</td><td>990.14 (n/a)</td><td>466.08 (n/a)</td><td>295.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.29 (+0.12%)</td><td>0.22 (-0.59%)</td><td>0.20 (+2.00%)</td><td>0.15 (-18.12%)</td><td>0.05 <b>(+27.53%)</b></td><td>8210.20 <b>(+22.13%)</b></td><td>6050.08 (+2.99%)</td><td>6275.30 (-1.96%)</td><td>4355.00 (-0.12%)</td><td>1505.28 <b>(+53.96%)</b></td><td>15.41 (+0.12%)</td><td>11.65 (-0.59%)</td><td>10.69 (+2.00%)</td><td>8.17 (-18.12%)</td><td>2.86 <b>(+27.53%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>6722.50 (n/a)</td><td>5874.48 (n/a)</td><td>6400.50 (n/a)</td><td>4360.40 (n/a)</td><td>977.73 (n/a)</td><td>15.39 (n/a)</td><td>11.72 (n/a)</td><td>10.48 (n/a)</td><td>9.98 (n/a)</td><td>2.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.68 (n/a)</td><td>3.57 (n/a)</td><td>3.66 (n/a)</td><td>3.41 (n/a)</td><td>0.13 (n/a)</td><td>3.67 (n/a)</td><td>3.57 (n/a)</td><td>3.66 (n/a)</td><td>3.40 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.84 (-6.21%)</td><td>5.94 (-1.62%)</td><td>5.73 (-2.00%)</td><td>5.26 (+11.64%)</td><td>0.64 <b>(-35.25%)</b></td><td>6.84 (-6.21%)</td><td>5.94 (-1.62%)</td><td>5.73 (-2.00%)</td><td>5.25 (+11.64%)</td><td>0.64 <b>(-35.25%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>7.29 (n/a)</td><td>6.04 (n/a)</td><td>5.85 (n/a)</td><td>4.71 (n/a)</td><td>0.99 (n/a)</td><td>7.29 (n/a)</td><td>6.03 (n/a)</td><td>5.84 (n/a)</td><td>4.71 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>14.23 (-1.38%)</td><td>9.84 (-3.91%)</td><td>9.08 (+7.51%)</td><td>8.00 <b>(+31.41%)</b></td><td>2.50 <b>(-33.09%)</b></td><td>14.22 (-1.38%)</td><td>9.84 (-3.91%)</td><td>9.07 (+7.51%)</td><td>8.00 <b>(+31.41%)</b></td><td>2.50 <b>(-33.09%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>14.43 (n/a)</td><td>10.25 (n/a)</td><td>8.44 (n/a)</td><td>6.09 (n/a)</td><td>3.73 (n/a)</td><td>14.42 (n/a)</td><td>10.24 (n/a)</td><td>8.44 (n/a)</td><td>6.09 (n/a)</td><td>3.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.95 (n/a)</td><td>3.61 (n/a)</td><td>3.51 (n/a)</td><td>3.34 (n/a)</td><td>0.24 (n/a)</td><td>3.95 (n/a)</td><td>3.61 (n/a)</td><td>3.51 (n/a)</td><td>3.34 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.47 (-15.57%)</td><td>5.96 (-6.91%)</td><td>5.76 (-8.78%)</td><td>5.67 (+13.08%)</td><td>0.36 <b>(-63.43%)</b></td><td>6.47 (-15.57%)</td><td>5.96 (-6.91%)</td><td>5.76 (-8.78%)</td><td>5.67 (+13.08%)</td><td>0.36 <b>(-63.43%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>7.67 (n/a)</td><td>6.40 (n/a)</td><td>6.31 (n/a)</td><td>5.02 (n/a)</td><td>0.98 (n/a)</td><td>7.66 (n/a)</td><td>6.40 (n/a)</td><td>6.31 (n/a)</td><td>5.01 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>13.58 (+1.06%)</td><td>10.23 (+8.06%)</td><td>9.66 (+17.90%)</td><td>8.35 (+3.66%)</td><td>1.97 (-14.54%)</td><td>13.57 (+1.06%)</td><td>10.22 (+8.06%)</td><td>9.66 (+17.90%)</td><td>8.34 (+3.66%)</td><td>1.97 (-14.54%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>13.43 (n/a)</td><td>9.47 (n/a)</td><td>8.20 (n/a)</td><td>8.05 (n/a)</td><td>2.30 (n/a)</td><td>13.43 (n/a)</td><td>9.46 (n/a)</td><td>8.19 (n/a)</td><td>8.05 (n/a)</td><td>2.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.96 (-1.36%)</td><td>2.22 (+13.61%)</td><td>2.88 <b>(+69.70%)</b></td><td>1.06 (+4.30%)</td><td>0.98 (+5.37%)</td><td>2.96 (-1.36%)</td><td>2.22 (+13.61%)</td><td>2.87 <b>(+69.70%)</b></td><td>1.06 (+4.30%)</td><td>0.98 (+5.37%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.01 (n/a)</td><td>1.96 (n/a)</td><td>1.70 (n/a)</td><td>1.02 (n/a)</td><td>0.93 (n/a)</td><td>3.00 (n/a)</td><td>1.95 (n/a)</td><td>1.69 (n/a)</td><td>1.02 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.47 (+0.13%)</td><td>0.26 (-10.19%)</td><td>0.23 <b>(-32.40%)</b></td><td>0.08 (+3.63%)</td><td>0.14 <b>(-21.50%)</b></td><td>0.46 (+0.13%)</td><td>0.26 (-10.19%)</td><td>0.23 <b>(-32.40%)</b></td><td>0.08 (+3.63%)</td><td>0.14 <b>(-21.50%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.18 (n/a)</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.67 (-8.69%)</td><td>0.37 <b>(-40.29%)</b></td><td>0.33 <b>(-50.82%)</b></td><td>0.08 <b>(-79.23%)</b></td><td>0.27 <b>(+87.22%)</b></td><td>0.66 (-8.69%)</td><td>0.36 <b>(-40.29%)</b></td><td>0.32 <b>(-50.82%)</b></td><td>0.08 <b>(-79.23%)</b></td><td>0.27 <b>(+87.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.67 (n/a)</td><td>0.37 (n/a)</td><td>0.15 (n/a)</td><td>0.73 (n/a)</td><td>0.61 (n/a)</td><td>0.66 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.44 (-15.37%)</td><td>1.43 (-2.61%)</td><td>1.45 (-2.53%)</td><td>0.72 <b>(+63.03%)</b></td><td>0.72 <b>(-30.56%)</b></td><td>2.40 (-15.37%)</td><td>1.40 (-2.61%)</td><td>1.43 (-2.53%)</td><td>0.71 <b>(+63.03%)</b></td><td>0.71 <b>(-30.56%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.89 (n/a)</td><td>1.46 (n/a)</td><td>1.49 (n/a)</td><td>0.44 (n/a)</td><td>1.04 (n/a)</td><td>2.84 (n/a)</td><td>1.44 (n/a)</td><td>1.47 (n/a)</td><td>0.44 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>274.60 (n/a)</td><td>259.86 (n/a)</td><td>269.30 (n/a)</td><td>236.90 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.50 (n/a)</td><td>328.66 (n/a)</td><td>296.30 (n/a)</td><td>241.70 (n/a)</td><td>117.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.20 (n/a)</td><td>530.12 (n/a)</td><td>553.00 (n/a)</td><td>410.70 (n/a)</td><td>71.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>638.00 (n/a)</td><td>386.70 (n/a)</td><td>295.70 (n/a)</td><td>246.50 (n/a)</td><td>164.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>473.20 (n/a)</td><td>393.90 (n/a)</td><td>453.40 (n/a)</td><td>255.70 (n/a)</td><td>100.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>705.00 (n/a)</td><td>480.18 (n/a)</td><td>499.80 (n/a)</td><td>261.70 (n/a)</td><td>167.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.60 (n/a)</td><td>423.40 (n/a)</td><td>429.40 (n/a)</td><td>207.40 (n/a)</td><td>203.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.30 (n/a)</td><td>421.54 (n/a)</td><td>512.80 (n/a)</td><td>226.90 (n/a)</td><td>163.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.80 (n/a)</td><td>395.68 (n/a)</td><td>271.60 (n/a)</td><td>229.00 (n/a)</td><td>191.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2465.00 (n/a)</td><td>854.78 (n/a)</td><td>538.00 (n/a)</td><td>280.40 (n/a)</td><td>906.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.70 (n/a)</td><td>376.08 (n/a)</td><td>366.60 (n/a)</td><td>251.50 (n/a)</td><td>110.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>658.40 (n/a)</td><td>540.78 (n/a)</td><td>531.70 (n/a)</td><td>354.40 (n/a)</td><td>122.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>640.90 (n/a)</td><td>372.74 (n/a)</td><td>310.30 (n/a)</td><td>261.10 (n/a)</td><td>152.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>421.10 (n/a)</td><td>359.96 (n/a)</td><td>363.10 (n/a)</td><td>298.70 (n/a)</td><td>60.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>673.60 (n/a)</td><td>540.64 (n/a)</td><td>652.20 (n/a)</td><td>216.10 (n/a)</td><td>196.40 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>736.20 (n/a)</td><td>451.24 (n/a)</td><td>493.20 (n/a)</td><td>247.10 (n/a)</td><td>197.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.40 (n/a)</td><td>438.70 (n/a)</td><td>494.00 (n/a)</td><td>246.60 (n/a)</td><td>161.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>615.20 (n/a)</td><td>462.62 (n/a)</td><td>454.80 (n/a)</td><td>302.40 (n/a)</td><td>139.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>513.70 (n/a)</td><td>386.02 (n/a)</td><td>347.10 (n/a)</td><td>307.20 (n/a)</td><td>86.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>658.50 (n/a)</td><td>485.54 (n/a)</td><td>534.70 (n/a)</td><td>225.80 (n/a)</td><td>181.78 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>561.90 (n/a)</td><td>462.16 (n/a)</td><td>490.00 (n/a)</td><td>316.70 (n/a)</td><td>98.75 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>622.80 (n/a)</td><td>430.16 (n/a)</td><td>360.50 (n/a)</td><td>268.20 (n/a)</td><td>160.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>604.30 (n/a)</td><td>432.86 (n/a)</td><td>408.70 (n/a)</td><td>266.00 (n/a)</td><td>163.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1863.40 (n/a)</td><td>758.40 (n/a)</td><td>483.90 (n/a)</td><td>361.30 (n/a)</td><td>627.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+0.42%)</td><td>0.01 <b>(-24.86%)</b></td><td>0.01 <b>(-44.84%)</b></td><td>0.01 (-13.87%)</td><td>0.00 (+16.29%)</td><td>567.00 (+16.09%)</td><td>414.06 <b>(+38.30%)</b></td><td>440.50 <b>(+81.28%)</b></td><td>237.30 (-0.42%)</td><td>144.11 <b>(+34.19%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.40 (n/a)</td><td>299.40 (n/a)</td><td>243.00 (n/a)</td><td>238.30 (n/a)</td><td>107.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-14.41%)</td><td>0.01 <b>(-25.60%)</b></td><td>0.01 <b>(-30.62%)</b></td><td>0.01 (-16.97%)</td><td>0.00 <b>(-24.03%)</b></td><td>536.50 <b>(+20.43%)</b></td><td>433.24 <b>(+32.30%)</b></td><td>481.50 <b>(+44.16%)</b></td><td>257.50 (+16.83%)</td><td>109.34 (+6.45%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>445.50 (n/a)</td><td>327.48 (n/a)</td><td>334.00 (n/a)</td><td>220.40 (n/a)</td><td>102.72 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(+68.22%)</b></td><td>0.01 <b>(+33.66%)</b></td><td>0.01 <b>(+28.16%)</b></td><td>0.01 (+9.38%)</td><td>0.00 <b>(+275.40%)</b></td><td>511.40 (-8.58%)</td><td>376.32 (-18.59%)</td><td>357.70 <b>(-21.98%)</b></td><td>236.10 <b>(-40.54%)</b></td><td>128.05 <b>(+110.04%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.40 (n/a)</td><td>462.28 (n/a)</td><td>458.50 (n/a)</td><td>397.10 (n/a)</td><td>60.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-0.40%)</td><td>0.01 (-1.93%)</td><td>0.01 (-6.30%)</td><td>0.01 (-6.51%)</td><td>0.00 (+7.16%)</td><td>532.80 (+6.97%)</td><td>404.60 (+3.70%)</td><td>478.50 (+6.71%)</td><td>258.10 (+0.39%)</td><td>135.08 (+12.18%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.10 (n/a)</td><td>390.18 (n/a)</td><td>448.40 (n/a)</td><td>257.10 (n/a)</td><td>120.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+6.18%)</td><td>0.01 <b>(-34.07%)</b></td><td>0.01 <b>(-44.30%)</b></td><td>0.00 <b>(-60.21%)</b></td><td>0.01 (+18.14%)</td><td>2012.10 <b>(+151.29%)</b></td><td>747.16 <b>(+101.52%)</b></td><td>488.50 <b>(+79.53%)</b></td><td>232.10 (-5.80%)</td><td>716.87 <b>(+197.88%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>800.70 (n/a)</td><td>370.76 (n/a)</td><td>272.10 (n/a)</td><td>246.40 (n/a)</td><td>240.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(-33.98%)</b></td><td>0.01 <b>(-32.41%)</b></td><td>0.01 <b>(-42.81%)</b></td><td>0.01 <b>(-20.00%)</b></td><td>0.00 <b>(-39.92%)</b></td><td>729.90 <b>(+25.00%)</b></td><td>512.44 <b>(+42.04%)</b></td><td>506.60 <b>(+74.87%)</b></td><td>332.20 <b>(+51.41%)</b></td><td>166.35 (+9.90%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.90 (n/a)</td><td>360.78 (n/a)</td><td>289.70 (n/a)</td><td>219.40 (n/a)</td><td>151.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-21.47%)</b></td><td>0.02 (-15.91%)</td><td>0.03 (-14.89%)</td><td>0.01 (-13.72%)</td><td>0.01 <b>(-27.99%)</b></td><td>585.40 (+15.92%)</td><td>392.84 (+14.68%)</td><td>301.00 (+17.49%)</td><td>273.80 <b>(+27.35%)</b></td><td>144.51 (-0.38%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.00 (n/a)</td><td>342.56 (n/a)</td><td>256.20 (n/a)</td><td>215.00 (n/a)</td><td>145.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-34.83%)</b></td><td>0.02 (-14.12%)</td><td>0.02 (-18.65%)</td><td>0.02 <b>(+31.88%)</b></td><td>0.01 <b>(-54.33%)</b></td><td>503.60 <b>(-24.18%)</b></td><td>402.94 (+2.17%)</td><td>430.20 <b>(+22.91%)</b></td><td>292.60 <b>(+53.43%)</b></td><td>95.96 <b>(-47.82%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.20 (n/a)</td><td>394.40 (n/a)</td><td>350.00 (n/a)</td><td>190.70 (n/a)</td><td>183.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (+5.74%)</td><td>0.03 (-11.60%)</td><td>0.03 (-11.02%)</td><td>0.02 (-7.50%)</td><td>0.01 <b>(+24.19%)</b></td><td>485.10 (+8.11%)</td><td>342.68 (+16.66%)</td><td>318.20 (+12.40%)</td><td>195.70 (-5.41%)</td><td>111.92 <b>(+21.14%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>448.70 (n/a)</td><td>293.74 (n/a)</td><td>283.10 (n/a)</td><td>206.90 (n/a)</td><td>92.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-22.93%)</b></td><td>0.02 <b>(-32.97%)</b></td><td>0.02 <b>(-32.40%)</b></td><td>0.01 <b>(-59.38%)</b></td><td>0.01 <b>(+21.29%)</b></td><td>1059.00 <b>(+146.16%)</b></td><td>526.72 <b>(+79.71%)</b></td><td>361.30 <b>(+47.95%)</b></td><td>287.50 <b>(+29.74%)</b></td><td>329.13 <b>(+272.95%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>430.20 (n/a)</td><td>293.10 (n/a)</td><td>244.20 (n/a)</td><td>221.60 (n/a)</td><td>88.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-44.32%)</b></td><td>0.02 <b>(-38.80%)</b></td><td>0.02 <b>(-45.91%)</b></td><td>0.02 (-4.89%)</td><td>0.01 <b>(-59.64%)</b></td><td>531.90 (+5.14%)</td><td>441.92 <b>(+48.11%)</b></td><td>473.10 <b>(+84.88%)</b></td><td>286.80 <b>(+79.59%)</b></td><td>94.63 <b>(-28.14%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.90 (n/a)</td><td>298.38 (n/a)</td><td>255.90 (n/a)</td><td>159.70 (n/a)</td><td>131.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (+17.83%)</td><td>0.02 (-2.94%)</td><td>0.02 (-18.53%)</td><td>0.02 (+10.89%)</td><td>0.01 <b>(+45.62%)</b></td><td>522.10 (-9.81%)</td><td>436.60 (+6.02%)</td><td>477.20 <b>(+22.77%)</b></td><td>243.40 (-15.13%)</td><td>113.18 (+6.20%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.90 (n/a)</td><td>411.80 (n/a)</td><td>388.70 (n/a)</td><td>286.80 (n/a)</td><td>106.57 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-20.48%)</b></td><td>0.02 (-18.67%)</td><td>0.03 (-13.61%)</td><td>0.01 (-18.60%)</td><td>0.01 (-11.51%)</td><td>587.80 <b>(+22.84%)</b></td><td>374.10 <b>(+23.94%)</b></td><td>298.10 (+15.77%)</td><td>290.80 <b>(+25.78%)</b></td><td>128.56 <b>(+27.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.50 (n/a)</td><td>301.84 (n/a)</td><td>257.50 (n/a)</td><td>231.20 (n/a)</td><td>101.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-24.53%)</b></td><td>0.02 <b>(-30.05%)</b></td><td>0.02 <b>(-43.85%)</b></td><td>0.01 <b>(+29.72%)</b></td><td>0.00 <b>(-52.74%)</b></td><td>564.40 <b>(-22.91%)</b></td><td>491.78 <b>(+26.27%)</b></td><td>516.70 <b>(+78.11%)</b></td><td>326.30 <b>(+32.53%)</b></td><td>96.14 <b>(-52.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>732.10 (n/a)</td><td>389.48 (n/a)</td><td>290.10 (n/a)</td><td>246.20 (n/a)</td><td>203.94 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-4.19%)</td><td>0.04 (-11.17%)</td><td>0.04 (+3.15%)</td><td>0.01 <b>(-71.79%)</b></td><td>0.02 <b>(+27.89%)</b></td><td>1975.60 <b>(+254.43%)</b></td><td>690.64 <b>(+69.83%)</b></td><td>441.50 (-3.05%)</td><td>258.50 (+4.36%)</td><td>725.32 <b>(+417.69%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>557.40 (n/a)</td><td>406.66 (n/a)</td><td>455.40 (n/a)</td><td>247.70 (n/a)</td><td>140.11 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (+7.53%)</td><td>0.05 (+13.32%)</td><td>0.06 <b>(+54.72%)</b></td><td>0.03 (-4.79%)</td><td>0.02 (+3.15%)</td><td>581.20 (+5.04%)</td><td>346.96 (-10.92%)</td><td>277.80 <b>(-35.37%)</b></td><td>223.00 (-6.97%)</td><td>143.73 (+8.18%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>553.30 (n/a)</td><td>389.48 (n/a)</td><td>429.80 (n/a)</td><td>239.70 (n/a)</td><td>132.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-11.21%)</td><td>0.04 <b>(-22.43%)</b></td><td>0.03 <b>(-45.20%)</b></td><td>0.03 (+18.01%)</td><td>0.01 <b>(-20.83%)</b></td><td>500.10 (-15.27%)</td><td>410.02 <b>(+23.65%)</b></td><td>476.10 <b>(+82.48%)</b></td><td>285.40 (+12.63%)</td><td>107.16 <b>(-26.33%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.20 (n/a)</td><td>331.60 (n/a)</td><td>260.90 (n/a)</td><td>253.40 (n/a)</td><td>145.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 <b>(-25.67%)</b></td><td>0.04 (-16.17%)</td><td>0.04 (+4.98%)</td><td>0.02 (-18.40%)</td><td>0.01 <b>(-42.06%)</b></td><td>799.40 <b>(+22.55%)</b></td><td>487.50 (+11.18%)</td><td>432.20 (-4.76%)</td><td>315.20 <b>(+34.53%)</b></td><td>190.21 (+0.43%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>652.30 (n/a)</td><td>438.46 (n/a)</td><td>453.80 (n/a)</td><td>234.30 (n/a)</td><td>189.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 <b>(-34.94%)</b></td><td>0.03 <b>(-22.70%)</b></td><td>0.03 (+7.74%)</td><td>0.02 (+1.97%)</td><td>0.01 <b>(-58.91%)</b></td><td>662.10 (-1.93%)</td><td>520.54 (+9.78%)</td><td>535.40 (-7.18%)</td><td>326.80 <b>(+53.64%)</b></td><td>123.83 <b>(-42.33%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>675.10 (n/a)</td><td>474.18 (n/a)</td><td>576.80 (n/a)</td><td>212.70 (n/a)</td><td>214.72 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (+19.98%)</td><td>0.04 (-10.86%)</td><td>0.03 <b>(-31.95%)</b></td><td>0.03 (-6.30%)</td><td>0.01 <b>(+53.26%)</b></td><td>560.60 (+6.74%)</td><td>429.34 (+16.60%)</td><td>468.70 <b>(+46.97%)</b></td><td>250.20 (-16.66%)</td><td>120.55 <b>(+30.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>525.20 (n/a)</td><td>368.22 (n/a)</td><td>318.90 (n/a)</td><td>300.20 (n/a)</td><td>92.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 <b>(+36.26%)</b></td><td>0.09 <b>(+25.03%)</b></td><td>0.08 (+9.52%)</td><td>0.07 <b>(+33.28%)</b></td><td>0.03 <b>(+23.27%)</b></td><td>459.40 <b>(-24.97%)</b></td><td>366.54 <b>(-21.02%)</b></td><td>397.90 (-8.68%)</td><td>239.20 <b>(-26.60%)</b></td><td>93.53 <b>(-33.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>612.30 (n/a)</td><td>464.08 (n/a)</td><td>435.70 (n/a)</td><td>325.90 (n/a)</td><td>139.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (-19.57%)</td><td>0.08 (-19.75%)</td><td>0.06 <b>(-29.84%)</b></td><td>0.05 (-7.82%)</td><td>0.03 <b>(-23.66%)</b></td><td>622.60 (+8.49%)</td><td>466.60 <b>(+21.75%)</b></td><td>524.00 <b>(+42.51%)</b></td><td>287.40 <b>(+24.31%)</b></td><td>154.38 (+3.85%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>573.90 (n/a)</td><td>383.24 (n/a)</td><td>367.70 (n/a)</td><td>231.20 (n/a)</td><td>148.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 (-17.94%)</td><td>0.08 (+7.25%)</td><td>0.08 <b>(+24.04%)</b></td><td>0.05 (+5.46%)</td><td>0.02 <b>(-26.82%)</b></td><td>605.30 (-5.18%)</td><td>433.18 (-10.85%)</td><td>420.30 (-19.39%)</td><td>301.70 <b>(+21.85%)</b></td><td>132.39 (-17.76%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>638.40 (n/a)</td><td>485.88 (n/a)</td><td>521.40 (n/a)</td><td>247.60 (n/a)</td><td>160.98 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 <b>(-21.14%)</b></td><td>0.06 (-19.55%)</td><td>0.06 <b>(-24.94%)</b></td><td>0.06 (-10.82%)</td><td>0.01 <b>(-48.92%)</b></td><td>576.00 (+12.13%)</td><td>512.72 <b>(+22.09%)</b></td><td>535.90 <b>(+33.24%)</b></td><td>430.40 <b>(+26.81%)</b></td><td>57.12 <b>(-28.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>513.70 (n/a)</td><td>419.96 (n/a)</td><td>402.20 (n/a)</td><td>339.40 (n/a)</td><td>79.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (+6.60%)</td><td>0.07 (-4.50%)</td><td>0.06 (-6.25%)</td><td>0.05 (-10.16%)</td><td>0.02 <b>(+43.73%)</b></td><td>617.40 (+11.30%)</td><td>508.38 (+7.03%)</td><td>505.90 (+6.66%)</td><td>349.40 (-6.18%)</td><td>107.19 <b>(+50.19%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>554.70 (n/a)</td><td>475.00 (n/a)</td><td>474.30 (n/a)</td><td>372.40 (n/a)</td><td>71.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-0.97%)</td><td>0.01 (+1.46%)</td><td>0.01 (-18.92%)</td><td>0.01 <b>(+189.89%)</b></td><td>0.00 <b>(-34.96%)</b></td><td>629.90 <b>(-65.50%)</b></td><td>385.42 <b>(-38.52%)</b></td><td>364.00 <b>(+23.35%)</b></td><td>226.90 (+0.98%)</td><td>156.06 <b>(-77.16%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1825.90 (n/a)</td><td>626.88 (n/a)</td><td>295.10 (n/a)</td><td>224.70 (n/a)</td><td>683.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+7.45%)</td><td>0.01 <b>(+20.41%)</b></td><td>0.01 (+13.10%)</td><td>0.01 <b>(+43.63%)</b></td><td>0.00 <b>(-32.54%)</b></td><td>439.00 <b>(-30.38%)</b></td><td>310.84 <b>(-25.00%)</b></td><td>297.90 (-11.58%)</td><td>227.30 (-6.96%)</td><td>77.88 <b>(-56.63%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>630.60 (n/a)</td><td>414.46 (n/a)</td><td>336.90 (n/a)</td><td>244.30 (n/a)</td><td>179.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-2.15%)</td><td>0.01 (+3.47%)</td><td>0.02 (+2.19%)</td><td>0.01 (-5.00%)</td><td>0.01 (+5.95%)</td><td>559.50 (+5.27%)</td><td>352.38 (-1.42%)</td><td>266.40 (-2.13%)</td><td>208.90 (+2.20%)</td><td>163.24 (+7.64%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>531.50 (n/a)</td><td>357.46 (n/a)</td><td>272.20 (n/a)</td><td>204.40 (n/a)</td><td>151.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(+23.73%)</b></td><td>0.01 <b>(+29.34%)</b></td><td>0.01 <b>(+51.58%)</b></td><td>0.01 <b>(+253.67%)</b></td><td>0.00 (-15.11%)</td><td>533.50 <b>(-71.73%)</b></td><td>371.88 <b>(-46.15%)</b></td><td>294.30 <b>(-34.03%)</b></td><td>229.40 (-19.20%)</td><td>140.19 <b>(-79.33%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1886.90 (n/a)</td><td>690.62 (n/a)</td><td>446.10 (n/a)</td><td>283.90 (n/a)</td><td>678.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(+78.56%)</b></td><td>0.01 <b>(+23.19%)</b></td><td>0.01 (-15.86%)</td><td>0.00 <b>(-47.32%)</b></td><td>0.01 <b>(+220.30%)</b></td><td>1051.50 <b>(+89.84%)</b></td><td>518.14 (+17.35%)</td><td>485.30 (+18.86%)</td><td>163.90 <b>(-43.98%)</b></td><td>354.45 <b>(+216.13%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.90 (n/a)</td><td>441.54 (n/a)</td><td>408.30 (n/a)</td><td>292.60 (n/a)</td><td>112.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+11.27%)</td><td>0.01 (+18.41%)</td><td>0.02 (+9.09%)</td><td>0.01 <b>(+266.84%)</b></td><td>0.01 (-1.09%)</td><td>675.50 <b>(-72.74%)</b></td><td>382.40 <b>(-49.17%)</b></td><td>266.10 (-8.34%)</td><td>208.90 (-10.15%)</td><td>215.50 <b>(-77.79%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2478.10 (n/a)</td><td>752.30 (n/a)</td><td>290.30 (n/a)</td><td>232.50 (n/a)</td><td>970.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(-36.69%)</b></td><td>0.01 (-15.69%)</td><td>0.01 (-4.59%)</td><td>0.00 (+1.06%)</td><td>0.00 <b>(-32.35%)</b></td><td>2403.50 (-1.05%)</td><td>887.04 (+5.48%)</td><td>527.80 (+4.81%)</td><td>446.60 <b>(+57.98%)</b></td><td>850.19 (-4.75%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2428.90 (n/a)</td><td>840.96 (n/a)</td><td>503.60 (n/a)</td><td>282.70 (n/a)</td><td>892.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(+20.48%)</b></td><td>0.01 (+2.22%)</td><td>0.01 (+1.42%)</td><td>0.01 (+3.37%)</td><td>0.01 (+16.42%)</td><td>550.20 (-3.25%)</td><td>364.08 (-1.00%)</td><td>308.00 (-1.38%)</td><td>201.60 (-17.00%)</td><td>140.38 (-1.88%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.70 (n/a)</td><td>367.76 (n/a)</td><td>312.30 (n/a)</td><td>242.90 (n/a)</td><td>143.07 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(-26.32%)</b></td><td>0.01 <b>(-21.65%)</b></td><td>0.01 (-19.93%)</td><td>0.00 (+11.98%)</td><td>0.00 (-19.79%)</td><td>1860.20 (-10.70%)</td><td>827.30 (+12.95%)</td><td>585.40 <b>(+24.87%)</b></td><td>318.50 <b>(+35.71%)</b></td><td>638.27 (-16.37%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2083.00 (n/a)</td><td>732.44 (n/a)</td><td>468.80 (n/a)</td><td>234.70 (n/a)</td><td>763.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(-22.77%)</b></td><td>0.01 <b>(-22.64%)</b></td><td>0.01 <b>(-22.93%)</b></td><td>0.01 (-8.44%)</td><td>0.00 <b>(-27.22%)</b></td><td>487.80 (+9.23%)</td><td>383.76 <b>(+27.39%)</b></td><td>383.20 <b>(+29.77%)</b></td><td>290.60 <b>(+29.50%)</b></td><td>88.32 (+0.37%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>446.60 (n/a)</td><td>301.24 (n/a)</td><td>295.30 (n/a)</td><td>224.40 (n/a)</td><td>87.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (-13.82%)</td><td>0.01 (-9.13%)</td><td>0.01 (-1.96%)</td><td>0.01 (-4.89%)</td><td>0.00 <b>(-29.61%)</b></td><td>652.30 (+5.16%)</td><td>486.92 (+4.38%)</td><td>549.90 (+2.00%)</td><td>304.60 (+16.04%)</td><td>141.90 (-16.94%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.30 (n/a)</td><td>466.50 (n/a)</td><td>539.10 (n/a)</td><td>262.50 (n/a)</td><td>170.85 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 (-19.06%)</td><td>0.01 <b>(-34.30%)</b></td><td>0.01 <b>(-34.95%)</b></td><td>0.00 <b>(-65.30%)</b></td><td>0.00 <b>(+46.80%)</b></td><td>1060.20 <b>(+188.18%)</b></td><td>550.34 <b>(+80.69%)</b></td><td>507.50 <b>(+53.74%)</b></td><td>284.10 <b>(+23.52%)</b></td><td>305.56 <b>(+437.56%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>367.90 (n/a)</td><td>304.58 (n/a)</td><td>330.10 (n/a)</td><td>230.00 (n/a)</td><td>56.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-0.88%)</td><td>0.02 (-6.32%)</td><td>0.02 (-9.06%)</td><td>0.02 (+19.94%)</td><td>0.01 (-12.61%)</td><td>474.80 (-16.63%)</td><td>387.22 (+3.48%)</td><td>412.30 (+9.95%)</td><td>242.10 (+0.87%)</td><td>89.06 <b>(-29.63%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.50 (n/a)</td><td>374.20 (n/a)</td><td>375.00 (n/a)</td><td>240.00 (n/a)</td><td>126.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(-39.82%)</b></td><td>0.03 (-17.22%)</td><td>0.03 (-5.94%)</td><td>0.02 (-11.63%)</td><td>0.01 <b>(-51.06%)</b></td><td>481.80 (+13.15%)</td><td>323.14 (+15.08%)</td><td>278.10 (+6.31%)</td><td>273.50 <b>(+66.16%)</b></td><td>89.89 (-6.64%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.80 (n/a)</td><td>280.80 (n/a)</td><td>261.60 (n/a)</td><td>164.60 (n/a)</td><td>96.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (-13.65%)</td><td>0.02 <b>(-33.43%)</b></td><td>0.02 <b>(-42.99%)</b></td><td>0.01 <b>(-32.53%)</b></td><td>0.01 (+4.22%)</td><td>726.50 <b>(+48.20%)</b></td><td>472.86 <b>(+59.84%)</b></td><td>487.40 <b>(+75.39%)</b></td><td>206.60 (+15.81%)</td><td>186.28 <b>(+58.66%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.20 (n/a)</td><td>295.84 (n/a)</td><td>277.90 (n/a)</td><td>178.40 (n/a)</td><td>117.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (-7.67%)</td><td>0.03 (+17.40%)</td><td>0.03 <b>(+77.26%)</b></td><td>0.02 (+9.14%)</td><td>0.01 <b>(-22.23%)</b></td><td>525.80 (-8.38%)</td><td>335.46 <b>(-20.20%)</b></td><td>291.40 <b>(-43.59%)</b></td><td>226.00 (+8.29%)</td><td>124.06 <b>(-25.06%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.90 (n/a)</td><td>420.40 (n/a)</td><td>516.60 (n/a)</td><td>208.70 (n/a)</td><td>165.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(-39.60%)</b></td><td>0.02 <b>(-27.66%)</b></td><td>0.02 <b>(-23.27%)</b></td><td>0.02 (+8.08%)</td><td>0.00 <b>(-64.55%)</b></td><td>506.00 (-7.48%)</td><td>447.52 <b>(+27.35%)</b></td><td>462.80 <b>(+30.33%)</b></td><td>336.00 <b>(+65.52%)</b></td><td>68.17 <b>(-46.21%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.90 (n/a)</td><td>351.42 (n/a)</td><td>355.10 (n/a)</td><td>203.00 (n/a)</td><td>126.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-18.06%)</td><td>0.02 (-5.43%)</td><td>0.03 (-2.54%)</td><td>0.02 (+13.73%)</td><td>0.01 <b>(-29.97%)</b></td><td>520.50 (-12.06%)</td><td>366.24 (+0.55%)</td><td>308.40 (+2.59%)</td><td>287.90 <b>(+22.04%)</b></td><td>102.92 <b>(-28.34%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.90 (n/a)</td><td>364.22 (n/a)</td><td>300.60 (n/a)</td><td>235.90 (n/a)</td><td>143.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 <b>(+77.20%)</b></td><td>0.02 (+3.51%)</td><td>0.01 (-17.04%)</td><td>0.01 <b>(-46.53%)</b></td><td>0.01 <b>(+216.46%)</b></td><td>1097.00 <b>(+87.01%)</b></td><td>592.66 <b>(+25.79%)</b></td><td>593.40 <b>(+20.54%)</b></td><td>199.10 <b>(-43.57%)</b></td><td>327.75 <b>(+218.34%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.60 (n/a)</td><td>471.14 (n/a)</td><td>492.30 (n/a)</td><td>352.80 (n/a)</td><td>102.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 (+1.73%)</td><td>0.02 (-1.21%)</td><td>0.02 (-3.12%)</td><td>0.02 (-6.14%)</td><td>0.01 (+12.61%)</td><td>533.80 (+6.53%)</td><td>397.56 (+4.13%)</td><td>462.90 (+3.21%)</td><td>232.30 (-1.69%)</td><td>140.81 (+17.79%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.10 (n/a)</td><td>381.78 (n/a)</td><td>448.50 (n/a)</td><td>236.30 (n/a)</td><td>119.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 <b>(+57.89%)</b></td><td>0.02 (+5.30%)</td><td>0.02 <b>(-35.74%)</b></td><td>0.02 <b>(+54.34%)</b></td><td>0.01 <b>(+49.89%)</b></td><td>541.80 <b>(-35.20%)</b></td><td>443.84 (-5.67%)</td><td>519.60 <b>(+55.62%)</b></td><td>196.30 <b>(-36.68%)</b></td><td>144.68 <b>(-37.06%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>836.10 (n/a)</td><td>470.52 (n/a)</td><td>333.90 (n/a)</td><td>310.00 (n/a)</td><td>229.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-10.97%)</td><td>0.02 (-5.10%)</td><td>0.02 (+1.14%)</td><td>0.02 (+4.45%)</td><td>0.01 <b>(-26.18%)</b></td><td>475.40 (-4.27%)</td><td>402.80 (+2.39%)</td><td>435.80 (-1.11%)</td><td>273.90 (+12.30%)</td><td>85.06 <b>(-20.44%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.60 (n/a)</td><td>393.40 (n/a)</td><td>440.70 (n/a)</td><td>243.90 (n/a)</td><td>106.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-17.41%)</td><td>0.02 (-14.97%)</td><td>0.02 (-9.08%)</td><td>0.01 <b>(-25.71%)</b></td><td>0.01 (-11.77%)</td><td>785.30 <b>(+34.61%)</b></td><td>544.10 <b>(+20.73%)</b></td><td>529.20 (+10.00%)</td><td>303.80 <b>(+21.08%)</b></td><td>188.15 <b>(+54.32%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.40 (n/a)</td><td>450.68 (n/a)</td><td>481.10 (n/a)</td><td>250.90 (n/a)</td><td>121.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-10.84%)</td><td>0.01 <b>(-33.68%)</b></td><td>0.01 <b>(-30.31%)</b></td><td>0.00 <b>(-65.03%)</b></td><td>0.01 <b>(+21.96%)</b></td><td>1953.80 <b>(+185.98%)</b></td><td>1088.36 <b>(+124.77%)</b></td><td>770.60 <b>(+43.50%)</b></td><td>306.00 (+12.17%)</td><td>807.46 <b>(+354.79%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>683.20 (n/a)</td><td>484.20 (n/a)</td><td>537.00 (n/a)</td><td>272.80 (n/a)</td><td>177.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-19.73%)</td><td>0.05 (+4.94%)</td><td>0.05 <b>(+59.07%)</b></td><td>0.03 (-1.72%)</td><td>0.01 <b>(-43.49%)</b></td><td>558.80 (+1.75%)</td><td>361.42 (-12.48%)</td><td>321.40 <b>(-37.13%)</b></td><td>272.20 <b>(+24.58%)</b></td><td>114.69 <b>(-27.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>549.20 (n/a)</td><td>412.98 (n/a)</td><td>511.20 (n/a)</td><td>218.50 (n/a)</td><td>157.59 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 <b>(+63.29%)</b></td><td>0.05 <b>(+34.03%)</b></td><td>0.05 <b>(+36.91%)</b></td><td>0.03 (+11.51%)</td><td>0.01 <b>(+239.34%)</b></td><td>469.40 (-10.33%)</td><td>349.46 <b>(-21.18%)</b></td><td>323.20 <b>(-26.96%)</b></td><td>236.00 <b>(-38.75%)</b></td><td>98.92 <b>(+90.10%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>523.50 (n/a)</td><td>443.36 (n/a)</td><td>442.50 (n/a)</td><td>385.30 (n/a)</td><td>52.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (+4.48%)</td><td>0.04 (-18.63%)</td><td>0.03 <b>(-20.40%)</b></td><td>0.01 <b>(-55.78%)</b></td><td>0.02 <b>(+28.22%)</b></td><td>1353.10 <b>(+126.12%)</b></td><td>633.64 <b>(+50.01%)</b></td><td>543.30 <b>(+25.62%)</b></td><td>230.80 (-4.27%)</td><td>423.69 <b>(+184.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.40 (n/a)</td><td>422.40 (n/a)</td><td>432.50 (n/a)</td><td>241.10 (n/a)</td><td>149.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-1.89%)</td><td>0.05 (+15.72%)</td><td>0.06 <b>(+54.07%)</b></td><td>0.03 <b>(+28.29%)</b></td><td>0.02 (-18.28%)</td><td>491.00 <b>(-22.05%)</b></td><td>350.10 (-19.55%)</td><td>275.70 <b>(-35.10%)</b></td><td>243.20 (+1.93%)</td><td>124.95 <b>(-33.71%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>629.90 (n/a)</td><td>435.18 (n/a)</td><td>424.80 (n/a)</td><td>238.60 (n/a)</td><td>188.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 <b>(+77.56%)</b></td><td>0.06 <b>(+21.58%)</b></td><td>0.04 <b>(-34.59%)</b></td><td>0.03 (+1.54%)</td><td>0.03 <b>(+186.03%)</b></td><td>509.10 (-1.51%)</td><td>356.34 (-0.47%)</td><td>453.00 <b>(+52.89%)</b></td><td>154.10 <b>(-43.68%)</b></td><td>169.55 <b>(+63.20%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>516.90 (n/a)</td><td>358.04 (n/a)</td><td>296.30 (n/a)</td><td>273.60 (n/a)</td><td>103.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-12.00%)</td><td>0.04 (-9.65%)</td><td>0.05 (+0.43%)</td><td>0.01 <b>(-66.34%)</b></td><td>0.02 <b>(+32.36%)</b></td><td>1834.10 <b>(+197.12%)</b></td><td>641.50 <b>(+67.11%)</b></td><td>313.50 (-0.41%)</td><td>257.30 (+13.60%)</td><td>676.78 <b>(+334.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>617.30 (n/a)</td><td>383.88 (n/a)</td><td>314.80 (n/a)</td><td>226.50 (n/a)</td><td>155.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 <b>(+22.00%)</b></td><td>0.05 <b>(+36.29%)</b></td><td>0.06 <b>(+75.26%)</b></td><td>0.03 (+17.80%)</td><td>0.02 <b>(+46.26%)</b></td><td>516.20 (-15.11%)</td><td>350.28 <b>(-24.22%)</b></td><td>264.80 <b>(-42.93%)</b></td><td>244.90 (-18.04%)</td><td>130.33 (+0.21%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>608.10 (n/a)</td><td>462.24 (n/a)</td><td>464.00 (n/a)</td><td>298.80 (n/a)</td><td>130.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-6.11%)</td><td>0.05 (+5.76%)</td><td>0.06 (+4.65%)</td><td>0.03 (-0.54%)</td><td>0.01 <b>(-25.19%)</b></td><td>572.00 (+0.54%)</td><td>334.70 (-10.18%)</td><td>274.90 (-4.45%)</td><td>252.50 (+6.50%)</td><td>134.15 (-16.86%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>568.90 (n/a)</td><td>372.62 (n/a)</td><td>287.70 (n/a)</td><td>237.10 (n/a)</td><td>161.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-3.01%)</td><td>0.05 (-0.10%)</td><td>0.06 (+4.47%)</td><td>0.03 (-9.10%)</td><td>0.02 (+6.96%)</td><td>496.30 (+10.00%)</td><td>343.96 (+1.70%)</td><td>290.90 (-4.28%)</td><td>243.00 (+3.10%)</td><td>116.80 (+15.33%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>451.20 (n/a)</td><td>338.22 (n/a)</td><td>303.90 (n/a)</td><td>235.70 (n/a)</td><td>101.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-2.48%)</td><td>0.05 (+3.50%)</td><td>0.06 (+6.44%)</td><td>0.03 (+2.05%)</td><td>0.02 (+5.29%)</td><td>526.30 (-2.01%)</td><td>353.02 (-2.57%)</td><td>261.40 (-6.07%)</td><td>242.20 (+2.54%)</td><td>139.76 (+2.10%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.10 (n/a)</td><td>362.32 (n/a)</td><td>278.30 (n/a)</td><td>236.20 (n/a)</td><td>136.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-5.62%)</td><td>0.05 <b>(+41.55%)</b></td><td>0.06 <b>(+110.40%)</b></td><td>0.03 (+14.88%)</td><td>0.02 (-17.90%)</td><td>615.30 (-12.96%)</td><td>362.32 <b>(-33.11%)</b></td><td>295.50 <b>(-52.47%)</b></td><td>248.30 (+5.93%)</td><td>151.53 <b>(-21.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>706.90 (n/a)</td><td>541.64 (n/a)</td><td>621.70 (n/a)</td><td>234.40 (n/a)</td><td>192.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (+8.04%)</td><td>0.04 (-5.35%)</td><td>0.03 <b>(-37.68%)</b></td><td>0.03 (+17.52%)</td><td>0.02 (-1.86%)</td><td>590.70 (-14.91%)</td><td>429.68 (+1.07%)</td><td>504.30 <b>(+60.45%)</b></td><td>221.80 (-7.43%)</td><td>169.58 <b>(-22.37%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>694.20 (n/a)</td><td>425.12 (n/a)</td><td>314.30 (n/a)</td><td>239.60 (n/a)</td><td>218.45 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 <b>(+43.08%)</b></td><td>0.10 <b>(+23.30%)</b></td><td>0.07 (-2.76%)</td><td>0.06 (-8.60%)</td><td>0.05 <b>(+119.65%)</b></td><td>584.60 (+9.41%)</td><td>413.70 (-7.14%)</td><td>502.70 (+2.84%)</td><td>198.70 <b>(-30.11%)</b></td><td>176.38 <b>(+70.25%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>534.30 (n/a)</td><td>445.50 (n/a)</td><td>488.80 (n/a)</td><td>284.30 (n/a)</td><td>103.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 <b>(+31.36%)</b></td><td>0.11 (+9.62%)</td><td>0.13 <b>(+24.92%)</b></td><td>0.05 (-9.78%)</td><td>0.05 <b>(+87.01%)</b></td><td>622.10 (+10.83%)</td><td>361.40 (+2.76%)</td><td>252.00 (-19.97%)</td><td>201.50 <b>(-23.85%)</b></td><td>184.82 <b>(+53.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.30 (n/a)</td><td>351.68 (n/a)</td><td>314.90 (n/a)</td><td>264.60 (n/a)</td><td>120.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.18 <b>(+24.88%)</b></td><td>0.13 <b>(+27.05%)</b></td><td>0.12 (+5.56%)</td><td>0.10 <b>(+103.68%)</b></td><td>0.03 <b>(-20.68%)</b></td><td>314.50 <b>(-50.91%)</b></td><td>269.24 <b>(-29.17%)</b></td><td>280.80 (-5.26%)</td><td>184.70 (-19.90%)</td><td>51.91 <b>(-69.71%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>640.60 (n/a)</td><td>380.12 (n/a)</td><td>296.40 (n/a)</td><td>230.60 (n/a)</td><td>171.40 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (+15.65%)</td><td>0.10 (+9.03%)</td><td>0.08 (-0.89%)</td><td>0.06 (-3.03%)</td><td>0.04 <b>(+60.11%)</b></td><td>532.20 (+3.12%)</td><td>378.96 (-2.89%)</td><td>387.30 (+0.89%)</td><td>241.20 (-13.55%)</td><td>133.24 <b>(+37.45%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>516.10 (n/a)</td><td>390.24 (n/a)</td><td>383.90 (n/a)</td><td>279.00 (n/a)</td><td>96.94 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (+15.92%)</td><td>0.11 <b>(+26.14%)</b></td><td>0.13 <b>(+69.27%)</b></td><td>0.06 (+9.37%)</td><td>0.04 <b>(+33.96%)</b></td><td>544.80 (-8.58%)</td><td>347.64 (-18.12%)</td><td>249.10 <b>(-40.93%)</b></td><td>244.20 (-13.74%)</td><td>141.53 (+3.68%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>595.90 (n/a)</td><td>424.56 (n/a)</td><td>421.70 (n/a)</td><td>283.10 (n/a)</td><td>136.51 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (-6.43%)</td><td>0.10 <b>(+20.94%)</b></td><td>0.12 <b>(+52.99%)</b></td><td>0.06 (-5.25%)</td><td>0.03 (-0.23%)</td><td>547.40 (+5.53%)</td><td>349.30 (-16.26%)</td><td>275.70 <b>(-34.65%)</b></td><td>245.50 (+6.88%)</td><td>131.04 (+15.66%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>518.70 (n/a)</td><td>417.10 (n/a)</td><td>421.90 (n/a)</td><td>229.70 (n/a)</td><td>113.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (+2.98%)</td><td>0.08 (-8.62%)</td><td>0.07 <b>(-37.16%)</b></td><td>0.05 <b>(+204.67%)</b></td><td>0.03 <b>(-25.42%)</b></td><td>597.30 <b>(-67.18%)</b></td><td>454.00 <b>(-27.73%)</b></td><td>483.50 <b>(+59.10%)</b></td><td>235.90 (-2.88%)</td><td>137.03 <b>(-79.60%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1819.90 (n/a)</td><td>628.16 (n/a)</td><td>303.90 (n/a)</td><td>242.90 (n/a)</td><td>671.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 <b>(-35.33%)</b></td><td>0.09 (-8.42%)</td><td>0.11 <b>(+63.42%)</b></td><td>0.06 <b>(+50.34%)</b></td><td>0.03 <b>(-58.40%)</b></td><td>517.70 <b>(-33.47%)</b></td><td>373.90 (-13.19%)</td><td>297.00 <b>(-38.80%)</b></td><td>287.50 <b>(+54.65%)</b></td><td>113.91 <b>(-53.53%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>778.20 (n/a)</td><td>430.72 (n/a)</td><td>485.30 (n/a)</td><td>185.90 (n/a)</td><td>245.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (+18.55%)</td><td>0.09 (-13.48%)</td><td>0.08 <b>(-35.52%)</b></td><td>0.05 (-13.33%)</td><td>0.04 <b>(+60.20%)</b></td><td>605.30 (+15.38%)</td><td>408.36 <b>(+25.48%)</b></td><td>432.30 <b>(+55.11%)</b></td><td>213.80 (-15.66%)</td><td>163.99 <b>(+46.00%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>524.60 (n/a)</td><td>325.44 (n/a)</td><td>278.70 (n/a)</td><td>253.50 (n/a)</td><td>112.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 <b>(-34.10%)</b></td><td>0.09 (+2.06%)</td><td>0.10 <b>(+53.49%)</b></td><td>0.04 <b>(-27.82%)</b></td><td>0.03 <b>(-40.79%)</b></td><td>762.70 <b>(+38.55%)</b></td><td>404.06 (-5.60%)</td><td>320.60 <b>(-34.85%)</b></td><td>270.10 <b>(+51.74%)</b></td><td>205.12 <b>(+30.74%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>550.50 (n/a)</td><td>428.04 (n/a)</td><td>492.10 (n/a)</td><td>178.00 (n/a)</td><td>156.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 <b>(-20.77%)</b></td><td>0.08 (-6.96%)</td><td>0.08 (+18.40%)</td><td>0.04 <b>(-24.48%)</b></td><td>0.02 <b>(-22.86%)</b></td><td>771.00 <b>(+32.41%)</b></td><td>466.92 (+7.77%)</td><td>412.40 (-15.54%)</td><td>309.00 <b>(+26.23%)</b></td><td>182.95 <b>(+34.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>582.30 (n/a)</td><td>433.26 (n/a)</td><td>488.30 (n/a)</td><td>244.80 (n/a)</td><td>135.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.19 <b>(+71.59%)</b></td><td>0.09 (+4.49%)</td><td>0.06 <b>(-32.61%)</b></td><td>0.05 <b>(+189.12%)</b></td><td>0.06 <b>(+49.51%)</b></td><td>645.90 <b>(-65.41%)</b></td><td>467.52 <b>(-26.80%)</b></td><td>508.80 <b>(+48.38%)</b></td><td>176.70 <b>(-41.72%)</b></td><td>182.34 <b>(-73.47%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1867.40 (n/a)</td><td>638.70 (n/a)</td><td>342.90 (n/a)</td><td>303.20 (n/a)</td><td>687.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(-34.28%)</b></td><td>0.01 (-18.41%)</td><td>0.01 (+5.24%)</td><td>0.01 (-4.19%)</td><td>0.00 <b>(-67.19%)</b></td><td>602.60 (+4.36%)</td><td>499.80 (+11.37%)</td><td>509.50 (-4.98%)</td><td>403.00 <b>(+52.19%)</b></td><td>78.70 <b>(-49.27%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.40 (n/a)</td><td>448.78 (n/a)</td><td>536.20 (n/a)</td><td>264.80 (n/a)</td><td>155.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 <b>(+71.02%)</b></td><td>0.02 <b>(+39.64%)</b></td><td>0.02 (+19.62%)</td><td>0.01 <b>(+121.74%)</b></td><td>0.01 <b>(+52.59%)</b></td><td>490.90 <b>(-54.91%)</b></td><td>394.90 <b>(-32.43%)</b></td><td>407.60 (-16.39%)</td><td>218.90 <b>(-41.52%)</b></td><td>106.92 <b>(-63.24%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1088.60 (n/a)</td><td>584.40 (n/a)</td><td>487.50 (n/a)</td><td>374.30 (n/a)</td><td>290.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+7.10%)</td><td>0.01 <b>(+39.01%)</b></td><td>0.01 <b>(+79.73%)</b></td><td>0.01 <b>(+27.74%)</b></td><td>0.00 (-7.77%)</td><td>489.50 <b>(-21.72%)</b></td><td>340.70 <b>(-30.13%)</b></td><td>295.20 <b>(-44.36%)</b></td><td>241.20 (-6.62%)</td><td>101.55 <b>(-26.27%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>625.30 (n/a)</td><td>487.64 (n/a)</td><td>530.60 (n/a)</td><td>258.30 (n/a)</td><td>137.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-10.91%)</td><td>0.01 (+7.56%)</td><td>0.01 (+10.51%)</td><td>0.01 (+12.55%)</td><td>0.00 <b>(-27.55%)</b></td><td>677.20 (-11.16%)</td><td>475.96 (-11.98%)</td><td>478.40 (-9.50%)</td><td>300.30 (+12.22%)</td><td>139.01 <b>(-24.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>762.30 (n/a)</td><td>540.76 (n/a)</td><td>528.60 (n/a)</td><td>267.60 (n/a)</td><td>184.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-9.17%)</td><td>0.01 (+1.19%)</td><td>0.02 (+11.96%)</td><td>0.01 (-8.23%)</td><td>0.01 (-2.05%)</td><td>630.70 (+8.97%)</td><td>386.84 (+0.76%)</td><td>271.10 (-10.70%)</td><td>215.60 (+10.11%)</td><td>196.54 (+11.51%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.80 (n/a)</td><td>383.94 (n/a)</td><td>303.60 (n/a)</td><td>195.80 (n/a)</td><td>176.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (-2.10%)</td><td>0.01 (+0.43%)</td><td>0.01 (+1.30%)</td><td>0.01 (+4.57%)</td><td>0.00 (-7.69%)</td><td>506.90 (-4.36%)</td><td>391.32 (-1.19%)</td><td>407.30 (-1.28%)</td><td>276.10 (+2.11%)</td><td>85.71 (-9.81%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.00 (n/a)</td><td>396.04 (n/a)</td><td>412.60 (n/a)</td><td>270.40 (n/a)</td><td>95.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(-37.67%)</b></td><td>0.01 (-10.76%)</td><td>0.01 (-5.42%)</td><td>0.01 (+12.95%)</td><td>0.00 <b>(-67.94%)</b></td><td>487.70 (-11.47%)</td><td>437.26 (+3.04%)</td><td>470.70 (+5.73%)</td><td>371.10 <b>(+60.44%)</b></td><td>59.22 <b>(-54.69%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.90 (n/a)</td><td>424.38 (n/a)</td><td>445.20 (n/a)</td><td>231.30 (n/a)</td><td>130.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 (+5.77%)</td><td>0.01 (+9.46%)</td><td>0.01 <b>(+27.32%)</b></td><td>0.01 (+0.33%)</td><td>0.00 (+10.98%)</td><td>631.70 (-0.33%)</td><td>440.78 (-7.40%)</td><td>425.30 <b>(-21.46%)</b></td><td>273.90 (-5.45%)</td><td>151.54 (+5.86%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.80 (n/a)</td><td>475.98 (n/a)</td><td>541.50 (n/a)</td><td>289.70 (n/a)</td><td>143.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(+29.42%)</b></td><td>0.01 <b>(+21.04%)</b></td><td>0.01 (-0.24%)</td><td>0.01 (-4.00%)</td><td>0.00 <b>(+100.33%)</b></td><td>546.60 (+4.17%)</td><td>411.66 (-9.64%)</td><td>483.70 (+0.23%)</td><td>233.80 <b>(-22.74%)</b></td><td>150.43 <b>(+66.37%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.70 (n/a)</td><td>455.58 (n/a)</td><td>482.60 (n/a)</td><td>302.60 (n/a)</td><td>90.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(+49.96%)</b></td><td>0.01 (+14.70%)</td><td>0.01 (+13.91%)</td><td>0.01 (-15.30%)</td><td>0.00 <b>(+181.89%)</b></td><td>683.80 (+18.06%)</td><td>485.08 (-6.06%)</td><td>480.30 (-12.21%)</td><td>271.70 <b>(-33.33%)</b></td><td>148.67 <b>(+111.75%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.20 (n/a)</td><td>516.36 (n/a)</td><td>547.10 (n/a)</td><td>407.50 (n/a)</td><td>70.21 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.01 <b>(+32.54%)</b></td><td>0.01 (+18.75%)</td><td>0.01 (+6.60%)</td><td>0.01 (+15.69%)</td><td>0.00 <b>(+55.22%)</b></td><td>678.50 (-13.56%)</td><td>511.90 (-12.92%)</td><td>560.60 (-6.18%)</td><td>275.60 <b>(-24.53%)</b></td><td>151.64 (-0.01%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>784.90 (n/a)</td><td>587.86 (n/a)</td><td>597.50 (n/a)</td><td>365.20 (n/a)</td><td>151.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-2.17%)</td><td>0.03 <b>(+30.39%)</b></td><td>0.03 (+9.82%)</td><td>0.03 <b>(+110.95%)</b></td><td>0.00 <b>(-84.45%)</b></td><td>280.30 <b>(-52.59%)</b></td><td>269.28 <b>(-32.88%)</b></td><td>272.00 (-8.97%)</td><td>249.50 (+2.21%)</td><td>11.66 <b>(-93.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.20 (n/a)</td><td>401.20 (n/a)</td><td>298.80 (n/a)</td><td>244.10 (n/a)</td><td>168.51 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (+9.35%)</td><td>0.04 <b>(+43.59%)</b></td><td>0.04 <b>(+93.41%)</b></td><td>0.02 <b>(+112.68%)</b></td><td>0.01 (-16.68%)</td><td>516.10 <b>(-52.98%)</b></td><td>359.00 <b>(-40.15%)</b></td><td>289.50 <b>(-48.29%)</b></td><td>243.40 (-8.53%)</td><td>121.78 <b>(-62.66%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1097.60 (n/a)</td><td>599.86 (n/a)</td><td>559.90 (n/a)</td><td>266.10 (n/a)</td><td>326.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(-32.11%)</b></td><td>0.02 (-6.89%)</td><td>0.02 (+1.57%)</td><td>0.01 (+0.28%)</td><td>0.00 <b>(-51.52%)</b></td><td>614.20 (-0.28%)</td><td>449.36 (-0.51%)</td><td>440.00 (-1.54%)</td><td>329.30 <b>(+47.27%)</b></td><td>111.75 <b>(-25.72%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.90 (n/a)</td><td>451.68 (n/a)</td><td>446.90 (n/a)</td><td>223.60 (n/a)</td><td>150.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.04 <b>(-20.74%)</b></td><td>0.03 (-8.05%)</td><td>0.04 <b>(+45.63%)</b></td><td>0.02 (-13.63%)</td><td>0.01 <b>(-34.27%)</b></td><td>623.50 (+15.78%)</td><td>377.88 (+2.01%)</td><td>280.20 <b>(-31.34%)</b></td><td>241.10 <b>(+26.16%)</b></td><td>162.57 (-1.03%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>538.50 (n/a)</td><td>370.44 (n/a)</td><td>408.10 (n/a)</td><td>191.10 (n/a)</td><td>164.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (+0.28%)</td><td>0.02 <b>(-24.02%)</b></td><td>0.02 <b>(-38.60%)</b></td><td>0.01 (-19.63%)</td><td>0.01 (+17.56%)</td><td>750.30 <b>(+24.43%)</b></td><td>472.94 <b>(+38.15%)</b></td><td>458.60 <b>(+62.86%)</b></td><td>248.10 (-0.28%)</td><td>197.76 <b>(+34.72%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.00 (n/a)</td><td>342.34 (n/a)</td><td>281.60 (n/a)</td><td>248.80 (n/a)</td><td>146.79 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 <b>(+74.57%)</b></td><td>0.03 <b>(+33.59%)</b></td><td>0.02 (+8.13%)</td><td>0.02 <b>(+47.71%)</b></td><td>0.02 <b>(+116.99%)</b></td><td>547.20 <b>(-32.30%)</b></td><td>414.68 (-18.31%)</td><td>452.60 (-7.54%)</td><td>155.30 <b>(-42.71%)</b></td><td>150.65 <b>(-21.95%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>808.30 (n/a)</td><td>507.64 (n/a)</td><td>489.50 (n/a)</td><td>271.10 (n/a)</td><td>193.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (-16.45%)</td><td>0.02 (+3.05%)</td><td>0.02 <b>(+25.05%)</b></td><td>0.01 <b>(+30.02%)</b></td><td>0.01 <b>(-39.35%)</b></td><td>602.20 <b>(-23.09%)</b></td><td>444.58 (-11.81%)</td><td>408.90 <b>(-20.03%)</b></td><td>319.60 (+19.66%)</td><td>120.84 <b>(-42.50%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>783.00 (n/a)</td><td>504.10 (n/a)</td><td>511.30 (n/a)</td><td>267.10 (n/a)</td><td>210.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 <b>(+45.45%)</b></td><td>0.03 (+13.24%)</td><td>0.02 (-1.94%)</td><td>0.02 (+14.89%)</td><td>0.01 <b>(+49.04%)</b></td><td>574.00 (-12.96%)</td><td>412.52 (-7.46%)</td><td>427.50 (+1.98%)</td><td>193.40 <b>(-31.25%)</b></td><td>167.64 (-2.78%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>659.50 (n/a)</td><td>445.76 (n/a)</td><td>419.20 (n/a)</td><td>281.30 (n/a)</td><td>172.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.03 (+3.74%)</td><td>0.02 (+7.01%)</td><td>0.02 (-5.97%)</td><td>0.01 <b>(+80.07%)</b></td><td>0.01 (-9.09%)</td><td>1094.20 <b>(-44.47%)</b></td><td>535.58 <b>(-26.18%)</b></td><td>471.70 (+6.36%)</td><td>254.30 (-3.60%)</td><td>324.71 <b>(-53.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1970.40 (n/a)</td><td>725.56 (n/a)</td><td>443.50 (n/a)</td><td>263.80 (n/a)</td><td>704.18 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 <b>(+38.59%)</b></td><td>0.03 (+6.52%)</td><td>0.02 (-16.52%)</td><td>0.02 (+14.76%)</td><td>0.02 <b>(+41.63%)</b></td><td>571.10 (-12.86%)</td><td>428.34 (+0.15%)</td><td>551.80 (+19.77%)</td><td>163.10 <b>(-27.83%)</b></td><td>190.05 (+0.94%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.40 (n/a)</td><td>427.70 (n/a)</td><td>460.70 (n/a)</td><td>226.00 (n/a)</td><td>188.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.02 <b>(-28.00%)</b></td><td>0.02 (+4.48%)</td><td>0.02 (+3.01%)</td><td>0.02 <b>(+61.81%)</b></td><td>0.00 <b>(-68.56%)</b></td><td>494.90 <b>(-38.20%)</b></td><td>446.52 (-14.28%)</td><td>468.80 (-2.92%)</td><td>381.00 <b>(+38.90%)</b></td><td>53.65 <b>(-72.21%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>800.80 (n/a)</td><td>520.90 (n/a)</td><td>482.90 (n/a)</td><td>274.30 (n/a)</td><td>193.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-15.89%)</td><td>0.04 <b>(-21.86%)</b></td><td>0.04 <b>(-43.72%)</b></td><td>0.02 <b>(-30.56%)</b></td><td>0.02 (-16.08%)</td><td>821.10 <b>(+44.00%)</b></td><td>463.12 <b>(+30.16%)</b></td><td>459.50 <b>(+77.69%)</b></td><td>280.80 (+18.88%)</td><td>218.91 <b>(+41.85%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.20 (n/a)</td><td>355.80 (n/a)</td><td>258.60 (n/a)</td><td>236.20 (n/a)</td><td>154.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (-16.24%)</td><td>0.06 <b>(-20.02%)</b></td><td>0.06 (-16.75%)</td><td>0.02 <b>(-51.32%)</b></td><td>0.02 (+1.05%)</td><td>1047.20 <b>(+105.45%)</b></td><td>519.64 <b>(+38.88%)</b></td><td>392.60 <b>(+20.13%)</b></td><td>306.20 (+19.42%)</td><td>300.92 <b>(+159.01%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>509.70 (n/a)</td><td>374.16 (n/a)</td><td>326.80 (n/a)</td><td>256.40 (n/a)</td><td>116.18 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-0.82%)</td><td>0.04 (-6.81%)</td><td>0.03 (-19.84%)</td><td>0.03 (-15.48%)</td><td>0.02 (+16.50%)</td><td>588.80 (+18.30%)</td><td>418.50 (+11.60%)</td><td>483.30 <b>(+24.72%)</b></td><td>256.10 (+0.87%)</td><td>147.76 <b>(+33.33%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>497.70 (n/a)</td><td>375.00 (n/a)</td><td>387.50 (n/a)</td><td>253.90 (n/a)</td><td>110.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (-12.19%)</td><td>0.06 (+14.17%)</td><td>0.07 <b>(+64.90%)</b></td><td>0.04 (+7.99%)</td><td>0.02 (-10.04%)</td><td>501.10 (-7.41%)</td><td>355.22 (-13.51%)</td><td>277.40 <b>(-39.35%)</b></td><td>250.10 (+13.89%)</td><td>130.66 (-4.06%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>541.20 (n/a)</td><td>410.72 (n/a)</td><td>457.40 (n/a)</td><td>219.60 (n/a)</td><td>136.18 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 <b>(-20.72%)</b></td><td>0.04 <b>(-25.08%)</b></td><td>0.03 <b>(-41.92%)</b></td><td>0.03 (-6.34%)</td><td>0.01 <b>(-34.66%)</b></td><td>612.00 (+6.77%)</td><td>466.98 <b>(+26.93%)</b></td><td>482.60 <b>(+72.17%)</b></td><td>298.60 <b>(+26.15%)</b></td><td>129.83 (-12.87%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.20 (n/a)</td><td>367.90 (n/a)</td><td>280.30 (n/a)</td><td>236.70 (n/a)</td><td>149.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 <b>(+107.74%)</b></td><td>0.05 <b>(+56.82%)</b></td><td>0.04 (+17.11%)</td><td>0.04 <b>(+109.68%)</b></td><td>0.02 <b>(+111.21%)</b></td><td>491.50 <b>(-52.30%)</b></td><td>417.44 <b>(-36.25%)</b></td><td>477.00 (-14.61%)</td><td>255.70 <b>(-51.86%)</b></td><td>100.71 <b>(-52.58%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1030.50 (n/a)</td><td>654.76 (n/a)</td><td>558.60 (n/a)</td><td>531.20 (n/a)</td><td>212.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-2.55%)</td><td>0.04 <b>(-32.14%)</b></td><td>0.03 <b>(-50.99%)</b></td><td>0.03 (-16.83%)</td><td>0.02 (+17.67%)</td><td>596.60 <b>(+20.23%)</b></td><td>467.90 <b>(+53.73%)</b></td><td>552.80 <b>(+104.06%)</b></td><td>241.30 (+2.59%)</td><td>150.63 <b>(+38.93%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>496.20 (n/a)</td><td>304.36 (n/a)</td><td>270.90 (n/a)</td><td>235.20 (n/a)</td><td>108.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 <b>(+47.36%)</b></td><td>0.04 (+19.50%)</td><td>0.04 (+17.51%)</td><td>0.03 (-4.23%)</td><td>0.01 <b>(+132.32%)</b></td><td>644.20 (+4.43%)</td><td>447.36 (-12.27%)</td><td>436.60 (-14.91%)</td><td>288.10 <b>(-32.15%)</b></td><td>127.83 <b>(+65.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>616.90 (n/a)</td><td>509.92 (n/a)</td><td>513.10 (n/a)</td><td>424.60 (n/a)</td><td>77.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 <b>(+36.37%)</b></td><td>0.05 (-10.76%)</td><td>0.05 (-19.55%)</td><td>0.03 <b>(-25.71%)</b></td><td>0.03 <b>(+110.10%)</b></td><td>586.50 <b>(+34.61%)</b></td><td>382.54 <b>(+31.53%)</b></td><td>320.70 <b>(+24.30%)</b></td><td>172.20 <b>(-26.66%)</b></td><td>185.61 <b>(+121.79%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>435.70 (n/a)</td><td>290.84 (n/a)</td><td>258.00 (n/a)</td><td>234.80 (n/a)</td><td>83.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-19.69%)</td><td>0.05 (+12.89%)</td><td>0.04 <b>(+20.69%)</b></td><td>0.04 <b>(+23.66%)</b></td><td>0.01 <b>(-38.97%)</b></td><td>471.80 (-19.13%)</td><td>390.56 (-16.93%)</td><td>419.00 (-17.14%)</td><td>292.90 <b>(+24.53%)</b></td><td>88.72 <b>(-35.56%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.40 (n/a)</td><td>470.16 (n/a)</td><td>505.70 (n/a)</td><td>235.20 (n/a)</td><td>137.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (+14.66%)</td><td>0.04 (+6.27%)</td><td>0.05 <b>(+23.61%)</b></td><td>0.03 (-17.23%)</td><td>0.01 <b>(+45.19%)</b></td><td>591.40 <b>(+20.82%)</b></td><td>396.58 (-1.83%)</td><td>357.10 (-19.10%)</td><td>251.70 (-12.79%)</td><td>127.30 <b>(+56.25%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>489.50 (n/a)</td><td>403.98 (n/a)</td><td>441.40 (n/a)</td><td>288.60 (n/a)</td><td>81.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (-0.18%)</td><td>0.08 (-17.66%)</td><td>0.07 <b>(-34.36%)</b></td><td>0.05 <b>(-23.95%)</b></td><td>0.03 <b>(+46.39%)</b></td><td>667.40 <b>(+31.51%)</b></td><td>447.24 <b>(+29.65%)</b></td><td>473.10 <b>(+52.32%)</b></td><td>281.60 (+0.18%)</td><td>162.51 <b>(+74.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>507.50 (n/a)</td><td>344.96 (n/a)</td><td>310.60 (n/a)</td><td>281.10 (n/a)</td><td>93.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (-8.74%)</td><td>0.10 <b>(+21.30%)</b></td><td>0.11 <b>(+96.72%)</b></td><td>0.06 <b>(+29.57%)</b></td><td>0.03 <b>(-31.39%)</b></td><td>552.70 <b>(-22.83%)</b></td><td>366.56 <b>(-25.12%)</b></td><td>292.20 <b>(-49.17%)</b></td><td>283.90 (+9.57%)</td><td>118.03 <b>(-41.65%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>716.20 (n/a)</td><td>489.54 (n/a)</td><td>574.90 (n/a)</td><td>259.10 (n/a)</td><td>202.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 <b>(+21.53%)</b></td><td>0.12 <b>(+48.80%)</b></td><td>0.11 <b>(+53.41%)</b></td><td>0.08 <b>(+58.65%)</b></td><td>0.04 (+8.97%)</td><td>498.20 <b>(-36.97%)</b></td><td>356.52 <b>(-34.99%)</b></td><td>366.50 <b>(-34.81%)</b></td><td>245.80 (-17.71%)</td><td>102.40 <b>(-41.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>790.40 (n/a)</td><td>548.44 (n/a)</td><td>562.20 (n/a)</td><td>298.70 (n/a)</td><td>176.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (-17.33%)</td><td>0.08 <b>(-21.81%)</b></td><td>0.07 <b>(-34.18%)</b></td><td>0.05 <b>(+33.13%)</b></td><td>0.03 <b>(-28.10%)</b></td><td>614.70 <b>(-24.89%)</b></td><td>469.22 (+15.63%)</td><td>493.30 <b>(+51.92%)</b></td><td>268.20 <b>(+20.92%)</b></td><td>141.62 <b>(-40.24%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>818.40 (n/a)</td><td>405.80 (n/a)</td><td>324.70 (n/a)</td><td>221.80 (n/a)</td><td>236.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 <b>(+31.99%)</b></td><td>0.12 <b>(+58.18%)</b></td><td>0.13 <b>(+55.14%)</b></td><td>0.06 <b>(+171.58%)</b></td><td>0.04 (+5.85%)</td><td>694.80 <b>(-63.18%)</b></td><td>379.58 <b>(-49.39%)</b></td><td>322.50 <b>(-35.55%)</b></td><td>271.50 <b>(-24.23%)</b></td><td>177.83 <b>(-72.23%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1886.90 (n/a)</td><td>750.08 (n/a)</td><td>500.40 (n/a)</td><td>358.30 (n/a)</td><td>640.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 <b>(+23.58%)</b></td><td>0.08 (+1.48%)</td><td>0.07 (-2.73%)</td><td>0.05 (+0.51%)</td><td>0.04 <b>(+51.42%)</b></td><td>595.80 (-0.52%)</td><td>469.64 (+3.69%)</td><td>472.30 (+2.81%)</td><td>230.20 (-19.06%)</td><td>146.32 (+18.36%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>598.90 (n/a)</td><td>452.94 (n/a)</td><td>459.40 (n/a)</td><td>284.40 (n/a)</td><td>123.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.20 <b>(+148.55%)</b></td><td>0.10 <b>(+52.65%)</b></td><td>0.08 <b>(+22.04%)</b></td><td>0.02 <b>(-70.59%)</b></td><td>0.07 <b>(+623.24%)</b></td><td>2394.40 <b>(+240.02%)</b></td><td>785.70 <b>(+32.98%)</b></td><td>486.60 (-18.07%)</td><td>187.80 <b>(-59.76%)</b></td><td>913.24 <b>(+982.58%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>704.20 (n/a)</td><td>590.86 (n/a)</td><td>593.90 (n/a)</td><td>466.70 (n/a)</td><td>84.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (-15.23%)</td><td>0.09 (+3.44%)</td><td>0.07 (-0.04%)</td><td>0.06 <b>(+285.15%)</b></td><td>0.03 <b>(-43.97%)</b></td><td>507.30 <b>(-74.04%)</b></td><td>405.62 <b>(-41.45%)</b></td><td>456.30 (+0.04%)</td><td>238.20 (+17.98%)</td><td>119.77 <b>(-83.37%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1954.00 (n/a)</td><td>692.72 (n/a)</td><td>456.10 (n/a)</td><td>201.90 (n/a)</td><td>720.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (+8.74%)</td><td>0.11 <b>(+41.57%)</b></td><td>0.12 <b>(+69.72%)</b></td><td>0.07 <b>(+43.94%)</b></td><td>0.03 (-13.48%)</td><td>547.70 <b>(-30.52%)</b></td><td>350.96 <b>(-32.76%)</b></td><td>314.70 <b>(-41.08%)</b></td><td>252.00 (-8.03%)</td><td>113.90 <b>(-38.00%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>788.30 (n/a)</td><td>521.92 (n/a)</td><td>534.10 (n/a)</td><td>274.00 (n/a)</td><td>183.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.11 <b>(-39.47%)</b></td><td>0.09 (-5.18%)</td><td>0.09 <b>(+32.16%)</b></td><td>0.08 <b>(+24.94%)</b></td><td>0.01 <b>(-79.10%)</b></td><td>399.40 (-19.96%)</td><td>362.40 (-7.77%)</td><td>359.50 <b>(-24.33%)</b></td><td>305.50 <b>(+65.22%)</b></td><td>36.85 <b>(-72.88%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>499.00 (n/a)</td><td>392.92 (n/a)</td><td>475.10 (n/a)</td><td>184.90 (n/a)</td><td>135.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-13.08%)</td><td>0.05 (+3.65%)</td><td>0.04 (-4.28%)</td><td>0.03 <b>(+21.40%)</b></td><td>0.02 (-16.89%)</td><td>587.10 (-17.62%)</td><td>428.56 (-7.23%)</td><td>463.90 (+4.48%)</td><td>286.50 (+15.01%)</td><td>131.79 <b>(-24.01%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>712.70 (n/a)</td><td>461.96 (n/a)</td><td>444.00 (n/a)</td><td>249.10 (n/a)</td><td>173.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 (-1.86%)</td><td>0.06 <b>(+40.64%)</b></td><td>0.07 <b>(+56.25%)</b></td><td>0.03 <b>(+213.54%)</b></td><td>0.02 <b>(-27.81%)</b></td><td>618.40 <b>(-68.11%)</b></td><td>352.08 <b>(-50.51%)</b></td><td>281.00 <b>(-36.01%)</b></td><td>269.10 (+1.89%)</td><td>149.77 <b>(-78.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1938.90 (n/a)</td><td>711.36 (n/a)</td><td>439.10 (n/a)</td><td>264.10 (n/a)</td><td>694.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 <b>(-33.77%)</b></td><td>0.05 (-3.28%)</td><td>0.05 (+9.39%)</td><td>0.04 (+3.72%)</td><td>0.01 <b>(-50.13%)</b></td><td>558.80 (-3.59%)</td><td>399.66 (-5.05%)</td><td>403.10 (-8.57%)</td><td>287.20 <b>(+51.00%)</b></td><td>110.60 <b>(-22.21%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>579.60 (n/a)</td><td>420.90 (n/a)</td><td>440.90 (n/a)</td><td>190.20 (n/a)</td><td>142.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.06 (-18.23%)</td><td>0.04 (-7.22%)</td><td>0.04 (+14.23%)</td><td>0.02 <b>(-28.78%)</b></td><td>0.02 <b>(-20.83%)</b></td><td>847.10 <b>(+40.41%)</b></td><td>542.38 (+8.49%)</td><td>495.10 (-12.46%)</td><td>318.30 <b>(+22.28%)</b></td><td>199.75 <b>(+40.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.30 (n/a)</td><td>499.94 (n/a)</td><td>565.60 (n/a)</td><td>260.30 (n/a)</td><td>141.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.05 (-4.59%)</td><td>0.04 (+15.42%)</td><td>0.04 (+15.48%)</td><td>0.04 <b>(+145.29%)</b></td><td>0.01 <b>(-59.02%)</b></td><td>567.50 <b>(-59.23%)</b></td><td>505.00 <b>(-27.47%)</b></td><td>521.00 (-13.40%)</td><td>403.30 (+4.81%)</td><td>66.28 <b>(-83.54%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1392.00 (n/a)</td><td>696.26 (n/a)</td><td>601.60 (n/a)</td><td>384.80 (n/a)</td><td>402.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 <b>(+50.34%)</b></td><td>0.06 <b>(+23.52%)</b></td><td>0.07 <b>(+54.51%)</b></td><td>0.01 <b>(-68.06%)</b></td><td>0.03 <b>(+175.02%)</b></td><td>2030.50 <b>(+213.06%)</b></td><td>655.96 <b>(+41.53%)</b></td><td>291.40 <b>(-35.27%)</b></td><td>238.40 <b>(-33.48%)</b></td><td>772.37 <b>(+542.38%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>648.60 (n/a)</td><td>463.48 (n/a)</td><td>450.20 (n/a)</td><td>358.40 (n/a)</td><td>120.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (-3.49%)</td><td>0.08 <b>(+30.68%)</b></td><td>0.09 <b>(+65.57%)</b></td><td>0.05 <b>(+24.72%)</b></td><td>0.02 <b>(-27.33%)</b></td><td>475.00 (-19.83%)</td><td>312.76 <b>(-28.02%)</b></td><td>288.50 <b>(-39.61%)</b></td><td>250.00 (+3.61%)</td><td>92.77 <b>(-38.03%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>592.50 (n/a)</td><td>434.52 (n/a)</td><td>477.70 (n/a)</td><td>241.30 (n/a)</td><td>149.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 (-12.63%)</td><td>0.08 (+8.82%)</td><td>0.08 (+8.49%)</td><td>0.07 <b>(+21.39%)</b></td><td>0.01 <b>(-44.56%)</b></td><td>374.30 (-17.63%)</td><td>299.92 (-12.66%)</td><td>306.90 (-7.81%)</td><td>248.90 (+14.44%)</td><td>49.72 <b>(-49.24%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>454.40 (n/a)</td><td>343.38 (n/a)</td><td>332.90 (n/a)</td><td>217.50 (n/a)</td><td>97.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (+17.18%)</td><td>0.06 (+4.90%)</td><td>0.06 (+1.78%)</td><td>0.04 (-6.11%)</td><td>0.02 <b>(+50.61%)</b></td><td>599.60 (+6.52%)</td><td>413.54 (-0.58%)</td><td>420.90 (-1.75%)</td><td>274.00 (-14.67%)</td><td>133.74 <b>(+36.16%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>562.90 (n/a)</td><td>415.94 (n/a)</td><td>428.40 (n/a)</td><td>321.10 (n/a)</td><td>98.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.09 (-0.08%)</td><td>0.06 (+15.86%)</td><td>0.06 (+14.79%)</td><td>0.04 (-3.34%)</td><td>0.02 (+5.87%)</td><td>605.50 (+3.45%)</td><td>410.86 (-12.77%)</td><td>418.30 (-12.87%)</td><td>279.20 (+0.11%)</td><td>131.33 (+10.37%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>585.30 (n/a)</td><td>471.02 (n/a)</td><td>480.10 (n/a)</td><td>278.90 (n/a)</td><td>118.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.10 <b>(+22.54%)</b></td><td>0.07 (+4.33%)</td><td>0.05 <b>(-31.57%)</b></td><td>0.04 (+7.24%)</td><td>0.03 <b>(+43.66%)</b></td><td>549.80 (-6.75%)</td><td>408.74 (-0.38%)</td><td>481.50 <b>(+46.13%)</b></td><td>238.80 (-18.41%)</td><td>140.90 (+7.24%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>589.60 (n/a)</td><td>410.30 (n/a)</td><td>329.50 (n/a)</td><td>292.70 (n/a)</td><td>131.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 <b>(-32.61%)</b></td><td>0.06 (-4.69%)</td><td>0.06 <b>(+26.41%)</b></td><td>0.04 (-10.05%)</td><td>0.02 <b>(-41.95%)</b></td><td>673.50 (+11.18%)</td><td>457.90 (-2.26%)</td><td>418.20 <b>(-20.89%)</b></td><td>290.70 <b>(+48.39%)</b></td><td>166.09 (-2.08%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>605.80 (n/a)</td><td>468.50 (n/a)</td><td>528.60 (n/a)</td><td>195.90 (n/a)</td><td>169.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 <b>(+36.91%)</b></td><td>0.07 <b>(+46.45%)</b></td><td>0.07 <b>(+49.61%)</b></td><td>0.04 <b>(+26.61%)</b></td><td>0.01 <b>(+22.76%)</b></td><td>449.80 <b>(-21.02%)</b></td><td>296.82 <b>(-32.21%)</b></td><td>272.60 <b>(-33.17%)</b></td><td>230.60 <b>(-26.96%)</b></td><td>87.98 <b>(-27.87%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.50 (n/a)</td><td>437.84 (n/a)</td><td>407.90 (n/a)</td><td>315.70 (n/a)</td><td>121.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-11.11%)</td><td>0.05 (-9.28%)</td><td>0.05 (-9.49%)</td><td>0.04 <b>(+22.79%)</b></td><td>0.01 (-19.34%)</td><td>498.90 (-18.56%)</td><td>374.06 (+5.56%)</td><td>347.30 (+10.46%)</td><td>253.70 (+12.51%)</td><td>106.20 <b>(-29.09%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>612.60 (n/a)</td><td>354.36 (n/a)</td><td>314.40 (n/a)</td><td>225.50 (n/a)</td><td>149.78 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-0.72%)</td><td>0.05 (-2.59%)</td><td>0.05 (-3.96%)</td><td>0.04 (-0.97%)</td><td>0.02 (+17.28%)</td><td>502.70 (+0.98%)</td><td>384.94 (+5.24%)</td><td>400.40 (+4.11%)</td><td>261.40 (+0.73%)</td><td>119.90 <b>(+21.28%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>497.80 (n/a)</td><td>365.76 (n/a)</td><td>384.60 (n/a)</td><td>259.50 (n/a)</td><td>98.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 <b>(+51.69%)</b></td><td>0.05 (+17.65%)</td><td>0.05 (+3.10%)</td><td>0.01 <b>(-75.70%)</b></td><td>0.03 <b>(+222.44%)</b></td><td>2544.30 <b>(+311.57%)</b></td><td>763.10 <b>(+72.84%)</b></td><td>379.70 (-2.99%)</td><td>227.30 <b>(-34.08%)</b></td><td>999.15 <b>(+825.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>618.20 (n/a)</td><td>441.50 (n/a)</td><td>391.40 (n/a)</td><td>344.80 (n/a)</td><td>108.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (+1.99%)</td><td>0.05 (+5.01%)</td><td>0.04 (+17.33%)</td><td>0.03 (-4.97%)</td><td>0.02 (+1.59%)</td><td>615.50 (+5.21%)</td><td>423.82 (-4.67%)</td><td>422.40 (-14.77%)</td><td>266.40 (-1.95%)</td><td>154.64 (+0.54%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.00 (n/a)</td><td>444.60 (n/a)</td><td>495.60 (n/a)</td><td>271.70 (n/a)</td><td>153.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.08 <b>(+85.56%)</b></td><td>0.05 <b>(+39.20%)</b></td><td>0.04 (+12.18%)</td><td>0.03 (-4.18%)</td><td>0.02 <b>(+481.59%)</b></td><td>609.00 (+4.37%)</td><td>411.86 (-19.57%)</td><td>459.40 (-10.85%)</td><td>242.70 <b>(-46.10%)</b></td><td>151.82 <b>(+211.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>583.50 (n/a)</td><td>512.10 (n/a)</td><td>515.30 (n/a)</td><td>450.30 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.38 (-4.04%)</td><td>0.29 (+0.66%)</td><td>0.33 (-2.93%)</td><td>0.20 (+11.32%)</td><td>0.08 <b>(-22.07%)</b></td><td>483.70 (-10.16%)</td><td>359.48 (-5.25%)</td><td>301.60 (+3.01%)</td><td>261.50 (+4.22%)</td><td>102.36 <b>(-29.04%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>538.40 (n/a)</td><td>379.38 (n/a)</td><td>292.80 (n/a)</td><td>250.90 (n/a)</td><td>144.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.38 (+16.34%)</td><td>0.24 (+9.54%)</td><td>0.21 (+6.82%)</td><td>0.15 (-3.18%)</td><td>0.10 <b>(+46.61%)</b></td><td>642.70 (+3.28%)</td><td>456.26 (-3.31%)</td><td>475.10 (-6.38%)</td><td>255.30 (-14.07%)</td><td>163.68 <b>(+35.40%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>622.30 (n/a)</td><td>471.90 (n/a)</td><td>507.50 (n/a)</td><td>297.10 (n/a)</td><td>120.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.37 (-0.61%)</td><td>0.24 (-14.49%)</td><td>0.22 <b>(-21.18%)</b></td><td>0.15 (-12.85%)</td><td>0.08 (-5.99%)</td><td>638.80 (+14.75%)</td><td>452.82 (+16.73%)</td><td>437.80 <b>(+26.90%)</b></td><td>268.50 (+0.64%)</td><td>138.11 (+6.88%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>556.70 (n/a)</td><td>387.92 (n/a)</td><td>345.00 (n/a)</td><td>266.80 (n/a)</td><td>129.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.24 <b>(-30.05%)</b></td><td>0.16 <b>(-31.60%)</b></td><td>0.15 <b>(-31.95%)</b></td><td>0.13 (-6.11%)</td><td>0.05 <b>(-46.49%)</b></td><td>569.40 (+6.51%)</td><td>479.72 <b>(+37.73%)</b></td><td>507.60 <b>(+46.92%)</b></td><td>305.90 <b>(+42.94%)</b></td><td>107.16 (-17.50%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>534.60 (n/a)</td><td>348.30 (n/a)</td><td>345.50 (n/a)</td><td>214.00 (n/a)</td><td>129.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.25 <b>(-31.81%)</b></td><td>0.19 (+5.09%)</td><td>0.18 <b>(+34.93%)</b></td><td>0.12 (-2.91%)</td><td>0.05 <b>(-50.56%)</b></td><td>612.00 (+3.00%)</td><td>416.90 (-13.82%)</td><td>416.50 <b>(-25.89%)</b></td><td>297.60 <b>(+46.60%)</b></td><td>124.51 <b>(-22.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.36 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>594.20 (n/a)</td><td>483.78 (n/a)</td><td>562.00 (n/a)</td><td>203.00 (n/a)</td><td>160.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.30 <b>(+21.27%)</b></td><td>0.23 <b>(+40.98%)</b></td><td>0.26 <b>(+77.60%)</b></td><td>0.17 <b>(+24.96%)</b></td><td>0.06 <b>(+33.34%)</b></td><td>444.10 (-19.97%)</td><td>333.40 <b>(-28.17%)</b></td><td>283.60 <b>(-43.69%)</b></td><td>246.40 (-17.56%)</td><td>94.20 (-5.58%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>554.90 (n/a)</td><td>464.18 (n/a)</td><td>503.60 (n/a)</td><td>298.90 (n/a)</td><td>99.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (-6.11%)</td><td>0.10 (-0.79%)</td><td>0.08 (+9.54%)</td><td>0.06 (-3.95%)</td><td>0.04 (-6.00%)</td><td>592.10 (+4.11%)</td><td>428.50 (+0.02%)</td><td>458.60 (-8.70%)</td><td>264.30 (+6.49%)</td><td>155.05 (+0.11%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>568.70 (n/a)</td><td>428.40 (n/a)</td><td>502.30 (n/a)</td><td>248.20 (n/a)</td><td>154.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (-3.05%)</td><td>0.11 (+7.95%)</td><td>0.12 (-7.39%)</td><td>0.07 <b>(+79.62%)</b></td><td>0.03 <b>(-36.60%)</b></td><td>562.70 <b>(-44.32%)</b></td><td>363.88 <b>(-23.43%)</b></td><td>310.10 (+7.97%)</td><td>276.50 (+3.13%)</td><td>120.12 <b>(-62.31%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1010.60 (n/a)</td><td>475.20 (n/a)</td><td>287.20 (n/a)</td><td>268.10 (n/a)</td><td>318.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 (+18.35%)</td><td>0.12 <b>(+39.47%)</b></td><td>0.14 <b>(+92.37%)</b></td><td>0.07 (+11.47%)</td><td>0.04 <b>(+32.47%)</b></td><td>529.50 (-10.28%)</td><td>333.32 <b>(-26.82%)</b></td><td>258.70 <b>(-48.02%)</b></td><td>241.00 (-15.50%)</td><td>126.10 (-3.19%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.20 (n/a)</td><td>455.48 (n/a)</td><td>497.70 (n/a)</td><td>285.20 (n/a)</td><td>130.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 <b>(-22.89%)</b></td><td>0.07 <b>(-30.38%)</b></td><td>0.06 <b>(-36.59%)</b></td><td>0.05 <b>(-29.34%)</b></td><td>0.03 (-13.64%)</td><td>800.20 <b>(+41.53%)</b></td><td>586.10 <b>(+48.45%)</b></td><td>598.20 <b>(+57.67%)</b></td><td>320.00 <b>(+29.71%)</b></td><td>207.37 <b>(+62.95%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>565.40 (n/a)</td><td>394.82 (n/a)</td><td>379.40 (n/a)</td><td>246.70 (n/a)</td><td>127.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (-17.04%)</td><td>0.09 (-12.61%)</td><td>0.08 (-1.75%)</td><td>0.07 (+3.41%)</td><td>0.02 <b>(-31.85%)</b></td><td>545.40 (-3.30%)</td><td>455.24 (+9.90%)</td><td>471.50 (+1.77%)</td><td>291.90 <b>(+20.52%)</b></td><td>103.72 (-19.61%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>564.00 (n/a)</td><td>414.22 (n/a)</td><td>463.30 (n/a)</td><td>242.20 (n/a)</td><td>129.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.15 <b>(+33.03%)</b></td><td>0.12 <b>(+31.82%)</b></td><td>0.12 <b>(+49.12%)</b></td><td>0.08 (+16.00%)</td><td>0.03 <b>(+51.41%)</b></td><td>467.10 (-13.79%)</td><td>331.52 <b>(-22.95%)</b></td><td>301.40 <b>(-32.95%)</b></td><td>253.10 <b>(-24.81%)</b></td><td>84.36 (+2.02%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>541.80 (n/a)</td><td>430.26 (n/a)</td><td>449.50 (n/a)</td><td>336.60 (n/a)</td><td>82.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (+3.14%)</td><td>0.11 (-1.95%)</td><td>0.12 (-8.39%)</td><td>0.06 (+2.45%)</td><td>0.04 (-13.07%)</td><td>730.00 (-2.39%)</td><td>408.84 (-1.72%)</td><td>330.90 (+9.14%)</td><td>251.90 (-3.04%)</td><td>190.28 (-9.98%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>747.90 (n/a)</td><td>415.98 (n/a)</td><td>303.20 (n/a)</td><td>259.80 (n/a)</td><td>211.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (-11.89%)</td><td>0.08 <b>(-28.41%)</b></td><td>0.08 <b>(-38.67%)</b></td><td>0.04 <b>(-39.64%)</b></td><td>0.04 (-8.38%)</td><td>1110.60 <b>(+65.69%)</b></td><td>608.04 <b>(+49.81%)</b></td><td>498.70 <b>(+63.03%)</b></td><td>300.50 (+13.48%)</td><td>324.13 <b>(+80.30%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>670.30 (n/a)</td><td>405.88 (n/a)</td><td>305.90 (n/a)</td><td>264.80 (n/a)</td><td>179.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (+2.53%)</td><td>0.11 (+1.44%)</td><td>0.09 (+2.25%)</td><td>0.07 (+5.83%)</td><td>0.04 (+7.79%)</td><td>566.10 (-5.51%)</td><td>411.54 (-0.72%)</td><td>436.60 (-2.22%)</td><td>258.80 (-2.45%)</td><td>130.58 (-0.23%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>599.10 (n/a)</td><td>414.54 (n/a)</td><td>446.50 (n/a)</td><td>265.30 (n/a)</td><td>130.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.16 (+18.12%)</td><td>0.09 (-10.70%)</td><td>0.08 <b>(-24.80%)</b></td><td>0.04 <b>(-42.32%)</b></td><td>0.05 <b>(+77.74%)</b></td><td>1114.90 <b>(+73.36%)</b></td><td>560.30 <b>(+35.08%)</b></td><td>524.70 <b>(+32.97%)</b></td><td>258.20 (-15.32%)</td><td>338.70 <b>(+151.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>643.10 (n/a)</td><td>414.80 (n/a)</td><td>394.60 (n/a)</td><td>304.90 (n/a)</td><td>134.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 <b>(+44.44%)</b></td><td>0.12 <b>(+22.53%)</b></td><td>0.11 (+15.70%)</td><td>0.08 (+7.14%)</td><td>0.04 <b>(+131.65%)</b></td><td>506.80 (-6.67%)</td><td>368.84 (-14.49%)</td><td>364.50 (-13.56%)</td><td>239.60 <b>(-30.77%)</b></td><td>103.80 <b>(+46.76%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>543.00 (n/a)</td><td>431.32 (n/a)</td><td>421.70 (n/a)</td><td>346.10 (n/a)</td><td>70.72 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 (+3.71%)</td><td>0.12 <b>(+29.27%)</b></td><td>0.11 <b>(+46.37%)</b></td><td>0.08 <b>(+34.71%)</b></td><td>0.04 (-9.20%)</td><td>496.50 <b>(-25.76%)</b></td><td>366.58 <b>(-25.35%)</b></td><td>358.40 <b>(-31.67%)</b></td><td>248.20 (-3.57%)</td><td>105.61 <b>(-30.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>668.80 (n/a)</td><td>491.08 (n/a)</td><td>524.50 (n/a)</td><td>257.40 (n/a)</td><td>151.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (-14.72%)</td><td>0.12 (+18.02%)</td><td>0.12 <b>(+44.48%)</b></td><td>0.07 <b>(+21.37%)</b></td><td>0.03 <b>(-38.51%)</b></td><td>502.50 (-17.61%)</td><td>316.74 <b>(-23.77%)</b></td><td>285.30 <b>(-30.79%)</b></td><td>247.80 (+17.27%)</td><td>106.18 <b>(-40.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>609.90 (n/a)</td><td>415.48 (n/a)</td><td>412.20 (n/a)</td><td>211.30 (n/a)</td><td>179.94 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 <b>(+21.16%)</b></td><td>0.09 (-8.21%)</td><td>0.08 <b>(-24.00%)</b></td><td>0.02 <b>(-73.04%)</b></td><td>0.05 <b>(+100.46%)</b></td><td>1972.10 <b>(+270.97%)</b></td><td>688.94 <b>(+75.68%)</b></td><td>425.50 <b>(+31.57%)</b></td><td>249.80 (-17.48%)</td><td>726.24 <b>(+544.18%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>531.60 (n/a)</td><td>392.16 (n/a)</td><td>323.40 (n/a)</td><td>302.70 (n/a)</td><td>112.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (-5.07%)</td><td>0.09 (-8.73%)</td><td>0.08 <b>(-34.51%)</b></td><td>0.07 (+5.73%)</td><td>0.03 (-19.40%)</td><td>520.00 (-5.42%)</td><td>408.90 (+5.48%)</td><td>462.20 <b>(+52.74%)</b></td><td>285.70 (+5.35%)</td><td>108.87 <b>(-23.78%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>549.80 (n/a)</td><td>387.64 (n/a)</td><td>302.60 (n/a)</td><td>271.20 (n/a)</td><td>142.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 (-14.52%)</td><td>0.08 (-18.68%)</td><td>0.07 (-9.58%)</td><td>0.05 <b>(-29.24%)</b></td><td>0.03 (-4.02%)</td><td>681.70 <b>(+41.34%)</b></td><td>500.32 <b>(+28.02%)</b></td><td>485.60 (+10.59%)</td><td>259.10 (+16.98%)</td><td>170.98 <b>(+64.83%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>482.30 (n/a)</td><td>390.80 (n/a)</td><td>439.10 (n/a)</td><td>221.50 (n/a)</td><td>103.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 <b>(+34.81%)</b></td><td>0.10 <b>(+24.35%)</b></td><td>0.08 (+18.24%)</td><td>0.07 (+7.30%)</td><td>0.03 <b>(+77.93%)</b></td><td>529.30 (-6.81%)</td><td>393.56 (-16.49%)</td><td>420.20 (-15.44%)</td><td>253.50 <b>(-25.83%)</b></td><td>111.98 <b>(+21.65%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>568.00 (n/a)</td><td>471.28 (n/a)</td><td>496.90 (n/a)</td><td>341.80 (n/a)</td><td>92.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.13 <b>(+42.44%)</b></td><td>0.10 <b>(+61.56%)</b></td><td>0.12 <b>(+72.44%)</b></td><td>0.06 <b>(+90.72%)</b></td><td>0.03 <b>(+32.36%)</b></td><td>588.80 <b>(-47.56%)</b></td><td>362.54 <b>(-41.03%)</b></td><td>293.40 <b>(-42.02%)</b></td><td>267.20 <b>(-29.80%)</b></td><td>133.89 <b>(-54.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1122.90 (n/a)</td><td>614.74 (n/a)</td><td>506.00 (n/a)</td><td>380.60 (n/a)</td><td>293.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.44 (-7.71%)</td><td>0.31 (-6.24%)</td><td>0.27 (-13.37%)</td><td>0.22 (+18.04%)</td><td>0.10 (-14.26%)</td><td>583.70 (-15.28%)</td><td>458.04 (+3.71%)</td><td>480.20 (+15.43%)</td><td>300.50 (+8.37%)</td><td>130.93 (-19.23%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>689.00 (n/a)</td><td>441.64 (n/a)</td><td>416.00 (n/a)</td><td>277.30 (n/a)</td><td>162.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.42 (-14.61%)</td><td>0.33 (-1.75%)</td><td>0.39 (+13.53%)</td><td>0.21 (-10.48%)</td><td>0.10 (-9.02%)</td><td>636.40 (+11.71%)</td><td>429.54 (+1.85%)</td><td>335.40 (-11.92%)</td><td>313.80 (+17.13%)</td><td>149.06 (+9.21%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>569.70 (n/a)</td><td>421.74 (n/a)</td><td>380.80 (n/a)</td><td>267.90 (n/a)</td><td>136.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.41 (-8.44%)</td><td>0.28 (-11.08%)</td><td>0.21 <b>(-24.31%)</b></td><td>0.18 (-15.66%)</td><td>0.11 <b>(+20.04%)</b></td><td>722.70 (+18.57%)</td><td>536.48 (+18.96%)</td><td>609.90 <b>(+32.13%)</b></td><td>316.60 (+9.21%)</td><td>192.46 <b>(+55.52%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>609.50 (n/a)</td><td>450.98 (n/a)</td><td>461.60 (n/a)</td><td>289.90 (n/a)</td><td>123.75 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-40.00%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-26.15%)</b></td><td>20603.53 <b>(+25.33%)</b></td><td>15809.03 <b>(+56.94%)</b></td><td>18042.25 <b>(+176.68%)</b></td><td>6534.82 (+15.89%)</td><td>5596.99 (+1.98%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16439.00 (n/a)</td><td>10073.45 (n/a)</td><td>6520.95 (n/a)</td><td>5639.02 (n/a)</td><td>5488.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.00 (-9.09%)</td><td>0.00 (-17.50%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-26.69%)</b></td><td>15780.96 (-7.51%)</td><td>12890.78 (+13.11%)</td><td>13699.66 <b>(+56.90%)</b></td><td>8600.74 <b>(+20.46%)</b></td><td>2892.46 <b>(-36.81%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17061.78 (n/a)</td><td>11396.32 (n/a)</td><td>8731.40 (n/a)</td><td>7139.74 (n/a)</td><td>4577.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.12 (-10.07%)</td><td>0.09 (-17.73%)</td><td>0.08 <b>(-20.84%)</b></td><td>0.07 (-5.31%)</td><td>0.02 (-15.59%)</td><td>28699.45 (+5.63%)</td><td>25398.59 <b>(+20.62%)</b></td><td>27191.22 <b>(+26.31%)</b></td><td>17004.26 (+11.13%)</td><td>4814.61 (-2.14%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27168.63 (n/a)</td><td>21057.45 (n/a)</td><td>21526.52 (n/a)</td><td>15300.87 (n/a)</td><td>4919.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.54 (+3.15%)</td><td>1.47 <b>(-25.77%)</b></td><td>1.71 (-4.56%)</td><td>0.31 <b>(-80.27%)</b></td><td>0.86 <b>(+128.10%)</b></td><td>3333.70 <b>(+406.80%)</b></td><td>1206.34 <b>(+121.32%)</b></td><td>612.70 (+4.77%)</td><td>412.40 (-3.06%)</td><td>1216.10 <b>(+1135.32%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.46 (n/a)</td><td>1.98 (n/a)</td><td>1.79 (n/a)</td><td>1.59 (n/a)</td><td>0.37 (n/a)</td><td>657.80 (n/a)</td><td>545.06 (n/a)</td><td>584.80 (n/a)</td><td>425.40 (n/a)</td><td>98.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.84 (+19.49%)</td><td>3.06 <b>(+41.18%)</b></td><td>3.04 <b>(+75.18%)</b></td><td>2.36 <b>(+103.43%)</b></td><td>0.57 <b>(-40.35%)</b></td><td>443.50 <b>(-50.85%)</b></td><td>353.06 <b>(-37.98%)</b></td><td>345.00 <b>(-42.92%)</b></td><td>273.30 (-16.29%)</td><td>66.53 <b>(-72.92%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.21 (n/a)</td><td>2.16 (n/a)</td><td>1.73 (n/a)</td><td>1.16 (n/a)</td><td>0.96 (n/a)</td><td>902.30 (n/a)</td><td>569.26 (n/a)</td><td>604.40 (n/a)</td><td>326.50 (n/a)</td><td>245.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.69 (+1.11%)</td><td>1.89 (-4.28%)</td><td>1.97 (+13.27%)</td><td>0.56 <b>(-60.40%)</b></td><td>0.87 <b>(+50.27%)</b></td><td>1885.10 <b>(+152.53%)</b></td><td>771.78 <b>(+35.74%)</b></td><td>531.30 (-11.70%)</td><td>389.70 (-1.09%)</td><td>631.19 <b>(+301.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.66 (n/a)</td><td>1.97 (n/a)</td><td>1.74 (n/a)</td><td>1.40 (n/a)</td><td>0.58 (n/a)</td><td>746.50 (n/a)</td><td>568.58 (n/a)</td><td>601.70 (n/a)</td><td>394.00 (n/a)</td><td>157.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.24 <b>(+32.24%)</b></td><td>2.23 <b>(+39.87%)</b></td><td>2.21 <b>(+68.43%)</b></td><td>1.05 (+10.32%)</td><td>0.84 <b>(+33.38%)</b></td><td>1000.50 (-9.36%)</td><td>547.58 <b>(-26.34%)</b></td><td>474.80 <b>(-40.63%)</b></td><td>323.80 <b>(-24.38%)</b></td><td>268.43 (-2.21%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.45 (n/a)</td><td>1.59 (n/a)</td><td>1.31 (n/a)</td><td>0.95 (n/a)</td><td>0.63 (n/a)</td><td>1103.80 (n/a)</td><td>743.34 (n/a)</td><td>799.70 (n/a)</td><td>428.20 (n/a)</td><td>274.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.59 <b>(-25.50%)</b></td><td>2.53 (-9.99%)</td><td>3.19 (+6.33%)</td><td>0.61 (+3.82%)</td><td>1.24 (-17.55%)</td><td>3418.10 (-3.68%)</td><td>1272.16 (+3.09%)</td><td>658.30 (-5.94%)</td><td>584.30 <b>(+34.23%)</b></td><td>1215.21 (-6.58%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.82 (n/a)</td><td>2.82 (n/a)</td><td>3.00 (n/a)</td><td>0.59 (n/a)</td><td>1.51 (n/a)</td><td>3548.70 (n/a)</td><td>1234.08 (n/a)</td><td>699.90 (n/a)</td><td>435.30 (n/a)</td><td>1300.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>3.91 <b>(-32.57%)</b></td><td>2.76 (-11.84%)</td><td>3.10 <b>(+21.12%)</b></td><td>0.66 <b>(-68.83%)</b></td><td>1.23 (-19.15%)</td><td>3189.80 <b>(+220.87%)</b></td><td>1154.88 <b>(+51.11%)</b></td><td>676.70 (-17.45%)</td><td>536.80 <b>(+48.33%)</b></td><td>1139.42 <b>(+359.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.79 (n/a)</td><td>3.13 (n/a)</td><td>2.56 (n/a)</td><td>2.11 (n/a)</td><td>1.52 (n/a)</td><td>994.10 (n/a)</td><td>764.28 (n/a)</td><td>819.70 (n/a)</td><td>361.90 (n/a)</td><td>247.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.65 <b>(+54.81%)</b></td><td>4.33 <b>(+27.70%)</b></td><td>4.21 (+15.59%)</td><td>2.33 (-3.71%)</td><td>1.95 <b>(+139.17%)</b></td><td>899.80 (+3.84%)</td><td>579.84 (-10.94%)</td><td>498.50 (-13.48%)</td><td>315.50 <b>(-35.41%)</b></td><td>270.59 <b>(+61.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.29 (n/a)</td><td>3.39 (n/a)</td><td>3.64 (n/a)</td><td>2.42 (n/a)</td><td>0.81 (n/a)</td><td>866.50 (n/a)</td><td>651.04 (n/a)</td><td>576.20 (n/a)</td><td>488.50 (n/a)</td><td>167.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.63 (+15.49%)</td><td>4.00 (+19.57%)</td><td>4.34 <b>(+38.10%)</b></td><td>0.59 <b>(-70.89%)</b></td><td>2.18 <b>(+45.09%)</b></td><td>3566.40 <b>(+243.48%)</b></td><td>1073.48 <b>(+48.51%)</b></td><td>483.50 <b>(-27.58%)</b></td><td>316.10 (-13.42%)</td><td>1396.09 <b>(+398.24%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.74 (n/a)</td><td>3.35 (n/a)</td><td>3.14 (n/a)</td><td>2.02 (n/a)</td><td>1.50 (n/a)</td><td>1038.30 (n/a)</td><td>722.82 (n/a)</td><td>667.60 (n/a)</td><td>365.10 (n/a)</td><td>280.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>7.64 <b>(+90.95%)</b></td><td>4.34 <b>(+140.99%)</b></td><td>4.36 <b>(+327.65%)</b></td><td>1.84 <b>(+213.22%)</b></td><td>2.14 <b>(+39.81%)</b></td><td>1141.30 <b>(-68.07%)</b></td><td>599.16 <b>(-71.37%)</b></td><td>481.30 <b>(-76.62%)</b></td><td>274.40 <b>(-47.63%)</b></td><td>330.07 <b>(-77.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.00 (n/a)</td><td>1.80 (n/a)</td><td>1.02 (n/a)</td><td>0.59 (n/a)</td><td>1.53 (n/a)</td><td>3574.60 (n/a)</td><td>2092.66 (n/a)</td><td>2058.50 (n/a)</td><td>524.00 (n/a)</td><td>1467.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>6.12 <b>(+26.42%)</b></td><td>3.20 (-0.63%)</td><td>3.15 (-8.16%)</td><td>0.58 (-5.94%)</td><td>2.03 <b>(+21.23%)</b></td><td>3610.30 (+6.32%)</td><td>1212.26 (+6.85%)</td><td>665.90 (+8.88%)</td><td>342.50 <b>(-20.90%)</b></td><td>1354.92 (+6.63%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.84 (n/a)</td><td>3.22 (n/a)</td><td>3.43 (n/a)</td><td>0.62 (n/a)</td><td>1.67 (n/a)</td><td>3395.80 (n/a)</td><td>1134.54 (n/a)</td><td>611.60 (n/a)</td><td>433.00 (n/a)</td><td>1270.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>5.26 (+9.19%)</td><td>4.17 (-2.77%)</td><td>4.83 (+16.08%)</td><td>1.24 <b>(-68.76%)</b></td><td>1.67 <b>(+391.89%)</b></td><td>3375.00 <b>(+220.06%)</b></td><td>1362.94 <b>(+38.66%)</b></td><td>868.30 (-13.85%)</td><td>797.50 (-8.42%)</td><td>1126.33 <b>(+1422.41%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.82 (n/a)</td><td>4.29 (n/a)</td><td>4.16 (n/a)</td><td>3.98 (n/a)</td><td>0.34 (n/a)</td><td>1054.50 (n/a)</td><td>982.94 (n/a)</td><td>1007.90 (n/a)</td><td>870.80 (n/a)</td><td>73.98 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>8.25 <b>(+34.91%)</b></td><td>5.29 <b>(+40.16%)</b></td><td>5.23 <b>(+36.73%)</b></td><td>1.12 (-4.66%)</td><td>2.76 <b>(+27.66%)</b></td><td>3736.50 (+4.88%)</td><td>1308.10 (-19.31%)</td><td>802.20 <b>(-26.87%)</b></td><td>508.20 <b>(-25.88%)</b></td><td>1367.45 (+13.02%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>6.12 (n/a)</td><td>3.77 (n/a)</td><td>3.82 (n/a)</td><td>1.18 (n/a)</td><td>2.16 (n/a)</td><td>3562.60 (n/a)</td><td>1621.22 (n/a)</td><td>1096.90 (n/a)</td><td>685.60 (n/a)</td><td>1209.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>8.33 (-1.56%)</td><td>4.82 <b>(-28.05%)</b></td><td>5.57 <b>(-25.83%)</b></td><td>1.16 <b>(-65.74%)</b></td><td>3.49 <b>(+71.27%)</b></td><td>3604.70 <b>(+191.88%)</b></td><td>1799.04 <b>(+157.05%)</b></td><td>752.50 <b>(+34.83%)</b></td><td>503.70 (+1.57%)</td><td>1649.12 <b>(+436.01%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>8.46 (n/a)</td><td>6.69 (n/a)</td><td>7.52 (n/a)</td><td>3.40 (n/a)</td><td>2.04 (n/a)</td><td>1235.00 (n/a)</td><td>699.88 (n/a)</td><td>558.10 (n/a)</td><td>495.90 (n/a)</td><td>307.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>10.31 <b>(+31.98%)</b></td><td>6.80 (+0.91%)</td><td>8.29 <b>(+22.93%)</b></td><td>1.12 <b>(-76.24%)</b></td><td>3.75 <b>(+198.97%)</b></td><td>3756.60 <b>(+320.81%)</b></td><td>1191.56 <b>(+85.18%)</b></td><td>505.80 (-18.66%)</td><td>406.70 <b>(-24.24%)</b></td><td>1443.87 <b>(+893.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>7.81 (n/a)</td><td>6.74 (n/a)</td><td>6.75 (n/a)</td><td>4.70 (n/a)</td><td>1.25 (n/a)</td><td>892.70 (n/a)</td><td>643.46 (n/a)</td><td>621.80 (n/a)</td><td>536.80 (n/a)</td><td>145.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>9.45 (+7.90%)</td><td>7.05 (+1.18%)</td><td>7.84 (+12.62%)</td><td>3.15 (-15.94%)</td><td>2.67 <b>(+30.17%)</b></td><td>1331.80 (+18.96%)</td><td>703.68 (+6.16%)</td><td>535.20 (-11.20%)</td><td>443.70 (-7.31%)</td><td>372.51 <b>(+40.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>8.76 (n/a)</td><td>6.97 (n/a)</td><td>6.96 (n/a)</td><td>3.75 (n/a)</td><td>2.05 (n/a)</td><td>1119.50 (n/a)</td><td>662.86 (n/a)</td><td>602.70 (n/a)</td><td>478.70 (n/a)</td><td>264.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>8.21 <b>(-22.93%)</b></td><td>7.73 (+10.16%)</td><td>7.77 (-3.47%)</td><td>6.95 <b>(+496.99%)</b></td><td>0.47 <b>(-86.53%)</b></td><td>603.80 <b>(-83.25%)</b></td><td>544.14 <b>(-51.63%)</b></td><td>539.70 (+3.59%)</td><td>511.10 <b>(+29.75%)</b></td><td>35.38 <b>(-97.45%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>10.65 (n/a)</td><td>7.02 (n/a)</td><td>8.05 (n/a)</td><td>1.16 (n/a)</td><td>3.53 (n/a)</td><td>3604.40 (n/a)</td><td>1124.96 (n/a)</td><td>521.00 (n/a)</td><td>393.90 (n/a)</td><td>1387.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>1.90 <b>(-25.91%)</b></td><td>1.25 (-5.18%)</td><td>0.96 (-11.06%)</td><td>0.84 (+0.91%)</td><td>0.49 <b>(-31.22%)</b></td><td>626.40 (-0.90%)</td><td>466.72 (+0.63%)</td><td>548.50 (+12.44%)</td><td>276.50 <b>(+35.01%)</b></td><td>158.93 (-3.44%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.56 (n/a)</td><td>1.32 (n/a)</td><td>1.07 (n/a)</td><td>0.83 (n/a)</td><td>0.71 (n/a)</td><td>632.10 (n/a)</td><td>463.78 (n/a)</td><td>487.80 (n/a)</td><td>204.80 (n/a)</td><td>164.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>2.70 (-3.49%)</td><td>1.91 (-17.90%)</td><td>2.26 (+6.72%)</td><td>0.31 <b>(-84.21%)</b></td><td>0.98 <b>(+156.56%)</b></td><td>3401.30 <b>(+533.15%)</b></td><td>1056.62 <b>(+129.17%)</b></td><td>464.60 (-6.29%)</td><td>388.20 (+3.60%)</td><td>1313.95 <b>(+1724.45%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.80 (n/a)</td><td>2.32 (n/a)</td><td>2.12 (n/a)</td><td>1.95 (n/a)</td><td>0.38 (n/a)</td><td>537.20 (n/a)</td><td>461.06 (n/a)</td><td>495.80 (n/a)</td><td>374.70 (n/a)</td><td>72.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>4.02 (+2.55%)</td><td>1.90 <b>(-42.45%)</b></td><td>0.86 <b>(-73.63%)</b></td><td>0.58 <b>(-77.61%)</b></td><td>1.69 <b>(+243.91%)</b></td><td>3595.70 <b>(+346.56%)</b></td><td>2150.46 <b>(+231.56%)</b></td><td>2442.70 <b>(+279.24%)</b></td><td>521.50 (-2.47%)</td><td>1520.15 <b>(+1395.46%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.92 (n/a)</td><td>3.29 (n/a)</td><td>3.26 (n/a)</td><td>2.60 (n/a)</td><td>0.49 (n/a)</td><td>805.20 (n/a)</td><td>648.58 (n/a)</td><td>644.10 (n/a)</td><td>534.70 (n/a)</td><td>101.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>1.50 (-9.28%)</td><td>1.05 <b>(-24.31%)</b></td><td>1.33 (-15.35%)</td><td>0.27 <b>(-71.65%)</b></td><td>0.56 <b>(+68.50%)</b></td><td>1927.10 <b>(+252.69%)</b></td><td>767.18 <b>(+92.41%)</b></td><td>393.30 (+18.14%)</td><td>348.40 (+10.22%)</td><td>677.46 <b>(+534.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>1.66 (n/a)</td><td>1.39 (n/a)</td><td>1.57 (n/a)</td><td>0.96 (n/a)</td><td>0.33 (n/a)</td><td>546.40 (n/a)</td><td>398.72 (n/a)</td><td>332.90 (n/a)</td><td>316.10 (n/a)</td><td>106.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.17 <b>(+26.14%)</b></td><td>0.12 (+18.55%)</td><td>0.11 (-1.49%)</td><td>0.08 <b>(+34.92%)</b></td><td>0.03 (+7.11%)</td><td>417.80 <b>(-25.87%)</b></td><td>294.00 (-18.27%)</td><td>299.20 (+1.53%)</td><td>192.90 <b>(-20.72%)</b></td><td>81.73 <b>(-38.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>563.60 (n/a)</td><td>359.74 (n/a)</td><td>294.70 (n/a)</td><td>243.30 (n/a)</td><td>132.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.14 (+16.49%)</td><td>0.11 (+16.01%)</td><td>0.13 (+14.81%)</td><td>0.07 (+16.15%)</td><td>0.04 (+18.71%)</td><td>494.50 (-13.91%)</td><td>335.50 (-13.44%)</td><td>260.50 (-12.91%)</td><td>238.50 (-14.15%)</td><td>124.32 (-12.02%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>574.40 (n/a)</td><td>387.60 (n/a)</td><td>299.10 (n/a)</td><td>277.80 (n/a)</td><td>141.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.36 <b>(+50.88%)</b></td><td>0.22 (-3.26%)</td><td>0.22 (-8.23%)</td><td>0.12 <b>(-32.72%)</b></td><td>0.09 <b>(+291.91%)</b></td><td>525.20 <b>(+48.61%)</b></td><td>339.98 (+16.43%)</td><td>302.90 (+8.96%)</td><td>180.40 <b>(-33.73%)</b></td><td>131.41 <b>(+280.31%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>353.40 (n/a)</td><td>292.00 (n/a)</td><td>278.00 (n/a)</td><td>272.20 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.26 (+9.77%)</td><td>0.21 <b>(+51.76%)</b></td><td>0.22 <b>(+68.97%)</b></td><td>0.13 <b>(+65.55%)</b></td><td>0.05 (-16.54%)</td><td>511.80 <b>(-39.60%)</b></td><td>327.60 <b>(-39.12%)</b></td><td>300.50 <b>(-40.81%)</b></td><td>247.60 (-8.90%)</td><td>106.04 <b>(-51.02%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>847.30 (n/a)</td><td>538.12 (n/a)</td><td>507.70 (n/a)</td><td>271.80 (n/a)</td><td>216.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.27 (-12.39%)</td><td>0.18 (-1.36%)</td><td>0.18 <b>(+20.94%)</b></td><td>0.12 (+9.21%)</td><td>0.06 <b>(-30.31%)</b></td><td>568.90 (-8.43%)</td><td>391.00 (-5.19%)</td><td>361.30 (-17.30%)</td><td>245.20 (+14.10%)</td><td>120.81 <b>(-25.66%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>621.30 (n/a)</td><td>412.40 (n/a)</td><td>436.90 (n/a)</td><td>214.90 (n/a)</td><td>162.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.58 (+3.71%)</td><td>0.34 (-7.30%)</td><td>0.30 (-8.66%)</td><td>0.22 (-2.36%)</td><td>0.15 (+7.24%)</td><td>598.10 (+2.41%)</td><td>440.04 (+9.79%)</td><td>432.40 (+9.47%)</td><td>224.90 (-3.56%)</td><td>160.16 (+10.11%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.56 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>584.00 (n/a)</td><td>400.80 (n/a)</td><td>395.00 (n/a)</td><td>233.20 (n/a)</td><td>145.46 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.47 (-9.11%)</td><td>0.35 (-11.84%)</td><td>0.46 (+0.07%)</td><td>0.12 <b>(-52.90%)</b></td><td>0.16 <b>(+38.64%)</b></td><td>1064.30 <b>(+112.31%)</b></td><td>485.42 <b>(+38.19%)</b></td><td>285.30 (-0.07%)</td><td>276.80 (+10.02%)</td><td>339.22 <b>(+204.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>501.30 (n/a)</td><td>351.26 (n/a)</td><td>285.50 (n/a)</td><td>251.60 (n/a)</td><td>111.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.56 (+14.29%)</td><td>0.31 (+1.25%)</td><td>0.26 (-4.31%)</td><td>0.20 (-13.25%)</td><td>0.14 <b>(+35.72%)</b></td><td>643.70 (+15.28%)</td><td>484.26 (+3.86%)</td><td>510.50 (+4.50%)</td><td>235.30 (-12.50%)</td><td>152.60 <b>(+30.93%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.49 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>558.40 (n/a)</td><td>466.26 (n/a)</td><td>488.50 (n/a)</td><td>268.90 (n/a)</td><td>116.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:25:31</td><td>0.07 (-3.74%)</td><td>0.05 (-1.51%)</td><td>0.06 <b>(+34.32%)</b></td><td>0.03 (-6.37%)</td><td>0.02 (-7.91%)</td><td>480.10 (+6.78%)</td><td>348.90 (+1.75%)</td><td>285.60 <b>(-25.55%)</b></td><td>239.90 (+3.90%)</td><td>113.21 (+11.95%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>449.60 (n/a)</td><td>342.90 (n/a)</td><td>383.60 (n/a)</td><td>230.90 (n/a)</td><td>101.12 (n/a)</td>
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
