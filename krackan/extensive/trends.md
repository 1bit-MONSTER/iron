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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-0.31%)</td><td>0.04 (-2.91%)</td><td>0.04 (+0.48%)</td><td>0.03 (+2.04%)</td><td>0.00 (-19.41%)</td><td>190.20 (-2.01%)</td><td>170.54 (+2.25%)</td><td>173.10 (-0.52%)</td><td>138.10 (+0.29%)</td><td>20.52 <b>(-20.41%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>166.78 (n/a)</td><td>174.00 (n/a)</td><td>137.70 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (+0.58%)</td><td>0.04 (+2.74%)</td><td>0.04 (+6.26%)</td><td>0.03 (-10.30%)</td><td>0.00 <b>(+46.45%)</b></td><td>222.10 (+11.50%)</td><td>173.80 (-1.65%)</td><td>163.20 (-5.88%)</td><td>153.20 (-0.58%)</td><td>27.80 <b>(+66.54%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.20 (n/a)</td><td>176.72 (n/a)</td><td>173.40 (n/a)</td><td>154.10 (n/a)</td><td>16.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (+6.50%)</td><td>0.03 (-4.26%)</td><td>0.03 (-7.73%)</td><td>0.03 (+9.85%)</td><td>0.01 (+3.12%)</td><td>241.70 (-8.96%)</td><td>186.20 (+3.88%)</td><td>177.50 (+8.36%)</td><td>138.40 (-6.11%)</td><td>41.86 (-14.34%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>265.50 (n/a)</td><td>179.24 (n/a)</td><td>163.80 (n/a)</td><td>147.40 (n/a)</td><td>48.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-13.30%)</td><td>0.03 (-3.86%)</td><td>0.03 (-0.18%)</td><td>0.03 (-8.49%)</td><td>0.00 <b>(-33.49%)</b></td><td>244.30 (+9.26%)</td><td>187.08 (+2.44%)</td><td>175.90 (+0.17%)</td><td>166.10 (+15.35%)</td><td>32.38 (-15.30%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>182.62 (n/a)</td><td>175.60 (n/a)</td><td>144.00 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-18.93%)</td><td>0.03 (-3.31%)</td><td>0.04 (-0.65%)</td><td>0.03 (+7.30%)</td><td>0.00 <b>(-71.60%)</b></td><td>190.40 (-6.80%)</td><td>176.44 (+1.24%)</td><td>172.70 (+0.64%)</td><td>166.30 <b>(+23.37%)</b></td><td>9.34 <b>(-67.79%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>174.28 (n/a)</td><td>171.60 (n/a)</td><td>134.80 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-8.05%)</td><td>0.03 (-6.79%)</td><td>0.03 (-0.16%)</td><td>0.03 (-7.67%)</td><td>0.00 (-18.08%)</td><td>201.90 (+8.32%)</td><td>180.16 (+7.10%)</td><td>175.70 (+0.17%)</td><td>159.10 (+8.75%)</td><td>16.35 (-2.64%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.40 (n/a)</td><td>168.22 (n/a)</td><td>175.40 (n/a)</td><td>146.30 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 <b>(+23.64%)</b></td><td>0.03 (+5.97%)</td><td>0.03 (-0.02%)</td><td>0.03 (+8.14%)</td><td>0.01 <b>(+78.13%)</b></td><td>229.60 (-7.53%)</td><td>200.24 (-4.07%)</td><td>204.20 (+0.00%)</td><td>142.70 (-19.10%)</td><td>34.52 <b>(+29.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.30 (n/a)</td><td>208.74 (n/a)</td><td>204.20 (n/a)</td><td>176.40 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (+16.72%)</td><td>0.03 (+3.52%)</td><td>0.03 (-3.48%)</td><td>0.03 (+3.43%)</td><td>0.00 <b>(+65.00%)</b></td><td>220.60 (-3.29%)</td><td>193.08 (-2.59%)</td><td>199.20 (+3.59%)</td><td>155.80 (-14.30%)</td><td>25.33 <b>(+35.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>228.10 (n/a)</td><td>198.22 (n/a)</td><td>192.30 (n/a)</td><td>181.80 (n/a)</td><td>18.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(-27.90%)</b></td><td>0.06 (-17.76%)</td><td>0.06 (-18.10%)</td><td>0.06 (-4.81%)</td><td>0.01 <b>(-57.58%)</b></td><td>213.50 (+5.07%)</td><td>197.70 (+19.59%)</td><td>203.20 <b>(+22.12%)</b></td><td>174.50 <b>(+38.71%)</b></td><td>17.43 <b>(-36.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>165.32 (n/a)</td><td>166.40 (n/a)</td><td>125.80 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (-17.89%)</td><td>0.07 <b>(-21.42%)</b></td><td>0.06 <b>(-24.12%)</b></td><td>0.05 <b>(-27.71%)</b></td><td>0.01 (+3.64%)</td><td>238.80 <b>(+38.27%)</b></td><td>192.24 <b>(+28.69%)</b></td><td>189.70 <b>(+31.74%)</b></td><td>149.10 <b>(+21.81%)</b></td><td>34.30 <b>(+73.33%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>149.38 (n/a)</td><td>144.00 (n/a)</td><td>122.40 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (+3.40%)</td><td>0.08 (+0.75%)</td><td>0.07 (-1.80%)</td><td>0.07 (+9.00%)</td><td>0.01 (+1.66%)</td><td>180.30 (-8.24%)</td><td>160.78 (-0.85%)</td><td>164.60 (+1.79%)</td><td>135.70 (-3.35%)</td><td>20.57 (-8.23%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>162.16 (n/a)</td><td>161.70 (n/a)</td><td>140.40 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (+13.63%)</td><td>0.07 (+1.41%)</td><td>0.07 (+8.80%)</td><td>0.05 (-5.70%)</td><td>0.01 <b>(+71.39%)</b></td><td>226.10 (+6.05%)</td><td>185.68 (+0.29%)</td><td>173.50 (-8.06%)</td><td>144.60 (-12.04%)</td><td>33.58 <b>(+66.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>185.14 (n/a)</td><td>188.70 (n/a)</td><td>164.40 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (-15.74%)</td><td>0.07 (+7.56%)</td><td>0.07 (+14.55%)</td><td>0.06 <b>(+62.35%)</b></td><td>0.01 <b>(-64.67%)</b></td><td>208.00 <b>(-38.41%)</b></td><td>175.60 (-14.72%)</td><td>168.60 (-12.73%)</td><td>156.70 (+18.71%)</td><td>19.66 <b>(-74.93%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>337.70 (n/a)</td><td>205.90 (n/a)</td><td>193.20 (n/a)</td><td>132.00 (n/a)</td><td>78.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (-0.06%)</td><td>0.07 (-11.54%)</td><td>0.06 (-19.28%)</td><td>0.06 (+1.08%)</td><td>0.01 (-9.44%)</td><td>215.40 (-1.06%)</td><td>186.94 (+12.48%)</td><td>191.30 <b>(+23.82%)</b></td><td>146.00 (+0.07%)</td><td>25.22 (-14.87%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>166.20 (n/a)</td><td>154.50 (n/a)</td><td>145.90 (n/a)</td><td>29.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 <b>(-20.27%)</b></td><td>0.07 (-1.21%)</td><td>0.06 (+4.79%)</td><td>0.06 (+6.06%)</td><td>0.01 <b>(-40.38%)</b></td><td>219.60 (-5.71%)</td><td>188.32 (-1.44%)</td><td>193.60 (-4.54%)</td><td>156.90 <b>(+25.42%)</b></td><td>29.82 <b>(-28.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>191.08 (n/a)</td><td>202.80 (n/a)</td><td>125.10 (n/a)</td><td>41.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (-7.84%)</td><td>0.07 (-0.99%)</td><td>0.07 (+1.92%)</td><td>0.05 (-15.11%)</td><td>0.01 (+7.88%)</td><td>230.80 (+17.82%)</td><td>179.54 (+1.86%)</td><td>179.90 (-1.85%)</td><td>146.90 (+8.49%)</td><td>33.82 <b>(+37.53%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>176.26 (n/a)</td><td>183.30 (n/a)</td><td>135.40 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 <b>(+41.23%)</b></td><td>0.17 (+16.18%)</td><td>0.15 (+3.71%)</td><td>0.15 (+9.44%)</td><td>0.05 <b>(+141.77%)</b></td><td>168.00 (-8.60%)</td><td>147.84 (-11.19%)</td><td>162.00 (-3.57%)</td><td>96.30 <b>(-29.19%)</b></td><td>29.51 <b>(+52.58%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>183.80 (n/a)</td><td>166.46 (n/a)</td><td>168.00 (n/a)</td><td>136.00 (n/a)</td><td>19.34 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 <b>(+27.97%)</b></td><td>0.16 (+12.64%)</td><td>0.15 (+6.60%)</td><td>0.13 <b>(+36.33%)</b></td><td>0.02 (+7.44%)</td><td>182.40 <b>(-26.66%)</b></td><td>160.08 (-12.07%)</td><td>159.60 (-6.17%)</td><td>125.00 <b>(-21.83%)</b></td><td>22.59 <b>(-40.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>182.06 (n/a)</td><td>170.10 (n/a)</td><td>159.90 (n/a)</td><td>37.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (-12.20%)</td><td>0.15 (+5.71%)</td><td>0.16 (+8.51%)</td><td>0.13 <b>(+46.56%)</b></td><td>0.02 <b>(-61.86%)</b></td><td>195.00 <b>(-31.77%)</b></td><td>162.16 (-11.94%)</td><td>153.20 (-7.82%)</td><td>148.90 (+13.93%)</td><td>19.16 <b>(-69.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>285.80 (n/a)</td><td>184.14 (n/a)</td><td>166.20 (n/a)</td><td>130.70 (n/a)</td><td>63.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (+2.37%)</td><td>0.16 (+9.35%)</td><td>0.17 (+17.34%)</td><td>0.12 (-5.25%)</td><td>0.02 (+11.37%)</td><td>198.80 (+5.58%)</td><td>152.34 (-8.07%)</td><td>143.60 (-14.78%)</td><td>130.40 (-2.25%)</td><td>26.75 (+18.55%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>188.30 (n/a)</td><td>165.72 (n/a)</td><td>168.50 (n/a)</td><td>133.40 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (-4.20%)</td><td>0.13 (-4.08%)</td><td>0.12 (-5.39%)</td><td>0.11 (+9.73%)</td><td>0.03 <b>(-20.18%)</b></td><td>230.30 (-8.86%)</td><td>193.54 (+2.25%)</td><td>201.80 (+5.65%)</td><td>139.10 (+4.35%)</td><td>33.74 <b>(-26.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>252.70 (n/a)</td><td>189.28 (n/a)</td><td>191.00 (n/a)</td><td>133.30 (n/a)</td><td>45.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (+14.00%)</td><td>0.14 (+1.28%)</td><td>0.13 (-6.93%)</td><td>0.12 (+2.72%)</td><td>0.03 <b>(+51.50%)</b></td><td>208.90 (-2.66%)</td><td>178.32 (-0.16%)</td><td>184.60 (+7.45%)</td><td>136.20 (-12.24%)</td><td>29.00 <b>(+26.97%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>178.60 (n/a)</td><td>171.80 (n/a)</td><td>155.20 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (+2.64%)</td><td>0.13 (+12.23%)</td><td>0.13 (+17.70%)</td><td>0.11 (+12.23%)</td><td>0.02 <b>(-25.99%)</b></td><td>229.20 (-10.92%)</td><td>193.06 (-12.10%)</td><td>192.30 (-15.02%)</td><td>166.90 (-2.57%)</td><td>24.28 <b>(-36.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>257.30 (n/a)</td><td>219.64 (n/a)</td><td>226.30 (n/a)</td><td>171.30 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (+4.06%)</td><td>0.12 (-12.98%)</td><td>0.11 (-17.41%)</td><td>0.07 <b>(-36.37%)</b></td><td>0.03 <b>(+98.58%)</b></td><td>333.80 <b>(+57.16%)</b></td><td>227.42 <b>(+21.95%)</b></td><td>227.00 <b>(+21.13%)</b></td><td>145.30 (-3.90%)</td><td>68.87 <b>(+207.12%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>186.48 (n/a)</td><td>187.40 (n/a)</td><td>151.20 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.43 (+2.54%)</td><td>0.29 (-3.00%)</td><td>0.27 (+6.75%)</td><td>0.22 (-1.01%)</td><td>0.08 (-8.09%)</td><td>221.60 (+1.05%)</td><td>179.44 (+1.67%)</td><td>181.30 (-6.30%)</td><td>114.60 (-2.47%)</td><td>41.90 (-13.27%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>219.30 (n/a)</td><td>176.50 (n/a)</td><td>193.50 (n/a)</td><td>117.50 (n/a)</td><td>48.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (-19.17%)</td><td>0.27 (-13.56%)</td><td>0.26 (-8.55%)</td><td>0.22 (-16.47%)</td><td>0.03 <b>(-35.30%)</b></td><td>223.10 (+19.69%)</td><td>186.64 (+14.83%)</td><td>186.80 (+9.30%)</td><td>163.90 <b>(+23.70%)</b></td><td>23.39 (-4.43%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>186.40 (n/a)</td><td>162.54 (n/a)</td><td>170.90 (n/a)</td><td>132.50 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.33 (-14.65%)</td><td>0.27 (-6.86%)</td><td>0.27 (-5.47%)</td><td>0.22 (+13.24%)</td><td>0.04 <b>(-48.30%)</b></td><td>220.40 (-11.70%)</td><td>183.52 (+2.87%)</td><td>180.50 (+5.80%)</td><td>146.90 (+17.15%)</td><td>26.31 <b>(-46.93%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>249.60 (n/a)</td><td>178.40 (n/a)</td><td>170.60 (n/a)</td><td>125.40 (n/a)</td><td>49.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.45 (+18.48%)</td><td>0.28 (-3.58%)</td><td>0.26 (+3.90%)</td><td>0.21 (-8.09%)</td><td>0.10 <b>(+25.63%)</b></td><td>238.70 (+8.85%)</td><td>188.90 (+5.79%)</td><td>191.50 (-3.77%)</td><td>109.40 (-15.65%)</td><td>49.30 (+12.30%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>219.30 (n/a)</td><td>178.56 (n/a)</td><td>199.00 (n/a)</td><td>129.70 (n/a)</td><td>43.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.32 (-14.07%)</td><td>0.25 (-14.79%)</td><td>0.26 (-6.08%)</td><td>0.13 <b>(-46.23%)</b></td><td>0.07 <b>(+53.74%)</b></td><td>372.90 <b>(+85.99%)</b></td><td>219.66 <b>(+26.96%)</b></td><td>187.80 (+6.52%)</td><td>155.10 (+16.44%)</td><td>88.75 <b>(+255.76%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>200.50 (n/a)</td><td>173.02 (n/a)</td><td>176.30 (n/a)</td><td>133.20 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.39 (+7.58%)</td><td>0.28 (+2.36%)</td><td>0.29 (-2.37%)</td><td>0.20 (+11.38%)</td><td>0.07 (+3.37%)</td><td>241.20 (-10.23%)</td><td>181.28 (-3.03%)</td><td>172.40 (+2.44%)</td><td>125.60 (-7.10%)</td><td>42.09 (-17.08%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>268.70 (n/a)</td><td>186.94 (n/a)</td><td>168.30 (n/a)</td><td>135.20 (n/a)</td><td>50.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.32 (+10.02%)</td><td>0.27 (+8.59%)</td><td>0.26 (+9.08%)</td><td>0.24 (+12.70%)</td><td>0.03 (-6.58%)</td><td>202.00 (-11.29%)</td><td>185.58 (-8.30%)</td><td>188.90 (-8.35%)</td><td>154.10 (-9.09%)</td><td>19.15 <b>(-26.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>227.70 (n/a)</td><td>202.38 (n/a)</td><td>206.10 (n/a)</td><td>169.50 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (-0.70%)</td><td>0.25 (+1.46%)</td><td>0.23 (-3.40%)</td><td>0.22 (+12.67%)</td><td>0.04 (-6.41%)</td><td>226.90 (-11.23%)</td><td>197.86 (-1.95%)</td><td>210.30 (+3.49%)</td><td>164.80 (+0.73%)</td><td>29.60 (-17.49%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>255.60 (n/a)</td><td>201.80 (n/a)</td><td>203.20 (n/a)</td><td>163.60 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (+9.73%)</td><td>0.02 (+12.25%)</td><td>0.02 (+5.33%)</td><td>0.01 (+5.55%)</td><td>0.00 <b>(+25.24%)</b></td><td>214.30 (-5.26%)</td><td>157.08 (-9.80%)</td><td>163.60 (-5.05%)</td><td>114.60 (-8.83%)</td><td>38.87 (+8.21%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>226.20 (n/a)</td><td>174.14 (n/a)</td><td>172.30 (n/a)</td><td>125.70 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-5.01%)</td><td>0.02 (-3.88%)</td><td>0.02 (-2.98%)</td><td>0.01 (-17.09%)</td><td>0.00 <b>(+32.06%)</b></td><td>231.30 <b>(+20.59%)</b></td><td>166.36 (+5.98%)</td><td>158.90 (+3.05%)</td><td>137.80 (+5.27%)</td><td>37.58 <b>(+70.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>191.80 (n/a)</td><td>156.98 (n/a)</td><td>154.20 (n/a)</td><td>130.90 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (+17.48%)</td><td>0.02 (-3.84%)</td><td>0.02 (-6.35%)</td><td>0.01 <b>(-28.37%)</b></td><td>0.00 <b>(+176.50%)</b></td><td>229.10 <b>(+39.61%)</b></td><td>164.84 (+8.63%)</td><td>160.60 (+6.78%)</td><td>113.30 (-14.88%)</td><td>41.35 <b>(+227.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.10 (n/a)</td><td>151.74 (n/a)</td><td>150.40 (n/a)</td><td>133.10 (n/a)</td><td>12.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (+2.56%)</td><td>0.01 (-12.79%)</td><td>0.01 (-15.77%)</td><td>0.01 <b>(-20.38%)</b></td><td>0.00 <b>(+56.06%)</b></td><td>233.50 <b>(+25.61%)</b></td><td>195.26 (+16.81%)</td><td>200.30 (+18.73%)</td><td>142.60 (-2.53%)</td><td>34.53 <b>(+86.11%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>185.90 (n/a)</td><td>167.16 (n/a)</td><td>168.70 (n/a)</td><td>146.30 (n/a)</td><td>18.55 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 <b>(-32.63%)</b></td><td>0.01 (-17.43%)</td><td>0.01 (-18.95%)</td><td>0.01 (+14.28%)</td><td>0.00 <b>(-76.69%)</b></td><td>208.70 (-12.53%)</td><td>197.66 (+15.59%)</td><td>203.50 <b>(+23.33%)</b></td><td>176.90 <b>(+48.41%)</b></td><td>13.05 <b>(-70.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>238.60 (n/a)</td><td>171.00 (n/a)</td><td>165.00 (n/a)</td><td>119.20 (n/a)</td><td>43.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 <b>(-28.40%)</b></td><td>0.01 (-15.95%)</td><td>0.01 (-8.34%)</td><td>0.01 (-16.74%)</td><td>0.00 <b>(-41.22%)</b></td><td>290.30 <b>(+20.11%)</b></td><td>222.26 (+16.62%)</td><td>224.90 (+9.12%)</td><td>183.50 <b>(+39.65%)</b></td><td>43.41 (-1.92%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>241.70 (n/a)</td><td>190.58 (n/a)</td><td>206.10 (n/a)</td><td>131.40 (n/a)</td><td>44.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 <b>(-24.41%)</b></td><td>0.01 (-6.71%)</td><td>0.01 (+15.49%)</td><td>0.01 (-7.36%)</td><td>0.00 <b>(-55.56%)</b></td><td>253.20 (+7.97%)</td><td>201.60 (+3.59%)</td><td>191.40 (-13.43%)</td><td>183.70 <b>(+32.35%)</b></td><td>29.06 <b>(-35.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>234.50 (n/a)</td><td>194.62 (n/a)</td><td>221.10 (n/a)</td><td>138.80 (n/a)</td><td>45.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 (+2.69%)</td><td>0.01 (+5.51%)</td><td>0.01 (+8.42%)</td><td>0.01 (+6.45%)</td><td>0.00 (-9.76%)</td><td>231.20 (-6.05%)</td><td>204.74 (-5.47%)</td><td>204.10 (-7.77%)</td><td>175.20 (-2.61%)</td><td>19.96 (-16.93%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>246.10 (n/a)</td><td>216.58 (n/a)</td><td>221.30 (n/a)</td><td>179.90 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-11.33%)</td><td>0.03 (+4.26%)</td><td>0.04 (+19.12%)</td><td>0.03 (-0.84%)</td><td>0.01 (-11.88%)</td><td>208.50 (+0.82%)</td><td>158.26 (-4.34%)</td><td>141.50 (-16.07%)</td><td>131.00 (+12.74%)</td><td>33.37 (+3.21%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>165.44 (n/a)</td><td>168.60 (n/a)</td><td>116.20 (n/a)</td><td>32.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (+14.33%)</td><td>0.03 (+17.40%)</td><td>0.03 (+18.03%)</td><td>0.02 (+9.89%)</td><td>0.01 (+16.57%)</td><td>216.40 (-9.00%)</td><td>167.26 (-14.58%)</td><td>169.10 (-15.28%)</td><td>125.70 (-12.53%)</td><td>33.34 (-5.34%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>195.82 (n/a)</td><td>199.60 (n/a)</td><td>143.70 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (+3.20%)</td><td>0.03 (+8.01%)</td><td>0.03 (+3.20%)</td><td>0.03 (+14.63%)</td><td>0.01 (-11.95%)</td><td>182.00 (-12.75%)</td><td>161.36 (-8.38%)</td><td>171.30 (-3.11%)</td><td>123.40 (-3.14%)</td><td>24.10 <b>(-25.55%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>176.12 (n/a)</td><td>176.80 (n/a)</td><td>127.40 (n/a)</td><td>32.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-1.22%)</td><td>0.03 (+5.85%)</td><td>0.03 (+15.12%)</td><td>0.02 (-10.46%)</td><td>0.00 (+13.85%)</td><td>265.70 (+11.69%)</td><td>199.60 (-4.64%)</td><td>181.20 (-13.14%)</td><td>163.90 (+1.24%)</td><td>40.25 <b>(+31.78%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.90 (n/a)</td><td>209.32 (n/a)</td><td>208.60 (n/a)</td><td>161.90 (n/a)</td><td>30.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-16.48%)</td><td>0.03 (-11.79%)</td><td>0.03 (-3.31%)</td><td>0.02 (-11.95%)</td><td>0.00 <b>(-22.02%)</b></td><td>248.60 (+13.57%)</td><td>190.14 (+12.88%)</td><td>175.80 (+3.41%)</td><td>157.60 (+19.76%)</td><td>35.03 (+8.02%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>168.44 (n/a)</td><td>170.00 (n/a)</td><td>131.60 (n/a)</td><td>32.43 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-14.28%)</td><td>0.03 (-3.14%)</td><td>0.03 (+8.16%)</td><td>0.03 <b>(+22.59%)</b></td><td>0.00 <b>(-55.62%)</b></td><td>203.60 (-18.43%)</td><td>175.70 (-1.65%)</td><td>172.50 (-7.56%)</td><td>146.40 (+16.65%)</td><td>21.25 <b>(-56.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.60 (n/a)</td><td>178.64 (n/a)</td><td>186.60 (n/a)</td><td>125.50 (n/a)</td><td>49.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-7.45%)</td><td>0.03 (+8.26%)</td><td>0.03 (+11.99%)</td><td>0.03 (+8.81%)</td><td>0.01 <b>(-22.78%)</b></td><td>199.60 (-8.10%)</td><td>160.08 (-9.90%)</td><td>171.80 (-10.71%)</td><td>116.70 (+8.06%)</td><td>33.89 <b>(-22.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>177.66 (n/a)</td><td>192.40 (n/a)</td><td>108.00 (n/a)</td><td>43.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-17.38%)</td><td>0.03 (+2.16%)</td><td>0.03 (+13.33%)</td><td>0.02 (+6.93%)</td><td>0.00 <b>(-51.16%)</b></td><td>240.10 (-6.47%)</td><td>209.42 (-4.37%)</td><td>203.00 (-11.78%)</td><td>184.70 <b>(+21.04%)</b></td><td>22.93 <b>(-42.05%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.70 (n/a)</td><td>218.98 (n/a)</td><td>230.10 (n/a)</td><td>152.60 (n/a)</td><td>39.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 <b>(+27.47%)</b></td><td>0.07 (+19.91%)</td><td>0.08 <b>(+26.96%)</b></td><td>0.06 (+14.02%)</td><td>0.01 <b>(+102.42%)</b></td><td>173.90 (-12.30%)</td><td>147.90 (-15.45%)</td><td>139.00 <b>(-21.25%)</b></td><td>123.30 <b>(-21.56%)</b></td><td>24.29 <b>(+45.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>174.92 (n/a)</td><td>176.50 (n/a)</td><td>157.20 (n/a)</td><td>16.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(-22.56%)</b></td><td>0.06 <b>(-21.05%)</b></td><td>0.05 (-19.38%)</td><td>0.05 (-19.21%)</td><td>0.01 <b>(-32.16%)</b></td><td>213.70 <b>(+23.74%)</b></td><td>184.20 <b>(+25.60%)</b></td><td>195.60 <b>(+24.03%)</b></td><td>140.30 <b>(+29.19%)</b></td><td>29.00 (+6.48%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>172.70 (n/a)</td><td>146.66 (n/a)</td><td>157.70 (n/a)</td><td>108.60 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-5.44%)</td><td>0.05 (-4.85%)</td><td>0.06 (-4.36%)</td><td>0.04 (+1.87%)</td><td>0.01 (-16.38%)</td><td>265.90 (-1.85%)</td><td>200.36 (+4.01%)</td><td>188.90 (+4.54%)</td><td>165.50 (+5.75%)</td><td>39.60 (-13.67%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>270.90 (n/a)</td><td>192.64 (n/a)</td><td>180.70 (n/a)</td><td>156.50 (n/a)</td><td>45.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 <b>(+56.39%)</b></td><td>0.07 <b>(+25.60%)</b></td><td>0.06 (+9.50%)</td><td>0.05 (+5.25%)</td><td>0.02 <b>(+183.58%)</b></td><td>210.80 (-4.96%)</td><td>164.56 (-16.13%)</td><td>180.60 (-8.65%)</td><td>108.00 <b>(-36.06%)</b></td><td>44.16 <b>(+71.65%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>196.22 (n/a)</td><td>197.70 (n/a)</td><td>168.90 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 <b>(+46.21%)</b></td><td>0.07 <b>(+21.63%)</b></td><td>0.07 (+18.82%)</td><td>0.06 (+10.71%)</td><td>0.02 <b>(+120.61%)</b></td><td>183.20 (-9.66%)</td><td>152.24 (-16.00%)</td><td>161.30 (-15.86%)</td><td>108.20 <b>(-31.61%)</b></td><td>28.39 <b>(+35.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>181.24 (n/a)</td><td>191.70 (n/a)</td><td>158.20 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(-21.08%)</b></td><td>0.06 (-3.27%)</td><td>0.06 (+8.09%)</td><td>0.05 (+13.17%)</td><td>0.01 <b>(-61.80%)</b></td><td>194.10 (-11.61%)</td><td>178.84 (-0.49%)</td><td>179.80 (-7.51%)</td><td>151.50 <b>(+26.67%)</b></td><td>17.09 <b>(-56.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>179.72 (n/a)</td><td>194.40 (n/a)</td><td>119.60 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-12.10%)</td><td>0.05 (+3.75%)</td><td>0.06 (+8.52%)</td><td>0.05 (+14.45%)</td><td>0.01 <b>(-47.91%)</b></td><td>225.90 (-12.65%)</td><td>195.44 (-5.68%)</td><td>186.80 (-7.84%)</td><td>174.40 (+13.76%)</td><td>20.55 <b>(-47.32%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>258.60 (n/a)</td><td>207.22 (n/a)</td><td>202.70 (n/a)</td><td>153.30 (n/a)</td><td>39.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (+7.14%)</td><td>0.05 (+8.70%)</td><td>0.05 (+4.06%)</td><td>0.04 <b>(+43.39%)</b></td><td>0.01 <b>(-40.00%)</b></td><td>239.70 <b>(-30.26%)</b></td><td>212.72 (-10.67%)</td><td>207.00 (-3.94%)</td><td>189.90 (-6.68%)</td><td>22.51 <b>(-62.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>343.70 (n/a)</td><td>238.12 (n/a)</td><td>215.50 (n/a)</td><td>203.50 (n/a)</td><td>59.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (-13.03%)</td><td>0.12 (-0.09%)</td><td>0.12 (+7.40%)</td><td>0.10 (+6.02%)</td><td>0.01 <b>(-51.46%)</b></td><td>204.80 (-5.67%)</td><td>177.06 (-1.81%)</td><td>173.20 (-6.88%)</td><td>159.40 (+14.92%)</td><td>16.92 <b>(-46.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>217.10 (n/a)</td><td>180.32 (n/a)</td><td>186.00 (n/a)</td><td>138.70 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (+16.12%)</td><td>0.12 (+9.30%)</td><td>0.13 <b>(+20.49%)</b></td><td>0.08 <b>(-21.12%)</b></td><td>0.02 <b>(+180.07%)</b></td><td>276.30 <b>(+26.80%)</b></td><td>189.10 (-4.96%)</td><td>167.00 (-17.04%)</td><td>156.00 (-13.86%)</td><td>49.64 <b>(+218.82%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>198.96 (n/a)</td><td>201.30 (n/a)</td><td>181.10 (n/a)</td><td>15.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (-7.36%)</td><td>0.12 (-10.82%)</td><td>0.13 (-3.90%)</td><td>0.10 <b>(-22.05%)</b></td><td>0.02 <b>(+60.86%)</b></td><td>220.20 <b>(+28.25%)</b></td><td>173.82 (+14.46%)</td><td>161.30 (+4.06%)</td><td>142.60 (+7.95%)</td><td>33.82 <b>(+122.36%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>171.70 (n/a)</td><td>151.86 (n/a)</td><td>155.00 (n/a)</td><td>132.10 (n/a)</td><td>15.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (+2.83%)</td><td>0.12 (-4.60%)</td><td>0.12 (-9.43%)</td><td>0.07 <b>(-27.16%)</b></td><td>0.03 <b>(+33.98%)</b></td><td>280.30 <b>(+37.33%)</b></td><td>180.88 (+9.25%)</td><td>172.00 (+10.40%)</td><td>126.20 (-2.70%)</td><td>59.74 <b>(+80.27%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>204.10 (n/a)</td><td>165.56 (n/a)</td><td>155.80 (n/a)</td><td>129.70 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (+10.04%)</td><td>0.13 (+8.38%)</td><td>0.13 (+9.94%)</td><td>0.09 (-5.51%)</td><td>0.02 <b>(+52.29%)</b></td><td>231.00 (+5.82%)</td><td>171.38 (-6.17%)</td><td>161.70 (-9.06%)</td><td>142.20 (-9.08%)</td><td>35.98 <b>(+46.87%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>218.30 (n/a)</td><td>182.64 (n/a)</td><td>177.80 (n/a)</td><td>156.40 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 <b>(-22.71%)</b></td><td>0.11 (-12.73%)</td><td>0.11 (-9.46%)</td><td>0.10 (+0.12%)</td><td>0.01 <b>(-69.68%)</b></td><td>204.40 (-0.15%)</td><td>186.44 (+11.19%)</td><td>187.10 (+10.45%)</td><td>171.30 <b>(+29.38%)</b></td><td>13.52 <b>(-60.41%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>204.70 (n/a)</td><td>167.68 (n/a)</td><td>169.40 (n/a)</td><td>132.40 (n/a)</td><td>34.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 <b>(+21.55%)</b></td><td>0.12 (+0.52%)</td><td>0.12 (-5.71%)</td><td>0.09 (+1.13%)</td><td>0.02 <b>(+40.26%)</b></td><td>236.80 (-1.13%)</td><td>181.30 (+0.64%)</td><td>176.90 (+6.06%)</td><td>132.90 (-17.71%)</td><td>37.03 (+11.33%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>239.50 (n/a)</td><td>180.14 (n/a)</td><td>166.80 (n/a)</td><td>161.50 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (-2.66%)</td><td>0.10 (+9.25%)</td><td>0.10 (+6.88%)</td><td>0.09 <b>(+32.23%)</b></td><td>0.01 <b>(-47.85%)</b></td><td>230.70 <b>(-24.39%)</b></td><td>209.26 (-10.35%)</td><td>208.60 (-6.42%)</td><td>189.10 (+2.72%)</td><td>17.45 <b>(-60.52%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>305.10 (n/a)</td><td>233.42 (n/a)</td><td>222.90 (n/a)</td><td>184.10 (n/a)</td><td>44.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>154.72 (n/a)</td><td>154.90 (n/a)</td><td>125.30 (n/a)</td><td>28.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>172.90 (n/a)</td><td>153.92 (n/a)</td><td>157.50 (n/a)</td><td>133.60 (n/a)</td><td>15.39 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>175.58 (n/a)</td><td>171.50 (n/a)</td><td>138.40 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>215.30 (n/a)</td><td>179.70 (n/a)</td><td>167.90 (n/a)</td><td>161.40 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.10 (n/a)</td><td>168.64 (n/a)</td><td>174.60 (n/a)</td><td>125.20 (n/a)</td><td>38.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.70 (n/a)</td><td>161.76 (n/a)</td><td>148.30 (n/a)</td><td>124.40 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>284.50 (n/a)</td><td>215.00 (n/a)</td><td>244.10 (n/a)</td><td>130.80 (n/a)</td><td>63.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>280.40 (n/a)</td><td>207.80 (n/a)</td><td>183.50 (n/a)</td><td>162.90 (n/a)</td><td>47.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>182.14 (n/a)</td><td>174.70 (n/a)</td><td>171.40 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>223.20 (n/a)</td><td>184.04 (n/a)</td><td>180.80 (n/a)</td><td>149.60 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>209.50 (n/a)</td><td>163.26 (n/a)</td><td>167.00 (n/a)</td><td>117.30 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>204.20 (n/a)</td><td>168.60 (n/a)</td><td>174.40 (n/a)</td><td>113.00 (n/a)</td><td>34.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.36 (+7.89%)</td><td>0.28 (+3.26%)</td><td>0.28 (-7.83%)</td><td>0.23 <b>(+52.05%)</b></td><td>0.05 <b>(-31.69%)</b></td><td>213.00 <b>(-34.22%)</b></td><td>178.90 (-8.62%)</td><td>176.50 (+8.48%)</td><td>137.00 (-7.31%)</td><td>28.74 <b>(-60.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>323.80 (n/a)</td><td>195.78 (n/a)</td><td>162.70 (n/a)</td><td>147.80 (n/a)</td><td>72.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>187.60 (n/a)</td><td>157.32 (n/a)</td><td>157.10 (n/a)</td><td>126.30 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>193.40 (n/a)</td><td>162.34 (n/a)</td><td>156.90 (n/a)</td><td>145.80 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>221.30 (n/a)</td><td>177.56 (n/a)</td><td>165.50 (n/a)</td><td>122.80 (n/a)</td><td>42.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>165.12 (n/a)</td><td>165.80 (n/a)</td><td>139.40 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>158.20 (n/a)</td><td>140.10 (n/a)</td><td>133.20 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>155.64 (n/a)</td><td>143.80 (n/a)</td><td>105.00 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>224.60 (n/a)</td><td>184.70 (n/a)</td><td>176.90 (n/a)</td><td>166.90 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>175.00 (n/a)</td><td>161.66 (n/a)</td><td>167.20 (n/a)</td><td>132.00 (n/a)</td><td>17.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>180.30 (n/a)</td><td>145.88 (n/a)</td><td>135.40 (n/a)</td><td>108.60 (n/a)</td><td>30.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>242.60 (n/a)</td><td>174.70 (n/a)</td><td>171.20 (n/a)</td><td>120.00 (n/a)</td><td>44.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>340.80 (n/a)</td><td>233.06 (n/a)</td><td>211.80 (n/a)</td><td>155.10 (n/a)</td><td>79.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>225.80 (n/a)</td><td>180.96 (n/a)</td><td>169.10 (n/a)</td><td>154.30 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>241.50 (n/a)</td><td>161.62 (n/a)</td><td>147.20 (n/a)</td><td>123.50 (n/a)</td><td>46.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>173.44 (n/a)</td><td>175.20 (n/a)</td><td>138.30 (n/a)</td><td>25.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>186.64 (n/a)</td><td>183.10 (n/a)</td><td>172.90 (n/a)</td><td>17.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>183.20 (n/a)</td><td>157.20 (n/a)</td><td>165.50 (n/a)</td><td>120.10 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>213.70 (n/a)</td><td>185.16 (n/a)</td><td>175.70 (n/a)</td><td>155.90 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>226.90 (n/a)</td><td>194.32 (n/a)</td><td>197.70 (n/a)</td><td>150.90 (n/a)</td><td>33.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>162.30 (n/a)</td><td>149.42 (n/a)</td><td>149.90 (n/a)</td><td>136.30 (n/a)</td><td>10.55 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>161.28 (n/a)</td><td>151.60 (n/a)</td><td>123.20 (n/a)</td><td>41.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.80 (n/a)</td><td>149.72 (n/a)</td><td>158.50 (n/a)</td><td>116.50 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>291.20 (n/a)</td><td>180.96 (n/a)</td><td>160.90 (n/a)</td><td>117.30 (n/a)</td><td>66.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.60 (n/a)</td><td>147.90 (n/a)</td><td>152.90 (n/a)</td><td>111.70 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.20 (n/a)</td><td>177.28 (n/a)</td><td>183.60 (n/a)</td><td>138.20 (n/a)</td><td>26.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.50 (n/a)</td><td>171.94 (n/a)</td><td>171.70 (n/a)</td><td>169.40 (n/a)</td><td>2.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.90 (n/a)</td><td>197.66 (n/a)</td><td>177.40 (n/a)</td><td>173.80 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.80 (n/a)</td><td>173.62 (n/a)</td><td>149.50 (n/a)</td><td>131.30 (n/a)</td><td>68.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>166.64 (n/a)</td><td>162.40 (n/a)</td><td>147.70 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>156.26 (n/a)</td><td>167.90 (n/a)</td><td>113.90 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>150.98 (n/a)</td><td>149.70 (n/a)</td><td>127.90 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>263.10 (n/a)</td><td>162.34 (n/a)</td><td>135.60 (n/a)</td><td>107.50 (n/a)</td><td>61.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>168.72 (n/a)</td><td>178.80 (n/a)</td><td>113.00 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.60 (n/a)</td><td>175.64 (n/a)</td><td>158.10 (n/a)</td><td>144.70 (n/a)</td><td>46.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.50 (n/a)</td><td>191.90 (n/a)</td><td>186.10 (n/a)</td><td>175.40 (n/a)</td><td>14.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>346.00 (n/a)</td><td>192.66 (n/a)</td><td>172.70 (n/a)</td><td>131.60 (n/a)</td><td>88.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>212.00 (n/a)</td><td>158.94 (n/a)</td><td>145.30 (n/a)</td><td>115.30 (n/a)</td><td>42.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>334.60 (n/a)</td><td>194.70 (n/a)</td><td>164.20 (n/a)</td><td>149.40 (n/a)</td><td>78.45 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>156.62 (n/a)</td><td>150.80 (n/a)</td><td>148.30 (n/a)</td><td>12.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.90 (n/a)</td><td>165.32 (n/a)</td><td>169.00 (n/a)</td><td>117.00 (n/a)</td><td>40.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.30 (n/a)</td><td>170.38 (n/a)</td><td>158.40 (n/a)</td><td>140.10 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.40 (n/a)</td><td>186.38 (n/a)</td><td>203.60 (n/a)</td><td>136.20 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.40 (n/a)</td><td>191.64 (n/a)</td><td>191.20 (n/a)</td><td>124.00 (n/a)</td><td>41.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.60 (n/a)</td><td>161.50 (n/a)</td><td>173.40 (n/a)</td><td>125.60 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>245.10 (n/a)</td><td>162.36 (n/a)</td><td>144.10 (n/a)</td><td>125.20 (n/a)</td><td>48.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>243.20 (n/a)</td><td>160.22 (n/a)</td><td>140.90 (n/a)</td><td>129.20 (n/a)</td><td>47.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>186.40 (n/a)</td><td>155.30 (n/a)</td><td>154.70 (n/a)</td><td>125.80 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>273.40 (n/a)</td><td>185.74 (n/a)</td><td>176.00 (n/a)</td><td>132.80 (n/a)</td><td>53.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.40 (n/a)</td><td>172.04 (n/a)</td><td>158.90 (n/a)</td><td>130.70 (n/a)</td><td>42.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>205.90 (n/a)</td><td>166.38 (n/a)</td><td>158.80 (n/a)</td><td>123.30 (n/a)</td><td>37.39 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>321.60 (n/a)</td><td>189.56 (n/a)</td><td>168.10 (n/a)</td><td>135.50 (n/a)</td><td>75.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.18 (-1.21%)</td><td>4.12 (+0.43%)</td><td>4.14 (+0.65%)</td><td>3.99 (+2.08%)</td><td>0.07 <b>(-45.33%)</b></td><td>2354.10 (-2.04%)</td><td>2282.32 (-0.49%)</td><td>2271.90 (-0.65%)</td><td>2248.40 (+1.23%)</td><td>41.28 <b>(-45.39%)</b></td><td>1645.33 (-1.21%)</td><td>1621.31 (+0.43%)</td><td>1628.33 (+0.65%)</td><td>1571.47 (+2.08%)</td><td>28.72 <b>(-45.33%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>4.23 (n/a)</td><td>4.10 (n/a)</td><td>4.11 (n/a)</td><td>3.91 (n/a)</td><td>0.13 (n/a)</td><td>2403.10 (n/a)</td><td>2293.58 (n/a)</td><td>2286.70 (n/a)</td><td>2221.10 (n/a)</td><td>75.58 (n/a)</td><td>1665.53 (n/a)</td><td>1614.30 (n/a)</td><td>1617.76 (n/a)</td><td>1539.43 (n/a)</td><td>52.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.10 (+14.64%)</td><td>0.97 <b>(+25.04%)</b></td><td>1.03 <b>(+53.42%)</b></td><td>0.75 (+18.05%)</td><td>0.14 (-11.05%)</td><td>294.50 (-15.28%)</td><td>233.06 <b>(-20.98%)</b></td><td>213.80 <b>(-34.82%)</b></td><td>201.70 (-12.76%)</td><td>37.32 <b>(-32.29%)</b></td><td>46.80 (+14.64%)</td><td>41.24 <b>(+25.04%)</b></td><td>44.14 <b>(+53.42%)</b></td><td>32.05 (+18.05%)</td><td>5.85 (-11.05%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.96 (n/a)</td><td>0.77 (n/a)</td><td>0.67 (n/a)</td><td>0.64 (n/a)</td><td>0.15 (n/a)</td><td>347.60 (n/a)</td><td>294.92 (n/a)</td><td>328.00 (n/a)</td><td>231.20 (n/a)</td><td>55.12 (n/a)</td><td>40.82 (n/a)</td><td>32.98 (n/a)</td><td>28.77 (n/a)</td><td>27.15 (n/a)</td><td>6.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.19 (-1.01%)</td><td>1.00 (+1.73%)</td><td>1.05 (+10.05%)</td><td>0.68 (-18.46%)</td><td>0.19 <b>(+41.09%)</b></td><td>325.20 <b>(+22.62%)</b></td><td>229.28 (+0.53%)</td><td>211.30 (-9.16%)</td><td>185.90 (+0.98%)</td><td>54.78 <b>(+88.48%)</b></td><td>50.76 (-1.01%)</td><td>42.69 (+1.73%)</td><td>44.66 (+10.05%)</td><td>29.02 (-18.46%)</td><td>8.10 <b>(+41.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.20 (n/a)</td><td>0.98 (n/a)</td><td>0.95 (n/a)</td><td>0.83 (n/a)</td><td>0.13 (n/a)</td><td>265.20 (n/a)</td><td>228.06 (n/a)</td><td>232.60 (n/a)</td><td>184.10 (n/a)</td><td>29.07 (n/a)</td><td>51.28 (n/a)</td><td>41.96 (n/a)</td><td>40.58 (n/a)</td><td>35.58 (n/a)</td><td>5.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.52 (-0.74%)</td><td>0.52 (-0.16%)</td><td>0.52 (-0.16%)</td><td>0.52 (+0.01%)</td><td>0.00 <b>(-69.28%)</b></td><td>48618.00 (-0.01%)</td><td>48513.76 (+0.16%)</td><td>48504.80 (+0.16%)</td><td>48456.60 (+0.75%)</td><td>65.02 <b>(-69.05%)</b></td><td>354.54 (-0.74%)</td><td>354.12 (-0.16%)</td><td>354.19 (-0.16%)</td><td>353.36 (+0.01%)</td><td>0.47 <b>(-69.28%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48621.90 (n/a)</td><td>48434.50 (n/a)</td><td>48429.30 (n/a)</td><td>48098.00 (n/a)</td><td>210.06 (n/a)</td><td>357.18 (n/a)</td><td>354.71 (n/a)</td><td>354.74 (n/a)</td><td>353.34 (n/a)</td><td>1.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.21 (-2.11%)</td><td>0.21 (-0.90%)</td><td>0.21 (-0.63%)</td><td>0.21 (-1.31%)</td><td>0.00 <b>(-27.93%)</b></td><td>120815.90 (+1.33%)</td><td>118435.64 (+0.90%)</td><td>117914.70 (+0.63%)</td><td>117332.40 (+2.15%)</td><td>1380.43 <b>(-25.44%)</b></td><td>146.42 (-2.11%)</td><td>145.07 (-0.90%)</td><td>145.70 (-0.63%)</td><td>142.20 (-1.31%)</td><td>1.67 <b>(-27.93%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119234.00 (n/a)</td><td>117381.82 (n/a)</td><td>117175.70 (n/a)</td><td>114861.50 (n/a)</td><td>1851.48 (n/a)</td><td>149.57 (n/a)</td><td>146.39 (n/a)</td><td>146.62 (n/a)</td><td>144.09 (n/a)</td><td>2.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.90 (+0.63%)</td><td>0.89 (+0.36%)</td><td>0.88 (+0.21%)</td><td>0.88 (+0.30%)</td><td>0.01 <b>(+30.53%)</b></td><td>28586.80 (-0.30%)</td><td>28380.12 (-0.35%)</td><td>28439.20 (-0.21%)</td><td>28023.60 (-0.63%)</td><td>233.38 <b>(+29.44%)</b></td><td>613.05 (+0.63%)</td><td>605.38 (+0.36%)</td><td>604.09 (+0.21%)</td><td>600.97 (+0.30%)</td><td>5.00 <b>(+30.53%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28671.60 (n/a)</td><td>28481.16 (n/a)</td><td>28499.80 (n/a)</td><td>28201.10 (n/a)</td><td>180.30 (n/a)</td><td>609.19 (n/a)</td><td>603.22 (n/a)</td><td>602.81 (n/a)</td><td>599.19 (n/a)</td><td>3.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.53 (-1.89%)</td><td>3.45 (-1.94%)</td><td>3.47 (-2.48%)</td><td>3.36 (+0.82%)</td><td>0.08 <b>(-24.07%)</b></td><td>7492.40 (-0.81%)</td><td>7302.26 (+1.94%)</td><td>7262.00 (+2.54%)</td><td>7128.30 (+1.92%)</td><td>171.16 <b>(-23.56%)</b></td><td>2410.11 (-1.89%)</td><td>2353.71 (-1.94%)</td><td>2365.71 (-2.48%)</td><td>2292.99 (+0.82%)</td><td>54.96 <b>(-24.07%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.60 (n/a)</td><td>3.52 (n/a)</td><td>3.55 (n/a)</td><td>3.33 (n/a)</td><td>0.11 (n/a)</td><td>7553.60 (n/a)</td><td>7163.10 (n/a)</td><td>7081.90 (n/a)</td><td>6993.80 (n/a)</td><td>223.91 (n/a)</td><td>2456.43 (n/a)</td><td>2400.20 (n/a)</td><td>2425.89 (n/a)</td><td>2274.40 (n/a)</td><td>72.38 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.03 (-1.60%)</td><td>2.85 (-0.03%)</td><td>2.82 (-0.80%)</td><td>2.74 (+0.03%)</td><td>0.11 (-16.08%)</td><td>9173.10 (-0.03%)</td><td>8834.64 (-0.02%)</td><td>8924.40 (+0.81%)</td><td>8303.60 (+1.62%)</td><td>345.99 (-14.73%)</td><td>2068.96 (-1.60%)</td><td>1947.05 (-0.03%)</td><td>1925.04 (-0.80%)</td><td>1872.86 (+0.03%)</td><td>78.18 (-16.09%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.08 (n/a)</td><td>2.85 (n/a)</td><td>2.84 (n/a)</td><td>2.74 (n/a)</td><td>0.14 (n/a)</td><td>9175.70 (n/a)</td><td>8836.44 (n/a)</td><td>8852.80 (n/a)</td><td>8171.00 (n/a)</td><td>405.74 (n/a)</td><td>2102.54 (n/a)</td><td>1947.63 (n/a)</td><td>1940.61 (n/a)</td><td>1872.32 (n/a)</td><td>93.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.31 (+3.19%)</td><td>3.19 (+0.63%)</td><td>3.17 (+0.41%)</td><td>3.10 (-1.38%)</td><td>0.08 <b>(+200.22%)</b></td><td>8111.20 (+1.40%)</td><td>7903.00 (-0.59%)</td><td>7931.40 (-0.41%)</td><td>7602.30 (-3.09%)</td><td>184.85 <b>(+193.57%)</b></td><td>2259.81 (+3.19%)</td><td>2174.81 (+0.63%)</td><td>2166.06 (+0.41%)</td><td>2118.03 (-1.38%)</td><td>51.77 <b>(+200.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.21 (n/a)</td><td>3.17 (n/a)</td><td>3.16 (n/a)</td><td>3.15 (n/a)</td><td>0.03 (n/a)</td><td>7999.50 (n/a)</td><td>7949.84 (n/a)</td><td>7964.10 (n/a)</td><td>7844.80 (n/a)</td><td>62.97 (n/a)</td><td>2189.97 (n/a)</td><td>2161.15 (n/a)</td><td>2157.17 (n/a)</td><td>2147.63 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.79 (+0.32%)</td><td>0.79 (+0.10%)</td><td>0.79 (+0.00%)</td><td>0.79 (+0.07%)</td><td>0.00 <b>(+141.23%)</b></td><td>96154.70 (-0.07%)</td><td>96050.10 (-0.10%)</td><td>96109.20 (-0.00%)</td><td>95780.50 (-0.32%)</td><td>152.32 <b>(+140.16%)</b></td><td>717.47 (+0.32%)</td><td>715.46 (+0.10%)</td><td>715.01 (+0.00%)</td><td>714.68 (+0.07%)</td><td>1.14 <b>(+141.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96221.30 (n/a)</td><td>96148.08 (n/a)</td><td>96112.00 (n/a)</td><td>96087.70 (n/a)</td><td>63.43 (n/a)</td><td>715.17 (n/a)</td><td>714.73 (n/a)</td><td>714.99 (n/a)</td><td>714.18 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.73 (-0.02%)</td><td>0.73 (+0.05%)</td><td>0.73 (+0.01%)</td><td>0.73 (+0.14%)</td><td>0.00 <b>(-62.86%)</b></td><td>103383.90 (-0.14%)</td><td>103315.48 (-0.05%)</td><td>103306.30 (-0.01%)</td><td>103287.60 (+0.02%)</td><td>39.43 <b>(-62.90%)</b></td><td>665.32 (-0.02%)</td><td>665.14 (+0.05%)</td><td>665.20 (+0.01%)</td><td>664.70 (+0.14%)</td><td>0.25 <b>(-62.86%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103531.80 (n/a)</td><td>103369.64 (n/a)</td><td>103316.50 (n/a)</td><td>103266.20 (n/a)</td><td>106.29 (n/a)</td><td>665.46 (n/a)</td><td>664.79 (n/a)</td><td>665.14 (n/a)</td><td>663.75 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.70 (-0.56%)</td><td>0.70 (-0.21%)</td><td>0.69 (-0.12%)</td><td>0.69 (-0.10%)</td><td>0.00 <b>(-45.46%)</b></td><td>108873.00 (+0.10%)</td><td>108581.66 (+0.21%)</td><td>108633.10 (+0.12%)</td><td>108265.80 (+0.56%)</td><td>229.38 <b>(-45.06%)</b></td><td>634.73 (-0.56%)</td><td>632.89 (-0.21%)</td><td>632.58 (-0.12%)</td><td>631.19 (-0.10%)</td><td>1.34 <b>(-45.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108765.70 (n/a)</td><td>108355.58 (n/a)</td><td>108498.20 (n/a)</td><td>107658.40 (n/a)</td><td>417.54 (n/a)</td><td>638.31 (n/a)</td><td>634.21 (n/a)</td><td>633.37 (n/a)</td><td>631.81 (n/a)</td><td>2.45 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.74 (+1.78%)</td><td>7.23 (+7.74%)</td><td>7.16 (+3.02%)</td><td>6.69 <b>(+36.30%)</b></td><td>0.42 <b>(-60.70%)</b></td><td>1331.40 <b>(-26.63%)</b></td><td>1235.30 (-9.18%)</td><td>1244.20 (-2.93%)</td><td>1152.10 (-1.75%)</td><td>71.54 <b>(-72.55%)</b></td><td>466.00 (+1.78%)</td><td>435.77 (+7.74%)</td><td>431.51 (+3.02%)</td><td>403.25 <b>(+36.30%)</b></td><td>25.13 <b>(-60.70%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.60 (n/a)</td><td>6.71 (n/a)</td><td>6.95 (n/a)</td><td>4.91 (n/a)</td><td>1.06 (n/a)</td><td>1814.70 (n/a)</td><td>1360.14 (n/a)</td><td>1281.80 (n/a)</td><td>1172.60 (n/a)</td><td>260.57 (n/a)</td><td>457.86 (n/a)</td><td>404.48 (n/a)</td><td>418.86 (n/a)</td><td>295.84 (n/a)</td><td>63.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.07 (+1.80%)</td><td>6.39 (-4.99%)</td><td>6.63 (-2.72%)</td><td>4.66 <b>(-27.36%)</b></td><td>1.00 <b>(+314.09%)</b></td><td>1913.90 <b>(+37.67%)</b></td><td>1429.86 (+7.72%)</td><td>1343.30 (+2.79%)</td><td>1261.20 (-1.78%)</td><td>274.64 <b>(+470.69%)</b></td><td>425.67 (+1.80%)</td><td>384.67 (-4.99%)</td><td>399.65 (-2.72%)</td><td>280.51 <b>(-27.36%)</b></td><td>60.05 <b>(+314.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.94 (n/a)</td><td>6.72 (n/a)</td><td>6.82 (n/a)</td><td>6.41 (n/a)</td><td>0.24 (n/a)</td><td>1390.20 (n/a)</td><td>1327.44 (n/a)</td><td>1306.80 (n/a)</td><td>1284.00 (n/a)</td><td>48.12 (n/a)</td><td>418.14 (n/a)</td><td>404.86 (n/a)</td><td>410.82 (n/a)</td><td>386.17 (n/a)</td><td>14.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.08 (-2.31%)</td><td>6.49 (-5.89%)</td><td>6.57 (-4.86%)</td><td>6.06 (-8.85%)</td><td>0.42 <b>(+67.36%)</b></td><td>1470.50 (+9.71%)</td><td>1378.16 (+6.51%)</td><td>1356.30 (+5.12%)</td><td>1259.50 (+2.37%)</td><td>89.02 <b>(+88.81%)</b></td><td>426.26 (-2.31%)</td><td>390.87 (-5.89%)</td><td>395.83 (-4.86%)</td><td>365.09 (-8.85%)</td><td>25.52 <b>(+67.36%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.24 (n/a)</td><td>6.90 (n/a)</td><td>6.91 (n/a)</td><td>6.65 (n/a)</td><td>0.25 (n/a)</td><td>1340.40 (n/a)</td><td>1293.98 (n/a)</td><td>1290.30 (n/a)</td><td>1230.40 (n/a)</td><td>47.15 (n/a)</td><td>436.33 (n/a)</td><td>415.34 (n/a)</td><td>416.07 (n/a)</td><td>400.52 (n/a)</td><td>15.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.48 (+5.23%)</td><td>8.04 (+6.66%)</td><td>7.96 (+4.50%)</td><td>7.79 (+9.73%)</td><td>0.27 <b>(-29.39%)</b></td><td>4475.80 (-8.87%)</td><td>4338.92 (-6.36%)</td><td>4379.40 (-4.31%)</td><td>4111.90 (-4.98%)</td><td>141.49 <b>(-39.30%)</b></td><td>522.26 (+5.23%)</td><td>495.37 (+6.66%)</td><td>490.36 (+4.50%)</td><td>479.80 (+9.73%)</td><td>16.57 <b>(-29.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.06 (n/a)</td><td>7.54 (n/a)</td><td>7.62 (n/a)</td><td>7.10 (n/a)</td><td>0.38 (n/a)</td><td>4911.40 (n/a)</td><td>4633.42 (n/a)</td><td>4576.60 (n/a)</td><td>4327.20 (n/a)</td><td>233.10 (n/a)</td><td>496.28 (n/a)</td><td>464.42 (n/a)</td><td>469.23 (n/a)</td><td>437.24 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.57 (-3.81%)</td><td>7.34 (-1.29%)</td><td>7.48 (-1.64%)</td><td>7.03 (+2.01%)</td><td>0.24 <b>(-38.30%)</b></td><td>4961.50 (-1.97%)</td><td>4751.72 (+1.17%)</td><td>4662.30 (+1.67%)</td><td>4603.70 (+3.96%)</td><td>157.25 <b>(-37.32%)</b></td><td>466.47 (-3.81%)</td><td>452.33 (-1.29%)</td><td>460.61 (-1.64%)</td><td>432.83 (+2.01%)</td><td>14.78 <b>(-38.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.87 (n/a)</td><td>7.44 (n/a)</td><td>7.60 (n/a)</td><td>6.89 (n/a)</td><td>0.39 (n/a)</td><td>5061.30 (n/a)</td><td>4696.92 (n/a)</td><td>4585.70 (n/a)</td><td>4428.20 (n/a)</td><td>250.87 (n/a)</td><td>484.95 (n/a)</td><td>458.23 (n/a)</td><td>468.30 (n/a)</td><td>424.30 (n/a)</td><td>23.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>7.43 (-5.24%)</td><td>7.06 (-0.48%)</td><td>7.06 (+1.39%)</td><td>6.70 (+1.69%)</td><td>0.30 <b>(-37.43%)</b></td><td>5202.70 (-1.66%)</td><td>4943.88 (+0.28%)</td><td>4937.60 (-1.37%)</td><td>4694.60 (+5.53%)</td><td>207.87 <b>(-34.58%)</b></td><td>457.44 (-5.24%)</td><td>434.99 (-0.48%)</td><td>434.93 (+1.39%)</td><td>412.76 (+1.69%)</td><td>18.28 <b>(-37.43%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.84 (n/a)</td><td>7.10 (n/a)</td><td>6.96 (n/a)</td><td>6.59 (n/a)</td><td>0.47 (n/a)</td><td>5290.50 (n/a)</td><td>4929.94 (n/a)</td><td>5006.10 (n/a)</td><td>4448.60 (n/a)</td><td>317.74 (n/a)</td><td>482.73 (n/a)</td><td>437.10 (n/a)</td><td>428.98 (n/a)</td><td>405.91 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.79 (+0.00%)</td><td>0.79 (+0.05%)</td><td>0.79 (+0.01%)</td><td>0.79 (+0.17%)</td><td>0.00 <b>(-69.77%)</b></td><td>95434.80 (-0.17%)</td><td>95398.28 (-0.05%)</td><td>95404.80 (-0.01%)</td><td>95370.80 (-0.00%)</td><td>26.63 <b>(-69.79%)</b></td><td>720.55 (+0.00%)</td><td>720.34 (+0.05%)</td><td>720.29 (+0.01%)</td><td>720.07 (+0.17%)</td><td>0.20 <b>(-69.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95595.20 (n/a)</td><td>95443.20 (n/a)</td><td>95416.10 (n/a)</td><td>95371.20 (n/a)</td><td>88.17 (n/a)</td><td>720.55 (n/a)</td><td>720.00 (n/a)</td><td>720.21 (n/a)</td><td>718.86 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.74 (-0.33%)</td><td>0.74 (-0.09%)</td><td>0.74 (-0.02%)</td><td>0.74 (-0.04%)</td><td>0.00 <b>(-81.04%)</b></td><td>102622.90 (+0.04%)</td><td>102578.24 (+0.08%)</td><td>102579.50 (+0.02%)</td><td>102536.80 (+0.33%)</td><td>31.20 <b>(-80.97%)</b></td><td>670.19 (-0.33%)</td><td>669.92 (-0.09%)</td><td>669.91 (-0.02%)</td><td>669.63 (-0.04%)</td><td>0.20 <b>(-81.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102584.80 (n/a)</td><td>102491.22 (n/a)</td><td>102557.00 (n/a)</td><td>102198.90 (n/a)</td><td>163.90 (n/a)</td><td>672.41 (n/a)</td><td>670.49 (n/a)</td><td>670.06 (n/a)</td><td>669.88 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.71 (+0.26%)</td><td>0.70 (+0.08%)</td><td>0.70 (-0.08%)</td><td>0.70 (-0.03%)</td><td>0.00 <b>(+122.02%)</b></td><td>107662.50 (+0.03%)</td><td>107394.78 (-0.08%)</td><td>107519.30 (+0.08%)</td><td>107087.50 (-0.26%)</td><td>249.61 <b>(+121.38%)</b></td><td>641.71 (+0.26%)</td><td>639.88 (+0.08%)</td><td>639.14 (-0.08%)</td><td>638.29 (-0.03%)</td><td>1.49 <b>(+122.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107627.70 (n/a)</td><td>107485.62 (n/a)</td><td>107431.90 (n/a)</td><td>107364.80 (n/a)</td><td>112.75 (n/a)</td><td>640.06 (n/a)</td><td>639.34 (n/a)</td><td>639.66 (n/a)</td><td>638.49 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.09 (-0.45%)</td><td>3.57 (-0.44%)</td><td>3.65 (+0.73%)</td><td>3.10 (+7.60%)</td><td>0.41 (-14.10%)</td><td>2601.90 (-7.07%)</td><td>2284.50 (-0.03%)</td><td>2206.40 (-0.73%)</td><td>1969.50 (+0.45%)</td><td>263.71 (-19.46%)</td><td>1073.33 (-0.45%)</td><td>935.23 (-0.44%)</td><td>958.08 (+0.73%)</td><td>812.45 (+7.60%)</td><td>107.44 (-14.10%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>4.11 (n/a)</td><td>3.58 (n/a)</td><td>3.63 (n/a)</td><td>2.88 (n/a)</td><td>0.48 (n/a)</td><td>2799.70 (n/a)</td><td>2285.12 (n/a)</td><td>2222.60 (n/a)</td><td>1960.70 (n/a)</td><td>327.41 (n/a)</td><td>1078.14 (n/a)</td><td>939.34 (n/a)</td><td>951.11 (n/a)</td><td>755.07 (n/a)</td><td>125.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.41 <b>(-20.45%)</b></td><td>0.34 <b>(-28.14%)</b></td><td>0.33 <b>(-34.46%)</b></td><td>0.28 (-12.64%)</td><td>0.05 <b>(-41.45%)</b></td><td>4375.70 (+14.47%)</td><td>3755.82 <b>(+36.90%)</b></td><td>3802.90 <b>(+52.58%)</b></td><td>3008.80 <b>(+25.71%)</b></td><td>489.58 (-19.42%)</td><td>22.30 <b>(-20.45%)</b></td><td>18.13 <b>(-28.14%)</b></td><td>17.65 <b>(-34.46%)</b></td><td>15.34 (-12.64%)</td><td>2.55 <b>(-41.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>3822.60 (n/a)</td><td>2743.56 (n/a)</td><td>2492.40 (n/a)</td><td>2393.50 (n/a)</td><td>607.56 (n/a)</td><td>28.04 (n/a)</td><td>25.23 (n/a)</td><td>26.93 (n/a)</td><td>17.56 (n/a)</td><td>4.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.92 <b>(-29.63%)</b></td><td>4.41 (-16.13%)</td><td>4.66 (-4.00%)</td><td>3.79 (-19.38%)</td><td>0.49 <b>(-49.80%)</b></td><td>1754.50 <b>(+24.05%)</b></td><td>1522.18 (+17.80%)</td><td>1428.90 (+4.17%)</td><td>1352.40 <b>(+42.10%)</b></td><td>174.68 (-9.25%)</td><td>1519.64 <b>(-29.63%)</b></td><td>1363.96 (-16.13%)</td><td>1438.35 (-4.00%)</td><td>1171.42 (-19.38%)</td><td>150.48 <b>(-49.80%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.99 (n/a)</td><td>5.26 (n/a)</td><td>4.85 (n/a)</td><td>4.70 (n/a)</td><td>0.97 (n/a)</td><td>1414.40 (n/a)</td><td>1292.14 (n/a)</td><td>1371.70 (n/a)</td><td>951.70 (n/a)</td><td>192.49 (n/a)</td><td>2159.44 (n/a)</td><td>1626.20 (n/a)</td><td>1498.26 (n/a)</td><td>1453.04 (n/a)</td><td>299.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.44 (n/a)</td><td>12.25 (n/a)</td><td>12.29 (n/a)</td><td>10.66 (n/a)</td><td>1.12 (n/a)</td><td>13.43 (n/a)</td><td>12.24 (n/a)</td><td>12.28 (n/a)</td><td>10.65 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>24.73 (-1.02%)</td><td>24.24 (-0.59%)</td><td>24.28 (-0.28%)</td><td>23.79 (+1.47%)</td><td>0.38 <b>(-40.36%)</b></td><td>24.72 (-1.02%)</td><td>24.23 (-0.59%)</td><td>24.27 (-0.28%)</td><td>23.77 (+1.47%)</td><td>0.38 <b>(-40.36%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>24.99 (n/a)</td><td>24.39 (n/a)</td><td>24.35 (n/a)</td><td>23.44 (n/a)</td><td>0.65 (n/a)</td><td>24.97 (n/a)</td><td>24.37 (n/a)</td><td>24.34 (n/a)</td><td>23.43 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>45.26 (+3.80%)</td><td>41.78 (+1.75%)</td><td>41.40 (+2.39%)</td><td>39.33 (+0.49%)</td><td>2.29 <b>(+23.97%)</b></td><td>45.23 (+3.80%)</td><td>41.76 (+1.75%)</td><td>41.37 (+2.39%)</td><td>39.31 (+0.49%)</td><td>2.29 <b>(+23.97%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>43.60 (n/a)</td><td>41.06 (n/a)</td><td>40.43 (n/a)</td><td>39.14 (n/a)</td><td>1.85 (n/a)</td><td>43.57 (n/a)</td><td>41.04 (n/a)</td><td>40.41 (n/a)</td><td>39.12 (n/a)</td><td>1.85 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>45.87 (+0.74%)</td><td>43.49 (+3.89%)</td><td>43.25 (+4.53%)</td><td>42.14 (+6.43%)</td><td>1.42 <b>(-36.29%)</b></td><td>45.84 (+0.74%)</td><td>43.46 (+3.89%)</td><td>43.22 (+4.53%)</td><td>42.11 (+6.43%)</td><td>1.42 <b>(-36.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>45.53 (n/a)</td><td>41.86 (n/a)</td><td>41.37 (n/a)</td><td>39.59 (n/a)</td><td>2.24 (n/a)</td><td>45.50 (n/a)</td><td>41.84 (n/a)</td><td>41.35 (n/a)</td><td>39.57 (n/a)</td><td>2.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.54 (n/a)</td><td>13.17 (n/a)</td><td>13.23 (n/a)</td><td>12.73 (n/a)</td><td>0.33 (n/a)</td><td>13.53 (n/a)</td><td>13.16 (n/a)</td><td>13.22 (n/a)</td><td>12.72 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>24.95 (+0.58%)</td><td>24.25 (+1.96%)</td><td>24.06 (+1.86%)</td><td>23.54 (+2.32%)</td><td>0.56 <b>(-21.81%)</b></td><td>24.93 (+0.58%)</td><td>24.24 (+1.96%)</td><td>24.05 (+1.86%)</td><td>23.53 (+2.32%)</td><td>0.56 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>24.80 (n/a)</td><td>23.79 (n/a)</td><td>23.62 (n/a)</td><td>23.01 (n/a)</td><td>0.71 (n/a)</td><td>24.79 (n/a)</td><td>23.77 (n/a)</td><td>23.61 (n/a)</td><td>22.99 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>42.21 (+0.64%)</td><td>41.14 (+2.04%)</td><td>40.82 (+2.51%)</td><td>40.38 (+3.40%)</td><td>0.77 <b>(-34.71%)</b></td><td>42.18 (+0.64%)</td><td>41.11 (+2.04%)</td><td>40.80 (+2.51%)</td><td>40.35 (+3.40%)</td><td>0.77 <b>(-34.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>41.94 (n/a)</td><td>40.31 (n/a)</td><td>39.82 (n/a)</td><td>39.05 (n/a)</td><td>1.19 (n/a)</td><td>41.91 (n/a)</td><td>40.29 (n/a)</td><td>39.80 (n/a)</td><td>39.03 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>46.64 (+1.54%)</td><td>41.46 (-5.32%)</td><td>42.78 (-1.62%)</td><td>29.89 <b>(-28.79%)</b></td><td>6.71 <b>(+327.29%)</b></td><td>46.61 (+1.54%)</td><td>41.44 (-5.32%)</td><td>42.75 (-1.62%)</td><td>29.87 <b>(-28.79%)</b></td><td>6.70 <b>(+327.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>45.93 (n/a)</td><td>43.79 (n/a)</td><td>43.49 (n/a)</td><td>41.97 (n/a)</td><td>1.57 (n/a)</td><td>45.90 (n/a)</td><td>43.77 (n/a)</td><td>43.46 (n/a)</td><td>41.94 (n/a)</td><td>1.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>9.88 (-1.86%)</td><td>9.11 (+4.61%)</td><td>8.87 (+5.61%)</td><td>8.51 (+9.24%)</td><td>0.61 <b>(-32.00%)</b></td><td>9.86 (-1.86%)</td><td>9.09 (+4.61%)</td><td>8.85 (+5.61%)</td><td>8.50 (+9.24%)</td><td>0.61 <b>(-32.00%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>10.06 (n/a)</td><td>8.71 (n/a)</td><td>8.40 (n/a)</td><td>7.79 (n/a)</td><td>0.89 (n/a)</td><td>10.04 (n/a)</td><td>8.69 (n/a)</td><td>8.38 (n/a)</td><td>7.78 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.97 (-7.88%)</td><td>0.91 (+6.80%)</td><td>0.94 (+10.94%)</td><td>0.80 (+12.12%)</td><td>0.07 <b>(-46.56%)</b></td><td>0.96 (-7.88%)</td><td>0.90 (+6.80%)</td><td>0.93 (+10.94%)</td><td>0.79 (+12.12%)</td><td>0.07 <b>(-46.56%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.06 (n/a)</td><td>0.86 (n/a)</td><td>0.85 (n/a)</td><td>0.71 (n/a)</td><td>0.13 (n/a)</td><td>1.04 (n/a)</td><td>0.84 (n/a)</td><td>0.84 (n/a)</td><td>0.70 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.24 (+2.19%)</td><td>1.15 (+2.80%)</td><td>1.17 (+5.17%)</td><td>0.96 (-3.46%)</td><td>0.11 (+15.59%)</td><td>1.23 (+2.19%)</td><td>1.14 (+2.80%)</td><td>1.16 (+5.17%)</td><td>0.95 (-3.46%)</td><td>0.11 (+15.59%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.21 (n/a)</td><td>1.12 (n/a)</td><td>1.11 (n/a)</td><td>0.99 (n/a)</td><td>0.10 (n/a)</td><td>1.20 (n/a)</td><td>1.10 (n/a)</td><td>1.10 (n/a)</td><td>0.98 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>18.52 (+5.65%)</td><td>16.23 (-3.52%)</td><td>16.60 (-1.75%)</td><td>14.52 (-8.31%)</td><td>1.66 <b>(+122.22%)</b></td><td>18.31 (+5.65%)</td><td>16.04 (-3.52%)</td><td>16.41 (-1.75%)</td><td>14.35 (-8.31%)</td><td>1.64 <b>(+122.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>17.53 (n/a)</td><td>16.82 (n/a)</td><td>16.90 (n/a)</td><td>15.84 (n/a)</td><td>0.75 (n/a)</td><td>17.33 (n/a)</td><td>16.63 (n/a)</td><td>16.70 (n/a)</td><td>15.65 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.71 (-3.19%)</td><td>11.06 (-12.77%)</td><td>12.83 (-4.88%)</td><td>7.51 (-13.80%)</td><td>3.05 <b>(+36.10%)</b></td><td>13.47 (-3.19%)</td><td>10.87 (-12.77%)</td><td>12.61 (-4.88%)</td><td>7.38 (-13.80%)</td><td>3.00 <b>(+36.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.16 (n/a)</td><td>12.68 (n/a)</td><td>13.49 (n/a)</td><td>8.71 (n/a)</td><td>2.24 (n/a)</td><td>13.91 (n/a)</td><td>12.46 (n/a)</td><td>13.26 (n/a)</td><td>8.56 (n/a)</td><td>2.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>9.67 <b>(+25.87%)</b></td><td>8.76 <b>(+26.57%)</b></td><td>9.00 (+19.70%)</td><td>7.32 <b>(+26.18%)</b></td><td>0.92 (-2.06%)</td><td>9.50 <b>(+25.87%)</b></td><td>8.61 <b>(+26.57%)</b></td><td>8.84 (+19.70%)</td><td>7.20 <b>(+26.18%)</b></td><td>0.90 (-2.06%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.68 (n/a)</td><td>6.92 (n/a)</td><td>7.52 (n/a)</td><td>5.80 (n/a)</td><td>0.94 (n/a)</td><td>7.55 (n/a)</td><td>6.80 (n/a)</td><td>7.39 (n/a)</td><td>5.70 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.65 (+4.72%)</td><td>5.64 (-2.12%)</td><td>5.39 (-6.30%)</td><td>5.31 (-0.44%)</td><td>0.57 <b>(+53.18%)</b></td><td>6.54 (+4.72%)</td><td>5.55 (-2.12%)</td><td>5.30 (-6.30%)</td><td>5.22 (-0.44%)</td><td>0.56 <b>(+53.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.35 (n/a)</td><td>5.76 (n/a)</td><td>5.75 (n/a)</td><td>5.33 (n/a)</td><td>0.37 (n/a)</td><td>6.25 (n/a)</td><td>5.67 (n/a)</td><td>5.66 (n/a)</td><td>5.25 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.20 (n/a)</td><td>12.29 (n/a)</td><td>12.37 (n/a)</td><td>11.26 (n/a)</td><td>0.73 (n/a)</td><td>13.19 (n/a)</td><td>12.28 (n/a)</td><td>12.36 (n/a)</td><td>11.26 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.29 (n/a)</td><td>12.02 (n/a)</td><td>11.70 (n/a)</td><td>10.92 (n/a)</td><td>1.03 (n/a)</td><td>13.28 (n/a)</td><td>12.01 (n/a)</td><td>11.69 (n/a)</td><td>10.92 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.30 (n/a)</td><td>156.82 (n/a)</td><td>162.30 (n/a)</td><td>137.50 (n/a)</td><td>12.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.90 (n/a)</td><td>164.30 (n/a)</td><td>153.90 (n/a)</td><td>149.40 (n/a)</td><td>18.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>159.36 (n/a)</td><td>157.80 (n/a)</td><td>133.60 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>144.24 (n/a)</td><td>131.00 (n/a)</td><td>121.00 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>151.86 (n/a)</td><td>146.70 (n/a)</td><td>126.70 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>326.90 (n/a)</td><td>245.48 (n/a)</td><td>277.50 (n/a)</td><td>115.60 (n/a)</td><td>87.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.30 (n/a)</td><td>201.24 (n/a)</td><td>206.30 (n/a)</td><td>151.10 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>349.00 (n/a)</td><td>213.70 (n/a)</td><td>189.20 (n/a)</td><td>159.40 (n/a)</td><td>77.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>163.70 (n/a)</td><td>148.66 (n/a)</td><td>160.60 (n/a)</td><td>116.80 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>170.80 (n/a)</td><td>158.96 (n/a)</td><td>164.60 (n/a)</td><td>141.20 (n/a)</td><td>13.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>137.80 (n/a)</td><td>126.70 (n/a)</td><td>118.60 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>180.04 (n/a)</td><td>193.80 (n/a)</td><td>140.70 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.50 (n/a)</td><td>162.78 (n/a)</td><td>168.50 (n/a)</td><td>141.40 (n/a)</td><td>13.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>184.24 (n/a)</td><td>186.10 (n/a)</td><td>124.00 (n/a)</td><td>42.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.30 (n/a)</td><td>197.48 (n/a)</td><td>191.60 (n/a)</td><td>181.00 (n/a)</td><td>20.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>284.10 (n/a)</td><td>208.58 (n/a)</td><td>221.30 (n/a)</td><td>122.90 (n/a)</td><td>58.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>188.56 (n/a)</td><td>192.40 (n/a)</td><td>157.40 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>174.70 (n/a)</td><td>174.80 (n/a)</td><td>159.20 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.70 (n/a)</td><td>166.84 (n/a)</td><td>161.10 (n/a)</td><td>135.90 (n/a)</td><td>27.55 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>172.68 (n/a)</td><td>166.60 (n/a)</td><td>154.10 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>185.20 (n/a)</td><td>180.30 (n/a)</td><td>163.70 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>164.32 (n/a)</td><td>160.40 (n/a)</td><td>139.30 (n/a)</td><td>17.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>171.54 (n/a)</td><td>167.50 (n/a)</td><td>155.50 (n/a)</td><td>17.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>197.96 (n/a)</td><td>203.60 (n/a)</td><td>152.40 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>200.20 (n/a)</td><td>160.20 (n/a)</td><td>176.70 (n/a)</td><td>117.80 (n/a)</td><td>35.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>318.10 (n/a)</td><td>191.10 (n/a)</td><td>155.00 (n/a)</td><td>127.80 (n/a)</td><td>77.85 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>290.80 (n/a)</td><td>215.46 (n/a)</td><td>175.00 (n/a)</td><td>163.20 (n/a)</td><td>64.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.50 (n/a)</td><td>146.02 (n/a)</td><td>140.80 (n/a)</td><td>125.60 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.60 (n/a)</td><td>155.54 (n/a)</td><td>147.90 (n/a)</td><td>120.30 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>222.10 (n/a)</td><td>173.56 (n/a)</td><td>162.40 (n/a)</td><td>152.60 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.50 (n/a)</td><td>168.40 (n/a)</td><td>173.40 (n/a)</td><td>122.10 (n/a)</td><td>39.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>189.84 (n/a)</td><td>188.30 (n/a)</td><td>180.30 (n/a)</td><td>10.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 <b>(+27.92%)</b></td><td>0.03 (+4.65%)</td><td>0.02 (+0.25%)</td><td>0.02 (-19.97%)</td><td>0.01 <b>(+182.71%)</b></td><td>231.30 <b>(+24.96%)</b></td><td>167.72 (-0.10%)</td><td>165.70 (-0.24%)</td><td>113.30 <b>(-21.81%)</b></td><td>42.16 <b>(+175.47%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>167.88 (n/a)</td><td>166.10 (n/a)</td><td>144.90 (n/a)</td><td>15.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (+19.35%)</td><td>0.02 (+7.76%)</td><td>0.02 (-0.32%)</td><td>0.02 (-1.90%)</td><td>0.00 <b>(+131.17%)</b></td><td>193.70 (+1.89%)</td><td>167.42 (-5.79%)</td><td>180.20 (+0.33%)</td><td>133.40 (-16.21%)</td><td>25.28 <b>(+95.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.10 (n/a)</td><td>177.70 (n/a)</td><td>179.60 (n/a)</td><td>159.20 (n/a)</td><td>12.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 <b>(+23.42%)</b></td><td>0.03 <b>(+33.29%)</b></td><td>0.03 <b>(+26.73%)</b></td><td>0.02 <b>(+62.62%)</b></td><td>0.01 (-5.37%)</td><td>208.90 <b>(-38.50%)</b></td><td>149.28 <b>(-28.36%)</b></td><td>143.70 <b>(-21.04%)</b></td><td>117.60 (-19.01%)</td><td>35.48 <b>(-53.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>339.70 (n/a)</td><td>208.38 (n/a)</td><td>182.00 (n/a)</td><td>145.20 (n/a)</td><td>76.82 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-1.23%)</td><td>0.02 (-0.76%)</td><td>0.02 (+1.73%)</td><td>0.02 (-7.81%)</td><td>0.00 <b>(+24.96%)</b></td><td>236.70 (+8.48%)</td><td>184.78 (+1.67%)</td><td>177.50 (-1.66%)</td><td>156.50 (+1.23%)</td><td>31.87 <b>(+36.85%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.20 (n/a)</td><td>181.74 (n/a)</td><td>180.50 (n/a)</td><td>154.60 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 <b>(+40.57%)</b></td><td>0.03 (+19.97%)</td><td>0.02 (+5.84%)</td><td>0.02 (-2.85%)</td><td>0.01 <b>(+280.56%)</b></td><td>215.00 (+2.92%)</td><td>163.62 (-11.98%)</td><td>177.00 (-5.55%)</td><td>116.90 <b>(-28.89%)</b></td><td>43.47 <b>(+165.79%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.90 (n/a)</td><td>185.90 (n/a)</td><td>187.40 (n/a)</td><td>164.40 (n/a)</td><td>16.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (+4.43%)</td><td>0.02 (-5.22%)</td><td>0.02 (-5.05%)</td><td>0.02 (-11.53%)</td><td>0.01 <b>(+26.71%)</b></td><td>255.50 (+13.00%)</td><td>203.78 (+7.68%)</td><td>192.90 (+5.35%)</td><td>138.80 (-4.21%)</td><td>48.61 <b>(+36.03%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.10 (n/a)</td><td>189.24 (n/a)</td><td>183.10 (n/a)</td><td>144.90 (n/a)</td><td>35.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 <b>(+25.91%)</b></td><td>0.02 (+12.28%)</td><td>0.02 (+3.44%)</td><td>0.01 (+4.86%)</td><td>0.00 <b>(+48.31%)</b></td><td>276.10 (-4.63%)</td><td>198.80 (-9.59%)</td><td>193.90 (-3.34%)</td><td>155.70 <b>(-20.56%)</b></td><td>46.08 (+15.54%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>289.50 (n/a)</td><td>219.88 (n/a)</td><td>200.60 (n/a)</td><td>196.00 (n/a)</td><td>39.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 <b>(+73.87%)</b></td><td>0.02 <b>(+44.08%)</b></td><td>0.02 <b>(+26.35%)</b></td><td>0.02 <b>(+72.93%)</b></td><td>0.00 <b>(+73.58%)</b></td><td>196.50 <b>(-42.15%)</b></td><td>174.54 <b>(-30.64%)</b></td><td>181.00 <b>(-20.86%)</b></td><td>128.10 <b>(-42.48%)</b></td><td>27.61 <b>(-44.37%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>339.70 (n/a)</td><td>251.66 (n/a)</td><td>228.70 (n/a)</td><td>222.70 (n/a)</td><td>49.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (+11.17%)</td><td>0.05 (+5.35%)</td><td>0.05 (+5.99%)</td><td>0.04 (-5.94%)</td><td>0.01 <b>(+70.02%)</b></td><td>205.60 (+6.31%)</td><td>162.04 (-3.70%)</td><td>158.30 (-5.66%)</td><td>133.20 (-10.00%)</td><td>28.13 <b>(+62.96%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.40 (n/a)</td><td>168.26 (n/a)</td><td>167.80 (n/a)</td><td>148.00 (n/a)</td><td>17.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (+17.87%)</td><td>0.05 (+7.31%)</td><td>0.05 (+13.03%)</td><td>0.04 (-11.35%)</td><td>0.01 <b>(+121.21%)</b></td><td>218.00 (+12.84%)</td><td>166.62 (-4.76%)</td><td>155.50 (-11.55%)</td><td>133.60 (-15.12%)</td><td>32.41 <b>(+116.55%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.20 (n/a)</td><td>174.94 (n/a)</td><td>175.80 (n/a)</td><td>157.40 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (-4.22%)</td><td>0.04 (-9.85%)</td><td>0.04 (-11.14%)</td><td>0.03 <b>(-24.35%)</b></td><td>0.01 <b>(+130.99%)</b></td><td>243.40 <b>(+32.14%)</b></td><td>194.96 (+12.34%)</td><td>190.50 (+12.52%)</td><td>172.40 (+4.42%)</td><td>28.24 <b>(+223.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.20 (n/a)</td><td>173.54 (n/a)</td><td>169.30 (n/a)</td><td>165.10 (n/a)</td><td>8.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (+13.04%)</td><td>0.06 (+13.49%)</td><td>0.06 <b>(+26.86%)</b></td><td>0.04 (+8.20%)</td><td>0.01 (+17.33%)</td><td>183.70 (-7.60%)</td><td>150.54 (-11.64%)</td><td>137.20 <b>(-21.19%)</b></td><td>122.90 (-11.58%)</td><td>26.34 (-2.20%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>170.38 (n/a)</td><td>174.10 (n/a)</td><td>139.00 (n/a)</td><td>26.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(+21.91%)</b></td><td>0.05 (+11.70%)</td><td>0.05 (+19.47%)</td><td>0.04 (-5.44%)</td><td>0.01 <b>(+133.31%)</b></td><td>216.10 (+5.78%)</td><td>164.42 (-7.36%)</td><td>149.00 (-16.29%)</td><td>124.70 (-18.01%)</td><td>39.12 <b>(+105.84%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>177.48 (n/a)</td><td>178.00 (n/a)</td><td>152.10 (n/a)</td><td>19.01 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(+55.12%)</b></td><td>0.05 <b>(+20.65%)</b></td><td>0.05 <b>(+21.47%)</b></td><td>0.03 (+2.16%)</td><td>0.01 <b>(+154.30%)</b></td><td>253.70 (-2.08%)</td><td>178.50 (-12.68%)</td><td>166.20 (-17.68%)</td><td>113.60 <b>(-35.53%)</b></td><td>52.27 <b>(+58.57%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.10 (n/a)</td><td>204.42 (n/a)</td><td>201.90 (n/a)</td><td>176.20 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (+15.33%)</td><td>0.05 (-2.15%)</td><td>0.04 (-2.68%)</td><td>0.04 (-9.09%)</td><td>0.01 <b>(+136.22%)</b></td><td>208.40 (+10.03%)</td><td>185.04 (+3.68%)</td><td>189.20 (+2.77%)</td><td>143.60 (-13.29%)</td><td>25.70 <b>(+124.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.40 (n/a)</td><td>178.48 (n/a)</td><td>184.10 (n/a)</td><td>165.60 (n/a)</td><td>11.46 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (-17.12%)</td><td>0.04 (-6.88%)</td><td>0.04 (-9.28%)</td><td>0.03 (+0.26%)</td><td>0.01 <b>(-43.29%)</b></td><td>239.70 (-0.25%)</td><td>197.82 (+3.97%)</td><td>196.80 (+10.19%)</td><td>155.60 <b>(+20.62%)</b></td><td>30.56 <b>(-34.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>190.26 (n/a)</td><td>178.60 (n/a)</td><td>129.00 (n/a)</td><td>46.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (+6.91%)</td><td>0.04 (-8.07%)</td><td>0.04 (-9.43%)</td><td>0.03 <b>(-24.06%)</b></td><td>0.01 <b>(+95.96%)</b></td><td>280.60 <b>(+31.68%)</b></td><td>205.74 (+12.28%)</td><td>201.90 (+10.39%)</td><td>148.40 (-6.49%)</td><td>47.49 <b>(+142.56%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>183.24 (n/a)</td><td>182.90 (n/a)</td><td>158.70 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 <b>(+20.02%)</b></td><td>0.04 (+16.49%)</td><td>0.04 (+7.56%)</td><td>0.03 <b>(+54.49%)</b></td><td>0.00 <b>(-24.96%)</b></td><td>239.10 <b>(-35.26%)</b></td><td>213.38 (-16.56%)</td><td>219.10 (-7.00%)</td><td>174.20 (-16.69%)</td><td>24.31 <b>(-62.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>369.30 (n/a)</td><td>255.72 (n/a)</td><td>235.60 (n/a)</td><td>209.10 (n/a)</td><td>64.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (+15.09%)</td><td>0.11 (-1.93%)</td><td>0.10 (-10.88%)</td><td>0.09 (-7.03%)</td><td>0.02 <b>(+72.46%)</b></td><td>184.20 (+7.59%)</td><td>157.58 (+3.55%)</td><td>164.60 (+12.20%)</td><td>115.70 (-13.07%)</td><td>25.46 <b>(+52.33%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>171.20 (n/a)</td><td>152.18 (n/a)</td><td>146.70 (n/a)</td><td>133.10 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (-15.08%)</td><td>0.09 (-15.39%)</td><td>0.10 (-6.33%)</td><td>0.06 <b>(-35.08%)</b></td><td>0.02 (+13.89%)</td><td>289.90 <b>(+54.04%)</b></td><td>194.30 <b>(+22.06%)</b></td><td>166.60 (+6.79%)</td><td>149.00 (+17.79%)</td><td>57.50 <b>(+104.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>159.18 (n/a)</td><td>156.00 (n/a)</td><td>126.50 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (+14.15%)</td><td>0.10 (+3.33%)</td><td>0.10 (-3.34%)</td><td>0.05 (-8.97%)</td><td>0.03 <b>(+44.91%)</b></td><td>305.20 (+9.86%)</td><td>187.50 (+1.18%)</td><td>171.70 (+3.50%)</td><td>126.50 (-12.40%)</td><td>71.36 <b>(+34.11%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>277.80 (n/a)</td><td>185.32 (n/a)</td><td>165.90 (n/a)</td><td>144.40 (n/a)</td><td>53.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (+8.89%)</td><td>0.10 (+8.42%)</td><td>0.10 (+8.21%)</td><td>0.08 (+7.26%)</td><td>0.02 (+15.33%)</td><td>193.90 (-6.78%)</td><td>161.98 (-7.49%)</td><td>163.20 (-7.59%)</td><td>124.00 (-8.15%)</td><td>26.06 (+0.04%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>175.10 (n/a)</td><td>176.60 (n/a)</td><td>135.00 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (-2.13%)</td><td>0.09 (+2.66%)</td><td>0.10 (+4.62%)</td><td>0.08 (+16.63%)</td><td>0.01 <b>(-25.86%)</b></td><td>213.20 (-14.27%)</td><td>179.20 (-4.25%)</td><td>172.30 (-4.38%)</td><td>150.70 (+2.17%)</td><td>26.06 <b>(-34.82%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>187.16 (n/a)</td><td>180.20 (n/a)</td><td>147.50 (n/a)</td><td>39.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 <b>(+34.97%)</b></td><td>0.10 (+13.53%)</td><td>0.10 (+11.64%)</td><td>0.06 (+8.68%)</td><td>0.03 <b>(+83.10%)</b></td><td>260.70 (-7.98%)</td><td>184.10 (-7.10%)</td><td>171.40 (-10.45%)</td><td>116.70 <b>(-25.90%)</b></td><td>63.24 <b>(+25.21%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>283.30 (n/a)</td><td>198.16 (n/a)</td><td>191.40 (n/a)</td><td>157.50 (n/a)</td><td>50.51 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (-17.34%)</td><td>0.09 (-4.10%)</td><td>0.09 (+14.40%)</td><td>0.06 (-10.87%)</td><td>0.02 (-18.50%)</td><td>254.10 (+12.19%)</td><td>196.38 (+3.86%)</td><td>181.80 (-12.55%)</td><td>158.20 <b>(+21.04%)</b></td><td>42.92 (+9.32%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.50 (n/a)</td><td>189.08 (n/a)</td><td>207.90 (n/a)</td><td>130.70 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 (+0.49%)</td><td>0.08 (+1.35%)</td><td>0.08 (+4.86%)</td><td>0.07 (+1.45%)</td><td>0.01 (-3.83%)</td><td>233.50 (-1.44%)</td><td>208.74 (-1.46%)</td><td>209.20 (-4.65%)</td><td>170.10 (-0.47%)</td><td>25.08 (-5.67%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.90 (n/a)</td><td>211.84 (n/a)</td><td>219.40 (n/a)</td><td>170.90 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (+19.28%)</td><td>0.20 (+15.53%)</td><td>0.19 (+4.73%)</td><td>0.13 <b>(+24.92%)</b></td><td>0.05 (+17.89%)</td><td>248.20 (-19.94%)</td><td>172.08 (-14.04%)</td><td>173.00 (-4.47%)</td><td>126.90 (-16.13%)</td><td>48.91 <b>(-24.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>310.00 (n/a)</td><td>200.18 (n/a)</td><td>181.10 (n/a)</td><td>151.30 (n/a)</td><td>64.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (+0.95%)</td><td>0.21 (+5.50%)</td><td>0.20 (+11.78%)</td><td>0.19 (+13.02%)</td><td>0.03 <b>(-28.83%)</b></td><td>176.30 (-11.54%)</td><td>157.60 (-6.67%)</td><td>160.30 (-10.55%)</td><td>127.90 (-0.93%)</td><td>18.24 <b>(-39.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>199.30 (n/a)</td><td>168.86 (n/a)</td><td>179.20 (n/a)</td><td>129.10 (n/a)</td><td>29.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (+3.64%)</td><td>0.22 (+17.69%)</td><td>0.21 (+18.48%)</td><td>0.19 <b>(+20.52%)</b></td><td>0.03 (-15.18%)</td><td>177.00 (-17.02%)</td><td>152.02 (-15.76%)</td><td>153.30 (-15.58%)</td><td>131.80 (-3.51%)</td><td>19.23 <b>(-30.93%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.30 (n/a)</td><td>180.46 (n/a)</td><td>181.60 (n/a)</td><td>136.60 (n/a)</td><td>27.84 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (-13.76%)</td><td>0.19 (-1.28%)</td><td>0.19 (-7.82%)</td><td>0.14 (+2.25%)</td><td>0.04 <b>(-28.49%)</b></td><td>235.10 (-2.20%)</td><td>173.42 (-0.94%)</td><td>169.00 (+8.47%)</td><td>144.90 (+15.92%)</td><td>36.78 <b>(-20.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>240.40 (n/a)</td><td>175.06 (n/a)</td><td>155.80 (n/a)</td><td>125.00 (n/a)</td><td>46.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (-9.47%)</td><td>0.20 (+5.08%)</td><td>0.20 (-4.83%)</td><td>0.17 <b>(+32.65%)</b></td><td>0.02 <b>(-60.77%)</b></td><td>188.80 <b>(-24.60%)</b></td><td>163.64 (-8.95%)</td><td>162.90 (+5.10%)</td><td>147.40 (+10.49%)</td><td>15.50 <b>(-67.37%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>250.40 (n/a)</td><td>179.72 (n/a)</td><td>155.00 (n/a)</td><td>133.40 (n/a)</td><td>47.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.24 (+12.36%)</td><td>0.20 (+12.83%)</td><td>0.20 <b>(+21.78%)</b></td><td>0.16 (+5.94%)</td><td>0.03 (+13.73%)</td><td>203.20 (-5.58%)</td><td>168.30 (-11.23%)</td><td>163.90 (-17.84%)</td><td>139.30 (-10.99%)</td><td>22.99 (-3.18%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>189.60 (n/a)</td><td>199.50 (n/a)</td><td>156.50 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (+11.40%)</td><td>0.17 (+13.49%)</td><td>0.17 (+14.71%)</td><td>0.16 (+15.27%)</td><td>0.01 (-8.36%)</td><td>206.90 (-13.25%)</td><td>195.38 (-11.94%)</td><td>191.70 (-12.82%)</td><td>188.30 (-10.25%)</td><td>7.46 <b>(-28.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>221.88 (n/a)</td><td>219.90 (n/a)</td><td>209.80 (n/a)</td><td>10.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-13.70%)</td><td>0.02 (-3.97%)</td><td>0.03 (+2.35%)</td><td>0.02 (-6.44%)</td><td>0.00 <b>(-28.58%)</b></td><td>202.50 (+6.92%)</td><td>170.32 (+3.59%)</td><td>161.30 (-2.30%)</td><td>150.70 (+15.92%)</td><td>20.20 (-8.36%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.40 (n/a)</td><td>164.42 (n/a)</td><td>165.10 (n/a)</td><td>130.00 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (+6.33%)</td><td>0.03 (+2.61%)</td><td>0.03 (+1.61%)</td><td>0.02 (-2.35%)</td><td>0.00 <b>(+35.37%)</b></td><td>187.00 (+2.41%)</td><td>158.66 (-2.10%)</td><td>155.70 (-1.58%)</td><td>136.90 (-5.98%)</td><td>18.59 <b>(+30.90%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.60 (n/a)</td><td>162.06 (n/a)</td><td>158.20 (n/a)</td><td>145.60 (n/a)</td><td>14.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-15.04%)</td><td>0.02 (+1.75%)</td><td>0.02 (+9.89%)</td><td>0.02 <b>(+31.65%)</b></td><td>0.00 <b>(-66.49%)</b></td><td>250.90 <b>(-24.04%)</b></td><td>226.74 (-6.17%)</td><td>219.20 (-9.01%)</td><td>204.90 (+17.69%)</td><td>18.95 <b>(-69.47%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>330.30 (n/a)</td><td>241.64 (n/a)</td><td>240.90 (n/a)</td><td>174.10 (n/a)</td><td>62.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-15.04%)</td><td>0.02 <b>(-21.79%)</b></td><td>0.02 (-17.13%)</td><td>0.01 <b>(-32.16%)</b></td><td>0.00 (+4.98%)</td><td>331.90 <b>(+47.45%)</b></td><td>242.28 <b>(+30.40%)</b></td><td>231.20 <b>(+20.67%)</b></td><td>183.10 (+17.67%)</td><td>56.77 <b>(+91.58%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.10 (n/a)</td><td>185.80 (n/a)</td><td>191.60 (n/a)</td><td>155.60 (n/a)</td><td>29.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-15.56%)</td><td>0.03 (-2.66%)</td><td>0.02 (+0.11%)</td><td>0.02 (+0.81%)</td><td>0.00 <b>(-35.02%)</b></td><td>187.30 (-0.79%)</td><td>160.04 (+0.70%)</td><td>168.30 (-0.12%)</td><td>123.80 (+18.47%)</td><td>25.55 (-19.91%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>158.92 (n/a)</td><td>168.50 (n/a)</td><td>104.50 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-12.43%)</td><td>0.02 (+6.39%)</td><td>0.02 (-2.33%)</td><td>0.02 <b>(+30.22%)</b></td><td>0.00 <b>(-52.03%)</b></td><td>225.60 <b>(-23.21%)</b></td><td>178.68 (-12.21%)</td><td>173.00 (+2.37%)</td><td>151.20 (+14.20%)</td><td>28.34 <b>(-58.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>293.80 (n/a)</td><td>203.54 (n/a)</td><td>169.00 (n/a)</td><td>132.40 (n/a)</td><td>67.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-18.64%)</td><td>0.02 (-15.45%)</td><td>0.02 (-12.71%)</td><td>0.02 (-18.52%)</td><td>0.00 (-18.31%)</td><td>231.00 <b>(+22.74%)</b></td><td>198.98 (+18.29%)</td><td>200.30 (+14.52%)</td><td>168.10 <b>(+22.88%)</b></td><td>24.90 <b>(+24.87%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.20 (n/a)</td><td>168.22 (n/a)</td><td>174.90 (n/a)</td><td>136.80 (n/a)</td><td>19.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-5.61%)</td><td>0.02 (-4.25%)</td><td>0.02 (-3.70%)</td><td>0.02 (-3.79%)</td><td>0.01 (-5.05%)</td><td>224.00 (+3.94%)</td><td>180.00 (+4.51%)</td><td>178.10 (+3.85%)</td><td>126.70 (+6.03%)</td><td>40.00 (+6.33%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>172.24 (n/a)</td><td>171.50 (n/a)</td><td>119.50 (n/a)</td><td>37.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-7.49%)</td><td>0.02 (-14.11%)</td><td>0.02 (-10.88%)</td><td>0.02 (-18.96%)</td><td>0.00 <b>(+45.85%)</b></td><td>254.50 <b>(+23.42%)</b></td><td>205.70 (+18.56%)</td><td>186.40 (+12.22%)</td><td>165.60 (+8.09%)</td><td>39.05 <b>(+95.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.20 (n/a)</td><td>173.50 (n/a)</td><td>166.10 (n/a)</td><td>153.20 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (+2.67%)</td><td>0.03 (-3.10%)</td><td>0.02 (-7.09%)</td><td>0.02 (+0.01%)</td><td>0.00 (+3.19%)</td><td>203.40 (-0.05%)</td><td>166.06 (+3.32%)</td><td>167.50 (+7.65%)</td><td>132.40 (-2.58%)</td><td>28.77 (+1.67%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.50 (n/a)</td><td>160.72 (n/a)</td><td>155.60 (n/a)</td><td>135.90 (n/a)</td><td>28.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-0.56%)</td><td>0.02 (+6.43%)</td><td>0.02 (+11.66%)</td><td>0.02 (+11.94%)</td><td>0.00 <b>(-27.64%)</b></td><td>207.70 (-10.67%)</td><td>180.28 (-7.07%)</td><td>181.40 (-10.46%)</td><td>152.90 (+0.53%)</td><td>20.06 <b>(-34.44%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.50 (n/a)</td><td>194.00 (n/a)</td><td>202.60 (n/a)</td><td>152.10 (n/a)</td><td>30.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-6.92%)</td><td>0.02 (-11.91%)</td><td>0.02 (-12.96%)</td><td>0.02 (-10.86%)</td><td>0.00 (+14.32%)</td><td>216.90 (+12.15%)</td><td>195.88 (+13.76%)</td><td>195.10 (+14.90%)</td><td>174.50 (+7.45%)</td><td>17.25 <b>(+37.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.40 (n/a)</td><td>172.18 (n/a)</td><td>169.80 (n/a)</td><td>162.40 (n/a)</td><td>12.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-1.85%)</td><td>0.02 (-1.37%)</td><td>0.02 (+7.47%)</td><td>0.02 (-1.81%)</td><td>0.00 (-9.83%)</td><td>246.50 (+1.86%)</td><td>190.72 (+0.78%)</td><td>186.20 (-6.95%)</td><td>139.90 (+1.89%)</td><td>38.09 (-5.92%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.00 (n/a)</td><td>189.24 (n/a)</td><td>200.10 (n/a)</td><td>137.30 (n/a)</td><td>40.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-15.15%)</td><td>0.02 (-7.68%)</td><td>0.02 (-3.09%)</td><td>0.02 (-5.38%)</td><td>0.00 <b>(-45.39%)</b></td><td>219.50 (+5.68%)</td><td>202.92 (+7.49%)</td><td>204.00 (+3.19%)</td><td>182.60 (+17.81%)</td><td>15.13 <b>(-32.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.70 (n/a)</td><td>188.78 (n/a)</td><td>197.70 (n/a)</td><td>155.00 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-0.78%)</td><td>0.02 (-1.17%)</td><td>0.02 (+2.38%)</td><td>0.01 (+11.93%)</td><td>0.00 <b>(-26.93%)</b></td><td>280.40 (-10.64%)</td><td>204.76 (-2.32%)</td><td>194.90 (-2.31%)</td><td>152.30 (+0.79%)</td><td>46.71 <b>(-30.21%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>313.80 (n/a)</td><td>209.62 (n/a)</td><td>199.50 (n/a)</td><td>151.10 (n/a)</td><td>66.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (-19.83%)</td><td>0.02 (-16.18%)</td><td>0.02 (-18.28%)</td><td>0.02 (-10.89%)</td><td>0.00 <b>(-36.97%)</b></td><td>250.70 (+12.22%)</td><td>210.96 (+18.33%)</td><td>207.90 <b>(+22.37%)</b></td><td>183.50 <b>(+24.75%)</b></td><td>24.82 (-12.15%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>178.28 (n/a)</td><td>169.90 (n/a)</td><td>147.10 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-7.67%)</td><td>0.05 (-12.30%)</td><td>0.04 (-12.65%)</td><td>0.03 <b>(-23.15%)</b></td><td>0.01 <b>(+33.20%)</b></td><td>234.50 <b>(+30.13%)</b></td><td>181.98 (+17.26%)</td><td>183.90 (+14.51%)</td><td>130.20 (+8.32%)</td><td>42.79 <b>(+92.37%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.20 (n/a)</td><td>155.20 (n/a)</td><td>160.60 (n/a)</td><td>120.20 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 <b>(-20.28%)</b></td><td>0.04 <b>(-22.21%)</b></td><td>0.05 (-16.29%)</td><td>0.04 (-18.17%)</td><td>0.01 <b>(-27.80%)</b></td><td>231.70 <b>(+22.20%)</b></td><td>187.52 <b>(+27.84%)</b></td><td>179.40 (+19.44%)</td><td>147.20 <b>(+25.49%)</b></td><td>31.66 (+11.68%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>146.68 (n/a)</td><td>150.20 (n/a)</td><td>117.30 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (-0.02%)</td><td>0.04 (-7.32%)</td><td>0.03 <b>(-21.09%)</b></td><td>0.03 <b>(+25.42%)</b></td><td>0.01 <b>(-35.74%)</b></td><td>301.00 <b>(-20.26%)</b></td><td>239.42 (+2.48%)</td><td>236.50 <b>(+26.67%)</b></td><td>181.60 (+0.00%)</td><td>42.30 <b>(-49.31%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>377.50 (n/a)</td><td>233.62 (n/a)</td><td>186.70 (n/a)</td><td>181.60 (n/a)</td><td>83.45 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (+10.32%)</td><td>0.04 (+0.31%)</td><td>0.04 (-0.88%)</td><td>0.03 (-9.97%)</td><td>0.01 <b>(+43.45%)</b></td><td>244.00 (+11.06%)</td><td>198.46 (+0.63%)</td><td>193.50 (+0.89%)</td><td>161.10 (-9.34%)</td><td>30.23 <b>(+44.66%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.70 (n/a)</td><td>197.22 (n/a)</td><td>191.80 (n/a)</td><td>177.70 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-11.67%)</td><td>0.04 (-18.20%)</td><td>0.05 (-14.64%)</td><td>0.03 <b>(-30.39%)</b></td><td>0.01 <b>(+51.43%)</b></td><td>261.40 <b>(+43.71%)</b></td><td>193.84 <b>(+26.76%)</b></td><td>169.90 (+17.09%)</td><td>147.40 (+13.21%)</td><td>49.96 <b>(+146.19%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.90 (n/a)</td><td>152.92 (n/a)</td><td>145.10 (n/a)</td><td>130.20 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-15.29%)</td><td>0.04 (-19.78%)</td><td>0.04 <b>(-25.41%)</b></td><td>0.04 (-7.96%)</td><td>0.01 <b>(-23.32%)</b></td><td>228.10 (+8.67%)</td><td>196.16 <b>(+23.68%)</b></td><td>193.30 <b>(+34.05%)</b></td><td>148.30 (+18.07%)</td><td>31.49 (-3.93%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>158.60 (n/a)</td><td>144.20 (n/a)</td><td>125.60 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-1.43%)</td><td>0.06 <b>(+20.11%)</b></td><td>0.06 <b>(+31.53%)</b></td><td>0.05 <b>(+31.22%)</b></td><td>0.01 <b>(-39.75%)</b></td><td>175.40 <b>(-23.81%)</b></td><td>146.88 (-18.89%)</td><td>142.80 <b>(-23.96%)</b></td><td>131.30 (+1.47%)</td><td>17.76 <b>(-52.41%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>181.08 (n/a)</td><td>187.80 (n/a)</td><td>129.40 (n/a)</td><td>37.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (+0.10%)</td><td>0.05 (+2.86%)</td><td>0.05 (-11.28%)</td><td>0.03 (+15.86%)</td><td>0.01 (-15.76%)</td><td>265.00 (-13.71%)</td><td>179.56 (-6.04%)</td><td>175.30 (+12.66%)</td><td>132.00 (-0.15%)</td><td>51.61 <b>(-27.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.10 (n/a)</td><td>191.10 (n/a)</td><td>155.60 (n/a)</td><td>132.20 (n/a)</td><td>70.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-7.83%)</td><td>0.05 (-4.09%)</td><td>0.06 (-0.42%)</td><td>0.04 (+7.53%)</td><td>0.01 (-10.97%)</td><td>198.40 (-6.99%)</td><td>160.68 (+3.52%)</td><td>140.70 (+0.43%)</td><td>135.80 (+8.47%)</td><td>30.30 (-12.74%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>155.22 (n/a)</td><td>140.10 (n/a)</td><td>125.20 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-6.87%)</td><td>0.04 (-8.67%)</td><td>0.04 (-8.51%)</td><td>0.03 <b>(-23.71%)</b></td><td>0.01 <b>(+28.32%)</b></td><td>248.00 <b>(+31.08%)</b></td><td>190.68 (+12.03%)</td><td>194.90 (+9.31%)</td><td>140.10 (+7.36%)</td><td>42.49 <b>(+83.60%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>170.20 (n/a)</td><td>178.30 (n/a)</td><td>130.50 (n/a)</td><td>23.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-10.09%)</td><td>0.05 (-14.77%)</td><td>0.04 (-19.00%)</td><td>0.03 <b>(-34.95%)</b></td><td>0.01 <b>(+35.74%)</b></td><td>292.40 <b>(+53.73%)</b></td><td>196.44 <b>(+23.53%)</b></td><td>203.30 <b>(+23.51%)</b></td><td>137.10 (+11.19%)</td><td>63.50 <b>(+120.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>159.02 (n/a)</td><td>164.60 (n/a)</td><td>123.30 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-11.99%)</td><td>0.05 (-12.80%)</td><td>0.05 <b>(-20.31%)</b></td><td>0.04 (+5.78%)</td><td>0.01 <b>(-37.97%)</b></td><td>190.40 (-5.46%)</td><td>170.16 (+12.64%)</td><td>176.70 <b>(+25.50%)</b></td><td>138.90 (+13.57%)</td><td>20.01 <b>(-35.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>151.06 (n/a)</td><td>140.80 (n/a)</td><td>122.30 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (-18.37%)</td><td>0.05 (-10.59%)</td><td>0.05 (-17.30%)</td><td>0.04 (+7.33%)</td><td>0.00 <b>(-62.45%)</b></td><td>210.80 (-6.81%)</td><td>182.16 (+8.30%)</td><td>172.80 <b>(+20.92%)</b></td><td>169.40 <b>(+22.58%)</b></td><td>17.19 <b>(-56.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>168.20 (n/a)</td><td>142.90 (n/a)</td><td>138.20 (n/a)</td><td>39.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 (-14.22%)</td><td>0.04 (-19.99%)</td><td>0.04 (-16.83%)</td><td>0.02 <b>(-41.75%)</b></td><td>0.01 <b>(+28.55%)</b></td><td>358.40 <b>(+71.65%)</b></td><td>212.18 <b>(+33.23%)</b></td><td>183.60 <b>(+20.24%)</b></td><td>148.60 (+16.55%)</td><td>83.75 <b>(+170.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>159.26 (n/a)</td><td>152.70 (n/a)</td><td>127.50 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 <b>(-24.44%)</b></td><td>0.05 (-4.34%)</td><td>0.05 (-2.18%)</td><td>0.04 (+19.41%)</td><td>0.00 <b>(-77.49%)</b></td><td>193.40 (-16.28%)</td><td>181.78 (-0.01%)</td><td>181.40 (+2.20%)</td><td>169.60 <b>(+32.40%)</b></td><td>10.54 <b>(-75.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>181.80 (n/a)</td><td>177.50 (n/a)</td><td>128.10 (n/a)</td><td>42.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 <b>(-26.86%)</b></td><td>0.04 (-17.19%)</td><td>0.04 (-10.52%)</td><td>0.03 (-7.13%)</td><td>0.00 <b>(-63.62%)</b></td><td>238.50 (+7.67%)</td><td>208.30 (+16.33%)</td><td>204.10 (+11.77%)</td><td>179.20 <b>(+36.69%)</b></td><td>22.22 <b>(-47.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>179.06 (n/a)</td><td>182.60 (n/a)</td><td>131.10 (n/a)</td><td>41.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (+5.98%)</td><td>0.11 (+4.43%)</td><td>0.12 <b>(+39.44%)</b></td><td>0.04 <b>(-41.73%)</b></td><td>0.04 <b>(+61.39%)</b></td><td>367.60 <b>(+71.62%)</b></td><td>184.02 (+10.27%)</td><td>131.80 <b>(-28.29%)</b></td><td>113.50 (-5.65%)</td><td>106.79 <b>(+170.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>214.20 (n/a)</td><td>166.88 (n/a)</td><td>183.80 (n/a)</td><td>120.30 (n/a)</td><td>39.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (-10.41%)</td><td>0.10 (-3.34%)</td><td>0.10 (+2.88%)</td><td>0.08 (-0.32%)</td><td>0.02 <b>(-31.47%)</b></td><td>202.90 (+0.30%)</td><td>172.14 (+1.68%)</td><td>168.30 (-2.83%)</td><td>137.70 (+11.68%)</td><td>25.92 <b>(-24.67%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.30 (n/a)</td><td>169.30 (n/a)</td><td>173.20 (n/a)</td><td>123.30 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (-16.07%)</td><td>0.08 (+7.57%)</td><td>0.08 (+4.70%)</td><td>0.07 <b>(+53.23%)</b></td><td>0.00 <b>(-83.80%)</b></td><td>224.10 <b>(-34.74%)</b></td><td>213.06 (-11.67%)</td><td>209.20 (-4.47%)</td><td>206.30 (+19.18%)</td><td>7.92 <b>(-87.75%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>343.40 (n/a)</td><td>241.22 (n/a)</td><td>219.00 (n/a)</td><td>173.10 (n/a)</td><td>64.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (+4.75%)</td><td>0.07 (-5.41%)</td><td>0.07 (-6.02%)</td><td>0.06 (-7.29%)</td><td>0.01 <b>(+32.04%)</b></td><td>291.50 (+7.88%)</td><td>230.98 (+6.92%)</td><td>220.30 (+6.37%)</td><td>176.40 (-4.55%)</td><td>42.20 <b>(+31.68%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>270.20 (n/a)</td><td>216.04 (n/a)</td><td>207.10 (n/a)</td><td>184.80 (n/a)</td><td>32.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (+0.01%)</td><td>0.10 (-3.92%)</td><td>0.09 (+1.28%)</td><td>0.08 (+3.10%)</td><td>0.02 (-11.57%)</td><td>196.40 (-3.01%)</td><td>172.10 (+3.31%)</td><td>179.50 (-1.27%)</td><td>128.30 (+0.00%)</td><td>27.61 (-13.35%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.50 (n/a)</td><td>166.58 (n/a)</td><td>181.80 (n/a)</td><td>128.30 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (+8.91%)</td><td>0.11 (+8.32%)</td><td>0.12 (+14.91%)</td><td>0.08 <b>(+21.71%)</b></td><td>0.02 (+13.06%)</td><td>192.90 (-17.84%)</td><td>156.24 (-7.76%)</td><td>139.50 (-12.98%)</td><td>123.10 (-8.20%)</td><td>33.02 (-14.62%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.80 (n/a)</td><td>169.38 (n/a)</td><td>160.30 (n/a)</td><td>134.10 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (+1.62%)</td><td>0.09 (-12.31%)</td><td>0.09 (-16.73%)</td><td>0.05 <b>(-38.16%)</b></td><td>0.03 <b>(+52.75%)</b></td><td>305.90 <b>(+61.68%)</b></td><td>195.86 <b>(+23.10%)</b></td><td>191.10 <b>(+20.11%)</b></td><td>111.90 (-1.58%)</td><td>71.80 <b>(+147.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>159.10 (n/a)</td><td>159.10 (n/a)</td><td>113.70 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (+3.05%)</td><td>0.11 (+15.59%)</td><td>0.10 (+7.90%)</td><td>0.09 <b>(+121.35%)</b></td><td>0.01 <b>(-51.92%)</b></td><td>177.30 <b>(-54.83%)</b></td><td>156.80 <b>(-23.99%)</b></td><td>162.20 (-7.31%)</td><td>125.30 (-2.94%)</td><td>19.95 <b>(-81.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>392.50 (n/a)</td><td>206.30 (n/a)</td><td>175.00 (n/a)</td><td>129.10 (n/a)</td><td>105.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 <b>(+23.39%)</b></td><td>0.11 (+17.67%)</td><td>0.09 (-1.02%)</td><td>0.08 <b>(+20.07%)</b></td><td>0.03 <b>(+34.15%)</b></td><td>194.00 (-16.70%)</td><td>161.94 (-14.24%)</td><td>186.30 (+1.03%)</td><td>107.40 (-18.94%)</td><td>38.53 (-10.44%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>188.82 (n/a)</td><td>184.40 (n/a)</td><td>132.50 (n/a)</td><td>43.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 <b>(+32.60%)</b></td><td>0.10 (+15.04%)</td><td>0.10 (+6.67%)</td><td>0.08 (+8.78%)</td><td>0.02 <b>(+85.96%)</b></td><td>200.60 (-8.07%)</td><td>164.40 (-11.49%)</td><td>171.70 (-6.28%)</td><td>117.40 <b>(-24.60%)</b></td><td>30.74 <b>(+24.56%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>185.74 (n/a)</td><td>183.20 (n/a)</td><td>155.70 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 <b>(+32.24%)</b></td><td>0.11 (+10.70%)</td><td>0.11 (+9.93%)</td><td>0.08 (+0.17%)</td><td>0.02 <b>(+121.26%)</b></td><td>198.30 (-0.15%)</td><td>156.56 (-7.11%)</td><td>152.10 (-8.98%)</td><td>110.70 <b>(-24.39%)</b></td><td>33.07 <b>(+64.87%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>168.54 (n/a)</td><td>167.10 (n/a)</td><td>146.40 (n/a)</td><td>20.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (-2.97%)</td><td>0.10 (-4.58%)</td><td>0.10 (-8.50%)</td><td>0.07 (+4.19%)</td><td>0.02 (-12.53%)</td><td>221.50 (-4.03%)</td><td>172.44 (+3.92%)</td><td>163.10 (+9.32%)</td><td>145.40 (+3.05%)</td><td>31.08 (-16.03%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.80 (n/a)</td><td>165.94 (n/a)</td><td>149.20 (n/a)</td><td>141.10 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (+12.68%)</td><td>0.09 (-1.40%)</td><td>0.09 (-5.29%)</td><td>0.07 (-14.48%)</td><td>0.02 <b>(+114.58%)</b></td><td>243.50 (+16.95%)</td><td>190.58 (+4.82%)</td><td>191.20 (+5.58%)</td><td>137.70 (-11.22%)</td><td>42.44 <b>(+123.64%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>181.82 (n/a)</td><td>181.10 (n/a)</td><td>155.10 (n/a)</td><td>18.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (-6.65%)</td><td>0.10 (-3.04%)</td><td>0.10 (+1.23%)</td><td>0.07 (-11.74%)</td><td>0.02 (+19.09%)</td><td>220.70 (+13.30%)</td><td>167.78 (+4.54%)</td><td>157.60 (-1.19%)</td><td>137.00 (+7.11%)</td><td>35.45 <b>(+42.37%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.80 (n/a)</td><td>160.50 (n/a)</td><td>159.50 (n/a)</td><td>127.90 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (+9.03%)</td><td>0.10 (-5.34%)</td><td>0.10 (-8.79%)</td><td>0.07 (-16.26%)</td><td>0.02 <b>(+80.72%)</b></td><td>230.40 (+19.44%)</td><td>176.60 (+7.85%)</td><td>170.30 (+9.66%)</td><td>138.90 (-8.32%)</td><td>34.69 <b>(+100.28%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>163.74 (n/a)</td><td>155.30 (n/a)</td><td>151.50 (n/a)</td><td>17.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (+6.55%)</td><td>0.09 (+2.03%)</td><td>0.09 (+1.19%)</td><td>0.08 (+3.05%)</td><td>0.01 (+12.15%)</td><td>208.00 (-2.99%)</td><td>178.34 (-1.78%)</td><td>180.90 (-1.15%)</td><td>144.30 (-6.12%)</td><td>24.46 (+1.79%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>181.58 (n/a)</td><td>183.00 (n/a)</td><td>153.70 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.24 (+17.58%)</td><td>0.18 (-0.25%)</td><td>0.18 (+2.39%)</td><td>0.14 (-17.87%)</td><td>0.04 <b>(+151.13%)</b></td><td>237.90 <b>(+21.75%)</b></td><td>187.74 (+3.40%)</td><td>185.20 (-2.32%)</td><td>136.60 (-14.94%)</td><td>39.26 <b>(+158.78%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.40 (n/a)</td><td>181.56 (n/a)</td><td>189.60 (n/a)</td><td>160.60 (n/a)</td><td>15.17 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 <b>(+30.26%)</b></td><td>0.19 (-2.66%)</td><td>0.19 (-6.35%)</td><td>0.14 (-15.45%)</td><td>0.05 <b>(+209.37%)</b></td><td>229.60 (+18.29%)</td><td>180.70 (+6.85%)</td><td>176.10 (+6.79%)</td><td>121.60 <b>(-23.23%)</b></td><td>39.74 <b>(+170.84%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.10 (n/a)</td><td>169.12 (n/a)</td><td>164.90 (n/a)</td><td>158.40 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (-14.63%)</td><td>0.16 (-10.63%)</td><td>0.15 (-7.52%)</td><td>0.12 (-0.35%)</td><td>0.03 <b>(-29.85%)</b></td><td>280.70 (+0.36%)</td><td>215.70 (+9.23%)</td><td>217.50 (+8.10%)</td><td>160.00 (+17.13%)</td><td>44.84 (-17.63%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>279.70 (n/a)</td><td>197.48 (n/a)</td><td>201.20 (n/a)</td><td>136.60 (n/a)</td><td>54.44 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (-1.61%)</td><td>0.16 (-5.75%)</td><td>0.15 (-6.01%)</td><td>0.14 (-12.00%)</td><td>0.02 <b>(+28.84%)</b></td><td>238.40 (+13.63%)</td><td>209.52 (+6.56%)</td><td>217.30 (+6.36%)</td><td>181.10 (+1.63%)</td><td>22.50 <b>(+47.63%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>196.62 (n/a)</td><td>204.30 (n/a)</td><td>178.20 (n/a)</td><td>15.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (+8.32%)</td><td>0.18 (-9.75%)</td><td>0.17 (-11.34%)</td><td>0.11 <b>(-39.12%)</b></td><td>0.05 <b>(+255.90%)</b></td><td>296.30 <b>(+64.25%)</b></td><td>200.16 (+18.75%)</td><td>188.80 (+12.78%)</td><td>139.70 (-7.67%)</td><td>63.19 <b>(+431.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>168.56 (n/a)</td><td>167.40 (n/a)</td><td>151.30 (n/a)</td><td>11.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (-15.58%)</td><td>0.20 (-9.42%)</td><td>0.21 (-12.21%)</td><td>0.17 <b>(+27.29%)</b></td><td>0.02 <b>(-59.58%)</b></td><td>189.00 <b>(-21.41%)</b></td><td>163.48 (+5.15%)</td><td>156.10 (+13.86%)</td><td>144.80 (+18.49%)</td><td>17.26 <b>(-64.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>240.50 (n/a)</td><td>155.48 (n/a)</td><td>137.10 (n/a)</td><td>122.20 (n/a)</td><td>48.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.24 (+15.86%)</td><td>0.20 <b>(+28.53%)</b></td><td>0.19 (+9.90%)</td><td>0.16 <b>(+68.72%)</b></td><td>0.04 <b>(-20.73%)</b></td><td>205.60 <b>(-40.73%)</b></td><td>169.00 <b>(-26.55%)</b></td><td>176.00 (-9.00%)</td><td>134.80 (-13.65%)</td><td>30.83 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>346.90 (n/a)</td><td>230.10 (n/a)</td><td>193.40 (n/a)</td><td>156.10 (n/a)</td><td>78.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (-8.53%)</td><td>0.19 (-15.00%)</td><td>0.19 <b>(-21.13%)</b></td><td>0.15 (-5.95%)</td><td>0.03 (-14.58%)</td><td>219.30 (+6.35%)</td><td>179.46 (+17.19%)</td><td>174.30 <b>(+26.76%)</b></td><td>144.70 (+9.37%)</td><td>31.37 (-0.01%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.20 (n/a)</td><td>153.14 (n/a)</td><td>137.50 (n/a)</td><td>132.30 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.21 (-3.76%)</td><td>0.17 (-6.97%)</td><td>0.17 (-7.43%)</td><td>0.16 (+9.21%)</td><td>0.02 <b>(-27.46%)</b></td><td>206.90 (-8.45%)</td><td>189.68 (+6.36%)</td><td>191.30 (+8.02%)</td><td>156.20 (+3.86%)</td><td>20.62 <b>(-31.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>226.00 (n/a)</td><td>178.34 (n/a)</td><td>177.10 (n/a)</td><td>150.40 (n/a)</td><td>29.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (-5.14%)</td><td>0.18 (-11.60%)</td><td>0.18 (-8.45%)</td><td>0.15 (-18.93%)</td><td>0.03 (+9.18%)</td><td>219.40 <b>(+23.33%)</b></td><td>180.90 (+13.83%)</td><td>182.40 (+9.22%)</td><td>144.30 (+5.41%)</td><td>26.98 <b>(+42.44%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>177.90 (n/a)</td><td>158.92 (n/a)</td><td>167.00 (n/a)</td><td>136.90 (n/a)</td><td>18.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (-7.12%)</td><td>0.22 (-7.77%)</td><td>0.21 (-15.39%)</td><td>0.17 (-5.49%)</td><td>0.03 (-15.10%)</td><td>191.00 (+5.82%)</td><td>154.10 (+7.93%)</td><td>153.90 (+18.20%)</td><td>129.20 (+7.67%)</td><td>24.98 (-4.01%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.50 (n/a)</td><td>142.78 (n/a)</td><td>130.20 (n/a)</td><td>120.00 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (-4.08%)</td><td>0.21 (-3.19%)</td><td>0.20 (-14.10%)</td><td>0.19 <b>(+39.89%)</b></td><td>0.03 <b>(-50.26%)</b></td><td>175.60 <b>(-28.50%)</b></td><td>159.94 (-2.07%)</td><td>165.40 (+16.40%)</td><td>128.20 (+4.23%)</td><td>18.58 <b>(-63.55%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>245.60 (n/a)</td><td>163.32 (n/a)</td><td>142.10 (n/a)</td><td>123.00 (n/a)</td><td>50.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (+3.34%)</td><td>0.19 (-0.26%)</td><td>0.19 (+3.22%)</td><td>0.16 (-2.64%)</td><td>0.03 (+11.30%)</td><td>206.60 (+2.68%)</td><td>172.58 (+0.64%)</td><td>174.30 (-3.11%)</td><td>130.20 (-3.20%)</td><td>27.35 (+8.67%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.20 (n/a)</td><td>171.48 (n/a)</td><td>179.90 (n/a)</td><td>134.50 (n/a)</td><td>25.17 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (-16.68%)</td><td>0.18 (-11.69%)</td><td>0.19 (-13.58%)</td><td>0.15 (-6.09%)</td><td>0.02 <b>(-38.69%)</b></td><td>213.70 (+6.48%)</td><td>182.20 (+11.63%)</td><td>176.90 (+15.70%)</td><td>159.90 <b>(+20.05%)</b></td><td>23.48 <b>(-23.12%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.70 (n/a)</td><td>163.22 (n/a)</td><td>152.90 (n/a)</td><td>133.20 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (-17.80%)</td><td>0.17 (-13.99%)</td><td>0.17 (-11.69%)</td><td>0.14 (-17.86%)</td><td>0.02 <b>(-26.38%)</b></td><td>242.00 <b>(+21.73%)</b></td><td>196.76 (+15.88%)</td><td>188.70 (+13.27%)</td><td>169.00 <b>(+21.67%)</b></td><td>27.52 (+10.24%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>198.80 (n/a)</td><td>169.80 (n/a)</td><td>166.60 (n/a)</td><td>138.90 (n/a)</td><td>24.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (-18.92%)</td><td>0.17 (-9.02%)</td><td>0.17 (+5.63%)</td><td>0.13 (-2.72%)</td><td>0.03 <b>(-48.33%)</b></td><td>242.90 (+2.79%)</td><td>192.82 (+5.38%)</td><td>191.60 (-5.34%)</td><td>151.80 <b>(+23.31%)</b></td><td>32.88 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>236.30 (n/a)</td><td>182.98 (n/a)</td><td>202.40 (n/a)</td><td>123.10 (n/a)</td><td>49.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (-0.17%)</td><td>0.18 (-0.17%)</td><td>0.18 (-0.16%)</td><td>0.18 (-0.26%)</td><td>0.00 <b>(+44.20%)</b></td><td>47565.20 (+0.26%)</td><td>47465.40 (+0.17%)</td><td>47471.70 (+0.16%)</td><td>47398.70 (+0.17%)</td><td>65.74 <b>(+44.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47441.80 (n/a)</td><td>47383.56 (n/a)</td><td>47394.30 (n/a)</td><td>47317.70 (n/a)</td><td>45.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.18 (-0.47%)</td><td>0.18 (+0.03%)</td><td>0.18 (+0.13%)</td><td>0.18 (+0.07%)</td><td>0.00 <b>(-50.27%)</b></td><td>47515.10 (-0.07%)</td><td>47371.04 (-0.03%)</td><td>47388.30 (-0.13%)</td><td>47257.30 (+0.47%)</td><td>100.04 <b>(-50.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47550.00 (n/a)</td><td>47386.10 (n/a)</td><td>47451.10 (n/a)</td><td>47037.00 (n/a)</td><td>200.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (+0.02%)</td><td>0.11 (+0.00%)</td><td>0.11 (-0.01%)</td><td>0.11 (-0.01%)</td><td>0.00 <b>(+64.40%)</b></td><td>374457.20 (+0.01%)</td><td>374339.90 (-0.00%)</td><td>374437.90 (+0.01%)</td><td>374092.40 (-0.02%)</td><td>158.94 <b>(+64.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374413.30 (n/a)</td><td>374341.64 (n/a)</td><td>374391.20 (n/a)</td><td>374180.20 (n/a)</td><td>96.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 <b>(-29.37%)</b></td><td>0.03 (-0.98%)</td><td>0.03 (+7.32%)</td><td>0.02 <b>(+33.61%)</b></td><td>0.00 <b>(-68.18%)</b></td><td>177.90 <b>(-25.16%)</b></td><td>154.52 (-5.69%)</td><td>145.60 (-6.85%)</td><td>141.00 <b>(+41.57%)</b></td><td>16.88 <b>(-65.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>163.84 (n/a)</td><td>156.30 (n/a)</td><td>99.60 (n/a)</td><td>49.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 (-19.35%)</td><td>0.03 <b>(-20.31%)</b></td><td>0.04 (-7.20%)</td><td>0.02 <b>(-37.98%)</b></td><td>0.01 <b>(+49.06%)</b></td><td>287.60 <b>(+61.21%)</b></td><td>199.56 <b>(+30.57%)</b></td><td>165.10 (+7.77%)</td><td>161.40 <b>(+24.06%)</b></td><td>55.07 <b>(+190.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>152.84 (n/a)</td><td>153.20 (n/a)</td><td>130.10 (n/a)</td><td>18.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-2.98%)</td><td>0.03 (+3.46%)</td><td>0.03 <b>(+27.29%)</b></td><td>0.01 <b>(-25.66%)</b></td><td>0.01 (+16.15%)</td><td>341.90 <b>(+34.55%)</b></td><td>177.54 (+3.75%)</td><td>134.20 <b>(-21.43%)</b></td><td>121.60 (+3.05%)</td><td>93.40 <b>(+70.79%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.10 (n/a)</td><td>171.12 (n/a)</td><td>170.80 (n/a)</td><td>118.00 (n/a)</td><td>54.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 <b>(-22.18%)</b></td><td>0.03 (-8.58%)</td><td>0.03 (-8.72%)</td><td>0.02 (+5.95%)</td><td>0.00 <b>(-53.06%)</b></td><td>215.10 (-5.62%)</td><td>173.68 (+5.64%)</td><td>164.40 (+9.60%)</td><td>153.70 <b>(+28.51%)</b></td><td>24.09 <b>(-42.53%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>164.40 (n/a)</td><td>150.00 (n/a)</td><td>119.60 (n/a)</td><td>41.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 <b>(-27.95%)</b></td><td>0.02 (-7.86%)</td><td>0.03 (+15.21%)</td><td>0.02 (+17.47%)</td><td>0.00 <b>(-68.37%)</b></td><td>210.40 (-14.85%)</td><td>170.08 (+0.04%)</td><td>161.00 (-13.21%)</td><td>153.00 <b>(+38.84%)</b></td><td>23.11 <b>(-59.47%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.10 (n/a)</td><td>170.02 (n/a)</td><td>185.50 (n/a)</td><td>110.20 (n/a)</td><td>57.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-16.83%)</td><td>0.03 (-12.06%)</td><td>0.03 (-13.67%)</td><td>0.03 (-1.46%)</td><td>0.00 <b>(-48.50%)</b></td><td>199.90 (+1.47%)</td><td>172.78 (+11.86%)</td><td>163.50 (+15.88%)</td><td>158.90 <b>(+20.20%)</b></td><td>17.93 <b>(-36.66%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>154.46 (n/a)</td><td>141.10 (n/a)</td><td>132.20 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-7.29%)</td><td>0.03 (+3.13%)</td><td>0.03 (+12.87%)</td><td>0.03 (+17.81%)</td><td>0.00 <b>(-54.41%)</b></td><td>161.40 (-15.14%)</td><td>144.80 (-6.14%)</td><td>143.90 (-11.39%)</td><td>127.80 (+7.94%)</td><td>14.68 <b>(-56.78%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>154.28 (n/a)</td><td>162.40 (n/a)</td><td>118.40 (n/a)</td><td>33.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 <b>(+20.76%)</b></td><td>0.03 <b>(+40.22%)</b></td><td>0.03 <b>(+53.09%)</b></td><td>0.03 <b>(+34.57%)</b></td><td>0.00 (-8.47%)</td><td>170.80 <b>(-25.71%)</b></td><td>143.14 <b>(-29.28%)</b></td><td>136.00 <b>(-34.68%)</b></td><td>131.10 (-17.18%)</td><td>16.31 <b>(-42.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.90 (n/a)</td><td>202.40 (n/a)</td><td>208.20 (n/a)</td><td>158.30 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.04 <b>(+49.33%)</b></td><td>0.03 <b>(+28.48%)</b></td><td>0.02 (+12.64%)</td><td>0.02 (+6.62%)</td><td>0.01 <b>(+284.63%)</b></td><td>202.50 (-6.21%)</td><td>157.62 (-18.60%)</td><td>171.40 (-11.24%)</td><td>116.50 <b>(-33.05%)</b></td><td>38.34 <b>(+130.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.90 (n/a)</td><td>193.64 (n/a)</td><td>193.10 (n/a)</td><td>174.00 (n/a)</td><td>16.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-13.43%)</td><td>0.02 (-6.60%)</td><td>0.02 (+5.57%)</td><td>0.02 <b>(+21.71%)</b></td><td>0.00 <b>(-58.79%)</b></td><td>208.30 (-17.86%)</td><td>189.76 (+1.38%)</td><td>192.30 (-5.27%)</td><td>153.70 (+15.56%)</td><td>21.32 <b>(-59.25%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.60 (n/a)</td><td>187.18 (n/a)</td><td>203.00 (n/a)</td><td>133.00 (n/a)</td><td>52.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-0.27%)</td><td>0.02 (+14.79%)</td><td>0.03 (+2.30%)</td><td>0.02 <b>(+67.22%)</b></td><td>0.00 <b>(-61.19%)</b></td><td>193.30 <b>(-40.21%)</b></td><td>170.78 (-19.68%)</td><td>163.30 (-2.27%)</td><td>152.20 (+0.26%)</td><td>18.05 <b>(-76.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>323.30 (n/a)</td><td>212.62 (n/a)</td><td>167.10 (n/a)</td><td>151.80 (n/a)</td><td>75.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (-16.08%)</td><td>0.02 (-2.50%)</td><td>0.02 (+4.26%)</td><td>0.02 <b>(+34.68%)</b></td><td>0.00 <b>(-60.89%)</b></td><td>212.70 <b>(-25.76%)</b></td><td>195.26 (-3.43%)</td><td>205.20 (-4.07%)</td><td>161.00 (+19.17%)</td><td>20.77 <b>(-65.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>286.50 (n/a)</td><td>202.20 (n/a)</td><td>213.90 (n/a)</td><td>135.10 (n/a)</td><td>59.51 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (+14.93%)</td><td>0.02 (+1.25%)</td><td>0.02 (+1.62%)</td><td>0.02 (-9.99%)</td><td>0.01 <b>(+56.34%)</b></td><td>229.90 (+11.12%)</td><td>185.18 (+1.46%)</td><td>192.30 (-1.64%)</td><td>119.60 (-12.95%)</td><td>40.84 <b>(+45.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.90 (n/a)</td><td>182.52 (n/a)</td><td>195.50 (n/a)</td><td>137.40 (n/a)</td><td>28.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.03 (+9.29%)</td><td>0.02 (+2.21%)</td><td>0.02 (-2.57%)</td><td>0.02 (-7.51%)</td><td>0.00 <b>(+62.32%)</b></td><td>242.00 (+8.13%)</td><td>206.94 (-0.84%)</td><td>219.90 (+2.66%)</td><td>158.90 (-8.52%)</td><td>32.43 <b>(+61.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>208.70 (n/a)</td><td>214.20 (n/a)</td><td>173.70 (n/a)</td><td>20.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.02 (+6.36%)</td><td>0.02 (+9.75%)</td><td>0.02 (+15.76%)</td><td>0.02 (-5.17%)</td><td>0.00 <b>(+32.70%)</b></td><td>269.70 (+5.43%)</td><td>209.94 (-8.10%)</td><td>197.80 (-13.62%)</td><td>180.40 (-5.99%)</td><td>35.57 <b>(+32.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.80 (n/a)</td><td>228.44 (n/a)</td><td>229.00 (n/a)</td><td>191.90 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(+40.12%)</b></td><td>0.05 <b>(+21.16%)</b></td><td>0.05 (+6.98%)</td><td>0.05 (+19.25%)</td><td>0.01 <b>(+112.94%)</b></td><td>180.30 (-16.14%)</td><td>153.10 (-16.10%)</td><td>163.60 (-6.51%)</td><td>117.20 <b>(-28.67%)</b></td><td>26.54 <b>(+27.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.00 (n/a)</td><td>182.48 (n/a)</td><td>175.00 (n/a)</td><td>164.30 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 <b>(+44.98%)</b></td><td>0.08 <b>(+28.23%)</b></td><td>0.08 <b>(+22.59%)</b></td><td>0.07 (+8.38%)</td><td>0.02 <b>(+401.42%)</b></td><td>184.40 (-7.75%)</td><td>151.34 <b>(-20.06%)</b></td><td>152.70 (-18.43%)</td><td>122.50 <b>(-30.99%)</b></td><td>27.24 <b>(+211.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>189.32 (n/a)</td><td>187.20 (n/a)</td><td>177.50 (n/a)</td><td>8.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (-16.71%)</td><td>0.04 (-9.95%)</td><td>0.04 (-1.56%)</td><td>0.03 <b>(-23.49%)</b></td><td>0.01 (-5.65%)</td><td>287.30 <b>(+30.71%)</b></td><td>203.20 (+12.63%)</td><td>193.00 (+1.58%)</td><td>154.80 <b>(+20.09%)</b></td><td>52.63 <b>(+52.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>180.42 (n/a)</td><td>190.00 (n/a)</td><td>128.90 (n/a)</td><td>34.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 (+18.41%)</td><td>0.06 (+5.65%)</td><td>0.06 (-2.61%)</td><td>0.04 (-9.75%)</td><td>0.01 <b>(+103.16%)</b></td><td>231.20 (+10.78%)</td><td>179.80 (-2.70%)</td><td>179.80 (+2.68%)</td><td>135.70 (-15.56%)</td><td>39.12 <b>(+84.08%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>184.78 (n/a)</td><td>175.10 (n/a)</td><td>160.70 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(+65.42%)</b></td><td>0.05 <b>(+36.03%)</b></td><td>0.05 <b>(+22.34%)</b></td><td>0.04 <b>(+39.91%)</b></td><td>0.01 <b>(+87.51%)</b></td><td>219.80 <b>(-28.54%)</b></td><td>159.38 <b>(-25.13%)</b></td><td>152.90 (-18.28%)</td><td>109.50 <b>(-39.54%)</b></td><td>43.02 <b>(-20.05%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.60 (n/a)</td><td>212.88 (n/a)</td><td>187.10 (n/a)</td><td>181.10 (n/a)</td><td>53.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 <b>(+22.98%)</b></td><td>0.06 (+10.17%)</td><td>0.05 (-10.65%)</td><td>0.05 (+4.73%)</td><td>0.02 <b>(+56.38%)</b></td><td>217.60 (-4.52%)</td><td>171.58 (-6.71%)</td><td>192.30 (+11.93%)</td><td>111.20 (-18.65%)</td><td>43.55 (+18.37%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>183.92 (n/a)</td><td>171.80 (n/a)</td><td>136.70 (n/a)</td><td>36.79 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 <b>(+28.30%)</b></td><td>0.05 (+19.09%)</td><td>0.05 (+2.49%)</td><td>0.05 <b>(+59.51%)</b></td><td>0.01 (-0.47%)</td><td>175.70 <b>(-37.29%)</b></td><td>153.96 (-18.75%)</td><td>162.00 (-2.41%)</td><td>108.30 <b>(-22.03%)</b></td><td>27.47 <b>(-52.41%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.20 (n/a)</td><td>189.50 (n/a)</td><td>166.00 (n/a)</td><td>138.90 (n/a)</td><td>57.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.08 <b>(+26.70%)</b></td><td>0.06 (+18.93%)</td><td>0.06 <b>(+21.52%)</b></td><td>0.04 (+6.73%)</td><td>0.01 <b>(+71.63%)</b></td><td>207.10 (-6.29%)</td><td>158.46 (-13.76%)</td><td>152.30 (-17.72%)</td><td>112.30 <b>(-21.08%)</b></td><td>37.73 <b>(+29.73%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>183.74 (n/a)</td><td>185.10 (n/a)</td><td>142.30 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 <b>(+36.08%)</b></td><td>0.06 (+16.60%)</td><td>0.05 (+2.02%)</td><td>0.05 (+3.07%)</td><td>0.01 <b>(+349.49%)</b></td><td>175.70 (-2.98%)</td><td>149.66 (-11.74%)</td><td>162.70 (-1.99%)</td><td>116.90 <b>(-26.52%)</b></td><td>28.38 <b>(+216.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>169.56 (n/a)</td><td>166.00 (n/a)</td><td>159.10 (n/a)</td><td>8.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.07 (-13.63%)</td><td>0.06 (+3.34%)</td><td>0.06 <b>(+24.26%)</b></td><td>0.04 (+3.06%)</td><td>0.01 <b>(-34.35%)</b></td><td>215.60 (-2.97%)</td><td>166.44 (-5.94%)</td><td>158.50 (-19.50%)</td><td>132.50 (+15.82%)</td><td>32.65 <b>(-24.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>222.20 (n/a)</td><td>176.96 (n/a)</td><td>196.90 (n/a)</td><td>114.40 (n/a)</td><td>43.38 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 <b>(-25.24%)</b></td><td>0.04 <b>(-20.50%)</b></td><td>0.04 <b>(-24.31%)</b></td><td>0.04 (+17.03%)</td><td>0.00 <b>(-66.21%)</b></td><td>231.50 (-14.54%)</td><td>195.82 (+17.17%)</td><td>189.60 <b>(+32.13%)</b></td><td>167.00 <b>(+33.81%)</b></td><td>23.70 <b>(-61.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.90 (n/a)</td><td>167.12 (n/a)</td><td>143.50 (n/a)</td><td>124.80 (n/a)</td><td>60.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 <b>(+26.83%)</b></td><td>0.04 (+15.24%)</td><td>0.05 <b>(+23.28%)</b></td><td>0.03 (-11.82%)</td><td>0.01 <b>(+84.80%)</b></td><td>339.60 (+13.39%)</td><td>213.54 (-8.41%)</td><td>188.80 (-18.87%)</td><td>146.80 <b>(-21.16%)</b></td><td>75.11 <b>(+72.19%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.50 (n/a)</td><td>233.16 (n/a)</td><td>232.70 (n/a)</td><td>186.20 (n/a)</td><td>43.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 (+5.47%)</td><td>0.04 (+4.04%)</td><td>0.04 (+1.41%)</td><td>0.04 <b>(+21.99%)</b></td><td>0.01 <b>(-20.29%)</b></td><td>218.50 (-18.04%)</td><td>189.20 (-5.38%)</td><td>197.10 (-1.40%)</td><td>154.60 (-5.15%)</td><td>26.11 <b>(-37.66%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.60 (n/a)</td><td>199.96 (n/a)</td><td>199.90 (n/a)</td><td>163.00 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.06 <b>(+38.21%)</b></td><td>0.05 <b>(+22.55%)</b></td><td>0.04 (+7.00%)</td><td>0.04 <b>(+42.71%)</b></td><td>0.01 <b>(+33.42%)</b></td><td>204.80 <b>(-29.91%)</b></td><td>185.20 (-18.55%)</td><td>199.50 (-6.51%)</td><td>147.30 <b>(-27.65%)</b></td><td>24.43 <b>(-33.53%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.20 (n/a)</td><td>227.38 (n/a)</td><td>213.40 (n/a)</td><td>203.60 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.05 <b>(+20.06%)</b></td><td>0.04 (+9.11%)</td><td>0.04 (+2.54%)</td><td>0.03 (-2.32%)</td><td>0.00 <b>(+150.34%)</b></td><td>239.60 (+2.39%)</td><td>204.20 (-7.44%)</td><td>208.70 (-2.48%)</td><td>175.10 (-16.70%)</td><td>25.30 <b>(+111.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>234.00 (n/a)</td><td>220.62 (n/a)</td><td>214.00 (n/a)</td><td>210.20 (n/a)</td><td>11.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (-17.43%)</td><td>0.10 (+2.02%)</td><td>0.10 (+5.31%)</td><td>0.09 (+17.17%)</td><td>0.01 <b>(-58.95%)</b></td><td>184.00 (-14.66%)</td><td>160.62 (-5.60%)</td><td>159.90 (-4.99%)</td><td>137.60 <b>(+21.13%)</b></td><td>16.50 <b>(-56.50%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>215.60 (n/a)</td><td>170.14 (n/a)</td><td>168.30 (n/a)</td><td>113.60 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (+0.95%)</td><td>0.14 (+5.86%)</td><td>0.14 (+8.95%)</td><td>0.13 (+13.14%)</td><td>0.02 (-19.02%)</td><td>189.50 (-11.61%)</td><td>174.40 (-6.31%)</td><td>181.00 (-8.22%)</td><td>140.80 (-0.91%)</td><td>19.73 <b>(-28.27%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.40 (n/a)</td><td>186.14 (n/a)</td><td>197.20 (n/a)</td><td>142.10 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (+5.30%)</td><td>0.10 (+4.25%)</td><td>0.10 (+2.20%)</td><td>0.09 (+11.97%)</td><td>0.01 (-3.51%)</td><td>191.20 (-10.70%)</td><td>165.14 (-4.42%)</td><td>164.40 (-2.14%)</td><td>138.10 (-5.02%)</td><td>20.74 (-19.64%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>172.78 (n/a)</td><td>168.00 (n/a)</td><td>145.40 (n/a)</td><td>25.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (-10.27%)</td><td>0.11 (+5.39%)</td><td>0.09 (-3.09%)</td><td>0.09 <b>(+21.16%)</b></td><td>0.03 (-11.87%)</td><td>238.20 (-17.46%)</td><td>197.52 (-6.56%)</td><td>222.20 (+3.20%)</td><td>146.30 (+11.42%)</td><td>46.62 (-17.17%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>288.60 (n/a)</td><td>211.38 (n/a)</td><td>215.30 (n/a)</td><td>131.30 (n/a)</td><td>56.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (+11.79%)</td><td>0.10 (+16.81%)</td><td>0.10 (+19.78%)</td><td>0.09 (+18.58%)</td><td>0.01 (-6.70%)</td><td>188.00 (-15.70%)</td><td>165.70 (-15.02%)</td><td>168.40 (-16.51%)</td><td>134.20 (-10.59%)</td><td>20.55 <b>(-30.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>194.98 (n/a)</td><td>201.70 (n/a)</td><td>150.10 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (+2.65%)</td><td>0.12 (-4.05%)</td><td>0.11 (-3.80%)</td><td>0.08 (-13.51%)</td><td>0.03 <b>(+27.55%)</b></td><td>243.30 (+15.58%)</td><td>185.80 (+6.73%)</td><td>190.00 (+3.94%)</td><td>134.20 (-2.61%)</td><td>47.14 <b>(+43.80%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>210.50 (n/a)</td><td>174.08 (n/a)</td><td>182.80 (n/a)</td><td>137.80 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 <b>(+37.49%)</b></td><td>0.11 (+19.65%)</td><td>0.11 <b>(+31.75%)</b></td><td>0.07 (-9.36%)</td><td>0.02 <b>(+162.37%)</b></td><td>222.90 (+10.35%)</td><td>159.84 (-13.46%)</td><td>147.80 <b>(-24.13%)</b></td><td>118.10 <b>(-27.28%)</b></td><td>38.93 <b>(+117.26%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>184.70 (n/a)</td><td>194.80 (n/a)</td><td>162.40 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 <b>(+31.46%)</b></td><td>0.11 (+13.94%)</td><td>0.11 (+17.75%)</td><td>0.08 (-3.31%)</td><td>0.02 <b>(+178.66%)</b></td><td>223.90 (+3.42%)</td><td>176.78 (-9.21%)</td><td>169.30 (-15.05%)</td><td>129.00 <b>(-23.94%)</b></td><td>39.15 <b>(+124.73%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>194.72 (n/a)</td><td>199.30 (n/a)</td><td>169.60 (n/a)</td><td>17.42 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 <b>(+39.73%)</b></td><td>0.11 (+8.92%)</td><td>0.10 (-1.51%)</td><td>0.09 (-1.60%)</td><td>0.02 <b>(+382.70%)</b></td><td>180.70 (+1.63%)</td><td>155.32 (-5.38%)</td><td>165.30 (+1.54%)</td><td>112.60 <b>(-28.46%)</b></td><td>29.07 <b>(+254.26%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>177.80 (n/a)</td><td>164.16 (n/a)</td><td>162.80 (n/a)</td><td>157.40 (n/a)</td><td>8.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (+12.78%)</td><td>0.10 (+4.48%)</td><td>0.10 (+5.93%)</td><td>0.08 (-5.68%)</td><td>0.02 <b>(+97.88%)</b></td><td>226.10 (+6.00%)</td><td>188.52 (-2.26%)</td><td>189.70 (-5.57%)</td><td>149.90 (-11.30%)</td><td>35.21 <b>(+87.17%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>192.88 (n/a)</td><td>200.90 (n/a)</td><td>169.00 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (+5.48%)</td><td>0.09 (+0.93%)</td><td>0.09 (-2.48%)</td><td>0.08 (+1.89%)</td><td>0.02 (+17.90%)</td><td>216.70 (-1.86%)</td><td>179.90 (-0.27%)</td><td>188.90 (+2.55%)</td><td>130.50 (-5.16%)</td><td>32.40 (+8.80%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.80 (n/a)</td><td>180.38 (n/a)</td><td>184.20 (n/a)</td><td>137.60 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (-6.24%)</td><td>0.09 (+9.03%)</td><td>0.09 (+8.93%)</td><td>0.08 <b>(+44.58%)</b></td><td>0.01 <b>(-51.25%)</b></td><td>215.90 <b>(-30.82%)</b></td><td>191.14 (-12.84%)</td><td>193.50 (-8.21%)</td><td>160.60 (+6.64%)</td><td>22.45 <b>(-64.06%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>312.10 (n/a)</td><td>219.30 (n/a)</td><td>210.80 (n/a)</td><td>150.60 (n/a)</td><td>62.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (+9.21%)</td><td>0.09 (+0.95%)</td><td>0.10 (+8.85%)</td><td>0.05 <b>(-30.22%)</b></td><td>0.02 <b>(+188.18%)</b></td><td>300.10 <b>(+43.31%)</b></td><td>194.76 (+4.70%)</td><td>163.90 (-8.13%)</td><td>155.60 (-8.42%)</td><td>61.11 <b>(+279.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>186.02 (n/a)</td><td>178.40 (n/a)</td><td>169.90 (n/a)</td><td>16.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 (-4.98%)</td><td>0.09 (-8.45%)</td><td>0.08 (+2.56%)</td><td>0.07 (-12.27%)</td><td>0.02 (-9.88%)</td><td>247.30 (+14.02%)</td><td>209.20 (+9.04%)</td><td>207.20 (-2.49%)</td><td>158.20 (+5.26%)</td><td>33.69 (+4.19%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.90 (n/a)</td><td>191.86 (n/a)</td><td>212.50 (n/a)</td><td>150.30 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.09 (+2.51%)</td><td>0.08 (+1.82%)</td><td>0.09 (+9.94%)</td><td>0.06 (-8.09%)</td><td>0.01 <b>(+43.61%)</b></td><td>265.20 (+8.78%)</td><td>207.04 (-0.47%)</td><td>191.60 (-9.07%)</td><td>173.70 (-2.42%)</td><td>37.88 <b>(+52.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>208.02 (n/a)</td><td>210.70 (n/a)</td><td>178.00 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 <b>(-20.68%)</b></td><td>0.17 (-17.24%)</td><td>0.17 (-8.86%)</td><td>0.14 (-11.49%)</td><td>0.03 <b>(-39.06%)</b></td><td>231.70 (+12.97%)</td><td>194.44 (+17.93%)</td><td>190.20 (+9.69%)</td><td>145.20 <b>(+26.04%)</b></td><td>34.21 (-14.01%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>205.10 (n/a)</td><td>164.88 (n/a)</td><td>173.40 (n/a)</td><td>115.20 (n/a)</td><td>39.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (+6.57%)</td><td>0.19 (-7.14%)</td><td>0.19 (-4.50%)</td><td>0.09 <b>(-43.61%)</b></td><td>0.07 <b>(+84.06%)</b></td><td>358.60 <b>(+77.35%)</b></td><td>196.72 (+19.95%)</td><td>172.30 (+4.74%)</td><td>119.90 (-6.18%)</td><td>93.13 <b>(+235.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.20 (n/a)</td><td>164.00 (n/a)</td><td>164.50 (n/a)</td><td>127.80 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (-17.37%)</td><td>0.22 (-9.02%)</td><td>0.22 (+1.90%)</td><td>0.19 (+3.12%)</td><td>0.02 <b>(-55.00%)</b></td><td>211.90 (-3.02%)</td><td>188.82 (+6.77%)</td><td>190.00 (-1.86%)</td><td>158.50 <b>(+20.99%)</b></td><td>19.65 <b>(-47.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>218.50 (n/a)</td><td>176.84 (n/a)</td><td>193.60 (n/a)</td><td>131.00 (n/a)</td><td>37.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.29 <b>(+34.75%)</b></td><td>0.23 <b>(+27.08%)</b></td><td>0.20 (+13.90%)</td><td>0.18 <b>(+29.61%)</b></td><td>0.05 <b>(+76.92%)</b></td><td>181.60 <b>(-22.85%)</b></td><td>149.32 <b>(-20.08%)</b></td><td>164.70 (-12.21%)</td><td>112.90 <b>(-25.77%)</b></td><td>30.63 (-1.61%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.40 (n/a)</td><td>186.84 (n/a)</td><td>187.60 (n/a)</td><td>152.10 (n/a)</td><td>31.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 <b>(+26.74%)</b></td><td>0.23 (+16.30%)</td><td>0.24 <b>(+22.99%)</b></td><td>0.19 (+0.33%)</td><td>0.04 <b>(+238.75%)</b></td><td>221.10 (-0.32%)</td><td>183.76 (-11.98%)</td><td>169.20 (-18.69%)</td><td>151.20 <b>(-21.09%)</b></td><td>33.84 <b>(+172.00%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>208.76 (n/a)</td><td>208.10 (n/a)</td><td>191.60 (n/a)</td><td>12.44 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 <b>(-30.70%)</b></td><td>0.20 (-3.45%)</td><td>0.21 (+5.99%)</td><td>0.18 (+8.14%)</td><td>0.02 <b>(-71.01%)</b></td><td>186.40 (-7.54%)</td><td>161.52 (-1.93%)</td><td>157.50 (-5.69%)</td><td>146.60 <b>(+44.29%)</b></td><td>15.88 <b>(-60.96%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>201.60 (n/a)</td><td>164.70 (n/a)</td><td>167.00 (n/a)</td><td>101.60 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 <b>(+48.85%)</b></td><td>0.22 (+17.14%)</td><td>0.20 (+1.73%)</td><td>0.15 (-5.49%)</td><td>0.07 <b>(+256.49%)</b></td><td>253.00 (+5.81%)</td><td>180.18 (-7.97%)</td><td>182.50 (-1.72%)</td><td>122.60 <b>(-32.82%)</b></td><td>57.77 <b>(+137.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>239.10 (n/a)</td><td>195.78 (n/a)</td><td>185.70 (n/a)</td><td>182.50 (n/a)</td><td>24.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 <b>(-31.77%)</b></td><td>0.18 <b>(-21.11%)</b></td><td>0.17 <b>(-20.24%)</b></td><td>0.15 (-17.44%)</td><td>0.02 <b>(-50.87%)</b></td><td>215.80 <b>(+21.17%)</b></td><td>187.18 <b>(+24.94%)</b></td><td>188.50 <b>(+25.42%)</b></td><td>164.20 <b>(+46.61%)</b></td><td>22.12 (-13.16%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>178.10 (n/a)</td><td>149.82 (n/a)</td><td>150.30 (n/a)</td><td>112.00 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 <b>(-23.32%)</b></td><td>0.21 (-4.72%)</td><td>0.18 (-1.27%)</td><td>0.17 (+2.52%)</td><td>0.04 <b>(-47.65%)</b></td><td>217.10 (-2.47%)</td><td>184.78 (-0.69%)</td><td>199.70 (+1.32%)</td><td>131.00 <b>(+30.35%)</b></td><td>33.38 <b>(-32.51%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.37 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>222.60 (n/a)</td><td>186.06 (n/a)</td><td>197.10 (n/a)</td><td>100.50 (n/a)</td><td>49.46 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (-6.32%)</td><td>0.18 (-7.19%)</td><td>0.18 (-4.10%)</td><td>0.14 (-16.38%)</td><td>0.02 (+19.51%)</td><td>235.00 (+19.59%)</td><td>188.14 (+8.59%)</td><td>182.20 (+4.23%)</td><td>161.00 (+6.76%)</td><td>28.93 <b>(+55.05%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>173.26 (n/a)</td><td>174.80 (n/a)</td><td>150.80 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 <b>(-21.02%)</b></td><td>0.17 (-6.89%)</td><td>0.17 (-0.20%)</td><td>0.15 (+2.85%)</td><td>0.01 <b>(-65.40%)</b></td><td>226.40 (-2.79%)</td><td>211.50 (+5.73%)</td><td>210.00 (+0.19%)</td><td>199.40 <b>(+26.60%)</b></td><td>12.45 <b>(-57.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>232.90 (n/a)</td><td>200.04 (n/a)</td><td>209.60 (n/a)</td><td>157.50 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (+5.71%)</td><td>0.16 (-7.11%)</td><td>0.16 (-7.94%)</td><td>0.10 <b>(-32.12%)</b></td><td>0.05 <b>(+82.11%)</b></td><td>321.00 <b>(+47.32%)</b></td><td>215.42 (+13.76%)</td><td>203.20 (+8.61%)</td><td>144.10 (-5.45%)</td><td>67.18 <b>(+156.88%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.90 (n/a)</td><td>189.36 (n/a)</td><td>187.10 (n/a)</td><td>152.40 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 (-13.97%)</td><td>0.18 (+1.60%)</td><td>0.18 (+6.89%)</td><td>0.15 (+18.30%)</td><td>0.02 <b>(-52.15%)</b></td><td>232.20 (-15.47%)</td><td>198.00 (-4.50%)</td><td>197.60 (-6.48%)</td><td>172.60 (+16.23%)</td><td>21.83 <b>(-52.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>274.70 (n/a)</td><td>207.32 (n/a)</td><td>211.30 (n/a)</td><td>148.50 (n/a)</td><td>45.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (-5.76%)</td><td>0.15 (-9.99%)</td><td>0.15 (-13.43%)</td><td>0.12 (+0.84%)</td><td>0.02 <b>(-30.18%)</b></td><td>265.30 (-0.82%)</td><td>226.26 (+9.95%)</td><td>223.70 (+15.55%)</td><td>190.70 (+6.12%)</td><td>26.65 <b>(-26.83%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>267.50 (n/a)</td><td>205.78 (n/a)</td><td>193.60 (n/a)</td><td>179.70 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (+1.16%)</td><td>0.11 (+8.04%)</td><td>0.10 (-1.20%)</td><td>0.09 <b>(+61.82%)</b></td><td>0.02 <b>(-35.24%)</b></td><td>217.30 <b>(-38.20%)</b></td><td>191.60 (-12.61%)</td><td>199.30 (+1.22%)</td><td>150.50 (-1.12%)</td><td>29.09 <b>(-62.25%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>351.60 (n/a)</td><td>219.24 (n/a)</td><td>196.90 (n/a)</td><td>152.20 (n/a)</td><td>77.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (-14.89%)</td><td>0.12 (-13.44%)</td><td>0.11 (-18.01%)</td><td>0.10 (-8.41%)</td><td>0.02 <b>(-31.61%)</b></td><td>204.90 (+9.16%)</td><td>173.86 (+14.44%)</td><td>178.20 <b>(+21.97%)</b></td><td>146.50 (+17.48%)</td><td>22.99 (-12.87%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>187.70 (n/a)</td><td>151.92 (n/a)</td><td>146.10 (n/a)</td><td>124.70 (n/a)</td><td>26.38 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (+4.58%)</td><td>0.13 (+2.88%)</td><td>0.12 (+1.92%)</td><td>0.11 (+11.78%)</td><td>0.03 (-14.26%)</td><td>185.10 (-10.54%)</td><td>162.44 (-4.48%)</td><td>177.80 (-1.88%)</td><td>117.80 (-4.38%)</td><td>29.51 <b>(-26.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>206.90 (n/a)</td><td>170.06 (n/a)</td><td>181.20 (n/a)</td><td>123.20 (n/a)</td><td>40.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (-12.61%)</td><td>0.12 (-1.85%)</td><td>0.11 (-2.33%)</td><td>0.11 (+10.32%)</td><td>0.02 <b>(-40.41%)</b></td><td>192.20 (-9.34%)</td><td>172.12 (-0.98%)</td><td>180.10 (+2.39%)</td><td>135.80 (+14.41%)</td><td>23.81 <b>(-38.63%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>212.00 (n/a)</td><td>173.82 (n/a)</td><td>175.90 (n/a)</td><td>118.70 (n/a)</td><td>38.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (-11.05%)</td><td>0.10 (-18.57%)</td><td>0.09 <b>(-22.82%)</b></td><td>0.07 <b>(-29.72%)</b></td><td>0.02 <b>(+55.03%)</b></td><td>278.50 <b>(+42.31%)</b></td><td>219.32 <b>(+25.66%)</b></td><td>226.00 <b>(+29.59%)</b></td><td>176.10 (+12.45%)</td><td>43.53 <b>(+140.95%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>174.54 (n/a)</td><td>174.40 (n/a)</td><td>156.60 (n/a)</td><td>18.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (-15.20%)</td><td>0.12 (-11.39%)</td><td>0.12 (-17.05%)</td><td>0.11 (-1.90%)</td><td>0.01 <b>(-41.86%)</b></td><td>189.50 (+1.94%)</td><td>169.56 (+11.67%)</td><td>174.10 <b>(+20.57%)</b></td><td>149.10 (+17.87%)</td><td>15.74 <b>(-31.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>151.84 (n/a)</td><td>144.40 (n/a)</td><td>126.50 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (+1.71%)</td><td>0.11 (-9.68%)</td><td>0.11 (-8.46%)</td><td>0.06 <b>(-41.17%)</b></td><td>0.03 <b>(+124.70%)</b></td><td>328.20 <b>(+69.96%)</b></td><td>197.30 (+19.71%)</td><td>179.30 (+9.26%)</td><td>138.20 (-1.64%)</td><td>75.56 <b>(+296.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>164.82 (n/a)</td><td>164.10 (n/a)</td><td>140.50 (n/a)</td><td>19.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 <b>(-29.84%)</b></td><td>0.11 (-17.59%)</td><td>0.11 (-15.97%)</td><td>0.10 (-18.80%)</td><td>0.02 <b>(-42.61%)</b></td><td>214.20 <b>(+23.17%)</b></td><td>186.58 (+19.96%)</td><td>194.20 (+19.00%)</td><td>157.50 <b>(+42.53%)</b></td><td>26.28 (+1.55%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>173.90 (n/a)</td><td>155.54 (n/a)</td><td>163.20 (n/a)</td><td>110.50 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (+0.93%)</td><td>0.14 (-16.63%)</td><td>0.14 <b>(-24.73%)</b></td><td>0.09 <b>(-37.05%)</b></td><td>0.04 <b>(+97.40%)</b></td><td>264.50 <b>(+58.86%)</b></td><td>180.72 <b>(+26.08%)</b></td><td>178.30 <b>(+32.86%)</b></td><td>127.80 (-0.85%)</td><td>52.18 <b>(+216.67%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>166.50 (n/a)</td><td>143.34 (n/a)</td><td>134.20 (n/a)</td><td>128.90 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.19 (-6.49%)</td><td>0.15 (-9.10%)</td><td>0.14 (-11.99%)</td><td>0.13 (-1.95%)</td><td>0.02 (-15.54%)</td><td>193.90 (+2.00%)</td><td>166.98 (+9.45%)</td><td>174.40 (+13.62%)</td><td>132.20 (+6.96%)</td><td>23.79 (-8.59%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.10 (n/a)</td><td>152.56 (n/a)</td><td>153.50 (n/a)</td><td>123.60 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (-19.39%)</td><td>0.14 (-6.96%)</td><td>0.14 (-5.48%)</td><td>0.13 (+7.57%)</td><td>0.02 <b>(-51.73%)</b></td><td>195.10 (-7.05%)</td><td>171.62 (+4.34%)</td><td>178.30 (+5.82%)</td><td>150.30 <b>(+24.01%)</b></td><td>19.97 <b>(-45.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>209.90 (n/a)</td><td>164.48 (n/a)</td><td>168.50 (n/a)</td><td>121.20 (n/a)</td><td>36.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (+5.24%)</td><td>0.16 (-3.01%)</td><td>0.13 <b>(-23.70%)</b></td><td>0.11 (-2.39%)</td><td>0.05 (+19.29%)</td><td>233.40 (+2.46%)</td><td>169.60 (+4.98%)</td><td>188.30 <b>(+31.04%)</b></td><td>111.00 (-4.97%)</td><td>50.11 (+11.31%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>227.80 (n/a)</td><td>161.56 (n/a)</td><td>143.70 (n/a)</td><td>116.80 (n/a)</td><td>45.01 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (-15.78%)</td><td>0.13 (-14.28%)</td><td>0.12 (-17.32%)</td><td>0.09 <b>(-31.30%)</b></td><td>0.03 <b>(+20.44%)</b></td><td>287.90 <b>(+45.55%)</b></td><td>205.74 <b>(+20.95%)</b></td><td>206.20 <b>(+21.01%)</b></td><td>149.00 (+18.73%)</td><td>58.21 <b>(+98.90%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.80 (n/a)</td><td>170.10 (n/a)</td><td>170.40 (n/a)</td><td>125.50 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (-1.53%)</td><td>0.17 (+6.46%)</td><td>0.17 (+7.06%)</td><td>0.14 <b>(+30.52%)</b></td><td>0.03 <b>(-32.97%)</b></td><td>172.10 <b>(-23.41%)</b></td><td>144.80 (-9.80%)</td><td>147.60 (-6.64%)</td><td>112.40 (+1.54%)</td><td>23.79 <b>(-47.56%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>224.70 (n/a)</td><td>160.54 (n/a)</td><td>158.10 (n/a)</td><td>110.70 (n/a)</td><td>45.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (-12.49%)</td><td>0.14 (-6.87%)</td><td>0.13 (-14.69%)</td><td>0.12 (+16.69%)</td><td>0.01 <b>(-47.44%)</b></td><td>199.50 (-14.30%)</td><td>182.28 (+5.16%)</td><td>189.50 (+17.26%)</td><td>161.50 (+14.21%)</td><td>17.40 <b>(-50.57%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.80 (n/a)</td><td>173.34 (n/a)</td><td>161.60 (n/a)</td><td>141.40 (n/a)</td><td>35.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.17 (-14.24%)</td><td>0.14 (-4.07%)</td><td>0.15 (-2.84%)</td><td>0.12 (+7.66%)</td><td>0.02 <b>(-46.31%)</b></td><td>206.40 (-7.11%)</td><td>174.20 (+1.54%)</td><td>167.90 (+2.88%)</td><td>148.40 (+16.58%)</td><td>21.85 <b>(-41.86%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>222.20 (n/a)</td><td>171.56 (n/a)</td><td>163.20 (n/a)</td><td>127.30 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.11 <b>(-21.75%)</b></td><td>0.10 <b>(-21.24%)</b></td><td>0.10 (-17.87%)</td><td>0.09 (-13.60%)</td><td>0.01 <b>(-33.55%)</b></td><td>208.50 (+15.77%)</td><td>188.58 <b>(+26.44%)</b></td><td>181.00 <b>(+21.72%)</b></td><td>165.10 <b>(+27.79%)</b></td><td>18.94 (-0.98%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>149.14 (n/a)</td><td>148.70 (n/a)</td><td>129.20 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.10 <b>(-31.93%)</b></td><td>0.09 <b>(-21.17%)</b></td><td>0.09 (-18.69%)</td><td>0.09 (+0.17%)</td><td>0.01 <b>(-65.36%)</b></td><td>216.00 (-0.18%)</td><td>198.62 <b>(+22.77%)</b></td><td>205.80 <b>(+23.01%)</b></td><td>176.40 <b>(+46.88%)</b></td><td>18.69 <b>(-49.06%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.40 (n/a)</td><td>161.78 (n/a)</td><td>167.30 (n/a)</td><td>120.10 (n/a)</td><td>36.70 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.16 (+11.25%)</td><td>0.12 (+12.41%)</td><td>0.11 (+3.59%)</td><td>0.07 (+13.10%)</td><td>0.03 (+15.32%)</td><td>250.50 (-11.58%)</td><td>170.46 (-10.87%)</td><td>172.10 (-3.48%)</td><td>117.10 (-10.13%)</td><td>52.39 (-10.89%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>283.30 (n/a)</td><td>191.24 (n/a)</td><td>178.30 (n/a)</td><td>130.30 (n/a)</td><td>58.79 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 <b>(-26.84%)</b></td><td>0.10 (-19.21%)</td><td>0.11 (-8.33%)</td><td>0.06 <b>(-39.14%)</b></td><td>0.02 (-9.65%)</td><td>302.10 <b>(+64.36%)</b></td><td>192.24 <b>(+27.23%)</b></td><td>166.60 (+9.03%)</td><td>158.00 <b>(+36.68%)</b></td><td>61.54 <b>(+109.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>183.80 (n/a)</td><td>151.10 (n/a)</td><td>152.80 (n/a)</td><td>115.60 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.15 (-3.03%)</td><td>0.11 (-14.02%)</td><td>0.10 <b>(-24.52%)</b></td><td>0.09 (+0.47%)</td><td>0.02 (-10.74%)</td><td>206.60 (-0.48%)</td><td>180.36 (+15.32%)</td><td>184.60 <b>(+32.52%)</b></td><td>125.10 (+3.13%)</td><td>32.61 (-11.47%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>207.60 (n/a)</td><td>156.40 (n/a)</td><td>139.30 (n/a)</td><td>121.30 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 (+0.51%)</td><td>0.11 (-13.97%)</td><td>0.10 <b>(-25.74%)</b></td><td>0.09 (-6.34%)</td><td>0.02 (+11.15%)</td><td>204.60 (+6.73%)</td><td>176.06 (+16.89%)</td><td>185.50 <b>(+34.62%)</b></td><td>129.70 (-0.46%)</td><td>29.19 (+15.00%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>191.70 (n/a)</td><td>150.62 (n/a)</td><td>137.80 (n/a)</td><td>130.30 (n/a)</td><td>25.38 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.13 (-1.34%)</td><td>0.09 (-5.70%)</td><td>0.09 (-7.79%)</td><td>0.06 <b>(-27.18%)</b></td><td>0.03 <b>(+41.23%)</b></td><td>294.80 <b>(+37.37%)</b></td><td>208.88 (+10.06%)</td><td>211.10 (+8.42%)</td><td>144.90 (+1.40%)</td><td>57.80 <b>(+95.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>189.78 (n/a)</td><td>194.70 (n/a)</td><td>142.90 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.14 <b>(+21.32%)</b></td><td>0.10 (+1.04%)</td><td>0.11 (+2.42%)</td><td>0.07 (-18.64%)</td><td>0.03 <b>(+187.15%)</b></td><td>250.00 <b>(+22.91%)</b></td><td>188.90 (+3.46%)</td><td>175.50 (-2.34%)</td><td>134.00 (-17.54%)</td><td>47.34 <b>(+194.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>182.58 (n/a)</td><td>179.70 (n/a)</td><td>162.50 (n/a)</td><td>16.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.56 <b>(-29.63%)</b></td><td>0.52 (-17.17%)</td><td>0.54 (-12.50%)</td><td>0.46 (+2.74%)</td><td>0.04 <b>(-75.65%)</b></td><td>214.90 (-2.67%)</td><td>189.98 (+14.72%)</td><td>183.00 (+14.23%)</td><td>175.80 <b>(+42.12%)</b></td><td>15.39 <b>(-64.85%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.79 (n/a)</td><td>0.63 (n/a)</td><td>0.61 (n/a)</td><td>0.45 (n/a)</td><td>0.16 (n/a)</td><td>220.80 (n/a)</td><td>165.60 (n/a)</td><td>160.20 (n/a)</td><td>123.70 (n/a)</td><td>43.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.59 <b>(-20.11%)</b></td><td>0.53 (-8.44%)</td><td>0.56 (-4.60%)</td><td>0.46 (+0.93%)</td><td>0.06 <b>(-43.04%)</b></td><td>215.60 (-0.96%)</td><td>189.00 (+7.29%)</td><td>175.60 (+4.77%)</td><td>167.10 <b>(+25.17%)</b></td><td>23.93 <b>(-29.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.74 (n/a)</td><td>0.58 (n/a)</td><td>0.59 (n/a)</td><td>0.45 (n/a)</td><td>0.11 (n/a)</td><td>217.70 (n/a)</td><td>176.16 (n/a)</td><td>167.60 (n/a)</td><td>133.50 (n/a)</td><td>33.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.87 (-9.83%)</td><td>0.59 (-14.44%)</td><td>0.55 (-11.69%)</td><td>0.48 (-13.30%)</td><td>0.16 (-2.35%)</td><td>204.80 (+15.32%)</td><td>173.24 (+17.87%)</td><td>179.10 (+13.21%)</td><td>113.20 (+10.87%)</td><td>37.45 <b>(+26.12%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.96 (n/a)</td><td>0.70 (n/a)</td><td>0.62 (n/a)</td><td>0.55 (n/a)</td><td>0.16 (n/a)</td><td>177.60 (n/a)</td><td>146.98 (n/a)</td><td>158.20 (n/a)</td><td>102.10 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.70 (-8.36%)</td><td>0.52 (-9.73%)</td><td>0.47 (-16.16%)</td><td>0.46 (+16.62%)</td><td>0.10 <b>(-25.02%)</b></td><td>213.10 (-14.25%)</td><td>192.80 (+8.35%)</td><td>207.50 (+19.25%)</td><td>140.10 (+9.11%)</td><td>30.23 <b>(-32.25%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.77 (n/a)</td><td>0.58 (n/a)</td><td>0.57 (n/a)</td><td>0.40 (n/a)</td><td>0.14 (n/a)</td><td>248.50 (n/a)</td><td>177.94 (n/a)</td><td>174.00 (n/a)</td><td>128.40 (n/a)</td><td>44.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.62 (+0.84%)</td><td>0.47 (+2.04%)</td><td>0.40 (-6.92%)</td><td>0.35 (+3.98%)</td><td>0.13 <b>(+26.42%)</b></td><td>212.00 (-3.81%)</td><td>167.02 (-0.11%)</td><td>182.90 (+7.46%)</td><td>119.70 (-0.83%)</td><td>42.48 (+17.48%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.61 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>220.40 (n/a)</td><td>167.20 (n/a)</td><td>170.20 (n/a)</td><td>120.70 (n/a)</td><td>36.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.71 <b>(+26.13%)</b></td><td>0.43 (+10.26%)</td><td>0.40 (+12.30%)</td><td>0.28 (+18.26%)</td><td>0.16 <b>(+29.92%)</b></td><td>260.50 (-15.45%)</td><td>185.20 (-8.91%)</td><td>184.90 (-10.98%)</td><td>104.30 <b>(-20.74%)</b></td><td>55.45 (-18.00%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>308.10 (n/a)</td><td>203.32 (n/a)</td><td>207.70 (n/a)</td><td>131.60 (n/a)</td><td>67.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.69 <b>(+35.88%)</b></td><td>0.42 (-2.62%)</td><td>0.36 <b>(-23.97%)</b></td><td>0.31 (-6.40%)</td><td>0.16 <b>(+75.68%)</b></td><td>238.60 (+6.80%)</td><td>192.68 (+7.33%)</td><td>207.50 <b>(+31.50%)</b></td><td>106.40 <b>(-26.42%)</b></td><td>51.16 <b>(+26.97%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>223.40 (n/a)</td><td>179.52 (n/a)</td><td>157.80 (n/a)</td><td>144.60 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.63 <b>(+26.84%)</b></td><td>0.47 (+3.84%)</td><td>0.47 (+4.15%)</td><td>0.30 <b>(-29.45%)</b></td><td>0.12 <b>(+296.12%)</b></td><td>248.60 <b>(+41.73%)</b></td><td>166.62 (+2.05%)</td><td>155.20 (-4.02%)</td><td>116.80 <b>(-21.13%)</b></td><td>49.64 <b>(+356.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.50 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.42 (n/a)</td><td>0.03 (n/a)</td><td>175.40 (n/a)</td><td>163.28 (n/a)</td><td>161.70 (n/a)</td><td>148.10 (n/a)</td><td>10.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (-11.03%)</td><td>0.21 (-15.85%)</td><td>0.20 (-15.64%)</td><td>0.17 (-9.04%)</td><td>0.04 <b>(-27.87%)</b></td><td>217.10 (+9.98%)</td><td>182.64 (+17.33%)</td><td>186.90 (+18.59%)</td><td>137.10 (+12.38%)</td><td>29.53 (-10.33%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>197.40 (n/a)</td><td>155.66 (n/a)</td><td>157.60 (n/a)</td><td>122.00 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.29 (+8.98%)</td><td>0.24 (+6.21%)</td><td>0.24 (+17.11%)</td><td>0.19 (-1.74%)</td><td>0.04 (+16.28%)</td><td>198.10 (+1.80%)</td><td>157.56 (-5.30%)</td><td>151.40 (-14.66%)</td><td>125.00 (-8.22%)</td><td>28.98 (+11.25%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>194.60 (n/a)</td><td>166.38 (n/a)</td><td>177.40 (n/a)</td><td>136.20 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (+1.93%)</td><td>0.22 (-4.92%)</td><td>0.22 (-5.27%)</td><td>0.15 <b>(-22.73%)</b></td><td>0.07 <b>(+103.11%)</b></td><td>239.80 <b>(+29.41%)</b></td><td>176.98 (+11.81%)</td><td>166.70 (+5.57%)</td><td>124.60 (-1.89%)</td><td>54.26 <b>(+160.43%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>185.30 (n/a)</td><td>158.28 (n/a)</td><td>157.90 (n/a)</td><td>127.00 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.29 (-16.84%)</td><td>0.21 <b>(-20.67%)</b></td><td>0.19 <b>(-27.85%)</b></td><td>0.16 <b>(-20.68%)</b></td><td>0.05 (-4.97%)</td><td>230.80 <b>(+26.05%)</b></td><td>182.02 <b>(+27.41%)</b></td><td>194.60 <b>(+38.60%)</b></td><td>129.10 <b>(+20.20%)</b></td><td>39.90 <b>(+42.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>183.10 (n/a)</td><td>142.86 (n/a)</td><td>140.40 (n/a)</td><td>107.40 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.31 (+12.88%)</td><td>0.23 (+5.86%)</td><td>0.21 (-1.26%)</td><td>0.20 <b>(+25.31%)</b></td><td>0.04 (-13.79%)</td><td>179.90 <b>(-20.19%)</b></td><td>161.88 (-7.39%)</td><td>171.90 (+1.30%)</td><td>119.60 (-11.41%)</td><td>25.11 <b>(-38.26%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>225.40 (n/a)</td><td>174.80 (n/a)</td><td>169.70 (n/a)</td><td>135.00 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.22 (-0.07%)</td><td>0.18 (-2.82%)</td><td>0.18 (-2.46%)</td><td>0.16 (-3.15%)</td><td>0.02 (+11.95%)</td><td>236.70 (+3.23%)</td><td>204.80 (+3.17%)</td><td>204.40 (+2.51%)</td><td>171.00 (+0.06%)</td><td>24.74 (+15.07%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>229.30 (n/a)</td><td>198.50 (n/a)</td><td>199.40 (n/a)</td><td>170.90 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.20 <b>(-31.93%)</b></td><td>0.17 <b>(-31.42%)</b></td><td>0.17 <b>(-32.90%)</b></td><td>0.14 (-15.28%)</td><td>0.03 <b>(-50.64%)</b></td><td>265.60 (+18.04%)</td><td>223.02 <b>(+42.23%)</b></td><td>219.60 <b>(+48.98%)</b></td><td>182.60 <b>(+46.90%)</b></td><td>33.15 (-16.94%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>225.00 (n/a)</td><td>156.80 (n/a)</td><td>147.40 (n/a)</td><td>124.30 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (-4.20%)</td><td>0.17 (-15.65%)</td><td>0.18 (-15.15%)</td><td>0.11 <b>(-29.16%)</b></td><td>0.04 <b>(+44.29%)</b></td><td>324.40 <b>(+41.17%)</b></td><td>231.62 <b>(+23.24%)</b></td><td>205.70 (+17.88%)</td><td>162.80 (+4.36%)</td><td>64.14 <b>(+114.00%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>229.80 (n/a)</td><td>187.94 (n/a)</td><td>174.50 (n/a)</td><td>156.00 (n/a)</td><td>29.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.35 (+15.65%)</td><td>0.26 (+4.16%)</td><td>0.26 (+10.65%)</td><td>0.20 (-2.17%)</td><td>0.06 <b>(+20.57%)</b></td><td>208.30 (+2.21%)</td><td>162.14 (-3.17%)</td><td>160.20 (-9.59%)</td><td>116.10 (-13.49%)</td><td>34.14 (+9.25%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>167.44 (n/a)</td><td>177.20 (n/a)</td><td>134.20 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (-7.84%)</td><td>0.23 (-1.83%)</td><td>0.22 (+2.07%)</td><td>0.20 (+6.07%)</td><td>0.02 <b>(-39.61%)</b></td><td>207.40 (-5.73%)</td><td>182.30 (+0.52%)</td><td>185.50 (-2.06%)</td><td>159.30 (+8.51%)</td><td>18.33 <b>(-37.55%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>220.00 (n/a)</td><td>181.36 (n/a)</td><td>189.40 (n/a)</td><td>146.80 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.31 (-4.73%)</td><td>0.24 (-4.84%)</td><td>0.23 (-8.73%)</td><td>0.20 (+6.60%)</td><td>0.04 (-12.07%)</td><td>202.90 (-6.20%)</td><td>171.32 (+4.32%)</td><td>178.10 (+9.60%)</td><td>132.40 (+5.00%)</td><td>28.25 (-15.09%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>216.30 (n/a)</td><td>164.22 (n/a)</td><td>162.50 (n/a)</td><td>126.10 (n/a)</td><td>33.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.42 <b>(+33.45%)</b></td><td>0.28 (+4.12%)</td><td>0.24 (-4.46%)</td><td>0.19 (-17.55%)</td><td>0.09 <b>(+191.88%)</b></td><td>210.50 <b>(+21.26%)</b></td><td>159.68 (+2.78%)</td><td>168.40 (+4.66%)</td><td>97.20 <b>(-25.06%)</b></td><td>46.12 <b>(+166.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>173.60 (n/a)</td><td>155.36 (n/a)</td><td>160.90 (n/a)</td><td>129.70 (n/a)</td><td>17.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (-16.69%)</td><td>0.25 (+3.50%)</td><td>0.26 (+17.28%)</td><td>0.22 (+11.04%)</td><td>0.03 <b>(-50.13%)</b></td><td>185.50 (-9.91%)</td><td>164.12 (-5.58%)</td><td>154.90 (-14.75%)</td><td>146.90 <b>(+20.02%)</b></td><td>17.93 <b>(-43.60%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>205.90 (n/a)</td><td>173.82 (n/a)</td><td>181.70 (n/a)</td><td>122.40 (n/a)</td><td>31.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.30 (+3.33%)</td><td>0.25 (+5.55%)</td><td>0.24 (+3.18%)</td><td>0.21 (+8.70%)</td><td>0.03 (-8.46%)</td><td>193.90 (-8.02%)</td><td>168.16 (-5.71%)</td><td>171.50 (-3.11%)</td><td>135.90 (-3.27%)</td><td>21.05 (-19.06%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>210.80 (n/a)</td><td>178.34 (n/a)</td><td>177.00 (n/a)</td><td>140.50 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (-9.47%)</td><td>0.21 (-19.16%)</td><td>0.20 <b>(-21.74%)</b></td><td>0.11 <b>(-46.82%)</b></td><td>0.07 <b>(+64.65%)</b></td><td>363.80 <b>(+88.01%)</b></td><td>218.98 <b>(+34.43%)</b></td><td>206.20 <b>(+27.84%)</b></td><td>147.50 (+10.49%)</td><td>86.92 <b>(+241.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>193.50 (n/a)</td><td>162.90 (n/a)</td><td>161.30 (n/a)</td><td>133.50 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (+11.81%)</td><td>0.20 (-2.55%)</td><td>0.19 (-11.45%)</td><td>0.15 (+6.42%)</td><td>0.05 (+7.03%)</td><td>278.90 (-6.03%)</td><td>213.22 (+2.22%)</td><td>212.90 (+12.94%)</td><td>146.80 (-10.54%)</td><td>46.79 (-13.34%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>296.80 (n/a)</td><td>208.58 (n/a)</td><td>188.50 (n/a)</td><td>164.10 (n/a)</td><td>53.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (-14.73%)</td><td>0.22 (-3.46%)</td><td>0.24 (+11.20%)</td><td>0.16 (-10.26%)</td><td>0.04 (-14.68%)</td><td>213.30 (+11.44%)</td><td>161.36 (+3.48%)</td><td>142.40 (-10.04%)</td><td>130.90 (+17.29%)</td><td>34.98 (+12.37%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>191.40 (n/a)</td><td>155.94 (n/a)</td><td>158.30 (n/a)</td><td>111.60 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 <b>(-21.81%)</b></td><td>0.19 <b>(-25.03%)</b></td><td>0.19 <b>(-26.85%)</b></td><td>0.14 <b>(-27.70%)</b></td><td>0.03 (-10.88%)</td><td>249.60 <b>(+38.28%)</b></td><td>189.20 <b>(+34.41%)</b></td><td>181.20 <b>(+36.75%)</b></td><td>152.30 <b>(+27.88%)</b></td><td>36.93 <b>(+56.70%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>180.50 (n/a)</td><td>140.76 (n/a)</td><td>132.50 (n/a)</td><td>119.10 (n/a)</td><td>23.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 (+5.16%)</td><td>0.22 (+16.89%)</td><td>0.23 <b>(+31.76%)</b></td><td>0.16 (+19.00%)</td><td>0.04 (-12.93%)</td><td>213.20 (-15.96%)</td><td>165.06 (-16.14%)</td><td>154.60 <b>(-24.10%)</b></td><td>125.50 (-4.92%)</td><td>34.04 <b>(-29.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>253.70 (n/a)</td><td>196.82 (n/a)</td><td>203.70 (n/a)</td><td>132.00 (n/a)</td><td>47.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 <b>(-29.92%)</b></td><td>0.20 (-19.29%)</td><td>0.20 (-4.70%)</td><td>0.16 (-18.31%)</td><td>0.02 <b>(-55.86%)</b></td><td>217.40 <b>(+22.48%)</b></td><td>180.64 <b>(+20.86%)</b></td><td>173.30 (+4.90%)</td><td>153.60 <b>(+42.75%)</b></td><td>23.73 <b>(-22.55%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>177.50 (n/a)</td><td>149.46 (n/a)</td><td>165.20 (n/a)</td><td>107.60 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.26 (-18.53%)</td><td>0.21 (-18.76%)</td><td>0.23 (-10.23%)</td><td>0.15 <b>(-28.15%)</b></td><td>0.05 (+1.53%)</td><td>240.00 <b>(+39.21%)</b></td><td>174.94 <b>(+25.51%)</b></td><td>151.20 (+11.42%)</td><td>135.20 <b>(+22.69%)</b></td><td>43.71 <b>(+74.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>172.40 (n/a)</td><td>139.38 (n/a)</td><td>135.70 (n/a)</td><td>110.20 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (-11.63%)</td><td>0.21 (+4.65%)</td><td>0.21 (+8.37%)</td><td>0.17 <b>(+75.44%)</b></td><td>0.03 <b>(-62.47%)</b></td><td>205.80 <b>(-43.01%)</b></td><td>169.28 (-15.02%)</td><td>167.90 (-7.75%)</td><td>150.10 (+13.20%)</td><td>22.36 <b>(-76.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>361.10 (n/a)</td><td>199.20 (n/a)</td><td>182.00 (n/a)</td><td>132.60 (n/a)</td><td>93.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.23 (-18.84%)</td><td>0.19 (-8.17%)</td><td>0.19 (-2.88%)</td><td>0.16 (+0.02%)</td><td>0.03 <b>(-44.66%)</b></td><td>221.00 (+0.00%)</td><td>189.14 (+6.23%)</td><td>182.00 (+3.00%)</td><td>153.70 <b>(+23.26%)</b></td><td>26.04 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>221.00 (n/a)</td><td>178.04 (n/a)</td><td>176.70 (n/a)</td><td>124.70 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.33 <b>(+51.94%)</b></td><td>0.21 (+9.39%)</td><td>0.18 (-13.65%)</td><td>0.12 <b>(-24.67%)</b></td><td>0.09 <b>(+228.74%)</b></td><td>279.70 <b>(+32.75%)</b></td><td>186.76 (+2.23%)</td><td>198.50 (+15.81%)</td><td>105.50 <b>(-34.19%)</b></td><td>70.79 <b>(+176.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>210.70 (n/a)</td><td>182.68 (n/a)</td><td>171.40 (n/a)</td><td>160.30 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.74 <b>(-31.47%)</b></td><td>0.69 <b>(-23.07%)</b></td><td>0.71 (-16.38%)</td><td>0.57 <b>(-29.41%)</b></td><td>0.07 <b>(-35.76%)</b></td><td>231.70 <b>(+41.63%)</b></td><td>192.34 <b>(+29.77%)</b></td><td>183.60 (+19.53%)</td><td>178.20 <b>(+45.95%)</b></td><td>22.40 <b>(+35.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.07 (n/a)</td><td>0.89 (n/a)</td><td>0.85 (n/a)</td><td>0.80 (n/a)</td><td>0.11 (n/a)</td><td>163.60 (n/a)</td><td>148.22 (n/a)</td><td>153.60 (n/a)</td><td>122.10 (n/a)</td><td>16.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.06 (+10.48%)</td><td>0.77 (-5.07%)</td><td>0.75 (-0.48%)</td><td>0.55 <b>(-20.30%)</b></td><td>0.18 <b>(+61.81%)</b></td><td>236.30 <b>(+25.49%)</b></td><td>177.60 (+8.31%)</td><td>174.80 (+0.46%)</td><td>123.90 (-9.50%)</td><td>40.33 <b>(+83.64%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.96 (n/a)</td><td>0.81 (n/a)</td><td>0.75 (n/a)</td><td>0.70 (n/a)</td><td>0.11 (n/a)</td><td>188.30 (n/a)</td><td>163.98 (n/a)</td><td>174.00 (n/a)</td><td>136.90 (n/a)</td><td>21.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.78 (-10.82%)</td><td>0.73 (-0.36%)</td><td>0.76 (-1.75%)</td><td>0.64 <b>(+38.90%)</b></td><td>0.06 <b>(-64.63%)</b></td><td>203.20 <b>(-28.02%)</b></td><td>179.34 (-4.18%)</td><td>171.40 (+1.78%)</td><td>167.10 (+12.07%)</td><td>14.76 <b>(-72.72%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.88 (n/a)</td><td>0.74 (n/a)</td><td>0.78 (n/a)</td><td>0.46 (n/a)</td><td>0.16 (n/a)</td><td>282.30 (n/a)</td><td>187.16 (n/a)</td><td>168.40 (n/a)</td><td>149.10 (n/a)</td><td>54.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.00 (+0.00%)</td><td>0.00 (+2.37%)</td><td>0.00 (+2.38%)</td><td>0.00 (+5.00%)</td><td>0.00 <b>(-43.59%)</b></td><td>974.43 (-4.49%)</td><td>954.74 (-1.94%)</td><td>959.94 (-2.04%)</td><td>938.73 (+1.24%)</td><td>15.49 <b>(-54.42%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1020.28 (n/a)</td><td>973.63 (n/a)</td><td>979.96 (n/a)</td><td>927.24 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.01 (-5.88%)</td><td>0.01 (-2.74%)</td><td>0.01 (-2.47%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(-38.33%)</b></td><td>1104.19 (-0.52%)</td><td>1046.24 (+2.32%)</td><td>1030.46 (+1.61%)</td><td>1025.16 (+6.90%)</td><td>33.52 <b>(-39.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1109.98 (n/a)</td><td>1022.52 (n/a)</td><td>1014.12 (n/a)</td><td>958.97 (n/a)</td><td>55.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.98 (-1.11%)</td><td>0.96 (+0.46%)</td><td>0.96 (+0.72%)</td><td>0.95 (+0.61%)</td><td>0.01 <b>(-35.02%)</b></td><td>2213.17 (-0.60%)</td><td>2177.35 (-0.47%)</td><td>2179.93 (-0.72%)</td><td>2147.63 (+1.13%)</td><td>25.63 <b>(-34.55%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2226.62 (n/a)</td><td>2187.63 (n/a)</td><td>2195.80 (n/a)</td><td>2123.59 (n/a)</td><td>39.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.42 (+2.61%)</td><td>0.40 (+1.51%)</td><td>0.40 (+1.84%)</td><td>0.39 (+0.34%)</td><td>0.01 <b>(+33.99%)</b></td><td>1361.90 (-0.33%)</td><td>1312.28 (-1.45%)</td><td>1317.52 (-1.82%)</td><td>1246.23 (-2.55%)</td><td>44.93 <b>(+30.44%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1366.35 (n/a)</td><td>1331.62 (n/a)</td><td>1341.93 (n/a)</td><td>1278.79 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.27 (+0.37%)</td><td>0.26 (-2.71%)</td><td>0.26 (-1.91%)</td><td>0.24 (-4.21%)</td><td>0.01 <b>(+80.52%)</b></td><td>2156.00 (+4.40%)</td><td>2030.90 (+2.93%)</td><td>1998.53 (+1.94%)</td><td>1914.65 (-0.38%)</td><td>103.54 <b>(+87.75%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2065.12 (n/a)</td><td>1973.07 (n/a)</td><td>1960.42 (n/a)</td><td>1922.04 (n/a)</td><td>55.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.38 (-1.23%)</td><td>0.37 (+1.46%)</td><td>0.37 (+2.28%)</td><td>0.36 (+1.58%)</td><td>0.01 <b>(-40.48%)</b></td><td>1452.13 (-1.58%)</td><td>1413.48 (-1.48%)</td><td>1408.65 (-2.21%)</td><td>1391.83 (+1.24%)</td><td>23.27 <b>(-40.72%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1475.40 (n/a)</td><td>1434.75 (n/a)</td><td>1440.55 (n/a)</td><td>1374.72 (n/a)</td><td>39.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>5.23 (-7.99%)</td><td>4.77 (+2.72%)</td><td>4.91 (+8.21%)</td><td>4.25 <b>(+25.52%)</b></td><td>0.46 <b>(-46.15%)</b></td><td>246.60 <b>(-20.32%)</b></td><td>221.62 (-4.79%)</td><td>213.70 (-7.61%)</td><td>200.70 (+8.66%)</td><td>21.73 <b>(-54.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>5.68 (n/a)</td><td>4.64 (n/a)</td><td>4.53 (n/a)</td><td>3.39 (n/a)</td><td>0.85 (n/a)</td><td>309.50 (n/a)</td><td>232.78 (n/a)</td><td>231.30 (n/a)</td><td>184.70 (n/a)</td><td>47.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.00 (+2.74%)</td><td>4.76 (-3.50%)</td><td>4.43 (-10.99%)</td><td>4.26 (-2.49%)</td><td>0.72 <b>(+20.07%)</b></td><td>246.20 (+2.58%)</td><td>223.70 (+4.10%)</td><td>236.50 (+12.35%)</td><td>174.80 (-2.67%)</td><td>29.17 (+17.07%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>5.84 (n/a)</td><td>4.94 (n/a)</td><td>4.98 (n/a)</td><td>4.37 (n/a)</td><td>0.60 (n/a)</td><td>240.00 (n/a)</td><td>214.88 (n/a)</td><td>210.50 (n/a)</td><td>179.60 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.06 (+12.72%)</td><td>4.82 (+4.44%)</td><td>4.58 (-1.86%)</td><td>3.83 (+1.48%)</td><td>0.83 <b>(+44.72%)</b></td><td>273.50 (-1.44%)</td><td>222.62 (-3.30%)</td><td>228.90 (+1.91%)</td><td>172.90 (-11.29%)</td><td>36.88 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>5.38 (n/a)</td><td>4.61 (n/a)</td><td>4.67 (n/a)</td><td>3.78 (n/a)</td><td>0.57 (n/a)</td><td>277.50 (n/a)</td><td>230.22 (n/a)</td><td>224.60 (n/a)</td><td>194.90 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>6.79 (+8.07%)</td><td>4.91 (+9.86%)</td><td>5.06 <b>(+23.21%)</b></td><td>2.83 (-16.45%)</td><td>1.45 <b>(+29.51%)</b></td><td>370.90 (+19.68%)</td><td>232.44 (-5.24%)</td><td>207.00 (-18.86%)</td><td>154.30 (-7.49%)</td><td>82.77 <b>(+54.66%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.29 (n/a)</td><td>4.47 (n/a)</td><td>4.11 (n/a)</td><td>3.38 (n/a)</td><td>1.12 (n/a)</td><td>309.90 (n/a)</td><td>245.30 (n/a)</td><td>255.10 (n/a)</td><td>166.80 (n/a)</td><td>53.52 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.96 (-10.30%)</td><td>8.30 (+6.56%)</td><td>8.23 (+6.57%)</td><td>7.84 <b>(+22.04%)</b></td><td>0.44 <b>(-66.93%)</b></td><td>267.60 (-18.04%)</td><td>253.20 (-7.95%)</td><td>255.00 (-6.15%)</td><td>234.10 (+11.48%)</td><td>13.32 <b>(-69.06%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.99 (n/a)</td><td>7.79 (n/a)</td><td>7.72 (n/a)</td><td>6.42 (n/a)</td><td>1.34 (n/a)</td><td>326.50 (n/a)</td><td>275.06 (n/a)</td><td>271.70 (n/a)</td><td>210.00 (n/a)</td><td>43.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.95 (+2.72%)</td><td>7.91 (+2.16%)</td><td>7.89 (+2.10%)</td><td>6.63 (-6.84%)</td><td>0.99 <b>(+56.27%)</b></td><td>316.30 (+7.33%)</td><td>268.58 (-1.34%)</td><td>265.70 (-2.06%)</td><td>234.30 (-2.66%)</td><td>34.67 <b>(+60.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.71 (n/a)</td><td>7.74 (n/a)</td><td>7.73 (n/a)</td><td>7.12 (n/a)</td><td>0.64 (n/a)</td><td>294.70 (n/a)</td><td>272.24 (n/a)</td><td>271.30 (n/a)</td><td>240.70 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.04 (-3.86%)</td><td>7.60 (-1.65%)</td><td>7.64 (-1.60%)</td><td>7.11 (+2.57%)</td><td>0.34 <b>(-36.91%)</b></td><td>295.00 (-2.51%)</td><td>276.32 (+1.45%)</td><td>274.60 (+1.63%)</td><td>260.80 (+4.03%)</td><td>12.46 <b>(-36.28%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.36 (n/a)</td><td>7.73 (n/a)</td><td>7.76 (n/a)</td><td>6.93 (n/a)</td><td>0.54 (n/a)</td><td>302.60 (n/a)</td><td>272.38 (n/a)</td><td>270.20 (n/a)</td><td>250.70 (n/a)</td><td>19.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>10.20 (+12.58%)</td><td>8.69 (+4.58%)</td><td>8.47 (-5.12%)</td><td>7.46 (+8.87%)</td><td>1.02 (+1.44%)</td><td>281.10 (-8.14%)</td><td>243.90 (-4.58%)</td><td>247.60 (+5.41%)</td><td>205.50 (-11.19%)</td><td>27.79 (-16.42%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.06 (n/a)</td><td>8.31 (n/a)</td><td>8.93 (n/a)</td><td>6.85 (n/a)</td><td>1.00 (n/a)</td><td>306.00 (n/a)</td><td>255.60 (n/a)</td><td>234.90 (n/a)</td><td>231.40 (n/a)</td><td>33.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.92 (-8.70%)</td><td>8.17 (-2.51%)</td><td>7.88 (-6.89%)</td><td>7.64 (+3.85%)</td><td>0.57 <b>(-43.60%)</b></td><td>274.60 (-3.68%)</td><td>257.74 (+1.81%)</td><td>266.20 (+7.38%)</td><td>235.00 (+9.56%)</td><td>17.40 <b>(-41.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.77 (n/a)</td><td>8.38 (n/a)</td><td>8.46 (n/a)</td><td>7.35 (n/a)</td><td>1.00 (n/a)</td><td>285.10 (n/a)</td><td>253.16 (n/a)</td><td>247.90 (n/a)</td><td>214.50 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>9.57 (+10.47%)</td><td>8.58 (+10.04%)</td><td>8.49 (+5.10%)</td><td>7.99 <b>(+26.00%)</b></td><td>0.59 <b>(-32.17%)</b></td><td>262.40 <b>(-20.65%)</b></td><td>245.16 (-9.82%)</td><td>247.10 (-4.85%)</td><td>219.00 (-9.47%)</td><td>15.97 <b>(-53.34%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.67 (n/a)</td><td>7.80 (n/a)</td><td>8.08 (n/a)</td><td>6.34 (n/a)</td><td>0.87 (n/a)</td><td>330.70 (n/a)</td><td>271.86 (n/a)</td><td>259.70 (n/a)</td><td>241.90 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>11.63 (-17.03%)</td><td>11.26 (-8.38%)</td><td>11.37 (-6.04%)</td><td>10.61 (-4.09%)</td><td>0.38 <b>(-69.89%)</b></td><td>395.20 (+4.27%)</td><td>372.82 (+8.35%)</td><td>368.80 (+6.44%)</td><td>360.70 <b>(+20.51%)</b></td><td>13.12 <b>(-62.21%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.02 (n/a)</td><td>12.29 (n/a)</td><td>12.10 (n/a)</td><td>11.07 (n/a)</td><td>1.27 (n/a)</td><td>379.00 (n/a)</td><td>344.10 (n/a)</td><td>346.50 (n/a)</td><td>299.30 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.71 (+6.05%)</td><td>12.49 (+7.15%)</td><td>12.02 (+2.60%)</td><td>11.67 (+18.40%)</td><td>1.27 (-14.90%)</td><td>359.50 (-15.55%)</td><td>338.22 (-7.17%)</td><td>348.90 (-2.51%)</td><td>285.10 (-5.72%)</td><td>30.58 <b>(-32.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.87 (n/a)</td><td>11.66 (n/a)</td><td>11.72 (n/a)</td><td>9.85 (n/a)</td><td>1.49 (n/a)</td><td>425.70 (n/a)</td><td>364.36 (n/a)</td><td>357.90 (n/a)</td><td>302.40 (n/a)</td><td>45.44 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>13.33 (+9.11%)</td><td>12.17 (+5.47%)</td><td>11.90 (+4.53%)</td><td>11.51 (+1.78%)</td><td>0.71 <b>(+84.58%)</b></td><td>364.50 (-1.75%)</td><td>345.60 (-5.03%)</td><td>352.40 (-4.34%)</td><td>314.60 (-8.36%)</td><td>19.17 <b>(+65.65%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>12.22 (n/a)</td><td>11.54 (n/a)</td><td>11.38 (n/a)</td><td>11.31 (n/a)</td><td>0.38 (n/a)</td><td>371.00 (n/a)</td><td>363.90 (n/a)</td><td>368.40 (n/a)</td><td>343.30 (n/a)</td><td>11.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>16.58 <b>(+28.21%)</b></td><td>13.22 (+10.90%)</td><td>12.50 (+2.94%)</td><td>12.00 (+10.09%)</td><td>1.89 <b>(+101.00%)</b></td><td>349.60 (-9.15%)</td><td>321.78 (-9.02%)</td><td>335.60 (-2.87%)</td><td>252.90 <b>(-22.02%)</b></td><td>38.99 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>12.94 (n/a)</td><td>11.92 (n/a)</td><td>12.14 (n/a)</td><td>10.90 (n/a)</td><td>0.94 (n/a)</td><td>384.80 (n/a)</td><td>353.70 (n/a)</td><td>345.50 (n/a)</td><td>324.30 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.12 (+1.28%)</td><td>13.16 (+3.11%)</td><td>13.56 (+7.38%)</td><td>12.03 (+4.20%)</td><td>0.85 (-14.44%)</td><td>348.80 (-4.02%)</td><td>319.70 (-3.16%)</td><td>309.30 (-6.89%)</td><td>297.00 (-1.26%)</td><td>21.19 (-18.05%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.94 (n/a)</td><td>12.77 (n/a)</td><td>12.63 (n/a)</td><td>11.54 (n/a)</td><td>1.00 (n/a)</td><td>363.40 (n/a)</td><td>330.12 (n/a)</td><td>332.20 (n/a)</td><td>300.80 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.75 (+2.66%)</td><td>13.51 (+8.60%)</td><td>13.33 (+9.79%)</td><td>12.12 (+6.55%)</td><td>1.16 (+1.33%)</td><td>346.20 (-6.13%)</td><td>312.26 (-7.95%)</td><td>314.60 (-8.89%)</td><td>284.40 (-2.57%)</td><td>26.88 (-6.90%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.37 (n/a)</td><td>12.44 (n/a)</td><td>12.15 (n/a)</td><td>11.37 (n/a)</td><td>1.14 (n/a)</td><td>368.80 (n/a)</td><td>339.22 (n/a)</td><td>345.30 (n/a)</td><td>291.90 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.44 (-1.31%)</td><td>12.60 (-1.87%)</td><td>12.69 (+0.65%)</td><td>9.77 (-18.19%)</td><td>1.82 <b>(+67.95%)</b></td><td>429.10 <b>(+22.25%)</b></td><td>339.06 (+3.28%)</td><td>330.60 (-0.63%)</td><td>290.40 (+1.33%)</td><td>54.67 <b>(+111.47%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.63 (n/a)</td><td>12.84 (n/a)</td><td>12.61 (n/a)</td><td>11.95 (n/a)</td><td>1.08 (n/a)</td><td>351.00 (n/a)</td><td>328.30 (n/a)</td><td>332.70 (n/a)</td><td>286.60 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>14.92 (+7.83%)</td><td>12.30 (-2.44%)</td><td>12.91 (+1.99%)</td><td>9.89 (-13.06%)</td><td>2.05 <b>(+133.82%)</b></td><td>424.00 (+15.03%)</td><td>348.88 (+4.46%)</td><td>325.00 (-1.96%)</td><td>281.10 (-7.26%)</td><td>59.41 <b>(+153.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.84 (n/a)</td><td>12.61 (n/a)</td><td>12.65 (n/a)</td><td>11.38 (n/a)</td><td>0.88 (n/a)</td><td>368.60 (n/a)</td><td>333.98 (n/a)</td><td>331.50 (n/a)</td><td>303.10 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.61 (+14.55%)</td><td>3.13 (+9.89%)</td><td>3.29 (+18.58%)</td><td>2.61 (+1.11%)</td><td>0.46 <b>(+84.15%)</b></td><td>200.90 (-1.08%)</td><td>170.80 (-7.89%)</td><td>159.40 (-15.66%)</td><td>145.30 (-12.68%)</td><td>26.00 <b>(+62.43%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.15 (n/a)</td><td>2.84 (n/a)</td><td>2.77 (n/a)</td><td>2.58 (n/a)</td><td>0.25 (n/a)</td><td>203.10 (n/a)</td><td>185.44 (n/a)</td><td>189.00 (n/a)</td><td>166.40 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>4.86 <b>(-21.12%)</b></td><td>3.95 (-15.65%)</td><td>3.71 (-17.81%)</td><td>3.02 (-16.07%)</td><td>0.76 (-17.78%)</td><td>347.00 (+19.16%)</td><td>273.32 (+18.64%)</td><td>282.70 <b>(+21.64%)</b></td><td>215.80 <b>(+26.79%)</b></td><td>53.33 <b>(+23.50%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.16 (n/a)</td><td>4.69 (n/a)</td><td>4.51 (n/a)</td><td>3.60 (n/a)</td><td>0.93 (n/a)</td><td>291.20 (n/a)</td><td>230.38 (n/a)</td><td>232.40 (n/a)</td><td>170.20 (n/a)</td><td>43.18 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>8.78 (-9.03%)</td><td>7.49 (-9.33%)</td><td>7.37 (-8.84%)</td><td>6.70 (-2.16%)</td><td>0.82 <b>(-34.37%)</b></td><td>313.00 (+2.22%)</td><td>282.62 (+9.28%)</td><td>284.70 (+9.71%)</td><td>238.90 (+9.94%)</td><td>28.96 <b>(-25.62%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.65 (n/a)</td><td>8.26 (n/a)</td><td>8.08 (n/a)</td><td>6.85 (n/a)</td><td>1.24 (n/a)</td><td>306.20 (n/a)</td><td>258.62 (n/a)</td><td>259.50 (n/a)</td><td>217.30 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>3.32 (+0.14%)</td><td>2.85 (-1.97%)</td><td>3.09 (+11.10%)</td><td>2.15 <b>(-21.52%)</b></td><td>0.47 <b>(+97.53%)</b></td><td>243.30 <b>(+27.45%)</b></td><td>188.60 (+4.06%)</td><td>169.80 (-9.97%)</td><td>157.80 (-0.13%)</td><td>35.01 <b>(+153.98%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.32 (n/a)</td><td>2.91 (n/a)</td><td>2.78 (n/a)</td><td>2.75 (n/a)</td><td>0.24 (n/a)</td><td>190.90 (n/a)</td><td>181.24 (n/a)</td><td>188.60 (n/a)</td><td>158.00 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.28 <b>(+32.50%)</b></td><td>0.22 (+8.52%)</td><td>0.24 (+12.62%)</td><td>0.10 <b>(-48.28%)</b></td><td>0.07 <b>(+599.85%)</b></td><td>333.60 <b>(+93.39%)</b></td><td>171.98 (+6.37%)</td><td>139.20 (-11.17%)</td><td>116.40 <b>(-24.56%)</b></td><td>91.05 <b>(+996.84%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>172.50 (n/a)</td><td>161.68 (n/a)</td><td>156.70 (n/a)</td><td>154.30 (n/a)</td><td>8.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.25 (+6.55%)</td><td>0.19 (-4.98%)</td><td>0.18 (-11.61%)</td><td>0.16 (-9.43%)</td><td>0.04 <b>(+58.44%)</b></td><td>210.60 (+10.38%)</td><td>174.28 (+7.00%)</td><td>181.90 (+13.12%)</td><td>128.90 (-6.19%)</td><td>30.72 <b>(+60.70%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>190.80 (n/a)</td><td>162.88 (n/a)</td><td>160.80 (n/a)</td><td>137.40 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.49 (-6.27%)</td><td>0.40 (+4.44%)</td><td>0.39 (+8.83%)</td><td>0.35 (+9.24%)</td><td>0.05 <b>(-35.39%)</b></td><td>186.10 (-8.46%)</td><td>165.00 (-6.06%)</td><td>169.90 (-8.11%)</td><td>132.90 (+6.66%)</td><td>19.95 <b>(-37.80%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>203.30 (n/a)</td><td>175.64 (n/a)</td><td>184.90 (n/a)</td><td>124.60 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.50 (+9.24%)</td><td>0.44 <b>(+22.40%)</b></td><td>0.44 <b>(+38.85%)</b></td><td>0.37 <b>(+32.54%)</b></td><td>0.05 <b>(-45.24%)</b></td><td>175.40 <b>(-24.53%)</b></td><td>150.30 <b>(-20.91%)</b></td><td>150.20 <b>(-28.00%)</b></td><td>131.40 (-8.43%)</td><td>16.30 <b>(-60.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>232.40 (n/a)</td><td>190.04 (n/a)</td><td>208.60 (n/a)</td><td>143.50 (n/a)</td><td>41.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.47 (-4.30%)</td><td>0.39 (-3.33%)</td><td>0.38 (-3.87%)</td><td>0.33 (-11.79%)</td><td>0.06 <b>(+37.71%)</b></td><td>200.50 (+13.34%)</td><td>171.20 (+4.68%)</td><td>174.60 (+4.05%)</td><td>140.70 (+4.53%)</td><td>27.54 <b>(+65.88%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>176.90 (n/a)</td><td>163.54 (n/a)</td><td>167.80 (n/a)</td><td>134.60 (n/a)</td><td>16.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.93 (-8.45%)</td><td>0.72 (-19.80%)</td><td>0.75 <b>(-25.47%)</b></td><td>0.40 <b>(-43.04%)</b></td><td>0.22 <b>(+45.20%)</b></td><td>329.30 <b>(+75.53%)</b></td><td>199.22 <b>(+33.85%)</b></td><td>175.60 <b>(+34.25%)</b></td><td>140.70 (+9.24%)</td><td>77.25 <b>(+185.84%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.02 (n/a)</td><td>0.90 (n/a)</td><td>1.00 (n/a)</td><td>0.70 (n/a)</td><td>0.15 (n/a)</td><td>187.60 (n/a)</td><td>148.84 (n/a)</td><td>130.80 (n/a)</td><td>128.80 (n/a)</td><td>27.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.88 (+0.96%)</td><td>0.76 (+12.23%)</td><td>0.81 <b>(+20.44%)</b></td><td>0.64 <b>(+29.20%)</b></td><td>0.10 <b>(-22.43%)</b></td><td>205.30 <b>(-22.59%)</b></td><td>174.24 (-12.42%)</td><td>162.20 (-16.99%)</td><td>149.60 (-0.93%)</td><td>24.68 <b>(-40.87%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.87 (n/a)</td><td>0.68 (n/a)</td><td>0.67 (n/a)</td><td>0.49 (n/a)</td><td>0.13 (n/a)</td><td>265.20 (n/a)</td><td>198.96 (n/a)</td><td>195.40 (n/a)</td><td>151.00 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>1.00 (-9.32%)</td><td>0.81 (-9.39%)</td><td>0.85 (-11.59%)</td><td>0.54 (-17.94%)</td><td>0.18 (-7.91%)</td><td>242.00 <b>(+21.85%)</b></td><td>169.38 (+11.00%)</td><td>155.10 (+13.13%)</td><td>130.90 (+10.28%)</td><td>43.63 <b>(+25.93%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.10 (n/a)</td><td>0.89 (n/a)</td><td>0.96 (n/a)</td><td>0.66 (n/a)</td><td>0.19 (n/a)</td><td>198.60 (n/a)</td><td>152.60 (n/a)</td><td>137.10 (n/a)</td><td>118.70 (n/a)</td><td>34.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.85 (-4.17%)</td><td>0.76 (-4.27%)</td><td>0.76 (-9.13%)</td><td>0.64 (+1.44%)</td><td>0.08 <b>(-34.32%)</b></td><td>205.20 (-1.44%)</td><td>174.52 (+3.38%)</td><td>171.50 (+10.01%)</td><td>153.40 (+4.35%)</td><td>18.87 <b>(-30.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.89 (n/a)</td><td>0.79 (n/a)</td><td>0.84 (n/a)</td><td>0.63 (n/a)</td><td>0.12 (n/a)</td><td>208.20 (n/a)</td><td>168.82 (n/a)</td><td>155.90 (n/a)</td><td>147.00 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:05:24</td><td>0.12 (+8.83%)</td><td>0.10 (+6.50%)</td><td>0.10 (+8.94%)</td><td>0.08 (+18.59%)</td><td>0.02 <b>(-20.23%)</b></td><td>197.80 (-15.69%)</td><td>171.30 (-7.88%)</td><td>171.80 (-8.23%)</td><td>132.10 (-8.14%)</td><td>24.39 <b>(-38.75%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.60 (n/a)</td><td>185.96 (n/a)</td><td>187.20 (n/a)</td><td>143.80 (n/a)</td><td>39.81 (n/a)</td>
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
