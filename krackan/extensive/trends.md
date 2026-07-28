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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (+7.09%)</td><td>0.04 <b>(+26.13%)</b></td><td>0.04 <b>(+22.07%)</b></td><td>0.04 <b>(+59.29%)</b></td><td>0.01 <b>(-40.74%)</b></td><td>172.10 <b>(-37.21%)</b></td><td>146.42 <b>(-24.09%)</b></td><td>144.70 (-18.06%)</td><td>126.50 (-6.64%)</td><td>17.91 <b>(-65.85%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>274.10 (n/a)</td><td>192.88 (n/a)</td><td>176.60 (n/a)</td><td>135.50 (n/a)</td><td>52.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (+7.95%)</td><td>0.04 (+3.76%)</td><td>0.04 (-4.30%)</td><td>0.03 (+2.66%)</td><td>0.01 <b>(+35.18%)</b></td><td>184.10 (-2.54%)</td><td>151.64 (-2.67%)</td><td>152.00 (+4.47%)</td><td>122.70 (-7.33%)</td><td>26.98 (+19.40%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>155.80 (n/a)</td><td>145.50 (n/a)</td><td>132.40 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 <b>(+20.65%)</b></td><td>0.04 (+3.73%)</td><td>0.03 (+3.04%)</td><td>0.03 (-14.56%)</td><td>0.01 <b>(+103.02%)</b></td><td>241.80 (+17.04%)</td><td>181.64 (+1.14%)</td><td>177.80 (-2.95%)</td><td>118.70 (-17.11%)</td><td>49.60 <b>(+99.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>179.60 (n/a)</td><td>183.20 (n/a)</td><td>143.20 (n/a)</td><td>24.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+7.00%)</td><td>0.04 (+12.77%)</td><td>0.04 (+5.25%)</td><td>0.04 <b>(+70.66%)</b></td><td>0.00 <b>(-67.58%)</b></td><td>172.00 <b>(-41.40%)</b></td><td>164.54 (-15.44%)</td><td>166.40 (-5.02%)</td><td>148.50 (-6.54%)</td><td>9.57 <b>(-82.92%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>293.50 (n/a)</td><td>194.58 (n/a)</td><td>175.20 (n/a)</td><td>158.90 (n/a)</td><td>56.03 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+19.99%)</td><td>0.04 (+10.32%)</td><td>0.04 (+11.38%)</td><td>0.03 (+0.20%)</td><td>0.00 <b>(+216.03%)</b></td><td>202.80 (-0.20%)</td><td>176.38 (-8.33%)</td><td>170.50 (-10.22%)</td><td>153.60 (-16.66%)</td><td>22.40 <b>(+164.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.20 (n/a)</td><td>192.40 (n/a)</td><td>189.90 (n/a)</td><td>184.30 (n/a)</td><td>8.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-14.35%)</td><td>0.03 (-10.35%)</td><td>0.03 (-12.87%)</td><td>0.03 <b>(+56.70%)</b></td><td>0.00 <b>(-59.24%)</b></td><td>221.40 <b>(-36.20%)</b></td><td>186.56 (-0.22%)</td><td>179.30 (+14.79%)</td><td>154.20 (+16.73%)</td><td>26.99 <b>(-70.26%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>347.00 (n/a)</td><td>186.98 (n/a)</td><td>156.20 (n/a)</td><td>132.10 (n/a)</td><td>90.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-17.97%)</td><td>0.04 (+3.02%)</td><td>0.04 (+19.31%)</td><td>0.03 (-14.36%)</td><td>0.01 <b>(-23.82%)</b></td><td>236.40 (+16.74%)</td><td>176.84 (-3.30%)</td><td>163.20 (-16.18%)</td><td>159.20 <b>(+21.90%)</b></td><td>33.39 (+12.41%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>182.88 (n/a)</td><td>194.70 (n/a)</td><td>130.60 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-3.82%)</td><td>0.04 (-0.84%)</td><td>0.04 (-0.61%)</td><td>0.03 (-8.00%)</td><td>0.00 (+19.02%)</td><td>204.30 (+8.73%)</td><td>170.30 (+1.20%)</td><td>163.20 (+0.62%)</td><td>159.20 (+3.98%)</td><td>19.09 <b>(+35.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>168.28 (n/a)</td><td>162.20 (n/a)</td><td>153.10 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (+9.87%)</td><td>0.08 (+4.58%)</td><td>0.08 (+3.87%)</td><td>0.06 (-9.48%)</td><td>0.01 <b>(+59.70%)</b></td><td>210.00 (+10.47%)</td><td>162.18 (-2.57%)</td><td>163.50 (-3.71%)</td><td>124.80 (-8.97%)</td><td>31.97 <b>(+63.52%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>166.46 (n/a)</td><td>169.80 (n/a)</td><td>137.10 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (-17.55%)</td><td>0.08 (-2.56%)</td><td>0.08 (+12.05%)</td><td>0.06 (-1.51%)</td><td>0.01 <b>(-43.87%)</b></td><td>202.50 (+1.55%)</td><td>158.02 (-0.03%)</td><td>150.40 (-10.74%)</td><td>135.10 <b>(+21.27%)</b></td><td>25.88 <b>(-27.55%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>199.40 (n/a)</td><td>158.06 (n/a)</td><td>168.50 (n/a)</td><td>111.40 (n/a)</td><td>35.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (+14.97%)</td><td>0.08 (+1.40%)</td><td>0.08 (+5.23%)</td><td>0.06 (-17.75%)</td><td>0.01 <b>(+192.93%)</b></td><td>212.50 <b>(+21.64%)</b></td><td>165.56 (+1.17%)</td><td>155.20 (-5.02%)</td><td>129.30 (-12.99%)</td><td>32.02 <b>(+213.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>174.70 (n/a)</td><td>163.64 (n/a)</td><td>163.40 (n/a)</td><td>148.60 (n/a)</td><td>10.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 <b>(-37.63%)</b></td><td>0.07 (-13.94%)</td><td>0.07 (+6.93%)</td><td>0.06 (+2.59%)</td><td>0.01 <b>(-72.49%)</b></td><td>207.10 (-2.54%)</td><td>175.06 (+7.65%)</td><td>174.60 (-6.48%)</td><td>151.60 <b>(+60.42%)</b></td><td>21.03 <b>(-56.32%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>212.50 (n/a)</td><td>162.62 (n/a)</td><td>186.70 (n/a)</td><td>94.50 (n/a)</td><td>48.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (-4.84%)</td><td>0.06 (-14.51%)</td><td>0.05 <b>(-20.29%)</b></td><td>0.05 (-18.86%)</td><td>0.01 <b>(+41.53%)</b></td><td>248.20 <b>(+23.24%)</b></td><td>213.58 (+19.27%)</td><td>233.90 <b>(+25.48%)</b></td><td>161.30 (+5.08%)</td><td>40.41 <b>(+87.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>179.08 (n/a)</td><td>186.40 (n/a)</td><td>153.50 (n/a)</td><td>21.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (-10.13%)</td><td>0.07 (-0.21%)</td><td>0.07 (+9.69%)</td><td>0.06 (+2.83%)</td><td>0.01 <b>(-31.37%)</b></td><td>198.60 (-2.74%)</td><td>172.00 (-1.40%)</td><td>174.00 (-8.85%)</td><td>138.80 (+11.31%)</td><td>24.75 <b>(-25.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>204.20 (n/a)</td><td>174.44 (n/a)</td><td>190.90 (n/a)</td><td>124.70 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(-24.42%)</b></td><td>0.06 (-14.58%)</td><td>0.06 (-11.99%)</td><td>0.06 (+17.24%)</td><td>0.00 <b>(-76.16%)</b></td><td>212.70 (-14.72%)</td><td>200.88 (+12.19%)</td><td>207.60 (+13.63%)</td><td>184.10 <b>(+32.26%)</b></td><td>12.41 <b>(-72.34%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>249.40 (n/a)</td><td>179.06 (n/a)</td><td>182.70 (n/a)</td><td>139.20 (n/a)</td><td>44.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(-36.51%)</b></td><td>0.06 <b>(-26.90%)</b></td><td>0.06 <b>(-24.92%)</b></td><td>0.04 (+6.18%)</td><td>0.01 <b>(-60.13%)</b></td><td>302.10 (-5.80%)</td><td>227.46 <b>(+24.81%)</b></td><td>213.20 <b>(+33.25%)</b></td><td>179.20 <b>(+57.47%)</b></td><td>46.44 <b>(-42.74%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>320.70 (n/a)</td><td>182.24 (n/a)</td><td>160.00 (n/a)</td><td>113.80 (n/a)</td><td>81.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 (-3.95%)</td><td>0.14 (-1.66%)</td><td>0.13 (-5.70%)</td><td>0.10 (+9.23%)</td><td>0.04 (-0.79%)</td><td>235.10 (-8.45%)</td><td>182.56 (+1.40%)</td><td>184.00 (+6.05%)</td><td>129.70 (+4.09%)</td><td>44.43 (-7.11%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>256.80 (n/a)</td><td>180.04 (n/a)</td><td>173.50 (n/a)</td><td>124.60 (n/a)</td><td>47.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 <b>(-21.82%)</b></td><td>0.14 <b>(-20.43%)</b></td><td>0.14 <b>(-26.36%)</b></td><td>0.10 <b>(-27.94%)</b></td><td>0.03 (-17.81%)</td><td>247.60 <b>(+38.71%)</b></td><td>181.14 <b>(+26.30%)</b></td><td>176.00 <b>(+35.80%)</b></td><td>143.10 <b>(+27.88%)</b></td><td>41.37 <b>(+42.15%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>178.50 (n/a)</td><td>143.42 (n/a)</td><td>129.60 (n/a)</td><td>111.90 (n/a)</td><td>29.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (+2.13%)</td><td>0.14 (+6.53%)</td><td>0.14 (+5.85%)</td><td>0.11 (+5.51%)</td><td>0.02 (+6.02%)</td><td>216.40 (-5.21%)</td><td>173.68 (-6.03%)</td><td>174.30 (-5.53%)</td><td>141.60 (-2.07%)</td><td>29.38 (-1.63%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>228.30 (n/a)</td><td>184.82 (n/a)</td><td>184.50 (n/a)</td><td>144.60 (n/a)</td><td>29.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (-14.21%)</td><td>0.13 (-11.87%)</td><td>0.13 (-9.16%)</td><td>0.11 (-10.35%)</td><td>0.01 (-14.69%)</td><td>218.30 (+11.55%)</td><td>191.10 (+13.41%)</td><td>184.00 (+10.05%)</td><td>170.00 (+16.60%)</td><td>20.42 (+10.87%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.70 (n/a)</td><td>168.50 (n/a)</td><td>167.20 (n/a)</td><td>145.80 (n/a)</td><td>18.42 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (+16.94%)</td><td>0.14 (+13.74%)</td><td>0.14 (+8.02%)</td><td>0.10 <b>(+44.37%)</b></td><td>0.03 (-7.30%)</td><td>244.20 <b>(-30.74%)</b></td><td>183.60 (-15.32%)</td><td>179.50 (-7.43%)</td><td>141.00 (-14.49%)</td><td>40.30 <b>(-47.74%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>352.60 (n/a)</td><td>216.82 (n/a)</td><td>193.90 (n/a)</td><td>164.90 (n/a)</td><td>77.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.18 (+11.33%)</td><td>0.15 (+19.17%)</td><td>0.14 (+19.48%)</td><td>0.13 <b>(+40.73%)</b></td><td>0.02 <b>(-32.78%)</b></td><td>182.10 <b>(-28.95%)</b></td><td>168.06 (-18.17%)</td><td>175.40 (-16.32%)</td><td>137.60 (-10.18%)</td><td>17.88 <b>(-57.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>256.30 (n/a)</td><td>205.38 (n/a)</td><td>209.60 (n/a)</td><td>153.20 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (+1.24%)</td><td>0.13 (+0.62%)</td><td>0.12 (-1.33%)</td><td>0.11 (+8.82%)</td><td>0.03 (-1.40%)</td><td>231.30 (-8.10%)</td><td>195.66 (-0.92%)</td><td>205.30 (+1.33%)</td><td>147.60 (-1.27%)</td><td>36.74 (-8.48%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>251.70 (n/a)</td><td>197.48 (n/a)</td><td>202.60 (n/a)</td><td>149.50 (n/a)</td><td>40.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (+4.21%)</td><td>0.14 <b>(+20.16%)</b></td><td>0.15 <b>(+40.95%)</b></td><td>0.12 <b>(+43.18%)</b></td><td>0.02 <b>(-26.57%)</b></td><td>210.80 <b>(-30.15%)</b></td><td>173.82 (-19.96%)</td><td>162.70 <b>(-29.04%)</b></td><td>143.80 (-4.01%)</td><td>31.06 <b>(-48.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>301.80 (n/a)</td><td>217.16 (n/a)</td><td>229.30 (n/a)</td><td>149.80 (n/a)</td><td>60.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.35 (-6.89%)</td><td>0.30 (+2.34%)</td><td>0.31 (+6.66%)</td><td>0.27 (+3.48%)</td><td>0.03 <b>(-30.96%)</b></td><td>184.20 (-3.36%)</td><td>163.46 (-3.15%)</td><td>158.70 (-6.21%)</td><td>141.00 (+7.39%)</td><td>17.31 <b>(-27.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>190.60 (n/a)</td><td>168.78 (n/a)</td><td>169.20 (n/a)</td><td>131.30 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.31 (-18.34%)</td><td>0.28 (-9.27%)</td><td>0.28 (-5.13%)</td><td>0.24 (+12.03%)</td><td>0.03 <b>(-60.87%)</b></td><td>204.70 (-10.73%)</td><td>175.76 (+6.34%)</td><td>173.40 (+5.41%)</td><td>156.40 <b>(+22.38%)</b></td><td>17.82 <b>(-56.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>229.30 (n/a)</td><td>165.28 (n/a)</td><td>164.50 (n/a)</td><td>127.80 (n/a)</td><td>40.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.36 (-5.79%)</td><td>0.29 (-4.27%)</td><td>0.31 (+13.31%)</td><td>0.22 (-11.27%)</td><td>0.05 (-1.18%)</td><td>224.00 (+12.68%)</td><td>176.40 (+4.95%)</td><td>160.20 (-11.74%)</td><td>138.10 (+6.15%)</td><td>35.14 <b>(+20.79%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>198.80 (n/a)</td><td>168.08 (n/a)</td><td>181.50 (n/a)</td><td>130.10 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.37 (+0.83%)</td><td>0.30 (+3.54%)</td><td>0.29 (-0.26%)</td><td>0.24 (+3.64%)</td><td>0.05 (-12.03%)</td><td>208.70 (-3.51%)</td><td>167.86 (-4.26%)</td><td>170.20 (+0.24%)</td><td>133.40 (-0.82%)</td><td>28.59 (-17.34%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>216.30 (n/a)</td><td>175.32 (n/a)</td><td>169.80 (n/a)</td><td>134.50 (n/a)</td><td>34.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.38 (+17.77%)</td><td>0.33 (+13.93%)</td><td>0.33 (+10.28%)</td><td>0.24 (+4.51%)</td><td>0.05 <b>(+58.18%)</b></td><td>200.90 (-4.29%)</td><td>153.90 (-11.21%)</td><td>149.50 (-9.28%)</td><td>130.70 (-15.13%)</td><td>27.88 <b>(+28.32%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>209.90 (n/a)</td><td>173.34 (n/a)</td><td>164.80 (n/a)</td><td>154.00 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.44 <b>(+30.43%)</b></td><td>0.34 (+18.93%)</td><td>0.30 (+7.34%)</td><td>0.27 (+18.26%)</td><td>0.08 <b>(+71.93%)</b></td><td>181.30 (-15.44%)</td><td>149.50 (-14.29%)</td><td>165.70 (-6.86%)</td><td>110.50 <b>(-23.32%)</b></td><td>31.92 (+12.29%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>214.40 (n/a)</td><td>174.42 (n/a)</td><td>177.90 (n/a)</td><td>144.10 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.31 (-10.68%)</td><td>0.29 (-5.12%)</td><td>0.31 (+3.95%)</td><td>0.21 (-17.97%)</td><td>0.04 (+5.25%)</td><td>231.10 <b>(+21.89%)</b></td><td>175.92 (+6.15%)</td><td>159.60 (-3.80%)</td><td>156.80 (+11.92%)</td><td>31.55 <b>(+44.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>189.60 (n/a)</td><td>165.72 (n/a)</td><td>165.90 (n/a)</td><td>140.10 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.34 <b>(-21.16%)</b></td><td>0.28 (-4.77%)</td><td>0.26 (-2.42%)</td><td>0.24 (+17.68%)</td><td>0.04 <b>(-50.44%)</b></td><td>207.20 (-15.01%)</td><td>180.42 (+0.64%)</td><td>191.40 (+2.52%)</td><td>146.10 <b>(+26.82%)</b></td><td>25.53 <b>(-45.20%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.43 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>243.80 (n/a)</td><td>179.28 (n/a)</td><td>186.70 (n/a)</td><td>115.20 (n/a)</td><td>46.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (+19.65%)</td><td>0.01 (-5.15%)</td><td>0.01 (-13.68%)</td><td>0.01 <b>(-49.31%)</b></td><td>0.01 <b>(+296.74%)</b></td><td>372.90 <b>(+97.30%)</b></td><td>209.64 <b>(+22.55%)</b></td><td>191.50 (+15.85%)</td><td>125.40 (-16.40%)</td><td>100.79 <b>(+522.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>171.06 (n/a)</td><td>165.30 (n/a)</td><td>150.00 (n/a)</td><td>16.20 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 <b>(-22.80%)</b></td><td>0.01 (-13.47%)</td><td>0.01 (-8.45%)</td><td>0.01 (-5.91%)</td><td>0.00 <b>(-61.33%)</b></td><td>195.50 (+6.31%)</td><td>183.42 (+13.67%)</td><td>189.30 (+9.23%)</td><td>162.70 <b>(+29.54%)</b></td><td>13.07 <b>(-47.32%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>183.90 (n/a)</td><td>161.36 (n/a)</td><td>173.30 (n/a)</td><td>125.60 (n/a)</td><td>24.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (-2.41%)</td><td>0.02 (-8.09%)</td><td>0.02 <b>(-23.01%)</b></td><td>0.01 (+2.69%)</td><td>0.00 (-17.23%)</td><td>189.50 (-2.62%)</td><td>160.08 (+7.48%)</td><td>166.00 <b>(+29.89%)</b></td><td>123.70 (+2.40%)</td><td>29.14 (-15.93%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.60 (n/a)</td><td>148.94 (n/a)</td><td>127.80 (n/a)</td><td>120.80 (n/a)</td><td>34.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (+11.30%)</td><td>0.02 (+9.13%)</td><td>0.02 (+11.57%)</td><td>0.01 (+3.92%)</td><td>0.00 <b>(+51.84%)</b></td><td>197.90 (-3.79%)</td><td>170.14 (-7.49%)</td><td>170.40 (-10.36%)</td><td>139.10 (-10.14%)</td><td>25.66 <b>(+34.59%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>183.92 (n/a)</td><td>190.10 (n/a)</td><td>154.80 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (-13.31%)</td><td>0.01 (-0.76%)</td><td>0.01 (+5.86%)</td><td>0.01 <b>(+21.54%)</b></td><td>0.00 <b>(-67.18%)</b></td><td>205.10 (-17.70%)</td><td>181.08 (-3.01%)</td><td>177.60 (-5.58%)</td><td>166.20 (+15.34%)</td><td>14.45 <b>(-67.04%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>249.20 (n/a)</td><td>186.70 (n/a)</td><td>188.10 (n/a)</td><td>144.10 (n/a)</td><td>43.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (-18.13%)</td><td>0.01 (-18.50%)</td><td>0.01 <b>(-27.39%)</b></td><td>0.01 (-8.25%)</td><td>0.00 <b>(-35.41%)</b></td><td>223.60 (+8.97%)</td><td>191.34 <b>(+20.51%)</b></td><td>202.40 <b>(+37.69%)</b></td><td>148.10 <b>(+22.19%)</b></td><td>30.19 (-15.88%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.20 (n/a)</td><td>158.78 (n/a)</td><td>147.00 (n/a)</td><td>121.20 (n/a)</td><td>35.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 <b>(+37.26%)</b></td><td>0.02 (+8.81%)</td><td>0.01 (+12.32%)</td><td>0.01 (+1.35%)</td><td>0.00 <b>(+89.60%)</b></td><td>222.00 (-1.33%)</td><td>181.98 (-5.19%)</td><td>184.20 (-10.97%)</td><td>116.40 <b>(-27.16%)</b></td><td>41.13 <b>(+37.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>225.00 (n/a)</td><td>191.94 (n/a)</td><td>206.90 (n/a)</td><td>159.80 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (+4.17%)</td><td>0.01 (-0.55%)</td><td>0.01 (-5.14%)</td><td>0.01 (+5.00%)</td><td>0.00 (+3.03%)</td><td>233.00 (-4.74%)</td><td>212.98 (+0.52%)</td><td>224.30 (+5.40%)</td><td>171.50 (-4.03%)</td><td>26.07 (-5.33%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>244.60 (n/a)</td><td>211.88 (n/a)</td><td>212.80 (n/a)</td><td>178.70 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+0.52%)</td><td>0.03 (+12.80%)</td><td>0.03 (+4.00%)</td><td>0.03 (+17.66%)</td><td>0.01 (+5.07%)</td><td>186.80 (-15.01%)</td><td>159.12 (-11.46%)</td><td>179.20 (-3.81%)</td><td>124.10 (-0.56%)</td><td>31.82 (-9.29%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>179.72 (n/a)</td><td>186.30 (n/a)</td><td>124.80 (n/a)</td><td>35.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-7.68%)</td><td>0.03 (-6.92%)</td><td>0.03 (-1.09%)</td><td>0.03 (+0.24%)</td><td>0.00 <b>(-31.27%)</b></td><td>193.70 (-0.26%)</td><td>174.46 (+6.47%)</td><td>172.20 (+1.06%)</td><td>146.60 (+8.27%)</td><td>18.52 <b>(-24.54%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.20 (n/a)</td><td>163.86 (n/a)</td><td>170.40 (n/a)</td><td>135.40 (n/a)</td><td>24.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-17.19%)</td><td>0.03 (-13.50%)</td><td>0.03 (-2.78%)</td><td>0.02 <b>(-23.90%)</b></td><td>0.01 <b>(-20.48%)</b></td><td>269.70 <b>(+31.37%)</b></td><td>199.12 (+15.55%)</td><td>186.30 (+2.87%)</td><td>146.60 <b>(+20.76%)</b></td><td>45.23 <b>(+26.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>172.32 (n/a)</td><td>181.10 (n/a)</td><td>121.40 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-4.12%)</td><td>0.03 (+2.61%)</td><td>0.03 (-1.16%)</td><td>0.02 (-1.50%)</td><td>0.01 (+5.21%)</td><td>215.80 (+1.51%)</td><td>182.56 (-1.90%)</td><td>200.30 (+1.16%)</td><td>136.70 (+4.27%)</td><td>37.15 (+16.60%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>186.10 (n/a)</td><td>198.00 (n/a)</td><td>131.10 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-4.21%)</td><td>0.03 (-12.84%)</td><td>0.03 (-2.60%)</td><td>0.02 <b>(-24.43%)</b></td><td>0.01 (+18.47%)</td><td>247.30 <b>(+32.32%)</b></td><td>189.12 (+18.82%)</td><td>179.80 (+2.63%)</td><td>123.30 (+4.31%)</td><td>55.56 <b>(+69.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>159.16 (n/a)</td><td>175.20 (n/a)</td><td>118.20 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+3.06%)</td><td>0.02 (-8.52%)</td><td>0.02 (-12.16%)</td><td>0.02 <b>(-24.79%)</b></td><td>0.01 <b>(+47.93%)</b></td><td>319.00 <b>(+32.97%)</b></td><td>222.16 (+13.16%)</td><td>220.60 (+13.83%)</td><td>155.40 (-2.94%)</td><td>60.38 <b>(+94.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.90 (n/a)</td><td>196.32 (n/a)</td><td>193.80 (n/a)</td><td>160.10 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-18.68%)</td><td>0.03 (-6.42%)</td><td>0.03 (-0.36%)</td><td>0.02 (-2.44%)</td><td>0.00 <b>(-44.17%)</b></td><td>215.30 (+2.52%)</td><td>187.88 (+4.84%)</td><td>186.40 (+0.38%)</td><td>160.90 <b>(+23.01%)</b></td><td>23.48 <b>(-30.41%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>179.20 (n/a)</td><td>185.70 (n/a)</td><td>130.80 (n/a)</td><td>33.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+3.80%)</td><td>0.02 (-12.58%)</td><td>0.02 (-8.59%)</td><td>0.01 <b>(-36.74%)</b></td><td>0.01 <b>(+154.45%)</b></td><td>351.70 <b>(+58.07%)</b></td><td>253.10 <b>(+23.95%)</b></td><td>233.50 (+9.42%)</td><td>164.90 (-3.68%)</td><td>84.02 <b>(+298.15%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.50 (n/a)</td><td>204.20 (n/a)</td><td>213.40 (n/a)</td><td>171.20 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (-12.81%)</td><td>0.05 (-12.23%)</td><td>0.05 (-12.38%)</td><td>0.04 <b>(-22.22%)</b></td><td>0.01 (+10.10%)</td><td>252.30 <b>(+28.59%)</b></td><td>198.36 (+15.68%)</td><td>202.00 (+14.12%)</td><td>150.40 (+14.72%)</td><td>40.29 <b>(+66.99%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>171.48 (n/a)</td><td>177.00 (n/a)</td><td>131.10 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (+8.80%)</td><td>0.07 (-4.53%)</td><td>0.05 <b>(-21.65%)</b></td><td>0.05 (-19.50%)</td><td>0.02 <b>(+57.97%)</b></td><td>227.50 <b>(+24.25%)</b></td><td>169.16 (+10.82%)</td><td>192.00 <b>(+27.66%)</b></td><td>100.00 (-8.09%)</td><td>51.45 <b>(+81.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>183.10 (n/a)</td><td>152.64 (n/a)</td><td>150.40 (n/a)</td><td>108.80 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (+0.48%)</td><td>0.07 (+0.58%)</td><td>0.07 (+10.48%)</td><td>0.05 (+8.01%)</td><td>0.02 (+12.30%)</td><td>210.90 (-7.38%)</td><td>164.68 (+0.39%)</td><td>145.70 (-9.50%)</td><td>121.00 (-0.49%)</td><td>43.05 (+7.57%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>164.04 (n/a)</td><td>161.00 (n/a)</td><td>121.60 (n/a)</td><td>40.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (-9.33%)</td><td>0.06 (-5.37%)</td><td>0.06 (-18.90%)</td><td>0.05 (+7.81%)</td><td>0.01 <b>(-42.58%)</b></td><td>217.60 (-7.25%)</td><td>170.06 (+0.47%)</td><td>169.60 <b>(+23.26%)</b></td><td>135.60 (+10.33%)</td><td>31.31 <b>(-42.05%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>234.60 (n/a)</td><td>169.26 (n/a)</td><td>137.60 (n/a)</td><td>122.90 (n/a)</td><td>54.03 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(-23.95%)</b></td><td>0.06 (-12.47%)</td><td>0.06 <b>(-20.99%)</b></td><td>0.06 (+16.05%)</td><td>0.00 <b>(-74.40%)</b></td><td>189.50 (-13.82%)</td><td>169.52 (+7.96%)</td><td>164.90 <b>(+26.55%)</b></td><td>154.80 <b>(+31.52%)</b></td><td>13.27 <b>(-70.78%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>219.90 (n/a)</td><td>157.02 (n/a)</td><td>130.30 (n/a)</td><td>117.70 (n/a)</td><td>45.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (+6.22%)</td><td>0.06 (-9.77%)</td><td>0.05 <b>(-25.78%)</b></td><td>0.04 (-15.47%)</td><td>0.02 <b>(+99.91%)</b></td><td>234.30 (+18.27%)</td><td>194.70 (+16.20%)</td><td>225.10 <b>(+34.71%)</b></td><td>132.30 (-5.84%)</td><td>50.03 <b>(+128.70%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>167.56 (n/a)</td><td>167.10 (n/a)</td><td>140.50 (n/a)</td><td>21.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (+2.58%)</td><td>0.06 (-8.54%)</td><td>0.06 (-14.82%)</td><td>0.05 (-17.57%)</td><td>0.02 <b>(+60.24%)</b></td><td>222.60 <b>(+21.31%)</b></td><td>175.94 (+14.01%)</td><td>184.30 (+17.39%)</td><td>123.20 (-2.53%)</td><td>47.37 <b>(+91.70%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>183.50 (n/a)</td><td>154.32 (n/a)</td><td>157.00 (n/a)</td><td>126.40 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+2.30%)</td><td>0.05 (+4.68%)</td><td>0.05 (-0.20%)</td><td>0.04 <b>(+40.63%)</b></td><td>0.01 <b>(-47.07%)</b></td><td>234.50 <b>(-28.87%)</b></td><td>202.88 (-8.38%)</td><td>203.70 (+0.20%)</td><td>171.60 (-2.28%)</td><td>22.70 <b>(-64.02%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>329.70 (n/a)</td><td>221.44 (n/a)</td><td>203.30 (n/a)</td><td>175.60 (n/a)</td><td>63.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (-9.06%)</td><td>0.10 <b>(-27.32%)</b></td><td>0.11 (-19.71%)</td><td>0.06 <b>(-42.36%)</b></td><td>0.04 <b>(+56.32%)</b></td><td>375.10 <b>(+73.50%)</b></td><td>244.78 <b>(+56.81%)</b></td><td>190.60 <b>(+24.58%)</b></td><td>140.30 (+9.95%)</td><td>113.47 <b>(+215.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>216.20 (n/a)</td><td>156.10 (n/a)</td><td>153.00 (n/a)</td><td>127.60 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (+8.42%)</td><td>0.13 (+12.13%)</td><td>0.12 (+1.54%)</td><td>0.10 <b>(+80.79%)</b></td><td>0.03 <b>(-21.52%)</b></td><td>210.00 <b>(-44.69%)</b></td><td>170.48 (-18.27%)</td><td>172.10 (-1.54%)</td><td>120.80 (-7.79%)</td><td>35.79 <b>(-63.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>379.70 (n/a)</td><td>208.58 (n/a)</td><td>174.80 (n/a)</td><td>131.00 (n/a)</td><td>97.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (-12.43%)</td><td>0.12 (-1.37%)</td><td>0.12 (-10.20%)</td><td>0.09 <b>(+58.77%)</b></td><td>0.02 <b>(-51.98%)</b></td><td>240.20 <b>(-37.00%)</b></td><td>181.62 (-9.97%)</td><td>175.00 (+11.32%)</td><td>149.50 (+14.21%)</td><td>34.69 <b>(-66.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>381.30 (n/a)</td><td>201.74 (n/a)</td><td>157.20 (n/a)</td><td>130.90 (n/a)</td><td>102.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (+7.77%)</td><td>0.13 (+5.75%)</td><td>0.11 (-6.30%)</td><td>0.11 (+17.58%)</td><td>0.02 (+18.80%)</td><td>188.20 (-14.96%)</td><td>168.66 (-5.24%)</td><td>186.00 (+6.71%)</td><td>135.90 (-7.17%)</td><td>25.32 (-6.39%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>221.30 (n/a)</td><td>177.98 (n/a)</td><td>174.30 (n/a)</td><td>146.40 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (+2.53%)</td><td>0.13 (+6.98%)</td><td>0.15 <b>(+21.44%)</b></td><td>0.09 (-10.75%)</td><td>0.03 <b>(+61.97%)</b></td><td>232.20 (+12.07%)</td><td>164.56 (-3.14%)</td><td>139.20 (-17.63%)</td><td>129.80 (-2.48%)</td><td>45.69 <b>(+73.93%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.20 (n/a)</td><td>169.90 (n/a)</td><td>169.00 (n/a)</td><td>133.10 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (+3.21%)</td><td>0.13 (-4.40%)</td><td>0.13 (-0.13%)</td><td>0.09 <b>(-23.89%)</b></td><td>0.02 <b>(+114.49%)</b></td><td>226.00 <b>(+31.40%)</b></td><td>170.50 (+7.06%)</td><td>163.00 (+0.12%)</td><td>137.00 (-3.11%)</td><td>33.77 <b>(+182.11%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>159.26 (n/a)</td><td>162.80 (n/a)</td><td>141.40 (n/a)</td><td>11.97 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (-16.52%)</td><td>0.12 (-1.25%)</td><td>0.13 (+15.12%)</td><td>0.09 (-6.15%)</td><td>0.02 <b>(-29.71%)</b></td><td>235.00 (+6.53%)</td><td>178.74 (+0.10%)</td><td>163.50 (-13.12%)</td><td>156.70 (+19.80%)</td><td>32.43 (-7.59%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>220.60 (n/a)</td><td>178.56 (n/a)</td><td>188.20 (n/a)</td><td>130.80 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (+7.83%)</td><td>0.11 (+10.87%)</td><td>0.11 (+8.12%)</td><td>0.09 <b>(+30.72%)</b></td><td>0.02 (-14.15%)</td><td>239.00 <b>(-23.50%)</b></td><td>196.70 (-11.56%)</td><td>196.80 (-7.48%)</td><td>160.40 (-7.28%)</td><td>31.94 <b>(-41.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>312.40 (n/a)</td><td>222.42 (n/a)</td><td>212.70 (n/a)</td><td>173.00 (n/a)</td><td>54.16 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>162.08 (n/a)</td><td>177.80 (n/a)</td><td>127.80 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>187.42 (n/a)</td><td>185.30 (n/a)</td><td>147.20 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>150.18 (n/a)</td><td>146.00 (n/a)</td><td>119.60 (n/a)</td><td>25.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>325.30 (n/a)</td><td>207.06 (n/a)</td><td>189.40 (n/a)</td><td>156.30 (n/a)</td><td>67.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>196.10 (n/a)</td><td>158.58 (n/a)</td><td>158.10 (n/a)</td><td>112.10 (n/a)</td><td>35.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>299.20 (n/a)</td><td>179.32 (n/a)</td><td>158.90 (n/a)</td><td>124.80 (n/a)</td><td>68.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>194.14 (n/a)</td><td>186.90 (n/a)</td><td>175.80 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>206.22 (n/a)</td><td>207.80 (n/a)</td><td>172.60 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.00 (n/a)</td><td>163.50 (n/a)</td><td>170.10 (n/a)</td><td>140.70 (n/a)</td><td>18.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>180.10 (n/a)</td><td>153.80 (n/a)</td><td>160.20 (n/a)</td><td>125.40 (n/a)</td><td>22.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>178.62 (n/a)</td><td>167.30 (n/a)</td><td>155.70 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>168.96 (n/a)</td><td>160.80 (n/a)</td><td>157.50 (n/a)</td><td>14.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.32 (+16.59%)</td><td>0.30 (+18.23%)</td><td>0.30 (+18.44%)</td><td>0.28 (+16.41%)</td><td>0.02 (+11.27%)</td><td>175.70 (-14.13%)</td><td>164.24 (-15.44%)</td><td>166.40 (-15.58%)</td><td>152.60 (-14.22%)</td><td>9.09 (-18.76%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>204.60 (n/a)</td><td>194.22 (n/a)</td><td>197.10 (n/a)</td><td>177.90 (n/a)</td><td>11.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.02 (n/a)</td><td>180.00 (n/a)</td><td>166.48 (n/a)</td><td>168.90 (n/a)</td><td>150.80 (n/a)</td><td>11.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>229.60 (n/a)</td><td>184.10 (n/a)</td><td>185.00 (n/a)</td><td>143.10 (n/a)</td><td>32.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>226.80 (n/a)</td><td>202.88 (n/a)</td><td>197.10 (n/a)</td><td>191.30 (n/a)</td><td>13.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.20 (n/a)</td><td>163.68 (n/a)</td><td>169.30 (n/a)</td><td>134.50 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.30 (n/a)</td><td>187.64 (n/a)</td><td>183.20 (n/a)</td><td>163.40 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.00 (n/a)</td><td>181.50 (n/a)</td><td>181.90 (n/a)</td><td>170.00 (n/a)</td><td>7.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>289.00 (n/a)</td><td>216.52 (n/a)</td><td>210.70 (n/a)</td><td>158.10 (n/a)</td><td>48.16 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>158.82 (n/a)</td><td>165.60 (n/a)</td><td>127.50 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>161.32 (n/a)</td><td>156.10 (n/a)</td><td>141.40 (n/a)</td><td>19.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>174.80 (n/a)</td><td>172.40 (n/a)</td><td>149.70 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>198.12 (n/a)</td><td>194.00 (n/a)</td><td>160.30 (n/a)</td><td>32.42 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>194.10 (n/a)</td><td>161.90 (n/a)</td><td>164.80 (n/a)</td><td>132.10 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>162.20 (n/a)</td><td>142.70 (n/a)</td><td>141.20 (n/a)</td><td>122.10 (n/a)</td><td>17.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>177.30 (n/a)</td><td>150.30 (n/a)</td><td>153.30 (n/a)</td><td>126.20 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.20 (n/a)</td><td>149.14 (n/a)</td><td>145.90 (n/a)</td><td>128.20 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>208.10 (n/a)</td><td>172.90 (n/a)</td><td>160.90 (n/a)</td><td>146.60 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>204.50 (n/a)</td><td>184.50 (n/a)</td><td>195.30 (n/a)</td><td>156.50 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>232.30 (n/a)</td><td>193.78 (n/a)</td><td>193.70 (n/a)</td><td>160.00 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>158.34 (n/a)</td><td>170.00 (n/a)</td><td>116.70 (n/a)</td><td>27.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.00 (n/a)</td><td>153.92 (n/a)</td><td>154.70 (n/a)</td><td>129.70 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.40 (n/a)</td><td>143.92 (n/a)</td><td>139.50 (n/a)</td><td>128.50 (n/a)</td><td>16.25 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>271.60 (n/a)</td><td>190.40 (n/a)</td><td>170.60 (n/a)</td><td>158.50 (n/a)</td><td>47.16 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.00 (n/a)</td><td>172.64 (n/a)</td><td>177.50 (n/a)</td><td>148.80 (n/a)</td><td>16.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>174.68 (n/a)</td><td>169.30 (n/a)</td><td>152.90 (n/a)</td><td>22.75 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.10 (n/a)</td><td>187.16 (n/a)</td><td>159.10 (n/a)</td><td>155.90 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>263.10 (n/a)</td><td>221.04 (n/a)</td><td>222.60 (n/a)</td><td>179.10 (n/a)</td><td>29.77 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>166.62 (n/a)</td><td>178.70 (n/a)</td><td>138.90 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>151.64 (n/a)</td><td>146.60 (n/a)</td><td>133.80 (n/a)</td><td>16.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>165.66 (n/a)</td><td>169.10 (n/a)</td><td>126.10 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>182.52 (n/a)</td><td>179.20 (n/a)</td><td>152.40 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>196.86 (n/a)</td><td>197.60 (n/a)</td><td>168.30 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>203.92 (n/a)</td><td>208.30 (n/a)</td><td>164.70 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>186.18 (n/a)</td><td>196.20 (n/a)</td><td>153.00 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.30 (n/a)</td><td>234.40 (n/a)</td><td>220.40 (n/a)</td><td>180.00 (n/a)</td><td>75.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>160.58 (n/a)</td><td>172.40 (n/a)</td><td>116.70 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>165.98 (n/a)</td><td>165.30 (n/a)</td><td>142.60 (n/a)</td><td>22.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>168.48 (n/a)</td><td>169.10 (n/a)</td><td>127.50 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.80 (n/a)</td><td>167.58 (n/a)</td><td>171.10 (n/a)</td><td>120.80 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>174.62 (n/a)</td><td>171.40 (n/a)</td><td>151.40 (n/a)</td><td>19.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.80 (n/a)</td><td>175.78 (n/a)</td><td>178.80 (n/a)</td><td>141.30 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>288.40 (n/a)</td><td>194.46 (n/a)</td><td>180.60 (n/a)</td><td>142.00 (n/a)</td><td>56.77 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>208.50 (n/a)</td><td>200.06 (n/a)</td><td>202.80 (n/a)</td><td>181.10 (n/a)</td><td>10.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.50 (n/a)</td><td>179.02 (n/a)</td><td>172.10 (n/a)</td><td>155.40 (n/a)</td><td>29.06 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>207.00 (n/a)</td><td>176.34 (n/a)</td><td>181.70 (n/a)</td><td>150.90 (n/a)</td><td>22.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>189.40 (n/a)</td><td>156.76 (n/a)</td><td>160.90 (n/a)</td><td>120.10 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>202.30 (n/a)</td><td>176.70 (n/a)</td><td>175.90 (n/a)</td><td>140.60 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>235.60 (n/a)</td><td>201.08 (n/a)</td><td>223.50 (n/a)</td><td>151.40 (n/a)</td><td>41.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.00 (n/a)</td><td>180.58 (n/a)</td><td>167.80 (n/a)</td><td>156.00 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>336.00 (n/a)</td><td>229.62 (n/a)</td><td>210.60 (n/a)</td><td>189.30 (n/a)</td><td>60.65 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>4.79 (-2.48%)</td><td>4.06 (-4.18%)</td><td>4.08 (-2.10%)</td><td>3.48 (-6.67%)</td><td>0.59 <b>(+31.14%)</b></td><td>2704.10 (+7.14%)</td><td>2355.50 (+5.21%)</td><td>2302.50 (+2.14%)</td><td>1961.50 (+2.54%)</td><td>339.42 <b>(+48.93%)</b></td><td>1886.02 (-2.48%)</td><td>1597.04 (-4.18%)</td><td>1606.69 (-2.10%)</td><td>1368.05 (-6.67%)</td><td>230.71 <b>(+31.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.92 (n/a)</td><td>4.24 (n/a)</td><td>4.17 (n/a)</td><td>3.73 (n/a)</td><td>0.45 (n/a)</td><td>2523.80 (n/a)</td><td>2238.82 (n/a)</td><td>2254.20 (n/a)</td><td>1912.90 (n/a)</td><td>227.90 (n/a)</td><td>1933.89 (n/a)</td><td>1666.65 (n/a)</td><td>1641.11 (n/a)</td><td>1465.82 (n/a)</td><td>175.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.16 (+5.56%)</td><td>1.01 (+18.03%)</td><td>1.03 (+16.48%)</td><td>0.79 <b>(+34.33%)</b></td><td>0.14 <b>(-37.53%)</b></td><td>279.30 <b>(-25.54%)</b></td><td>223.26 (-18.77%)</td><td>214.20 (-14.15%)</td><td>191.10 (-5.26%)</td><td>34.21 <b>(-55.11%)</b></td><td>49.38 (+5.56%)</td><td>42.99 (+18.03%)</td><td>44.07 (+16.48%)</td><td>33.79 <b>(+34.33%)</b></td><td>5.94 <b>(-37.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.10 (n/a)</td><td>0.85 (n/a)</td><td>0.89 (n/a)</td><td>0.59 (n/a)</td><td>0.22 (n/a)</td><td>375.10 (n/a)</td><td>274.84 (n/a)</td><td>249.50 (n/a)</td><td>201.70 (n/a)</td><td>76.21 (n/a)</td><td>46.78 (n/a)</td><td>36.43 (n/a)</td><td>37.83 (n/a)</td><td>25.16 (n/a)</td><td>9.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.12 (-1.65%)</td><td>1.06 (+2.33%)</td><td>1.08 (+5.38%)</td><td>0.98 (-0.21%)</td><td>0.06 (-3.26%)</td><td>225.80 (+0.18%)</td><td>209.02 (-2.30%)</td><td>205.20 (-5.13%)</td><td>198.30 (+1.64%)</td><td>11.28 (-0.11%)</td><td>47.59 (-1.65%)</td><td>45.25 (+2.33%)</td><td>45.98 (+5.38%)</td><td>41.79 (-0.21%)</td><td>2.38 (-3.26%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.13 (n/a)</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>0.98 (n/a)</td><td>0.06 (n/a)</td><td>225.40 (n/a)</td><td>213.94 (n/a)</td><td>216.30 (n/a)</td><td>195.10 (n/a)</td><td>11.29 (n/a)</td><td>48.38 (n/a)</td><td>44.22 (n/a)</td><td>43.63 (n/a)</td><td>41.87 (n/a)</td><td>2.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.52 (+0.77%)</td><td>0.52 (+0.26%)</td><td>0.52 (+0.10%)</td><td>0.51 (-0.20%)</td><td>0.00 <b>(+270.33%)</b></td><td>48868.20 (+0.20%)</td><td>48543.44 (-0.26%)</td><td>48591.00 (-0.10%)</td><td>48245.70 (-0.77%)</td><td>235.65 <b>(+268.16%)</b></td><td>356.09 (+0.77%)</td><td>353.91 (+0.26%)</td><td>353.56 (+0.10%)</td><td>351.56 (-0.20%)</td><td>1.72 <b>(+270.33%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48771.60 (n/a)</td><td>48669.50 (n/a)</td><td>48640.20 (n/a)</td><td>48618.90 (n/a)</td><td>64.01 (n/a)</td><td>353.36 (n/a)</td><td>352.99 (n/a)</td><td>353.20 (n/a)</td><td>352.25 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (+1.13%)</td><td>0.22 (+0.75%)</td><td>0.21 (+0.45%)</td><td>0.21 (+1.04%)</td><td>0.00 (+2.89%)</td><td>117696.90 (-1.03%)</td><td>116953.58 (-0.75%)</td><td>117251.50 (-0.44%)</td><td>115511.80 (-1.12%)</td><td>845.72 (+0.53%)</td><td>148.73 (+1.13%)</td><td>146.90 (+0.75%)</td><td>146.52 (+0.45%)</td><td>145.97 (+1.04%)</td><td>1.07 (+2.89%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118923.00 (n/a)</td><td>117833.10 (n/a)</td><td>117774.60 (n/a)</td><td>116817.60 (n/a)</td><td>841.23 (n/a)</td><td>147.07 (n/a)</td><td>145.80 (n/a)</td><td>145.87 (n/a)</td><td>144.46 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.90 (+0.60%)</td><td>0.89 (+0.27%)</td><td>0.89 (-0.19%)</td><td>0.88 (+0.11%)</td><td>0.01 (-9.79%)</td><td>28683.80 (-0.11%)</td><td>28320.44 (-0.27%)</td><td>28296.60 (+0.19%)</td><td>27962.90 (-0.60%)</td><td>257.46 (-10.54%)</td><td>614.38 (+0.60%)</td><td>606.66 (+0.27%)</td><td>607.14 (-0.19%)</td><td>598.94 (+0.11%)</td><td>5.51 (-9.79%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28716.80 (n/a)</td><td>28396.52 (n/a)</td><td>28242.80 (n/a)</td><td>28132.10 (n/a)</td><td>287.80 (n/a)</td><td>610.69 (n/a)</td><td>605.05 (n/a)</td><td>608.29 (n/a)</td><td>598.25 (n/a)</td><td>6.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.60 (-0.18%)</td><td>3.47 (-0.91%)</td><td>3.53 (+0.46%)</td><td>3.33 (-0.74%)</td><td>0.13 <b>(+31.88%)</b></td><td>7568.30 (+0.75%)</td><td>7265.58 (+0.96%)</td><td>7128.50 (-0.45%)</td><td>6983.60 (+0.18%)</td><td>268.65 <b>(+33.45%)</b></td><td>2460.05 (-0.18%)</td><td>2367.12 (-0.91%)</td><td>2410.03 (+0.46%)</td><td>2269.97 (-0.74%)</td><td>86.77 <b>(+31.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.61 (n/a)</td><td>3.50 (n/a)</td><td>3.51 (n/a)</td><td>3.35 (n/a)</td><td>0.10 (n/a)</td><td>7512.10 (n/a)</td><td>7196.24 (n/a)</td><td>7161.00 (n/a)</td><td>6971.20 (n/a)</td><td>201.31 (n/a)</td><td>2464.39 (n/a)</td><td>2388.81 (n/a)</td><td>2399.08 (n/a)</td><td>2286.97 (n/a)</td><td>65.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.23 (-1.01%)</td><td>2.85 (-5.36%)</td><td>2.79 (-6.14%)</td><td>2.70 (-1.78%)</td><td>0.22 (+5.68%)</td><td>9322.20 (+1.81%)</td><td>8881.88 (+5.72%)</td><td>9024.80 (+6.54%)</td><td>7798.40 (+1.02%)</td><td>621.46 (+8.03%)</td><td>2203.00 (-1.01%)</td><td>1942.56 (-5.36%)</td><td>1903.62 (-6.14%)</td><td>1842.91 (-1.78%)</td><td>148.35 (+5.68%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.26 (n/a)</td><td>3.01 (n/a)</td><td>2.97 (n/a)</td><td>2.75 (n/a)</td><td>0.21 (n/a)</td><td>9156.60 (n/a)</td><td>8400.96 (n/a)</td><td>8471.10 (n/a)</td><td>7719.70 (n/a)</td><td>575.29 (n/a)</td><td>2225.46 (n/a)</td><td>2052.67 (n/a)</td><td>2028.05 (n/a)</td><td>1876.23 (n/a)</td><td>140.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.32 (+0.20%)</td><td>3.20 (-0.29%)</td><td>3.15 (-1.81%)</td><td>3.14 (+0.58%)</td><td>0.08 (+12.78%)</td><td>8004.90 (-0.58%)</td><td>7857.26 (+0.30%)</td><td>7978.90 (+1.85%)</td><td>7587.10 (-0.20%)</td><td>190.54 (+12.23%)</td><td>2264.35 (+0.20%)</td><td>2187.54 (-0.29%)</td><td>2153.16 (-1.81%)</td><td>2146.16 (+0.58%)</td><td>53.75 (+12.78%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.31 (n/a)</td><td>3.21 (n/a)</td><td>3.21 (n/a)</td><td>3.13 (n/a)</td><td>0.07 (n/a)</td><td>8051.40 (n/a)</td><td>7833.44 (n/a)</td><td>7834.10 (n/a)</td><td>7602.40 (n/a)</td><td>169.78 (n/a)</td><td>2259.79 (n/a)</td><td>2193.97 (n/a)</td><td>2192.95 (n/a)</td><td>2133.78 (n/a)</td><td>47.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.78 (+0.01%)</td><td>0.78 (+0.09%)</td><td>0.78 (+0.02%)</td><td>0.78 (+0.23%)</td><td>0.00 <b>(-86.95%)</b></td><td>96468.30 (-0.23%)</td><td>96451.74 (-0.09%)</td><td>96450.90 (-0.02%)</td><td>96434.40 (-0.01%)</td><td>14.73 <b>(-86.99%)</b></td><td>712.60 (+0.01%)</td><td>712.48 (+0.09%)</td><td>712.48 (+0.02%)</td><td>712.35 (+0.24%)</td><td>0.11 <b>(-86.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96695.00 (n/a)</td><td>96538.14 (n/a)</td><td>96468.70 (n/a)</td><td>96447.10 (n/a)</td><td>113.16 (n/a)</td><td>712.51 (n/a)</td><td>711.84 (n/a)</td><td>712.35 (n/a)</td><td>710.68 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.73 (+0.02%)</td><td>0.73 (+0.06%)</td><td>0.73 (+0.14%)</td><td>0.73 (-0.02%)</td><td>0.00 (+11.31%)</td><td>103928.20 (+0.02%)</td><td>103685.12 (-0.06%)</td><td>103629.30 (-0.14%)</td><td>103601.20 (-0.02%)</td><td>137.23 (+11.34%)</td><td>663.31 (+0.02%)</td><td>662.77 (+0.06%)</td><td>663.13 (+0.14%)</td><td>661.22 (-0.02%)</td><td>0.88 (+11.31%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103907.10 (n/a)</td><td>103752.34 (n/a)</td><td>103774.80 (n/a)</td><td>103622.90 (n/a)</td><td>123.25 (n/a)</td><td>663.17 (n/a)</td><td>662.34 (n/a)</td><td>662.20 (n/a)</td><td>661.36 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.70 (-0.08%)</td><td>0.69 (-0.10%)</td><td>0.69 (-0.15%)</td><td>0.69 (-0.05%)</td><td>0.00 (-9.12%)</td><td>108952.20 (+0.05%)</td><td>108707.94 (+0.10%)</td><td>108718.60 (+0.15%)</td><td>108519.40 (+0.08%)</td><td>159.53 (-9.02%)</td><td>633.25 (-0.08%)</td><td>632.15 (-0.10%)</td><td>632.09 (-0.15%)</td><td>630.73 (-0.05%)</td><td>0.93 (-9.12%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108896.20 (n/a)</td><td>108597.56 (n/a)</td><td>108551.30 (n/a)</td><td>108430.20 (n/a)</td><td>175.36 (n/a)</td><td>633.77 (n/a)</td><td>632.79 (n/a)</td><td>633.06 (n/a)</td><td>631.05 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.75 (+9.44%)</td><td>7.06 (+4.43%)</td><td>6.88 (-2.22%)</td><td>6.47 (+5.02%)</td><td>0.50 <b>(+20.98%)</b></td><td>1377.00 (-4.78%)</td><td>1267.76 (-4.16%)</td><td>1296.10 (+2.27%)</td><td>1149.90 (-8.62%)</td><td>88.67 (+5.47%)</td><td>466.90 (+9.44%)</td><td>425.17 (+4.43%)</td><td>414.23 (-2.22%)</td><td>389.88 (+5.02%)</td><td>30.21 <b>(+20.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.08 (n/a)</td><td>6.76 (n/a)</td><td>7.03 (n/a)</td><td>6.16 (n/a)</td><td>0.41 (n/a)</td><td>1446.10 (n/a)</td><td>1322.72 (n/a)</td><td>1267.30 (n/a)</td><td>1258.40 (n/a)</td><td>84.07 (n/a)</td><td>426.64 (n/a)</td><td>407.15 (n/a)</td><td>423.64 (n/a)</td><td>371.24 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.00 (+1.31%)</td><td>6.75 (+4.48%)</td><td>6.82 (+8.62%)</td><td>6.28 (+2.96%)</td><td>0.27 <b>(-25.47%)</b></td><td>1418.30 (-2.88%)</td><td>1322.46 (-4.39%)</td><td>1306.20 (-7.94%)</td><td>1273.40 (-1.29%)</td><td>56.08 <b>(-27.62%)</b></td><td>421.61 (+1.31%)</td><td>406.53 (+4.48%)</td><td>411.03 (+8.62%)</td><td>378.54 (+2.96%)</td><td>16.52 <b>(-25.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.91 (n/a)</td><td>6.46 (n/a)</td><td>6.28 (n/a)</td><td>6.10 (n/a)</td><td>0.37 (n/a)</td><td>1460.30 (n/a)</td><td>1383.24 (n/a)</td><td>1418.80 (n/a)</td><td>1290.00 (n/a)</td><td>77.48 (n/a)</td><td>416.16 (n/a)</td><td>389.12 (n/a)</td><td>378.41 (n/a)</td><td>367.65 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.91 (+5.24%)</td><td>5.79 (-0.50%)</td><td>6.17 (+6.49%)</td><td>4.20 (-11.02%)</td><td>1.05 <b>(+48.33%)</b></td><td>2120.80 (+12.38%)</td><td>1587.44 (+2.26%)</td><td>1445.10 (-6.09%)</td><td>1289.70 (-4.97%)</td><td>328.89 <b>(+59.76%)</b></td><td>416.29 (+5.24%)</td><td>348.60 (-0.50%)</td><td>371.52 (+6.49%)</td><td>253.15 (-11.02%)</td><td>63.33 <b>(+48.33%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.57 (n/a)</td><td>5.82 (n/a)</td><td>5.79 (n/a)</td><td>4.72 (n/a)</td><td>0.71 (n/a)</td><td>1887.10 (n/a)</td><td>1552.34 (n/a)</td><td>1538.80 (n/a)</td><td>1357.20 (n/a)</td><td>205.87 (n/a)</td><td>395.57 (n/a)</td><td>350.35 (n/a)</td><td>348.88 (n/a)</td><td>284.49 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.52 (+7.50%)</td><td>7.93 (+4.15%)</td><td>7.92 (+1.54%)</td><td>7.34 (+1.17%)</td><td>0.42 <b>(+30.43%)</b></td><td>4747.10 (-1.15%)</td><td>4407.78 (-3.91%)</td><td>4403.40 (-1.52%)</td><td>4092.00 (-6.97%)</td><td>232.41 (+19.20%)</td><td>524.81 (+7.50%)</td><td>488.28 (+4.15%)</td><td>487.69 (+1.54%)</td><td>452.38 (+1.17%)</td><td>25.67 <b>(+30.43%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.93 (n/a)</td><td>7.61 (n/a)</td><td>7.80 (n/a)</td><td>7.26 (n/a)</td><td>0.32 (n/a)</td><td>4802.50 (n/a)</td><td>4586.98 (n/a)</td><td>4471.20 (n/a)</td><td>4398.70 (n/a)</td><td>194.98 (n/a)</td><td>488.21 (n/a)</td><td>468.84 (n/a)</td><td>480.29 (n/a)</td><td>447.16 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.76 (+2.51%)</td><td>7.55 (+3.13%)</td><td>7.59 (+2.81%)</td><td>7.14 (+1.60%)</td><td>0.24 (-8.12%)</td><td>4886.50 (-1.57%)</td><td>4624.24 (-3.05%)</td><td>4596.40 (-2.73%)</td><td>4491.30 (-2.45%)</td><td>153.57 (-11.28%)</td><td>478.15 (+2.51%)</td><td>464.79 (+3.13%)</td><td>467.21 (+2.81%)</td><td>439.47 (+1.60%)</td><td>14.93 (-8.12%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.57 (n/a)</td><td>7.32 (n/a)</td><td>7.38 (n/a)</td><td>7.02 (n/a)</td><td>0.26 (n/a)</td><td>4964.40 (n/a)</td><td>4769.94 (n/a)</td><td>4725.40 (n/a)</td><td>4604.00 (n/a)</td><td>173.10 (n/a)</td><td>466.44 (n/a)</td><td>450.68 (n/a)</td><td>454.46 (n/a)</td><td>432.57 (n/a)</td><td>16.25 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.38 (+0.72%)</td><td>7.28 (+1.23%)</td><td>7.30 (+0.30%)</td><td>7.15 (+4.20%)</td><td>0.08 <b>(-56.46%)</b></td><td>4874.40 (-4.03%)</td><td>4786.36 (-1.26%)</td><td>4775.90 (-0.30%)</td><td>4727.00 (-0.71%)</td><td>54.35 <b>(-58.59%)</b></td><td>454.30 (+0.72%)</td><td>448.71 (+1.23%)</td><td>449.65 (+0.30%)</td><td>440.56 (+4.20%)</td><td>5.05 <b>(-56.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.32 (n/a)</td><td>7.20 (n/a)</td><td>7.28 (n/a)</td><td>6.86 (n/a)</td><td>0.19 (n/a)</td><td>5079.20 (n/a)</td><td>4847.50 (n/a)</td><td>4790.40 (n/a)</td><td>4760.90 (n/a)</td><td>131.24 (n/a)</td><td>451.07 (n/a)</td><td>443.26 (n/a)</td><td>448.29 (n/a)</td><td>422.80 (n/a)</td><td>11.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.79 (-0.33%)</td><td>0.79 (-0.07%)</td><td>0.79 (-0.01%)</td><td>0.79 (+0.03%)</td><td>0.00 <b>(-58.76%)</b></td><td>95891.20 (-0.03%)</td><td>95797.16 (+0.07%)</td><td>95754.10 (+0.01%)</td><td>95716.40 (+0.34%)</td><td>85.53 <b>(-58.62%)</b></td><td>717.95 (-0.33%)</td><td>717.34 (-0.07%)</td><td>717.67 (-0.01%)</td><td>716.64 (+0.03%)</td><td>0.64 <b>(-58.76%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95916.80 (n/a)</td><td>95727.14 (n/a)</td><td>95740.10 (n/a)</td><td>95396.80 (n/a)</td><td>206.68 (n/a)</td><td>720.35 (n/a)</td><td>717.87 (n/a)</td><td>717.77 (n/a)</td><td>716.45 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.74 (+0.28%)</td><td>0.73 (+0.11%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.19%)</td><td>0.00 <b>(+39.29%)</b></td><td>102965.30 (-0.19%)</td><td>102840.68 (-0.11%)</td><td>102886.50 (-0.03%)</td><td>102542.70 (-0.28%)</td><td>169.77 <b>(+38.56%)</b></td><td>670.15 (+0.28%)</td><td>668.21 (+0.11%)</td><td>667.92 (+0.03%)</td><td>667.40 (+0.19%)</td><td>1.11 <b>(+39.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103157.80 (n/a)</td><td>102949.30 (n/a)</td><td>102917.10 (n/a)</td><td>102832.00 (n/a)</td><td>122.53 (n/a)</td><td>668.27 (n/a)</td><td>667.51 (n/a)</td><td>667.72 (n/a)</td><td>666.16 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.70 (+0.01%)</td><td>0.70 (+0.17%)</td><td>0.70 (+0.10%)</td><td>0.70 (+0.35%)</td><td>0.00 <b>(-40.86%)</b></td><td>107848.80 (-0.35%)</td><td>107717.28 (-0.17%)</td><td>107795.40 (-0.10%)</td><td>107547.70 (-0.01%)</td><td>140.11 <b>(-41.07%)</b></td><td>638.97 (+0.01%)</td><td>637.96 (+0.17%)</td><td>637.50 (+0.10%)</td><td>637.18 (+0.35%)</td><td>0.83 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108231.40 (n/a)</td><td>107895.50 (n/a)</td><td>107904.60 (n/a)</td><td>107559.90 (n/a)</td><td>237.77 (n/a)</td><td>638.90 (n/a)</td><td>636.91 (n/a)</td><td>636.85 (n/a)</td><td>634.93 (n/a)</td><td>1.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>4.19 (+1.96%)</td><td>3.52 (+1.47%)</td><td>3.46 (+4.36%)</td><td>3.05 (+4.23%)</td><td>0.43 <b>(-26.46%)</b></td><td>2639.70 (-4.06%)</td><td>2315.08 (-2.53%)</td><td>2329.60 (-4.18%)</td><td>1923.30 (-1.92%)</td><td>267.46 <b>(-31.34%)</b></td><td>1099.14 (+1.96%)</td><td>923.46 (+1.47%)</td><td>907.42 (+4.36%)</td><td>800.81 (+4.23%)</td><td>112.56 <b>(-26.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.11 (n/a)</td><td>3.47 (n/a)</td><td>3.32 (n/a)</td><td>2.93 (n/a)</td><td>0.58 (n/a)</td><td>2751.30 (n/a)</td><td>2375.06 (n/a)</td><td>2431.20 (n/a)</td><td>1960.90 (n/a)</td><td>389.54 (n/a)</td><td>1078.02 (n/a)</td><td>910.09 (n/a)</td><td>869.49 (n/a)</td><td>768.34 (n/a)</td><td>153.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.42 (-15.18%)</td><td>0.34 (-2.04%)</td><td>0.33 (+2.23%)</td><td>0.32 (+10.65%)</td><td>0.04 <b>(-47.43%)</b></td><td>3943.00 (-9.63%)</td><td>3674.82 (-0.45%)</td><td>3809.80 (-2.18%)</td><td>2959.20 (+17.90%)</td><td>403.83 <b>(-42.14%)</b></td><td>22.68 (-15.18%)</td><td>18.47 (-2.04%)</td><td>17.61 (+2.23%)</td><td>17.02 (+10.65%)</td><td>2.37 <b>(-47.43%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>4363.10 (n/a)</td><td>3691.44 (n/a)</td><td>3894.90 (n/a)</td><td>2510.00 (n/a)</td><td>697.98 (n/a)</td><td>26.74 (n/a)</td><td>18.85 (n/a)</td><td>17.23 (n/a)</td><td>15.38 (n/a)</td><td>4.50 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.02 (-4.08%)</td><td>4.54 (-4.97%)</td><td>4.93 (+3.98%)</td><td>3.15 (-8.70%)</td><td>1.14 (+13.58%)</td><td>2115.00 (+9.52%)</td><td>1547.06 (+7.11%)</td><td>1349.80 (-3.83%)</td><td>1105.40 (+4.25%)</td><td>408.67 <b>(+31.13%)</b></td><td>1859.20 (-4.08%)</td><td>1401.73 (-4.97%)</td><td>1522.60 (+3.98%)</td><td>971.71 (-8.70%)</td><td>352.32 (+13.58%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.27 (n/a)</td><td>4.77 (n/a)</td><td>4.74 (n/a)</td><td>3.44 (n/a)</td><td>1.00 (n/a)</td><td>1931.10 (n/a)</td><td>1444.34 (n/a)</td><td>1403.50 (n/a)</td><td>1060.30 (n/a)</td><td>311.65 (n/a)</td><td>1938.34 (n/a)</td><td>1475.08 (n/a)</td><td>1464.34 (n/a)</td><td>1064.24 (n/a)</td><td>310.20 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.17 (n/a)</td><td>12.57 (n/a)</td><td>12.62 (n/a)</td><td>11.63 (n/a)</td><td>0.65 (n/a)</td><td>13.16 (n/a)</td><td>12.56 (n/a)</td><td>12.61 (n/a)</td><td>11.62 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>25.14 (-0.11%)</td><td>23.00 (-7.58%)</td><td>24.62 (-1.26%)</td><td>16.14 <b>(-34.31%)</b></td><td>3.85 <b>(+1560.09%)</b></td><td>25.12 (-0.11%)</td><td>22.99 (-7.58%)</td><td>24.61 (-1.26%)</td><td>16.13 <b>(-34.31%)</b></td><td>3.84 <b>(+1560.09%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>25.16 (n/a)</td><td>24.88 (n/a)</td><td>24.94 (n/a)</td><td>24.58 (n/a)</td><td>0.23 (n/a)</td><td>25.15 (n/a)</td><td>24.87 (n/a)</td><td>24.92 (n/a)</td><td>24.56 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>41.52 (-3.52%)</td><td>39.93 (+5.57%)</td><td>39.78 (-2.54%)</td><td>38.06 <b>(+67.53%)</b></td><td>1.37 <b>(-83.88%)</b></td><td>41.49 (-3.52%)</td><td>39.90 (+5.57%)</td><td>39.75 (-2.54%)</td><td>38.04 <b>(+67.53%)</b></td><td>1.37 <b>(-83.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>43.03 (n/a)</td><td>37.82 (n/a)</td><td>40.81 (n/a)</td><td>22.72 (n/a)</td><td>8.53 (n/a)</td><td>43.00 (n/a)</td><td>37.80 (n/a)</td><td>40.79 (n/a)</td><td>22.71 (n/a)</td><td>8.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>44.71 (+0.42%)</td><td>42.99 (-0.07%)</td><td>44.39 (+4.26%)</td><td>38.61 (-8.19%)</td><td>2.60 <b>(+157.84%)</b></td><td>44.69 (+0.42%)</td><td>42.96 (-0.07%)</td><td>44.36 (+4.26%)</td><td>38.59 (-8.19%)</td><td>2.60 <b>(+157.84%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>44.53 (n/a)</td><td>43.01 (n/a)</td><td>42.57 (n/a)</td><td>42.05 (n/a)</td><td>1.01 (n/a)</td><td>44.50 (n/a)</td><td>42.99 (n/a)</td><td>42.55 (n/a)</td><td>42.03 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.24 (n/a)</td><td>12.61 (n/a)</td><td>13.10 (n/a)</td><td>10.75 (n/a)</td><td>1.06 (n/a)</td><td>13.23 (n/a)</td><td>12.60 (n/a)</td><td>13.09 (n/a)</td><td>10.74 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>24.06 (-1.42%)</td><td>23.42 (-1.73%)</td><td>23.88 (-0.71%)</td><td>22.23 (-3.72%)</td><td>0.83 <b>(+56.21%)</b></td><td>24.05 (-1.42%)</td><td>23.40 (-1.73%)</td><td>23.86 (-0.71%)</td><td>22.22 (-3.72%)</td><td>0.83 <b>(+56.21%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>24.41 (n/a)</td><td>23.83 (n/a)</td><td>24.05 (n/a)</td><td>23.09 (n/a)</td><td>0.53 (n/a)</td><td>24.40 (n/a)</td><td>23.82 (n/a)</td><td>24.03 (n/a)</td><td>23.08 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>42.68 (-3.68%)</td><td>40.59 (-0.59%)</td><td>40.11 (-0.21%)</td><td>39.23 (+2.44%)</td><td>1.45 <b>(-35.51%)</b></td><td>42.66 (-3.68%)</td><td>40.57 (-0.59%)</td><td>40.09 (-0.21%)</td><td>39.21 (+2.44%)</td><td>1.45 <b>(-35.51%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>44.31 (n/a)</td><td>40.84 (n/a)</td><td>40.20 (n/a)</td><td>38.30 (n/a)</td><td>2.26 (n/a)</td><td>44.29 (n/a)</td><td>40.81 (n/a)</td><td>40.17 (n/a)</td><td>38.28 (n/a)</td><td>2.25 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>44.66 (-1.37%)</td><td>41.85 (-1.73%)</td><td>41.92 (-3.44%)</td><td>38.93 (-0.25%)</td><td>2.14 (-18.44%)</td><td>44.64 (-1.37%)</td><td>41.82 (-1.73%)</td><td>41.89 (-3.44%)</td><td>38.91 (-0.25%)</td><td>2.14 (-18.44%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>45.28 (n/a)</td><td>42.59 (n/a)</td><td>43.41 (n/a)</td><td>39.03 (n/a)</td><td>2.62 (n/a)</td><td>45.26 (n/a)</td><td>42.56 (n/a)</td><td>43.39 (n/a)</td><td>39.01 (n/a)</td><td>2.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.57 (-0.07%)</td><td>8.96 (+1.12%)</td><td>8.91 (+1.59%)</td><td>8.67 (+7.68%)</td><td>0.36 <b>(-35.35%)</b></td><td>9.55 (-0.07%)</td><td>8.94 (+1.12%)</td><td>8.89 (+1.59%)</td><td>8.66 (+7.68%)</td><td>0.36 <b>(-35.35%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.57 (n/a)</td><td>8.86 (n/a)</td><td>8.77 (n/a)</td><td>8.05 (n/a)</td><td>0.56 (n/a)</td><td>9.55 (n/a)</td><td>8.84 (n/a)</td><td>8.75 (n/a)</td><td>8.04 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.90 (-8.55%)</td><td>0.81 (-4.37%)</td><td>0.81 (+1.45%)</td><td>0.73 (+4.15%)</td><td>0.06 <b>(-50.60%)</b></td><td>0.88 (-8.55%)</td><td>0.80 (-4.37%)</td><td>0.79 (+1.45%)</td><td>0.72 (+4.15%)</td><td>0.06 <b>(-50.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.98 (n/a)</td><td>0.85 (n/a)</td><td>0.79 (n/a)</td><td>0.70 (n/a)</td><td>0.12 (n/a)</td><td>0.97 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.33 (+3.42%)</td><td>1.16 (-0.59%)</td><td>1.22 (+1.90%)</td><td>0.93 (-8.58%)</td><td>0.15 <b>(+42.47%)</b></td><td>1.31 (+3.42%)</td><td>1.15 (-0.59%)</td><td>1.20 (+1.90%)</td><td>0.92 (-8.58%)</td><td>0.15 <b>(+42.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.28 (n/a)</td><td>1.17 (n/a)</td><td>1.19 (n/a)</td><td>1.02 (n/a)</td><td>0.10 (n/a)</td><td>1.27 (n/a)</td><td>1.16 (n/a)</td><td>1.18 (n/a)</td><td>1.01 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>16.27 (-7.86%)</td><td>15.14 (-3.29%)</td><td>14.83 (-6.86%)</td><td>13.76 (+6.62%)</td><td>1.07 <b>(-38.16%)</b></td><td>16.09 (-7.86%)</td><td>14.96 (-3.29%)</td><td>14.66 (-6.86%)</td><td>13.61 (+6.62%)</td><td>1.06 <b>(-38.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>17.66 (n/a)</td><td>15.65 (n/a)</td><td>15.92 (n/a)</td><td>12.91 (n/a)</td><td>1.74 (n/a)</td><td>17.46 (n/a)</td><td>15.47 (n/a)</td><td>15.74 (n/a)</td><td>12.76 (n/a)</td><td>1.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>12.32 (-1.25%)</td><td>12.03 (-0.59%)</td><td>12.15 (+0.40%)</td><td>11.72 (-0.10%)</td><td>0.26 (-19.62%)</td><td>12.10 (-1.25%)</td><td>11.82 (-0.59%)</td><td>11.94 (+0.40%)</td><td>11.52 (-0.10%)</td><td>0.25 (-19.62%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>12.48 (n/a)</td><td>12.10 (n/a)</td><td>12.11 (n/a)</td><td>11.73 (n/a)</td><td>0.32 (n/a)</td><td>12.26 (n/a)</td><td>11.89 (n/a)</td><td>11.89 (n/a)</td><td>11.53 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.01 (+6.18%)</td><td>7.45 (+12.64%)</td><td>7.31 (+4.63%)</td><td>6.96 <b>(+24.85%)</b></td><td>0.41 <b>(-48.92%)</b></td><td>7.87 (+6.18%)</td><td>7.32 (+12.64%)</td><td>7.18 (+4.63%)</td><td>6.84 <b>(+24.85%)</b></td><td>0.41 <b>(-48.92%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.55 (n/a)</td><td>6.61 (n/a)</td><td>6.98 (n/a)</td><td>5.57 (n/a)</td><td>0.81 (n/a)</td><td>7.42 (n/a)</td><td>6.50 (n/a)</td><td>6.86 (n/a)</td><td>5.48 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.98 (+5.94%)</td><td>6.04 (+4.59%)</td><td>5.84 (+0.28%)</td><td>5.34 (+4.42%)</td><td>0.76 <b>(+30.34%)</b></td><td>6.87 (+5.94%)</td><td>5.94 (+4.59%)</td><td>5.75 (+0.28%)</td><td>5.26 (+4.42%)</td><td>0.75 <b>(+30.34%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.59 (n/a)</td><td>5.77 (n/a)</td><td>5.82 (n/a)</td><td>5.12 (n/a)</td><td>0.58 (n/a)</td><td>6.49 (n/a)</td><td>5.68 (n/a)</td><td>5.73 (n/a)</td><td>5.03 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.56 (n/a)</td><td>12.35 (n/a)</td><td>13.11 (n/a)</td><td>10.87 (n/a)</td><td>1.30 (n/a)</td><td>13.56 (n/a)</td><td>12.34 (n/a)</td><td>13.11 (n/a)</td><td>10.86 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.28 (n/a)</td><td>12.17 (n/a)</td><td>12.19 (n/a)</td><td>11.09 (n/a)</td><td>1.07 (n/a)</td><td>13.27 (n/a)</td><td>12.17 (n/a)</td><td>12.18 (n/a)</td><td>11.09 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>163.44 (n/a)</td><td>172.90 (n/a)</td><td>111.60 (n/a)</td><td>35.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.10 (n/a)</td><td>182.36 (n/a)</td><td>188.50 (n/a)</td><td>139.30 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.50 (n/a)</td><td>153.72 (n/a)</td><td>156.80 (n/a)</td><td>122.30 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>267.20 (n/a)</td><td>182.68 (n/a)</td><td>189.50 (n/a)</td><td>129.30 (n/a)</td><td>55.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.40 (n/a)</td><td>158.36 (n/a)</td><td>162.40 (n/a)</td><td>118.30 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>298.00 (n/a)</td><td>205.42 (n/a)</td><td>176.50 (n/a)</td><td>169.50 (n/a)</td><td>54.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.80 (n/a)</td><td>196.48 (n/a)</td><td>190.80 (n/a)</td><td>149.50 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.70 (n/a)</td><td>198.12 (n/a)</td><td>195.90 (n/a)</td><td>144.60 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>185.66 (n/a)</td><td>177.10 (n/a)</td><td>155.20 (n/a)</td><td>37.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.20 (n/a)</td><td>157.46 (n/a)</td><td>152.50 (n/a)</td><td>136.00 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>159.20 (n/a)</td><td>171.40 (n/a)</td><td>108.90 (n/a)</td><td>36.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>163.38 (n/a)</td><td>156.20 (n/a)</td><td>141.50 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>185.84 (n/a)</td><td>182.90 (n/a)</td><td>128.90 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>176.68 (n/a)</td><td>179.20 (n/a)</td><td>146.90 (n/a)</td><td>24.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>183.06 (n/a)</td><td>176.70 (n/a)</td><td>155.90 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>348.40 (n/a)</td><td>242.24 (n/a)</td><td>221.70 (n/a)</td><td>190.30 (n/a)</td><td>61.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>186.96 (n/a)</td><td>186.30 (n/a)</td><td>172.00 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>251.50 (n/a)</td><td>201.52 (n/a)</td><td>196.00 (n/a)</td><td>168.50 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>249.20 (n/a)</td><td>214.98 (n/a)</td><td>216.20 (n/a)</td><td>184.70 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>204.88 (n/a)</td><td>195.40 (n/a)</td><td>159.50 (n/a)</td><td>35.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>189.56 (n/a)</td><td>171.30 (n/a)</td><td>160.90 (n/a)</td><td>32.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.40 (n/a)</td><td>210.24 (n/a)</td><td>216.70 (n/a)</td><td>180.40 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>194.20 (n/a)</td><td>188.90 (n/a)</td><td>152.90 (n/a)</td><td>32.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>265.80 (n/a)</td><td>243.76 (n/a)</td><td>253.90 (n/a)</td><td>212.40 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-3.27%)</td><td>0.17 (-9.70%)</td><td>0.17 (-12.84%)</td><td>0.13 (-14.94%)</td><td>0.04 (+18.23%)</td><td>249.60 (+17.51%)</td><td>195.08 (+12.48%)</td><td>194.60 (+14.74%)</td><td>139.80 (+3.40%)</td><td>41.96 <b>(+42.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.40 (n/a)</td><td>173.44 (n/a)</td><td>169.60 (n/a)</td><td>135.20 (n/a)</td><td>29.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>247.00 (n/a)</td><td>194.80 (n/a)</td><td>188.40 (n/a)</td><td>124.70 (n/a)</td><td>47.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.70 (n/a)</td><td>169.36 (n/a)</td><td>181.20 (n/a)</td><td>123.50 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>185.50 (n/a)</td><td>172.10 (n/a)</td><td>166.90 (n/a)</td><td>27.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>224.60 (n/a)</td><td>185.68 (n/a)</td><td>182.60 (n/a)</td><td>161.40 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>227.40 (n/a)</td><td>200.14 (n/a)</td><td>194.50 (n/a)</td><td>177.30 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.40 (n/a)</td><td>178.04 (n/a)</td><td>172.30 (n/a)</td><td>135.80 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>298.90 (n/a)</td><td>225.02 (n/a)</td><td>210.90 (n/a)</td><td>189.50 (n/a)</td><td>44.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 <b>(+43.10%)</b></td><td>0.03 <b>(+25.04%)</b></td><td>0.03 <b>(+28.11%)</b></td><td>0.02 (-15.43%)</td><td>0.01 <b>(+202.50%)</b></td><td>243.30 (+18.22%)</td><td>153.42 (-14.82%)</td><td>143.90 <b>(-21.92%)</b></td><td>110.30 <b>(-30.15%)</b></td><td>52.22 <b>(+166.75%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.80 (n/a)</td><td>180.12 (n/a)</td><td>184.30 (n/a)</td><td>157.90 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-7.57%)</td><td>0.03 (+5.47%)</td><td>0.03 (+10.17%)</td><td>0.02 (+19.53%)</td><td>0.00 <b>(-54.76%)</b></td><td>170.30 (-16.36%)</td><td>157.52 (-6.79%)</td><td>161.00 (-9.24%)</td><td>144.90 (+8.22%)</td><td>11.02 <b>(-59.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>169.00 (n/a)</td><td>177.40 (n/a)</td><td>133.90 (n/a)</td><td>26.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+8.08%)</td><td>0.03 (+16.30%)</td><td>0.03 (+11.16%)</td><td>0.03 <b>(+50.67%)</b></td><td>0.00 <b>(-47.94%)</b></td><td>152.30 <b>(-33.64%)</b></td><td>142.02 (-16.22%)</td><td>143.70 (-10.02%)</td><td>124.30 (-7.51%)</td><td>10.95 <b>(-69.43%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.50 (n/a)</td><td>169.52 (n/a)</td><td>159.70 (n/a)</td><td>134.40 (n/a)</td><td>35.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 <b>(+41.27%)</b></td><td>0.03 <b>(+21.25%)</b></td><td>0.03 <b>(+30.56%)</b></td><td>0.02 (-6.72%)</td><td>0.01 <b>(+189.98%)</b></td><td>246.30 (+7.18%)</td><td>170.40 (-12.16%)</td><td>148.30 <b>(-23.44%)</b></td><td>117.30 <b>(-29.17%)</b></td><td>53.98 <b>(+122.19%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.80 (n/a)</td><td>193.98 (n/a)</td><td>193.70 (n/a)</td><td>165.60 (n/a)</td><td>24.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-16.79%)</td><td>0.02 (-8.12%)</td><td>0.02 (+5.90%)</td><td>0.02 (-4.79%)</td><td>0.00 <b>(-42.79%)</b></td><td>205.20 (+5.02%)</td><td>176.02 (+6.70%)</td><td>171.60 (-5.56%)</td><td>153.50 <b>(+20.11%)</b></td><td>23.61 <b>(-27.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>164.96 (n/a)</td><td>181.70 (n/a)</td><td>127.80 (n/a)</td><td>32.53 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-4.28%)</td><td>0.02 (-4.57%)</td><td>0.02 (-18.26%)</td><td>0.02 (+9.29%)</td><td>0.00 <b>(-34.68%)</b></td><td>188.10 (-8.51%)</td><td>168.58 (+2.78%)</td><td>178.30 <b>(+22.37%)</b></td><td>137.50 (+4.48%)</td><td>20.50 <b>(-39.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>164.02 (n/a)</td><td>145.70 (n/a)</td><td>131.60 (n/a)</td><td>33.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-2.99%)</td><td>0.02 (+2.94%)</td><td>0.02 (+15.33%)</td><td>0.02 (-11.64%)</td><td>0.00 (-5.83%)</td><td>240.80 (+13.16%)</td><td>174.70 (-2.67%)</td><td>166.20 (-13.30%)</td><td>136.40 (+3.10%)</td><td>39.33 (+13.39%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>179.50 (n/a)</td><td>191.70 (n/a)</td><td>132.30 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (+12.16%)</td><td>0.02 (+8.68%)</td><td>0.02 (+5.33%)</td><td>0.02 <b>(+42.24%)</b></td><td>0.00 <b>(-27.67%)</b></td><td>236.90 <b>(-29.70%)</b></td><td>213.32 (-10.38%)</td><td>217.00 (-5.03%)</td><td>173.40 (-10.85%)</td><td>25.96 <b>(-55.23%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>337.00 (n/a)</td><td>238.02 (n/a)</td><td>228.50 (n/a)</td><td>194.50 (n/a)</td><td>57.99 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-5.20%)</td><td>0.05 (+3.35%)</td><td>0.06 (+17.25%)</td><td>0.05 (+15.31%)</td><td>0.01 <b>(-40.54%)</b></td><td>173.50 (-13.29%)</td><td>151.52 (-5.71%)</td><td>145.70 (-14.75%)</td><td>126.30 (+5.51%)</td><td>19.23 <b>(-43.99%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>160.70 (n/a)</td><td>170.90 (n/a)</td><td>119.70 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(+28.20%)</b></td><td>0.06 <b>(+26.74%)</b></td><td>0.06 (+18.93%)</td><td>0.06 <b>(+43.01%)</b></td><td>0.00 (-10.60%)</td><td>147.00 <b>(-30.07%)</b></td><td>136.12 <b>(-21.55%)</b></td><td>139.20 (-15.89%)</td><td>123.50 <b>(-21.98%)</b></td><td>9.88 <b>(-52.58%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>173.52 (n/a)</td><td>165.50 (n/a)</td><td>158.30 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(+37.20%)</b></td><td>0.06 <b>(+30.83%)</b></td><td>0.06 <b>(+29.65%)</b></td><td>0.05 (+19.51%)</td><td>0.01 <b>(+164.47%)</b></td><td>164.30 (-16.30%)</td><td>136.16 <b>(-22.45%)</b></td><td>134.50 <b>(-22.88%)</b></td><td>115.40 <b>(-27.15%)</b></td><td>21.25 <b>(+57.32%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>196.30 (n/a)</td><td>175.58 (n/a)</td><td>174.40 (n/a)</td><td>158.40 (n/a)</td><td>13.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-10.12%)</td><td>0.05 (+5.51%)</td><td>0.05 (+15.04%)</td><td>0.04 (+19.33%)</td><td>0.01 <b>(-52.52%)</b></td><td>191.60 (-16.19%)</td><td>160.04 (-8.69%)</td><td>150.10 (-13.09%)</td><td>146.30 (+11.25%)</td><td>19.21 <b>(-54.93%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.60 (n/a)</td><td>175.28 (n/a)</td><td>172.70 (n/a)</td><td>131.50 (n/a)</td><td>42.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (+1.04%)</td><td>0.05 (+16.58%)</td><td>0.05 <b>(+27.85%)</b></td><td>0.03 <b>(+35.52%)</b></td><td>0.02 (-1.14%)</td><td>236.10 <b>(-26.20%)</b></td><td>167.48 (-16.50%)</td><td>155.00 <b>(-21.80%)</b></td><td>115.40 (-1.03%)</td><td>53.33 <b>(-29.12%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>319.90 (n/a)</td><td>200.58 (n/a)</td><td>198.20 (n/a)</td><td>116.60 (n/a)</td><td>75.24 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (-3.53%)</td><td>0.05 (-2.28%)</td><td>0.05 (+5.69%)</td><td>0.03 <b>(-22.99%)</b></td><td>0.01 <b>(+53.13%)</b></td><td>239.80 <b>(+29.83%)</b></td><td>180.48 (+4.17%)</td><td>169.40 (-5.42%)</td><td>150.00 (+3.66%)</td><td>34.98 <b>(+116.23%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>173.26 (n/a)</td><td>179.10 (n/a)</td><td>144.70 (n/a)</td><td>16.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-1.23%)</td><td>0.05 (+2.65%)</td><td>0.05 (+17.26%)</td><td>0.04 (-10.23%)</td><td>0.01 (+4.05%)</td><td>233.00 (+11.38%)</td><td>173.62 (-1.92%)</td><td>157.40 (-14.73%)</td><td>131.90 (+1.23%)</td><td>39.08 (+18.52%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>177.02 (n/a)</td><td>184.60 (n/a)</td><td>130.30 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+1.39%)</td><td>0.05 (+18.70%)</td><td>0.05 <b>(+26.97%)</b></td><td>0.04 <b>(+33.89%)</b></td><td>0.01 <b>(-35.55%)</b></td><td>205.40 <b>(-25.31%)</b></td><td>170.38 (-19.16%)</td><td>172.80 <b>(-21.24%)</b></td><td>134.20 (-1.32%)</td><td>25.73 <b>(-52.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>275.00 (n/a)</td><td>210.76 (n/a)</td><td>219.40 (n/a)</td><td>136.00 (n/a)</td><td>54.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+8.34%)</td><td>0.04 (+11.21%)</td><td>0.04 (+17.44%)</td><td>0.03 (+4.36%)</td><td>0.01 (+2.54%)</td><td>272.00 (-4.19%)</td><td>194.30 (-10.26%)</td><td>184.40 (-14.83%)</td><td>146.70 (-7.74%)</td><td>47.68 (-5.95%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.90 (n/a)</td><td>216.52 (n/a)</td><td>216.50 (n/a)</td><td>159.00 (n/a)</td><td>50.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (-2.12%)</td><td>0.04 (+9.44%)</td><td>0.04 (+11.59%)</td><td>0.04 (+13.78%)</td><td>0.00 <b>(-32.80%)</b></td><td>213.50 (-12.10%)</td><td>193.76 (-9.36%)</td><td>194.60 (-10.41%)</td><td>177.20 (+2.13%)</td><td>16.00 <b>(-39.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.90 (n/a)</td><td>213.76 (n/a)</td><td>217.20 (n/a)</td><td>173.50 (n/a)</td><td>26.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (+10.02%)</td><td>0.11 (+14.59%)</td><td>0.11 <b>(+22.80%)</b></td><td>0.09 (+12.55%)</td><td>0.01 (+15.23%)</td><td>185.50 (-11.16%)</td><td>154.20 (-12.65%)</td><td>145.70 (-18.56%)</td><td>136.60 (-9.12%)</td><td>20.48 (-7.30%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>176.54 (n/a)</td><td>178.90 (n/a)</td><td>150.30 (n/a)</td><td>22.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (+2.94%)</td><td>0.11 (+4.42%)</td><td>0.10 (-2.95%)</td><td>0.10 (+12.59%)</td><td>0.02 (-16.79%)</td><td>165.40 (-11.17%)</td><td>145.72 (-5.54%)</td><td>156.30 (+3.03%)</td><td>116.10 (-2.85%)</td><td>22.15 <b>(-29.31%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.20 (n/a)</td><td>154.26 (n/a)</td><td>151.70 (n/a)</td><td>119.50 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (-4.21%)</td><td>0.11 (+3.49%)</td><td>0.11 (+2.64%)</td><td>0.10 <b>(+29.64%)</b></td><td>0.01 <b>(-64.47%)</b></td><td>160.10 <b>(-22.84%)</b></td><td>151.28 (-6.01%)</td><td>153.70 (-2.60%)</td><td>135.90 (+4.38%)</td><td>9.45 <b>(-70.85%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.50 (n/a)</td><td>160.96 (n/a)</td><td>157.80 (n/a)</td><td>130.20 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 <b>(+61.26%)</b></td><td>0.12 <b>(+50.08%)</b></td><td>0.11 <b>(+38.93%)</b></td><td>0.11 <b>(+93.74%)</b></td><td>0.02 (+13.78%)</td><td>156.00 <b>(-48.40%)</b></td><td>137.50 <b>(-34.96%)</b></td><td>143.60 <b>(-28.06%)</b></td><td>107.60 <b>(-37.98%)</b></td><td>18.17 <b>(-65.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>302.30 (n/a)</td><td>211.42 (n/a)</td><td>199.60 (n/a)</td><td>173.50 (n/a)</td><td>52.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (+16.49%)</td><td>0.11 (+18.70%)</td><td>0.11 <b>(+20.89%)</b></td><td>0.10 <b>(+20.14%)</b></td><td>0.01 (+2.54%)</td><td>165.30 (-16.77%)</td><td>153.36 (-15.87%)</td><td>149.00 (-17.31%)</td><td>143.30 (-14.19%)</td><td>10.98 <b>(-26.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>182.28 (n/a)</td><td>180.20 (n/a)</td><td>167.00 (n/a)</td><td>14.93 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 <b>(+27.57%)</b></td><td>0.10 (+17.83%)</td><td>0.10 (+16.00%)</td><td>0.10 (+15.86%)</td><td>0.01 <b>(+84.20%)</b></td><td>171.40 (-13.70%)</td><td>159.82 (-14.63%)</td><td>166.10 (-13.76%)</td><td>130.10 <b>(-21.58%)</b></td><td>16.86 <b>(+21.87%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>187.20 (n/a)</td><td>192.60 (n/a)</td><td>165.90 (n/a)</td><td>13.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (+1.84%)</td><td>0.11 <b>(+22.51%)</b></td><td>0.11 <b>(+36.47%)</b></td><td>0.09 <b>(+26.25%)</b></td><td>0.01 <b>(-35.50%)</b></td><td>179.40 <b>(-20.79%)</b></td><td>157.10 (-19.79%)</td><td>149.00 <b>(-26.71%)</b></td><td>139.80 (-1.83%)</td><td>16.91 <b>(-47.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.50 (n/a)</td><td>195.86 (n/a)</td><td>203.30 (n/a)</td><td>142.40 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (+9.59%)</td><td>0.09 (+9.26%)</td><td>0.09 (+11.18%)</td><td>0.07 (+5.52%)</td><td>0.01 (+5.73%)</td><td>222.90 (-5.23%)</td><td>189.00 (-8.50%)</td><td>184.50 (-10.04%)</td><td>164.00 (-8.79%)</td><td>21.70 (-7.42%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.20 (n/a)</td><td>206.56 (n/a)</td><td>205.10 (n/a)</td><td>179.80 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (+11.95%)</td><td>0.21 (+1.82%)</td><td>0.21 (+6.54%)</td><td>0.14 (-16.21%)</td><td>0.05 <b>(+82.60%)</b></td><td>227.70 (+19.40%)</td><td>165.32 (+1.55%)</td><td>153.40 (-6.18%)</td><td>123.80 (-10.68%)</td><td>41.47 <b>(+97.34%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>190.70 (n/a)</td><td>162.80 (n/a)</td><td>163.50 (n/a)</td><td>138.60 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (+13.82%)</td><td>0.20 (+6.52%)</td><td>0.20 (+10.60%)</td><td>0.16 (+0.10%)</td><td>0.04 <b>(+22.05%)</b></td><td>210.70 (-0.09%)</td><td>164.82 (-5.49%)</td><td>160.40 (-9.58%)</td><td>129.80 (-12.12%)</td><td>30.15 (+11.59%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.90 (n/a)</td><td>174.40 (n/a)</td><td>177.40 (n/a)</td><td>147.70 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 <b>(-37.85%)</b></td><td>0.19 (-14.94%)</td><td>0.20 (-10.89%)</td><td>0.14 (+13.15%)</td><td>0.03 <b>(-63.34%)</b></td><td>238.10 (-11.62%)</td><td>176.42 (+7.18%)</td><td>162.00 (+12.27%)</td><td>153.10 <b>(+60.99%)</b></td><td>34.84 <b>(-47.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>269.40 (n/a)</td><td>164.60 (n/a)</td><td>144.30 (n/a)</td><td>95.10 (n/a)</td><td>66.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 <b>(+29.66%)</b></td><td>0.24 <b>(+42.69%)</b></td><td>0.24 <b>(+31.10%)</b></td><td>0.18 <b>(+91.93%)</b></td><td>0.04 <b>(-27.22%)</b></td><td>184.90 <b>(-47.90%)</b></td><td>138.90 <b>(-35.62%)</b></td><td>134.30 <b>(-23.74%)</b></td><td>114.50 <b>(-22.90%)</b></td><td>27.28 <b>(-68.96%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>354.90 (n/a)</td><td>215.76 (n/a)</td><td>176.10 (n/a)</td><td>148.50 (n/a)</td><td>87.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 <b>(-26.88%)</b></td><td>0.19 (-0.31%)</td><td>0.19 (+1.90%)</td><td>0.17 <b>(+31.65%)</b></td><td>0.01 <b>(-74.89%)</b></td><td>195.40 <b>(-24.06%)</b></td><td>173.02 (-5.81%)</td><td>173.00 (-1.87%)</td><td>161.00 <b>(+36.67%)</b></td><td>13.73 <b>(-73.67%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>257.30 (n/a)</td><td>183.70 (n/a)</td><td>176.30 (n/a)</td><td>117.80 (n/a)</td><td>52.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (+1.79%)</td><td>0.18 (+2.60%)</td><td>0.19 (+15.64%)</td><td>0.15 (-5.06%)</td><td>0.02 (+19.78%)</td><td>219.00 (+5.29%)</td><td>184.72 (-2.12%)</td><td>171.10 (-13.54%)</td><td>163.70 (-1.74%)</td><td>24.40 <b>(+24.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>188.72 (n/a)</td><td>197.90 (n/a)</td><td>166.60 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (+0.36%)</td><td>0.15 (-0.97%)</td><td>0.16 (+6.90%)</td><td>0.12 (-7.01%)</td><td>0.02 (+18.77%)</td><td>272.10 (+7.51%)</td><td>222.46 (+1.77%)</td><td>198.90 (-6.44%)</td><td>189.00 (-0.32%)</td><td>38.72 <b>(+27.74%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>253.10 (n/a)</td><td>218.60 (n/a)</td><td>212.60 (n/a)</td><td>189.60 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+5.41%)</td><td>0.03 (+5.18%)</td><td>0.03 (+18.66%)</td><td>0.02 (-3.62%)</td><td>0.00 (+10.56%)</td><td>211.70 (+3.72%)</td><td>157.92 (-4.34%)</td><td>146.00 (-15.70%)</td><td>127.50 (-5.13%)</td><td>32.68 (+14.34%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>165.08 (n/a)</td><td>173.20 (n/a)</td><td>134.40 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (-9.81%)</td><td>0.03 (+10.59%)</td><td>0.03 (+18.10%)</td><td>0.02 <b>(+46.12%)</b></td><td>0.01 <b>(-42.20%)</b></td><td>170.40 <b>(-31.57%)</b></td><td>144.78 (-15.13%)</td><td>149.00 (-15.34%)</td><td>116.70 (+10.93%)</td><td>24.53 <b>(-55.63%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.00 (n/a)</td><td>170.60 (n/a)</td><td>176.00 (n/a)</td><td>105.20 (n/a)</td><td>55.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 <b>(+44.42%)</b></td><td>0.02 <b>(+23.89%)</b></td><td>0.02 (+10.03%)</td><td>0.02 (+9.05%)</td><td>0.00 <b>(+340.00%)</b></td><td>219.00 (-8.29%)</td><td>179.62 (-17.07%)</td><td>192.30 (-9.12%)</td><td>143.60 <b>(-30.76%)</b></td><td>33.78 <b>(+165.91%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.80 (n/a)</td><td>216.58 (n/a)</td><td>211.60 (n/a)</td><td>207.40 (n/a)</td><td>12.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 <b>(+24.99%)</b></td><td>0.02 (+14.73%)</td><td>0.02 (+12.05%)</td><td>0.02 (+11.57%)</td><td>0.00 <b>(+34.84%)</b></td><td>256.50 (-10.38%)</td><td>186.58 (-12.18%)</td><td>174.80 (-10.77%)</td><td>149.30 (-19.99%)</td><td>40.85 (-1.60%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>286.20 (n/a)</td><td>212.46 (n/a)</td><td>195.90 (n/a)</td><td>186.60 (n/a)</td><td>41.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-10.94%)</td><td>0.03 (-12.14%)</td><td>0.02 (-19.77%)</td><td>0.02 (-0.46%)</td><td>0.00 <b>(-21.25%)</b></td><td>192.40 (+0.47%)</td><td>158.92 (+12.47%)</td><td>165.30 <b>(+24.66%)</b></td><td>119.40 (+12.22%)</td><td>26.95 (-14.86%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>141.30 (n/a)</td><td>132.60 (n/a)</td><td>106.40 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-19.95%)</td><td>0.03 (+1.60%)</td><td>0.03 (+5.67%)</td><td>0.02 (+11.50%)</td><td>0.00 <b>(-59.38%)</b></td><td>182.00 (-10.30%)</td><td>158.30 (-5.56%)</td><td>159.60 (-5.39%)</td><td>133.80 <b>(+24.93%)</b></td><td>17.46 <b>(-53.51%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>167.62 (n/a)</td><td>168.70 (n/a)</td><td>107.10 (n/a)</td><td>37.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-12.09%)</td><td>0.02 (-16.93%)</td><td>0.02 <b>(-22.19%)</b></td><td>0.02 (-9.02%)</td><td>0.00 <b>(-21.19%)</b></td><td>199.00 (+9.88%)</td><td>176.52 <b>(+20.02%)</b></td><td>179.40 <b>(+28.51%)</b></td><td>151.00 (+13.79%)</td><td>18.61 (-4.40%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>147.08 (n/a)</td><td>139.60 (n/a)</td><td>132.70 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-12.44%)</td><td>0.02 (-2.43%)</td><td>0.02 (-2.81%)</td><td>0.02 (+2.06%)</td><td>0.00 <b>(-32.74%)</b></td><td>184.60 (-2.02%)</td><td>169.54 (+1.63%)</td><td>178.40 (+2.88%)</td><td>145.80 (+14.17%)</td><td>18.14 <b>(-21.08%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.40 (n/a)</td><td>166.82 (n/a)</td><td>173.40 (n/a)</td><td>127.70 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-15.02%)</td><td>0.02 (-2.76%)</td><td>0.02 (-9.48%)</td><td>0.02 (+17.46%)</td><td>0.00 <b>(-47.44%)</b></td><td>198.20 (-14.90%)</td><td>173.24 (-0.49%)</td><td>173.50 (+10.44%)</td><td>148.10 (+17.63%)</td><td>21.85 <b>(-48.11%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>174.10 (n/a)</td><td>157.10 (n/a)</td><td>125.90 (n/a)</td><td>42.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+10.52%)</td><td>0.03 (+13.85%)</td><td>0.03 <b>(+25.93%)</b></td><td>0.02 (+15.67%)</td><td>0.00 <b>(+20.69%)</b></td><td>205.60 (-13.54%)</td><td>163.94 (-11.90%)</td><td>145.80 <b>(-20.63%)</b></td><td>137.00 (-9.51%)</td><td>30.45 (-6.83%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.80 (n/a)</td><td>186.08 (n/a)</td><td>183.70 (n/a)</td><td>151.40 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 <b>(+24.55%)</b></td><td>0.03 (+18.80%)</td><td>0.03 (+10.07%)</td><td>0.02 (+14.14%)</td><td>0.01 <b>(+43.00%)</b></td><td>187.40 (-12.39%)</td><td>152.54 (-15.07%)</td><td>163.80 (-9.15%)</td><td>117.20 (-19.73%)</td><td>29.38 (-1.06%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.90 (n/a)</td><td>179.60 (n/a)</td><td>180.30 (n/a)</td><td>146.00 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+15.45%)</td><td>0.03 (+16.91%)</td><td>0.03 <b>(+22.10%)</b></td><td>0.02 <b>(+21.45%)</b></td><td>0.01 <b>(+29.95%)</b></td><td>180.00 (-17.66%)</td><td>144.14 (-13.82%)</td><td>135.40 (-18.09%)</td><td>112.30 (-13.35%)</td><td>32.31 (-5.93%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.60 (n/a)</td><td>167.26 (n/a)</td><td>165.30 (n/a)</td><td>129.60 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 <b>(+29.23%)</b></td><td>0.02 <b>(+43.77%)</b></td><td>0.02 <b>(+53.41%)</b></td><td>0.02 <b>(+43.57%)</b></td><td>0.00 (+12.61%)</td><td>200.70 <b>(-30.36%)</b></td><td>170.26 <b>(-30.93%)</b></td><td>171.20 <b>(-34.81%)</b></td><td>144.30 <b>(-22.63%)</b></td><td>24.00 <b>(-38.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>288.20 (n/a)</td><td>246.52 (n/a)</td><td>262.60 (n/a)</td><td>186.50 (n/a)</td><td>39.34 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+14.72%)</td><td>0.03 <b>(+21.95%)</b></td><td>0.03 <b>(+27.94%)</b></td><td>0.02 <b>(+31.38%)</b></td><td>0.00 <b>(-41.14%)</b></td><td>166.40 <b>(-23.88%)</b></td><td>152.12 (-18.99%)</td><td>153.90 <b>(-21.84%)</b></td><td>138.20 (-12.86%)</td><td>10.40 <b>(-60.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.60 (n/a)</td><td>187.78 (n/a)</td><td>196.90 (n/a)</td><td>158.60 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-5.95%)</td><td>0.03 (+5.52%)</td><td>0.03 (+15.16%)</td><td>0.02 <b>(+26.48%)</b></td><td>0.00 <b>(-47.82%)</b></td><td>176.30 <b>(-20.94%)</b></td><td>156.80 (-8.94%)</td><td>156.10 (-13.18%)</td><td>129.60 (+6.32%)</td><td>19.19 <b>(-55.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>172.20 (n/a)</td><td>179.80 (n/a)</td><td>121.90 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 <b>(+45.30%)</b></td><td>0.03 <b>(+28.95%)</b></td><td>0.03 (+19.32%)</td><td>0.02 (+11.79%)</td><td>0.00 <b>(+345.55%)</b></td><td>177.40 (-10.54%)</td><td>146.10 <b>(-20.97%)</b></td><td>152.70 (-16.19%)</td><td>122.20 <b>(-31.15%)</b></td><td>23.48 <b>(+165.99%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.30 (n/a)</td><td>184.86 (n/a)</td><td>182.20 (n/a)</td><td>177.50 (n/a)</td><td>8.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+1.30%)</td><td>0.06 (+19.35%)</td><td>0.06 (+16.31%)</td><td>0.05 <b>(+44.09%)</b></td><td>0.00 <b>(-57.08%)</b></td><td>157.80 <b>(-30.61%)</b></td><td>144.70 (-18.18%)</td><td>147.30 (-14.01%)</td><td>134.10 (-1.32%)</td><td>9.59 <b>(-71.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>176.86 (n/a)</td><td>171.30 (n/a)</td><td>135.90 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 <b>(+32.41%)</b></td><td>0.07 <b>(+30.25%)</b></td><td>0.06 <b>(+26.56%)</b></td><td>0.06 <b>(+56.41%)</b></td><td>0.01 (-2.81%)</td><td>147.70 <b>(-36.09%)</b></td><td>128.46 <b>(-25.06%)</b></td><td>132.80 <b>(-20.95%)</b></td><td>98.30 <b>(-24.44%)</b></td><td>20.28 <b>(-51.79%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>171.42 (n/a)</td><td>168.00 (n/a)</td><td>130.10 (n/a)</td><td>42.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (-1.53%)</td><td>0.04 (-11.20%)</td><td>0.04 (-13.44%)</td><td>0.04 (-17.36%)</td><td>0.00 <b>(+128.63%)</b></td><td>226.50 <b>(+20.99%)</b></td><td>200.58 (+13.35%)</td><td>200.70 (+15.54%)</td><td>172.70 (+1.53%)</td><td>19.48 <b>(+178.19%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.20 (n/a)</td><td>176.96 (n/a)</td><td>173.70 (n/a)</td><td>170.10 (n/a)</td><td>7.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (-9.68%)</td><td>0.04 (-3.00%)</td><td>0.04 (+2.17%)</td><td>0.04 (-7.60%)</td><td>0.01 (-18.54%)</td><td>219.30 (+8.24%)</td><td>188.04 (+2.79%)</td><td>192.00 (-2.14%)</td><td>164.50 (+10.70%)</td><td>22.10 (-3.91%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>182.94 (n/a)</td><td>196.20 (n/a)</td><td>148.60 (n/a)</td><td>23.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (+14.13%)</td><td>0.06 <b>(+23.06%)</b></td><td>0.06 (+9.70%)</td><td>0.05 <b>(+52.79%)</b></td><td>0.01 (-19.41%)</td><td>152.10 <b>(-34.55%)</b></td><td>132.82 <b>(-21.24%)</b></td><td>141.40 (-8.89%)</td><td>105.00 (-12.43%)</td><td>19.70 <b>(-54.38%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.40 (n/a)</td><td>168.64 (n/a)</td><td>155.20 (n/a)</td><td>119.90 (n/a)</td><td>43.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(+27.76%)</b></td><td>0.06 <b>(+27.82%)</b></td><td>0.06 <b>(+23.76%)</b></td><td>0.04 (+11.56%)</td><td>0.01 <b>(+60.33%)</b></td><td>193.30 (-10.34%)</td><td>145.68 <b>(-20.60%)</b></td><td>146.20 (-19.18%)</td><td>113.10 <b>(-21.68%)</b></td><td>30.28 (+15.93%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>183.48 (n/a)</td><td>180.90 (n/a)</td><td>144.40 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (+19.81%)</td><td>0.06 (+13.03%)</td><td>0.06 (+18.22%)</td><td>0.04 (-1.59%)</td><td>0.01 <b>(+67.26%)</b></td><td>191.40 (+1.59%)</td><td>150.22 (-10.41%)</td><td>147.40 (-15.43%)</td><td>120.90 (-16.51%)</td><td>25.58 <b>(+45.68%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.40 (n/a)</td><td>167.68 (n/a)</td><td>174.30 (n/a)</td><td>144.80 (n/a)</td><td>17.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-15.76%)</td><td>0.05 (+7.98%)</td><td>0.06 <b>(+28.54%)</b></td><td>0.04 (+13.65%)</td><td>0.01 <b>(-45.13%)</b></td><td>199.40 (-12.00%)</td><td>153.48 (-11.00%)</td><td>143.00 <b>(-22.20%)</b></td><td>132.90 (+18.77%)</td><td>26.65 <b>(-39.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>172.44 (n/a)</td><td>183.80 (n/a)</td><td>111.90 (n/a)</td><td>44.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-12.98%)</td><td>0.05 (-5.68%)</td><td>0.05 (-12.76%)</td><td>0.04 (+1.73%)</td><td>0.01 <b>(-29.97%)</b></td><td>184.70 (-1.70%)</td><td>166.70 (+5.07%)</td><td>174.00 (+14.62%)</td><td>146.10 (+14.86%)</td><td>18.99 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.90 (n/a)</td><td>158.66 (n/a)</td><td>151.80 (n/a)</td><td>127.20 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-5.43%)</td><td>0.05 (-0.14%)</td><td>0.05 (-0.44%)</td><td>0.05 (+12.47%)</td><td>0.00 <b>(-40.88%)</b></td><td>177.80 (-11.10%)</td><td>159.50 (-0.97%)</td><td>154.40 (+0.39%)</td><td>144.60 (+5.78%)</td><td>13.27 <b>(-45.18%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>161.06 (n/a)</td><td>153.80 (n/a)</td><td>136.70 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (+13.92%)</td><td>0.05 (-6.21%)</td><td>0.05 (-2.89%)</td><td>0.04 <b>(-27.81%)</b></td><td>0.01 <b>(+232.13%)</b></td><td>231.90 <b>(+38.53%)</b></td><td>167.94 (+11.17%)</td><td>153.80 (+2.95%)</td><td>123.00 (-12.21%)</td><td>41.47 <b>(+307.27%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>167.40 (n/a)</td><td>151.06 (n/a)</td><td>149.40 (n/a)</td><td>140.10 (n/a)</td><td>10.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(+26.88%)</b></td><td>0.06 (+12.26%)</td><td>0.05 (+4.57%)</td><td>0.05 (+4.71%)</td><td>0.01 <b>(+161.91%)</b></td><td>174.80 (-4.48%)</td><td>147.80 (-9.29%)</td><td>152.80 (-4.38%)</td><td>117.40 <b>(-21.21%)</b></td><td>24.23 <b>(+94.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>183.00 (n/a)</td><td>162.94 (n/a)</td><td>159.80 (n/a)</td><td>149.00 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+3.88%)</td><td>0.05 (+6.26%)</td><td>0.05 (-0.69%)</td><td>0.04 <b>(+21.70%)</b></td><td>0.00 <b>(-32.73%)</b></td><td>185.00 (-17.85%)</td><td>171.42 (-7.01%)</td><td>175.30 (+0.69%)</td><td>146.50 (-3.68%)</td><td>14.61 <b>(-48.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>184.34 (n/a)</td><td>174.10 (n/a)</td><td>152.10 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (-12.45%)</td><td>0.05 (+7.87%)</td><td>0.05 <b>(+23.57%)</b></td><td>0.04 (+4.24%)</td><td>0.01 <b>(-35.46%)</b></td><td>212.50 (-4.06%)</td><td>174.08 (-9.13%)</td><td>167.60 (-19.11%)</td><td>150.80 (+14.16%)</td><td>25.98 <b>(-29.51%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>191.58 (n/a)</td><td>207.20 (n/a)</td><td>132.10 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 <b>(+27.57%)</b></td><td>0.05 (+11.36%)</td><td>0.04 (-7.87%)</td><td>0.04 <b>(+25.46%)</b></td><td>0.01 <b>(+31.46%)</b></td><td>201.70 <b>(-20.28%)</b></td><td>172.84 (-9.84%)</td><td>195.40 (+8.56%)</td><td>114.10 <b>(-21.63%)</b></td><td>37.78 (-16.88%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.00 (n/a)</td><td>191.70 (n/a)</td><td>180.00 (n/a)</td><td>145.60 (n/a)</td><td>45.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+2.60%)</td><td>0.05 (-9.98%)</td><td>0.05 (-11.67%)</td><td>0.04 (-15.54%)</td><td>0.01 <b>(+68.59%)</b></td><td>203.80 (+18.42%)</td><td>169.86 (+13.41%)</td><td>159.60 (+13.19%)</td><td>131.20 (-2.53%)</td><td>32.49 <b>(+102.68%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>149.78 (n/a)</td><td>141.00 (n/a)</td><td>134.60 (n/a)</td><td>16.03 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (+9.40%)</td><td>0.12 (+2.23%)</td><td>0.11 (+1.90%)</td><td>0.10 (-1.14%)</td><td>0.03 <b>(+29.84%)</b></td><td>166.50 (+1.15%)</td><td>140.94 (-0.79%)</td><td>151.60 (-1.88%)</td><td>99.30 (-8.56%)</td><td>29.02 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>164.60 (n/a)</td><td>142.06 (n/a)</td><td>154.50 (n/a)</td><td>108.60 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (-5.03%)</td><td>0.11 (-0.01%)</td><td>0.11 (-13.11%)</td><td>0.09 <b>(+34.27%)</b></td><td>0.01 <b>(-60.76%)</b></td><td>177.40 <b>(-25.56%)</b></td><td>152.06 (-5.19%)</td><td>149.40 (+15.10%)</td><td>134.60 (+5.32%)</td><td>15.69 <b>(-67.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>238.30 (n/a)</td><td>160.38 (n/a)</td><td>129.80 (n/a)</td><td>127.80 (n/a)</td><td>48.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (+8.88%)</td><td>0.08 (+5.16%)</td><td>0.08 (+3.89%)</td><td>0.07 (+0.53%)</td><td>0.01 <b>(+75.24%)</b></td><td>233.10 (-0.51%)</td><td>206.84 (-4.53%)</td><td>209.50 (-3.77%)</td><td>188.50 (-8.18%)</td><td>18.70 <b>(+58.74%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>216.66 (n/a)</td><td>217.70 (n/a)</td><td>205.30 (n/a)</td><td>11.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (+2.74%)</td><td>0.08 (+11.65%)</td><td>0.09 (+16.18%)</td><td>0.07 (+7.07%)</td><td>0.01 (+1.23%)</td><td>232.00 (-6.60%)</td><td>197.98 (-10.46%)</td><td>190.60 (-13.95%)</td><td>184.90 (-2.63%)</td><td>19.56 (-5.92%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>248.40 (n/a)</td><td>221.12 (n/a)</td><td>221.50 (n/a)</td><td>189.90 (n/a)</td><td>20.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 <b>(+31.40%)</b></td><td>0.09 (-0.45%)</td><td>0.10 (+1.09%)</td><td>0.05 <b>(-37.26%)</b></td><td>0.03 <b>(+395.76%)</b></td><td>311.70 <b>(+59.44%)</b></td><td>192.66 (+9.08%)</td><td>172.00 (-1.09%)</td><td>128.20 <b>(-23.92%)</b></td><td>70.10 <b>(+534.63%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>176.62 (n/a)</td><td>173.90 (n/a)</td><td>168.50 (n/a)</td><td>11.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (+19.99%)</td><td>0.10 (+16.43%)</td><td>0.10 (+15.25%)</td><td>0.08 (+15.57%)</td><td>0.01 <b>(+37.32%)</b></td><td>199.60 (-13.44%)</td><td>171.46 (-13.81%)</td><td>169.90 (-13.27%)</td><td>146.80 (-16.69%)</td><td>22.15 (-0.56%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>198.94 (n/a)</td><td>195.90 (n/a)</td><td>176.20 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (+14.41%)</td><td>0.10 (+8.69%)</td><td>0.10 (+5.01%)</td><td>0.09 (+19.83%)</td><td>0.01 (+10.27%)</td><td>190.60 (-16.55%)</td><td>168.78 (-8.18%)</td><td>169.40 (-4.78%)</td><td>136.90 (-12.58%)</td><td>20.94 <b>(-22.21%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>183.82 (n/a)</td><td>177.90 (n/a)</td><td>156.60 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (+0.19%)</td><td>0.10 (+13.18%)</td><td>0.10 (+19.02%)</td><td>0.09 (+17.45%)</td><td>0.01 <b>(-38.93%)</b></td><td>180.00 (-14.85%)</td><td>161.26 (-12.72%)</td><td>164.40 (-15.95%)</td><td>145.20 (-0.21%)</td><td>13.75 <b>(-48.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>184.76 (n/a)</td><td>195.60 (n/a)</td><td>145.50 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (+10.75%)</td><td>0.09 (+0.59%)</td><td>0.09 (+3.09%)</td><td>0.07 (-0.11%)</td><td>0.02 <b>(+29.29%)</b></td><td>233.80 (+0.13%)</td><td>187.94 (+0.17%)</td><td>181.40 (-2.99%)</td><td>145.40 (-9.75%)</td><td>32.17 (+14.86%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>187.62 (n/a)</td><td>187.00 (n/a)</td><td>161.10 (n/a)</td><td>28.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (-3.08%)</td><td>0.09 (+3.62%)</td><td>0.10 (+11.74%)</td><td>0.07 (-16.57%)</td><td>0.02 (+13.65%)</td><td>240.40 (+19.90%)</td><td>179.64 (-2.45%)</td><td>171.20 (-10.51%)</td><td>146.80 (+3.16%)</td><td>35.59 <b>(+49.84%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>184.16 (n/a)</td><td>191.30 (n/a)</td><td>142.30 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (+12.55%)</td><td>0.10 (-0.58%)</td><td>0.10 (+6.76%)</td><td>0.06 <b>(-31.35%)</b></td><td>0.03 <b>(+79.26%)</b></td><td>279.90 <b>(+45.71%)</b></td><td>184.64 (+8.12%)</td><td>167.50 (-6.32%)</td><td>110.70 (-11.16%)</td><td>64.18 <b>(+142.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.10 (n/a)</td><td>170.78 (n/a)</td><td>178.80 (n/a)</td><td>124.60 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 <b>(+44.16%)</b></td><td>0.10 <b>(+25.18%)</b></td><td>0.11 <b>(+35.76%)</b></td><td>0.07 (+0.15%)</td><td>0.03 <b>(+197.71%)</b></td><td>230.70 (-0.13%)</td><td>166.46 (-16.39%)</td><td>145.70 <b>(-26.34%)</b></td><td>119.10 <b>(-30.63%)</b></td><td>44.75 <b>(+109.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>199.08 (n/a)</td><td>197.80 (n/a)</td><td>171.70 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 <b>(+40.43%)</b></td><td>0.09 (+8.40%)</td><td>0.08 (+1.26%)</td><td>0.06 (-15.27%)</td><td>0.02 <b>(+326.64%)</b></td><td>265.90 (+18.02%)</td><td>195.32 (-3.27%)</td><td>194.90 (-1.27%)</td><td>134.40 <b>(-28.78%)</b></td><td>48.78 <b>(+251.09%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>225.30 (n/a)</td><td>201.92 (n/a)</td><td>197.40 (n/a)</td><td>188.70 (n/a)</td><td>13.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (+7.46%)</td><td>0.10 <b>(+23.10%)</b></td><td>0.10 <b>(+21.47%)</b></td><td>0.09 <b>(+47.98%)</b></td><td>0.01 <b>(-48.70%)</b></td><td>187.60 <b>(-32.45%)</b></td><td>169.24 <b>(-20.72%)</b></td><td>166.80 (-17.71%)</td><td>153.20 (-6.98%)</td><td>13.32 <b>(-68.05%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>277.70 (n/a)</td><td>213.48 (n/a)</td><td>202.70 (n/a)</td><td>164.70 (n/a)</td><td>41.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 <b>(+25.13%)</b></td><td>0.09 (+7.68%)</td><td>0.08 (-1.69%)</td><td>0.06 (+4.55%)</td><td>0.03 <b>(+41.95%)</b></td><td>265.30 (-4.36%)</td><td>194.00 (-5.20%)</td><td>202.80 (+1.71%)</td><td>123.30 <b>(-20.09%)</b></td><td>52.49 (+6.57%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>277.40 (n/a)</td><td>204.64 (n/a)</td><td>199.40 (n/a)</td><td>154.30 (n/a)</td><td>49.25 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 <b>(+54.53%)</b></td><td>0.11 <b>(+31.62%)</b></td><td>0.10 (+19.10%)</td><td>0.09 (+10.41%)</td><td>0.03 <b>(+392.09%)</b></td><td>185.40 (-9.43%)</td><td>155.32 <b>(-20.96%)</b></td><td>168.90 (-16.01%)</td><td>114.30 <b>(-35.28%)</b></td><td>34.18 <b>(+192.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>196.50 (n/a)</td><td>201.10 (n/a)</td><td>176.60 (n/a)</td><td>11.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-4.72%)</td><td>0.19 (+2.34%)</td><td>0.18 (+1.69%)</td><td>0.15 <b>(+22.02%)</b></td><td>0.03 <b>(-33.71%)</b></td><td>215.20 (-18.05%)</td><td>178.18 (-5.45%)</td><td>181.00 (-1.63%)</td><td>141.20 (+4.90%)</td><td>28.32 <b>(-43.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>262.60 (n/a)</td><td>188.46 (n/a)</td><td>184.00 (n/a)</td><td>134.60 (n/a)</td><td>49.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (+1.29%)</td><td>0.20 (+8.48%)</td><td>0.20 (+3.85%)</td><td>0.16 (+15.22%)</td><td>0.02 <b>(-28.51%)</b></td><td>206.20 (-13.22%)</td><td>168.46 (-9.34%)</td><td>167.20 (-3.69%)</td><td>147.30 (-1.27%)</td><td>22.98 <b>(-38.09%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.60 (n/a)</td><td>185.82 (n/a)</td><td>173.60 (n/a)</td><td>149.20 (n/a)</td><td>37.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.18 (-1.12%)</td><td>0.15 (+1.68%)</td><td>0.16 (-2.15%)</td><td>0.14 <b>(+44.33%)</b></td><td>0.02 <b>(-49.61%)</b></td><td>239.50 <b>(-30.72%)</b></td><td>215.00 (-5.70%)</td><td>209.00 (+2.20%)</td><td>187.10 (+1.14%)</td><td>22.83 <b>(-65.62%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>345.70 (n/a)</td><td>228.00 (n/a)</td><td>204.50 (n/a)</td><td>185.00 (n/a)</td><td>66.41 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 <b>(-32.39%)</b></td><td>0.15 (-11.01%)</td><td>0.15 (-3.76%)</td><td>0.13 (+9.63%)</td><td>0.02 <b>(-64.94%)</b></td><td>243.90 (-8.79%)</td><td>215.80 (+7.04%)</td><td>217.40 (+3.92%)</td><td>187.30 <b>(+47.95%)</b></td><td>24.98 <b>(-50.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>267.40 (n/a)</td><td>201.60 (n/a)</td><td>209.20 (n/a)</td><td>126.60 (n/a)</td><td>50.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 <b>(+31.35%)</b></td><td>0.20 (+14.81%)</td><td>0.21 (+19.65%)</td><td>0.16 (-0.54%)</td><td>0.04 <b>(+199.69%)</b></td><td>202.70 (+0.50%)</td><td>165.80 (-10.74%)</td><td>157.60 (-16.39%)</td><td>128.00 <b>(-23.85%)</b></td><td>31.08 <b>(+134.02%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>185.74 (n/a)</td><td>188.50 (n/a)</td><td>168.10 (n/a)</td><td>13.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (-6.68%)</td><td>0.19 (-7.52%)</td><td>0.18 (-8.30%)</td><td>0.17 (-5.15%)</td><td>0.02 (-19.03%)</td><td>192.50 (+5.42%)</td><td>177.52 (+7.88%)</td><td>182.90 (+9.06%)</td><td>152.40 (+7.17%)</td><td>15.88 (-9.70%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>182.60 (n/a)</td><td>164.56 (n/a)</td><td>167.70 (n/a)</td><td>142.20 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (-15.69%)</td><td>0.20 (-5.25%)</td><td>0.19 (-12.90%)</td><td>0.16 <b>(+72.87%)</b></td><td>0.04 <b>(-49.39%)</b></td><td>198.60 <b>(-42.15%)</b></td><td>165.30 (-6.99%)</td><td>168.20 (+14.81%)</td><td>127.50 (+18.60%)</td><td>29.65 <b>(-68.51%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>343.30 (n/a)</td><td>177.72 (n/a)</td><td>146.50 (n/a)</td><td>107.50 (n/a)</td><td>94.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.24 (-15.79%)</td><td>0.20 (-2.49%)</td><td>0.19 (-3.85%)</td><td>0.16 (+6.64%)</td><td>0.03 <b>(-38.48%)</b></td><td>199.70 (-6.24%)</td><td>163.24 (-0.34%)</td><td>168.20 (+4.02%)</td><td>135.50 (+18.76%)</td><td>26.43 <b>(-33.30%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.00 (n/a)</td><td>163.80 (n/a)</td><td>161.70 (n/a)</td><td>114.10 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (-2.49%)</td><td>0.17 (-14.05%)</td><td>0.18 (-8.60%)</td><td>0.11 <b>(-34.53%)</b></td><td>0.04 <b>(+77.57%)</b></td><td>306.30 <b>(+52.77%)</b></td><td>204.12 <b>(+21.76%)</b></td><td>183.10 (+9.44%)</td><td>148.70 (+2.55%)</td><td>60.04 <b>(+189.92%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>167.64 (n/a)</td><td>167.30 (n/a)</td><td>145.00 (n/a)</td><td>20.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (-4.49%)</td><td>0.18 (-6.75%)</td><td>0.18 (-6.15%)</td><td>0.15 (-12.44%)</td><td>0.02 (+11.92%)</td><td>216.40 (+14.20%)</td><td>184.54 (+7.73%)</td><td>186.80 (+6.56%)</td><td>149.90 (+4.68%)</td><td>24.18 <b>(+33.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>189.50 (n/a)</td><td>171.30 (n/a)</td><td>175.30 (n/a)</td><td>143.20 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (-4.48%)</td><td>0.20 (-5.36%)</td><td>0.18 (-6.11%)</td><td>0.16 (+2.93%)</td><td>0.05 (-6.29%)</td><td>207.90 (-2.85%)</td><td>171.94 (+5.21%)</td><td>177.60 (+6.54%)</td><td>115.80 (+4.70%)</td><td>34.89 (-5.23%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>214.00 (n/a)</td><td>163.42 (n/a)</td><td>166.70 (n/a)</td><td>110.60 (n/a)</td><td>36.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (+17.76%)</td><td>0.21 (+2.96%)</td><td>0.19 (-10.53%)</td><td>0.15 (-11.12%)</td><td>0.04 <b>(+89.72%)</b></td><td>212.60 (+12.55%)</td><td>164.64 (-0.35%)</td><td>171.80 (+11.78%)</td><td>125.10 (-15.13%)</td><td>35.26 <b>(+76.22%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.90 (n/a)</td><td>165.22 (n/a)</td><td>153.70 (n/a)</td><td>147.40 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 <b>(-20.69%)</b></td><td>0.18 (+1.94%)</td><td>0.19 (+9.76%)</td><td>0.16 <b>(+22.90%)</b></td><td>0.02 <b>(-61.49%)</b></td><td>209.70 (-18.63%)</td><td>184.90 (-5.64%)</td><td>173.20 (-8.89%)</td><td>169.70 <b>(+26.08%)</b></td><td>18.21 <b>(-60.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>257.70 (n/a)</td><td>195.96 (n/a)</td><td>190.10 (n/a)</td><td>134.60 (n/a)</td><td>45.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 <b>(-32.91%)</b></td><td>0.18 (-15.12%)</td><td>0.18 (-10.60%)</td><td>0.16 (+5.23%)</td><td>0.01 <b>(-77.37%)</b></td><td>202.90 (-4.96%)</td><td>184.92 (+12.36%)</td><td>180.40 (+11.84%)</td><td>172.30 <b>(+49.05%)</b></td><td>12.93 <b>(-68.26%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.50 (n/a)</td><td>164.58 (n/a)</td><td>161.30 (n/a)</td><td>115.60 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (-19.14%)</td><td>0.17 (+3.93%)</td><td>0.19 (+15.62%)</td><td>0.11 (+0.75%)</td><td>0.04 <b>(-38.53%)</b></td><td>308.50 (-0.74%)</td><td>199.00 (-9.49%)</td><td>172.80 (-13.51%)</td><td>161.60 <b>(+23.74%)</b></td><td>61.66 <b>(-25.45%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>310.80 (n/a)</td><td>219.86 (n/a)</td><td>199.80 (n/a)</td><td>130.60 (n/a)</td><td>82.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (-8.73%)</td><td>0.19 (-4.29%)</td><td>0.19 (-2.22%)</td><td>0.15 (-8.65%)</td><td>0.03 (-16.87%)</td><td>217.10 (+9.48%)</td><td>175.72 (+4.12%)</td><td>170.40 (+2.28%)</td><td>147.70 (+9.57%)</td><td>26.46 (-0.43%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>198.30 (n/a)</td><td>168.76 (n/a)</td><td>166.60 (n/a)</td><td>134.80 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (+0.87%)</td><td>0.21 (+0.22%)</td><td>0.21 (+0.10%)</td><td>0.21 (+0.06%)</td><td>0.00 <b>(+141.22%)</b></td><td>40901.20 (-0.06%)</td><td>40755.80 (-0.22%)</td><td>40833.70 (-0.10%)</td><td>40384.90 (-0.86%)</td><td>211.51 <b>(+138.80%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40927.70 (n/a)</td><td>40844.62 (n/a)</td><td>40876.60 (n/a)</td><td>40735.60 (n/a)</td><td>88.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (+0.31%)</td><td>0.21 (+0.04%)</td><td>0.21 (-0.05%)</td><td>0.21 (-0.11%)</td><td>0.00 <b>(+64.66%)</b></td><td>40899.70 (+0.11%)</td><td>40755.16 (-0.04%)</td><td>40822.60 (+0.05%)</td><td>40449.80 (-0.31%)</td><td>184.54 <b>(+64.34%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40855.20 (n/a)</td><td>40769.98 (n/a)</td><td>40802.00 (n/a)</td><td>40574.50 (n/a)</td><td>112.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (-0.01%)</td><td>0.13 (+0.00%)</td><td>0.13 (+0.00%)</td><td>0.13 (+0.03%)</td><td>0.00 <b>(-40.04%)</b></td><td>321831.30 (-0.03%)</td><td>321726.62 (-0.00%)</td><td>321695.90 (-0.00%)</td><td>321631.00 (+0.01%)</td><td>84.50 <b>(-40.04%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321919.00 (n/a)</td><td>321727.02 (n/a)</td><td>321696.20 (n/a)</td><td>321590.20 (n/a)</td><td>140.93 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+3.24%)</td><td>0.02 (-16.66%)</td><td>0.02 <b>(-27.12%)</b></td><td>0.02 <b>(-24.23%)</b></td><td>0.01 <b>(+78.98%)</b></td><td>210.60 <b>(+31.95%)</b></td><td>174.26 <b>(+23.33%)</b></td><td>184.10 <b>(+37.18%)</b></td><td>124.00 (-3.12%)</td><td>35.01 <b>(+127.40%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>159.60 (n/a)</td><td>141.30 (n/a)</td><td>134.20 (n/a)</td><td>128.00 (n/a)</td><td>15.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (+15.50%)</td><td>0.04 (+11.94%)</td><td>0.04 (+4.55%)</td><td>0.03 (+6.32%)</td><td>0.01 <b>(+52.09%)</b></td><td>189.90 (-5.94%)</td><td>156.04 (-9.25%)</td><td>165.40 (-4.34%)</td><td>117.50 (-13.41%)</td><td>30.70 <b>(+24.86%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>171.94 (n/a)</td><td>172.90 (n/a)</td><td>135.70 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-15.61%)</td><td>0.02 <b>(-21.85%)</b></td><td>0.02 (-16.47%)</td><td>0.01 <b>(-35.05%)</b></td><td>0.00 <b>(+26.33%)</b></td><td>288.20 <b>(+54.04%)</b></td><td>208.34 <b>(+32.03%)</b></td><td>189.40 (+19.72%)</td><td>149.40 (+18.48%)</td><td>52.29 <b>(+137.74%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.10 (n/a)</td><td>157.80 (n/a)</td><td>158.20 (n/a)</td><td>126.10 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+4.78%)</td><td>0.04 (+10.08%)</td><td>0.03 (+2.56%)</td><td>0.03 <b>(+57.27%)</b></td><td>0.00 <b>(-51.31%)</b></td><td>165.90 <b>(-36.44%)</b></td><td>147.10 (-14.30%)</td><td>147.40 (-2.45%)</td><td>123.60 (-4.56%)</td><td>16.39 <b>(-70.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>261.00 (n/a)</td><td>171.64 (n/a)</td><td>151.10 (n/a)</td><td>129.50 (n/a)</td><td>54.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 <b>(-31.17%)</b></td><td>0.02 (-14.40%)</td><td>0.02 (-5.42%)</td><td>0.01 (+19.58%)</td><td>0.01 <b>(-49.80%)</b></td><td>282.60 (-16.39%)</td><td>188.72 (+4.15%)</td><td>172.60 (+5.76%)</td><td>130.80 <b>(+45.33%)</b></td><td>56.46 <b>(-39.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>338.00 (n/a)</td><td>181.20 (n/a)</td><td>163.20 (n/a)</td><td>90.00 (n/a)</td><td>92.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+6.87%)</td><td>0.04 <b>(+24.69%)</b></td><td>0.03 <b>(+23.82%)</b></td><td>0.03 <b>(+62.30%)</b></td><td>0.00 <b>(-41.65%)</b></td><td>169.60 <b>(-38.37%)</b></td><td>146.98 <b>(-23.79%)</b></td><td>148.70 (-19.23%)</td><td>125.80 (-6.47%)</td><td>18.71 <b>(-66.54%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>275.20 (n/a)</td><td>192.86 (n/a)</td><td>184.10 (n/a)</td><td>134.50 (n/a)</td><td>55.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 <b>(-30.12%)</b></td><td>0.02 (-2.35%)</td><td>0.02 (+11.73%)</td><td>0.02 <b>(+33.40%)</b></td><td>0.00 <b>(-75.50%)</b></td><td>219.20 <b>(-25.06%)</b></td><td>195.92 (-5.44%)</td><td>195.30 (-10.49%)</td><td>172.30 <b>(+43.11%)</b></td><td>17.12 <b>(-72.82%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>292.50 (n/a)</td><td>207.20 (n/a)</td><td>218.20 (n/a)</td><td>120.40 (n/a)</td><td>62.99 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+17.68%)</td><td>0.03 <b>(+25.03%)</b></td><td>0.04 <b>(+21.41%)</b></td><td>0.03 <b>(+35.21%)</b></td><td>0.00 <b>(-31.89%)</b></td><td>150.90 <b>(-26.03%)</b></td><td>135.26 <b>(-20.85%)</b></td><td>130.10 (-17.66%)</td><td>126.70 (-15.02%)</td><td>10.11 <b>(-57.27%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.00 (n/a)</td><td>170.88 (n/a)</td><td>158.00 (n/a)</td><td>149.10 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+11.34%)</td><td>0.02 (-2.89%)</td><td>0.02 (-5.35%)</td><td>0.02 (-10.60%)</td><td>0.00 <b>(+187.98%)</b></td><td>210.40 (+11.86%)</td><td>184.10 (+4.11%)</td><td>187.10 (+5.65%)</td><td>149.40 (-10.22%)</td><td>21.98 <b>(+182.08%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.10 (n/a)</td><td>176.84 (n/a)</td><td>177.10 (n/a)</td><td>166.40 (n/a)</td><td>7.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (+19.65%)</td><td>0.03 <b>(+21.38%)</b></td><td>0.03 <b>(+23.96%)</b></td><td>0.02 <b>(+20.72%)</b></td><td>0.01 (+2.44%)</td><td>200.60 (-17.14%)</td><td>158.44 (-18.46%)</td><td>148.00 (-19.35%)</td><td>124.50 (-16.44%)</td><td>29.14 <b>(-30.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>194.32 (n/a)</td><td>183.50 (n/a)</td><td>149.00 (n/a)</td><td>41.65 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+8.15%)</td><td>0.02 (+3.52%)</td><td>0.02 (+0.36%)</td><td>0.02 (+6.87%)</td><td>0.00 (+16.10%)</td><td>210.60 (-6.44%)</td><td>187.80 (-3.27%)</td><td>189.00 (-0.32%)</td><td>155.20 (-7.51%)</td><td>20.59 (-2.08%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.10 (n/a)</td><td>194.14 (n/a)</td><td>189.60 (n/a)</td><td>167.80 (n/a)</td><td>21.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-11.27%)</td><td>0.02 (-7.81%)</td><td>0.02 (-12.10%)</td><td>0.02 (-5.86%)</td><td>0.00 (+2.54%)</td><td>210.60 (+6.20%)</td><td>189.38 (+8.86%)</td><td>204.30 (+13.82%)</td><td>159.70 (+12.70%)</td><td>26.13 <b>(+25.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.30 (n/a)</td><td>173.96 (n/a)</td><td>179.50 (n/a)</td><td>141.70 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (+13.81%)</td><td>0.02 (+5.78%)</td><td>0.02 (+8.52%)</td><td>0.01 (-19.94%)</td><td>0.00 <b>(+155.12%)</b></td><td>273.10 <b>(+24.93%)</b></td><td>189.74 (-1.87%)</td><td>170.80 (-7.87%)</td><td>154.40 (-12.12%)</td><td>48.97 <b>(+182.43%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.60 (n/a)</td><td>193.36 (n/a)</td><td>185.40 (n/a)</td><td>175.70 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (-11.07%)</td><td>0.03 (+2.42%)</td><td>0.03 (+5.71%)</td><td>0.02 (+10.12%)</td><td>0.00 <b>(-32.99%)</b></td><td>228.80 (-9.21%)</td><td>178.08 (-4.97%)</td><td>162.40 (-5.36%)</td><td>146.50 (+12.43%)</td><td>32.49 <b>(-31.33%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.00 (n/a)</td><td>187.40 (n/a)</td><td>171.60 (n/a)</td><td>130.30 (n/a)</td><td>47.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (+17.02%)</td><td>0.02 (+5.97%)</td><td>0.02 (+14.34%)</td><td>0.02 (-9.92%)</td><td>0.00 <b>(+307.42%)</b></td><td>240.50 (+10.98%)</td><td>201.42 (-3.55%)</td><td>185.40 (-12.55%)</td><td>166.10 (-14.56%)</td><td>34.83 <b>(+300.62%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>208.84 (n/a)</td><td>212.00 (n/a)</td><td>194.40 (n/a)</td><td>8.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (+14.27%)</td><td>0.05 (+11.22%)</td><td>0.05 (+1.57%)</td><td>0.05 <b>(+48.87%)</b></td><td>0.01 <b>(-24.14%)</b></td><td>174.90 <b>(-32.81%)</b></td><td>155.52 (-12.73%)</td><td>162.30 (-1.58%)</td><td>125.00 (-12.53%)</td><td>19.89 <b>(-57.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.30 (n/a)</td><td>178.20 (n/a)</td><td>164.90 (n/a)</td><td>142.90 (n/a)</td><td>47.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (+11.48%)</td><td>0.08 (+6.87%)</td><td>0.07 (-2.32%)</td><td>0.06 (-0.66%)</td><td>0.02 <b>(+31.78%)</b></td><td>200.60 (+0.70%)</td><td>158.60 (-5.23%)</td><td>168.30 (+2.37%)</td><td>120.70 (-10.33%)</td><td>34.09 (+13.57%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>167.36 (n/a)</td><td>164.40 (n/a)</td><td>134.60 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-2.79%)</td><td>0.05 (+4.71%)</td><td>0.05 (-1.38%)</td><td>0.04 <b>(+29.99%)</b></td><td>0.01 <b>(-36.18%)</b></td><td>190.60 <b>(-23.05%)</b></td><td>166.60 (-8.48%)</td><td>178.80 (+1.42%)</td><td>130.50 (+2.84%)</td><td>26.27 <b>(-48.85%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.70 (n/a)</td><td>182.04 (n/a)</td><td>176.30 (n/a)</td><td>126.90 (n/a)</td><td>51.37 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (-2.34%)</td><td>0.07 (+11.43%)</td><td>0.07 (+5.10%)</td><td>0.06 <b>(+62.42%)</b></td><td>0.01 <b>(-53.08%)</b></td><td>180.80 <b>(-38.42%)</b></td><td>157.34 (-15.54%)</td><td>157.20 (-4.84%)</td><td>135.30 (+2.42%)</td><td>17.26 <b>(-72.29%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>293.60 (n/a)</td><td>186.28 (n/a)</td><td>165.20 (n/a)</td><td>132.10 (n/a)</td><td>62.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+8.92%)</td><td>0.05 (+2.76%)</td><td>0.05 (-4.67%)</td><td>0.04 (-7.87%)</td><td>0.01 <b>(+113.77%)</b></td><td>191.60 (+8.56%)</td><td>162.34 (-0.28%)</td><td>177.30 (+4.91%)</td><td>128.30 (-8.23%)</td><td>31.04 <b>(+109.24%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>176.50 (n/a)</td><td>162.80 (n/a)</td><td>169.00 (n/a)</td><td>139.80 (n/a)</td><td>14.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 <b>(+41.66%)</b></td><td>0.07 <b>(+31.37%)</b></td><td>0.07 <b>(+23.80%)</b></td><td>0.06 (+16.73%)</td><td>0.01 <b>(+193.88%)</b></td><td>182.10 (-14.35%)</td><td>153.18 <b>(-22.71%)</b></td><td>155.90 (-19.22%)</td><td>128.40 <b>(-29.41%)</b></td><td>23.53 <b>(+70.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>212.60 (n/a)</td><td>198.18 (n/a)</td><td>193.00 (n/a)</td><td>181.90 (n/a)</td><td>13.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-13.93%)</td><td>0.05 (-14.69%)</td><td>0.05 (-2.95%)</td><td>0.02 <b>(-48.56%)</b></td><td>0.01 <b>(+28.44%)</b></td><td>352.60 <b>(+94.48%)</b></td><td>199.64 <b>(+26.98%)</b></td><td>176.00 (+3.04%)</td><td>134.70 (+16.22%)</td><td>87.29 <b>(+210.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>157.22 (n/a)</td><td>170.80 (n/a)</td><td>115.90 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (+13.65%)</td><td>0.06 (+16.21%)</td><td>0.06 <b>(+22.49%)</b></td><td>0.05 (+18.35%)</td><td>0.01 (+5.30%)</td><td>183.20 (-15.54%)</td><td>155.34 (-14.30%)</td><td>154.30 (-18.36%)</td><td>120.60 (-12.04%)</td><td>23.62 <b>(-21.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>181.26 (n/a)</td><td>189.00 (n/a)</td><td>137.10 (n/a)</td><td>29.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (+6.92%)</td><td>0.05 (+19.79%)</td><td>0.06 (+16.38%)</td><td>0.04 <b>(+105.76%)</b></td><td>0.01 <b>(-40.21%)</b></td><td>182.60 <b>(-51.38%)</b></td><td>156.84 <b>(-24.56%)</b></td><td>147.80 (-14.07%)</td><td>125.20 (-6.50%)</td><td>24.71 <b>(-74.24%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>375.60 (n/a)</td><td>207.90 (n/a)</td><td>172.00 (n/a)</td><td>133.90 (n/a)</td><td>95.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (+1.94%)</td><td>0.06 (+11.09%)</td><td>0.06 <b>(+22.54%)</b></td><td>0.05 (+11.08%)</td><td>0.01 (+2.58%)</td><td>194.80 (-9.98%)</td><td>157.72 (-9.98%)</td><td>147.90 (-18.38%)</td><td>122.00 (-1.85%)</td><td>32.25 (-3.52%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>175.20 (n/a)</td><td>181.20 (n/a)</td><td>124.30 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (-11.64%)</td><td>0.05 (+3.63%)</td><td>0.05 (+17.69%)</td><td>0.04 (+2.05%)</td><td>0.01 (-17.21%)</td><td>204.90 (-2.01%)</td><td>175.98 (-3.95%)</td><td>157.40 (-15.06%)</td><td>157.00 (+13.19%)</td><td>25.81 (-7.07%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>183.22 (n/a)</td><td>185.30 (n/a)</td><td>138.70 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+6.57%)</td><td>0.05 (+4.92%)</td><td>0.05 <b>(+21.99%)</b></td><td>0.03 (-18.11%)</td><td>0.01 <b>(+25.59%)</b></td><td>272.90 <b>(+22.16%)</b></td><td>191.24 (-2.89%)</td><td>175.00 (-18.03%)</td><td>152.10 (-6.17%)</td><td>47.47 <b>(+51.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.40 (n/a)</td><td>196.94 (n/a)</td><td>213.50 (n/a)</td><td>162.10 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (-9.91%)</td><td>0.05 (-1.09%)</td><td>0.05 (+4.53%)</td><td>0.03 (-7.90%)</td><td>0.01 (-4.16%)</td><td>234.90 (+8.55%)</td><td>176.34 (+1.36%)</td><td>161.50 (-4.32%)</td><td>147.00 (+11.03%)</td><td>37.22 (+13.25%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>173.98 (n/a)</td><td>168.80 (n/a)</td><td>132.40 (n/a)</td><td>32.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+9.09%)</td><td>0.05 (+16.79%)</td><td>0.06 <b>(+38.16%)</b></td><td>0.04 (+18.07%)</td><td>0.01 <b>(+21.35%)</b></td><td>232.30 (-15.31%)</td><td>180.06 (-13.99%)</td><td>152.10 <b>(-27.64%)</b></td><td>149.60 (-8.33%)</td><td>40.39 (-7.13%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.30 (n/a)</td><td>209.34 (n/a)</td><td>210.20 (n/a)</td><td>163.20 (n/a)</td><td>43.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (+3.06%)</td><td>0.05 (+9.90%)</td><td>0.05 (+9.12%)</td><td>0.04 <b>(+42.06%)</b></td><td>0.01 <b>(-27.62%)</b></td><td>229.10 <b>(-29.59%)</b></td><td>184.90 (-12.73%)</td><td>177.50 (-8.32%)</td><td>147.00 (-2.91%)</td><td>31.70 <b>(-52.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>325.40 (n/a)</td><td>211.88 (n/a)</td><td>193.60 (n/a)</td><td>151.40 (n/a)</td><td>66.97 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (+7.07%)</td><td>0.10 (+0.06%)</td><td>0.09 (-7.86%)</td><td>0.08 (-2.09%)</td><td>0.02 <b>(+54.59%)</b></td><td>196.20 (+2.13%)</td><td>170.28 (+1.48%)</td><td>189.90 (+8.51%)</td><td>136.60 (-6.57%)</td><td>30.03 <b>(+49.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>167.80 (n/a)</td><td>175.00 (n/a)</td><td>146.20 (n/a)</td><td>20.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (+8.74%)</td><td>0.15 (+7.71%)</td><td>0.18 <b>(+26.17%)</b></td><td>0.08 <b>(-31.46%)</b></td><td>0.05 <b>(+110.19%)</b></td><td>297.30 <b>(+45.88%)</b></td><td>178.38 (+1.42%)</td><td>137.60 <b>(-20.74%)</b></td><td>125.90 (-8.04%)</td><td>73.10 <b>(+176.32%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>175.88 (n/a)</td><td>173.60 (n/a)</td><td>136.90 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (+13.84%)</td><td>0.11 (+4.46%)</td><td>0.10 (+2.14%)</td><td>0.08 (-2.82%)</td><td>0.02 <b>(+24.72%)</b></td><td>194.40 (+2.91%)</td><td>156.52 (-3.57%)</td><td>160.10 (-2.14%)</td><td>114.30 (-12.14%)</td><td>28.83 (+7.65%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.90 (n/a)</td><td>162.32 (n/a)</td><td>163.60 (n/a)</td><td>130.10 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (+2.13%)</td><td>0.12 (-4.15%)</td><td>0.12 (-2.31%)</td><td>0.07 <b>(-31.95%)</b></td><td>0.03 <b>(+49.19%)</b></td><td>292.10 <b>(+46.93%)</b></td><td>189.06 (+9.35%)</td><td>173.00 (+2.37%)</td><td>130.20 (-2.03%)</td><td>60.73 <b>(+124.21%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>172.90 (n/a)</td><td>169.00 (n/a)</td><td>132.90 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 <b>(+22.62%)</b></td><td>0.11 (+7.18%)</td><td>0.11 (+11.55%)</td><td>0.06 <b>(-29.93%)</b></td><td>0.03 <b>(+174.92%)</b></td><td>257.20 <b>(+42.73%)</b></td><td>162.92 (+0.69%)</td><td>146.80 (-10.32%)</td><td>110.10 (-18.50%)</td><td>58.06 <b>(+228.64%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.20 (n/a)</td><td>161.80 (n/a)</td><td>163.70 (n/a)</td><td>135.10 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 <b>(+43.22%)</b></td><td>0.12 <b>(+21.63%)</b></td><td>0.11 (+8.80%)</td><td>0.10 <b>(+32.61%)</b></td><td>0.02 <b>(+55.32%)</b></td><td>211.20 <b>(-24.60%)</b></td><td>174.04 (-17.41%)</td><td>179.80 (-8.12%)</td><td>128.80 <b>(-30.19%)</b></td><td>30.87 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>280.10 (n/a)</td><td>210.74 (n/a)</td><td>195.70 (n/a)</td><td>184.50 (n/a)</td><td>39.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (-0.25%)</td><td>0.09 (+1.67%)</td><td>0.09 (-3.77%)</td><td>0.07 (-6.39%)</td><td>0.02 (+14.25%)</td><td>243.40 (+6.80%)</td><td>181.42 (-0.78%)</td><td>178.50 (+3.90%)</td><td>146.20 (+0.21%)</td><td>38.38 <b>(+21.82%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.90 (n/a)</td><td>182.84 (n/a)</td><td>171.80 (n/a)</td><td>145.90 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (-1.57%)</td><td>0.12 (-8.88%)</td><td>0.13 (-8.88%)</td><td>0.06 <b>(-43.71%)</b></td><td>0.04 <b>(+51.04%)</b></td><td>327.10 <b>(+77.68%)</b></td><td>174.24 <b>(+21.34%)</b></td><td>145.70 (+9.71%)</td><td>118.80 (+1.54%)</td><td>86.55 <b>(+193.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>184.10 (n/a)</td><td>143.60 (n/a)</td><td>132.80 (n/a)</td><td>117.00 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 <b>(+41.28%)</b></td><td>0.10 <b>(+26.98%)</b></td><td>0.11 <b>(+38.95%)</b></td><td>0.07 (+12.01%)</td><td>0.03 <b>(+69.62%)</b></td><td>249.20 (-10.74%)</td><td>169.10 (-18.76%)</td><td>146.40 <b>(-28.06%)</b></td><td>117.60 <b>(-29.24%)</b></td><td>51.93 (+11.91%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>279.20 (n/a)</td><td>208.16 (n/a)</td><td>203.50 (n/a)</td><td>166.20 (n/a)</td><td>46.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (+10.75%)</td><td>0.12 (+12.33%)</td><td>0.12 (+3.11%)</td><td>0.10 <b>(+55.61%)</b></td><td>0.01 <b>(-50.06%)</b></td><td>177.60 <b>(-35.72%)</b></td><td>156.46 (-14.73%)</td><td>152.10 (-3.06%)</td><td>138.60 (-9.71%)</td><td>15.25 <b>(-71.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>276.30 (n/a)</td><td>183.48 (n/a)</td><td>156.90 (n/a)</td><td>153.50 (n/a)</td><td>52.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (+4.32%)</td><td>0.10 (+0.72%)</td><td>0.10 (+2.05%)</td><td>0.07 <b>(-20.32%)</b></td><td>0.02 <b>(+64.07%)</b></td><td>239.50 <b>(+25.52%)</b></td><td>172.68 (+2.52%)</td><td>168.80 (-2.03%)</td><td>131.20 (-4.09%)</td><td>43.61 <b>(+93.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>168.44 (n/a)</td><td>172.30 (n/a)</td><td>136.80 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (+3.22%)</td><td>0.10 (+7.50%)</td><td>0.11 <b>(+22.12%)</b></td><td>0.08 (+5.39%)</td><td>0.01 (-8.67%)</td><td>208.80 (-5.09%)</td><td>174.94 (-7.33%)</td><td>162.70 (-18.12%)</td><td>152.10 (-3.06%)</td><td>24.16 (-14.04%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>188.78 (n/a)</td><td>198.70 (n/a)</td><td>156.90 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (-2.64%)</td><td>0.10 (-2.53%)</td><td>0.09 (-11.64%)</td><td>0.08 <b>(+30.78%)</b></td><td>0.02 <b>(-24.70%)</b></td><td>206.40 <b>(-23.56%)</b></td><td>173.52 (-0.95%)</td><td>177.80 (+13.18%)</td><td>132.50 (+2.71%)</td><td>30.89 <b>(-43.86%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>270.00 (n/a)</td><td>175.18 (n/a)</td><td>157.10 (n/a)</td><td>129.00 (n/a)</td><td>55.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (-4.53%)</td><td>0.08 (-17.07%)</td><td>0.09 (-13.20%)</td><td>0.05 <b>(-45.88%)</b></td><td>0.02 <b>(+113.93%)</b></td><td>356.60 <b>(+84.77%)</b></td><td>224.36 <b>(+28.99%)</b></td><td>201.10 (+15.24%)</td><td>156.10 (+4.69%)</td><td>77.53 <b>(+336.63%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>173.94 (n/a)</td><td>174.50 (n/a)</td><td>149.10 (n/a)</td><td>17.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 <b>(+26.49%)</b></td><td>0.08 (+14.05%)</td><td>0.08 (+4.40%)</td><td>0.05 (+0.14%)</td><td>0.02 <b>(+41.30%)</b></td><td>337.80 (-0.12%)</td><td>215.94 (-9.82%)</td><td>194.00 (-4.24%)</td><td>152.40 <b>(-20.91%)</b></td><td>72.91 (+17.00%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>338.20 (n/a)</td><td>239.46 (n/a)</td><td>202.60 (n/a)</td><td>192.70 (n/a)</td><td>62.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (+13.03%)</td><td>0.21 (+13.10%)</td><td>0.22 <b>(+26.72%)</b></td><td>0.15 (+0.54%)</td><td>0.05 <b>(+28.66%)</b></td><td>225.00 (-0.53%)</td><td>160.88 (-10.24%)</td><td>150.80 <b>(-21.09%)</b></td><td>125.80 (-11.53%)</td><td>41.51 (+15.36%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.20 (n/a)</td><td>179.24 (n/a)</td><td>191.10 (n/a)</td><td>142.20 (n/a)</td><td>35.99 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (+13.92%)</td><td>0.25 <b>(+32.37%)</b></td><td>0.25 <b>(+37.81%)</b></td><td>0.21 <b>(+38.61%)</b></td><td>0.03 (-8.30%)</td><td>156.20 <b>(-27.89%)</b></td><td>134.80 <b>(-25.36%)</b></td><td>133.30 <b>(-27.44%)</b></td><td>115.60 (-12.22%)</td><td>18.55 <b>(-39.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.60 (n/a)</td><td>180.60 (n/a)</td><td>183.70 (n/a)</td><td>131.70 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (-12.68%)</td><td>0.23 (-3.93%)</td><td>0.24 (-2.09%)</td><td>0.17 (-0.87%)</td><td>0.04 <b>(-37.76%)</b></td><td>242.60 (+0.87%)</td><td>184.92 (+0.99%)</td><td>173.90 (+2.11%)</td><td>152.60 (+14.48%)</td><td>34.97 <b>(-27.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>240.50 (n/a)</td><td>183.10 (n/a)</td><td>170.30 (n/a)</td><td>133.30 (n/a)</td><td>48.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-5.96%)</td><td>0.19 (-11.44%)</td><td>0.19 (-12.72%)</td><td>0.12 <b>(-29.03%)</b></td><td>0.04 <b>(+35.82%)</b></td><td>276.00 <b>(+40.89%)</b></td><td>185.32 (+16.86%)</td><td>170.20 (+14.54%)</td><td>144.20 (+6.34%)</td><td>53.38 <b>(+108.51%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.90 (n/a)</td><td>158.58 (n/a)</td><td>148.60 (n/a)</td><td>135.60 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (-18.66%)</td><td>0.24 (-8.20%)</td><td>0.21 (-8.56%)</td><td>0.20 (+3.22%)</td><td>0.04 <b>(-45.06%)</b></td><td>207.80 (-3.12%)</td><td>177.34 (+4.97%)</td><td>191.00 (+9.39%)</td><td>145.00 <b>(+22.99%)</b></td><td>27.91 <b>(-36.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>214.50 (n/a)</td><td>168.94 (n/a)</td><td>174.60 (n/a)</td><td>117.90 (n/a)</td><td>43.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (+5.42%)</td><td>0.21 (+4.13%)</td><td>0.22 (+13.33%)</td><td>0.16 (+0.31%)</td><td>0.04 <b>(+23.65%)</b></td><td>204.80 (-0.29%)</td><td>163.88 (-2.98%)</td><td>149.10 (-11.78%)</td><td>130.30 (-5.17%)</td><td>33.05 <b>(+20.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.40 (n/a)</td><td>168.92 (n/a)</td><td>169.00 (n/a)</td><td>137.40 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-18.23%)</td><td>0.21 (-5.67%)</td><td>0.21 (+9.64%)</td><td>0.19 (+3.81%)</td><td>0.01 <b>(-68.83%)</b></td><td>192.40 (-3.66%)</td><td>175.60 (+3.00%)</td><td>172.30 (-8.79%)</td><td>162.30 <b>(+22.31%)</b></td><td>12.26 <b>(-62.80%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>199.70 (n/a)</td><td>170.48 (n/a)</td><td>188.90 (n/a)</td><td>132.70 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (+3.84%)</td><td>0.21 (+5.93%)</td><td>0.22 (+8.44%)</td><td>0.18 (+0.24%)</td><td>0.02 <b>(+29.70%)</b></td><td>185.50 (-0.22%)</td><td>157.54 (-5.28%)</td><td>148.70 (-7.75%)</td><td>144.10 (-3.68%)</td><td>17.45 <b>(+23.67%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>166.32 (n/a)</td><td>161.20 (n/a)</td><td>149.60 (n/a)</td><td>14.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.36 <b>(+51.15%)</b></td><td>0.25 (+14.13%)</td><td>0.25 (+9.26%)</td><td>0.15 (-17.74%)</td><td>0.08 <b>(+230.76%)</b></td><td>252.30 <b>(+21.59%)</b></td><td>164.50 (-5.01%)</td><td>149.70 (-8.50%)</td><td>101.30 <b>(-33.83%)</b></td><td>57.21 <b>(+166.48%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>207.50 (n/a)</td><td>173.18 (n/a)</td><td>163.60 (n/a)</td><td>153.10 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (-1.88%)</td><td>0.19 (+6.51%)</td><td>0.20 (+2.75%)</td><td>0.17 (+17.49%)</td><td>0.01 <b>(-55.61%)</b></td><td>187.80 (-14.91%)</td><td>170.60 (-7.57%)</td><td>166.70 (-2.69%)</td><td>158.70 (+1.93%)</td><td>11.04 <b>(-61.68%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.70 (n/a)</td><td>184.58 (n/a)</td><td>171.30 (n/a)</td><td>155.70 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-14.68%)</td><td>0.20 (+3.33%)</td><td>0.20 (+10.48%)</td><td>0.19 (+16.31%)</td><td>0.02 <b>(-59.89%)</b></td><td>188.00 (-14.04%)</td><td>174.22 (-5.76%)</td><td>171.50 (-9.50%)</td><td>154.20 (+17.17%)</td><td>14.18 <b>(-58.24%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>218.70 (n/a)</td><td>184.86 (n/a)</td><td>189.50 (n/a)</td><td>131.60 (n/a)</td><td>33.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 <b>(+37.84%)</b></td><td>0.22 <b>(+26.88%)</b></td><td>0.21 (+19.91%)</td><td>0.18 <b>(+42.37%)</b></td><td>0.04 <b>(+34.37%)</b></td><td>182.10 <b>(-29.75%)</b></td><td>154.28 <b>(-21.44%)</b></td><td>156.60 (-16.57%)</td><td>117.60 <b>(-27.45%)</b></td><td>23.61 <b>(-36.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>259.20 (n/a)</td><td>196.38 (n/a)</td><td>187.70 (n/a)</td><td>162.10 (n/a)</td><td>36.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (-11.26%)</td><td>0.18 (-8.95%)</td><td>0.18 (-15.24%)</td><td>0.15 (+10.03%)</td><td>0.02 <b>(-53.42%)</b></td><td>225.30 (-9.12%)</td><td>198.34 (+7.47%)</td><td>198.10 (+17.99%)</td><td>176.10 (+12.67%)</td><td>17.71 <b>(-52.70%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>247.90 (n/a)</td><td>184.56 (n/a)</td><td>167.90 (n/a)</td><td>156.30 (n/a)</td><td>37.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.24 (-3.51%)</td><td>0.18 (+3.23%)</td><td>0.19 <b>(+21.11%)</b></td><td>0.12 (-17.58%)</td><td>0.05 (+11.49%)</td><td>265.10 <b>(+21.33%)</b></td><td>193.26 (-1.11%)</td><td>172.70 (-17.45%)</td><td>137.40 (+3.62%)</td><td>52.01 <b>(+46.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.50 (n/a)</td><td>195.42 (n/a)</td><td>209.20 (n/a)</td><td>132.60 (n/a)</td><td>35.41 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (+2.03%)</td><td>0.14 (+8.84%)</td><td>0.15 (+15.40%)</td><td>0.11 (+5.14%)</td><td>0.02 <b>(-20.59%)</b></td><td>184.80 (-4.89%)</td><td>148.34 (-9.21%)</td><td>140.80 (-13.35%)</td><td>125.40 (-2.03%)</td><td>22.50 <b>(-26.12%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>194.30 (n/a)</td><td>163.38 (n/a)</td><td>162.50 (n/a)</td><td>128.00 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 <b>(+46.34%)</b></td><td>0.14 <b>(+36.75%)</b></td><td>0.13 <b>(+34.34%)</b></td><td>0.13 <b>(+37.84%)</b></td><td>0.02 <b>(+93.33%)</b></td><td>163.60 <b>(-27.45%)</b></td><td>152.30 <b>(-26.48%)</b></td><td>158.80 <b>(-25.59%)</b></td><td>122.00 <b>(-31.69%)</b></td><td>17.10 (-4.48%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>207.16 (n/a)</td><td>213.40 (n/a)</td><td>178.60 (n/a)</td><td>17.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (+12.54%)</td><td>0.12 (+4.95%)</td><td>0.11 (-8.38%)</td><td>0.09 (+6.22%)</td><td>0.03 <b>(+22.76%)</b></td><td>223.00 (-5.83%)</td><td>179.84 (-4.11%)</td><td>189.10 (+9.18%)</td><td>132.80 (-11.11%)</td><td>35.84 (+0.38%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>236.80 (n/a)</td><td>187.54 (n/a)</td><td>173.20 (n/a)</td><td>149.40 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (-2.50%)</td><td>0.10 (-15.07%)</td><td>0.10 (-14.38%)</td><td>0.05 <b>(-44.34%)</b></td><td>0.03 <b>(+71.21%)</b></td><td>386.40 <b>(+79.64%)</b></td><td>220.52 <b>(+29.49%)</b></td><td>197.40 (+16.80%)</td><td>139.30 (+2.50%)</td><td>96.74 <b>(+231.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>170.30 (n/a)</td><td>169.00 (n/a)</td><td>135.90 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (+10.94%)</td><td>0.13 (+4.19%)</td><td>0.13 (+14.94%)</td><td>0.09 (-10.39%)</td><td>0.02 <b>(+75.71%)</b></td><td>216.20 (+11.62%)</td><td>167.70 (-2.36%)</td><td>153.10 (-12.96%)</td><td>139.10 (-9.91%)</td><td>31.07 <b>(+82.84%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>171.76 (n/a)</td><td>175.90 (n/a)</td><td>154.40 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 <b>(+23.03%)</b></td><td>0.12 (+4.11%)</td><td>0.12 (-0.99%)</td><td>0.10 (+7.06%)</td><td>0.03 <b>(+51.08%)</b></td><td>214.30 (-6.58%)</td><td>173.44 (-2.46%)</td><td>172.60 (+0.99%)</td><td>122.20 (-18.75%)</td><td>35.73 (+13.07%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>229.40 (n/a)</td><td>177.82 (n/a)</td><td>170.90 (n/a)</td><td>150.40 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (-8.65%)</td><td>0.10 (-13.90%)</td><td>0.12 (-3.30%)</td><td>0.06 <b>(-20.98%)</b></td><td>0.04 (+19.01%)</td><td>318.50 <b>(+26.54%)</b></td><td>223.44 <b>(+23.26%)</b></td><td>173.10 (+3.47%)</td><td>138.30 (+9.50%)</td><td>86.09 <b>(+76.90%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>251.70 (n/a)</td><td>181.28 (n/a)</td><td>167.30 (n/a)</td><td>126.30 (n/a)</td><td>48.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (-8.27%)</td><td>0.12 (+6.33%)</td><td>0.13 <b>(+25.63%)</b></td><td>0.09 (-4.31%)</td><td>0.02 (-15.22%)</td><td>230.00 (+4.50%)</td><td>179.32 (-6.47%)</td><td>161.50 <b>(-20.36%)</b></td><td>151.00 (+9.03%)</td><td>33.09 (-4.20%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>220.10 (n/a)</td><td>191.72 (n/a)</td><td>202.80 (n/a)</td><td>138.50 (n/a)</td><td>34.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.18 (+4.02%)</td><td>0.15 (+10.67%)</td><td>0.15 (+0.41%)</td><td>0.14 <b>(+81.01%)</b></td><td>0.02 <b>(-52.20%)</b></td><td>181.70 <b>(-44.76%)</b></td><td>163.64 (-16.50%)</td><td>165.40 (-0.36%)</td><td>134.10 (-3.87%)</td><td>17.86 <b>(-76.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>328.90 (n/a)</td><td>195.98 (n/a)</td><td>166.00 (n/a)</td><td>139.50 (n/a)</td><td>76.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (-12.18%)</td><td>0.14 (-3.09%)</td><td>0.14 (+0.74%)</td><td>0.12 (+3.13%)</td><td>0.01 <b>(-48.61%)</b></td><td>206.50 (-3.05%)</td><td>177.98 (+1.14%)</td><td>180.20 (-0.77%)</td><td>159.50 (+13.85%)</td><td>18.70 <b>(-42.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.00 (n/a)</td><td>175.98 (n/a)</td><td>181.60 (n/a)</td><td>140.10 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (-2.54%)</td><td>0.14 (-1.28%)</td><td>0.14 (+1.11%)</td><td>0.11 (+0.21%)</td><td>0.02 <b>(-25.52%)</b></td><td>214.80 (-0.19%)</td><td>173.62 (+0.08%)</td><td>170.30 (-1.10%)</td><td>143.60 (+2.64%)</td><td>26.27 <b>(-20.90%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>215.20 (n/a)</td><td>173.48 (n/a)</td><td>172.20 (n/a)</td><td>139.90 (n/a)</td><td>33.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (-4.96%)</td><td>0.13 (-10.12%)</td><td>0.12 (-14.65%)</td><td>0.11 (-17.20%)</td><td>0.01 <b>(+117.30%)</b></td><td>214.40 <b>(+20.79%)</b></td><td>190.58 (+12.16%)</td><td>198.30 (+17.20%)</td><td>167.60 (+5.28%)</td><td>20.56 <b>(+169.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>169.92 (n/a)</td><td>169.20 (n/a)</td><td>159.20 (n/a)</td><td>7.64 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (-10.87%)</td><td>0.15 (+6.70%)</td><td>0.15 (+19.82%)</td><td>0.13 <b>(+20.07%)</b></td><td>0.02 <b>(-53.35%)</b></td><td>190.80 (-16.72%)</td><td>167.38 (-9.50%)</td><td>159.90 (-16.54%)</td><td>147.40 (+12.26%)</td><td>18.20 <b>(-56.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>229.10 (n/a)</td><td>184.96 (n/a)</td><td>191.60 (n/a)</td><td>131.30 (n/a)</td><td>41.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (-5.41%)</td><td>0.13 (-10.05%)</td><td>0.14 (+1.41%)</td><td>0.07 <b>(-44.99%)</b></td><td>0.04 <b>(+87.97%)</b></td><td>363.40 <b>(+81.79%)</b></td><td>212.08 <b>(+20.62%)</b></td><td>180.10 (-1.37%)</td><td>149.90 (+5.71%)</td><td>86.25 <b>(+295.34%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>199.90 (n/a)</td><td>175.82 (n/a)</td><td>182.60 (n/a)</td><td>141.80 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 <b>(-20.14%)</b></td><td>0.13 (-4.59%)</td><td>0.13 (+5.95%)</td><td>0.10 (-2.24%)</td><td>0.02 <b>(-50.34%)</b></td><td>235.90 (+2.30%)</td><td>197.54 (+1.56%)</td><td>196.40 (-5.58%)</td><td>161.10 <b>(+25.27%)</b></td><td>26.77 <b>(-36.58%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>230.60 (n/a)</td><td>194.50 (n/a)</td><td>208.00 (n/a)</td><td>128.60 (n/a)</td><td>42.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 <b>(-23.49%)</b></td><td>0.14 (-6.70%)</td><td>0.15 (-3.25%)</td><td>0.11 (+7.32%)</td><td>0.02 <b>(-52.43%)</b></td><td>219.60 (-6.83%)</td><td>179.72 (+2.80%)</td><td>168.70 (+3.37%)</td><td>151.50 <b>(+30.72%)</b></td><td>26.90 <b>(-41.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>235.70 (n/a)</td><td>174.82 (n/a)</td><td>163.20 (n/a)</td><td>115.90 (n/a)</td><td>46.06 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (+18.39%)</td><td>0.13 (+7.67%)</td><td>0.12 (-0.93%)</td><td>0.11 (+3.38%)</td><td>0.02 <b>(+93.45%)</b></td><td>168.40 (-3.27%)</td><td>145.58 (-5.76%)</td><td>154.60 (+0.91%)</td><td>115.20 (-15.54%)</td><td>23.07 <b>(+57.96%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>154.48 (n/a)</td><td>153.20 (n/a)</td><td>136.40 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 <b>(+32.68%)</b></td><td>0.12 <b>(+32.49%)</b></td><td>0.12 <b>(+36.69%)</b></td><td>0.09 <b>(+29.38%)</b></td><td>0.02 <b>(+22.12%)</b></td><td>197.00 <b>(-22.71%)</b></td><td>159.14 <b>(-24.71%)</b></td><td>159.70 <b>(-26.84%)</b></td><td>129.40 <b>(-24.64%)</b></td><td>24.74 <b>(-27.23%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>254.90 (n/a)</td><td>211.38 (n/a)</td><td>218.30 (n/a)</td><td>171.70 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (-3.43%)</td><td>0.10 (+3.05%)</td><td>0.10 (+3.39%)</td><td>0.08 (+4.47%)</td><td>0.02 <b>(-26.47%)</b></td><td>238.20 (-4.26%)</td><td>182.84 (-5.77%)</td><td>184.60 (-3.30%)</td><td>136.40 (+3.49%)</td><td>36.82 <b>(-29.38%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>248.80 (n/a)</td><td>194.04 (n/a)</td><td>190.90 (n/a)</td><td>131.80 (n/a)</td><td>52.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (+13.34%)</td><td>0.11 (+10.14%)</td><td>0.10 (+18.90%)</td><td>0.09 <b>(+41.27%)</b></td><td>0.03 (-13.49%)</td><td>207.80 <b>(-29.20%)</b></td><td>173.00 (-13.01%)</td><td>176.70 (-15.90%)</td><td>116.70 (-11.79%)</td><td>34.37 <b>(-46.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>293.50 (n/a)</td><td>198.88 (n/a)</td><td>210.10 (n/a)</td><td>132.30 (n/a)</td><td>64.37 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (-10.74%)</td><td>0.11 (+1.12%)</td><td>0.11 (+6.35%)</td><td>0.08 (-9.94%)</td><td>0.02 (-15.63%)</td><td>241.70 (+11.02%)</td><td>178.06 (-1.29%)</td><td>170.70 (-5.95%)</td><td>142.00 (+11.99%)</td><td>38.06 (+12.52%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.70 (n/a)</td><td>180.38 (n/a)</td><td>181.50 (n/a)</td><td>126.80 (n/a)</td><td>33.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 <b>(+29.48%)</b></td><td>0.13 <b>(+28.97%)</b></td><td>0.13 <b>(+34.75%)</b></td><td>0.09 (+11.61%)</td><td>0.03 <b>(+98.30%)</b></td><td>212.70 (-10.40%)</td><td>154.20 <b>(-20.26%)</b></td><td>140.20 <b>(-25.78%)</b></td><td>121.40 <b>(-22.77%)</b></td><td>38.53 <b>(+34.12%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>193.38 (n/a)</td><td>188.90 (n/a)</td><td>157.20 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 <b>(-21.84%)</b></td><td>0.07 <b>(-25.12%)</b></td><td>0.07 <b>(-29.56%)</b></td><td>0.06 <b>(-30.26%)</b></td><td>0.01 (+14.81%)</td><td>301.10 <b>(+43.38%)</b></td><td>254.68 <b>(+35.11%)</b></td><td>258.80 <b>(+41.96%)</b></td><td>209.80 <b>(+27.93%)</b></td><td>40.29 <b>(+104.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>188.50 (n/a)</td><td>182.30 (n/a)</td><td>164.00 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (-17.06%)</td><td>0.10 (-8.32%)</td><td>0.10 (-3.12%)</td><td>0.08 (-2.71%)</td><td>0.01 <b>(-35.58%)</b></td><td>232.90 (+2.78%)</td><td>192.00 (+7.71%)</td><td>182.00 (+3.23%)</td><td>162.90 <b>(+20.58%)</b></td><td>26.48 (-18.68%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>226.60 (n/a)</td><td>178.26 (n/a)</td><td>176.30 (n/a)</td><td>135.10 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.73 (-2.41%)</td><td>0.57 (+5.18%)</td><td>0.50 (-0.95%)</td><td>0.41 (-8.67%)</td><td>0.14 (+18.94%)</td><td>239.20 (+9.47%)</td><td>182.34 (-3.20%)</td><td>196.30 (+0.98%)</td><td>134.40 (+2.44%)</td><td>44.68 <b>(+32.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.75 (n/a)</td><td>0.54 (n/a)</td><td>0.51 (n/a)</td><td>0.45 (n/a)</td><td>0.12 (n/a)</td><td>218.50 (n/a)</td><td>188.36 (n/a)</td><td>194.40 (n/a)</td><td>131.20 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.62 (+6.66%)</td><td>0.51 (-9.20%)</td><td>0.52 (-7.28%)</td><td>0.40 <b>(-24.28%)</b></td><td>0.09 <b>(+416.56%)</b></td><td>243.60 <b>(+32.10%)</b></td><td>197.94 (+12.82%)</td><td>188.40 (+7.84%)</td><td>159.30 (-6.24%)</td><td>35.29 <b>(+545.43%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.58 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.02 (n/a)</td><td>184.40 (n/a)</td><td>175.44 (n/a)</td><td>174.70 (n/a)</td><td>169.90 (n/a)</td><td>5.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.64 (-0.25%)</td><td>0.54 (-3.09%)</td><td>0.53 (-1.30%)</td><td>0.45 (-12.88%)</td><td>0.07 <b>(+48.00%)</b></td><td>218.00 (+14.74%)</td><td>183.46 (+4.14%)</td><td>184.00 (+1.32%)</td><td>152.50 (+0.26%)</td><td>25.26 <b>(+72.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.65 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.05 (n/a)</td><td>190.00 (n/a)</td><td>176.16 (n/a)</td><td>181.60 (n/a)</td><td>152.10 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.61 (-2.01%)</td><td>0.53 (+3.26%)</td><td>0.52 (+3.93%)</td><td>0.42 (-4.07%)</td><td>0.07 (+12.91%)</td><td>233.60 (+4.24%)</td><td>188.22 (-2.72%)</td><td>188.70 (-3.82%)</td><td>162.30 (+2.08%)</td><td>28.48 <b>(+21.56%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.62 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.07 (n/a)</td><td>224.10 (n/a)</td><td>193.48 (n/a)</td><td>196.20 (n/a)</td><td>159.00 (n/a)</td><td>23.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.51 (+12.70%)</td><td>0.46 (+18.92%)</td><td>0.50 <b>(+27.80%)</b></td><td>0.33 (+1.71%)</td><td>0.08 <b>(+46.18%)</b></td><td>223.30 (-1.67%)</td><td>166.42 (-14.87%)</td><td>147.60 <b>(-21.78%)</b></td><td>144.60 (-11.23%)</td><td>33.35 <b>(+26.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>227.10 (n/a)</td><td>195.48 (n/a)</td><td>188.70 (n/a)</td><td>162.90 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.51 <b>(+22.79%)</b></td><td>0.42 (+11.27%)</td><td>0.41 (+2.90%)</td><td>0.36 (+15.19%)</td><td>0.06 <b>(+30.75%)</b></td><td>207.10 (-13.17%)</td><td>177.66 (-9.95%)</td><td>178.30 (-2.83%)</td><td>143.20 (-18.54%)</td><td>23.05 (-9.83%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.04 (n/a)</td><td>238.50 (n/a)</td><td>197.28 (n/a)</td><td>183.50 (n/a)</td><td>175.80 (n/a)</td><td>25.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.50 (+6.57%)</td><td>0.45 (+16.08%)</td><td>0.46 <b>(+22.08%)</b></td><td>0.37 <b>(+20.29%)</b></td><td>0.05 (-17.70%)</td><td>201.90 (-16.88%)</td><td>165.16 (-14.75%)</td><td>159.40 (-18.09%)</td><td>148.60 (-6.19%)</td><td>21.72 <b>(-34.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.06 (n/a)</td><td>242.90 (n/a)</td><td>193.74 (n/a)</td><td>194.60 (n/a)</td><td>158.40 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.47 (+13.67%)</td><td>0.35 (-3.32%)</td><td>0.30 (-15.85%)</td><td>0.29 (-15.08%)</td><td>0.08 <b>(+156.93%)</b></td><td>257.90 (+17.76%)</td><td>217.42 (+7.23%)</td><td>244.50 (+18.86%)</td><td>156.90 (-12.00%)</td><td>47.06 <b>(+166.86%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.03 (n/a)</td><td>219.00 (n/a)</td><td>202.76 (n/a)</td><td>205.70 (n/a)</td><td>178.30 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.24 (-10.38%)</td><td>0.21 (+8.43%)</td><td>0.20 (+8.21%)</td><td>0.18 <b>(+21.35%)</b></td><td>0.02 <b>(-55.55%)</b></td><td>203.60 (-17.60%)</td><td>179.66 (-10.91%)</td><td>181.30 (-7.55%)</td><td>154.90 (+11.60%)</td><td>17.59 <b>(-59.71%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>247.10 (n/a)</td><td>201.66 (n/a)</td><td>196.10 (n/a)</td><td>138.80 (n/a)</td><td>43.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 <b>(+23.79%)</b></td><td>0.22 (+2.77%)</td><td>0.21 (+0.58%)</td><td>0.16 (-17.69%)</td><td>0.05 <b>(+258.18%)</b></td><td>232.40 <b>(+21.48%)</b></td><td>177.42 (+0.60%)</td><td>177.30 (-0.56%)</td><td>132.90 (-19.21%)</td><td>37.98 <b>(+252.82%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>176.36 (n/a)</td><td>178.30 (n/a)</td><td>164.50 (n/a)</td><td>10.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 <b>(+26.11%)</b></td><td>0.21 (+11.33%)</td><td>0.21 (+10.26%)</td><td>0.15 (-16.59%)</td><td>0.04 <b>(+240.21%)</b></td><td>250.60 (+19.85%)</td><td>180.88 (-7.14%)</td><td>175.00 (-9.33%)</td><td>141.20 <b>(-20.72%)</b></td><td>41.74 <b>(+232.31%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>194.78 (n/a)</td><td>193.00 (n/a)</td><td>178.10 (n/a)</td><td>12.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (+9.41%)</td><td>0.22 (+1.50%)</td><td>0.20 (+1.77%)</td><td>0.19 (+8.73%)</td><td>0.04 (+0.02%)</td><td>197.60 (-8.01%)</td><td>171.70 (-1.93%)</td><td>185.30 (-1.75%)</td><td>125.00 (-8.63%)</td><td>29.22 (-14.46%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>214.80 (n/a)</td><td>175.08 (n/a)</td><td>188.60 (n/a)</td><td>136.80 (n/a)</td><td>34.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (-7.49%)</td><td>0.22 (+1.15%)</td><td>0.21 (-2.77%)</td><td>0.16 (+7.83%)</td><td>0.04 <b>(-21.03%)</b></td><td>225.20 (-7.25%)</td><td>173.54 (-2.85%)</td><td>174.60 (+2.83%)</td><td>141.30 (+8.11%)</td><td>33.92 <b>(-22.71%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>242.80 (n/a)</td><td>178.64 (n/a)</td><td>169.80 (n/a)</td><td>130.70 (n/a)</td><td>43.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-2.85%)</td><td>0.19 (-4.71%)</td><td>0.18 (-4.80%)</td><td>0.18 (+2.40%)</td><td>0.02 <b>(-24.78%)</b></td><td>208.50 (-2.34%)</td><td>191.64 (+4.34%)</td><td>200.00 (+5.04%)</td><td>162.70 (+2.97%)</td><td>18.26 <b>(-23.31%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>213.50 (n/a)</td><td>183.66 (n/a)</td><td>190.40 (n/a)</td><td>158.00 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-0.31%)</td><td>0.20 (-0.01%)</td><td>0.19 (-10.54%)</td><td>0.18 (+12.48%)</td><td>0.02 <b>(-29.82%)</b></td><td>203.00 (-11.08%)</td><td>187.08 (-1.20%)</td><td>199.00 (+11.73%)</td><td>160.70 (+0.31%)</td><td>20.21 <b>(-36.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>228.30 (n/a)</td><td>189.36 (n/a)</td><td>178.10 (n/a)</td><td>160.20 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (+7.19%)</td><td>0.22 (+2.56%)</td><td>0.21 (+15.44%)</td><td>0.18 (+5.47%)</td><td>0.04 (-6.14%)</td><td>200.60 (-5.20%)</td><td>173.06 (-3.18%)</td><td>171.80 (-13.36%)</td><td>129.20 (-6.71%)</td><td>27.88 (-17.28%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>211.60 (n/a)</td><td>178.74 (n/a)</td><td>198.30 (n/a)</td><td>138.50 (n/a)</td><td>33.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.30 (+13.67%)</td><td>0.25 (+9.25%)</td><td>0.24 (+0.52%)</td><td>0.21 (+17.43%)</td><td>0.03 (-9.57%)</td><td>190.60 (-14.83%)</td><td>167.82 (-9.18%)</td><td>170.50 (-0.53%)</td><td>137.50 (-12.03%)</td><td>19.21 <b>(-34.27%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>223.80 (n/a)</td><td>184.78 (n/a)</td><td>171.40 (n/a)</td><td>156.30 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (+4.97%)</td><td>0.23 (+1.63%)</td><td>0.23 (+4.34%)</td><td>0.19 (-11.86%)</td><td>0.03 <b>(+95.86%)</b></td><td>218.50 (+13.45%)</td><td>180.20 (-0.73%)</td><td>177.90 (-4.15%)</td><td>160.80 (-4.74%)</td><td>22.83 <b>(+115.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>181.52 (n/a)</td><td>185.60 (n/a)</td><td>168.80 (n/a)</td><td>10.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 <b>(+27.42%)</b></td><td>0.27 <b>(+22.27%)</b></td><td>0.27 <b>(+22.55%)</b></td><td>0.23 (+10.94%)</td><td>0.02 <b>(+231.00%)</b></td><td>176.70 (-9.85%)</td><td>153.04 (-17.72%)</td><td>151.00 (-18.42%)</td><td>139.90 <b>(-21.54%)</b></td><td>14.85 <b>(+133.30%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>186.00 (n/a)</td><td>185.10 (n/a)</td><td>178.30 (n/a)</td><td>6.37 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.38 <b>(+58.22%)</b></td><td>0.27 <b>(+28.93%)</b></td><td>0.24 (+12.00%)</td><td>0.23 <b>(+22.41%)</b></td><td>0.06 <b>(+234.51%)</b></td><td>176.00 (-18.29%)</td><td>156.66 <b>(-20.22%)</b></td><td>173.10 (-10.68%)</td><td>108.80 <b>(-36.82%)</b></td><td>28.99 <b>(+74.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>215.40 (n/a)</td><td>196.36 (n/a)</td><td>193.80 (n/a)</td><td>172.20 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (+4.81%)</td><td>0.21 (-2.34%)</td><td>0.21 (-9.26%)</td><td>0.18 (-4.04%)</td><td>0.03 <b>(+30.23%)</b></td><td>225.60 (+4.20%)</td><td>195.62 (+2.97%)</td><td>198.80 (+10.20%)</td><td>165.30 (-4.56%)</td><td>25.42 <b>(+29.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>189.98 (n/a)</td><td>180.40 (n/a)</td><td>173.20 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (-7.76%)</td><td>0.21 (-14.08%)</td><td>0.21 (-13.92%)</td><td>0.15 <b>(-27.27%)</b></td><td>0.05 (+16.64%)</td><td>270.50 <b>(+37.52%)</b></td><td>201.14 (+18.78%)</td><td>199.00 (+16.17%)</td><td>142.10 (+8.39%)</td><td>45.72 <b>(+72.85%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>196.70 (n/a)</td><td>169.34 (n/a)</td><td>171.30 (n/a)</td><td>131.10 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (-10.03%)</td><td>0.20 (+8.31%)</td><td>0.21 <b>(+26.71%)</b></td><td>0.14 (-2.89%)</td><td>0.04 <b>(-21.18%)</b></td><td>290.40 (+2.98%)</td><td>208.98 (-8.73%)</td><td>193.30 <b>(-21.07%)</b></td><td>162.90 (+11.19%)</td><td>49.53 (-2.80%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>282.00 (n/a)</td><td>228.98 (n/a)</td><td>244.90 (n/a)</td><td>146.50 (n/a)</td><td>50.96 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (-14.95%)</td><td>0.24 (+2.15%)</td><td>0.23 (+7.67%)</td><td>0.20 (+19.25%)</td><td>0.04 <b>(-43.30%)</b></td><td>208.70 (-16.15%)</td><td>173.90 (-5.75%)</td><td>178.90 (-7.11%)</td><td>142.50 (+17.57%)</td><td>26.62 <b>(-43.48%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>248.90 (n/a)</td><td>184.50 (n/a)</td><td>192.60 (n/a)</td><td>121.20 (n/a)</td><td>47.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (+10.52%)</td><td>0.19 (+10.82%)</td><td>0.21 (+13.74%)</td><td>0.14 (-1.98%)</td><td>0.03 <b>(+40.61%)</b></td><td>254.40 (+2.00%)</td><td>184.68 (-8.47%)</td><td>165.50 (-12.11%)</td><td>157.20 (-9.50%)</td><td>40.44 <b>(+31.05%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>249.40 (n/a)</td><td>201.76 (n/a)</td><td>188.30 (n/a)</td><td>173.70 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (-0.04%)</td><td>0.20 (+3.26%)</td><td>0.20 (+10.39%)</td><td>0.16 (+1.39%)</td><td>0.04 (-4.61%)</td><td>221.80 (-1.38%)</td><td>176.72 (-3.41%)</td><td>172.50 (-9.45%)</td><td>132.90 (+0.08%)</td><td>32.40 (-4.18%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.90 (n/a)</td><td>182.96 (n/a)</td><td>190.50 (n/a)</td><td>132.80 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (+8.92%)</td><td>0.23 (+9.04%)</td><td>0.24 (+17.98%)</td><td>0.17 (+2.43%)</td><td>0.05 <b>(+58.46%)</b></td><td>203.60 (-2.35%)</td><td>159.84 (-6.16%)</td><td>144.40 (-15.26%)</td><td>126.60 (-8.19%)</td><td>37.04 <b>(+42.76%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>208.50 (n/a)</td><td>170.34 (n/a)</td><td>170.40 (n/a)</td><td>137.90 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (-13.83%)</td><td>0.20 (-3.25%)</td><td>0.21 (+7.56%)</td><td>0.16 (-11.68%)</td><td>0.03 (-17.19%)</td><td>224.00 (+13.25%)</td><td>180.38 (+3.16%)</td><td>166.10 (-7.05%)</td><td>153.00 (+16.08%)</td><td>29.46 (+9.95%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>197.80 (n/a)</td><td>174.86 (n/a)</td><td>178.70 (n/a)</td><td>131.80 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 <b>(+21.70%)</b></td><td>0.21 (+3.10%)</td><td>0.21 (+2.99%)</td><td>0.16 (-16.10%)</td><td>0.04 <b>(+280.51%)</b></td><td>218.80 (+19.24%)</td><td>173.40 (-0.37%)</td><td>168.50 (-2.88%)</td><td>132.30 (-17.83%)</td><td>32.74 <b>(+274.71%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>183.50 (n/a)</td><td>174.04 (n/a)</td><td>173.50 (n/a)</td><td>161.00 (n/a)</td><td>8.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (-6.41%)</td><td>0.18 (-9.32%)</td><td>0.19 (-4.44%)</td><td>0.15 (-14.25%)</td><td>0.03 <b>(+37.31%)</b></td><td>225.70 (+16.64%)</td><td>192.16 (+11.53%)</td><td>181.30 (+4.62%)</td><td>157.20 (+6.79%)</td><td>29.77 <b>(+78.58%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>172.30 (n/a)</td><td>173.30 (n/a)</td><td>147.20 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (-2.61%)</td><td>0.19 (+4.27%)</td><td>0.19 (+3.51%)</td><td>0.18 (+12.78%)</td><td>0.02 <b>(-33.79%)</b></td><td>198.80 (-11.33%)</td><td>180.12 (-5.20%)</td><td>186.30 (-3.37%)</td><td>157.20 (+2.68%)</td><td>17.42 <b>(-39.80%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>224.20 (n/a)</td><td>190.00 (n/a)</td><td>192.80 (n/a)</td><td>153.10 (n/a)</td><td>28.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (+9.88%)</td><td>0.19 <b>(+22.56%)</b></td><td>0.19 <b>(+33.33%)</b></td><td>0.16 <b>(+43.19%)</b></td><td>0.03 <b>(-26.53%)</b></td><td>222.90 <b>(-30.15%)</b></td><td>190.70 <b>(-20.61%)</b></td><td>183.80 <b>(-24.98%)</b></td><td>163.60 (-8.96%)</td><td>26.87 <b>(-52.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>319.10 (n/a)</td><td>240.22 (n/a)</td><td>245.00 (n/a)</td><td>179.70 (n/a)</td><td>56.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.93 (+5.20%)</td><td>0.68 (-15.07%)</td><td>0.65 (-19.13%)</td><td>0.48 <b>(-34.89%)</b></td><td>0.16 <b>(+141.67%)</b></td><td>274.50 <b>(+53.61%)</b></td><td>200.64 <b>(+22.45%)</b></td><td>200.90 <b>(+23.63%)</b></td><td>141.50 (-4.97%)</td><td>47.99 <b>(+252.86%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.73 (n/a)</td><td>0.07 (n/a)</td><td>178.70 (n/a)</td><td>163.86 (n/a)</td><td>162.50 (n/a)</td><td>148.90 (n/a)</td><td>13.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.94 (-8.45%)</td><td>0.78 (-5.64%)</td><td>0.77 (-8.05%)</td><td>0.68 (+14.49%)</td><td>0.10 <b>(-43.80%)</b></td><td>192.30 (-12.63%)</td><td>170.28 (+2.99%)</td><td>170.20 (+8.75%)</td><td>138.80 (+9.21%)</td><td>20.50 <b>(-46.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.03 (n/a)</td><td>0.83 (n/a)</td><td>0.84 (n/a)</td><td>0.60 (n/a)</td><td>0.18 (n/a)</td><td>220.10 (n/a)</td><td>165.34 (n/a)</td><td>156.50 (n/a)</td><td>127.10 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.08 (+8.10%)</td><td>0.87 (+4.78%)</td><td>0.87 (+2.28%)</td><td>0.65 (-0.54%)</td><td>0.19 <b>(+53.34%)</b></td><td>202.10 (+0.55%)</td><td>156.74 (-2.48%)</td><td>150.30 (-2.28%)</td><td>120.90 (-7.50%)</td><td>35.85 <b>(+39.20%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.00 (n/a)</td><td>0.83 (n/a)</td><td>0.85 (n/a)</td><td>0.65 (n/a)</td><td>0.13 (n/a)</td><td>201.00 (n/a)</td><td>160.72 (n/a)</td><td>153.80 (n/a)</td><td>130.70 (n/a)</td><td>25.75 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.00 (+2.27%)</td><td>0.00 (-2.76%)</td><td>0.00 (-2.27%)</td><td>0.00 (-7.14%)</td><td>0.00 <b>(+154.95%)</b></td><td>1039.56 (+6.47%)</td><td>967.69 (+2.23%)</td><td>949.21 (+0.88%)</td><td>904.24 (-2.81%)</td><td>53.25 <b>(+203.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>976.40 (n/a)</td><td>946.58 (n/a)</td><td>940.94 (n/a)</td><td>930.36 (n/a)</td><td>17.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.01 (+1.23%)</td><td>0.01 (+2.04%)</td><td>0.01 (+2.53%)</td><td>0.01 (+0.00%)</td><td>0.00 (+14.95%)</td><td>1058.10 (-0.56%)</td><td>1020.57 (-1.84%)</td><td>1017.40 (-1.41%)</td><td>996.74 (-1.43%)</td><td>22.67 (+2.44%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1064.01 (n/a)</td><td>1039.70 (n/a)</td><td>1031.92 (n/a)</td><td>1011.24 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.95 (-1.26%)</td><td>0.93 (-1.12%)</td><td>0.93 (-1.18%)</td><td>0.91 (-0.94%)</td><td>0.01 (-15.33%)</td><td>2302.71 (+0.95%)</td><td>2259.06 (+1.12%)</td><td>2253.58 (+1.19%)</td><td>2210.16 (+1.28%)</td><td>35.28 (-13.63%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.92 (n/a)</td><td>0.02 (n/a)</td><td>2281.14 (n/a)</td><td>2234.02 (n/a)</td><td>2227.07 (n/a)</td><td>2182.25 (n/a)</td><td>40.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.89 (+3.07%)</td><td>4.87 (+5.31%)</td><td>4.83 (+3.14%)</td><td>3.58 (+13.22%)</td><td>0.95 (+1.35%)</td><td>292.70 (-11.65%)</td><td>222.36 (-5.63%)</td><td>216.90 (-3.04%)</td><td>178.10 (-3.00%)</td><td>46.58 (-17.65%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>5.71 (n/a)</td><td>4.63 (n/a)</td><td>4.69 (n/a)</td><td>3.16 (n/a)</td><td>0.94 (n/a)</td><td>331.30 (n/a)</td><td>235.62 (n/a)</td><td>223.70 (n/a)</td><td>183.60 (n/a)</td><td>56.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.02 (+17.21%)</td><td>4.93 (+11.00%)</td><td>4.89 (+4.66%)</td><td>4.23 (+15.39%)</td><td>0.67 (+9.41%)</td><td>248.10 (-13.34%)</td><td>215.78 (-10.11%)</td><td>214.40 (-4.46%)</td><td>174.20 (-14.65%)</td><td>27.03 <b>(-21.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>5.14 (n/a)</td><td>4.44 (n/a)</td><td>4.67 (n/a)</td><td>3.66 (n/a)</td><td>0.61 (n/a)</td><td>286.30 (n/a)</td><td>240.06 (n/a)</td><td>224.40 (n/a)</td><td>204.10 (n/a)</td><td>34.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.47 (+16.87%)</td><td>4.85 (+13.41%)</td><td>4.72 (+11.76%)</td><td>4.58 <b>(+23.43%)</b></td><td>0.35 (-6.62%)</td><td>229.00 (-19.00%)</td><td>216.84 (-12.06%)</td><td>222.10 (-10.52%)</td><td>191.90 (-14.41%)</td><td>14.62 <b>(-36.30%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.68 (n/a)</td><td>4.28 (n/a)</td><td>4.22 (n/a)</td><td>3.71 (n/a)</td><td>0.38 (n/a)</td><td>282.70 (n/a)</td><td>246.58 (n/a)</td><td>248.20 (n/a)</td><td>224.20 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.66 (+19.01%)</td><td>5.08 (+20.00%)</td><td>5.05 <b>(+21.43%)</b></td><td>4.08 (+8.61%)</td><td>0.64 <b>(+54.02%)</b></td><td>257.20 (-7.91%)</td><td>209.24 (-16.13%)</td><td>207.40 (-17.67%)</td><td>185.40 (-15.96%)</td><td>29.09 (+19.72%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.75 (n/a)</td><td>4.24 (n/a)</td><td>4.16 (n/a)</td><td>3.75 (n/a)</td><td>0.42 (n/a)</td><td>279.30 (n/a)</td><td>249.48 (n/a)</td><td>251.90 (n/a)</td><td>220.60 (n/a)</td><td>24.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.89 (-3.40%)</td><td>7.48 (-0.67%)</td><td>7.27 (-1.93%)</td><td>7.13 (+1.11%)</td><td>0.36 (-14.01%)</td><td>294.10 (-1.08%)</td><td>280.98 (+0.62%)</td><td>288.40 (+1.98%)</td><td>265.60 (+3.51%)</td><td>13.49 (-11.84%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>8.17 (n/a)</td><td>7.53 (n/a)</td><td>7.41 (n/a)</td><td>7.05 (n/a)</td><td>0.42 (n/a)</td><td>297.30 (n/a)</td><td>279.26 (n/a)</td><td>282.80 (n/a)</td><td>256.60 (n/a)</td><td>15.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.80 (+2.23%)</td><td>7.99 (+8.16%)</td><td>8.15 (+12.19%)</td><td>6.89 (+6.36%)</td><td>0.70 (-10.08%)</td><td>304.50 (-5.96%)</td><td>264.24 (-7.72%)</td><td>257.30 (-10.88%)</td><td>238.20 (-2.18%)</td><td>24.52 (-14.63%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>8.61 (n/a)</td><td>7.39 (n/a)</td><td>7.26 (n/a)</td><td>6.48 (n/a)</td><td>0.77 (n/a)</td><td>323.80 (n/a)</td><td>286.36 (n/a)</td><td>288.70 (n/a)</td><td>243.50 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.98 (+3.91%)</td><td>7.54 (-1.92%)</td><td>7.42 (-1.04%)</td><td>6.80 (+0.45%)</td><td>0.86 (+0.11%)</td><td>308.50 (-0.45%)</td><td>280.66 (+1.92%)</td><td>282.50 (+1.07%)</td><td>233.50 (-3.75%)</td><td>29.28 (-4.08%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>8.65 (n/a)</td><td>7.69 (n/a)</td><td>7.50 (n/a)</td><td>6.77 (n/a)</td><td>0.86 (n/a)</td><td>309.90 (n/a)</td><td>275.36 (n/a)</td><td>279.50 (n/a)</td><td>242.60 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>10.41 (+10.96%)</td><td>8.73 (+3.48%)</td><td>8.74 (+6.82%)</td><td>7.33 (-4.83%)</td><td>1.17 <b>(+71.09%)</b></td><td>286.20 (+5.10%)</td><td>243.54 (-2.47%)</td><td>240.00 (-6.40%)</td><td>201.40 (-9.89%)</td><td>32.23 <b>(+62.97%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.38 (n/a)</td><td>8.44 (n/a)</td><td>8.18 (n/a)</td><td>7.70 (n/a)</td><td>0.69 (n/a)</td><td>272.30 (n/a)</td><td>249.72 (n/a)</td><td>256.40 (n/a)</td><td>223.50 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.17 (-4.47%)</td><td>8.30 (+1.46%)</td><td>8.27 (-4.15%)</td><td>7.75 <b>(+28.47%)</b></td><td>0.54 <b>(-59.49%)</b></td><td>270.50 <b>(-22.16%)</b></td><td>253.66 (-3.57%)</td><td>253.70 (+4.32%)</td><td>228.80 (+4.67%)</td><td>15.98 <b>(-68.15%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.60 (n/a)</td><td>8.18 (n/a)</td><td>8.62 (n/a)</td><td>6.04 (n/a)</td><td>1.34 (n/a)</td><td>347.50 (n/a)</td><td>263.06 (n/a)</td><td>243.20 (n/a)</td><td>218.60 (n/a)</td><td>50.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.50 (+3.92%)</td><td>7.93 (-5.88%)</td><td>7.84 (-8.26%)</td><td>6.76 (-1.68%)</td><td>1.08 (+17.58%)</td><td>310.40 (+1.70%)</td><td>268.24 (+6.62%)</td><td>267.50 (+9.01%)</td><td>220.80 (-3.79%)</td><td>35.33 (+13.87%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.14 (n/a)</td><td>8.43 (n/a)</td><td>8.55 (n/a)</td><td>6.87 (n/a)</td><td>0.92 (n/a)</td><td>305.20 (n/a)</td><td>251.58 (n/a)</td><td>245.40 (n/a)</td><td>229.50 (n/a)</td><td>31.03 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>12.72 (-0.36%)</td><td>11.42 (-1.78%)</td><td>11.32 (-0.48%)</td><td>10.43 (-1.74%)</td><td>0.94 (-7.69%)</td><td>402.30 (+1.77%)</td><td>369.24 (+1.74%)</td><td>370.60 (+0.46%)</td><td>329.80 (+0.37%)</td><td>29.68 (-4.94%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>12.76 (n/a)</td><td>11.63 (n/a)</td><td>11.37 (n/a)</td><td>10.61 (n/a)</td><td>1.01 (n/a)</td><td>395.30 (n/a)</td><td>362.94 (n/a)</td><td>368.90 (n/a)</td><td>328.60 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.33 (-0.79%)</td><td>11.82 (+1.88%)</td><td>11.94 (+4.15%)</td><td>10.09 (+1.30%)</td><td>1.21 (-4.31%)</td><td>415.80 (-1.28%)</td><td>357.84 (-1.91%)</td><td>351.30 (-3.96%)</td><td>314.60 (+0.80%)</td><td>38.00 (-3.85%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.44 (n/a)</td><td>11.61 (n/a)</td><td>11.46 (n/a)</td><td>9.96 (n/a)</td><td>1.26 (n/a)</td><td>421.20 (n/a)</td><td>364.82 (n/a)</td><td>365.80 (n/a)</td><td>312.10 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.12 (+0.19%)</td><td>12.22 (+2.33%)</td><td>11.87 (+2.44%)</td><td>11.39 (+1.79%)</td><td>0.81 (-4.68%)</td><td>368.30 (-1.76%)</td><td>344.50 (-2.32%)</td><td>353.40 (-2.38%)</td><td>319.60 (-0.19%)</td><td>22.63 (-7.99%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.10 (n/a)</td><td>11.94 (n/a)</td><td>11.59 (n/a)</td><td>11.19 (n/a)</td><td>0.85 (n/a)</td><td>374.90 (n/a)</td><td>352.70 (n/a)</td><td>362.00 (n/a)</td><td>320.20 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>15.08 (-2.37%)</td><td>13.71 (-1.89%)</td><td>14.08 (-0.60%)</td><td>12.08 (+3.15%)</td><td>1.13 (-18.79%)</td><td>347.10 (-3.04%)</td><td>307.68 (+1.63%)</td><td>298.00 (+0.61%)</td><td>278.20 (+2.43%)</td><td>26.17 <b>(-20.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>15.44 (n/a)</td><td>13.97 (n/a)</td><td>14.16 (n/a)</td><td>11.71 (n/a)</td><td>1.39 (n/a)</td><td>358.00 (n/a)</td><td>302.76 (n/a)</td><td>296.20 (n/a)</td><td>271.60 (n/a)</td><td>32.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>14.69 (+8.00%)</td><td>12.89 (-0.93%)</td><td>12.94 (+0.16%)</td><td>11.28 (-11.35%)</td><td>1.45 <b>(+322.95%)</b></td><td>371.90 (+12.80%)</td><td>328.68 (+1.92%)</td><td>324.30 (-0.15%)</td><td>285.50 (-7.40%)</td><td>37.07 <b>(+346.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.60 (n/a)</td><td>13.01 (n/a)</td><td>12.91 (n/a)</td><td>12.72 (n/a)</td><td>0.34 (n/a)</td><td>329.70 (n/a)</td><td>322.50 (n/a)</td><td>324.80 (n/a)</td><td>308.30 (n/a)</td><td>8.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>14.76 (+8.07%)</td><td>13.52 (+11.28%)</td><td>13.41 (+7.93%)</td><td>11.77 (+12.69%)</td><td>1.17 (-8.41%)</td><td>356.40 (-11.25%)</td><td>312.30 (-10.40%)</td><td>312.90 (-7.34%)</td><td>284.30 (-7.45%)</td><td>28.35 <b>(-25.09%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.65 (n/a)</td><td>12.15 (n/a)</td><td>12.42 (n/a)</td><td>10.44 (n/a)</td><td>1.28 (n/a)</td><td>401.60 (n/a)</td><td>348.54 (n/a)</td><td>337.70 (n/a)</td><td>307.20 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>15.20 (+2.48%)</td><td>13.42 (-1.36%)</td><td>12.67 (-2.92%)</td><td>11.69 (-8.39%)</td><td>1.61 <b>(+56.70%)</b></td><td>358.70 (+9.16%)</td><td>316.16 (+2.08%)</td><td>331.00 (+3.02%)</td><td>275.90 (-2.44%)</td><td>37.01 <b>(+62.85%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>14.83 (n/a)</td><td>13.60 (n/a)</td><td>13.05 (n/a)</td><td>12.77 (n/a)</td><td>1.02 (n/a)</td><td>328.60 (n/a)</td><td>309.72 (n/a)</td><td>321.30 (n/a)</td><td>282.80 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>14.78 (-0.76%)</td><td>13.63 (+13.83%)</td><td>13.65 (+7.44%)</td><td>12.69 <b>(+40.99%)</b></td><td>0.94 <b>(-60.62%)</b></td><td>330.50 <b>(-29.06%)</b></td><td>308.86 (-14.73%)</td><td>307.30 (-6.91%)</td><td>283.90 (+0.78%)</td><td>21.29 <b>(-71.97%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>14.89 (n/a)</td><td>11.98 (n/a)</td><td>12.70 (n/a)</td><td>9.00 (n/a)</td><td>2.39 (n/a)</td><td>465.90 (n/a)</td><td>362.22 (n/a)</td><td>330.10 (n/a)</td><td>281.70 (n/a)</td><td>75.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.24 (+5.19%)</td><td>2.92 (+11.87%)</td><td>2.85 (+12.39%)</td><td>2.73 (+18.31%)</td><td>0.22 <b>(-24.04%)</b></td><td>192.10 (-15.49%)</td><td>180.60 (-11.03%)</td><td>183.90 (-10.99%)</td><td>162.00 (-4.93%)</td><td>13.04 <b>(-37.29%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.08 (n/a)</td><td>2.61 (n/a)</td><td>2.54 (n/a)</td><td>2.31 (n/a)</td><td>0.29 (n/a)</td><td>227.30 (n/a)</td><td>202.98 (n/a)</td><td>206.60 (n/a)</td><td>170.40 (n/a)</td><td>20.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.64 (-5.65%)</td><td>4.78 (+1.75%)</td><td>4.70 (+5.41%)</td><td>4.32 (+10.63%)</td><td>0.51 <b>(-34.66%)</b></td><td>242.60 (-9.61%)</td><td>221.02 (-2.87%)</td><td>222.90 (-5.15%)</td><td>185.80 (+5.99%)</td><td>21.69 <b>(-36.91%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>5.98 (n/a)</td><td>4.70 (n/a)</td><td>4.46 (n/a)</td><td>3.91 (n/a)</td><td>0.78 (n/a)</td><td>268.40 (n/a)</td><td>227.56 (n/a)</td><td>235.00 (n/a)</td><td>175.30 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.15 (-0.44%)</td><td>7.51 (-6.20%)</td><td>7.09 (-9.11%)</td><td>6.91 (-0.20%)</td><td>0.95 (-14.35%)</td><td>303.40 (+0.20%)</td><td>282.42 (+6.18%)</td><td>296.00 (+10.04%)</td><td>229.10 (+0.44%)</td><td>31.11 (-14.01%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.19 (n/a)</td><td>8.00 (n/a)</td><td>7.80 (n/a)</td><td>6.92 (n/a)</td><td>1.10 (n/a)</td><td>302.80 (n/a)</td><td>265.98 (n/a)</td><td>269.00 (n/a)</td><td>228.10 (n/a)</td><td>36.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.29 (-16.77%)</td><td>2.96 (-3.85%)</td><td>2.85 (+0.13%)</td><td>2.62 (+0.35%)</td><td>0.30 <b>(-45.64%)</b></td><td>200.20 (-0.35%)</td><td>178.70 (+2.51%)</td><td>183.80 (-0.11%)</td><td>159.60 <b>(+20.18%)</b></td><td>17.70 <b>(-35.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.95 (n/a)</td><td>3.08 (n/a)</td><td>2.85 (n/a)</td><td>2.61 (n/a)</td><td>0.54 (n/a)</td><td>200.90 (n/a)</td><td>174.32 (n/a)</td><td>184.00 (n/a)</td><td>132.80 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (-3.60%)</td><td>0.20 (-12.82%)</td><td>0.19 (-12.63%)</td><td>0.12 <b>(-39.02%)</b></td><td>0.06 <b>(+92.86%)</b></td><td>270.10 <b>(+64.00%)</b></td><td>175.22 <b>(+22.74%)</b></td><td>169.30 (+14.47%)</td><td>121.00 (+3.77%)</td><td>59.35 <b>(+230.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>164.70 (n/a)</td><td>142.76 (n/a)</td><td>147.90 (n/a)</td><td>116.60 (n/a)</td><td>17.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (-6.20%)</td><td>0.20 (-7.06%)</td><td>0.20 (-7.09%)</td><td>0.12 <b>(-27.33%)</b></td><td>0.05 <b>(+39.02%)</b></td><td>264.30 <b>(+37.66%)</b></td><td>176.16 (+11.83%)</td><td>165.00 (+7.63%)</td><td>131.30 (+6.66%)</td><td>52.62 <b>(+111.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.00 (n/a)</td><td>157.52 (n/a)</td><td>153.30 (n/a)</td><td>123.10 (n/a)</td><td>24.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.49 (-1.63%)</td><td>0.43 (+11.89%)</td><td>0.43 (+1.34%)</td><td>0.37 <b>(+103.14%)</b></td><td>0.04 <b>(-63.82%)</b></td><td>178.20 <b>(-50.79%)</b></td><td>152.70 <b>(-20.79%)</b></td><td>152.00 (-1.30%)</td><td>135.00 (+1.66%)</td><td>16.16 <b>(-83.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.43 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>362.10 (n/a)</td><td>192.78 (n/a)</td><td>154.00 (n/a)</td><td>132.80 (n/a)</td><td>95.39 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.51 (-0.42%)</td><td>0.40 (-1.92%)</td><td>0.39 (-10.10%)</td><td>0.34 (+18.20%)</td><td>0.07 (-19.83%)</td><td>195.60 (-15.40%)</td><td>167.42 (+0.07%)</td><td>169.50 (+11.22%)</td><td>128.00 (+0.39%)</td><td>25.49 <b>(-35.22%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>231.20 (n/a)</td><td>167.30 (n/a)</td><td>152.40 (n/a)</td><td>127.50 (n/a)</td><td>39.34 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.40 <b>(-21.88%)</b></td><td>0.34 (-16.99%)</td><td>0.36 (-5.43%)</td><td>0.24 <b>(-36.19%)</b></td><td>0.06 (+1.79%)</td><td>278.10 <b>(+56.68%)</b></td><td>197.28 <b>(+22.72%)</b></td><td>183.90 (+5.69%)</td><td>163.10 <b>(+28.02%)</b></td><td>46.35 <b>(+108.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.06 (n/a)</td><td>177.50 (n/a)</td><td>160.76 (n/a)</td><td>174.00 (n/a)</td><td>127.40 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.84 <b>(-35.29%)</b></td><td>0.79 (-9.41%)</td><td>0.77 (-1.45%)</td><td>0.73 <b>(+50.59%)</b></td><td>0.05 <b>(-85.54%)</b></td><td>178.50 <b>(-33.59%)</b></td><td>166.46 (-0.87%)</td><td>169.70 (+1.50%)</td><td>155.80 <b>(+54.56%)</b></td><td>9.49 <b>(-85.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.30 (n/a)</td><td>0.87 (n/a)</td><td>0.78 (n/a)</td><td>0.49 (n/a)</td><td>0.31 (n/a)</td><td>268.80 (n/a)</td><td>167.92 (n/a)</td><td>167.20 (n/a)</td><td>100.80 (n/a)</td><td>64.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.97 (-7.57%)</td><td>0.77 (-8.96%)</td><td>0.75 (-8.35%)</td><td>0.64 (-4.04%)</td><td>0.13 (-10.83%)</td><td>204.20 (+4.24%)</td><td>174.46 (+9.56%)</td><td>174.30 (+9.07%)</td><td>134.70 (+8.19%)</td><td>25.54 (-1.39%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.05 (n/a)</td><td>0.84 (n/a)</td><td>0.82 (n/a)</td><td>0.67 (n/a)</td><td>0.14 (n/a)</td><td>195.90 (n/a)</td><td>159.24 (n/a)</td><td>159.80 (n/a)</td><td>124.50 (n/a)</td><td>25.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.93 (-11.17%)</td><td>0.82 (+9.35%)</td><td>0.79 (+0.93%)</td><td>0.75 <b>(+57.64%)</b></td><td>0.07 <b>(-67.70%)</b></td><td>173.70 <b>(-36.58%)</b></td><td>161.14 (-14.87%)</td><td>165.80 (-0.90%)</td><td>140.20 (+12.52%)</td><td>13.52 <b>(-77.41%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.05 (n/a)</td><td>0.75 (n/a)</td><td>0.78 (n/a)</td><td>0.48 (n/a)</td><td>0.23 (n/a)</td><td>273.90 (n/a)</td><td>189.28 (n/a)</td><td>167.30 (n/a)</td><td>124.60 (n/a)</td><td>59.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.92 (-8.20%)</td><td>0.75 (-1.81%)</td><td>0.75 (-0.40%)</td><td>0.59 (+3.69%)</td><td>0.13 (-14.99%)</td><td>221.10 (-3.58%)</td><td>179.48 (+1.16%)</td><td>173.70 (+0.40%)</td><td>143.00 (+8.99%)</td><td>31.54 (-9.69%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.00 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.57 (n/a)</td><td>0.15 (n/a)</td><td>229.30 (n/a)</td><td>177.42 (n/a)</td><td>173.00 (n/a)</td><td>131.20 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (-11.71%)</td><td>0.10 (-4.52%)</td><td>0.11 (+3.64%)</td><td>0.07 (-18.43%)</td><td>0.02 (+2.27%)</td><td>235.20 <b>(+22.56%)</b></td><td>169.60 (+6.16%)</td><td>152.90 (-3.47%)</td><td>132.50 (+13.25%)</td><td>42.83 <b>(+39.35%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.90 (n/a)</td><td>159.76 (n/a)</td><td>158.40 (n/a)</td><td>117.00 (n/a)</td><td>30.74 (n/a)</td>
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
