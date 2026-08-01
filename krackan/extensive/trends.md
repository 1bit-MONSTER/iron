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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (+7.95%)</td><td>0.04 (+7.40%)</td><td>0.04 <b>(+20.71%)</b></td><td>0.03 (-18.70%)</td><td>0.01 <b>(+23.90%)</b></td><td>239.00 <b>(+23.01%)</b></td><td>163.52 (-4.40%)</td><td>156.80 (-17.12%)</td><td>107.30 (-7.34%)</td><td>47.54 <b>(+43.50%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>171.04 (n/a)</td><td>189.20 (n/a)</td><td>115.80 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (-12.87%)</td><td>0.03 (-7.32%)</td><td>0.03 (-7.65%)</td><td>0.03 (-1.63%)</td><td>0.00 <b>(-35.20%)</b></td><td>203.50 (+1.65%)</td><td>178.60 (+6.31%)</td><td>187.20 (+8.27%)</td><td>145.60 (+14.83%)</td><td>22.90 <b>(-25.62%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>168.00 (n/a)</td><td>172.90 (n/a)</td><td>126.80 (n/a)</td><td>30.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (-12.14%)</td><td>0.04 (-6.39%)</td><td>0.03 (-15.72%)</td><td>0.03 (+6.80%)</td><td>0.00 <b>(-29.21%)</b></td><td>191.60 (-6.35%)</td><td>173.38 (+5.73%)</td><td>184.50 (+18.65%)</td><td>148.20 (+13.82%)</td><td>20.85 <b>(-25.02%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>163.98 (n/a)</td><td>155.50 (n/a)</td><td>130.20 (n/a)</td><td>27.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (+9.97%)</td><td>0.04 (+12.23%)</td><td>0.04 (+16.60%)</td><td>0.03 (+13.63%)</td><td>0.00 (-1.57%)</td><td>180.20 (-11.97%)</td><td>157.02 (-11.10%)</td><td>153.00 (-14.24%)</td><td>138.00 (-9.09%)</td><td>16.11 <b>(-20.45%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.70 (n/a)</td><td>176.62 (n/a)</td><td>178.40 (n/a)</td><td>151.80 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 <b>(+45.44%)</b></td><td>0.03 (+11.18%)</td><td>0.03 (+6.00%)</td><td>0.02 (-19.95%)</td><td>0.01 <b>(+146.24%)</b></td><td>319.50 <b>(+24.90%)</b></td><td>206.18 (-3.51%)</td><td>190.80 (-5.64%)</td><td>124.90 <b>(-31.26%)</b></td><td>70.62 <b>(+113.63%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.80 (n/a)</td><td>213.68 (n/a)</td><td>202.20 (n/a)</td><td>181.70 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-17.11%)</td><td>0.03 (-9.76%)</td><td>0.03 (-6.55%)</td><td>0.02 <b>(-22.28%)</b></td><td>0.01 (-4.52%)</td><td>357.10 <b>(+28.68%)</b></td><td>223.56 (+13.08%)</td><td>188.50 (+6.98%)</td><td>176.10 <b>(+20.62%)</b></td><td>76.42 <b>(+48.11%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>277.50 (n/a)</td><td>197.70 (n/a)</td><td>176.20 (n/a)</td><td>146.00 (n/a)</td><td>51.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (+3.36%)</td><td>0.03 (+0.73%)</td><td>0.03 (+5.77%)</td><td>0.03 (+7.67%)</td><td>0.01 (+6.46%)</td><td>237.90 (-7.11%)</td><td>188.78 (-0.64%)</td><td>179.10 (-5.44%)</td><td>138.10 (-3.29%)</td><td>40.12 (-4.37%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.10 (n/a)</td><td>190.00 (n/a)</td><td>189.40 (n/a)</td><td>142.80 (n/a)</td><td>41.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 <b>(+24.11%)</b></td><td>0.03 (+19.97%)</td><td>0.04 <b>(+27.70%)</b></td><td>0.03 (+5.89%)</td><td>0.00 <b>(+150.17%)</b></td><td>212.50 (-5.56%)</td><td>179.94 (-15.70%)</td><td>169.10 <b>(-21.71%)</b></td><td>155.10 (-19.39%)</td><td>24.42 <b>(+93.67%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>225.00 (n/a)</td><td>213.44 (n/a)</td><td>216.00 (n/a)</td><td>192.40 (n/a)</td><td>12.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (+2.53%)</td><td>0.07 (+1.44%)</td><td>0.07 (-5.37%)</td><td>0.05 (-6.66%)</td><td>0.02 (+18.36%)</td><td>253.70 (+7.14%)</td><td>175.92 (-0.07%)</td><td>165.80 (+5.67%)</td><td>142.00 (-2.47%)</td><td>45.86 <b>(+22.98%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.80 (n/a)</td><td>176.04 (n/a)</td><td>156.90 (n/a)</td><td>145.60 (n/a)</td><td>37.29 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (-5.36%)</td><td>0.07 (-11.31%)</td><td>0.07 (-14.02%)</td><td>0.05 (-12.75%)</td><td>0.01 <b>(+21.83%)</b></td><td>226.90 (+14.65%)</td><td>185.84 (+14.19%)</td><td>185.90 (+16.26%)</td><td>142.70 (+5.70%)</td><td>34.55 <b>(+47.09%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>162.74 (n/a)</td><td>159.90 (n/a)</td><td>135.00 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (+11.40%)</td><td>0.07 (+2.23%)</td><td>0.07 (+2.86%)</td><td>0.05 (-8.97%)</td><td>0.01 <b>(+34.94%)</b></td><td>241.60 (+9.87%)</td><td>186.42 (-0.62%)</td><td>186.70 (-2.81%)</td><td>137.60 (-10.24%)</td><td>39.68 <b>(+33.13%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>187.58 (n/a)</td><td>192.10 (n/a)</td><td>153.30 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (-5.68%)</td><td>0.06 (-13.25%)</td><td>0.06 (-10.29%)</td><td>0.05 <b>(-24.77%)</b></td><td>0.01 <b>(+33.17%)</b></td><td>248.40 <b>(+32.98%)</b></td><td>205.44 (+17.34%)</td><td>205.30 (+11.45%)</td><td>147.30 (+5.97%)</td><td>37.30 <b>(+83.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>175.08 (n/a)</td><td>184.20 (n/a)</td><td>139.00 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (+4.92%)</td><td>0.07 (-2.60%)</td><td>0.07 (+4.23%)</td><td>0.05 (-7.43%)</td><td>0.01 <b>(+20.62%)</b></td><td>232.10 (+8.05%)</td><td>193.08 (+3.54%)</td><td>187.00 (-4.05%)</td><td>148.00 (-4.64%)</td><td>33.08 <b>(+25.90%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>186.48 (n/a)</td><td>194.90 (n/a)</td><td>155.20 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (+15.26%)</td><td>0.07 (-3.37%)</td><td>0.06 (-13.25%)</td><td>0.05 <b>(-22.34%)</b></td><td>0.02 <b>(+126.92%)</b></td><td>249.80 <b>(+28.76%)</b></td><td>186.94 (+8.35%)</td><td>195.40 (+15.28%)</td><td>133.20 (-13.22%)</td><td>48.65 <b>(+146.48%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>172.54 (n/a)</td><td>169.50 (n/a)</td><td>153.50 (n/a)</td><td>19.74 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 <b>(-25.15%)</b></td><td>0.06 (-5.98%)</td><td>0.06 (-0.93%)</td><td>0.05 (+7.58%)</td><td>0.01 <b>(-51.70%)</b></td><td>250.70 (-7.04%)</td><td>201.16 (+1.46%)</td><td>204.10 (+0.94%)</td><td>161.50 <b>(+33.58%)</b></td><td>33.67 <b>(-37.39%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>269.70 (n/a)</td><td>198.26 (n/a)</td><td>202.20 (n/a)</td><td>120.90 (n/a)</td><td>53.78 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (+10.21%)</td><td>0.07 (+11.17%)</td><td>0.06 (+2.88%)</td><td>0.06 <b>(+40.99%)</b></td><td>0.01 (-9.27%)</td><td>221.70 <b>(-29.08%)</b></td><td>184.84 (-12.36%)</td><td>189.90 (-2.81%)</td><td>143.50 (-9.29%)</td><td>34.66 <b>(-43.04%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>312.60 (n/a)</td><td>210.92 (n/a)</td><td>195.40 (n/a)</td><td>158.20 (n/a)</td><td>60.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (+13.29%)</td><td>0.15 (+10.75%)</td><td>0.15 (+0.53%)</td><td>0.12 (+19.40%)</td><td>0.02 (+1.20%)</td><td>204.70 (-16.24%)</td><td>167.46 (-10.33%)</td><td>166.30 (-0.54%)</td><td>136.60 (-11.76%)</td><td>27.19 <b>(-25.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>244.40 (n/a)</td><td>186.76 (n/a)</td><td>167.20 (n/a)</td><td>154.80 (n/a)</td><td>36.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (-3.66%)</td><td>0.15 (+7.04%)</td><td>0.15 (+8.05%)</td><td>0.10 (-12.26%)</td><td>0.04 (+9.12%)</td><td>239.40 (+13.95%)</td><td>168.52 (-5.35%)</td><td>166.40 (-7.40%)</td><td>129.80 (+3.84%)</td><td>44.28 <b>(+25.93%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>210.10 (n/a)</td><td>178.04 (n/a)</td><td>179.70 (n/a)</td><td>125.00 (n/a)</td><td>35.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 <b>(-20.87%)</b></td><td>0.13 (-7.35%)</td><td>0.13 (-2.00%)</td><td>0.12 (-5.26%)</td><td>0.01 <b>(-42.36%)</b></td><td>212.90 (+5.50%)</td><td>189.58 (+6.78%)</td><td>188.20 (+2.06%)</td><td>169.50 <b>(+26.40%)</b></td><td>20.20 <b>(-20.78%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>201.80 (n/a)</td><td>177.54 (n/a)</td><td>184.40 (n/a)</td><td>134.10 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (-4.00%)</td><td>0.14 (-0.15%)</td><td>0.14 (-3.75%)</td><td>0.12 <b>(+36.96%)</b></td><td>0.03 <b>(-38.63%)</b></td><td>213.60 <b>(-26.97%)</b></td><td>179.20 (-6.45%)</td><td>178.40 (+3.90%)</td><td>130.50 (+4.15%)</td><td>31.75 <b>(-53.98%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>292.50 (n/a)</td><td>191.56 (n/a)</td><td>171.70 (n/a)</td><td>125.30 (n/a)</td><td>68.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (+8.34%)</td><td>0.14 (-8.46%)</td><td>0.12 <b>(-22.07%)</b></td><td>0.11 (+2.45%)</td><td>0.03 <b>(+24.20%)</b></td><td>226.80 (-2.37%)</td><td>187.88 (+10.31%)</td><td>203.30 <b>(+28.35%)</b></td><td>138.80 (-7.71%)</td><td>38.40 (+9.92%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>232.30 (n/a)</td><td>170.32 (n/a)</td><td>158.40 (n/a)</td><td>150.40 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 (+9.16%)</td><td>0.13 (-6.58%)</td><td>0.13 (-8.71%)</td><td>0.07 <b>(-40.14%)</b></td><td>0.04 <b>(+139.99%)</b></td><td>368.60 <b>(+67.01%)</b></td><td>216.46 (+17.55%)</td><td>196.50 (+9.53%)</td><td>142.50 (-8.36%)</td><td>89.41 <b>(+278.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.70 (n/a)</td><td>184.14 (n/a)</td><td>179.40 (n/a)</td><td>155.50 (n/a)</td><td>23.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (-1.72%)</td><td>0.13 (-2.79%)</td><td>0.14 (-1.46%)</td><td>0.11 <b>(+30.39%)</b></td><td>0.03 <b>(-29.17%)</b></td><td>231.30 <b>(-23.33%)</b></td><td>189.38 (-1.74%)</td><td>181.40 (+1.51%)</td><td>140.10 (+1.74%)</td><td>36.33 <b>(-44.76%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>301.70 (n/a)</td><td>192.74 (n/a)</td><td>178.70 (n/a)</td><td>137.70 (n/a)</td><td>65.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (+8.45%)</td><td>0.12 (+11.37%)</td><td>0.12 (+11.76%)</td><td>0.07 (-4.31%)</td><td>0.03 (+14.88%)</td><td>339.00 (+4.50%)</td><td>218.40 (-8.85%)</td><td>199.50 (-10.54%)</td><td>174.60 (-7.77%)</td><td>68.50 (+17.72%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>324.40 (n/a)</td><td>239.60 (n/a)</td><td>223.00 (n/a)</td><td>189.30 (n/a)</td><td>58.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.45 (+19.37%)</td><td>0.37 (+14.66%)</td><td>0.36 (+15.49%)</td><td>0.32 (+17.66%)</td><td>0.05 <b>(+26.66%)</b></td><td>155.00 (-15.02%)</td><td>135.90 (-12.65%)</td><td>137.70 (-13.40%)</td><td>109.60 (-16.27%)</td><td>17.46 (-10.28%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>182.40 (n/a)</td><td>155.58 (n/a)</td><td>159.00 (n/a)</td><td>130.90 (n/a)</td><td>19.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.43 (+1.10%)</td><td>0.33 (+1.72%)</td><td>0.32 (+1.90%)</td><td>0.28 (+10.79%)</td><td>0.06 (-10.84%)</td><td>176.00 (-9.74%)</td><td>154.62 (-2.67%)</td><td>156.00 (-1.83%)</td><td>113.90 (-1.04%)</td><td>24.95 <b>(-21.46%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>195.00 (n/a)</td><td>158.86 (n/a)</td><td>158.90 (n/a)</td><td>115.10 (n/a)</td><td>31.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.44 <b>(+48.57%)</b></td><td>0.34 <b>(+23.58%)</b></td><td>0.33 <b>(+20.91%)</b></td><td>0.26 (+3.66%)</td><td>0.07 <b>(+274.70%)</b></td><td>192.30 (-3.51%)</td><td>151.20 (-16.52%)</td><td>150.00 (-17.31%)</td><td>112.60 <b>(-32.70%)</b></td><td>31.25 <b>(+143.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>199.30 (n/a)</td><td>181.12 (n/a)</td><td>181.40 (n/a)</td><td>167.30 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.39 (+5.80%)</td><td>0.33 (+2.59%)</td><td>0.31 (-1.21%)</td><td>0.28 (+0.94%)</td><td>0.04 <b>(+23.89%)</b></td><td>177.70 (-0.95%)</td><td>153.16 (-2.11%)</td><td>159.20 (+1.21%)</td><td>125.10 (-5.51%)</td><td>20.01 (+15.50%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>179.40 (n/a)</td><td>156.46 (n/a)</td><td>157.30 (n/a)</td><td>132.40 (n/a)</td><td>17.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.33 (-6.83%)</td><td>0.28 (-2.83%)</td><td>0.30 (-5.31%)</td><td>0.19 (-8.37%)</td><td>0.05 (-13.54%)</td><td>253.20 (+9.14%)</td><td>180.38 (+2.49%)</td><td>164.70 (+5.58%)</td><td>148.00 (+7.32%)</td><td>42.42 (+3.63%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>232.00 (n/a)</td><td>176.00 (n/a)</td><td>156.00 (n/a)</td><td>137.90 (n/a)</td><td>40.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.34 (-5.99%)</td><td>0.30 (+3.73%)</td><td>0.29 (-1.68%)</td><td>0.28 (+17.31%)</td><td>0.03 <b>(-42.24%)</b></td><td>177.80 (-14.77%)</td><td>165.86 (-4.84%)</td><td>172.00 (+1.71%)</td><td>146.30 (+6.40%)</td><td>13.97 <b>(-46.78%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>208.60 (n/a)</td><td>174.30 (n/a)</td><td>169.10 (n/a)</td><td>137.50 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.33 (-2.92%)</td><td>0.26 (-4.26%)</td><td>0.23 (-4.53%)</td><td>0.20 (-13.56%)</td><td>0.06 <b>(+35.31%)</b></td><td>245.30 (+15.71%)</td><td>201.02 (+6.88%)</td><td>210.20 (+4.73%)</td><td>148.80 (+3.05%)</td><td>44.56 <b>(+64.32%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>212.00 (n/a)</td><td>188.08 (n/a)</td><td>200.70 (n/a)</td><td>144.40 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.32 (+10.13%)</td><td>0.25 (-10.20%)</td><td>0.23 (-16.99%)</td><td>0.20 <b>(-23.76%)</b></td><td>0.05 <b>(+362.30%)</b></td><td>247.80 <b>(+31.18%)</b></td><td>206.98 (+15.39%)</td><td>216.70 <b>(+20.46%)</b></td><td>152.50 (-9.17%)</td><td>42.57 <b>(+462.85%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>179.38 (n/a)</td><td>179.90 (n/a)</td><td>167.90 (n/a)</td><td>7.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (-1.05%)</td><td>0.02 (+14.65%)</td><td>0.02 <b>(+23.36%)</b></td><td>0.01 (-0.86%)</td><td>0.00 (-7.59%)</td><td>187.40 (+0.86%)</td><td>135.06 (-12.95%)</td><td>127.90 (-18.95%)</td><td>108.30 (+1.03%)</td><td>30.45 (+2.34%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>185.80 (n/a)</td><td>155.16 (n/a)</td><td>157.80 (n/a)</td><td>107.20 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (+18.99%)</td><td>0.02 (+11.38%)</td><td>0.02 (+14.38%)</td><td>0.01 (-0.98%)</td><td>0.00 <b>(+85.69%)</b></td><td>190.60 (+1.01%)</td><td>154.04 (-7.67%)</td><td>150.90 (-12.57%)</td><td>112.00 (-15.98%)</td><td>34.29 <b>(+66.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>188.70 (n/a)</td><td>166.84 (n/a)</td><td>172.60 (n/a)</td><td>133.30 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 <b>(+37.95%)</b></td><td>0.02 <b>(+29.62%)</b></td><td>0.02 (+16.99%)</td><td>0.01 <b>(+23.65%)</b></td><td>0.00 <b>(+52.88%)</b></td><td>175.20 (-19.15%)</td><td>139.40 <b>(-22.28%)</b></td><td>143.50 (-14.53%)</td><td>107.90 <b>(-27.49%)</b></td><td>27.04 (-12.77%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>179.36 (n/a)</td><td>167.90 (n/a)</td><td>148.80 (n/a)</td><td>31.00 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (+10.40%)</td><td>0.02 (+10.04%)</td><td>0.01 (+0.40%)</td><td>0.01 <b>(+21.76%)</b></td><td>0.00 (-8.84%)</td><td>181.70 (-17.86%)</td><td>168.72 (-9.47%)</td><td>176.40 (-0.40%)</td><td>151.80 (-9.43%)</td><td>14.50 <b>(-32.93%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>221.20 (n/a)</td><td>186.36 (n/a)</td><td>177.10 (n/a)</td><td>167.60 (n/a)</td><td>21.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (-13.23%)</td><td>0.02 (+13.60%)</td><td>0.02 <b>(+28.34%)</b></td><td>0.01 <b>(+29.84%)</b></td><td>0.00 <b>(-55.85%)</b></td><td>180.40 <b>(-22.97%)</b></td><td>161.42 (-16.11%)</td><td>163.10 <b>(-22.07%)</b></td><td>134.80 (+15.21%)</td><td>18.65 <b>(-58.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>234.20 (n/a)</td><td>192.42 (n/a)</td><td>209.30 (n/a)</td><td>117.00 (n/a)</td><td>44.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (-13.61%)</td><td>0.01 (-12.56%)</td><td>0.01 (-9.98%)</td><td>0.01 (-13.51%)</td><td>0.00 (-18.46%)</td><td>216.40 (+15.60%)</td><td>189.88 (+14.14%)</td><td>195.10 (+11.04%)</td><td>152.50 (+15.71%)</td><td>23.36 (+8.08%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>187.20 (n/a)</td><td>166.36 (n/a)</td><td>175.70 (n/a)</td><td>131.80 (n/a)</td><td>21.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 <b>(+20.76%)</b></td><td>0.02 <b>(+20.60%)</b></td><td>0.02 (+16.24%)</td><td>0.02 <b>(+31.78%)</b></td><td>0.00 (-13.30%)</td><td>170.70 <b>(-24.10%)</b></td><td>153.42 (-17.53%)</td><td>151.50 (-13.97%)</td><td>141.20 (-17.18%)</td><td>11.97 <b>(-46.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>224.90 (n/a)</td><td>186.04 (n/a)</td><td>176.10 (n/a)</td><td>170.50 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 <b>(+20.97%)</b></td><td>0.01 (+15.53%)</td><td>0.01 (+16.05%)</td><td>0.01 (+9.36%)</td><td>0.00 <b>(+65.49%)</b></td><td>213.30 (-8.57%)</td><td>190.80 (-13.22%)</td><td>190.00 (-13.79%)</td><td>170.80 (-17.37%)</td><td>15.10 <b>(+25.71%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.30 (n/a)</td><td>219.86 (n/a)</td><td>220.40 (n/a)</td><td>206.70 (n/a)</td><td>12.01 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 <b>(+26.02%)</b></td><td>0.04 <b>(+20.14%)</b></td><td>0.04 <b>(+30.68%)</b></td><td>0.03 (+11.09%)</td><td>0.01 <b>(+92.33%)</b></td><td>189.90 (-10.00%)</td><td>152.46 (-15.10%)</td><td>135.20 <b>(-23.49%)</b></td><td>125.00 <b>(-20.63%)</b></td><td>31.04 <b>(+40.10%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>179.58 (n/a)</td><td>176.70 (n/a)</td><td>157.50 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (+14.64%)</td><td>0.04 <b>(+31.99%)</b></td><td>0.04 (+12.18%)</td><td>0.03 <b>(+131.27%)</b></td><td>0.00 <b>(-70.11%)</b></td><td>160.10 <b>(-56.76%)</b></td><td>147.50 <b>(-31.93%)</b></td><td>146.60 (-10.83%)</td><td>135.20 (-12.77%)</td><td>10.59 <b>(-88.48%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>370.30 (n/a)</td><td>216.70 (n/a)</td><td>164.40 (n/a)</td><td>155.00 (n/a)</td><td>91.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 <b>(+22.13%)</b></td><td>0.03 (+17.44%)</td><td>0.03 (+8.14%)</td><td>0.03 <b>(+28.70%)</b></td><td>0.00 (-16.60%)</td><td>177.30 <b>(-22.27%)</b></td><td>154.44 (-15.99%)</td><td>152.30 (-7.53%)</td><td>128.90 (-18.11%)</td><td>17.61 <b>(-46.77%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.10 (n/a)</td><td>183.84 (n/a)</td><td>164.70 (n/a)</td><td>157.40 (n/a)</td><td>33.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (+17.68%)</td><td>0.03 (-0.13%)</td><td>0.03 (+6.58%)</td><td>0.01 <b>(-45.79%)</b></td><td>0.01 <b>(+183.87%)</b></td><td>409.00 <b>(+84.48%)</b></td><td>207.74 (+15.78%)</td><td>157.60 (-6.19%)</td><td>136.40 (-15.02%)</td><td>114.10 <b>(+362.87%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.70 (n/a)</td><td>179.42 (n/a)</td><td>168.00 (n/a)</td><td>160.50 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (+17.87%)</td><td>0.04 <b>(+22.96%)</b></td><td>0.04 <b>(+31.01%)</b></td><td>0.03 (+15.43%)</td><td>0.00 <b>(+35.64%)</b></td><td>168.70 (-13.35%)</td><td>147.64 (-18.41%)</td><td>146.20 <b>(-23.70%)</b></td><td>128.20 (-15.16%)</td><td>18.70 (-1.24%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.70 (n/a)</td><td>180.96 (n/a)</td><td>191.60 (n/a)</td><td>151.10 (n/a)</td><td>18.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+7.61%)</td><td>0.03 (-1.91%)</td><td>0.03 (+0.47%)</td><td>0.02 <b>(-24.36%)</b></td><td>0.00 <b>(+234.48%)</b></td><td>283.10 <b>(+32.23%)</b></td><td>211.30 (+5.18%)</td><td>203.80 (-0.44%)</td><td>171.90 (-7.08%)</td><td>45.55 <b>(+307.68%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>200.90 (n/a)</td><td>204.70 (n/a)</td><td>185.00 (n/a)</td><td>11.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+2.95%)</td><td>0.03 (+4.85%)</td><td>0.03 (+4.95%)</td><td>0.03 (+6.42%)</td><td>0.00 (-2.54%)</td><td>208.70 (-6.03%)</td><td>187.90 (-4.75%)</td><td>194.50 (-4.75%)</td><td>162.60 (-2.87%)</td><td>18.61 (-10.65%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.10 (n/a)</td><td>197.26 (n/a)</td><td>204.20 (n/a)</td><td>167.40 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 <b>(+23.38%)</b></td><td>0.03 <b>(+27.02%)</b></td><td>0.03 <b>(+21.65%)</b></td><td>0.02 <b>(+63.10%)</b></td><td>0.00 <b>(-42.80%)</b></td><td>210.20 <b>(-38.68%)</b></td><td>191.28 <b>(-23.21%)</b></td><td>191.60 (-17.77%)</td><td>170.40 (-18.93%)</td><td>14.40 <b>(-72.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>342.80 (n/a)</td><td>249.08 (n/a)</td><td>233.00 (n/a)</td><td>210.20 (n/a)</td><td>53.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (-13.36%)</td><td>0.07 (-5.51%)</td><td>0.07 (-14.79%)</td><td>0.06 <b>(+23.15%)</b></td><td>0.00 <b>(-75.35%)</b></td><td>166.50 (-18.78%)</td><td>157.12 (+2.15%)</td><td>153.90 (+17.39%)</td><td>147.10 (+15.37%)</td><td>8.39 <b>(-76.07%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>153.82 (n/a)</td><td>131.10 (n/a)</td><td>127.50 (n/a)</td><td>35.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (+3.09%)</td><td>0.06 (-8.80%)</td><td>0.06 (-1.72%)</td><td>0.04 <b>(-33.60%)</b></td><td>0.01 <b>(+117.34%)</b></td><td>271.30 <b>(+50.55%)</b></td><td>190.34 (+14.54%)</td><td>175.20 (+1.74%)</td><td>139.80 (-2.98%)</td><td>51.07 <b>(+220.55%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>180.20 (n/a)</td><td>166.18 (n/a)</td><td>172.20 (n/a)</td><td>144.10 (n/a)</td><td>15.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+2.33%)</td><td>0.07 (+10.69%)</td><td>0.07 (+17.38%)</td><td>0.06 (+10.07%)</td><td>0.01 <b>(-20.88%)</b></td><td>176.10 (-9.13%)</td><td>156.12 (-10.10%)</td><td>148.30 (-14.82%)</td><td>145.70 (-2.28%)</td><td>13.65 <b>(-31.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>173.66 (n/a)</td><td>174.10 (n/a)</td><td>149.10 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 <b>(+29.68%)</b></td><td>0.06 <b>(+20.79%)</b></td><td>0.06 (+11.14%)</td><td>0.05 (+14.48%)</td><td>0.01 <b>(+115.70%)</b></td><td>195.10 (-12.67%)</td><td>167.02 (-16.47%)</td><td>171.50 (-10.02%)</td><td>145.30 <b>(-22.92%)</b></td><td>21.59 <b>(+41.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>199.96 (n/a)</td><td>190.60 (n/a)</td><td>188.50 (n/a)</td><td>15.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (-8.72%)</td><td>0.06 (+0.49%)</td><td>0.06 (+13.62%)</td><td>0.05 (-2.36%)</td><td>0.01 (-16.54%)</td><td>216.30 (+2.41%)</td><td>177.88 (-0.91%)</td><td>168.60 (-11.96%)</td><td>153.20 (+9.59%)</td><td>26.44 (-5.51%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>179.52 (n/a)</td><td>191.50 (n/a)</td><td>139.80 (n/a)</td><td>27.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+6.09%)</td><td>0.06 (+9.42%)</td><td>0.06 (+12.53%)</td><td>0.05 (+9.74%)</td><td>0.00 (-13.04%)</td><td>197.30 (-8.87%)</td><td>173.38 (-8.85%)</td><td>172.50 (-11.13%)</td><td>158.20 (-5.72%)</td><td>14.70 <b>(-23.78%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>190.22 (n/a)</td><td>194.10 (n/a)</td><td>167.80 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (-9.93%)</td><td>0.06 (-3.91%)</td><td>0.06 (+4.03%)</td><td>0.05 (-4.91%)</td><td>0.01 (-14.09%)</td><td>226.00 (+5.17%)</td><td>184.22 (+3.74%)</td><td>177.00 (-3.91%)</td><td>133.50 (+11.06%)</td><td>37.34 (+6.86%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>177.58 (n/a)</td><td>184.20 (n/a)</td><td>120.20 (n/a)</td><td>34.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 <b>(-33.28%)</b></td><td>0.05 (-17.85%)</td><td>0.05 (-17.57%)</td><td>0.04 (-11.96%)</td><td>0.00 <b>(-68.59%)</b></td><td>260.30 (+13.62%)</td><td>228.12 (+18.64%)</td><td>226.30 <b>(+21.34%)</b></td><td>208.40 <b>(+49.93%)</b></td><td>19.47 <b>(-45.60%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>192.28 (n/a)</td><td>186.50 (n/a)</td><td>139.00 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (-0.69%)</td><td>0.12 <b>(+20.09%)</b></td><td>0.13 <b>(+30.04%)</b></td><td>0.11 <b>(+33.23%)</b></td><td>0.01 <b>(-61.21%)</b></td><td>183.00 <b>(-24.94%)</b></td><td>171.66 (-18.46%)</td><td>167.10 <b>(-23.10%)</b></td><td>162.90 (+0.74%)</td><td>10.08 <b>(-71.00%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>243.80 (n/a)</td><td>210.52 (n/a)</td><td>217.30 (n/a)</td><td>161.70 (n/a)</td><td>34.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (-10.21%)</td><td>0.12 (-7.68%)</td><td>0.11 (-4.58%)</td><td>0.09 (-10.48%)</td><td>0.04 (-12.77%)</td><td>233.00 (+11.70%)</td><td>181.42 (+7.83%)</td><td>192.60 (+4.79%)</td><td>114.90 (+11.34%)</td><td>46.87 (+7.13%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>208.60 (n/a)</td><td>168.24 (n/a)</td><td>183.80 (n/a)</td><td>103.20 (n/a)</td><td>43.75 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 <b>(-21.59%)</b></td><td>0.12 (-10.28%)</td><td>0.12 (-8.40%)</td><td>0.11 (+1.63%)</td><td>0.01 <b>(-66.75%)</b></td><td>194.10 (-1.62%)</td><td>174.14 (+8.96%)</td><td>170.40 (+9.16%)</td><td>161.50 <b>(+27.47%)</b></td><td>12.19 <b>(-57.85%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>197.30 (n/a)</td><td>159.82 (n/a)</td><td>156.10 (n/a)</td><td>126.70 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (+6.36%)</td><td>0.13 (-4.28%)</td><td>0.12 (-15.44%)</td><td>0.10 (+1.15%)</td><td>0.04 (+9.97%)</td><td>203.00 (-1.12%)</td><td>165.56 (+5.12%)</td><td>178.70 (+18.27%)</td><td>106.40 (-6.01%)</td><td>41.09 (+2.11%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>205.30 (n/a)</td><td>157.50 (n/a)</td><td>151.10 (n/a)</td><td>113.20 (n/a)</td><td>40.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+13.28%)</td><td>0.12 (+19.80%)</td><td>0.13 <b>(+26.26%)</b></td><td>0.10 (+12.48%)</td><td>0.01 <b>(+27.37%)</b></td><td>203.80 (-11.12%)</td><td>171.86 (-16.37%)</td><td>165.40 <b>(-20.79%)</b></td><td>160.10 (-11.69%)</td><td>18.07 (+1.76%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>205.50 (n/a)</td><td>208.80 (n/a)</td><td>181.30 (n/a)</td><td>17.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (-19.27%)</td><td>0.12 (-12.46%)</td><td>0.12 (-8.53%)</td><td>0.09 (-3.35%)</td><td>0.02 <b>(-38.94%)</b></td><td>228.90 (+3.43%)</td><td>184.80 (+10.92%)</td><td>173.30 (+9.34%)</td><td>144.30 <b>(+23.86%)</b></td><td>34.65 <b>(-21.66%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>221.30 (n/a)</td><td>166.60 (n/a)</td><td>158.50 (n/a)</td><td>116.50 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (-14.01%)</td><td>0.12 (-10.51%)</td><td>0.12 (-13.94%)</td><td>0.10 (-0.92%)</td><td>0.01 <b>(-33.90%)</b></td><td>202.80 (+0.95%)</td><td>173.02 (+10.60%)</td><td>174.50 (+16.18%)</td><td>151.90 (+16.31%)</td><td>20.14 <b>(-24.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>200.90 (n/a)</td><td>156.44 (n/a)</td><td>150.20 (n/a)</td><td>130.60 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (-0.43%)</td><td>0.11 (+7.20%)</td><td>0.11 (+18.60%)</td><td>0.08 (+0.31%)</td><td>0.01 (-7.31%)</td><td>250.80 (-0.32%)</td><td>199.48 (-6.98%)</td><td>188.00 (-15.70%)</td><td>174.30 (+0.40%)</td><td>31.30 (-6.10%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>251.60 (n/a)</td><td>214.44 (n/a)</td><td>223.00 (n/a)</td><td>173.60 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>227.80 (n/a)</td><td>190.70 (n/a)</td><td>191.20 (n/a)</td><td>165.30 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>200.60 (n/a)</td><td>206.40 (n/a)</td><td>147.10 (n/a)</td><td>36.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>218.10 (n/a)</td><td>191.82 (n/a)</td><td>202.00 (n/a)</td><td>161.90 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>291.90 (n/a)</td><td>212.56 (n/a)</td><td>197.40 (n/a)</td><td>167.00 (n/a)</td><td>47.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>169.50 (n/a)</td><td>180.10 (n/a)</td><td>128.60 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>203.84 (n/a)</td><td>207.00 (n/a)</td><td>173.50 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>283.60 (n/a)</td><td>198.34 (n/a)</td><td>183.80 (n/a)</td><td>169.50 (n/a)</td><td>48.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>325.90 (n/a)</td><td>234.30 (n/a)</td><td>208.10 (n/a)</td><td>203.00 (n/a)</td><td>52.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>181.82 (n/a)</td><td>184.00 (n/a)</td><td>165.00 (n/a)</td><td>10.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>360.20 (n/a)</td><td>233.00 (n/a)</td><td>213.00 (n/a)</td><td>175.70 (n/a)</td><td>72.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>338.90 (n/a)</td><td>226.06 (n/a)</td><td>186.60 (n/a)</td><td>181.40 (n/a)</td><td>67.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>253.10 (n/a)</td><td>203.72 (n/a)</td><td>199.70 (n/a)</td><td>158.00 (n/a)</td><td>35.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.28 <b>(-23.71%)</b></td><td>0.25 (-12.47%)</td><td>0.24 (-12.11%)</td><td>0.23 (+0.65%)</td><td>0.02 <b>(-59.12%)</b></td><td>209.40 (-0.66%)</td><td>197.28 (+12.18%)</td><td>205.80 (+13.76%)</td><td>173.60 <b>(+31.02%)</b></td><td>15.79 <b>(-44.85%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>210.80 (n/a)</td><td>175.86 (n/a)</td><td>180.90 (n/a)</td><td>132.50 (n/a)</td><td>28.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>212.60 (n/a)</td><td>196.16 (n/a)</td><td>202.10 (n/a)</td><td>176.60 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>286.40 (n/a)</td><td>227.00 (n/a)</td><td>219.00 (n/a)</td><td>192.30 (n/a)</td><td>35.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>223.30 (n/a)</td><td>208.98 (n/a)</td><td>215.50 (n/a)</td><td>188.30 (n/a)</td><td>13.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>259.70 (n/a)</td><td>202.14 (n/a)</td><td>198.70 (n/a)</td><td>161.70 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.60 (n/a)</td><td>179.06 (n/a)</td><td>186.80 (n/a)</td><td>150.20 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>166.64 (n/a)</td><td>180.80 (n/a)</td><td>122.40 (n/a)</td><td>33.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>194.08 (n/a)</td><td>205.50 (n/a)</td><td>151.90 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>172.24 (n/a)</td><td>185.30 (n/a)</td><td>129.20 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>165.40 (n/a)</td><td>166.40 (n/a)</td><td>130.20 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>314.50 (n/a)</td><td>224.34 (n/a)</td><td>211.20 (n/a)</td><td>168.20 (n/a)</td><td>56.00 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>185.10 (n/a)</td><td>173.70 (n/a)</td><td>158.10 (n/a)</td><td>24.18 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>201.60 (n/a)</td><td>178.60 (n/a)</td><td>175.80 (n/a)</td><td>162.10 (n/a)</td><td>14.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.10 (n/a)</td><td>177.48 (n/a)</td><td>170.70 (n/a)</td><td>139.90 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>220.10 (n/a)</td><td>190.00 (n/a)</td><td>206.80 (n/a)</td><td>127.10 (n/a)</td><td>37.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>186.88 (n/a)</td><td>193.60 (n/a)</td><td>154.60 (n/a)</td><td>23.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>197.80 (n/a)</td><td>178.16 (n/a)</td><td>187.80 (n/a)</td><td>151.60 (n/a)</td><td>22.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>232.20 (n/a)</td><td>204.26 (n/a)</td><td>218.20 (n/a)</td><td>156.60 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>183.36 (n/a)</td><td>184.30 (n/a)</td><td>161.30 (n/a)</td><td>15.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.40 (n/a)</td><td>199.36 (n/a)</td><td>201.90 (n/a)</td><td>144.90 (n/a)</td><td>37.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>189.74 (n/a)</td><td>198.90 (n/a)</td><td>143.00 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>170.18 (n/a)</td><td>173.20 (n/a)</td><td>135.00 (n/a)</td><td>31.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>168.30 (n/a)</td><td>166.50 (n/a)</td><td>143.40 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>286.80 (n/a)</td><td>195.10 (n/a)</td><td>193.60 (n/a)</td><td>132.80 (n/a)</td><td>57.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>179.74 (n/a)</td><td>180.90 (n/a)</td><td>146.30 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.70 (n/a)</td><td>177.26 (n/a)</td><td>178.20 (n/a)</td><td>155.40 (n/a)</td><td>18.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.30 (n/a)</td><td>213.68 (n/a)</td><td>233.50 (n/a)</td><td>166.50 (n/a)</td><td>40.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>181.16 (n/a)</td><td>180.40 (n/a)</td><td>149.40 (n/a)</td><td>21.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>188.70 (n/a)</td><td>184.00 (n/a)</td><td>152.60 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>179.80 (n/a)</td><td>177.60 (n/a)</td><td>125.90 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>164.80 (n/a)</td><td>151.90 (n/a)</td><td>125.40 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>180.82 (n/a)</td><td>184.10 (n/a)</td><td>146.30 (n/a)</td><td>24.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>242.30 (n/a)</td><td>209.80 (n/a)</td><td>209.80 (n/a)</td><td>175.00 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.90 (n/a)</td><td>207.30 (n/a)</td><td>203.10 (n/a)</td><td>164.20 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.80 (n/a)</td><td>221.00 (n/a)</td><td>219.60 (n/a)</td><td>208.80 (n/a)</td><td>10.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>164.32 (n/a)</td><td>151.40 (n/a)</td><td>141.80 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>182.48 (n/a)</td><td>181.70 (n/a)</td><td>159.60 (n/a)</td><td>23.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>195.40 (n/a)</td><td>185.88 (n/a)</td><td>186.50 (n/a)</td><td>175.20 (n/a)</td><td>7.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>237.60 (n/a)</td><td>200.82 (n/a)</td><td>214.20 (n/a)</td><td>161.30 (n/a)</td><td>34.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.00 (n/a)</td><td>200.48 (n/a)</td><td>193.50 (n/a)</td><td>140.50 (n/a)</td><td>41.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>203.40 (n/a)</td><td>195.98 (n/a)</td><td>195.80 (n/a)</td><td>188.10 (n/a)</td><td>5.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>163.24 (n/a)</td><td>168.80 (n/a)</td><td>140.50 (n/a)</td><td>16.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>218.60 (n/a)</td><td>187.74 (n/a)</td><td>197.50 (n/a)</td><td>137.20 (n/a)</td><td>31.48 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.40 (n/a)</td><td>172.82 (n/a)</td><td>157.40 (n/a)</td><td>154.80 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>198.30 (n/a)</td><td>169.14 (n/a)</td><td>166.70 (n/a)</td><td>146.10 (n/a)</td><td>18.74 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>197.60 (n/a)</td><td>163.76 (n/a)</td><td>160.40 (n/a)</td><td>142.40 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.70 (n/a)</td><td>167.14 (n/a)</td><td>163.40 (n/a)</td><td>123.50 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.50 (n/a)</td><td>165.46 (n/a)</td><td>153.80 (n/a)</td><td>140.80 (n/a)</td><td>30.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>245.30 (n/a)</td><td>199.08 (n/a)</td><td>182.40 (n/a)</td><td>168.60 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.30 (n/a)</td><td>198.12 (n/a)</td><td>210.90 (n/a)</td><td>152.50 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>236.30 (n/a)</td><td>202.90 (n/a)</td><td>229.10 (n/a)</td><td>151.70 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>4.89 (+2.33%)</td><td>4.34 (+6.91%)</td><td>4.15 (+7.44%)</td><td>3.87 (+11.98%)</td><td>0.46 <b>(-30.95%)</b></td><td>2432.70 (-10.70%)</td><td>2185.60 (-7.60%)</td><td>2266.30 (-6.92%)</td><td>1923.30 (-2.28%)</td><td>225.08 <b>(-40.05%)</b></td><td>1923.50 (+2.33%)</td><td>1707.44 (+6.91%)</td><td>1632.33 (+7.44%)</td><td>1520.72 (+11.98%)</td><td>180.04 <b>(-30.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>4.78 (n/a)</td><td>4.06 (n/a)</td><td>3.86 (n/a)</td><td>3.45 (n/a)</td><td>0.66 (n/a)</td><td>2724.10 (n/a)</td><td>2365.26 (n/a)</td><td>2434.90 (n/a)</td><td>1968.10 (n/a)</td><td>375.41 (n/a)</td><td>1879.67 (n/a)</td><td>1597.09 (n/a)</td><td>1519.34 (n/a)</td><td>1358.01 (n/a)</td><td>260.74 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.25 (+0.99%)</td><td>1.01 (+4.01%)</td><td>0.94 (-4.51%)</td><td>0.75 <b>(+22.83%)</b></td><td>0.22 (-8.19%)</td><td>295.50 (-18.60%)</td><td>227.58 (-5.87%)</td><td>234.80 (+4.73%)</td><td>177.50 (-0.95%)</td><td>50.25 <b>(-30.91%)</b></td><td>53.17 (+0.99%)</td><td>43.12 (+4.01%)</td><td>40.19 (-4.51%)</td><td>31.94 <b>(+22.83%)</b></td><td>9.46 (-8.19%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.23 (n/a)</td><td>0.97 (n/a)</td><td>0.99 (n/a)</td><td>0.61 (n/a)</td><td>0.24 (n/a)</td><td>363.00 (n/a)</td><td>241.78 (n/a)</td><td>224.20 (n/a)</td><td>179.20 (n/a)</td><td>72.74 (n/a)</td><td>52.65 (n/a)</td><td>41.46 (n/a)</td><td>42.08 (n/a)</td><td>26.00 (n/a)</td><td>10.31 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.19 (+3.55%)</td><td>1.05 (+18.25%)</td><td>1.08 <b>(+25.37%)</b></td><td>0.81 <b>(+32.75%)</b></td><td>0.15 <b>(-39.37%)</b></td><td>274.30 <b>(-24.66%)</b></td><td>214.70 (-19.08%)</td><td>203.90 <b>(-20.26%)</b></td><td>186.30 (-3.47%)</td><td>34.72 <b>(-53.26%)</b></td><td>50.64 (+3.55%)</td><td>44.75 (+18.25%)</td><td>46.27 <b>(+25.37%)</b></td><td>34.41 <b>(+32.75%)</b></td><td>6.23 <b>(-39.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.15 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.61 (n/a)</td><td>0.24 (n/a)</td><td>364.10 (n/a)</td><td>265.32 (n/a)</td><td>255.70 (n/a)</td><td>193.00 (n/a)</td><td>74.27 (n/a)</td><td>48.91 (n/a)</td><td>37.85 (n/a)</td><td>36.91 (n/a)</td><td>25.92 (n/a)</td><td>10.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.52 (-0.01%)</td><td>0.52 (+0.04%)</td><td>0.52 (+0.03%)</td><td>0.52 (+0.09%)</td><td>0.00 <b>(-20.09%)</b></td><td>48831.50 (-0.09%)</td><td>48696.16 (-0.04%)</td><td>48637.30 (-0.03%)</td><td>48624.30 (+0.01%)</td><td>91.81 <b>(-20.15%)</b></td><td>353.32 (-0.01%)</td><td>352.80 (+0.04%)</td><td>353.22 (+0.03%)</td><td>351.82 (+0.09%)</td><td>0.66 <b>(-20.09%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>48873.60 (n/a)</td><td>48713.34 (n/a)</td><td>48649.50 (n/a)</td><td>48620.60 (n/a)</td><td>114.98 (n/a)</td><td>353.35 (n/a)</td><td>352.67 (n/a)</td><td>353.14 (n/a)</td><td>351.52 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (+0.21%)</td><td>0.21 (-0.11%)</td><td>0.21 (+0.23%)</td><td>0.21 (-0.96%)</td><td>0.00 <b>(+87.91%)</b></td><td>120041.00 (+0.97%)</td><td>117990.78 (+0.11%)</td><td>117344.40 (-0.23%)</td><td>116751.60 (-0.21%)</td><td>1347.01 <b>(+89.30%)</b></td><td>147.15 (+0.21%)</td><td>145.62 (-0.11%)</td><td>146.41 (+0.23%)</td><td>143.12 (-0.96%)</td><td>1.65 <b>(+87.91%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118892.30 (n/a)</td><td>117858.10 (n/a)</td><td>117617.10 (n/a)</td><td>116996.20 (n/a)</td><td>711.58 (n/a)</td><td>146.84 (n/a)</td><td>145.77 (n/a)</td><td>146.07 (n/a)</td><td>144.50 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.89 (-0.64%)</td><td>0.88 (-0.37%)</td><td>0.89 (+0.13%)</td><td>0.88 (-0.55%)</td><td>0.01 (-7.13%)</td><td>28723.50 (+0.55%)</td><td>28459.94 (+0.37%)</td><td>28385.90 (-0.13%)</td><td>28240.50 (+0.65%)</td><td>195.62 (-5.96%)</td><td>608.34 (-0.64%)</td><td>603.67 (-0.37%)</td><td>605.22 (+0.13%)</td><td>598.11 (-0.55%)</td><td>4.14 (-7.13%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28566.40 (n/a)</td><td>28354.80 (n/a)</td><td>28422.50 (n/a)</td><td>28059.30 (n/a)</td><td>208.02 (n/a)</td><td>612.27 (n/a)</td><td>605.92 (n/a)</td><td>604.45 (n/a)</td><td>601.40 (n/a)</td><td>4.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.64 (+0.33%)</td><td>3.40 (-2.11%)</td><td>3.37 (-3.67%)</td><td>3.31 (-0.09%)</td><td>0.13 (-6.97%)</td><td>7606.70 (+0.09%)</td><td>7407.40 (+2.13%)</td><td>7477.20 (+3.81%)</td><td>6920.30 (-0.33%)</td><td>279.15 (-7.76%)</td><td>2482.53 (+0.33%)</td><td>2322.04 (-2.11%)</td><td>2297.63 (-3.67%)</td><td>2258.52 (-0.09%)</td><td>91.63 (-6.97%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.62 (n/a)</td><td>3.47 (n/a)</td><td>3.49 (n/a)</td><td>3.31 (n/a)</td><td>0.14 (n/a)</td><td>7599.90 (n/a)</td><td>7252.64 (n/a)</td><td>7202.70 (n/a)</td><td>6943.00 (n/a)</td><td>302.64 (n/a)</td><td>2474.42 (n/a)</td><td>2372.06 (n/a)</td><td>2385.20 (n/a)</td><td>2260.53 (n/a)</td><td>98.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.17 (-2.69%)</td><td>3.07 (+2.53%)</td><td>3.14 (+7.86%)</td><td>2.84 (+1.69%)</td><td>0.14 <b>(-29.28%)</b></td><td>8854.70 (-1.66%)</td><td>8220.94 (-2.63%)</td><td>8007.80 (-7.28%)</td><td>7937.90 (+2.77%)</td><td>381.82 <b>(-28.29%)</b></td><td>2164.30 (-2.69%)</td><td>2093.24 (+2.53%)</td><td>2145.40 (+7.86%)</td><td>1940.19 (+1.69%)</td><td>93.20 <b>(-29.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.26 (n/a)</td><td>2.99 (n/a)</td><td>2.91 (n/a)</td><td>2.79 (n/a)</td><td>0.19 (n/a)</td><td>9004.30 (n/a)</td><td>8442.80 (n/a)</td><td>8637.00 (n/a)</td><td>7724.10 (n/a)</td><td>532.42 (n/a)</td><td>2224.19 (n/a)</td><td>2041.49 (n/a)</td><td>1989.09 (n/a)</td><td>1907.95 (n/a)</td><td>131.78 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.31 (-0.14%)</td><td>3.21 (+0.61%)</td><td>3.18 (+0.71%)</td><td>3.09 (-1.77%)</td><td>0.10 <b>(+35.88%)</b></td><td>8137.40 (+1.80%)</td><td>7847.12 (-0.57%)</td><td>7907.30 (-0.70%)</td><td>7598.40 (+0.14%)</td><td>236.02 <b>(+38.06%)</b></td><td>2260.98 (-0.14%)</td><td>2190.90 (+0.61%)</td><td>2172.66 (+0.71%)</td><td>2111.21 (-1.77%)</td><td>65.98 <b>(+35.88%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.32 (n/a)</td><td>3.19 (n/a)</td><td>3.16 (n/a)</td><td>3.15 (n/a)</td><td>0.07 (n/a)</td><td>7993.30 (n/a)</td><td>7891.94 (n/a)</td><td>7963.30 (n/a)</td><td>7587.50 (n/a)</td><td>170.95 (n/a)</td><td>2264.23 (n/a)</td><td>2177.73 (n/a)</td><td>2157.37 (n/a)</td><td>2149.30 (n/a)</td><td>48.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.79 (+0.06%)</td><td>0.78 (+0.06%)</td><td>0.78 (+0.01%)</td><td>0.78 (+0.06%)</td><td>0.00 (-2.81%)</td><td>96552.40 (-0.06%)</td><td>96396.62 (-0.06%)</td><td>96442.90 (-0.01%)</td><td>96096.90 (-0.06%)</td><td>175.32 (-2.96%)</td><td>715.11 (+0.06%)</td><td>712.88 (+0.06%)</td><td>712.54 (+0.01%)</td><td>711.73 (+0.06%)</td><td>1.30 (-2.81%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96611.50 (n/a)</td><td>96453.88 (n/a)</td><td>96456.60 (n/a)</td><td>96158.20 (n/a)</td><td>180.67 (n/a)</td><td>714.65 (n/a)</td><td>712.46 (n/a)</td><td>712.44 (n/a)</td><td>711.30 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.73 (+0.02%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.06%)</td><td>0.00 <b>(-44.04%)</b></td><td>103652.50 (-0.06%)</td><td>103619.86 (-0.03%)</td><td>103613.60 (-0.03%)</td><td>103600.60 (-0.02%)</td><td>19.77 <b>(-44.12%)</b></td><td>663.31 (+0.02%)</td><td>663.19 (+0.03%)</td><td>663.23 (+0.03%)</td><td>662.98 (+0.06%)</td><td>0.13 <b>(-44.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103713.20 (n/a)</td><td>103654.48 (n/a)</td><td>103649.50 (n/a)</td><td>103617.70 (n/a)</td><td>35.38 (n/a)</td><td>663.20 (n/a)</td><td>662.97 (n/a)</td><td>663.00 (n/a)</td><td>662.59 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.70 (-0.05%)</td><td>0.69 (+0.03%)</td><td>0.70 (+0.24%)</td><td>0.69 (-0.03%)</td><td>0.00 (+5.26%)</td><td>108985.20 (+0.03%)</td><td>108700.28 (-0.03%)</td><td>108569.90 (-0.23%)</td><td>108501.90 (+0.05%)</td><td>231.05 (+5.37%)</td><td>633.35 (-0.05%)</td><td>632.19 (+0.03%)</td><td>632.95 (+0.24%)</td><td>630.54 (-0.03%)</td><td>1.34 (+5.26%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108949.70 (n/a)</td><td>108732.18 (n/a)</td><td>108825.20 (n/a)</td><td>108444.90 (n/a)</td><td>219.28 (n/a)</td><td>633.68 (n/a)</td><td>632.01 (n/a)</td><td>631.47 (n/a)</td><td>630.75 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.45 (-0.44%)</td><td>7.00 (+6.71%)</td><td>7.15 (+8.28%)</td><td>6.45 <b>(+26.78%)</b></td><td>0.46 <b>(-50.68%)</b></td><td>1382.40 <b>(-21.12%)</b></td><td>1277.12 (-7.66%)</td><td>1247.20 (-7.65%)</td><td>1196.80 (+0.44%)</td><td>85.34 <b>(-61.49%)</b></td><td>448.57 (-0.44%)</td><td>421.85 (+6.71%)</td><td>430.47 (+8.28%)</td><td>388.37 <b>(+26.78%)</b></td><td>27.69 <b>(-50.68%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.48 (n/a)</td><td>6.56 (n/a)</td><td>6.60 (n/a)</td><td>5.09 (n/a)</td><td>0.93 (n/a)</td><td>1752.50 (n/a)</td><td>1383.12 (n/a)</td><td>1350.50 (n/a)</td><td>1191.60 (n/a)</td><td>221.57 (n/a)</td><td>450.53 (n/a)</td><td>395.31 (n/a)</td><td>397.53 (n/a)</td><td>306.34 (n/a)</td><td>56.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.75 (-3.22%)</td><td>5.89 (-8.69%)</td><td>6.49 (-3.32%)</td><td>4.82 (-9.30%)</td><td>0.94 <b>(+39.04%)</b></td><td>1848.20 (+10.25%)</td><td>1546.32 (+10.84%)</td><td>1374.10 (+3.44%)</td><td>1321.00 (+3.32%)</td><td>261.83 <b>(+59.26%)</b></td><td>406.41 (-3.22%)</td><td>354.88 (-8.69%)</td><td>390.72 (-3.32%)</td><td>290.48 (-9.30%)</td><td>56.80 <b>(+39.04%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.97 (n/a)</td><td>6.45 (n/a)</td><td>6.71 (n/a)</td><td>5.32 (n/a)</td><td>0.68 (n/a)</td><td>1676.40 (n/a)</td><td>1395.14 (n/a)</td><td>1328.40 (n/a)</td><td>1278.50 (n/a)</td><td>164.41 (n/a)</td><td>419.94 (n/a)</td><td>388.66 (n/a)</td><td>404.14 (n/a)</td><td>320.26 (n/a)</td><td>40.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.08 (+1.80%)</td><td>6.50 (+1.91%)</td><td>6.54 (+4.79%)</td><td>5.75 (-4.89%)</td><td>0.49 <b>(+29.01%)</b></td><td>1550.60 (+5.14%)</td><td>1377.96 (-1.67%)</td><td>1363.50 (-4.57%)</td><td>1259.20 (-1.77%)</td><td>108.93 <b>(+34.25%)</b></td><td>426.35 (+1.80%)</td><td>391.49 (+1.91%)</td><td>393.75 (+4.79%)</td><td>346.23 (-4.89%)</td><td>29.66 <b>(+29.01%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.95 (n/a)</td><td>6.38 (n/a)</td><td>6.24 (n/a)</td><td>6.04 (n/a)</td><td>0.38 (n/a)</td><td>1474.80 (n/a)</td><td>1401.38 (n/a)</td><td>1428.80 (n/a)</td><td>1281.90 (n/a)</td><td>81.14 (n/a)</td><td>418.81 (n/a)</td><td>384.16 (n/a)</td><td>375.76 (n/a)</td><td>364.02 (n/a)</td><td>22.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.01 (+0.38%)</td><td>7.60 (-3.94%)</td><td>7.47 (-5.97%)</td><td>7.17 (-7.80%)</td><td>0.35 <b>(+293.27%)</b></td><td>4864.70 (+8.46%)</td><td>4597.88 (+4.27%)</td><td>4666.70 (+6.34%)</td><td>4352.70 (-0.38%)</td><td>209.23 <b>(+322.76%)</b></td><td>493.37 (+0.38%)</td><td>467.84 (-3.94%)</td><td>460.17 (-5.97%)</td><td>441.44 (-7.80%)</td><td>21.33 <b>(+293.27%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.98 (n/a)</td><td>7.91 (n/a)</td><td>7.95 (n/a)</td><td>7.77 (n/a)</td><td>0.09 (n/a)</td><td>4485.30 (n/a)</td><td>4409.80 (n/a)</td><td>4388.30 (n/a)</td><td>4369.20 (n/a)</td><td>49.49 (n/a)</td><td>491.50 (n/a)</td><td>487.03 (n/a)</td><td>489.37 (n/a)</td><td>478.79 (n/a)</td><td>5.42 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.98 (+0.58%)</td><td>7.51 (+0.93%)</td><td>7.56 (+0.04%)</td><td>6.83 (-1.65%)</td><td>0.42 (+9.66%)</td><td>5107.70 (+1.68%)</td><td>4654.78 (-0.87%)</td><td>4610.00 (-0.05%)</td><td>4367.10 (-0.58%)</td><td>272.91 (+11.97%)</td><td>491.74 (+0.58%)</td><td>462.57 (+0.93%)</td><td>465.83 (+0.04%)</td><td>420.44 (-1.65%)</td><td>25.94 (+9.66%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.94 (n/a)</td><td>7.44 (n/a)</td><td>7.56 (n/a)</td><td>6.94 (n/a)</td><td>0.38 (n/a)</td><td>5023.20 (n/a)</td><td>4695.84 (n/a)</td><td>4612.10 (n/a)</td><td>4392.60 (n/a)</td><td>243.72 (n/a)</td><td>488.89 (n/a)</td><td>458.30 (n/a)</td><td>465.62 (n/a)</td><td>427.51 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.48 (+1.73%)</td><td>7.30 (+2.34%)</td><td>7.43 (+2.16%)</td><td>6.83 (+0.34%)</td><td>0.27 (+5.76%)</td><td>5101.70 (-0.34%)</td><td>4781.98 (-2.28%)</td><td>4694.70 (-2.11%)</td><td>4659.20 (-1.70%)</td><td>184.67 (+3.97%)</td><td>460.92 (+1.73%)</td><td>449.59 (+2.34%)</td><td>457.43 (+2.16%)</td><td>420.93 (+0.34%)</td><td>16.63 (+5.76%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.36 (n/a)</td><td>7.13 (n/a)</td><td>7.27 (n/a)</td><td>6.81 (n/a)</td><td>0.26 (n/a)</td><td>5119.30 (n/a)</td><td>4893.38 (n/a)</td><td>4795.90 (n/a)</td><td>4739.70 (n/a)</td><td>177.61 (n/a)</td><td>453.09 (n/a)</td><td>439.31 (n/a)</td><td>447.77 (n/a)</td><td>419.49 (n/a)</td><td>15.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.79 (-0.00%)</td><td>0.79 (-0.02%)</td><td>0.79 (+0.04%)</td><td>0.79 (-0.07%)</td><td>0.00 <b>(+53.75%)</b></td><td>95956.50 (+0.07%)</td><td>95808.52 (+0.02%)</td><td>95737.30 (-0.04%)</td><td>95726.80 (+0.00%)</td><td>106.50 <b>(+53.80%)</b></td><td>717.87 (-0.00%)</td><td>717.26 (-0.02%)</td><td>717.79 (+0.04%)</td><td>716.15 (-0.07%)</td><td>0.80 <b>(+53.75%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95893.90 (n/a)</td><td>95793.72 (n/a)</td><td>95771.80 (n/a)</td><td>95724.70 (n/a)</td><td>69.24 (n/a)</td><td>717.89 (n/a)</td><td>717.37 (n/a)</td><td>717.53 (n/a)</td><td>716.62 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.73 (-0.01%)</td><td>0.73 (-0.06%)</td><td>0.73 (-0.02%)</td><td>0.73 (-0.24%)</td><td>0.00 <b>(+356.25%)</b></td><td>103206.50 (+0.25%)</td><td>102983.98 (+0.06%)</td><td>102943.80 (+0.02%)</td><td>102907.60 (+0.01%)</td><td>125.70 <b>(+357.66%)</b></td><td>667.78 (-0.01%)</td><td>667.28 (-0.06%)</td><td>667.54 (-0.02%)</td><td>665.84 (-0.24%)</td><td>0.81 <b>(+356.29%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102954.10 (n/a)</td><td>102924.34 (n/a)</td><td>102919.80 (n/a)</td><td>102895.70 (n/a)</td><td>27.47 (n/a)</td><td>667.86 (n/a)</td><td>667.67 (n/a)</td><td>667.70 (n/a)</td><td>667.48 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.70 (+0.09%)</td><td>0.70 (-0.09%)</td><td>0.70 (-0.05%)</td><td>0.70 (-0.17%)</td><td>0.00 <b>(+44.04%)</b></td><td>108187.50 (+0.17%)</td><td>107888.88 (+0.09%)</td><td>107917.10 (+0.05%)</td><td>107436.60 (-0.09%)</td><td>279.16 <b>(+44.10%)</b></td><td>639.63 (+0.09%)</td><td>636.95 (-0.09%)</td><td>636.78 (-0.05%)</td><td>635.19 (-0.17%)</td><td>1.65 <b>(+44.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108001.90 (n/a)</td><td>107787.92 (n/a)</td><td>107868.50 (n/a)</td><td>107533.40 (n/a)</td><td>193.73 (n/a)</td><td>639.05 (n/a)</td><td>637.55 (n/a)</td><td>637.07 (n/a)</td><td>636.28 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>4.23 (+3.37%)</td><td>3.74 (+8.73%)</td><td>3.67 (+2.71%)</td><td>3.44 (+19.49%)</td><td>0.31 <b>(-41.41%)</b></td><td>2340.00 (-16.31%)</td><td>2168.26 (-9.31%)</td><td>2198.90 (-2.64%)</td><td>1903.80 (-3.25%)</td><td>169.99 <b>(-54.33%)</b></td><td>1110.39 (+3.37%)</td><td>980.03 (+8.73%)</td><td>961.35 (+2.71%)</td><td>903.39 (+19.49%)</td><td>81.20 <b>(-41.41%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>4.10 (n/a)</td><td>3.44 (n/a)</td><td>3.57 (n/a)</td><td>2.88 (n/a)</td><td>0.53 (n/a)</td><td>2796.10 (n/a)</td><td>2390.90 (n/a)</td><td>2258.50 (n/a)</td><td>1967.80 (n/a)</td><td>372.24 (n/a)</td><td>1074.23 (n/a)</td><td>901.35 (n/a)</td><td>935.99 (n/a)</td><td>756.03 (n/a)</td><td>138.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (+14.16%)</td><td>0.35 (+5.77%)</td><td>0.33 (+4.08%)</td><td>0.28 (-1.63%)</td><td>0.08 <b>(+33.00%)</b></td><td>4471.80 (+1.66%)</td><td>3644.96 (-4.33%)</td><td>3738.80 (-3.92%)</td><td>2497.50 (-12.40%)</td><td>713.75 (+11.82%)</td><td>26.87 (+14.16%)</td><td>19.11 (+5.77%)</td><td>17.95 (+4.08%)</td><td>15.01 (-1.63%)</td><td>4.52 <b>(+33.00%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>4398.70 (n/a)</td><td>3809.78 (n/a)</td><td>3891.40 (n/a)</td><td>2851.10 (n/a)</td><td>638.33 (n/a)</td><td>23.54 (n/a)</td><td>18.07 (n/a)</td><td>17.25 (n/a)</td><td>15.26 (n/a)</td><td>3.40 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.44 (+3.08%)</td><td>4.91 (-4.44%)</td><td>4.77 (-0.78%)</td><td>3.76 <b>(-20.98%)</b></td><td>0.97 <b>(+51.61%)</b></td><td>1769.90 <b>(+26.55%)</b></td><td>1395.84 (+6.60%)</td><td>1394.90 (+0.79%)</td><td>1033.20 (-2.99%)</td><td>261.46 <b>(+83.80%)</b></td><td>1989.16 (+3.08%)</td><td>1516.21 (-4.44%)</td><td>1473.41 (-0.78%)</td><td>1161.18 <b>(-20.98%)</b></td><td>298.58 <b>(+51.61%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.25 (n/a)</td><td>5.14 (n/a)</td><td>4.81 (n/a)</td><td>4.76 (n/a)</td><td>0.64 (n/a)</td><td>1398.60 (n/a)</td><td>1309.38 (n/a)</td><td>1384.00 (n/a)</td><td>1065.00 (n/a)</td><td>142.25 (n/a)</td><td>1929.76 (n/a)</td><td>1586.72 (n/a)</td><td>1485.02 (n/a)</td><td>1469.49 (n/a)</td><td>196.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>13.35 (n/a)</td><td>12.24 (n/a)</td><td>12.30 (n/a)</td><td>11.07 (n/a)</td><td>1.12 (n/a)</td><td>13.34 (n/a)</td><td>12.23 (n/a)</td><td>12.29 (n/a)</td><td>11.06 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>24.68 (-1.11%)</td><td>23.86 (-1.13%)</td><td>24.11 (+0.73%)</td><td>22.45 (-4.68%)</td><td>0.85 <b>(+54.91%)</b></td><td>24.66 (-1.11%)</td><td>23.84 (-1.13%)</td><td>24.09 (+0.73%)</td><td>22.44 (-4.68%)</td><td>0.85 <b>(+54.91%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>24.95 (n/a)</td><td>24.13 (n/a)</td><td>23.93 (n/a)</td><td>23.56 (n/a)</td><td>0.55 (n/a)</td><td>24.94 (n/a)</td><td>24.12 (n/a)</td><td>23.92 (n/a)</td><td>23.54 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>41.20 (-3.19%)</td><td>39.87 (+0.14%)</td><td>40.01 (+2.38%)</td><td>38.55 (+0.20%)</td><td>0.99 <b>(-38.78%)</b></td><td>41.17 (-3.19%)</td><td>39.85 (+0.14%)</td><td>39.99 (+2.38%)</td><td>38.53 (+0.20%)</td><td>0.99 <b>(-38.78%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>42.56 (n/a)</td><td>39.82 (n/a)</td><td>39.08 (n/a)</td><td>38.47 (n/a)</td><td>1.62 (n/a)</td><td>42.53 (n/a)</td><td>39.79 (n/a)</td><td>39.06 (n/a)</td><td>38.45 (n/a)</td><td>1.62 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>44.21 (+1.39%)</td><td>42.36 (+2.32%)</td><td>41.87 (+1.45%)</td><td>39.96 (+2.63%)</td><td>1.75 (-4.08%)</td><td>44.19 (+1.39%)</td><td>42.33 (+2.32%)</td><td>41.85 (+1.45%)</td><td>39.94 (+2.63%)</td><td>1.75 (-4.08%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>43.61 (n/a)</td><td>41.40 (n/a)</td><td>41.27 (n/a)</td><td>38.94 (n/a)</td><td>1.82 (n/a)</td><td>43.58 (n/a)</td><td>41.37 (n/a)</td><td>41.25 (n/a)</td><td>38.91 (n/a)</td><td>1.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>13.34 (n/a)</td><td>12.65 (n/a)</td><td>12.41 (n/a)</td><td>11.93 (n/a)</td><td>0.62 (n/a)</td><td>13.33 (n/a)</td><td>12.64 (n/a)</td><td>12.40 (n/a)</td><td>11.92 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>25.01 (+2.51%)</td><td>23.49 (-1.42%)</td><td>24.03 (+0.27%)</td><td>20.06 (-10.81%)</td><td>1.96 <b>(+153.39%)</b></td><td>24.99 (+2.51%)</td><td>23.48 (-1.42%)</td><td>24.02 (+0.27%)</td><td>20.05 (-10.81%)</td><td>1.96 <b>(+153.39%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>24.40 (n/a)</td><td>23.83 (n/a)</td><td>23.97 (n/a)</td><td>22.49 (n/a)</td><td>0.77 (n/a)</td><td>24.38 (n/a)</td><td>23.81 (n/a)</td><td>23.95 (n/a)</td><td>22.48 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>39.39 (-2.92%)</td><td>35.49 (-10.42%)</td><td>38.00 (-4.22%)</td><td>30.27 <b>(-21.91%)</b></td><td>4.66 <b>(+514.98%)</b></td><td>39.37 (-2.92%)</td><td>35.46 (-10.42%)</td><td>37.97 (-4.22%)</td><td>30.25 <b>(-21.91%)</b></td><td>4.66 <b>(+514.98%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>40.58 (n/a)</td><td>39.61 (n/a)</td><td>39.67 (n/a)</td><td>38.76 (n/a)</td><td>0.76 (n/a)</td><td>40.56 (n/a)</td><td>39.59 (n/a)</td><td>39.65 (n/a)</td><td>38.74 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>44.29 (+0.23%)</td><td>42.54 (-1.51%)</td><td>42.85 (-0.70%)</td><td>40.17 (-4.69%)</td><td>1.68 <b>(+86.93%)</b></td><td>44.26 (+0.23%)</td><td>42.52 (-1.51%)</td><td>42.83 (-0.70%)</td><td>40.14 (-4.69%)</td><td>1.68 <b>(+86.93%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>44.19 (n/a)</td><td>43.20 (n/a)</td><td>43.16 (n/a)</td><td>42.14 (n/a)</td><td>0.90 (n/a)</td><td>44.16 (n/a)</td><td>43.17 (n/a)</td><td>43.13 (n/a)</td><td>42.12 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.29 (+1.30%)</td><td>9.15 (+8.32%)</td><td>9.18 (+8.73%)</td><td>8.93 (+18.05%)</td><td>0.15 <b>(-73.62%)</b></td><td>9.27 (+1.30%)</td><td>9.14 (+8.32%)</td><td>9.16 (+8.73%)</td><td>8.91 (+18.05%)</td><td>0.15 <b>(-73.62%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.17 (n/a)</td><td>8.45 (n/a)</td><td>8.44 (n/a)</td><td>7.57 (n/a)</td><td>0.58 (n/a)</td><td>9.16 (n/a)</td><td>8.43 (n/a)</td><td>8.43 (n/a)</td><td>7.55 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.91 (-7.70%)</td><td>0.83 (+0.80%)</td><td>0.81 (+0.85%)</td><td>0.79 (+5.61%)</td><td>0.05 <b>(-49.46%)</b></td><td>0.89 (-7.70%)</td><td>0.81 (+0.80%)</td><td>0.80 (+0.85%)</td><td>0.77 (+5.61%)</td><td>0.05 <b>(-49.46%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.98 (n/a)</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.74 (n/a)</td><td>0.10 (n/a)</td><td>0.97 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.73 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.28 (+10.40%)</td><td>1.09 (+4.17%)</td><td>1.08 (+6.97%)</td><td>0.90 (-8.44%)</td><td>0.17 <b>(+126.86%)</b></td><td>1.26 (+10.40%)</td><td>1.08 (+4.17%)</td><td>1.07 (+6.97%)</td><td>0.89 (-8.44%)</td><td>0.17 <b>(+126.86%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.16 (n/a)</td><td>1.05 (n/a)</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.07 (n/a)</td><td>1.14 (n/a)</td><td>1.04 (n/a)</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>16.08 (-1.76%)</td><td>14.79 (-3.46%)</td><td>15.49 (+0.97%)</td><td>12.32 (-14.14%)</td><td>1.55 <b>(+81.62%)</b></td><td>15.90 (-1.76%)</td><td>14.62 (-3.46%)</td><td>15.31 (+0.97%)</td><td>12.18 (-14.14%)</td><td>1.53 <b>(+81.62%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>16.37 (n/a)</td><td>15.32 (n/a)</td><td>15.34 (n/a)</td><td>14.35 (n/a)</td><td>0.85 (n/a)</td><td>16.18 (n/a)</td><td>15.15 (n/a)</td><td>15.16 (n/a)</td><td>14.19 (n/a)</td><td>0.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>11.90 (-1.87%)</td><td>11.40 (-2.61%)</td><td>11.63 (-1.08%)</td><td>10.21 (-6.92%)</td><td>0.69 <b>(+44.79%)</b></td><td>11.69 (-1.87%)</td><td>11.20 (-2.61%)</td><td>11.43 (-1.08%)</td><td>10.04 (-6.92%)</td><td>0.68 <b>(+44.79%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.13 (n/a)</td><td>11.71 (n/a)</td><td>11.76 (n/a)</td><td>10.97 (n/a)</td><td>0.48 (n/a)</td><td>11.91 (n/a)</td><td>11.50 (n/a)</td><td>11.55 (n/a)</td><td>10.78 (n/a)</td><td>0.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.77 (+7.17%)</td><td>8.06 (+13.26%)</td><td>8.03 (+11.34%)</td><td>7.03 (+16.84%)</td><td>0.73 (-11.10%)</td><td>8.62 (+7.17%)</td><td>7.92 (+13.26%)</td><td>7.89 (+11.34%)</td><td>6.90 (+16.84%)</td><td>0.72 (-11.10%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>8.19 (n/a)</td><td>7.12 (n/a)</td><td>7.21 (n/a)</td><td>6.01 (n/a)</td><td>0.83 (n/a)</td><td>8.04 (n/a)</td><td>7.00 (n/a)</td><td>7.09 (n/a)</td><td>5.91 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.43 (+2.18%)</td><td>5.75 (-0.48%)</td><td>5.74 (-5.38%)</td><td>5.18 (+11.38%)</td><td>0.46 <b>(-33.94%)</b></td><td>6.33 (+2.18%)</td><td>5.66 (-0.48%)</td><td>5.65 (-5.38%)</td><td>5.10 (+11.38%)</td><td>0.45 <b>(-33.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.29 (n/a)</td><td>5.78 (n/a)</td><td>6.07 (n/a)</td><td>4.65 (n/a)</td><td>0.69 (n/a)</td><td>6.19 (n/a)</td><td>5.69 (n/a)</td><td>5.97 (n/a)</td><td>4.58 (n/a)</td><td>0.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>13.39 (n/a)</td><td>12.41 (n/a)</td><td>12.22 (n/a)</td><td>11.09 (n/a)</td><td>0.91 (n/a)</td><td>13.39 (n/a)</td><td>12.41 (n/a)</td><td>12.21 (n/a)</td><td>11.08 (n/a)</td><td>0.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>13.36 (n/a)</td><td>12.37 (n/a)</td><td>12.55 (n/a)</td><td>10.05 (n/a)</td><td>1.36 (n/a)</td><td>13.36 (n/a)</td><td>12.36 (n/a)</td><td>12.54 (n/a)</td><td>10.04 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.40 (n/a)</td><td>160.36 (n/a)</td><td>148.30 (n/a)</td><td>134.90 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.60 (n/a)</td><td>169.74 (n/a)</td><td>171.50 (n/a)</td><td>141.60 (n/a)</td><td>21.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.20 (n/a)</td><td>183.44 (n/a)</td><td>161.40 (n/a)</td><td>150.10 (n/a)</td><td>43.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.90 (n/a)</td><td>169.96 (n/a)</td><td>161.50 (n/a)</td><td>156.70 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.70 (n/a)</td><td>205.02 (n/a)</td><td>189.70 (n/a)</td><td>174.80 (n/a)</td><td>38.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.60 (n/a)</td><td>187.72 (n/a)</td><td>191.90 (n/a)</td><td>145.50 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>170.06 (n/a)</td><td>165.50 (n/a)</td><td>149.80 (n/a)</td><td>21.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>381.10 (n/a)</td><td>257.50 (n/a)</td><td>240.10 (n/a)</td><td>191.30 (n/a)</td><td>72.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>193.52 (n/a)</td><td>184.40 (n/a)</td><td>165.90 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>262.60 (n/a)</td><td>202.74 (n/a)</td><td>176.50 (n/a)</td><td>165.80 (n/a)</td><td>44.14 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>161.14 (n/a)</td><td>161.30 (n/a)</td><td>130.90 (n/a)</td><td>22.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>178.92 (n/a)</td><td>180.70 (n/a)</td><td>139.50 (n/a)</td><td>26.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>179.44 (n/a)</td><td>181.30 (n/a)</td><td>159.20 (n/a)</td><td>15.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>189.74 (n/a)</td><td>197.00 (n/a)</td><td>153.40 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>243.50 (n/a)</td><td>201.28 (n/a)</td><td>189.80 (n/a)</td><td>178.90 (n/a)</td><td>26.35 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>267.70 (n/a)</td><td>230.46 (n/a)</td><td>237.50 (n/a)</td><td>180.30 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.90 (n/a)</td><td>196.28 (n/a)</td><td>211.60 (n/a)</td><td>150.20 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>171.80 (n/a)</td><td>178.80 (n/a)</td><td>138.10 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>201.72 (n/a)</td><td>202.60 (n/a)</td><td>176.70 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.50 (n/a)</td><td>205.00 (n/a)</td><td>201.60 (n/a)</td><td>149.90 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>186.78 (n/a)</td><td>186.90 (n/a)</td><td>160.00 (n/a)</td><td>18.75 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>218.92 (n/a)</td><td>211.30 (n/a)</td><td>203.00 (n/a)</td><td>17.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>246.00 (n/a)</td><td>222.00 (n/a)</td><td>219.60 (n/a)</td><td>204.80 (n/a)</td><td>15.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.40 (n/a)</td><td>226.98 (n/a)</td><td>233.00 (n/a)</td><td>200.60 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>388.00 (n/a)</td><td>226.62 (n/a)</td><td>198.10 (n/a)</td><td>159.70 (n/a)</td><td>91.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>222.20 (n/a)</td><td>194.26 (n/a)</td><td>199.30 (n/a)</td><td>150.20 (n/a)</td><td>27.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>241.80 (n/a)</td><td>197.70 (n/a)</td><td>197.10 (n/a)</td><td>173.30 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>206.32 (n/a)</td><td>201.30 (n/a)</td><td>199.60 (n/a)</td><td>11.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.40 (n/a)</td><td>186.94 (n/a)</td><td>182.10 (n/a)</td><td>163.20 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.40 (n/a)</td><td>170.52 (n/a)</td><td>173.20 (n/a)</td><td>134.90 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>246.40 (n/a)</td><td>192.32 (n/a)</td><td>186.20 (n/a)</td><td>165.60 (n/a)</td><td>31.78 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.50 (n/a)</td><td>197.08 (n/a)</td><td>204.10 (n/a)</td><td>157.50 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+8.81%)</td><td>0.02 (-5.20%)</td><td>0.02 (-11.07%)</td><td>0.02 (-13.63%)</td><td>0.01 <b>(+47.81%)</b></td><td>239.70 (+15.80%)</td><td>179.58 (+7.84%)</td><td>178.20 (+12.43%)</td><td>127.20 (-8.09%)</td><td>40.07 <b>(+53.85%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.00 (n/a)</td><td>166.52 (n/a)</td><td>158.50 (n/a)</td><td>138.40 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+11.09%)</td><td>0.03 (-1.90%)</td><td>0.02 (-3.49%)</td><td>0.02 <b>(-21.47%)</b></td><td>0.00 <b>(+217.33%)</b></td><td>222.20 <b>(+27.34%)</b></td><td>166.92 (+4.90%)</td><td>164.40 (+3.66%)</td><td>134.40 (-9.98%)</td><td>34.80 <b>(+261.57%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.50 (n/a)</td><td>159.12 (n/a)</td><td>158.60 (n/a)</td><td>149.30 (n/a)</td><td>9.62 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-17.21%)</td><td>0.03 (+0.05%)</td><td>0.02 (-11.73%)</td><td>0.02 <b>(+59.67%)</b></td><td>0.01 <b>(-42.68%)</b></td><td>209.10 <b>(-37.36%)</b></td><td>167.18 (-10.92%)</td><td>165.10 (+13.24%)</td><td>125.00 <b>(+20.77%)</b></td><td>38.19 <b>(-57.76%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>333.80 (n/a)</td><td>187.68 (n/a)</td><td>145.80 (n/a)</td><td>103.50 (n/a)</td><td>90.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 <b>(+21.87%)</b></td><td>0.03 <b>(+24.80%)</b></td><td>0.03 (+17.38%)</td><td>0.02 <b>(+55.46%)</b></td><td>0.00 (-2.04%)</td><td>197.40 <b>(-35.68%)</b></td><td>159.30 <b>(-22.13%)</b></td><td>160.50 (-14.81%)</td><td>122.00 (-17.90%)</td><td>29.03 <b>(-51.51%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>306.90 (n/a)</td><td>204.56 (n/a)</td><td>188.40 (n/a)</td><td>148.60 (n/a)</td><td>59.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+16.10%)</td><td>0.02 <b>(+20.56%)</b></td><td>0.02 (+12.50%)</td><td>0.02 <b>(+58.05%)</b></td><td>0.00 <b>(-25.51%)</b></td><td>234.30 <b>(-36.74%)</b></td><td>178.96 <b>(-21.36%)</b></td><td>171.10 (-11.12%)</td><td>150.60 (-13.84%)</td><td>33.22 <b>(-59.53%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>370.40 (n/a)</td><td>227.56 (n/a)</td><td>192.50 (n/a)</td><td>174.80 (n/a)</td><td>82.09 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-14.44%)</td><td>0.02 (-16.05%)</td><td>0.02 (-19.20%)</td><td>0.02 (-6.96%)</td><td>0.00 <b>(-27.47%)</b></td><td>219.40 (+7.44%)</td><td>188.40 (+17.65%)</td><td>202.10 <b>(+23.76%)</b></td><td>141.50 (+16.85%)</td><td>31.39 (-8.36%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>160.14 (n/a)</td><td>163.30 (n/a)</td><td>121.10 (n/a)</td><td>34.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 <b>(+46.56%)</b></td><td>0.02 <b>(+20.44%)</b></td><td>0.02 (+10.27%)</td><td>0.02 (+9.21%)</td><td>0.00 <b>(+236.47%)</b></td><td>201.70 (-8.44%)</td><td>172.80 (-15.02%)</td><td>179.60 (-9.29%)</td><td>126.20 <b>(-31.78%)</b></td><td>29.47 <b>(+104.60%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.30 (n/a)</td><td>203.34 (n/a)</td><td>198.00 (n/a)</td><td>185.00 (n/a)</td><td>14.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (-5.36%)</td><td>0.02 (-4.42%)</td><td>0.02 (-5.15%)</td><td>0.02 (+2.12%)</td><td>0.00 <b>(-35.48%)</b></td><td>219.50 (-2.10%)</td><td>195.88 (+3.90%)</td><td>196.80 (+5.47%)</td><td>175.40 (+5.66%)</td><td>16.09 <b>(-32.43%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.20 (n/a)</td><td>188.52 (n/a)</td><td>186.60 (n/a)</td><td>166.00 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-14.01%)</td><td>0.04 (-6.81%)</td><td>0.04 (-5.48%)</td><td>0.04 (-9.25%)</td><td>0.01 (-8.08%)</td><td>212.10 (+10.18%)</td><td>186.10 (+7.45%)</td><td>189.20 (+5.82%)</td><td>161.00 (+16.33%)</td><td>24.40 (+19.51%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>173.20 (n/a)</td><td>178.80 (n/a)</td><td>138.40 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-4.17%)</td><td>0.05 (+7.01%)</td><td>0.05 (-0.57%)</td><td>0.04 <b>(+25.67%)</b></td><td>0.00 <b>(-59.38%)</b></td><td>187.30 <b>(-20.43%)</b></td><td>173.60 (-8.31%)</td><td>176.40 (+0.57%)</td><td>161.60 (+4.33%)</td><td>10.63 <b>(-66.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>189.34 (n/a)</td><td>175.40 (n/a)</td><td>154.90 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-5.72%)</td><td>0.05 (+14.67%)</td><td>0.05 <b>(+33.85%)</b></td><td>0.04 <b>(+29.20%)</b></td><td>0.00 <b>(-61.94%)</b></td><td>193.60 <b>(-22.59%)</b></td><td>179.80 (-15.08%)</td><td>173.00 <b>(-25.30%)</b></td><td>169.00 (+6.09%)</td><td>12.32 <b>(-68.55%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>211.72 (n/a)</td><td>231.60 (n/a)</td><td>159.30 (n/a)</td><td>39.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (+2.24%)</td><td>0.05 (-4.34%)</td><td>0.05 (-1.72%)</td><td>0.04 (-9.72%)</td><td>0.01 (+18.91%)</td><td>190.00 (+10.79%)</td><td>166.06 (+4.93%)</td><td>168.20 (+1.75%)</td><td>138.00 (-2.20%)</td><td>18.73 <b>(+27.19%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.50 (n/a)</td><td>158.26 (n/a)</td><td>165.30 (n/a)</td><td>141.10 (n/a)</td><td>14.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+0.33%)</td><td>0.05 (+3.12%)</td><td>0.05 (-0.26%)</td><td>0.05 (+8.72%)</td><td>0.01 (-0.88%)</td><td>178.80 (-8.02%)</td><td>156.20 (-3.15%)</td><td>164.50 (+0.30%)</td><td>122.70 (-0.32%)</td><td>24.33 (-6.20%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>161.28 (n/a)</td><td>164.00 (n/a)</td><td>123.10 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-0.18%)</td><td>0.05 (-1.91%)</td><td>0.05 (-0.19%)</td><td>0.04 (-5.57%)</td><td>0.01 (+13.20%)</td><td>199.90 (+5.88%)</td><td>173.92 (+2.27%)</td><td>174.30 (+0.23%)</td><td>142.30 (+0.14%)</td><td>20.64 <b>(+20.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>170.06 (n/a)</td><td>173.90 (n/a)</td><td>142.10 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-14.57%)</td><td>0.04 (-13.42%)</td><td>0.04 (-12.00%)</td><td>0.03 (-10.84%)</td><td>0.01 (-4.32%)</td><td>235.70 (+12.13%)</td><td>200.78 (+15.78%)</td><td>191.60 (+13.57%)</td><td>174.30 (+17.06%)</td><td>28.59 <b>(+23.40%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>173.42 (n/a)</td><td>168.70 (n/a)</td><td>148.90 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (+7.10%)</td><td>0.04 (+1.18%)</td><td>0.04 (-0.25%)</td><td>0.03 (-6.85%)</td><td>0.01 <b>(+48.79%)</b></td><td>239.60 (+7.35%)</td><td>192.38 (+0.06%)</td><td>183.60 (+0.27%)</td><td>161.10 (-6.61%)</td><td>33.01 <b>(+48.58%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.20 (n/a)</td><td>192.26 (n/a)</td><td>183.10 (n/a)</td><td>172.50 (n/a)</td><td>22.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (+4.27%)</td><td>0.05 (+6.54%)</td><td>0.05 (+4.40%)</td><td>0.04 (+16.30%)</td><td>0.00 <b>(-20.57%)</b></td><td>215.10 (-14.03%)</td><td>179.78 (-7.02%)</td><td>173.60 (-4.25%)</td><td>160.70 (-4.12%)</td><td>20.97 <b>(-35.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.20 (n/a)</td><td>193.36 (n/a)</td><td>181.30 (n/a)</td><td>167.60 (n/a)</td><td>32.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (+0.42%)</td><td>0.04 (+1.55%)</td><td>0.04 (-0.46%)</td><td>0.04 (+3.62%)</td><td>0.00 (-10.44%)</td><td>228.00 (-3.51%)</td><td>213.02 (-1.61%)</td><td>217.50 (+0.46%)</td><td>196.90 (-0.40%)</td><td>12.15 (-14.43%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>216.50 (n/a)</td><td>216.50 (n/a)</td><td>197.70 (n/a)</td><td>14.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (+3.52%)</td><td>0.10 (+6.84%)</td><td>0.10 (+3.34%)</td><td>0.08 (+2.51%)</td><td>0.01 (+13.66%)</td><td>199.70 (-2.44%)</td><td>167.90 (-6.18%)</td><td>172.30 (-3.26%)</td><td>143.10 (-3.44%)</td><td>24.55 (+2.44%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>178.96 (n/a)</td><td>178.10 (n/a)</td><td>148.20 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+13.90%)</td><td>0.10 (-1.04%)</td><td>0.10 (+1.82%)</td><td>0.08 (-12.23%)</td><td>0.02 <b>(+81.81%)</b></td><td>210.70 (+13.95%)</td><td>171.46 (+3.02%)</td><td>170.30 (-1.79%)</td><td>126.30 (-12.23%)</td><td>30.75 <b>(+78.68%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.90 (n/a)</td><td>166.44 (n/a)</td><td>173.40 (n/a)</td><td>143.90 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (+11.46%)</td><td>0.10 (-4.35%)</td><td>0.09 (-9.56%)</td><td>0.08 (-4.34%)</td><td>0.03 <b>(+45.96%)</b></td><td>199.00 (+4.52%)</td><td>169.54 (+6.59%)</td><td>185.10 (+10.57%)</td><td>113.80 (-10.25%)</td><td>33.59 <b>(+33.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.40 (n/a)</td><td>159.06 (n/a)</td><td>167.40 (n/a)</td><td>126.80 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (-14.93%)</td><td>0.09 (-6.51%)</td><td>0.10 (-5.32%)</td><td>0.08 (-0.73%)</td><td>0.01 <b>(-38.19%)</b></td><td>209.90 (+0.72%)</td><td>180.10 (+5.22%)</td><td>170.70 (+5.63%)</td><td>159.40 (+17.55%)</td><td>23.41 <b>(-29.11%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>171.16 (n/a)</td><td>161.60 (n/a)</td><td>135.60 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (+10.07%)</td><td>0.09 (+4.72%)</td><td>0.09 (+5.64%)</td><td>0.07 (+3.66%)</td><td>0.02 <b>(+59.84%)</b></td><td>224.80 (-3.52%)</td><td>187.98 (-3.26%)</td><td>180.70 (-5.34%)</td><td>155.40 (-9.12%)</td><td>32.51 <b>(+38.58%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>194.32 (n/a)</td><td>190.90 (n/a)</td><td>171.00 (n/a)</td><td>23.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (+13.87%)</td><td>0.08 (+6.37%)</td><td>0.08 (-8.23%)</td><td>0.07 <b>(+38.84%)</b></td><td>0.02 (-8.52%)</td><td>250.20 <b>(-27.98%)</b></td><td>204.18 (-8.63%)</td><td>215.40 (+8.95%)</td><td>158.20 (-12.21%)</td><td>37.80 <b>(-45.73%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>347.40 (n/a)</td><td>223.46 (n/a)</td><td>197.70 (n/a)</td><td>180.20 (n/a)</td><td>69.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (+9.82%)</td><td>0.09 (-4.33%)</td><td>0.08 (-8.33%)</td><td>0.07 (-16.10%)</td><td>0.01 <b>(+245.56%)</b></td><td>230.80 (+19.15%)</td><td>196.06 (+6.55%)</td><td>197.30 (+9.07%)</td><td>158.10 (-8.93%)</td><td>31.25 <b>(+273.79%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>184.00 (n/a)</td><td>180.90 (n/a)</td><td>173.60 (n/a)</td><td>8.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (+3.82%)</td><td>0.08 (-4.93%)</td><td>0.08 (-5.08%)</td><td>0.07 (-14.54%)</td><td>0.01 <b>(+155.54%)</b></td><td>243.10 (+16.99%)</td><td>213.34 (+6.04%)</td><td>214.90 (+5.34%)</td><td>181.10 (-3.67%)</td><td>22.62 <b>(+186.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>201.18 (n/a)</td><td>204.00 (n/a)</td><td>188.00 (n/a)</td><td>7.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (-7.08%)</td><td>0.17 (-14.84%)</td><td>0.17 (-11.20%)</td><td>0.14 <b>(-23.81%)</b></td><td>0.03 <b>(+72.68%)</b></td><td>234.80 <b>(+31.25%)</b></td><td>196.52 (+19.39%)</td><td>190.40 (+12.60%)</td><td>161.60 (+7.59%)</td><td>32.72 <b>(+149.46%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>178.90 (n/a)</td><td>164.60 (n/a)</td><td>169.10 (n/a)</td><td>150.20 (n/a)</td><td>13.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (-6.20%)</td><td>0.16 (-11.73%)</td><td>0.16 (-12.07%)</td><td>0.14 (-17.43%)</td><td>0.02 <b>(+65.50%)</b></td><td>239.90 <b>(+21.16%)</b></td><td>209.38 (+14.32%)</td><td>200.40 (+13.73%)</td><td>184.10 (+6.60%)</td><td>26.57 <b>(+115.50%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>198.00 (n/a)</td><td>183.16 (n/a)</td><td>176.20 (n/a)</td><td>172.70 (n/a)</td><td>12.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (-7.50%)</td><td>0.16 (-13.30%)</td><td>0.16 (-13.87%)</td><td>0.11 <b>(-22.76%)</b></td><td>0.03 (+19.68%)</td><td>294.50 <b>(+29.45%)</b></td><td>212.60 (+17.35%)</td><td>201.30 (+16.09%)</td><td>168.00 (+8.11%)</td><td>47.88 <b>(+71.90%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>227.50 (n/a)</td><td>181.16 (n/a)</td><td>173.40 (n/a)</td><td>155.40 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (-2.82%)</td><td>0.18 (-9.15%)</td><td>0.17 (-7.04%)</td><td>0.15 (-4.47%)</td><td>0.03 (-9.76%)</td><td>216.10 (+4.70%)</td><td>189.16 (+9.81%)</td><td>194.60 (+7.57%)</td><td>147.20 (+2.87%)</td><td>25.89 (-2.86%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>206.40 (n/a)</td><td>172.26 (n/a)</td><td>180.90 (n/a)</td><td>143.10 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (+1.89%)</td><td>0.16 (+9.87%)</td><td>0.16 (+7.67%)</td><td>0.14 <b>(+37.27%)</b></td><td>0.02 <b>(-39.94%)</b></td><td>240.40 <b>(-27.15%)</b></td><td>206.98 (-11.79%)</td><td>202.00 (-7.13%)</td><td>178.00 (-1.87%)</td><td>24.40 <b>(-57.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>330.00 (n/a)</td><td>234.64 (n/a)</td><td>217.50 (n/a)</td><td>181.40 (n/a)</td><td>58.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (-16.13%)</td><td>0.15 (-15.56%)</td><td>0.16 (-8.17%)</td><td>0.09 <b>(-37.46%)</b></td><td>0.04 (+5.54%)</td><td>358.40 <b>(+59.86%)</b></td><td>229.64 <b>(+22.38%)</b></td><td>201.80 (+8.90%)</td><td>176.60 (+19.24%)</td><td>73.25 <b>(+109.21%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>224.20 (n/a)</td><td>187.64 (n/a)</td><td>185.30 (n/a)</td><td>148.10 (n/a)</td><td>35.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 (-5.32%)</td><td>0.15 (-1.64%)</td><td>0.15 (-3.78%)</td><td>0.14 (+9.10%)</td><td>0.01 <b>(-39.61%)</b></td><td>232.70 (-8.35%)</td><td>219.78 (+0.92%)</td><td>222.70 (+3.92%)</td><td>195.20 (+5.63%)</td><td>15.17 <b>(-41.89%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>253.90 (n/a)</td><td>217.78 (n/a)</td><td>214.30 (n/a)</td><td>184.80 (n/a)</td><td>26.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 <b>(+26.51%)</b></td><td>0.03 <b>(+37.16%)</b></td><td>0.03 <b>(+32.58%)</b></td><td>0.03 <b>(+108.61%)</b></td><td>0.00 <b>(-51.46%)</b></td><td>163.10 <b>(-52.07%)</b></td><td>143.18 <b>(-31.81%)</b></td><td>137.60 <b>(-24.56%)</b></td><td>129.10 <b>(-20.94%)</b></td><td>13.37 <b>(-81.99%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>340.30 (n/a)</td><td>209.96 (n/a)</td><td>182.40 (n/a)</td><td>163.30 (n/a)</td><td>74.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+17.03%)</td><td>0.03 <b>(+21.26%)</b></td><td>0.03 (+17.71%)</td><td>0.02 (+15.37%)</td><td>0.01 (+13.74%)</td><td>191.90 (-13.32%)</td><td>149.44 (-17.65%)</td><td>145.70 (-15.04%)</td><td>117.70 (-14.59%)</td><td>27.95 (-15.81%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.40 (n/a)</td><td>181.46 (n/a)</td><td>171.50 (n/a)</td><td>137.80 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (+3.45%)</td><td>0.02 (-1.70%)</td><td>0.02 (-6.11%)</td><td>0.01 (-8.28%)</td><td>0.00 <b>(+20.90%)</b></td><td>336.70 (+9.03%)</td><td>231.46 (+3.34%)</td><td>223.00 (+6.49%)</td><td>180.20 (-3.33%)</td><td>61.72 <b>(+26.72%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>308.80 (n/a)</td><td>223.98 (n/a)</td><td>209.40 (n/a)</td><td>186.40 (n/a)</td><td>48.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-2.31%)</td><td>0.02 (-4.46%)</td><td>0.02 (-3.50%)</td><td>0.02 (-9.30%)</td><td>0.00 (+7.82%)</td><td>237.60 (+10.26%)</td><td>186.70 (+5.28%)</td><td>183.70 (+3.61%)</td><td>145.10 (+2.33%)</td><td>33.25 <b>(+22.98%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.50 (n/a)</td><td>177.34 (n/a)</td><td>177.30 (n/a)</td><td>141.80 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-17.35%)</td><td>0.03 (-3.94%)</td><td>0.03 (-0.02%)</td><td>0.02 (-17.93%)</td><td>0.01 (-18.39%)</td><td>245.50 <b>(+21.84%)</b></td><td>169.72 (+3.92%)</td><td>159.80 (+0.06%)</td><td>133.20 <b>(+20.98%)</b></td><td>45.39 (+18.11%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>163.32 (n/a)</td><td>159.70 (n/a)</td><td>110.10 (n/a)</td><td>38.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+3.89%)</td><td>0.03 (+11.56%)</td><td>0.03 (+9.65%)</td><td>0.02 <b>(+24.03%)</b></td><td>0.00 (+0.26%)</td><td>188.10 (-19.37%)</td><td>157.60 (-10.95%)</td><td>150.80 (-8.77%)</td><td>131.50 (-3.73%)</td><td>27.59 <b>(-23.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.30 (n/a)</td><td>176.98 (n/a)</td><td>165.30 (n/a)</td><td>136.60 (n/a)</td><td>35.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+6.65%)</td><td>0.03 (+8.98%)</td><td>0.03 (+6.15%)</td><td>0.02 <b>(+24.30%)</b></td><td>0.00 (-14.08%)</td><td>194.30 (-19.54%)</td><td>161.78 (-9.43%)</td><td>161.30 (-5.84%)</td><td>140.50 (-6.27%)</td><td>22.46 <b>(-38.39%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.50 (n/a)</td><td>178.62 (n/a)</td><td>171.30 (n/a)</td><td>149.90 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 <b>(+21.53%)</b></td><td>0.02 (+1.57%)</td><td>0.02 (-7.04%)</td><td>0.02 (-7.05%)</td><td>0.01 <b>(+113.53%)</b></td><td>221.30 (+7.58%)</td><td>177.16 (+2.09%)</td><td>188.20 (+7.54%)</td><td>122.60 (-17.66%)</td><td>41.21 <b>(+88.77%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>173.54 (n/a)</td><td>175.00 (n/a)</td><td>148.90 (n/a)</td><td>21.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-2.27%)</td><td>0.03 (+5.12%)</td><td>0.03 (+5.63%)</td><td>0.02 <b>(+27.18%)</b></td><td>0.01 (-16.12%)</td><td>219.90 <b>(-21.35%)</b></td><td>169.74 (-7.91%)</td><td>156.30 (-5.33%)</td><td>128.30 (+2.31%)</td><td>41.37 <b>(-32.40%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>279.60 (n/a)</td><td>184.32 (n/a)</td><td>165.10 (n/a)</td><td>125.40 (n/a)</td><td>61.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+3.70%)</td><td>0.02 (-1.88%)</td><td>0.02 (-6.18%)</td><td>0.02 (+14.25%)</td><td>0.00 (-7.76%)</td><td>209.00 (-12.48%)</td><td>175.36 (+0.77%)</td><td>180.40 (+6.56%)</td><td>131.00 (-3.61%)</td><td>28.13 <b>(-27.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.80 (n/a)</td><td>174.02 (n/a)</td><td>169.30 (n/a)</td><td>135.90 (n/a)</td><td>38.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-6.64%)</td><td>0.02 (-5.11%)</td><td>0.02 (-11.76%)</td><td>0.02 (+5.34%)</td><td>0.00 <b>(-25.64%)</b></td><td>236.30 (-5.06%)</td><td>175.10 (+3.32%)</td><td>168.10 (+13.35%)</td><td>149.80 (+7.08%)</td><td>35.28 <b>(-23.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.90 (n/a)</td><td>169.48 (n/a)</td><td>148.30 (n/a)</td><td>139.90 (n/a)</td><td>45.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 <b>(+31.34%)</b></td><td>0.02 (-1.62%)</td><td>0.02 (-6.93%)</td><td>0.01 <b>(-36.29%)</b></td><td>0.01 <b>(+140.16%)</b></td><td>343.20 <b>(+57.00%)</b></td><td>208.56 (+13.10%)</td><td>186.80 (+7.48%)</td><td>112.80 <b>(-23.84%)</b></td><td>84.92 <b>(+181.34%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.60 (n/a)</td><td>184.40 (n/a)</td><td>173.80 (n/a)</td><td>148.10 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (-17.40%)</td><td>0.02 (-16.44%)</td><td>0.02 (-4.25%)</td><td>0.01 <b>(-22.24%)</b></td><td>0.00 (+9.33%)</td><td>285.40 <b>(+28.62%)</b></td><td>232.46 <b>(+21.53%)</b></td><td>210.50 (+4.47%)</td><td>185.40 <b>(+21.02%)</b></td><td>47.11 <b>(+78.57%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.90 (n/a)</td><td>191.28 (n/a)</td><td>201.50 (n/a)</td><td>153.20 (n/a)</td><td>26.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-9.67%)</td><td>0.02 (+7.60%)</td><td>0.02 (+13.34%)</td><td>0.02 (+19.30%)</td><td>0.00 <b>(-45.69%)</b></td><td>189.70 (-16.17%)</td><td>168.06 (-9.78%)</td><td>165.10 (-11.76%)</td><td>140.30 (+10.65%)</td><td>20.20 <b>(-48.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>186.28 (n/a)</td><td>187.10 (n/a)</td><td>126.80 (n/a)</td><td>39.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-9.54%)</td><td>0.02 (+8.91%)</td><td>0.02 <b>(+21.52%)</b></td><td>0.02 (+5.41%)</td><td>0.00 <b>(-29.84%)</b></td><td>219.80 (-5.14%)</td><td>173.88 (-9.39%)</td><td>168.10 (-17.68%)</td><td>154.70 (+10.58%)</td><td>26.52 <b>(-23.27%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.70 (n/a)</td><td>191.90 (n/a)</td><td>204.20 (n/a)</td><td>139.90 (n/a)</td><td>34.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+2.24%)</td><td>0.03 <b>(+30.48%)</b></td><td>0.03 <b>(+36.42%)</b></td><td>0.02 <b>(+54.08%)</b></td><td>0.00 <b>(-40.11%)</b></td><td>167.50 <b>(-35.10%)</b></td><td>140.82 <b>(-27.14%)</b></td><td>137.20 <b>(-26.67%)</b></td><td>118.80 (-2.14%)</td><td>20.19 <b>(-61.60%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.10 (n/a)</td><td>193.28 (n/a)</td><td>187.10 (n/a)</td><td>121.40 (n/a)</td><td>52.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-1.93%)</td><td>0.06 (+3.00%)</td><td>0.06 (+4.52%)</td><td>0.05 (+16.68%)</td><td>0.01 <b>(-39.58%)</b></td><td>161.00 (-14.27%)</td><td>148.14 (-4.36%)</td><td>148.40 (-4.32%)</td><td>127.00 (+1.93%)</td><td>13.59 <b>(-47.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>154.90 (n/a)</td><td>155.10 (n/a)</td><td>124.60 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-8.25%)</td><td>0.05 (-5.03%)</td><td>0.05 (+6.33%)</td><td>0.04 (-8.01%)</td><td>0.01 (+6.59%)</td><td>230.70 (+8.72%)</td><td>172.34 (+6.90%)</td><td>160.90 (-5.96%)</td><td>127.80 (+8.95%)</td><td>47.20 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>161.22 (n/a)</td><td>171.10 (n/a)</td><td>117.30 (n/a)</td><td>37.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 <b>(+79.16%)</b></td><td>0.04 (+13.15%)</td><td>0.04 (+3.12%)</td><td>0.02 <b>(-40.70%)</b></td><td>0.02 <b>(+935.61%)</b></td><td>378.90 <b>(+68.62%)</b></td><td>218.08 (+2.65%)</td><td>209.20 (-3.06%)</td><td>112.90 <b>(-44.19%)</b></td><td>98.77 <b>(+900.43%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.70 (n/a)</td><td>212.46 (n/a)</td><td>215.80 (n/a)</td><td>202.30 (n/a)</td><td>9.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 <b>(+34.58%)</b></td><td>0.05 (+10.62%)</td><td>0.04 (+0.78%)</td><td>0.03 (+4.82%)</td><td>0.02 <b>(+72.08%)</b></td><td>285.90 (-4.60%)</td><td>198.74 (-5.56%)</td><td>207.00 (-0.77%)</td><td>120.10 <b>(-25.68%)</b></td><td>63.91 (+18.01%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.70 (n/a)</td><td>210.44 (n/a)</td><td>208.60 (n/a)</td><td>161.60 (n/a)</td><td>54.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+15.32%)</td><td>0.05 (-6.41%)</td><td>0.05 (-11.03%)</td><td>0.04 (-12.37%)</td><td>0.01 <b>(+130.74%)</b></td><td>201.50 (+14.10%)</td><td>168.06 (+9.54%)</td><td>168.60 (+12.40%)</td><td>120.00 (-13.29%)</td><td>30.87 <b>(+118.68%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>176.60 (n/a)</td><td>153.42 (n/a)</td><td>150.00 (n/a)</td><td>138.40 (n/a)</td><td>14.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+6.27%)</td><td>0.05 (-2.85%)</td><td>0.06 (+0.66%)</td><td>0.03 <b>(-26.15%)</b></td><td>0.01 <b>(+79.84%)</b></td><td>239.20 <b>(+35.45%)</b></td><td>165.02 (+7.98%)</td><td>144.90 (-0.62%)</td><td>117.20 (-5.86%)</td><td>48.93 <b>(+129.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.60 (n/a)</td><td>152.82 (n/a)</td><td>145.80 (n/a)</td><td>124.50 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+9.51%)</td><td>0.06 (+11.55%)</td><td>0.06 (+17.99%)</td><td>0.05 <b>(+20.87%)</b></td><td>0.01 (-17.43%)</td><td>172.60 (-17.30%)</td><td>145.78 (-11.88%)</td><td>143.90 (-15.25%)</td><td>117.30 (-8.64%)</td><td>22.96 <b>(-35.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>165.44 (n/a)</td><td>169.80 (n/a)</td><td>128.40 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 <b>(+21.36%)</b></td><td>0.06 <b>(+27.55%)</b></td><td>0.06 <b>(+46.74%)</b></td><td>0.05 <b>(+24.66%)</b></td><td>0.01 (-16.74%)</td><td>170.50 (-19.80%)</td><td>145.28 <b>(-22.54%)</b></td><td>140.20 <b>(-31.84%)</b></td><td>126.80 (-17.56%)</td><td>17.04 <b>(-44.25%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>187.56 (n/a)</td><td>205.70 (n/a)</td><td>153.80 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (+18.56%)</td><td>0.05 (+2.74%)</td><td>0.05 (+0.49%)</td><td>0.04 (-8.83%)</td><td>0.01 <b>(+110.09%)</b></td><td>203.00 (+9.73%)</td><td>166.32 (-0.96%)</td><td>159.90 (-0.50%)</td><td>130.30 (-15.66%)</td><td>27.88 <b>(+94.04%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.00 (n/a)</td><td>167.94 (n/a)</td><td>160.70 (n/a)</td><td>154.50 (n/a)</td><td>14.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+12.27%)</td><td>0.05 (+10.46%)</td><td>0.05 (+9.79%)</td><td>0.04 (-1.34%)</td><td>0.01 <b>(+53.66%)</b></td><td>184.20 (+1.38%)</td><td>152.40 (-8.58%)</td><td>155.60 (-8.95%)</td><td>124.50 (-10.94%)</td><td>23.32 <b>(+38.45%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.70 (n/a)</td><td>166.70 (n/a)</td><td>170.90 (n/a)</td><td>139.80 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-17.95%)</td><td>0.05 (-7.89%)</td><td>0.05 (+0.67%)</td><td>0.04 (-17.10%)</td><td>0.01 <b>(-30.55%)</b></td><td>217.70 <b>(+20.68%)</b></td><td>179.38 (+8.01%)</td><td>172.70 (-0.63%)</td><td>152.10 <b>(+21.87%)</b></td><td>24.57 (+5.44%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>166.08 (n/a)</td><td>173.80 (n/a)</td><td>124.80 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 <b>(+20.87%)</b></td><td>0.06 <b>(+33.52%)</b></td><td>0.06 <b>(+42.40%)</b></td><td>0.04 (+18.40%)</td><td>0.01 <b>(+36.33%)</b></td><td>182.40 (-15.56%)</td><td>135.50 <b>(-24.59%)</b></td><td>128.70 <b>(-29.75%)</b></td><td>116.50 (-17.26%)</td><td>27.00 (-1.23%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>179.68 (n/a)</td><td>183.20 (n/a)</td><td>140.80 (n/a)</td><td>27.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-13.87%)</td><td>0.04 (-8.59%)</td><td>0.04 (+2.83%)</td><td>0.03 <b>(-33.24%)</b></td><td>0.01 (+17.02%)</td><td>309.70 <b>(+49.76%)</b></td><td>202.12 (+13.49%)</td><td>182.00 (-2.78%)</td><td>152.60 (+16.05%)</td><td>63.37 <b>(+111.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>178.10 (n/a)</td><td>187.20 (n/a)</td><td>131.50 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (+13.63%)</td><td>0.05 (+5.00%)</td><td>0.05 (+1.48%)</td><td>0.04 (-6.59%)</td><td>0.01 <b>(+83.61%)</b></td><td>201.20 (+7.08%)</td><td>168.32 (-3.62%)</td><td>174.20 (-1.41%)</td><td>135.30 (-12.03%)</td><td>24.58 <b>(+70.26%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>174.64 (n/a)</td><td>176.70 (n/a)</td><td>153.80 (n/a)</td><td>14.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-11.16%)</td><td>0.05 (+4.46%)</td><td>0.05 (+1.24%)</td><td>0.05 <b>(+24.25%)</b></td><td>0.01 <b>(-50.26%)</b></td><td>179.10 (-19.51%)</td><td>166.26 (-6.75%)</td><td>176.40 (-1.23%)</td><td>143.20 (+12.58%)</td><td>16.42 <b>(-53.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>178.30 (n/a)</td><td>178.60 (n/a)</td><td>127.20 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 <b>(+32.13%)</b></td><td>0.05 (+9.64%)</td><td>0.05 (+8.62%)</td><td>0.03 (-8.47%)</td><td>0.01 <b>(+128.79%)</b></td><td>234.80 (+9.26%)</td><td>175.86 (-5.58%)</td><td>174.70 (-7.96%)</td><td>124.50 <b>(-24.32%)</b></td><td>41.53 <b>(+92.75%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>186.26 (n/a)</td><td>189.80 (n/a)</td><td>164.50 (n/a)</td><td>21.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (-5.50%)</td><td>0.09 (-6.97%)</td><td>0.10 (-1.19%)</td><td>0.07 <b>(-20.46%)</b></td><td>0.02 <b>(+29.80%)</b></td><td>243.30 <b>(+25.74%)</b></td><td>180.34 (+9.34%)</td><td>171.50 (+1.18%)</td><td>148.10 (+5.86%)</td><td>37.70 <b>(+77.54%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>164.94 (n/a)</td><td>169.50 (n/a)</td><td>139.90 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (+12.57%)</td><td>0.10 (+7.85%)</td><td>0.10 (-1.96%)</td><td>0.09 (+15.71%)</td><td>0.02 (+12.26%)</td><td>192.40 (-13.57%)</td><td>162.66 (-7.41%)</td><td>171.20 (+2.03%)</td><td>119.00 (-11.19%)</td><td>28.86 (-15.51%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.60 (n/a)</td><td>175.68 (n/a)</td><td>167.80 (n/a)</td><td>134.00 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (+16.14%)</td><td>0.09 (+10.10%)</td><td>0.08 (+3.77%)</td><td>0.07 (+4.77%)</td><td>0.01 <b>(+97.80%)</b></td><td>221.90 (-4.56%)</td><td>194.28 (-7.90%)</td><td>206.80 (-3.63%)</td><td>161.20 (-13.93%)</td><td>30.38 <b>(+60.82%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.50 (n/a)</td><td>210.94 (n/a)</td><td>214.60 (n/a)</td><td>187.30 (n/a)</td><td>18.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 <b>(+22.74%)</b></td><td>0.08 (-4.60%)</td><td>0.07 (-9.86%)</td><td>0.05 <b>(-35.77%)</b></td><td>0.03 <b>(+238.06%)</b></td><td>359.40 <b>(+55.72%)</b></td><td>234.80 (+13.90%)</td><td>229.20 (+10.94%)</td><td>145.70 (-18.51%)</td><td>80.44 <b>(+336.11%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>206.14 (n/a)</td><td>206.60 (n/a)</td><td>178.80 (n/a)</td><td>18.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (+4.85%)</td><td>0.10 (-1.82%)</td><td>0.11 (+12.13%)</td><td>0.07 <b>(-24.32%)</b></td><td>0.02 <b>(+126.09%)</b></td><td>236.10 <b>(+32.12%)</b></td><td>178.04 (+6.89%)</td><td>152.50 (-10.82%)</td><td>132.20 (-4.62%)</td><td>48.68 <b>(+196.89%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.70 (n/a)</td><td>166.56 (n/a)</td><td>171.00 (n/a)</td><td>138.60 (n/a)</td><td>16.40 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (-17.19%)</td><td>0.08 (-11.59%)</td><td>0.09 (-9.50%)</td><td>0.06 (-6.60%)</td><td>0.01 <b>(-30.69%)</b></td><td>263.50 (+7.07%)</td><td>202.20 (+11.58%)</td><td>192.30 (+10.45%)</td><td>165.70 <b>(+20.77%)</b></td><td>37.02 (-9.46%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>246.10 (n/a)</td><td>181.22 (n/a)</td><td>174.10 (n/a)</td><td>137.20 (n/a)</td><td>40.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (+15.43%)</td><td>0.10 (-1.55%)</td><td>0.10 (+5.24%)</td><td>0.07 (-19.23%)</td><td>0.02 <b>(+182.33%)</b></td><td>237.00 <b>(+23.82%)</b></td><td>177.68 (+6.05%)</td><td>156.70 (-4.97%)</td><td>132.40 (-13.35%)</td><td>44.97 <b>(+205.50%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>167.54 (n/a)</td><td>164.90 (n/a)</td><td>152.80 (n/a)</td><td>14.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+10.26%)</td><td>0.10 (+4.45%)</td><td>0.09 (-17.01%)</td><td>0.06 <b>(+37.64%)</b></td><td>0.03 (-1.14%)</td><td>274.60 <b>(-27.34%)</b></td><td>179.00 (-9.44%)</td><td>182.80 <b>(+20.50%)</b></td><td>124.30 (-9.27%)</td><td>60.50 <b>(-40.44%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>377.90 (n/a)</td><td>197.66 (n/a)</td><td>151.70 (n/a)</td><td>137.00 (n/a)</td><td>101.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+7.58%)</td><td>0.10 (+2.22%)</td><td>0.10 (+16.25%)</td><td>0.08 (-11.78%)</td><td>0.02 <b>(+37.89%)</b></td><td>214.30 (+13.33%)</td><td>167.42 (-0.61%)</td><td>157.00 (-14.02%)</td><td>129.20 (-7.05%)</td><td>34.07 <b>(+46.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>168.44 (n/a)</td><td>182.60 (n/a)</td><td>139.00 (n/a)</td><td>23.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (+4.50%)</td><td>0.08 (-10.00%)</td><td>0.08 (-13.71%)</td><td>0.07 (-18.69%)</td><td>0.02 <b>(+62.95%)</b></td><td>249.70 <b>(+23.00%)</b></td><td>202.50 (+13.28%)</td><td>200.90 (+15.93%)</td><td>150.30 (-4.27%)</td><td>36.94 <b>(+87.38%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>178.76 (n/a)</td><td>173.30 (n/a)</td><td>157.00 (n/a)</td><td>19.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (-4.45%)</td><td>0.09 (-4.43%)</td><td>0.09 (-4.22%)</td><td>0.07 (-6.20%)</td><td>0.01 (+3.23%)</td><td>221.20 (+6.60%)</td><td>188.78 (+4.76%)</td><td>185.30 (+4.39%)</td><td>171.10 (+4.65%)</td><td>19.03 (+15.71%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>180.20 (n/a)</td><td>177.50 (n/a)</td><td>163.50 (n/a)</td><td>16.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 <b>(-37.62%)</b></td><td>0.09 (-12.44%)</td><td>0.09 (-2.13%)</td><td>0.07 (-0.41%)</td><td>0.01 <b>(-72.75%)</b></td><td>219.40 (+0.41%)</td><td>185.66 (+8.60%)</td><td>180.20 (+2.21%)</td><td>172.00 <b>(+60.30%)</b></td><td>19.28 <b>(-53.48%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>218.50 (n/a)</td><td>170.96 (n/a)</td><td>176.30 (n/a)</td><td>107.30 (n/a)</td><td>41.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (+9.19%)</td><td>0.09 (-1.42%)</td><td>0.08 (-5.58%)</td><td>0.08 (+1.55%)</td><td>0.01 <b>(+26.18%)</b></td><td>209.70 (-1.50%)</td><td>192.28 (+1.88%)</td><td>200.60 (+5.91%)</td><td>150.00 (-8.42%)</td><td>23.99 (+10.97%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>188.74 (n/a)</td><td>189.40 (n/a)</td><td>163.80 (n/a)</td><td>21.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (-15.56%)</td><td>0.08 (-13.29%)</td><td>0.08 (-12.46%)</td><td>0.07 (-19.02%)</td><td>0.01 (+13.76%)</td><td>239.70 <b>(+23.49%)</b></td><td>207.14 (+16.15%)</td><td>205.50 (+14.29%)</td><td>179.20 (+18.44%)</td><td>28.12 <b>(+64.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>178.34 (n/a)</td><td>179.80 (n/a)</td><td>151.30 (n/a)</td><td>17.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 <b>(+54.17%)</b></td><td>0.09 (+13.54%)</td><td>0.08 (-1.49%)</td><td>0.07 (+13.12%)</td><td>0.03 <b>(+144.04%)</b></td><td>231.90 (-11.59%)</td><td>188.58 (-8.82%)</td><td>199.60 (+1.47%)</td><td>120.40 <b>(-35.13%)</b></td><td>42.09 <b>(+31.92%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>262.30 (n/a)</td><td>206.82 (n/a)</td><td>196.70 (n/a)</td><td>185.60 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (+3.35%)</td><td>0.10 (+16.72%)</td><td>0.09 (+12.99%)</td><td>0.08 <b>(+53.58%)</b></td><td>0.01 <b>(-43.83%)</b></td><td>194.80 <b>(-34.87%)</b></td><td>172.88 (-19.00%)</td><td>175.20 (-11.47%)</td><td>142.00 (-3.20%)</td><td>23.04 <b>(-64.12%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>299.10 (n/a)</td><td>213.42 (n/a)</td><td>197.90 (n/a)</td><td>146.70 (n/a)</td><td>64.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (+5.61%)</td><td>0.17 (-1.15%)</td><td>0.17 (-4.18%)</td><td>0.15 (-1.55%)</td><td>0.02 <b>(+47.23%)</b></td><td>223.00 (+1.55%)</td><td>196.66 (+1.73%)</td><td>197.90 (+4.38%)</td><td>167.30 (-5.32%)</td><td>22.70 <b>(+39.88%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>193.32 (n/a)</td><td>189.60 (n/a)</td><td>176.70 (n/a)</td><td>16.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 <b>(+31.23%)</b></td><td>0.20 (+11.74%)</td><td>0.19 (+11.34%)</td><td>0.16 (+8.30%)</td><td>0.04 <b>(+112.88%)</b></td><td>200.60 (-7.69%)</td><td>170.10 (-8.76%)</td><td>169.00 (-10.20%)</td><td>125.70 <b>(-23.77%)</b></td><td>30.29 <b>(+49.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>186.44 (n/a)</td><td>188.20 (n/a)</td><td>164.90 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (+17.34%)</td><td>0.16 (+16.87%)</td><td>0.17 (+18.67%)</td><td>0.11 (+19.48%)</td><td>0.03 (+16.35%)</td><td>295.20 (-16.30%)</td><td>210.18 (-14.61%)</td><td>195.10 (-15.72%)</td><td>158.00 (-14.78%)</td><td>51.45 (-18.11%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>352.70 (n/a)</td><td>246.14 (n/a)</td><td>231.50 (n/a)</td><td>185.40 (n/a)</td><td>62.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (+2.03%)</td><td>0.18 (+14.40%)</td><td>0.17 <b>(+22.73%)</b></td><td>0.16 (+16.87%)</td><td>0.02 <b>(-26.23%)</b></td><td>206.50 (-14.46%)</td><td>181.18 (-13.86%)</td><td>188.10 (-18.54%)</td><td>156.00 (-1.95%)</td><td>21.77 <b>(-39.78%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>241.40 (n/a)</td><td>210.34 (n/a)</td><td>230.90 (n/a)</td><td>159.10 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (-13.25%)</td><td>0.17 (-16.52%)</td><td>0.18 (-10.38%)</td><td>0.10 <b>(-42.27%)</b></td><td>0.05 <b>(+51.61%)</b></td><td>344.30 <b>(+73.19%)</b></td><td>215.14 <b>(+28.69%)</b></td><td>182.90 (+11.59%)</td><td>150.60 (+15.23%)</td><td>80.39 <b>(+199.08%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>198.80 (n/a)</td><td>167.18 (n/a)</td><td>163.90 (n/a)</td><td>130.70 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (+14.74%)</td><td>0.20 <b>(+26.33%)</b></td><td>0.19 <b>(+20.07%)</b></td><td>0.18 <b>(+40.85%)</b></td><td>0.03 (-18.63%)</td><td>182.00 <b>(-29.02%)</b></td><td>164.10 <b>(-22.26%)</b></td><td>173.20 (-16.69%)</td><td>134.60 (-12.88%)</td><td>20.14 <b>(-49.23%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>256.40 (n/a)</td><td>211.08 (n/a)</td><td>207.90 (n/a)</td><td>154.50 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 <b>(+23.31%)</b></td><td>0.20 (+8.36%)</td><td>0.21 (+17.93%)</td><td>0.14 (-15.68%)</td><td>0.05 <b>(+175.00%)</b></td><td>238.40 (+18.61%)</td><td>174.44 (-3.55%)</td><td>157.80 (-15.21%)</td><td>128.20 (-18.86%)</td><td>45.28 <b>(+169.17%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>201.00 (n/a)</td><td>180.86 (n/a)</td><td>186.10 (n/a)</td><td>158.00 (n/a)</td><td>16.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (-13.48%)</td><td>0.17 (-15.82%)</td><td>0.17 (-7.16%)</td><td>0.14 (-10.07%)</td><td>0.03 <b>(-26.71%)</b></td><td>238.10 (+11.21%)</td><td>197.86 (+17.58%)</td><td>190.20 (+7.76%)</td><td>149.50 (+15.62%)</td><td>36.83 (+0.18%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>214.10 (n/a)</td><td>168.28 (n/a)</td><td>176.50 (n/a)</td><td>129.30 (n/a)</td><td>36.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (-11.92%)</td><td>0.19 (+1.98%)</td><td>0.20 (+9.87%)</td><td>0.15 (-4.06%)</td><td>0.03 <b>(-28.54%)</b></td><td>223.60 (+4.24%)</td><td>174.88 (-2.95%)</td><td>167.40 (-8.97%)</td><td>146.90 (+13.52%)</td><td>28.89 (-9.71%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>214.50 (n/a)</td><td>180.20 (n/a)</td><td>183.90 (n/a)</td><td>129.40 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (-4.08%)</td><td>0.18 (+12.24%)</td><td>0.19 (+11.97%)</td><td>0.16 <b>(+75.11%)</b></td><td>0.02 <b>(-53.21%)</b></td><td>203.60 <b>(-42.89%)</b></td><td>179.90 (-17.13%)</td><td>169.80 (-10.68%)</td><td>155.60 (+4.29%)</td><td>21.26 <b>(-73.55%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>356.50 (n/a)</td><td>217.08 (n/a)</td><td>190.10 (n/a)</td><td>149.20 (n/a)</td><td>80.36 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 <b>(+25.82%)</b></td><td>0.20 (+10.26%)</td><td>0.19 (-1.30%)</td><td>0.16 (+4.15%)</td><td>0.03 <b>(+83.38%)</b></td><td>206.50 (-3.95%)</td><td>169.26 (-8.06%)</td><td>174.40 (+1.28%)</td><td>133.60 <b>(-20.52%)</b></td><td>28.02 <b>(+39.55%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.00 (n/a)</td><td>184.10 (n/a)</td><td>172.20 (n/a)</td><td>168.10 (n/a)</td><td>20.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (+7.04%)</td><td>0.18 (+0.69%)</td><td>0.18 (-0.96%)</td><td>0.14 (-6.11%)</td><td>0.03 (+18.20%)</td><td>230.60 (+6.46%)</td><td>188.98 (-0.18%)</td><td>186.80 (+0.97%)</td><td>152.40 (-6.56%)</td><td>29.22 (+16.44%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.60 (n/a)</td><td>189.32 (n/a)</td><td>185.00 (n/a)</td><td>163.10 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (-6.35%)</td><td>0.17 (-8.71%)</td><td>0.18 (-7.65%)</td><td>0.14 (-7.67%)</td><td>0.03 (+2.74%)</td><td>238.40 (+8.31%)</td><td>199.60 (+10.02%)</td><td>183.00 (+8.22%)</td><td>168.60 (+6.78%)</td><td>33.66 <b>(+22.16%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.10 (n/a)</td><td>181.42 (n/a)</td><td>169.10 (n/a)</td><td>157.90 (n/a)</td><td>27.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (-17.62%)</td><td>0.18 (-6.71%)</td><td>0.19 (+5.67%)</td><td>0.14 (-12.13%)</td><td>0.04 (-14.46%)</td><td>229.00 (+13.82%)</td><td>185.52 (+7.24%)</td><td>176.50 (-5.36%)</td><td>148.00 <b>(+21.41%)</b></td><td>39.67 (+17.31%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.20 (n/a)</td><td>173.00 (n/a)</td><td>186.50 (n/a)</td><td>121.90 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 <b>(+21.41%)</b></td><td>0.19 (+17.90%)</td><td>0.20 <b>(+28.18%)</b></td><td>0.16 (+1.37%)</td><td>0.04 <b>(+122.14%)</b></td><td>211.10 (-1.36%)</td><td>173.08 (-13.34%)</td><td>160.00 <b>(-21.99%)</b></td><td>139.50 (-17.60%)</td><td>32.98 <b>(+88.99%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.00 (n/a)</td><td>199.72 (n/a)</td><td>205.10 (n/a)</td><td>169.30 (n/a)</td><td>17.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (+6.20%)</td><td>0.20 (+17.10%)</td><td>0.19 (+8.49%)</td><td>0.16 <b>(+91.87%)</b></td><td>0.03 <b>(-43.12%)</b></td><td>200.10 <b>(-47.86%)</b></td><td>169.28 <b>(-22.59%)</b></td><td>176.80 (-7.82%)</td><td>132.70 (-5.82%)</td><td>24.97 <b>(-74.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>383.80 (n/a)</td><td>218.68 (n/a)</td><td>191.80 (n/a)</td><td>140.90 (n/a)</td><td>96.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (-0.05%)</td><td>0.21 (+0.01%)</td><td>0.21 (+0.04%)</td><td>0.21 (-0.08%)</td><td>0.00 (-1.31%)</td><td>40911.30 (+0.08%)</td><td>40743.20 (-0.01%)</td><td>40811.50 (-0.04%)</td><td>40414.30 (+0.05%)</td><td>199.15 (-1.19%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40880.60 (n/a)</td><td>40745.90 (n/a)</td><td>40829.40 (n/a)</td><td>40393.50 (n/a)</td><td>201.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (+0.78%)</td><td>0.21 (+0.03%)</td><td>0.21 (-0.12%)</td><td>0.20 (-0.47%)</td><td>0.00 <b>(+337.09%)</b></td><td>41109.30 (+0.47%)</td><td>40841.70 (-0.03%)</td><td>40895.60 (+0.12%)</td><td>40483.50 (-0.77%)</td><td>228.83 <b>(+335.24%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40917.50 (n/a)</td><td>40853.86 (n/a)</td><td>40846.20 (n/a)</td><td>40798.40 (n/a)</td><td>52.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+0.25%)</td><td>0.13 (+0.05%)</td><td>0.13 (-0.03%)</td><td>0.13 (+0.00%)</td><td>0.00 <b>(+294.03%)</b></td><td>321901.20 (-0.00%)</td><td>321619.66 (-0.05%)</td><td>321843.90 (+0.03%)</td><td>320812.60 (-0.25%)</td><td>460.96 <b>(+293.32%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321912.20 (n/a)</td><td>321770.64 (n/a)</td><td>321760.20 (n/a)</td><td>321628.00 (n/a)</td><td>117.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 <b>(-26.67%)</b></td><td>0.02 <b>(-20.81%)</b></td><td>0.02 <b>(-32.29%)</b></td><td>0.02 (+0.71%)</td><td>0.00 <b>(-56.04%)</b></td><td>216.60 (-0.69%)</td><td>183.56 <b>(+20.67%)</b></td><td>187.30 <b>(+47.71%)</b></td><td>154.80 <b>(+36.39%)</b></td><td>26.16 <b>(-41.51%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>152.12 (n/a)</td><td>126.80 (n/a)</td><td>113.50 (n/a)</td><td>44.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 <b>(+62.32%)</b></td><td>0.04 <b>(+38.14%)</b></td><td>0.04 <b>(+31.02%)</b></td><td>0.03 <b>(+43.00%)</b></td><td>0.01 <b>(+82.41%)</b></td><td>194.00 <b>(-30.09%)</b></td><td>150.78 <b>(-26.97%)</b></td><td>147.80 <b>(-23.66%)</b></td><td>109.50 <b>(-38.41%)</b></td><td>30.65 <b>(-24.52%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>277.50 (n/a)</td><td>206.46 (n/a)</td><td>193.60 (n/a)</td><td>177.80 (n/a)</td><td>40.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-14.19%)</td><td>0.03 (+2.40%)</td><td>0.03 (+9.79%)</td><td>0.02 <b>(+20.18%)</b></td><td>0.00 <b>(-66.16%)</b></td><td>165.70 (-16.78%)</td><td>155.58 (-4.62%)</td><td>156.20 (-8.92%)</td><td>144.80 (+16.49%)</td><td>9.62 <b>(-66.67%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.10 (n/a)</td><td>163.12 (n/a)</td><td>171.50 (n/a)</td><td>124.30 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 <b>(+33.84%)</b></td><td>0.03 (+18.58%)</td><td>0.04 (+19.22%)</td><td>0.03 (+15.37%)</td><td>0.01 <b>(+119.91%)</b></td><td>179.50 (-13.33%)</td><td>152.00 (-14.16%)</td><td>146.00 (-16.14%)</td><td>118.80 <b>(-25.28%)</b></td><td>26.93 <b>(+45.95%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.10 (n/a)</td><td>177.08 (n/a)</td><td>174.10 (n/a)</td><td>159.00 (n/a)</td><td>18.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-7.72%)</td><td>0.02 (+6.57%)</td><td>0.02 (+2.93%)</td><td>0.02 <b>(+27.08%)</b></td><td>0.00 <b>(-45.95%)</b></td><td>203.00 <b>(-21.32%)</b></td><td>177.70 (-8.47%)</td><td>180.50 (-2.85%)</td><td>159.10 (+8.38%)</td><td>18.20 <b>(-55.31%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.00 (n/a)</td><td>194.14 (n/a)</td><td>185.80 (n/a)</td><td>146.80 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (+11.94%)</td><td>0.03 (+17.34%)</td><td>0.04 <b>(+24.79%)</b></td><td>0.03 (+7.42%)</td><td>0.00 <b>(+34.12%)</b></td><td>176.80 (-6.95%)</td><td>149.80 (-14.50%)</td><td>144.40 (-19.87%)</td><td>134.00 (-10.67%)</td><td>17.55 (+12.41%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.00 (n/a)</td><td>175.20 (n/a)</td><td>180.20 (n/a)</td><td>150.00 (n/a)</td><td>15.62 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+5.65%)</td><td>0.03 (+11.90%)</td><td>0.03 (+4.95%)</td><td>0.02 (+9.37%)</td><td>0.00 (+7.48%)</td><td>182.90 (-8.55%)</td><td>149.78 (-10.69%)</td><td>154.20 (-4.70%)</td><td>125.30 (-5.36%)</td><td>24.06 (-10.20%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.00 (n/a)</td><td>167.70 (n/a)</td><td>161.80 (n/a)</td><td>132.40 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+6.29%)</td><td>0.03 (+7.45%)</td><td>0.03 (+12.99%)</td><td>0.02 (-6.35%)</td><td>0.01 <b>(+24.88%)</b></td><td>260.60 (+6.76%)</td><td>175.28 (-5.20%)</td><td>152.00 (-11.47%)</td><td>141.90 (-5.90%)</td><td>49.25 <b>(+28.50%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.10 (n/a)</td><td>184.90 (n/a)</td><td>171.70 (n/a)</td><td>150.80 (n/a)</td><td>38.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+7.08%)</td><td>0.03 (+5.02%)</td><td>0.02 (+6.20%)</td><td>0.02 (+10.13%)</td><td>0.01 (+2.64%)</td><td>184.80 (-9.23%)</td><td>159.68 (-5.09%)</td><td>169.60 (-5.83%)</td><td>117.10 (-6.54%)</td><td>26.45 (-13.99%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>168.24 (n/a)</td><td>180.10 (n/a)</td><td>125.30 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-11.45%)</td><td>0.03 (-7.34%)</td><td>0.02 (-9.07%)</td><td>0.02 (-7.98%)</td><td>0.00 (-14.88%)</td><td>204.20 (+8.67%)</td><td>180.68 (+7.74%)</td><td>189.10 (+9.94%)</td><td>142.70 (+12.90%)</td><td>26.17 (+8.45%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>167.70 (n/a)</td><td>172.00 (n/a)</td><td>126.40 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+3.43%)</td><td>0.02 (+5.57%)</td><td>0.02 (+4.37%)</td><td>0.02 (+13.51%)</td><td>0.00 (-6.57%)</td><td>203.50 (-11.87%)</td><td>176.98 (-5.79%)</td><td>182.20 (-4.21%)</td><td>140.50 (-3.30%)</td><td>24.67 <b>(-20.16%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.90 (n/a)</td><td>187.86 (n/a)</td><td>190.20 (n/a)</td><td>145.30 (n/a)</td><td>30.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (+3.72%)</td><td>0.02 (-2.88%)</td><td>0.02 (-7.04%)</td><td>0.02 (+13.67%)</td><td>0.00 (-15.69%)</td><td>271.80 (-12.01%)</td><td>211.52 (+0.80%)</td><td>213.60 (+7.55%)</td><td>157.20 (-3.56%)</td><td>43.07 <b>(-28.06%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>308.90 (n/a)</td><td>209.84 (n/a)</td><td>198.60 (n/a)</td><td>163.00 (n/a)</td><td>59.88 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (-1.10%)</td><td>0.02 (+11.59%)</td><td>0.02 (+9.39%)</td><td>0.02 (+15.53%)</td><td>0.00 <b>(-30.00%)</b></td><td>238.10 (-13.45%)</td><td>193.16 (-11.94%)</td><td>182.30 (-8.58%)</td><td>173.30 (+1.11%)</td><td>26.44 <b>(-39.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>275.10 (n/a)</td><td>219.36 (n/a)</td><td>199.40 (n/a)</td><td>171.40 (n/a)</td><td>43.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (-1.59%)</td><td>0.02 (+0.11%)</td><td>0.02 (-1.86%)</td><td>0.02 (+12.67%)</td><td>0.00 <b>(-25.56%)</b></td><td>225.80 (-11.24%)</td><td>192.54 (-1.38%)</td><td>190.00 (+1.88%)</td><td>160.20 (+1.59%)</td><td>23.75 <b>(-34.73%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>254.40 (n/a)</td><td>195.24 (n/a)</td><td>186.50 (n/a)</td><td>157.70 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (+2.43%)</td><td>0.02 (+11.34%)</td><td>0.02 (+11.50%)</td><td>0.02 (+15.35%)</td><td>0.00 <b>(-26.40%)</b></td><td>219.60 (-13.30%)</td><td>190.68 (-10.91%)</td><td>189.00 (-10.30%)</td><td>174.50 (-2.35%)</td><td>18.26 <b>(-38.03%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.30 (n/a)</td><td>214.02 (n/a)</td><td>210.70 (n/a)</td><td>178.70 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 <b>(+24.11%)</b></td><td>0.06 (+16.45%)</td><td>0.06 (+16.88%)</td><td>0.05 (+15.17%)</td><td>0.01 <b>(+60.95%)</b></td><td>170.70 (-13.17%)</td><td>148.66 (-13.76%)</td><td>145.40 (-14.42%)</td><td>126.80 (-19.44%)</td><td>16.19 (+10.63%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>196.60 (n/a)</td><td>172.38 (n/a)</td><td>169.90 (n/a)</td><td>157.40 (n/a)</td><td>14.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (+8.26%)</td><td>0.07 (-1.25%)</td><td>0.07 (-1.04%)</td><td>0.06 (-8.18%)</td><td>0.02 (+18.08%)</td><td>216.20 (+8.92%)</td><td>170.10 (+2.19%)</td><td>169.50 (+1.07%)</td><td>119.30 (-7.59%)</td><td>34.70 (+13.29%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>166.46 (n/a)</td><td>167.70 (n/a)</td><td>129.10 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-7.86%)</td><td>0.05 (+6.95%)</td><td>0.05 (+15.37%)</td><td>0.04 <b>(+25.83%)</b></td><td>0.01 <b>(-50.96%)</b></td><td>183.90 <b>(-20.53%)</b></td><td>161.36 (-9.36%)</td><td>159.50 (-13.36%)</td><td>140.70 (+8.56%)</td><td>16.71 <b>(-57.18%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>178.02 (n/a)</td><td>184.10 (n/a)</td><td>129.60 (n/a)</td><td>39.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 <b>(-33.25%)</b></td><td>0.05 (-17.90%)</td><td>0.05 <b>(-22.82%)</b></td><td>0.05 (-4.07%)</td><td>0.00 <b>(-71.80%)</b></td><td>201.60 (+4.24%)</td><td>189.52 (+17.99%)</td><td>197.70 <b>(+29.55%)</b></td><td>173.20 <b>(+49.83%)</b></td><td>13.98 <b>(-57.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>160.62 (n/a)</td><td>152.60 (n/a)</td><td>115.60 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (+8.71%)</td><td>0.05 (+4.79%)</td><td>0.05 (+9.64%)</td><td>0.04 (-6.93%)</td><td>0.01 <b>(+36.73%)</b></td><td>204.80 (+7.45%)</td><td>165.40 (-3.55%)</td><td>164.80 (-8.80%)</td><td>128.00 (-8.05%)</td><td>28.26 <b>(+35.15%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>171.48 (n/a)</td><td>180.70 (n/a)</td><td>139.20 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-12.64%)</td><td>0.05 (-16.07%)</td><td>0.04 <b>(-25.21%)</b></td><td>0.04 <b>(-24.34%)</b></td><td>0.01 <b>(+53.05%)</b></td><td>248.60 <b>(+32.16%)</b></td><td>210.62 <b>(+21.66%)</b></td><td>231.90 <b>(+33.74%)</b></td><td>166.70 (+14.49%)</td><td>38.88 <b>(+127.26%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>173.12 (n/a)</td><td>173.40 (n/a)</td><td>145.60 (n/a)</td><td>17.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-13.68%)</td><td>0.05 (-1.22%)</td><td>0.05 (+3.65%)</td><td>0.04 (-4.06%)</td><td>0.01 <b>(-27.17%)</b></td><td>213.90 (+4.19%)</td><td>168.54 (+0.33%)</td><td>156.40 (-3.52%)</td><td>152.50 (+15.88%)</td><td>25.93 (-12.09%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>167.98 (n/a)</td><td>162.10 (n/a)</td><td>131.60 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-4.69%)</td><td>0.05 (+0.57%)</td><td>0.05 (+7.55%)</td><td>0.04 (-3.55%)</td><td>0.01 (+0.57%)</td><td>205.20 (+3.69%)</td><td>177.94 (-0.41%)</td><td>169.90 (-7.01%)</td><td>155.00 (+4.94%)</td><td>21.05 (+13.42%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>178.68 (n/a)</td><td>182.70 (n/a)</td><td>147.70 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (+5.30%)</td><td>0.05 (+10.92%)</td><td>0.06 <b>(+24.51%)</b></td><td>0.04 (-1.53%)</td><td>0.01 <b>(+45.47%)</b></td><td>216.00 (+1.55%)</td><td>168.86 (-8.16%)</td><td>144.70 (-19.70%)</td><td>137.60 (-5.04%)</td><td>37.00 <b>(+41.53%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>183.86 (n/a)</td><td>180.20 (n/a)</td><td>144.90 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (+16.25%)</td><td>0.05 (+14.26%)</td><td>0.05 <b>(+22.72%)</b></td><td>0.04 (+16.65%)</td><td>0.01 (+12.60%)</td><td>212.80 (-14.26%)</td><td>178.46 (-12.71%)</td><td>177.30 (-18.48%)</td><td>125.10 (-13.96%)</td><td>34.71 (-17.43%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>248.20 (n/a)</td><td>204.44 (n/a)</td><td>217.50 (n/a)</td><td>145.40 (n/a)</td><td>42.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (-2.86%)</td><td>0.05 (+1.48%)</td><td>0.05 (-3.70%)</td><td>0.04 (+13.28%)</td><td>0.01 (-5.23%)</td><td>211.10 (-11.71%)</td><td>174.66 (-2.10%)</td><td>180.20 (+3.80%)</td><td>137.50 (+3.00%)</td><td>32.21 (-16.17%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.10 (n/a)</td><td>178.40 (n/a)</td><td>173.60 (n/a)</td><td>133.50 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 <b>(+33.36%)</b></td><td>0.05 (+15.14%)</td><td>0.05 (+9.53%)</td><td>0.04 (+12.90%)</td><td>0.01 <b>(+101.47%)</b></td><td>214.40 (-11.40%)</td><td>186.48 (-11.85%)</td><td>190.90 (-8.70%)</td><td>142.00 <b>(-25.03%)</b></td><td>30.30 <b>(+36.56%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>242.00 (n/a)</td><td>211.56 (n/a)</td><td>209.10 (n/a)</td><td>189.40 (n/a)</td><td>22.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (-0.78%)</td><td>0.04 (+3.70%)</td><td>0.05 (+7.36%)</td><td>0.03 (+6.56%)</td><td>0.01 (-1.02%)</td><td>311.10 (-6.15%)</td><td>208.02 (-4.09%)</td><td>178.20 (-6.90%)</td><td>173.90 (+0.81%)</td><td>58.47 (-9.78%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>331.50 (n/a)</td><td>216.90 (n/a)</td><td>191.40 (n/a)</td><td>172.50 (n/a)</td><td>64.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (+10.55%)</td><td>0.05 (+8.13%)</td><td>0.04 (-4.22%)</td><td>0.04 <b>(+27.72%)</b></td><td>0.01 (-17.84%)</td><td>212.30 <b>(-21.69%)</b></td><td>191.76 (-8.67%)</td><td>199.80 (+4.44%)</td><td>158.50 (-9.58%)</td><td>21.86 <b>(-42.79%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>271.10 (n/a)</td><td>209.96 (n/a)</td><td>191.30 (n/a)</td><td>175.30 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (-4.53%)</td><td>0.03 (-1.20%)</td><td>0.03 (-9.25%)</td><td>0.03 (+8.50%)</td><td>0.00 <b>(-30.46%)</b></td><td>306.60 (-7.82%)</td><td>243.18 (-0.54%)</td><td>237.60 (+10.20%)</td><td>215.50 (+4.71%)</td><td>37.11 <b>(-31.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.60 (n/a)</td><td>244.50 (n/a)</td><td>215.60 (n/a)</td><td>205.80 (n/a)</td><td>54.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (-9.70%)</td><td>0.09 (-8.71%)</td><td>0.09 (-7.81%)</td><td>0.07 (-5.71%)</td><td>0.02 (-18.24%)</td><td>228.70 (+6.03%)</td><td>185.20 (+8.61%)</td><td>192.60 (+8.45%)</td><td>140.70 (+10.79%)</td><td>36.29 (-3.37%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.70 (n/a)</td><td>170.52 (n/a)</td><td>177.60 (n/a)</td><td>127.00 (n/a)</td><td>37.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (-14.10%)</td><td>0.14 (-6.80%)</td><td>0.13 (-6.54%)</td><td>0.13 (+19.11%)</td><td>0.02 <b>(-49.47%)</b></td><td>193.10 (-16.04%)</td><td>181.20 (+4.51%)</td><td>186.20 (+7.01%)</td><td>149.70 (+16.41%)</td><td>17.94 <b>(-51.50%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>230.00 (n/a)</td><td>173.38 (n/a)</td><td>174.00 (n/a)</td><td>128.60 (n/a)</td><td>36.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+10.49%)</td><td>0.10 (+6.36%)</td><td>0.09 (-7.90%)</td><td>0.08 (+14.24%)</td><td>0.02 <b>(+42.97%)</b></td><td>197.40 (-12.46%)</td><td>168.10 (-4.74%)</td><td>188.90 (+8.56%)</td><td>128.80 (-9.49%)</td><td>33.87 (+10.50%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.50 (n/a)</td><td>176.46 (n/a)</td><td>174.00 (n/a)</td><td>142.30 (n/a)</td><td>30.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (+14.46%)</td><td>0.11 (+12.23%)</td><td>0.11 (+10.05%)</td><td>0.07 (-14.68%)</td><td>0.03 <b>(+77.15%)</b></td><td>274.30 (+17.22%)</td><td>189.70 (-7.58%)</td><td>182.90 (-9.10%)</td><td>142.80 (-12.61%)</td><td>52.58 <b>(+77.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>234.00 (n/a)</td><td>205.26 (n/a)</td><td>201.20 (n/a)</td><td>163.40 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+7.87%)</td><td>0.10 (+13.69%)</td><td>0.10 (+14.86%)</td><td>0.07 (+8.84%)</td><td>0.02 <b>(+22.66%)</b></td><td>223.10 (-8.15%)</td><td>167.38 (-11.33%)</td><td>163.20 (-12.91%)</td><td>130.50 (-7.32%)</td><td>38.06 (+2.95%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.90 (n/a)</td><td>188.76 (n/a)</td><td>187.40 (n/a)</td><td>140.80 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+13.27%)</td><td>0.11 (+0.43%)</td><td>0.12 (+7.83%)</td><td>0.06 <b>(-41.69%)</b></td><td>0.03 <b>(+339.92%)</b></td><td>368.00 <b>(+71.56%)</b></td><td>211.40 (+9.06%)</td><td>178.00 (-7.29%)</td><td>159.20 (-11.70%)</td><td>87.89 <b>(+599.22%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>193.84 (n/a)</td><td>192.00 (n/a)</td><td>180.30 (n/a)</td><td>12.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (-6.01%)</td><td>0.09 (-15.17%)</td><td>0.09 <b>(-21.93%)</b></td><td>0.08 (+3.14%)</td><td>0.02 (-4.81%)</td><td>214.10 (-3.03%)</td><td>181.66 (+17.32%)</td><td>185.60 <b>(+28.09%)</b></td><td>124.00 (+6.44%)</td><td>36.02 (-7.76%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.80 (n/a)</td><td>154.84 (n/a)</td><td>144.90 (n/a)</td><td>116.50 (n/a)</td><td>39.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 <b>(-27.74%)</b></td><td>0.08 <b>(-22.80%)</b></td><td>0.09 <b>(-24.42%)</b></td><td>0.08 (-17.22%)</td><td>0.00 <b>(-69.44%)</b></td><td>227.10 <b>(+20.80%)</b></td><td>217.18 <b>(+28.60%)</b></td><td>214.00 <b>(+32.34%)</b></td><td>208.50 <b>(+38.35%)</b></td><td>8.83 <b>(-49.73%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>168.88 (n/a)</td><td>161.70 (n/a)</td><td>150.70 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (-1.01%)</td><td>0.10 (+0.91%)</td><td>0.10 (+2.87%)</td><td>0.08 (-2.69%)</td><td>0.01 (+10.49%)</td><td>198.20 (+2.75%)</td><td>171.38 (-0.67%)</td><td>163.70 (-2.79%)</td><td>149.50 (+1.01%)</td><td>20.88 (+14.20%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>172.54 (n/a)</td><td>168.40 (n/a)</td><td>148.00 (n/a)</td><td>18.29 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+11.30%)</td><td>0.10 (-3.06%)</td><td>0.10 (-7.73%)</td><td>0.07 <b>(-20.07%)</b></td><td>0.02 <b>(+79.81%)</b></td><td>248.20 <b>(+25.10%)</b></td><td>185.12 (+5.99%)</td><td>179.30 (+8.40%)</td><td>136.80 (-10.12%)</td><td>41.11 <b>(+100.12%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>174.66 (n/a)</td><td>165.40 (n/a)</td><td>152.20 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (-1.62%)</td><td>0.10 (+10.69%)</td><td>0.10 (+4.97%)</td><td>0.08 <b>(+28.26%)</b></td><td>0.01 <b>(-43.78%)</b></td><td>196.30 <b>(-22.01%)</b></td><td>170.04 (-11.89%)</td><td>166.90 (-4.74%)</td><td>152.90 (+1.66%)</td><td>17.81 <b>(-56.19%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>251.70 (n/a)</td><td>192.98 (n/a)</td><td>175.20 (n/a)</td><td>150.40 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (-5.16%)</td><td>0.08 (-6.46%)</td><td>0.09 (+0.87%)</td><td>0.07 (-14.84%)</td><td>0.01 <b>(+53.31%)</b></td><td>249.50 (+17.41%)</td><td>215.68 (+7.44%)</td><td>204.00 (-0.87%)</td><td>197.00 (+5.46%)</td><td>21.70 <b>(+90.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>200.74 (n/a)</td><td>205.80 (n/a)</td><td>186.80 (n/a)</td><td>11.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (+1.79%)</td><td>0.10 (+8.52%)</td><td>0.10 (+7.41%)</td><td>0.08 (+8.75%)</td><td>0.01 (-17.56%)</td><td>194.70 (-8.03%)</td><td>169.36 (-8.28%)</td><td>170.70 (-6.87%)</td><td>152.80 (-1.74%)</td><td>16.71 <b>(-26.25%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>184.64 (n/a)</td><td>183.30 (n/a)</td><td>155.50 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 <b>(+35.58%)</b></td><td>0.09 (+6.00%)</td><td>0.09 (+4.94%)</td><td>0.06 (-17.47%)</td><td>0.03 <b>(+204.78%)</b></td><td>279.00 <b>(+21.20%)</b></td><td>208.90 (+0.15%)</td><td>200.80 (-4.70%)</td><td>128.90 <b>(-26.26%)</b></td><td>56.73 <b>(+171.97%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>208.58 (n/a)</td><td>210.70 (n/a)</td><td>174.80 (n/a)</td><td>20.86 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (-12.36%)</td><td>0.08 (-2.14%)</td><td>0.08 (+5.83%)</td><td>0.06 (+0.31%)</td><td>0.01 <b>(-38.83%)</b></td><td>254.10 (-0.31%)</td><td>209.84 (+0.27%)</td><td>201.00 (-5.50%)</td><td>177.10 (+14.11%)</td><td>28.92 <b>(-30.01%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>254.90 (n/a)</td><td>209.28 (n/a)</td><td>212.70 (n/a)</td><td>155.20 (n/a)</td><td>41.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 <b>(+25.85%)</b></td><td>0.20 (+13.93%)</td><td>0.19 (+12.46%)</td><td>0.17 (+12.80%)</td><td>0.03 <b>(+49.15%)</b></td><td>196.20 (-11.34%)</td><td>167.36 (-11.58%)</td><td>170.50 (-11.11%)</td><td>129.00 <b>(-20.52%)</b></td><td>25.52 (+4.62%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.30 (n/a)</td><td>189.28 (n/a)</td><td>191.80 (n/a)</td><td>162.30 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 <b>(+20.94%)</b></td><td>0.20 (+12.48%)</td><td>0.18 (+4.95%)</td><td>0.15 (+13.88%)</td><td>0.05 <b>(+47.91%)</b></td><td>216.80 (-12.16%)</td><td>174.70 (-9.66%)</td><td>182.60 (-4.75%)</td><td>127.20 (-17.35%)</td><td>39.33 (+7.86%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>246.80 (n/a)</td><td>193.38 (n/a)</td><td>191.70 (n/a)</td><td>153.90 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 <b>(-22.66%)</b></td><td>0.21 (-4.51%)</td><td>0.20 (-1.28%)</td><td>0.19 (+10.00%)</td><td>0.02 <b>(-66.08%)</b></td><td>211.80 (-9.06%)</td><td>195.64 (+1.99%)</td><td>201.20 (+1.31%)</td><td>176.40 <b>(+29.33%)</b></td><td>14.48 <b>(-58.44%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>232.90 (n/a)</td><td>191.82 (n/a)</td><td>198.60 (n/a)</td><td>136.40 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 <b>(+39.94%)</b></td><td>0.19 <b>(+20.41%)</b></td><td>0.21 <b>(+30.19%)</b></td><td>0.11 (-17.52%)</td><td>0.06 <b>(+265.33%)</b></td><td>299.90 <b>(+21.22%)</b></td><td>189.10 (-9.30%)</td><td>157.30 <b>(-23.19%)</b></td><td>131.60 <b>(-28.56%)</b></td><td>71.26 <b>(+204.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>247.40 (n/a)</td><td>208.48 (n/a)</td><td>204.80 (n/a)</td><td>184.20 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.30 <b>(+33.48%)</b></td><td>0.24 (+17.86%)</td><td>0.22 (+17.31%)</td><td>0.21 (+15.30%)</td><td>0.04 <b>(+105.76%)</b></td><td>194.70 (-13.27%)</td><td>176.64 (-14.34%)</td><td>182.60 (-14.75%)</td><td>137.90 <b>(-25.10%)</b></td><td>22.67 <b>(+31.75%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>224.50 (n/a)</td><td>206.20 (n/a)</td><td>214.20 (n/a)</td><td>184.10 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (+7.35%)</td><td>0.21 (+16.63%)</td><td>0.21 <b>(+30.14%)</b></td><td>0.17 (+8.71%)</td><td>0.04 <b>(+21.35%)</b></td><td>198.20 (-8.03%)</td><td>162.04 (-13.69%)</td><td>152.70 <b>(-23.19%)</b></td><td>131.60 (-6.86%)</td><td>30.70 (+8.06%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.50 (n/a)</td><td>187.74 (n/a)</td><td>198.80 (n/a)</td><td>141.30 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (+10.30%)</td><td>0.19 (+6.00%)</td><td>0.18 (-8.15%)</td><td>0.17 (+12.63%)</td><td>0.03 (-13.83%)</td><td>221.00 (-11.21%)</td><td>192.56 (-6.56%)</td><td>200.50 (+8.85%)</td><td>157.60 (-9.37%)</td><td>24.14 <b>(-32.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>248.90 (n/a)</td><td>206.08 (n/a)</td><td>184.20 (n/a)</td><td>173.90 (n/a)</td><td>35.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 <b>(+28.36%)</b></td><td>0.21 <b>(+20.17%)</b></td><td>0.19 (+6.80%)</td><td>0.18 (+18.83%)</td><td>0.03 <b>(+121.49%)</b></td><td>177.70 (-15.86%)</td><td>158.08 (-15.77%)</td><td>172.80 (-6.34%)</td><td>132.50 <b>(-22.10%)</b></td><td>22.88 <b>(+43.25%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>187.68 (n/a)</td><td>184.50 (n/a)</td><td>170.10 (n/a)</td><td>15.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (+1.04%)</td><td>0.21 (+7.78%)</td><td>0.22 (+15.99%)</td><td>0.18 (+15.02%)</td><td>0.03 <b>(-23.42%)</b></td><td>209.40 (-13.04%)</td><td>176.44 (-8.32%)</td><td>167.30 (-13.81%)</td><td>151.80 (-0.98%)</td><td>22.93 <b>(-33.14%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>240.80 (n/a)</td><td>192.46 (n/a)</td><td>194.10 (n/a)</td><td>153.30 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (+10.38%)</td><td>0.20 (+15.95%)</td><td>0.20 (+3.44%)</td><td>0.19 <b>(+37.66%)</b></td><td>0.02 <b>(-52.74%)</b></td><td>176.40 <b>(-27.38%)</b></td><td>161.30 (-15.91%)</td><td>163.70 (-3.31%)</td><td>144.80 (-9.39%)</td><td>11.86 <b>(-68.92%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>242.90 (n/a)</td><td>191.82 (n/a)</td><td>169.30 (n/a)</td><td>159.80 (n/a)</td><td>38.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 <b>(+23.34%)</b></td><td>0.19 (+12.53%)</td><td>0.18 (+2.85%)</td><td>0.16 (+8.42%)</td><td>0.03 <b>(+143.05%)</b></td><td>214.00 (-7.76%)</td><td>185.68 (-9.59%)</td><td>194.90 (-2.74%)</td><td>151.40 (-18.91%)</td><td>30.03 <b>(+79.18%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>205.38 (n/a)</td><td>200.40 (n/a)</td><td>186.70 (n/a)</td><td>16.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 <b>(+41.22%)</b></td><td>0.18 (+11.92%)</td><td>0.17 (+8.23%)</td><td>0.13 (-18.70%)</td><td>0.05 <b>(+503.69%)</b></td><td>261.10 <b>(+22.99%)</b></td><td>191.74 (-5.91%)</td><td>191.80 (-7.61%)</td><td>133.30 <b>(-29.17%)</b></td><td>49.29 <b>(+425.43%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>203.78 (n/a)</td><td>207.60 (n/a)</td><td>188.20 (n/a)</td><td>9.38 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (-16.68%)</td><td>0.17 (-2.96%)</td><td>0.17 (+5.71%)</td><td>0.16 (-0.10%)</td><td>0.01 <b>(-65.92%)</b></td><td>222.20 (+0.09%)</td><td>205.04 (+1.94%)</td><td>201.40 (-5.40%)</td><td>198.50 <b>(+20.01%)</b></td><td>9.86 <b>(-59.04%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>222.00 (n/a)</td><td>201.14 (n/a)</td><td>212.90 (n/a)</td><td>165.40 (n/a)</td><td>24.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (-0.27%)</td><td>0.14 (-7.57%)</td><td>0.15 (-3.64%)</td><td>0.09 <b>(-26.16%)</b></td><td>0.03 <b>(+117.79%)</b></td><td>350.30 <b>(+35.41%)</b></td><td>252.26 (+12.07%)</td><td>225.50 (+3.77%)</td><td>203.80 (+0.25%)</td><td>61.87 <b>(+189.13%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>258.70 (n/a)</td><td>225.10 (n/a)</td><td>217.30 (n/a)</td><td>203.30 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (+11.58%)</td><td>0.12 (+2.27%)</td><td>0.12 (+1.19%)</td><td>0.09 (-15.55%)</td><td>0.02 <b>(+115.86%)</b></td><td>229.10 (+18.40%)</td><td>173.82 (+0.43%)</td><td>168.90 (-1.17%)</td><td>135.70 (-10.37%)</td><td>36.66 <b>(+129.31%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>173.08 (n/a)</td><td>170.90 (n/a)</td><td>151.40 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (-2.37%)</td><td>0.12 (+6.94%)</td><td>0.12 (+19.29%)</td><td>0.09 <b>(+67.60%)</b></td><td>0.02 <b>(-49.38%)</b></td><td>216.80 <b>(-40.32%)</b></td><td>181.50 (-15.78%)</td><td>177.00 (-16.19%)</td><td>139.90 (+2.42%)</td><td>29.60 <b>(-67.81%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>363.30 (n/a)</td><td>215.50 (n/a)</td><td>211.20 (n/a)</td><td>136.60 (n/a)</td><td>91.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (+13.73%)</td><td>0.13 (+7.86%)</td><td>0.13 (+11.17%)</td><td>0.09 (+2.36%)</td><td>0.03 <b>(+52.45%)</b></td><td>216.80 (-2.30%)</td><td>166.80 (-5.12%)</td><td>155.00 (-10.04%)</td><td>126.30 (-12.05%)</td><td>40.58 <b>(+31.90%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>221.90 (n/a)</td><td>175.80 (n/a)</td><td>172.30 (n/a)</td><td>143.60 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (+10.12%)</td><td>0.11 (-6.75%)</td><td>0.10 (-10.58%)</td><td>0.09 (-16.01%)</td><td>0.02 <b>(+108.26%)</b></td><td>218.40 (+19.08%)</td><td>185.84 (+9.77%)</td><td>195.70 (+11.83%)</td><td>131.60 (-9.18%)</td><td>32.54 <b>(+118.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>169.30 (n/a)</td><td>175.00 (n/a)</td><td>144.90 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (-4.26%)</td><td>0.11 (-12.18%)</td><td>0.12 (+4.21%)</td><td>0.06 <b>(-42.10%)</b></td><td>0.03 <b>(+133.53%)</b></td><td>318.00 <b>(+72.73%)</b></td><td>211.36 <b>(+23.33%)</b></td><td>170.40 (-4.00%)</td><td>147.30 (+4.47%)</td><td>74.27 <b>(+329.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>171.38 (n/a)</td><td>177.50 (n/a)</td><td>141.00 (n/a)</td><td>17.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (+12.02%)</td><td>0.11 (-3.40%)</td><td>0.10 (-3.19%)</td><td>0.09 (-10.89%)</td><td>0.02 <b>(+73.16%)</b></td><td>225.80 (+12.17%)</td><td>191.66 (+5.57%)</td><td>197.00 (+3.30%)</td><td>136.90 (-10.70%)</td><td>34.11 <b>(+68.33%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>181.54 (n/a)</td><td>190.70 (n/a)</td><td>153.30 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (-6.52%)</td><td>0.12 (+12.35%)</td><td>0.12 (+9.45%)</td><td>0.10 <b>(+65.21%)</b></td><td>0.02 <b>(-42.84%)</b></td><td>203.70 <b>(-39.48%)</b></td><td>175.80 (-16.50%)</td><td>172.70 (-8.62%)</td><td>149.40 (+6.94%)</td><td>26.06 <b>(-64.92%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>336.60 (n/a)</td><td>210.54 (n/a)</td><td>189.00 (n/a)</td><td>139.70 (n/a)</td><td>74.28 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+19.88%)</td><td>0.11 (+17.76%)</td><td>0.11 (+18.97%)</td><td>0.10 (+19.74%)</td><td>0.01 <b>(+20.53%)</b></td><td>205.40 (-16.47%)</td><td>182.90 (-15.05%)</td><td>183.20 (-15.92%)</td><td>153.20 (-16.56%)</td><td>21.66 (-15.04%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>245.90 (n/a)</td><td>215.30 (n/a)</td><td>217.90 (n/a)</td><td>183.60 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (-6.54%)</td><td>0.13 (-8.38%)</td><td>0.13 (-10.55%)</td><td>0.11 (-10.86%)</td><td>0.02 (+5.46%)</td><td>220.20 (+12.18%)</td><td>185.16 (+9.56%)</td><td>187.80 (+11.79%)</td><td>150.70 (+7.03%)</td><td>25.11 <b>(+26.73%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>196.30 (n/a)</td><td>169.00 (n/a)</td><td>168.00 (n/a)</td><td>140.80 (n/a)</td><td>19.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (+2.61%)</td><td>0.12 <b>(-24.93%)</b></td><td>0.12 <b>(-27.95%)</b></td><td>0.07 <b>(-49.59%)</b></td><td>0.04 <b>(+133.07%)</b></td><td>375.40 <b>(+98.41%)</b></td><td>232.34 <b>(+46.38%)</b></td><td>208.90 <b>(+38.80%)</b></td><td>136.80 (-2.49%)</td><td>88.23 <b>(+356.45%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>158.72 (n/a)</td><td>150.50 (n/a)</td><td>140.30 (n/a)</td><td>19.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 <b>(-35.16%)</b></td><td>0.11 <b>(-33.46%)</b></td><td>0.12 <b>(-32.09%)</b></td><td>0.08 <b>(-42.17%)</b></td><td>0.02 <b>(-25.61%)</b></td><td>303.00 <b>(+72.85%)</b></td><td>230.98 <b>(+51.28%)</b></td><td>213.40 <b>(+47.27%)</b></td><td>204.20 <b>(+54.23%)</b></td><td>41.34 <b>(+97.14%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>175.30 (n/a)</td><td>152.68 (n/a)</td><td>144.90 (n/a)</td><td>132.40 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (-7.86%)</td><td>0.13 (-7.53%)</td><td>0.13 (-9.96%)</td><td>0.11 (-8.77%)</td><td>0.02 (-13.23%)</td><td>229.20 (+9.61%)</td><td>186.52 (+7.98%)</td><td>184.50 (+11.08%)</td><td>156.90 (+8.51%)</td><td>26.64 (+4.48%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>209.10 (n/a)</td><td>172.74 (n/a)</td><td>166.10 (n/a)</td><td>144.60 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (-9.34%)</td><td>0.14 (-4.00%)</td><td>0.14 (-2.75%)</td><td>0.12 (+14.71%)</td><td>0.02 <b>(-36.52%)</b></td><td>202.60 (-12.82%)</td><td>179.24 (+2.29%)</td><td>172.90 (+2.79%)</td><td>156.80 (+10.34%)</td><td>22.03 <b>(-38.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.40 (n/a)</td><td>175.22 (n/a)</td><td>168.20 (n/a)</td><td>142.10 (n/a)</td><td>35.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 <b>(-23.32%)</b></td><td>0.13 (-16.74%)</td><td>0.14 (-7.56%)</td><td>0.10 <b>(-31.88%)</b></td><td>0.03 (-19.63%)</td><td>258.50 <b>(+46.79%)</b></td><td>188.44 <b>(+21.00%)</b></td><td>175.80 (+8.12%)</td><td>147.40 <b>(+30.44%)</b></td><td>41.83 <b>(+61.37%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>176.10 (n/a)</td><td>155.74 (n/a)</td><td>162.60 (n/a)</td><td>113.00 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 <b>(+40.45%)</b></td><td>0.15 <b>(+31.63%)</b></td><td>0.14 <b>(+27.94%)</b></td><td>0.11 (+13.70%)</td><td>0.03 <b>(+159.26%)</b></td><td>220.00 (-12.04%)</td><td>173.52 <b>(-21.90%)</b></td><td>178.20 <b>(-21.84%)</b></td><td>133.70 <b>(-28.77%)</b></td><td>36.65 <b>(+60.69%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>222.18 (n/a)</td><td>228.00 (n/a)</td><td>187.70 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 (+2.29%)</td><td>0.13 (+4.59%)</td><td>0.12 (+6.18%)</td><td>0.10 (-2.77%)</td><td>0.03 <b>(+22.79%)</b></td><td>257.10 (+2.84%)</td><td>197.66 (-2.54%)</td><td>198.20 (-5.80%)</td><td>140.80 (-2.22%)</td><td>50.99 <b>(+25.02%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>250.00 (n/a)</td><td>202.82 (n/a)</td><td>210.40 (n/a)</td><td>144.00 (n/a)</td><td>40.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 <b>(+33.45%)</b></td><td>0.11 (+6.11%)</td><td>0.10 (-3.64%)</td><td>0.05 <b>(-39.99%)</b></td><td>0.04 <b>(+160.80%)</b></td><td>404.50 <b>(+66.67%)</b></td><td>207.58 (+10.46%)</td><td>184.30 (+3.77%)</td><td>113.00 <b>(-25.07%)</b></td><td>114.71 <b>(+238.14%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>242.70 (n/a)</td><td>187.92 (n/a)</td><td>177.60 (n/a)</td><td>150.80 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (-1.22%)</td><td>0.10 (-7.67%)</td><td>0.09 (-10.88%)</td><td>0.08 (-14.58%)</td><td>0.02 <b>(+44.63%)</b></td><td>223.80 (+17.05%)</td><td>191.78 (+9.90%)</td><td>198.90 (+12.18%)</td><td>145.80 (+1.25%)</td><td>31.97 <b>(+74.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>174.50 (n/a)</td><td>177.30 (n/a)</td><td>144.00 (n/a)</td><td>18.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 <b>(+24.97%)</b></td><td>0.11 (+7.72%)</td><td>0.10 (+4.15%)</td><td>0.08 (-5.38%)</td><td>0.02 <b>(+168.98%)</b></td><td>223.50 (+5.67%)</td><td>177.48 (-4.51%)</td><td>178.00 (-3.99%)</td><td>135.60 (-19.95%)</td><td>36.16 <b>(+124.14%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>185.86 (n/a)</td><td>185.40 (n/a)</td><td>169.40 (n/a)</td><td>16.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 <b>(+24.77%)</b></td><td>0.11 (+10.92%)</td><td>0.10 (+2.24%)</td><td>0.08 (-4.91%)</td><td>0.02 <b>(+97.90%)</b></td><td>243.00 (+5.19%)</td><td>180.86 (-7.37%)</td><td>184.50 (-2.17%)</td><td>136.00 (-19.86%)</td><td>41.00 <b>(+66.32%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>195.26 (n/a)</td><td>188.60 (n/a)</td><td>169.70 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (-2.59%)</td><td>0.10 (-2.70%)</td><td>0.10 (-8.53%)</td><td>0.09 (+8.25%)</td><td>0.01 <b>(-25.25%)</b></td><td>196.20 (-7.58%)</td><td>182.18 (+2.11%)</td><td>190.50 (+9.36%)</td><td>154.60 (+2.66%)</td><td>16.75 <b>(-30.00%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>178.42 (n/a)</td><td>174.20 (n/a)</td><td>150.60 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (-18.04%)</td><td>0.10 (-9.05%)</td><td>0.09 (-14.81%)</td><td>0.09 (+4.51%)</td><td>0.01 <b>(-60.63%)</b></td><td>207.10 (-4.30%)</td><td>194.52 (+8.40%)</td><td>199.80 (+17.39%)</td><td>180.40 <b>(+21.97%)</b></td><td>12.03 <b>(-54.66%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>216.40 (n/a)</td><td>179.44 (n/a)</td><td>170.20 (n/a)</td><td>147.90 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (+12.47%)</td><td>0.10 (+6.57%)</td><td>0.09 (+3.28%)</td><td>0.08 (-2.88%)</td><td>0.02 <b>(+50.64%)</b></td><td>232.40 (+2.97%)</td><td>191.80 (-4.96%)</td><td>198.70 (-3.17%)</td><td>146.40 (-11.11%)</td><td>32.67 <b>(+37.66%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>201.82 (n/a)</td><td>205.20 (n/a)</td><td>164.70 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 <b>(+33.77%)</b></td><td>0.10 (+13.62%)</td><td>0.11 <b>(+26.38%)</b></td><td>0.05 <b>(-32.98%)</b></td><td>0.03 <b>(+342.69%)</b></td><td>346.40 <b>(+49.25%)</b></td><td>208.58 (-3.60%)</td><td>173.90 <b>(-20.88%)</b></td><td>142.40 <b>(-25.25%)</b></td><td>81.47 <b>(+424.99%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>216.38 (n/a)</td><td>219.80 (n/a)</td><td>190.50 (n/a)</td><td>15.52 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.65 (-4.55%)</td><td>0.54 (-4.95%)</td><td>0.52 (-5.80%)</td><td>0.46 (-2.71%)</td><td>0.07 (-18.71%)</td><td>213.10 (+2.80%)</td><td>186.02 (+4.63%)</td><td>189.70 (+6.16%)</td><td>151.40 (+4.78%)</td><td>22.15 (-14.97%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.68 (n/a)</td><td>0.56 (n/a)</td><td>0.55 (n/a)</td><td>0.47 (n/a)</td><td>0.09 (n/a)</td><td>207.30 (n/a)</td><td>177.78 (n/a)</td><td>178.70 (n/a)</td><td>144.50 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.68 (-15.38%)</td><td>0.57 (-6.25%)</td><td>0.54 (-19.51%)</td><td>0.47 (+14.02%)</td><td>0.10 <b>(-39.68%)</b></td><td>210.60 (-12.29%)</td><td>177.54 (+2.13%)</td><td>182.10 <b>(+24.30%)</b></td><td>145.40 (+18.21%)</td><td>31.14 <b>(-40.60%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.80 (n/a)</td><td>0.61 (n/a)</td><td>0.67 (n/a)</td><td>0.41 (n/a)</td><td>0.17 (n/a)</td><td>240.10 (n/a)</td><td>173.84 (n/a)</td><td>146.50 (n/a)</td><td>123.00 (n/a)</td><td>52.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.60 (-15.04%)</td><td>0.54 (-9.68%)</td><td>0.55 (-0.28%)</td><td>0.47 (-13.14%)</td><td>0.06 (-15.91%)</td><td>207.80 (+15.12%)</td><td>183.54 (+10.67%)</td><td>177.60 (+0.28%)</td><td>163.00 (+17.69%)</td><td>20.88 (+13.55%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.71 (n/a)</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>0.07 (n/a)</td><td>180.50 (n/a)</td><td>165.84 (n/a)</td><td>177.10 (n/a)</td><td>138.50 (n/a)</td><td>18.39 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.60 (+5.12%)</td><td>0.52 (+3.25%)</td><td>0.55 (+13.89%)</td><td>0.38 (-19.77%)</td><td>0.08 <b>(+121.44%)</b></td><td>258.00 <b>(+24.64%)</b></td><td>194.48 (-1.10%)</td><td>178.70 (-12.19%)</td><td>164.90 (-4.85%)</td><td>37.36 <b>(+170.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.04 (n/a)</td><td>207.00 (n/a)</td><td>196.64 (n/a)</td><td>203.50 (n/a)</td><td>173.30 (n/a)</td><td>13.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (-11.31%)</td><td>0.41 (-7.26%)</td><td>0.43 (-3.73%)</td><td>0.30 (-4.04%)</td><td>0.07 <b>(-26.61%)</b></td><td>246.90 (+4.18%)</td><td>185.32 (+6.18%)</td><td>173.40 (+3.89%)</td><td>148.70 (+12.74%)</td><td>37.81 (-11.19%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>237.00 (n/a)</td><td>174.54 (n/a)</td><td>166.90 (n/a)</td><td>131.90 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.54 (+3.33%)</td><td>0.42 (-3.99%)</td><td>0.41 (-18.44%)</td><td>0.34 (+15.06%)</td><td>0.08 <b>(-29.13%)</b></td><td>213.80 (-13.09%)</td><td>180.96 (+0.86%)</td><td>179.40 <b>(+22.62%)</b></td><td>135.70 (-3.21%)</td><td>29.15 <b>(-40.96%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.50 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>246.00 (n/a)</td><td>179.42 (n/a)</td><td>146.30 (n/a)</td><td>140.20 (n/a)</td><td>49.37 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.39 (-10.58%)</td><td>0.35 (-14.96%)</td><td>0.37 (-14.53%)</td><td>0.28 (-15.33%)</td><td>0.05 (-4.86%)</td><td>266.80 (+18.11%)</td><td>212.62 (+17.93%)</td><td>197.00 (+17.05%)</td><td>186.90 (+11.85%)</td><td>32.29 <b>(+26.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>225.90 (n/a)</td><td>180.30 (n/a)</td><td>168.30 (n/a)</td><td>167.10 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.46 <b>(+23.86%)</b></td><td>0.39 <b>(+21.25%)</b></td><td>0.37 (+8.67%)</td><td>0.34 <b>(+40.98%)</b></td><td>0.05 (+5.02%)</td><td>218.10 <b>(-29.07%)</b></td><td>190.28 (-18.29%)</td><td>201.20 (-7.96%)</td><td>159.40 (-19.25%)</td><td>25.22 <b>(-42.21%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>307.50 (n/a)</td><td>232.86 (n/a)</td><td>218.60 (n/a)</td><td>197.40 (n/a)</td><td>43.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (-0.75%)</td><td>0.21 (+6.51%)</td><td>0.22 (+5.68%)</td><td>0.19 <b>(+50.04%)</b></td><td>0.03 <b>(-39.70%)</b></td><td>199.10 <b>(-33.34%)</b></td><td>175.10 (-10.53%)</td><td>169.30 (-5.37%)</td><td>141.60 (+0.71%)</td><td>24.15 <b>(-60.44%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>298.70 (n/a)</td><td>195.70 (n/a)</td><td>178.90 (n/a)</td><td>140.60 (n/a)</td><td>61.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (+3.57%)</td><td>0.21 (-5.63%)</td><td>0.19 (-18.08%)</td><td>0.17 (-13.05%)</td><td>0.04 <b>(+35.27%)</b></td><td>223.30 (+15.04%)</td><td>179.80 (+7.68%)</td><td>190.70 <b>(+22.09%)</b></td><td>140.40 (-3.44%)</td><td>35.86 <b>(+43.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>194.10 (n/a)</td><td>166.98 (n/a)</td><td>156.20 (n/a)</td><td>145.40 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 <b>(-35.05%)</b></td><td>0.19 <b>(-20.45%)</b></td><td>0.19 (-13.24%)</td><td>0.18 (+1.97%)</td><td>0.01 <b>(-84.65%)</b></td><td>209.90 (-1.92%)</td><td>195.02 <b>(+20.86%)</b></td><td>192.70 (+15.25%)</td><td>186.50 <b>(+53.88%)</b></td><td>8.77 <b>(-76.10%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>214.00 (n/a)</td><td>161.36 (n/a)</td><td>167.20 (n/a)</td><td>121.20 (n/a)</td><td>36.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.29 (+9.88%)</td><td>0.20 (-15.50%)</td><td>0.18 <b>(-26.19%)</b></td><td>0.16 (-9.58%)</td><td>0.05 <b>(+51.00%)</b></td><td>230.20 (+10.62%)</td><td>194.16 <b>(+20.99%)</b></td><td>200.20 <b>(+35.55%)</b></td><td>128.40 (-9.00%)</td><td>39.00 <b>(+42.20%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>208.10 (n/a)</td><td>160.48 (n/a)</td><td>147.70 (n/a)</td><td>141.10 (n/a)</td><td>27.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.27 (-15.82%)</td><td>0.24 (+8.09%)</td><td>0.25 <b>(+24.45%)</b></td><td>0.17 (+3.94%)</td><td>0.04 <b>(-37.34%)</b></td><td>211.70 (-3.82%)</td><td>158.66 (-9.64%)</td><td>147.20 (-19.61%)</td><td>136.00 (+18.78%)</td><td>30.21 <b>(-21.42%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>220.10 (n/a)</td><td>175.58 (n/a)</td><td>183.10 (n/a)</td><td>114.50 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (-7.87%)</td><td>0.20 (-2.55%)</td><td>0.20 (-5.19%)</td><td>0.17 (+4.21%)</td><td>0.02 <b>(-38.45%)</b></td><td>213.90 (-4.04%)</td><td>186.84 (+1.09%)</td><td>183.10 (+5.47%)</td><td>163.20 (+8.51%)</td><td>20.50 <b>(-37.02%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>222.90 (n/a)</td><td>184.82 (n/a)</td><td>173.60 (n/a)</td><td>150.40 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.29 <b>(+26.00%)</b></td><td>0.22 (+13.54%)</td><td>0.19 (-1.48%)</td><td>0.17 (+10.82%)</td><td>0.05 <b>(+74.45%)</b></td><td>220.70 (-9.77%)</td><td>176.58 (-10.07%)</td><td>190.70 (+1.49%)</td><td>127.00 <b>(-20.62%)</b></td><td>37.58 <b>(+21.52%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>244.60 (n/a)</td><td>196.36 (n/a)</td><td>187.90 (n/a)</td><td>160.00 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.30 (+17.98%)</td><td>0.21 (+0.15%)</td><td>0.21 (+2.16%)</td><td>0.14 (-6.64%)</td><td>0.06 <b>(+78.42%)</b></td><td>257.80 (+7.15%)</td><td>191.56 (+5.08%)</td><td>172.10 (-2.10%)</td><td>124.60 (-15.24%)</td><td>59.11 <b>(+66.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>240.60 (n/a)</td><td>182.30 (n/a)</td><td>175.80 (n/a)</td><td>147.00 (n/a)</td><td>35.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.28 (+1.42%)</td><td>0.21 (-9.55%)</td><td>0.22 (-7.46%)</td><td>0.13 <b>(-33.89%)</b></td><td>0.06 <b>(+83.94%)</b></td><td>326.90 <b>(+51.27%)</b></td><td>208.06 (+17.51%)</td><td>185.80 (+8.09%)</td><td>144.50 (-1.43%)</td><td>71.01 <b>(+182.67%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>216.10 (n/a)</td><td>177.06 (n/a)</td><td>171.90 (n/a)</td><td>146.60 (n/a)</td><td>25.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.30 <b>(+26.80%)</b></td><td>0.23 (+7.10%)</td><td>0.23 (+3.91%)</td><td>0.18 (-2.95%)</td><td>0.05 <b>(+121.79%)</b></td><td>224.00 (+3.04%)</td><td>184.32 (-4.58%)</td><td>176.40 (-3.71%)</td><td>137.30 <b>(-21.14%)</b></td><td>34.05 <b>(+79.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>217.40 (n/a)</td><td>193.16 (n/a)</td><td>183.20 (n/a)</td><td>174.10 (n/a)</td><td>18.97 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.35 (+5.93%)</td><td>0.23 (-10.54%)</td><td>0.20 (-16.41%)</td><td>0.20 (-0.07%)</td><td>0.07 <b>(+24.09%)</b></td><td>209.90 (+0.10%)</td><td>184.00 (+13.47%)</td><td>199.90 (+19.63%)</td><td>115.50 (-5.56%)</td><td>38.77 (+14.53%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>209.70 (n/a)</td><td>162.16 (n/a)</td><td>167.10 (n/a)</td><td>122.30 (n/a)</td><td>33.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.27 (-9.68%)</td><td>0.22 (+2.37%)</td><td>0.22 (+19.11%)</td><td>0.17 (+1.24%)</td><td>0.04 <b>(-32.16%)</b></td><td>244.10 (-1.21%)</td><td>191.58 (-4.50%)</td><td>182.20 (-16.08%)</td><td>151.80 (+10.72%)</td><td>34.16 <b>(-24.51%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>247.10 (n/a)</td><td>200.60 (n/a)</td><td>217.10 (n/a)</td><td>137.10 (n/a)</td><td>45.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (+0.08%)</td><td>0.22 (-0.11%)</td><td>0.22 (-2.80%)</td><td>0.20 (+3.25%)</td><td>0.02 (-6.56%)</td><td>207.90 (-3.17%)</td><td>183.62 (-0.02%)</td><td>183.80 (+2.91%)</td><td>165.90 (-0.06%)</td><td>16.22 (-11.57%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>183.66 (n/a)</td><td>178.60 (n/a)</td><td>166.00 (n/a)</td><td>18.34 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (-0.53%)</td><td>0.19 (-13.80%)</td><td>0.19 (-15.91%)</td><td>0.14 <b>(-29.95%)</b></td><td>0.04 <b>(+117.19%)</b></td><td>290.40 <b>(+42.77%)</b></td><td>220.76 (+19.06%)</td><td>213.90 (+18.97%)</td><td>172.70 (+0.52%)</td><td>44.62 <b>(+215.73%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>203.40 (n/a)</td><td>185.42 (n/a)</td><td>179.80 (n/a)</td><td>171.80 (n/a)</td><td>14.13 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.32 (+4.62%)</td><td>0.25 (+10.53%)</td><td>0.27 <b>(+25.31%)</b></td><td>0.13 <b>(-30.32%)</b></td><td>0.08 <b>(+69.42%)</b></td><td>322.00 <b>(+43.49%)</b></td><td>180.80 (-1.60%)</td><td>151.60 <b>(-20.17%)</b></td><td>128.90 (-4.45%)</td><td>80.65 <b>(+146.53%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>224.40 (n/a)</td><td>183.74 (n/a)</td><td>189.90 (n/a)</td><td>134.90 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.32 (+5.11%)</td><td>0.26 (+6.26%)</td><td>0.26 (+6.58%)</td><td>0.21 (+9.82%)</td><td>0.05 (+9.15%)</td><td>199.50 (-8.95%)</td><td>164.68 (-5.76%)</td><td>160.50 (-6.14%)</td><td>128.60 (-4.81%)</td><td>28.72 (-4.36%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>219.10 (n/a)</td><td>174.74 (n/a)</td><td>171.00 (n/a)</td><td>135.10 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (+1.45%)</td><td>0.21 (+13.12%)</td><td>0.20 (+15.77%)</td><td>0.18 <b>(+80.96%)</b></td><td>0.03 <b>(-49.04%)</b></td><td>197.10 <b>(-44.73%)</b></td><td>169.18 (-19.28%)</td><td>170.50 (-13.63%)</td><td>140.30 (-1.41%)</td><td>23.90 <b>(-72.44%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>356.60 (n/a)</td><td>209.60 (n/a)</td><td>197.40 (n/a)</td><td>142.30 (n/a)</td><td>86.74 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (-4.09%)</td><td>0.18 (-4.82%)</td><td>0.18 (-0.44%)</td><td>0.16 (+0.29%)</td><td>0.03 (-7.50%)</td><td>219.90 (-0.27%)</td><td>194.30 (+4.82%)</td><td>197.50 (+0.46%)</td><td>146.60 (+4.27%)</td><td>29.64 (-2.77%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>220.50 (n/a)</td><td>185.36 (n/a)</td><td>196.60 (n/a)</td><td>140.60 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (+0.75%)</td><td>0.20 (+0.46%)</td><td>0.19 (-8.88%)</td><td>0.17 (+6.46%)</td><td>0.03 (+7.18%)</td><td>206.90 (-6.08%)</td><td>174.56 (-0.41%)</td><td>182.60 (+9.74%)</td><td>145.00 (-0.75%)</td><td>26.83 (-4.52%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>220.30 (n/a)</td><td>175.28 (n/a)</td><td>166.40 (n/a)</td><td>146.10 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (+11.69%)</td><td>0.20 (+18.92%)</td><td>0.20 <b>(+24.31%)</b></td><td>0.17 <b>(+20.63%)</b></td><td>0.02 (-4.88%)</td><td>201.30 (-17.13%)</td><td>177.88 (-16.21%)</td><td>171.30 (-19.58%)</td><td>157.70 (-10.50%)</td><td>17.28 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>242.90 (n/a)</td><td>212.30 (n/a)</td><td>213.00 (n/a)</td><td>176.20 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (+0.48%)</td><td>0.18 (+0.10%)</td><td>0.18 (-1.93%)</td><td>0.15 (+2.92%)</td><td>0.03 (-1.50%)</td><td>238.90 (-2.85%)</td><td>194.46 (-0.24%)</td><td>189.40 (+1.99%)</td><td>164.40 (-0.48%)</td><td>29.49 (-6.18%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>245.90 (n/a)</td><td>194.92 (n/a)</td><td>185.70 (n/a)</td><td>165.20 (n/a)</td><td>31.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (+7.86%)</td><td>0.20 (+6.19%)</td><td>0.21 (+10.16%)</td><td>0.17 (+0.55%)</td><td>0.02 <b>(+31.27%)</b></td><td>204.20 (-0.54%)</td><td>176.14 (-5.50%)</td><td>169.00 (-9.24%)</td><td>156.90 (-7.27%)</td><td>19.57 <b>(+21.84%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>205.30 (n/a)</td><td>186.40 (n/a)</td><td>186.20 (n/a)</td><td>169.20 (n/a)</td><td>16.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (+11.30%)</td><td>0.17 (+8.64%)</td><td>0.17 (+14.45%)</td><td>0.11 (-14.76%)</td><td>0.05 <b>(+57.04%)</b></td><td>331.20 (+17.32%)</td><td>217.74 (-3.66%)</td><td>201.90 (-12.64%)</td><td>150.40 (-10.16%)</td><td>70.67 <b>(+71.91%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>282.30 (n/a)</td><td>226.02 (n/a)</td><td>231.10 (n/a)</td><td>167.40 (n/a)</td><td>41.11 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (-10.40%)</td><td>0.18 (-9.23%)</td><td>0.17 (-14.25%)</td><td>0.14 (+9.54%)</td><td>0.03 <b>(-27.27%)</b></td><td>241.20 (-8.71%)</td><td>201.56 (+7.87%)</td><td>207.90 (+16.60%)</td><td>153.40 (+11.56%)</td><td>32.61 <b>(-30.07%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>264.20 (n/a)</td><td>186.86 (n/a)</td><td>178.30 (n/a)</td><td>137.50 (n/a)</td><td>46.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.91 (-10.78%)</td><td>0.72 (-10.02%)</td><td>0.71 (-9.94%)</td><td>0.60 (-4.64%)</td><td>0.13 (-12.49%)</td><td>218.70 (+4.84%)</td><td>187.48 (+10.93%)</td><td>183.40 (+11.02%)</td><td>144.20 (+12.04%)</td><td>30.69 (+5.67%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.02 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.63 (n/a)</td><td>0.14 (n/a)</td><td>208.60 (n/a)</td><td>169.00 (n/a)</td><td>165.20 (n/a)</td><td>128.70 (n/a)</td><td>29.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.14 <b>(+48.39%)</b></td><td>0.78 <b>(+20.47%)</b></td><td>0.77 <b>(+23.61%)</b></td><td>0.51 (-5.86%)</td><td>0.25 <b>(+206.80%)</b></td><td>254.60 (+6.22%)</td><td>182.42 (-11.23%)</td><td>169.20 (-19.12%)</td><td>114.80 <b>(-32.63%)</b></td><td>56.08 <b>(+124.82%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.77 (n/a)</td><td>0.65 (n/a)</td><td>0.63 (n/a)</td><td>0.55 (n/a)</td><td>0.08 (n/a)</td><td>239.70 (n/a)</td><td>205.50 (n/a)</td><td>209.20 (n/a)</td><td>170.40 (n/a)</td><td>24.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.04 <b>(+20.64%)</b></td><td>0.77 (+13.09%)</td><td>0.66 (-7.78%)</td><td>0.61 (+13.28%)</td><td>0.20 <b>(+47.12%)</b></td><td>213.90 (-11.72%)</td><td>178.48 (-10.03%)</td><td>198.00 (+8.43%)</td><td>126.20 (-17.08%)</td><td>41.40 (+5.85%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.86 (n/a)</td><td>0.68 (n/a)</td><td>0.72 (n/a)</td><td>0.54 (n/a)</td><td>0.13 (n/a)</td><td>242.30 (n/a)</td><td>198.38 (n/a)</td><td>182.60 (n/a)</td><td>152.20 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.00 (-2.27%)</td><td>0.00 (-1.85%)</td><td>0.00 (-2.33%)</td><td>0.00 (-2.33%)</td><td>0.00 <b>(+22.47%)</b></td><td>983.98 (+2.73%)</td><td>972.27 (+1.94%)</td><td>974.97 (+1.92%)</td><td>959.59 (+1.98%)</td><td>12.07 <b>(+68.33%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>957.84 (n/a)</td><td>953.73 (n/a)</td><td>956.58 (n/a)</td><td>940.95 (n/a)</td><td>7.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.01 (+2.41%)</td><td>0.01 (+2.49%)</td><td>0.01 (+2.44%)</td><td>0.01 (+5.41%)</td><td>0.00 <b>(-21.00%)</b></td><td>1044.06 (-5.14%)</td><td>994.57 (-2.23%)</td><td>980.77 (-2.04%)</td><td>959.25 (-2.47%)</td><td>33.98 <b>(-28.38%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1100.64 (n/a)</td><td>1017.29 (n/a)</td><td>1001.21 (n/a)</td><td>983.56 (n/a)</td><td>47.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.94 (-0.24%)</td><td>0.93 (-0.03%)</td><td>0.93 (-0.91%)</td><td>0.92 (+1.25%)</td><td>0.01 <b>(-55.91%)</b></td><td>2267.71 (-1.23%)</td><td>2254.15 (+0.02%)</td><td>2257.93 (+0.92%)</td><td>2237.80 (+0.24%)</td><td>12.21 <b>(-56.15%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.94 (n/a)</td><td>0.91 (n/a)</td><td>0.01 (n/a)</td><td>2295.97 (n/a)</td><td>2253.66 (n/a)</td><td>2237.45 (n/a)</td><td>2232.42 (n/a)</td><td>27.85 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill_stream</summary>


### test_swiglu_prefill_stream[k_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.44 (-1.42%)</td><td>0.44 (-1.89%)</td><td>0.44 (-2.50%)</td><td>0.43 (-0.75%)</td><td>0.00 <b>(-20.15%)</b></td><td>1208.31 (+0.77%)</td><td>1195.78 (+1.93%)</td><td>1200.15 (+2.59%)</td><td>1179.22 (+1.45%)</td><td>12.34 (-18.01%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.01 (n/a)</td><td>1199.06 (n/a)</td><td>1173.15 (n/a)</td><td>1169.90 (n/a)</td><td>1162.41 (n/a)</td><td>15.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.37 (-0.88%)</td><td>0.37 (-0.35%)</td><td>0.37 (+0.08%)</td><td>0.36 (+0.14%)</td><td>0.00 <b>(-35.88%)</b></td><td>1440.88 (-0.14%)</td><td>1427.48 (+0.33%)</td><td>1429.66 (-0.10%)</td><td>1410.77 (+0.88%)</td><td>12.52 <b>(-35.23%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1442.89 (n/a)</td><td>1422.72 (n/a)</td><td>1431.10 (n/a)</td><td>1398.44 (n/a)</td><td>19.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.37 (+2.54%)</td><td>0.36 (+0.87%)</td><td>0.36 (+0.51%)</td><td>0.35 (+0.57%)</td><td>0.01 <b>(+100.03%)</b></td><td>1482.07 (-0.54%)</td><td>1460.73 (-0.83%)</td><td>1463.88 (-0.50%)</td><td>1425.32 (-2.47%)</td><td>23.75 <b>(+96.36%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.00 (n/a)</td><td>1490.13 (n/a)</td><td>1473.01 (n/a)</td><td>1471.24 (n/a)</td><td>1461.47 (n/a)</td><td>12.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.19 (+14.32%)</td><td>4.97 (+2.92%)</td><td>5.16 (+8.02%)</td><td>4.14 (-4.21%)</td><td>0.84 <b>(+59.79%)</b></td><td>253.40 (+4.41%)</td><td>215.48 (-1.60%)</td><td>203.20 (-7.43%)</td><td>169.30 (-12.55%)</td><td>35.21 <b>(+48.99%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.42 (n/a)</td><td>4.83 (n/a)</td><td>4.78 (n/a)</td><td>4.32 (n/a)</td><td>0.53 (n/a)</td><td>242.70 (n/a)</td><td>218.98 (n/a)</td><td>219.50 (n/a)</td><td>193.60 (n/a)</td><td>23.63 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.44 (+0.88%)</td><td>4.77 (-1.12%)</td><td>5.05 (+3.53%)</td><td>4.00 (-1.51%)</td><td>0.67 <b>(+24.71%)</b></td><td>262.10 (+1.55%)</td><td>223.68 (+1.76%)</td><td>207.50 (-3.44%)</td><td>192.60 (-0.87%)</td><td>32.79 <b>(+27.63%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.40 (n/a)</td><td>4.82 (n/a)</td><td>4.88 (n/a)</td><td>4.06 (n/a)</td><td>0.54 (n/a)</td><td>258.10 (n/a)</td><td>219.82 (n/a)</td><td>214.90 (n/a)</td><td>194.30 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.59 (+3.13%)</td><td>5.02 (+10.40%)</td><td>5.08 (+4.90%)</td><td>4.51 <b>(+48.41%)</b></td><td>0.48 <b>(-47.13%)</b></td><td>232.30 <b>(-32.61%)</b></td><td>210.60 (-12.37%)</td><td>206.30 (-4.67%)</td><td>187.60 (-3.05%)</td><td>20.33 <b>(-66.31%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.42 (n/a)</td><td>4.54 (n/a)</td><td>4.85 (n/a)</td><td>3.04 (n/a)</td><td>0.91 (n/a)</td><td>344.70 (n/a)</td><td>240.34 (n/a)</td><td>216.40 (n/a)</td><td>193.50 (n/a)</td><td>60.35 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.12 (+0.87%)</td><td>4.56 (-2.43%)</td><td>4.41 (-3.85%)</td><td>4.24 (-3.54%)</td><td>0.37 <b>(+43.27%)</b></td><td>247.20 (+3.69%)</td><td>231.30 (+2.77%)</td><td>237.80 (+3.98%)</td><td>204.90 (-0.82%)</td><td>17.81 <b>(+48.52%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.07 (n/a)</td><td>4.67 (n/a)</td><td>4.59 (n/a)</td><td>4.40 (n/a)</td><td>0.26 (n/a)</td><td>238.40 (n/a)</td><td>225.06 (n/a)</td><td>228.70 (n/a)</td><td>206.60 (n/a)</td><td>11.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.02 (-13.24%)</td><td>7.08 (-10.16%)</td><td>7.29 (-8.68%)</td><td>5.96 (-5.44%)</td><td>0.79 <b>(-27.29%)</b></td><td>352.00 (+5.74%)</td><td>299.24 (+10.66%)</td><td>287.70 (+9.52%)</td><td>261.60 (+15.24%)</td><td>35.10 (-11.89%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.24 (n/a)</td><td>7.88 (n/a)</td><td>7.98 (n/a)</td><td>6.30 (n/a)</td><td>1.09 (n/a)</td><td>332.90 (n/a)</td><td>270.42 (n/a)</td><td>262.70 (n/a)</td><td>227.00 (n/a)</td><td>39.84 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.32 (+9.23%)</td><td>7.59 (+7.13%)</td><td>7.85 (+9.77%)</td><td>6.38 (+0.01%)</td><td>0.73 <b>(+58.93%)</b></td><td>328.60 (+0.00%)</td><td>278.74 (-6.22%)</td><td>267.20 (-8.90%)</td><td>252.00 (-8.46%)</td><td>29.50 <b>(+47.47%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.62 (n/a)</td><td>7.08 (n/a)</td><td>7.15 (n/a)</td><td>6.38 (n/a)</td><td>0.46 (n/a)</td><td>328.60 (n/a)</td><td>297.22 (n/a)</td><td>293.30 (n/a)</td><td>275.30 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.29 (+8.66%)</td><td>8.00 (+4.75%)</td><td>7.82 (+4.50%)</td><td>7.05 (-0.37%)</td><td>0.92 <b>(+67.87%)</b></td><td>297.50 (+0.37%)</td><td>264.68 (-3.93%)</td><td>268.20 (-4.32%)</td><td>225.80 (-7.95%)</td><td>29.43 <b>(+57.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>8.55 (n/a)</td><td>7.64 (n/a)</td><td>7.48 (n/a)</td><td>7.08 (n/a)</td><td>0.55 (n/a)</td><td>296.40 (n/a)</td><td>275.50 (n/a)</td><td>280.30 (n/a)</td><td>245.30 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.83 (+2.41%)</td><td>8.68 (+10.93%)</td><td>8.35 (-2.97%)</td><td>7.89 <b>(+58.89%)</b></td><td>0.85 <b>(-52.98%)</b></td><td>265.70 <b>(-37.07%)</b></td><td>243.40 (-13.96%)</td><td>251.30 (+3.08%)</td><td>213.40 (-2.33%)</td><td>22.95 <b>(-71.99%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.60 (n/a)</td><td>7.83 (n/a)</td><td>8.60 (n/a)</td><td>4.97 (n/a)</td><td>1.80 (n/a)</td><td>422.20 (n/a)</td><td>282.88 (n/a)</td><td>243.80 (n/a)</td><td>218.50 (n/a)</td><td>81.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.96 (-4.17%)</td><td>8.35 (-1.65%)</td><td>8.37 (+1.75%)</td><td>7.67 (-1.76%)</td><td>0.58 <b>(-24.52%)</b></td><td>273.60 (+1.79%)</td><td>252.02 (+1.42%)</td><td>250.70 (-1.72%)</td><td>234.00 (+4.37%)</td><td>17.64 (-19.99%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.35 (n/a)</td><td>8.49 (n/a)</td><td>8.22 (n/a)</td><td>7.80 (n/a)</td><td>0.77 (n/a)</td><td>268.80 (n/a)</td><td>248.48 (n/a)</td><td>255.10 (n/a)</td><td>224.20 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.48 (-7.01%)</td><td>8.47 (+5.24%)</td><td>8.72 (+14.90%)</td><td>7.48 (+12.82%)</td><td>0.80 <b>(-40.18%)</b></td><td>280.30 (-11.35%)</td><td>249.42 (-6.19%)</td><td>240.60 (-12.95%)</td><td>221.30 (+7.58%)</td><td>23.79 <b>(-41.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>10.19 (n/a)</td><td>8.05 (n/a)</td><td>7.59 (n/a)</td><td>6.63 (n/a)</td><td>1.33 (n/a)</td><td>316.20 (n/a)</td><td>265.88 (n/a)</td><td>276.40 (n/a)</td><td>205.70 (n/a)</td><td>40.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>12.38 (+0.47%)</td><td>11.55 (+1.80%)</td><td>11.11 (-4.69%)</td><td>10.96 (+12.02%)</td><td>0.69 <b>(-35.49%)</b></td><td>382.80 (-10.73%)</td><td>364.10 (-2.23%)</td><td>377.40 (+4.89%)</td><td>338.80 (-0.47%)</td><td>21.33 <b>(-42.51%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.32 (n/a)</td><td>11.35 (n/a)</td><td>11.66 (n/a)</td><td>9.78 (n/a)</td><td>1.07 (n/a)</td><td>428.80 (n/a)</td><td>372.42 (n/a)</td><td>359.80 (n/a)</td><td>340.40 (n/a)</td><td>37.09 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>12.18 (-2.19%)</td><td>11.63 (+4.14%)</td><td>11.80 (+5.54%)</td><td>10.62 (+3.91%)</td><td>0.64 <b>(-22.38%)</b></td><td>394.90 (-3.78%)</td><td>361.64 (-4.14%)</td><td>355.50 (-5.25%)</td><td>344.50 (+2.26%)</td><td>20.86 <b>(-23.36%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.45 (n/a)</td><td>11.17 (n/a)</td><td>11.18 (n/a)</td><td>10.22 (n/a)</td><td>0.83 (n/a)</td><td>410.40 (n/a)</td><td>377.24 (n/a)</td><td>375.20 (n/a)</td><td>336.90 (n/a)</td><td>27.22 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>12.84 (+7.56%)</td><td>10.85 (-2.99%)</td><td>10.96 (-2.49%)</td><td>8.60 (-19.49%)</td><td>1.61 <b>(+209.98%)</b></td><td>487.80 <b>(+24.19%)</b></td><td>393.86 (+4.83%)</td><td>382.60 (+2.55%)</td><td>326.70 (-7.03%)</td><td>61.64 <b>(+258.90%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>11.94 (n/a)</td><td>11.18 (n/a)</td><td>11.24 (n/a)</td><td>10.68 (n/a)</td><td>0.52 (n/a)</td><td>392.80 (n/a)</td><td>375.70 (n/a)</td><td>373.10 (n/a)</td><td>351.40 (n/a)</td><td>17.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>14.78 (+16.65%)</td><td>13.28 (+14.81%)</td><td>12.79 (+5.43%)</td><td>12.24 <b>(+24.66%)</b></td><td>1.04 (-14.62%)</td><td>342.80 (-19.78%)</td><td>317.30 (-13.30%)</td><td>327.80 (-5.15%)</td><td>283.70 (-14.26%)</td><td>24.05 <b>(-41.33%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.67 (n/a)</td><td>11.57 (n/a)</td><td>12.14 (n/a)</td><td>9.82 (n/a)</td><td>1.22 (n/a)</td><td>427.30 (n/a)</td><td>365.98 (n/a)</td><td>345.60 (n/a)</td><td>330.90 (n/a)</td><td>40.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>15.04 (+17.12%)</td><td>13.41 (+11.38%)</td><td>13.70 (+12.71%)</td><td>11.98 (+14.99%)</td><td>1.19 <b>(+20.27%)</b></td><td>350.20 (-13.06%)</td><td>314.72 (-10.19%)</td><td>306.10 (-11.28%)</td><td>278.90 (-14.63%)</td><td>27.71 (-10.82%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.84 (n/a)</td><td>12.04 (n/a)</td><td>12.16 (n/a)</td><td>10.41 (n/a)</td><td>0.99 (n/a)</td><td>402.80 (n/a)</td><td>350.42 (n/a)</td><td>345.00 (n/a)</td><td>326.70 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>14.49 (+3.70%)</td><td>12.74 (+4.77%)</td><td>12.44 (+0.11%)</td><td>11.89 (+17.59%)</td><td>1.01 <b>(-30.87%)</b></td><td>352.70 (-14.97%)</td><td>330.72 (-5.26%)</td><td>337.10 (-0.12%)</td><td>289.50 (-3.56%)</td><td>24.01 <b>(-44.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>13.97 (n/a)</td><td>12.16 (n/a)</td><td>12.43 (n/a)</td><td>10.11 (n/a)</td><td>1.46 (n/a)</td><td>414.80 (n/a)</td><td>349.08 (n/a)</td><td>337.50 (n/a)</td><td>300.20 (n/a)</td><td>43.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>13.73 (+10.24%)</td><td>11.58 (-1.62%)</td><td>11.97 (-0.17%)</td><td>8.65 (-18.14%)</td><td>1.90 <b>(+142.15%)</b></td><td>484.70 <b>(+22.15%)</b></td><td>371.14 (+3.77%)</td><td>350.40 (+0.17%)</td><td>305.50 (-9.29%)</td><td>68.80 <b>(+176.10%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.46 (n/a)</td><td>11.77 (n/a)</td><td>11.99 (n/a)</td><td>10.57 (n/a)</td><td>0.78 (n/a)</td><td>396.80 (n/a)</td><td>357.66 (n/a)</td><td>349.80 (n/a)</td><td>336.80 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>14.03 (+10.30%)</td><td>11.87 (+7.33%)</td><td>12.42 (+14.67%)</td><td>9.55 (-3.16%)</td><td>1.98 <b>(+71.72%)</b></td><td>439.10 (+3.24%)</td><td>361.64 (-5.44%)</td><td>337.80 (-12.80%)</td><td>298.80 (-9.34%)</td><td>62.63 <b>(+62.65%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.72 (n/a)</td><td>11.06 (n/a)</td><td>10.83 (n/a)</td><td>9.86 (n/a)</td><td>1.15 (n/a)</td><td>425.30 (n/a)</td><td>382.44 (n/a)</td><td>387.40 (n/a)</td><td>329.60 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.44 (+12.50%)</td><td>2.86 (+11.24%)</td><td>2.77 (+6.87%)</td><td>2.58 <b>(+26.70%)</b></td><td>0.34 (-7.92%)</td><td>202.90 <b>(-21.08%)</b></td><td>184.92 (-10.76%)</td><td>189.10 (-6.43%)</td><td>152.60 (-11.12%)</td><td>19.82 <b>(-37.20%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.05 (n/a)</td><td>2.57 (n/a)</td><td>2.59 (n/a)</td><td>2.04 (n/a)</td><td>0.37 (n/a)</td><td>257.10 (n/a)</td><td>207.22 (n/a)</td><td>202.10 (n/a)</td><td>171.70 (n/a)</td><td>31.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.83 (+2.29%)</td><td>4.83 (+1.75%)</td><td>4.67 (-1.06%)</td><td>3.93 (+4.47%)</td><td>0.72 (-6.38%)</td><td>267.10 (-4.27%)</td><td>220.86 (-2.09%)</td><td>224.70 (+1.08%)</td><td>179.90 (-2.23%)</td><td>32.96 (-12.51%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.70 (n/a)</td><td>4.75 (n/a)</td><td>4.72 (n/a)</td><td>3.76 (n/a)</td><td>0.77 (n/a)</td><td>279.00 (n/a)</td><td>225.58 (n/a)</td><td>222.30 (n/a)</td><td>184.00 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.75 (-10.29%)</td><td>7.11 (-5.33%)</td><td>7.45 (-4.66%)</td><td>5.87 (+3.40%)</td><td>0.78 <b>(-33.93%)</b></td><td>357.00 (-3.30%)</td><td>298.08 (+4.39%)</td><td>281.70 (+4.88%)</td><td>270.60 (+11.45%)</td><td>35.79 <b>(-29.48%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>8.64 (n/a)</td><td>7.51 (n/a)</td><td>7.81 (n/a)</td><td>5.68 (n/a)</td><td>1.17 (n/a)</td><td>369.20 (n/a)</td><td>285.54 (n/a)</td><td>268.60 (n/a)</td><td>242.80 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.22 (-14.76%)</td><td>2.90 (+1.84%)</td><td>3.12 <b>(+21.44%)</b></td><td>2.46 (+16.02%)</td><td>0.38 <b>(-49.18%)</b></td><td>213.10 (-13.79%)</td><td>183.40 (-5.57%)</td><td>167.90 (-17.66%)</td><td>162.80 (+17.38%)</td><td>25.31 <b>(-47.87%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.78 (n/a)</td><td>2.85 (n/a)</td><td>2.57 (n/a)</td><td>2.12 (n/a)</td><td>0.75 (n/a)</td><td>247.20 (n/a)</td><td>194.22 (n/a)</td><td>203.90 (n/a)</td><td>138.70 (n/a)</td><td>48.55 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (+8.02%)</td><td>0.19 (-0.06%)</td><td>0.20 (+5.10%)</td><td>0.13 (-19.02%)</td><td>0.05 <b>(+66.55%)</b></td><td>249.70 <b>(+23.49%)</b></td><td>176.94 (+3.64%)</td><td>165.50 (-4.83%)</td><td>126.30 (-7.40%)</td><td>46.51 <b>(+97.14%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>202.20 (n/a)</td><td>170.72 (n/a)</td><td>173.90 (n/a)</td><td>136.40 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.28 <b>(+31.74%)</b></td><td>0.20 (+6.83%)</td><td>0.21 (+2.44%)</td><td>0.15 (+3.10%)</td><td>0.05 <b>(+105.88%)</b></td><td>212.50 (-3.01%)</td><td>170.18 (-3.36%)</td><td>159.40 (-2.39%)</td><td>118.80 <b>(-24.09%)</b></td><td>39.97 <b>(+55.89%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.10 (n/a)</td><td>176.10 (n/a)</td><td>163.30 (n/a)</td><td>156.50 (n/a)</td><td>25.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.55 (+8.08%)</td><td>0.42 (+8.40%)</td><td>0.45 <b>(+24.85%)</b></td><td>0.18 <b>(-42.16%)</b></td><td>0.15 <b>(+79.59%)</b></td><td>361.30 <b>(+72.87%)</b></td><td>182.48 (+4.96%)</td><td>146.90 (-19.90%)</td><td>119.80 (-7.49%)</td><td>101.30 <b>(+201.54%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>209.00 (n/a)</td><td>173.86 (n/a)</td><td>183.40 (n/a)</td><td>129.50 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (+18.39%)</td><td>0.40 <b>(+20.67%)</b></td><td>0.40 (+18.71%)</td><td>0.29 <b>(+50.13%)</b></td><td>0.08 (-9.06%)</td><td>226.30 <b>(-33.40%)</b></td><td>170.50 <b>(-20.22%)</b></td><td>162.40 (-15.72%)</td><td>131.70 (-15.58%)</td><td>35.07 <b>(-51.39%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>339.80 (n/a)</td><td>213.72 (n/a)</td><td>192.70 (n/a)</td><td>156.00 (n/a)</td><td>72.14 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (+15.87%)</td><td>0.42 <b>(+21.20%)</b></td><td>0.42 (+17.43%)</td><td>0.35 <b>(+32.69%)</b></td><td>0.06 <b>(-22.00%)</b></td><td>188.00 <b>(-24.65%)</b></td><td>157.36 (-19.83%)</td><td>154.60 (-14.87%)</td><td>131.30 (-13.73%)</td><td>24.25 <b>(-49.71%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>249.50 (n/a)</td><td>196.28 (n/a)</td><td>181.60 (n/a)</td><td>152.20 (n/a)</td><td>48.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.03 <b>(+24.42%)</b></td><td>0.93 <b>(+29.11%)</b></td><td>0.96 <b>(+36.98%)</b></td><td>0.78 (+16.36%)</td><td>0.10 <b>(+61.47%)</b></td><td>169.10 (-14.03%)</td><td>142.46 <b>(-22.19%)</b></td><td>136.80 <b>(-27.00%)</b></td><td>127.80 (-19.62%)</td><td>16.55 (+14.02%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.82 (n/a)</td><td>0.72 (n/a)</td><td>0.70 (n/a)</td><td>0.67 (n/a)</td><td>0.06 (n/a)</td><td>196.70 (n/a)</td><td>183.08 (n/a)</td><td>187.40 (n/a)</td><td>159.00 (n/a)</td><td>14.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.09 <b>(+52.22%)</b></td><td>0.88 <b>(+34.53%)</b></td><td>0.85 <b>(+28.86%)</b></td><td>0.77 <b>(+32.53%)</b></td><td>0.13 <b>(+141.93%)</b></td><td>170.10 <b>(-24.53%)</b></td><td>151.68 <b>(-24.87%)</b></td><td>153.60 <b>(-22.42%)</b></td><td>119.80 <b>(-34.32%)</b></td><td>20.69 <b>(+20.27%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.72 (n/a)</td><td>0.65 (n/a)</td><td>0.66 (n/a)</td><td>0.58 (n/a)</td><td>0.05 (n/a)</td><td>225.40 (n/a)</td><td>201.90 (n/a)</td><td>198.00 (n/a)</td><td>182.40 (n/a)</td><td>17.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.89 (-13.06%)</td><td>0.77 (+12.59%)</td><td>0.76 <b>(+25.99%)</b></td><td>0.59 (+9.83%)</td><td>0.11 <b>(-43.91%)</b></td><td>220.50 (-8.96%)</td><td>173.80 (-14.40%)</td><td>171.40 <b>(-20.65%)</b></td><td>146.70 (+15.06%)</td><td>28.50 <b>(-40.08%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.03 (n/a)</td><td>0.68 (n/a)</td><td>0.61 (n/a)</td><td>0.54 (n/a)</td><td>0.20 (n/a)</td><td>242.20 (n/a)</td><td>203.04 (n/a)</td><td>216.00 (n/a)</td><td>127.50 (n/a)</td><td>47.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.92 (-9.51%)</td><td>0.78 (+7.60%)</td><td>0.74 (+12.84%)</td><td>0.63 (+7.81%)</td><td>0.12 <b>(-30.44%)</b></td><td>206.50 (-7.23%)</td><td>171.90 (-8.70%)</td><td>177.90 (-11.40%)</td><td>141.90 (+10.51%)</td><td>26.27 <b>(-26.69%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.02 (n/a)</td><td>0.72 (n/a)</td><td>0.65 (n/a)</td><td>0.59 (n/a)</td><td>0.17 (n/a)</td><td>222.60 (n/a)</td><td>188.28 (n/a)</td><td>200.80 (n/a)</td><td>128.40 (n/a)</td><td>35.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (-5.06%)</td><td>0.09 (-0.31%)</td><td>0.09 (-1.76%)</td><td>0.07 <b>(+31.97%)</b></td><td>0.01 <b>(-50.25%)</b></td><td>229.30 <b>(-24.25%)</b></td><td>193.16 (-4.49%)</td><td>189.70 (+1.77%)</td><td>162.00 (+5.33%)</td><td>24.60 <b>(-59.77%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>302.70 (n/a)</td><td>202.24 (n/a)</td><td>186.40 (n/a)</td><td>153.80 (n/a)</td><td>61.16 (n/a)</td>
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
