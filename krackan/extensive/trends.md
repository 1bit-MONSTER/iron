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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+14.00%)</td><td>0.04 (+10.68%)</td><td>0.04 (+2.57%)</td><td>0.03 (+9.97%)</td><td>0.01 <b>(+22.02%)</b></td><td>194.10 (-9.09%)</td><td>166.78 (-9.40%)</td><td>174.00 (-2.47%)</td><td>137.70 (-12.29%)</td><td>25.78 (-4.95%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>213.50 (n/a)</td><td>184.08 (n/a)</td><td>178.40 (n/a)</td><td>157.00 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+11.97%)</td><td>0.04 (+5.39%)</td><td>0.04 (+7.21%)</td><td>0.03 (+3.40%)</td><td>0.00 <b>(+49.30%)</b></td><td>199.20 (-3.30%)</td><td>176.72 (-4.79%)</td><td>173.40 (-6.72%)</td><td>154.10 (-10.72%)</td><td>16.69 <b>(+28.54%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>185.62 (n/a)</td><td>185.90 (n/a)</td><td>172.60 (n/a)</td><td>12.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+5.69%)</td><td>0.04 (+6.56%)</td><td>0.04 <b>(+20.37%)</b></td><td>0.02 <b>(-20.65%)</b></td><td>0.01 <b>(+59.70%)</b></td><td>265.50 <b>(+26.01%)</b></td><td>179.24 (-3.18%)</td><td>163.80 (-16.89%)</td><td>147.40 (-5.39%)</td><td>48.87 <b>(+99.88%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>185.12 (n/a)</td><td>197.10 (n/a)</td><td>155.80 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (-7.70%)</td><td>0.03 (-0.45%)</td><td>0.03 (+5.43%)</td><td>0.03 (-6.08%)</td><td>0.01 (+8.19%)</td><td>223.60 (+6.48%)</td><td>182.62 (+1.47%)</td><td>175.60 (-5.13%)</td><td>144.00 (+8.35%)</td><td>38.23 <b>(+29.90%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>179.98 (n/a)</td><td>185.10 (n/a)</td><td>132.90 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-3.80%)</td><td>0.04 (+6.96%)</td><td>0.04 (+11.19%)</td><td>0.03 <b>(+30.66%)</b></td><td>0.01 <b>(-29.79%)</b></td><td>204.30 <b>(-23.45%)</b></td><td>174.28 (-9.52%)</td><td>171.60 (-10.06%)</td><td>134.80 (+3.93%)</td><td>28.99 <b>(-42.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>266.90 (n/a)</td><td>192.62 (n/a)</td><td>190.80 (n/a)</td><td>129.70 (n/a)</td><td>50.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+12.24%)</td><td>0.04 (+4.17%)</td><td>0.04 (+0.04%)</td><td>0.03 (-2.41%)</td><td>0.00 <b>(+181.27%)</b></td><td>186.40 (+2.42%)</td><td>168.22 (-3.32%)</td><td>175.40 (-0.06%)</td><td>146.30 (-10.90%)</td><td>16.80 <b>(+155.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.00 (n/a)</td><td>174.00 (n/a)</td><td>175.50 (n/a)</td><td>164.20 (n/a)</td><td>6.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-7.58%)</td><td>0.03 (-5.47%)</td><td>0.03 (+0.59%)</td><td>0.02 (-16.00%)</td><td>0.00 (+6.19%)</td><td>248.30 (+19.09%)</td><td>208.74 (+6.20%)</td><td>204.20 (-0.58%)</td><td>176.40 (+8.15%)</td><td>26.70 <b>(+38.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.50 (n/a)</td><td>196.56 (n/a)</td><td>205.40 (n/a)</td><td>163.10 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-16.41%)</td><td>0.03 (-6.12%)</td><td>0.03 (+6.86%)</td><td>0.03 (-4.37%)</td><td>0.00 <b>(-51.21%)</b></td><td>228.10 (+4.59%)</td><td>198.22 (+4.88%)</td><td>192.30 (-6.42%)</td><td>181.80 (+19.61%)</td><td>18.74 <b>(-38.44%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>189.00 (n/a)</td><td>205.50 (n/a)</td><td>152.00 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (-6.39%)</td><td>0.08 (-5.75%)</td><td>0.07 (-12.43%)</td><td>0.06 (+1.38%)</td><td>0.01 <b>(-25.39%)</b></td><td>203.20 (-1.36%)</td><td>165.32 (+4.21%)</td><td>166.40 (+14.21%)</td><td>125.80 (+6.79%)</td><td>27.40 <b>(-24.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>206.00 (n/a)</td><td>158.64 (n/a)</td><td>145.70 (n/a)</td><td>117.80 (n/a)</td><td>36.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (-10.14%)</td><td>0.08 (-0.43%)</td><td>0.09 (+8.83%)</td><td>0.07 <b>(+23.31%)</b></td><td>0.01 <b>(-46.05%)</b></td><td>172.70 (-18.88%)</td><td>149.38 (-3.33%)</td><td>144.00 (-8.10%)</td><td>122.40 (+11.27%)</td><td>19.79 <b>(-50.55%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>212.90 (n/a)</td><td>154.52 (n/a)</td><td>156.70 (n/a)</td><td>110.00 (n/a)</td><td>40.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (-8.47%)</td><td>0.08 (+2.16%)</td><td>0.08 (+7.74%)</td><td>0.06 (+1.51%)</td><td>0.01 <b>(-25.89%)</b></td><td>196.50 (-1.50%)</td><td>162.16 (-3.06%)</td><td>161.70 (-7.18%)</td><td>140.40 (+9.26%)</td><td>22.41 <b>(-20.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>167.28 (n/a)</td><td>174.20 (n/a)</td><td>128.50 (n/a)</td><td>28.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-10.63%)</td><td>0.07 (-4.56%)</td><td>0.07 (-10.16%)</td><td>0.06 (+5.13%)</td><td>0.01 <b>(-42.65%)</b></td><td>213.20 (-4.86%)</td><td>185.14 (+2.96%)</td><td>188.70 (+11.33%)</td><td>164.40 (+11.91%)</td><td>20.20 <b>(-39.93%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>179.82 (n/a)</td><td>169.50 (n/a)</td><td>146.90 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (+5.87%)</td><td>0.07 (-14.51%)</td><td>0.06 (-17.26%)</td><td>0.04 <b>(-37.01%)</b></td><td>0.02 <b>(+66.20%)</b></td><td>337.70 <b>(+58.77%)</b></td><td>205.90 <b>(+25.72%)</b></td><td>193.20 <b>(+20.90%)</b></td><td>132.00 (-5.51%)</td><td>78.41 <b>(+162.73%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>163.78 (n/a)</td><td>159.80 (n/a)</td><td>139.70 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.08 <b>(-21.31%)</b></td><td>0.08 (-2.23%)</td><td>0.08 (+6.75%)</td><td>0.06 (+10.66%)</td><td>0.01 <b>(-44.46%)</b></td><td>217.70 (-9.63%)</td><td>166.20 (-1.31%)</td><td>154.50 (-6.31%)</td><td>145.90 <b>(+27.09%)</b></td><td>29.63 <b>(-35.85%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>240.90 (n/a)</td><td>168.40 (n/a)</td><td>164.90 (n/a)</td><td>114.80 (n/a)</td><td>46.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (-7.76%)</td><td>0.07 (-3.50%)</td><td>0.06 (-7.81%)</td><td>0.05 <b>(+28.39%)</b></td><td>0.02 <b>(-25.15%)</b></td><td>232.90 <b>(-22.11%)</b></td><td>191.08 (-1.38%)</td><td>202.80 (+8.45%)</td><td>125.10 (+8.41%)</td><td>41.71 <b>(-38.88%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>299.00 (n/a)</td><td>193.76 (n/a)</td><td>187.00 (n/a)</td><td>115.40 (n/a)</td><td>68.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 <b>(+22.76%)</b></td><td>0.07 (+3.30%)</td><td>0.07 (-6.65%)</td><td>0.06 (+8.61%)</td><td>0.01 <b>(+75.89%)</b></td><td>195.90 (-7.90%)</td><td>176.26 (-2.20%)</td><td>183.30 (+7.13%)</td><td>135.40 (-18.53%)</td><td>24.59 <b>(+29.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>180.22 (n/a)</td><td>171.10 (n/a)</td><td>166.20 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (+4.34%)</td><td>0.15 (+9.51%)</td><td>0.15 (+17.08%)</td><td>0.13 (+9.96%)</td><td>0.02 (-12.99%)</td><td>183.80 (-9.10%)</td><td>166.46 (-9.25%)</td><td>168.00 (-14.59%)</td><td>136.00 (-4.16%)</td><td>19.34 <b>(-24.48%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.20 (n/a)</td><td>183.42 (n/a)</td><td>196.70 (n/a)</td><td>141.90 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (-15.57%)</td><td>0.14 (+1.74%)</td><td>0.14 (+12.80%)</td><td>0.10 (-17.19%)</td><td>0.02 (-12.05%)</td><td>248.70 <b>(+20.73%)</b></td><td>182.06 (-1.37%)</td><td>170.10 (-11.36%)</td><td>159.90 (+18.44%)</td><td>37.66 <b>(+30.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>206.00 (n/a)</td><td>184.58 (n/a)</td><td>191.90 (n/a)</td><td>135.00 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 (-11.16%)</td><td>0.14 (-10.67%)</td><td>0.15 (-8.16%)</td><td>0.09 <b>(-26.32%)</b></td><td>0.04 (+18.70%)</td><td>285.80 <b>(+35.71%)</b></td><td>184.14 (+16.75%)</td><td>166.20 (+8.91%)</td><td>130.70 (+12.58%)</td><td>63.49 <b>(+78.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>210.60 (n/a)</td><td>157.72 (n/a)</td><td>152.60 (n/a)</td><td>116.10 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (-4.23%)</td><td>0.15 (-6.09%)</td><td>0.15 (-8.32%)</td><td>0.13 (-5.12%)</td><td>0.02 (+2.25%)</td><td>188.30 (+5.37%)</td><td>165.72 (+6.71%)</td><td>168.50 (+9.13%)</td><td>133.40 (+4.38%)</td><td>22.56 (+13.14%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>178.70 (n/a)</td><td>155.30 (n/a)</td><td>154.40 (n/a)</td><td>127.80 (n/a)</td><td>19.94 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (+3.10%)</td><td>0.14 (-5.23%)</td><td>0.13 <b>(-21.36%)</b></td><td>0.10 (+7.92%)</td><td>0.03 (-9.92%)</td><td>252.70 (-7.33%)</td><td>189.28 (+3.62%)</td><td>191.00 <b>(+27.16%)</b></td><td>133.30 (-2.98%)</td><td>45.88 (-19.41%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>272.70 (n/a)</td><td>182.66 (n/a)</td><td>150.20 (n/a)</td><td>137.40 (n/a)</td><td>56.94 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 <b>(-29.62%)</b></td><td>0.14 (-16.06%)</td><td>0.14 (-4.91%)</td><td>0.11 (-19.38%)</td><td>0.02 <b>(-52.03%)</b></td><td>214.60 <b>(+24.05%)</b></td><td>178.60 (+17.13%)</td><td>171.80 (+5.21%)</td><td>155.20 <b>(+42.12%)</b></td><td>22.84 (-14.02%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>173.00 (n/a)</td><td>152.48 (n/a)</td><td>163.30 (n/a)</td><td>109.20 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (-15.73%)</td><td>0.11 (-12.24%)</td><td>0.11 (-8.59%)</td><td>0.10 (-11.78%)</td><td>0.02 <b>(-22.83%)</b></td><td>257.30 (+13.35%)</td><td>219.64 (+13.20%)</td><td>226.30 (+9.43%)</td><td>171.30 (+18.63%)</td><td>38.37 (+3.33%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>227.00 (n/a)</td><td>194.02 (n/a)</td><td>206.80 (n/a)</td><td>144.40 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (+3.25%)</td><td>0.13 (+14.28%)</td><td>0.13 (+9.43%)</td><td>0.12 <b>(+71.63%)</b></td><td>0.02 <b>(-47.81%)</b></td><td>212.40 <b>(-41.73%)</b></td><td>186.48 (-18.40%)</td><td>187.40 (-8.63%)</td><td>151.20 (-3.14%)</td><td>22.42 <b>(-72.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>364.50 (n/a)</td><td>228.54 (n/a)</td><td>205.10 (n/a)</td><td>156.10 (n/a)</td><td>81.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.42 (+18.08%)</td><td>0.30 (-5.07%)</td><td>0.25 <b>(-20.23%)</b></td><td>0.22 (-9.54%)</td><td>0.09 <b>(+103.04%)</b></td><td>219.30 (+10.53%)</td><td>176.50 (+10.77%)</td><td>193.50 <b>(+25.32%)</b></td><td>117.50 (-15.35%)</td><td>48.31 <b>(+96.37%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>198.40 (n/a)</td><td>159.34 (n/a)</td><td>154.40 (n/a)</td><td>138.80 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.37 (+4.71%)</td><td>0.31 (+2.53%)</td><td>0.29 (-2.84%)</td><td>0.26 (+12.21%)</td><td>0.05 (-6.92%)</td><td>186.40 (-10.86%)</td><td>162.54 (-3.03%)</td><td>170.90 (+2.95%)</td><td>132.50 (-4.47%)</td><td>24.48 (-18.51%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>209.10 (n/a)</td><td>167.62 (n/a)</td><td>166.00 (n/a)</td><td>138.70 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.39 <b>(+22.79%)</b></td><td>0.29 (-3.56%)</td><td>0.29 (-8.78%)</td><td>0.20 <b>(-22.16%)</b></td><td>0.08 <b>(+175.94%)</b></td><td>249.60 <b>(+28.46%)</b></td><td>178.40 (+9.21%)</td><td>170.60 (+9.64%)</td><td>125.40 (-18.57%)</td><td>49.57 <b>(+185.70%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>163.36 (n/a)</td><td>155.60 (n/a)</td><td>154.00 (n/a)</td><td>17.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.38 <b>(+20.59%)</b></td><td>0.29 (-0.34%)</td><td>0.25 <b>(-20.26%)</b></td><td>0.22 (-14.05%)</td><td>0.08 <b>(+184.34%)</b></td><td>219.30 (+16.34%)</td><td>178.56 (+5.12%)</td><td>199.00 <b>(+25.39%)</b></td><td>129.70 (-17.07%)</td><td>43.90 <b>(+167.52%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>188.50 (n/a)</td><td>169.86 (n/a)</td><td>158.70 (n/a)</td><td>156.40 (n/a)</td><td>16.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.37 (-0.26%)</td><td>0.29 (-2.14%)</td><td>0.28 (-6.73%)</td><td>0.25 (+9.85%)</td><td>0.05 (-12.65%)</td><td>200.50 (-8.99%)</td><td>173.02 (+1.26%)</td><td>176.30 (+7.17%)</td><td>133.20 (+0.23%)</td><td>24.95 <b>(-23.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>220.30 (n/a)</td><td>170.86 (n/a)</td><td>164.50 (n/a)</td><td>132.90 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.36 (+16.41%)</td><td>0.28 (+13.09%)</td><td>0.29 (+9.54%)</td><td>0.18 <b>(+53.22%)</b></td><td>0.07 (-13.60%)</td><td>268.70 <b>(-34.72%)</b></td><td>186.94 (-17.52%)</td><td>168.30 (-8.68%)</td><td>135.20 (-14.05%)</td><td>50.77 <b>(-52.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>411.60 (n/a)</td><td>226.64 (n/a)</td><td>184.30 (n/a)</td><td>157.30 (n/a)</td><td>105.78 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 <b>(-36.19%)</b></td><td>0.25 (-14.77%)</td><td>0.24 (-10.90%)</td><td>0.22 <b>(+33.60%)</b></td><td>0.03 <b>(-70.07%)</b></td><td>227.70 <b>(-25.15%)</b></td><td>202.38 (+5.97%)</td><td>206.10 (+12.25%)</td><td>169.50 <b>(+56.65%)</b></td><td>26.04 <b>(-64.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>304.20 (n/a)</td><td>190.98 (n/a)</td><td>183.60 (n/a)</td><td>108.20 (n/a)</td><td>73.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.30 (-14.45%)</td><td>0.25 (+1.68%)</td><td>0.24 (+3.24%)</td><td>0.19 <b>(+22.37%)</b></td><td>0.04 <b>(-42.37%)</b></td><td>255.60 (-18.29%)</td><td>201.80 (-6.31%)</td><td>203.20 (-3.10%)</td><td>163.60 (+16.86%)</td><td>35.88 <b>(-45.18%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>312.80 (n/a)</td><td>215.40 (n/a)</td><td>209.70 (n/a)</td><td>140.00 (n/a)</td><td>65.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (-12.14%)</td><td>0.02 (-17.60%)</td><td>0.02 (-13.82%)</td><td>0.01 (-14.07%)</td><td>0.00 (-17.62%)</td><td>226.20 (+16.42%)</td><td>174.14 <b>(+20.83%)</b></td><td>172.30 (+16.03%)</td><td>125.70 (+13.76%)</td><td>35.92 (+8.98%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>144.12 (n/a)</td><td>148.50 (n/a)</td><td>110.50 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (-5.34%)</td><td>0.02 (-0.76%)</td><td>0.02 (+4.44%)</td><td>0.01 (-5.55%)</td><td>0.00 (-8.66%)</td><td>191.80 (+5.91%)</td><td>156.98 (+0.72%)</td><td>154.20 (-4.22%)</td><td>130.90 (+5.65%)</td><td>22.08 (+6.30%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>155.86 (n/a)</td><td>161.00 (n/a)</td><td>123.90 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (-12.22%)</td><td>0.02 (-0.80%)</td><td>0.02 (+6.49%)</td><td>0.02 (+17.04%)</td><td>0.00 <b>(-63.54%)</b></td><td>164.10 (-14.58%)</td><td>151.74 (-2.95%)</td><td>150.40 (-6.12%)</td><td>133.10 (+13.96%)</td><td>12.64 <b>(-64.49%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>156.36 (n/a)</td><td>160.20 (n/a)</td><td>116.80 (n/a)</td><td>35.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (-7.07%)</td><td>0.02 (+1.10%)</td><td>0.02 (-6.74%)</td><td>0.01 <b>(+47.20%)</b></td><td>0.00 <b>(-51.00%)</b></td><td>185.90 <b>(-32.08%)</b></td><td>167.16 (-5.75%)</td><td>168.70 (+7.25%)</td><td>146.30 (+7.65%)</td><td>18.55 <b>(-66.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>273.70 (n/a)</td><td>177.36 (n/a)</td><td>157.30 (n/a)</td><td>135.90 (n/a)</td><td>54.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (+3.01%)</td><td>0.02 (-0.06%)</td><td>0.02 (+1.67%)</td><td>0.01 (+1.02%)</td><td>0.00 (-17.50%)</td><td>238.60 (-1.00%)</td><td>171.00 (-2.36%)</td><td>165.00 (-1.61%)</td><td>119.20 (-2.93%)</td><td>43.65 (-18.11%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>241.00 (n/a)</td><td>175.14 (n/a)</td><td>167.70 (n/a)</td><td>122.80 (n/a)</td><td>53.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (+9.99%)</td><td>0.01 (+0.08%)</td><td>0.01 (-13.07%)</td><td>0.01 (-7.10%)</td><td>0.00 <b>(+46.70%)</b></td><td>241.70 (+7.66%)</td><td>190.58 (+2.40%)</td><td>206.10 (+15.01%)</td><td>131.40 (-9.07%)</td><td>44.26 <b>(+40.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>224.50 (n/a)</td><td>186.12 (n/a)</td><td>179.20 (n/a)</td><td>144.50 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (+12.77%)</td><td>0.01 (+1.73%)</td><td>0.01 (-14.52%)</td><td>0.01 (+14.24%)</td><td>0.00 <b>(+24.46%)</b></td><td>234.50 (-12.47%)</td><td>194.62 (-0.79%)</td><td>221.10 (+16.98%)</td><td>138.80 (-11.37%)</td><td>45.22 (-0.92%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>267.90 (n/a)</td><td>196.16 (n/a)</td><td>189.00 (n/a)</td><td>156.60 (n/a)</td><td>45.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.01 (-10.68%)</td><td>0.01 (-10.01%)</td><td>0.01 (-13.93%)</td><td>0.01 (-2.28%)</td><td>0.00 <b>(-42.23%)</b></td><td>246.10 (+2.33%)</td><td>216.58 (+9.20%)</td><td>221.30 (+16.17%)</td><td>179.90 (+11.95%)</td><td>24.03 <b>(-35.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>240.50 (n/a)</td><td>198.34 (n/a)</td><td>190.50 (n/a)</td><td>160.70 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (+10.23%)</td><td>0.03 (+3.96%)</td><td>0.03 (+3.53%)</td><td>0.03 (+1.17%)</td><td>0.01 <b>(+25.59%)</b></td><td>206.80 (-1.15%)</td><td>165.44 (-2.87%)</td><td>168.60 (-3.38%)</td><td>116.20 (-9.22%)</td><td>32.33 (+10.48%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>170.32 (n/a)</td><td>174.50 (n/a)</td><td>128.00 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (-12.00%)</td><td>0.03 (-16.27%)</td><td>0.03 (-14.49%)</td><td>0.02 <b>(-25.01%)</b></td><td>0.01 (+10.80%)</td><td>237.80 <b>(+33.37%)</b></td><td>195.82 <b>(+20.98%)</b></td><td>199.60 (+16.93%)</td><td>143.70 (+13.60%)</td><td>35.23 <b>(+66.33%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>178.30 (n/a)</td><td>161.86 (n/a)</td><td>170.70 (n/a)</td><td>126.50 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+16.42%)</td><td>0.03 (-1.95%)</td><td>0.03 (-3.97%)</td><td>0.03 (-10.20%)</td><td>0.01 <b>(+137.39%)</b></td><td>208.60 (+11.31%)</td><td>176.12 (+4.56%)</td><td>176.80 (+4.12%)</td><td>127.40 (-14.09%)</td><td>32.37 <b>(+127.17%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>168.44 (n/a)</td><td>169.80 (n/a)</td><td>148.30 (n/a)</td><td>14.25 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-15.22%)</td><td>0.03 (-16.42%)</td><td>0.03 (-17.05%)</td><td>0.02 (-15.36%)</td><td>0.00 (-15.71%)</td><td>237.90 (+18.12%)</td><td>209.32 (+19.60%)</td><td>208.60 <b>(+20.58%)</b></td><td>161.90 (+18.00%)</td><td>30.54 (+15.68%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.40 (n/a)</td><td>175.02 (n/a)</td><td>173.00 (n/a)</td><td>137.20 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (-3.49%)</td><td>0.03 (+4.28%)</td><td>0.03 (+1.82%)</td><td>0.02 (-0.56%)</td><td>0.01 (-9.40%)</td><td>218.90 (+0.55%)</td><td>168.44 (-4.43%)</td><td>170.00 (-1.79%)</td><td>131.60 (+3.62%)</td><td>32.43 (-1.86%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>176.24 (n/a)</td><td>173.10 (n/a)</td><td>127.00 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+7.81%)</td><td>0.03 (-1.31%)</td><td>0.03 (-3.28%)</td><td>0.02 (-17.15%)</td><td>0.01 <b>(+51.52%)</b></td><td>249.60 <b>(+20.70%)</b></td><td>178.64 (+5.05%)</td><td>186.60 (+3.38%)</td><td>125.50 (-7.24%)</td><td>49.35 <b>(+68.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>170.06 (n/a)</td><td>180.50 (n/a)</td><td>135.30 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 <b>(+34.68%)</b></td><td>0.03 (+10.61%)</td><td>0.03 (+5.25%)</td><td>0.02 (-5.59%)</td><td>0.01 <b>(+123.82%)</b></td><td>217.20 (+5.95%)</td><td>177.66 (-5.29%)</td><td>192.40 (-4.99%)</td><td>108.00 <b>(-25.77%)</b></td><td>43.72 <b>(+72.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>187.58 (n/a)</td><td>202.50 (n/a)</td><td>145.50 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-10.72%)</td><td>0.02 (-8.71%)</td><td>0.02 (-7.44%)</td><td>0.02 (-7.34%)</td><td>0.01 (-16.14%)</td><td>256.70 (+7.90%)</td><td>218.98 (+8.92%)</td><td>230.10 (+8.08%)</td><td>152.60 (+12.04%)</td><td>39.56 (+0.63%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.90 (n/a)</td><td>201.04 (n/a)</td><td>212.90 (n/a)</td><td>136.20 (n/a)</td><td>39.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 <b>(-22.68%)</b></td><td>0.06 (-8.70%)</td><td>0.06 (-5.47%)</td><td>0.05 <b>(+34.45%)</b></td><td>0.01 <b>(-70.76%)</b></td><td>198.30 <b>(-25.62%)</b></td><td>174.92 (+1.71%)</td><td>176.50 (+5.82%)</td><td>157.20 <b>(+29.38%)</b></td><td>16.75 <b>(-71.51%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>266.60 (n/a)</td><td>171.98 (n/a)</td><td>166.80 (n/a)</td><td>121.50 (n/a)</td><td>58.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 <b>(+26.97%)</b></td><td>0.07 <b>(+27.69%)</b></td><td>0.07 (+11.32%)</td><td>0.06 <b>(+36.81%)</b></td><td>0.02 (+15.31%)</td><td>172.70 <b>(-26.88%)</b></td><td>146.66 <b>(-22.48%)</b></td><td>157.70 (-10.14%)</td><td>108.60 <b>(-21.25%)</b></td><td>27.24 <b>(-35.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>189.20 (n/a)</td><td>175.50 (n/a)</td><td>137.90 (n/a)</td><td>42.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-9.64%)</td><td>0.06 (-12.05%)</td><td>0.06 (-16.59%)</td><td>0.04 <b>(-22.39%)</b></td><td>0.01 (-1.00%)</td><td>270.90 <b>(+28.88%)</b></td><td>192.64 (+15.00%)</td><td>180.70 (+19.91%)</td><td>156.50 (+10.68%)</td><td>45.87 <b>(+46.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>167.52 (n/a)</td><td>150.70 (n/a)</td><td>141.40 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 <b>(-25.19%)</b></td><td>0.05 (-10.31%)</td><td>0.05 (-3.61%)</td><td>0.05 (+4.20%)</td><td>0.01 <b>(-49.68%)</b></td><td>221.80 (-4.02%)</td><td>196.22 (+8.55%)</td><td>197.70 (+3.73%)</td><td>168.90 <b>(+33.73%)</b></td><td>25.73 <b>(-33.85%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>180.76 (n/a)</td><td>190.60 (n/a)</td><td>126.30 (n/a)</td><td>38.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-17.80%)</td><td>0.06 (-10.19%)</td><td>0.05 (-9.98%)</td><td>0.05 (-12.04%)</td><td>0.01 <b>(-21.93%)</b></td><td>202.80 (+13.68%)</td><td>181.24 (+11.11%)</td><td>191.70 (+11.07%)</td><td>158.20 <b>(+21.69%)</b></td><td>21.03 (+7.26%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>163.12 (n/a)</td><td>172.60 (n/a)</td><td>130.00 (n/a)</td><td>19.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 <b>(+22.81%)</b></td><td>0.06 (-0.61%)</td><td>0.05 (-5.78%)</td><td>0.05 (-11.26%)</td><td>0.02 <b>(+107.39%)</b></td><td>219.60 (+12.67%)</td><td>179.72 (+4.09%)</td><td>194.40 (+6.17%)</td><td>119.60 (-18.53%)</td><td>39.09 <b>(+87.29%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>172.66 (n/a)</td><td>183.10 (n/a)</td><td>146.80 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-19.81%)</td><td>0.05 (-16.56%)</td><td>0.05 (-16.75%)</td><td>0.04 (+1.00%)</td><td>0.01 <b>(-36.38%)</b></td><td>258.60 (-0.96%)</td><td>207.22 (+16.27%)</td><td>202.70 <b>(+20.08%)</b></td><td>153.30 <b>(+24.74%)</b></td><td>39.02 <b>(-24.23%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>261.10 (n/a)</td><td>178.22 (n/a)</td><td>168.80 (n/a)</td><td>122.90 (n/a)</td><td>51.49 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (+0.67%)</td><td>0.05 (+4.13%)</td><td>0.05 (+10.72%)</td><td>0.03 (-19.32%)</td><td>0.01 <b>(+59.99%)</b></td><td>343.70 <b>(+23.95%)</b></td><td>238.12 (-1.42%)</td><td>215.50 (-9.64%)</td><td>203.50 (-0.68%)</td><td>59.27 <b>(+102.17%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>277.30 (n/a)</td><td>241.54 (n/a)</td><td>238.50 (n/a)</td><td>204.90 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (+0.37%)</td><td>0.12 (+5.95%)</td><td>0.11 (+5.62%)</td><td>0.10 (+7.13%)</td><td>0.02 (-3.87%)</td><td>217.10 (-6.66%)</td><td>180.32 (-5.93%)</td><td>186.00 (-5.34%)</td><td>138.70 (-0.36%)</td><td>31.36 (-8.17%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>191.68 (n/a)</td><td>196.50 (n/a)</td><td>139.20 (n/a)</td><td>34.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 <b>(-31.71%)</b></td><td>0.11 (-13.74%)</td><td>0.10 <b>(-21.74%)</b></td><td>0.10 <b>(+50.43%)</b></td><td>0.01 <b>(-79.45%)</b></td><td>217.90 <b>(-33.53%)</b></td><td>198.96 (+3.90%)</td><td>201.30 <b>(+27.81%)</b></td><td>181.10 <b>(+46.40%)</b></td><td>15.57 <b>(-80.89%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>327.80 (n/a)</td><td>191.50 (n/a)</td><td>157.50 (n/a)</td><td>123.70 (n/a)</td><td>81.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 <b>(+26.08%)</b></td><td>0.14 <b>(+25.38%)</b></td><td>0.14 (+17.52%)</td><td>0.12 <b>(+55.80%)</b></td><td>0.01 <b>(-27.52%)</b></td><td>171.70 <b>(-35.81%)</b></td><td>151.86 <b>(-22.00%)</b></td><td>155.00 (-14.88%)</td><td>132.10 <b>(-20.66%)</b></td><td>15.21 <b>(-63.78%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>267.50 (n/a)</td><td>194.68 (n/a)</td><td>182.10 (n/a)</td><td>166.50 (n/a)</td><td>42.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (+14.03%)</td><td>0.13 (+5.34%)</td><td>0.13 (+7.83%)</td><td>0.10 (+5.19%)</td><td>0.03 <b>(+53.71%)</b></td><td>204.10 (-4.94%)</td><td>165.56 (-3.58%)</td><td>155.80 (-7.26%)</td><td>129.70 (-12.31%)</td><td>33.14 <b>(+28.51%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>171.70 (n/a)</td><td>168.00 (n/a)</td><td>147.90 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (-5.02%)</td><td>0.12 (+2.45%)</td><td>0.12 (+7.69%)</td><td>0.10 (+16.04%)</td><td>0.02 <b>(-31.96%)</b></td><td>218.30 (-13.82%)</td><td>182.64 (-4.21%)</td><td>177.80 (-7.15%)</td><td>156.40 (+5.25%)</td><td>24.50 <b>(-38.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>253.30 (n/a)</td><td>190.66 (n/a)</td><td>191.50 (n/a)</td><td>148.60 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (+8.97%)</td><td>0.13 (+14.63%)</td><td>0.12 <b>(+23.28%)</b></td><td>0.10 (+11.48%)</td><td>0.03 (+11.62%)</td><td>204.70 (-10.30%)</td><td>167.68 (-12.74%)</td><td>169.40 (-18.87%)</td><td>132.40 (-8.25%)</td><td>34.15 (-9.78%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>228.20 (n/a)</td><td>192.16 (n/a)</td><td>208.80 (n/a)</td><td>144.30 (n/a)</td><td>37.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (-15.78%)</td><td>0.12 (-4.61%)</td><td>0.13 (-1.83%)</td><td>0.09 (+8.10%)</td><td>0.02 <b>(-34.10%)</b></td><td>239.50 (-7.49%)</td><td>180.14 (+2.26%)</td><td>166.80 (+1.83%)</td><td>161.50 (+18.75%)</td><td>33.26 <b>(-30.29%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>258.90 (n/a)</td><td>176.16 (n/a)</td><td>163.80 (n/a)</td><td>136.00 (n/a)</td><td>47.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-6.73%)</td><td>0.09 (-2.98%)</td><td>0.09 (+4.86%)</td><td>0.07 (-15.03%)</td><td>0.02 (-2.60%)</td><td>305.10 (+17.71%)</td><td>233.42 (+3.58%)</td><td>222.90 (-4.66%)</td><td>184.10 (+7.22%)</td><td>44.20 <b>(+27.52%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>259.20 (n/a)</td><td>225.36 (n/a)</td><td>233.80 (n/a)</td><td>171.70 (n/a)</td><td>34.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>225.00 (n/a)</td><td>183.12 (n/a)</td><td>179.90 (n/a)</td><td>164.10 (n/a)</td><td>24.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>315.30 (n/a)</td><td>199.88 (n/a)</td><td>183.50 (n/a)</td><td>141.60 (n/a)</td><td>67.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>307.80 (n/a)</td><td>206.52 (n/a)</td><td>182.70 (n/a)</td><td>169.10 (n/a)</td><td>57.20 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.30 (n/a)</td><td>163.50 (n/a)</td><td>175.80 (n/a)</td><td>118.20 (n/a)</td><td>31.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>207.10 (n/a)</td><td>176.38 (n/a)</td><td>182.20 (n/a)</td><td>124.70 (n/a)</td><td>34.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>175.96 (n/a)</td><td>177.60 (n/a)</td><td>132.50 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>185.52 (n/a)</td><td>186.00 (n/a)</td><td>142.10 (n/a)</td><td>32.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>193.76 (n/a)</td><td>202.80 (n/a)</td><td>138.80 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>328.70 (n/a)</td><td>196.18 (n/a)</td><td>168.20 (n/a)</td><td>142.00 (n/a)</td><td>75.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>245.70 (n/a)</td><td>163.62 (n/a)</td><td>141.40 (n/a)</td><td>133.40 (n/a)</td><td>47.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>168.30 (n/a)</td><td>170.50 (n/a)</td><td>147.60 (n/a)</td><td>12.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>241.60 (n/a)</td><td>181.10 (n/a)</td><td>175.70 (n/a)</td><td>127.80 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.33 (-11.90%)</td><td>0.27 (-11.60%)</td><td>0.30 (+1.61%)</td><td>0.15 <b>(-44.99%)</b></td><td>0.07 <b>(+79.31%)</b></td><td>323.80 <b>(+81.81%)</b></td><td>195.78 <b>(+21.18%)</b></td><td>162.70 (-1.57%)</td><td>147.80 (+13.52%)</td><td>72.92 <b>(+297.37%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>178.10 (n/a)</td><td>161.56 (n/a)</td><td>165.30 (n/a)</td><td>130.20 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>195.40 (n/a)</td><td>157.12 (n/a)</td><td>163.70 (n/a)</td><td>125.80 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>192.10 (n/a)</td><td>165.60 (n/a)</td><td>167.40 (n/a)</td><td>133.20 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>216.60 (n/a)</td><td>179.18 (n/a)</td><td>163.20 (n/a)</td><td>147.20 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>173.20 (n/a)</td><td>149.68 (n/a)</td><td>162.70 (n/a)</td><td>118.40 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>141.22 (n/a)</td><td>130.10 (n/a)</td><td>111.90 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>138.04 (n/a)</td><td>125.80 (n/a)</td><td>124.90 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>164.46 (n/a)</td><td>162.60 (n/a)</td><td>118.30 (n/a)</td><td>35.49 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.40 (n/a)</td><td>142.02 (n/a)</td><td>133.30 (n/a)</td><td>119.10 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>132.32 (n/a)</td><td>120.90 (n/a)</td><td>115.50 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>162.00 (n/a)</td><td>146.70 (n/a)</td><td>157.10 (n/a)</td><td>125.50 (n/a)</td><td>17.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>163.50 (n/a)</td><td>144.30 (n/a)</td><td>153.90 (n/a)</td><td>108.20 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>150.00 (n/a)</td><td>132.52 (n/a)</td><td>133.10 (n/a)</td><td>117.90 (n/a)</td><td>14.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>164.80 (n/a)</td><td>153.32 (n/a)</td><td>153.70 (n/a)</td><td>143.60 (n/a)</td><td>8.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.10 (n/a)</td><td>146.30 (n/a)</td><td>134.80 (n/a)</td><td>119.10 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>197.50 (n/a)</td><td>166.88 (n/a)</td><td>165.00 (n/a)</td><td>139.50 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>196.60 (n/a)</td><td>150.70 (n/a)</td><td>144.20 (n/a)</td><td>125.70 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>180.50 (n/a)</td><td>141.38 (n/a)</td><td>130.80 (n/a)</td><td>127.50 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>321.30 (n/a)</td><td>174.84 (n/a)</td><td>140.80 (n/a)</td><td>106.60 (n/a)</td><td>85.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>163.08 (n/a)</td><td>169.40 (n/a)</td><td>124.00 (n/a)</td><td>33.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>159.18 (n/a)</td><td>153.40 (n/a)</td><td>113.40 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>187.20 (n/a)</td><td>159.90 (n/a)</td><td>166.70 (n/a)</td><td>114.90 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.80 (n/a)</td><td>198.44 (n/a)</td><td>194.20 (n/a)</td><td>160.60 (n/a)</td><td>37.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.40 (n/a)</td><td>162.26 (n/a)</td><td>164.20 (n/a)</td><td>138.90 (n/a)</td><td>22.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>179.30 (n/a)</td><td>191.90 (n/a)</td><td>133.00 (n/a)</td><td>37.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>286.00 (n/a)</td><td>191.42 (n/a)</td><td>204.50 (n/a)</td><td>108.20 (n/a)</td><td>70.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>195.66 (n/a)</td><td>201.20 (n/a)</td><td>147.90 (n/a)</td><td>37.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.90 (n/a)</td><td>183.20 (n/a)</td><td>179.70 (n/a)</td><td>162.20 (n/a)</td><td>18.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>186.10 (n/a)</td><td>166.10 (n/a)</td><td>156.60 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>186.68 (n/a)</td><td>189.70 (n/a)</td><td>140.60 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>172.76 (n/a)</td><td>163.70 (n/a)</td><td>144.80 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>177.14 (n/a)</td><td>169.10 (n/a)</td><td>155.10 (n/a)</td><td>21.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>269.90 (n/a)</td><td>209.42 (n/a)</td><td>209.90 (n/a)</td><td>135.90 (n/a)</td><td>48.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.20 (n/a)</td><td>190.00 (n/a)</td><td>198.70 (n/a)</td><td>130.30 (n/a)</td><td>46.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.50 (n/a)</td><td>212.28 (n/a)</td><td>214.10 (n/a)</td><td>179.10 (n/a)</td><td>22.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.10 (n/a)</td><td>180.90 (n/a)</td><td>167.90 (n/a)</td><td>140.60 (n/a)</td><td>37.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.20 (n/a)</td><td>159.64 (n/a)</td><td>156.90 (n/a)</td><td>127.30 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.60 (n/a)</td><td>177.58 (n/a)</td><td>171.20 (n/a)</td><td>143.10 (n/a)</td><td>35.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>170.12 (n/a)</td><td>181.30 (n/a)</td><td>116.60 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.90 (n/a)</td><td>165.02 (n/a)</td><td>165.90 (n/a)</td><td>124.70 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>277.70 (n/a)</td><td>191.46 (n/a)</td><td>182.80 (n/a)</td><td>147.00 (n/a)</td><td>52.58 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>188.14 (n/a)</td><td>190.30 (n/a)</td><td>147.80 (n/a)</td><td>25.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>318.80 (n/a)</td><td>234.92 (n/a)</td><td>236.50 (n/a)</td><td>173.40 (n/a)</td><td>54.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>183.10 (n/a)</td><td>168.16 (n/a)</td><td>173.60 (n/a)</td><td>139.60 (n/a)</td><td>16.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.70 (n/a)</td><td>183.06 (n/a)</td><td>176.90 (n/a)</td><td>155.90 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>244.20 (n/a)</td><td>186.66 (n/a)</td><td>175.50 (n/a)</td><td>161.30 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>213.90 (n/a)</td><td>168.48 (n/a)</td><td>170.00 (n/a)</td><td>104.00 (n/a)</td><td>40.96 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.70 (n/a)</td><td>164.82 (n/a)</td><td>165.90 (n/a)</td><td>133.70 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>198.40 (n/a)</td><td>169.40 (n/a)</td><td>165.40 (n/a)</td><td>131.40 (n/a)</td><td>26.94 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.20 (n/a)</td><td>179.18 (n/a)</td><td>182.50 (n/a)</td><td>141.60 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.00 (n/a)</td><td>235.90 (n/a)</td><td>226.52 (n/a)</td><td>223.70 (n/a)</td><td>218.70 (n/a)</td><td>6.96 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>4.23 (-3.74%)</td><td>4.10 (-2.15%)</td><td>4.11 (-1.64%)</td><td>3.91 (+0.09%)</td><td>0.13 <b>(-33.22%)</b></td><td>2403.10 (-0.08%)</td><td>2293.58 (+2.10%)</td><td>2286.70 (+1.67%)</td><td>2221.10 (+3.88%)</td><td>75.58 <b>(-30.56%)</b></td><td>1665.53 (-3.74%)</td><td>1614.30 (-2.15%)</td><td>1617.76 (-1.64%)</td><td>1539.43 (+0.09%)</td><td>52.54 <b>(-33.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>4.40 (n/a)</td><td>4.19 (n/a)</td><td>4.18 (n/a)</td><td>3.91 (n/a)</td><td>0.20 (n/a)</td><td>2405.10 (n/a)</td><td>2246.40 (n/a)</td><td>2249.20 (n/a)</td><td>2138.20 (n/a)</td><td>108.85 (n/a)</td><td>1730.16 (n/a)</td><td>1649.85 (n/a)</td><td>1644.75 (n/a)</td><td>1538.12 (n/a)</td><td>78.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.96 (-11.34%)</td><td>0.77 (-10.13%)</td><td>0.67 <b>(-23.68%)</b></td><td>0.64 (-1.45%)</td><td>0.15 <b>(-25.72%)</b></td><td>347.60 (+1.46%)</td><td>294.92 (+9.18%)</td><td>328.00 <b>(+31.04%)</b></td><td>231.20 (+12.78%)</td><td>55.12 (-18.34%)</td><td>40.82 (-11.34%)</td><td>32.98 (-10.13%)</td><td>28.77 <b>(-23.68%)</b></td><td>27.15 (-1.45%)</td><td>6.58 <b>(-25.72%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.08 (n/a)</td><td>0.86 (n/a)</td><td>0.88 (n/a)</td><td>0.65 (n/a)</td><td>0.21 (n/a)</td><td>342.60 (n/a)</td><td>270.12 (n/a)</td><td>250.30 (n/a)</td><td>205.00 (n/a)</td><td>67.49 (n/a)</td><td>46.04 (n/a)</td><td>36.70 (n/a)</td><td>37.70 (n/a)</td><td>27.55 (n/a)</td><td>8.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.20 (+0.11%)</td><td>0.98 (-5.13%)</td><td>0.95 (-19.69%)</td><td>0.83 <b>(+30.60%)</b></td><td>0.13 <b>(-44.68%)</b></td><td>265.20 <b>(-23.44%)</b></td><td>228.06 (+0.77%)</td><td>232.60 <b>(+24.52%)</b></td><td>184.10 (-0.11%)</td><td>29.07 <b>(-58.31%)</b></td><td>51.28 (+0.11%)</td><td>41.96 (-5.13%)</td><td>40.58 (-19.69%)</td><td>35.58 <b>(+30.60%)</b></td><td>5.74 <b>(-44.68%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.20 (n/a)</td><td>1.04 (n/a)</td><td>1.18 (n/a)</td><td>0.64 (n/a)</td><td>0.24 (n/a)</td><td>346.40 (n/a)</td><td>226.32 (n/a)</td><td>186.80 (n/a)</td><td>184.30 (n/a)</td><td>69.72 (n/a)</td><td>51.22 (n/a)</td><td>44.24 (n/a)</td><td>50.53 (n/a)</td><td>27.25 (n/a)</td><td>10.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.52 (+1.02%)</td><td>0.52 (+0.51%)</td><td>0.52 (+0.50%)</td><td>0.52 (+0.32%)</td><td>0.00 <b>(+176.53%)</b></td><td>48621.90 (-0.32%)</td><td>48434.50 (-0.50%)</td><td>48429.30 (-0.50%)</td><td>48098.00 (-1.01%)</td><td>210.06 <b>(+172.84%)</b></td><td>357.18 (+1.02%)</td><td>354.71 (+0.51%)</td><td>354.74 (+0.50%)</td><td>353.34 (+0.32%)</td><td>1.54 <b>(+176.53%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48777.20 (n/a)</td><td>48679.30 (n/a)</td><td>48673.80 (n/a)</td><td>48590.90 (n/a)</td><td>76.99 (n/a)</td><td>353.56 (n/a)</td><td>352.92 (n/a)</td><td>352.96 (n/a)</td><td>352.21 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (+2.13%)</td><td>0.21 (+1.23%)</td><td>0.21 (+1.74%)</td><td>0.21 (+0.49%)</td><td>0.00 <b>(+71.80%)</b></td><td>119234.00 (-0.49%)</td><td>117381.82 (-1.20%)</td><td>117175.70 (-1.71%)</td><td>114861.50 (-2.08%)</td><td>1851.48 <b>(+67.76%)</b></td><td>149.57 (+2.13%)</td><td>146.39 (+1.23%)</td><td>146.62 (+1.74%)</td><td>144.09 (+0.49%)</td><td>2.32 <b>(+71.80%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119817.20 (n/a)</td><td>118806.74 (n/a)</td><td>119218.40 (n/a)</td><td>117305.40 (n/a)</td><td>1103.65 (n/a)</td><td>146.45 (n/a)</td><td>144.61 (n/a)</td><td>144.10 (n/a)</td><td>143.38 (n/a)</td><td>1.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.89 (-2.70%)</td><td>0.88 (-1.14%)</td><td>0.88 (-0.46%)</td><td>0.88 (-0.82%)</td><td>0.01 <b>(-58.58%)</b></td><td>28671.60 (+0.82%)</td><td>28481.16 (+1.14%)</td><td>28499.80 (+0.46%)</td><td>28201.10 (+2.78%)</td><td>180.30 <b>(-57.07%)</b></td><td>609.19 (-2.70%)</td><td>603.22 (-1.14%)</td><td>602.81 (-0.46%)</td><td>599.19 (-0.82%)</td><td>3.83 <b>(-58.58%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.92 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28437.00 (n/a)</td><td>28160.18 (n/a)</td><td>28369.60 (n/a)</td><td>27438.60 (n/a)</td><td>419.95 (n/a)</td><td>626.12 (n/a)</td><td>610.19 (n/a)</td><td>605.57 (n/a)</td><td>604.14 (n/a)</td><td>9.25 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.60 (+2.27%)</td><td>3.52 (+1.97%)</td><td>3.55 (+1.07%)</td><td>3.33 (-0.14%)</td><td>0.11 (+11.65%)</td><td>7553.60 (+0.14%)</td><td>7163.10 (-1.92%)</td><td>7081.90 (-1.06%)</td><td>6993.80 (-2.22%)</td><td>223.91 (+10.16%)</td><td>2456.43 (+2.27%)</td><td>2400.20 (+1.97%)</td><td>2425.89 (+1.07%)</td><td>2274.40 (-0.14%)</td><td>72.38 (+11.65%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.52 (n/a)</td><td>3.45 (n/a)</td><td>3.52 (n/a)</td><td>3.34 (n/a)</td><td>0.09 (n/a)</td><td>7542.70 (n/a)</td><td>7303.44 (n/a)</td><td>7157.50 (n/a)</td><td>7152.70 (n/a)</td><td>203.26 (n/a)</td><td>2401.89 (n/a)</td><td>2353.75 (n/a)</td><td>2400.26 (n/a)</td><td>2277.69 (n/a)</td><td>64.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.08 (+7.02%)</td><td>2.85 (+2.39%)</td><td>2.84 (+1.18%)</td><td>2.74 (+2.42%)</td><td>0.14 <b>(+75.86%)</b></td><td>9175.70 (-2.36%)</td><td>8836.44 (-2.23%)</td><td>8852.80 (-1.17%)</td><td>8171.00 (-6.56%)</td><td>405.74 <b>(+59.82%)</b></td><td>2102.54 (+7.02%)</td><td>1947.63 (+2.39%)</td><td>1940.61 (+1.18%)</td><td>1872.32 (+2.42%)</td><td>93.16 <b>(+75.86%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>2.88 (n/a)</td><td>2.79 (n/a)</td><td>2.81 (n/a)</td><td>2.68 (n/a)</td><td>0.08 (n/a)</td><td>9397.60 (n/a)</td><td>9037.78 (n/a)</td><td>8957.60 (n/a)</td><td>8744.50 (n/a)</td><td>253.88 (n/a)</td><td>1964.65 (n/a)</td><td>1902.09 (n/a)</td><td>1917.91 (n/a)</td><td>1828.11 (n/a)</td><td>52.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.21 (-3.49%)</td><td>3.17 (-0.82%)</td><td>3.16 (-0.58%)</td><td>3.15 (+4.47%)</td><td>0.03 <b>(-80.35%)</b></td><td>7999.50 (-4.28%)</td><td>7949.84 (+0.70%)</td><td>7964.10 (+0.59%)</td><td>7844.80 (+3.61%)</td><td>62.97 <b>(-80.44%)</b></td><td>2189.97 (-3.49%)</td><td>2161.15 (-0.82%)</td><td>2157.17 (-0.58%)</td><td>2147.63 (+4.47%)</td><td>17.24 <b>(-80.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.32 (n/a)</td><td>3.19 (n/a)</td><td>3.18 (n/a)</td><td>3.01 (n/a)</td><td>0.13 (n/a)</td><td>8357.20 (n/a)</td><td>7894.52 (n/a)</td><td>7917.70 (n/a)</td><td>7571.40 (n/a)</td><td>321.84 (n/a)</td><td>2269.06 (n/a)</td><td>2179.04 (n/a)</td><td>2169.81 (n/a)</td><td>2055.69 (n/a)</td><td>87.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.79 (+0.34%)</td><td>0.79 (+0.34%)</td><td>0.79 (+0.38%)</td><td>0.78 (+0.30%)</td><td>0.00 <b>(+54.86%)</b></td><td>96221.30 (-0.30%)</td><td>96148.08 (-0.34%)</td><td>96112.00 (-0.38%)</td><td>96087.70 (-0.34%)</td><td>63.43 <b>(+53.87%)</b></td><td>715.17 (+0.34%)</td><td>714.73 (+0.34%)</td><td>714.99 (+0.38%)</td><td>714.18 (+0.30%)</td><td>0.47 <b>(+54.85%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96514.30 (n/a)</td><td>96472.96 (n/a)</td><td>96473.80 (n/a)</td><td>96417.10 (n/a)</td><td>41.22 (n/a)</td><td>712.73 (n/a)</td><td>712.32 (n/a)</td><td>712.31 (n/a)</td><td>712.01 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.73 (+0.32%)</td><td>0.73 (+0.31%)</td><td>0.73 (+0.32%)</td><td>0.73 (+0.32%)</td><td>0.00 (+2.84%)</td><td>103531.80 (-0.32%)</td><td>103369.64 (-0.31%)</td><td>103316.50 (-0.32%)</td><td>103266.20 (-0.32%)</td><td>106.29 (+2.15%)</td><td>665.46 (+0.32%)</td><td>664.79 (+0.31%)</td><td>665.14 (+0.32%)</td><td>663.75 (+0.32%)</td><td>0.68 (+2.83%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103859.20 (n/a)</td><td>103694.06 (n/a)</td><td>103651.30 (n/a)</td><td>103598.40 (n/a)</td><td>104.06 (n/a)</td><td>663.33 (n/a)</td><td>662.71 (n/a)</td><td>662.99 (n/a)</td><td>661.66 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.70 (+0.71%)</td><td>0.70 (+0.36%)</td><td>0.70 (+0.14%)</td><td>0.69 (+0.43%)</td><td>0.00 <b>(+23.10%)</b></td><td>108765.70 (-0.43%)</td><td>108355.58 (-0.35%)</td><td>108498.20 (-0.13%)</td><td>107658.40 (-0.70%)</td><td>417.54 <b>(+21.64%)</b></td><td>638.31 (+0.71%)</td><td>634.21 (+0.36%)</td><td>633.37 (+0.14%)</td><td>631.81 (+0.43%)</td><td>2.45 <b>(+23.10%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109231.30 (n/a)</td><td>108740.02 (n/a)</td><td>108644.80 (n/a)</td><td>108420.10 (n/a)</td><td>343.26 (n/a)</td><td>633.83 (n/a)</td><td>631.97 (n/a)</td><td>632.52 (n/a)</td><td>629.12 (n/a)</td><td>1.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.60 (+2.00%)</td><td>6.71 (+3.17%)</td><td>6.95 (-2.21%)</td><td>4.91 (-3.11%)</td><td>1.06 (-4.34%)</td><td>1814.70 (+3.21%)</td><td>1360.14 (-3.17%)</td><td>1281.80 (+2.27%)</td><td>1172.60 (-1.96%)</td><td>260.57 (+0.80%)</td><td>457.86 (+2.00%)</td><td>404.48 (+3.17%)</td><td>418.86 (-2.21%)</td><td>295.84 (-3.11%)</td><td>63.94 (-4.34%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.45 (n/a)</td><td>6.51 (n/a)</td><td>7.11 (n/a)</td><td>5.07 (n/a)</td><td>1.11 (n/a)</td><td>1758.30 (n/a)</td><td>1404.62 (n/a)</td><td>1253.40 (n/a)</td><td>1196.10 (n/a)</td><td>258.51 (n/a)</td><td>448.87 (n/a)</td><td>392.04 (n/a)</td><td>428.32 (n/a)</td><td>305.34 (n/a)</td><td>66.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.94 (-0.43%)</td><td>6.72 (+0.07%)</td><td>6.82 (+1.90%)</td><td>6.41 (+0.37%)</td><td>0.24 (+9.85%)</td><td>1390.20 (-0.37%)</td><td>1327.44 (-0.05%)</td><td>1306.80 (-1.87%)</td><td>1284.00 (+0.44%)</td><td>48.12 (+9.51%)</td><td>418.14 (-0.43%)</td><td>404.86 (+0.07%)</td><td>410.82 (+1.90%)</td><td>386.17 (+0.37%)</td><td>14.50 (+9.85%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>6.97 (n/a)</td><td>6.72 (n/a)</td><td>6.69 (n/a)</td><td>6.39 (n/a)</td><td>0.22 (n/a)</td><td>1395.30 (n/a)</td><td>1328.12 (n/a)</td><td>1331.70 (n/a)</td><td>1278.40 (n/a)</td><td>43.95 (n/a)</td><td>419.97 (n/a)</td><td>404.59 (n/a)</td><td>403.16 (n/a)</td><td>384.76 (n/a)</td><td>13.20 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.24 (+2.17%)</td><td>6.90 (+5.02%)</td><td>6.91 (+4.70%)</td><td>6.65 (+8.90%)</td><td>0.25 <b>(-43.11%)</b></td><td>1340.40 (-8.17%)</td><td>1293.98 (-5.03%)</td><td>1290.30 (-4.49%)</td><td>1230.40 (-2.12%)</td><td>47.15 <b>(-49.01%)</b></td><td>436.33 (+2.17%)</td><td>415.34 (+5.02%)</td><td>416.07 (+4.70%)</td><td>400.52 (+8.90%)</td><td>15.25 <b>(-43.11%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.09 (n/a)</td><td>6.57 (n/a)</td><td>6.60 (n/a)</td><td>6.11 (n/a)</td><td>0.44 (n/a)</td><td>1459.70 (n/a)</td><td>1362.48 (n/a)</td><td>1351.00 (n/a)</td><td>1257.10 (n/a)</td><td>92.46 (n/a)</td><td>427.08 (n/a)</td><td>395.50 (n/a)</td><td>397.37 (n/a)</td><td>367.80 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.06 (+0.59%)</td><td>7.54 (-0.15%)</td><td>7.62 (+2.54%)</td><td>7.10 (-0.90%)</td><td>0.38 (-1.75%)</td><td>4911.40 (+0.91%)</td><td>4633.42 (+0.15%)</td><td>4576.60 (-2.48%)</td><td>4327.20 (-0.59%)</td><td>233.10 (-0.81%)</td><td>496.28 (+0.59%)</td><td>464.42 (-0.15%)</td><td>469.23 (+2.54%)</td><td>437.24 (-0.90%)</td><td>23.47 (-1.75%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.01 (n/a)</td><td>7.55 (n/a)</td><td>7.43 (n/a)</td><td>7.16 (n/a)</td><td>0.39 (n/a)</td><td>4867.30 (n/a)</td><td>4626.64 (n/a)</td><td>4692.90 (n/a)</td><td>4352.70 (n/a)</td><td>235.01 (n/a)</td><td>493.37 (n/a)</td><td>465.13 (n/a)</td><td>457.60 (n/a)</td><td>441.21 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.87 (+3.78%)</td><td>7.44 (+2.26%)</td><td>7.60 (+2.35%)</td><td>6.89 (+1.84%)</td><td>0.39 (+6.18%)</td><td>5061.30 (-1.81%)</td><td>4696.92 (-2.19%)</td><td>4585.70 (-2.30%)</td><td>4428.20 (-3.64%)</td><td>250.87 (+1.31%)</td><td>484.95 (+3.78%)</td><td>458.23 (+2.26%)</td><td>468.30 (+2.35%)</td><td>424.30 (+1.84%)</td><td>23.95 (+6.18%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.59 (n/a)</td><td>7.28 (n/a)</td><td>7.43 (n/a)</td><td>6.76 (n/a)</td><td>0.37 (n/a)</td><td>5154.60 (n/a)</td><td>4802.32 (n/a)</td><td>4693.50 (n/a)</td><td>4595.40 (n/a)</td><td>247.63 (n/a)</td><td>467.31 (n/a)</td><td>448.11 (n/a)</td><td>457.55 (n/a)</td><td>416.62 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.84 (+3.21%)</td><td>7.10 (+0.30%)</td><td>6.96 (-2.25%)</td><td>6.59 (-2.15%)</td><td>0.47 <b>(+32.89%)</b></td><td>5290.50 (+2.20%)</td><td>4929.94 (-0.16%)</td><td>5006.10 (+2.31%)</td><td>4448.60 (-3.11%)</td><td>317.74 <b>(+29.59%)</b></td><td>482.73 (+3.21%)</td><td>437.10 (+0.30%)</td><td>428.98 (-2.25%)</td><td>405.91 (-2.15%)</td><td>29.21 <b>(+32.89%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.59 (n/a)</td><td>7.08 (n/a)</td><td>7.13 (n/a)</td><td>6.73 (n/a)</td><td>0.36 (n/a)</td><td>5176.80 (n/a)</td><td>4937.62 (n/a)</td><td>4893.30 (n/a)</td><td>4591.20 (n/a)</td><td>245.19 (n/a)</td><td>467.73 (n/a)</td><td>435.80 (n/a)</td><td>438.87 (n/a)</td><td>414.83 (n/a)</td><td>21.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.79 (+0.24%)</td><td>0.79 (+0.33%)</td><td>0.79 (+0.37%)</td><td>0.79 (+0.30%)</td><td>0.00 (-13.19%)</td><td>95595.20 (-0.30%)</td><td>95443.20 (-0.33%)</td><td>95416.10 (-0.37%)</td><td>95371.20 (-0.24%)</td><td>88.17 (-13.64%)</td><td>720.55 (+0.24%)</td><td>720.00 (+0.33%)</td><td>720.21 (+0.37%)</td><td>718.86 (+0.30%)</td><td>0.66 (-13.20%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95878.20 (n/a)</td><td>95755.36 (n/a)</td><td>95769.20 (n/a)</td><td>95599.20 (n/a)</td><td>102.09 (n/a)</td><td>718.83 (n/a)</td><td>717.66 (n/a)</td><td>717.55 (n/a)</td><td>716.74 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.74 (+0.69%)</td><td>0.74 (+0.42%)</td><td>0.74 (+0.35%)</td><td>0.74 (+0.34%)</td><td>0.00 <b>(+1215.89%)</b></td><td>102584.80 (-0.34%)</td><td>102491.22 (-0.42%)</td><td>102557.00 (-0.35%)</td><td>102198.90 (-0.69%)</td><td>163.90 <b>(+1204.31%)</b></td><td>672.41 (+0.69%)</td><td>670.49 (+0.42%)</td><td>670.06 (+0.35%)</td><td>669.88 (+0.34%)</td><td>1.07 <b>(+1215.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102934.00 (n/a)</td><td>102919.40 (n/a)</td><td>102913.20 (n/a)</td><td>102908.30 (n/a)</td><td>12.57 (n/a)</td><td>667.77 (n/a)</td><td>667.70 (n/a)</td><td>667.74 (n/a)</td><td>667.61 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.70 (+0.25%)</td><td>0.70 (+0.36%)</td><td>0.70 (+0.43%)</td><td>0.70 (+0.56%)</td><td>0.00 <b>(-50.62%)</b></td><td>107627.70 (-0.55%)</td><td>107485.62 (-0.36%)</td><td>107431.90 (-0.43%)</td><td>107364.80 (-0.25%)</td><td>112.75 <b>(-51.00%)</b></td><td>640.06 (+0.25%)</td><td>639.34 (+0.36%)</td><td>639.66 (+0.43%)</td><td>638.49 (+0.56%)</td><td>0.67 <b>(-50.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108227.80 (n/a)</td><td>107871.82 (n/a)</td><td>107890.80 (n/a)</td><td>107630.80 (n/a)</td><td>230.13 (n/a)</td><td>638.47 (n/a)</td><td>637.05 (n/a)</td><td>636.94 (n/a)</td><td>634.95 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>4.11 (+10.47%)</td><td>3.58 (+1.53%)</td><td>3.63 (-1.01%)</td><td>2.88 (-2.35%)</td><td>0.48 <b>(+45.43%)</b></td><td>2799.70 (+2.40%)</td><td>2285.12 (-0.78%)</td><td>2222.60 (+1.02%)</td><td>1960.70 (-9.48%)</td><td>327.41 <b>(+34.78%)</b></td><td>1078.14 (+10.47%)</td><td>939.34 (+1.53%)</td><td>951.11 (-1.01%)</td><td>755.07 (-2.35%)</td><td>125.08 <b>(+45.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.72 (n/a)</td><td>3.53 (n/a)</td><td>3.66 (n/a)</td><td>2.95 (n/a)</td><td>0.33 (n/a)</td><td>2734.00 (n/a)</td><td>2302.98 (n/a)</td><td>2200.20 (n/a)</td><td>2166.10 (n/a)</td><td>242.93 (n/a)</td><td>975.92 (n/a)</td><td>925.17 (n/a)</td><td>960.78 (n/a)</td><td>773.20 (n/a)</td><td>86.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.52 (+2.52%)</td><td>0.47 <b>(+37.29%)</b></td><td>0.50 <b>(+59.86%)</b></td><td>0.33 (+19.22%)</td><td>0.08 (-14.96%)</td><td>3822.60 (-16.12%)</td><td>2743.56 <b>(-28.42%)</b></td><td>2492.40 <b>(-37.44%)</b></td><td>2393.50 (-2.46%)</td><td>607.56 <b>(-25.99%)</b></td><td>28.04 (+2.52%)</td><td>25.23 <b>(+37.29%)</b></td><td>26.93 <b>(+59.86%)</b></td><td>17.56 (+19.22%)</td><td>4.36 (-14.96%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.51 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>4557.20 (n/a)</td><td>3832.96 (n/a)</td><td>3984.30 (n/a)</td><td>2453.80 (n/a)</td><td>820.96 (n/a)</td><td>27.35 (n/a)</td><td>18.38 (n/a)</td><td>16.84 (n/a)</td><td>14.73 (n/a)</td><td>5.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.99 <b>(+38.52%)</b></td><td>5.26 <b>(+32.17%)</b></td><td>4.85 <b>(+23.11%)</b></td><td>4.70 <b>(+42.59%)</b></td><td>0.97 <b>(+44.24%)</b></td><td>1414.40 <b>(-29.87%)</b></td><td>1292.14 <b>(-24.26%)</b></td><td>1371.70 (-18.78%)</td><td>951.70 <b>(-27.81%)</b></td><td>192.49 <b>(-27.75%)</b></td><td>2159.44 <b>(+38.52%)</b></td><td>1626.20 <b>(+32.17%)</b></td><td>1498.26 <b>(+23.11%)</b></td><td>1453.04 <b>(+42.59%)</b></td><td>299.74 <b>(+44.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.05 (n/a)</td><td>3.98 (n/a)</td><td>3.94 (n/a)</td><td>3.30 (n/a)</td><td>0.67 (n/a)</td><td>2016.90 (n/a)</td><td>1706.06 (n/a)</td><td>1688.80 (n/a)</td><td>1318.40 (n/a)</td><td>266.40 (n/a)</td><td>1558.89 (n/a)</td><td>1230.39 (n/a)</td><td>1216.99 (n/a)</td><td>1019.02 (n/a)</td><td>207.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.49 (n/a)</td><td>12.99 (n/a)</td><td>13.09 (n/a)</td><td>11.93 (n/a)</td><td>0.64 (n/a)</td><td>13.49 (n/a)</td><td>12.98 (n/a)</td><td>13.08 (n/a)</td><td>11.93 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>24.99 (+0.77%)</td><td>24.39 (+1.07%)</td><td>24.35 (+0.70%)</td><td>23.44 (+0.01%)</td><td>0.65 <b>(+28.92%)</b></td><td>24.97 (+0.77%)</td><td>24.37 (+1.07%)</td><td>24.34 (+0.70%)</td><td>23.43 (+0.01%)</td><td>0.64 <b>(+28.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>24.80 (n/a)</td><td>24.13 (n/a)</td><td>24.18 (n/a)</td><td>23.44 (n/a)</td><td>0.50 (n/a)</td><td>24.78 (n/a)</td><td>24.11 (n/a)</td><td>24.17 (n/a)</td><td>23.42 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>43.60 (+5.69%)</td><td>41.06 (+4.18%)</td><td>40.43 (+2.72%)</td><td>39.14 (+2.91%)</td><td>1.85 <b>(+58.43%)</b></td><td>43.57 (+5.69%)</td><td>41.04 (+4.18%)</td><td>40.41 (+2.72%)</td><td>39.12 (+2.91%)</td><td>1.85 <b>(+58.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>41.26 (n/a)</td><td>39.42 (n/a)</td><td>39.36 (n/a)</td><td>38.03 (n/a)</td><td>1.17 (n/a)</td><td>41.23 (n/a)</td><td>39.39 (n/a)</td><td>39.34 (n/a)</td><td>38.01 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>45.53 (+1.04%)</td><td>41.86 (-3.37%)</td><td>41.37 (-4.82%)</td><td>39.59 (-5.94%)</td><td>2.24 <b>(+87.95%)</b></td><td>45.50 (+1.04%)</td><td>41.84 (-3.37%)</td><td>41.35 (-4.82%)</td><td>39.57 (-5.94%)</td><td>2.23 <b>(+87.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>45.06 (n/a)</td><td>43.32 (n/a)</td><td>43.47 (n/a)</td><td>42.09 (n/a)</td><td>1.19 (n/a)</td><td>45.04 (n/a)</td><td>43.29 (n/a)</td><td>43.45 (n/a)</td><td>42.07 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.34 (n/a)</td><td>12.73 (n/a)</td><td>13.11 (n/a)</td><td>10.99 (n/a)</td><td>0.98 (n/a)</td><td>13.33 (n/a)</td><td>12.72 (n/a)</td><td>13.11 (n/a)</td><td>10.98 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>24.80 (+1.60%)</td><td>23.79 (-0.88%)</td><td>23.62 (-1.16%)</td><td>23.01 (-3.49%)</td><td>0.71 <b>(+204.81%)</b></td><td>24.79 (+1.60%)</td><td>23.77 (-0.88%)</td><td>23.61 (-1.16%)</td><td>22.99 (-3.49%)</td><td>0.71 <b>(+204.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>24.41 (n/a)</td><td>24.00 (n/a)</td><td>23.90 (n/a)</td><td>23.84 (n/a)</td><td>0.23 (n/a)</td><td>24.40 (n/a)</td><td>23.99 (n/a)</td><td>23.88 (n/a)</td><td>23.83 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>41.94 (+1.82%)</td><td>40.31 (+9.89%)</td><td>39.82 (+1.70%)</td><td>39.05 <b>(+59.68%)</b></td><td>1.19 <b>(-82.79%)</b></td><td>41.91 (+1.82%)</td><td>40.29 (+9.89%)</td><td>39.80 (+1.70%)</td><td>39.03 <b>(+59.68%)</b></td><td>1.19 <b>(-82.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>41.19 (n/a)</td><td>36.69 (n/a)</td><td>39.16 (n/a)</td><td>24.46 (n/a)</td><td>6.89 (n/a)</td><td>41.16 (n/a)</td><td>36.66 (n/a)</td><td>39.14 (n/a)</td><td>24.44 (n/a)</td><td>6.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>45.93 (+6.83%)</td><td>43.79 (+2.71%)</td><td>43.49 (+2.20%)</td><td>41.97 (-1.09%)</td><td>1.57 <b>(+560.82%)</b></td><td>45.90 (+6.83%)</td><td>43.77 (+2.71%)</td><td>43.46 (+2.20%)</td><td>41.94 (-1.09%)</td><td>1.57 <b>(+560.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>42.99 (n/a)</td><td>42.64 (n/a)</td><td>42.55 (n/a)</td><td>42.43 (n/a)</td><td>0.24 (n/a)</td><td>42.97 (n/a)</td><td>42.61 (n/a)</td><td>42.52 (n/a)</td><td>42.41 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>10.06 (+10.21%)</td><td>8.71 (+0.27%)</td><td>8.40 (-2.71%)</td><td>7.79 (-7.40%)</td><td>0.89 <b>(+231.72%)</b></td><td>10.04 (+10.21%)</td><td>8.69 (+0.27%)</td><td>8.38 (-2.71%)</td><td>7.78 (-7.40%)</td><td>0.89 <b>(+231.72%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>9.13 (n/a)</td><td>8.68 (n/a)</td><td>8.63 (n/a)</td><td>8.41 (n/a)</td><td>0.27 (n/a)</td><td>9.11 (n/a)</td><td>8.67 (n/a)</td><td>8.62 (n/a)</td><td>8.40 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.06 (+15.56%)</td><td>0.86 (+9.03%)</td><td>0.85 (+12.73%)</td><td>0.71 (+3.70%)</td><td>0.13 <b>(+49.87%)</b></td><td>1.04 (+15.56%)</td><td>0.84 (+9.03%)</td><td>0.84 (+12.73%)</td><td>0.70 (+3.70%)</td><td>0.13 <b>(+49.87%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.91 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.69 (n/a)</td><td>0.09 (n/a)</td><td>0.90 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.21 (+3.55%)</td><td>1.12 (+8.40%)</td><td>1.11 (-0.21%)</td><td>0.99 (+15.90%)</td><td>0.10 <b>(-35.05%)</b></td><td>1.20 (+3.55%)</td><td>1.10 (+8.40%)</td><td>1.10 (-0.21%)</td><td>0.98 (+15.90%)</td><td>0.09 <b>(-35.05%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.17 (n/a)</td><td>1.03 (n/a)</td><td>1.11 (n/a)</td><td>0.86 (n/a)</td><td>0.15 (n/a)</td><td>1.16 (n/a)</td><td>1.02 (n/a)</td><td>1.10 (n/a)</td><td>0.85 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>17.53 (+10.95%)</td><td>16.82 (+13.53%)</td><td>16.90 (+15.20%)</td><td>15.84 (+14.76%)</td><td>0.75 (-3.96%)</td><td>17.33 (+10.95%)</td><td>16.63 (+13.53%)</td><td>16.70 (+15.20%)</td><td>15.65 (+14.76%)</td><td>0.74 (-3.96%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>15.80 (n/a)</td><td>14.82 (n/a)</td><td>14.67 (n/a)</td><td>13.80 (n/a)</td><td>0.78 (n/a)</td><td>15.62 (n/a)</td><td>14.64 (n/a)</td><td>14.50 (n/a)</td><td>13.64 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.16 (+16.82%)</td><td>12.68 (+16.48%)</td><td>13.49 (+14.77%)</td><td>8.71 <b>(+25.40%)</b></td><td>2.24 (+1.20%)</td><td>13.91 (+16.82%)</td><td>12.46 (+16.48%)</td><td>13.26 (+14.77%)</td><td>8.56 <b>(+25.40%)</b></td><td>2.20 (+1.20%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>12.12 (n/a)</td><td>10.89 (n/a)</td><td>11.76 (n/a)</td><td>6.95 (n/a)</td><td>2.21 (n/a)</td><td>11.91 (n/a)</td><td>10.70 (n/a)</td><td>11.55 (n/a)</td><td>6.83 (n/a)</td><td>2.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>7.68 (-2.90%)</td><td>6.92 (-6.77%)</td><td>7.52 (-3.73%)</td><td>5.80 (-4.47%)</td><td>0.94 <b>(+21.33%)</b></td><td>7.55 (-2.90%)</td><td>6.80 (-6.77%)</td><td>7.39 (-3.73%)</td><td>5.70 (-4.47%)</td><td>0.92 <b>(+21.33%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.91 (n/a)</td><td>7.42 (n/a)</td><td>7.81 (n/a)</td><td>6.08 (n/a)</td><td>0.77 (n/a)</td><td>7.78 (n/a)</td><td>7.29 (n/a)</td><td>7.67 (n/a)</td><td>5.97 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.35 (-6.20%)</td><td>5.76 (-6.89%)</td><td>5.75 (-6.45%)</td><td>5.33 (-3.10%)</td><td>0.37 <b>(-29.61%)</b></td><td>6.25 (-6.20%)</td><td>5.67 (-6.89%)</td><td>5.66 (-6.45%)</td><td>5.25 (-3.10%)</td><td>0.37 <b>(-29.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>6.77 (n/a)</td><td>6.19 (n/a)</td><td>6.14 (n/a)</td><td>5.50 (n/a)</td><td>0.53 (n/a)</td><td>6.66 (n/a)</td><td>6.09 (n/a)</td><td>6.05 (n/a)</td><td>5.42 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.44 (n/a)</td><td>13.01 (n/a)</td><td>13.17 (n/a)</td><td>12.18 (n/a)</td><td>0.49 (n/a)</td><td>13.43 (n/a)</td><td>13.01 (n/a)</td><td>13.16 (n/a)</td><td>12.17 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.40 (n/a)</td><td>11.72 (n/a)</td><td>11.47 (n/a)</td><td>10.80 (n/a)</td><td>1.02 (n/a)</td><td>13.39 (n/a)</td><td>11.72 (n/a)</td><td>11.47 (n/a)</td><td>10.79 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.40 (n/a)</td><td>158.02 (n/a)</td><td>157.90 (n/a)</td><td>126.10 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.70 (n/a)</td><td>154.60 (n/a)</td><td>151.80 (n/a)</td><td>135.70 (n/a)</td><td>15.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>145.70 (n/a)</td><td>135.66 (n/a)</td><td>134.20 (n/a)</td><td>126.40 (n/a)</td><td>7.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.40 (n/a)</td><td>170.32 (n/a)</td><td>177.60 (n/a)</td><td>132.80 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.60 (n/a)</td><td>177.08 (n/a)</td><td>186.40 (n/a)</td><td>138.00 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.60 (n/a)</td><td>208.38 (n/a)</td><td>203.00 (n/a)</td><td>189.40 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>160.24 (n/a)</td><td>152.50 (n/a)</td><td>145.10 (n/a)</td><td>17.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.50 (n/a)</td><td>218.66 (n/a)</td><td>221.80 (n/a)</td><td>198.90 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.80 (n/a)</td><td>182.18 (n/a)</td><td>189.40 (n/a)</td><td>125.90 (n/a)</td><td>38.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>183.50 (n/a)</td><td>202.10 (n/a)</td><td>124.80 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>153.56 (n/a)</td><td>158.20 (n/a)</td><td>123.60 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.50 (n/a)</td><td>191.84 (n/a)</td><td>177.50 (n/a)</td><td>130.40 (n/a)</td><td>52.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.80 (n/a)</td><td>187.46 (n/a)</td><td>179.00 (n/a)</td><td>149.50 (n/a)</td><td>35.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>186.72 (n/a)</td><td>178.50 (n/a)</td><td>176.20 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>190.74 (n/a)</td><td>179.30 (n/a)</td><td>163.40 (n/a)</td><td>35.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>199.88 (n/a)</td><td>193.70 (n/a)</td><td>166.60 (n/a)</td><td>25.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>239.30 (n/a)</td><td>180.20 (n/a)</td><td>177.90 (n/a)</td><td>123.40 (n/a)</td><td>46.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>163.86 (n/a)</td><td>175.30 (n/a)</td><td>99.20 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.80 (n/a)</td><td>162.26 (n/a)</td><td>159.20 (n/a)</td><td>125.90 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>272.80 (n/a)</td><td>172.04 (n/a)</td><td>160.10 (n/a)</td><td>112.00 (n/a)</td><td>62.37 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.60 (n/a)</td><td>161.52 (n/a)</td><td>166.20 (n/a)</td><td>116.60 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>177.20 (n/a)</td><td>147.98 (n/a)</td><td>142.00 (n/a)</td><td>123.20 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.80 (n/a)</td><td>182.34 (n/a)</td><td>182.60 (n/a)</td><td>123.00 (n/a)</td><td>42.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>372.30 (n/a)</td><td>262.12 (n/a)</td><td>244.50 (n/a)</td><td>194.20 (n/a)</td><td>72.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.60 (n/a)</td><td>177.04 (n/a)</td><td>170.40 (n/a)</td><td>157.90 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>161.24 (n/a)</td><td>164.70 (n/a)</td><td>135.20 (n/a)</td><td>24.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.40 (n/a)</td><td>173.28 (n/a)</td><td>176.00 (n/a)</td><td>155.40 (n/a)</td><td>16.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>228.00 (n/a)</td><td>175.26 (n/a)</td><td>165.00 (n/a)</td><td>153.00 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>232.70 (n/a)</td><td>163.70 (n/a)</td><td>156.40 (n/a)</td><td>119.00 (n/a)</td><td>42.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>198.70 (n/a)</td><td>176.52 (n/a)</td><td>188.20 (n/a)</td><td>125.90 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.50 (n/a)</td><td>180.40 (n/a)</td><td>175.40 (n/a)</td><td>161.60 (n/a)</td><td>16.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>232.50 (n/a)</td><td>203.96 (n/a)</td><td>200.30 (n/a)</td><td>184.10 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-17.27%)</td><td>0.02 (-3.94%)</td><td>0.02 (-1.58%)</td><td>0.02 (+13.75%)</td><td>0.00 <b>(-56.54%)</b></td><td>185.10 (-12.11%)</td><td>167.88 (+1.38%)</td><td>166.10 (+1.59%)</td><td>144.90 <b>(+20.85%)</b></td><td>15.30 <b>(-53.30%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>165.60 (n/a)</td><td>163.50 (n/a)</td><td>119.90 (n/a)</td><td>32.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-18.01%)</td><td>0.02 (-2.64%)</td><td>0.02 (+11.26%)</td><td>0.02 (+7.96%)</td><td>0.00 <b>(-65.54%)</b></td><td>190.10 (-7.36%)</td><td>177.70 (-0.13%)</td><td>179.60 (-10.11%)</td><td>159.20 <b>(+21.99%)</b></td><td>12.95 <b>(-61.65%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>177.94 (n/a)</td><td>199.80 (n/a)</td><td>130.50 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+5.00%)</td><td>0.02 (-11.16%)</td><td>0.02 (-9.63%)</td><td>0.01 <b>(-42.34%)</b></td><td>0.01 <b>(+150.71%)</b></td><td>339.70 <b>(+73.40%)</b></td><td>208.38 <b>(+21.49%)</b></td><td>182.00 (+10.64%)</td><td>145.20 (-4.72%)</td><td>76.82 <b>(+332.54%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.90 (n/a)</td><td>171.52 (n/a)</td><td>164.50 (n/a)</td><td>152.40 (n/a)</td><td>17.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-13.68%)</td><td>0.02 (-3.37%)</td><td>0.02 (-0.17%)</td><td>0.02 (+3.81%)</td><td>0.00 <b>(-38.44%)</b></td><td>218.20 (-3.66%)</td><td>181.74 (+1.85%)</td><td>180.50 (+0.17%)</td><td>154.60 (+15.81%)</td><td>23.29 <b>(-29.63%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.50 (n/a)</td><td>178.44 (n/a)</td><td>180.20 (n/a)</td><td>133.50 (n/a)</td><td>33.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (-11.70%)</td><td>0.02 (-3.90%)</td><td>0.02 (+1.23%)</td><td>0.02 (-4.57%)</td><td>0.00 <b>(-37.19%)</b></td><td>208.90 (+4.82%)</td><td>185.90 (+3.35%)</td><td>187.40 (-1.21%)</td><td>164.40 (+13.30%)</td><td>16.36 <b>(-24.89%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.30 (n/a)</td><td>179.88 (n/a)</td><td>189.70 (n/a)</td><td>145.10 (n/a)</td><td>21.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+5.04%)</td><td>0.02 (-3.25%)</td><td>0.02 (-4.61%)</td><td>0.02 (-7.79%)</td><td>0.00 <b>(+59.78%)</b></td><td>226.10 (+8.49%)</td><td>189.24 (+5.30%)</td><td>183.10 (+4.81%)</td><td>144.90 (-4.80%)</td><td>35.74 <b>(+70.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>179.72 (n/a)</td><td>174.70 (n/a)</td><td>152.20 (n/a)</td><td>20.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 <b>(-28.52%)</b></td><td>0.02 (-15.69%)</td><td>0.02 (-4.38%)</td><td>0.01 <b>(-23.59%)</b></td><td>0.00 <b>(-28.55%)</b></td><td>289.50 <b>(+30.88%)</b></td><td>219.88 (+18.55%)</td><td>200.60 (+4.59%)</td><td>196.00 <b>(+39.90%)</b></td><td>39.88 <b>(+35.85%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.20 (n/a)</td><td>185.48 (n/a)</td><td>191.80 (n/a)</td><td>140.10 (n/a)</td><td>29.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (-11.62%)</td><td>0.02 (-13.57%)</td><td>0.02 (-8.23%)</td><td>0.01 <b>(-29.09%)</b></td><td>0.00 <b>(+67.88%)</b></td><td>339.70 <b>(+41.01%)</b></td><td>251.66 (+18.01%)</td><td>228.70 (+9.01%)</td><td>222.70 (+13.16%)</td><td>49.63 <b>(+174.23%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.90 (n/a)</td><td>213.26 (n/a)</td><td>209.80 (n/a)</td><td>196.80 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 <b>(-25.55%)</b></td><td>0.05 (-4.84%)</td><td>0.05 (+1.50%)</td><td>0.04 (+7.68%)</td><td>0.00 <b>(-62.96%)</b></td><td>193.40 (-7.11%)</td><td>168.26 (+1.40%)</td><td>167.80 (-1.47%)</td><td>148.00 <b>(+34.30%)</b></td><td>17.26 <b>(-51.07%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>165.94 (n/a)</td><td>170.30 (n/a)</td><td>110.20 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (+1.21%)</td><td>0.05 (+0.59%)</td><td>0.05 (-1.86%)</td><td>0.04 (+7.68%)</td><td>0.00 (-9.66%)</td><td>193.20 (-7.16%)</td><td>174.94 (-0.83%)</td><td>175.80 (+1.91%)</td><td>157.40 (-1.25%)</td><td>14.97 (-19.28%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.10 (n/a)</td><td>176.40 (n/a)</td><td>172.50 (n/a)</td><td>159.40 (n/a)</td><td>18.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 <b>(-27.51%)</b></td><td>0.05 (-3.41%)</td><td>0.05 (+5.45%)</td><td>0.04 (+16.18%)</td><td>0.00 <b>(-79.47%)</b></td><td>184.20 (-13.93%)</td><td>173.54 (+0.02%)</td><td>169.30 (-5.15%)</td><td>165.10 <b>(+37.93%)</b></td><td>8.72 <b>(-74.29%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>173.50 (n/a)</td><td>178.50 (n/a)</td><td>119.70 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (-6.90%)</td><td>0.05 (-0.74%)</td><td>0.05 (+0.71%)</td><td>0.04 (+16.56%)</td><td>0.01 <b>(-27.01%)</b></td><td>198.80 (-14.20%)</td><td>170.38 (-1.25%)</td><td>174.10 (-0.68%)</td><td>139.00 (+7.42%)</td><td>26.93 <b>(-32.27%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>172.54 (n/a)</td><td>175.30 (n/a)</td><td>129.40 (n/a)</td><td>39.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 <b>(-22.64%)</b></td><td>0.05 (-8.65%)</td><td>0.05 (+3.48%)</td><td>0.04 (-5.76%)</td><td>0.01 <b>(-56.11%)</b></td><td>204.30 (+6.13%)</td><td>177.48 (+6.72%)</td><td>178.00 (-3.37%)</td><td>152.10 <b>(+29.34%)</b></td><td>19.01 <b>(-40.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>166.30 (n/a)</td><td>184.20 (n/a)</td><td>117.60 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 <b>(-25.96%)</b></td><td>0.04 (-14.12%)</td><td>0.04 (-17.33%)</td><td>0.03 (+0.96%)</td><td>0.01 <b>(-49.98%)</b></td><td>259.10 (-0.96%)</td><td>204.42 (+12.36%)</td><td>201.90 <b>(+20.97%)</b></td><td>176.20 <b>(+35.02%)</b></td><td>32.96 <b>(-34.08%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.60 (n/a)</td><td>181.94 (n/a)</td><td>166.90 (n/a)</td><td>130.50 (n/a)</td><td>50.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-11.22%)</td><td>0.05 (+3.30%)</td><td>0.04 (+6.73%)</td><td>0.04 (+11.01%)</td><td>0.00 <b>(-56.48%)</b></td><td>189.40 (-9.94%)</td><td>178.48 (-4.56%)</td><td>184.10 (-6.31%)</td><td>165.60 (+12.65%)</td><td>11.46 <b>(-56.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>187.00 (n/a)</td><td>196.50 (n/a)</td><td>147.00 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (+7.98%)</td><td>0.05 (-11.67%)</td><td>0.05 (-16.95%)</td><td>0.03 (-18.01%)</td><td>0.01 <b>(+44.58%)</b></td><td>240.30 <b>(+21.98%)</b></td><td>190.26 (+16.65%)</td><td>178.60 <b>(+20.43%)</b></td><td>129.00 (-7.39%)</td><td>46.58 <b>(+68.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>163.10 (n/a)</td><td>148.30 (n/a)</td><td>139.30 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-15.91%)</td><td>0.05 (-9.57%)</td><td>0.04 (-8.40%)</td><td>0.04 (-9.78%)</td><td>0.00 <b>(-36.81%)</b></td><td>213.10 (+10.87%)</td><td>183.24 (+9.74%)</td><td>182.90 (+9.19%)</td><td>158.70 (+18.97%)</td><td>19.58 (-16.16%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>166.98 (n/a)</td><td>167.50 (n/a)</td><td>133.40 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (-13.81%)</td><td>0.03 (-18.16%)</td><td>0.03 (-11.63%)</td><td>0.02 <b>(-38.62%)</b></td><td>0.01 <b>(+76.12%)</b></td><td>369.30 <b>(+62.90%)</b></td><td>255.72 <b>(+26.33%)</b></td><td>235.60 (+13.16%)</td><td>209.10 (+16.04%)</td><td>64.48 <b>(+251.86%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.70 (n/a)</td><td>202.42 (n/a)</td><td>208.20 (n/a)</td><td>180.20 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (-2.38%)</td><td>0.11 (-2.45%)</td><td>0.11 (-3.62%)</td><td>0.10 (+1.17%)</td><td>0.01 (-14.88%)</td><td>171.20 (-1.15%)</td><td>152.18 (+2.18%)</td><td>146.70 (+3.75%)</td><td>133.10 (+2.46%)</td><td>16.71 (-12.91%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>173.20 (n/a)</td><td>148.94 (n/a)</td><td>141.40 (n/a)</td><td>129.90 (n/a)</td><td>19.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (+12.20%)</td><td>0.11 (+18.50%)</td><td>0.11 (-1.71%)</td><td>0.09 <b>(+62.94%)</b></td><td>0.02 <b>(-40.23%)</b></td><td>188.20 <b>(-38.62%)</b></td><td>159.18 <b>(-23.32%)</b></td><td>156.00 (+1.76%)</td><td>126.50 (-10.92%)</td><td>28.12 <b>(-66.48%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>306.60 (n/a)</td><td>207.58 (n/a)</td><td>153.30 (n/a)</td><td>142.00 (n/a)</td><td>83.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-6.95%)</td><td>0.09 (+2.50%)</td><td>0.10 (+17.41%)</td><td>0.06 <b>(-23.24%)</b></td><td>0.02 (+15.57%)</td><td>277.80 <b>(+30.24%)</b></td><td>185.32 (+0.11%)</td><td>165.90 (-14.84%)</td><td>144.40 (+7.44%)</td><td>53.21 <b>(+76.48%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.30 (n/a)</td><td>185.12 (n/a)</td><td>194.80 (n/a)</td><td>134.40 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (+14.88%)</td><td>0.10 (+3.64%)</td><td>0.09 (+4.04%)</td><td>0.08 (-3.20%)</td><td>0.02 <b>(+54.53%)</b></td><td>208.00 (+3.33%)</td><td>175.10 (-2.53%)</td><td>176.60 (-3.92%)</td><td>135.00 (-12.96%)</td><td>26.05 <b>(+35.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>179.64 (n/a)</td><td>183.80 (n/a)</td><td>155.10 (n/a)</td><td>19.25 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-8.45%)</td><td>0.09 (+0.20%)</td><td>0.09 (+3.24%)</td><td>0.07 (-6.27%)</td><td>0.02 (-7.50%)</td><td>248.70 (+6.69%)</td><td>187.16 (-0.13%)</td><td>180.20 (-3.17%)</td><td>147.50 (+9.26%)</td><td>39.98 (+10.31%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.10 (n/a)</td><td>187.40 (n/a)</td><td>186.10 (n/a)</td><td>135.00 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (+0.46%)</td><td>0.09 (-3.17%)</td><td>0.09 (-8.52%)</td><td>0.06 <b>(-20.15%)</b></td><td>0.02 <b>(+46.87%)</b></td><td>283.30 <b>(+25.24%)</b></td><td>198.16 (+6.10%)</td><td>191.40 (+9.31%)</td><td>157.50 (-0.44%)</td><td>50.51 <b>(+84.12%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>186.76 (n/a)</td><td>175.10 (n/a)</td><td>158.20 (n/a)</td><td>27.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (+10.37%)</td><td>0.09 (-8.43%)</td><td>0.08 (-16.53%)</td><td>0.07 (-18.88%)</td><td>0.02 <b>(+109.19%)</b></td><td>226.50 <b>(+23.30%)</b></td><td>189.08 (+12.75%)</td><td>207.90 (+19.76%)</td><td>130.70 (-9.42%)</td><td>39.26 <b>(+131.07%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>167.70 (n/a)</td><td>173.60 (n/a)</td><td>144.30 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (+5.33%)</td><td>0.08 (+2.92%)</td><td>0.07 (-8.01%)</td><td>0.07 <b>(+35.62%)</b></td><td>0.01 <b>(-34.42%)</b></td><td>236.90 <b>(-26.27%)</b></td><td>211.84 (-5.84%)</td><td>219.40 (+8.72%)</td><td>170.90 (-5.06%)</td><td>26.59 <b>(-54.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>321.30 (n/a)</td><td>224.98 (n/a)</td><td>201.80 (n/a)</td><td>180.00 (n/a)</td><td>58.35 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 <b>(-24.20%)</b></td><td>0.17 <b>(-26.26%)</b></td><td>0.18 <b>(-23.06%)</b></td><td>0.11 <b>(-45.73%)</b></td><td>0.04 <b>(+33.54%)</b></td><td>310.00 <b>(+84.30%)</b></td><td>200.18 <b>(+42.66%)</b></td><td>181.10 <b>(+29.91%)</b></td><td>151.30 <b>(+31.91%)</b></td><td>64.56 <b>(+231.33%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>168.20 (n/a)</td><td>140.32 (n/a)</td><td>139.40 (n/a)</td><td>114.70 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (+2.38%)</td><td>0.20 (+13.50%)</td><td>0.18 (+4.38%)</td><td>0.16 <b>(+59.87%)</b></td><td>0.04 <b>(-26.26%)</b></td><td>199.30 <b>(-37.45%)</b></td><td>168.86 (-16.44%)</td><td>179.20 (-4.17%)</td><td>129.10 (-2.34%)</td><td>29.95 <b>(-56.96%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>318.60 (n/a)</td><td>202.08 (n/a)</td><td>187.00 (n/a)</td><td>132.20 (n/a)</td><td>69.58 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (+9.14%)</td><td>0.19 (-2.47%)</td><td>0.18 (-5.03%)</td><td>0.15 (-9.33%)</td><td>0.03 <b>(+62.41%)</b></td><td>213.30 (+10.29%)</td><td>180.46 (+3.87%)</td><td>181.60 (+5.28%)</td><td>136.60 (-8.38%)</td><td>27.84 <b>(+58.30%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.40 (n/a)</td><td>173.74 (n/a)</td><td>172.50 (n/a)</td><td>149.10 (n/a)</td><td>17.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (-1.69%)</td><td>0.20 (+6.88%)</td><td>0.21 <b>(+20.17%)</b></td><td>0.14 (+0.58%)</td><td>0.05 (-1.37%)</td><td>240.40 (-0.58%)</td><td>175.06 (-6.27%)</td><td>155.80 (-16.77%)</td><td>125.00 (+1.71%)</td><td>46.07 (+4.44%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>241.80 (n/a)</td><td>186.78 (n/a)</td><td>187.20 (n/a)</td><td>122.90 (n/a)</td><td>44.11 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (+9.00%)</td><td>0.19 (+11.54%)</td><td>0.21 <b>(+44.41%)</b></td><td>0.13 (-5.37%)</td><td>0.05 (+14.93%)</td><td>250.40 (+5.70%)</td><td>179.72 (-9.35%)</td><td>155.00 <b>(-30.77%)</b></td><td>133.40 (-8.25%)</td><td>47.49 (+12.81%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>236.90 (n/a)</td><td>198.26 (n/a)</td><td>223.90 (n/a)</td><td>145.40 (n/a)</td><td>42.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (+5.22%)</td><td>0.18 (+2.63%)</td><td>0.16 (-3.68%)</td><td>0.15 (-1.72%)</td><td>0.02 <b>(+31.13%)</b></td><td>215.20 (+1.75%)</td><td>189.60 (-2.07%)</td><td>199.50 (+3.80%)</td><td>156.50 (-4.98%)</td><td>23.74 <b>(+25.90%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>211.50 (n/a)</td><td>193.60 (n/a)</td><td>192.20 (n/a)</td><td>164.70 (n/a)</td><td>18.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (-2.09%)</td><td>0.15 (+7.05%)</td><td>0.15 (+0.77%)</td><td>0.14 <b>(+34.43%)</b></td><td>0.01 <b>(-69.34%)</b></td><td>238.50 <b>(-25.61%)</b></td><td>221.88 (-8.68%)</td><td>219.90 (-0.77%)</td><td>209.80 (+2.14%)</td><td>10.50 <b>(-77.12%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>320.60 (n/a)</td><td>242.98 (n/a)</td><td>221.60 (n/a)</td><td>205.40 (n/a)</td><td>45.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+14.22%)</td><td>0.03 (+11.75%)</td><td>0.02 (+3.64%)</td><td>0.02 <b>(+38.63%)</b></td><td>0.00 <b>(-20.63%)</b></td><td>189.40 <b>(-27.88%)</b></td><td>164.42 (-12.72%)</td><td>165.10 (-3.51%)</td><td>130.00 (-12.46%)</td><td>22.04 <b>(-51.76%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>262.60 (n/a)</td><td>188.38 (n/a)</td><td>171.10 (n/a)</td><td>148.50 (n/a)</td><td>45.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-0.77%)</td><td>0.03 (+6.08%)</td><td>0.03 (+14.07%)</td><td>0.02 (+10.37%)</td><td>0.00 <b>(-40.74%)</b></td><td>182.60 (-9.38%)</td><td>162.06 (-6.87%)</td><td>158.20 (-12.31%)</td><td>145.60 (+0.76%)</td><td>14.21 <b>(-44.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.50 (n/a)</td><td>174.02 (n/a)</td><td>180.40 (n/a)</td><td>144.50 (n/a)</td><td>25.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (+3.08%)</td><td>0.02 (-6.28%)</td><td>0.02 (-11.57%)</td><td>0.01 (+0.18%)</td><td>0.00 (+9.47%)</td><td>330.30 (-0.18%)</td><td>241.64 (+7.21%)</td><td>240.90 (+13.05%)</td><td>174.10 (-2.95%)</td><td>62.06 (+1.59%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>330.90 (n/a)</td><td>225.38 (n/a)</td><td>213.10 (n/a)</td><td>179.40 (n/a)</td><td>61.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-0.19%)</td><td>0.02 (+4.73%)</td><td>0.02 (-1.43%)</td><td>0.02 (-2.03%)</td><td>0.00 (+13.66%)</td><td>225.10 (+2.04%)</td><td>185.80 (-4.10%)</td><td>191.60 (+1.48%)</td><td>155.60 (+0.19%)</td><td>29.63 (+11.21%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.60 (n/a)</td><td>193.74 (n/a)</td><td>188.80 (n/a)</td><td>155.30 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+9.85%)</td><td>0.03 (+1.57%)</td><td>0.02 (-2.02%)</td><td>0.02 (-2.13%)</td><td>0.01 <b>(+25.17%)</b></td><td>188.80 (+2.16%)</td><td>158.92 (-0.43%)</td><td>168.50 (+2.06%)</td><td>104.50 (-8.97%)</td><td>31.90 (+9.74%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>159.60 (n/a)</td><td>165.10 (n/a)</td><td>114.80 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+0.14%)</td><td>0.02 (-10.92%)</td><td>0.02 (+3.14%)</td><td>0.01 <b>(-23.71%)</b></td><td>0.01 (+15.48%)</td><td>293.80 <b>(+31.04%)</b></td><td>203.54 (+16.66%)</td><td>169.00 (-3.04%)</td><td>132.40 (-0.15%)</td><td>67.95 <b>(+61.23%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>174.48 (n/a)</td><td>174.30 (n/a)</td><td>132.60 (n/a)</td><td>42.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-2.59%)</td><td>0.02 (+7.69%)</td><td>0.02 (+4.52%)</td><td>0.02 <b>(+27.96%)</b></td><td>0.00 <b>(-38.24%)</b></td><td>188.20 <b>(-21.84%)</b></td><td>168.22 (-9.65%)</td><td>174.90 (-4.32%)</td><td>136.80 (+2.70%)</td><td>19.94 <b>(-50.97%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>186.18 (n/a)</td><td>182.80 (n/a)</td><td>133.20 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 <b>(+45.35%)</b></td><td>0.02 <b>(+25.78%)</b></td><td>0.02 (+9.43%)</td><td>0.02 <b>(+69.81%)</b></td><td>0.01 <b>(+20.02%)</b></td><td>215.50 <b>(-41.10%)</b></td><td>172.24 <b>(-23.05%)</b></td><td>171.50 (-8.63%)</td><td>119.50 <b>(-31.24%)</b></td><td>37.62 <b>(-53.31%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>365.90 (n/a)</td><td>223.84 (n/a)</td><td>187.70 (n/a)</td><td>173.80 (n/a)</td><td>80.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-2.85%)</td><td>0.02 (+1.87%)</td><td>0.02 (+0.69%)</td><td>0.02 (+18.69%)</td><td>0.00 <b>(-37.84%)</b></td><td>206.20 (-15.77%)</td><td>173.50 (-3.75%)</td><td>166.10 (-0.72%)</td><td>153.20 (+2.96%)</td><td>20.02 <b>(-47.00%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.80 (n/a)</td><td>180.26 (n/a)</td><td>167.30 (n/a)</td><td>148.80 (n/a)</td><td>37.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-6.71%)</td><td>0.03 (+3.08%)</td><td>0.03 (+6.80%)</td><td>0.02 (+4.40%)</td><td>0.00 (-14.93%)</td><td>203.50 (-4.19%)</td><td>160.72 (-3.78%)</td><td>155.60 (-6.38%)</td><td>135.90 (+7.18%)</td><td>28.30 (-14.11%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>167.04 (n/a)</td><td>166.20 (n/a)</td><td>126.80 (n/a)</td><td>32.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-1.56%)</td><td>0.02 (-3.60%)</td><td>0.02 (-9.33%)</td><td>0.02 (-7.12%)</td><td>0.00 (+15.11%)</td><td>232.50 (+7.69%)</td><td>194.00 (+4.41%)</td><td>202.60 (+10.29%)</td><td>152.10 (+1.60%)</td><td>30.60 <b>(+26.51%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.90 (n/a)</td><td>185.80 (n/a)</td><td>183.70 (n/a)</td><td>149.70 (n/a)</td><td>24.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+7.46%)</td><td>0.02 (+16.79%)</td><td>0.02 <b>(+22.45%)</b></td><td>0.02 (+14.63%)</td><td>0.00 (-14.05%)</td><td>193.40 (-12.76%)</td><td>172.18 (-14.60%)</td><td>169.80 (-18.37%)</td><td>162.40 (-6.99%)</td><td>12.57 <b>(-28.91%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.70 (n/a)</td><td>201.62 (n/a)</td><td>208.00 (n/a)</td><td>174.60 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+14.08%)</td><td>0.02 (+4.46%)</td><td>0.02 (+1.34%)</td><td>0.02 (-6.94%)</td><td>0.01 <b>(+50.25%)</b></td><td>242.00 (+7.46%)</td><td>189.24 (-2.33%)</td><td>200.10 (-1.33%)</td><td>137.30 (-12.32%)</td><td>40.49 <b>(+40.15%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.20 (n/a)</td><td>193.76 (n/a)</td><td>202.80 (n/a)</td><td>156.60 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-17.99%)</td><td>0.02 (-10.64%)</td><td>0.02 (-11.27%)</td><td>0.02 (-2.51%)</td><td>0.00 <b>(-44.30%)</b></td><td>207.70 (+2.57%)</td><td>188.78 (+9.78%)</td><td>197.70 (+12.71%)</td><td>155.00 <b>(+21.95%)</b></td><td>22.25 <b>(-31.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>171.96 (n/a)</td><td>175.40 (n/a)</td><td>127.10 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-18.14%)</td><td>0.02 (-12.18%)</td><td>0.02 (-7.13%)</td><td>0.01 <b>(-36.25%)</b></td><td>0.01 (+14.81%)</td><td>313.80 <b>(+56.82%)</b></td><td>209.62 (+18.86%)</td><td>199.50 (+7.66%)</td><td>151.10 <b>(+22.15%)</b></td><td>66.94 <b>(+119.37%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>176.36 (n/a)</td><td>185.30 (n/a)</td><td>123.70 (n/a)</td><td>30.51 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+13.10%)</td><td>0.02 (+10.23%)</td><td>0.02 (+16.77%)</td><td>0.02 (-0.89%)</td><td>0.00 <b>(+44.72%)</b></td><td>223.40 (+0.90%)</td><td>178.28 (-8.49%)</td><td>169.90 (-14.36%)</td><td>147.10 (-11.60%)</td><td>28.25 <b>(+32.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.40 (n/a)</td><td>194.82 (n/a)</td><td>198.40 (n/a)</td><td>166.40 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (+3.34%)</td><td>0.05 (+8.29%)</td><td>0.05 (+10.82%)</td><td>0.05 (+3.50%)</td><td>0.01 (-6.33%)</td><td>180.20 (-3.38%)</td><td>155.20 (-8.05%)</td><td>160.60 (-9.78%)</td><td>120.20 (-3.22%)</td><td>22.25 (-13.06%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>168.78 (n/a)</td><td>178.00 (n/a)</td><td>124.20 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (+0.62%)</td><td>0.06 (+0.36%)</td><td>0.05 (-7.29%)</td><td>0.04 (-9.14%)</td><td>0.01 (+13.89%)</td><td>189.60 (+10.10%)</td><td>146.68 (+0.40%)</td><td>150.20 (+7.90%)</td><td>117.30 (-0.59%)</td><td>28.35 <b>(+20.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>146.10 (n/a)</td><td>139.20 (n/a)</td><td>118.00 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-2.75%)</td><td>0.04 (-0.12%)</td><td>0.04 (+12.87%)</td><td>0.02 (-16.78%)</td><td>0.01 (+13.50%)</td><td>377.50 <b>(+20.18%)</b></td><td>233.62 (+3.07%)</td><td>186.70 (-11.39%)</td><td>181.60 (+2.83%)</td><td>83.45 <b>(+43.88%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.10 (n/a)</td><td>226.66 (n/a)</td><td>210.70 (n/a)</td><td>176.60 (n/a)</td><td>58.00 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-1.66%)</td><td>0.04 (+11.62%)</td><td>0.04 (+13.59%)</td><td>0.04 <b>(+31.42%)</b></td><td>0.00 <b>(-35.71%)</b></td><td>219.70 <b>(-23.90%)</b></td><td>197.22 (-12.04%)</td><td>191.80 (-11.98%)</td><td>177.70 (+1.66%)</td><td>20.90 <b>(-50.50%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.70 (n/a)</td><td>224.22 (n/a)</td><td>217.90 (n/a)</td><td>174.80 (n/a)</td><td>42.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (-7.70%)</td><td>0.05 (-2.32%)</td><td>0.06 (+2.13%)</td><td>0.05 (+6.94%)</td><td>0.01 <b>(-38.06%)</b></td><td>181.90 (-6.53%)</td><td>152.92 (+0.31%)</td><td>145.10 (-2.09%)</td><td>130.20 (+8.41%)</td><td>20.29 <b>(-36.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>152.44 (n/a)</td><td>148.20 (n/a)</td><td>120.10 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-3.49%)</td><td>0.05 (-11.82%)</td><td>0.06 (-9.15%)</td><td>0.04 (-14.80%)</td><td>0.01 (+16.11%)</td><td>209.90 (+17.39%)</td><td>158.60 (+14.73%)</td><td>144.20 (+10.08%)</td><td>125.60 (+3.54%)</td><td>32.78 <b>(+40.60%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>138.24 (n/a)</td><td>131.00 (n/a)</td><td>121.30 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (-8.22%)</td><td>0.05 (-9.44%)</td><td>0.04 (-10.66%)</td><td>0.04 (-18.42%)</td><td>0.01 (+1.91%)</td><td>230.20 <b>(+22.58%)</b></td><td>181.08 (+11.50%)</td><td>187.80 (+11.92%)</td><td>129.40 (+8.92%)</td><td>37.31 <b>(+34.90%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>162.40 (n/a)</td><td>167.80 (n/a)</td><td>118.80 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (-7.29%)</td><td>0.05 (-17.12%)</td><td>0.05 (-9.20%)</td><td>0.03 <b>(-44.31%)</b></td><td>0.01 <b>(+66.71%)</b></td><td>307.10 <b>(+79.59%)</b></td><td>191.10 <b>(+29.77%)</b></td><td>155.60 (+10.20%)</td><td>132.20 (+7.92%)</td><td>70.93 <b>(+221.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>147.26 (n/a)</td><td>141.20 (n/a)</td><td>122.50 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-3.80%)</td><td>0.05 (-4.28%)</td><td>0.06 (+3.52%)</td><td>0.04 (-19.47%)</td><td>0.01 <b>(+41.39%)</b></td><td>213.30 <b>(+24.16%)</b></td><td>155.22 (+6.70%)</td><td>140.10 (-3.45%)</td><td>125.20 (+3.99%)</td><td>34.72 <b>(+88.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.80 (n/a)</td><td>145.48 (n/a)</td><td>145.10 (n/a)</td><td>120.40 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (+2.74%)</td><td>0.05 (-12.76%)</td><td>0.05 <b>(-23.29%)</b></td><td>0.04 (-3.87%)</td><td>0.01 (+16.48%)</td><td>189.20 (+4.07%)</td><td>170.20 (+15.16%)</td><td>178.30 <b>(+30.34%)</b></td><td>130.50 (-2.61%)</td><td>23.14 (+14.71%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>147.80 (n/a)</td><td>136.80 (n/a)</td><td>134.00 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (+17.25%)</td><td>0.05 (+0.20%)</td><td>0.05 (-10.19%)</td><td>0.04 (-3.63%)</td><td>0.01 <b>(+95.78%)</b></td><td>190.20 (+3.76%)</td><td>159.02 (+1.77%)</td><td>164.60 (+11.29%)</td><td>123.30 (-14.67%)</td><td>28.77 <b>(+73.91%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>156.26 (n/a)</td><td>147.90 (n/a)</td><td>144.50 (n/a)</td><td>16.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-16.21%)</td><td>0.06 (-4.74%)</td><td>0.06 (-0.57%)</td><td>0.04 (-2.15%)</td><td>0.01 <b>(-33.82%)</b></td><td>201.40 (+2.18%)</td><td>151.06 (+2.43%)</td><td>140.80 (+0.57%)</td><td>122.30 (+19.43%)</td><td>31.02 (-18.68%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>197.10 (n/a)</td><td>147.48 (n/a)</td><td>140.00 (n/a)</td><td>102.40 (n/a)</td><td>38.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (+12.00%)</td><td>0.05 (+11.03%)</td><td>0.06 <b>(+23.68%)</b></td><td>0.04 (-3.91%)</td><td>0.01 <b>(+83.19%)</b></td><td>226.20 (+4.05%)</td><td>168.20 (-7.57%)</td><td>142.90 (-19.17%)</td><td>138.20 (-10.72%)</td><td>39.16 <b>(+65.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>181.98 (n/a)</td><td>176.80 (n/a)</td><td>154.80 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (+17.53%)</td><td>0.05 (+12.13%)</td><td>0.05 (+8.40%)</td><td>0.04 (+6.02%)</td><td>0.01 (+16.57%)</td><td>208.80 (-5.65%)</td><td>159.26 (-10.56%)</td><td>152.70 (-7.73%)</td><td>127.50 (-14.94%)</td><td>30.97 (-3.44%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>178.06 (n/a)</td><td>165.50 (n/a)</td><td>149.90 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 <b>(+22.92%)</b></td><td>0.05 (+14.60%)</td><td>0.05 (+1.68%)</td><td>0.04 <b>(+50.15%)</b></td><td>0.01 (+7.34%)</td><td>231.00 <b>(-33.41%)</b></td><td>181.80 (-15.28%)</td><td>177.50 (-1.66%)</td><td>128.10 (-18.67%)</td><td>42.93 <b>(-43.77%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.90 (n/a)</td><td>214.58 (n/a)</td><td>180.50 (n/a)</td><td>157.50 (n/a)</td><td>76.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (+3.44%)</td><td>0.05 (+8.36%)</td><td>0.04 (+9.67%)</td><td>0.04 (-1.95%)</td><td>0.01 <b>(+24.84%)</b></td><td>221.50 (+1.98%)</td><td>179.06 (-6.15%)</td><td>182.60 (-8.84%)</td><td>131.10 (-3.32%)</td><td>41.96 <b>(+26.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>190.80 (n/a)</td><td>200.30 (n/a)</td><td>135.60 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (-2.75%)</td><td>0.10 (-3.61%)</td><td>0.09 (-14.09%)</td><td>0.08 (+0.63%)</td><td>0.03 (-5.79%)</td><td>214.20 (-0.65%)</td><td>166.88 (+3.17%)</td><td>183.80 (+16.40%)</td><td>120.30 (+2.82%)</td><td>39.50 (-5.40%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>215.60 (n/a)</td><td>161.76 (n/a)</td><td>157.90 (n/a)</td><td>117.00 (n/a)</td><td>41.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (+2.41%)</td><td>0.10 (+3.56%)</td><td>0.09 (-2.21%)</td><td>0.08 <b>(+21.21%)</b></td><td>0.02 (-1.73%)</td><td>202.30 (-17.50%)</td><td>169.30 (-4.26%)</td><td>173.20 (+2.30%)</td><td>123.30 (-2.38%)</td><td>34.41 <b>(-20.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.20 (n/a)</td><td>176.84 (n/a)</td><td>169.30 (n/a)</td><td>126.30 (n/a)</td><td>43.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (+14.14%)</td><td>0.07 (+1.63%)</td><td>0.07 (+10.06%)</td><td>0.05 <b>(-24.08%)</b></td><td>0.02 <b>(+115.88%)</b></td><td>343.40 <b>(+31.72%)</b></td><td>241.22 (+2.66%)</td><td>219.00 (-9.13%)</td><td>173.10 (-12.40%)</td><td>64.69 <b>(+155.97%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>260.70 (n/a)</td><td>234.98 (n/a)</td><td>241.00 (n/a)</td><td>197.60 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (-18.44%)</td><td>0.08 (-11.92%)</td><td>0.08 (-7.62%)</td><td>0.06 (-13.77%)</td><td>0.01 <b>(-28.63%)</b></td><td>270.20 (+15.97%)</td><td>216.04 (+12.97%)</td><td>207.10 (+8.26%)</td><td>184.80 <b>(+22.63%)</b></td><td>32.05 (+5.36%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>191.24 (n/a)</td><td>191.30 (n/a)</td><td>150.70 (n/a)</td><td>30.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (+11.56%)</td><td>0.10 (+6.22%)</td><td>0.09 (+3.39%)</td><td>0.08 (+0.52%)</td><td>0.02 <b>(+31.52%)</b></td><td>202.50 (-0.49%)</td><td>166.58 (-4.82%)</td><td>181.80 (-3.25%)</td><td>128.30 (-10.34%)</td><td>31.86 (+17.02%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.50 (n/a)</td><td>175.02 (n/a)</td><td>187.90 (n/a)</td><td>143.10 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (-10.81%)</td><td>0.10 (-13.05%)</td><td>0.10 (-13.35%)</td><td>0.07 <b>(-26.60%)</b></td><td>0.02 (+2.63%)</td><td>234.80 <b>(+36.19%)</b></td><td>169.38 (+16.54%)</td><td>160.30 (+15.41%)</td><td>134.10 (+12.12%)</td><td>38.67 <b>(+59.60%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>172.40 (n/a)</td><td>145.34 (n/a)</td><td>138.90 (n/a)</td><td>119.60 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (+4.51%)</td><td>0.11 (+11.96%)</td><td>0.10 (+12.85%)</td><td>0.09 <b>(+28.13%)</b></td><td>0.02 <b>(-22.33%)</b></td><td>189.20 <b>(-21.91%)</b></td><td>159.10 (-14.15%)</td><td>159.10 (-11.36%)</td><td>113.70 (-4.29%)</td><td>29.05 <b>(-45.03%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>242.30 (n/a)</td><td>185.32 (n/a)</td><td>179.50 (n/a)</td><td>118.80 (n/a)</td><td>52.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (-0.50%)</td><td>0.09 (-2.37%)</td><td>0.09 (+7.39%)</td><td>0.04 <b>(-36.64%)</b></td><td>0.03 <b>(+34.29%)</b></td><td>392.50 <b>(+57.82%)</b></td><td>206.30 (+12.68%)</td><td>175.00 (-6.87%)</td><td>129.10 (+0.47%)</td><td>105.83 <b>(+135.39%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>183.08 (n/a)</td><td>187.90 (n/a)</td><td>128.50 (n/a)</td><td>44.96 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (-12.42%)</td><td>0.09 (-14.24%)</td><td>0.09 <b>(-26.09%)</b></td><td>0.07 (+15.71%)</td><td>0.02 <b>(-31.04%)</b></td><td>232.90 (-13.58%)</td><td>188.82 (+11.32%)</td><td>184.40 <b>(+35.29%)</b></td><td>132.50 (+14.22%)</td><td>43.03 <b>(-31.09%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>269.50 (n/a)</td><td>169.62 (n/a)</td><td>136.30 (n/a)</td><td>116.00 (n/a)</td><td>62.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-13.83%)</td><td>0.09 (-5.04%)</td><td>0.09 (-7.18%)</td><td>0.08 (-2.02%)</td><td>0.01 <b>(-35.87%)</b></td><td>218.20 (+2.06%)</td><td>185.74 (+3.71%)</td><td>183.20 (+7.70%)</td><td>155.70 (+16.11%)</td><td>24.68 <b>(-25.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.80 (n/a)</td><td>179.10 (n/a)</td><td>170.10 (n/a)</td><td>134.10 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-17.75%)</td><td>0.10 (+1.13%)</td><td>0.10 (+7.86%)</td><td>0.08 (+8.96%)</td><td>0.01 <b>(-52.63%)</b></td><td>198.60 (-8.23%)</td><td>168.54 (-4.11%)</td><td>167.10 (-7.32%)</td><td>146.40 <b>(+21.59%)</b></td><td>20.06 <b>(-46.06%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.40 (n/a)</td><td>175.76 (n/a)</td><td>180.30 (n/a)</td><td>120.40 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (-12.54%)</td><td>0.10 (-1.41%)</td><td>0.11 (+1.91%)</td><td>0.07 (-15.21%)</td><td>0.02 (-10.42%)</td><td>230.80 (+17.94%)</td><td>165.94 (+1.67%)</td><td>149.20 (-1.91%)</td><td>141.10 (+14.34%)</td><td>37.01 <b>(+20.27%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.70 (n/a)</td><td>163.22 (n/a)</td><td>152.10 (n/a)</td><td>123.40 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-9.55%)</td><td>0.09 (-6.94%)</td><td>0.09 (-12.52%)</td><td>0.08 (+7.13%)</td><td>0.01 <b>(-50.67%)</b></td><td>208.20 (-6.68%)</td><td>181.82 (+4.67%)</td><td>181.10 (+14.33%)</td><td>155.10 (+10.55%)</td><td>18.98 <b>(-49.05%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.10 (n/a)</td><td>173.70 (n/a)</td><td>158.40 (n/a)</td><td>140.30 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (+5.72%)</td><td>0.10 (+0.59%)</td><td>0.10 (+7.52%)</td><td>0.08 (-6.14%)</td><td>0.02 (+14.57%)</td><td>194.80 (+6.56%)</td><td>160.50 (-0.11%)</td><td>159.50 (-7.00%)</td><td>127.90 (-5.40%)</td><td>24.90 (+16.59%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.80 (n/a)</td><td>160.68 (n/a)</td><td>171.50 (n/a)</td><td>135.20 (n/a)</td><td>21.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-13.15%)</td><td>0.10 (+8.35%)</td><td>0.11 <b>(+20.59%)</b></td><td>0.08 <b>(+48.83%)</b></td><td>0.01 <b>(-64.06%)</b></td><td>192.90 <b>(-32.81%)</b></td><td>163.74 (-13.74%)</td><td>155.30 (-17.08%)</td><td>151.50 (+15.12%)</td><td>17.32 <b>(-71.87%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>287.10 (n/a)</td><td>189.82 (n/a)</td><td>187.30 (n/a)</td><td>131.60 (n/a)</td><td>61.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (+1.54%)</td><td>0.09 (-4.99%)</td><td>0.09 (-5.38%)</td><td>0.08 (-11.72%)</td><td>0.01 <b>(+54.06%)</b></td><td>214.40 (+13.26%)</td><td>181.58 (+6.15%)</td><td>183.00 (+5.66%)</td><td>153.70 (-1.54%)</td><td>24.03 <b>(+72.74%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>171.06 (n/a)</td><td>173.20 (n/a)</td><td>156.10 (n/a)</td><td>13.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (-19.99%)</td><td>0.18 (-12.01%)</td><td>0.17 (-9.64%)</td><td>0.17 (+3.83%)</td><td>0.02 <b>(-58.30%)</b></td><td>195.40 (-3.65%)</td><td>181.56 (+11.30%)</td><td>189.60 (+10.68%)</td><td>160.60 <b>(+24.98%)</b></td><td>15.17 <b>(-48.80%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.80 (n/a)</td><td>163.12 (n/a)</td><td>171.30 (n/a)</td><td>128.50 (n/a)</td><td>29.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (-14.85%)</td><td>0.19 (-8.51%)</td><td>0.20 (-3.97%)</td><td>0.17 (-11.63%)</td><td>0.02 <b>(-32.78%)</b></td><td>194.10 (+13.18%)</td><td>169.12 (+8.90%)</td><td>164.90 (+4.10%)</td><td>158.40 (+17.51%)</td><td>14.67 (-10.91%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>171.50 (n/a)</td><td>155.30 (n/a)</td><td>158.40 (n/a)</td><td>134.80 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 <b>(+43.70%)</b></td><td>0.18 (+18.87%)</td><td>0.16 (+11.55%)</td><td>0.12 (-14.58%)</td><td>0.05 <b>(+282.13%)</b></td><td>279.70 (+17.03%)</td><td>197.48 (-11.25%)</td><td>201.20 (-10.34%)</td><td>136.60 <b>(-30.41%)</b></td><td>54.44 <b>(+208.96%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>222.52 (n/a)</td><td>224.40 (n/a)</td><td>196.30 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (-19.59%)</td><td>0.17 (-4.76%)</td><td>0.16 (-5.96%)</td><td>0.16 (+6.52%)</td><td>0.01 <b>(-57.88%)</b></td><td>209.80 (-6.09%)</td><td>196.62 (+3.15%)</td><td>204.30 (+6.35%)</td><td>178.20 <b>(+24.35%)</b></td><td>15.24 <b>(-49.52%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.40 (n/a)</td><td>190.62 (n/a)</td><td>192.10 (n/a)</td><td>143.30 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 <b>(-23.04%)</b></td><td>0.20 (-13.09%)</td><td>0.20 (-19.16%)</td><td>0.18 (+10.74%)</td><td>0.01 <b>(-71.85%)</b></td><td>180.40 (-9.71%)</td><td>168.56 (+10.60%)</td><td>167.40 <b>(+23.73%)</b></td><td>151.30 <b>(+29.98%)</b></td><td>11.90 <b>(-67.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>199.80 (n/a)</td><td>152.40 (n/a)</td><td>135.30 (n/a)</td><td>116.40 (n/a)</td><td>36.45 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (-4.66%)</td><td>0.22 (+9.16%)</td><td>0.24 <b>(+22.14%)</b></td><td>0.14 (+9.99%)</td><td>0.05 (-14.96%)</td><td>240.50 (-9.11%)</td><td>155.48 (-10.17%)</td><td>137.10 (-18.10%)</td><td>122.20 (+4.89%)</td><td>48.13 (-15.52%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>264.60 (n/a)</td><td>173.08 (n/a)</td><td>167.40 (n/a)</td><td>116.50 (n/a)</td><td>56.97 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (-17.70%)</td><td>0.16 (-16.63%)</td><td>0.17 (-0.68%)</td><td>0.09 <b>(-31.18%)</b></td><td>0.05 (-1.57%)</td><td>346.90 <b>(+45.27%)</b></td><td>230.10 <b>(+24.24%)</b></td><td>193.40 (+0.68%)</td><td>156.10 <b>(+21.48%)</b></td><td>78.95 <b>(+77.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>238.80 (n/a)</td><td>185.20 (n/a)</td><td>192.10 (n/a)</td><td>128.50 (n/a)</td><td>44.49 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (-1.00%)</td><td>0.22 (+10.40%)</td><td>0.24 <b>(+34.58%)</b></td><td>0.16 (+2.01%)</td><td>0.04 (-14.36%)</td><td>206.20 (-1.95%)</td><td>153.14 (-10.28%)</td><td>137.50 <b>(-25.68%)</b></td><td>132.30 (+0.99%)</td><td>31.37 (-12.47%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.30 (n/a)</td><td>170.68 (n/a)</td><td>185.00 (n/a)</td><td>131.00 (n/a)</td><td>35.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (+0.34%)</td><td>0.19 (+5.61%)</td><td>0.18 (+11.39%)</td><td>0.15 (-4.54%)</td><td>0.03 (+12.65%)</td><td>226.00 (+4.78%)</td><td>178.34 (-4.80%)</td><td>177.10 (-10.24%)</td><td>150.40 (-0.33%)</td><td>29.98 (+19.06%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.70 (n/a)</td><td>187.34 (n/a)</td><td>197.30 (n/a)</td><td>150.90 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (+6.07%)</td><td>0.21 (+9.53%)</td><td>0.20 (+13.10%)</td><td>0.18 (+8.87%)</td><td>0.03 (-4.74%)</td><td>177.90 (-8.11%)</td><td>158.92 (-9.01%)</td><td>167.00 (-11.59%)</td><td>136.90 (-5.72%)</td><td>18.94 (-19.17%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.60 (n/a)</td><td>174.66 (n/a)</td><td>188.90 (n/a)</td><td>145.20 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (-1.37%)</td><td>0.24 <b>(+30.69%)</b></td><td>0.25 <b>(+50.24%)</b></td><td>0.18 <b>(+65.41%)</b></td><td>0.04 <b>(-37.55%)</b></td><td>180.50 <b>(-39.55%)</b></td><td>142.78 <b>(-28.69%)</b></td><td>130.20 <b>(-33.47%)</b></td><td>120.00 (+1.44%)</td><td>26.02 <b>(-61.57%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>298.60 (n/a)</td><td>200.22 (n/a)</td><td>195.70 (n/a)</td><td>118.30 (n/a)</td><td>67.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (+2.87%)</td><td>0.21 (+16.10%)</td><td>0.23 <b>(+34.15%)</b></td><td>0.13 (-1.44%)</td><td>0.06 (+15.61%)</td><td>245.60 (+1.49%)</td><td>163.32 (-12.46%)</td><td>142.10 <b>(-25.45%)</b></td><td>123.00 (-2.77%)</td><td>50.96 (+15.07%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>242.00 (n/a)</td><td>186.56 (n/a)</td><td>190.60 (n/a)</td><td>126.50 (n/a)</td><td>44.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (+9.91%)</td><td>0.19 (+5.75%)</td><td>0.18 (-6.96%)</td><td>0.16 <b>(+49.06%)</b></td><td>0.03 <b>(-29.15%)</b></td><td>201.20 <b>(-32.91%)</b></td><td>171.48 (-9.61%)</td><td>179.90 (+7.47%)</td><td>134.50 (-9.00%)</td><td>25.17 <b>(-59.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>299.90 (n/a)</td><td>189.72 (n/a)</td><td>167.40 (n/a)</td><td>147.80 (n/a)</td><td>62.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (-13.97%)</td><td>0.21 (-0.43%)</td><td>0.21 (+15.28%)</td><td>0.16 (+3.55%)</td><td>0.04 <b>(-29.00%)</b></td><td>200.70 (-3.42%)</td><td>163.22 (-1.48%)</td><td>152.90 (-13.27%)</td><td>133.20 (+16.23%)</td><td>30.55 (-19.03%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>207.80 (n/a)</td><td>165.68 (n/a)</td><td>176.30 (n/a)</td><td>114.60 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (-8.37%)</td><td>0.20 (+14.29%)</td><td>0.20 <b>(+33.65%)</b></td><td>0.16 <b>(+24.16%)</b></td><td>0.03 <b>(-42.12%)</b></td><td>198.80 (-19.45%)</td><td>169.80 (-15.79%)</td><td>166.60 <b>(-25.19%)</b></td><td>138.90 (+9.11%)</td><td>24.96 <b>(-47.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>246.80 (n/a)</td><td>201.64 (n/a)</td><td>222.70 (n/a)</td><td>127.30 (n/a)</td><td>47.21 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (+12.37%)</td><td>0.19 (+2.32%)</td><td>0.16 (-14.53%)</td><td>0.14 (-4.13%)</td><td>0.06 <b>(+62.21%)</b></td><td>236.30 (+4.33%)</td><td>182.98 (+1.46%)</td><td>202.40 (+16.99%)</td><td>123.10 (-10.99%)</td><td>49.19 <b>(+48.14%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>226.50 (n/a)</td><td>180.34 (n/a)</td><td>173.00 (n/a)</td><td>138.30 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (-0.05%)</td><td>0.18 (+0.06%)</td><td>0.18 (+0.05%)</td><td>0.18 (+0.20%)</td><td>0.00 <b>(-52.50%)</b></td><td>47441.80 (-0.20%)</td><td>47383.56 (-0.06%)</td><td>47394.30 (-0.05%)</td><td>47317.70 (+0.05%)</td><td>45.41 <b>(-52.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47538.60 (n/a)</td><td>47411.48 (n/a)</td><td>47417.00 (n/a)</td><td>47294.30 (n/a)</td><td>95.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (+0.71%)</td><td>0.18 (+0.05%)</td><td>0.18 (-0.08%)</td><td>0.18 (-0.23%)</td><td>0.00 <b>(+632.06%)</b></td><td>47550.00 (+0.23%)</td><td>47386.10 (-0.05%)</td><td>47451.10 (+0.08%)</td><td>47037.00 (-0.70%)</td><td>200.15 <b>(+628.14%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47440.60 (n/a)</td><td>47409.20 (n/a)</td><td>47413.40 (n/a)</td><td>47369.00 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (+0.11%)</td><td>0.11 (+0.11%)</td><td>0.11 (+0.08%)</td><td>0.11 (+0.14%)</td><td>0.00 <b>(-27.04%)</b></td><td>374413.30 (-0.14%)</td><td>374341.64 (-0.11%)</td><td>374391.20 (-0.08%)</td><td>374180.20 (-0.11%)</td><td>96.68 <b>(-27.25%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374919.50 (n/a)</td><td>374743.28 (n/a)</td><td>374708.80 (n/a)</td><td>374591.70 (n/a)</td><td>132.90 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 <b>(+30.90%)</b></td><td>0.03 (+11.73%)</td><td>0.03 (+0.00%)</td><td>0.02 <b>(+42.26%)</b></td><td>0.01 (+11.31%)</td><td>237.70 <b>(-29.70%)</b></td><td>163.84 (-14.26%)</td><td>156.30 (+0.00%)</td><td>99.60 <b>(-23.56%)</b></td><td>49.56 <b>(-42.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>338.10 (n/a)</td><td>191.08 (n/a)</td><td>156.30 (n/a)</td><td>130.30 (n/a)</td><td>85.97 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-10.47%)</td><td>0.04 (+7.22%)</td><td>0.04 (+9.32%)</td><td>0.03 <b>(+24.14%)</b></td><td>0.01 <b>(-45.92%)</b></td><td>178.40 (-19.46%)</td><td>152.84 (-9.67%)</td><td>153.20 (-8.54%)</td><td>130.10 (+11.67%)</td><td>18.96 <b>(-50.50%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>169.20 (n/a)</td><td>167.50 (n/a)</td><td>116.50 (n/a)</td><td>38.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+2.72%)</td><td>0.03 (-7.33%)</td><td>0.02 (-4.75%)</td><td>0.02 <b>(-31.18%)</b></td><td>0.01 <b>(+58.42%)</b></td><td>254.10 <b>(+45.28%)</b></td><td>171.12 (+13.85%)</td><td>170.80 (+4.98%)</td><td>118.00 (-2.64%)</td><td>54.69 <b>(+121.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.90 (n/a)</td><td>150.30 (n/a)</td><td>162.70 (n/a)</td><td>121.20 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+12.23%)</td><td>0.03 (-4.81%)</td><td>0.03 (-2.86%)</td><td>0.02 (-17.57%)</td><td>0.01 <b>(+79.53%)</b></td><td>227.90 <b>(+21.29%)</b></td><td>164.40 (+8.69%)</td><td>150.00 (+2.88%)</td><td>119.60 (-10.88%)</td><td>41.92 <b>(+94.33%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>151.26 (n/a)</td><td>145.80 (n/a)</td><td>134.20 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (+4.59%)</td><td>0.03 (-12.58%)</td><td>0.02 <b>(-26.81%)</b></td><td>0.02 <b>(-31.18%)</b></td><td>0.01 <b>(+114.93%)</b></td><td>247.10 <b>(+45.27%)</b></td><td>170.02 <b>(+23.63%)</b></td><td>185.50 <b>(+36.60%)</b></td><td>110.20 (-4.42%)</td><td>57.03 <b>(+177.86%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.10 (n/a)</td><td>137.52 (n/a)</td><td>135.80 (n/a)</td><td>115.30 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (-5.59%)</td><td>0.03 (+11.58%)</td><td>0.04 <b>(+20.12%)</b></td><td>0.03 <b>(+56.45%)</b></td><td>0.01 <b>(-41.81%)</b></td><td>197.00 <b>(-36.08%)</b></td><td>154.46 (-17.11%)</td><td>141.10 (-16.80%)</td><td>132.20 (+5.93%)</td><td>28.32 <b>(-61.55%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>308.20 (n/a)</td><td>186.34 (n/a)</td><td>169.60 (n/a)</td><td>124.80 (n/a)</td><td>73.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+7.88%)</td><td>0.03 (-2.06%)</td><td>0.03 (-8.98%)</td><td>0.02 (-10.60%)</td><td>0.01 <b>(+102.80%)</b></td><td>190.20 (+11.88%)</td><td>154.28 (+5.31%)</td><td>162.40 (+9.88%)</td><td>118.40 (-7.36%)</td><td>33.95 <b>(+105.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.00 (n/a)</td><td>146.50 (n/a)</td><td>147.80 (n/a)</td><td>127.80 (n/a)</td><td>16.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-5.34%)</td><td>0.02 (-10.16%)</td><td>0.02 (-12.29%)</td><td>0.02 (-8.34%)</td><td>0.00 (+8.13%)</td><td>229.90 (+9.11%)</td><td>202.40 (+11.82%)</td><td>208.20 (+14.02%)</td><td>158.30 (+5.67%)</td><td>28.50 <b>(+24.32%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>181.00 (n/a)</td><td>182.60 (n/a)</td><td>149.80 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 <b>(-28.70%)</b></td><td>0.02 <b>(-24.36%)</b></td><td>0.02 <b>(-31.22%)</b></td><td>0.02 (-16.37%)</td><td>0.00 <b>(-62.51%)</b></td><td>215.90 (+19.61%)</td><td>193.64 <b>(+29.68%)</b></td><td>193.10 <b>(+45.41%)</b></td><td>174.00 <b>(+40.32%)</b></td><td>16.65 <b>(-38.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.50 (n/a)</td><td>149.32 (n/a)</td><td>132.80 (n/a)</td><td>124.00 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 <b>(-20.43%)</b></td><td>0.03 (-14.52%)</td><td>0.02 <b>(-25.02%)</b></td><td>0.02 (-6.11%)</td><td>0.01 (-16.88%)</td><td>253.60 (+6.51%)</td><td>187.18 (+15.99%)</td><td>203.00 <b>(+33.38%)</b></td><td>133.00 <b>(+25.71%)</b></td><td>52.32 (+3.52%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>161.38 (n/a)</td><td>152.20 (n/a)</td><td>105.80 (n/a)</td><td>50.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-14.13%)</td><td>0.02 (-11.40%)</td><td>0.02 (+10.41%)</td><td>0.01 <b>(-36.40%)</b></td><td>0.01 <b>(+44.13%)</b></td><td>323.30 <b>(+57.25%)</b></td><td>212.62 <b>(+20.55%)</b></td><td>167.10 (-9.43%)</td><td>151.80 (+16.41%)</td><td>75.73 <b>(+169.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>176.38 (n/a)</td><td>184.50 (n/a)</td><td>130.40 (n/a)</td><td>28.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (-7.08%)</td><td>0.02 (-9.89%)</td><td>0.02 (-14.32%)</td><td>0.02 <b>(-22.38%)</b></td><td>0.01 (+19.30%)</td><td>286.50 <b>(+28.88%)</b></td><td>202.20 (+14.81%)</td><td>213.90 (+16.69%)</td><td>135.10 (+7.65%)</td><td>59.51 <b>(+65.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>176.12 (n/a)</td><td>183.30 (n/a)</td><td>125.50 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 (+2.25%)</td><td>0.02 (-2.88%)</td><td>0.02 (-13.97%)</td><td>0.02 <b>(+28.07%)</b></td><td>0.00 <b>(-29.05%)</b></td><td>206.90 <b>(-21.92%)</b></td><td>182.52 (-0.43%)</td><td>195.50 (+16.30%)</td><td>137.40 (-2.21%)</td><td>28.14 <b>(-45.50%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>265.00 (n/a)</td><td>183.30 (n/a)</td><td>168.10 (n/a)</td><td>140.50 (n/a)</td><td>51.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.03 <b>(-38.32%)</b></td><td>0.02 (-11.90%)</td><td>0.02 (-4.36%)</td><td>0.02 <b>(+30.53%)</b></td><td>0.00 <b>(-76.56%)</b></td><td>223.80 <b>(-23.41%)</b></td><td>208.70 (+2.97%)</td><td>214.20 (+4.54%)</td><td>173.70 <b>(+62.18%)</b></td><td>20.13 <b>(-69.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>292.20 (n/a)</td><td>202.68 (n/a)</td><td>204.90 (n/a)</td><td>107.10 (n/a)</td><td>65.69 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.02 (-10.38%)</td><td>0.02 (-0.85%)</td><td>0.02 (+1.93%)</td><td>0.02 <b>(+29.70%)</b></td><td>0.00 <b>(-48.06%)</b></td><td>255.80 <b>(-22.88%)</b></td><td>228.44 (-2.75%)</td><td>229.00 (-1.89%)</td><td>191.90 (+11.57%)</td><td>26.86 <b>(-55.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>331.70 (n/a)</td><td>234.90 (n/a)</td><td>233.40 (n/a)</td><td>172.00 (n/a)</td><td>60.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-17.33%)</td><td>0.05 (+5.32%)</td><td>0.05 <b>(+24.99%)</b></td><td>0.04 (+7.24%)</td><td>0.00 <b>(-54.42%)</b></td><td>215.00 (-6.76%)</td><td>182.48 (-8.01%)</td><td>175.00 (-19.98%)</td><td>164.30 <b>(+20.99%)</b></td><td>20.85 <b>(-49.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>198.36 (n/a)</td><td>218.70 (n/a)</td><td>135.80 (n/a)</td><td>41.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 <b>(-22.77%)</b></td><td>0.07 (-8.45%)</td><td>0.07 (-11.93%)</td><td>0.06 <b>(+31.71%)</b></td><td>0.00 <b>(-81.18%)</b></td><td>199.90 <b>(-24.05%)</b></td><td>189.32 (+4.21%)</td><td>187.20 (+13.52%)</td><td>177.50 <b>(+29.47%)</b></td><td>8.75 <b>(-82.08%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>263.20 (n/a)</td><td>181.68 (n/a)</td><td>164.90 (n/a)</td><td>137.10 (n/a)</td><td>48.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (+4.32%)</td><td>0.05 (-5.68%)</td><td>0.04 (-15.88%)</td><td>0.04 (-10.54%)</td><td>0.01 <b>(+25.34%)</b></td><td>219.80 (+11.74%)</td><td>180.42 (+7.30%)</td><td>190.00 (+18.90%)</td><td>128.90 (-4.16%)</td><td>34.57 <b>(+26.74%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>168.14 (n/a)</td><td>159.80 (n/a)</td><td>134.50 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (-12.99%)</td><td>0.06 (-1.02%)</td><td>0.06 (+2.06%)</td><td>0.05 (+16.88%)</td><td>0.01 <b>(-45.67%)</b></td><td>208.70 (-14.43%)</td><td>184.78 (-1.35%)</td><td>175.10 (-2.01%)</td><td>160.70 (+14.95%)</td><td>21.25 <b>(-45.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>243.90 (n/a)</td><td>187.30 (n/a)</td><td>178.70 (n/a)</td><td>139.80 (n/a)</td><td>39.08 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-19.70%)</td><td>0.04 <b>(-24.03%)</b></td><td>0.04 (-18.37%)</td><td>0.03 <b>(-44.34%)</b></td><td>0.01 <b>(+128.56%)</b></td><td>307.60 <b>(+79.67%)</b></td><td>212.88 <b>(+36.53%)</b></td><td>187.10 <b>(+22.53%)</b></td><td>181.10 <b>(+24.55%)</b></td><td>53.81 <b>(+418.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>171.20 (n/a)</td><td>155.92 (n/a)</td><td>152.70 (n/a)</td><td>145.40 (n/a)</td><td>10.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 (-14.78%)</td><td>0.06 (-8.43%)</td><td>0.06 (-0.33%)</td><td>0.04 (-4.38%)</td><td>0.01 <b>(-22.92%)</b></td><td>227.90 (+4.59%)</td><td>183.92 (+8.12%)</td><td>171.80 (+0.29%)</td><td>136.70 (+17.34%)</td><td>36.79 (-1.28%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>217.90 (n/a)</td><td>170.10 (n/a)</td><td>171.30 (n/a)</td><td>116.50 (n/a)</td><td>37.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 (+5.68%)</td><td>0.05 (-4.05%)</td><td>0.05 (+2.40%)</td><td>0.03 <b>(-24.63%)</b></td><td>0.01 <b>(+64.97%)</b></td><td>280.20 <b>(+32.67%)</b></td><td>189.50 (+9.07%)</td><td>166.00 (-2.35%)</td><td>138.90 (-5.38%)</td><td>57.72 <b>(+111.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>173.74 (n/a)</td><td>170.00 (n/a)</td><td>146.80 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.06 <b>(+32.15%)</b></td><td>0.05 (+13.87%)</td><td>0.05 (+6.49%)</td><td>0.04 (+2.19%)</td><td>0.01 <b>(+142.51%)</b></td><td>221.00 (-2.13%)</td><td>183.74 (-10.75%)</td><td>185.10 (-6.09%)</td><td>142.30 <b>(-24.35%)</b></td><td>29.08 <b>(+75.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.80 (n/a)</td><td>205.86 (n/a)</td><td>197.10 (n/a)</td><td>188.10 (n/a)</td><td>16.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-10.24%)</td><td>0.05 (-11.48%)</td><td>0.05 (-11.63%)</td><td>0.05 (-9.12%)</td><td>0.00 (-14.07%)</td><td>181.10 (+10.02%)</td><td>169.56 (+12.95%)</td><td>166.00 (+13.16%)</td><td>159.10 (+11.41%)</td><td>8.96 (+4.84%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>164.60 (n/a)</td><td>150.12 (n/a)</td><td>146.70 (n/a)</td><td>142.80 (n/a)</td><td>8.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.08 (+10.08%)</td><td>0.06 (+1.19%)</td><td>0.05 (-8.13%)</td><td>0.04 (-7.02%)</td><td>0.02 <b>(+45.06%)</b></td><td>222.20 (+7.55%)</td><td>176.96 (+1.78%)</td><td>196.90 (+8.84%)</td><td>114.40 (-9.21%)</td><td>43.38 <b>(+45.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>173.86 (n/a)</td><td>180.90 (n/a)</td><td>126.00 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.07 <b>(+27.77%)</b></td><td>0.05 (+18.04%)</td><td>0.06 (+19.92%)</td><td>0.03 <b>(-23.00%)</b></td><td>0.01 <b>(+170.79%)</b></td><td>270.90 <b>(+29.87%)</b></td><td>167.12 (-9.10%)</td><td>143.50 (-16.62%)</td><td>124.80 <b>(-21.76%)</b></td><td>60.96 <b>(+168.15%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>183.86 (n/a)</td><td>172.10 (n/a)</td><td>159.50 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 (-7.25%)</td><td>0.04 (-4.57%)</td><td>0.04 (-13.47%)</td><td>0.03 <b>(+23.55%)</b></td><td>0.01 <b>(-32.84%)</b></td><td>299.50 (-19.05%)</td><td>233.16 (+0.37%)</td><td>232.70 (+15.54%)</td><td>186.20 (+7.82%)</td><td>43.62 <b>(-44.71%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>370.00 (n/a)</td><td>232.30 (n/a)</td><td>201.40 (n/a)</td><td>172.70 (n/a)</td><td>78.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.05 <b>(-30.21%)</b></td><td>0.04 <b>(-21.01%)</b></td><td>0.04 <b>(-20.43%)</b></td><td>0.03 <b>(-29.12%)</b></td><td>0.01 <b>(-30.88%)</b></td><td>266.60 <b>(+41.13%)</b></td><td>199.96 <b>(+26.37%)</b></td><td>199.90 <b>(+25.64%)</b></td><td>163.00 <b>(+43.23%)</b></td><td>41.89 <b>(+37.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>158.24 (n/a)</td><td>159.10 (n/a)</td><td>113.80 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 <b>(-23.86%)</b></td><td>0.04 <b>(-20.59%)</b></td><td>0.04 (-17.78%)</td><td>0.03 <b>(-28.20%)</b></td><td>0.01 (-13.58%)</td><td>292.20 <b>(+39.28%)</b></td><td>227.38 <b>(+26.53%)</b></td><td>213.40 <b>(+21.60%)</b></td><td>203.60 <b>(+31.35%)</b></td><td>36.75 <b>(+61.45%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>179.70 (n/a)</td><td>175.50 (n/a)</td><td>155.00 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.04 (-5.43%)</td><td>0.04 (+1.82%)</td><td>0.04 (+3.29%)</td><td>0.04 (+10.29%)</td><td>0.00 <b>(-44.10%)</b></td><td>234.00 (-9.34%)</td><td>220.62 (-2.31%)</td><td>214.00 (-3.17%)</td><td>210.20 (+5.73%)</td><td>11.97 <b>(-46.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>258.10 (n/a)</td><td>225.84 (n/a)</td><td>221.00 (n/a)</td><td>198.80 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 <b>(+26.49%)</b></td><td>0.10 (+8.18%)</td><td>0.10 (+8.68%)</td><td>0.08 (-4.50%)</td><td>0.03 <b>(+102.30%)</b></td><td>215.60 (+4.71%)</td><td>170.14 (-4.57%)</td><td>168.30 (-8.03%)</td><td>113.60 <b>(-20.95%)</b></td><td>37.93 <b>(+65.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>178.28 (n/a)</td><td>183.00 (n/a)</td><td>143.70 (n/a)</td><td>22.91 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (-16.87%)</td><td>0.13 <b>(-22.27%)</b></td><td>0.12 <b>(-29.10%)</b></td><td>0.11 (-6.08%)</td><td>0.02 <b>(-29.41%)</b></td><td>214.40 (+6.45%)</td><td>186.14 <b>(+26.97%)</b></td><td>197.20 <b>(+40.96%)</b></td><td>142.10 <b>(+20.32%)</b></td><td>27.51 (-14.94%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>146.60 (n/a)</td><td>139.90 (n/a)</td><td>118.10 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (+6.32%)</td><td>0.10 (+1.92%)</td><td>0.10 (+5.50%)</td><td>0.08 (-11.44%)</td><td>0.01 <b>(+72.70%)</b></td><td>214.10 (+12.92%)</td><td>172.78 (-0.77%)</td><td>168.00 (-5.19%)</td><td>145.40 (-5.95%)</td><td>25.80 <b>(+87.36%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>174.12 (n/a)</td><td>177.20 (n/a)</td><td>154.60 (n/a)</td><td>13.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (-9.27%)</td><td>0.10 <b>(-25.36%)</b></td><td>0.10 <b>(-33.81%)</b></td><td>0.07 <b>(-25.02%)</b></td><td>0.03 (-8.46%)</td><td>288.60 <b>(+33.36%)</b></td><td>211.38 <b>(+35.29%)</b></td><td>215.30 <b>(+51.09%)</b></td><td>131.30 (+10.24%)</td><td>56.29 <b>(+32.65%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.40 (n/a)</td><td>156.24 (n/a)</td><td>142.50 (n/a)</td><td>119.10 (n/a)</td><td>42.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-5.98%)</td><td>0.09 (-12.68%)</td><td>0.08 (-11.81%)</td><td>0.07 (-10.87%)</td><td>0.01 (-12.64%)</td><td>223.00 (+12.23%)</td><td>194.98 (+14.33%)</td><td>201.70 (+13.38%)</td><td>150.10 (+6.38%)</td><td>29.48 (+6.18%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.70 (n/a)</td><td>170.54 (n/a)</td><td>177.90 (n/a)</td><td>141.10 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (-8.98%)</td><td>0.12 (-3.47%)</td><td>0.11 (-11.69%)</td><td>0.10 (-1.58%)</td><td>0.02 (-8.31%)</td><td>210.50 (+1.64%)</td><td>174.08 (+3.31%)</td><td>182.80 (+13.26%)</td><td>137.80 (+9.89%)</td><td>32.78 (-1.63%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>207.10 (n/a)</td><td>168.50 (n/a)</td><td>161.40 (n/a)</td><td>125.40 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (-12.01%)</td><td>0.09 (-0.65%)</td><td>0.08 (+4.42%)</td><td>0.08 (+14.51%)</td><td>0.01 <b>(-53.79%)</b></td><td>202.00 (-12.67%)</td><td>184.70 (-2.10%)</td><td>194.80 (-4.23%)</td><td>162.40 (+13.65%)</td><td>17.92 <b>(-53.42%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.30 (n/a)</td><td>188.66 (n/a)</td><td>203.40 (n/a)</td><td>142.90 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-6.09%)</td><td>0.10 (-6.23%)</td><td>0.09 (-9.10%)</td><td>0.09 (-5.93%)</td><td>0.01 (-12.64%)</td><td>216.50 (+6.28%)</td><td>194.72 (+6.52%)</td><td>199.30 (+9.99%)</td><td>169.60 (+6.47%)</td><td>17.42 (-2.38%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>182.80 (n/a)</td><td>181.20 (n/a)</td><td>159.30 (n/a)</td><td>17.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 <b>(-24.25%)</b></td><td>0.10 (-13.08%)</td><td>0.10 <b>(-21.19%)</b></td><td>0.09 (+12.58%)</td><td>0.00 <b>(-79.28%)</b></td><td>177.80 (-11.19%)</td><td>164.16 (+11.05%)</td><td>162.80 <b>(+26.89%)</b></td><td>157.40 <b>(+32.05%)</b></td><td>8.21 <b>(-75.71%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.20 (n/a)</td><td>147.82 (n/a)</td><td>128.30 (n/a)</td><td>119.20 (n/a)</td><td>33.78 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 <b>(-29.18%)</b></td><td>0.10 (-10.11%)</td><td>0.09 (-0.36%)</td><td>0.09 (+5.12%)</td><td>0.01 <b>(-68.34%)</b></td><td>213.30 (-4.86%)</td><td>192.88 (+5.88%)</td><td>200.90 (+0.35%)</td><td>169.00 <b>(+41.19%)</b></td><td>18.81 <b>(-58.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>224.20 (n/a)</td><td>182.16 (n/a)</td><td>200.20 (n/a)</td><td>119.70 (n/a)</td><td>44.94 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (-5.34%)</td><td>0.09 (-5.76%)</td><td>0.09 (+6.55%)</td><td>0.07 (-6.46%)</td><td>0.02 <b>(-32.35%)</b></td><td>220.80 (+6.87%)</td><td>180.38 (+3.77%)</td><td>184.20 (-6.16%)</td><td>137.60 (+5.60%)</td><td>29.78 <b>(-24.17%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>173.82 (n/a)</td><td>196.30 (n/a)</td><td>130.30 (n/a)</td><td>39.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 <b>(-24.22%)</b></td><td>0.08 (-16.15%)</td><td>0.08 (-10.71%)</td><td>0.06 (-19.24%)</td><td>0.02 <b>(-29.92%)</b></td><td>312.10 <b>(+23.80%)</b></td><td>219.30 (+17.65%)</td><td>210.80 (+12.01%)</td><td>150.60 <b>(+31.99%)</b></td><td>62.47 (+16.17%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>252.10 (n/a)</td><td>186.40 (n/a)</td><td>188.20 (n/a)</td><td>114.10 (n/a)</td><td>53.78 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.10 (-8.52%)</td><td>0.09 (-6.27%)</td><td>0.09 (-6.53%)</td><td>0.08 (+3.21%)</td><td>0.01 <b>(-36.78%)</b></td><td>209.40 (-3.10%)</td><td>186.02 (+5.86%)</td><td>178.40 (+7.02%)</td><td>169.90 (+9.33%)</td><td>16.11 <b>(-33.68%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>175.72 (n/a)</td><td>166.70 (n/a)</td><td>155.40 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.12 (-6.03%)</td><td>0.09 (+1.72%)</td><td>0.08 (-1.22%)</td><td>0.08 (+2.91%)</td><td>0.02 (-9.17%)</td><td>216.90 (-2.87%)</td><td>191.86 (-2.01%)</td><td>212.50 (+1.24%)</td><td>150.30 (+6.37%)</td><td>32.34 (-2.73%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>223.30 (n/a)</td><td>195.80 (n/a)</td><td>209.90 (n/a)</td><td>141.30 (n/a)</td><td>33.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.09 (-2.10%)</td><td>0.08 (+6.20%)</td><td>0.08 (+4.51%)</td><td>0.07 (+8.81%)</td><td>0.01 <b>(-24.86%)</b></td><td>243.80 (-8.10%)</td><td>208.02 (-6.76%)</td><td>210.70 (-4.31%)</td><td>178.00 (+2.12%)</td><td>24.88 <b>(-29.34%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>265.30 (n/a)</td><td>223.10 (n/a)</td><td>220.20 (n/a)</td><td>174.30 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.28 <b>(+20.67%)</b></td><td>0.21 (+9.03%)</td><td>0.19 (-0.07%)</td><td>0.16 (+3.67%)</td><td>0.05 <b>(+70.83%)</b></td><td>205.10 (-3.53%)</td><td>164.88 (-5.56%)</td><td>173.40 (+0.06%)</td><td>115.20 (-17.12%)</td><td>39.78 <b>(+38.10%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.60 (n/a)</td><td>174.58 (n/a)</td><td>173.30 (n/a)</td><td>139.00 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (-3.98%)</td><td>0.20 (-8.05%)</td><td>0.20 (-14.90%)</td><td>0.16 (-11.74%)</td><td>0.04 (-3.62%)</td><td>202.20 (+13.28%)</td><td>164.00 (+8.85%)</td><td>164.50 (+17.50%)</td><td>127.80 (+4.16%)</td><td>27.76 (+9.11%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>178.50 (n/a)</td><td>150.66 (n/a)</td><td>140.00 (n/a)</td><td>122.70 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 (+0.96%)</td><td>0.24 (-9.34%)</td><td>0.21 (-19.84%)</td><td>0.19 (-0.42%)</td><td>0.05 (+11.92%)</td><td>218.50 (+0.41%)</td><td>176.84 (+11.02%)</td><td>193.60 <b>(+24.74%)</b></td><td>131.00 (-0.98%)</td><td>37.19 (+8.09%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>217.60 (n/a)</td><td>159.28 (n/a)</td><td>155.20 (n/a)</td><td>132.30 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (-16.34%)</td><td>0.18 (-8.67%)</td><td>0.17 (-15.80%)</td><td>0.14 (-4.56%)</td><td>0.03 <b>(-36.38%)</b></td><td>235.40 (+4.76%)</td><td>186.84 (+7.29%)</td><td>187.60 (+18.81%)</td><td>152.10 (+19.48%)</td><td>31.14 <b>(-20.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.70 (n/a)</td><td>174.14 (n/a)</td><td>157.90 (n/a)</td><td>127.30 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 <b>(-35.65%)</b></td><td>0.20 (-12.20%)</td><td>0.20 (-10.83%)</td><td>0.18 <b>(+29.21%)</b></td><td>0.01 <b>(-83.22%)</b></td><td>221.80 <b>(-22.61%)</b></td><td>208.76 (+5.62%)</td><td>208.10 (+12.12%)</td><td>191.60 <b>(+55.39%)</b></td><td>12.44 <b>(-79.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>286.60 (n/a)</td><td>197.66 (n/a)</td><td>185.60 (n/a)</td><td>123.30 (n/a)</td><td>61.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 <b>(+46.51%)</b></td><td>0.21 (+17.34%)</td><td>0.20 (+1.70%)</td><td>0.16 (+19.77%)</td><td>0.07 <b>(+74.38%)</b></td><td>201.60 (-16.52%)</td><td>164.70 (-12.66%)</td><td>167.00 (-1.65%)</td><td>101.60 <b>(-31.77%)</b></td><td>40.67 (-2.37%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>241.50 (n/a)</td><td>188.58 (n/a)</td><td>169.80 (n/a)</td><td>148.90 (n/a)</td><td>41.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (-15.84%)</td><td>0.19 (-6.77%)</td><td>0.20 (-11.75%)</td><td>0.15 (-1.11%)</td><td>0.02 <b>(-45.97%)</b></td><td>239.10 (+1.14%)</td><td>195.78 (+5.24%)</td><td>185.70 (+13.30%)</td><td>182.50 (+18.82%)</td><td>24.35 <b>(-34.44%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>236.40 (n/a)</td><td>186.04 (n/a)</td><td>163.90 (n/a)</td><td>153.60 (n/a)</td><td>37.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 (+3.54%)</td><td>0.22 (+7.90%)</td><td>0.22 (+3.75%)</td><td>0.18 <b>(+26.56%)</b></td><td>0.04 (-17.44%)</td><td>178.10 <b>(-21.02%)</b></td><td>149.82 (-9.46%)</td><td>150.30 (-3.59%)</td><td>112.00 (-3.45%)</td><td>25.48 <b>(-38.07%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.50 (n/a)</td><td>165.48 (n/a)</td><td>155.90 (n/a)</td><td>116.00 (n/a)</td><td>41.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.37 <b>(+42.39%)</b></td><td>0.22 (+3.34%)</td><td>0.19 (-7.17%)</td><td>0.17 (+1.13%)</td><td>0.09 <b>(+120.68%)</b></td><td>222.60 (-1.11%)</td><td>186.06 (+2.68%)</td><td>197.10 (+7.70%)</td><td>100.50 <b>(-29.77%)</b></td><td>49.46 <b>(+48.57%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>225.10 (n/a)</td><td>181.20 (n/a)</td><td>183.00 (n/a)</td><td>143.10 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (-12.95%)</td><td>0.19 (-3.90%)</td><td>0.19 (-1.21%)</td><td>0.17 <b>(+29.04%)</b></td><td>0.02 <b>(-57.54%)</b></td><td>196.50 <b>(-22.52%)</b></td><td>173.26 (-0.63%)</td><td>174.80 (+1.27%)</td><td>150.80 (+14.94%)</td><td>18.66 <b>(-61.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>253.60 (n/a)</td><td>174.36 (n/a)</td><td>172.60 (n/a)</td><td>131.20 (n/a)</td><td>49.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (+3.52%)</td><td>0.18 (-3.52%)</td><td>0.17 (-2.32%)</td><td>0.15 (-5.63%)</td><td>0.03 (+3.76%)</td><td>232.90 (+6.01%)</td><td>200.04 (+3.84%)</td><td>209.60 (+2.34%)</td><td>157.50 (-3.37%)</td><td>28.97 (+6.98%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>219.70 (n/a)</td><td>192.64 (n/a)</td><td>204.80 (n/a)</td><td>163.00 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (-11.00%)</td><td>0.18 (-7.80%)</td><td>0.18 (-16.22%)</td><td>0.15 (+18.66%)</td><td>0.03 <b>(-47.91%)</b></td><td>217.90 (-15.74%)</td><td>189.36 (+3.70%)</td><td>187.10 (+19.32%)</td><td>152.40 (+12.39%)</td><td>26.15 <b>(-50.49%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>258.60 (n/a)</td><td>182.60 (n/a)</td><td>156.80 (n/a)</td><td>135.60 (n/a)</td><td>52.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.23 (-10.45%)</td><td>0.17 (-13.26%)</td><td>0.16 (-9.31%)</td><td>0.13 <b>(-23.33%)</b></td><td>0.04 (+1.56%)</td><td>274.70 <b>(+30.44%)</b></td><td>207.32 (+16.76%)</td><td>211.30 (+10.28%)</td><td>148.50 (+11.65%)</td><td>45.62 <b>(+48.96%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>210.60 (n/a)</td><td>177.56 (n/a)</td><td>191.60 (n/a)</td><td>133.00 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.18 (-7.58%)</td><td>0.16 (-3.38%)</td><td>0.17 (+6.00%)</td><td>0.12 (-12.32%)</td><td>0.02 (+7.26%)</td><td>267.50 (+14.07%)</td><td>205.78 (+4.17%)</td><td>193.60 (-5.65%)</td><td>179.70 (+8.19%)</td><td>36.43 <b>(+34.48%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>234.50 (n/a)</td><td>197.54 (n/a)</td><td>205.20 (n/a)</td><td>166.10 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (-9.03%)</td><td>0.10 (-10.76%)</td><td>0.10 (-3.24%)</td><td>0.06 <b>(-34.57%)</b></td><td>0.03 (+11.19%)</td><td>351.60 <b>(+52.87%)</b></td><td>219.24 (+16.69%)</td><td>196.90 (+3.36%)</td><td>152.20 (+9.89%)</td><td>77.07 <b>(+96.51%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>230.00 (n/a)</td><td>187.88 (n/a)</td><td>190.50 (n/a)</td><td>138.50 (n/a)</td><td>39.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (+9.78%)</td><td>0.14 (+15.16%)</td><td>0.14 <b>(+25.79%)</b></td><td>0.11 (+15.96%)</td><td>0.02 (-6.44%)</td><td>187.70 (-13.74%)</td><td>151.92 (-14.02%)</td><td>146.10 <b>(-20.51%)</b></td><td>124.70 (-8.91%)</td><td>26.38 <b>(-25.11%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>217.60 (n/a)</td><td>176.70 (n/a)</td><td>183.80 (n/a)</td><td>136.90 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (+18.99%)</td><td>0.13 (+1.79%)</td><td>0.11 (-10.57%)</td><td>0.10 (-6.66%)</td><td>0.03 <b>(+117.98%)</b></td><td>206.90 (+7.15%)</td><td>170.06 (+1.94%)</td><td>181.20 (+11.85%)</td><td>123.20 (-15.96%)</td><td>40.00 <b>(+98.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>166.82 (n/a)</td><td>162.00 (n/a)</td><td>146.60 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (-4.02%)</td><td>0.12 (-8.92%)</td><td>0.12 (-13.41%)</td><td>0.10 (+0.47%)</td><td>0.03 (+3.22%)</td><td>212.00 (-0.47%)</td><td>173.82 (+10.35%)</td><td>175.90 (+15.50%)</td><td>118.70 (+4.21%)</td><td>38.80 (+7.68%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>213.00 (n/a)</td><td>157.52 (n/a)</td><td>152.30 (n/a)</td><td>113.90 (n/a)</td><td>36.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (+0.22%)</td><td>0.12 (+2.35%)</td><td>0.12 (-3.22%)</td><td>0.10 (+12.18%)</td><td>0.01 <b>(-22.90%)</b></td><td>195.70 (-10.88%)</td><td>174.54 (-3.05%)</td><td>174.40 (+3.32%)</td><td>156.60 (-0.25%)</td><td>18.07 <b>(-31.97%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>180.04 (n/a)</td><td>168.80 (n/a)</td><td>157.00 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (-8.94%)</td><td>0.14 (+7.12%)</td><td>0.14 <b>(+20.07%)</b></td><td>0.11 (+9.86%)</td><td>0.02 <b>(-33.83%)</b></td><td>185.90 (-8.96%)</td><td>151.84 (-8.49%)</td><td>144.40 (-16.72%)</td><td>126.50 (+9.81%)</td><td>22.87 <b>(-30.78%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>204.20 (n/a)</td><td>165.92 (n/a)</td><td>173.40 (n/a)</td><td>115.20 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 <b>(+30.46%)</b></td><td>0.13 <b>(+22.84%)</b></td><td>0.12 <b>(+25.60%)</b></td><td>0.11 (+14.98%)</td><td>0.01 <b>(+81.83%)</b></td><td>193.10 (-13.02%)</td><td>164.82 (-18.12%)</td><td>164.10 <b>(-20.38%)</b></td><td>140.50 <b>(-23.35%)</b></td><td>19.07 <b>(+22.65%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>201.30 (n/a)</td><td>206.10 (n/a)</td><td>183.30 (n/a)</td><td>15.55 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 <b>(+34.47%)</b></td><td>0.14 (+19.42%)</td><td>0.13 (+9.43%)</td><td>0.12 <b>(+43.12%)</b></td><td>0.03 <b>(+24.41%)</b></td><td>173.90 <b>(-30.13%)</b></td><td>155.54 (-16.85%)</td><td>163.20 (-8.62%)</td><td>110.50 <b>(-25.64%)</b></td><td>25.88 <b>(-36.48%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>248.90 (n/a)</td><td>187.06 (n/a)</td><td>178.60 (n/a)</td><td>148.60 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 (-2.92%)</td><td>0.17 <b>(+28.06%)</b></td><td>0.18 <b>(+33.68%)</b></td><td>0.15 <b>(+99.64%)</b></td><td>0.02 <b>(-56.54%)</b></td><td>166.50 <b>(-49.92%)</b></td><td>143.34 <b>(-28.58%)</b></td><td>134.20 <b>(-25.20%)</b></td><td>128.90 (+2.96%)</td><td>16.48 <b>(-78.86%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>332.50 (n/a)</td><td>200.70 (n/a)</td><td>179.40 (n/a)</td><td>125.20 (n/a)</td><td>77.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (+18.52%)</td><td>0.16 (+11.67%)</td><td>0.16 (+5.09%)</td><td>0.13 (+13.92%)</td><td>0.03 <b>(+23.90%)</b></td><td>190.10 (-12.19%)</td><td>152.56 (-10.22%)</td><td>153.50 (-4.84%)</td><td>123.60 (-15.63%)</td><td>26.02 (-8.84%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>169.92 (n/a)</td><td>161.30 (n/a)</td><td>146.50 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (-1.72%)</td><td>0.16 (+5.27%)</td><td>0.15 (-3.37%)</td><td>0.12 <b>(+72.87%)</b></td><td>0.04 <b>(-34.36%)</b></td><td>209.90 <b>(-42.14%)</b></td><td>164.48 (-15.10%)</td><td>168.50 (+3.50%)</td><td>121.20 (+1.76%)</td><td>36.37 <b>(-63.12%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>362.80 (n/a)</td><td>193.74 (n/a)</td><td>162.80 (n/a)</td><td>119.10 (n/a)</td><td>98.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (+2.14%)</td><td>0.16 (+13.29%)</td><td>0.17 <b>(+29.28%)</b></td><td>0.11 (+7.96%)</td><td>0.04 (-2.64%)</td><td>227.80 (-7.40%)</td><td>161.56 (-12.40%)</td><td>143.70 <b>(-22.66%)</b></td><td>116.80 (-2.10%)</td><td>45.01 (-10.18%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>246.00 (n/a)</td><td>184.42 (n/a)</td><td>185.80 (n/a)</td><td>119.30 (n/a)</td><td>50.12 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.20 (-1.64%)</td><td>0.15 (-1.63%)</td><td>0.14 (-1.07%)</td><td>0.12 (+6.93%)</td><td>0.03 (-6.39%)</td><td>197.80 (-6.48%)</td><td>170.10 (+1.19%)</td><td>170.40 (+1.07%)</td><td>125.50 (+1.70%)</td><td>29.26 (-9.63%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.50 (n/a)</td><td>168.10 (n/a)</td><td>168.60 (n/a)</td><td>123.40 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (+16.07%)</td><td>0.16 (+0.97%)</td><td>0.16 (-9.77%)</td><td>0.11 (+8.68%)</td><td>0.05 <b>(+24.34%)</b></td><td>224.70 (-7.99%)</td><td>160.54 (-0.09%)</td><td>158.10 (+10.87%)</td><td>110.70 (-13.85%)</td><td>45.37 (-5.18%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>244.20 (n/a)</td><td>160.68 (n/a)</td><td>142.60 (n/a)</td><td>128.50 (n/a)</td><td>47.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.17 (+5.11%)</td><td>0.15 (+12.49%)</td><td>0.15 <b>(+27.73%)</b></td><td>0.11 (+7.56%)</td><td>0.03 (-4.40%)</td><td>232.80 (-7.03%)</td><td>173.34 (-11.54%)</td><td>161.60 <b>(-21.74%)</b></td><td>141.40 (-4.85%)</td><td>35.19 (-11.27%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>250.40 (n/a)</td><td>195.96 (n/a)</td><td>206.50 (n/a)</td><td>148.60 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.19 <b>(+23.69%)</b></td><td>0.15 (+11.42%)</td><td>0.15 (+1.43%)</td><td>0.11 (+11.89%)</td><td>0.03 (+18.01%)</td><td>222.20 (-10.62%)</td><td>171.56 (-10.17%)</td><td>163.20 (-1.39%)</td><td>127.30 (-19.17%)</td><td>37.58 (-12.29%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>248.60 (n/a)</td><td>190.98 (n/a)</td><td>165.50 (n/a)</td><td>157.50 (n/a)</td><td>42.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (+17.42%)</td><td>0.13 <b>(+28.19%)</b></td><td>0.12 <b>(+26.91%)</b></td><td>0.10 <b>(+54.26%)</b></td><td>0.01 <b>(-31.18%)</b></td><td>180.10 <b>(-35.17%)</b></td><td>149.14 <b>(-24.50%)</b></td><td>148.70 <b>(-21.20%)</b></td><td>129.20 (-14.83%)</td><td>19.13 <b>(-61.66%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>277.80 (n/a)</td><td>197.54 (n/a)</td><td>188.70 (n/a)</td><td>151.70 (n/a)</td><td>49.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 (+19.41%)</td><td>0.12 (+8.50%)</td><td>0.11 (-9.26%)</td><td>0.09 (+5.30%)</td><td>0.03 <b>(+25.18%)</b></td><td>216.40 (-5.05%)</td><td>161.78 (-7.15%)</td><td>167.30 (+10.21%)</td><td>120.10 (-16.25%)</td><td>36.70 (-0.27%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>227.90 (n/a)</td><td>174.24 (n/a)</td><td>151.80 (n/a)</td><td>143.40 (n/a)</td><td>36.79 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (-1.55%)</td><td>0.10 (-13.81%)</td><td>0.10 (-18.18%)</td><td>0.07 <b>(-30.63%)</b></td><td>0.03 <b>(+32.41%)</b></td><td>283.30 <b>(+44.17%)</b></td><td>191.24 <b>(+20.85%)</b></td><td>178.30 <b>(+22.21%)</b></td><td>130.30 (+1.56%)</td><td>58.79 <b>(+94.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>158.24 (n/a)</td><td>145.90 (n/a)</td><td>128.30 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.16 (+10.62%)</td><td>0.13 (-0.05%)</td><td>0.12 (-5.33%)</td><td>0.10 (-5.46%)</td><td>0.03 <b>(+86.08%)</b></td><td>183.80 (+5.75%)</td><td>151.10 (+2.27%)</td><td>152.80 (+5.67%)</td><td>115.60 (-9.62%)</td><td>29.42 <b>(+76.86%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>147.74 (n/a)</td><td>144.60 (n/a)</td><td>127.90 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.15 <b>(+28.29%)</b></td><td>0.12 <b>(+24.17%)</b></td><td>0.13 <b>(+34.95%)</b></td><td>0.09 (+4.58%)</td><td>0.03 <b>(+94.94%)</b></td><td>207.60 (-4.38%)</td><td>156.40 (-17.28%)</td><td>139.30 <b>(-25.90%)</b></td><td>121.30 <b>(-22.04%)</b></td><td>36.83 <b>(+45.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>189.08 (n/a)</td><td>188.00 (n/a)</td><td>155.60 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.14 (+3.71%)</td><td>0.12 (+12.78%)</td><td>0.13 <b>(+23.79%)</b></td><td>0.10 <b>(+23.09%)</b></td><td>0.02 <b>(-24.18%)</b></td><td>191.70 (-18.74%)</td><td>150.62 (-13.31%)</td><td>137.80 (-19.18%)</td><td>130.30 (-3.62%)</td><td>25.38 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>235.90 (n/a)</td><td>173.74 (n/a)</td><td>170.50 (n/a)</td><td>135.20 (n/a)</td><td>41.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.13 (-15.02%)</td><td>0.10 (-10.40%)</td><td>0.09 (-6.90%)</td><td>0.09 (+0.84%)</td><td>0.02 <b>(-33.36%)</b></td><td>214.60 (-0.83%)</td><td>189.78 (+9.43%)</td><td>194.70 (+7.39%)</td><td>142.90 (+17.61%)</td><td>29.61 <b>(-21.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.40 (n/a)</td><td>173.42 (n/a)</td><td>181.30 (n/a)</td><td>121.50 (n/a)</td><td>37.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (-7.00%)</td><td>0.10 (+5.47%)</td><td>0.10 (+16.40%)</td><td>0.09 (+11.02%)</td><td>0.01 <b>(-45.86%)</b></td><td>203.40 (-9.92%)</td><td>182.58 (-6.62%)</td><td>179.70 (-14.10%)</td><td>162.50 (+7.47%)</td><td>16.07 <b>(-46.96%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>225.80 (n/a)</td><td>195.52 (n/a)</td><td>209.20 (n/a)</td><td>151.20 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.79 (+2.04%)</td><td>0.63 (+6.96%)</td><td>0.61 (+15.66%)</td><td>0.45 (-0.50%)</td><td>0.16 <b>(+25.12%)</b></td><td>220.80 (+0.50%)</td><td>165.60 (-4.74%)</td><td>160.20 (-13.55%)</td><td>123.70 (-1.98%)</td><td>43.78 <b>(+20.94%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.78 (n/a)</td><td>0.59 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.13 (n/a)</td><td>219.70 (n/a)</td><td>173.84 (n/a)</td><td>185.30 (n/a)</td><td>126.20 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.74 (-4.27%)</td><td>0.58 (+10.84%)</td><td>0.59 (+18.10%)</td><td>0.45 (+16.78%)</td><td>0.11 <b>(-24.40%)</b></td><td>217.70 (-14.36%)</td><td>176.16 (-12.01%)</td><td>167.60 (-15.31%)</td><td>133.50 (+4.46%)</td><td>33.75 <b>(-29.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.77 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.15 (n/a)</td><td>254.20 (n/a)</td><td>200.20 (n/a)</td><td>197.90 (n/a)</td><td>127.80 (n/a)</td><td>47.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.96 <b>(+31.78%)</b></td><td>0.70 (+14.22%)</td><td>0.62 (+6.72%)</td><td>0.55 <b>(+26.53%)</b></td><td>0.16 <b>(+34.98%)</b></td><td>177.60 <b>(-20.96%)</b></td><td>146.98 (-12.16%)</td><td>158.20 (-6.28%)</td><td>102.10 <b>(-24.09%)</b></td><td>29.69 (-18.88%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.73 (n/a)</td><td>0.61 (n/a)</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.12 (n/a)</td><td>224.70 (n/a)</td><td>167.32 (n/a)</td><td>168.80 (n/a)</td><td>134.50 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.77 <b>(+24.27%)</b></td><td>0.58 (+12.34%)</td><td>0.57 (+8.25%)</td><td>0.40 (-6.20%)</td><td>0.14 <b>(+79.25%)</b></td><td>248.50 (+6.61%)</td><td>177.94 (-8.34%)</td><td>174.00 (-7.59%)</td><td>128.40 (-19.55%)</td><td>44.62 <b>(+55.58%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.62 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.08 (n/a)</td><td>233.10 (n/a)</td><td>194.12 (n/a)</td><td>188.30 (n/a)</td><td>159.60 (n/a)</td><td>28.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.61 (+9.05%)</td><td>0.46 (-0.48%)</td><td>0.43 (+2.48%)</td><td>0.33 (-17.84%)</td><td>0.10 <b>(+56.75%)</b></td><td>220.40 <b>(+21.70%)</b></td><td>167.20 (+2.87%)</td><td>170.20 (-2.46%)</td><td>120.70 (-8.28%)</td><td>36.16 <b>(+73.38%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.06 (n/a)</td><td>181.10 (n/a)</td><td>162.54 (n/a)</td><td>174.50 (n/a)</td><td>131.60 (n/a)</td><td>20.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.56 (+7.72%)</td><td>0.39 (-9.31%)</td><td>0.35 (-19.19%)</td><td>0.24 <b>(-31.74%)</b></td><td>0.12 <b>(+103.99%)</b></td><td>308.10 <b>(+46.50%)</b></td><td>203.32 (+17.99%)</td><td>207.70 <b>(+23.78%)</b></td><td>131.60 (-7.13%)</td><td>67.62 <b>(+174.63%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>210.30 (n/a)</td><td>172.32 (n/a)</td><td>167.80 (n/a)</td><td>141.70 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.51 (+9.23%)</td><td>0.43 (+9.49%)</td><td>0.47 (+16.34%)</td><td>0.33 (+11.62%)</td><td>0.09 (+18.87%)</td><td>223.40 (-10.39%)</td><td>179.52 (-8.06%)</td><td>157.80 (-14.05%)</td><td>144.60 (-8.42%)</td><td>40.30 (+1.19%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>249.30 (n/a)</td><td>195.26 (n/a)</td><td>183.60 (n/a)</td><td>157.90 (n/a)</td><td>39.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.50 <b>(+20.45%)</b></td><td>0.45 (+18.32%)</td><td>0.46 (+16.73%)</td><td>0.42 <b>(+26.23%)</b></td><td>0.03 (-9.51%)</td><td>175.40 <b>(-20.78%)</b></td><td>163.28 (-15.72%)</td><td>161.70 (-14.31%)</td><td>148.10 (-16.98%)</td><td>10.87 <b>(-39.79%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.03 (n/a)</td><td>221.40 (n/a)</td><td>193.74 (n/a)</td><td>188.70 (n/a)</td><td>178.40 (n/a)</td><td>18.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.30 <b>(+25.91%)</b></td><td>0.25 <b>(+22.56%)</b></td><td>0.23 (+4.05%)</td><td>0.19 <b>(+73.27%)</b></td><td>0.05 (-3.02%)</td><td>197.40 <b>(-42.30%)</b></td><td>155.66 <b>(-22.53%)</b></td><td>157.60 (-3.90%)</td><td>122.00 <b>(-20.57%)</b></td><td>32.94 <b>(-58.68%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>342.10 (n/a)</td><td>200.92 (n/a)</td><td>164.00 (n/a)</td><td>153.60 (n/a)</td><td>79.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (-5.29%)</td><td>0.23 (+2.87%)</td><td>0.21 (-11.07%)</td><td>0.19 <b>(+89.76%)</b></td><td>0.04 <b>(-48.33%)</b></td><td>194.60 <b>(-47.32%)</b></td><td>166.38 (-13.80%)</td><td>177.40 (+12.49%)</td><td>136.20 (+5.58%)</td><td>26.05 <b>(-73.85%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>369.40 (n/a)</td><td>193.02 (n/a)</td><td>157.70 (n/a)</td><td>129.00 (n/a)</td><td>99.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 <b>(+29.24%)</b></td><td>0.24 (+18.83%)</td><td>0.23 (+17.38%)</td><td>0.20 (+16.51%)</td><td>0.03 <b>(+38.69%)</b></td><td>185.30 (-14.17%)</td><td>158.28 (-15.62%)</td><td>157.90 (-14.83%)</td><td>127.00 <b>(-22.66%)</b></td><td>20.83 (-8.95%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>215.90 (n/a)</td><td>187.58 (n/a)</td><td>185.40 (n/a)</td><td>164.20 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.34 <b>(+21.57%)</b></td><td>0.27 <b>(+22.18%)</b></td><td>0.26 <b>(+23.21%)</b></td><td>0.20 (+11.29%)</td><td>0.05 <b>(+34.08%)</b></td><td>183.10 (-10.11%)</td><td>142.86 (-17.50%)</td><td>140.40 (-18.84%)</td><td>107.40 (-17.70%)</td><td>28.08 (+0.69%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>203.70 (n/a)</td><td>173.16 (n/a)</td><td>173.00 (n/a)</td><td>130.50 (n/a)</td><td>27.89 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 <b>(+20.24%)</b></td><td>0.22 (+4.50%)</td><td>0.22 (+0.22%)</td><td>0.16 (-11.99%)</td><td>0.05 <b>(+189.01%)</b></td><td>225.40 (+13.61%)</td><td>174.80 (-0.65%)</td><td>169.70 (-0.24%)</td><td>135.00 (-16.82%)</td><td>40.67 <b>(+167.71%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>198.40 (n/a)</td><td>175.94 (n/a)</td><td>170.10 (n/a)</td><td>162.30 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 <b>(-24.75%)</b></td><td>0.19 (-16.62%)</td><td>0.18 (-15.56%)</td><td>0.16 (-10.48%)</td><td>0.02 <b>(-57.64%)</b></td><td>229.30 (+11.69%)</td><td>198.50 (+16.82%)</td><td>199.40 (+18.41%)</td><td>170.90 <b>(+32.89%)</b></td><td>21.50 <b>(-38.99%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>205.30 (n/a)</td><td>169.92 (n/a)</td><td>168.40 (n/a)</td><td>128.60 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.30 <b>(+52.93%)</b></td><td>0.25 <b>(+31.94%)</b></td><td>0.25 <b>(+34.53%)</b></td><td>0.16 (-8.00%)</td><td>0.05 <b>(+717.42%)</b></td><td>225.00 (+8.70%)</td><td>156.80 <b>(-20.98%)</b></td><td>147.40 <b>(-25.67%)</b></td><td>124.30 <b>(-34.61%)</b></td><td>39.91 <b>(+502.31%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>198.42 (n/a)</td><td>198.30 (n/a)</td><td>190.10 (n/a)</td><td>6.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (+9.18%)</td><td>0.20 (+7.06%)</td><td>0.21 (+18.92%)</td><td>0.16 (-4.26%)</td><td>0.03 <b>(+57.83%)</b></td><td>229.80 (+4.45%)</td><td>187.94 (-5.50%)</td><td>174.50 (-15.90%)</td><td>156.00 (-8.40%)</td><td>29.97 <b>(+53.83%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>198.88 (n/a)</td><td>207.50 (n/a)</td><td>170.30 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 (+14.03%)</td><td>0.25 (+7.28%)</td><td>0.23 (-1.32%)</td><td>0.20 (+6.03%)</td><td>0.05 <b>(+60.89%)</b></td><td>203.80 (-5.65%)</td><td>167.44 (-5.40%)</td><td>177.20 (+1.32%)</td><td>134.20 (-12.34%)</td><td>31.25 <b>(+27.52%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>216.00 (n/a)</td><td>177.00 (n/a)</td><td>174.90 (n/a)</td><td>153.10 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.28 (-9.62%)</td><td>0.23 (-10.11%)</td><td>0.22 (-14.90%)</td><td>0.19 (-18.54%)</td><td>0.04 (+19.52%)</td><td>220.00 <b>(+22.77%)</b></td><td>181.36 (+12.39%)</td><td>189.40 (+17.57%)</td><td>146.80 (+10.63%)</td><td>29.35 <b>(+61.57%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>179.20 (n/a)</td><td>161.36 (n/a)</td><td>161.10 (n/a)</td><td>132.70 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (+12.83%)</td><td>0.26 (+7.94%)</td><td>0.25 (+2.32%)</td><td>0.19 (-0.55%)</td><td>0.05 <b>(+33.90%)</b></td><td>216.30 (+0.56%)</td><td>164.22 (-6.30%)</td><td>162.50 (-2.29%)</td><td>126.10 (-11.38%)</td><td>33.27 <b>(+20.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>215.10 (n/a)</td><td>175.26 (n/a)</td><td>166.30 (n/a)</td><td>142.30 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (+3.60%)</td><td>0.27 (+11.80%)</td><td>0.25 <b>(+20.33%)</b></td><td>0.24 <b>(+22.62%)</b></td><td>0.03 <b>(-34.02%)</b></td><td>173.60 (-18.42%)</td><td>155.36 (-12.33%)</td><td>160.90 (-16.89%)</td><td>129.70 (-3.50%)</td><td>17.32 <b>(-47.96%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>212.80 (n/a)</td><td>177.20 (n/a)</td><td>193.60 (n/a)</td><td>134.40 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.33 <b>(+20.35%)</b></td><td>0.24 (+5.27%)</td><td>0.23 (+2.44%)</td><td>0.20 (-2.63%)</td><td>0.05 <b>(+75.67%)</b></td><td>205.90 (+2.69%)</td><td>173.82 (-3.14%)</td><td>181.70 (-2.36%)</td><td>122.40 (-16.90%)</td><td>31.80 <b>(+44.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>200.50 (n/a)</td><td>179.46 (n/a)</td><td>186.10 (n/a)</td><td>147.30 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 <b>(+20.01%)</b></td><td>0.23 (+8.35%)</td><td>0.23 (+6.67%)</td><td>0.19 (+6.29%)</td><td>0.04 <b>(+58.26%)</b></td><td>210.80 (-5.89%)</td><td>178.34 (-6.89%)</td><td>177.00 (-6.25%)</td><td>140.50 (-16.67%)</td><td>26.01 <b>(+21.78%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>224.00 (n/a)</td><td>191.54 (n/a)</td><td>188.80 (n/a)</td><td>168.60 (n/a)</td><td>21.36 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 <b>(+32.06%)</b></td><td>0.26 <b>(+34.48%)</b></td><td>0.25 <b>(+22.15%)</b></td><td>0.21 <b>(+70.99%)</b></td><td>0.04 (-5.91%)</td><td>193.50 <b>(-41.51%)</b></td><td>162.90 <b>(-27.88%)</b></td><td>161.30 (-18.16%)</td><td>133.50 <b>(-24.32%)</b></td><td>25.47 <b>(-59.18%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>330.80 (n/a)</td><td>225.88 (n/a)</td><td>197.10 (n/a)</td><td>176.40 (n/a)</td><td>62.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.25 (+5.21%)</td><td>0.21 (+4.72%)</td><td>0.22 (+16.36%)</td><td>0.14 <b>(-21.05%)</b></td><td>0.05 <b>(+83.48%)</b></td><td>296.80 <b>(+26.68%)</b></td><td>208.58 (-1.16%)</td><td>188.50 (-14.08%)</td><td>164.10 (-4.98%)</td><td>53.99 <b>(+126.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>234.30 (n/a)</td><td>211.02 (n/a)</td><td>219.40 (n/a)</td><td>172.70 (n/a)</td><td>23.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.31 (+19.09%)</td><td>0.23 (+17.47%)</td><td>0.22 (+15.92%)</td><td>0.18 <b>(+56.63%)</b></td><td>0.05 (-7.23%)</td><td>191.40 <b>(-36.16%)</b></td><td>155.94 (-18.32%)</td><td>158.30 (-13.73%)</td><td>111.60 (-16.03%)</td><td>31.13 <b>(-52.17%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>299.80 (n/a)</td><td>190.92 (n/a)</td><td>183.50 (n/a)</td><td>132.90 (n/a)</td><td>65.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.29 <b>(+32.82%)</b></td><td>0.25 <b>(+34.33%)</b></td><td>0.26 <b>(+33.31%)</b></td><td>0.19 <b>(+20.92%)</b></td><td>0.04 <b>(+40.62%)</b></td><td>180.50 (-17.28%)</td><td>140.76 <b>(-25.29%)</b></td><td>132.50 <b>(-25.01%)</b></td><td>119.10 <b>(-24.72%)</b></td><td>23.57 (-12.24%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>218.20 (n/a)</td><td>188.42 (n/a)</td><td>176.70 (n/a)</td><td>158.20 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (+9.81%)</td><td>0.19 (-4.19%)</td><td>0.17 (-9.92%)</td><td>0.14 (-14.49%)</td><td>0.05 <b>(+68.06%)</b></td><td>253.70 (+16.91%)</td><td>196.82 (+8.08%)</td><td>203.70 (+11.01%)</td><td>132.00 (-8.97%)</td><td>47.95 <b>(+78.84%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>217.00 (n/a)</td><td>182.10 (n/a)</td><td>183.50 (n/a)</td><td>145.00 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (+17.76%)</td><td>0.24 (+11.69%)</td><td>0.21 (-0.54%)</td><td>0.20 (+11.02%)</td><td>0.06 <b>(+30.87%)</b></td><td>177.50 (-9.94%)</td><td>149.46 (-9.72%)</td><td>165.20 (+0.55%)</td><td>107.60 (-15.07%)</td><td>30.64 (-1.87%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>197.10 (n/a)</td><td>165.56 (n/a)</td><td>164.30 (n/a)</td><td>126.70 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.32 (+8.97%)</td><td>0.26 <b>(+27.31%)</b></td><td>0.26 <b>(+34.25%)</b></td><td>0.20 <b>(+126.06%)</b></td><td>0.05 <b>(-41.19%)</b></td><td>172.40 <b>(-55.77%)</b></td><td>139.38 <b>(-31.84%)</b></td><td>135.70 <b>(-25.52%)</b></td><td>110.20 (-8.17%)</td><td>25.10 <b>(-76.83%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>389.80 (n/a)</td><td>204.48 (n/a)</td><td>182.20 (n/a)</td><td>120.00 (n/a)</td><td>108.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.26 (+3.55%)</td><td>0.20 (-4.54%)</td><td>0.19 (-6.35%)</td><td>0.10 <b>(-41.95%)</b></td><td>0.07 <b>(+57.48%)</b></td><td>361.10 <b>(+72.28%)</b></td><td>199.20 (+15.36%)</td><td>182.00 (+6.81%)</td><td>132.60 (-3.49%)</td><td>93.77 <b>(+166.85%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>209.60 (n/a)</td><td>172.68 (n/a)</td><td>170.40 (n/a)</td><td>137.40 (n/a)</td><td>35.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.28 <b>(+24.78%)</b></td><td>0.20 (+12.25%)</td><td>0.20 (+14.04%)</td><td>0.16 (+11.24%)</td><td>0.05 <b>(+42.30%)</b></td><td>221.00 (-10.13%)</td><td>178.04 (-9.79%)</td><td>176.70 (-12.35%)</td><td>124.70 (-19.86%)</td><td>38.08 (+3.89%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>245.90 (n/a)</td><td>197.36 (n/a)</td><td>201.60 (n/a)</td><td>155.60 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.22 (+10.34%)</td><td>0.19 (+9.42%)</td><td>0.20 (+9.39%)</td><td>0.17 (+7.22%)</td><td>0.03 <b>(+24.86%)</b></td><td>210.70 (-6.73%)</td><td>182.68 (-8.28%)</td><td>171.40 (-8.59%)</td><td>160.30 (-9.38%)</td><td>25.59 (+4.99%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.90 (n/a)</td><td>199.18 (n/a)</td><td>187.50 (n/a)</td><td>176.90 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.07 (+6.01%)</td><td>0.89 (+17.00%)</td><td>0.85 <b>(+24.17%)</b></td><td>0.80 <b>(+35.16%)</b></td><td>0.11 <b>(-35.14%)</b></td><td>163.60 <b>(-26.01%)</b></td><td>148.22 (-16.67%)</td><td>153.60 (-19.45%)</td><td>122.10 (-5.71%)</td><td>16.56 <b>(-54.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.01 (n/a)</td><td>0.76 (n/a)</td><td>0.69 (n/a)</td><td>0.59 (n/a)</td><td>0.17 (n/a)</td><td>221.10 (n/a)</td><td>177.88 (n/a)</td><td>190.70 (n/a)</td><td>129.50 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.96 (+7.78%)</td><td>0.81 (-2.80%)</td><td>0.75 (-12.13%)</td><td>0.70 (-0.21%)</td><td>0.11 <b>(+43.39%)</b></td><td>188.30 (+0.21%)</td><td>163.98 (+3.59%)</td><td>174.00 (+13.80%)</td><td>136.90 (-7.25%)</td><td>21.96 <b>(+30.38%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.89 (n/a)</td><td>0.83 (n/a)</td><td>0.86 (n/a)</td><td>0.70 (n/a)</td><td>0.08 (n/a)</td><td>187.90 (n/a)</td><td>158.30 (n/a)</td><td>152.90 (n/a)</td><td>147.60 (n/a)</td><td>16.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.88 (-15.22%)</td><td>0.74 (-5.12%)</td><td>0.78 (+17.46%)</td><td>0.46 <b>(-25.89%)</b></td><td>0.16 (-16.48%)</td><td>282.30 <b>(+34.94%)</b></td><td>187.16 (+6.05%)</td><td>168.40 (-14.86%)</td><td>149.10 (+17.96%)</td><td>54.08 <b>(+36.86%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.04 (n/a)</td><td>0.78 (n/a)</td><td>0.66 (n/a)</td><td>0.63 (n/a)</td><td>0.19 (n/a)</td><td>209.20 (n/a)</td><td>176.48 (n/a)</td><td>197.80 (n/a)</td><td>126.40 (n/a)</td><td>39.51 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.00 (+0.00%)</td><td>0.00 (-0.47%)</td><td>0.00 (-2.33%)</td><td>0.00 (+2.56%)</td><td>0.00 <b>(-28.47%)</b></td><td>1020.28 (-3.34%)</td><td>973.63 (+0.43%)</td><td>979.96 (+3.34%)</td><td>927.24 (-0.97%)</td><td>33.98 <b>(-31.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1055.53 (n/a)</td><td>969.43 (n/a)</td><td>948.29 (n/a)</td><td>936.36 (n/a)</td><td>49.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.01 (+1.19%)</td><td>0.01 (-2.66%)</td><td>0.01 (-1.22%)</td><td>0.01 (-8.64%)</td><td>0.00 <b>(+200.92%)</b></td><td>1109.98 (+9.92%)</td><td>1022.52 (+3.21%)</td><td>1014.12 (+1.98%)</td><td>958.97 (-1.67%)</td><td>55.41 <b>(+296.05%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1009.78 (n/a)</td><td>990.69 (n/a)</td><td>994.41 (n/a)</td><td>975.27 (n/a)</td><td>13.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.99 (-1.47%)</td><td>0.96 (-0.81%)</td><td>0.96 (-0.49%)</td><td>0.94 (-0.83%)</td><td>0.02 (-14.92%)</td><td>2226.62 (+0.84%)</td><td>2187.63 (+0.81%)</td><td>2195.80 (+0.50%)</td><td>2123.59 (+1.49%)</td><td>39.16 (-12.68%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2208.09 (n/a)</td><td>2170.08 (n/a)</td><td>2184.93 (n/a)</td><td>2092.51 (n/a)</td><td>44.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.41 (+1.94%)</td><td>0.39 (-1.52%)</td><td>0.39 (-2.15%)</td><td>0.38 (-3.74%)</td><td>0.01 <b>(+594.49%)</b></td><td>1366.35 (+3.89%)</td><td>1331.62 (+1.60%)</td><td>1341.93 (+2.21%)</td><td>1278.79 (-1.90%)</td><td>34.45 <b>(+615.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.00 (n/a)</td><td>1315.19 (n/a)</td><td>1310.68 (n/a)</td><td>1312.97 (n/a)</td><td>1303.62 (n/a)</td><td>4.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.27 (+2.13%)</td><td>0.27 (+2.29%)</td><td>0.27 (+4.17%)</td><td>0.25 (-0.31%)</td><td>0.01 <b>(+21.59%)</b></td><td>2065.12 (+0.31%)</td><td>1973.07 (-2.23%)</td><td>1960.42 (-4.03%)</td><td>1922.04 (-2.09%)</td><td>55.15 <b>(+20.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2058.68 (n/a)</td><td>2018.00 (n/a)</td><td>2042.70 (n/a)</td><td>1963.09 (n/a)</td><td>45.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.38 (+1.14%)</td><td>0.37 (-1.30%)</td><td>0.36 (-1.44%)</td><td>0.36 (-2.12%)</td><td>0.01 <b>(+89.92%)</b></td><td>1475.40 (+2.19%)</td><td>1434.75 (+1.37%)</td><td>1440.55 (+1.43%)</td><td>1374.72 (-1.13%)</td><td>39.25 <b>(+92.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1443.73 (n/a)</td><td>1415.38 (n/a)</td><td>1420.24 (n/a)</td><td>1390.38 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>5.68 (+4.15%)</td><td>4.64 (-2.62%)</td><td>4.53 (-0.04%)</td><td>3.39 <b>(-20.02%)</b></td><td>0.85 <b>(+46.45%)</b></td><td>309.50 <b>(+25.05%)</b></td><td>232.78 (+4.58%)</td><td>231.30 (+0.04%)</td><td>184.70 (-3.95%)</td><td>47.24 <b>(+80.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.45 (n/a)</td><td>4.77 (n/a)</td><td>4.54 (n/a)</td><td>4.24 (n/a)</td><td>0.58 (n/a)</td><td>247.50 (n/a)</td><td>222.58 (n/a)</td><td>231.20 (n/a)</td><td>192.30 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>5.84 (+6.68%)</td><td>4.94 (+4.47%)</td><td>4.98 (+2.61%)</td><td>4.37 (+4.37%)</td><td>0.60 (+12.59%)</td><td>240.00 (-4.19%)</td><td>214.88 (-4.16%)</td><td>210.50 (-2.55%)</td><td>179.60 (-6.26%)</td><td>24.92 (+0.59%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.47 (n/a)</td><td>4.72 (n/a)</td><td>4.85 (n/a)</td><td>4.19 (n/a)</td><td>0.53 (n/a)</td><td>250.50 (n/a)</td><td>224.20 (n/a)</td><td>216.00 (n/a)</td><td>191.60 (n/a)</td><td>24.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>5.38 (+5.80%)</td><td>4.61 (-1.89%)</td><td>4.67 (-6.37%)</td><td>3.78 (-8.70%)</td><td>0.57 <b>(+22.83%)</b></td><td>277.50 (+9.51%)</td><td>230.22 (+2.40%)</td><td>224.60 (+6.80%)</td><td>194.90 (-5.48%)</td><td>29.86 <b>(+29.42%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.08 (n/a)</td><td>4.70 (n/a)</td><td>4.99 (n/a)</td><td>4.14 (n/a)</td><td>0.46 (n/a)</td><td>253.40 (n/a)</td><td>224.82 (n/a)</td><td>210.30 (n/a)</td><td>206.20 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.29 <b>(+24.73%)</b></td><td>4.47 (-3.72%)</td><td>4.11 (-11.75%)</td><td>3.38 <b>(-21.11%)</b></td><td>1.12 <b>(+303.30%)</b></td><td>309.90 <b>(+26.75%)</b></td><td>245.30 (+8.20%)</td><td>255.10 (+13.33%)</td><td>166.80 (-19.81%)</td><td>53.52 <b>(+298.56%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.04 (n/a)</td><td>4.64 (n/a)</td><td>4.66 (n/a)</td><td>4.29 (n/a)</td><td>0.28 (n/a)</td><td>244.50 (n/a)</td><td>226.70 (n/a)</td><td>225.10 (n/a)</td><td>208.00 (n/a)</td><td>13.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.99 <b>(+24.29%)</b></td><td>7.79 (+3.20%)</td><td>7.72 (+1.15%)</td><td>6.42 (-8.48%)</td><td>1.34 <b>(+261.00%)</b></td><td>326.50 (+9.27%)</td><td>275.06 (-1.18%)</td><td>271.70 (-1.13%)</td><td>210.00 (-19.54%)</td><td>43.03 <b>(+209.49%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.03 (n/a)</td><td>7.55 (n/a)</td><td>7.63 (n/a)</td><td>7.02 (n/a)</td><td>0.37 (n/a)</td><td>298.80 (n/a)</td><td>278.34 (n/a)</td><td>274.80 (n/a)</td><td>261.00 (n/a)</td><td>13.90 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.71 (+9.65%)</td><td>7.74 (+3.02%)</td><td>7.73 (+4.94%)</td><td>7.12 (-1.66%)</td><td>0.64 <b>(+95.11%)</b></td><td>294.70 (+1.69%)</td><td>272.24 (-2.57%)</td><td>271.30 (-4.74%)</td><td>240.70 (-8.79%)</td><td>21.57 <b>(+80.71%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.95 (n/a)</td><td>7.52 (n/a)</td><td>7.36 (n/a)</td><td>7.24 (n/a)</td><td>0.33 (n/a)</td><td>289.80 (n/a)</td><td>279.42 (n/a)</td><td>284.80 (n/a)</td><td>263.90 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.36 (-2.27%)</td><td>7.73 (+5.17%)</td><td>7.76 (+8.16%)</td><td>6.93 (+16.05%)</td><td>0.54 <b>(-44.95%)</b></td><td>302.60 (-13.84%)</td><td>272.38 (-5.94%)</td><td>270.20 (-7.53%)</td><td>250.70 (+2.28%)</td><td>19.56 <b>(-51.37%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.56 (n/a)</td><td>7.35 (n/a)</td><td>7.18 (n/a)</td><td>5.97 (n/a)</td><td>0.98 (n/a)</td><td>351.20 (n/a)</td><td>289.58 (n/a)</td><td>292.20 (n/a)</td><td>245.10 (n/a)</td><td>40.22 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.06 (+4.31%)</td><td>8.31 (+4.60%)</td><td>8.93 (+15.94%)</td><td>6.85 (-8.83%)</td><td>1.00 <b>(+91.11%)</b></td><td>306.00 (+9.68%)</td><td>255.60 (-3.50%)</td><td>234.90 (-13.77%)</td><td>231.40 (-4.10%)</td><td>33.25 <b>(+96.16%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.69 (n/a)</td><td>7.94 (n/a)</td><td>7.70 (n/a)</td><td>7.52 (n/a)</td><td>0.52 (n/a)</td><td>279.00 (n/a)</td><td>264.88 (n/a)</td><td>272.40 (n/a)</td><td>241.30 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.77 (+7.58%)</td><td>8.38 (+2.36%)</td><td>8.46 (+1.14%)</td><td>7.35 (+2.34%)</td><td>1.00 (+11.33%)</td><td>285.10 (-2.30%)</td><td>253.16 (-2.18%)</td><td>247.90 (-1.12%)</td><td>214.50 (-7.06%)</td><td>29.80 (+2.43%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>9.09 (n/a)</td><td>8.18 (n/a)</td><td>8.36 (n/a)</td><td>7.19 (n/a)</td><td>0.90 (n/a)</td><td>291.80 (n/a)</td><td>258.80 (n/a)</td><td>250.70 (n/a)</td><td>230.80 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>8.67 (-7.95%)</td><td>7.80 (-9.86%)</td><td>8.08 (-6.97%)</td><td>6.34 <b>(-21.33%)</b></td><td>0.87 <b>(+66.39%)</b></td><td>330.70 <b>(+27.09%)</b></td><td>271.86 (+11.86%)</td><td>259.70 (+7.49%)</td><td>241.90 (+8.62%)</td><td>34.22 <b>(+136.00%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>9.42 (n/a)</td><td>8.65 (n/a)</td><td>8.68 (n/a)</td><td>8.06 (n/a)</td><td>0.52 (n/a)</td><td>260.20 (n/a)</td><td>243.04 (n/a)</td><td>241.60 (n/a)</td><td>222.70 (n/a)</td><td>14.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.02 <b>(+22.59%)</b></td><td>12.29 (+16.19%)</td><td>12.10 (+15.17%)</td><td>11.07 (+14.60%)</td><td>1.27 <b>(+78.09%)</b></td><td>379.00 (-12.75%)</td><td>344.10 (-13.54%)</td><td>346.50 (-13.18%)</td><td>299.30 (-18.42%)</td><td>34.72 <b>(+28.42%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>11.43 (n/a)</td><td>10.58 (n/a)</td><td>10.51 (n/a)</td><td>9.66 (n/a)</td><td>0.71 (n/a)</td><td>434.40 (n/a)</td><td>397.98 (n/a)</td><td>399.10 (n/a)</td><td>366.90 (n/a)</td><td>27.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.87 (+13.20%)</td><td>11.66 (+0.12%)</td><td>11.72 (-1.31%)</td><td>9.85 (-8.55%)</td><td>1.49 <b>(+127.05%)</b></td><td>425.70 (+9.35%)</td><td>364.36 (+0.90%)</td><td>357.90 (+1.30%)</td><td>302.40 (-11.66%)</td><td>45.44 <b>(+119.18%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>12.25 (n/a)</td><td>11.65 (n/a)</td><td>11.87 (n/a)</td><td>10.77 (n/a)</td><td>0.65 (n/a)</td><td>389.30 (n/a)</td><td>361.12 (n/a)</td><td>353.30 (n/a)</td><td>342.30 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>12.22 (+6.57%)</td><td>11.54 (+4.80%)</td><td>11.38 (+3.69%)</td><td>11.31 (+10.15%)</td><td>0.38 <b>(-20.88%)</b></td><td>371.00 (-9.20%)</td><td>363.90 (-4.65%)</td><td>368.40 (-3.56%)</td><td>343.30 (-6.15%)</td><td>11.57 <b>(-32.77%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>11.47 (n/a)</td><td>11.01 (n/a)</td><td>10.98 (n/a)</td><td>10.26 (n/a)</td><td>0.48 (n/a)</td><td>408.60 (n/a)</td><td>381.64 (n/a)</td><td>382.00 (n/a)</td><td>365.80 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>12.94 (-9.34%)</td><td>11.92 (-7.27%)</td><td>12.14 (-5.76%)</td><td>10.90 (-4.72%)</td><td>0.94 <b>(-20.47%)</b></td><td>384.80 (+4.94%)</td><td>353.70 (+7.64%)</td><td>345.50 (+6.11%)</td><td>324.30 (+10.31%)</td><td>28.31 (-7.18%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>14.27 (n/a)</td><td>12.85 (n/a)</td><td>12.88 (n/a)</td><td>11.44 (n/a)</td><td>1.19 (n/a)</td><td>366.70 (n/a)</td><td>328.60 (n/a)</td><td>325.60 (n/a)</td><td>294.00 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.94 (+11.53%)</td><td>12.77 (+7.45%)</td><td>12.63 (+4.19%)</td><td>11.54 (+6.73%)</td><td>1.00 <b>(+52.44%)</b></td><td>363.40 (-6.32%)</td><td>330.12 (-6.71%)</td><td>332.20 (-4.02%)</td><td>300.80 (-10.34%)</td><td>25.86 <b>(+26.25%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>12.50 (n/a)</td><td>11.88 (n/a)</td><td>12.12 (n/a)</td><td>10.81 (n/a)</td><td>0.65 (n/a)</td><td>387.90 (n/a)</td><td>353.88 (n/a)</td><td>346.10 (n/a)</td><td>335.50 (n/a)</td><td>20.48 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.37 (-1.39%)</td><td>12.44 (-3.36%)</td><td>12.15 (-8.40%)</td><td>11.37 (+0.35%)</td><td>1.14 (-16.06%)</td><td>368.80 (-0.35%)</td><td>339.22 (+3.18%)</td><td>345.30 (+9.17%)</td><td>291.90 (+1.39%)</td><td>28.87 (-17.88%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>14.57 (n/a)</td><td>12.87 (n/a)</td><td>13.26 (n/a)</td><td>11.33 (n/a)</td><td>1.36 (n/a)</td><td>370.10 (n/a)</td><td>328.76 (n/a)</td><td>316.30 (n/a)</td><td>287.90 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>14.63 (+2.06%)</td><td>12.84 (-1.37%)</td><td>12.61 (-3.89%)</td><td>11.95 (+0.22%)</td><td>1.08 <b>(+21.00%)</b></td><td>351.00 (-0.23%)</td><td>328.30 (+1.55%)</td><td>332.70 (+4.03%)</td><td>286.60 (-2.02%)</td><td>25.85 (+18.02%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>14.34 (n/a)</td><td>13.02 (n/a)</td><td>13.12 (n/a)</td><td>11.92 (n/a)</td><td>0.89 (n/a)</td><td>351.80 (n/a)</td><td>323.28 (n/a)</td><td>319.80 (n/a)</td><td>292.50 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>13.84 (-0.83%)</td><td>12.61 (+1.06%)</td><td>12.65 (+0.84%)</td><td>11.38 (+5.27%)</td><td>0.88 <b>(-32.91%)</b></td><td>368.60 (-5.00%)</td><td>333.98 (-1.55%)</td><td>331.50 (-0.81%)</td><td>303.10 (+0.83%)</td><td>23.47 <b>(-35.34%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>13.95 (n/a)</td><td>12.48 (n/a)</td><td>12.55 (n/a)</td><td>10.81 (n/a)</td><td>1.31 (n/a)</td><td>388.00 (n/a)</td><td>339.24 (n/a)</td><td>334.20 (n/a)</td><td>300.60 (n/a)</td><td>36.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.15 (+16.26%)</td><td>2.84 (+12.51%)</td><td>2.77 (+5.61%)</td><td>2.58 (+16.91%)</td><td>0.25 (+12.81%)</td><td>203.10 (-14.48%)</td><td>185.44 (-11.15%)</td><td>189.00 (-5.31%)</td><td>166.40 (-14.01%)</td><td>16.01 (-16.66%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>2.71 (n/a)</td><td>2.53 (n/a)</td><td>2.63 (n/a)</td><td>2.21 (n/a)</td><td>0.22 (n/a)</td><td>237.50 (n/a)</td><td>208.72 (n/a)</td><td>199.60 (n/a)</td><td>193.50 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>6.16 (+13.60%)</td><td>4.69 (-2.08%)</td><td>4.51 (-4.42%)</td><td>3.60 (-14.39%)</td><td>0.93 <b>(+109.89%)</b></td><td>291.20 (+16.81%)</td><td>230.38 (+4.49%)</td><td>232.40 (+4.64%)</td><td>170.20 (-11.95%)</td><td>43.18 <b>(+112.25%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.42 (n/a)</td><td>4.79 (n/a)</td><td>4.72 (n/a)</td><td>4.21 (n/a)</td><td>0.44 (n/a)</td><td>249.30 (n/a)</td><td>220.48 (n/a)</td><td>222.10 (n/a)</td><td>193.30 (n/a)</td><td>20.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>9.65 <b>(+22.63%)</b></td><td>8.26 (+14.59%)</td><td>8.08 (+14.34%)</td><td>6.85 (-0.56%)</td><td>1.24 <b>(+223.68%)</b></td><td>306.20 (+0.56%)</td><td>258.62 (-11.32%)</td><td>259.50 (-12.54%)</td><td>217.30 (-18.46%)</td><td>38.94 <b>(+164.58%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.87 (n/a)</td><td>7.21 (n/a)</td><td>7.07 (n/a)</td><td>6.89 (n/a)</td><td>0.38 (n/a)</td><td>304.50 (n/a)</td><td>291.62 (n/a)</td><td>296.70 (n/a)</td><td>266.50 (n/a)</td><td>14.72 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>3.32 (-9.85%)</td><td>2.91 (-7.58%)</td><td>2.78 (-10.67%)</td><td>2.75 (+0.23%)</td><td>0.24 <b>(-29.05%)</b></td><td>190.90 (-0.26%)</td><td>181.24 (+7.77%)</td><td>188.60 (+11.93%)</td><td>158.00 (+10.88%)</td><td>13.78 <b>(-20.73%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.68 (n/a)</td><td>3.15 (n/a)</td><td>3.11 (n/a)</td><td>2.74 (n/a)</td><td>0.34 (n/a)</td><td>191.40 (n/a)</td><td>168.18 (n/a)</td><td>168.50 (n/a)</td><td>142.50 (n/a)</td><td>17.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.21 (-7.68%)</td><td>0.20 (+9.79%)</td><td>0.21 (+19.66%)</td><td>0.19 <b>(+23.84%)</b></td><td>0.01 <b>(-68.18%)</b></td><td>172.50 (-19.28%)</td><td>161.68 (-10.82%)</td><td>156.70 (-16.43%)</td><td>154.30 (+8.36%)</td><td>8.30 <b>(-72.26%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.70 (n/a)</td><td>181.30 (n/a)</td><td>187.50 (n/a)</td><td>142.40 (n/a)</td><td>29.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.24 (+16.36%)</td><td>0.20 <b>(+26.10%)</b></td><td>0.20 <b>(+27.47%)</b></td><td>0.17 <b>(+31.28%)</b></td><td>0.02 (-12.30%)</td><td>190.80 <b>(-23.80%)</b></td><td>162.88 <b>(-21.50%)</b></td><td>160.80 <b>(-21.52%)</b></td><td>137.40 (-14.07%)</td><td>19.12 <b>(-41.44%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>250.40 (n/a)</td><td>207.50 (n/a)</td><td>204.90 (n/a)</td><td>159.90 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.53 (-5.40%)</td><td>0.39 (-2.02%)</td><td>0.35 (-2.42%)</td><td>0.32 (+4.74%)</td><td>0.08 (-12.25%)</td><td>203.30 (-4.51%)</td><td>175.64 (+1.33%)</td><td>184.90 (+2.44%)</td><td>124.60 (+5.68%)</td><td>32.07 (-7.93%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>212.90 (n/a)</td><td>173.34 (n/a)</td><td>180.50 (n/a)</td><td>117.90 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.46 (+18.53%)</td><td>0.36 (+12.96%)</td><td>0.31 (+5.97%)</td><td>0.28 (+3.32%)</td><td>0.08 <b>(+60.56%)</b></td><td>232.40 (-3.21%)</td><td>190.04 (-9.60%)</td><td>208.60 (-5.61%)</td><td>143.50 (-15.64%)</td><td>41.56 <b>(+26.48%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>240.10 (n/a)</td><td>210.22 (n/a)</td><td>221.00 (n/a)</td><td>170.10 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.49 (+12.31%)</td><td>0.40 <b>(+21.32%)</b></td><td>0.39 (+10.63%)</td><td>0.37 <b>(+82.67%)</b></td><td>0.05 <b>(-44.94%)</b></td><td>176.90 <b>(-45.25%)</b></td><td>163.54 <b>(-22.03%)</b></td><td>167.80 (-9.59%)</td><td>134.60 (-10.98%)</td><td>16.60 <b>(-75.09%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>323.10 (n/a)</td><td>209.76 (n/a)</td><td>185.60 (n/a)</td><td>151.20 (n/a)</td><td>66.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.02 (+5.30%)</td><td>0.90 (+12.27%)</td><td>1.00 <b>(+28.09%)</b></td><td>0.70 (+1.86%)</td><td>0.15 <b>(+46.11%)</b></td><td>187.60 (-1.83%)</td><td>148.84 (-9.86%)</td><td>130.80 <b>(-21.96%)</b></td><td>128.80 (-5.01%)</td><td>27.03 <b>(+35.20%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.97 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.10 (n/a)</td><td>191.10 (n/a)</td><td>165.12 (n/a)</td><td>167.60 (n/a)</td><td>135.60 (n/a)</td><td>19.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.87 (+0.42%)</td><td>0.68 (-2.66%)</td><td>0.67 (-1.78%)</td><td>0.49 (-6.26%)</td><td>0.13 (+9.38%)</td><td>265.20 (+6.68%)</td><td>198.96 (+3.44%)</td><td>195.40 (+1.82%)</td><td>151.00 (-0.40%)</td><td>41.74 (+16.57%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.86 (n/a)</td><td>0.70 (n/a)</td><td>0.68 (n/a)</td><td>0.53 (n/a)</td><td>0.12 (n/a)</td><td>248.60 (n/a)</td><td>192.34 (n/a)</td><td>191.90 (n/a)</td><td>151.60 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>1.10 <b>(+52.39%)</b></td><td>0.89 <b>(+38.60%)</b></td><td>0.96 <b>(+50.49%)</b></td><td>0.66 (+17.28%)</td><td>0.19 <b>(+223.04%)</b></td><td>198.60 (-14.76%)</td><td>152.60 <b>(-25.48%)</b></td><td>137.10 <b>(-33.58%)</b></td><td>118.70 <b>(-34.38%)</b></td><td>34.65 <b>(+82.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.72 (n/a)</td><td>0.64 (n/a)</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.06 (n/a)</td><td>233.00 (n/a)</td><td>204.78 (n/a)</td><td>206.40 (n/a)</td><td>180.90 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.89 (+13.00%)</td><td>0.79 (+19.48%)</td><td>0.84 <b>(+27.91%)</b></td><td>0.63 (+15.62%)</td><td>0.12 <b>(+21.88%)</b></td><td>208.20 (-13.50%)</td><td>168.82 (-16.13%)</td><td>155.90 <b>(-21.82%)</b></td><td>147.00 (-11.50%)</td><td>27.01 (-8.15%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.79 (n/a)</td><td>0.66 (n/a)</td><td>0.66 (n/a)</td><td>0.54 (n/a)</td><td>0.10 (n/a)</td><td>240.70 (n/a)</td><td>201.28 (n/a)</td><td>199.40 (n/a)</td><td>166.10 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:04:24</td><td>0.11 (+2.14%)</td><td>0.09 (-2.48%)</td><td>0.09 (-8.38%)</td><td>0.07 (+4.79%)</td><td>0.02 (+19.26%)</td><td>234.60 (-4.56%)</td><td>185.96 (+3.31%)</td><td>187.20 (+9.15%)</td><td>143.80 (-2.11%)</td><td>39.81 (+4.35%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.80 (n/a)</td><td>180.00 (n/a)</td><td>171.50 (n/a)</td><td>146.90 (n/a)</td><td>38.15 (n/a)</td>
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
