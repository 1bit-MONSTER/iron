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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(-21.13%)</b></td><td>0.03 (-3.60%)</td><td>0.04 (+8.97%)</td><td>0.03 (+13.07%)</td><td>0.00 <b>(-53.49%)</b></td><td>206.00 (-11.55%)</td><td>180.28 (+0.54%)</td><td>169.90 (-8.21%)</td><td>158.30 <b>(+26.84%)</b></td><td>21.44 <b>(-46.01%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>179.32 (n/a)</td><td>185.10 (n/a)</td><td>124.80 (n/a)</td><td>39.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (-4.15%)</td><td>0.04 (+16.80%)</td><td>0.04 <b>(+23.87%)</b></td><td>0.04 (+19.16%)</td><td>0.01 <b>(-33.52%)</b></td><td>168.60 (-16.08%)</td><td>147.70 (-16.07%)</td><td>152.20 (-19.30%)</td><td>126.30 (+4.38%)</td><td>18.86 <b>(-40.36%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.90 (n/a)</td><td>175.98 (n/a)</td><td>188.60 (n/a)</td><td>121.00 (n/a)</td><td>31.62 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (+11.78%)</td><td>0.04 (-0.42%)</td><td>0.04 <b>(+25.16%)</b></td><td>0.02 <b>(-27.08%)</b></td><td>0.02 <b>(+48.76%)</b></td><td>377.80 <b>(+37.13%)</b></td><td>211.98 (+14.04%)</td><td>155.30 <b>(-20.07%)</b></td><td>112.00 (-10.54%)</td><td>112.95 <b>(+90.04%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>275.50 (n/a)</td><td>185.88 (n/a)</td><td>194.30 (n/a)</td><td>125.20 (n/a)</td><td>59.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (+2.00%)</td><td>0.04 (+3.52%)</td><td>0.04 (+16.22%)</td><td>0.03 (+1.68%)</td><td>0.01 <b>(-21.35%)</b></td><td>192.00 (-1.69%)</td><td>158.22 (-4.58%)</td><td>154.40 (-13.94%)</td><td>127.30 (-1.93%)</td><td>24.13 <b>(-23.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>165.82 (n/a)</td><td>179.40 (n/a)</td><td>129.80 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-9.30%)</td><td>0.04 (+4.12%)</td><td>0.04 (+10.71%)</td><td>0.03 <b>(+33.35%)</b></td><td>0.01 <b>(-33.20%)</b></td><td>242.60 <b>(-25.01%)</b></td><td>180.96 (-9.01%)</td><td>163.80 (-9.70%)</td><td>144.40 (+10.23%)</td><td>38.56 <b>(-47.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>323.50 (n/a)</td><td>198.88 (n/a)</td><td>181.40 (n/a)</td><td>131.00 (n/a)</td><td>72.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(-22.21%)</b></td><td>0.03 (+5.62%)</td><td>0.04 (+16.06%)</td><td>0.03 <b>(+27.30%)</b></td><td>0.00 <b>(-53.43%)</b></td><td>241.90 <b>(-21.46%)</b></td><td>188.78 (-10.26%)</td><td>174.80 (-13.85%)</td><td>173.50 <b>(+28.52%)</b></td><td>29.76 <b>(-52.73%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>308.00 (n/a)</td><td>210.36 (n/a)</td><td>202.90 (n/a)</td><td>135.00 (n/a)</td><td>62.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-9.04%)</td><td>0.03 (+19.05%)</td><td>0.04 (+10.03%)</td><td>0.03 <b>(+54.61%)</b></td><td>0.00 <b>(-69.62%)</b></td><td>208.00 <b>(-35.34%)</b></td><td>180.38 <b>(-22.70%)</b></td><td>174.20 (-9.13%)</td><td>168.30 (+9.93%)</td><td>16.06 <b>(-79.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>321.70 (n/a)</td><td>233.34 (n/a)</td><td>191.70 (n/a)</td><td>153.10 (n/a)</td><td>78.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (+0.03%)</td><td>0.03 (+7.11%)</td><td>0.03 (+18.27%)</td><td>0.03 (-3.56%)</td><td>0.01 (+8.35%)</td><td>235.60 (+3.70%)</td><td>184.96 (-6.13%)</td><td>187.50 (-15.43%)</td><td>141.50 (-0.07%)</td><td>41.50 (+6.65%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>197.04 (n/a)</td><td>221.70 (n/a)</td><td>141.60 (n/a)</td><td>38.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (-3.30%)</td><td>0.08 (+2.49%)</td><td>0.08 (+13.01%)</td><td>0.06 (+3.55%)</td><td>0.01 (-17.43%)</td><td>191.40 (-3.43%)</td><td>161.80 (-3.08%)</td><td>157.60 (-11.51%)</td><td>135.20 (+3.36%)</td><td>22.33 (-16.15%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>166.94 (n/a)</td><td>178.10 (n/a)</td><td>130.80 (n/a)</td><td>26.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (+11.49%)</td><td>0.08 (+18.41%)</td><td>0.08 <b>(+31.96%)</b></td><td>0.06 (+1.14%)</td><td>0.02 (+15.56%)</td><td>199.80 (-1.09%)</td><td>152.54 (-15.10%)</td><td>147.30 <b>(-24.23%)</b></td><td>116.80 (-10.29%)</td><td>30.88 (+5.58%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>179.68 (n/a)</td><td>194.40 (n/a)</td><td>130.20 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 <b>(+21.56%)</b></td><td>0.07 (+13.21%)</td><td>0.07 (+1.54%)</td><td>0.05 (+2.42%)</td><td>0.02 <b>(+37.56%)</b></td><td>232.90 (-2.35%)</td><td>170.82 (-10.50%)</td><td>168.30 (-1.52%)</td><td>131.80 (-17.73%)</td><td>39.84 (+10.78%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>190.86 (n/a)</td><td>170.90 (n/a)</td><td>160.20 (n/a)</td><td>35.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (+0.47%)</td><td>0.08 (+9.28%)</td><td>0.08 (+8.79%)</td><td>0.07 <b>(+24.63%)</b></td><td>0.01 <b>(-28.98%)</b></td><td>175.30 (-19.77%)</td><td>158.30 (-9.60%)</td><td>156.50 (-8.05%)</td><td>138.00 (-0.43%)</td><td>16.43 <b>(-42.58%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>175.12 (n/a)</td><td>170.20 (n/a)</td><td>138.60 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (+18.16%)</td><td>0.07 (+13.89%)</td><td>0.08 <b>(+26.50%)</b></td><td>0.06 (-5.10%)</td><td>0.02 <b>(+102.59%)</b></td><td>214.70 (+5.40%)</td><td>170.50 (-9.63%)</td><td>154.70 <b>(-20.95%)</b></td><td>130.10 (-15.35%)</td><td>38.13 <b>(+91.13%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>188.66 (n/a)</td><td>195.70 (n/a)</td><td>153.70 (n/a)</td><td>19.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 <b>(+25.17%)</b></td><td>0.07 (+12.82%)</td><td>0.07 (+3.32%)</td><td>0.05 <b>(+29.50%)</b></td><td>0.02 <b>(+21.32%)</b></td><td>245.40 <b>(-22.76%)</b></td><td>187.98 (-11.80%)</td><td>177.60 (-3.22%)</td><td>133.90 <b>(-20.11%)</b></td><td>45.90 <b>(-25.44%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>317.70 (n/a)</td><td>213.12 (n/a)</td><td>183.50 (n/a)</td><td>167.60 (n/a)</td><td>61.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (+15.41%)</td><td>0.07 <b>(+22.66%)</b></td><td>0.06 <b>(+21.53%)</b></td><td>0.06 <b>(+60.92%)</b></td><td>0.01 <b>(-33.06%)</b></td><td>198.80 <b>(-37.88%)</b></td><td>186.92 <b>(-21.12%)</b></td><td>194.50 (-17.69%)</td><td>151.20 (-13.35%)</td><td>20.18 <b>(-64.20%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>320.00 (n/a)</td><td>236.96 (n/a)</td><td>236.30 (n/a)</td><td>174.50 (n/a)</td><td>56.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 <b>(+26.25%)</b></td><td>0.07 <b>(+25.94%)</b></td><td>0.07 <b>(+32.09%)</b></td><td>0.06 <b>(+36.57%)</b></td><td>0.01 (+0.05%)</td><td>221.10 <b>(-26.76%)</b></td><td>187.60 <b>(-22.05%)</b></td><td>181.00 <b>(-24.30%)</b></td><td>141.70 <b>(-20.79%)</b></td><td>33.28 <b>(-41.01%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>301.90 (n/a)</td><td>240.66 (n/a)</td><td>239.10 (n/a)</td><td>178.90 (n/a)</td><td>56.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 <b>(+41.39%)</b></td><td>0.17 <b>(+35.44%)</b></td><td>0.16 (+12.03%)</td><td>0.12 <b>(+86.95%)</b></td><td>0.04 (+13.94%)</td><td>208.00 <b>(-46.52%)</b></td><td>153.78 <b>(-30.14%)</b></td><td>157.10 (-10.74%)</td><td>114.90 <b>(-29.29%)</b></td><td>38.15 <b>(-60.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>388.90 (n/a)</td><td>220.12 (n/a)</td><td>176.00 (n/a)</td><td>162.50 (n/a)</td><td>95.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.20 <b>(+48.39%)</b></td><td>0.16 (+19.95%)</td><td>0.16 (+18.39%)</td><td>0.12 (+2.44%)</td><td>0.03 <b>(+340.88%)</b></td><td>199.50 (-2.40%)</td><td>159.46 (-14.45%)</td><td>153.50 (-15.57%)</td><td>121.20 <b>(-32.59%)</b></td><td>29.58 <b>(+188.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>186.40 (n/a)</td><td>181.80 (n/a)</td><td>179.80 (n/a)</td><td>10.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 <b>(+24.99%)</b></td><td>0.17 <b>(+22.12%)</b></td><td>0.19 <b>(+34.55%)</b></td><td>0.12 (+1.24%)</td><td>0.03 <b>(+133.92%)</b></td><td>208.60 (-1.23%)</td><td>153.34 (-15.79%)</td><td>131.80 <b>(-25.70%)</b></td><td>126.70 (-19.96%)</td><td>35.03 <b>(+81.51%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>182.10 (n/a)</td><td>177.40 (n/a)</td><td>158.30 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (+11.65%)</td><td>0.15 (+7.81%)</td><td>0.15 (+13.06%)</td><td>0.11 (-11.59%)</td><td>0.02 <b>(+122.57%)</b></td><td>217.50 (+13.10%)</td><td>169.72 (-5.88%)</td><td>160.10 (-11.60%)</td><td>149.10 (-10.45%)</td><td>27.67 <b>(+128.93%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>180.32 (n/a)</td><td>181.10 (n/a)</td><td>166.50 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (+17.17%)</td><td>0.16 <b>(+23.97%)</b></td><td>0.17 <b>(+28.19%)</b></td><td>0.13 <b>(+34.09%)</b></td><td>0.02 (-6.44%)</td><td>188.30 <b>(-25.40%)</b></td><td>154.36 <b>(-20.16%)</b></td><td>142.90 <b>(-22.00%)</b></td><td>140.20 (-14.67%)</td><td>20.56 <b>(-41.63%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>252.40 (n/a)</td><td>193.34 (n/a)</td><td>183.20 (n/a)</td><td>164.30 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.20 <b>(+21.12%)</b></td><td>0.18 <b>(+26.82%)</b></td><td>0.18 <b>(+30.82%)</b></td><td>0.16 <b>(+22.47%)</b></td><td>0.02 (+11.36%)</td><td>152.10 (-18.36%)</td><td>136.68 <b>(-21.21%)</b></td><td>134.00 <b>(-23.56%)</b></td><td>122.40 (-17.41%)</td><td>11.41 <b>(-23.66%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>186.30 (n/a)</td><td>173.48 (n/a)</td><td>175.30 (n/a)</td><td>148.20 (n/a)</td><td>14.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 <b>(+37.71%)</b></td><td>0.17 <b>(+30.44%)</b></td><td>0.17 <b>(+31.45%)</b></td><td>0.15 (+19.23%)</td><td>0.02 <b>(+139.99%)</b></td><td>167.70 (-16.15%)</td><td>145.88 <b>(-22.84%)</b></td><td>144.10 <b>(-23.92%)</b></td><td>126.70 <b>(-27.39%)</b></td><td>15.66 <b>(+45.67%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>189.06 (n/a)</td><td>189.40 (n/a)</td><td>174.50 (n/a)</td><td>10.75 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 <b>(+26.36%)</b></td><td>0.16 <b>(+31.06%)</b></td><td>0.17 <b>(+40.74%)</b></td><td>0.13 <b>(+20.62%)</b></td><td>0.02 <b>(+50.76%)</b></td><td>190.70 (-17.09%)</td><td>152.68 <b>(-23.28%)</b></td><td>142.50 <b>(-28.96%)</b></td><td>132.70 <b>(-20.82%)</b></td><td>22.80 (+1.62%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>230.00 (n/a)</td><td>199.00 (n/a)</td><td>200.60 (n/a)</td><td>167.60 (n/a)</td><td>22.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.35 (-0.64%)</td><td>0.33 <b>(+35.76%)</b></td><td>0.33 <b>(+29.21%)</b></td><td>0.30 <b>(+140.54%)</b></td><td>0.02 <b>(-76.51%)</b></td><td>163.30 <b>(-58.42%)</b></td><td>150.08 <b>(-34.04%)</b></td><td>150.00 <b>(-22.64%)</b></td><td>141.10 (+0.64%)</td><td>8.86 <b>(-90.82%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>392.70 (n/a)</td><td>227.52 (n/a)</td><td>193.90 (n/a)</td><td>140.20 (n/a)</td><td>96.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.36 (+11.39%)</td><td>0.33 <b>(+21.70%)</b></td><td>0.32 <b>(+20.26%)</b></td><td>0.30 <b>(+33.64%)</b></td><td>0.02 <b>(-32.20%)</b></td><td>164.90 <b>(-25.18%)</b></td><td>150.26 (-18.66%)</td><td>153.70 (-16.87%)</td><td>138.40 (-10.19%)</td><td>11.32 <b>(-55.16%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>220.40 (n/a)</td><td>184.74 (n/a)</td><td>184.90 (n/a)</td><td>154.10 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.32 (-14.83%)</td><td>0.28 (-4.13%)</td><td>0.29 (+0.90%)</td><td>0.23 (+1.14%)</td><td>0.03 <b>(-41.30%)</b></td><td>209.20 (-1.13%)</td><td>175.50 (+2.88%)</td><td>171.60 (-0.87%)</td><td>154.30 (+17.34%)</td><td>20.32 <b>(-29.58%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>211.60 (n/a)</td><td>170.58 (n/a)</td><td>173.10 (n/a)</td><td>131.50 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.30 (-12.06%)</td><td>0.29 (+2.39%)</td><td>0.29 (+0.81%)</td><td>0.28 (+17.06%)</td><td>0.01 <b>(-75.84%)</b></td><td>176.90 (-14.58%)</td><td>168.96 (-3.75%)</td><td>169.80 (-0.82%)</td><td>162.50 (+13.72%)</td><td>5.64 <b>(-76.53%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>207.10 (n/a)</td><td>175.54 (n/a)</td><td>171.20 (n/a)</td><td>142.90 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.37 <b>(+37.62%)</b></td><td>0.33 <b>(+40.52%)</b></td><td>0.32 <b>(+29.88%)</b></td><td>0.27 <b>(+45.28%)</b></td><td>0.04 <b>(+27.19%)</b></td><td>180.80 <b>(-31.18%)</b></td><td>152.84 <b>(-29.12%)</b></td><td>153.50 <b>(-23.02%)</b></td><td>132.40 <b>(-27.33%)</b></td><td>20.79 <b>(-38.32%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>262.70 (n/a)</td><td>215.64 (n/a)</td><td>199.40 (n/a)</td><td>182.20 (n/a)</td><td>33.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.35 (-4.40%)</td><td>0.29 (-1.97%)</td><td>0.31 (+10.10%)</td><td>0.21 (-11.70%)</td><td>0.05 (-8.20%)</td><td>238.20 (+13.27%)</td><td>172.58 (+2.22%)</td><td>158.40 (-9.17%)</td><td>138.80 (+4.60%)</td><td>38.39 (+16.48%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>210.30 (n/a)</td><td>168.84 (n/a)</td><td>174.40 (n/a)</td><td>132.70 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.36 <b>(+20.18%)</b></td><td>0.30 (+16.70%)</td><td>0.30 (+19.99%)</td><td>0.25 (+8.84%)</td><td>0.05 <b>(+64.49%)</b></td><td>200.30 (-8.12%)</td><td>167.40 (-13.43%)</td><td>161.80 (-16.68%)</td><td>137.10 (-16.81%)</td><td>26.55 <b>(+27.19%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>218.00 (n/a)</td><td>193.38 (n/a)</td><td>194.20 (n/a)</td><td>164.80 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.34 (+6.52%)</td><td>0.30 (+13.19%)</td><td>0.31 <b>(+22.95%)</b></td><td>0.22 (+1.31%)</td><td>0.05 <b>(+21.14%)</b></td><td>220.10 (-1.30%)</td><td>169.24 (-11.08%)</td><td>159.00 (-18.67%)</td><td>143.80 (-6.07%)</td><td>31.63 (+11.92%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>223.00 (n/a)</td><td>190.32 (n/a)</td><td>195.50 (n/a)</td><td>153.10 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (-3.64%)</td><td>0.02 (+2.27%)</td><td>0.02 (-5.21%)</td><td>0.02 <b>(+26.72%)</b></td><td>0.00 <b>(-55.72%)</b></td><td>152.80 <b>(-21.07%)</b></td><td>141.10 (-4.61%)</td><td>141.00 (+5.46%)</td><td>126.90 (+3.76%)</td><td>10.91 <b>(-63.39%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>147.92 (n/a)</td><td>133.70 (n/a)</td><td>122.30 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (-7.31%)</td><td>0.02 (+7.33%)</td><td>0.02 (+11.37%)</td><td>0.02 <b>(+48.96%)</b></td><td>0.00 <b>(-64.74%)</b></td><td>155.70 <b>(-32.86%)</b></td><td>144.40 (-12.41%)</td><td>148.30 (-10.18%)</td><td>123.50 (+7.95%)</td><td>12.45 <b>(-74.22%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.90 (n/a)</td><td>164.86 (n/a)</td><td>165.10 (n/a)</td><td>114.40 (n/a)</td><td>48.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(+101.40%)</b></td><td>0.02 <b>(+41.04%)</b></td><td>0.02 <b>(+23.31%)</b></td><td>0.02 <b>(+45.24%)</b></td><td>0.01 <b>(+176.09%)</b></td><td>173.30 <b>(-31.15%)</b></td><td>140.50 <b>(-24.32%)</b></td><td>153.30 (-18.93%)</td><td>69.30 <b>(-50.36%)</b></td><td>40.77 (-9.70%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>251.70 (n/a)</td><td>185.64 (n/a)</td><td>189.10 (n/a)</td><td>139.60 (n/a)</td><td>45.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (-2.40%)</td><td>0.02 (+0.91%)</td><td>0.02 (-2.31%)</td><td>0.01 (+9.01%)</td><td>0.00 (-14.37%)</td><td>237.60 (-8.26%)</td><td>165.66 (-3.66%)</td><td>173.00 (+2.37%)</td><td>118.10 (+2.52%)</td><td>49.21 (-18.75%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>259.00 (n/a)</td><td>171.96 (n/a)</td><td>169.00 (n/a)</td><td>115.20 (n/a)</td><td>60.57 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (-8.95%)</td><td>0.02 (+3.28%)</td><td>0.02 (+5.48%)</td><td>0.01 (+9.61%)</td><td>0.00 <b>(-42.14%)</b></td><td>176.60 (-8.78%)</td><td>159.80 (-4.70%)</td><td>161.70 (-5.16%)</td><td>135.40 (+9.81%)</td><td>15.85 <b>(-40.51%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>167.68 (n/a)</td><td>170.50 (n/a)</td><td>123.30 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (+5.91%)</td><td>0.02 <b>(+21.98%)</b></td><td>0.02 <b>(+28.25%)</b></td><td>0.02 <b>(+33.11%)</b></td><td>0.00 <b>(-48.91%)</b></td><td>171.40 <b>(-24.86%)</b></td><td>157.70 (-19.60%)</td><td>160.20 <b>(-22.01%)</b></td><td>139.60 (-5.61%)</td><td>11.56 <b>(-63.85%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>228.10 (n/a)</td><td>196.14 (n/a)</td><td>205.40 (n/a)</td><td>147.90 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (-7.15%)</td><td>0.02 (-1.56%)</td><td>0.02 (-3.31%)</td><td>0.02 (+12.46%)</td><td>0.00 <b>(-45.17%)</b></td><td>160.90 (-11.06%)</td><td>155.02 (+0.70%)</td><td>158.50 (+3.39%)</td><td>137.40 (+7.68%)</td><td>9.95 <b>(-47.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>180.90 (n/a)</td><td>153.94 (n/a)</td><td>153.30 (n/a)</td><td>127.60 (n/a)</td><td>18.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (+1.39%)</td><td>0.01 (+4.08%)</td><td>0.01 (-3.60%)</td><td>0.01 (+4.62%)</td><td>0.00 <b>(-29.19%)</b></td><td>212.80 (-4.40%)</td><td>179.74 (-4.75%)</td><td>176.10 (+3.77%)</td><td>164.00 (-1.38%)</td><td>19.23 <b>(-31.87%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>222.60 (n/a)</td><td>188.70 (n/a)</td><td>169.70 (n/a)</td><td>166.30 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-8.50%)</td><td>0.04 (-2.10%)</td><td>0.04 <b>(+24.27%)</b></td><td>0.02 (-16.76%)</td><td>0.01 (+4.41%)</td><td>210.10 <b>(+20.13%)</b></td><td>153.40 (+3.38%)</td><td>130.10 (-19.54%)</td><td>125.90 (+9.29%)</td><td>37.68 <b>(+34.04%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>174.90 (n/a)</td><td>148.38 (n/a)</td><td>161.70 (n/a)</td><td>115.20 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (+15.27%)</td><td>0.03 (+17.55%)</td><td>0.04 <b>(+26.10%)</b></td><td>0.03 (+11.41%)</td><td>0.01 (+19.99%)</td><td>194.90 (-10.27%)</td><td>154.30 (-14.70%)</td><td>147.90 <b>(-20.65%)</b></td><td>129.10 (-13.30%)</td><td>27.19 (-5.50%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>180.90 (n/a)</td><td>186.40 (n/a)</td><td>148.90 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 <b>(+55.55%)</b></td><td>0.04 <b>(+36.79%)</b></td><td>0.04 <b>(+40.94%)</b></td><td>0.03 (+9.78%)</td><td>0.01 <b>(+347.27%)</b></td><td>183.20 (-8.95%)</td><td>139.90 <b>(-24.92%)</b></td><td>131.00 <b>(-29.04%)</b></td><td>111.60 <b>(-35.71%)</b></td><td>27.88 <b>(+164.78%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.20 (n/a)</td><td>186.34 (n/a)</td><td>184.60 (n/a)</td><td>173.60 (n/a)</td><td>10.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(+25.58%)</b></td><td>0.03 (+16.42%)</td><td>0.03 <b>(+21.10%)</b></td><td>0.02 (+1.86%)</td><td>0.01 <b>(+56.43%)</b></td><td>226.20 (-1.82%)</td><td>166.36 (-12.63%)</td><td>153.60 (-17.42%)</td><td>128.00 <b>(-20.35%)</b></td><td>36.84 <b>(+26.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.40 (n/a)</td><td>190.40 (n/a)</td><td>186.00 (n/a)</td><td>160.70 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-0.94%)</td><td>0.04 (+10.60%)</td><td>0.04 (+8.12%)</td><td>0.03 <b>(+21.45%)</b></td><td>0.00 <b>(-40.96%)</b></td><td>171.40 (-17.68%)</td><td>146.68 (-11.51%)</td><td>144.00 (-7.51%)</td><td>128.90 (+0.94%)</td><td>15.83 <b>(-51.04%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>165.76 (n/a)</td><td>155.70 (n/a)</td><td>127.70 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+2.58%)</td><td>0.03 (+7.02%)</td><td>0.03 (+6.98%)</td><td>0.03 (-0.24%)</td><td>0.00 (+16.15%)</td><td>205.60 (+0.24%)</td><td>173.94 (-6.35%)</td><td>169.60 (-6.50%)</td><td>159.10 (-2.51%)</td><td>18.96 (+13.20%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>185.74 (n/a)</td><td>181.40 (n/a)</td><td>163.20 (n/a)</td><td>16.75 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(+41.01%)</b></td><td>0.03 <b>(+32.27%)</b></td><td>0.03 <b>(+27.86%)</b></td><td>0.03 (+16.38%)</td><td>0.01 <b>(+101.92%)</b></td><td>206.00 (-14.06%)</td><td>164.48 <b>(-23.36%)</b></td><td>161.50 <b>(-21.75%)</b></td><td>132.90 <b>(-29.08%)</b></td><td>28.38 <b>(+20.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.70 (n/a)</td><td>214.62 (n/a)</td><td>206.40 (n/a)</td><td>187.40 (n/a)</td><td>23.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-0.56%)</td><td>0.03 (+9.11%)</td><td>0.03 (+9.85%)</td><td>0.02 (+3.50%)</td><td>0.00 (-3.53%)</td><td>238.50 (-3.36%)</td><td>199.52 (-8.47%)</td><td>201.90 (-8.97%)</td><td>175.90 (+0.51%)</td><td>25.59 (-5.56%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.80 (n/a)</td><td>217.98 (n/a)</td><td>221.80 (n/a)</td><td>175.00 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (+7.09%)</td><td>0.07 (+15.83%)</td><td>0.08 <b>(+42.31%)</b></td><td>0.05 (-0.16%)</td><td>0.02 (+5.27%)</td><td>224.90 (+0.18%)</td><td>155.38 (-13.37%)</td><td>137.20 <b>(-29.71%)</b></td><td>116.00 (-6.60%)</td><td>42.22 (+2.79%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>224.50 (n/a)</td><td>179.36 (n/a)</td><td>195.20 (n/a)</td><td>124.20 (n/a)</td><td>41.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (+8.53%)</td><td>0.07 (+18.02%)</td><td>0.08 <b>(+26.80%)</b></td><td>0.06 <b>(+20.85%)</b></td><td>0.01 (-3.05%)</td><td>168.70 (-17.26%)</td><td>144.66 (-15.63%)</td><td>136.40 <b>(-21.16%)</b></td><td>127.40 (-7.88%)</td><td>17.77 <b>(-24.93%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>171.46 (n/a)</td><td>173.00 (n/a)</td><td>138.30 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 <b>(+33.92%)</b></td><td>0.06 (+13.26%)</td><td>0.06 (+10.45%)</td><td>0.03 (-14.93%)</td><td>0.02 <b>(+91.56%)</b></td><td>340.70 (+17.52%)</td><td>190.88 (-3.94%)</td><td>165.10 (-9.48%)</td><td>122.60 <b>(-25.33%)</b></td><td>87.58 <b>(+68.98%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>289.90 (n/a)</td><td>198.70 (n/a)</td><td>182.40 (n/a)</td><td>164.20 (n/a)</td><td>51.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (+2.62%)</td><td>0.06 (+0.08%)</td><td>0.06 (+2.18%)</td><td>0.05 (-10.69%)</td><td>0.01 <b>(+32.30%)</b></td><td>221.40 (+11.99%)</td><td>173.14 (+1.29%)</td><td>174.00 (-2.14%)</td><td>134.20 (-2.54%)</td><td>32.78 <b>(+47.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>170.94 (n/a)</td><td>177.80 (n/a)</td><td>137.70 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 <b>(+24.43%)</b></td><td>0.06 (-5.56%)</td><td>0.06 (-5.13%)</td><td>0.03 <b>(-51.47%)</b></td><td>0.02 <b>(+358.35%)</b></td><td>384.90 <b>(+106.05%)</b></td><td>208.10 <b>(+20.78%)</b></td><td>177.40 (+5.41%)</td><td>126.50 (-19.63%)</td><td>101.18 <b>(+726.81%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>186.80 (n/a)</td><td>172.30 (n/a)</td><td>168.30 (n/a)</td><td>157.40 (n/a)</td><td>12.24 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 <b>(-33.10%)</b></td><td>0.06 (-9.66%)</td><td>0.06 (-3.81%)</td><td>0.05 (+6.69%)</td><td>0.01 <b>(-70.23%)</b></td><td>195.90 (-6.27%)</td><td>176.02 (+5.16%)</td><td>179.70 (+3.93%)</td><td>158.40 <b>(+49.43%)</b></td><td>16.99 <b>(-58.57%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>167.38 (n/a)</td><td>172.90 (n/a)</td><td>106.00 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (+14.16%)</td><td>0.06 (+1.90%)</td><td>0.06 (-9.50%)</td><td>0.05 (-3.03%)</td><td>0.01 <b>(+80.92%)</b></td><td>208.70 (+3.11%)</td><td>171.36 (-0.30%)</td><td>179.10 (+10.49%)</td><td>137.50 (-12.42%)</td><td>29.48 <b>(+59.06%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>171.88 (n/a)</td><td>162.10 (n/a)</td><td>157.00 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (+3.33%)</td><td>0.05 (-1.50%)</td><td>0.06 (+15.15%)</td><td>0.03 <b>(-26.13%)</b></td><td>0.01 <b>(+141.95%)</b></td><td>308.00 <b>(+35.38%)</b></td><td>225.16 (+7.96%)</td><td>185.90 (-13.17%)</td><td>167.80 (-3.23%)</td><td>69.14 <b>(+223.20%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>208.56 (n/a)</td><td>214.10 (n/a)</td><td>173.40 (n/a)</td><td>21.39 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 <b>(+46.77%)</b></td><td>0.15 <b>(+51.17%)</b></td><td>0.16 <b>(+47.33%)</b></td><td>0.13 <b>(+48.26%)</b></td><td>0.01 (+15.97%)</td><td>161.30 <b>(-32.57%)</b></td><td>137.42 <b>(-34.19%)</b></td><td>131.00 <b>(-32.12%)</b></td><td>126.10 <b>(-31.87%)</b></td><td>14.34 <b>(-47.06%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>208.80 (n/a)</td><td>193.00 (n/a)</td><td>185.10 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (+1.99%)</td><td>0.16 <b>(+22.87%)</b></td><td>0.17 <b>(+22.51%)</b></td><td>0.14 <b>(+56.12%)</b></td><td>0.01 <b>(-53.24%)</b></td><td>151.50 <b>(-35.94%)</b></td><td>130.20 <b>(-21.69%)</b></td><td>125.50 (-18.40%)</td><td>121.00 (-2.02%)</td><td>12.15 <b>(-71.18%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>236.50 (n/a)</td><td>166.26 (n/a)</td><td>153.80 (n/a)</td><td>123.50 (n/a)</td><td>42.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (-1.87%)</td><td>0.16 <b>(+26.09%)</b></td><td>0.16 <b>(+36.76%)</b></td><td>0.14 <b>(+31.79%)</b></td><td>0.01 <b>(-51.16%)</b></td><td>153.90 <b>(-24.11%)</b></td><td>136.24 <b>(-23.13%)</b></td><td>134.80 <b>(-26.90%)</b></td><td>121.40 (+1.93%)</td><td>13.18 <b>(-61.53%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>202.80 (n/a)</td><td>177.24 (n/a)</td><td>184.40 (n/a)</td><td>119.10 (n/a)</td><td>34.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 <b>(+20.51%)</b></td><td>0.14 (+12.60%)</td><td>0.14 (+7.67%)</td><td>0.10 (-0.08%)</td><td>0.03 <b>(+52.15%)</b></td><td>211.80 (+0.09%)</td><td>155.88 (-9.11%)</td><td>151.20 (-7.13%)</td><td>111.40 (-16.99%)</td><td>39.22 <b>(+24.76%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.60 (n/a)</td><td>171.50 (n/a)</td><td>162.80 (n/a)</td><td>134.20 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 <b>(+20.38%)</b></td><td>0.15 <b>(+26.67%)</b></td><td>0.16 <b>(+37.04%)</b></td><td>0.12 (+15.09%)</td><td>0.02 <b>(+38.21%)</b></td><td>168.90 (-13.12%)</td><td>141.06 <b>(-20.80%)</b></td><td>134.60 <b>(-27.01%)</b></td><td>125.90 (-16.90%)</td><td>17.51 (+0.21%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>178.10 (n/a)</td><td>184.40 (n/a)</td><td>151.50 (n/a)</td><td>17.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (+1.36%)</td><td>0.12 (+15.59%)</td><td>0.13 <b>(+21.65%)</b></td><td>0.11 (+14.83%)</td><td>0.01 <b>(-26.64%)</b></td><td>195.60 (-12.91%)</td><td>169.72 (-14.00%)</td><td>166.00 (-17.78%)</td><td>159.60 (-1.36%)</td><td>14.80 <b>(-34.77%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>224.60 (n/a)</td><td>197.34 (n/a)</td><td>201.90 (n/a)</td><td>161.80 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (+15.00%)</td><td>0.13 (+9.58%)</td><td>0.12 (+13.94%)</td><td>0.12 (+11.67%)</td><td>0.02 (+2.94%)</td><td>176.90 (-10.48%)</td><td>161.28 (-9.03%)</td><td>169.20 (-12.24%)</td><td>129.40 (-13.04%)</td><td>19.01 <b>(-21.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>197.60 (n/a)</td><td>177.28 (n/a)</td><td>192.80 (n/a)</td><td>148.80 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (-2.07%)</td><td>0.11 (+17.15%)</td><td>0.11 (+18.27%)</td><td>0.08 <b>(+38.37%)</b></td><td>0.01 <b>(-33.95%)</b></td><td>259.20 <b>(-27.72%)</b></td><td>200.64 (-17.83%)</td><td>185.90 (-15.46%)</td><td>179.70 (+2.10%)</td><td>33.45 <b>(-52.22%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>358.60 (n/a)</td><td>244.18 (n/a)</td><td>219.90 (n/a)</td><td>176.00 (n/a)</td><td>70.00 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>172.20 (n/a)</td><td>156.42 (n/a)</td><td>156.10 (n/a)</td><td>135.60 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.20 (n/a)</td><td>157.62 (n/a)</td><td>149.00 (n/a)</td><td>142.50 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>171.84 (n/a)</td><td>157.40 (n/a)</td><td>130.80 (n/a)</td><td>50.59 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>296.20 (n/a)</td><td>190.76 (n/a)</td><td>167.30 (n/a)</td><td>124.00 (n/a)</td><td>68.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>183.30 (n/a)</td><td>146.54 (n/a)</td><td>143.80 (n/a)</td><td>118.10 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.70 (n/a)</td><td>139.78 (n/a)</td><td>142.50 (n/a)</td><td>115.80 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.30 (n/a)</td><td>136.28 (n/a)</td><td>130.20 (n/a)</td><td>120.10 (n/a)</td><td>20.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>173.78 (n/a)</td><td>166.70 (n/a)</td><td>152.10 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.40 (n/a)</td><td>157.00 (n/a)</td><td>158.80 (n/a)</td><td>121.70 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>197.70 (n/a)</td><td>172.40 (n/a)</td><td>181.10 (n/a)</td><td>146.10 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>179.80 (n/a)</td><td>160.70 (n/a)</td><td>175.70 (n/a)</td><td>134.20 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>213.20 (n/a)</td><td>174.88 (n/a)</td><td>187.40 (n/a)</td><td>113.80 (n/a)</td><td>39.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.34 (-15.25%)</td><td>0.28 (-18.34%)</td><td>0.30 <b>(-23.68%)</b></td><td>0.21 (-19.45%)</td><td>0.06 <b>(-21.83%)</b></td><td>230.30 <b>(+24.15%)</b></td><td>179.90 <b>(+21.98%)</b></td><td>164.00 <b>(+30.99%)</b></td><td>144.00 (+17.94%)</td><td>37.47 (+15.18%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>185.50 (n/a)</td><td>147.48 (n/a)</td><td>125.20 (n/a)</td><td>122.10 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>192.00 (n/a)</td><td>165.04 (n/a)</td><td>161.40 (n/a)</td><td>143.40 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>229.00 (n/a)</td><td>188.64 (n/a)</td><td>207.40 (n/a)</td><td>128.30 (n/a)</td><td>46.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>197.88 (n/a)</td><td>193.00 (n/a)</td><td>185.50 (n/a)</td><td>10.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>166.82 (n/a)</td><td>153.50 (n/a)</td><td>137.20 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>314.00 (n/a)</td><td>218.72 (n/a)</td><td>187.60 (n/a)</td><td>167.50 (n/a)</td><td>62.55 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>173.62 (n/a)</td><td>182.20 (n/a)</td><td>146.60 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>313.20 (n/a)</td><td>226.56 (n/a)</td><td>203.10 (n/a)</td><td>174.00 (n/a)</td><td>55.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>236.40 (n/a)</td><td>165.38 (n/a)</td><td>144.40 (n/a)</td><td>131.20 (n/a)</td><td>43.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>250.90 (n/a)</td><td>186.84 (n/a)</td><td>182.10 (n/a)</td><td>142.10 (n/a)</td><td>39.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>178.04 (n/a)</td><td>187.00 (n/a)</td><td>139.30 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>218.10 (n/a)</td><td>201.20 (n/a)</td><td>199.70 (n/a)</td><td>187.70 (n/a)</td><td>11.62 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.30 (n/a)</td><td>176.04 (n/a)</td><td>167.50 (n/a)</td><td>131.70 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.00 (n/a)</td><td>169.14 (n/a)</td><td>178.10 (n/a)</td><td>128.10 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>178.80 (n/a)</td><td>154.02 (n/a)</td><td>143.80 (n/a)</td><td>130.60 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>317.10 (n/a)</td><td>226.92 (n/a)</td><td>210.80 (n/a)</td><td>190.90 (n/a)</td><td>51.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>179.36 (n/a)</td><td>179.30 (n/a)</td><td>167.40 (n/a)</td><td>11.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>230.00 (n/a)</td><td>185.30 (n/a)</td><td>183.70 (n/a)</td><td>148.40 (n/a)</td><td>32.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>239.10 (n/a)</td><td>202.36 (n/a)</td><td>205.70 (n/a)</td><td>169.90 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.10 (n/a)</td><td>148.48 (n/a)</td><td>138.50 (n/a)</td><td>123.50 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>157.00 (n/a)</td><td>137.78 (n/a)</td><td>137.20 (n/a)</td><td>115.30 (n/a)</td><td>18.98 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>157.22 (n/a)</td><td>166.00 (n/a)</td><td>112.40 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>161.40 (n/a)</td><td>154.70 (n/a)</td><td>140.90 (n/a)</td><td>20.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>162.04 (n/a)</td><td>163.80 (n/a)</td><td>116.90 (n/a)</td><td>27.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.40 (n/a)</td><td>176.28 (n/a)</td><td>158.70 (n/a)</td><td>143.70 (n/a)</td><td>38.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.80 (n/a)</td><td>180.46 (n/a)</td><td>177.90 (n/a)</td><td>139.20 (n/a)</td><td>40.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.10 (n/a)</td><td>187.90 (n/a)</td><td>177.70 (n/a)</td><td>154.10 (n/a)</td><td>37.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.70 (n/a)</td><td>143.32 (n/a)</td><td>137.60 (n/a)</td><td>118.90 (n/a)</td><td>20.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>154.26 (n/a)</td><td>144.10 (n/a)</td><td>122.50 (n/a)</td><td>32.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>358.50 (n/a)</td><td>191.04 (n/a)</td><td>168.90 (n/a)</td><td>123.50 (n/a)</td><td>96.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>157.78 (n/a)</td><td>165.40 (n/a)</td><td>121.90 (n/a)</td><td>33.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>307.90 (n/a)</td><td>176.48 (n/a)</td><td>132.10 (n/a)</td><td>121.50 (n/a)</td><td>79.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>175.38 (n/a)</td><td>181.00 (n/a)</td><td>127.20 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.70 (n/a)</td><td>188.36 (n/a)</td><td>188.00 (n/a)</td><td>147.70 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.30 (n/a)</td><td>200.16 (n/a)</td><td>207.00 (n/a)</td><td>154.00 (n/a)</td><td>32.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>178.04 (n/a)</td><td>180.70 (n/a)</td><td>157.20 (n/a)</td><td>12.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>173.30 (n/a)</td><td>175.30 (n/a)</td><td>156.40 (n/a)</td><td>10.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.40 (n/a)</td><td>174.42 (n/a)</td><td>178.70 (n/a)</td><td>134.70 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>193.26 (n/a)</td><td>199.60 (n/a)</td><td>162.90 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.70 (n/a)</td><td>168.76 (n/a)</td><td>177.00 (n/a)</td><td>122.80 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.00 (n/a)</td><td>189.68 (n/a)</td><td>186.00 (n/a)</td><td>157.00 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>190.84 (n/a)</td><td>183.30 (n/a)</td><td>169.90 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>333.80 (n/a)</td><td>223.56 (n/a)</td><td>200.50 (n/a)</td><td>182.80 (n/a)</td><td>62.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>185.90 (n/a)</td><td>161.44 (n/a)</td><td>180.40 (n/a)</td><td>126.60 (n/a)</td><td>29.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>240.50 (n/a)</td><td>172.26 (n/a)</td><td>172.00 (n/a)</td><td>120.90 (n/a)</td><td>49.14 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.10 (n/a)</td><td>153.56 (n/a)</td><td>142.70 (n/a)</td><td>125.00 (n/a)</td><td>26.31 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>223.00 (n/a)</td><td>164.38 (n/a)</td><td>159.60 (n/a)</td><td>115.50 (n/a)</td><td>46.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>218.20 (n/a)</td><td>165.02 (n/a)</td><td>160.00 (n/a)</td><td>113.10 (n/a)</td><td>39.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>246.70 (n/a)</td><td>199.46 (n/a)</td><td>222.40 (n/a)</td><td>137.90 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>259.30 (n/a)</td><td>211.36 (n/a)</td><td>201.10 (n/a)</td><td>181.10 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>4.39 (-13.90%)</td><td>3.80 (-11.11%)</td><td>3.52 (-16.69%)</td><td>3.41 (-4.31%)</td><td>0.47 (-13.50%)</td><td>2759.50 (+4.50%)</td><td>2503.62 (+12.38%)</td><td>2668.00 <b>(+20.04%)</b></td><td>2142.40 (+16.14%)</td><td>299.14 (+5.46%)</td><td>1726.77 (-13.90%)</td><td>1495.47 (-11.11%)</td><td>1386.60 (-16.69%)</td><td>1340.59 (-4.31%)</td><td>186.82 (-13.50%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>5.10 (n/a)</td><td>4.28 (n/a)</td><td>4.23 (n/a)</td><td>3.56 (n/a)</td><td>0.55 (n/a)</td><td>2640.60 (n/a)</td><td>2227.74 (n/a)</td><td>2222.60 (n/a)</td><td>1844.60 (n/a)</td><td>283.65 (n/a)</td><td>2005.49 (n/a)</td><td>1682.39 (n/a)</td><td>1664.41 (n/a)</td><td>1400.98 (n/a)</td><td>215.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.46 <b>(+49.35%)</b></td><td>1.03 <b>(+27.95%)</b></td><td>1.02 (+18.55%)</td><td>0.66 (+17.76%)</td><td>0.29 <b>(+57.88%)</b></td><td>333.30 (-15.08%)</td><td>229.90 <b>(-20.46%)</b></td><td>216.60 (-15.62%)</td><td>151.70 <b>(-33.05%)</b></td><td>65.96 (-8.51%)</td><td>62.21 <b>(+49.35%)</b></td><td>43.74 <b>(+27.95%)</b></td><td>43.58 (+18.55%)</td><td>28.32 (+17.76%)</td><td>12.20 <b>(+57.88%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.98 (n/a)</td><td>0.80 (n/a)</td><td>0.86 (n/a)</td><td>0.56 (n/a)</td><td>0.18 (n/a)</td><td>392.50 (n/a)</td><td>289.04 (n/a)</td><td>256.70 (n/a)</td><td>226.60 (n/a)</td><td>72.09 (n/a)</td><td>41.65 (n/a)</td><td>34.18 (n/a)</td><td>36.76 (n/a)</td><td>24.05 (n/a)</td><td>7.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.19 (-14.79%)</td><td>0.82 <b>(-29.55%)</b></td><td>0.75 <b>(-31.40%)</b></td><td>0.63 <b>(-33.73%)</b></td><td>0.23 <b>(+30.08%)</b></td><td>350.90 <b>(+50.92%)</b></td><td>285.88 <b>(+47.48%)</b></td><td>296.70 <b>(+45.73%)</b></td><td>185.60 (+17.32%)</td><td>70.68 <b>(+138.62%)</b></td><td>50.84 (-14.79%)</td><td>34.96 <b>(-29.55%)</b></td><td>31.80 <b>(-31.40%)</b></td><td>26.89 <b>(-33.73%)</b></td><td>10.01 <b>(+30.08%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>1.40 (n/a)</td><td>1.16 (n/a)</td><td>1.09 (n/a)</td><td>0.95 (n/a)</td><td>0.18 (n/a)</td><td>232.50 (n/a)</td><td>193.84 (n/a)</td><td>203.60 (n/a)</td><td>158.20 (n/a)</td><td>29.62 (n/a)</td><td>59.66 (n/a)</td><td>49.62 (n/a)</td><td>46.36 (n/a)</td><td>40.58 (n/a)</td><td>7.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.52 (+0.33%)</td><td>0.52 (+0.46%)</td><td>0.52 (+0.44%)</td><td>0.52 (+0.69%)</td><td>0.00 <b>(-62.35%)</b></td><td>48718.50 (-0.68%)</td><td>48647.00 (-0.46%)</td><td>48634.80 (-0.43%)</td><td>48607.30 (-0.33%)</td><td>43.67 <b>(-62.73%)</b></td><td>353.44 (+0.33%)</td><td>353.15 (+0.46%)</td><td>353.24 (+0.44%)</td><td>352.64 (+0.69%)</td><td>0.32 <b>(-62.35%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>49053.60 (n/a)</td><td>48871.12 (n/a)</td><td>48847.10 (n/a)</td><td>48766.30 (n/a)</td><td>117.16 (n/a)</td><td>352.29 (n/a)</td><td>351.54 (n/a)</td><td>351.71 (n/a)</td><td>350.23 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (-1.52%)</td><td>0.21 (+0.01%)</td><td>0.21 (+0.57%)</td><td>0.21 (+1.31%)</td><td>0.00 <b>(-87.19%)</b></td><td>118926.80 (-1.29%)</td><td>118651.76 (-0.02%)</td><td>118580.60 (-0.56%)</td><td>118403.70 (+1.54%)</td><td>209.01 <b>(-87.14%)</b></td><td>145.10 (-1.52%)</td><td>144.79 (+0.01%)</td><td>144.88 (+0.57%)</td><td>144.46 (+1.31%)</td><td>0.25 <b>(-87.19%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120479.40 (n/a)</td><td>118677.06 (n/a)</td><td>119254.20 (n/a)</td><td>116605.40 (n/a)</td><td>1625.58 (n/a)</td><td>147.33 (n/a)</td><td>144.78 (n/a)</td><td>144.06 (n/a)</td><td>142.60 (n/a)</td><td>1.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.88 (-1.26%)</td><td>0.88 (-0.05%)</td><td>0.88 (-0.08%)</td><td>0.88 (+1.60%)</td><td>0.00 <b>(-87.66%)</b></td><td>28722.60 (-1.57%)</td><td>28643.48 (+0.03%)</td><td>28618.10 (+0.08%)</td><td>28613.10 (+1.28%)</td><td>46.06 <b>(-87.69%)</b></td><td>600.42 (-1.26%)</td><td>599.78 (-0.05%)</td><td>600.32 (-0.08%)</td><td>598.13 (+1.60%)</td><td>0.96 <b>(-87.66%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.86 (n/a)</td><td>0.01 (n/a)</td><td>29181.20 (n/a)</td><td>28634.28 (n/a)</td><td>28595.90 (n/a)</td><td>28251.30 (n/a)</td><td>374.27 (n/a)</td><td>608.11 (n/a)</td><td>600.06 (n/a)</td><td>600.78 (n/a)</td><td>588.73 (n/a)</td><td>7.80 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.59 (+6.71%)</td><td>3.45 (+4.06%)</td><td>3.52 (+5.91%)</td><td>3.29 (+0.72%)</td><td>0.13 <b>(+268.63%)</b></td><td>7655.10 (-0.71%)</td><td>7296.44 (-3.80%)</td><td>7144.50 (-5.58%)</td><td>7014.70 (-6.29%)</td><td>279.77 <b>(+243.41%)</b></td><td>2449.11 (+6.71%)</td><td>2357.29 (+4.06%)</td><td>2404.64 (+5.91%)</td><td>2244.24 (+0.72%)</td><td>89.27 <b>(+268.63%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>3.36 (n/a)</td><td>3.32 (n/a)</td><td>3.33 (n/a)</td><td>3.26 (n/a)</td><td>0.04 (n/a)</td><td>7710.20 (n/a)</td><td>7584.74 (n/a)</td><td>7566.50 (n/a)</td><td>7485.60 (n/a)</td><td>81.47 (n/a)</td><td>2295.06 (n/a)</td><td>2265.27 (n/a)</td><td>2270.52 (n/a)</td><td>2228.20 (n/a)</td><td>24.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.16 (+5.62%)</td><td>2.87 (+1.05%)</td><td>2.81 (+0.03%)</td><td>2.76 (+0.84%)</td><td>0.17 <b>(+75.88%)</b></td><td>9113.60 (-0.84%)</td><td>8796.00 (-0.88%)</td><td>8947.10 (-0.03%)</td><td>7960.60 (-5.33%)</td><td>472.49 <b>(+64.78%)</b></td><td>2158.10 (+5.62%)</td><td>1957.99 (+1.05%)</td><td>1920.15 (+0.03%)</td><td>1885.07 (+0.84%)</td><td>112.89 <b>(+75.88%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>2.99 (n/a)</td><td>2.84 (n/a)</td><td>2.81 (n/a)</td><td>2.74 (n/a)</td><td>0.09 (n/a)</td><td>9190.60 (n/a)</td><td>8874.26 (n/a)</td><td>8949.40 (n/a)</td><td>8408.40 (n/a)</td><td>286.73 (n/a)</td><td>2043.17 (n/a)</td><td>1937.58 (n/a)</td><td>1919.67 (n/a)</td><td>1869.29 (n/a)</td><td>64.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.29 (-1.50%)</td><td>3.21 (-0.78%)</td><td>3.19 (-1.79%)</td><td>3.15 (+1.10%)</td><td>0.06 <b>(-36.12%)</b></td><td>7982.50 (-1.09%)</td><td>7831.52 (+0.75%)</td><td>7885.90 (+1.82%)</td><td>7657.70 (+1.53%)</td><td>142.14 <b>(-35.86%)</b></td><td>2243.48 (-1.50%)</td><td>2194.27 (-0.78%)</td><td>2178.57 (-1.79%)</td><td>2152.18 (+1.10%)</td><td>40.01 <b>(-36.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>3.34 (n/a)</td><td>3.24 (n/a)</td><td>3.25 (n/a)</td><td>3.12 (n/a)</td><td>0.09 (n/a)</td><td>8070.60 (n/a)</td><td>7773.30 (n/a)</td><td>7744.90 (n/a)</td><td>7542.50 (n/a)</td><td>221.60 (n/a)</td><td>2277.73 (n/a)</td><td>2211.54 (n/a)</td><td>2218.21 (n/a)</td><td>2128.69 (n/a)</td><td>62.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.78 (+0.35%)</td><td>0.78 (+0.29%)</td><td>0.78 (+0.34%)</td><td>0.78 (+0.25%)</td><td>0.00 <b>(+70.41%)</b></td><td>96670.00 (-0.25%)</td><td>96521.52 (-0.29%)</td><td>96460.70 (-0.34%)</td><td>96420.50 (-0.35%)</td><td>107.88 <b>(+69.30%)</b></td><td>712.71 (+0.35%)</td><td>711.96 (+0.29%)</td><td>712.41 (+0.34%)</td><td>710.87 (+0.25%)</td><td>0.80 <b>(+70.41%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96912.60 (n/a)</td><td>96801.62 (n/a)</td><td>96785.30 (n/a)</td><td>96755.70 (n/a)</td><td>63.72 (n/a)</td><td>710.24 (n/a)</td><td>709.90 (n/a)</td><td>710.02 (n/a)</td><td>709.09 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.73 (-0.54%)</td><td>0.73 (-0.57%)</td><td>0.73 (-0.56%)</td><td>0.73 (-0.65%)</td><td>0.00 <b>(+68.74%)</b></td><td>103861.90 (+0.66%)</td><td>103691.16 (+0.58%)</td><td>103671.00 (+0.56%)</td><td>103593.70 (+0.54%)</td><td>100.81 <b>(+70.76%)</b></td><td>663.36 (-0.54%)</td><td>662.73 (-0.57%)</td><td>662.86 (-0.56%)</td><td>661.64 (-0.65%)</td><td>0.64 <b>(+68.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103183.90 (n/a)</td><td>103096.22 (n/a)</td><td>103093.70 (n/a)</td><td>103035.40 (n/a)</td><td>59.04 (n/a)</td><td>666.95 (n/a)</td><td>666.56 (n/a)</td><td>666.57 (n/a)</td><td>665.99 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.69 (+0.12%)</td><td>0.69 (+0.04%)</td><td>0.69 (+0.05%)</td><td>0.69 (+0.02%)</td><td>0.00 (+2.54%)</td><td>109897.00 (-0.02%)</td><td>109545.68 (-0.04%)</td><td>109578.70 (-0.05%)</td><td>109184.40 (-0.12%)</td><td>255.81 (+2.42%)</td><td>629.39 (+0.12%)</td><td>627.32 (+0.04%)</td><td>627.12 (+0.05%)</td><td>625.31 (+0.02%)</td><td>1.47 (+2.54%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109918.60 (n/a)</td><td>109585.58 (n/a)</td><td>109636.60 (n/a)</td><td>109317.80 (n/a)</td><td>249.77 (n/a)</td><td>628.62 (n/a)</td><td>627.09 (n/a)</td><td>626.79 (n/a)</td><td>625.19 (n/a)</td><td>1.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.55 (-2.60%)</td><td>6.35 (-10.98%)</td><td>7.22 (+2.46%)</td><td>4.70 <b>(-30.61%)</b></td><td>1.41 <b>(+260.05%)</b></td><td>1898.10 <b>(+44.11%)</b></td><td>1465.80 (+17.08%)</td><td>1233.70 (-2.40%)</td><td>1180.90 (+2.67%)</td><td>353.79 <b>(+433.38%)</b></td><td>454.63 (-2.60%)</td><td>382.62 (-10.98%)</td><td>435.17 (+2.46%)</td><td>282.85 <b>(-30.61%)</b></td><td>84.80 <b>(+260.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>7.75 (n/a)</td><td>7.14 (n/a)</td><td>7.05 (n/a)</td><td>6.77 (n/a)</td><td>0.39 (n/a)</td><td>1317.10 (n/a)</td><td>1252.00 (n/a)</td><td>1264.10 (n/a)</td><td>1150.20 (n/a)</td><td>66.33 (n/a)</td><td>466.78 (n/a)</td><td>429.81 (n/a)</td><td>424.71 (n/a)</td><td>407.63 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.26 (+5.41%)</td><td>7.03 (+3.85%)</td><td>7.06 (+4.86%)</td><td>6.77 (+1.95%)</td><td>0.19 <b>(+87.40%)</b></td><td>1317.20 (-1.91%)</td><td>1269.46 (-3.67%)</td><td>1263.10 (-4.64%)</td><td>1227.50 (-5.13%)</td><td>34.24 <b>(+74.91%)</b></td><td>437.36 (+5.41%)</td><td>423.16 (+3.85%)</td><td>425.03 (+4.86%)</td><td>407.60 (+1.95%)</td><td>11.35 <b>(+87.40%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>6.89 (n/a)</td><td>6.76 (n/a)</td><td>6.73 (n/a)</td><td>6.64 (n/a)</td><td>0.10 (n/a)</td><td>1342.80 (n/a)</td><td>1317.82 (n/a)</td><td>1324.60 (n/a)</td><td>1293.90 (n/a)</td><td>19.58 (n/a)</td><td>414.91 (n/a)</td><td>407.47 (n/a)</td><td>405.31 (n/a)</td><td>399.81 (n/a)</td><td>6.06 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.33 (+3.73%)</td><td>6.25 (-3.01%)</td><td>6.52 (-4.03%)</td><td>4.91 (+1.42%)</td><td>1.05 (+16.32%)</td><td>1815.60 (-1.40%)</td><td>1461.42 (+3.60%)</td><td>1366.60 (+4.20%)</td><td>1215.30 (-3.59%)</td><td>260.51 (+7.55%)</td><td>441.77 (+3.73%)</td><td>376.39 (-3.01%)</td><td>392.85 (-4.03%)</td><td>295.71 (+1.42%)</td><td>63.55 (+16.32%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>7.07 (n/a)</td><td>6.44 (n/a)</td><td>6.80 (n/a)</td><td>4.84 (n/a)</td><td>0.91 (n/a)</td><td>1841.30 (n/a)</td><td>1410.66 (n/a)</td><td>1311.50 (n/a)</td><td>1260.60 (n/a)</td><td>242.23 (n/a)</td><td>425.90 (n/a)</td><td>388.08 (n/a)</td><td>409.36 (n/a)</td><td>291.58 (n/a)</td><td>54.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>8.38 (-0.73%)</td><td>8.04 (+1.58%)</td><td>7.95 (+0.11%)</td><td>7.84 (+6.83%)</td><td>0.21 <b>(-47.98%)</b></td><td>4447.30 (-6.40%)</td><td>4339.64 (-1.71%)</td><td>4383.60 (-0.11%)</td><td>4162.10 (+0.74%)</td><td>111.92 <b>(-51.23%)</b></td><td>515.96 (-0.73%)</td><td>495.12 (+1.58%)</td><td>489.89 (+0.11%)</td><td>482.87 (+6.83%)</td><td>13.02 <b>(-47.98%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>8.44 (n/a)</td><td>7.91 (n/a)</td><td>7.95 (n/a)</td><td>7.34 (n/a)</td><td>0.41 (n/a)</td><td>4751.20 (n/a)</td><td>4415.02 (n/a)</td><td>4388.30 (n/a)</td><td>4131.60 (n/a)</td><td>229.49 (n/a)</td><td>519.77 (n/a)</td><td>487.44 (n/a)</td><td>489.37 (n/a)</td><td>451.99 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.91 (-1.06%)</td><td>7.57 (+0.00%)</td><td>7.56 (-0.09%)</td><td>7.37 (+2.90%)</td><td>0.21 <b>(-29.69%)</b></td><td>4731.00 (-2.82%)</td><td>4606.26 (-0.07%)</td><td>4610.00 (+0.09%)</td><td>4410.20 (+1.07%)</td><td>123.72 <b>(-31.14%)</b></td><td>486.94 (-1.06%)</td><td>466.48 (+0.00%)</td><td>465.83 (-0.09%)</td><td>453.92 (+2.90%)</td><td>12.77 <b>(-29.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>7.99 (n/a)</td><td>7.57 (n/a)</td><td>7.57 (n/a)</td><td>7.16 (n/a)</td><td>0.29 (n/a)</td><td>4868.20 (n/a)</td><td>4609.26 (n/a)</td><td>4606.00 (n/a)</td><td>4363.30 (n/a)</td><td>179.66 (n/a)</td><td>492.17 (n/a)</td><td>466.47 (n/a)</td><td>466.24 (n/a)</td><td>441.12 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.52 (+0.66%)</td><td>7.33 (+0.47%)</td><td>7.26 (-1.56%)</td><td>7.18 (+3.92%)</td><td>0.14 <b>(-36.83%)</b></td><td>4856.80 (-3.77%)</td><td>4759.10 (-0.52%)</td><td>4804.80 (+1.58%)</td><td>4636.60 (-0.66%)</td><td>91.21 <b>(-40.03%)</b></td><td>463.16 (+0.66%)</td><td>451.37 (+0.47%)</td><td>446.94 (-1.56%)</td><td>442.16 (+3.92%)</td><td>8.71 <b>(-36.83%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>7.47 (n/a)</td><td>7.29 (n/a)</td><td>7.37 (n/a)</td><td>6.91 (n/a)</td><td>0.22 (n/a)</td><td>5047.30 (n/a)</td><td>4784.00 (n/a)</td><td>4730.00 (n/a)</td><td>4667.20 (n/a)</td><td>152.09 (n/a)</td><td>460.12 (n/a)</td><td>449.24 (n/a)</td><td>454.01 (n/a)</td><td>425.47 (n/a)</td><td>13.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.79 (+0.57%)</td><td>0.79 (+0.33%)</td><td>0.79 (+0.32%)</td><td>0.79 (+0.16%)</td><td>0.00 <b>(+868.98%)</b></td><td>95909.80 (-0.16%)</td><td>95732.78 (-0.33%)</td><td>95746.20 (-0.32%)</td><td>95488.50 (-0.56%)</td><td>152.65 <b>(+862.96%)</b></td><td>719.66 (+0.57%)</td><td>717.83 (+0.33%)</td><td>717.73 (+0.32%)</td><td>716.50 (+0.16%)</td><td>1.15 <b>(+868.92%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96060.20 (n/a)</td><td>96045.32 (n/a)</td><td>96053.50 (n/a)</td><td>96028.10 (n/a)</td><td>15.85 (n/a)</td><td>715.62 (n/a)</td><td>715.49 (n/a)</td><td>715.43 (n/a)</td><td>715.38 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.73 (-0.66%)</td><td>0.73 (-0.60%)</td><td>0.73 (-0.59%)</td><td>0.73 (-0.59%)</td><td>0.00 <b>(-58.02%)</b></td><td>102959.20 (+0.59%)</td><td>102920.00 (+0.61%)</td><td>102916.70 (+0.59%)</td><td>102891.40 (+0.67%)</td><td>24.58 <b>(-57.51%)</b></td><td>667.88 (-0.66%)</td><td>667.70 (-0.60%)</td><td>667.72 (-0.59%)</td><td>667.44 (-0.59%)</td><td>0.16 <b>(-58.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102356.40 (n/a)</td><td>102298.80 (n/a)</td><td>102312.00 (n/a)</td><td>102208.80 (n/a)</td><td>57.86 (n/a)</td><td>672.34 (n/a)</td><td>671.75 (n/a)</td><td>671.67 (n/a)</td><td>671.37 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.70 (+0.22%)</td><td>0.70 (+0.12%)</td><td>0.70 (+0.03%)</td><td>0.70 (+0.07%)</td><td>0.00 <b>(+70.12%)</b></td><td>108362.00 (-0.07%)</td><td>108114.94 (-0.12%)</td><td>108198.50 (-0.03%)</td><td>107850.00 (-0.22%)</td><td>219.50 <b>(+69.59%)</b></td><td>637.18 (+0.22%)</td><td>635.62 (+0.12%)</td><td>635.12 (+0.03%)</td><td>634.17 (+0.07%)</td><td>1.29 <b>(+70.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108442.70 (n/a)</td><td>108241.50 (n/a)</td><td>108227.80 (n/a)</td><td>108092.50 (n/a)</td><td>129.44 (n/a)</td><td>635.75 (n/a)</td><td>634.87 (n/a)</td><td>634.95 (n/a)</td><td>633.69 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>4.22 (+2.73%)</td><td>3.52 (-1.83%)</td><td>3.44 (-4.31%)</td><td>3.03 (-1.09%)</td><td>0.44 (+17.41%)</td><td>2663.20 (+1.10%)</td><td>2317.36 (+2.15%)</td><td>2341.50 (+4.50%)</td><td>1910.30 (-2.65%)</td><td>269.78 (+12.74%)</td><td>1106.61 (+2.73%)</td><td>922.78 (-1.83%)</td><td>902.80 (-4.31%)</td><td>793.76 (-1.09%)</td><td>114.16 (+17.41%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>4.11 (n/a)</td><td>3.58 (n/a)</td><td>3.60 (n/a)</td><td>3.06 (n/a)</td><td>0.37 (n/a)</td><td>2634.20 (n/a)</td><td>2268.62 (n/a)</td><td>2240.70 (n/a)</td><td>1962.40 (n/a)</td><td>239.29 (n/a)</td><td>1077.23 (n/a)</td><td>939.97 (n/a)</td><td>943.42 (n/a)</td><td>802.50 (n/a)</td><td>97.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.57 (+8.14%)</td><td>0.40 (-6.69%)</td><td>0.35 <b>(-28.73%)</b></td><td>0.30 (-4.89%)</td><td>0.11 (+14.33%)</td><td>4130.40 (+5.14%)</td><td>3272.10 (+8.40%)</td><td>3567.80 <b>(+40.30%)</b></td><td>2192.70 (-7.53%)</td><td>836.73 (+9.79%)</td><td>30.61 (+8.14%)</td><td>21.76 (-6.69%)</td><td>18.81 <b>(-28.73%)</b></td><td>16.25 (-4.89%)</td><td>6.19 (+14.33%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.10 (n/a)</td><td>3928.60 (n/a)</td><td>3018.56 (n/a)</td><td>2542.90 (n/a)</td><td>2371.20 (n/a)</td><td>762.15 (n/a)</td><td>28.30 (n/a)</td><td>23.32 (n/a)</td><td>26.39 (n/a)</td><td>17.08 (n/a)</td><td>5.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.47 (+0.02%)</td><td>5.07 (+2.79%)</td><td>4.96 (+1.62%)</td><td>3.92 (+3.50%)</td><td>0.93 (-4.32%)</td><td>1695.30 (-3.38%)</td><td>1346.66 (-3.00%)</td><td>1342.10 (-1.60%)</td><td>1028.10 (-0.03%)</td><td>241.53 (-6.54%)</td><td>1998.95 (+0.02%)</td><td>1566.53 (+2.79%)</td><td>1531.29 (+1.62%)</td><td>1212.28 (+3.50%)</td><td>286.36 (-4.32%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>6.47 (n/a)</td><td>4.93 (n/a)</td><td>4.88 (n/a)</td><td>3.79 (n/a)</td><td>0.97 (n/a)</td><td>1754.60 (n/a)</td><td>1388.34 (n/a)</td><td>1363.90 (n/a)</td><td>1028.40 (n/a)</td><td>258.44 (n/a)</td><td>1998.52 (n/a)</td><td>1524.02 (n/a)</td><td>1506.83 (n/a)</td><td>1171.31 (n/a)</td><td>299.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (-4.48%)</td><td>0.24 (-0.63%)</td><td>0.26 (+1.61%)</td><td>0.21 (+4.68%)</td><td>0.02 <b>(-24.95%)</b></td><td>0.26 (-4.48%)</td><td>0.24 (-0.63%)</td><td>0.25 (+1.61%)</td><td>0.21 (+4.68%)</td><td>0.02 <b>(-24.95%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.70 (+2.75%)</td><td>12.66 (-2.48%)</td><td>13.20 (+0.40%)</td><td>11.24 (-7.93%)</td><td>1.08 <b>(+141.94%)</b></td><td>13.69 (+2.75%)</td><td>12.65 (-2.48%)</td><td>13.20 (+0.40%)</td><td>11.24 (-7.93%)</td><td>1.08 <b>(+141.94%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>13.33 (n/a)</td><td>12.98 (n/a)</td><td>13.15 (n/a)</td><td>12.21 (n/a)</td><td>0.45 (n/a)</td><td>13.32 (n/a)</td><td>12.97 (n/a)</td><td>13.14 (n/a)</td><td>12.21 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>25.25 (+1.94%)</td><td>24.54 (+6.37%)</td><td>24.66 (+1.88%)</td><td>23.76 <b>(+23.60%)</b></td><td>0.56 <b>(-75.33%)</b></td><td>25.23 (+1.94%)</td><td>24.53 (+6.37%)</td><td>24.65 (+1.88%)</td><td>23.74 <b>(+23.60%)</b></td><td>0.56 <b>(-75.33%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>24.77 (n/a)</td><td>23.07 (n/a)</td><td>24.21 (n/a)</td><td>19.22 (n/a)</td><td>2.27 (n/a)</td><td>24.75 (n/a)</td><td>23.06 (n/a)</td><td>24.20 (n/a)</td><td>19.21 (n/a)</td><td>2.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>42.03 (+0.67%)</td><td>39.74 (+0.86%)</td><td>40.14 (+1.98%)</td><td>36.77 (-3.27%)</td><td>2.27 <b>(+53.76%)</b></td><td>42.01 (+0.67%)</td><td>39.71 (+0.86%)</td><td>40.12 (+1.98%)</td><td>36.75 (-3.27%)</td><td>2.26 <b>(+53.76%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>41.75 (n/a)</td><td>39.40 (n/a)</td><td>39.36 (n/a)</td><td>38.02 (n/a)</td><td>1.47 (n/a)</td><td>41.73 (n/a)</td><td>39.37 (n/a)</td><td>39.34 (n/a)</td><td>37.99 (n/a)</td><td>1.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>44.92 (+2.48%)</td><td>43.05 (+1.47%)</td><td>43.51 (+3.35%)</td><td>40.38 (-3.89%)</td><td>1.97 <b>(+151.98%)</b></td><td>44.89 (+2.48%)</td><td>43.03 (+1.47%)</td><td>43.49 (+3.35%)</td><td>40.35 (-3.89%)</td><td>1.97 <b>(+151.98%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>43.83 (n/a)</td><td>42.43 (n/a)</td><td>42.10 (n/a)</td><td>42.01 (n/a)</td><td>0.78 (n/a)</td><td>43.80 (n/a)</td><td>42.41 (n/a)</td><td>42.08 (n/a)</td><td>41.99 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.44 (-0.02%)</td><td>12.15 (-6.52%)</td><td>12.27 (-6.85%)</td><td>10.37 (-17.01%)</td><td>1.28 <b>(+213.57%)</b></td><td>13.43 (-0.02%)</td><td>12.14 (-6.52%)</td><td>12.26 (-6.85%)</td><td>10.36 (-17.01%)</td><td>1.28 <b>(+213.57%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>13.44 (n/a)</td><td>12.99 (n/a)</td><td>13.17 (n/a)</td><td>12.49 (n/a)</td><td>0.41 (n/a)</td><td>13.44 (n/a)</td><td>12.99 (n/a)</td><td>13.16 (n/a)</td><td>12.48 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>25.13 (+1.64%)</td><td>24.58 (+1.72%)</td><td>24.68 (+2.50%)</td><td>23.97 (+1.54%)</td><td>0.47 (+10.40%)</td><td>25.11 (+1.64%)</td><td>24.56 (+1.72%)</td><td>24.66 (+2.50%)</td><td>23.96 (+1.54%)</td><td>0.47 (+10.40%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>24.72 (n/a)</td><td>24.16 (n/a)</td><td>24.08 (n/a)</td><td>23.61 (n/a)</td><td>0.42 (n/a)</td><td>24.71 (n/a)</td><td>24.15 (n/a)</td><td>24.06 (n/a)</td><td>23.60 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>43.72 (+7.02%)</td><td>40.54 (+1.41%)</td><td>39.93 (-0.31%)</td><td>38.50 (-1.78%)</td><td>2.15 <b>(+238.22%)</b></td><td>43.70 (+7.02%)</td><td>40.52 (+1.41%)</td><td>39.91 (-0.31%)</td><td>38.48 (-1.78%)</td><td>2.15 <b>(+238.22%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>40.86 (n/a)</td><td>39.98 (n/a)</td><td>40.05 (n/a)</td><td>39.20 (n/a)</td><td>0.64 (n/a)</td><td>40.83 (n/a)</td><td>39.96 (n/a)</td><td>40.03 (n/a)</td><td>39.17 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>47.73 (+2.82%)</td><td>43.83 (+3.76%)</td><td>43.66 (+2.03%)</td><td>41.36 (+8.21%)</td><td>2.45 (-18.74%)</td><td>47.70 (+2.82%)</td><td>43.80 (+3.76%)</td><td>43.63 (+2.03%)</td><td>41.33 (+8.21%)</td><td>2.45 (-18.74%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>46.41 (n/a)</td><td>42.24 (n/a)</td><td>42.79 (n/a)</td><td>38.22 (n/a)</td><td>3.02 (n/a)</td><td>46.39 (n/a)</td><td>42.21 (n/a)</td><td>42.76 (n/a)</td><td>38.20 (n/a)</td><td>3.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>159.70 (n/a)</td><td>150.38 (n/a)</td><td>152.20 (n/a)</td><td>138.60 (n/a)</td><td>7.92 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>152.70 (n/a)</td><td>141.68 (n/a)</td><td>136.20 (n/a)</td><td>134.60 (n/a)</td><td>8.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>150.70 (n/a)</td><td>145.78 (n/a)</td><td>148.00 (n/a)</td><td>134.10 (n/a)</td><td>6.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.90 (n/a)</td><td>151.52 (n/a)</td><td>149.60 (n/a)</td><td>129.50 (n/a)</td><td>16.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>144.68 (n/a)</td><td>144.10 (n/a)</td><td>112.20 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.40 (n/a)</td><td>171.52 (n/a)</td><td>164.70 (n/a)</td><td>159.40 (n/a)</td><td>14.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>363.00 (n/a)</td><td>200.00 (n/a)</td><td>164.30 (n/a)</td><td>121.60 (n/a)</td><td>95.36 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>363.40 (n/a)</td><td>227.88 (n/a)</td><td>183.80 (n/a)</td><td>170.80 (n/a)</td><td>80.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>151.26 (n/a)</td><td>155.30 (n/a)</td><td>127.40 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.50 (n/a)</td><td>169.22 (n/a)</td><td>147.90 (n/a)</td><td>124.60 (n/a)</td><td>43.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.40 (n/a)</td><td>192.26 (n/a)</td><td>182.20 (n/a)</td><td>129.60 (n/a)</td><td>55.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>391.60 (n/a)</td><td>244.34 (n/a)</td><td>223.90 (n/a)</td><td>148.20 (n/a)</td><td>103.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>186.60 (n/a)</td><td>189.50 (n/a)</td><td>149.10 (n/a)</td><td>36.89 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>192.28 (n/a)</td><td>200.60 (n/a)</td><td>134.70 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.90 (n/a)</td><td>180.26 (n/a)</td><td>157.40 (n/a)</td><td>131.60 (n/a)</td><td>55.62 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.10 (n/a)</td><td>200.24 (n/a)</td><td>198.30 (n/a)</td><td>164.60 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.20 (n/a)</td><td>147.58 (n/a)</td><td>138.50 (n/a)</td><td>124.70 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>171.50 (n/a)</td><td>139.28 (n/a)</td><td>129.60 (n/a)</td><td>119.80 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>166.74 (n/a)</td><td>153.30 (n/a)</td><td>134.40 (n/a)</td><td>29.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>159.00 (n/a)</td><td>146.66 (n/a)</td><td>149.70 (n/a)</td><td>129.90 (n/a)</td><td>10.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.90 (n/a)</td><td>155.42 (n/a)</td><td>147.90 (n/a)</td><td>122.50 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.10 (n/a)</td><td>159.06 (n/a)</td><td>146.50 (n/a)</td><td>130.80 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>282.10 (n/a)</td><td>180.96 (n/a)</td><td>154.80 (n/a)</td><td>119.30 (n/a)</td><td>68.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>303.10 (n/a)</td><td>204.10 (n/a)</td><td>180.50 (n/a)</td><td>151.70 (n/a)</td><td>58.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (+3.31%)</td><td>0.18 (+2.40%)</td><td>0.18 (+3.49%)</td><td>0.16 (+9.74%)</td><td>0.03 (-10.23%)</td><td>201.70 (-8.86%)</td><td>180.68 (-3.11%)</td><td>186.70 (-3.36%)</td><td>138.40 (-3.22%)</td><td>25.33 <b>(-22.21%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.30 (n/a)</td><td>186.48 (n/a)</td><td>193.20 (n/a)</td><td>143.00 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>257.90 (n/a)</td><td>179.46 (n/a)</td><td>157.80 (n/a)</td><td>145.20 (n/a)</td><td>45.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.80 (n/a)</td><td>148.48 (n/a)</td><td>133.10 (n/a)</td><td>123.60 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>169.10 (n/a)</td><td>150.68 (n/a)</td><td>154.20 (n/a)</td><td>128.10 (n/a)</td><td>15.05 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>198.70 (n/a)</td><td>162.48 (n/a)</td><td>151.80 (n/a)</td><td>119.50 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.40 (n/a)</td><td>156.52 (n/a)</td><td>154.50 (n/a)</td><td>133.70 (n/a)</td><td>15.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.40 (n/a)</td><td>162.52 (n/a)</td><td>177.70 (n/a)</td><td>129.10 (n/a)</td><td>25.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>175.10 (n/a)</td><td>166.78 (n/a)</td><td>173.60 (n/a)</td><td>143.30 (n/a)</td><td>13.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-5.44%)</td><td>0.03 (+5.11%)</td><td>0.03 (-1.08%)</td><td>0.03 <b>(+27.49%)</b></td><td>0.00 <b>(-49.99%)</b></td><td>133.00 <b>(-21.58%)</b></td><td>123.06 (-6.83%)</td><td>124.90 (+1.13%)</td><td>110.40 (+5.75%)</td><td>10.18 <b>(-58.88%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>169.60 (n/a)</td><td>132.08 (n/a)</td><td>123.50 (n/a)</td><td>104.40 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-10.08%)</td><td>0.03 (-6.72%)</td><td>0.03 (-6.38%)</td><td>0.02 (-4.33%)</td><td>0.00 (-19.72%)</td><td>165.60 (+4.48%)</td><td>144.10 (+6.87%)</td><td>142.60 (+6.82%)</td><td>125.80 (+11.23%)</td><td>15.59 (-6.74%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>158.50 (n/a)</td><td>134.84 (n/a)</td><td>133.50 (n/a)</td><td>113.10 (n/a)</td><td>16.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 <b>(-22.27%)</b></td><td>0.02 (-13.98%)</td><td>0.02 <b>(-20.75%)</b></td><td>0.02 (-1.46%)</td><td>0.00 <b>(-54.70%)</b></td><td>238.50 (+1.49%)</td><td>217.82 (+13.99%)</td><td>225.70 <b>(+26.16%)</b></td><td>191.90 <b>(+28.71%)</b></td><td>20.24 <b>(-42.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.00 (n/a)</td><td>191.08 (n/a)</td><td>178.90 (n/a)</td><td>149.10 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-5.65%)</td><td>0.02 (-2.39%)</td><td>0.02 (-15.50%)</td><td>0.02 <b>(+34.09%)</b></td><td>0.00 <b>(-34.02%)</b></td><td>237.80 <b>(-25.41%)</b></td><td>199.86 (-2.34%)</td><td>213.10 (+18.39%)</td><td>152.80 (+6.04%)</td><td>33.79 <b>(-50.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>318.80 (n/a)</td><td>204.64 (n/a)</td><td>180.00 (n/a)</td><td>144.10 (n/a)</td><td>68.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-13.51%)</td><td>0.03 (-4.21%)</td><td>0.03 (+16.72%)</td><td>0.02 (-6.23%)</td><td>0.01 <b>(-22.05%)</b></td><td>202.00 (+6.65%)</td><td>159.24 (+3.17%)</td><td>143.90 (-14.35%)</td><td>126.20 (+15.57%)</td><td>35.15 (-3.02%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>154.34 (n/a)</td><td>168.00 (n/a)</td><td>109.20 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-7.22%)</td><td>0.02 (-2.32%)</td><td>0.03 (-2.79%)</td><td>0.02 (+2.91%)</td><td>0.00 (-15.97%)</td><td>209.40 (-2.83%)</td><td>170.16 (+1.37%)</td><td>158.60 (+2.92%)</td><td>140.30 (+7.76%)</td><td>32.26 (-13.11%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>167.86 (n/a)</td><td>154.10 (n/a)</td><td>130.20 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+7.31%)</td><td>0.03 (+4.30%)</td><td>0.03 (+3.59%)</td><td>0.02 (+4.90%)</td><td>0.01 <b>(+42.64%)</b></td><td>197.70 (-4.68%)</td><td>160.62 (-2.75%)</td><td>157.40 (-3.44%)</td><td>127.70 (-6.86%)</td><td>32.51 <b>(+23.64%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.40 (n/a)</td><td>165.16 (n/a)</td><td>163.00 (n/a)</td><td>137.10 (n/a)</td><td>26.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+9.17%)</td><td>0.03 (+0.05%)</td><td>0.02 (-1.69%)</td><td>0.02 (-12.75%)</td><td>0.01 <b>(+40.56%)</b></td><td>232.40 (+14.60%)</td><td>166.40 (+2.56%)</td><td>165.00 (+1.73%)</td><td>122.20 (-8.40%)</td><td>43.14 <b>(+50.07%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.80 (n/a)</td><td>162.24 (n/a)</td><td>162.20 (n/a)</td><td>133.40 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+13.20%)</td><td>0.03 <b>(+21.28%)</b></td><td>0.03 <b>(+28.67%)</b></td><td>0.02 <b>(+40.94%)</b></td><td>0.00 <b>(-41.71%)</b></td><td>179.10 <b>(-29.04%)</b></td><td>156.38 (-19.48%)</td><td>154.40 <b>(-22.29%)</b></td><td>139.30 (-11.67%)</td><td>14.83 <b>(-61.95%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.40 (n/a)</td><td>194.22 (n/a)</td><td>198.70 (n/a)</td><td>157.70 (n/a)</td><td>38.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+10.87%)</td><td>0.02 (-5.14%)</td><td>0.02 (-8.33%)</td><td>0.02 <b>(-28.06%)</b></td><td>0.01 <b>(+138.70%)</b></td><td>260.40 <b>(+39.03%)</b></td><td>185.90 (+10.13%)</td><td>184.60 (+9.10%)</td><td>130.50 (-9.75%)</td><td>48.00 <b>(+206.14%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.30 (n/a)</td><td>168.80 (n/a)</td><td>169.20 (n/a)</td><td>144.60 (n/a)</td><td>15.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+3.31%)</td><td>0.02 (+0.71%)</td><td>0.02 (+1.83%)</td><td>0.02 (+3.35%)</td><td>0.00 (+15.00%)</td><td>197.00 (-3.24%)</td><td>176.62 (-0.51%)</td><td>170.70 (-1.78%)</td><td>150.80 (-3.21%)</td><td>19.36 (+9.03%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>177.52 (n/a)</td><td>173.80 (n/a)</td><td>155.80 (n/a)</td><td>17.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-10.93%)</td><td>0.02 (-7.64%)</td><td>0.02 (-2.98%)</td><td>0.02 (-3.07%)</td><td>0.00 <b>(-26.33%)</b></td><td>211.30 (+3.17%)</td><td>178.96 (+7.19%)</td><td>173.40 (+3.09%)</td><td>142.90 (+12.25%)</td><td>25.76 (-14.75%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.80 (n/a)</td><td>166.96 (n/a)</td><td>168.20 (n/a)</td><td>127.30 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (+4.88%)</td><td>0.02 (+0.73%)</td><td>0.02 (-4.96%)</td><td>0.02 <b>(+31.01%)</b></td><td>0.00 <b>(-39.17%)</b></td><td>218.30 <b>(-23.67%)</b></td><td>199.38 (-3.00%)</td><td>201.80 (+5.21%)</td><td>168.40 (-4.64%)</td><td>19.33 <b>(-57.52%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>286.00 (n/a)</td><td>205.54 (n/a)</td><td>191.80 (n/a)</td><td>176.60 (n/a)</td><td>45.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(+39.64%)</b></td><td>0.02 (+3.72%)</td><td>0.02 (-9.38%)</td><td>0.02 (-3.38%)</td><td>0.01 <b>(+158.62%)</b></td><td>213.40 (+3.49%)</td><td>175.66 (+1.08%)</td><td>187.70 (+10.35%)</td><td>106.40 <b>(-28.40%)</b></td><td>41.41 <b>(+82.29%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.20 (n/a)</td><td>173.78 (n/a)</td><td>170.10 (n/a)</td><td>148.60 (n/a)</td><td>22.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+1.54%)</td><td>0.02 (-0.82%)</td><td>0.02 (-5.18%)</td><td>0.02 (+15.06%)</td><td>0.00 (-10.37%)</td><td>248.30 (-13.09%)</td><td>207.66 (-0.72%)</td><td>223.30 (+5.48%)</td><td>147.00 (-1.54%)</td><td>40.82 <b>(-23.26%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>285.70 (n/a)</td><td>209.16 (n/a)</td><td>211.70 (n/a)</td><td>149.30 (n/a)</td><td>53.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-17.05%)</td><td>0.02 (-10.00%)</td><td>0.02 (-17.68%)</td><td>0.02 (+10.13%)</td><td>0.00 <b>(-52.27%)</b></td><td>225.30 (-9.19%)</td><td>193.48 (+5.18%)</td><td>193.60 <b>(+21.46%)</b></td><td>152.20 <b>(+20.60%)</b></td><td>27.19 <b>(-51.27%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.10 (n/a)</td><td>183.96 (n/a)</td><td>159.40 (n/a)</td><td>126.20 (n/a)</td><td>55.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 <b>(-28.41%)</b></td><td>0.05 (-12.84%)</td><td>0.04 (-10.46%)</td><td>0.04 (-3.30%)</td><td>0.00 <b>(-72.17%)</b></td><td>187.60 (+3.42%)</td><td>178.06 (+12.10%)</td><td>182.70 (+11.67%)</td><td>163.00 <b>(+39.67%)</b></td><td>10.74 <b>(-59.49%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>158.84 (n/a)</td><td>163.60 (n/a)</td><td>116.70 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 <b>(-20.81%)</b></td><td>0.04 (-14.83%)</td><td>0.04 (-17.72%)</td><td>0.04 (-4.22%)</td><td>0.00 <b>(-53.11%)</b></td><td>210.20 (+4.37%)</td><td>192.60 (+15.63%)</td><td>188.80 <b>(+21.57%)</b></td><td>170.10 <b>(+26.28%)</b></td><td>16.95 <b>(-38.35%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>166.56 (n/a)</td><td>155.30 (n/a)</td><td>134.70 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-7.88%)</td><td>0.03 (-6.53%)</td><td>0.04 (-3.90%)</td><td>0.02 (-14.68%)</td><td>0.01 (+6.84%)</td><td>374.20 (+17.19%)</td><td>255.96 (+8.48%)</td><td>232.30 (+4.08%)</td><td>205.00 (+8.58%)</td><td>67.42 <b>(+37.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.30 (n/a)</td><td>235.96 (n/a)</td><td>223.20 (n/a)</td><td>188.80 (n/a)</td><td>49.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (+4.88%)</td><td>0.04 (+11.65%)</td><td>0.04 (+1.94%)</td><td>0.03 <b>(+44.68%)</b></td><td>0.01 <b>(-35.09%)</b></td><td>238.70 <b>(-30.87%)</b></td><td>190.84 (-18.90%)</td><td>192.10 (-1.89%)</td><td>133.50 (-4.64%)</td><td>37.53 <b>(-61.34%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>345.30 (n/a)</td><td>235.30 (n/a)</td><td>195.80 (n/a)</td><td>140.00 (n/a)</td><td>97.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(-41.70%)</b></td><td>0.04 <b>(-31.94%)</b></td><td>0.04 <b>(-22.17%)</b></td><td>0.03 <b>(-42.01%)</b></td><td>0.01 <b>(-34.68%)</b></td><td>316.00 <b>(+72.39%)</b></td><td>228.22 <b>(+48.04%)</b></td><td>204.40 <b>(+28.47%)</b></td><td>198.70 <b>(+71.59%)</b></td><td>50.02 <b>(+100.65%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>154.16 (n/a)</td><td>159.10 (n/a)</td><td>115.80 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 <b>(-22.02%)</b></td><td>0.04 (-12.94%)</td><td>0.04 (-13.14%)</td><td>0.04 (-7.96%)</td><td>0.01 <b>(-43.09%)</b></td><td>220.00 (+8.64%)</td><td>195.36 (+13.34%)</td><td>197.30 (+15.11%)</td><td>168.90 <b>(+28.25%)</b></td><td>22.76 <b>(-21.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>172.36 (n/a)</td><td>171.40 (n/a)</td><td>131.70 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (-3.91%)</td><td>0.04 <b>(-20.43%)</b></td><td>0.04 <b>(-25.04%)</b></td><td>0.04 (-12.66%)</td><td>0.01 (+12.59%)</td><td>216.80 (+14.47%)</td><td>195.48 <b>(+27.13%)</b></td><td>210.90 <b>(+33.40%)</b></td><td>133.60 (+4.05%)</td><td>34.86 <b>(+35.65%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>153.76 (n/a)</td><td>158.10 (n/a)</td><td>128.40 (n/a)</td><td>25.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 <b>(-23.78%)</b></td><td>0.04 <b>(-22.64%)</b></td><td>0.04 (-19.02%)</td><td>0.02 <b>(-40.40%)</b></td><td>0.01 (+5.95%)</td><td>345.00 <b>(+67.72%)</b></td><td>220.96 <b>(+34.13%)</b></td><td>190.40 <b>(+23.48%)</b></td><td>173.30 <b>(+31.19%)</b></td><td>70.78 <b>(+139.99%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>164.74 (n/a)</td><td>154.20 (n/a)</td><td>132.10 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (-15.66%)</td><td>0.04 <b>(-26.96%)</b></td><td>0.04 <b>(-22.84%)</b></td><td>0.02 <b>(-41.70%)</b></td><td>0.01 <b>(+50.33%)</b></td><td>356.60 <b>(+71.52%)</b></td><td>238.30 <b>(+43.85%)</b></td><td>201.90 <b>(+29.59%)</b></td><td>178.10 (+18.58%)</td><td>73.36 <b>(+204.33%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>165.66 (n/a)</td><td>155.80 (n/a)</td><td>150.20 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (+1.89%)</td><td>0.05 (-7.68%)</td><td>0.04 (-14.68%)</td><td>0.04 (-1.00%)</td><td>0.01 <b>(+22.81%)</b></td><td>195.30 (+1.03%)</td><td>178.58 (+8.86%)</td><td>189.80 (+17.23%)</td><td>141.00 (-1.88%)</td><td>22.99 <b>(+21.18%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>164.04 (n/a)</td><td>161.90 (n/a)</td><td>143.70 (n/a)</td><td>18.98 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (-16.03%)</td><td>0.05 (-2.62%)</td><td>0.05 (-0.96%)</td><td>0.04 (+5.04%)</td><td>0.00 <b>(-58.71%)</b></td><td>200.20 (-4.76%)</td><td>179.16 (+1.28%)</td><td>174.90 (+0.98%)</td><td>169.20 (+19.15%)</td><td>12.27 <b>(-52.52%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>176.90 (n/a)</td><td>173.20 (n/a)</td><td>142.00 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 <b>(-23.90%)</b></td><td>0.04 (-13.50%)</td><td>0.04 (-16.57%)</td><td>0.04 (+4.68%)</td><td>0.00 <b>(-57.51%)</b></td><td>205.00 (-4.47%)</td><td>185.24 (+12.25%)</td><td>192.30 (+19.89%)</td><td>160.30 <b>(+31.39%)</b></td><td>19.12 <b>(-46.90%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>165.02 (n/a)</td><td>160.40 (n/a)</td><td>122.00 (n/a)</td><td>36.00 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (-14.72%)</td><td>0.05 (+1.14%)</td><td>0.05 (+7.67%)</td><td>0.04 (+5.02%)</td><td>0.01 <b>(-43.41%)</b></td><td>208.80 (-4.79%)</td><td>171.76 (-3.24%)</td><td>171.00 (-7.12%)</td><td>150.20 (+17.25%)</td><td>22.72 <b>(-35.08%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>177.52 (n/a)</td><td>184.10 (n/a)</td><td>128.10 (n/a)</td><td>34.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (+9.47%)</td><td>0.05 (-1.77%)</td><td>0.04 (-1.57%)</td><td>0.04 (+8.89%)</td><td>0.01 (+9.35%)</td><td>206.60 (-8.14%)</td><td>176.84 (+1.78%)</td><td>191.40 (+1.59%)</td><td>113.60 (-8.68%)</td><td>37.34 (-9.05%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>173.74 (n/a)</td><td>188.40 (n/a)</td><td>124.40 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (-11.25%)</td><td>0.04 (-8.73%)</td><td>0.04 (-12.88%)</td><td>0.04 (-11.57%)</td><td>0.01 (-4.79%)</td><td>228.40 (+13.07%)</td><td>191.90 (+10.08%)</td><td>202.30 (+14.75%)</td><td>143.50 (+12.64%)</td><td>35.92 <b>(+25.23%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>174.32 (n/a)</td><td>176.30 (n/a)</td><td>127.40 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 <b>(+57.55%)</b></td><td>0.05 (+10.23%)</td><td>0.05 (+2.47%)</td><td>0.04 (-15.46%)</td><td>0.02 <b>(+431.08%)</b></td><td>224.60 (+18.27%)</td><td>168.26 (-2.17%)</td><td>164.20 (-2.38%)</td><td>102.20 <b>(-36.56%)</b></td><td>49.65 <b>(+305.43%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.90 (n/a)</td><td>172.00 (n/a)</td><td>168.20 (n/a)</td><td>161.10 (n/a)</td><td>12.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (+3.02%)</td><td>0.12 (+11.78%)</td><td>0.13 <b>(+31.98%)</b></td><td>0.09 (+12.50%)</td><td>0.02 (+0.56%)</td><td>178.90 (-11.13%)</td><td>145.60 (-10.84%)</td><td>128.70 <b>(-24.20%)</b></td><td>123.50 (-2.99%)</td><td>27.86 (-11.84%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.30 (n/a)</td><td>163.30 (n/a)</td><td>169.80 (n/a)</td><td>127.30 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (-14.13%)</td><td>0.09 (-9.03%)</td><td>0.09 (-8.57%)</td><td>0.08 (-8.79%)</td><td>0.01 <b>(-24.22%)</b></td><td>202.60 (+9.63%)</td><td>180.40 (+9.68%)</td><td>179.60 (+9.38%)</td><td>163.70 (+16.43%)</td><td>16.13 (-3.39%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>164.48 (n/a)</td><td>164.20 (n/a)</td><td>140.60 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (-19.28%)</td><td>0.08 (-9.74%)</td><td>0.08 (-9.81%)</td><td>0.05 (+4.10%)</td><td>0.02 <b>(-32.70%)</b></td><td>316.70 (-3.91%)</td><td>218.48 (+6.82%)</td><td>192.80 (+10.87%)</td><td>177.10 <b>(+23.93%)</b></td><td>57.03 <b>(-22.10%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>329.60 (n/a)</td><td>204.54 (n/a)</td><td>173.90 (n/a)</td><td>142.90 (n/a)</td><td>73.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (+15.41%)</td><td>0.10 <b>(+21.91%)</b></td><td>0.10 <b>(+21.39%)</b></td><td>0.08 <b>(+44.85%)</b></td><td>0.01 <b>(-23.49%)</b></td><td>202.20 <b>(-30.97%)</b></td><td>170.70 (-19.69%)</td><td>164.70 (-17.61%)</td><td>151.60 (-13.37%)</td><td>20.65 <b>(-55.79%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>292.90 (n/a)</td><td>212.54 (n/a)</td><td>199.90 (n/a)</td><td>175.00 (n/a)</td><td>46.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (-16.95%)</td><td>0.10 (+16.85%)</td><td>0.10 <b>(+23.62%)</b></td><td>0.08 <b>(+58.10%)</b></td><td>0.01 <b>(-55.78%)</b></td><td>209.80 <b>(-36.75%)</b></td><td>164.40 <b>(-21.65%)</b></td><td>158.10 (-19.09%)</td><td>145.90 <b>(+20.38%)</b></td><td>26.29 <b>(-66.14%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>331.70 (n/a)</td><td>209.82 (n/a)</td><td>195.40 (n/a)</td><td>121.20 (n/a)</td><td>77.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (-9.72%)</td><td>0.11 (+0.87%)</td><td>0.10 (-0.02%)</td><td>0.09 (+2.94%)</td><td>0.02 (-17.01%)</td><td>184.30 (-2.85%)</td><td>154.80 (-1.91%)</td><td>168.00 (+0.06%)</td><td>119.70 (+10.73%)</td><td>29.61 (-11.43%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>189.70 (n/a)</td><td>157.82 (n/a)</td><td>167.90 (n/a)</td><td>108.10 (n/a)</td><td>33.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (+4.45%)</td><td>0.10 (-4.77%)</td><td>0.11 (+1.38%)</td><td>0.09 (-11.22%)</td><td>0.02 <b>(+87.12%)</b></td><td>190.50 (+12.66%)</td><td>162.46 (+6.78%)</td><td>152.10 (-1.36%)</td><td>128.20 (-4.26%)</td><td>27.00 <b>(+110.28%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.10 (n/a)</td><td>152.14 (n/a)</td><td>154.20 (n/a)</td><td>133.90 (n/a)</td><td>12.84 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (-3.28%)</td><td>0.11 (+4.86%)</td><td>0.11 (+12.46%)</td><td>0.09 (+4.25%)</td><td>0.01 <b>(-25.89%)</b></td><td>178.80 (-4.08%)</td><td>152.78 (-5.49%)</td><td>151.40 (-11.10%)</td><td>132.90 (+3.34%)</td><td>17.95 <b>(-26.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>161.66 (n/a)</td><td>170.30 (n/a)</td><td>128.60 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (-2.76%)</td><td>0.10 (+2.89%)</td><td>0.10 (+14.67%)</td><td>0.07 (-6.60%)</td><td>0.01 (-1.75%)</td><td>223.20 (+7.05%)</td><td>174.72 (-2.66%)</td><td>163.50 (-12.80%)</td><td>156.60 (+2.82%)</td><td>27.49 (+13.10%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>179.50 (n/a)</td><td>187.50 (n/a)</td><td>152.30 (n/a)</td><td>24.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 <b>(-23.99%)</b></td><td>0.10 (-1.40%)</td><td>0.09 (+9.12%)</td><td>0.09 (+16.41%)</td><td>0.01 <b>(-69.74%)</b></td><td>190.30 (-14.09%)</td><td>173.28 (-3.22%)</td><td>179.30 (-8.38%)</td><td>154.20 <b>(+31.57%)</b></td><td>14.42 <b>(-65.50%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>221.50 (n/a)</td><td>179.04 (n/a)</td><td>195.70 (n/a)</td><td>117.20 (n/a)</td><td>41.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 <b>(+21.51%)</b></td><td>0.11 (+14.92%)</td><td>0.10 (+7.94%)</td><td>0.09 (+3.95%)</td><td>0.02 <b>(+100.81%)</b></td><td>189.80 (-3.80%)</td><td>154.38 (-11.84%)</td><td>156.20 (-7.35%)</td><td>130.60 (-17.71%)</td><td>24.39 <b>(+54.82%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>175.12 (n/a)</td><td>168.60 (n/a)</td><td>158.70 (n/a)</td><td>15.75 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (-8.35%)</td><td>0.11 (-5.77%)</td><td>0.10 (-6.42%)</td><td>0.08 (-14.49%)</td><td>0.02 (-5.86%)</td><td>208.80 (+16.91%)</td><td>158.90 (+6.56%)</td><td>159.10 (+6.85%)</td><td>115.50 (+9.17%)</td><td>34.99 (+19.22%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>178.60 (n/a)</td><td>149.12 (n/a)</td><td>148.90 (n/a)</td><td>105.80 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (+17.37%)</td><td>0.10 (+0.36%)</td><td>0.09 (-7.17%)</td><td>0.09 (-11.74%)</td><td>0.02 <b>(+418.31%)</b></td><td>192.20 (+13.33%)</td><td>165.14 (+1.76%)</td><td>175.30 (+7.74%)</td><td>133.70 (-14.79%)</td><td>26.56 <b>(+400.02%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>169.60 (n/a)</td><td>162.28 (n/a)</td><td>162.70 (n/a)</td><td>156.90 (n/a)</td><td>5.31 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 <b>(+36.16%)</b></td><td>0.12 (+11.53%)</td><td>0.11 (+10.37%)</td><td>0.08 (-10.20%)</td><td>0.03 <b>(+150.71%)</b></td><td>196.40 (+11.34%)</td><td>146.52 (-6.25%)</td><td>145.30 (-9.41%)</td><td>94.50 <b>(-26.57%)</b></td><td>36.76 <b>(+100.76%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.40 (n/a)</td><td>156.28 (n/a)</td><td>160.40 (n/a)</td><td>128.70 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 <b>(-21.89%)</b></td><td>0.09 (-8.09%)</td><td>0.10 (-6.91%)</td><td>0.08 <b>(+33.78%)</b></td><td>0.01 <b>(-52.02%)</b></td><td>208.70 <b>(-25.25%)</b></td><td>178.02 (+2.06%)</td><td>171.20 (+7.40%)</td><td>151.80 <b>(+27.99%)</b></td><td>27.38 <b>(-55.93%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>279.20 (n/a)</td><td>174.42 (n/a)</td><td>159.40 (n/a)</td><td>118.60 (n/a)</td><td>62.14 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 <b>(-35.90%)</b></td><td>0.09 <b>(-24.60%)</b></td><td>0.10 (+0.81%)</td><td>0.04 <b>(-50.76%)</b></td><td>0.03 (-15.74%)</td><td>373.60 <b>(+103.04%)</b></td><td>205.74 <b>(+41.38%)</b></td><td>158.60 (-0.81%)</td><td>153.50 <b>(+56.00%)</b></td><td>94.61 <b>(+179.07%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>184.00 (n/a)</td><td>145.52 (n/a)</td><td>159.90 (n/a)</td><td>98.40 (n/a)</td><td>33.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-6.87%)</td><td>0.21 (-5.14%)</td><td>0.20 (-5.03%)</td><td>0.18 (+4.10%)</td><td>0.03 <b>(-21.65%)</b></td><td>177.70 (-3.95%)</td><td>159.28 (+4.65%)</td><td>162.60 (+5.31%)</td><td>130.70 (+7.40%)</td><td>19.93 (-17.82%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>185.00 (n/a)</td><td>152.20 (n/a)</td><td>154.40 (n/a)</td><td>121.70 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-5.68%)</td><td>0.21 (-10.10%)</td><td>0.20 (-11.33%)</td><td>0.17 (-4.79%)</td><td>0.03 (-11.84%)</td><td>189.60 (+5.04%)</td><td>161.94 (+10.98%)</td><td>161.70 (+12.76%)</td><td>131.60 (+6.04%)</td><td>23.19 (-0.12%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>180.50 (n/a)</td><td>145.92 (n/a)</td><td>143.40 (n/a)</td><td>124.10 (n/a)</td><td>23.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (-2.73%)</td><td>0.15 (+0.05%)</td><td>0.17 (+7.13%)</td><td>0.11 (+2.29%)</td><td>0.03 (+3.79%)</td><td>305.50 (-2.24%)</td><td>222.94 (+0.11%)</td><td>192.00 (-6.66%)</td><td>181.60 (+2.83%)</td><td>52.77 (-0.36%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>312.50 (n/a)</td><td>222.70 (n/a)</td><td>205.70 (n/a)</td><td>176.60 (n/a)</td><td>52.96 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (+11.30%)</td><td>0.22 (+13.50%)</td><td>0.21 (+5.10%)</td><td>0.17 (+14.11%)</td><td>0.03 (-15.28%)</td><td>189.40 (-12.36%)</td><td>154.00 (-12.93%)</td><td>153.30 (-4.90%)</td><td>130.50 (-10.12%)</td><td>21.99 <b>(-33.36%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>216.10 (n/a)</td><td>176.86 (n/a)</td><td>161.20 (n/a)</td><td>145.20 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (-19.08%)</td><td>0.18 <b>(-25.59%)</b></td><td>0.19 <b>(-28.78%)</b></td><td>0.10 <b>(-38.68%)</b></td><td>0.05 (-2.92%)</td><td>334.20 <b>(+63.10%)</b></td><td>194.74 <b>(+40.65%)</b></td><td>169.40 <b>(+40.35%)</b></td><td>137.10 <b>(+23.62%)</b></td><td>79.10 <b>(+105.89%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>204.90 (n/a)</td><td>138.46 (n/a)</td><td>120.70 (n/a)</td><td>110.90 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (-2.05%)</td><td>0.23 (+7.58%)</td><td>0.25 <b>(+25.58%)</b></td><td>0.19 (+5.83%)</td><td>0.04 (-2.27%)</td><td>172.40 (-5.53%)</td><td>144.28 (-7.13%)</td><td>130.90 <b>(-20.33%)</b></td><td>122.30 (+2.09%)</td><td>24.00 (-3.17%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>182.50 (n/a)</td><td>155.36 (n/a)</td><td>164.30 (n/a)</td><td>119.80 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-2.35%)</td><td>0.19 (-12.80%)</td><td>0.19 (-9.11%)</td><td>0.09 <b>(-50.38%)</b></td><td>0.06 <b>(+124.77%)</b></td><td>351.70 <b>(+101.55%)</b></td><td>194.68 <b>(+27.91%)</b></td><td>168.90 (+10.03%)</td><td>131.30 (+2.42%)</td><td>89.87 <b>(+391.09%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>174.50 (n/a)</td><td>152.20 (n/a)</td><td>153.50 (n/a)</td><td>128.20 (n/a)</td><td>18.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-10.57%)</td><td>0.21 (-9.88%)</td><td>0.20 (-8.43%)</td><td>0.17 (-13.23%)</td><td>0.03 (-6.92%)</td><td>188.90 (+15.25%)</td><td>161.64 (+11.14%)</td><td>160.60 (+9.18%)</td><td>130.70 (+11.80%)</td><td>23.38 (+19.40%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>163.90 (n/a)</td><td>145.44 (n/a)</td><td>147.10 (n/a)</td><td>116.90 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (-3.13%)</td><td>0.21 (+8.21%)</td><td>0.22 (+14.02%)</td><td>0.18 (+19.38%)</td><td>0.03 <b>(-22.12%)</b></td><td>183.10 (-16.24%)</td><td>157.70 (-8.80%)</td><td>145.80 (-12.33%)</td><td>133.90 (+3.24%)</td><td>22.84 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.60 (n/a)</td><td>172.92 (n/a)</td><td>166.30 (n/a)</td><td>129.70 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (+5.22%)</td><td>0.22 (+2.87%)</td><td>0.21 (-3.86%)</td><td>0.18 (+9.35%)</td><td>0.04 (+7.18%)</td><td>181.70 (-8.56%)</td><td>150.60 (-2.84%)</td><td>152.80 (+4.02%)</td><td>124.00 (-4.98%)</td><td>25.44 (-8.75%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>198.70 (n/a)</td><td>155.00 (n/a)</td><td>146.90 (n/a)</td><td>130.50 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (+2.04%)</td><td>0.22 (+11.52%)</td><td>0.23 <b>(+25.61%)</b></td><td>0.18 (+2.34%)</td><td>0.03 (+2.07%)</td><td>178.80 (-2.30%)</td><td>148.00 (-10.38%)</td><td>140.90 <b>(-20.40%)</b></td><td>130.70 (-2.02%)</td><td>20.58 (-4.09%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.00 (n/a)</td><td>165.14 (n/a)</td><td>177.00 (n/a)</td><td>133.40 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-10.10%)</td><td>0.20 (-11.87%)</td><td>0.18 <b>(-22.88%)</b></td><td>0.17 (-7.46%)</td><td>0.04 (+15.51%)</td><td>198.30 (+8.07%)</td><td>167.72 (+14.72%)</td><td>185.30 <b>(+29.67%)</b></td><td>133.10 (+11.29%)</td><td>31.66 <b>(+32.94%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>183.50 (n/a)</td><td>146.20 (n/a)</td><td>142.90 (n/a)</td><td>119.60 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (-11.09%)</td><td>0.19 (+2.39%)</td><td>0.19 (-3.09%)</td><td>0.17 <b>(+55.63%)</b></td><td>0.02 <b>(-56.01%)</b></td><td>197.70 <b>(-35.73%)</b></td><td>174.38 (-9.12%)</td><td>171.70 (+3.19%)</td><td>144.30 (+12.47%)</td><td>20.72 <b>(-69.86%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>307.60 (n/a)</td><td>191.88 (n/a)</td><td>166.40 (n/a)</td><td>128.30 (n/a)</td><td>68.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.22 <b>(-20.92%)</b></td><td>0.20 (-6.35%)</td><td>0.19 (-7.19%)</td><td>0.19 (+7.76%)</td><td>0.02 <b>(-60.18%)</b></td><td>174.00 (-7.20%)</td><td>163.76 (+4.48%)</td><td>172.10 (+7.76%)</td><td>148.70 <b>(+26.45%)</b></td><td>12.96 <b>(-52.91%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>187.50 (n/a)</td><td>156.74 (n/a)</td><td>159.70 (n/a)</td><td>117.60 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (-7.45%)</td><td>0.19 (-7.11%)</td><td>0.21 (-7.15%)</td><td>0.14 (-12.39%)</td><td>0.03 (+0.03%)</td><td>238.90 (+14.14%)</td><td>176.90 (+8.31%)</td><td>159.50 (+7.70%)</td><td>145.10 (+8.12%)</td><td>37.49 <b>(+24.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.30 (n/a)</td><td>163.32 (n/a)</td><td>148.10 (n/a)</td><td>134.20 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.33 (+4.92%)</td><td>0.25 (+5.75%)</td><td>0.25 (+5.44%)</td><td>0.19 (+5.39%)</td><td>0.05 (+3.03%)</td><td>175.70 (-5.13%)</td><td>133.10 (-5.58%)</td><td>131.80 (-5.18%)</td><td>99.10 (-4.71%)</td><td>27.84 (-6.36%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>185.20 (n/a)</td><td>140.96 (n/a)</td><td>139.00 (n/a)</td><td>104.00 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (-1.20%)</td><td>0.21 (-0.71%)</td><td>0.21 (-0.66%)</td><td>0.20 (-0.39%)</td><td>0.00 <b>(-78.06%)</b></td><td>40933.00 (+0.39%)</td><td>40882.34 (+0.71%)</td><td>40885.30 (+0.66%)</td><td>40841.80 (+1.21%)</td><td>34.89 <b>(-77.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40774.30 (n/a)</td><td>40592.98 (n/a)</td><td>40615.30 (n/a)</td><td>40352.00 (n/a)</td><td>156.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (-0.55%)</td><td>0.21 (-0.30%)</td><td>0.21 (-0.29%)</td><td>0.20 (-0.24%)</td><td>0.00 <b>(-52.15%)</b></td><td>40952.60 (+0.24%)</td><td>40890.68 (+0.31%)</td><td>40901.90 (+0.29%)</td><td>40806.20 (+0.55%)</td><td>53.00 <b>(-51.80%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40853.30 (n/a)</td><td>40766.28 (n/a)</td><td>40784.20 (n/a)</td><td>40582.30 (n/a)</td><td>109.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (-0.62%)</td><td>0.13 (-0.69%)</td><td>0.13 (-0.68%)</td><td>0.13 (-0.73%)</td><td>0.00 <b>(+80.98%)</b></td><td>322557.30 (+0.74%)</td><td>322264.98 (+0.70%)</td><td>322269.10 (+0.69%)</td><td>321866.90 (+0.62%)</td><td>255.66 <b>(+83.40%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>320197.20 (n/a)</td><td>320029.26 (n/a)</td><td>320076.00 (n/a)</td><td>319879.60 (n/a)</td><td>139.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+8.96%)</td><td>0.03 (+18.54%)</td><td>0.03 <b>(+29.39%)</b></td><td>0.02 (+16.56%)</td><td>0.01 (+14.64%)</td><td>225.70 (-14.22%)</td><td>159.02 (-15.60%)</td><td>128.20 <b>(-22.68%)</b></td><td>120.90 (-8.20%)</td><td>48.10 (-13.06%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>263.10 (n/a)</td><td>188.42 (n/a)</td><td>165.80 (n/a)</td><td>131.70 (n/a)</td><td>55.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-1.22%)</td><td>0.04 (+3.45%)</td><td>0.04 (+11.29%)</td><td>0.03 (-1.91%)</td><td>0.01 (+14.22%)</td><td>207.50 (+1.97%)</td><td>165.44 (-2.74%)</td><td>157.80 (-10.19%)</td><td>137.90 (+1.25%)</td><td>29.20 (+18.08%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>170.10 (n/a)</td><td>175.70 (n/a)</td><td>136.20 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (+13.15%)</td><td>0.03 <b>(+26.33%)</b></td><td>0.03 <b>(+29.54%)</b></td><td>0.02 <b>(+33.96%)</b></td><td>0.00 (-7.93%)</td><td>169.20 <b>(-25.36%)</b></td><td>132.80 <b>(-22.09%)</b></td><td>132.50 <b>(-22.83%)</b></td><td>112.50 (-11.63%)</td><td>22.53 <b>(-39.44%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.70 (n/a)</td><td>170.46 (n/a)</td><td>171.70 (n/a)</td><td>127.30 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 <b>(+31.47%)</b></td><td>0.03 <b>(+28.48%)</b></td><td>0.03 (+10.80%)</td><td>0.03 <b>(+111.29%)</b></td><td>0.01 (-18.00%)</td><td>198.80 <b>(-52.68%)</b></td><td>166.72 <b>(-28.43%)</b></td><td>167.80 (-9.78%)</td><td>131.80 <b>(-23.90%)</b></td><td>30.67 <b>(-70.99%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>420.10 (n/a)</td><td>232.96 (n/a)</td><td>186.00 (n/a)</td><td>173.20 (n/a)</td><td>105.74 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+7.07%)</td><td>0.03 (+6.91%)</td><td>0.03 (+1.83%)</td><td>0.02 (+18.10%)</td><td>0.01 (-2.94%)</td><td>203.90 (-15.32%)</td><td>161.40 (-7.74%)</td><td>158.10 (-1.80%)</td><td>120.10 (-6.61%)</td><td>37.87 <b>(-21.80%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>174.94 (n/a)</td><td>161.00 (n/a)</td><td>128.60 (n/a)</td><td>48.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (+9.66%)</td><td>0.03 (-14.01%)</td><td>0.03 (-8.88%)</td><td>0.02 <b>(-42.29%)</b></td><td>0.01 <b>(+144.30%)</b></td><td>299.90 <b>(+73.25%)</b></td><td>195.14 <b>(+25.17%)</b></td><td>179.60 (+9.71%)</td><td>123.20 (-8.81%)</td><td>65.49 <b>(+296.52%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>173.10 (n/a)</td><td>155.90 (n/a)</td><td>163.70 (n/a)</td><td>135.10 (n/a)</td><td>16.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 <b>(+32.49%)</b></td><td>0.03 (+19.84%)</td><td>0.03 (+19.77%)</td><td>0.02 (+10.10%)</td><td>0.00 <b>(+153.74%)</b></td><td>189.50 (-9.16%)</td><td>157.26 (-15.13%)</td><td>152.60 (-16.48%)</td><td>127.90 <b>(-24.50%)</b></td><td>25.89 <b>(+73.97%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.60 (n/a)</td><td>185.30 (n/a)</td><td>182.70 (n/a)</td><td>169.40 (n/a)</td><td>14.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (-9.95%)</td><td>0.03 (-0.03%)</td><td>0.03 (+12.34%)</td><td>0.02 (+1.45%)</td><td>0.01 <b>(-31.76%)</b></td><td>202.00 (-1.46%)</td><td>156.80 (-2.97%)</td><td>159.10 (-10.97%)</td><td>123.30 (+10.98%)</td><td>31.68 <b>(-25.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>161.60 (n/a)</td><td>178.70 (n/a)</td><td>111.10 (n/a)</td><td>42.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 <b>(+37.78%)</b></td><td>0.03 <b>(+33.22%)</b></td><td>0.03 <b>(+27.36%)</b></td><td>0.02 <b>(+32.42%)</b></td><td>0.00 <b>(+39.01%)</b></td><td>172.70 <b>(-24.49%)</b></td><td>138.04 <b>(-24.86%)</b></td><td>131.40 <b>(-21.51%)</b></td><td>120.00 <b>(-27.45%)</b></td><td>21.30 <b>(-22.45%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.70 (n/a)</td><td>183.70 (n/a)</td><td>167.40 (n/a)</td><td>165.40 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (+19.53%)</td><td>0.03 (-3.23%)</td><td>0.03 (-8.20%)</td><td>0.02 <b>(-27.39%)</b></td><td>0.01 <b>(+259.63%)</b></td><td>252.60 <b>(+37.73%)</b></td><td>179.44 (+7.89%)</td><td>177.30 (+8.91%)</td><td>129.90 (-16.36%)</td><td>45.35 <b>(+321.41%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>166.32 (n/a)</td><td>162.80 (n/a)</td><td>155.30 (n/a)</td><td>10.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+8.85%)</td><td>0.02 <b>(+27.51%)</b></td><td>0.02 <b>(+27.59%)</b></td><td>0.02 <b>(+48.89%)</b></td><td>0.00 <b>(-21.05%)</b></td><td>208.60 <b>(-32.84%)</b></td><td>172.02 <b>(-24.55%)</b></td><td>181.20 <b>(-21.63%)</b></td><td>128.20 (-8.10%)</td><td>30.48 <b>(-49.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>310.60 (n/a)</td><td>228.00 (n/a)</td><td>231.20 (n/a)</td><td>139.50 (n/a)</td><td>60.59 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+9.10%)</td><td>0.02 (-0.87%)</td><td>0.02 (-3.36%)</td><td>0.02 (+5.76%)</td><td>0.00 <b>(+24.93%)</b></td><td>222.60 (-5.44%)</td><td>191.96 (+1.48%)</td><td>194.90 (+3.45%)</td><td>150.40 (-8.35%)</td><td>31.16 (+9.82%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.40 (n/a)</td><td>189.16 (n/a)</td><td>188.40 (n/a)</td><td>164.10 (n/a)</td><td>28.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (+13.72%)</td><td>0.03 <b>(+28.29%)</b></td><td>0.02 <b>(+27.95%)</b></td><td>0.02 (+12.53%)</td><td>0.01 <b>(+24.36%)</b></td><td>216.90 (-11.14%)</td><td>166.08 <b>(-21.53%)</b></td><td>173.50 <b>(-21.85%)</b></td><td>127.50 (-12.07%)</td><td>37.57 (-3.15%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.10 (n/a)</td><td>211.66 (n/a)</td><td>222.00 (n/a)</td><td>145.00 (n/a)</td><td>38.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-8.99%)</td><td>0.02 (-6.81%)</td><td>0.02 (-10.43%)</td><td>0.02 (-1.63%)</td><td>0.00 <b>(-24.39%)</b></td><td>238.60 (+1.66%)</td><td>207.16 (+6.59%)</td><td>212.70 (+11.65%)</td><td>171.70 (+9.85%)</td><td>24.40 (-16.52%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.70 (n/a)</td><td>194.36 (n/a)</td><td>190.50 (n/a)</td><td>156.30 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (-12.23%)</td><td>0.02 (+6.36%)</td><td>0.02 (+17.09%)</td><td>0.01 (-3.93%)</td><td>0.01 (-12.85%)</td><td>375.30 (+4.11%)</td><td>222.82 (-5.97%)</td><td>196.90 (-14.61%)</td><td>158.60 (+13.94%)</td><td>87.49 (+10.36%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>360.50 (n/a)</td><td>236.96 (n/a)</td><td>230.60 (n/a)</td><td>139.20 (n/a)</td><td>79.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (+8.75%)</td><td>0.05 (+11.14%)</td><td>0.05 (+17.49%)</td><td>0.04 (+0.24%)</td><td>0.01 <b>(+41.28%)</b></td><td>196.00 (-0.25%)</td><td>156.68 (-8.56%)</td><td>150.10 (-14.86%)</td><td>124.30 (-8.06%)</td><td>34.04 <b>(+26.19%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>171.34 (n/a)</td><td>176.30 (n/a)</td><td>135.20 (n/a)</td><td>26.98 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 <b>(-42.42%)</b></td><td>0.07 <b>(-20.81%)</b></td><td>0.07 (-17.07%)</td><td>0.06 (-6.23%)</td><td>0.01 <b>(-77.35%)</b></td><td>206.20 (+6.67%)</td><td>177.54 (+18.82%)</td><td>169.50 <b>(+20.55%)</b></td><td>163.90 <b>(+73.81%)</b></td><td>16.95 <b>(-58.67%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>193.30 (n/a)</td><td>149.42 (n/a)</td><td>140.60 (n/a)</td><td>94.30 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 <b>(+34.97%)</b></td><td>0.05 <b>(+30.37%)</b></td><td>0.05 <b>(+23.75%)</b></td><td>0.04 <b>(+82.71%)</b></td><td>0.01 (+1.63%)</td><td>199.70 <b>(-45.26%)</b></td><td>157.34 <b>(-27.48%)</b></td><td>164.00 (-19.17%)</td><td>113.40 <b>(-25.88%)</b></td><td>35.72 <b>(-58.92%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.80 (n/a)</td><td>216.96 (n/a)</td><td>202.90 (n/a)</td><td>153.00 (n/a)</td><td>86.96 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (+3.93%)</td><td>0.06 (+2.09%)</td><td>0.06 (+4.01%)</td><td>0.04 (+6.28%)</td><td>0.02 <b>(+31.10%)</b></td><td>228.80 (-5.92%)</td><td>174.32 (-0.18%)</td><td>158.60 (-3.88%)</td><td>130.90 (-3.82%)</td><td>47.00 (+15.00%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>243.20 (n/a)</td><td>174.64 (n/a)</td><td>165.00 (n/a)</td><td>136.10 (n/a)</td><td>40.87 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (+2.22%)</td><td>0.05 (+5.53%)</td><td>0.05 (+7.71%)</td><td>0.05 (+17.75%)</td><td>0.01 <b>(-42.50%)</b></td><td>167.00 (-15.06%)</td><td>155.26 (-6.92%)</td><td>161.80 (-7.17%)</td><td>133.00 (-2.21%)</td><td>13.99 <b>(-51.30%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>166.80 (n/a)</td><td>174.30 (n/a)</td><td>136.00 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (-18.61%)</td><td>0.05 (-10.01%)</td><td>0.06 (+13.05%)</td><td>0.04 (-2.89%)</td><td>0.02 (-18.57%)</td><td>291.30 (+2.97%)</td><td>209.82 (+10.12%)</td><td>180.90 (-11.54%)</td><td>145.00 <b>(+22.88%)</b></td><td>71.50 (+8.62%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>282.90 (n/a)</td><td>190.54 (n/a)</td><td>204.50 (n/a)</td><td>118.00 (n/a)</td><td>65.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (+1.24%)</td><td>0.05 (+2.35%)</td><td>0.05 (+0.10%)</td><td>0.04 (+11.30%)</td><td>0.01 (-13.84%)</td><td>197.80 (-10.13%)</td><td>168.18 (-3.19%)</td><td>169.80 (-0.12%)</td><td>132.10 (-1.20%)</td><td>23.55 <b>(-25.61%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>173.72 (n/a)</td><td>170.00 (n/a)</td><td>133.70 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (+4.13%)</td><td>0.05 (+8.99%)</td><td>0.05 (+1.65%)</td><td>0.05 <b>(+57.54%)</b></td><td>0.01 <b>(-52.94%)</b></td><td>196.50 <b>(-36.53%)</b></td><td>170.72 (-13.23%)</td><td>172.00 (-1.66%)</td><td>149.10 (-3.99%)</td><td>18.00 <b>(-72.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.60 (n/a)</td><td>196.74 (n/a)</td><td>174.90 (n/a)</td><td>155.30 (n/a)</td><td>64.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (+4.24%)</td><td>0.05 (+18.49%)</td><td>0.05 <b>(+22.32%)</b></td><td>0.04 (+12.81%)</td><td>0.01 (-18.47%)</td><td>211.30 (-11.37%)</td><td>166.86 (-17.06%)</td><td>164.70 (-18.26%)</td><td>131.40 (-4.09%)</td><td>28.96 <b>(-30.09%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.40 (n/a)</td><td>201.18 (n/a)</td><td>201.50 (n/a)</td><td>137.00 (n/a)</td><td>41.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (-10.01%)</td><td>0.06 (-1.39%)</td><td>0.06 (+3.38%)</td><td>0.05 (+1.88%)</td><td>0.01 <b>(-28.50%)</b></td><td>195.00 (-1.81%)</td><td>156.62 (-0.17%)</td><td>154.70 (-3.25%)</td><td>122.90 (+11.12%)</td><td>25.81 <b>(-20.10%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>156.88 (n/a)</td><td>159.90 (n/a)</td><td>110.60 (n/a)</td><td>32.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (+13.56%)</td><td>0.05 (+4.43%)</td><td>0.05 (+13.56%)</td><td>0.03 <b>(-28.15%)</b></td><td>0.01 <b>(+218.98%)</b></td><td>292.30 <b>(+39.19%)</b></td><td>190.46 (+0.79%)</td><td>163.60 (-11.95%)</td><td>154.50 (-11.97%)</td><td>57.89 <b>(+303.78%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>188.96 (n/a)</td><td>185.80 (n/a)</td><td>175.50 (n/a)</td><td>14.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (-6.43%)</td><td>0.06 <b>(+45.90%)</b></td><td>0.05 <b>(+47.58%)</b></td><td>0.05 <b>(+128.15%)</b></td><td>0.00 <b>(-79.23%)</b></td><td>163.10 <b>(-56.18%)</b></td><td>154.64 <b>(-39.82%)</b></td><td>159.70 <b>(-32.22%)</b></td><td>141.50 (+6.87%)</td><td>9.29 <b>(-90.39%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>372.20 (n/a)</td><td>256.98 (n/a)</td><td>235.60 (n/a)</td><td>132.40 (n/a)</td><td>96.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 <b>(+40.30%)</b></td><td>0.05 <b>(+35.29%)</b></td><td>0.04 <b>(+22.97%)</b></td><td>0.04 <b>(+41.13%)</b></td><td>0.01 <b>(+23.80%)</b></td><td>225.30 <b>(-29.15%)</b></td><td>176.30 <b>(-26.88%)</b></td><td>186.40 (-18.67%)</td><td>130.10 <b>(-28.75%)</b></td><td>37.00 <b>(-37.58%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.00 (n/a)</td><td>241.10 (n/a)</td><td>229.20 (n/a)</td><td>182.60 (n/a)</td><td>59.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 <b>(+31.27%)</b></td><td>0.05 (+4.70%)</td><td>0.04 (-10.22%)</td><td>0.03 (+11.96%)</td><td>0.02 <b>(+56.98%)</b></td><td>258.40 (-10.71%)</td><td>202.06 (-1.91%)</td><td>206.00 (+11.41%)</td><td>118.70 <b>(-23.81%)</b></td><td>54.10 (+1.78%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.40 (n/a)</td><td>206.00 (n/a)</td><td>184.90 (n/a)</td><td>155.80 (n/a)</td><td>53.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 <b>(+20.40%)</b></td><td>0.04 <b>(+37.08%)</b></td><td>0.04 <b>(+26.27%)</b></td><td>0.04 <b>(+65.07%)</b></td><td>0.00 <b>(-55.07%)</b></td><td>216.70 <b>(-39.42%)</b></td><td>192.84 <b>(-29.46%)</b></td><td>188.50 <b>(-20.83%)</b></td><td>180.30 (-16.95%)</td><td>13.96 <b>(-77.15%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>357.70 (n/a)</td><td>273.36 (n/a)</td><td>238.10 (n/a)</td><td>217.10 (n/a)</td><td>61.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 <b>(+37.00%)</b></td><td>0.09 (+8.53%)</td><td>0.09 (-1.44%)</td><td>0.07 (-1.93%)</td><td>0.02 <b>(+183.40%)</b></td><td>224.10 (+1.96%)</td><td>184.06 (-4.71%)</td><td>187.50 (+1.46%)</td><td>127.40 <b>(-27.03%)</b></td><td>38.71 <b>(+109.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>193.16 (n/a)</td><td>184.80 (n/a)</td><td>174.60 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 <b>(+23.11%)</b></td><td>0.15 (+3.67%)</td><td>0.14 (-3.55%)</td><td>0.13 (-1.19%)</td><td>0.04 <b>(+120.32%)</b></td><td>187.30 (+1.24%)</td><td>167.16 (-1.04%)</td><td>179.20 (+3.64%)</td><td>114.40 (-18.75%)</td><td>30.24 <b>(+81.84%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>185.00 (n/a)</td><td>168.92 (n/a)</td><td>172.90 (n/a)</td><td>140.80 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (-8.31%)</td><td>0.11 (-5.32%)</td><td>0.12 (+11.29%)</td><td>0.07 <b>(-23.24%)</b></td><td>0.03 <b>(+39.58%)</b></td><td>225.20 <b>(+30.32%)</b></td><td>165.00 (+9.93%)</td><td>141.80 (-10.14%)</td><td>124.50 (+9.11%)</td><td>47.65 <b>(+97.15%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>172.80 (n/a)</td><td>150.10 (n/a)</td><td>157.80 (n/a)</td><td>114.10 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (-7.34%)</td><td>0.12 (-19.32%)</td><td>0.11 <b>(-23.26%)</b></td><td>0.10 <b>(-27.02%)</b></td><td>0.02 <b>(+38.80%)</b></td><td>210.30 <b>(+37.00%)</b></td><td>175.06 <b>(+25.53%)</b></td><td>180.10 <b>(+30.32%)</b></td><td>136.20 (+7.84%)</td><td>26.80 <b>(+101.50%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>153.50 (n/a)</td><td>139.46 (n/a)</td><td>138.20 (n/a)</td><td>126.30 (n/a)</td><td>13.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (+4.91%)</td><td>0.11 (+19.45%)</td><td>0.10 <b>(+25.99%)</b></td><td>0.08 (-1.13%)</td><td>0.03 (+8.67%)</td><td>212.90 (+1.14%)</td><td>154.26 (-15.89%)</td><td>158.40 <b>(-20.60%)</b></td><td>116.40 (-4.67%)</td><td>38.38 (+3.79%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.50 (n/a)</td><td>183.40 (n/a)</td><td>199.50 (n/a)</td><td>122.10 (n/a)</td><td>36.98 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (-2.60%)</td><td>0.11 (-2.12%)</td><td>0.13 (+1.50%)</td><td>0.06 <b>(-34.19%)</b></td><td>0.03 <b>(+30.74%)</b></td><td>366.60 <b>(+51.93%)</b></td><td>202.36 (+9.67%)</td><td>163.70 (-1.44%)</td><td>147.80 (+2.71%)</td><td>92.76 <b>(+111.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>241.30 (n/a)</td><td>184.52 (n/a)</td><td>166.10 (n/a)</td><td>143.90 (n/a)</td><td>43.84 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (-1.69%)</td><td>0.09 (+8.15%)</td><td>0.10 (+17.93%)</td><td>0.08 <b>(+20.60%)</b></td><td>0.01 <b>(-32.87%)</b></td><td>210.90 (-17.10%)</td><td>176.10 (-9.59%)</td><td>170.00 (-15.21%)</td><td>148.10 (+1.72%)</td><td>24.05 <b>(-42.55%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>254.40 (n/a)</td><td>194.78 (n/a)</td><td>200.50 (n/a)</td><td>145.60 (n/a)</td><td>41.86 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 <b>(+42.58%)</b></td><td>0.12 <b>(+45.56%)</b></td><td>0.13 <b>(+52.33%)</b></td><td>0.09 <b>(+26.04%)</b></td><td>0.02 <b>(+114.83%)</b></td><td>199.50 <b>(-20.68%)</b></td><td>152.30 <b>(-30.39%)</b></td><td>138.80 <b>(-34.34%)</b></td><td>135.20 <b>(-29.84%)</b></td><td>27.14 (+19.71%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>251.50 (n/a)</td><td>218.80 (n/a)</td><td>211.40 (n/a)</td><td>192.70 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 <b>(+37.35%)</b></td><td>0.12 <b>(+34.97%)</b></td><td>0.12 <b>(+43.25%)</b></td><td>0.08 (-4.56%)</td><td>0.02 <b>(+279.34%)</b></td><td>216.00 (+4.75%)</td><td>148.00 <b>(-23.16%)</b></td><td>132.50 <b>(-30.19%)</b></td><td>127.30 <b>(-27.22%)</b></td><td>38.08 <b>(+193.61%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>192.60 (n/a)</td><td>189.80 (n/a)</td><td>174.90 (n/a)</td><td>12.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (+19.02%)</td><td>0.12 <b>(+23.02%)</b></td><td>0.12 <b>(+30.46%)</b></td><td>0.10 <b>(+22.50%)</b></td><td>0.01 (+7.64%)</td><td>180.00 (-18.37%)</td><td>157.54 (-18.94%)</td><td>154.00 <b>(-23.38%)</b></td><td>134.80 (-15.96%)</td><td>18.99 <b>(-25.63%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>194.36 (n/a)</td><td>201.00 (n/a)</td><td>160.40 (n/a)</td><td>25.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (-12.90%)</td><td>0.10 (-4.83%)</td><td>0.10 (+3.17%)</td><td>0.08 (-4.42%)</td><td>0.01 <b>(-32.75%)</b></td><td>215.70 (+4.61%)</td><td>173.68 (+3.49%)</td><td>172.30 (-3.09%)</td><td>139.80 (+14.87%)</td><td>27.35 (-17.55%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>167.82 (n/a)</td><td>177.80 (n/a)</td><td>121.70 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (-3.32%)</td><td>0.09 (+13.74%)</td><td>0.10 (+17.25%)</td><td>0.07 <b>(+23.08%)</b></td><td>0.01 <b>(-24.44%)</b></td><td>249.20 (-18.75%)</td><td>188.98 (-14.05%)</td><td>174.80 (-14.69%)</td><td>163.90 (+3.41%)</td><td>34.63 <b>(-36.20%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>306.70 (n/a)</td><td>219.86 (n/a)</td><td>204.90 (n/a)</td><td>158.50 (n/a)</td><td>54.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (+13.59%)</td><td>0.09 (+6.26%)</td><td>0.09 (-5.33%)</td><td>0.08 <b>(+48.02%)</b></td><td>0.02 <b>(-26.37%)</b></td><td>207.70 <b>(-32.43%)</b></td><td>178.80 (-9.78%)</td><td>178.80 (+5.61%)</td><td>137.80 (-11.95%)</td><td>26.46 <b>(-57.96%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>307.40 (n/a)</td><td>198.18 (n/a)</td><td>169.30 (n/a)</td><td>156.50 (n/a)</td><td>62.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (+5.08%)</td><td>0.09 (-2.04%)</td><td>0.09 (-3.07%)</td><td>0.08 (-3.92%)</td><td>0.01 <b>(+32.76%)</b></td><td>228.10 (+4.11%)</td><td>194.52 (+2.92%)</td><td>194.40 (+3.18%)</td><td>151.20 (-4.85%)</td><td>29.10 <b>(+30.26%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>189.00 (n/a)</td><td>188.40 (n/a)</td><td>158.90 (n/a)</td><td>22.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (-2.98%)</td><td>0.08 (+9.95%)</td><td>0.08 (+14.76%)</td><td>0.07 (+10.47%)</td><td>0.01 <b>(-29.84%)</b></td><td>230.40 (-9.47%)</td><td>197.08 (-9.81%)</td><td>194.10 (-12.88%)</td><td>180.50 (+3.08%)</td><td>19.97 <b>(-33.18%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>254.50 (n/a)</td><td>218.52 (n/a)</td><td>222.80 (n/a)</td><td>175.10 (n/a)</td><td>29.89 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (+7.41%)</td><td>0.20 (+9.02%)</td><td>0.20 (+9.22%)</td><td>0.15 (-11.69%)</td><td>0.04 <b>(+45.94%)</b></td><td>222.90 (+13.20%)</td><td>165.38 (-6.63%)</td><td>161.60 (-8.44%)</td><td>131.70 (-6.86%)</td><td>35.35 <b>(+55.78%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.90 (n/a)</td><td>177.12 (n/a)</td><td>176.50 (n/a)</td><td>141.40 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (+10.33%)</td><td>0.20 (-5.27%)</td><td>0.19 (-11.13%)</td><td>0.14 (-18.67%)</td><td>0.04 <b>(+89.61%)</b></td><td>232.30 <b>(+22.98%)</b></td><td>173.34 (+8.31%)</td><td>171.80 (+12.51%)</td><td>131.20 (-9.33%)</td><td>37.20 <b>(+112.43%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.90 (n/a)</td><td>160.04 (n/a)</td><td>152.70 (n/a)</td><td>144.70 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.29 (-0.66%)</td><td>0.25 (+6.41%)</td><td>0.26 (+17.72%)</td><td>0.17 (-7.38%)</td><td>0.04 <b>(+21.89%)</b></td><td>235.10 (+7.99%)</td><td>172.42 (-4.83%)</td><td>155.20 (-15.10%)</td><td>143.30 (+0.70%)</td><td>37.19 <b>(+37.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>217.70 (n/a)</td><td>181.18 (n/a)</td><td>182.80 (n/a)</td><td>142.30 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (+7.36%)</td><td>0.21 (+11.57%)</td><td>0.20 (+5.13%)</td><td>0.19 <b>(+29.51%)</b></td><td>0.03 <b>(-28.95%)</b></td><td>176.20 <b>(-22.79%)</b></td><td>159.38 (-12.29%)</td><td>160.70 (-4.85%)</td><td>129.50 (-6.83%)</td><td>18.57 <b>(-50.42%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.20 (n/a)</td><td>181.72 (n/a)</td><td>168.90 (n/a)</td><td>139.00 (n/a)</td><td>37.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.29 (+1.32%)</td><td>0.28 <b>(+23.94%)</b></td><td>0.28 <b>(+34.44%)</b></td><td>0.24 <b>(+27.78%)</b></td><td>0.02 <b>(-47.17%)</b></td><td>168.50 <b>(-21.77%)</b></td><td>148.30 <b>(-20.59%)</b></td><td>143.80 <b>(-25.65%)</b></td><td>139.40 (-1.27%)</td><td>11.78 <b>(-57.36%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>215.40 (n/a)</td><td>186.76 (n/a)</td><td>193.40 (n/a)</td><td>141.20 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (+16.37%)</td><td>0.16 (-10.78%)</td><td>0.17 (-3.47%)</td><td>0.09 <b>(-34.46%)</b></td><td>0.07 <b>(+146.26%)</b></td><td>371.70 <b>(+52.59%)</b></td><td>247.70 <b>(+29.20%)</b></td><td>192.60 (+3.60%)</td><td>133.20 (-14.12%)</td><td>111.40 <b>(+247.14%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>243.60 (n/a)</td><td>191.72 (n/a)</td><td>185.90 (n/a)</td><td>155.10 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.32 <b>(+23.95%)</b></td><td>0.24 (+9.29%)</td><td>0.24 (+4.05%)</td><td>0.18 (-2.62%)</td><td>0.05 <b>(+60.22%)</b></td><td>208.70 (+2.71%)</td><td>158.04 (-6.81%)</td><td>153.40 (-3.94%)</td><td>114.30 (-19.34%)</td><td>33.71 <b>(+30.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>203.20 (n/a)</td><td>169.58 (n/a)</td><td>159.70 (n/a)</td><td>141.70 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (+14.26%)</td><td>0.21 (+11.33%)</td><td>0.20 (+5.71%)</td><td>0.19 <b>(+27.83%)</b></td><td>0.03 (-8.36%)</td><td>173.10 <b>(-21.78%)</b></td><td>155.70 (-11.01%)</td><td>163.00 (-5.40%)</td><td>126.40 (-12.47%)</td><td>18.08 <b>(-38.95%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.30 (n/a)</td><td>174.96 (n/a)</td><td>172.30 (n/a)</td><td>144.40 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (-15.72%)</td><td>0.21 (+5.13%)</td><td>0.22 (+11.21%)</td><td>0.17 (+16.87%)</td><td>0.03 <b>(-42.34%)</b></td><td>222.10 (-14.45%)</td><td>179.60 (-7.71%)</td><td>169.90 (-10.06%)</td><td>156.50 (+18.65%)</td><td>27.22 <b>(-40.41%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>259.60 (n/a)</td><td>194.60 (n/a)</td><td>188.90 (n/a)</td><td>131.90 (n/a)</td><td>45.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (+14.67%)</td><td>0.18 (+7.24%)</td><td>0.18 (+7.17%)</td><td>0.15 <b>(+24.08%)</b></td><td>0.03 (-9.27%)</td><td>219.80 (-19.43%)</td><td>183.18 (-8.12%)</td><td>181.60 (-6.68%)</td><td>142.70 (-12.78%)</td><td>28.18 <b>(-36.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>272.80 (n/a)</td><td>199.36 (n/a)</td><td>194.60 (n/a)</td><td>163.60 (n/a)</td><td>44.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (-0.81%)</td><td>0.19 (-8.07%)</td><td>0.21 (+11.93%)</td><td>0.10 <b>(-33.61%)</b></td><td>0.07 (+14.81%)</td><td>360.80 <b>(+50.65%)</b></td><td>213.12 (+16.04%)</td><td>164.70 (-10.68%)</td><td>130.50 (+0.77%)</td><td>94.06 <b>(+80.13%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>239.50 (n/a)</td><td>183.66 (n/a)</td><td>184.40 (n/a)</td><td>129.50 (n/a)</td><td>52.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (+11.15%)</td><td>0.21 (+15.88%)</td><td>0.24 <b>(+34.60%)</b></td><td>0.16 (+0.06%)</td><td>0.05 <b>(+71.94%)</b></td><td>210.50 (-0.09%)</td><td>161.04 (-11.24%)</td><td>139.40 <b>(-25.69%)</b></td><td>128.40 (-10.08%)</td><td>39.38 <b>(+57.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.70 (n/a)</td><td>181.44 (n/a)</td><td>187.60 (n/a)</td><td>142.80 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (-0.45%)</td><td>0.19 <b>(+40.77%)</b></td><td>0.20 <b>(+74.44%)</b></td><td>0.16 <b>(+44.34%)</b></td><td>0.02 <b>(-47.59%)</b></td><td>223.80 <b>(-30.71%)</b></td><td>183.84 <b>(-32.34%)</b></td><td>171.00 <b>(-42.68%)</b></td><td>166.30 (+0.42%)</td><td>24.05 <b>(-62.83%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>323.00 (n/a)</td><td>271.72 (n/a)</td><td>298.30 (n/a)</td><td>165.60 (n/a)</td><td>64.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 <b>(+20.91%)</b></td><td>0.16 (+9.13%)</td><td>0.16 (+7.49%)</td><td>0.11 (-6.77%)</td><td>0.04 <b>(+95.54%)</b></td><td>298.40 (+7.26%)</td><td>216.56 (-4.72%)</td><td>209.20 (-6.94%)</td><td>155.10 (-17.28%)</td><td>58.12 <b>(+71.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>278.20 (n/a)</td><td>227.28 (n/a)</td><td>224.80 (n/a)</td><td>187.50 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (-18.95%)</td><td>0.11 (-11.97%)</td><td>0.11 (-6.02%)</td><td>0.10 (-10.42%)</td><td>0.01 <b>(-38.47%)</b></td><td>206.50 (+11.62%)</td><td>183.72 (+12.57%)</td><td>188.40 (+6.38%)</td><td>161.10 <b>(+23.35%)</b></td><td>19.93 (-16.59%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>185.00 (n/a)</td><td>163.20 (n/a)</td><td>177.10 (n/a)</td><td>130.60 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (+8.11%)</td><td>0.13 (+8.77%)</td><td>0.13 (-3.68%)</td><td>0.11 <b>(+23.96%)</b></td><td>0.02 <b>(-27.37%)</b></td><td>185.30 (-19.33%)</td><td>157.16 (-10.24%)</td><td>153.80 (+3.85%)</td><td>132.70 (-7.53%)</td><td>22.52 <b>(-44.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>229.70 (n/a)</td><td>175.08 (n/a)</td><td>148.10 (n/a)</td><td>143.50 (n/a)</td><td>40.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (-3.66%)</td><td>0.13 (+6.60%)</td><td>0.14 (+17.43%)</td><td>0.11 (+7.28%)</td><td>0.01 <b>(-37.17%)</b></td><td>183.60 (-6.75%)</td><td>156.30 (-7.41%)</td><td>148.30 (-14.82%)</td><td>144.00 (+3.82%)</td><td>16.66 <b>(-38.71%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>196.90 (n/a)</td><td>168.80 (n/a)</td><td>174.10 (n/a)</td><td>138.70 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 <b>(+43.33%)</b></td><td>0.13 (+19.20%)</td><td>0.13 <b>(+20.07%)</b></td><td>0.08 (-11.44%)</td><td>0.04 <b>(+135.35%)</b></td><td>266.20 (+12.89%)</td><td>168.76 (-10.87%)</td><td>158.80 (-16.68%)</td><td>112.20 <b>(-30.22%)</b></td><td>57.92 <b>(+95.24%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>235.80 (n/a)</td><td>189.34 (n/a)</td><td>190.60 (n/a)</td><td>160.80 (n/a)</td><td>29.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (+4.78%)</td><td>0.13 (+4.36%)</td><td>0.12 (-0.83%)</td><td>0.11 (+17.45%)</td><td>0.02 (-14.98%)</td><td>190.10 (-14.87%)</td><td>161.10 (-5.28%)</td><td>164.20 (+0.80%)</td><td>130.30 (-4.54%)</td><td>21.95 <b>(-33.26%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>223.30 (n/a)</td><td>170.08 (n/a)</td><td>162.90 (n/a)</td><td>136.50 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (+19.92%)</td><td>0.13 (+13.59%)</td><td>0.12 (+8.21%)</td><td>0.11 <b>(+27.54%)</b></td><td>0.02 (-0.60%)</td><td>188.20 <b>(-21.62%)</b></td><td>165.76 (-12.59%)</td><td>170.00 (-7.56%)</td><td>135.20 (-16.59%)</td><td>20.09 <b>(-36.02%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>240.10 (n/a)</td><td>189.64 (n/a)</td><td>183.90 (n/a)</td><td>162.10 (n/a)</td><td>31.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (-7.41%)</td><td>0.11 (-13.02%)</td><td>0.12 (-7.95%)</td><td>0.06 <b>(-41.60%)</b></td><td>0.04 <b>(+69.73%)</b></td><td>331.60 <b>(+71.28%)</b></td><td>203.00 <b>(+24.60%)</b></td><td>174.10 (+8.61%)</td><td>139.10 (+8.00%)</td><td>79.11 <b>(+212.70%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>193.60 (n/a)</td><td>162.92 (n/a)</td><td>160.30 (n/a)</td><td>128.80 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (+2.79%)</td><td>0.10 (-6.34%)</td><td>0.11 (-1.44%)</td><td>0.08 (-19.27%)</td><td>0.02 <b>(+99.69%)</b></td><td>259.80 <b>(+23.83%)</b></td><td>204.64 (+10.10%)</td><td>184.20 (+1.49%)</td><td>162.10 (-2.76%)</td><td>46.25 <b>(+144.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>185.86 (n/a)</td><td>181.50 (n/a)</td><td>166.70 (n/a)</td><td>18.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (-6.85%)</td><td>0.15 (-4.30%)</td><td>0.17 (+10.92%)</td><td>0.11 (-8.06%)</td><td>0.04 (+13.13%)</td><td>231.40 (+8.74%)</td><td>169.90 (+6.13%)</td><td>143.30 (-9.87%)</td><td>132.10 (+7.40%)</td><td>43.72 <b>(+30.17%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>212.80 (n/a)</td><td>160.08 (n/a)</td><td>159.00 (n/a)</td><td>123.00 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 <b>(+22.89%)</b></td><td>0.14 (+9.20%)</td><td>0.12 (-1.39%)</td><td>0.11 <b>(+39.29%)</b></td><td>0.03 (+3.99%)</td><td>221.70 <b>(-28.21%)</b></td><td>187.88 (-10.11%)</td><td>202.20 (+1.40%)</td><td>135.60 (-18.61%)</td><td>35.07 <b>(-40.00%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>308.80 (n/a)</td><td>209.00 (n/a)</td><td>199.40 (n/a)</td><td>166.60 (n/a)</td><td>58.44 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (+7.54%)</td><td>0.15 <b>(+21.83%)</b></td><td>0.15 (+9.95%)</td><td>0.13 <b>(+91.57%)</b></td><td>0.02 <b>(-48.07%)</b></td><td>183.00 <b>(-47.80%)</b></td><td>162.92 <b>(-23.96%)</b></td><td>168.70 (-9.06%)</td><td>133.30 (-7.04%)</td><td>18.46 <b>(-76.86%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>350.60 (n/a)</td><td>214.26 (n/a)</td><td>185.50 (n/a)</td><td>143.40 (n/a)</td><td>79.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (-14.83%)</td><td>0.12 (-14.66%)</td><td>0.13 <b>(-20.31%)</b></td><td>0.09 (-14.27%)</td><td>0.02 <b>(-25.48%)</b></td><td>280.10 (+16.61%)</td><td>204.82 (+15.98%)</td><td>192.00 <b>(+25.49%)</b></td><td>163.60 (+17.44%)</td><td>46.21 (+4.38%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>240.20 (n/a)</td><td>176.60 (n/a)</td><td>153.00 (n/a)</td><td>139.30 (n/a)</td><td>44.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (-7.61%)</td><td>0.15 (+2.91%)</td><td>0.15 (-0.98%)</td><td>0.11 <b>(+39.31%)</b></td><td>0.03 <b>(-34.23%)</b></td><td>214.60 <b>(-28.23%)</b></td><td>168.02 (-8.35%)</td><td>165.80 (+0.97%)</td><td>132.00 (+8.29%)</td><td>32.62 <b>(-52.00%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>299.00 (n/a)</td><td>183.32 (n/a)</td><td>164.20 (n/a)</td><td>121.90 (n/a)</td><td>67.96 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 <b>(+20.20%)</b></td><td>0.15 (+10.94%)</td><td>0.15 (+10.74%)</td><td>0.09 (+1.10%)</td><td>0.03 <b>(+39.57%)</b></td><td>274.40 (-1.08%)</td><td>178.32 (-7.85%)</td><td>159.20 (-9.70%)</td><td>136.90 (-16.83%)</td><td>55.21 (+16.85%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>277.40 (n/a)</td><td>193.52 (n/a)</td><td>176.30 (n/a)</td><td>164.60 (n/a)</td><td>47.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (-10.57%)</td><td>0.13 (-12.04%)</td><td>0.13 (-16.43%)</td><td>0.12 (+8.75%)</td><td>0.01 <b>(-45.16%)</b></td><td>206.50 (-8.06%)</td><td>186.52 (+11.45%)</td><td>188.60 (+19.67%)</td><td>156.70 (+11.77%)</td><td>18.74 <b>(-45.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>224.60 (n/a)</td><td>167.36 (n/a)</td><td>157.60 (n/a)</td><td>140.20 (n/a)</td><td>34.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (+2.10%)</td><td>0.14 (-9.93%)</td><td>0.12 (-18.17%)</td><td>0.10 (-11.26%)</td><td>0.04 <b>(+35.87%)</b></td><td>253.70 (+12.66%)</td><td>190.84 (+13.92%)</td><td>198.50 <b>(+22.15%)</b></td><td>135.10 (-2.03%)</td><td>48.78 <b>(+42.79%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>225.20 (n/a)</td><td>167.52 (n/a)</td><td>162.50 (n/a)</td><td>137.90 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (-16.11%)</td><td>0.12 (-3.57%)</td><td>0.11 (-10.02%)</td><td>0.10 (+2.69%)</td><td>0.02 <b>(-36.47%)</b></td><td>175.60 (-2.61%)</td><td>153.16 (+1.84%)</td><td>162.40 (+11.16%)</td><td>129.80 (+19.19%)</td><td>20.90 <b>(-28.98%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>180.30 (n/a)</td><td>150.40 (n/a)</td><td>146.10 (n/a)</td><td>108.90 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (-2.83%)</td><td>0.11 (-10.82%)</td><td>0.11 (-12.11%)</td><td>0.09 <b>(-23.83%)</b></td><td>0.02 <b>(+115.87%)</b></td><td>212.10 <b>(+31.25%)</b></td><td>168.58 (+14.99%)</td><td>164.00 (+13.73%)</td><td>135.40 (+2.89%)</td><td>33.15 <b>(+186.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>161.60 (n/a)</td><td>146.60 (n/a)</td><td>144.20 (n/a)</td><td>131.60 (n/a)</td><td>11.57 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 <b>(+35.73%)</b></td><td>0.11 (+4.31%)</td><td>0.11 (+6.88%)</td><td>0.07 <b>(-27.37%)</b></td><td>0.03 <b>(+278.91%)</b></td><td>260.40 <b>(+37.70%)</b></td><td>181.26 (+2.00%)</td><td>171.50 (-6.44%)</td><td>115.70 <b>(-26.31%)</b></td><td>52.02 <b>(+279.06%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>177.70 (n/a)</td><td>183.30 (n/a)</td><td>157.00 (n/a)</td><td>13.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (-4.96%)</td><td>0.10 (+2.00%)</td><td>0.10 (+8.51%)</td><td>0.08 (-15.82%)</td><td>0.02 (+8.28%)</td><td>236.30 (+18.74%)</td><td>181.20 (-1.21%)</td><td>176.20 (-7.85%)</td><td>150.40 (+5.17%)</td><td>32.69 <b>(+42.74%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>199.00 (n/a)</td><td>183.42 (n/a)</td><td>191.20 (n/a)</td><td>143.00 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (-19.51%)</td><td>0.11 (-0.25%)</td><td>0.12 (+18.81%)</td><td>0.08 <b>(+29.40%)</b></td><td>0.02 <b>(-49.66%)</b></td><td>231.60 <b>(-22.72%)</b></td><td>176.26 (-6.59%)</td><td>158.80 (-15.85%)</td><td>150.50 <b>(+24.17%)</b></td><td>33.49 <b>(-51.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>299.70 (n/a)</td><td>188.70 (n/a)</td><td>188.70 (n/a)</td><td>121.20 (n/a)</td><td>69.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (+0.93%)</td><td>0.10 (+10.18%)</td><td>0.11 (+12.08%)</td><td>0.08 <b>(+27.27%)</b></td><td>0.02 (-13.64%)</td><td>227.20 <b>(-21.44%)</b></td><td>184.26 (-10.81%)</td><td>169.40 (-10.80%)</td><td>155.00 (-0.90%)</td><td>32.47 <b>(-35.21%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>289.20 (n/a)</td><td>206.60 (n/a)</td><td>189.90 (n/a)</td><td>156.40 (n/a)</td><td>50.11 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (-8.86%)</td><td>0.11 (-10.13%)</td><td>0.11 (-8.80%)</td><td>0.09 (-12.46%)</td><td>0.01 (-15.26%)</td><td>195.40 (+14.20%)</td><td>167.06 (+11.12%)</td><td>171.70 (+9.64%)</td><td>139.60 (+9.75%)</td><td>20.81 (+6.33%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>171.10 (n/a)</td><td>150.34 (n/a)</td><td>156.60 (n/a)</td><td>127.20 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (+4.33%)</td><td>0.11 (+8.49%)</td><td>0.11 (+8.61%)</td><td>0.09 (+18.46%)</td><td>0.01 <b>(-37.35%)</b></td><td>201.50 (-15.58%)</td><td>169.60 (-9.74%)</td><td>165.60 (-7.90%)</td><td>146.50 (-4.12%)</td><td>20.00 <b>(-47.32%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>238.70 (n/a)</td><td>187.90 (n/a)</td><td>179.80 (n/a)</td><td>152.80 (n/a)</td><td>37.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.78 (+16.81%)</td><td>0.59 (+8.60%)</td><td>0.61 (+12.15%)</td><td>0.40 (-1.19%)</td><td>0.14 <b>(+51.10%)</b></td><td>244.50 (+1.20%)</td><td>175.86 (-5.65%)</td><td>162.40 (-10.87%)</td><td>126.20 (-14.38%)</td><td>45.43 <b>(+30.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.67 (n/a)</td><td>0.54 (n/a)</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.09 (n/a)</td><td>241.60 (n/a)</td><td>186.40 (n/a)</td><td>182.20 (n/a)</td><td>147.40 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.77 (+8.79%)</td><td>0.59 (+8.53%)</td><td>0.58 (+6.04%)</td><td>0.46 <b>(+22.17%)</b></td><td>0.12 (-19.35%)</td><td>214.00 (-18.13%)</td><td>170.30 (-10.48%)</td><td>170.60 (-5.69%)</td><td>128.20 (-8.03%)</td><td>32.00 <b>(-38.55%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.71 (n/a)</td><td>0.55 (n/a)</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.14 (n/a)</td><td>261.40 (n/a)</td><td>190.24 (n/a)</td><td>180.90 (n/a)</td><td>139.40 (n/a)</td><td>52.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.60 (-17.30%)</td><td>0.56 (+0.03%)</td><td>0.56 (-0.85%)</td><td>0.47 <b>(+31.16%)</b></td><td>0.05 <b>(-59.35%)</b></td><td>211.00 <b>(-23.74%)</b></td><td>178.28 (-4.55%)</td><td>175.70 (+0.86%)</td><td>163.20 <b>(+20.98%)</b></td><td>19.23 <b>(-63.91%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.73 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.36 (n/a)</td><td>0.13 (n/a)</td><td>276.70 (n/a)</td><td>186.78 (n/a)</td><td>174.20 (n/a)</td><td>134.90 (n/a)</td><td>53.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.70 (+1.80%)</td><td>0.53 (-4.14%)</td><td>0.49 (-11.06%)</td><td>0.40 (+6.39%)</td><td>0.12 (-6.89%)</td><td>246.10 (-6.00%)</td><td>194.44 (+3.36%)</td><td>199.60 (+12.45%)</td><td>140.60 (-1.75%)</td><td>41.79 (-13.79%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.69 (n/a)</td><td>0.55 (n/a)</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.13 (n/a)</td><td>261.80 (n/a)</td><td>188.12 (n/a)</td><td>177.50 (n/a)</td><td>143.10 (n/a)</td><td>48.48 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.56 (+4.28%)</td><td>0.48 (+1.91%)</td><td>0.49 (-2.32%)</td><td>0.41 (+9.88%)</td><td>0.06 <b>(-20.40%)</b></td><td>179.90 (-9.00%)</td><td>156.74 (-2.88%)</td><td>151.90 (+2.43%)</td><td>131.90 (-4.14%)</td><td>20.19 <b>(-28.66%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>197.70 (n/a)</td><td>161.38 (n/a)</td><td>148.30 (n/a)</td><td>137.60 (n/a)</td><td>28.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.56 (+8.18%)</td><td>0.43 (-10.17%)</td><td>0.41 (-11.94%)</td><td>0.32 <b>(-23.28%)</b></td><td>0.09 <b>(+109.85%)</b></td><td>229.20 <b>(+30.38%)</b></td><td>177.46 (+14.36%)</td><td>177.90 (+13.60%)</td><td>130.50 (-7.58%)</td><td>35.77 <b>(+153.81%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.52 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.04 (n/a)</td><td>175.80 (n/a)</td><td>155.18 (n/a)</td><td>156.60 (n/a)</td><td>141.20 (n/a)</td><td>14.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.53 (-1.43%)</td><td>0.42 <b>(+25.57%)</b></td><td>0.41 <b>(+34.09%)</b></td><td>0.32 <b>(+63.02%)</b></td><td>0.09 <b>(-31.45%)</b></td><td>234.00 <b>(-38.66%)</b></td><td>181.40 <b>(-27.22%)</b></td><td>180.40 <b>(-25.42%)</b></td><td>140.40 (+1.45%)</td><td>40.63 <b>(-58.34%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.53 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>381.50 (n/a)</td><td>249.24 (n/a)</td><td>241.90 (n/a)</td><td>138.40 (n/a)</td><td>97.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.55 <b>(+20.64%)</b></td><td>0.46 (+14.33%)</td><td>0.45 <b>(+21.17%)</b></td><td>0.40 (+15.85%)</td><td>0.06 (+7.61%)</td><td>186.10 (-13.68%)</td><td>163.60 (-12.74%)</td><td>163.50 (-17.47%)</td><td>134.10 (-17.07%)</td><td>19.02 <b>(-22.18%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.46 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>215.60 (n/a)</td><td>187.48 (n/a)</td><td>198.10 (n/a)</td><td>161.70 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 <b>(+29.53%)</b></td><td>0.21 (+9.67%)</td><td>0.19 (-1.78%)</td><td>0.17 (-0.50%)</td><td>0.04 <b>(+223.39%)</b></td><td>211.10 (+0.52%)</td><td>179.96 (-6.26%)</td><td>194.80 (+1.83%)</td><td>136.60 <b>(-22.78%)</b></td><td>34.08 <b>(+153.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>191.98 (n/a)</td><td>191.30 (n/a)</td><td>176.90 (n/a)</td><td>13.44 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (+4.23%)</td><td>0.21 (+18.93%)</td><td>0.21 (+14.78%)</td><td>0.17 <b>(+64.41%)</b></td><td>0.03 <b>(-45.35%)</b></td><td>215.30 <b>(-39.18%)</b></td><td>179.02 <b>(-20.75%)</b></td><td>176.60 (-12.88%)</td><td>151.60 (-4.05%)</td><td>23.08 <b>(-69.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>354.00 (n/a)</td><td>225.90 (n/a)</td><td>202.70 (n/a)</td><td>158.00 (n/a)</td><td>75.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (+5.64%)</td><td>0.20 (-9.11%)</td><td>0.20 (-12.84%)</td><td>0.16 (-12.71%)</td><td>0.05 <b>(+30.53%)</b></td><td>226.70 (+14.55%)</td><td>188.76 (+11.71%)</td><td>184.70 (+14.72%)</td><td>132.40 (-5.29%)</td><td>36.87 <b>(+35.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>197.90 (n/a)</td><td>168.98 (n/a)</td><td>161.00 (n/a)</td><td>139.80 (n/a)</td><td>27.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (-6.13%)</td><td>0.20 (-4.72%)</td><td>0.19 (-11.50%)</td><td>0.17 (+3.65%)</td><td>0.03 (-15.84%)</td><td>212.90 (-3.53%)</td><td>184.06 (+4.32%)</td><td>189.10 (+13.03%)</td><td>151.60 (+6.54%)</td><td>25.35 (-14.71%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>220.70 (n/a)</td><td>176.44 (n/a)</td><td>167.30 (n/a)</td><td>142.30 (n/a)</td><td>29.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (+5.22%)</td><td>0.23 (+0.35%)</td><td>0.22 (+4.39%)</td><td>0.19 (-5.62%)</td><td>0.03 (+18.86%)</td><td>190.60 (+5.95%)</td><td>165.28 (-0.04%)</td><td>165.40 (-4.23%)</td><td>136.00 (-4.96%)</td><td>19.50 (+16.51%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>179.90 (n/a)</td><td>165.34 (n/a)</td><td>172.70 (n/a)</td><td>143.10 (n/a)</td><td>16.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (+10.55%)</td><td>0.23 (-1.44%)</td><td>0.24 (+5.66%)</td><td>0.16 <b>(-22.95%)</b></td><td>0.05 <b>(+146.77%)</b></td><td>227.50 <b>(+29.78%)</b></td><td>169.82 (+4.65%)</td><td>154.10 (-5.34%)</td><td>131.30 (-9.51%)</td><td>37.49 <b>(+191.90%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>175.30 (n/a)</td><td>162.28 (n/a)</td><td>162.80 (n/a)</td><td>145.10 (n/a)</td><td>12.84 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (-18.67%)</td><td>0.21 (-0.74%)</td><td>0.23 <b>(+21.31%)</b></td><td>0.15 (+17.91%)</td><td>0.03 <b>(-47.69%)</b></td><td>244.30 (-15.20%)</td><td>181.88 (-4.93%)</td><td>163.10 (-17.54%)</td><td>157.00 <b>(+22.94%)</b></td><td>36.28 <b>(-43.17%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>288.10 (n/a)</td><td>191.32 (n/a)</td><td>197.80 (n/a)</td><td>127.70 (n/a)</td><td>63.84 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-9.40%)</td><td>0.21 (-2.86%)</td><td>0.23 (+10.34%)</td><td>0.15 (+6.78%)</td><td>0.05 (-18.38%)</td><td>245.00 (-6.35%)</td><td>187.66 (+1.18%)</td><td>162.60 (-9.36%)</td><td>148.40 (+10.42%)</td><td>46.95 (-12.58%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>261.60 (n/a)</td><td>185.48 (n/a)</td><td>179.40 (n/a)</td><td>134.40 (n/a)</td><td>53.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.32 <b>(+22.00%)</b></td><td>0.25 (+14.24%)</td><td>0.25 (+6.56%)</td><td>0.14 (+11.02%)</td><td>0.06 (+19.17%)</td><td>286.90 (-9.92%)</td><td>179.42 (-11.95%)</td><td>162.80 (-6.17%)</td><td>128.00 (-18.05%)</td><td>62.03 (-7.65%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>318.50 (n/a)</td><td>203.76 (n/a)</td><td>173.50 (n/a)</td><td>156.20 (n/a)</td><td>67.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.35 <b>(+41.08%)</b></td><td>0.24 (+9.21%)</td><td>0.22 (-4.62%)</td><td>0.21 (+7.47%)</td><td>0.06 <b>(+129.88%)</b></td><td>199.30 (-6.96%)</td><td>176.86 (-5.96%)</td><td>189.30 (+4.82%)</td><td>117.90 <b>(-29.15%)</b></td><td>33.58 <b>(+46.91%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>214.20 (n/a)</td><td>188.06 (n/a)</td><td>180.60 (n/a)</td><td>166.40 (n/a)</td><td>22.86 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-9.62%)</td><td>0.22 (-5.22%)</td><td>0.21 (+0.10%)</td><td>0.19 (-7.95%)</td><td>0.02 (-19.12%)</td><td>212.80 (+8.63%)</td><td>190.58 (+5.25%)</td><td>191.20 (-0.10%)</td><td>164.90 (+10.60%)</td><td>19.44 (-2.85%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>195.90 (n/a)</td><td>181.08 (n/a)</td><td>191.40 (n/a)</td><td>149.10 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (-17.88%)</td><td>0.19 <b>(-26.21%)</b></td><td>0.18 <b>(-26.42%)</b></td><td>0.15 <b>(-31.33%)</b></td><td>0.04 (+3.81%)</td><td>276.80 <b>(+45.61%)</b></td><td>227.50 <b>(+37.26%)</b></td><td>228.40 <b>(+35.87%)</b></td><td>168.80 <b>(+21.79%)</b></td><td>40.58 <b>(+80.40%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>190.10 (n/a)</td><td>165.74 (n/a)</td><td>168.10 (n/a)</td><td>138.60 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.33 (+14.81%)</td><td>0.27 (+14.86%)</td><td>0.25 (+10.88%)</td><td>0.25 <b>(+24.01%)</b></td><td>0.03 (-10.87%)</td><td>164.30 (-19.34%)</td><td>152.94 (-13.70%)</td><td>161.80 (-9.81%)</td><td>124.80 (-12.91%)</td><td>16.62 <b>(-38.81%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>203.70 (n/a)</td><td>177.22 (n/a)</td><td>179.40 (n/a)</td><td>143.30 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.30 (+9.96%)</td><td>0.27 <b>(+21.18%)</b></td><td>0.27 <b>(+20.61%)</b></td><td>0.25 <b>(+59.82%)</b></td><td>0.02 <b>(-58.42%)</b></td><td>160.70 <b>(-37.42%)</b></td><td>150.90 <b>(-20.27%)</b></td><td>149.80 (-17.10%)</td><td>135.30 (-9.07%)</td><td>10.37 <b>(-76.10%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>256.80 (n/a)</td><td>189.26 (n/a)</td><td>180.70 (n/a)</td><td>148.80 (n/a)</td><td>43.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (-9.28%)</td><td>0.22 (-2.78%)</td><td>0.23 (+9.94%)</td><td>0.17 (+3.17%)</td><td>0.03 <b>(-42.60%)</b></td><td>235.20 (-3.09%)</td><td>186.38 (+0.02%)</td><td>181.00 (-9.05%)</td><td>156.30 (+10.23%)</td><td>29.26 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>242.70 (n/a)</td><td>186.34 (n/a)</td><td>199.00 (n/a)</td><td>141.80 (n/a)</td><td>43.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.36 <b>(+21.78%)</b></td><td>0.25 (+10.28%)</td><td>0.23 (+2.04%)</td><td>0.20 (+7.70%)</td><td>0.06 <b>(+53.72%)</b></td><td>208.00 (-7.14%)</td><td>169.92 (-7.72%)</td><td>179.20 (-1.97%)</td><td>114.80 (-17.88%)</td><td>34.55 (+14.83%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>224.00 (n/a)</td><td>184.14 (n/a)</td><td>182.80 (n/a)</td><td>139.80 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (+13.70%)</td><td>0.23 (+16.28%)</td><td>0.23 (+11.00%)</td><td>0.19 <b>(+20.13%)</b></td><td>0.03 (-7.40%)</td><td>183.90 (-16.75%)</td><td>156.72 (-14.73%)</td><td>153.30 (-9.93%)</td><td>135.50 (-12.07%)</td><td>20.85 <b>(-33.50%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>220.90 (n/a)</td><td>183.80 (n/a)</td><td>170.20 (n/a)</td><td>154.10 (n/a)</td><td>31.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (-8.73%)</td><td>0.20 (+2.95%)</td><td>0.19 (+9.27%)</td><td>0.15 (-6.36%)</td><td>0.04 (-16.88%)</td><td>236.50 (+6.82%)</td><td>178.54 (-3.51%)</td><td>178.80 (-8.50%)</td><td>131.30 (+9.60%)</td><td>39.43 (+3.00%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>221.40 (n/a)</td><td>185.04 (n/a)</td><td>195.40 (n/a)</td><td>119.80 (n/a)</td><td>38.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (+12.04%)</td><td>0.22 (+6.71%)</td><td>0.21 (+6.67%)</td><td>0.19 (+4.27%)</td><td>0.04 <b>(+27.81%)</b></td><td>181.20 (-4.08%)</td><td>158.56 (-5.72%)</td><td>168.90 (-6.27%)</td><td>123.60 (-10.76%)</td><td>24.76 (+9.81%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>188.90 (n/a)</td><td>168.18 (n/a)</td><td>180.20 (n/a)</td><td>138.50 (n/a)</td><td>22.55 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (+7.29%)</td><td>0.19 (-13.30%)</td><td>0.19 (-17.99%)</td><td>0.15 <b>(-22.21%)</b></td><td>0.04 <b>(+123.53%)</b></td><td>225.20 <b>(+28.54%)</b></td><td>188.12 (+18.60%)</td><td>183.50 <b>(+21.93%)</b></td><td>137.50 (-6.78%)</td><td>36.93 <b>(+175.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>175.20 (n/a)</td><td>158.62 (n/a)</td><td>150.50 (n/a)</td><td>147.50 (n/a)</td><td>13.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-1.08%)</td><td>0.22 (+8.83%)</td><td>0.22 (-2.22%)</td><td>0.18 <b>(+55.09%)</b></td><td>0.03 <b>(-44.36%)</b></td><td>194.30 <b>(-35.51%)</b></td><td>163.74 (-13.99%)</td><td>159.00 (+2.25%)</td><td>138.60 (+1.09%)</td><td>24.48 <b>(-64.02%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>301.30 (n/a)</td><td>190.38 (n/a)</td><td>155.50 (n/a)</td><td>137.10 (n/a)</td><td>68.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (+7.98%)</td><td>0.24 (+18.89%)</td><td>0.24 (+18.12%)</td><td>0.21 <b>(+32.40%)</b></td><td>0.02 <b>(-31.58%)</b></td><td>164.90 <b>(-24.46%)</b></td><td>147.78 (-17.26%)</td><td>142.10 (-15.37%)</td><td>132.10 (-7.43%)</td><td>15.02 <b>(-52.14%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>218.30 (n/a)</td><td>178.60 (n/a)</td><td>167.90 (n/a)</td><td>142.70 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.22 (-12.02%)</td><td>0.19 (-8.02%)</td><td>0.18 (-8.15%)</td><td>0.13 (-16.13%)</td><td>0.04 (+6.26%)</td><td>265.30 (+19.24%)</td><td>194.46 (+9.95%)</td><td>192.70 (+8.87%)</td><td>160.40 (+13.68%)</td><td>42.79 <b>(+42.27%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>222.50 (n/a)</td><td>176.86 (n/a)</td><td>177.00 (n/a)</td><td>141.10 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (-4.48%)</td><td>0.21 (+3.02%)</td><td>0.22 <b>(+22.40%)</b></td><td>0.15 (-1.03%)</td><td>0.04 (-14.98%)</td><td>225.30 (+1.03%)</td><td>175.48 (-4.01%)</td><td>159.60 (-18.28%)</td><td>137.10 (+4.74%)</td><td>38.94 (-10.17%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>223.00 (n/a)</td><td>182.82 (n/a)</td><td>195.30 (n/a)</td><td>130.90 (n/a)</td><td>43.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.06 <b>(+22.69%)</b></td><td>0.94 <b>(+30.77%)</b></td><td>0.95 <b>(+37.38%)</b></td><td>0.83 <b>(+35.65%)</b></td><td>0.09 (-6.73%)</td><td>158.30 <b>(-26.27%)</b></td><td>140.62 <b>(-24.04%)</b></td><td>137.80 <b>(-27.21%)</b></td><td>123.30 (-18.45%)</td><td>13.90 <b>(-43.33%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.87 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.61 (n/a)</td><td>0.10 (n/a)</td><td>214.70 (n/a)</td><td>185.12 (n/a)</td><td>189.30 (n/a)</td><td>151.20 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.01 (+5.82%)</td><td>0.92 (+15.20%)</td><td>0.95 (+19.72%)</td><td>0.74 (+8.80%)</td><td>0.11 (+11.45%)</td><td>178.20 (-8.10%)</td><td>144.42 (-13.09%)</td><td>138.70 (-16.45%)</td><td>129.30 (-5.55%)</td><td>20.12 (-1.78%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.96 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.68 (n/a)</td><td>0.10 (n/a)</td><td>193.90 (n/a)</td><td>166.18 (n/a)</td><td>166.00 (n/a)</td><td>136.90 (n/a)</td><td>20.48 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.06 (-2.32%)</td><td>0.89 (+18.16%)</td><td>0.87 <b>(+41.78%)</b></td><td>0.75 <b>(+39.85%)</b></td><td>0.14 <b>(-42.30%)</b></td><td>174.90 <b>(-28.50%)</b></td><td>150.18 (-19.90%)</td><td>151.30 <b>(-29.46%)</b></td><td>124.00 (+2.31%)</td><td>22.84 <b>(-57.10%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>1.08 (n/a)</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.54 (n/a)</td><td>0.24 (n/a)</td><td>244.60 (n/a)</td><td>187.48 (n/a)</td><td>214.50 (n/a)</td><td>121.20 (n/a)</td><td>53.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.00 (+0.00%)</td><td>0.00 (+7.55%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+22.22%)</b></td><td>0.00 <b>(-51.96%)</b></td><td>3600.17 <b>(-24.42%)</b></td><td>3562.57 (-10.55%)</td><td>3580.29 (-5.00%)</td><td>3510.17 (+1.01%)</td><td>40.17 <b>(-92.18%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4763.13 (n/a)</td><td>3982.62 (n/a)</td><td>3768.70 (n/a)</td><td>3474.95 (n/a)</td><td>513.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.00 (+0.00%)</td><td>0.00 (-1.82%)</td><td>0.00 (-4.35%)</td><td>0.00 (+0.00%)</td><td>0.00 (-7.26%)</td><td>4655.18 (+1.61%)</td><td>3821.51 (+1.64%)</td><td>3655.29 (+2.84%)</td><td>3568.53 (+0.50%)</td><td>468.04 (+1.92%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4581.45 (n/a)</td><td>3760.00 (n/a)</td><td>3554.23 (n/a)</td><td>3550.89 (n/a)</td><td>459.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (+0.98%)</td><td>0.23 (+9.37%)</td><td>0.28 (+14.77%)</td><td>0.15 (-0.60%)</td><td>0.06 (+9.33%)</td><td>14070.88 (+0.55%)</td><td>9712.30 (-8.17%)</td><td>7580.60 (-12.89%)</td><td>7558.09 (-0.95%)</td><td>3045.16 (-2.10%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>13993.22 (n/a)</td><td>10576.83 (n/a)</td><td>8702.74 (n/a)</td><td>7630.90 (n/a)</td><td>3110.55 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.28 (+14.65%)</td><td>5.17 (+7.81%)</td><td>5.01 (+6.20%)</td><td>3.91 (-7.10%)</td><td>1.06 <b>(+123.51%)</b></td><td>268.10 (+7.63%)</td><td>209.90 (-4.72%)</td><td>209.10 (-5.85%)</td><td>167.00 (-12.75%)</td><td>43.70 <b>(+103.52%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>5.48 (n/a)</td><td>4.80 (n/a)</td><td>4.72 (n/a)</td><td>4.21 (n/a)</td><td>0.47 (n/a)</td><td>249.10 (n/a)</td><td>220.30 (n/a)</td><td>222.10 (n/a)</td><td>191.40 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.44 <b>(+26.36%)</b></td><td>5.85 <b>(+25.57%)</b></td><td>5.89 <b>(+25.62%)</b></td><td>5.26 <b>(+20.65%)</b></td><td>0.42 <b>(+45.58%)</b></td><td>199.20 (-17.14%)</td><td>179.88 <b>(-20.28%)</b></td><td>178.10 <b>(-20.38%)</b></td><td>162.90 <b>(-20.88%)</b></td><td>13.08 (-4.54%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>5.09 (n/a)</td><td>4.66 (n/a)</td><td>4.69 (n/a)</td><td>4.36 (n/a)</td><td>0.29 (n/a)</td><td>240.40 (n/a)</td><td>225.64 (n/a)</td><td>223.70 (n/a)</td><td>205.90 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>5.74 (-0.25%)</td><td>4.96 (+8.10%)</td><td>5.14 (+18.24%)</td><td>3.47 (-15.44%)</td><td>0.89 <b>(+29.96%)</b></td><td>302.10 (+18.29%)</td><td>218.24 (-5.95%)</td><td>204.10 (-15.45%)</td><td>182.60 (+0.27%)</td><td>48.31 <b>(+59.96%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>5.76 (n/a)</td><td>4.59 (n/a)</td><td>4.34 (n/a)</td><td>4.11 (n/a)</td><td>0.69 (n/a)</td><td>255.40 (n/a)</td><td>232.04 (n/a)</td><td>241.40 (n/a)</td><td>182.10 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.20 (+13.65%)</td><td>5.19 (+9.20%)</td><td>5.18 (+13.18%)</td><td>4.08 (-5.95%)</td><td>0.76 <b>(+69.25%)</b></td><td>257.30 (+6.32%)</td><td>205.64 (-7.37%)</td><td>202.40 (-11.65%)</td><td>169.10 (-12.02%)</td><td>32.09 <b>(+62.71%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>5.46 (n/a)</td><td>4.76 (n/a)</td><td>4.58 (n/a)</td><td>4.33 (n/a)</td><td>0.45 (n/a)</td><td>242.00 (n/a)</td><td>222.00 (n/a)</td><td>229.10 (n/a)</td><td>192.20 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.14 (-1.75%)</td><td>8.59 (+4.77%)</td><td>8.60 (+7.12%)</td><td>8.26 (+11.26%)</td><td>0.36 <b>(-49.59%)</b></td><td>254.00 (-10.12%)</td><td>244.48 (-4.97%)</td><td>243.90 (-6.66%)</td><td>229.60 (+1.82%)</td><td>9.92 <b>(-53.43%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>9.30 (n/a)</td><td>8.20 (n/a)</td><td>8.03 (n/a)</td><td>7.42 (n/a)</td><td>0.71 (n/a)</td><td>282.60 (n/a)</td><td>257.26 (n/a)</td><td>261.30 (n/a)</td><td>225.50 (n/a)</td><td>21.31 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.28 (+8.39%)</td><td>8.08 (+2.29%)</td><td>7.87 (-1.00%)</td><td>7.20 (+3.65%)</td><td>0.80 <b>(+32.87%)</b></td><td>291.40 (-3.51%)</td><td>261.66 (-1.99%)</td><td>266.40 (+1.02%)</td><td>226.10 (-7.75%)</td><td>25.02 (+16.28%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>8.56 (n/a)</td><td>7.89 (n/a)</td><td>7.95 (n/a)</td><td>6.94 (n/a)</td><td>0.60 (n/a)</td><td>302.00 (n/a)</td><td>266.96 (n/a)</td><td>263.70 (n/a)</td><td>245.10 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>8.89 (-0.19%)</td><td>8.42 (+8.31%)</td><td>8.39 (+8.49%)</td><td>8.00 (+18.65%)</td><td>0.39 <b>(-51.02%)</b></td><td>262.20 (-15.69%)</td><td>249.54 (-8.28%)</td><td>250.10 (-7.81%)</td><td>235.90 (+0.21%)</td><td>11.59 <b>(-58.49%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>8.91 (n/a)</td><td>7.77 (n/a)</td><td>7.73 (n/a)</td><td>6.74 (n/a)</td><td>0.80 (n/a)</td><td>311.00 (n/a)</td><td>272.08 (n/a)</td><td>271.30 (n/a)</td><td>235.40 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.61 (+3.90%)</td><td>8.28 (+2.62%)</td><td>8.24 (+2.69%)</td><td>6.97 (-2.63%)</td><td>0.96 (+6.28%)</td><td>300.90 (+2.70%)</td><td>255.90 (-2.45%)</td><td>254.50 (-2.60%)</td><td>218.30 (-3.75%)</td><td>30.09 (+4.27%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>9.25 (n/a)</td><td>8.07 (n/a)</td><td>8.03 (n/a)</td><td>7.16 (n/a)</td><td>0.90 (n/a)</td><td>293.00 (n/a)</td><td>262.32 (n/a)</td><td>261.30 (n/a)</td><td>226.80 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.88 (-1.17%)</td><td>9.06 (+8.73%)</td><td>8.91 (+8.40%)</td><td>8.65 (+16.20%)</td><td>0.48 <b>(-51.13%)</b></td><td>242.50 (-13.95%)</td><td>232.04 (-8.77%)</td><td>235.40 (-7.76%)</td><td>212.20 (+1.14%)</td><td>11.75 <b>(-56.98%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>10.00 (n/a)</td><td>8.33 (n/a)</td><td>8.22 (n/a)</td><td>7.44 (n/a)</td><td>0.99 (n/a)</td><td>281.80 (n/a)</td><td>254.36 (n/a)</td><td>255.20 (n/a)</td><td>209.80 (n/a)</td><td>27.31 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.80 (-17.22%)</td><td>8.93 (+3.75%)</td><td>9.09 (+6.74%)</td><td>8.17 <b>(+45.23%)</b></td><td>0.65 <b>(-70.27%)</b></td><td>256.70 <b>(-31.14%)</b></td><td>235.80 (-8.46%)</td><td>230.70 (-6.30%)</td><td>214.00 <b>(+20.77%)</b></td><td>17.27 <b>(-75.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>11.84 (n/a)</td><td>8.61 (n/a)</td><td>8.52 (n/a)</td><td>5.63 (n/a)</td><td>2.20 (n/a)</td><td>372.80 (n/a)</td><td>257.60 (n/a)</td><td>246.20 (n/a)</td><td>177.20 (n/a)</td><td>71.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.20 (+1.75%)</td><td>11.24 (+1.23%)</td><td>11.18 (+0.67%)</td><td>10.28 (+1.12%)</td><td>0.83 (+11.42%)</td><td>407.80 (-1.12%)</td><td>374.74 (-1.14%)</td><td>375.30 (-0.66%)</td><td>343.80 (-1.72%)</td><td>27.49 (+7.97%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>11.99 (n/a)</td><td>11.10 (n/a)</td><td>11.10 (n/a)</td><td>10.17 (n/a)</td><td>0.74 (n/a)</td><td>412.40 (n/a)</td><td>379.08 (n/a)</td><td>377.80 (n/a)</td><td>349.80 (n/a)</td><td>25.46 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.15 (+11.79%)</td><td>11.91 (+5.33%)</td><td>12.47 (+11.05%)</td><td>10.16 (-6.33%)</td><td>1.20 <b>(+205.87%)</b></td><td>412.80 (+6.75%)</td><td>355.28 (-4.34%)</td><td>336.50 (-9.95%)</td><td>318.90 (-10.55%)</td><td>37.76 <b>(+194.51%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>11.77 (n/a)</td><td>11.31 (n/a)</td><td>11.22 (n/a)</td><td>10.85 (n/a)</td><td>0.39 (n/a)</td><td>386.70 (n/a)</td><td>371.38 (n/a)</td><td>373.70 (n/a)</td><td>356.50 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.54 (+6.97%)</td><td>11.85 (+5.08%)</td><td>11.65 (+2.20%)</td><td>11.34 (+6.39%)</td><td>0.50 (+4.63%)</td><td>369.80 (-6.00%)</td><td>354.42 (-4.84%)</td><td>360.20 (-2.15%)</td><td>334.60 (-6.51%)</td><td>14.71 (-7.88%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>11.72 (n/a)</td><td>11.28 (n/a)</td><td>11.39 (n/a)</td><td>10.66 (n/a)</td><td>0.48 (n/a)</td><td>393.40 (n/a)</td><td>372.44 (n/a)</td><td>368.10 (n/a)</td><td>357.90 (n/a)</td><td>15.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>15.34 (+4.19%)</td><td>13.49 (+2.99%)</td><td>12.94 (-5.24%)</td><td>11.83 (+4.52%)</td><td>1.56 (-5.59%)</td><td>354.50 (-4.32%)</td><td>314.26 (-3.16%)</td><td>324.10 (+5.50%)</td><td>273.40 (-4.04%)</td><td>35.56 (-15.70%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>14.72 (n/a)</td><td>13.10 (n/a)</td><td>13.66 (n/a)</td><td>11.32 (n/a)</td><td>1.65 (n/a)</td><td>370.50 (n/a)</td><td>324.52 (n/a)</td><td>307.20 (n/a)</td><td>284.90 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.98 (+14.89%)</td><td>13.40 (+9.56%)</td><td>13.50 (+10.24%)</td><td>12.29 (+11.39%)</td><td>1.14 <b>(+51.51%)</b></td><td>341.20 (-10.21%)</td><td>314.80 (-8.49%)</td><td>310.60 (-9.29%)</td><td>280.10 (-12.96%)</td><td>26.46 (+19.42%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>13.03 (n/a)</td><td>12.23 (n/a)</td><td>12.25 (n/a)</td><td>11.04 (n/a)</td><td>0.75 (n/a)</td><td>380.00 (n/a)</td><td>344.00 (n/a)</td><td>342.40 (n/a)</td><td>321.80 (n/a)</td><td>22.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.43 (+4.53%)</td><td>12.56 (-0.19%)</td><td>12.94 (+3.76%)</td><td>10.69 (-10.11%)</td><td>1.56 <b>(+115.56%)</b></td><td>392.20 (+11.26%)</td><td>338.28 (+1.21%)</td><td>324.10 (-3.63%)</td><td>290.70 (-4.31%)</td><td>42.90 <b>(+134.52%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>13.80 (n/a)</td><td>12.58 (n/a)</td><td>12.47 (n/a)</td><td>11.90 (n/a)</td><td>0.72 (n/a)</td><td>352.50 (n/a)</td><td>334.24 (n/a)</td><td>336.30 (n/a)</td><td>303.80 (n/a)</td><td>18.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.97 (-9.33%)</td><td>13.35 (+3.88%)</td><td>13.36 (+8.23%)</td><td>12.73 <b>(+24.87%)</b></td><td>0.48 <b>(-76.49%)</b></td><td>329.60 (-19.92%)</td><td>314.50 (-5.58%)</td><td>314.00 (-7.59%)</td><td>300.20 (+10.29%)</td><td>11.25 <b>(-79.11%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>15.41 (n/a)</td><td>12.85 (n/a)</td><td>12.34 (n/a)</td><td>10.19 (n/a)</td><td>2.02 (n/a)</td><td>411.60 (n/a)</td><td>333.10 (n/a)</td><td>339.80 (n/a)</td><td>272.20 (n/a)</td><td>53.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>19.19 <b>(+25.77%)</b></td><td>14.23 (+12.05%)</td><td>13.89 (+7.16%)</td><td>9.30 (-5.01%)</td><td>3.81 <b>(+94.70%)</b></td><td>451.10 (+5.27%)</td><td>313.40 (-7.00%)</td><td>302.00 (-6.67%)</td><td>218.60 <b>(-20.48%)</b></td><td>89.93 <b>(+59.87%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>15.26 (n/a)</td><td>12.70 (n/a)</td><td>12.96 (n/a)</td><td>9.79 (n/a)</td><td>1.95 (n/a)</td><td>428.50 (n/a)</td><td>337.00 (n/a)</td><td>323.60 (n/a)</td><td>274.90 (n/a)</td><td>56.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.18 (-1.24%)</td><td>2.72 (+0.10%)</td><td>2.98 (+15.50%)</td><td>1.49 <b>(-39.62%)</b></td><td>0.69 <b>(+124.66%)</b></td><td>351.70 <b>(+65.58%)</b></td><td>209.16 (+7.28%)</td><td>176.20 (-13.42%)</td><td>164.80 (+1.29%)</td><td>79.85 <b>(+294.67%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>3.22 (n/a)</td><td>2.71 (n/a)</td><td>2.58 (n/a)</td><td>2.47 (n/a)</td><td>0.31 (n/a)</td><td>212.40 (n/a)</td><td>194.96 (n/a)</td><td>203.50 (n/a)</td><td>162.70 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.02 (-18.36%)</td><td>2.87 (-12.59%)</td><td>3.01 (-3.37%)</td><td>2.40 (-20.00%)</td><td>0.27 (-18.61%)</td><td>218.10 <b>(+24.99%)</b></td><td>183.78 (+14.40%)</td><td>174.20 (+3.44%)</td><td>173.80 <b>(+22.48%)</b></td><td>19.30 <b>(+25.17%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>3.69 (n/a)</td><td>3.29 (n/a)</td><td>3.11 (n/a)</td><td>3.00 (n/a)</td><td>0.33 (n/a)</td><td>174.50 (n/a)</td><td>160.64 (n/a)</td><td>168.40 (n/a)</td><td>141.90 (n/a)</td><td>15.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.31 <b>(+47.14%)</b></td><td>0.22 (+15.91%)</td><td>0.22 (+12.79%)</td><td>0.16 (-9.01%)</td><td>0.06 <b>(+251.19%)</b></td><td>204.10 (+9.91%)</td><td>154.08 (-9.53%)</td><td>149.80 (-11.36%)</td><td>105.50 <b>(-32.02%)</b></td><td>38.97 <b>(+161.99%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.70 (n/a)</td><td>170.32 (n/a)</td><td>169.00 (n/a)</td><td>155.20 (n/a)</td><td>14.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 <b>(+41.81%)</b></td><td>0.21 (+15.11%)</td><td>0.21 (+15.74%)</td><td>0.16 (-7.15%)</td><td>0.04 <b>(+428.17%)</b></td><td>208.00 (+7.72%)</td><td>164.36 (-10.49%)</td><td>158.20 (-13.55%)</td><td>122.70 <b>(-29.48%)</b></td><td>32.08 <b>(+299.80%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>183.62 (n/a)</td><td>183.00 (n/a)</td><td>174.00 (n/a)</td><td>8.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.53 <b>(+23.93%)</b></td><td>0.44 <b>(+23.78%)</b></td><td>0.45 <b>(+36.37%)</b></td><td>0.32 (+6.37%)</td><td>0.08 <b>(+56.11%)</b></td><td>207.00 (-5.99%)</td><td>153.72 (-18.02%)</td><td>145.10 <b>(-26.68%)</b></td><td>124.40 (-19.33%)</td><td>32.52 <b>(+22.01%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>220.20 (n/a)</td><td>187.52 (n/a)</td><td>197.90 (n/a)</td><td>154.20 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.50 (-6.90%)</td><td>0.39 (-6.94%)</td><td>0.36 (-7.15%)</td><td>0.28 <b>(-24.89%)</b></td><td>0.09 <b>(+36.80%)</b></td><td>234.40 <b>(+33.11%)</b></td><td>174.30 (+10.34%)</td><td>180.00 (+7.72%)</td><td>131.90 (+7.41%)</td><td>41.01 <b>(+95.43%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.53 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.06 (n/a)</td><td>176.10 (n/a)</td><td>157.96 (n/a)</td><td>167.10 (n/a)</td><td>122.80 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.48 (+5.01%)</td><td>0.43 <b>(+23.13%)</b></td><td>0.42 (+17.74%)</td><td>0.38 <b>(+87.38%)</b></td><td>0.04 <b>(-59.29%)</b></td><td>172.90 <b>(-46.62%)</b></td><td>153.06 <b>(-24.18%)</b></td><td>154.60 (-15.05%)</td><td>136.70 (-4.74%)</td><td>13.69 <b>(-80.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>323.90 (n/a)</td><td>201.88 (n/a)</td><td>182.00 (n/a)</td><td>143.50 (n/a)</td><td>70.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.02 (+2.33%)</td><td>0.84 <b>(+29.35%)</b></td><td>0.85 <b>(+34.00%)</b></td><td>0.61 <b>(+68.48%)</b></td><td>0.16 <b>(-29.52%)</b></td><td>215.00 <b>(-40.66%)</b></td><td>160.22 <b>(-28.00%)</b></td><td>154.10 <b>(-25.38%)</b></td><td>128.90 (-2.27%)</td><td>33.91 <b>(-59.96%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.99 (n/a)</td><td>0.65 (n/a)</td><td>0.63 (n/a)</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>362.30 (n/a)</td><td>222.52 (n/a)</td><td>206.50 (n/a)</td><td>131.90 (n/a)</td><td>84.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.97 <b>(+24.11%)</b></td><td>0.76 (+12.47%)</td><td>0.74 (+1.51%)</td><td>0.62 (+12.26%)</td><td>0.13 <b>(+30.60%)</b></td><td>210.10 (-10.90%)</td><td>175.54 (-10.78%)</td><td>176.00 (-1.51%)</td><td>135.70 (-19.42%)</td><td>27.74 (-8.21%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.78 (n/a)</td><td>0.68 (n/a)</td><td>0.73 (n/a)</td><td>0.56 (n/a)</td><td>0.10 (n/a)</td><td>235.80 (n/a)</td><td>196.76 (n/a)</td><td>178.70 (n/a)</td><td>168.40 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.99 <b>(+20.66%)</b></td><td>0.82 (+15.20%)</td><td>0.80 (+9.46%)</td><td>0.69 (+10.04%)</td><td>0.12 <b>(+51.66%)</b></td><td>189.40 (-9.12%)</td><td>163.48 (-12.59%)</td><td>164.10 (-8.63%)</td><td>133.00 (-17.08%)</td><td>23.26 (+12.20%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.82 (n/a)</td><td>0.71 (n/a)</td><td>0.73 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>208.40 (n/a)</td><td>187.02 (n/a)</td><td>179.60 (n/a)</td><td>160.40 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.26 <b>(+56.37%)</b></td><td>0.91 <b>(+57.32%)</b></td><td>0.85 <b>(+54.68%)</b></td><td>0.64 <b>(+51.15%)</b></td><td>0.25 <b>(+53.09%)</b></td><td>206.30 <b>(-33.84%)</b></td><td>153.02 <b>(-36.62%)</b></td><td>153.60 <b>(-35.35%)</b></td><td>103.70 <b>(-36.07%)</b></td><td>41.10 <b>(-37.45%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.81 (n/a)</td><td>0.58 (n/a)</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.17 (n/a)</td><td>311.80 (n/a)</td><td>241.44 (n/a)</td><td>237.60 (n/a)</td><td>162.20 (n/a)</td><td>65.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (-18.39%)</td><td>0.10 (+4.45%)</td><td>0.11 (+16.64%)</td><td>0.09 <b>(+23.76%)</b></td><td>0.01 <b>(-52.91%)</b></td><td>184.10 (-19.22%)</td><td>159.14 (-8.22%)</td><td>153.70 (-14.28%)</td><td>135.30 <b>(+22.55%)</b></td><td>20.83 <b>(-50.40%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:34</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>227.90 (n/a)</td><td>173.40 (n/a)</td><td>179.30 (n/a)</td><td>110.40 (n/a)</td><td>42.00 (n/a)</td>
</tr>
</tbody>
</table>


</details>
