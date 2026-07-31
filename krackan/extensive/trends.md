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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(-29.18%)</b></td><td>0.03 <b>(-28.60%)</b></td><td>0.03 <b>(-21.77%)</b></td><td>0.02 <b>(-42.83%)</b></td><td>0.01 (+15.91%)</td><td>301.00 <b>(+74.90%)</b></td><td>210.64 <b>(+43.86%)</b></td><td>184.90 <b>(+27.78%)</b></td><td>178.70 <b>(+41.26%)</b></td><td>51.83 <b>(+189.33%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>146.42 (n/a)</td><td>144.70 (n/a)</td><td>126.50 (n/a)</td><td>17.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-4.01%)</td><td>0.04 (-14.49%)</td><td>0.03 (-15.88%)</td><td>0.03 <b>(-21.03%)</b></td><td>0.01 (+18.29%)</td><td>233.10 <b>(+26.62%)</b></td><td>181.18 (+19.48%)</td><td>180.70 (+18.88%)</td><td>127.80 (+4.16%)</td><td>42.77 <b>(+58.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>151.64 (n/a)</td><td>152.00 (n/a)</td><td>122.70 (n/a)</td><td>26.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-12.79%)</td><td>0.03 (-3.58%)</td><td>0.03 (-6.43%)</td><td>0.03 (+16.12%)</td><td>0.01 <b>(-38.12%)</b></td><td>208.20 (-13.90%)</td><td>181.14 (-0.28%)</td><td>190.10 (+6.92%)</td><td>136.10 (+14.66%)</td><td>30.32 <b>(-38.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>181.64 (n/a)</td><td>177.80 (n/a)</td><td>118.70 (n/a)</td><td>49.60 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-16.90%)</td><td>0.03 (-13.43%)</td><td>0.03 (-12.00%)</td><td>0.03 (-14.56%)</td><td>0.00 <b>(-28.03%)</b></td><td>201.30 (+17.03%)</td><td>189.90 (+15.41%)</td><td>189.10 (+13.64%)</td><td>178.70 <b>(+20.34%)</b></td><td>9.76 (+1.98%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>172.00 (n/a)</td><td>164.54 (n/a)</td><td>166.40 (n/a)</td><td>148.50 (n/a)</td><td>9.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (-6.67%)</td><td>0.03 (-13.37%)</td><td>0.03 (-17.44%)</td><td>0.03 (-12.60%)</td><td>0.00 (-4.58%)</td><td>232.00 (+14.40%)</td><td>203.82 (+15.56%)</td><td>206.50 <b>(+21.11%)</b></td><td>164.60 (+7.16%)</td><td>25.69 (+14.68%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.80 (n/a)</td><td>176.38 (n/a)</td><td>170.50 (n/a)</td><td>153.60 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-14.41%)</td><td>0.03 (-7.85%)</td><td>0.03 (-11.62%)</td><td>0.03 (+3.99%)</td><td>0.00 <b>(-57.88%)</b></td><td>212.90 (-3.84%)</td><td>199.78 (+7.09%)</td><td>202.90 (+13.16%)</td><td>180.20 (+16.86%)</td><td>12.55 <b>(-53.49%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>221.40 (n/a)</td><td>186.56 (n/a)</td><td>179.30 (n/a)</td><td>154.20 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (-2.26%)</td><td>0.03 (-9.99%)</td><td>0.03 (-14.69%)</td><td>0.03 (-1.48%)</td><td>0.00 (-17.81%)</td><td>240.00 (+1.52%)</td><td>195.12 (+10.34%)</td><td>191.30 (+17.22%)</td><td>162.90 (+2.32%)</td><td>28.54 (-14.53%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>176.84 (n/a)</td><td>163.20 (n/a)</td><td>159.20 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-12.68%)</td><td>0.03 <b>(-20.78%)</b></td><td>0.03 <b>(-27.77%)</b></td><td>0.03 (-13.53%)</td><td>0.00 (-11.17%)</td><td>236.30 (+15.66%)</td><td>215.04 <b>(+26.27%)</b></td><td>226.00 <b>(+38.48%)</b></td><td>182.30 (+14.51%)</td><td>22.09 (+15.72%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.30 (n/a)</td><td>170.30 (n/a)</td><td>163.20 (n/a)</td><td>159.20 (n/a)</td><td>19.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 <b>(+25.87%)</b></td><td>0.08 (-1.25%)</td><td>0.07 (-12.85%)</td><td>0.06 (+3.52%)</td><td>0.03 <b>(+78.58%)</b></td><td>202.90 (-3.38%)</td><td>171.04 (+5.46%)</td><td>187.60 (+14.74%)</td><td>99.10 <b>(-20.59%)</b></td><td>42.80 <b>(+33.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>162.18 (n/a)</td><td>163.50 (n/a)</td><td>124.80 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 <b>(-24.69%)</b></td><td>0.06 <b>(-21.85%)</b></td><td>0.06 <b>(-23.17%)</b></td><td>0.05 (-14.70%)</td><td>0.01 <b>(-44.81%)</b></td><td>237.40 (+17.23%)</td><td>200.24 <b>(+26.72%)</b></td><td>195.70 <b>(+30.12%)</b></td><td>179.50 <b>(+32.86%)</b></td><td>21.94 (-15.22%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>158.02 (n/a)</td><td>150.40 (n/a)</td><td>135.10 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (-6.41%)</td><td>0.07 (-3.74%)</td><td>0.07 (-12.42%)</td><td>0.07 (+13.75%)</td><td>0.01 <b>(-32.86%)</b></td><td>186.80 (-12.09%)</td><td>169.18 (+2.19%)</td><td>177.30 (+14.24%)</td><td>138.10 (+6.81%)</td><td>19.90 <b>(-37.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>165.56 (n/a)</td><td>155.20 (n/a)</td><td>129.30 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (-19.16%)</td><td>0.06 (-15.39%)</td><td>0.06 (-11.31%)</td><td>0.05 (-17.93%)</td><td>0.01 (-19.78%)</td><td>252.30 <b>(+21.83%)</b></td><td>206.90 (+18.19%)</td><td>196.90 (+12.77%)</td><td>187.50 <b>(+23.68%)</b></td><td>25.91 <b>(+23.21%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>175.06 (n/a)</td><td>174.60 (n/a)</td><td>151.60 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (+14.30%)</td><td>0.07 <b>(+23.26%)</b></td><td>0.07 <b>(+30.85%)</b></td><td>0.07 <b>(+32.55%)</b></td><td>0.01 <b>(-28.77%)</b></td><td>187.20 <b>(-24.58%)</b></td><td>169.66 <b>(-20.56%)</b></td><td>178.70 <b>(-23.60%)</b></td><td>141.20 (-12.46%)</td><td>18.56 <b>(-54.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>248.20 (n/a)</td><td>213.58 (n/a)</td><td>233.90 (n/a)</td><td>161.30 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (+2.24%)</td><td>0.07 (-2.44%)</td><td>0.07 (-3.63%)</td><td>0.06 (-10.43%)</td><td>0.01 <b>(+26.83%)</b></td><td>221.70 (+11.63%)</td><td>178.52 (+3.79%)</td><td>180.60 (+3.79%)</td><td>135.70 (-2.23%)</td><td>33.93 <b>(+37.06%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>172.00 (n/a)</td><td>174.00 (n/a)</td><td>138.80 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 <b>(+47.42%)</b></td><td>0.07 (+16.92%)</td><td>0.07 (+15.97%)</td><td>0.05 (-5.57%)</td><td>0.02 <b>(+313.62%)</b></td><td>225.20 (+5.88%)</td><td>177.50 (-11.64%)</td><td>179.00 (-13.78%)</td><td>124.90 <b>(-32.16%)</b></td><td>35.58 <b>(+186.73%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>212.70 (n/a)</td><td>200.88 (n/a)</td><td>207.60 (n/a)</td><td>184.10 (n/a)</td><td>12.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 <b>(+30.02%)</b></td><td>0.07 <b>(+29.48%)</b></td><td>0.07 (+17.93%)</td><td>0.05 <b>(+34.22%)</b></td><td>0.01 <b>(+39.20%)</b></td><td>225.00 <b>(-25.52%)</b></td><td>175.98 <b>(-22.63%)</b></td><td>180.70 (-15.24%)</td><td>137.80 <b>(-23.10%)</b></td><td>35.38 <b>(-23.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>302.10 (n/a)</td><td>227.46 (n/a)</td><td>213.20 (n/a)</td><td>179.20 (n/a)</td><td>46.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (-4.22%)</td><td>0.15 (+8.71%)</td><td>0.16 <b>(+20.45%)</b></td><td>0.12 (+13.22%)</td><td>0.03 <b>(-27.65%)</b></td><td>207.60 (-11.70%)</td><td>163.72 (-10.32%)</td><td>152.70 (-17.01%)</td><td>135.40 (+4.39%)</td><td>29.69 <b>(-33.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>235.10 (n/a)</td><td>182.56 (n/a)</td><td>184.00 (n/a)</td><td>129.70 (n/a)</td><td>44.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (+1.00%)</td><td>0.15 (+6.66%)</td><td>0.14 (+2.72%)</td><td>0.13 <b>(+30.76%)</b></td><td>0.02 <b>(-35.82%)</b></td><td>189.40 <b>(-23.51%)</b></td><td>165.54 (-8.61%)</td><td>171.30 (-2.67%)</td><td>141.70 (-0.98%)</td><td>19.82 <b>(-52.09%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>247.60 (n/a)</td><td>181.14 (n/a)</td><td>176.00 (n/a)</td><td>143.10 (n/a)</td><td>41.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (-10.92%)</td><td>0.13 (-7.20%)</td><td>0.13 (-5.37%)</td><td>0.12 (+7.47%)</td><td>0.01 <b>(-43.29%)</b></td><td>201.30 (-6.98%)</td><td>184.46 (+6.21%)</td><td>184.20 (+5.68%)</td><td>159.00 (+12.29%)</td><td>17.68 <b>(-39.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.40 (n/a)</td><td>173.68 (n/a)</td><td>174.30 (n/a)</td><td>141.60 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (+17.11%)</td><td>0.13 (+2.82%)</td><td>0.13 (-1.93%)</td><td>0.11 (-6.22%)</td><td>0.03 <b>(+90.04%)</b></td><td>232.80 (+6.64%)</td><td>189.58 (-0.80%)</td><td>187.70 (+2.01%)</td><td>145.10 (-14.65%)</td><td>35.36 <b>(+73.17%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>191.10 (n/a)</td><td>184.00 (n/a)</td><td>170.00 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (-7.66%)</td><td>0.14 (-2.51%)</td><td>0.14 (-1.37%)</td><td>0.12 (+14.86%)</td><td>0.02 <b>(-34.26%)</b></td><td>212.60 (-12.94%)</td><td>184.40 (+0.44%)</td><td>182.00 (+1.39%)</td><td>152.70 (+8.30%)</td><td>25.24 <b>(-37.35%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>244.20 (n/a)</td><td>183.60 (n/a)</td><td>179.50 (n/a)</td><td>141.00 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (-10.79%)</td><td>0.13 (-11.45%)</td><td>0.13 (-9.81%)</td><td>0.11 (-16.22%)</td><td>0.02 (-3.30%)</td><td>217.40 (+19.38%)</td><td>190.26 (+13.21%)</td><td>194.50 (+10.89%)</td><td>154.20 (+12.06%)</td><td>22.97 <b>(+28.47%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.10 (n/a)</td><td>168.06 (n/a)</td><td>175.40 (n/a)</td><td>137.60 (n/a)</td><td>17.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (-2.02%)</td><td>0.12 (-7.34%)</td><td>0.11 (-6.76%)</td><td>0.09 (-10.91%)</td><td>0.03 (-1.34%)</td><td>259.60 (+12.24%)</td><td>211.52 (+8.11%)</td><td>220.20 (+7.26%)</td><td>150.70 (+2.10%)</td><td>39.53 (+7.60%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>231.30 (n/a)</td><td>195.66 (n/a)</td><td>205.30 (n/a)</td><td>147.60 (n/a)</td><td>36.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 <b>(-22.37%)</b></td><td>0.10 <b>(-29.24%)</b></td><td>0.11 <b>(-29.56%)</b></td><td>0.07 <b>(-40.65%)</b></td><td>0.02 (-6.58%)</td><td>355.20 <b>(+68.50%)</b></td><td>251.04 <b>(+44.43%)</b></td><td>231.00 <b>(+41.98%)</b></td><td>185.20 <b>(+28.79%)</b></td><td>64.22 <b>(+106.76%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.80 (n/a)</td><td>173.82 (n/a)</td><td>162.70 (n/a)</td><td>143.80 (n/a)</td><td>31.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.41 (+18.92%)</td><td>0.31 (+1.49%)</td><td>0.27 (-11.24%)</td><td>0.27 (-0.64%)</td><td>0.06 <b>(+91.98%)</b></td><td>185.40 (+0.65%)</td><td>164.06 (+0.37%)</td><td>178.80 (+12.67%)</td><td>118.50 (-15.96%)</td><td>27.73 <b>(+60.20%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>184.20 (n/a)</td><td>163.46 (n/a)</td><td>158.70 (n/a)</td><td>141.00 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.44 <b>(+38.95%)</b></td><td>0.32 (+13.23%)</td><td>0.31 (+10.95%)</td><td>0.24 (+1.60%)</td><td>0.07 <b>(+172.74%)</b></td><td>201.50 (-1.56%)</td><td>160.04 (-8.94%)</td><td>156.30 (-9.86%)</td><td>112.60 <b>(-28.01%)</b></td><td>33.29 <b>(+86.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>204.70 (n/a)</td><td>175.76 (n/a)</td><td>173.40 (n/a)</td><td>156.40 (n/a)</td><td>17.82 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.34 (-3.78%)</td><td>0.27 (-4.32%)</td><td>0.28 (-10.16%)</td><td>0.20 (-8.40%)</td><td>0.05 (-7.36%)</td><td>244.60 (+9.20%)</td><td>184.22 (+4.43%)</td><td>178.30 (+11.30%)</td><td>143.50 (+3.91%)</td><td>37.30 (+6.16%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>224.00 (n/a)</td><td>176.40 (n/a)</td><td>160.20 (n/a)</td><td>138.10 (n/a)</td><td>35.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.41 (+12.11%)</td><td>0.30 (+0.51%)</td><td>0.28 (-2.75%)</td><td>0.25 (+6.97%)</td><td>0.07 <b>(+28.95%)</b></td><td>195.10 (-6.52%)</td><td>168.40 (+0.32%)</td><td>175.00 (+2.82%)</td><td>118.90 (-10.87%)</td><td>30.19 (+5.60%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>208.70 (n/a)</td><td>167.86 (n/a)</td><td>170.20 (n/a)</td><td>133.40 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.37 (-1.02%)</td><td>0.29 (-12.72%)</td><td>0.26 <b>(-21.24%)</b></td><td>0.21 (-14.43%)</td><td>0.07 <b>(+33.06%)</b></td><td>234.70 (+16.82%)</td><td>180.28 (+17.14%)</td><td>189.80 <b>(+26.96%)</b></td><td>132.10 (+1.07%)</td><td>42.00 <b>(+50.62%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>200.90 (n/a)</td><td>153.90 (n/a)</td><td>149.50 (n/a)</td><td>130.70 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.30 <b>(-31.74%)</b></td><td>0.28 (-19.07%)</td><td>0.29 (-2.65%)</td><td>0.24 (-11.98%)</td><td>0.03 <b>(-64.46%)</b></td><td>206.00 (+13.62%)</td><td>179.02 (+19.75%)</td><td>170.20 (+2.72%)</td><td>161.90 <b>(+46.52%)</b></td><td>18.99 <b>(-40.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.08 (n/a)</td><td>181.30 (n/a)</td><td>149.50 (n/a)</td><td>165.70 (n/a)</td><td>110.50 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.31 (-0.53%)</td><td>0.25 (-11.02%)</td><td>0.24 <b>(-21.42%)</b></td><td>0.22 (+3.11%)</td><td>0.04 (-8.72%)</td><td>224.20 (-2.99%)</td><td>196.92 (+11.94%)</td><td>203.10 <b>(+27.26%)</b></td><td>157.70 (+0.57%)</td><td>28.04 (-11.13%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>231.10 (n/a)</td><td>175.92 (n/a)</td><td>159.60 (n/a)</td><td>156.80 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.35 (+3.40%)</td><td>0.29 (+2.91%)</td><td>0.28 (+9.65%)</td><td>0.23 (-5.00%)</td><td>0.05 (+12.13%)</td><td>218.10 (+5.26%)</td><td>176.14 (-2.37%)</td><td>174.50 (-8.83%)</td><td>141.30 (-3.29%)</td><td>29.28 (+14.72%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>207.20 (n/a)</td><td>180.42 (n/a)</td><td>191.40 (n/a)</td><td>146.10 (n/a)</td><td>25.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(+25.08%)</b></td><td>0.02 <b>(+33.44%)</b></td><td>0.02 <b>(+32.11%)</b></td><td>0.02 <b>(+118.15%)</b></td><td>0.00 <b>(-30.02%)</b></td><td>171.00 <b>(-54.14%)</b></td><td>138.54 <b>(-33.92%)</b></td><td>145.00 <b>(-24.28%)</b></td><td>100.30 <b>(-20.02%)</b></td><td>26.13 <b>(-74.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>372.90 (n/a)</td><td>209.64 (n/a)</td><td>191.50 (n/a)</td><td>125.40 (n/a)</td><td>100.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 <b>(+41.20%)</b></td><td>0.02 <b>(+37.64%)</b></td><td>0.02 <b>(+47.84%)</b></td><td>0.02 <b>(+23.81%)</b></td><td>0.00 <b>(+117.45%)</b></td><td>157.90 (-19.23%)</td><td>134.28 <b>(-26.79%)</b></td><td>128.10 <b>(-32.33%)</b></td><td>115.20 <b>(-29.19%)</b></td><td>16.50 <b>(+26.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>195.50 (n/a)</td><td>183.42 (n/a)</td><td>189.30 (n/a)</td><td>162.70 (n/a)</td><td>13.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (-1.92%)</td><td>0.02 (+8.56%)</td><td>0.02 (+17.22%)</td><td>0.01 (+6.35%)</td><td>0.00 <b>(-30.40%)</b></td><td>178.20 (-5.96%)</td><td>145.30 (-9.23%)</td><td>141.60 (-14.70%)</td><td>126.20 (+2.02%)</td><td>19.73 <b>(-32.29%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>160.08 (n/a)</td><td>166.00 (n/a)</td><td>123.70 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (+14.15%)</td><td>0.02 (+0.07%)</td><td>0.02 (-1.25%)</td><td>0.01 (-7.97%)</td><td>0.00 <b>(+51.88%)</b></td><td>215.00 (+8.64%)</td><td>173.60 (+2.03%)</td><td>172.50 (+1.23%)</td><td>121.80 (-12.44%)</td><td>36.57 <b>(+42.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>197.90 (n/a)</td><td>170.14 (n/a)</td><td>170.40 (n/a)</td><td>139.10 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 <b>(+28.04%)</b></td><td>0.02 (+11.73%)</td><td>0.02 (+7.68%)</td><td>0.01 (-8.62%)</td><td>0.00 <b>(+187.48%)</b></td><td>224.40 (+9.41%)</td><td>166.70 (-7.94%)</td><td>165.00 (-7.09%)</td><td>129.80 <b>(-21.90%)</b></td><td>35.63 <b>(+146.62%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>181.08 (n/a)</td><td>177.60 (n/a)</td><td>166.20 (n/a)</td><td>14.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (-2.26%)</td><td>0.02 (+11.20%)</td><td>0.02 <b>(+28.57%)</b></td><td>0.01 (+7.39%)</td><td>0.00 (-16.04%)</td><td>208.20 (-6.89%)</td><td>170.84 (-10.71%)</td><td>157.40 <b>(-22.23%)</b></td><td>151.50 (+2.30%)</td><td>24.21 (-19.80%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.60 (n/a)</td><td>191.34 (n/a)</td><td>202.40 (n/a)</td><td>148.10 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (+6.93%)</td><td>0.02 (+18.42%)</td><td>0.02 <b>(+20.37%)</b></td><td>0.01 (+17.45%)</td><td>0.00 (+1.40%)</td><td>189.00 (-14.86%)</td><td>152.64 (-16.12%)</td><td>153.00 (-16.94%)</td><td>108.90 (-6.44%)</td><td>35.01 (-14.90%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>222.00 (n/a)</td><td>181.98 (n/a)</td><td>184.20 (n/a)</td><td>116.40 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (-1.75%)</td><td>0.01 (-0.60%)</td><td>0.01 (+9.07%)</td><td>0.01 <b>(-24.07%)</b></td><td>0.00 <b>(+44.32%)</b></td><td>306.80 <b>(+31.67%)</b></td><td>219.52 (+3.07%)</td><td>205.70 (-8.29%)</td><td>174.60 (+1.81%)</td><td>51.78 <b>(+98.61%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.00 (n/a)</td><td>212.98 (n/a)</td><td>224.30 (n/a)</td><td>171.50 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (-8.34%)</td><td>0.03 (-6.16%)</td><td>0.03 (-2.60%)</td><td>0.03 (-3.63%)</td><td>0.01 <b>(-24.01%)</b></td><td>193.80 (+3.75%)</td><td>167.54 (+5.29%)</td><td>183.90 (+2.62%)</td><td>135.40 (+9.11%)</td><td>27.53 (-13.50%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>159.12 (n/a)</td><td>179.20 (n/a)</td><td>124.10 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (+17.85%)</td><td>0.03 (+7.88%)</td><td>0.03 (+5.55%)</td><td>0.02 (-8.69%)</td><td>0.01 <b>(+88.19%)</b></td><td>212.10 (+9.50%)</td><td>165.18 (-5.32%)</td><td>163.20 (-5.23%)</td><td>124.40 (-15.14%)</td><td>32.38 <b>(+74.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>174.46 (n/a)</td><td>172.20 (n/a)</td><td>146.60 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(-22.81%)</b></td><td>0.02 (-14.35%)</td><td>0.03 (-5.34%)</td><td>0.01 <b>(-25.89%)</b></td><td>0.01 (-4.38%)</td><td>364.00 <b>(+34.96%)</b></td><td>237.72 (+19.39%)</td><td>196.80 (+5.64%)</td><td>190.00 <b>(+29.60%)</b></td><td>74.13 <b>(+63.90%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>269.70 (n/a)</td><td>199.12 (n/a)</td><td>186.30 (n/a)</td><td>146.60 (n/a)</td><td>45.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (+11.08%)</td><td>0.03 (+14.16%)</td><td>0.03 <b>(+31.45%)</b></td><td>0.02 (-0.91%)</td><td>0.01 (+5.99%)</td><td>217.80 (+0.93%)</td><td>160.04 (-12.34%)</td><td>152.40 <b>(-23.91%)</b></td><td>123.10 (-9.95%)</td><td>36.20 (-2.56%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>182.56 (n/a)</td><td>200.30 (n/a)</td><td>136.70 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (-17.35%)</td><td>0.03 (+0.55%)</td><td>0.03 (+0.31%)</td><td>0.02 (+15.37%)</td><td>0.00 <b>(-56.21%)</b></td><td>214.30 (-13.34%)</td><td>177.44 (-6.18%)</td><td>179.30 (-0.28%)</td><td>149.20 <b>(+21.01%)</b></td><td>24.39 <b>(-56.09%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.30 (n/a)</td><td>189.12 (n/a)</td><td>179.80 (n/a)</td><td>123.30 (n/a)</td><td>55.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 <b>(+22.45%)</b></td><td>0.03 <b>(+32.90%)</b></td><td>0.03 <b>(+38.58%)</b></td><td>0.02 <b>(+47.88%)</b></td><td>0.01 (+5.83%)</td><td>215.70 <b>(-32.38%)</b></td><td>163.82 <b>(-26.26%)</b></td><td>159.20 <b>(-27.83%)</b></td><td>126.90 (-18.34%)</td><td>34.65 <b>(-42.61%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>319.00 (n/a)</td><td>222.16 (n/a)</td><td>220.60 (n/a)</td><td>155.40 (n/a)</td><td>60.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 <b>(+28.24%)</b></td><td>0.03 <b>(+22.63%)</b></td><td>0.03 <b>(+21.08%)</b></td><td>0.02 (-3.24%)</td><td>0.01 <b>(+105.32%)</b></td><td>222.50 (+3.34%)</td><td>157.70 (-16.06%)</td><td>153.90 (-17.44%)</td><td>125.40 <b>(-22.06%)</b></td><td>38.95 <b>(+65.92%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.30 (n/a)</td><td>187.88 (n/a)</td><td>186.40 (n/a)</td><td>160.90 (n/a)</td><td>23.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-6.71%)</td><td>0.03 (+18.33%)</td><td>0.03 <b>(+29.29%)</b></td><td>0.02 <b>(+50.72%)</b></td><td>0.00 <b>(-53.97%)</b></td><td>233.40 <b>(-33.64%)</b></td><td>198.30 <b>(-21.65%)</b></td><td>180.60 <b>(-22.66%)</b></td><td>176.70 (+7.16%)</td><td>26.67 <b>(-68.26%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>351.70 (n/a)</td><td>253.10 (n/a)</td><td>233.50 (n/a)</td><td>164.90 (n/a)</td><td>84.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 <b>(+27.40%)</b></td><td>0.07 <b>(+21.52%)</b></td><td>0.07 <b>(+27.82%)</b></td><td>0.05 (+10.94%)</td><td>0.02 <b>(+36.73%)</b></td><td>227.40 (-9.87%)</td><td>165.02 (-16.81%)</td><td>158.10 <b>(-21.73%)</b></td><td>118.10 <b>(-21.48%)</b></td><td>39.85 (-1.10%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>198.36 (n/a)</td><td>202.00 (n/a)</td><td>150.40 (n/a)</td><td>40.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 <b>(-22.58%)</b></td><td>0.07 (-3.70%)</td><td>0.06 (+15.61%)</td><td>0.06 <b>(+26.71%)</b></td><td>0.01 <b>(-61.35%)</b></td><td>179.50 <b>(-21.10%)</b></td><td>163.10 (-3.58%)</td><td>166.10 (-13.49%)</td><td>129.20 <b>(+29.20%)</b></td><td>20.34 <b>(-60.45%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.50 (n/a)</td><td>169.16 (n/a)</td><td>192.00 (n/a)</td><td>100.00 (n/a)</td><td>51.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (+2.63%)</td><td>0.08 (+12.29%)</td><td>0.07 (+2.60%)</td><td>0.07 <b>(+32.62%)</b></td><td>0.01 <b>(-45.65%)</b></td><td>159.00 <b>(-24.61%)</b></td><td>140.64 (-14.60%)</td><td>142.00 (-2.54%)</td><td>117.90 (-2.56%)</td><td>16.24 <b>(-62.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>164.68 (n/a)</td><td>145.70 (n/a)</td><td>121.00 (n/a)</td><td>43.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 (-2.06%)</td><td>0.07 (+6.18%)</td><td>0.06 (+1.75%)</td><td>0.06 <b>(+25.97%)</b></td><td>0.01 <b>(-31.64%)</b></td><td>172.70 <b>(-20.63%)</b></td><td>157.62 (-7.32%)</td><td>166.70 (-1.71%)</td><td>138.40 (+2.06%)</td><td>17.14 <b>(-45.26%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>170.06 (n/a)</td><td>169.60 (n/a)</td><td>135.60 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (-0.48%)</td><td>0.06 (-6.88%)</td><td>0.05 (-13.96%)</td><td>0.05 (-7.65%)</td><td>0.01 <b>(+56.72%)</b></td><td>205.20 (+8.28%)</td><td>183.46 (+8.22%)</td><td>191.70 (+16.25%)</td><td>155.60 (+0.52%)</td><td>22.46 <b>(+69.24%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>169.52 (n/a)</td><td>164.90 (n/a)</td><td>154.80 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (-9.61%)</td><td>0.06 (+4.44%)</td><td>0.06 <b>(+33.82%)</b></td><td>0.04 (-7.12%)</td><td>0.01 <b>(-29.64%)</b></td><td>252.30 (+7.68%)</td><td>181.84 (-6.61%)</td><td>168.20 <b>(-25.28%)</b></td><td>146.30 (+10.58%)</td><td>41.93 (-16.19%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>234.30 (n/a)</td><td>194.70 (n/a)</td><td>225.10 (n/a)</td><td>132.30 (n/a)</td><td>50.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (+2.63%)</td><td>0.07 (+4.79%)</td><td>0.07 (+17.17%)</td><td>0.05 (+8.61%)</td><td>0.01 <b>(-21.89%)</b></td><td>205.00 (-7.91%)</td><td>163.28 (-7.20%)</td><td>157.30 (-14.65%)</td><td>120.10 (-2.52%)</td><td>33.36 <b>(-29.56%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>222.60 (n/a)</td><td>175.94 (n/a)</td><td>184.30 (n/a)</td><td>123.20 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-4.20%)</td><td>0.05 (-1.57%)</td><td>0.05 (-7.28%)</td><td>0.05 (+4.85%)</td><td>0.01 (-3.35%)</td><td>223.60 (-4.65%)</td><td>206.00 (+1.54%)</td><td>219.70 (+7.85%)</td><td>179.10 (+4.37%)</td><td>22.09 (-2.67%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>202.88 (n/a)</td><td>203.70 (n/a)</td><td>171.60 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (-8.70%)</td><td>0.12 (+14.77%)</td><td>0.12 (+12.75%)</td><td>0.09 <b>(+59.98%)</b></td><td>0.02 <b>(-50.98%)</b></td><td>234.50 <b>(-37.48%)</b></td><td>185.62 <b>(-24.17%)</b></td><td>169.00 (-11.33%)</td><td>153.70 (+9.55%)</td><td>35.80 <b>(-68.45%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>375.10 (n/a)</td><td>244.78 (n/a)</td><td>190.60 (n/a)</td><td>140.30 (n/a)</td><td>113.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (-9.46%)</td><td>0.12 (-7.14%)</td><td>0.12 (-5.16%)</td><td>0.10 (-4.71%)</td><td>0.02 <b>(-22.00%)</b></td><td>220.40 (+4.95%)</td><td>181.40 (+6.41%)</td><td>181.50 (+5.46%)</td><td>133.50 (+10.51%)</td><td>31.20 (-12.82%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>210.00 (n/a)</td><td>170.48 (n/a)</td><td>172.10 (n/a)</td><td>120.80 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (+17.10%)</td><td>0.14 (+19.61%)</td><td>0.14 (+16.84%)</td><td>0.13 <b>(+44.72%)</b></td><td>0.01 <b>(-26.11%)</b></td><td>166.00 <b>(-30.89%)</b></td><td>149.24 (-17.83%)</td><td>149.80 (-14.40%)</td><td>127.70 (-14.58%)</td><td>14.51 <b>(-58.16%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>240.20 (n/a)</td><td>181.62 (n/a)</td><td>175.00 (n/a)</td><td>149.50 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (+9.62%)</td><td>0.15 (+14.26%)</td><td>0.14 <b>(+27.47%)</b></td><td>0.12 (+3.98%)</td><td>0.02 (+11.09%)</td><td>181.00 (-3.83%)</td><td>147.72 (-12.42%)</td><td>145.90 <b>(-21.56%)</b></td><td>123.90 (-8.83%)</td><td>23.87 (-5.73%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>168.66 (n/a)</td><td>186.00 (n/a)</td><td>135.90 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (+1.07%)</td><td>0.14 (+4.49%)</td><td>0.14 (-8.98%)</td><td>0.13 <b>(+43.09%)</b></td><td>0.01 <b>(-59.99%)</b></td><td>162.30 <b>(-30.10%)</b></td><td>149.98 (-8.86%)</td><td>152.90 (+9.84%)</td><td>128.40 (-1.08%)</td><td>12.78 <b>(-72.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>232.20 (n/a)</td><td>164.56 (n/a)</td><td>139.20 (n/a)</td><td>129.80 (n/a)</td><td>45.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (-10.21%)</td><td>0.13 (-0.51%)</td><td>0.13 (+1.20%)</td><td>0.10 (+6.93%)</td><td>0.02 <b>(-31.03%)</b></td><td>211.40 (-6.46%)</td><td>169.02 (-0.87%)</td><td>161.10 (-1.17%)</td><td>152.60 (+11.39%)</td><td>24.12 <b>(-28.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>226.00 (n/a)</td><td>170.50 (n/a)</td><td>163.00 (n/a)</td><td>137.00 (n/a)</td><td>33.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (+14.77%)</td><td>0.13 (+6.94%)</td><td>0.12 (-10.33%)</td><td>0.11 <b>(+25.33%)</b></td><td>0.02 (+12.13%)</td><td>187.50 <b>(-20.21%)</b></td><td>166.68 (-6.75%)</td><td>182.30 (+11.50%)</td><td>136.60 (-12.83%)</td><td>24.92 <b>(-23.14%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>178.74 (n/a)</td><td>163.50 (n/a)</td><td>156.70 (n/a)</td><td>32.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (-4.34%)</td><td>0.11 (-2.61%)</td><td>0.11 (+2.07%)</td><td>0.08 (-9.20%)</td><td>0.02 (-6.12%)</td><td>263.20 (+10.13%)</td><td>202.20 (+2.80%)</td><td>192.80 (-2.03%)</td><td>167.70 (+4.55%)</td><td>36.04 (+12.85%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>239.00 (n/a)</td><td>196.70 (n/a)</td><td>196.80 (n/a)</td><td>160.40 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.50 (n/a)</td><td>161.34 (n/a)</td><td>157.10 (n/a)</td><td>116.20 (n/a)</td><td>31.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>162.80 (n/a)</td><td>150.30 (n/a)</td><td>130.50 (n/a)</td><td>37.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.40 (n/a)</td><td>164.12 (n/a)</td><td>157.00 (n/a)</td><td>148.20 (n/a)</td><td>18.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>191.48 (n/a)</td><td>204.10 (n/a)</td><td>143.70 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.20 (n/a)</td><td>148.72 (n/a)</td><td>136.80 (n/a)</td><td>127.30 (n/a)</td><td>22.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>222.40 (n/a)</td><td>169.34 (n/a)</td><td>192.80 (n/a)</td><td>115.70 (n/a)</td><td>47.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>170.60 (n/a)</td><td>153.50 (n/a)</td><td>154.30 (n/a)</td><td>126.90 (n/a)</td><td>18.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>181.18 (n/a)</td><td>172.20 (n/a)</td><td>154.60 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>358.00 (n/a)</td><td>205.22 (n/a)</td><td>176.20 (n/a)</td><td>143.70 (n/a)</td><td>87.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>165.00 (n/a)</td><td>144.34 (n/a)</td><td>149.70 (n/a)</td><td>125.00 (n/a)</td><td>17.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>173.10 (n/a)</td><td>153.96 (n/a)</td><td>152.70 (n/a)</td><td>132.50 (n/a)</td><td>15.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>172.90 (n/a)</td><td>152.42 (n/a)</td><td>152.20 (n/a)</td><td>139.80 (n/a)</td><td>13.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.38 (+18.10%)</td><td>0.31 (+3.83%)</td><td>0.31 (+5.80%)</td><td>0.25 (-12.40%)</td><td>0.05 <b>(+192.16%)</b></td><td>200.60 (+14.17%)</td><td>161.00 (-1.97%)</td><td>157.30 (-5.47%)</td><td>129.20 (-15.33%)</td><td>25.99 <b>(+185.79%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>175.70 (n/a)</td><td>164.24 (n/a)</td><td>166.40 (n/a)</td><td>152.60 (n/a)</td><td>9.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>208.40 (n/a)</td><td>176.58 (n/a)</td><td>193.00 (n/a)</td><td>129.10 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>191.20 (n/a)</td><td>163.66 (n/a)</td><td>161.30 (n/a)</td><td>141.10 (n/a)</td><td>19.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>199.00 (n/a)</td><td>159.84 (n/a)</td><td>153.60 (n/a)</td><td>141.60 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>166.00 (n/a)</td><td>156.70 (n/a)</td><td>135.10 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>163.16 (n/a)</td><td>164.70 (n/a)</td><td>121.10 (n/a)</td><td>30.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>171.32 (n/a)</td><td>175.40 (n/a)</td><td>121.30 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>161.68 (n/a)</td><td>163.60 (n/a)</td><td>136.60 (n/a)</td><td>22.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>164.20 (n/a)</td><td>154.20 (n/a)</td><td>129.30 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.40 (n/a)</td><td>161.08 (n/a)</td><td>154.50 (n/a)</td><td>122.20 (n/a)</td><td>36.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>244.60 (n/a)</td><td>168.26 (n/a)</td><td>156.70 (n/a)</td><td>118.30 (n/a)</td><td>50.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>182.24 (n/a)</td><td>172.30 (n/a)</td><td>162.30 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.70 (n/a)</td><td>154.82 (n/a)</td><td>155.00 (n/a)</td><td>127.30 (n/a)</td><td>27.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>228.70 (n/a)</td><td>155.06 (n/a)</td><td>147.90 (n/a)</td><td>122.10 (n/a)</td><td>43.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>168.36 (n/a)</td><td>162.30 (n/a)</td><td>152.70 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>242.90 (n/a)</td><td>190.84 (n/a)</td><td>164.50 (n/a)</td><td>152.40 (n/a)</td><td>43.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>350.30 (n/a)</td><td>193.66 (n/a)</td><td>163.70 (n/a)</td><td>132.30 (n/a)</td><td>88.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>210.50 (n/a)</td><td>155.56 (n/a)</td><td>138.20 (n/a)</td><td>120.00 (n/a)</td><td>38.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>248.20 (n/a)</td><td>197.34 (n/a)</td><td>189.20 (n/a)</td><td>160.30 (n/a)</td><td>35.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.40 (n/a)</td><td>151.94 (n/a)</td><td>148.80 (n/a)</td><td>129.30 (n/a)</td><td>15.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>293.80 (n/a)</td><td>181.96 (n/a)</td><td>152.00 (n/a)</td><td>121.60 (n/a)</td><td>67.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.50 (n/a)</td><td>158.12 (n/a)</td><td>154.00 (n/a)</td><td>140.40 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.00 (n/a)</td><td>184.72 (n/a)</td><td>187.70 (n/a)</td><td>153.60 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>167.14 (n/a)</td><td>175.00 (n/a)</td><td>117.20 (n/a)</td><td>30.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.90 (n/a)</td><td>185.38 (n/a)</td><td>182.30 (n/a)</td><td>160.90 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.20 (n/a)</td><td>210.80 (n/a)</td><td>204.90 (n/a)</td><td>188.40 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>353.50 (n/a)</td><td>238.56 (n/a)</td><td>233.10 (n/a)</td><td>183.80 (n/a)</td><td>68.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>234.00 (n/a)</td><td>182.52 (n/a)</td><td>177.30 (n/a)</td><td>109.40 (n/a)</td><td>47.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>205.00 (n/a)</td><td>196.60 (n/a)</td><td>176.70 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>168.44 (n/a)</td><td>184.40 (n/a)</td><td>135.10 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>184.32 (n/a)</td><td>200.20 (n/a)</td><td>142.30 (n/a)</td><td>32.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>183.92 (n/a)</td><td>164.80 (n/a)</td><td>137.20 (n/a)</td><td>42.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>191.62 (n/a)</td><td>193.90 (n/a)</td><td>151.80 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.90 (n/a)</td><td>200.02 (n/a)</td><td>196.40 (n/a)</td><td>186.00 (n/a)</td><td>11.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>386.30 (n/a)</td><td>236.00 (n/a)</td><td>220.30 (n/a)</td><td>162.80 (n/a)</td><td>89.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>171.30 (n/a)</td><td>182.80 (n/a)</td><td>131.60 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>188.04 (n/a)</td><td>188.80 (n/a)</td><td>167.00 (n/a)</td><td>14.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>164.32 (n/a)</td><td>167.40 (n/a)</td><td>149.20 (n/a)</td><td>13.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>272.50 (n/a)</td><td>204.82 (n/a)</td><td>190.70 (n/a)</td><td>179.90 (n/a)</td><td>38.13 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>168.86 (n/a)</td><td>155.10 (n/a)</td><td>135.90 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>196.96 (n/a)</td><td>197.30 (n/a)</td><td>152.80 (n/a)</td><td>31.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>187.36 (n/a)</td><td>195.50 (n/a)</td><td>168.90 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>215.86 (n/a)</td><td>207.00 (n/a)</td><td>194.70 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>321.50 (n/a)</td><td>232.72 (n/a)</td><td>214.40 (n/a)</td><td>188.10 (n/a)</td><td>52.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>261.00 (n/a)</td><td>210.78 (n/a)</td><td>212.60 (n/a)</td><td>179.10 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>265.20 (n/a)</td><td>195.94 (n/a)</td><td>188.00 (n/a)</td><td>146.20 (n/a)</td><td>45.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>238.90 (n/a)</td><td>178.04 (n/a)</td><td>180.80 (n/a)</td><td>119.70 (n/a)</td><td>43.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>256.60 (n/a)</td><td>207.88 (n/a)</td><td>194.90 (n/a)</td><td>156.00 (n/a)</td><td>45.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>348.10 (n/a)</td><td>243.48 (n/a)</td><td>236.20 (n/a)</td><td>166.50 (n/a)</td><td>65.64 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>274.00 (n/a)</td><td>237.98 (n/a)</td><td>236.40 (n/a)</td><td>187.80 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>4.18 (-12.90%)</td><td>3.97 (-2.11%)</td><td>4.06 (-0.49%)</td><td>3.45 (-0.71%)</td><td>0.30 <b>(-49.50%)</b></td><td>2723.50 (+0.72%)</td><td>2378.08 (+0.96%)</td><td>2313.80 (+0.49%)</td><td>2252.10 (+14.82%)</td><td>195.40 <b>(-42.43%)</b></td><td>1642.67 (-12.90%)</td><td>1563.27 (-2.11%)</td><td>1598.81 (-0.49%)</td><td>1358.30 (-0.71%)</td><td>116.51 <b>(-49.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>4.79 (n/a)</td><td>4.06 (n/a)</td><td>4.08 (n/a)</td><td>3.48 (n/a)</td><td>0.59 (n/a)</td><td>2704.10 (n/a)</td><td>2355.50 (n/a)</td><td>2302.50 (n/a)</td><td>1961.50 (n/a)</td><td>339.42 (n/a)</td><td>1886.02 (n/a)</td><td>1597.04 (n/a)</td><td>1606.69 (n/a)</td><td>1368.05 (n/a)</td><td>230.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.12 (-3.29%)</td><td>0.94 (-6.40%)</td><td>0.99 (-4.45%)</td><td>0.74 (-7.14%)</td><td>0.15 (+10.02%)</td><td>300.80 (+7.70%)</td><td>239.86 (+7.44%)</td><td>224.10 (+4.62%)</td><td>197.60 (+3.40%)</td><td>41.55 <b>(+21.44%)</b></td><td>47.75 (-3.29%)</td><td>40.24 (-6.40%)</td><td>42.10 (-4.45%)</td><td>31.38 (-7.14%)</td><td>6.54 (+10.02%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.16 (n/a)</td><td>1.01 (n/a)</td><td>1.03 (n/a)</td><td>0.79 (n/a)</td><td>0.14 (n/a)</td><td>279.30 (n/a)</td><td>223.26 (n/a)</td><td>214.20 (n/a)</td><td>191.10 (n/a)</td><td>34.21 (n/a)</td><td>49.38 (n/a)</td><td>42.99 (n/a)</td><td>44.07 (n/a)</td><td>33.79 (n/a)</td><td>5.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.14 (+1.90%)</td><td>0.96 (-9.83%)</td><td>0.97 (-10.26%)</td><td>0.78 <b>(-20.28%)</b></td><td>0.13 <b>(+141.83%)</b></td><td>283.30 <b>(+25.47%)</b></td><td>235.06 (+12.46%)</td><td>228.70 (+11.45%)</td><td>194.60 (-1.87%)</td><td>33.79 <b>(+199.59%)</b></td><td>48.49 (+1.90%)</td><td>40.80 (-9.83%)</td><td>41.26 (-10.26%)</td><td>33.31 <b>(-20.28%)</b></td><td>5.75 <b>(+141.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.12 (n/a)</td><td>1.06 (n/a)</td><td>1.08 (n/a)</td><td>0.98 (n/a)</td><td>0.06 (n/a)</td><td>225.80 (n/a)</td><td>209.02 (n/a)</td><td>205.20 (n/a)</td><td>198.30 (n/a)</td><td>11.28 (n/a)</td><td>47.59 (n/a)</td><td>45.25 (n/a)</td><td>45.98 (n/a)</td><td>41.79 (n/a)</td><td>2.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.52 (-0.77%)</td><td>0.52 (-0.26%)</td><td>0.52 (-0.12%)</td><td>0.52 (+0.19%)</td><td>0.00 <b>(-73.00%)</b></td><td>48777.00 (-0.19%)</td><td>48669.12 (+0.26%)</td><td>48650.20 (+0.12%)</td><td>48617.90 (+0.77%)</td><td>64.02 <b>(-72.83%)</b></td><td>353.36 (-0.77%)</td><td>352.99 (-0.26%)</td><td>353.13 (-0.12%)</td><td>352.21 (+0.19%)</td><td>0.46 <b>(-73.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>48868.20 (n/a)</td><td>48543.44 (n/a)</td><td>48591.00 (n/a)</td><td>48245.70 (n/a)</td><td>235.65 (n/a)</td><td>356.09 (n/a)</td><td>353.91 (n/a)</td><td>353.56 (n/a)</td><td>351.56 (n/a)</td><td>1.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.22 (-1.19%)</td><td>0.21 (-0.77%)</td><td>0.21 (-0.29%)</td><td>0.21 (-1.51%)</td><td>0.00 (+14.40%)</td><td>119505.60 (+1.54%)</td><td>117860.22 (+0.78%)</td><td>117596.90 (+0.29%)</td><td>116907.50 (+1.21%)</td><td>997.15 (+17.91%)</td><td>146.95 (-1.19%)</td><td>145.77 (-0.77%)</td><td>146.09 (-0.29%)</td><td>143.76 (-1.51%)</td><td>1.22 (+14.41%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>117696.90 (n/a)</td><td>116953.58 (n/a)</td><td>117251.50 (n/a)</td><td>115511.80 (n/a)</td><td>845.72 (n/a)</td><td>148.73 (n/a)</td><td>146.90 (n/a)</td><td>146.52 (n/a)</td><td>145.97 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.90 (+0.08%)</td><td>0.89 (-0.34%)</td><td>0.89 (-0.45%)</td><td>0.88 (-0.19%)</td><td>0.01 (+16.31%)</td><td>28739.60 (+0.19%)</td><td>28417.02 (+0.34%)</td><td>28425.30 (+0.45%)</td><td>27939.90 (-0.08%)</td><td>299.33 (+16.26%)</td><td>614.89 (+0.08%)</td><td>604.62 (-0.34%)</td><td>604.39 (-0.45%)</td><td>597.78 (-0.19%)</td><td>6.41 (+16.31%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28683.80 (n/a)</td><td>28320.44 (n/a)</td><td>28296.60 (n/a)</td><td>27962.90 (n/a)</td><td>257.46 (n/a)</td><td>614.38 (n/a)</td><td>606.66 (n/a)</td><td>607.14 (n/a)</td><td>598.94 (n/a)</td><td>5.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.53 (-2.16%)</td><td>3.41 (-1.56%)</td><td>3.36 (-4.87%)</td><td>3.32 (-0.05%)</td><td>0.10 (-19.46%)</td><td>7572.10 (+0.05%)</td><td>7378.00 (+1.55%)</td><td>7493.60 (+5.12%)</td><td>7137.50 (+2.20%)</td><td>219.13 (-18.43%)</td><td>2406.98 (-2.16%)</td><td>2330.18 (-1.56%)</td><td>2292.60 (-4.87%)</td><td>2268.83 (-0.05%)</td><td>69.88 (-19.46%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.60 (n/a)</td><td>3.47 (n/a)</td><td>3.53 (n/a)</td><td>3.33 (n/a)</td><td>0.13 (n/a)</td><td>7568.30 (n/a)</td><td>7265.58 (n/a)</td><td>7128.50 (n/a)</td><td>6983.60 (n/a)</td><td>268.65 (n/a)</td><td>2460.05 (n/a)</td><td>2367.12 (n/a)</td><td>2410.03 (n/a)</td><td>2269.97 (n/a)</td><td>86.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.25 (+0.65%)</td><td>2.96 (+4.14%)</td><td>2.89 (+3.53%)</td><td>2.66 (-1.30%)</td><td>0.25 (+13.96%)</td><td>9445.20 (+1.32%)</td><td>8539.50 (-3.85%)</td><td>8717.50 (-3.41%)</td><td>7747.80 (-0.65%)</td><td>711.65 (+14.51%)</td><td>2217.38 (+0.65%)</td><td>2023.07 (+4.14%)</td><td>1970.74 (+3.53%)</td><td>1818.89 (-1.30%)</td><td>169.06 (+13.96%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.23 (n/a)</td><td>2.85 (n/a)</td><td>2.79 (n/a)</td><td>2.70 (n/a)</td><td>0.22 (n/a)</td><td>9322.20 (n/a)</td><td>8881.88 (n/a)</td><td>9024.80 (n/a)</td><td>7798.40 (n/a)</td><td>621.46 (n/a)</td><td>2203.00 (n/a)</td><td>1942.56 (n/a)</td><td>1903.62 (n/a)</td><td>1842.91 (n/a)</td><td>148.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.33 (+0.51%)</td><td>3.23 (+0.79%)</td><td>3.28 (+3.93%)</td><td>3.10 (-1.49%)</td><td>0.11 <b>(+35.55%)</b></td><td>8126.20 (+1.52%)</td><td>7798.84 (-0.74%)</td><td>7676.90 (-3.78%)</td><td>7548.60 (-0.51%)</td><td>260.52 <b>(+36.73%)</b></td><td>2275.90 (+0.51%)</td><td>2204.82 (+0.79%)</td><td>2237.86 (+3.93%)</td><td>2114.14 (-1.49%)</td><td>72.86 <b>(+35.55%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.32 (n/a)</td><td>3.20 (n/a)</td><td>3.15 (n/a)</td><td>3.14 (n/a)</td><td>0.08 (n/a)</td><td>8004.90 (n/a)</td><td>7857.26 (n/a)</td><td>7978.90 (n/a)</td><td>7587.10 (n/a)</td><td>190.54 (n/a)</td><td>2264.35 (n/a)</td><td>2187.54 (n/a)</td><td>2153.16 (n/a)</td><td>2146.16 (n/a)</td><td>53.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.78 (-0.01%)</td><td>0.78 (-0.02%)</td><td>0.78 (-0.01%)</td><td>0.78 (-0.03%)</td><td>0.00 <b>(+64.96%)</b></td><td>96499.60 (+0.03%)</td><td>96468.02 (+0.02%)</td><td>96458.50 (+0.01%)</td><td>96440.30 (+0.01%)</td><td>24.33 <b>(+65.25%)</b></td><td>712.56 (-0.01%)</td><td>712.35 (-0.02%)</td><td>712.42 (-0.01%)</td><td>712.12 (-0.03%)</td><td>0.18 <b>(+64.99%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96468.30 (n/a)</td><td>96451.74 (n/a)</td><td>96450.90 (n/a)</td><td>96434.40 (n/a)</td><td>14.73 (n/a)</td><td>712.60 (n/a)</td><td>712.48 (n/a)</td><td>712.48 (n/a)</td><td>712.35 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.73 (-0.04%)</td><td>0.73 (+0.02%)</td><td>0.73 (-0.03%)</td><td>0.73 (+0.23%)</td><td>0.00 <b>(-84.87%)</b></td><td>103692.70 (-0.23%)</td><td>103665.12 (-0.02%)</td><td>103657.50 (+0.03%)</td><td>103642.70 (+0.04%)</td><td>20.73 <b>(-84.89%)</b></td><td>663.04 (-0.04%)</td><td>662.90 (+0.02%)</td><td>662.95 (-0.03%)</td><td>662.72 (+0.23%)</td><td>0.13 <b>(-84.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103928.20 (n/a)</td><td>103685.12 (n/a)</td><td>103629.30 (n/a)</td><td>103601.20 (n/a)</td><td>137.23 (n/a)</td><td>663.31 (n/a)</td><td>662.77 (n/a)</td><td>663.13 (n/a)</td><td>661.22 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.70 (+0.08%)</td><td>0.69 (+0.02%)</td><td>0.69 (-0.00%)</td><td>0.69 (+0.14%)</td><td>0.00 (-7.88%)</td><td>108803.80 (-0.14%)</td><td>108683.32 (-0.02%)</td><td>108723.00 (+0.00%)</td><td>108432.10 (-0.08%)</td><td>146.58 (-8.12%)</td><td>633.76 (+0.08%)</td><td>632.29 (+0.02%)</td><td>632.06 (-0.00%)</td><td>631.59 (+0.14%)</td><td>0.85 (-7.88%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108952.20 (n/a)</td><td>108707.94 (n/a)</td><td>108718.60 (n/a)</td><td>108519.40 (n/a)</td><td>159.53 (n/a)</td><td>633.25 (n/a)</td><td>632.15 (n/a)</td><td>632.09 (n/a)</td><td>630.73 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.33 (-5.44%)</td><td>6.85 (-2.99%)</td><td>7.10 (+3.23%)</td><td>6.29 (-2.79%)</td><td>0.48 (-4.80%)</td><td>1416.50 (+2.87%)</td><td>1306.82 (+3.08%)</td><td>1255.50 (-3.13%)</td><td>1216.10 (+5.76%)</td><td>93.06 (+4.95%)</td><td>441.49 (-5.44%)</td><td>412.47 (-2.99%)</td><td>427.61 (+3.23%)</td><td>379.01 (-2.79%)</td><td>28.77 (-4.79%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.75 (n/a)</td><td>7.06 (n/a)</td><td>6.88 (n/a)</td><td>6.47 (n/a)</td><td>0.50 (n/a)</td><td>1377.00 (n/a)</td><td>1267.76 (n/a)</td><td>1296.10 (n/a)</td><td>1149.90 (n/a)</td><td>88.67 (n/a)</td><td>466.90 (n/a)</td><td>425.17 (n/a)</td><td>414.23 (n/a)</td><td>389.88 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.80 (-2.90%)</td><td>6.52 (-3.45%)</td><td>6.48 (-5.07%)</td><td>6.20 (-1.28%)</td><td>0.22 (-19.81%)</td><td>1436.70 (+1.30%)</td><td>1369.02 (+3.52%)</td><td>1375.90 (+5.34%)</td><td>1311.40 (+2.98%)</td><td>46.55 (-16.99%)</td><td>409.39 (-2.90%)</td><td>392.52 (-3.45%)</td><td>390.19 (-5.07%)</td><td>373.68 (-1.28%)</td><td>13.25 (-19.81%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.00 (n/a)</td><td>6.75 (n/a)</td><td>6.82 (n/a)</td><td>6.28 (n/a)</td><td>0.27 (n/a)</td><td>1418.30 (n/a)</td><td>1322.46 (n/a)</td><td>1306.20 (n/a)</td><td>1273.40 (n/a)</td><td>56.08 (n/a)</td><td>421.61 (n/a)</td><td>406.53 (n/a)</td><td>411.03 (n/a)</td><td>378.54 (n/a)</td><td>16.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.08 (+2.51%)</td><td>6.45 (+11.53%)</td><td>6.49 (+5.30%)</td><td>5.35 <b>(+27.20%)</b></td><td>0.70 <b>(-33.80%)</b></td><td>1667.30 <b>(-21.38%)</b></td><td>1394.98 (-12.12%)</td><td>1372.30 (-5.04%)</td><td>1258.10 (-2.45%)</td><td>164.58 <b>(-49.96%)</b></td><td>426.73 (+2.51%)</td><td>388.80 (+11.53%)</td><td>391.22 (+5.30%)</td><td>322.00 <b>(+27.20%)</b></td><td>41.92 <b>(-33.80%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.91 (n/a)</td><td>5.79 (n/a)</td><td>6.17 (n/a)</td><td>4.20 (n/a)</td><td>1.05 (n/a)</td><td>2120.80 (n/a)</td><td>1587.44 (n/a)</td><td>1445.10 (n/a)</td><td>1289.70 (n/a)</td><td>328.89 (n/a)</td><td>416.29 (n/a)</td><td>348.60 (n/a)</td><td>371.52 (n/a)</td><td>253.15 (n/a)</td><td>63.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.23 (-3.40%)</td><td>7.47 (-5.76%)</td><td>7.28 (-8.05%)</td><td>7.10 (-3.27%)</td><td>0.44 (+6.72%)</td><td>4907.60 (+3.38%)</td><td>4679.26 (+6.16%)</td><td>4788.90 (+8.75%)</td><td>4236.00 (+3.52%)</td><td>262.51 (+12.95%)</td><td>506.96 (-3.40%)</td><td>460.17 (-5.76%)</td><td>448.43 (-8.05%)</td><td>437.58 (-3.27%)</td><td>27.39 (+6.72%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.52 (n/a)</td><td>7.93 (n/a)</td><td>7.92 (n/a)</td><td>7.34 (n/a)</td><td>0.42 (n/a)</td><td>4747.10 (n/a)</td><td>4407.78 (n/a)</td><td>4403.40 (n/a)</td><td>4092.00 (n/a)</td><td>232.41 (n/a)</td><td>524.81 (n/a)</td><td>488.28 (n/a)</td><td>487.69 (n/a)</td><td>452.38 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.58 (-2.34%)</td><td>7.30 (-3.21%)</td><td>7.41 (-2.36%)</td><td>6.96 (-2.41%)</td><td>0.29 <b>(+20.43%)</b></td><td>5007.10 (+2.47%)</td><td>4779.84 (+3.36%)</td><td>4707.30 (+2.41%)</td><td>4599.00 (+2.40%)</td><td>193.04 <b>(+25.70%)</b></td><td>466.95 (-2.34%)</td><td>449.86 (-3.21%)</td><td>456.20 (-2.36%)</td><td>428.89 (-2.41%)</td><td>17.98 <b>(+20.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.76 (n/a)</td><td>7.55 (n/a)</td><td>7.59 (n/a)</td><td>7.14 (n/a)</td><td>0.24 (n/a)</td><td>4886.50 (n/a)</td><td>4624.24 (n/a)</td><td>4596.40 (n/a)</td><td>4491.30 (n/a)</td><td>153.57 (n/a)</td><td>478.15 (n/a)</td><td>464.79 (n/a)</td><td>467.21 (n/a)</td><td>439.47 (n/a)</td><td>14.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.44 (+0.85%)</td><td>7.25 (-0.43%)</td><td>7.30 (+0.02%)</td><td>6.90 (-3.57%)</td><td>0.21 <b>(+152.58%)</b></td><td>5054.80 (+3.70%)</td><td>4809.56 (+0.48%)</td><td>4775.00 (-0.02%)</td><td>4687.00 (-0.85%)</td><td>141.86 <b>(+160.99%)</b></td><td>458.18 (+0.85%)</td><td>446.80 (-0.43%)</td><td>449.73 (+0.02%)</td><td>424.84 (-3.57%)</td><td>12.77 <b>(+152.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.38 (n/a)</td><td>7.28 (n/a)</td><td>7.30 (n/a)</td><td>7.15 (n/a)</td><td>0.08 (n/a)</td><td>4874.40 (n/a)</td><td>4786.36 (n/a)</td><td>4775.90 (n/a)</td><td>4727.00 (n/a)</td><td>54.35 (n/a)</td><td>454.30 (n/a)</td><td>448.71 (n/a)</td><td>449.65 (n/a)</td><td>440.56 (n/a)</td><td>5.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.79 (-0.01%)</td><td>0.79 (+0.01%)</td><td>0.79 (+0.02%)</td><td>0.79 (-0.00%)</td><td>0.00 (-5.16%)</td><td>95892.10 (+0.00%)</td><td>95791.00 (-0.01%)</td><td>95738.60 (-0.02%)</td><td>95721.40 (+0.01%)</td><td>81.10 (-5.17%)</td><td>717.91 (-0.01%)</td><td>717.39 (+0.01%)</td><td>717.78 (+0.02%)</td><td>716.63 (-0.00%)</td><td>0.61 (-5.15%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95891.20 (n/a)</td><td>95797.16 (n/a)</td><td>95754.10 (n/a)</td><td>95716.40 (n/a)</td><td>85.53 (n/a)</td><td>717.95 (n/a)</td><td>717.34 (n/a)</td><td>717.67 (n/a)</td><td>716.64 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.73 (-0.36%)</td><td>0.73 (-0.14%)</td><td>0.73 (-0.04%)</td><td>0.73 (-0.20%)</td><td>0.00 <b>(-36.58%)</b></td><td>103167.00 (+0.20%)</td><td>102980.30 (+0.14%)</td><td>102929.50 (+0.04%)</td><td>102911.00 (+0.36%)</td><td>108.32 <b>(-36.19%)</b></td><td>667.76 (-0.36%)</td><td>667.31 (-0.14%)</td><td>667.64 (-0.04%)</td><td>666.10 (-0.20%)</td><td>0.70 <b>(-36.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102965.30 (n/a)</td><td>102840.68 (n/a)</td><td>102886.50 (n/a)</td><td>102542.70 (n/a)</td><td>169.77 (n/a)</td><td>670.15 (n/a)</td><td>668.21 (n/a)</td><td>667.92 (n/a)</td><td>667.40 (n/a)</td><td>1.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.70 (-0.15%)</td><td>0.70 (-0.08%)</td><td>0.70 (+0.01%)</td><td>0.70 (-0.03%)</td><td>0.00 <b>(-46.92%)</b></td><td>107883.60 (+0.03%)</td><td>107798.04 (+0.07%)</td><td>107786.60 (-0.01%)</td><td>107713.50 (+0.15%)</td><td>74.55 <b>(-46.79%)</b></td><td>637.98 (-0.15%)</td><td>637.48 (-0.07%)</td><td>637.55 (+0.01%)</td><td>636.98 (-0.03%)</td><td>0.44 <b>(-46.92%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107848.80 (n/a)</td><td>107717.28 (n/a)</td><td>107795.40 (n/a)</td><td>107547.70 (n/a)</td><td>140.11 (n/a)</td><td>638.97 (n/a)</td><td>637.96 (n/a)</td><td>637.50 (n/a)</td><td>637.18 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>4.05 (-3.43%)</td><td>3.46 (-1.75%)</td><td>3.33 (-3.63%)</td><td>3.15 (+3.14%)</td><td>0.36 (-15.97%)</td><td>2559.30 (-3.05%)</td><td>2348.74 (+1.45%)</td><td>2417.30 (+3.76%)</td><td>1991.50 (+3.55%)</td><td>226.47 (-15.33%)</td><td>1061.49 (-3.43%)</td><td>907.30 (-1.75%)</td><td>874.51 (-3.63%)</td><td>825.96 (+3.14%)</td><td>94.58 (-15.97%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>4.19 (n/a)</td><td>3.52 (n/a)</td><td>3.46 (n/a)</td><td>3.05 (n/a)</td><td>0.43 (n/a)</td><td>2639.70 (n/a)</td><td>2315.08 (n/a)</td><td>2329.60 (n/a)</td><td>1923.30 (n/a)</td><td>267.46 (n/a)</td><td>1099.14 (n/a)</td><td>923.46 (n/a)</td><td>907.42 (n/a)</td><td>800.81 (n/a)</td><td>112.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.35 (-15.85%)</td><td>0.33 (-4.39%)</td><td>0.32 (-1.32%)</td><td>0.31 (-2.58%)</td><td>0.02 <b>(-59.05%)</b></td><td>4047.40 (+2.65%)</td><td>3809.36 (+3.66%)</td><td>3860.60 (+1.33%)</td><td>3516.70 (+18.84%)</td><td>204.70 <b>(-49.31%)</b></td><td>19.08 (-15.85%)</td><td>17.66 (-4.39%)</td><td>17.38 (-1.32%)</td><td>16.58 (-2.58%)</td><td>0.97 <b>(-59.05%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.04 (n/a)</td><td>3943.00 (n/a)</td><td>3674.82 (n/a)</td><td>3809.80 (n/a)</td><td>2959.20 (n/a)</td><td>403.83 (n/a)</td><td>22.68 (n/a)</td><td>18.47 (n/a)</td><td>17.61 (n/a)</td><td>17.02 (n/a)</td><td>2.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.14 (+2.11%)</td><td>4.58 (+0.85%)</td><td>4.73 (-4.08%)</td><td>3.23 (+2.74%)</td><td>1.09 (-4.01%)</td><td>2058.60 (-2.67%)</td><td>1523.04 (-1.55%)</td><td>1407.20 (+4.25%)</td><td>1082.50 (-2.07%)</td><td>369.82 (-9.51%)</td><td>1898.49 (+2.11%)</td><td>1413.63 (+0.85%)</td><td>1460.54 (-4.08%)</td><td>998.37 (+2.74%)</td><td>338.21 (-4.01%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.02 (n/a)</td><td>4.54 (n/a)</td><td>4.93 (n/a)</td><td>3.15 (n/a)</td><td>1.14 (n/a)</td><td>2115.00 (n/a)</td><td>1547.06 (n/a)</td><td>1349.80 (n/a)</td><td>1105.40 (n/a)</td><td>408.67 (n/a)</td><td>1859.20 (n/a)</td><td>1401.73 (n/a)</td><td>1522.60 (n/a)</td><td>971.71 (n/a)</td><td>352.32 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.46 (n/a)</td><td>13.00 (n/a)</td><td>13.24 (n/a)</td><td>12.28 (n/a)</td><td>0.48 (n/a)</td><td>13.46 (n/a)</td><td>12.99 (n/a)</td><td>13.23 (n/a)</td><td>12.27 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>24.60 (-2.14%)</td><td>23.67 (+2.93%)</td><td>23.41 (-4.93%)</td><td>22.85 <b>(+41.53%)</b></td><td>0.77 <b>(-80.09%)</b></td><td>24.58 (-2.14%)</td><td>23.66 (+2.93%)</td><td>23.40 (-4.93%)</td><td>22.84 <b>(+41.53%)</b></td><td>0.77 <b>(-80.09%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>25.14 (n/a)</td><td>23.00 (n/a)</td><td>24.62 (n/a)</td><td>16.14 (n/a)</td><td>3.85 (n/a)</td><td>25.12 (n/a)</td><td>22.99 (n/a)</td><td>24.61 (n/a)</td><td>16.13 (n/a)</td><td>3.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>41.54 (+0.05%)</td><td>37.36 (-6.42%)</td><td>39.16 (-1.55%)</td><td>25.76 <b>(-32.32%)</b></td><td>6.59 <b>(+379.41%)</b></td><td>41.51 (+0.05%)</td><td>37.34 (-6.42%)</td><td>39.14 (-1.55%)</td><td>25.74 <b>(-32.32%)</b></td><td>6.59 <b>(+379.41%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>41.52 (n/a)</td><td>39.93 (n/a)</td><td>39.78 (n/a)</td><td>38.06 (n/a)</td><td>1.37 (n/a)</td><td>41.49 (n/a)</td><td>39.90 (n/a)</td><td>39.75 (n/a)</td><td>38.04 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>45.17 (+1.03%)</td><td>43.89 (+2.11%)</td><td>43.48 (-2.05%)</td><td>42.88 (+11.06%)</td><td>1.13 <b>(-56.54%)</b></td><td>45.15 (+1.03%)</td><td>43.87 (+2.11%)</td><td>43.45 (-2.05%)</td><td>42.85 (+11.06%)</td><td>1.13 <b>(-56.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>44.71 (n/a)</td><td>42.99 (n/a)</td><td>44.39 (n/a)</td><td>38.61 (n/a)</td><td>2.60 (n/a)</td><td>44.69 (n/a)</td><td>42.96 (n/a)</td><td>44.36 (n/a)</td><td>38.59 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.43 (n/a)</td><td>13.01 (n/a)</td><td>13.16 (n/a)</td><td>12.16 (n/a)</td><td>0.52 (n/a)</td><td>13.42 (n/a)</td><td>13.00 (n/a)</td><td>13.16 (n/a)</td><td>12.15 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>25.01 (+3.95%)</td><td>24.28 (+3.66%)</td><td>24.17 (+1.23%)</td><td>23.83 (+7.18%)</td><td>0.45 <b>(-45.21%)</b></td><td>25.00 (+3.95%)</td><td>24.26 (+3.66%)</td><td>24.16 (+1.23%)</td><td>23.81 (+7.18%)</td><td>0.45 <b>(-45.21%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>24.06 (n/a)</td><td>23.42 (n/a)</td><td>23.88 (n/a)</td><td>22.23 (n/a)</td><td>0.83 (n/a)</td><td>24.05 (n/a)</td><td>23.40 (n/a)</td><td>23.86 (n/a)</td><td>22.22 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>42.19 (-1.16%)</td><td>37.78 (-6.93%)</td><td>39.76 (-0.86%)</td><td>25.80 <b>(-34.24%)</b></td><td>6.81 <b>(+368.45%)</b></td><td>42.16 (-1.16%)</td><td>37.76 (-6.93%)</td><td>39.74 (-0.86%)</td><td>25.78 <b>(-34.24%)</b></td><td>6.81 <b>(+368.45%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>42.68 (n/a)</td><td>40.59 (n/a)</td><td>40.11 (n/a)</td><td>39.23 (n/a)</td><td>1.45 (n/a)</td><td>42.66 (n/a)</td><td>40.57 (n/a)</td><td>40.09 (n/a)</td><td>39.21 (n/a)</td><td>1.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>44.34 (-0.73%)</td><td>43.00 (+2.75%)</td><td>43.92 (+4.78%)</td><td>39.20 (+0.68%)</td><td>2.14 (+0.31%)</td><td>44.31 (-0.73%)</td><td>42.97 (+2.75%)</td><td>43.90 (+4.78%)</td><td>39.17 (+0.68%)</td><td>2.14 (+0.31%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>44.66 (n/a)</td><td>41.85 (n/a)</td><td>41.92 (n/a)</td><td>38.93 (n/a)</td><td>2.14 (n/a)</td><td>44.64 (n/a)</td><td>41.82 (n/a)</td><td>41.89 (n/a)</td><td>38.91 (n/a)</td><td>2.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.94 (+3.90%)</td><td>9.27 (+3.44%)</td><td>9.21 (+3.39%)</td><td>8.82 (+1.66%)</td><td>0.42 (+16.09%)</td><td>9.92 (+3.90%)</td><td>9.25 (+3.44%)</td><td>9.20 (+3.39%)</td><td>8.80 (+1.66%)</td><td>0.42 (+16.09%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.57 (n/a)</td><td>8.96 (n/a)</td><td>8.91 (n/a)</td><td>8.67 (n/a)</td><td>0.36 (n/a)</td><td>9.55 (n/a)</td><td>8.94 (n/a)</td><td>8.89 (n/a)</td><td>8.66 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.93 (+3.38%)</td><td>0.84 (+3.27%)</td><td>0.84 (+4.63%)</td><td>0.69 (-5.42%)</td><td>0.09 <b>(+57.14%)</b></td><td>0.91 (+3.38%)</td><td>0.82 (+3.27%)</td><td>0.83 (+4.63%)</td><td>0.68 (-5.42%)</td><td>0.09 <b>(+57.14%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.90 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.73 (n/a)</td><td>0.06 (n/a)</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.22 (-8.00%)</td><td>1.07 (-7.90%)</td><td>1.08 (-11.04%)</td><td>0.84 (-10.27%)</td><td>0.14 (-3.48%)</td><td>1.21 (-8.00%)</td><td>1.06 (-7.90%)</td><td>1.07 (-11.04%)</td><td>0.83 (-10.27%)</td><td>0.14 (-3.48%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.33 (n/a)</td><td>1.16 (n/a)</td><td>1.22 (n/a)</td><td>0.93 (n/a)</td><td>0.15 (n/a)</td><td>1.31 (n/a)</td><td>1.15 (n/a)</td><td>1.20 (n/a)</td><td>0.92 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>16.19 (-0.55%)</td><td>15.62 (+3.17%)</td><td>15.82 (+6.68%)</td><td>14.77 (+7.28%)</td><td>0.54 <b>(-49.69%)</b></td><td>16.00 (-0.55%)</td><td>15.44 (+3.17%)</td><td>15.64 (+6.68%)</td><td>14.60 (+7.28%)</td><td>0.53 <b>(-49.69%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>16.27 (n/a)</td><td>15.14 (n/a)</td><td>14.83 (n/a)</td><td>13.76 (n/a)</td><td>1.07 (n/a)</td><td>16.09 (n/a)</td><td>14.96 (n/a)</td><td>14.66 (n/a)</td><td>13.61 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>12.37 (+0.43%)</td><td>11.98 (-0.43%)</td><td>11.94 (-1.73%)</td><td>11.56 (-1.41%)</td><td>0.30 (+16.56%)</td><td>12.16 (+0.43%)</td><td>11.77 (-0.43%)</td><td>11.73 (-1.73%)</td><td>11.35 (-1.41%)</td><td>0.29 (+16.56%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>12.32 (n/a)</td><td>12.03 (n/a)</td><td>12.15 (n/a)</td><td>11.72 (n/a)</td><td>0.26 (n/a)</td><td>12.10 (n/a)</td><td>11.82 (n/a)</td><td>11.94 (n/a)</td><td>11.52 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.00 (+12.37%)</td><td>8.04 (+7.99%)</td><td>8.12 (+11.16%)</td><td>6.97 (+0.20%)</td><td>0.83 <b>(+101.08%)</b></td><td>8.85 (+12.37%)</td><td>7.91 (+7.99%)</td><td>7.98 (+11.16%)</td><td>6.85 (+0.20%)</td><td>0.82 <b>(+101.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.01 (n/a)</td><td>7.45 (n/a)</td><td>7.31 (n/a)</td><td>6.96 (n/a)</td><td>0.41 (n/a)</td><td>7.87 (n/a)</td><td>7.32 (n/a)</td><td>7.18 (n/a)</td><td>6.84 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.78 (-2.91%)</td><td>6.17 (+2.19%)</td><td>6.01 (+2.92%)</td><td>5.67 (+6.16%)</td><td>0.51 <b>(-33.63%)</b></td><td>6.67 (-2.91%)</td><td>6.07 (+2.19%)</td><td>5.91 (+2.92%)</td><td>5.58 (+6.16%)</td><td>0.50 <b>(-33.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.98 (n/a)</td><td>6.04 (n/a)</td><td>5.84 (n/a)</td><td>5.34 (n/a)</td><td>0.76 (n/a)</td><td>6.87 (n/a)</td><td>5.94 (n/a)</td><td>5.75 (n/a)</td><td>5.26 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.61 (n/a)</td><td>12.98 (n/a)</td><td>12.74 (n/a)</td><td>12.60 (n/a)</td><td>0.43 (n/a)</td><td>13.60 (n/a)</td><td>12.97 (n/a)</td><td>12.74 (n/a)</td><td>12.59 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.20 (n/a)</td><td>12.38 (n/a)</td><td>12.58 (n/a)</td><td>10.68 (n/a)</td><td>1.01 (n/a)</td><td>13.20 (n/a)</td><td>12.38 (n/a)</td><td>12.57 (n/a)</td><td>10.67 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.80 (n/a)</td><td>167.22 (n/a)</td><td>163.30 (n/a)</td><td>128.30 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.20 (n/a)</td><td>166.58 (n/a)</td><td>157.50 (n/a)</td><td>139.70 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>172.88 (n/a)</td><td>171.50 (n/a)</td><td>125.30 (n/a)</td><td>33.95 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.30 (n/a)</td><td>179.62 (n/a)</td><td>162.70 (n/a)</td><td>155.10 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.90 (n/a)</td><td>218.42 (n/a)</td><td>215.00 (n/a)</td><td>171.80 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.80 (n/a)</td><td>194.82 (n/a)</td><td>187.10 (n/a)</td><td>169.40 (n/a)</td><td>23.36 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.00 (n/a)</td><td>210.48 (n/a)</td><td>203.40 (n/a)</td><td>186.80 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>254.20 (n/a)</td><td>214.20 (n/a)</td><td>239.70 (n/a)</td><td>164.90 (n/a)</td><td>42.24 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>168.90 (n/a)</td><td>160.10 (n/a)</td><td>124.40 (n/a)</td><td>47.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>172.08 (n/a)</td><td>177.40 (n/a)</td><td>134.10 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>175.12 (n/a)</td><td>176.90 (n/a)</td><td>147.20 (n/a)</td><td>21.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.00 (n/a)</td><td>186.36 (n/a)</td><td>189.60 (n/a)</td><td>132.40 (n/a)</td><td>42.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.90 (n/a)</td><td>146.40 (n/a)</td><td>141.30 (n/a)</td><td>126.30 (n/a)</td><td>23.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>192.30 (n/a)</td><td>193.80 (n/a)</td><td>177.70 (n/a)</td><td>12.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>190.74 (n/a)</td><td>180.90 (n/a)</td><td>163.50 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>386.90 (n/a)</td><td>257.04 (n/a)</td><td>226.10 (n/a)</td><td>187.00 (n/a)</td><td>79.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.00 (n/a)</td><td>199.20 (n/a)</td><td>191.60 (n/a)</td><td>151.40 (n/a)</td><td>35.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>264.90 (n/a)</td><td>205.10 (n/a)</td><td>213.80 (n/a)</td><td>142.90 (n/a)</td><td>48.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>238.30 (n/a)</td><td>182.86 (n/a)</td><td>178.60 (n/a)</td><td>145.00 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>197.72 (n/a)</td><td>204.10 (n/a)</td><td>164.00 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>248.40 (n/a)</td><td>203.52 (n/a)</td><td>203.20 (n/a)</td><td>160.80 (n/a)</td><td>31.85 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.20 (n/a)</td><td>206.38 (n/a)</td><td>209.10 (n/a)</td><td>173.10 (n/a)</td><td>31.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>195.34 (n/a)</td><td>190.00 (n/a)</td><td>157.50 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.20 (n/a)</td><td>211.92 (n/a)</td><td>218.20 (n/a)</td><td>165.80 (n/a)</td><td>32.80 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 <b>(-24.31%)</b></td><td>0.16 (-10.39%)</td><td>0.15 (-10.05%)</td><td>0.14 (+8.89%)</td><td>0.01 <b>(-64.58%)</b></td><td>229.30 (-8.13%)</td><td>210.66 (+7.99%)</td><td>216.40 (+11.20%)</td><td>184.70 <b>(+32.12%)</b></td><td>18.15 <b>(-56.74%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>249.60 (n/a)</td><td>195.08 (n/a)</td><td>194.60 (n/a)</td><td>139.80 (n/a)</td><td>41.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>181.06 (n/a)</td><td>180.70 (n/a)</td><td>162.40 (n/a)</td><td>13.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>307.90 (n/a)</td><td>202.72 (n/a)</td><td>174.10 (n/a)</td><td>149.90 (n/a)</td><td>63.80 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>275.20 (n/a)</td><td>186.28 (n/a)</td><td>176.10 (n/a)</td><td>133.40 (n/a)</td><td>57.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>195.40 (n/a)</td><td>169.40 (n/a)</td><td>190.10 (n/a)</td><td>134.10 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>313.30 (n/a)</td><td>202.74 (n/a)</td><td>181.00 (n/a)</td><td>144.30 (n/a)</td><td>66.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>216.70 (n/a)</td><td>184.22 (n/a)</td><td>181.20 (n/a)</td><td>136.80 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>246.20 (n/a)</td><td>227.40 (n/a)</td><td>229.70 (n/a)</td><td>206.10 (n/a)</td><td>17.85 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-17.60%)</td><td>0.03 (-6.36%)</td><td>0.03 (-6.79%)</td><td>0.02 <b>(+38.89%)</b></td><td>0.00 <b>(-55.18%)</b></td><td>175.20 <b>(-27.99%)</b></td><td>154.32 (+0.59%)</td><td>154.40 (+7.30%)</td><td>133.90 <b>(+21.40%)</b></td><td>19.35 <b>(-62.94%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.30 (n/a)</td><td>153.42 (n/a)</td><td>143.90 (n/a)</td><td>110.30 (n/a)</td><td>52.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+16.48%)</td><td>0.03 (-1.65%)</td><td>0.02 (-4.53%)</td><td>0.02 (-6.84%)</td><td>0.00 <b>(+124.15%)</b></td><td>182.80 (+7.34%)</td><td>162.38 (+3.09%)</td><td>168.60 (+4.72%)</td><td>124.40 (-14.15%)</td><td>22.19 <b>(+101.37%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.30 (n/a)</td><td>157.52 (n/a)</td><td>161.00 (n/a)</td><td>144.90 (n/a)</td><td>11.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (+7.42%)</td><td>0.03 (-10.42%)</td><td>0.02 (-12.82%)</td><td>0.02 <b>(-25.88%)</b></td><td>0.01 <b>(+139.29%)</b></td><td>205.50 <b>(+34.93%)</b></td><td>163.26 (+14.96%)</td><td>164.80 (+14.68%)</td><td>115.70 (-6.92%)</td><td>32.10 <b>(+193.16%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>152.30 (n/a)</td><td>142.02 (n/a)</td><td>143.70 (n/a)</td><td>124.30 (n/a)</td><td>10.95 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-7.27%)</td><td>0.03 (+3.12%)</td><td>0.03 (-1.11%)</td><td>0.02 <b>(+36.75%)</b></td><td>0.00 <b>(-49.51%)</b></td><td>180.10 <b>(-26.88%)</b></td><td>155.68 (-8.64%)</td><td>150.00 (+1.15%)</td><td>126.50 (+7.84%)</td><td>21.35 <b>(-60.45%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.30 (n/a)</td><td>170.40 (n/a)</td><td>148.30 (n/a)</td><td>117.30 (n/a)</td><td>53.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+5.37%)</td><td>0.02 (-2.63%)</td><td>0.02 (+2.79%)</td><td>0.01 <b>(-25.34%)</b></td><td>0.01 <b>(+63.23%)</b></td><td>274.80 <b>(+33.92%)</b></td><td>187.14 (+6.32%)</td><td>166.90 (-2.74%)</td><td>145.70 (-5.08%)</td><td>51.38 <b>(+117.65%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.20 (n/a)</td><td>176.02 (n/a)</td><td>171.60 (n/a)</td><td>153.50 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+9.77%)</td><td>0.02 (-0.37%)</td><td>0.02 (-1.63%)</td><td>0.02 (-6.25%)</td><td>0.00 <b>(+48.97%)</b></td><td>200.60 (+6.65%)</td><td>171.58 (+1.78%)</td><td>181.30 (+1.68%)</td><td>125.20 (-8.95%)</td><td>29.11 <b>(+42.03%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.10 (n/a)</td><td>168.58 (n/a)</td><td>178.30 (n/a)</td><td>137.50 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-10.46%)</td><td>0.02 (-2.09%)</td><td>0.02 (-2.13%)</td><td>0.02 (+9.32%)</td><td>0.00 <b>(-33.19%)</b></td><td>220.30 (-8.51%)</td><td>175.08 (+0.22%)</td><td>169.90 (+2.23%)</td><td>152.30 (+11.66%)</td><td>26.51 <b>(-32.61%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.80 (n/a)</td><td>174.70 (n/a)</td><td>166.20 (n/a)</td><td>136.40 (n/a)</td><td>39.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+8.73%)</td><td>0.02 (+5.43%)</td><td>0.02 (+4.64%)</td><td>0.01 (-16.42%)</td><td>0.00 <b>(+66.89%)</b></td><td>283.50 (+19.67%)</td><td>207.64 (-2.66%)</td><td>207.30 (-4.47%)</td><td>159.40 (-8.07%)</td><td>47.98 <b>(+84.79%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.90 (n/a)</td><td>213.32 (n/a)</td><td>217.00 (n/a)</td><td>173.40 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (+7.40%)</td><td>0.06 (+5.68%)</td><td>0.05 (-3.59%)</td><td>0.05 (+3.23%)</td><td>0.01 <b>(+35.58%)</b></td><td>168.10 (-3.11%)</td><td>144.58 (-4.58%)</td><td>151.20 (+3.77%)</td><td>117.60 (-6.89%)</td><td>23.08 (+19.98%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.50 (n/a)</td><td>151.52 (n/a)</td><td>145.70 (n/a)</td><td>126.30 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-2.65%)</td><td>0.05 (-11.40%)</td><td>0.05 (-14.10%)</td><td>0.05 (-17.32%)</td><td>0.01 <b>(+59.96%)</b></td><td>177.80 <b>(+20.95%)</b></td><td>155.04 (+13.90%)</td><td>162.00 (+16.38%)</td><td>126.80 (+2.67%)</td><td>19.47 <b>(+97.12%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>147.00 (n/a)</td><td>136.12 (n/a)</td><td>139.20 (n/a)</td><td>123.50 (n/a)</td><td>9.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-11.19%)</td><td>0.06 (-9.88%)</td><td>0.05 (-11.02%)</td><td>0.04 (-11.75%)</td><td>0.01 (-17.92%)</td><td>186.20 (+13.33%)</td><td>150.72 (+10.69%)</td><td>151.20 (+12.42%)</td><td>130.00 (+12.65%)</td><td>22.57 (+6.21%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.30 (n/a)</td><td>136.16 (n/a)</td><td>134.50 (n/a)</td><td>115.40 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (+9.12%)</td><td>0.05 (+2.90%)</td><td>0.05 (-2.08%)</td><td>0.04 (+0.13%)</td><td>0.01 <b>(+44.16%)</b></td><td>191.30 (-0.16%)</td><td>156.94 (-1.94%)</td><td>153.30 (+2.13%)</td><td>134.10 (-8.34%)</td><td>24.80 <b>(+29.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>160.04 (n/a)</td><td>150.10 (n/a)</td><td>146.30 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (-7.40%)</td><td>0.05 (+1.16%)</td><td>0.05 (+2.50%)</td><td>0.04 <b>(+23.16%)</b></td><td>0.01 <b>(-47.26%)</b></td><td>191.70 (-18.81%)</td><td>155.96 (-6.88%)</td><td>151.20 (-2.45%)</td><td>124.60 (+7.97%)</td><td>25.01 <b>(-53.11%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>236.10 (n/a)</td><td>167.48 (n/a)</td><td>155.00 (n/a)</td><td>115.40 (n/a)</td><td>53.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 <b>(+30.19%)</b></td><td>0.06 <b>(+36.29%)</b></td><td>0.07 <b>(+36.50%)</b></td><td>0.05 <b>(+41.42%)</b></td><td>0.01 (+18.79%)</td><td>169.60 <b>(-29.27%)</b></td><td>131.60 <b>(-27.08%)</b></td><td>124.10 <b>(-26.74%)</b></td><td>115.20 <b>(-23.20%)</b></td><td>22.20 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>180.48 (n/a)</td><td>169.40 (n/a)</td><td>150.00 (n/a)</td><td>34.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (+0.66%)</td><td>0.05 (+11.24%)</td><td>0.05 (-4.07%)</td><td>0.05 <b>(+39.11%)</b></td><td>0.01 <b>(-29.93%)</b></td><td>167.50 <b>(-28.11%)</b></td><td>152.34 (-12.26%)</td><td>164.10 (+4.26%)</td><td>131.10 (-0.61%)</td><td>19.16 <b>(-50.96%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>173.62 (n/a)</td><td>157.40 (n/a)</td><td>131.90 (n/a)</td><td>39.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-19.83%)</td><td>0.04 <b>(-24.77%)</b></td><td>0.04 (-15.91%)</td><td>0.03 <b>(-36.59%)</b></td><td>0.01 <b>(+37.36%)</b></td><td>323.90 <b>(+57.69%)</b></td><td>239.08 <b>(+40.32%)</b></td><td>205.50 (+18.92%)</td><td>167.30 <b>(+24.66%)</b></td><td>73.63 <b>(+186.22%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>170.38 (n/a)</td><td>172.80 (n/a)</td><td>134.20 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (+6.86%)</td><td>0.05 (+6.62%)</td><td>0.05 (+13.83%)</td><td>0.03 (-0.04%)</td><td>0.01 <b>(+21.28%)</b></td><td>272.10 (+0.04%)</td><td>185.06 (-4.76%)</td><td>162.00 (-12.15%)</td><td>137.30 (-6.41%)</td><td>53.81 (+12.87%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.00 (n/a)</td><td>194.30 (n/a)</td><td>184.40 (n/a)</td><td>146.70 (n/a)</td><td>47.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (-5.15%)</td><td>0.04 (-17.38%)</td><td>0.04 (-9.12%)</td><td>0.03 <b>(-33.78%)</b></td><td>0.01 <b>(+137.30%)</b></td><td>322.40 <b>(+51.01%)</b></td><td>244.98 <b>(+26.43%)</b></td><td>214.10 (+10.02%)</td><td>186.90 (+5.47%)</td><td>62.16 <b>(+288.56%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.50 (n/a)</td><td>193.76 (n/a)</td><td>194.60 (n/a)</td><td>177.20 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+2.61%)</td><td>0.10 (-8.45%)</td><td>0.10 (-14.79%)</td><td>0.08 (-8.39%)</td><td>0.02 (+14.93%)</td><td>202.50 (+9.16%)</td><td>169.24 (+9.75%)</td><td>171.00 (+17.36%)</td><td>133.10 (-2.56%)</td><td>24.65 <b>(+20.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>154.20 (n/a)</td><td>145.70 (n/a)</td><td>136.60 (n/a)</td><td>20.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (-13.29%)</td><td>0.10 (-10.16%)</td><td>0.11 (+0.54%)</td><td>0.08 (-16.78%)</td><td>0.01 <b>(-21.33%)</b></td><td>198.70 <b>(+20.13%)</b></td><td>161.70 (+10.97%)</td><td>155.40 (-0.58%)</td><td>133.80 (+15.25%)</td><td>24.22 (+9.36%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>165.40 (n/a)</td><td>145.72 (n/a)</td><td>156.30 (n/a)</td><td>116.10 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+2.80%)</td><td>0.10 (-4.33%)</td><td>0.11 (+4.99%)</td><td>0.08 (-17.91%)</td><td>0.02 <b>(+153.73%)</b></td><td>195.00 <b>(+21.80%)</b></td><td>161.70 (+6.89%)</td><td>146.40 (-4.75%)</td><td>132.20 (-2.72%)</td><td>29.52 <b>(+212.48%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>160.10 (n/a)</td><td>151.28 (n/a)</td><td>153.70 (n/a)</td><td>135.90 (n/a)</td><td>9.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 <b>(-21.98%)</b></td><td>0.10 (-13.46%)</td><td>0.11 (-4.80%)</td><td>0.08 <b>(-26.63%)</b></td><td>0.02 (-6.85%)</td><td>212.70 <b>(+36.35%)</b></td><td>160.36 (+16.63%)</td><td>150.90 (+5.08%)</td><td>137.90 <b>(+28.16%)</b></td><td>30.78 <b>(+69.44%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>156.00 (n/a)</td><td>137.50 (n/a)</td><td>143.60 (n/a)</td><td>107.60 (n/a)</td><td>18.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (+9.89%)</td><td>0.10 (-6.85%)</td><td>0.10 (-12.04%)</td><td>0.08 (-17.92%)</td><td>0.02 <b>(+126.00%)</b></td><td>201.40 <b>(+21.84%)</b></td><td>167.60 (+9.29%)</td><td>169.40 (+13.69%)</td><td>130.40 (-9.00%)</td><td>27.08 <b>(+146.68%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>165.30 (n/a)</td><td>153.36 (n/a)</td><td>149.00 (n/a)</td><td>143.30 (n/a)</td><td>10.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (+11.32%)</td><td>0.09 (-16.89%)</td><td>0.09 (-4.14%)</td><td>0.05 <b>(-47.22%)</b></td><td>0.04 <b>(+196.67%)</b></td><td>324.70 <b>(+89.44%)</b></td><td>222.34 <b>(+39.12%)</b></td><td>173.20 (+4.27%)</td><td>116.80 (-10.22%)</td><td>95.88 <b>(+468.61%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>171.40 (n/a)</td><td>159.82 (n/a)</td><td>166.10 (n/a)</td><td>130.10 (n/a)</td><td>16.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+5.56%)</td><td>0.10 (-0.57%)</td><td>0.10 (-7.41%)</td><td>0.08 (-8.36%)</td><td>0.02 <b>(+43.26%)</b></td><td>195.80 (+9.14%)</td><td>159.56 (+1.57%)</td><td>160.90 (+7.99%)</td><td>132.50 (-5.22%)</td><td>24.73 <b>(+46.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.40 (n/a)</td><td>157.10 (n/a)</td><td>149.00 (n/a)</td><td>139.80 (n/a)</td><td>16.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (-7.54%)</td><td>0.08 (-5.74%)</td><td>0.09 (-1.69%)</td><td>0.07 (-9.61%)</td><td>0.01 (+18.44%)</td><td>246.60 (+10.63%)</td><td>201.80 (+6.77%)</td><td>187.60 (+1.68%)</td><td>177.40 (+8.17%)</td><td>30.03 <b>(+38.39%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>189.00 (n/a)</td><td>184.50 (n/a)</td><td>164.00 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.33 <b>(+24.17%)</b></td><td>0.22 (+7.10%)</td><td>0.19 (-8.85%)</td><td>0.17 <b>(+20.77%)</b></td><td>0.07 <b>(+35.96%)</b></td><td>188.50 (-17.22%)</td><td>156.08 (-5.59%)</td><td>168.40 (+9.78%)</td><td>99.70 (-19.47%)</td><td>37.78 (-8.89%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>227.70 (n/a)</td><td>165.32 (n/a)</td><td>153.40 (n/a)</td><td>123.80 (n/a)</td><td>41.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (-3.22%)</td><td>0.21 (+5.09%)</td><td>0.21 (+4.65%)</td><td>0.18 (+18.62%)</td><td>0.02 <b>(-35.42%)</b></td><td>177.60 (-15.71%)</td><td>154.30 (-6.38%)</td><td>153.30 (-4.43%)</td><td>134.10 (+3.31%)</td><td>16.80 <b>(-44.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.70 (n/a)</td><td>164.82 (n/a)</td><td>160.40 (n/a)</td><td>129.80 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (+10.50%)</td><td>0.21 (+11.75%)</td><td>0.22 (+9.66%)</td><td>0.17 <b>(+22.99%)</b></td><td>0.03 (-14.52%)</td><td>193.60 (-18.69%)</td><td>156.02 (-11.56%)</td><td>147.70 (-8.83%)</td><td>138.50 (-9.54%)</td><td>21.75 <b>(-37.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>238.10 (n/a)</td><td>176.42 (n/a)</td><td>162.00 (n/a)</td><td>153.10 (n/a)</td><td>34.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (-8.20%)</td><td>0.21 (-11.36%)</td><td>0.21 (-12.29%)</td><td>0.19 (+5.36%)</td><td>0.03 <b>(-25.18%)</b></td><td>175.50 (-5.08%)</td><td>154.94 (+11.55%)</td><td>153.10 (+14.00%)</td><td>124.80 (+9.00%)</td><td>20.67 <b>(-24.23%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.90 (n/a)</td><td>138.90 (n/a)</td><td>134.30 (n/a)</td><td>114.50 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.28 <b>(+35.29%)</b></td><td>0.20 (+5.30%)</td><td>0.19 (-0.18%)</td><td>0.17 (-0.81%)</td><td>0.04 <b>(+203.21%)</b></td><td>197.00 (+0.82%)</td><td>168.64 (-2.53%)</td><td>173.30 (+0.17%)</td><td>119.00 <b>(-26.09%)</b></td><td>29.85 <b>(+117.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>173.02 (n/a)</td><td>173.00 (n/a)</td><td>161.00 (n/a)</td><td>13.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 <b>(+24.24%)</b></td><td>0.20 (+8.61%)</td><td>0.18 (-3.77%)</td><td>0.17 (+12.88%)</td><td>0.03 <b>(+38.27%)</b></td><td>194.00 (-11.42%)</td><td>170.78 (-7.55%)</td><td>177.80 (+3.92%)</td><td>131.70 (-19.55%)</td><td>23.33 (-4.35%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.00 (n/a)</td><td>184.72 (n/a)</td><td>171.10 (n/a)</td><td>163.70 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (+7.17%)</td><td>0.17 (+13.75%)</td><td>0.17 (+6.16%)</td><td>0.16 <b>(+30.00%)</b></td><td>0.01 <b>(-49.59%)</b></td><td>209.30 <b>(-23.08%)</b></td><td>191.92 (-13.73%)</td><td>187.30 (-5.83%)</td><td>176.30 (-6.72%)</td><td>14.09 <b>(-63.61%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>272.10 (n/a)</td><td>222.46 (n/a)</td><td>198.90 (n/a)</td><td>189.00 (n/a)</td><td>38.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (+11.40%)</td><td>0.03 (-2.25%)</td><td>0.02 (-13.04%)</td><td>0.02 (+4.00%)</td><td>0.01 <b>(+24.26%)</b></td><td>203.60 (-3.83%)</td><td>162.82 (+3.10%)</td><td>167.90 (+15.00%)</td><td>114.40 (-10.27%)</td><td>33.40 (+2.21%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>157.92 (n/a)</td><td>146.00 (n/a)</td><td>127.50 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-2.13%)</td><td>0.03 (-7.98%)</td><td>0.02 (-12.32%)</td><td>0.02 (-6.75%)</td><td>0.01 (+3.57%)</td><td>182.70 (+7.22%)</td><td>158.04 (+9.16%)</td><td>169.90 (+14.03%)</td><td>119.20 (+2.14%)</td><td>28.37 (+15.67%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>170.40 (n/a)</td><td>144.78 (n/a)</td><td>149.00 (n/a)</td><td>116.70 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-12.33%)</td><td>0.02 <b>(-22.18%)</b></td><td>0.02 (-17.17%)</td><td>0.01 <b>(-37.36%)</b></td><td>0.01 (+10.86%)</td><td>349.60 <b>(+59.63%)</b></td><td>239.46 <b>(+33.31%)</b></td><td>232.10 <b>(+20.70%)</b></td><td>163.80 (+14.07%)</td><td>71.42 <b>(+111.45%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.00 (n/a)</td><td>179.62 (n/a)</td><td>192.30 (n/a)</td><td>143.60 (n/a)</td><td>33.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-3.67%)</td><td>0.02 (-10.38%)</td><td>0.02 (-14.22%)</td><td>0.02 (+0.26%)</td><td>0.00 (-7.11%)</td><td>255.90 (-0.23%)</td><td>207.12 (+11.01%)</td><td>203.80 (+16.59%)</td><td>154.90 (+3.75%)</td><td>36.97 (-9.49%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.50 (n/a)</td><td>186.58 (n/a)</td><td>174.80 (n/a)</td><td>149.30 (n/a)</td><td>40.85 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-7.08%)</td><td>0.03 (+3.63%)</td><td>0.03 (+10.91%)</td><td>0.02 (+7.65%)</td><td>0.00 <b>(-32.37%)</b></td><td>178.70 (-7.12%)</td><td>151.32 (-4.78%)</td><td>149.00 (-9.86%)</td><td>128.50 (+7.62%)</td><td>18.71 <b>(-30.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.40 (n/a)</td><td>158.92 (n/a)</td><td>165.30 (n/a)</td><td>119.40 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-5.26%)</td><td>0.02 (-5.07%)</td><td>0.03 (-1.92%)</td><td>0.02 (-9.41%)</td><td>0.00 (+4.20%)</td><td>200.90 (+10.38%)</td><td>167.22 (+5.63%)</td><td>162.80 (+2.01%)</td><td>141.20 (+5.53%)</td><td>21.62 <b>(+23.86%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.00 (n/a)</td><td>158.30 (n/a)</td><td>159.60 (n/a)</td><td>133.80 (n/a)</td><td>17.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+3.39%)</td><td>0.02 (+0.38%)</td><td>0.02 (+5.07%)</td><td>0.02 (-8.75%)</td><td>0.00 <b>(+33.11%)</b></td><td>218.10 (+9.60%)</td><td>177.28 (+0.43%)</td><td>170.70 (-4.85%)</td><td>146.00 (-3.31%)</td><td>26.71 <b>(+43.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.00 (n/a)</td><td>176.52 (n/a)</td><td>179.40 (n/a)</td><td>151.00 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+19.06%)</td><td>0.03 (+5.93%)</td><td>0.03 (+9.26%)</td><td>0.02 (-2.30%)</td><td>0.00 <b>(+64.16%)</b></td><td>188.90 (+2.33%)</td><td>161.90 (-4.51%)</td><td>163.30 (-8.46%)</td><td>122.50 (-15.98%)</td><td>24.46 <b>(+34.88%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.60 (n/a)</td><td>169.54 (n/a)</td><td>178.40 (n/a)</td><td>145.80 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(+26.09%)</b></td><td>0.03 (+7.51%)</td><td>0.02 (+0.58%)</td><td>0.02 (+10.08%)</td><td>0.01 <b>(+69.22%)</b></td><td>180.10 (-9.13%)</td><td>163.26 (-5.76%)</td><td>172.50 (-0.58%)</td><td>117.50 <b>(-20.66%)</b></td><td>26.22 (+19.96%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.20 (n/a)</td><td>173.24 (n/a)</td><td>173.50 (n/a)</td><td>148.10 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-10.78%)</td><td>0.02 (-9.65%)</td><td>0.02 (-18.26%)</td><td>0.02 (+2.25%)</td><td>0.00 <b>(-46.47%)</b></td><td>201.10 (-2.19%)</td><td>178.28 (+8.75%)</td><td>178.40 <b>(+22.36%)</b></td><td>153.60 (+12.12%)</td><td>17.78 <b>(-41.61%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>163.94 (n/a)</td><td>145.80 (n/a)</td><td>137.00 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-0.48%)</td><td>0.02 (-11.85%)</td><td>0.02 (-11.83%)</td><td>0.02 (-12.42%)</td><td>0.01 (+10.28%)</td><td>214.00 (+14.19%)</td><td>175.00 (+14.72%)</td><td>185.80 (+13.43%)</td><td>117.80 (+0.51%)</td><td>36.68 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>187.40 (n/a)</td><td>152.54 (n/a)</td><td>163.80 (n/a)</td><td>117.20 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(-28.08%)</b></td><td>0.02 (-18.69%)</td><td>0.02 (-19.55%)</td><td>0.02 (-4.71%)</td><td>0.00 <b>(-73.65%)</b></td><td>188.90 (+4.94%)</td><td>171.10 (+18.70%)</td><td>168.30 <b>(+24.30%)</b></td><td>156.10 <b>(+39.00%)</b></td><td>12.29 <b>(-61.97%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>180.00 (n/a)</td><td>144.14 (n/a)</td><td>135.40 (n/a)</td><td>112.30 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 <b>(-25.02%)</b></td><td>0.02 <b>(-23.23%)</b></td><td>0.02 (-15.99%)</td><td>0.01 <b>(-34.16%)</b></td><td>0.00 (-8.30%)</td><td>304.90 <b>(+51.92%)</b></td><td>224.48 <b>(+31.85%)</b></td><td>203.80 (+19.04%)</td><td>192.50 <b>(+33.40%)</b></td><td>46.24 <b>(+92.67%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.70 (n/a)</td><td>170.26 (n/a)</td><td>171.20 (n/a)</td><td>144.30 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 <b>(-22.74%)</b></td><td>0.02 <b>(-21.47%)</b></td><td>0.02 <b>(-20.37%)</b></td><td>0.02 <b>(-22.96%)</b></td><td>0.00 (-15.54%)</td><td>216.00 <b>(+29.81%)</b></td><td>193.86 <b>(+27.44%)</b></td><td>193.30 <b>(+25.60%)</b></td><td>178.90 <b>(+29.45%)</b></td><td>14.74 <b>(+41.71%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.40 (n/a)</td><td>152.12 (n/a)</td><td>153.90 (n/a)</td><td>138.20 (n/a)</td><td>10.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-18.39%)</td><td>0.02 (-19.47%)</td><td>0.02 (-19.63%)</td><td>0.02 <b>(-22.03%)</b></td><td>0.00 (-17.32%)</td><td>226.10 <b>(+28.25%)</b></td><td>194.84 <b>(+24.26%)</b></td><td>194.20 <b>(+24.41%)</b></td><td>158.80 <b>(+22.53%)</b></td><td>24.30 <b>(+26.61%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.30 (n/a)</td><td>156.80 (n/a)</td><td>156.10 (n/a)</td><td>129.60 (n/a)</td><td>19.19 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(-21.04%)</b></td><td>0.02 <b>(-21.98%)</b></td><td>0.02 (-15.66%)</td><td>0.02 <b>(-24.21%)</b></td><td>0.00 (-17.36%)</td><td>234.10 <b>(+31.96%)</b></td><td>187.94 <b>(+28.64%)</b></td><td>181.10 (+18.60%)</td><td>154.70 <b>(+26.60%)</b></td><td>33.33 <b>(+41.97%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.40 (n/a)</td><td>146.10 (n/a)</td><td>152.70 (n/a)</td><td>122.20 (n/a)</td><td>23.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (+14.59%)</td><td>0.06 (-1.63%)</td><td>0.05 (-2.49%)</td><td>0.05 (-9.68%)</td><td>0.01 <b>(+155.83%)</b></td><td>174.70 (+10.71%)</td><td>149.86 (+3.57%)</td><td>151.00 (+2.51%)</td><td>117.10 (-12.68%)</td><td>24.17 <b>(+152.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>157.80 (n/a)</td><td>144.70 (n/a)</td><td>147.30 (n/a)</td><td>134.10 (n/a)</td><td>9.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (-16.82%)</td><td>0.05 <b>(-21.97%)</b></td><td>0.05 <b>(-23.79%)</b></td><td>0.04 <b>(-34.91%)</b></td><td>0.01 (+13.89%)</td><td>227.00 <b>(+53.69%)</b></td><td>169.46 <b>(+31.92%)</b></td><td>174.20 <b>(+31.17%)</b></td><td>118.20 <b>(+20.24%)</b></td><td>42.11 <b>(+107.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>147.70 (n/a)</td><td>128.46 (n/a)</td><td>132.80 (n/a)</td><td>98.30 (n/a)</td><td>20.28 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (-8.77%)</td><td>0.04 (-4.89%)</td><td>0.04 (+0.22%)</td><td>0.04 (-2.64%)</td><td>0.00 (-11.89%)</td><td>232.60 (+2.69%)</td><td>210.72 (+5.06%)</td><td>200.30 (-0.20%)</td><td>189.30 (+9.61%)</td><td>19.85 (+1.90%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.50 (n/a)</td><td>200.58 (n/a)</td><td>200.70 (n/a)</td><td>172.70 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (+0.71%)</td><td>0.04 (+0.11%)</td><td>0.04 (+4.91%)</td><td>0.04 (+2.68%)</td><td>0.01 (+0.82%)</td><td>213.60 (-2.60%)</td><td>187.84 (-0.11%)</td><td>183.00 (-4.69%)</td><td>163.30 (-0.73%)</td><td>22.06 (-0.15%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>188.04 (n/a)</td><td>192.00 (n/a)</td><td>164.50 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 <b>(-22.21%)</b></td><td>0.05 (-16.79%)</td><td>0.06 (-2.32%)</td><td>0.04 <b>(-27.69%)</b></td><td>0.01 (-5.33%)</td><td>210.30 <b>(+38.26%)</b></td><td>161.32 <b>(+21.46%)</b></td><td>144.80 (+2.40%)</td><td>135.00 <b>(+28.57%)</b></td><td>32.70 <b>(+66.02%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>152.10 (n/a)</td><td>132.82 (n/a)</td><td>141.40 (n/a)</td><td>105.00 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-16.92%)</td><td>0.05 (-12.88%)</td><td>0.05 (-14.75%)</td><td>0.05 (+6.79%)</td><td>0.01 <b>(-47.43%)</b></td><td>181.00 (-6.36%)</td><td>163.58 (+12.29%)</td><td>171.50 (+17.31%)</td><td>136.10 <b>(+20.34%)</b></td><td>17.51 <b>(-42.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>145.68 (n/a)</td><td>146.20 (n/a)</td><td>113.10 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-7.34%)</td><td>0.05 (-2.62%)</td><td>0.06 (+0.16%)</td><td>0.04 (+0.06%)</td><td>0.01 (-18.75%)</td><td>191.30 (-0.05%)</td><td>153.38 (+2.10%)</td><td>147.20 (-0.14%)</td><td>130.50 (+7.94%)</td><td>22.62 (-11.58%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>150.22 (n/a)</td><td>147.40 (n/a)</td><td>120.90 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (+0.36%)</td><td>0.05 (-13.43%)</td><td>0.05 <b>(-20.61%)</b></td><td>0.04 (-7.36%)</td><td>0.01 (+10.91%)</td><td>215.20 (+7.92%)</td><td>178.16 (+16.08%)</td><td>180.10 <b>(+25.94%)</b></td><td>132.40 (-0.38%)</td><td>30.02 (+12.63%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>153.48 (n/a)</td><td>143.00 (n/a)</td><td>132.90 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-7.40%)</td><td>0.04 (-10.61%)</td><td>0.04 (-7.99%)</td><td>0.04 (-13.86%)</td><td>0.01 (-3.16%)</td><td>214.50 (+16.13%)</td><td>186.88 (+12.11%)</td><td>189.10 (+8.68%)</td><td>157.80 (+8.01%)</td><td>23.34 <b>(+22.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>166.70 (n/a)</td><td>174.00 (n/a)</td><td>146.10 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-3.89%)</td><td>0.05 (-10.77%)</td><td>0.05 (-13.76%)</td><td>0.04 <b>(-24.03%)</b></td><td>0.01 <b>(+72.49%)</b></td><td>234.00 <b>(+31.61%)</b></td><td>181.76 (+13.96%)</td><td>179.10 (+16.00%)</td><td>150.40 (+4.01%)</td><td>31.86 <b>(+140.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.80 (n/a)</td><td>159.50 (n/a)</td><td>154.40 (n/a)</td><td>144.60 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-10.89%)</td><td>0.04 (-12.90%)</td><td>0.04 <b>(-24.41%)</b></td><td>0.04 (+3.17%)</td><td>0.01 (-16.06%)</td><td>224.80 (-3.06%)</td><td>190.88 (+13.66%)</td><td>203.40 <b>(+32.25%)</b></td><td>138.00 (+12.20%)</td><td>37.80 (-8.86%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>167.94 (n/a)</td><td>153.80 (n/a)</td><td>123.00 (n/a)</td><td>41.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-9.60%)</td><td>0.05 (-18.54%)</td><td>0.05 (-15.91%)</td><td>0.04 <b>(-25.21%)</b></td><td>0.01 (+17.37%)</td><td>233.60 <b>(+33.64%)</b></td><td>185.72 <b>(+25.66%)</b></td><td>181.80 (+18.98%)</td><td>129.90 (+10.65%)</td><td>42.90 <b>(+77.01%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>147.80 (n/a)</td><td>152.80 (n/a)</td><td>117.40 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 <b>(-21.00%)</b></td><td>0.04 <b>(-26.04%)</b></td><td>0.04 <b>(-21.86%)</b></td><td>0.03 <b>(-41.88%)</b></td><td>0.01 <b>(+57.51%)</b></td><td>318.30 <b>(+72.05%)</b></td><td>238.50 <b>(+39.13%)</b></td><td>224.30 <b>(+27.95%)</b></td><td>185.40 <b>(+26.55%)</b></td><td>51.92 <b>(+255.39%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.00 (n/a)</td><td>171.42 (n/a)</td><td>175.30 (n/a)</td><td>146.50 (n/a)</td><td>14.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 <b>(+39.60%)</b></td><td>0.05 (-1.58%)</td><td>0.04 (-16.35%)</td><td>0.04 (-8.89%)</td><td>0.02 <b>(+143.45%)</b></td><td>233.30 (+9.79%)</td><td>186.90 (+7.36%)</td><td>200.40 (+19.57%)</td><td>108.10 <b>(-28.32%)</b></td><td>47.23 <b>(+81.79%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>174.08 (n/a)</td><td>167.60 (n/a)</td><td>150.80 (n/a)</td><td>25.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-19.67%)</td><td>0.04 (-11.06%)</td><td>0.04 (-5.50%)</td><td>0.04 (-10.28%)</td><td>0.01 <b>(-30.63%)</b></td><td>224.80 (+11.45%)</td><td>191.36 (+10.72%)</td><td>206.70 (+5.78%)</td><td>142.10 <b>(+24.54%)</b></td><td>36.30 (-3.92%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>172.84 (n/a)</td><td>195.40 (n/a)</td><td>114.10 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (+10.03%)</td><td>0.05 (+0.17%)</td><td>0.04 (-14.35%)</td><td>0.04 (-8.85%)</td><td>0.01 <b>(+38.79%)</b></td><td>223.60 (+9.72%)</td><td>173.56 (+2.18%)</td><td>186.30 (+16.73%)</td><td>119.20 (-9.15%)</td><td>42.55 <b>(+30.98%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>169.86 (n/a)</td><td>159.60 (n/a)</td><td>131.20 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 <b>(-21.26%)</b></td><td>0.11 (-12.30%)</td><td>0.10 (-3.57%)</td><td>0.09 (-6.98%)</td><td>0.01 <b>(-47.70%)</b></td><td>179.00 (+7.51%)</td><td>156.76 (+11.22%)</td><td>157.20 (+3.69%)</td><td>126.10 <b>(+26.99%)</b></td><td>20.19 <b>(-30.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>166.50 (n/a)</td><td>140.94 (n/a)</td><td>151.60 (n/a)</td><td>99.30 (n/a)</td><td>29.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+1.06%)</td><td>0.10 (-8.04%)</td><td>0.11 (-2.96%)</td><td>0.07 <b>(-24.05%)</b></td><td>0.02 <b>(+124.18%)</b></td><td>233.60 <b>(+31.68%)</b></td><td>172.50 (+13.44%)</td><td>154.00 (+3.08%)</td><td>133.20 (-1.04%)</td><td>44.60 <b>(+184.23%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>152.06 (n/a)</td><td>149.40 (n/a)</td><td>134.60 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 <b>(+30.20%)</b></td><td>0.09 (+11.71%)</td><td>0.08 (+5.14%)</td><td>0.07 (-3.84%)</td><td>0.02 <b>(+182.52%)</b></td><td>242.40 (+3.99%)</td><td>191.46 (-7.44%)</td><td>199.30 (-4.87%)</td><td>144.80 <b>(-23.18%)</b></td><td>41.81 <b>(+123.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>206.84 (n/a)</td><td>209.50 (n/a)</td><td>188.50 (n/a)</td><td>18.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (+3.67%)</td><td>0.08 (-3.40%)</td><td>0.08 (-5.26%)</td><td>0.07 (-2.10%)</td><td>0.01 (+11.00%)</td><td>236.90 (+2.11%)</td><td>205.24 (+3.67%)</td><td>201.20 (+5.56%)</td><td>178.30 (-3.57%)</td><td>21.28 (+8.79%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>197.98 (n/a)</td><td>190.60 (n/a)</td><td>184.90 (n/a)</td><td>19.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (-0.16%)</td><td>0.10 (+13.19%)</td><td>0.10 (+8.12%)</td><td>0.08 <b>(+48.72%)</b></td><td>0.02 <b>(-31.72%)</b></td><td>209.60 <b>(-32.76%)</b></td><td>160.58 (-16.65%)</td><td>159.10 (-7.50%)</td><td>128.40 (+0.16%)</td><td>30.86 <b>(-55.98%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>311.70 (n/a)</td><td>192.66 (n/a)</td><td>172.00 (n/a)</td><td>128.20 (n/a)</td><td>70.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (+19.69%)</td><td>0.10 (+5.26%)</td><td>0.10 (+2.85%)</td><td>0.09 (+5.54%)</td><td>0.02 <b>(+54.55%)</b></td><td>189.10 (-5.26%)</td><td>164.82 (-3.87%)</td><td>165.20 (-2.77%)</td><td>122.70 (-16.42%)</td><td>27.25 <b>(+23.02%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>171.46 (n/a)</td><td>169.90 (n/a)</td><td>146.80 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (+4.61%)</td><td>0.09 (-5.92%)</td><td>0.09 (-3.32%)</td><td>0.07 <b>(-20.52%)</b></td><td>0.02 <b>(+60.39%)</b></td><td>239.80 <b>(+25.81%)</b></td><td>184.26 (+9.17%)</td><td>175.20 (+3.42%)</td><td>130.80 (-4.46%)</td><td>40.43 <b>(+93.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>168.78 (n/a)</td><td>169.40 (n/a)</td><td>136.90 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 <b>(+23.34%)</b></td><td>0.11 (+8.72%)</td><td>0.10 (+4.14%)</td><td>0.09 (+4.16%)</td><td>0.02 <b>(+100.33%)</b></td><td>172.80 (-4.00%)</td><td>150.10 (-6.92%)</td><td>157.80 (-4.01%)</td><td>117.70 (-18.94%)</td><td>21.23 <b>(+54.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.00 (n/a)</td><td>161.26 (n/a)</td><td>164.40 (n/a)</td><td>145.20 (n/a)</td><td>13.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+4.14%)</td><td>0.10 (+7.54%)</td><td>0.10 (+14.30%)</td><td>0.05 <b>(-23.68%)</b></td><td>0.02 <b>(+59.19%)</b></td><td>306.30 <b>(+31.01%)</b></td><td>184.68 (-1.73%)</td><td>158.70 (-12.51%)</td><td>139.60 (-3.99%)</td><td>68.69 <b>(+113.52%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>187.94 (n/a)</td><td>181.40 (n/a)</td><td>145.40 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+6.27%)</td><td>0.10 (+6.69%)</td><td>0.09 (-2.38%)</td><td>0.09 <b>(+36.43%)</b></td><td>0.01 <b>(-30.30%)</b></td><td>176.20 <b>(-26.71%)</b></td><td>165.38 (-7.94%)</td><td>175.30 (+2.39%)</td><td>138.20 (-5.86%)</td><td>16.44 <b>(-53.80%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.40 (n/a)</td><td>179.64 (n/a)</td><td>171.20 (n/a)</td><td>146.80 (n/a)</td><td>35.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 <b>(-23.87%)</b></td><td>0.10 (+6.44%)</td><td>0.11 (+8.10%)</td><td>0.08 <b>(+45.04%)</b></td><td>0.01 <b>(-66.89%)</b></td><td>193.00 <b>(-31.05%)</b></td><td>159.26 (-13.75%)</td><td>155.00 (-7.46%)</td><td>145.40 <b>(+31.35%)</b></td><td>19.41 <b>(-69.76%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>279.90 (n/a)</td><td>184.64 (n/a)</td><td>167.50 (n/a)</td><td>110.70 (n/a)</td><td>64.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (-3.45%)</td><td>0.11 (+8.48%)</td><td>0.11 (-0.60%)</td><td>0.09 <b>(+33.55%)</b></td><td>0.01 <b>(-42.93%)</b></td><td>172.70 <b>(-25.14%)</b></td><td>147.32 (-11.50%)</td><td>146.60 (+0.62%)</td><td>123.30 (+3.53%)</td><td>19.46 <b>(-56.51%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.70 (n/a)</td><td>166.46 (n/a)</td><td>145.70 (n/a)</td><td>119.10 (n/a)</td><td>44.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 <b>(-23.14%)</b></td><td>0.08 (-5.14%)</td><td>0.09 (+6.18%)</td><td>0.06 (-6.63%)</td><td>0.01 <b>(-34.16%)</b></td><td>284.80 (+7.11%)</td><td>202.22 (+3.53%)</td><td>183.60 (-5.80%)</td><td>174.80 <b>(+30.06%)</b></td><td>46.39 (-4.91%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>265.90 (n/a)</td><td>195.32 (n/a)</td><td>194.90 (n/a)</td><td>134.40 (n/a)</td><td>48.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (-6.85%)</td><td>0.09 (-8.37%)</td><td>0.08 (-15.12%)</td><td>0.08 (-7.04%)</td><td>0.01 <b>(+26.07%)</b></td><td>201.90 (+7.62%)</td><td>185.48 (+9.60%)</td><td>196.60 (+17.87%)</td><td>164.50 (+7.38%)</td><td>19.15 <b>(+43.78%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>169.24 (n/a)</td><td>166.80 (n/a)</td><td>153.20 (n/a)</td><td>13.32 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 <b>(-24.85%)</b></td><td>0.09 (+1.87%)</td><td>0.09 (+10.51%)</td><td>0.09 <b>(+39.86%)</b></td><td>0.01 <b>(-78.56%)</b></td><td>189.70 <b>(-28.50%)</b></td><td>179.10 (-7.68%)</td><td>183.60 (-9.47%)</td><td>164.10 <b>(+33.09%)</b></td><td>11.00 <b>(-79.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>265.30 (n/a)</td><td>194.00 (n/a)</td><td>202.80 (n/a)</td><td>123.30 (n/a)</td><td>52.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 <b>(-26.71%)</b></td><td>0.10 (-10.37%)</td><td>0.10 (+0.23%)</td><td>0.09 (+4.18%)</td><td>0.01 <b>(-78.32%)</b></td><td>178.00 (-3.99%)</td><td>166.54 (+7.22%)</td><td>168.50 (-0.24%)</td><td>156.00 <b>(+36.48%)</b></td><td>9.53 <b>(-72.13%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>185.40 (n/a)</td><td>155.32 (n/a)</td><td>168.90 (n/a)</td><td>114.30 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (+13.85%)</td><td>0.19 (+1.58%)</td><td>0.17 (-6.63%)</td><td>0.15 (+1.69%)</td><td>0.04 <b>(+43.19%)</b></td><td>211.60 (-1.67%)</td><td>178.10 (-0.04%)</td><td>193.80 (+7.07%)</td><td>124.10 (-12.11%)</td><td>34.47 <b>(+21.69%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.20 (n/a)</td><td>178.18 (n/a)</td><td>181.00 (n/a)</td><td>141.20 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (+16.09%)</td><td>0.21 (+4.71%)</td><td>0.19 (-3.66%)</td><td>0.18 (+11.39%)</td><td>0.03 <b>(+38.66%)</b></td><td>185.10 (-10.23%)</td><td>161.88 (-3.91%)</td><td>173.50 (+3.77%)</td><td>126.90 (-13.85%)</td><td>24.34 (+5.89%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>168.46 (n/a)</td><td>167.20 (n/a)</td><td>147.30 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (-9.39%)</td><td>0.15 (-4.37%)</td><td>0.16 (+0.48%)</td><td>0.11 (-17.75%)</td><td>0.02 <b>(+21.15%)</b></td><td>291.20 <b>(+21.59%)</b></td><td>226.76 (+5.47%)</td><td>208.00 (-0.48%)</td><td>206.50 (+10.37%)</td><td>36.57 <b>(+60.15%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>239.50 (n/a)</td><td>215.00 (n/a)</td><td>209.00 (n/a)</td><td>187.10 (n/a)</td><td>22.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (+12.94%)</td><td>0.17 (+8.09%)</td><td>0.16 (+3.52%)</td><td>0.15 (+11.24%)</td><td>0.02 (+9.19%)</td><td>219.30 (-10.09%)</td><td>199.52 (-7.54%)</td><td>210.00 (-3.40%)</td><td>165.80 (-11.48%)</td><td>21.65 (-13.32%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>243.90 (n/a)</td><td>215.80 (n/a)</td><td>217.40 (n/a)</td><td>187.30 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (+6.00%)</td><td>0.20 (-0.62%)</td><td>0.19 (-6.33%)</td><td>0.11 <b>(-30.10%)</b></td><td>0.06 <b>(+68.22%)</b></td><td>290.10 <b>(+43.12%)</b></td><td>179.04 (+7.99%)</td><td>168.20 (+6.73%)</td><td>120.80 (-5.63%)</td><td>68.31 <b>(+119.82%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.70 (n/a)</td><td>165.80 (n/a)</td><td>157.60 (n/a)</td><td>128.00 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (-3.64%)</td><td>0.17 (-7.13%)</td><td>0.16 (-7.99%)</td><td>0.14 (-16.69%)</td><td>0.03 <b>(+52.11%)</b></td><td>231.10 <b>(+20.05%)</b></td><td>193.56 (+9.04%)</td><td>198.70 (+8.64%)</td><td>158.10 (+3.74%)</td><td>30.02 <b>(+89.11%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.50 (n/a)</td><td>177.52 (n/a)</td><td>182.90 (n/a)</td><td>152.40 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (-3.50%)</td><td>0.18 (-11.63%)</td><td>0.17 (-11.37%)</td><td>0.09 <b>(-43.06%)</b></td><td>0.06 <b>(+53.76%)</b></td><td>348.80 <b>(+75.63%)</b></td><td>203.50 <b>(+23.11%)</b></td><td>189.80 (+12.84%)</td><td>132.10 (+3.61%)</td><td>85.69 <b>(+189.05%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>198.60 (n/a)</td><td>165.30 (n/a)</td><td>168.20 (n/a)</td><td>127.50 (n/a)</td><td>29.65 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (+0.38%)</td><td>0.19 (-8.33%)</td><td>0.21 (+9.50%)</td><td>0.09 <b>(-47.52%)</b></td><td>0.07 <b>(+100.16%)</b></td><td>380.50 <b>(+90.54%)</b></td><td>202.40 <b>(+23.99%)</b></td><td>153.60 (-8.68%)</td><td>135.00 (-0.37%)</td><td>103.39 <b>(+291.12%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.70 (n/a)</td><td>163.24 (n/a)</td><td>168.20 (n/a)</td><td>135.50 (n/a)</td><td>26.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 <b>(+22.37%)</b></td><td>0.20 (+16.49%)</td><td>0.18 (+0.24%)</td><td>0.14 <b>(+31.19%)</b></td><td>0.06 <b>(+52.32%)</b></td><td>233.50 <b>(-23.77%)</b></td><td>179.00 (-12.31%)</td><td>182.60 (-0.27%)</td><td>121.50 (-18.29%)</td><td>53.98 (-10.10%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>306.30 (n/a)</td><td>204.12 (n/a)</td><td>183.10 (n/a)</td><td>148.70 (n/a)</td><td>60.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (+5.91%)</td><td>0.20 (+12.14%)</td><td>0.20 (+12.80%)</td><td>0.18 (+17.94%)</td><td>0.02 (-16.07%)</td><td>183.40 (-15.25%)</td><td>163.54 (-11.38%)</td><td>165.60 (-11.35%)</td><td>141.50 (-5.60%)</td><td>16.38 <b>(-32.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.40 (n/a)</td><td>184.54 (n/a)</td><td>186.80 (n/a)</td><td>149.90 (n/a)</td><td>24.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (-17.15%)</td><td>0.20 (+0.48%)</td><td>0.21 (+11.56%)</td><td>0.14 (-13.48%)</td><td>0.04 <b>(-21.08%)</b></td><td>240.40 (+15.63%)</td><td>170.62 (-0.77%)</td><td>159.20 (-10.36%)</td><td>139.80 <b>(+20.73%)</b></td><td>40.79 (+16.89%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>207.90 (n/a)</td><td>171.94 (n/a)</td><td>177.60 (n/a)</td><td>115.80 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (-6.08%)</td><td>0.22 (+5.02%)</td><td>0.21 (+11.49%)</td><td>0.19 <b>(+21.15%)</b></td><td>0.02 <b>(-50.02%)</b></td><td>175.50 (-17.45%)</td><td>152.36 (-7.46%)</td><td>154.10 (-10.30%)</td><td>133.20 (+6.47%)</td><td>15.84 <b>(-55.07%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.60 (n/a)</td><td>164.64 (n/a)</td><td>171.80 (n/a)</td><td>125.10 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (-0.07%)</td><td>0.18 (-0.89%)</td><td>0.19 (-0.29%)</td><td>0.13 (-15.64%)</td><td>0.03 <b>(+52.08%)</b></td><td>248.50 (+18.50%)</td><td>189.00 (+2.22%)</td><td>173.70 (+0.29%)</td><td>169.80 (+0.06%)</td><td>33.50 <b>(+84.01%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.70 (n/a)</td><td>184.90 (n/a)</td><td>173.20 (n/a)</td><td>169.70 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (+3.56%)</td><td>0.17 (-3.11%)</td><td>0.17 (-7.61%)</td><td>0.15 (-7.89%)</td><td>0.02 <b>(+47.10%)</b></td><td>220.30 (+8.58%)</td><td>191.80 (+3.72%)</td><td>195.30 (+8.26%)</td><td>166.40 (-3.42%)</td><td>19.93 <b>(+54.14%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>184.92 (n/a)</td><td>180.40 (n/a)</td><td>172.30 (n/a)</td><td>12.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (-0.26%)</td><td>0.18 (+2.33%)</td><td>0.18 (-3.26%)</td><td>0.14 <b>(+27.72%)</b></td><td>0.03 <b>(-31.51%)</b></td><td>241.50 <b>(-21.72%)</b></td><td>187.56 (-5.75%)</td><td>178.60 (+3.36%)</td><td>162.00 (+0.25%)</td><td>32.16 <b>(-47.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>308.50 (n/a)</td><td>199.00 (n/a)</td><td>172.80 (n/a)</td><td>161.60 (n/a)</td><td>61.66 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (-19.51%)</td><td>0.16 (-13.41%)</td><td>0.16 (-16.31%)</td><td>0.15 (-2.51%)</td><td>0.01 <b>(-51.32%)</b></td><td>222.60 (+2.53%)</td><td>200.52 (+14.11%)</td><td>203.60 (+19.48%)</td><td>183.50 <b>(+24.24%)</b></td><td>16.01 <b>(-39.47%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.10 (n/a)</td><td>175.72 (n/a)</td><td>170.40 (n/a)</td><td>147.70 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (-1.07%)</td><td>0.21 (-0.25%)</td><td>0.21 (-0.05%)</td><td>0.21 (+0.03%)</td><td>0.00 <b>(-86.99%)</b></td><td>40889.40 (-0.03%)</td><td>40856.46 (+0.25%)</td><td>40854.20 (+0.05%)</td><td>40823.70 (+1.09%)</td><td>27.83 <b>(-86.84%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40901.20 (n/a)</td><td>40755.80 (n/a)</td><td>40833.70 (n/a)</td><td>40384.90 (n/a)</td><td>211.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (-0.90%)</td><td>0.21 (-0.26%)</td><td>0.21 (-0.05%)</td><td>0.21 (-0.03%)</td><td>0.00 <b>(-78.25%)</b></td><td>40913.30 (+0.03%)</td><td>40859.42 (+0.26%)</td><td>40841.30 (+0.05%)</td><td>40818.00 (+0.91%)</td><td>40.53 <b>(-78.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40899.70 (n/a)</td><td>40755.16 (n/a)</td><td>40822.60 (n/a)</td><td>40449.80 (n/a)</td><td>184.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (+0.01%)</td><td>0.13 (-0.01%)</td><td>0.13 (-0.03%)</td><td>0.13 (-0.00%)</td><td>0.00 (+0.50%)</td><td>321838.30 (+0.00%)</td><td>321759.50 (+0.01%)</td><td>321784.00 (+0.03%)</td><td>321614.20 (-0.01%)</td><td>84.93 (+0.50%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321831.30 (n/a)</td><td>321726.62 (n/a)</td><td>321695.90 (n/a)</td><td>321631.00 (n/a)</td><td>84.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-2.44%)</td><td>0.03 (+10.24%)</td><td>0.02 (+9.70%)</td><td>0.02 <b>(+23.31%)</b></td><td>0.00 <b>(-29.86%)</b></td><td>170.80 (-18.90%)</td><td>154.78 (-11.18%)</td><td>167.90 (-8.80%)</td><td>127.10 (+2.50%)</td><td>20.92 <b>(-40.24%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>174.26 (n/a)</td><td>184.10 (n/a)</td><td>124.00 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-13.40%)</td><td>0.04 (-9.65%)</td><td>0.04 (-5.53%)</td><td>0.03 (-10.87%)</td><td>0.01 <b>(-25.26%)</b></td><td>213.10 (+12.22%)</td><td>171.16 (+9.69%)</td><td>175.10 (+5.86%)</td><td>135.70 (+15.49%)</td><td>29.77 (-3.03%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>156.04 (n/a)</td><td>165.40 (n/a)</td><td>117.50 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+15.88%)</td><td>0.02 (+18.10%)</td><td>0.02 (+8.31%)</td><td>0.02 <b>(+48.67%)</b></td><td>0.00 (-11.10%)</td><td>193.80 <b>(-32.76%)</b></td><td>171.94 (-17.47%)</td><td>174.80 (-7.71%)</td><td>129.00 (-13.65%)</td><td>26.30 <b>(-49.70%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>288.20 (n/a)</td><td>208.34 (n/a)</td><td>189.40 (n/a)</td><td>149.40 (n/a)</td><td>52.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(-20.81%)</b></td><td>0.03 (-19.70%)</td><td>0.03 (-14.58%)</td><td>0.02 <b>(-29.95%)</b></td><td>0.00 (+6.62%)</td><td>236.90 <b>(+42.80%)</b></td><td>185.20 <b>(+25.90%)</b></td><td>172.50 (+17.03%)</td><td>156.00 <b>(+26.21%)</b></td><td>32.10 <b>(+95.90%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>165.90 (n/a)</td><td>147.10 (n/a)</td><td>147.40 (n/a)</td><td>123.60 (n/a)</td><td>16.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+2.23%)</td><td>0.03 (+11.79%)</td><td>0.03 (+8.61%)</td><td>0.01 (-2.87%)</td><td>0.01 <b>(+21.36%)</b></td><td>291.00 (+2.97%)</td><td>173.60 (-8.01%)</td><td>158.90 (-7.94%)</td><td>128.00 (-2.14%)</td><td>67.52 (+19.60%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>282.60 (n/a)</td><td>188.72 (n/a)</td><td>172.60 (n/a)</td><td>130.80 (n/a)</td><td>56.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (-10.80%)</td><td>0.03 (-15.77%)</td><td>0.03 (-14.37%)</td><td>0.03 (-15.16%)</td><td>0.00 (-10.87%)</td><td>199.90 (+17.87%)</td><td>174.60 (+18.79%)</td><td>173.70 (+16.81%)</td><td>141.10 (+12.16%)</td><td>21.82 (+16.60%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>169.60 (n/a)</td><td>146.98 (n/a)</td><td>148.70 (n/a)</td><td>125.80 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+13.77%)</td><td>0.02 (+18.42%)</td><td>0.03 <b>(+23.05%)</b></td><td>0.02 <b>(+21.05%)</b></td><td>0.00 (+11.78%)</td><td>181.10 (-17.38%)</td><td>165.36 (-15.60%)</td><td>158.70 (-18.74%)</td><td>151.40 (-12.13%)</td><td>14.16 (-17.33%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.20 (n/a)</td><td>195.92 (n/a)</td><td>195.30 (n/a)</td><td>172.30 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-19.00%)</td><td>0.02 <b>(-28.70%)</b></td><td>0.02 <b>(-29.78%)</b></td><td>0.02 <b>(-41.79%)</b></td><td>0.00 <b>(+74.69%)</b></td><td>259.20 <b>(+71.77%)</b></td><td>194.26 <b>(+43.62%)</b></td><td>185.30 <b>(+42.43%)</b></td><td>156.40 <b>(+23.44%)</b></td><td>38.81 <b>(+283.82%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>150.90 (n/a)</td><td>135.26 (n/a)</td><td>130.10 (n/a)</td><td>126.70 (n/a)</td><td>10.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (+1.50%)</td><td>0.02 (+10.05%)</td><td>0.03 (+14.34%)</td><td>0.02 (+9.55%)</td><td>0.00 (-2.17%)</td><td>192.10 (-8.70%)</td><td>167.04 (-9.27%)</td><td>163.60 (-12.56%)</td><td>147.20 (-1.47%)</td><td>19.73 (-10.26%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.40 (n/a)</td><td>184.10 (n/a)</td><td>187.10 (n/a)</td><td>149.40 (n/a)</td><td>21.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-18.50%)</td><td>0.03 (-14.75%)</td><td>0.03 (-15.13%)</td><td>0.02 (-8.63%)</td><td>0.00 <b>(-31.24%)</b></td><td>219.50 (+9.42%)</td><td>184.12 (+16.21%)</td><td>174.40 (+17.84%)</td><td>152.80 <b>(+22.73%)</b></td><td>26.91 (-7.65%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>158.44 (n/a)</td><td>148.00 (n/a)</td><td>124.50 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 <b>(+26.90%)</b></td><td>0.02 (+7.54%)</td><td>0.02 (+2.35%)</td><td>0.02 (+2.39%)</td><td>0.01 <b>(+112.74%)</b></td><td>205.70 (-2.33%)</td><td>179.08 (-4.64%)</td><td>184.60 (-2.33%)</td><td>122.30 <b>(-21.20%)</b></td><td>33.49 <b>(+62.68%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>187.80 (n/a)</td><td>189.00 (n/a)</td><td>155.20 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (-8.77%)</td><td>0.02 <b>(-22.44%)</b></td><td>0.02 (-18.00%)</td><td>0.01 <b>(-36.63%)</b></td><td>0.00 <b>(+46.50%)</b></td><td>332.40 <b>(+57.83%)</b></td><td>254.88 <b>(+34.59%)</b></td><td>249.10 <b>(+21.93%)</b></td><td>175.10 (+9.64%)</td><td>67.51 <b>(+158.33%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>189.38 (n/a)</td><td>204.30 (n/a)</td><td>159.70 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (-1.87%)</td><td>0.02 (-0.18%)</td><td>0.02 (-5.70%)</td><td>0.02 <b>(+32.00%)</b></td><td>0.00 <b>(-43.05%)</b></td><td>206.90 <b>(-24.24%)</b></td><td>184.04 (-3.00%)</td><td>181.20 (+6.09%)</td><td>157.30 (+1.88%)</td><td>21.64 <b>(-55.80%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>273.10 (n/a)</td><td>189.74 (n/a)</td><td>170.80 (n/a)</td><td>154.40 (n/a)</td><td>48.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (-18.54%)</td><td>0.02 (-17.66%)</td><td>0.02 (-12.78%)</td><td>0.01 <b>(-27.15%)</b></td><td>0.00 (+12.39%)</td><td>314.10 <b>(+37.28%)</b></td><td>221.68 <b>(+24.48%)</b></td><td>186.20 (+14.66%)</td><td>179.80 <b>(+22.73%)</b></td><td>58.96 <b>(+81.48%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.80 (n/a)</td><td>178.08 (n/a)</td><td>162.40 (n/a)</td><td>146.50 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (-4.21%)</td><td>0.02 (-2.87%)</td><td>0.02 (-11.07%)</td><td>0.02 (-8.70%)</td><td>0.00 (-3.14%)</td><td>263.40 (+9.52%)</td><td>207.46 (+3.00%)</td><td>208.50 (+12.46%)</td><td>173.40 (+4.39%)</td><td>36.72 (+5.42%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.50 (n/a)</td><td>201.42 (n/a)</td><td>185.40 (n/a)</td><td>166.10 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-10.02%)</td><td>0.05 (-10.38%)</td><td>0.05 (-0.74%)</td><td>0.04 <b>(-22.86%)</b></td><td>0.01 <b>(+24.01%)</b></td><td>226.70 <b>(+29.62%)</b></td><td>176.62 (+13.57%)</td><td>163.50 (+0.74%)</td><td>138.90 (+11.12%)</td><td>36.18 <b>(+81.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.90 (n/a)</td><td>155.52 (n/a)</td><td>162.30 (n/a)</td><td>125.00 (n/a)</td><td>19.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (+2.51%)</td><td>0.08 (-0.54%)</td><td>0.08 (+8.08%)</td><td>0.07 (+8.55%)</td><td>0.02 (-14.13%)</td><td>184.80 (-7.88%)</td><td>157.60 (-0.63%)</td><td>155.70 (-7.49%)</td><td>117.80 (-2.40%)</td><td>27.45 (-19.49%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>200.60 (n/a)</td><td>158.60 (n/a)</td><td>168.30 (n/a)</td><td>120.70 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (+6.65%)</td><td>0.05 (-5.73%)</td><td>0.04 (-8.93%)</td><td>0.03 (-19.48%)</td><td>0.01 <b>(+46.95%)</b></td><td>236.70 <b>(+24.19%)</b></td><td>182.06 (+9.28%)</td><td>196.40 (+9.84%)</td><td>122.40 (-6.21%)</td><td>43.71 <b>(+66.36%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>166.60 (n/a)</td><td>178.80 (n/a)</td><td>130.50 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (-9.31%)</td><td>0.06 (-13.15%)</td><td>0.06 (-14.18%)</td><td>0.05 (-15.28%)</td><td>0.01 (+14.69%)</td><td>213.40 (+18.03%)</td><td>182.42 (+15.94%)</td><td>183.20 (+16.54%)</td><td>149.20 (+10.27%)</td><td>25.79 <b>(+49.40%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>157.34 (n/a)</td><td>157.20 (n/a)</td><td>135.30 (n/a)</td><td>17.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-12.79%)</td><td>0.04 (-19.80%)</td><td>0.04 (-14.08%)</td><td>0.03 (-18.94%)</td><td>0.01 (-17.70%)</td><td>236.30 <b>(+23.33%)</b></td><td>202.34 <b>(+24.64%)</b></td><td>206.40 (+16.41%)</td><td>147.10 (+14.65%)</td><td>37.57 <b>(+21.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>162.34 (n/a)</td><td>177.30 (n/a)</td><td>128.30 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 <b>(-20.67%)</b></td><td>0.06 (-18.48%)</td><td>0.06 (-15.49%)</td><td>0.05 (-16.16%)</td><td>0.01 <b>(-31.46%)</b></td><td>217.20 (+19.28%)</td><td>186.86 <b>(+21.99%)</b></td><td>184.40 (+18.28%)</td><td>161.80 <b>(+26.01%)</b></td><td>24.60 (+4.52%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>153.18 (n/a)</td><td>155.90 (n/a)</td><td>128.40 (n/a)</td><td>23.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (-9.27%)</td><td>0.05 (+0.53%)</td><td>0.05 (+0.62%)</td><td>0.04 <b>(+61.79%)</b></td><td>0.01 <b>(-52.90%)</b></td><td>217.90 <b>(-38.20%)</b></td><td>180.96 (-9.36%)</td><td>174.90 (-0.62%)</td><td>148.40 (+10.17%)</td><td>26.05 <b>(-70.16%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>352.60 (n/a)</td><td>199.64 (n/a)</td><td>176.00 (n/a)</td><td>134.70 (n/a)</td><td>87.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 <b>(-21.67%)</b></td><td>0.05 (-19.38%)</td><td>0.05 (-15.89%)</td><td>0.04 <b>(-25.06%)</b></td><td>0.01 (-10.96%)</td><td>244.50 <b>(+33.46%)</b></td><td>194.16 <b>(+24.99%)</b></td><td>183.50 (+18.92%)</td><td>154.00 <b>(+27.69%)</b></td><td>36.59 <b>(+54.91%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>155.34 (n/a)</td><td>154.30 (n/a)</td><td>120.60 (n/a)</td><td>23.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-16.74%)</td><td>0.04 (-16.75%)</td><td>0.04 <b>(-23.67%)</b></td><td>0.04 (-13.72%)</td><td>0.01 <b>(-29.91%)</b></td><td>211.60 (+15.88%)</td><td>187.08 (+19.28%)</td><td>193.70 <b>(+31.06%)</b></td><td>150.40 <b>(+20.13%)</b></td><td>22.75 (-7.95%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>156.84 (n/a)</td><td>147.80 (n/a)</td><td>125.20 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 <b>(-20.12%)</b></td><td>0.05 (-16.29%)</td><td>0.05 <b>(-23.38%)</b></td><td>0.04 (-12.14%)</td><td>0.01 <b>(-37.90%)</b></td><td>221.70 (+13.81%)</td><td>185.50 (+17.61%)</td><td>193.00 <b>(+30.49%)</b></td><td>152.70 <b>(+25.16%)</b></td><td>27.41 (-15.03%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>157.72 (n/a)</td><td>147.90 (n/a)</td><td>122.00 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (+12.55%)</td><td>0.05 (+0.48%)</td><td>0.04 (-14.95%)</td><td>0.04 (+0.99%)</td><td>0.01 (+9.89%)</td><td>202.90 (-0.98%)</td><td>175.28 (-0.40%)</td><td>185.10 (+17.60%)</td><td>139.50 (-11.15%)</td><td>24.70 (-4.29%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>175.98 (n/a)</td><td>157.40 (n/a)</td><td>157.00 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 <b>(-25.76%)</b></td><td>0.04 <b>(-21.97%)</b></td><td>0.04 <b>(-20.70%)</b></td><td>0.03 (-16.26%)</td><td>0.01 <b>(-33.44%)</b></td><td>325.90 (+19.42%)</td><td>242.18 <b>(+26.64%)</b></td><td>220.70 <b>(+26.11%)</b></td><td>204.90 <b>(+34.71%)</b></td><td>49.42 (+4.11%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.90 (n/a)</td><td>191.24 (n/a)</td><td>175.00 (n/a)</td><td>152.10 (n/a)</td><td>47.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-4.72%)</td><td>0.04 (-17.47%)</td><td>0.04 <b>(-21.46%)</b></td><td>0.03 (-15.63%)</td><td>0.01 (+1.30%)</td><td>278.40 (+18.52%)</td><td>215.54 <b>(+22.23%)</b></td><td>205.60 <b>(+27.31%)</b></td><td>154.20 (+4.90%)</td><td>47.68 <b>(+28.09%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>176.34 (n/a)</td><td>161.50 (n/a)</td><td>147.00 (n/a)</td><td>37.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (-7.78%)</td><td>0.04 (-12.75%)</td><td>0.05 (-19.93%)</td><td>0.03 <b>(-21.09%)</b></td><td>0.01 (-14.26%)</td><td>294.40 <b>(+26.73%)</b></td><td>206.88 (+14.90%)</td><td>190.00 <b>(+24.92%)</b></td><td>162.20 (+8.42%)</td><td>51.00 <b>(+26.27%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>180.06 (n/a)</td><td>152.10 (n/a)</td><td>149.60 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 <b>(-22.16%)</b></td><td>0.04 (-15.07%)</td><td>0.04 <b>(-21.38%)</b></td><td>0.03 (-2.86%)</td><td>0.00 <b>(-48.05%)</b></td><td>235.80 (+2.92%)</td><td>214.46 (+15.99%)</td><td>225.70 <b>(+27.15%)</b></td><td>188.80 <b>(+28.44%)</b></td><td>21.46 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>184.90 (n/a)</td><td>177.50 (n/a)</td><td>147.00 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+3.74%)</td><td>0.09 (-5.52%)</td><td>0.09 (-1.14%)</td><td>0.07 <b>(-20.16%)</b></td><td>0.02 <b>(+23.81%)</b></td><td>245.80 <b>(+25.28%)</b></td><td>184.14 (+8.14%)</td><td>192.10 (+1.16%)</td><td>131.70 (-3.59%)</td><td>44.77 <b>(+49.07%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.20 (n/a)</td><td>170.28 (n/a)</td><td>189.90 (n/a)</td><td>136.60 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (-15.18%)</td><td>0.13 (-14.49%)</td><td>0.14 <b>(-22.76%)</b></td><td>0.10 (+16.03%)</td><td>0.03 <b>(-39.04%)</b></td><td>256.20 (-13.82%)</td><td>195.70 (+9.71%)</td><td>178.10 <b>(+29.43%)</b></td><td>148.50 (+17.95%)</td><td>46.81 <b>(-35.97%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>297.30 (n/a)</td><td>178.38 (n/a)</td><td>137.60 (n/a)</td><td>125.90 (n/a)</td><td>73.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (-19.49%)</td><td>0.08 <b>(-25.33%)</b></td><td>0.08 <b>(-20.03%)</b></td><td>0.05 <b>(-38.11%)</b></td><td>0.02 (+8.41%)</td><td>314.10 <b>(+61.57%)</b></td><td>218.24 <b>(+39.43%)</b></td><td>200.30 <b>(+25.11%)</b></td><td>142.00 <b>(+24.23%)</b></td><td>64.90 <b>(+125.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.40 (n/a)</td><td>156.52 (n/a)</td><td>160.10 (n/a)</td><td>114.30 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (-18.26%)</td><td>0.11 (-6.03%)</td><td>0.11 (-10.48%)</td><td>0.09 <b>(+32.29%)</b></td><td>0.01 <b>(-57.24%)</b></td><td>220.80 <b>(-24.41%)</b></td><td>190.04 (+0.52%)</td><td>193.20 (+11.68%)</td><td>159.20 <b>(+22.27%)</b></td><td>22.58 <b>(-62.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>292.10 (n/a)</td><td>189.06 (n/a)</td><td>173.00 (n/a)</td><td>130.20 (n/a)</td><td>60.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (-19.75%)</td><td>0.09 (-15.56%)</td><td>0.09 <b>(-22.99%)</b></td><td>0.07 (+11.57%)</td><td>0.02 <b>(-43.45%)</b></td><td>230.50 (-10.38%)</td><td>182.60 (+12.08%)</td><td>190.60 <b>(+29.84%)</b></td><td>137.20 <b>(+24.61%)</b></td><td>35.55 <b>(-38.77%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>257.20 (n/a)</td><td>162.92 (n/a)</td><td>146.80 (n/a)</td><td>110.10 (n/a)</td><td>58.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 <b>(-26.10%)</b></td><td>0.10 (-15.71%)</td><td>0.10 (-12.44%)</td><td>0.09 (-4.80%)</td><td>0.01 <b>(-57.02%)</b></td><td>221.90 (+5.07%)</td><td>202.38 (+16.28%)</td><td>205.40 (+14.24%)</td><td>174.30 <b>(+35.33%)</b></td><td>19.30 <b>(-37.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.20 (n/a)</td><td>174.04 (n/a)</td><td>179.80 (n/a)</td><td>128.80 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (+13.66%)</td><td>0.10 (+8.04%)</td><td>0.09 (+1.28%)</td><td>0.09 <b>(+33.84%)</b></td><td>0.02 (-12.44%)</td><td>181.90 <b>(-25.27%)</b></td><td>165.28 (-8.90%)</td><td>176.20 (-1.29%)</td><td>128.70 (-11.97%)</td><td>21.65 <b>(-43.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.40 (n/a)</td><td>181.42 (n/a)</td><td>178.50 (n/a)</td><td>146.20 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 <b>(-27.27%)</b></td><td>0.09 <b>(-25.08%)</b></td><td>0.09 <b>(-28.55%)</b></td><td>0.06 (+0.38%)</td><td>0.02 <b>(-44.23%)</b></td><td>325.80 (-0.40%)</td><td>215.70 <b>(+23.79%)</b></td><td>203.90 <b>(+39.95%)</b></td><td>163.40 <b>(+37.54%)</b></td><td>64.43 <b>(-25.56%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>327.10 (n/a)</td><td>174.24 (n/a)</td><td>145.70 (n/a)</td><td>118.80 (n/a)</td><td>86.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (-4.42%)</td><td>0.10 (-1.61%)</td><td>0.10 (-9.46%)</td><td>0.09 <b>(+29.90%)</b></td><td>0.02 <b>(-33.54%)</b></td><td>191.80 <b>(-23.03%)</b></td><td>164.54 (-2.70%)</td><td>161.70 (+10.45%)</td><td>123.10 (+4.68%)</td><td>26.92 <b>(-48.16%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>249.20 (n/a)</td><td>169.10 (n/a)</td><td>146.40 (n/a)</td><td>117.60 (n/a)</td><td>51.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (-11.60%)</td><td>0.09 <b>(-22.32%)</b></td><td>0.10 <b>(-20.41%)</b></td><td>0.06 <b>(-43.91%)</b></td><td>0.02 <b>(+90.43%)</b></td><td>316.60 <b>(+78.27%)</b></td><td>211.20 <b>(+34.99%)</b></td><td>191.20 <b>(+25.71%)</b></td><td>156.80 (+13.13%)</td><td>61.50 <b>(+303.35%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>177.60 (n/a)</td><td>156.46 (n/a)</td><td>152.10 (n/a)</td><td>138.60 (n/a)</td><td>15.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (-18.12%)</td><td>0.09 (-7.62%)</td><td>0.09 (-3.87%)</td><td>0.07 (+9.30%)</td><td>0.01 <b>(-52.56%)</b></td><td>219.10 (-8.52%)</td><td>180.52 (+4.54%)</td><td>175.60 (+4.03%)</td><td>160.20 <b>(+22.10%)</b></td><td>23.58 <b>(-45.92%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.50 (n/a)</td><td>172.68 (n/a)</td><td>168.80 (n/a)</td><td>131.20 (n/a)</td><td>43.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (-10.68%)</td><td>0.08 (-18.47%)</td><td>0.08 <b>(-23.19%)</b></td><td>0.07 (-15.58%)</td><td>0.01 (-5.89%)</td><td>247.30 (+18.44%)</td><td>215.04 <b>(+22.92%)</b></td><td>211.80 <b>(+30.18%)</b></td><td>170.20 (+11.90%)</td><td>29.83 <b>(+23.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>174.94 (n/a)</td><td>162.70 (n/a)</td><td>152.10 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (-13.05%)</td><td>0.09 (-9.11%)</td><td>0.08 (-8.52%)</td><td>0.06 (-19.79%)</td><td>0.02 (-6.86%)</td><td>257.40 <b>(+24.71%)</b></td><td>192.10 (+10.71%)</td><td>194.30 (+9.28%)</td><td>152.40 (+15.02%)</td><td>41.12 <b>(+33.13%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.40 (n/a)</td><td>173.52 (n/a)</td><td>177.80 (n/a)</td><td>132.50 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (-18.42%)</td><td>0.08 (-2.46%)</td><td>0.08 (-2.21%)</td><td>0.07 <b>(+42.31%)</b></td><td>0.01 <b>(-63.62%)</b></td><td>250.60 <b>(-29.73%)</b></td><td>215.02 (-4.16%)</td><td>205.60 (+2.24%)</td><td>191.40 <b>(+22.61%)</b></td><td>23.17 <b>(-70.12%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>356.60 (n/a)</td><td>224.36 (n/a)</td><td>201.10 (n/a)</td><td>156.10 (n/a)</td><td>77.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (-14.92%)</td><td>0.07 (-8.86%)</td><td>0.08 (-6.63%)</td><td>0.05 (+3.46%)</td><td>0.02 <b>(-29.42%)</b></td><td>326.50 (-3.35%)</td><td>229.58 (+6.32%)</td><td>207.80 (+7.11%)</td><td>179.10 (+17.52%)</td><td>58.16 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>337.80 (n/a)</td><td>215.94 (n/a)</td><td>194.00 (n/a)</td><td>152.40 (n/a)</td><td>72.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (-9.17%)</td><td>0.20 (-6.15%)</td><td>0.21 (-4.12%)</td><td>0.15 (+1.72%)</td><td>0.04 <b>(-26.44%)</b></td><td>221.20 (-1.69%)</td><td>168.26 (+4.59%)</td><td>157.30 (+4.31%)</td><td>138.50 (+10.10%)</td><td>33.86 (-18.43%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.00 (n/a)</td><td>160.88 (n/a)</td><td>150.80 (n/a)</td><td>125.80 (n/a)</td><td>41.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (-13.92%)</td><td>0.19 <b>(-23.73%)</b></td><td>0.19 <b>(-23.84%)</b></td><td>0.15 <b>(-30.50%)</b></td><td>0.04 (+11.25%)</td><td>224.80 <b>(+43.92%)</b></td><td>179.58 <b>(+33.22%)</b></td><td>175.10 <b>(+31.36%)</b></td><td>134.30 (+16.18%)</td><td>34.64 <b>(+86.69%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>156.20 (n/a)</td><td>134.80 (n/a)</td><td>133.30 (n/a)</td><td>115.60 (n/a)</td><td>18.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (-14.61%)</td><td>0.22 (-4.54%)</td><td>0.22 (-4.64%)</td><td>0.20 (+17.12%)</td><td>0.01 <b>(-63.88%)</b></td><td>207.10 (-14.63%)</td><td>189.52 (+2.49%)</td><td>182.40 (+4.89%)</td><td>178.70 (+17.10%)</td><td>12.30 <b>(-64.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>242.60 (n/a)</td><td>184.92 (n/a)</td><td>173.90 (n/a)</td><td>152.60 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (+15.35%)</td><td>0.19 (+0.78%)</td><td>0.18 (-5.61%)</td><td>0.09 <b>(-27.86%)</b></td><td>0.08 <b>(+74.25%)</b></td><td>382.60 <b>(+38.62%)</b></td><td>206.22 (+11.28%)</td><td>180.30 (+5.93%)</td><td>125.00 (-13.31%)</td><td>105.99 <b>(+98.55%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>276.00 (n/a)</td><td>185.32 (n/a)</td><td>170.20 (n/a)</td><td>144.20 (n/a)</td><td>53.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (-12.74%)</td><td>0.22 (-8.55%)</td><td>0.21 (-2.42%)</td><td>0.18 (-7.78%)</td><td>0.03 <b>(-30.98%)</b></td><td>225.30 (+8.42%)</td><td>192.26 (+8.41%)</td><td>195.70 (+2.46%)</td><td>166.10 (+14.55%)</td><td>24.12 (-13.57%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>207.80 (n/a)</td><td>177.34 (n/a)</td><td>191.00 (n/a)</td><td>145.00 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (-16.97%)</td><td>0.17 (-17.80%)</td><td>0.16 <b>(-27.54%)</b></td><td>0.13 (-17.37%)</td><td>0.03 <b>(-22.77%)</b></td><td>247.80 <b>(+21.00%)</b></td><td>198.38 <b>(+21.05%)</b></td><td>205.70 <b>(+37.96%)</b></td><td>157.00 <b>(+20.49%)</b></td><td>35.94 (+8.74%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.80 (n/a)</td><td>163.88 (n/a)</td><td>149.10 (n/a)</td><td>130.30 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.30 <b>(+31.70%)</b></td><td>0.22 (+2.63%)</td><td>0.20 (-8.16%)</td><td>0.19 (-2.82%)</td><td>0.05 <b>(+224.64%)</b></td><td>197.90 (+2.86%)</td><td>175.62 (+0.01%)</td><td>187.60 (+8.88%)</td><td>123.20 <b>(-24.09%)</b></td><td>30.04 <b>(+144.99%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>175.60 (n/a)</td><td>172.30 (n/a)</td><td>162.30 (n/a)</td><td>12.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (+15.89%)</td><td>0.18 (-13.74%)</td><td>0.17 <b>(-23.82%)</b></td><td>0.13 <b>(-23.94%)</b></td><td>0.05 <b>(+131.14%)</b></td><td>243.90 <b>(+31.48%)</b></td><td>190.46 <b>(+20.90%)</b></td><td>195.20 <b>(+31.27%)</b></td><td>124.30 (-13.74%)</td><td>44.22 <b>(+153.35%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.50 (n/a)</td><td>157.54 (n/a)</td><td>148.70 (n/a)</td><td>144.10 (n/a)</td><td>17.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 <b>(-31.04%)</b></td><td>0.21 (-13.42%)</td><td>0.20 (-16.87%)</td><td>0.18 <b>(+23.40%)</b></td><td>0.03 <b>(-63.28%)</b></td><td>204.40 (-18.99%)</td><td>176.00 (+6.99%)</td><td>180.10 <b>(+20.31%)</b></td><td>146.90 <b>(+45.01%)</b></td><td>24.18 <b>(-57.74%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>252.30 (n/a)</td><td>164.50 (n/a)</td><td>149.70 (n/a)</td><td>101.30 (n/a)</td><td>57.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.22 (+4.80%)</td><td>0.18 (-6.02%)</td><td>0.16 (-16.68%)</td><td>0.15 (-11.54%)</td><td>0.03 <b>(+164.70%)</b></td><td>212.30 (+13.05%)</td><td>185.26 (+8.59%)</td><td>200.10 <b>(+20.04%)</b></td><td>151.40 (-4.60%)</td><td>30.85 <b>(+179.49%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>170.60 (n/a)</td><td>166.70 (n/a)</td><td>158.70 (n/a)</td><td>11.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (-12.02%)</td><td>0.19 (-6.30%)</td><td>0.19 (-5.64%)</td><td>0.16 (-12.44%)</td><td>0.02 (-10.67%)</td><td>214.70 (+14.20%)</td><td>186.00 (+6.76%)</td><td>181.80 (+6.01%)</td><td>175.30 (+13.68%)</td><td>16.37 (+15.46%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>188.00 (n/a)</td><td>174.22 (n/a)</td><td>171.50 (n/a)</td><td>154.20 (n/a)</td><td>14.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 <b>(-25.48%)</b></td><td>0.16 <b>(-25.21%)</b></td><td>0.16 <b>(-22.93%)</b></td><td>0.10 <b>(-44.90%)</b></td><td>0.05 <b>(+24.82%)</b></td><td>330.40 <b>(+81.44%)</b></td><td>217.94 <b>(+41.26%)</b></td><td>203.20 <b>(+29.76%)</b></td><td>157.80 <b>(+34.18%)</b></td><td>71.46 <b>(+202.71%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>182.10 (n/a)</td><td>154.28 (n/a)</td><td>156.60 (n/a)</td><td>117.60 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (+0.86%)</td><td>0.17 (-1.69%)</td><td>0.17 (-2.70%)</td><td>0.16 (+2.21%)</td><td>0.02 (+4.20%)</td><td>220.40 (-2.17%)</td><td>201.78 (+1.73%)</td><td>203.60 (+2.78%)</td><td>174.60 (-0.85%)</td><td>17.66 (-0.28%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.30 (n/a)</td><td>198.34 (n/a)</td><td>198.10 (n/a)</td><td>176.10 (n/a)</td><td>17.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 <b>(-20.83%)</b></td><td>0.15 (-18.83%)</td><td>0.15 (-18.92%)</td><td>0.09 <b>(-25.08%)</b></td><td>0.04 <b>(-23.68%)</b></td><td>353.80 <b>(+33.46%)</b></td><td>238.12 <b>(+23.21%)</b></td><td>213.00 <b>(+23.34%)</b></td><td>173.60 <b>(+26.35%)</b></td><td>68.79 <b>(+32.26%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>265.10 (n/a)</td><td>193.26 (n/a)</td><td>172.70 (n/a)</td><td>137.40 (n/a)</td><td>52.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (+1.54%)</td><td>0.13 (-9.41%)</td><td>0.12 (-17.09%)</td><td>0.10 (-6.70%)</td><td>0.02 (+19.90%)</td><td>198.10 (+7.20%)</td><td>164.94 (+11.19%)</td><td>169.80 <b>(+20.60%)</b></td><td>123.50 (-1.52%)</td><td>27.05 <b>(+20.25%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>184.80 (n/a)</td><td>148.34 (n/a)</td><td>140.80 (n/a)</td><td>125.40 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (-18.67%)</td><td>0.11 (-15.65%)</td><td>0.11 (-13.33%)</td><td>0.10 <b>(-20.94%)</b></td><td>0.01 (-18.84%)</td><td>207.00 <b>(+26.53%)</b></td><td>180.62 (+18.59%)</td><td>183.20 (+15.37%)</td><td>150.00 <b>(+22.95%)</b></td><td>21.84 <b>(+27.72%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>163.60 (n/a)</td><td>152.30 (n/a)</td><td>158.80 (n/a)</td><td>122.00 (n/a)</td><td>17.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (-5.17%)</td><td>0.13 (+8.23%)</td><td>0.13 (+19.27%)</td><td>0.10 (+13.52%)</td><td>0.02 <b>(-37.28%)</b></td><td>196.40 (-11.93%)</td><td>162.64 (-9.56%)</td><td>158.50 (-16.18%)</td><td>140.00 (+5.42%)</td><td>21.39 <b>(-40.33%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>223.00 (n/a)</td><td>179.84 (n/a)</td><td>189.10 (n/a)</td><td>132.80 (n/a)</td><td>35.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (+0.15%)</td><td>0.13 <b>(+21.71%)</b></td><td>0.13 <b>(+28.55%)</b></td><td>0.11 <b>(+100.78%)</b></td><td>0.02 <b>(-52.18%)</b></td><td>192.40 <b>(-50.21%)</b></td><td>163.34 <b>(-25.93%)</b></td><td>153.60 <b>(-22.19%)</b></td><td>139.10 (-0.14%)</td><td>21.88 <b>(-77.39%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>386.40 (n/a)</td><td>220.52 (n/a)</td><td>197.40 (n/a)</td><td>139.30 (n/a)</td><td>96.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (+1.71%)</td><td>0.13 (+2.44%)</td><td>0.13 (-3.22%)</td><td>0.11 (+15.99%)</td><td>0.02 <b>(-21.81%)</b></td><td>186.40 (-13.78%)</td><td>161.78 (-3.53%)</td><td>158.20 (+3.33%)</td><td>136.80 (-1.65%)</td><td>20.60 <b>(-33.70%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>216.20 (n/a)</td><td>167.70 (n/a)</td><td>153.10 (n/a)</td><td>139.10 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (-8.13%)</td><td>0.13 (+8.62%)</td><td>0.13 (+12.48%)</td><td>0.11 <b>(+20.32%)</b></td><td>0.02 <b>(-37.93%)</b></td><td>178.10 (-16.89%)</td><td>155.88 (-10.12%)</td><td>153.50 (-11.07%)</td><td>133.00 (+8.84%)</td><td>20.51 <b>(-42.60%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>214.30 (n/a)</td><td>173.44 (n/a)</td><td>172.60 (n/a)</td><td>122.20 (n/a)</td><td>35.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (-16.78%)</td><td>0.10 (+1.87%)</td><td>0.11 (-10.78%)</td><td>0.09 <b>(+38.77%)</b></td><td>0.01 <b>(-60.29%)</b></td><td>229.60 <b>(-27.91%)</b></td><td>198.54 (-11.14%)</td><td>194.00 (+12.07%)</td><td>166.10 <b>(+20.10%)</b></td><td>27.73 <b>(-67.79%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>318.50 (n/a)</td><td>223.44 (n/a)</td><td>173.10 (n/a)</td><td>138.30 (n/a)</td><td>86.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (-2.58%)</td><td>0.12 (+0.45%)</td><td>0.12 (-5.12%)</td><td>0.09 (-0.51%)</td><td>0.02 (-10.49%)</td><td>231.20 (+0.52%)</td><td>177.82 (-0.84%)</td><td>170.20 (+5.39%)</td><td>155.00 (+2.65%)</td><td>31.04 (-6.17%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>230.00 (n/a)</td><td>179.32 (n/a)</td><td>161.50 (n/a)</td><td>151.00 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (-2.75%)</td><td>0.15 (-1.71%)</td><td>0.15 (+0.29%)</td><td>0.12 (-11.22%)</td><td>0.02 (+12.65%)</td><td>204.70 (+12.66%)</td><td>167.40 (+2.30%)</td><td>164.90 (-0.30%)</td><td>137.90 (+2.83%)</td><td>24.13 <b>(+35.07%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.70 (n/a)</td><td>163.64 (n/a)</td><td>165.40 (n/a)</td><td>134.10 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (+5.88%)</td><td>0.14 (+3.46%)</td><td>0.14 (+1.75%)</td><td>0.12 (+1.93%)</td><td>0.02 <b>(+25.75%)</b></td><td>202.60 (-1.89%)</td><td>172.68 (-2.98%)</td><td>177.10 (-1.72%)</td><td>150.70 (-5.52%)</td><td>21.47 (+14.82%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>177.98 (n/a)</td><td>180.20 (n/a)</td><td>159.50 (n/a)</td><td>18.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (-4.95%)</td><td>0.13 (-10.00%)</td><td>0.13 (-11.68%)</td><td>0.08 <b>(-26.13%)</b></td><td>0.03 <b>(+49.28%)</b></td><td>290.70 <b>(+35.34%)</b></td><td>199.92 (+15.15%)</td><td>192.80 (+13.21%)</td><td>151.10 (+5.22%)</td><td>55.42 <b>(+110.96%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.80 (n/a)</td><td>173.62 (n/a)</td><td>170.30 (n/a)</td><td>143.60 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (+18.09%)</td><td>0.14 (+11.17%)</td><td>0.14 (+16.69%)</td><td>0.10 (-10.66%)</td><td>0.03 <b>(+87.04%)</b></td><td>240.00 (+11.94%)</td><td>175.42 (-7.95%)</td><td>169.90 (-14.32%)</td><td>141.90 (-15.33%)</td><td>38.24 <b>(+85.98%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>190.58 (n/a)</td><td>198.30 (n/a)</td><td>167.60 (n/a)</td><td>20.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (+17.97%)</td><td>0.16 (+9.36%)</td><td>0.16 (+1.73%)</td><td>0.14 (+6.38%)</td><td>0.02 <b>(+54.03%)</b></td><td>179.40 (-5.97%)</td><td>154.26 (-7.84%)</td><td>157.20 (-1.69%)</td><td>124.90 (-15.26%)</td><td>22.13 <b>(+21.64%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.80 (n/a)</td><td>167.38 (n/a)</td><td>159.90 (n/a)</td><td>147.40 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (+17.09%)</td><td>0.15 (+15.63%)</td><td>0.15 (+7.87%)</td><td>0.12 <b>(+72.36%)</b></td><td>0.03 <b>(-22.04%)</b></td><td>210.80 <b>(-41.99%)</b></td><td>171.40 (-19.18%)</td><td>166.90 (-7.33%)</td><td>128.00 (-14.61%)</td><td>30.66 <b>(-64.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>363.40 (n/a)</td><td>212.08 (n/a)</td><td>180.10 (n/a)</td><td>149.90 (n/a)</td><td>86.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (+15.62%)</td><td>0.15 (+17.29%)</td><td>0.14 (+10.79%)</td><td>0.13 <b>(+20.23%)</b></td><td>0.02 <b>(+42.72%)</b></td><td>196.20 (-16.83%)</td><td>169.58 (-14.15%)</td><td>177.20 (-9.78%)</td><td>139.30 (-13.53%)</td><td>27.40 (+2.33%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>235.90 (n/a)</td><td>197.54 (n/a)</td><td>196.40 (n/a)</td><td>161.10 (n/a)</td><td>26.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (-9.86%)</td><td>0.14 (-2.49%)</td><td>0.14 (-5.02%)</td><td>0.12 (+8.50%)</td><td>0.01 <b>(-52.27%)</b></td><td>202.40 (-7.83%)</td><td>181.94 (+1.24%)</td><td>177.60 (+5.28%)</td><td>168.10 (+10.96%)</td><td>13.09 <b>(-51.33%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>179.72 (n/a)</td><td>168.70 (n/a)</td><td>151.50 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (-9.39%)</td><td>0.11 (-18.61%)</td><td>0.12 (-2.48%)</td><td>0.05 <b>(-53.77%)</b></td><td>0.03 <b>(+59.53%)</b></td><td>364.30 <b>(+116.33%)</b></td><td>199.24 <b>(+36.86%)</b></td><td>158.60 (+2.59%)</td><td>127.10 (+10.33%)</td><td>94.79 <b>(+310.96%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>168.40 (n/a)</td><td>145.58 (n/a)</td><td>154.60 (n/a)</td><td>115.20 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (+1.95%)</td><td>0.12 (+4.02%)</td><td>0.11 (-1.73%)</td><td>0.11 (+17.32%)</td><td>0.02 (-7.88%)</td><td>167.90 (-14.77%)</td><td>152.20 (-4.36%)</td><td>162.50 (+1.75%)</td><td>126.90 (-1.93%)</td><td>19.13 <b>(-22.67%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>197.00 (n/a)</td><td>159.14 (n/a)</td><td>159.70 (n/a)</td><td>129.40 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (+6.63%)</td><td>0.12 (+12.84%)</td><td>0.13 <b>(+27.41%)</b></td><td>0.08 (+3.27%)</td><td>0.03 <b>(+26.53%)</b></td><td>230.60 (-3.19%)</td><td>164.44 (-10.06%)</td><td>144.90 <b>(-21.51%)</b></td><td>127.90 (-6.23%)</td><td>42.41 (+15.18%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>238.20 (n/a)</td><td>182.84 (n/a)</td><td>184.60 (n/a)</td><td>136.40 (n/a)</td><td>36.82 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (-7.20%)</td><td>0.12 (+5.66%)</td><td>0.11 (+5.52%)</td><td>0.10 (+9.81%)</td><td>0.02 <b>(-30.27%)</b></td><td>189.20 (-8.95%)</td><td>160.52 (-7.21%)</td><td>167.50 (-5.21%)</td><td>125.70 (+7.71%)</td><td>24.23 <b>(-29.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>207.80 (n/a)</td><td>173.00 (n/a)</td><td>176.70 (n/a)</td><td>116.70 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (+7.17%)</td><td>0.11 (+3.68%)</td><td>0.11 (+0.70%)</td><td>0.09 (+12.67%)</td><td>0.02 (+4.52%)</td><td>214.50 (-11.25%)</td><td>171.08 (-3.92%)</td><td>169.50 (-0.70%)</td><td>132.50 (-6.69%)</td><td>31.84 (-16.35%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>241.70 (n/a)</td><td>178.06 (n/a)</td><td>170.70 (n/a)</td><td>142.00 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 <b>(-20.74%)</b></td><td>0.11 (-11.17%)</td><td>0.11 (-15.68%)</td><td>0.10 (+19.19%)</td><td>0.01 <b>(-72.97%)</b></td><td>178.40 (-16.13%)</td><td>166.52 (+7.99%)</td><td>166.30 (+18.62%)</td><td>153.20 <b>(+26.19%)</b></td><td>11.25 <b>(-70.80%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>212.70 (n/a)</td><td>154.20 (n/a)</td><td>140.20 (n/a)</td><td>121.40 (n/a)</td><td>38.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 <b>(+38.94%)</b></td><td>0.11 <b>(+43.12%)</b></td><td>0.11 <b>(+53.86%)</b></td><td>0.09 <b>(+40.78%)</b></td><td>0.01 (+17.63%)</td><td>213.90 <b>(-28.96%)</b></td><td>176.94 <b>(-30.52%)</b></td><td>168.20 <b>(-35.01%)</b></td><td>151.00 <b>(-28.03%)</b></td><td>24.73 <b>(-38.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>301.10 (n/a)</td><td>254.68 (n/a)</td><td>258.80 (n/a)</td><td>209.80 (n/a)</td><td>40.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (+8.01%)</td><td>0.11 (+9.00%)</td><td>0.12 (+13.66%)</td><td>0.07 (-9.87%)</td><td>0.02 <b>(+60.60%)</b></td><td>258.40 (+10.95%)</td><td>180.42 (-6.03%)</td><td>160.10 (-12.03%)</td><td>150.80 (-7.43%)</td><td>44.46 <b>(+67.86%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>192.00 (n/a)</td><td>182.00 (n/a)</td><td>162.90 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.67 (-9.02%)</td><td>0.59 (+4.63%)</td><td>0.59 (+18.70%)</td><td>0.52 <b>(+25.72%)</b></td><td>0.06 <b>(-58.05%)</b></td><td>190.30 <b>(-20.44%)</b></td><td>167.12 (-8.35%)</td><td>165.40 (-15.74%)</td><td>147.70 (+9.90%)</td><td>17.14 <b>(-61.64%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.73 (n/a)</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.14 (n/a)</td><td>239.20 (n/a)</td><td>182.34 (n/a)</td><td>196.30 (n/a)</td><td>134.40 (n/a)</td><td>44.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.73 (+18.25%)</td><td>0.61 (+18.90%)</td><td>0.60 (+15.61%)</td><td>0.48 (+17.81%)</td><td>0.09 (+4.29%)</td><td>206.80 (-15.11%)</td><td>165.58 (-16.35%)</td><td>163.00 (-13.48%)</td><td>134.70 (-15.44%)</td><td>26.52 <b>(-24.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.62 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.09 (n/a)</td><td>243.60 (n/a)</td><td>197.94 (n/a)</td><td>188.40 (n/a)</td><td>159.30 (n/a)</td><td>35.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.78 <b>(+20.58%)</b></td><td>0.62 (+13.57%)</td><td>0.58 (+8.77%)</td><td>0.52 (+14.53%)</td><td>0.10 <b>(+37.37%)</b></td><td>190.40 (-12.66%)</td><td>162.42 (-11.47%)</td><td>169.20 (-8.04%)</td><td>126.50 (-17.05%)</td><td>24.92 (-1.34%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.07 (n/a)</td><td>218.00 (n/a)</td><td>183.46 (n/a)</td><td>184.00 (n/a)</td><td>152.50 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.65 (+6.76%)</td><td>0.53 (-0.96%)</td><td>0.50 (-3.76%)</td><td>0.44 (+4.22%)</td><td>0.08 (+6.57%)</td><td>224.10 (-4.07%)</td><td>190.08 (+0.99%)</td><td>196.10 (+3.92%)</td><td>152.00 (-6.35%)</td><td>26.99 (-5.23%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.61 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>233.60 (n/a)</td><td>188.22 (n/a)</td><td>188.70 (n/a)</td><td>162.30 (n/a)</td><td>28.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.57 (+11.85%)</td><td>0.45 (-0.06%)</td><td>0.42 (-15.51%)</td><td>0.40 <b>(+20.20%)</b></td><td>0.07 (-7.41%)</td><td>185.80 (-16.79%)</td><td>164.86 (-0.94%)</td><td>174.70 (+18.36%)</td><td>129.20 (-10.65%)</td><td>22.70 <b>(-31.94%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.51 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>223.30 (n/a)</td><td>166.42 (n/a)</td><td>147.60 (n/a)</td><td>144.60 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.60 (+17.27%)</td><td>0.44 (+4.57%)</td><td>0.42 (+1.43%)</td><td>0.31 (-13.30%)</td><td>0.11 <b>(+90.60%)</b></td><td>238.80 (+15.31%)</td><td>176.10 (-0.88%)</td><td>175.80 (-1.40%)</td><td>122.10 (-14.73%)</td><td>43.78 <b>(+89.91%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>207.10 (n/a)</td><td>177.66 (n/a)</td><td>178.30 (n/a)</td><td>143.20 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.47 (-5.41%)</td><td>0.40 (-12.46%)</td><td>0.37 (-19.14%)</td><td>0.37 (+1.38%)</td><td>0.04 <b>(-20.77%)</b></td><td>199.10 (-1.39%)</td><td>187.82 (+13.72%)</td><td>197.10 <b>(+23.65%)</b></td><td>157.10 (+5.72%)</td><td>17.67 (-18.65%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.50 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>201.90 (n/a)</td><td>165.16 (n/a)</td><td>159.40 (n/a)</td><td>148.60 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.52 (+10.14%)</td><td>0.43 <b>(+20.46%)</b></td><td>0.40 <b>(+33.07%)</b></td><td>0.36 <b>(+27.17%)</b></td><td>0.06 <b>(-26.19%)</b></td><td>202.80 <b>(-21.36%)</b></td><td>175.86 (-19.12%)</td><td>183.70 <b>(-24.87%)</b></td><td>142.40 (-9.24%)</td><td>24.31 <b>(-48.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>257.90 (n/a)</td><td>217.42 (n/a)</td><td>244.50 (n/a)</td><td>156.90 (n/a)</td><td>47.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (+7.21%)</td><td>0.21 (+1.88%)</td><td>0.20 (+0.27%)</td><td>0.19 (+2.93%)</td><td>0.03 <b>(+29.66%)</b></td><td>197.80 (-2.85%)</td><td>177.02 (-1.47%)</td><td>180.80 (-0.28%)</td><td>144.40 (-6.78%)</td><td>20.53 (+16.67%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>179.66 (n/a)</td><td>181.30 (n/a)</td><td>154.90 (n/a)</td><td>17.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (-14.71%)</td><td>0.20 (-8.72%)</td><td>0.19 (-9.54%)</td><td>0.17 (+7.38%)</td><td>0.03 <b>(-40.74%)</b></td><td>216.40 (-6.88%)</td><td>190.10 (+7.15%)</td><td>195.90 (+10.49%)</td><td>155.80 (+17.23%)</td><td>24.58 <b>(-35.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>232.40 (n/a)</td><td>177.42 (n/a)</td><td>177.30 (n/a)</td><td>132.90 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.29 (+12.32%)</td><td>0.23 (+8.10%)</td><td>0.24 (+14.19%)</td><td>0.15 (+3.62%)</td><td>0.05 <b>(+25.28%)</b></td><td>241.90 (-3.47%)</td><td>169.38 (-6.36%)</td><td>153.30 (-12.40%)</td><td>125.70 (-10.98%)</td><td>44.74 (+7.18%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>250.60 (n/a)</td><td>180.88 (n/a)</td><td>175.00 (n/a)</td><td>141.20 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.29 (-3.20%)</td><td>0.23 (+3.53%)</td><td>0.23 (+15.91%)</td><td>0.18 (-3.89%)</td><td>0.04 (-12.32%)</td><td>205.60 (+4.05%)</td><td>165.08 (-3.86%)</td><td>159.90 (-13.71%)</td><td>129.10 (+3.28%)</td><td>27.97 (-4.30%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>197.60 (n/a)</td><td>171.70 (n/a)</td><td>185.30 (n/a)</td><td>125.00 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (+3.84%)</td><td>0.22 (+0.18%)</td><td>0.20 (-3.04%)</td><td>0.20 <b>(+20.88%)</b></td><td>0.03 <b>(-23.48%)</b></td><td>186.30 (-17.27%)</td><td>170.64 (-1.67%)</td><td>180.10 (+3.15%)</td><td>136.00 (-3.75%)</td><td>21.00 <b>(-38.09%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>225.20 (n/a)</td><td>173.54 (n/a)</td><td>174.60 (n/a)</td><td>141.30 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (+2.53%)</td><td>0.21 (+9.79%)</td><td>0.21 (+14.61%)</td><td>0.20 (+11.53%)</td><td>0.01 <b>(-28.03%)</b></td><td>187.00 (-10.31%)</td><td>173.82 (-9.30%)</td><td>174.50 (-12.75%)</td><td>158.70 (-2.46%)</td><td>11.62 <b>(-36.37%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>208.50 (n/a)</td><td>191.64 (n/a)</td><td>200.00 (n/a)</td><td>162.70 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (-13.71%)</td><td>0.19 (-6.22%)</td><td>0.19 (+1.72%)</td><td>0.17 (-4.39%)</td><td>0.01 <b>(-49.15%)</b></td><td>212.30 (+4.58%)</td><td>198.16 (+5.92%)</td><td>195.70 (-1.66%)</td><td>186.20 (+15.87%)</td><td>12.29 <b>(-39.17%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>187.08 (n/a)</td><td>199.00 (n/a)</td><td>160.70 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 <b>(-35.21%)</b></td><td>0.18 (-18.93%)</td><td>0.18 (-15.28%)</td><td>0.16 (-14.30%)</td><td>0.01 <b>(-72.23%)</b></td><td>234.10 (+16.70%)</td><td>209.20 <b>(+20.88%)</b></td><td>202.80 (+18.04%)</td><td>199.50 <b>(+54.41%)</b></td><td>14.26 <b>(-48.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>200.60 (n/a)</td><td>173.06 (n/a)</td><td>171.80 (n/a)</td><td>129.20 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.30 (-0.16%)</td><td>0.23 (-6.38%)</td><td>0.22 (-10.36%)</td><td>0.20 (-5.73%)</td><td>0.04 <b>(+25.55%)</b></td><td>202.20 (+6.09%)</td><td>180.68 (+7.66%)</td><td>190.20 (+11.55%)</td><td>137.80 (+0.22%)</td><td>25.74 <b>(+34.02%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>190.60 (n/a)</td><td>167.82 (n/a)</td><td>170.50 (n/a)</td><td>137.50 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (-8.84%)</td><td>0.22 (-5.90%)</td><td>0.22 (-3.97%)</td><td>0.20 (+6.32%)</td><td>0.01 <b>(-49.66%)</b></td><td>205.60 (-5.90%)</td><td>189.88 (+5.37%)</td><td>185.30 (+4.16%)</td><td>176.40 (+9.70%)</td><td>11.78 <b>(-48.41%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>218.50 (n/a)</td><td>180.20 (n/a)</td><td>177.90 (n/a)</td><td>160.80 (n/a)</td><td>22.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.34 (+14.64%)</td><td>0.27 (+1.18%)</td><td>0.30 (+9.95%)</td><td>0.17 <b>(-25.05%)</b></td><td>0.07 <b>(+179.07%)</b></td><td>235.70 <b>(+33.39%)</b></td><td>159.68 (+4.34%)</td><td>137.40 (-9.01%)</td><td>122.00 (-12.79%)</td><td>47.77 <b>(+221.72%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>176.70 (n/a)</td><td>153.04 (n/a)</td><td>151.00 (n/a)</td><td>139.90 (n/a)</td><td>14.85 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.31 (-16.29%)</td><td>0.25 (-9.12%)</td><td>0.26 (+8.08%)</td><td>0.16 <b>(-31.92%)</b></td><td>0.06 (-6.87%)</td><td>258.50 <b>(+46.88%)</b></td><td>175.58 (+12.08%)</td><td>160.10 (-7.51%)</td><td>130.00 (+19.49%)</td><td>49.25 <b>(+69.90%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>176.00 (n/a)</td><td>156.66 (n/a)</td><td>173.10 (n/a)</td><td>108.80 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (-1.99%)</td><td>0.20 (-4.48%)</td><td>0.22 (+8.79%)</td><td>0.11 <b>(-40.51%)</b></td><td>0.05 <b>(+94.18%)</b></td><td>379.20 <b>(+68.09%)</b></td><td>220.98 (+12.96%)</td><td>182.70 (-8.10%)</td><td>168.60 (+2.00%)</td><td>89.06 <b>(+250.35%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>225.60 (n/a)</td><td>195.62 (n/a)</td><td>198.80 (n/a)</td><td>165.30 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.28 (-1.82%)</td><td>0.22 (+5.13%)</td><td>0.21 (-0.26%)</td><td>0.19 <b>(+24.67%)</b></td><td>0.04 <b>(-21.02%)</b></td><td>217.00 (-19.78%)</td><td>187.60 (-6.73%)</td><td>199.50 (+0.25%)</td><td>144.70 (+1.83%)</td><td>29.53 <b>(-35.41%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>270.50 (n/a)</td><td>201.14 (n/a)</td><td>199.00 (n/a)</td><td>142.10 (n/a)</td><td>45.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.33 <b>(+30.07%)</b></td><td>0.25 <b>(+21.93%)</b></td><td>0.23 (+10.71%)</td><td>0.20 <b>(+38.70%)</b></td><td>0.05 (+17.14%)</td><td>209.40 <b>(-27.89%)</b></td><td>169.56 (-18.86%)</td><td>174.60 (-9.67%)</td><td>125.20 <b>(-23.14%)</b></td><td>30.60 <b>(-38.22%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>290.40 (n/a)</td><td>208.98 (n/a)</td><td>193.30 (n/a)</td><td>162.90 (n/a)</td><td>49.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (-5.53%)</td><td>0.23 (-3.36%)</td><td>0.22 (-4.28%)</td><td>0.20 (+1.16%)</td><td>0.03 <b>(-21.23%)</b></td><td>206.30 (-1.15%)</td><td>178.78 (+2.81%)</td><td>186.90 (+4.47%)</td><td>150.80 (+5.82%)</td><td>22.00 (-17.37%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>208.70 (n/a)</td><td>173.90 (n/a)</td><td>178.90 (n/a)</td><td>142.50 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 <b>(+21.59%)</b></td><td>0.21 (+9.19%)</td><td>0.20 (-7.11%)</td><td>0.17 <b>(+24.07%)</b></td><td>0.04 <b>(+25.67%)</b></td><td>205.10 (-19.38%)</td><td>169.28 (-8.34%)</td><td>178.20 (+7.67%)</td><td>129.30 (-17.75%)</td><td>32.96 (-18.49%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>254.40 (n/a)</td><td>184.68 (n/a)</td><td>165.50 (n/a)</td><td>157.20 (n/a)</td><td>40.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (-8.89%)</td><td>0.20 (-3.60%)</td><td>0.18 (-10.66%)</td><td>0.16 (+2.83%)</td><td>0.03 (-17.09%)</td><td>215.70 (-2.75%)</td><td>181.98 (+2.98%)</td><td>193.10 (+11.94%)</td><td>145.80 (+9.71%)</td><td>28.61 (-11.71%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>221.80 (n/a)</td><td>176.72 (n/a)</td><td>172.50 (n/a)</td><td>132.90 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.28 (+0.47%)</td><td>0.23 (+3.47%)</td><td>0.23 (-4.70%)</td><td>0.17 (+1.09%)</td><td>0.04 (-13.75%)</td><td>201.40 (-1.08%)</td><td>152.66 (-4.49%)</td><td>151.50 (+4.92%)</td><td>126.00 (-0.47%)</td><td>30.74 (-17.00%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>203.60 (n/a)</td><td>159.84 (n/a)</td><td>144.40 (n/a)</td><td>126.60 (n/a)</td><td>37.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (+19.25%)</td><td>0.22 (+11.41%)</td><td>0.22 (+3.84%)</td><td>0.14 (-8.57%)</td><td>0.05 <b>(+68.95%)</b></td><td>245.00 (+9.38%)</td><td>167.10 (-7.36%)</td><td>160.00 (-3.67%)</td><td>128.30 (-16.14%)</td><td>46.36 <b>(+57.40%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>224.00 (n/a)</td><td>180.38 (n/a)</td><td>166.10 (n/a)</td><td>153.00 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (-5.25%)</td><td>0.21 (+0.71%)</td><td>0.21 (+3.22%)</td><td>0.16 (+1.68%)</td><td>0.04 (+7.21%)</td><td>215.10 (-1.69%)</td><td>173.12 (-0.16%)</td><td>163.20 (-3.15%)</td><td>139.60 (+5.52%)</td><td>36.23 (+10.67%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>218.80 (n/a)</td><td>173.40 (n/a)</td><td>168.50 (n/a)</td><td>132.30 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (+17.44%)</td><td>0.21 (+13.00%)</td><td>0.21 (+10.07%)</td><td>0.14 (-6.43%)</td><td>0.04 <b>(+49.97%)</b></td><td>241.20 (+6.87%)</td><td>173.40 (-9.76%)</td><td>164.80 (-9.10%)</td><td>133.90 (-14.82%)</td><td>40.83 <b>(+37.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.70 (n/a)</td><td>192.16 (n/a)</td><td>181.30 (n/a)</td><td>157.20 (n/a)</td><td>29.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (+7.28%)</td><td>0.21 (+9.17%)</td><td>0.22 (+15.75%)</td><td>0.17 (-3.08%)</td><td>0.03 <b>(+31.17%)</b></td><td>205.10 (+3.17%)</td><td>165.90 (-7.89%)</td><td>160.90 (-13.63%)</td><td>146.50 (-6.81%)</td><td>22.72 <b>(+30.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>180.12 (n/a)</td><td>186.30 (n/a)</td><td>157.20 (n/a)</td><td>17.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (-0.75%)</td><td>0.19 (+0.53%)</td><td>0.18 (-2.39%)</td><td>0.16 (+4.07%)</td><td>0.02 <b>(-23.73%)</b></td><td>214.20 (-3.90%)</td><td>188.38 (-1.22%)</td><td>188.30 (+2.45%)</td><td>164.80 (+0.73%)</td><td>19.73 <b>(-26.55%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>222.90 (n/a)</td><td>190.70 (n/a)</td><td>183.80 (n/a)</td><td>163.60 (n/a)</td><td>26.87 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.93 (+0.65%)</td><td>0.83 <b>(+20.78%)</b></td><td>0.81 <b>(+23.52%)</b></td><td>0.69 <b>(+44.26%)</b></td><td>0.10 <b>(-39.71%)</b></td><td>190.30 <b>(-30.67%)</b></td><td>160.70 (-19.91%)</td><td>162.70 (-19.01%)</td><td>140.60 (-0.64%)</td><td>19.73 <b>(-58.90%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.93 (n/a)</td><td>0.68 (n/a)</td><td>0.65 (n/a)</td><td>0.48 (n/a)</td><td>0.16 (n/a)</td><td>274.50 (n/a)</td><td>200.64 (n/a)</td><td>200.90 (n/a)</td><td>141.50 (n/a)</td><td>47.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.00 (+6.25%)</td><td>0.65 (-16.57%)</td><td>0.70 (-8.78%)</td><td>0.34 <b>(-50.33%)</b></td><td>0.29 <b>(+189.56%)</b></td><td>387.10 <b>(+101.30%)</b></td><td>244.54 <b>(+43.61%)</b></td><td>186.60 (+9.64%)</td><td>130.60 (-5.91%)</td><td>121.34 <b>(+491.79%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.94 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.68 (n/a)</td><td>0.10 (n/a)</td><td>192.30 (n/a)</td><td>170.28 (n/a)</td><td>170.20 (n/a)</td><td>138.80 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.30 <b>(+20.13%)</b></td><td>0.88 (+1.13%)</td><td>0.83 (-5.35%)</td><td>0.60 (-7.25%)</td><td>0.27 <b>(+37.53%)</b></td><td>217.90 (+7.82%)</td><td>159.02 (+1.45%)</td><td>158.80 (+5.66%)</td><td>100.60 (-16.79%)</td><td>43.89 <b>(+22.42%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>1.08 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.65 (n/a)</td><td>0.19 (n/a)</td><td>202.10 (n/a)</td><td>156.74 (n/a)</td><td>150.30 (n/a)</td><td>120.90 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.00 (+0.00%)</td><td>0.00 (+2.37%)</td><td>0.00 (+2.33%)</td><td>0.00 (+5.13%)</td><td>0.00 <b>(-27.94%)</b></td><td>1005.86 (-3.24%)</td><td>952.13 (-1.61%)</td><td>941.23 (-0.84%)</td><td>909.90 (+0.63%)</td><td>35.80 <b>(-32.76%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1039.56 (n/a)</td><td>967.69 (n/a)</td><td>949.21 (n/a)</td><td>904.24 (n/a)</td><td>53.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.01 (+1.22%)</td><td>0.01 (+1.25%)</td><td>0.01 (+1.23%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(+29.45%)</b></td><td>1061.95 (+0.36%)</td><td>1010.42 (-0.99%)</td><td>1000.75 (-1.64%)</td><td>989.89 (-0.69%)</td><td>29.65 <b>(+30.76%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1058.10 (n/a)</td><td>1020.57 (n/a)</td><td>1017.40 (n/a)</td><td>996.74 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.97 (+2.75%)</td><td>0.94 (+1.25%)</td><td>0.93 (+0.03%)</td><td>0.92 (+1.54%)</td><td>0.02 <b>(+42.31%)</b></td><td>2267.94 (-1.51%)</td><td>2231.49 (-1.22%)</td><td>2252.74 (-0.04%)</td><td>2150.83 (-2.68%)</td><td>48.15 <b>(+36.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.95 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.91 (n/a)</td><td>0.01 (n/a)</td><td>2302.71 (n/a)</td><td>2259.06 (n/a)</td><td>2253.58 (n/a)</td><td>2210.16 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>5.16 (-12.30%)</td><td>4.61 (-5.46%)</td><td>4.66 (-3.64%)</td><td>3.75 (+4.74%)</td><td>0.56 <b>(-41.16%)</b></td><td>279.40 (-4.54%)</td><td>230.54 (+3.68%)</td><td>225.10 (+3.78%)</td><td>203.10 (+14.04%)</td><td>30.36 <b>(-34.82%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.89 (n/a)</td><td>4.87 (n/a)</td><td>4.83 (n/a)</td><td>3.58 (n/a)</td><td>0.95 (n/a)</td><td>292.70 (n/a)</td><td>222.36 (n/a)</td><td>216.90 (n/a)</td><td>178.10 (n/a)</td><td>46.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>4.81 <b>(-20.04%)</b></td><td>4.54 (-7.90%)</td><td>4.52 (-7.63%)</td><td>4.31 (+1.89%)</td><td>0.18 <b>(-72.55%)</b></td><td>243.50 (-1.85%)</td><td>231.40 (+7.24%)</td><td>232.10 (+8.26%)</td><td>217.80 <b>(+25.03%)</b></td><td>9.27 <b>(-65.70%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>6.02 (n/a)</td><td>4.93 (n/a)</td><td>4.89 (n/a)</td><td>4.23 (n/a)</td><td>0.67 (n/a)</td><td>248.10 (n/a)</td><td>215.78 (n/a)</td><td>214.40 (n/a)</td><td>174.20 (n/a)</td><td>27.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.20 (+13.40%)</td><td>4.48 (-7.67%)</td><td>4.10 (-13.12%)</td><td>3.82 (-16.56%)</td><td>0.97 <b>(+174.43%)</b></td><td>274.50 (+19.87%)</td><td>241.08 (+11.18%)</td><td>255.70 (+15.13%)</td><td>169.20 (-11.83%)</td><td>41.38 <b>(+183.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.47 (n/a)</td><td>4.85 (n/a)</td><td>4.72 (n/a)</td><td>4.58 (n/a)</td><td>0.35 (n/a)</td><td>229.00 (n/a)</td><td>216.84 (n/a)</td><td>222.10 (n/a)</td><td>191.90 (n/a)</td><td>14.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>5.06 (-10.51%)</td><td>4.77 (-6.18%)</td><td>4.86 (-3.83%)</td><td>4.30 (+5.51%)</td><td>0.32 <b>(-50.31%)</b></td><td>243.80 (-5.21%)</td><td>220.74 (+5.50%)</td><td>215.70 (+4.00%)</td><td>207.10 (+11.70%)</td><td>15.29 <b>(-47.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.66 (n/a)</td><td>5.08 (n/a)</td><td>5.05 (n/a)</td><td>4.08 (n/a)</td><td>0.64 (n/a)</td><td>257.20 (n/a)</td><td>209.24 (n/a)</td><td>207.40 (n/a)</td><td>185.40 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.51 (+7.86%)</td><td>7.54 (+0.79%)</td><td>7.83 (+7.62%)</td><td>5.64 <b>(-20.86%)</b></td><td>1.10 <b>(+203.51%)</b></td><td>371.60 <b>(+26.35%)</b></td><td>284.10 (+1.11%)</td><td>268.00 (-7.07%)</td><td>246.30 (-7.27%)</td><td>49.94 <b>(+270.20%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>7.89 (n/a)</td><td>7.48 (n/a)</td><td>7.27 (n/a)</td><td>7.13 (n/a)</td><td>0.36 (n/a)</td><td>294.10 (n/a)</td><td>280.98 (n/a)</td><td>288.40 (n/a)</td><td>265.60 (n/a)</td><td>13.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.92 (+1.31%)</td><td>8.01 (+0.28%)</td><td>7.97 (-2.26%)</td><td>7.51 (+8.98%)</td><td>0.55 <b>(-21.30%)</b></td><td>279.40 (-8.24%)</td><td>262.74 (-0.57%)</td><td>263.30 (+2.33%)</td><td>235.10 (-1.30%)</td><td>17.01 <b>(-30.60%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.80 (n/a)</td><td>7.99 (n/a)</td><td>8.15 (n/a)</td><td>6.89 (n/a)</td><td>0.70 (n/a)</td><td>304.50 (n/a)</td><td>264.24 (n/a)</td><td>257.30 (n/a)</td><td>238.20 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.47 (-5.76%)</td><td>7.86 (+4.21%)</td><td>7.90 (+6.42%)</td><td>7.28 (+7.06%)</td><td>0.47 <b>(-45.33%)</b></td><td>288.10 (-6.61%)</td><td>267.48 (-4.70%)</td><td>265.40 (-6.05%)</td><td>247.70 (+6.08%)</td><td>16.08 <b>(-45.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>8.98 (n/a)</td><td>7.54 (n/a)</td><td>7.42 (n/a)</td><td>6.80 (n/a)</td><td>0.86 (n/a)</td><td>308.50 (n/a)</td><td>280.66 (n/a)</td><td>282.50 (n/a)</td><td>233.50 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.09 (-12.70%)</td><td>8.32 (-4.75%)</td><td>8.43 (-3.54%)</td><td>7.20 (-1.75%)</td><td>0.69 <b>(-40.77%)</b></td><td>291.20 (+1.75%)</td><td>253.56 (+4.11%)</td><td>248.80 (+3.67%)</td><td>230.70 (+14.55%)</td><td>22.63 <b>(-29.78%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>10.41 (n/a)</td><td>8.73 (n/a)</td><td>8.74 (n/a)</td><td>7.33 (n/a)</td><td>1.17 (n/a)</td><td>286.20 (n/a)</td><td>243.54 (n/a)</td><td>240.00 (n/a)</td><td>201.40 (n/a)</td><td>32.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.06 (-1.15%)</td><td>8.33 (+0.41%)</td><td>8.20 (-0.86%)</td><td>7.56 (-2.50%)</td><td>0.59 (+8.82%)</td><td>277.40 (+2.55%)</td><td>252.78 (-0.35%)</td><td>255.90 (+0.87%)</td><td>231.40 (+1.14%)</td><td>18.09 (+13.20%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.17 (n/a)</td><td>8.30 (n/a)</td><td>8.27 (n/a)</td><td>7.75 (n/a)</td><td>0.54 (n/a)</td><td>270.50 (n/a)</td><td>253.66 (n/a)</td><td>253.70 (n/a)</td><td>228.80 (n/a)</td><td>15.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.00 (-5.20%)</td><td>8.19 (+3.21%)</td><td>8.35 (+6.44%)</td><td>7.06 (+4.56%)</td><td>0.72 <b>(-33.02%)</b></td><td>296.90 (-4.35%)</td><td>257.92 (-3.85%)</td><td>251.30 (-6.06%)</td><td>233.00 (+5.53%)</td><td>24.17 <b>(-31.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.50 (n/a)</td><td>7.93 (n/a)</td><td>7.84 (n/a)</td><td>6.76 (n/a)</td><td>1.08 (n/a)</td><td>310.40 (n/a)</td><td>268.24 (n/a)</td><td>267.50 (n/a)</td><td>220.80 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>11.41 (-10.27%)</td><td>10.66 (-6.65%)</td><td>10.89 (-3.75%)</td><td>9.79 (-6.14%)</td><td>0.79 (-16.02%)</td><td>428.60 (+6.54%)</td><td>395.20 (+7.03%)</td><td>385.00 (+3.89%)</td><td>367.50 (+11.43%)</td><td>29.64 (-0.13%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>12.72 (n/a)</td><td>11.42 (n/a)</td><td>11.32 (n/a)</td><td>10.43 (n/a)</td><td>0.94 (n/a)</td><td>402.30 (n/a)</td><td>369.24 (n/a)</td><td>370.60 (n/a)</td><td>329.80 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>10.90 (-18.26%)</td><td>10.07 (-14.81%)</td><td>9.94 (-16.73%)</td><td>9.40 (-6.82%)</td><td>0.55 <b>(-54.49%)</b></td><td>446.20 (+7.31%)</td><td>417.40 (+16.64%)</td><td>421.90 <b>(+20.10%)</b></td><td>384.90 <b>(+22.35%)</b></td><td>22.38 <b>(-41.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.33 (n/a)</td><td>11.82 (n/a)</td><td>11.94 (n/a)</td><td>10.09 (n/a)</td><td>1.21 (n/a)</td><td>415.80 (n/a)</td><td>357.84 (n/a)</td><td>351.30 (n/a)</td><td>314.60 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>12.69 (-3.27%)</td><td>11.44 (-6.33%)</td><td>11.23 (-5.35%)</td><td>10.62 (-6.71%)</td><td>0.90 (+11.00%)</td><td>394.80 (+7.20%)</td><td>368.28 (+6.90%)</td><td>373.40 (+5.66%)</td><td>330.40 (+3.38%)</td><td>28.39 <b>(+25.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>13.12 (n/a)</td><td>12.22 (n/a)</td><td>11.87 (n/a)</td><td>11.39 (n/a)</td><td>0.81 (n/a)</td><td>368.30 (n/a)</td><td>344.50 (n/a)</td><td>353.40 (n/a)</td><td>319.60 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.07 (-13.31%)</td><td>12.02 (-12.30%)</td><td>11.98 (-14.88%)</td><td>10.45 (-13.49%)</td><td>1.00 (-11.24%)</td><td>401.20 (+15.59%)</td><td>350.90 (+14.05%)</td><td>350.10 (+17.48%)</td><td>320.90 (+15.35%)</td><td>31.00 (+18.45%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>15.08 (n/a)</td><td>13.71 (n/a)</td><td>14.08 (n/a)</td><td>12.08 (n/a)</td><td>1.13 (n/a)</td><td>347.10 (n/a)</td><td>307.68 (n/a)</td><td>298.00 (n/a)</td><td>278.20 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.97 (-4.94%)</td><td>12.51 (-3.00%)</td><td>12.14 (-6.17%)</td><td>11.14 (-1.26%)</td><td>1.30 (-10.34%)</td><td>376.60 (+1.26%)</td><td>338.28 (+2.92%)</td><td>345.60 (+6.57%)</td><td>300.30 (+5.18%)</td><td>34.73 (-6.31%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>14.69 (n/a)</td><td>12.89 (n/a)</td><td>12.94 (n/a)</td><td>11.28 (n/a)</td><td>1.45 (n/a)</td><td>371.90 (n/a)</td><td>328.68 (n/a)</td><td>324.30 (n/a)</td><td>285.50 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.73 (-6.93%)</td><td>12.51 (-7.46%)</td><td>12.29 (-8.35%)</td><td>12.10 (+2.77%)</td><td>0.69 <b>(-41.08%)</b></td><td>346.70 (-2.72%)</td><td>336.12 (+7.63%)</td><td>341.40 (+9.11%)</td><td>305.40 (+7.42%)</td><td>17.36 <b>(-38.77%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>14.76 (n/a)</td><td>13.52 (n/a)</td><td>13.41 (n/a)</td><td>11.77 (n/a)</td><td>1.17 (n/a)</td><td>356.40 (n/a)</td><td>312.30 (n/a)</td><td>312.90 (n/a)</td><td>284.30 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.92 (-8.42%)</td><td>12.78 (-4.77%)</td><td>13.40 (+5.75%)</td><td>9.80 (-16.19%)</td><td>1.72 (+6.98%)</td><td>427.90 (+19.29%)</td><td>333.98 (+5.64%)</td><td>313.00 (-5.44%)</td><td>301.30 (+9.21%)</td><td>53.43 <b>(+44.37%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>15.20 (n/a)</td><td>13.42 (n/a)</td><td>12.67 (n/a)</td><td>11.69 (n/a)</td><td>1.61 (n/a)</td><td>358.70 (n/a)</td><td>316.16 (n/a)</td><td>331.00 (n/a)</td><td>275.90 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>14.18 (-4.02%)</td><td>12.02 (-11.80%)</td><td>12.55 (-8.07%)</td><td>8.51 <b>(-32.99%)</b></td><td>2.27 <b>(+140.62%)</b></td><td>493.10 <b>(+49.20%)</b></td><td>360.72 (+16.79%)</td><td>334.30 (+8.79%)</td><td>295.80 (+4.19%)</td><td>79.74 <b>(+274.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>14.78 (n/a)</td><td>13.63 (n/a)</td><td>13.65 (n/a)</td><td>12.69 (n/a)</td><td>0.94 (n/a)</td><td>330.50 (n/a)</td><td>308.86 (n/a)</td><td>307.30 (n/a)</td><td>283.90 (n/a)</td><td>21.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>2.79 (-13.83%)</td><td>2.63 (-9.88%)</td><td>2.71 (-5.12%)</td><td>2.32 (-14.99%)</td><td>0.19 (-12.04%)</td><td>226.00 (+17.65%)</td><td>200.44 (+10.99%)</td><td>193.80 (+5.38%)</td><td>188.00 (+16.05%)</td><td>15.58 (+19.45%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.24 (n/a)</td><td>2.92 (n/a)</td><td>2.85 (n/a)</td><td>2.73 (n/a)</td><td>0.22 (n/a)</td><td>192.10 (n/a)</td><td>180.60 (n/a)</td><td>183.90 (n/a)</td><td>162.00 (n/a)</td><td>13.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.12 (+8.42%)</td><td>4.76 (-0.46%)</td><td>4.68 (-0.46%)</td><td>2.95 <b>(-31.71%)</b></td><td>1.19 <b>(+131.87%)</b></td><td>355.30 <b>(+46.46%)</b></td><td>234.18 (+5.95%)</td><td>224.00 (+0.49%)</td><td>171.40 (-7.75%)</td><td>71.67 <b>(+230.35%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>5.64 (n/a)</td><td>4.78 (n/a)</td><td>4.70 (n/a)</td><td>4.32 (n/a)</td><td>0.51 (n/a)</td><td>242.60 (n/a)</td><td>221.02 (n/a)</td><td>222.90 (n/a)</td><td>185.80 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.75 (-4.38%)</td><td>7.12 (-5.19%)</td><td>6.72 (-5.14%)</td><td>5.87 (-15.10%)</td><td>1.10 (+16.64%)</td><td>357.40 (+17.80%)</td><td>300.08 (+6.25%)</td><td>312.00 (+5.41%)</td><td>239.60 (+4.58%)</td><td>44.55 <b>(+43.19%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>9.15 (n/a)</td><td>7.51 (n/a)</td><td>7.09 (n/a)</td><td>6.91 (n/a)</td><td>0.95 (n/a)</td><td>303.40 (n/a)</td><td>282.42 (n/a)</td><td>296.00 (n/a)</td><td>229.10 (n/a)</td><td>31.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.14 (-4.34%)</td><td>2.65 (-10.42%)</td><td>2.80 (-1.97%)</td><td>2.06 <b>(-21.44%)</b></td><td>0.52 <b>(+77.09%)</b></td><td>254.90 <b>(+27.32%)</b></td><td>204.62 (+14.50%)</td><td>187.50 (+2.01%)</td><td>166.80 (+4.51%)</td><td>42.57 <b>(+140.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>3.29 (n/a)</td><td>2.96 (n/a)</td><td>2.85 (n/a)</td><td>2.62 (n/a)</td><td>0.30 (n/a)</td><td>200.20 (n/a)</td><td>178.70 (n/a)</td><td>183.80 (n/a)</td><td>159.60 (n/a)</td><td>17.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 <b>(-26.31%)</b></td><td>0.18 (-11.54%)</td><td>0.18 (-9.28%)</td><td>0.17 <b>(+37.11%)</b></td><td>0.01 <b>(-78.29%)</b></td><td>197.00 <b>(-27.06%)</b></td><td>183.42 (+4.68%)</td><td>186.60 (+10.22%)</td><td>164.20 <b>(+35.70%)</b></td><td>12.77 <b>(-78.47%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>270.10 (n/a)</td><td>175.22 (n/a)</td><td>169.30 (n/a)</td><td>121.00 (n/a)</td><td>59.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 <b>(-23.06%)</b></td><td>0.15 <b>(-23.83%)</b></td><td>0.16 <b>(-20.59%)</b></td><td>0.09 <b>(-28.25%)</b></td><td>0.04 <b>(-22.24%)</b></td><td>368.30 <b>(+39.35%)</b></td><td>233.18 <b>(+32.37%)</b></td><td>207.70 <b>(+25.88%)</b></td><td>170.60 <b>(+29.93%)</b></td><td>77.50 <b>(+47.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>264.30 (n/a)</td><td>176.16 (n/a)</td><td>165.00 (n/a)</td><td>131.30 (n/a)</td><td>52.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.52 (+6.67%)</td><td>0.34 <b>(-21.22%)</b></td><td>0.32 <b>(-25.81%)</b></td><td>0.19 <b>(-47.13%)</b></td><td>0.12 <b>(+174.73%)</b></td><td>337.10 <b>(+89.17%)</b></td><td>213.08 <b>(+39.54%)</b></td><td>204.90 <b>(+34.80%)</b></td><td>126.60 (-6.22%)</td><td>78.70 <b>(+387.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.04 (n/a)</td><td>178.20 (n/a)</td><td>152.70 (n/a)</td><td>152.00 (n/a)</td><td>135.00 (n/a)</td><td>16.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.45 (-12.76%)</td><td>0.38 (-4.77%)</td><td>0.36 (-7.98%)</td><td>0.32 (-5.93%)</td><td>0.06 (-10.33%)</td><td>207.90 (+6.29%)</td><td>175.70 (+4.95%)</td><td>184.20 (+8.67%)</td><td>146.70 (+14.61%)</td><td>27.51 (+7.93%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.51 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>195.60 (n/a)</td><td>167.42 (n/a)</td><td>169.50 (n/a)</td><td>128.00 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.55 <b>(+36.64%)</b></td><td>0.39 (+13.61%)</td><td>0.36 (+0.66%)</td><td>0.33 <b>(+40.07%)</b></td><td>0.09 <b>(+38.22%)</b></td><td>198.60 <b>(-28.59%)</b></td><td>173.22 (-12.20%)</td><td>182.70 (-0.65%)</td><td>119.40 <b>(-26.79%)</b></td><td>30.90 <b>(-33.33%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>278.10 (n/a)</td><td>197.28 (n/a)</td><td>183.90 (n/a)</td><td>163.10 (n/a)</td><td>46.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.14 <b>(+35.95%)</b></td><td>0.82 (+3.34%)</td><td>0.72 (-6.84%)</td><td>0.68 (-7.20%)</td><td>0.19 <b>(+323.21%)</b></td><td>192.30 (+7.73%)</td><td>166.48 (+0.01%)</td><td>182.10 (+7.31%)</td><td>114.60 <b>(-26.44%)</b></td><td>31.46 <b>(+231.44%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.05 (n/a)</td><td>178.50 (n/a)</td><td>166.46 (n/a)</td><td>169.70 (n/a)</td><td>155.80 (n/a)</td><td>9.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.90 (-7.92%)</td><td>0.72 (-5.58%)</td><td>0.66 (-12.77%)</td><td>0.64 (+0.16%)</td><td>0.11 (-10.60%)</td><td>203.90 (-0.15%)</td><td>184.48 (+5.74%)</td><td>199.90 (+14.69%)</td><td>146.20 (+8.54%)</td><td>25.91 (+1.46%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.97 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.64 (n/a)</td><td>0.13 (n/a)</td><td>204.20 (n/a)</td><td>174.46 (n/a)</td><td>174.30 (n/a)</td><td>134.70 (n/a)</td><td>25.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.95 (+1.84%)</td><td>0.79 (-3.15%)</td><td>0.75 (-5.21%)</td><td>0.62 (-17.94%)</td><td>0.13 <b>(+83.80%)</b></td><td>211.70 <b>(+21.88%)</b></td><td>169.36 (+5.10%)</td><td>174.90 (+5.49%)</td><td>137.70 (-1.78%)</td><td>29.41 <b>(+117.48%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.93 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.75 (n/a)</td><td>0.07 (n/a)</td><td>173.70 (n/a)</td><td>161.14 (n/a)</td><td>165.80 (n/a)</td><td>140.20 (n/a)</td><td>13.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.80 (-13.19%)</td><td>0.62 (-17.36%)</td><td>0.64 (-14.83%)</td><td>0.41 <b>(-31.67%)</b></td><td>0.14 (+7.74%)</td><td>323.50 <b>(+46.31%)</b></td><td>222.52 <b>(+23.98%)</b></td><td>204.00 (+17.44%)</td><td>164.70 (+15.17%)</td><td>59.77 <b>(+89.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.92 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.59 (n/a)</td><td>0.13 (n/a)</td><td>221.10 (n/a)</td><td>179.48 (n/a)</td><td>173.70 (n/a)</td><td>143.00 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (-10.86%)</td><td>0.09 (-12.48%)</td><td>0.08 <b>(-26.25%)</b></td><td>0.08 (+11.43%)</td><td>0.01 <b>(-34.35%)</b></td><td>211.10 (-10.25%)</td><td>189.04 (+11.46%)</td><td>207.30 <b>(+35.58%)</b></td><td>148.70 (+12.23%)</td><td>29.13 <b>(-32.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:48:14</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.20 (n/a)</td><td>169.60 (n/a)</td><td>152.90 (n/a)</td><td>132.50 (n/a)</td><td>42.83 (n/a)</td>
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
