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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (-5.05%)</td><td>0.03 (-11.80%)</td><td>0.03 (-17.51%)</td><td>0.02 <b>(-34.47%)</b></td><td>0.01 <b>(+44.93%)</b></td><td>317.50 <b>(+52.64%)</b></td><td>198.90 <b>(+20.37%)</b></td><td>191.40 <b>(+21.22%)</b></td><td>137.50 (+5.28%)</td><td>71.88 <b>(+131.78%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>165.24 (n/a)</td><td>157.90 (n/a)</td><td>130.60 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+15.33%)</td><td>0.04 (+7.52%)</td><td>0.03 (+8.08%)</td><td>0.03 (+4.43%)</td><td>0.01 (+17.33%)</td><td>200.80 (-4.24%)</td><td>171.16 (-6.82%)</td><td>175.70 (-7.48%)</td><td>138.00 (-13.32%)</td><td>23.02 (-1.53%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>183.68 (n/a)</td><td>189.90 (n/a)</td><td>159.20 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+4.83%)</td><td>0.03 (-1.58%)</td><td>0.03 (-15.53%)</td><td>0.03 (+7.19%)</td><td>0.00 (-14.51%)</td><td>222.20 (-6.72%)</td><td>188.56 (+0.68%)</td><td>193.80 (+18.32%)</td><td>152.60 (-4.63%)</td><td>27.15 <b>(-23.14%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>187.28 (n/a)</td><td>163.80 (n/a)</td><td>160.00 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(+43.73%)</b></td><td>0.03 (+3.45%)</td><td>0.03 (+6.10%)</td><td>0.02 <b>(-31.10%)</b></td><td>0.01 <b>(+508.43%)</b></td><td>282.40 <b>(+45.12%)</b></td><td>192.38 (+5.47%)</td><td>176.10 (-5.73%)</td><td>117.90 <b>(-30.44%)</b></td><td>63.98 <b>(+522.81%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.60 (n/a)</td><td>182.40 (n/a)</td><td>186.80 (n/a)</td><td>169.50 (n/a)</td><td>10.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 <b>(-32.31%)</b></td><td>0.03 <b>(-20.04%)</b></td><td>0.03 (-9.86%)</td><td>0.02 <b>(-22.86%)</b></td><td>0.01 <b>(-48.39%)</b></td><td>293.20 <b>(+29.62%)</b></td><td>211.30 <b>(+20.39%)</b></td><td>205.60 (+10.90%)</td><td>156.80 <b>(+47.79%)</b></td><td>50.72 (-0.11%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>175.52 (n/a)</td><td>185.40 (n/a)</td><td>106.10 (n/a)</td><td>50.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(+29.29%)</b></td><td>0.04 <b>(+21.44%)</b></td><td>0.04 <b>(+31.44%)</b></td><td>0.03 (-6.87%)</td><td>0.01 <b>(+157.95%)</b></td><td>230.90 (+7.35%)</td><td>168.64 (-15.23%)</td><td>157.30 <b>(-23.94%)</b></td><td>134.70 <b>(-22.68%)</b></td><td>38.09 <b>(+116.96%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>215.10 (n/a)</td><td>198.94 (n/a)</td><td>206.80 (n/a)</td><td>174.20 (n/a)</td><td>17.56 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (-8.71%)</td><td>0.03 (+8.75%)</td><td>0.03 <b>(+20.15%)</b></td><td>0.03 (+8.03%)</td><td>0.01 <b>(-28.09%)</b></td><td>213.60 (-7.45%)</td><td>182.98 (-9.72%)</td><td>185.80 (-16.76%)</td><td>148.50 (+9.59%)</td><td>29.61 <b>(-25.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>202.68 (n/a)</td><td>223.20 (n/a)</td><td>135.50 (n/a)</td><td>39.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (-13.89%)</td><td>0.03 (-9.45%)</td><td>0.04 (+14.01%)</td><td>0.02 <b>(-29.76%)</b></td><td>0.01 (+0.55%)</td><td>327.70 <b>(+42.42%)</b></td><td>205.88 (+14.06%)</td><td>167.30 (-12.27%)</td><td>153.00 (+16.08%)</td><td>73.08 <b>(+70.71%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>180.50 (n/a)</td><td>190.70 (n/a)</td><td>131.80 (n/a)</td><td>42.81 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 <b>(-24.73%)</b></td><td>0.07 <b>(-20.45%)</b></td><td>0.07 (-8.94%)</td><td>0.03 <b>(-50.28%)</b></td><td>0.02 <b>(+34.21%)</b></td><td>352.60 <b>(+101.14%)</b></td><td>202.88 <b>(+35.63%)</b></td><td>171.90 (+9.84%)</td><td>154.30 <b>(+32.90%)</b></td><td>84.35 <b>(+279.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>175.30 (n/a)</td><td>149.58 (n/a)</td><td>156.50 (n/a)</td><td>116.10 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (-8.80%)</td><td>0.08 (+0.26%)</td><td>0.07 (-9.28%)</td><td>0.06 (+19.85%)</td><td>0.02 (-12.90%)</td><td>190.50 (-16.56%)</td><td>165.46 (-1.50%)</td><td>187.20 (+10.25%)</td><td>129.90 (+9.71%)</td><td>31.71 <b>(-20.58%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>228.30 (n/a)</td><td>167.98 (n/a)</td><td>169.80 (n/a)</td><td>118.40 (n/a)</td><td>39.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (+0.91%)</td><td>0.09 (+13.49%)</td><td>0.09 <b>(+21.61%)</b></td><td>0.07 (+8.74%)</td><td>0.01 (-12.14%)</td><td>174.20 (-8.03%)</td><td>141.04 (-12.31%)</td><td>136.00 (-17.78%)</td><td>122.60 (-0.89%)</td><td>19.98 (-15.68%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>160.84 (n/a)</td><td>165.40 (n/a)</td><td>123.70 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (+11.42%)</td><td>0.09 (+8.42%)</td><td>0.09 (+0.27%)</td><td>0.07 (+7.20%)</td><td>0.02 <b>(+32.66%)</b></td><td>188.60 (-6.68%)</td><td>146.76 (-6.80%)</td><td>142.80 (-0.21%)</td><td>116.80 (-10.22%)</td><td>31.09 (+7.26%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>157.46 (n/a)</td><td>143.10 (n/a)</td><td>130.10 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (-4.27%)</td><td>0.08 (-6.78%)</td><td>0.07 (-11.47%)</td><td>0.06 <b>(-21.69%)</b></td><td>0.02 <b>(+41.72%)</b></td><td>221.40 <b>(+27.68%)</b></td><td>168.14 (+11.48%)</td><td>171.40 (+12.99%)</td><td>117.60 (+4.44%)</td><td>45.76 <b>(+87.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>173.40 (n/a)</td><td>150.82 (n/a)</td><td>151.70 (n/a)</td><td>112.60 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (+7.95%)</td><td>0.08 (+18.74%)</td><td>0.07 (+11.28%)</td><td>0.06 <b>(+46.83%)</b></td><td>0.02 (-9.58%)</td><td>198.90 <b>(-31.88%)</b></td><td>156.32 (-18.71%)</td><td>167.20 (-10.16%)</td><td>118.70 (-7.34%)</td><td>33.19 <b>(-45.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>292.00 (n/a)</td><td>192.30 (n/a)</td><td>186.10 (n/a)</td><td>128.10 (n/a)</td><td>61.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (-14.78%)</td><td>0.06 (-16.70%)</td><td>0.06 <b>(-25.90%)</b></td><td>0.04 <b>(-36.85%)</b></td><td>0.02 <b>(+27.92%)</b></td><td>324.50 <b>(+58.37%)</b></td><td>212.26 <b>(+27.41%)</b></td><td>222.40 <b>(+34.95%)</b></td><td>143.60 (+17.32%)</td><td>74.73 <b>(+118.96%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>204.90 (n/a)</td><td>166.60 (n/a)</td><td>164.80 (n/a)</td><td>122.40 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (+3.35%)</td><td>0.08 (+18.01%)</td><td>0.09 <b>(+24.33%)</b></td><td>0.05 (+10.28%)</td><td>0.02 (-2.35%)</td><td>224.80 (-9.32%)</td><td>154.10 (-15.88%)</td><td>134.20 (-19.54%)</td><td>129.60 (-3.21%)</td><td>40.26 (-13.87%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>247.90 (n/a)</td><td>183.18 (n/a)</td><td>166.80 (n/a)</td><td>133.90 (n/a)</td><td>46.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 <b>(+27.60%)</b></td><td>0.16 (+16.00%)</td><td>0.14 (-10.26%)</td><td>0.11 <b>(+58.14%)</b></td><td>0.04 (+3.71%)</td><td>223.80 <b>(-36.76%)</b></td><td>162.64 (-18.23%)</td><td>172.50 (+11.43%)</td><td>113.40 <b>(-21.63%)</b></td><td>43.30 <b>(-50.99%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>353.90 (n/a)</td><td>198.90 (n/a)</td><td>154.80 (n/a)</td><td>144.70 (n/a)</td><td>88.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (+18.74%)</td><td>0.17 <b>(+20.98%)</b></td><td>0.17 <b>(+25.23%)</b></td><td>0.15 <b>(+25.14%)</b></td><td>0.02 (-13.91%)</td><td>161.50 <b>(-20.09%)</b></td><td>141.96 (-17.96%)</td><td>144.70 <b>(-20.14%)</b></td><td>124.30 (-15.79%)</td><td>14.12 <b>(-40.65%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>173.04 (n/a)</td><td>181.20 (n/a)</td><td>147.60 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (+6.28%)</td><td>0.14 (+10.39%)</td><td>0.15 (+3.55%)</td><td>0.10 <b>(+35.91%)</b></td><td>0.03 (-13.14%)</td><td>237.20 <b>(-26.43%)</b></td><td>179.98 (-12.60%)</td><td>164.50 (-3.46%)</td><td>140.30 (-5.90%)</td><td>41.20 <b>(-41.26%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>322.40 (n/a)</td><td>205.92 (n/a)</td><td>170.40 (n/a)</td><td>149.10 (n/a)</td><td>70.13 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 <b>(+21.80%)</b></td><td>0.16 (+3.58%)</td><td>0.16 (+6.14%)</td><td>0.09 <b>(-36.54%)</b></td><td>0.04 <b>(+557.21%)</b></td><td>268.10 <b>(+57.52%)</b></td><td>167.56 (+3.55%)</td><td>151.30 (-5.79%)</td><td>125.80 (-17.89%)</td><td>57.67 <b>(+789.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>170.20 (n/a)</td><td>161.82 (n/a)</td><td>160.60 (n/a)</td><td>153.20 (n/a)</td><td>6.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (+0.23%)</td><td>0.16 (+3.37%)</td><td>0.16 (+8.37%)</td><td>0.13 (+13.47%)</td><td>0.03 (-10.15%)</td><td>190.80 (-11.91%)</td><td>158.78 (-4.10%)</td><td>151.80 (-7.72%)</td><td>131.80 (-0.23%)</td><td>27.43 (-19.52%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.60 (n/a)</td><td>165.56 (n/a)</td><td>164.50 (n/a)</td><td>132.10 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (+18.22%)</td><td>0.17 <b>(+21.99%)</b></td><td>0.18 <b>(+30.19%)</b></td><td>0.13 (+12.20%)</td><td>0.03 <b>(+52.99%)</b></td><td>193.20 (-10.84%)</td><td>150.64 (-17.05%)</td><td>136.80 <b>(-23.19%)</b></td><td>125.30 (-15.40%)</td><td>29.12 (+15.05%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.70 (n/a)</td><td>181.60 (n/a)</td><td>178.10 (n/a)</td><td>148.10 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (+5.34%)</td><td>0.14 (+9.50%)</td><td>0.16 (+12.89%)</td><td>0.07 <b>(-25.77%)</b></td><td>0.04 <b>(+70.24%)</b></td><td>329.60 <b>(+34.70%)</b></td><td>190.56 (-2.51%)</td><td>156.40 (-11.39%)</td><td>153.00 (-5.09%)</td><td>77.79 <b>(+119.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>244.70 (n/a)</td><td>195.46 (n/a)</td><td>176.50 (n/a)</td><td>161.20 (n/a)</td><td>35.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (+7.08%)</td><td>0.13 (-4.43%)</td><td>0.13 (-0.72%)</td><td>0.08 <b>(-27.53%)</b></td><td>0.03 <b>(+99.66%)</b></td><td>303.70 <b>(+37.98%)</b></td><td>200.96 (+9.90%)</td><td>183.70 (+0.71%)</td><td>149.10 (-6.58%)</td><td>61.26 <b>(+162.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.10 (n/a)</td><td>182.86 (n/a)</td><td>182.40 (n/a)</td><td>159.60 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (+6.30%)</td><td>0.28 (-0.41%)</td><td>0.28 (-5.79%)</td><td>0.25 (-0.54%)</td><td>0.03 <b>(+22.08%)</b></td><td>195.30 (+0.57%)</td><td>176.10 (+0.69%)</td><td>177.70 (+6.15%)</td><td>147.00 (-5.95%)</td><td>18.46 (+12.55%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>194.20 (n/a)</td><td>174.90 (n/a)</td><td>167.40 (n/a)</td><td>156.30 (n/a)</td><td>16.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.38 (+0.48%)</td><td>0.31 (-2.22%)</td><td>0.31 (+5.47%)</td><td>0.26 (+2.55%)</td><td>0.05 (-18.72%)</td><td>191.30 (-2.50%)</td><td>162.14 (+1.35%)</td><td>160.90 (-5.19%)</td><td>128.90 (-0.46%)</td><td>23.21 (-19.08%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>196.20 (n/a)</td><td>159.98 (n/a)</td><td>169.70 (n/a)</td><td>129.50 (n/a)</td><td>28.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (-7.46%)</td><td>0.28 (-13.62%)</td><td>0.26 (-19.02%)</td><td>0.22 <b>(-20.00%)</b></td><td>0.05 <b>(+72.43%)</b></td><td>218.80 <b>(+25.03%)</b></td><td>179.44 (+17.90%)</td><td>186.40 <b>(+23.53%)</b></td><td>147.40 (+8.06%)</td><td>31.25 <b>(+120.94%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>175.00 (n/a)</td><td>152.20 (n/a)</td><td>150.90 (n/a)</td><td>136.40 (n/a)</td><td>14.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.38 (-8.48%)</td><td>0.28 (-9.21%)</td><td>0.27 (-9.37%)</td><td>0.23 (-6.52%)</td><td>0.06 (-2.52%)</td><td>217.80 (+6.97%)</td><td>178.58 (+10.63%)</td><td>179.50 (+10.33%)</td><td>129.00 (+9.32%)</td><td>35.30 (+16.46%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>203.60 (n/a)</td><td>161.42 (n/a)</td><td>162.70 (n/a)</td><td>118.00 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.31 (-11.13%)</td><td>0.26 (-10.58%)</td><td>0.28 (-4.26%)</td><td>0.23 (-16.61%)</td><td>0.03 (+15.19%)</td><td>215.60 (+19.91%)</td><td>188.14 (+12.55%)</td><td>177.20 (+4.42%)</td><td>158.50 (+12.57%)</td><td>24.90 <b>(+62.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>179.80 (n/a)</td><td>167.16 (n/a)</td><td>169.70 (n/a)</td><td>140.80 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (-16.96%)</td><td>0.26 (-14.06%)</td><td>0.27 (-10.33%)</td><td>0.23 (-2.53%)</td><td>0.03 <b>(-44.79%)</b></td><td>215.80 (+2.62%)</td><td>188.82 (+14.78%)</td><td>184.10 (+11.51%)</td><td>164.30 <b>(+20.45%)</b></td><td>19.39 <b>(-32.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>210.30 (n/a)</td><td>164.50 (n/a)</td><td>165.10 (n/a)</td><td>136.40 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (-1.35%)</td><td>0.22 (-9.93%)</td><td>0.23 (-7.54%)</td><td>0.15 <b>(-33.30%)</b></td><td>0.04 <b>(+125.49%)</b></td><td>322.80 <b>(+49.93%)</b></td><td>227.82 (+14.75%)</td><td>212.20 (+8.15%)</td><td>180.60 (+1.35%)</td><td>54.87 <b>(+258.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>215.30 (n/a)</td><td>198.54 (n/a)</td><td>196.20 (n/a)</td><td>178.20 (n/a)</td><td>15.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (-9.20%)</td><td>0.25 (-4.67%)</td><td>0.25 (-2.75%)</td><td>0.21 (-3.11%)</td><td>0.03 <b>(-24.88%)</b></td><td>239.80 (+3.23%)</td><td>201.30 (+4.37%)</td><td>193.90 (+2.86%)</td><td>179.00 (+10.15%)</td><td>23.39 (-13.49%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>232.30 (n/a)</td><td>192.88 (n/a)</td><td>188.50 (n/a)</td><td>162.50 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (+8.31%)</td><td>0.02 (-2.17%)</td><td>0.02 (-5.14%)</td><td>0.01 (-7.22%)</td><td>0.00 (+5.10%)</td><td>208.40 (+7.81%)</td><td>159.42 (+2.47%)</td><td>156.40 (+5.39%)</td><td>115.40 (-7.68%)</td><td>33.40 (+4.43%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>193.30 (n/a)</td><td>155.58 (n/a)</td><td>148.40 (n/a)</td><td>125.00 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (+17.15%)</td><td>0.02 (+8.91%)</td><td>0.02 (+1.43%)</td><td>0.01 (+18.42%)</td><td>0.00 (+16.98%)</td><td>183.80 (-15.57%)</td><td>159.70 (-8.28%)</td><td>169.70 (-1.45%)</td><td>119.50 (-14.64%)</td><td>24.64 (-18.12%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>217.70 (n/a)</td><td>174.12 (n/a)</td><td>172.20 (n/a)</td><td>140.00 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (-12.08%)</td><td>0.02 (-4.22%)</td><td>0.02 (+12.75%)</td><td>0.01 <b>(-24.57%)</b></td><td>0.00 (+9.05%)</td><td>241.60 <b>(+32.60%)</b></td><td>172.10 (+6.43%)</td><td>149.80 (-11.31%)</td><td>136.00 (+13.71%)</td><td>43.06 <b>(+68.05%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>182.20 (n/a)</td><td>161.70 (n/a)</td><td>168.90 (n/a)</td><td>119.60 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 <b>(-20.45%)</b></td><td>0.02 (-8.68%)</td><td>0.02 (-4.22%)</td><td>0.01 (-1.36%)</td><td>0.00 <b>(-50.91%)</b></td><td>191.60 (+1.38%)</td><td>171.42 (+7.29%)</td><td>170.80 (+4.40%)</td><td>143.50 <b>(+25.66%)</b></td><td>18.04 <b>(-36.11%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>159.78 (n/a)</td><td>163.60 (n/a)</td><td>114.20 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (-1.12%)</td><td>0.02 (+6.05%)</td><td>0.02 (+5.85%)</td><td>0.01 (+5.61%)</td><td>0.00 (-6.39%)</td><td>215.20 (-5.32%)</td><td>171.72 (-6.05%)</td><td>163.10 (-5.50%)</td><td>149.20 (+1.15%)</td><td>27.39 (-11.89%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>227.30 (n/a)</td><td>182.78 (n/a)</td><td>172.60 (n/a)</td><td>147.50 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.01 (-18.26%)</td><td>0.01 (-9.19%)</td><td>0.01 (+3.12%)</td><td>0.01 (-15.93%)</td><td>0.00 <b>(-36.60%)</b></td><td>235.20 (+18.97%)</td><td>193.84 (+9.33%)</td><td>187.70 (-3.00%)</td><td>178.40 <b>(+22.36%)</b></td><td>23.65 (-7.61%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>197.70 (n/a)</td><td>177.30 (n/a)</td><td>193.50 (n/a)</td><td>145.80 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (+4.67%)</td><td>0.01 (+5.46%)</td><td>0.01 (+3.78%)</td><td>0.01 (-0.71%)</td><td>0.00 <b>(+22.71%)</b></td><td>232.50 (+0.69%)</td><td>194.06 (-4.47%)</td><td>200.70 (-3.65%)</td><td>152.40 (-4.45%)</td><td>32.27 <b>(+20.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>230.90 (n/a)</td><td>203.14 (n/a)</td><td>208.30 (n/a)</td><td>159.50 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.01 (-3.33%)</td><td>0.01 (+1.39%)</td><td>0.01 (+6.24%)</td><td>0.01 (+6.16%)</td><td>0.00 (-15.39%)</td><td>242.30 (-5.79%)</td><td>214.00 (-1.86%)</td><td>207.20 (-5.90%)</td><td>181.30 (+3.42%)</td><td>27.18 (-14.97%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>257.20 (n/a)</td><td>218.06 (n/a)</td><td>220.20 (n/a)</td><td>175.30 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+10.84%)</td><td>0.03 (+1.87%)</td><td>0.03 (-14.79%)</td><td>0.03 (+11.54%)</td><td>0.00 (-9.80%)</td><td>168.50 (-10.32%)</td><td>153.96 (-2.51%)</td><td>164.30 (+17.36%)</td><td>124.40 (-9.79%)</td><td>18.92 <b>(-26.45%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>187.90 (n/a)</td><td>157.92 (n/a)</td><td>140.00 (n/a)</td><td>137.90 (n/a)</td><td>25.72 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+17.85%)</td><td>0.03 (+6.36%)</td><td>0.03 (-2.48%)</td><td>0.02 (+16.12%)</td><td>0.01 (+9.98%)</td><td>231.30 (-13.89%)</td><td>171.74 (-6.70%)</td><td>175.60 (+2.51%)</td><td>118.50 (-15.11%)</td><td>40.67 <b>(-21.30%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.60 (n/a)</td><td>184.08 (n/a)</td><td>171.30 (n/a)</td><td>139.60 (n/a)</td><td>51.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-8.00%)</td><td>0.03 (-4.45%)</td><td>0.03 (+0.06%)</td><td>0.03 (+3.33%)</td><td>0.00 <b>(-44.89%)</b></td><td>184.40 (-3.20%)</td><td>168.90 (+3.77%)</td><td>167.30 (-0.06%)</td><td>152.60 (+8.69%)</td><td>12.18 <b>(-40.88%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>162.76 (n/a)</td><td>167.40 (n/a)</td><td>140.40 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 <b>(-28.07%)</b></td><td>0.02 (-19.36%)</td><td>0.03 (-14.55%)</td><td>0.02 <b>(-22.50%)</b></td><td>0.01 <b>(-23.31%)</b></td><td>341.50 <b>(+29.06%)</b></td><td>227.34 <b>(+24.38%)</b></td><td>200.80 (+17.02%)</td><td>178.60 <b>(+39.10%)</b></td><td>67.34 <b>(+34.64%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>264.60 (n/a)</td><td>182.78 (n/a)</td><td>171.60 (n/a)</td><td>128.40 (n/a)</td><td>50.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-1.41%)</td><td>0.03 (+6.46%)</td><td>0.03 (+6.15%)</td><td>0.03 (+18.06%)</td><td>0.00 <b>(-48.55%)</b></td><td>187.40 (-15.28%)</td><td>173.50 (-7.66%)</td><td>176.00 (-5.78%)</td><td>153.50 (+1.45%)</td><td>13.43 <b>(-56.55%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.20 (n/a)</td><td>187.90 (n/a)</td><td>186.80 (n/a)</td><td>151.30 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 <b>(+30.35%)</b></td><td>0.03 (+14.36%)</td><td>0.03 (-0.74%)</td><td>0.02 (+6.88%)</td><td>0.01 <b>(+140.01%)</b></td><td>215.00 (-6.44%)</td><td>177.88 (-10.00%)</td><td>196.50 (+0.72%)</td><td>130.50 <b>(-23.28%)</b></td><td>37.03 <b>(+70.76%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.80 (n/a)</td><td>197.64 (n/a)</td><td>195.10 (n/a)</td><td>170.10 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-11.88%)</td><td>0.03 (+13.28%)</td><td>0.03 <b>(+21.29%)</b></td><td>0.03 <b>(+44.92%)</b></td><td>0.00 <b>(-70.13%)</b></td><td>209.60 <b>(-30.98%)</b></td><td>195.08 (-15.76%)</td><td>192.30 (-17.57%)</td><td>181.10 (+13.47%)</td><td>13.36 <b>(-76.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>303.70 (n/a)</td><td>231.58 (n/a)</td><td>233.30 (n/a)</td><td>159.60 (n/a)</td><td>56.30 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+15.49%)</td><td>0.03 (+7.25%)</td><td>0.03 (+9.75%)</td><td>0.02 (-17.29%)</td><td>0.01 <b>(+89.08%)</b></td><td>306.80 <b>(+20.93%)</b></td><td>210.50 (-2.37%)</td><td>204.40 (-8.87%)</td><td>148.30 (-13.43%)</td><td>61.82 <b>(+101.78%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.70 (n/a)</td><td>215.60 (n/a)</td><td>224.30 (n/a)</td><td>171.30 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(+26.07%)</b></td><td>0.07 <b>(+21.71%)</b></td><td>0.06 (+9.74%)</td><td>0.06 <b>(+50.77%)</b></td><td>0.01 (+3.00%)</td><td>168.20 <b>(-33.70%)</b></td><td>150.48 (-18.96%)</td><td>162.60 (-8.86%)</td><td>122.90 <b>(-20.66%)</b></td><td>21.78 <b>(-45.77%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>253.70 (n/a)</td><td>185.68 (n/a)</td><td>178.40 (n/a)</td><td>154.90 (n/a)</td><td>40.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (-11.65%)</td><td>0.05 (-12.88%)</td><td>0.05 <b>(-22.96%)</b></td><td>0.04 (-10.21%)</td><td>0.01 (-3.23%)</td><td>255.40 (+11.38%)</td><td>203.78 (+15.43%)</td><td>221.00 <b>(+29.77%)</b></td><td>152.40 (+13.22%)</td><td>46.34 (+18.13%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>176.54 (n/a)</td><td>170.30 (n/a)</td><td>134.60 (n/a)</td><td>39.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (-0.17%)</td><td>0.07 (+9.34%)</td><td>0.07 (+12.45%)</td><td>0.05 (-0.81%)</td><td>0.01 (+6.56%)</td><td>193.20 (+0.78%)</td><td>153.76 (-8.31%)</td><td>156.80 (-11.11%)</td><td>127.20 (+0.16%)</td><td>27.27 (+6.00%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>167.70 (n/a)</td><td>176.40 (n/a)</td><td>127.00 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(+25.54%)</b></td><td>0.07 <b>(+41.92%)</b></td><td>0.07 <b>(+44.51%)</b></td><td>0.06 <b>(+40.39%)</b></td><td>0.01 (+3.83%)</td><td>183.60 <b>(-28.78%)</b></td><td>145.40 <b>(-30.44%)</b></td><td>147.60 <b>(-30.77%)</b></td><td>118.70 <b>(-20.34%)</b></td><td>24.90 <b>(-39.97%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>257.80 (n/a)</td><td>209.02 (n/a)</td><td>213.20 (n/a)</td><td>149.00 (n/a)</td><td>41.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (+16.04%)</td><td>0.07 (+15.41%)</td><td>0.07 <b>(+21.92%)</b></td><td>0.05 (+13.51%)</td><td>0.01 (-2.40%)</td><td>213.80 (-11.87%)</td><td>161.80 (-14.29%)</td><td>147.90 (-17.97%)</td><td>126.30 (-13.85%)</td><td>33.60 <b>(-23.36%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>242.60 (n/a)</td><td>188.78 (n/a)</td><td>180.30 (n/a)</td><td>146.60 (n/a)</td><td>43.84 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (-13.62%)</td><td>0.05 (-16.08%)</td><td>0.05 (-18.11%)</td><td>0.03 (+0.15%)</td><td>0.02 <b>(-22.48%)</b></td><td>342.40 (-0.15%)</td><td>213.98 (+14.57%)</td><td>191.50 <b>(+22.13%)</b></td><td>148.30 (+15.77%)</td><td>76.12 (-13.71%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>342.90 (n/a)</td><td>186.76 (n/a)</td><td>156.80 (n/a)</td><td>128.10 (n/a)</td><td>88.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (+10.13%)</td><td>0.06 (-7.03%)</td><td>0.06 (-11.46%)</td><td>0.05 (-15.62%)</td><td>0.01 <b>(+70.82%)</b></td><td>217.20 (+18.49%)</td><td>175.34 (+10.08%)</td><td>180.20 (+12.91%)</td><td>126.90 (-9.23%)</td><td>34.78 <b>(+84.11%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>159.28 (n/a)</td><td>159.60 (n/a)</td><td>139.80 (n/a)</td><td>18.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(-22.41%)</b></td><td>0.04 <b>(-22.47%)</b></td><td>0.04 <b>(-22.74%)</b></td><td>0.03 (+9.74%)</td><td>0.01 <b>(-40.48%)</b></td><td>358.80 (-8.86%)</td><td>274.46 <b>(+21.55%)</b></td><td>238.80 <b>(+29.43%)</b></td><td>209.70 <b>(+28.89%)</b></td><td>66.61 <b>(-30.80%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>393.70 (n/a)</td><td>225.80 (n/a)</td><td>184.50 (n/a)</td><td>162.70 (n/a)</td><td>96.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (+6.18%)</td><td>0.12 (-11.16%)</td><td>0.12 <b>(-22.66%)</b></td><td>0.10 (-7.16%)</td><td>0.03 (+7.83%)</td><td>208.90 (+7.74%)</td><td>178.48 (+13.08%)</td><td>176.70 <b>(+29.36%)</b></td><td>126.50 (-5.81%)</td><td>33.00 (+8.87%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>193.90 (n/a)</td><td>157.84 (n/a)</td><td>136.60 (n/a)</td><td>134.30 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 <b>(+38.02%)</b></td><td>0.13 (+4.45%)</td><td>0.14 (+10.55%)</td><td>0.06 <b>(-28.77%)</b></td><td>0.05 <b>(+131.60%)</b></td><td>338.00 <b>(+40.42%)</b></td><td>190.78 (+7.57%)</td><td>153.60 (-9.54%)</td><td>106.40 <b>(-27.57%)</b></td><td>89.12 <b>(+139.79%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>240.70 (n/a)</td><td>177.36 (n/a)</td><td>169.80 (n/a)</td><td>146.90 (n/a)</td><td>37.17 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (-11.02%)</td><td>0.14 (-4.34%)</td><td>0.14 (-1.19%)</td><td>0.12 (+9.12%)</td><td>0.02 <b>(-45.70%)</b></td><td>173.40 (-8.35%)</td><td>150.14 (+1.51%)</td><td>154.70 (+1.18%)</td><td>124.40 (+12.38%)</td><td>19.10 <b>(-43.13%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>189.20 (n/a)</td><td>147.90 (n/a)</td><td>152.90 (n/a)</td><td>110.70 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-8.23%)</td><td>0.12 (-7.79%)</td><td>0.12 (-2.99%)</td><td>0.09 (-18.55%)</td><td>0.01 (+11.89%)</td><td>223.50 <b>(+22.80%)</b></td><td>182.24 (+9.01%)</td><td>177.90 (+3.07%)</td><td>162.80 (+8.97%)</td><td>24.22 <b>(+52.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>182.00 (n/a)</td><td>167.18 (n/a)</td><td>172.60 (n/a)</td><td>149.40 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (+15.89%)</td><td>0.13 (+14.20%)</td><td>0.13 (+11.69%)</td><td>0.12 (+16.46%)</td><td>0.01 (+2.35%)</td><td>181.10 (-14.13%)</td><td>163.68 (-12.57%)</td><td>161.60 (-10.47%)</td><td>146.70 (-13.71%)</td><td>14.16 <b>(-23.62%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>187.22 (n/a)</td><td>180.50 (n/a)</td><td>170.00 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (+7.38%)</td><td>0.12 (+7.07%)</td><td>0.12 (+5.59%)</td><td>0.11 (+12.61%)</td><td>0.01 (+1.08%)</td><td>189.00 (-11.23%)</td><td>173.86 (-6.75%)</td><td>182.10 (-5.30%)</td><td>149.00 (-6.88%)</td><td>17.67 (-15.13%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>186.44 (n/a)</td><td>192.30 (n/a)</td><td>160.00 (n/a)</td><td>20.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 <b>(+23.52%)</b></td><td>0.12 (-0.70%)</td><td>0.12 (+9.28%)</td><td>0.07 <b>(-28.38%)</b></td><td>0.04 <b>(+187.05%)</b></td><td>291.10 <b>(+39.62%)</b></td><td>197.46 (+8.88%)</td><td>169.10 (-8.50%)</td><td>129.00 (-19.02%)</td><td>67.00 <b>(+235.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>181.36 (n/a)</td><td>184.80 (n/a)</td><td>159.30 (n/a)</td><td>19.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (-5.04%)</td><td>0.11 (+8.30%)</td><td>0.10 (+8.19%)</td><td>0.09 <b>(+24.04%)</b></td><td>0.01 <b>(-42.23%)</b></td><td>226.10 (-19.39%)</td><td>201.48 (-9.55%)</td><td>201.80 (-7.60%)</td><td>174.80 (+5.30%)</td><td>20.70 <b>(-50.34%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>280.50 (n/a)</td><td>222.76 (n/a)</td><td>218.40 (n/a)</td><td>166.00 (n/a)</td><td>41.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>180.00 (n/a)</td><td>178.10 (n/a)</td><td>173.10 (n/a)</td><td>8.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>175.52 (n/a)</td><td>172.70 (n/a)</td><td>140.60 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>224.60 (n/a)</td><td>202.64 (n/a)</td><td>196.40 (n/a)</td><td>184.40 (n/a)</td><td>16.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>227.60 (n/a)</td><td>211.70 (n/a)</td><td>206.80 (n/a)</td><td>202.70 (n/a)</td><td>10.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>241.60 (n/a)</td><td>190.30 (n/a)</td><td>177.30 (n/a)</td><td>158.90 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>271.90 (n/a)</td><td>213.86 (n/a)</td><td>205.00 (n/a)</td><td>180.10 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>216.00 (n/a)</td><td>201.96 (n/a)</td><td>201.00 (n/a)</td><td>180.30 (n/a)</td><td>14.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>259.90 (n/a)</td><td>211.34 (n/a)</td><td>205.90 (n/a)</td><td>190.70 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>197.20 (n/a)</td><td>175.62 (n/a)</td><td>177.70 (n/a)</td><td>149.00 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>332.90 (n/a)</td><td>217.06 (n/a)</td><td>213.70 (n/a)</td><td>158.30 (n/a)</td><td>70.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>211.86 (n/a)</td><td>210.20 (n/a)</td><td>179.70 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>241.20 (n/a)</td><td>202.64 (n/a)</td><td>205.20 (n/a)</td><td>141.80 (n/a)</td><td>37.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (-3.05%)</td><td>0.28 (+14.32%)</td><td>0.30 <b>(+22.60%)</b></td><td>0.22 <b>(+31.89%)</b></td><td>0.05 (-18.95%)</td><td>227.50 <b>(-24.17%)</b></td><td>183.06 (-14.74%)</td><td>165.20 (-18.42%)</td><td>150.30 (+3.16%)</td><td>36.28 <b>(-36.26%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>300.00 (n/a)</td><td>214.70 (n/a)</td><td>202.50 (n/a)</td><td>145.70 (n/a)</td><td>56.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>192.50 (n/a)</td><td>193.10 (n/a)</td><td>178.00 (n/a)</td><td>14.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>238.90 (n/a)</td><td>204.04 (n/a)</td><td>228.20 (n/a)</td><td>126.30 (n/a)</td><td>47.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>252.10 (n/a)</td><td>202.10 (n/a)</td><td>201.90 (n/a)</td><td>165.70 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>161.80 (n/a)</td><td>139.42 (n/a)</td><td>135.20 (n/a)</td><td>128.70 (n/a)</td><td>12.87 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>168.50 (n/a)</td><td>145.62 (n/a)</td><td>140.30 (n/a)</td><td>124.10 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>166.50 (n/a)</td><td>150.64 (n/a)</td><td>145.20 (n/a)</td><td>138.10 (n/a)</td><td>13.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.50 (n/a)</td><td>186.12 (n/a)</td><td>186.20 (n/a)</td><td>128.60 (n/a)</td><td>47.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>144.12 (n/a)</td><td>145.00 (n/a)</td><td>120.20 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>177.30 (n/a)</td><td>150.04 (n/a)</td><td>142.50 (n/a)</td><td>131.20 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>171.06 (n/a)</td><td>175.70 (n/a)</td><td>147.90 (n/a)</td><td>16.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.20 (n/a)</td><td>185.84 (n/a)</td><td>187.30 (n/a)</td><td>150.10 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>167.80 (n/a)</td><td>164.00 (n/a)</td><td>140.60 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>178.08 (n/a)</td><td>179.70 (n/a)</td><td>142.80 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.20 (n/a)</td><td>172.04 (n/a)</td><td>161.20 (n/a)</td><td>132.70 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.90 (n/a)</td><td>172.78 (n/a)</td><td>152.30 (n/a)</td><td>141.50 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>194.40 (n/a)</td><td>165.18 (n/a)</td><td>160.00 (n/a)</td><td>132.40 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>170.80 (n/a)</td><td>148.62 (n/a)</td><td>138.00 (n/a)</td><td>136.80 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>211.90 (n/a)</td><td>185.38 (n/a)</td><td>203.00 (n/a)</td><td>149.60 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.70 (n/a)</td><td>156.18 (n/a)</td><td>155.30 (n/a)</td><td>117.00 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>185.60 (n/a)</td><td>151.48 (n/a)</td><td>145.10 (n/a)</td><td>120.00 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>165.66 (n/a)</td><td>158.90 (n/a)</td><td>144.20 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>175.48 (n/a)</td><td>180.30 (n/a)</td><td>130.50 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.10 (n/a)</td><td>182.84 (n/a)</td><td>170.80 (n/a)</td><td>154.70 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.90 (n/a)</td><td>162.78 (n/a)</td><td>168.50 (n/a)</td><td>136.70 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.00 (n/a)</td><td>178.40 (n/a)</td><td>186.00 (n/a)</td><td>147.20 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>267.80 (n/a)</td><td>219.06 (n/a)</td><td>213.20 (n/a)</td><td>194.30 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>386.40 (n/a)</td><td>219.94 (n/a)</td><td>182.30 (n/a)</td><td>169.20 (n/a)</td><td>93.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>162.34 (n/a)</td><td>147.80 (n/a)</td><td>131.60 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>178.30 (n/a)</td><td>189.90 (n/a)</td><td>128.30 (n/a)</td><td>31.53 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>178.54 (n/a)</td><td>179.60 (n/a)</td><td>156.00 (n/a)</td><td>19.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>255.50 (n/a)</td><td>181.54 (n/a)</td><td>163.20 (n/a)</td><td>120.70 (n/a)</td><td>59.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>168.30 (n/a)</td><td>160.30 (n/a)</td><td>125.00 (n/a)</td><td>36.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>167.90 (n/a)</td><td>166.70 (n/a)</td><td>120.80 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>326.30 (n/a)</td><td>255.86 (n/a)</td><td>239.60 (n/a)</td><td>209.70 (n/a)</td><td>46.96 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>276.00 (n/a)</td><td>199.48 (n/a)</td><td>190.30 (n/a)</td><td>129.60 (n/a)</td><td>54.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>164.80 (n/a)</td><td>171.80 (n/a)</td><td>131.60 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>165.64 (n/a)</td><td>156.30 (n/a)</td><td>134.00 (n/a)</td><td>40.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>169.64 (n/a)</td><td>168.60 (n/a)</td><td>149.60 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.00 (n/a)</td><td>159.00 (n/a)</td><td>153.60 (n/a)</td><td>117.60 (n/a)</td><td>40.56 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.50 (n/a)</td><td>173.78 (n/a)</td><td>183.70 (n/a)</td><td>133.50 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>157.40 (n/a)</td><td>151.92 (n/a)</td><td>153.50 (n/a)</td><td>145.70 (n/a)</td><td>5.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>317.30 (n/a)</td><td>233.62 (n/a)</td><td>212.00 (n/a)</td><td>173.70 (n/a)</td><td>55.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>303.30 (n/a)</td><td>183.68 (n/a)</td><td>157.40 (n/a)</td><td>133.30 (n/a)</td><td>69.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.00 (n/a)</td><td>159.36 (n/a)</td><td>146.10 (n/a)</td><td>133.80 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>234.00 (n/a)</td><td>159.90 (n/a)</td><td>134.70 (n/a)</td><td>132.50 (n/a)</td><td>43.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>166.20 (n/a)</td><td>147.12 (n/a)</td><td>147.70 (n/a)</td><td>126.50 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.30 (n/a)</td><td>159.34 (n/a)</td><td>147.90 (n/a)</td><td>145.10 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.80 (n/a)</td><td>163.68 (n/a)</td><td>155.30 (n/a)</td><td>128.50 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>178.14 (n/a)</td><td>175.60 (n/a)</td><td>166.00 (n/a)</td><td>10.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>4.62 (-5.58%)</td><td>3.98 (-2.56%)</td><td>4.06 (-0.94%)</td><td>3.48 (+6.94%)</td><td>0.45 <b>(-23.57%)</b></td><td>2706.20 (-6.49%)</td><td>2383.88 (+1.90%)</td><td>2314.30 (+0.95%)</td><td>2034.50 (+5.91%)</td><td>261.59 <b>(-25.18%)</b></td><td>1818.31 (-5.58%)</td><td>1567.13 (-2.56%)</td><td>1598.46 (-0.94%)</td><td>1367.02 (+6.94%)</td><td>175.05 <b>(-23.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>4.90 (n/a)</td><td>4.09 (n/a)</td><td>4.10 (n/a)</td><td>3.25 (n/a)</td><td>0.58 (n/a)</td><td>2894.00 (n/a)</td><td>2339.42 (n/a)</td><td>2292.50 (n/a)</td><td>1921.00 (n/a)</td><td>349.63 (n/a)</td><td>1925.73 (n/a)</td><td>1608.36 (n/a)</td><td>1613.68 (n/a)</td><td>1278.29 (n/a)</td><td>229.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.36 <b>(+21.89%)</b></td><td>0.99 (+5.15%)</td><td>1.03 (+9.35%)</td><td>0.65 (-16.54%)</td><td>0.30 <b>(+156.29%)</b></td><td>338.00 (+19.82%)</td><td>241.16 (+1.58%)</td><td>214.00 (-8.55%)</td><td>163.20 (-17.95%)</td><td>76.34 <b>(+156.80%)</b></td><td>57.84 <b>(+21.89%)</b></td><td>42.32 (+5.15%)</td><td>44.10 (+9.35%)</td><td>27.92 (-16.54%)</td><td>12.77 <b>(+156.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>1.11 (n/a)</td><td>0.94 (n/a)</td><td>0.95 (n/a)</td><td>0.78 (n/a)</td><td>0.12 (n/a)</td><td>282.10 (n/a)</td><td>237.40 (n/a)</td><td>234.00 (n/a)</td><td>198.90 (n/a)</td><td>29.73 (n/a)</td><td>47.45 (n/a)</td><td>40.25 (n/a)</td><td>40.33 (n/a)</td><td>33.45 (n/a)</td><td>4.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.04 (-10.49%)</td><td>0.93 (-5.58%)</td><td>0.95 (-13.39%)</td><td>0.76 <b>(+24.41%)</b></td><td>0.10 <b>(-54.65%)</b></td><td>290.70 (-19.61%)</td><td>240.90 (+1.18%)</td><td>233.00 (+15.46%)</td><td>212.50 (+11.72%)</td><td>29.58 <b>(-58.79%)</b></td><td>44.41 (-10.49%)</td><td>39.61 (-5.58%)</td><td>40.50 (-13.39%)</td><td>32.47 <b>(+24.41%)</b></td><td>4.41 <b>(-54.65%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>1.16 (n/a)</td><td>0.98 (n/a)</td><td>1.10 (n/a)</td><td>0.61 (n/a)</td><td>0.23 (n/a)</td><td>361.60 (n/a)</td><td>238.10 (n/a)</td><td>201.80 (n/a)</td><td>190.20 (n/a)</td><td>71.78 (n/a)</td><td>49.62 (n/a)</td><td>41.95 (n/a)</td><td>46.76 (n/a)</td><td>26.10 (n/a)</td><td>9.72 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.52 (-0.02%)</td><td>0.52 (-0.03%)</td><td>0.52 (+0.04%)</td><td>0.52 (-0.17%)</td><td>0.00 <b>(+127.09%)</b></td><td>48755.00 (+0.17%)</td><td>48656.00 (+0.03%)</td><td>48626.40 (-0.04%)</td><td>48623.90 (+0.02%)</td><td>56.48 <b>(+127.69%)</b></td><td>353.32 (-0.02%)</td><td>353.09 (-0.03%)</td><td>353.30 (+0.04%)</td><td>352.37 (-0.17%)</td><td>0.41 <b>(+127.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48672.00 (n/a)</td><td>48641.44 (n/a)</td><td>48648.20 (n/a)</td><td>48614.70 (n/a)</td><td>24.81 (n/a)</td><td>353.39 (n/a)</td><td>353.19 (n/a)</td><td>353.15 (n/a)</td><td>352.97 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (+1.77%)</td><td>0.21 (+0.87%)</td><td>0.21 (+0.74%)</td><td>0.21 (+0.61%)</td><td>0.00 <b>(+136.84%)</b></td><td>117911.50 (-0.61%)</td><td>117260.90 (-0.86%)</td><td>117457.90 (-0.74%)</td><td>115869.40 (-1.74%)</td><td>800.61 <b>(+130.99%)</b></td><td>148.27 (+1.77%)</td><td>146.52 (+0.87%)</td><td>146.26 (+0.74%)</td><td>145.70 (+0.61%)</td><td>1.01 <b>(+136.85%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118633.00 (n/a)</td><td>118282.30 (n/a)</td><td>118331.30 (n/a)</td><td>117917.90 (n/a)</td><td>346.60 (n/a)</td><td>145.69 (n/a)</td><td>145.25 (n/a)</td><td>145.18 (n/a)</td><td>144.82 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.89 (-1.22%)</td><td>0.88 (-0.94%)</td><td>0.88 (-0.84%)</td><td>0.87 (-0.73%)</td><td>0.01 <b>(-27.91%)</b></td><td>28924.80 (+0.74%)</td><td>28568.00 (+0.94%)</td><td>28618.30 (+0.85%)</td><td>28240.50 (+1.24%)</td><td>256.45 <b>(-26.39%)</b></td><td>608.34 (-1.22%)</td><td>601.41 (-0.94%)</td><td>600.31 (-0.84%)</td><td>593.95 (-0.73%)</td><td>5.39 <b>(-27.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28713.10 (n/a)</td><td>28301.36 (n/a)</td><td>28378.30 (n/a)</td><td>27895.20 (n/a)</td><td>348.41 (n/a)</td><td>615.87 (n/a)</td><td>607.11 (n/a)</td><td>605.39 (n/a)</td><td>598.33 (n/a)</td><td>7.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>3.50 (-1.83%)</td><td>3.41 (-0.40%)</td><td>3.46 (+1.72%)</td><td>3.28 (-1.54%)</td><td>0.10 (+2.00%)</td><td>7666.20 (+1.56%)</td><td>7379.52 (+0.40%)</td><td>7281.00 (-1.69%)</td><td>7189.60 (+1.87%)</td><td>219.52 (+5.17%)</td><td>2389.56 (-1.83%)</td><td>2329.68 (-0.40%)</td><td>2359.55 (+1.72%)</td><td>2240.98 (-1.54%)</td><td>68.55 (+2.00%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.57 (n/a)</td><td>3.43 (n/a)</td><td>3.40 (n/a)</td><td>3.33 (n/a)</td><td>0.10 (n/a)</td><td>7548.50 (n/a)</td><td>7349.78 (n/a)</td><td>7406.40 (n/a)</td><td>7057.80 (n/a)</td><td>208.74 (n/a)</td><td>2434.17 (n/a)</td><td>2339.00 (n/a)</td><td>2319.59 (n/a)</td><td>2275.93 (n/a)</td><td>67.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>2.97 (+4.51%)</td><td>2.81 (+0.54%)</td><td>2.81 (-0.30%)</td><td>2.69 (+0.18%)</td><td>0.11 <b>(+72.98%)</b></td><td>9347.90 (-0.18%)</td><td>8952.90 (-0.46%)</td><td>8955.20 (+0.30%)</td><td>8469.60 (-4.31%)</td><td>347.96 <b>(+64.79%)</b></td><td>2028.42 (+4.51%)</td><td>1921.26 (+0.54%)</td><td>1918.42 (-0.30%)</td><td>1837.84 (+0.18%)</td><td>75.46 <b>(+72.98%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>2.84 (n/a)</td><td>2.80 (n/a)</td><td>2.82 (n/a)</td><td>2.69 (n/a)</td><td>0.06 (n/a)</td><td>9364.80 (n/a)</td><td>8994.48 (n/a)</td><td>8928.30 (n/a)</td><td>8851.50 (n/a)</td><td>211.15 (n/a)</td><td>1940.90 (n/a)</td><td>1910.87 (n/a)</td><td>1924.20 (n/a)</td><td>1834.52 (n/a)</td><td>43.62 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>3.18 (-3.96%)</td><td>3.14 (-1.24%)</td><td>3.15 (-0.20%)</td><td>3.07 (-1.66%)</td><td>0.04 <b>(-41.87%)</b></td><td>8193.80 (+1.69%)</td><td>8005.64 (+1.23%)</td><td>7986.10 (+0.20%)</td><td>7913.80 (+4.13%)</td><td>112.83 <b>(-38.19%)</b></td><td>2170.87 (-3.96%)</td><td>2146.31 (-1.24%)</td><td>2151.22 (-0.20%)</td><td>2096.69 (-1.66%)</td><td>29.86 <b>(-41.87%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.31 (n/a)</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>3.12 (n/a)</td><td>0.08 (n/a)</td><td>8058.00 (n/a)</td><td>7908.20 (n/a)</td><td>7970.30 (n/a)</td><td>7600.20 (n/a)</td><td>182.54 (n/a)</td><td>2260.46 (n/a)</td><td>2173.36 (n/a)</td><td>2155.49 (n/a)</td><td>2132.01 (n/a)</td><td>51.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.78 (-0.23%)</td><td>0.78 (+0.01%)</td><td>0.78 (-0.01%)</td><td>0.78 (+0.17%)</td><td>0.00 <b>(-88.27%)</b></td><td>96491.40 (-0.17%)</td><td>96459.18 (-0.01%)</td><td>96451.10 (+0.01%)</td><td>96444.80 (+0.23%)</td><td>18.97 <b>(-88.26%)</b></td><td>712.53 (-0.23%)</td><td>712.42 (+0.01%)</td><td>712.48 (-0.01%)</td><td>712.18 (+0.17%)</td><td>0.14 <b>(-88.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96651.00 (n/a)</td><td>96464.64 (n/a)</td><td>96440.70 (n/a)</td><td>96224.00 (n/a)</td><td>161.63 (n/a)</td><td>714.16 (n/a)</td><td>712.38 (n/a)</td><td>712.56 (n/a)</td><td>711.01 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.73 (+0.35%)</td><td>0.73 (+0.16%)</td><td>0.73 (+0.06%)</td><td>0.73 (+0.20%)</td><td>0.00 <b>(+100.85%)</b></td><td>103635.70 (-0.20%)</td><td>103553.76 (-0.16%)</td><td>103626.20 (-0.06%)</td><td>103265.60 (-0.35%)</td><td>161.38 <b>(+99.74%)</b></td><td>665.46 (+0.35%)</td><td>663.61 (+0.16%)</td><td>663.15 (+0.06%)</td><td>663.09 (+0.20%)</td><td>1.04 <b>(+100.85%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103840.80 (n/a)</td><td>103715.18 (n/a)</td><td>103686.90 (n/a)</td><td>103627.60 (n/a)</td><td>80.79 (n/a)</td><td>663.14 (n/a)</td><td>662.58 (n/a)</td><td>662.76 (n/a)</td><td>661.78 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.69 (-0.05%)</td><td>0.69 (-0.03%)</td><td>0.69 (+0.10%)</td><td>0.69 (-0.28%)</td><td>0.00 <b>(+68.22%)</b></td><td>109864.30 (+0.28%)</td><td>109417.12 (+0.03%)</td><td>109279.10 (-0.10%)</td><td>109165.60 (+0.05%)</td><td>297.79 <b>(+68.77%)</b></td><td>629.50 (-0.05%)</td><td>628.05 (-0.03%)</td><td>628.84 (+0.10%)</td><td>625.49 (-0.28%)</td><td>1.71 <b>(+68.22%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109552.80 (n/a)</td><td>109385.24 (n/a)</td><td>109393.20 (n/a)</td><td>109110.30 (n/a)</td><td>176.45 (n/a)</td><td>629.82 (n/a)</td><td>628.23 (n/a)</td><td>628.19 (n/a)</td><td>627.27 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.26 (-4.86%)</td><td>6.91 (-5.72%)</td><td>7.09 (-3.12%)</td><td>6.26 (-11.78%)</td><td>0.39 <b>(+68.46%)</b></td><td>1423.10 (+13.35%)</td><td>1292.72 (+6.27%)</td><td>1257.30 (+3.22%)</td><td>1227.90 (+5.11%)</td><td>77.79 <b>(+101.42%)</b></td><td>437.22 (-4.86%)</td><td>416.44 (-5.72%)</td><td>427.01 (-3.12%)</td><td>377.24 (-11.78%)</td><td>23.72 <b>(+68.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.63 (n/a)</td><td>7.33 (n/a)</td><td>7.32 (n/a)</td><td>7.10 (n/a)</td><td>0.23 (n/a)</td><td>1255.50 (n/a)</td><td>1216.50 (n/a)</td><td>1218.10 (n/a)</td><td>1168.20 (n/a)</td><td>38.62 (n/a)</td><td>459.56 (n/a)</td><td>441.69 (n/a)</td><td>440.74 (n/a)</td><td>427.63 (n/a)</td><td>14.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.07 (-0.08%)</td><td>6.47 (-3.94%)</td><td>6.88 (+0.40%)</td><td>5.17 (-19.15%)</td><td>0.82 <b>(+187.32%)</b></td><td>1725.50 <b>(+23.68%)</b></td><td>1397.92 (+5.46%)</td><td>1296.20 (-0.40%)</td><td>1260.50 (+0.08%)</td><td>198.59 <b>(+251.74%)</b></td><td>425.93 (-0.08%)</td><td>389.64 (-3.94%)</td><td>414.19 (+0.40%)</td><td>311.14 (-19.15%)</td><td>49.34 <b>(+187.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.08 (n/a)</td><td>6.73 (n/a)</td><td>6.85 (n/a)</td><td>6.39 (n/a)</td><td>0.29 (n/a)</td><td>1395.10 (n/a)</td><td>1325.56 (n/a)</td><td>1301.40 (n/a)</td><td>1259.50 (n/a)</td><td>56.46 (n/a)</td><td>426.27 (n/a)</td><td>405.60 (n/a)</td><td>412.53 (n/a)</td><td>384.82 (n/a)</td><td>17.17 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>6.87 (+0.94%)</td><td>6.09 (+1.08%)</td><td>6.07 (-4.60%)</td><td>5.39 <b>(+28.85%)</b></td><td>0.53 <b>(-50.40%)</b></td><td>1652.70 <b>(-22.39%)</b></td><td>1473.18 (-3.60%)</td><td>1468.00 (+4.83%)</td><td>1297.00 (-0.92%)</td><td>126.09 <b>(-63.03%)</b></td><td>413.94 (+0.94%)</td><td>366.60 (+1.08%)</td><td>365.72 (-4.60%)</td><td>324.85 <b>(+28.85%)</b></td><td>31.68 <b>(-50.40%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>6.81 (n/a)</td><td>6.02 (n/a)</td><td>6.36 (n/a)</td><td>4.19 (n/a)</td><td>1.06 (n/a)</td><td>2129.50 (n/a)</td><td>1528.22 (n/a)</td><td>1400.40 (n/a)</td><td>1309.10 (n/a)</td><td>341.01 (n/a)</td><td>410.09 (n/a)</td><td>362.66 (n/a)</td><td>383.36 (n/a)</td><td>252.11 (n/a)</td><td>63.87 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.98 (-1.06%)</td><td>7.39 (-4.16%)</td><td>7.23 (-7.82%)</td><td>7.15 (+0.21%)</td><td>0.34 (-3.70%)</td><td>4876.60 (-0.21%)</td><td>4727.56 (+4.33%)</td><td>4822.90 (+8.48%)</td><td>4371.20 (+1.07%)</td><td>208.74 (-3.94%)</td><td>491.28 (-1.06%)</td><td>454.99 (-4.16%)</td><td>445.27 (-7.82%)</td><td>440.37 (+0.21%)</td><td>21.11 (-3.70%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.06 (n/a)</td><td>7.71 (n/a)</td><td>7.84 (n/a)</td><td>7.13 (n/a)</td><td>0.36 (n/a)</td><td>4887.00 (n/a)</td><td>4531.40 (n/a)</td><td>4445.80 (n/a)</td><td>4325.00 (n/a)</td><td>217.30 (n/a)</td><td>496.53 (n/a)</td><td>474.75 (n/a)</td><td>483.03 (n/a)</td><td>439.43 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.99 (+2.91%)</td><td>7.70 (+2.32%)</td><td>7.63 (+0.74%)</td><td>7.57 (+3.92%)</td><td>0.18 (-3.80%)</td><td>4608.60 (-3.77%)</td><td>4531.62 (-2.27%)</td><td>4569.50 (-0.74%)</td><td>4363.40 (-2.83%)</td><td>102.35 (-10.21%)</td><td>492.16 (+2.91%)</td><td>474.09 (+2.32%)</td><td>469.96 (+0.74%)</td><td>465.97 (+3.92%)</td><td>10.93 (-3.80%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.76 (n/a)</td><td>7.52 (n/a)</td><td>7.57 (n/a)</td><td>7.28 (n/a)</td><td>0.18 (n/a)</td><td>4789.30 (n/a)</td><td>4636.86 (n/a)</td><td>4603.50 (n/a)</td><td>4490.40 (n/a)</td><td>113.99 (n/a)</td><td>478.23 (n/a)</td><td>463.36 (n/a)</td><td>466.49 (n/a)</td><td>448.39 (n/a)</td><td>11.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.80 (-0.73%)</td><td>7.16 (-2.00%)</td><td>6.97 (-5.06%)</td><td>6.79 (+3.39%)</td><td>0.42 (-11.39%)</td><td>5138.50 (-3.28%)</td><td>4885.14 (+1.96%)</td><td>5004.10 (+5.33%)</td><td>4471.10 (+0.74%)</td><td>275.05 (-14.70%)</td><td>480.31 (-0.73%)</td><td>440.75 (-2.00%)</td><td>429.15 (-5.06%)</td><td>417.92 (+3.39%)</td><td>25.73 (-11.39%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.86 (n/a)</td><td>7.30 (n/a)</td><td>7.34 (n/a)</td><td>6.56 (n/a)</td><td>0.47 (n/a)</td><td>5312.80 (n/a)</td><td>4791.40 (n/a)</td><td>4750.80 (n/a)</td><td>4438.20 (n/a)</td><td>322.47 (n/a)</td><td>483.86 (n/a)</td><td>449.76 (n/a)</td><td>452.02 (n/a)</td><td>404.21 (n/a)</td><td>29.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.79 (+0.35%)</td><td>0.79 (+0.18%)</td><td>0.79 (+0.07%)</td><td>0.79 (-0.02%)</td><td>0.00 <b>(+202.57%)</b></td><td>95913.50 (+0.02%)</td><td>95635.72 (-0.18%)</td><td>95737.10 (-0.07%)</td><td>95386.00 (-0.35%)</td><td>235.00 <b>(+201.41%)</b></td><td>720.44 (+0.35%)</td><td>718.56 (+0.18%)</td><td>717.79 (+0.07%)</td><td>716.47 (-0.02%)</td><td>1.77 <b>(+202.58%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95889.60 (n/a)</td><td>95803.78 (n/a)</td><td>95805.70 (n/a)</td><td>95717.70 (n/a)</td><td>77.97 (n/a)</td><td>717.94 (n/a)</td><td>717.29 (n/a)</td><td>717.28 (n/a)</td><td>716.65 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.74 (-0.06%)</td><td>0.73 (-0.00%)</td><td>0.73 (-0.01%)</td><td>0.73 (+0.04%)</td><td>0.00 (-17.10%)</td><td>102930.40 (-0.04%)</td><td>102839.42 (+0.00%)</td><td>102915.10 (+0.01%)</td><td>102526.60 (+0.06%)</td><td>175.06 (-17.08%)</td><td>670.26 (-0.06%)</td><td>668.22 (-0.00%)</td><td>667.73 (-0.01%)</td><td>667.63 (+0.04%)</td><td>1.14 (-17.10%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102968.20 (n/a)</td><td>102836.82 (n/a)</td><td>102908.60 (n/a)</td><td>102461.80 (n/a)</td><td>211.11 (n/a)</td><td>670.68 (n/a)</td><td>668.24 (n/a)</td><td>667.77 (n/a)</td><td>667.39 (n/a)</td><td>1.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.70 (-0.02%)</td><td>0.70 (-0.04%)</td><td>0.70 (-0.02%)</td><td>0.70 (-0.08%)</td><td>0.00 (+15.42%)</td><td>108466.80 (+0.08%)</td><td>108152.72 (+0.04%)</td><td>108122.40 (+0.02%)</td><td>107990.40 (+0.02%)</td><td>186.13 (+15.56%)</td><td>636.35 (-0.02%)</td><td>635.39 (-0.04%)</td><td>635.57 (-0.02%)</td><td>633.55 (-0.08%)</td><td>1.09 (+15.41%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108374.80 (n/a)</td><td>108113.32 (n/a)</td><td>108099.00 (n/a)</td><td>107973.30 (n/a)</td><td>161.06 (n/a)</td><td>636.45 (n/a)</td><td>635.63 (n/a)</td><td>635.71 (n/a)</td><td>634.09 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>4.22 (-0.69%)</td><td>3.80 (-0.08%)</td><td>3.59 (-10.05%)</td><td>3.53 (+14.29%)</td><td>0.33 <b>(-31.35%)</b></td><td>2284.70 (-12.50%)</td><td>2133.26 (-0.72%)</td><td>2243.30 (+11.16%)</td><td>1909.80 (+0.70%)</td><td>178.08 <b>(-39.47%)</b></td><td>1106.91 (-0.69%)</td><td>996.69 (-0.08%)</td><td>942.32 (-10.05%)</td><td>925.26 (+14.29%)</td><td>86.05 <b>(-31.35%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>4.25 (n/a)</td><td>3.80 (n/a)</td><td>3.99 (n/a)</td><td>3.09 (n/a)</td><td>0.48 (n/a)</td><td>2611.20 (n/a)</td><td>2148.68 (n/a)</td><td>2018.00 (n/a)</td><td>1896.60 (n/a)</td><td>294.23 (n/a)</td><td>1114.58 (n/a)</td><td>997.51 (n/a)</td><td>1047.55 (n/a)</td><td>809.57 (n/a)</td><td>125.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.43 (+14.19%)</td><td>0.37 (+6.77%)</td><td>0.35 (+7.21%)</td><td>0.33 (+4.52%)</td><td>0.04 <b>(+57.74%)</b></td><td>3733.30 (-4.32%)</td><td>3435.20 (-5.95%)</td><td>3508.30 (-6.73%)</td><td>2872.90 (-12.42%)</td><td>327.91 <b>(+29.23%)</b></td><td>23.36 (+14.19%)</td><td>19.70 (+6.77%)</td><td>19.13 (+7.21%)</td><td>17.98 (+4.52%)</td><td>2.10 <b>(+57.74%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.02 (n/a)</td><td>3901.90 (n/a)</td><td>3652.48 (n/a)</td><td>3761.30 (n/a)</td><td>3280.50 (n/a)</td><td>253.74 (n/a)</td><td>20.46 (n/a)</td><td>18.45 (n/a)</td><td>17.84 (n/a)</td><td>17.20 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.16 (+7.01%)</td><td>4.31 (-8.35%)</td><td>4.69 (-2.36%)</td><td>3.22 <b>(-26.86%)</b></td><td>0.81 <b>(+359.80%)</b></td><td>2064.40 <b>(+36.72%)</b></td><td>1590.98 (+12.43%)</td><td>1417.50 (+2.42%)</td><td>1289.30 (-6.55%)</td><td>326.13 <b>(+489.67%)</b></td><td>1594.03 (+7.01%)</td><td>1332.63 (-8.35%)</td><td>1449.90 (-2.36%)</td><td>995.54 <b>(-26.86%)</b></td><td>250.51 <b>(+359.80%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>4.82 (n/a)</td><td>4.71 (n/a)</td><td>4.81 (n/a)</td><td>4.41 (n/a)</td><td>0.18 (n/a)</td><td>1510.00 (n/a)</td><td>1415.08 (n/a)</td><td>1384.00 (n/a)</td><td>1379.60 (n/a)</td><td>55.31 (n/a)</td><td>1489.67 (n/a)</td><td>1454.06 (n/a)</td><td>1484.99 (n/a)</td><td>1361.10 (n/a)</td><td>54.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (+19.18%)</td><td>0.20 (+7.21%)</td><td>0.20 (+2.60%)</td><td>0.15 (+10.12%)</td><td>0.04 <b>(+26.27%)</b></td><td>0.27 (+19.18%)</td><td>0.20 (+7.21%)</td><td>0.20 (+2.60%)</td><td>0.15 (+10.12%)</td><td>0.04 <b>(+26.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.49 (-0.21%)</td><td>12.84 (-0.94%)</td><td>13.23 (+3.07%)</td><td>11.07 (-12.23%)</td><td>1.00 <b>(+156.44%)</b></td><td>13.48 (-0.21%)</td><td>12.83 (-0.94%)</td><td>13.22 (+3.07%)</td><td>11.07 (-12.23%)</td><td>1.00 <b>(+156.44%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>13.52 (n/a)</td><td>12.96 (n/a)</td><td>12.84 (n/a)</td><td>12.62 (n/a)</td><td>0.39 (n/a)</td><td>13.51 (n/a)</td><td>12.95 (n/a)</td><td>12.83 (n/a)</td><td>12.61 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>24.94 (+0.19%)</td><td>24.45 (-0.09%)</td><td>24.48 (+0.44%)</td><td>24.01 (-1.00%)</td><td>0.34 <b>(+32.73%)</b></td><td>24.92 (+0.19%)</td><td>24.44 (-0.09%)</td><td>24.47 (+0.44%)</td><td>24.00 (-1.00%)</td><td>0.34 <b>(+32.73%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>24.89 (n/a)</td><td>24.47 (n/a)</td><td>24.38 (n/a)</td><td>24.25 (n/a)</td><td>0.26 (n/a)</td><td>24.87 (n/a)</td><td>24.46 (n/a)</td><td>24.36 (n/a)</td><td>24.24 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>42.46 (+3.88%)</td><td>41.35 (+3.92%)</td><td>42.31 (+4.95%)</td><td>39.06 (+6.50%)</td><td>1.53 (-13.06%)</td><td>42.43 (+3.88%)</td><td>41.32 (+3.92%)</td><td>42.29 (+4.95%)</td><td>39.04 (+6.50%)</td><td>1.53 (-13.06%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>40.87 (n/a)</td><td>39.79 (n/a)</td><td>40.32 (n/a)</td><td>36.68 (n/a)</td><td>1.76 (n/a)</td><td>40.85 (n/a)</td><td>39.76 (n/a)</td><td>40.29 (n/a)</td><td>36.66 (n/a)</td><td>1.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>45.26 (+0.80%)</td><td>40.98 (-4.15%)</td><td>44.23 (+5.11%)</td><td>26.16 <b>(-36.03%)</b></td><td>8.30 <b>(+406.95%)</b></td><td>45.24 (+0.80%)</td><td>40.96 (-4.15%)</td><td>44.21 (+5.11%)</td><td>26.14 <b>(-36.03%)</b></td><td>8.30 <b>(+406.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>44.90 (n/a)</td><td>42.76 (n/a)</td><td>42.08 (n/a)</td><td>40.90 (n/a)</td><td>1.64 (n/a)</td><td>44.88 (n/a)</td><td>42.73 (n/a)</td><td>42.06 (n/a)</td><td>40.87 (n/a)</td><td>1.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.64 (+1.69%)</td><td>11.83 (-4.93%)</td><td>11.15 (-9.74%)</td><td>10.83 (-2.80%)</td><td>1.24 <b>(+34.27%)</b></td><td>13.63 (+1.69%)</td><td>11.82 (-4.93%)</td><td>11.14 (-9.74%)</td><td>10.82 (-2.80%)</td><td>1.24 <b>(+34.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>13.41 (n/a)</td><td>12.44 (n/a)</td><td>12.35 (n/a)</td><td>11.14 (n/a)</td><td>0.92 (n/a)</td><td>13.40 (n/a)</td><td>12.43 (n/a)</td><td>12.34 (n/a)</td><td>11.14 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>24.98 (-0.25%)</td><td>24.48 (+3.37%)</td><td>24.49 (-0.26%)</td><td>24.00 (+19.87%)</td><td>0.35 <b>(-83.22%)</b></td><td>24.96 (-0.25%)</td><td>24.47 (+3.37%)</td><td>24.47 (-0.26%)</td><td>23.98 (+19.87%)</td><td>0.35 <b>(-83.22%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>25.04 (n/a)</td><td>23.68 (n/a)</td><td>24.55 (n/a)</td><td>20.02 (n/a)</td><td>2.10 (n/a)</td><td>25.03 (n/a)</td><td>23.67 (n/a)</td><td>24.53 (n/a)</td><td>20.01 (n/a)</td><td>2.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>40.47 (-3.14%)</td><td>39.89 (+0.78%)</td><td>40.01 (+1.80%)</td><td>39.24 (+5.83%)</td><td>0.46 <b>(-76.54%)</b></td><td>40.45 (-3.14%)</td><td>39.87 (+0.78%)</td><td>39.98 (+1.80%)</td><td>39.22 (+5.83%)</td><td>0.46 <b>(-76.54%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>41.78 (n/a)</td><td>39.58 (n/a)</td><td>39.30 (n/a)</td><td>37.08 (n/a)</td><td>1.96 (n/a)</td><td>41.75 (n/a)</td><td>39.56 (n/a)</td><td>39.27 (n/a)</td><td>37.06 (n/a)</td><td>1.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>46.08 (-3.98%)</td><td>43.70 (-0.95%)</td><td>42.57 (-3.23%)</td><td>41.83 (+2.73%)</td><td>2.16 (-16.53%)</td><td>46.05 (-3.98%)</td><td>43.67 (-0.95%)</td><td>42.55 (-3.23%)</td><td>41.80 (+2.73%)</td><td>2.16 (-16.53%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>47.99 (n/a)</td><td>44.12 (n/a)</td><td>43.99 (n/a)</td><td>40.71 (n/a)</td><td>2.58 (n/a)</td><td>47.96 (n/a)</td><td>44.09 (n/a)</td><td>43.97 (n/a)</td><td>40.69 (n/a)</td><td>2.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>167.30 (n/a)</td><td>172.60 (n/a)</td><td>131.10 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>169.04 (n/a)</td><td>152.90 (n/a)</td><td>117.60 (n/a)</td><td>42.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>174.46 (n/a)</td><td>189.00 (n/a)</td><td>112.30 (n/a)</td><td>37.29 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>173.92 (n/a)</td><td>168.30 (n/a)</td><td>145.00 (n/a)</td><td>28.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>168.02 (n/a)</td><td>159.00 (n/a)</td><td>115.80 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>173.88 (n/a)</td><td>182.60 (n/a)</td><td>128.00 (n/a)</td><td>45.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.00 (n/a)</td><td>175.08 (n/a)</td><td>173.90 (n/a)</td><td>165.50 (n/a)</td><td>9.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.30 (n/a)</td><td>195.38 (n/a)</td><td>187.20 (n/a)</td><td>165.10 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.40 (n/a)</td><td>185.62 (n/a)</td><td>159.50 (n/a)</td><td>129.80 (n/a)</td><td>64.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>143.48 (n/a)</td><td>126.00 (n/a)</td><td>115.40 (n/a)</td><td>29.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>176.74 (n/a)</td><td>183.40 (n/a)</td><td>125.40 (n/a)</td><td>34.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>173.00 (n/a)</td><td>162.40 (n/a)</td><td>136.30 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>302.70 (n/a)</td><td>168.78 (n/a)</td><td>147.30 (n/a)</td><td>116.00 (n/a)</td><td>76.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.90 (n/a)</td><td>197.62 (n/a)</td><td>179.90 (n/a)</td><td>158.50 (n/a)</td><td>48.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>169.92 (n/a)</td><td>158.00 (n/a)</td><td>138.20 (n/a)</td><td>30.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>271.30 (n/a)</td><td>195.32 (n/a)</td><td>186.00 (n/a)</td><td>156.70 (n/a)</td><td>44.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.70 (n/a)</td><td>153.54 (n/a)</td><td>145.30 (n/a)</td><td>132.30 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.90 (n/a)</td><td>153.98 (n/a)</td><td>154.80 (n/a)</td><td>131.10 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.00 (n/a)</td><td>156.62 (n/a)</td><td>154.60 (n/a)</td><td>130.30 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>166.88 (n/a)</td><td>164.70 (n/a)</td><td>129.80 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>177.02 (n/a)</td><td>168.50 (n/a)</td><td>147.60 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.70 (n/a)</td><td>185.46 (n/a)</td><td>195.80 (n/a)</td><td>141.60 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>173.62 (n/a)</td><td>181.00 (n/a)</td><td>148.90 (n/a)</td><td>15.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>265.90 (n/a)</td><td>195.32 (n/a)</td><td>177.20 (n/a)</td><td>142.90 (n/a)</td><td>51.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (-16.30%)</td><td>0.18 (-3.65%)</td><td>0.19 (-0.82%)</td><td>0.16 (+11.00%)</td><td>0.01 <b>(-62.33%)</b></td><td>202.70 (-9.91%)</td><td>183.98 (+1.59%)</td><td>175.80 (+0.86%)</td><td>173.60 (+19.48%)</td><td>13.04 <b>(-59.90%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.00 (n/a)</td><td>181.10 (n/a)</td><td>174.30 (n/a)</td><td>145.30 (n/a)</td><td>32.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>272.70 (n/a)</td><td>195.10 (n/a)</td><td>183.60 (n/a)</td><td>128.30 (n/a)</td><td>66.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.90 (n/a)</td><td>181.14 (n/a)</td><td>165.60 (n/a)</td><td>156.20 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>187.70 (n/a)</td><td>171.02 (n/a)</td><td>166.50 (n/a)</td><td>161.70 (n/a)</td><td>10.61 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>209.60 (n/a)</td><td>155.90 (n/a)</td><td>144.70 (n/a)</td><td>129.90 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>270.50 (n/a)</td><td>189.70 (n/a)</td><td>191.50 (n/a)</td><td>137.60 (n/a)</td><td>51.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.30 (n/a)</td><td>179.44 (n/a)</td><td>170.70 (n/a)</td><td>161.60 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>256.80 (n/a)</td><td>212.72 (n/a)</td><td>199.20 (n/a)</td><td>190.90 (n/a)</td><td>26.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 <b>(+36.21%)</b></td><td>0.03 <b>(+29.68%)</b></td><td>0.03 <b>(+41.41%)</b></td><td>0.02 <b>(+26.85%)</b></td><td>0.01 <b>(+38.44%)</b></td><td>173.80 <b>(-21.14%)</b></td><td>146.38 <b>(-22.71%)</b></td><td>145.90 <b>(-29.28%)</b></td><td>107.70 <b>(-26.58%)</b></td><td>25.53 <b>(-21.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.40 (n/a)</td><td>189.40 (n/a)</td><td>206.30 (n/a)</td><td>146.70 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+14.63%)</td><td>0.02 (+5.25%)</td><td>0.02 (+12.44%)</td><td>0.02 (+3.09%)</td><td>0.01 <b>(+25.96%)</b></td><td>212.70 (-3.01%)</td><td>178.46 (-4.15%)</td><td>172.90 (-11.06%)</td><td>126.00 (-12.74%)</td><td>35.34 (+6.67%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.30 (n/a)</td><td>186.18 (n/a)</td><td>194.40 (n/a)</td><td>144.40 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+13.26%)</td><td>0.03 (+12.95%)</td><td>0.02 (+3.70%)</td><td>0.02 (+19.04%)</td><td>0.01 (+16.18%)</td><td>210.50 (-16.00%)</td><td>168.78 (-11.30%)</td><td>169.30 (-3.59%)</td><td>113.00 (-11.72%)</td><td>41.94 (-11.46%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.60 (n/a)</td><td>190.28 (n/a)</td><td>175.60 (n/a)</td><td>128.00 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+19.35%)</td><td>0.02 (+4.64%)</td><td>0.02 (+7.65%)</td><td>0.02 (-1.36%)</td><td>0.00 <b>(+74.77%)</b></td><td>219.70 (+1.38%)</td><td>183.20 (-2.89%)</td><td>179.80 (-7.08%)</td><td>135.60 (-16.24%)</td><td>31.46 <b>(+46.40%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>188.66 (n/a)</td><td>193.50 (n/a)</td><td>161.90 (n/a)</td><td>21.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-11.90%)</td><td>0.02 (-12.72%)</td><td>0.02 <b>(-23.21%)</b></td><td>0.02 (-13.47%)</td><td>0.01 (+4.10%)</td><td>239.10 (+15.56%)</td><td>201.70 (+15.93%)</td><td>225.60 <b>(+30.18%)</b></td><td>149.10 (+13.47%)</td><td>44.18 <b>(+33.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.90 (n/a)</td><td>173.98 (n/a)</td><td>173.30 (n/a)</td><td>131.40 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 <b>(+23.27%)</b></td><td>0.02 (+0.63%)</td><td>0.02 (+0.65%)</td><td>0.02 (-8.23%)</td><td>0.01 <b>(+105.21%)</b></td><td>261.00 (+8.98%)</td><td>210.06 (+2.66%)</td><td>206.80 (-0.67%)</td><td>140.30 (-18.85%)</td><td>45.83 <b>(+77.56%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.50 (n/a)</td><td>204.62 (n/a)</td><td>208.20 (n/a)</td><td>172.90 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-4.57%)</td><td>0.02 (-11.36%)</td><td>0.02 <b>(-22.29%)</b></td><td>0.02 (+5.50%)</td><td>0.00 <b>(-22.99%)</b></td><td>224.40 (-5.20%)</td><td>195.64 (+11.26%)</td><td>201.40 <b>(+28.69%)</b></td><td>151.40 (+4.85%)</td><td>30.33 <b>(-22.45%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.70 (n/a)</td><td>175.84 (n/a)</td><td>156.50 (n/a)</td><td>144.40 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (-4.77%)</td><td>0.02 (-3.26%)</td><td>0.02 (-13.93%)</td><td>0.01 (+1.24%)</td><td>0.00 (-12.78%)</td><td>327.60 (-1.24%)</td><td>256.44 (+1.96%)</td><td>255.00 (+16.17%)</td><td>182.60 (+5.00%)</td><td>59.10 (-12.78%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>331.70 (n/a)</td><td>251.50 (n/a)</td><td>219.50 (n/a)</td><td>173.90 (n/a)</td><td>67.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (-14.69%)</td><td>0.04 (-8.66%)</td><td>0.05 (+0.09%)</td><td>0.04 (-0.63%)</td><td>0.01 <b>(-32.27%)</b></td><td>215.50 (+0.65%)</td><td>188.06 (+8.39%)</td><td>177.00 (-0.11%)</td><td>159.40 (+17.29%)</td><td>24.34 (-17.68%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>173.50 (n/a)</td><td>177.20 (n/a)</td><td>135.90 (n/a)</td><td>29.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+3.44%)</td><td>0.05 (-2.59%)</td><td>0.04 (-3.43%)</td><td>0.04 (+0.13%)</td><td>0.01 (+14.30%)</td><td>215.60 (-0.09%)</td><td>180.68 (+3.47%)</td><td>183.60 (+3.55%)</td><td>137.00 (-3.39%)</td><td>35.66 (+15.57%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>174.62 (n/a)</td><td>177.30 (n/a)</td><td>141.80 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (-12.23%)</td><td>0.05 (-3.35%)</td><td>0.05 (+2.58%)</td><td>0.04 (-12.09%)</td><td>0.01 (-1.22%)</td><td>226.20 (+13.78%)</td><td>175.98 (+4.23%)</td><td>172.10 (-2.55%)</td><td>140.20 (+13.89%)</td><td>36.51 <b>(+30.68%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>168.84 (n/a)</td><td>176.60 (n/a)</td><td>123.10 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (+2.29%)</td><td>0.04 (+14.99%)</td><td>0.04 <b>(+22.42%)</b></td><td>0.03 <b>(+34.38%)</b></td><td>0.01 <b>(-30.96%)</b></td><td>277.70 <b>(-25.59%)</b></td><td>208.00 (-19.07%)</td><td>187.90 (-18.30%)</td><td>159.10 (-2.27%)</td><td>48.48 <b>(-49.71%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>373.20 (n/a)</td><td>257.00 (n/a)</td><td>230.00 (n/a)</td><td>162.80 (n/a)</td><td>96.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (-5.04%)</td><td>0.05 (-8.47%)</td><td>0.05 (+1.41%)</td><td>0.02 <b>(-31.58%)</b></td><td>0.01 <b>(+25.47%)</b></td><td>330.00 <b>(+46.15%)</b></td><td>193.10 (+15.46%)</td><td>163.20 (-1.39%)</td><td>142.00 (+5.34%)</td><td>77.45 <b>(+109.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>167.24 (n/a)</td><td>165.50 (n/a)</td><td>134.80 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+0.53%)</td><td>0.05 (+4.76%)</td><td>0.04 (+6.03%)</td><td>0.04 (+14.42%)</td><td>0.01 (-18.04%)</td><td>206.40 (-12.62%)</td><td>182.22 (-5.85%)</td><td>193.60 (-5.70%)</td><td>139.20 (-0.57%)</td><td>26.39 <b>(-28.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>193.54 (n/a)</td><td>205.30 (n/a)</td><td>140.00 (n/a)</td><td>37.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (-6.76%)</td><td>0.04 (-10.82%)</td><td>0.04 (-12.79%)</td><td>0.03 (-13.01%)</td><td>0.01 (-1.28%)</td><td>283.20 (+14.94%)</td><td>200.44 (+12.87%)</td><td>186.70 (+14.68%)</td><td>150.90 (+7.25%)</td><td>49.32 <b>(+21.71%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.40 (n/a)</td><td>177.58 (n/a)</td><td>162.80 (n/a)</td><td>140.70 (n/a)</td><td>40.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(-28.37%)</b></td><td>0.04 (-12.81%)</td><td>0.04 (-11.60%)</td><td>0.03 (-10.70%)</td><td>0.00 <b>(-56.56%)</b></td><td>239.60 (+11.96%)</td><td>200.82 (+12.30%)</td><td>197.60 (+13.11%)</td><td>181.10 <b>(+39.63%)</b></td><td>22.87 <b>(-30.13%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>178.82 (n/a)</td><td>174.70 (n/a)</td><td>129.70 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 <b>(-28.90%)</b></td><td>0.04 (-15.63%)</td><td>0.04 (-11.68%)</td><td>0.04 (+6.06%)</td><td>0.00 <b>(-89.69%)</b></td><td>208.80 (-5.73%)</td><td>203.98 (+15.78%)</td><td>205.30 (+13.18%)</td><td>198.70 <b>(+40.62%)</b></td><td>4.20 <b>(-86.34%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>176.18 (n/a)</td><td>181.40 (n/a)</td><td>141.30 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (-13.18%)</td><td>0.04 (-7.45%)</td><td>0.03 (-8.39%)</td><td>0.03 (-2.94%)</td><td>0.00 <b>(-43.99%)</b></td><td>238.10 (+3.03%)</td><td>229.10 (+7.52%)</td><td>237.00 (+9.17%)</td><td>206.80 (+15.14%)</td><td>13.51 <b>(-32.03%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>213.08 (n/a)</td><td>217.10 (n/a)</td><td>179.60 (n/a)</td><td>19.87 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+3.00%)</td><td>0.10 (-0.89%)</td><td>0.10 (+1.72%)</td><td>0.07 <b>(-20.36%)</b></td><td>0.03 <b>(+47.27%)</b></td><td>241.90 <b>(+25.53%)</b></td><td>176.90 (+4.85%)</td><td>166.90 (-1.65%)</td><td>122.20 (-2.86%)</td><td>49.36 <b>(+80.94%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>168.72 (n/a)</td><td>169.70 (n/a)</td><td>125.80 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 <b>(-20.56%)</b></td><td>0.10 (-2.06%)</td><td>0.10 (+11.50%)</td><td>0.09 (+6.79%)</td><td>0.01 <b>(-65.79%)</b></td><td>191.10 (-6.37%)</td><td>172.58 (-0.36%)</td><td>166.80 (-10.27%)</td><td>160.60 <b>(+25.86%)</b></td><td>12.49 <b>(-59.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>173.20 (n/a)</td><td>185.90 (n/a)</td><td>127.60 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(-26.73%)</b></td><td>0.08 (-13.56%)</td><td>0.08 (-2.39%)</td><td>0.08 (+16.23%)</td><td>0.01 <b>(-78.55%)</b></td><td>207.50 (-13.97%)</td><td>198.32 (+9.36%)</td><td>204.20 (+2.46%)</td><td>177.20 <b>(+36.52%)</b></td><td>12.70 <b>(-73.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>241.20 (n/a)</td><td>181.34 (n/a)</td><td>199.30 (n/a)</td><td>129.80 (n/a)</td><td>48.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (-12.03%)</td><td>0.09 (-9.14%)</td><td>0.08 (+0.54%)</td><td>0.08 (+5.02%)</td><td>0.01 <b>(-42.40%)</b></td><td>212.20 (-4.76%)</td><td>193.16 (+6.45%)</td><td>204.20 (-0.54%)</td><td>146.60 (+13.73%)</td><td>27.24 <b>(-37.98%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>222.80 (n/a)</td><td>181.46 (n/a)</td><td>205.30 (n/a)</td><td>128.90 (n/a)</td><td>43.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (-9.27%)</td><td>0.09 (-9.16%)</td><td>0.09 (+5.52%)</td><td>0.05 <b>(-39.94%)</b></td><td>0.02 <b>(+21.68%)</b></td><td>340.80 <b>(+66.49%)</b></td><td>202.08 (+16.55%)</td><td>175.10 (-5.25%)</td><td>142.30 (+10.22%)</td><td>79.16 <b>(+137.85%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>173.38 (n/a)</td><td>184.80 (n/a)</td><td>129.10 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (-0.05%)</td><td>0.08 (-15.08%)</td><td>0.08 (-18.18%)</td><td>0.05 <b>(-32.51%)</b></td><td>0.02 <b>(+85.48%)</b></td><td>305.10 <b>(+48.18%)</b></td><td>210.54 <b>(+22.58%)</b></td><td>200.70 <b>(+22.23%)</b></td><td>157.00 (+0.06%)</td><td>56.99 <b>(+182.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>171.76 (n/a)</td><td>164.20 (n/a)</td><td>156.90 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(-28.90%)</b></td><td>0.08 (-17.93%)</td><td>0.08 (-13.52%)</td><td>0.06 <b>(-20.17%)</b></td><td>0.01 <b>(-34.80%)</b></td><td>283.20 <b>(+25.25%)</b></td><td>213.68 <b>(+21.07%)</b></td><td>198.60 (+15.67%)</td><td>192.70 <b>(+40.66%)</b></td><td>38.99 (+15.80%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.10 (n/a)</td><td>176.50 (n/a)</td><td>171.70 (n/a)</td><td>137.00 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (-7.66%)</td><td>0.07 (-15.47%)</td><td>0.07 (-10.10%)</td><td>0.04 (-18.86%)</td><td>0.02 (+18.04%)</td><td>382.80 <b>(+23.25%)</b></td><td>272.14 <b>(+22.60%)</b></td><td>235.80 (+11.23%)</td><td>183.60 (+8.25%)</td><td>86.33 <b>(+58.75%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>310.60 (n/a)</td><td>221.98 (n/a)</td><td>212.00 (n/a)</td><td>169.60 (n/a)</td><td>54.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (-4.43%)</td><td>0.17 (-1.21%)</td><td>0.17 (-2.50%)</td><td>0.16 (+4.74%)</td><td>0.02 <b>(-21.15%)</b></td><td>208.10 (-4.54%)</td><td>189.80 (+0.82%)</td><td>193.10 (+2.60%)</td><td>163.70 (+4.67%)</td><td>17.35 <b>(-20.80%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.00 (n/a)</td><td>188.26 (n/a)</td><td>188.20 (n/a)</td><td>156.40 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (-6.35%)</td><td>0.19 (-4.67%)</td><td>0.19 (-1.99%)</td><td>0.16 (-5.98%)</td><td>0.02 <b>(-28.99%)</b></td><td>206.70 (+6.33%)</td><td>174.78 (+3.89%)</td><td>176.90 (+2.02%)</td><td>146.10 (+6.80%)</td><td>21.90 <b>(-20.03%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.40 (n/a)</td><td>168.24 (n/a)</td><td>173.40 (n/a)</td><td>136.80 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (-0.20%)</td><td>0.19 (-0.38%)</td><td>0.19 (+9.86%)</td><td>0.14 (-12.91%)</td><td>0.04 <b>(+29.30%)</b></td><td>236.10 (+14.83%)</td><td>182.62 (+2.49%)</td><td>173.40 (-8.98%)</td><td>138.50 (+0.22%)</td><td>43.23 <b>(+48.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.60 (n/a)</td><td>178.18 (n/a)</td><td>190.50 (n/a)</td><td>138.20 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (-10.78%)</td><td>0.18 (-10.74%)</td><td>0.18 (-16.57%)</td><td>0.13 (+4.38%)</td><td>0.03 <b>(-27.24%)</b></td><td>245.00 (-4.22%)</td><td>191.36 (+9.42%)</td><td>185.10 (+19.81%)</td><td>147.90 (+12.05%)</td><td>37.84 <b>(-23.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>255.80 (n/a)</td><td>174.88 (n/a)</td><td>154.50 (n/a)</td><td>132.00 (n/a)</td><td>49.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 <b>(+26.09%)</b></td><td>0.17 (+14.65%)</td><td>0.15 (-3.84%)</td><td>0.15 <b>(+43.35%)</b></td><td>0.03 (-5.12%)</td><td>216.00 <b>(-30.23%)</b></td><td>197.40 (-14.18%)</td><td>212.40 (+3.96%)</td><td>153.40 <b>(-20.68%)</b></td><td>26.76 <b>(-46.48%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>309.60 (n/a)</td><td>230.02 (n/a)</td><td>204.30 (n/a)</td><td>193.40 (n/a)</td><td>49.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (-6.31%)</td><td>0.17 (-0.67%)</td><td>0.18 (+8.33%)</td><td>0.15 (+1.98%)</td><td>0.02 <b>(-34.38%)</b></td><td>215.00 (-1.92%)</td><td>189.34 (-0.22%)</td><td>186.00 (-7.69%)</td><td>170.40 (+6.70%)</td><td>18.79 <b>(-30.05%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.20 (n/a)</td><td>189.76 (n/a)</td><td>201.50 (n/a)</td><td>159.70 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (+9.33%)</td><td>0.15 (+11.24%)</td><td>0.16 <b>(+30.31%)</b></td><td>0.09 (-12.40%)</td><td>0.04 <b>(+25.63%)</b></td><td>380.00 (+14.15%)</td><td>238.40 (-7.02%)</td><td>207.20 <b>(-23.26%)</b></td><td>162.10 (-8.52%)</td><td>84.62 <b>(+39.19%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>332.90 (n/a)</td><td>256.40 (n/a)</td><td>270.00 (n/a)</td><td>177.20 (n/a)</td><td>60.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-0.95%)</td><td>0.02 (-3.23%)</td><td>0.02 (-8.11%)</td><td>0.02 (+12.20%)</td><td>0.00 (-7.90%)</td><td>225.10 (-10.85%)</td><td>182.18 (+2.26%)</td><td>187.10 (+8.78%)</td><td>142.30 (+0.99%)</td><td>35.48 (-19.99%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.50 (n/a)</td><td>178.16 (n/a)</td><td>172.00 (n/a)</td><td>140.90 (n/a)</td><td>44.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+8.79%)</td><td>0.02 (+0.75%)</td><td>0.02 (-2.97%)</td><td>0.02 (+10.74%)</td><td>0.00 (+3.81%)</td><td>211.70 (-9.72%)</td><td>172.00 (-1.10%)</td><td>168.40 (+3.06%)</td><td>135.50 (-8.14%)</td><td>29.78 (-15.48%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.50 (n/a)</td><td>173.92 (n/a)</td><td>163.40 (n/a)</td><td>147.50 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 <b>(+30.60%)</b></td><td>0.02 (+14.96%)</td><td>0.02 (+7.99%)</td><td>0.02 (+12.51%)</td><td>0.00 <b>(+77.26%)</b></td><td>233.00 (-11.10%)</td><td>195.70 (-11.93%)</td><td>202.40 (-7.37%)</td><td>146.50 <b>(-23.42%)</b></td><td>31.96 (+16.87%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>262.10 (n/a)</td><td>222.20 (n/a)</td><td>218.50 (n/a)</td><td>191.30 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 <b>(-23.52%)</b></td><td>0.02 (-1.49%)</td><td>0.02 (+7.14%)</td><td>0.02 (+5.58%)</td><td>0.00 <b>(-54.67%)</b></td><td>226.00 (-5.28%)</td><td>201.58 (-1.96%)</td><td>206.20 (-6.65%)</td><td>171.30 <b>(+30.76%)</b></td><td>25.28 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.60 (n/a)</td><td>205.62 (n/a)</td><td>220.90 (n/a)</td><td>131.00 (n/a)</td><td>43.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+18.78%)</td><td>0.03 (+4.72%)</td><td>0.02 (-2.04%)</td><td>0.02 (-3.99%)</td><td>0.01 <b>(+50.59%)</b></td><td>236.20 (+4.14%)</td><td>169.24 (-2.41%)</td><td>164.70 (+2.11%)</td><td>121.80 (-15.83%)</td><td>41.84 <b>(+31.10%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.80 (n/a)</td><td>173.42 (n/a)</td><td>161.30 (n/a)</td><td>144.70 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+12.91%)</td><td>0.02 (-2.29%)</td><td>0.02 (+1.05%)</td><td>0.02 <b>(-21.46%)</b></td><td>0.01 <b>(+89.97%)</b></td><td>235.40 <b>(+27.31%)</b></td><td>179.68 (+9.00%)</td><td>174.30 (-1.02%)</td><td>110.80 (-11.43%)</td><td>55.10 <b>(+128.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>164.84 (n/a)</td><td>176.10 (n/a)</td><td>125.10 (n/a)</td><td>24.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+10.47%)</td><td>0.03 (+10.87%)</td><td>0.02 (+4.48%)</td><td>0.02 (+19.52%)</td><td>0.01 (-8.47%)</td><td>208.70 (-16.32%)</td><td>167.30 (-12.45%)</td><td>184.90 (-4.30%)</td><td>113.70 (-9.47%)</td><td>38.72 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>191.08 (n/a)</td><td>193.20 (n/a)</td><td>125.60 (n/a)</td><td>57.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-13.66%)</td><td>0.02 (-9.79%)</td><td>0.03 (+1.89%)</td><td>0.01 <b>(-30.62%)</b></td><td>0.01 <b>(+21.40%)</b></td><td>288.20 <b>(+44.17%)</b></td><td>185.94 (+14.85%)</td><td>163.20 (-1.86%)</td><td>147.70 (+15.84%)</td><td>57.88 <b>(+114.04%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>161.90 (n/a)</td><td>166.30 (n/a)</td><td>127.50 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 <b>(+21.83%)</b></td><td>0.03 <b>(+26.25%)</b></td><td>0.03 <b>(+46.66%)</b></td><td>0.02 (+19.98%)</td><td>0.01 <b>(+56.10%)</b></td><td>187.30 (-16.64%)</td><td>151.18 (-19.68%)</td><td>130.80 <b>(-31.84%)</b></td><td>124.60 (-17.92%)</td><td>32.01 (+9.36%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.70 (n/a)</td><td>188.22 (n/a)</td><td>191.90 (n/a)</td><td>151.80 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-19.12%)</td><td>0.02 (-8.13%)</td><td>0.02 (+3.36%)</td><td>0.02 (+6.64%)</td><td>0.00 <b>(-57.11%)</b></td><td>203.30 (-6.23%)</td><td>178.74 (+5.02%)</td><td>180.20 (-3.22%)</td><td>149.40 <b>(+23.57%)</b></td><td>19.48 <b>(-50.17%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>170.20 (n/a)</td><td>186.20 (n/a)</td><td>120.90 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 <b>(-29.26%)</b></td><td>0.02 (-8.39%)</td><td>0.02 (+15.60%)</td><td>0.01 <b>(-29.56%)</b></td><td>0.01 <b>(-25.64%)</b></td><td>372.80 <b>(+41.96%)</b></td><td>216.02 (+10.67%)</td><td>176.70 (-13.51%)</td><td>167.60 <b>(+41.43%)</b></td><td>88.21 <b>(+55.89%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>262.60 (n/a)</td><td>195.20 (n/a)</td><td>204.30 (n/a)</td><td>118.50 (n/a)</td><td>56.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+0.23%)</td><td>0.03 (+2.74%)</td><td>0.03 (+19.94%)</td><td>0.02 (+9.47%)</td><td>0.00 <b>(-26.34%)</b></td><td>184.10 (-8.64%)</td><td>158.10 (-4.64%)</td><td>150.60 (-16.61%)</td><td>123.50 (-0.16%)</td><td>25.79 <b>(-29.97%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>165.80 (n/a)</td><td>180.60 (n/a)</td><td>123.70 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (+5.58%)</td><td>0.02 (-0.27%)</td><td>0.02 (-7.90%)</td><td>0.02 (+9.72%)</td><td>0.00 (-6.34%)</td><td>218.00 (-8.86%)</td><td>199.64 (-0.04%)</td><td>209.20 (+8.62%)</td><td>166.90 (-5.33%)</td><td>22.27 (-17.10%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.20 (n/a)</td><td>199.72 (n/a)</td><td>192.60 (n/a)</td><td>176.30 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (+2.08%)</td><td>0.03 (+4.72%)</td><td>0.02 (-3.28%)</td><td>0.02 (-0.40%)</td><td>0.01 <b>(+31.34%)</b></td><td>223.10 (+0.41%)</td><td>169.88 (-0.82%)</td><td>180.60 (+3.44%)</td><td>110.50 (-2.04%)</td><td>53.96 <b>(+31.52%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>171.28 (n/a)</td><td>174.60 (n/a)</td><td>112.80 (n/a)</td><td>41.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+19.75%)</td><td>0.02 (-1.84%)</td><td>0.02 (-15.21%)</td><td>0.02 (-13.44%)</td><td>0.01 <b>(+66.59%)</b></td><td>250.90 (+15.52%)</td><td>186.26 (+5.17%)</td><td>189.80 (+17.89%)</td><td>128.70 (-16.54%)</td><td>46.73 <b>(+61.56%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>177.10 (n/a)</td><td>161.00 (n/a)</td><td>154.20 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 <b>(+44.82%)</b></td><td>0.03 (+9.91%)</td><td>0.02 (+2.34%)</td><td>0.02 (-8.01%)</td><td>0.01 <b>(+256.41%)</b></td><td>206.80 (+8.67%)</td><td>166.14 (-4.94%)</td><td>169.50 (-2.31%)</td><td>106.90 <b>(-30.99%)</b></td><td>36.89 <b>(+151.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>174.78 (n/a)</td><td>173.50 (n/a)</td><td>154.90 (n/a)</td><td>14.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+1.68%)</td><td>0.05 (-6.01%)</td><td>0.06 (+13.87%)</td><td>0.02 <b>(-43.69%)</b></td><td>0.02 <b>(+86.60%)</b></td><td>335.00 <b>(+77.62%)</b></td><td>185.64 (+17.87%)</td><td>143.60 (-12.17%)</td><td>127.90 (-1.69%)</td><td>86.16 <b>(+244.86%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>157.50 (n/a)</td><td>163.50 (n/a)</td><td>130.10 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (+0.42%)</td><td>0.05 (-8.56%)</td><td>0.05 (-15.59%)</td><td>0.04 (-8.57%)</td><td>0.01 <b>(+29.85%)</b></td><td>201.70 (+9.38%)</td><td>168.48 (+10.92%)</td><td>171.50 (+18.44%)</td><td>125.30 (-0.40%)</td><td>31.91 <b>(+41.72%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>151.90 (n/a)</td><td>144.80 (n/a)</td><td>125.80 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(+21.88%)</b></td><td>0.04 (+8.51%)</td><td>0.04 (+3.76%)</td><td>0.04 (+3.38%)</td><td>0.00 <b>(+195.86%)</b></td><td>231.60 (-3.26%)</td><td>212.74 (-7.15%)</td><td>221.70 (-3.61%)</td><td>177.20 (-17.96%)</td><td>21.25 <b>(+131.59%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.40 (n/a)</td><td>229.12 (n/a)</td><td>230.00 (n/a)</td><td>216.00 (n/a)</td><td>9.17 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 <b>(+31.86%)</b></td><td>0.04 (+12.22%)</td><td>0.04 (+6.58%)</td><td>0.03 (+9.40%)</td><td>0.01 <b>(+69.92%)</b></td><td>235.20 (-8.59%)</td><td>191.74 (-9.08%)</td><td>184.00 (-6.17%)</td><td>132.50 <b>(-24.16%)</b></td><td>40.88 (+16.71%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.30 (n/a)</td><td>210.88 (n/a)</td><td>196.10 (n/a)</td><td>174.70 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+4.22%)</td><td>0.05 (+6.28%)</td><td>0.05 (-0.81%)</td><td>0.05 <b>(+21.47%)</b></td><td>0.00 <b>(-48.72%)</b></td><td>170.40 (-17.68%)</td><td>159.42 (-6.82%)</td><td>160.30 (+0.82%)</td><td>146.30 (-4.00%)</td><td>8.90 <b>(-60.03%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>171.08 (n/a)</td><td>159.00 (n/a)</td><td>152.40 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 <b>(-21.26%)</b></td><td>0.05 <b>(-20.56%)</b></td><td>0.05 (-10.55%)</td><td>0.03 <b>(-28.72%)</b></td><td>0.01 (+1.70%)</td><td>239.20 <b>(+40.29%)</b></td><td>179.50 <b>(+28.60%)</b></td><td>158.60 (+11.85%)</td><td>136.20 <b>(+26.93%)</b></td><td>44.23 <b>(+85.68%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.50 (n/a)</td><td>139.58 (n/a)</td><td>141.80 (n/a)</td><td>107.30 (n/a)</td><td>23.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (-12.98%)</td><td>0.05 (-10.23%)</td><td>0.05 (-9.25%)</td><td>0.04 (-2.59%)</td><td>0.01 <b>(-26.10%)</b></td><td>182.50 (+2.64%)</td><td>162.72 (+10.74%)</td><td>160.00 (+10.19%)</td><td>135.60 (+14.92%)</td><td>18.84 (-11.88%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.80 (n/a)</td><td>146.94 (n/a)</td><td>145.20 (n/a)</td><td>118.00 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (-6.27%)</td><td>0.05 (-7.82%)</td><td>0.06 (+3.52%)</td><td>0.04 (-12.63%)</td><td>0.01 (+8.94%)</td><td>233.30 (+14.47%)</td><td>164.20 (+10.41%)</td><td>142.20 (-3.40%)</td><td>121.70 (+6.75%)</td><td>46.10 <b>(+33.01%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>148.72 (n/a)</td><td>147.20 (n/a)</td><td>114.00 (n/a)</td><td>34.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+1.61%)</td><td>0.04 (-11.85%)</td><td>0.04 (-8.76%)</td><td>0.03 <b>(-26.07%)</b></td><td>0.01 <b>(+135.01%)</b></td><td>240.20 <b>(+35.25%)</b></td><td>191.02 (+16.69%)</td><td>184.60 (+9.62%)</td><td>146.80 (-1.61%)</td><td>38.59 <b>(+217.58%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.60 (n/a)</td><td>163.70 (n/a)</td><td>168.40 (n/a)</td><td>149.20 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (-1.71%)</td><td>0.05 (-7.28%)</td><td>0.05 (-3.43%)</td><td>0.03 <b>(-29.89%)</b></td><td>0.01 <b>(+99.12%)</b></td><td>243.10 <b>(+42.58%)</b></td><td>170.14 (+12.02%)</td><td>161.10 (+3.53%)</td><td>132.20 (+1.69%)</td><td>44.21 <b>(+195.31%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.50 (n/a)</td><td>151.88 (n/a)</td><td>155.60 (n/a)</td><td>130.00 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+1.56%)</td><td>0.05 (-11.55%)</td><td>0.05 (-8.83%)</td><td>0.03 (-19.64%)</td><td>0.01 <b>(+63.16%)</b></td><td>246.70 <b>(+24.41%)</b></td><td>184.54 (+16.43%)</td><td>164.60 (+9.66%)</td><td>141.80 (-1.53%)</td><td>44.31 <b>(+97.23%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>158.50 (n/a)</td><td>150.10 (n/a)</td><td>144.00 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+13.74%)</td><td>0.04 (-15.28%)</td><td>0.04 <b>(-24.67%)</b></td><td>0.04 (-19.69%)</td><td>0.01 <b>(+132.65%)</b></td><td>227.00 <b>(+24.52%)</b></td><td>194.04 <b>(+22.04%)</b></td><td>200.80 <b>(+32.72%)</b></td><td>129.00 (-12.13%)</td><td>38.44 <b>(+148.05%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.30 (n/a)</td><td>159.00 (n/a)</td><td>151.30 (n/a)</td><td>146.80 (n/a)</td><td>15.50 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (-4.59%)</td><td>0.04 (-7.52%)</td><td>0.04 (+0.45%)</td><td>0.03 (-17.35%)</td><td>0.01 <b>(+50.75%)</b></td><td>250.50 <b>(+20.96%)</b></td><td>202.84 (+10.48%)</td><td>190.30 (-0.47%)</td><td>161.50 (+4.80%)</td><td>41.41 <b>(+95.25%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>183.60 (n/a)</td><td>191.20 (n/a)</td><td>154.10 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+10.09%)</td><td>0.04 <b>(-22.47%)</b></td><td>0.04 <b>(-30.16%)</b></td><td>0.02 <b>(-43.61%)</b></td><td>0.01 <b>(+101.63%)</b></td><td>371.50 <b>(+77.33%)</b></td><td>227.98 <b>(+41.15%)</b></td><td>216.20 <b>(+43.18%)</b></td><td>131.90 (-9.16%)</td><td>87.94 <b>(+225.21%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>161.52 (n/a)</td><td>151.00 (n/a)</td><td>145.20 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (+0.58%)</td><td>0.04 (-0.31%)</td><td>0.04 (-5.18%)</td><td>0.04 (+7.50%)</td><td>0.01 (-7.62%)</td><td>228.70 (-6.99%)</td><td>196.70 (-0.15%)</td><td>200.20 (+5.48%)</td><td>158.50 (-0.56%)</td><td>28.16 (-15.40%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.90 (n/a)</td><td>197.00 (n/a)</td><td>189.80 (n/a)</td><td>159.40 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(+20.83%)</b></td><td>0.04 (-3.71%)</td><td>0.04 (-6.40%)</td><td>0.02 <b>(-49.41%)</b></td><td>0.01 <b>(+714.14%)</b></td><td>391.00 <b>(+97.67%)</b></td><td>224.28 (+16.70%)</td><td>210.90 (+6.84%)</td><td>152.30 (-17.23%)</td><td>97.98 <b>(+1219.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.80 (n/a)</td><td>192.18 (n/a)</td><td>197.40 (n/a)</td><td>184.00 (n/a)</td><td>7.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+9.99%)</td><td>0.10 (+4.48%)</td><td>0.09 (-7.23%)</td><td>0.09 (+1.46%)</td><td>0.02 <b>(+65.09%)</b></td><td>192.70 (-1.43%)</td><td>161.82 (-2.24%)</td><td>177.70 (+7.76%)</td><td>121.80 (-9.04%)</td><td>32.72 <b>(+49.77%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>165.52 (n/a)</td><td>164.90 (n/a)</td><td>133.90 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (+10.06%)</td><td>0.10 (+6.24%)</td><td>0.11 (+14.04%)</td><td>0.07 (-10.08%)</td><td>0.02 <b>(+61.73%)</b></td><td>233.40 (+11.20%)</td><td>164.54 (-3.38%)</td><td>148.60 (-12.28%)</td><td>133.10 (-9.15%)</td><td>41.27 <b>(+64.35%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>170.30 (n/a)</td><td>169.40 (n/a)</td><td>146.50 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (-8.41%)</td><td>0.09 (+7.17%)</td><td>0.09 <b>(+21.18%)</b></td><td>0.07 (+2.49%)</td><td>0.01 <b>(-33.64%)</b></td><td>227.60 (-2.40%)</td><td>190.22 (-7.64%)</td><td>181.40 (-17.51%)</td><td>174.30 (+9.14%)</td><td>21.72 <b>(-27.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>205.96 (n/a)</td><td>219.90 (n/a)</td><td>159.70 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 <b>(+24.67%)</b></td><td>0.09 (+15.68%)</td><td>0.09 (+9.76%)</td><td>0.08 (+14.27%)</td><td>0.01 <b>(+76.20%)</b></td><td>200.00 (-12.47%)</td><td>175.42 (-12.87%)</td><td>181.80 (-8.92%)</td><td>145.80 (-19.80%)</td><td>23.16 <b>(+23.83%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>201.34 (n/a)</td><td>199.60 (n/a)</td><td>181.80 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (-11.92%)</td><td>0.09 (-11.26%)</td><td>0.10 (-9.21%)</td><td>0.06 (-19.54%)</td><td>0.02 (+1.47%)</td><td>253.30 <b>(+24.29%)</b></td><td>179.98 (+14.07%)</td><td>159.90 (+10.12%)</td><td>147.50 (+13.55%)</td><td>43.69 <b>(+44.14%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>157.78 (n/a)</td><td>145.20 (n/a)</td><td>129.90 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (-6.01%)</td><td>0.12 (+3.84%)</td><td>0.12 (+10.51%)</td><td>0.10 (+17.30%)</td><td>0.02 (-17.48%)</td><td>171.50 (-14.76%)</td><td>142.96 (-5.00%)</td><td>133.70 (-9.54%)</td><td>119.50 (+6.41%)</td><td>24.97 <b>(-24.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.20 (n/a)</td><td>150.48 (n/a)</td><td>147.80 (n/a)</td><td>112.30 (n/a)</td><td>33.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (+15.80%)</td><td>0.11 (+8.51%)</td><td>0.11 (+5.69%)</td><td>0.09 (-1.12%)</td><td>0.02 <b>(+89.37%)</b></td><td>187.10 (+1.14%)</td><td>149.76 (-6.33%)</td><td>150.60 (-5.40%)</td><td>121.10 (-13.62%)</td><td>26.39 <b>(+62.10%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>159.88 (n/a)</td><td>159.20 (n/a)</td><td>140.20 (n/a)</td><td>16.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (-10.38%)</td><td>0.11 (-0.87%)</td><td>0.11 (-2.88%)</td><td>0.10 (+1.57%)</td><td>0.02 <b>(-25.83%)</b></td><td>168.60 (-1.58%)</td><td>145.74 (-0.25%)</td><td>149.40 (+2.96%)</td><td>119.30 (+11.60%)</td><td>21.17 (-18.60%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>171.30 (n/a)</td><td>146.10 (n/a)</td><td>145.10 (n/a)</td><td>106.90 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+2.39%)</td><td>0.11 (+12.64%)</td><td>0.11 (+13.68%)</td><td>0.09 (+14.18%)</td><td>0.01 (-19.92%)</td><td>189.00 (-12.42%)</td><td>155.90 (-12.28%)</td><td>155.70 (-12.03%)</td><td>127.40 (-2.30%)</td><td>22.06 <b>(-29.40%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.80 (n/a)</td><td>177.72 (n/a)</td><td>177.00 (n/a)</td><td>130.40 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+1.32%)</td><td>0.11 (+15.09%)</td><td>0.12 <b>(+21.50%)</b></td><td>0.08 (+1.40%)</td><td>0.02 (-0.80%)</td><td>207.30 (-1.38%)</td><td>150.64 (-13.19%)</td><td>139.10 (-17.69%)</td><td>128.70 (-1.30%)</td><td>32.42 (-3.19%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.20 (n/a)</td><td>173.52 (n/a)</td><td>169.00 (n/a)</td><td>130.40 (n/a)</td><td>33.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (+5.69%)</td><td>0.11 (+4.98%)</td><td>0.11 (+2.56%)</td><td>0.09 (+11.90%)</td><td>0.01 (-12.45%)</td><td>176.20 (-10.65%)</td><td>155.28 (-5.26%)</td><td>152.30 (-2.50%)</td><td>133.20 (-5.40%)</td><td>17.49 <b>(-25.44%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>163.90 (n/a)</td><td>156.20 (n/a)</td><td>140.80 (n/a)</td><td>23.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+9.87%)</td><td>0.12 <b>(+20.97%)</b></td><td>0.12 <b>(+30.99%)</b></td><td>0.09 (+19.91%)</td><td>0.02 (-0.86%)</td><td>173.00 (-16.59%)</td><td>142.64 (-17.71%)</td><td>136.30 <b>(-23.64%)</b></td><td>121.50 (-8.92%)</td><td>20.92 <b>(-23.03%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.40 (n/a)</td><td>173.34 (n/a)</td><td>178.50 (n/a)</td><td>133.40 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 <b>(+23.16%)</b></td><td>0.11 <b>(+24.92%)</b></td><td>0.12 <b>(+27.46%)</b></td><td>0.10 <b>(+24.07%)</b></td><td>0.01 <b>(+21.84%)</b></td><td>170.10 (-19.38%)</td><td>146.12 (-19.96%)</td><td>139.40 <b>(-21.55%)</b></td><td>131.90 (-18.83%)</td><td>15.16 (-19.90%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>182.56 (n/a)</td><td>177.70 (n/a)</td><td>162.50 (n/a)</td><td>18.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-3.71%)</td><td>0.11 (+11.94%)</td><td>0.10 (+11.93%)</td><td>0.09 (+18.01%)</td><td>0.02 <b>(-21.30%)</b></td><td>184.00 (-15.29%)</td><td>152.96 (-12.00%)</td><td>158.90 (-10.68%)</td><td>128.70 (+3.87%)</td><td>23.35 <b>(-30.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.20 (n/a)</td><td>173.82 (n/a)</td><td>177.90 (n/a)</td><td>123.90 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+4.10%)</td><td>0.11 (+9.49%)</td><td>0.10 (+9.26%)</td><td>0.09 <b>(+20.07%)</b></td><td>0.01 <b>(-25.57%)</b></td><td>179.60 (-16.74%)</td><td>157.14 (-9.95%)</td><td>158.80 (-8.47%)</td><td>129.40 (-3.93%)</td><td>17.92 <b>(-41.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.70 (n/a)</td><td>174.50 (n/a)</td><td>173.50 (n/a)</td><td>134.70 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-0.70%)</td><td>0.11 (+8.65%)</td><td>0.12 (+16.37%)</td><td>0.07 (-1.76%)</td><td>0.02 (+9.62%)</td><td>235.20 (+1.77%)</td><td>158.20 (-6.97%)</td><td>140.40 (-14.02%)</td><td>125.30 (+0.64%)</td><td>44.33 (+15.31%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.10 (n/a)</td><td>170.06 (n/a)</td><td>163.30 (n/a)</td><td>124.50 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (-5.80%)</td><td>0.21 (+7.88%)</td><td>0.21 (+14.48%)</td><td>0.18 (+12.34%)</td><td>0.02 <b>(-38.84%)</b></td><td>181.10 (-10.96%)</td><td>155.70 (-8.69%)</td><td>154.30 (-12.68%)</td><td>139.50 (+6.16%)</td><td>16.44 <b>(-41.55%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.40 (n/a)</td><td>170.52 (n/a)</td><td>176.70 (n/a)</td><td>131.40 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 (-2.75%)</td><td>0.20 (-8.71%)</td><td>0.21 (-2.83%)</td><td>0.14 <b>(-20.27%)</b></td><td>0.04 <b>(+34.30%)</b></td><td>230.40 <b>(+25.42%)</b></td><td>167.86 (+12.19%)</td><td>153.40 (+2.88%)</td><td>125.20 (+2.88%)</td><td>40.12 <b>(+75.86%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.70 (n/a)</td><td>149.62 (n/a)</td><td>149.10 (n/a)</td><td>121.70 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (+18.78%)</td><td>0.15 (+11.19%)</td><td>0.16 (+12.89%)</td><td>0.14 (+7.48%)</td><td>0.01 <b>(+145.01%)</b></td><td>232.60 (-6.96%)</td><td>212.88 (-9.57%)</td><td>208.80 (-11.41%)</td><td>186.80 (-15.82%)</td><td>19.47 <b>(+94.65%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>250.00 (n/a)</td><td>235.42 (n/a)</td><td>235.70 (n/a)</td><td>221.90 (n/a)</td><td>10.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (-0.30%)</td><td>0.17 (-4.94%)</td><td>0.17 (-6.01%)</td><td>0.14 (-5.28%)</td><td>0.02 (+2.42%)</td><td>231.70 (+5.61%)</td><td>199.50 (+5.39%)</td><td>187.50 (+6.41%)</td><td>165.30 (+0.30%)</td><td>28.96 (+9.91%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.40 (n/a)</td><td>189.30 (n/a)</td><td>176.20 (n/a)</td><td>164.80 (n/a)</td><td>26.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (+3.00%)</td><td>0.18 (-9.41%)</td><td>0.18 (-3.96%)</td><td>0.10 <b>(-34.26%)</b></td><td>0.05 <b>(+64.09%)</b></td><td>317.40 <b>(+52.08%)</b></td><td>202.68 (+17.26%)</td><td>184.10 (+4.13%)</td><td>131.40 (-2.88%)</td><td>69.35 <b>(+154.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.70 (n/a)</td><td>172.84 (n/a)</td><td>176.80 (n/a)</td><td>135.30 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (+3.04%)</td><td>0.17 (-15.19%)</td><td>0.18 (-4.93%)</td><td>0.09 <b>(-47.39%)</b></td><td>0.06 <b>(+110.19%)</b></td><td>385.10 <b>(+90.08%)</b></td><td>224.22 <b>(+32.17%)</b></td><td>177.30 (+5.16%)</td><td>140.30 (-2.97%)</td><td>99.92 <b>(+301.68%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>202.60 (n/a)</td><td>169.64 (n/a)</td><td>168.60 (n/a)</td><td>144.60 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 <b>(+28.63%)</b></td><td>0.23 (+16.40%)</td><td>0.22 (+16.33%)</td><td>0.19 (+7.09%)</td><td>0.04 <b>(+71.12%)</b></td><td>175.60 (-6.65%)</td><td>146.94 (-13.00%)</td><td>149.10 (-14.06%)</td><td>114.80 <b>(-22.27%)</b></td><td>25.04 <b>(+25.38%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.10 (n/a)</td><td>168.90 (n/a)</td><td>173.50 (n/a)</td><td>147.70 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (+10.06%)</td><td>0.20 (-3.62%)</td><td>0.19 (-9.69%)</td><td>0.18 (-7.63%)</td><td>0.03 <b>(+133.54%)</b></td><td>184.90 (+8.26%)</td><td>163.78 (+5.27%)</td><td>169.20 (+10.73%)</td><td>130.30 (-9.14%)</td><td>23.50 <b>(+131.26%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>170.80 (n/a)</td><td>155.58 (n/a)</td><td>152.80 (n/a)</td><td>143.40 (n/a)</td><td>10.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (-1.34%)</td><td>0.21 (-2.95%)</td><td>0.20 (+5.07%)</td><td>0.17 (-6.29%)</td><td>0.04 (-10.11%)</td><td>194.90 (+6.68%)</td><td>160.00 (+2.51%)</td><td>160.90 (-4.85%)</td><td>119.40 (+1.36%)</td><td>27.23 (-6.26%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>182.70 (n/a)</td><td>156.08 (n/a)</td><td>169.10 (n/a)</td><td>117.80 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (-5.49%)</td><td>0.20 (-5.13%)</td><td>0.19 (-5.66%)</td><td>0.17 (-11.53%)</td><td>0.02 <b>(+36.86%)</b></td><td>194.60 (+13.01%)</td><td>168.32 (+5.84%)</td><td>168.90 (+5.96%)</td><td>151.90 (+5.78%)</td><td>16.98 <b>(+64.50%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>159.04 (n/a)</td><td>159.40 (n/a)</td><td>143.60 (n/a)</td><td>10.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 <b>(+24.16%)</b></td><td>0.19 (-4.03%)</td><td>0.18 (-7.36%)</td><td>0.14 <b>(-25.31%)</b></td><td>0.05 <b>(+243.68%)</b></td><td>236.40 <b>(+33.86%)</b></td><td>179.18 (+8.41%)</td><td>180.60 (+7.95%)</td><td>123.30 (-19.46%)</td><td>40.26 <b>(+262.51%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>176.60 (n/a)</td><td>165.28 (n/a)</td><td>167.30 (n/a)</td><td>153.10 (n/a)</td><td>11.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.28 (+1.68%)</td><td>0.19 (-13.99%)</td><td>0.18 (-11.93%)</td><td>0.12 <b>(-33.14%)</b></td><td>0.06 <b>(+59.89%)</b></td><td>269.20 <b>(+49.56%)</b></td><td>189.82 <b>(+22.91%)</b></td><td>185.30 (+13.54%)</td><td>116.60 (-1.60%)</td><td>56.93 <b>(+134.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.00 (n/a)</td><td>154.44 (n/a)</td><td>163.20 (n/a)</td><td>118.50 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (+4.19%)</td><td>0.18 (-8.09%)</td><td>0.18 (-11.79%)</td><td>0.15 (-18.60%)</td><td>0.03 <b>(+192.77%)</b></td><td>215.40 <b>(+22.88%)</b></td><td>182.44 (+10.85%)</td><td>186.10 (+13.41%)</td><td>148.90 (-4.00%)</td><td>28.79 <b>(+244.26%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>175.30 (n/a)</td><td>164.58 (n/a)</td><td>164.10 (n/a)</td><td>155.10 (n/a)</td><td>8.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (+13.35%)</td><td>0.19 (+0.55%)</td><td>0.17 (-5.17%)</td><td>0.13 (-17.42%)</td><td>0.05 <b>(+128.34%)</b></td><td>247.40 <b>(+21.10%)</b></td><td>186.34 (+4.22%)</td><td>189.20 (+5.40%)</td><td>134.40 (-11.81%)</td><td>49.28 <b>(+136.68%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.30 (n/a)</td><td>178.80 (n/a)</td><td>179.50 (n/a)</td><td>152.40 (n/a)</td><td>20.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (-9.34%)</td><td>0.18 (-7.17%)</td><td>0.17 (-6.35%)</td><td>0.14 (-6.18%)</td><td>0.03 (-14.47%)</td><td>232.90 (+6.59%)</td><td>185.64 (+7.38%)</td><td>188.10 (+6.75%)</td><td>154.00 (+10.32%)</td><td>30.50 (+0.80%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>218.50 (n/a)</td><td>172.88 (n/a)</td><td>176.20 (n/a)</td><td>139.60 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (+13.01%)</td><td>0.20 (+14.37%)</td><td>0.20 (+11.95%)</td><td>0.17 (+10.44%)</td><td>0.02 (+5.72%)</td><td>193.60 (-9.49%)</td><td>164.70 (-12.69%)</td><td>167.10 (-10.69%)</td><td>141.60 (-11.50%)</td><td>19.46 (-16.35%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.90 (n/a)</td><td>188.64 (n/a)</td><td>187.10 (n/a)</td><td>160.00 (n/a)</td><td>23.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (+0.13%)</td><td>0.21 (+0.12%)</td><td>0.21 (+0.22%)</td><td>0.20 (-0.13%)</td><td>0.00 <b>(+116.05%)</b></td><td>41013.10 (+0.13%)</td><td>40867.64 (-0.12%)</td><td>40828.60 (-0.22%)</td><td>40807.80 (-0.13%)</td><td>83.64 <b>(+115.91%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40958.10 (n/a)</td><td>40915.30 (n/a)</td><td>40918.30 (n/a)</td><td>40860.30 (n/a)</td><td>38.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (-0.02%)</td><td>0.21 (-0.01%)</td><td>0.21 (+0.10%)</td><td>0.20 (-0.12%)</td><td>0.00 <b>(+32.40%)</b></td><td>40933.30 (+0.12%)</td><td>40841.94 (+0.01%)</td><td>40817.50 (-0.09%)</td><td>40786.30 (+0.02%)</td><td>61.85 <b>(+32.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40883.90 (n/a)</td><td>40838.70 (n/a)</td><td>40856.30 (n/a)</td><td>40779.70 (n/a)</td><td>46.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+0.07%)</td><td>0.13 (+0.12%)</td><td>0.13 (+0.10%)</td><td>0.13 (+0.20%)</td><td>0.00 <b>(-54.57%)</b></td><td>321919.60 (-0.20%)</td><td>321754.58 (-0.12%)</td><td>321678.70 (-0.10%)</td><td>321643.20 (-0.07%)</td><td>128.77 <b>(-54.73%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>322554.50 (n/a)</td><td>322126.10 (n/a)</td><td>321997.90 (n/a)</td><td>321880.20 (n/a)</td><td>284.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-4.44%)</td><td>0.02 (-4.24%)</td><td>0.02 (+4.00%)</td><td>0.02 (-13.03%)</td><td>0.01 (-6.07%)</td><td>236.00 (+14.95%)</td><td>173.80 (+4.72%)</td><td>171.80 (-3.86%)</td><td>131.30 (+4.70%)</td><td>38.78 (+17.29%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>165.96 (n/a)</td><td>178.70 (n/a)</td><td>125.40 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (-13.55%)</td><td>0.03 (-17.21%)</td><td>0.03 <b>(-21.26%)</b></td><td>0.02 <b>(-22.44%)</b></td><td>0.01 (-13.53%)</td><td>275.90 <b>(+28.93%)</b></td><td>203.44 <b>(+21.08%)</b></td><td>193.10 <b>(+26.96%)</b></td><td>143.20 (+15.67%)</td><td>48.31 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>168.02 (n/a)</td><td>152.10 (n/a)</td><td>123.80 (n/a)</td><td>38.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+10.00%)</td><td>0.02 (+1.85%)</td><td>0.02 (-5.75%)</td><td>0.02 (-8.19%)</td><td>0.00 <b>(+35.98%)</b></td><td>234.80 (+8.91%)</td><td>181.50 (-0.58%)</td><td>182.40 (+6.11%)</td><td>143.90 (-9.10%)</td><td>35.02 <b>(+34.50%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.60 (n/a)</td><td>182.56 (n/a)</td><td>171.90 (n/a)</td><td>158.30 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-3.03%)</td><td>0.03 (-4.68%)</td><td>0.03 (-2.51%)</td><td>0.03 (-4.34%)</td><td>0.00 (-19.77%)</td><td>204.00 (+4.56%)</td><td>180.60 (+4.50%)</td><td>177.40 (+2.60%)</td><td>155.20 (+3.12%)</td><td>19.15 (-12.95%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>172.82 (n/a)</td><td>172.90 (n/a)</td><td>150.50 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 <b>(-20.95%)</b></td><td>0.02 (-8.59%)</td><td>0.02 (-1.78%)</td><td>0.02 (+0.52%)</td><td>0.00 <b>(-30.39%)</b></td><td>207.30 (-0.53%)</td><td>171.86 (+7.72%)</td><td>165.80 (+1.84%)</td><td>138.30 <b>(+26.42%)</b></td><td>32.72 (-8.93%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>159.54 (n/a)</td><td>162.80 (n/a)</td><td>109.40 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 <b>(-20.11%)</b></td><td>0.03 <b>(-25.98%)</b></td><td>0.03 <b>(-27.75%)</b></td><td>0.02 <b>(-27.08%)</b></td><td>0.00 (-10.02%)</td><td>233.60 <b>(+37.17%)</b></td><td>183.54 <b>(+35.94%)</b></td><td>173.00 <b>(+38.40%)</b></td><td>152.70 <b>(+25.16%)</b></td><td>31.66 <b>(+55.56%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>170.30 (n/a)</td><td>135.02 (n/a)</td><td>125.00 (n/a)</td><td>122.00 (n/a)</td><td>20.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (-15.10%)</td><td>0.02 (-11.20%)</td><td>0.02 (-7.80%)</td><td>0.02 (-7.09%)</td><td>0.00 <b>(-29.64%)</b></td><td>229.80 (+7.63%)</td><td>202.82 (+11.78%)</td><td>206.60 (+8.45%)</td><td>175.20 (+17.82%)</td><td>25.73 (-10.02%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.50 (n/a)</td><td>181.44 (n/a)</td><td>190.50 (n/a)</td><td>148.70 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-6.66%)</td><td>0.03 (-1.54%)</td><td>0.03 (+3.61%)</td><td>0.02 (-2.58%)</td><td>0.01 (-5.89%)</td><td>219.00 (+2.67%)</td><td>168.60 (+1.47%)</td><td>154.90 (-3.49%)</td><td>137.00 (+7.11%)</td><td>35.37 (+2.46%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>166.16 (n/a)</td><td>160.50 (n/a)</td><td>127.90 (n/a)</td><td>34.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+18.26%)</td><td>0.03 (+8.50%)</td><td>0.02 (+3.56%)</td><td>0.02 (-12.84%)</td><td>0.01 <b>(+92.41%)</b></td><td>223.50 (+14.73%)</td><td>166.74 (-4.92%)</td><td>171.00 (-3.44%)</td><td>120.10 (-15.42%)</td><td>38.99 <b>(+87.56%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>175.36 (n/a)</td><td>177.10 (n/a)</td><td>142.00 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 <b>(-23.34%)</b></td><td>0.03 (-10.22%)</td><td>0.03 (-2.22%)</td><td>0.02 (-15.26%)</td><td>0.00 <b>(-37.09%)</b></td><td>217.00 (+18.00%)</td><td>174.68 (+9.93%)</td><td>174.00 (+2.23%)</td><td>142.70 <b>(+30.44%)</b></td><td>29.31 (-0.73%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>158.90 (n/a)</td><td>170.20 (n/a)</td><td>109.40 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+15.02%)</td><td>0.02 (+2.10%)</td><td>0.02 (+2.18%)</td><td>0.02 <b>(-20.38%)</b></td><td>0.01 <b>(+205.52%)</b></td><td>235.80 <b>(+25.56%)</b></td><td>179.44 (+1.45%)</td><td>179.50 (-2.13%)</td><td>139.00 (-13.02%)</td><td>40.18 <b>(+222.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.80 (n/a)</td><td>176.88 (n/a)</td><td>183.40 (n/a)</td><td>159.80 (n/a)</td><td>12.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-3.33%)</td><td>0.02 (+5.41%)</td><td>0.02 (-1.93%)</td><td>0.02 <b>(+29.44%)</b></td><td>0.00 <b>(-42.00%)</b></td><td>208.70 <b>(-22.76%)</b></td><td>187.66 (-7.54%)</td><td>193.90 (+2.00%)</td><td>163.70 (+3.48%)</td><td>20.16 <b>(-54.42%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.20 (n/a)</td><td>202.96 (n/a)</td><td>190.10 (n/a)</td><td>158.20 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (-3.92%)</td><td>0.02 (+6.01%)</td><td>0.02 (+12.93%)</td><td>0.02 (+6.27%)</td><td>0.00 <b>(-36.26%)</b></td><td>205.00 (-5.92%)</td><td>173.04 (-6.73%)</td><td>167.10 (-11.45%)</td><td>159.80 (+4.10%)</td><td>18.25 <b>(-35.94%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.90 (n/a)</td><td>185.52 (n/a)</td><td>188.70 (n/a)</td><td>153.50 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (+8.58%)</td><td>0.02 (+8.94%)</td><td>0.02 (+11.78%)</td><td>0.02 (+9.99%)</td><td>0.00 (-5.52%)</td><td>209.00 (-9.09%)</td><td>180.88 (-8.77%)</td><td>183.70 (-10.56%)</td><td>143.50 (-7.89%)</td><td>24.58 <b>(-22.96%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.90 (n/a)</td><td>198.26 (n/a)</td><td>205.40 (n/a)</td><td>155.80 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (+4.92%)</td><td>0.02 (+3.06%)</td><td>0.02 (-0.00%)</td><td>0.02 <b>(+24.08%)</b></td><td>0.00 <b>(-25.56%)</b></td><td>262.30 (-19.42%)</td><td>220.48 (-4.96%)</td><td>216.00 (+0.00%)</td><td>180.70 (-4.69%)</td><td>29.34 <b>(-45.47%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>325.50 (n/a)</td><td>231.98 (n/a)</td><td>216.00 (n/a)</td><td>189.60 (n/a)</td><td>53.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (-1.15%)</td><td>0.05 (+1.17%)</td><td>0.06 (-4.64%)</td><td>0.04 (+3.97%)</td><td>0.01 (-12.70%)</td><td>216.80 (-3.82%)</td><td>160.18 (-2.09%)</td><td>147.10 (+4.85%)</td><td>135.60 (+1.12%)</td><td>33.42 (-13.61%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.40 (n/a)</td><td>163.60 (n/a)</td><td>140.30 (n/a)</td><td>134.10 (n/a)</td><td>38.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (+5.31%)</td><td>0.08 (+3.10%)</td><td>0.07 (-7.15%)</td><td>0.07 (+18.15%)</td><td>0.01 (-1.18%)</td><td>188.20 (-15.34%)</td><td>159.42 (-3.66%)</td><td>168.10 (+7.69%)</td><td>133.20 (-5.06%)</td><td>24.45 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>165.48 (n/a)</td><td>156.10 (n/a)</td><td>140.30 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(-26.90%)</b></td><td>0.05 (-12.99%)</td><td>0.05 (-7.16%)</td><td>0.04 (-7.20%)</td><td>0.01 <b>(-50.10%)</b></td><td>229.60 (+7.74%)</td><td>178.82 (+11.68%)</td><td>172.20 (+7.69%)</td><td>159.70 <b>(+36.85%)</b></td><td>29.08 <b>(-24.72%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>160.12 (n/a)</td><td>159.90 (n/a)</td><td>116.70 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (-9.51%)</td><td>0.07 (+15.63%)</td><td>0.07 <b>(+32.61%)</b></td><td>0.05 (+15.95%)</td><td>0.01 <b>(-33.64%)</b></td><td>199.00 (-13.74%)</td><td>159.76 (-15.69%)</td><td>143.50 <b>(-24.59%)</b></td><td>138.50 (+10.53%)</td><td>26.25 <b>(-35.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>189.50 (n/a)</td><td>190.30 (n/a)</td><td>125.30 (n/a)</td><td>40.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (-8.49%)</td><td>0.05 (-5.04%)</td><td>0.05 (-11.55%)</td><td>0.04 (-5.97%)</td><td>0.01 (+3.24%)</td><td>209.20 (+6.35%)</td><td>176.36 (+5.85%)</td><td>180.20 (+13.05%)</td><td>141.10 (+9.30%)</td><td>32.33 (+18.16%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>166.62 (n/a)</td><td>159.40 (n/a)</td><td>129.10 (n/a)</td><td>27.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 <b>(-20.16%)</b></td><td>0.06 (-8.75%)</td><td>0.06 (-5.53%)</td><td>0.05 (+13.79%)</td><td>0.01 <b>(-54.80%)</b></td><td>197.00 (-12.09%)</td><td>175.80 (+6.40%)</td><td>169.50 (+5.87%)</td><td>158.30 <b>(+25.34%)</b></td><td>18.69 <b>(-50.47%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>165.22 (n/a)</td><td>160.10 (n/a)</td><td>126.30 (n/a)</td><td>37.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+15.20%)</td><td>0.05 (+16.35%)</td><td>0.05 (+9.31%)</td><td>0.05 <b>(+41.09%)</b></td><td>0.00 <b>(-30.44%)</b></td><td>172.90 <b>(-29.11%)</b></td><td>162.28 (-15.15%)</td><td>169.30 (-8.54%)</td><td>142.10 (-13.19%)</td><td>12.73 <b>(-58.65%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.90 (n/a)</td><td>191.26 (n/a)</td><td>185.10 (n/a)</td><td>163.70 (n/a)</td><td>30.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 <b>(+25.74%)</b></td><td>0.06 (+6.68%)</td><td>0.06 (-1.84%)</td><td>0.04 (-7.65%)</td><td>0.02 <b>(+79.85%)</b></td><td>242.70 (+8.25%)</td><td>173.30 (-2.51%)</td><td>164.10 (+1.86%)</td><td>120.60 <b>(-20.50%)</b></td><td>49.08 <b>(+56.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>177.76 (n/a)</td><td>161.10 (n/a)</td><td>151.70 (n/a)</td><td>31.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+1.71%)</td><td>0.05 (+5.22%)</td><td>0.05 <b>(+21.15%)</b></td><td>0.04 (-5.00%)</td><td>0.01 (+6.31%)</td><td>216.90 (+5.29%)</td><td>169.96 (-4.47%)</td><td>157.10 (-17.45%)</td><td>127.90 (-1.69%)</td><td>34.72 (+11.94%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>177.92 (n/a)</td><td>190.30 (n/a)</td><td>130.10 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (+5.96%)</td><td>0.06 (-0.95%)</td><td>0.05 (+3.20%)</td><td>0.05 (-5.67%)</td><td>0.01 (+11.88%)</td><td>197.20 (+6.02%)</td><td>164.98 (+1.49%)</td><td>174.30 (-3.11%)</td><td>118.20 (-5.67%)</td><td>30.59 (+7.92%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>162.56 (n/a)</td><td>179.90 (n/a)</td><td>125.30 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (+8.69%)</td><td>0.04 (-9.05%)</td><td>0.04 (-19.37%)</td><td>0.03 <b>(-29.05%)</b></td><td>0.01 <b>(+112.72%)</b></td><td>286.60 <b>(+40.97%)</b></td><td>205.68 (+16.90%)</td><td>220.90 <b>(+24.03%)</b></td><td>130.90 (-8.01%)</td><td>60.41 <b>(+177.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>175.94 (n/a)</td><td>178.10 (n/a)</td><td>142.30 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (+17.49%)</td><td>0.04 (-5.27%)</td><td>0.05 (-8.06%)</td><td>0.02 (+4.37%)</td><td>0.02 <b>(+28.19%)</b></td><td>364.50 (-4.18%)</td><td>233.28 (+8.94%)</td><td>191.30 (+8.75%)</td><td>127.60 (-14.93%)</td><td>98.44 (+3.51%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>380.40 (n/a)</td><td>214.14 (n/a)</td><td>175.90 (n/a)</td><td>150.00 (n/a)</td><td>95.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 <b>(-28.63%)</b></td><td>0.05 (-3.03%)</td><td>0.05 (+3.64%)</td><td>0.04 <b>(+28.97%)</b></td><td>0.00 <b>(-88.33%)</b></td><td>184.80 <b>(-22.45%)</b></td><td>177.22 (-2.27%)</td><td>176.40 (-3.50%)</td><td>169.40 <b>(+40.12%)</b></td><td>5.81 <b>(-87.14%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>181.34 (n/a)</td><td>182.80 (n/a)</td><td>120.90 (n/a)</td><td>45.18 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (-6.23%)</td><td>0.05 (-8.83%)</td><td>0.05 (-3.57%)</td><td>0.04 (-12.66%)</td><td>0.01 (-9.20%)</td><td>228.90 (+14.51%)</td><td>190.48 (+9.66%)</td><td>186.20 (+3.67%)</td><td>151.40 (+6.62%)</td><td>28.59 (+9.98%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>173.70 (n/a)</td><td>179.60 (n/a)</td><td>142.00 (n/a)</td><td>26.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (-9.87%)</td><td>0.03 (-19.71%)</td><td>0.03 (-16.67%)</td><td>0.02 <b>(-35.76%)</b></td><td>0.01 <b>(+41.31%)</b></td><td>372.90 <b>(+55.70%)</b></td><td>259.04 <b>(+30.14%)</b></td><td>244.70 <b>(+20.01%)</b></td><td>185.40 (+10.95%)</td><td>75.21 <b>(+148.75%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>199.04 (n/a)</td><td>203.90 (n/a)</td><td>167.10 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-3.18%)</td><td>0.11 (+0.81%)</td><td>0.10 (+7.13%)</td><td>0.07 (-4.89%)</td><td>0.02 (-8.02%)</td><td>220.80 (+5.14%)</td><td>156.90 (-1.03%)</td><td>156.50 (-6.68%)</td><td>123.70 (+3.34%)</td><td>39.22 (+3.60%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>210.00 (n/a)</td><td>158.54 (n/a)</td><td>167.70 (n/a)</td><td>119.70 (n/a)</td><td>37.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (-17.20%)</td><td>0.15 (-10.35%)</td><td>0.14 <b>(-23.70%)</b></td><td>0.13 (+10.52%)</td><td>0.02 <b>(-39.87%)</b></td><td>196.40 (-9.53%)</td><td>169.68 (+8.56%)</td><td>180.10 <b>(+31.08%)</b></td><td>143.20 <b>(+20.74%)</b></td><td>24.37 <b>(-37.35%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>217.10 (n/a)</td><td>156.30 (n/a)</td><td>137.40 (n/a)</td><td>118.60 (n/a)</td><td>38.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-3.19%)</td><td>0.10 (+2.07%)</td><td>0.11 (+7.39%)</td><td>0.08 (-3.10%)</td><td>0.02 (+1.73%)</td><td>213.00 (+3.20%)</td><td>164.68 (-1.62%)</td><td>155.80 (-6.87%)</td><td>127.10 (+3.33%)</td><td>34.55 (+10.84%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.40 (n/a)</td><td>167.40 (n/a)</td><td>167.30 (n/a)</td><td>123.00 (n/a)</td><td>31.17 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (-17.23%)</td><td>0.14 (-5.92%)</td><td>0.15 (+1.70%)</td><td>0.10 (-10.49%)</td><td>0.03 <b>(-20.37%)</b></td><td>195.90 (+11.75%)</td><td>154.06 (+5.68%)</td><td>139.10 (-1.70%)</td><td>127.70 <b>(+20.81%)</b></td><td>30.56 (+3.75%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>175.30 (n/a)</td><td>145.78 (n/a)</td><td>141.50 (n/a)</td><td>105.70 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (-13.75%)</td><td>0.10 (+2.63%)</td><td>0.11 (+5.16%)</td><td>0.09 <b>(+20.63%)</b></td><td>0.01 <b>(-53.14%)</b></td><td>181.20 (-17.11%)</td><td>159.62 (-5.16%)</td><td>154.10 (-4.88%)</td><td>144.20 (+16.01%)</td><td>15.73 <b>(-55.10%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>218.60 (n/a)</td><td>168.30 (n/a)</td><td>162.00 (n/a)</td><td>124.30 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (+0.56%)</td><td>0.12 (-2.83%)</td><td>0.11 (-0.22%)</td><td>0.10 (+3.47%)</td><td>0.02 (-15.62%)</td><td>211.10 (-3.34%)</td><td>175.28 (+1.62%)</td><td>181.90 (+0.22%)</td><td>129.00 (-0.54%)</td><td>31.38 (-18.09%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>218.40 (n/a)</td><td>172.48 (n/a)</td><td>181.50 (n/a)</td><td>129.70 (n/a)</td><td>38.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+6.61%)</td><td>0.11 (+3.95%)</td><td>0.10 (+1.29%)</td><td>0.08 (+18.75%)</td><td>0.02 (-6.45%)</td><td>208.40 (-15.76%)</td><td>160.30 (-5.28%)</td><td>156.50 (-1.26%)</td><td>122.40 (-6.21%)</td><td>32.11 <b>(-29.28%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>247.40 (n/a)</td><td>169.24 (n/a)</td><td>158.50 (n/a)</td><td>130.50 (n/a)</td><td>45.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (-2.13%)</td><td>0.10 <b>(-24.13%)</b></td><td>0.10 <b>(-28.43%)</b></td><td>0.08 <b>(-26.20%)</b></td><td>0.02 <b>(+59.29%)</b></td><td>238.90 <b>(+35.51%)</b></td><td>192.80 <b>(+35.99%)</b></td><td>185.00 <b>(+39.73%)</b></td><td>132.20 (+2.16%)</td><td>42.81 <b>(+118.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>176.30 (n/a)</td><td>141.78 (n/a)</td><td>132.40 (n/a)</td><td>129.40 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (-0.15%)</td><td>0.10 <b>(+22.65%)</b></td><td>0.10 <b>(+32.02%)</b></td><td>0.08 <b>(+90.33%)</b></td><td>0.01 <b>(-58.74%)</b></td><td>201.30 <b>(-47.44%)</b></td><td>168.88 <b>(-28.04%)</b></td><td>162.50 <b>(-24.28%)</b></td><td>140.90 (+0.14%)</td><td>22.71 <b>(-77.41%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>383.00 (n/a)</td><td>234.68 (n/a)</td><td>214.60 (n/a)</td><td>140.70 (n/a)</td><td>100.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (-7.18%)</td><td>0.10 (-14.95%)</td><td>0.10 (-17.15%)</td><td>0.08 (-19.54%)</td><td>0.02 <b>(+34.56%)</b></td><td>240.70 <b>(+24.26%)</b></td><td>196.64 (+19.09%)</td><td>193.90 <b>(+20.73%)</b></td><td>158.90 (+7.73%)</td><td>32.56 <b>(+78.77%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>165.12 (n/a)</td><td>160.60 (n/a)</td><td>147.50 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(-20.02%)</b></td><td>0.08 (-16.12%)</td><td>0.08 (-12.58%)</td><td>0.06 (-12.00%)</td><td>0.01 <b>(-30.44%)</b></td><td>259.90 (+13.64%)</td><td>210.82 (+18.31%)</td><td>206.00 (+14.38%)</td><td>181.50 <b>(+25.09%)</b></td><td>31.92 (-1.96%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>228.70 (n/a)</td><td>178.20 (n/a)</td><td>180.10 (n/a)</td><td>145.10 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(-28.14%)</b></td><td>0.08 (-17.99%)</td><td>0.08 (-18.11%)</td><td>0.08 (-5.67%)</td><td>0.00 <b>(-70.88%)</b></td><td>225.50 (+6.02%)</td><td>211.18 (+19.66%)</td><td>211.70 <b>(+22.09%)</b></td><td>194.10 <b>(+39.14%)</b></td><td>12.25 <b>(-57.13%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.70 (n/a)</td><td>176.48 (n/a)</td><td>173.40 (n/a)</td><td>139.50 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (-7.94%)</td><td>0.07 (-16.96%)</td><td>0.07 <b>(-22.65%)</b></td><td>0.06 (-16.99%)</td><td>0.02 (+6.69%)</td><td>272.80 <b>(+20.44%)</b></td><td>228.72 <b>(+21.87%)</b></td><td>241.90 <b>(+29.29%)</b></td><td>163.70 (+8.63%)</td><td>46.03 <b>(+40.79%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.50 (n/a)</td><td>187.68 (n/a)</td><td>187.10 (n/a)</td><td>150.70 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(-29.18%)</b></td><td>0.07 <b>(-25.26%)</b></td><td>0.08 (-17.62%)</td><td>0.05 <b>(-27.01%)</b></td><td>0.02 <b>(-25.50%)</b></td><td>324.60 <b>(+37.02%)</b></td><td>258.64 <b>(+34.48%)</b></td><td>229.10 <b>(+21.41%)</b></td><td>192.70 <b>(+41.28%)</b></td><td>59.43 <b>(+51.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.90 (n/a)</td><td>192.32 (n/a)</td><td>188.70 (n/a)</td><td>136.40 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (-0.63%)</td><td>0.07 (-18.23%)</td><td>0.07 (-15.29%)</td><td>0.05 <b>(-22.00%)</b></td><td>0.02 <b>(+53.68%)</b></td><td>311.20 <b>(+28.17%)</b></td><td>247.92 <b>(+26.03%)</b></td><td>225.60 (+18.05%)</td><td>176.10 (+0.63%)</td><td>57.31 <b>(+105.80%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.80 (n/a)</td><td>196.72 (n/a)</td><td>191.10 (n/a)</td><td>175.00 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (+2.61%)</td><td>0.19 (-4.79%)</td><td>0.17 (-14.69%)</td><td>0.16 (-6.66%)</td><td>0.03 <b>(+48.74%)</b></td><td>202.10 (+7.16%)</td><td>176.70 (+6.28%)</td><td>187.90 (+17.22%)</td><td>141.20 (-2.49%)</td><td>27.57 <b>(+54.83%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.60 (n/a)</td><td>166.26 (n/a)</td><td>160.30 (n/a)</td><td>144.80 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (-10.37%)</td><td>0.20 (-11.95%)</td><td>0.20 (-14.28%)</td><td>0.17 (-6.66%)</td><td>0.03 (-13.83%)</td><td>188.70 (+7.16%)</td><td>163.26 (+13.36%)</td><td>165.80 (+16.68%)</td><td>135.20 (+11.55%)</td><td>21.31 (+1.94%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.10 (n/a)</td><td>144.02 (n/a)</td><td>142.10 (n/a)</td><td>121.20 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (-4.94%)</td><td>0.20 (-7.52%)</td><td>0.21 (-8.02%)</td><td>0.15 (-15.16%)</td><td>0.03 (+14.43%)</td><td>264.50 (+17.87%)</td><td>204.54 (+9.09%)</td><td>195.10 (+8.69%)</td><td>169.00 (+5.16%)</td><td>36.74 <b>(+44.14%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>224.40 (n/a)</td><td>187.50 (n/a)</td><td>179.50 (n/a)</td><td>160.70 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (+19.60%)</td><td>0.20 (+4.66%)</td><td>0.18 (-1.61%)</td><td>0.18 (+0.01%)</td><td>0.03 <b>(+95.60%)</b></td><td>184.00 (-0.05%)</td><td>165.64 (-3.30%)</td><td>180.10 (+1.64%)</td><td>130.40 (-16.41%)</td><td>23.20 <b>(+65.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>184.10 (n/a)</td><td>171.30 (n/a)</td><td>177.20 (n/a)</td><td>156.00 (n/a)</td><td>13.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (-16.64%)</td><td>0.19 (-18.86%)</td><td>0.19 (-16.09%)</td><td>0.16 (-15.32%)</td><td>0.03 (-19.18%)</td><td>259.60 (+18.11%)</td><td>217.16 <b>(+23.09%)</b></td><td>210.70 (+19.17%)</td><td>175.10 <b>(+20.01%)</b></td><td>33.31 (+15.39%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>219.80 (n/a)</td><td>176.42 (n/a)</td><td>176.80 (n/a)</td><td>145.90 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.28 <b>(+32.65%)</b></td><td>0.19 (-0.32%)</td><td>0.18 (-9.91%)</td><td>0.15 (+2.31%)</td><td>0.05 <b>(+98.80%)</b></td><td>214.20 (-2.24%)</td><td>176.94 (+3.27%)</td><td>179.90 (+10.98%)</td><td>115.60 <b>(-24.64%)</b></td><td>37.77 <b>(+38.64%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.10 (n/a)</td><td>171.34 (n/a)</td><td>162.10 (n/a)</td><td>153.40 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (-17.04%)</td><td>0.17 <b>(-21.21%)</b></td><td>0.16 <b>(-28.61%)</b></td><td>0.13 <b>(-21.64%)</b></td><td>0.04 (-12.71%)</td><td>292.80 <b>(+27.64%)</b></td><td>227.50 <b>(+27.55%)</b></td><td>230.20 <b>(+40.02%)</b></td><td>170.00 <b>(+20.57%)</b></td><td>49.78 <b>(+32.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>229.40 (n/a)</td><td>178.36 (n/a)</td><td>164.40 (n/a)</td><td>141.00 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (-16.97%)</td><td>0.19 (-0.85%)</td><td>0.19 (+7.24%)</td><td>0.15 (+6.74%)</td><td>0.02 <b>(-43.55%)</b></td><td>212.60 (-6.34%)</td><td>178.36 (-1.17%)</td><td>168.60 (-6.75%)</td><td>155.60 <b>(+20.43%)</b></td><td>23.05 <b>(-33.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>227.00 (n/a)</td><td>180.48 (n/a)</td><td>180.80 (n/a)</td><td>129.20 (n/a)</td><td>34.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (+3.40%)</td><td>0.20 (+1.58%)</td><td>0.20 (-2.67%)</td><td>0.16 (+5.17%)</td><td>0.03 (+7.08%)</td><td>226.60 (-4.91%)</td><td>189.16 (-1.47%)</td><td>185.60 (+2.71%)</td><td>154.10 (-3.32%)</td><td>30.87 (-1.82%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>238.30 (n/a)</td><td>191.98 (n/a)</td><td>180.70 (n/a)</td><td>159.40 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (-14.52%)</td><td>0.18 (-8.22%)</td><td>0.18 (-12.02%)</td><td>0.15 (-2.27%)</td><td>0.01 <b>(-51.66%)</b></td><td>214.00 (+2.29%)</td><td>187.96 (+7.28%)</td><td>184.30 (+13.70%)</td><td>170.50 (+16.94%)</td><td>16.57 <b>(-42.88%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.20 (n/a)</td><td>175.20 (n/a)</td><td>162.10 (n/a)</td><td>145.80 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (+5.23%)</td><td>0.17 (-11.33%)</td><td>0.16 (-4.49%)</td><td>0.10 <b>(-32.00%)</b></td><td>0.06 <b>(+52.37%)</b></td><td>332.10 <b>(+47.08%)</b></td><td>230.70 <b>(+20.50%)</b></td><td>215.80 (+4.71%)</td><td>140.10 (-4.95%)</td><td>78.82 <b>(+115.89%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.80 (n/a)</td><td>191.46 (n/a)</td><td>206.10 (n/a)</td><td>147.40 (n/a)</td><td>36.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (+11.86%)</td><td>0.18 (-0.04%)</td><td>0.17 (-4.65%)</td><td>0.14 (-2.60%)</td><td>0.03 <b>(+52.88%)</b></td><td>226.10 (+2.68%)</td><td>189.52 (+1.39%)</td><td>192.80 (+4.84%)</td><td>138.70 (-10.63%)</td><td>31.85 <b>(+35.41%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>220.20 (n/a)</td><td>186.92 (n/a)</td><td>183.90 (n/a)</td><td>155.20 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 <b>(+26.76%)</b></td><td>0.18 (+9.03%)</td><td>0.16 (-6.24%)</td><td>0.15 <b>(+45.12%)</b></td><td>0.04 (+17.20%)</td><td>225.50 <b>(-31.10%)</b></td><td>204.30 (-9.43%)</td><td>219.30 (+6.66%)</td><td>141.40 <b>(-21.09%)</b></td><td>35.51 <b>(-39.85%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>327.30 (n/a)</td><td>225.56 (n/a)</td><td>205.60 (n/a)</td><td>179.20 (n/a)</td><td>59.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 <b>(-29.70%)</b></td><td>0.16 (-2.57%)</td><td>0.16 (+9.89%)</td><td>0.14 <b>(+55.40%)</b></td><td>0.02 <b>(-73.37%)</b></td><td>242.70 <b>(-35.66%)</b></td><td>211.94 (-8.01%)</td><td>204.10 (-9.01%)</td><td>187.50 <b>(+42.26%)</b></td><td>22.23 <b>(-75.80%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>377.20 (n/a)</td><td>230.40 (n/a)</td><td>224.30 (n/a)</td><td>131.80 (n/a)</td><td>91.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-17.85%)</td><td>0.12 (-18.92%)</td><td>0.12 <b>(-20.69%)</b></td><td>0.09 (-17.09%)</td><td>0.02 <b>(-21.99%)</b></td><td>216.60 <b>(+20.60%)</b></td><td>173.98 <b>(+23.11%)</b></td><td>166.70 <b>(+26.10%)</b></td><td>153.90 <b>(+21.66%)</b></td><td>25.26 (+14.45%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>179.60 (n/a)</td><td>141.32 (n/a)</td><td>132.20 (n/a)</td><td>126.50 (n/a)</td><td>22.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 (+8.75%)</td><td>0.12 (-7.90%)</td><td>0.11 (-17.08%)</td><td>0.11 (+4.75%)</td><td>0.02 <b>(+24.24%)</b></td><td>194.00 (-4.57%)</td><td>175.90 (+9.00%)</td><td>183.90 <b>(+20.59%)</b></td><td>133.10 (-8.08%)</td><td>24.46 (+3.17%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>161.38 (n/a)</td><td>152.50 (n/a)</td><td>144.80 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-11.32%)</td><td>0.11 (-5.28%)</td><td>0.11 (-10.37%)</td><td>0.11 (+14.58%)</td><td>0.01 <b>(-55.29%)</b></td><td>193.20 (-12.74%)</td><td>180.82 (+2.87%)</td><td>181.40 (+11.56%)</td><td>155.40 (+12.77%)</td><td>15.40 <b>(-56.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>175.78 (n/a)</td><td>162.60 (n/a)</td><td>137.80 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (-5.32%)</td><td>0.11 (+6.42%)</td><td>0.11 (-2.13%)</td><td>0.09 <b>(+30.13%)</b></td><td>0.01 <b>(-56.73%)</b></td><td>223.10 <b>(-23.15%)</b></td><td>195.64 (-9.83%)</td><td>187.50 (+2.18%)</td><td>179.00 (+5.60%)</td><td>19.35 <b>(-65.12%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>290.30 (n/a)</td><td>216.96 (n/a)</td><td>183.50 (n/a)</td><td>169.50 (n/a)</td><td>55.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 <b>(+22.23%)</b></td><td>0.12 (+5.39%)</td><td>0.13 (+12.26%)</td><td>0.07 <b>(-35.21%)</b></td><td>0.03 <b>(+195.78%)</b></td><td>309.20 <b>(+54.29%)</b></td><td>185.50 (+2.87%)</td><td>160.90 (-10.91%)</td><td>127.10 (-18.16%)</td><td>71.22 <b>(+302.17%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>180.32 (n/a)</td><td>180.60 (n/a)</td><td>155.30 (n/a)</td><td>17.71 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-18.18%)</td><td>0.12 (-8.03%)</td><td>0.11 (-7.14%)</td><td>0.11 (+1.22%)</td><td>0.01 <b>(-55.61%)</b></td><td>190.70 (-1.19%)</td><td>177.72 (+7.01%)</td><td>178.70 (+7.72%)</td><td>157.10 <b>(+22.26%)</b></td><td>13.97 <b>(-46.31%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>193.00 (n/a)</td><td>166.08 (n/a)</td><td>165.90 (n/a)</td><td>128.50 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (-15.45%)</td><td>0.12 (-7.27%)</td><td>0.13 (+0.97%)</td><td>0.09 (-13.38%)</td><td>0.02 (-14.92%)</td><td>219.00 (+15.45%)</td><td>179.14 (+7.79%)</td><td>162.50 (-0.98%)</td><td>155.30 (+18.28%)</td><td>27.68 (+14.21%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.70 (n/a)</td><td>166.20 (n/a)</td><td>164.10 (n/a)</td><td>131.30 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+2.42%)</td><td>0.10 (+0.51%)</td><td>0.10 (-2.73%)</td><td>0.05 (-14.10%)</td><td>0.03 (+4.88%)</td><td>374.60 (+16.41%)</td><td>222.98 (+1.71%)</td><td>201.60 (+2.80%)</td><td>156.70 (-2.37%)</td><td>87.98 <b>(+27.45%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>321.80 (n/a)</td><td>219.24 (n/a)</td><td>196.10 (n/a)</td><td>160.50 (n/a)</td><td>69.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (-14.75%)</td><td>0.14 (-15.33%)</td><td>0.15 (-16.28%)</td><td>0.12 (-4.19%)</td><td>0.02 <b>(-38.48%)</b></td><td>197.50 (+4.39%)</td><td>174.22 (+16.82%)</td><td>167.50 (+19.47%)</td><td>149.90 (+17.29%)</td><td>19.16 <b>(-23.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>189.20 (n/a)</td><td>149.14 (n/a)</td><td>140.20 (n/a)</td><td>127.80 (n/a)</td><td>25.19 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (-14.19%)</td><td>0.14 (-3.77%)</td><td>0.16 (+14.43%)</td><td>0.12 (-4.91%)</td><td>0.02 <b>(-33.61%)</b></td><td>207.90 (+5.16%)</td><td>172.30 (+2.65%)</td><td>157.30 (-12.61%)</td><td>152.90 (+16.54%)</td><td>24.11 (-19.04%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.70 (n/a)</td><td>167.86 (n/a)</td><td>180.00 (n/a)</td><td>131.20 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 <b>(-27.35%)</b></td><td>0.13 <b>(-21.68%)</b></td><td>0.13 <b>(-32.00%)</b></td><td>0.10 (+11.29%)</td><td>0.02 <b>(-57.44%)</b></td><td>235.80 (-10.14%)</td><td>194.98 (+18.83%)</td><td>185.70 <b>(+47.15%)</b></td><td>163.00 <b>(+37.67%)</b></td><td>33.25 <b>(-46.34%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>262.40 (n/a)</td><td>164.08 (n/a)</td><td>126.20 (n/a)</td><td>118.40 (n/a)</td><td>61.96 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (-13.86%)</td><td>0.15 (-1.30%)</td><td>0.15 (+9.46%)</td><td>0.13 (+9.45%)</td><td>0.01 <b>(-60.03%)</b></td><td>188.30 (-8.64%)</td><td>165.02 (-2.10%)</td><td>164.40 (-8.67%)</td><td>149.00 (+16.13%)</td><td>16.01 <b>(-56.82%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>206.10 (n/a)</td><td>168.56 (n/a)</td><td>180.00 (n/a)</td><td>128.30 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 <b>(-20.29%)</b></td><td>0.14 (-0.94%)</td><td>0.14 (+2.94%)</td><td>0.13 <b>(+30.81%)</b></td><td>0.01 <b>(-63.71%)</b></td><td>193.50 <b>(-23.55%)</b></td><td>174.52 (-3.63%)</td><td>174.50 (-2.84%)</td><td>153.50 <b>(+25.41%)</b></td><td>16.47 <b>(-64.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>253.10 (n/a)</td><td>181.10 (n/a)</td><td>179.60 (n/a)</td><td>122.40 (n/a)</td><td>46.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 (-15.20%)</td><td>0.13 <b>(-21.78%)</b></td><td>0.13 (-19.70%)</td><td>0.11 <b>(-23.10%)</b></td><td>0.02 <b>(+31.23%)</b></td><td>218.20 <b>(+30.04%)</b></td><td>195.46 <b>(+28.74%)</b></td><td>190.40 <b>(+24.53%)</b></td><td>163.50 (+17.97%)</td><td>22.65 <b>(+104.10%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>167.80 (n/a)</td><td>151.82 (n/a)</td><td>152.90 (n/a)</td><td>138.60 (n/a)</td><td>11.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (+8.32%)</td><td>0.12 (-6.89%)</td><td>0.12 (-13.73%)</td><td>0.09 (-10.40%)</td><td>0.03 <b>(+20.25%)</b></td><td>270.80 (+11.58%)</td><td>209.30 (+8.54%)</td><td>207.30 (+15.87%)</td><td>151.10 (-7.70%)</td><td>42.46 <b>(+23.61%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>242.70 (n/a)</td><td>192.84 (n/a)</td><td>178.90 (n/a)</td><td>163.70 (n/a)</td><td>34.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (+4.42%)</td><td>0.14 (+4.86%)</td><td>0.14 (+0.59%)</td><td>0.12 (+16.90%)</td><td>0.03 (-8.18%)</td><td>211.40 (-14.45%)</td><td>174.34 (-5.69%)</td><td>179.70 (-0.61%)</td><td>133.30 (-4.24%)</td><td>28.82 <b>(-27.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>247.10 (n/a)</td><td>184.86 (n/a)</td><td>180.80 (n/a)</td><td>139.20 (n/a)</td><td>39.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (-2.70%)</td><td>0.11 (-4.10%)</td><td>0.10 (-15.85%)</td><td>0.10 <b>(+23.70%)</b></td><td>0.02 (-17.87%)</td><td>189.90 (-19.16%)</td><td>165.86 (+2.19%)</td><td>183.40 (+18.86%)</td><td>131.60 (+2.81%)</td><td>29.41 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>234.90 (n/a)</td><td>162.30 (n/a)</td><td>154.30 (n/a)</td><td>128.00 (n/a)</td><td>43.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (+1.79%)</td><td>0.11 (+2.00%)</td><td>0.11 (+5.97%)</td><td>0.08 (+7.00%)</td><td>0.02 (-3.15%)</td><td>236.10 (-6.53%)</td><td>179.46 (-2.48%)</td><td>168.60 (-5.60%)</td><td>136.90 (-1.72%)</td><td>36.81 (-12.38%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>252.60 (n/a)</td><td>184.02 (n/a)</td><td>178.60 (n/a)</td><td>139.30 (n/a)</td><td>42.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (-3.57%)</td><td>0.10 (+2.93%)</td><td>0.11 (+16.78%)</td><td>0.06 <b>(-27.02%)</b></td><td>0.03 (+13.57%)</td><td>331.70 <b>(+37.01%)</b></td><td>195.66 (+2.14%)</td><td>170.00 (-14.36%)</td><td>127.20 (+3.67%)</td><td>79.13 <b>(+83.72%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>242.10 (n/a)</td><td>191.56 (n/a)</td><td>198.50 (n/a)</td><td>122.70 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (-17.16%)</td><td>0.11 (-1.50%)</td><td>0.10 (-5.05%)</td><td>0.09 (+11.75%)</td><td>0.01 <b>(-49.85%)</b></td><td>214.00 (-10.54%)</td><td>176.84 (-2.57%)</td><td>175.80 (+5.27%)</td><td>150.20 <b>(+20.74%)</b></td><td>25.01 <b>(-47.37%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>239.20 (n/a)</td><td>181.50 (n/a)</td><td>167.00 (n/a)</td><td>124.40 (n/a)</td><td>47.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (+9.73%)</td><td>0.11 (+3.95%)</td><td>0.10 (-0.03%)</td><td>0.10 (+7.80%)</td><td>0.02 <b>(+32.84%)</b></td><td>191.30 (-7.23%)</td><td>169.46 (-3.22%)</td><td>176.30 (+0.06%)</td><td>133.70 (-8.86%)</td><td>23.99 (+12.88%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>175.10 (n/a)</td><td>176.20 (n/a)</td><td>146.70 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 <b>(+41.15%)</b></td><td>0.11 (+18.08%)</td><td>0.13 <b>(+22.33%)</b></td><td>0.06 <b>(-26.19%)</b></td><td>0.04 <b>(+233.84%)</b></td><td>295.00 <b>(+35.45%)</b></td><td>177.70 (-7.36%)</td><td>146.00 (-18.25%)</td><td>122.70 <b>(-29.16%)</b></td><td>70.42 <b>(+224.85%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>191.82 (n/a)</td><td>178.60 (n/a)</td><td>173.20 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (-1.27%)</td><td>0.10 (+2.77%)</td><td>0.11 (+12.47%)</td><td>0.08 (+12.37%)</td><td>0.02 (-19.74%)</td><td>243.30 (-11.01%)</td><td>189.76 (-4.39%)</td><td>169.20 (-11.09%)</td><td>157.50 (+1.29%)</td><td>36.27 <b>(-25.72%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>273.40 (n/a)</td><td>198.48 (n/a)</td><td>190.30 (n/a)</td><td>155.50 (n/a)</td><td>48.83 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (-15.85%)</td><td>0.08 <b>(-23.27%)</b></td><td>0.08 <b>(-24.64%)</b></td><td>0.05 <b>(-38.65%)</b></td><td>0.02 (+13.18%)</td><td>368.10 <b>(+63.02%)</b></td><td>236.78 <b>(+36.02%)</b></td><td>224.10 <b>(+32.68%)</b></td><td>162.20 (+18.83%)</td><td>77.84 <b>(+128.54%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>225.80 (n/a)</td><td>174.08 (n/a)</td><td>168.90 (n/a)</td><td>136.50 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.67 (-7.27%)</td><td>0.57 (-0.53%)</td><td>0.61 (+3.38%)</td><td>0.41 (-5.81%)</td><td>0.11 (-16.76%)</td><td>237.50 (+6.17%)</td><td>176.96 (-0.49%)</td><td>160.20 (-3.26%)</td><td>147.10 (+7.84%)</td><td>38.41 (-8.20%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.72 (n/a)</td><td>0.58 (n/a)</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.13 (n/a)</td><td>223.70 (n/a)</td><td>177.84 (n/a)</td><td>165.60 (n/a)</td><td>136.40 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.79 (+0.20%)</td><td>0.63 (+4.31%)</td><td>0.66 (+18.30%)</td><td>0.40 <b>(-24.07%)</b></td><td>0.15 <b>(+36.37%)</b></td><td>247.00 <b>(+31.73%)</b></td><td>165.02 (-0.90%)</td><td>149.50 (-15.44%)</td><td>124.60 (-0.24%)</td><td>48.03 <b>(+90.61%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.79 (n/a)</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.52 (n/a)</td><td>0.11 (n/a)</td><td>187.50 (n/a)</td><td>166.52 (n/a)</td><td>176.80 (n/a)</td><td>124.90 (n/a)</td><td>25.20 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.64 (-13.93%)</td><td>0.52 (-11.81%)</td><td>0.52 (-4.69%)</td><td>0.38 <b>(-21.04%)</b></td><td>0.10 (-1.50%)</td><td>256.20 <b>(+26.64%)</b></td><td>193.64 (+14.47%)</td><td>187.70 (+4.92%)</td><td>154.60 (+16.15%)</td><td>39.64 <b>(+47.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.74 (n/a)</td><td>0.59 (n/a)</td><td>0.55 (n/a)</td><td>0.49 (n/a)</td><td>0.10 (n/a)</td><td>202.30 (n/a)</td><td>169.16 (n/a)</td><td>178.90 (n/a)</td><td>133.10 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.54 <b>(-34.65%)</b></td><td>0.49 (-15.94%)</td><td>0.48 (-9.72%)</td><td>0.44 (-7.68%)</td><td>0.04 <b>(-70.57%)</b></td><td>222.60 (+8.32%)</td><td>199.90 (+15.06%)</td><td>202.80 (+10.76%)</td><td>182.90 <b>(+53.05%)</b></td><td>16.90 <b>(-51.75%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.82 (n/a)</td><td>0.59 (n/a)</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>205.50 (n/a)</td><td>173.74 (n/a)</td><td>183.10 (n/a)</td><td>119.50 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.50 (-14.99%)</td><td>0.43 (-6.19%)</td><td>0.43 (-8.68%)</td><td>0.30 <b>(+41.74%)</b></td><td>0.07 <b>(-49.75%)</b></td><td>241.80 <b>(-29.46%)</b></td><td>178.20 (-3.71%)</td><td>170.50 (+9.51%)</td><td>147.90 (+17.66%)</td><td>37.06 <b>(-58.81%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.59 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>342.80 (n/a)</td><td>185.06 (n/a)</td><td>155.70 (n/a)</td><td>125.70 (n/a)</td><td>89.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.47 <b>(-21.37%)</b></td><td>0.40 (-12.34%)</td><td>0.38 (-14.49%)</td><td>0.35 (+6.01%)</td><td>0.05 <b>(-50.77%)</b></td><td>211.10 (-5.67%)</td><td>186.28 (+10.64%)</td><td>194.70 (+16.94%)</td><td>156.00 <b>(+27.14%)</b></td><td>23.20 <b>(-41.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.60 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.11 (n/a)</td><td>223.80 (n/a)</td><td>168.36 (n/a)</td><td>166.50 (n/a)</td><td>122.70 (n/a)</td><td>39.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.58 (+18.19%)</td><td>0.48 (+8.87%)</td><td>0.50 (+6.44%)</td><td>0.25 <b>(-30.60%)</b></td><td>0.14 <b>(+135.78%)</b></td><td>300.50 <b>(+44.12%)</b></td><td>170.56 (+0.20%)</td><td>148.40 (-6.08%)</td><td>126.60 (-15.37%)</td><td>73.45 <b>(+198.67%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>208.50 (n/a)</td><td>170.22 (n/a)</td><td>158.00 (n/a)</td><td>149.60 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.49 (-8.28%)</td><td>0.38 (-10.77%)</td><td>0.38 (-18.80%)</td><td>0.29 (+3.94%)</td><td>0.07 <b>(-24.84%)</b></td><td>252.40 (-3.77%)</td><td>197.12 (+9.77%)</td><td>195.20 <b>(+23.15%)</b></td><td>150.00 (+9.01%)</td><td>37.13 <b>(-24.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>262.30 (n/a)</td><td>179.58 (n/a)</td><td>158.50 (n/a)</td><td>137.60 (n/a)</td><td>48.96 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (-12.58%)</td><td>0.21 (-4.49%)</td><td>0.21 (-3.94%)</td><td>0.18 (+12.36%)</td><td>0.02 <b>(-46.12%)</b></td><td>200.70 (-11.00%)</td><td>175.12 (+2.34%)</td><td>177.70 (+4.10%)</td><td>147.70 (+14.41%)</td><td>18.95 <b>(-46.21%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>225.50 (n/a)</td><td>171.12 (n/a)</td><td>170.70 (n/a)</td><td>129.10 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (-16.68%)</td><td>0.17 <b>(-23.22%)</b></td><td>0.17 <b>(-23.39%)</b></td><td>0.10 <b>(-41.08%)</b></td><td>0.04 (+6.66%)</td><td>359.10 <b>(+69.71%)</b></td><td>234.58 <b>(+34.92%)</b></td><td>211.00 <b>(+30.49%)</b></td><td>169.40 <b>(+20.06%)</b></td><td>72.83 <b>(+125.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>211.60 (n/a)</td><td>173.86 (n/a)</td><td>161.70 (n/a)</td><td>141.10 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (-2.29%)</td><td>0.24 (+4.56%)</td><td>0.25 (+10.65%)</td><td>0.17 (+6.08%)</td><td>0.05 (+1.07%)</td><td>216.70 (-5.74%)</td><td>162.36 (-4.28%)</td><td>148.60 (-9.61%)</td><td>121.50 (+2.36%)</td><td>39.29 (-1.05%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>229.90 (n/a)</td><td>169.62 (n/a)</td><td>164.40 (n/a)</td><td>118.70 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 (-3.66%)</td><td>0.23 (+5.78%)</td><td>0.23 (+7.35%)</td><td>0.17 (+9.49%)</td><td>0.04 (-17.71%)</td><td>213.10 (-8.66%)</td><td>163.28 (-6.71%)</td><td>160.50 (-6.85%)</td><td>128.30 (+3.80%)</td><td>31.29 (-19.72%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>233.30 (n/a)</td><td>175.02 (n/a)</td><td>172.30 (n/a)</td><td>123.60 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (-11.03%)</td><td>0.18 (-16.42%)</td><td>0.19 <b>(-21.63%)</b></td><td>0.10 <b>(-28.84%)</b></td><td>0.05 (+11.71%)</td><td>362.70 <b>(+40.53%)</b></td><td>220.06 <b>(+24.47%)</b></td><td>198.90 <b>(+27.58%)</b></td><td>161.60 (+12.38%)</td><td>82.03 <b>(+76.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>258.10 (n/a)</td><td>176.80 (n/a)</td><td>155.90 (n/a)</td><td>143.80 (n/a)</td><td>46.54 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (+19.20%)</td><td>0.24 (+10.77%)</td><td>0.22 (+1.93%)</td><td>0.18 <b>(+25.41%)</b></td><td>0.05 (+11.48%)</td><td>205.70 <b>(-20.24%)</b></td><td>161.44 (-10.43%)</td><td>167.00 (-1.94%)</td><td>121.10 (-16.14%)</td><td>34.42 <b>(-26.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>257.90 (n/a)</td><td>180.24 (n/a)</td><td>170.30 (n/a)</td><td>144.40 (n/a)</td><td>46.61 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (-11.63%)</td><td>0.21 (-9.39%)</td><td>0.22 (-4.90%)</td><td>0.17 (-6.09%)</td><td>0.03 (-12.82%)</td><td>215.80 (+6.52%)</td><td>182.00 (+10.20%)</td><td>166.20 (+5.12%)</td><td>157.20 (+13.09%)</td><td>29.17 (+6.84%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>202.60 (n/a)</td><td>165.16 (n/a)</td><td>158.10 (n/a)</td><td>139.00 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (+14.53%)</td><td>0.21 (+4.57%)</td><td>0.21 (+17.48%)</td><td>0.14 (-17.69%)</td><td>0.06 <b>(+36.74%)</b></td><td>266.50 <b>(+21.52%)</b></td><td>184.38 (-1.63%)</td><td>175.60 (-14.84%)</td><td>123.50 (-12.66%)</td><td>51.66 <b>(+45.72%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>219.30 (n/a)</td><td>187.44 (n/a)</td><td>206.20 (n/a)</td><td>141.40 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 (-9.88%)</td><td>0.25 (+0.11%)</td><td>0.24 (+3.55%)</td><td>0.22 (+2.88%)</td><td>0.03 <b>(-31.40%)</b></td><td>187.30 (-2.80%)</td><td>168.22 (-1.20%)</td><td>171.40 (-3.38%)</td><td>141.50 (+10.89%)</td><td>20.24 <b>(-24.64%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>192.70 (n/a)</td><td>170.26 (n/a)</td><td>177.40 (n/a)</td><td>127.60 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.31 (-3.57%)</td><td>0.22 (+0.28%)</td><td>0.21 (-7.25%)</td><td>0.16 <b>(+33.74%)</b></td><td>0.05 <b>(-24.73%)</b></td><td>252.60 <b>(-25.24%)</b></td><td>192.54 (-5.70%)</td><td>194.10 (+7.83%)</td><td>134.20 (+3.71%)</td><td>43.04 <b>(-45.71%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>337.90 (n/a)</td><td>204.18 (n/a)</td><td>180.00 (n/a)</td><td>129.40 (n/a)</td><td>79.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (+4.73%)</td><td>0.29 <b>(+24.05%)</b></td><td>0.31 <b>(+43.28%)</b></td><td>0.24 (+17.79%)</td><td>0.04 (-13.43%)</td><td>171.40 (-15.11%)</td><td>142.38 <b>(-20.19%)</b></td><td>130.40 <b>(-30.23%)</b></td><td>122.50 (-4.52%)</td><td>21.21 <b>(-27.48%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>201.90 (n/a)</td><td>178.40 (n/a)</td><td>186.90 (n/a)</td><td>128.30 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.32 (-10.55%)</td><td>0.27 (+3.36%)</td><td>0.29 <b>(+25.31%)</b></td><td>0.21 (-7.80%)</td><td>0.05 (-12.62%)</td><td>193.80 (+8.45%)</td><td>154.88 (-3.44%)</td><td>140.10 <b>(-20.22%)</b></td><td>129.80 (+11.80%)</td><td>28.21 (+5.99%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>178.70 (n/a)</td><td>160.40 (n/a)</td><td>175.60 (n/a)</td><td>116.10 (n/a)</td><td>26.61 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.32 (+8.39%)</td><td>0.25 (+6.26%)</td><td>0.22 (-10.73%)</td><td>0.21 <b>(+36.22%)</b></td><td>0.05 (-16.04%)</td><td>195.40 <b>(-26.60%)</b></td><td>170.86 (-8.35%)</td><td>183.80 (+12.00%)</td><td>128.50 (-7.75%)</td><td>27.76 <b>(-44.48%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>266.20 (n/a)</td><td>186.42 (n/a)</td><td>164.10 (n/a)</td><td>139.30 (n/a)</td><td>49.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.31 (+8.28%)</td><td>0.25 (+2.49%)</td><td>0.25 (-1.12%)</td><td>0.17 (-13.25%)</td><td>0.05 <b>(+48.73%)</b></td><td>247.00 (+15.26%)</td><td>171.80 (+0.16%)</td><td>164.00 (+1.11%)</td><td>130.60 (-7.64%)</td><td>44.67 <b>(+62.03%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>214.30 (n/a)</td><td>171.52 (n/a)</td><td>162.20 (n/a)</td><td>141.40 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 (+0.34%)</td><td>0.21 (-13.03%)</td><td>0.19 (-18.99%)</td><td>0.16 <b>(-24.93%)</b></td><td>0.05 <b>(+171.94%)</b></td><td>248.70 <b>(+33.21%)</b></td><td>200.86 (+18.73%)</td><td>211.40 <b>(+23.48%)</b></td><td>156.70 (-0.38%)</td><td>41.43 <b>(+250.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>186.70 (n/a)</td><td>169.18 (n/a)</td><td>171.20 (n/a)</td><td>157.30 (n/a)</td><td>11.83 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.36 (-11.18%)</td><td>0.25 (-8.04%)</td><td>0.24 (-6.02%)</td><td>0.16 <b>(-20.69%)</b></td><td>0.08 (-2.91%)</td><td>262.80 <b>(+26.10%)</b></td><td>173.94 (+11.12%)</td><td>168.90 (+6.43%)</td><td>113.40 (+12.61%)</td><td>55.90 <b>(+46.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>208.40 (n/a)</td><td>156.54 (n/a)</td><td>158.70 (n/a)</td><td>100.70 (n/a)</td><td>38.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (-4.85%)</td><td>0.18 (-14.31%)</td><td>0.17 (-11.05%)</td><td>0.10 <b>(-28.92%)</b></td><td>0.05 (+17.84%)</td><td>339.20 <b>(+40.69%)</b></td><td>214.44 <b>(+21.69%)</b></td><td>199.00 (+12.43%)</td><td>137.90 (+5.11%)</td><td>74.67 <b>(+80.17%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>241.10 (n/a)</td><td>176.22 (n/a)</td><td>177.00 (n/a)</td><td>131.20 (n/a)</td><td>41.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (-3.61%)</td><td>0.19 (-6.42%)</td><td>0.18 (-2.15%)</td><td>0.16 (-8.09%)</td><td>0.04 (-7.11%)</td><td>224.00 (+8.79%)</td><td>187.76 (+6.67%)</td><td>193.50 (+2.22%)</td><td>138.10 (+3.76%)</td><td>31.33 (+0.60%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>205.90 (n/a)</td><td>176.02 (n/a)</td><td>189.30 (n/a)</td><td>133.10 (n/a)</td><td>31.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (-3.60%)</td><td>0.20 (+0.34%)</td><td>0.21 (+16.07%)</td><td>0.16 <b>(+23.09%)</b></td><td>0.04 <b>(-28.49%)</b></td><td>217.60 (-18.75%)</td><td>178.78 (-3.77%)</td><td>164.20 (-13.85%)</td><td>137.40 (+3.78%)</td><td>36.65 <b>(-33.89%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>267.80 (n/a)</td><td>185.78 (n/a)</td><td>190.60 (n/a)</td><td>132.40 (n/a)</td><td>55.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (+10.65%)</td><td>0.18 (-9.72%)</td><td>0.18 (-10.84%)</td><td>0.13 <b>(-20.78%)</b></td><td>0.05 <b>(+97.49%)</b></td><td>260.30 <b>(+26.24%)</b></td><td>200.50 (+15.80%)</td><td>189.60 (+12.19%)</td><td>131.10 (-9.65%)</td><td>51.18 <b>(+125.62%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>206.20 (n/a)</td><td>173.14 (n/a)</td><td>169.00 (n/a)</td><td>145.10 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (-1.55%)</td><td>0.18 (-17.68%)</td><td>0.17 <b>(-27.92%)</b></td><td>0.13 (-19.69%)</td><td>0.04 (+10.68%)</td><td>268.00 <b>(+24.54%)</b></td><td>205.94 <b>(+23.16%)</b></td><td>207.90 <b>(+38.79%)</b></td><td>144.80 (+1.54%)</td><td>44.77 <b>(+40.01%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>215.20 (n/a)</td><td>167.22 (n/a)</td><td>149.80 (n/a)</td><td>142.60 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 <b>(+21.23%)</b></td><td>0.20 (+6.50%)</td><td>0.19 (-3.77%)</td><td>0.14 (-14.98%)</td><td>0.05 <b>(+172.83%)</b></td><td>251.70 (+17.62%)</td><td>179.16 (-1.98%)</td><td>182.70 (+3.92%)</td><td>136.40 (-17.48%)</td><td>46.85 <b>(+151.76%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>214.00 (n/a)</td><td>182.78 (n/a)</td><td>175.80 (n/a)</td><td>165.30 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (+4.33%)</td><td>0.19 (+4.70%)</td><td>0.19 (-12.98%)</td><td>0.16 <b>(+53.07%)</b></td><td>0.03 <b>(-35.64%)</b></td><td>217.10 <b>(-34.69%)</b></td><td>186.46 (-9.72%)</td><td>187.00 (+14.94%)</td><td>155.70 (-4.13%)</td><td>30.18 <b>(-59.01%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>332.40 (n/a)</td><td>206.54 (n/a)</td><td>162.70 (n/a)</td><td>162.40 (n/a)</td><td>73.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 (+17.35%)</td><td>0.19 (-11.03%)</td><td>0.18 (-18.57%)</td><td>0.13 <b>(-21.72%)</b></td><td>0.06 <b>(+91.11%)</b></td><td>274.90 <b>(+27.74%)</b></td><td>196.58 (+18.36%)</td><td>196.30 <b>(+22.84%)</b></td><td>118.40 (-14.82%)</td><td>55.53 <b>(+92.12%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>215.20 (n/a)</td><td>166.08 (n/a)</td><td>159.80 (n/a)</td><td>139.00 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.91 (-14.95%)</td><td>0.68 <b>(-20.87%)</b></td><td>0.64 <b>(-24.86%)</b></td><td>0.53 <b>(-26.47%)</b></td><td>0.15 (+14.10%)</td><td>245.80 <b>(+36.03%)</b></td><td>200.96 <b>(+28.77%)</b></td><td>204.20 <b>(+33.12%)</b></td><td>144.50 (+17.58%)</td><td>40.72 <b>(+84.55%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>1.07 (n/a)</td><td>0.85 (n/a)</td><td>0.85 (n/a)</td><td>0.73 (n/a)</td><td>0.13 (n/a)</td><td>180.70 (n/a)</td><td>156.06 (n/a)</td><td>153.40 (n/a)</td><td>122.90 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.94 <b>(+25.21%)</b></td><td>0.76 (+9.49%)</td><td>0.72 (+2.09%)</td><td>0.63 (-1.85%)</td><td>0.12 <b>(+137.26%)</b></td><td>208.20 (+1.86%)</td><td>174.74 (-7.39%)</td><td>180.80 (-2.06%)</td><td>139.30 <b>(-20.17%)</b></td><td>25.70 <b>(+89.58%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.75 (n/a)</td><td>0.70 (n/a)</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.05 (n/a)</td><td>204.40 (n/a)</td><td>188.68 (n/a)</td><td>184.60 (n/a)</td><td>174.50 (n/a)</td><td>13.55 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.16 <b>(+31.18%)</b></td><td>0.80 (+3.12%)</td><td>0.73 (-14.65%)</td><td>0.61 (+1.99%)</td><td>0.21 <b>(+58.13%)</b></td><td>213.30 (-1.98%)</td><td>171.40 (-1.10%)</td><td>179.70 (+17.14%)</td><td>113.00 <b>(-23.75%)</b></td><td>36.85 (+14.46%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.88 (n/a)</td><td>0.78 (n/a)</td><td>0.85 (n/a)</td><td>0.60 (n/a)</td><td>0.13 (n/a)</td><td>217.60 (n/a)</td><td>173.30 (n/a)</td><td>153.40 (n/a)</td><td>148.20 (n/a)</td><td>32.19 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.00 (+0.00%)</td><td>0.00 (+0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+8.40%)</td><td>1035.23 (+0.15%)</td><td>952.12 (-0.77%)</td><td>928.26 (-1.35%)</td><td>905.79 (-1.55%)</td><td>52.44 (+17.58%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1033.64 (n/a)</td><td>959.47 (n/a)</td><td>940.92 (n/a)</td><td>920.01 (n/a)</td><td>44.60 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.01 (+2.41%)</td><td>0.01 (+1.24%)</td><td>0.01 (+2.44%)</td><td>0.01 (-1.32%)</td><td>0.00 <b>(+55.84%)</b></td><td>1091.94 (+0.85%)</td><td>1000.87 (-1.49%)</td><td>976.35 (-2.05%)</td><td>958.67 (-2.78%)</td><td>56.50 <b>(+44.71%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1082.79 (n/a)</td><td>1016.00 (n/a)</td><td>996.83 (n/a)</td><td>986.05 (n/a)</td><td>39.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.97 (+0.94%)</td><td>0.95 (+0.25%)</td><td>0.95 (-0.45%)</td><td>0.94 (+1.49%)</td><td>0.01 (-8.00%)</td><td>2230.78 (-1.47%)</td><td>2210.65 (-0.25%)</td><td>2218.02 (+0.45%)</td><td>2168.52 (-0.93%)</td><td>25.50 (-10.52%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.93 (n/a)</td><td>0.01 (n/a)</td><td>2264.04 (n/a)</td><td>2216.23 (n/a)</td><td>2207.98 (n/a)</td><td>2188.92 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.41 (-0.67%)</td><td>4.63 (-3.31%)</td><td>4.69 (-0.04%)</td><td>3.68 (-7.17%)</td><td>0.62 (+7.88%)</td><td>284.80 (+7.72%)</td><td>230.20 (+3.78%)</td><td>223.50 (+0.04%)</td><td>194.00 (+0.67%)</td><td>33.38 (+19.74%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.44 (n/a)</td><td>4.78 (n/a)</td><td>4.69 (n/a)</td><td>3.97 (n/a)</td><td>0.57 (n/a)</td><td>264.40 (n/a)</td><td>221.82 (n/a)</td><td>223.40 (n/a)</td><td>192.70 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.85 (+14.07%)</td><td>4.82 (+1.95%)</td><td>4.46 (-10.36%)</td><td>3.68 (-9.90%)</td><td>0.98 <b>(+99.51%)</b></td><td>285.00 (+10.98%)</td><td>225.10 (+0.49%)</td><td>235.40 (+11.56%)</td><td>179.30 (-12.32%)</td><td>45.50 <b>(+87.07%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.13 (n/a)</td><td>4.72 (n/a)</td><td>4.97 (n/a)</td><td>4.08 (n/a)</td><td>0.49 (n/a)</td><td>256.80 (n/a)</td><td>224.00 (n/a)</td><td>211.00 (n/a)</td><td>204.50 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.73 (+2.90%)</td><td>4.89 (+1.57%)</td><td>4.67 (-9.37%)</td><td>4.30 <b>(+22.67%)</b></td><td>0.56 <b>(-31.55%)</b></td><td>243.80 (-18.46%)</td><td>216.42 (-3.22%)</td><td>224.50 (+10.37%)</td><td>183.10 (-2.81%)</td><td>23.62 <b>(-47.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.57 (n/a)</td><td>4.82 (n/a)</td><td>5.15 (n/a)</td><td>3.51 (n/a)</td><td>0.82 (n/a)</td><td>299.00 (n/a)</td><td>223.62 (n/a)</td><td>203.40 (n/a)</td><td>188.40 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.17 (-4.17%)</td><td>4.57 (-6.52%)</td><td>5.08 (-0.36%)</td><td>2.77 <b>(-32.67%)</b></td><td>1.02 <b>(+109.29%)</b></td><td>378.00 <b>(+48.53%)</b></td><td>242.84 (+12.33%)</td><td>206.50 (+0.34%)</td><td>202.70 (+4.38%)</td><td>76.01 <b>(+224.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.40 (n/a)</td><td>4.89 (n/a)</td><td>5.10 (n/a)</td><td>4.12 (n/a)</td><td>0.49 (n/a)</td><td>254.50 (n/a)</td><td>216.18 (n/a)</td><td>205.80 (n/a)</td><td>194.20 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.26 (+10.64%)</td><td>7.85 (-1.20%)</td><td>8.06 (+1.07%)</td><td>6.75 (-5.97%)</td><td>1.00 <b>(+113.78%)</b></td><td>310.50 (+6.34%)</td><td>270.56 (+2.21%)</td><td>260.10 (-1.07%)</td><td>226.60 (-9.61%)</td><td>33.76 <b>(+106.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.37 (n/a)</td><td>7.95 (n/a)</td><td>7.98 (n/a)</td><td>7.18 (n/a)</td><td>0.47 (n/a)</td><td>292.00 (n/a)</td><td>264.72 (n/a)</td><td>262.90 (n/a)</td><td>250.70 (n/a)</td><td>16.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.12 (+5.53%)</td><td>7.61 (-1.77%)</td><td>7.91 (+1.61%)</td><td>5.63 (-15.33%)</td><td>1.59 <b>(+122.97%)</b></td><td>372.60 (+18.10%)</td><td>286.12 (+4.95%)</td><td>265.20 (-1.60%)</td><td>229.90 (-5.27%)</td><td>63.70 <b>(+140.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.64 (n/a)</td><td>7.75 (n/a)</td><td>7.78 (n/a)</td><td>6.65 (n/a)</td><td>0.71 (n/a)</td><td>315.50 (n/a)</td><td>272.62 (n/a)</td><td>269.50 (n/a)</td><td>242.70 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.44 (+10.11%)</td><td>7.86 (+0.46%)</td><td>7.69 (-3.57%)</td><td>6.18 (-6.18%)</td><td>1.22 <b>(+55.43%)</b></td><td>339.60 (+6.59%)</td><td>272.34 (+0.69%)</td><td>272.80 (+3.69%)</td><td>222.20 (-9.19%)</td><td>44.26 <b>(+50.30%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.57 (n/a)</td><td>7.82 (n/a)</td><td>7.97 (n/a)</td><td>6.58 (n/a)</td><td>0.79 (n/a)</td><td>318.60 (n/a)</td><td>270.48 (n/a)</td><td>263.10 (n/a)</td><td>244.70 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.95 (+6.99%)</td><td>8.72 (+0.12%)</td><td>8.67 (-2.28%)</td><td>6.55 (-16.89%)</td><td>1.38 <b>(+138.43%)</b></td><td>320.20 <b>(+20.33%)</b></td><td>245.96 (+1.81%)</td><td>242.00 (+2.33%)</td><td>210.70 (-6.56%)</td><td>44.40 <b>(+169.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>9.30 (n/a)</td><td>8.71 (n/a)</td><td>8.87 (n/a)</td><td>7.88 (n/a)</td><td>0.58 (n/a)</td><td>266.10 (n/a)</td><td>241.58 (n/a)</td><td>236.50 (n/a)</td><td>225.50 (n/a)</td><td>16.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>10.73 <b>(+20.30%)</b></td><td>9.29 (+17.30%)</td><td>9.73 (+13.22%)</td><td>7.23 (+13.61%)</td><td>1.53 <b>(+27.40%)</b></td><td>290.00 (-11.96%)</td><td>231.08 (-14.45%)</td><td>215.50 (-11.72%)</td><td>195.40 (-16.89%)</td><td>40.80 (-6.58%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.92 (n/a)</td><td>7.92 (n/a)</td><td>8.59 (n/a)</td><td>6.37 (n/a)</td><td>1.20 (n/a)</td><td>329.40 (n/a)</td><td>270.10 (n/a)</td><td>244.10 (n/a)</td><td>235.10 (n/a)</td><td>43.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>8.13 <b>(-22.83%)</b></td><td>7.39 (-18.76%)</td><td>7.32 (-17.65%)</td><td>6.50 (-11.35%)</td><td>0.61 <b>(-49.64%)</b></td><td>322.90 (+12.82%)</td><td>285.28 <b>(+21.91%)</b></td><td>286.40 <b>(+21.41%)</b></td><td>258.00 <b>(+29.58%)</b></td><td>24.41 <b>(-26.52%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>10.53 (n/a)</td><td>9.10 (n/a)</td><td>8.89 (n/a)</td><td>7.33 (n/a)</td><td>1.21 (n/a)</td><td>286.20 (n/a)</td><td>234.00 (n/a)</td><td>235.90 (n/a)</td><td>199.10 (n/a)</td><td>33.22 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.29 (+2.26%)</td><td>11.23 (+3.43%)</td><td>11.29 (+2.84%)</td><td>10.15 (+5.92%)</td><td>0.76 (-15.46%)</td><td>413.10 (-5.60%)</td><td>374.94 (-3.51%)</td><td>371.60 (-2.77%)</td><td>341.20 (-2.21%)</td><td>25.75 <b>(-22.24%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>12.02 (n/a)</td><td>10.86 (n/a)</td><td>10.98 (n/a)</td><td>9.59 (n/a)</td><td>0.90 (n/a)</td><td>437.60 (n/a)</td><td>388.58 (n/a)</td><td>382.20 (n/a)</td><td>348.90 (n/a)</td><td>33.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.69 (+3.24%)</td><td>11.91 (+8.87%)</td><td>12.11 (+6.92%)</td><td>11.11 (+16.01%)</td><td>0.67 <b>(-47.80%)</b></td><td>377.50 (-13.81%)</td><td>352.94 (-8.96%)</td><td>346.40 (-6.48%)</td><td>330.50 (-3.14%)</td><td>20.11 <b>(-57.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>12.29 (n/a)</td><td>10.94 (n/a)</td><td>11.32 (n/a)</td><td>9.58 (n/a)</td><td>1.29 (n/a)</td><td>438.00 (n/a)</td><td>387.68 (n/a)</td><td>370.40 (n/a)</td><td>341.20 (n/a)</td><td>46.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.79 (+7.99%)</td><td>11.68 (+7.39%)</td><td>11.75 (+9.66%)</td><td>10.41 (+2.66%)</td><td>0.86 (+11.32%)</td><td>403.00 (-2.59%)</td><td>360.78 (-6.84%)</td><td>357.00 (-8.81%)</td><td>327.90 (-7.40%)</td><td>27.41 (+0.57%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>11.85 (n/a)</td><td>10.87 (n/a)</td><td>10.71 (n/a)</td><td>10.14 (n/a)</td><td>0.78 (n/a)</td><td>413.70 (n/a)</td><td>387.26 (n/a)</td><td>391.50 (n/a)</td><td>354.10 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.03 (-14.67%)</td><td>12.52 (-1.68%)</td><td>12.42 (-0.47%)</td><td>11.91 (+4.91%)</td><td>0.45 <b>(-70.68%)</b></td><td>352.20 (-4.68%)</td><td>335.42 (+0.74%)</td><td>337.60 (+0.48%)</td><td>321.90 (+17.18%)</td><td>12.06 <b>(-66.83%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>15.27 (n/a)</td><td>12.73 (n/a)</td><td>12.48 (n/a)</td><td>11.35 (n/a)</td><td>1.53 (n/a)</td><td>369.50 (n/a)</td><td>332.94 (n/a)</td><td>336.00 (n/a)</td><td>274.70 (n/a)</td><td>36.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.78 (-17.92%)</td><td>12.51 (-3.40%)</td><td>12.46 (+0.49%)</td><td>12.25 (+7.96%)</td><td>0.24 <b>(-85.62%)</b></td><td>342.30 (-7.36%)</td><td>335.36 (+2.31%)</td><td>336.50 (-0.50%)</td><td>328.30 <b>(+21.86%)</b></td><td>6.35 <b>(-83.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>15.57 (n/a)</td><td>12.95 (n/a)</td><td>12.40 (n/a)</td><td>11.35 (n/a)</td><td>1.65 (n/a)</td><td>369.50 (n/a)</td><td>327.80 (n/a)</td><td>338.20 (n/a)</td><td>269.40 (n/a)</td><td>38.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.11 (-14.02%)</td><td>11.77 (-10.11%)</td><td>12.71 (+1.24%)</td><td>9.57 (-14.22%)</td><td>1.68 (-6.46%)</td><td>438.20 (+16.57%)</td><td>362.64 (+11.55%)</td><td>330.10 (-1.23%)</td><td>319.90 (+16.33%)</td><td>55.13 <b>(+26.34%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>15.25 (n/a)</td><td>13.09 (n/a)</td><td>12.55 (n/a)</td><td>11.16 (n/a)</td><td>1.79 (n/a)</td><td>375.90 (n/a)</td><td>325.10 (n/a)</td><td>334.20 (n/a)</td><td>275.00 (n/a)</td><td>43.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>14.07 (-2.12%)</td><td>11.75 (-11.10%)</td><td>12.55 (-8.58%)</td><td>8.84 <b>(-22.42%)</b></td><td>2.19 <b>(+72.03%)</b></td><td>474.70 <b>(+28.89%)</b></td><td>367.84 (+15.05%)</td><td>334.30 (+9.39%)</td><td>298.20 (+2.16%)</td><td>74.24 <b>(+128.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>14.37 (n/a)</td><td>13.22 (n/a)</td><td>13.72 (n/a)</td><td>11.39 (n/a)</td><td>1.27 (n/a)</td><td>368.30 (n/a)</td><td>319.72 (n/a)</td><td>305.60 (n/a)</td><td>291.90 (n/a)</td><td>32.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>14.57 (+4.01%)</td><td>12.75 (+4.36%)</td><td>12.14 (-4.25%)</td><td>11.65 <b>(+26.49%)</b></td><td>1.33 <b>(-25.82%)</b></td><td>360.10 <b>(-20.93%)</b></td><td>331.68 (-5.32%)</td><td>345.40 (+4.41%)</td><td>287.90 (-3.84%)</td><td>33.22 <b>(-45.19%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>14.01 (n/a)</td><td>12.22 (n/a)</td><td>12.68 (n/a)</td><td>9.21 (n/a)</td><td>1.79 (n/a)</td><td>455.40 (n/a)</td><td>350.32 (n/a)</td><td>330.80 (n/a)</td><td>299.40 (n/a)</td><td>60.62 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>2.71 <b>(-21.84%)</b></td><td>2.45 <b>(-23.89%)</b></td><td>2.45 <b>(-27.57%)</b></td><td>2.00 <b>(-27.89%)</b></td><td>0.28 (-9.04%)</td><td>261.70 <b>(+38.69%)</b></td><td>216.56 <b>(+31.87%)</b></td><td>213.60 <b>(+38.07%)</b></td><td>193.80 <b>(+27.92%)</b></td><td>26.95 <b>(+64.76%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.46 (n/a)</td><td>3.22 (n/a)</td><td>3.39 (n/a)</td><td>2.78 (n/a)</td><td>0.30 (n/a)</td><td>188.70 (n/a)</td><td>164.22 (n/a)</td><td>154.70 (n/a)</td><td>151.50 (n/a)</td><td>16.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>6.07 (+12.93%)</td><td>4.66 (+3.92%)</td><td>4.39 (-3.32%)</td><td>3.77 (-0.28%)</td><td>0.91 <b>(+40.70%)</b></td><td>278.10 (+0.29%)</td><td>231.24 (-2.64%)</td><td>238.90 (+3.46%)</td><td>172.70 (-11.44%)</td><td>41.40 <b>(+22.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.38 (n/a)</td><td>4.49 (n/a)</td><td>4.54 (n/a)</td><td>3.78 (n/a)</td><td>0.65 (n/a)</td><td>277.30 (n/a)</td><td>237.50 (n/a)</td><td>230.90 (n/a)</td><td>195.00 (n/a)</td><td>33.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>8.00 (-9.17%)</td><td>7.11 (-10.73%)</td><td>7.15 (-11.85%)</td><td>6.09 (-7.42%)</td><td>0.76 (-8.57%)</td><td>344.40 (+8.00%)</td><td>297.80 (+11.97%)</td><td>293.40 (+13.41%)</td><td>262.00 (+10.08%)</td><td>32.85 (+6.00%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.81 (n/a)</td><td>7.96 (n/a)</td><td>8.11 (n/a)</td><td>6.58 (n/a)</td><td>0.84 (n/a)</td><td>318.90 (n/a)</td><td>265.96 (n/a)</td><td>258.70 (n/a)</td><td>238.00 (n/a)</td><td>30.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>3.84 (+9.31%)</td><td>2.58 (-14.65%)</td><td>2.54 <b>(-20.07%)</b></td><td>1.80 <b>(-20.81%)</b></td><td>0.79 <b>(+70.03%)</b></td><td>291.40 <b>(+26.26%)</b></td><td>217.04 <b>(+22.59%)</b></td><td>206.20 <b>(+25.12%)</b></td><td>136.40 (-8.52%)</td><td>59.39 <b>(+88.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.52 (n/a)</td><td>3.03 (n/a)</td><td>3.18 (n/a)</td><td>2.27 (n/a)</td><td>0.47 (n/a)</td><td>230.80 (n/a)</td><td>177.04 (n/a)</td><td>164.80 (n/a)</td><td>149.10 (n/a)</td><td>31.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 <b>(-25.31%)</b></td><td>0.17 (-16.44%)</td><td>0.17 (-19.34%)</td><td>0.14 (-10.62%)</td><td>0.02 <b>(-42.48%)</b></td><td>230.60 (+11.89%)</td><td>192.48 (+17.96%)</td><td>193.70 <b>(+24.01%)</b></td><td>165.70 <b>(+33.84%)</b></td><td>26.28 (-14.93%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.10 (n/a)</td><td>163.18 (n/a)</td><td>156.20 (n/a)</td><td>123.80 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (-13.56%)</td><td>0.17 (-11.76%)</td><td>0.18 (-8.17%)</td><td>0.14 (-8.60%)</td><td>0.02 (-4.86%)</td><td>228.60 (+9.43%)</td><td>199.32 (+13.50%)</td><td>185.20 (+8.94%)</td><td>179.40 (+15.67%)</td><td>24.31 (+18.53%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>208.90 (n/a)</td><td>175.62 (n/a)</td><td>170.00 (n/a)</td><td>155.10 (n/a)</td><td>20.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.38 <b>(-23.11%)</b></td><td>0.35 (-9.50%)</td><td>0.34 (-13.60%)</td><td>0.32 (+12.96%)</td><td>0.03 <b>(-65.84%)</b></td><td>207.40 (-11.48%)</td><td>190.80 (+7.22%)</td><td>191.80 (+15.75%)</td><td>173.80 <b>(+29.99%)</b></td><td>14.65 <b>(-61.15%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>234.30 (n/a)</td><td>177.96 (n/a)</td><td>165.70 (n/a)</td><td>133.70 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.35 (-16.24%)</td><td>0.31 (-15.50%)</td><td>0.31 (-13.66%)</td><td>0.25 (-18.32%)</td><td>0.04 (-18.29%)</td><td>264.50 <b>(+22.45%)</b></td><td>216.18 (+18.36%)</td><td>208.30 (+15.79%)</td><td>188.60 (+19.44%)</td><td>28.60 <b>(+23.10%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.04 (n/a)</td><td>216.00 (n/a)</td><td>182.64 (n/a)</td><td>179.90 (n/a)</td><td>157.90 (n/a)</td><td>23.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.36 (-12.97%)</td><td>0.32 (-16.19%)</td><td>0.34 (-11.14%)</td><td>0.27 <b>(-22.79%)</b></td><td>0.03 <b>(+36.15%)</b></td><td>240.30 <b>(+29.47%)</b></td><td>203.96 <b>(+20.06%)</b></td><td>194.20 (+12.58%)</td><td>182.00 (+14.90%)</td><td>23.18 <b>(+106.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.03 (n/a)</td><td>185.60 (n/a)</td><td>169.88 (n/a)</td><td>172.50 (n/a)</td><td>158.40 (n/a)</td><td>11.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.77 <b>(-21.95%)</b></td><td>0.66 <b>(-21.89%)</b></td><td>0.63 <b>(-29.46%)</b></td><td>0.54 (-18.73%)</td><td>0.09 <b>(-34.35%)</b></td><td>242.50 <b>(+23.03%)</b></td><td>202.90 <b>(+27.05%)</b></td><td>206.60 <b>(+41.70%)</b></td><td>171.00 <b>(+28.09%)</b></td><td>28.38 (+2.05%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.98 (n/a)</td><td>0.84 (n/a)</td><td>0.90 (n/a)</td><td>0.67 (n/a)</td><td>0.14 (n/a)</td><td>197.10 (n/a)</td><td>159.70 (n/a)</td><td>145.80 (n/a)</td><td>133.50 (n/a)</td><td>27.81 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.87 (-1.90%)</td><td>0.64 (-19.91%)</td><td>0.56 <b>(-28.88%)</b></td><td>0.43 <b>(-31.41%)</b></td><td>0.19 <b>(+75.33%)</b></td><td>307.10 <b>(+45.75%)</b></td><td>220.94 <b>(+31.68%)</b></td><td>233.20 <b>(+40.65%)</b></td><td>149.90 (+1.97%)</td><td>64.06 <b>(+150.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.89 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.62 (n/a)</td><td>0.11 (n/a)</td><td>210.70 (n/a)</td><td>167.78 (n/a)</td><td>165.80 (n/a)</td><td>147.00 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.11 <b>(+21.79%)</b></td><td>0.77 (+0.75%)</td><td>0.68 (-8.42%)</td><td>0.56 (-14.92%)</td><td>0.23 <b>(+141.08%)</b></td><td>232.60 (+17.53%)</td><td>182.28 (+4.75%)</td><td>193.60 (+9.19%)</td><td>118.10 (-17.87%)</td><td>48.84 <b>(+137.14%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.91 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.66 (n/a)</td><td>0.10 (n/a)</td><td>197.90 (n/a)</td><td>174.02 (n/a)</td><td>177.30 (n/a)</td><td>143.80 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.77 (-14.12%)</td><td>0.67 (-7.59%)</td><td>0.66 (-16.87%)</td><td>0.57 (+11.99%)</td><td>0.09 <b>(-45.60%)</b></td><td>228.60 (-10.70%)</td><td>197.04 (+5.14%)</td><td>200.00 <b>(+20.34%)</b></td><td>169.70 (+16.47%)</td><td>24.87 <b>(-44.76%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.90 (n/a)</td><td>0.73 (n/a)</td><td>0.79 (n/a)</td><td>0.51 (n/a)</td><td>0.16 (n/a)</td><td>256.00 (n/a)</td><td>187.40 (n/a)</td><td>166.20 (n/a)</td><td>145.70 (n/a)</td><td>45.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 <b>(-32.64%)</b></td><td>0.08 <b>(-28.43%)</b></td><td>0.08 <b>(-21.80%)</b></td><td>0.07 <b>(-25.89%)</b></td><td>0.01 <b>(-53.01%)</b></td><td>231.90 <b>(+34.90%)</b></td><td>208.18 <b>(+38.23%)</b></td><td>202.20 <b>(+27.81%)</b></td><td>183.60 <b>(+48.42%)</b></td><td>21.90 (-4.30%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>171.90 (n/a)</td><td>150.60 (n/a)</td><td>158.20 (n/a)</td><td>123.70 (n/a)</td><td>22.88 (n/a)</td>
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
