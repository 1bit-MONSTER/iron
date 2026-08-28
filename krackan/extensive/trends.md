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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (+11.23%)</td><td>0.04 (+6.52%)</td><td>0.04 (+6.02%)</td><td>0.03 (-8.34%)</td><td>0.01 <b>(+56.01%)</b></td><td>207.50 (+9.10%)</td><td>162.92 (-4.47%)</td><td>163.30 (-5.66%)</td><td>124.20 (-10.07%)</td><td>31.57 <b>(+53.87%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.20 (n/a)</td><td>170.54 (n/a)</td><td>173.10 (n/a)</td><td>138.10 (n/a)</td><td>20.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (-5.55%)</td><td>0.03 (-12.20%)</td><td>0.03 (-11.58%)</td><td>0.03 (-8.08%)</td><td>0.01 (+7.93%)</td><td>241.70 (+8.82%)</td><td>199.08 (+14.55%)</td><td>184.50 (+13.05%)</td><td>162.20 (+5.87%)</td><td>34.42 <b>(+23.81%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>222.10 (n/a)</td><td>173.80 (n/a)</td><td>163.20 (n/a)</td><td>153.20 (n/a)</td><td>27.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 <b>(+31.24%)</b></td><td>0.04 <b>(+20.55%)</b></td><td>0.04 (+7.62%)</td><td>0.03 (+18.43%)</td><td>0.01 <b>(+40.56%)</b></td><td>204.10 (-15.56%)</td><td>155.78 (-16.34%)</td><td>164.90 (-7.10%)</td><td>105.50 <b>(-23.77%)</b></td><td>36.70 (-12.34%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>186.20 (n/a)</td><td>177.50 (n/a)</td><td>138.40 (n/a)</td><td>41.86 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 <b>(+42.89%)</b></td><td>0.04 (+8.27%)</td><td>0.03 (-8.15%)</td><td>0.03 <b>(+20.84%)</b></td><td>0.01 <b>(+97.31%)</b></td><td>202.20 (-17.23%)</td><td>176.70 (-5.55%)</td><td>191.50 (+8.87%)</td><td>116.30 <b>(-29.98%)</b></td><td>35.29 (+9.00%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>244.30 (n/a)</td><td>187.08 (n/a)</td><td>175.90 (n/a)</td><td>166.10 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (+3.45%)</td><td>0.03 (-0.79%)</td><td>0.04 (-1.44%)</td><td>0.03 (-2.41%)</td><td>0.00 <b>(+46.76%)</b></td><td>195.10 (+2.47%)</td><td>178.26 (+1.03%)</td><td>175.20 (+1.45%)</td><td>160.70 (-3.37%)</td><td>13.58 <b>(+45.49%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.40 (n/a)</td><td>176.44 (n/a)</td><td>172.70 (n/a)</td><td>166.30 (n/a)</td><td>9.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (+6.50%)</td><td>0.04 (+12.36%)</td><td>0.04 (+13.64%)</td><td>0.04 (+17.23%)</td><td>0.00 <b>(-24.87%)</b></td><td>172.20 (-14.71%)</td><td>159.76 (-11.32%)</td><td>154.60 (-12.01%)</td><td>149.40 (-6.10%)</td><td>9.86 <b>(-39.72%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>180.16 (n/a)</td><td>175.70 (n/a)</td><td>159.10 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (-0.88%)</td><td>0.03 (+8.95%)</td><td>0.03 (+7.63%)</td><td>0.03 (+18.15%)</td><td>0.00 <b>(-29.75%)</b></td><td>194.30 (-15.37%)</td><td>180.76 (-9.73%)</td><td>189.70 (-7.10%)</td><td>144.00 (+0.91%)</td><td>20.84 <b>(-39.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>200.24 (n/a)</td><td>204.20 (n/a)</td><td>142.70 (n/a)</td><td>34.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (+0.62%)</td><td>0.03 (+1.75%)</td><td>0.03 (+2.32%)</td><td>0.03 (+1.85%)</td><td>0.00 (-7.89%)</td><td>216.50 (-1.86%)</td><td>189.22 (-2.00%)</td><td>194.70 (-2.26%)</td><td>154.80 (-0.64%)</td><td>22.52 (-11.09%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>220.60 (n/a)</td><td>193.08 (n/a)</td><td>199.20 (n/a)</td><td>155.80 (n/a)</td><td>25.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 <b>(+21.16%)</b></td><td>0.07 (+12.79%)</td><td>0.07 <b>(+21.87%)</b></td><td>0.05 (-12.99%)</td><td>0.01 <b>(+125.73%)</b></td><td>245.40 (+14.94%)</td><td>179.72 (-9.09%)</td><td>166.70 (-17.96%)</td><td>144.00 (-17.48%)</td><td>38.64 <b>(+121.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>197.70 (n/a)</td><td>203.20 (n/a)</td><td>174.50 (n/a)</td><td>17.43 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (+4.01%)</td><td>0.07 (+8.37%)</td><td>0.07 (+15.03%)</td><td>0.06 (+10.96%)</td><td>0.01 (-5.13%)</td><td>215.20 (-9.88%)</td><td>176.46 (-8.21%)</td><td>164.90 (-13.07%)</td><td>143.30 (-3.89%)</td><td>28.55 (-16.76%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.80 (n/a)</td><td>192.24 (n/a)</td><td>189.70 (n/a)</td><td>149.10 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (-12.58%)</td><td>0.07 (-8.82%)</td><td>0.07 (-1.81%)</td><td>0.05 <b>(-20.33%)</b></td><td>0.01 (-6.80%)</td><td>226.30 <b>(+25.51%)</b></td><td>177.00 (+10.09%)</td><td>167.70 (+1.88%)</td><td>155.30 (+14.44%)</td><td>28.15 <b>(+36.88%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.30 (n/a)</td><td>160.78 (n/a)</td><td>164.60 (n/a)</td><td>135.70 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (+2.03%)</td><td>0.07 (-0.48%)</td><td>0.07 (-1.86%)</td><td>0.05 (-13.98%)</td><td>0.01 (+17.37%)</td><td>262.80 (+16.23%)</td><td>189.30 (+1.95%)</td><td>176.70 (+1.84%)</td><td>141.80 (-1.94%)</td><td>45.26 <b>(+34.78%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.10 (n/a)</td><td>185.68 (n/a)</td><td>173.50 (n/a)</td><td>144.60 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 <b>(+29.32%)</b></td><td>0.07 (-2.60%)</td><td>0.07 (-3.62%)</td><td>0.04 <b>(-24.07%)</b></td><td>0.02 <b>(+191.69%)</b></td><td>273.90 <b>(+31.68%)</b></td><td>192.22 (+9.46%)</td><td>175.00 (+3.80%)</td><td>121.10 <b>(-22.72%)</b></td><td>57.25 <b>(+191.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>175.60 (n/a)</td><td>168.60 (n/a)</td><td>156.70 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (+14.42%)</td><td>0.07 (+4.76%)</td><td>0.07 (+10.52%)</td><td>0.04 <b>(-26.66%)</b></td><td>0.02 <b>(+97.46%)</b></td><td>293.70 <b>(+36.35%)</b></td><td>189.64 (+1.44%)</td><td>173.10 (-9.51%)</td><td>127.60 (-12.60%)</td><td>63.52 <b>(+151.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>186.94 (n/a)</td><td>191.30 (n/a)</td><td>146.00 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (-12.05%)</td><td>0.06 (-9.06%)</td><td>0.06 (-10.10%)</td><td>0.05 (-4.50%)</td><td>0.01 <b>(-36.14%)</b></td><td>230.00 (+4.74%)</td><td>204.94 (+8.83%)</td><td>215.30 (+11.21%)</td><td>178.40 (+13.70%)</td><td>22.75 <b>(-23.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>188.32 (n/a)</td><td>193.60 (n/a)</td><td>156.90 (n/a)</td><td>29.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (-6.38%)</td><td>0.06 (-15.87%)</td><td>0.06 (-16.03%)</td><td>0.05 (-15.31%)</td><td>0.01 (-0.32%)</td><td>272.50 (+18.07%)</td><td>214.80 (+19.64%)</td><td>214.20 (+19.07%)</td><td>156.90 (+6.81%)</td><td>42.62 <b>(+26.02%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>179.54 (n/a)</td><td>179.90 (n/a)</td><td>146.90 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 <b>(-22.99%)</b></td><td>0.16 (-7.40%)</td><td>0.15 (-0.78%)</td><td>0.12 (-14.82%)</td><td>0.03 <b>(-36.28%)</b></td><td>197.20 (+17.38%)</td><td>157.10 (+6.26%)</td><td>163.30 (+0.80%)</td><td>125.00 <b>(+29.80%)</b></td><td>28.93 (-1.94%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>168.00 (n/a)</td><td>147.84 (n/a)</td><td>162.00 (n/a)</td><td>96.30 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 <b>(-23.59%)</b></td><td>0.13 (-17.17%)</td><td>0.13 (-14.57%)</td><td>0.10 <b>(-25.43%)</b></td><td>0.02 <b>(-25.72%)</b></td><td>244.70 <b>(+34.16%)</b></td><td>193.28 <b>(+20.74%)</b></td><td>186.80 (+17.04%)</td><td>163.50 <b>(+30.80%)</b></td><td>30.64 <b>(+35.63%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.40 (n/a)</td><td>160.08 (n/a)</td><td>159.60 (n/a)</td><td>125.00 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (-13.20%)</td><td>0.13 (-15.26%)</td><td>0.14 (-13.00%)</td><td>0.09 <b>(-26.68%)</b></td><td>0.02 <b>(+33.71%)</b></td><td>266.00 <b>(+36.41%)</b></td><td>194.80 <b>(+20.13%)</b></td><td>176.10 (+14.95%)</td><td>171.50 (+15.18%)</td><td>40.42 <b>(+110.93%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.00 (n/a)</td><td>162.16 (n/a)</td><td>153.20 (n/a)</td><td>148.90 (n/a)</td><td>19.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (-6.66%)</td><td>0.15 (-10.31%)</td><td>0.14 (-17.20%)</td><td>0.14 (+11.56%)</td><td>0.02 <b>(-34.80%)</b></td><td>178.20 (-10.36%)</td><td>167.70 (+10.08%)</td><td>173.40 <b>(+20.75%)</b></td><td>139.70 (+7.13%)</td><td>15.91 <b>(-40.53%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>152.34 (n/a)</td><td>143.60 (n/a)</td><td>130.40 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (+6.65%)</td><td>0.16 (+19.44%)</td><td>0.16 <b>(+33.55%)</b></td><td>0.13 <b>(+20.76%)</b></td><td>0.02 (-12.25%)</td><td>190.70 (-17.19%)</td><td>160.34 (-17.15%)</td><td>151.10 <b>(-25.12%)</b></td><td>130.40 (-6.25%)</td><td>24.23 <b>(-28.19%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>230.30 (n/a)</td><td>193.54 (n/a)</td><td>201.80 (n/a)</td><td>139.10 (n/a)</td><td>33.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (-4.47%)</td><td>0.16 (+13.10%)</td><td>0.17 <b>(+26.99%)</b></td><td>0.12 (+1.80%)</td><td>0.02 (-10.94%)</td><td>205.20 (-1.77%)</td><td>157.04 (-11.93%)</td><td>145.30 <b>(-21.29%)</b></td><td>142.50 (+4.63%)</td><td>27.05 (-6.74%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.90 (n/a)</td><td>178.32 (n/a)</td><td>184.60 (n/a)</td><td>136.20 (n/a)</td><td>29.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 <b>(+22.12%)</b></td><td>0.14 (+6.93%)</td><td>0.13 (+5.55%)</td><td>0.11 (+5.90%)</td><td>0.03 <b>(+62.82%)</b></td><td>216.50 (-5.54%)</td><td>182.74 (-5.35%)</td><td>182.20 (-5.25%)</td><td>136.70 (-18.09%)</td><td>29.89 <b>(+23.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>229.20 (n/a)</td><td>193.06 (n/a)</td><td>192.30 (n/a)</td><td>166.90 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (+11.27%)</td><td>0.12 (+6.16%)</td><td>0.12 (+12.36%)</td><td>0.08 (+5.61%)</td><td>0.05 <b>(+30.10%)</b></td><td>316.00 (-5.33%)</td><td>221.90 (-2.43%)</td><td>202.00 (-11.01%)</td><td>130.60 (-10.12%)</td><td>78.97 (+14.67%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>333.80 (n/a)</td><td>227.42 (n/a)</td><td>227.00 (n/a)</td><td>145.30 (n/a)</td><td>68.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.41 (-4.28%)</td><td>0.32 (+10.77%)</td><td>0.28 (+4.12%)</td><td>0.28 <b>(+25.18%)</b></td><td>0.06 <b>(-28.91%)</b></td><td>177.00 <b>(-20.13%)</b></td><td>157.28 (-12.35%)</td><td>174.10 (-3.97%)</td><td>119.70 (+4.45%)</td><td>25.93 <b>(-38.11%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.43 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>221.60 (n/a)</td><td>179.44 (n/a)</td><td>181.30 (n/a)</td><td>114.60 (n/a)</td><td>41.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.37 <b>(+24.94%)</b></td><td>0.33 <b>(+25.27%)</b></td><td>0.32 <b>(+23.45%)</b></td><td>0.29 <b>(+32.70%)</b></td><td>0.04 <b>(+20.06%)</b></td><td>168.10 <b>(-24.65%)</b></td><td>148.76 <b>(-20.30%)</b></td><td>151.40 (-18.95%)</td><td>131.20 (-19.95%)</td><td>16.67 <b>(-28.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>223.10 (n/a)</td><td>186.64 (n/a)</td><td>186.80 (n/a)</td><td>163.90 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (-12.79%)</td><td>0.26 (-5.93%)</td><td>0.28 (+1.55%)</td><td>0.20 (-11.35%)</td><td>0.04 (-5.27%)</td><td>248.60 (+12.79%)</td><td>195.70 (+6.64%)</td><td>177.70 (-1.55%)</td><td>168.50 (+14.70%)</td><td>32.76 <b>(+24.52%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>220.40 (n/a)</td><td>183.52 (n/a)</td><td>180.50 (n/a)</td><td>146.90 (n/a)</td><td>26.31 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.35 <b>(-22.69%)</b></td><td>0.27 (-4.11%)</td><td>0.26 (+1.95%)</td><td>0.21 (+0.71%)</td><td>0.05 <b>(-44.07%)</b></td><td>237.00 (-0.71%)</td><td>188.94 (+0.02%)</td><td>187.80 (-1.93%)</td><td>141.60 <b>(+29.43%)</b></td><td>37.10 <b>(-24.74%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>238.70 (n/a)</td><td>188.90 (n/a)</td><td>191.50 (n/a)</td><td>109.40 (n/a)</td><td>49.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.36 (+13.47%)</td><td>0.29 (+16.88%)</td><td>0.29 (+11.56%)</td><td>0.22 <b>(+65.08%)</b></td><td>0.05 <b>(-26.16%)</b></td><td>225.90 <b>(-39.42%)</b></td><td>175.48 <b>(-20.11%)</b></td><td>168.30 (-10.38%)</td><td>136.70 (-11.86%)</td><td>33.95 <b>(-61.75%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>372.90 (n/a)</td><td>219.66 (n/a)</td><td>187.80 (n/a)</td><td>155.10 (n/a)</td><td>88.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.37 (-4.91%)</td><td>0.27 (-4.38%)</td><td>0.27 (-3.65%)</td><td>0.18 (-11.77%)</td><td>0.07 (+0.07%)</td><td>273.40 (+13.35%)</td><td>191.38 (+5.57%)</td><td>178.90 (+3.77%)</td><td>132.10 (+5.18%)</td><td>51.66 <b>(+22.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>241.20 (n/a)</td><td>181.28 (n/a)</td><td>172.40 (n/a)</td><td>125.60 (n/a)</td><td>42.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 <b>(-24.56%)</b></td><td>0.23 (-14.26%)</td><td>0.23 (-11.20%)</td><td>0.22 (-10.99%)</td><td>0.01 <b>(-70.04%)</b></td><td>227.00 (+12.38%)</td><td>214.66 (+15.67%)</td><td>212.70 (+12.60%)</td><td>204.20 <b>(+32.51%)</b></td><td>8.67 <b>(-54.72%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>202.00 (n/a)</td><td>185.58 (n/a)</td><td>188.90 (n/a)</td><td>154.10 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.30 (-0.93%)</td><td>0.25 (-1.57%)</td><td>0.24 (+2.38%)</td><td>0.21 (-0.93%)</td><td>0.03 <b>(-23.49%)</b></td><td>229.00 (+0.93%)</td><td>199.50 (+0.83%)</td><td>205.40 (-2.33%)</td><td>166.30 (+0.91%)</td><td>23.23 <b>(-21.54%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>226.90 (n/a)</td><td>197.86 (n/a)</td><td>210.30 (n/a)</td><td>164.80 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (-18.69%)</td><td>0.02 (-7.20%)</td><td>0.02 (+2.31%)</td><td>0.01 (+4.50%)</td><td>0.00 <b>(-47.36%)</b></td><td>205.10 (-4.29%)</td><td>164.06 (+4.44%)</td><td>159.90 (-2.26%)</td><td>140.90 <b>(+22.95%)</b></td><td>24.83 <b>(-36.11%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>157.08 (n/a)</td><td>163.60 (n/a)</td><td>114.60 (n/a)</td><td>38.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (+1.35%)</td><td>0.02 (-6.76%)</td><td>0.02 (-8.99%)</td><td>0.01 (+1.18%)</td><td>0.00 (-5.50%)</td><td>228.60 (-1.17%)</td><td>177.48 (+6.68%)</td><td>174.60 (+9.88%)</td><td>135.90 (-1.38%)</td><td>33.82 (-10.00%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.30 (n/a)</td><td>166.36 (n/a)</td><td>158.90 (n/a)</td><td>137.80 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (-17.53%)</td><td>0.01 (-12.10%)</td><td>0.02 (-3.54%)</td><td>0.01 (-12.89%)</td><td>0.00 (-11.68%)</td><td>263.00 (+14.80%)</td><td>188.66 (+14.45%)</td><td>166.50 (+3.67%)</td><td>137.40 <b>(+21.27%)</b></td><td>51.46 <b>(+24.44%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>229.10 (n/a)</td><td>164.84 (n/a)</td><td>160.60 (n/a)</td><td>113.30 (n/a)</td><td>41.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (+14.22%)</td><td>0.02 <b>(+23.52%)</b></td><td>0.02 <b>(+34.40%)</b></td><td>0.01 (+15.72%)</td><td>0.00 <b>(+31.61%)</b></td><td>201.80 (-13.58%)</td><td>159.70 (-18.21%)</td><td>149.00 <b>(-25.61%)</b></td><td>124.90 (-12.41%)</td><td>35.49 (+2.77%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.50 (n/a)</td><td>195.26 (n/a)</td><td>200.30 (n/a)</td><td>142.60 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 <b>(+45.96%)</b></td><td>0.02 (+15.17%)</td><td>0.01 (+7.32%)</td><td>0.01 (-0.65%)</td><td>0.00 <b>(+303.76%)</b></td><td>210.10 (+0.67%)</td><td>178.00 (-9.95%)</td><td>189.70 (-6.78%)</td><td>121.20 <b>(-31.49%)</b></td><td>36.08 <b>(+176.41%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>197.66 (n/a)</td><td>203.50 (n/a)</td><td>176.90 (n/a)</td><td>13.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 <b>(+61.48%)</b></td><td>0.02 <b>(+31.86%)</b></td><td>0.01 <b>(+28.01%)</b></td><td>0.01 <b>(+41.23%)</b></td><td>0.00 <b>(+87.41%)</b></td><td>205.60 <b>(-29.18%)</b></td><td>170.90 <b>(-23.11%)</b></td><td>175.70 <b>(-21.88%)</b></td><td>113.70 <b>(-38.04%)</b></td><td>34.70 <b>(-20.07%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>290.30 (n/a)</td><td>222.26 (n/a)</td><td>224.90 (n/a)</td><td>183.50 (n/a)</td><td>43.41 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (+7.72%)</td><td>0.01 (+8.20%)</td><td>0.02 (+9.56%)</td><td>0.01 (+8.61%)</td><td>0.00 (+6.33%)</td><td>233.10 (-7.94%)</td><td>186.22 (-7.63%)</td><td>174.70 (-8.73%)</td><td>170.50 (-7.19%)</td><td>26.36 (-9.30%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>253.20 (n/a)</td><td>201.60 (n/a)</td><td>191.40 (n/a)</td><td>183.70 (n/a)</td><td>29.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 <b>(+29.08%)</b></td><td>0.01 (+13.67%)</td><td>0.01 (+5.13%)</td><td>0.01 (+11.58%)</td><td>0.00 <b>(+112.64%)</b></td><td>207.20 (-10.38%)</td><td>183.18 (-10.53%)</td><td>194.20 (-4.85%)</td><td>135.70 <b>(-22.55%)</b></td><td>29.78 <b>(+49.22%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.20 (n/a)</td><td>204.74 (n/a)</td><td>204.10 (n/a)</td><td>175.20 (n/a)</td><td>19.96 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-13.08%)</td><td>0.03 <b>(-20.15%)</b></td><td>0.03 <b>(-20.45%)</b></td><td>0.01 <b>(-43.40%)</b></td><td>0.01 <b>(+21.75%)</b></td><td>368.40 <b>(+76.69%)</b></td><td>212.02 <b>(+33.97%)</b></td><td>177.90 <b>(+25.72%)</b></td><td>150.70 (+15.04%)</td><td>88.97 <b>(+166.65%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>158.26 (n/a)</td><td>141.50 (n/a)</td><td>131.00 (n/a)</td><td>33.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (-10.96%)</td><td>0.03 (-4.25%)</td><td>0.03 (-8.18%)</td><td>0.03 (+13.29%)</td><td>0.00 <b>(-34.19%)</b></td><td>191.00 (-11.74%)</td><td>171.66 (+2.63%)</td><td>184.20 (+8.93%)</td><td>141.20 (+12.33%)</td><td>21.90 <b>(-34.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>167.26 (n/a)</td><td>169.10 (n/a)</td><td>125.70 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 <b>(-22.93%)</b></td><td>0.03 (-13.57%)</td><td>0.03 (-9.02%)</td><td>0.02 (-16.51%)</td><td>0.00 <b>(-35.81%)</b></td><td>218.00 (+19.78%)</td><td>185.32 (+14.85%)</td><td>188.30 (+9.92%)</td><td>160.10 <b>(+29.74%)</b></td><td>23.77 (-1.36%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.00 (n/a)</td><td>161.36 (n/a)</td><td>171.30 (n/a)</td><td>123.40 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+0.83%)</td><td>0.03 (+8.09%)</td><td>0.03 (-3.49%)</td><td>0.03 <b>(+34.95%)</b></td><td>0.00 <b>(-46.39%)</b></td><td>196.90 <b>(-25.89%)</b></td><td>180.54 (-9.55%)</td><td>187.70 (+3.59%)</td><td>162.50 (-0.85%)</td><td>15.39 <b>(-61.77%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>265.70 (n/a)</td><td>199.60 (n/a)</td><td>181.20 (n/a)</td><td>163.90 (n/a)</td><td>40.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 <b>(+45.13%)</b></td><td>0.03 (+7.68%)</td><td>0.03 (-9.39%)</td><td>0.02 (+4.92%)</td><td>0.01 <b>(+126.49%)</b></td><td>237.00 (-4.67%)</td><td>185.06 (-2.67%)</td><td>194.00 (+10.35%)</td><td>108.60 <b>(-31.09%)</b></td><td>47.58 <b>(+35.81%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.60 (n/a)</td><td>190.14 (n/a)</td><td>175.80 (n/a)</td><td>157.60 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-3.08%)</td><td>0.03 (-2.86%)</td><td>0.03 (+2.00%)</td><td>0.02 (-6.05%)</td><td>0.00 <b>(+21.70%)</b></td><td>216.80 (+6.48%)</td><td>182.38 (+3.80%)</td><td>169.10 (-1.97%)</td><td>151.10 (+3.21%)</td><td>29.23 <b>(+37.56%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>175.70 (n/a)</td><td>172.50 (n/a)</td><td>146.40 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (-16.94%)</td><td>0.03 (-16.52%)</td><td>0.03 (-14.41%)</td><td>0.02 (-16.09%)</td><td>0.01 <b>(-23.76%)</b></td><td>237.90 (+19.19%)</td><td>190.52 (+19.02%)</td><td>200.70 (+16.82%)</td><td>140.50 <b>(+20.39%)</b></td><td>36.97 (+9.10%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>160.08 (n/a)</td><td>171.80 (n/a)</td><td>116.70 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+2.09%)</td><td>0.03 (-1.09%)</td><td>0.02 (-7.61%)</td><td>0.02 (+8.13%)</td><td>0.00 (-15.39%)</td><td>222.00 (-7.54%)</td><td>211.00 (+0.75%)</td><td>219.70 (+8.23%)</td><td>180.90 (-2.06%)</td><td>17.41 <b>(-24.04%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.10 (n/a)</td><td>209.42 (n/a)</td><td>203.00 (n/a)</td><td>184.70 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (-2.31%)</td><td>0.07 (-9.29%)</td><td>0.06 (-19.23%)</td><td>0.05 (-17.93%)</td><td>0.01 (+13.00%)</td><td>211.90 <b>(+21.85%)</b></td><td>164.80 (+11.43%)</td><td>172.10 <b>(+23.81%)</b></td><td>126.20 (+2.35%)</td><td>32.97 <b>(+35.72%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>173.90 (n/a)</td><td>147.90 (n/a)</td><td>139.00 (n/a)</td><td>123.30 (n/a)</td><td>24.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 <b>(+23.32%)</b></td><td>0.06 (+6.06%)</td><td>0.06 (+11.80%)</td><td>0.04 <b>(-24.24%)</b></td><td>0.02 <b>(+94.57%)</b></td><td>282.10 <b>(+32.01%)</b></td><td>184.98 (+0.42%)</td><td>174.90 (-10.58%)</td><td>113.70 (-18.96%)</td><td>61.75 <b>(+112.92%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>184.20 (n/a)</td><td>195.60 (n/a)</td><td>140.30 (n/a)</td><td>29.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+6.30%)</td><td>0.06 (+2.98%)</td><td>0.06 (+1.73%)</td><td>0.04 (+9.35%)</td><td>0.01 (+7.15%)</td><td>243.20 (-8.54%)</td><td>194.42 (-2.96%)</td><td>185.70 (-1.69%)</td><td>155.60 (-5.98%)</td><td>36.00 (-9.10%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>265.90 (n/a)</td><td>200.36 (n/a)</td><td>188.90 (n/a)</td><td>165.50 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (-6.47%)</td><td>0.06 (-12.11%)</td><td>0.05 (-5.64%)</td><td>0.04 <b>(-23.53%)</b></td><td>0.02 (-0.34%)</td><td>275.60 <b>(+30.74%)</b></td><td>191.22 (+16.20%)</td><td>191.40 (+5.98%)</td><td>115.50 (+6.94%)</td><td>60.83 <b>(+37.74%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>210.80 (n/a)</td><td>164.56 (n/a)</td><td>180.60 (n/a)</td><td>108.00 (n/a)</td><td>44.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 <b>(-34.99%)</b></td><td>0.06 (-18.80%)</td><td>0.06 (-7.92%)</td><td>0.05 (-19.68%)</td><td>0.01 <b>(-55.65%)</b></td><td>228.10 <b>(+24.51%)</b></td><td>183.86 <b>(+20.77%)</b></td><td>175.20 (+8.62%)</td><td>166.40 <b>(+53.79%)</b></td><td>25.31 (-10.86%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>183.20 (n/a)</td><td>152.24 (n/a)</td><td>161.30 (n/a)</td><td>108.20 (n/a)</td><td>28.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (+15.59%)</td><td>0.06 (+5.79%)</td><td>0.06 (-0.37%)</td><td>0.05 (-2.14%)</td><td>0.01 <b>(+78.41%)</b></td><td>198.30 (+2.16%)</td><td>171.44 (-4.14%)</td><td>180.50 (+0.39%)</td><td>131.10 (-13.47%)</td><td>26.76 <b>(+56.60%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>178.84 (n/a)</td><td>179.80 (n/a)</td><td>151.50 (n/a)</td><td>17.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (-19.33%)</td><td>0.05 (-15.58%)</td><td>0.04 <b>(-20.17%)</b></td><td>0.04 (-8.66%)</td><td>0.00 <b>(-53.85%)</b></td><td>247.30 (+9.47%)</td><td>230.08 (+17.72%)</td><td>234.00 <b>(+25.27%)</b></td><td>216.10 <b>(+23.91%)</b></td><td>12.70 <b>(-38.19%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>195.44 (n/a)</td><td>186.80 (n/a)</td><td>174.40 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (-5.91%)</td><td>0.05 (-4.31%)</td><td>0.05 (-3.46%)</td><td>0.04 (-7.63%)</td><td>0.00 (-16.38%)</td><td>259.50 (+8.26%)</td><td>221.96 (+4.34%)</td><td>214.50 (+3.62%)</td><td>201.90 (+6.32%)</td><td>22.05 (-2.04%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>212.72 (n/a)</td><td>207.00 (n/a)</td><td>189.90 (n/a)</td><td>22.51 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 <b>(+51.08%)</b></td><td>0.14 (+16.06%)</td><td>0.14 (+16.57%)</td><td>0.10 (-1.79%)</td><td>0.04 <b>(+262.78%)</b></td><td>208.50 (+1.81%)</td><td>160.50 (-9.35%)</td><td>148.60 (-14.20%)</td><td>105.50 <b>(-33.81%)</b></td><td>41.08 <b>(+142.75%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>177.06 (n/a)</td><td>173.20 (n/a)</td><td>159.40 (n/a)</td><td>16.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (+19.25%)</td><td>0.12 (+5.93%)</td><td>0.12 (-3.92%)</td><td>0.10 <b>(+28.97%)</b></td><td>0.02 (-0.25%)</td><td>214.20 <b>(-22.48%)</b></td><td>175.54 (-7.17%)</td><td>173.90 (+4.13%)</td><td>130.80 (-16.15%)</td><td>30.38 <b>(-38.81%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>276.30 (n/a)</td><td>189.10 (n/a)</td><td>167.00 (n/a)</td><td>156.00 (n/a)</td><td>49.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 <b>(-22.28%)</b></td><td>0.10 <b>(-20.01%)</b></td><td>0.10 <b>(-20.08%)</b></td><td>0.07 <b>(-27.23%)</b></td><td>0.02 (-18.80%)</td><td>302.70 <b>(+37.47%)</b></td><td>218.42 <b>(+25.66%)</b></td><td>201.80 <b>(+25.11%)</b></td><td>183.50 <b>(+28.68%)</b></td><td>49.34 <b>(+45.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>220.20 (n/a)</td><td>173.82 (n/a)</td><td>161.30 (n/a)</td><td>142.60 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 <b>(-27.95%)</b></td><td>0.11 (-8.80%)</td><td>0.12 (-4.55%)</td><td>0.11 <b>(+40.55%)</b></td><td>0.01 <b>(-81.43%)</b></td><td>199.40 <b>(-28.86%)</b></td><td>184.84 (+2.19%)</td><td>180.30 (+4.83%)</td><td>175.10 <b>(+38.75%)</b></td><td>10.60 <b>(-82.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>280.30 (n/a)</td><td>180.88 (n/a)</td><td>172.00 (n/a)</td><td>126.20 (n/a)</td><td>59.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (+6.52%)</td><td>0.13 (+1.90%)</td><td>0.12 (-4.96%)</td><td>0.11 (+17.98%)</td><td>0.02 (-18.60%)</td><td>195.80 (-15.24%)</td><td>165.74 (-3.29%)</td><td>170.20 (+5.26%)</td><td>133.40 (-6.19%)</td><td>22.89 <b>(-36.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>231.00 (n/a)</td><td>171.38 (n/a)</td><td>161.70 (n/a)</td><td>142.20 (n/a)</td><td>35.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (+18.30%)</td><td>0.11 (-0.88%)</td><td>0.11 (-3.25%)</td><td>0.09 (-11.82%)</td><td>0.02 <b>(+149.07%)</b></td><td>231.80 (+13.41%)</td><td>191.84 (+2.90%)</td><td>193.40 (+3.37%)</td><td>144.80 (-15.47%)</td><td>31.68 <b>(+134.33%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>186.44 (n/a)</td><td>187.10 (n/a)</td><td>171.30 (n/a)</td><td>13.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (-0.51%)</td><td>0.11 (-4.48%)</td><td>0.12 (-0.93%)</td><td>0.07 (-18.41%)</td><td>0.03 <b>(+28.93%)</b></td><td>290.30 <b>(+22.59%)</b></td><td>196.62 (+8.45%)</td><td>178.60 (+0.96%)</td><td>133.60 (+0.53%)</td><td>60.26 <b>(+62.72%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>236.80 (n/a)</td><td>181.30 (n/a)</td><td>176.90 (n/a)</td><td>132.90 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (-9.83%)</td><td>0.09 (-5.91%)</td><td>0.10 (-2.53%)</td><td>0.09 (-2.99%)</td><td>0.01 <b>(-34.35%)</b></td><td>237.80 (+3.08%)</td><td>221.78 (+5.98%)</td><td>214.00 (+2.59%)</td><td>209.70 (+10.89%)</td><td>13.14 <b>(-24.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>209.26 (n/a)</td><td>208.60 (n/a)</td><td>189.10 (n/a)</td><td>17.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>155.22 (n/a)</td><td>145.80 (n/a)</td><td>122.50 (n/a)</td><td>36.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>150.68 (n/a)</td><td>144.10 (n/a)</td><td>122.20 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.00 (n/a)</td><td>172.62 (n/a)</td><td>171.00 (n/a)</td><td>127.20 (n/a)</td><td>49.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>186.70 (n/a)</td><td>188.80 (n/a)</td><td>145.90 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>169.40 (n/a)</td><td>182.80 (n/a)</td><td>126.80 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.20 (n/a)</td><td>160.06 (n/a)</td><td>162.60 (n/a)</td><td>125.40 (n/a)</td><td>20.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.50 (n/a)</td><td>155.02 (n/a)</td><td>160.90 (n/a)</td><td>125.50 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>305.40 (n/a)</td><td>201.82 (n/a)</td><td>191.70 (n/a)</td><td>135.60 (n/a)</td><td>64.96 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.20 (n/a)</td><td>169.72 (n/a)</td><td>176.40 (n/a)</td><td>120.70 (n/a)</td><td>28.62 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>227.60 (n/a)</td><td>184.72 (n/a)</td><td>182.10 (n/a)</td><td>156.20 (n/a)</td><td>26.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.20 (n/a)</td><td>157.76 (n/a)</td><td>161.50 (n/a)</td><td>124.50 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>323.00 (n/a)</td><td>205.62 (n/a)</td><td>208.00 (n/a)</td><td>109.80 (n/a)</td><td>76.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.46 <b>(+28.17%)</b></td><td>0.34 <b>(+22.41%)</b></td><td>0.34 <b>(+21.54%)</b></td><td>0.25 (+7.46%)</td><td>0.08 <b>(+62.95%)</b></td><td>198.20 (-6.95%)</td><td>149.12 (-16.65%)</td><td>145.20 (-17.73%)</td><td>106.90 <b>(-21.97%)</b></td><td>34.37 (+19.60%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>213.00 (n/a)</td><td>178.90 (n/a)</td><td>176.50 (n/a)</td><td>137.00 (n/a)</td><td>28.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>206.70 (n/a)</td><td>169.54 (n/a)</td><td>187.20 (n/a)</td><td>125.00 (n/a)</td><td>38.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>196.20 (n/a)</td><td>168.62 (n/a)</td><td>171.70 (n/a)</td><td>131.00 (n/a)</td><td>23.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>201.40 (n/a)</td><td>170.88 (n/a)</td><td>171.40 (n/a)</td><td>117.50 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>138.12 (n/a)</td><td>125.00 (n/a)</td><td>116.00 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>132.40 (n/a)</td><td>125.88 (n/a)</td><td>128.40 (n/a)</td><td>119.50 (n/a)</td><td>5.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>165.40 (n/a)</td><td>142.74 (n/a)</td><td>142.10 (n/a)</td><td>119.20 (n/a)</td><td>17.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>164.44 (n/a)</td><td>161.50 (n/a)</td><td>108.30 (n/a)</td><td>45.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>173.30 (n/a)</td><td>148.46 (n/a)</td><td>154.00 (n/a)</td><td>119.60 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>228.30 (n/a)</td><td>159.24 (n/a)</td><td>135.10 (n/a)</td><td>111.10 (n/a)</td><td>51.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>171.14 (n/a)</td><td>172.20 (n/a)</td><td>149.60 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>179.24 (n/a)</td><td>194.60 (n/a)</td><td>135.70 (n/a)</td><td>30.94 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>168.40 (n/a)</td><td>150.68 (n/a)</td><td>166.90 (n/a)</td><td>117.40 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>183.40 (n/a)</td><td>166.52 (n/a)</td><td>176.70 (n/a)</td><td>135.30 (n/a)</td><td>19.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>255.30 (n/a)</td><td>186.22 (n/a)</td><td>191.60 (n/a)</td><td>130.30 (n/a)</td><td>54.01 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>199.50 (n/a)</td><td>161.66 (n/a)</td><td>166.60 (n/a)</td><td>109.60 (n/a)</td><td>32.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>168.00 (n/a)</td><td>137.98 (n/a)</td><td>135.10 (n/a)</td><td>120.60 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>185.50 (n/a)</td><td>155.32 (n/a)</td><td>154.90 (n/a)</td><td>123.40 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>184.10 (n/a)</td><td>156.24 (n/a)</td><td>163.10 (n/a)</td><td>118.20 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>366.50 (n/a)</td><td>191.66 (n/a)</td><td>148.90 (n/a)</td><td>134.60 (n/a)</td><td>98.14 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>155.62 (n/a)</td><td>165.20 (n/a)</td><td>101.60 (n/a)</td><td>40.36 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>265.50 (n/a)</td><td>198.44 (n/a)</td><td>194.40 (n/a)</td><td>161.40 (n/a)</td><td>42.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.30 (n/a)</td><td>183.64 (n/a)</td><td>184.10 (n/a)</td><td>133.70 (n/a)</td><td>34.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.80 (n/a)</td><td>174.14 (n/a)</td><td>173.40 (n/a)</td><td>144.30 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>169.08 (n/a)</td><td>170.00 (n/a)</td><td>135.10 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>317.70 (n/a)</td><td>193.82 (n/a)</td><td>166.50 (n/a)</td><td>124.10 (n/a)</td><td>74.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.40 (n/a)</td><td>216.06 (n/a)</td><td>216.80 (n/a)</td><td>188.60 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.20 (n/a)</td><td>156.20 (n/a)</td><td>155.30 (n/a)</td><td>140.70 (n/a)</td><td>12.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>176.70 (n/a)</td><td>165.14 (n/a)</td><td>164.00 (n/a)</td><td>148.40 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.30 (n/a)</td><td>177.46 (n/a)</td><td>177.70 (n/a)</td><td>137.90 (n/a)</td><td>36.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>188.04 (n/a)</td><td>192.50 (n/a)</td><td>132.80 (n/a)</td><td>41.62 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>162.76 (n/a)</td><td>169.00 (n/a)</td><td>110.80 (n/a)</td><td>30.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>254.80 (n/a)</td><td>184.30 (n/a)</td><td>201.80 (n/a)</td><td>107.90 (n/a)</td><td>59.47 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.20 (n/a)</td><td>199.24 (n/a)</td><td>210.70 (n/a)</td><td>133.30 (n/a)</td><td>54.86 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>286.20 (n/a)</td><td>234.08 (n/a)</td><td>219.30 (n/a)</td><td>210.20 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.90 (n/a)</td><td>154.50 (n/a)</td><td>163.10 (n/a)</td><td>115.80 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.20 (n/a)</td><td>166.02 (n/a)</td><td>155.50 (n/a)</td><td>140.50 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>215.40 (n/a)</td><td>153.12 (n/a)</td><td>150.30 (n/a)</td><td>115.70 (n/a)</td><td>39.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>181.90 (n/a)</td><td>163.02 (n/a)</td><td>166.00 (n/a)</td><td>141.40 (n/a)</td><td>17.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>179.70 (n/a)</td><td>149.94 (n/a)</td><td>158.40 (n/a)</td><td>115.70 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>192.44 (n/a)</td><td>186.20 (n/a)</td><td>160.90 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.30 (n/a)</td><td>156.86 (n/a)</td><td>153.90 (n/a)</td><td>129.30 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.20 (n/a)</td><td>204.02 (n/a)</td><td>207.40 (n/a)</td><td>175.50 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.80 (n/a)</td><td>166.52 (n/a)</td><td>167.00 (n/a)</td><td>135.00 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.50 (n/a)</td><td>160.38 (n/a)</td><td>162.90 (n/a)</td><td>123.30 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.50 (n/a)</td><td>161.22 (n/a)</td><td>146.60 (n/a)</td><td>133.00 (n/a)</td><td>32.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>179.80 (n/a)</td><td>149.66 (n/a)</td><td>147.90 (n/a)</td><td>128.30 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.20 (n/a)</td><td>149.84 (n/a)</td><td>147.10 (n/a)</td><td>112.80 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>190.40 (n/a)</td><td>161.72 (n/a)</td><td>179.90 (n/a)</td><td>115.50 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.30 (n/a)</td><td>152.22 (n/a)</td><td>153.00 (n/a)</td><td>116.00 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>186.94 (n/a)</td><td>179.90 (n/a)</td><td>172.80 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.28 (+2.36%)</td><td>3.87 (-6.18%)</td><td>4.12 (-0.46%)</td><td>3.21 (-19.65%)</td><td>0.49 <b>(+571.91%)</b></td><td>2929.70 <b>(+24.45%)</b></td><td>2465.66 (+8.03%)</td><td>2282.50 (+0.47%)</td><td>2196.60 (-2.30%)</td><td>332.10 <b>(+704.54%)</b></td><td>1684.12 (+2.36%)</td><td>1521.12 (-6.18%)</td><td>1620.78 (-0.46%)</td><td>1262.70 (-19.65%)</td><td>192.99 <b>(+571.90%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.18 (n/a)</td><td>4.12 (n/a)</td><td>4.14 (n/a)</td><td>3.99 (n/a)</td><td>0.07 (n/a)</td><td>2354.10 (n/a)</td><td>2282.32 (n/a)</td><td>2271.90 (n/a)</td><td>2248.40 (n/a)</td><td>41.28 (n/a)</td><td>1645.33 (n/a)</td><td>1621.31 (n/a)</td><td>1628.33 (n/a)</td><td>1571.47 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.22 (+10.81%)</td><td>1.01 (+4.77%)</td><td>0.97 (-6.65%)</td><td>0.92 <b>(+22.71%)</b></td><td>0.12 (-12.77%)</td><td>240.00 (-18.51%)</td><td>220.62 (-5.34%)</td><td>229.00 (+7.11%)</td><td>182.00 (-9.77%)</td><td>23.38 <b>(-37.36%)</b></td><td>51.86 (+10.81%)</td><td>43.21 (+4.77%)</td><td>41.21 (-6.65%)</td><td>39.33 <b>(+22.71%)</b></td><td>5.10 (-12.77%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.10 (n/a)</td><td>0.97 (n/a)</td><td>1.03 (n/a)</td><td>0.75 (n/a)</td><td>0.14 (n/a)</td><td>294.50 (n/a)</td><td>233.06 (n/a)</td><td>213.80 (n/a)</td><td>201.70 (n/a)</td><td>37.32 (n/a)</td><td>46.80 (n/a)</td><td>41.24 (n/a)</td><td>44.14 (n/a)</td><td>32.05 (n/a)</td><td>5.85 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.22 (+2.27%)</td><td>1.03 (+2.50%)</td><td>1.02 (-2.85%)</td><td>0.70 (+3.65%)</td><td>0.21 (+9.38%)</td><td>313.80 (-3.51%)</td><td>224.24 (-2.20%)</td><td>217.50 (+2.93%)</td><td>181.80 (-2.21%)</td><td>53.63 (-2.11%)</td><td>51.91 (+2.27%)</td><td>43.76 (+2.50%)</td><td>43.39 (-2.85%)</td><td>30.07 (+3.65%)</td><td>8.86 (+9.38%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.19 (n/a)</td><td>1.00 (n/a)</td><td>1.05 (n/a)</td><td>0.68 (n/a)</td><td>0.19 (n/a)</td><td>325.20 (n/a)</td><td>229.28 (n/a)</td><td>211.30 (n/a)</td><td>185.90 (n/a)</td><td>54.78 (n/a)</td><td>50.76 (n/a)</td><td>42.69 (n/a)</td><td>44.66 (n/a)</td><td>29.02 (n/a)</td><td>8.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.52 (+0.08%)</td><td>0.52 (+0.08%)</td><td>0.52 (+0.05%)</td><td>0.52 (+0.20%)</td><td>0.00 <b>(-37.34%)</b></td><td>48523.30 (-0.19%)</td><td>48476.00 (-0.08%)</td><td>48482.90 (-0.05%)</td><td>48420.00 (-0.08%)</td><td>40.63 <b>(-37.51%)</b></td><td>354.81 (+0.08%)</td><td>354.40 (+0.08%)</td><td>354.35 (+0.05%)</td><td>354.05 (+0.20%)</td><td>0.30 <b>(-37.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48618.00 (n/a)</td><td>48513.76 (n/a)</td><td>48504.80 (n/a)</td><td>48456.60 (n/a)</td><td>65.02 (n/a)</td><td>354.54 (n/a)</td><td>354.12 (n/a)</td><td>354.19 (n/a)</td><td>353.36 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (+0.80%)</td><td>0.21 (-0.01%)</td><td>0.21 (-0.36%)</td><td>0.21 (+0.76%)</td><td>0.00 (-1.01%)</td><td>119906.10 (-0.75%)</td><td>118441.72 (+0.01%)</td><td>118344.50 (+0.36%)</td><td>116406.10 (-0.79%)</td><td>1341.88 (-2.79%)</td><td>147.59 (+0.80%)</td><td>145.06 (-0.01%)</td><td>145.17 (-0.36%)</td><td>143.28 (+0.76%)</td><td>1.65 (-1.01%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120815.90 (n/a)</td><td>118435.64 (n/a)</td><td>117914.70 (n/a)</td><td>117332.40 (n/a)</td><td>1380.43 (n/a)</td><td>146.42 (n/a)</td><td>145.07 (n/a)</td><td>145.70 (n/a)</td><td>142.20 (n/a)</td><td>1.67 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.90 (-0.28%)</td><td>0.89 (+0.45%)</td><td>0.89 (+0.67%)</td><td>0.88 (+0.51%)</td><td>0.00 <b>(-44.38%)</b></td><td>28442.60 (-0.50%)</td><td>28251.40 (-0.45%)</td><td>28249.10 (-0.67%)</td><td>28101.50 (+0.28%)</td><td>129.51 <b>(-44.51%)</b></td><td>611.35 (-0.28%)</td><td>608.12 (+0.45%)</td><td>608.16 (+0.67%)</td><td>604.02 (+0.51%)</td><td>2.78 <b>(-44.38%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28586.80 (n/a)</td><td>28380.12 (n/a)</td><td>28439.20 (n/a)</td><td>28023.60 (n/a)</td><td>233.38 (n/a)</td><td>613.05 (n/a)</td><td>605.38 (n/a)</td><td>604.09 (n/a)</td><td>600.97 (n/a)</td><td>5.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.56 (+0.73%)</td><td>3.44 (-0.26%)</td><td>3.49 (+0.67%)</td><td>3.26 (-2.95%)</td><td>0.12 <b>(+53.27%)</b></td><td>7719.70 (+3.03%)</td><td>7325.92 (+0.32%)</td><td>7213.70 (-0.67%)</td><td>7076.40 (-0.73%)</td><td>267.87 <b>(+56.50%)</b></td><td>2427.78 (+0.73%)</td><td>2347.54 (-0.26%)</td><td>2381.57 (+0.67%)</td><td>2225.45 (-2.95%)</td><td>84.25 <b>(+53.27%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.53 (n/a)</td><td>3.45 (n/a)</td><td>3.47 (n/a)</td><td>3.36 (n/a)</td><td>0.08 (n/a)</td><td>7492.40 (n/a)</td><td>7302.26 (n/a)</td><td>7262.00 (n/a)</td><td>7128.30 (n/a)</td><td>171.16 (n/a)</td><td>2410.11 (n/a)</td><td>2353.71 (n/a)</td><td>2365.71 (n/a)</td><td>2292.99 (n/a)</td><td>54.96 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.11 (+2.53%)</td><td>2.95 (+3.38%)</td><td>2.94 (+4.25%)</td><td>2.78 (+1.32%)</td><td>0.13 (+14.64%)</td><td>9054.00 (-1.30%)</td><td>8548.60 (-3.24%)</td><td>8560.50 (-4.08%)</td><td>8098.90 (-2.47%)</td><td>382.00 (+10.41%)</td><td>2121.25 (+2.53%)</td><td>2012.87 (+3.38%)</td><td>2006.88 (+4.25%)</td><td>1897.49 (+1.32%)</td><td>89.63 (+14.64%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.03 (n/a)</td><td>2.85 (n/a)</td><td>2.82 (n/a)</td><td>2.74 (n/a)</td><td>0.11 (n/a)</td><td>9173.10 (n/a)</td><td>8834.64 (n/a)</td><td>8924.40 (n/a)</td><td>8303.60 (n/a)</td><td>345.99 (n/a)</td><td>2068.96 (n/a)</td><td>1947.05 (n/a)</td><td>1925.04 (n/a)</td><td>1872.86 (n/a)</td><td>78.18 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.35 (+1.33%)</td><td>3.21 (+0.67%)</td><td>3.18 (+0.09%)</td><td>3.15 (+1.59%)</td><td>0.08 (+9.90%)</td><td>7984.00 (-1.57%)</td><td>7851.14 (-0.66%)</td><td>7924.20 (-0.09%)</td><td>7502.40 (-1.31%)</td><td>197.53 (+6.86%)</td><td>2289.92 (+1.33%)</td><td>2189.35 (+0.67%)</td><td>2168.02 (+0.09%)</td><td>2151.79 (+1.59%)</td><td>56.89 (+9.89%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.31 (n/a)</td><td>3.19 (n/a)</td><td>3.17 (n/a)</td><td>3.10 (n/a)</td><td>0.08 (n/a)</td><td>8111.20 (n/a)</td><td>7903.00 (n/a)</td><td>7931.40 (n/a)</td><td>7602.30 (n/a)</td><td>184.85 (n/a)</td><td>2259.81 (n/a)</td><td>2174.81 (n/a)</td><td>2166.06 (n/a)</td><td>2118.03 (n/a)</td><td>51.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 (-0.34%)</td><td>0.79 (-0.11%)</td><td>0.79 (-0.01%)</td><td>0.78 (-0.17%)</td><td>0.00 <b>(-41.52%)</b></td><td>96317.30 (+0.17%)</td><td>96158.30 (+0.11%)</td><td>96116.70 (+0.01%)</td><td>96110.20 (+0.34%)</td><td>89.57 <b>(-41.20%)</b></td><td>715.01 (-0.34%)</td><td>714.65 (-0.11%)</td><td>714.96 (-0.01%)</td><td>713.47 (-0.17%)</td><td>0.66 <b>(-41.52%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96154.70 (n/a)</td><td>96050.10 (n/a)</td><td>96109.20 (n/a)</td><td>95780.50 (n/a)</td><td>152.32 (n/a)</td><td>717.47 (n/a)</td><td>715.46 (n/a)</td><td>715.01 (n/a)</td><td>714.68 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.73 (+0.37%)</td><td>0.73 (+0.06%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.06%)</td><td>0.00 <b>(+425.58%)</b></td><td>103447.70 (+0.06%)</td><td>103255.56 (-0.06%)</td><td>103304.70 (-0.00%)</td><td>102902.30 (-0.37%)</td><td>206.49 <b>(+423.69%)</b></td><td>667.81 (+0.37%)</td><td>665.53 (+0.06%)</td><td>665.21 (+0.00%)</td><td>664.29 (-0.06%)</td><td>1.33 <b>(+425.59%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103383.90 (n/a)</td><td>103315.48 (n/a)</td><td>103306.30 (n/a)</td><td>103287.60 (n/a)</td><td>39.43 (n/a)</td><td>665.32 (n/a)</td><td>665.14 (n/a)</td><td>665.20 (n/a)</td><td>664.70 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.70 (-0.22%)</td><td>0.69 (-0.26%)</td><td>0.69 (-0.20%)</td><td>0.69 (-0.37%)</td><td>0.00 (+18.33%)</td><td>109277.20 (+0.37%)</td><td>108868.22 (+0.26%)</td><td>108848.50 (+0.20%)</td><td>108508.90 (+0.22%)</td><td>273.12 (+19.07%)</td><td>633.31 (-0.22%)</td><td>631.22 (-0.26%)</td><td>631.33 (-0.20%)</td><td>628.85 (-0.37%)</td><td>1.58 (+18.32%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108873.00 (n/a)</td><td>108581.66 (n/a)</td><td>108633.10 (n/a)</td><td>108265.80 (n/a)</td><td>229.38 (n/a)</td><td>634.73 (n/a)</td><td>632.89 (n/a)</td><td>632.58 (n/a)</td><td>631.19 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.65 (-1.09%)</td><td>6.85 (-5.37%)</td><td>6.80 (-5.14%)</td><td>6.42 (-4.03%)</td><td>0.48 (+15.00%)</td><td>1387.30 (+4.20%)</td><td>1306.70 (+5.78%)</td><td>1311.60 (+5.42%)</td><td>1164.70 (+1.09%)</td><td>86.11 <b>(+20.37%)</b></td><td>460.94 (-1.09%)</td><td>412.38 (-5.37%)</td><td>409.31 (-5.14%)</td><td>386.99 (-4.03%)</td><td>28.90 (+15.00%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.74 (n/a)</td><td>7.23 (n/a)</td><td>7.16 (n/a)</td><td>6.69 (n/a)</td><td>0.42 (n/a)</td><td>1331.40 (n/a)</td><td>1235.30 (n/a)</td><td>1244.20 (n/a)</td><td>1152.10 (n/a)</td><td>71.54 (n/a)</td><td>466.00 (n/a)</td><td>435.77 (n/a)</td><td>431.51 (n/a)</td><td>403.25 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.07 (+0.01%)</td><td>6.84 (+7.14%)</td><td>6.88 (+3.77%)</td><td>6.59 <b>(+41.51%)</b></td><td>0.18 <b>(-81.68%)</b></td><td>1352.50 <b>(-29.33%)</b></td><td>1303.38 (-8.85%)</td><td>1294.60 (-3.63%)</td><td>1261.20 (+0.00%)</td><td>34.99 <b>(-87.26%)</b></td><td>425.70 (+0.01%)</td><td>412.15 (+7.14%)</td><td>414.71 (+3.77%)</td><td>396.95 <b>(+41.51%)</b></td><td>11.00 <b>(-81.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.07 (n/a)</td><td>6.39 (n/a)</td><td>6.63 (n/a)</td><td>4.66 (n/a)</td><td>1.00 (n/a)</td><td>1913.90 (n/a)</td><td>1429.86 (n/a)</td><td>1343.30 (n/a)</td><td>1261.20 (n/a)</td><td>274.64 (n/a)</td><td>425.67 (n/a)</td><td>384.67 (n/a)</td><td>399.65 (n/a)</td><td>280.51 (n/a)</td><td>60.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.10 (+0.35%)</td><td>6.22 (-4.14%)</td><td>6.58 (+0.13%)</td><td>4.34 <b>(-28.34%)</b></td><td>1.08 <b>(+155.07%)</b></td><td>2051.90 <b>(+39.54%)</b></td><td>1477.86 (+7.23%)</td><td>1354.50 (-0.13%)</td><td>1255.10 (-0.35%)</td><td>324.88 <b>(+264.95%)</b></td><td>427.75 (+0.35%)</td><td>374.68 (-4.14%)</td><td>396.35 (+0.13%)</td><td>261.64 <b>(-28.34%)</b></td><td>65.10 <b>(+155.07%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.08 (n/a)</td><td>6.49 (n/a)</td><td>6.57 (n/a)</td><td>6.06 (n/a)</td><td>0.42 (n/a)</td><td>1470.50 (n/a)</td><td>1378.16 (n/a)</td><td>1356.30 (n/a)</td><td>1259.50 (n/a)</td><td>89.02 (n/a)</td><td>426.26 (n/a)</td><td>390.87 (n/a)</td><td>395.83 (n/a)</td><td>365.09 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.01 (-5.48%)</td><td>7.84 (-2.57%)</td><td>7.91 (-0.62%)</td><td>7.40 (-5.03%)</td><td>0.25 (-7.70%)</td><td>4712.60 (+5.29%)</td><td>4453.06 (+2.63%)</td><td>4406.60 (+0.62%)</td><td>4350.30 (+5.80%)</td><td>146.92 (+3.84%)</td><td>493.64 (-5.48%)</td><td>482.65 (-2.57%)</td><td>487.34 (-0.62%)</td><td>455.69 (-5.03%)</td><td>15.30 (-7.70%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.48 (n/a)</td><td>8.04 (n/a)</td><td>7.96 (n/a)</td><td>7.79 (n/a)</td><td>0.27 (n/a)</td><td>4475.80 (n/a)</td><td>4338.92 (n/a)</td><td>4379.40 (n/a)</td><td>4111.90 (n/a)</td><td>141.49 (n/a)</td><td>522.26 (n/a)</td><td>495.37 (n/a)</td><td>490.36 (n/a)</td><td>479.80 (n/a)</td><td>16.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.90 (+4.27%)</td><td>7.41 (+0.89%)</td><td>7.57 (+1.23%)</td><td>6.92 (-1.59%)</td><td>0.42 <b>(+74.46%)</b></td><td>5041.80 (+1.62%)</td><td>4717.72 (-0.72%)</td><td>4605.70 (-1.21%)</td><td>4415.20 (-4.09%)</td><td>269.14 <b>(+71.15%)</b></td><td>486.39 (+4.27%)</td><td>456.37 (+0.89%)</td><td>466.26 (+1.23%)</td><td>425.93 (-1.59%)</td><td>25.78 <b>(+74.46%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.57 (n/a)</td><td>7.34 (n/a)</td><td>7.48 (n/a)</td><td>7.03 (n/a)</td><td>0.24 (n/a)</td><td>4961.50 (n/a)</td><td>4751.72 (n/a)</td><td>4662.30 (n/a)</td><td>4603.70 (n/a)</td><td>157.25 (n/a)</td><td>466.47 (n/a)</td><td>452.33 (n/a)</td><td>460.61 (n/a)</td><td>432.83 (n/a)</td><td>14.78 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.37 (-0.82%)</td><td>7.17 (+1.53%)</td><td>7.18 (+1.73%)</td><td>6.89 (+2.74%)</td><td>0.20 <b>(-33.23%)</b></td><td>5063.90 (-2.67%)</td><td>4865.36 (-1.59%)</td><td>4853.60 (-1.70%)</td><td>4733.30 (+0.82%)</td><td>135.93 <b>(-34.61%)</b></td><td>453.69 (-0.82%)</td><td>441.65 (+1.53%)</td><td>442.45 (+1.73%)</td><td>424.08 (+2.74%)</td><td>12.20 <b>(-33.23%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.43 (n/a)</td><td>7.06 (n/a)</td><td>7.06 (n/a)</td><td>6.70 (n/a)</td><td>0.30 (n/a)</td><td>5202.70 (n/a)</td><td>4943.88 (n/a)</td><td>4937.60 (n/a)</td><td>4694.60 (n/a)</td><td>207.87 (n/a)</td><td>457.44 (n/a)</td><td>434.99 (n/a)</td><td>434.93 (n/a)</td><td>412.76 (n/a)</td><td>18.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 (+0.02%)</td><td>0.79 (-0.00%)</td><td>0.79 (+0.00%)</td><td>0.79 (+0.00%)</td><td>0.00 <b>(+25.50%)</b></td><td>95431.20 (-0.00%)</td><td>95399.64 (+0.00%)</td><td>95403.00 (-0.00%)</td><td>95347.80 (-0.02%)</td><td>33.36 <b>(+25.24%)</b></td><td>720.72 (+0.02%)</td><td>720.33 (-0.00%)</td><td>720.31 (+0.00%)</td><td>720.09 (+0.00%)</td><td>0.25 <b>(+25.49%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95434.80 (n/a)</td><td>95398.28 (n/a)</td><td>95404.80 (n/a)</td><td>95370.80 (n/a)</td><td>26.63 (n/a)</td><td>720.55 (n/a)</td><td>720.34 (n/a)</td><td>720.29 (n/a)</td><td>720.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.74 (-0.01%)</td><td>0.74 (-0.03%)</td><td>0.74 (-0.04%)</td><td>0.74 (-0.06%)</td><td>0.00 <b>(+59.91%)</b></td><td>102681.10 (+0.06%)</td><td>102611.28 (+0.03%)</td><td>102617.20 (+0.04%)</td><td>102547.70 (+0.01%)</td><td>49.90 <b>(+59.95%)</b></td><td>670.12 (-0.01%)</td><td>669.71 (-0.03%)</td><td>669.67 (-0.04%)</td><td>669.25 (-0.06%)</td><td>0.33 <b>(+59.91%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102622.90 (n/a)</td><td>102578.24 (n/a)</td><td>102579.50 (n/a)</td><td>102536.80 (n/a)</td><td>31.20 (n/a)</td><td>670.19 (n/a)</td><td>669.92 (n/a)</td><td>669.91 (n/a)</td><td>669.63 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.71 (+0.03%)</td><td>0.70 (+0.02%)</td><td>0.70 (+0.09%)</td><td>0.70 (+0.04%)</td><td>0.00 (-17.17%)</td><td>107619.30 (-0.04%)</td><td>107370.40 (-0.02%)</td><td>107426.70 (-0.09%)</td><td>107053.80 (-0.03%)</td><td>206.61 (-17.23%)</td><td>641.92 (+0.03%)</td><td>640.02 (+0.02%)</td><td>639.69 (+0.09%)</td><td>638.54 (+0.04%)</td><td>1.23 (-17.17%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.71 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107662.50 (n/a)</td><td>107394.78 (n/a)</td><td>107519.30 (n/a)</td><td>107087.50 (n/a)</td><td>249.61 (n/a)</td><td>641.71 (n/a)</td><td>639.88 (n/a)</td><td>639.14 (n/a)</td><td>638.29 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.27 (+4.44%)</td><td>3.45 (-3.37%)</td><td>3.15 (-13.68%)</td><td>3.02 (-2.68%)</td><td>0.53 <b>(+29.33%)</b></td><td>2673.50 (+2.75%)</td><td>2379.80 (+4.17%)</td><td>2556.20 (+15.85%)</td><td>1885.70 (-4.25%)</td><td>332.07 <b>(+25.92%)</b></td><td>1121.02 (+4.44%)</td><td>903.74 (-3.37%)</td><td>827.00 (-13.68%)</td><td>790.70 (-2.68%)</td><td>138.96 <b>(+29.33%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.09 (n/a)</td><td>3.57 (n/a)</td><td>3.65 (n/a)</td><td>3.10 (n/a)</td><td>0.41 (n/a)</td><td>2601.90 (n/a)</td><td>2284.50 (n/a)</td><td>2206.40 (n/a)</td><td>1969.50 (n/a)</td><td>263.71 (n/a)</td><td>1073.33 (n/a)</td><td>935.23 (n/a)</td><td>958.08 (n/a)</td><td>812.45 (n/a)</td><td>107.44 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.54 <b>(+29.63%)</b></td><td>0.42 <b>(+23.81%)</b></td><td>0.47 <b>(+44.52%)</b></td><td>0.28 (-0.49%)</td><td>0.11 <b>(+136.14%)</b></td><td>4397.20 (+0.49%)</td><td>3189.46 (-15.08%)</td><td>2631.40 <b>(-30.81%)</b></td><td>2321.00 <b>(-22.86%)</b></td><td>936.63 <b>(+91.32%)</b></td><td>28.91 <b>(+29.63%)</b></td><td>22.45 <b>(+23.81%)</b></td><td>25.50 <b>(+44.52%)</b></td><td>15.26 (-0.49%)</td><td>6.03 <b>(+136.14%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>4375.70 (n/a)</td><td>3755.82 (n/a)</td><td>3802.90 (n/a)</td><td>3008.80 (n/a)</td><td>489.58 (n/a)</td><td>22.30 (n/a)</td><td>18.13 (n/a)</td><td>17.65 (n/a)</td><td>15.34 (n/a)</td><td>2.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.94 (+0.54%)</td><td>3.94 (-10.86%)</td><td>3.69 <b>(-20.70%)</b></td><td>3.50 (-7.60%)</td><td>0.58 (+19.92%)</td><td>1898.80 (+8.22%)</td><td>1716.38 (+12.76%)</td><td>1801.90 <b>(+26.10%)</b></td><td>1345.20 (-0.53%)</td><td>219.78 <b>(+25.82%)</b></td><td>1527.79 (+0.54%)</td><td>1215.84 (-10.86%)</td><td>1140.56 <b>(-20.70%)</b></td><td>1082.39 (-7.60%)</td><td>180.45 (+19.92%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.92 (n/a)</td><td>4.41 (n/a)</td><td>4.66 (n/a)</td><td>3.79 (n/a)</td><td>0.49 (n/a)</td><td>1754.50 (n/a)</td><td>1522.18 (n/a)</td><td>1428.90 (n/a)</td><td>1352.40 (n/a)</td><td>174.68 (n/a)</td><td>1519.64 (n/a)</td><td>1363.96 (n/a)</td><td>1438.35 (n/a)</td><td>1171.42 (n/a)</td><td>150.48 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.29 (n/a)</td><td>13.22 (n/a)</td><td>13.20 (n/a)</td><td>13.18 (n/a)</td><td>0.05 (n/a)</td><td>13.28 (n/a)</td><td>13.21 (n/a)</td><td>13.19 (n/a)</td><td>13.17 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>24.49 (-0.99%)</td><td>24.20 (-0.18%)</td><td>24.31 (+0.11%)</td><td>23.81 (+0.10%)</td><td>0.27 <b>(-30.08%)</b></td><td>24.47 (-0.99%)</td><td>24.19 (-0.18%)</td><td>24.29 (+0.11%)</td><td>23.79 (+0.10%)</td><td>0.27 <b>(-30.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>24.73 (n/a)</td><td>24.24 (n/a)</td><td>24.28 (n/a)</td><td>23.79 (n/a)</td><td>0.38 (n/a)</td><td>24.72 (n/a)</td><td>24.23 (n/a)</td><td>24.27 (n/a)</td><td>23.77 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>40.69 (-10.10%)</td><td>39.47 (-5.55%)</td><td>40.01 (-3.37%)</td><td>37.28 (-5.22%)</td><td>1.32 <b>(-42.42%)</b></td><td>40.66 (-10.10%)</td><td>39.44 (-5.55%)</td><td>39.98 (-3.37%)</td><td>37.26 (-5.22%)</td><td>1.32 <b>(-42.42%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>45.26 (n/a)</td><td>41.78 (n/a)</td><td>41.40 (n/a)</td><td>39.33 (n/a)</td><td>2.29 (n/a)</td><td>45.23 (n/a)</td><td>41.76 (n/a)</td><td>41.37 (n/a)</td><td>39.31 (n/a)</td><td>2.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>43.95 (-4.18%)</td><td>40.97 (-5.80%)</td><td>41.08 (-5.02%)</td><td>37.57 (-10.83%)</td><td>2.85 <b>(+99.85%)</b></td><td>43.92 (-4.18%)</td><td>40.94 (-5.80%)</td><td>41.05 (-5.02%)</td><td>37.55 (-10.83%)</td><td>2.84 <b>(+99.85%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>45.87 (n/a)</td><td>43.49 (n/a)</td><td>43.25 (n/a)</td><td>42.14 (n/a)</td><td>1.42 (n/a)</td><td>45.84 (n/a)</td><td>43.46 (n/a)</td><td>43.22 (n/a)</td><td>42.11 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.31 (n/a)</td><td>13.07 (n/a)</td><td>13.25 (n/a)</td><td>12.55 (n/a)</td><td>0.33 (n/a)</td><td>13.30 (n/a)</td><td>13.06 (n/a)</td><td>13.25 (n/a)</td><td>12.54 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>24.46 (-1.94%)</td><td>24.12 (-0.55%)</td><td>24.08 (+0.09%)</td><td>23.79 (+1.05%)</td><td>0.29 <b>(-48.85%)</b></td><td>24.45 (-1.94%)</td><td>24.10 (-0.55%)</td><td>24.07 (+0.09%)</td><td>23.78 (+1.05%)</td><td>0.29 <b>(-48.85%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>24.95 (n/a)</td><td>24.25 (n/a)</td><td>24.06 (n/a)</td><td>23.54 (n/a)</td><td>0.56 (n/a)</td><td>24.93 (n/a)</td><td>24.24 (n/a)</td><td>24.05 (n/a)</td><td>23.53 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>41.78 (-1.00%)</td><td>39.32 (-4.41%)</td><td>39.49 (-3.27%)</td><td>35.73 (-11.51%)</td><td>2.35 <b>(+203.01%)</b></td><td>41.76 (-1.00%)</td><td>39.30 (-4.41%)</td><td>39.46 (-3.27%)</td><td>35.71 (-11.51%)</td><td>2.35 <b>(+203.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>42.21 (n/a)</td><td>41.14 (n/a)</td><td>40.82 (n/a)</td><td>40.38 (n/a)</td><td>0.77 (n/a)</td><td>42.18 (n/a)</td><td>41.11 (n/a)</td><td>40.80 (n/a)</td><td>40.35 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>45.49 (-2.47%)</td><td>41.32 (-0.34%)</td><td>41.65 (-2.64%)</td><td>37.74 <b>(+26.27%)</b></td><td>3.47 <b>(-48.21%)</b></td><td>45.46 (-2.47%)</td><td>41.30 (-0.34%)</td><td>41.63 (-2.64%)</td><td>37.71 <b>(+26.27%)</b></td><td>3.47 <b>(-48.21%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>46.64 (n/a)</td><td>41.46 (n/a)</td><td>42.78 (n/a)</td><td>29.89 (n/a)</td><td>6.71 (n/a)</td><td>46.61 (n/a)</td><td>41.44 (n/a)</td><td>42.75 (n/a)</td><td>29.87 (n/a)</td><td>6.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>9.53 (-3.48%)</td><td>8.90 (-2.28%)</td><td>9.05 (+2.07%)</td><td>8.39 (-1.43%)</td><td>0.48 <b>(-20.78%)</b></td><td>9.51 (-3.48%)</td><td>8.88 (-2.28%)</td><td>9.04 (+2.07%)</td><td>8.37 (-1.43%)</td><td>0.48 <b>(-20.78%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>9.88 (n/a)</td><td>9.11 (n/a)</td><td>8.87 (n/a)</td><td>8.51 (n/a)</td><td>0.61 (n/a)</td><td>9.86 (n/a)</td><td>9.09 (n/a)</td><td>8.85 (n/a)</td><td>8.50 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.03 (+5.45%)</td><td>0.97 (+5.88%)</td><td>1.02 (+8.22%)</td><td>0.86 (+7.63%)</td><td>0.08 (+8.28%)</td><td>1.01 (+5.45%)</td><td>0.95 (+5.88%)</td><td>1.00 (+8.22%)</td><td>0.85 (+7.63%)</td><td>0.07 (+8.28%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.97 (n/a)</td><td>0.91 (n/a)</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.07 (n/a)</td><td>0.96 (n/a)</td><td>0.90 (n/a)</td><td>0.93 (n/a)</td><td>0.79 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.30 (+4.81%)</td><td>1.04 (-9.52%)</td><td>1.04 (-11.43%)</td><td>0.85 (-11.90%)</td><td>0.18 <b>(+61.89%)</b></td><td>1.29 (+4.81%)</td><td>1.03 (-9.52%)</td><td>1.02 (-11.43%)</td><td>0.84 (-11.90%)</td><td>0.18 <b>(+61.89%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.24 (n/a)</td><td>1.15 (n/a)</td><td>1.17 (n/a)</td><td>0.96 (n/a)</td><td>0.11 (n/a)</td><td>1.23 (n/a)</td><td>1.14 (n/a)</td><td>1.16 (n/a)</td><td>0.95 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>18.41 (-0.63%)</td><td>17.09 (+5.28%)</td><td>16.96 (+2.14%)</td><td>16.07 (+10.67%)</td><td>1.04 <b>(-37.34%)</b></td><td>18.19 (-0.63%)</td><td>16.89 (+5.28%)</td><td>16.76 (+2.14%)</td><td>15.88 (+10.67%)</td><td>1.03 <b>(-37.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>18.52 (n/a)</td><td>16.23 (n/a)</td><td>16.60 (n/a)</td><td>14.52 (n/a)</td><td>1.66 (n/a)</td><td>18.31 (n/a)</td><td>16.04 (n/a)</td><td>16.41 (n/a)</td><td>14.35 (n/a)</td><td>1.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>14.38 (+4.86%)</td><td>13.52 <b>(+22.20%)</b></td><td>13.19 (+2.75%)</td><td>12.93 <b>(+72.10%)</b></td><td>0.61 <b>(-79.93%)</b></td><td>14.13 (+4.86%)</td><td>13.28 <b>(+22.20%)</b></td><td>12.96 (+2.75%)</td><td>12.70 <b>(+72.10%)</b></td><td>0.60 <b>(-79.93%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.71 (n/a)</td><td>11.06 (n/a)</td><td>12.83 (n/a)</td><td>7.51 (n/a)</td><td>3.05 (n/a)</td><td>13.47 (n/a)</td><td>10.87 (n/a)</td><td>12.61 (n/a)</td><td>7.38 (n/a)</td><td>3.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.35 (-13.71%)</td><td>7.57 (-13.55%)</td><td>7.91 (-12.13%)</td><td>6.37 (-12.98%)</td><td>0.84 (-8.26%)</td><td>8.20 (-13.71%)</td><td>7.44 (-13.55%)</td><td>7.77 (-12.13%)</td><td>6.26 (-12.98%)</td><td>0.83 (-8.26%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>9.67 (n/a)</td><td>8.76 (n/a)</td><td>9.00 (n/a)</td><td>7.32 (n/a)</td><td>0.92 (n/a)</td><td>9.50 (n/a)</td><td>8.61 (n/a)</td><td>8.84 (n/a)</td><td>7.20 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>5.80 (-12.69%)</td><td>5.44 (-3.52%)</td><td>5.49 (+1.87%)</td><td>4.72 (-11.05%)</td><td>0.44 <b>(-22.13%)</b></td><td>5.71 (-12.69%)</td><td>5.35 (-3.52%)</td><td>5.40 (+1.87%)</td><td>4.65 (-11.05%)</td><td>0.44 <b>(-22.13%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.65 (n/a)</td><td>5.64 (n/a)</td><td>5.39 (n/a)</td><td>5.31 (n/a)</td><td>0.57 (n/a)</td><td>6.54 (n/a)</td><td>5.55 (n/a)</td><td>5.30 (n/a)</td><td>5.22 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.39 (n/a)</td><td>12.04 (n/a)</td><td>11.83 (n/a)</td><td>11.03 (n/a)</td><td>1.06 (n/a)</td><td>13.38 (n/a)</td><td>12.03 (n/a)</td><td>11.83 (n/a)</td><td>11.02 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.43 (n/a)</td><td>13.15 (n/a)</td><td>13.17 (n/a)</td><td>12.87 (n/a)</td><td>0.25 (n/a)</td><td>13.42 (n/a)</td><td>13.15 (n/a)</td><td>13.17 (n/a)</td><td>12.86 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>174.82 (n/a)</td><td>171.50 (n/a)</td><td>136.70 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.90 (n/a)</td><td>165.98 (n/a)</td><td>176.20 (n/a)</td><td>141.10 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.60 (n/a)</td><td>180.34 (n/a)</td><td>188.10 (n/a)</td><td>135.70 (n/a)</td><td>27.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.20 (n/a)</td><td>177.28 (n/a)</td><td>166.40 (n/a)</td><td>147.00 (n/a)</td><td>40.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.10 (n/a)</td><td>184.20 (n/a)</td><td>162.00 (n/a)</td><td>147.40 (n/a)</td><td>38.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>257.80 (n/a)</td><td>196.48 (n/a)</td><td>184.20 (n/a)</td><td>151.80 (n/a)</td><td>42.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.20 (n/a)</td><td>159.62 (n/a)</td><td>154.90 (n/a)</td><td>130.80 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.90 (n/a)</td><td>209.28 (n/a)</td><td>205.70 (n/a)</td><td>179.20 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>161.22 (n/a)</td><td>162.90 (n/a)</td><td>124.90 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>169.62 (n/a)</td><td>167.40 (n/a)</td><td>114.50 (n/a)</td><td>39.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>197.16 (n/a)</td><td>188.70 (n/a)</td><td>169.90 (n/a)</td><td>26.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>175.70 (n/a)</td><td>172.00 (n/a)</td><td>168.80 (n/a)</td><td>8.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.30 (n/a)</td><td>178.70 (n/a)</td><td>175.80 (n/a)</td><td>171.00 (n/a)</td><td>6.94 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>183.14 (n/a)</td><td>188.50 (n/a)</td><td>130.80 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>165.76 (n/a)</td><td>176.40 (n/a)</td><td>132.80 (n/a)</td><td>29.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>268.10 (n/a)</td><td>221.76 (n/a)</td><td>216.50 (n/a)</td><td>190.20 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>356.80 (n/a)</td><td>224.14 (n/a)</td><td>191.30 (n/a)</td><td>149.80 (n/a)</td><td>82.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.40 (n/a)</td><td>181.76 (n/a)</td><td>160.60 (n/a)</td><td>129.50 (n/a)</td><td>48.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>178.10 (n/a)</td><td>174.20 (n/a)</td><td>168.00 (n/a)</td><td>10.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>181.20 (n/a)</td><td>175.84 (n/a)</td><td>176.60 (n/a)</td><td>167.70 (n/a)</td><td>5.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>168.58 (n/a)</td><td>171.30 (n/a)</td><td>139.50 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>253.30 (n/a)</td><td>208.20 (n/a)</td><td>209.10 (n/a)</td><td>176.40 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>300.80 (n/a)</td><td>216.04 (n/a)</td><td>205.00 (n/a)</td><td>157.00 (n/a)</td><td>52.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.60 (n/a)</td><td>215.00 (n/a)</td><td>207.70 (n/a)</td><td>179.80 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>186.54 (n/a)</td><td>188.20 (n/a)</td><td>166.30 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>260.40 (n/a)</td><td>189.64 (n/a)</td><td>184.40 (n/a)</td><td>134.20 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>177.70 (n/a)</td><td>146.20 (n/a)</td><td>147.30 (n/a)</td><td>116.80 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>262.40 (n/a)</td><td>169.38 (n/a)</td><td>139.40 (n/a)</td><td>126.80 (n/a)</td><td>55.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>248.70 (n/a)</td><td>164.96 (n/a)</td><td>137.50 (n/a)</td><td>127.50 (n/a)</td><td>50.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>248.30 (n/a)</td><td>185.96 (n/a)</td><td>173.30 (n/a)</td><td>157.00 (n/a)</td><td>37.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>252.10 (n/a)</td><td>200.22 (n/a)</td><td>190.60 (n/a)</td><td>175.80 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>292.60 (n/a)</td><td>228.12 (n/a)</td><td>207.90 (n/a)</td><td>189.90 (n/a)</td><td>44.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-19.69%)</td><td>0.02 (-3.08%)</td><td>0.02 (+0.13%)</td><td>0.02 <b>(+20.65%)</b></td><td>0.00 <b>(-53.40%)</b></td><td>191.70 (-17.12%)</td><td>166.40 (-0.79%)</td><td>165.50 (-0.12%)</td><td>141.00 <b>(+24.45%)</b></td><td>20.52 <b>(-51.33%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.30 (n/a)</td><td>167.72 (n/a)</td><td>165.70 (n/a)</td><td>113.30 (n/a)</td><td>42.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (-19.27%)</td><td>0.02 (-12.86%)</td><td>0.02 (-5.34%)</td><td>0.02 (-10.59%)</td><td>0.00 <b>(-47.86%)</b></td><td>216.70 (+11.87%)</td><td>189.80 (+13.37%)</td><td>190.30 (+5.60%)</td><td>165.20 <b>(+23.84%)</b></td><td>18.38 <b>(-27.29%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>167.42 (n/a)</td><td>180.20 (n/a)</td><td>133.40 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-14.92%)</td><td>0.02 (-15.22%)</td><td>0.03 (-8.46%)</td><td>0.02 (-17.18%)</td><td>0.01 (-11.03%)</td><td>252.20 <b>(+20.73%)</b></td><td>176.90 (+18.50%)</td><td>156.90 (+9.19%)</td><td>138.30 (+17.60%)</td><td>44.89 <b>(+26.53%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>149.28 (n/a)</td><td>143.70 (n/a)</td><td>117.60 (n/a)</td><td>35.48 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 <b>(+51.55%)</b></td><td>0.02 (+5.21%)</td><td>0.02 (-13.98%)</td><td>0.02 (-1.19%)</td><td>0.01 <b>(+160.87%)</b></td><td>239.60 (+1.23%)</td><td>187.48 (+1.46%)</td><td>206.30 (+16.23%)</td><td>103.30 <b>(-33.99%)</b></td><td>52.00 <b>(+63.15%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.70 (n/a)</td><td>184.78 (n/a)</td><td>177.50 (n/a)</td><td>156.50 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-6.21%)</td><td>0.03 (-0.65%)</td><td>0.03 (+8.90%)</td><td>0.02 (+14.08%)</td><td>0.00 <b>(-39.86%)</b></td><td>188.50 (-12.33%)</td><td>158.44 (-3.17%)</td><td>162.60 (-8.14%)</td><td>124.70 (+6.67%)</td><td>25.55 <b>(-41.23%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>163.62 (n/a)</td><td>177.00 (n/a)</td><td>116.90 (n/a)</td><td>43.47 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 <b>(+20.33%)</b></td><td>0.02 (+16.64%)</td><td>0.02 (-5.26%)</td><td>0.02 (+9.97%)</td><td>0.01 <b>(+47.34%)</b></td><td>232.30 (-9.08%)</td><td>179.84 (-11.75%)</td><td>203.60 (+5.55%)</td><td>115.30 (-16.93%)</td><td>52.47 (+7.93%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>255.50 (n/a)</td><td>203.78 (n/a)</td><td>192.90 (n/a)</td><td>138.80 (n/a)</td><td>48.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 <b>(+26.33%)</b></td><td>0.03 (+18.94%)</td><td>0.03 (+18.61%)</td><td>0.02 (+10.56%)</td><td>0.01 <b>(+47.83%)</b></td><td>249.70 (-9.56%)</td><td>170.38 (-14.30%)</td><td>163.50 (-15.68%)</td><td>123.30 <b>(-20.81%)</b></td><td>48.38 (+5.01%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>276.10 (n/a)</td><td>198.80 (n/a)</td><td>193.90 (n/a)</td><td>155.70 (n/a)</td><td>46.08 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 <b>(-37.67%)</b></td><td>0.02 <b>(-20.91%)</b></td><td>0.02 (-12.49%)</td><td>0.02 <b>(-23.68%)</b></td><td>0.00 <b>(-61.93%)</b></td><td>257.40 <b>(+30.99%)</b></td><td>217.02 <b>(+24.34%)</b></td><td>206.80 (+14.25%)</td><td>205.50 <b>(+60.42%)</b></td><td>22.62 (-18.09%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>174.54 (n/a)</td><td>181.00 (n/a)</td><td>128.10 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (-5.30%)</td><td>0.05 (+1.70%)</td><td>0.06 (+8.49%)</td><td>0.04 (+6.84%)</td><td>0.01 <b>(-20.54%)</b></td><td>192.40 (-6.42%)</td><td>157.96 (-2.52%)</td><td>145.90 (-7.83%)</td><td>140.60 (+5.56%)</td><td>21.89 <b>(-22.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>162.04 (n/a)</td><td>158.30 (n/a)</td><td>133.20 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+11.23%)</td><td>0.05 (-1.09%)</td><td>0.04 (-15.00%)</td><td>0.04 (+9.27%)</td><td>0.01 <b>(+29.68%)</b></td><td>199.50 (-8.49%)</td><td>170.22 (+2.16%)</td><td>182.90 (+17.62%)</td><td>120.10 (-10.10%)</td><td>34.51 (+6.47%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>166.62 (n/a)</td><td>155.50 (n/a)</td><td>133.60 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (+7.97%)</td><td>0.04 (+1.34%)</td><td>0.05 (+9.24%)</td><td>0.02 <b>(-33.88%)</b></td><td>0.01 <b>(+121.56%)</b></td><td>368.20 <b>(+51.27%)</b></td><td>209.24 (+7.32%)</td><td>174.40 (-8.45%)</td><td>159.70 (-7.37%)</td><td>89.28 <b>(+216.13%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.40 (n/a)</td><td>194.96 (n/a)</td><td>190.50 (n/a)</td><td>172.40 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (-7.34%)</td><td>0.05 (-11.84%)</td><td>0.05 <b>(-20.97%)</b></td><td>0.04 (-8.85%)</td><td>0.01 (-16.96%)</td><td>201.60 (+9.74%)</td><td>169.90 (+12.86%)</td><td>173.60 <b>(+26.53%)</b></td><td>132.70 (+7.97%)</td><td>24.82 (-5.76%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>150.54 (n/a)</td><td>137.20 (n/a)</td><td>122.90 (n/a)</td><td>26.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (-8.57%)</td><td>0.05 (-4.50%)</td><td>0.06 (+0.51%)</td><td>0.03 <b>(-32.30%)</b></td><td>0.01 <b>(+21.30%)</b></td><td>319.20 <b>(+47.71%)</b></td><td>182.36 (+10.91%)</td><td>148.20 (-0.54%)</td><td>136.40 (+9.38%)</td><td>77.64 <b>(+98.45%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>164.42 (n/a)</td><td>149.00 (n/a)</td><td>124.70 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (-18.00%)</td><td>0.05 (+1.75%)</td><td>0.05 (+5.54%)</td><td>0.04 <b>(+20.16%)</b></td><td>0.01 <b>(-49.78%)</b></td><td>211.10 (-16.79%)</td><td>166.70 (-6.61%)</td><td>157.50 (-5.23%)</td><td>138.50 <b>(+21.92%)</b></td><td>27.35 <b>(-47.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.70 (n/a)</td><td>178.50 (n/a)</td><td>166.20 (n/a)</td><td>113.60 (n/a)</td><td>52.27 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+15.45%)</td><td>0.06 <b>(+23.32%)</b></td><td>0.06 <b>(+29.53%)</b></td><td>0.05 <b>(+20.39%)</b></td><td>0.01 (+6.17%)</td><td>173.10 (-16.94%)</td><td>149.60 (-19.15%)</td><td>146.10 <b>(-22.78%)</b></td><td>124.30 (-13.44%)</td><td>20.15 <b>(-21.57%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>185.04 (n/a)</td><td>189.20 (n/a)</td><td>143.60 (n/a)</td><td>25.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 <b>(+20.18%)</b></td><td>0.05 (+12.44%)</td><td>0.04 (+7.83%)</td><td>0.04 (+16.62%)</td><td>0.01 <b>(+36.51%)</b></td><td>205.50 (-14.27%)</td><td>176.98 (-10.53%)</td><td>182.50 (-7.27%)</td><td>129.50 (-16.77%)</td><td>29.19 (-4.46%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>197.82 (n/a)</td><td>196.80 (n/a)</td><td>155.60 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 <b>(+26.66%)</b></td><td>0.05 <b>(+26.72%)</b></td><td>0.05 (+12.64%)</td><td>0.04 <b>(+38.67%)</b></td><td>0.01 <b>(+50.41%)</b></td><td>202.30 <b>(-27.90%)</b></td><td>164.34 <b>(-20.12%)</b></td><td>179.30 (-11.19%)</td><td>117.20 <b>(-21.02%)</b></td><td>40.10 (-15.56%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.60 (n/a)</td><td>205.74 (n/a)</td><td>201.90 (n/a)</td><td>148.40 (n/a)</td><td>47.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (+0.51%)</td><td>0.04 (+6.76%)</td><td>0.04 (+5.99%)</td><td>0.04 (+7.93%)</td><td>0.00 (-3.38%)</td><td>221.50 (-7.36%)</td><td>199.58 (-6.47%)</td><td>206.70 (-5.66%)</td><td>173.30 (-0.52%)</td><td>22.07 (-9.24%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.10 (n/a)</td><td>213.38 (n/a)</td><td>219.10 (n/a)</td><td>174.20 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (+4.18%)</td><td>0.12 (+10.02%)</td><td>0.11 (+11.20%)</td><td>0.11 (+19.31%)</td><td>0.02 (-15.94%)</td><td>154.40 (-16.18%)</td><td>141.76 (-10.04%)</td><td>148.00 (-10.09%)</td><td>111.00 (-4.06%)</td><td>17.55 <b>(-31.05%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.20 (n/a)</td><td>157.58 (n/a)</td><td>164.60 (n/a)</td><td>115.70 (n/a)</td><td>25.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 <b>(+25.34%)</b></td><td>0.11 <b>(+22.21%)</b></td><td>0.10 (+6.05%)</td><td>0.09 <b>(+57.79%)</b></td><td>0.02 (-11.92%)</td><td>183.70 <b>(-36.63%)</b></td><td>153.50 <b>(-21.00%)</b></td><td>157.00 (-5.76%)</td><td>118.90 <b>(-20.20%)</b></td><td>24.92 <b>(-56.67%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>289.90 (n/a)</td><td>194.30 (n/a)</td><td>166.60 (n/a)</td><td>149.00 (n/a)</td><td>57.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (-9.42%)</td><td>0.10 (+1.78%)</td><td>0.10 (+5.54%)</td><td>0.08 <b>(+40.39%)</b></td><td>0.02 <b>(-43.42%)</b></td><td>217.40 <b>(-28.77%)</b></td><td>171.72 (-8.42%)</td><td>162.70 (-5.24%)</td><td>139.70 (+10.43%)</td><td>31.51 <b>(-55.84%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>305.20 (n/a)</td><td>187.50 (n/a)</td><td>171.70 (n/a)</td><td>126.50 (n/a)</td><td>71.36 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (-8.50%)</td><td>0.11 (+2.21%)</td><td>0.11 (+7.60%)</td><td>0.09 (+2.33%)</td><td>0.01 <b>(-28.24%)</b></td><td>189.50 (-2.27%)</td><td>156.96 (-3.10%)</td><td>151.70 (-7.05%)</td><td>135.50 (+9.27%)</td><td>20.60 <b>(-20.97%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.90 (n/a)</td><td>161.98 (n/a)</td><td>163.20 (n/a)</td><td>124.00 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 <b>(+20.90%)</b></td><td>0.11 (+18.12%)</td><td>0.11 (+12.86%)</td><td>0.09 <b>(+20.41%)</b></td><td>0.01 (+7.00%)</td><td>177.10 (-16.93%)</td><td>151.16 (-15.65%)</td><td>152.70 (-11.38%)</td><td>124.60 (-17.32%)</td><td>18.89 <b>(-27.51%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>179.20 (n/a)</td><td>172.30 (n/a)</td><td>150.70 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (-3.97%)</td><td>0.10 (-0.69%)</td><td>0.09 (-4.10%)</td><td>0.08 <b>(+22.84%)</b></td><td>0.02 <b>(-34.45%)</b></td><td>212.20 (-18.60%)</td><td>174.14 (-5.41%)</td><td>178.80 (+4.32%)</td><td>121.50 (+4.11%)</td><td>33.01 <b>(-47.81%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>260.70 (n/a)</td><td>184.10 (n/a)</td><td>171.40 (n/a)</td><td>116.70 (n/a)</td><td>63.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (+3.30%)</td><td>0.08 (-3.70%)</td><td>0.09 (-3.20%)</td><td>0.06 (-12.55%)</td><td>0.02 (+11.47%)</td><td>290.50 (+14.33%)</td><td>206.82 (+5.32%)</td><td>187.80 (+3.30%)</td><td>153.10 (-3.22%)</td><td>54.58 <b>(+27.19%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>254.10 (n/a)</td><td>196.38 (n/a)</td><td>181.80 (n/a)</td><td>158.20 (n/a)</td><td>42.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (-18.58%)</td><td>0.07 (-7.95%)</td><td>0.08 (-3.89%)</td><td>0.06 (-13.30%)</td><td>0.01 <b>(-30.20%)</b></td><td>269.40 (+15.37%)</td><td>225.94 (+8.24%)</td><td>217.70 (+4.06%)</td><td>208.90 <b>(+22.81%)</b></td><td>25.13 (+0.20%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>208.74 (n/a)</td><td>209.20 (n/a)</td><td>170.10 (n/a)</td><td>25.08 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (+1.55%)</td><td>0.21 (+4.24%)</td><td>0.20 (+3.54%)</td><td>0.16 <b>(+21.22%)</b></td><td>0.05 (-12.92%)</td><td>204.70 (-17.53%)</td><td>161.44 (-6.18%)</td><td>167.00 (-3.47%)</td><td>124.90 (-1.58%)</td><td>34.34 <b>(-29.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>248.20 (n/a)</td><td>172.08 (n/a)</td><td>173.00 (n/a)</td><td>126.90 (n/a)</td><td>48.91 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 <b>(-26.32%)</b></td><td>0.18 (-13.94%)</td><td>0.18 (-11.64%)</td><td>0.17 (-6.48%)</td><td>0.01 <b>(-78.87%)</b></td><td>188.60 (+6.98%)</td><td>181.12 (+14.92%)</td><td>181.40 (+13.16%)</td><td>173.60 <b>(+35.73%)</b></td><td>5.74 <b>(-68.53%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.30 (n/a)</td><td>157.60 (n/a)</td><td>160.30 (n/a)</td><td>127.90 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (+2.47%)</td><td>0.21 (-5.83%)</td><td>0.20 (-8.22%)</td><td>0.17 (-9.01%)</td><td>0.04 <b>(+43.71%)</b></td><td>194.50 (+9.89%)</td><td>164.04 (+7.91%)</td><td>167.00 (+8.94%)</td><td>128.60 (-2.43%)</td><td>30.51 <b>(+58.67%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>177.00 (n/a)</td><td>152.02 (n/a)</td><td>153.30 (n/a)</td><td>131.80 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 <b>(+28.98%)</b></td><td>0.19 (-2.56%)</td><td>0.19 (-2.90%)</td><td>0.09 <b>(-38.95%)</b></td><td>0.07 <b>(+108.79%)</b></td><td>385.10 <b>(+63.80%)</b></td><td>202.86 (+16.98%)</td><td>174.00 (+2.96%)</td><td>112.40 <b>(-22.43%)</b></td><td>105.52 <b>(+186.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>235.10 (n/a)</td><td>173.42 (n/a)</td><td>169.00 (n/a)</td><td>144.90 (n/a)</td><td>36.78 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (+11.96%)</td><td>0.19 (-5.43%)</td><td>0.17 (-14.63%)</td><td>0.16 (-8.58%)</td><td>0.04 <b>(+110.38%)</b></td><td>206.50 (+9.37%)</td><td>176.82 (+8.05%)</td><td>190.80 (+17.13%)</td><td>131.60 (-10.72%)</td><td>31.48 <b>(+103.13%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.80 (n/a)</td><td>163.64 (n/a)</td><td>162.90 (n/a)</td><td>147.40 (n/a)</td><td>15.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (-4.07%)</td><td>0.16 (-18.19%)</td><td>0.16 <b>(-22.27%)</b></td><td>0.11 <b>(-28.85%)</b></td><td>0.05 <b>(+79.02%)</b></td><td>285.60 <b>(+40.55%)</b></td><td>216.88 <b>(+28.87%)</b></td><td>210.80 <b>(+28.62%)</b></td><td>145.20 (+4.24%)</td><td>61.40 <b>(+167.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.20 (n/a)</td><td>168.30 (n/a)</td><td>163.90 (n/a)</td><td>139.30 (n/a)</td><td>22.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (-15.91%)</td><td>0.13 <b>(-24.13%)</b></td><td>0.14 (-17.44%)</td><td>0.09 <b>(-45.30%)</b></td><td>0.03 <b>(+306.07%)</b></td><td>378.20 <b>(+82.79%)</b></td><td>267.56 <b>(+36.94%)</b></td><td>232.20 <b>(+21.13%)</b></td><td>223.90 (+18.91%)</td><td>65.50 <b>(+778.10%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>195.38 (n/a)</td><td>191.70 (n/a)</td><td>188.30 (n/a)</td><td>7.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 <b>(+49.67%)</b></td><td>0.02 (-7.59%)</td><td>0.02 <b>(-25.52%)</b></td><td>0.01 <b>(-27.76%)</b></td><td>0.01 <b>(+287.70%)</b></td><td>280.30 <b>(+38.42%)</b></td><td>205.68 <b>(+20.76%)</b></td><td>216.60 <b>(+34.28%)</b></td><td>100.70 <b>(-33.18%)</b></td><td>65.27 <b>(+223.21%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.50 (n/a)</td><td>170.32 (n/a)</td><td>161.30 (n/a)</td><td>150.70 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 <b>(+23.35%)</b></td><td>0.03 (+9.26%)</td><td>0.03 (-4.02%)</td><td>0.02 (+2.34%)</td><td>0.01 <b>(+106.73%)</b></td><td>182.70 (-2.30%)</td><td>148.72 (-6.26%)</td><td>162.20 (+4.17%)</td><td>111.00 (-18.92%)</td><td>29.75 <b>(+59.98%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.00 (n/a)</td><td>158.66 (n/a)</td><td>155.70 (n/a)</td><td>136.90 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (+15.46%)</td><td>0.02 (-1.12%)</td><td>0.02 (+4.85%)</td><td>0.01 <b>(-22.77%)</b></td><td>0.01 <b>(+234.42%)</b></td><td>324.90 <b>(+29.49%)</b></td><td>244.38 (+7.78%)</td><td>209.10 (-4.61%)</td><td>177.50 (-13.37%)</td><td>73.49 <b>(+287.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.90 (n/a)</td><td>226.74 (n/a)</td><td>219.20 (n/a)</td><td>204.90 (n/a)</td><td>18.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 <b>(+31.50%)</b></td><td>0.02 <b>(+36.35%)</b></td><td>0.02 <b>(+34.71%)</b></td><td>0.02 <b>(+53.07%)</b></td><td>0.00 (+0.64%)</td><td>216.80 <b>(-34.68%)</b></td><td>174.20 <b>(-28.10%)</b></td><td>171.60 <b>(-25.78%)</b></td><td>139.20 <b>(-23.98%)</b></td><td>28.08 <b>(-50.54%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>331.90 (n/a)</td><td>242.28 (n/a)</td><td>231.20 (n/a)</td><td>183.10 (n/a)</td><td>56.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-10.71%)</td><td>0.02 (-13.68%)</td><td>0.02 (-7.16%)</td><td>0.01 <b>(-42.75%)</b></td><td>0.01 <b>(+52.85%)</b></td><td>327.10 <b>(+74.64%)</b></td><td>199.56 <b>(+24.69%)</b></td><td>181.30 (+7.72%)</td><td>138.70 (+12.04%)</td><td>76.62 <b>(+199.84%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.30 (n/a)</td><td>160.04 (n/a)</td><td>168.30 (n/a)</td><td>123.80 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 <b>(+41.21%)</b></td><td>0.03 (+19.92%)</td><td>0.03 (+12.12%)</td><td>0.02 (-6.16%)</td><td>0.01 <b>(+147.59%)</b></td><td>240.50 (+6.60%)</td><td>158.14 (-11.50%)</td><td>154.30 (-10.81%)</td><td>107.00 <b>(-29.23%)</b></td><td>51.97 <b>(+83.42%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>178.68 (n/a)</td><td>173.00 (n/a)</td><td>151.20 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 <b>(+20.55%)</b></td><td>0.03 <b>(+25.30%)</b></td><td>0.03 <b>(+35.21%)</b></td><td>0.02 <b>(+28.07%)</b></td><td>0.00 (+16.06%)</td><td>180.40 <b>(-21.90%)</b></td><td>158.60 <b>(-20.29%)</b></td><td>148.20 <b>(-26.01%)</b></td><td>139.40 (-17.07%)</td><td>19.16 <b>(-23.03%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.00 (n/a)</td><td>198.98 (n/a)</td><td>200.30 (n/a)</td><td>168.10 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+0.06%)</td><td>0.03 (+13.16%)</td><td>0.03 (+10.36%)</td><td>0.02 (+7.63%)</td><td>0.01 (-6.97%)</td><td>208.10 (-7.10%)</td><td>157.54 (-12.48%)</td><td>161.40 (-9.38%)</td><td>126.60 (-0.08%)</td><td>33.20 (-16.99%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>180.00 (n/a)</td><td>178.10 (n/a)</td><td>126.70 (n/a)</td><td>40.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 <b>(+29.77%)</b></td><td>0.02 (+19.61%)</td><td>0.02 (+4.11%)</td><td>0.02 <b>(+25.61%)</b></td><td>0.00 <b>(+34.39%)</b></td><td>202.60 <b>(-20.39%)</b></td><td>172.42 (-16.18%)</td><td>179.00 (-3.97%)</td><td>127.60 <b>(-22.95%)</b></td><td>32.00 (-18.06%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>254.50 (n/a)</td><td>205.70 (n/a)</td><td>186.40 (n/a)</td><td>165.60 (n/a)</td><td>39.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-4.36%)</td><td>0.02 (-11.22%)</td><td>0.02 (-13.86%)</td><td>0.02 (-14.82%)</td><td>0.00 (+5.38%)</td><td>238.80 (+17.40%)</td><td>188.56 (+13.55%)</td><td>194.50 (+16.12%)</td><td>138.40 (+4.53%)</td><td>36.95 <b>(+28.43%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.40 (n/a)</td><td>166.06 (n/a)</td><td>167.50 (n/a)</td><td>132.40 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+18.46%)</td><td>0.03 (+9.63%)</td><td>0.02 (+7.86%)</td><td>0.02 (+13.91%)</td><td>0.00 <b>(+45.08%)</b></td><td>182.30 (-12.23%)</td><td>165.34 (-8.29%)</td><td>168.20 (-7.28%)</td><td>129.10 (-15.57%)</td><td>21.22 (+5.77%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.70 (n/a)</td><td>180.28 (n/a)</td><td>181.40 (n/a)</td><td>152.90 (n/a)</td><td>20.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+19.23%)</td><td>0.03 <b>(+20.60%)</b></td><td>0.03 <b>(+20.00%)</b></td><td>0.02 <b>(+21.22%)</b></td><td>0.00 (+7.03%)</td><td>179.00 (-17.47%)</td><td>162.24 (-17.17%)</td><td>162.60 (-16.66%)</td><td>146.40 (-16.10%)</td><td>12.73 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.90 (n/a)</td><td>195.88 (n/a)</td><td>195.10 (n/a)</td><td>174.50 (n/a)</td><td>17.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-7.47%)</td><td>0.02 (+3.27%)</td><td>0.02 (+5.48%)</td><td>0.02 (+9.45%)</td><td>0.00 (-15.81%)</td><td>225.20 (-8.64%)</td><td>183.00 (-4.05%)</td><td>176.50 (-5.21%)</td><td>151.20 (+8.08%)</td><td>31.73 (-16.70%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.50 (n/a)</td><td>190.72 (n/a)</td><td>186.20 (n/a)</td><td>139.90 (n/a)</td><td>38.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (+6.45%)</td><td>0.02 (+9.08%)</td><td>0.02 (+9.12%)</td><td>0.02 (+12.36%)</td><td>0.00 <b>(-21.82%)</b></td><td>195.40 (-10.98%)</td><td>185.64 (-8.52%)</td><td>187.00 (-8.33%)</td><td>171.60 (-6.02%)</td><td>9.89 <b>(-34.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>202.92 (n/a)</td><td>204.00 (n/a)</td><td>182.60 (n/a)</td><td>15.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+18.99%)</td><td>0.02 (+7.90%)</td><td>0.02 (-1.13%)</td><td>0.02 (+4.66%)</td><td>0.01 <b>(+40.14%)</b></td><td>267.90 (-4.46%)</td><td>193.30 (-5.60%)</td><td>197.10 (+1.13%)</td><td>128.00 (-15.96%)</td><td>50.57 (+8.25%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>280.40 (n/a)</td><td>204.76 (n/a)</td><td>194.90 (n/a)</td><td>152.30 (n/a)</td><td>46.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 <b>(+44.82%)</b></td><td>0.03 <b>(+31.80%)</b></td><td>0.02 (+18.95%)</td><td>0.02 <b>(+35.12%)</b></td><td>0.00 <b>(+97.23%)</b></td><td>185.50 <b>(-26.01%)</b></td><td>161.64 <b>(-23.38%)</b></td><td>174.80 (-15.92%)</td><td>126.70 <b>(-30.95%)</b></td><td>24.57 (-0.98%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.70 (n/a)</td><td>210.96 (n/a)</td><td>207.90 (n/a)</td><td>183.50 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+3.78%)</td><td>0.05 (+4.97%)</td><td>0.05 (+6.92%)</td><td>0.04 (+6.00%)</td><td>0.01 (-8.19%)</td><td>221.30 (-5.63%)</td><td>171.46 (-5.78%)</td><td>172.00 (-6.47%)</td><td>125.40 (-3.69%)</td><td>35.59 (-16.85%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>181.98 (n/a)</td><td>183.90 (n/a)</td><td>130.20 (n/a)</td><td>42.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (+14.84%)</td><td>0.06 <b>(+24.08%)</b></td><td>0.05 (+19.78%)</td><td>0.05 <b>(+39.69%)</b></td><td>0.01 <b>(-30.16%)</b></td><td>165.80 <b>(-28.44%)</b></td><td>148.72 <b>(-20.69%)</b></td><td>149.80 (-16.50%)</td><td>128.10 (-12.98%)</td><td>13.57 <b>(-57.15%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>187.52 (n/a)</td><td>179.40 (n/a)</td><td>147.20 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (+11.47%)</td><td>0.04 (+10.48%)</td><td>0.04 (+10.60%)</td><td>0.03 (+4.28%)</td><td>0.01 <b>(+22.43%)</b></td><td>288.60 (-4.12%)</td><td>218.42 (-8.77%)</td><td>213.90 (-9.56%)</td><td>162.90 (-10.30%)</td><td>45.38 (+7.28%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.00 (n/a)</td><td>239.42 (n/a)</td><td>236.50 (n/a)</td><td>181.60 (n/a)</td><td>42.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (+16.67%)</td><td>0.04 (+6.93%)</td><td>0.04 (+3.66%)</td><td>0.04 (+5.10%)</td><td>0.01 <b>(+44.70%)</b></td><td>232.20 (-4.84%)</td><td>187.78 (-5.38%)</td><td>186.60 (-3.57%)</td><td>138.10 (-14.28%)</td><td>34.84 (+15.24%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.00 (n/a)</td><td>198.46 (n/a)</td><td>193.50 (n/a)</td><td>161.10 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (+16.29%)</td><td>0.05 (+14.69%)</td><td>0.06 (+17.01%)</td><td>0.02 <b>(-23.01%)</b></td><td>0.02 <b>(+48.18%)</b></td><td>339.50 <b>(+29.88%)</b></td><td>182.20 (-6.00%)</td><td>145.20 (-14.54%)</td><td>126.70 (-14.04%)</td><td>88.57 <b>(+77.29%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.40 (n/a)</td><td>193.84 (n/a)</td><td>169.90 (n/a)</td><td>147.40 (n/a)</td><td>49.96 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 <b>(+26.04%)</b></td><td>0.05 <b>(+20.09%)</b></td><td>0.05 (+16.09%)</td><td>0.04 (+11.69%)</td><td>0.01 <b>(+48.15%)</b></td><td>204.20 (-10.48%)</td><td>165.30 (-15.73%)</td><td>166.50 (-13.86%)</td><td>117.70 <b>(-20.63%)</b></td><td>32.66 (+3.73%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>196.16 (n/a)</td><td>193.30 (n/a)</td><td>148.30 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (+3.16%)</td><td>0.05 (-13.93%)</td><td>0.05 (-17.21%)</td><td>0.04 <b>(-20.65%)</b></td><td>0.01 <b>(+68.53%)</b></td><td>221.10 <b>(+26.05%)</b></td><td>175.14 (+19.24%)</td><td>172.50 <b>(+20.80%)</b></td><td>127.30 (-3.05%)</td><td>36.43 <b>(+105.12%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.40 (n/a)</td><td>146.88 (n/a)</td><td>142.80 (n/a)</td><td>131.30 (n/a)</td><td>17.76 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+9.88%)</td><td>0.05 (+2.19%)</td><td>0.05 (+4.05%)</td><td>0.04 <b>(+21.72%)</b></td><td>0.01 (-1.86%)</td><td>217.70 (-17.85%)</td><td>172.72 (-3.81%)</td><td>168.50 (-3.88%)</td><td>120.20 (-8.94%)</td><td>36.08 <b>(-30.09%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.00 (n/a)</td><td>179.56 (n/a)</td><td>175.30 (n/a)</td><td>132.00 (n/a)</td><td>51.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 <b>(+24.41%)</b></td><td>0.05 (-8.99%)</td><td>0.04 <b>(-27.56%)</b></td><td>0.03 <b>(-30.01%)</b></td><td>0.02 <b>(+85.40%)</b></td><td>283.40 <b>(+42.84%)</b></td><td>188.98 (+17.61%)</td><td>194.30 <b>(+38.10%)</b></td><td>109.20 (-19.59%)</td><td>63.20 <b>(+108.59%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>160.68 (n/a)</td><td>140.70 (n/a)</td><td>135.80 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+18.21%)</td><td>0.05 (+8.97%)</td><td>0.05 (+12.33%)</td><td>0.03 (+2.32%)</td><td>0.01 <b>(+26.43%)</b></td><td>242.30 (-2.30%)</td><td>176.96 (-7.20%)</td><td>173.50 (-10.98%)</td><td>118.50 (-15.42%)</td><td>44.18 (+3.97%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.00 (n/a)</td><td>190.68 (n/a)</td><td>194.90 (n/a)</td><td>140.10 (n/a)</td><td>42.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 <b>(+22.61%)</b></td><td>0.05 (+4.39%)</td><td>0.05 (+13.49%)</td><td>0.03 (+5.95%)</td><td>0.02 (+17.94%)</td><td>276.00 (-5.61%)</td><td>189.18 (-3.70%)</td><td>179.10 (-11.90%)</td><td>111.80 (-18.45%)</td><td>59.19 (-6.79%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.40 (n/a)</td><td>196.44 (n/a)</td><td>203.30 (n/a)</td><td>137.10 (n/a)</td><td>63.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (+1.24%)</td><td>0.05 (-1.15%)</td><td>0.05 (+11.13%)</td><td>0.03 <b>(-20.84%)</b></td><td>0.01 <b>(+61.24%)</b></td><td>240.60 <b>(+26.37%)</b></td><td>176.98 (+4.01%)</td><td>159.00 (-10.02%)</td><td>137.20 (-1.22%)</td><td>41.40 <b>(+106.90%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>170.16 (n/a)</td><td>176.70 (n/a)</td><td>138.90 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 <b>(+46.98%)</b></td><td>0.05 (+8.04%)</td><td>0.05 (+2.13%)</td><td>0.04 (-7.17%)</td><td>0.01 <b>(+244.55%)</b></td><td>227.10 (+7.73%)</td><td>176.64 (-3.03%)</td><td>169.20 (-2.08%)</td><td>115.20 <b>(-32.00%)</b></td><td>42.42 <b>(+146.80%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.80 (n/a)</td><td>182.16 (n/a)</td><td>172.80 (n/a)</td><td>169.40 (n/a)</td><td>17.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (-7.44%)</td><td>0.05 (+6.85%)</td><td>0.05 (+8.73%)</td><td>0.04 <b>(+54.72%)</b></td><td>0.01 <b>(-43.94%)</b></td><td>231.60 <b>(-35.38%)</b></td><td>184.84 (-12.89%)</td><td>168.90 (-8.01%)</td><td>160.60 (+8.08%)</td><td>30.33 <b>(-63.78%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>358.40 (n/a)</td><td>212.18 (n/a)</td><td>183.60 (n/a)</td><td>148.60 (n/a)</td><td>83.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 <b>(+45.48%)</b></td><td>0.05 (+12.08%)</td><td>0.05 (+14.91%)</td><td>0.04 (-8.22%)</td><td>0.01 <b>(+381.62%)</b></td><td>210.80 (+9.00%)</td><td>169.42 (-6.80%)</td><td>157.90 (-12.95%)</td><td>116.60 <b>(-31.25%)</b></td><td>38.86 <b>(+268.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.40 (n/a)</td><td>181.78 (n/a)</td><td>181.40 (n/a)</td><td>169.60 (n/a)</td><td>10.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 <b>(+52.36%)</b></td><td>0.05 <b>(+20.86%)</b></td><td>0.04 (+11.29%)</td><td>0.04 (+11.84%)</td><td>0.01 <b>(+195.24%)</b></td><td>213.20 (-10.61%)</td><td>178.48 (-14.32%)</td><td>183.40 (-10.14%)</td><td>117.60 <b>(-34.38%)</b></td><td>37.17 <b>(+67.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>208.30 (n/a)</td><td>204.10 (n/a)</td><td>179.20 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (-15.29%)</td><td>0.10 (-8.68%)</td><td>0.10 (-17.81%)</td><td>0.07 <b>(+61.86%)</b></td><td>0.02 <b>(-55.90%)</b></td><td>227.10 <b>(-38.22%)</b></td><td>171.92 (-6.58%)</td><td>160.40 <b>(+21.70%)</b></td><td>134.00 (+18.06%)</td><td>34.79 <b>(-67.42%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>367.60 (n/a)</td><td>184.02 (n/a)</td><td>131.80 (n/a)</td><td>113.50 (n/a)</td><td>106.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (+8.68%)</td><td>0.10 (+3.03%)</td><td>0.10 (-0.32%)</td><td>0.09 (+6.41%)</td><td>0.02 (+14.90%)</td><td>190.70 (-6.01%)</td><td>167.48 (-2.71%)</td><td>168.90 (+0.36%)</td><td>126.70 (-7.99%)</td><td>25.18 (-2.85%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.90 (n/a)</td><td>172.14 (n/a)</td><td>168.30 (n/a)</td><td>137.70 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 <b>(+29.99%)</b></td><td>0.08 (+8.38%)</td><td>0.07 (-4.29%)</td><td>0.07 (-3.65%)</td><td>0.01 <b>(+414.77%)</b></td><td>232.60 (+3.79%)</td><td>200.92 (-5.70%)</td><td>218.50 (+4.45%)</td><td>158.70 <b>(-23.07%)</b></td><td>32.68 <b>(+312.54%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>224.10 (n/a)</td><td>213.06 (n/a)</td><td>209.20 (n/a)</td><td>206.30 (n/a)</td><td>7.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (+0.43%)</td><td>0.08 (+9.83%)</td><td>0.08 (+13.28%)</td><td>0.07 <b>(+21.09%)</b></td><td>0.01 <b>(-20.28%)</b></td><td>240.70 (-17.43%)</td><td>207.76 (-10.05%)</td><td>194.50 (-11.71%)</td><td>175.70 (-0.40%)</td><td>28.29 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>291.50 (n/a)</td><td>230.98 (n/a)</td><td>220.30 (n/a)</td><td>176.40 (n/a)</td><td>42.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (+13.38%)</td><td>0.11 (+10.18%)</td><td>0.11 (+16.29%)</td><td>0.08 (-6.01%)</td><td>0.02 <b>(+31.86%)</b></td><td>208.90 (+6.36%)</td><td>158.38 (-7.97%)</td><td>154.30 (-14.04%)</td><td>113.10 (-11.85%)</td><td>34.09 <b>(+23.48%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.40 (n/a)</td><td>172.10 (n/a)</td><td>179.50 (n/a)</td><td>128.30 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (-4.66%)</td><td>0.11 (-0.84%)</td><td>0.11 (-9.19%)</td><td>0.09 (+0.49%)</td><td>0.01 <b>(-31.64%)</b></td><td>192.00 (-0.47%)</td><td>154.74 (-0.96%)</td><td>153.60 (+10.11%)</td><td>129.10 (+4.87%)</td><td>23.11 <b>(-30.00%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>192.90 (n/a)</td><td>156.24 (n/a)</td><td>139.50 (n/a)</td><td>123.10 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (-10.27%)</td><td>0.11 (+14.74%)</td><td>0.11 <b>(+30.28%)</b></td><td>0.09 <b>(+64.22%)</b></td><td>0.02 <b>(-48.01%)</b></td><td>186.30 <b>(-39.10%)</b></td><td>156.74 (-19.97%)</td><td>146.60 <b>(-23.29%)</b></td><td>124.70 (+11.44%)</td><td>26.15 <b>(-63.58%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>305.90 (n/a)</td><td>195.86 (n/a)</td><td>191.10 (n/a)</td><td>111.90 (n/a)</td><td>71.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (+15.85%)</td><td>0.13 <b>(+21.16%)</b></td><td>0.14 <b>(+35.75%)</b></td><td>0.10 (+11.25%)</td><td>0.02 <b>(+52.91%)</b></td><td>159.40 (-10.10%)</td><td>131.06 (-16.42%)</td><td>119.50 <b>(-26.33%)</b></td><td>108.20 (-13.65%)</td><td>24.55 <b>(+23.07%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.30 (n/a)</td><td>156.80 (n/a)</td><td>162.20 (n/a)</td><td>125.30 (n/a)</td><td>19.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 <b>(-22.61%)</b></td><td>0.10 (-7.19%)</td><td>0.11 <b>(+20.52%)</b></td><td>0.07 (-19.77%)</td><td>0.02 <b>(-36.07%)</b></td><td>241.80 <b>(+24.64%)</b></td><td>171.48 (+5.89%)</td><td>154.60 (-17.02%)</td><td>138.80 <b>(+29.24%)</b></td><td>40.63 (+5.44%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>194.00 (n/a)</td><td>161.94 (n/a)</td><td>186.30 (n/a)</td><td>107.40 (n/a)</td><td>38.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (-6.88%)</td><td>0.10 (-1.13%)</td><td>0.11 (+10.72%)</td><td>0.07 (-14.42%)</td><td>0.02 (+0.62%)</td><td>234.40 (+16.85%)</td><td>168.08 (+2.24%)</td><td>155.10 (-9.67%)</td><td>126.00 (+7.33%)</td><td>41.20 <b>(+34.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.60 (n/a)</td><td>164.40 (n/a)</td><td>171.70 (n/a)</td><td>117.40 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (-1.69%)</td><td>0.10 (-5.99%)</td><td>0.10 (-9.59%)</td><td>0.07 (-12.32%)</td><td>0.03 (+8.40%)</td><td>226.20 (+14.07%)</td><td>168.62 (+7.70%)</td><td>168.20 (+10.59%)</td><td>112.60 (+1.72%)</td><td>41.12 <b>(+24.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.30 (n/a)</td><td>156.56 (n/a)</td><td>152.10 (n/a)</td><td>110.70 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (-0.49%)</td><td>0.10 (-0.14%)</td><td>0.10 (-1.32%)</td><td>0.07 (-2.00%)</td><td>0.02 (-4.98%)</td><td>226.00 (+2.03%)</td><td>172.50 (+0.03%)</td><td>165.30 (+1.35%)</td><td>146.10 (+0.48%)</td><td>31.27 (+0.62%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.50 (n/a)</td><td>172.44 (n/a)</td><td>163.10 (n/a)</td><td>145.40 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (+15.28%)</td><td>0.11 <b>(+24.15%)</b></td><td>0.11 <b>(+23.37%)</b></td><td>0.08 <b>(+20.75%)</b></td><td>0.02 (+13.49%)</td><td>201.60 (-17.21%)</td><td>152.86 (-19.79%)</td><td>155.00 (-18.93%)</td><td>119.40 (-13.29%)</td><td>33.68 <b>(-20.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.50 (n/a)</td><td>190.58 (n/a)</td><td>191.20 (n/a)</td><td>137.70 (n/a)</td><td>42.44 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (+7.27%)</td><td>0.09 (-7.42%)</td><td>0.08 <b>(-21.96%)</b></td><td>0.07 (-1.09%)</td><td>0.02 (+16.50%)</td><td>223.10 (+1.09%)</td><td>182.96 (+9.05%)</td><td>201.90 <b>(+28.11%)</b></td><td>127.70 (-6.79%)</td><td>39.45 (+11.29%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.70 (n/a)</td><td>167.78 (n/a)</td><td>157.60 (n/a)</td><td>137.00 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (+5.68%)</td><td>0.10 (+6.29%)</td><td>0.10 (+8.56%)</td><td>0.08 (+9.69%)</td><td>0.02 (-1.35%)</td><td>210.00 (-8.85%)</td><td>165.40 (-6.34%)</td><td>156.90 (-7.87%)</td><td>131.50 (-5.33%)</td><td>29.45 (-15.10%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.40 (n/a)</td><td>176.60 (n/a)</td><td>170.30 (n/a)</td><td>138.90 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (+17.23%)</td><td>0.10 (+12.28%)</td><td>0.10 (+7.61%)</td><td>0.07 (-10.45%)</td><td>0.03 <b>(+95.89%)</b></td><td>232.30 (+11.68%)</td><td>165.12 (-7.41%)</td><td>168.10 (-7.08%)</td><td>123.10 (-14.69%)</td><td>44.44 <b>(+81.70%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>178.34 (n/a)</td><td>180.90 (n/a)</td><td>144.30 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (-8.71%)</td><td>0.19 (+7.53%)</td><td>0.21 (+19.56%)</td><td>0.14 (+3.58%)</td><td>0.03 (-19.70%)</td><td>229.60 (-3.49%)</td><td>172.64 (-8.04%)</td><td>154.90 (-16.36%)</td><td>149.60 (+9.52%)</td><td>33.55 (-14.55%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.90 (n/a)</td><td>187.74 (n/a)</td><td>185.20 (n/a)</td><td>136.60 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (-4.28%)</td><td>0.21 (+8.89%)</td><td>0.19 (+3.28%)</td><td>0.16 (+14.19%)</td><td>0.04 (-18.24%)</td><td>201.10 (-12.41%)</td><td>163.26 (-9.65%)</td><td>170.50 (-3.18%)</td><td>127.00 (+4.44%)</td><td>30.27 <b>(-23.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>229.60 (n/a)</td><td>180.70 (n/a)</td><td>176.10 (n/a)</td><td>121.60 (n/a)</td><td>39.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (-15.09%)</td><td>0.16 (-0.58%)</td><td>0.16 (+6.45%)</td><td>0.14 (+18.93%)</td><td>0.01 <b>(-58.92%)</b></td><td>236.00 (-15.92%)</td><td>210.84 (-2.25%)</td><td>204.30 (-6.07%)</td><td>188.50 (+17.81%)</td><td>18.38 <b>(-59.02%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>280.70 (n/a)</td><td>215.70 (n/a)</td><td>217.50 (n/a)</td><td>160.00 (n/a)</td><td>44.84 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 <b>(+44.77%)</b></td><td>0.18 (+12.32%)</td><td>0.16 (+3.66%)</td><td>0.14 (+3.71%)</td><td>0.05 <b>(+181.84%)</b></td><td>229.90 (-3.57%)</td><td>193.66 (-7.57%)</td><td>209.70 (-3.50%)</td><td>125.10 <b>(-30.92%)</b></td><td>40.79 <b>(+81.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>238.40 (n/a)</td><td>209.52 (n/a)</td><td>217.30 (n/a)</td><td>181.10 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (-1.51%)</td><td>0.20 (+16.29%)</td><td>0.20 (+13.03%)</td><td>0.18 <b>(+67.01%)</b></td><td>0.02 <b>(-60.78%)</b></td><td>177.40 <b>(-40.13%)</b></td><td>161.10 (-19.51%)</td><td>167.00 (-11.55%)</td><td>141.80 (+1.50%)</td><td>15.14 <b>(-76.04%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>296.30 (n/a)</td><td>200.16 (n/a)</td><td>188.80 (n/a)</td><td>139.70 (n/a)</td><td>63.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (+4.58%)</td><td>0.17 (-13.77%)</td><td>0.17 (-19.81%)</td><td>0.12 <b>(-30.32%)</b></td><td>0.04 <b>(+107.11%)</b></td><td>271.20 <b>(+43.49%)</b></td><td>197.20 <b>(+20.63%)</b></td><td>194.70 <b>(+24.73%)</b></td><td>138.50 (-4.35%)</td><td>48.77 <b>(+182.66%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>189.00 (n/a)</td><td>163.48 (n/a)</td><td>156.10 (n/a)</td><td>144.80 (n/a)</td><td>17.26 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 <b>(-20.90%)</b></td><td>0.18 (-11.81%)</td><td>0.17 (-6.43%)</td><td>0.15 (-4.08%)</td><td>0.02 <b>(-59.72%)</b></td><td>214.40 (+4.28%)</td><td>187.54 (+10.97%)</td><td>188.00 (+6.82%)</td><td>170.40 <b>(+26.41%)</b></td><td>16.89 <b>(-45.24%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.60 (n/a)</td><td>169.00 (n/a)</td><td>176.00 (n/a)</td><td>134.80 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (-17.74%)</td><td>0.15 (-19.32%)</td><td>0.17 (-11.63%)</td><td>0.10 <b>(-36.19%)</b></td><td>0.04 (+14.84%)</td><td>343.60 <b>(+56.68%)</b></td><td>230.46 <b>(+28.42%)</b></td><td>197.20 (+13.14%)</td><td>175.90 <b>(+21.56%)</b></td><td>68.99 <b>(+119.94%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.30 (n/a)</td><td>179.46 (n/a)</td><td>174.30 (n/a)</td><td>144.70 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (-4.02%)</td><td>0.17 (-5.32%)</td><td>0.17 (-3.00%)</td><td>0.14 (-12.78%)</td><td>0.02 (+12.28%)</td><td>237.20 (+14.64%)</td><td>201.40 (+6.18%)</td><td>197.30 (+3.14%)</td><td>162.80 (+4.23%)</td><td>27.53 <b>(+33.51%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>189.68 (n/a)</td><td>191.30 (n/a)</td><td>156.20 (n/a)</td><td>20.62 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (-2.03%)</td><td>0.18 (-2.77%)</td><td>0.17 (-5.55%)</td><td>0.13 (-9.88%)</td><td>0.04 <b>(+33.25%)</b></td><td>243.50 (+10.98%)</td><td>189.32 (+4.65%)</td><td>193.10 (+5.87%)</td><td>147.30 (+2.08%)</td><td>39.91 <b>(+47.93%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.40 (n/a)</td><td>180.90 (n/a)</td><td>182.40 (n/a)</td><td>144.30 (n/a)</td><td>26.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (-16.60%)</td><td>0.18 (-14.88%)</td><td>0.18 (-14.91%)</td><td>0.15 (-11.18%)</td><td>0.02 <b>(-33.26%)</b></td><td>215.00 (+12.57%)</td><td>179.64 (+16.57%)</td><td>180.90 (+17.54%)</td><td>154.90 (+19.89%)</td><td>22.89 (-8.34%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.00 (n/a)</td><td>154.10 (n/a)</td><td>153.90 (n/a)</td><td>129.20 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (+6.51%)</td><td>0.19 (-9.94%)</td><td>0.17 (-15.50%)</td><td>0.14 <b>(-23.49%)</b></td><td>0.05 <b>(+83.13%)</b></td><td>229.50 <b>(+30.69%)</b></td><td>184.18 (+15.16%)</td><td>195.80 (+18.38%)</td><td>120.40 (-6.08%)</td><td>41.06 <b>(+121.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>175.60 (n/a)</td><td>159.94 (n/a)</td><td>165.40 (n/a)</td><td>128.20 (n/a)</td><td>18.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (+13.62%)</td><td>0.20 (+2.12%)</td><td>0.18 (-4.02%)</td><td>0.15 (-7.01%)</td><td>0.06 <b>(+70.13%)</b></td><td>222.20 (+7.55%)</td><td>176.16 (+2.07%)</td><td>181.60 (+4.19%)</td><td>114.60 (-11.98%)</td><td>46.75 <b>(+70.91%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>206.60 (n/a)</td><td>172.58 (n/a)</td><td>174.30 (n/a)</td><td>130.20 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (-1.30%)</td><td>0.18 (-0.21%)</td><td>0.19 (+1.01%)</td><td>0.16 (+6.79%)</td><td>0.02 <b>(-25.01%)</b></td><td>200.10 (-6.36%)</td><td>181.52 (-0.37%)</td><td>175.20 (-0.96%)</td><td>162.00 (+1.31%)</td><td>17.23 <b>(-26.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.70 (n/a)</td><td>182.20 (n/a)</td><td>176.90 (n/a)</td><td>159.90 (n/a)</td><td>23.48 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (+6.61%)</td><td>0.19 (+11.97%)</td><td>0.20 (+14.13%)</td><td>0.16 (+19.76%)</td><td>0.02 (-10.11%)</td><td>202.10 (-16.49%)</td><td>174.76 (-11.18%)</td><td>165.30 (-12.40%)</td><td>158.50 (-6.21%)</td><td>18.89 <b>(-31.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>242.00 (n/a)</td><td>196.76 (n/a)</td><td>188.70 (n/a)</td><td>169.00 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 <b>(+24.17%)</b></td><td>0.19 (+12.05%)</td><td>0.19 (+10.74%)</td><td>0.09 <b>(-34.03%)</b></td><td>0.07 <b>(+155.82%)</b></td><td>368.20 <b>(+51.59%)</b></td><td>197.40 (+2.38%)</td><td>173.00 (-9.71%)</td><td>122.30 (-19.43%)</td><td>100.85 <b>(+206.74%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>242.90 (n/a)</td><td>192.82 (n/a)</td><td>191.60 (n/a)</td><td>151.80 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (+0.19%)</td><td>0.18 (+0.23%)</td><td>0.18 (+0.26%)</td><td>0.18 (+0.29%)</td><td>0.00 <b>(-26.12%)</b></td><td>47426.10 (-0.29%)</td><td>47354.50 (-0.23%)</td><td>47350.10 (-0.26%)</td><td>47307.50 (-0.19%)</td><td>48.34 <b>(-26.47%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47565.20 (n/a)</td><td>47465.40 (n/a)</td><td>47471.70 (n/a)</td><td>47398.70 (n/a)</td><td>65.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (-0.10%)</td><td>0.18 (-0.10%)</td><td>0.18 (-0.04%)</td><td>0.18 (+0.04%)</td><td>0.00 <b>(-23.28%)</b></td><td>47497.70 (-0.04%)</td><td>47416.16 (+0.10%)</td><td>47409.30 (+0.04%)</td><td>47306.70 (+0.10%)</td><td>76.78 <b>(-23.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47515.10 (n/a)</td><td>47371.04 (n/a)</td><td>47388.30 (n/a)</td><td>47257.30 (n/a)</td><td>100.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (+0.00%)</td><td>0.11 (+0.01%)</td><td>0.11 (+0.03%)</td><td>0.11 (+0.01%)</td><td>0.00 (-19.32%)</td><td>374415.60 (-0.01%)</td><td>374286.66 (-0.01%)</td><td>374313.90 (-0.03%)</td><td>374076.40 (-0.00%)</td><td>128.22 (-19.33%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374457.20 (n/a)</td><td>374339.90 (n/a)</td><td>374437.90 (n/a)</td><td>374092.40 (n/a)</td><td>158.94 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-3.65%)</td><td>0.02 (-8.66%)</td><td>0.03 (-10.90%)</td><td>0.02 (-15.62%)</td><td>0.00 (+19.76%)</td><td>210.80 (+18.49%)</td><td>170.38 (+10.26%)</td><td>163.40 (+12.23%)</td><td>146.30 (+3.76%)</td><td>25.37 <b>(+50.32%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.90 (n/a)</td><td>154.52 (n/a)</td><td>145.60 (n/a)</td><td>141.00 (n/a)</td><td>16.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 <b>(+25.45%)</b></td><td>0.04 (+18.43%)</td><td>0.04 (+0.41%)</td><td>0.03 <b>(+35.07%)</b></td><td>0.01 (-8.85%)</td><td>213.00 <b>(-25.94%)</b></td><td>164.30 (-17.67%)</td><td>164.40 (-0.42%)</td><td>128.60 <b>(-20.32%)</b></td><td>30.94 <b>(-43.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>287.60 (n/a)</td><td>199.56 (n/a)</td><td>165.10 (n/a)</td><td>161.40 (n/a)</td><td>55.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-3.74%)</td><td>0.03 (-1.16%)</td><td>0.03 (-15.79%)</td><td>0.02 <b>(+87.19%)</b></td><td>0.00 <b>(-57.76%)</b></td><td>182.60 <b>(-46.59%)</b></td><td>157.34 (-11.38%)</td><td>159.40 (+18.78%)</td><td>126.30 (+3.87%)</td><td>20.90 <b>(-77.62%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>341.90 (n/a)</td><td>177.54 (n/a)</td><td>134.20 (n/a)</td><td>121.60 (n/a)</td><td>93.40 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 <b>(+39.01%)</b></td><td>0.04 <b>(+21.38%)</b></td><td>0.03 (+3.72%)</td><td>0.03 <b>(+23.42%)</b></td><td>0.01 <b>(+107.12%)</b></td><td>174.30 (-18.97%)</td><td>145.80 (-16.05%)</td><td>158.50 (-3.59%)</td><td>110.50 <b>(-28.11%)</b></td><td>28.21 (+17.11%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.10 (n/a)</td><td>173.68 (n/a)</td><td>164.40 (n/a)</td><td>153.70 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (-13.37%)</td><td>0.02 (-10.16%)</td><td>0.02 (-12.93%)</td><td>0.02 (+2.31%)</td><td>0.00 <b>(-57.49%)</b></td><td>205.60 (-2.28%)</td><td>187.40 (+10.18%)</td><td>184.90 (+14.84%)</td><td>176.60 (+15.42%)</td><td>10.94 <b>(-52.65%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.40 (n/a)</td><td>170.08 (n/a)</td><td>161.00 (n/a)</td><td>153.00 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+6.79%)</td><td>0.03 (+1.48%)</td><td>0.03 (-1.22%)</td><td>0.02 (-5.11%)</td><td>0.00 <b>(+44.20%)</b></td><td>210.70 (+5.40%)</td><td>171.70 (-0.63%)</td><td>165.50 (+1.22%)</td><td>148.80 (-6.36%)</td><td>25.58 <b>(+42.60%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>172.78 (n/a)</td><td>163.50 (n/a)</td><td>158.90 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (-7.89%)</td><td>0.02 (-18.94%)</td><td>0.02 (-13.48%)</td><td>0.01 <b>(-41.64%)</b></td><td>0.01 <b>(+108.00%)</b></td><td>276.60 <b>(+71.38%)</b></td><td>188.78 <b>(+30.37%)</b></td><td>166.30 (+15.57%)</td><td>138.70 (+8.53%)</td><td>56.70 <b>(+286.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>161.40 (n/a)</td><td>144.80 (n/a)</td><td>143.90 (n/a)</td><td>127.80 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (+6.15%)</td><td>0.03 (-13.29%)</td><td>0.03 <b>(-20.73%)</b></td><td>0.02 <b>(-27.18%)</b></td><td>0.01 <b>(+93.82%)</b></td><td>234.60 <b>(+37.35%)</b></td><td>170.86 (+19.37%)</td><td>171.60 <b>(+26.18%)</b></td><td>123.50 (-5.80%)</td><td>40.99 <b>(+151.32%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>170.80 (n/a)</td><td>143.14 (n/a)</td><td>136.00 (n/a)</td><td>131.10 (n/a)</td><td>16.31 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 <b>(-25.85%)</b></td><td>0.02 (-11.85%)</td><td>0.02 (+2.58%)</td><td>0.02 (+1.34%)</td><td>0.00 <b>(-69.78%)</b></td><td>199.80 (-1.33%)</td><td>171.12 (+8.56%)</td><td>167.10 (-2.51%)</td><td>157.10 <b>(+34.85%)</b></td><td>16.55 <b>(-56.83%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>157.62 (n/a)</td><td>171.40 (n/a)</td><td>116.50 (n/a)</td><td>38.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (+18.28%)</td><td>0.03 (+14.16%)</td><td>0.03 (+16.62%)</td><td>0.02 (-11.45%)</td><td>0.01 <b>(+82.03%)</b></td><td>235.30 (+12.96%)</td><td>170.58 (-10.11%)</td><td>164.90 (-14.25%)</td><td>129.90 (-15.48%)</td><td>39.19 <b>(+83.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.30 (n/a)</td><td>189.76 (n/a)</td><td>192.30 (n/a)</td><td>153.70 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+11.56%)</td><td>0.02 (-11.75%)</td><td>0.02 (-18.16%)</td><td>0.02 (-18.76%)</td><td>0.01 <b>(+106.22%)</b></td><td>238.00 <b>(+23.12%)</b></td><td>199.46 (+16.79%)</td><td>199.60 <b>(+22.23%)</b></td><td>136.40 (-10.38%)</td><td>40.12 <b>(+122.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.30 (n/a)</td><td>170.78 (n/a)</td><td>163.30 (n/a)</td><td>152.20 (n/a)</td><td>18.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (+19.90%)</td><td>0.02 (+5.47%)</td><td>0.02 (-2.49%)</td><td>0.02 (-4.01%)</td><td>0.01 <b>(+104.35%)</b></td><td>221.60 (+4.18%)</td><td>190.16 (-2.61%)</td><td>210.40 (+2.53%)</td><td>134.30 (-16.58%)</td><td>37.73 <b>(+81.67%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.70 (n/a)</td><td>195.26 (n/a)</td><td>205.20 (n/a)</td><td>161.00 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 <b>(-31.24%)</b></td><td>0.02 (-10.38%)</td><td>0.02 (-4.12%)</td><td>0.02 (+4.34%)</td><td>0.00 <b>(-70.88%)</b></td><td>220.30 (-4.18%)</td><td>197.96 (+6.90%)</td><td>200.60 (+4.32%)</td><td>173.90 <b>(+45.40%)</b></td><td>17.35 <b>(-57.52%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>185.18 (n/a)</td><td>192.30 (n/a)</td><td>119.60 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (-11.91%)</td><td>0.02 (+3.03%)</td><td>0.02 (+9.35%)</td><td>0.02 (+16.10%)</td><td>0.00 <b>(-62.50%)</b></td><td>208.40 (-13.88%)</td><td>197.14 (-4.74%)</td><td>201.10 (-8.55%)</td><td>180.40 (+13.53%)</td><td>12.10 <b>(-62.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.00 (n/a)</td><td>206.94 (n/a)</td><td>219.90 (n/a)</td><td>158.90 (n/a)</td><td>32.43 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (-2.96%)</td><td>0.02 (-7.22%)</td><td>0.02 (-13.13%)</td><td>0.02 (+4.71%)</td><td>0.00 (-11.47%)</td><td>257.60 (-4.49%)</td><td>225.20 (+7.27%)</td><td>227.70 (+15.12%)</td><td>185.90 (+3.05%)</td><td>30.71 (-13.68%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>269.70 (n/a)</td><td>209.94 (n/a)</td><td>197.80 (n/a)</td><td>180.40 (n/a)</td><td>35.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (-13.59%)</td><td>0.05 (-13.15%)</td><td>0.05 (-6.88%)</td><td>0.04 (-11.30%)</td><td>0.01 <b>(-25.25%)</b></td><td>203.30 (+12.76%)</td><td>175.00 (+14.30%)</td><td>175.70 (+7.40%)</td><td>135.70 (+15.78%)</td><td>25.42 (-4.21%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.30 (n/a)</td><td>153.10 (n/a)</td><td>163.60 (n/a)</td><td>117.20 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 <b>(-30.64%)</b></td><td>0.07 <b>(-21.37%)</b></td><td>0.06 <b>(-20.15%)</b></td><td>0.06 (-5.00%)</td><td>0.00 <b>(-82.91%)</b></td><td>194.10 (+5.26%)</td><td>187.68 <b>(+24.01%)</b></td><td>191.30 <b>(+25.28%)</b></td><td>176.50 <b>(+44.08%)</b></td><td>7.21 <b>(-73.52%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>184.40 (n/a)</td><td>151.34 (n/a)</td><td>152.70 (n/a)</td><td>122.50 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (-5.51%)</td><td>0.05 (+10.22%)</td><td>0.05 (+11.56%)</td><td>0.04 <b>(+47.88%)</b></td><td>0.00 <b>(-70.33%)</b></td><td>194.30 <b>(-32.37%)</b></td><td>176.36 (-13.21%)</td><td>173.00 (-10.36%)</td><td>163.80 (+5.81%)</td><td>11.25 <b>(-78.63%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>287.30 (n/a)</td><td>203.20 (n/a)</td><td>193.00 (n/a)</td><td>154.80 (n/a)</td><td>52.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 <b>(-33.39%)</b></td><td>0.04 <b>(-24.94%)</b></td><td>0.04 <b>(-22.07%)</b></td><td>0.04 <b>(-20.12%)</b></td><td>0.01 <b>(-56.18%)</b></td><td>289.40 <b>(+25.17%)</b></td><td>233.92 <b>(+30.10%)</b></td><td>230.70 <b>(+28.31%)</b></td><td>203.80 <b>(+50.18%)</b></td><td>33.14 (-15.27%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>179.80 (n/a)</td><td>179.80 (n/a)</td><td>135.70 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 <b>(-29.00%)</b></td><td>0.04 (-19.30%)</td><td>0.04 (-19.01%)</td><td>0.04 (-5.17%)</td><td>0.01 <b>(-55.87%)</b></td><td>231.80 (+5.46%)</td><td>189.58 (+18.95%)</td><td>188.80 <b>(+23.48%)</b></td><td>154.20 <b>(+40.82%)</b></td><td>28.24 <b>(-34.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>159.38 (n/a)</td><td>152.90 (n/a)</td><td>109.50 (n/a)</td><td>43.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (-11.67%)</td><td>0.06 (-5.21%)</td><td>0.05 (-0.66%)</td><td>0.05 (+7.82%)</td><td>0.01 <b>(-31.03%)</b></td><td>201.80 (-7.26%)</td><td>175.74 (+2.42%)</td><td>193.60 (+0.68%)</td><td>125.80 (+13.13%)</td><td>31.80 <b>(-26.98%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>217.60 (n/a)</td><td>171.58 (n/a)</td><td>192.30 (n/a)</td><td>111.20 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 <b>(-32.44%)</b></td><td>0.04 <b>(-21.18%)</b></td><td>0.04 (-12.12%)</td><td>0.04 <b>(-22.16%)</b></td><td>0.01 <b>(-47.57%)</b></td><td>225.70 <b>(+28.46%)</b></td><td>192.52 <b>(+25.05%)</b></td><td>184.40 (+13.83%)</td><td>160.20 <b>(+47.92%)</b></td><td>28.33 (+3.15%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>153.96 (n/a)</td><td>162.00 (n/a)</td><td>108.30 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 <b>(-24.71%)</b></td><td>0.05 (-15.76%)</td><td>0.05 (-14.71%)</td><td>0.04 (-8.50%)</td><td>0.01 <b>(-48.94%)</b></td><td>226.30 (+9.27%)</td><td>182.82 (+15.37%)</td><td>178.60 (+17.27%)</td><td>149.20 <b>(+32.86%)</b></td><td>28.06 <b>(-25.62%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>158.46 (n/a)</td><td>152.30 (n/a)</td><td>112.30 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+0.21%)</td><td>0.05 (-12.78%)</td><td>0.05 (-8.15%)</td><td>0.04 (-16.68%)</td><td>0.01 (+8.37%)</td><td>210.90 <b>(+20.03%)</b></td><td>173.48 (+15.92%)</td><td>177.10 (+8.85%)</td><td>116.70 (-0.17%)</td><td>35.96 <b>(+26.72%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>149.66 (n/a)</td><td>162.70 (n/a)</td><td>116.90 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (+5.84%)</td><td>0.06 (-2.02%)</td><td>0.05 (-12.58%)</td><td>0.05 (+8.16%)</td><td>0.01 (+3.93%)</td><td>199.30 (-7.56%)</td><td>169.50 (+1.84%)</td><td>181.30 (+14.38%)</td><td>125.20 (-5.51%)</td><td>28.85 (-11.64%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>166.44 (n/a)</td><td>158.50 (n/a)</td><td>132.50 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (+16.81%)</td><td>0.05 (+14.19%)</td><td>0.05 <b>(+21.05%)</b></td><td>0.04 (-0.76%)</td><td>0.01 <b>(+98.31%)</b></td><td>233.30 (+0.78%)</td><td>176.00 (-10.12%)</td><td>156.70 (-17.35%)</td><td>142.90 (-14.43%)</td><td>39.70 <b>(+67.52%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.50 (n/a)</td><td>195.82 (n/a)</td><td>189.60 (n/a)</td><td>167.00 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 <b>(+42.92%)</b></td><td>0.05 (+5.88%)</td><td>0.04 (-18.26%)</td><td>0.04 <b>(+38.42%)</b></td><td>0.02 <b>(+69.71%)</b></td><td>245.40 <b>(-27.74%)</b></td><td>207.76 (-2.71%)</td><td>230.90 <b>(+22.30%)</b></td><td>102.70 <b>(-30.04%)</b></td><td>59.90 <b>(-20.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>339.60 (n/a)</td><td>213.54 (n/a)</td><td>188.80 (n/a)</td><td>146.80 (n/a)</td><td>75.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (+13.58%)</td><td>0.04 (+1.50%)</td><td>0.05 (+9.95%)</td><td>0.03 <b>(-24.90%)</b></td><td>0.01 <b>(+97.29%)</b></td><td>291.00 <b>(+33.18%)</b></td><td>196.96 (+4.10%)</td><td>179.30 (-9.03%)</td><td>136.10 (-11.97%)</td><td>61.43 <b>(+135.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>189.20 (n/a)</td><td>197.10 (n/a)</td><td>154.60 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 <b>(-25.33%)</b></td><td>0.04 (-12.24%)</td><td>0.04 (-4.55%)</td><td>0.04 (-5.99%)</td><td>0.00 <b>(-78.37%)</b></td><td>217.80 (+6.35%)</td><td>207.98 (+12.30%)</td><td>209.00 (+4.76%)</td><td>197.30 <b>(+33.94%)</b></td><td>7.47 <b>(-69.43%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>185.20 (n/a)</td><td>199.50 (n/a)</td><td>147.30 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (-0.85%)</td><td>0.04 (-1.50%)</td><td>0.04 (-1.94%)</td><td>0.04 (+7.31%)</td><td>0.00 <b>(-22.32%)</b></td><td>223.30 (-6.80%)</td><td>206.20 (+0.98%)</td><td>212.80 (+1.96%)</td><td>176.60 (+0.86%)</td><td>18.41 <b>(-27.21%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.60 (n/a)</td><td>204.20 (n/a)</td><td>208.70 (n/a)</td><td>175.10 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (+14.55%)</td><td>0.11 (+3.63%)</td><td>0.10 (-1.17%)</td><td>0.09 (+2.47%)</td><td>0.02 <b>(+62.71%)</b></td><td>179.60 (-2.39%)</td><td>156.58 (-2.52%)</td><td>161.80 (+1.19%)</td><td>120.10 (-12.72%)</td><td>22.30 <b>(+35.17%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>160.62 (n/a)</td><td>159.90 (n/a)</td><td>137.60 (n/a)</td><td>16.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 <b>(+22.83%)</b></td><td>0.16 (+10.73%)</td><td>0.16 (+16.06%)</td><td>0.12 (-6.26%)</td><td>0.04 <b>(+94.76%)</b></td><td>202.20 (+6.70%)</td><td>161.70 (-7.28%)</td><td>156.00 (-13.81%)</td><td>114.60 (-18.61%)</td><td>33.69 <b>(+70.78%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.50 (n/a)</td><td>174.40 (n/a)</td><td>181.00 (n/a)</td><td>140.80 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (+4.83%)</td><td>0.10 (+2.58%)</td><td>0.10 (+1.98%)</td><td>0.08 (-6.08%)</td><td>0.02 <b>(+61.88%)</b></td><td>203.60 (+6.49%)</td><td>164.32 (-0.50%)</td><td>161.20 (-1.95%)</td><td>131.70 (-4.63%)</td><td>33.46 <b>(+61.35%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>165.14 (n/a)</td><td>164.40 (n/a)</td><td>138.10 (n/a)</td><td>20.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 <b>(+24.96%)</b></td><td>0.12 (+10.25%)</td><td>0.12 <b>(+24.89%)</b></td><td>0.08 (-5.37%)</td><td>0.03 <b>(+25.22%)</b></td><td>251.80 (+5.71%)</td><td>181.68 (-8.02%)</td><td>177.90 (-19.94%)</td><td>117.10 (-19.96%)</td><td>49.64 (+6.47%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>238.20 (n/a)</td><td>197.52 (n/a)</td><td>222.20 (n/a)</td><td>146.30 (n/a)</td><td>46.62 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (-2.79%)</td><td>0.10 (+1.90%)</td><td>0.11 (+8.19%)</td><td>0.08 (-6.76%)</td><td>0.02 (+12.51%)</td><td>201.70 (+7.29%)</td><td>163.54 (-1.30%)</td><td>155.60 (-7.60%)</td><td>138.10 (+2.91%)</td><td>25.92 <b>(+26.12%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>165.70 (n/a)</td><td>168.40 (n/a)</td><td>134.20 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (+5.89%)</td><td>0.13 (+10.63%)</td><td>0.11 (+5.20%)</td><td>0.11 <b>(+32.62%)</b></td><td>0.02 <b>(-23.81%)</b></td><td>183.50 <b>(-24.58%)</b></td><td>163.00 (-12.27%)</td><td>180.60 (-4.95%)</td><td>126.80 (-5.51%)</td><td>26.75 <b>(-43.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>243.30 (n/a)</td><td>185.80 (n/a)</td><td>190.00 (n/a)</td><td>134.20 (n/a)</td><td>47.14 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (-5.45%)</td><td>0.11 (-1.71%)</td><td>0.11 (-2.96%)</td><td>0.07 (+1.42%)</td><td>0.02 (-1.95%)</td><td>219.70 (-1.44%)</td><td>162.52 (+1.68%)</td><td>152.30 (+3.04%)</td><td>124.90 (+5.76%)</td><td>38.60 (-0.83%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.90 (n/a)</td><td>159.84 (n/a)</td><td>147.80 (n/a)</td><td>118.10 (n/a)</td><td>38.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (+6.17%)</td><td>0.11 (-2.42%)</td><td>0.09 (-15.60%)</td><td>0.09 (+10.04%)</td><td>0.03 (+6.78%)</td><td>203.50 (-9.11%)</td><td>180.90 (+2.33%)</td><td>200.60 (+18.49%)</td><td>121.50 (-5.81%)</td><td>35.09 (-10.39%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>223.90 (n/a)</td><td>176.78 (n/a)</td><td>169.30 (n/a)</td><td>129.00 (n/a)</td><td>39.15 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 <b>(-24.69%)</b></td><td>0.10 (-11.18%)</td><td>0.10 (-0.39%)</td><td>0.07 (-17.40%)</td><td>0.01 <b>(-42.63%)</b></td><td>218.80 <b>(+21.08%)</b></td><td>172.34 (+10.96%)</td><td>166.00 (+0.42%)</td><td>149.50 <b>(+32.77%)</b></td><td>27.21 (-6.38%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.70 (n/a)</td><td>155.32 (n/a)</td><td>165.30 (n/a)</td><td>112.60 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 <b>(+21.09%)</b></td><td>0.11 (+6.81%)</td><td>0.10 (+8.04%)</td><td>0.08 (+2.69%)</td><td>0.02 <b>(+30.28%)</b></td><td>220.20 (-2.61%)</td><td>178.02 (-5.57%)</td><td>175.50 (-7.49%)</td><td>123.80 (-17.41%)</td><td>35.74 (+1.50%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>226.10 (n/a)</td><td>188.52 (n/a)</td><td>189.70 (n/a)</td><td>149.90 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (-12.85%)</td><td>0.09 (-7.19%)</td><td>0.08 (-2.44%)</td><td>0.06 (-16.93%)</td><td>0.02 (-6.67%)</td><td>260.90 <b>(+20.40%)</b></td><td>195.16 (+8.48%)</td><td>193.60 (+2.49%)</td><td>149.70 (+14.71%)</td><td>43.01 <b>(+32.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.70 (n/a)</td><td>179.90 (n/a)</td><td>188.90 (n/a)</td><td>130.50 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (-12.76%)</td><td>0.09 (-4.65%)</td><td>0.09 (-1.26%)</td><td>0.08 (-2.83%)</td><td>0.01 <b>(-46.45%)</b></td><td>222.20 (+2.92%)</td><td>198.94 (+4.08%)</td><td>195.90 (+1.24%)</td><td>184.10 (+14.63%)</td><td>14.33 <b>(-36.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>191.14 (n/a)</td><td>193.50 (n/a)</td><td>160.60 (n/a)</td><td>22.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (-17.44%)</td><td>0.08 (-10.91%)</td><td>0.08 (-19.88%)</td><td>0.07 <b>(+32.28%)</b></td><td>0.01 <b>(-73.55%)</b></td><td>226.90 <b>(-24.39%)</b></td><td>206.46 (+6.01%)</td><td>204.50 <b>(+24.77%)</b></td><td>188.40 <b>(+21.08%)</b></td><td>14.76 <b>(-75.85%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>300.10 (n/a)</td><td>194.76 (n/a)</td><td>163.90 (n/a)</td><td>155.60 (n/a)</td><td>61.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (-5.44%)</td><td>0.08 (-6.25%)</td><td>0.08 (-0.03%)</td><td>0.05 <b>(-24.77%)</b></td><td>0.02 <b>(+25.71%)</b></td><td>328.70 <b>(+32.92%)</b></td><td>229.72 (+9.81%)</td><td>207.30 (+0.05%)</td><td>167.30 (+5.75%)</td><td>62.12 <b>(+84.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>247.30 (n/a)</td><td>209.20 (n/a)</td><td>207.20 (n/a)</td><td>158.20 (n/a)</td><td>33.69 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (-14.89%)</td><td>0.07 (-18.19%)</td><td>0.07 (-15.61%)</td><td>0.05 (-18.90%)</td><td>0.01 (-2.34%)</td><td>327.10 <b>(+23.34%)</b></td><td>255.52 <b>(+23.42%)</b></td><td>227.10 (+18.53%)</td><td>204.00 (+17.44%)</td><td>54.29 <b>(+43.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>265.20 (n/a)</td><td>207.04 (n/a)</td><td>191.60 (n/a)</td><td>173.70 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (-7.25%)</td><td>0.19 (+11.88%)</td><td>0.19 (+12.32%)</td><td>0.18 <b>(+29.22%)</b></td><td>0.01 <b>(-70.50%)</b></td><td>179.30 <b>(-22.62%)</b></td><td>169.52 (-12.82%)</td><td>169.40 (-10.94%)</td><td>156.60 (+7.85%)</td><td>8.34 <b>(-75.63%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.70 (n/a)</td><td>194.44 (n/a)</td><td>190.20 (n/a)</td><td>145.20 (n/a)</td><td>34.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (-7.02%)</td><td>0.22 (+15.79%)</td><td>0.21 (+7.97%)</td><td>0.19 <b>(+112.23%)</b></td><td>0.03 <b>(-58.86%)</b></td><td>169.00 <b>(-52.87%)</b></td><td>150.72 <b>(-23.38%)</b></td><td>159.60 (-7.37%)</td><td>129.00 (+7.59%)</td><td>17.70 <b>(-80.99%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>358.60 (n/a)</td><td>196.72 (n/a)</td><td>172.30 (n/a)</td><td>119.90 (n/a)</td><td>93.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (+10.66%)</td><td>0.24 (+10.65%)</td><td>0.26 (+19.03%)</td><td>0.18 (-7.19%)</td><td>0.04 <b>(+74.26%)</b></td><td>228.30 (+7.74%)</td><td>173.86 (-7.92%)</td><td>159.70 (-15.95%)</td><td>143.30 (-9.59%)</td><td>34.19 <b>(+73.99%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>211.90 (n/a)</td><td>188.82 (n/a)</td><td>190.00 (n/a)</td><td>158.50 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 <b>(-27.28%)</b></td><td>0.19 (-16.13%)</td><td>0.19 (-6.37%)</td><td>0.17 (-5.03%)</td><td>0.02 <b>(-69.11%)</b></td><td>191.20 (+5.29%)</td><td>172.54 (+15.55%)</td><td>175.90 (+6.80%)</td><td>155.20 <b>(+37.47%)</b></td><td>13.89 <b>(-54.65%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>181.60 (n/a)</td><td>149.32 (n/a)</td><td>164.70 (n/a)</td><td>112.90 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.31 (+12.89%)</td><td>0.23 (-1.64%)</td><td>0.22 (-9.98%)</td><td>0.17 (-10.42%)</td><td>0.05 <b>(+32.43%)</b></td><td>246.80 (+11.62%)</td><td>189.98 (+3.38%)</td><td>188.00 (+11.11%)</td><td>133.90 (-11.44%)</td><td>42.85 <b>(+26.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>221.10 (n/a)</td><td>183.76 (n/a)</td><td>169.20 (n/a)</td><td>151.20 (n/a)</td><td>33.84 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (-6.46%)</td><td>0.19 (-7.16%)</td><td>0.19 (-10.54%)</td><td>0.18 (+2.84%)</td><td>0.01 <b>(-38.37%)</b></td><td>181.30 (-2.74%)</td><td>173.24 (+7.26%)</td><td>176.10 (+11.81%)</td><td>156.70 (+6.89%)</td><td>10.14 <b>(-36.11%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>161.52 (n/a)</td><td>157.50 (n/a)</td><td>146.60 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.33 (+11.07%)</td><td>0.22 (+0.88%)</td><td>0.20 (-0.08%)</td><td>0.16 (+8.82%)</td><td>0.07 (-7.80%)</td><td>232.50 (-8.10%)</td><td>174.38 (-3.22%)</td><td>182.70 (+0.11%)</td><td>110.40 (-9.95%)</td><td>45.17 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>253.00 (n/a)</td><td>180.18 (n/a)</td><td>182.50 (n/a)</td><td>122.60 (n/a)</td><td>57.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (+11.03%)</td><td>0.19 (+8.82%)</td><td>0.18 (+5.91%)</td><td>0.18 (+16.92%)</td><td>0.02 (-10.67%)</td><td>184.60 (-14.46%)</td><td>171.34 (-8.46%)</td><td>178.00 (-5.57%)</td><td>147.90 (-9.93%)</td><td>15.52 <b>(-29.83%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.80 (n/a)</td><td>187.18 (n/a)</td><td>188.50 (n/a)</td><td>164.20 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (-13.35%)</td><td>0.19 (-6.74%)</td><td>0.18 (+0.03%)</td><td>0.17 (-0.26%)</td><td>0.03 <b>(-33.02%)</b></td><td>217.70 (+0.28%)</td><td>195.22 (+5.65%)</td><td>199.60 (-0.05%)</td><td>151.20 (+15.42%)</td><td>25.92 <b>(-22.36%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>217.10 (n/a)</td><td>184.78 (n/a)</td><td>199.70 (n/a)</td><td>131.00 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 <b>(+21.05%)</b></td><td>0.20 (+13.34%)</td><td>0.21 (+16.53%)</td><td>0.15 (+9.11%)</td><td>0.04 <b>(+43.97%)</b></td><td>215.40 (-8.34%)</td><td>167.62 (-10.91%)</td><td>156.40 (-14.16%)</td><td>133.00 (-17.39%)</td><td>31.59 (+9.20%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>188.14 (n/a)</td><td>182.20 (n/a)</td><td>161.00 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (+18.51%)</td><td>0.19 (+14.06%)</td><td>0.19 (+16.07%)</td><td>0.16 (+5.99%)</td><td>0.02 <b>(+68.96%)</b></td><td>213.60 (-5.65%)</td><td>186.08 (-12.02%)</td><td>181.00 (-13.81%)</td><td>168.20 (-15.65%)</td><td>17.07 <b>(+37.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>211.50 (n/a)</td><td>210.00 (n/a)</td><td>199.40 (n/a)</td><td>12.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (+10.01%)</td><td>0.18 (+12.25%)</td><td>0.18 (+9.16%)</td><td>0.11 (+6.83%)</td><td>0.05 (+13.27%)</td><td>300.50 (-6.39%)</td><td>193.26 (-10.29%)</td><td>186.20 (-8.37%)</td><td>131.00 (-9.09%)</td><td>65.31 (-2.78%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>321.00 (n/a)</td><td>215.42 (n/a)</td><td>203.20 (n/a)</td><td>144.10 (n/a)</td><td>67.18 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (+14.77%)</td><td>0.18 (+2.42%)</td><td>0.18 (+3.06%)</td><td>0.15 (-1.40%)</td><td>0.03 <b>(+77.87%)</b></td><td>235.50 (+1.42%)</td><td>196.52 (-0.75%)</td><td>191.80 (-2.94%)</td><td>150.40 (-12.86%)</td><td>34.26 <b>(+56.91%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>232.20 (n/a)</td><td>198.00 (n/a)</td><td>197.60 (n/a)</td><td>172.60 (n/a)</td><td>21.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (+9.35%)</td><td>0.17 (+17.37%)</td><td>0.17 (+14.53%)</td><td>0.15 <b>(+24.96%)</b></td><td>0.01 (-17.86%)</td><td>212.30 (-19.98%)</td><td>191.68 (-15.28%)</td><td>195.30 (-12.70%)</td><td>174.40 (-8.55%)</td><td>15.84 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>265.30 (n/a)</td><td>226.26 (n/a)</td><td>223.70 (n/a)</td><td>190.70 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (-15.50%)</td><td>0.10 (-4.28%)</td><td>0.11 (+5.80%)</td><td>0.09 (-6.67%)</td><td>0.01 <b>(-36.09%)</b></td><td>232.80 (+7.13%)</td><td>198.20 (+3.44%)</td><td>188.30 (-5.52%)</td><td>178.10 (+18.34%)</td><td>23.11 <b>(-20.56%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>191.60 (n/a)</td><td>199.30 (n/a)</td><td>150.50 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (+3.72%)</td><td>0.12 (-2.85%)</td><td>0.12 (+0.16%)</td><td>0.10 (-4.33%)</td><td>0.02 <b>(+20.91%)</b></td><td>214.20 (+4.54%)</td><td>180.16 (+3.62%)</td><td>177.90 (-0.17%)</td><td>141.30 (-3.55%)</td><td>28.17 <b>(+22.51%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.90 (n/a)</td><td>173.86 (n/a)</td><td>178.20 (n/a)</td><td>146.50 (n/a)</td><td>22.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (+2.23%)</td><td>0.13 (+3.05%)</td><td>0.13 (+13.96%)</td><td>0.10 (-11.81%)</td><td>0.03 (+6.95%)</td><td>209.90 (+13.40%)</td><td>158.70 (-2.30%)</td><td>156.00 (-12.26%)</td><td>115.30 (-2.12%)</td><td>34.36 (+16.46%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>185.10 (n/a)</td><td>162.44 (n/a)</td><td>177.80 (n/a)</td><td>117.80 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (+5.55%)</td><td>0.13 (+8.46%)</td><td>0.13 (+10.02%)</td><td>0.11 (+6.20%)</td><td>0.02 (-3.31%)</td><td>180.90 (-5.88%)</td><td>158.20 (-8.09%)</td><td>163.70 (-9.11%)</td><td>128.60 (-5.30%)</td><td>20.19 (-15.19%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>192.20 (n/a)</td><td>172.12 (n/a)</td><td>180.10 (n/a)</td><td>135.80 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 <b>(+31.56%)</b></td><td>0.12 <b>(+25.27%)</b></td><td>0.13 <b>(+44.82%)</b></td><td>0.08 (+4.59%)</td><td>0.03 <b>(+62.42%)</b></td><td>266.30 (-4.38%)</td><td>180.50 (-17.70%)</td><td>156.00 <b>(-30.97%)</b></td><td>133.80 <b>(-24.02%)</b></td><td>54.13 <b>(+24.33%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>278.50 (n/a)</td><td>219.32 (n/a)</td><td>226.00 (n/a)</td><td>176.10 (n/a)</td><td>43.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (-3.39%)</td><td>0.12 (-0.74%)</td><td>0.12 (+3.55%)</td><td>0.11 (-1.65%)</td><td>0.01 (-15.73%)</td><td>192.70 (+1.69%)</td><td>170.56 (+0.59%)</td><td>168.10 (-3.45%)</td><td>154.40 (+3.55%)</td><td>14.16 (-10.03%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>169.56 (n/a)</td><td>174.10 (n/a)</td><td>149.10 (n/a)</td><td>15.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 <b>(-22.66%)</b></td><td>0.11 (-6.72%)</td><td>0.11 (-6.07%)</td><td>0.10 <b>(+55.55%)</b></td><td>0.01 <b>(-76.59%)</b></td><td>211.00 <b>(-35.71%)</b></td><td>194.38 (-1.48%)</td><td>190.90 (+6.47%)</td><td>178.60 <b>(+29.23%)</b></td><td>13.99 <b>(-81.49%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>328.20 (n/a)</td><td>197.30 (n/a)</td><td>179.30 (n/a)</td><td>138.20 (n/a)</td><td>75.56 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (-11.03%)</td><td>0.10 (-6.06%)</td><td>0.10 (-1.08%)</td><td>0.10 (-0.26%)</td><td>0.01 <b>(-54.06%)</b></td><td>214.70 (+0.23%)</td><td>196.14 (+5.12%)</td><td>196.40 (+1.13%)</td><td>177.00 (+12.38%)</td><td>13.79 <b>(-47.51%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>186.58 (n/a)</td><td>194.20 (n/a)</td><td>157.50 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 <b>(-22.24%)</b></td><td>0.14 (-4.73%)</td><td>0.14 (+1.40%)</td><td>0.12 <b>(+32.57%)</b></td><td>0.01 <b>(-73.57%)</b></td><td>199.50 <b>(-24.57%)</b></td><td>179.42 (-0.72%)</td><td>175.80 (-1.40%)</td><td>164.30 <b>(+28.56%)</b></td><td>13.24 <b>(-74.63%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>264.50 (n/a)</td><td>180.72 (n/a)</td><td>178.30 (n/a)</td><td>127.80 (n/a)</td><td>52.18 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (-12.35%)</td><td>0.15 (-0.89%)</td><td>0.15 (+4.22%)</td><td>0.13 (+6.21%)</td><td>0.01 <b>(-55.55%)</b></td><td>182.50 (-5.88%)</td><td>166.16 (-0.49%)</td><td>167.30 (-4.07%)</td><td>150.80 (+14.07%)</td><td>11.51 <b>(-51.63%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>193.90 (n/a)</td><td>166.98 (n/a)</td><td>174.40 (n/a)</td><td>132.20 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 <b>(+25.40%)</b></td><td>0.18 <b>(+21.87%)</b></td><td>0.16 (+16.05%)</td><td>0.16 <b>(+24.94%)</b></td><td>0.02 <b>(+39.61%)</b></td><td>156.20 (-19.94%)</td><td>141.26 (-17.69%)</td><td>153.60 (-13.85%)</td><td>119.90 <b>(-20.23%)</b></td><td>18.23 (-8.70%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>171.62 (n/a)</td><td>178.30 (n/a)</td><td>150.30 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (-6.15%)</td><td>0.16 (+3.16%)</td><td>0.14 (+7.18%)</td><td>0.12 (+12.89%)</td><td>0.04 (-15.42%)</td><td>206.80 (-11.40%)</td><td>160.48 (-5.38%)</td><td>175.70 (-6.69%)</td><td>118.30 (+6.58%)</td><td>39.23 <b>(-21.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>233.40 (n/a)</td><td>169.60 (n/a)</td><td>188.30 (n/a)</td><td>111.00 (n/a)</td><td>50.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (-1.16%)</td><td>0.14 (+8.60%)</td><td>0.13 (+13.05%)</td><td>0.12 <b>(+42.22%)</b></td><td>0.02 <b>(-56.08%)</b></td><td>202.40 <b>(-29.70%)</b></td><td>179.50 (-12.75%)</td><td>182.40 (-11.54%)</td><td>150.70 (+1.14%)</td><td>18.68 <b>(-67.91%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>287.90 (n/a)</td><td>205.74 (n/a)</td><td>206.20 (n/a)</td><td>149.00 (n/a)</td><td>58.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 <b>(-28.81%)</b></td><td>0.14 (-18.76%)</td><td>0.14 (-16.69%)</td><td>0.13 (-6.89%)</td><td>0.01 <b>(-71.04%)</b></td><td>184.90 (+7.44%)</td><td>174.72 <b>(+20.66%)</b></td><td>177.20 <b>(+20.05%)</b></td><td>157.90 <b>(+40.48%)</b></td><td>10.32 <b>(-56.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>172.10 (n/a)</td><td>144.80 (n/a)</td><td>147.60 (n/a)</td><td>112.40 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 <b>(+21.22%)</b></td><td>0.13 (-1.44%)</td><td>0.12 (-9.73%)</td><td>0.12 (-5.19%)</td><td>0.03 <b>(+119.03%)</b></td><td>210.50 (+5.51%)</td><td>189.38 (+3.90%)</td><td>209.90 (+10.77%)</td><td>133.30 (-17.46%)</td><td>33.47 <b>(+92.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>182.28 (n/a)</td><td>189.50 (n/a)</td><td>161.50 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (+0.48%)</td><td>0.13 (-7.85%)</td><td>0.12 (-18.68%)</td><td>0.12 (-3.20%)</td><td>0.02 <b>(+28.38%)</b></td><td>213.20 (+3.29%)</td><td>190.68 (+9.46%)</td><td>206.50 <b>(+22.99%)</b></td><td>147.70 (-0.47%)</td><td>29.09 <b>(+33.12%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>206.40 (n/a)</td><td>174.20 (n/a)</td><td>167.90 (n/a)</td><td>148.40 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 <b>(+24.34%)</b></td><td>0.11 (+7.02%)</td><td>0.10 (-1.44%)</td><td>0.09 (+0.57%)</td><td>0.02 <b>(+95.10%)</b></td><td>207.30 (-0.58%)</td><td>178.84 (-5.16%)</td><td>183.70 (+1.49%)</td><td>132.80 (-19.56%)</td><td>27.77 <b>(+46.61%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>188.58 (n/a)</td><td>181.00 (n/a)</td><td>165.10 (n/a)</td><td>18.94 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 <b>(+28.42%)</b></td><td>0.11 (+16.62%)</td><td>0.11 (+17.92%)</td><td>0.10 (+13.09%)</td><td>0.01 <b>(+65.79%)</b></td><td>191.00 (-11.57%)</td><td>171.40 (-13.70%)</td><td>174.50 (-15.21%)</td><td>137.40 <b>(-22.11%)</b></td><td>21.06 (+12.65%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>198.62 (n/a)</td><td>205.80 (n/a)</td><td>176.40 (n/a)</td><td>18.69 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (-10.94%)</td><td>0.12 (+0.20%)</td><td>0.11 (+4.10%)</td><td>0.10 <b>(+35.22%)</b></td><td>0.02 <b>(-53.32%)</b></td><td>185.20 <b>(-26.07%)</b></td><td>160.62 (-5.77%)</td><td>165.40 (-3.89%)</td><td>131.50 (+12.30%)</td><td>20.30 <b>(-61.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>250.50 (n/a)</td><td>170.46 (n/a)</td><td>172.10 (n/a)</td><td>117.10 (n/a)</td><td>52.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 <b>(+31.70%)</b></td><td>0.12 (+14.07%)</td><td>0.12 (+6.38%)</td><td>0.08 <b>(+37.40%)</b></td><td>0.03 (+11.19%)</td><td>219.90 <b>(-27.21%)</b></td><td>165.14 (-14.10%)</td><td>156.70 (-5.94%)</td><td>120.00 <b>(-24.05%)</b></td><td>36.64 <b>(-40.46%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>302.10 (n/a)</td><td>192.24 (n/a)</td><td>166.60 (n/a)</td><td>158.00 (n/a)</td><td>61.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (-2.61%)</td><td>0.10 (-1.42%)</td><td>0.10 (-3.58%)</td><td>0.07 <b>(-23.84%)</b></td><td>0.03 <b>(+21.71%)</b></td><td>271.30 <b>(+31.32%)</b></td><td>188.86 (+4.71%)</td><td>191.40 (+3.68%)</td><td>128.40 (+2.64%)</td><td>54.75 <b>(+67.89%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>180.36 (n/a)</td><td>184.60 (n/a)</td><td>125.10 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (+18.55%)</td><td>0.12 (+8.00%)</td><td>0.11 (+6.50%)</td><td>0.09 (+1.19%)</td><td>0.03 <b>(+46.56%)</b></td><td>202.20 (-1.17%)</td><td>166.06 (-5.68%)</td><td>174.20 (-6.09%)</td><td>109.40 (-15.65%)</td><td>34.72 (+18.96%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>204.60 (n/a)</td><td>176.06 (n/a)</td><td>185.50 (n/a)</td><td>129.70 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 <b>(-20.19%)</b></td><td>0.09 (-5.74%)</td><td>0.09 (+0.29%)</td><td>0.07 (+18.10%)</td><td>0.01 <b>(-60.27%)</b></td><td>249.60 (-15.33%)</td><td>211.00 (+1.01%)</td><td>210.50 (-0.28%)</td><td>181.50 <b>(+25.26%)</b></td><td>24.79 <b>(-57.11%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>294.80 (n/a)</td><td>208.88 (n/a)</td><td>211.10 (n/a)</td><td>144.90 (n/a)</td><td>57.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (-6.61%)</td><td>0.09 (-9.11%)</td><td>0.09 (-10.74%)</td><td>0.06 (-15.83%)</td><td>0.02 (-4.48%)</td><td>297.00 (+18.80%)</td><td>209.20 (+10.75%)</td><td>196.60 (+12.02%)</td><td>143.50 (+7.09%)</td><td>57.21 <b>(+20.85%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>250.00 (n/a)</td><td>188.90 (n/a)</td><td>175.50 (n/a)</td><td>134.00 (n/a)</td><td>47.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.76 <b>(+36.70%)</b></td><td>0.57 (+9.33%)</td><td>0.57 (+6.28%)</td><td>0.43 (-6.48%)</td><td>0.13 <b>(+221.36%)</b></td><td>229.80 (+6.93%)</td><td>179.62 (-5.45%)</td><td>172.20 (-5.90%)</td><td>128.60 <b>(-26.85%)</b></td><td>38.12 <b>(+147.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.56 (n/a)</td><td>0.52 (n/a)</td><td>0.54 (n/a)</td><td>0.46 (n/a)</td><td>0.04 (n/a)</td><td>214.90 (n/a)</td><td>189.98 (n/a)</td><td>183.00 (n/a)</td><td>175.80 (n/a)</td><td>15.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 <b>(+34.22%)</b></td><td>0.54 (+2.33%)</td><td>0.54 (-2.86%)</td><td>0.32 <b>(-29.31%)</b></td><td>0.17 <b>(+163.41%)</b></td><td>305.10 <b>(+41.51%)</b></td><td>198.34 (+4.94%)</td><td>180.80 (+2.96%)</td><td>124.50 <b>(-25.49%)</b></td><td>66.70 <b>(+178.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.59 (n/a)</td><td>0.53 (n/a)</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.06 (n/a)</td><td>215.60 (n/a)</td><td>189.00 (n/a)</td><td>175.60 (n/a)</td><td>167.10 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 (-9.19%)</td><td>0.71 (+18.54%)</td><td>0.71 <b>(+29.79%)</b></td><td>0.61 <b>(+27.93%)</b></td><td>0.07 <b>(-55.47%)</b></td><td>160.10 <b>(-21.83%)</b></td><td>140.62 (-18.83%)</td><td>138.00 <b>(-22.95%)</b></td><td>124.70 (+10.16%)</td><td>14.48 <b>(-61.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.87 (n/a)</td><td>0.59 (n/a)</td><td>0.55 (n/a)</td><td>0.48 (n/a)</td><td>0.16 (n/a)</td><td>204.80 (n/a)</td><td>173.24 (n/a)</td><td>179.10 (n/a)</td><td>113.20 (n/a)</td><td>37.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.66 (-6.62%)</td><td>0.56 (+8.07%)</td><td>0.58 <b>(+22.74%)</b></td><td>0.48 (+3.06%)</td><td>0.07 <b>(-33.50%)</b></td><td>206.70 (-3.00%)</td><td>176.08 (-8.67%)</td><td>169.00 (-18.55%)</td><td>150.10 (+7.14%)</td><td>21.38 <b>(-29.30%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.70 (n/a)</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.46 (n/a)</td><td>0.10 (n/a)</td><td>213.10 (n/a)</td><td>192.80 (n/a)</td><td>207.50 (n/a)</td><td>140.10 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.53 (-14.49%)</td><td>0.45 (-3.31%)</td><td>0.50 <b>(+25.09%)</b></td><td>0.34 (-1.65%)</td><td>0.09 <b>(-32.39%)</b></td><td>215.60 (+1.70%)</td><td>168.52 (+0.90%)</td><td>146.20 <b>(-20.07%)</b></td><td>140.00 (+16.96%)</td><td>34.95 (-17.73%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.62 (n/a)</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>212.00 (n/a)</td><td>167.02 (n/a)</td><td>182.90 (n/a)</td><td>119.70 (n/a)</td><td>42.48 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.62 (-12.89%)</td><td>0.48 (+9.37%)</td><td>0.42 (+4.33%)</td><td>0.39 <b>(+36.74%)</b></td><td>0.10 <b>(-35.00%)</b></td><td>190.50 <b>(-26.87%)</b></td><td>160.76 (-13.20%)</td><td>177.30 (-4.11%)</td><td>119.80 (+14.86%)</td><td>32.29 <b>(-41.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.71 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>260.50 (n/a)</td><td>185.20 (n/a)</td><td>184.90 (n/a)</td><td>104.30 (n/a)</td><td>55.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.54 <b>(-22.62%)</b></td><td>0.42 (+1.71%)</td><td>0.38 (+8.00%)</td><td>0.35 (+14.72%)</td><td>0.08 <b>(-47.35%)</b></td><td>208.00 (-12.82%)</td><td>179.54 (-6.82%)</td><td>192.20 (-7.37%)</td><td>137.50 <b>(+29.23%)</b></td><td>32.73 <b>(-36.04%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.69 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.16 (n/a)</td><td>238.60 (n/a)</td><td>192.68 (n/a)</td><td>207.50 (n/a)</td><td>106.40 (n/a)</td><td>51.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.55 (-12.64%)</td><td>0.42 (-9.74%)</td><td>0.41 (-13.20%)</td><td>0.35 (+17.25%)</td><td>0.08 <b>(-36.12%)</b></td><td>212.10 (-14.68%)</td><td>177.82 (+6.72%)</td><td>178.80 (+15.21%)</td><td>133.70 (+14.47%)</td><td>29.20 <b>(-41.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.63 (n/a)</td><td>0.47 (n/a)</td><td>0.47 (n/a)</td><td>0.30 (n/a)</td><td>0.12 (n/a)</td><td>248.60 (n/a)</td><td>166.62 (n/a)</td><td>155.20 (n/a)</td><td>116.80 (n/a)</td><td>49.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (-1.58%)</td><td>0.22 (+7.65%)</td><td>0.22 (+13.68%)</td><td>0.17 (-2.15%)</td><td>0.04 (+1.51%)</td><td>221.80 (+2.16%)</td><td>170.10 (-6.87%)</td><td>164.40 (-12.04%)</td><td>139.30 (+1.60%)</td><td>32.30 (+9.36%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>217.10 (n/a)</td><td>182.64 (n/a)</td><td>186.90 (n/a)</td><td>137.10 (n/a)</td><td>29.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.35 (+19.81%)</td><td>0.23 (-2.91%)</td><td>0.19 <b>(-20.55%)</b></td><td>0.17 (-7.97%)</td><td>0.08 <b>(+75.37%)</b></td><td>215.30 (+8.68%)</td><td>169.62 (+7.65%)</td><td>190.60 <b>(+25.89%)</b></td><td>104.30 (-16.56%)</td><td>45.56 <b>(+57.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>198.10 (n/a)</td><td>157.56 (n/a)</td><td>151.40 (n/a)</td><td>125.00 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (-8.70%)</td><td>0.19 (-13.32%)</td><td>0.21 (-7.12%)</td><td>0.10 <b>(-35.42%)</b></td><td>0.06 (-8.91%)</td><td>371.30 <b>(+54.84%)</b></td><td>211.54 (+19.53%)</td><td>179.50 (+7.68%)</td><td>136.50 (+9.55%)</td><td>91.86 <b>(+69.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>239.80 (n/a)</td><td>176.98 (n/a)</td><td>166.70 (n/a)</td><td>124.60 (n/a)</td><td>54.26 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 <b>(-23.61%)</b></td><td>0.20 (-5.02%)</td><td>0.21 (+8.70%)</td><td>0.17 (+5.16%)</td><td>0.02 <b>(-58.52%)</b></td><td>219.50 (-4.90%)</td><td>185.50 (+1.91%)</td><td>179.00 (-8.02%)</td><td>169.00 <b>(+30.91%)</b></td><td>20.90 <b>(-47.62%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>230.80 (n/a)</td><td>182.02 (n/a)</td><td>194.60 (n/a)</td><td>129.10 (n/a)</td><td>39.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (-13.53%)</td><td>0.22 (-5.21%)</td><td>0.22 (+1.33%)</td><td>0.18 (-12.43%)</td><td>0.04 (-2.63%)</td><td>205.40 (+14.17%)</td><td>171.84 (+6.15%)</td><td>169.60 (-1.34%)</td><td>138.30 (+15.64%)</td><td>32.84 <b>(+30.77%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>179.90 (n/a)</td><td>161.88 (n/a)</td><td>171.90 (n/a)</td><td>119.60 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (+12.96%)</td><td>0.20 (+7.62%)</td><td>0.21 (+14.22%)</td><td>0.12 <b>(-21.11%)</b></td><td>0.05 <b>(+108.78%)</b></td><td>300.10 <b>(+26.78%)</b></td><td>199.36 (-2.66%)</td><td>179.00 (-12.43%)</td><td>151.40 (-11.46%)</td><td>59.74 <b>(+141.46%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>236.70 (n/a)</td><td>204.80 (n/a)</td><td>204.40 (n/a)</td><td>171.00 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 <b>(+21.13%)</b></td><td>0.22 <b>(+29.40%)</b></td><td>0.21 <b>(+27.82%)</b></td><td>0.20 <b>(+43.11%)</b></td><td>0.02 <b>(-21.72%)</b></td><td>185.60 <b>(-30.12%)</b></td><td>170.40 <b>(-23.59%)</b></td><td>171.80 <b>(-21.77%)</b></td><td>150.70 (-17.47%)</td><td>15.06 <b>(-54.59%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>265.60 (n/a)</td><td>223.02 (n/a)</td><td>219.60 (n/a)</td><td>182.60 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (+15.55%)</td><td>0.20 (+19.92%)</td><td>0.20 (+11.65%)</td><td>0.16 <b>(+43.60%)</b></td><td>0.04 (-17.16%)</td><td>225.90 <b>(-30.36%)</b></td><td>186.58 (-19.45%)</td><td>184.20 (-10.45%)</td><td>140.90 (-13.45%)</td><td>30.74 <b>(-52.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>324.40 (n/a)</td><td>231.62 (n/a)</td><td>205.70 (n/a)</td><td>162.80 (n/a)</td><td>64.14 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 <b>(-25.61%)</b></td><td>0.20 <b>(-22.21%)</b></td><td>0.21 (-18.91%)</td><td>0.11 <b>(-43.31%)</b></td><td>0.06 (-0.89%)</td><td>367.40 <b>(+76.38%)</b></td><td>219.62 <b>(+35.45%)</b></td><td>197.50 <b>(+23.28%)</b></td><td>156.00 <b>(+34.37%)</b></td><td>85.19 <b>(+149.54%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>208.30 (n/a)</td><td>162.14 (n/a)</td><td>160.20 (n/a)</td><td>116.10 (n/a)</td><td>34.14 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.35 <b>(+35.41%)</b></td><td>0.30 <b>(+30.72%)</b></td><td>0.29 <b>(+30.60%)</b></td><td>0.26 <b>(+30.17%)</b></td><td>0.04 <b>(+80.14%)</b></td><td>159.40 <b>(-23.14%)</b></td><td>140.48 <b>(-22.94%)</b></td><td>142.10 <b>(-23.40%)</b></td><td>117.60 <b>(-26.18%)</b></td><td>19.07 (+4.06%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>207.40 (n/a)</td><td>182.30 (n/a)</td><td>185.50 (n/a)</td><td>159.30 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (-14.22%)</td><td>0.22 (-8.77%)</td><td>0.21 (-7.16%)</td><td>0.20 (+0.33%)</td><td>0.02 <b>(-42.58%)</b></td><td>202.20 (-0.34%)</td><td>185.08 (+8.03%)</td><td>191.80 (+7.69%)</td><td>154.30 (+16.54%)</td><td>18.66 <b>(-33.94%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>202.90 (n/a)</td><td>171.32 (n/a)</td><td>178.10 (n/a)</td><td>132.40 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.34 (-18.36%)</td><td>0.23 (-16.96%)</td><td>0.21 (-15.54%)</td><td>0.17 (-10.84%)</td><td>0.07 <b>(-28.57%)</b></td><td>236.10 (+12.16%)</td><td>187.48 (+17.41%)</td><td>199.40 (+18.41%)</td><td>119.00 <b>(+22.43%)</b></td><td>43.05 (-6.65%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>210.50 (n/a)</td><td>159.68 (n/a)</td><td>168.40 (n/a)</td><td>97.20 (n/a)</td><td>46.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (-8.26%)</td><td>0.23 (-8.36%)</td><td>0.23 (-14.48%)</td><td>0.21 (-4.13%)</td><td>0.02 <b>(-34.10%)</b></td><td>193.40 (+4.26%)</td><td>178.20 (+8.58%)</td><td>181.10 (+16.91%)</td><td>160.10 (+8.99%)</td><td>13.24 <b>(-26.16%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>185.50 (n/a)</td><td>164.12 (n/a)</td><td>154.90 (n/a)</td><td>146.90 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.33 (+7.92%)</td><td>0.24 (-4.00%)</td><td>0.22 (-5.83%)</td><td>0.18 (-12.48%)</td><td>0.05 <b>(+60.17%)</b></td><td>221.60 (+14.29%)</td><td>179.14 (+6.53%)</td><td>182.20 (+6.24%)</td><td>125.90 (-7.36%)</td><td>35.44 <b>(+68.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>193.90 (n/a)</td><td>168.16 (n/a)</td><td>171.50 (n/a)</td><td>135.90 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (-7.16%)</td><td>0.21 (-0.34%)</td><td>0.23 (+14.85%)</td><td>0.13 (+14.20%)</td><td>0.05 (-18.71%)</td><td>318.60 (-12.42%)</td><td>211.92 (-3.22%)</td><td>179.50 (-12.95%)</td><td>158.90 (+7.73%)</td><td>66.52 <b>(-23.47%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>363.80 (n/a)</td><td>218.98 (n/a)</td><td>206.20 (n/a)</td><td>147.50 (n/a)</td><td>86.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.34 <b>(+23.24%)</b></td><td>0.23 (+13.83%)</td><td>0.24 <b>(+25.81%)</b></td><td>0.13 (-11.64%)</td><td>0.08 <b>(+66.77%)</b></td><td>315.60 (+13.16%)</td><td>199.78 (-6.30%)</td><td>169.20 <b>(-20.53%)</b></td><td>119.10 (-18.87%)</td><td>75.26 <b>(+60.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>278.90 (n/a)</td><td>213.22 (n/a)</td><td>212.90 (n/a)</td><td>146.80 (n/a)</td><td>46.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (-13.97%)</td><td>0.20 (-12.35%)</td><td>0.20 (-17.99%)</td><td>0.15 (-9.20%)</td><td>0.03 <b>(-23.63%)</b></td><td>234.90 (+10.13%)</td><td>182.48 (+13.09%)</td><td>173.60 <b>(+21.91%)</b></td><td>152.10 (+16.20%)</td><td>34.02 (-2.77%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>213.30 (n/a)</td><td>161.36 (n/a)</td><td>142.40 (n/a)</td><td>130.90 (n/a)</td><td>34.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (-0.35%)</td><td>0.20 (+4.97%)</td><td>0.20 (+2.58%)</td><td>0.16 (+16.51%)</td><td>0.03 <b>(-23.36%)</b></td><td>214.20 (-14.18%)</td><td>177.80 (-6.03%)</td><td>176.60 (-2.54%)</td><td>152.90 (+0.39%)</td><td>23.80 <b>(-35.55%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>249.60 (n/a)</td><td>189.20 (n/a)</td><td>181.20 (n/a)</td><td>152.30 (n/a)</td><td>36.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (+5.30%)</td><td>0.23 (+4.20%)</td><td>0.20 (-9.62%)</td><td>0.17 (+4.05%)</td><td>0.06 <b>(+36.50%)</b></td><td>204.90 (-3.89%)</td><td>161.70 (-2.04%)</td><td>171.00 (+10.61%)</td><td>119.20 (-5.02%)</td><td>40.41 (+18.72%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>213.20 (n/a)</td><td>165.06 (n/a)</td><td>154.60 (n/a)</td><td>125.50 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 <b>(+27.45%)</b></td><td>0.20 (+1.60%)</td><td>0.18 (-8.25%)</td><td>0.13 (-16.60%)</td><td>0.06 <b>(+156.46%)</b></td><td>260.60 (+19.87%)</td><td>189.38 (+4.84%)</td><td>188.90 (+9.00%)</td><td>120.50 <b>(-21.55%)</b></td><td>56.41 <b>(+137.69%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>217.40 (n/a)</td><td>180.64 (n/a)</td><td>173.30 (n/a)</td><td>153.60 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.31 <b>(+21.46%)</b></td><td>0.23 (+10.74%)</td><td>0.22 (-3.15%)</td><td>0.17 (+15.94%)</td><td>0.06 <b>(+24.14%)</b></td><td>207.00 (-13.75%)</td><td>158.54 (-9.37%)</td><td>156.10 (+3.24%)</td><td>111.30 (-17.68%)</td><td>38.38 (-12.19%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>240.00 (n/a)</td><td>174.94 (n/a)</td><td>151.20 (n/a)</td><td>135.20 (n/a)</td><td>43.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 <b>(+26.41%)</b></td><td>0.22 (+5.61%)</td><td>0.23 (+10.91%)</td><td>0.15 (-8.86%)</td><td>0.05 <b>(+105.41%)</b></td><td>225.80 (+9.72%)</td><td>165.66 (-2.14%)</td><td>151.40 (-9.83%)</td><td>118.70 <b>(-20.92%)</b></td><td>40.26 <b>(+80.02%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>205.80 (n/a)</td><td>169.28 (n/a)</td><td>167.90 (n/a)</td><td>150.10 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (+5.78%)</td><td>0.18 (-3.31%)</td><td>0.17 (-10.26%)</td><td>0.16 (-1.38%)</td><td>0.03 <b>(+26.06%)</b></td><td>224.10 (+1.40%)</td><td>197.06 (+4.19%)</td><td>202.80 (+11.43%)</td><td>145.30 (-5.47%)</td><td>30.24 (+16.13%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>221.00 (n/a)</td><td>189.14 (n/a)</td><td>182.00 (n/a)</td><td>153.70 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.28 (-16.35%)</td><td>0.20 (-3.73%)</td><td>0.18 (+2.61%)</td><td>0.17 <b>(+38.86%)</b></td><td>0.04 <b>(-49.07%)</b></td><td>201.50 <b>(-27.96%)</b></td><td>176.32 (-5.59%)</td><td>193.40 (-2.57%)</td><td>126.10 (+19.53%)</td><td>32.09 <b>(-54.66%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>279.70 (n/a)</td><td>186.76 (n/a)</td><td>198.50 (n/a)</td><td>105.50 (n/a)</td><td>70.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.95 <b>(+29.45%)</b></td><td>0.69 (-0.29%)</td><td>0.63 (-12.05%)</td><td>0.54 (-5.20%)</td><td>0.16 <b>(+127.78%)</b></td><td>244.40 (+5.48%)</td><td>198.40 (+3.15%)</td><td>208.80 (+13.73%)</td><td>137.70 <b>(-22.73%)</b></td><td>39.73 <b>(+77.33%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.74 (n/a)</td><td>0.69 (n/a)</td><td>0.71 (n/a)</td><td>0.57 (n/a)</td><td>0.07 (n/a)</td><td>231.70 (n/a)</td><td>192.34 (n/a)</td><td>183.60 (n/a)</td><td>178.20 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.01 (-4.44%)</td><td>0.74 (-3.82%)</td><td>0.72 (-3.55%)</td><td>0.40 <b>(-28.18%)</b></td><td>0.25 <b>(+34.45%)</b></td><td>329.00 <b>(+39.23%)</b></td><td>197.36 (+11.13%)</td><td>181.30 (+3.72%)</td><td>129.70 (+4.68%)</td><td>80.02 <b>(+98.42%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.06 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.55 (n/a)</td><td>0.18 (n/a)</td><td>236.30 (n/a)</td><td>177.60 (n/a)</td><td>174.80 (n/a)</td><td>123.90 (n/a)</td><td>40.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.02 <b>(+29.75%)</b></td><td>0.73 (-0.95%)</td><td>0.69 (-9.99%)</td><td>0.61 (-5.86%)</td><td>0.17 <b>(+192.83%)</b></td><td>215.90 (+6.25%)</td><td>186.32 (+3.89%)</td><td>190.40 (+11.09%)</td><td>128.80 <b>(-22.92%)</b></td><td>34.05 <b>(+130.78%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.76 (n/a)</td><td>0.64 (n/a)</td><td>0.06 (n/a)</td><td>203.20 (n/a)</td><td>179.34 (n/a)</td><td>171.40 (n/a)</td><td>167.10 (n/a)</td><td>14.76 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.00 (+2.27%)</td><td>0.00 (+0.46%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+81.27%)</b></td><td>980.88 (+0.66%)</td><td>941.79 (-1.36%)</td><td>945.45 (-1.51%)</td><td>905.75 (-3.51%)</td><td>33.92 <b>(+119.05%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>974.43 (n/a)</td><td>954.74 (n/a)</td><td>959.94 (n/a)</td><td>938.73 (n/a)</td><td>15.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.01 (+7.50%)</td><td>0.01 (+1.53%)</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(+71.80%)</b></td><td>1107.91 (+0.34%)</td><td>1035.56 (-1.02%)</td><td>1036.65 (+0.60%)</td><td>956.44 (-6.70%)</td><td>53.69 <b>(+60.14%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1104.19 (n/a)</td><td>1046.24 (n/a)</td><td>1030.46 (n/a)</td><td>1025.16 (n/a)</td><td>33.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.97 (-1.09%)</td><td>0.96 (-0.73%)</td><td>0.96 (-0.43%)</td><td>0.94 (-0.53%)</td><td>0.01 <b>(-25.26%)</b></td><td>2224.90 (+0.53%)</td><td>2193.42 (+0.74%)</td><td>2189.41 (+0.43%)</td><td>2171.23 (+1.10%)</td><td>19.48 <b>(-23.97%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2213.17 (n/a)</td><td>2177.35 (n/a)</td><td>2179.93 (n/a)</td><td>2147.63 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.40 (-4.71%)</td><td>0.40 (-1.21%)</td><td>0.40 (-0.73%)</td><td>0.39 (+0.60%)</td><td>0.01 <b>(-58.30%)</b></td><td>1353.60 (-0.61%)</td><td>1327.35 (+1.15%)</td><td>1327.23 (+0.74%)</td><td>1307.89 (+4.95%)</td><td>19.42 <b>(-56.77%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.01 (n/a)</td><td>1361.90 (n/a)</td><td>1312.28 (n/a)</td><td>1317.52 (n/a)</td><td>1246.23 (n/a)</td><td>44.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (-1.17%)</td><td>0.26 (-0.09%)</td><td>0.25 (-3.01%)</td><td>0.25 (+3.41%)</td><td>0.01 <b>(-40.27%)</b></td><td>2084.48 (-3.32%)</td><td>2029.92 (-0.05%)</td><td>2060.68 (+3.11%)</td><td>1937.29 (+1.18%)</td><td>60.14 <b>(-41.91%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>2156.00 (n/a)</td><td>2030.90 (n/a)</td><td>1998.53 (n/a)</td><td>1914.65 (n/a)</td><td>103.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.37 (-0.82%)</td><td>0.37 (-1.03%)</td><td>0.37 (-1.24%)</td><td>0.36 (-0.28%)</td><td>0.00 (-18.50%)</td><td>1456.30 (+0.29%)</td><td>1428.09 (+1.03%)</td><td>1426.24 (+1.25%)</td><td>1403.29 (+0.82%)</td><td>19.24 (-17.33%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1452.13 (n/a)</td><td>1413.48 (n/a)</td><td>1408.65 (n/a)</td><td>1391.83 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>6.11 (+17.00%)</td><td>5.02 (+5.38%)</td><td>4.90 (-0.14%)</td><td>4.37 (+2.77%)</td><td>0.67 <b>(+45.83%)</b></td><td>239.90 (-2.72%)</td><td>211.42 (-4.60%)</td><td>214.00 (+0.14%)</td><td>171.50 (-14.55%)</td><td>25.71 (+18.34%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>5.23 (n/a)</td><td>4.77 (n/a)</td><td>4.91 (n/a)</td><td>4.25 (n/a)</td><td>0.46 (n/a)</td><td>246.60 (n/a)</td><td>221.62 (n/a)</td><td>213.70 (n/a)</td><td>200.70 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.84 (-19.29%)</td><td>4.53 (-4.83%)</td><td>4.68 (+5.58%)</td><td>3.70 (-13.16%)</td><td>0.47 <b>(-34.28%)</b></td><td>283.50 (+15.15%)</td><td>233.70 (+4.47%)</td><td>224.00 (-5.29%)</td><td>216.60 <b>(+23.91%)</b></td><td>28.08 (-3.75%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.00 (n/a)</td><td>4.76 (n/a)</td><td>4.43 (n/a)</td><td>4.26 (n/a)</td><td>0.72 (n/a)</td><td>246.20 (n/a)</td><td>223.70 (n/a)</td><td>236.50 (n/a)</td><td>174.80 (n/a)</td><td>29.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>5.61 (-7.45%)</td><td>4.95 (+2.73%)</td><td>4.89 (+6.65%)</td><td>4.06 (+5.87%)</td><td>0.63 <b>(-23.31%)</b></td><td>258.40 (-5.52%)</td><td>214.82 (-3.50%)</td><td>214.60 (-6.25%)</td><td>186.90 (+8.10%)</td><td>28.88 <b>(-21.70%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.06 (n/a)</td><td>4.82 (n/a)</td><td>4.58 (n/a)</td><td>3.83 (n/a)</td><td>0.83 (n/a)</td><td>273.50 (n/a)</td><td>222.62 (n/a)</td><td>228.90 (n/a)</td><td>172.90 (n/a)</td><td>36.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>6.76 (-0.54%)</td><td>5.15 (+5.05%)</td><td>4.97 (-1.81%)</td><td>4.09 <b>(+44.82%)</b></td><td>0.98 <b>(-32.61%)</b></td><td>256.10 <b>(-30.95%)</b></td><td>208.78 (-10.18%)</td><td>210.80 (+1.84%)</td><td>155.20 (+0.58%)</td><td>35.83 <b>(-56.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.79 (n/a)</td><td>4.91 (n/a)</td><td>5.06 (n/a)</td><td>2.83 (n/a)</td><td>1.45 (n/a)</td><td>370.90 (n/a)</td><td>232.44 (n/a)</td><td>207.00 (n/a)</td><td>154.30 (n/a)</td><td>82.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>9.96 (+11.24%)</td><td>8.19 (-1.31%)</td><td>8.48 (+3.06%)</td><td>6.28 (-19.83%)</td><td>1.65 <b>(+271.00%)</b></td><td>333.70 <b>(+24.70%)</b></td><td>264.88 (+4.61%)</td><td>247.40 (-2.98%)</td><td>210.50 (-10.08%)</td><td>55.52 <b>(+316.92%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.96 (n/a)</td><td>8.30 (n/a)</td><td>8.23 (n/a)</td><td>7.84 (n/a)</td><td>0.44 (n/a)</td><td>267.60 (n/a)</td><td>253.20 (n/a)</td><td>255.00 (n/a)</td><td>234.10 (n/a)</td><td>13.32 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>9.54 (+6.58%)</td><td>7.85 (-0.82%)</td><td>7.67 (-2.83%)</td><td>6.74 (+1.62%)</td><td>1.04 (+4.56%)</td><td>311.30 (-1.58%)</td><td>270.82 (+0.83%)</td><td>273.50 (+2.94%)</td><td>219.80 (-6.19%)</td><td>33.26 (-4.04%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.95 (n/a)</td><td>7.91 (n/a)</td><td>7.89 (n/a)</td><td>6.63 (n/a)</td><td>0.99 (n/a)</td><td>316.30 (n/a)</td><td>268.58 (n/a)</td><td>265.70 (n/a)</td><td>234.30 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>10.10 <b>(+25.55%)</b></td><td>8.41 (+10.69%)</td><td>8.56 (+12.14%)</td><td>7.01 (-1.43%)</td><td>1.32 <b>(+288.34%)</b></td><td>299.30 (+1.46%)</td><td>254.18 (-8.01%)</td><td>244.90 (-10.82%)</td><td>207.70 <b>(-20.36%)</b></td><td>39.80 <b>(+219.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.04 (n/a)</td><td>7.60 (n/a)</td><td>7.64 (n/a)</td><td>7.11 (n/a)</td><td>0.34 (n/a)</td><td>295.00 (n/a)</td><td>276.32 (n/a)</td><td>274.60 (n/a)</td><td>260.80 (n/a)</td><td>12.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.27 (-18.96%)</td><td>7.74 (-10.88%)</td><td>7.61 (-10.11%)</td><td>7.41 (-0.73%)</td><td>0.37 <b>(-63.45%)</b></td><td>283.20 (+0.75%)</td><td>271.26 (+11.22%)</td><td>275.40 (+11.23%)</td><td>253.60 <b>(+23.41%)</b></td><td>12.76 <b>(-54.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>10.20 (n/a)</td><td>8.69 (n/a)</td><td>8.47 (n/a)</td><td>7.46 (n/a)</td><td>1.02 (n/a)</td><td>281.10 (n/a)</td><td>243.90 (n/a)</td><td>247.60 (n/a)</td><td>205.50 (n/a)</td><td>27.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>10.71 (+19.99%)</td><td>9.25 (+13.23%)</td><td>9.90 <b>(+25.73%)</b></td><td>7.42 (-2.79%)</td><td>1.48 <b>(+161.97%)</b></td><td>282.40 (+2.84%)</td><td>231.80 (-10.06%)</td><td>211.80 <b>(-20.44%)</b></td><td>195.80 (-16.68%)</td><td>39.31 <b>(+125.85%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.92 (n/a)</td><td>8.17 (n/a)</td><td>7.88 (n/a)</td><td>7.64 (n/a)</td><td>0.57 (n/a)</td><td>274.60 (n/a)</td><td>257.74 (n/a)</td><td>266.20 (n/a)</td><td>235.00 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>10.73 (+12.07%)</td><td>8.81 (+2.62%)</td><td>8.55 (+0.69%)</td><td>7.77 (-2.81%)</td><td>1.17 <b>(+98.33%)</b></td><td>270.00 (+2.90%)</td><td>241.14 (-1.64%)</td><td>245.40 (-0.69%)</td><td>195.40 (-10.78%)</td><td>29.23 <b>(+83.06%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>9.57 (n/a)</td><td>8.58 (n/a)</td><td>8.49 (n/a)</td><td>7.99 (n/a)</td><td>0.59 (n/a)</td><td>262.40 (n/a)</td><td>245.16 (n/a)</td><td>247.10 (n/a)</td><td>219.00 (n/a)</td><td>15.97 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>12.06 (+3.72%)</td><td>11.01 (-2.27%)</td><td>10.72 (-5.74%)</td><td>10.26 (-3.31%)</td><td>0.74 <b>(+94.63%)</b></td><td>408.70 (+3.42%)</td><td>382.48 (+2.59%)</td><td>391.30 (+6.10%)</td><td>347.70 (-3.60%)</td><td>25.21 <b>(+92.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>11.63 (n/a)</td><td>11.26 (n/a)</td><td>11.37 (n/a)</td><td>10.61 (n/a)</td><td>0.38 (n/a)</td><td>395.20 (n/a)</td><td>372.82 (n/a)</td><td>368.80 (n/a)</td><td>360.70 (n/a)</td><td>13.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>11.75 <b>(-20.15%)</b></td><td>10.98 (-12.14%)</td><td>10.76 (-10.49%)</td><td>10.50 (-10.03%)</td><td>0.55 <b>(-56.36%)</b></td><td>399.60 (+11.15%)</td><td>382.90 (+13.21%)</td><td>389.80 (+11.72%)</td><td>357.10 <b>(+25.25%)</b></td><td>18.85 <b>(-38.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.71 (n/a)</td><td>12.49 (n/a)</td><td>12.02 (n/a)</td><td>11.67 (n/a)</td><td>1.27 (n/a)</td><td>359.50 (n/a)</td><td>338.22 (n/a)</td><td>348.90 (n/a)</td><td>285.10 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.83 (+3.71%)</td><td>12.29 (+1.03%)</td><td>12.24 (+2.82%)</td><td>10.61 (-7.82%)</td><td>1.27 <b>(+79.20%)</b></td><td>395.40 (+8.48%)</td><td>344.20 (-0.41%)</td><td>342.80 (-2.72%)</td><td>303.40 (-3.56%)</td><td>36.15 <b>(+88.60%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.33 (n/a)</td><td>12.17 (n/a)</td><td>11.90 (n/a)</td><td>11.51 (n/a)</td><td>0.71 (n/a)</td><td>364.50 (n/a)</td><td>345.60 (n/a)</td><td>352.40 (n/a)</td><td>314.60 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>15.53 (-6.38%)</td><td>13.61 (+2.93%)</td><td>13.40 (+7.24%)</td><td>11.37 (-5.25%)</td><td>1.53 (-19.35%)</td><td>368.90 (+5.52%)</td><td>311.56 (-3.18%)</td><td>313.00 (-6.73%)</td><td>270.10 (+6.80%)</td><td>36.69 (-5.92%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>16.58 (n/a)</td><td>13.22 (n/a)</td><td>12.50 (n/a)</td><td>12.00 (n/a)</td><td>1.89 (n/a)</td><td>349.60 (n/a)</td><td>321.78 (n/a)</td><td>335.60 (n/a)</td><td>252.90 (n/a)</td><td>38.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.79 (-2.35%)</td><td>12.60 (-4.28%)</td><td>12.76 (-5.92%)</td><td>11.79 (-1.98%)</td><td>0.84 (-1.31%)</td><td>355.80 (+2.01%)</td><td>334.04 (+4.49%)</td><td>328.80 (+6.30%)</td><td>304.20 (+2.42%)</td><td>22.00 (+3.83%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.12 (n/a)</td><td>13.16 (n/a)</td><td>13.56 (n/a)</td><td>12.03 (n/a)</td><td>0.85 (n/a)</td><td>348.80 (n/a)</td><td>319.70 (n/a)</td><td>309.30 (n/a)</td><td>297.00 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.45 (-8.82%)</td><td>12.91 (-4.44%)</td><td>13.30 (-0.22%)</td><td>11.20 (-7.59%)</td><td>0.96 (-17.13%)</td><td>374.60 (+8.20%)</td><td>326.42 (+4.53%)</td><td>315.20 (+0.19%)</td><td>311.90 (+9.67%)</td><td>26.97 (+0.36%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.75 (n/a)</td><td>13.51 (n/a)</td><td>13.33 (n/a)</td><td>12.12 (n/a)</td><td>1.16 (n/a)</td><td>346.20 (n/a)</td><td>312.26 (n/a)</td><td>314.60 (n/a)</td><td>284.40 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.95 (-3.43%)</td><td>13.06 (+3.63%)</td><td>13.03 (+2.67%)</td><td>12.43 <b>(+27.19%)</b></td><td>0.57 <b>(-68.41%)</b></td><td>337.40 <b>(-21.37%)</b></td><td>321.64 (-5.14%)</td><td>322.00 (-2.60%)</td><td>300.80 (+3.58%)</td><td>13.84 <b>(-74.69%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.44 (n/a)</td><td>12.60 (n/a)</td><td>12.69 (n/a)</td><td>9.77 (n/a)</td><td>1.82 (n/a)</td><td>429.10 (n/a)</td><td>339.06 (n/a)</td><td>330.60 (n/a)</td><td>290.40 (n/a)</td><td>54.67 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>14.35 (-3.83%)</td><td>13.06 (+6.21%)</td><td>13.24 (+2.61%)</td><td>11.99 <b>(+21.24%)</b></td><td>0.93 <b>(-54.95%)</b></td><td>349.70 (-17.52%)</td><td>322.32 (-7.61%)</td><td>316.70 (-2.55%)</td><td>292.30 (+3.98%)</td><td>22.65 <b>(-61.88%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.92 (n/a)</td><td>12.30 (n/a)</td><td>12.91 (n/a)</td><td>9.89 (n/a)</td><td>2.05 (n/a)</td><td>424.00 (n/a)</td><td>348.88 (n/a)</td><td>325.00 (n/a)</td><td>281.10 (n/a)</td><td>59.41 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.76 (+4.28%)</td><td>2.83 (-9.52%)</td><td>2.81 (-14.45%)</td><td>2.30 (-12.01%)</td><td>0.59 <b>(+27.63%)</b></td><td>228.30 (+13.64%)</td><td>191.22 (+11.96%)</td><td>186.30 (+16.88%)</td><td>139.30 (-4.13%)</td><td>35.70 <b>(+37.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.61 (n/a)</td><td>3.13 (n/a)</td><td>3.29 (n/a)</td><td>2.61 (n/a)</td><td>0.46 (n/a)</td><td>200.90 (n/a)</td><td>170.80 (n/a)</td><td>159.40 (n/a)</td><td>145.30 (n/a)</td><td>26.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>5.54 (+14.03%)</td><td>4.62 (+16.72%)</td><td>4.87 <b>(+31.21%)</b></td><td>3.57 (+18.24%)</td><td>0.76 (-0.02%)</td><td>293.40 (-15.45%)</td><td>232.54 (-14.92%)</td><td>215.50 <b>(-23.77%)</b></td><td>189.20 (-12.33%)</td><td>40.94 <b>(-23.23%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.86 (n/a)</td><td>3.95 (n/a)</td><td>3.71 (n/a)</td><td>3.02 (n/a)</td><td>0.76 (n/a)</td><td>347.00 (n/a)</td><td>273.32 (n/a)</td><td>282.70 (n/a)</td><td>215.80 (n/a)</td><td>53.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.27 (-5.78%)</td><td>7.37 (-1.58%)</td><td>7.30 (-0.88%)</td><td>6.49 (-3.14%)</td><td>0.64 <b>(-22.07%)</b></td><td>323.10 (+3.23%)</td><td>286.30 (+1.30%)</td><td>287.20 (+0.88%)</td><td>253.60 (+6.15%)</td><td>24.88 (-14.10%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.78 (n/a)</td><td>7.49 (n/a)</td><td>7.37 (n/a)</td><td>6.70 (n/a)</td><td>0.82 (n/a)</td><td>313.00 (n/a)</td><td>282.62 (n/a)</td><td>284.70 (n/a)</td><td>238.90 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.29 (-0.83%)</td><td>2.98 (+4.45%)</td><td>2.86 (-7.35%)</td><td>2.68 <b>(+24.21%)</b></td><td>0.26 <b>(-45.29%)</b></td><td>195.90 (-19.48%)</td><td>177.18 (-6.06%)</td><td>183.30 (+7.95%)</td><td>159.10 (+0.82%)</td><td>15.31 <b>(-56.27%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.32 (n/a)</td><td>2.85 (n/a)</td><td>3.09 (n/a)</td><td>2.15 (n/a)</td><td>0.47 (n/a)</td><td>243.30 (n/a)</td><td>188.60 (n/a)</td><td>169.80 (n/a)</td><td>157.80 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 <b>(-24.42%)</b></td><td>0.18 (-16.88%)</td><td>0.21 (-10.63%)</td><td>0.10 (-3.04%)</td><td>0.05 <b>(-29.86%)</b></td><td>344.10 (+3.15%)</td><td>196.94 (+14.51%)</td><td>155.70 (+11.85%)</td><td>154.00 <b>(+32.30%)</b></td><td>82.73 (-9.14%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>333.60 (n/a)</td><td>171.98 (n/a)</td><td>139.20 (n/a)</td><td>116.40 (n/a)</td><td>91.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (-0.31%)</td><td>0.22 (+15.44%)</td><td>0.22 <b>(+21.28%)</b></td><td>0.19 <b>(+23.88%)</b></td><td>0.03 <b>(-25.84%)</b></td><td>170.00 (-19.28%)</td><td>148.72 (-14.67%)</td><td>150.00 (-17.54%)</td><td>129.30 (+0.31%)</td><td>18.60 <b>(-39.45%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.60 (n/a)</td><td>174.28 (n/a)</td><td>181.90 (n/a)</td><td>128.90 (n/a)</td><td>30.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.56 (+13.37%)</td><td>0.40 (-0.29%)</td><td>0.39 (+0.62%)</td><td>0.31 (-12.84%)</td><td>0.10 <b>(+77.48%)</b></td><td>213.50 (+14.72%)</td><td>170.06 (+3.07%)</td><td>168.90 (-0.59%)</td><td>117.30 (-11.74%)</td><td>35.64 <b>(+78.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.05 (n/a)</td><td>186.10 (n/a)</td><td>165.00 (n/a)</td><td>169.90 (n/a)</td><td>132.90 (n/a)</td><td>19.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.55 (+10.48%)</td><td>0.44 (+0.72%)</td><td>0.46 (+4.79%)</td><td>0.32 (-14.64%)</td><td>0.11 <b>(+138.21%)</b></td><td>205.50 (+17.16%)</td><td>155.82 (+3.67%)</td><td>143.40 (-4.53%)</td><td>118.90 (-9.51%)</td><td>40.40 <b>(+147.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>175.40 (n/a)</td><td>150.30 (n/a)</td><td>150.20 (n/a)</td><td>131.40 (n/a)</td><td>16.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.54 (+15.45%)</td><td>0.38 (-3.72%)</td><td>0.34 (-9.64%)</td><td>0.29 (-12.24%)</td><td>0.11 <b>(+63.79%)</b></td><td>228.50 (+13.97%)</td><td>184.12 (+7.55%)</td><td>193.20 (+10.65%)</td><td>121.90 (-13.36%)</td><td>45.48 <b>(+65.17%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>200.50 (n/a)</td><td>171.20 (n/a)</td><td>174.60 (n/a)</td><td>140.70 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.05 (+12.99%)</td><td>0.77 (+6.05%)</td><td>0.72 (-4.09%)</td><td>0.58 <b>(+46.70%)</b></td><td>0.18 (-15.78%)</td><td>224.50 <b>(-31.83%)</b></td><td>178.06 (-10.62%)</td><td>183.00 (+4.21%)</td><td>124.50 (-11.51%)</td><td>38.59 <b>(-50.05%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.93 (n/a)</td><td>0.72 (n/a)</td><td>0.75 (n/a)</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>329.30 (n/a)</td><td>199.22 (n/a)</td><td>175.60 (n/a)</td><td>140.70 (n/a)</td><td>77.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.08 <b>(+23.39%)</b></td><td>0.78 (+1.78%)</td><td>0.74 (-8.21%)</td><td>0.59 (-8.04%)</td><td>0.19 <b>(+86.99%)</b></td><td>223.20 (+8.72%)</td><td>176.40 (+1.24%)</td><td>176.70 (+8.94%)</td><td>121.20 (-18.98%)</td><td>39.97 <b>(+61.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.88 (n/a)</td><td>0.76 (n/a)</td><td>0.81 (n/a)</td><td>0.64 (n/a)</td><td>0.10 (n/a)</td><td>205.30 (n/a)</td><td>174.24 (n/a)</td><td>162.20 (n/a)</td><td>149.60 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.95 (-4.70%)</td><td>0.89 (+9.59%)</td><td>0.91 (+7.52%)</td><td>0.78 <b>(+44.37%)</b></td><td>0.07 <b>(-62.14%)</b></td><td>167.70 <b>(-30.70%)</b></td><td>148.50 (-12.33%)</td><td>144.30 (-6.96%)</td><td>137.40 (+4.97%)</td><td>11.78 <b>(-73.00%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.00 (n/a)</td><td>0.81 (n/a)</td><td>0.85 (n/a)</td><td>0.54 (n/a)</td><td>0.18 (n/a)</td><td>242.00 (n/a)</td><td>169.38 (n/a)</td><td>155.10 (n/a)</td><td>130.90 (n/a)</td><td>43.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.78 (-9.24%)</td><td>0.65 (-14.14%)</td><td>0.62 (-19.14%)</td><td>0.54 (-15.53%)</td><td>0.11 <b>(+40.13%)</b></td><td>243.00 (+18.42%)</td><td>205.92 (+17.99%)</td><td>212.10 <b>(+23.67%)</b></td><td>169.10 (+10.23%)</td><td>33.35 <b>(+76.75%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.85 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.64 (n/a)</td><td>0.08 (n/a)</td><td>205.20 (n/a)</td><td>174.52 (n/a)</td><td>171.50 (n/a)</td><td>153.40 (n/a)</td><td>18.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (+10.46%)</td><td>0.10 (+4.55%)</td><td>0.10 (+1.52%)</td><td>0.06 <b>(-30.70%)</b></td><td>0.03 <b>(+98.40%)</b></td><td>285.50 <b>(+44.34%)</b></td><td>176.42 (+2.99%)</td><td>169.20 (-1.51%)</td><td>119.60 (-9.46%)</td><td>65.80 <b>(+169.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.80 (n/a)</td><td>171.30 (n/a)</td><td>171.80 (n/a)</td><td>132.10 (n/a)</td><td>24.39 (n/a)</td>
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
