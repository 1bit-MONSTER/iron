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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 <b>(+30.26%)</b></td><td>0.05 (+15.89%)</td><td>0.04 (+11.31%)</td><td>0.04 <b>(+20.43%)</b></td><td>0.01 <b>(+49.50%)</b></td><td>174.70 (-16.97%)</td><td>143.98 (-12.41%)</td><td>152.80 (-10.17%)</td><td>90.60 <b>(-23.22%)</b></td><td>32.75 (-6.91%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>164.38 (n/a)</td><td>170.10 (n/a)</td><td>118.00 (n/a)</td><td>35.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (+14.95%)</td><td>0.04 (-11.79%)</td><td>0.03 (-16.76%)</td><td>0.03 <b>(-22.03%)</b></td><td>0.01 <b>(+194.20%)</b></td><td>209.70 <b>(+28.26%)</b></td><td>177.54 (+17.84%)</td><td>185.10 <b>(+20.12%)</b></td><td>119.20 (-12.99%)</td><td>37.35 <b>(+229.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>163.50 (n/a)</td><td>150.66 (n/a)</td><td>154.10 (n/a)</td><td>137.00 (n/a)</td><td>11.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (+3.58%)</td><td>0.04 (+6.29%)</td><td>0.04 (+14.50%)</td><td>0.03 (+7.71%)</td><td>0.01 (-6.05%)</td><td>201.50 (-7.14%)</td><td>158.70 (-6.56%)</td><td>149.20 (-12.65%)</td><td>126.30 (-3.44%)</td><td>31.65 (-13.61%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>169.84 (n/a)</td><td>170.80 (n/a)</td><td>130.80 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 <b>(+25.10%)</b></td><td>0.04 (+0.85%)</td><td>0.04 (-7.64%)</td><td>0.03 (-5.55%)</td><td>0.01 <b>(+105.04%)</b></td><td>214.90 (+5.86%)</td><td>168.12 (+2.66%)</td><td>172.70 (+8.28%)</td><td>112.50 <b>(-20.10%)</b></td><td>39.39 <b>(+66.72%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.00 (n/a)</td><td>163.76 (n/a)</td><td>159.50 (n/a)</td><td>140.80 (n/a)</td><td>23.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (-2.62%)</td><td>0.04 <b>(+27.99%)</b></td><td>0.04 <b>(+45.91%)</b></td><td>0.03 <b>(+58.89%)</b></td><td>0.00 <b>(-53.90%)</b></td><td>186.10 <b>(-37.04%)</b></td><td>160.88 <b>(-26.55%)</b></td><td>157.20 <b>(-31.47%)</b></td><td>135.80 (+2.72%)</td><td>18.74 <b>(-69.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>295.60 (n/a)</td><td>219.04 (n/a)</td><td>229.40 (n/a)</td><td>132.20 (n/a)</td><td>60.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (+1.74%)</td><td>0.04 (+15.61%)</td><td>0.04 <b>(+22.94%)</b></td><td>0.03 (+12.32%)</td><td>0.01 (-4.23%)</td><td>205.20 (-10.98%)</td><td>160.10 (-14.08%)</td><td>154.60 (-18.63%)</td><td>130.90 (-1.65%)</td><td>31.07 (-16.33%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.50 (n/a)</td><td>186.34 (n/a)</td><td>190.00 (n/a)</td><td>133.10 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+2.53%)</td><td>0.03 (+2.98%)</td><td>0.03 (+19.87%)</td><td>0.02 (-7.36%)</td><td>0.01 (+14.58%)</td><td>246.90 (+7.91%)</td><td>196.88 (-2.07%)</td><td>184.50 (-16.59%)</td><td>159.50 (-2.45%)</td><td>39.61 <b>(+20.75%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.80 (n/a)</td><td>201.04 (n/a)</td><td>221.20 (n/a)</td><td>163.50 (n/a)</td><td>32.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+0.48%)</td><td>0.03 (-1.51%)</td><td>0.03 (-7.34%)</td><td>0.03 (+1.14%)</td><td>0.01 (+10.79%)</td><td>217.40 (-1.09%)</td><td>185.46 (+2.14%)</td><td>204.00 (+7.94%)</td><td>140.00 (-0.43%)</td><td>34.49 (+10.76%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>181.58 (n/a)</td><td>189.00 (n/a)</td><td>140.60 (n/a)</td><td>31.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (+13.07%)</td><td>0.08 (+9.17%)</td><td>0.09 (+16.73%)</td><td>0.06 (-4.19%)</td><td>0.02 <b>(+63.23%)</b></td><td>203.50 (+4.36%)</td><td>158.70 (-5.60%)</td><td>139.80 (-14.34%)</td><td>116.10 (-11.58%)</td><td>39.92 <b>(+57.82%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.00 (n/a)</td><td>168.12 (n/a)</td><td>163.20 (n/a)</td><td>131.30 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (-8.29%)</td><td>0.08 (+6.42%)</td><td>0.08 (+17.95%)</td><td>0.06 <b>(+22.52%)</b></td><td>0.01 <b>(-42.23%)</b></td><td>191.00 (-18.38%)</td><td>153.62 (-10.86%)</td><td>157.10 (-15.22%)</td><td>121.90 (+9.03%)</td><td>26.55 <b>(-47.79%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>234.00 (n/a)</td><td>172.34 (n/a)</td><td>185.30 (n/a)</td><td>111.80 (n/a)</td><td>50.84 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 <b>(+22.42%)</b></td><td>0.08 (+16.34%)</td><td>0.08 (+14.78%)</td><td>0.07 (+14.18%)</td><td>0.01 <b>(+46.38%)</b></td><td>172.80 (-12.42%)</td><td>148.50 (-13.46%)</td><td>152.50 (-12.86%)</td><td>114.30 (-18.36%)</td><td>22.18 (+4.38%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>171.60 (n/a)</td><td>175.00 (n/a)</td><td>140.00 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (+18.35%)</td><td>0.08 (+7.29%)</td><td>0.08 (+2.16%)</td><td>0.06 (-8.65%)</td><td>0.02 <b>(+137.20%)</b></td><td>202.00 (+9.49%)</td><td>158.44 (-3.75%)</td><td>160.60 (-2.13%)</td><td>119.60 (-15.54%)</td><td>35.01 <b>(+117.42%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>164.62 (n/a)</td><td>164.10 (n/a)</td><td>141.60 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 <b>(-24.71%)</b></td><td>0.07 (-6.07%)</td><td>0.07 (+3.97%)</td><td>0.04 (-11.67%)</td><td>0.01 <b>(-37.35%)</b></td><td>274.70 (+13.23%)</td><td>191.52 (+4.29%)</td><td>176.70 (-3.81%)</td><td>155.10 <b>(+32.79%)</b></td><td>47.61 (+1.76%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>242.60 (n/a)</td><td>183.64 (n/a)</td><td>183.70 (n/a)</td><td>116.80 (n/a)</td><td>46.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (+16.17%)</td><td>0.08 <b>(+25.89%)</b></td><td>0.08 <b>(+27.04%)</b></td><td>0.07 <b>(+43.65%)</b></td><td>0.01 <b>(-33.83%)</b></td><td>187.80 <b>(-30.39%)</b></td><td>162.58 <b>(-22.12%)</b></td><td>163.50 <b>(-21.28%)</b></td><td>147.10 (-13.93%)</td><td>15.92 <b>(-59.81%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>269.80 (n/a)</td><td>208.76 (n/a)</td><td>207.70 (n/a)</td><td>170.90 (n/a)</td><td>39.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (+8.09%)</td><td>0.06 (-6.24%)</td><td>0.06 (-6.05%)</td><td>0.05 (-3.74%)</td><td>0.02 <b>(+31.00%)</b></td><td>236.20 (+3.92%)</td><td>200.28 (+8.81%)</td><td>210.20 (+6.43%)</td><td>126.30 (-7.54%)</td><td>44.45 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>184.06 (n/a)</td><td>197.50 (n/a)</td><td>136.60 (n/a)</td><td>35.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (-7.05%)</td><td>0.06 (-1.49%)</td><td>0.06 (+7.19%)</td><td>0.05 (-7.26%)</td><td>0.01 (-0.89%)</td><td>252.20 (+7.82%)</td><td>205.42 (+1.75%)</td><td>195.80 (-6.72%)</td><td>173.80 (+7.62%)</td><td>31.89 (+16.97%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>201.88 (n/a)</td><td>209.90 (n/a)</td><td>161.50 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (-13.68%)</td><td>0.15 (-4.67%)</td><td>0.15 (-13.02%)</td><td>0.15 (+14.00%)</td><td>0.00 <b>(-84.33%)</b></td><td>168.00 (-12.27%)</td><td>160.68 (+2.27%)</td><td>159.00 (+14.97%)</td><td>156.10 (+15.80%)</td><td>4.67 <b>(-83.93%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.50 (n/a)</td><td>157.12 (n/a)</td><td>138.30 (n/a)</td><td>134.80 (n/a)</td><td>29.06 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (-15.38%)</td><td>0.15 (+2.12%)</td><td>0.16 (+7.95%)</td><td>0.12 (+11.82%)</td><td>0.02 <b>(-44.28%)</b></td><td>204.80 (-10.57%)</td><td>162.94 (-5.78%)</td><td>157.80 (-7.39%)</td><td>129.80 (+18.21%)</td><td>26.99 <b>(-38.64%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>229.00 (n/a)</td><td>172.94 (n/a)</td><td>170.40 (n/a)</td><td>109.80 (n/a)</td><td>43.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (-16.14%)</td><td>0.15 (-6.71%)</td><td>0.15 (+1.85%)</td><td>0.11 (-6.87%)</td><td>0.02 <b>(-33.47%)</b></td><td>225.50 (+7.38%)</td><td>172.14 (+5.41%)</td><td>165.50 (-1.78%)</td><td>143.60 (+19.27%)</td><td>32.06 (-11.76%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>210.00 (n/a)</td><td>163.30 (n/a)</td><td>168.50 (n/a)</td><td>120.40 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (+2.14%)</td><td>0.16 (-6.12%)</td><td>0.14 <b>(-25.36%)</b></td><td>0.13 (+9.78%)</td><td>0.03 (-10.73%)</td><td>183.50 (-8.89%)</td><td>160.90 (+5.41%)</td><td>178.70 <b>(+33.96%)</b></td><td>119.80 (-2.04%)</td><td>28.78 (-18.39%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>201.40 (n/a)</td><td>152.64 (n/a)</td><td>133.40 (n/a)</td><td>122.30 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (-5.18%)</td><td>0.13 (-11.28%)</td><td>0.13 (-16.76%)</td><td>0.11 (-15.56%)</td><td>0.02 (+13.43%)</td><td>225.00 (+18.42%)</td><td>190.08 (+13.55%)</td><td>194.90 <b>(+20.16%)</b></td><td>145.20 (+5.52%)</td><td>29.48 <b>(+35.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.00 (n/a)</td><td>167.40 (n/a)</td><td>162.20 (n/a)</td><td>137.60 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 <b>(+37.16%)</b></td><td>0.15 (+5.20%)</td><td>0.15 (-0.86%)</td><td>0.11 (-14.17%)</td><td>0.04 <b>(+250.84%)</b></td><td>221.10 (+16.49%)</td><td>170.50 (-1.11%)</td><td>168.90 (+0.90%)</td><td>115.30 <b>(-27.12%)</b></td><td>37.78 <b>(+185.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>172.42 (n/a)</td><td>167.40 (n/a)</td><td>158.20 (n/a)</td><td>13.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (-6.74%)</td><td>0.13 (-10.97%)</td><td>0.12 (-13.50%)</td><td>0.09 <b>(-31.24%)</b></td><td>0.03 <b>(+63.04%)</b></td><td>276.80 <b>(+45.45%)</b></td><td>199.28 (+16.65%)</td><td>206.00 (+15.67%)</td><td>150.60 (+7.26%)</td><td>51.51 <b>(+143.42%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>170.84 (n/a)</td><td>178.10 (n/a)</td><td>140.40 (n/a)</td><td>21.16 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (+5.59%)</td><td>0.14 (-0.70%)</td><td>0.14 (+3.57%)</td><td>0.10 (-5.43%)</td><td>0.04 <b>(+30.26%)</b></td><td>234.30 (+5.73%)</td><td>181.86 (+2.66%)</td><td>169.90 (-3.47%)</td><td>125.90 (-5.34%)</td><td>42.38 <b>(+33.13%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>221.60 (n/a)</td><td>177.14 (n/a)</td><td>176.00 (n/a)</td><td>133.00 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.38 (+2.05%)</td><td>0.29 (-8.43%)</td><td>0.31 (-5.41%)</td><td>0.15 <b>(-29.81%)</b></td><td>0.09 <b>(+50.72%)</b></td><td>322.70 <b>(+42.47%)</b></td><td>191.66 (+17.61%)</td><td>157.30 (+5.71%)</td><td>129.70 (-2.04%)</td><td>79.85 <b>(+108.43%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>226.50 (n/a)</td><td>162.96 (n/a)</td><td>148.80 (n/a)</td><td>132.40 (n/a)</td><td>38.31 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.44 (+6.08%)</td><td>0.35 (+11.73%)</td><td>0.34 (+13.84%)</td><td>0.26 <b>(+28.29%)</b></td><td>0.06 <b>(-22.56%)</b></td><td>187.50 <b>(-22.04%)</b></td><td>146.20 (-13.49%)</td><td>145.60 (-12.13%)</td><td>111.10 (-5.77%)</td><td>27.58 <b>(-42.70%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>240.50 (n/a)</td><td>169.00 (n/a)</td><td>165.70 (n/a)</td><td>117.90 (n/a)</td><td>48.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.41 (+15.30%)</td><td>0.32 (+5.81%)</td><td>0.32 (+14.23%)</td><td>0.25 (-5.53%)</td><td>0.06 <b>(+56.72%)</b></td><td>193.20 (+5.86%)</td><td>158.76 (-4.19%)</td><td>154.90 (-12.44%)</td><td>119.60 (-13.27%)</td><td>27.12 <b>(+40.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>182.50 (n/a)</td><td>165.70 (n/a)</td><td>176.90 (n/a)</td><td>137.90 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.42 (+12.54%)</td><td>0.33 (+11.68%)</td><td>0.34 (+15.97%)</td><td>0.28 (+11.96%)</td><td>0.05 (+15.87%)</td><td>177.50 (-10.67%)</td><td>149.96 (-10.33%)</td><td>145.40 (-13.76%)</td><td>117.80 (-11.16%)</td><td>23.01 (-7.21%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>198.70 (n/a)</td><td>167.24 (n/a)</td><td>168.60 (n/a)</td><td>132.60 (n/a)</td><td>24.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.35 (+0.11%)</td><td>0.27 (-8.37%)</td><td>0.26 (-13.08%)</td><td>0.23 (-8.35%)</td><td>0.05 (+9.69%)</td><td>218.40 (+9.09%)</td><td>185.36 (+9.60%)</td><td>188.20 (+15.04%)</td><td>139.40 (-0.14%)</td><td>28.75 (+14.11%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>200.20 (n/a)</td><td>169.12 (n/a)</td><td>163.60 (n/a)</td><td>139.60 (n/a)</td><td>25.19 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.36 (-3.00%)</td><td>0.26 (-9.81%)</td><td>0.25 (-18.42%)</td><td>0.20 (-12.38%)</td><td>0.06 (+5.03%)</td><td>243.80 (+14.14%)</td><td>194.76 (+11.71%)</td><td>194.90 <b>(+22.58%)</b></td><td>135.80 (+3.11%)</td><td>41.62 (+17.83%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>213.60 (n/a)</td><td>174.34 (n/a)</td><td>159.00 (n/a)</td><td>131.70 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.34 (+12.38%)</td><td>0.28 (+10.09%)</td><td>0.25 (+5.68%)</td><td>0.25 (+13.39%)</td><td>0.04 (+5.86%)</td><td>199.00 (-11.79%)</td><td>178.88 (-9.35%)</td><td>194.60 (-5.40%)</td><td>145.90 (-10.98%)</td><td>24.73 (-15.52%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>225.60 (n/a)</td><td>197.32 (n/a)</td><td>205.70 (n/a)</td><td>163.90 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.34 (+11.52%)</td><td>0.24 (+9.90%)</td><td>0.22 (+5.42%)</td><td>0.14 (-13.04%)</td><td>0.08 <b>(+27.94%)</b></td><td>363.20 (+14.97%)</td><td>227.68 (-5.64%)</td><td>220.00 (-5.13%)</td><td>144.80 (-10.34%)</td><td>83.68 <b>(+32.16%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>315.90 (n/a)</td><td>241.30 (n/a)</td><td>231.90 (n/a)</td><td>161.50 (n/a)</td><td>63.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (-18.95%)</td><td>0.02 (-12.50%)</td><td>0.02 (-17.24%)</td><td>0.01 (-4.51%)</td><td>0.00 <b>(-34.66%)</b></td><td>187.20 (+4.70%)</td><td>158.96 (+12.72%)</td><td>155.90 <b>(+20.85%)</b></td><td>136.10 <b>(+23.39%)</b></td><td>22.96 (-17.79%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>178.80 (n/a)</td><td>141.02 (n/a)</td><td>129.00 (n/a)</td><td>110.30 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (+9.81%)</td><td>0.01 (-4.04%)</td><td>0.01 (-7.38%)</td><td>0.01 (-15.05%)</td><td>0.00 <b>(+50.01%)</b></td><td>253.90 (+17.71%)</td><td>184.34 (+6.94%)</td><td>177.40 (+7.97%)</td><td>129.70 (-8.92%)</td><td>44.65 <b>(+59.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.70 (n/a)</td><td>172.38 (n/a)</td><td>164.30 (n/a)</td><td>142.40 (n/a)</td><td>27.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (-1.85%)</td><td>0.02 (-7.62%)</td><td>0.02 (-13.45%)</td><td>0.01 (-0.75%)</td><td>0.00 (-10.23%)</td><td>210.70 (+0.77%)</td><td>170.84 (+7.70%)</td><td>169.90 (+15.50%)</td><td>135.10 (+1.89%)</td><td>26.87 (-10.50%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>209.10 (n/a)</td><td>158.62 (n/a)</td><td>147.10 (n/a)</td><td>132.60 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (+8.05%)</td><td>0.02 (+3.26%)</td><td>0.01 (-4.42%)</td><td>0.01 (-2.00%)</td><td>0.00 <b>(+35.03%)</b></td><td>217.00 (+2.07%)</td><td>175.34 (-1.79%)</td><td>185.80 (+4.62%)</td><td>128.50 (-7.42%)</td><td>34.31 <b>(+28.33%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>212.60 (n/a)</td><td>178.54 (n/a)</td><td>177.60 (n/a)</td><td>138.80 (n/a)</td><td>26.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 <b>(+42.93%)</b></td><td>0.02 (+3.36%)</td><td>0.01 (-11.95%)</td><td>0.01 (-7.62%)</td><td>0.00 <b>(+277.06%)</b></td><td>214.70 (+8.27%)</td><td>177.36 (+2.19%)</td><td>195.70 (+13.58%)</td><td>112.20 <b>(-30.05%)</b></td><td>43.92 <b>(+188.86%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>198.30 (n/a)</td><td>173.56 (n/a)</td><td>172.30 (n/a)</td><td>160.40 (n/a)</td><td>15.20 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 <b>(+35.65%)</b></td><td>0.01 (+5.77%)</td><td>0.01 (+0.33%)</td><td>0.01 (-10.43%)</td><td>0.00 <b>(+373.91%)</b></td><td>233.40 (+11.67%)</td><td>190.74 (-1.75%)</td><td>191.50 (-0.31%)</td><td>133.70 <b>(-26.30%)</b></td><td>40.71 <b>(+292.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>194.14 (n/a)</td><td>192.10 (n/a)</td><td>181.40 (n/a)</td><td>10.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (+7.60%)</td><td>0.01 (-10.09%)</td><td>0.01 (-5.44%)</td><td>0.01 <b>(-24.59%)</b></td><td>0.00 <b>(+159.14%)</b></td><td>246.10 <b>(+32.60%)</b></td><td>199.10 (+14.43%)</td><td>190.30 (+5.78%)</td><td>146.80 (-7.03%)</td><td>38.84 <b>(+220.32%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>185.60 (n/a)</td><td>174.00 (n/a)</td><td>179.90 (n/a)</td><td>157.90 (n/a)</td><td>12.12 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.01 (+4.49%)</td><td>0.01 (-2.24%)</td><td>0.01 (-3.08%)</td><td>0.01 <b>(-22.45%)</b></td><td>0.00 <b>(+47.05%)</b></td><td>404.30 <b>(+28.92%)</b></td><td>247.06 (+7.46%)</td><td>218.80 (+3.16%)</td><td>180.10 (-4.25%)</td><td>90.21 <b>(+84.43%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>313.60 (n/a)</td><td>229.90 (n/a)</td><td>212.10 (n/a)</td><td>188.10 (n/a)</td><td>48.91 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+10.34%)</td><td>0.03 (+14.25%)</td><td>0.03 (+1.38%)</td><td>0.03 (+9.49%)</td><td>0.01 <b>(+33.88%)</b></td><td>185.00 (-8.64%)</td><td>155.18 (-11.57%)</td><td>172.10 (-1.38%)</td><td>120.90 (-9.37%)</td><td>29.82 (+9.36%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>175.48 (n/a)</td><td>174.50 (n/a)</td><td>133.40 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-11.37%)</td><td>0.03 (-11.46%)</td><td>0.03 (-16.63%)</td><td>0.02 <b>(-23.74%)</b></td><td>0.01 (+15.73%)</td><td>276.70 <b>(+31.14%)</b></td><td>203.92 (+15.59%)</td><td>204.90 (+19.96%)</td><td>151.70 (+12.79%)</td><td>51.72 <b>(+62.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>176.42 (n/a)</td><td>170.80 (n/a)</td><td>134.50 (n/a)</td><td>31.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+1.02%)</td><td>0.03 (-10.24%)</td><td>0.03 (-15.28%)</td><td>0.02 (-17.61%)</td><td>0.01 <b>(+39.89%)</b></td><td>226.90 <b>(+21.34%)</b></td><td>182.84 (+13.95%)</td><td>184.40 (+17.98%)</td><td>130.60 (-0.99%)</td><td>39.38 <b>(+65.94%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.00 (n/a)</td><td>160.46 (n/a)</td><td>156.30 (n/a)</td><td>131.90 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(-22.52%)</b></td><td>0.03 <b>(-25.62%)</b></td><td>0.02 <b>(-25.53%)</b></td><td>0.01 <b>(-51.47%)</b></td><td>0.01 <b>(+40.14%)</b></td><td>381.70 <b>(+105.99%)</b></td><td>231.48 <b>(+45.55%)</b></td><td>226.90 <b>(+34.26%)</b></td><td>158.40 <b>(+29.10%)</b></td><td>90.31 <b>(+274.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>159.04 (n/a)</td><td>169.00 (n/a)</td><td>122.70 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(-20.36%)</b></td><td>0.03 (-11.76%)</td><td>0.03 (-12.76%)</td><td>0.02 (-7.05%)</td><td>0.00 <b>(-38.12%)</b></td><td>222.50 (+7.59%)</td><td>191.58 (+11.85%)</td><td>186.70 (+14.61%)</td><td>162.00 <b>(+25.58%)</b></td><td>25.85 (-16.15%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>171.28 (n/a)</td><td>162.90 (n/a)</td><td>129.00 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(-32.65%)</b></td><td>0.03 (-19.76%)</td><td>0.03 (-17.12%)</td><td>0.02 (-13.87%)</td><td>0.00 <b>(-72.44%)</b></td><td>213.70 (+16.14%)</td><td>196.26 <b>(+22.48%)</b></td><td>196.90 <b>(+20.65%)</b></td><td>182.30 <b>(+48.45%)</b></td><td>11.55 <b>(-51.46%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>160.24 (n/a)</td><td>163.20 (n/a)</td><td>122.80 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-8.72%)</td><td>0.03 (-10.01%)</td><td>0.03 (-11.40%)</td><td>0.02 (-5.64%)</td><td>0.00 (-13.99%)</td><td>215.50 (+5.95%)</td><td>200.18 (+11.03%)</td><td>199.60 (+12.90%)</td><td>175.10 (+9.57%)</td><td>15.99 (-0.94%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.40 (n/a)</td><td>180.30 (n/a)</td><td>176.80 (n/a)</td><td>159.80 (n/a)</td><td>16.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(-22.83%)</b></td><td>0.02 (-19.19%)</td><td>0.02 (-16.99%)</td><td>0.02 <b>(-21.58%)</b></td><td>0.00 <b>(-29.94%)</b></td><td>273.20 <b>(+27.54%)</b></td><td>226.60 <b>(+23.18%)</b></td><td>231.00 <b>(+20.44%)</b></td><td>182.30 <b>(+29.66%)</b></td><td>34.79 (+14.86%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>183.96 (n/a)</td><td>191.80 (n/a)</td><td>140.60 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (-12.46%)</td><td>0.06 (-9.49%)</td><td>0.06 (-8.83%)</td><td>0.05 (-4.49%)</td><td>0.01 (-7.92%)</td><td>225.40 (+4.69%)</td><td>172.58 (+10.39%)</td><td>161.70 (+9.63%)</td><td>137.50 (+14.30%)</td><td>37.29 (+5.11%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>156.34 (n/a)</td><td>147.50 (n/a)</td><td>120.30 (n/a)</td><td>35.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (-5.57%)</td><td>0.06 (+0.02%)</td><td>0.06 (+8.84%)</td><td>0.04 (-8.22%)</td><td>0.01 (+3.83%)</td><td>253.00 (+8.96%)</td><td>180.00 (+0.72%)</td><td>161.60 (-8.13%)</td><td>153.60 (+5.93%)</td><td>41.54 <b>(+22.08%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.20 (n/a)</td><td>178.72 (n/a)</td><td>175.90 (n/a)</td><td>145.00 (n/a)</td><td>34.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (-6.85%)</td><td>0.05 <b>(-25.16%)</b></td><td>0.06 (-15.52%)</td><td>0.03 <b>(-39.94%)</b></td><td>0.02 <b>(+77.55%)</b></td><td>308.70 <b>(+66.50%)</b></td><td>213.68 <b>(+45.28%)</b></td><td>170.30 (+18.43%)</td><td>136.30 (+7.32%)</td><td>77.60 <b>(+232.21%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>147.08 (n/a)</td><td>143.80 (n/a)</td><td>127.00 (n/a)</td><td>23.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (-3.32%)</td><td>0.06 (-7.97%)</td><td>0.06 (-8.78%)</td><td>0.05 (-4.18%)</td><td>0.01 (-16.82%)</td><td>212.10 (+4.38%)</td><td>173.12 (+7.76%)</td><td>177.30 (+9.58%)</td><td>131.20 (+3.47%)</td><td>29.59 (-9.43%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>160.66 (n/a)</td><td>161.80 (n/a)</td><td>126.80 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (-7.05%)</td><td>0.06 (-9.96%)</td><td>0.06 (-10.47%)</td><td>0.04 <b>(-22.02%)</b></td><td>0.01 <b>(+32.66%)</b></td><td>236.70 <b>(+28.22%)</b></td><td>181.58 (+12.56%)</td><td>177.10 (+11.74%)</td><td>152.70 (+7.61%)</td><td>32.58 <b>(+87.97%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.60 (n/a)</td><td>161.32 (n/a)</td><td>158.50 (n/a)</td><td>141.90 (n/a)</td><td>17.33 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 <b>(+57.25%)</b></td><td>0.06 <b>(+26.40%)</b></td><td>0.05 (+2.68%)</td><td>0.05 <b>(+33.53%)</b></td><td>0.02 <b>(+104.77%)</b></td><td>232.90 <b>(-25.11%)</b></td><td>181.32 (-17.97%)</td><td>192.20 (-2.58%)</td><td>113.20 <b>(-36.37%)</b></td><td>51.39 (-3.63%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.00 (n/a)</td><td>221.04 (n/a)</td><td>197.30 (n/a)</td><td>177.90 (n/a)</td><td>53.33 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 <b>(+23.69%)</b></td><td>0.07 (+11.51%)</td><td>0.07 (+19.91%)</td><td>0.04 (-16.08%)</td><td>0.01 <b>(+135.51%)</b></td><td>237.30 (+19.13%)</td><td>167.58 (-6.93%)</td><td>151.90 (-16.63%)</td><td>126.80 (-19.13%)</td><td>42.97 <b>(+130.91%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>180.06 (n/a)</td><td>182.20 (n/a)</td><td>156.80 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 <b>(-23.83%)</b></td><td>0.05 (-13.68%)</td><td>0.05 (-4.52%)</td><td>0.04 (-11.18%)</td><td>0.01 <b>(-30.63%)</b></td><td>267.20 (+12.55%)</td><td>218.36 (+14.78%)</td><td>195.00 (+4.73%)</td><td>183.50 <b>(+31.26%)</b></td><td>39.15 (+3.31%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>190.24 (n/a)</td><td>186.20 (n/a)</td><td>139.80 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (-0.21%)</td><td>0.13 (-1.97%)</td><td>0.13 (-10.98%)</td><td>0.13 <b>(+32.54%)</b></td><td>0.01 <b>(-47.95%)</b></td><td>165.70 <b>(-24.54%)</b></td><td>157.14 (-0.67%)</td><td>162.10 (+12.34%)</td><td>133.20 (+0.23%)</td><td>13.55 <b>(-61.92%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>219.60 (n/a)</td><td>158.20 (n/a)</td><td>144.30 (n/a)</td><td>132.90 (n/a)</td><td>35.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (-11.84%)</td><td>0.15 (+6.92%)</td><td>0.15 <b>(+21.35%)</b></td><td>0.12 <b>(+33.43%)</b></td><td>0.01 <b>(-60.38%)</b></td><td>168.40 <b>(-25.06%)</b></td><td>141.80 (-10.99%)</td><td>136.90 (-17.58%)</td><td>129.70 (+13.47%)</td><td>15.35 <b>(-64.91%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>224.70 (n/a)</td><td>159.30 (n/a)</td><td>166.10 (n/a)</td><td>114.30 (n/a)</td><td>43.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (-5.34%)</td><td>0.12 (-13.81%)</td><td>0.13 (-11.96%)</td><td>0.06 <b>(-53.03%)</b></td><td>0.04 <b>(+120.97%)</b></td><td>360.20 <b>(+112.88%)</b></td><td>194.44 <b>(+30.46%)</b></td><td>162.20 (+13.59%)</td><td>135.30 (+5.62%)</td><td>94.49 <b>(+396.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>169.20 (n/a)</td><td>149.04 (n/a)</td><td>142.80 (n/a)</td><td>128.10 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (+3.04%)</td><td>0.13 (-0.91%)</td><td>0.13 (+3.00%)</td><td>0.09 <b>(-20.65%)</b></td><td>0.02 <b>(+75.80%)</b></td><td>238.20 <b>(+26.03%)</b></td><td>169.58 (+3.63%)</td><td>158.60 (-2.94%)</td><td>136.30 (-2.92%)</td><td>39.63 <b>(+125.74%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>163.64 (n/a)</td><td>163.40 (n/a)</td><td>140.40 (n/a)</td><td>17.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (-6.04%)</td><td>0.12 (-8.64%)</td><td>0.13 (-1.31%)</td><td>0.10 (-17.37%)</td><td>0.02 <b>(+29.10%)</b></td><td>219.10 <b>(+20.98%)</b></td><td>174.48 (+11.28%)</td><td>162.00 (+1.31%)</td><td>140.60 (+6.43%)</td><td>34.97 <b>(+67.90%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>181.10 (n/a)</td><td>156.80 (n/a)</td><td>159.90 (n/a)</td><td>132.10 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (-19.99%)</td><td>0.12 (-2.96%)</td><td>0.13 (+6.99%)</td><td>0.08 (+17.22%)</td><td>0.02 <b>(-41.56%)</b></td><td>258.10 (-14.68%)</td><td>187.28 (-3.01%)</td><td>163.10 (-6.53%)</td><td>153.10 <b>(+24.98%)</b></td><td>43.73 <b>(-38.25%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>302.50 (n/a)</td><td>193.10 (n/a)</td><td>174.50 (n/a)</td><td>122.50 (n/a)</td><td>70.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (-16.49%)</td><td>0.13 (-5.66%)</td><td>0.13 (+6.60%)</td><td>0.09 (-7.82%)</td><td>0.03 <b>(-27.22%)</b></td><td>222.30 (+8.49%)</td><td>174.98 (+4.33%)</td><td>165.40 (-6.18%)</td><td>121.50 (+19.70%)</td><td>39.43 (+1.05%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>204.90 (n/a)</td><td>167.72 (n/a)</td><td>176.30 (n/a)</td><td>101.50 (n/a)</td><td>39.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (+2.78%)</td><td>0.11 (+2.15%)</td><td>0.10 (+1.72%)</td><td>0.10 (+3.06%)</td><td>0.02 (+4.64%)</td><td>220.50 (-2.99%)</td><td>200.64 (-1.99%)</td><td>214.30 (-1.70%)</td><td>142.50 (-2.66%)</td><td>32.99 (-0.08%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>227.30 (n/a)</td><td>204.72 (n/a)</td><td>218.00 (n/a)</td><td>146.40 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>157.62 (n/a)</td><td>153.00 (n/a)</td><td>116.80 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>159.08 (n/a)</td><td>160.90 (n/a)</td><td>116.50 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>177.60 (n/a)</td><td>158.66 (n/a)</td><td>159.80 (n/a)</td><td>131.50 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>275.00 (n/a)</td><td>207.74 (n/a)</td><td>196.10 (n/a)</td><td>162.20 (n/a)</td><td>48.34 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>292.30 (n/a)</td><td>167.08 (n/a)</td><td>137.50 (n/a)</td><td>115.80 (n/a)</td><td>72.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>341.70 (n/a)</td><td>184.90 (n/a)</td><td>150.80 (n/a)</td><td>114.70 (n/a)</td><td>90.29 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>153.48 (n/a)</td><td>155.00 (n/a)</td><td>125.30 (n/a)</td><td>17.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>174.92 (n/a)</td><td>178.00 (n/a)</td><td>150.70 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.20 (n/a)</td><td>156.44 (n/a)</td><td>156.60 (n/a)</td><td>118.20 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>182.50 (n/a)</td><td>148.34 (n/a)</td><td>146.10 (n/a)</td><td>109.40 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>162.34 (n/a)</td><td>164.80 (n/a)</td><td>151.10 (n/a)</td><td>10.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>232.30 (n/a)</td><td>170.00 (n/a)</td><td>170.60 (n/a)</td><td>118.30 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.41 (+8.63%)</td><td>0.34 (+14.79%)</td><td>0.32 (-1.76%)</td><td>0.28 <b>(+35.00%)</b></td><td>0.06 (-17.89%)</td><td>175.10 <b>(-25.93%)</b></td><td>146.18 (-15.51%)</td><td>151.30 (+1.75%)</td><td>119.20 (-7.95%)</td><td>25.48 <b>(-46.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>236.40 (n/a)</td><td>173.02 (n/a)</td><td>148.70 (n/a)</td><td>129.50 (n/a)</td><td>47.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>248.60 (n/a)</td><td>164.10 (n/a)</td><td>150.80 (n/a)</td><td>112.50 (n/a)</td><td>50.72 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>208.70 (n/a)</td><td>178.18 (n/a)</td><td>176.60 (n/a)</td><td>156.70 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>239.10 (n/a)</td><td>190.96 (n/a)</td><td>176.00 (n/a)</td><td>162.60 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>185.16 (n/a)</td><td>193.40 (n/a)</td><td>108.40 (n/a)</td><td>46.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>165.90 (n/a)</td><td>140.56 (n/a)</td><td>141.30 (n/a)</td><td>113.70 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>175.88 (n/a)</td><td>178.00 (n/a)</td><td>107.90 (n/a)</td><td>46.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>358.60 (n/a)</td><td>226.82 (n/a)</td><td>201.00 (n/a)</td><td>172.60 (n/a)</td><td>75.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>351.40 (n/a)</td><td>213.96 (n/a)</td><td>179.50 (n/a)</td><td>156.70 (n/a)</td><td>78.92 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>248.50 (n/a)</td><td>179.88 (n/a)</td><td>185.20 (n/a)</td><td>119.80 (n/a)</td><td>47.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>168.38 (n/a)</td><td>174.00 (n/a)</td><td>138.50 (n/a)</td><td>20.67 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>313.00 (n/a)</td><td>202.96 (n/a)</td><td>180.00 (n/a)</td><td>113.20 (n/a)</td><td>74.51 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.40 (n/a)</td><td>161.82 (n/a)</td><td>162.10 (n/a)</td><td>123.80 (n/a)</td><td>25.15 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>172.78 (n/a)</td><td>166.50 (n/a)</td><td>145.70 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.80 (n/a)</td><td>179.86 (n/a)</td><td>191.20 (n/a)</td><td>147.60 (n/a)</td><td>20.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>208.82 (n/a)</td><td>212.30 (n/a)</td><td>194.00 (n/a)</td><td>11.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>294.50 (n/a)</td><td>225.62 (n/a)</td><td>215.00 (n/a)</td><td>195.00 (n/a)</td><td>39.57 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.01 (n/a)</td><td>223.90 (n/a)</td><td>214.92 (n/a)</td><td>219.70 (n/a)</td><td>204.10 (n/a)</td><td>9.41 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>245.50 (n/a)</td><td>225.72 (n/a)</td><td>225.10 (n/a)</td><td>207.20 (n/a)</td><td>14.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.70 (n/a)</td><td>150.96 (n/a)</td><td>150.80 (n/a)</td><td>129.90 (n/a)</td><td>15.38 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.20 (n/a)</td><td>175.48 (n/a)</td><td>172.50 (n/a)</td><td>139.40 (n/a)</td><td>29.79 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.70 (n/a)</td><td>170.82 (n/a)</td><td>154.40 (n/a)</td><td>120.70 (n/a)</td><td>45.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>172.78 (n/a)</td><td>176.00 (n/a)</td><td>127.50 (n/a)</td><td>29.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>395.50 (n/a)</td><td>225.46 (n/a)</td><td>200.10 (n/a)</td><td>145.30 (n/a)</td><td>100.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.30 (n/a)</td><td>196.98 (n/a)</td><td>193.40 (n/a)</td><td>133.20 (n/a)</td><td>43.94 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>281.70 (n/a)</td><td>204.96 (n/a)</td><td>203.60 (n/a)</td><td>128.00 (n/a)</td><td>56.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>306.20 (n/a)</td><td>249.14 (n/a)</td><td>218.20 (n/a)</td><td>204.20 (n/a)</td><td>50.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>182.00 (n/a)</td><td>156.28 (n/a)</td><td>165.40 (n/a)</td><td>127.20 (n/a)</td><td>23.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>178.82 (n/a)</td><td>180.00 (n/a)</td><td>144.70 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>273.50 (n/a)</td><td>176.12 (n/a)</td><td>153.40 (n/a)</td><td>122.40 (n/a)</td><td>58.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>179.12 (n/a)</td><td>185.70 (n/a)</td><td>148.00 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.40 (n/a)</td><td>182.10 (n/a)</td><td>164.20 (n/a)</td><td>142.00 (n/a)</td><td>50.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>195.12 (n/a)</td><td>204.60 (n/a)</td><td>157.00 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>174.92 (n/a)</td><td>171.90 (n/a)</td><td>141.80 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>337.50 (n/a)</td><td>225.60 (n/a)</td><td>215.30 (n/a)</td><td>172.80 (n/a)</td><td>65.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.00 (n/a)</td><td>150.04 (n/a)</td><td>132.10 (n/a)</td><td>125.90 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>218.30 (n/a)</td><td>165.90 (n/a)</td><td>153.40 (n/a)</td><td>133.50 (n/a)</td><td>32.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>316.40 (n/a)</td><td>202.48 (n/a)</td><td>178.10 (n/a)</td><td>149.80 (n/a)</td><td>65.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.70 (n/a)</td><td>164.24 (n/a)</td><td>165.80 (n/a)</td><td>126.00 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>242.20 (n/a)</td><td>187.52 (n/a)</td><td>205.90 (n/a)</td><td>128.30 (n/a)</td><td>46.88 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>176.28 (n/a)</td><td>171.20 (n/a)</td><td>148.80 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>228.00 (n/a)</td><td>190.46 (n/a)</td><td>220.80 (n/a)</td><td>129.10 (n/a)</td><td>46.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>197.04 (n/a)</td><td>190.30 (n/a)</td><td>161.90 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>235.00 (n/a)</td><td>180.76 (n/a)</td><td>165.90 (n/a)</td><td>133.60 (n/a)</td><td>43.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>233.00 (n/a)</td><td>165.06 (n/a)</td><td>163.20 (n/a)</td><td>127.70 (n/a)</td><td>41.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.80 (n/a)</td><td>165.66 (n/a)</td><td>157.20 (n/a)</td><td>150.20 (n/a)</td><td>17.19 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>182.40 (n/a)</td><td>154.78 (n/a)</td><td>153.50 (n/a)</td><td>125.90 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>216.60 (n/a)</td><td>171.76 (n/a)</td><td>153.20 (n/a)</td><td>127.50 (n/a)</td><td>41.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.20 (n/a)</td><td>183.72 (n/a)</td><td>186.10 (n/a)</td><td>146.70 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>258.50 (n/a)</td><td>212.82 (n/a)</td><td>222.60 (n/a)</td><td>172.50 (n/a)</td><td>38.57 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>4.28 (-15.27%)</td><td>3.98 (-3.72%)</td><td>4.05 (-1.42%)</td><td>3.47 (+1.56%)</td><td>0.30 <b>(-50.28%)</b></td><td>2712.80 (-1.53%)</td><td>2377.84 (+2.63%)</td><td>2321.00 (+1.44%)</td><td>2196.30 (+18.02%)</td><td>196.57 <b>(-40.75%)</b></td><td>1684.37 (-15.27%)</td><td>1563.67 (-3.72%)</td><td>1593.88 (-1.42%)</td><td>1363.66 (+1.56%)</td><td>119.78 <b>(-50.28%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.05 (n/a)</td><td>4.13 (n/a)</td><td>4.11 (n/a)</td><td>3.41 (n/a)</td><td>0.61 (n/a)</td><td>2755.00 (n/a)</td><td>2316.82 (n/a)</td><td>2288.00 (n/a)</td><td>1860.90 (n/a)</td><td>331.76 (n/a)</td><td>1987.98 (n/a)</td><td>1624.09 (n/a)</td><td>1616.88 (n/a)</td><td>1342.78 (n/a)</td><td>240.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.12 (-8.36%)</td><td>0.96 (+11.03%)</td><td>1.10 <b>(+28.25%)</b></td><td>0.61 (-7.74%)</td><td>0.22 (-0.00%)</td><td>362.50 (+8.40%)</td><td>243.78 (-9.26%)</td><td>201.40 <b>(-22.00%)</b></td><td>197.90 (+9.16%)</td><td>71.07 (+14.69%)</td><td>47.69 (-8.36%)</td><td>40.92 (+11.03%)</td><td>46.87 <b>(+28.25%)</b></td><td>26.04 (-7.74%)</td><td>9.54 (-0.00%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.22 (n/a)</td><td>0.86 (n/a)</td><td>0.86 (n/a)</td><td>0.66 (n/a)</td><td>0.22 (n/a)</td><td>334.40 (n/a)</td><td>268.66 (n/a)</td><td>258.20 (n/a)</td><td>181.30 (n/a)</td><td>61.97 (n/a)</td><td>52.05 (n/a)</td><td>36.85 (n/a)</td><td>36.54 (n/a)</td><td>28.22 (n/a)</td><td>9.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.16 (+1.69%)</td><td>0.91 (-5.55%)</td><td>0.92 (-3.48%)</td><td>0.57 <b>(-21.33%)</b></td><td>0.22 <b>(+30.10%)</b></td><td>385.70 <b>(+27.13%)</b></td><td>258.46 (+9.17%)</td><td>240.70 (+3.62%)</td><td>190.30 (-1.65%)</td><td>75.81 <b>(+70.57%)</b></td><td>49.59 (+1.69%)</td><td>38.67 (-5.55%)</td><td>39.21 (-3.48%)</td><td>24.47 <b>(-21.33%)</b></td><td>9.39 <b>(+30.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.14 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.73 (n/a)</td><td>0.17 (n/a)</td><td>303.40 (n/a)</td><td>236.74 (n/a)</td><td>232.30 (n/a)</td><td>193.50 (n/a)</td><td>44.45 (n/a)</td><td>48.77 (n/a)</td><td>40.94 (n/a)</td><td>40.62 (n/a)</td><td>31.10 (n/a)</td><td>7.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.52 (-0.74%)</td><td>0.52 (-0.38%)</td><td>0.52 (-0.25%)</td><td>0.51 (-0.28%)</td><td>0.00 <b>(-44.12%)</b></td><td>48871.20 (+0.28%)</td><td>48737.48 (+0.38%)</td><td>48748.90 (+0.25%)</td><td>48608.70 (+0.74%)</td><td>109.08 <b>(-43.53%)</b></td><td>353.43 (-0.74%)</td><td>352.50 (-0.38%)</td><td>352.42 (-0.25%)</td><td>351.53 (-0.28%)</td><td>0.79 <b>(-44.12%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48732.90 (n/a)</td><td>48554.78 (n/a)</td><td>48626.10 (n/a)</td><td>48251.30 (n/a)</td><td>193.18 (n/a)</td><td>356.05 (n/a)</td><td>353.83 (n/a)</td><td>353.31 (n/a)</td><td>352.53 (n/a)</td><td>1.41 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (+0.75%)</td><td>0.22 (+0.99%)</td><td>0.21 (+0.49%)</td><td>0.21 (+1.71%)</td><td>0.00 <b>(-34.37%)</b></td><td>117925.70 (-1.68%)</td><td>117008.20 (-0.99%)</td><td>117227.10 (-0.48%)</td><td>115663.40 (-0.74%)</td><td>899.45 <b>(-36.02%)</b></td><td>148.53 (+0.75%)</td><td>146.83 (+0.99%)</td><td>146.55 (+0.49%)</td><td>145.68 (+1.71%)</td><td>1.13 <b>(-34.37%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119939.60 (n/a)</td><td>118173.50 (n/a)</td><td>117796.50 (n/a)</td><td>116526.60 (n/a)</td><td>1405.78 (n/a)</td><td>147.43 (n/a)</td><td>145.39 (n/a)</td><td>145.84 (n/a)</td><td>143.24 (n/a)</td><td>1.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.89 (-0.46%)</td><td>0.88 (-0.17%)</td><td>0.88 (+0.02%)</td><td>0.87 (-0.03%)</td><td>0.01 (-13.94%)</td><td>28833.80 (+0.03%)</td><td>28648.94 (+0.17%)</td><td>28636.60 (-0.02%)</td><td>28372.70 (+0.46%)</td><td>187.14 (-13.33%)</td><td>605.51 (-0.46%)</td><td>599.69 (-0.17%)</td><td>599.93 (+0.02%)</td><td>595.82 (-0.03%)</td><td>3.93 (-13.94%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28826.30 (n/a)</td><td>28601.10 (n/a)</td><td>28642.00 (n/a)</td><td>28242.50 (n/a)</td><td>215.91 (n/a)</td><td>608.30 (n/a)</td><td>600.70 (n/a)</td><td>599.81 (n/a)</td><td>595.98 (n/a)</td><td>4.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.48 (-1.00%)</td><td>3.38 (+0.33%)</td><td>3.36 (+0.98%)</td><td>3.34 (+2.44%)</td><td>0.06 <b>(-52.69%)</b></td><td>7543.90 (-2.38%)</td><td>7439.82 (-0.41%)</td><td>7484.50 (-0.97%)</td><td>7234.60 (+1.01%)</td><td>126.36 <b>(-53.30%)</b></td><td>2374.67 (-1.00%)</td><td>2309.71 (+0.33%)</td><td>2295.41 (+0.98%)</td><td>2277.30 (+2.44%)</td><td>39.80 <b>(-52.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.51 (n/a)</td><td>3.37 (n/a)</td><td>3.33 (n/a)</td><td>3.26 (n/a)</td><td>0.12 (n/a)</td><td>7728.00 (n/a)</td><td>7470.30 (n/a)</td><td>7557.60 (n/a)</td><td>7162.30 (n/a)</td><td>270.59 (n/a)</td><td>2398.65 (n/a)</td><td>2302.19 (n/a)</td><td>2273.18 (n/a)</td><td>2223.07 (n/a)</td><td>84.12 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>2.99 (+1.76%)</td><td>2.85 (+1.63%)</td><td>2.84 (+0.76%)</td><td>2.74 (+3.03%)</td><td>0.09 (-10.92%)</td><td>9191.70 (-2.94%)</td><td>8824.96 (-1.63%)</td><td>8849.50 (-0.75%)</td><td>8410.50 (-1.73%)</td><td>280.93 (-15.54%)</td><td>2042.68 (+1.76%)</td><td>1948.33 (+1.63%)</td><td>1941.34 (+0.76%)</td><td>1869.07 (+3.03%)</td><td>62.61 (-10.92%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>2.94 (n/a)</td><td>2.81 (n/a)</td><td>2.82 (n/a)</td><td>2.66 (n/a)</td><td>0.10 (n/a)</td><td>9470.10 (n/a)</td><td>8971.04 (n/a)</td><td>8916.70 (n/a)</td><td>8558.40 (n/a)</td><td>332.61 (n/a)</td><td>2007.37 (n/a)</td><td>1917.12 (n/a)</td><td>1926.72 (n/a)</td><td>1814.12 (n/a)</td><td>70.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.42 (+7.12%)</td><td>3.24 (+2.08%)</td><td>3.16 (-0.35%)</td><td>3.14 (-0.10%)</td><td>0.13 <b>(+565.82%)</b></td><td>8014.70 (+0.10%)</td><td>7787.98 (-1.92%)</td><td>7963.10 (+0.35%)</td><td>7349.90 (-6.65%)</td><td>298.23 <b>(+525.28%)</b></td><td>2337.42 (+7.12%)</td><td>2208.59 (+2.08%)</td><td>2157.44 (-0.35%)</td><td>2143.55 (-0.10%)</td><td>86.57 <b>(+565.82%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.20 (n/a)</td><td>3.17 (n/a)</td><td>3.17 (n/a)</td><td>3.14 (n/a)</td><td>0.02 (n/a)</td><td>8006.30 (n/a)</td><td>7940.44 (n/a)</td><td>7935.60 (n/a)</td><td>7873.20 (n/a)</td><td>47.70 (n/a)</td><td>2182.07 (n/a)</td><td>2163.65 (n/a)</td><td>2164.91 (n/a)</td><td>2145.79 (n/a)</td><td>13.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.78 (-0.39%)</td><td>0.78 (-0.10%)</td><td>0.78 (-0.01%)</td><td>0.78 (-0.03%)</td><td>0.00 <b>(-81.70%)</b></td><td>96495.80 (+0.03%)</td><td>96459.82 (+0.10%)</td><td>96452.20 (+0.01%)</td><td>96413.50 (+0.39%)</td><td>33.85 <b>(-81.62%)</b></td><td>712.76 (-0.39%)</td><td>712.42 (-0.10%)</td><td>712.47 (-0.01%)</td><td>712.15 (-0.03%)</td><td>0.25 <b>(-81.70%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96467.20 (n/a)</td><td>96365.40 (n/a)</td><td>96446.70 (n/a)</td><td>96037.30 (n/a)</td><td>184.20 (n/a)</td><td>715.55 (n/a)</td><td>713.12 (n/a)</td><td>712.51 (n/a)</td><td>712.36 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.73 (+0.20%)</td><td>0.73 (+0.07%)</td><td>0.73 (+0.04%)</td><td>0.73 (+0.05%)</td><td>0.00 <b>(+143.07%)</b></td><td>103696.10 (-0.05%)</td><td>103601.64 (-0.07%)</td><td>103613.90 (-0.04%)</td><td>103430.50 (-0.20%)</td><td>103.13 <b>(+142.49%)</b></td><td>664.40 (+0.20%)</td><td>663.31 (+0.07%)</td><td>663.23 (+0.04%)</td><td>662.70 (+0.05%)</td><td>0.66 <b>(+143.06%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103743.20 (n/a)</td><td>103672.94 (n/a)</td><td>103659.80 (n/a)</td><td>103635.00 (n/a)</td><td>42.53 (n/a)</td><td>663.09 (n/a)</td><td>662.85 (n/a)</td><td>662.93 (n/a)</td><td>662.40 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.69 (-0.02%)</td><td>0.69 (-0.53%)</td><td>0.69 (-0.60%)</td><td>0.68 (-0.79%)</td><td>0.00 <b>(+104.94%)</b></td><td>110295.90 (+0.80%)</td><td>109620.18 (+0.53%)</td><td>109525.70 (+0.61%)</td><td>108832.80 (+0.02%)</td><td>588.32 <b>(+106.73%)</b></td><td>631.42 (-0.02%)</td><td>626.90 (-0.53%)</td><td>627.43 (-0.60%)</td><td>623.05 (-0.79%)</td><td>3.37 <b>(+104.94%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109424.30 (n/a)</td><td>109039.56 (n/a)</td><td>108865.60 (n/a)</td><td>108811.10 (n/a)</td><td>284.58 (n/a)</td><td>631.55 (n/a)</td><td>630.23 (n/a)</td><td>631.23 (n/a)</td><td>628.01 (n/a)</td><td>1.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>7.52 (-2.41%)</td><td>6.28 (-13.69%)</td><td>6.33 (-16.15%)</td><td>4.46 <b>(-34.01%)</b></td><td>1.14 <b>(+149.77%)</b></td><td>1997.40 <b>(+51.55%)</b></td><td>1464.02 (+19.17%)</td><td>1407.40 (+19.26%)</td><td>1185.50 (+2.46%)</td><td>314.53 <b>(+298.57%)</b></td><td>452.86 (-2.41%)</td><td>378.42 (-13.69%)</td><td>381.47 (-16.15%)</td><td>268.78 <b>(-34.01%)</b></td><td>68.90 <b>(+149.77%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.70 (n/a)</td><td>7.28 (n/a)</td><td>7.55 (n/a)</td><td>6.76 (n/a)</td><td>0.46 (n/a)</td><td>1318.00 (n/a)</td><td>1228.54 (n/a)</td><td>1180.10 (n/a)</td><td>1157.00 (n/a)</td><td>78.92 (n/a)</td><td>464.04 (n/a)</td><td>438.42 (n/a)</td><td>454.95 (n/a)</td><td>407.34 (n/a)</td><td>27.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.97 (-1.47%)</td><td>6.43 (-5.25%)</td><td>6.75 (-0.38%)</td><td>4.79 <b>(-26.59%)</b></td><td>0.93 <b>(+250.96%)</b></td><td>1861.80 <b>(+36.23%)</b></td><td>1414.38 (+7.61%)</td><td>1319.90 (+0.38%)</td><td>1278.80 (+1.49%)</td><td>250.93 <b>(+391.64%)</b></td><td>419.84 (-1.47%)</td><td>387.49 (-5.25%)</td><td>406.75 (-0.38%)</td><td>288.36 <b>(-26.59%)</b></td><td>55.79 <b>(+250.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.07 (n/a)</td><td>6.79 (n/a)</td><td>6.78 (n/a)</td><td>6.52 (n/a)</td><td>0.26 (n/a)</td><td>1366.70 (n/a)</td><td>1314.40 (n/a)</td><td>1314.90 (n/a)</td><td>1260.00 (n/a)</td><td>51.04 (n/a)</td><td>426.10 (n/a)</td><td>408.95 (n/a)</td><td>408.31 (n/a)</td><td>392.83 (n/a)</td><td>15.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.93 (+4.97%)</td><td>6.37 (-0.86%)</td><td>6.90 (+6.62%)</td><td>4.66 <b>(-23.57%)</b></td><td>0.98 <b>(+410.67%)</b></td><td>1911.00 <b>(+30.84%)</b></td><td>1431.42 (+3.18%)</td><td>1292.30 (-6.21%)</td><td>1286.80 (-4.73%)</td><td>270.85 <b>(+536.14%)</b></td><td>417.22 (+4.97%)</td><td>383.95 (-0.86%)</td><td>415.45 (+6.62%)</td><td>280.94 <b>(-23.57%)</b></td><td>58.75 <b>(+410.67%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.60 (n/a)</td><td>6.43 (n/a)</td><td>6.47 (n/a)</td><td>6.10 (n/a)</td><td>0.19 (n/a)</td><td>1460.60 (n/a)</td><td>1387.34 (n/a)</td><td>1377.90 (n/a)</td><td>1350.70 (n/a)</td><td>42.58 (n/a)</td><td>397.49 (n/a)</td><td>387.26 (n/a)</td><td>389.64 (n/a)</td><td>367.58 (n/a)</td><td>11.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>8.26 (-2.74%)</td><td>7.81 (-0.20%)</td><td>7.96 (-1.33%)</td><td>7.38 (+5.09%)</td><td>0.37 <b>(-49.32%)</b></td><td>4723.10 (-4.84%)</td><td>4474.74 (-0.35%)</td><td>4382.40 (+1.35%)</td><td>4222.10 (+2.82%)</td><td>215.66 <b>(-50.29%)</b></td><td>508.63 (-2.74%)</td><td>480.80 (-0.20%)</td><td>490.03 (-1.33%)</td><td>454.68 (+5.09%)</td><td>23.05 <b>(-49.32%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.49 (n/a)</td><td>7.82 (n/a)</td><td>8.06 (n/a)</td><td>7.02 (n/a)</td><td>0.74 (n/a)</td><td>4963.30 (n/a)</td><td>4490.28 (n/a)</td><td>4324.20 (n/a)</td><td>4106.50 (n/a)</td><td>433.89 (n/a)</td><td>522.94 (n/a)</td><td>481.76 (n/a)</td><td>496.61 (n/a)</td><td>432.67 (n/a)</td><td>45.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>7.79 (-0.99%)</td><td>7.66 (+1.68%)</td><td>7.65 (+1.67%)</td><td>7.54 (+5.41%)</td><td>0.09 <b>(-72.28%)</b></td><td>4621.30 (-5.14%)</td><td>4554.82 (-1.80%)</td><td>4556.30 (-1.65%)</td><td>4475.80 (+1.00%)</td><td>55.35 <b>(-73.35%)</b></td><td>479.80 (-0.99%)</td><td>471.53 (+1.68%)</td><td>471.32 (+1.67%)</td><td>464.69 (+5.41%)</td><td>5.75 <b>(-72.28%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.87 (n/a)</td><td>7.53 (n/a)</td><td>7.53 (n/a)</td><td>7.16 (n/a)</td><td>0.34 (n/a)</td><td>4871.60 (n/a)</td><td>4638.44 (n/a)</td><td>4632.60 (n/a)</td><td>4431.30 (n/a)</td><td>207.72 (n/a)</td><td>484.62 (n/a)</td><td>463.72 (n/a)</td><td>463.56 (n/a)</td><td>440.82 (n/a)</td><td>20.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>7.74 (+0.62%)</td><td>7.54 (+1.94%)</td><td>7.53 (+1.16%)</td><td>7.36 (+7.95%)</td><td>0.16 <b>(-53.41%)</b></td><td>4738.50 (-7.37%)</td><td>4624.48 (-2.05%)</td><td>4628.70 (-1.14%)</td><td>4502.20 (-0.61%)</td><td>100.22 <b>(-57.28%)</b></td><td>476.98 (+0.62%)</td><td>464.55 (+1.94%)</td><td>463.95 (+1.16%)</td><td>453.20 (+7.95%)</td><td>10.09 <b>(-53.41%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.70 (n/a)</td><td>7.40 (n/a)</td><td>7.45 (n/a)</td><td>6.82 (n/a)</td><td>0.35 (n/a)</td><td>5115.30 (n/a)</td><td>4721.26 (n/a)</td><td>4682.20 (n/a)</td><td>4530.00 (n/a)</td><td>234.62 (n/a)</td><td>474.05 (n/a)</td><td>455.71 (n/a)</td><td>458.65 (n/a)</td><td>419.81 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.79 (+0.01%)</td><td>0.79 (+0.07%)</td><td>0.79 (+0.13%)</td><td>0.79 (+0.09%)</td><td>0.00 <b>(-31.94%)</b></td><td>95847.90 (-0.09%)</td><td>95780.60 (-0.07%)</td><td>95755.40 (-0.13%)</td><td>95727.30 (-0.01%)</td><td>54.28 <b>(-32.01%)</b></td><td>717.87 (+0.01%)</td><td>717.47 (+0.07%)</td><td>717.66 (+0.13%)</td><td>716.96 (+0.09%)</td><td>0.41 <b>(-31.94%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95930.20 (n/a)</td><td>95845.88 (n/a)</td><td>95876.00 (n/a)</td><td>95735.80 (n/a)</td><td>79.83 (n/a)</td><td>717.80 (n/a)</td><td>716.98 (n/a)</td><td>716.75 (n/a)</td><td>716.35 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.74 (+0.35%)</td><td>0.73 (+0.07%)</td><td>0.73 (+0.04%)</td><td>0.73 (-0.02%)</td><td>0.00 <b>(+511.02%)</b></td><td>102985.90 (+0.02%)</td><td>102856.98 (-0.07%)</td><td>102898.80 (-0.04%)</td><td>102535.00 (-0.35%)</td><td>184.73 <b>(+509.14%)</b></td><td>670.21 (+0.35%)</td><td>668.11 (+0.07%)</td><td>667.84 (+0.04%)</td><td>667.27 (-0.02%)</td><td>1.20 <b>(+510.97%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102965.20 (n/a)</td><td>102930.34 (n/a)</td><td>102939.30 (n/a)</td><td>102897.60 (n/a)</td><td>30.33 (n/a)</td><td>667.84 (n/a)</td><td>667.63 (n/a)</td><td>667.57 (n/a)</td><td>667.40 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.70 (-0.02%)</td><td>0.70 (-0.09%)</td><td>0.70 (-0.07%)</td><td>0.70 (-0.08%)</td><td>0.00 (+6.08%)</td><td>108372.70 (+0.08%)</td><td>107985.48 (+0.09%)</td><td>107973.90 (+0.07%)</td><td>107649.20 (+0.02%)</td><td>263.38 (+6.19%)</td><td>638.37 (-0.02%)</td><td>636.38 (-0.09%)</td><td>636.45 (-0.07%)</td><td>634.10 (-0.08%)</td><td>1.55 (+6.08%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108281.40 (n/a)</td><td>107889.08 (n/a)</td><td>107898.40 (n/a)</td><td>107632.00 (n/a)</td><td>248.02 (n/a)</td><td>638.47 (n/a)</td><td>636.95 (n/a)</td><td>636.89 (n/a)</td><td>634.64 (n/a)</td><td>1.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>4.29 (+3.51%)</td><td>3.40 (-6.88%)</td><td>3.17 (-14.90%)</td><td>2.92 (-8.36%)</td><td>0.57 <b>(+28.91%)</b></td><td>2761.40 (+9.12%)</td><td>2422.44 (+8.30%)</td><td>2539.20 (+17.51%)</td><td>1879.80 (-3.40%)</td><td>367.80 <b>(+33.72%)</b></td><td>1124.53 (+3.51%)</td><td>890.67 (-6.88%)</td><td>832.50 (-14.90%)</td><td>765.52 (-8.36%)</td><td>149.24 <b>(+28.91%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>4.14 (n/a)</td><td>3.65 (n/a)</td><td>3.73 (n/a)</td><td>3.19 (n/a)</td><td>0.44 (n/a)</td><td>2530.60 (n/a)</td><td>2236.72 (n/a)</td><td>2160.80 (n/a)</td><td>1945.90 (n/a)</td><td>275.05 (n/a)</td><td>1086.36 (n/a)</td><td>956.48 (n/a)</td><td>978.30 (n/a)</td><td>835.36 (n/a)</td><td>115.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.40 (+10.34%)</td><td>0.33 (+3.25%)</td><td>0.33 (+2.15%)</td><td>0.29 (+0.46%)</td><td>0.04 <b>(+28.14%)</b></td><td>4333.90 (-0.45%)</td><td>3790.00 (-2.81%)</td><td>3759.20 (-2.11%)</td><td>3135.40 (-9.37%)</td><td>437.73 (+13.24%)</td><td>21.40 (+10.34%)</td><td>17.91 (+3.25%)</td><td>17.85 (+2.15%)</td><td>15.48 (+0.46%)</td><td>2.19 <b>(+28.14%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>4353.70 (n/a)</td><td>3899.52 (n/a)</td><td>3840.10 (n/a)</td><td>3459.50 (n/a)</td><td>386.56 (n/a)</td><td>19.40 (n/a)</td><td>17.35 (n/a)</td><td>17.48 (n/a)</td><td>15.41 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.59 (+2.88%)</td><td>4.81 (+5.33%)</td><td>4.60 (-2.18%)</td><td>3.63 (+10.22%)</td><td>1.16 (-6.82%)</td><td>1833.10 (-9.27%)</td><td>1443.16 (-6.41%)</td><td>1447.50 (+2.23%)</td><td>1009.60 (-2.80%)</td><td>321.07 <b>(-20.33%)</b></td><td>2035.71 (+2.88%)</td><td>1486.89 (+5.33%)</td><td>1419.79 (-2.18%)</td><td>1121.18 (+10.22%)</td><td>358.62 (-6.82%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.40 (n/a)</td><td>4.57 (n/a)</td><td>4.70 (n/a)</td><td>3.29 (n/a)</td><td>1.25 (n/a)</td><td>2020.40 (n/a)</td><td>1542.00 (n/a)</td><td>1415.90 (n/a)</td><td>1038.70 (n/a)</td><td>402.99 (n/a)</td><td>1978.65 (n/a)</td><td>1411.69 (n/a)</td><td>1451.49 (n/a)</td><td>1017.23 (n/a)</td><td>384.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.30 (+14.20%)</td><td>0.22 (+0.63%)</td><td>0.20 (-13.99%)</td><td>0.20 (+9.66%)</td><td>0.04 <b>(+27.55%)</b></td><td>0.29 (+14.20%)</td><td>0.22 (+0.63%)</td><td>0.20 (-13.99%)</td><td>0.19 (+9.66%)</td><td>0.04 <b>(+27.55%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>13.58 (+0.15%)</td><td>12.80 (-2.38%)</td><td>13.16 (-0.21%)</td><td>11.38 (-8.64%)</td><td>0.86 <b>(+114.32%)</b></td><td>13.57 (+0.15%)</td><td>12.79 (-2.38%)</td><td>13.15 (-0.21%)</td><td>11.38 (-8.64%)</td><td>0.86 <b>(+114.32%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>13.56 (n/a)</td><td>13.11 (n/a)</td><td>13.19 (n/a)</td><td>12.46 (n/a)</td><td>0.40 (n/a)</td><td>13.55 (n/a)</td><td>13.10 (n/a)</td><td>13.18 (n/a)</td><td>12.45 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>24.79 (-1.19%)</td><td>24.11 (-0.16%)</td><td>24.58 (+1.11%)</td><td>22.62 (-0.99%)</td><td>0.90 (+4.91%)</td><td>24.77 (-1.19%)</td><td>24.10 (-0.16%)</td><td>24.57 (+1.11%)</td><td>22.61 (-0.99%)</td><td>0.90 (+4.91%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>25.08 (n/a)</td><td>24.15 (n/a)</td><td>24.31 (n/a)</td><td>22.85 (n/a)</td><td>0.86 (n/a)</td><td>25.07 (n/a)</td><td>24.14 (n/a)</td><td>24.30 (n/a)</td><td>22.83 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>41.14 (-0.35%)</td><td>38.83 (-2.04%)</td><td>39.31 (+1.42%)</td><td>34.68 (-9.75%)</td><td>2.54 <b>(+82.83%)</b></td><td>41.12 (-0.35%)</td><td>38.80 (-2.04%)</td><td>39.28 (+1.42%)</td><td>34.66 (-9.75%)</td><td>2.54 <b>(+82.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>41.28 (n/a)</td><td>39.64 (n/a)</td><td>38.76 (n/a)</td><td>38.43 (n/a)</td><td>1.39 (n/a)</td><td>41.26 (n/a)</td><td>39.61 (n/a)</td><td>38.73 (n/a)</td><td>38.40 (n/a)</td><td>1.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>42.47 (-3.34%)</td><td>41.21 (-2.89%)</td><td>41.83 (-1.07%)</td><td>38.48 (-6.99%)</td><td>1.57 <b>(+55.68%)</b></td><td>42.44 (-3.34%)</td><td>41.18 (-2.89%)</td><td>41.80 (-1.07%)</td><td>38.45 (-6.99%)</td><td>1.57 <b>(+55.68%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>43.94 (n/a)</td><td>42.44 (n/a)</td><td>42.28 (n/a)</td><td>41.37 (n/a)</td><td>1.01 (n/a)</td><td>43.91 (n/a)</td><td>42.41 (n/a)</td><td>42.25 (n/a)</td><td>41.34 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>13.26 (+0.65%)</td><td>12.57 (-1.03%)</td><td>13.13 (+0.10%)</td><td>11.16 (+1.80%)</td><td>0.91 (-5.97%)</td><td>13.25 (+0.65%)</td><td>12.56 (-1.03%)</td><td>13.12 (+0.10%)</td><td>11.15 (+1.80%)</td><td>0.91 (-5.97%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>13.17 (n/a)</td><td>12.70 (n/a)</td><td>13.12 (n/a)</td><td>10.96 (n/a)</td><td>0.97 (n/a)</td><td>13.17 (n/a)</td><td>12.69 (n/a)</td><td>13.11 (n/a)</td><td>10.96 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>24.68 (-0.57%)</td><td>24.22 (+1.15%)</td><td>24.13 (+0.61%)</td><td>23.79 (+4.48%)</td><td>0.38 <b>(-50.53%)</b></td><td>24.67 (-0.57%)</td><td>24.20 (+1.15%)</td><td>24.12 (+0.61%)</td><td>23.77 (+4.48%)</td><td>0.38 <b>(-50.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>24.82 (n/a)</td><td>23.94 (n/a)</td><td>23.99 (n/a)</td><td>22.77 (n/a)</td><td>0.77 (n/a)</td><td>24.81 (n/a)</td><td>23.93 (n/a)</td><td>23.97 (n/a)</td><td>22.75 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>43.19 (+4.70%)</td><td>40.75 (+2.21%)</td><td>39.92 (+0.54%)</td><td>39.10 (+0.26%)</td><td>1.78 <b>(+101.76%)</b></td><td>43.17 (+4.70%)</td><td>40.72 (+2.21%)</td><td>39.90 (+0.54%)</td><td>39.08 (+0.26%)</td><td>1.78 <b>(+101.76%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>41.25 (n/a)</td><td>39.87 (n/a)</td><td>39.70 (n/a)</td><td>39.00 (n/a)</td><td>0.88 (n/a)</td><td>41.23 (n/a)</td><td>39.84 (n/a)</td><td>39.68 (n/a)</td><td>38.98 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>45.48 (+4.59%)</td><td>43.36 (+11.50%)</td><td>42.74 (-0.06%)</td><td>41.24 <b>(+79.96%)</b></td><td>1.81 <b>(-79.79%)</b></td><td>45.45 (+4.59%)</td><td>43.33 (+11.50%)</td><td>42.71 (-0.06%)</td><td>41.22 <b>(+79.96%)</b></td><td>1.81 <b>(-79.79%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>43.48 (n/a)</td><td>38.89 (n/a)</td><td>42.77 (n/a)</td><td>22.92 (n/a)</td><td>8.94 (n/a)</td><td>43.45 (n/a)</td><td>38.86 (n/a)</td><td>42.74 (n/a)</td><td>22.90 (n/a)</td><td>8.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>373.60 (n/a)</td><td>195.98 (n/a)</td><td>155.70 (n/a)</td><td>138.70 (n/a)</td><td>99.66 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>286.80 (n/a)</td><td>186.36 (n/a)</td><td>163.50 (n/a)</td><td>137.00 (n/a)</td><td>58.45 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>169.52 (n/a)</td><td>162.30 (n/a)</td><td>125.60 (n/a)</td><td>42.91 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.80 (n/a)</td><td>184.84 (n/a)</td><td>179.30 (n/a)</td><td>164.90 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>185.82 (n/a)</td><td>188.00 (n/a)</td><td>156.00 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>177.34 (n/a)</td><td>194.90 (n/a)</td><td>133.50 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.20 (n/a)</td><td>178.38 (n/a)</td><td>190.20 (n/a)</td><td>130.70 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.80 (n/a)</td><td>219.70 (n/a)</td><td>219.50 (n/a)</td><td>189.70 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>163.02 (n/a)</td><td>161.20 (n/a)</td><td>141.70 (n/a)</td><td>22.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>185.50 (n/a)</td><td>196.20 (n/a)</td><td>136.00 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>197.80 (n/a)</td><td>208.80 (n/a)</td><td>145.40 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>185.00 (n/a)</td><td>179.60 (n/a)</td><td>131.20 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>181.80 (n/a)</td><td>179.60 (n/a)</td><td>149.90 (n/a)</td><td>32.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>300.20 (n/a)</td><td>209.60 (n/a)</td><td>203.50 (n/a)</td><td>149.30 (n/a)</td><td>55.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>188.40 (n/a)</td><td>191.00 (n/a)</td><td>156.70 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>372.70 (n/a)</td><td>256.24 (n/a)</td><td>231.80 (n/a)</td><td>213.50 (n/a)</td><td>65.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>194.98 (n/a)</td><td>194.40 (n/a)</td><td>191.50 (n/a)</td><td>3.49 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>172.08 (n/a)</td><td>170.80 (n/a)</td><td>135.20 (n/a)</td><td>23.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>280.10 (n/a)</td><td>196.62 (n/a)</td><td>183.90 (n/a)</td><td>152.30 (n/a)</td><td>50.38 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>251.20 (n/a)</td><td>201.64 (n/a)</td><td>181.70 (n/a)</td><td>157.70 (n/a)</td><td>44.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.70 (n/a)</td><td>169.40 (n/a)</td><td>160.20 (n/a)</td><td>156.10 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>166.30 (n/a)</td><td>171.50 (n/a)</td><td>131.40 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.70 (n/a)</td><td>162.96 (n/a)</td><td>162.70 (n/a)</td><td>125.20 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>214.12 (n/a)</td><td>223.90 (n/a)</td><td>174.70 (n/a)</td><td>22.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (-15.13%)</td><td>0.18 (+1.58%)</td><td>0.18 (+5.26%)</td><td>0.17 (+16.36%)</td><td>0.01 <b>(-75.54%)</b></td><td>191.80 (-14.07%)</td><td>182.48 (-3.53%)</td><td>181.40 (-4.98%)</td><td>174.40 (+17.84%)</td><td>7.47 <b>(-75.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.20 (n/a)</td><td>189.16 (n/a)</td><td>190.90 (n/a)</td><td>148.00 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.60 (n/a)</td><td>157.78 (n/a)</td><td>163.00 (n/a)</td><td>128.40 (n/a)</td><td>20.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>178.88 (n/a)</td><td>173.10 (n/a)</td><td>161.50 (n/a)</td><td>14.79 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>166.60 (n/a)</td><td>154.10 (n/a)</td><td>162.90 (n/a)</td><td>136.90 (n/a)</td><td>14.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>211.90 (n/a)</td><td>169.64 (n/a)</td><td>166.50 (n/a)</td><td>117.80 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>335.80 (n/a)</td><td>212.76 (n/a)</td><td>191.90 (n/a)</td><td>159.60 (n/a)</td><td>71.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>280.80 (n/a)</td><td>218.86 (n/a)</td><td>219.10 (n/a)</td><td>147.90 (n/a)</td><td>52.17 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>321.90 (n/a)</td><td>261.34 (n/a)</td><td>257.90 (n/a)</td><td>219.50 (n/a)</td><td>44.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (+8.02%)</td><td>0.03 (+0.31%)</td><td>0.03 (+7.00%)</td><td>0.02 <b>(-27.39%)</b></td><td>0.01 <b>(+154.00%)</b></td><td>229.00 <b>(+37.70%)</b></td><td>159.12 (+5.00%)</td><td>143.60 (-6.51%)</td><td>119.00 (-7.47%)</td><td>45.80 <b>(+227.19%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.30 (n/a)</td><td>151.54 (n/a)</td><td>153.60 (n/a)</td><td>128.60 (n/a)</td><td>14.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-8.88%)</td><td>0.03 (+1.45%)</td><td>0.03 (-10.39%)</td><td>0.03 <b>(+38.00%)</b></td><td>0.00 <b>(-57.14%)</b></td><td>148.60 <b>(-27.55%)</b></td><td>138.84 (-4.79%)</td><td>146.20 (+11.60%)</td><td>125.00 (+9.75%)</td><td>11.73 <b>(-67.04%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>145.82 (n/a)</td><td>131.00 (n/a)</td><td>113.90 (n/a)</td><td>35.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(+34.35%)</b></td><td>0.02 (-0.02%)</td><td>0.02 (+2.80%)</td><td>0.01 <b>(-47.40%)</b></td><td>0.01 <b>(+449.25%)</b></td><td>404.70 <b>(+90.09%)</b></td><td>220.56 (+14.16%)</td><td>183.00 (-2.76%)</td><td>135.00 <b>(-25.58%)</b></td><td>106.27 <b>(+736.90%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>193.20 (n/a)</td><td>188.20 (n/a)</td><td>181.40 (n/a)</td><td>12.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (+11.20%)</td><td>0.02 (-1.41%)</td><td>0.02 (-1.79%)</td><td>0.02 (-4.19%)</td><td>0.01 <b>(+30.39%)</b></td><td>228.40 (+4.39%)</td><td>182.76 (+3.38%)</td><td>182.30 (+1.79%)</td><td>120.70 (-10.06%)</td><td>43.50 <b>(+23.15%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>176.78 (n/a)</td><td>179.10 (n/a)</td><td>134.20 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-5.65%)</td><td>0.03 (+10.13%)</td><td>0.03 <b>(+21.36%)</b></td><td>0.02 (+3.89%)</td><td>0.01 (-4.85%)</td><td>196.50 (-3.72%)</td><td>144.06 (-9.37%)</td><td>129.30 (-17.64%)</td><td>122.10 (+5.99%)</td><td>31.44 (-1.99%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>158.96 (n/a)</td><td>157.00 (n/a)</td><td>115.20 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-7.86%)</td><td>0.03 (-3.67%)</td><td>0.03 (-8.32%)</td><td>0.02 (+2.81%)</td><td>0.01 (-19.59%)</td><td>202.50 (-2.74%)</td><td>157.26 (+2.22%)</td><td>147.70 (+9.08%)</td><td>129.10 (+8.49%)</td><td>32.13 (-17.03%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>153.84 (n/a)</td><td>135.40 (n/a)</td><td>119.00 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 <b>(+24.70%)</b></td><td>0.03 (-3.17%)</td><td>0.02 (-19.05%)</td><td>0.02 (-8.69%)</td><td>0.01 <b>(+152.97%)</b></td><td>188.20 (+9.55%)</td><td>155.90 (+7.71%)</td><td>172.00 <b>(+23.56%)</b></td><td>106.50 (-19.80%)</td><td>36.79 <b>(+126.98%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.80 (n/a)</td><td>144.74 (n/a)</td><td>139.20 (n/a)</td><td>132.80 (n/a)</td><td>16.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-11.48%)</td><td>0.03 (-14.00%)</td><td>0.02 <b>(-27.92%)</b></td><td>0.02 (+1.95%)</td><td>0.01 <b>(-36.16%)</b></td><td>206.10 (-1.90%)</td><td>167.18 (+12.02%)</td><td>171.60 <b>(+38.72%)</b></td><td>124.20 (+12.91%)</td><td>31.60 <b>(-30.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>149.24 (n/a)</td><td>123.70 (n/a)</td><td>110.00 (n/a)</td><td>45.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(+21.47%)</b></td><td>0.03 (+17.62%)</td><td>0.03 (+9.14%)</td><td>0.02 (+16.66%)</td><td>0.00 <b>(+47.18%)</b></td><td>192.70 (-14.28%)</td><td>149.86 (-14.28%)</td><td>150.70 (-8.33%)</td><td>123.50 (-17.67%)</td><td>28.34 (-2.17%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.80 (n/a)</td><td>174.82 (n/a)</td><td>164.40 (n/a)</td><td>150.00 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+17.90%)</td><td>0.03 (+14.95%)</td><td>0.03 (+6.44%)</td><td>0.02 (+12.52%)</td><td>0.00 <b>(+36.39%)</b></td><td>167.20 (-11.11%)</td><td>141.12 (-12.60%)</td><td>146.80 (-6.08%)</td><td>115.50 (-15.20%)</td><td>20.25 (+1.40%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.10 (n/a)</td><td>161.46 (n/a)</td><td>156.30 (n/a)</td><td>136.20 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (+10.19%)</td><td>0.03 <b>(+20.44%)</b></td><td>0.03 <b>(+40.91%)</b></td><td>0.02 (+3.84%)</td><td>0.01 <b>(+50.25%)</b></td><td>194.10 (-3.72%)</td><td>151.60 (-15.11%)</td><td>130.20 <b>(-29.05%)</b></td><td>121.10 (-9.22%)</td><td>36.71 <b>(+35.31%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.60 (n/a)</td><td>178.58 (n/a)</td><td>183.50 (n/a)</td><td>133.40 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+2.87%)</td><td>0.03 (+4.71%)</td><td>0.03 (-8.45%)</td><td>0.02 <b>(+31.86%)</b></td><td>0.01 <b>(-24.20%)</b></td><td>170.10 <b>(-24.20%)</b></td><td>144.56 (-7.71%)</td><td>150.20 (+9.24%)</td><td>109.80 (-2.83%)</td><td>24.63 <b>(-45.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>156.64 (n/a)</td><td>137.50 (n/a)</td><td>113.00 (n/a)</td><td>44.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-12.75%)</td><td>0.02 (+10.21%)</td><td>0.03 <b>(+27.48%)</b></td><td>0.02 <b>(+40.96%)</b></td><td>0.00 <b>(-57.43%)</b></td><td>207.60 <b>(-29.05%)</b></td><td>170.50 (-14.91%)</td><td>159.20 <b>(-21.58%)</b></td><td>155.40 (+14.60%)</td><td>22.20 <b>(-64.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>292.60 (n/a)</td><td>200.38 (n/a)</td><td>203.00 (n/a)</td><td>135.60 (n/a)</td><td>62.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (-10.68%)</td><td>0.03 (-2.93%)</td><td>0.03 (-5.11%)</td><td>0.02 (+10.13%)</td><td>0.01 <b>(-29.27%)</b></td><td>183.20 (-9.22%)</td><td>155.84 (+0.66%)</td><td>158.70 (+5.38%)</td><td>116.50 (+11.91%)</td><td>26.61 <b>(-27.13%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>154.82 (n/a)</td><td>150.60 (n/a)</td><td>104.10 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-5.72%)</td><td>0.02 (-3.82%)</td><td>0.02 (-7.25%)</td><td>0.02 (+7.88%)</td><td>0.00 <b>(-37.64%)</b></td><td>210.60 (-7.31%)</td><td>177.30 (+2.46%)</td><td>172.70 (+7.80%)</td><td>157.00 (+6.08%)</td><td>19.91 <b>(-38.09%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.20 (n/a)</td><td>173.04 (n/a)</td><td>160.20 (n/a)</td><td>148.00 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+6.15%)</td><td>0.03 (-10.52%)</td><td>0.02 (-7.76%)</td><td>0.02 <b>(-31.26%)</b></td><td>0.01 <b>(+95.24%)</b></td><td>235.50 <b>(+45.46%)</b></td><td>172.94 (+16.68%)</td><td>169.50 (+8.38%)</td><td>115.20 (-5.81%)</td><td>43.95 <b>(+163.04%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>161.90 (n/a)</td><td>148.22 (n/a)</td><td>156.40 (n/a)</td><td>122.30 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (+1.51%)</td><td>0.05 (-8.95%)</td><td>0.06 (-5.19%)</td><td>0.04 <b>(-24.34%)</b></td><td>0.01 <b>(+134.70%)</b></td><td>200.40 <b>(+32.19%)</b></td><td>155.94 (+13.99%)</td><td>143.70 (+5.51%)</td><td>121.50 (-1.46%)</td><td>36.77 <b>(+207.21%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>151.60 (n/a)</td><td>136.80 (n/a)</td><td>136.20 (n/a)</td><td>123.30 (n/a)</td><td>11.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 <b>(-21.49%)</b></td><td>0.05 (-8.14%)</td><td>0.05 (-0.86%)</td><td>0.05 (-1.17%)</td><td>0.00 <b>(-55.05%)</b></td><td>178.30 (+1.19%)</td><td>162.76 (+7.19%)</td><td>157.80 (+0.83%)</td><td>150.00 <b>(+27.33%)</b></td><td>13.75 <b>(-41.65%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>151.84 (n/a)</td><td>156.50 (n/a)</td><td>117.80 (n/a)</td><td>23.57 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (+18.05%)</td><td>0.05 (+4.98%)</td><td>0.05 (+5.02%)</td><td>0.04 (-4.74%)</td><td>0.01 <b>(+65.07%)</b></td><td>219.90 (+5.01%)</td><td>179.98 (-2.12%)</td><td>181.60 (-4.77%)</td><td>117.90 (-15.24%)</td><td>38.87 <b>(+47.09%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>183.88 (n/a)</td><td>190.70 (n/a)</td><td>139.10 (n/a)</td><td>26.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (-5.50%)</td><td>0.04 (+6.77%)</td><td>0.04 (+5.59%)</td><td>0.04 <b>(+27.61%)</b></td><td>0.00 <b>(-44.65%)</b></td><td>218.70 <b>(-21.64%)</b></td><td>196.00 (-8.51%)</td><td>192.40 (-5.31%)</td><td>170.60 (+5.83%)</td><td>19.86 <b>(-53.95%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.10 (n/a)</td><td>214.24 (n/a)</td><td>203.20 (n/a)</td><td>161.20 (n/a)</td><td>43.12 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (+14.93%)</td><td>0.05 (-8.06%)</td><td>0.04 (-17.73%)</td><td>0.04 (-16.97%)</td><td>0.01 <b>(+86.90%)</b></td><td>230.20 <b>(+20.46%)</b></td><td>184.18 (+12.74%)</td><td>197.90 <b>(+21.56%)</b></td><td>120.70 (-13.04%)</td><td>42.20 <b>(+91.73%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>163.36 (n/a)</td><td>162.80 (n/a)</td><td>138.80 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (+8.57%)</td><td>0.05 (+1.69%)</td><td>0.05 (+0.09%)</td><td>0.05 (+7.25%)</td><td>0.01 <b>(+21.90%)</b></td><td>166.00 (-6.79%)</td><td>151.44 (-1.51%)</td><td>149.90 (-0.13%)</td><td>129.00 (-7.86%)</td><td>14.78 (+2.41%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>153.76 (n/a)</td><td>150.10 (n/a)</td><td>140.00 (n/a)</td><td>14.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (+8.90%)</td><td>0.05 (+3.38%)</td><td>0.05 (+1.20%)</td><td>0.04 (-2.67%)</td><td>0.01 <b>(+42.09%)</b></td><td>214.80 (+2.73%)</td><td>171.18 (-1.52%)</td><td>171.00 (-1.16%)</td><td>124.60 (-8.18%)</td><td>35.88 <b>(+36.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>173.82 (n/a)</td><td>173.00 (n/a)</td><td>135.70 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (+10.46%)</td><td>0.05 (+9.45%)</td><td>0.05 (+9.98%)</td><td>0.04 (+1.77%)</td><td>0.01 (+17.73%)</td><td>187.00 (-1.73%)</td><td>156.40 (-8.45%)</td><td>150.60 (-9.06%)</td><td>139.30 (-9.49%)</td><td>18.13 (+6.50%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>170.84 (n/a)</td><td>165.60 (n/a)</td><td>153.90 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (+16.55%)</td><td>0.05 (+12.54%)</td><td>0.05 (+14.88%)</td><td>0.04 (+4.50%)</td><td>0.01 <b>(+86.27%)</b></td><td>182.20 (-4.31%)</td><td>155.42 (-10.44%)</td><td>150.50 (-12.96%)</td><td>133.60 (-14.25%)</td><td>19.62 <b>(+54.33%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.40 (n/a)</td><td>173.54 (n/a)</td><td>172.90 (n/a)</td><td>155.80 (n/a)</td><td>12.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 <b>(+23.66%)</b></td><td>0.05 (+12.41%)</td><td>0.06 (+13.05%)</td><td>0.04 (-7.25%)</td><td>0.01 <b>(+349.33%)</b></td><td>192.30 (+7.79%)</td><td>152.32 (-9.60%)</td><td>148.50 (-11.50%)</td><td>131.90 (-19.13%)</td><td>23.56 <b>(+299.09%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.40 (n/a)</td><td>168.50 (n/a)</td><td>167.80 (n/a)</td><td>163.10 (n/a)</td><td>5.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (+8.94%)</td><td>0.05 (+10.38%)</td><td>0.05 (+9.42%)</td><td>0.05 (+15.22%)</td><td>0.00 (-16.88%)</td><td>165.30 (-13.18%)</td><td>151.04 (-9.77%)</td><td>151.10 (-8.59%)</td><td>133.30 (-8.20%)</td><td>11.73 <b>(-34.54%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>167.40 (n/a)</td><td>165.30 (n/a)</td><td>145.20 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 <b>(+51.19%)</b></td><td>0.06 (+19.27%)</td><td>0.06 (+13.46%)</td><td>0.04 (-4.31%)</td><td>0.01 <b>(+316.77%)</b></td><td>188.60 (+4.55%)</td><td>145.82 (-12.82%)</td><td>147.30 (-11.90%)</td><td>102.80 <b>(-33.89%)</b></td><td>32.75 <b>(+187.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>180.40 (n/a)</td><td>167.26 (n/a)</td><td>167.20 (n/a)</td><td>155.50 (n/a)</td><td>11.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 <b>(+28.37%)</b></td><td>0.06 <b>(+26.14%)</b></td><td>0.06 <b>(+21.48%)</b></td><td>0.05 <b>(+37.06%)</b></td><td>0.01 (+13.46%)</td><td>157.90 <b>(-27.03%)</b></td><td>136.54 <b>(-21.22%)</b></td><td>137.90 (-17.67%)</td><td>108.10 <b>(-22.12%)</b></td><td>18.10 <b>(-37.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>173.32 (n/a)</td><td>167.50 (n/a)</td><td>138.80 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (+7.80%)</td><td>0.05 (-4.84%)</td><td>0.05 (-0.01%)</td><td>0.04 (-5.26%)</td><td>0.01 (+13.80%)</td><td>209.60 (+5.54%)</td><td>161.90 (+5.98%)</td><td>156.70 (+0.00%)</td><td>112.90 (-7.23%)</td><td>35.42 (+12.64%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>152.76 (n/a)</td><td>156.70 (n/a)</td><td>121.70 (n/a)</td><td>31.45 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (-4.66%)</td><td>0.05 (+2.45%)</td><td>0.05 (+10.38%)</td><td>0.03 <b>(-26.70%)</b></td><td>0.01 <b>(+51.20%)</b></td><td>282.00 <b>(+36.43%)</b></td><td>177.78 (+1.84%)</td><td>150.70 (-9.38%)</td><td>148.80 (+4.86%)</td><td>58.36 <b>(+115.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>174.56 (n/a)</td><td>166.30 (n/a)</td><td>141.90 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 <b>(-26.83%)</b></td><td>0.05 (-6.67%)</td><td>0.05 (+14.16%)</td><td>0.03 <b>(-25.32%)</b></td><td>0.01 <b>(-31.15%)</b></td><td>240.50 <b>(+33.91%)</b></td><td>164.70 (+6.33%)</td><td>151.40 (-12.43%)</td><td>128.10 <b>(+36.57%)</b></td><td>46.01 <b>(+27.66%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>179.60 (n/a)</td><td>154.90 (n/a)</td><td>172.90 (n/a)</td><td>93.80 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (+15.39%)</td><td>0.11 (+1.07%)</td><td>0.10 (-10.96%)</td><td>0.09 (-6.58%)</td><td>0.02 <b>(+104.28%)</b></td><td>182.20 (+6.99%)</td><td>154.18 (+0.72%)</td><td>165.20 (+12.38%)</td><td>122.40 (-13.31%)</td><td>25.94 <b>(+87.54%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>170.30 (n/a)</td><td>153.08 (n/a)</td><td>147.00 (n/a)</td><td>141.20 (n/a)</td><td>13.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (+14.03%)</td><td>0.11 (-2.58%)</td><td>0.10 (-10.11%)</td><td>0.08 (-12.27%)</td><td>0.03 <b>(+91.82%)</b></td><td>210.30 (+13.98%)</td><td>158.18 (+6.22%)</td><td>156.50 (+11.23%)</td><td>115.10 (-12.27%)</td><td>38.62 <b>(+85.35%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>148.92 (n/a)</td><td>140.70 (n/a)</td><td>131.20 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (-2.84%)</td><td>0.08 (-6.95%)</td><td>0.08 <b>(-22.35%)</b></td><td>0.06 <b>(+21.78%)</b></td><td>0.02 <b>(-28.78%)</b></td><td>262.30 (-17.88%)</td><td>205.10 (+0.81%)</td><td>207.90 <b>(+28.81%)</b></td><td>136.30 (+2.87%)</td><td>45.11 <b>(-43.18%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>319.40 (n/a)</td><td>203.46 (n/a)</td><td>161.40 (n/a)</td><td>132.50 (n/a)</td><td>79.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (-10.22%)</td><td>0.08 (-12.52%)</td><td>0.08 <b>(-25.54%)</b></td><td>0.06 (-6.43%)</td><td>0.02 <b>(-21.10%)</b></td><td>256.60 (+6.87%)</td><td>202.50 (+12.06%)</td><td>210.50 <b>(+34.33%)</b></td><td>136.90 (+11.39%)</td><td>43.98 (-13.35%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>240.10 (n/a)</td><td>180.70 (n/a)</td><td>156.70 (n/a)</td><td>122.90 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (+10.60%)</td><td>0.10 (-4.69%)</td><td>0.10 (-2.39%)</td><td>0.08 (-18.52%)</td><td>0.02 <b>(+185.10%)</b></td><td>206.20 <b>(+22.74%)</b></td><td>165.52 (+7.10%)</td><td>157.90 (+2.47%)</td><td>132.30 (-9.63%)</td><td>28.55 <b>(+221.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>168.00 (n/a)</td><td>154.54 (n/a)</td><td>154.10 (n/a)</td><td>146.40 (n/a)</td><td>8.88 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (+12.11%)</td><td>0.12 (+8.90%)</td><td>0.13 (+17.78%)</td><td>0.10 (-1.71%)</td><td>0.02 <b>(+128.70%)</b></td><td>167.80 (+1.70%)</td><td>140.62 (-6.97%)</td><td>129.20 (-15.11%)</td><td>122.80 (-10.82%)</td><td>20.80 <b>(+107.21%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>165.00 (n/a)</td><td>151.16 (n/a)</td><td>152.20 (n/a)</td><td>137.70 (n/a)</td><td>10.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (-17.57%)</td><td>0.10 (-11.71%)</td><td>0.11 (+2.90%)</td><td>0.08 <b>(-22.69%)</b></td><td>0.02 (-2.98%)</td><td>210.60 <b>(+29.36%)</b></td><td>169.00 (+14.72%)</td><td>153.20 (-2.85%)</td><td>131.20 <b>(+21.37%)</b></td><td>36.13 <b>(+60.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>162.80 (n/a)</td><td>147.32 (n/a)</td><td>157.70 (n/a)</td><td>108.10 (n/a)</td><td>22.45 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (+3.58%)</td><td>0.11 (-7.93%)</td><td>0.11 (-6.12%)</td><td>0.08 <b>(-24.00%)</b></td><td>0.02 <b>(+228.08%)</b></td><td>193.30 <b>(+31.59%)</b></td><td>153.78 (+11.60%)</td><td>149.30 (+6.57%)</td><td>124.40 (-3.49%)</td><td>29.68 <b>(+313.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>146.90 (n/a)</td><td>137.80 (n/a)</td><td>140.10 (n/a)</td><td>128.90 (n/a)</td><td>7.19 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (-9.02%)</td><td>0.10 (-6.23%)</td><td>0.11 (-3.41%)</td><td>0.08 (-13.49%)</td><td>0.02 (+0.76%)</td><td>214.40 (+15.58%)</td><td>162.06 (+7.48%)</td><td>148.10 (+3.57%)</td><td>127.40 (+9.92%)</td><td>34.38 <b>(+29.61%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.50 (n/a)</td><td>150.78 (n/a)</td><td>143.00 (n/a)</td><td>115.90 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (-16.27%)</td><td>0.11 (-14.74%)</td><td>0.11 (-12.88%)</td><td>0.09 (-10.82%)</td><td>0.02 (-12.97%)</td><td>186.90 (+12.12%)</td><td>158.76 (+17.39%)</td><td>152.10 (+14.79%)</td><td>129.00 (+19.33%)</td><td>25.12 (+19.27%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>166.70 (n/a)</td><td>135.24 (n/a)</td><td>132.50 (n/a)</td><td>108.10 (n/a)</td><td>21.06 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (+3.78%)</td><td>0.10 (-4.33%)</td><td>0.10 (+6.19%)</td><td>0.08 (-12.81%)</td><td>0.02 <b>(+21.39%)</b></td><td>211.80 (+14.67%)</td><td>169.72 (+5.57%)</td><td>161.40 (-5.83%)</td><td>132.60 (-3.63%)</td><td>30.18 <b>(+39.11%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>160.76 (n/a)</td><td>171.40 (n/a)</td><td>137.60 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (-10.08%)</td><td>0.09 (-9.40%)</td><td>0.09 (-10.52%)</td><td>0.08 (+0.75%)</td><td>0.01 <b>(-27.97%)</b></td><td>202.40 (-0.74%)</td><td>180.20 (+9.46%)</td><td>185.40 (+11.75%)</td><td>148.20 (+11.18%)</td><td>19.97 <b>(-22.74%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.90 (n/a)</td><td>164.62 (n/a)</td><td>165.90 (n/a)</td><td>133.30 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (+0.62%)</td><td>0.09 (-14.22%)</td><td>0.08 (-16.24%)</td><td>0.07 <b>(-25.31%)</b></td><td>0.02 <b>(+49.87%)</b></td><td>246.90 <b>(+33.89%)</b></td><td>195.02 (+19.22%)</td><td>199.80 (+19.35%)</td><td>139.00 (-0.64%)</td><td>38.85 <b>(+94.19%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>163.58 (n/a)</td><td>167.40 (n/a)</td><td>139.90 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (-0.25%)</td><td>0.10 (-5.71%)</td><td>0.10 (-8.13%)</td><td>0.08 (-5.82%)</td><td>0.02 (+5.03%)</td><td>203.80 (+6.15%)</td><td>168.50 (+6.58%)</td><td>161.10 (+8.85%)</td><td>124.20 (+0.24%)</td><td>34.35 (+11.95%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.00 (n/a)</td><td>158.10 (n/a)</td><td>148.00 (n/a)</td><td>123.90 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (-7.04%)</td><td>0.09 (-5.69%)</td><td>0.09 (-11.57%)</td><td>0.06 (-9.72%)</td><td>0.02 (-18.24%)</td><td>285.40 (+10.75%)</td><td>197.78 (+5.02%)</td><td>185.40 (+13.12%)</td><td>153.80 (+7.55%)</td><td>51.54 (+1.24%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>257.70 (n/a)</td><td>188.32 (n/a)</td><td>163.90 (n/a)</td><td>143.00 (n/a)</td><td>50.91 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (-3.94%)</td><td>0.10 (+0.25%)</td><td>0.10 (-10.45%)</td><td>0.07 (+9.00%)</td><td>0.02 (-17.18%)</td><td>221.00 (-8.26%)</td><td>172.40 (-2.49%)</td><td>163.50 (+11.68%)</td><td>136.10 (+4.05%)</td><td>38.85 <b>(-23.76%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>240.90 (n/a)</td><td>176.80 (n/a)</td><td>146.40 (n/a)</td><td>130.80 (n/a)</td><td>50.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 <b>(-28.12%)</b></td><td>0.17 <b>(-21.75%)</b></td><td>0.16 <b>(-21.98%)</b></td><td>0.14 (-8.83%)</td><td>0.02 <b>(-55.10%)</b></td><td>226.30 (+9.69%)</td><td>199.26 <b>(+24.87%)</b></td><td>203.60 <b>(+28.21%)</b></td><td>165.50 <b>(+39.08%)</b></td><td>21.99 <b>(-32.57%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.30 (n/a)</td><td>159.58 (n/a)</td><td>158.80 (n/a)</td><td>119.00 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (-10.86%)</td><td>0.17 (-13.05%)</td><td>0.17 (-7.62%)</td><td>0.14 (-12.63%)</td><td>0.03 <b>(-25.95%)</b></td><td>227.60 (+14.43%)</td><td>190.68 (+14.14%)</td><td>189.50 (+8.22%)</td><td>150.40 (+12.24%)</td><td>27.84 (-4.94%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>198.90 (n/a)</td><td>167.06 (n/a)</td><td>175.10 (n/a)</td><td>134.00 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (-9.61%)</td><td>0.17 (+9.74%)</td><td>0.18 <b>(+22.96%)</b></td><td>0.10 (-2.07%)</td><td>0.04 (-4.20%)</td><td>339.50 (+2.11%)</td><td>211.20 (-8.33%)</td><td>180.90 (-18.70%)</td><td>170.40 (+10.65%)</td><td>72.07 (+10.94%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>332.50 (n/a)</td><td>230.40 (n/a)</td><td>222.50 (n/a)</td><td>154.00 (n/a)</td><td>64.96 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 <b>(+38.12%)</b></td><td>0.20 (+15.54%)</td><td>0.19 (+8.82%)</td><td>0.14 (-6.25%)</td><td>0.05 <b>(+103.69%)</b></td><td>237.90 (+6.68%)</td><td>172.06 (-10.35%)</td><td>169.60 (-8.08%)</td><td>116.90 <b>(-27.62%)</b></td><td>44.13 <b>(+53.39%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.00 (n/a)</td><td>191.92 (n/a)</td><td>184.50 (n/a)</td><td>161.50 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (-7.32%)</td><td>0.18 (-14.63%)</td><td>0.17 <b>(-24.34%)</b></td><td>0.14 (-6.10%)</td><td>0.03 <b>(-22.04%)</b></td><td>236.50 (+6.48%)</td><td>186.84 (+16.05%)</td><td>188.20 <b>(+32.16%)</b></td><td>151.20 (+7.85%)</td><td>31.72 (-9.65%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.10 (n/a)</td><td>161.00 (n/a)</td><td>142.40 (n/a)</td><td>140.20 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (+5.69%)</td><td>0.20 (-2.11%)</td><td>0.19 (-1.71%)</td><td>0.16 (-2.59%)</td><td>0.04 (+15.93%)</td><td>199.00 (+2.63%)</td><td>165.36 (+2.99%)</td><td>174.10 (+1.69%)</td><td>121.40 (-5.38%)</td><td>32.17 (+15.09%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.90 (n/a)</td><td>160.56 (n/a)</td><td>171.20 (n/a)</td><td>128.30 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 <b>(+21.85%)</b></td><td>0.21 (+5.91%)</td><td>0.19 (+0.78%)</td><td>0.16 (-9.10%)</td><td>0.05 <b>(+115.52%)</b></td><td>201.00 (+10.02%)</td><td>163.46 (-3.04%)</td><td>171.10 (-0.75%)</td><td>115.10 (-17.90%)</td><td>31.88 <b>(+92.24%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>182.70 (n/a)</td><td>168.58 (n/a)</td><td>172.40 (n/a)</td><td>140.20 (n/a)</td><td>16.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (+15.70%)</td><td>0.20 (-2.30%)</td><td>0.21 (+5.37%)</td><td>0.09 <b>(-45.16%)</b></td><td>0.07 <b>(+106.74%)</b></td><td>369.20 <b>(+82.32%)</b></td><td>192.32 (+16.95%)</td><td>158.10 (-5.10%)</td><td>115.80 (-13.58%)</td><td>101.58 <b>(+258.26%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>202.50 (n/a)</td><td>164.44 (n/a)</td><td>166.60 (n/a)</td><td>134.00 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (-13.96%)</td><td>0.19 (-14.57%)</td><td>0.19 (-16.49%)</td><td>0.15 (-7.34%)</td><td>0.03 (-15.75%)</td><td>214.70 (+7.89%)</td><td>177.32 (+16.67%)</td><td>176.00 (+19.73%)</td><td>151.50 (+16.27%)</td><td>27.23 (-0.08%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.00 (n/a)</td><td>151.98 (n/a)</td><td>147.00 (n/a)</td><td>130.30 (n/a)</td><td>27.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (+1.85%)</td><td>0.24 (+13.90%)</td><td>0.24 (+18.57%)</td><td>0.21 <b>(+23.29%)</b></td><td>0.03 <b>(-27.33%)</b></td><td>154.70 (-18.88%)</td><td>135.26 (-13.46%)</td><td>133.80 (-15.69%)</td><td>118.20 (-1.75%)</td><td>15.85 <b>(-41.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>190.70 (n/a)</td><td>156.30 (n/a)</td><td>158.70 (n/a)</td><td>120.30 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (-8.14%)</td><td>0.21 (-1.11%)</td><td>0.20 (+0.64%)</td><td>0.17 (-2.41%)</td><td>0.05 (-13.77%)</td><td>197.80 (+2.43%)</td><td>162.64 (+0.54%)</td><td>160.40 (-0.62%)</td><td>119.10 (+8.87%)</td><td>33.16 (-0.70%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>193.10 (n/a)</td><td>161.76 (n/a)</td><td>161.40 (n/a)</td><td>109.40 (n/a)</td><td>33.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.30 (+8.09%)</td><td>0.19 (-10.70%)</td><td>0.18 (-11.26%)</td><td>0.15 (-16.13%)</td><td>0.06 <b>(+42.87%)</b></td><td>215.00 (+19.25%)</td><td>178.72 (+15.21%)</td><td>186.00 (+12.66%)</td><td>110.20 (-7.47%)</td><td>40.15 <b>(+47.37%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.30 (n/a)</td><td>155.12 (n/a)</td><td>165.10 (n/a)</td><td>119.10 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (+7.42%)</td><td>0.20 (-4.72%)</td><td>0.18 (-13.86%)</td><td>0.17 (-0.20%)</td><td>0.03 (+16.67%)</td><td>191.40 (+0.21%)</td><td>170.78 (+5.34%)</td><td>179.00 (+16.08%)</td><td>133.40 (-6.91%)</td><td>23.44 (+9.05%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.00 (n/a)</td><td>162.12 (n/a)</td><td>154.20 (n/a)</td><td>143.30 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 <b>(-23.72%)</b></td><td>0.20 (-0.68%)</td><td>0.21 (+4.59%)</td><td>0.17 (+10.76%)</td><td>0.02 <b>(-59.72%)</b></td><td>194.60 (-9.74%)</td><td>162.48 (-4.46%)</td><td>158.50 (-4.40%)</td><td>143.90 <b>(+31.18%)</b></td><td>20.83 <b>(-54.68%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>215.60 (n/a)</td><td>170.06 (n/a)</td><td>165.80 (n/a)</td><td>109.70 (n/a)</td><td>45.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (+6.80%)</td><td>0.19 (+5.97%)</td><td>0.21 (+19.95%)</td><td>0.13 (-13.09%)</td><td>0.05 <b>(+37.89%)</b></td><td>255.50 (+15.04%)</td><td>179.88 (-2.67%)</td><td>158.90 (-16.63%)</td><td>128.20 (-6.36%)</td><td>51.36 <b>(+51.57%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.10 (n/a)</td><td>184.82 (n/a)</td><td>190.60 (n/a)</td><td>136.90 (n/a)</td><td>33.88 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.31 (+16.88%)</td><td>0.25 (+15.95%)</td><td>0.27 <b>(+35.90%)</b></td><td>0.20 <b>(+21.21%)</b></td><td>0.05 (+1.84%)</td><td>165.00 (-17.50%)</td><td>134.46 (-14.39%)</td><td>122.60 <b>(-26.45%)</b></td><td>106.00 (-14.45%)</td><td>25.55 <b>(-22.20%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>200.00 (n/a)</td><td>157.06 (n/a)</td><td>166.70 (n/a)</td><td>123.90 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (-0.65%)</td><td>0.21 (-0.12%)</td><td>0.21 (+0.05%)</td><td>0.21 (-0.04%)</td><td>0.00 <b>(-75.46%)</b></td><td>40902.80 (+0.04%)</td><td>40854.42 (+0.12%)</td><td>40850.10 (-0.05%)</td><td>40806.80 (+0.66%)</td><td>36.86 <b>(-75.29%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40885.90 (n/a)</td><td>40806.28 (n/a)</td><td>40871.20 (n/a)</td><td>40540.60 (n/a)</td><td>149.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (+0.52%)</td><td>0.21 (+0.20%)</td><td>0.21 (+0.07%)</td><td>0.21 (+0.12%)</td><td>0.00 <b>(+109.87%)</b></td><td>40896.60 (-0.12%)</td><td>40806.44 (-0.19%)</td><td>40877.50 (-0.07%)</td><td>40552.10 (-0.52%)</td><td>145.94 <b>(+108.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40944.20 (n/a)</td><td>40885.84 (n/a)</td><td>40907.70 (n/a)</td><td>40764.50 (n/a)</td><td>69.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (-0.03%)</td><td>0.13 (+0.01%)</td><td>0.13 (+0.02%)</td><td>0.13 (+0.03%)</td><td>0.00 <b>(-36.88%)</b></td><td>322375.00 (-0.03%)</td><td>322208.68 (-0.01%)</td><td>322255.30 (-0.02%)</td><td>322049.60 (+0.03%)</td><td>138.61 <b>(-36.88%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>322474.10 (n/a)</td><td>322227.64 (n/a)</td><td>322329.10 (n/a)</td><td>321967.10 (n/a)</td><td>219.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (-19.42%)</td><td>0.03 (-4.49%)</td><td>0.03 (+4.72%)</td><td>0.02 (+5.89%)</td><td>0.00 <b>(-53.00%)</b></td><td>181.50 (-5.52%)</td><td>154.72 (+1.78%)</td><td>144.70 (-4.49%)</td><td>140.20 <b>(+24.07%)</b></td><td>17.96 <b>(-45.31%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>152.02 (n/a)</td><td>151.50 (n/a)</td><td>113.00 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+2.50%)</td><td>0.03 (+0.34%)</td><td>0.04 (+8.54%)</td><td>0.02 (+12.81%)</td><td>0.01 (+0.48%)</td><td>291.10 (-11.36%)</td><td>189.12 (-1.84%)</td><td>152.30 (-7.92%)</td><td>143.30 (-2.45%)</td><td>62.99 (-17.75%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.40 (n/a)</td><td>192.66 (n/a)</td><td>165.40 (n/a)</td><td>146.90 (n/a)</td><td>76.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(-29.75%)</b></td><td>0.02 <b>(-21.43%)</b></td><td>0.03 (-15.03%)</td><td>0.01 <b>(-30.52%)</b></td><td>0.01 (-19.89%)</td><td>309.30 <b>(+43.93%)</b></td><td>187.04 <b>(+29.76%)</b></td><td>149.50 (+17.72%)</td><td>142.80 <b>(+42.37%)</b></td><td>70.28 <b>(+61.40%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>144.14 (n/a)</td><td>127.00 (n/a)</td><td>100.30 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+0.13%)</td><td>0.03 (+1.66%)</td><td>0.04 (+9.52%)</td><td>0.03 (-0.76%)</td><td>0.01 (+0.88%)</td><td>186.80 (+0.76%)</td><td>149.40 (-1.53%)</td><td>141.70 (-8.64%)</td><td>123.20 (-0.08%)</td><td>24.38 (+3.19%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>151.72 (n/a)</td><td>155.10 (n/a)</td><td>123.30 (n/a)</td><td>23.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(-20.94%)</b></td><td>0.02 (-19.24%)</td><td>0.02 <b>(-22.52%)</b></td><td>0.01 <b>(-24.04%)</b></td><td>0.01 (-14.90%)</td><td>304.90 <b>(+31.65%)</b></td><td>206.96 <b>(+25.25%)</b></td><td>209.50 <b>(+29.08%)</b></td><td>138.70 <b>(+26.44%)</b></td><td>67.39 <b>(+37.72%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.60 (n/a)</td><td>165.24 (n/a)</td><td>162.30 (n/a)</td><td>109.70 (n/a)</td><td>48.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+19.12%)</td><td>0.04 (+16.13%)</td><td>0.04 (+7.08%)</td><td>0.03 <b>(+21.56%)</b></td><td>0.00 <b>(+24.46%)</b></td><td>167.90 (-17.74%)</td><td>144.82 (-13.83%)</td><td>145.70 (-6.66%)</td><td>124.90 (-16.01%)</td><td>19.65 (-15.57%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>168.06 (n/a)</td><td>156.10 (n/a)</td><td>148.70 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 <b>(+38.70%)</b></td><td>0.03 <b>(+29.05%)</b></td><td>0.03 (+16.36%)</td><td>0.02 <b>(+27.53%)</b></td><td>0.01 <b>(+96.16%)</b></td><td>166.10 <b>(-21.58%)</b></td><td>138.12 <b>(-21.07%)</b></td><td>147.10 (-14.08%)</td><td>104.70 <b>(-27.89%)</b></td><td>27.65 (+9.87%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.80 (n/a)</td><td>174.98 (n/a)</td><td>171.20 (n/a)</td><td>145.20 (n/a)</td><td>25.17 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (+11.40%)</td><td>0.03 <b>(+20.07%)</b></td><td>0.03 (+18.20%)</td><td>0.03 <b>(+37.73%)</b></td><td>0.00 <b>(-31.99%)</b></td><td>165.20 <b>(-27.38%)</b></td><td>151.00 (-18.02%)</td><td>152.00 (-15.41%)</td><td>129.30 (-10.27%)</td><td>13.42 <b>(-56.25%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.50 (n/a)</td><td>184.20 (n/a)</td><td>179.70 (n/a)</td><td>144.10 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 <b>(+22.93%)</b></td><td>0.03 (+15.95%)</td><td>0.03 (+17.76%)</td><td>0.02 (-16.49%)</td><td>0.01 <b>(+68.23%)</b></td><td>257.00 (+19.76%)</td><td>164.30 (-9.40%)</td><td>150.90 (-15.08%)</td><td>109.00 (-18.66%)</td><td>55.83 <b>(+68.34%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.60 (n/a)</td><td>181.34 (n/a)</td><td>177.70 (n/a)</td><td>134.00 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 <b>(+41.92%)</b></td><td>0.03 <b>(+32.51%)</b></td><td>0.03 <b>(+34.59%)</b></td><td>0.03 <b>(+20.30%)</b></td><td>0.00 <b>(+150.68%)</b></td><td>174.40 (-16.87%)</td><td>149.62 <b>(-23.98%)</b></td><td>144.70 <b>(-25.72%)</b></td><td>130.70 <b>(-29.50%)</b></td><td>17.03 <b>(+47.39%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.80 (n/a)</td><td>196.82 (n/a)</td><td>194.80 (n/a)</td><td>185.40 (n/a)</td><td>11.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (+14.80%)</td><td>0.02 (+11.21%)</td><td>0.03 <b>(+24.84%)</b></td><td>0.02 <b>(+21.21%)</b></td><td>0.01 <b>(+25.40%)</b></td><td>267.10 (-17.51%)</td><td>190.90 (-9.22%)</td><td>160.40 (-19.92%)</td><td>125.30 (-12.87%)</td><td>60.43 (-10.66%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>323.80 (n/a)</td><td>210.28 (n/a)</td><td>200.30 (n/a)</td><td>143.80 (n/a)</td><td>67.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (+4.26%)</td><td>0.03 (+13.62%)</td><td>0.03 (+15.47%)</td><td>0.02 <b>(+33.58%)</b></td><td>0.00 <b>(-30.05%)</b></td><td>203.80 <b>(-25.13%)</b></td><td>173.58 (-13.81%)</td><td>164.80 (-13.40%)</td><td>150.60 (-4.08%)</td><td>21.19 <b>(-50.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>272.20 (n/a)</td><td>201.40 (n/a)</td><td>190.30 (n/a)</td><td>157.00 (n/a)</td><td>43.12 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (+4.32%)</td><td>0.02 <b>(+20.18%)</b></td><td>0.02 <b>(+30.24%)</b></td><td>0.02 <b>(+24.65%)</b></td><td>0.00 <b>(-32.73%)</b></td><td>198.40 (-19.77%)</td><td>174.20 (-17.94%)</td><td>168.80 <b>(-23.20%)</b></td><td>152.20 (-4.16%)</td><td>17.60 <b>(-45.90%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.30 (n/a)</td><td>212.28 (n/a)</td><td>219.80 (n/a)</td><td>158.80 (n/a)</td><td>32.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 <b>(+32.03%)</b></td><td>0.02 (+10.85%)</td><td>0.02 (+12.78%)</td><td>0.01 <b>(-28.10%)</b></td><td>0.01 <b>(+237.31%)</b></td><td>350.40 <b>(+39.10%)</b></td><td>207.98 (-1.96%)</td><td>180.30 (-11.31%)</td><td>150.90 <b>(-24.28%)</b></td><td>81.85 <b>(+265.88%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.90 (n/a)</td><td>212.14 (n/a)</td><td>203.30 (n/a)</td><td>199.30 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (-8.09%)</td><td>0.02 (+3.39%)</td><td>0.02 (-9.94%)</td><td>0.01 <b>(+20.30%)</b></td><td>0.00 <b>(-43.07%)</b></td><td>283.80 (-16.87%)</td><td>232.08 (-8.17%)</td><td>230.70 (+11.02%)</td><td>191.10 (+8.83%)</td><td>37.48 <b>(-51.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>341.40 (n/a)</td><td>252.74 (n/a)</td><td>207.80 (n/a)</td><td>175.60 (n/a)</td><td>77.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 <b>(+50.00%)</b></td><td>0.06 <b>(+36.70%)</b></td><td>0.05 <b>(+34.18%)</b></td><td>0.05 <b>(+30.26%)</b></td><td>0.01 <b>(+109.16%)</b></td><td>179.30 <b>(-23.24%)</b></td><td>150.80 <b>(-26.14%)</b></td><td>152.90 <b>(-25.49%)</b></td><td>118.30 <b>(-33.35%)</b></td><td>21.72 (+4.64%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.60 (n/a)</td><td>204.18 (n/a)</td><td>205.20 (n/a)</td><td>177.50 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 <b>(+26.20%)</b></td><td>0.09 <b>(+26.94%)</b></td><td>0.09 <b>(+29.29%)</b></td><td>0.07 (+6.64%)</td><td>0.02 <b>(+82.83%)</b></td><td>186.20 (-6.24%)</td><td>135.50 (-19.56%)</td><td>132.30 <b>(-22.63%)</b></td><td>110.20 <b>(-20.78%)</b></td><td>30.56 <b>(+37.07%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>168.44 (n/a)</td><td>171.00 (n/a)</td><td>139.10 (n/a)</td><td>22.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 <b>(+61.99%)</b></td><td>0.06 <b>(+55.44%)</b></td><td>0.06 <b>(+51.33%)</b></td><td>0.04 <b>(+81.11%)</b></td><td>0.01 <b>(+30.52%)</b></td><td>203.60 <b>(-44.78%)</b></td><td>145.00 <b>(-37.34%)</b></td><td>132.60 <b>(-33.90%)</b></td><td>114.90 <b>(-38.26%)</b></td><td>34.26 <b>(-55.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>368.70 (n/a)</td><td>231.42 (n/a)</td><td>200.60 (n/a)</td><td>186.10 (n/a)</td><td>77.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 <b>(+75.25%)</b></td><td>0.07 <b>(+80.16%)</b></td><td>0.08 <b>(+102.98%)</b></td><td>0.05 <b>(+59.82%)</b></td><td>0.01 <b>(+100.59%)</b></td><td>203.10 <b>(-37.43%)</b></td><td>151.28 <b>(-43.87%)</b></td><td>129.40 <b>(-50.72%)</b></td><td>123.00 <b>(-42.95%)</b></td><td>35.62 <b>(-30.48%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>324.60 (n/a)</td><td>269.52 (n/a)</td><td>262.60 (n/a)</td><td>215.60 (n/a)</td><td>51.23 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 <b>(+29.58%)</b></td><td>0.05 (-4.32%)</td><td>0.05 (-0.84%)</td><td>0.03 <b>(-41.13%)</b></td><td>0.02 <b>(+257.49%)</b></td><td>322.70 <b>(+69.84%)</b></td><td>196.36 (+15.85%)</td><td>172.70 (+0.82%)</td><td>118.00 <b>(-22.77%)</b></td><td>77.75 <b>(+390.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.00 (n/a)</td><td>169.50 (n/a)</td><td>171.30 (n/a)</td><td>152.80 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (+14.33%)</td><td>0.07 (+18.78%)</td><td>0.07 <b>(+20.06%)</b></td><td>0.06 (+15.62%)</td><td>0.01 (+17.82%)</td><td>171.70 (-13.50%)</td><td>146.32 (-15.55%)</td><td>151.00 (-16.71%)</td><td>108.20 (-12.53%)</td><td>27.18 (-5.33%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>173.26 (n/a)</td><td>181.30 (n/a)</td><td>123.70 (n/a)</td><td>28.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (-7.41%)</td><td>0.06 (+17.58%)</td><td>0.05 <b>(+34.03%)</b></td><td>0.05 <b>(+66.41%)</b></td><td>0.01 <b>(-46.53%)</b></td><td>176.40 <b>(-39.92%)</b></td><td>151.84 <b>(-22.79%)</b></td><td>157.30 <b>(-25.38%)</b></td><td>112.30 (+8.08%)</td><td>25.01 <b>(-64.82%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>293.60 (n/a)</td><td>196.66 (n/a)</td><td>210.80 (n/a)</td><td>103.90 (n/a)</td><td>71.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (+11.37%)</td><td>0.06 <b>(+22.57%)</b></td><td>0.06 <b>(+22.32%)</b></td><td>0.05 <b>(+35.02%)</b></td><td>0.01 (-18.62%)</td><td>170.40 <b>(-25.95%)</b></td><td>155.00 (-19.66%)</td><td>164.00 (-18.29%)</td><td>124.50 (-10.17%)</td><td>18.82 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>192.92 (n/a)</td><td>200.70 (n/a)</td><td>138.60 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 <b>(+29.56%)</b></td><td>0.05 (+15.04%)</td><td>0.05 (+8.49%)</td><td>0.03 (+2.59%)</td><td>0.01 <b>(+32.50%)</b></td><td>295.00 (-2.51%)</td><td>183.56 (-11.05%)</td><td>167.70 (-7.81%)</td><td>118.90 <b>(-22.79%)</b></td><td>66.70 (+6.21%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.60 (n/a)</td><td>206.36 (n/a)</td><td>181.90 (n/a)</td><td>154.00 (n/a)</td><td>62.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (+15.53%)</td><td>0.05 (+10.54%)</td><td>0.06 (+18.48%)</td><td>0.03 <b>(-22.99%)</b></td><td>0.01 <b>(+289.08%)</b></td><td>275.60 <b>(+29.82%)</b></td><td>184.06 (-5.45%)</td><td>161.60 (-15.57%)</td><td>156.60 (-13.48%)</td><td>51.45 <b>(+341.92%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.30 (n/a)</td><td>194.66 (n/a)</td><td>191.40 (n/a)</td><td>181.00 (n/a)</td><td>11.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (+10.19%)</td><td>0.05 (+17.79%)</td><td>0.05 (+16.71%)</td><td>0.05 <b>(+46.80%)</b></td><td>0.01 <b>(-46.77%)</b></td><td>172.10 <b>(-31.87%)</b></td><td>157.66 (-17.74%)</td><td>164.10 (-14.31%)</td><td>137.00 (-9.21%)</td><td>14.66 <b>(-65.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>191.66 (n/a)</td><td>191.50 (n/a)</td><td>150.90 (n/a)</td><td>42.89 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 <b>(+47.35%)</b></td><td>0.05 <b>(+25.80%)</b></td><td>0.05 <b>(+22.80%)</b></td><td>0.03 (+8.04%)</td><td>0.01 <b>(+72.90%)</b></td><td>293.20 (-7.42%)</td><td>182.38 (-17.44%)</td><td>160.50 (-18.61%)</td><td>123.40 <b>(-32.16%)</b></td><td>64.77 (+15.13%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.70 (n/a)</td><td>220.90 (n/a)</td><td>197.20 (n/a)</td><td>181.90 (n/a)</td><td>56.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 <b>(+22.81%)</b></td><td>0.05 <b>(+24.47%)</b></td><td>0.05 <b>(+21.91%)</b></td><td>0.05 <b>(+84.75%)</b></td><td>0.01 <b>(-32.23%)</b></td><td>175.10 <b>(-45.86%)</b></td><td>158.50 <b>(-24.31%)</b></td><td>161.60 (-17.97%)</td><td>123.30 (-18.56%)</td><td>20.86 <b>(-70.17%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>323.40 (n/a)</td><td>209.42 (n/a)</td><td>197.00 (n/a)</td><td>151.40 (n/a)</td><td>69.94 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 <b>(+41.88%)</b></td><td>0.05 <b>(+20.73%)</b></td><td>0.05 <b>(+31.22%)</b></td><td>0.03 <b>(-21.70%)</b></td><td>0.01 <b>(+379.09%)</b></td><td>295.10 <b>(+27.69%)</b></td><td>184.48 (-11.47%)</td><td>158.30 <b>(-23.82%)</b></td><td>137.80 <b>(-29.51%)</b></td><td>63.16 <b>(+355.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>208.38 (n/a)</td><td>207.80 (n/a)</td><td>195.50 (n/a)</td><td>13.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (+2.26%)</td><td>0.04 (+5.44%)</td><td>0.04 (+6.58%)</td><td>0.03 (+9.09%)</td><td>0.01 <b>(+21.14%)</b></td><td>301.70 (-8.33%)</td><td>235.06 (-4.12%)</td><td>221.30 (-6.15%)</td><td>179.40 (-2.18%)</td><td>56.26 (+7.05%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>329.10 (n/a)</td><td>245.16 (n/a)</td><td>235.80 (n/a)</td><td>183.40 (n/a)</td><td>52.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (-13.42%)</td><td>0.10 (+4.54%)</td><td>0.11 (+14.75%)</td><td>0.09 (+6.19%)</td><td>0.01 <b>(-44.83%)</b></td><td>184.50 (-5.82%)</td><td>158.92 (-5.76%)</td><td>151.20 (-12.85%)</td><td>144.70 (+15.48%)</td><td>16.41 <b>(-37.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.90 (n/a)</td><td>168.64 (n/a)</td><td>173.50 (n/a)</td><td>125.30 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (+5.51%)</td><td>0.14 (-0.24%)</td><td>0.15 (+7.14%)</td><td>0.09 (-19.90%)</td><td>0.04 <b>(+41.11%)</b></td><td>282.70 <b>(+24.87%)</b></td><td>185.98 (+4.33%)</td><td>166.60 (-6.67%)</td><td>126.50 (-5.24%)</td><td>58.66 <b>(+75.26%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.40 (n/a)</td><td>178.26 (n/a)</td><td>178.50 (n/a)</td><td>133.50 (n/a)</td><td>33.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (-8.64%)</td><td>0.11 (+2.33%)</td><td>0.11 (+13.42%)</td><td>0.07 (-16.15%)</td><td>0.02 (+6.28%)</td><td>225.30 (+19.27%)</td><td>159.98 (-0.98%)</td><td>149.50 (-11.80%)</td><td>130.40 (+9.40%)</td><td>38.36 <b>(+46.41%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.90 (n/a)</td><td>161.56 (n/a)</td><td>169.50 (n/a)</td><td>119.20 (n/a)</td><td>26.20 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (+0.62%)</td><td>0.14 (+14.68%)</td><td>0.14 <b>(+22.49%)</b></td><td>0.11 <b>(+32.38%)</b></td><td>0.03 <b>(-21.68%)</b></td><td>185.20 <b>(-24.47%)</b></td><td>148.36 (-15.40%)</td><td>149.00 (-18.40%)</td><td>119.70 (-0.58%)</td><td>27.27 <b>(-42.08%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>245.20 (n/a)</td><td>175.36 (n/a)</td><td>182.60 (n/a)</td><td>120.40 (n/a)</td><td>47.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (+11.95%)</td><td>0.10 (+11.74%)</td><td>0.11 (+18.40%)</td><td>0.07 (-4.04%)</td><td>0.02 <b>(+65.43%)</b></td><td>219.50 (+4.18%)</td><td>164.48 (-9.07%)</td><td>154.80 (-15.55%)</td><td>138.60 (-10.70%)</td><td>32.19 <b>(+57.84%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>180.88 (n/a)</td><td>183.30 (n/a)</td><td>155.20 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 <b>(+20.84%)</b></td><td>0.14 <b>(+37.44%)</b></td><td>0.14 <b>(+24.22%)</b></td><td>0.11 <b>(+62.34%)</b></td><td>0.02 <b>(-23.59%)</b></td><td>187.60 <b>(-38.39%)</b></td><td>149.90 <b>(-31.70%)</b></td><td>145.70 (-19.50%)</td><td>121.10 (-17.28%)</td><td>27.27 <b>(-63.40%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>304.50 (n/a)</td><td>219.46 (n/a)</td><td>181.00 (n/a)</td><td>146.40 (n/a)</td><td>74.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (-7.92%)</td><td>0.09 (+3.65%)</td><td>0.10 (+14.11%)</td><td>0.07 (-5.62%)</td><td>0.02 (-3.38%)</td><td>248.70 (+5.92%)</td><td>184.72 (-3.29%)</td><td>167.40 (-12.40%)</td><td>158.90 (+8.61%)</td><td>37.28 (+13.60%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.80 (n/a)</td><td>191.00 (n/a)</td><td>191.10 (n/a)</td><td>146.30 (n/a)</td><td>32.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (-1.46%)</td><td>0.11 (-0.57%)</td><td>0.12 (+18.42%)</td><td>0.05 <b>(-32.67%)</b></td><td>0.04 <b>(+26.99%)</b></td><td>347.90 <b>(+48.48%)</b></td><td>193.18 (+8.22%)</td><td>152.60 (-15.55%)</td><td>129.40 (+1.49%)</td><td>89.64 <b>(+101.59%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>234.30 (n/a)</td><td>178.50 (n/a)</td><td>180.70 (n/a)</td><td>127.50 (n/a)</td><td>44.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 <b>(+30.52%)</b></td><td>0.12 <b>(+40.56%)</b></td><td>0.12 <b>(+50.99%)</b></td><td>0.08 <b>(+54.72%)</b></td><td>0.02 (+12.52%)</td><td>205.70 <b>(-35.38%)</b></td><td>145.96 <b>(-30.54%)</b></td><td>131.50 <b>(-33.75%)</b></td><td>116.50 <b>(-23.41%)</b></td><td>36.42 <b>(-44.61%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>318.30 (n/a)</td><td>210.14 (n/a)</td><td>198.50 (n/a)</td><td>152.10 (n/a)</td><td>65.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (-11.41%)</td><td>0.11 (-5.33%)</td><td>0.12 (-3.88%)</td><td>0.06 (+9.84%)</td><td>0.03 (-18.30%)</td><td>284.60 (-8.96%)</td><td>178.34 (+1.65%)</td><td>151.30 (+4.06%)</td><td>129.30 (+12.93%)</td><td>63.48 (-19.91%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>312.60 (n/a)</td><td>175.44 (n/a)</td><td>145.40 (n/a)</td><td>114.50 (n/a)</td><td>79.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 <b>(+33.55%)</b></td><td>0.10 (+8.64%)</td><td>0.09 (-1.19%)</td><td>0.08 (+3.08%)</td><td>0.02 <b>(+132.83%)</b></td><td>199.70 (-2.96%)</td><td>168.06 (-5.52%)</td><td>175.30 (+1.21%)</td><td>120.40 <b>(-25.12%)</b></td><td>33.02 <b>(+72.20%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>177.88 (n/a)</td><td>173.20 (n/a)</td><td>160.80 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (-0.56%)</td><td>0.09 (-9.51%)</td><td>0.10 (-6.37%)</td><td>0.06 <b>(-35.12%)</b></td><td>0.02 <b>(+101.95%)</b></td><td>313.10 <b>(+54.08%)</b></td><td>203.76 (+16.71%)</td><td>173.30 (+6.78%)</td><td>158.40 (+0.57%)</td><td>65.16 <b>(+213.58%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>174.58 (n/a)</td><td>162.30 (n/a)</td><td>157.50 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 <b>(+25.21%)</b></td><td>0.10 (+16.05%)</td><td>0.10 (+17.35%)</td><td>0.05 (-12.66%)</td><td>0.03 <b>(+85.30%)</b></td><td>298.80 (+14.48%)</td><td>180.78 (-8.27%)</td><td>156.20 (-14.74%)</td><td>127.00 <b>(-20.13%)</b></td><td>69.74 <b>(+71.49%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>261.00 (n/a)</td><td>197.08 (n/a)</td><td>183.20 (n/a)</td><td>159.00 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (+3.73%)</td><td>0.08 (-16.96%)</td><td>0.08 (-15.97%)</td><td>0.05 <b>(-46.85%)</b></td><td>0.03 <b>(+260.97%)</b></td><td>372.30 <b>(+88.13%)</b></td><td>237.62 <b>(+34.52%)</b></td><td>206.20 (+18.98%)</td><td>155.90 (-3.59%)</td><td>93.94 <b>(+531.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>176.64 (n/a)</td><td>173.30 (n/a)</td><td>161.70 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (-17.72%)</td><td>0.07 (-10.66%)</td><td>0.08 (-16.82%)</td><td>0.05 (+5.29%)</td><td>0.01 <b>(-44.57%)</b></td><td>299.10 (-5.02%)</td><td>227.56 (+7.70%)</td><td>214.10 <b>(+20.21%)</b></td><td>190.50 <b>(+21.57%)</b></td><td>41.64 <b>(-34.74%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>314.90 (n/a)</td><td>211.30 (n/a)</td><td>178.10 (n/a)</td><td>156.70 (n/a)</td><td>63.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.29 <b>(+24.34%)</b></td><td>0.22 (+12.09%)</td><td>0.21 (+3.80%)</td><td>0.17 (+14.09%)</td><td>0.04 <b>(+34.74%)</b></td><td>188.70 (-12.35%)</td><td>151.22 (-10.23%)</td><td>154.70 (-3.61%)</td><td>113.00 (-19.57%)</td><td>28.55 (-6.02%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.30 (n/a)</td><td>168.46 (n/a)</td><td>160.50 (n/a)</td><td>140.50 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.24 (+0.46%)</td><td>0.21 (+2.49%)</td><td>0.19 (-3.34%)</td><td>0.19 <b>(+35.31%)</b></td><td>0.02 <b>(-43.60%)</b></td><td>175.90 <b>(-26.09%)</b></td><td>160.40 (-5.37%)</td><td>168.70 (+3.50%)</td><td>135.20 (-0.52%)</td><td>16.95 <b>(-58.75%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>238.00 (n/a)</td><td>169.50 (n/a)</td><td>163.00 (n/a)</td><td>135.90 (n/a)</td><td>41.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 <b>(-24.30%)</b></td><td>0.25 (-13.33%)</td><td>0.26 (-7.51%)</td><td>0.19 (-10.13%)</td><td>0.04 <b>(-39.33%)</b></td><td>218.70 (+11.30%)</td><td>170.58 (+13.49%)</td><td>157.20 (+8.12%)</td><td>144.40 <b>(+32.11%)</b></td><td>29.54 (-9.27%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>196.50 (n/a)</td><td>150.30 (n/a)</td><td>145.40 (n/a)</td><td>109.30 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 <b>(-22.04%)</b></td><td>0.19 (-15.25%)</td><td>0.18 (-13.24%)</td><td>0.16 (-3.07%)</td><td>0.02 <b>(-50.07%)</b></td><td>199.60 (+3.15%)</td><td>175.42 (+15.24%)</td><td>183.30 (+15.21%)</td><td>145.70 <b>(+28.26%)</b></td><td>20.87 <b>(-33.73%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>193.50 (n/a)</td><td>152.22 (n/a)</td><td>159.10 (n/a)</td><td>113.60 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.33 (+15.35%)</td><td>0.22 (-12.38%)</td><td>0.19 <b>(-27.63%)</b></td><td>0.15 <b>(-33.46%)</b></td><td>0.07 <b>(+165.35%)</b></td><td>281.10 <b>(+50.24%)</b></td><td>200.90 <b>(+22.89%)</b></td><td>218.30 <b>(+38.16%)</b></td><td>123.10 (-13.31%)</td><td>61.81 <b>(+235.22%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>187.10 (n/a)</td><td>163.48 (n/a)</td><td>158.00 (n/a)</td><td>142.00 (n/a)</td><td>18.44 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (-2.20%)</td><td>0.20 (+1.20%)</td><td>0.21 (+2.04%)</td><td>0.16 (+9.87%)</td><td>0.03 (-19.34%)</td><td>199.90 (-8.97%)</td><td>164.06 (-2.60%)</td><td>156.10 (-1.95%)</td><td>128.30 (+2.23%)</td><td>27.18 <b>(-25.46%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.60 (n/a)</td><td>168.44 (n/a)</td><td>159.20 (n/a)</td><td>125.50 (n/a)</td><td>36.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (+0.74%)</td><td>0.22 (-6.61%)</td><td>0.21 (-14.97%)</td><td>0.18 (+16.59%)</td><td>0.04 <b>(-20.11%)</b></td><td>203.30 (-14.26%)</td><td>168.44 (+4.74%)</td><td>176.90 (+17.62%)</td><td>129.60 (-0.77%)</td><td>28.94 <b>(-34.12%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>237.10 (n/a)</td><td>160.82 (n/a)</td><td>150.40 (n/a)</td><td>130.60 (n/a)</td><td>43.92 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 (-10.01%)</td><td>0.20 (+2.45%)</td><td>0.20 (+2.83%)</td><td>0.18 (+14.51%)</td><td>0.02 <b>(-47.22%)</b></td><td>182.50 (-12.64%)</td><td>161.40 (-4.18%)</td><td>162.90 (-2.80%)</td><td>144.20 (+11.18%)</td><td>15.22 <b>(-48.84%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.90 (n/a)</td><td>168.44 (n/a)</td><td>167.60 (n/a)</td><td>129.70 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 (-13.70%)</td><td>0.22 (+2.46%)</td><td>0.23 (+0.38%)</td><td>0.18 (+19.54%)</td><td>0.02 <b>(-53.62%)</b></td><td>202.80 (-16.34%)</td><td>171.50 (-5.66%)</td><td>161.70 (-0.43%)</td><td>157.80 (+15.86%)</td><td>19.03 <b>(-55.82%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>242.40 (n/a)</td><td>181.78 (n/a)</td><td>162.40 (n/a)</td><td>136.20 (n/a)</td><td>43.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 <b>(+25.01%)</b></td><td>0.23 <b>(+22.85%)</b></td><td>0.22 <b>(+20.16%)</b></td><td>0.20 <b>(+32.86%)</b></td><td>0.03 <b>(+26.16%)</b></td><td>167.50 <b>(-24.72%)</b></td><td>146.36 (-18.65%)</td><td>148.40 (-16.77%)</td><td>123.50 <b>(-20.01%)</b></td><td>19.91 <b>(-24.66%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>222.50 (n/a)</td><td>179.92 (n/a)</td><td>178.30 (n/a)</td><td>154.40 (n/a)</td><td>26.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (+0.07%)</td><td>0.18 (+6.88%)</td><td>0.17 (+5.27%)</td><td>0.14 (+0.96%)</td><td>0.03 (-10.91%)</td><td>257.40 (-0.96%)</td><td>203.22 (-7.01%)</td><td>201.50 (-5.04%)</td><td>160.30 (-0.12%)</td><td>35.04 (-10.74%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>259.90 (n/a)</td><td>218.54 (n/a)</td><td>212.20 (n/a)</td><td>160.50 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (-11.32%)</td><td>0.16 <b>(-20.21%)</b></td><td>0.18 (-13.69%)</td><td>0.10 <b>(-43.33%)</b></td><td>0.04 <b>(+90.13%)</b></td><td>330.10 <b>(+76.52%)</b></td><td>214.94 <b>(+33.34%)</b></td><td>185.00 (+15.84%)</td><td>156.40 (+12.76%)</td><td>70.76 <b>(+282.65%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>187.00 (n/a)</td><td>161.20 (n/a)</td><td>159.70 (n/a)</td><td>138.70 (n/a)</td><td>18.49 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 <b>(-37.72%)</b></td><td>0.15 (-14.53%)</td><td>0.17 (-6.66%)</td><td>0.13 <b>(+25.50%)</b></td><td>0.02 <b>(-66.10%)</b></td><td>270.60 <b>(-20.32%)</b></td><td>228.68 (+7.30%)</td><td>210.10 (+7.14%)</td><td>200.20 <b>(+60.55%)</b></td><td>33.75 <b>(-57.27%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>339.60 (n/a)</td><td>213.12 (n/a)</td><td>196.10 (n/a)</td><td>124.70 (n/a)</td><td>78.99 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (+2.88%)</td><td>0.15 (-6.72%)</td><td>0.15 (-9.18%)</td><td>0.10 <b>(-25.78%)</b></td><td>0.04 <b>(+66.49%)</b></td><td>326.40 <b>(+34.71%)</b></td><td>225.60 (+11.99%)</td><td>214.70 (+10.10%)</td><td>166.40 (-2.80%)</td><td>65.57 <b>(+114.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>242.30 (n/a)</td><td>201.44 (n/a)</td><td>195.00 (n/a)</td><td>171.20 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (+3.84%)</td><td>0.13 (+13.04%)</td><td>0.13 (+13.66%)</td><td>0.11 <b>(+33.10%)</b></td><td>0.02 <b>(-34.04%)</b></td><td>182.10 <b>(-24.88%)</b></td><td>156.38 (-14.37%)</td><td>158.90 (-12.02%)</td><td>126.40 (-3.66%)</td><td>21.06 <b>(-52.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>242.40 (n/a)</td><td>182.62 (n/a)</td><td>180.60 (n/a)</td><td>131.20 (n/a)</td><td>44.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (+9.08%)</td><td>0.13 (+9.29%)</td><td>0.14 <b>(+20.68%)</b></td><td>0.11 (+4.56%)</td><td>0.02 <b>(+25.17%)</b></td><td>186.30 (-4.36%)</td><td>159.34 (-8.10%)</td><td>149.30 (-17.15%)</td><td>134.10 (-8.34%)</td><td>22.60 (+12.31%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>173.38 (n/a)</td><td>180.20 (n/a)</td><td>146.30 (n/a)</td><td>20.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (+1.93%)</td><td>0.12 (+4.46%)</td><td>0.12 (-0.67%)</td><td>0.10 (+5.15%)</td><td>0.02 (-10.64%)</td><td>203.80 (-4.90%)</td><td>167.56 (-5.03%)</td><td>169.90 (+0.71%)</td><td>129.00 (-1.90%)</td><td>26.76 (-18.90%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>176.44 (n/a)</td><td>168.70 (n/a)</td><td>131.50 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (-15.56%)</td><td>0.10 (-15.83%)</td><td>0.10 (-16.43%)</td><td>0.08 <b>(-22.46%)</b></td><td>0.02 (+12.28%)</td><td>247.10 <b>(+28.97%)</b></td><td>199.88 <b>(+20.05%)</b></td><td>207.20 (+19.70%)</td><td>166.00 (+18.40%)</td><td>33.56 <b>(+68.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>191.60 (n/a)</td><td>166.50 (n/a)</td><td>173.10 (n/a)</td><td>140.20 (n/a)</td><td>19.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (+1.30%)</td><td>0.12 (+1.00%)</td><td>0.12 (+2.95%)</td><td>0.10 (+4.75%)</td><td>0.01 <b>(-20.51%)</b></td><td>197.90 (-4.53%)</td><td>173.86 (-1.56%)</td><td>166.80 (-2.85%)</td><td>151.40 (-1.24%)</td><td>18.46 <b>(-23.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.30 (n/a)</td><td>176.62 (n/a)</td><td>171.70 (n/a)</td><td>153.30 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (+12.48%)</td><td>0.13 (+5.78%)</td><td>0.13 (+14.90%)</td><td>0.09 <b>(-20.52%)</b></td><td>0.03 <b>(+82.53%)</b></td><td>235.50 <b>(+25.87%)</b></td><td>169.44 (-2.42%)</td><td>156.60 (-12.95%)</td><td>124.50 (-11.07%)</td><td>41.20 <b>(+111.95%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>187.10 (n/a)</td><td>173.64 (n/a)</td><td>179.90 (n/a)</td><td>140.00 (n/a)</td><td>19.44 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 <b>(-22.77%)</b></td><td>0.10 (-6.31%)</td><td>0.10 (+2.25%)</td><td>0.10 (+9.93%)</td><td>0.01 <b>(-72.68%)</b></td><td>214.30 (-9.04%)</td><td>207.42 (+3.79%)</td><td>211.60 (-2.17%)</td><td>186.40 <b>(+29.53%)</b></td><td>11.82 <b>(-67.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>235.60 (n/a)</td><td>199.84 (n/a)</td><td>216.30 (n/a)</td><td>143.90 (n/a)</td><td>36.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (-2.01%)</td><td>0.12 (+5.97%)</td><td>0.12 (+10.65%)</td><td>0.10 (-0.12%)</td><td>0.02 (-0.26%)</td><td>204.60 (+0.15%)</td><td>168.86 (-5.55%)</td><td>168.00 (-9.63%)</td><td>141.10 (+2.10%)</td><td>25.92 (+3.91%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.30 (n/a)</td><td>178.78 (n/a)</td><td>185.90 (n/a)</td><td>138.20 (n/a)</td><td>24.94 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (+0.22%)</td><td>0.18 (+7.40%)</td><td>0.19 (+4.89%)</td><td>0.15 (+14.53%)</td><td>0.02 <b>(-27.00%)</b></td><td>167.80 (-12.70%)</td><td>139.38 (-7.90%)</td><td>131.90 (-4.63%)</td><td>129.20 (-0.23%)</td><td>16.23 <b>(-36.34%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>192.20 (n/a)</td><td>151.34 (n/a)</td><td>138.30 (n/a)</td><td>129.50 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (+11.45%)</td><td>0.16 (+15.74%)</td><td>0.16 <b>(+24.19%)</b></td><td>0.14 (+12.67%)</td><td>0.02 (+5.04%)</td><td>175.20 (-11.25%)</td><td>153.84 (-13.72%)</td><td>151.10 (-19.50%)</td><td>130.50 (-10.31%)</td><td>17.89 (-15.27%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>197.40 (n/a)</td><td>178.30 (n/a)</td><td>187.70 (n/a)</td><td>145.50 (n/a)</td><td>21.11 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.18 (-1.52%)</td><td>0.15 (-0.15%)</td><td>0.15 (-0.07%)</td><td>0.12 (-13.99%)</td><td>0.02 <b>(+21.74%)</b></td><td>204.20 (+16.29%)</td><td>162.68 (+1.02%)</td><td>163.20 (+0.12%)</td><td>133.30 (+1.52%)</td><td>26.47 <b>(+46.24%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>175.60 (n/a)</td><td>161.04 (n/a)</td><td>163.00 (n/a)</td><td>131.30 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (-15.94%)</td><td>0.14 (-7.85%)</td><td>0.14 (-9.36%)</td><td>0.13 (+1.01%)</td><td>0.01 <b>(-52.70%)</b></td><td>182.40 (-0.98%)</td><td>170.84 (+7.49%)</td><td>174.70 (+10.29%)</td><td>154.10 (+18.90%)</td><td>11.12 <b>(-43.41%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.20 (n/a)</td><td>158.94 (n/a)</td><td>158.40 (n/a)</td><td>129.60 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (+6.51%)</td><td>0.17 (+5.63%)</td><td>0.18 (+2.80%)</td><td>0.11 (-10.91%)</td><td>0.04 <b>(+23.25%)</b></td><td>221.70 (+12.25%)</td><td>150.42 (-3.60%)</td><td>138.00 (-2.68%)</td><td>120.10 (-6.10%)</td><td>40.53 <b>(+36.74%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.50 (n/a)</td><td>156.04 (n/a)</td><td>141.80 (n/a)</td><td>127.90 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (+10.91%)</td><td>0.16 <b>(+20.20%)</b></td><td>0.17 <b>(+30.56%)</b></td><td>0.11 (+13.06%)</td><td>0.04 <b>(+30.72%)</b></td><td>233.40 (-11.56%)</td><td>161.60 (-15.45%)</td><td>143.90 <b>(-23.38%)</b></td><td>120.90 (-9.84%)</td><td>47.73 (+1.70%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>263.90 (n/a)</td><td>191.14 (n/a)</td><td>187.80 (n/a)</td><td>134.10 (n/a)</td><td>46.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (-14.90%)</td><td>0.11 (-16.26%)</td><td>0.11 (-13.14%)</td><td>0.07 (-15.62%)</td><td>0.03 <b>(-21.84%)</b></td><td>347.90 (+18.53%)</td><td>229.24 (+18.67%)</td><td>214.50 (+15.08%)</td><td>170.10 (+17.55%)</td><td>68.80 (+14.82%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>293.50 (n/a)</td><td>193.18 (n/a)</td><td>186.40 (n/a)</td><td>144.70 (n/a)</td><td>59.92 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (+5.92%)</td><td>0.13 (+5.70%)</td><td>0.13 (-5.65%)</td><td>0.11 <b>(+20.47%)</b></td><td>0.02 (-17.68%)</td><td>219.60 (-16.98%)</td><td>185.92 (-6.85%)</td><td>187.90 (+5.98%)</td><td>152.30 (-5.58%)</td><td>27.35 <b>(-36.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>264.50 (n/a)</td><td>199.60 (n/a)</td><td>177.30 (n/a)</td><td>161.30 (n/a)</td><td>42.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (-3.06%)</td><td>0.14 <b>(+29.66%)</b></td><td>0.14 <b>(+33.73%)</b></td><td>0.12 <b>(+119.24%)</b></td><td>0.01 <b>(-72.04%)</b></td><td>156.50 <b>(-54.39%)</b></td><td>136.44 <b>(-33.53%)</b></td><td>132.20 <b>(-25.18%)</b></td><td>123.50 (+3.17%)</td><td>12.69 <b>(-86.46%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>343.10 (n/a)</td><td>205.28 (n/a)</td><td>176.70 (n/a)</td><td>119.70 (n/a)</td><td>93.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (+7.96%)</td><td>0.12 (+15.00%)</td><td>0.12 <b>(+21.98%)</b></td><td>0.09 <b>(+36.32%)</b></td><td>0.03 (-8.99%)</td><td>197.00 <b>(-26.63%)</b></td><td>157.56 (-15.22%)</td><td>152.20 (-18.00%)</td><td>118.60 (-7.42%)</td><td>33.18 <b>(-37.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>268.50 (n/a)</td><td>185.84 (n/a)</td><td>185.60 (n/a)</td><td>128.10 (n/a)</td><td>53.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (+10.77%)</td><td>0.12 (+12.35%)</td><td>0.12 (+4.29%)</td><td>0.10 <b>(+43.70%)</b></td><td>0.02 (-18.41%)</td><td>183.90 <b>(-30.42%)</b></td><td>154.46 (-13.91%)</td><td>158.70 (-4.11%)</td><td>117.20 (-9.71%)</td><td>24.93 <b>(-51.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>264.30 (n/a)</td><td>179.42 (n/a)</td><td>165.50 (n/a)</td><td>129.80 (n/a)</td><td>51.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 <b>(-21.07%)</b></td><td>0.11 (-15.53%)</td><td>0.11 <b>(-21.05%)</b></td><td>0.09 (-3.53%)</td><td>0.01 <b>(-61.55%)</b></td><td>196.00 (+3.65%)</td><td>174.18 (+15.93%)</td><td>169.10 <b>(+26.67%)</b></td><td>158.30 <b>(+26.64%)</b></td><td>14.21 <b>(-49.16%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>189.10 (n/a)</td><td>150.24 (n/a)</td><td>133.50 (n/a)</td><td>125.00 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (-9.93%)</td><td>0.12 (-6.88%)</td><td>0.11 (-10.48%)</td><td>0.10 (+10.03%)</td><td>0.02 <b>(-38.25%)</b></td><td>189.20 (-9.13%)</td><td>162.20 (+2.89%)</td><td>164.80 (+11.65%)</td><td>121.00 (+11.01%)</td><td>27.93 <b>(-39.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>208.20 (n/a)</td><td>157.64 (n/a)</td><td>147.60 (n/a)</td><td>109.00 (n/a)</td><td>46.05 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (+19.89%)</td><td>0.11 (+3.69%)</td><td>0.12 (+14.34%)</td><td>0.06 <b>(-30.58%)</b></td><td>0.03 <b>(+135.55%)</b></td><td>292.70 <b>(+44.05%)</b></td><td>183.38 (+3.01%)</td><td>154.10 (-12.54%)</td><td>130.20 (-16.59%)</td><td>64.31 <b>(+198.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>178.02 (n/a)</td><td>176.20 (n/a)</td><td>156.10 (n/a)</td><td>21.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (-12.56%)</td><td>0.10 (+4.27%)</td><td>0.10 (+17.68%)</td><td>0.09 (+9.36%)</td><td>0.01 <b>(-42.66%)</b></td><td>214.40 (-8.57%)</td><td>188.02 (-6.07%)</td><td>178.80 (-15.02%)</td><td>160.00 (+14.37%)</td><td>23.13 <b>(-36.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>234.50 (n/a)</td><td>200.18 (n/a)</td><td>210.40 (n/a)</td><td>139.90 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 <b>(+26.58%)</b></td><td>0.11 (+16.59%)</td><td>0.11 (+18.78%)</td><td>0.09 (+19.07%)</td><td>0.02 <b>(+51.98%)</b></td><td>213.70 (-16.03%)</td><td>178.82 (-13.15%)</td><td>169.80 (-15.82%)</td><td>129.20 <b>(-20.98%)</b></td><td>35.68 (+3.52%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>254.50 (n/a)</td><td>205.90 (n/a)</td><td>201.70 (n/a)</td><td>163.50 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.75 (+11.62%)</td><td>0.67 <b>(+30.61%)</b></td><td>0.72 <b>(+37.84%)</b></td><td>0.56 <b>(+56.58%)</b></td><td>0.09 <b>(-25.51%)</b></td><td>175.40 <b>(-36.15%)</b></td><td>148.36 <b>(-25.67%)</b></td><td>137.30 <b>(-27.47%)</b></td><td>131.70 (-10.41%)</td><td>20.07 <b>(-58.42%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.67 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>0.36 (n/a)</td><td>0.12 (n/a)</td><td>274.70 (n/a)</td><td>199.60 (n/a)</td><td>189.30 (n/a)</td><td>147.00 (n/a)</td><td>48.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.87 (+12.02%)</td><td>0.66 (+9.54%)</td><td>0.59 (+10.27%)</td><td>0.56 <b>(+29.16%)</b></td><td>0.13 (-11.21%)</td><td>176.90 <b>(-22.58%)</b></td><td>153.22 (-10.58%)</td><td>167.10 (-9.33%)</td><td>113.10 (-10.73%)</td><td>27.01 <b>(-35.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.78 (n/a)</td><td>0.60 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.15 (n/a)</td><td>228.50 (n/a)</td><td>171.34 (n/a)</td><td>184.30 (n/a)</td><td>126.70 (n/a)</td><td>42.11 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.71 (-6.80%)</td><td>0.61 <b>(+20.87%)</b></td><td>0.61 <b>(+29.34%)</b></td><td>0.52 <b>(+44.60%)</b></td><td>0.08 <b>(-50.20%)</b></td><td>188.80 <b>(-30.84%)</b></td><td>162.70 <b>(-21.28%)</b></td><td>161.90 <b>(-22.68%)</b></td><td>138.40 (+7.29%)</td><td>20.33 <b>(-61.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.76 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.15 (n/a)</td><td>273.00 (n/a)</td><td>206.68 (n/a)</td><td>209.40 (n/a)</td><td>129.00 (n/a)</td><td>52.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.61 (-18.16%)</td><td>0.49 (-8.96%)</td><td>0.50 (-6.72%)</td><td>0.27 <b>(-27.60%)</b></td><td>0.13 (-13.59%)</td><td>359.00 <b>(+38.13%)</b></td><td>218.82 (+11.72%)</td><td>196.10 (+7.22%)</td><td>162.40 <b>(+22.20%)</b></td><td>80.19 <b>(+48.50%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.74 (n/a)</td><td>0.53 (n/a)</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.15 (n/a)</td><td>259.90 (n/a)</td><td>195.86 (n/a)</td><td>182.90 (n/a)</td><td>132.90 (n/a)</td><td>54.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.54 (-3.37%)</td><td>0.47 (+6.23%)</td><td>0.48 (+10.10%)</td><td>0.35 (+8.13%)</td><td>0.07 <b>(-21.00%)</b></td><td>213.30 (-7.50%)</td><td>161.56 (-7.13%)</td><td>153.20 (-9.19%)</td><td>136.00 (+3.50%)</td><td>29.84 <b>(-21.51%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>230.60 (n/a)</td><td>173.96 (n/a)</td><td>168.70 (n/a)</td><td>131.40 (n/a)</td><td>38.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.59 (+2.14%)</td><td>0.42 (-6.76%)</td><td>0.43 (-2.98%)</td><td>0.30 <b>(-20.03%)</b></td><td>0.11 <b>(+26.14%)</b></td><td>248.50 <b>(+25.06%)</b></td><td>182.48 (+9.74%)</td><td>172.10 (+3.05%)</td><td>125.30 (-2.03%)</td><td>44.94 <b>(+52.16%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.58 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>198.70 (n/a)</td><td>166.28 (n/a)</td><td>167.00 (n/a)</td><td>127.90 (n/a)</td><td>29.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.56 (-4.23%)</td><td>0.43 (+2.34%)</td><td>0.40 (+0.15%)</td><td>0.35 (-0.11%)</td><td>0.09 (-11.16%)</td><td>212.70 (+0.09%)</td><td>177.82 (-2.87%)</td><td>184.70 (-0.16%)</td><td>130.80 (+4.39%)</td><td>33.20 (-6.05%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>212.50 (n/a)</td><td>183.08 (n/a)</td><td>185.00 (n/a)</td><td>125.30 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.50 <b>(-25.68%)</b></td><td>0.40 (-6.53%)</td><td>0.38 (+2.32%)</td><td>0.31 (-1.29%)</td><td>0.08 <b>(-46.99%)</b></td><td>236.40 (+1.33%)</td><td>189.82 (+2.82%)</td><td>192.00 (-2.24%)</td><td>147.40 <b>(+34.49%)</b></td><td>35.30 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.67 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.14 (n/a)</td><td>233.30 (n/a)</td><td>184.62 (n/a)</td><td>196.40 (n/a)</td><td>109.60 (n/a)</td><td>46.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.29 (+0.24%)</td><td>0.23 (-3.04%)</td><td>0.21 (-5.49%)</td><td>0.18 (-9.60%)</td><td>0.04 (+8.81%)</td><td>209.30 (+10.62%)</td><td>167.86 (+3.78%)</td><td>175.30 (+5.79%)</td><td>126.90 (-0.24%)</td><td>31.65 (+17.35%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>189.20 (n/a)</td><td>161.74 (n/a)</td><td>165.70 (n/a)</td><td>127.20 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.29 (+8.56%)</td><td>0.24 (+18.09%)</td><td>0.23 <b>(+20.18%)</b></td><td>0.20 (+19.84%)</td><td>0.03 (-11.81%)</td><td>184.70 (-16.58%)</td><td>157.82 (-16.09%)</td><td>160.60 (-16.79%)</td><td>128.50 (-7.89%)</td><td>20.94 <b>(-30.25%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>221.40 (n/a)</td><td>188.08 (n/a)</td><td>193.00 (n/a)</td><td>139.50 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 <b>(-29.51%)</b></td><td>0.18 <b>(-22.09%)</b></td><td>0.17 <b>(-20.06%)</b></td><td>0.16 (-10.79%)</td><td>0.02 <b>(-52.84%)</b></td><td>235.20 (+12.11%)</td><td>205.08 <b>(+25.51%)</b></td><td>214.30 <b>(+25.10%)</b></td><td>172.50 <b>(+41.86%)</b></td><td>25.41 <b>(-24.82%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>209.80 (n/a)</td><td>163.40 (n/a)</td><td>171.30 (n/a)</td><td>121.60 (n/a)</td><td>33.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.33 <b>(+34.81%)</b></td><td>0.23 (+8.31%)</td><td>0.26 <b>(+22.32%)</b></td><td>0.10 <b>(-46.73%)</b></td><td>0.09 <b>(+234.82%)</b></td><td>382.80 <b>(+87.65%)</b></td><td>191.16 (+9.37%)</td><td>144.20 (-18.25%)</td><td>113.00 <b>(-25.80%)</b></td><td>110.02 <b>(+407.84%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>204.00 (n/a)</td><td>174.78 (n/a)</td><td>176.40 (n/a)</td><td>152.30 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (+6.17%)</td><td>0.21 (+0.27%)</td><td>0.19 (-7.06%)</td><td>0.15 (-17.96%)</td><td>0.05 <b>(+108.26%)</b></td><td>238.00 <b>(+21.93%)</b></td><td>180.46 (+3.33%)</td><td>191.70 (+7.58%)</td><td>137.80 (-5.81%)</td><td>42.56 <b>(+129.65%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>174.64 (n/a)</td><td>178.20 (n/a)</td><td>146.30 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 <b>(+37.31%)</b></td><td>0.23 (+11.88%)</td><td>0.22 (+3.92%)</td><td>0.15 (-13.88%)</td><td>0.06 <b>(+164.69%)</b></td><td>244.80 (+16.07%)</td><td>171.14 (-5.66%)</td><td>165.20 (-3.79%)</td><td>116.40 <b>(-27.16%)</b></td><td>49.93 <b>(+123.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>181.40 (n/a)</td><td>171.70 (n/a)</td><td>159.80 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.30 <b>(+22.49%)</b></td><td>0.21 (+3.68%)</td><td>0.19 (-10.30%)</td><td>0.11 <b>(-22.05%)</b></td><td>0.08 <b>(+77.26%)</b></td><td>348.60 <b>(+28.26%)</b></td><td>199.86 (+5.42%)</td><td>195.70 (+11.45%)</td><td>121.50 (-18.40%)</td><td>89.85 <b>(+82.97%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>271.80 (n/a)</td><td>189.58 (n/a)</td><td>175.60 (n/a)</td><td>148.90 (n/a)</td><td>49.11 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (+0.15%)</td><td>0.18 (+9.26%)</td><td>0.19 <b>(+36.04%)</b></td><td>0.11 (-16.33%)</td><td>0.07 (+15.78%)</td><td>343.90 (+19.53%)</td><td>235.14 (-2.73%)</td><td>191.10 <b>(-26.50%)</b></td><td>132.20 (-0.15%)</td><td>99.03 <b>(+58.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>287.70 (n/a)</td><td>241.74 (n/a)</td><td>260.00 (n/a)</td><td>132.40 (n/a)</td><td>62.66 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.31 (+15.68%)</td><td>0.27 (+12.08%)</td><td>0.26 (+1.98%)</td><td>0.24 <b>(+24.91%)</b></td><td>0.03 (-9.11%)</td><td>170.30 (-19.93%)</td><td>155.42 (-11.36%)</td><td>160.30 (-1.90%)</td><td>131.00 (-13.59%)</td><td>15.23 <b>(-38.34%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>212.70 (n/a)</td><td>175.34 (n/a)</td><td>163.40 (n/a)</td><td>151.60 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 (+6.22%)</td><td>0.27 (+0.33%)</td><td>0.26 (-4.96%)</td><td>0.23 (+1.10%)</td><td>0.04 <b>(+41.56%)</b></td><td>176.80 (-1.06%)</td><td>152.62 (+0.37%)</td><td>156.40 (+5.18%)</td><td>127.10 (-5.85%)</td><td>20.93 <b>(+28.70%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>178.70 (n/a)</td><td>152.06 (n/a)</td><td>148.70 (n/a)</td><td>135.00 (n/a)</td><td>16.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 (-1.40%)</td><td>0.28 (+13.00%)</td><td>0.28 (-2.32%)</td><td>0.24 <b>(+98.72%)</b></td><td>0.04 <b>(-55.61%)</b></td><td>172.10 <b>(-49.68%)</b></td><td>149.36 <b>(-22.35%)</b></td><td>146.50 (+2.38%)</td><td>127.60 (+1.43%)</td><td>21.69 <b>(-76.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.29 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>342.00 (n/a)</td><td>192.34 (n/a)</td><td>143.10 (n/a)</td><td>125.80 (n/a)</td><td>92.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 (-4.68%)</td><td>0.22 (-16.78%)</td><td>0.23 (-14.27%)</td><td>0.11 <b>(-33.55%)</b></td><td>0.08 (+19.72%)</td><td>375.40 <b>(+50.46%)</b></td><td>218.20 <b>(+29.46%)</b></td><td>179.60 (+16.62%)</td><td>128.00 (+4.92%)</td><td>98.32 <b>(+92.73%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>249.50 (n/a)</td><td>168.54 (n/a)</td><td>154.00 (n/a)</td><td>122.00 (n/a)</td><td>51.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 <b>(-29.15%)</b></td><td>0.20 (-19.50%)</td><td>0.22 (-8.47%)</td><td>0.16 <b>(-24.51%)</b></td><td>0.03 <b>(-39.68%)</b></td><td>260.20 <b>(+32.48%)</b></td><td>204.60 <b>(+23.21%)</b></td><td>188.60 (+9.27%)</td><td>175.40 <b>(+41.11%)</b></td><td>33.73 (+14.88%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>196.40 (n/a)</td><td>166.06 (n/a)</td><td>172.60 (n/a)</td><td>124.30 (n/a)</td><td>29.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 <b>(-33.68%)</b></td><td>0.22 (-10.96%)</td><td>0.22 (-13.33%)</td><td>0.18 <b>(+39.60%)</b></td><td>0.03 <b>(-67.49%)</b></td><td>227.10 <b>(-28.36%)</b></td><td>189.02 (+0.33%)</td><td>184.90 (+15.35%)</td><td>158.60 <b>(+50.76%)</b></td><td>27.30 <b>(-65.73%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>317.00 (n/a)</td><td>188.40 (n/a)</td><td>160.30 (n/a)</td><td>105.20 (n/a)</td><td>79.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.33 (+11.39%)</td><td>0.21 (-5.32%)</td><td>0.21 (-14.04%)</td><td>0.11 (-1.85%)</td><td>0.09 <b>(+31.54%)</b></td><td>373.60 (+1.88%)</td><td>233.84 (+11.24%)</td><td>199.30 (+16.28%)</td><td>124.90 (-10.21%)</td><td>104.56 (+15.53%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>366.70 (n/a)</td><td>210.22 (n/a)</td><td>171.40 (n/a)</td><td>139.10 (n/a)</td><td>90.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (+1.43%)</td><td>0.20 (-2.57%)</td><td>0.20 (-0.29%)</td><td>0.12 (-16.19%)</td><td>0.06 <b>(+42.08%)</b></td><td>351.20 (+19.29%)</td><td>226.04 (+7.35%)</td><td>201.20 (+0.30%)</td><td>162.00 (-1.40%)</td><td>78.70 <b>(+57.59%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>294.40 (n/a)</td><td>210.56 (n/a)</td><td>200.60 (n/a)</td><td>164.30 (n/a)</td><td>49.94 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (+8.65%)</td><td>0.22 (+14.25%)</td><td>0.22 <b>(+23.01%)</b></td><td>0.19 (+18.73%)</td><td>0.03 (-14.55%)</td><td>180.20 (-15.79%)</td><td>161.56 (-13.51%)</td><td>161.90 (-18.68%)</td><td>128.50 (-8.02%)</td><td>21.21 <b>(-34.51%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>214.00 (n/a)</td><td>186.80 (n/a)</td><td>199.10 (n/a)</td><td>139.70 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (+17.26%)</td><td>0.23 (+17.88%)</td><td>0.24 <b>(+28.00%)</b></td><td>0.17 (+1.11%)</td><td>0.04 <b>(+77.58%)</b></td><td>201.00 (-1.13%)</td><td>156.58 (-13.56%)</td><td>143.80 <b>(-21.89%)</b></td><td>127.50 (-14.72%)</td><td>31.40 <b>(+50.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>181.14 (n/a)</td><td>184.10 (n/a)</td><td>149.50 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (+13.59%)</td><td>0.20 (-5.43%)</td><td>0.20 (-4.27%)</td><td>0.13 <b>(-30.98%)</b></td><td>0.05 <b>(+150.21%)</b></td><td>267.30 <b>(+44.88%)</b></td><td>182.92 (+11.05%)</td><td>172.80 (+4.47%)</td><td>127.40 (-11.96%)</td><td>51.36 <b>(+230.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>184.50 (n/a)</td><td>164.72 (n/a)</td><td>165.40 (n/a)</td><td>144.70 (n/a)</td><td>15.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (-7.42%)</td><td>0.17 (-10.01%)</td><td>0.17 (-12.79%)</td><td>0.13 <b>(-21.46%)</b></td><td>0.03 <b>(+45.42%)</b></td><td>270.30 <b>(+27.32%)</b></td><td>206.74 (+13.44%)</td><td>203.20 (+14.67%)</td><td>167.40 (+8.07%)</td><td>42.64 <b>(+93.88%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>212.30 (n/a)</td><td>182.24 (n/a)</td><td>177.20 (n/a)</td><td>154.90 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (-3.47%)</td><td>0.20 (+0.35%)</td><td>0.20 (+3.70%)</td><td>0.17 (-1.68%)</td><td>0.03 (-13.43%)</td><td>200.80 (+1.72%)</td><td>174.26 (-0.75%)</td><td>176.40 (-3.61%)</td><td>139.50 (+3.56%)</td><td>22.79 (-9.00%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>197.40 (n/a)</td><td>175.58 (n/a)</td><td>183.00 (n/a)</td><td>134.70 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.37 <b>(+48.07%)</b></td><td>0.25 <b>(+23.51%)</b></td><td>0.23 <b>(+21.41%)</b></td><td>0.19 (+11.06%)</td><td>0.07 <b>(+117.64%)</b></td><td>185.60 (-9.95%)</td><td>146.10 (-16.53%)</td><td>148.80 (-17.65%)</td><td>95.20 <b>(-32.43%)</b></td><td>32.59 <b>(+26.50%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>206.10 (n/a)</td><td>175.04 (n/a)</td><td>180.70 (n/a)</td><td>140.90 (n/a)</td><td>25.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (+2.83%)</td><td>0.22 (+13.19%)</td><td>0.22 (+17.24%)</td><td>0.17 (+14.52%)</td><td>0.05 (-0.31%)</td><td>209.90 (-12.69%)</td><td>164.34 (-12.39%)</td><td>157.30 (-14.70%)</td><td>127.00 (-2.68%)</td><td>38.12 (-17.48%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>240.40 (n/a)</td><td>187.58 (n/a)</td><td>184.40 (n/a)</td><td>130.50 (n/a)</td><td>46.19 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 <b>(+22.89%)</b></td><td>0.20 (+17.39%)</td><td>0.21 <b>(+33.61%)</b></td><td>0.10 (-11.26%)</td><td>0.06 <b>(+52.30%)</b></td><td>331.70 (+12.71%)</td><td>191.12 (-9.64%)</td><td>163.90 <b>(-25.16%)</b></td><td>130.10 (-18.64%)</td><td>81.65 <b>(+50.00%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>294.30 (n/a)</td><td>211.50 (n/a)</td><td>219.00 (n/a)</td><td>159.90 (n/a)</td><td>54.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.81 (-6.72%)</td><td>0.72 (+1.47%)</td><td>0.75 (+5.51%)</td><td>0.61 (+7.66%)</td><td>0.09 <b>(-21.85%)</b></td><td>216.30 (-7.13%)</td><td>185.48 (-2.18%)</td><td>174.80 (-5.21%)</td><td>161.10 (+7.19%)</td><td>23.38 <b>(-21.26%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.87 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.56 (n/a)</td><td>0.11 (n/a)</td><td>232.90 (n/a)</td><td>189.62 (n/a)</td><td>184.40 (n/a)</td><td>150.30 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.13 <b>(+41.03%)</b></td><td>0.80 (+15.96%)</td><td>0.74 (+13.39%)</td><td>0.62 (+0.04%)</td><td>0.21 <b>(+150.54%)</b></td><td>212.60 (-0.05%)</td><td>171.92 (-10.48%)</td><td>176.50 (-11.84%)</td><td>116.00 <b>(-29.10%)</b></td><td>39.73 <b>(+77.75%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.65 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>212.70 (n/a)</td><td>192.04 (n/a)</td><td>200.20 (n/a)</td><td>163.60 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.85 (-0.33%)</td><td>0.70 (-4.36%)</td><td>0.75 (-3.35%)</td><td>0.35 <b>(-33.63%)</b></td><td>0.21 <b>(+60.24%)</b></td><td>376.90 <b>(+50.64%)</b></td><td>209.08 (+13.42%)</td><td>175.90 (+3.47%)</td><td>153.80 (+0.33%)</td><td>94.66 <b>(+144.89%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.86 (n/a)</td><td>0.73 (n/a)</td><td>0.77 (n/a)</td><td>0.52 (n/a)</td><td>0.13 (n/a)</td><td>250.20 (n/a)</td><td>184.34 (n/a)</td><td>170.00 (n/a)</td><td>153.30 (n/a)</td><td>38.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.00 (+0.00%)</td><td>0.00 (+1.92%)</td><td>0.00 (+10.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+33.01%)</b></td><td>4759.67 (+2.86%)</td><td>4049.40 (+0.77%)</td><td>3723.25 (-8.64%)</td><td>3514.63 (+0.49%)</td><td>641.77 <b>(+47.74%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4627.55 (n/a)</td><td>4018.43 (n/a)</td><td>4075.53 (n/a)</td><td>3497.60 (n/a)</td><td>434.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.00 (+0.00%)</td><td>0.00 (-0.94%)</td><td>0.00 (+4.55%)</td><td>0.00 (-5.56%)</td><td>0.00 <b>(+47.04%)</b></td><td>4886.68 (+6.75%)</td><td>3974.46 (+2.70%)</td><td>3563.96 (-4.03%)</td><td>3537.80 (-0.29%)</td><td>608.26 <b>(+47.58%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4577.85 (n/a)</td><td>3869.88 (n/a)</td><td>3713.49 (n/a)</td><td>3548.04 (n/a)</td><td>412.17 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (+0.07%)</td><td>0.24 <b>(+30.01%)</b></td><td>0.26 <b>(+62.41%)</b></td><td>0.18 (+18.62%)</td><td>0.05 (-11.19%)</td><td>11546.64 (-15.70%)</td><td>9176.72 <b>(-24.30%)</b></td><td>8073.83 <b>(-38.43%)</b></td><td>7538.74 (-0.07%)</td><td>1981.56 <b>(-22.98%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>13696.68 (n/a)</td><td>12121.75 (n/a)</td><td>13112.31 (n/a)</td><td>7543.78 (n/a)</td><td>2572.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>5.73 (n/a)</td><td>5.07 (n/a)</td><td>4.77 (n/a)</td><td>4.62 (n/a)</td><td>0.53 (n/a)</td><td>226.90 (n/a)</td><td>208.66 (n/a)</td><td>220.00 (n/a)</td><td>183.10 (n/a)</td><td>21.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>5.15 (n/a)</td><td>4.68 (n/a)</td><td>4.63 (n/a)</td><td>4.15 (n/a)</td><td>0.44 (n/a)</td><td>252.80 (n/a)</td><td>225.74 (n/a)</td><td>226.30 (n/a)</td><td>203.50 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>5.88 (n/a)</td><td>5.12 (n/a)</td><td>5.33 (n/a)</td><td>4.23 (n/a)</td><td>0.69 (n/a)</td><td>248.00 (n/a)</td><td>207.84 (n/a)</td><td>196.70 (n/a)</td><td>178.30 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.00 (n/a)</td><td>5.26 (n/a)</td><td>5.06 (n/a)</td><td>4.76 (n/a)</td><td>0.56 (n/a)</td><td>220.30 (n/a)</td><td>201.04 (n/a)</td><td>207.10 (n/a)</td><td>174.90 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.30 (n/a)</td><td>8.41 (n/a)</td><td>8.52 (n/a)</td><td>7.51 (n/a)</td><td>0.78 (n/a)</td><td>279.30 (n/a)</td><td>251.24 (n/a)</td><td>246.20 (n/a)</td><td>225.50 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>8.76 (n/a)</td><td>8.05 (n/a)</td><td>8.05 (n/a)</td><td>7.25 (n/a)</td><td>0.54 (n/a)</td><td>289.40 (n/a)</td><td>261.60 (n/a)</td><td>260.50 (n/a)</td><td>239.40 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.70 (n/a)</td><td>8.21 (n/a)</td><td>7.93 (n/a)</td><td>7.49 (n/a)</td><td>0.89 (n/a)</td><td>280.00 (n/a)</td><td>257.62 (n/a)</td><td>264.60 (n/a)</td><td>216.30 (n/a)</td><td>25.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.52 (n/a)</td><td>9.04 (n/a)</td><td>9.09 (n/a)</td><td>8.25 (n/a)</td><td>0.48 (n/a)</td><td>254.10 (n/a)</td><td>232.42 (n/a)</td><td>230.70 (n/a)</td><td>220.30 (n/a)</td><td>12.89 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>10.65 (n/a)</td><td>9.15 (n/a)</td><td>10.40 (n/a)</td><td>6.04 (n/a)</td><td>2.06 (n/a)</td><td>347.20 (n/a)</td><td>240.90 (n/a)</td><td>201.60 (n/a)</td><td>197.00 (n/a)</td><td>65.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>11.01 (n/a)</td><td>9.57 (n/a)</td><td>9.58 (n/a)</td><td>8.09 (n/a)</td><td>1.06 (n/a)</td><td>259.20 (n/a)</td><td>221.38 (n/a)</td><td>219.00 (n/a)</td><td>190.50 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>12.63 (n/a)</td><td>12.01 (n/a)</td><td>11.86 (n/a)</td><td>11.18 (n/a)</td><td>0.59 (n/a)</td><td>375.10 (n/a)</td><td>349.84 (n/a)</td><td>353.60 (n/a)</td><td>332.00 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>12.39 (n/a)</td><td>11.78 (n/a)</td><td>12.24 (n/a)</td><td>10.95 (n/a)</td><td>0.73 (n/a)</td><td>383.10 (n/a)</td><td>357.10 (n/a)</td><td>342.60 (n/a)</td><td>338.50 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>13.38 (n/a)</td><td>11.80 (n/a)</td><td>11.75 (n/a)</td><td>10.19 (n/a)</td><td>1.16 (n/a)</td><td>411.50 (n/a)</td><td>358.24 (n/a)</td><td>356.90 (n/a)</td><td>313.50 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>15.30 (n/a)</td><td>13.41 (n/a)</td><td>12.82 (n/a)</td><td>12.26 (n/a)</td><td>1.35 (n/a)</td><td>342.30 (n/a)</td><td>315.32 (n/a)</td><td>327.10 (n/a)</td><td>274.10 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>14.21 (n/a)</td><td>13.30 (n/a)</td><td>13.43 (n/a)</td><td>11.90 (n/a)</td><td>0.98 (n/a)</td><td>352.60 (n/a)</td><td>316.78 (n/a)</td><td>312.30 (n/a)</td><td>295.10 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>15.22 (n/a)</td><td>13.91 (n/a)</td><td>14.33 (n/a)</td><td>11.60 (n/a)</td><td>1.43 (n/a)</td><td>361.50 (n/a)</td><td>304.26 (n/a)</td><td>292.60 (n/a)</td><td>275.50 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>14.41 (n/a)</td><td>12.77 (n/a)</td><td>12.46 (n/a)</td><td>10.26 (n/a)</td><td>1.71 (n/a)</td><td>408.70 (n/a)</td><td>333.62 (n/a)</td><td>336.70 (n/a)</td><td>291.00 (n/a)</td><td>47.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>16.18 (n/a)</td><td>13.85 (n/a)</td><td>15.00 (n/a)</td><td>10.69 (n/a)</td><td>2.30 (n/a)</td><td>392.40 (n/a)</td><td>310.24 (n/a)</td><td>279.60 (n/a)</td><td>259.20 (n/a)</td><td>55.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.41 (n/a)</td><td>2.60 (n/a)</td><td>2.61 (n/a)</td><td>1.93 (n/a)</td><td>0.57 (n/a)</td><td>271.30 (n/a)</td><td>209.18 (n/a)</td><td>201.00 (n/a)</td><td>153.60 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.15 (n/a)</td><td>5.18 (n/a)</td><td>5.07 (n/a)</td><td>4.64 (n/a)</td><td>0.57 (n/a)</td><td>226.00 (n/a)</td><td>204.16 (n/a)</td><td>206.80 (n/a)</td><td>170.50 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.31 (n/a)</td><td>8.45 (n/a)</td><td>9.02 (n/a)</td><td>6.91 (n/a)</td><td>1.03 (n/a)</td><td>303.40 (n/a)</td><td>251.40 (n/a)</td><td>232.50 (n/a)</td><td>225.30 (n/a)</td><td>33.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.91 (n/a)</td><td>3.16 (n/a)</td><td>3.27 (n/a)</td><td>2.16 (n/a)</td><td>0.75 (n/a)</td><td>242.40 (n/a)</td><td>174.48 (n/a)</td><td>160.20 (n/a)</td><td>134.20 (n/a)</td><td>45.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.10 (n/a)</td><td>161.90 (n/a)</td><td>154.40 (n/a)</td><td>127.90 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>203.40 (n/a)</td><td>149.90 (n/a)</td><td>146.70 (n/a)</td><td>116.40 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>195.80 (n/a)</td><td>146.16 (n/a)</td><td>128.90 (n/a)</td><td>113.90 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>203.70 (n/a)</td><td>161.14 (n/a)</td><td>152.90 (n/a)</td><td>120.30 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>179.90 (n/a)</td><td>159.62 (n/a)</td><td>168.90 (n/a)</td><td>119.40 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.85 (n/a)</td><td>0.79 (n/a)</td><td>0.82 (n/a)</td><td>0.66 (n/a)</td><td>0.08 (n/a)</td><td>199.30 (n/a)</td><td>167.84 (n/a)</td><td>159.80 (n/a)</td><td>155.00 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.02 (n/a)</td><td>0.82 (n/a)</td><td>0.71 (n/a)</td><td>0.65 (n/a)</td><td>0.18 (n/a)</td><td>200.90 (n/a)</td><td>167.06 (n/a)</td><td>183.50 (n/a)</td><td>127.90 (n/a)</td><td>35.16 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.89 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.57 (n/a)</td><td>0.12 (n/a)</td><td>230.70 (n/a)</td><td>186.12 (n/a)</td><td>191.00 (n/a)</td><td>146.50 (n/a)</td><td>31.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.97 (n/a)</td><td>0.68 (n/a)</td><td>0.65 (n/a)</td><td>0.51 (n/a)</td><td>0.18 (n/a)</td><td>257.00 (n/a)</td><td>202.66 (n/a)</td><td>202.20 (n/a)</td><td>135.10 (n/a)</td><td>48.05 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>184.60 (n/a)</td><td>138.06 (n/a)</td><td>135.30 (n/a)</td><td>102.10 (n/a)</td><td>30.87 (n/a)</td>
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
