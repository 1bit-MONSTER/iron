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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 <b>(+21.53%)</b></td><td>0.04 (+13.17%)</td><td>0.04 <b>(+24.79%)</b></td><td>0.03 (-18.00%)</td><td>0.01 <b>(+203.78%)</b></td><td>235.90 <b>(+21.91%)</b></td><td>166.14 (-6.55%)</td><td>145.40 (-19.89%)</td><td>124.50 (-17.71%)</td><td>48.70 <b>(+205.37%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.50 (n/a)</td><td>177.78 (n/a)</td><td>181.50 (n/a)</td><td>151.30 (n/a)</td><td>15.95 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (+11.54%)</td><td>0.04 <b>(+25.14%)</b></td><td>0.05 <b>(+40.60%)</b></td><td>0.03 (+12.36%)</td><td>0.01 (+18.44%)</td><td>188.80 (-10.99%)</td><td>144.08 (-19.84%)</td><td>135.20 <b>(-28.88%)</b></td><td>121.80 (-10.38%)</td><td>27.63 (-3.47%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>179.74 (n/a)</td><td>190.10 (n/a)</td><td>135.90 (n/a)</td><td>28.62 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (+10.81%)</td><td>0.04 <b>(+24.77%)</b></td><td>0.04 <b>(+37.35%)</b></td><td>0.03 <b>(+40.54%)</b></td><td>0.01 (-11.78%)</td><td>189.00 <b>(-28.84%)</b></td><td>162.32 <b>(-21.09%)</b></td><td>151.60 <b>(-27.19%)</b></td><td>134.60 (-9.79%)</td><td>24.66 <b>(-40.54%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>265.60 (n/a)</td><td>205.70 (n/a)</td><td>208.20 (n/a)</td><td>149.20 (n/a)</td><td>41.47 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (-0.85%)</td><td>0.04 (+6.80%)</td><td>0.04 (+1.99%)</td><td>0.03 (+16.13%)</td><td>0.01 (-15.83%)</td><td>197.40 (-13.91%)</td><td>170.30 (-7.71%)</td><td>174.80 (-1.91%)</td><td>128.70 (+0.86%)</td><td>29.30 <b>(-24.62%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>184.52 (n/a)</td><td>178.20 (n/a)</td><td>127.60 (n/a)</td><td>38.87 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (-5.54%)</td><td>0.04 (+18.08%)</td><td>0.04 <b>(+20.15%)</b></td><td>0.03 <b>(+40.39%)</b></td><td>0.00 <b>(-47.09%)</b></td><td>205.10 <b>(-28.76%)</b></td><td>166.34 (-19.42%)</td><td>155.30 (-16.73%)</td><td>145.70 (+5.81%)</td><td>23.42 <b>(-59.85%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>287.90 (n/a)</td><td>206.42 (n/a)</td><td>186.50 (n/a)</td><td>137.70 (n/a)</td><td>58.33 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 <b>(+21.33%)</b></td><td>0.03 (-1.88%)</td><td>0.03 <b>(-21.19%)</b></td><td>0.03 (-9.23%)</td><td>0.01 <b>(+166.81%)</b></td><td>239.20 (+10.18%)</td><td>195.36 (+7.65%)</td><td>221.20 <b>(+26.91%)</b></td><td>135.90 (-17.59%)</td><td>52.32 <b>(+142.40%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>217.10 (n/a)</td><td>181.48 (n/a)</td><td>174.30 (n/a)</td><td>164.90 (n/a)</td><td>21.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (+15.34%)</td><td>0.03 (+8.17%)</td><td>0.03 (+15.68%)</td><td>0.02 (-12.39%)</td><td>0.00 <b>(+304.32%)</b></td><td>253.40 (+14.14%)</td><td>196.82 (-5.82%)</td><td>180.30 (-13.53%)</td><td>173.30 (-13.26%)</td><td>33.20 <b>(+301.71%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>222.00 (n/a)</td><td>208.98 (n/a)</td><td>208.50 (n/a)</td><td>199.80 (n/a)</td><td>8.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 <b>(+31.08%)</b></td><td>0.03 <b>(+21.04%)</b></td><td>0.03 (+13.33%)</td><td>0.03 (+9.92%)</td><td>0.00 <b>(+203.65%)</b></td><td>217.70 (-9.03%)</td><td>189.56 (-16.26%)</td><td>202.40 (-11.73%)</td><td>160.60 <b>(-23.74%)</b></td><td>26.24 <b>(+105.63%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.30 (n/a)</td><td>226.38 (n/a)</td><td>229.30 (n/a)</td><td>210.60 (n/a)</td><td>12.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (+4.81%)</td><td>0.07 (+7.60%)</td><td>0.07 (+11.74%)</td><td>0.06 (+13.75%)</td><td>0.01 (+3.21%)</td><td>212.70 (-12.07%)</td><td>179.62 (-7.22%)</td><td>170.00 (-10.48%)</td><td>149.30 (-4.54%)</td><td>27.50 (-12.76%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>241.90 (n/a)</td><td>193.60 (n/a)</td><td>189.90 (n/a)</td><td>156.40 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 <b>(+29.91%)</b></td><td>0.07 (+3.41%)</td><td>0.06 (-4.49%)</td><td>0.04 <b>(-21.95%)</b></td><td>0.02 <b>(+169.76%)</b></td><td>284.30 <b>(+28.12%)</b></td><td>195.90 (+3.32%)</td><td>196.30 (+4.69%)</td><td>124.40 <b>(-23.02%)</b></td><td>60.75 <b>(+163.47%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>189.60 (n/a)</td><td>187.50 (n/a)</td><td>161.60 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 <b>(+33.59%)</b></td><td>0.08 (+18.69%)</td><td>0.08 (+17.09%)</td><td>0.06 (-0.18%)</td><td>0.02 <b>(+140.02%)</b></td><td>208.60 (+0.19%)</td><td>153.62 (-12.81%)</td><td>149.70 (-14.60%)</td><td>113.00 <b>(-25.12%)</b></td><td>37.25 <b>(+78.52%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>176.18 (n/a)</td><td>175.30 (n/a)</td><td>150.90 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (-7.30%)</td><td>0.07 (-10.74%)</td><td>0.07 (-5.33%)</td><td>0.04 <b>(-34.04%)</b></td><td>0.02 <b>(+63.32%)</b></td><td>291.10 <b>(+51.61%)</b></td><td>195.62 (+17.62%)</td><td>176.20 (+5.64%)</td><td>145.40 (+7.86%)</td><td>59.55 <b>(+167.32%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>166.32 (n/a)</td><td>166.80 (n/a)</td><td>134.80 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (-9.33%)</td><td>0.07 (+1.98%)</td><td>0.07 (+5.35%)</td><td>0.06 (+3.20%)</td><td>0.01 <b>(-35.44%)</b></td><td>213.00 (-3.09%)</td><td>181.02 (-3.24%)</td><td>177.50 (-5.08%)</td><td>153.10 (+10.30%)</td><td>21.75 <b>(-29.02%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>187.08 (n/a)</td><td>187.00 (n/a)</td><td>138.80 (n/a)</td><td>30.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 <b>(+29.36%)</b></td><td>0.07 (+16.17%)</td><td>0.08 <b>(+36.64%)</b></td><td>0.04 (-11.31%)</td><td>0.02 <b>(+183.97%)</b></td><td>273.20 (+12.75%)</td><td>191.32 (-7.57%)</td><td>153.10 <b>(-26.82%)</b></td><td>136.20 <b>(-22.70%)</b></td><td>64.07 <b>(+151.03%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>207.00 (n/a)</td><td>209.20 (n/a)</td><td>176.20 (n/a)</td><td>25.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (+8.02%)</td><td>0.06 (-3.05%)</td><td>0.06 (-8.97%)</td><td>0.05 (-11.60%)</td><td>0.01 <b>(+108.17%)</b></td><td>246.80 (+13.11%)</td><td>210.66 (+5.20%)</td><td>221.00 (+9.84%)</td><td>161.70 (-7.44%)</td><td>36.01 <b>(+121.72%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>200.24 (n/a)</td><td>201.20 (n/a)</td><td>174.70 (n/a)</td><td>16.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (-11.13%)</td><td>0.06 (-6.63%)</td><td>0.05 (-15.90%)</td><td>0.05 <b>(+39.54%)</b></td><td>0.01 <b>(-44.61%)</b></td><td>259.30 <b>(-28.33%)</b></td><td>218.14 (-0.19%)</td><td>225.80 (+18.90%)</td><td>165.10 (+12.54%)</td><td>34.68 <b>(-58.81%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>361.80 (n/a)</td><td>218.56 (n/a)</td><td>189.90 (n/a)</td><td>146.70 (n/a)</td><td>84.19 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (+9.87%)</td><td>0.14 (-1.50%)</td><td>0.13 (-8.90%)</td><td>0.11 (-14.22%)</td><td>0.03 <b>(+109.94%)</b></td><td>215.30 (+16.63%)</td><td>177.10 (+3.96%)</td><td>189.50 (+9.73%)</td><td>132.60 (-8.99%)</td><td>32.99 <b>(+124.78%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>184.60 (n/a)</td><td>170.36 (n/a)</td><td>172.70 (n/a)</td><td>145.70 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (+16.36%)</td><td>0.16 (+10.31%)</td><td>0.14 (+2.62%)</td><td>0.12 (+11.19%)</td><td>0.03 (+9.22%)</td><td>196.90 (-10.09%)</td><td>160.54 (-9.66%)</td><td>170.70 (-2.57%)</td><td>118.80 (-14.04%)</td><td>32.08 (-16.48%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>219.00 (n/a)</td><td>177.70 (n/a)</td><td>175.20 (n/a)</td><td>138.20 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (-4.14%)</td><td>0.15 (+4.86%)</td><td>0.16 (+12.83%)</td><td>0.13 (+10.92%)</td><td>0.02 <b>(-28.39%)</b></td><td>196.00 (-9.84%)</td><td>168.18 (-6.13%)</td><td>154.20 (-11.33%)</td><td>148.00 (+4.30%)</td><td>23.41 <b>(-33.17%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.40 (n/a)</td><td>179.16 (n/a)</td><td>173.90 (n/a)</td><td>141.90 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (+6.74%)</td><td>0.15 (+10.06%)</td><td>0.14 (+15.60%)</td><td>0.13 (+9.49%)</td><td>0.02 (-0.04%)</td><td>192.40 (-8.64%)</td><td>169.54 (-9.36%)</td><td>169.90 (-13.49%)</td><td>134.70 (-6.33%)</td><td>22.63 (-12.90%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.60 (n/a)</td><td>187.04 (n/a)</td><td>196.40 (n/a)</td><td>143.80 (n/a)</td><td>25.98 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (-5.97%)</td><td>0.14 (+1.96%)</td><td>0.14 (+2.44%)</td><td>0.11 (+6.52%)</td><td>0.02 (-12.02%)</td><td>217.30 (-6.13%)</td><td>184.16 (-2.43%)</td><td>181.60 (-2.37%)</td><td>154.20 (+6.34%)</td><td>28.36 (-11.75%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>188.74 (n/a)</td><td>186.00 (n/a)</td><td>145.00 (n/a)</td><td>32.14 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 <b>(+28.21%)</b></td><td>0.17 (+18.18%)</td><td>0.17 <b>(+22.52%)</b></td><td>0.13 (+9.83%)</td><td>0.03 <b>(+60.54%)</b></td><td>191.50 (-8.94%)</td><td>151.00 (-14.06%)</td><td>145.90 (-18.35%)</td><td>113.00 <b>(-22.02%)</b></td><td>30.81 (+15.78%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>175.70 (n/a)</td><td>178.70 (n/a)</td><td>144.90 (n/a)</td><td>26.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 <b>(-32.77%)</b></td><td>0.11 (-17.99%)</td><td>0.12 (-8.32%)</td><td>0.10 (-13.04%)</td><td>0.01 <b>(-61.35%)</b></td><td>254.20 (+14.97%)</td><td>217.14 (+19.28%)</td><td>208.80 (+9.09%)</td><td>195.50 <b>(+48.67%)</b></td><td>22.79 <b>(-30.75%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>221.10 (n/a)</td><td>182.04 (n/a)</td><td>191.40 (n/a)</td><td>131.50 (n/a)</td><td>32.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (+18.03%)</td><td>0.13 (+18.57%)</td><td>0.13 (+12.28%)</td><td>0.10 <b>(+34.30%)</b></td><td>0.02 (-4.54%)</td><td>238.90 <b>(-25.53%)</b></td><td>194.42 (-16.77%)</td><td>193.80 (-10.94%)</td><td>166.00 (-15.31%)</td><td>28.66 <b>(-42.35%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>320.80 (n/a)</td><td>233.60 (n/a)</td><td>217.60 (n/a)</td><td>196.00 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.44 (+16.29%)</td><td>0.35 (+19.94%)</td><td>0.32 <b>(+26.96%)</b></td><td>0.26 (+13.90%)</td><td>0.08 (+14.24%)</td><td>188.80 (-12.23%)</td><td>147.06 (-16.75%)</td><td>154.70 <b>(-21.23%)</b></td><td>110.50 (-14.01%)</td><td>32.17 (-15.40%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>215.10 (n/a)</td><td>176.64 (n/a)</td><td>196.40 (n/a)</td><td>128.50 (n/a)</td><td>38.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.34 (+2.16%)</td><td>0.27 (-0.44%)</td><td>0.26 (-4.24%)</td><td>0.16 <b>(-25.05%)</b></td><td>0.07 <b>(+39.21%)</b></td><td>306.10 <b>(+33.44%)</b></td><td>197.52 (+4.55%)</td><td>189.20 (+4.47%)</td><td>144.00 (-2.17%)</td><td>63.81 <b>(+85.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>229.40 (n/a)</td><td>188.92 (n/a)</td><td>181.10 (n/a)</td><td>147.20 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (-11.77%)</td><td>0.24 (-14.20%)</td><td>0.22 (-17.95%)</td><td>0.20 (-17.95%)</td><td>0.04 (+16.79%)</td><td>247.90 <b>(+21.88%)</b></td><td>210.16 (+17.91%)</td><td>223.70 <b>(+21.84%)</b></td><td>166.70 (+13.32%)</td><td>36.27 <b>(+60.46%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>203.40 (n/a)</td><td>178.24 (n/a)</td><td>183.60 (n/a)</td><td>147.10 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.32 (+5.45%)</td><td>0.25 (-5.22%)</td><td>0.27 (+5.42%)</td><td>0.17 <b>(-28.48%)</b></td><td>0.06 <b>(+79.70%)</b></td><td>290.30 <b>(+39.84%)</b></td><td>203.28 (+9.47%)</td><td>180.00 (-5.16%)</td><td>154.50 (-5.16%)</td><td>53.55 <b>(+147.12%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>207.60 (n/a)</td><td>185.70 (n/a)</td><td>189.80 (n/a)</td><td>162.90 (n/a)</td><td>21.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.42 <b>(+28.33%)</b></td><td>0.29 (+9.14%)</td><td>0.27 (-1.35%)</td><td>0.23 (+1.41%)</td><td>0.08 <b>(+87.73%)</b></td><td>214.70 (-1.42%)</td><td>177.46 (-5.55%)</td><td>184.10 (+1.38%)</td><td>116.20 <b>(-22.07%)</b></td><td>40.08 <b>(+40.95%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>217.80 (n/a)</td><td>187.88 (n/a)</td><td>181.60 (n/a)</td><td>149.10 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 (+3.42%)</td><td>0.25 (-8.16%)</td><td>0.28 (+5.55%)</td><td>0.13 <b>(-49.18%)</b></td><td>0.07 <b>(+339.76%)</b></td><td>373.20 <b>(+96.73%)</b></td><td>215.86 (+19.71%)</td><td>173.20 (-5.25%)</td><td>157.80 (-3.25%)</td><td>89.53 <b>(+786.07%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>189.70 (n/a)</td><td>180.32 (n/a)</td><td>182.80 (n/a)</td><td>163.10 (n/a)</td><td>10.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.36 (+1.37%)</td><td>0.28 (+7.42%)</td><td>0.26 (+6.83%)</td><td>0.23 (+6.46%)</td><td>0.06 (+0.72%)</td><td>215.50 (-6.06%)</td><td>182.52 (-6.94%)</td><td>191.00 (-6.42%)</td><td>136.50 (-1.37%)</td><td>33.98 (-1.61%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>229.40 (n/a)</td><td>196.14 (n/a)</td><td>204.10 (n/a)</td><td>138.40 (n/a)</td><td>34.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 (-9.59%)</td><td>0.26 (+1.38%)</td><td>0.28 <b>(+24.67%)</b></td><td>0.20 (-10.29%)</td><td>0.04 <b>(-26.76%)</b></td><td>248.40 (+11.49%)</td><td>189.88 (-2.50%)</td><td>177.20 (-19.78%)</td><td>158.40 (+10.54%)</td><td>34.49 (-9.31%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>222.80 (n/a)</td><td>194.74 (n/a)</td><td>220.90 (n/a)</td><td>143.30 (n/a)</td><td>38.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (-13.12%)</td><td>0.02 (+17.31%)</td><td>0.02 <b>(+66.33%)</b></td><td>0.01 (+6.60%)</td><td>0.00 <b>(-30.24%)</b></td><td>207.00 (-6.17%)</td><td>142.14 (-18.07%)</td><td>121.10 <b>(-39.90%)</b></td><td>117.90 (+15.02%)</td><td>37.89 <b>(-25.31%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>173.48 (n/a)</td><td>201.50 (n/a)</td><td>102.50 (n/a)</td><td>50.74 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (+14.29%)</td><td>0.02 <b>(+21.04%)</b></td><td>0.02 (+8.84%)</td><td>0.02 <b>(+41.14%)</b></td><td>0.00 <b>(-29.24%)</b></td><td>160.80 <b>(-29.16%)</b></td><td>142.96 (-19.35%)</td><td>147.70 (-8.09%)</td><td>124.50 (-12.51%)</td><td>16.40 <b>(-56.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>227.00 (n/a)</td><td>177.26 (n/a)</td><td>160.70 (n/a)</td><td>142.30 (n/a)</td><td>37.97 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 <b>(+20.42%)</b></td><td>0.01 (-2.53%)</td><td>0.02 (-1.21%)</td><td>0.01 <b>(-32.06%)</b></td><td>0.00 <b>(+149.85%)</b></td><td>298.60 <b>(+47.17%)</b></td><td>193.18 (+9.52%)</td><td>170.10 (+1.25%)</td><td>132.20 (-16.96%)</td><td>64.36 <b>(+219.13%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>176.38 (n/a)</td><td>168.00 (n/a)</td><td>159.20 (n/a)</td><td>20.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (+5.32%)</td><td>0.02 (+5.90%)</td><td>0.02 (+7.57%)</td><td>0.01 (-4.46%)</td><td>0.00 (+17.31%)</td><td>221.60 (+4.68%)</td><td>157.32 (-4.52%)</td><td>139.80 (-6.99%)</td><td>127.80 (-5.05%)</td><td>39.26 (+16.73%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>164.76 (n/a)</td><td>150.30 (n/a)</td><td>134.60 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (+5.53%)</td><td>0.02 (+4.79%)</td><td>0.02 (-2.61%)</td><td>0.01 (+1.55%)</td><td>0.00 (+15.88%)</td><td>200.00 (-1.53%)</td><td>156.48 (-3.75%)</td><td>148.10 (+2.70%)</td><td>116.70 (-5.20%)</td><td>38.48 (+4.74%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>162.58 (n/a)</td><td>144.20 (n/a)</td><td>123.10 (n/a)</td><td>36.74 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (-2.57%)</td><td>0.02 (-0.27%)</td><td>0.02 (+7.01%)</td><td>0.01 (-10.63%)</td><td>0.00 (-0.21%)</td><td>214.30 (+11.91%)</td><td>169.48 (+0.52%)</td><td>164.60 (-6.58%)</td><td>144.70 (+2.62%)</td><td>27.07 (+17.13%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>191.50 (n/a)</td><td>168.60 (n/a)</td><td>176.20 (n/a)</td><td>141.00 (n/a)</td><td>23.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (+11.12%)</td><td>0.02 (+13.15%)</td><td>0.02 (+8.08%)</td><td>0.01 (+5.20%)</td><td>0.00 (+9.99%)</td><td>205.30 (-4.91%)</td><td>161.18 (-11.56%)</td><td>159.60 (-7.48%)</td><td>128.40 (-10.02%)</td><td>28.12 (-6.08%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.90 (n/a)</td><td>182.24 (n/a)</td><td>172.50 (n/a)</td><td>142.70 (n/a)</td><td>29.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.01 (-8.51%)</td><td>0.01 (+2.33%)</td><td>0.01 (+3.63%)</td><td>0.01 (+12.95%)</td><td>0.00 <b>(-41.14%)</b></td><td>237.70 (-11.47%)</td><td>208.60 (-3.75%)</td><td>208.60 (-3.47%)</td><td>181.60 (+9.27%)</td><td>20.93 <b>(-42.25%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>268.50 (n/a)</td><td>216.72 (n/a)</td><td>216.10 (n/a)</td><td>166.20 (n/a)</td><td>36.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (+3.88%)</td><td>0.04 (+5.18%)</td><td>0.04 (+14.38%)</td><td>0.02 <b>(-21.37%)</b></td><td>0.01 <b>(+68.96%)</b></td><td>225.70 <b>(+27.23%)</b></td><td>155.12 (-1.96%)</td><td>143.70 (-12.54%)</td><td>126.50 (-3.73%)</td><td>40.25 <b>(+116.65%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>177.40 (n/a)</td><td>158.22 (n/a)</td><td>164.30 (n/a)</td><td>131.40 (n/a)</td><td>18.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (-14.15%)</td><td>0.03 (-1.05%)</td><td>0.04 (+7.95%)</td><td>0.02 <b>(-21.05%)</b></td><td>0.01 (-3.30%)</td><td>234.50 <b>(+26.69%)</b></td><td>161.64 (+2.34%)</td><td>149.40 (-7.38%)</td><td>134.60 (+16.54%)</td><td>41.28 <b>(+49.13%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.10 (n/a)</td><td>157.94 (n/a)</td><td>161.30 (n/a)</td><td>115.50 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (-5.38%)</td><td>0.03 (-10.75%)</td><td>0.03 <b>(-28.41%)</b></td><td>0.02 (-5.20%)</td><td>0.01 (+15.84%)</td><td>226.80 (+5.49%)</td><td>178.32 (+14.18%)</td><td>190.70 <b>(+39.71%)</b></td><td>127.70 (+5.62%)</td><td>48.02 <b>(+23.78%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>156.18 (n/a)</td><td>136.50 (n/a)</td><td>120.90 (n/a)</td><td>38.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (-3.03%)</td><td>0.03 (-2.00%)</td><td>0.03 (-2.77%)</td><td>0.03 (+0.32%)</td><td>0.01 (-9.38%)</td><td>181.60 (-0.33%)</td><td>161.44 (+1.69%)</td><td>175.40 (+2.81%)</td><td>127.70 (+3.15%)</td><td>23.81 (-6.54%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.20 (n/a)</td><td>158.76 (n/a)</td><td>170.60 (n/a)</td><td>123.80 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (-1.54%)</td><td>0.03 (+7.18%)</td><td>0.03 (+0.07%)</td><td>0.03 <b>(+28.05%)</b></td><td>0.01 <b>(-28.85%)</b></td><td>178.40 <b>(-21.89%)</b></td><td>156.42 (-9.56%)</td><td>159.30 (-0.13%)</td><td>118.90 (+1.54%)</td><td>24.31 <b>(-43.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>172.96 (n/a)</td><td>159.50 (n/a)</td><td>117.10 (n/a)</td><td>43.20 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (-9.41%)</td><td>0.03 (+3.03%)</td><td>0.03 (+2.68%)</td><td>0.02 (+15.51%)</td><td>0.01 <b>(-27.26%)</b></td><td>223.00 (-13.43%)</td><td>173.72 (-7.03%)</td><td>178.30 (-2.62%)</td><td>116.70 (+10.30%)</td><td>40.21 <b>(-29.95%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.60 (n/a)</td><td>186.86 (n/a)</td><td>183.10 (n/a)</td><td>105.80 (n/a)</td><td>57.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 <b>(+28.46%)</b></td><td>0.03 (+0.02%)</td><td>0.03 (-6.96%)</td><td>0.02 <b>(-27.25%)</b></td><td>0.01 <b>(+196.62%)</b></td><td>289.90 <b>(+37.46%)</b></td><td>195.12 (+7.56%)</td><td>187.10 (+7.47%)</td><td>125.10 <b>(-22.15%)</b></td><td>63.63 <b>(+216.20%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.90 (n/a)</td><td>181.40 (n/a)</td><td>174.10 (n/a)</td><td>160.70 (n/a)</td><td>20.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-15.19%)</td><td>0.02 (-16.58%)</td><td>0.02 (-19.05%)</td><td>0.02 <b>(-28.09%)</b></td><td>0.00 (+2.52%)</td><td>331.50 <b>(+39.05%)</b></td><td>249.98 <b>(+21.17%)</b></td><td>244.80 <b>(+23.51%)</b></td><td>207.30 (+17.92%)</td><td>48.51 <b>(+69.07%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.40 (n/a)</td><td>206.30 (n/a)</td><td>198.20 (n/a)</td><td>175.80 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (-12.12%)</td><td>0.06 (-7.93%)</td><td>0.07 (-0.46%)</td><td>0.05 (-5.77%)</td><td>0.01 (-19.04%)</td><td>205.70 (+6.14%)</td><td>175.02 (+8.16%)</td><td>160.90 (+0.44%)</td><td>148.70 (+13.86%)</td><td>26.90 (-0.47%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>161.82 (n/a)</td><td>160.20 (n/a)</td><td>130.60 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (-6.89%)</td><td>0.05 (-19.47%)</td><td>0.06 (-1.13%)</td><td>0.03 <b>(-36.31%)</b></td><td>0.02 <b>(+54.05%)</b></td><td>327.70 <b>(+57.02%)</b></td><td>234.72 <b>(+33.71%)</b></td><td>189.80 (+1.17%)</td><td>148.20 (+7.39%)</td><td>82.38 <b>(+182.00%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>175.54 (n/a)</td><td>187.60 (n/a)</td><td>138.00 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (-4.18%)</td><td>0.07 (+9.48%)</td><td>0.07 (+13.19%)</td><td>0.06 <b>(+22.21%)</b></td><td>0.01 <b>(-38.66%)</b></td><td>173.50 (-18.16%)</td><td>153.70 (-11.09%)</td><td>154.10 (-11.64%)</td><td>123.50 (+4.40%)</td><td>18.82 <b>(-47.58%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>212.00 (n/a)</td><td>172.88 (n/a)</td><td>174.40 (n/a)</td><td>118.30 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (+15.13%)</td><td>0.06 (+2.36%)</td><td>0.07 (+10.87%)</td><td>0.04 <b>(-28.71%)</b></td><td>0.01 <b>(+488.84%)</b></td><td>242.90 <b>(+40.32%)</b></td><td>168.56 (+1.66%)</td><td>151.40 (-9.77%)</td><td>137.90 (-13.11%)</td><td>42.62 <b>(+649.59%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>173.10 (n/a)</td><td>165.80 (n/a)</td><td>167.80 (n/a)</td><td>158.70 (n/a)</td><td>5.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (+7.53%)</td><td>0.06 (+3.87%)</td><td>0.06 (+2.22%)</td><td>0.05 (-5.84%)</td><td>0.01 <b>(+37.93%)</b></td><td>217.60 (+6.20%)</td><td>170.92 (-2.74%)</td><td>167.10 (-2.17%)</td><td>143.50 (-7.00%)</td><td>29.35 <b>(+37.05%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>175.74 (n/a)</td><td>170.80 (n/a)</td><td>154.30 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 <b>(-28.40%)</b></td><td>0.06 <b>(-20.01%)</b></td><td>0.06 (-19.25%)</td><td>0.05 (-11.20%)</td><td>0.01 <b>(-50.02%)</b></td><td>222.60 (+12.65%)</td><td>186.38 <b>(+22.39%)</b></td><td>180.90 <b>(+23.82%)</b></td><td>156.40 <b>(+39.64%)</b></td><td>25.22 <b>(-20.86%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>197.60 (n/a)</td><td>152.28 (n/a)</td><td>146.10 (n/a)</td><td>112.00 (n/a)</td><td>31.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (-3.31%)</td><td>0.06 (-8.24%)</td><td>0.06 (+0.70%)</td><td>0.05 (-18.41%)</td><td>0.01 <b>(+108.00%)</b></td><td>226.60 <b>(+22.55%)</b></td><td>186.32 (+11.00%)</td><td>167.10 (-0.71%)</td><td>157.70 (+3.48%)</td><td>31.94 <b>(+165.07%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>167.86 (n/a)</td><td>168.30 (n/a)</td><td>152.40 (n/a)</td><td>12.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (-17.69%)</td><td>0.05 (-3.38%)</td><td>0.05 (+7.67%)</td><td>0.04 (-2.25%)</td><td>0.01 <b>(-36.83%)</b></td><td>244.50 (+2.30%)</td><td>209.30 (+1.57%)</td><td>210.90 (-7.13%)</td><td>175.80 <b>(+21.49%)</b></td><td>31.31 <b>(-23.08%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>206.06 (n/a)</td><td>227.10 (n/a)</td><td>144.70 (n/a)</td><td>40.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (-9.94%)</td><td>0.14 (+3.57%)</td><td>0.13 (+5.72%)</td><td>0.13 <b>(+34.10%)</b></td><td>0.01 <b>(-59.88%)</b></td><td>164.40 <b>(-25.41%)</b></td><td>153.58 (-7.59%)</td><td>157.70 (-5.40%)</td><td>130.00 (+11.02%)</td><td>13.51 <b>(-67.24%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>220.40 (n/a)</td><td>166.20 (n/a)</td><td>166.70 (n/a)</td><td>117.10 (n/a)</td><td>41.23 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (-11.81%)</td><td>0.13 (-1.64%)</td><td>0.13 (+5.52%)</td><td>0.11 (-0.86%)</td><td>0.01 <b>(-47.03%)</b></td><td>188.40 (+0.86%)</td><td>166.08 (+0.40%)</td><td>167.00 (-5.22%)</td><td>151.20 (+13.43%)</td><td>14.54 <b>(-40.23%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>186.80 (n/a)</td><td>165.42 (n/a)</td><td>176.20 (n/a)</td><td>133.30 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 <b>(+26.18%)</b></td><td>0.15 (+11.45%)</td><td>0.16 (+17.31%)</td><td>0.10 (-13.00%)</td><td>0.03 <b>(+166.71%)</b></td><td>204.30 (+14.97%)</td><td>148.12 (-6.83%)</td><td>128.20 (-14.70%)</td><td>115.70 <b>(-20.70%)</b></td><td>36.95 <b>(+143.75%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>177.70 (n/a)</td><td>158.98 (n/a)</td><td>150.30 (n/a)</td><td>145.90 (n/a)</td><td>15.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 <b>(-33.34%)</b></td><td>0.13 (-16.04%)</td><td>0.12 (-12.52%)</td><td>0.11 (-5.58%)</td><td>0.01 <b>(-62.50%)</b></td><td>192.90 (+5.93%)</td><td>169.52 (+15.51%)</td><td>169.40 (+14.30%)</td><td>151.40 <b>(+50.05%)</b></td><td>18.35 <b>(-39.76%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>182.10 (n/a)</td><td>146.76 (n/a)</td><td>148.20 (n/a)</td><td>100.90 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (-2.53%)</td><td>0.12 (+7.65%)</td><td>0.14 <b>(+20.08%)</b></td><td>0.07 <b>(+26.34%)</b></td><td>0.03 <b>(-23.24%)</b></td><td>282.10 <b>(-20.85%)</b></td><td>180.16 (-12.70%)</td><td>150.50 (-16.71%)</td><td>134.60 (+2.59%)</td><td>59.98 <b>(-34.81%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>356.40 (n/a)</td><td>206.36 (n/a)</td><td>180.70 (n/a)</td><td>131.20 (n/a)</td><td>92.00 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (-8.35%)</td><td>0.11 (-3.08%)</td><td>0.11 (-4.86%)</td><td>0.11 (+1.35%)</td><td>0.01 <b>(-34.45%)</b></td><td>198.40 (-1.34%)</td><td>184.94 (+2.36%)</td><td>188.60 (+5.13%)</td><td>157.30 (+9.08%)</td><td>16.08 <b>(-30.83%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>201.10 (n/a)</td><td>180.68 (n/a)</td><td>179.40 (n/a)</td><td>144.20 (n/a)</td><td>23.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (+3.88%)</td><td>0.13 (+4.44%)</td><td>0.13 (+8.95%)</td><td>0.11 (+2.26%)</td><td>0.02 (+14.58%)</td><td>188.20 (-2.23%)</td><td>161.68 (-3.90%)</td><td>157.00 (-8.19%)</td><td>132.90 (-3.77%)</td><td>24.16 (+10.14%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>192.50 (n/a)</td><td>168.24 (n/a)</td><td>171.00 (n/a)</td><td>138.10 (n/a)</td><td>21.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (-5.88%)</td><td>0.10 (-11.40%)</td><td>0.10 (-6.44%)</td><td>0.07 <b>(-22.34%)</b></td><td>0.02 (+9.50%)</td><td>297.90 <b>(+28.79%)</b></td><td>220.30 (+14.38%)</td><td>203.40 (+6.88%)</td><td>173.80 (+6.23%)</td><td>47.09 <b>(+58.00%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>231.30 (n/a)</td><td>192.60 (n/a)</td><td>190.30 (n/a)</td><td>163.60 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>175.42 (n/a)</td><td>188.10 (n/a)</td><td>141.40 (n/a)</td><td>29.97 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>175.72 (n/a)</td><td>176.50 (n/a)</td><td>142.90 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>194.20 (n/a)</td><td>193.80 (n/a)</td><td>178.00 (n/a)</td><td>15.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>334.10 (n/a)</td><td>212.82 (n/a)</td><td>203.50 (n/a)</td><td>133.50 (n/a)</td><td>74.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>175.18 (n/a)</td><td>176.20 (n/a)</td><td>160.80 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>173.24 (n/a)</td><td>166.90 (n/a)</td><td>145.90 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>182.58 (n/a)</td><td>189.30 (n/a)</td><td>145.20 (n/a)</td><td>35.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>240.60 (n/a)</td><td>207.82 (n/a)</td><td>210.00 (n/a)</td><td>173.50 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>177.38 (n/a)</td><td>171.10 (n/a)</td><td>164.70 (n/a)</td><td>20.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>212.00 (n/a)</td><td>176.00 (n/a)</td><td>168.30 (n/a)</td><td>161.50 (n/a)</td><td>20.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>183.50 (n/a)</td><td>174.96 (n/a)</td><td>178.20 (n/a)</td><td>166.20 (n/a)</td><td>7.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>255.50 (n/a)</td><td>215.36 (n/a)</td><td>218.50 (n/a)</td><td>183.80 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 <b>(-23.47%)</b></td><td>0.27 (-10.55%)</td><td>0.28 (-4.83%)</td><td>0.25 (+3.22%)</td><td>0.02 <b>(-65.91%)</b></td><td>196.90 (-3.10%)</td><td>183.26 (+9.93%)</td><td>178.10 (+5.07%)</td><td>172.60 <b>(+30.66%)</b></td><td>11.35 <b>(-56.43%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>203.20 (n/a)</td><td>166.70 (n/a)</td><td>169.50 (n/a)</td><td>132.10 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>248.80 (n/a)</td><td>194.60 (n/a)</td><td>187.60 (n/a)</td><td>163.90 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>279.40 (n/a)</td><td>236.34 (n/a)</td><td>241.70 (n/a)</td><td>169.30 (n/a)</td><td>45.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>278.80 (n/a)</td><td>226.38 (n/a)</td><td>220.80 (n/a)</td><td>196.90 (n/a)</td><td>32.20 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>175.32 (n/a)</td><td>179.10 (n/a)</td><td>146.00 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>215.20 (n/a)</td><td>192.38 (n/a)</td><td>188.90 (n/a)</td><td>167.80 (n/a)</td><td>18.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.70 (n/a)</td><td>179.06 (n/a)</td><td>180.70 (n/a)</td><td>145.10 (n/a)</td><td>23.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>227.20 (n/a)</td><td>197.02 (n/a)</td><td>206.00 (n/a)</td><td>165.30 (n/a)</td><td>26.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>175.66 (n/a)</td><td>185.00 (n/a)</td><td>138.40 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>192.46 (n/a)</td><td>198.00 (n/a)</td><td>153.60 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>184.86 (n/a)</td><td>196.40 (n/a)</td><td>150.20 (n/a)</td><td>24.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>314.80 (n/a)</td><td>190.16 (n/a)</td><td>165.50 (n/a)</td><td>144.40 (n/a)</td><td>70.26 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>254.70 (n/a)</td><td>178.30 (n/a)</td><td>162.60 (n/a)</td><td>140.70 (n/a)</td><td>44.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.60 (n/a)</td><td>158.56 (n/a)</td><td>146.80 (n/a)</td><td>136.60 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.80 (n/a)</td><td>170.90 (n/a)</td><td>154.20 (n/a)</td><td>142.80 (n/a)</td><td>32.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>183.56 (n/a)</td><td>186.20 (n/a)</td><td>163.90 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>190.90 (n/a)</td><td>170.34 (n/a)</td><td>183.50 (n/a)</td><td>111.50 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>210.10 (n/a)</td><td>175.14 (n/a)</td><td>177.60 (n/a)</td><td>140.20 (n/a)</td><td>27.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>222.20 (n/a)</td><td>191.92 (n/a)</td><td>189.90 (n/a)</td><td>163.10 (n/a)</td><td>27.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.10 (n/a)</td><td>157.00 (n/a)</td><td>157.00 (n/a)</td><td>126.30 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.20 (n/a)</td><td>149.74 (n/a)</td><td>148.10 (n/a)</td><td>135.20 (n/a)</td><td>14.62 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.70 (n/a)</td><td>167.76 (n/a)</td><td>158.70 (n/a)</td><td>130.80 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.70 (n/a)</td><td>167.18 (n/a)</td><td>164.40 (n/a)</td><td>138.60 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.30 (n/a)</td><td>180.68 (n/a)</td><td>181.20 (n/a)</td><td>139.50 (n/a)</td><td>35.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>185.84 (n/a)</td><td>192.10 (n/a)</td><td>164.60 (n/a)</td><td>12.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>164.74 (n/a)</td><td>164.80 (n/a)</td><td>138.60 (n/a)</td><td>22.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.20 (n/a)</td><td>210.70 (n/a)</td><td>207.60 (n/a)</td><td>185.10 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>164.84 (n/a)</td><td>152.00 (n/a)</td><td>141.00 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>262.40 (n/a)</td><td>169.02 (n/a)</td><td>138.30 (n/a)</td><td>124.10 (n/a)</td><td>57.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>169.38 (n/a)</td><td>149.60 (n/a)</td><td>137.30 (n/a)</td><td>37.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>184.94 (n/a)</td><td>177.10 (n/a)</td><td>123.80 (n/a)</td><td>43.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>188.10 (n/a)</td><td>208.80 (n/a)</td><td>134.90 (n/a)</td><td>35.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>347.90 (n/a)</td><td>209.84 (n/a)</td><td>176.50 (n/a)</td><td>155.30 (n/a)</td><td>79.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>193.30 (n/a)</td><td>190.00 (n/a)</td><td>158.50 (n/a)</td><td>29.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>342.70 (n/a)</td><td>232.58 (n/a)</td><td>213.70 (n/a)</td><td>192.00 (n/a)</td><td>62.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.60 (n/a)</td><td>193.24 (n/a)</td><td>183.00 (n/a)</td><td>137.90 (n/a)</td><td>46.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>173.30 (n/a)</td><td>163.20 (n/a)</td><td>152.00 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.40 (n/a)</td><td>162.12 (n/a)</td><td>147.00 (n/a)</td><td>123.90 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>233.10 (n/a)</td><td>175.58 (n/a)</td><td>174.20 (n/a)</td><td>117.20 (n/a)</td><td>44.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>159.22 (n/a)</td><td>139.20 (n/a)</td><td>129.50 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.80 (n/a)</td><td>166.28 (n/a)</td><td>160.80 (n/a)</td><td>134.60 (n/a)</td><td>31.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>261.00 (n/a)</td><td>183.66 (n/a)</td><td>172.30 (n/a)</td><td>150.00 (n/a)</td><td>44.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>194.70 (n/a)</td><td>194.70 (n/a)</td><td>174.90 (n/a)</td><td>15.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>149.70 (n/a)</td><td>138.76 (n/a)</td><td>142.20 (n/a)</td><td>113.40 (n/a)</td><td>14.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>179.70 (n/a)</td><td>155.02 (n/a)</td><td>149.40 (n/a)</td><td>138.40 (n/a)</td><td>17.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.80 (n/a)</td><td>153.88 (n/a)</td><td>137.50 (n/a)</td><td>128.70 (n/a)</td><td>40.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.70 (n/a)</td><td>166.76 (n/a)</td><td>171.30 (n/a)</td><td>141.80 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>179.40 (n/a)</td><td>164.32 (n/a)</td><td>169.00 (n/a)</td><td>145.90 (n/a)</td><td>14.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>287.60 (n/a)</td><td>179.82 (n/a)</td><td>156.30 (n/a)</td><td>137.40 (n/a)</td><td>60.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>268.40 (n/a)</td><td>209.12 (n/a)</td><td>202.60 (n/a)</td><td>174.30 (n/a)</td><td>38.95 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>4.16 (-4.54%)</td><td>4.03 (-3.69%)</td><td>3.99 (-4.47%)</td><td>3.96 (+0.17%)</td><td>0.08 <b>(-50.05%)</b></td><td>2376.40 (-0.16%)</td><td>2336.38 (+3.73%)</td><td>2356.40 (+4.68%)</td><td>2262.20 (+4.76%)</td><td>47.70 <b>(-47.55%)</b></td><td>1635.33 (-4.54%)</td><td>1583.93 (-3.69%)</td><td>1569.91 (-4.47%)</td><td>1556.74 (+0.17%)</td><td>32.82 <b>(-50.05%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>4.35 (n/a)</td><td>4.18 (n/a)</td><td>4.18 (n/a)</td><td>3.95 (n/a)</td><td>0.17 (n/a)</td><td>2380.30 (n/a)</td><td>2252.32 (n/a)</td><td>2251.00 (n/a)</td><td>2159.50 (n/a)</td><td>90.95 (n/a)</td><td>1713.09 (n/a)</td><td>1644.59 (n/a)</td><td>1643.43 (n/a)</td><td>1554.15 (n/a)</td><td>65.70 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>1.20 (+7.13%)</td><td>0.97 (-4.49%)</td><td>0.95 (-4.93%)</td><td>0.67 <b>(-27.63%)</b></td><td>0.20 <b>(+179.98%)</b></td><td>327.90 <b>(+38.18%)</b></td><td>236.96 (+8.36%)</td><td>232.30 (+5.16%)</td><td>184.90 (-6.66%)</td><td>55.35 <b>(+269.95%)</b></td><td>51.04 (+7.13%)</td><td>41.38 (-4.49%)</td><td>40.62 (-4.93%)</td><td>28.78 <b>(-27.63%)</b></td><td>8.44 <b>(+179.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.12 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.93 (n/a)</td><td>0.07 (n/a)</td><td>237.30 (n/a)</td><td>218.68 (n/a)</td><td>220.90 (n/a)</td><td>198.10 (n/a)</td><td>14.96 (n/a)</td><td>47.64 (n/a)</td><td>43.32 (n/a)</td><td>42.73 (n/a)</td><td>39.77 (n/a)</td><td>3.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>1.05 (-5.62%)</td><td>0.87 (-3.34%)</td><td>0.99 (+5.16%)</td><td>0.60 (-6.66%)</td><td>0.21 (+17.64%)</td><td>370.10 (+7.12%)</td><td>269.36 (+5.38%)</td><td>223.10 (-4.90%)</td><td>210.70 (+5.99%)</td><td>73.20 <b>(+28.83%)</b></td><td>44.79 (-5.62%)</td><td>36.98 (-3.34%)</td><td>42.30 (+5.16%)</td><td>25.50 (-6.66%)</td><td>8.99 (+17.64%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.11 (n/a)</td><td>0.90 (n/a)</td><td>0.94 (n/a)</td><td>0.64 (n/a)</td><td>0.18 (n/a)</td><td>345.50 (n/a)</td><td>255.60 (n/a)</td><td>234.60 (n/a)</td><td>198.80 (n/a)</td><td>56.82 (n/a)</td><td>47.46 (n/a)</td><td>38.26 (n/a)</td><td>40.23 (n/a)</td><td>27.32 (n/a)</td><td>7.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.52 (-0.34%)</td><td>0.52 (+0.05%)</td><td>0.52 (+0.02%)</td><td>0.52 (+0.35%)</td><td>0.00 <b>(-82.78%)</b></td><td>48670.00 (-0.35%)</td><td>48631.36 (-0.05%)</td><td>48618.80 (-0.02%)</td><td>48603.40 (+0.34%)</td><td>26.61 <b>(-82.77%)</b></td><td>353.47 (-0.34%)</td><td>353.27 (+0.05%)</td><td>353.36 (+0.02%)</td><td>352.99 (+0.35%)</td><td>0.19 <b>(-82.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48839.80 (n/a)</td><td>48656.88 (n/a)</td><td>48628.60 (n/a)</td><td>48440.10 (n/a)</td><td>154.43 (n/a)</td><td>354.66 (n/a)</td><td>353.08 (n/a)</td><td>353.29 (n/a)</td><td>351.76 (n/a)</td><td>1.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (-1.21%)</td><td>0.21 (-1.80%)</td><td>0.21 (-1.53%)</td><td>0.21 (-1.40%)</td><td>0.00 (+13.19%)</td><td>120168.80 (+1.42%)</td><td>118483.24 (+1.84%)</td><td>118166.90 (+1.55%)</td><td>116292.30 (+1.22%)</td><td>1669.64 (+16.56%)</td><td>147.73 (-1.21%)</td><td>145.02 (-1.80%)</td><td>145.39 (-1.53%)</td><td>142.96 (-1.40%)</td><td>2.05 (+13.19%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118489.30 (n/a)</td><td>116347.74 (n/a)</td><td>116360.20 (n/a)</td><td>114889.80 (n/a)</td><td>1432.39 (n/a)</td><td>149.53 (n/a)</td><td>147.68 (n/a)</td><td>147.64 (n/a)</td><td>144.99 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.88 (-0.46%)</td><td>0.88 (+0.17%)</td><td>0.88 (+0.72%)</td><td>0.87 (+0.00%)</td><td>0.00 <b>(-29.36%)</b></td><td>28892.50 (-0.00%)</td><td>28708.92 (-0.17%)</td><td>28660.40 (-0.72%)</td><td>28511.20 (+0.46%)</td><td>154.82 <b>(-28.95%)</b></td><td>602.57 (-0.46%)</td><td>598.43 (+0.17%)</td><td>599.43 (+0.72%)</td><td>594.61 (+0.00%)</td><td>3.23 <b>(-29.36%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28893.70 (n/a)</td><td>28758.68 (n/a)</td><td>28867.60 (n/a)</td><td>28379.80 (n/a)</td><td>217.91 (n/a)</td><td>605.36 (n/a)</td><td>597.41 (n/a)</td><td>595.13 (n/a)</td><td>594.59 (n/a)</td><td>4.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.51 (+0.22%)</td><td>3.38 (-0.12%)</td><td>3.36 (+0.19%)</td><td>3.25 (+0.22%)</td><td>0.12 (+9.57%)</td><td>7747.20 (-0.22%)</td><td>7449.48 (+0.14%)</td><td>7487.50 (-0.19%)</td><td>7165.20 (-0.22%)</td><td>268.84 (+9.24%)</td><td>2397.69 (+0.22%)</td><td>2308.59 (-0.12%)</td><td>2294.46 (+0.19%)</td><td>2217.55 (+0.22%)</td><td>83.57 (+9.57%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>3.50 (n/a)</td><td>3.39 (n/a)</td><td>3.35 (n/a)</td><td>3.24 (n/a)</td><td>0.11 (n/a)</td><td>7764.50 (n/a)</td><td>7439.24 (n/a)</td><td>7501.60 (n/a)</td><td>7180.70 (n/a)</td><td>246.09 (n/a)</td><td>2392.50 (n/a)</td><td>2311.38 (n/a)</td><td>2290.17 (n/a)</td><td>2212.61 (n/a)</td><td>76.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>2.86 (+0.79%)</td><td>2.80 (+0.36%)</td><td>2.81 (+0.06%)</td><td>2.75 (+0.48%)</td><td>0.04 (-0.02%)</td><td>9161.80 (-0.48%)</td><td>8983.10 (-0.35%)</td><td>8945.70 (-0.06%)</td><td>8805.80 (-0.79%)</td><td>136.23 (-1.29%)</td><td>1950.97 (+0.79%)</td><td>1912.81 (+0.36%)</td><td>1920.46 (+0.06%)</td><td>1875.15 (+0.48%)</td><td>28.99 (-0.02%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>2.84 (n/a)</td><td>2.79 (n/a)</td><td>2.81 (n/a)</td><td>2.73 (n/a)</td><td>0.04 (n/a)</td><td>9206.20 (n/a)</td><td>9015.10 (n/a)</td><td>8951.00 (n/a)</td><td>8875.80 (n/a)</td><td>138.01 (n/a)</td><td>1935.59 (n/a)</td><td>1906.03 (n/a)</td><td>1919.32 (n/a)</td><td>1866.12 (n/a)</td><td>29.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.45 (+4.28%)</td><td>3.25 (+1.24%)</td><td>3.19 (+0.74%)</td><td>3.14 (-0.14%)</td><td>0.13 <b>(+66.44%)</b></td><td>8023.90 (+0.14%)</td><td>7754.20 (-1.15%)</td><td>7893.60 (-0.73%)</td><td>7294.70 (-4.11%)</td><td>305.20 <b>(+59.88%)</b></td><td>2355.12 (+4.28%)</td><td>2218.38 (+1.24%)</td><td>2176.44 (+0.74%)</td><td>2141.08 (-0.14%)</td><td>89.55 <b>(+66.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>3.31 (n/a)</td><td>3.21 (n/a)</td><td>3.16 (n/a)</td><td>3.14 (n/a)</td><td>0.08 (n/a)</td><td>8012.50 (n/a)</td><td>7844.10 (n/a)</td><td>7951.90 (n/a)</td><td>7607.20 (n/a)</td><td>190.90 (n/a)</td><td>2258.36 (n/a)</td><td>2191.21 (n/a)</td><td>2160.47 (n/a)</td><td>2144.14 (n/a)</td><td>53.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.78 (+0.01%)</td><td>0.78 (-0.01%)</td><td>0.78 (-0.02%)</td><td>0.78 (-0.01%)</td><td>0.00 <b>(+33.46%)</b></td><td>96492.70 (+0.01%)</td><td>96466.46 (+0.01%)</td><td>96475.20 (+0.02%)</td><td>96437.50 (-0.01%)</td><td>22.24 <b>(+33.45%)</b></td><td>712.58 (+0.01%)</td><td>712.37 (-0.01%)</td><td>712.30 (-0.02%)</td><td>712.17 (-0.01%)</td><td>0.16 <b>(+33.47%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96485.40 (n/a)</td><td>96461.48 (n/a)</td><td>96452.40 (n/a)</td><td>96447.00 (n/a)</td><td>16.66 (n/a)</td><td>712.51 (n/a)</td><td>712.40 (n/a)</td><td>712.47 (n/a)</td><td>712.23 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.73 (-0.39%)</td><td>0.73 (-0.11%)</td><td>0.73 (+0.01%)</td><td>0.73 (-0.07%)</td><td>0.00 <b>(-50.92%)</b></td><td>103865.50 (+0.07%)</td><td>103712.90 (+0.11%)</td><td>103651.60 (-0.01%)</td><td>103596.00 (+0.39%)</td><td>114.66 <b>(-50.67%)</b></td><td>663.34 (-0.39%)</td><td>662.59 (-0.11%)</td><td>662.98 (+0.01%)</td><td>661.62 (-0.07%)</td><td>0.73 <b>(-50.92%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103788.40 (n/a)</td><td>103596.80 (n/a)</td><td>103660.40 (n/a)</td><td>103195.00 (n/a)</td><td>232.46 (n/a)</td><td>665.92 (n/a)</td><td>663.34 (n/a)</td><td>662.93 (n/a)</td><td>662.11 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.69 (-0.50%)</td><td>0.69 (-0.30%)</td><td>0.69 (-0.33%)</td><td>0.69 (-0.19%)</td><td>0.00 <b>(-41.38%)</b></td><td>109933.80 (+0.19%)</td><td>109674.64 (+0.30%)</td><td>109650.40 (+0.33%)</td><td>109490.90 (+0.50%)</td><td>184.48 <b>(-40.99%)</b></td><td>627.63 (-0.50%)</td><td>626.58 (-0.30%)</td><td>626.71 (-0.33%)</td><td>625.10 (-0.19%)</td><td>1.05 <b>(-41.38%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109728.60 (n/a)</td><td>109349.16 (n/a)</td><td>109293.70 (n/a)</td><td>108942.20 (n/a)</td><td>312.60 (n/a)</td><td>630.79 (n/a)</td><td>628.45 (n/a)</td><td>628.76 (n/a)</td><td>626.27 (n/a)</td><td>1.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.12 (-2.27%)</td><td>6.75 (-3.25%)</td><td>6.88 (-2.28%)</td><td>6.35 (-1.74%)</td><td>0.36 (+9.11%)</td><td>1404.00 (+1.77%)</td><td>1323.66 (+3.40%)</td><td>1295.70 (+2.34%)</td><td>1251.10 (+2.32%)</td><td>70.73 (+14.01%)</td><td>429.11 (-2.27%)</td><td>406.51 (-3.25%)</td><td>414.34 (-2.28%)</td><td>382.37 (-1.74%)</td><td>21.47 (+9.11%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.29 (n/a)</td><td>6.98 (n/a)</td><td>7.04 (n/a)</td><td>6.46 (n/a)</td><td>0.33 (n/a)</td><td>1379.60 (n/a)</td><td>1280.12 (n/a)</td><td>1266.10 (n/a)</td><td>1222.70 (n/a)</td><td>62.04 (n/a)</td><td>439.07 (n/a)</td><td>420.14 (n/a)</td><td>424.02 (n/a)</td><td>389.15 (n/a)</td><td>19.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.11 (+0.93%)</td><td>6.02 (-11.81%)</td><td>6.72 (-1.93%)</td><td>4.74 <b>(-27.68%)</b></td><td>1.18 <b>(+556.38%)</b></td><td>1881.50 <b>(+38.27%)</b></td><td>1531.82 (+17.15%)</td><td>1326.20 (+1.97%)</td><td>1252.90 (-0.93%)</td><td>320.33 <b>(+822.92%)</b></td><td>428.50 (+0.93%)</td><td>362.32 (-11.81%)</td><td>404.82 (-1.93%)</td><td>285.34 <b>(-27.68%)</b></td><td>70.85 <b>(+556.38%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.05 (n/a)</td><td>6.82 (n/a)</td><td>6.85 (n/a)</td><td>6.55 (n/a)</td><td>0.18 (n/a)</td><td>1360.70 (n/a)</td><td>1307.54 (n/a)</td><td>1300.60 (n/a)</td><td>1264.60 (n/a)</td><td>34.71 (n/a)</td><td>424.54 (n/a)</td><td>410.82 (n/a)</td><td>412.78 (n/a)</td><td>394.56 (n/a)</td><td>10.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.04 (+2.46%)</td><td>6.55 (+7.90%)</td><td>6.55 (+3.97%)</td><td>6.22 <b>(+34.78%)</b></td><td>0.33 <b>(-61.14%)</b></td><td>1432.40 <b>(-25.80%)</b></td><td>1364.48 (-8.88%)</td><td>1359.80 (-3.83%)</td><td>1266.70 (-2.40%)</td><td>68.33 <b>(-72.62%)</b></td><td>423.83 (+2.46%)</td><td>394.27 (+7.90%)</td><td>394.80 (+3.97%)</td><td>374.82 <b>(+34.78%)</b></td><td>20.11 <b>(-61.14%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>6.87 (n/a)</td><td>6.07 (n/a)</td><td>6.30 (n/a)</td><td>4.62 (n/a)</td><td>0.86 (n/a)</td><td>1930.50 (n/a)</td><td>1497.44 (n/a)</td><td>1413.90 (n/a)</td><td>1297.90 (n/a)</td><td>249.58 (n/a)</td><td>413.66 (n/a)</td><td>365.40 (n/a)</td><td>379.71 (n/a)</td><td>278.11 (n/a)</td><td>51.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.23 (+0.45%)</td><td>7.94 (+0.80%)</td><td>7.89 (-0.12%)</td><td>7.79 (+3.31%)</td><td>0.17 <b>(-30.36%)</b></td><td>4477.90 (-3.21%)</td><td>4392.22 (-0.83%)</td><td>4418.40 (+0.12%)</td><td>4236.20 (-0.45%)</td><td>91.38 <b>(-33.36%)</b></td><td>506.94 (+0.45%)</td><td>489.10 (+0.80%)</td><td>486.04 (-0.12%)</td><td>479.58 (+3.31%)</td><td>10.40 <b>(-30.36%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.19 (n/a)</td><td>7.88 (n/a)</td><td>7.90 (n/a)</td><td>7.54 (n/a)</td><td>0.24 (n/a)</td><td>4626.20 (n/a)</td><td>4429.12 (n/a)</td><td>4413.10 (n/a)</td><td>4255.40 (n/a)</td><td>137.12 (n/a)</td><td>504.65 (n/a)</td><td>485.22 (n/a)</td><td>486.61 (n/a)</td><td>464.20 (n/a)</td><td>14.93 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.71 (-1.43%)</td><td>7.52 (+0.97%)</td><td>7.55 (-0.42%)</td><td>7.24 (+5.98%)</td><td>0.17 <b>(-54.90%)</b></td><td>4814.00 (-5.64%)</td><td>4638.42 (-1.13%)</td><td>4615.00 (+0.42%)</td><td>4520.40 (+1.45%)</td><td>107.38 <b>(-56.98%)</b></td><td>475.07 (-1.43%)</td><td>463.17 (+0.97%)</td><td>465.32 (-0.42%)</td><td>446.09 (+5.98%)</td><td>10.55 <b>(-54.90%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.82 (n/a)</td><td>7.45 (n/a)</td><td>7.59 (n/a)</td><td>6.83 (n/a)</td><td>0.38 (n/a)</td><td>5102.00 (n/a)</td><td>4691.60 (n/a)</td><td>4595.80 (n/a)</td><td>4455.90 (n/a)</td><td>249.61 (n/a)</td><td>481.94 (n/a)</td><td>458.72 (n/a)</td><td>467.27 (n/a)</td><td>420.91 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.29 (-4.01%)</td><td>7.08 (-3.85%)</td><td>7.20 (-1.53%)</td><td>6.83 (-5.79%)</td><td>0.23 <b>(+63.84%)</b></td><td>5108.40 (+6.15%)</td><td>4926.30 (+4.07%)</td><td>4840.80 (+1.55%)</td><td>4779.30 (+4.18%)</td><td>163.00 <b>(+82.13%)</b></td><td>449.33 (-4.01%)</td><td>436.30 (-3.85%)</td><td>443.62 (-1.53%)</td><td>420.39 (-5.79%)</td><td>14.29 <b>(+63.84%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.60 (n/a)</td><td>7.37 (n/a)</td><td>7.31 (n/a)</td><td>7.24 (n/a)</td><td>0.14 (n/a)</td><td>4812.50 (n/a)</td><td>4733.68 (n/a)</td><td>4766.80 (n/a)</td><td>4587.60 (n/a)</td><td>89.49 (n/a)</td><td>468.10 (n/a)</td><td>453.79 (n/a)</td><td>450.51 (n/a)</td><td>446.23 (n/a)</td><td>8.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.79 (+0.42%)</td><td>0.79 (+0.09%)</td><td>0.79 (+0.00%)</td><td>0.79 (-0.02%)</td><td>0.00 <b>(+487.39%)</b></td><td>95833.00 (+0.02%)</td><td>95675.16 (-0.09%)</td><td>95745.50 (-0.00%)</td><td>95330.80 (-0.42%)</td><td>197.35 <b>(+484.90%)</b></td><td>720.85 (+0.42%)</td><td>718.26 (+0.09%)</td><td>717.73 (+0.00%)</td><td>717.08 (-0.02%)</td><td>1.49 <b>(+487.37%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95809.70 (n/a)</td><td>95764.80 (n/a)</td><td>95745.70 (n/a)</td><td>95733.40 (n/a)</td><td>33.74 (n/a)</td><td>717.82 (n/a)</td><td>717.59 (n/a)</td><td>717.73 (n/a)</td><td>717.25 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.73 (-0.00%)</td><td>0.73 (-0.04%)</td><td>0.73 (+0.01%)</td><td>0.73 (-0.14%)</td><td>0.00 <b>(+52.77%)</b></td><td>103307.50 (+0.14%)</td><td>103025.28 (+0.04%)</td><td>102936.30 (-0.01%)</td><td>102902.20 (+0.00%)</td><td>166.70 <b>(+52.99%)</b></td><td>667.81 (-0.00%)</td><td>667.02 (-0.04%)</td><td>667.59 (+0.01%)</td><td>665.19 (-0.14%)</td><td>1.08 <b>(+52.76%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103167.40 (n/a)</td><td>102979.90 (n/a)</td><td>102946.80 (n/a)</td><td>102898.50 (n/a)</td><td>108.96 (n/a)</td><td>667.84 (n/a)</td><td>667.31 (n/a)</td><td>667.52 (n/a)</td><td>666.10 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.70 (+0.19%)</td><td>0.70 (+0.10%)</td><td>0.70 (+0.06%)</td><td>0.70 (+0.23%)</td><td>0.00 (-8.88%)</td><td>108322.30 (-0.23%)</td><td>108113.84 (-0.10%)</td><td>108101.10 (-0.06%)</td><td>107881.20 (-0.19%)</td><td>178.75 (-9.29%)</td><td>636.99 (+0.19%)</td><td>635.62 (+0.10%)</td><td>635.70 (+0.06%)</td><td>634.40 (+0.23%)</td><td>1.05 (-8.87%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108570.60 (n/a)</td><td>108224.64 (n/a)</td><td>108163.10 (n/a)</td><td>108084.10 (n/a)</td><td>197.04 (n/a)</td><td>635.80 (n/a)</td><td>634.97 (n/a)</td><td>635.33 (n/a)</td><td>632.95 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.91 (-6.87%)</td><td>3.64 (+4.85%)</td><td>3.69 (+6.35%)</td><td>3.31 (+14.38%)</td><td>0.26 <b>(-45.92%)</b></td><td>2434.60 (-12.57%)</td><td>2224.78 (-5.66%)</td><td>2183.40 (-5.98%)</td><td>2064.10 (+7.38%)</td><td>162.60 <b>(-49.10%)</b></td><td>1024.13 (-6.87%)</td><td>954.17 (+4.85%)</td><td>968.17 (+6.35%)</td><td>868.27 (+14.38%)</td><td>68.54 <b>(-45.92%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>4.19 (n/a)</td><td>3.47 (n/a)</td><td>3.47 (n/a)</td><td>2.89 (n/a)</td><td>0.48 (n/a)</td><td>2784.70 (n/a)</td><td>2358.22 (n/a)</td><td>2322.20 (n/a)</td><td>1922.30 (n/a)</td><td>319.46 (n/a)</td><td>1099.70 (n/a)</td><td>910.04 (n/a)</td><td>910.33 (n/a)</td><td>759.13 (n/a)</td><td>126.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.34 (-11.80%)</td><td>0.31 (-8.12%)</td><td>0.32 (-6.22%)</td><td>0.27 (-6.56%)</td><td>0.03 (-18.30%)</td><td>4609.20 (+7.02%)</td><td>4081.22 (+8.66%)</td><td>3868.00 (+6.63%)</td><td>3696.50 (+13.39%)</td><td>393.68 (-0.90%)</td><td>18.15 (-11.80%)</td><td>16.56 (-8.12%)</td><td>17.35 (-6.22%)</td><td>14.56 (-6.56%)</td><td>1.54 (-18.30%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>4306.90 (n/a)</td><td>3756.12 (n/a)</td><td>3627.40 (n/a)</td><td>3260.10 (n/a)</td><td>397.25 (n/a)</td><td>20.58 (n/a)</td><td>18.03 (n/a)</td><td>18.50 (n/a)</td><td>15.58 (n/a)</td><td>1.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>6.20 (-5.02%)</td><td>4.75 (-3.46%)</td><td>4.81 (-3.60%)</td><td>3.24 (-7.49%)</td><td>1.05 <b>(-24.56%)</b></td><td>2050.20 (+8.10%)</td><td>1463.06 (+1.10%)</td><td>1382.70 (+3.73%)</td><td>1073.10 (+5.29%)</td><td>358.09 (-14.79%)</td><td>1915.18 (-5.02%)</td><td>1466.48 (-3.46%)</td><td>1486.33 (-3.60%)</td><td>1002.44 (-7.49%)</td><td>324.10 <b>(-24.56%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>6.53 (n/a)</td><td>4.92 (n/a)</td><td>4.99 (n/a)</td><td>3.51 (n/a)</td><td>1.39 (n/a)</td><td>1896.60 (n/a)</td><td>1447.20 (n/a)</td><td>1333.00 (n/a)</td><td>1019.20 (n/a)</td><td>420.23 (n/a)</td><td>2016.50 (n/a)</td><td>1519.01 (n/a)</td><td>1541.76 (n/a)</td><td>1083.60 (n/a)</td><td>429.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 <b>(-30.94%)</b></td><td>0.17 (-18.76%)</td><td>0.19 (-4.97%)</td><td>0.15 (-16.84%)</td><td>0.02 <b>(-54.86%)</b></td><td>0.19 <b>(-30.94%)</b></td><td>0.17 (-18.76%)</td><td>0.18 (-4.97%)</td><td>0.15 (-16.84%)</td><td>0.02 <b>(-54.86%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.33 (-1.02%)</td><td>12.95 (+0.29%)</td><td>13.26 (+0.66%)</td><td>11.60 (-3.98%)</td><td>0.75 <b>(+28.00%)</b></td><td>13.32 (-1.02%)</td><td>12.94 (+0.29%)</td><td>13.25 (+0.66%)</td><td>11.60 (-3.98%)</td><td>0.75 <b>(+28.00%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.47 (n/a)</td><td>12.91 (n/a)</td><td>13.17 (n/a)</td><td>12.09 (n/a)</td><td>0.59 (n/a)</td><td>13.46 (n/a)</td><td>12.90 (n/a)</td><td>13.17 (n/a)</td><td>12.08 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>24.90 (-0.78%)</td><td>24.08 (-0.75%)</td><td>23.92 (+0.14%)</td><td>23.55 (-0.58%)</td><td>0.53 (-16.14%)</td><td>24.88 (-0.78%)</td><td>24.06 (-0.75%)</td><td>23.91 (+0.14%)</td><td>23.54 (-0.58%)</td><td>0.53 (-16.14%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>25.09 (n/a)</td><td>24.26 (n/a)</td><td>23.89 (n/a)</td><td>23.69 (n/a)</td><td>0.63 (n/a)</td><td>25.07 (n/a)</td><td>24.25 (n/a)</td><td>23.87 (n/a)</td><td>23.67 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>40.72 (+0.99%)</td><td>40.01 (+0.91%)</td><td>40.64 (+1.59%)</td><td>38.53 (-0.04%)</td><td>0.97 <b>(+31.16%)</b></td><td>40.70 (+0.99%)</td><td>39.99 (+0.91%)</td><td>40.62 (+1.59%)</td><td>38.51 (-0.04%)</td><td>0.97 <b>(+31.16%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>40.32 (n/a)</td><td>39.65 (n/a)</td><td>40.01 (n/a)</td><td>38.55 (n/a)</td><td>0.74 (n/a)</td><td>40.30 (n/a)</td><td>39.63 (n/a)</td><td>39.98 (n/a)</td><td>38.53 (n/a)</td><td>0.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>45.33 (+0.41%)</td><td>43.35 (-0.31%)</td><td>43.72 (+1.41%)</td><td>41.61 (-0.42%)</td><td>1.51 (+1.13%)</td><td>45.30 (+0.41%)</td><td>43.32 (-0.31%)</td><td>43.69 (+1.41%)</td><td>41.58 (-0.42%)</td><td>1.51 (+1.13%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>45.14 (n/a)</td><td>43.48 (n/a)</td><td>43.11 (n/a)</td><td>41.78 (n/a)</td><td>1.50 (n/a)</td><td>45.11 (n/a)</td><td>43.46 (n/a)</td><td>43.08 (n/a)</td><td>41.76 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.31 (-0.55%)</td><td>12.95 (-0.71%)</td><td>13.23 (+0.39%)</td><td>12.44 (+1.21%)</td><td>0.42 (-4.31%)</td><td>13.30 (-0.55%)</td><td>12.95 (-0.71%)</td><td>13.22 (+0.39%)</td><td>12.43 (+1.21%)</td><td>0.42 (-4.31%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.38 (n/a)</td><td>13.05 (n/a)</td><td>13.18 (n/a)</td><td>12.29 (n/a)</td><td>0.43 (n/a)</td><td>13.37 (n/a)</td><td>13.04 (n/a)</td><td>13.17 (n/a)</td><td>12.28 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>24.29 (-1.99%)</td><td>23.86 (+0.18%)</td><td>24.12 (+1.91%)</td><td>22.73 (-1.37%)</td><td>0.65 (-19.57%)</td><td>24.28 (-1.99%)</td><td>23.85 (+0.18%)</td><td>24.10 (+1.91%)</td><td>22.72 (-1.37%)</td><td>0.65 (-19.57%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>24.79 (n/a)</td><td>23.82 (n/a)</td><td>23.66 (n/a)</td><td>23.05 (n/a)</td><td>0.80 (n/a)</td><td>24.77 (n/a)</td><td>23.80 (n/a)</td><td>23.65 (n/a)</td><td>23.04 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>42.98 (+5.97%)</td><td>41.22 (+5.63%)</td><td>40.96 (+5.82%)</td><td>40.50 (+7.85%)</td><td>1.00 (-12.90%)</td><td>42.95 (+5.97%)</td><td>41.20 (+5.63%)</td><td>40.94 (+5.82%)</td><td>40.47 (+7.85%)</td><td>1.00 (-12.90%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>40.56 (n/a)</td><td>39.03 (n/a)</td><td>38.71 (n/a)</td><td>37.55 (n/a)</td><td>1.15 (n/a)</td><td>40.53 (n/a)</td><td>39.00 (n/a)</td><td>38.68 (n/a)</td><td>37.53 (n/a)</td><td>1.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>42.94 (-3.66%)</td><td>41.80 (-2.37%)</td><td>42.69 (+0.37%)</td><td>38.83 (-7.28%)</td><td>1.74 <b>(+68.91%)</b></td><td>42.92 (-3.66%)</td><td>41.78 (-2.37%)</td><td>42.66 (+0.37%)</td><td>38.81 (-7.28%)</td><td>1.74 <b>(+68.91%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>44.57 (n/a)</td><td>42.82 (n/a)</td><td>42.53 (n/a)</td><td>41.88 (n/a)</td><td>1.03 (n/a)</td><td>44.54 (n/a)</td><td>42.79 (n/a)</td><td>42.50 (n/a)</td><td>41.85 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>168.52 (n/a)</td><td>176.90 (n/a)</td><td>124.60 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>160.46 (n/a)</td><td>170.80 (n/a)</td><td>99.00 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.70 (n/a)</td><td>164.00 (n/a)</td><td>160.00 (n/a)</td><td>129.10 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>175.34 (n/a)</td><td>156.90 (n/a)</td><td>129.20 (n/a)</td><td>40.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>301.60 (n/a)</td><td>185.58 (n/a)</td><td>158.00 (n/a)</td><td>139.60 (n/a)</td><td>66.10 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>183.76 (n/a)</td><td>188.60 (n/a)</td><td>155.20 (n/a)</td><td>23.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>262.20 (n/a)</td><td>201.44 (n/a)</td><td>183.20 (n/a)</td><td>173.40 (n/a)</td><td>36.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.50 (n/a)</td><td>200.38 (n/a)</td><td>195.10 (n/a)</td><td>194.50 (n/a)</td><td>10.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>390.30 (n/a)</td><td>197.12 (n/a)</td><td>158.20 (n/a)</td><td>130.50 (n/a)</td><td>109.53 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>164.52 (n/a)</td><td>167.60 (n/a)</td><td>132.60 (n/a)</td><td>32.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.40 (n/a)</td><td>176.22 (n/a)</td><td>153.10 (n/a)</td><td>141.30 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>303.70 (n/a)</td><td>196.08 (n/a)</td><td>179.80 (n/a)</td><td>124.30 (n/a)</td><td>67.97 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>163.98 (n/a)</td><td>177.40 (n/a)</td><td>127.80 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>172.86 (n/a)</td><td>168.10 (n/a)</td><td>158.80 (n/a)</td><td>12.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>348.50 (n/a)</td><td>217.50 (n/a)</td><td>178.60 (n/a)</td><td>163.00 (n/a)</td><td>76.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>191.20 (n/a)</td><td>194.10 (n/a)</td><td>170.40 (n/a)</td><td>19.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>241.50 (n/a)</td><td>170.32 (n/a)</td><td>156.30 (n/a)</td><td>144.80 (n/a)</td><td>40.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>166.82 (n/a)</td><td>150.90 (n/a)</td><td>140.60 (n/a)</td><td>37.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.60 (n/a)</td><td>174.56 (n/a)</td><td>167.20 (n/a)</td><td>130.80 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>256.30 (n/a)</td><td>199.24 (n/a)</td><td>184.30 (n/a)</td><td>140.30 (n/a)</td><td>45.66 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.30 (n/a)</td><td>190.22 (n/a)</td><td>183.90 (n/a)</td><td>152.70 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>196.60 (n/a)</td><td>199.10 (n/a)</td><td>161.30 (n/a)</td><td>33.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>244.60 (n/a)</td><td>204.60 (n/a)</td><td>192.30 (n/a)</td><td>174.90 (n/a)</td><td>33.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>260.30 (n/a)</td><td>240.24 (n/a)</td><td>244.00 (n/a)</td><td>222.40 (n/a)</td><td>15.89 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (+17.50%)</td><td>0.18 (+8.39%)</td><td>0.17 (-0.32%)</td><td>0.14 (-6.88%)</td><td>0.04 <b>(+88.25%)</b></td><td>235.50 (+7.39%)</td><td>185.60 (-4.86%)</td><td>197.70 (+0.36%)</td><td>132.60 (-14.89%)</td><td>42.16 <b>(+72.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.30 (n/a)</td><td>195.08 (n/a)</td><td>197.00 (n/a)</td><td>155.80 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>250.10 (n/a)</td><td>208.90 (n/a)</td><td>240.90 (n/a)</td><td>145.10 (n/a)</td><td>51.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>250.60 (n/a)</td><td>182.80 (n/a)</td><td>172.30 (n/a)</td><td>144.90 (n/a)</td><td>43.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.90 (n/a)</td><td>180.12 (n/a)</td><td>190.40 (n/a)</td><td>136.20 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>375.90 (n/a)</td><td>214.36 (n/a)</td><td>174.60 (n/a)</td><td>171.20 (n/a)</td><td>90.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.40 (n/a)</td><td>178.44 (n/a)</td><td>171.30 (n/a)</td><td>155.60 (n/a)</td><td>21.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>201.50 (n/a)</td><td>178.76 (n/a)</td><td>171.40 (n/a)</td><td>154.60 (n/a)</td><td>21.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>259.10 (n/a)</td><td>218.14 (n/a)</td><td>219.40 (n/a)</td><td>185.10 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+10.93%)</td><td>0.03 (+17.73%)</td><td>0.03 (+7.28%)</td><td>0.02 <b>(+108.56%)</b></td><td>0.00 <b>(-51.30%)</b></td><td>189.30 <b>(-52.05%)</b></td><td>161.82 <b>(-23.82%)</b></td><td>158.90 (-6.80%)</td><td>140.50 (-9.88%)</td><td>20.42 <b>(-80.04%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>394.80 (n/a)</td><td>212.42 (n/a)</td><td>170.50 (n/a)</td><td>155.90 (n/a)</td><td>102.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-1.53%)</td><td>0.02 (+4.57%)</td><td>0.02 (+1.75%)</td><td>0.02 <b>(+29.32%)</b></td><td>0.00 <b>(-38.64%)</b></td><td>205.60 <b>(-22.65%)</b></td><td>172.30 (-7.75%)</td><td>165.70 (-1.72%)</td><td>148.00 (+1.58%)</td><td>24.88 <b>(-50.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>265.80 (n/a)</td><td>186.78 (n/a)</td><td>168.60 (n/a)</td><td>145.70 (n/a)</td><td>50.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+1.12%)</td><td>0.02 (+12.65%)</td><td>0.02 <b>(+29.73%)</b></td><td>0.02 <b>(+28.41%)</b></td><td>0.00 <b>(-34.80%)</b></td><td>257.50 <b>(-22.11%)</b></td><td>190.54 (-15.71%)</td><td>177.80 <b>(-22.93%)</b></td><td>154.80 (-1.09%)</td><td>40.17 <b>(-44.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>330.60 (n/a)</td><td>226.04 (n/a)</td><td>230.70 (n/a)</td><td>156.50 (n/a)</td><td>73.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+11.97%)</td><td>0.02 (+6.46%)</td><td>0.02 (+10.32%)</td><td>0.02 (+2.63%)</td><td>0.00 <b>(+20.43%)</b></td><td>230.30 (-2.54%)</td><td>193.44 (-5.62%)</td><td>188.50 (-9.38%)</td><td>146.10 (-10.70%)</td><td>32.83 (+2.74%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>204.96 (n/a)</td><td>208.00 (n/a)</td><td>163.60 (n/a)</td><td>31.95 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+14.57%)</td><td>0.02 (-10.03%)</td><td>0.02 (-15.17%)</td><td>0.02 (-18.38%)</td><td>0.01 <b>(+81.76%)</b></td><td>251.10 <b>(+22.55%)</b></td><td>191.44 (+14.79%)</td><td>193.60 (+17.90%)</td><td>129.10 (-12.71%)</td><td>43.66 <b>(+88.51%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.90 (n/a)</td><td>166.78 (n/a)</td><td>164.20 (n/a)</td><td>147.90 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-8.76%)</td><td>0.03 (-7.62%)</td><td>0.02 (-6.90%)</td><td>0.02 (+0.38%)</td><td>0.00 <b>(-27.58%)</b></td><td>205.30 (-0.34%)</td><td>164.96 (+6.22%)</td><td>172.10 (+7.43%)</td><td>128.20 (+9.57%)</td><td>30.56 (-18.56%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>155.30 (n/a)</td><td>160.20 (n/a)</td><td>117.00 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-9.10%)</td><td>0.02 (+7.91%)</td><td>0.02 (+5.48%)</td><td>0.02 <b>(+92.51%)</b></td><td>0.00 <b>(-59.85%)</b></td><td>204.40 <b>(-48.04%)</b></td><td>178.72 (-17.42%)</td><td>168.40 (-5.18%)</td><td>158.00 (+10.03%)</td><td>22.59 <b>(-77.86%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>393.40 (n/a)</td><td>216.42 (n/a)</td><td>177.60 (n/a)</td><td>143.60 (n/a)</td><td>102.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-2.52%)</td><td>0.03 (+3.56%)</td><td>0.02 (-3.45%)</td><td>0.02 <b>(+22.55%)</b></td><td>0.01 <b>(-21.18%)</b></td><td>190.70 (-18.40%)</td><td>166.08 (-5.68%)</td><td>182.70 (+3.57%)</td><td>123.10 (+2.58%)</td><td>29.11 <b>(-32.82%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.70 (n/a)</td><td>176.08 (n/a)</td><td>176.40 (n/a)</td><td>120.00 (n/a)</td><td>43.33 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-0.68%)</td><td>0.02 (+16.68%)</td><td>0.02 (+9.85%)</td><td>0.02 <b>(+64.59%)</b></td><td>0.00 <b>(-66.40%)</b></td><td>182.60 <b>(-39.25%)</b></td><td>172.18 (-17.95%)</td><td>173.30 (-8.98%)</td><td>157.40 (+0.70%)</td><td>10.89 <b>(-80.08%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>300.60 (n/a)</td><td>209.86 (n/a)</td><td>190.40 (n/a)</td><td>156.30 (n/a)</td><td>54.68 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-12.68%)</td><td>0.03 (+8.62%)</td><td>0.02 (+13.84%)</td><td>0.02 <b>(+21.95%)</b></td><td>0.00 <b>(-54.73%)</b></td><td>181.50 (-17.98%)</td><td>161.16 (-11.55%)</td><td>164.80 (-12.15%)</td><td>136.80 (+14.48%)</td><td>17.57 <b>(-57.59%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>182.20 (n/a)</td><td>187.60 (n/a)</td><td>119.50 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-5.03%)</td><td>0.02 (+1.29%)</td><td>0.02 (+17.76%)</td><td>0.02 (-3.56%)</td><td>0.00 (-11.95%)</td><td>219.90 (+3.68%)</td><td>186.90 (-1.59%)</td><td>177.10 (-15.10%)</td><td>161.90 (+5.27%)</td><td>26.49 (-5.17%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.10 (n/a)</td><td>189.92 (n/a)</td><td>208.60 (n/a)</td><td>153.80 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 <b>(+61.44%)</b></td><td>0.03 <b>(+28.61%)</b></td><td>0.02 (+5.08%)</td><td>0.02 <b>(+27.08%)</b></td><td>0.01 <b>(+112.42%)</b></td><td>182.60 <b>(-21.33%)</b></td><td>152.70 <b>(-20.77%)</b></td><td>164.50 (-4.80%)</td><td>106.70 <b>(-38.04%)</b></td><td>29.22 (+2.84%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.10 (n/a)</td><td>192.72 (n/a)</td><td>172.80 (n/a)</td><td>172.20 (n/a)</td><td>28.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 <b>(+21.00%)</b></td><td>0.02 (+18.24%)</td><td>0.02 (+12.89%)</td><td>0.02 <b>(+21.58%)</b></td><td>0.00 (+4.96%)</td><td>194.00 (-17.76%)</td><td>171.56 (-15.58%)</td><td>170.30 (-11.39%)</td><td>155.40 (-17.34%)</td><td>14.57 <b>(-28.06%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.90 (n/a)</td><td>203.22 (n/a)</td><td>192.20 (n/a)</td><td>188.00 (n/a)</td><td>20.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+13.77%)</td><td>0.02 (-2.30%)</td><td>0.02 (-2.86%)</td><td>0.02 (-15.12%)</td><td>0.00 <b>(+109.27%)</b></td><td>238.30 (+17.80%)</td><td>180.34 (+5.00%)</td><td>168.70 (+2.99%)</td><td>140.40 (-12.09%)</td><td>37.84 <b>(+116.53%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>171.76 (n/a)</td><td>163.80 (n/a)</td><td>159.70 (n/a)</td><td>17.47 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-6.72%)</td><td>0.03 (+11.73%)</td><td>0.02 <b>(+21.20%)</b></td><td>0.02 <b>(+25.11%)</b></td><td>0.00 <b>(-48.95%)</b></td><td>181.00 <b>(-20.05%)</b></td><td>161.78 (-13.67%)</td><td>165.40 (-17.47%)</td><td>135.90 (+7.18%)</td><td>18.18 <b>(-56.63%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>187.40 (n/a)</td><td>200.40 (n/a)</td><td>126.80 (n/a)</td><td>41.90 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-16.97%)</td><td>0.02 (-7.55%)</td><td>0.02 (+8.42%)</td><td>0.02 (-6.81%)</td><td>0.01 <b>(-25.59%)</b></td><td>248.10 (+7.31%)</td><td>196.90 (+6.46%)</td><td>183.80 (-7.78%)</td><td>136.20 <b>(+20.42%)</b></td><td>48.77 (+1.53%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>184.96 (n/a)</td><td>199.30 (n/a)</td><td>113.10 (n/a)</td><td>48.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 <b>(+58.38%)</b></td><td>0.05 <b>(+22.53%)</b></td><td>0.05 (+13.67%)</td><td>0.04 (+2.65%)</td><td>0.01 <b>(+341.13%)</b></td><td>206.80 (-2.54%)</td><td>165.94 (-14.62%)</td><td>167.90 (-12.05%)</td><td>111.40 <b>(-36.85%)</b></td><td>38.53 <b>(+170.92%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.20 (n/a)</td><td>194.36 (n/a)</td><td>190.90 (n/a)</td><td>176.40 (n/a)</td><td>14.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (+18.72%)</td><td>0.05 (+7.04%)</td><td>0.05 (+12.40%)</td><td>0.04 (-3.83%)</td><td>0.01 <b>(+137.64%)</b></td><td>205.90 (+3.99%)</td><td>169.58 (-5.03%)</td><td>159.80 (-11.02%)</td><td>138.80 (-15.73%)</td><td>27.34 <b>(+110.30%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.00 (n/a)</td><td>178.56 (n/a)</td><td>179.60 (n/a)</td><td>164.70 (n/a)</td><td>13.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (-1.00%)</td><td>0.04 (-6.71%)</td><td>0.03 (-17.62%)</td><td>0.03 (-0.83%)</td><td>0.00 (+2.04%)</td><td>237.00 (+0.85%)</td><td>219.72 (+7.27%)</td><td>234.90 <b>(+21.40%)</b></td><td>185.60 (+1.03%)</td><td>22.98 (+4.81%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.00 (n/a)</td><td>204.82 (n/a)</td><td>193.50 (n/a)</td><td>183.70 (n/a)</td><td>21.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (-9.84%)</td><td>0.04 (-16.39%)</td><td>0.04 (-17.01%)</td><td>0.03 <b>(-28.57%)</b></td><td>0.01 (+9.43%)</td><td>319.20 <b>(+40.00%)</b></td><td>233.00 <b>(+21.66%)</b></td><td>221.90 <b>(+20.47%)</b></td><td>173.00 (+10.90%)</td><td>53.19 <b>(+71.49%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>191.52 (n/a)</td><td>184.20 (n/a)</td><td>156.00 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 <b>(+31.11%)</b></td><td>0.05 <b>(+20.46%)</b></td><td>0.05 (+13.79%)</td><td>0.04 (+16.87%)</td><td>0.01 <b>(+64.30%)</b></td><td>186.60 (-14.44%)</td><td>163.48 (-16.39%)</td><td>173.20 (-12.13%)</td><td>129.30 <b>(-23.72%)</b></td><td>22.70 (+5.33%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.10 (n/a)</td><td>195.52 (n/a)</td><td>197.10 (n/a)</td><td>169.50 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (-6.03%)</td><td>0.05 (+2.78%)</td><td>0.05 (-3.48%)</td><td>0.05 <b>(+25.84%)</b></td><td>0.00 <b>(-58.28%)</b></td><td>172.30 <b>(-20.53%)</b></td><td>162.30 (-4.41%)</td><td>166.40 (+3.61%)</td><td>150.40 (+6.36%)</td><td>9.86 <b>(-65.65%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>169.78 (n/a)</td><td>160.60 (n/a)</td><td>141.40 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 <b>(+21.06%)</b></td><td>0.06 <b>(+24.69%)</b></td><td>0.06 (+18.23%)</td><td>0.05 <b>(+34.00%)</b></td><td>0.01 (-6.61%)</td><td>173.80 <b>(-25.38%)</b></td><td>148.44 <b>(-20.73%)</b></td><td>147.30 (-15.44%)</td><td>129.90 (-17.42%)</td><td>19.23 <b>(-42.95%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>187.26 (n/a)</td><td>174.20 (n/a)</td><td>157.30 (n/a)</td><td>33.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 <b>(+23.33%)</b></td><td>0.06 (+16.91%)</td><td>0.05 (+6.25%)</td><td>0.05 (+17.65%)</td><td>0.01 <b>(+59.85%)</b></td><td>178.00 (-15.00%)</td><td>150.26 (-13.48%)</td><td>163.00 (-5.89%)</td><td>115.80 (-18.96%)</td><td>26.41 (+9.34%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>173.68 (n/a)</td><td>173.20 (n/a)</td><td>142.90 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 <b>(+49.64%)</b></td><td>0.06 <b>(+31.93%)</b></td><td>0.06 <b>(+25.38%)</b></td><td>0.04 (+4.15%)</td><td>0.01 <b>(+242.56%)</b></td><td>210.00 (-4.02%)</td><td>153.62 <b>(-20.92%)</b></td><td>147.40 <b>(-20.24%)</b></td><td>117.10 <b>(-33.16%)</b></td><td>39.09 <b>(+112.15%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>194.26 (n/a)</td><td>184.80 (n/a)</td><td>175.20 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 <b>(+37.73%)</b></td><td>0.06 <b>(+26.30%)</b></td><td>0.06 <b>(+25.67%)</b></td><td>0.05 (+18.93%)</td><td>0.01 <b>(+93.36%)</b></td><td>176.10 (-15.90%)</td><td>145.62 (-19.55%)</td><td>131.90 <b>(-20.45%)</b></td><td>118.20 <b>(-27.40%)</b></td><td>27.63 <b>(+22.89%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>181.00 (n/a)</td><td>165.80 (n/a)</td><td>162.80 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 <b>(+44.26%)</b></td><td>0.06 (+19.15%)</td><td>0.05 (+8.85%)</td><td>0.05 <b>(+26.19%)</b></td><td>0.01 <b>(+100.01%)</b></td><td>171.80 <b>(-20.72%)</b></td><td>149.80 (-14.46%)</td><td>155.90 (-8.13%)</td><td>101.80 <b>(-30.65%)</b></td><td>27.98 (+5.21%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>175.12 (n/a)</td><td>169.70 (n/a)</td><td>146.80 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (+15.19%)</td><td>0.05 (+8.55%)</td><td>0.05 (+11.15%)</td><td>0.04 (-3.64%)</td><td>0.01 <b>(+45.43%)</b></td><td>227.40 (+3.79%)</td><td>181.10 (-6.89%)</td><td>176.10 (-10.02%)</td><td>142.40 (-13.22%)</td><td>31.07 <b>(+30.19%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>194.50 (n/a)</td><td>195.70 (n/a)</td><td>164.10 (n/a)</td><td>23.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (-14.57%)</td><td>0.04 (+7.34%)</td><td>0.04 (+13.14%)</td><td>0.04 <b>(+57.24%)</b></td><td>0.00 <b>(-67.41%)</b></td><td>204.10 <b>(-36.40%)</b></td><td>188.56 (-13.19%)</td><td>193.30 (-11.61%)</td><td>162.40 (+17.00%)</td><td>16.44 <b>(-75.89%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>320.90 (n/a)</td><td>217.20 (n/a)</td><td>218.70 (n/a)</td><td>138.80 (n/a)</td><td>68.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 <b>(+26.37%)</b></td><td>0.05 (+14.91%)</td><td>0.05 (+9.28%)</td><td>0.04 (+1.83%)</td><td>0.01 <b>(+44.90%)</b></td><td>219.60 (-1.83%)</td><td>165.52 (-11.77%)</td><td>167.60 (-8.47%)</td><td>121.60 <b>(-20.83%)</b></td><td>36.14 (+11.71%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>187.60 (n/a)</td><td>183.10 (n/a)</td><td>153.60 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 <b>(+23.38%)</b></td><td>0.05 (+9.95%)</td><td>0.04 (+3.66%)</td><td>0.04 (+6.16%)</td><td>0.01 <b>(+70.76%)</b></td><td>213.70 (-5.82%)</td><td>185.52 (-7.06%)</td><td>199.70 (-3.53%)</td><td>124.60 (-18.93%)</td><td>36.10 <b>(+31.89%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>199.62 (n/a)</td><td>207.00 (n/a)</td><td>153.70 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (+15.60%)</td><td>0.05 (+8.90%)</td><td>0.05 (+2.83%)</td><td>0.04 (+2.57%)</td><td>0.01 <b>(+111.87%)</b></td><td>200.70 (-2.53%)</td><td>172.04 (-7.13%)</td><td>179.30 (-2.71%)</td><td>145.80 (-13.47%)</td><td>23.57 <b>(+73.57%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.90 (n/a)</td><td>185.24 (n/a)</td><td>184.30 (n/a)</td><td>168.50 (n/a)</td><td>13.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (-7.45%)</td><td>0.10 (-3.10%)</td><td>0.10 (-4.02%)</td><td>0.09 (-0.76%)</td><td>0.01 <b>(-22.08%)</b></td><td>178.50 (+0.79%)</td><td>164.64 (+2.91%)</td><td>166.00 (+4.21%)</td><td>148.10 (+8.02%)</td><td>13.66 (-15.00%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.10 (n/a)</td><td>159.98 (n/a)</td><td>159.30 (n/a)</td><td>137.10 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (+9.50%)</td><td>0.11 (+2.93%)</td><td>0.10 (-11.08%)</td><td>0.08 (-10.67%)</td><td>0.03 <b>(+90.97%)</b></td><td>206.30 (+11.94%)</td><td>156.54 (+1.25%)</td><td>171.30 (+12.48%)</td><td>113.30 (-8.63%)</td><td>40.78 <b>(+86.31%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.30 (n/a)</td><td>154.60 (n/a)</td><td>152.30 (n/a)</td><td>124.00 (n/a)</td><td>21.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (+14.13%)</td><td>0.08 (+10.97%)</td><td>0.09 (+13.22%)</td><td>0.06 (-7.74%)</td><td>0.02 <b>(+101.46%)</b></td><td>262.60 (+8.38%)</td><td>201.26 (-7.81%)</td><td>192.60 (-11.69%)</td><td>162.80 (-12.38%)</td><td>41.06 <b>(+90.85%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>218.32 (n/a)</td><td>218.10 (n/a)</td><td>185.80 (n/a)</td><td>21.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (+0.24%)</td><td>0.08 (-10.57%)</td><td>0.08 (-13.97%)</td><td>0.06 (-19.92%)</td><td>0.02 <b>(+40.15%)</b></td><td>277.40 <b>(+24.90%)</b></td><td>213.10 (+14.13%)</td><td>210.70 (+16.22%)</td><td>154.00 (-0.26%)</td><td>44.33 <b>(+72.37%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>186.72 (n/a)</td><td>181.30 (n/a)</td><td>154.40 (n/a)</td><td>25.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (+18.31%)</td><td>0.11 (+1.90%)</td><td>0.09 (-9.78%)</td><td>0.08 (-15.79%)</td><td>0.03 <b>(+170.85%)</b></td><td>204.50 (+18.76%)</td><td>162.16 (+2.26%)</td><td>175.30 (+10.88%)</td><td>116.40 (-15.47%)</td><td>38.08 <b>(+164.91%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>158.58 (n/a)</td><td>158.10 (n/a)</td><td>137.70 (n/a)</td><td>14.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (-11.19%)</td><td>0.10 (-1.25%)</td><td>0.10 (+6.30%)</td><td>0.08 (-10.06%)</td><td>0.01 (-6.37%)</td><td>213.40 (+11.20%)</td><td>169.92 (+1.48%)</td><td>159.50 (-5.90%)</td><td>153.20 (+12.65%)</td><td>24.72 <b>(+22.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>167.44 (n/a)</td><td>169.50 (n/a)</td><td>136.00 (n/a)</td><td>20.15 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (+15.23%)</td><td>0.10 (+10.48%)</td><td>0.11 (+16.90%)</td><td>0.07 (-8.37%)</td><td>0.02 <b>(+32.64%)</b></td><td>236.30 (+9.15%)</td><td>164.92 (-7.64%)</td><td>149.80 (-14.45%)</td><td>122.70 (-13.16%)</td><td>44.52 <b>(+27.05%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>178.56 (n/a)</td><td>175.10 (n/a)</td><td>141.30 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (+5.95%)</td><td>0.11 (+5.64%)</td><td>0.11 (+9.03%)</td><td>0.08 (-5.27%)</td><td>0.02 <b>(+34.10%)</b></td><td>204.10 (+5.59%)</td><td>157.38 (-4.41%)</td><td>149.50 (-8.28%)</td><td>131.00 (-5.62%)</td><td>27.68 <b>(+38.26%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>164.64 (n/a)</td><td>163.00 (n/a)</td><td>138.80 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (-15.50%)</td><td>0.09 (-5.87%)</td><td>0.10 (-5.78%)</td><td>0.07 (-8.58%)</td><td>0.01 <b>(-30.52%)</b></td><td>229.00 (+9.41%)</td><td>181.44 (+5.29%)</td><td>168.70 (+6.17%)</td><td>166.60 (+18.32%)</td><td>26.78 (-10.79%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.30 (n/a)</td><td>172.32 (n/a)</td><td>158.90 (n/a)</td><td>140.80 (n/a)</td><td>30.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (+9.27%)</td><td>0.09 (-4.58%)</td><td>0.09 (-10.32%)</td><td>0.07 (-12.89%)</td><td>0.02 <b>(+43.79%)</b></td><td>218.90 (+14.79%)</td><td>178.22 (+6.13%)</td><td>175.10 (+11.53%)</td><td>136.90 (-8.49%)</td><td>30.51 <b>(+47.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>167.92 (n/a)</td><td>157.00 (n/a)</td><td>149.60 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 <b>(+25.97%)</b></td><td>0.10 (+17.64%)</td><td>0.10 (+17.98%)</td><td>0.07 (-3.14%)</td><td>0.02 <b>(+112.19%)</b></td><td>225.90 (+3.24%)</td><td>166.04 (-12.91%)</td><td>163.80 (-15.22%)</td><td>132.60 <b>(-20.60%)</b></td><td>36.13 <b>(+78.66%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>218.80 (n/a)</td><td>190.66 (n/a)</td><td>193.20 (n/a)</td><td>167.00 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (+15.87%)</td><td>0.10 (+11.78%)</td><td>0.09 (+7.88%)</td><td>0.08 (+13.87%)</td><td>0.02 <b>(+31.42%)</b></td><td>210.70 (-12.17%)</td><td>174.86 (-9.74%)</td><td>174.50 (-7.33%)</td><td>126.50 (-13.65%)</td><td>34.92 (+2.15%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>193.72 (n/a)</td><td>188.30 (n/a)</td><td>146.50 (n/a)</td><td>34.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (+15.03%)</td><td>0.09 (+12.66%)</td><td>0.09 (+9.34%)</td><td>0.07 (+8.69%)</td><td>0.02 <b>(+42.33%)</b></td><td>230.70 (-7.98%)</td><td>185.32 (-10.29%)</td><td>187.40 (-8.54%)</td><td>144.60 (-13.05%)</td><td>34.28 (+13.29%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.70 (n/a)</td><td>206.58 (n/a)</td><td>204.90 (n/a)</td><td>166.30 (n/a)</td><td>30.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (-10.35%)</td><td>0.08 (-8.49%)</td><td>0.08 (-5.10%)</td><td>0.07 (-10.73%)</td><td>0.01 (-7.30%)</td><td>243.70 (+12.05%)</td><td>205.34 (+9.39%)</td><td>194.50 (+5.36%)</td><td>176.80 (+11.55%)</td><td>29.13 (+15.29%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>187.72 (n/a)</td><td>184.60 (n/a)</td><td>158.50 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (+19.42%)</td><td>0.09 (-2.10%)</td><td>0.08 (-19.13%)</td><td>0.06 (-6.99%)</td><td>0.02 <b>(+47.03%)</b></td><td>257.20 (+7.53%)</td><td>193.02 (+4.90%)</td><td>206.60 <b>(+23.64%)</b></td><td>128.80 (-16.31%)</td><td>49.31 <b>(+32.46%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.20 (n/a)</td><td>184.00 (n/a)</td><td>167.10 (n/a)</td><td>153.90 (n/a)</td><td>37.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (-11.71%)</td><td>0.09 (+6.94%)</td><td>0.09 (+4.38%)</td><td>0.08 <b>(+37.32%)</b></td><td>0.01 <b>(-62.98%)</b></td><td>205.50 <b>(-27.18%)</b></td><td>183.62 (-10.68%)</td><td>178.20 (-4.19%)</td><td>164.60 (+13.28%)</td><td>16.09 <b>(-69.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>282.20 (n/a)</td><td>205.58 (n/a)</td><td>186.00 (n/a)</td><td>145.30 (n/a)</td><td>53.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (+4.32%)</td><td>0.20 (-0.78%)</td><td>0.19 (-2.70%)</td><td>0.15 (-8.43%)</td><td>0.05 <b>(+22.55%)</b></td><td>212.60 (+9.19%)</td><td>169.00 (+2.56%)</td><td>175.60 (+2.75%)</td><td>111.30 (-4.13%)</td><td>38.18 <b>(+29.63%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.70 (n/a)</td><td>164.78 (n/a)</td><td>170.90 (n/a)</td><td>116.10 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 <b>(+38.93%)</b></td><td>0.20 (+8.96%)</td><td>0.18 (-0.41%)</td><td>0.17 (+13.97%)</td><td>0.05 <b>(+118.61%)</b></td><td>188.20 (-12.26%)</td><td>167.64 (-5.67%)</td><td>180.70 (+0.39%)</td><td>109.70 <b>(-28.02%)</b></td><td>32.79 <b>(+35.11%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.50 (n/a)</td><td>177.72 (n/a)</td><td>180.00 (n/a)</td><td>152.40 (n/a)</td><td>24.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (+5.06%)</td><td>0.16 <b>(+38.45%)</b></td><td>0.17 <b>(+72.63%)</b></td><td>0.13 <b>(+34.66%)</b></td><td>0.03 <b>(-27.44%)</b></td><td>255.80 <b>(-25.73%)</b></td><td>207.94 <b>(-30.41%)</b></td><td>195.40 <b>(-42.07%)</b></td><td>171.50 (-4.78%)</td><td>36.29 <b>(-47.87%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>344.40 (n/a)</td><td>298.80 (n/a)</td><td>337.30 (n/a)</td><td>180.10 (n/a)</td><td>69.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 <b>(+24.63%)</b></td><td>0.18 (+6.92%)</td><td>0.17 (+2.55%)</td><td>0.14 (-6.52%)</td><td>0.04 <b>(+96.74%)</b></td><td>234.60 (+6.98%)</td><td>189.68 (-4.53%)</td><td>197.20 (-2.47%)</td><td>137.60 (-19.77%)</td><td>35.14 <b>(+62.06%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.30 (n/a)</td><td>198.68 (n/a)</td><td>202.20 (n/a)</td><td>171.50 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 <b>(+37.88%)</b></td><td>0.21 <b>(+22.95%)</b></td><td>0.20 (+12.45%)</td><td>0.16 (+8.94%)</td><td>0.06 <b>(+118.75%)</b></td><td>206.20 (-8.19%)</td><td>162.38 (-15.72%)</td><td>162.50 (-11.06%)</td><td>114.10 <b>(-27.46%)</b></td><td>40.35 <b>(+45.68%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>224.60 (n/a)</td><td>192.66 (n/a)</td><td>182.70 (n/a)</td><td>157.30 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (+10.84%)</td><td>0.19 (-2.75%)</td><td>0.21 (+14.46%)</td><td>0.09 <b>(-49.91%)</b></td><td>0.07 <b>(+163.52%)</b></td><td>371.00 <b>(+99.57%)</b></td><td>201.56 (+17.76%)</td><td>154.10 (-12.59%)</td><td>123.40 (-9.80%)</td><td>99.97 <b>(+406.76%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>185.90 (n/a)</td><td>171.16 (n/a)</td><td>176.30 (n/a)</td><td>136.80 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 <b>(+47.25%)</b></td><td>0.21 <b>(+39.74%)</b></td><td>0.21 <b>(+39.21%)</b></td><td>0.15 <b>(+58.31%)</b></td><td>0.05 <b>(+25.68%)</b></td><td>216.90 <b>(-36.84%)</b></td><td>161.52 <b>(-29.96%)</b></td><td>155.80 <b>(-28.20%)</b></td><td>112.70 <b>(-32.07%)</b></td><td>37.94 <b>(-46.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>343.40 (n/a)</td><td>230.62 (n/a)</td><td>217.00 (n/a)</td><td>165.90 (n/a)</td><td>70.83 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (-8.67%)</td><td>0.21 (+17.26%)</td><td>0.21 (+16.38%)</td><td>0.18 <b>(+111.47%)</b></td><td>0.03 <b>(-60.84%)</b></td><td>178.60 <b>(-52.71%)</b></td><td>155.26 <b>(-26.48%)</b></td><td>159.50 (-14.11%)</td><td>124.50 (+9.50%)</td><td>19.70 <b>(-80.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>377.70 (n/a)</td><td>211.18 (n/a)</td><td>185.70 (n/a)</td><td>113.70 (n/a)</td><td>102.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (+0.55%)</td><td>0.18 (+8.31%)</td><td>0.18 (+14.50%)</td><td>0.15 <b>(+24.83%)</b></td><td>0.02 <b>(-44.18%)</b></td><td>216.90 (-19.90%)</td><td>184.84 (-10.77%)</td><td>178.70 (-12.66%)</td><td>157.60 (-0.51%)</td><td>23.03 <b>(-53.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>270.80 (n/a)</td><td>207.16 (n/a)</td><td>204.60 (n/a)</td><td>158.40 (n/a)</td><td>49.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (-6.35%)</td><td>0.19 (-1.97%)</td><td>0.16 (-19.48%)</td><td>0.15 (+7.40%)</td><td>0.05 (+15.46%)</td><td>222.20 (-6.91%)</td><td>182.12 (+3.58%)</td><td>210.70 <b>(+24.16%)</b></td><td>130.50 (+6.79%)</td><td>47.16 (+12.78%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>238.70 (n/a)</td><td>175.82 (n/a)</td><td>169.70 (n/a)</td><td>122.20 (n/a)</td><td>41.82 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.20 (-0.95%)</td><td>0.17 (+1.98%)</td><td>0.16 (-2.06%)</td><td>0.15 (+16.27%)</td><td>0.02 <b>(-20.64%)</b></td><td>212.40 (-14.01%)</td><td>190.62 (-2.90%)</td><td>202.50 (+2.07%)</td><td>165.70 (+0.98%)</td><td>22.80 <b>(-31.51%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>247.00 (n/a)</td><td>196.32 (n/a)</td><td>198.40 (n/a)</td><td>164.10 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (-13.86%)</td><td>0.17 (+10.56%)</td><td>0.17 (-8.25%)</td><td>0.17 <b>(+76.27%)</b></td><td>0.01 <b>(-86.52%)</b></td><td>197.90 <b>(-43.26%)</b></td><td>187.90 <b>(-20.85%)</b></td><td>191.50 (+8.99%)</td><td>178.90 (+16.09%)</td><td>8.50 <b>(-91.58%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>348.80 (n/a)</td><td>237.40 (n/a)</td><td>175.70 (n/a)</td><td>154.10 (n/a)</td><td>100.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 <b>(-23.63%)</b></td><td>0.15 (-12.91%)</td><td>0.16 (-11.07%)</td><td>0.13 (+1.17%)</td><td>0.02 <b>(-51.63%)</b></td><td>261.70 (-1.17%)</td><td>215.14 (+12.05%)</td><td>206.50 (+12.41%)</td><td>194.80 <b>(+30.91%)</b></td><td>26.60 <b>(-38.47%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>264.80 (n/a)</td><td>192.00 (n/a)</td><td>183.70 (n/a)</td><td>148.80 (n/a)</td><td>43.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 (+10.28%)</td><td>0.20 <b>(+29.21%)</b></td><td>0.18 <b>(+26.41%)</b></td><td>0.16 <b>(+80.12%)</b></td><td>0.05 <b>(-24.27%)</b></td><td>203.90 <b>(-44.47%)</b></td><td>167.98 <b>(-28.56%)</b></td><td>177.50 <b>(-20.90%)</b></td><td>116.90 (-9.38%)</td><td>32.78 <b>(-62.62%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>367.20 (n/a)</td><td>235.12 (n/a)</td><td>224.40 (n/a)</td><td>129.00 (n/a)</td><td>87.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (-13.45%)</td><td>0.17 (+0.38%)</td><td>0.18 (+7.31%)</td><td>0.14 (+4.08%)</td><td>0.02 <b>(-44.11%)</b></td><td>226.50 (-3.90%)</td><td>193.36 (-1.61%)</td><td>186.50 (-6.80%)</td><td>177.40 (+15.57%)</td><td>19.28 <b>(-35.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.70 (n/a)</td><td>196.52 (n/a)</td><td>200.10 (n/a)</td><td>153.50 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (+1.34%)</td><td>0.19 (+6.95%)</td><td>0.17 (-5.53%)</td><td>0.16 <b>(+20.54%)</b></td><td>0.03 (-14.03%)</td><td>207.60 (-17.03%)</td><td>179.20 (-7.58%)</td><td>188.60 (+5.84%)</td><td>150.10 (-1.31%)</td><td>25.73 <b>(-31.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>250.20 (n/a)</td><td>193.90 (n/a)</td><td>178.20 (n/a)</td><td>152.10 (n/a)</td><td>37.82 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-0.13%)</td><td>0.21 (-0.15%)</td><td>0.21 (-0.17%)</td><td>0.20 (-0.13%)</td><td>0.00 (+4.71%)</td><td>40958.10 (+0.14%)</td><td>40915.30 (+0.15%)</td><td>40918.30 (+0.17%)</td><td>40860.30 (+0.13%)</td><td>38.74 (+5.11%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40902.80 (n/a)</td><td>40854.42 (n/a)</td><td>40850.10 (n/a)</td><td>40806.80 (n/a)</td><td>36.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-0.56%)</td><td>0.21 (-0.08%)</td><td>0.21 (+0.05%)</td><td>0.21 (+0.03%)</td><td>0.00 <b>(-68.21%)</b></td><td>40883.90 (-0.03%)</td><td>40838.70 (+0.08%)</td><td>40856.30 (-0.05%)</td><td>40779.70 (+0.56%)</td><td>46.63 <b>(-68.05%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40896.60 (n/a)</td><td>40806.44 (n/a)</td><td>40877.50 (n/a)</td><td>40552.10 (n/a)</td><td>145.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+0.05%)</td><td>0.13 (+0.03%)</td><td>0.13 (+0.08%)</td><td>0.13 (-0.06%)</td><td>0.00 <b>(+105.19%)</b></td><td>322554.50 (+0.06%)</td><td>322126.10 (-0.03%)</td><td>321997.90 (-0.08%)</td><td>321880.20 (-0.05%)</td><td>284.43 <b>(+105.20%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>322375.00 (n/a)</td><td>322208.68 (n/a)</td><td>322255.30 (n/a)</td><td>322049.60 (n/a)</td><td>138.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+14.49%)</td><td>0.03 (+11.27%)</td><td>0.03 (+10.89%)</td><td>0.02 (+16.34%)</td><td>0.00 (+0.76%)</td><td>170.00 (-14.01%)</td><td>155.78 (-10.33%)</td><td>160.80 (-9.81%)</td><td>133.10 (-12.61%)</td><td>14.49 <b>(-23.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.70 (n/a)</td><td>173.72 (n/a)</td><td>178.30 (n/a)</td><td>152.30 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (+7.08%)</td><td>0.04 (+18.55%)</td><td>0.04 <b>(+23.41%)</b></td><td>0.03 <b>(+60.61%)</b></td><td>0.01 <b>(-29.90%)</b></td><td>216.20 <b>(-37.73%)</b></td><td>160.04 <b>(-21.74%)</b></td><td>154.00 (-18.95%)</td><td>128.70 (-6.60%)</td><td>34.54 <b>(-59.14%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>347.20 (n/a)</td><td>204.50 (n/a)</td><td>190.00 (n/a)</td><td>137.80 (n/a)</td><td>84.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+3.40%)</td><td>0.02 (+8.11%)</td><td>0.02 (+5.15%)</td><td>0.02 (+7.19%)</td><td>0.00 (-17.83%)</td><td>196.50 (-6.70%)</td><td>170.32 (-7.95%)</td><td>169.20 (-4.89%)</td><td>148.90 (-3.25%)</td><td>17.01 <b>(-26.23%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>185.02 (n/a)</td><td>177.90 (n/a)</td><td>153.90 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-10.44%)</td><td>0.03 (-3.44%)</td><td>0.03 (-7.10%)</td><td>0.03 (+5.55%)</td><td>0.00 <b>(-45.49%)</b></td><td>197.90 (-5.27%)</td><td>185.70 (+2.39%)</td><td>193.90 (+7.66%)</td><td>166.10 (+11.63%)</td><td>14.75 <b>(-42.78%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.90 (n/a)</td><td>181.36 (n/a)</td><td>180.10 (n/a)</td><td>148.80 (n/a)</td><td>25.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-12.89%)</td><td>0.02 (-8.64%)</td><td>0.02 (-11.92%)</td><td>0.02 (-4.61%)</td><td>0.00 <b>(-34.74%)</b></td><td>191.90 (+4.86%)</td><td>174.30 (+8.77%)</td><td>178.90 (+13.52%)</td><td>150.50 (+14.80%)</td><td>15.40 <b>(-21.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.00 (n/a)</td><td>160.24 (n/a)</td><td>157.60 (n/a)</td><td>131.10 (n/a)</td><td>19.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (+10.81%)</td><td>0.03 (+9.41%)</td><td>0.03 (+1.83%)</td><td>0.02 <b>(+29.51%)</b></td><td>0.01 (-6.87%)</td><td>254.10 <b>(-22.77%)</b></td><td>182.92 (-11.15%)</td><td>171.60 (-1.83%)</td><td>145.30 (-9.75%)</td><td>44.28 <b>(-37.04%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>329.00 (n/a)</td><td>205.88 (n/a)</td><td>174.80 (n/a)</td><td>161.00 (n/a)</td><td>70.34 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-2.72%)</td><td>0.03 (-3.22%)</td><td>0.02 (-7.23%)</td><td>0.02 (-1.03%)</td><td>0.01 (+8.69%)</td><td>224.50 (+1.04%)</td><td>171.66 (+4.10%)</td><td>181.50 (+7.78%)</td><td>128.30 (+2.80%)</td><td>41.17 (+8.54%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>164.90 (n/a)</td><td>168.40 (n/a)</td><td>124.80 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+0.62%)</td><td>0.02 (+2.27%)</td><td>0.02 (-2.01%)</td><td>0.02 (+14.93%)</td><td>0.00 <b>(-42.88%)</b></td><td>208.20 (-13.00%)</td><td>195.46 (-2.87%)</td><td>196.30 (+2.03%)</td><td>182.30 (-0.65%)</td><td>10.98 <b>(-51.20%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.30 (n/a)</td><td>201.24 (n/a)</td><td>192.40 (n/a)</td><td>183.50 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+7.88%)</td><td>0.02 (+3.93%)</td><td>0.02 (+0.16%)</td><td>0.02 (+11.43%)</td><td>0.00 (+2.99%)</td><td>195.60 (-10.23%)</td><td>174.92 (-4.08%)</td><td>177.70 (-0.17%)</td><td>133.20 (-7.31%)</td><td>24.72 (-16.74%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.90 (n/a)</td><td>182.36 (n/a)</td><td>178.00 (n/a)</td><td>143.70 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (-1.79%)</td><td>0.02 (-4.04%)</td><td>0.02 (-10.64%)</td><td>0.02 (-10.27%)</td><td>0.00 <b>(+45.88%)</b></td><td>239.20 (+11.41%)</td><td>200.18 (+5.90%)</td><td>218.90 (+11.91%)</td><td>159.70 (+1.85%)</td><td>36.29 <b>(+62.08%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.70 (n/a)</td><td>189.02 (n/a)</td><td>195.60 (n/a)</td><td>156.80 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+11.69%)</td><td>0.02 <b>(+20.13%)</b></td><td>0.03 <b>(+26.01%)</b></td><td>0.02 <b>(+43.43%)</b></td><td>0.00 <b>(-21.88%)</b></td><td>221.70 <b>(-30.28%)</b></td><td>176.20 (-19.30%)</td><td>163.10 <b>(-20.63%)</b></td><td>150.40 (-10.48%)</td><td>29.07 <b>(-51.57%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>318.00 (n/a)</td><td>218.34 (n/a)</td><td>205.50 (n/a)</td><td>168.00 (n/a)</td><td>60.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 <b>(+27.29%)</b></td><td>0.02 <b>(+20.63%)</b></td><td>0.02 (+10.93%)</td><td>0.02 (+8.90%)</td><td>0.00 <b>(+146.93%)</b></td><td>213.60 (-8.21%)</td><td>179.96 (-15.79%)</td><td>191.00 (-9.86%)</td><td>150.00 <b>(-21.42%)</b></td><td>28.48 <b>(+70.83%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>213.70 (n/a)</td><td>211.90 (n/a)</td><td>190.90 (n/a)</td><td>16.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (+18.04%)</td><td>0.02 (+8.49%)</td><td>0.02 (+12.09%)</td><td>0.02 (+1.80%)</td><td>0.00 <b>(+58.34%)</b></td><td>201.20 (-1.76%)</td><td>170.40 (-6.66%)</td><td>168.90 (-10.78%)</td><td>129.80 (-15.27%)</td><td>28.36 <b>(+32.12%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.80 (n/a)</td><td>182.56 (n/a)</td><td>189.30 (n/a)</td><td>153.20 (n/a)</td><td>21.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 <b>(+26.65%)</b></td><td>0.02 (+0.01%)</td><td>0.02 (-2.49%)</td><td>0.01 <b>(-24.41%)</b></td><td>0.00 <b>(+382.98%)</b></td><td>300.50 <b>(+32.32%)</b></td><td>222.82 (+4.38%)</td><td>216.40 (+2.56%)</td><td>157.40 <b>(-21.06%)</b></td><td>52.85 <b>(+404.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.10 (n/a)</td><td>213.46 (n/a)</td><td>211.00 (n/a)</td><td>199.40 (n/a)</td><td>10.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (-10.50%)</td><td>0.02 (+7.34%)</td><td>0.02 <b>(+30.98%)</b></td><td>0.02 <b>(+22.96%)</b></td><td>0.00 <b>(-50.67%)</b></td><td>222.20 (-18.67%)</td><td>193.12 (-10.70%)</td><td>179.30 <b>(-23.64%)</b></td><td>168.50 (+11.74%)</td><td>24.93 <b>(-53.93%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>273.20 (n/a)</td><td>216.26 (n/a)</td><td>234.80 (n/a)</td><td>150.80 (n/a)</td><td>54.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (+1.77%)</td><td>0.05 (+0.79%)</td><td>0.04 (-4.10%)</td><td>0.04 (+3.97%)</td><td>0.01 (+11.85%)</td><td>198.50 (-3.83%)</td><td>176.62 (-0.51%)</td><td>185.60 (+4.27%)</td><td>142.40 (-1.79%)</td><td>24.64 (+8.11%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>177.52 (n/a)</td><td>178.00 (n/a)</td><td>145.00 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (+10.65%)</td><td>0.07 (+4.48%)</td><td>0.07 (+0.78%)</td><td>0.06 (-0.70%)</td><td>0.01 <b>(+65.89%)</b></td><td>208.80 (+0.72%)</td><td>179.02 (-2.96%)</td><td>181.20 (-0.77%)</td><td>146.10 (-9.59%)</td><td>29.81 <b>(+51.03%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>184.48 (n/a)</td><td>182.60 (n/a)</td><td>161.60 (n/a)</td><td>19.74 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 <b>(+25.02%)</b></td><td>0.04 (+4.79%)</td><td>0.05 (+7.20%)</td><td>0.03 <b>(-28.82%)</b></td><td>0.01 <b>(+252.47%)</b></td><td>314.80 <b>(+40.47%)</b></td><td>198.98 (+1.80%)</td><td>176.40 (-6.72%)</td><td>147.00 <b>(-20.02%)</b></td><td>66.95 <b>(+310.31%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.10 (n/a)</td><td>195.46 (n/a)</td><td>189.10 (n/a)</td><td>183.80 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 <b>(+37.45%)</b></td><td>0.06 (+14.24%)</td><td>0.07 <b>(+26.58%)</b></td><td>0.04 (-10.37%)</td><td>0.01 <b>(+252.66%)</b></td><td>234.30 (+11.57%)</td><td>177.56 (-8.33%)</td><td>157.10 <b>(-21.02%)</b></td><td>128.30 <b>(-27.27%)</b></td><td>45.39 <b>(+197.93%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>193.70 (n/a)</td><td>198.90 (n/a)</td><td>176.40 (n/a)</td><td>15.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 <b>(+20.37%)</b></td><td>0.05 (+4.18%)</td><td>0.04 (-4.01%)</td><td>0.03 (-16.84%)</td><td>0.01 <b>(+234.31%)</b></td><td>239.70 <b>(+20.27%)</b></td><td>179.06 (+0.58%)</td><td>182.60 (+4.16%)</td><td>133.30 (-16.90%)</td><td>45.36 <b>(+217.92%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.30 (n/a)</td><td>178.02 (n/a)</td><td>175.30 (n/a)</td><td>160.40 (n/a)</td><td>14.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 <b>(+36.75%)</b></td><td>0.05 (+4.00%)</td><td>0.05 (-1.26%)</td><td>0.03 <b>(-30.77%)</b></td><td>0.02 <b>(+170.58%)</b></td><td>362.50 <b>(+44.42%)</b></td><td>222.86 (+5.98%)</td><td>204.00 (+1.24%)</td><td>127.30 <b>(-26.88%)</b></td><td>87.09 <b>(+188.24%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>251.00 (n/a)</td><td>210.28 (n/a)</td><td>201.50 (n/a)</td><td>174.10 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (+14.02%)</td><td>0.04 (+9.73%)</td><td>0.04 (+13.82%)</td><td>0.04 (+9.17%)</td><td>0.01 (-0.54%)</td><td>224.60 (-8.40%)</td><td>189.20 (-9.27%)</td><td>192.80 (-12.12%)</td><td>150.40 (-12.30%)</td><td>26.57 (-19.76%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.20 (n/a)</td><td>208.52 (n/a)</td><td>219.40 (n/a)</td><td>171.50 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (-7.27%)</td><td>0.05 (-3.87%)</td><td>0.04 (-3.56%)</td><td>0.04 (-9.79%)</td><td>0.01 (+16.39%)</td><td>239.70 (+10.87%)</td><td>205.74 (+4.79%)</td><td>206.60 (+3.66%)</td><td>172.30 (+7.82%)</td><td>31.65 <b>(+39.43%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>196.34 (n/a)</td><td>199.30 (n/a)</td><td>159.80 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (+13.70%)</td><td>0.04 (+6.82%)</td><td>0.04 (+0.98%)</td><td>0.04 <b>(+21.39%)</b></td><td>0.01 (+7.65%)</td><td>208.30 (-17.60%)</td><td>190.98 (-6.75%)</td><td>200.30 (-0.94%)</td><td>144.10 (-12.08%)</td><td>26.51 <b>(-23.52%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>204.80 (n/a)</td><td>202.20 (n/a)</td><td>163.90 (n/a)</td><td>34.66 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 <b>(+27.06%)</b></td><td>0.05 (+14.42%)</td><td>0.05 <b>(+20.95%)</b></td><td>0.04 (-5.71%)</td><td>0.01 <b>(+287.95%)</b></td><td>231.40 (+6.05%)</td><td>186.26 (-10.18%)</td><td>173.30 (-17.28%)</td><td>151.00 <b>(-21.31%)</b></td><td>36.49 <b>(+224.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.20 (n/a)</td><td>207.36 (n/a)</td><td>209.50 (n/a)</td><td>191.90 (n/a)</td><td>11.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 <b>(+23.87%)</b></td><td>0.04 (+7.88%)</td><td>0.04 (+4.12%)</td><td>0.03 (-0.95%)</td><td>0.01 <b>(+92.32%)</b></td><td>251.30 (+0.92%)</td><td>194.92 (-5.17%)</td><td>193.70 (-3.97%)</td><td>144.00 (-19.28%)</td><td>40.49 <b>(+52.90%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>249.00 (n/a)</td><td>205.54 (n/a)</td><td>201.70 (n/a)</td><td>178.40 (n/a)</td><td>26.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 <b>(+26.99%)</b></td><td>0.04 (+13.01%)</td><td>0.04 (+14.91%)</td><td>0.03 <b>(+23.04%)</b></td><td>0.01 <b>(+29.16%)</b></td><td>316.70 (-18.73%)</td><td>225.78 (-11.26%)</td><td>195.70 (-12.98%)</td><td>159.70 <b>(-21.25%)</b></td><td>63.50 (-18.07%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>389.70 (n/a)</td><td>254.44 (n/a)</td><td>224.90 (n/a)</td><td>202.80 (n/a)</td><td>77.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (+16.31%)</td><td>0.04 (+9.17%)</td><td>0.04 (+11.92%)</td><td>0.03 (+6.82%)</td><td>0.01 <b>(+36.05%)</b></td><td>247.30 (-6.36%)</td><td>192.36 (-6.96%)</td><td>184.50 (-10.65%)</td><td>131.30 (-14.01%)</td><td>44.87 (+10.29%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.10 (n/a)</td><td>206.76 (n/a)</td><td>206.50 (n/a)</td><td>152.70 (n/a)</td><td>40.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 <b>(+34.44%)</b></td><td>0.04 (+0.17%)</td><td>0.04 (-6.12%)</td><td>0.03 (-14.82%)</td><td>0.01 <b>(+1446.72%)</b></td><td>266.80 (+17.43%)</td><td>229.64 (+2.94%)</td><td>237.80 (+6.54%)</td><td>162.60 <b>(-25.62%)</b></td><td>40.82 <b>(+1223.13%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>227.20 (n/a)</td><td>223.08 (n/a)</td><td>223.20 (n/a)</td><td>218.60 (n/a)</td><td>3.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (+8.47%)</td><td>0.03 (-8.19%)</td><td>0.03 (-9.87%)</td><td>0.02 (-18.98%)</td><td>0.01 <b>(+55.31%)</b></td><td>354.70 <b>(+23.42%)</b></td><td>258.66 (+11.75%)</td><td>254.70 (+10.93%)</td><td>189.10 (-7.80%)</td><td>60.35 <b>(+79.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>287.40 (n/a)</td><td>231.46 (n/a)</td><td>229.60 (n/a)</td><td>205.10 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (+13.16%)</td><td>0.10 (+14.88%)</td><td>0.11 (+19.26%)</td><td>0.08 (+18.12%)</td><td>0.02 <b>(+25.47%)</b></td><td>197.70 (-15.33%)</td><td>166.58 (-12.65%)</td><td>155.70 (-16.16%)</td><td>141.10 (-11.65%)</td><td>27.61 (-5.17%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>190.70 (n/a)</td><td>185.70 (n/a)</td><td>159.70 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 <b>(+25.50%)</b></td><td>0.16 <b>(+26.55%)</b></td><td>0.17 <b>(+42.23%)</b></td><td>0.13 (+4.35%)</td><td>0.03 <b>(+134.55%)</b></td><td>196.60 (-4.14%)</td><td>157.48 (-19.03%)</td><td>142.60 <b>(-29.72%)</b></td><td>129.80 <b>(-20.32%)</b></td><td>32.29 <b>(+80.34%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>194.50 (n/a)</td><td>202.90 (n/a)</td><td>162.90 (n/a)</td><td>17.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 <b>(-24.50%)</b></td><td>0.09 (-1.49%)</td><td>0.09 (+3.98%)</td><td>0.08 (+17.78%)</td><td>0.01 <b>(-76.47%)</b></td><td>195.30 (-15.09%)</td><td>183.18 (-2.51%)</td><td>183.90 (-3.82%)</td><td>166.40 <b>(+32.48%)</b></td><td>10.76 <b>(-72.93%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.00 (n/a)</td><td>187.90 (n/a)</td><td>191.20 (n/a)</td><td>125.60 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 <b>(+25.74%)</b></td><td>0.12 (+4.28%)</td><td>0.11 (-7.39%)</td><td>0.09 (-6.71%)</td><td>0.02 <b>(+172.91%)</b></td><td>226.30 (+7.20%)</td><td>181.80 (-1.48%)</td><td>193.60 (+7.98%)</td><td>137.80 <b>(-20.48%)</b></td><td>35.66 <b>(+128.12%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>184.54 (n/a)</td><td>179.30 (n/a)</td><td>173.30 (n/a)</td><td>15.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 <b>(-27.98%)</b></td><td>0.08 (-15.58%)</td><td>0.08 (-7.17%)</td><td>0.05 <b>(-36.10%)</b></td><td>0.02 (-17.06%)</td><td>316.60 <b>(+56.50%)</b></td><td>215.04 <b>(+20.39%)</b></td><td>196.80 (+7.72%)</td><td>176.90 <b>(+38.85%)</b></td><td>57.67 <b>(+90.87%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.30 (n/a)</td><td>178.62 (n/a)</td><td>182.70 (n/a)</td><td>127.40 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (-7.03%)</td><td>0.10 (-16.18%)</td><td>0.10 (-17.73%)</td><td>0.08 <b>(-26.61%)</b></td><td>0.01 <b>(+99.18%)</b></td><td>269.60 <b>(+36.23%)</b></td><td>216.40 <b>(+20.91%)</b></td><td>210.90 <b>(+21.56%)</b></td><td>185.10 (+7.55%)</td><td>32.35 <b>(+196.56%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>178.98 (n/a)</td><td>173.50 (n/a)</td><td>172.10 (n/a)</td><td>10.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (+2.30%)</td><td>0.09 (+5.52%)</td><td>0.09 (+6.07%)</td><td>0.08 (+9.05%)</td><td>0.01 <b>(-34.47%)</b></td><td>201.10 (-8.30%)</td><td>186.80 (-5.69%)</td><td>182.50 (-5.73%)</td><td>175.30 (-2.29%)</td><td>11.40 <b>(-41.22%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>198.06 (n/a)</td><td>193.60 (n/a)</td><td>179.40 (n/a)</td><td>19.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (-3.01%)</td><td>0.10 (-5.42%)</td><td>0.10 (-11.68%)</td><td>0.09 (+11.72%)</td><td>0.01 <b>(-35.51%)</b></td><td>194.30 (-10.50%)</td><td>186.90 (+4.96%)</td><td>192.00 (+13.21%)</td><td>163.80 (+3.08%)</td><td>13.02 <b>(-42.42%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>178.06 (n/a)</td><td>169.60 (n/a)</td><td>158.90 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (-13.62%)</td><td>0.10 (-7.92%)</td><td>0.09 (-4.13%)</td><td>0.08 (-5.83%)</td><td>0.01 <b>(-36.03%)</b></td><td>196.50 (+6.16%)</td><td>173.14 (+7.38%)</td><td>174.10 (+4.31%)</td><td>142.60 (+15.75%)</td><td>19.43 <b>(-23.17%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.10 (n/a)</td><td>161.24 (n/a)</td><td>166.90 (n/a)</td><td>123.20 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (-18.46%)</td><td>0.08 (-15.71%)</td><td>0.09 (-8.94%)</td><td>0.06 <b>(-24.24%)</b></td><td>0.01 (-1.62%)</td><td>316.90 <b>(+31.99%)</b></td><td>229.14 (+19.96%)</td><td>204.90 (+9.81%)</td><td>201.30 <b>(+22.67%)</b></td><td>49.68 <b>(+61.59%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>240.10 (n/a)</td><td>191.02 (n/a)</td><td>186.60 (n/a)</td><td>164.10 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (+8.86%)</td><td>0.08 (+6.98%)</td><td>0.08 (+0.96%)</td><td>0.07 <b>(+60.93%)</b></td><td>0.01 <b>(-41.26%)</b></td><td>220.00 <b>(-37.87%)</b></td><td>198.20 (-11.28%)</td><td>199.10 (-0.95%)</td><td>161.70 (-8.13%)</td><td>24.04 <b>(-67.55%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>354.10 (n/a)</td><td>223.40 (n/a)</td><td>201.00 (n/a)</td><td>176.00 (n/a)</td><td>74.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (-0.30%)</td><td>0.08 (-3.27%)</td><td>0.08 (-2.08%)</td><td>0.05 <b>(-20.34%)</b></td><td>0.02 <b>(+28.36%)</b></td><td>330.00 <b>(+25.57%)</b></td><td>233.90 (+5.84%)</td><td>218.20 (+2.11%)</td><td>172.70 (+0.29%)</td><td>59.10 <b>(+65.95%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>262.80 (n/a)</td><td>221.00 (n/a)</td><td>213.70 (n/a)</td><td>172.20 (n/a)</td><td>35.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (+8.96%)</td><td>0.09 (+1.82%)</td><td>0.09 (-0.33%)</td><td>0.07 (-2.51%)</td><td>0.01 <b>(+56.87%)</b></td><td>221.20 (+2.60%)</td><td>188.50 (-0.62%)</td><td>180.60 (+0.33%)</td><td>156.10 (-8.18%)</td><td>30.15 <b>(+50.34%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>189.68 (n/a)</td><td>180.00 (n/a)</td><td>170.00 (n/a)</td><td>20.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 <b>(+36.65%)</b></td><td>0.09 (+12.22%)</td><td>0.09 (+13.46%)</td><td>0.06 (-15.53%)</td><td>0.02 <b>(+267.34%)</b></td><td>293.00 (+18.38%)</td><td>207.40 (-6.90%)</td><td>194.30 (-11.88%)</td><td>148.10 <b>(-26.83%)</b></td><td>53.17 <b>(+224.12%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>247.50 (n/a)</td><td>222.76 (n/a)</td><td>220.50 (n/a)</td><td>202.40 (n/a)</td><td>16.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 <b>(-29.94%)</b></td><td>0.08 (-2.20%)</td><td>0.08 (+2.94%)</td><td>0.07 <b>(+52.26%)</b></td><td>0.01 <b>(-77.47%)</b></td><td>236.40 <b>(-34.32%)</b></td><td>207.78 (-7.38%)</td><td>207.30 (-2.86%)</td><td>193.30 <b>(+42.76%)</b></td><td>17.58 <b>(-79.28%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>359.90 (n/a)</td><td>224.34 (n/a)</td><td>213.40 (n/a)</td><td>135.40 (n/a)</td><td>84.85 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (-2.13%)</td><td>0.17 (+6.45%)</td><td>0.17 (+7.17%)</td><td>0.14 (+9.65%)</td><td>0.02 <b>(-38.89%)</b></td><td>236.90 (-8.81%)</td><td>198.88 (-7.61%)</td><td>194.50 (-6.67%)</td><td>180.10 (+2.21%)</td><td>22.41 <b>(-42.28%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>259.80 (n/a)</td><td>215.26 (n/a)</td><td>208.40 (n/a)</td><td>176.20 (n/a)</td><td>38.82 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (-4.25%)</td><td>0.20 (+0.45%)</td><td>0.19 (+0.53%)</td><td>0.17 (-4.11%)</td><td>0.02 (-4.60%)</td><td>191.40 (+4.25%)</td><td>168.44 (-0.46%)</td><td>172.20 (-0.52%)</td><td>149.80 (+4.39%)</td><td>16.46 (+4.38%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>183.60 (n/a)</td><td>169.22 (n/a)</td><td>173.10 (n/a)</td><td>143.50 (n/a)</td><td>15.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (-1.73%)</td><td>0.23 (+5.97%)</td><td>0.24 <b>(+24.88%)</b></td><td>0.19 (+5.47%)</td><td>0.03 (-9.97%)</td><td>216.10 (-5.22%)</td><td>183.18 (-6.06%)</td><td>169.10 (-19.90%)</td><td>154.10 (+1.72%)</td><td>28.57 (-10.62%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>228.00 (n/a)</td><td>195.00 (n/a)</td><td>211.10 (n/a)</td><td>151.50 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (+4.76%)</td><td>0.18 (+0.39%)</td><td>0.17 (-4.09%)</td><td>0.16 (-0.17%)</td><td>0.02 <b>(+24.59%)</b></td><td>198.80 (+0.15%)</td><td>181.84 (+0.00%)</td><td>194.60 (+4.29%)</td><td>148.50 (-4.56%)</td><td>21.53 (+19.18%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>198.50 (n/a)</td><td>181.84 (n/a)</td><td>186.60 (n/a)</td><td>155.60 (n/a)</td><td>18.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (+3.08%)</td><td>0.22 (-1.00%)</td><td>0.22 (-3.43%)</td><td>0.19 (-1.53%)</td><td>0.02 (-1.18%)</td><td>210.70 (+1.54%)</td><td>189.60 (+0.99%)</td><td>189.70 (+3.55%)</td><td>166.50 (-2.97%)</td><td>15.75 (-3.71%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>207.50 (n/a)</td><td>187.74 (n/a)</td><td>183.20 (n/a)</td><td>171.60 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 <b>(+30.42%)</b></td><td>0.20 <b>(+20.49%)</b></td><td>0.19 (+13.63%)</td><td>0.17 (+14.32%)</td><td>0.04 <b>(+121.44%)</b></td><td>194.30 (-12.52%)</td><td>165.46 (-15.55%)</td><td>175.10 (-12.01%)</td><td>130.40 <b>(-23.29%)</b></td><td>28.26 <b>(+48.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>222.10 (n/a)</td><td>195.92 (n/a)</td><td>199.00 (n/a)</td><td>170.00 (n/a)</td><td>19.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (+4.27%)</td><td>0.21 (+1.41%)</td><td>0.20 (+4.25%)</td><td>0.16 (-8.76%)</td><td>0.05 <b>(+52.95%)</b></td><td>226.00 (+9.60%)</td><td>185.32 (+0.81%)</td><td>188.30 (-4.08%)</td><td>143.80 (-4.13%)</td><td>39.64 <b>(+58.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>206.20 (n/a)</td><td>183.84 (n/a)</td><td>196.30 (n/a)</td><td>150.00 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 <b>(+37.20%)</b></td><td>0.18 (+3.61%)</td><td>0.17 (-4.04%)</td><td>0.12 <b>(-28.49%)</b></td><td>0.05 <b>(+723.75%)</b></td><td>270.60 <b>(+39.84%)</b></td><td>192.38 (+3.54%)</td><td>195.20 (+4.22%)</td><td>128.50 <b>(-27.15%)</b></td><td>56.89 <b>(+728.43%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>185.80 (n/a)</td><td>187.30 (n/a)</td><td>176.40 (n/a)</td><td>6.87 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.32 <b>(+59.88%)</b></td><td>0.22 <b>(+35.84%)</b></td><td>0.20 <b>(+26.38%)</b></td><td>0.18 <b>(+40.29%)</b></td><td>0.06 <b>(+98.52%)</b></td><td>202.20 <b>(-28.73%)</b></td><td>170.88 <b>(-25.24%)</b></td><td>181.80 <b>(-20.85%)</b></td><td>114.90 <b>(-37.45%)</b></td><td>33.09 (-15.36%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>283.70 (n/a)</td><td>228.58 (n/a)</td><td>229.70 (n/a)</td><td>183.70 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (+8.07%)</td><td>0.17 (-12.00%)</td><td>0.17 (-13.21%)</td><td>0.13 <b>(-26.23%)</b></td><td>0.04 <b>(+97.52%)</b></td><td>260.30 <b>(+35.57%)</b></td><td>195.32 (+17.31%)</td><td>190.10 (+15.21%)</td><td>138.70 (-7.47%)</td><td>43.56 <b>(+148.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.00 (n/a)</td><td>166.50 (n/a)</td><td>165.00 (n/a)</td><td>149.90 (n/a)</td><td>17.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (-16.49%)</td><td>0.15 (-8.69%)</td><td>0.16 (-3.51%)</td><td>0.11 (+5.60%)</td><td>0.02 <b>(-39.87%)</b></td><td>309.70 (-5.29%)</td><td>232.78 (+5.94%)</td><td>217.10 (+3.63%)</td><td>197.80 (+19.73%)</td><td>44.79 <b>(-30.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>327.00 (n/a)</td><td>219.72 (n/a)</td><td>209.50 (n/a)</td><td>165.20 (n/a)</td><td>64.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (-3.34%)</td><td>0.17 (-6.05%)</td><td>0.17 (-3.61%)</td><td>0.15 (-6.96%)</td><td>0.02 (+0.38%)</td><td>221.40 (+7.48%)</td><td>199.24 (+6.53%)</td><td>194.10 (+3.74%)</td><td>172.90 (+3.41%)</td><td>20.12 (+12.84%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.00 (n/a)</td><td>187.02 (n/a)</td><td>187.10 (n/a)</td><td>167.20 (n/a)</td><td>17.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (-18.92%)</td><td>0.17 (-9.35%)</td><td>0.17 (-2.53%)</td><td>0.14 (-15.35%)</td><td>0.02 <b>(-34.58%)</b></td><td>249.00 (+18.12%)</td><td>209.52 (+9.60%)</td><td>204.90 (+2.55%)</td><td>179.00 <b>(+23.36%)</b></td><td>25.92 (-1.00%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>210.80 (n/a)</td><td>191.16 (n/a)</td><td>199.80 (n/a)</td><td>145.10 (n/a)</td><td>26.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (+0.13%)</td><td>0.15 (-6.38%)</td><td>0.14 (-6.95%)</td><td>0.13 (-12.08%)</td><td>0.02 <b>(+38.81%)</b></td><td>254.60 (+13.71%)</td><td>221.12 (+7.66%)</td><td>226.50 (+7.50%)</td><td>175.20 (-0.17%)</td><td>28.78 <b>(+55.39%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>223.90 (n/a)</td><td>205.38 (n/a)</td><td>210.70 (n/a)</td><td>175.50 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (+6.21%)</td><td>0.14 (+12.08%)</td><td>0.14 <b>(+22.26%)</b></td><td>0.11 (+19.80%)</td><td>0.03 (-18.07%)</td><td>181.50 (-16.51%)</td><td>151.18 (-12.88%)</td><td>151.70 (-18.22%)</td><td>113.80 (-5.87%)</td><td>26.80 <b>(-35.64%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>217.40 (n/a)</td><td>173.54 (n/a)</td><td>185.50 (n/a)</td><td>120.90 (n/a)</td><td>41.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 <b>(+22.03%)</b></td><td>0.13 <b>(+29.16%)</b></td><td>0.13 <b>(+25.57%)</b></td><td>0.11 <b>(+30.06%)</b></td><td>0.02 <b>(+35.75%)</b></td><td>188.00 <b>(-23.11%)</b></td><td>156.12 <b>(-22.27%)</b></td><td>160.70 <b>(-20.37%)</b></td><td>125.30 (-18.05%)</td><td>28.09 (-13.93%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>244.50 (n/a)</td><td>200.84 (n/a)</td><td>201.80 (n/a)</td><td>152.90 (n/a)</td><td>32.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (+5.52%)</td><td>0.12 (+7.78%)</td><td>0.13 (+8.91%)</td><td>0.10 <b>(+24.38%)</b></td><td>0.02 (-9.09%)</td><td>211.40 (-19.62%)</td><td>172.52 (-8.49%)</td><td>156.40 (-8.22%)</td><td>145.10 (-5.23%)</td><td>29.61 <b>(-32.40%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>263.00 (n/a)</td><td>188.52 (n/a)</td><td>170.40 (n/a)</td><td>153.10 (n/a)</td><td>43.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (+5.97%)</td><td>0.12 (+5.66%)</td><td>0.12 (+7.41%)</td><td>0.09 (-3.16%)</td><td>0.02 <b>(+26.08%)</b></td><td>220.20 (+3.23%)</td><td>172.30 (-4.64%)</td><td>165.00 (-6.88%)</td><td>141.80 (-5.59%)</td><td>28.92 <b>(+26.61%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>180.68 (n/a)</td><td>177.20 (n/a)</td><td>150.20 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (-10.88%)</td><td>0.12 (-4.47%)</td><td>0.12 (-8.81%)</td><td>0.11 (+12.69%)</td><td>0.01 <b>(-45.33%)</b></td><td>186.40 (-11.28%)</td><td>166.04 (+2.43%)</td><td>165.10 (+9.70%)</td><td>139.60 (+12.22%)</td><td>17.18 <b>(-47.02%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>210.10 (n/a)</td><td>162.10 (n/a)</td><td>150.50 (n/a)</td><td>124.40 (n/a)</td><td>32.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (-3.17%)</td><td>0.11 (-8.10%)</td><td>0.11 (-13.83%)</td><td>0.09 (-12.00%)</td><td>0.02 <b>(+27.94%)</b></td><td>227.00 (+13.61%)</td><td>189.16 (+10.13%)</td><td>193.90 (+16.04%)</td><td>152.50 (+3.32%)</td><td>33.45 <b>(+47.19%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>171.76 (n/a)</td><td>167.10 (n/a)</td><td>147.60 (n/a)</td><td>22.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (+10.84%)</td><td>0.12 (+14.99%)</td><td>0.12 (+18.22%)</td><td>0.10 (+9.71%)</td><td>0.02 (+8.77%)</td><td>207.40 (-8.84%)</td><td>168.56 (-13.02%)</td><td>169.00 (-15.42%)</td><td>131.60 (-9.74%)</td><td>27.46 (-7.88%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>227.50 (n/a)</td><td>193.80 (n/a)</td><td>199.80 (n/a)</td><td>145.80 (n/a)</td><td>29.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (-7.50%)</td><td>0.11 (+12.22%)</td><td>0.10 (+16.21%)</td><td>0.09 <b>(+32.35%)</b></td><td>0.02 <b>(-38.28%)</b></td><td>224.40 <b>(-24.44%)</b></td><td>193.46 (-15.07%)</td><td>202.60 (-13.93%)</td><td>158.70 (+8.11%)</td><td>31.50 <b>(-50.68%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>297.00 (n/a)</td><td>227.80 (n/a)</td><td>235.40 (n/a)</td><td>146.80 (n/a)</td><td>63.87 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 <b>(+28.31%)</b></td><td>0.16 (+19.96%)</td><td>0.16 <b>(+23.62%)</b></td><td>0.12 (+9.91%)</td><td>0.03 <b>(+140.66%)</b></td><td>199.80 (-9.02%)</td><td>162.46 (-14.58%)</td><td>149.80 (-19.11%)</td><td>130.80 <b>(-22.05%)</b></td><td>33.16 <b>(+72.55%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>190.20 (n/a)</td><td>185.20 (n/a)</td><td>167.80 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (-9.92%)</td><td>0.14 (-10.51%)</td><td>0.14 (-14.13%)</td><td>0.11 (-15.04%)</td><td>0.02 (-16.17%)</td><td>220.90 (+17.75%)</td><td>174.32 (+11.42%)</td><td>171.60 (+16.42%)</td><td>138.90 (+11.03%)</td><td>30.54 (+7.00%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>187.60 (n/a)</td><td>156.46 (n/a)</td><td>147.40 (n/a)</td><td>125.10 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (-15.67%)</td><td>0.14 (-14.75%)</td><td>0.13 (-9.73%)</td><td>0.11 <b>(-21.06%)</b></td><td>0.02 (-13.40%)</td><td>233.40 <b>(+26.64%)</b></td><td>185.04 (+17.59%)</td><td>186.60 (+10.74%)</td><td>150.40 (+18.52%)</td><td>34.04 <b>(+29.34%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>184.30 (n/a)</td><td>157.36 (n/a)</td><td>168.50 (n/a)</td><td>126.90 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (-1.35%)</td><td>0.15 (+2.69%)</td><td>0.15 (-5.99%)</td><td>0.12 (+14.22%)</td><td>0.02 <b>(-25.85%)</b></td><td>207.20 (-12.43%)</td><td>169.64 (-4.47%)</td><td>168.40 (+6.38%)</td><td>144.20 (+1.41%)</td><td>26.06 <b>(-35.13%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>236.60 (n/a)</td><td>177.58 (n/a)</td><td>158.30 (n/a)</td><td>142.20 (n/a)</td><td>40.18 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (+13.23%)</td><td>0.15 (+4.40%)</td><td>0.13 (-7.24%)</td><td>0.13 (+9.79%)</td><td>0.03 <b>(+26.65%)</b></td><td>192.10 (-8.91%)</td><td>168.74 (-3.72%)</td><td>184.80 (+7.82%)</td><td>129.30 (-11.74%)</td><td>26.90 (+2.64%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>175.26 (n/a)</td><td>171.40 (n/a)</td><td>146.50 (n/a)</td><td>26.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (-4.07%)</td><td>0.13 (+0.14%)</td><td>0.13 (+10.22%)</td><td>0.08 (-11.43%)</td><td>0.03 (-1.82%)</td><td>326.70 (+12.89%)</td><td>208.60 (+1.00%)</td><td>185.80 (-9.23%)</td><td>158.60 (+4.20%)</td><td>67.07 <b>(+24.41%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>289.40 (n/a)</td><td>206.54 (n/a)</td><td>204.70 (n/a)</td><td>152.20 (n/a)</td><td>53.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (-0.81%)</td><td>0.14 (+2.32%)</td><td>0.13 (-11.35%)</td><td>0.11 (+5.40%)</td><td>0.02 (-18.00%)</td><td>230.40 (-5.11%)</td><td>186.38 (-3.81%)</td><td>193.10 (+12.86%)</td><td>146.20 (+0.83%)</td><td>32.76 <b>(-25.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>242.80 (n/a)</td><td>193.76 (n/a)</td><td>171.10 (n/a)</td><td>145.00 (n/a)</td><td>44.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 <b>(-23.53%)</b></td><td>0.13 (-13.74%)</td><td>0.13 (-19.96%)</td><td>0.11 <b>(+40.52%)</b></td><td>0.01 <b>(-68.36%)</b></td><td>214.50 <b>(-28.83%)</b></td><td>192.02 (+6.84%)</td><td>189.20 <b>(+24.97%)</b></td><td>166.50 <b>(+30.79%)</b></td><td>19.61 <b>(-72.00%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>301.40 (n/a)</td><td>179.72 (n/a)</td><td>151.40 (n/a)</td><td>127.30 (n/a)</td><td>70.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (+9.24%)</td><td>0.10 (+4.48%)</td><td>0.11 (+13.89%)</td><td>0.08 (-10.92%)</td><td>0.02 <b>(+83.20%)</b></td><td>239.70 (+12.27%)</td><td>186.12 (-2.71%)</td><td>168.10 (-12.17%)</td><td>158.40 (-8.49%)</td><td>33.33 <b>(+91.61%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>191.30 (n/a)</td><td>191.40 (n/a)</td><td>173.10 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (+11.37%)</td><td>0.12 <b>(+24.16%)</b></td><td>0.12 <b>(+38.83%)</b></td><td>0.09 (+9.23%)</td><td>0.03 (+10.88%)</td><td>202.00 (-8.43%)</td><td>153.64 (-19.33%)</td><td>147.90 <b>(-27.99%)</b></td><td>115.40 (-10.19%)</td><td>34.33 (-4.80%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>220.60 (n/a)</td><td>190.46 (n/a)</td><td>205.40 (n/a)</td><td>128.50 (n/a)</td><td>36.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (+1.66%)</td><td>0.12 (+9.12%)</td><td>0.11 (+9.05%)</td><td>0.11 <b>(+26.39%)</b></td><td>0.01 <b>(-31.15%)</b></td><td>173.90 <b>(-20.88%)</b></td><td>160.26 (-9.90%)</td><td>165.10 (-8.28%)</td><td>131.50 (-1.65%)</td><td>17.08 <b>(-46.31%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>219.80 (n/a)</td><td>177.86 (n/a)</td><td>180.00 (n/a)</td><td>133.70 (n/a)</td><td>31.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (-10.84%)</td><td>0.10 (-7.30%)</td><td>0.10 (-7.09%)</td><td>0.10 (-3.68%)</td><td>0.01 <b>(-28.26%)</b></td><td>193.30 (+3.81%)</td><td>177.50 (+7.20%)</td><td>179.70 (+7.67%)</td><td>148.80 (+12.13%)</td><td>18.37 (-16.72%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>186.20 (n/a)</td><td>165.58 (n/a)</td><td>166.90 (n/a)</td><td>132.70 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (-5.38%)</td><td>0.10 (-4.75%)</td><td>0.10 (-14.83%)</td><td>0.09 <b>(+46.02%)</b></td><td>0.01 <b>(-54.30%)</b></td><td>215.70 <b>(-31.52%)</b></td><td>183.42 (-2.05%)</td><td>179.60 (+17.39%)</td><td>157.20 (+5.65%)</td><td>23.18 <b>(-67.69%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>315.00 (n/a)</td><td>187.26 (n/a)</td><td>153.00 (n/a)</td><td>148.80 (n/a)</td><td>71.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (-4.07%)</td><td>0.11 (+8.65%)</td><td>0.12 (+5.37%)</td><td>0.09 <b>(+52.82%)</b></td><td>0.02 <b>(-48.46%)</b></td><td>205.80 <b>(-34.58%)</b></td><td>164.86 (-14.28%)</td><td>160.30 (-5.09%)</td><td>138.40 (+4.22%)</td><td>24.74 <b>(-65.55%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>314.60 (n/a)</td><td>192.32 (n/a)</td><td>168.90 (n/a)</td><td>132.80 (n/a)</td><td>71.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (-13.71%)</td><td>0.10 (+1.53%)</td><td>0.11 (+6.97%)</td><td>0.08 <b>(+37.45%)</b></td><td>0.02 <b>(-36.67%)</b></td><td>224.20 <b>(-27.23%)</b></td><td>186.06 (-6.06%)</td><td>167.90 (-6.51%)</td><td>155.90 (+15.91%)</td><td>33.82 <b>(-48.23%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>308.10 (n/a)</td><td>198.06 (n/a)</td><td>179.60 (n/a)</td><td>134.50 (n/a)</td><td>65.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (+8.16%)</td><td>0.10 (+2.34%)</td><td>0.10 (+1.48%)</td><td>0.08 (-1.79%)</td><td>0.02 <b>(+47.73%)</b></td><td>228.20 (+1.83%)</td><td>190.76 (-1.00%)</td><td>193.50 (-1.48%)</td><td>149.00 (-7.57%)</td><td>33.43 <b>(+40.61%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>192.68 (n/a)</td><td>196.40 (n/a)</td><td>161.20 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.67 (-9.30%)</td><td>0.55 (-3.01%)</td><td>0.53 (+7.14%)</td><td>0.46 (-7.42%)</td><td>0.08 <b>(-28.24%)</b></td><td>214.20 (+8.02%)</td><td>180.68 (+2.01%)</td><td>184.30 (-6.68%)</td><td>145.70 (+10.30%)</td><td>24.73 (-17.72%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.74 (n/a)</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.50 (n/a)</td><td>0.11 (n/a)</td><td>198.30 (n/a)</td><td>177.12 (n/a)</td><td>197.50 (n/a)</td><td>132.10 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.62 (-3.13%)</td><td>0.52 (-4.28%)</td><td>0.55 (+3.49%)</td><td>0.41 <b>(-20.78%)</b></td><td>0.08 <b>(+57.29%)</b></td><td>239.30 <b>(+26.21%)</b></td><td>190.90 (+5.87%)</td><td>178.20 (-3.36%)</td><td>159.60 (+3.23%)</td><td>30.77 <b>(+110.27%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.05 (n/a)</td><td>189.60 (n/a)</td><td>180.32 (n/a)</td><td>184.40 (n/a)</td><td>154.60 (n/a)</td><td>14.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.71 (+10.01%)</td><td>0.53 (-0.89%)</td><td>0.47 (-9.41%)</td><td>0.43 (-5.27%)</td><td>0.12 <b>(+67.26%)</b></td><td>229.00 (+5.58%)</td><td>191.72 (+3.29%)</td><td>210.20 (+10.40%)</td><td>138.50 (-9.06%)</td><td>38.86 <b>(+62.68%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.65 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.45 (n/a)</td><td>0.07 (n/a)</td><td>216.90 (n/a)</td><td>185.62 (n/a)</td><td>190.40 (n/a)</td><td>152.30 (n/a)</td><td>23.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.55 <b>(-33.52%)</b></td><td>0.45 (-18.51%)</td><td>0.45 (-14.06%)</td><td>0.39 (-0.88%)</td><td>0.06 <b>(-65.86%)</b></td><td>252.90 (+0.88%)</td><td>219.26 (+16.43%)</td><td>219.60 (+16.31%)</td><td>180.30 <b>(+50.38%)</b></td><td>25.91 <b>(-48.39%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.82 (n/a)</td><td>0.56 (n/a)</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.17 (n/a)</td><td>250.70 (n/a)</td><td>188.32 (n/a)</td><td>188.80 (n/a)</td><td>119.90 (n/a)</td><td>50.20 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.53 (+11.53%)</td><td>0.43 (+5.37%)</td><td>0.41 (+3.68%)</td><td>0.39 (+0.17%)</td><td>0.06 <b>(+54.77%)</b></td><td>189.00 (-0.16%)</td><td>171.78 (-4.51%)</td><td>177.90 (-3.58%)</td><td>138.60 (-10.35%)</td><td>19.62 <b>(+37.05%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.04 (n/a)</td><td>189.30 (n/a)</td><td>179.90 (n/a)</td><td>184.50 (n/a)</td><td>154.60 (n/a)</td><td>14.31 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.41 <b>(-23.46%)</b></td><td>0.36 <b>(-20.17%)</b></td><td>0.40 (-11.22%)</td><td>0.25 <b>(-36.14%)</b></td><td>0.07 <b>(+23.68%)</b></td><td>299.80 <b>(+56.64%)</b></td><td>212.40 <b>(+28.40%)</b></td><td>185.40 (+12.64%)</td><td>180.70 <b>(+30.66%)</b></td><td>50.34 <b>(+157.50%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.05 (n/a)</td><td>191.40 (n/a)</td><td>165.42 (n/a)</td><td>164.60 (n/a)</td><td>138.30 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.47 <b>(-25.45%)</b></td><td>0.40 (-8.63%)</td><td>0.39 (-0.49%)</td><td>0.36 (+0.90%)</td><td>0.05 <b>(-58.90%)</b></td><td>205.80 (-0.91%)</td><td>186.30 (+5.90%)</td><td>190.40 (+0.53%)</td><td>158.10 <b>(+34.10%)</b></td><td>20.44 <b>(-44.25%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.63 (n/a)</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.11 (n/a)</td><td>207.70 (n/a)</td><td>175.92 (n/a)</td><td>189.40 (n/a)</td><td>117.90 (n/a)</td><td>36.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.50 (+15.09%)</td><td>0.42 (+4.24%)</td><td>0.46 (+7.19%)</td><td>0.32 (-9.05%)</td><td>0.08 <b>(+94.77%)</b></td><td>233.80 (+9.97%)</td><td>180.84 (-1.99%)</td><td>161.00 (-6.72%)</td><td>147.60 (-13.13%)</td><td>36.27 <b>(+89.17%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.04 (n/a)</td><td>212.60 (n/a)</td><td>184.52 (n/a)</td><td>172.60 (n/a)</td><td>169.90 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (+1.50%)</td><td>0.23 (+5.89%)</td><td>0.23 (+3.66%)</td><td>0.19 (+12.71%)</td><td>0.04 <b>(-22.35%)</b></td><td>194.90 (-11.29%)</td><td>163.20 (-7.25%)</td><td>162.00 (-3.51%)</td><td>127.80 (-1.54%)</td><td>24.32 <b>(-34.51%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>219.70 (n/a)</td><td>175.96 (n/a)</td><td>167.90 (n/a)</td><td>129.80 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (-1.60%)</td><td>0.21 (-4.18%)</td><td>0.20 (-9.80%)</td><td>0.19 (+15.11%)</td><td>0.02 <b>(-25.66%)</b></td><td>195.50 (-13.11%)</td><td>179.18 (+3.23%)</td><td>186.20 (+10.90%)</td><td>148.80 (+1.64%)</td><td>19.00 <b>(-36.94%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>225.00 (n/a)</td><td>173.58 (n/a)</td><td>167.90 (n/a)</td><td>146.40 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 (+8.39%)</td><td>0.23 (+13.60%)</td><td>0.22 (+9.25%)</td><td>0.17 (+19.55%)</td><td>0.06 (+4.46%)</td><td>218.30 (-16.36%)</td><td>171.44 (-12.74%)</td><td>170.60 (-8.48%)</td><td>120.30 (-7.75%)</td><td>42.61 (-19.02%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>261.00 (n/a)</td><td>196.46 (n/a)</td><td>186.40 (n/a)</td><td>130.40 (n/a)</td><td>52.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 <b>(+25.57%)</b></td><td>0.23 (+6.51%)</td><td>0.21 (+5.35%)</td><td>0.19 (+2.66%)</td><td>0.04 <b>(+97.84%)</b></td><td>192.50 (-2.58%)</td><td>167.18 (-4.66%)</td><td>171.70 (-5.09%)</td><td>123.50 <b>(-20.32%)</b></td><td>25.89 <b>(+48.75%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>197.60 (n/a)</td><td>175.36 (n/a)</td><td>180.90 (n/a)</td><td>155.00 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (+10.51%)</td><td>0.22 (+12.47%)</td><td>0.24 <b>(+20.00%)</b></td><td>0.17 (+0.41%)</td><td>0.05 <b>(+51.14%)</b></td><td>217.90 (-0.41%)</td><td>171.04 (-9.36%)</td><td>152.60 (-16.66%)</td><td>135.20 (-9.50%)</td><td>37.64 <b>(+38.45%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>218.80 (n/a)</td><td>188.70 (n/a)</td><td>183.10 (n/a)</td><td>149.40 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 (+15.82%)</td><td>0.22 (+11.03%)</td><td>0.21 (+9.85%)</td><td>0.18 (+19.45%)</td><td>0.04 <b>(+25.79%)</b></td><td>204.60 (-16.28%)</td><td>175.30 (-9.57%)</td><td>177.50 (-8.97%)</td><td>129.40 (-13.68%)</td><td>31.02 (-8.21%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>244.40 (n/a)</td><td>193.86 (n/a)</td><td>195.00 (n/a)</td><td>149.90 (n/a)</td><td>33.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (-18.46%)</td><td>0.19 (-6.31%)</td><td>0.19 (-3.37%)</td><td>0.18 (+10.26%)</td><td>0.01 <b>(-63.21%)</b></td><td>206.90 (-9.29%)</td><td>195.12 (+4.63%)</td><td>198.30 (+3.50%)</td><td>175.10 <b>(+22.62%)</b></td><td>12.95 <b>(-58.41%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>228.10 (n/a)</td><td>186.48 (n/a)</td><td>191.60 (n/a)</td><td>142.80 (n/a)</td><td>31.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (-19.55%)</td><td>0.20 (-7.55%)</td><td>0.21 (+9.68%)</td><td>0.15 (-12.29%)</td><td>0.03 <b>(-39.75%)</b></td><td>247.00 (+13.98%)</td><td>190.08 (+6.17%)</td><td>179.50 (-8.84%)</td><td>158.40 <b>(+24.33%)</b></td><td>33.50 (-11.36%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>216.70 (n/a)</td><td>179.04 (n/a)</td><td>196.90 (n/a)</td><td>127.40 (n/a)</td><td>37.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (-9.99%)</td><td>0.20 (-12.77%)</td><td>0.23 (-2.22%)</td><td>0.11 <b>(-45.50%)</b></td><td>0.06 <b>(+106.93%)</b></td><td>375.90 <b>(+83.46%)</b></td><td>221.00 <b>(+24.05%)</b></td><td>174.80 (+2.28%)</td><td>172.00 (+11.11%)</td><td>87.90 <b>(+321.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>204.90 (n/a)</td><td>178.16 (n/a)</td><td>170.90 (n/a)</td><td>154.80 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (-11.59%)</td><td>0.23 (-11.77%)</td><td>0.23 (-9.20%)</td><td>0.20 (-5.27%)</td><td>0.03 <b>(-32.99%)</b></td><td>205.60 (+5.54%)</td><td>181.72 (+12.21%)</td><td>175.00 (+10.13%)</td><td>152.10 (+13.09%)</td><td>22.26 (-17.82%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>194.80 (n/a)</td><td>161.94 (n/a)</td><td>158.90 (n/a)</td><td>134.50 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.36 <b>(+31.77%)</b></td><td>0.27 (+18.63%)</td><td>0.27 (+19.14%)</td><td>0.22 (+11.01%)</td><td>0.05 <b>(+94.61%)</b></td><td>186.60 (-9.94%)</td><td>154.58 (-14.38%)</td><td>153.50 (-16.07%)</td><td>115.20 <b>(-24.06%)</b></td><td>26.30 <b>(+31.04%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>207.20 (n/a)</td><td>180.54 (n/a)</td><td>182.90 (n/a)</td><td>151.70 (n/a)</td><td>20.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.33 (+6.52%)</td><td>0.23 (-11.54%)</td><td>0.24 (-9.17%)</td><td>0.14 <b>(-37.03%)</b></td><td>0.07 <b>(+89.17%)</b></td><td>295.10 <b>(+58.83%)</b></td><td>194.86 <b>(+21.27%)</b></td><td>173.00 (+10.12%)</td><td>123.20 (-6.10%)</td><td>66.41 <b>(+180.18%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>185.80 (n/a)</td><td>160.68 (n/a)</td><td>157.10 (n/a)</td><td>131.20 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.35 (+16.80%)</td><td>0.25 (+11.19%)</td><td>0.22 (+7.34%)</td><td>0.19 (-2.61%)</td><td>0.07 <b>(+55.91%)</b></td><td>221.40 (+2.69%)</td><td>169.96 (-7.39%)</td><td>185.00 (-6.85%)</td><td>116.90 (-14.36%)</td><td>43.10 <b>(+35.93%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>215.60 (n/a)</td><td>183.52 (n/a)</td><td>198.60 (n/a)</td><td>136.50 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (+18.42%)</td><td>0.24 (+9.59%)</td><td>0.26 (+11.57%)</td><td>0.17 (-1.09%)</td><td>0.05 <b>(+53.85%)</b></td><td>247.20 (+1.06%)</td><td>174.60 (-6.87%)</td><td>158.20 (-10.42%)</td><td>136.10 (-15.57%)</td><td>43.31 <b>(+31.45%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>244.60 (n/a)</td><td>187.48 (n/a)</td><td>176.60 (n/a)</td><td>161.20 (n/a)</td><td>32.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 <b>(-20.70%)</b></td><td>0.23 (-7.52%)</td><td>0.22 (+6.59%)</td><td>0.20 (+14.67%)</td><td>0.03 <b>(-57.94%)</b></td><td>205.80 (-12.80%)</td><td>180.90 (+2.32%)</td><td>182.40 (-6.17%)</td><td>149.10 <b>(+26.14%)</b></td><td>23.96 <b>(-51.99%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>236.00 (n/a)</td><td>176.80 (n/a)</td><td>194.40 (n/a)</td><td>118.20 (n/a)</td><td>49.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (+7.21%)</td><td>0.21 (+5.91%)</td><td>0.20 (+0.22%)</td><td>0.19 (+18.62%)</td><td>0.02 <b>(-21.39%)</b></td><td>214.00 (-15.68%)</td><td>196.72 (-6.12%)</td><td>201.40 (-0.25%)</td><td>175.60 (-6.70%)</td><td>15.85 <b>(-39.35%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>253.80 (n/a)</td><td>209.54 (n/a)</td><td>201.90 (n/a)</td><td>188.20 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (-3.43%)</td><td>0.20 (+2.29%)</td><td>0.20 (+5.29%)</td><td>0.12 (-1.31%)</td><td>0.06 (-7.55%)</td><td>279.50 (+1.34%)</td><td>185.52 (-3.11%)</td><td>177.60 (-5.03%)</td><td>132.60 (+3.59%)</td><td>60.03 (-3.24%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>275.80 (n/a)</td><td>191.48 (n/a)</td><td>187.00 (n/a)</td><td>128.00 (n/a)</td><td>62.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (-1.01%)</td><td>0.19 (-8.64%)</td><td>0.18 (+2.94%)</td><td>0.12 <b>(-22.37%)</b></td><td>0.05 (+10.21%)</td><td>282.00 <b>(+28.83%)</b></td><td>198.08 (+12.16%)</td><td>190.50 (-2.86%)</td><td>132.80 (+1.07%)</td><td>57.91 <b>(+47.54%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>218.90 (n/a)</td><td>176.60 (n/a)</td><td>196.10 (n/a)</td><td>131.40 (n/a)</td><td>39.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (+9.02%)</td><td>0.19 (-8.02%)</td><td>0.17 (-7.87%)</td><td>0.10 <b>(-37.81%)</b></td><td>0.08 <b>(+94.61%)</b></td><td>333.50 <b>(+60.80%)</b></td><td>210.12 <b>(+21.34%)</b></td><td>200.20 (+8.51%)</td><td>120.50 (-8.23%)</td><td>86.70 <b>(+184.75%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>207.40 (n/a)</td><td>173.16 (n/a)</td><td>184.50 (n/a)</td><td>131.30 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 <b>(+36.31%)</b></td><td>0.25 <b>(+37.36%)</b></td><td>0.25 <b>(+42.27%)</b></td><td>0.17 (+12.06%)</td><td>0.06 <b>(+76.41%)</b></td><td>208.20 (-10.76%)</td><td>146.50 <b>(-25.51%)</b></td><td>140.60 <b>(-29.74%)</b></td><td>113.20 <b>(-26.64%)</b></td><td>37.69 (+16.36%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>233.30 (n/a)</td><td>196.68 (n/a)</td><td>200.10 (n/a)</td><td>154.30 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (+9.91%)</td><td>0.22 <b>(+27.69%)</b></td><td>0.21 (+14.88%)</td><td>0.19 <b>(+102.22%)</b></td><td>0.02 <b>(-53.98%)</b></td><td>187.20 <b>(-50.55%)</b></td><td>163.42 <b>(-28.36%)</b></td><td>167.30 (-12.96%)</td><td>138.80 (-9.04%)</td><td>17.72 <b>(-80.25%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>378.60 (n/a)</td><td>228.10 (n/a)</td><td>192.20 (n/a)</td><td>152.60 (n/a)</td><td>89.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (+4.07%)</td><td>0.23 (+17.23%)</td><td>0.23 <b>(+31.68%)</b></td><td>0.18 (+10.32%)</td><td>0.05 (-3.27%)</td><td>197.50 (-9.36%)</td><td>156.18 (-15.43%)</td><td>154.00 <b>(-24.06%)</b></td><td>114.30 (-3.87%)</td><td>35.31 (-14.66%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>217.90 (n/a)</td><td>184.68 (n/a)</td><td>202.80 (n/a)</td><td>118.90 (n/a)</td><td>41.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 <b>(-37.49%)</b></td><td>0.16 <b>(-24.17%)</b></td><td>0.17 <b>(-26.54%)</b></td><td>0.14 (-2.27%)</td><td>0.02 <b>(-66.68%)</b></td><td>250.30 (+2.29%)</td><td>219.76 <b>(+24.26%)</b></td><td>209.90 <b>(+36.12%)</b></td><td>182.80 <b>(+60.07%)</b></td><td>28.81 <b>(-45.56%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>244.70 (n/a)</td><td>176.86 (n/a)</td><td>154.20 (n/a)</td><td>114.20 (n/a)</td><td>52.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (-14.62%)</td><td>0.19 (-6.79%)</td><td>0.18 (-12.99%)</td><td>0.17 (+15.62%)</td><td>0.03 <b>(-40.46%)</b></td><td>209.30 (-13.51%)</td><td>185.68 (+4.66%)</td><td>190.00 (+14.94%)</td><td>154.60 (+17.12%)</td><td>24.50 <b>(-40.18%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>242.00 (n/a)</td><td>177.42 (n/a)</td><td>165.30 (n/a)</td><td>132.00 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.93 (+7.50%)</td><td>0.80 (+5.94%)</td><td>0.74 (-5.94%)</td><td>0.68 (+2.96%)</td><td>0.12 <b>(+26.10%)</b></td><td>193.80 (-2.86%)</td><td>166.74 (-5.18%)</td><td>177.30 (+6.29%)</td><td>141.00 (-6.99%)</td><td>23.86 (+7.46%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.86 (n/a)</td><td>0.75 (n/a)</td><td>0.79 (n/a)</td><td>0.66 (n/a)</td><td>0.09 (n/a)</td><td>199.50 (n/a)</td><td>175.84 (n/a)</td><td>166.80 (n/a)</td><td>151.60 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.91 (-0.79%)</td><td>0.80 (+1.40%)</td><td>0.82 (+11.23%)</td><td>0.69 (+1.44%)</td><td>0.10 (-2.84%)</td><td>190.20 (-1.40%)</td><td>166.54 (-1.41%)</td><td>159.70 (-10.08%)</td><td>144.80 (+0.77%)</td><td>20.72 (-0.48%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.91 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.10 (n/a)</td><td>192.90 (n/a)</td><td>168.92 (n/a)</td><td>177.60 (n/a)</td><td>143.70 (n/a)</td><td>20.82 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.74 (-16.49%)</td><td>0.72 (-3.00%)</td><td>0.72 (+1.69%)</td><td>0.71 (+6.94%)</td><td>0.01 <b>(-83.79%)</b></td><td>185.80 (-6.49%)</td><td>181.04 (+1.97%)</td><td>182.40 (-1.67%)</td><td>177.00 (+19.76%)</td><td>3.69 <b>(-81.87%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.89 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.66 (n/a)</td><td>0.09 (n/a)</td><td>198.70 (n/a)</td><td>177.54 (n/a)</td><td>185.50 (n/a)</td><td>147.80 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.00 (+0.00%)</td><td>0.00 (+1.82%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+18.32%)</td><td>3904.01 (-0.95%)</td><td>3621.29 (-3.85%)</td><td>3624.14 (-4.99%)</td><td>3472.18 (-2.34%)</td><td>175.68 (+16.72%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>3941.55 (n/a)</td><td>3766.17 (n/a)</td><td>3814.62 (n/a)</td><td>3555.25 (n/a)</td><td>150.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.00 (+0.00%)</td><td>0.00 (+1.82%)</td><td>0.00 (+0.00%)</td><td>0.00 (+4.76%)</td><td>0.00 <b>(-45.23%)</b></td><td>3765.70 (-3.25%)</td><td>3661.81 (-1.42%)</td><td>3649.03 (-0.69%)</td><td>3530.29 (+0.45%)</td><td>102.15 <b>(-39.04%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>3892.29 (n/a)</td><td>3714.59 (n/a)</td><td>3674.48 (n/a)</td><td>3514.47 (n/a)</td><td>167.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 (+0.11%)</td><td>0.19 (+2.25%)</td><td>0.16 (-1.23%)</td><td>0.15 (-2.14%)</td><td>0.05 (-0.77%)</td><td>13910.50 (+2.24%)</td><td>11765.58 (-2.19%)</td><td>13091.30 (+1.25%)</td><td>7499.80 (-0.11%)</td><td>2593.00 (+1.71%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>13606.27 (n/a)</td><td>12028.65 (n/a)</td><td>12929.34 (n/a)</td><td>7507.78 (n/a)</td><td>2549.31 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>6.00 (-7.48%)</td><td>4.76 (-5.20%)</td><td>4.61 (-0.02%)</td><td>3.76 (-9.40%)</td><td>0.81 (-11.39%)</td><td>278.60 (+10.38%)</td><td>225.40 (+5.35%)</td><td>227.50 (+0.00%)</td><td>174.80 (+8.10%)</td><td>37.08 (+6.77%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>6.48 (n/a)</td><td>5.02 (n/a)</td><td>4.61 (n/a)</td><td>4.15 (n/a)</td><td>0.91 (n/a)</td><td>252.40 (n/a)</td><td>213.96 (n/a)</td><td>227.50 (n/a)</td><td>161.70 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.07 (-3.32%)</td><td>5.04 (-2.53%)</td><td>4.57 (-8.79%)</td><td>4.45 (+13.74%)</td><td>0.75 <b>(-29.32%)</b></td><td>235.70 (-12.09%)</td><td>211.54 (+0.78%)</td><td>229.30 (+9.66%)</td><td>172.70 (+3.41%)</td><td>29.42 <b>(-32.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.28 (n/a)</td><td>5.17 (n/a)</td><td>5.01 (n/a)</td><td>3.91 (n/a)</td><td>1.06 (n/a)</td><td>268.10 (n/a)</td><td>209.90 (n/a)</td><td>209.10 (n/a)</td><td>167.00 (n/a)</td><td>43.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>5.95 (+11.71%)</td><td>4.84 (+7.44%)</td><td>4.72 (+6.09%)</td><td>4.21 (+3.07%)</td><td>0.67 <b>(+34.95%)</b></td><td>249.30 (-3.00%)</td><td>219.48 (-6.46%)</td><td>222.20 (-5.73%)</td><td>176.30 (-10.46%)</td><td>27.64 (+15.56%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.32 (n/a)</td><td>4.51 (n/a)</td><td>4.45 (n/a)</td><td>4.08 (n/a)</td><td>0.50 (n/a)</td><td>257.00 (n/a)</td><td>234.64 (n/a)</td><td>235.70 (n/a)</td><td>196.90 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.90 (-8.30%)</td><td>5.29 (-9.69%)</td><td>5.33 (-9.44%)</td><td>4.32 (-17.92%)</td><td>0.63 <b>(+48.72%)</b></td><td>242.80 <b>(+21.89%)</b></td><td>200.84 (+11.65%)</td><td>196.70 (+10.44%)</td><td>177.70 (+9.09%)</td><td>25.91 <b>(+98.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.44 (n/a)</td><td>5.85 (n/a)</td><td>5.89 (n/a)</td><td>5.26 (n/a)</td><td>0.42 (n/a)</td><td>199.20 (n/a)</td><td>179.88 (n/a)</td><td>178.10 (n/a)</td><td>162.90 (n/a)</td><td>13.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>5.01 (-2.49%)</td><td>4.70 (-1.00%)</td><td>4.76 (-0.36%)</td><td>4.15 (-5.79%)</td><td>0.33 (+19.72%)</td><td>252.40 (+6.14%)</td><td>224.24 (+1.16%)</td><td>220.50 (+0.36%)</td><td>209.20 (+2.55%)</td><td>16.76 <b>(+32.02%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.14 (n/a)</td><td>4.74 (n/a)</td><td>4.77 (n/a)</td><td>4.41 (n/a)</td><td>0.27 (n/a)</td><td>237.80 (n/a)</td><td>221.66 (n/a)</td><td>219.70 (n/a)</td><td>204.00 (n/a)</td><td>12.70 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.74 (-0.12%)</td><td>4.61 (-7.02%)</td><td>4.54 (-11.57%)</td><td>3.96 (+14.09%)</td><td>0.71 <b>(-20.62%)</b></td><td>264.80 (-12.35%)</td><td>231.30 (+5.98%)</td><td>230.90 (+13.13%)</td><td>182.80 (+0.11%)</td><td>32.62 <b>(-32.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>5.74 (n/a)</td><td>4.96 (n/a)</td><td>5.14 (n/a)</td><td>3.47 (n/a)</td><td>0.89 (n/a)</td><td>302.10 (n/a)</td><td>218.24 (n/a)</td><td>204.10 (n/a)</td><td>182.60 (n/a)</td><td>48.31 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>6.29 (+15.85%)</td><td>5.36 (+14.43%)</td><td>5.02 (-4.00%)</td><td>4.50 <b>(+21.85%)</b></td><td>0.79 (-8.28%)</td><td>232.90 (-17.94%)</td><td>198.84 (-13.71%)</td><td>208.80 (+4.14%)</td><td>166.70 (-13.72%)</td><td>28.74 <b>(-36.89%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.43 (n/a)</td><td>4.69 (n/a)</td><td>5.23 (n/a)</td><td>3.69 (n/a)</td><td>0.87 (n/a)</td><td>283.80 (n/a)</td><td>230.42 (n/a)</td><td>200.50 (n/a)</td><td>193.20 (n/a)</td><td>45.55 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.46 (-11.94%)</td><td>4.86 (-6.49%)</td><td>5.12 (-1.20%)</td><td>3.86 (-5.40%)</td><td>0.62 (-18.01%)</td><td>271.90 (+5.67%)</td><td>219.16 (+6.57%)</td><td>204.90 (+1.24%)</td><td>192.00 (+13.54%)</td><td>31.52 (-1.78%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.20 (n/a)</td><td>5.19 (n/a)</td><td>5.18 (n/a)</td><td>4.08 (n/a)</td><td>0.76 (n/a)</td><td>257.30 (n/a)</td><td>205.64 (n/a)</td><td>202.40 (n/a)</td><td>169.10 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>9.10 (-5.10%)</td><td>7.92 (-1.77%)</td><td>7.89 (+0.64%)</td><td>5.99 (-14.58%)</td><td>1.27 <b>(+31.27%)</b></td><td>349.90 (+17.06%)</td><td>271.12 (+3.06%)</td><td>265.60 (-0.64%)</td><td>230.50 (+5.35%)</td><td>48.65 <b>(+62.78%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>9.58 (n/a)</td><td>8.06 (n/a)</td><td>7.84 (n/a)</td><td>7.02 (n/a)</td><td>0.97 (n/a)</td><td>298.90 (n/a)</td><td>263.08 (n/a)</td><td>267.30 (n/a)</td><td>218.80 (n/a)</td><td>29.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.30 (+1.85%)</td><td>7.79 (-9.28%)</td><td>7.97 (-7.36%)</td><td>6.48 <b>(-21.46%)</b></td><td>1.12 <b>(+212.94%)</b></td><td>323.40 <b>(+27.32%)</b></td><td>273.58 (+11.90%)</td><td>263.30 (+7.95%)</td><td>225.40 (-1.83%)</td><td>39.14 <b>(+294.42%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.14 (n/a)</td><td>8.59 (n/a)</td><td>8.60 (n/a)</td><td>8.26 (n/a)</td><td>0.36 (n/a)</td><td>254.00 (n/a)</td><td>244.48 (n/a)</td><td>243.90 (n/a)</td><td>229.60 (n/a)</td><td>9.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.91 (-0.33%)</td><td>7.48 (-8.87%)</td><td>8.07 (+0.87%)</td><td>5.77 <b>(-21.29%)</b></td><td>1.27 <b>(+80.86%)</b></td><td>363.70 <b>(+27.08%)</b></td><td>287.48 (+11.87%)</td><td>260.00 (-0.84%)</td><td>235.50 (+0.34%)</td><td>52.53 <b>(+137.47%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.94 (n/a)</td><td>8.21 (n/a)</td><td>8.00 (n/a)</td><td>7.33 (n/a)</td><td>0.70 (n/a)</td><td>286.20 (n/a)</td><td>256.98 (n/a)</td><td>262.20 (n/a)</td><td>234.70 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.96 (-14.23%)</td><td>7.45 (-7.69%)</td><td>7.63 (-3.08%)</td><td>6.68 (-7.17%)</td><td>0.49 <b>(-39.44%)</b></td><td>313.90 (+7.72%)</td><td>282.30 (+7.89%)</td><td>274.80 (+3.15%)</td><td>263.60 (+16.59%)</td><td>19.35 <b>(-22.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.28 (n/a)</td><td>8.08 (n/a)</td><td>7.87 (n/a)</td><td>7.20 (n/a)</td><td>0.80 (n/a)</td><td>291.40 (n/a)</td><td>261.66 (n/a)</td><td>266.40 (n/a)</td><td>226.10 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>9.51 (+6.01%)</td><td>7.94 (-3.92%)</td><td>7.73 (-10.93%)</td><td>7.14 (-1.26%)</td><td>0.91 <b>(+23.13%)</b></td><td>293.50 (+1.24%)</td><td>266.54 (+4.35%)</td><td>271.40 (+12.29%)</td><td>220.60 (-5.69%)</td><td>27.30 (+14.53%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.97 (n/a)</td><td>8.27 (n/a)</td><td>8.68 (n/a)</td><td>7.24 (n/a)</td><td>0.74 (n/a)</td><td>289.90 (n/a)</td><td>255.42 (n/a)</td><td>241.70 (n/a)</td><td>233.90 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.32 (+4.81%)</td><td>7.98 (-5.16%)</td><td>7.86 (-6.29%)</td><td>6.85 (-14.35%)</td><td>0.92 <b>(+134.01%)</b></td><td>306.10 (+16.74%)</td><td>265.38 (+6.35%)</td><td>266.90 (+6.72%)</td><td>225.00 (-4.62%)</td><td>30.03 <b>(+159.23%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>8.89 (n/a)</td><td>8.42 (n/a)</td><td>8.39 (n/a)</td><td>8.00 (n/a)</td><td>0.39 (n/a)</td><td>262.20 (n/a)</td><td>249.54 (n/a)</td><td>250.10 (n/a)</td><td>235.90 (n/a)</td><td>11.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>10.79 (+18.66%)</td><td>8.53 (+7.04%)</td><td>8.07 (-2.50%)</td><td>7.19 <b>(+32.22%)</b></td><td>1.49 (+0.50%)</td><td>291.80 <b>(-24.36%)</b></td><td>251.60 (-7.77%)</td><td>259.90 (+2.57%)</td><td>194.30 (-15.70%)</td><td>40.54 <b>(-37.12%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>9.10 (n/a)</td><td>7.97 (n/a)</td><td>8.27 (n/a)</td><td>5.44 (n/a)</td><td>1.48 (n/a)</td><td>385.80 (n/a)</td><td>272.80 (n/a)</td><td>253.40 (n/a)</td><td>230.50 (n/a)</td><td>64.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.58 (-10.71%)</td><td>7.74 (-6.57%)</td><td>7.96 (-3.41%)</td><td>7.02 (+0.70%)</td><td>0.68 <b>(-29.18%)</b></td><td>298.80 (-0.70%)</td><td>272.60 (+6.53%)</td><td>263.40 (+3.50%)</td><td>244.40 (+11.96%)</td><td>24.05 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.61 (n/a)</td><td>8.28 (n/a)</td><td>8.24 (n/a)</td><td>6.97 (n/a)</td><td>0.96 (n/a)</td><td>300.90 (n/a)</td><td>255.90 (n/a)</td><td>254.50 (n/a)</td><td>218.30 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>10.28 (-2.91%)</td><td>8.64 (+0.99%)</td><td>8.70 (+4.22%)</td><td>7.57 (+5.72%)</td><td>1.06 <b>(-20.03%)</b></td><td>277.10 (-5.43%)</td><td>245.54 (-1.65%)</td><td>241.10 (-4.06%)</td><td>203.90 (+2.98%)</td><td>28.42 <b>(-21.61%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>10.59 (n/a)</td><td>8.55 (n/a)</td><td>8.35 (n/a)</td><td>7.16 (n/a)</td><td>1.32 (n/a)</td><td>293.00 (n/a)</td><td>249.66 (n/a)</td><td>251.30 (n/a)</td><td>198.00 (n/a)</td><td>36.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.12 (-7.72%)</td><td>7.78 (-14.12%)</td><td>8.18 (-8.20%)</td><td>5.47 <b>(-36.73%)</b></td><td>1.37 <b>(+184.57%)</b></td><td>383.20 <b>(+58.02%)</b></td><td>278.10 (+19.85%)</td><td>256.50 (+8.96%)</td><td>230.00 (+8.39%)</td><td>60.38 <b>(+413.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.88 (n/a)</td><td>9.06 (n/a)</td><td>8.91 (n/a)</td><td>8.65 (n/a)</td><td>0.48 (n/a)</td><td>242.50 (n/a)</td><td>232.04 (n/a)</td><td>235.40 (n/a)</td><td>212.20 (n/a)</td><td>11.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.97 (+1.35%)</td><td>8.16 (-3.51%)</td><td>8.47 (+0.60%)</td><td>6.88 (-14.56%)</td><td>0.80 <b>(+176.53%)</b></td><td>304.70 (+17.06%)</td><td>259.04 (+4.40%)</td><td>247.60 (-0.60%)</td><td>233.70 (-1.35%)</td><td>27.55 <b>(+225.07%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.85 (n/a)</td><td>8.46 (n/a)</td><td>8.42 (n/a)</td><td>8.06 (n/a)</td><td>0.29 (n/a)</td><td>260.30 (n/a)</td><td>248.12 (n/a)</td><td>249.10 (n/a)</td><td>236.90 (n/a)</td><td>8.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.39 (-14.41%)</td><td>7.08 <b>(-20.79%)</b></td><td>7.49 (-17.64%)</td><td>5.61 <b>(-31.28%)</b></td><td>1.27 <b>(+93.89%)</b></td><td>373.50 <b>(+45.50%)</b></td><td>304.60 <b>(+29.18%)</b></td><td>280.10 <b>(+21.41%)</b></td><td>250.10 (+16.87%)</td><td>57.28 <b>(+231.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.80 (n/a)</td><td>8.93 (n/a)</td><td>9.09 (n/a)</td><td>8.17 (n/a)</td><td>0.65 (n/a)</td><td>256.70 (n/a)</td><td>235.80 (n/a)</td><td>230.70 (n/a)</td><td>214.00 (n/a)</td><td>17.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>11.11 (-3.62%)</td><td>10.63 (-0.32%)</td><td>10.80 (+0.82%)</td><td>9.71 (-0.27%)</td><td>0.57 <b>(-21.47%)</b></td><td>432.00 (+0.26%)</td><td>395.60 (+0.18%)</td><td>388.20 (-0.82%)</td><td>377.40 (+3.77%)</td><td>22.37 (-18.31%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>11.53 (n/a)</td><td>10.66 (n/a)</td><td>10.72 (n/a)</td><td>9.73 (n/a)</td><td>0.73 (n/a)</td><td>430.90 (n/a)</td><td>394.90 (n/a)</td><td>391.40 (n/a)</td><td>363.70 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.79 (+4.79%)</td><td>10.71 (-4.69%)</td><td>10.59 (-5.22%)</td><td>8.04 <b>(-21.86%)</b></td><td>1.77 <b>(+114.98%)</b></td><td>521.90 <b>(+27.98%)</b></td><td>401.16 (+7.05%)</td><td>396.00 (+5.52%)</td><td>328.10 (-4.57%)</td><td>73.89 <b>(+168.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.20 (n/a)</td><td>11.24 (n/a)</td><td>11.18 (n/a)</td><td>10.28 (n/a)</td><td>0.83 (n/a)</td><td>407.80 (n/a)</td><td>374.74 (n/a)</td><td>375.30 (n/a)</td><td>343.80 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>12.06 (-6.03%)</td><td>11.28 (-1.26%)</td><td>11.57 (+6.33%)</td><td>10.32 (-3.51%)</td><td>0.69 <b>(-26.47%)</b></td><td>406.50 (+3.65%)</td><td>372.82 (+1.06%)</td><td>362.40 (-5.97%)</td><td>347.80 (+6.39%)</td><td>23.33 (-18.90%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>12.83 (n/a)</td><td>11.43 (n/a)</td><td>10.88 (n/a)</td><td>10.69 (n/a)</td><td>0.94 (n/a)</td><td>392.20 (n/a)</td><td>368.90 (n/a)</td><td>385.40 (n/a)</td><td>326.90 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.22 (-7.10%)</td><td>11.22 (-5.79%)</td><td>11.11 (-10.84%)</td><td>10.08 (-0.84%)</td><td>0.82 <b>(-31.08%)</b></td><td>416.30 (+0.85%)</td><td>375.54 (+5.70%)</td><td>377.40 (+12.15%)</td><td>343.30 (+7.65%)</td><td>28.08 <b>(-25.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.15 (n/a)</td><td>11.91 (n/a)</td><td>12.47 (n/a)</td><td>10.16 (n/a)</td><td>1.20 (n/a)</td><td>412.80 (n/a)</td><td>355.28 (n/a)</td><td>336.50 (n/a)</td><td>318.90 (n/a)</td><td>37.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>12.66 (-3.80%)</td><td>11.29 (-1.82%)</td><td>11.25 (+1.28%)</td><td>9.73 (-10.72%)</td><td>1.05 (+10.48%)</td><td>430.90 (+12.01%)</td><td>374.34 (+2.09%)</td><td>372.90 (-1.24%)</td><td>331.30 (+3.95%)</td><td>36.22 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.16 (n/a)</td><td>11.50 (n/a)</td><td>11.11 (n/a)</td><td>10.90 (n/a)</td><td>0.95 (n/a)</td><td>384.70 (n/a)</td><td>366.68 (n/a)</td><td>377.60 (n/a)</td><td>318.70 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.69 (+1.23%)</td><td>10.74 (-9.37%)</td><td>11.05 (-5.08%)</td><td>8.04 <b>(-29.12%)</b></td><td>1.68 <b>(+237.04%)</b></td><td>521.70 <b>(+41.08%)</b></td><td>399.42 (+12.70%)</td><td>379.40 (+5.33%)</td><td>330.50 (-1.23%)</td><td>71.97 <b>(+389.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.54 (n/a)</td><td>11.85 (n/a)</td><td>11.65 (n/a)</td><td>11.34 (n/a)</td><td>0.50 (n/a)</td><td>369.80 (n/a)</td><td>354.42 (n/a)</td><td>360.20 (n/a)</td><td>334.60 (n/a)</td><td>14.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.35 (-9.53%)</td><td>12.75 (-6.64%)</td><td>12.97 (-4.78%)</td><td>11.99 (-3.64%)</td><td>0.60 <b>(-37.94%)</b></td><td>349.70 (+3.77%)</td><td>329.44 (+6.87%)</td><td>323.30 (+5.04%)</td><td>314.30 (+10.55%)</td><td>15.68 <b>(-28.60%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>14.75 (n/a)</td><td>13.66 (n/a)</td><td>13.63 (n/a)</td><td>12.45 (n/a)</td><td>0.96 (n/a)</td><td>337.00 (n/a)</td><td>308.26 (n/a)</td><td>307.80 (n/a)</td><td>284.30 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.14 (-1.28%)</td><td>12.97 (-3.81%)</td><td>12.38 (-4.30%)</td><td>12.00 (+1.39%)</td><td>1.32 (-15.31%)</td><td>349.60 (-1.38%)</td><td>325.76 (+3.66%)</td><td>338.70 (+4.50%)</td><td>277.00 (+1.32%)</td><td>30.47 (-14.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>15.34 (n/a)</td><td>13.49 (n/a)</td><td>12.94 (n/a)</td><td>11.83 (n/a)</td><td>1.56 (n/a)</td><td>354.50 (n/a)</td><td>314.26 (n/a)</td><td>324.10 (n/a)</td><td>273.40 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>12.80 (-6.03%)</td><td>12.29 (-3.73%)</td><td>12.46 (-0.68%)</td><td>11.38 (-5.90%)</td><td>0.55 (-6.92%)</td><td>368.50 (+6.29%)</td><td>341.96 (+3.88%)</td><td>336.50 (+0.69%)</td><td>327.60 (+6.40%)</td><td>15.87 (+6.76%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.62 (n/a)</td><td>12.76 (n/a)</td><td>12.55 (n/a)</td><td>12.10 (n/a)</td><td>0.59 (n/a)</td><td>346.70 (n/a)</td><td>329.20 (n/a)</td><td>334.20 (n/a)</td><td>307.90 (n/a)</td><td>14.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.09 (-5.90%)</td><td>12.36 (-7.75%)</td><td>12.58 (-6.85%)</td><td>10.90 (-11.37%)</td><td>1.20 (+4.75%)</td><td>384.90 (+12.81%)</td><td>341.76 (+8.56%)</td><td>333.40 (+7.34%)</td><td>297.60 (+6.25%)</td><td>32.68 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.98 (n/a)</td><td>13.40 (n/a)</td><td>13.50 (n/a)</td><td>12.29 (n/a)</td><td>1.14 (n/a)</td><td>341.20 (n/a)</td><td>314.80 (n/a)</td><td>310.60 (n/a)</td><td>280.10 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.27 (-2.01%)</td><td>12.26 (+2.33%)</td><td>12.13 (-2.00%)</td><td>11.02 (+17.17%)</td><td>0.97 <b>(-41.43%)</b></td><td>380.40 (-14.65%)</td><td>343.84 (-3.45%)</td><td>345.80 (+2.04%)</td><td>316.10 (+2.03%)</td><td>27.37 <b>(-50.00%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.54 (n/a)</td><td>11.98 (n/a)</td><td>12.37 (n/a)</td><td>9.41 (n/a)</td><td>1.65 (n/a)</td><td>445.70 (n/a)</td><td>356.12 (n/a)</td><td>338.90 (n/a)</td><td>309.80 (n/a)</td><td>54.74 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.26 (+5.74%)</td><td>12.48 (-0.64%)</td><td>12.66 (-2.21%)</td><td>9.12 (-14.69%)</td><td>2.19 <b>(+40.34%)</b></td><td>459.80 (+17.24%)</td><td>345.66 (+2.18%)</td><td>331.40 (+2.25%)</td><td>274.90 (-5.44%)</td><td>68.46 <b>(+59.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.43 (n/a)</td><td>12.56 (n/a)</td><td>12.94 (n/a)</td><td>10.69 (n/a)</td><td>1.56 (n/a)</td><td>392.20 (n/a)</td><td>338.28 (n/a)</td><td>324.10 (n/a)</td><td>290.70 (n/a)</td><td>42.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>14.57 (-6.34%)</td><td>12.86 (-6.12%)</td><td>13.10 (-0.03%)</td><td>11.22 (-8.47%)</td><td>1.29 (-8.81%)</td><td>373.90 (+9.26%)</td><td>328.74 (+6.49%)</td><td>320.10 (+0.03%)</td><td>287.80 (+6.75%)</td><td>33.31 (+7.51%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>15.56 (n/a)</td><td>13.70 (n/a)</td><td>13.11 (n/a)</td><td>12.26 (n/a)</td><td>1.42 (n/a)</td><td>342.20 (n/a)</td><td>308.70 (n/a)</td><td>320.00 (n/a)</td><td>269.60 (n/a)</td><td>30.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.75 (+5.58%)</td><td>13.18 (-1.29%)</td><td>13.02 (-2.55%)</td><td>10.68 (-16.09%)</td><td>1.64 <b>(+245.21%)</b></td><td>392.80 (+19.17%)</td><td>322.62 (+2.58%)</td><td>322.20 (+2.61%)</td><td>284.40 (-5.26%)</td><td>43.64 <b>(+287.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.97 (n/a)</td><td>13.35 (n/a)</td><td>13.36 (n/a)</td><td>12.73 (n/a)</td><td>0.48 (n/a)</td><td>329.60 (n/a)</td><td>314.50 (n/a)</td><td>314.00 (n/a)</td><td>300.20 (n/a)</td><td>11.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>14.10 (+4.81%)</td><td>12.86 (+6.86%)</td><td>13.58 (+6.83%)</td><td>10.79 (+11.47%)</td><td>1.44 (-12.86%)</td><td>388.70 (-10.29%)</td><td>329.66 (-6.95%)</td><td>308.80 (-6.40%)</td><td>297.50 (-4.62%)</td><td>39.49 <b>(-25.02%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.45 (n/a)</td><td>12.04 (n/a)</td><td>12.71 (n/a)</td><td>9.68 (n/a)</td><td>1.65 (n/a)</td><td>433.30 (n/a)</td><td>354.28 (n/a)</td><td>329.90 (n/a)</td><td>311.90 (n/a)</td><td>52.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>17.73 (-7.59%)</td><td>12.82 (-9.96%)</td><td>12.67 (-8.75%)</td><td>9.51 (+2.33%)</td><td>3.37 (-11.44%)</td><td>440.80 (-2.28%)</td><td>345.08 (+10.11%)</td><td>330.90 (+9.57%)</td><td>236.50 (+8.19%)</td><td>86.11 (-4.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>19.19 (n/a)</td><td>14.23 (n/a)</td><td>13.89 (n/a)</td><td>9.30 (n/a)</td><td>3.81 (n/a)</td><td>451.10 (n/a)</td><td>313.40 (n/a)</td><td>302.00 (n/a)</td><td>218.60 (n/a)</td><td>89.93 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.21 (-7.12%)</td><td>2.65 (-2.72%)</td><td>2.61 (+3.59%)</td><td>2.31 (+1.79%)</td><td>0.35 <b>(-27.80%)</b></td><td>226.70 (-1.73%)</td><td>200.62 (+1.75%)</td><td>201.20 (-3.45%)</td><td>163.10 (+7.66%)</td><td>24.11 <b>(-24.16%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>3.46 (n/a)</td><td>2.72 (n/a)</td><td>2.52 (n/a)</td><td>2.27 (n/a)</td><td>0.48 (n/a)</td><td>230.70 (n/a)</td><td>197.16 (n/a)</td><td>208.40 (n/a)</td><td>151.50 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>5.58 (+0.05%)</td><td>4.84 (-2.66%)</td><td>4.74 (-8.13%)</td><td>3.66 (-13.36%)</td><td>0.77 <b>(+33.89%)</b></td><td>286.30 (+15.44%)</td><td>221.84 (+3.94%)</td><td>221.40 (+8.85%)</td><td>187.80 (-0.05%)</td><td>39.60 <b>(+53.81%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.58 (n/a)</td><td>4.97 (n/a)</td><td>5.16 (n/a)</td><td>4.23 (n/a)</td><td>0.58 (n/a)</td><td>248.00 (n/a)</td><td>213.44 (n/a)</td><td>203.40 (n/a)</td><td>187.90 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.87 (+12.37%)</td><td>7.97 (+6.18%)</td><td>8.08 (+5.93%)</td><td>7.25 (+4.56%)</td><td>0.66 <b>(+64.31%)</b></td><td>289.10 (-4.37%)</td><td>264.46 (-5.54%)</td><td>259.50 (-5.60%)</td><td>236.50 (-11.02%)</td><td>21.68 <b>(+41.43%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.89 (n/a)</td><td>7.51 (n/a)</td><td>7.63 (n/a)</td><td>6.94 (n/a)</td><td>0.40 (n/a)</td><td>302.30 (n/a)</td><td>279.98 (n/a)</td><td>274.90 (n/a)</td><td>265.80 (n/a)</td><td>15.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.42 (+7.36%)</td><td>2.69 (-1.00%)</td><td>2.67 (-10.43%)</td><td>2.19 <b>(+46.58%)</b></td><td>0.45 <b>(-34.58%)</b></td><td>239.90 <b>(-31.79%)</b></td><td>199.02 (-4.85%)</td><td>196.70 (+11.63%)</td><td>153.50 (-6.86%)</td><td>31.19 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.18 (n/a)</td><td>2.72 (n/a)</td><td>2.98 (n/a)</td><td>1.49 (n/a)</td><td>0.69 (n/a)</td><td>351.70 (n/a)</td><td>209.16 (n/a)</td><td>176.20 (n/a)</td><td>164.80 (n/a)</td><td>79.85 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.46 (-13.72%)</td><td>2.80 (-9.64%)</td><td>2.86 (-5.57%)</td><td>2.19 (-16.79%)</td><td>0.46 (-14.51%)</td><td>239.20 <b>(+20.20%)</b></td><td>191.54 (+10.77%)</td><td>183.30 (+5.89%)</td><td>151.60 (+15.90%)</td><td>32.14 <b>(+22.37%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>4.01 (n/a)</td><td>3.10 (n/a)</td><td>3.03 (n/a)</td><td>2.63 (n/a)</td><td>0.54 (n/a)</td><td>199.00 (n/a)</td><td>172.92 (n/a)</td><td>173.10 (n/a)</td><td>130.80 (n/a)</td><td>26.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.35 (+11.05%)</td><td>2.64 (-8.02%)</td><td>2.64 (-12.30%)</td><td>2.18 (-9.18%)</td><td>0.45 <b>(+68.04%)</b></td><td>240.20 (+10.13%)</td><td>202.52 (+10.20%)</td><td>198.70 (+14.06%)</td><td>156.50 (-9.95%)</td><td>31.72 <b>(+64.35%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.02 (n/a)</td><td>2.87 (n/a)</td><td>3.01 (n/a)</td><td>2.40 (n/a)</td><td>0.27 (n/a)</td><td>218.10 (n/a)</td><td>183.78 (n/a)</td><td>174.20 (n/a)</td><td>173.80 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (-11.30%)</td><td>0.20 (+4.87%)</td><td>0.20 (+2.64%)</td><td>0.17 <b>(+67.72%)</b></td><td>0.04 <b>(-47.44%)</b></td><td>192.20 <b>(-40.37%)</b></td><td>164.18 (-13.78%)</td><td>167.20 (-2.56%)</td><td>125.30 (+12.78%)</td><td>28.29 <b>(-65.14%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>322.30 (n/a)</td><td>190.42 (n/a)</td><td>171.60 (n/a)</td><td>111.10 (n/a)</td><td>81.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (-2.71%)</td><td>0.22 (-4.17%)</td><td>0.21 (-2.48%)</td><td>0.13 (-19.03%)</td><td>0.07 (+16.95%)</td><td>252.00 <b>(+23.47%)</b></td><td>166.80 (+8.26%)</td><td>153.70 (+2.60%)</td><td>108.40 (+2.75%)</td><td>57.68 <b>(+48.01%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>204.10 (n/a)</td><td>154.08 (n/a)</td><td>149.80 (n/a)</td><td>105.50 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 <b>(+37.23%)</b></td><td>0.24 <b>(+35.97%)</b></td><td>0.25 <b>(+37.76%)</b></td><td>0.20 <b>(+29.03%)</b></td><td>0.04 <b>(+95.32%)</b></td><td>161.70 <b>(-22.48%)</b></td><td>137.86 <b>(-25.55%)</b></td><td>133.50 <b>(-27.41%)</b></td><td>113.20 <b>(-27.11%)</b></td><td>22.89 (+14.11%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>208.60 (n/a)</td><td>185.18 (n/a)</td><td>183.90 (n/a)</td><td>155.30 (n/a)</td><td>20.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (+10.75%)</td><td>0.24 (+16.62%)</td><td>0.25 <b>(+23.01%)</b></td><td>0.17 (+5.41%)</td><td>0.05 <b>(+22.12%)</b></td><td>197.30 (-5.14%)</td><td>142.28 (-13.43%)</td><td>128.60 (-18.71%)</td><td>110.80 (-9.70%)</td><td>34.24 (+6.74%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.00 (n/a)</td><td>164.36 (n/a)</td><td>158.20 (n/a)</td><td>122.70 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.45 (+7.14%)</td><td>0.39 (+3.13%)</td><td>0.44 <b>(+23.49%)</b></td><td>0.29 (-12.72%)</td><td>0.07 <b>(+83.30%)</b></td><td>223.30 (+14.57%)</td><td>174.52 (-0.69%)</td><td>149.90 (-19.02%)</td><td>145.40 (-6.62%)</td><td>36.64 <b>(+97.33%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.04 (n/a)</td><td>194.90 (n/a)</td><td>175.74 (n/a)</td><td>185.10 (n/a)</td><td>155.70 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+7.51%)</td><td>0.41 (-6.98%)</td><td>0.38 (-15.71%)</td><td>0.35 (+10.51%)</td><td>0.09 (+10.99%)</td><td>187.30 (-9.52%)</td><td>165.30 (+7.53%)</td><td>172.10 (+18.61%)</td><td>115.70 (-6.99%)</td><td>29.42 (-9.54%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>207.00 (n/a)</td><td>153.72 (n/a)</td><td>145.10 (n/a)</td><td>124.40 (n/a)</td><td>32.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.41 <b>(-27.66%)</b></td><td>0.37 (-11.17%)</td><td>0.39 (+0.66%)</td><td>0.30 (-6.69%)</td><td>0.05 <b>(-47.07%)</b></td><td>220.10 (+7.21%)</td><td>181.84 (+10.34%)</td><td>170.00 (-0.64%)</td><td>160.00 <b>(+38.17%)</b></td><td>26.19 (-19.48%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.57 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>205.30 (n/a)</td><td>164.80 (n/a)</td><td>171.10 (n/a)</td><td>115.80 (n/a)</td><td>32.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+14.09%)</td><td>0.41 (+4.91%)</td><td>0.40 (+8.52%)</td><td>0.34 <b>(+22.63%)</b></td><td>0.09 (+0.96%)</td><td>191.20 (-18.43%)</td><td>164.24 (-5.77%)</td><td>165.90 (-7.83%)</td><td>115.60 (-12.36%)</td><td>29.39 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>234.40 (n/a)</td><td>174.30 (n/a)</td><td>180.00 (n/a)</td><td>131.90 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.43 <b>(-28.77%)</b></td><td>0.38 (-10.68%)</td><td>0.40 (+13.49%)</td><td>0.32 (-3.07%)</td><td>0.05 <b>(-61.92%)</b></td><td>207.50 (+3.18%)</td><td>176.64 (+6.98%)</td><td>165.90 (-11.90%)</td><td>152.60 <b>(+40.39%)</b></td><td>22.40 <b>(-45.25%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.60 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.12 (n/a)</td><td>201.10 (n/a)</td><td>165.12 (n/a)</td><td>188.30 (n/a)</td><td>108.70 (n/a)</td><td>40.91 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.44 (-8.43%)</td><td>0.35 (-17.74%)</td><td>0.36 (-14.25%)</td><td>0.28 <b>(-25.93%)</b></td><td>0.06 <b>(+56.54%)</b></td><td>233.40 <b>(+34.99%)</b></td><td>189.10 <b>(+23.55%)</b></td><td>180.30 (+16.62%)</td><td>149.30 (+9.22%)</td><td>31.69 <b>(+131.51%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.04 (n/a)</td><td>172.90 (n/a)</td><td>153.06 (n/a)</td><td>154.60 (n/a)</td><td>136.70 (n/a)</td><td>13.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>1.12 (+3.03%)</td><td>0.78 (-3.28%)</td><td>0.72 (-4.66%)</td><td>0.58 (-6.00%)</td><td>0.22 <b>(+25.19%)</b></td><td>224.10 (+6.41%)</td><td>177.64 (+5.64%)</td><td>182.70 (+4.88%)</td><td>117.10 (-2.90%)</td><td>43.00 <b>(+32.83%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.09 (n/a)</td><td>0.81 (n/a)</td><td>0.75 (n/a)</td><td>0.62 (n/a)</td><td>0.17 (n/a)</td><td>210.60 (n/a)</td><td>168.16 (n/a)</td><td>174.20 (n/a)</td><td>120.60 (n/a)</td><td>32.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.12 (+10.46%)</td><td>0.82 (-2.73%)</td><td>0.75 (-11.80%)</td><td>0.51 (-17.11%)</td><td>0.25 <b>(+58.42%)</b></td><td>259.40 <b>(+20.65%)</b></td><td>173.04 (+8.00%)</td><td>174.80 (+13.43%)</td><td>116.70 (-9.46%)</td><td>56.79 <b>(+67.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.61 (n/a)</td><td>0.16 (n/a)</td><td>215.00 (n/a)</td><td>160.22 (n/a)</td><td>154.10 (n/a)</td><td>128.90 (n/a)</td><td>33.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.75 <b>(-25.84%)</b></td><td>0.66 <b>(-20.23%)</b></td><td>0.70 (-17.77%)</td><td>0.45 <b>(-28.46%)</b></td><td>0.12 <b>(-22.98%)</b></td><td>289.00 <b>(+39.75%)</b></td><td>205.14 <b>(+25.93%)</b></td><td>187.40 <b>(+21.61%)</b></td><td>173.70 <b>(+34.86%)</b></td><td>47.37 <b>(+49.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.02 (n/a)</td><td>0.83 (n/a)</td><td>0.85 (n/a)</td><td>0.63 (n/a)</td><td>0.15 (n/a)</td><td>206.80 (n/a)</td><td>162.90 (n/a)</td><td>154.10 (n/a)</td><td>128.80 (n/a)</td><td>31.62 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.08 (+11.42%)</td><td>0.84 (+10.19%)</td><td>0.71 (-5.09%)</td><td>0.68 (+8.35%)</td><td>0.20 <b>(+53.95%)</b></td><td>193.90 (-7.71%)</td><td>162.64 (-7.35%)</td><td>185.40 (+5.34%)</td><td>121.80 (-10.24%)</td><td>35.51 <b>(+27.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.97 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.13 (n/a)</td><td>210.10 (n/a)</td><td>175.54 (n/a)</td><td>176.00 (n/a)</td><td>135.70 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.82 (-16.23%)</td><td>0.75 (-8.13%)</td><td>0.79 (-1.09%)</td><td>0.62 (-7.98%)</td><td>0.08 <b>(-31.04%)</b></td><td>210.30 (+8.68%)</td><td>176.00 (+8.21%)</td><td>166.50 (+1.09%)</td><td>160.80 (+19.38%)</td><td>20.54 (-9.79%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.97 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.68 (n/a)</td><td>0.12 (n/a)</td><td>193.50 (n/a)</td><td>162.64 (n/a)</td><td>164.70 (n/a)</td><td>134.70 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.91 (-7.72%)</td><td>0.75 (-7.56%)</td><td>0.74 (-7.43%)</td><td>0.61 (-12.47%)</td><td>0.15 <b>(+21.75%)</b></td><td>216.40 (+14.26%)</td><td>179.28 (+9.66%)</td><td>177.30 (+8.04%)</td><td>144.10 (+8.35%)</td><td>34.73 <b>(+49.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.99 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.12 (n/a)</td><td>189.40 (n/a)</td><td>163.48 (n/a)</td><td>164.10 (n/a)</td><td>133.00 (n/a)</td><td>23.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.96 (+8.71%)</td><td>0.76 (+5.96%)</td><td>0.79 (+5.67%)</td><td>0.53 (+2.90%)</td><td>0.16 (+14.50%)</td><td>248.60 (-2.81%)</td><td>180.48 (-5.05%)</td><td>166.20 (-5.35%)</td><td>135.90 (-7.99%)</td><td>42.87 (+2.73%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.89 (n/a)</td><td>0.71 (n/a)</td><td>0.75 (n/a)</td><td>0.51 (n/a)</td><td>0.14 (n/a)</td><td>255.80 (n/a)</td><td>190.08 (n/a)</td><td>175.60 (n/a)</td><td>147.70 (n/a)</td><td>41.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.87 <b>(-30.80%)</b></td><td>0.68 <b>(-25.14%)</b></td><td>0.68 <b>(-20.51%)</b></td><td>0.48 <b>(-24.02%)</b></td><td>0.14 <b>(-45.20%)</b></td><td>271.50 <b>(+31.60%)</b></td><td>199.46 <b>(+30.35%)</b></td><td>193.20 <b>(+25.78%)</b></td><td>149.90 <b>(+44.55%)</b></td><td>44.25 (+7.66%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.26 (n/a)</td><td>0.91 (n/a)</td><td>0.85 (n/a)</td><td>0.64 (n/a)</td><td>0.25 (n/a)</td><td>206.30 (n/a)</td><td>153.02 (n/a)</td><td>153.60 (n/a)</td><td>103.70 (n/a)</td><td>41.10 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (-15.84%)</td><td>0.10 (-0.20%)</td><td>0.10 (+17.15%)</td><td>0.07 (+7.08%)</td><td>0.02 <b>(-28.18%)</b></td><td>229.80 (-6.62%)</td><td>176.14 (-2.37%)</td><td>160.90 (-14.60%)</td><td>131.10 (+18.86%)</td><td>41.96 (-15.68%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>246.10 (n/a)</td><td>180.42 (n/a)</td><td>188.40 (n/a)</td><td>110.30 (n/a)</td><td>49.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (+5.28%)</td><td>0.10 (-6.35%)</td><td>0.10 (-9.66%)</td><td>0.07 (-18.86%)</td><td>0.02 <b>(+61.29%)</b></td><td>226.90 <b>(+23.25%)</b></td><td>174.48 (+9.64%)</td><td>170.10 (+10.67%)</td><td>128.50 (-5.03%)</td><td>38.92 <b>(+86.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>159.14 (n/a)</td><td>153.70 (n/a)</td><td>135.30 (n/a)</td><td>20.83 (n/a)</td>
</tr>
</tbody>
</table>


</details>
