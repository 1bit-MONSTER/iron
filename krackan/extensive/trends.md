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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (-2.25%)</td><td>0.04 (+0.77%)</td><td>0.04 (+0.71%)</td><td>0.03 (+5.82%)</td><td>0.01 (-3.07%)</td><td>196.10 (-5.49%)</td><td>161.24 (-1.03%)</td><td>162.10 (-0.73%)</td><td>127.00 (+2.25%)</td><td>29.63 (-6.13%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>162.92 (n/a)</td><td>163.30 (n/a)</td><td>124.20 (n/a)</td><td>31.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 <b>(+26.74%)</b></td><td>0.04 <b>(+30.12%)</b></td><td>0.04 <b>(+26.38%)</b></td><td>0.04 <b>(+40.05%)</b></td><td>0.01 (-3.68%)</td><td>172.50 <b>(-28.63%)</b></td><td>151.32 <b>(-23.99%)</b></td><td>146.00 <b>(-20.87%)</b></td><td>128.00 <b>(-21.09%)</b></td><td>18.60 <b>(-45.96%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>199.08 (n/a)</td><td>184.50 (n/a)</td><td>162.20 (n/a)</td><td>34.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 <b>(-22.22%)</b></td><td>0.04 (-9.75%)</td><td>0.04 (-2.29%)</td><td>0.03 (-4.51%)</td><td>0.01 <b>(-35.31%)</b></td><td>213.70 (+4.70%)</td><td>169.12 (+8.56%)</td><td>168.80 (+2.37%)</td><td>135.60 <b>(+28.53%)</b></td><td>32.14 (-12.41%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>155.78 (n/a)</td><td>164.90 (n/a)</td><td>105.50 (n/a)</td><td>36.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (+9.79%)</td><td>0.04 <b>(+20.02%)</b></td><td>0.04 <b>(+30.32%)</b></td><td>0.03 (-1.08%)</td><td>0.01 (+11.71%)</td><td>204.40 (+1.09%)</td><td>148.18 (-16.14%)</td><td>146.90 <b>(-23.29%)</b></td><td>105.90 (-8.94%)</td><td>37.25 (+5.57%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>176.70 (n/a)</td><td>191.50 (n/a)</td><td>116.30 (n/a)</td><td>35.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (+19.14%)</td><td>0.04 (+14.75%)</td><td>0.04 (+10.85%)</td><td>0.03 (-0.83%)</td><td>0.01 <b>(+116.58%)</b></td><td>196.70 (+0.82%)</td><td>157.46 (-11.67%)</td><td>158.10 (-9.76%)</td><td>134.90 (-16.05%)</td><td>24.68 <b>(+81.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>178.26 (n/a)</td><td>175.20 (n/a)</td><td>160.70 (n/a)</td><td>13.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (+10.65%)</td><td>0.04 (+0.63%)</td><td>0.04 (-2.75%)</td><td>0.03 (-9.37%)</td><td>0.00 <b>(+99.13%)</b></td><td>190.10 (+10.39%)</td><td>160.18 (+0.26%)</td><td>159.00 (+2.85%)</td><td>135.00 (-9.64%)</td><td>19.62 <b>(+99.08%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>172.20 (n/a)</td><td>159.76 (n/a)</td><td>154.60 (n/a)</td><td>149.40 (n/a)</td><td>9.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (+4.14%)</td><td>0.04 (+2.06%)</td><td>0.04 (+10.07%)</td><td>0.03 (-8.41%)</td><td>0.01 <b>(+32.63%)</b></td><td>212.10 (+9.16%)</td><td>179.06 (-0.94%)</td><td>172.40 (-9.12%)</td><td>138.30 (-3.96%)</td><td>29.77 <b>(+42.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>180.76 (n/a)</td><td>189.70 (n/a)</td><td>144.00 (n/a)</td><td>20.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 <b>(+25.89%)</b></td><td>0.04 <b>(+25.44%)</b></td><td>0.04 <b>(+30.50%)</b></td><td>0.03 (+16.86%)</td><td>0.01 <b>(+79.75%)</b></td><td>185.30 (-14.41%)</td><td>153.16 (-19.06%)</td><td>149.20 <b>(-23.37%)</b></td><td>123.00 <b>(-20.54%)</b></td><td>28.31 <b>(+25.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>216.50 (n/a)</td><td>189.22 (n/a)</td><td>194.70 (n/a)</td><td>154.80 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (+9.87%)</td><td>0.08 (+6.50%)</td><td>0.08 (+4.63%)</td><td>0.06 (+14.79%)</td><td>0.01 (+6.43%)</td><td>213.80 (-12.88%)</td><td>168.08 (-6.48%)</td><td>159.40 (-4.38%)</td><td>131.10 (-8.96%)</td><td>31.52 (-18.42%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>245.40 (n/a)</td><td>179.72 (n/a)</td><td>166.70 (n/a)</td><td>144.00 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (+17.04%)</td><td>0.08 (+12.02%)</td><td>0.07 (-0.26%)</td><td>0.07 <b>(+20.16%)</b></td><td>0.01 (+12.52%)</td><td>179.10 (-16.78%)</td><td>157.16 (-10.94%)</td><td>165.40 (+0.30%)</td><td>122.50 (-14.52%)</td><td>22.25 <b>(-22.05%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>176.46 (n/a)</td><td>164.90 (n/a)</td><td>143.30 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 <b>(+23.03%)</b></td><td>0.07 (+5.54%)</td><td>0.08 (+6.61%)</td><td>0.04 <b>(-23.56%)</b></td><td>0.02 <b>(+128.49%)</b></td><td>296.00 <b>(+30.80%)</b></td><td>180.34 (+1.89%)</td><td>157.30 (-6.20%)</td><td>126.20 (-18.74%)</td><td>68.24 <b>(+142.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>177.00 (n/a)</td><td>167.70 (n/a)</td><td>155.30 (n/a)</td><td>28.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (+19.53%)</td><td>0.09 <b>(+27.38%)</b></td><td>0.08 (+15.16%)</td><td>0.08 <b>(+64.67%)</b></td><td>0.01 <b>(-20.92%)</b></td><td>159.60 <b>(-39.27%)</b></td><td>144.56 <b>(-23.63%)</b></td><td>153.50 (-13.13%)</td><td>118.60 (-16.36%)</td><td>17.80 <b>(-60.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>262.80 (n/a)</td><td>189.30 (n/a)</td><td>176.70 (n/a)</td><td>141.80 (n/a)</td><td>45.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (-1.07%)</td><td>0.08 (+14.27%)</td><td>0.07 (+5.10%)</td><td>0.07 <b>(+51.82%)</b></td><td>0.01 <b>(-38.94%)</b></td><td>180.40 <b>(-34.14%)</b></td><td>159.34 (-17.11%)</td><td>166.50 (-4.86%)</td><td>122.50 (+1.16%)</td><td>22.95 <b>(-59.91%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>273.90 (n/a)</td><td>192.22 (n/a)</td><td>175.00 (n/a)</td><td>121.10 (n/a)</td><td>57.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (-5.45%)</td><td>0.07 (+1.23%)</td><td>0.08 (+6.73%)</td><td>0.05 <b>(+22.39%)</b></td><td>0.02 <b>(-23.41%)</b></td><td>240.00 (-18.28%)</td><td>180.52 (-4.81%)</td><td>162.20 (-6.30%)</td><td>135.00 (+5.80%)</td><td>41.27 <b>(-35.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>293.70 (n/a)</td><td>189.64 (n/a)</td><td>173.10 (n/a)</td><td>127.60 (n/a)</td><td>63.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 <b>(+59.13%)</b></td><td>0.08 <b>(+27.84%)</b></td><td>0.07 <b>(+27.68%)</b></td><td>0.06 (+15.90%)</td><td>0.02 <b>(+184.13%)</b></td><td>198.40 (-13.74%)</td><td>165.84 (-19.08%)</td><td>168.60 <b>(-21.69%)</b></td><td>112.10 <b>(-37.16%)</b></td><td>35.95 <b>(+58.00%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.00 (n/a)</td><td>204.94 (n/a)</td><td>215.30 (n/a)</td><td>178.40 (n/a)</td><td>22.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (-3.35%)</td><td>0.07 (+11.09%)</td><td>0.06 (+12.02%)</td><td>0.06 <b>(+29.00%)</b></td><td>0.01 <b>(-41.34%)</b></td><td>211.20 <b>(-22.50%)</b></td><td>188.84 (-12.09%)</td><td>191.30 (-10.69%)</td><td>162.30 (+3.44%)</td><td>20.35 <b>(-52.27%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>272.50 (n/a)</td><td>214.80 (n/a)</td><td>214.20 (n/a)</td><td>156.90 (n/a)</td><td>42.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (+14.18%)</td><td>0.17 (+6.55%)</td><td>0.18 <b>(+20.99%)</b></td><td>0.12 (-4.89%)</td><td>0.04 <b>(+41.69%)</b></td><td>207.40 (+5.17%)</td><td>150.98 (-3.90%)</td><td>134.90 (-17.39%)</td><td>109.50 (-12.40%)</td><td>39.08 <b>(+35.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.20 (n/a)</td><td>157.10 (n/a)</td><td>163.30 (n/a)</td><td>125.00 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 <b>(+39.58%)</b></td><td>0.17 <b>(+34.57%)</b></td><td>0.19 <b>(+41.36%)</b></td><td>0.13 <b>(+26.73%)</b></td><td>0.04 <b>(+104.03%)</b></td><td>193.10 <b>(-21.09%)</b></td><td>146.88 <b>(-24.01%)</b></td><td>132.20 <b>(-29.23%)</b></td><td>117.20 <b>(-28.32%)</b></td><td>33.92 (+10.71%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>244.70 (n/a)</td><td>193.28 (n/a)</td><td>186.80 (n/a)</td><td>163.50 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 <b>(+36.62%)</b></td><td>0.15 (+14.60%)</td><td>0.14 (+1.22%)</td><td>0.11 <b>(+23.10%)</b></td><td>0.03 <b>(+59.00%)</b></td><td>216.10 (-18.76%)</td><td>172.22 (-11.59%)</td><td>173.90 (-1.25%)</td><td>125.50 <b>(-26.82%)</b></td><td>37.98 (-6.04%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>266.00 (n/a)</td><td>194.80 (n/a)</td><td>176.10 (n/a)</td><td>171.50 (n/a)</td><td>40.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (+16.11%)</td><td>0.14 (-5.76%)</td><td>0.13 (-10.46%)</td><td>0.08 <b>(-44.01%)</b></td><td>0.06 <b>(+249.51%)</b></td><td>318.20 <b>(+78.56%)</b></td><td>202.24 <b>(+20.60%)</b></td><td>193.60 (+11.65%)</td><td>120.30 (-13.89%)</td><td>83.21 <b>(+423.15%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>178.20 (n/a)</td><td>167.70 (n/a)</td><td>173.40 (n/a)</td><td>139.70 (n/a)</td><td>15.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (+6.27%)</td><td>0.15 (-4.33%)</td><td>0.16 (+0.45%)</td><td>0.08 <b>(-35.16%)</b></td><td>0.04 <b>(+86.89%)</b></td><td>294.10 <b>(+54.22%)</b></td><td>180.14 (+12.35%)</td><td>150.50 (-0.40%)</td><td>122.70 (-5.90%)</td><td>67.79 <b>(+179.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.70 (n/a)</td><td>160.34 (n/a)</td><td>151.10 (n/a)</td><td>130.40 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 <b>(+25.11%)</b></td><td>0.16 (+0.82%)</td><td>0.16 (-4.85%)</td><td>0.10 (-16.10%)</td><td>0.05 <b>(+119.03%)</b></td><td>244.60 (+19.20%)</td><td>165.90 (+5.64%)</td><td>152.80 (+5.16%)</td><td>113.90 <b>(-20.07%)</b></td><td>54.78 <b>(+102.55%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>205.20 (n/a)</td><td>157.04 (n/a)</td><td>145.30 (n/a)</td><td>142.50 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (+0.87%)</td><td>0.13 (-3.60%)</td><td>0.12 (-9.10%)</td><td>0.11 (-7.51%)</td><td>0.03 (+14.14%)</td><td>234.00 (+8.08%)</td><td>191.22 (+4.64%)</td><td>200.40 (+9.99%)</td><td>135.50 (-0.88%)</td><td>36.04 <b>(+20.59%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.50 (n/a)</td><td>182.74 (n/a)</td><td>182.20 (n/a)</td><td>136.70 (n/a)</td><td>29.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (+18.81%)</td><td>0.14 (+16.79%)</td><td>0.13 (+6.23%)</td><td>0.10 <b>(+34.49%)</b></td><td>0.05 (+5.73%)</td><td>235.00 <b>(-25.63%)</b></td><td>183.58 (-17.27%)</td><td>190.10 (-5.89%)</td><td>109.90 (-15.85%)</td><td>49.64 <b>(-37.14%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>316.00 (n/a)</td><td>221.90 (n/a)</td><td>202.00 (n/a)</td><td>130.60 (n/a)</td><td>78.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.40 (-3.63%)</td><td>0.30 (-5.12%)</td><td>0.36 <b>(+27.99%)</b></td><td>0.14 <b>(-49.31%)</b></td><td>0.11 <b>(+84.43%)</b></td><td>349.20 <b>(+97.29%)</b></td><td>188.12 (+19.61%)</td><td>136.00 <b>(-21.88%)</b></td><td>124.20 (+3.76%)</td><td>95.19 <b>(+267.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>177.00 (n/a)</td><td>157.28 (n/a)</td><td>174.10 (n/a)</td><td>119.70 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 (-17.37%)</td><td>0.28 (-16.87%)</td><td>0.28 (-12.82%)</td><td>0.23 <b>(-20.75%)</b></td><td>0.03 <b>(-20.62%)</b></td><td>212.20 <b>(+26.23%)</b></td><td>178.94 <b>(+20.29%)</b></td><td>173.60 (+14.66%)</td><td>158.80 <b>(+21.04%)</b></td><td>20.80 <b>(+24.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>168.10 (n/a)</td><td>148.76 (n/a)</td><td>151.40 (n/a)</td><td>131.20 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.40 <b>(+36.95%)</b></td><td>0.30 (+17.80%)</td><td>0.26 (-5.28%)</td><td>0.22 (+10.39%)</td><td>0.08 <b>(+116.56%)</b></td><td>225.20 (-9.41%)</td><td>172.54 (-11.83%)</td><td>187.60 (+5.57%)</td><td>123.00 <b>(-27.00%)</b></td><td>44.74 <b>(+36.58%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>248.60 (n/a)</td><td>195.70 (n/a)</td><td>177.70 (n/a)</td><td>168.50 (n/a)</td><td>32.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.45 <b>(+29.09%)</b></td><td>0.31 (+15.51%)</td><td>0.29 (+9.32%)</td><td>0.24 (+17.90%)</td><td>0.08 <b>(+45.38%)</b></td><td>201.00 (-15.19%)</td><td>165.18 (-12.58%)</td><td>171.80 (-8.52%)</td><td>109.70 <b>(-22.53%)</b></td><td>33.52 (-9.66%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>237.00 (n/a)</td><td>188.94 (n/a)</td><td>187.80 (n/a)</td><td>141.60 (n/a)</td><td>37.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 (-13.24%)</td><td>0.28 (-3.18%)</td><td>0.28 (-4.30%)</td><td>0.25 (+15.51%)</td><td>0.02 <b>(-59.04%)</b></td><td>195.60 (-13.41%)</td><td>176.96 (+0.84%)</td><td>175.90 (+4.52%)</td><td>157.50 (+15.22%)</td><td>13.71 <b>(-59.61%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>225.90 (n/a)</td><td>175.48 (n/a)</td><td>168.30 (n/a)</td><td>136.70 (n/a)</td><td>33.95 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.35 (-5.37%)</td><td>0.28 (+3.35%)</td><td>0.26 (-5.97%)</td><td>0.21 (+16.38%)</td><td>0.07 (-2.76%)</td><td>234.90 (-14.08%)</td><td>183.50 (-4.12%)</td><td>190.20 (+6.32%)</td><td>139.60 (+5.68%)</td><td>42.82 (-17.11%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>273.40 (n/a)</td><td>191.38 (n/a)</td><td>178.90 (n/a)</td><td>132.10 (n/a)</td><td>51.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (+19.55%)</td><td>0.25 (+9.70%)</td><td>0.25 (+9.66%)</td><td>0.19 (-12.59%)</td><td>0.04 <b>(+320.25%)</b></td><td>259.70 (+14.41%)</td><td>199.74 (-6.95%)</td><td>194.00 (-8.79%)</td><td>170.80 (-16.36%)</td><td>35.39 <b>(+308.10%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>214.66 (n/a)</td><td>212.70 (n/a)</td><td>204.20 (n/a)</td><td>8.67 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.33 (+12.09%)</td><td>0.25 (+0.83%)</td><td>0.23 (-2.82%)</td><td>0.15 <b>(-32.37%)</b></td><td>0.08 <b>(+148.02%)</b></td><td>338.60 <b>(+47.86%)</b></td><td>213.28 (+6.91%)</td><td>211.40 (+2.92%)</td><td>148.40 (-10.76%)</td><td>76.23 <b>(+228.23%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>229.00 (n/a)</td><td>199.50 (n/a)</td><td>205.40 (n/a)</td><td>166.30 (n/a)</td><td>23.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (+19.42%)</td><td>0.02 (+7.80%)</td><td>0.02 (+3.85%)</td><td>0.01 (+5.61%)</td><td>0.00 <b>(+60.82%)</b></td><td>194.20 (-5.31%)</td><td>154.70 (-5.71%)</td><td>154.00 (-3.69%)</td><td>118.00 (-16.25%)</td><td>31.01 <b>(+24.89%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>164.06 (n/a)</td><td>159.90 (n/a)</td><td>140.90 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (+16.78%)</td><td>0.02 <b>(+30.33%)</b></td><td>0.02 <b>(+27.40%)</b></td><td>0.02 <b>(+58.17%)</b></td><td>0.00 <b>(-40.44%)</b></td><td>144.50 <b>(-36.79%)</b></td><td>133.10 <b>(-25.01%)</b></td><td>137.10 <b>(-21.48%)</b></td><td>116.40 (-14.35%)</td><td>10.73 <b>(-68.28%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>228.60 (n/a)</td><td>177.48 (n/a)</td><td>174.60 (n/a)</td><td>135.90 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (-10.02%)</td><td>0.02 (+4.06%)</td><td>0.02 (+0.47%)</td><td>0.01 <b>(+34.98%)</b></td><td>0.00 <b>(-58.73%)</b></td><td>194.80 <b>(-25.93%)</b></td><td>172.90 (-8.35%)</td><td>165.70 (-0.48%)</td><td>152.70 (+11.14%)</td><td>17.41 <b>(-66.17%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>263.00 (n/a)</td><td>188.66 (n/a)</td><td>166.50 (n/a)</td><td>137.40 (n/a)</td><td>51.46 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (-10.81%)</td><td>0.02 (-11.41%)</td><td>0.01 (-17.94%)</td><td>0.01 (-0.96%)</td><td>0.00 <b>(-35.89%)</b></td><td>203.80 (+0.99%)</td><td>176.58 (+10.57%)</td><td>181.60 <b>(+21.88%)</b></td><td>140.00 (+12.09%)</td><td>25.42 <b>(-28.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>201.80 (n/a)</td><td>159.70 (n/a)</td><td>149.00 (n/a)</td><td>124.90 (n/a)</td><td>35.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 <b>(-26.96%)</b></td><td>0.01 (-5.95%)</td><td>0.01 (+8.15%)</td><td>0.01 (-3.64%)</td><td>0.00 <b>(-61.75%)</b></td><td>218.00 (+3.76%)</td><td>183.44 (+3.06%)</td><td>175.40 (-7.54%)</td><td>165.90 <b>(+36.88%)</b></td><td>20.24 <b>(-43.91%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>210.10 (n/a)</td><td>178.00 (n/a)</td><td>189.70 (n/a)</td><td>121.20 (n/a)</td><td>36.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 <b>(-24.20%)</b></td><td>0.01 (-7.44%)</td><td>0.02 (+1.39%)</td><td>0.01 (-1.34%)</td><td>0.00 <b>(-52.29%)</b></td><td>208.40 (+1.36%)</td><td>179.52 (+5.04%)</td><td>173.30 (-1.37%)</td><td>149.90 <b>(+31.84%)</b></td><td>23.42 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>170.90 (n/a)</td><td>175.70 (n/a)</td><td>113.70 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.01 (-10.43%)</td><td>0.01 (-8.94%)</td><td>0.01 (-10.69%)</td><td>0.01 (-0.01%)</td><td>0.00 <b>(-38.59%)</b></td><td>233.10 (+0.00%)</td><td>202.88 (+8.95%)</td><td>195.60 (+11.96%)</td><td>190.40 (+11.67%)</td><td>17.80 <b>(-32.45%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.10 (n/a)</td><td>186.22 (n/a)</td><td>174.70 (n/a)</td><td>170.50 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.01 <b>(-38.92%)</b></td><td>0.01 <b>(-27.65%)</b></td><td>0.01 (-13.99%)</td><td>0.01 <b>(-38.47%)</b></td><td>0.00 <b>(-37.46%)</b></td><td>336.70 <b>(+62.50%)</b></td><td>253.40 <b>(+38.33%)</b></td><td>225.70 (+16.22%)</td><td>222.20 <b>(+63.74%)</b></td><td>49.22 <b>(+65.26%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>207.20 (n/a)</td><td>183.18 (n/a)</td><td>194.20 (n/a)</td><td>135.70 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-2.75%)</td><td>0.03 (+9.78%)</td><td>0.03 (+1.17%)</td><td>0.03 <b>(+95.93%)</b></td><td>0.00 <b>(-69.70%)</b></td><td>188.00 <b>(-48.97%)</b></td><td>175.62 (-17.17%)</td><td>175.80 (-1.18%)</td><td>155.00 (+2.85%)</td><td>13.27 <b>(-85.08%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>368.40 (n/a)</td><td>212.02 (n/a)</td><td>177.90 (n/a)</td><td>150.70 (n/a)</td><td>88.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (+2.03%)</td><td>0.03 (-1.56%)</td><td>0.03 (+6.00%)</td><td>0.02 (-10.21%)</td><td>0.01 <b>(+22.81%)</b></td><td>212.70 (+11.36%)</td><td>175.90 (+2.47%)</td><td>173.80 (-5.65%)</td><td>138.40 (-1.98%)</td><td>29.23 <b>(+33.43%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.00 (n/a)</td><td>171.66 (n/a)</td><td>184.20 (n/a)</td><td>141.20 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-13.20%)</td><td>0.03 (-12.68%)</td><td>0.03 (-5.20%)</td><td>0.02 <b>(-29.19%)</b></td><td>0.00 <b>(+29.27%)</b></td><td>307.90 <b>(+41.24%)</b></td><td>217.24 (+17.22%)</td><td>198.70 (+5.52%)</td><td>184.50 (+15.24%)</td><td>51.73 <b>(+117.63%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>185.32 (n/a)</td><td>188.30 (n/a)</td><td>160.10 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 <b>(+23.58%)</b></td><td>0.03 (-2.88%)</td><td>0.03 (-5.87%)</td><td>0.02 (-16.59%)</td><td>0.01 <b>(+164.84%)</b></td><td>236.10 (+19.91%)</td><td>191.92 (+6.30%)</td><td>199.40 (+6.23%)</td><td>131.50 (-19.08%)</td><td>38.07 <b>(+147.38%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>196.90 (n/a)</td><td>180.54 (n/a)</td><td>187.70 (n/a)</td><td>162.50 (n/a)</td><td>15.39 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (-17.23%)</td><td>0.03 (-1.98%)</td><td>0.03 (+2.90%)</td><td>0.02 (+10.69%)</td><td>0.01 <b>(-37.52%)</b></td><td>214.10 (-9.66%)</td><td>181.90 (-1.71%)</td><td>188.60 (-2.78%)</td><td>131.20 <b>(+20.81%)</b></td><td>34.94 <b>(-26.56%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>185.06 (n/a)</td><td>194.00 (n/a)</td><td>108.60 (n/a)</td><td>47.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (+14.85%)</td><td>0.03 (+7.10%)</td><td>0.03 (-1.19%)</td><td>0.02 (-1.73%)</td><td>0.01 <b>(+40.06%)</b></td><td>220.60 (+1.75%)</td><td>172.56 (-5.38%)</td><td>171.10 (+1.18%)</td><td>131.60 (-12.91%)</td><td>35.27 <b>(+20.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.80 (n/a)</td><td>182.38 (n/a)</td><td>169.10 (n/a)</td><td>151.10 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (-5.45%)</td><td>0.03 (+6.02%)</td><td>0.03 (+15.57%)</td><td>0.02 (+11.46%)</td><td>0.00 (-18.19%)</td><td>213.40 (-10.30%)</td><td>177.68 (-6.74%)</td><td>173.70 (-13.45%)</td><td>148.60 (+5.77%)</td><td>28.88 <b>(-21.88%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.90 (n/a)</td><td>190.52 (n/a)</td><td>200.70 (n/a)</td><td>140.50 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+8.63%)</td><td>0.03 (+0.14%)</td><td>0.02 (-0.44%)</td><td>0.02 (-4.48%)</td><td>0.00 <b>(+59.47%)</b></td><td>232.40 (+4.68%)</td><td>212.48 (+0.70%)</td><td>220.70 (+0.46%)</td><td>166.50 (-7.96%)</td><td>26.17 <b>(+50.30%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.00 (n/a)</td><td>211.00 (n/a)</td><td>219.70 (n/a)</td><td>180.90 (n/a)</td><td>17.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (+3.78%)</td><td>0.07 (+5.87%)</td><td>0.06 (-0.24%)</td><td>0.06 <b>(+20.56%)</b></td><td>0.01 (-2.44%)</td><td>175.80 (-17.04%)</td><td>154.62 (-6.18%)</td><td>172.50 (+0.23%)</td><td>121.60 (-3.65%)</td><td>26.30 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>211.90 (n/a)</td><td>164.80 (n/a)</td><td>172.10 (n/a)</td><td>126.20 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(-24.41%)</b></td><td>0.06 (-8.65%)</td><td>0.06 (+3.34%)</td><td>0.03 (-7.45%)</td><td>0.01 <b>(-32.23%)</b></td><td>304.80 (+8.05%)</td><td>197.68 (+6.87%)</td><td>169.30 (-3.20%)</td><td>150.50 <b>(+32.37%)</b></td><td>62.02 (+0.44%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>282.10 (n/a)</td><td>184.98 (n/a)</td><td>174.90 (n/a)</td><td>113.70 (n/a)</td><td>61.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 <b>(+23.66%)</b></td><td>0.06 (+16.33%)</td><td>0.06 (+4.93%)</td><td>0.05 <b>(+21.26%)</b></td><td>0.01 <b>(+34.21%)</b></td><td>200.60 (-17.52%)</td><td>168.04 (-13.57%)</td><td>176.90 (-4.74%)</td><td>125.90 (-19.09%)</td><td>32.23 (-10.47%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>243.20 (n/a)</td><td>194.42 (n/a)</td><td>185.70 (n/a)</td><td>155.60 (n/a)</td><td>36.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(-26.71%)</b></td><td>0.06 (-0.44%)</td><td>0.06 (+5.41%)</td><td>0.05 <b>(+41.20%)</b></td><td>0.01 <b>(-75.39%)</b></td><td>195.20 <b>(-29.17%)</b></td><td>177.06 (-7.41%)</td><td>181.50 (-5.17%)</td><td>157.60 <b>(+36.45%)</b></td><td>14.56 <b>(-76.07%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>275.60 (n/a)</td><td>191.22 (n/a)</td><td>191.40 (n/a)</td><td>115.50 (n/a)</td><td>60.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 <b>(+51.27%)</b></td><td>0.07 (+15.91%)</td><td>0.05 (-12.98%)</td><td>0.05 (+11.27%)</td><td>0.02 <b>(+209.21%)</b></td><td>205.00 (-10.13%)</td><td>168.46 (-8.38%)</td><td>201.40 (+14.95%)</td><td>110.00 <b>(-33.89%)</b></td><td>47.13 <b>(+86.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>183.86 (n/a)</td><td>175.20 (n/a)</td><td>166.40 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (-15.09%)</td><td>0.06 (-4.70%)</td><td>0.06 (+3.10%)</td><td>0.05 (-9.44%)</td><td>0.01 <b>(-20.64%)</b></td><td>219.00 (+10.44%)</td><td>179.18 (+4.51%)</td><td>175.10 (-2.99%)</td><td>154.40 (+17.77%)</td><td>27.34 (+2.19%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>171.44 (n/a)</td><td>180.50 (n/a)</td><td>131.10 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 <b>(+94.86%)</b></td><td>0.06 <b>(+29.44%)</b></td><td>0.06 <b>(+23.03%)</b></td><td>0.04 (-3.85%)</td><td>0.02 <b>(+724.79%)</b></td><td>257.20 (+4.00%)</td><td>191.72 (-16.67%)</td><td>190.20 (-18.72%)</td><td>110.90 <b>(-48.68%)</b></td><td>53.14 <b>(+318.30%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>247.30 (n/a)</td><td>230.08 (n/a)</td><td>234.00 (n/a)</td><td>216.10 (n/a)</td><td>12.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (-6.04%)</td><td>0.05 (-1.16%)</td><td>0.05 (-3.77%)</td><td>0.05 (+12.27%)</td><td>0.00 <b>(-71.76%)</b></td><td>231.20 (-10.91%)</td><td>223.06 (+0.50%)</td><td>222.90 (+3.92%)</td><td>214.80 (+6.39%)</td><td>5.81 <b>(-73.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>259.50 (n/a)</td><td>221.96 (n/a)</td><td>214.50 (n/a)</td><td>201.90 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 <b>(-34.83%)</b></td><td>0.12 (-12.05%)</td><td>0.12 (-13.43%)</td><td>0.11 (+12.09%)</td><td>0.01 <b>(-83.35%)</b></td><td>186.00 (-10.79%)</td><td>172.68 (+7.59%)</td><td>171.70 (+15.55%)</td><td>161.90 <b>(+53.46%)</b></td><td>9.27 <b>(-77.43%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>208.50 (n/a)</td><td>160.50 (n/a)</td><td>148.60 (n/a)</td><td>105.50 (n/a)</td><td>41.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 <b>(+37.16%)</b></td><td>0.15 <b>(+20.42%)</b></td><td>0.13 (+6.10%)</td><td>0.12 <b>(+25.32%)</b></td><td>0.04 <b>(+76.94%)</b></td><td>170.90 <b>(-20.21%)</b></td><td>148.98 (-15.13%)</td><td>163.90 (-5.75%)</td><td>95.40 <b>(-27.06%)</b></td><td>31.42 (+3.45%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>175.54 (n/a)</td><td>173.90 (n/a)</td><td>130.80 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 <b>(+25.53%)</b></td><td>0.12 (+18.40%)</td><td>0.12 (+10.58%)</td><td>0.09 <b>(+33.43%)</b></td><td>0.02 (+4.07%)</td><td>226.80 <b>(-25.07%)</b></td><td>182.24 (-16.56%)</td><td>182.50 (-9.56%)</td><td>146.10 <b>(-20.38%)</b></td><td>30.41 <b>(-38.36%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>302.70 (n/a)</td><td>218.42 (n/a)</td><td>201.80 (n/a)</td><td>183.50 (n/a)</td><td>49.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 <b>(+49.67%)</b></td><td>0.14 <b>(+21.06%)</b></td><td>0.13 (+11.36%)</td><td>0.09 (-10.51%)</td><td>0.03 <b>(+409.52%)</b></td><td>222.80 (+11.74%)</td><td>159.78 (-13.56%)</td><td>161.90 (-10.21%)</td><td>117.00 <b>(-33.18%)</b></td><td>40.54 <b>(+282.58%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>184.84 (n/a)</td><td>180.30 (n/a)</td><td>175.10 (n/a)</td><td>10.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (+4.10%)</td><td>0.14 (+7.70%)</td><td>0.13 (+6.88%)</td><td>0.12 (+8.41%)</td><td>0.02 (+0.42%)</td><td>180.60 (-7.76%)</td><td>153.64 (-7.30%)</td><td>159.20 (-6.46%)</td><td>128.20 (-3.90%)</td><td>20.42 (-10.78%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>195.80 (n/a)</td><td>165.74 (n/a)</td><td>170.20 (n/a)</td><td>133.40 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (+10.25%)</td><td>0.12 (+11.39%)</td><td>0.13 (+16.37%)</td><td>0.10 (+11.20%)</td><td>0.03 <b>(+23.79%)</b></td><td>208.50 (-10.05%)</td><td>173.64 (-9.49%)</td><td>166.20 (-14.06%)</td><td>131.40 (-9.25%)</td><td>34.09 (+7.61%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>231.80 (n/a)</td><td>191.84 (n/a)</td><td>193.40 (n/a)</td><td>144.80 (n/a)</td><td>31.68 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (+1.75%)</td><td>0.13 (+12.17%)</td><td>0.12 (+3.36%)</td><td>0.11 <b>(+49.60%)</b></td><td>0.02 <b>(-38.75%)</b></td><td>194.00 <b>(-33.17%)</b></td><td>166.46 (-15.34%)</td><td>172.80 (-3.25%)</td><td>131.30 (-1.72%)</td><td>23.29 <b>(-61.35%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>290.30 (n/a)</td><td>196.62 (n/a)</td><td>178.60 (n/a)</td><td>133.60 (n/a)</td><td>60.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (+17.30%)</td><td>0.10 (+5.50%)</td><td>0.11 (+7.77%)</td><td>0.07 <b>(-23.62%)</b></td><td>0.02 <b>(+264.32%)</b></td><td>311.40 <b>(+30.95%)</b></td><td>218.32 (-1.56%)</td><td>198.60 (-7.20%)</td><td>178.80 (-14.74%)</td><td>54.31 <b>(+313.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>221.78 (n/a)</td><td>214.00 (n/a)</td><td>209.70 (n/a)</td><td>13.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>147.74 (n/a)</td><td>133.00 (n/a)</td><td>120.80 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>173.24 (n/a)</td><td>174.70 (n/a)</td><td>144.70 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.00 (n/a)</td><td>177.42 (n/a)</td><td>176.50 (n/a)</td><td>140.60 (n/a)</td><td>38.87 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.00 (n/a)</td><td>185.34 (n/a)</td><td>182.80 (n/a)</td><td>130.50 (n/a)</td><td>42.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>160.48 (n/a)</td><td>156.40 (n/a)</td><td>128.10 (n/a)</td><td>22.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>166.96 (n/a)</td><td>152.40 (n/a)</td><td>132.10 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>264.70 (n/a)</td><td>183.00 (n/a)</td><td>173.00 (n/a)</td><td>132.20 (n/a)</td><td>54.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>176.80 (n/a)</td><td>174.60 (n/a)</td><td>143.70 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.10 (n/a)</td><td>153.62 (n/a)</td><td>145.30 (n/a)</td><td>134.50 (n/a)</td><td>21.87 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.50 (n/a)</td><td>153.12 (n/a)</td><td>149.60 (n/a)</td><td>126.30 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>218.30 (n/a)</td><td>168.84 (n/a)</td><td>168.40 (n/a)</td><td>125.10 (n/a)</td><td>36.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>248.50 (n/a)</td><td>187.78 (n/a)</td><td>167.40 (n/a)</td><td>142.20 (n/a)</td><td>43.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.33 <b>(-27.87%)</b></td><td>0.29 (-16.52%)</td><td>0.28 (-16.48%)</td><td>0.26 (+4.47%)</td><td>0.03 <b>(-63.87%)</b></td><td>189.70 (-4.29%)</td><td>172.50 (+15.68%)</td><td>173.90 (+19.77%)</td><td>148.20 <b>(+38.63%)</b></td><td>16.46 <b>(-52.13%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>198.20 (n/a)</td><td>149.12 (n/a)</td><td>145.20 (n/a)</td><td>106.90 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>171.90 (n/a)</td><td>149.64 (n/a)</td><td>161.40 (n/a)</td><td>118.90 (n/a)</td><td>22.72 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>238.80 (n/a)</td><td>176.98 (n/a)</td><td>163.40 (n/a)</td><td>121.30 (n/a)</td><td>44.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>194.20 (n/a)</td><td>161.28 (n/a)</td><td>170.60 (n/a)</td><td>132.50 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>176.50 (n/a)</td><td>159.54 (n/a)</td><td>165.60 (n/a)</td><td>142.60 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>174.22 (n/a)</td><td>186.20 (n/a)</td><td>117.20 (n/a)</td><td>33.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>175.42 (n/a)</td><td>179.40 (n/a)</td><td>132.00 (n/a)</td><td>32.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>314.80 (n/a)</td><td>214.86 (n/a)</td><td>204.90 (n/a)</td><td>163.60 (n/a)</td><td>59.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>370.70 (n/a)</td><td>205.90 (n/a)</td><td>182.70 (n/a)</td><td>99.90 (n/a)</td><td>100.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>185.40 (n/a)</td><td>166.10 (n/a)</td><td>165.50 (n/a)</td><td>156.00 (n/a)</td><td>11.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>212.00 (n/a)</td><td>178.72 (n/a)</td><td>187.10 (n/a)</td><td>126.20 (n/a)</td><td>31.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>304.00 (n/a)</td><td>214.52 (n/a)</td><td>194.10 (n/a)</td><td>176.00 (n/a)</td><td>51.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>167.10 (n/a)</td><td>170.10 (n/a)</td><td>130.80 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.50 (n/a)</td><td>164.16 (n/a)</td><td>167.50 (n/a)</td><td>132.80 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>194.80 (n/a)</td><td>173.86 (n/a)</td><td>181.80 (n/a)</td><td>142.40 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.40 (n/a)</td><td>177.98 (n/a)</td><td>190.30 (n/a)</td><td>140.60 (n/a)</td><td>34.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>205.50 (n/a)</td><td>170.82 (n/a)</td><td>168.30 (n/a)</td><td>148.10 (n/a)</td><td>21.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>260.00 (n/a)</td><td>206.38 (n/a)</td><td>196.10 (n/a)</td><td>156.40 (n/a)</td><td>40.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>264.70 (n/a)</td><td>194.58 (n/a)</td><td>201.10 (n/a)</td><td>145.90 (n/a)</td><td>49.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>163.80 (n/a)</td><td>165.80 (n/a)</td><td>134.40 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.30 (n/a)</td><td>144.34 (n/a)</td><td>151.40 (n/a)</td><td>98.10 (n/a)</td><td>31.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.40 (n/a)</td><td>186.86 (n/a)</td><td>181.40 (n/a)</td><td>162.20 (n/a)</td><td>25.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.60 (n/a)</td><td>168.98 (n/a)</td><td>172.00 (n/a)</td><td>134.30 (n/a)</td><td>32.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>163.62 (n/a)</td><td>164.70 (n/a)</td><td>135.50 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.70 (n/a)</td><td>166.96 (n/a)</td><td>171.70 (n/a)</td><td>141.70 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>178.16 (n/a)</td><td>167.60 (n/a)</td><td>139.00 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>349.50 (n/a)</td><td>224.48 (n/a)</td><td>200.40 (n/a)</td><td>169.70 (n/a)</td><td>72.28 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>172.50 (n/a)</td><td>178.90 (n/a)</td><td>141.50 (n/a)</td><td>24.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.20 (n/a)</td><td>149.16 (n/a)</td><td>141.40 (n/a)</td><td>124.70 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>165.10 (n/a)</td><td>167.80 (n/a)</td><td>138.00 (n/a)</td><td>20.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>382.90 (n/a)</td><td>206.70 (n/a)</td><td>173.90 (n/a)</td><td>136.10 (n/a)</td><td>99.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>179.04 (n/a)</td><td>178.80 (n/a)</td><td>152.10 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>179.48 (n/a)</td><td>183.40 (n/a)</td><td>133.00 (n/a)</td><td>30.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.30 (n/a)</td><td>200.70 (n/a)</td><td>210.40 (n/a)</td><td>136.50 (n/a)</td><td>43.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>244.90 (n/a)</td><td>231.46 (n/a)</td><td>232.70 (n/a)</td><td>214.60 (n/a)</td><td>13.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>264.00 (n/a)</td><td>190.20 (n/a)</td><td>177.80 (n/a)</td><td>162.30 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>158.64 (n/a)</td><td>150.20 (n/a)</td><td>137.60 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.70 (n/a)</td><td>166.72 (n/a)</td><td>159.80 (n/a)</td><td>134.70 (n/a)</td><td>27.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>188.60 (n/a)</td><td>154.76 (n/a)</td><td>164.70 (n/a)</td><td>109.20 (n/a)</td><td>32.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>168.56 (n/a)</td><td>171.70 (n/a)</td><td>127.30 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>192.88 (n/a)</td><td>185.80 (n/a)</td><td>181.20 (n/a)</td><td>13.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>282.90 (n/a)</td><td>194.54 (n/a)</td><td>178.60 (n/a)</td><td>137.80 (n/a)</td><td>54.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.00 (n/a)</td><td>208.36 (n/a)</td><td>219.30 (n/a)</td><td>154.50 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>199.70 (n/a)</td><td>174.58 (n/a)</td><td>169.40 (n/a)</td><td>155.00 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>318.00 (n/a)</td><td>191.44 (n/a)</td><td>161.10 (n/a)</td><td>135.90 (n/a)</td><td>73.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.00 (n/a)</td><td>167.14 (n/a)</td><td>166.50 (n/a)</td><td>137.10 (n/a)</td><td>24.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>195.20 (n/a)</td><td>171.40 (n/a)</td><td>180.90 (n/a)</td><td>123.10 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>283.00 (n/a)</td><td>204.12 (n/a)</td><td>188.40 (n/a)</td><td>173.20 (n/a)</td><td>44.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>211.10 (n/a)</td><td>190.94 (n/a)</td><td>192.40 (n/a)</td><td>169.50 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>282.10 (n/a)</td><td>189.50 (n/a)</td><td>183.50 (n/a)</td><td>114.10 (n/a)</td><td>60.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>209.70 (n/a)</td><td>215.70 (n/a)</td><td>198.30 (n/a)</td><td>9.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>4.19 (-2.04%)</td><td>4.02 (+4.06%)</td><td>4.11 (-0.28%)</td><td>3.85 (+19.79%)</td><td>0.16 <b>(-67.38%)</b></td><td>2445.80 (-16.52%)</td><td>2340.18 (-5.09%)</td><td>2288.90 (+0.28%)</td><td>2242.30 (+2.08%)</td><td>93.99 <b>(-71.70%)</b></td><td>1649.83 (-2.04%)</td><td>1582.83 (+4.06%)</td><td>1616.23 (-0.28%)</td><td>1512.55 (+19.79%)</td><td>62.96 <b>(-67.38%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.28 (n/a)</td><td>3.87 (n/a)</td><td>4.12 (n/a)</td><td>3.21 (n/a)</td><td>0.49 (n/a)</td><td>2929.70 (n/a)</td><td>2465.66 (n/a)</td><td>2282.50 (n/a)</td><td>2196.60 (n/a)</td><td>332.10 (n/a)</td><td>1684.12 (n/a)</td><td>1521.12 (n/a)</td><td>1620.78 (n/a)</td><td>1262.70 (n/a)</td><td>192.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.04 (-14.16%)</td><td>0.95 (-6.06%)</td><td>0.93 (-3.25%)</td><td>0.82 (-11.46%)</td><td>0.09 <b>(-20.66%)</b></td><td>271.00 (+12.92%)</td><td>234.44 (+6.26%)</td><td>236.70 (+3.36%)</td><td>212.00 (+16.48%)</td><td>24.31 (+3.96%)</td><td>44.51 (-14.16%)</td><td>40.59 (-6.06%)</td><td>39.87 (-3.25%)</td><td>34.82 (-11.46%)</td><td>4.05 <b>(-20.66%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.22 (n/a)</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.92 (n/a)</td><td>0.12 (n/a)</td><td>240.00 (n/a)</td><td>220.62 (n/a)</td><td>229.00 (n/a)</td><td>182.00 (n/a)</td><td>23.38 (n/a)</td><td>51.86 (n/a)</td><td>43.21 (n/a)</td><td>41.21 (n/a)</td><td>39.33 (n/a)</td><td>5.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.21 (-0.42%)</td><td>0.90 (-11.94%)</td><td>1.02 (+0.00%)</td><td>0.60 (-14.69%)</td><td>0.27 <b>(+30.87%)</b></td><td>367.80 (+17.21%)</td><td>265.56 (+18.43%)</td><td>217.50 (+0.00%)</td><td>182.60 (+0.44%)</td><td>86.46 <b>(+61.23%)</b></td><td>51.69 (-0.42%)</td><td>38.54 (-11.94%)</td><td>43.39 (+0.00%)</td><td>25.66 (-14.69%)</td><td>11.60 <b>(+30.87%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.22 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.70 (n/a)</td><td>0.21 (n/a)</td><td>313.80 (n/a)</td><td>224.24 (n/a)</td><td>217.50 (n/a)</td><td>181.80 (n/a)</td><td>53.63 (n/a)</td><td>51.91 (n/a)</td><td>43.76 (n/a)</td><td>43.39 (n/a)</td><td>30.07 (n/a)</td><td>8.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.52 (-0.03%)</td><td>0.52 (+0.05%)</td><td>0.52 (+0.07%)</td><td>0.52 (+0.13%)</td><td>0.00 <b>(-78.06%)</b></td><td>48460.00 (-0.13%)</td><td>48449.92 (-0.05%)</td><td>48450.00 (-0.07%)</td><td>48435.90 (+0.03%)</td><td>8.90 <b>(-78.10%)</b></td><td>354.69 (-0.03%)</td><td>354.59 (+0.05%)</td><td>354.59 (+0.07%)</td><td>354.52 (+0.13%)</td><td>0.07 <b>(-78.07%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48523.30 (n/a)</td><td>48476.00 (n/a)</td><td>48482.90 (n/a)</td><td>48420.00 (n/a)</td><td>40.63 (n/a)</td><td>354.81 (n/a)</td><td>354.40 (n/a)</td><td>354.35 (n/a)</td><td>354.05 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (-1.32%)</td><td>0.21 (-0.35%)</td><td>0.21 (-0.08%)</td><td>0.21 (-0.79%)</td><td>0.00 (-14.21%)</td><td>120861.50 (+0.80%)</td><td>118851.50 (+0.35%)</td><td>118439.60 (+0.08%)</td><td>117964.50 (+1.34%)</td><td>1177.81 (-12.23%)</td><td>145.64 (-1.32%)</td><td>144.56 (-0.35%)</td><td>145.05 (-0.08%)</td><td>142.15 (-0.79%)</td><td>1.42 (-14.20%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119906.10 (n/a)</td><td>118441.72 (n/a)</td><td>118344.50 (n/a)</td><td>116406.10 (n/a)</td><td>1341.88 (n/a)</td><td>147.59 (n/a)</td><td>145.06 (n/a)</td><td>145.17 (n/a)</td><td>143.28 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.89 (-0.32%)</td><td>0.89 (-0.13%)</td><td>0.89 (-0.15%)</td><td>0.89 (+0.26%)</td><td>0.00 <b>(-40.19%)</b></td><td>28370.10 (-0.25%)</td><td>28287.10 (+0.13%)</td><td>28290.50 (+0.15%)</td><td>28190.90 (+0.32%)</td><td>77.48 <b>(-40.17%)</b></td><td>609.41 (-0.32%)</td><td>607.34 (-0.13%)</td><td>607.27 (-0.15%)</td><td>605.56 (+0.26%)</td><td>1.66 <b>(-40.19%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28442.60 (n/a)</td><td>28251.40 (n/a)</td><td>28249.10 (n/a)</td><td>28101.50 (n/a)</td><td>129.51 (n/a)</td><td>611.35 (n/a)</td><td>608.12 (n/a)</td><td>608.16 (n/a)</td><td>604.02 (n/a)</td><td>2.78 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.54 (-0.42%)</td><td>3.46 (+0.50%)</td><td>3.49 (+0.18%)</td><td>3.35 (+2.83%)</td><td>0.09 <b>(-27.96%)</b></td><td>7507.20 (-2.75%)</td><td>7285.68 (-0.55%)</td><td>7200.90 (-0.18%)</td><td>7106.60 (+0.43%)</td><td>188.81 <b>(-29.52%)</b></td><td>2417.47 (-0.42%)</td><td>2359.30 (+0.50%)</td><td>2385.80 (+0.18%)</td><td>2288.45 (+2.83%)</td><td>60.69 <b>(-27.96%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.56 (n/a)</td><td>3.44 (n/a)</td><td>3.49 (n/a)</td><td>3.26 (n/a)</td><td>0.12 (n/a)</td><td>7719.70 (n/a)</td><td>7325.92 (n/a)</td><td>7213.70 (n/a)</td><td>7076.40 (n/a)</td><td>267.87 (n/a)</td><td>2427.78 (n/a)</td><td>2347.54 (n/a)</td><td>2381.57 (n/a)</td><td>2225.45 (n/a)</td><td>84.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.02 (-2.70%)</td><td>2.80 (-5.08%)</td><td>2.76 (-6.13%)</td><td>2.66 (-4.37%)</td><td>0.15 (+15.72%)</td><td>9467.20 (+4.56%)</td><td>9012.80 (+5.43%)</td><td>9119.50 (+6.53%)</td><td>8323.40 (+2.77%)</td><td>476.89 <b>(+24.84%)</b></td><td>2064.05 (-2.70%)</td><td>1910.55 (-5.08%)</td><td>1883.85 (-6.13%)</td><td>1814.67 (-4.37%)</td><td>103.72 (+15.72%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.11 (n/a)</td><td>2.95 (n/a)</td><td>2.94 (n/a)</td><td>2.78 (n/a)</td><td>0.13 (n/a)</td><td>9054.00 (n/a)</td><td>8548.60 (n/a)</td><td>8560.50 (n/a)</td><td>8098.90 (n/a)</td><td>382.00 (n/a)</td><td>2121.25 (n/a)</td><td>2012.87 (n/a)</td><td>2006.88 (n/a)</td><td>1897.49 (n/a)</td><td>89.63 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.31 (-1.29%)</td><td>3.19 (-0.53%)</td><td>3.17 (-0.18%)</td><td>3.14 (-0.40%)</td><td>0.07 (-17.29%)</td><td>8016.10 (+0.40%)</td><td>7891.54 (+0.51%)</td><td>7938.60 (+0.18%)</td><td>7600.30 (+1.30%)</td><td>166.14 (-15.89%)</td><td>2260.41 (-1.29%)</td><td>2177.79 (-0.53%)</td><td>2164.10 (-0.18%)</td><td>2143.16 (-0.40%)</td><td>47.05 (-17.29%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.35 (n/a)</td><td>3.21 (n/a)</td><td>3.18 (n/a)</td><td>3.15 (n/a)</td><td>0.08 (n/a)</td><td>7984.00 (n/a)</td><td>7851.14 (n/a)</td><td>7924.20 (n/a)</td><td>7502.40 (n/a)</td><td>197.53 (n/a)</td><td>2289.92 (n/a)</td><td>2189.35 (n/a)</td><td>2168.02 (n/a)</td><td>2151.79 (n/a)</td><td>56.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.79 (+0.01%)</td><td>0.78 (-0.07%)</td><td>0.78 (-0.12%)</td><td>0.78 (-0.07%)</td><td>0.00 <b>(+27.63%)</b></td><td>96380.50 (+0.07%)</td><td>96221.04 (+0.07%)</td><td>96234.50 (+0.12%)</td><td>96102.90 (-0.01%)</td><td>114.35 <b>(+27.67%)</b></td><td>715.06 (+0.01%)</td><td>714.18 (-0.07%)</td><td>714.08 (-0.12%)</td><td>713.00 (-0.07%)</td><td>0.85 <b>(+27.62%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96317.30 (n/a)</td><td>96158.30 (n/a)</td><td>96116.70 (n/a)</td><td>96110.20 (n/a)</td><td>89.57 (n/a)</td><td>715.01 (n/a)</td><td>714.65 (n/a)</td><td>714.96 (n/a)</td><td>713.47 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.73 (-0.37%)</td><td>0.73 (-0.05%)</td><td>0.73 (-0.01%)</td><td>0.73 (+0.12%)</td><td>0.00 <b>(-92.56%)</b></td><td>103319.90 (-0.12%)</td><td>103306.78 (+0.05%)</td><td>103313.40 (+0.01%)</td><td>103285.20 (+0.37%)</td><td>15.43 <b>(-92.53%)</b></td><td>665.34 (-0.37%)</td><td>665.20 (-0.05%)</td><td>665.16 (-0.01%)</td><td>665.11 (+0.12%)</td><td>0.10 <b>(-92.56%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103447.70 (n/a)</td><td>103255.56 (n/a)</td><td>103304.70 (n/a)</td><td>102902.30 (n/a)</td><td>206.49 (n/a)</td><td>667.81 (n/a)</td><td>665.53 (n/a)</td><td>665.21 (n/a)</td><td>664.29 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.70 (-0.03%)</td><td>0.69 (+0.04%)</td><td>0.69 (-0.04%)</td><td>0.69 (+0.14%)</td><td>0.00 (-16.22%)</td><td>109124.80 (-0.14%)</td><td>108821.16 (-0.04%)</td><td>108888.40 (+0.04%)</td><td>108543.10 (+0.03%)</td><td>228.51 (-16.33%)</td><td>633.11 (-0.03%)</td><td>631.49 (+0.04%)</td><td>631.10 (-0.04%)</td><td>629.73 (+0.14%)</td><td>1.33 (-16.22%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109277.20 (n/a)</td><td>108868.22 (n/a)</td><td>108848.50 (n/a)</td><td>108508.90 (n/a)</td><td>273.12 (n/a)</td><td>633.31 (n/a)</td><td>631.22 (n/a)</td><td>631.33 (n/a)</td><td>628.85 (n/a)</td><td>1.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.17 (-6.27%)</td><td>6.67 (-2.61%)</td><td>6.58 (-3.13%)</td><td>6.06 (-5.70%)</td><td>0.46 (-5.04%)</td><td>1471.10 (+6.04%)</td><td>1341.80 (+2.69%)</td><td>1354.00 (+3.23%)</td><td>1242.70 (+6.70%)</td><td>92.78 (+7.75%)</td><td>432.01 (-6.27%)</td><td>401.63 (-2.61%)</td><td>396.52 (-3.13%)</td><td>364.94 (-5.70%)</td><td>27.44 (-5.04%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.65 (n/a)</td><td>6.85 (n/a)</td><td>6.80 (n/a)</td><td>6.42 (n/a)</td><td>0.48 (n/a)</td><td>1387.30 (n/a)</td><td>1306.70 (n/a)</td><td>1311.60 (n/a)</td><td>1164.70 (n/a)</td><td>86.11 (n/a)</td><td>460.94 (n/a)</td><td>412.38 (n/a)</td><td>409.31 (n/a)</td><td>386.99 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>6.91 (-2.20%)</td><td>6.41 (-6.35%)</td><td>6.86 (-0.35%)</td><td>5.04 <b>(-23.60%)</b></td><td>0.80 <b>(+337.75%)</b></td><td>1770.20 <b>(+30.88%)</b></td><td>1411.42 (+8.29%)</td><td>1299.20 (+0.36%)</td><td>1289.60 (+2.25%)</td><td>205.65 <b>(+487.74%)</b></td><td>416.31 (-2.20%)</td><td>385.98 (-6.35%)</td><td>413.24 (-0.35%)</td><td>303.29 <b>(-23.60%)</b></td><td>48.15 <b>(+337.75%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.07 (n/a)</td><td>6.84 (n/a)</td><td>6.88 (n/a)</td><td>6.59 (n/a)</td><td>0.18 (n/a)</td><td>1352.50 (n/a)</td><td>1303.38 (n/a)</td><td>1294.60 (n/a)</td><td>1261.20 (n/a)</td><td>34.99 (n/a)</td><td>425.70 (n/a)</td><td>412.15 (n/a)</td><td>414.71 (n/a)</td><td>396.95 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.20 (+1.39%)</td><td>6.10 (-1.95%)</td><td>6.13 (-6.84%)</td><td>4.85 (+11.76%)</td><td>0.83 <b>(-22.99%)</b></td><td>1836.00 (-10.52%)</td><td>1484.82 (+0.47%)</td><td>1454.00 (+7.35%)</td><td>1237.90 (-1.37%)</td><td>216.83 <b>(-33.26%)</b></td><td>433.71 (+1.39%)</td><td>367.37 (-1.95%)</td><td>369.24 (-6.84%)</td><td>292.41 (+11.76%)</td><td>50.13 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.10 (n/a)</td><td>6.22 (n/a)</td><td>6.58 (n/a)</td><td>4.34 (n/a)</td><td>1.08 (n/a)</td><td>2051.90 (n/a)</td><td>1477.86 (n/a)</td><td>1354.50 (n/a)</td><td>1255.10 (n/a)</td><td>324.88 (n/a)</td><td>427.75 (n/a)</td><td>374.68 (n/a)</td><td>396.35 (n/a)</td><td>261.64 (n/a)</td><td>65.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.98 (-0.49%)</td><td>7.72 (-1.43%)</td><td>7.81 (-1.27%)</td><td>7.16 (-3.22%)</td><td>0.32 <b>(+30.15%)</b></td><td>4869.30 (+3.33%)</td><td>4520.70 (+1.52%)</td><td>4463.30 (+1.29%)</td><td>4371.50 (+0.49%)</td><td>199.05 <b>(+35.49%)</b></td><td>491.24 (-0.49%)</td><td>475.73 (-1.43%)</td><td>481.15 (-1.27%)</td><td>441.02 (-3.22%)</td><td>19.91 <b>(+30.15%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.01 (n/a)</td><td>7.84 (n/a)</td><td>7.91 (n/a)</td><td>7.40 (n/a)</td><td>0.25 (n/a)</td><td>4712.60 (n/a)</td><td>4453.06 (n/a)</td><td>4406.60 (n/a)</td><td>4350.30 (n/a)</td><td>146.92 (n/a)</td><td>493.64 (n/a)</td><td>482.65 (n/a)</td><td>487.34 (n/a)</td><td>455.69 (n/a)</td><td>15.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.68 (-2.79%)</td><td>7.40 (-0.11%)</td><td>7.59 (+0.20%)</td><td>7.03 (+1.62%)</td><td>0.30 <b>(-28.44%)</b></td><td>4961.30 (-1.60%)</td><td>4717.18 (-0.01%)</td><td>4596.40 (-0.20%)</td><td>4542.10 (+2.87%)</td><td>193.77 <b>(-28.00%)</b></td><td>472.80 (-2.79%)</td><td>455.86 (-0.11%)</td><td>467.21 (+0.20%)</td><td>432.85 (+1.62%)</td><td>18.45 <b>(-28.44%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.90 (n/a)</td><td>7.41 (n/a)</td><td>7.57 (n/a)</td><td>6.92 (n/a)</td><td>0.42 (n/a)</td><td>5041.80 (n/a)</td><td>4717.72 (n/a)</td><td>4605.70 (n/a)</td><td>4415.20 (n/a)</td><td>269.14 (n/a)</td><td>486.39 (n/a)</td><td>456.37 (n/a)</td><td>466.26 (n/a)</td><td>425.93 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.34 (-0.38%)</td><td>7.18 (+0.13%)</td><td>7.29 (+1.50%)</td><td>6.80 (-1.17%)</td><td>0.22 (+10.87%)</td><td>5124.00 (+1.19%)</td><td>4859.98 (-0.11%)</td><td>4781.90 (-1.48%)</td><td>4751.40 (+0.38%)</td><td>153.84 (+13.18%)</td><td>451.97 (-0.38%)</td><td>442.22 (+0.13%)</td><td>449.09 (+1.50%)</td><td>419.11 (-1.17%)</td><td>13.53 (+10.87%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>7.37 (n/a)</td><td>7.17 (n/a)</td><td>7.18 (n/a)</td><td>6.89 (n/a)</td><td>0.20 (n/a)</td><td>5063.90 (n/a)</td><td>4865.36 (n/a)</td><td>4853.60 (n/a)</td><td>4733.30 (n/a)</td><td>135.93 (n/a)</td><td>453.69 (n/a)</td><td>441.65 (n/a)</td><td>442.45 (n/a)</td><td>424.08 (n/a)</td><td>12.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.79 (+0.01%)</td><td>0.79 (+0.01%)</td><td>0.79 (+0.03%)</td><td>0.79 (+0.00%)</td><td>0.00 (+15.28%)</td><td>95431.10 (-0.00%)</td><td>95387.76 (-0.01%)</td><td>95374.30 (-0.03%)</td><td>95339.30 (-0.01%)</td><td>38.46 (+15.31%)</td><td>720.79 (+0.01%)</td><td>720.42 (+0.01%)</td><td>720.52 (+0.03%)</td><td>720.10 (+0.00%)</td><td>0.29 (+15.29%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95431.20 (n/a)</td><td>95399.64 (n/a)</td><td>95403.00 (n/a)</td><td>95347.80 (n/a)</td><td>33.36 (n/a)</td><td>720.72 (n/a)</td><td>720.33 (n/a)</td><td>720.31 (n/a)</td><td>720.09 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.74 (-0.03%)</td><td>0.74 (+0.00%)</td><td>0.74 (+0.03%)</td><td>0.74 (-0.01%)</td><td>0.00 (-7.45%)</td><td>102689.10 (+0.01%)</td><td>102610.24 (-0.00%)</td><td>102587.90 (-0.03%)</td><td>102576.50 (+0.03%)</td><td>46.20 (-7.40%)</td><td>669.93 (-0.03%)</td><td>669.71 (+0.00%)</td><td>669.86 (+0.03%)</td><td>669.20 (-0.01%)</td><td>0.30 (-7.45%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102681.10 (n/a)</td><td>102611.28 (n/a)</td><td>102617.20 (n/a)</td><td>102547.70 (n/a)</td><td>49.90 (n/a)</td><td>670.12 (n/a)</td><td>669.71 (n/a)</td><td>669.67 (n/a)</td><td>669.25 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.70 (-0.35%)</td><td>0.70 (-0.20%)</td><td>0.70 (-0.09%)</td><td>0.70 (-0.20%)</td><td>0.00 <b>(-22.49%)</b></td><td>107839.40 (+0.20%)</td><td>107582.54 (+0.20%)</td><td>107526.60 (+0.09%)</td><td>107426.10 (+0.35%)</td><td>161.08 <b>(-22.03%)</b></td><td>639.69 (-0.35%)</td><td>638.76 (-0.20%)</td><td>639.09 (-0.09%)</td><td>637.24 (-0.20%)</td><td>0.96 <b>(-22.49%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.71 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107619.30 (n/a)</td><td>107370.40 (n/a)</td><td>107426.70 (n/a)</td><td>107053.80 (n/a)</td><td>206.61 (n/a)</td><td>641.92 (n/a)</td><td>640.02 (n/a)</td><td>639.69 (n/a)</td><td>638.54 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>4.11 (-3.95%)</td><td>3.33 (-3.45%)</td><td>3.02 (-4.26%)</td><td>2.96 (-1.80%)</td><td>0.49 (-6.82%)</td><td>2722.60 (+1.84%)</td><td>2461.90 (+3.45%)</td><td>2669.90 (+4.45%)</td><td>1963.20 (+4.11%)</td><td>330.55 (-0.46%)</td><td>1076.77 (-3.95%)</td><td>872.53 (-3.45%)</td><td>791.77 (-4.26%)</td><td>776.45 (-1.80%)</td><td>129.48 (-6.82%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.27 (n/a)</td><td>3.45 (n/a)</td><td>3.15 (n/a)</td><td>3.02 (n/a)</td><td>0.53 (n/a)</td><td>2673.50 (n/a)</td><td>2379.80 (n/a)</td><td>2556.20 (n/a)</td><td>1885.70 (n/a)</td><td>332.07 (n/a)</td><td>1121.02 (n/a)</td><td>903.74 (n/a)</td><td>827.00 (n/a)</td><td>790.70 (n/a)</td><td>138.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.49 (-9.29%)</td><td>0.37 (-10.16%)</td><td>0.35 <b>(-27.09%)</b></td><td>0.34 <b>(+20.57%)</b></td><td>0.06 <b>(-43.68%)</b></td><td>3646.90 (-17.06%)</td><td>3390.32 (+6.30%)</td><td>3609.00 <b>(+37.15%)</b></td><td>2558.80 (+10.25%)</td><td>467.47 <b>(-50.09%)</b></td><td>26.23 (-9.29%)</td><td>20.17 (-10.16%)</td><td>18.59 <b>(-27.09%)</b></td><td>18.40 <b>(+20.57%)</b></td><td>3.40 <b>(-43.68%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.47 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>4397.20 (n/a)</td><td>3189.46 (n/a)</td><td>2631.40 (n/a)</td><td>2321.00 (n/a)</td><td>936.63 (n/a)</td><td>28.91 (n/a)</td><td>22.45 (n/a)</td><td>25.50 (n/a)</td><td>15.26 (n/a)</td><td>6.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>4.76 (-3.75%)</td><td>4.16 (+5.75%)</td><td>4.40 (+19.28%)</td><td>3.34 (-4.74%)</td><td>0.66 (+13.48%)</td><td>1993.30 (+4.98%)</td><td>1633.44 (-4.83%)</td><td>1510.60 (-16.17%)</td><td>1397.60 (+3.90%)</td><td>274.96 <b>(+25.10%)</b></td><td>1470.51 (-3.75%)</td><td>1285.71 (+5.75%)</td><td>1360.49 (+19.28%)</td><td>1031.07 (-4.74%)</td><td>204.77 (+13.48%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.94 (n/a)</td><td>3.94 (n/a)</td><td>3.69 (n/a)</td><td>3.50 (n/a)</td><td>0.58 (n/a)</td><td>1898.80 (n/a)</td><td>1716.38 (n/a)</td><td>1801.90 (n/a)</td><td>1345.20 (n/a)</td><td>219.78 (n/a)</td><td>1527.79 (n/a)</td><td>1215.84 (n/a)</td><td>1140.56 (n/a)</td><td>1082.39 (n/a)</td><td>180.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.68 (n/a)</td><td>13.07 (n/a)</td><td>13.35 (n/a)</td><td>11.59 (n/a)</td><td>0.84 (n/a)</td><td>13.67 (n/a)</td><td>13.06 (n/a)</td><td>13.34 (n/a)</td><td>11.58 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>24.76 (+1.14%)</td><td>24.53 (+1.38%)</td><td>24.50 (+0.80%)</td><td>24.21 (+1.67%)</td><td>0.22 (-18.19%)</td><td>24.75 (+1.14%)</td><td>24.52 (+1.38%)</td><td>24.49 (+0.80%)</td><td>24.19 (+1.67%)</td><td>0.22 (-18.19%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>24.49 (n/a)</td><td>24.20 (n/a)</td><td>24.31 (n/a)</td><td>23.81 (n/a)</td><td>0.27 (n/a)</td><td>24.47 (n/a)</td><td>24.19 (n/a)</td><td>24.29 (n/a)</td><td>23.79 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>42.29 (+3.94%)</td><td>41.09 (+4.11%)</td><td>40.94 (+2.33%)</td><td>40.16 (+7.73%)</td><td>0.94 <b>(-28.59%)</b></td><td>42.27 (+3.94%)</td><td>41.06 (+4.11%)</td><td>40.91 (+2.33%)</td><td>40.14 (+7.73%)</td><td>0.94 <b>(-28.59%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>40.69 (n/a)</td><td>39.47 (n/a)</td><td>40.01 (n/a)</td><td>37.28 (n/a)</td><td>1.32 (n/a)</td><td>40.66 (n/a)</td><td>39.44 (n/a)</td><td>39.98 (n/a)</td><td>37.26 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>46.22 (+5.16%)</td><td>43.17 (+5.37%)</td><td>43.36 (+5.57%)</td><td>39.83 (+6.00%)</td><td>2.28 (-19.91%)</td><td>46.19 (+5.16%)</td><td>43.14 (+5.37%)</td><td>43.34 (+5.57%)</td><td>39.80 (+6.00%)</td><td>2.28 (-19.91%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>43.95 (n/a)</td><td>40.97 (n/a)</td><td>41.08 (n/a)</td><td>37.57 (n/a)</td><td>2.85 (n/a)</td><td>43.92 (n/a)</td><td>40.94 (n/a)</td><td>41.05 (n/a)</td><td>37.55 (n/a)</td><td>2.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.27 (n/a)</td><td>13.09 (n/a)</td><td>13.18 (n/a)</td><td>12.81 (n/a)</td><td>0.21 (n/a)</td><td>13.26 (n/a)</td><td>13.08 (n/a)</td><td>13.17 (n/a)</td><td>12.80 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>24.65 (+0.78%)</td><td>24.42 (+1.24%)</td><td>24.33 (+1.02%)</td><td>24.24 (+1.89%)</td><td>0.18 <b>(-37.82%)</b></td><td>24.64 (+0.78%)</td><td>24.40 (+1.24%)</td><td>24.31 (+1.02%)</td><td>24.23 (+1.89%)</td><td>0.18 <b>(-37.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>24.46 (n/a)</td><td>24.12 (n/a)</td><td>24.08 (n/a)</td><td>23.79 (n/a)</td><td>0.29 (n/a)</td><td>24.45 (n/a)</td><td>24.10 (n/a)</td><td>24.07 (n/a)</td><td>23.78 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>43.27 (+3.55%)</td><td>39.73 (+1.03%)</td><td>40.41 (+2.33%)</td><td>36.24 (+1.42%)</td><td>3.10 <b>(+32.08%)</b></td><td>43.24 (+3.55%)</td><td>39.70 (+1.03%)</td><td>40.38 (+2.33%)</td><td>36.21 (+1.42%)</td><td>3.10 <b>(+32.08%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>41.78 (n/a)</td><td>39.32 (n/a)</td><td>39.49 (n/a)</td><td>35.73 (n/a)</td><td>2.35 (n/a)</td><td>41.76 (n/a)</td><td>39.30 (n/a)</td><td>39.46 (n/a)</td><td>35.71 (n/a)</td><td>2.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>44.36 (-2.47%)</td><td>42.11 (+1.90%)</td><td>42.74 (+2.61%)</td><td>39.35 (+4.27%)</td><td>2.01 <b>(-42.08%)</b></td><td>44.34 (-2.47%)</td><td>42.09 (+1.90%)</td><td>42.72 (+2.61%)</td><td>39.32 (+4.27%)</td><td>2.01 <b>(-42.08%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>45.49 (n/a)</td><td>41.32 (n/a)</td><td>41.65 (n/a)</td><td>37.74 (n/a)</td><td>3.47 (n/a)</td><td>45.46 (n/a)</td><td>41.30 (n/a)</td><td>41.63 (n/a)</td><td>37.71 (n/a)</td><td>3.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>9.17 (-3.76%)</td><td>8.95 (+0.61%)</td><td>8.88 (-1.92%)</td><td>8.83 (+5.25%)</td><td>0.14 <b>(-70.89%)</b></td><td>9.16 (-3.76%)</td><td>8.94 (+0.61%)</td><td>8.86 (-1.92%)</td><td>8.81 (+5.25%)</td><td>0.14 <b>(-70.89%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>9.53 (n/a)</td><td>8.90 (n/a)</td><td>9.05 (n/a)</td><td>8.39 (n/a)</td><td>0.48 (n/a)</td><td>9.51 (n/a)</td><td>8.88 (n/a)</td><td>9.04 (n/a)</td><td>8.37 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.97 (-5.46%)</td><td>0.87 (-9.84%)</td><td>0.90 (-11.26%)</td><td>0.70 (-18.36%)</td><td>0.10 <b>(+31.67%)</b></td><td>0.95 (-5.46%)</td><td>0.86 (-9.84%)</td><td>0.89 (-11.26%)</td><td>0.69 (-18.36%)</td><td>0.10 <b>(+31.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.03 (n/a)</td><td>0.97 (n/a)</td><td>1.02 (n/a)</td><td>0.86 (n/a)</td><td>0.08 (n/a)</td><td>1.01 (n/a)</td><td>0.95 (n/a)</td><td>1.00 (n/a)</td><td>0.85 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.18 (-9.29%)</td><td>1.07 (+2.51%)</td><td>1.11 (+7.67%)</td><td>0.91 (+7.03%)</td><td>0.11 <b>(-35.70%)</b></td><td>1.17 (-9.29%)</td><td>1.05 (+2.51%)</td><td>1.10 (+7.67%)</td><td>0.90 (+7.03%)</td><td>0.11 <b>(-35.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.30 (n/a)</td><td>1.04 (n/a)</td><td>1.04 (n/a)</td><td>0.85 (n/a)</td><td>0.18 (n/a)</td><td>1.29 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>19.96 (+8.45%)</td><td>16.73 (-2.06%)</td><td>16.24 (-4.22%)</td><td>14.84 (-7.62%)</td><td>1.96 <b>(+89.29%)</b></td><td>19.73 (+8.45%)</td><td>16.54 (-2.06%)</td><td>16.05 (-4.22%)</td><td>14.67 (-7.62%)</td><td>1.94 <b>(+89.29%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>18.41 (n/a)</td><td>17.09 (n/a)</td><td>16.96 (n/a)</td><td>16.07 (n/a)</td><td>1.04 (n/a)</td><td>18.19 (n/a)</td><td>16.89 (n/a)</td><td>16.76 (n/a)</td><td>15.88 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.46 (+0.60%)</td><td>13.71 (+1.39%)</td><td>13.65 (+3.53%)</td><td>13.20 (+2.09%)</td><td>0.54 (-12.21%)</td><td>14.21 (+0.60%)</td><td>13.47 (+1.39%)</td><td>13.41 (+3.53%)</td><td>12.97 (+2.09%)</td><td>0.53 (-12.21%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>14.38 (n/a)</td><td>13.52 (n/a)</td><td>13.19 (n/a)</td><td>12.93 (n/a)</td><td>0.61 (n/a)</td><td>14.13 (n/a)</td><td>13.28 (n/a)</td><td>12.96 (n/a)</td><td>12.70 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>8.56 (+2.54%)</td><td>7.65 (+1.02%)</td><td>8.04 (+1.66%)</td><td>5.78 (-9.30%)</td><td>1.14 <b>(+35.41%)</b></td><td>8.41 (+2.54%)</td><td>7.52 (+1.02%)</td><td>7.90 (+1.66%)</td><td>5.68 (-9.30%)</td><td>1.12 <b>(+35.41%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.35 (n/a)</td><td>7.57 (n/a)</td><td>7.91 (n/a)</td><td>6.37 (n/a)</td><td>0.84 (n/a)</td><td>8.20 (n/a)</td><td>7.44 (n/a)</td><td>7.77 (n/a)</td><td>6.26 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>6.52 (+12.42%)</td><td>5.64 (+3.74%)</td><td>5.98 (+8.99%)</td><td>4.44 (-5.99%)</td><td>0.83 <b>(+86.84%)</b></td><td>6.42 (+12.42%)</td><td>5.55 (+3.74%)</td><td>5.88 (+8.99%)</td><td>4.37 (-5.99%)</td><td>0.81 <b>(+86.84%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>5.80 (n/a)</td><td>5.44 (n/a)</td><td>5.49 (n/a)</td><td>4.72 (n/a)</td><td>0.44 (n/a)</td><td>5.71 (n/a)</td><td>5.35 (n/a)</td><td>5.40 (n/a)</td><td>4.65 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.48 (n/a)</td><td>12.88 (n/a)</td><td>13.26 (n/a)</td><td>12.12 (n/a)</td><td>0.67 (n/a)</td><td>13.47 (n/a)</td><td>12.88 (n/a)</td><td>13.26 (n/a)</td><td>12.11 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.36 (n/a)</td><td>12.91 (n/a)</td><td>13.25 (n/a)</td><td>12.12 (n/a)</td><td>0.56 (n/a)</td><td>13.35 (n/a)</td><td>12.90 (n/a)</td><td>13.24 (n/a)</td><td>12.11 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>157.34 (n/a)</td><td>175.40 (n/a)</td><td>111.60 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.70 (n/a)</td><td>166.12 (n/a)</td><td>161.40 (n/a)</td><td>129.60 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>275.30 (n/a)</td><td>195.90 (n/a)</td><td>185.20 (n/a)</td><td>124.30 (n/a)</td><td>62.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.00 (n/a)</td><td>183.20 (n/a)</td><td>162.50 (n/a)</td><td>140.90 (n/a)</td><td>39.93 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>264.70 (n/a)</td><td>166.08 (n/a)</td><td>130.40 (n/a)</td><td>118.80 (n/a)</td><td>62.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>285.30 (n/a)</td><td>185.92 (n/a)</td><td>181.30 (n/a)</td><td>110.10 (n/a)</td><td>69.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.40 (n/a)</td><td>182.76 (n/a)</td><td>183.10 (n/a)</td><td>147.60 (n/a)</td><td>29.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.20 (n/a)</td><td>187.66 (n/a)</td><td>185.90 (n/a)</td><td>160.10 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>155.18 (n/a)</td><td>158.50 (n/a)</td><td>136.00 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>190.52 (n/a)</td><td>193.60 (n/a)</td><td>159.30 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.50 (n/a)</td><td>193.28 (n/a)</td><td>174.50 (n/a)</td><td>133.10 (n/a)</td><td>63.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>162.40 (n/a)</td><td>159.90 (n/a)</td><td>142.90 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.60 (n/a)</td><td>187.00 (n/a)</td><td>184.00 (n/a)</td><td>146.50 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>177.22 (n/a)</td><td>172.70 (n/a)</td><td>144.70 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>175.64 (n/a)</td><td>184.60 (n/a)</td><td>127.30 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>195.50 (n/a)</td><td>198.30 (n/a)</td><td>167.10 (n/a)</td><td>16.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.90 (n/a)</td><td>168.76 (n/a)</td><td>173.30 (n/a)</td><td>123.30 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>178.40 (n/a)</td><td>152.00 (n/a)</td><td>167.40 (n/a)</td><td>101.20 (n/a)</td><td>31.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>227.50 (n/a)</td><td>174.36 (n/a)</td><td>162.50 (n/a)</td><td>127.10 (n/a)</td><td>48.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>208.80 (n/a)</td><td>174.66 (n/a)</td><td>172.50 (n/a)</td><td>116.00 (n/a)</td><td>37.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>368.40 (n/a)</td><td>223.76 (n/a)</td><td>186.80 (n/a)</td><td>144.90 (n/a)</td><td>87.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>283.30 (n/a)</td><td>218.20 (n/a)</td><td>208.50 (n/a)</td><td>173.30 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>175.10 (n/a)</td><td>174.20 (n/a)</td><td>146.60 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>282.40 (n/a)</td><td>204.76 (n/a)</td><td>200.30 (n/a)</td><td>130.70 (n/a)</td><td>55.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.20 (n/a)</td><td>166.08 (n/a)</td><td>170.40 (n/a)</td><td>144.70 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>292.30 (n/a)</td><td>189.62 (n/a)</td><td>175.40 (n/a)</td><td>137.20 (n/a)</td><td>59.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>211.00 (n/a)</td><td>180.04 (n/a)</td><td>185.40 (n/a)</td><td>134.50 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.20 (n/a)</td><td>193.12 (n/a)</td><td>198.10 (n/a)</td><td>167.20 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>216.80 (n/a)</td><td>184.06 (n/a)</td><td>188.60 (n/a)</td><td>140.40 (n/a)</td><td>29.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.30 (n/a)</td><td>195.60 (n/a)</td><td>189.00 (n/a)</td><td>162.50 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>249.60 (n/a)</td><td>190.58 (n/a)</td><td>186.90 (n/a)</td><td>154.10 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>260.40 (n/a)</td><td>216.46 (n/a)</td><td>207.50 (n/a)</td><td>193.10 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+3.94%)</td><td>0.03 (+1.38%)</td><td>0.03 (+12.10%)</td><td>0.02 (-13.56%)</td><td>0.00 <b>(+56.83%)</b></td><td>221.80 (+15.70%)</td><td>167.62 (+0.73%)</td><td>147.60 (-10.82%)</td><td>135.70 (-3.76%)</td><td>35.88 <b>(+74.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.70 (n/a)</td><td>166.40 (n/a)</td><td>165.50 (n/a)</td><td>141.00 (n/a)</td><td>20.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+6.00%)</td><td>0.02 (+4.19%)</td><td>0.02 (+11.23%)</td><td>0.02 (-12.22%)</td><td>0.00 <b>(+90.21%)</b></td><td>246.90 (+13.94%)</td><td>186.08 (-1.96%)</td><td>171.10 (-10.09%)</td><td>155.80 (-5.69%)</td><td>37.59 <b>(+104.57%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>189.80 (n/a)</td><td>190.30 (n/a)</td><td>165.20 (n/a)</td><td>18.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+10.76%)</td><td>0.03 (+17.67%)</td><td>0.03 <b>(+21.45%)</b></td><td>0.02 <b>(+28.89%)</b></td><td>0.01 (+4.21%)</td><td>195.70 <b>(-22.40%)</b></td><td>148.62 (-15.99%)</td><td>129.20 (-17.65%)</td><td>124.80 (-9.76%)</td><td>31.19 <b>(-30.53%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.20 (n/a)</td><td>176.90 (n/a)</td><td>156.90 (n/a)</td><td>138.30 (n/a)</td><td>44.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 <b>(-20.22%)</b></td><td>0.03 (+12.25%)</td><td>0.03 <b>(+37.55%)</b></td><td>0.02 <b>(+26.32%)</b></td><td>0.00 <b>(-58.32%)</b></td><td>189.60 <b>(-20.87%)</b></td><td>155.76 (-16.92%)</td><td>150.00 <b>(-27.29%)</b></td><td>129.50 <b>(+25.36%)</b></td><td>22.92 <b>(-55.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.60 (n/a)</td><td>187.48 (n/a)</td><td>206.30 (n/a)</td><td>103.30 (n/a)</td><td>52.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 <b>(-20.02%)</b></td><td>0.02 (-11.99%)</td><td>0.02 (-5.18%)</td><td>0.02 <b>(-20.11%)</b></td><td>0.00 <b>(-22.46%)</b></td><td>235.90 <b>(+25.15%)</b></td><td>179.92 (+13.56%)</td><td>171.50 (+5.47%)</td><td>155.90 <b>(+25.02%)</b></td><td>32.09 <b>(+25.63%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.50 (n/a)</td><td>158.44 (n/a)</td><td>162.60 (n/a)</td><td>124.70 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-14.33%)</td><td>0.02 (-5.16%)</td><td>0.02 (+11.58%)</td><td>0.02 (+13.05%)</td><td>0.00 <b>(-48.17%)</b></td><td>205.50 (-11.54%)</td><td>179.20 (-0.36%)</td><td>182.50 (-10.36%)</td><td>134.60 (+16.74%)</td><td>27.68 <b>(-47.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>179.84 (n/a)</td><td>203.60 (n/a)</td><td>115.30 (n/a)</td><td>52.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-7.45%)</td><td>0.03 (+1.23%)</td><td>0.03 (+3.10%)</td><td>0.02 (+17.86%)</td><td>0.00 <b>(-29.32%)</b></td><td>211.90 (-15.14%)</td><td>163.34 (-4.13%)</td><td>158.60 (-3.00%)</td><td>133.20 (+8.03%)</td><td>30.76 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.70 (n/a)</td><td>170.38 (n/a)</td><td>163.50 (n/a)</td><td>123.30 (n/a)</td><td>48.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 <b>(+26.09%)</b></td><td>0.02 (+7.52%)</td><td>0.02 (-2.89%)</td><td>0.02 (+17.04%)</td><td>0.00 <b>(+53.19%)</b></td><td>219.90 (-14.57%)</td><td>202.68 (-6.61%)</td><td>213.00 (+3.00%)</td><td>163.00 <b>(-20.68%)</b></td><td>22.88 (+1.18%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>257.40 (n/a)</td><td>217.02 (n/a)</td><td>206.80 (n/a)</td><td>205.50 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (+10.77%)</td><td>0.05 (-1.06%)</td><td>0.05 (-12.30%)</td><td>0.04 (+4.51%)</td><td>0.01 (+14.37%)</td><td>184.10 (-4.31%)</td><td>159.90 (+1.23%)</td><td>166.40 (+14.05%)</td><td>126.90 (-9.74%)</td><td>21.20 (-3.16%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>157.96 (n/a)</td><td>145.90 (n/a)</td><td>140.60 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 <b>(-25.66%)</b></td><td>0.04 (-13.76%)</td><td>0.04 (-1.17%)</td><td>0.03 <b>(-30.39%)</b></td><td>0.01 <b>(-25.69%)</b></td><td>286.60 <b>(+43.66%)</b></td><td>198.04 (+16.34%)</td><td>185.10 (+1.20%)</td><td>161.50 <b>(+34.47%)</b></td><td>50.66 <b>(+46.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>170.22 (n/a)</td><td>182.90 (n/a)</td><td>120.10 (n/a)</td><td>34.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(+31.86%)</b></td><td>0.05 (+7.67%)</td><td>0.05 (+1.26%)</td><td>0.02 (-3.60%)</td><td>0.02 <b>(+38.65%)</b></td><td>381.90 (+3.72%)</td><td>203.66 (-2.67%)</td><td>172.20 (-1.26%)</td><td>121.10 <b>(-24.17%)</b></td><td>102.38 (+14.67%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>368.20 (n/a)</td><td>209.24 (n/a)</td><td>174.40 (n/a)</td><td>159.70 (n/a)</td><td>89.28 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (+13.29%)</td><td>0.05 (+4.69%)</td><td>0.05 (+4.34%)</td><td>0.04 (-0.02%)</td><td>0.01 <b>(+47.62%)</b></td><td>201.60 (+0.00%)</td><td>165.06 (-2.85%)</td><td>166.40 (-4.15%)</td><td>117.10 (-11.76%)</td><td>32.68 <b>(+31.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.60 (n/a)</td><td>169.90 (n/a)</td><td>173.60 (n/a)</td><td>132.70 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 <b>(-23.12%)</b></td><td>0.04 (-10.29%)</td><td>0.05 (-18.34%)</td><td>0.04 <b>(+65.28%)</b></td><td>0.00 <b>(-89.59%)</b></td><td>193.10 <b>(-39.51%)</b></td><td>183.90 (+0.84%)</td><td>181.50 <b>(+22.47%)</b></td><td>177.40 <b>(+30.06%)</b></td><td>6.23 <b>(-91.98%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.20 (n/a)</td><td>182.36 (n/a)</td><td>148.20 (n/a)</td><td>136.40 (n/a)</td><td>77.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 <b>(+26.90%)</b></td><td>0.05 (-3.29%)</td><td>0.04 (-17.87%)</td><td>0.04 (-2.77%)</td><td>0.02 <b>(+101.71%)</b></td><td>217.10 (+2.84%)</td><td>179.18 (+7.49%)</td><td>191.70 <b>(+21.71%)</b></td><td>109.20 <b>(-21.16%)</b></td><td>41.21 <b>(+50.71%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>166.70 (n/a)</td><td>157.50 (n/a)</td><td>138.50 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (+5.42%)</td><td>0.05 (-2.32%)</td><td>0.06 (+3.72%)</td><td>0.04 <b>(-22.69%)</b></td><td>0.01 <b>(+75.59%)</b></td><td>223.90 <b>(+29.35%)</b></td><td>159.28 (+6.47%)</td><td>140.80 (-3.63%)</td><td>117.90 (-5.15%)</td><td>43.33 <b>(+115.01%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.10 (n/a)</td><td>149.60 (n/a)</td><td>146.10 (n/a)</td><td>124.30 (n/a)</td><td>20.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 <b>(-32.59%)</b></td><td>0.04 (-16.37%)</td><td>0.04 (-10.54%)</td><td>0.04 (-11.06%)</td><td>0.00 <b>(-67.42%)</b></td><td>231.10 (+12.46%)</td><td>207.24 (+17.10%)</td><td>204.00 (+11.78%)</td><td>192.10 <b>(+48.34%)</b></td><td>16.26 <b>(-44.31%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>176.98 (n/a)</td><td>182.50 (n/a)</td><td>129.50 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-7.26%)</td><td>0.05 (-13.84%)</td><td>0.04 (-10.95%)</td><td>0.04 (-3.09%)</td><td>0.01 <b>(-20.98%)</b></td><td>208.80 (+3.21%)</td><td>187.62 (+14.17%)</td><td>201.30 (+12.27%)</td><td>126.40 (+7.85%)</td><td>34.51 (-13.93%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>164.34 (n/a)</td><td>179.30 (n/a)</td><td>117.20 (n/a)</td><td>40.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (+0.62%)</td><td>0.04 (+3.96%)</td><td>0.04 (+12.70%)</td><td>0.04 (-1.27%)</td><td>0.00 (-0.23%)</td><td>224.30 (+1.26%)</td><td>191.98 (-3.81%)</td><td>183.40 (-11.27%)</td><td>172.30 (-0.58%)</td><td>22.11 (+0.18%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.50 (n/a)</td><td>199.58 (n/a)</td><td>206.70 (n/a)</td><td>173.30 (n/a)</td><td>22.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (-15.50%)</td><td>0.10 (-11.91%)</td><td>0.11 (-4.58%)</td><td>0.08 <b>(-28.70%)</b></td><td>0.02 (+17.55%)</td><td>216.50 <b>(+40.22%)</b></td><td>163.98 (+15.67%)</td><td>155.10 (+4.80%)</td><td>131.40 (+18.38%)</td><td>34.78 <b>(+98.14%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>154.40 (n/a)</td><td>141.76 (n/a)</td><td>148.00 (n/a)</td><td>111.00 (n/a)</td><td>17.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (+0.92%)</td><td>0.11 (+0.15%)</td><td>0.11 (+5.41%)</td><td>0.08 (-6.59%)</td><td>0.02 (+7.96%)</td><td>196.70 (+7.08%)</td><td>154.12 (+0.40%)</td><td>149.00 (-5.10%)</td><td>117.80 (-0.93%)</td><td>28.90 (+15.99%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.70 (n/a)</td><td>153.50 (n/a)</td><td>157.00 (n/a)</td><td>118.90 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (-0.88%)</td><td>0.10 (+0.75%)</td><td>0.10 (-2.87%)</td><td>0.09 (+13.37%)</td><td>0.01 <b>(-28.37%)</b></td><td>191.80 (-11.78%)</td><td>168.10 (-2.11%)</td><td>167.50 (+2.95%)</td><td>140.90 (+0.86%)</td><td>20.07 <b>(-36.33%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.40 (n/a)</td><td>171.72 (n/a)</td><td>162.70 (n/a)</td><td>139.70 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (+18.02%)</td><td>0.11 (+3.35%)</td><td>0.11 (-0.75%)</td><td>0.08 (-10.04%)</td><td>0.03 <b>(+140.00%)</b></td><td>210.70 (+11.19%)</td><td>160.34 (+2.15%)</td><td>152.80 (+0.73%)</td><td>114.80 (-15.28%)</td><td>46.12 <b>(+123.91%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>156.96 (n/a)</td><td>151.70 (n/a)</td><td>135.50 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (+13.31%)</td><td>0.11 (+1.14%)</td><td>0.11 (+4.45%)</td><td>0.09 (-5.98%)</td><td>0.02 <b>(+68.73%)</b></td><td>188.30 (+6.32%)</td><td>152.56 (+0.93%)</td><td>146.10 (-4.32%)</td><td>110.00 (-11.72%)</td><td>29.86 <b>(+58.09%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.10 (n/a)</td><td>151.16 (n/a)</td><td>152.70 (n/a)</td><td>124.60 (n/a)</td><td>18.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 <b>(-25.64%)</b></td><td>0.09 (-6.51%)</td><td>0.09 (+0.27%)</td><td>0.08 (+2.71%)</td><td>0.01 <b>(-61.22%)</b></td><td>206.60 (-2.64%)</td><td>181.30 (+4.11%)</td><td>178.30 (-0.28%)</td><td>163.40 <b>(+34.49%)</b></td><td>17.50 <b>(-46.97%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.20 (n/a)</td><td>174.14 (n/a)</td><td>178.80 (n/a)</td><td>121.50 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (-1.58%)</td><td>0.10 (+15.48%)</td><td>0.10 (+10.95%)</td><td>0.09 <b>(+54.12%)</b></td><td>0.01 <b>(-66.77%)</b></td><td>188.50 <b>(-35.11%)</b></td><td>170.90 (-17.37%)</td><td>169.20 (-9.90%)</td><td>155.60 (+1.63%)</td><td>11.84 <b>(-78.31%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>290.50 (n/a)</td><td>206.82 (n/a)</td><td>187.80 (n/a)</td><td>153.10 (n/a)</td><td>54.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (+14.50%)</td><td>0.08 (+5.48%)</td><td>0.08 (+0.24%)</td><td>0.07 (+14.46%)</td><td>0.01 (+3.41%)</td><td>235.30 (-12.66%)</td><td>213.78 (-5.38%)</td><td>217.20 (-0.23%)</td><td>182.40 (-12.69%)</td><td>19.24 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>269.40 (n/a)</td><td>225.94 (n/a)</td><td>217.70 (n/a)</td><td>208.90 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.27 (+1.27%)</td><td>0.20 (-4.17%)</td><td>0.21 (+5.83%)</td><td>0.12 <b>(-25.03%)</b></td><td>0.05 (+17.13%)</td><td>273.10 <b>(+33.41%)</b></td><td>174.22 (+7.92%)</td><td>157.80 (-5.51%)</td><td>123.40 (-1.20%)</td><td>57.88 <b>(+68.53%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>204.70 (n/a)</td><td>161.44 (n/a)</td><td>167.00 (n/a)</td><td>124.90 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 <b>(+36.47%)</b></td><td>0.22 <b>(+20.70%)</b></td><td>0.20 (+11.50%)</td><td>0.19 (+7.63%)</td><td>0.03 <b>(+480.09%)</b></td><td>175.20 (-7.10%)</td><td>152.64 (-15.72%)</td><td>162.70 (-10.31%)</td><td>127.20 <b>(-26.73%)</b></td><td>22.24 <b>(+287.43%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>181.12 (n/a)</td><td>181.40 (n/a)</td><td>173.60 (n/a)</td><td>5.74 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (+2.27%)</td><td>0.19 (-5.57%)</td><td>0.18 (-10.02%)</td><td>0.15 (-11.75%)</td><td>0.04 (+9.87%)</td><td>220.40 (+13.32%)</td><td>175.08 (+6.73%)</td><td>185.60 (+11.14%)</td><td>125.70 (-2.26%)</td><td>36.07 (+18.23%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.50 (n/a)</td><td>164.04 (n/a)</td><td>167.00 (n/a)</td><td>128.60 (n/a)</td><td>30.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 <b>(-23.73%)</b></td><td>0.19 (-1.10%)</td><td>0.18 (-3.71%)</td><td>0.17 <b>(+101.14%)</b></td><td>0.02 <b>(-72.63%)</b></td><td>191.50 <b>(-50.27%)</b></td><td>175.94 (-13.27%)</td><td>180.70 (+3.85%)</td><td>147.30 <b>(+31.05%)</b></td><td>17.07 <b>(-83.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>385.10 (n/a)</td><td>202.86 (n/a)</td><td>174.00 (n/a)</td><td>112.40 (n/a)</td><td>105.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 <b>(+23.53%)</b></td><td>0.20 (+2.93%)</td><td>0.18 (+6.24%)</td><td>0.15 (-6.88%)</td><td>0.06 <b>(+71.05%)</b></td><td>221.70 (+7.36%)</td><td>178.74 (+1.09%)</td><td>179.60 (-5.87%)</td><td>106.60 (-19.00%)</td><td>45.51 <b>(+44.58%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.50 (n/a)</td><td>176.82 (n/a)</td><td>190.80 (n/a)</td><td>131.60 (n/a)</td><td>31.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (-9.99%)</td><td>0.16 (+2.00%)</td><td>0.16 (+1.76%)</td><td>0.15 <b>(+30.07%)</b></td><td>0.02 <b>(-53.09%)</b></td><td>219.50 <b>(-23.14%)</b></td><td>201.30 (-7.18%)</td><td>207.20 (-1.71%)</td><td>161.30 (+11.09%)</td><td>23.75 <b>(-61.32%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>285.60 (n/a)</td><td>216.88 (n/a)</td><td>210.80 (n/a)</td><td>145.20 (n/a)</td><td>61.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (+8.98%)</td><td>0.14 (+6.47%)</td><td>0.14 (-1.72%)</td><td>0.09 (+0.37%)</td><td>0.03 (+13.49%)</td><td>376.80 (-0.37%)</td><td>253.44 (-5.28%)</td><td>236.20 (+1.72%)</td><td>205.50 (-8.22%)</td><td>70.44 (+7.53%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>378.20 (n/a)</td><td>267.56 (n/a)</td><td>232.20 (n/a)</td><td>223.90 (n/a)</td><td>65.50 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (-8.42%)</td><td>0.03 <b>(+28.83%)</b></td><td>0.03 <b>(+48.91%)</b></td><td>0.02 <b>(+59.44%)</b></td><td>0.01 <b>(-48.81%)</b></td><td>175.80 <b>(-37.28%)</b></td><td>145.16 <b>(-29.42%)</b></td><td>145.50 <b>(-32.83%)</b></td><td>109.90 (+9.14%)</td><td>24.76 <b>(-62.07%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>280.30 (n/a)</td><td>205.68 (n/a)</td><td>216.60 (n/a)</td><td>100.70 (n/a)</td><td>65.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-15.41%)</td><td>0.03 (-7.94%)</td><td>0.03 (+8.55%)</td><td>0.02 <b>(-21.00%)</b></td><td>0.01 (-11.26%)</td><td>231.20 <b>(+26.55%)</b></td><td>162.66 (+9.37%)</td><td>149.40 (-7.89%)</td><td>131.20 (+18.20%)</td><td>40.62 <b>(+36.54%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>148.72 (n/a)</td><td>162.20 (n/a)</td><td>111.00 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 <b>(+23.16%)</b></td><td>0.02 <b>(+33.62%)</b></td><td>0.02 <b>(+20.60%)</b></td><td>0.02 <b>(+61.06%)</b></td><td>0.00 <b>(-35.01%)</b></td><td>201.70 <b>(-37.92%)</b></td><td>173.16 <b>(-29.14%)</b></td><td>173.40 (-17.07%)</td><td>144.10 (-18.82%)</td><td>23.09 <b>(-68.57%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>324.90 (n/a)</td><td>244.38 (n/a)</td><td>209.10 (n/a)</td><td>177.50 (n/a)</td><td>73.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-3.62%)</td><td>0.02 (-5.02%)</td><td>0.02 (-9.34%)</td><td>0.02 (-12.98%)</td><td>0.00 <b>(+23.64%)</b></td><td>249.10 (+14.90%)</td><td>186.34 (+6.97%)</td><td>189.30 (+10.31%)</td><td>144.50 (+3.81%)</td><td>40.90 <b>(+45.64%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.80 (n/a)</td><td>174.20 (n/a)</td><td>171.60 (n/a)</td><td>139.20 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+13.70%)</td><td>0.02 (+8.29%)</td><td>0.03 (+12.07%)</td><td>0.02 <b>(+20.71%)</b></td><td>0.01 (+0.61%)</td><td>271.00 (-17.15%)</td><td>180.20 (-9.70%)</td><td>161.80 (-10.76%)</td><td>122.00 (-12.04%)</td><td>57.60 <b>(-24.82%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>327.10 (n/a)</td><td>199.56 (n/a)</td><td>181.30 (n/a)</td><td>138.70 (n/a)</td><td>76.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-13.00%)</td><td>0.03 (-6.42%)</td><td>0.02 (-7.40%)</td><td>0.02 <b>(+25.71%)</b></td><td>0.00 <b>(-45.79%)</b></td><td>191.30 <b>(-20.46%)</b></td><td>159.74 (+1.01%)</td><td>166.60 (+7.97%)</td><td>123.00 (+14.95%)</td><td>25.16 <b>(-51.59%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.50 (n/a)</td><td>158.14 (n/a)</td><td>154.30 (n/a)</td><td>107.00 (n/a)</td><td>51.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+11.69%)</td><td>0.03 (+8.03%)</td><td>0.03 (+0.76%)</td><td>0.03 (+10.12%)</td><td>0.00 (+0.37%)</td><td>163.80 (-9.20%)</td><td>146.48 (-7.64%)</td><td>147.10 (-0.74%)</td><td>124.80 (-10.47%)</td><td>15.31 <b>(-20.11%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.40 (n/a)</td><td>158.60 (n/a)</td><td>148.20 (n/a)</td><td>139.40 (n/a)</td><td>19.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+1.69%)</td><td>0.03 (+6.15%)</td><td>0.03 (+9.35%)</td><td>0.02 <b>(+26.53%)</b></td><td>0.00 <b>(-41.76%)</b></td><td>164.50 <b>(-20.95%)</b></td><td>144.88 (-8.04%)</td><td>147.60 (-8.55%)</td><td>124.50 (-1.66%)</td><td>15.36 <b>(-53.73%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>157.54 (n/a)</td><td>161.40 (n/a)</td><td>126.60 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-5.72%)</td><td>0.02 (-0.98%)</td><td>0.02 (+4.18%)</td><td>0.02 (-0.64%)</td><td>0.00 (-12.73%)</td><td>203.90 (+0.64%)</td><td>173.18 (+0.44%)</td><td>171.80 (-4.02%)</td><td>135.30 (+6.03%)</td><td>30.13 (-5.82%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.60 (n/a)</td><td>172.42 (n/a)</td><td>179.00 (n/a)</td><td>127.60 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+1.92%)</td><td>0.02 (+10.93%)</td><td>0.02 (+17.97%)</td><td>0.02 (+11.18%)</td><td>0.00 (-14.61%)</td><td>214.80 (-10.05%)</td><td>168.18 (-10.81%)</td><td>164.80 (-15.27%)</td><td>135.80 (-1.88%)</td><td>28.90 <b>(-21.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.80 (n/a)</td><td>188.56 (n/a)</td><td>194.50 (n/a)</td><td>138.40 (n/a)</td><td>36.95 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-10.24%)</td><td>0.02 (-4.08%)</td><td>0.02 (-2.53%)</td><td>0.02 (-5.78%)</td><td>0.00 <b>(-29.17%)</b></td><td>193.50 (+6.14%)</td><td>171.28 (+3.59%)</td><td>172.60 (+2.62%)</td><td>143.80 (+11.39%)</td><td>17.80 (-16.11%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.30 (n/a)</td><td>165.34 (n/a)</td><td>168.20 (n/a)</td><td>129.10 (n/a)</td><td>21.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+8.70%)</td><td>0.02 (-6.55%)</td><td>0.02 (-13.01%)</td><td>0.02 <b>(-21.98%)</b></td><td>0.00 <b>(+149.28%)</b></td><td>229.40 <b>(+28.16%)</b></td><td>178.88 (+10.26%)</td><td>186.90 (+14.94%)</td><td>134.70 (-7.99%)</td><td>36.99 <b>(+190.52%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.00 (n/a)</td><td>162.24 (n/a)</td><td>162.60 (n/a)</td><td>146.40 (n/a)</td><td>12.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 <b>(+29.35%)</b></td><td>0.02 (+0.11%)</td><td>0.02 (-9.09%)</td><td>0.02 (-6.52%)</td><td>0.01 <b>(+86.71%)</b></td><td>240.90 (+6.97%)</td><td>190.28 (+3.98%)</td><td>194.10 (+9.97%)</td><td>116.90 <b>(-22.69%)</b></td><td>47.97 <b>(+51.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.20 (n/a)</td><td>183.00 (n/a)</td><td>176.50 (n/a)</td><td>151.20 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+6.77%)</td><td>0.02 (+2.96%)</td><td>0.02 (+4.51%)</td><td>0.02 (-1.95%)</td><td>0.00 <b>(+77.08%)</b></td><td>199.30 (+2.00%)</td><td>181.14 (-2.42%)</td><td>178.90 (-4.33%)</td><td>160.70 (-6.35%)</td><td>16.91 <b>(+71.03%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.40 (n/a)</td><td>185.64 (n/a)</td><td>187.00 (n/a)</td><td>171.60 (n/a)</td><td>9.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 <b>(-29.63%)</b></td><td>0.02 (-6.78%)</td><td>0.02 (+2.45%)</td><td>0.02 <b>(+23.38%)</b></td><td>0.00 <b>(-75.45%)</b></td><td>217.10 (-18.96%)</td><td>196.76 (+1.79%)</td><td>192.40 (-2.38%)</td><td>181.90 <b>(+42.11%)</b></td><td>14.48 <b>(-71.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>267.90 (n/a)</td><td>193.30 (n/a)</td><td>197.10 (n/a)</td><td>128.00 (n/a)</td><td>50.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+3.88%)</td><td>0.03 (-0.69%)</td><td>0.02 (-0.06%)</td><td>0.02 (-1.78%)</td><td>0.01 (+18.85%)</td><td>188.90 (+1.83%)</td><td>164.12 (+1.53%)</td><td>174.90 (+0.06%)</td><td>122.00 (-3.71%)</td><td>29.12 (+18.49%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.50 (n/a)</td><td>161.64 (n/a)</td><td>174.80 (n/a)</td><td>126.70 (n/a)</td><td>24.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-1.27%)</td><td>0.05 (+2.58%)</td><td>0.05 (-1.03%)</td><td>0.04 (+12.97%)</td><td>0.01 (-13.40%)</td><td>195.80 (-11.52%)</td><td>165.26 (-3.62%)</td><td>173.80 (+1.05%)</td><td>127.00 (+1.28%)</td><td>27.62 <b>(-22.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>171.46 (n/a)</td><td>172.00 (n/a)</td><td>125.40 (n/a)</td><td>35.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (+0.62%)</td><td>0.05 (-3.29%)</td><td>0.06 (+1.40%)</td><td>0.04 (-14.08%)</td><td>0.01 <b>(+75.09%)</b></td><td>193.00 (+16.41%)</td><td>156.60 (+5.30%)</td><td>147.70 (-1.40%)</td><td>127.30 (-0.62%)</td><td>28.08 <b>(+107.00%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.80 (n/a)</td><td>148.72 (n/a)</td><td>149.80 (n/a)</td><td>128.10 (n/a)</td><td>13.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (-8.95%)</td><td>0.04 (-2.15%)</td><td>0.04 (-3.91%)</td><td>0.03 <b>(+20.39%)</b></td><td>0.00 <b>(-39.89%)</b></td><td>239.80 (-16.91%)</td><td>218.36 (-0.03%)</td><td>222.60 (+4.07%)</td><td>179.00 (+9.88%)</td><td>24.56 <b>(-45.87%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.60 (n/a)</td><td>218.42 (n/a)</td><td>213.90 (n/a)</td><td>162.90 (n/a)</td><td>45.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 <b>(-20.15%)</b></td><td>0.04 (-16.33%)</td><td>0.04 (-11.84%)</td><td>0.02 <b>(-30.88%)</b></td><td>0.01 (-8.54%)</td><td>335.90 <b>(+44.66%)</b></td><td>228.58 <b>(+21.73%)</b></td><td>211.70 (+13.45%)</td><td>172.90 <b>(+25.20%)</b></td><td>62.28 <b>(+78.76%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.20 (n/a)</td><td>187.78 (n/a)</td><td>186.60 (n/a)</td><td>138.10 (n/a)</td><td>34.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (-15.25%)</td><td>0.05 (-5.01%)</td><td>0.05 (-14.81%)</td><td>0.04 <b>(+83.29%)</b></td><td>0.00 <b>(-72.15%)</b></td><td>185.20 <b>(-45.45%)</b></td><td>170.30 (-6.53%)</td><td>170.50 (+17.42%)</td><td>149.50 (+18.00%)</td><td>14.84 <b>(-83.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>339.50 (n/a)</td><td>182.20 (n/a)</td><td>145.20 (n/a)</td><td>126.70 (n/a)</td><td>88.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-9.27%)</td><td>0.05 (-1.64%)</td><td>0.05 (+1.45%)</td><td>0.04 (-6.08%)</td><td>0.01 (-4.37%)</td><td>217.40 (+6.46%)</td><td>168.58 (+1.98%)</td><td>164.10 (-1.44%)</td><td>129.70 (+10.20%)</td><td>37.02 (+13.33%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>165.30 (n/a)</td><td>166.50 (n/a)</td><td>117.70 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (+10.41%)</td><td>0.05 (+8.09%)</td><td>0.05 (+8.32%)</td><td>0.04 (-4.99%)</td><td>0.01 <b>(+21.47%)</b></td><td>232.70 (+5.25%)</td><td>164.38 (-6.14%)</td><td>159.20 (-7.71%)</td><td>115.30 (-9.43%)</td><td>42.99 (+18.00%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>175.14 (n/a)</td><td>172.50 (n/a)</td><td>127.30 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-13.39%)</td><td>0.05 (+10.07%)</td><td>0.06 (+15.80%)</td><td>0.05 <b>(+28.75%)</b></td><td>0.00 <b>(-59.34%)</b></td><td>169.10 <b>(-22.32%)</b></td><td>151.84 (-12.09%)</td><td>145.50 (-13.65%)</td><td>138.80 (+15.47%)</td><td>13.52 <b>(-62.53%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>172.72 (n/a)</td><td>168.50 (n/a)</td><td>120.20 (n/a)</td><td>36.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (-11.10%)</td><td>0.05 (-3.36%)</td><td>0.04 (+0.26%)</td><td>0.03 (+17.05%)</td><td>0.01 <b>(-22.41%)</b></td><td>242.10 (-14.57%)</td><td>188.70 (-0.15%)</td><td>193.80 (-0.26%)</td><td>122.80 (+12.45%)</td><td>48.01 <b>(-24.03%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>283.40 (n/a)</td><td>188.98 (n/a)</td><td>194.30 (n/a)</td><td>109.20 (n/a)</td><td>63.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-17.28%)</td><td>0.05 (+2.65%)</td><td>0.05 (+15.05%)</td><td>0.03 (-3.10%)</td><td>0.01 <b>(-22.38%)</b></td><td>250.10 (+3.22%)</td><td>170.78 (-3.49%)</td><td>150.80 (-13.08%)</td><td>143.30 <b>(+20.93%)</b></td><td>44.82 (+1.46%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>176.96 (n/a)</td><td>173.50 (n/a)</td><td>118.50 (n/a)</td><td>44.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-12.35%)</td><td>0.06 (+16.73%)</td><td>0.05 (+10.75%)</td><td>0.05 <b>(+63.81%)</b></td><td>0.01 <b>(-52.96%)</b></td><td>168.50 <b>(-38.95%)</b></td><td>151.12 <b>(-20.12%)</b></td><td>161.70 (-9.72%)</td><td>127.60 (+14.13%)</td><td>19.85 <b>(-66.47%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>276.00 (n/a)</td><td>189.18 (n/a)</td><td>179.10 (n/a)</td><td>111.80 (n/a)</td><td>59.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-3.43%)</td><td>0.05 (+4.66%)</td><td>0.05 (+1.50%)</td><td>0.03 (+1.72%)</td><td>0.01 (-9.18%)</td><td>236.50 (-1.70%)</td><td>168.18 (-4.97%)</td><td>156.70 (-1.45%)</td><td>142.10 (+3.57%)</td><td>38.89 (-6.06%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.60 (n/a)</td><td>176.98 (n/a)</td><td>159.00 (n/a)</td><td>137.20 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-11.13%)</td><td>0.05 (+11.26%)</td><td>0.06 (+16.87%)</td><td>0.04 (+14.30%)</td><td>0.01 <b>(-31.64%)</b></td><td>198.60 (-12.55%)</td><td>154.42 (-12.58%)</td><td>144.80 (-14.42%)</td><td>129.60 (+12.50%)</td><td>28.83 <b>(-32.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>176.64 (n/a)</td><td>169.20 (n/a)</td><td>115.20 (n/a)</td><td>42.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 <b>(+24.45%)</b></td><td>0.05 (+16.13%)</td><td>0.05 (+13.18%)</td><td>0.03 (-7.01%)</td><td>0.01 <b>(+74.56%)</b></td><td>249.10 (+7.56%)</td><td>164.62 (-10.94%)</td><td>149.20 (-11.66%)</td><td>129.00 (-19.68%)</td><td>48.39 <b>(+59.52%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.60 (n/a)</td><td>184.84 (n/a)</td><td>168.90 (n/a)</td><td>160.60 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-9.29%)</td><td>0.05 (-0.74%)</td><td>0.05 (+0.72%)</td><td>0.04 (+3.29%)</td><td>0.01 <b>(-24.51%)</b></td><td>204.00 (-3.23%)</td><td>167.66 (-1.04%)</td><td>156.70 (-0.76%)</td><td>128.50 (+10.21%)</td><td>31.28 (-19.51%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>169.42 (n/a)</td><td>157.90 (n/a)</td><td>116.60 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-14.79%)</td><td>0.05 (+8.23%)</td><td>0.05 <b>(+20.36%)</b></td><td>0.04 (+2.38%)</td><td>0.01 <b>(-40.22%)</b></td><td>208.30 (-2.30%)</td><td>160.96 (-9.82%)</td><td>152.40 (-16.90%)</td><td>138.00 (+17.35%)</td><td>27.34 <b>(-26.44%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>178.48 (n/a)</td><td>183.40 (n/a)</td><td>117.60 (n/a)</td><td>37.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (-17.39%)</td><td>0.09 (-7.53%)</td><td>0.10 (-3.05%)</td><td>0.07 (-0.97%)</td><td>0.01 <b>(-28.94%)</b></td><td>229.30 (+0.97%)</td><td>183.76 (+6.89%)</td><td>165.50 (+3.18%)</td><td>162.30 <b>(+21.12%)</b></td><td>29.15 (-16.20%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.10 (n/a)</td><td>171.92 (n/a)</td><td>160.40 (n/a)</td><td>134.00 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (-8.70%)</td><td>0.10 (-2.95%)</td><td>0.10 (-0.09%)</td><td>0.07 (-16.31%)</td><td>0.02 (-4.52%)</td><td>227.90 (+19.51%)</td><td>173.42 (+3.55%)</td><td>169.00 (+0.06%)</td><td>138.70 (+9.47%)</td><td>33.01 <b>(+31.10%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.70 (n/a)</td><td>167.48 (n/a)</td><td>168.90 (n/a)</td><td>126.70 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 <b>(-20.88%)</b></td><td>0.07 (-14.31%)</td><td>0.08 (+1.73%)</td><td>0.05 <b>(-25.98%)</b></td><td>0.01 <b>(-20.99%)</b></td><td>314.20 <b>(+35.08%)</b></td><td>234.98 (+16.95%)</td><td>214.80 (-1.69%)</td><td>200.60 <b>(+26.40%)</b></td><td>45.59 <b>(+39.52%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>200.92 (n/a)</td><td>218.50 (n/a)</td><td>158.70 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (-8.03%)</td><td>0.07 (-12.82%)</td><td>0.07 (-15.83%)</td><td>0.05 <b>(-25.06%)</b></td><td>0.01 (+15.34%)</td><td>321.20 <b>(+33.44%)</b></td><td>241.52 (+16.25%)</td><td>231.10 (+18.82%)</td><td>191.00 (+8.71%)</td><td>47.95 <b>(+69.50%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>207.76 (n/a)</td><td>194.50 (n/a)</td><td>175.70 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 <b>(-39.05%)</b></td><td>0.08 <b>(-22.24%)</b></td><td>0.08 <b>(-20.87%)</b></td><td>0.08 (-0.81%)</td><td>0.00 <b>(-83.57%)</b></td><td>210.70 (+0.86%)</td><td>196.48 <b>(+24.06%)</b></td><td>195.00 <b>(+26.38%)</b></td><td>185.60 <b>(+64.10%)</b></td><td>9.41 <b>(-72.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.90 (n/a)</td><td>158.38 (n/a)</td><td>154.30 (n/a)</td><td>113.10 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (-19.48%)</td><td>0.09 (-15.84%)</td><td>0.08 <b>(-20.69%)</b></td><td>0.08 (-5.25%)</td><td>0.01 <b>(-31.95%)</b></td><td>202.60 (+5.52%)</td><td>182.60 (+18.00%)</td><td>193.60 <b>(+26.04%)</b></td><td>160.30 <b>(+24.17%)</b></td><td>19.86 (-14.08%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>154.74 (n/a)</td><td>153.60 (n/a)</td><td>129.10 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 <b>(+65.38%)</b></td><td>0.11 (+2.44%)</td><td>0.09 <b>(-23.70%)</b></td><td>0.08 (-10.72%)</td><td>0.06 <b>(+236.24%)</b></td><td>208.60 (+11.97%)</td><td>174.06 (+11.05%)</td><td>192.20 <b>(+31.11%)</b></td><td>75.40 <b>(-39.53%)</b></td><td>55.71 <b>(+113.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.30 (n/a)</td><td>156.74 (n/a)</td><td>146.60 (n/a)</td><td>124.70 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (-7.22%)</td><td>0.09 <b>(-26.37%)</b></td><td>0.09 <b>(-32.38%)</b></td><td>0.04 <b>(-57.86%)</b></td><td>0.04 <b>(+54.54%)</b></td><td>378.20 <b>(+137.26%)</b></td><td>201.92 <b>(+54.07%)</b></td><td>176.70 <b>(+47.87%)</b></td><td>116.60 (+7.76%)</td><td>102.30 <b>(+316.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>159.40 (n/a)</td><td>131.06 (n/a)</td><td>119.50 (n/a)</td><td>108.20 (n/a)</td><td>24.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (+8.56%)</td><td>0.10 (-0.68%)</td><td>0.09 (-12.98%)</td><td>0.08 <b>(+20.60%)</b></td><td>0.02 (+0.05%)</td><td>200.50 (-17.08%)</td><td>171.02 (-0.27%)</td><td>177.70 (+14.94%)</td><td>127.80 (-7.93%)</td><td>29.72 <b>(-26.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>241.80 (n/a)</td><td>171.48 (n/a)</td><td>154.60 (n/a)</td><td>138.80 (n/a)</td><td>40.63 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (-13.17%)</td><td>0.09 (-8.92%)</td><td>0.10 (-5.63%)</td><td>0.07 (+5.91%)</td><td>0.02 <b>(-24.92%)</b></td><td>221.30 (-5.59%)</td><td>181.66 (+8.08%)</td><td>164.40 (+6.00%)</td><td>145.20 (+15.24%)</td><td>33.72 (-18.16%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.40 (n/a)</td><td>168.08 (n/a)</td><td>155.10 (n/a)</td><td>126.00 (n/a)</td><td>41.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (-13.42%)</td><td>0.10 (+0.18%)</td><td>0.10 (-0.84%)</td><td>0.09 <b>(+24.05%)</b></td><td>0.01 <b>(-46.76%)</b></td><td>182.30 (-19.41%)</td><td>162.20 (-3.81%)</td><td>169.60 (+0.83%)</td><td>130.10 (+15.54%)</td><td>20.57 <b>(-49.99%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>226.20 (n/a)</td><td>168.62 (n/a)</td><td>168.20 (n/a)</td><td>112.60 (n/a)</td><td>41.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 <b>(+33.74%)</b></td><td>0.11 (+9.34%)</td><td>0.09 (-9.73%)</td><td>0.08 (+12.22%)</td><td>0.03 <b>(+97.64%)</b></td><td>201.40 (-10.88%)</td><td>163.20 (-5.39%)</td><td>183.10 (+10.77%)</td><td>109.20 <b>(-25.26%)</b></td><td>40.25 <b>(+28.71%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.00 (n/a)</td><td>172.50 (n/a)</td><td>165.30 (n/a)</td><td>146.10 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 <b>(-28.66%)</b></td><td>0.08 <b>(-26.79%)</b></td><td>0.08 <b>(-23.93%)</b></td><td>0.07 (-18.06%)</td><td>0.01 <b>(-52.22%)</b></td><td>246.00 <b>(+22.02%)</b></td><td>204.20 <b>(+33.59%)</b></td><td>203.70 <b>(+31.42%)</b></td><td>167.40 <b>(+40.20%)</b></td><td>28.33 (-15.88%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.60 (n/a)</td><td>152.86 (n/a)</td><td>155.00 (n/a)</td><td>119.40 (n/a)</td><td>33.68 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 <b>(-31.30%)</b></td><td>0.08 (-15.48%)</td><td>0.08 (-2.77%)</td><td>0.07 (-1.88%)</td><td>0.01 <b>(-72.72%)</b></td><td>227.40 (+1.93%)</td><td>208.44 (+13.93%)</td><td>207.70 (+2.87%)</td><td>185.90 <b>(+45.58%)</b></td><td>16.04 <b>(-59.35%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.10 (n/a)</td><td>182.96 (n/a)</td><td>201.90 (n/a)</td><td>127.70 (n/a)</td><td>39.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (-17.44%)</td><td>0.07 <b>(-26.82%)</b></td><td>0.07 <b>(-35.06%)</b></td><td>0.06 <b>(-27.30%)</b></td><td>0.02 (+2.02%)</td><td>288.90 <b>(+37.57%)</b></td><td>229.58 <b>(+38.80%)</b></td><td>241.60 <b>(+53.98%)</b></td><td>159.30 <b>(+21.14%)</b></td><td>48.05 <b>(+63.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.00 (n/a)</td><td>165.40 (n/a)</td><td>156.90 (n/a)</td><td>131.50 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 <b>(-25.14%)</b></td><td>0.09 (-18.26%)</td><td>0.08 (-17.17%)</td><td>0.07 (+1.03%)</td><td>0.01 <b>(-50.14%)</b></td><td>229.90 (-1.03%)</td><td>194.84 (+18.00%)</td><td>202.90 <b>(+20.70%)</b></td><td>164.40 <b>(+33.55%)</b></td><td>29.30 <b>(-34.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>232.30 (n/a)</td><td>165.12 (n/a)</td><td>168.10 (n/a)</td><td>123.10 (n/a)</td><td>44.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 (+10.88%)</td><td>0.20 (+1.07%)</td><td>0.21 (-2.53%)</td><td>0.15 (+1.96%)</td><td>0.04 <b>(+23.18%)</b></td><td>225.20 (-1.92%)</td><td>172.26 (-0.22%)</td><td>158.90 (+2.58%)</td><td>134.90 (-9.83%)</td><td>36.70 (+9.40%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>229.60 (n/a)</td><td>172.64 (n/a)</td><td>154.90 (n/a)</td><td>149.60 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 <b>(-22.25%)</b></td><td>0.16 <b>(-23.51%)</b></td><td>0.16 (-17.17%)</td><td>0.13 <b>(-22.69%)</b></td><td>0.03 <b>(-29.51%)</b></td><td>260.10 <b>(+29.34%)</b></td><td>212.42 <b>(+30.11%)</b></td><td>205.90 <b>(+20.76%)</b></td><td>163.40 <b>(+28.66%)</b></td><td>35.73 (+18.02%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.10 (n/a)</td><td>163.26 (n/a)</td><td>170.50 (n/a)</td><td>127.00 (n/a)</td><td>30.27 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (-8.18%)</td><td>0.13 (-13.90%)</td><td>0.14 (-11.21%)</td><td>0.11 <b>(-22.35%)</b></td><td>0.02 <b>(+64.28%)</b></td><td>304.00 <b>(+28.81%)</b></td><td>249.04 (+18.12%)</td><td>230.10 (+12.63%)</td><td>205.30 (+8.91%)</td><td>42.74 <b>(+132.55%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>210.84 (n/a)</td><td>204.30 (n/a)</td><td>188.50 (n/a)</td><td>18.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 <b>(-29.11%)</b></td><td>0.17 (-2.51%)</td><td>0.17 (+7.72%)</td><td>0.16 (+13.01%)</td><td>0.01 <b>(-77.93%)</b></td><td>203.40 (-11.53%)</td><td>190.14 (-1.82%)</td><td>194.70 (-7.15%)</td><td>176.50 <b>(+41.09%)</b></td><td>11.63 <b>(-71.49%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>229.90 (n/a)</td><td>193.66 (n/a)</td><td>209.70 (n/a)</td><td>125.10 (n/a)</td><td>40.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (-17.74%)</td><td>0.17 (-16.13%)</td><td>0.17 (-13.18%)</td><td>0.16 (-15.39%)</td><td>0.01 <b>(-39.08%)</b></td><td>209.70 (+18.21%)</td><td>191.44 (+18.83%)</td><td>192.40 (+15.21%)</td><td>172.40 <b>(+21.58%)</b></td><td>13.26 (-12.44%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>177.40 (n/a)</td><td>161.10 (n/a)</td><td>167.00 (n/a)</td><td>141.80 (n/a)</td><td>15.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (-10.90%)</td><td>0.17 (-3.23%)</td><td>0.19 (+15.08%)</td><td>0.10 <b>(-20.38%)</b></td><td>0.05 (+11.86%)</td><td>340.60 <b>(+25.59%)</b></td><td>211.28 (+7.14%)</td><td>169.20 (-13.10%)</td><td>155.40 (+12.20%)</td><td>77.22 <b>(+58.31%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>271.20 (n/a)</td><td>197.20 (n/a)</td><td>194.70 (n/a)</td><td>138.50 (n/a)</td><td>48.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 <b>(+36.89%)</b></td><td>0.20 (+13.93%)</td><td>0.19 (+9.65%)</td><td>0.15 (+0.94%)</td><td>0.04 <b>(+165.15%)</b></td><td>212.40 (-0.93%)</td><td>168.56 (-10.12%)</td><td>171.50 (-8.78%)</td><td>124.50 <b>(-26.94%)</b></td><td>31.61 <b>(+87.21%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.40 (n/a)</td><td>187.54 (n/a)</td><td>188.00 (n/a)</td><td>170.40 (n/a)</td><td>16.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 <b>(+22.15%)</b></td><td>0.18 (+18.58%)</td><td>0.19 (+14.84%)</td><td>0.09 (-9.75%)</td><td>0.05 <b>(+46.63%)</b></td><td>380.70 (+10.80%)</td><td>206.56 (-10.37%)</td><td>171.70 (-12.93%)</td><td>144.00 (-18.14%)</td><td>98.12 <b>(+42.21%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>343.60 (n/a)</td><td>230.46 (n/a)</td><td>197.20 (n/a)</td><td>175.90 (n/a)</td><td>68.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 <b>(+27.64%)</b></td><td>0.18 (+7.92%)</td><td>0.16 (-5.63%)</td><td>0.15 (+7.73%)</td><td>0.05 <b>(+92.80%)</b></td><td>220.20 (-7.17%)</td><td>191.46 (-4.94%)</td><td>209.00 (+5.93%)</td><td>127.50 <b>(-21.68%)</b></td><td>38.40 <b>(+39.52%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>237.20 (n/a)</td><td>201.40 (n/a)</td><td>197.30 (n/a)</td><td>162.80 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (-1.15%)</td><td>0.18 (+0.74%)</td><td>0.19 (+11.64%)</td><td>0.14 (+5.12%)</td><td>0.03 (-10.42%)</td><td>231.60 (-4.89%)</td><td>186.68 (-1.39%)</td><td>173.00 (-10.41%)</td><td>149.00 (+1.15%)</td><td>35.95 (-9.93%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.50 (n/a)</td><td>189.32 (n/a)</td><td>193.10 (n/a)</td><td>147.30 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (+9.45%)</td><td>0.19 (+1.64%)</td><td>0.19 (+2.49%)</td><td>0.14 (-7.18%)</td><td>0.03 <b>(+53.52%)</b></td><td>231.70 (+7.77%)</td><td>179.60 (-0.02%)</td><td>176.50 (-2.43%)</td><td>141.50 (-8.65%)</td><td>34.60 <b>(+51.14%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.00 (n/a)</td><td>179.64 (n/a)</td><td>180.90 (n/a)</td><td>154.90 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 <b>(-33.47%)</b></td><td>0.18 (-4.10%)</td><td>0.18 (+7.46%)</td><td>0.17 <b>(+22.53%)</b></td><td>0.00 <b>(-95.28%)</b></td><td>187.30 (-18.39%)</td><td>182.94 (-0.67%)</td><td>182.20 (-6.95%)</td><td>181.00 <b>(+50.33%)</b></td><td>2.49 <b>(-93.93%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>229.50 (n/a)</td><td>184.18 (n/a)</td><td>195.80 (n/a)</td><td>120.40 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 <b>(-22.34%)</b></td><td>0.19 (-5.51%)</td><td>0.19 (+6.75%)</td><td>0.14 (-4.99%)</td><td>0.03 <b>(-49.53%)</b></td><td>233.90 (+5.27%)</td><td>178.94 (+1.58%)</td><td>170.10 (-6.33%)</td><td>147.50 <b>(+28.71%)</b></td><td>32.43 <b>(-30.64%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>222.20 (n/a)</td><td>176.16 (n/a)</td><td>181.60 (n/a)</td><td>114.60 (n/a)</td><td>46.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (+4.37%)</td><td>0.19 (+2.57%)</td><td>0.19 (-0.23%)</td><td>0.17 (+1.95%)</td><td>0.02 (-2.74%)</td><td>196.30 (-1.90%)</td><td>176.84 (-2.58%)</td><td>175.60 (+0.23%)</td><td>155.20 (-4.20%)</td><td>15.40 (-10.64%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.10 (n/a)</td><td>181.52 (n/a)</td><td>175.20 (n/a)</td><td>162.00 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (+3.25%)</td><td>0.19 (-1.48%)</td><td>0.19 (-6.59%)</td><td>0.15 (-6.58%)</td><td>0.02 <b>(+22.09%)</b></td><td>216.30 (+7.03%)</td><td>178.26 (+2.00%)</td><td>177.00 (+7.08%)</td><td>153.50 (-3.15%)</td><td>24.17 <b>(+27.91%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>174.76 (n/a)</td><td>165.30 (n/a)</td><td>158.50 (n/a)</td><td>18.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (-4.09%)</td><td>0.20 (+0.47%)</td><td>0.18 (-6.76%)</td><td>0.16 <b>(+83.11%)</b></td><td>0.04 <b>(-48.66%)</b></td><td>201.10 <b>(-45.38%)</b></td><td>172.02 (-12.86%)</td><td>185.60 (+7.28%)</td><td>127.50 (+4.25%)</td><td>29.52 <b>(-70.73%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>368.20 (n/a)</td><td>197.40 (n/a)</td><td>173.00 (n/a)</td><td>122.30 (n/a)</td><td>100.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (-0.07%)</td><td>0.18 (-0.23%)</td><td>0.18 (-0.07%)</td><td>0.18 (-0.41%)</td><td>0.00 <b>(+175.93%)</b></td><td>47619.70 (+0.41%)</td><td>47463.60 (+0.23%)</td><td>47384.60 (+0.07%)</td><td>47339.40 (+0.07%)</td><td>134.07 <b>(+177.34%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47426.10 (n/a)</td><td>47354.50 (n/a)</td><td>47350.10 (n/a)</td><td>47307.50 (n/a)</td><td>48.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (-0.27%)</td><td>0.18 (-0.20%)</td><td>0.18 (-0.16%)</td><td>0.18 (-0.25%)</td><td>0.00 (+6.31%)</td><td>47615.80 (+0.25%)</td><td>47510.44 (+0.20%)</td><td>47484.30 (+0.16%)</td><td>47435.30 (+0.27%)</td><td>82.06 (+6.88%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47497.70 (n/a)</td><td>47416.16 (n/a)</td><td>47409.30 (n/a)</td><td>47306.70 (n/a)</td><td>76.78 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (-0.08%)</td><td>0.11 (-0.04%)</td><td>0.11 (-0.04%)</td><td>0.11 (-0.02%)</td><td>0.00 <b>(-65.15%)</b></td><td>374498.60 (+0.02%)</td><td>374441.56 (+0.04%)</td><td>374447.50 (+0.04%)</td><td>374389.20 (+0.08%)</td><td>44.76 <b>(-65.09%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374415.60 (n/a)</td><td>374286.66 (n/a)</td><td>374313.90 (n/a)</td><td>374076.40 (n/a)</td><td>128.22 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 <b>(+24.35%)</b></td><td>0.03 (+11.30%)</td><td>0.03 (+1.07%)</td><td>0.02 (+17.38%)</td><td>0.00 <b>(+39.16%)</b></td><td>179.60 (-14.80%)</td><td>153.80 (-9.73%)</td><td>161.70 (-1.04%)</td><td>117.70 (-19.55%)</td><td>23.39 (-7.80%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.80 (n/a)</td><td>170.38 (n/a)</td><td>163.40 (n/a)</td><td>146.30 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (+15.44%)</td><td>0.04 (+13.36%)</td><td>0.04 (+12.75%)</td><td>0.03 (-2.35%)</td><td>0.01 <b>(+56.46%)</b></td><td>218.10 (+2.39%)</td><td>149.24 (-9.17%)</td><td>145.80 (-11.31%)</td><td>111.40 (-13.37%)</td><td>42.35 <b>(+36.89%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>164.30 (n/a)</td><td>164.40 (n/a)</td><td>128.60 (n/a)</td><td>30.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (+8.68%)</td><td>0.03 (+2.06%)</td><td>0.03 (-0.36%)</td><td>0.02 (+2.94%)</td><td>0.00 <b>(+31.25%)</b></td><td>177.40 (-2.85%)</td><td>155.44 (-1.21%)</td><td>159.90 (+0.31%)</td><td>116.20 (-8.00%)</td><td>24.74 (+18.40%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.60 (n/a)</td><td>157.34 (n/a)</td><td>159.40 (n/a)</td><td>126.30 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (+1.77%)</td><td>0.03 (-4.51%)</td><td>0.03 (+1.42%)</td><td>0.03 (+1.39%)</td><td>0.01 (-4.68%)</td><td>171.90 (-1.38%)</td><td>152.06 (+4.29%)</td><td>156.30 (-1.39%)</td><td>108.60 (-1.72%)</td><td>25.75 (-8.72%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>174.30 (n/a)</td><td>145.80 (n/a)</td><td>158.50 (n/a)</td><td>110.50 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 <b>(+37.46%)</b></td><td>0.02 (+4.09%)</td><td>0.02 (+6.66%)</td><td>0.01 <b>(-33.29%)</b></td><td>0.01 <b>(+490.35%)</b></td><td>308.20 <b>(+49.90%)</b></td><td>196.92 (+5.08%)</td><td>173.40 (-6.22%)</td><td>128.50 <b>(-27.24%)</b></td><td>70.98 <b>(+548.51%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>187.40 (n/a)</td><td>184.90 (n/a)</td><td>176.60 (n/a)</td><td>10.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 <b>(+22.14%)</b></td><td>0.03 (+10.44%)</td><td>0.04 <b>(+28.07%)</b></td><td>0.01 <b>(-38.30%)</b></td><td>0.01 <b>(+170.55%)</b></td><td>341.40 <b>(+62.03%)</b></td><td>177.74 (+3.52%)</td><td>129.20 <b>(-21.93%)</b></td><td>121.80 (-18.15%)</td><td>93.62 <b>(+266.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>171.70 (n/a)</td><td>165.50 (n/a)</td><td>148.80 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-0.17%)</td><td>0.02 (+4.30%)</td><td>0.02 (+0.64%)</td><td>0.02 <b>(+28.43%)</b></td><td>0.00 <b>(-32.07%)</b></td><td>215.40 <b>(-22.13%)</b></td><td>173.92 (-7.87%)</td><td>165.30 (-0.60%)</td><td>138.90 (+0.14%)</td><td>30.27 <b>(-46.62%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>276.60 (n/a)</td><td>188.78 (n/a)</td><td>166.30 (n/a)</td><td>138.70 (n/a)</td><td>56.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (+1.50%)</td><td>0.03 (+0.08%)</td><td>0.03 (-1.15%)</td><td>0.02 (+15.85%)</td><td>0.01 (-6.02%)</td><td>202.50 (-13.68%)</td><td>168.90 (-1.15%)</td><td>173.60 (+1.17%)</td><td>121.60 (-1.54%)</td><td>32.27 <b>(-21.27%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>170.86 (n/a)</td><td>171.60 (n/a)</td><td>123.50 (n/a)</td><td>40.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+18.38%)</td><td>0.02 (+2.24%)</td><td>0.02 (-1.56%)</td><td>0.02 (-12.83%)</td><td>0.01 <b>(+154.28%)</b></td><td>229.20 (+14.71%)</td><td>172.98 (+1.09%)</td><td>169.70 (+1.56%)</td><td>132.70 (-15.53%)</td><td>39.34 <b>(+137.67%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.80 (n/a)</td><td>171.12 (n/a)</td><td>167.10 (n/a)</td><td>157.10 (n/a)</td><td>16.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-11.90%)</td><td>0.03 (-6.79%)</td><td>0.03 (-10.52%)</td><td>0.02 (+9.01%)</td><td>0.00 <b>(-27.03%)</b></td><td>215.80 (-8.29%)</td><td>179.92 (+5.48%)</td><td>184.30 (+11.76%)</td><td>147.50 (+13.55%)</td><td>28.34 <b>(-27.68%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>170.58 (n/a)</td><td>164.90 (n/a)</td><td>129.90 (n/a)</td><td>39.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 <b>(+20.33%)</b></td><td>0.03 (+19.50%)</td><td>0.02 (+18.15%)</td><td>0.02 (+14.46%)</td><td>0.01 <b>(+21.80%)</b></td><td>207.90 (-12.65%)</td><td>167.18 (-16.18%)</td><td>168.90 (-15.38%)</td><td>113.40 (-16.86%)</td><td>34.45 (-14.14%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.00 (n/a)</td><td>199.46 (n/a)</td><td>199.60 (n/a)</td><td>136.40 (n/a)</td><td>40.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (-6.17%)</td><td>0.02 (-6.17%)</td><td>0.02 (-0.15%)</td><td>0.02 (+0.14%)</td><td>0.00 (-16.36%)</td><td>221.30 (-0.14%)</td><td>200.62 (+5.50%)</td><td>210.70 (+0.14%)</td><td>143.10 (+6.55%)</td><td>32.49 (-13.89%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>190.16 (n/a)</td><td>210.40 (n/a)</td><td>134.30 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+19.83%)</td><td>0.02 (+12.13%)</td><td>0.03 <b>(+31.71%)</b></td><td>0.01 <b>(-31.20%)</b></td><td>0.01 <b>(+255.67%)</b></td><td>320.20 <b>(+45.35%)</b></td><td>192.16 (-2.93%)</td><td>152.30 <b>(-24.08%)</b></td><td>145.10 (-16.56%)</td><td>74.72 <b>(+330.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.30 (n/a)</td><td>197.96 (n/a)</td><td>200.60 (n/a)</td><td>173.90 (n/a)</td><td>17.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (+4.41%)</td><td>0.02 (+3.07%)</td><td>0.02 (+2.75%)</td><td>0.02 (-5.50%)</td><td>0.00 <b>(+63.55%)</b></td><td>220.50 (+5.81%)</td><td>192.22 (-2.50%)</td><td>195.70 (-2.69%)</td><td>172.80 (-4.21%)</td><td>19.66 <b>(+62.45%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>197.14 (n/a)</td><td>201.10 (n/a)</td><td>180.40 (n/a)</td><td>12.10 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (-11.88%)</td><td>0.02 (-3.45%)</td><td>0.02 (+2.76%)</td><td>0.02 (-1.92%)</td><td>0.00 <b>(-34.55%)</b></td><td>262.60 (+1.94%)</td><td>231.42 (+2.76%)</td><td>221.60 (-2.68%)</td><td>211.00 (+13.50%)</td><td>22.92 <b>(-25.35%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>257.60 (n/a)</td><td>225.20 (n/a)</td><td>227.70 (n/a)</td><td>185.90 (n/a)</td><td>30.71 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(+24.05%)</b></td><td>0.05 (+5.91%)</td><td>0.05 (+6.47%)</td><td>0.04 (-11.89%)</td><td>0.01 <b>(+92.67%)</b></td><td>230.70 (+13.48%)</td><td>172.22 (-1.59%)</td><td>165.00 (-6.09%)</td><td>109.40 (-19.38%)</td><td>44.30 <b>(+74.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>175.00 (n/a)</td><td>175.70 (n/a)</td><td>135.70 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 <b>(+40.18%)</b></td><td>0.08 <b>(+21.65%)</b></td><td>0.08 <b>(+23.02%)</b></td><td>0.06 (-0.41%)</td><td>0.01 <b>(+418.53%)</b></td><td>194.90 (+0.41%)</td><td>157.66 (-16.00%)</td><td>155.50 (-18.71%)</td><td>125.90 <b>(-28.67%)</b></td><td>26.78 <b>(+271.23%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>194.10 (n/a)</td><td>187.68 (n/a)</td><td>191.30 (n/a)</td><td>176.50 (n/a)</td><td>7.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(+47.60%)</b></td><td>0.05 (+13.98%)</td><td>0.05 (+11.14%)</td><td>0.04 (-15.31%)</td><td>0.01 <b>(+377.33%)</b></td><td>229.40 (+18.06%)</td><td>162.72 (-7.73%)</td><td>155.60 (-10.06%)</td><td>111.00 <b>(-32.23%)</b></td><td>42.76 <b>(+280.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>176.36 (n/a)</td><td>173.00 (n/a)</td><td>163.80 (n/a)</td><td>11.25 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 <b>(+51.40%)</b></td><td>0.07 <b>(+47.81%)</b></td><td>0.06 <b>(+39.47%)</b></td><td>0.05 <b>(+50.53%)</b></td><td>0.01 <b>(+75.75%)</b></td><td>192.30 <b>(-33.55%)</b></td><td>158.92 <b>(-32.06%)</b></td><td>165.40 <b>(-28.31%)</b></td><td>134.60 <b>(-33.95%)</b></td><td>24.28 <b>(-26.74%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>289.40 (n/a)</td><td>233.92 (n/a)</td><td>230.70 (n/a)</td><td>203.80 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(+33.23%)</b></td><td>0.05 (+15.43%)</td><td>0.05 (+10.79%)</td><td>0.04 (+16.82%)</td><td>0.01 <b>(+83.14%)</b></td><td>198.50 (-14.37%)</td><td>167.38 (-11.71%)</td><td>170.40 (-9.75%)</td><td>115.80 <b>(-24.90%)</b></td><td>32.40 (+14.74%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>189.58 (n/a)</td><td>188.80 (n/a)</td><td>154.20 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (-2.14%)</td><td>0.06 (+2.37%)</td><td>0.06 (+13.38%)</td><td>0.05 (-7.47%)</td><td>0.01 (-5.79%)</td><td>218.10 (+8.08%)</td><td>171.54 (-2.39%)</td><td>170.80 (-11.78%)</td><td>128.60 (+2.23%)</td><td>32.92 (+3.51%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>175.74 (n/a)</td><td>193.60 (n/a)</td><td>125.80 (n/a)</td><td>31.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(+38.96%)</b></td><td>0.05 (+6.61%)</td><td>0.04 (-2.93%)</td><td>0.02 <b>(-39.09%)</b></td><td>0.02 <b>(+192.54%)</b></td><td>370.50 <b>(+64.16%)</b></td><td>206.92 (+7.48%)</td><td>189.90 (+2.98%)</td><td>115.30 <b>(-28.03%)</b></td><td>98.88 <b>(+249.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>192.52 (n/a)</td><td>184.40 (n/a)</td><td>160.20 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (+15.45%)</td><td>0.06 (+15.87%)</td><td>0.06 (+12.70%)</td><td>0.05 <b>(+30.90%)</b></td><td>0.01 (-6.55%)</td><td>172.90 <b>(-23.60%)</b></td><td>156.54 (-14.37%)</td><td>158.50 (-11.25%)</td><td>129.20 (-13.40%)</td><td>16.92 <b>(-39.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>182.82 (n/a)</td><td>178.60 (n/a)</td><td>149.20 (n/a)</td><td>28.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (-16.93%)</td><td>0.05 (+0.24%)</td><td>0.05 (+0.49%)</td><td>0.04 (+14.30%)</td><td>0.01 <b>(-51.44%)</b></td><td>184.50 (-12.52%)</td><td>167.82 (-3.26%)</td><td>176.20 (-0.51%)</td><td>140.50 <b>(+20.39%)</b></td><td>19.10 <b>(-46.89%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>173.48 (n/a)</td><td>177.10 (n/a)</td><td>116.70 (n/a)</td><td>35.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (-1.08%)</td><td>0.05 (-7.72%)</td><td>0.05 (-0.40%)</td><td>0.04 (-13.11%)</td><td>0.01 (+19.86%)</td><td>229.40 (+15.10%)</td><td>186.96 (+10.30%)</td><td>182.00 (+0.39%)</td><td>126.50 (+1.04%)</td><td>40.95 <b>(+41.96%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.30 (n/a)</td><td>169.50 (n/a)</td><td>181.30 (n/a)</td><td>125.20 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (+5.25%)</td><td>0.04 (-12.22%)</td><td>0.04 <b>(-23.70%)</b></td><td>0.03 (-2.23%)</td><td>0.01 (+4.36%)</td><td>238.60 (+2.27%)</td><td>200.68 (+14.02%)</td><td>205.30 <b>(+31.01%)</b></td><td>135.80 (-4.97%)</td><td>39.09 (-1.53%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.30 (n/a)</td><td>176.00 (n/a)</td><td>156.70 (n/a)</td><td>142.90 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 <b>(-40.77%)</b></td><td>0.05 (-0.27%)</td><td>0.05 <b>(+21.55%)</b></td><td>0.04 <b>(+21.98%)</b></td><td>0.00 <b>(-86.54%)</b></td><td>201.10 (-18.05%)</td><td>187.12 (-9.93%)</td><td>190.00 (-17.71%)</td><td>173.40 <b>(+68.84%)</b></td><td>11.44 <b>(-80.90%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>245.40 (n/a)</td><td>207.76 (n/a)</td><td>230.90 (n/a)</td><td>102.70 (n/a)</td><td>59.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (-12.72%)</td><td>0.04 (-3.34%)</td><td>0.05 (-1.08%)</td><td>0.03 (+13.18%)</td><td>0.01 <b>(-36.89%)</b></td><td>257.10 (-11.65%)</td><td>195.52 (-0.73%)</td><td>181.20 (+1.06%)</td><td>155.90 (+14.55%)</td><td>39.46 <b>(-35.75%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.00 (n/a)</td><td>196.96 (n/a)</td><td>179.30 (n/a)</td><td>136.10 (n/a)</td><td>61.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 <b>(+48.82%)</b></td><td>0.05 <b>(+27.13%)</b></td><td>0.05 (+10.92%)</td><td>0.04 (+11.98%)</td><td>0.01 <b>(+587.55%)</b></td><td>194.50 (-10.70%)</td><td>168.22 (-19.12%)</td><td>188.40 (-9.86%)</td><td>132.50 <b>(-32.84%)</b></td><td>30.82 <b>(+312.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.80 (n/a)</td><td>207.98 (n/a)</td><td>209.00 (n/a)</td><td>197.30 (n/a)</td><td>7.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (+2.96%)</td><td>0.04 (+3.46%)</td><td>0.04 (+8.56%)</td><td>0.03 (-7.39%)</td><td>0.01 <b>(+34.27%)</b></td><td>241.10 (+7.97%)</td><td>200.56 (-2.74%)</td><td>196.00 (-7.89%)</td><td>171.50 (-2.89%)</td><td>26.44 <b>(+43.63%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.30 (n/a)</td><td>206.20 (n/a)</td><td>212.80 (n/a)</td><td>176.60 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (-10.51%)</td><td>0.09 (-12.44%)</td><td>0.10 (+0.68%)</td><td>0.06 <b>(-28.83%)</b></td><td>0.02 <b>(+41.02%)</b></td><td>252.30 <b>(+40.48%)</b></td><td>186.46 (+19.08%)</td><td>160.70 (-0.68%)</td><td>134.20 (+11.74%)</td><td>52.47 <b>(+135.28%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>179.60 (n/a)</td><td>156.58 (n/a)</td><td>161.80 (n/a)</td><td>120.10 (n/a)</td><td>22.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (-5.31%)</td><td>0.15 (-6.05%)</td><td>0.14 (-12.34%)</td><td>0.12 (-1.65%)</td><td>0.03 (-10.14%)</td><td>205.60 (+1.68%)</td><td>171.10 (+5.81%)</td><td>177.90 (+14.04%)</td><td>121.00 (+5.58%)</td><td>31.50 (-6.51%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>202.20 (n/a)</td><td>161.70 (n/a)</td><td>156.00 (n/a)</td><td>114.60 (n/a)</td><td>33.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (+18.15%)</td><td>0.11 (+10.70%)</td><td>0.12 (+18.93%)</td><td>0.08 (-4.44%)</td><td>0.03 <b>(+32.67%)</b></td><td>213.00 (+4.62%)</td><td>151.30 (-7.92%)</td><td>135.50 (-15.94%)</td><td>111.50 (-15.34%)</td><td>40.61 <b>(+21.38%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>164.32 (n/a)</td><td>161.20 (n/a)</td><td>131.70 (n/a)</td><td>33.46 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 <b>(-20.01%)</b></td><td>0.11 (-6.37%)</td><td>0.12 (+1.81%)</td><td>0.07 (-8.59%)</td><td>0.03 <b>(-23.84%)</b></td><td>275.40 (+9.37%)</td><td>191.90 (+5.63%)</td><td>174.80 (-1.74%)</td><td>146.40 <b>(+25.02%)</b></td><td>52.48 (+5.72%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>251.80 (n/a)</td><td>181.68 (n/a)</td><td>177.90 (n/a)</td><td>117.10 (n/a)</td><td>49.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (+10.35%)</td><td>0.11 (+6.39%)</td><td>0.13 (+19.02%)</td><td>0.06 <b>(-24.71%)</b></td><td>0.03 <b>(+96.73%)</b></td><td>267.90 <b>(+32.82%)</b></td><td>164.04 (+0.31%)</td><td>130.80 (-15.94%)</td><td>125.10 (-9.41%)</td><td>60.83 <b>(+134.71%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.70 (n/a)</td><td>163.54 (n/a)</td><td>155.60 (n/a)</td><td>138.10 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (-12.59%)</td><td>0.12 (-5.65%)</td><td>0.12 (+6.71%)</td><td>0.11 (-4.88%)</td><td>0.01 <b>(-41.64%)</b></td><td>192.90 (+5.12%)</td><td>170.32 (+4.49%)</td><td>169.30 (-6.26%)</td><td>145.00 (+14.35%)</td><td>18.33 <b>(-31.49%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>183.50 (n/a)</td><td>163.00 (n/a)</td><td>180.60 (n/a)</td><td>126.80 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (+13.76%)</td><td>0.11 (+3.50%)</td><td>0.11 (-1.46%)</td><td>0.08 (+13.29%)</td><td>0.02 (+6.26%)</td><td>194.00 (-11.70%)</td><td>156.06 (-3.97%)</td><td>154.60 (+1.51%)</td><td>109.80 (-12.09%)</td><td>31.02 (-19.66%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.70 (n/a)</td><td>162.52 (n/a)</td><td>152.30 (n/a)</td><td>124.90 (n/a)</td><td>38.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (-18.73%)</td><td>0.10 (-8.89%)</td><td>0.10 (+4.81%)</td><td>0.06 <b>(-34.49%)</b></td><td>0.02 (-8.21%)</td><td>310.60 <b>(+52.63%)</b></td><td>203.28 (+12.37%)</td><td>191.40 (-4.59%)</td><td>149.50 <b>(+23.05%)</b></td><td>63.13 <b>(+79.91%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>203.50 (n/a)</td><td>180.90 (n/a)</td><td>200.60 (n/a)</td><td>121.50 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (-0.19%)</td><td>0.10 (+2.01%)</td><td>0.10 (+1.57%)</td><td>0.08 (+6.41%)</td><td>0.01 (-8.11%)</td><td>205.60 (-6.03%)</td><td>168.26 (-2.37%)</td><td>163.40 (-1.57%)</td><td>149.80 (+0.20%)</td><td>22.90 (-15.87%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>218.80 (n/a)</td><td>172.34 (n/a)</td><td>166.00 (n/a)</td><td>149.50 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 <b>(-36.95%)</b></td><td>0.08 <b>(-22.58%)</b></td><td>0.09 (-16.45%)</td><td>0.06 <b>(-24.81%)</b></td><td>0.01 <b>(-51.49%)</b></td><td>292.90 <b>(+33.02%)</b></td><td>226.00 <b>(+26.95%)</b></td><td>210.10 (+19.72%)</td><td>196.30 <b>(+58.56%)</b></td><td>38.75 (+8.40%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>220.20 (n/a)</td><td>178.02 (n/a)</td><td>175.50 (n/a)</td><td>123.80 (n/a)</td><td>35.74 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (-4.25%)</td><td>0.10 (+10.15%)</td><td>0.10 <b>(+23.02%)</b></td><td>0.08 <b>(+26.40%)</b></td><td>0.01 <b>(-34.13%)</b></td><td>206.40 <b>(-20.89%)</b></td><td>173.10 (-11.30%)</td><td>157.40 (-18.70%)</td><td>156.40 (+4.48%)</td><td>22.95 <b>(-46.65%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>260.90 (n/a)</td><td>195.16 (n/a)</td><td>193.60 (n/a)</td><td>149.70 (n/a)</td><td>43.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (+9.65%)</td><td>0.08 (-9.57%)</td><td>0.08 (-7.37%)</td><td>0.06 <b>(-27.44%)</b></td><td>0.02 <b>(+186.26%)</b></td><td>306.20 <b>(+37.80%)</b></td><td>227.86 (+14.54%)</td><td>211.50 (+7.96%)</td><td>167.90 (-8.80%)</td><td>51.56 <b>(+259.84%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>198.94 (n/a)</td><td>195.90 (n/a)</td><td>184.10 (n/a)</td><td>14.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 <b>(+64.99%)</b></td><td>0.11 <b>(+37.29%)</b></td><td>0.10 <b>(+29.81%)</b></td><td>0.09 <b>(+26.60%)</b></td><td>0.02 <b>(+251.81%)</b></td><td>179.20 <b>(-21.02%)</b></td><td>153.20 <b>(-25.80%)</b></td><td>157.50 <b>(-22.98%)</b></td><td>114.20 <b>(-39.38%)</b></td><td>23.76 <b>(+61.00%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>206.46 (n/a)</td><td>204.50 (n/a)</td><td>188.40 (n/a)</td><td>14.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 <b>(+22.30%)</b></td><td>0.09 (+18.60%)</td><td>0.09 (+7.26%)</td><td>0.08 <b>(+46.18%)</b></td><td>0.02 (+6.67%)</td><td>224.90 <b>(-31.58%)</b></td><td>190.12 (-17.24%)</td><td>193.30 (-6.75%)</td><td>136.80 (-18.23%)</td><td>36.51 <b>(-41.22%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>328.70 (n/a)</td><td>229.72 (n/a)</td><td>207.30 (n/a)</td><td>167.30 (n/a)</td><td>62.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (+18.15%)</td><td>0.09 <b>(+28.69%)</b></td><td>0.08 (+17.61%)</td><td>0.07 <b>(+43.02%)</b></td><td>0.01 <b>(-32.61%)</b></td><td>228.70 <b>(-30.08%)</b></td><td>193.66 <b>(-24.21%)</b></td><td>193.10 (-14.97%)</td><td>172.70 (-15.34%)</td><td>21.63 <b>(-60.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>327.10 (n/a)</td><td>255.52 (n/a)</td><td>227.10 (n/a)</td><td>204.00 (n/a)</td><td>54.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 <b>(+32.83%)</b></td><td>0.22 (+12.12%)</td><td>0.20 (+3.85%)</td><td>0.19 (+6.44%)</td><td>0.03 <b>(+254.89%)</b></td><td>168.50 (-6.02%)</td><td>153.56 (-9.41%)</td><td>163.10 (-3.72%)</td><td>117.90 <b>(-24.71%)</b></td><td>20.79 <b>(+149.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>179.30 (n/a)</td><td>169.52 (n/a)</td><td>169.40 (n/a)</td><td>156.60 (n/a)</td><td>8.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (+13.57%)</td><td>0.22 (-0.44%)</td><td>0.23 (+13.42%)</td><td>0.16 (-17.16%)</td><td>0.05 <b>(+98.97%)</b></td><td>204.00 <b>(+20.71%)</b></td><td>157.18 (+4.29%)</td><td>140.70 (-11.84%)</td><td>113.60 (-11.94%)</td><td>39.08 <b>(+120.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>169.00 (n/a)</td><td>150.72 (n/a)</td><td>159.60 (n/a)</td><td>129.00 (n/a)</td><td>17.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.27 (-4.20%)</td><td>0.26 (+6.14%)</td><td>0.27 (+3.70%)</td><td>0.23 <b>(+30.44%)</b></td><td>0.02 <b>(-59.10%)</b></td><td>175.00 <b>(-23.35%)</b></td><td>159.88 (-8.04%)</td><td>154.00 (-3.57%)</td><td>149.50 (+4.33%)</td><td>11.09 <b>(-67.57%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>228.30 (n/a)</td><td>173.86 (n/a)</td><td>159.70 (n/a)</td><td>143.30 (n/a)</td><td>34.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 <b>(+21.76%)</b></td><td>0.22 (+12.99%)</td><td>0.21 (+14.28%)</td><td>0.18 (+5.37%)</td><td>0.03 <b>(+125.31%)</b></td><td>181.50 (-5.07%)</td><td>155.12 (-10.10%)</td><td>153.90 (-12.51%)</td><td>127.50 (-17.85%)</td><td>24.77 <b>(+78.28%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>191.20 (n/a)</td><td>172.54 (n/a)</td><td>175.90 (n/a)</td><td>155.20 (n/a)</td><td>13.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.32 (+5.05%)</td><td>0.27 (+19.28%)</td><td>0.27 <b>(+21.89%)</b></td><td>0.21 <b>(+25.39%)</b></td><td>0.05 (-13.79%)</td><td>196.80 <b>(-20.26%)</b></td><td>156.40 (-17.68%)</td><td>154.20 (-17.98%)</td><td>127.50 (-4.78%)</td><td>27.98 <b>(-34.71%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>246.80 (n/a)</td><td>189.98 (n/a)</td><td>188.00 (n/a)</td><td>133.90 (n/a)</td><td>42.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 <b>(+33.36%)</b></td><td>0.23 <b>(+23.65%)</b></td><td>0.24 <b>(+30.77%)</b></td><td>0.18 (+0.57%)</td><td>0.04 <b>(+227.81%)</b></td><td>180.30 (-0.55%)</td><td>142.94 (-17.49%)</td><td>134.70 <b>(-23.51%)</b></td><td>117.50 <b>(-25.02%)</b></td><td>24.99 <b>(+146.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>173.24 (n/a)</td><td>176.10 (n/a)</td><td>156.70 (n/a)</td><td>10.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.32 (-2.67%)</td><td>0.23 (+4.05%)</td><td>0.24 (+18.43%)</td><td>0.14 (-9.88%)</td><td>0.07 (+2.19%)</td><td>257.90 (+10.92%)</td><td>170.10 (-2.45%)</td><td>154.30 (-15.54%)</td><td>113.40 (+2.72%)</td><td>55.55 <b>(+23.00%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>232.50 (n/a)</td><td>174.38 (n/a)</td><td>182.70 (n/a)</td><td>110.40 (n/a)</td><td>45.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 <b>(+33.02%)</b></td><td>0.24 <b>(+23.09%)</b></td><td>0.26 <b>(+40.90%)</b></td><td>0.16 (-7.88%)</td><td>0.05 <b>(+184.99%)</b></td><td>200.40 (+8.56%)</td><td>144.64 (-15.58%)</td><td>126.30 <b>(-29.04%)</b></td><td>111.20 <b>(-24.81%)</b></td><td>36.39 <b>(+134.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>184.60 (n/a)</td><td>171.34 (n/a)</td><td>178.00 (n/a)</td><td>147.90 (n/a)</td><td>15.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.32 <b>(+29.32%)</b></td><td>0.24 <b>(+24.09%)</b></td><td>0.21 (+15.39%)</td><td>0.19 (+14.97%)</td><td>0.05 <b>(+65.00%)</b></td><td>189.40 (-13.00%)</td><td>159.54 (-18.28%)</td><td>173.00 (-13.33%)</td><td>116.90 <b>(-22.69%)</b></td><td>29.31 (+13.09%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>217.70 (n/a)</td><td>195.22 (n/a)</td><td>199.60 (n/a)</td><td>151.20 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (-7.94%)</td><td>0.20 (+0.65%)</td><td>0.21 (-1.03%)</td><td>0.18 (+16.44%)</td><td>0.02 <b>(-46.74%)</b></td><td>185.00 (-14.11%)</td><td>163.24 (-2.61%)</td><td>158.00 (+1.02%)</td><td>144.40 (+8.57%)</td><td>15.58 <b>(-50.68%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>215.40 (n/a)</td><td>167.62 (n/a)</td><td>156.40 (n/a)</td><td>133.00 (n/a)</td><td>31.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (+11.10%)</td><td>0.20 (+3.94%)</td><td>0.19 (-2.79%)</td><td>0.17 (+1.29%)</td><td>0.03 <b>(+58.01%)</b></td><td>210.90 (-1.26%)</td><td>180.36 (-3.07%)</td><td>186.20 (+2.87%)</td><td>151.40 (-9.99%)</td><td>23.45 <b>(+37.41%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>186.08 (n/a)</td><td>181.00 (n/a)</td><td>168.20 (n/a)</td><td>17.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (+3.70%)</td><td>0.21 (+13.32%)</td><td>0.20 (+15.16%)</td><td>0.18 <b>(+65.30%)</b></td><td>0.03 <b>(-39.45%)</b></td><td>181.80 <b>(-39.50%)</b></td><td>160.46 (-16.97%)</td><td>161.70 (-13.16%)</td><td>126.30 (-3.59%)</td><td>22.59 <b>(-65.40%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>300.50 (n/a)</td><td>193.26 (n/a)</td><td>186.20 (n/a)</td><td>131.00 (n/a)</td><td>65.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (-15.17%)</td><td>0.18 (-0.80%)</td><td>0.19 (+2.74%)</td><td>0.16 (+5.10%)</td><td>0.02 <b>(-46.47%)</b></td><td>224.10 (-4.84%)</td><td>194.70 (-0.93%)</td><td>186.70 (-2.66%)</td><td>177.30 (+17.89%)</td><td>20.23 <b>(-40.95%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>235.50 (n/a)</td><td>196.52 (n/a)</td><td>191.80 (n/a)</td><td>150.40 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (+18.26%)</td><td>0.18 (+6.11%)</td><td>0.19 (+12.37%)</td><td>0.15 (-4.09%)</td><td>0.03 <b>(+127.09%)</b></td><td>221.30 (+4.24%)</td><td>184.28 (-3.86%)</td><td>173.80 (-11.01%)</td><td>147.50 (-15.42%)</td><td>32.99 <b>(+108.35%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>191.68 (n/a)</td><td>195.30 (n/a)</td><td>174.40 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 <b>(+47.89%)</b></td><td>0.13 <b>(+25.40%)</b></td><td>0.12 (+8.41%)</td><td>0.10 (+15.60%)</td><td>0.03 <b>(+158.18%)</b></td><td>201.40 (-13.49%)</td><td>162.66 (-17.93%)</td><td>173.70 (-7.75%)</td><td>120.40 <b>(-32.40%)</b></td><td>34.60 <b>(+49.73%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>198.20 (n/a)</td><td>188.30 (n/a)</td><td>178.10 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (-7.79%)</td><td>0.11 (-3.80%)</td><td>0.11 (-2.29%)</td><td>0.09 (-10.89%)</td><td>0.02 (-0.94%)</td><td>240.40 (+12.23%)</td><td>188.08 (+4.40%)</td><td>182.10 (+2.36%)</td><td>153.20 (+8.42%)</td><td>34.20 <b>(+21.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>180.16 (n/a)</td><td>177.90 (n/a)</td><td>141.30 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (+6.08%)</td><td>0.15 (+8.87%)</td><td>0.14 (+8.97%)</td><td>0.10 (+3.96%)</td><td>0.04 <b>(+25.19%)</b></td><td>201.90 (-3.81%)</td><td>148.00 (-6.74%)</td><td>143.10 (-8.27%)</td><td>108.70 (-5.72%)</td><td>38.51 (+12.05%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>209.90 (n/a)</td><td>158.70 (n/a)</td><td>156.00 (n/a)</td><td>115.30 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (-7.54%)</td><td>0.13 (-1.28%)</td><td>0.14 (+14.41%)</td><td>0.09 (-17.02%)</td><td>0.02 <b>(+25.73%)</b></td><td>218.00 <b>(+20.51%)</b></td><td>162.64 (+2.81%)</td><td>143.10 (-12.58%)</td><td>139.10 (+8.16%)</td><td>33.34 <b>(+65.12%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>180.90 (n/a)</td><td>158.20 (n/a)</td><td>163.70 (n/a)</td><td>128.60 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (+2.46%)</td><td>0.13 (+3.97%)</td><td>0.12 (-6.85%)</td><td>0.10 <b>(+33.38%)</b></td><td>0.02 <b>(-36.40%)</b></td><td>199.60 <b>(-25.05%)</b></td><td>166.16 (-7.94%)</td><td>167.50 (+7.37%)</td><td>130.60 (-2.39%)</td><td>24.47 <b>(-54.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>266.30 (n/a)</td><td>180.50 (n/a)</td><td>156.00 (n/a)</td><td>133.80 (n/a)</td><td>54.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 <b>(+27.16%)</b></td><td>0.12 (-3.66%)</td><td>0.12 (-3.82%)</td><td>0.08 <b>(-25.47%)</b></td><td>0.03 <b>(+245.24%)</b></td><td>258.60 <b>(+34.20%)</b></td><td>187.32 (+9.83%)</td><td>174.80 (+3.99%)</td><td>121.40 <b>(-21.37%)</b></td><td>50.57 <b>(+257.05%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>170.56 (n/a)</td><td>168.10 (n/a)</td><td>154.40 (n/a)</td><td>14.16 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (+13.58%)</td><td>0.10 (-3.20%)</td><td>0.10 (-9.48%)</td><td>0.08 <b>(-21.98%)</b></td><td>0.03 <b>(+244.51%)</b></td><td>270.50 <b>(+28.20%)</b></td><td>210.62 (+8.35%)</td><td>210.90 (+10.48%)</td><td>157.30 (-11.93%)</td><td>52.67 <b>(+276.53%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>194.38 (n/a)</td><td>190.90 (n/a)</td><td>178.60 (n/a)</td><td>13.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 <b>(+38.24%)</b></td><td>0.13 <b>(+22.89%)</b></td><td>0.13 <b>(+26.15%)</b></td><td>0.10 (+2.55%)</td><td>0.02 <b>(+208.20%)</b></td><td>209.40 (-2.47%)</td><td>163.28 (-16.75%)</td><td>155.70 <b>(-20.72%)</b></td><td>128.10 <b>(-27.63%)</b></td><td>30.40 <b>(+120.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>196.14 (n/a)</td><td>196.40 (n/a)</td><td>177.00 (n/a)</td><td>13.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 <b>(+31.05%)</b></td><td>0.15 (+5.47%)</td><td>0.14 (-1.92%)</td><td>0.12 (-5.11%)</td><td>0.03 <b>(+203.98%)</b></td><td>210.30 (+5.41%)</td><td>174.48 (-2.75%)</td><td>179.30 (+1.99%)</td><td>125.40 <b>(-23.68%)</b></td><td>30.87 <b>(+133.18%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>179.42 (n/a)</td><td>175.80 (n/a)</td><td>164.30 (n/a)</td><td>13.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 <b>(+26.60%)</b></td><td>0.16 (+5.94%)</td><td>0.14 (-3.54%)</td><td>0.13 (-0.57%)</td><td>0.03 <b>(+187.70%)</b></td><td>183.60 (+0.60%)</td><td>160.12 (-3.64%)</td><td>173.40 (+3.65%)</td><td>119.10 <b>(-21.02%)</b></td><td>26.00 <b>(+126.00%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>166.16 (n/a)</td><td>167.30 (n/a)</td><td>150.80 (n/a)</td><td>11.51 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (-7.48%)</td><td>0.17 (-2.65%)</td><td>0.17 (+6.73%)</td><td>0.15 (-3.86%)</td><td>0.01 <b>(-40.98%)</b></td><td>162.40 (+3.97%)</td><td>143.86 (+1.84%)</td><td>143.90 (-6.32%)</td><td>129.60 (+8.09%)</td><td>12.15 <b>(-33.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>156.20 (n/a)</td><td>141.26 (n/a)</td><td>153.60 (n/a)</td><td>119.90 (n/a)</td><td>18.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (+0.21%)</td><td>0.16 (-0.19%)</td><td>0.16 (+12.99%)</td><td>0.12 (+4.33%)</td><td>0.03 <b>(-27.05%)</b></td><td>198.20 (-4.16%)</td><td>156.92 (-2.22%)</td><td>155.50 (-11.50%)</td><td>118.00 (-0.25%)</td><td>28.42 <b>(-27.56%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>206.80 (n/a)</td><td>160.48 (n/a)</td><td>175.70 (n/a)</td><td>118.30 (n/a)</td><td>39.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 <b>(+44.28%)</b></td><td>0.17 <b>(+20.47%)</b></td><td>0.17 <b>(+23.67%)</b></td><td>0.12 (-5.12%)</td><td>0.05 <b>(+198.73%)</b></td><td>213.30 (+5.39%)</td><td>156.54 (-12.79%)</td><td>147.50 (-19.13%)</td><td>104.50 <b>(-30.66%)</b></td><td>41.52 <b>(+122.26%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.40 (n/a)</td><td>179.50 (n/a)</td><td>182.40 (n/a)</td><td>150.70 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (+7.22%)</td><td>0.13 (-8.62%)</td><td>0.11 (-18.12%)</td><td>0.11 <b>(-20.94%)</b></td><td>0.03 <b>(+213.94%)</b></td><td>233.80 <b>(+26.45%)</b></td><td>197.24 (+12.89%)</td><td>216.40 <b>(+22.12%)</b></td><td>147.20 (-6.78%)</td><td>38.77 <b>(+275.73%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>184.90 (n/a)</td><td>174.72 (n/a)</td><td>177.20 (n/a)</td><td>157.90 (n/a)</td><td>10.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 <b>(-21.36%)</b></td><td>0.13 (-1.95%)</td><td>0.13 (+11.32%)</td><td>0.12 (+5.54%)</td><td>0.01 <b>(-69.67%)</b></td><td>199.40 (-5.27%)</td><td>187.88 (-0.79%)</td><td>188.60 (-10.15%)</td><td>169.50 <b>(+27.16%)</b></td><td>12.20 <b>(-63.56%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>210.50 (n/a)</td><td>189.38 (n/a)</td><td>209.90 (n/a)</td><td>133.30 (n/a)</td><td>33.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (-9.04%)</td><td>0.14 (+3.39%)</td><td>0.13 (+12.47%)</td><td>0.12 (+3.52%)</td><td>0.01 <b>(-46.90%)</b></td><td>206.00 (-3.38%)</td><td>181.76 (-4.68%)</td><td>183.60 (-11.09%)</td><td>162.40 (+9.95%)</td><td>16.21 <b>(-44.27%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>213.20 (n/a)</td><td>190.68 (n/a)</td><td>206.50 (n/a)</td><td>147.70 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (-8.47%)</td><td>0.10 (-6.68%)</td><td>0.11 (+4.71%)</td><td>0.05 <b>(-43.16%)</b></td><td>0.03 <b>(+47.64%)</b></td><td>364.60 <b>(+75.88%)</b></td><td>207.50 (+16.03%)</td><td>175.40 (-4.52%)</td><td>145.10 (+9.26%)</td><td>88.92 <b>(+220.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>207.30 (n/a)</td><td>178.84 (n/a)</td><td>183.70 (n/a)</td><td>132.80 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (+5.06%)</td><td>0.11 (+4.22%)</td><td>0.12 (+9.74%)</td><td>0.08 (-19.89%)</td><td>0.02 <b>(+59.72%)</b></td><td>238.40 <b>(+24.82%)</b></td><td>169.14 (-1.32%)</td><td>159.00 (-8.88%)</td><td>130.80 (-4.80%)</td><td>41.71 <b>(+98.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>171.40 (n/a)</td><td>174.50 (n/a)</td><td>137.40 (n/a)</td><td>21.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (-0.25%)</td><td>0.10 (-10.63%)</td><td>0.10 (-8.23%)</td><td>0.08 <b>(-22.13%)</b></td><td>0.03 <b>(+61.80%)</b></td><td>237.90 <b>(+28.46%)</b></td><td>185.58 (+15.54%)</td><td>180.20 (+8.95%)</td><td>131.80 (+0.23%)</td><td>43.32 <b>(+113.42%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>185.20 (n/a)</td><td>160.62 (n/a)</td><td>165.40 (n/a)</td><td>131.50 (n/a)</td><td>20.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (-7.83%)</td><td>0.11 (-0.97%)</td><td>0.11 (-8.14%)</td><td>0.09 (+10.75%)</td><td>0.02 (-14.59%)</td><td>198.50 (-9.73%)</td><td>164.94 (-0.12%)</td><td>170.50 (+8.81%)</td><td>130.20 (+8.50%)</td><td>30.20 (-17.57%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>219.90 (n/a)</td><td>165.14 (n/a)</td><td>156.70 (n/a)</td><td>120.00 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (+19.47%)</td><td>0.12 (+11.75%)</td><td>0.10 (+4.33%)</td><td>0.09 <b>(+33.41%)</b></td><td>0.03 (+16.15%)</td><td>203.30 <b>(-25.06%)</b></td><td>167.60 (-11.26%)</td><td>183.50 (-4.13%)</td><td>107.50 (-16.28%)</td><td>40.16 <b>(-26.65%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>271.30 (n/a)</td><td>188.86 (n/a)</td><td>191.40 (n/a)</td><td>128.40 (n/a)</td><td>54.75 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (-6.08%)</td><td>0.12 (+2.28%)</td><td>0.12 (+16.33%)</td><td>0.06 <b>(-34.23%)</b></td><td>0.04 <b>(+34.80%)</b></td><td>307.50 <b>(+52.08%)</b></td><td>176.30 (+6.17%)</td><td>149.70 (-14.06%)</td><td>116.50 (+6.49%)</td><td>78.80 <b>(+126.94%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>202.20 (n/a)</td><td>166.06 (n/a)</td><td>174.20 (n/a)</td><td>109.40 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (+19.84%)</td><td>0.10 (+8.25%)</td><td>0.10 (+14.44%)</td><td>0.07 (-6.95%)</td><td>0.02 <b>(+104.68%)</b></td><td>268.20 (+7.45%)</td><td>200.56 (-4.95%)</td><td>184.00 (-12.59%)</td><td>151.50 (-16.53%)</td><td>45.61 <b>(+83.99%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>249.60 (n/a)</td><td>211.00 (n/a)</td><td>210.50 (n/a)</td><td>181.50 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (-14.62%)</td><td>0.10 (+3.99%)</td><td>0.09 (+0.66%)</td><td>0.09 <b>(+42.75%)</b></td><td>0.01 <b>(-62.40%)</b></td><td>208.00 <b>(-29.97%)</b></td><td>191.32 (-8.55%)</td><td>195.30 (-0.66%)</td><td>168.00 (+17.07%)</td><td>17.58 <b>(-69.27%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>297.00 (n/a)</td><td>209.20 (n/a)</td><td>196.60 (n/a)</td><td>143.50 (n/a)</td><td>57.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.73 (-4.14%)</td><td>0.55 (-4.03%)</td><td>0.52 (-8.50%)</td><td>0.47 (+9.39%)</td><td>0.11 (-15.12%)</td><td>210.10 (-8.57%)</td><td>185.00 (+3.00%)</td><td>188.20 (+9.29%)</td><td>134.20 (+4.35%)</td><td>30.45 <b>(-20.11%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.76 (n/a)</td><td>0.57 (n/a)</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.13 (n/a)</td><td>229.80 (n/a)</td><td>179.62 (n/a)</td><td>172.20 (n/a)</td><td>128.60 (n/a)</td><td>38.12 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.89 (+12.51%)</td><td>0.70 <b>(+30.36%)</b></td><td>0.73 <b>(+33.68%)</b></td><td>0.58 <b>(+79.02%)</b></td><td>0.13 <b>(-23.51%)</b></td><td>170.40 <b>(-44.15%)</b></td><td>143.68 <b>(-27.56%)</b></td><td>135.30 <b>(-25.17%)</b></td><td>110.60 (-11.16%)</td><td>25.68 <b>(-61.50%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 (n/a)</td><td>0.54 (n/a)</td><td>0.54 (n/a)</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>305.10 (n/a)</td><td>198.34 (n/a)</td><td>180.80 (n/a)</td><td>124.50 (n/a)</td><td>66.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.79 (+0.14%)</td><td>0.58 (-17.18%)</td><td>0.55 <b>(-22.74%)</b></td><td>0.42 <b>(-31.91%)</b></td><td>0.15 <b>(+105.24%)</b></td><td>235.10 <b>(+46.85%)</b></td><td>176.88 <b>(+25.79%)</b></td><td>178.60 <b>(+29.42%)</b></td><td>124.50 (-0.16%)</td><td>43.23 <b>(+198.63%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.79 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.61 (n/a)</td><td>0.07 (n/a)</td><td>160.10 (n/a)</td><td>140.62 (n/a)</td><td>138.00 (n/a)</td><td>124.70 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.43 <b>(-33.86%)</b></td><td>0.37 <b>(-34.77%)</b></td><td>0.38 <b>(-34.14%)</b></td><td>0.26 <b>(-45.60%)</b></td><td>0.07 (+0.77%)</td><td>380.10 <b>(+83.89%)</b></td><td>275.78 <b>(+56.62%)</b></td><td>256.60 <b>(+51.83%)</b></td><td>226.90 <b>(+51.17%)</b></td><td>61.19 <b>(+186.27%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.66 (n/a)</td><td>0.56 (n/a)</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.07 (n/a)</td><td>206.70 (n/a)</td><td>176.08 (n/a)</td><td>169.00 (n/a)</td><td>150.10 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.53 (+0.77%)</td><td>0.41 (-9.98%)</td><td>0.41 (-18.70%)</td><td>0.20 <b>(-40.41%)</b></td><td>0.13 <b>(+50.09%)</b></td><td>361.70 <b>(+67.76%)</b></td><td>203.70 <b>(+20.88%)</b></td><td>179.80 <b>(+22.98%)</b></td><td>138.90 (-0.79%)</td><td>91.14 <b>(+160.74%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>215.60 (n/a)</td><td>168.52 (n/a)</td><td>146.20 (n/a)</td><td>140.00 (n/a)</td><td>34.95 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.53 (-13.69%)</td><td>0.45 (-5.12%)</td><td>0.47 (+11.94%)</td><td>0.34 (-11.77%)</td><td>0.08 <b>(-25.88%)</b></td><td>215.90 (+13.33%)</td><td>167.74 (+4.34%)</td><td>158.40 (-10.66%)</td><td>138.80 (+15.86%)</td><td>31.30 (-3.06%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.62 (n/a)</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.10 (n/a)</td><td>190.50 (n/a)</td><td>160.76 (n/a)</td><td>177.30 (n/a)</td><td>119.80 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.60 (+11.02%)</td><td>0.47 (+11.31%)</td><td>0.47 <b>(+22.10%)</b></td><td>0.34 (-3.42%)</td><td>0.12 <b>(+49.83%)</b></td><td>215.40 (+3.56%)</td><td>166.06 (-7.51%)</td><td>157.40 (-18.11%)</td><td>123.90 (-9.89%)</td><td>44.63 <b>(+36.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>208.00 (n/a)</td><td>179.54 (n/a)</td><td>192.20 (n/a)</td><td>137.50 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.46 (-16.09%)</td><td>0.39 (-9.13%)</td><td>0.37 (-9.38%)</td><td>0.32 (-8.32%)</td><td>0.05 <b>(-29.54%)</b></td><td>231.30 (+9.05%)</td><td>194.08 (+9.14%)</td><td>197.30 (+10.35%)</td><td>159.30 (+19.15%)</td><td>27.21 (-6.81%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>212.10 (n/a)</td><td>177.82 (n/a)</td><td>178.80 (n/a)</td><td>133.70 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (+8.97%)</td><td>0.23 (+4.60%)</td><td>0.23 (+2.10%)</td><td>0.20 (+19.72%)</td><td>0.04 (-5.01%)</td><td>185.30 (-16.46%)</td><td>161.34 (-5.15%)</td><td>161.00 (-2.07%)</td><td>127.90 (-8.18%)</td><td>23.48 <b>(-27.29%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>221.80 (n/a)</td><td>170.10 (n/a)</td><td>164.40 (n/a)</td><td>139.30 (n/a)</td><td>32.30 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.30 (-14.91%)</td><td>0.24 (+4.43%)</td><td>0.27 <b>(+37.05%)</b></td><td>0.16 (-4.30%)</td><td>0.06 <b>(-21.80%)</b></td><td>224.90 (+4.46%)</td><td>159.72 (-5.84%)</td><td>139.10 <b>(-27.02%)</b></td><td>122.60 (+17.55%)</td><td>43.66 (-4.16%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>215.30 (n/a)</td><td>169.62 (n/a)</td><td>190.60 (n/a)</td><td>104.30 (n/a)</td><td>45.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (+7.48%)</td><td>0.20 (+5.05%)</td><td>0.20 (-3.35%)</td><td>0.15 <b>(+48.71%)</b></td><td>0.06 (-9.30%)</td><td>249.70 <b>(-32.75%)</b></td><td>190.42 (-9.98%)</td><td>185.70 (+3.45%)</td><td>127.00 (-6.96%)</td><td>48.03 <b>(-47.72%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>371.30 (n/a)</td><td>211.54 (n/a)</td><td>179.50 (n/a)</td><td>136.50 (n/a)</td><td>91.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 <b>(+40.44%)</b></td><td>0.24 (+19.28%)</td><td>0.24 (+18.89%)</td><td>0.15 (-8.22%)</td><td>0.05 <b>(+162.06%)</b></td><td>239.10 (+8.93%)</td><td>162.08 (-12.63%)</td><td>150.50 (-15.92%)</td><td>120.40 <b>(-28.76%)</b></td><td>44.98 <b>(+115.22%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>185.50 (n/a)</td><td>179.00 (n/a)</td><td>169.00 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.38 <b>(+43.48%)</b></td><td>0.26 (+16.60%)</td><td>0.22 (+3.06%)</td><td>0.20 (+12.88%)</td><td>0.08 <b>(+77.96%)</b></td><td>182.00 (-11.39%)</td><td>151.38 (-11.91%)</td><td>164.60 (-2.95%)</td><td>96.40 <b>(-30.30%)</b></td><td>35.92 (+9.39%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>205.40 (n/a)</td><td>171.84 (n/a)</td><td>169.60 (n/a)</td><td>138.30 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.25 (+2.48%)</td><td>0.22 (+9.92%)</td><td>0.23 (+11.92%)</td><td>0.15 <b>(+21.81%)</b></td><td>0.04 (-11.76%)</td><td>246.40 (-17.89%)</td><td>177.38 (-11.03%)</td><td>159.90 (-10.67%)</td><td>147.70 (-2.44%)</td><td>41.20 <b>(-31.03%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>300.10 (n/a)</td><td>199.36 (n/a)</td><td>179.00 (n/a)</td><td>151.40 (n/a)</td><td>59.74 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (-14.29%)</td><td>0.18 (-16.00%)</td><td>0.18 (-15.37%)</td><td>0.16 (-17.54%)</td><td>0.02 (-15.01%)</td><td>225.10 <b>(+21.28%)</b></td><td>202.88 (+19.06%)</td><td>203.10 (+18.22%)</td><td>175.90 (+16.72%)</td><td>17.72 (+17.68%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>185.60 (n/a)</td><td>170.40 (n/a)</td><td>171.80 (n/a)</td><td>150.70 (n/a)</td><td>15.06 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 <b>(-27.52%)</b></td><td>0.18 (-13.44%)</td><td>0.18 (-12.20%)</td><td>0.17 (+1.30%)</td><td>0.01 <b>(-72.53%)</b></td><td>223.00 (-1.28%)</td><td>211.04 (+13.11%)</td><td>209.80 (+13.90%)</td><td>194.40 <b>(+37.97%)</b></td><td>11.87 <b>(-61.37%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>225.90 (n/a)</td><td>186.58 (n/a)</td><td>184.20 (n/a)</td><td>140.90 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.30 (+12.40%)</td><td>0.27 <b>(+30.73%)</b></td><td>0.26 <b>(+25.92%)</b></td><td>0.23 <b>(+109.42%)</b></td><td>0.02 <b>(-58.40%)</b></td><td>175.40 <b>(-52.26%)</b></td><td>154.58 <b>(-29.61%)</b></td><td>156.90 <b>(-20.56%)</b></td><td>138.80 (-11.03%)</td><td>14.28 <b>(-83.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>367.40 (n/a)</td><td>219.62 (n/a)</td><td>197.50 (n/a)</td><td>156.00 (n/a)</td><td>85.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.33 (-5.66%)</td><td>0.27 (-10.02%)</td><td>0.26 (-11.55%)</td><td>0.23 (-10.05%)</td><td>0.04 (-3.95%)</td><td>177.20 (+11.17%)</td><td>156.28 (+11.25%)</td><td>160.60 (+13.02%)</td><td>124.70 (+6.04%)</td><td>21.27 (+11.52%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>159.40 (n/a)</td><td>140.48 (n/a)</td><td>142.10 (n/a)</td><td>117.60 (n/a)</td><td>19.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 (+3.79%)</td><td>0.23 (+3.89%)</td><td>0.22 (+4.84%)</td><td>0.21 (+3.89%)</td><td>0.03 (+2.52%)</td><td>194.70 (-3.71%)</td><td>178.10 (-3.77%)</td><td>182.90 (-4.64%)</td><td>148.70 (-3.63%)</td><td>17.69 (-5.23%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>202.20 (n/a)</td><td>185.08 (n/a)</td><td>191.80 (n/a)</td><td>154.30 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (-15.25%)</td><td>0.25 (+10.05%)</td><td>0.26 <b>(+25.16%)</b></td><td>0.21 <b>(+20.66%)</b></td><td>0.03 <b>(-54.67%)</b></td><td>195.70 (-17.11%)</td><td>163.46 (-12.81%)</td><td>159.30 <b>(-20.11%)</b></td><td>140.50 (+18.07%)</td><td>20.43 <b>(-52.55%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>236.10 (n/a)</td><td>187.48 (n/a)</td><td>199.40 (n/a)</td><td>119.00 (n/a)</td><td>43.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (+13.44%)</td><td>0.25 (+9.30%)</td><td>0.24 (+6.65%)</td><td>0.22 (+6.02%)</td><td>0.03 <b>(+59.63%)</b></td><td>182.50 (-5.64%)</td><td>163.90 (-8.02%)</td><td>169.80 (-6.24%)</td><td>141.20 (-11.81%)</td><td>17.58 <b>(+32.72%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>193.40 (n/a)</td><td>178.20 (n/a)</td><td>181.10 (n/a)</td><td>160.10 (n/a)</td><td>13.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (-10.55%)</td><td>0.23 (-4.64%)</td><td>0.24 (+7.62%)</td><td>0.16 (-15.21%)</td><td>0.05 (-1.08%)</td><td>261.30 (+17.92%)</td><td>190.16 (+6.15%)</td><td>169.30 (-7.08%)</td><td>140.80 (+11.83%)</td><td>48.29 <b>(+36.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>221.60 (n/a)</td><td>179.14 (n/a)</td><td>182.20 (n/a)</td><td>125.90 (n/a)</td><td>35.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (-19.85%)</td><td>0.20 (-3.58%)</td><td>0.20 (-11.71%)</td><td>0.19 <b>(+46.68%)</b></td><td>0.01 <b>(-86.17%)</b></td><td>217.20 <b>(-31.83%)</b></td><td>205.86 (-2.86%)</td><td>203.30 (+13.26%)</td><td>198.20 <b>(+24.73%)</b></td><td>7.85 <b>(-88.20%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>318.60 (n/a)</td><td>211.92 (n/a)</td><td>179.50 (n/a)</td><td>158.90 (n/a)</td><td>66.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 <b>(-24.26%)</b></td><td>0.22 (-4.18%)</td><td>0.20 (-17.50%)</td><td>0.18 <b>(+40.73%)</b></td><td>0.04 <b>(-55.33%)</b></td><td>224.30 <b>(-28.93%)</b></td><td>191.44 (-4.17%)</td><td>205.10 <b>(+21.22%)</b></td><td>157.30 <b>(+32.07%)</b></td><td>30.19 <b>(-59.88%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>315.60 (n/a)</td><td>199.78 (n/a)</td><td>169.20 (n/a)</td><td>119.10 (n/a)</td><td>75.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 <b>(+27.21%)</b></td><td>0.20 (+3.72%)</td><td>0.19 (-5.03%)</td><td>0.15 (+3.80%)</td><td>0.05 <b>(+55.25%)</b></td><td>226.30 (-3.66%)</td><td>179.16 (-1.82%)</td><td>182.80 (+5.30%)</td><td>119.60 <b>(-21.37%)</b></td><td>38.25 (+12.44%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>234.90 (n/a)</td><td>182.48 (n/a)</td><td>173.60 (n/a)</td><td>152.10 (n/a)</td><td>34.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 <b>(+24.18%)</b></td><td>0.23 (+14.94%)</td><td>0.23 (+16.41%)</td><td>0.16 (+0.55%)</td><td>0.05 <b>(+90.19%)</b></td><td>213.10 (-0.51%)</td><td>158.62 (-10.79%)</td><td>151.70 (-14.10%)</td><td>123.10 (-19.49%)</td><td>36.11 <b>(+51.70%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>214.20 (n/a)</td><td>177.80 (n/a)</td><td>176.60 (n/a)</td><td>152.90 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (-2.18%)</td><td>0.21 (-5.49%)</td><td>0.20 (-3.13%)</td><td>0.18 (+5.73%)</td><td>0.04 <b>(-26.57%)</b></td><td>193.80 (-5.42%)</td><td>167.00 (+3.28%)</td><td>176.60 (+3.27%)</td><td>121.90 (+2.27%)</td><td>29.85 <b>(-26.14%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>204.90 (n/a)</td><td>161.70 (n/a)</td><td>171.00 (n/a)</td><td>119.20 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 (-1.96%)</td><td>0.22 (+11.40%)</td><td>0.23 <b>(+26.95%)</b></td><td>0.17 <b>(+25.39%)</b></td><td>0.05 (-18.89%)</td><td>207.80 <b>(-20.26%)</b></td><td>164.60 (-13.08%)</td><td>148.80 <b>(-21.23%)</b></td><td>122.90 (+1.99%)</td><td>39.02 <b>(-30.84%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>260.60 (n/a)</td><td>189.38 (n/a)</td><td>188.90 (n/a)</td><td>120.50 (n/a)</td><td>56.41 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 <b>(-29.75%)</b></td><td>0.18 <b>(-21.47%)</b></td><td>0.19 (-13.95%)</td><td>0.15 (-13.15%)</td><td>0.03 <b>(-45.75%)</b></td><td>238.30 (+15.12%)</td><td>197.06 <b>(+24.30%)</b></td><td>181.40 (+16.21%)</td><td>158.50 <b>(+42.41%)</b></td><td>34.95 (-8.95%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>207.00 (n/a)</td><td>158.54 (n/a)</td><td>156.10 (n/a)</td><td>111.30 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.27 (-8.26%)</td><td>0.23 (+3.64%)</td><td>0.21 (-6.60%)</td><td>0.19 <b>(+24.14%)</b></td><td>0.03 <b>(-39.93%)</b></td><td>181.90 (-19.44%)</td><td>154.96 (-6.46%)</td><td>162.10 (+7.07%)</td><td>129.40 (+9.01%)</td><td>20.77 <b>(-48.39%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.80 (n/a)</td><td>165.66 (n/a)</td><td>151.40 (n/a)</td><td>118.70 (n/a)</td><td>40.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (-12.27%)</td><td>0.16 (-9.93%)</td><td>0.17 (-2.99%)</td><td>0.13 (-18.95%)</td><td>0.03 (-4.23%)</td><td>276.50 <b>(+23.38%)</b></td><td>220.40 (+11.84%)</td><td>209.10 (+3.11%)</td><td>165.60 (+13.97%)</td><td>42.41 <b>(+40.23%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>224.10 (n/a)</td><td>197.06 (n/a)</td><td>202.80 (n/a)</td><td>145.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 <b>(-22.33%)</b></td><td>0.18 (-11.29%)</td><td>0.20 (+9.03%)</td><td>0.14 (-16.14%)</td><td>0.03 <b>(-25.24%)</b></td><td>240.20 (+19.21%)</td><td>198.04 (+12.32%)</td><td>177.40 (-8.27%)</td><td>162.40 <b>(+28.79%)</b></td><td>37.75 (+17.61%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>201.50 (n/a)</td><td>176.32 (n/a)</td><td>193.40 (n/a)</td><td>126.10 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.99 (+4.45%)</td><td>0.75 (+8.91%)</td><td>0.66 (+5.61%)</td><td>0.60 (+11.31%)</td><td>0.17 (+5.39%)</td><td>219.60 (-10.15%)</td><td>182.14 (-8.20%)</td><td>197.70 (-5.32%)</td><td>131.80 (-4.28%)</td><td>37.27 (-6.19%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.95 (n/a)</td><td>0.69 (n/a)</td><td>0.63 (n/a)</td><td>0.54 (n/a)</td><td>0.16 (n/a)</td><td>244.40 (n/a)</td><td>198.40 (n/a)</td><td>208.80 (n/a)</td><td>137.70 (n/a)</td><td>39.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.83 (-18.35%)</td><td>0.78 (+5.21%)</td><td>0.79 (+9.38%)</td><td>0.70 <b>(+75.11%)</b></td><td>0.05 <b>(-80.08%)</b></td><td>187.90 <b>(-42.89%)</b></td><td>168.72 (-14.51%)</td><td>165.70 (-8.60%)</td><td>158.80 <b>(+22.44%)</b></td><td>11.30 <b>(-85.88%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.01 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>329.00 (n/a)</td><td>197.36 (n/a)</td><td>181.30 (n/a)</td><td>129.70 (n/a)</td><td>80.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.81 <b>(-20.41%)</b></td><td>0.67 (-8.08%)</td><td>0.72 (+3.90%)</td><td>0.38 <b>(-37.03%)</b></td><td>0.17 (+3.66%)</td><td>342.80 <b>(+58.78%)</b></td><td>211.28 (+13.40%)</td><td>183.30 (-3.73%)</td><td>161.90 <b>(+25.70%)</b></td><td>75.19 <b>(+120.80%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.02 (n/a)</td><td>0.73 (n/a)</td><td>0.69 (n/a)</td><td>0.61 (n/a)</td><td>0.17 (n/a)</td><td>215.90 (n/a)</td><td>186.32 (n/a)</td><td>190.40 (n/a)</td><td>128.80 (n/a)</td><td>34.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.00 (-4.44%)</td><td>0.00 (-3.69%)</td><td>0.00 (-2.33%)</td><td>0.00 (-2.38%)</td><td>0.00 <b>(-44.83%)</b></td><td>1009.93 (+2.96%)</td><td>980.41 (+4.10%)</td><td>976.38 (+3.27%)</td><td>948.01 (+4.67%)</td><td>22.99 <b>(-32.24%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>980.88 (n/a)</td><td>941.79 (n/a)</td><td>945.45 (n/a)</td><td>905.75 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.01 (-4.65%)</td><td>0.01 (+1.01%)</td><td>0.01 (+2.53%)</td><td>0.01 (+2.70%)</td><td>0.00 <b>(-41.79%)</b></td><td>1074.13 (-3.05%)</td><td>1021.98 (-1.31%)</td><td>1005.66 (-2.99%)</td><td>997.49 (+4.29%)</td><td>31.41 <b>(-41.50%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1107.91 (n/a)</td><td>1035.56 (n/a)</td><td>1036.65 (n/a)</td><td>956.44 (n/a)</td><td>53.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.98 (+1.34%)</td><td>0.96 (+0.07%)</td><td>0.95 (-0.30%)</td><td>0.94 (-0.11%)</td><td>0.01 <b>(+62.82%)</b></td><td>2227.21 (+0.10%)</td><td>2192.00 (-0.06%)</td><td>2196.06 (+0.30%)</td><td>2142.61 (-1.32%)</td><td>31.21 <b>(+60.17%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2224.90 (n/a)</td><td>2193.42 (n/a)</td><td>2189.41 (n/a)</td><td>2171.23 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.41 (+2.27%)</td><td>0.40 (+0.99%)</td><td>0.40 (+0.53%)</td><td>0.38 (-1.37%)</td><td>0.01 <b>(+96.69%)</b></td><td>1372.59 (+1.40%)</td><td>1315.00 (-0.93%)</td><td>1320.41 (-0.51%)</td><td>1278.61 (-2.24%)</td><td>38.13 <b>(+96.30%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.01 (n/a)</td><td>1353.60 (n/a)</td><td>1327.35 (n/a)</td><td>1327.23 (n/a)</td><td>1307.89 (n/a)</td><td>19.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (-2.40%)</td><td>0.25 (-1.87%)</td><td>0.26 (+3.30%)</td><td>0.23 (-10.10%)</td><td>0.02 <b>(+108.37%)</b></td><td>2319.28 (+11.26%)</td><td>2074.64 (+2.20%)</td><td>1994.88 (-3.19%)</td><td>1985.37 (+2.48%)</td><td>143.07 <b>(+137.88%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2084.48 (n/a)</td><td>2029.92 (n/a)</td><td>2060.68 (n/a)</td><td>1937.29 (n/a)</td><td>60.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.38 (+2.57%)</td><td>0.37 (+0.81%)</td><td>0.37 (+1.14%)</td><td>0.36 (+0.33%)</td><td>0.01 <b>(+84.68%)</b></td><td>1451.41 (-0.34%)</td><td>1417.08 (-0.77%)</td><td>1410.04 (-1.14%)</td><td>1368.21 (-2.50%)</td><td>34.58 <b>(+79.77%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.00 (n/a)</td><td>1456.30 (n/a)</td><td>1428.09 (n/a)</td><td>1426.24 (n/a)</td><td>1403.29 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.79 (-5.26%)</td><td>4.80 (-4.36%)</td><td>4.60 (-6.01%)</td><td>4.38 (+0.18%)</td><td>0.56 (-15.31%)</td><td>239.50 (-0.17%)</td><td>220.38 (+4.24%)</td><td>227.70 (+6.40%)</td><td>181.00 (+5.54%)</td><td>22.82 (-11.25%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>6.11 (n/a)</td><td>5.02 (n/a)</td><td>4.90 (n/a)</td><td>4.37 (n/a)</td><td>0.67 (n/a)</td><td>239.90 (n/a)</td><td>211.42 (n/a)</td><td>214.00 (n/a)</td><td>171.50 (n/a)</td><td>25.71 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.78 (+19.45%)</td><td>4.91 (+8.37%)</td><td>4.77 (+1.84%)</td><td>4.46 <b>(+20.44%)</b></td><td>0.54 (+14.22%)</td><td>235.40 (-16.97%)</td><td>215.40 (-7.83%)</td><td>219.90 (-1.83%)</td><td>181.30 (-16.30%)</td><td>21.95 <b>(-21.84%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>4.84 (n/a)</td><td>4.53 (n/a)</td><td>4.68 (n/a)</td><td>3.70 (n/a)</td><td>0.47 (n/a)</td><td>283.50 (n/a)</td><td>233.70 (n/a)</td><td>224.00 (n/a)</td><td>216.60 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.39 (-3.87%)</td><td>4.95 (-0.06%)</td><td>5.26 (+7.68%)</td><td>4.38 (+7.85%)</td><td>0.51 (-19.81%)</td><td>239.50 (-7.31%)</td><td>213.84 (-0.46%)</td><td>199.30 (-7.13%)</td><td>194.40 (+4.01%)</td><td>22.73 <b>(-21.29%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>5.61 (n/a)</td><td>4.95 (n/a)</td><td>4.89 (n/a)</td><td>4.06 (n/a)</td><td>0.63 (n/a)</td><td>258.40 (n/a)</td><td>214.82 (n/a)</td><td>214.60 (n/a)</td><td>186.90 (n/a)</td><td>28.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>6.12 (-9.43%)</td><td>5.29 (+2.70%)</td><td>5.47 (+9.93%)</td><td>4.27 (+4.41%)</td><td>0.71 <b>(-27.52%)</b></td><td>245.30 (-4.22%)</td><td>201.12 (-3.67%)</td><td>191.80 (-9.01%)</td><td>171.30 (+10.37%)</td><td>28.65 <b>(-20.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>6.76 (n/a)</td><td>5.15 (n/a)</td><td>4.97 (n/a)</td><td>4.09 (n/a)</td><td>0.98 (n/a)</td><td>256.10 (n/a)</td><td>208.78 (n/a)</td><td>210.80 (n/a)</td><td>155.20 (n/a)</td><td>35.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.46 <b>(-25.13%)</b></td><td>7.13 (-12.94%)</td><td>7.26 (-14.32%)</td><td>6.40 (+1.81%)</td><td>0.44 <b>(-73.52%)</b></td><td>327.80 (-1.77%)</td><td>294.92 (+11.34%)</td><td>288.70 (+16.69%)</td><td>281.10 <b>(+33.54%)</b></td><td>19.29 <b>(-65.25%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>9.96 (n/a)</td><td>8.19 (n/a)</td><td>8.48 (n/a)</td><td>6.28 (n/a)</td><td>1.65 (n/a)</td><td>333.70 (n/a)</td><td>264.88 (n/a)</td><td>247.40 (n/a)</td><td>210.50 (n/a)</td><td>55.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>8.66 (-9.27%)</td><td>7.98 (+1.67%)</td><td>8.37 (+9.12%)</td><td>6.66 (-1.15%)</td><td>0.83 (-19.97%)</td><td>314.90 (+1.16%)</td><td>265.46 (-1.98%)</td><td>250.60 (-8.37%)</td><td>242.30 (+10.24%)</td><td>30.30 (-8.90%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>9.54 (n/a)</td><td>7.85 (n/a)</td><td>7.67 (n/a)</td><td>6.74 (n/a)</td><td>1.04 (n/a)</td><td>311.30 (n/a)</td><td>270.82 (n/a)</td><td>273.50 (n/a)</td><td>219.80 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>9.43 (-6.56%)</td><td>8.01 (-4.79%)</td><td>7.75 (-9.53%)</td><td>6.90 (-1.45%)</td><td>0.98 <b>(-25.65%)</b></td><td>303.70 (+1.47%)</td><td>264.78 (+4.17%)</td><td>270.60 (+10.49%)</td><td>222.30 (+7.03%)</td><td>31.27 <b>(-21.44%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>10.10 (n/a)</td><td>8.41 (n/a)</td><td>8.56 (n/a)</td><td>7.01 (n/a)</td><td>1.32 (n/a)</td><td>299.30 (n/a)</td><td>254.18 (n/a)</td><td>244.90 (n/a)</td><td>207.70 (n/a)</td><td>39.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>9.35 (+13.12%)</td><td>8.53 (+10.09%)</td><td>8.74 (+14.77%)</td><td>7.28 (-1.64%)</td><td>0.77 <b>(+106.58%)</b></td><td>287.90 (+1.66%)</td><td>247.70 (-8.69%)</td><td>240.00 (-12.85%)</td><td>224.20 (-11.59%)</td><td>24.06 <b>(+88.56%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.27 (n/a)</td><td>7.74 (n/a)</td><td>7.61 (n/a)</td><td>7.41 (n/a)</td><td>0.37 (n/a)</td><td>283.20 (n/a)</td><td>271.26 (n/a)</td><td>275.40 (n/a)</td><td>253.60 (n/a)</td><td>12.76 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>11.44 (+6.83%)</td><td>9.36 (+1.17%)</td><td>9.30 (-6.08%)</td><td>6.74 (-9.16%)</td><td>1.88 <b>(+26.98%)</b></td><td>310.90 (+10.09%)</td><td>232.26 (+0.20%)</td><td>225.50 (+6.47%)</td><td>183.30 (-6.38%)</td><td>50.97 <b>(+29.66%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>10.71 (n/a)</td><td>9.25 (n/a)</td><td>9.90 (n/a)</td><td>7.42 (n/a)</td><td>1.48 (n/a)</td><td>282.40 (n/a)</td><td>231.80 (n/a)</td><td>211.80 (n/a)</td><td>195.80 (n/a)</td><td>39.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>10.63 (-0.94%)</td><td>9.24 (+4.87%)</td><td>9.57 (+11.98%)</td><td>7.37 (-5.17%)</td><td>1.21 (+2.85%)</td><td>284.70 (+5.44%)</td><td>230.44 (-4.44%)</td><td>219.10 (-10.72%)</td><td>197.30 (+0.97%)</td><td>33.05 (+13.06%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>10.73 (n/a)</td><td>8.81 (n/a)</td><td>8.55 (n/a)</td><td>7.77 (n/a)</td><td>1.17 (n/a)</td><td>270.00 (n/a)</td><td>241.14 (n/a)</td><td>245.40 (n/a)</td><td>195.40 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>12.25 (+1.54%)</td><td>11.94 (+8.46%)</td><td>12.10 (+12.90%)</td><td>11.41 (+11.17%)</td><td>0.35 <b>(-53.60%)</b></td><td>367.60 (-10.06%)</td><td>351.64 (-8.06%)</td><td>346.60 (-11.42%)</td><td>342.50 (-1.50%)</td><td>10.36 <b>(-58.92%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>12.06 (n/a)</td><td>11.01 (n/a)</td><td>10.72 (n/a)</td><td>10.26 (n/a)</td><td>0.74 (n/a)</td><td>408.70 (n/a)</td><td>382.48 (n/a)</td><td>391.30 (n/a)</td><td>347.70 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.47 (+14.63%)</td><td>13.08 (+19.20%)</td><td>13.19 <b>(+22.55%)</b></td><td>12.38 (+17.99%)</td><td>0.41 <b>(-25.52%)</b></td><td>338.70 (-15.24%)</td><td>320.82 (-16.21%)</td><td>318.00 (-18.42%)</td><td>311.50 (-12.77%)</td><td>10.42 <b>(-44.69%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>11.75 (n/a)</td><td>10.98 (n/a)</td><td>10.76 (n/a)</td><td>10.50 (n/a)</td><td>0.55 (n/a)</td><td>399.60 (n/a)</td><td>382.90 (n/a)</td><td>389.80 (n/a)</td><td>357.10 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.62 (-1.51%)</td><td>12.15 (-1.19%)</td><td>12.41 (+1.44%)</td><td>10.49 (-1.11%)</td><td>1.14 (-9.89%)</td><td>399.80 (+1.11%)</td><td>347.84 (+1.06%)</td><td>337.90 (-1.43%)</td><td>308.00 (+1.52%)</td><td>33.82 (-6.45%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.83 (n/a)</td><td>12.29 (n/a)</td><td>12.24 (n/a)</td><td>10.61 (n/a)</td><td>1.27 (n/a)</td><td>395.40 (n/a)</td><td>344.20 (n/a)</td><td>342.80 (n/a)</td><td>303.40 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.14 (-8.96%)</td><td>13.62 (+0.14%)</td><td>14.06 (+4.89%)</td><td>12.79 (+12.52%)</td><td>0.67 <b>(-56.43%)</b></td><td>327.90 (-11.11%)</td><td>308.44 (-1.00%)</td><td>298.40 (-4.66%)</td><td>296.70 (+9.85%)</td><td>15.39 <b>(-58.04%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>15.53 (n/a)</td><td>13.61 (n/a)</td><td>13.40 (n/a)</td><td>11.37 (n/a)</td><td>1.53 (n/a)</td><td>368.90 (n/a)</td><td>311.56 (n/a)</td><td>313.00 (n/a)</td><td>270.10 (n/a)</td><td>36.69 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.14 (+2.54%)</td><td>13.38 (+6.22%)</td><td>13.63 (+6.88%)</td><td>12.19 (+3.42%)</td><td>0.74 (-12.29%)</td><td>344.10 (-3.29%)</td><td>314.18 (-5.95%)</td><td>307.60 (-6.45%)</td><td>296.60 (-2.50%)</td><td>18.18 (-17.35%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.79 (n/a)</td><td>12.60 (n/a)</td><td>12.76 (n/a)</td><td>11.79 (n/a)</td><td>0.84 (n/a)</td><td>355.80 (n/a)</td><td>334.04 (n/a)</td><td>328.80 (n/a)</td><td>304.20 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>15.45 (+14.84%)</td><td>14.13 (+9.41%)</td><td>14.37 (+8.03%)</td><td>12.51 (+11.76%)</td><td>1.18 <b>(+23.03%)</b></td><td>335.20 (-10.52%)</td><td>298.62 (-8.52%)</td><td>291.80 (-7.42%)</td><td>271.60 (-12.92%)</td><td>25.72 (-4.64%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.45 (n/a)</td><td>12.91 (n/a)</td><td>13.30 (n/a)</td><td>11.20 (n/a)</td><td>0.96 (n/a)</td><td>374.60 (n/a)</td><td>326.42 (n/a)</td><td>315.20 (n/a)</td><td>311.90 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.79 (+6.05%)</td><td>13.07 (+0.09%)</td><td>13.28 (+1.95%)</td><td>10.79 (-13.19%)</td><td>1.50 <b>(+160.46%)</b></td><td>388.60 (+15.17%)</td><td>324.50 (+0.89%)</td><td>315.90 (-1.89%)</td><td>283.60 (-5.72%)</td><td>39.89 <b>(+188.28%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>13.95 (n/a)</td><td>13.06 (n/a)</td><td>13.03 (n/a)</td><td>12.43 (n/a)</td><td>0.57 (n/a)</td><td>337.40 (n/a)</td><td>321.64 (n/a)</td><td>322.00 (n/a)</td><td>300.80 (n/a)</td><td>13.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.18 (-1.17%)</td><td>12.99 (-0.54%)</td><td>13.51 (+2.04%)</td><td>11.49 (-4.22%)</td><td>1.22 <b>(+31.55%)</b></td><td>365.10 (+4.40%)</td><td>325.16 (+0.88%)</td><td>310.40 (-1.99%)</td><td>295.80 (+1.20%)</td><td>31.42 <b>(+38.72%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>14.35 (n/a)</td><td>13.06 (n/a)</td><td>13.24 (n/a)</td><td>11.99 (n/a)</td><td>0.93 (n/a)</td><td>349.70 (n/a)</td><td>322.32 (n/a)</td><td>316.70 (n/a)</td><td>292.30 (n/a)</td><td>22.65 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.40 (-9.55%)</td><td>2.89 (+2.19%)</td><td>2.87 (+2.07%)</td><td>2.52 (+9.95%)</td><td>0.32 <b>(-45.07%)</b></td><td>207.60 (-9.07%)</td><td>183.12 (-4.24%)</td><td>182.50 (-2.04%)</td><td>154.10 (+10.62%)</td><td>19.29 <b>(-45.96%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.76 (n/a)</td><td>2.83 (n/a)</td><td>2.81 (n/a)</td><td>2.30 (n/a)</td><td>0.59 (n/a)</td><td>228.30 (n/a)</td><td>191.22 (n/a)</td><td>186.30 (n/a)</td><td>139.30 (n/a)</td><td>35.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.74 (+3.51%)</td><td>4.75 (+2.84%)</td><td>4.48 (-7.95%)</td><td>3.68 (+2.84%)</td><td>0.83 (+8.52%)</td><td>285.30 (-2.76%)</td><td>226.52 (-2.59%)</td><td>234.10 (+8.63%)</td><td>182.80 (-3.38%)</td><td>40.66 (-0.69%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>5.54 (n/a)</td><td>4.62 (n/a)</td><td>4.87 (n/a)</td><td>3.57 (n/a)</td><td>0.76 (n/a)</td><td>293.40 (n/a)</td><td>232.54 (n/a)</td><td>215.50 (n/a)</td><td>189.20 (n/a)</td><td>40.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.67 (-7.31%)</td><td>6.78 (-8.04%)</td><td>6.59 (-9.72%)</td><td>6.19 (-4.58%)</td><td>0.58 (-8.90%)</td><td>338.60 (+4.80%)</td><td>311.22 (+8.70%)</td><td>318.10 (+10.76%)</td><td>273.60 (+7.89%)</td><td>25.44 (+2.24%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>8.27 (n/a)</td><td>7.37 (n/a)</td><td>7.30 (n/a)</td><td>6.49 (n/a)</td><td>0.64 (n/a)</td><td>323.10 (n/a)</td><td>286.30 (n/a)</td><td>287.20 (n/a)</td><td>253.60 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.14 (-4.66%)</td><td>2.84 (-4.56%)</td><td>3.13 (+9.55%)</td><td>1.87 <b>(-30.20%)</b></td><td>0.55 <b>(+112.43%)</b></td><td>280.60 <b>(+43.24%)</b></td><td>192.22 (+8.49%)</td><td>167.30 (-8.73%)</td><td>166.90 (+4.90%)</td><td>49.70 <b>(+224.59%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>3.29 (n/a)</td><td>2.98 (n/a)</td><td>2.86 (n/a)</td><td>2.68 (n/a)</td><td>0.26 (n/a)</td><td>195.90 (n/a)</td><td>177.18 (n/a)</td><td>183.30 (n/a)</td><td>159.10 (n/a)</td><td>15.31 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (+9.92%)</td><td>0.19 (+2.17%)</td><td>0.19 (-9.76%)</td><td>0.15 <b>(+61.08%)</b></td><td>0.03 <b>(-38.94%)</b></td><td>213.60 <b>(-37.93%)</b></td><td>178.70 (-9.26%)</td><td>172.50 (+10.79%)</td><td>140.10 (-9.03%)</td><td>28.00 <b>(-66.16%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>344.10 (n/a)</td><td>196.94 (n/a)</td><td>155.70 (n/a)</td><td>154.00 (n/a)</td><td>82.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 <b>(-25.91%)</b></td><td>0.16 <b>(-26.50%)</b></td><td>0.16 <b>(-24.49%)</b></td><td>0.14 <b>(-25.68%)</b></td><td>0.02 <b>(-41.92%)</b></td><td>228.80 <b>(+34.59%)</b></td><td>201.38 <b>(+35.41%)</b></td><td>198.60 <b>(+32.40%)</b></td><td>174.60 <b>(+35.03%)</b></td><td>19.85 (+6.69%)</td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>170.00 (n/a)</td><td>148.72 (n/a)</td><td>150.00 (n/a)</td><td>129.30 (n/a)</td><td>18.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.49 (-12.90%)</td><td>0.37 (-8.43%)</td><td>0.36 (-6.34%)</td><td>0.20 <b>(-35.33%)</b></td><td>0.12 <b>(+27.73%)</b></td><td>330.10 <b>(+54.61%)</b></td><td>199.10 (+17.08%)</td><td>180.30 (+6.75%)</td><td>134.60 (+14.75%)</td><td>80.53 <b>(+125.96%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>213.50 (n/a)</td><td>170.06 (n/a)</td><td>168.90 (n/a)</td><td>117.30 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.39 <b>(-29.37%)</b></td><td>0.33 <b>(-25.80%)</b></td><td>0.31 <b>(-32.29%)</b></td><td>0.29 (-9.08%)</td><td>0.04 <b>(-63.97%)</b></td><td>226.00 (+9.98%)</td><td>201.48 <b>(+29.30%)</b></td><td>211.70 <b>(+47.63%)</b></td><td>168.40 <b>(+41.63%)</b></td><td>22.71 <b>(-43.77%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>205.50 (n/a)</td><td>155.82 (n/a)</td><td>143.40 (n/a)</td><td>118.90 (n/a)</td><td>40.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.53 (-1.67%)</td><td>0.41 (+9.55%)</td><td>0.35 (+3.95%)</td><td>0.33 (+16.28%)</td><td>0.09 (-11.38%)</td><td>196.50 (-14.00%)</td><td>165.12 (-10.32%)</td><td>185.80 (-3.83%)</td><td>123.90 (+1.64%)</td><td>34.54 <b>(-24.06%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.11 (n/a)</td><td>228.50 (n/a)</td><td>184.12 (n/a)</td><td>193.20 (n/a)</td><td>121.90 (n/a)</td><td>45.48 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.09 (+3.34%)</td><td>0.90 (+17.10%)</td><td>0.94 <b>(+31.23%)</b></td><td>0.69 (+18.83%)</td><td>0.17 (-8.43%)</td><td>188.90 (-15.86%)</td><td>150.24 (-15.62%)</td><td>139.50 <b>(-23.77%)</b></td><td>120.50 (-3.21%)</td><td>29.41 <b>(-23.78%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.05 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.58 (n/a)</td><td>0.18 (n/a)</td><td>224.50 (n/a)</td><td>178.06 (n/a)</td><td>183.00 (n/a)</td><td>124.50 (n/a)</td><td>38.59 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.90 (-16.36%)</td><td>0.75 (-4.16%)</td><td>0.77 (+4.22%)</td><td>0.42 <b>(-28.02%)</b></td><td>0.19 (-2.55%)</td><td>310.10 <b>(+38.93%)</b></td><td>189.60 (+7.48%)</td><td>169.60 (-4.02%)</td><td>144.90 (+19.55%)</td><td>68.29 <b>(+70.86%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>1.08 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.59 (n/a)</td><td>0.19 (n/a)</td><td>223.20 (n/a)</td><td>176.40 (n/a)</td><td>176.70 (n/a)</td><td>121.20 (n/a)</td><td>39.97 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.98 (+2.91%)</td><td>0.83 (-6.16%)</td><td>0.81 (-10.70%)</td><td>0.75 (-4.63%)</td><td>0.09 <b>(+35.55%)</b></td><td>175.80 (+4.83%)</td><td>158.84 (+6.96%)</td><td>161.50 (+11.92%)</td><td>133.50 (-2.84%)</td><td>15.81 <b>(+34.19%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.95 (n/a)</td><td>0.89 (n/a)</td><td>0.91 (n/a)</td><td>0.78 (n/a)</td><td>0.07 (n/a)</td><td>167.70 (n/a)</td><td>148.50 (n/a)</td><td>144.30 (n/a)</td><td>137.40 (n/a)</td><td>11.78 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.08 <b>(+38.76%)</b></td><td>0.81 <b>(+24.59%)</b></td><td>0.85 <b>(+36.97%)</b></td><td>0.57 (+4.75%)</td><td>0.22 <b>(+103.19%)</b></td><td>232.00 (-4.53%)</td><td>172.16 (-16.39%)</td><td>154.90 <b>(-26.97%)</b></td><td>121.80 <b>(-27.97%)</b></td><td>48.60 <b>(+45.74%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.62 (n/a)</td><td>0.54 (n/a)</td><td>0.11 (n/a)</td><td>243.00 (n/a)</td><td>205.92 (n/a)</td><td>212.10 (n/a)</td><td>169.10 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 <b>(-20.81%)</b></td><td>0.10 (-2.97%)</td><td>0.10 (+7.57%)</td><td>0.08 <b>(+41.90%)</b></td><td>0.01 <b>(-63.36%)</b></td><td>201.20 <b>(-29.53%)</b></td><td>167.72 (-4.93%)</td><td>157.30 (-7.03%)</td><td>151.00 <b>(+26.25%)</b></td><td>21.16 <b>(-67.84%)</b></td>
</tr>
<tr>
<td><code>9b92482</code> — 2026-08-28 20:07:47</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>285.50 (n/a)</td><td>176.42 (n/a)</td><td>169.20 (n/a)</td><td>119.60 (n/a)</td><td>65.80 (n/a)</td>
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
