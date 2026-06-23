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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 <b>(+34.15%)</b></td><td>0.04 (+12.78%)</td><td>0.04 (-0.16%)</td><td>0.03 (-2.12%)</td><td>0.01 <b>(+121.72%)</b></td><td>210.40 (+2.14%)</td><td>164.38 (-8.82%)</td><td>170.10 (+0.12%)</td><td>118.00 <b>(-25.46%)</b></td><td>35.18 <b>(+64.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>180.28 (n/a)</td><td>169.90 (n/a)</td><td>158.30 (n/a)</td><td>21.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-7.81%)</td><td>0.04 (-2.83%)</td><td>0.04 (-1.17%)</td><td>0.04 (+3.12%)</td><td>0.00 <b>(-43.32%)</b></td><td>163.50 (-3.02%)</td><td>150.66 (+2.00%)</td><td>154.10 (+1.25%)</td><td>137.00 (+8.47%)</td><td>11.32 <b>(-39.95%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>168.60 (n/a)</td><td>147.70 (n/a)</td><td>152.20 (n/a)</td><td>126.30 (n/a)</td><td>18.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (-14.41%)</td><td>0.04 (+5.52%)</td><td>0.04 (-9.08%)</td><td>0.03 <b>(+74.12%)</b></td><td>0.01 <b>(-49.76%)</b></td><td>217.00 <b>(-42.56%)</b></td><td>169.84 (-19.88%)</td><td>170.80 (+9.98%)</td><td>130.80 (+16.79%)</td><td>36.64 <b>(-67.56%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>377.80 (n/a)</td><td>211.98 (n/a)</td><td>155.30 (n/a)</td><td>112.00 (n/a)</td><td>112.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-9.59%)</td><td>0.04 (-3.74%)</td><td>0.04 (-3.22%)</td><td>0.03 (-5.40%)</td><td>0.00 (-18.14%)</td><td>203.00 (+5.73%)</td><td>163.76 (+3.50%)</td><td>159.50 (+3.30%)</td><td>140.80 (+10.60%)</td><td>23.63 (-2.07%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>158.22 (n/a)</td><td>154.40 (n/a)</td><td>127.30 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (+9.26%)</td><td>0.03 (-13.95%)</td><td>0.03 <b>(-28.59%)</b></td><td>0.02 (-17.95%)</td><td>0.01 <b>(+49.40%)</b></td><td>295.60 <b>(+21.85%)</b></td><td>219.04 <b>(+21.04%)</b></td><td>229.40 <b>(+40.05%)</b></td><td>132.20 (-8.45%)</td><td>60.64 <b>(+57.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.60 (n/a)</td><td>180.96 (n/a)</td><td>163.80 (n/a)</td><td>144.40 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 <b>(+30.33%)</b></td><td>0.03 (+3.22%)</td><td>0.03 (-8.01%)</td><td>0.03 (+4.97%)</td><td>0.01 <b>(+74.73%)</b></td><td>230.50 (-4.71%)</td><td>186.34 (-1.29%)</td><td>190.00 (+8.70%)</td><td>133.10 <b>(-23.29%)</b></td><td>37.13 <b>(+24.76%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>241.90 (n/a)</td><td>188.78 (n/a)</td><td>174.80 (n/a)</td><td>173.50 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+2.94%)</td><td>0.03 (-8.73%)</td><td>0.03 <b>(-21.25%)</b></td><td>0.03 (-9.06%)</td><td>0.01 <b>(+94.40%)</b></td><td>228.80 (+10.00%)</td><td>201.04 (+11.45%)</td><td>221.20 <b>(+26.98%)</b></td><td>163.50 (-2.85%)</td><td>32.81 <b>(+104.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.00 (n/a)</td><td>180.38 (n/a)</td><td>174.20 (n/a)</td><td>168.30 (n/a)</td><td>16.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+0.66%)</td><td>0.03 (+0.18%)</td><td>0.03 (-0.82%)</td><td>0.03 (+7.16%)</td><td>0.01 <b>(-20.40%)</b></td><td>219.80 (-6.71%)</td><td>181.58 (-1.83%)</td><td>189.00 (+0.80%)</td><td>140.60 (-0.64%)</td><td>31.14 <b>(-24.95%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>184.96 (n/a)</td><td>187.50 (n/a)</td><td>141.50 (n/a)</td><td>41.50 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (+2.97%)</td><td>0.07 (-3.32%)</td><td>0.08 (-3.43%)</td><td>0.06 (-1.81%)</td><td>0.01 (+14.67%)</td><td>195.00 (+1.88%)</td><td>168.12 (+3.91%)</td><td>163.20 (+3.55%)</td><td>131.30 (-2.88%)</td><td>25.29 (+13.28%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>161.80 (n/a)</td><td>157.60 (n/a)</td><td>135.20 (n/a)</td><td>22.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (+4.47%)</td><td>0.08 (-7.40%)</td><td>0.07 <b>(-20.50%)</b></td><td>0.05 (-14.63%)</td><td>0.02 <b>(+51.73%)</b></td><td>234.00 (+17.12%)</td><td>172.34 (+12.98%)</td><td>185.30 <b>(+25.80%)</b></td><td>111.80 (-4.28%)</td><td>50.84 <b>(+64.67%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>152.54 (n/a)</td><td>147.30 (n/a)</td><td>116.80 (n/a)</td><td>30.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (-5.87%)</td><td>0.07 (-3.09%)</td><td>0.07 (-3.81%)</td><td>0.06 (+18.03%)</td><td>0.01 <b>(-39.91%)</b></td><td>197.30 (-15.29%)</td><td>171.60 (+0.46%)</td><td>175.00 (+3.98%)</td><td>140.00 (+6.22%)</td><td>21.25 <b>(-46.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>170.82 (n/a)</td><td>168.30 (n/a)</td><td>131.80 (n/a)</td><td>39.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (-2.52%)</td><td>0.08 (-3.91%)</td><td>0.07 (-4.65%)</td><td>0.07 (-5.00%)</td><td>0.01 (-7.00%)</td><td>184.50 (+5.25%)</td><td>164.62 (+3.99%)</td><td>164.10 (+4.86%)</td><td>141.60 (+2.61%)</td><td>16.10 (-1.96%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>175.30 (n/a)</td><td>158.30 (n/a)</td><td>156.50 (n/a)</td><td>138.00 (n/a)</td><td>16.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (+11.41%)</td><td>0.07 (-5.20%)</td><td>0.07 (-15.79%)</td><td>0.05 (-11.52%)</td><td>0.02 <b>(+28.96%)</b></td><td>242.60 (+12.99%)</td><td>183.64 (+7.71%)</td><td>183.70 (+18.75%)</td><td>116.80 (-10.22%)</td><td>46.78 <b>(+22.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>170.50 (n/a)</td><td>154.70 (n/a)</td><td>130.10 (n/a)</td><td>38.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 <b>(-21.66%)</b></td><td>0.06 (-11.89%)</td><td>0.06 (-14.48%)</td><td>0.05 (-9.07%)</td><td>0.01 <b>(-36.83%)</b></td><td>269.80 (+9.94%)</td><td>208.76 (+11.05%)</td><td>207.70 (+16.95%)</td><td>170.90 <b>(+27.63%)</b></td><td>39.62 (-13.69%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>245.40 (n/a)</td><td>187.98 (n/a)</td><td>177.60 (n/a)</td><td>133.90 (n/a)</td><td>45.90 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (+10.73%)</td><td>0.07 (+3.75%)</td><td>0.06 (-1.52%)</td><td>0.05 (-12.54%)</td><td>0.01 <b>(+71.61%)</b></td><td>227.30 (+14.34%)</td><td>184.06 (-1.53%)</td><td>197.50 (+1.54%)</td><td>136.60 (-9.66%)</td><td>35.61 <b>(+76.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>186.92 (n/a)</td><td>194.50 (n/a)</td><td>151.20 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (-12.27%)</td><td>0.06 (-8.10%)</td><td>0.06 (-13.74%)</td><td>0.05 (-5.48%)</td><td>0.01 <b>(-29.33%)</b></td><td>233.90 (+5.79%)</td><td>201.88 (+7.61%)</td><td>209.90 (+15.97%)</td><td>161.50 (+13.97%)</td><td>27.26 (-18.07%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>187.60 (n/a)</td><td>181.00 (n/a)</td><td>141.70 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (-14.71%)</td><td>0.16 (-4.29%)</td><td>0.18 (+13.57%)</td><td>0.13 (+8.61%)</td><td>0.03 <b>(-31.25%)</b></td><td>191.50 (-7.93%)</td><td>157.12 (+2.17%)</td><td>138.30 (-11.97%)</td><td>134.80 (+17.32%)</td><td>29.06 <b>(-23.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>208.00 (n/a)</td><td>153.78 (n/a)</td><td>157.10 (n/a)</td><td>114.90 (n/a)</td><td>38.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (+10.30%)</td><td>0.15 (-4.84%)</td><td>0.14 (-9.90%)</td><td>0.11 (-12.86%)</td><td>0.04 <b>(+47.24%)</b></td><td>229.00 (+14.79%)</td><td>172.94 (+8.45%)</td><td>170.40 (+11.01%)</td><td>109.80 (-9.41%)</td><td>43.98 <b>(+48.67%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>199.50 (n/a)</td><td>159.46 (n/a)</td><td>153.50 (n/a)</td><td>121.20 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (+5.16%)</td><td>0.16 (-5.70%)</td><td>0.15 <b>(-21.79%)</b></td><td>0.12 (-0.66%)</td><td>0.04 (+8.74%)</td><td>210.00 (+0.67%)</td><td>163.30 (+6.50%)</td><td>168.50 <b>(+27.85%)</b></td><td>120.40 (-4.97%)</td><td>36.33 (+3.72%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.60 (n/a)</td><td>153.34 (n/a)</td><td>131.80 (n/a)</td><td>126.70 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 <b>(+21.89%)</b></td><td>0.17 (+13.58%)</td><td>0.18 <b>(+20.04%)</b></td><td>0.12 (+7.96%)</td><td>0.04 <b>(+72.19%)</b></td><td>201.40 (-7.40%)</td><td>152.64 (-10.06%)</td><td>133.40 (-16.68%)</td><td>122.30 (-17.97%)</td><td>35.26 <b>(+27.44%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>169.72 (n/a)</td><td>160.10 (n/a)</td><td>149.10 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (+1.89%)</td><td>0.15 (-7.68%)</td><td>0.15 (-11.89%)</td><td>0.13 (-0.91%)</td><td>0.02 (+4.31%)</td><td>190.00 (+0.90%)</td><td>167.40 (+8.45%)</td><td>162.20 (+13.51%)</td><td>137.60 (-1.85%)</td><td>21.70 (+5.53%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>188.30 (n/a)</td><td>154.36 (n/a)</td><td>142.90 (n/a)</td><td>140.20 (n/a)</td><td>20.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 <b>(-22.65%)</b></td><td>0.14 <b>(-20.80%)</b></td><td>0.15 (-19.95%)</td><td>0.13 (-19.86%)</td><td>0.01 <b>(-28.37%)</b></td><td>189.80 <b>(+24.79%)</b></td><td>172.42 <b>(+26.15%)</b></td><td>167.40 <b>(+24.93%)</b></td><td>158.20 <b>(+29.25%)</b></td><td>13.22 (+15.82%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>152.10 (n/a)</td><td>136.68 (n/a)</td><td>134.00 (n/a)</td><td>122.40 (n/a)</td><td>11.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (-9.80%)</td><td>0.15 (-14.28%)</td><td>0.14 (-19.12%)</td><td>0.13 (-11.85%)</td><td>0.02 (+6.90%)</td><td>190.30 (+13.48%)</td><td>170.84 (+17.11%)</td><td>178.10 <b>(+23.59%)</b></td><td>140.40 (+10.81%)</td><td>21.16 <b>(+35.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>167.70 (n/a)</td><td>145.88 (n/a)</td><td>144.10 (n/a)</td><td>126.70 (n/a)</td><td>15.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (-0.22%)</td><td>0.14 (-12.84%)</td><td>0.14 (-19.01%)</td><td>0.11 (-13.96%)</td><td>0.03 <b>(+24.21%)</b></td><td>221.60 (+16.20%)</td><td>177.14 (+16.02%)</td><td>176.00 <b>(+23.51%)</b></td><td>133.00 (+0.23%)</td><td>31.83 <b>(+39.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.70 (n/a)</td><td>152.68 (n/a)</td><td>142.50 (n/a)</td><td>132.70 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 (+6.64%)</td><td>0.31 (-4.62%)</td><td>0.33 (+0.83%)</td><td>0.22 <b>(-27.93%)</b></td><td>0.06 <b>(+228.75%)</b></td><td>226.50 <b>(+38.70%)</b></td><td>162.96 (+8.58%)</td><td>148.80 (-0.80%)</td><td>132.40 (-6.17%)</td><td>38.31 <b>(+332.34%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.02 (n/a)</td><td>163.30 (n/a)</td><td>150.08 (n/a)</td><td>150.00 (n/a)</td><td>141.10 (n/a)</td><td>8.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.42 (+17.40%)</td><td>0.31 (-5.81%)</td><td>0.30 (-7.25%)</td><td>0.20 <b>(-31.44%)</b></td><td>0.08 <b>(+239.03%)</b></td><td>240.50 <b>(+45.85%)</b></td><td>169.00 (+12.47%)</td><td>165.70 (+7.81%)</td><td>117.90 (-14.81%)</td><td>48.14 <b>(+325.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.02 (n/a)</td><td>164.90 (n/a)</td><td>150.26 (n/a)</td><td>153.70 (n/a)</td><td>138.40 (n/a)</td><td>11.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.36 (+11.95%)</td><td>0.30 (+6.10%)</td><td>0.28 (-3.00%)</td><td>0.27 (+14.62%)</td><td>0.04 <b>(+23.87%)</b></td><td>182.50 (-12.76%)</td><td>165.70 (-5.58%)</td><td>176.90 (+3.09%)</td><td>137.90 (-10.63%)</td><td>19.26 (-5.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>209.20 (n/a)</td><td>175.50 (n/a)</td><td>171.60 (n/a)</td><td>154.30 (n/a)</td><td>20.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 <b>(+22.58%)</b></td><td>0.30 (+2.82%)</td><td>0.29 (+0.69%)</td><td>0.25 (-10.95%)</td><td>0.05 <b>(+382.98%)</b></td><td>198.70 (+12.32%)</td><td>167.24 (-1.02%)</td><td>168.60 (-0.71%)</td><td>132.60 (-18.40%)</td><td>24.80 <b>(+339.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.01 (n/a)</td><td>176.90 (n/a)</td><td>168.96 (n/a)</td><td>169.80 (n/a)</td><td>162.50 (n/a)</td><td>5.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.35 (-5.13%)</td><td>0.30 (-9.34%)</td><td>0.30 (-6.19%)</td><td>0.25 (-9.68%)</td><td>0.04 (+0.36%)</td><td>200.20 (+10.73%)</td><td>169.12 (+10.65%)</td><td>163.60 (+6.58%)</td><td>139.60 (+5.44%)</td><td>25.19 <b>(+21.14%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>180.80 (n/a)</td><td>152.84 (n/a)</td><td>153.50 (n/a)</td><td>132.40 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 (+5.38%)</td><td>0.29 (-1.01%)</td><td>0.31 (-0.40%)</td><td>0.23 (+11.52%)</td><td>0.06 (+8.80%)</td><td>213.60 (-10.33%)</td><td>174.34 (+1.02%)</td><td>159.00 (+0.38%)</td><td>131.70 (-5.12%)</td><td>35.32 (-8.00%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>238.20 (n/a)</td><td>172.58 (n/a)</td><td>158.40 (n/a)</td><td>138.80 (n/a)</td><td>38.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (-16.36%)</td><td>0.25 (-15.29%)</td><td>0.24 <b>(-21.31%)</b></td><td>0.22 (-11.24%)</td><td>0.04 (-16.99%)</td><td>225.60 (+12.63%)</td><td>197.32 (+17.87%)</td><td>205.70 <b>(+27.13%)</b></td><td>163.90 (+19.55%)</td><td>29.28 (+10.26%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>200.30 (n/a)</td><td>167.40 (n/a)</td><td>161.80 (n/a)</td><td>137.10 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (-11.00%)</td><td>0.22 <b>(-27.44%)</b></td><td>0.21 <b>(-31.43%)</b></td><td>0.16 <b>(-30.33%)</b></td><td>0.06 <b>(+21.29%)</b></td><td>315.90 <b>(+43.53%)</b></td><td>241.30 <b>(+42.58%)</b></td><td>231.90 <b>(+45.85%)</b></td><td>161.50 (+12.31%)</td><td>63.32 <b>(+100.18%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>220.10 (n/a)</td><td>169.24 (n/a)</td><td>159.00 (n/a)</td><td>143.80 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (+15.04%)</td><td>0.02 (+2.63%)</td><td>0.02 (+9.29%)</td><td>0.01 (-14.54%)</td><td>0.00 <b>(+149.68%)</b></td><td>178.80 (+17.02%)</td><td>141.02 (-0.06%)</td><td>129.00 (-8.51%)</td><td>110.30 (-13.08%)</td><td>27.93 <b>(+155.89%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>152.80 (n/a)</td><td>141.10 (n/a)</td><td>141.00 (n/a)</td><td>126.90 (n/a)</td><td>10.91 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (-13.32%)</td><td>0.02 (-15.14%)</td><td>0.02 (-9.77%)</td><td>0.01 <b>(-27.83%)</b></td><td>0.00 <b>(+36.22%)</b></td><td>215.70 <b>(+38.54%)</b></td><td>172.38 (+19.38%)</td><td>164.30 (+10.79%)</td><td>142.40 (+15.30%)</td><td>27.98 <b>(+124.75%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>155.70 (n/a)</td><td>144.40 (n/a)</td><td>148.30 (n/a)</td><td>123.50 (n/a)</td><td>12.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 <b>(-47.71%)</b></td><td>0.02 (-18.73%)</td><td>0.02 (+4.27%)</td><td>0.01 (-17.15%)</td><td>0.00 <b>(-70.97%)</b></td><td>209.10 <b>(+20.66%)</b></td><td>158.62 (+12.90%)</td><td>147.10 (-4.04%)</td><td>132.60 <b>(+91.34%)</b></td><td>30.02 <b>(-26.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>173.30 (n/a)</td><td>140.50 (n/a)</td><td>153.30 (n/a)</td><td>69.30 (n/a)</td><td>40.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (-14.95%)</td><td>0.01 (-11.69%)</td><td>0.01 (-2.59%)</td><td>0.01 (+11.76%)</td><td>0.00 <b>(-49.92%)</b></td><td>212.60 (-10.52%)</td><td>178.54 (+7.77%)</td><td>177.60 (+2.66%)</td><td>138.80 (+17.53%)</td><td>26.73 <b>(-45.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>237.60 (n/a)</td><td>165.66 (n/a)</td><td>173.00 (n/a)</td><td>118.10 (n/a)</td><td>49.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (-15.59%)</td><td>0.02 (-8.18%)</td><td>0.02 (-6.20%)</td><td>0.01 (-10.93%)</td><td>0.00 <b>(-28.78%)</b></td><td>198.30 (+12.29%)</td><td>173.56 (+8.61%)</td><td>172.30 (+6.56%)</td><td>160.40 (+18.46%)</td><td>15.20 (-4.11%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>176.60 (n/a)</td><td>159.80 (n/a)</td><td>161.70 (n/a)</td><td>135.40 (n/a)</td><td>15.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.01 <b>(-23.03%)</b></td><td>0.01 (-18.96%)</td><td>0.01 (-16.63%)</td><td>0.01 (-18.01%)</td><td>0.00 <b>(-44.20%)</b></td><td>209.00 <b>(+21.94%)</b></td><td>194.14 <b>(+23.11%)</b></td><td>192.10 (+19.91%)</td><td>181.40 <b>(+29.94%)</b></td><td>10.36 (-10.34%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.40 (n/a)</td><td>157.70 (n/a)</td><td>160.20 (n/a)</td><td>139.60 (n/a)</td><td>11.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (-12.99%)</td><td>0.02 (-10.88%)</td><td>0.01 (-11.90%)</td><td>0.01 (-13.31%)</td><td>0.00 (-8.65%)</td><td>185.60 (+15.35%)</td><td>174.00 (+12.24%)</td><td>179.90 (+13.50%)</td><td>157.90 (+14.92%)</td><td>12.12 <b>(+21.84%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>160.90 (n/a)</td><td>155.02 (n/a)</td><td>158.50 (n/a)</td><td>137.40 (n/a)</td><td>9.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.01 (-12.82%)</td><td>0.01 <b>(-20.08%)</b></td><td>0.01 (-16.99%)</td><td>0.01 <b>(-32.14%)</b></td><td>0.00 <b>(+47.40%)</b></td><td>313.60 <b>(+47.37%)</b></td><td>229.90 <b>(+27.91%)</b></td><td>212.10 <b>(+20.44%)</b></td><td>188.10 (+14.70%)</td><td>48.91 <b>(+154.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>212.80 (n/a)</td><td>179.74 (n/a)</td><td>176.10 (n/a)</td><td>164.00 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-5.60%)</td><td>0.03 (-14.43%)</td><td>0.03 <b>(-25.43%)</b></td><td>0.03 (+3.75%)</td><td>0.01 <b>(-30.68%)</b></td><td>202.50 (-3.62%)</td><td>175.48 (+14.39%)</td><td>174.50 <b>(+34.13%)</b></td><td>133.40 (+5.96%)</td><td>27.27 <b>(-27.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>153.40 (n/a)</td><td>130.10 (n/a)</td><td>125.90 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-3.99%)</td><td>0.03 (-12.18%)</td><td>0.03 (-13.45%)</td><td>0.02 (-7.61%)</td><td>0.01 (+0.83%)</td><td>211.00 (+8.26%)</td><td>176.42 (+14.34%)</td><td>170.80 (+15.48%)</td><td>134.50 (+4.18%)</td><td>31.80 (+16.97%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>154.30 (n/a)</td><td>147.90 (n/a)</td><td>129.10 (n/a)</td><td>27.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-15.42%)</td><td>0.03 (-13.81%)</td><td>0.03 (-16.18%)</td><td>0.03 (-1.99%)</td><td>0.00 <b>(-29.76%)</b></td><td>187.00 (+2.07%)</td><td>160.46 (+14.70%)</td><td>156.30 (+19.31%)</td><td>131.90 (+18.19%)</td><td>23.73 (-14.89%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>139.90 (n/a)</td><td>131.00 (n/a)</td><td>111.60 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+4.32%)</td><td>0.03 (+3.09%)</td><td>0.03 (-9.10%)</td><td>0.03 <b>(+22.11%)</b></td><td>0.01 (-12.84%)</td><td>185.30 (-18.08%)</td><td>159.04 (-4.40%)</td><td>169.00 (+10.03%)</td><td>122.70 (-4.14%)</td><td>24.09 <b>(-34.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>166.36 (n/a)</td><td>153.60 (n/a)</td><td>128.00 (n/a)</td><td>36.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-0.09%)</td><td>0.03 (-12.73%)</td><td>0.03 (-11.56%)</td><td>0.03 (-17.09%)</td><td>0.01 <b>(+61.80%)</b></td><td>206.80 <b>(+20.65%)</b></td><td>171.28 (+16.77%)</td><td>162.90 (+13.13%)</td><td>129.00 (+0.08%)</td><td>30.83 <b>(+94.71%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>171.40 (n/a)</td><td>146.68 (n/a)</td><td>144.00 (n/a)</td><td>128.90 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 <b>(+29.57%)</b></td><td>0.03 (+9.77%)</td><td>0.03 (+3.89%)</td><td>0.03 (+11.69%)</td><td>0.01 <b>(+85.39%)</b></td><td>184.00 (-10.51%)</td><td>160.24 (-7.88%)</td><td>163.20 (-3.77%)</td><td>122.80 <b>(-22.82%)</b></td><td>23.80 <b>(+25.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>173.94 (n/a)</td><td>169.60 (n/a)</td><td>159.10 (n/a)</td><td>18.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-16.85%)</td><td>0.03 (-10.29%)</td><td>0.03 (-8.69%)</td><td>0.03 (+1.28%)</td><td>0.00 <b>(-52.20%)</b></td><td>203.40 (-1.26%)</td><td>180.30 (+9.62%)</td><td>176.80 (+9.47%)</td><td>159.80 <b>(+20.24%)</b></td><td>16.14 <b>(-43.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>164.48 (n/a)</td><td>161.50 (n/a)</td><td>132.90 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 <b>(+25.10%)</b></td><td>0.03 (+9.71%)</td><td>0.03 (+5.28%)</td><td>0.02 (+11.32%)</td><td>0.01 <b>(+62.40%)</b></td><td>214.20 (-10.19%)</td><td>183.96 (-7.80%)</td><td>191.80 (-5.00%)</td><td>140.60 <b>(-20.07%)</b></td><td>30.29 (+18.39%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>199.52 (n/a)</td><td>201.90 (n/a)</td><td>175.90 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (-3.60%)</td><td>0.07 (-2.04%)</td><td>0.07 (-6.98%)</td><td>0.05 (+4.48%)</td><td>0.01 (-15.69%)</td><td>215.30 (-4.27%)</td><td>156.34 (+0.62%)</td><td>147.50 (+7.51%)</td><td>120.30 (+3.71%)</td><td>35.48 (-15.97%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>224.90 (n/a)</td><td>155.38 (n/a)</td><td>137.20 (n/a)</td><td>116.00 (n/a)</td><td>42.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (-12.14%)</td><td>0.06 (-17.81%)</td><td>0.06 <b>(-22.42%)</b></td><td>0.05 <b>(-27.34%)</b></td><td>0.01 <b>(+22.27%)</b></td><td>232.20 <b>(+37.64%)</b></td><td>178.72 <b>(+23.54%)</b></td><td>175.90 <b>(+28.96%)</b></td><td>145.00 (+13.81%)</td><td>34.03 <b>(+91.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>168.70 (n/a)</td><td>144.66 (n/a)</td><td>136.40 (n/a)</td><td>127.40 (n/a)</td><td>17.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (-3.45%)</td><td>0.07 (+16.41%)</td><td>0.07 (+14.79%)</td><td>0.06 <b>(+83.76%)</b></td><td>0.01 <b>(-51.00%)</b></td><td>185.40 <b>(-45.58%)</b></td><td>147.08 <b>(-22.95%)</b></td><td>143.80 (-12.90%)</td><td>127.00 (+3.59%)</td><td>23.36 <b>(-73.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>340.70 (n/a)</td><td>190.88 (n/a)</td><td>165.10 (n/a)</td><td>122.60 (n/a)</td><td>87.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (+5.78%)</td><td>0.07 (+8.31%)</td><td>0.06 (+7.59%)</td><td>0.05 (+8.93%)</td><td>0.01 (+17.98%)</td><td>203.20 (-8.22%)</td><td>160.66 (-7.21%)</td><td>161.80 (-7.01%)</td><td>126.80 (-5.51%)</td><td>32.68 (-0.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>173.14 (n/a)</td><td>174.00 (n/a)</td><td>134.20 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (-10.88%)</td><td>0.07 (+13.65%)</td><td>0.07 (+11.88%)</td><td>0.06 <b>(+108.53%)</b></td><td>0.01 <b>(-65.09%)</b></td><td>184.60 <b>(-52.04%)</b></td><td>161.32 <b>(-22.48%)</b></td><td>158.50 (-10.65%)</td><td>141.90 (+12.17%)</td><td>17.33 <b>(-82.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>384.90 (n/a)</td><td>208.10 (n/a)</td><td>177.40 (n/a)</td><td>126.50 (n/a)</td><td>101.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (-10.99%)</td><td>0.05 (-17.84%)</td><td>0.05 (-8.92%)</td><td>0.03 <b>(-37.01%)</b></td><td>0.01 <b>(+68.11%)</b></td><td>311.00 <b>(+58.75%)</b></td><td>221.04 <b>(+25.58%)</b></td><td>197.30 (+9.79%)</td><td>177.90 (+12.31%)</td><td>53.33 <b>(+213.90%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>176.02 (n/a)</td><td>179.70 (n/a)</td><td>158.40 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (-12.32%)</td><td>0.06 (-6.30%)</td><td>0.06 (-1.69%)</td><td>0.05 (+4.79%)</td><td>0.01 <b>(-43.64%)</b></td><td>199.20 (-4.55%)</td><td>180.06 (+5.08%)</td><td>182.20 (+1.73%)</td><td>156.80 (+14.04%)</td><td>18.61 <b>(-36.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>171.36 (n/a)</td><td>179.10 (n/a)</td><td>137.50 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 <b>(+20.05%)</b></td><td>0.06 (+14.04%)</td><td>0.06 (-0.13%)</td><td>0.04 <b>(+29.77%)</b></td><td>0.01 (-14.04%)</td><td>237.40 <b>(-22.92%)</b></td><td>190.24 (-15.51%)</td><td>186.20 (+0.16%)</td><td>139.80 (-16.69%)</td><td>37.90 <b>(-45.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>308.00 (n/a)</td><td>225.16 (n/a)</td><td>185.90 (n/a)</td><td>167.80 (n/a)</td><td>69.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (-5.11%)</td><td>0.14 (-10.89%)</td><td>0.15 (-9.20%)</td><td>0.10 <b>(-26.53%)</b></td><td>0.03 <b>(+70.59%)</b></td><td>219.60 <b>(+36.14%)</b></td><td>158.20 (+15.12%)</td><td>144.30 (+10.15%)</td><td>132.90 (+5.39%)</td><td>35.59 <b>(+148.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>161.30 (n/a)</td><td>137.42 (n/a)</td><td>131.00 (n/a)</td><td>126.10 (n/a)</td><td>14.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (+5.87%)</td><td>0.14 (-13.95%)</td><td>0.13 <b>(-24.41%)</b></td><td>0.09 <b>(-32.59%)</b></td><td>0.04 <b>(+167.88%)</b></td><td>224.70 <b>(+48.32%)</b></td><td>159.30 <b>(+22.35%)</b></td><td>166.10 <b>(+32.35%)</b></td><td>114.30 (-5.54%)</td><td>43.74 <b>(+260.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>151.50 (n/a)</td><td>130.20 (n/a)</td><td>125.50 (n/a)</td><td>121.00 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (-5.25%)</td><td>0.14 (-8.07%)</td><td>0.15 (-5.56%)</td><td>0.12 (-9.04%)</td><td>0.02 <b>(+21.15%)</b></td><td>169.20 (+9.94%)</td><td>149.04 (+9.40%)</td><td>142.80 (+5.93%)</td><td>128.10 (+5.52%)</td><td>19.04 <b>(+44.39%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>153.90 (n/a)</td><td>136.24 (n/a)</td><td>134.80 (n/a)</td><td>121.40 (n/a)</td><td>13.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 <b>(-20.72%)</b></td><td>0.13 (-8.56%)</td><td>0.13 (-7.46%)</td><td>0.11 (+12.04%)</td><td>0.01 <b>(-60.24%)</b></td><td>189.00 (-10.76%)</td><td>163.64 (+4.98%)</td><td>163.40 (+8.07%)</td><td>140.40 <b>(+26.03%)</b></td><td>17.56 <b>(-55.24%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>211.80 (n/a)</td><td>155.88 (n/a)</td><td>151.20 (n/a)</td><td>111.40 (n/a)</td><td>39.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (-4.69%)</td><td>0.14 (-9.75%)</td><td>0.13 (-15.82%)</td><td>0.12 (-6.70%)</td><td>0.02 (+6.66%)</td><td>181.10 (+7.22%)</td><td>156.80 (+11.16%)</td><td>159.90 (+18.80%)</td><td>132.10 (+4.92%)</td><td>20.83 (+18.97%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>168.90 (n/a)</td><td>141.06 (n/a)</td><td>134.60 (n/a)</td><td>125.90 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 <b>(+30.26%)</b></td><td>0.12 (-3.59%)</td><td>0.12 (-4.90%)</td><td>0.07 <b>(-35.34%)</b></td><td>0.04 <b>(+302.38%)</b></td><td>302.50 <b>(+54.65%)</b></td><td>193.10 (+13.78%)</td><td>174.50 (+5.12%)</td><td>122.50 <b>(-23.25%)</b></td><td>70.83 <b>(+378.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>169.72 (n/a)</td><td>166.00 (n/a)</td><td>159.60 (n/a)</td><td>14.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 <b>(+27.54%)</b></td><td>0.13 (+0.82%)</td><td>0.12 (-4.01%)</td><td>0.10 (-13.66%)</td><td>0.04 <b>(+137.00%)</b></td><td>204.90 (+15.83%)</td><td>167.72 (+3.99%)</td><td>176.30 (+4.20%)</td><td>101.50 <b>(-21.56%)</b></td><td>39.02 <b>(+105.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>176.90 (n/a)</td><td>161.28 (n/a)</td><td>169.20 (n/a)</td><td>129.40 (n/a)</td><td>19.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 <b>(+22.74%)</b></td><td>0.11 (-1.24%)</td><td>0.10 (-14.72%)</td><td>0.09 (+14.03%)</td><td>0.02 <b>(+43.82%)</b></td><td>227.30 (-12.31%)</td><td>204.72 (+2.03%)</td><td>218.00 (+17.27%)</td><td>146.40 (-18.53%)</td><td>33.01 (-1.30%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>259.20 (n/a)</td><td>200.64 (n/a)</td><td>185.90 (n/a)</td><td>179.70 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>156.20 (n/a)</td><td>165.60 (n/a)</td><td>110.50 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>168.52 (n/a)</td><td>167.50 (n/a)</td><td>110.00 (n/a)</td><td>45.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>324.80 (n/a)</td><td>211.28 (n/a)</td><td>187.40 (n/a)</td><td>127.60 (n/a)</td><td>74.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>167.58 (n/a)</td><td>160.30 (n/a)</td><td>121.90 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>168.90 (n/a)</td><td>147.10 (n/a)</td><td>157.80 (n/a)</td><td>104.50 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>191.00 (n/a)</td><td>148.38 (n/a)</td><td>146.40 (n/a)</td><td>112.40 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>236.80 (n/a)</td><td>156.60 (n/a)</td><td>143.40 (n/a)</td><td>116.90 (n/a)</td><td>48.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>328.00 (n/a)</td><td>191.62 (n/a)</td><td>177.20 (n/a)</td><td>111.20 (n/a)</td><td>81.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.00 (n/a)</td><td>146.20 (n/a)</td><td>134.00 (n/a)</td><td>123.40 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.60 (n/a)</td><td>144.18 (n/a)</td><td>132.80 (n/a)</td><td>127.20 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>240.10 (n/a)</td><td>171.70 (n/a)</td><td>163.90 (n/a)</td><td>127.10 (n/a)</td><td>42.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>253.70 (n/a)</td><td>197.50 (n/a)</td><td>212.30 (n/a)</td><td>123.30 (n/a)</td><td>53.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.38 (+11.20%)</td><td>0.30 (+6.37%)</td><td>0.33 (+10.31%)</td><td>0.21 (-2.58%)</td><td>0.08 <b>(+35.90%)</b></td><td>236.40 (+2.65%)</td><td>173.02 (-3.82%)</td><td>148.70 (-9.33%)</td><td>129.50 (-10.07%)</td><td>47.21 <b>(+25.97%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>230.30 (n/a)</td><td>179.90 (n/a)</td><td>164.00 (n/a)</td><td>144.00 (n/a)</td><td>37.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>214.80 (n/a)</td><td>177.70 (n/a)</td><td>180.00 (n/a)</td><td>137.70 (n/a)</td><td>33.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>242.40 (n/a)</td><td>182.42 (n/a)</td><td>185.50 (n/a)</td><td>133.90 (n/a)</td><td>41.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>211.70 (n/a)</td><td>172.38 (n/a)</td><td>158.00 (n/a)</td><td>146.20 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>168.20 (n/a)</td><td>145.18 (n/a)</td><td>154.70 (n/a)</td><td>103.10 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>150.04 (n/a)</td><td>152.60 (n/a)</td><td>109.40 (n/a)</td><td>31.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>151.94 (n/a)</td><td>136.30 (n/a)</td><td>120.00 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>294.60 (n/a)</td><td>195.12 (n/a)</td><td>177.30 (n/a)</td><td>138.60 (n/a)</td><td>60.73 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>165.70 (n/a)</td><td>147.00 (n/a)</td><td>150.00 (n/a)</td><td>125.20 (n/a)</td><td>17.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>243.30 (n/a)</td><td>158.54 (n/a)</td><td>135.50 (n/a)</td><td>131.60 (n/a)</td><td>47.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>312.20 (n/a)</td><td>207.08 (n/a)</td><td>209.40 (n/a)</td><td>135.30 (n/a)</td><td>67.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>307.10 (n/a)</td><td>202.94 (n/a)</td><td>185.20 (n/a)</td><td>139.80 (n/a)</td><td>71.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.20 (n/a)</td><td>169.28 (n/a)</td><td>168.00 (n/a)</td><td>133.80 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.20 (n/a)</td><td>189.10 (n/a)</td><td>187.10 (n/a)</td><td>164.80 (n/a)</td><td>22.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>236.60 (n/a)</td><td>173.48 (n/a)</td><td>170.70 (n/a)</td><td>130.10 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>225.80 (n/a)</td><td>180.56 (n/a)</td><td>173.90 (n/a)</td><td>138.10 (n/a)</td><td>40.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>181.00 (n/a)</td><td>138.68 (n/a)</td><td>132.20 (n/a)</td><td>115.40 (n/a)</td><td>24.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>172.10 (n/a)</td><td>145.04 (n/a)</td><td>135.00 (n/a)</td><td>114.80 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>313.00 (n/a)</td><td>195.12 (n/a)</td><td>165.30 (n/a)</td><td>142.10 (n/a)</td><td>68.17 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.20 (n/a)</td><td>168.72 (n/a)</td><td>182.10 (n/a)</td><td>134.40 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>322.40 (n/a)</td><td>207.44 (n/a)</td><td>193.50 (n/a)</td><td>134.50 (n/a)</td><td>77.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.00 (n/a)</td><td>176.76 (n/a)</td><td>175.30 (n/a)</td><td>145.40 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.30 (n/a)</td><td>179.72 (n/a)</td><td>186.90 (n/a)</td><td>149.40 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>156.74 (n/a)</td><td>153.70 (n/a)</td><td>101.50 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>171.72 (n/a)</td><td>168.80 (n/a)</td><td>154.40 (n/a)</td><td>14.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>288.00 (n/a)</td><td>227.18 (n/a)</td><td>192.30 (n/a)</td><td>187.80 (n/a)</td><td>51.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>308.90 (n/a)</td><td>219.04 (n/a)</td><td>223.20 (n/a)</td><td>152.90 (n/a)</td><td>60.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>166.22 (n/a)</td><td>151.50 (n/a)</td><td>131.40 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.80 (n/a)</td><td>146.12 (n/a)</td><td>136.00 (n/a)</td><td>130.40 (n/a)</td><td>17.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>165.78 (n/a)</td><td>150.30 (n/a)</td><td>140.30 (n/a)</td><td>33.70 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.90 (n/a)</td><td>146.96 (n/a)</td><td>142.60 (n/a)</td><td>130.40 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>164.22 (n/a)</td><td>154.80 (n/a)</td><td>122.30 (n/a)</td><td>34.51 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>161.72 (n/a)</td><td>155.80 (n/a)</td><td>117.90 (n/a)</td><td>39.11 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.50 (n/a)</td><td>177.56 (n/a)</td><td>172.90 (n/a)</td><td>128.40 (n/a)</td><td>41.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>200.34 (n/a)</td><td>196.90 (n/a)</td><td>177.50 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>177.10 (n/a)</td><td>154.36 (n/a)</td><td>159.00 (n/a)</td><td>127.70 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.30 (n/a)</td><td>167.12 (n/a)</td><td>172.20 (n/a)</td><td>126.80 (n/a)</td><td>37.91 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>251.10 (n/a)</td><td>168.66 (n/a)</td><td>143.80 (n/a)</td><td>99.10 (n/a)</td><td>64.93 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>171.32 (n/a)</td><td>165.70 (n/a)</td><td>151.10 (n/a)</td><td>21.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>168.66 (n/a)</td><td>162.70 (n/a)</td><td>152.10 (n/a)</td><td>15.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>296.70 (n/a)</td><td>197.42 (n/a)</td><td>158.10 (n/a)</td><td>134.60 (n/a)</td><td>71.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.50 (n/a)</td><td>187.50 (n/a)</td><td>183.50 (n/a)</td><td>138.20 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>316.10 (n/a)</td><td>241.56 (n/a)</td><td>239.30 (n/a)</td><td>172.40 (n/a)</td><td>52.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.00 (n/a)</td><td>181.02 (n/a)</td><td>161.70 (n/a)</td><td>137.90 (n/a)</td><td>41.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>192.94 (n/a)</td><td>199.50 (n/a)</td><td>167.50 (n/a)</td><td>15.54 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>382.90 (n/a)</td><td>237.48 (n/a)</td><td>242.60 (n/a)</td><td>125.90 (n/a)</td><td>95.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.30 (n/a)</td><td>197.32 (n/a)</td><td>206.50 (n/a)</td><td>132.80 (n/a)</td><td>40.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.50 (n/a)</td><td>169.52 (n/a)</td><td>169.80 (n/a)</td><td>129.80 (n/a)</td><td>32.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>220.30 (n/a)</td><td>171.52 (n/a)</td><td>162.40 (n/a)</td><td>116.30 (n/a)</td><td>39.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>215.24 (n/a)</td><td>222.00 (n/a)</td><td>187.00 (n/a)</td><td>19.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.05 (+15.13%)</td><td>4.13 (+8.60%)</td><td>4.11 (+16.61%)</td><td>3.41 (+0.16%)</td><td>0.61 <b>(+28.94%)</b></td><td>2755.00 (-0.16%)</td><td>2316.82 (-7.46%)</td><td>2288.00 (-14.24%)</td><td>1860.90 (-13.14%)</td><td>331.76 (+10.90%)</td><td>1987.98 (+15.13%)</td><td>1624.09 (+8.60%)</td><td>1616.88 (+16.61%)</td><td>1342.78 (+0.16%)</td><td>240.90 <b>(+28.95%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>4.39 (n/a)</td><td>3.80 (n/a)</td><td>3.52 (n/a)</td><td>3.41 (n/a)</td><td>0.47 (n/a)</td><td>2759.50 (n/a)</td><td>2503.62 (n/a)</td><td>2668.00 (n/a)</td><td>2142.40 (n/a)</td><td>299.14 (n/a)</td><td>1726.77 (n/a)</td><td>1495.47 (n/a)</td><td>1386.60 (n/a)</td><td>1340.59 (n/a)</td><td>186.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.22 (-16.33%)</td><td>0.86 (-15.74%)</td><td>0.86 (-16.14%)</td><td>0.66 (-0.34%)</td><td>0.22 <b>(-21.81%)</b></td><td>334.40 (+0.33%)</td><td>268.66 (+16.86%)</td><td>258.20 (+19.21%)</td><td>181.30 (+19.51%)</td><td>61.97 (-6.05%)</td><td>52.05 (-16.33%)</td><td>36.85 (-15.74%)</td><td>36.54 (-16.14%)</td><td>28.22 (-0.34%)</td><td>9.54 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.46 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.66 (n/a)</td><td>0.29 (n/a)</td><td>333.30 (n/a)</td><td>229.90 (n/a)</td><td>216.60 (n/a)</td><td>151.70 (n/a)</td><td>65.96 (n/a)</td><td>62.21 (n/a)</td><td>43.74 (n/a)</td><td>43.58 (n/a)</td><td>28.32 (n/a)</td><td>12.20 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.14 (-4.06%)</td><td>0.96 (+17.11%)</td><td>0.95 <b>(+27.74%)</b></td><td>0.73 (+15.65%)</td><td>0.17 <b>(-27.91%)</b></td><td>303.40 (-13.54%)</td><td>236.74 (-17.19%)</td><td>232.30 <b>(-21.71%)</b></td><td>193.50 (+4.26%)</td><td>44.45 <b>(-37.12%)</b></td><td>48.77 (-4.06%)</td><td>40.94 (+17.11%)</td><td>40.62 <b>(+27.74%)</b></td><td>31.10 (+15.65%)</td><td>7.22 <b>(-27.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.19 (n/a)</td><td>0.82 (n/a)</td><td>0.75 (n/a)</td><td>0.63 (n/a)</td><td>0.23 (n/a)</td><td>350.90 (n/a)</td><td>285.88 (n/a)</td><td>296.70 (n/a)</td><td>185.60 (n/a)</td><td>70.68 (n/a)</td><td>50.84 (n/a)</td><td>34.96 (n/a)</td><td>31.80 (n/a)</td><td>26.89 (n/a)</td><td>10.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.52 (+0.74%)</td><td>0.52 (+0.19%)</td><td>0.52 (+0.02%)</td><td>0.52 (-0.03%)</td><td>0.00 <b>(+345.62%)</b></td><td>48732.90 (+0.03%)</td><td>48554.78 (-0.19%)</td><td>48626.10 (-0.02%)</td><td>48251.30 (-0.73%)</td><td>193.18 <b>(+342.37%)</b></td><td>356.05 (+0.74%)</td><td>353.83 (+0.19%)</td><td>353.31 (+0.02%)</td><td>352.53 (-0.03%)</td><td>1.41 <b>(+345.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48718.50 (n/a)</td><td>48647.00 (n/a)</td><td>48634.80 (n/a)</td><td>48607.30 (n/a)</td><td>43.67 (n/a)</td><td>353.44 (n/a)</td><td>353.15 (n/a)</td><td>353.24 (n/a)</td><td>352.64 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (+1.61%)</td><td>0.21 (+0.42%)</td><td>0.21 (+0.67%)</td><td>0.21 (-0.84%)</td><td>0.00 <b>(+577.18%)</b></td><td>119939.60 (+0.85%)</td><td>118173.50 (-0.40%)</td><td>117796.50 (-0.66%)</td><td>116526.60 (-1.59%)</td><td>1405.78 <b>(+572.58%)</b></td><td>147.43 (+1.61%)</td><td>145.39 (+0.42%)</td><td>145.84 (+0.67%)</td><td>143.24 (-0.84%)</td><td>1.73 <b>(+577.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118926.80 (n/a)</td><td>118651.76 (n/a)</td><td>118580.60 (n/a)</td><td>118403.70 (n/a)</td><td>209.01 (n/a)</td><td>145.10 (n/a)</td><td>144.79 (n/a)</td><td>144.88 (n/a)</td><td>144.46 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.89 (+1.31%)</td><td>0.88 (+0.15%)</td><td>0.88 (-0.08%)</td><td>0.87 (-0.36%)</td><td>0.01 <b>(+374.04%)</b></td><td>28826.30 (+0.36%)</td><td>28601.10 (-0.15%)</td><td>28642.00 (+0.08%)</td><td>28242.50 (-1.30%)</td><td>215.91 <b>(+368.75%)</b></td><td>608.30 (+1.31%)</td><td>600.70 (+0.15%)</td><td>599.81 (-0.08%)</td><td>595.98 (-0.36%)</td><td>4.56 <b>(+374.03%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28722.60 (n/a)</td><td>28643.48 (n/a)</td><td>28618.10 (n/a)</td><td>28613.10 (n/a)</td><td>46.06 (n/a)</td><td>600.42 (n/a)</td><td>599.78 (n/a)</td><td>600.32 (n/a)</td><td>598.13 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.51 (-2.06%)</td><td>3.37 (-2.34%)</td><td>3.33 (-5.47%)</td><td>3.26 (-0.94%)</td><td>0.12 (-5.77%)</td><td>7728.00 (+0.95%)</td><td>7470.30 (+2.38%)</td><td>7557.60 (+5.78%)</td><td>7162.30 (+2.10%)</td><td>270.59 (-3.28%)</td><td>2398.65 (-2.06%)</td><td>2302.19 (-2.34%)</td><td>2273.18 (-5.47%)</td><td>2223.07 (-0.94%)</td><td>84.12 (-5.77%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.59 (n/a)</td><td>3.45 (n/a)</td><td>3.52 (n/a)</td><td>3.29 (n/a)</td><td>0.13 (n/a)</td><td>7655.10 (n/a)</td><td>7296.44 (n/a)</td><td>7144.50 (n/a)</td><td>7014.70 (n/a)</td><td>279.77 (n/a)</td><td>2449.11 (n/a)</td><td>2357.29 (n/a)</td><td>2404.64 (n/a)</td><td>2244.24 (n/a)</td><td>89.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>2.94 (-6.98%)</td><td>2.81 (-2.09%)</td><td>2.82 (+0.34%)</td><td>2.66 (-3.76%)</td><td>0.10 <b>(-37.74%)</b></td><td>9470.10 (+3.91%)</td><td>8971.04 (+1.99%)</td><td>8916.70 (-0.34%)</td><td>8558.40 (+7.51%)</td><td>332.61 <b>(-29.60%)</b></td><td>2007.37 (-6.98%)</td><td>1917.12 (-2.09%)</td><td>1926.72 (+0.34%)</td><td>1814.12 (-3.76%)</td><td>70.28 <b>(-37.74%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.16 (n/a)</td><td>2.87 (n/a)</td><td>2.81 (n/a)</td><td>2.76 (n/a)</td><td>0.17 (n/a)</td><td>9113.60 (n/a)</td><td>8796.00 (n/a)</td><td>8947.10 (n/a)</td><td>7960.60 (n/a)</td><td>472.49 (n/a)</td><td>2158.10 (n/a)</td><td>1957.99 (n/a)</td><td>1920.15 (n/a)</td><td>1885.07 (n/a)</td><td>112.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.20 (-2.74%)</td><td>3.17 (-1.40%)</td><td>3.17 (-0.63%)</td><td>3.14 (-0.30%)</td><td>0.02 <b>(-67.50%)</b></td><td>8006.30 (+0.30%)</td><td>7940.44 (+1.39%)</td><td>7935.60 (+0.63%)</td><td>7873.20 (+2.81%)</td><td>47.70 <b>(-66.44%)</b></td><td>2182.07 (-2.74%)</td><td>2163.65 (-1.40%)</td><td>2164.91 (-0.63%)</td><td>2145.79 (-0.30%)</td><td>13.00 <b>(-67.50%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.29 (n/a)</td><td>3.21 (n/a)</td><td>3.19 (n/a)</td><td>3.15 (n/a)</td><td>0.06 (n/a)</td><td>7982.50 (n/a)</td><td>7831.52 (n/a)</td><td>7885.90 (n/a)</td><td>7657.70 (n/a)</td><td>142.14 (n/a)</td><td>2243.48 (n/a)</td><td>2194.27 (n/a)</td><td>2178.57 (n/a)</td><td>2152.18 (n/a)</td><td>40.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.79 (+0.40%)</td><td>0.78 (+0.16%)</td><td>0.78 (+0.01%)</td><td>0.78 (+0.21%)</td><td>0.00 <b>(+71.81%)</b></td><td>96467.20 (-0.21%)</td><td>96365.40 (-0.16%)</td><td>96446.70 (-0.01%)</td><td>96037.30 (-0.40%)</td><td>184.20 <b>(+70.75%)</b></td><td>715.55 (+0.40%)</td><td>713.12 (+0.16%)</td><td>712.51 (+0.01%)</td><td>712.36 (+0.21%)</td><td>1.37 <b>(+71.80%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96670.00 (n/a)</td><td>96521.52 (n/a)</td><td>96460.70 (n/a)</td><td>96420.50 (n/a)</td><td>107.88 (n/a)</td><td>712.71 (n/a)</td><td>711.96 (n/a)</td><td>712.41 (n/a)</td><td>710.87 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.73 (-0.04%)</td><td>0.73 (+0.02%)</td><td>0.73 (+0.01%)</td><td>0.73 (+0.11%)</td><td>0.00 <b>(-57.77%)</b></td><td>103743.20 (-0.11%)</td><td>103672.94 (-0.02%)</td><td>103659.80 (-0.01%)</td><td>103635.00 (+0.04%)</td><td>42.53 <b>(-57.81%)</b></td><td>663.09 (-0.04%)</td><td>662.85 (+0.02%)</td><td>662.93 (+0.01%)</td><td>662.40 (+0.11%)</td><td>0.27 <b>(-57.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103861.90 (n/a)</td><td>103691.16 (n/a)</td><td>103671.00 (n/a)</td><td>103593.70 (n/a)</td><td>100.81 (n/a)</td><td>663.36 (n/a)</td><td>662.73 (n/a)</td><td>662.86 (n/a)</td><td>661.64 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.69 (+0.34%)</td><td>0.69 (+0.46%)</td><td>0.69 (+0.65%)</td><td>0.69 (+0.43%)</td><td>0.00 (+12.11%)</td><td>109424.30 (-0.43%)</td><td>109039.56 (-0.46%)</td><td>108865.60 (-0.65%)</td><td>108811.10 (-0.34%)</td><td>284.58 (+11.25%)</td><td>631.55 (+0.34%)</td><td>630.23 (+0.46%)</td><td>631.23 (+0.65%)</td><td>628.01 (+0.43%)</td><td>1.64 (+12.11%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109897.00 (n/a)</td><td>109545.68 (n/a)</td><td>109578.70 (n/a)</td><td>109184.40 (n/a)</td><td>255.81 (n/a)</td><td>629.39 (n/a)</td><td>627.32 (n/a)</td><td>627.12 (n/a)</td><td>625.31 (n/a)</td><td>1.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.70 (+2.07%)</td><td>7.28 (+14.58%)</td><td>7.55 (+4.54%)</td><td>6.76 <b>(+44.01%)</b></td><td>0.46 <b>(-67.47%)</b></td><td>1318.00 <b>(-30.56%)</b></td><td>1228.54 (-16.19%)</td><td>1180.10 (-4.34%)</td><td>1157.00 (-2.02%)</td><td>78.92 <b>(-77.69%)</b></td><td>464.04 (+2.07%)</td><td>438.42 (+14.58%)</td><td>454.95 (+4.54%)</td><td>407.34 <b>(+44.01%)</b></td><td>27.59 <b>(-67.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.55 (n/a)</td><td>6.35 (n/a)</td><td>7.22 (n/a)</td><td>4.70 (n/a)</td><td>1.41 (n/a)</td><td>1898.10 (n/a)</td><td>1465.80 (n/a)</td><td>1233.70 (n/a)</td><td>1180.90 (n/a)</td><td>353.79 (n/a)</td><td>454.63 (n/a)</td><td>382.62 (n/a)</td><td>435.17 (n/a)</td><td>282.85 (n/a)</td><td>84.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.07 (-2.57%)</td><td>6.79 (-3.36%)</td><td>6.78 (-3.93%)</td><td>6.52 (-3.62%)</td><td>0.26 <b>(+40.06%)</b></td><td>1366.70 (+3.76%)</td><td>1314.40 (+3.54%)</td><td>1314.90 (+4.10%)</td><td>1260.00 (+2.65%)</td><td>51.04 <b>(+49.07%)</b></td><td>426.10 (-2.57%)</td><td>408.95 (-3.36%)</td><td>408.31 (-3.93%)</td><td>392.83 (-3.62%)</td><td>15.90 <b>(+40.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.26 (n/a)</td><td>7.03 (n/a)</td><td>7.06 (n/a)</td><td>6.77 (n/a)</td><td>0.19 (n/a)</td><td>1317.20 (n/a)</td><td>1269.46 (n/a)</td><td>1263.10 (n/a)</td><td>1227.50 (n/a)</td><td>34.24 (n/a)</td><td>437.36 (n/a)</td><td>423.16 (n/a)</td><td>425.03 (n/a)</td><td>407.60 (n/a)</td><td>11.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.60 (-10.03%)</td><td>6.43 (+2.89%)</td><td>6.47 (-0.82%)</td><td>6.10 <b>(+24.31%)</b></td><td>0.19 <b>(-81.90%)</b></td><td>1460.60 (-19.55%)</td><td>1387.34 (-5.07%)</td><td>1377.90 (+0.83%)</td><td>1350.70 (+11.14%)</td><td>42.58 <b>(-83.66%)</b></td><td>397.49 (-10.03%)</td><td>387.26 (+2.89%)</td><td>389.64 (-0.82%)</td><td>367.58 <b>(+24.31%)</b></td><td>11.50 <b>(-81.90%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.33 (n/a)</td><td>6.25 (n/a)</td><td>6.52 (n/a)</td><td>4.91 (n/a)</td><td>1.05 (n/a)</td><td>1815.60 (n/a)</td><td>1461.42 (n/a)</td><td>1366.60 (n/a)</td><td>1215.30 (n/a)</td><td>260.51 (n/a)</td><td>441.77 (n/a)</td><td>376.39 (n/a)</td><td>392.85 (n/a)</td><td>295.71 (n/a)</td><td>63.55 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.49 (+1.35%)</td><td>7.82 (-2.70%)</td><td>8.06 (+1.37%)</td><td>7.02 (-10.40%)</td><td>0.74 <b>(+249.22%)</b></td><td>4963.30 (+11.60%)</td><td>4490.28 (+3.47%)</td><td>4324.20 (-1.36%)</td><td>4106.50 (-1.34%)</td><td>433.89 <b>(+287.68%)</b></td><td>522.94 (+1.35%)</td><td>481.76 (-2.70%)</td><td>496.61 (+1.37%)</td><td>432.67 (-10.40%)</td><td>45.47 <b>(+249.22%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>8.38 (n/a)</td><td>8.04 (n/a)</td><td>7.95 (n/a)</td><td>7.84 (n/a)</td><td>0.21 (n/a)</td><td>4447.30 (n/a)</td><td>4339.64 (n/a)</td><td>4383.60 (n/a)</td><td>4162.10 (n/a)</td><td>111.92 (n/a)</td><td>515.96 (n/a)</td><td>495.12 (n/a)</td><td>489.89 (n/a)</td><td>482.87 (n/a)</td><td>13.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.87 (-0.48%)</td><td>7.53 (-0.59%)</td><td>7.53 (-0.49%)</td><td>7.16 (-2.89%)</td><td>0.34 <b>(+62.48%)</b></td><td>4871.60 (+2.97%)</td><td>4638.44 (+0.70%)</td><td>4632.60 (+0.49%)</td><td>4431.30 (+0.48%)</td><td>207.72 <b>(+67.89%)</b></td><td>484.62 (-0.48%)</td><td>463.72 (-0.59%)</td><td>463.56 (-0.49%)</td><td>440.82 (-2.89%)</td><td>20.74 <b>(+62.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.91 (n/a)</td><td>7.57 (n/a)</td><td>7.56 (n/a)</td><td>7.37 (n/a)</td><td>0.21 (n/a)</td><td>4731.00 (n/a)</td><td>4606.26 (n/a)</td><td>4610.00 (n/a)</td><td>4410.20 (n/a)</td><td>123.72 (n/a)</td><td>486.94 (n/a)</td><td>466.48 (n/a)</td><td>465.83 (n/a)</td><td>453.92 (n/a)</td><td>12.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.70 (+2.35%)</td><td>7.40 (+0.96%)</td><td>7.45 (+2.62%)</td><td>6.82 (-5.05%)</td><td>0.35 <b>(+148.53%)</b></td><td>5115.30 (+5.32%)</td><td>4721.26 (-0.80%)</td><td>4682.20 (-2.55%)</td><td>4530.00 (-2.30%)</td><td>234.62 <b>(+157.23%)</b></td><td>474.05 (+2.35%)</td><td>455.71 (+0.96%)</td><td>458.65 (+2.62%)</td><td>419.81 (-5.05%)</td><td>21.65 <b>(+148.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>7.52 (n/a)</td><td>7.33 (n/a)</td><td>7.26 (n/a)</td><td>7.18 (n/a)</td><td>0.14 (n/a)</td><td>4856.80 (n/a)</td><td>4759.10 (n/a)</td><td>4804.80 (n/a)</td><td>4636.60 (n/a)</td><td>91.21 (n/a)</td><td>463.16 (n/a)</td><td>451.37 (n/a)</td><td>446.94 (n/a)</td><td>442.16 (n/a)</td><td>8.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.79 (-0.26%)</td><td>0.79 (-0.12%)</td><td>0.79 (-0.14%)</td><td>0.79 (-0.02%)</td><td>0.00 <b>(-47.87%)</b></td><td>95930.20 (+0.02%)</td><td>95845.88 (+0.12%)</td><td>95876.00 (+0.14%)</td><td>95735.80 (+0.26%)</td><td>79.83 <b>(-47.71%)</b></td><td>717.80 (-0.26%)</td><td>716.98 (-0.12%)</td><td>716.75 (-0.14%)</td><td>716.35 (-0.02%)</td><td>0.60 <b>(-47.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95909.80 (n/a)</td><td>95732.78 (n/a)</td><td>95746.20 (n/a)</td><td>95488.50 (n/a)</td><td>152.65 (n/a)</td><td>719.66 (n/a)</td><td>717.83 (n/a)</td><td>717.73 (n/a)</td><td>716.50 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.73 (-0.01%)</td><td>0.73 (-0.01%)</td><td>0.73 (-0.02%)</td><td>0.73 (-0.01%)</td><td>0.00 <b>(+23.39%)</b></td><td>102965.20 (+0.01%)</td><td>102930.34 (+0.01%)</td><td>102939.30 (+0.02%)</td><td>102897.60 (+0.01%)</td><td>30.33 <b>(+23.36%)</b></td><td>667.84 (-0.01%)</td><td>667.63 (-0.01%)</td><td>667.57 (-0.02%)</td><td>667.40 (-0.01%)</td><td>0.20 <b>(+23.41%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102959.20 (n/a)</td><td>102920.00 (n/a)</td><td>102916.70 (n/a)</td><td>102891.40 (n/a)</td><td>24.58 (n/a)</td><td>667.88 (n/a)</td><td>667.70 (n/a)</td><td>667.72 (n/a)</td><td>667.44 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.70 (+0.20%)</td><td>0.70 (+0.21%)</td><td>0.70 (+0.28%)</td><td>0.70 (+0.07%)</td><td>0.00 (+13.26%)</td><td>108281.40 (-0.07%)</td><td>107889.08 (-0.21%)</td><td>107898.40 (-0.28%)</td><td>107632.00 (-0.20%)</td><td>248.02 (+12.99%)</td><td>638.47 (+0.20%)</td><td>636.95 (+0.21%)</td><td>636.89 (+0.28%)</td><td>634.64 (+0.07%)</td><td>1.46 (+13.26%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108362.00 (n/a)</td><td>108114.94 (n/a)</td><td>108198.50 (n/a)</td><td>107850.00 (n/a)</td><td>219.50 (n/a)</td><td>637.18 (n/a)</td><td>635.62 (n/a)</td><td>635.12 (n/a)</td><td>634.17 (n/a)</td><td>1.29 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>4.14 (-1.83%)</td><td>3.65 (+3.65%)</td><td>3.73 (+8.36%)</td><td>3.19 (+5.24%)</td><td>0.44 (+1.41%)</td><td>2530.60 (-4.98%)</td><td>2236.72 (-3.48%)</td><td>2160.80 (-7.72%)</td><td>1945.90 (+1.86%)</td><td>275.05 (+1.95%)</td><td>1086.36 (-1.83%)</td><td>956.48 (+3.65%)</td><td>978.30 (+8.36%)</td><td>835.36 (+5.24%)</td><td>115.78 (+1.41%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>4.22 (n/a)</td><td>3.52 (n/a)</td><td>3.44 (n/a)</td><td>3.03 (n/a)</td><td>0.44 (n/a)</td><td>2663.20 (n/a)</td><td>2317.36 (n/a)</td><td>2341.50 (n/a)</td><td>1910.30 (n/a)</td><td>269.78 (n/a)</td><td>1106.61 (n/a)</td><td>922.78 (n/a)</td><td>902.80 (n/a)</td><td>793.76 (n/a)</td><td>114.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.36 <b>(-36.62%)</b></td><td>0.32 <b>(-20.30%)</b></td><td>0.32 (-7.09%)</td><td>0.29 (-5.13%)</td><td>0.03 <b>(-72.36%)</b></td><td>4353.70 (+5.41%)</td><td>3899.52 (+19.17%)</td><td>3840.10 (+7.63%)</td><td>3459.50 <b>(+57.77%)</b></td><td>386.56 <b>(-53.80%)</b></td><td>19.40 <b>(-36.62%)</b></td><td>17.35 <b>(-20.30%)</b></td><td>17.48 (-7.09%)</td><td>15.41 (-5.13%)</td><td>1.71 <b>(-72.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.57 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>4130.40 (n/a)</td><td>3272.10 (n/a)</td><td>3567.80 (n/a)</td><td>2192.70 (n/a)</td><td>836.73 (n/a)</td><td>30.61 (n/a)</td><td>21.76 (n/a)</td><td>18.81 (n/a)</td><td>16.25 (n/a)</td><td>6.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.40 (-1.02%)</td><td>4.57 (-9.88%)</td><td>4.70 (-5.21%)</td><td>3.29 (-16.09%)</td><td>1.25 <b>(+34.40%)</b></td><td>2020.40 (+19.18%)</td><td>1542.00 (+14.51%)</td><td>1415.90 (+5.50%)</td><td>1038.70 (+1.03%)</td><td>402.99 <b>(+66.85%)</b></td><td>1978.65 (-1.02%)</td><td>1411.69 (-9.88%)</td><td>1451.49 (-5.21%)</td><td>1017.23 (-16.09%)</td><td>384.85 <b>(+34.40%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.47 (n/a)</td><td>5.07 (n/a)</td><td>4.96 (n/a)</td><td>3.92 (n/a)</td><td>0.93 (n/a)</td><td>1695.30 (n/a)</td><td>1346.66 (n/a)</td><td>1342.10 (n/a)</td><td>1028.10 (n/a)</td><td>241.53 (n/a)</td><td>1998.95 (n/a)</td><td>1566.53 (n/a)</td><td>1531.29 (n/a)</td><td>1212.28 (n/a)</td><td>286.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (-3.46%)</td><td>0.22 (-8.78%)</td><td>0.24 (-6.77%)</td><td>0.18 (-14.77%)</td><td>0.03 <b>(+36.17%)</b></td><td>0.25 (-3.46%)</td><td>0.22 (-8.78%)</td><td>0.23 (-6.77%)</td><td>0.18 (-14.77%)</td><td>0.03 <b>(+36.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>13.56 (-1.00%)</td><td>13.11 (+3.58%)</td><td>13.19 (-0.13%)</td><td>12.46 (+10.81%)</td><td>0.40 <b>(-62.86%)</b></td><td>13.55 (-1.00%)</td><td>13.10 (+3.58%)</td><td>13.18 (-0.13%)</td><td>12.45 (+10.81%)</td><td>0.40 <b>(-62.86%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.70 (n/a)</td><td>12.66 (n/a)</td><td>13.20 (n/a)</td><td>11.24 (n/a)</td><td>1.08 (n/a)</td><td>13.69 (n/a)</td><td>12.65 (n/a)</td><td>13.20 (n/a)</td><td>11.24 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>25.08 (-0.64%)</td><td>24.15 (-1.59%)</td><td>24.31 (-1.43%)</td><td>22.85 (-3.83%)</td><td>0.86 <b>(+54.08%)</b></td><td>25.07 (-0.64%)</td><td>24.14 (-1.59%)</td><td>24.30 (-1.43%)</td><td>22.83 (-3.83%)</td><td>0.86 <b>(+54.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>25.25 (n/a)</td><td>24.54 (n/a)</td><td>24.66 (n/a)</td><td>23.76 (n/a)</td><td>0.56 (n/a)</td><td>25.23 (n/a)</td><td>24.53 (n/a)</td><td>24.65 (n/a)</td><td>23.74 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>41.28 (-1.79%)</td><td>39.64 (-0.25%)</td><td>38.76 (-3.45%)</td><td>38.43 (+4.49%)</td><td>1.39 <b>(-38.70%)</b></td><td>41.26 (-1.79%)</td><td>39.61 (-0.25%)</td><td>38.73 (-3.45%)</td><td>38.40 (+4.49%)</td><td>1.39 <b>(-38.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>42.03 (n/a)</td><td>39.74 (n/a)</td><td>40.14 (n/a)</td><td>36.77 (n/a)</td><td>2.27 (n/a)</td><td>42.01 (n/a)</td><td>39.71 (n/a)</td><td>40.12 (n/a)</td><td>36.75 (n/a)</td><td>2.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>43.94 (-2.18%)</td><td>42.44 (-1.44%)</td><td>42.28 (-2.84%)</td><td>41.37 (+2.45%)</td><td>1.01 <b>(-48.61%)</b></td><td>43.91 (-2.18%)</td><td>42.41 (-1.44%)</td><td>42.25 (-2.84%)</td><td>41.34 (+2.45%)</td><td>1.01 <b>(-48.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>44.92 (n/a)</td><td>43.05 (n/a)</td><td>43.51 (n/a)</td><td>40.38 (n/a)</td><td>1.97 (n/a)</td><td>44.89 (n/a)</td><td>43.03 (n/a)</td><td>43.49 (n/a)</td><td>40.35 (n/a)</td><td>1.97 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>13.17 (-1.99%)</td><td>12.70 (+4.53%)</td><td>13.12 (+6.91%)</td><td>10.96 (+5.76%)</td><td>0.97 <b>(-24.31%)</b></td><td>13.17 (-1.99%)</td><td>12.69 (+4.53%)</td><td>13.11 (+6.91%)</td><td>10.96 (+5.76%)</td><td>0.97 <b>(-24.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.44 (n/a)</td><td>12.15 (n/a)</td><td>12.27 (n/a)</td><td>10.37 (n/a)</td><td>1.28 (n/a)</td><td>13.43 (n/a)</td><td>12.14 (n/a)</td><td>12.26 (n/a)</td><td>10.36 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>24.82 (-1.21%)</td><td>23.94 (-2.60%)</td><td>23.99 (-2.81%)</td><td>22.77 (-5.03%)</td><td>0.77 <b>(+64.02%)</b></td><td>24.81 (-1.21%)</td><td>23.93 (-2.60%)</td><td>23.97 (-2.81%)</td><td>22.75 (-5.03%)</td><td>0.77 <b>(+64.03%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>25.13 (n/a)</td><td>24.58 (n/a)</td><td>24.68 (n/a)</td><td>23.97 (n/a)</td><td>0.47 (n/a)</td><td>25.11 (n/a)</td><td>24.56 (n/a)</td><td>24.66 (n/a)</td><td>23.96 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>41.25 (-5.65%)</td><td>39.87 (-1.67%)</td><td>39.70 (-0.57%)</td><td>39.00 (+1.30%)</td><td>0.88 <b>(-58.85%)</b></td><td>41.23 (-5.65%)</td><td>39.84 (-1.67%)</td><td>39.68 (-0.57%)</td><td>38.98 (+1.30%)</td><td>0.88 <b>(-58.85%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>43.72 (n/a)</td><td>40.54 (n/a)</td><td>39.93 (n/a)</td><td>38.50 (n/a)</td><td>2.15 (n/a)</td><td>43.70 (n/a)</td><td>40.52 (n/a)</td><td>39.91 (n/a)</td><td>38.48 (n/a)</td><td>2.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>43.48 (-8.90%)</td><td>38.89 (-11.28%)</td><td>42.77 (-2.04%)</td><td>22.92 <b>(-44.58%)</b></td><td>8.94 <b>(+264.31%)</b></td><td>43.45 (-8.90%)</td><td>38.86 (-11.28%)</td><td>42.74 (-2.04%)</td><td>22.90 <b>(-44.58%)</b></td><td>8.93 <b>(+264.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>47.73 (n/a)</td><td>43.83 (n/a)</td><td>43.66 (n/a)</td><td>41.36 (n/a)</td><td>2.45 (n/a)</td><td>47.70 (n/a)</td><td>43.80 (n/a)</td><td>43.63 (n/a)</td><td>41.33 (n/a)</td><td>2.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>155.92 (n/a)</td><td>170.80 (n/a)</td><td>108.80 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>161.72 (n/a)</td><td>168.40 (n/a)</td><td>105.70 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>162.78 (n/a)</td><td>157.70 (n/a)</td><td>125.90 (n/a)</td><td>37.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.10 (n/a)</td><td>145.78 (n/a)</td><td>147.20 (n/a)</td><td>115.80 (n/a)</td><td>22.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.70 (n/a)</td><td>169.30 (n/a)</td><td>168.30 (n/a)</td><td>149.80 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>260.50 (n/a)</td><td>194.42 (n/a)</td><td>206.20 (n/a)</td><td>127.30 (n/a)</td><td>52.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.10 (n/a)</td><td>180.78 (n/a)</td><td>178.50 (n/a)</td><td>159.70 (n/a)</td><td>25.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.40 (n/a)</td><td>223.34 (n/a)</td><td>232.40 (n/a)</td><td>187.90 (n/a)</td><td>21.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>167.92 (n/a)</td><td>163.50 (n/a)</td><td>146.30 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>175.06 (n/a)</td><td>144.90 (n/a)</td><td>138.00 (n/a)</td><td>45.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.20 (n/a)</td><td>169.24 (n/a)</td><td>142.20 (n/a)</td><td>135.70 (n/a)</td><td>47.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.70 (n/a)</td><td>145.36 (n/a)</td><td>142.70 (n/a)</td><td>120.00 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>176.44 (n/a)</td><td>176.10 (n/a)</td><td>146.50 (n/a)</td><td>19.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>175.14 (n/a)</td><td>157.30 (n/a)</td><td>134.80 (n/a)</td><td>39.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.20 (n/a)</td><td>214.10 (n/a)</td><td>212.90 (n/a)</td><td>161.60 (n/a)</td><td>47.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.60 (n/a)</td><td>207.08 (n/a)</td><td>206.40 (n/a)</td><td>159.40 (n/a)</td><td>33.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.20 (n/a)</td><td>179.32 (n/a)</td><td>176.80 (n/a)</td><td>130.60 (n/a)</td><td>43.94 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>172.40 (n/a)</td><td>157.86 (n/a)</td><td>154.00 (n/a)</td><td>140.90 (n/a)</td><td>13.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.30 (n/a)</td><td>169.80 (n/a)</td><td>176.00 (n/a)</td><td>124.30 (n/a)</td><td>30.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.20 (n/a)</td><td>179.88 (n/a)</td><td>178.90 (n/a)</td><td>137.90 (n/a)</td><td>40.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>185.02 (n/a)</td><td>185.60 (n/a)</td><td>165.30 (n/a)</td><td>15.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>187.66 (n/a)</td><td>182.60 (n/a)</td><td>150.40 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>175.82 (n/a)</td><td>188.30 (n/a)</td><td>144.10 (n/a)</td><td>20.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>298.90 (n/a)</td><td>246.16 (n/a)</td><td>239.20 (n/a)</td><td>213.80 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (-6.48%)</td><td>0.18 (-4.17%)</td><td>0.17 (-2.19%)</td><td>0.15 (-9.63%)</td><td>0.03 (-1.19%)</td><td>223.20 (+10.66%)</td><td>189.16 (+4.69%)</td><td>190.90 (+2.25%)</td><td>148.00 (+6.94%)</td><td>30.14 (+19.01%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.70 (n/a)</td><td>180.68 (n/a)</td><td>186.70 (n/a)</td><td>138.40 (n/a)</td><td>25.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.00 (n/a)</td><td>176.56 (n/a)</td><td>184.20 (n/a)</td><td>143.30 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.00 (n/a)</td><td>173.56 (n/a)</td><td>164.10 (n/a)</td><td>161.30 (n/a)</td><td>15.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>228.80 (n/a)</td><td>191.94 (n/a)</td><td>187.10 (n/a)</td><td>158.30 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>209.80 (n/a)</td><td>162.92 (n/a)</td><td>159.80 (n/a)</td><td>123.50 (n/a)</td><td>31.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>275.40 (n/a)</td><td>203.26 (n/a)</td><td>183.10 (n/a)</td><td>166.50 (n/a)</td><td>43.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>181.38 (n/a)</td><td>177.50 (n/a)</td><td>165.20 (n/a)</td><td>13.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>325.30 (n/a)</td><td>214.62 (n/a)</td><td>197.40 (n/a)</td><td>153.40 (n/a)</td><td>65.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-14.11%)</td><td>0.03 (-18.64%)</td><td>0.03 (-18.71%)</td><td>0.02 <b>(-20.03%)</b></td><td>0.00 (-2.86%)</td><td>166.30 <b>(+25.04%)</b></td><td>151.54 <b>(+23.14%)</b></td><td>153.60 <b>(+22.98%)</b></td><td>128.60 (+16.49%)</td><td>14.00 <b>(+37.56%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>133.00 (n/a)</td><td>123.06 (n/a)</td><td>124.90 (n/a)</td><td>110.40 (n/a)</td><td>10.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+10.43%)</td><td>0.03 (+1.97%)</td><td>0.03 (+8.86%)</td><td>0.02 (-19.25%)</td><td>0.01 <b>(+97.14%)</b></td><td>205.10 <b>(+23.85%)</b></td><td>145.82 (+1.19%)</td><td>131.00 (-8.13%)</td><td>113.90 (-9.46%)</td><td>35.59 <b>(+128.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.60 (n/a)</td><td>144.10 (n/a)</td><td>142.60 (n/a)</td><td>125.80 (n/a)</td><td>15.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (+5.75%)</td><td>0.02 (+12.31%)</td><td>0.02 (+19.95%)</td><td>0.02 (+12.02%)</td><td>0.00 <b>(-26.25%)</b></td><td>212.90 (-10.73%)</td><td>193.20 (-11.30%)</td><td>188.20 (-16.61%)</td><td>181.40 (-5.47%)</td><td>12.70 <b>(-37.28%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>217.82 (n/a)</td><td>225.70 (n/a)</td><td>191.90 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (+13.82%)</td><td>0.02 (+13.99%)</td><td>0.02 (+18.99%)</td><td>0.02 (+8.68%)</td><td>0.00 <b>(+28.14%)</b></td><td>218.80 (-7.99%)</td><td>176.78 (-11.55%)</td><td>179.10 (-15.95%)</td><td>134.20 (-12.17%)</td><td>35.32 (+4.52%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.80 (n/a)</td><td>199.86 (n/a)</td><td>213.10 (n/a)</td><td>152.80 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+9.58%)</td><td>0.03 (-0.14%)</td><td>0.03 (-8.30%)</td><td>0.02 (-1.03%)</td><td>0.01 (+1.76%)</td><td>204.10 (+1.04%)</td><td>158.96 (-0.18%)</td><td>157.00 (+9.10%)</td><td>115.20 (-8.72%)</td><td>32.08 (-8.72%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>159.24 (n/a)</td><td>143.90 (n/a)</td><td>126.20 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (+17.94%)</td><td>0.03 (+12.75%)</td><td>0.03 (+17.12%)</td><td>0.02 (+0.58%)</td><td>0.01 <b>(+42.62%)</b></td><td>208.20 (-0.57%)</td><td>153.84 (-9.59%)</td><td>135.40 (-14.63%)</td><td>119.00 (-15.18%)</td><td>38.73 <b>(+20.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.40 (n/a)</td><td>170.16 (n/a)</td><td>158.60 (n/a)</td><td>140.30 (n/a)</td><td>32.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-3.82%)</td><td>0.03 (+8.36%)</td><td>0.03 (+13.07%)</td><td>0.02 (+15.05%)</td><td>0.00 <b>(-45.15%)</b></td><td>171.80 (-13.10%)</td><td>144.74 (-9.89%)</td><td>139.20 (-11.56%)</td><td>132.80 (+3.99%)</td><td>16.21 <b>(-50.15%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>160.62 (n/a)</td><td>157.40 (n/a)</td><td>127.70 (n/a)</td><td>32.51 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+11.13%)</td><td>0.03 (+13.49%)</td><td>0.03 <b>(+33.40%)</b></td><td>0.02 (+10.62%)</td><td>0.01 <b>(+28.08%)</b></td><td>210.10 (-9.60%)</td><td>149.24 (-10.31%)</td><td>123.70 <b>(-25.03%)</b></td><td>110.00 (-9.98%)</td><td>45.21 (+4.79%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.40 (n/a)</td><td>166.40 (n/a)</td><td>165.00 (n/a)</td><td>122.20 (n/a)</td><td>43.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-7.15%)</td><td>0.02 (-9.48%)</td><td>0.02 (-6.10%)</td><td>0.02 <b>(-20.33%)</b></td><td>0.00 <b>(+40.47%)</b></td><td>224.80 <b>(+25.52%)</b></td><td>174.82 (+11.79%)</td><td>164.40 (+6.48%)</td><td>150.00 (+7.68%)</td><td>28.97 <b>(+95.28%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.10 (n/a)</td><td>156.38 (n/a)</td><td>154.40 (n/a)</td><td>139.30 (n/a)</td><td>14.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-4.24%)</td><td>0.03 (+10.76%)</td><td>0.03 (+18.15%)</td><td>0.02 <b>(+38.40%)</b></td><td>0.00 <b>(-44.60%)</b></td><td>188.10 <b>(-27.76%)</b></td><td>161.46 (-13.15%)</td><td>156.30 (-15.33%)</td><td>136.20 (+4.37%)</td><td>19.97 <b>(-58.39%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>260.40 (n/a)</td><td>185.90 (n/a)</td><td>184.60 (n/a)</td><td>130.50 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (+13.02%)</td><td>0.02 (+0.12%)</td><td>0.02 (-6.98%)</td><td>0.02 (-2.28%)</td><td>0.00 <b>(+60.47%)</b></td><td>201.60 (+2.34%)</td><td>178.58 (+1.11%)</td><td>183.50 (+7.50%)</td><td>133.40 (-11.54%)</td><td>27.13 <b>(+40.14%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.00 (n/a)</td><td>176.62 (n/a)</td><td>170.70 (n/a)</td><td>150.80 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 <b>(+26.43%)</b></td><td>0.03 (+19.14%)</td><td>0.03 <b>(+26.07%)</b></td><td>0.02 (-5.84%)</td><td>0.01 <b>(+102.79%)</b></td><td>224.40 (+6.20%)</td><td>156.64 (-12.47%)</td><td>137.50 <b>(-20.70%)</b></td><td>113.00 <b>(-20.92%)</b></td><td>44.81 <b>(+73.98%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.30 (n/a)</td><td>178.96 (n/a)</td><td>173.40 (n/a)</td><td>142.90 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 <b>(+24.18%)</b></td><td>0.02 (+6.53%)</td><td>0.02 (-0.56%)</td><td>0.01 <b>(-25.40%)</b></td><td>0.01 <b>(+204.61%)</b></td><td>292.60 <b>(+34.04%)</b></td><td>200.38 (+0.50%)</td><td>203.00 (+0.59%)</td><td>135.60 (-19.48%)</td><td>62.77 <b>(+224.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.30 (n/a)</td><td>199.38 (n/a)</td><td>201.80 (n/a)</td><td>168.40 (n/a)</td><td>19.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+2.27%)</td><td>0.03 (+12.18%)</td><td>0.03 <b>(+24.68%)</b></td><td>0.02 (+5.79%)</td><td>0.01 (-7.54%)</td><td>201.80 (-5.44%)</td><td>154.82 (-11.86%)</td><td>150.60 (-19.77%)</td><td>104.10 (-2.16%)</td><td>36.52 (-11.81%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>175.66 (n/a)</td><td>187.70 (n/a)</td><td>106.40 (n/a)</td><td>41.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-0.70%)</td><td>0.02 (+18.57%)</td><td>0.03 <b>(+39.41%)</b></td><td>0.02 (+9.29%)</td><td>0.00 (-16.55%)</td><td>227.20 (-8.50%)</td><td>173.04 (-16.67%)</td><td>160.20 <b>(-28.26%)</b></td><td>148.00 (+0.68%)</td><td>32.16 <b>(-21.23%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.30 (n/a)</td><td>207.66 (n/a)</td><td>223.30 (n/a)</td><td>147.00 (n/a)</td><td>40.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 <b>(+24.40%)</b></td><td>0.03 <b>(+29.74%)</b></td><td>0.03 <b>(+23.79%)</b></td><td>0.03 <b>(+39.17%)</b></td><td>0.00 (+4.03%)</td><td>161.90 <b>(-28.14%)</b></td><td>148.22 <b>(-23.39%)</b></td><td>156.40 (-19.21%)</td><td>122.30 (-19.65%)</td><td>16.71 <b>(-38.56%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>193.48 (n/a)</td><td>193.60 (n/a)</td><td>152.20 (n/a)</td><td>27.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 <b>(+32.23%)</b></td><td>0.06 <b>(+30.57%)</b></td><td>0.06 <b>(+34.10%)</b></td><td>0.05 <b>(+23.77%)</b></td><td>0.01 <b>(+83.76%)</b></td><td>151.60 (-19.19%)</td><td>136.80 <b>(-23.17%)</b></td><td>136.20 <b>(-25.45%)</b></td><td>123.30 <b>(-24.36%)</b></td><td>11.97 (+11.44%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.60 (n/a)</td><td>178.06 (n/a)</td><td>182.70 (n/a)</td><td>163.00 (n/a)</td><td>10.74 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 <b>(+44.39%)</b></td><td>0.06 <b>(+28.72%)</b></td><td>0.05 <b>(+20.63%)</b></td><td>0.05 (+19.34%)</td><td>0.01 <b>(+143.44%)</b></td><td>176.20 (-16.18%)</td><td>151.84 <b>(-21.16%)</b></td><td>156.50 (-17.11%)</td><td>117.80 <b>(-30.75%)</b></td><td>23.57 <b>(+39.04%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.20 (n/a)</td><td>192.60 (n/a)</td><td>188.80 (n/a)</td><td>170.10 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 <b>(+47.34%)</b></td><td>0.05 <b>(+35.87%)</b></td><td>0.04 <b>(+21.77%)</b></td><td>0.04 <b>(+78.69%)</b></td><td>0.01 (+13.13%)</td><td>209.40 <b>(-44.04%)</b></td><td>183.88 <b>(-28.16%)</b></td><td>190.70 (-17.91%)</td><td>139.10 <b>(-32.15%)</b></td><td>26.43 <b>(-60.80%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>374.20 (n/a)</td><td>255.96 (n/a)</td><td>232.30 (n/a)</td><td>205.00 (n/a)</td><td>67.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (-17.17%)</td><td>0.04 (-11.25%)</td><td>0.04 (-5.47%)</td><td>0.03 (-14.50%)</td><td>0.01 <b>(-22.36%)</b></td><td>279.10 (+16.93%)</td><td>214.24 (+12.26%)</td><td>203.20 (+5.78%)</td><td>161.20 <b>(+20.75%)</b></td><td>43.12 (+14.89%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.70 (n/a)</td><td>190.84 (n/a)</td><td>192.10 (n/a)</td><td>133.50 (n/a)</td><td>37.53 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 <b>(+43.17%)</b></td><td>0.05 <b>(+37.42%)</b></td><td>0.05 <b>(+25.59%)</b></td><td>0.04 <b>(+65.35%)</b></td><td>0.01 (+5.84%)</td><td>191.10 <b>(-39.53%)</b></td><td>163.36 <b>(-28.42%)</b></td><td>162.80 <b>(-20.35%)</b></td><td>138.80 <b>(-30.15%)</b></td><td>22.01 <b>(-56.00%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.00 (n/a)</td><td>228.22 (n/a)</td><td>204.40 (n/a)</td><td>198.70 (n/a)</td><td>50.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 <b>(+20.65%)</b></td><td>0.05 <b>(+26.49%)</b></td><td>0.05 <b>(+31.49%)</b></td><td>0.05 <b>(+23.57%)</b></td><td>0.00 (-7.38%)</td><td>178.10 (-19.05%)</td><td>153.76 <b>(-21.29%)</b></td><td>150.10 <b>(-23.92%)</b></td><td>140.00 (-17.11%)</td><td>14.43 <b>(-36.60%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>195.36 (n/a)</td><td>197.30 (n/a)</td><td>168.90 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (-1.51%)</td><td>0.05 (+10.87%)</td><td>0.05 <b>(+21.87%)</b></td><td>0.04 (+3.68%)</td><td>0.01 <b>(-23.26%)</b></td><td>209.10 (-3.55%)</td><td>173.82 (-11.08%)</td><td>173.00 (-17.97%)</td><td>135.70 (+1.57%)</td><td>26.28 <b>(-24.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>195.48 (n/a)</td><td>210.90 (n/a)</td><td>133.60 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (+12.58%)</td><td>0.05 <b>(+22.54%)</b></td><td>0.05 (+14.96%)</td><td>0.04 <b>(+81.30%)</b></td><td>0.00 <b>(-49.29%)</b></td><td>190.30 <b>(-44.84%)</b></td><td>170.84 <b>(-22.68%)</b></td><td>165.60 (-13.03%)</td><td>153.90 (-11.19%)</td><td>17.02 <b>(-75.95%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>345.00 (n/a)</td><td>220.96 (n/a)</td><td>190.40 (n/a)</td><td>173.30 (n/a)</td><td>70.78 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (+14.35%)</td><td>0.05 <b>(+29.39%)</b></td><td>0.05 (+16.78%)</td><td>0.04 <b>(+87.33%)</b></td><td>0.00 <b>(-62.42%)</b></td><td>190.40 <b>(-46.61%)</b></td><td>173.54 <b>(-27.18%)</b></td><td>172.90 (-14.36%)</td><td>155.80 (-12.52%)</td><td>12.71 <b>(-82.67%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>356.60 (n/a)</td><td>238.30 (n/a)</td><td>201.90 (n/a)</td><td>178.10 (n/a)</td><td>73.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (-13.52%)</td><td>0.05 (+4.49%)</td><td>0.05 (+13.10%)</td><td>0.05 (+9.46%)</td><td>0.00 <b>(-75.79%)</b></td><td>178.40 (-8.65%)</td><td>168.50 (-5.64%)</td><td>167.80 (-11.59%)</td><td>163.10 (+15.67%)</td><td>5.90 <b>(-74.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>178.58 (n/a)</td><td>189.80 (n/a)</td><td>141.00 (n/a)</td><td>22.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (+16.49%)</td><td>0.05 (+7.62%)</td><td>0.05 (+5.80%)</td><td>0.04 (+5.11%)</td><td>0.01 <b>(+80.66%)</b></td><td>190.40 (-4.90%)</td><td>167.40 (-6.56%)</td><td>165.30 (-5.49%)</td><td>145.20 (-14.18%)</td><td>17.92 <b>(+46.10%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>200.20 (n/a)</td><td>179.16 (n/a)</td><td>174.90 (n/a)</td><td>169.20 (n/a)</td><td>12.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (+3.11%)</td><td>0.05 (+10.20%)</td><td>0.05 (+15.02%)</td><td>0.05 (+13.64%)</td><td>0.00 <b>(-29.85%)</b></td><td>180.40 (-12.00%)</td><td>167.26 (-9.71%)</td><td>167.20 (-13.05%)</td><td>155.50 (-2.99%)</td><td>11.40 <b>(-40.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>185.24 (n/a)</td><td>192.30 (n/a)</td><td>160.30 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (+8.23%)</td><td>0.05 (-0.00%)</td><td>0.05 (+2.06%)</td><td>0.04 (-3.48%)</td><td>0.01 <b>(+34.04%)</b></td><td>216.40 (+3.64%)</td><td>173.32 (+0.91%)</td><td>167.50 (-2.05%)</td><td>138.80 (-7.59%)</td><td>29.05 <b>(+27.88%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>171.76 (n/a)</td><td>171.00 (n/a)</td><td>150.20 (n/a)</td><td>22.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (-6.65%)</td><td>0.06 (+14.07%)</td><td>0.05 <b>(+22.11%)</b></td><td>0.04 (+4.01%)</td><td>0.01 (-18.41%)</td><td>198.60 (-3.87%)</td><td>152.76 (-13.62%)</td><td>156.70 (-18.13%)</td><td>121.70 (+7.13%)</td><td>31.45 (-15.79%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>176.84 (n/a)</td><td>191.40 (n/a)</td><td>113.60 (n/a)</td><td>37.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (+1.19%)</td><td>0.05 (+8.70%)</td><td>0.05 <b>(+21.65%)</b></td><td>0.04 (+10.49%)</td><td>0.01 (-16.94%)</td><td>206.70 (-9.50%)</td><td>174.56 (-9.04%)</td><td>166.30 (-17.80%)</td><td>141.90 (-1.11%)</td><td>27.08 <b>(-24.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>191.90 (n/a)</td><td>202.30 (n/a)</td><td>143.50 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (+9.04%)</td><td>0.06 (+6.57%)</td><td>0.05 (-5.03%)</td><td>0.05 <b>(+25.08%)</b></td><td>0.02 (+1.53%)</td><td>179.60 <b>(-20.04%)</b></td><td>154.90 (-7.94%)</td><td>172.90 (+5.30%)</td><td>93.80 (-8.22%)</td><td>36.04 <b>(-27.41%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>224.60 (n/a)</td><td>168.26 (n/a)</td><td>164.20 (n/a)</td><td>102.20 (n/a)</td><td>49.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (-12.51%)</td><td>0.11 (-6.90%)</td><td>0.11 (-12.50%)</td><td>0.10 (+5.09%)</td><td>0.01 <b>(-54.42%)</b></td><td>170.30 (-4.81%)</td><td>153.08 (+5.14%)</td><td>147.00 (+14.22%)</td><td>141.20 (+14.33%)</td><td>13.83 <b>(-50.35%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.90 (n/a)</td><td>145.60 (n/a)</td><td>128.70 (n/a)</td><td>123.50 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 <b>(+24.77%)</b></td><td>0.11 <b>(+22.06%)</b></td><td>0.12 <b>(+27.64%)</b></td><td>0.09 (+9.82%)</td><td>0.01 <b>(+71.21%)</b></td><td>184.50 (-8.93%)</td><td>148.92 (-17.45%)</td><td>140.70 <b>(-21.66%)</b></td><td>131.20 (-19.85%)</td><td>20.83 <b>(+29.14%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>180.40 (n/a)</td><td>179.60 (n/a)</td><td>163.70 (n/a)</td><td>16.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 <b>(+33.67%)</b></td><td>0.09 (+14.67%)</td><td>0.10 (+19.43%)</td><td>0.05 (-0.86%)</td><td>0.03 <b>(+87.55%)</b></td><td>319.40 (+0.85%)</td><td>203.46 (-6.87%)</td><td>161.40 (-16.29%)</td><td>132.50 <b>(-25.18%)</b></td><td>79.39 <b>(+39.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>316.70 (n/a)</td><td>218.48 (n/a)</td><td>192.80 (n/a)</td><td>177.10 (n/a)</td><td>57.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 <b>(+23.34%)</b></td><td>0.10 (-0.45%)</td><td>0.10 (+5.07%)</td><td>0.07 (-15.78%)</td><td>0.03 <b>(+143.79%)</b></td><td>240.10 (+18.74%)</td><td>180.70 (+5.86%)</td><td>156.70 (-4.86%)</td><td>122.90 (-18.93%)</td><td>50.75 <b>(+145.72%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>170.70 (n/a)</td><td>164.70 (n/a)</td><td>151.60 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (-0.31%)</td><td>0.11 (+4.79%)</td><td>0.11 (+2.58%)</td><td>0.10 <b>(+24.87%)</b></td><td>0.01 <b>(-57.12%)</b></td><td>168.00 (-19.92%)</td><td>154.54 (-6.00%)</td><td>154.10 (-2.53%)</td><td>146.40 (+0.34%)</td><td>8.88 <b>(-66.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>164.40 (n/a)</td><td>158.10 (n/a)</td><td>145.90 (n/a)</td><td>26.29 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (-13.03%)</td><td>0.11 (-0.42%)</td><td>0.11 (+10.38%)</td><td>0.10 (+11.70%)</td><td>0.01 <b>(-67.39%)</b></td><td>165.00 (-10.47%)</td><td>151.16 (-2.35%)</td><td>152.20 (-9.40%)</td><td>137.70 (+15.04%)</td><td>10.04 <b>(-66.10%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.30 (n/a)</td><td>154.80 (n/a)</td><td>168.00 (n/a)</td><td>119.70 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (+18.57%)</td><td>0.11 (+10.33%)</td><td>0.10 (-3.52%)</td><td>0.10 (+17.03%)</td><td>0.02 <b>(+21.94%)</b></td><td>162.80 (-14.54%)</td><td>147.32 (-9.32%)</td><td>157.70 (+3.68%)</td><td>108.10 (-15.68%)</td><td>22.45 (-16.86%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.50 (n/a)</td><td>162.46 (n/a)</td><td>152.10 (n/a)</td><td>128.20 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (+3.14%)</td><td>0.12 (+9.93%)</td><td>0.12 (+8.04%)</td><td>0.11 <b>(+21.69%)</b></td><td>0.01 <b>(-49.40%)</b></td><td>146.90 (-17.84%)</td><td>137.80 (-9.80%)</td><td>140.10 (-7.46%)</td><td>128.90 (-3.01%)</td><td>7.19 <b>(-59.98%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>152.78 (n/a)</td><td>151.40 (n/a)</td><td>132.90 (n/a)</td><td>17.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 <b>(+35.10%)</b></td><td>0.11 (+16.91%)</td><td>0.11 (+14.34%)</td><td>0.09 <b>(+20.33%)</b></td><td>0.02 <b>(+60.31%)</b></td><td>185.50 (-16.89%)</td><td>150.78 (-13.70%)</td><td>143.00 (-12.54%)</td><td>115.90 <b>(-25.99%)</b></td><td>26.52 (-3.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>174.72 (n/a)</td><td>163.50 (n/a)</td><td>156.60 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 <b>(+42.74%)</b></td><td>0.12 <b>(+29.89%)</b></td><td>0.12 <b>(+35.30%)</b></td><td>0.10 (+14.18%)</td><td>0.02 <b>(+136.39%)</b></td><td>166.70 (-12.40%)</td><td>135.24 <b>(-21.95%)</b></td><td>132.50 <b>(-26.10%)</b></td><td>108.10 <b>(-29.90%)</b></td><td>21.06 <b>(+46.02%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>173.28 (n/a)</td><td>179.30 (n/a)</td><td>154.20 (n/a)</td><td>14.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (-5.09%)</td><td>0.10 (-4.37%)</td><td>0.10 (-8.88%)</td><td>0.09 (+2.75%)</td><td>0.01 (-12.43%)</td><td>184.70 (-2.69%)</td><td>160.76 (+4.13%)</td><td>171.40 (+9.73%)</td><td>137.60 (+5.36%)</td><td>21.70 (-11.03%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.80 (n/a)</td><td>154.38 (n/a)</td><td>156.20 (n/a)</td><td>130.60 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (-13.36%)</td><td>0.10 (-5.40%)</td><td>0.10 (-4.08%)</td><td>0.08 (+2.42%)</td><td>0.02 <b>(-35.22%)</b></td><td>203.90 (-2.35%)</td><td>164.62 (+3.60%)</td><td>165.90 (+4.27%)</td><td>133.30 (+15.41%)</td><td>25.85 <b>(-26.15%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.80 (n/a)</td><td>158.90 (n/a)</td><td>159.10 (n/a)</td><td>115.50 (n/a)</td><td>34.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (-4.45%)</td><td>0.10 (-0.01%)</td><td>0.10 (+4.72%)</td><td>0.09 (+4.23%)</td><td>0.01 <b>(-25.69%)</b></td><td>184.40 (-4.06%)</td><td>163.58 (-0.94%)</td><td>167.40 (-4.51%)</td><td>139.90 (+4.64%)</td><td>20.01 <b>(-24.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.20 (n/a)</td><td>165.14 (n/a)</td><td>175.30 (n/a)</td><td>133.70 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 <b>(-23.74%)</b></td><td>0.11 (-9.76%)</td><td>0.11 (-1.83%)</td><td>0.09 (+2.34%)</td><td>0.02 <b>(-39.18%)</b></td><td>192.00 (-2.24%)</td><td>158.10 (+7.90%)</td><td>148.00 (+1.86%)</td><td>123.90 <b>(+31.11%)</b></td><td>30.68 (-16.54%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>196.40 (n/a)</td><td>146.52 (n/a)</td><td>145.30 (n/a)</td><td>94.50 (n/a)</td><td>36.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (+6.19%)</td><td>0.09 (-2.02%)</td><td>0.10 (+4.47%)</td><td>0.06 (-19.02%)</td><td>0.02 <b>(+60.88%)</b></td><td>257.70 <b>(+23.48%)</b></td><td>188.32 (+5.79%)</td><td>163.90 (-4.26%)</td><td>143.00 (-5.80%)</td><td>50.91 <b>(+85.93%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>178.02 (n/a)</td><td>171.20 (n/a)</td><td>151.80 (n/a)</td><td>27.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (+17.35%)</td><td>0.10 (+10.57%)</td><td>0.11 (+8.37%)</td><td>0.07 <b>(+55.10%)</b></td><td>0.03 (-1.08%)</td><td>240.90 <b>(-35.52%)</b></td><td>176.80 (-14.07%)</td><td>146.40 (-7.69%)</td><td>130.80 (-14.79%)</td><td>50.95 <b>(-46.15%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>373.60 (n/a)</td><td>205.74 (n/a)</td><td>158.60 (n/a)</td><td>153.50 (n/a)</td><td>94.61 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (+9.88%)</td><td>0.21 (+1.86%)</td><td>0.21 (+2.38%)</td><td>0.16 (-13.87%)</td><td>0.04 <b>(+57.14%)</b></td><td>206.30 (+16.09%)</td><td>159.58 (+0.19%)</td><td>158.80 (-2.34%)</td><td>119.00 (-8.95%)</td><td>32.61 <b>(+63.65%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>177.70 (n/a)</td><td>159.28 (n/a)</td><td>162.60 (n/a)</td><td>130.70 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (-1.83%)</td><td>0.20 (-2.22%)</td><td>0.19 (-7.62%)</td><td>0.16 (-4.68%)</td><td>0.04 <b>(+20.43%)</b></td><td>198.90 (+4.91%)</td><td>167.06 (+3.16%)</td><td>175.10 (+8.29%)</td><td>134.00 (+1.82%)</td><td>29.28 <b>(+26.24%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>189.60 (n/a)</td><td>161.94 (n/a)</td><td>161.70 (n/a)</td><td>131.60 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (+17.88%)</td><td>0.15 (-1.15%)</td><td>0.15 (-13.69%)</td><td>0.10 (-8.12%)</td><td>0.04 <b>(+30.90%)</b></td><td>332.50 (+8.84%)</td><td>230.40 (+3.35%)</td><td>222.50 (+15.89%)</td><td>154.00 (-15.20%)</td><td>64.96 <b>(+23.11%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>305.50 (n/a)</td><td>222.94 (n/a)</td><td>192.00 (n/a)</td><td>181.60 (n/a)</td><td>52.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (-19.22%)</td><td>0.17 (-19.55%)</td><td>0.18 (-16.89%)</td><td>0.15 (-15.10%)</td><td>0.03 (-10.56%)</td><td>223.00 (+17.74%)</td><td>191.92 <b>(+24.62%)</b></td><td>184.50 <b>(+20.35%)</b></td><td>161.50 <b>(+23.75%)</b></td><td>28.77 <b>(+30.85%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>189.40 (n/a)</td><td>154.00 (n/a)</td><td>153.30 (n/a)</td><td>130.50 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (-2.19%)</td><td>0.21 (+13.57%)</td><td>0.23 (+19.00%)</td><td>0.15 <b>(+50.49%)</b></td><td>0.04 <b>(-29.33%)</b></td><td>222.10 <b>(-33.54%)</b></td><td>161.00 (-17.33%)</td><td>142.40 (-15.94%)</td><td>140.20 (+2.26%)</td><td>35.11 <b>(-55.62%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>334.20 (n/a)</td><td>194.74 (n/a)</td><td>169.40 (n/a)</td><td>137.10 (n/a)</td><td>79.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (-4.68%)</td><td>0.21 (-9.79%)</td><td>0.19 <b>(-23.54%)</b></td><td>0.17 (-11.07%)</td><td>0.04 (+2.65%)</td><td>193.90 (+12.47%)</td><td>160.56 (+11.28%)</td><td>171.20 <b>(+30.79%)</b></td><td>128.30 (+4.91%)</td><td>27.96 (+16.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>172.40 (n/a)</td><td>144.28 (n/a)</td><td>130.90 (n/a)</td><td>122.30 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (-6.39%)</td><td>0.20 (+3.22%)</td><td>0.19 (-2.04%)</td><td>0.18 <b>(+92.50%)</b></td><td>0.02 <b>(-64.18%)</b></td><td>182.70 <b>(-48.05%)</b></td><td>168.58 (-13.41%)</td><td>172.40 (+2.07%)</td><td>140.20 (+6.78%)</td><td>16.58 <b>(-81.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>351.70 (n/a)</td><td>194.68 (n/a)</td><td>168.90 (n/a)</td><td>131.30 (n/a)</td><td>89.87 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (-2.50%)</td><td>0.20 (-1.07%)</td><td>0.20 (-3.59%)</td><td>0.16 (-6.69%)</td><td>0.03 (+12.82%)</td><td>202.50 (+7.20%)</td><td>164.44 (+1.73%)</td><td>166.60 (+3.74%)</td><td>134.00 (+2.52%)</td><td>28.35 <b>(+21.26%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>188.90 (n/a)</td><td>161.64 (n/a)</td><td>160.60 (n/a)</td><td>130.70 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (+2.75%)</td><td>0.22 (+4.32%)</td><td>0.22 (-0.80%)</td><td>0.16 (-7.99%)</td><td>0.03 (+12.74%)</td><td>199.00 (+8.68%)</td><td>151.98 (-3.63%)</td><td>147.00 (+0.82%)</td><td>130.30 (-2.69%)</td><td>27.25 (+19.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.10 (n/a)</td><td>157.70 (n/a)</td><td>145.80 (n/a)</td><td>133.90 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (+3.05%)</td><td>0.22 (-3.42%)</td><td>0.21 (-3.71%)</td><td>0.17 (-4.72%)</td><td>0.04 (+3.49%)</td><td>190.70 (+4.95%)</td><td>156.30 (+3.78%)</td><td>158.70 (+3.86%)</td><td>120.30 (-2.98%)</td><td>27.26 (+7.16%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>181.70 (n/a)</td><td>150.60 (n/a)</td><td>152.80 (n/a)</td><td>124.00 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (+19.46%)</td><td>0.21 (-6.02%)</td><td>0.20 (-12.69%)</td><td>0.17 (-7.39%)</td><td>0.05 <b>(+79.38%)</b></td><td>193.10 (+8.00%)</td><td>161.76 (+9.30%)</td><td>161.40 (+14.55%)</td><td>109.40 (-16.30%)</td><td>33.40 <b>(+62.27%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.80 (n/a)</td><td>148.00 (n/a)</td><td>140.90 (n/a)</td><td>130.70 (n/a)</td><td>20.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (+11.76%)</td><td>0.22 (+7.72%)</td><td>0.20 (+12.22%)</td><td>0.18 (+10.00%)</td><td>0.04 (+1.72%)</td><td>180.30 (-9.08%)</td><td>155.12 (-7.51%)</td><td>165.10 (-10.90%)</td><td>119.10 (-10.52%)</td><td>27.24 (-13.94%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>198.30 (n/a)</td><td>167.72 (n/a)</td><td>185.30 (n/a)</td><td>133.10 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (+0.71%)</td><td>0.20 (+7.73%)</td><td>0.21 (+11.35%)</td><td>0.17 (+3.49%)</td><td>0.03 (+9.18%)</td><td>191.00 (-3.39%)</td><td>162.12 (-7.03%)</td><td>154.20 (-10.19%)</td><td>143.30 (-0.69%)</td><td>21.50 (+3.76%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>197.70 (n/a)</td><td>174.38 (n/a)</td><td>171.70 (n/a)</td><td>144.30 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 <b>(+35.50%)</b></td><td>0.21 (+2.22%)</td><td>0.20 (+3.78%)</td><td>0.15 (-19.30%)</td><td>0.06 <b>(+272.72%)</b></td><td>215.60 <b>(+23.91%)</b></td><td>170.06 (+3.85%)</td><td>165.80 (-3.66%)</td><td>109.70 <b>(-26.23%)</b></td><td>45.97 <b>(+254.67%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>174.00 (n/a)</td><td>163.76 (n/a)</td><td>172.10 (n/a)</td><td>148.70 (n/a)</td><td>12.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (+5.94%)</td><td>0.18 (-4.42%)</td><td>0.17 (-16.30%)</td><td>0.15 (+7.61%)</td><td>0.04 (+5.57%)</td><td>222.10 (-7.03%)</td><td>184.82 (+4.48%)</td><td>190.60 (+19.50%)</td><td>136.90 (-5.65%)</td><td>33.88 (-9.61%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>238.90 (n/a)</td><td>176.90 (n/a)</td><td>159.50 (n/a)</td><td>145.10 (n/a)</td><td>37.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (-19.98%)</td><td>0.22 (-15.09%)</td><td>0.20 <b>(-20.90%)</b></td><td>0.16 (-12.13%)</td><td>0.05 (-12.20%)</td><td>200.00 (+13.83%)</td><td>157.06 (+18.00%)</td><td>166.70 <b>(+26.48%)</b></td><td>123.90 <b>(+25.03%)</b></td><td>32.85 (+17.96%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>175.70 (n/a)</td><td>133.10 (n/a)</td><td>131.80 (n/a)</td><td>99.10 (n/a)</td><td>27.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (+0.74%)</td><td>0.21 (+0.19%)</td><td>0.21 (+0.03%)</td><td>0.21 (+0.12%)</td><td>0.00 <b>(+331.59%)</b></td><td>40885.90 (-0.12%)</td><td>40806.28 (-0.19%)</td><td>40871.20 (-0.03%)</td><td>40540.60 (-0.74%)</td><td>149.18 <b>(+327.60%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40933.00 (n/a)</td><td>40882.34 (n/a)</td><td>40885.30 (n/a)</td><td>40841.80 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (+0.10%)</td><td>0.21 (+0.01%)</td><td>0.21 (-0.01%)</td><td>0.20 (+0.02%)</td><td>0.00 <b>(+32.14%)</b></td><td>40944.20 (-0.02%)</td><td>40885.84 (-0.01%)</td><td>40907.70 (+0.01%)</td><td>40764.50 (-0.10%)</td><td>69.98 <b>(+32.03%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40952.60 (n/a)</td><td>40890.68 (n/a)</td><td>40901.90 (n/a)</td><td>40806.20 (n/a)</td><td>53.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (-0.03%)</td><td>0.13 (+0.01%)</td><td>0.13 (-0.02%)</td><td>0.13 (+0.03%)</td><td>0.00 (-14.10%)</td><td>322474.10 (-0.03%)</td><td>322227.64 (-0.01%)</td><td>322329.10 (+0.02%)</td><td>321967.10 (+0.03%)</td><td>219.59 (-14.11%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>322557.30 (n/a)</td><td>322264.98 (n/a)</td><td>322269.10 (n/a)</td><td>321866.90 (n/a)</td><td>255.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+6.96%)</td><td>0.03 (+1.72%)</td><td>0.03 (-15.41%)</td><td>0.02 (+17.46%)</td><td>0.01 (-15.79%)</td><td>192.10 (-14.89%)</td><td>152.02 (-4.40%)</td><td>151.50 (+18.17%)</td><td>113.00 (-6.53%)</td><td>32.85 <b>(-31.71%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>159.02 (n/a)</td><td>128.20 (n/a)</td><td>120.90 (n/a)</td><td>48.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-6.14%)</td><td>0.03 (-8.38%)</td><td>0.04 (-4.56%)</td><td>0.02 <b>(-36.81%)</b></td><td>0.01 <b>(+47.97%)</b></td><td>328.40 <b>(+58.27%)</b></td><td>192.66 (+16.45%)</td><td>165.40 (+4.82%)</td><td>146.90 (+6.53%)</td><td>76.59 <b>(+162.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>165.44 (n/a)</td><td>157.80 (n/a)</td><td>137.90 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+12.10%)</td><td>0.03 (-3.82%)</td><td>0.03 (+4.34%)</td><td>0.02 <b>(-21.27%)</b></td><td>0.01 <b>(+65.06%)</b></td><td>214.90 <b>(+27.01%)</b></td><td>144.14 (+8.54%)</td><td>127.00 (-4.15%)</td><td>100.30 (-10.84%)</td><td>43.55 <b>(+93.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>169.20 (n/a)</td><td>132.80 (n/a)</td><td>132.50 (n/a)</td><td>112.50 (n/a)</td><td>22.53 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+6.82%)</td><td>0.03 (+8.90%)</td><td>0.03 (+8.19%)</td><td>0.03 (+7.22%)</td><td>0.01 (-10.73%)</td><td>185.40 (-6.74%)</td><td>151.72 (-9.00%)</td><td>155.10 (-7.57%)</td><td>123.30 (-6.45%)</td><td>23.63 <b>(-22.98%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>166.72 (n/a)</td><td>167.80 (n/a)</td><td>131.80 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (+9.50%)</td><td>0.03 (+0.30%)</td><td>0.03 (-2.62%)</td><td>0.02 (-11.94%)</td><td>0.01 <b>(+26.45%)</b></td><td>231.60 (+13.59%)</td><td>165.24 (+2.38%)</td><td>162.30 (+2.66%)</td><td>109.70 (-8.66%)</td><td>48.93 <b>(+29.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>161.40 (n/a)</td><td>158.10 (n/a)</td><td>120.10 (n/a)</td><td>37.87 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-17.18%)</td><td>0.03 (+8.40%)</td><td>0.03 (+15.07%)</td><td>0.03 <b>(+46.92%)</b></td><td>0.00 <b>(-55.76%)</b></td><td>204.10 <b>(-31.94%)</b></td><td>168.06 (-13.88%)</td><td>156.10 (-13.08%)</td><td>148.70 <b>(+20.70%)</b></td><td>23.27 <b>(-64.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>299.90 (n/a)</td><td>195.14 (n/a)</td><td>179.60 (n/a)</td><td>123.20 (n/a)</td><td>65.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-11.95%)</td><td>0.02 (-10.63%)</td><td>0.02 (-10.89%)</td><td>0.02 (-10.52%)</td><td>0.00 <b>(-23.37%)</b></td><td>211.80 (+11.77%)</td><td>174.98 (+11.27%)</td><td>171.20 (+12.19%)</td><td>145.20 (+13.53%)</td><td>25.17 (-2.79%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>157.26 (n/a)</td><td>152.60 (n/a)</td><td>127.90 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-14.40%)</td><td>0.03 (-15.66%)</td><td>0.03 (-11.48%)</td><td>0.02 (-11.19%)</td><td>0.00 <b>(-27.50%)</b></td><td>227.50 (+12.62%)</td><td>184.20 (+17.47%)</td><td>179.70 (+12.95%)</td><td>144.10 (+16.87%)</td><td>30.67 (-3.19%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>156.80 (n/a)</td><td>159.10 (n/a)</td><td>123.30 (n/a)</td><td>31.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-10.46%)</td><td>0.02 <b>(-22.93%)</b></td><td>0.02 <b>(-26.02%)</b></td><td>0.02 (-19.53%)</td><td>0.00 (+11.18%)</td><td>214.60 <b>(+24.26%)</b></td><td>181.34 <b>(+31.37%)</b></td><td>177.70 <b>(+35.24%)</b></td><td>134.00 (+11.67%)</td><td>33.16 <b>(+55.71%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.70 (n/a)</td><td>138.04 (n/a)</td><td>131.40 (n/a)</td><td>120.00 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 <b>(-29.93%)</b></td><td>0.02 (-12.72%)</td><td>0.02 (-8.97%)</td><td>0.02 <b>(+20.40%)</b></td><td>0.00 <b>(-78.02%)</b></td><td>209.80 (-16.94%)</td><td>196.82 (+9.69%)</td><td>194.80 (+9.87%)</td><td>185.40 <b>(+42.73%)</b></td><td>11.56 <b>(-74.52%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>179.44 (n/a)</td><td>177.30 (n/a)</td><td>129.90 (n/a)</td><td>45.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-10.85%)</td><td>0.02 (-14.67%)</td><td>0.02 (-9.54%)</td><td>0.01 <b>(-35.56%)</b></td><td>0.01 (+19.40%)</td><td>323.80 <b>(+55.23%)</b></td><td>210.28 <b>(+22.24%)</b></td><td>200.30 (+10.54%)</td><td>143.80 (+12.17%)</td><td>67.64 <b>(+121.90%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.60 (n/a)</td><td>172.02 (n/a)</td><td>181.20 (n/a)</td><td>128.20 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-4.22%)</td><td>0.02 (-3.71%)</td><td>0.02 (+2.45%)</td><td>0.02 (-18.23%)</td><td>0.00 (+6.98%)</td><td>272.20 <b>(+22.28%)</b></td><td>201.40 (+4.92%)</td><td>190.30 (-2.36%)</td><td>157.00 (+4.39%)</td><td>43.12 <b>(+38.41%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.60 (n/a)</td><td>191.96 (n/a)</td><td>194.90 (n/a)</td><td>150.40 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (-19.72%)</td><td>0.02 <b>(-23.26%)</b></td><td>0.02 <b>(-21.06%)</b></td><td>0.02 (-12.28%)</td><td>0.00 <b>(-39.20%)</b></td><td>247.30 (+14.02%)</td><td>212.28 <b>(+27.82%)</b></td><td>219.80 <b>(+26.69%)</b></td><td>158.80 <b>(+24.55%)</b></td><td>32.52 (-13.43%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>166.08 (n/a)</td><td>173.50 (n/a)</td><td>127.50 (n/a)</td><td>37.57 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (-13.84%)</td><td>0.02 (-2.72%)</td><td>0.02 (+4.59%)</td><td>0.02 (-5.31%)</td><td>0.00 <b>(-26.82%)</b></td><td>251.90 (+5.57%)</td><td>212.14 (+2.40%)</td><td>203.30 (-4.42%)</td><td>199.30 (+16.07%)</td><td>22.37 (-8.31%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.60 (n/a)</td><td>207.16 (n/a)</td><td>212.70 (n/a)</td><td>171.70 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (-9.69%)</td><td>0.02 (-13.45%)</td><td>0.02 (-5.23%)</td><td>0.01 (+9.92%)</td><td>0.01 (-12.10%)</td><td>341.40 (-9.03%)</td><td>252.74 (+13.43%)</td><td>207.80 (+5.54%)</td><td>175.60 (+10.72%)</td><td>77.48 (-11.44%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>375.30 (n/a)</td><td>222.82 (n/a)</td><td>196.90 (n/a)</td><td>158.60 (n/a)</td><td>87.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 <b>(-29.98%)</b></td><td>0.04 <b>(-25.48%)</b></td><td>0.04 <b>(-26.87%)</b></td><td>0.04 (-16.08%)</td><td>0.00 <b>(-64.50%)</b></td><td>233.60 (+19.18%)</td><td>204.18 <b>(+30.32%)</b></td><td>205.20 <b>(+36.71%)</b></td><td>177.50 <b>(+42.80%)</b></td><td>20.76 <b>(-39.03%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>156.68 (n/a)</td><td>150.10 (n/a)</td><td>124.30 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (+17.79%)</td><td>0.07 (+6.20%)</td><td>0.07 (-0.87%)</td><td>0.06 (+3.84%)</td><td>0.01 <b>(+63.51%)</b></td><td>198.60 (-3.69%)</td><td>168.44 (-5.13%)</td><td>171.00 (+0.88%)</td><td>139.10 (-15.13%)</td><td>22.30 <b>(+31.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>177.54 (n/a)</td><td>169.50 (n/a)</td><td>163.90 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 <b>(-39.09%)</b></td><td>0.04 <b>(-30.66%)</b></td><td>0.04 (-18.29%)</td><td>0.02 <b>(-45.84%)</b></td><td>0.01 <b>(-32.67%)</b></td><td>368.70 <b>(+84.63%)</b></td><td>231.42 <b>(+47.08%)</b></td><td>200.60 <b>(+22.32%)</b></td><td>186.10 <b>(+64.11%)</b></td><td>77.01 <b>(+115.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>157.34 (n/a)</td><td>164.00 (n/a)</td><td>113.40 (n/a)</td><td>35.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 <b>(-39.25%)</b></td><td>0.04 <b>(-37.07%)</b></td><td>0.04 <b>(-39.60%)</b></td><td>0.03 <b>(-29.51%)</b></td><td>0.01 <b>(-53.68%)</b></td><td>324.60 <b>(+41.87%)</b></td><td>269.52 <b>(+54.61%)</b></td><td>262.60 <b>(+65.57%)</b></td><td>215.60 <b>(+64.71%)</b></td><td>51.23 (+9.01%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>228.80 (n/a)</td><td>174.32 (n/a)</td><td>158.60 (n/a)</td><td>130.90 (n/a)</td><td>47.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (-12.98%)</td><td>0.05 (-8.40%)</td><td>0.05 (-5.52%)</td><td>0.04 (-12.12%)</td><td>0.00 (-12.38%)</td><td>190.00 (+13.77%)</td><td>169.50 (+9.17%)</td><td>171.30 (+5.87%)</td><td>152.80 (+14.89%)</td><td>15.86 (+13.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.00 (n/a)</td><td>155.26 (n/a)</td><td>161.80 (n/a)</td><td>133.00 (n/a)</td><td>13.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (+17.25%)</td><td>0.06 (+13.80%)</td><td>0.06 (-0.21%)</td><td>0.05 <b>(+46.77%)</b></td><td>0.01 <b>(-26.29%)</b></td><td>198.50 <b>(-31.86%)</b></td><td>173.26 (-17.42%)</td><td>181.30 (+0.22%)</td><td>123.70 (-14.69%)</td><td>28.71 <b>(-59.84%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>291.30 (n/a)</td><td>209.82 (n/a)</td><td>180.90 (n/a)</td><td>145.00 (n/a)</td><td>71.50 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 <b>(+27.05%)</b></td><td>0.05 (-5.03%)</td><td>0.04 (-19.45%)</td><td>0.03 <b>(-32.64%)</b></td><td>0.02 <b>(+160.19%)</b></td><td>293.60 <b>(+48.43%)</b></td><td>196.66 (+16.93%)</td><td>210.80 <b>(+24.15%)</b></td><td>103.90 <b>(-21.35%)</b></td><td>71.09 <b>(+201.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>168.18 (n/a)</td><td>169.80 (n/a)</td><td>132.10 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (+7.57%)</td><td>0.05 (-9.72%)</td><td>0.05 (-14.26%)</td><td>0.04 (-14.58%)</td><td>0.01 <b>(+78.74%)</b></td><td>230.10 (+17.10%)</td><td>192.92 (+13.00%)</td><td>200.70 (+16.69%)</td><td>138.60 (-7.04%)</td><td>33.58 <b>(+86.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>170.72 (n/a)</td><td>172.00 (n/a)</td><td>149.10 (n/a)</td><td>18.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (-14.68%)</td><td>0.04 (-15.64%)</td><td>0.05 (-9.44%)</td><td>0.03 <b>(-30.18%)</b></td><td>0.01 <b>(+32.68%)</b></td><td>302.60 <b>(+43.21%)</b></td><td>206.36 <b>(+23.67%)</b></td><td>181.90 (+10.44%)</td><td>154.00 (+17.20%)</td><td>62.81 <b>(+116.89%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>166.86 (n/a)</td><td>164.70 (n/a)</td><td>131.40 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 <b>(-32.10%)</b></td><td>0.05 <b>(-21.06%)</b></td><td>0.05 (-19.21%)</td><td>0.04 (-8.15%)</td><td>0.00 <b>(-72.04%)</b></td><td>212.30 (+8.87%)</td><td>194.66 <b>(+24.29%)</b></td><td>191.40 <b>(+23.72%)</b></td><td>181.00 <b>(+47.27%)</b></td><td>11.64 <b>(-54.89%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.00 (n/a)</td><td>156.62 (n/a)</td><td>154.70 (n/a)</td><td>122.90 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (+2.39%)</td><td>0.04 (-2.28%)</td><td>0.04 (-14.58%)</td><td>0.03 (+15.71%)</td><td>0.01 (-6.19%)</td><td>252.60 (-13.58%)</td><td>191.66 (+0.63%)</td><td>191.50 (+17.05%)</td><td>150.90 (-2.33%)</td><td>42.89 <b>(-25.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.30 (n/a)</td><td>190.46 (n/a)</td><td>163.60 (n/a)</td><td>154.50 (n/a)</td><td>57.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 <b>(-22.19%)</b></td><td>0.04 <b>(-27.18%)</b></td><td>0.04 (-19.02%)</td><td>0.03 <b>(-48.49%)</b></td><td>0.01 <b>(+141.47%)</b></td><td>316.70 <b>(+94.18%)</b></td><td>220.90 <b>(+42.85%)</b></td><td>197.20 <b>(+23.48%)</b></td><td>181.90 <b>(+28.55%)</b></td><td>56.26 <b>(+505.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>163.10 (n/a)</td><td>154.64 (n/a)</td><td>159.70 (n/a)</td><td>141.50 (n/a)</td><td>9.29 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (-14.05%)</td><td>0.04 (-12.46%)</td><td>0.04 (-5.41%)</td><td>0.03 <b>(-30.33%)</b></td><td>0.01 (+13.20%)</td><td>323.40 <b>(+43.54%)</b></td><td>209.42 (+18.79%)</td><td>197.00 (+5.69%)</td><td>151.40 (+16.37%)</td><td>69.94 <b>(+89.00%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.30 (n/a)</td><td>176.30 (n/a)</td><td>186.40 (n/a)</td><td>130.10 (n/a)</td><td>37.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 <b>(-39.27%)</b></td><td>0.04 (-9.64%)</td><td>0.04 (-0.87%)</td><td>0.04 (+11.84%)</td><td>0.00 <b>(-83.26%)</b></td><td>231.10 (-10.57%)</td><td>208.38 (+3.13%)</td><td>207.80 (+0.87%)</td><td>195.50 <b>(+64.70%)</b></td><td>13.86 <b>(-74.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>258.40 (n/a)</td><td>202.06 (n/a)</td><td>206.00 (n/a)</td><td>118.70 (n/a)</td><td>54.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (-1.69%)</td><td>0.03 (-18.90%)</td><td>0.03 <b>(-20.06%)</b></td><td>0.02 <b>(-34.17%)</b></td><td>0.01 <b>(+143.35%)</b></td><td>329.10 <b>(+51.87%)</b></td><td>245.16 <b>(+27.13%)</b></td><td>235.80 <b>(+25.09%)</b></td><td>183.40 (+1.72%)</td><td>52.56 <b>(+276.39%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>192.84 (n/a)</td><td>188.50 (n/a)</td><td>180.30 (n/a)</td><td>13.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (+1.67%)</td><td>0.10 (+7.23%)</td><td>0.09 (+8.07%)</td><td>0.08 (+14.42%)</td><td>0.02 (-18.24%)</td><td>195.90 (-12.58%)</td><td>168.64 (-8.38%)</td><td>173.50 (-7.47%)</td><td>125.30 (-1.65%)</td><td>26.30 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.10 (n/a)</td><td>184.06 (n/a)</td><td>187.50 (n/a)</td><td>127.40 (n/a)</td><td>38.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (-14.29%)</td><td>0.14 (-6.72%)</td><td>0.14 (+0.42%)</td><td>0.11 (-17.28%)</td><td>0.03 <b>(-22.44%)</b></td><td>226.40 <b>(+20.88%)</b></td><td>178.26 (+6.64%)</td><td>178.50 (-0.39%)</td><td>133.50 (+16.70%)</td><td>33.47 (+10.69%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>187.30 (n/a)</td><td>167.16 (n/a)</td><td>179.20 (n/a)</td><td>114.40 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (+4.43%)</td><td>0.10 (-1.70%)</td><td>0.10 (-16.36%)</td><td>0.09 (+19.20%)</td><td>0.02 <b>(-29.65%)</b></td><td>188.90 (-16.12%)</td><td>161.56 (-2.08%)</td><td>169.50 (+19.53%)</td><td>119.20 (-4.26%)</td><td>26.20 <b>(-45.02%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>225.20 (n/a)</td><td>165.00 (n/a)</td><td>141.80 (n/a)</td><td>124.50 (n/a)</td><td>47.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (+13.16%)</td><td>0.12 (+3.60%)</td><td>0.11 (-1.35%)</td><td>0.08 (-14.23%)</td><td>0.03 <b>(+68.27%)</b></td><td>245.20 (+16.60%)</td><td>175.36 (+0.17%)</td><td>182.60 (+1.39%)</td><td>120.40 (-11.60%)</td><td>47.08 <b>(+75.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>175.06 (n/a)</td><td>180.10 (n/a)</td><td>136.20 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 <b>(-24.98%)</b></td><td>0.09 (-17.76%)</td><td>0.09 (-13.61%)</td><td>0.08 (+1.07%)</td><td>0.01 <b>(-60.46%)</b></td><td>210.70 (-1.03%)</td><td>180.88 (+17.26%)</td><td>183.30 (+15.72%)</td><td>155.20 <b>(+33.33%)</b></td><td>20.39 <b>(-46.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>212.90 (n/a)</td><td>154.26 (n/a)</td><td>158.40 (n/a)</td><td>116.40 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (+0.95%)</td><td>0.10 (-10.06%)</td><td>0.11 (-9.58%)</td><td>0.07 <b>(+20.41%)</b></td><td>0.03 (-4.20%)</td><td>304.50 (-16.94%)</td><td>219.46 (+8.45%)</td><td>181.00 (+10.57%)</td><td>146.40 (-0.95%)</td><td>74.52 (-19.66%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>366.60 (n/a)</td><td>202.36 (n/a)</td><td>163.70 (n/a)</td><td>147.80 (n/a)</td><td>92.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (+1.19%)</td><td>0.09 (-6.86%)</td><td>0.09 (-11.02%)</td><td>0.07 (-10.16%)</td><td>0.02 <b>(+25.99%)</b></td><td>234.80 (+11.33%)</td><td>191.00 (+8.46%)</td><td>191.10 (+12.41%)</td><td>146.30 (-1.22%)</td><td>32.82 <b>(+36.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>176.10 (n/a)</td><td>170.00 (n/a)</td><td>148.10 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (+5.99%)</td><td>0.11 (-12.07%)</td><td>0.10 <b>(-23.19%)</b></td><td>0.08 (-14.82%)</td><td>0.03 <b>(+50.66%)</b></td><td>234.30 (+17.44%)</td><td>178.50 (+17.20%)</td><td>180.70 <b>(+30.19%)</b></td><td>127.50 (-5.70%)</td><td>44.47 <b>(+63.82%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>199.50 (n/a)</td><td>152.30 (n/a)</td><td>138.80 (n/a)</td><td>135.20 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (-16.29%)</td><td>0.08 <b>(-27.69%)</b></td><td>0.08 <b>(-33.24%)</b></td><td>0.05 <b>(-32.13%)</b></td><td>0.02 (-0.78%)</td><td>318.30 <b>(+47.36%)</b></td><td>210.14 <b>(+41.99%)</b></td><td>198.50 <b>(+49.81%)</b></td><td>152.10 (+19.48%)</td><td>65.76 <b>(+72.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.00 (n/a)</td><td>148.00 (n/a)</td><td>132.50 (n/a)</td><td>127.30 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (+17.68%)</td><td>0.12 (+0.01%)</td><td>0.13 (+5.94%)</td><td>0.06 <b>(-42.42%)</b></td><td>0.04 <b>(+168.07%)</b></td><td>312.60 <b>(+73.67%)</b></td><td>175.44 (+11.36%)</td><td>145.40 (-5.58%)</td><td>114.50 (-15.06%)</td><td>79.25 <b>(+317.44%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>180.00 (n/a)</td><td>157.54 (n/a)</td><td>154.00 (n/a)</td><td>134.80 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (-13.10%)</td><td>0.09 (-3.37%)</td><td>0.09 (-0.52%)</td><td>0.08 (+4.81%)</td><td>0.01 <b>(-34.95%)</b></td><td>205.80 (-4.59%)</td><td>177.88 (+2.42%)</td><td>173.20 (+0.52%)</td><td>160.80 (+15.02%)</td><td>19.18 <b>(-29.88%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>173.68 (n/a)</td><td>172.30 (n/a)</td><td>139.80 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (+4.09%)</td><td>0.10 (+7.01%)</td><td>0.11 (+7.72%)</td><td>0.09 <b>(+22.64%)</b></td><td>0.01 <b>(-20.73%)</b></td><td>203.20 (-18.46%)</td><td>174.58 (-7.62%)</td><td>162.30 (-7.15%)</td><td>157.50 (-3.90%)</td><td>20.78 <b>(-40.00%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>249.20 (n/a)</td><td>188.98 (n/a)</td><td>174.80 (n/a)</td><td>163.90 (n/a)</td><td>34.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (-13.34%)</td><td>0.09 (-8.27%)</td><td>0.09 (-2.42%)</td><td>0.06 <b>(-20.43%)</b></td><td>0.02 (+2.90%)</td><td>261.00 <b>(+25.66%)</b></td><td>197.08 (+10.22%)</td><td>183.20 (+2.46%)</td><td>159.00 (+15.38%)</td><td>40.67 <b>(+53.73%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.70 (n/a)</td><td>178.80 (n/a)</td><td>178.80 (n/a)</td><td>137.80 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (-6.49%)</td><td>0.10 (+8.60%)</td><td>0.10 (+12.17%)</td><td>0.09 (+15.26%)</td><td>0.01 <b>(-45.61%)</b></td><td>197.90 (-13.24%)</td><td>176.64 (-9.19%)</td><td>173.30 (-10.85%)</td><td>161.70 (+6.94%)</td><td>14.87 <b>(-48.90%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>194.52 (n/a)</td><td>194.40 (n/a)</td><td>151.20 (n/a)</td><td>29.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (+15.15%)</td><td>0.08 (-1.56%)</td><td>0.09 (+8.98%)</td><td>0.05 <b>(-26.86%)</b></td><td>0.02 <b>(+165.76%)</b></td><td>314.90 <b>(+36.68%)</b></td><td>211.30 (+7.22%)</td><td>178.10 (-8.24%)</td><td>156.70 (-13.19%)</td><td>63.80 <b>(+219.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>197.08 (n/a)</td><td>194.10 (n/a)</td><td>180.50 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (-6.30%)</td><td>0.20 (-2.66%)</td><td>0.20 (+0.68%)</td><td>0.15 (+3.55%)</td><td>0.03 (-15.27%)</td><td>215.30 (-3.41%)</td><td>168.46 (+1.86%)</td><td>160.50 (-0.68%)</td><td>140.50 (+6.68%)</td><td>30.37 (-14.08%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.90 (n/a)</td><td>165.38 (n/a)</td><td>161.60 (n/a)</td><td>131.70 (n/a)</td><td>35.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (-3.46%)</td><td>0.20 (+2.84%)</td><td>0.20 (+5.36%)</td><td>0.14 (-2.41%)</td><td>0.04 (+5.07%)</td><td>238.00 (+2.45%)</td><td>169.50 (-2.22%)</td><td>163.00 (-5.12%)</td><td>135.90 (+3.58%)</td><td>41.09 (+10.44%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>232.30 (n/a)</td><td>173.34 (n/a)</td><td>171.80 (n/a)</td><td>131.20 (n/a)</td><td>37.20 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 <b>(+31.09%)</b></td><td>0.28 (+15.46%)</td><td>0.28 (+6.76%)</td><td>0.21 (+19.60%)</td><td>0.06 <b>(+40.18%)</b></td><td>196.50 (-16.42%)</td><td>150.30 (-12.83%)</td><td>145.40 (-6.31%)</td><td>109.30 <b>(-23.73%)</b></td><td>32.56 (-12.45%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>235.10 (n/a)</td><td>172.42 (n/a)</td><td>155.20 (n/a)</td><td>143.30 (n/a)</td><td>37.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (+14.02%)</td><td>0.22 (+7.20%)</td><td>0.21 (+1.02%)</td><td>0.17 (-8.92%)</td><td>0.05 <b>(+76.93%)</b></td><td>193.50 (+9.82%)</td><td>152.22 (-4.49%)</td><td>159.10 (-1.00%)</td><td>113.60 (-12.28%)</td><td>31.50 <b>(+69.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.20 (n/a)</td><td>159.38 (n/a)</td><td>160.70 (n/a)</td><td>129.50 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (-1.88%)</td><td>0.25 (-8.79%)</td><td>0.26 (-8.95%)</td><td>0.22 (-9.90%)</td><td>0.03 <b>(+38.21%)</b></td><td>187.10 (+11.04%)</td><td>163.48 (+10.24%)</td><td>158.00 (+9.87%)</td><td>142.00 (+1.87%)</td><td>18.44 <b>(+56.52%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>168.50 (n/a)</td><td>148.30 (n/a)</td><td>143.80 (n/a)</td><td>139.40 (n/a)</td><td>11.78 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (+6.20%)</td><td>0.20 <b>(+29.65%)</b></td><td>0.21 <b>(+20.97%)</b></td><td>0.15 <b>(+69.23%)</b></td><td>0.04 <b>(-35.85%)</b></td><td>219.60 <b>(-40.92%)</b></td><td>168.44 <b>(-32.00%)</b></td><td>159.20 (-17.34%)</td><td>125.50 (-5.78%)</td><td>36.47 <b>(-67.26%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>371.70 (n/a)</td><td>247.70 (n/a)</td><td>192.60 (n/a)</td><td>133.20 (n/a)</td><td>111.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (-12.47%)</td><td>0.24 (-0.66%)</td><td>0.25 (+2.00%)</td><td>0.16 (-11.96%)</td><td>0.05 (-2.04%)</td><td>237.10 (+13.61%)</td><td>160.82 (+1.76%)</td><td>150.40 (-1.96%)</td><td>130.60 (+14.26%)</td><td>43.92 <b>(+30.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>208.70 (n/a)</td><td>158.04 (n/a)</td><td>153.40 (n/a)</td><td>114.30 (n/a)</td><td>33.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (-2.59%)</td><td>0.20 (-6.31%)</td><td>0.20 (-2.73%)</td><td>0.16 (-17.16%)</td><td>0.04 <b>(+30.95%)</b></td><td>208.90 <b>(+20.68%)</b></td><td>168.44 (+8.18%)</td><td>167.60 (+2.82%)</td><td>129.70 (+2.61%)</td><td>29.76 <b>(+64.62%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>173.10 (n/a)</td><td>155.70 (n/a)</td><td>163.00 (n/a)</td><td>126.40 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (+14.90%)</td><td>0.21 (+1.39%)</td><td>0.23 (+4.62%)</td><td>0.15 (-8.36%)</td><td>0.05 <b>(+63.17%)</b></td><td>242.40 (+9.14%)</td><td>181.78 (+1.21%)</td><td>162.40 (-4.41%)</td><td>136.20 (-12.97%)</td><td>43.08 <b>(+58.23%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>222.10 (n/a)</td><td>179.60 (n/a)</td><td>169.90 (n/a)</td><td>156.50 (n/a)</td><td>27.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (-7.60%)</td><td>0.19 (+1.37%)</td><td>0.18 (+1.84%)</td><td>0.15 (-1.19%)</td><td>0.02 (-16.55%)</td><td>222.50 (+1.23%)</td><td>179.92 (-1.78%)</td><td>178.30 (-1.82%)</td><td>154.40 (+8.20%)</td><td>26.43 (-6.22%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.80 (n/a)</td><td>183.18 (n/a)</td><td>181.60 (n/a)</td><td>142.70 (n/a)</td><td>28.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (-18.66%)</td><td>0.16 (-12.11%)</td><td>0.16 <b>(-22.36%)</b></td><td>0.13 <b>(+38.81%)</b></td><td>0.03 <b>(-51.73%)</b></td><td>259.90 <b>(-27.97%)</b></td><td>218.54 (+2.54%)</td><td>212.20 <b>(+28.84%)</b></td><td>160.50 <b>(+22.99%)</b></td><td>39.26 <b>(-58.26%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>360.80 (n/a)</td><td>213.12 (n/a)</td><td>164.70 (n/a)</td><td>130.50 (n/a)</td><td>94.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (-7.40%)</td><td>0.21 (-3.50%)</td><td>0.21 (-12.74%)</td><td>0.18 (+12.56%)</td><td>0.02 <b>(-51.35%)</b></td><td>187.00 (-11.16%)</td><td>161.20 (+0.10%)</td><td>159.70 (+14.56%)</td><td>138.70 (+8.02%)</td><td>18.49 <b>(-53.04%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>210.50 (n/a)</td><td>161.04 (n/a)</td><td>139.40 (n/a)</td><td>128.40 (n/a)</td><td>39.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 <b>(+33.42%)</b></td><td>0.18 (-5.52%)</td><td>0.18 (-12.82%)</td><td>0.10 <b>(-34.09%)</b></td><td>0.06 <b>(+185.40%)</b></td><td>339.60 <b>(+51.74%)</b></td><td>213.12 (+15.93%)</td><td>196.10 (+14.68%)</td><td>124.70 <b>(-25.02%)</b></td><td>78.99 <b>(+228.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>223.80 (n/a)</td><td>183.84 (n/a)</td><td>171.00 (n/a)</td><td>166.30 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (-9.38%)</td><td>0.17 (+3.47%)</td><td>0.17 (+7.28%)</td><td>0.14 <b>(+23.18%)</b></td><td>0.02 <b>(-41.34%)</b></td><td>242.30 (-18.80%)</td><td>201.44 (-6.98%)</td><td>195.00 (-6.79%)</td><td>171.20 (+10.38%)</td><td>30.55 <b>(-47.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>298.40 (n/a)</td><td>216.56 (n/a)</td><td>209.20 (n/a)</td><td>155.10 (n/a)</td><td>58.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 <b>(+22.81%)</b></td><td>0.12 (+4.56%)</td><td>0.11 (+4.34%)</td><td>0.08 (-14.80%)</td><td>0.03 <b>(+131.70%)</b></td><td>242.40 (+17.38%)</td><td>182.62 (-0.60%)</td><td>180.60 (-4.14%)</td><td>131.20 (-18.56%)</td><td>44.46 <b>(+123.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>183.72 (n/a)</td><td>188.40 (n/a)</td><td>161.10 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (-9.29%)</td><td>0.12 (-9.79%)</td><td>0.11 (-14.63%)</td><td>0.11 (-4.87%)</td><td>0.01 <b>(-22.62%)</b></td><td>194.80 (+5.13%)</td><td>173.38 (+10.32%)</td><td>180.20 (+17.17%)</td><td>146.30 (+10.25%)</td><td>20.13 (-10.62%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>185.30 (n/a)</td><td>157.16 (n/a)</td><td>153.80 (n/a)</td><td>132.70 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (+9.51%)</td><td>0.12 (-9.52%)</td><td>0.12 (-12.12%)</td><td>0.10 (-14.37%)</td><td>0.02 <b>(+84.06%)</b></td><td>214.30 (+16.72%)</td><td>176.44 (+12.89%)</td><td>168.70 (+13.76%)</td><td>131.50 (-8.68%)</td><td>33.00 <b>(+98.11%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>156.30 (n/a)</td><td>148.30 (n/a)</td><td>144.00 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (-19.98%)</td><td>0.12 (-5.21%)</td><td>0.12 (-8.28%)</td><td>0.11 <b>(+38.98%)</b></td><td>0.02 <b>(-59.43%)</b></td><td>191.60 <b>(-28.02%)</b></td><td>166.50 (-1.34%)</td><td>173.10 (+9.01%)</td><td>140.20 <b>(+24.96%)</b></td><td>19.95 <b>(-65.56%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>266.20 (n/a)</td><td>168.76 (n/a)</td><td>158.80 (n/a)</td><td>112.20 (n/a)</td><td>57.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (-15.01%)</td><td>0.12 (-8.85%)</td><td>0.12 (-4.33%)</td><td>0.10 (-8.32%)</td><td>0.02 (-13.94%)</td><td>207.30 (+9.05%)</td><td>176.62 (+9.63%)</td><td>171.70 (+4.57%)</td><td>153.30 (+17.65%)</td><td>24.25 (+10.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>161.10 (n/a)</td><td>164.20 (n/a)</td><td>130.30 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (-3.46%)</td><td>0.12 (-4.65%)</td><td>0.11 (-5.51%)</td><td>0.11 (+0.58%)</td><td>0.02 (-6.34%)</td><td>187.10 (-0.58%)</td><td>173.64 (+4.75%)</td><td>179.90 (+5.82%)</td><td>140.00 (+3.55%)</td><td>19.44 (-3.23%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>165.76 (n/a)</td><td>170.00 (n/a)</td><td>135.20 (n/a)</td><td>20.09 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (-3.37%)</td><td>0.11 (-5.27%)</td><td>0.09 (-19.52%)</td><td>0.09 <b>(+40.77%)</b></td><td>0.02 <b>(-36.66%)</b></td><td>235.60 <b>(-28.95%)</b></td><td>199.84 (-1.56%)</td><td>216.30 <b>(+24.24%)</b></td><td>143.90 (+3.45%)</td><td>36.40 <b>(-53.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>331.60 (n/a)</td><td>203.00 (n/a)</td><td>174.10 (n/a)</td><td>139.10 (n/a)</td><td>79.11 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (+17.29%)</td><td>0.12 (+12.05%)</td><td>0.11 (-0.89%)</td><td>0.10 <b>(+27.18%)</b></td><td>0.02 (-16.21%)</td><td>204.30 <b>(-21.36%)</b></td><td>178.78 (-12.64%)</td><td>185.90 (+0.92%)</td><td>138.20 (-14.74%)</td><td>24.94 <b>(-46.07%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>259.80 (n/a)</td><td>204.64 (n/a)</td><td>184.20 (n/a)</td><td>162.10 (n/a)</td><td>46.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (+2.00%)</td><td>0.17 (+9.16%)</td><td>0.18 (+3.65%)</td><td>0.13 <b>(+20.41%)</b></td><td>0.02 <b>(-29.00%)</b></td><td>192.20 (-16.94%)</td><td>151.34 (-10.92%)</td><td>138.30 (-3.49%)</td><td>129.50 (-1.97%)</td><td>25.50 <b>(-41.67%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>231.40 (n/a)</td><td>169.90 (n/a)</td><td>143.30 (n/a)</td><td>132.10 (n/a)</td><td>43.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (-6.79%)</td><td>0.14 (+3.31%)</td><td>0.13 (+7.73%)</td><td>0.12 (+12.30%)</td><td>0.02 <b>(-37.02%)</b></td><td>197.40 (-10.96%)</td><td>178.30 (-5.10%)</td><td>187.70 (-7.17%)</td><td>145.50 (+7.30%)</td><td>21.11 <b>(-39.80%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>221.70 (n/a)</td><td>187.88 (n/a)</td><td>202.20 (n/a)</td><td>135.60 (n/a)</td><td>35.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (+1.54%)</td><td>0.15 (+1.18%)</td><td>0.15 (+3.49%)</td><td>0.14 (+4.19%)</td><td>0.02 (+1.90%)</td><td>175.60 (-4.04%)</td><td>161.04 (-1.15%)</td><td>163.00 (-3.38%)</td><td>131.30 (-1.50%)</td><td>18.10 (-1.94%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>183.00 (n/a)</td><td>162.92 (n/a)</td><td>168.70 (n/a)</td><td>133.30 (n/a)</td><td>18.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 <b>(+26.25%)</b></td><td>0.16 <b>(+25.97%)</b></td><td>0.16 <b>(+21.24%)</b></td><td>0.13 <b>(+52.09%)</b></td><td>0.02 (-15.73%)</td><td>184.20 <b>(-34.24%)</b></td><td>158.94 <b>(-22.40%)</b></td><td>158.40 (-17.50%)</td><td>129.60 <b>(-20.78%)</b></td><td>19.65 <b>(-57.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>280.10 (n/a)</td><td>204.82 (n/a)</td><td>192.00 (n/a)</td><td>163.60 (n/a)</td><td>46.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (+3.14%)</td><td>0.16 (+7.42%)</td><td>0.17 (+16.89%)</td><td>0.12 (+8.64%)</td><td>0.03 (+0.89%)</td><td>197.50 (-7.97%)</td><td>156.04 (-7.13%)</td><td>141.80 (-14.48%)</td><td>127.90 (-3.11%)</td><td>29.64 (-9.13%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.60 (n/a)</td><td>168.02 (n/a)</td><td>165.80 (n/a)</td><td>132.00 (n/a)</td><td>32.62 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (+2.08%)</td><td>0.13 (-7.86%)</td><td>0.13 (-15.26%)</td><td>0.09 (+3.99%)</td><td>0.03 (-5.82%)</td><td>263.90 (-3.83%)</td><td>191.14 (+7.19%)</td><td>187.80 (+17.96%)</td><td>134.10 (-2.05%)</td><td>46.93 (-15.00%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>274.40 (n/a)</td><td>178.32 (n/a)</td><td>159.20 (n/a)</td><td>136.90 (n/a)</td><td>55.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (+8.29%)</td><td>0.14 (+2.01%)</td><td>0.13 (+1.18%)</td><td>0.08 <b>(-29.64%)</b></td><td>0.03 <b>(+138.57%)</b></td><td>293.50 <b>(+42.13%)</b></td><td>193.18 (+3.57%)</td><td>186.40 (-1.17%)</td><td>144.70 (-7.66%)</td><td>59.92 <b>(+219.74%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>186.52 (n/a)</td><td>188.60 (n/a)</td><td>156.70 (n/a)</td><td>18.74 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (-16.27%)</td><td>0.13 (-6.40%)</td><td>0.14 (+11.97%)</td><td>0.09 (-4.06%)</td><td>0.02 <b>(-31.51%)</b></td><td>264.50 (+4.26%)</td><td>199.60 (+4.59%)</td><td>177.30 (-10.68%)</td><td>161.30 (+19.39%)</td><td>42.76 (-12.34%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>253.70 (n/a)</td><td>190.84 (n/a)</td><td>198.50 (n/a)</td><td>135.10 (n/a)</td><td>48.78 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (+8.40%)</td><td>0.10 (-14.20%)</td><td>0.10 (-8.13%)</td><td>0.05 <b>(-48.83%)</b></td><td>0.04 <b>(+148.15%)</b></td><td>343.10 <b>(+95.39%)</b></td><td>205.28 <b>(+34.03%)</b></td><td>176.70 (+8.81%)</td><td>119.70 (-7.78%)</td><td>93.70 <b>(+348.30%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>175.60 (n/a)</td><td>153.16 (n/a)</td><td>162.40 (n/a)</td><td>129.80 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (+5.74%)</td><td>0.11 (-6.43%)</td><td>0.10 (-11.64%)</td><td>0.07 <b>(-21.00%)</b></td><td>0.03 <b>(+31.05%)</b></td><td>268.50 <b>(+26.59%)</b></td><td>185.84 (+10.24%)</td><td>185.60 (+13.17%)</td><td>128.10 (-5.39%)</td><td>53.14 <b>(+60.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>212.10 (n/a)</td><td>168.58 (n/a)</td><td>164.00 (n/a)</td><td>135.40 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (-10.86%)</td><td>0.11 (-0.02%)</td><td>0.11 (+3.61%)</td><td>0.07 (-1.48%)</td><td>0.03 (-16.75%)</td><td>264.30 (+1.50%)</td><td>179.42 (-1.02%)</td><td>165.50 (-3.50%)</td><td>129.80 (+12.19%)</td><td>51.46 (-1.08%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>260.40 (n/a)</td><td>181.26 (n/a)</td><td>171.50 (n/a)</td><td>115.70 (n/a)</td><td>52.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 <b>(+20.36%)</b></td><td>0.13 <b>(+21.02%)</b></td><td>0.14 <b>(+31.99%)</b></td><td>0.10 <b>(+25.01%)</b></td><td>0.02 <b>(+32.54%)</b></td><td>189.10 (-19.97%)</td><td>150.24 (-17.09%)</td><td>133.50 <b>(-24.23%)</b></td><td>125.00 (-16.89%)</td><td>27.95 (-14.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>236.30 (n/a)</td><td>181.20 (n/a)</td><td>176.20 (n/a)</td><td>150.40 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 <b>(+38.11%)</b></td><td>0.13 (+16.86%)</td><td>0.12 (+7.64%)</td><td>0.09 (+11.23%)</td><td>0.04 <b>(+106.11%)</b></td><td>208.20 (-10.10%)</td><td>157.64 (-10.56%)</td><td>147.60 (-7.05%)</td><td>109.00 <b>(-27.57%)</b></td><td>46.05 <b>(+37.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>231.60 (n/a)</td><td>176.26 (n/a)</td><td>158.80 (n/a)</td><td>150.50 (n/a)</td><td>33.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (-0.72%)</td><td>0.10 (+2.27%)</td><td>0.10 (-3.82%)</td><td>0.09 (+11.82%)</td><td>0.01 <b>(-26.03%)</b></td><td>203.20 (-10.56%)</td><td>178.02 (-3.39%)</td><td>176.20 (+4.01%)</td><td>156.10 (+0.71%)</td><td>21.54 <b>(-33.65%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>184.26 (n/a)</td><td>169.40 (n/a)</td><td>155.00 (n/a)</td><td>32.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (-0.20%)</td><td>0.10 (-14.82%)</td><td>0.09 (-18.40%)</td><td>0.08 (-16.65%)</td><td>0.02 <b>(+50.36%)</b></td><td>234.50 <b>(+20.01%)</b></td><td>200.18 (+19.83%)</td><td>210.40 <b>(+22.54%)</b></td><td>139.90 (+0.21%)</td><td>36.64 <b>(+76.10%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>167.06 (n/a)</td><td>171.70 (n/a)</td><td>139.60 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (-10.40%)</td><td>0.09 (-16.66%)</td><td>0.09 (-17.92%)</td><td>0.07 <b>(-20.81%)</b></td><td>0.02 <b>(+23.86%)</b></td><td>254.50 <b>(+26.30%)</b></td><td>205.90 <b>(+21.40%)</b></td><td>201.70 <b>(+21.80%)</b></td><td>163.50 (+11.60%)</td><td>34.46 <b>(+72.28%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>169.60 (n/a)</td><td>165.60 (n/a)</td><td>146.50 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.67 (-14.18%)</td><td>0.51 (-12.49%)</td><td>0.52 (-14.19%)</td><td>0.36 (-11.00%)</td><td>0.12 (-18.94%)</td><td>274.70 (+12.35%)</td><td>199.60 (+13.50%)</td><td>189.30 (+16.56%)</td><td>147.00 (+16.48%)</td><td>48.28 (+6.27%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.78 (n/a)</td><td>0.59 (n/a)</td><td>0.61 (n/a)</td><td>0.40 (n/a)</td><td>0.14 (n/a)</td><td>244.50 (n/a)</td><td>175.86 (n/a)</td><td>162.40 (n/a)</td><td>126.20 (n/a)</td><td>45.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.78 (+1.14%)</td><td>0.60 (+1.39%)</td><td>0.53 (-7.41%)</td><td>0.43 (-6.35%)</td><td>0.15 <b>(+28.73%)</b></td><td>228.50 (+6.78%)</td><td>171.34 (+0.61%)</td><td>184.30 (+8.03%)</td><td>126.70 (-1.17%)</td><td>42.11 <b>(+31.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.77 (n/a)</td><td>0.59 (n/a)</td><td>0.58 (n/a)</td><td>0.46 (n/a)</td><td>0.12 (n/a)</td><td>214.00 (n/a)</td><td>170.30 (n/a)</td><td>170.60 (n/a)</td><td>128.20 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.76 <b>(+26.48%)</b></td><td>0.51 (-8.98%)</td><td>0.47 (-16.10%)</td><td>0.36 <b>(-22.72%)</b></td><td>0.15 <b>(+182.65%)</b></td><td>273.00 <b>(+29.38%)</b></td><td>206.68 (+15.93%)</td><td>209.40 (+19.18%)</td><td>129.00 <b>(-20.96%)</b></td><td>52.86 <b>(+174.84%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.47 (n/a)</td><td>0.05 (n/a)</td><td>211.00 (n/a)</td><td>178.28 (n/a)</td><td>175.70 (n/a)</td><td>163.20 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.74 (+5.81%)</td><td>0.53 (+1.60%)</td><td>0.54 (+9.14%)</td><td>0.38 (-5.33%)</td><td>0.15 <b>(+24.87%)</b></td><td>259.90 (+5.61%)</td><td>195.86 (+0.73%)</td><td>182.90 (-8.37%)</td><td>132.90 (-5.48%)</td><td>54.00 <b>(+29.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.70 (n/a)</td><td>0.53 (n/a)</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.12 (n/a)</td><td>246.10 (n/a)</td><td>194.44 (n/a)</td><td>199.60 (n/a)</td><td>140.60 (n/a)</td><td>41.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.56 (+0.41%)</td><td>0.44 (-7.77%)</td><td>0.44 (-9.98%)</td><td>0.32 <b>(-21.97%)</b></td><td>0.09 <b>(+49.01%)</b></td><td>230.60 <b>(+28.18%)</b></td><td>173.96 (+10.99%)</td><td>168.70 (+11.06%)</td><td>131.40 (-0.38%)</td><td>38.02 <b>(+88.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.56 (n/a)</td><td>0.48 (n/a)</td><td>0.49 (n/a)</td><td>0.41 (n/a)</td><td>0.06 (n/a)</td><td>179.90 (n/a)</td><td>156.74 (n/a)</td><td>151.90 (n/a)</td><td>131.90 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.58 (+2.04%)</td><td>0.46 (+6.01%)</td><td>0.44 (+6.54%)</td><td>0.37 (+15.33%)</td><td>0.08 (-4.50%)</td><td>198.70 (-13.31%)</td><td>166.28 (-6.30%)</td><td>167.00 (-6.13%)</td><td>127.90 (-1.99%)</td><td>29.53 (-17.44%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>229.20 (n/a)</td><td>177.46 (n/a)</td><td>177.90 (n/a)</td><td>130.50 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.59 (+12.07%)</td><td>0.42 (-1.24%)</td><td>0.40 (-2.50%)</td><td>0.35 (+10.13%)</td><td>0.10 (+5.71%)</td><td>212.50 (-9.19%)</td><td>183.08 (+0.93%)</td><td>185.00 (+2.55%)</td><td>125.30 (-10.75%)</td><td>35.34 (-13.03%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.53 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>234.00 (n/a)</td><td>181.40 (n/a)</td><td>180.40 (n/a)</td><td>140.40 (n/a)</td><td>40.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.67 <b>(+22.36%)</b></td><td>0.43 (-6.27%)</td><td>0.38 (-16.77%)</td><td>0.32 <b>(-20.22%)</b></td><td>0.14 <b>(+146.92%)</b></td><td>233.30 <b>(+25.36%)</b></td><td>184.62 (+12.85%)</td><td>196.40 <b>(+20.12%)</b></td><td>109.60 (-18.27%)</td><td>46.46 <b>(+144.29%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.06 (n/a)</td><td>186.10 (n/a)</td><td>163.60 (n/a)</td><td>163.50 (n/a)</td><td>134.10 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (+7.39%)</td><td>0.23 (+10.37%)</td><td>0.22 (+17.56%)</td><td>0.19 (+11.54%)</td><td>0.04 (-5.41%)</td><td>189.20 (-10.37%)</td><td>161.74 (-10.12%)</td><td>165.70 (-14.94%)</td><td>127.20 (-6.88%)</td><td>26.97 <b>(-20.88%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>211.10 (n/a)</td><td>179.96 (n/a)</td><td>194.80 (n/a)</td><td>136.60 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (+8.66%)</td><td>0.20 (-3.76%)</td><td>0.19 (-8.51%)</td><td>0.17 (-2.73%)</td><td>0.04 <b>(+44.76%)</b></td><td>221.40 (+2.83%)</td><td>188.08 (+5.06%)</td><td>193.00 (+9.29%)</td><td>139.50 (-7.98%)</td><td>30.02 <b>(+30.10%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>215.30 (n/a)</td><td>179.02 (n/a)</td><td>176.60 (n/a)</td><td>151.60 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (+8.88%)</td><td>0.23 (+15.46%)</td><td>0.22 (+7.83%)</td><td>0.18 (+8.03%)</td><td>0.05 (+7.72%)</td><td>209.80 (-7.45%)</td><td>163.40 (-13.44%)</td><td>171.30 (-7.26%)</td><td>121.60 (-8.16%)</td><td>33.80 (-8.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>226.70 (n/a)</td><td>188.76 (n/a)</td><td>184.70 (n/a)</td><td>132.40 (n/a)</td><td>36.87 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (-0.45%)</td><td>0.21 (+4.94%)</td><td>0.21 (+7.19%)</td><td>0.18 (+4.39%)</td><td>0.03 (-9.96%)</td><td>204.00 (-4.18%)</td><td>174.78 (-5.04%)</td><td>176.40 (-6.72%)</td><td>152.30 (+0.46%)</td><td>21.66 (-14.55%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>212.90 (n/a)</td><td>184.06 (n/a)</td><td>189.10 (n/a)</td><td>151.60 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (-7.07%)</td><td>0.21 (-5.57%)</td><td>0.21 (-7.17%)</td><td>0.19 (-2.38%)</td><td>0.02 (-14.24%)</td><td>195.20 (+2.41%)</td><td>174.64 (+5.66%)</td><td>178.20 (+7.74%)</td><td>146.30 (+7.57%)</td><td>18.53 (-4.94%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>190.60 (n/a)</td><td>165.28 (n/a)</td><td>165.40 (n/a)</td><td>136.00 (n/a)</td><td>19.50 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (-17.88%)</td><td>0.21 (-8.62%)</td><td>0.21 (-10.23%)</td><td>0.17 (+7.91%)</td><td>0.02 <b>(-46.41%)</b></td><td>210.90 (-7.30%)</td><td>181.40 (+6.82%)</td><td>171.70 (+11.42%)</td><td>159.80 <b>(+21.71%)</b></td><td>22.38 <b>(-40.30%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>227.50 (n/a)</td><td>169.82 (n/a)</td><td>154.10 (n/a)</td><td>131.30 (n/a)</td><td>37.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (+5.49%)</td><td>0.20 (-2.26%)</td><td>0.21 (-7.12%)</td><td>0.14 (-10.10%)</td><td>0.04 <b>(+27.54%)</b></td><td>271.80 (+11.26%)</td><td>189.58 (+4.23%)</td><td>175.60 (+7.66%)</td><td>148.90 (-5.16%)</td><td>49.11 <b>(+35.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>244.30 (n/a)</td><td>181.88 (n/a)</td><td>163.10 (n/a)</td><td>157.00 (n/a)</td><td>36.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (+12.10%)</td><td>0.17 (-19.61%)</td><td>0.14 <b>(-37.47%)</b></td><td>0.13 (-14.85%)</td><td>0.06 <b>(+33.28%)</b></td><td>287.70 (+17.43%)</td><td>241.74 <b>(+28.82%)</b></td><td>260.00 <b>(+59.90%)</b></td><td>132.40 (-10.78%)</td><td>62.66 <b>(+33.45%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>245.00 (n/a)</td><td>187.66 (n/a)</td><td>162.60 (n/a)</td><td>148.40 (n/a)</td><td>46.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (-15.53%)</td><td>0.24 (-3.52%)</td><td>0.25 (-0.37%)</td><td>0.19 <b>(+34.89%)</b></td><td>0.03 <b>(-51.91%)</b></td><td>212.70 <b>(-25.86%)</b></td><td>175.34 (-2.27%)</td><td>163.40 (+0.37%)</td><td>151.60 (+18.44%)</td><td>24.70 <b>(-60.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>286.90 (n/a)</td><td>179.42 (n/a)</td><td>162.80 (n/a)</td><td>128.00 (n/a)</td><td>62.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (-12.64%)</td><td>0.27 (+12.89%)</td><td>0.28 <b>(+27.37%)</b></td><td>0.23 (+11.50%)</td><td>0.03 <b>(-54.84%)</b></td><td>178.70 (-10.34%)</td><td>152.06 (-14.02%)</td><td>148.70 <b>(-21.45%)</b></td><td>135.00 (+14.50%)</td><td>16.26 <b>(-51.57%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>199.30 (n/a)</td><td>176.86 (n/a)</td><td>189.30 (n/a)</td><td>117.90 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.33 <b>(+31.08%)</b></td><td>0.25 (+13.88%)</td><td>0.29 <b>(+33.57%)</b></td><td>0.12 <b>(-37.77%)</b></td><td>0.09 <b>(+300.50%)</b></td><td>342.00 <b>(+60.71%)</b></td><td>192.34 (+0.92%)</td><td>143.10 <b>(-25.16%)</b></td><td>125.80 <b>(-23.71%)</b></td><td>92.42 <b>(+375.46%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>190.58 (n/a)</td><td>191.20 (n/a)</td><td>164.90 (n/a)</td><td>19.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.34 <b>(+38.37%)</b></td><td>0.26 <b>(+40.00%)</b></td><td>0.27 <b>(+48.30%)</b></td><td>0.16 (+10.95%)</td><td>0.07 <b>(+88.62%)</b></td><td>249.50 (-9.86%)</td><td>168.54 <b>(-25.92%)</b></td><td>154.00 <b>(-32.57%)</b></td><td>122.00 <b>(-27.73%)</b></td><td>51.01 <b>(+25.72%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>276.80 (n/a)</td><td>227.50 (n/a)</td><td>228.40 (n/a)</td><td>168.80 (n/a)</td><td>40.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.33 (+0.42%)</td><td>0.25 (-6.35%)</td><td>0.24 (-6.29%)</td><td>0.21 (-16.35%)</td><td>0.05 <b>(+47.97%)</b></td><td>196.40 (+19.54%)</td><td>166.06 (+8.58%)</td><td>172.60 (+6.67%)</td><td>124.30 (-0.40%)</td><td>29.36 <b>(+76.65%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>164.30 (n/a)</td><td>152.94 (n/a)</td><td>161.80 (n/a)</td><td>124.80 (n/a)</td><td>16.62 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.39 <b>(+28.61%)</b></td><td>0.25 (-9.23%)</td><td>0.26 (-6.53%)</td><td>0.13 <b>(-49.32%)</b></td><td>0.10 <b>(+390.73%)</b></td><td>317.00 <b>(+97.26%)</b></td><td>188.40 <b>(+24.85%)</b></td><td>160.30 (+7.01%)</td><td>105.20 <b>(-22.25%)</b></td><td>79.64 <b>(+667.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>160.70 (n/a)</td><td>150.90 (n/a)</td><td>149.80 (n/a)</td><td>135.30 (n/a)</td><td>10.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (+12.37%)</td><td>0.22 (-2.79%)</td><td>0.24 (+5.62%)</td><td>0.11 <b>(-35.84%)</b></td><td>0.07 <b>(+114.79%)</b></td><td>366.70 <b>(+55.91%)</b></td><td>210.22 (+12.79%)</td><td>171.40 (-5.30%)</td><td>139.10 (-11.00%)</td><td>90.50 <b>(+209.26%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>235.20 (n/a)</td><td>186.38 (n/a)</td><td>181.00 (n/a)</td><td>156.30 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 <b>(-30.12%)</b></td><td>0.20 (-19.46%)</td><td>0.20 (-10.68%)</td><td>0.14 <b>(-29.34%)</b></td><td>0.04 <b>(-34.13%)</b></td><td>294.40 <b>(+41.54%)</b></td><td>210.56 <b>(+23.92%)</b></td><td>200.60 (+11.94%)</td><td>164.30 <b>(+43.12%)</b></td><td>49.94 <b>(+44.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>208.00 (n/a)</td><td>169.92 (n/a)</td><td>179.20 (n/a)</td><td>114.80 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (-2.95%)</td><td>0.19 (-14.98%)</td><td>0.17 <b>(-23.01%)</b></td><td>0.16 (-14.07%)</td><td>0.04 <b>(+26.82%)</b></td><td>214.00 (+16.37%)</td><td>186.80 (+19.19%)</td><td>199.10 <b>(+29.88%)</b></td><td>139.70 (+3.10%)</td><td>32.39 <b>(+55.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>183.90 (n/a)</td><td>156.72 (n/a)</td><td>153.30 (n/a)</td><td>135.50 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (-12.18%)</td><td>0.19 (-4.07%)</td><td>0.19 (-2.87%)</td><td>0.17 (+16.33%)</td><td>0.02 <b>(-45.55%)</b></td><td>203.30 (-14.04%)</td><td>181.14 (+1.46%)</td><td>184.10 (+2.96%)</td><td>149.50 (+13.86%)</td><td>20.85 <b>(-47.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>236.50 (n/a)</td><td>178.54 (n/a)</td><td>178.80 (n/a)</td><td>131.30 (n/a)</td><td>39.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (-14.55%)</td><td>0.21 (-5.09%)</td><td>0.21 (+2.14%)</td><td>0.19 (-1.81%)</td><td>0.02 <b>(-46.84%)</b></td><td>184.50 (+1.82%)</td><td>164.72 (+3.88%)</td><td>165.40 (-2.07%)</td><td>144.70 (+17.07%)</td><td>15.54 <b>(-37.26%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>181.20 (n/a)</td><td>158.56 (n/a)</td><td>168.90 (n/a)</td><td>123.60 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (-11.26%)</td><td>0.19 (+0.99%)</td><td>0.20 (+3.53%)</td><td>0.16 (+6.09%)</td><td>0.02 <b>(-42.85%)</b></td><td>212.30 (-5.73%)</td><td>182.24 (-3.13%)</td><td>177.20 (-3.43%)</td><td>154.90 (+12.65%)</td><td>21.99 <b>(-40.45%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.20 (n/a)</td><td>188.12 (n/a)</td><td>183.50 (n/a)</td><td>137.50 (n/a)</td><td>36.93 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (+2.88%)</td><td>0.20 (-6.63%)</td><td>0.19 (-13.10%)</td><td>0.18 (-1.59%)</td><td>0.03 (+4.92%)</td><td>197.40 (+1.60%)</td><td>175.58 (+7.23%)</td><td>183.00 (+15.09%)</td><td>134.70 (-2.81%)</td><td>25.04 (+2.29%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>163.74 (n/a)</td><td>159.00 (n/a)</td><td>138.60 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (-6.23%)</td><td>0.20 (-14.72%)</td><td>0.19 <b>(-21.34%)</b></td><td>0.17 <b>(-20.00%)</b></td><td>0.03 <b>(+31.77%)</b></td><td>206.10 <b>(+24.98%)</b></td><td>175.04 (+18.45%)</td><td>180.70 <b>(+27.16%)</b></td><td>140.90 (+6.66%)</td><td>25.77 <b>(+71.51%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>164.90 (n/a)</td><td>147.78 (n/a)</td><td>142.10 (n/a)</td><td>132.10 (n/a)</td><td>15.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 <b>(+22.84%)</b></td><td>0.20 (+5.51%)</td><td>0.19 (+4.48%)</td><td>0.14 (+10.38%)</td><td>0.05 <b>(+43.01%)</b></td><td>240.40 (-9.39%)</td><td>187.58 (-3.54%)</td><td>184.40 (-4.31%)</td><td>130.50 (-18.64%)</td><td>46.19 (+7.97%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>265.30 (n/a)</td><td>194.46 (n/a)</td><td>192.70 (n/a)</td><td>160.40 (n/a)</td><td>42.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (-14.30%)</td><td>0.17 (-16.06%)</td><td>0.16 <b>(-27.16%)</b></td><td>0.12 <b>(-23.45%)</b></td><td>0.04 (-4.31%)</td><td>294.30 <b>(+30.63%)</b></td><td>211.50 <b>(+20.53%)</b></td><td>219.00 <b>(+37.22%)</b></td><td>159.90 (+16.63%)</td><td>54.43 <b>(+39.79%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.30 (n/a)</td><td>175.48 (n/a)</td><td>159.60 (n/a)</td><td>137.10 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.87 (-17.96%)</td><td>0.71 <b>(-24.96%)</b></td><td>0.71 <b>(-25.28%)</b></td><td>0.56 <b>(-32.05%)</b></td><td>0.11 <b>(+20.00%)</b></td><td>232.90 <b>(+47.13%)</b></td><td>189.62 <b>(+34.85%)</b></td><td>184.40 <b>(+33.82%)</b></td><td>150.30 <b>(+21.90%)</b></td><td>29.69 <b>(+113.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.06 (n/a)</td><td>0.94 (n/a)</td><td>0.95 (n/a)</td><td>0.83 (n/a)</td><td>0.09 (n/a)</td><td>158.30 (n/a)</td><td>140.62 (n/a)</td><td>137.80 (n/a)</td><td>123.30 (n/a)</td><td>13.90 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.80 <b>(-20.92%)</b></td><td>0.69 <b>(-24.98%)</b></td><td>0.65 <b>(-30.71%)</b></td><td>0.62 (-16.21%)</td><td>0.08 <b>(-26.57%)</b></td><td>212.70 (+19.36%)</td><td>192.04 <b>(+32.97%)</b></td><td>200.20 <b>(+44.34%)</b></td><td>163.60 <b>(+26.53%)</b></td><td>22.35 (+11.09%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.01 (n/a)</td><td>0.92 (n/a)</td><td>0.95 (n/a)</td><td>0.74 (n/a)</td><td>0.11 (n/a)</td><td>178.20 (n/a)</td><td>144.42 (n/a)</td><td>138.70 (n/a)</td><td>129.30 (n/a)</td><td>20.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.86 (-19.09%)</td><td>0.73 (-17.66%)</td><td>0.77 (-11.01%)</td><td>0.52 <b>(-30.10%)</b></td><td>0.13 (-6.61%)</td><td>250.20 <b>(+43.05%)</b></td><td>184.34 <b>(+22.75%)</b></td><td>170.00 (+12.36%)</td><td>153.30 <b>(+23.63%)</b></td><td>38.65 <b>(+69.27%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.06 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.75 (n/a)</td><td>0.14 (n/a)</td><td>174.90 (n/a)</td><td>150.18 (n/a)</td><td>151.30 (n/a)</td><td>124.00 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.00 (+0.00%)</td><td>0.00 (-8.77%)</td><td>0.00 (-9.09%)</td><td>0.00 (-18.18%)</td><td>0.00 <b>(+108.17%)</b></td><td>4627.55 <b>(+28.54%)</b></td><td>4018.43 (+12.80%)</td><td>4075.53 (+13.83%)</td><td>3497.60 (-0.36%)</td><td>434.39 <b>(+981.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>3600.17 (n/a)</td><td>3562.57 (n/a)</td><td>3580.29 (n/a)</td><td>3510.17 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.00 (+0.00%)</td><td>0.00 (-1.85%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-7.24%)</td><td>4577.85 (-1.66%)</td><td>3869.88 (+1.27%)</td><td>3713.49 (+1.59%)</td><td>3548.04 (-0.57%)</td><td>412.17 (-11.94%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4655.18 (n/a)</td><td>3821.51 (n/a)</td><td>3655.29 (n/a)</td><td>3568.53 (n/a)</td><td>468.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (+0.18%)</td><td>0.18 <b>(-21.39%)</b></td><td>0.16 <b>(-42.19%)</b></td><td>0.15 (+2.75%)</td><td>0.05 (-14.87%)</td><td>13696.68 (-2.66%)</td><td>12121.75 <b>(+24.81%)</b></td><td>13112.31 <b>(+72.97%)</b></td><td>7543.78 (-0.19%)</td><td>2572.86 (-15.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.28 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>14070.88 (n/a)</td><td>9712.30 (n/a)</td><td>7580.60 (n/a)</td><td>7558.09 (n/a)</td><td>3045.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.07 (-3.32%)</td><td>5.04 (-2.53%)</td><td>4.57 (-8.79%)</td><td>4.45 (+13.74%)</td><td>0.75 <b>(-29.32%)</b></td><td>235.70 (-12.09%)</td><td>211.54 (+0.78%)</td><td>229.30 (+9.66%)</td><td>172.70 (+3.41%)</td><td>29.42 <b>(-32.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.28 (n/a)</td><td>5.17 (n/a)</td><td>5.01 (n/a)</td><td>3.91 (n/a)</td><td>1.06 (n/a)</td><td>268.10 (n/a)</td><td>209.90 (n/a)</td><td>209.10 (n/a)</td><td>167.00 (n/a)</td><td>43.70 (n/a)</td>
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
