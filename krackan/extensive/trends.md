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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 <b>(+23.37%)</b></td><td>0.04 <b>(+23.98%)</b></td><td>0.04 <b>(+21.32%)</b></td><td>0.03 <b>(+47.20%)</b></td><td>0.01 (-8.43%)</td><td>204.40 <b>(-32.09%)</b></td><td>166.38 <b>(-21.01%)</b></td><td>152.40 (-17.58%)</td><td>144.80 (-18.97%)</td><td>25.68 <b>(-50.46%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>301.00 (n/a)</td><td>210.64 (n/a)</td><td>184.90 (n/a)</td><td>178.70 (n/a)</td><td>51.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (-9.60%)</td><td>0.04 (+9.94%)</td><td>0.04 (+17.32%)</td><td>0.03 <b>(+27.27%)</b></td><td>0.00 <b>(-58.85%)</b></td><td>183.10 <b>(-21.45%)</b></td><td>158.36 (-12.60%)</td><td>154.10 (-14.72%)</td><td>141.40 (+10.64%)</td><td>15.45 <b>(-63.88%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>181.18 (n/a)</td><td>180.70 (n/a)</td><td>127.80 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (+4.07%)</td><td>0.04 (+12.83%)</td><td>0.04 (+10.63%)</td><td>0.03 (+8.97%)</td><td>0.01 (+2.32%)</td><td>191.10 (-8.21%)</td><td>160.12 (-11.60%)</td><td>171.80 (-9.63%)</td><td>130.80 (-3.89%)</td><td>26.39 (-12.97%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>181.14 (n/a)</td><td>190.10 (n/a)</td><td>136.10 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 <b>(+48.66%)</b></td><td>0.04 <b>(+24.92%)</b></td><td>0.04 <b>(+21.30%)</b></td><td>0.04 (+15.46%)</td><td>0.01 <b>(+284.00%)</b></td><td>174.30 (-13.41%)</td><td>154.42 (-18.68%)</td><td>155.90 (-17.56%)</td><td>120.20 <b>(-32.74%)</b></td><td>21.64 <b>(+121.75%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.30 (n/a)</td><td>189.90 (n/a)</td><td>189.10 (n/a)</td><td>178.70 (n/a)</td><td>9.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+7.29%)</td><td>0.04 (+15.00%)</td><td>0.04 <b>(+21.77%)</b></td><td>0.03 (+13.68%)</td><td>0.00 (+7.21%)</td><td>204.10 (-12.03%)</td><td>177.18 (-13.07%)</td><td>169.60 (-17.87%)</td><td>153.40 (-6.80%)</td><td>23.18 (-9.75%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>232.00 (n/a)</td><td>203.82 (n/a)</td><td>206.50 (n/a)</td><td>164.60 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 <b>(+29.15%)</b></td><td>0.04 (+17.21%)</td><td>0.03 (+13.56%)</td><td>0.03 (+0.10%)</td><td>0.01 <b>(+204.19%)</b></td><td>212.70 (-0.09%)</td><td>173.88 (-12.96%)</td><td>178.70 (-11.93%)</td><td>139.50 <b>(-22.59%)</b></td><td>29.40 <b>(+134.25%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>199.78 (n/a)</td><td>202.90 (n/a)</td><td>180.20 (n/a)</td><td>12.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+1.48%)</td><td>0.03 (+5.20%)</td><td>0.04 (+11.39%)</td><td>0.03 (+5.06%)</td><td>0.01 (+14.08%)</td><td>228.40 (-4.83%)</td><td>186.06 (-4.64%)</td><td>171.70 (-10.25%)</td><td>160.50 (-1.47%)</td><td>29.86 (+4.64%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>240.00 (n/a)</td><td>195.12 (n/a)</td><td>191.30 (n/a)</td><td>162.90 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+17.44%)</td><td>0.03 (+14.20%)</td><td>0.03 (+9.87%)</td><td>0.03 (+7.50%)</td><td>0.01 <b>(+80.54%)</b></td><td>219.80 (-6.98%)</td><td>190.92 (-11.22%)</td><td>205.70 (-8.98%)</td><td>155.20 (-14.87%)</td><td>31.36 <b>(+41.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>215.04 (n/a)</td><td>226.00 (n/a)</td><td>182.30 (n/a)</td><td>22.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (-16.77%)</td><td>0.08 (-1.30%)</td><td>0.07 (+6.74%)</td><td>0.07 (+11.00%)</td><td>0.02 <b>(-43.06%)</b></td><td>182.80 (-9.91%)</td><td>165.62 (-3.17%)</td><td>175.70 (-6.34%)</td><td>119.10 <b>(+20.18%)</b></td><td>26.37 <b>(-38.39%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>202.90 (n/a)</td><td>171.04 (n/a)</td><td>187.60 (n/a)</td><td>99.10 (n/a)</td><td>42.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 <b>(+41.60%)</b></td><td>0.08 <b>(+30.10%)</b></td><td>0.08 <b>(+34.18%)</b></td><td>0.07 <b>(+32.22%)</b></td><td>0.01 <b>(+95.05%)</b></td><td>179.50 <b>(-24.39%)</b></td><td>155.30 <b>(-22.44%)</b></td><td>145.90 <b>(-25.45%)</b></td><td>126.70 <b>(-29.42%)</b></td><td>23.05 (+5.06%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>200.24 (n/a)</td><td>195.70 (n/a)</td><td>179.50 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (+15.89%)</td><td>0.08 (+11.57%)</td><td>0.09 <b>(+23.32%)</b></td><td>0.06 (-8.51%)</td><td>0.02 <b>(+84.35%)</b></td><td>204.10 (+9.26%)</td><td>155.70 (-7.97%)</td><td>143.70 (-18.95%)</td><td>119.20 (-13.69%)</td><td>35.03 <b>(+76.08%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>169.18 (n/a)</td><td>177.30 (n/a)</td><td>138.10 (n/a)</td><td>19.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 <b>(+32.53%)</b></td><td>0.07 (+10.35%)</td><td>0.07 (+4.19%)</td><td>0.04 (-10.67%)</td><td>0.02 <b>(+168.39%)</b></td><td>282.50 (+11.97%)</td><td>197.28 (-4.65%)</td><td>189.00 (-4.01%)</td><td>141.50 <b>(-24.53%)</b></td><td>56.75 <b>(+119.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>206.90 (n/a)</td><td>196.90 (n/a)</td><td>187.50 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (+14.05%)</td><td>0.08 (+5.89%)</td><td>0.07 (+7.42%)</td><td>0.06 (-6.62%)</td><td>0.01 <b>(+65.03%)</b></td><td>200.50 (+7.10%)</td><td>162.78 (-4.06%)</td><td>166.40 (-6.88%)</td><td>123.80 (-12.32%)</td><td>28.62 <b>(+54.19%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.20 (n/a)</td><td>169.66 (n/a)</td><td>178.70 (n/a)</td><td>141.20 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 <b>(+61.82%)</b></td><td>0.09 <b>(+22.82%)</b></td><td>0.08 (+19.87%)</td><td>0.05 (-1.81%)</td><td>0.04 <b>(+153.77%)</b></td><td>225.80 (+1.85%)</td><td>157.08 (-12.01%)</td><td>150.60 (-16.61%)</td><td>83.90 <b>(-38.17%)</b></td><td>52.02 <b>(+53.33%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>178.52 (n/a)</td><td>180.60 (n/a)</td><td>135.70 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (-5.06%)</td><td>0.07 (+0.64%)</td><td>0.07 (-5.25%)</td><td>0.06 (+13.62%)</td><td>0.01 (-16.91%)</td><td>198.20 (-11.99%)</td><td>174.38 (-1.76%)</td><td>188.90 (+5.53%)</td><td>131.60 (+5.36%)</td><td>28.61 (-19.60%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>225.20 (n/a)</td><td>177.50 (n/a)</td><td>179.00 (n/a)</td><td>124.90 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (-14.68%)</td><td>0.06 (-18.90%)</td><td>0.06 (-17.57%)</td><td>0.04 <b>(-32.24%)</b></td><td>0.02 (+5.07%)</td><td>332.10 <b>(+47.60%)</b></td><td>223.50 <b>(+27.00%)</b></td><td>219.30 <b>(+21.36%)</b></td><td>161.50 (+17.20%)</td><td>66.59 <b>(+88.20%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>175.98 (n/a)</td><td>180.70 (n/a)</td><td>137.80 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (-6.57%)</td><td>0.15 (-2.96%)</td><td>0.14 (-11.60%)</td><td>0.13 (+11.69%)</td><td>0.02 <b>(-33.92%)</b></td><td>185.90 (-10.45%)</td><td>166.34 (+1.60%)</td><td>172.80 (+13.16%)</td><td>144.90 (+7.02%)</td><td>18.56 <b>(-37.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>207.60 (n/a)</td><td>163.72 (n/a)</td><td>152.70 (n/a)</td><td>135.40 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (-5.15%)</td><td>0.15 (-2.46%)</td><td>0.14 (+1.02%)</td><td>0.13 (+3.18%)</td><td>0.01 <b>(-39.02%)</b></td><td>183.60 (-3.06%)</td><td>168.50 (+1.79%)</td><td>169.60 (-0.99%)</td><td>149.40 (+5.43%)</td><td>12.32 <b>(-37.82%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.40 (n/a)</td><td>165.54 (n/a)</td><td>171.30 (n/a)</td><td>141.70 (n/a)</td><td>19.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 <b>(+36.23%)</b></td><td>0.14 (+7.74%)</td><td>0.13 (-0.98%)</td><td>0.11 (-13.80%)</td><td>0.04 <b>(+205.38%)</b></td><td>233.60 (+16.05%)</td><td>179.78 (-2.54%)</td><td>186.00 (+0.98%)</td><td>116.70 <b>(-26.60%)</b></td><td>44.50 <b>(+151.78%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>184.46 (n/a)</td><td>184.20 (n/a)</td><td>159.00 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (+0.30%)</td><td>0.14 (+4.91%)</td><td>0.13 (+2.11%)</td><td>0.11 (+8.15%)</td><td>0.03 (+3.87%)</td><td>215.20 (-7.56%)</td><td>180.66 (-4.71%)</td><td>183.80 (-2.08%)</td><td>144.70 (-0.28%)</td><td>33.52 (-5.21%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.80 (n/a)</td><td>189.58 (n/a)</td><td>187.70 (n/a)</td><td>145.10 (n/a)</td><td>35.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (+5.23%)</td><td>0.14 (+0.72%)</td><td>0.12 (-9.51%)</td><td>0.11 (-0.88%)</td><td>0.03 <b>(+34.40%)</b></td><td>214.50 (+0.89%)</td><td>185.08 (+0.37%)</td><td>201.20 (+10.55%)</td><td>145.10 (-4.98%)</td><td>32.23 <b>(+27.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.60 (n/a)</td><td>184.40 (n/a)</td><td>182.00 (n/a)</td><td>152.70 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 <b>(+22.43%)</b></td><td>0.14 (+5.17%)</td><td>0.14 (+12.39%)</td><td>0.07 <b>(-40.84%)</b></td><td>0.05 <b>(+165.64%)</b></td><td>367.50 <b>(+69.04%)</b></td><td>202.58 (+6.48%)</td><td>173.00 (-11.05%)</td><td>126.00 (-18.29%)</td><td>94.47 <b>(+311.33%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.40 (n/a)</td><td>190.26 (n/a)</td><td>194.50 (n/a)</td><td>154.20 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (-5.26%)</td><td>0.14 (+17.61%)</td><td>0.14 <b>(+29.13%)</b></td><td>0.11 <b>(+20.18%)</b></td><td>0.02 <b>(-37.23%)</b></td><td>216.00 (-16.80%)</td><td>176.24 (-16.68%)</td><td>170.50 <b>(-22.57%)</b></td><td>159.00 (+5.51%)</td><td>23.01 <b>(-41.79%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>259.60 (n/a)</td><td>211.52 (n/a)</td><td>220.20 (n/a)</td><td>150.70 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 <b>(+32.98%)</b></td><td>0.13 <b>(+28.93%)</b></td><td>0.14 <b>(+34.17%)</b></td><td>0.08 (+15.21%)</td><td>0.04 <b>(+59.41%)</b></td><td>308.30 (-13.20%)</td><td>200.42 <b>(-20.16%)</b></td><td>172.10 <b>(-25.50%)</b></td><td>139.20 <b>(-24.84%)</b></td><td>66.75 (+3.93%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>355.20 (n/a)</td><td>251.04 (n/a)</td><td>231.00 (n/a)</td><td>185.20 (n/a)</td><td>64.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.38 (-8.85%)</td><td>0.34 (+9.55%)</td><td>0.34 <b>(+23.42%)</b></td><td>0.30 (+12.00%)</td><td>0.03 <b>(-53.96%)</b></td><td>165.50 (-10.73%)</td><td>146.50 (-10.70%)</td><td>144.80 (-19.02%)</td><td>130.00 (+9.70%)</td><td>12.66 <b>(-54.36%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>185.40 (n/a)</td><td>164.06 (n/a)</td><td>178.80 (n/a)</td><td>118.50 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.38 (-14.04%)</td><td>0.33 (+2.84%)</td><td>0.35 (+11.19%)</td><td>0.23 (-4.48%)</td><td>0.06 (-19.59%)</td><td>210.90 (+4.67%)</td><td>154.56 (-3.42%)</td><td>140.60 (-10.04%)</td><td>131.00 (+16.34%)</td><td>33.28 (-0.03%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>201.50 (n/a)</td><td>160.04 (n/a)</td><td>156.30 (n/a)</td><td>112.60 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.36 (+4.04%)</td><td>0.27 (-0.77%)</td><td>0.26 (-4.97%)</td><td>0.23 (+16.50%)</td><td>0.05 (-2.93%)</td><td>209.90 (-14.19%)</td><td>184.32 (+0.05%)</td><td>187.60 (+5.22%)</td><td>138.00 (-3.83%)</td><td>28.76 <b>(-22.90%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>244.60 (n/a)</td><td>184.22 (n/a)</td><td>178.30 (n/a)</td><td>143.50 (n/a)</td><td>37.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.32 <b>(-21.54%)</b></td><td>0.29 (-3.10%)</td><td>0.31 (+9.75%)</td><td>0.23 (-7.16%)</td><td>0.04 <b>(-45.47%)</b></td><td>210.10 (+7.69%)</td><td>170.70 (+1.37%)</td><td>159.50 (-8.86%)</td><td>151.60 <b>(+27.50%)</b></td><td>23.44 <b>(-22.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>195.10 (n/a)</td><td>168.40 (n/a)</td><td>175.00 (n/a)</td><td>118.90 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.31 (-16.49%)</td><td>0.28 (-2.97%)</td><td>0.29 (+10.69%)</td><td>0.22 (+6.14%)</td><td>0.03 <b>(-50.53%)</b></td><td>221.10 (-5.79%)</td><td>179.96 (-0.18%)</td><td>171.40 (-9.69%)</td><td>158.10 (+19.68%)</td><td>24.52 <b>(-41.61%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>234.70 (n/a)</td><td>180.28 (n/a)</td><td>189.80 (n/a)</td><td>132.10 (n/a)</td><td>42.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.32 (+4.97%)</td><td>0.28 (+0.06%)</td><td>0.27 (-6.92%)</td><td>0.25 (+5.05%)</td><td>0.03 (-7.51%)</td><td>196.10 (-4.81%)</td><td>178.54 (-0.27%)</td><td>182.90 (+7.46%)</td><td>154.20 (-4.76%)</td><td>15.78 (-16.91%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>206.00 (n/a)</td><td>179.02 (n/a)</td><td>170.20 (n/a)</td><td>161.90 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.33 (+6.45%)</td><td>0.27 (+6.61%)</td><td>0.27 (+12.99%)</td><td>0.21 (-4.27%)</td><td>0.06 <b>(+47.49%)</b></td><td>234.20 (+4.46%)</td><td>188.30 (-4.38%)</td><td>179.70 (-11.52%)</td><td>148.10 (-6.09%)</td><td>40.55 <b>(+44.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>224.20 (n/a)</td><td>196.92 (n/a)</td><td>203.10 (n/a)</td><td>157.70 (n/a)</td><td>28.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (-14.97%)</td><td>0.24 (-16.30%)</td><td>0.22 <b>(-21.46%)</b></td><td>0.20 (-10.09%)</td><td>0.04 (-19.57%)</td><td>242.50 (+11.19%)</td><td>209.72 (+19.06%)</td><td>222.20 <b>(+27.34%)</b></td><td>166.20 (+17.62%)</td><td>30.47 (+4.05%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>218.10 (n/a)</td><td>176.14 (n/a)</td><td>174.50 (n/a)</td><td>141.30 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (-13.54%)</td><td>0.02 (-5.64%)</td><td>0.02 (-2.87%)</td><td>0.02 (+3.43%)</td><td>0.00 <b>(-36.54%)</b></td><td>165.30 (-3.33%)</td><td>144.34 (+4.19%)</td><td>149.30 (+2.97%)</td><td>116.00 (+15.65%)</td><td>18.71 <b>(-28.41%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.00 (n/a)</td><td>138.54 (n/a)</td><td>145.00 (n/a)</td><td>100.30 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (-14.14%)</td><td>0.02 (-15.58%)</td><td>0.02 (-16.99%)</td><td>0.01 <b>(-23.35%)</b></td><td>0.00 <b>(+23.99%)</b></td><td>206.00 <b>(+30.46%)</b></td><td>161.40 <b>(+20.20%)</b></td><td>154.30 <b>(+20.45%)</b></td><td>134.20 (+16.49%)</td><td>30.29 <b>(+83.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>157.90 (n/a)</td><td>134.28 (n/a)</td><td>128.10 (n/a)</td><td>115.20 (n/a)</td><td>16.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (+13.25%)</td><td>0.02 (-3.58%)</td><td>0.02 (-8.62%)</td><td>0.01 (-5.04%)</td><td>0.00 <b>(+73.75%)</b></td><td>187.70 (+5.33%)</td><td>154.24 (+6.15%)</td><td>155.00 (+9.46%)</td><td>111.40 (-11.73%)</td><td>31.55 <b>(+59.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>178.20 (n/a)</td><td>145.30 (n/a)</td><td>141.60 (n/a)</td><td>126.20 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (-0.26%)</td><td>0.02 (+4.34%)</td><td>0.02 (+9.59%)</td><td>0.01 (+8.33%)</td><td>0.00 (-9.15%)</td><td>198.50 (-7.67%)</td><td>165.00 (-4.95%)</td><td>157.40 (-8.75%)</td><td>122.10 (+0.25%)</td><td>31.55 (-13.74%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.00 (n/a)</td><td>173.60 (n/a)</td><td>172.50 (n/a)</td><td>121.80 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (-9.93%)</td><td>0.02 (+0.32%)</td><td>0.02 (+4.92%)</td><td>0.01 <b>(+23.30%)</b></td><td>0.00 <b>(-52.75%)</b></td><td>182.00 (-18.89%)</td><td>161.84 (-2.92%)</td><td>157.20 (-4.73%)</td><td>144.10 (+11.02%)</td><td>14.93 <b>(-58.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>224.40 (n/a)</td><td>166.70 (n/a)</td><td>165.00 (n/a)</td><td>129.80 (n/a)</td><td>35.63 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (-4.75%)</td><td>0.01 (-4.96%)</td><td>0.02 (-8.75%)</td><td>0.01 (+2.58%)</td><td>0.00 (-17.86%)</td><td>203.00 (-2.50%)</td><td>179.00 (+4.78%)</td><td>172.50 (+9.59%)</td><td>159.10 (+5.02%)</td><td>20.58 (-14.99%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.20 (n/a)</td><td>170.84 (n/a)</td><td>157.40 (n/a)</td><td>151.50 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 <b>(-24.53%)</b></td><td>0.02 (-15.11%)</td><td>0.02 (-7.28%)</td><td>0.01 (-9.30%)</td><td>0.00 <b>(-50.11%)</b></td><td>208.40 (+10.26%)</td><td>174.76 (+14.49%)</td><td>165.00 (+7.84%)</td><td>144.30 <b>(+32.51%)</b></td><td>25.11 <b>(-28.27%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>152.64 (n/a)</td><td>153.00 (n/a)</td><td>108.90 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.01 (-11.59%)</td><td>0.01 (-16.88%)</td><td>0.01 (-17.54%)</td><td>0.01 (-16.73%)</td><td>0.00 (+7.63%)</td><td>368.40 <b>(+20.08%)</b></td><td>269.14 <b>(+22.60%)</b></td><td>249.40 <b>(+21.24%)</b></td><td>197.50 (+13.12%)</td><td>72.98 <b>(+40.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>306.80 (n/a)</td><td>219.52 (n/a)</td><td>205.70 (n/a)</td><td>174.60 (n/a)</td><td>51.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+3.55%)</td><td>0.03 (+4.72%)</td><td>0.03 <b>(+20.88%)</b></td><td>0.03 (-0.14%)</td><td>0.01 (-3.72%)</td><td>194.10 (+0.15%)</td><td>159.72 (-4.67%)</td><td>152.20 (-17.24%)</td><td>130.80 (-3.40%)</td><td>26.19 (-4.86%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>167.54 (n/a)</td><td>183.90 (n/a)</td><td>135.40 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (-4.19%)</td><td>0.03 (-1.94%)</td><td>0.04 (+10.51%)</td><td>0.02 (-10.64%)</td><td>0.01 <b>(+22.06%)</b></td><td>237.40 (+11.93%)</td><td>172.42 (+4.38%)</td><td>147.70 (-9.50%)</td><td>129.90 (+4.42%)</td><td>46.53 <b>(+43.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>165.18 (n/a)</td><td>163.20 (n/a)</td><td>124.40 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 <b>(+49.97%)</b></td><td>0.03 <b>(+44.09%)</b></td><td>0.04 <b>(+32.90%)</b></td><td>0.02 <b>(+59.11%)</b></td><td>0.01 <b>(+30.52%)</b></td><td>228.70 <b>(-37.17%)</b></td><td>162.26 <b>(-31.74%)</b></td><td>148.10 <b>(-24.75%)</b></td><td>126.70 <b>(-33.32%)</b></td><td>41.10 <b>(-44.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>364.00 (n/a)</td><td>237.72 (n/a)</td><td>196.80 (n/a)</td><td>190.00 (n/a)</td><td>74.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(-21.97%)</b></td><td>0.03 (-10.36%)</td><td>0.03 (-6.53%)</td><td>0.02 (-1.68%)</td><td>0.00 <b>(-42.52%)</b></td><td>221.50 (+1.70%)</td><td>174.82 (+9.24%)</td><td>163.00 (+6.96%)</td><td>157.70 <b>(+28.11%)</b></td><td>26.85 <b>(-25.83%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>160.04 (n/a)</td><td>152.40 (n/a)</td><td>123.10 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+8.09%)</td><td>0.03 (+7.39%)</td><td>0.03 (+9.65%)</td><td>0.02 (-6.31%)</td><td>0.01 <b>(+50.05%)</b></td><td>228.80 (+6.77%)</td><td>168.18 (-5.22%)</td><td>163.50 (-8.81%)</td><td>138.10 (-7.44%)</td><td>36.34 <b>(+48.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>177.44 (n/a)</td><td>179.30 (n/a)</td><td>149.20 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(-21.34%)</b></td><td>0.03 (-9.67%)</td><td>0.03 (-8.57%)</td><td>0.03 (+12.09%)</td><td>0.00 <b>(-62.11%)</b></td><td>192.40 (-10.80%)</td><td>176.28 (+7.61%)</td><td>174.10 (+9.36%)</td><td>161.30 <b>(+27.11%)</b></td><td>14.89 <b>(-57.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>163.82 (n/a)</td><td>159.20 (n/a)</td><td>126.90 (n/a)</td><td>34.65 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (-9.51%)</td><td>0.03 (-12.21%)</td><td>0.03 (-7.51%)</td><td>0.03 (+6.96%)</td><td>0.01 <b>(-28.96%)</b></td><td>208.00 (-6.52%)</td><td>176.24 (+11.76%)</td><td>166.40 (+8.12%)</td><td>138.60 (+10.53%)</td><td>29.12 <b>(-25.25%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>157.70 (n/a)</td><td>153.90 (n/a)</td><td>125.40 (n/a)</td><td>38.95 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+15.48%)</td><td>0.03 (+1.75%)</td><td>0.03 (-0.84%)</td><td>0.02 (-15.35%)</td><td>0.01 <b>(+76.18%)</b></td><td>275.70 (+18.12%)</td><td>200.74 (+1.23%)</td><td>182.10 (+0.83%)</td><td>153.10 (-13.36%)</td><td>49.00 <b>(+83.75%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.40 (n/a)</td><td>198.30 (n/a)</td><td>180.60 (n/a)</td><td>176.70 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (-12.89%)</td><td>0.07 (+5.99%)</td><td>0.07 (+5.92%)</td><td>0.06 <b>(+29.82%)</b></td><td>0.01 <b>(-54.85%)</b></td><td>175.20 <b>(-22.96%)</b></td><td>150.16 (-9.00%)</td><td>149.20 (-5.63%)</td><td>135.50 (+14.73%)</td><td>15.75 <b>(-60.47%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.40 (n/a)</td><td>165.02 (n/a)</td><td>158.10 (n/a)</td><td>118.10 (n/a)</td><td>39.85 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (-3.99%)</td><td>0.07 (+6.61%)</td><td>0.07 (+11.93%)</td><td>0.06 (+7.10%)</td><td>0.01 <b>(-35.88%)</b></td><td>167.60 (-6.63%)</td><td>151.68 (-7.00%)</td><td>148.40 (-10.66%)</td><td>134.50 (+4.10%)</td><td>12.88 <b>(-36.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>163.10 (n/a)</td><td>166.10 (n/a)</td><td>129.20 (n/a)</td><td>20.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (-9.85%)</td><td>0.07 (-3.72%)</td><td>0.07 (+0.53%)</td><td>0.06 (-6.72%)</td><td>0.01 <b>(-24.15%)</b></td><td>170.40 (+7.17%)</td><td>145.54 (+3.48%)</td><td>141.20 (-0.56%)</td><td>130.80 (+10.94%)</td><td>14.94 (-7.97%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>159.00 (n/a)</td><td>140.64 (n/a)</td><td>142.00 (n/a)</td><td>117.90 (n/a)</td><td>16.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (+10.16%)</td><td>0.08 (+12.90%)</td><td>0.07 (+15.95%)</td><td>0.07 (+17.40%)</td><td>0.01 <b>(-25.94%)</b></td><td>147.10 (-14.82%)</td><td>138.84 (-11.91%)</td><td>143.80 (-13.74%)</td><td>125.70 (-9.18%)</td><td>9.96 <b>(-41.90%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>157.62 (n/a)</td><td>166.70 (n/a)</td><td>138.40 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 <b>(+74.01%)</b></td><td>0.08 <b>(+44.13%)</b></td><td>0.08 <b>(+45.67%)</b></td><td>0.07 <b>(+27.28%)</b></td><td>0.02 <b>(+170.05%)</b></td><td>161.20 <b>(-21.44%)</b></td><td>130.64 <b>(-28.79%)</b></td><td>131.60 <b>(-31.35%)</b></td><td>89.40 <b>(-42.54%)</b></td><td>26.19 (+16.58%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>183.46 (n/a)</td><td>191.70 (n/a)</td><td>155.60 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 <b>(+23.72%)</b></td><td>0.07 (+19.52%)</td><td>0.07 (+18.89%)</td><td>0.05 <b>(+22.24%)</b></td><td>0.01 (+18.11%)</td><td>206.40 (-18.19%)</td><td>151.74 (-16.55%)</td><td>141.50 (-15.87%)</td><td>118.30 (-19.14%)</td><td>32.99 <b>(-21.31%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>181.84 (n/a)</td><td>168.20 (n/a)</td><td>146.30 (n/a)</td><td>41.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (-13.17%)</td><td>0.07 (-1.99%)</td><td>0.07 (+3.67%)</td><td>0.05 (-9.30%)</td><td>0.01 (-10.99%)</td><td>226.00 (+10.24%)</td><td>166.56 (+2.01%)</td><td>151.80 (-3.50%)</td><td>138.30 (+15.15%)</td><td>36.99 (+10.86%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>163.28 (n/a)</td><td>157.30 (n/a)</td><td>120.10 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (+17.89%)</td><td>0.06 (+8.89%)</td><td>0.06 (+17.15%)</td><td>0.05 (-3.60%)</td><td>0.01 <b>(+60.67%)</b></td><td>232.00 (+3.76%)</td><td>191.44 (-7.07%)</td><td>187.50 (-14.66%)</td><td>151.90 (-15.19%)</td><td>31.13 <b>(+40.89%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>206.00 (n/a)</td><td>219.70 (n/a)</td><td>179.10 (n/a)</td><td>22.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 <b>(+31.33%)</b></td><td>0.15 <b>(+28.06%)</b></td><td>0.14 (+15.07%)</td><td>0.11 <b>(+27.60%)</b></td><td>0.03 <b>(+20.27%)</b></td><td>183.80 <b>(-21.62%)</b></td><td>144.40 <b>(-22.21%)</b></td><td>146.90 (-13.08%)</td><td>117.00 <b>(-23.88%)</b></td><td>25.80 <b>(-27.92%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>234.50 (n/a)</td><td>185.62 (n/a)</td><td>169.00 (n/a)</td><td>153.70 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (+4.30%)</td><td>0.14 (+16.61%)</td><td>0.13 (+10.57%)</td><td>0.12 <b>(+23.76%)</b></td><td>0.02 (-11.19%)</td><td>178.10 (-19.19%)</td><td>154.06 (-15.07%)</td><td>164.20 (-9.53%)</td><td>128.00 (-4.12%)</td><td>21.90 <b>(-29.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>220.40 (n/a)</td><td>181.40 (n/a)</td><td>181.50 (n/a)</td><td>133.50 (n/a)</td><td>31.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (+1.64%)</td><td>0.13 (-10.34%)</td><td>0.13 (-10.77%)</td><td>0.11 (-15.66%)</td><td>0.02 <b>(+67.58%)</b></td><td>196.80 (+18.55%)</td><td>169.42 (+13.52%)</td><td>167.90 (+12.08%)</td><td>125.60 (-1.64%)</td><td>28.50 <b>(+96.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>166.00 (n/a)</td><td>149.24 (n/a)</td><td>149.80 (n/a)</td><td>127.70 (n/a)</td><td>14.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (-3.54%)</td><td>0.12 (-18.68%)</td><td>0.11 <b>(-23.43%)</b></td><td>0.08 <b>(-34.02%)</b></td><td>0.03 <b>(+44.98%)</b></td><td>274.40 <b>(+51.60%)</b></td><td>189.98 <b>(+28.61%)</b></td><td>190.60 <b>(+30.64%)</b></td><td>128.50 (+3.71%)</td><td>55.34 <b>(+131.88%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>181.00 (n/a)</td><td>147.72 (n/a)</td><td>145.90 (n/a)</td><td>123.90 (n/a)</td><td>23.87 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (+0.09%)</td><td>0.13 (-4.92%)</td><td>0.13 (-8.59%)</td><td>0.10 <b>(-20.63%)</b></td><td>0.02 <b>(+87.29%)</b></td><td>204.40 <b>(+25.94%)</b></td><td>161.12 (+7.43%)</td><td>167.30 (+9.42%)</td><td>128.30 (-0.08%)</td><td>30.24 <b>(+136.70%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>162.30 (n/a)</td><td>149.98 (n/a)</td><td>152.90 (n/a)</td><td>128.40 (n/a)</td><td>12.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (+10.06%)</td><td>0.12 (-1.04%)</td><td>0.12 (-5.57%)</td><td>0.10 (+2.59%)</td><td>0.02 <b>(+23.15%)</b></td><td>206.00 (-2.55%)</td><td>171.48 (+1.46%)</td><td>170.60 (+5.90%)</td><td>138.60 (-9.17%)</td><td>25.71 (+6.60%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.40 (n/a)</td><td>169.02 (n/a)</td><td>161.10 (n/a)</td><td>152.60 (n/a)</td><td>24.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (+14.38%)</td><td>0.13 (+3.60%)</td><td>0.13 (+9.15%)</td><td>0.11 (+2.66%)</td><td>0.03 <b>(+23.06%)</b></td><td>182.70 (-2.56%)</td><td>161.68 (-3.00%)</td><td>167.00 (-8.39%)</td><td>119.40 (-12.59%)</td><td>25.79 (+3.49%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>187.50 (n/a)</td><td>166.68 (n/a)</td><td>182.30 (n/a)</td><td>136.60 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (+10.23%)</td><td>0.11 (+1.78%)</td><td>0.10 (-5.54%)</td><td>0.09 (+11.49%)</td><td>0.02 <b>(+20.06%)</b></td><td>236.00 (-10.33%)</td><td>199.24 (-1.46%)</td><td>204.10 (+5.86%)</td><td>152.10 (-9.30%)</td><td>33.94 (-5.85%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>263.20 (n/a)</td><td>202.20 (n/a)</td><td>192.80 (n/a)</td><td>167.70 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.20 (n/a)</td><td>169.04 (n/a)</td><td>170.40 (n/a)</td><td>154.40 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.80 (n/a)</td><td>166.74 (n/a)</td><td>161.30 (n/a)</td><td>157.00 (n/a)</td><td>11.15 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>226.10 (n/a)</td><td>186.66 (n/a)</td><td>171.70 (n/a)</td><td>161.00 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>279.60 (n/a)</td><td>221.54 (n/a)</td><td>223.30 (n/a)</td><td>178.70 (n/a)</td><td>37.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.00 (n/a)</td><td>186.26 (n/a)</td><td>195.40 (n/a)</td><td>143.60 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>189.34 (n/a)</td><td>181.20 (n/a)</td><td>138.70 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>177.12 (n/a)</td><td>166.40 (n/a)</td><td>157.70 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>210.20 (n/a)</td><td>187.02 (n/a)</td><td>187.80 (n/a)</td><td>172.50 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>231.80 (n/a)</td><td>194.64 (n/a)</td><td>212.10 (n/a)</td><td>142.30 (n/a)</td><td>39.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>225.70 (n/a)</td><td>189.58 (n/a)</td><td>179.40 (n/a)</td><td>163.70 (n/a)</td><td>26.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>263.30 (n/a)</td><td>209.88 (n/a)</td><td>213.40 (n/a)</td><td>148.40 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>229.70 (n/a)</td><td>205.48 (n/a)</td><td>206.30 (n/a)</td><td>173.90 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.31 (-18.45%)</td><td>0.27 (-13.52%)</td><td>0.26 (-16.00%)</td><td>0.24 (-3.94%)</td><td>0.03 <b>(-43.77%)</b></td><td>208.80 (+4.09%)</td><td>183.96 (+14.26%)</td><td>187.20 (+19.01%)</td><td>158.50 <b>(+22.68%)</b></td><td>18.35 <b>(-29.36%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>200.60 (n/a)</td><td>161.00 (n/a)</td><td>157.30 (n/a)</td><td>129.20 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>237.80 (n/a)</td><td>191.16 (n/a)</td><td>196.60 (n/a)</td><td>149.80 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>221.50 (n/a)</td><td>193.32 (n/a)</td><td>186.90 (n/a)</td><td>177.10 (n/a)</td><td>18.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>224.30 (n/a)</td><td>196.78 (n/a)</td><td>207.70 (n/a)</td><td>149.80 (n/a)</td><td>29.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>225.70 (n/a)</td><td>194.08 (n/a)</td><td>186.90 (n/a)</td><td>171.20 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>170.86 (n/a)</td><td>172.00 (n/a)</td><td>145.30 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>183.46 (n/a)</td><td>189.70 (n/a)</td><td>142.70 (n/a)</td><td>24.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.70 (n/a)</td><td>205.34 (n/a)</td><td>202.90 (n/a)</td><td>176.50 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>172.06 (n/a)</td><td>154.60 (n/a)</td><td>141.90 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>173.66 (n/a)</td><td>164.00 (n/a)</td><td>132.20 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>219.10 (n/a)</td><td>172.92 (n/a)</td><td>180.70 (n/a)</td><td>120.20 (n/a)</td><td>37.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>181.32 (n/a)</td><td>176.70 (n/a)</td><td>157.40 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.10 (n/a)</td><td>153.32 (n/a)</td><td>150.30 (n/a)</td><td>141.90 (n/a)</td><td>16.14 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>173.92 (n/a)</td><td>163.20 (n/a)</td><td>147.40 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>252.70 (n/a)</td><td>184.86 (n/a)</td><td>169.80 (n/a)</td><td>156.30 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>229.10 (n/a)</td><td>199.30 (n/a)</td><td>214.40 (n/a)</td><td>160.60 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>219.10 (n/a)</td><td>184.30 (n/a)</td><td>178.50 (n/a)</td><td>157.90 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>207.90 (n/a)</td><td>170.14 (n/a)</td><td>178.00 (n/a)</td><td>138.50 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>312.50 (n/a)</td><td>215.56 (n/a)</td><td>214.40 (n/a)</td><td>155.30 (n/a)</td><td>61.14 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.10 (n/a)</td><td>148.78 (n/a)</td><td>145.70 (n/a)</td><td>127.50 (n/a)</td><td>18.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>263.20 (n/a)</td><td>183.70 (n/a)</td><td>173.70 (n/a)</td><td>147.70 (n/a)</td><td>46.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.90 (n/a)</td><td>161.04 (n/a)</td><td>163.80 (n/a)</td><td>127.60 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.40 (n/a)</td><td>166.48 (n/a)</td><td>166.00 (n/a)</td><td>126.80 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.60 (n/a)</td><td>165.52 (n/a)</td><td>159.90 (n/a)</td><td>129.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.00 (n/a)</td><td>177.60 (n/a)</td><td>156.60 (n/a)</td><td>154.00 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>169.84 (n/a)</td><td>170.90 (n/a)</td><td>122.90 (n/a)</td><td>45.62 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.30 (n/a)</td><td>190.50 (n/a)</td><td>188.10 (n/a)</td><td>169.50 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>157.34 (n/a)</td><td>148.60 (n/a)</td><td>128.30 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>342.10 (n/a)</td><td>198.08 (n/a)</td><td>175.40 (n/a)</td><td>128.80 (n/a)</td><td>83.54 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>269.60 (n/a)</td><td>178.88 (n/a)</td><td>170.80 (n/a)</td><td>125.40 (n/a)</td><td>57.63 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>173.06 (n/a)</td><td>178.30 (n/a)</td><td>122.00 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>359.40 (n/a)</td><td>214.66 (n/a)</td><td>179.70 (n/a)</td><td>161.40 (n/a)</td><td>82.87 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.10 (n/a)</td><td>222.64 (n/a)</td><td>210.60 (n/a)</td><td>172.10 (n/a)</td><td>40.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>166.84 (n/a)</td><td>160.90 (n/a)</td><td>152.10 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.30 (n/a)</td><td>229.08 (n/a)</td><td>219.90 (n/a)</td><td>185.10 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>162.76 (n/a)</td><td>156.50 (n/a)</td><td>127.80 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.90 (n/a)</td><td>171.90 (n/a)</td><td>171.40 (n/a)</td><td>140.70 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.10 (n/a)</td><td>164.26 (n/a)</td><td>167.90 (n/a)</td><td>128.80 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>179.80 (n/a)</td><td>156.20 (n/a)</td><td>162.00 (n/a)</td><td>121.40 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.70 (n/a)</td><td>168.30 (n/a)</td><td>166.00 (n/a)</td><td>136.50 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>183.16 (n/a)</td><td>176.40 (n/a)</td><td>150.90 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>188.14 (n/a)</td><td>174.40 (n/a)</td><td>169.40 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>189.58 (n/a)</td><td>192.40 (n/a)</td><td>145.50 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>189.10 (n/a)</td><td>162.12 (n/a)</td><td>161.90 (n/a)</td><td>125.30 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.00 (n/a)</td><td>172.98 (n/a)</td><td>167.80 (n/a)</td><td>136.50 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.10 (n/a)</td><td>167.82 (n/a)</td><td>154.60 (n/a)</td><td>147.20 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>175.70 (n/a)</td><td>153.82 (n/a)</td><td>150.40 (n/a)</td><td>137.00 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.20 (n/a)</td><td>169.70 (n/a)</td><td>170.60 (n/a)</td><td>126.90 (n/a)</td><td>29.44 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>293.50 (n/a)</td><td>206.58 (n/a)</td><td>191.60 (n/a)</td><td>148.30 (n/a)</td><td>54.11 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.30 (n/a)</td><td>208.42 (n/a)</td><td>215.60 (n/a)</td><td>161.00 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>4.92 (+17.91%)</td><td>4.30 (+8.30%)</td><td>4.32 (+6.29%)</td><td>3.47 (+0.44%)</td><td>0.58 <b>(+95.59%)</b></td><td>2711.50 (-0.44%)</td><td>2219.16 (-6.68%)</td><td>2177.00 (-5.91%)</td><td>1910.00 (-15.19%)</td><td>318.90 <b>(+63.21%)</b></td><td>1936.80 (+17.91%)</td><td>1693.06 (+8.30%)</td><td>1699.31 (+6.29%)</td><td>1364.33 (+0.44%)</td><td>227.88 <b>(+95.59%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>4.18 (n/a)</td><td>3.97 (n/a)</td><td>4.06 (n/a)</td><td>3.45 (n/a)</td><td>0.30 (n/a)</td><td>2723.50 (n/a)</td><td>2378.08 (n/a)</td><td>2313.80 (n/a)</td><td>2252.10 (n/a)</td><td>195.40 (n/a)</td><td>1642.67 (n/a)</td><td>1563.27 (n/a)</td><td>1598.81 (n/a)</td><td>1358.30 (n/a)</td><td>116.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.21 (+8.46%)</td><td>1.10 (+16.92%)</td><td>1.07 (+8.43%)</td><td>1.00 <b>(+36.40%)</b></td><td>0.09 <b>(-38.35%)</b></td><td>220.50 <b>(-26.70%)</b></td><td>201.72 (-15.90%)</td><td>206.70 (-7.76%)</td><td>182.20 (-7.79%)</td><td>16.98 <b>(-59.12%)</b></td><td>51.79 (+8.46%)</td><td>47.06 (+16.92%)</td><td>45.65 (+8.43%)</td><td>42.80 <b>(+36.40%)</b></td><td>4.03 <b>(-38.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.12 (n/a)</td><td>0.94 (n/a)</td><td>0.99 (n/a)</td><td>0.74 (n/a)</td><td>0.15 (n/a)</td><td>300.80 (n/a)</td><td>239.86 (n/a)</td><td>224.10 (n/a)</td><td>197.60 (n/a)</td><td>41.55 (n/a)</td><td>47.75 (n/a)</td><td>40.24 (n/a)</td><td>42.10 (n/a)</td><td>31.38 (n/a)</td><td>6.54 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.22 (+7.20%)</td><td>1.10 (+15.18%)</td><td>1.11 (+14.44%)</td><td>0.98 <b>(+25.56%)</b></td><td>0.12 (-13.83%)</td><td>225.60 <b>(-20.37%)</b></td><td>202.62 (-13.80%)</td><td>199.80 (-12.64%)</td><td>181.60 (-6.68%)</td><td>21.49 <b>(-36.39%)</b></td><td>51.98 (+7.20%)</td><td>47.00 (+15.18%)</td><td>47.22 (+14.44%)</td><td>41.83 <b>(+25.56%)</b></td><td>4.96 (-13.83%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.14 (n/a)</td><td>0.96 (n/a)</td><td>0.97 (n/a)</td><td>0.78 (n/a)</td><td>0.13 (n/a)</td><td>283.30 (n/a)</td><td>235.06 (n/a)</td><td>228.70 (n/a)</td><td>194.60 (n/a)</td><td>33.79 (n/a)</td><td>48.49 (n/a)</td><td>40.80 (n/a)</td><td>41.26 (n/a)</td><td>33.31 (n/a)</td><td>5.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.52 (-0.06%)</td><td>0.52 (-0.08%)</td><td>0.52 (-0.18%)</td><td>0.52 (+0.01%)</td><td>0.00 (-13.75%)</td><td>48771.00 (-0.01%)</td><td>48709.56 (+0.08%)</td><td>48735.50 (+0.18%)</td><td>48645.90 (+0.06%)</td><td>55.21 (-13.76%)</td><td>353.16 (-0.06%)</td><td>352.70 (-0.08%)</td><td>352.51 (-0.18%)</td><td>352.26 (+0.01%)</td><td>0.40 (-13.75%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48777.00 (n/a)</td><td>48669.12 (n/a)</td><td>48650.20 (n/a)</td><td>48617.90 (n/a)</td><td>64.02 (n/a)</td><td>353.36 (n/a)</td><td>352.99 (n/a)</td><td>353.13 (n/a)</td><td>352.21 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (+1.43%)</td><td>0.21 (+0.06%)</td><td>0.21 (-0.53%)</td><td>0.21 (-0.38%)</td><td>0.00 <b>(+103.97%)</b></td><td>119956.70 (+0.38%)</td><td>117809.10 (-0.04%)</td><td>118217.80 (+0.53%)</td><td>115259.70 (-1.41%)</td><td>2009.89 <b>(+101.56%)</b></td><td>149.05 (+1.43%)</td><td>145.86 (+0.06%)</td><td>145.32 (-0.53%)</td><td>143.22 (-0.38%)</td><td>2.50 <b>(+103.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119505.60 (n/a)</td><td>117860.22 (n/a)</td><td>117596.90 (n/a)</td><td>116907.50 (n/a)</td><td>997.15 (n/a)</td><td>146.95 (n/a)</td><td>145.77 (n/a)</td><td>146.09 (n/a)</td><td>143.76 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.90 (-0.53%)</td><td>0.89 (+0.12%)</td><td>0.89 (+0.34%)</td><td>0.87 (-0.18%)</td><td>0.01 (-14.87%)</td><td>28791.50 (+0.18%)</td><td>28381.98 (-0.12%)</td><td>28330.20 (-0.33%)</td><td>28087.40 (+0.53%)</td><td>257.41 (-14.01%)</td><td>611.66 (-0.53%)</td><td>605.35 (+0.12%)</td><td>606.41 (+0.34%)</td><td>596.70 (-0.18%)</td><td>5.46 (-14.87%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28739.60 (n/a)</td><td>28417.02 (n/a)</td><td>28425.30 (n/a)</td><td>27939.90 (n/a)</td><td>299.33 (n/a)</td><td>614.89 (n/a)</td><td>604.62 (n/a)</td><td>604.39 (n/a)</td><td>597.78 (n/a)</td><td>6.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>3.53 (+0.21%)</td><td>3.38 (-0.99%)</td><td>3.33 (-0.80%)</td><td>3.25 (-2.11%)</td><td>0.12 (+16.19%)</td><td>7735.30 (+2.16%)</td><td>7453.58 (+1.02%)</td><td>7554.10 (+0.81%)</td><td>7122.90 (-0.20%)</td><td>259.78 (+18.55%)</td><td>2411.93 (+0.21%)</td><td>2307.18 (-0.99%)</td><td>2274.26 (-0.80%)</td><td>2220.97 (-2.11%)</td><td>81.19 (+16.19%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.53 (n/a)</td><td>3.41 (n/a)</td><td>3.36 (n/a)</td><td>3.32 (n/a)</td><td>0.10 (n/a)</td><td>7572.10 (n/a)</td><td>7378.00 (n/a)</td><td>7493.60 (n/a)</td><td>7137.50 (n/a)</td><td>219.13 (n/a)</td><td>2406.98 (n/a)</td><td>2330.18 (n/a)</td><td>2292.60 (n/a)</td><td>2268.83 (n/a)</td><td>69.88 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>2.86 (-11.85%)</td><td>2.82 (-4.77%)</td><td>2.83 (-2.00%)</td><td>2.77 (+3.90%)</td><td>0.04 <b>(-83.00%)</b></td><td>9091.00 (-3.75%)</td><td>8919.30 (+4.45%)</td><td>8895.80 (+2.05%)</td><td>8789.20 (+13.44%)</td><td>133.51 <b>(-81.24%)</b></td><td>1954.67 (-11.85%)</td><td>1926.49 (-4.77%)</td><td>1931.23 (-2.00%)</td><td>1889.76 (+3.90%)</td><td>28.74 <b>(-83.00%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.25 (n/a)</td><td>2.96 (n/a)</td><td>2.89 (n/a)</td><td>2.66 (n/a)</td><td>0.25 (n/a)</td><td>9445.20 (n/a)</td><td>8539.50 (n/a)</td><td>8717.50 (n/a)</td><td>7747.80 (n/a)</td><td>711.65 (n/a)</td><td>2217.38 (n/a)</td><td>2023.07 (n/a)</td><td>1970.74 (n/a)</td><td>1818.89 (n/a)</td><td>169.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>3.29 (-1.30%)</td><td>3.19 (-1.32%)</td><td>3.17 (-3.40%)</td><td>3.12 (+0.86%)</td><td>0.06 <b>(-41.51%)</b></td><td>8056.60 (-0.86%)</td><td>7898.20 (+1.27%)</td><td>7946.90 (+3.52%)</td><td>7648.10 (+1.32%)</td><td>152.24 <b>(-41.56%)</b></td><td>2246.29 (-1.30%)</td><td>2175.82 (-1.32%)</td><td>2161.85 (-3.40%)</td><td>2132.39 (+0.86%)</td><td>42.62 <b>(-41.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.33 (n/a)</td><td>3.23 (n/a)</td><td>3.28 (n/a)</td><td>3.10 (n/a)</td><td>0.11 (n/a)</td><td>8126.20 (n/a)</td><td>7798.84 (n/a)</td><td>7676.90 (n/a)</td><td>7548.60 (n/a)</td><td>260.52 (n/a)</td><td>2275.90 (n/a)</td><td>2204.82 (n/a)</td><td>2237.86 (n/a)</td><td>2114.14 (n/a)</td><td>72.86 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.78 (-0.00%)</td><td>0.78 (-0.03%)</td><td>0.78 (+0.00%)</td><td>0.78 (-0.19%)</td><td>0.00 <b>(+312.19%)</b></td><td>96679.30 (+0.19%)</td><td>96500.66 (+0.03%)</td><td>96453.90 (-0.00%)</td><td>96445.00 (+0.00%)</td><td>100.44 <b>(+312.75%)</b></td><td>712.53 (-0.00%)</td><td>712.11 (-0.03%)</td><td>712.46 (+0.00%)</td><td>710.80 (-0.19%)</td><td>0.74 <b>(+312.14%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96499.60 (n/a)</td><td>96468.02 (n/a)</td><td>96458.50 (n/a)</td><td>96440.30 (n/a)</td><td>24.33 (n/a)</td><td>712.56 (n/a)</td><td>712.35 (n/a)</td><td>712.42 (n/a)</td><td>712.12 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.73 (+0.03%)</td><td>0.73 (-0.06%)</td><td>0.73 (+0.01%)</td><td>0.73 (-0.22%)</td><td>0.00 <b>(+549.41%)</b></td><td>103925.40 (+0.22%)</td><td>103726.50 (+0.06%)</td><td>103642.30 (-0.01%)</td><td>103615.60 (-0.03%)</td><td>134.79 <b>(+550.14%)</b></td><td>663.22 (+0.03%)</td><td>662.51 (-0.06%)</td><td>663.04 (+0.01%)</td><td>661.24 (-0.22%)</td><td>0.86 <b>(+549.26%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103692.70 (n/a)</td><td>103665.12 (n/a)</td><td>103657.50 (n/a)</td><td>103642.70 (n/a)</td><td>20.73 (n/a)</td><td>663.04 (n/a)</td><td>662.90 (n/a)</td><td>662.95 (n/a)</td><td>662.72 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.70 (-0.02%)</td><td>0.69 (-0.01%)</td><td>0.69 (-0.03%)</td><td>0.69 (-0.08%)</td><td>0.00 <b>(+22.34%)</b></td><td>108895.10 (+0.08%)</td><td>108698.66 (+0.01%)</td><td>108753.60 (+0.03%)</td><td>108450.20 (+0.02%)</td><td>179.56 <b>(+22.50%)</b></td><td>633.65 (-0.02%)</td><td>632.20 (-0.01%)</td><td>631.88 (-0.03%)</td><td>631.06 (-0.08%)</td><td>1.04 <b>(+22.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108803.80 (n/a)</td><td>108683.32 (n/a)</td><td>108723.00 (n/a)</td><td>108432.10 (n/a)</td><td>146.58 (n/a)</td><td>633.76 (n/a)</td><td>632.29 (n/a)</td><td>632.06 (n/a)</td><td>631.59 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.56 (+3.11%)</td><td>6.90 (+0.72%)</td><td>7.07 (-0.37%)</td><td>6.23 (-0.94%)</td><td>0.53 (+10.20%)</td><td>1429.90 (+0.95%)</td><td>1298.46 (-0.64%)</td><td>1260.20 (+0.37%)</td><td>1179.30 (-3.03%)</td><td>100.17 (+7.64%)</td><td>455.23 (+3.11%)</td><td>415.43 (+0.72%)</td><td>426.03 (-0.37%)</td><td>375.47 (-0.94%)</td><td>31.70 (+10.20%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.33 (n/a)</td><td>6.85 (n/a)</td><td>7.10 (n/a)</td><td>6.29 (n/a)</td><td>0.48 (n/a)</td><td>1416.50 (n/a)</td><td>1306.82 (n/a)</td><td>1255.50 (n/a)</td><td>1216.10 (n/a)</td><td>93.06 (n/a)</td><td>441.49 (n/a)</td><td>412.47 (n/a)</td><td>427.61 (n/a)</td><td>379.01 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.04 (+3.52%)</td><td>6.40 (-1.84%)</td><td>6.82 (+5.26%)</td><td>4.58 <b>(-26.17%)</b></td><td>1.03 <b>(+367.99%)</b></td><td>1946.00 <b>(+35.45%)</b></td><td>1430.68 (+4.50%)</td><td>1307.20 (-4.99%)</td><td>1266.90 (-3.39%)</td><td>289.90 <b>(+522.83%)</b></td><td>423.78 (+3.52%)</td><td>385.29 (-1.84%)</td><td>410.71 (+5.26%)</td><td>275.88 <b>(-26.17%)</b></td><td>62.00 <b>(+367.99%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.80 (n/a)</td><td>6.52 (n/a)</td><td>6.48 (n/a)</td><td>6.20 (n/a)</td><td>0.22 (n/a)</td><td>1436.70 (n/a)</td><td>1369.02 (n/a)</td><td>1375.90 (n/a)</td><td>1311.40 (n/a)</td><td>46.55 (n/a)</td><td>409.39 (n/a)</td><td>392.52 (n/a)</td><td>390.19 (n/a)</td><td>373.68 (n/a)</td><td>13.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.04 (-0.62%)</td><td>6.25 (-3.09%)</td><td>6.58 (+1.34%)</td><td>4.78 (-10.49%)</td><td>0.90 <b>(+29.23%)</b></td><td>1862.70 (+11.72%)</td><td>1452.64 (+4.13%)</td><td>1354.10 (-1.33%)</td><td>1266.00 (+0.63%)</td><td>241.82 <b>(+46.93%)</b></td><td>424.08 (-0.62%)</td><td>376.77 (-3.09%)</td><td>396.47 (+1.34%)</td><td>288.22 (-10.49%)</td><td>54.18 <b>(+29.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.08 (n/a)</td><td>6.45 (n/a)</td><td>6.49 (n/a)</td><td>5.35 (n/a)</td><td>0.70 (n/a)</td><td>1667.30 (n/a)</td><td>1394.98 (n/a)</td><td>1372.30 (n/a)</td><td>1258.10 (n/a)</td><td>164.58 (n/a)</td><td>426.73 (n/a)</td><td>388.80 (n/a)</td><td>391.22 (n/a)</td><td>322.00 (n/a)</td><td>41.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.17 (-0.68%)</td><td>7.62 (+2.02%)</td><td>7.39 (+1.57%)</td><td>7.23 (+1.79%)</td><td>0.44 (-1.83%)</td><td>4821.50 (-1.75%)</td><td>4586.20 (-1.99%)</td><td>4714.80 (-1.55%)</td><td>4265.00 (+0.68%)</td><td>257.47 (-1.92%)</td><td>503.51 (-0.68%)</td><td>469.46 (+2.02%)</td><td>455.48 (+1.57%)</td><td>445.40 (+1.79%)</td><td>26.89 (-1.83%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.23 (n/a)</td><td>7.47 (n/a)</td><td>7.28 (n/a)</td><td>7.10 (n/a)</td><td>0.44 (n/a)</td><td>4907.60 (n/a)</td><td>4679.26 (n/a)</td><td>4788.90 (n/a)</td><td>4236.00 (n/a)</td><td>262.51 (n/a)</td><td>506.96 (n/a)</td><td>460.17 (n/a)</td><td>448.43 (n/a)</td><td>437.58 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.86 (+3.67%)</td><td>7.56 (+3.52%)</td><td>7.57 (+2.17%)</td><td>7.33 (+5.22%)</td><td>0.20 <b>(-32.17%)</b></td><td>4758.50 (-4.96%)</td><td>4613.84 (-3.47%)</td><td>4607.60 (-2.12%)</td><td>4436.20 (-3.54%)</td><td>119.65 <b>(-38.02%)</b></td><td>484.08 (+3.67%)</td><td>465.70 (+3.52%)</td><td>466.08 (+2.17%)</td><td>451.29 (+5.22%)</td><td>12.19 <b>(-32.17%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.58 (n/a)</td><td>7.30 (n/a)</td><td>7.41 (n/a)</td><td>6.96 (n/a)</td><td>0.29 (n/a)</td><td>5007.10 (n/a)</td><td>4779.84 (n/a)</td><td>4707.30 (n/a)</td><td>4599.00 (n/a)</td><td>193.04 (n/a)</td><td>466.95 (n/a)</td><td>449.86 (n/a)</td><td>456.20 (n/a)</td><td>428.89 (n/a)</td><td>17.98 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.38 (-0.76%)</td><td>7.17 (-1.21%)</td><td>7.34 (+0.57%)</td><td>6.79 (-1.49%)</td><td>0.28 <b>(+34.90%)</b></td><td>5131.40 (+1.52%)</td><td>4871.06 (+1.28%)</td><td>4748.20 (-0.56%)</td><td>4722.70 (+0.76%)</td><td>193.42 <b>(+36.35%)</b></td><td>454.72 (-0.76%)</td><td>441.41 (-1.21%)</td><td>452.28 (+0.57%)</td><td>418.50 (-1.49%)</td><td>17.22 <b>(+34.90%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>7.44 (n/a)</td><td>7.25 (n/a)</td><td>7.30 (n/a)</td><td>6.90 (n/a)</td><td>0.21 (n/a)</td><td>5054.80 (n/a)</td><td>4809.56 (n/a)</td><td>4775.00 (n/a)</td><td>4687.00 (n/a)</td><td>141.86 (n/a)</td><td>458.18 (n/a)</td><td>446.80 (n/a)</td><td>449.73 (n/a)</td><td>424.84 (n/a)</td><td>12.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.79 (+0.39%)</td><td>0.79 (+0.05%)</td><td>0.79 (-0.12%)</td><td>0.79 (-0.01%)</td><td>0.00 <b>(+187.92%)</b></td><td>95902.40 (+0.01%)</td><td>95747.94 (-0.04%)</td><td>95858.10 (+0.12%)</td><td>95348.40 (-0.39%)</td><td>232.61 <b>(+186.81%)</b></td><td>720.72 (+0.39%)</td><td>717.72 (+0.05%)</td><td>716.89 (-0.12%)</td><td>716.56 (-0.01%)</td><td>1.75 <b>(+187.90%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95892.10 (n/a)</td><td>95791.00 (n/a)</td><td>95738.60 (n/a)</td><td>95721.40 (n/a)</td><td>81.10 (n/a)</td><td>717.91 (n/a)</td><td>717.39 (n/a)</td><td>717.78 (n/a)</td><td>716.63 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.73 (+0.01%)</td><td>0.73 (+0.06%)</td><td>0.73 (+0.01%)</td><td>0.73 (+0.22%)</td><td>0.00 <b>(-83.10%)</b></td><td>102937.80 (-0.22%)</td><td>102918.70 (-0.06%)</td><td>102914.70 (-0.01%)</td><td>102900.00 (-0.01%)</td><td>18.23 <b>(-83.18%)</b></td><td>667.83 (+0.01%)</td><td>667.71 (+0.06%)</td><td>667.73 (+0.01%)</td><td>667.58 (+0.22%)</td><td>0.12 <b>(-83.11%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103167.00 (n/a)</td><td>102980.30 (n/a)</td><td>102929.50 (n/a)</td><td>102911.00 (n/a)</td><td>108.32 (n/a)</td><td>667.76 (n/a)</td><td>667.31 (n/a)</td><td>667.64 (n/a)</td><td>666.10 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.70 (+0.15%)</td><td>0.70 (-0.05%)</td><td>0.70 (-0.10%)</td><td>0.70 (-0.22%)</td><td>0.00 <b>(+189.08%)</b></td><td>108125.60 (+0.22%)</td><td>107849.78 (+0.05%)</td><td>107890.60 (+0.10%)</td><td>107546.90 (-0.15%)</td><td>215.53 <b>(+189.11%)</b></td><td>638.97 (+0.15%)</td><td>637.18 (-0.05%)</td><td>636.94 (-0.10%)</td><td>635.55 (-0.22%)</td><td>1.27 <b>(+189.08%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107883.60 (n/a)</td><td>107798.04 (n/a)</td><td>107786.60 (n/a)</td><td>107713.50 (n/a)</td><td>74.55 (n/a)</td><td>637.98 (n/a)</td><td>637.48 (n/a)</td><td>637.55 (n/a)</td><td>636.98 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>4.24 (+4.65%)</td><td>3.75 (+8.47%)</td><td>3.96 (+18.85%)</td><td>2.77 (-12.01%)</td><td>0.60 <b>(+67.64%)</b></td><td>2908.70 (+13.65%)</td><td>2201.48 (-6.27%)</td><td>2033.80 (-15.86%)</td><td>1903.00 (-4.44%)</td><td>417.65 <b>(+84.42%)</b></td><td>1110.82 (+4.65%)</td><td>984.15 (+8.47%)</td><td>1039.40 (+18.85%)</td><td>726.75 (-12.01%)</td><td>158.56 <b>(+67.64%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>4.05 (n/a)</td><td>3.46 (n/a)</td><td>3.33 (n/a)</td><td>3.15 (n/a)</td><td>0.36 (n/a)</td><td>2559.30 (n/a)</td><td>2348.74 (n/a)</td><td>2417.30 (n/a)</td><td>1991.50 (n/a)</td><td>226.47 (n/a)</td><td>1061.49 (n/a)</td><td>907.30 (n/a)</td><td>874.51 (n/a)</td><td>825.96 (n/a)</td><td>94.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.50 <b>(+42.06%)</b></td><td>0.37 (+11.47%)</td><td>0.34 (+5.34%)</td><td>0.31 (-0.16%)</td><td>0.08 <b>(+337.08%)</b></td><td>4053.80 (+0.16%)</td><td>3513.42 (-7.77%)</td><td>3664.80 (-5.07%)</td><td>2475.50 <b>(-29.61%)</b></td><td>607.71 <b>(+196.88%)</b></td><td>27.11 <b>(+42.06%)</b></td><td>19.68 (+11.47%)</td><td>18.31 (+5.34%)</td><td>16.55 (-0.16%)</td><td>4.23 <b>(+337.08%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.02 (n/a)</td><td>4047.40 (n/a)</td><td>3809.36 (n/a)</td><td>3860.60 (n/a)</td><td>3516.70 (n/a)</td><td>204.70 (n/a)</td><td>19.08 (n/a)</td><td>17.66 (n/a)</td><td>17.38 (n/a)</td><td>16.58 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>6.42 (+4.46%)</td><td>4.86 (+6.12%)</td><td>4.69 (-0.78%)</td><td>3.71 (+14.66%)</td><td>0.98 (-10.44%)</td><td>1795.30 (-12.79%)</td><td>1412.56 (-7.25%)</td><td>1418.20 (+0.78%)</td><td>1036.30 (-4.27%)</td><td>269.17 <b>(-27.21%)</b></td><td>1983.19 (+4.46%)</td><td>1500.15 (+6.12%)</td><td>1449.16 (-0.78%)</td><td>1144.75 (+14.66%)</td><td>302.89 (-10.44%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.14 (n/a)</td><td>4.58 (n/a)</td><td>4.73 (n/a)</td><td>3.23 (n/a)</td><td>1.09 (n/a)</td><td>2058.60 (n/a)</td><td>1523.04 (n/a)</td><td>1407.20 (n/a)</td><td>1082.50 (n/a)</td><td>369.82 (n/a)</td><td>1898.49 (n/a)</td><td>1413.63 (n/a)</td><td>1460.54 (n/a)</td><td>998.37 (n/a)</td><td>338.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>13.44 (n/a)</td><td>13.17 (n/a)</td><td>13.10 (n/a)</td><td>12.81 (n/a)</td><td>0.27 (n/a)</td><td>13.44 (n/a)</td><td>13.16 (n/a)</td><td>13.09 (n/a)</td><td>12.80 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>25.25 (+2.65%)</td><td>24.16 (+2.06%)</td><td>23.94 (+2.28%)</td><td>23.59 (+3.22%)</td><td>0.64 (-16.53%)</td><td>25.23 (+2.65%)</td><td>24.14 (+2.06%)</td><td>23.93 (+2.28%)</td><td>23.57 (+3.22%)</td><td>0.64 (-16.53%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>24.60 (n/a)</td><td>23.67 (n/a)</td><td>23.41 (n/a)</td><td>22.85 (n/a)</td><td>0.77 (n/a)</td><td>24.58 (n/a)</td><td>23.66 (n/a)</td><td>23.40 (n/a)</td><td>22.84 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>41.28 (-0.62%)</td><td>39.06 (+4.54%)</td><td>39.91 (+1.91%)</td><td>34.94 <b>(+35.64%)</b></td><td>2.48 <b>(-62.34%)</b></td><td>41.25 (-0.62%)</td><td>39.03 (+4.54%)</td><td>39.88 (+1.91%)</td><td>34.92 <b>(+35.64%)</b></td><td>2.48 <b>(-62.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>41.54 (n/a)</td><td>37.36 (n/a)</td><td>39.16 (n/a)</td><td>25.76 (n/a)</td><td>6.59 (n/a)</td><td>41.51 (n/a)</td><td>37.34 (n/a)</td><td>39.14 (n/a)</td><td>25.74 (n/a)</td><td>6.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>45.31 (+0.31%)</td><td>44.21 (+0.73%)</td><td>43.87 (+0.89%)</td><td>43.23 (+0.82%)</td><td>0.84 <b>(-25.48%)</b></td><td>45.29 (+0.31%)</td><td>44.19 (+0.73%)</td><td>43.84 (+0.89%)</td><td>43.20 (+0.82%)</td><td>0.84 <b>(-25.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>45.17 (n/a)</td><td>43.89 (n/a)</td><td>43.48 (n/a)</td><td>42.88 (n/a)</td><td>1.13 (n/a)</td><td>45.15 (n/a)</td><td>43.87 (n/a)</td><td>43.45 (n/a)</td><td>42.85 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>13.37 (n/a)</td><td>12.66 (n/a)</td><td>13.18 (n/a)</td><td>10.60 (n/a)</td><td>1.18 (n/a)</td><td>13.36 (n/a)</td><td>12.66 (n/a)</td><td>13.18 (n/a)</td><td>10.59 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>25.91 (+3.58%)</td><td>24.46 (+0.74%)</td><td>24.66 (+2.00%)</td><td>22.59 (-5.19%)</td><td>1.21 <b>(+167.54%)</b></td><td>25.89 (+3.58%)</td><td>24.44 (+0.74%)</td><td>24.64 (+2.00%)</td><td>22.58 (-5.19%)</td><td>1.21 <b>(+167.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>25.01 (n/a)</td><td>24.28 (n/a)</td><td>24.17 (n/a)</td><td>23.83 (n/a)</td><td>0.45 (n/a)</td><td>25.00 (n/a)</td><td>24.26 (n/a)</td><td>24.16 (n/a)</td><td>23.81 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>41.96 (-0.53%)</td><td>40.61 (+7.50%)</td><td>40.60 (+2.10%)</td><td>39.60 <b>(+53.50%)</b></td><td>0.88 <b>(-87.10%)</b></td><td>41.94 (-0.53%)</td><td>40.59 (+7.50%)</td><td>40.58 (+2.10%)</td><td>39.58 <b>(+53.50%)</b></td><td>0.88 <b>(-87.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>42.19 (n/a)</td><td>37.78 (n/a)</td><td>39.76 (n/a)</td><td>25.80 (n/a)</td><td>6.81 (n/a)</td><td>42.16 (n/a)</td><td>37.76 (n/a)</td><td>39.74 (n/a)</td><td>25.78 (n/a)</td><td>6.81 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>48.17 (+8.63%)</td><td>43.37 (+0.85%)</td><td>41.75 (-4.94%)</td><td>39.33 (+0.34%)</td><td>3.59 <b>(+67.64%)</b></td><td>48.14 (+8.63%)</td><td>43.34 (+0.85%)</td><td>41.73 (-4.94%)</td><td>39.31 (+0.34%)</td><td>3.59 <b>(+67.64%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>44.34 (n/a)</td><td>43.00 (n/a)</td><td>43.92 (n/a)</td><td>39.20 (n/a)</td><td>2.14 (n/a)</td><td>44.31 (n/a)</td><td>42.97 (n/a)</td><td>43.90 (n/a)</td><td>39.17 (n/a)</td><td>2.14 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.33 (-6.14%)</td><td>8.78 (-5.19%)</td><td>9.03 (-1.98%)</td><td>7.95 (-9.82%)</td><td>0.55 <b>(+30.66%)</b></td><td>9.31 (-6.14%)</td><td>8.77 (-5.19%)</td><td>9.01 (-1.98%)</td><td>7.94 (-9.82%)</td><td>0.55 <b>(+30.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.94 (n/a)</td><td>9.27 (n/a)</td><td>9.21 (n/a)</td><td>8.82 (n/a)</td><td>0.42 (n/a)</td><td>9.92 (n/a)</td><td>9.25 (n/a)</td><td>9.20 (n/a)</td><td>8.80 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.91 (-1.95%)</td><td>0.83 (-0.50%)</td><td>0.84 (-0.56%)</td><td>0.77 (+11.23%)</td><td>0.06 <b>(-40.34%)</b></td><td>0.90 (-1.95%)</td><td>0.82 (-0.50%)</td><td>0.82 (-0.56%)</td><td>0.76 (+11.23%)</td><td>0.05 <b>(-40.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.93 (n/a)</td><td>0.84 (n/a)</td><td>0.84 (n/a)</td><td>0.69 (n/a)</td><td>0.09 (n/a)</td><td>0.91 (n/a)</td><td>0.82 (n/a)</td><td>0.83 (n/a)</td><td>0.68 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.99 (-18.71%)</td><td>0.86 (-19.93%)</td><td>0.89 (-18.16%)</td><td>0.65 <b>(-21.91%)</b></td><td>0.12 (-13.78%)</td><td>0.98 (-18.71%)</td><td>0.85 (-19.93%)</td><td>0.88 (-18.16%)</td><td>0.65 <b>(-21.91%)</b></td><td>0.12 (-13.78%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.22 (n/a)</td><td>1.07 (n/a)</td><td>1.08 (n/a)</td><td>0.84 (n/a)</td><td>0.14 (n/a)</td><td>1.21 (n/a)</td><td>1.06 (n/a)</td><td>1.07 (n/a)</td><td>0.83 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>15.07 (-6.92%)</td><td>14.36 (-8.04%)</td><td>14.32 (-9.46%)</td><td>13.52 (-8.42%)</td><td>0.59 (+9.59%)</td><td>14.89 (-6.92%)</td><td>14.20 (-8.04%)</td><td>14.16 (-9.46%)</td><td>13.37 (-8.42%)</td><td>0.59 (+9.59%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>16.19 (n/a)</td><td>15.62 (n/a)</td><td>15.82 (n/a)</td><td>14.77 (n/a)</td><td>0.54 (n/a)</td><td>16.00 (n/a)</td><td>15.44 (n/a)</td><td>15.64 (n/a)</td><td>14.60 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.35 (-0.22%)</td><td>12.10 (+1.05%)</td><td>12.12 (+1.51%)</td><td>11.74 (+1.59%)</td><td>0.25 (-14.89%)</td><td>12.13 (-0.22%)</td><td>11.89 (+1.05%)</td><td>11.91 (+1.51%)</td><td>11.53 (+1.59%)</td><td>0.25 (-14.89%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>12.37 (n/a)</td><td>11.98 (n/a)</td><td>11.94 (n/a)</td><td>11.56 (n/a)</td><td>0.30 (n/a)</td><td>12.16 (n/a)</td><td>11.77 (n/a)</td><td>11.73 (n/a)</td><td>11.35 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.89 (-12.35%)</td><td>7.19 (-10.59%)</td><td>6.92 (-14.84%)</td><td>6.88 (-1.34%)</td><td>0.44 <b>(-47.30%)</b></td><td>7.75 (-12.35%)</td><td>7.07 (-10.59%)</td><td>6.80 (-14.84%)</td><td>6.76 (-1.34%)</td><td>0.43 <b>(-47.30%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.00 (n/a)</td><td>8.04 (n/a)</td><td>8.12 (n/a)</td><td>6.97 (n/a)</td><td>0.83 (n/a)</td><td>8.85 (n/a)</td><td>7.91 (n/a)</td><td>7.98 (n/a)</td><td>6.85 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>6.45 (-4.90%)</td><td>5.78 (-6.42%)</td><td>5.74 (-4.46%)</td><td>5.00 (-11.89%)</td><td>0.56 (+10.37%)</td><td>6.34 (-4.90%)</td><td>5.68 (-6.42%)</td><td>5.65 (-4.46%)</td><td>4.92 (-11.89%)</td><td>0.55 (+10.37%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.78 (n/a)</td><td>6.17 (n/a)</td><td>6.01 (n/a)</td><td>5.67 (n/a)</td><td>0.51 (n/a)</td><td>6.67 (n/a)</td><td>6.07 (n/a)</td><td>5.91 (n/a)</td><td>5.58 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>13.46 (n/a)</td><td>12.86 (n/a)</td><td>13.33 (n/a)</td><td>12.08 (n/a)</td><td>0.72 (n/a)</td><td>13.46 (n/a)</td><td>12.86 (n/a)</td><td>13.32 (n/a)</td><td>12.07 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>13.14 (n/a)</td><td>12.12 (n/a)</td><td>12.14 (n/a)</td><td>10.68 (n/a)</td><td>1.06 (n/a)</td><td>13.13 (n/a)</td><td>12.12 (n/a)</td><td>12.13 (n/a)</td><td>10.67 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>158.62 (n/a)</td><td>163.90 (n/a)</td><td>112.90 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>171.12 (n/a)</td><td>185.20 (n/a)</td><td>115.30 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.20 (n/a)</td><td>168.34 (n/a)</td><td>170.60 (n/a)</td><td>126.20 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>179.28 (n/a)</td><td>177.20 (n/a)</td><td>146.80 (n/a)</td><td>31.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>159.20 (n/a)</td><td>157.00 (n/a)</td><td>97.20 (n/a)</td><td>42.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.20 (n/a)</td><td>184.84 (n/a)</td><td>176.00 (n/a)</td><td>157.90 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.20 (n/a)</td><td>207.92 (n/a)</td><td>208.10 (n/a)</td><td>179.60 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.50 (n/a)</td><td>205.72 (n/a)</td><td>217.60 (n/a)</td><td>169.20 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>194.84 (n/a)</td><td>196.70 (n/a)</td><td>166.90 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>182.08 (n/a)</td><td>184.90 (n/a)</td><td>158.30 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.60 (n/a)</td><td>195.36 (n/a)</td><td>178.90 (n/a)</td><td>153.80 (n/a)</td><td>45.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.40 (n/a)</td><td>187.76 (n/a)</td><td>177.90 (n/a)</td><td>175.60 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.50 (n/a)</td><td>181.14 (n/a)</td><td>162.00 (n/a)</td><td>126.00 (n/a)</td><td>55.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.30 (n/a)</td><td>201.50 (n/a)</td><td>197.00 (n/a)</td><td>166.10 (n/a)</td><td>31.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>196.66 (n/a)</td><td>196.50 (n/a)</td><td>170.40 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>242.20 (n/a)</td><td>222.48 (n/a)</td><td>228.70 (n/a)</td><td>188.00 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>284.70 (n/a)</td><td>204.92 (n/a)</td><td>189.30 (n/a)</td><td>151.60 (n/a)</td><td>50.27 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>188.90 (n/a)</td><td>184.50 (n/a)</td><td>148.80 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.60 (n/a)</td><td>190.42 (n/a)</td><td>194.50 (n/a)</td><td>127.30 (n/a)</td><td>41.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.80 (n/a)</td><td>189.56 (n/a)</td><td>190.20 (n/a)</td><td>163.20 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.70 (n/a)</td><td>166.80 (n/a)</td><td>165.70 (n/a)</td><td>120.20 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>204.40 (n/a)</td><td>209.20 (n/a)</td><td>159.30 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>292.00 (n/a)</td><td>196.28 (n/a)</td><td>177.20 (n/a)</td><td>159.80 (n/a)</td><td>54.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>255.00 (n/a)</td><td>215.92 (n/a)</td><td>213.10 (n/a)</td><td>195.00 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (+8.45%)</td><td>0.18 (+15.28%)</td><td>0.18 (+19.88%)</td><td>0.16 (+13.45%)</td><td>0.01 <b>(-20.02%)</b></td><td>202.10 (-11.86%)</td><td>182.18 (-13.52%)</td><td>180.50 (-16.59%)</td><td>170.30 (-7.80%)</td><td>11.97 <b>(-34.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>210.66 (n/a)</td><td>216.40 (n/a)</td><td>184.70 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>175.48 (n/a)</td><td>174.60 (n/a)</td><td>164.50 (n/a)</td><td>10.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.40 (n/a)</td><td>173.82 (n/a)</td><td>162.20 (n/a)</td><td>149.00 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>196.00 (n/a)</td><td>155.12 (n/a)</td><td>138.90 (n/a)</td><td>132.90 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>251.60 (n/a)</td><td>197.90 (n/a)</td><td>201.30 (n/a)</td><td>150.00 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>216.50 (n/a)</td><td>214.40 (n/a)</td><td>201.30 (n/a)</td><td>12.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>327.20 (n/a)</td><td>233.54 (n/a)</td><td>219.00 (n/a)</td><td>170.50 (n/a)</td><td>59.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>368.60 (n/a)</td><td>232.52 (n/a)</td><td>223.60 (n/a)</td><td>146.30 (n/a)</td><td>83.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-0.80%)</td><td>0.03 (-6.43%)</td><td>0.02 (-11.99%)</td><td>0.02 (-5.88%)</td><td>0.00 (+1.00%)</td><td>186.10 (+6.22%)</td><td>165.12 (+7.00%)</td><td>175.40 (+13.60%)</td><td>135.00 (+0.82%)</td><td>20.85 (+7.77%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.20 (n/a)</td><td>154.32 (n/a)</td><td>154.40 (n/a)</td><td>133.90 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-12.57%)</td><td>0.03 (-2.50%)</td><td>0.03 (+3.40%)</td><td>0.02 (-0.28%)</td><td>0.00 <b>(-40.05%)</b></td><td>183.40 (+0.33%)</td><td>164.84 (+1.51%)</td><td>163.10 (-3.26%)</td><td>142.20 (+14.31%)</td><td>15.84 <b>(-28.63%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.80 (n/a)</td><td>162.38 (n/a)</td><td>168.60 (n/a)</td><td>124.40 (n/a)</td><td>22.19 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(-21.43%)</b></td><td>0.02 (-7.77%)</td><td>0.02 (-5.44%)</td><td>0.02 (-4.10%)</td><td>0.00 <b>(-40.36%)</b></td><td>214.30 (+4.28%)</td><td>174.00 (+6.58%)</td><td>174.30 (+5.76%)</td><td>147.30 <b>(+27.31%)</b></td><td>26.24 (-18.26%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>163.26 (n/a)</td><td>164.80 (n/a)</td><td>115.70 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+0.35%)</td><td>0.02 (-15.20%)</td><td>0.02 (-17.76%)</td><td>0.01 <b>(-43.62%)</b></td><td>0.01 <b>(+83.90%)</b></td><td>319.50 <b>(+77.40%)</b></td><td>197.74 <b>(+27.02%)</b></td><td>182.40 <b>(+21.60%)</b></td><td>126.00 (-0.40%)</td><td>72.44 <b>(+239.39%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.10 (n/a)</td><td>155.68 (n/a)</td><td>150.00 (n/a)</td><td>126.50 (n/a)</td><td>21.35 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+12.40%)</td><td>0.03 (+11.75%)</td><td>0.03 (+12.90%)</td><td>0.02 (+11.84%)</td><td>0.01 <b>(+24.65%)</b></td><td>245.70 (-10.59%)</td><td>168.92 (-9.74%)</td><td>147.90 (-11.38%)</td><td>129.60 (-11.05%)</td><td>48.65 (-5.33%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>274.80 (n/a)</td><td>187.14 (n/a)</td><td>166.90 (n/a)</td><td>145.70 (n/a)</td><td>51.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(-20.13%)</b></td><td>0.02 (-3.98%)</td><td>0.02 (+8.20%)</td><td>0.02 (-10.81%)</td><td>0.00 <b>(-32.87%)</b></td><td>224.90 (+12.11%)</td><td>177.04 (+3.18%)</td><td>167.50 (-7.61%)</td><td>156.80 <b>(+25.24%)</b></td><td>28.25 (-2.97%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.60 (n/a)</td><td>171.58 (n/a)</td><td>181.30 (n/a)</td><td>125.20 (n/a)</td><td>29.11 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-1.39%)</td><td>0.02 (-13.19%)</td><td>0.02 (-9.11%)</td><td>0.01 <b>(-28.13%)</b></td><td>0.01 <b>(+61.71%)</b></td><td>306.50 <b>(+39.13%)</b></td><td>210.12 <b>(+20.01%)</b></td><td>186.90 (+10.01%)</td><td>154.50 (+1.44%)</td><td>60.13 <b>(+126.87%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.30 (n/a)</td><td>175.08 (n/a)</td><td>169.90 (n/a)</td><td>152.30 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+1.15%)</td><td>0.02 (+6.01%)</td><td>0.02 (+11.29%)</td><td>0.02 <b>(+29.10%)</b></td><td>0.00 <b>(-26.82%)</b></td><td>219.60 <b>(-22.54%)</b></td><td>191.58 (-7.73%)</td><td>186.30 (-10.13%)</td><td>157.60 (-1.13%)</td><td>27.50 <b>(-42.68%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>283.50 (n/a)</td><td>207.64 (n/a)</td><td>207.30 (n/a)</td><td>159.40 (n/a)</td><td>47.98 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (-7.62%)</td><td>0.05 (-7.50%)</td><td>0.06 (+5.32%)</td><td>0.04 (-16.54%)</td><td>0.01 (+2.64%)</td><td>201.40 (+19.81%)</td><td>157.56 (+8.98%)</td><td>143.50 (-5.09%)</td><td>127.30 (+8.25%)</td><td>31.13 <b>(+34.90%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.10 (n/a)</td><td>144.58 (n/a)</td><td>151.20 (n/a)</td><td>117.60 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (-11.91%)</td><td>0.05 (-11.58%)</td><td>0.05 (-9.85%)</td><td>0.04 (-12.64%)</td><td>0.01 (-13.97%)</td><td>203.50 (+14.45%)</td><td>175.26 (+13.04%)</td><td>179.70 (+10.93%)</td><td>144.00 (+13.56%)</td><td>21.73 (+11.62%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.80 (n/a)</td><td>155.04 (n/a)</td><td>162.00 (n/a)</td><td>126.80 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (+3.78%)</td><td>0.06 (+3.41%)</td><td>0.06 (+5.72%)</td><td>0.05 (+12.09%)</td><td>0.01 (-3.00%)</td><td>166.10 (-10.79%)</td><td>145.30 (-3.60%)</td><td>143.00 (-5.42%)</td><td>125.20 (-3.69%)</td><td>19.08 (-15.48%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>150.72 (n/a)</td><td>151.20 (n/a)</td><td>130.00 (n/a)</td><td>22.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+2.34%)</td><td>0.05 (-1.42%)</td><td>0.05 (+0.99%)</td><td>0.04 (-0.19%)</td><td>0.01 (+12.06%)</td><td>191.70 (+0.21%)</td><td>160.08 (+2.00%)</td><td>151.80 (-0.98%)</td><td>131.00 (-2.31%)</td><td>28.44 (+14.67%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>156.94 (n/a)</td><td>153.30 (n/a)</td><td>134.10 (n/a)</td><td>24.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (-15.82%)</td><td>0.05 (-14.00%)</td><td>0.05 (-16.65%)</td><td>0.04 (-10.63%)</td><td>0.01 <b>(-28.21%)</b></td><td>214.50 (+11.89%)</td><td>180.22 (+15.56%)</td><td>181.50 <b>(+20.04%)</b></td><td>148.00 (+18.78%)</td><td>23.70 (-5.23%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>155.96 (n/a)</td><td>151.20 (n/a)</td><td>124.60 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 <b>(-31.44%)</b></td><td>0.04 <b>(-33.67%)</b></td><td>0.04 <b>(-38.15%)</b></td><td>0.03 <b>(-28.68%)</b></td><td>0.01 <b>(-33.52%)</b></td><td>237.80 <b>(+40.21%)</b></td><td>197.94 <b>(+50.41%)</b></td><td>200.70 <b>(+61.72%)</b></td><td>168.10 <b>(+45.92%)</b></td><td>29.11 <b>(+31.13%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.60 (n/a)</td><td>131.60 (n/a)</td><td>124.10 (n/a)</td><td>115.20 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 <b>(-21.31%)</b></td><td>0.05 (-17.09%)</td><td>0.04 (-13.42%)</td><td>0.04 (-12.32%)</td><td>0.00 <b>(-59.34%)</b></td><td>191.00 (+14.03%)</td><td>181.88 (+19.39%)</td><td>189.50 (+15.48%)</td><td>166.60 <b>(+27.08%)</b></td><td>11.39 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.50 (n/a)</td><td>152.34 (n/a)</td><td>164.10 (n/a)</td><td>131.10 (n/a)</td><td>19.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (-5.70%)</td><td>0.04 (+16.43%)</td><td>0.04 (+6.79%)</td><td>0.04 <b>(+61.08%)</b></td><td>0.00 <b>(-81.14%)</b></td><td>201.10 <b>(-37.91%)</b></td><td>191.18 <b>(-20.04%)</b></td><td>192.40 (-6.37%)</td><td>177.50 (+6.10%)</td><td>8.67 <b>(-88.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>323.90 (n/a)</td><td>239.08 (n/a)</td><td>205.50 (n/a)</td><td>167.30 (n/a)</td><td>73.63 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (-14.10%)</td><td>0.05 (-0.92%)</td><td>0.05 (-5.99%)</td><td>0.04 <b>(+39.23%)</b></td><td>0.00 <b>(-64.15%)</b></td><td>195.50 <b>(-28.15%)</b></td><td>177.40 (-4.14%)</td><td>172.30 (+6.36%)</td><td>159.80 (+16.39%)</td><td>16.03 <b>(-70.21%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.10 (n/a)</td><td>185.06 (n/a)</td><td>162.00 (n/a)</td><td>137.30 (n/a)</td><td>53.81 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (+4.35%)</td><td>0.04 (+12.16%)</td><td>0.04 (+6.33%)</td><td>0.03 <b>(+25.17%)</b></td><td>0.01 <b>(-36.47%)</b></td><td>257.60 <b>(-20.10%)</b></td><td>211.20 (-13.79%)</td><td>201.40 (-5.93%)</td><td>179.10 (-4.17%)</td><td>30.08 <b>(-51.61%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>322.40 (n/a)</td><td>244.98 (n/a)</td><td>214.10 (n/a)</td><td>186.90 (n/a)</td><td>62.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+9.02%)</td><td>0.10 (+1.57%)</td><td>0.10 (-0.81%)</td><td>0.08 (+2.71%)</td><td>0.02 <b>(+36.01%)</b></td><td>197.10 (-2.67%)</td><td>168.66 (-0.34%)</td><td>172.40 (+0.82%)</td><td>122.10 (-8.26%)</td><td>30.48 <b>(+23.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.50 (n/a)</td><td>169.24 (n/a)</td><td>171.00 (n/a)</td><td>133.10 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+3.23%)</td><td>0.10 (-2.84%)</td><td>0.09 (-14.61%)</td><td>0.08 (-4.34%)</td><td>0.02 <b>(+34.85%)</b></td><td>207.70 (+4.53%)</td><td>168.66 (+4.30%)</td><td>182.00 (+17.12%)</td><td>129.60 (-3.14%)</td><td>32.11 <b>(+32.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>161.70 (n/a)</td><td>155.40 (n/a)</td><td>133.80 (n/a)</td><td>24.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-13.25%)</td><td>0.09 (-10.49%)</td><td>0.09 (-18.41%)</td><td>0.07 (-13.57%)</td><td>0.01 <b>(-22.99%)</b></td><td>225.60 (+15.69%)</td><td>179.58 (+11.06%)</td><td>179.50 <b>(+22.61%)</b></td><td>152.40 (+15.28%)</td><td>29.21 (-1.03%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.00 (n/a)</td><td>161.70 (n/a)</td><td>146.40 (n/a)</td><td>132.20 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-5.69%)</td><td>0.10 (-7.77%)</td><td>0.10 (-9.45%)</td><td>0.09 (+10.44%)</td><td>0.01 <b>(-36.90%)</b></td><td>192.50 (-9.50%)</td><td>171.20 (+6.76%)</td><td>166.60 (+10.40%)</td><td>146.20 (+6.02%)</td><td>18.62 <b>(-39.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.70 (n/a)</td><td>160.36 (n/a)</td><td>150.90 (n/a)</td><td>137.90 (n/a)</td><td>30.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-9.53%)</td><td>0.10 (+0.95%)</td><td>0.10 (+0.14%)</td><td>0.09 (+11.51%)</td><td>0.01 <b>(-36.66%)</b></td><td>180.60 (-10.33%)</td><td>163.88 (-2.22%)</td><td>169.20 (-0.12%)</td><td>144.20 (+10.58%)</td><td>17.07 <b>(-36.96%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>167.60 (n/a)</td><td>169.40 (n/a)</td><td>130.40 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 <b>(-22.97%)</b></td><td>0.09 (+6.06%)</td><td>0.10 (+2.90%)</td><td>0.07 <b>(+37.91%)</b></td><td>0.02 <b>(-57.58%)</b></td><td>235.50 <b>(-27.47%)</b></td><td>184.26 (-17.13%)</td><td>168.40 (-2.77%)</td><td>151.70 <b>(+29.88%)</b></td><td>34.77 <b>(-63.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>324.70 (n/a)</td><td>222.34 (n/a)</td><td>173.20 (n/a)</td><td>116.80 (n/a)</td><td>95.88 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 <b>(-21.98%)</b></td><td>0.08 (-19.15%)</td><td>0.09 (-8.43%)</td><td>0.06 <b>(-22.47%)</b></td><td>0.01 (-5.77%)</td><td>252.60 <b>(+29.01%)</b></td><td>199.02 <b>(+24.73%)</b></td><td>175.70 (+9.20%)</td><td>169.80 <b>(+28.15%)</b></td><td>37.98 <b>(+53.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.80 (n/a)</td><td>159.56 (n/a)</td><td>160.90 (n/a)</td><td>132.50 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (-5.36%)</td><td>0.08 (-5.44%)</td><td>0.08 (-13.55%)</td><td>0.07 (+11.77%)</td><td>0.01 <b>(-52.69%)</b></td><td>220.60 (-10.54%)</td><td>210.70 (+4.41%)</td><td>217.10 (+15.72%)</td><td>187.50 (+5.69%)</td><td>13.42 <b>(-55.30%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>246.60 (n/a)</td><td>201.80 (n/a)</td><td>187.60 (n/a)</td><td>177.40 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 <b>(-31.88%)</b></td><td>0.20 (-12.04%)</td><td>0.19 (-3.88%)</td><td>0.17 (-2.01%)</td><td>0.02 <b>(-62.91%)</b></td><td>192.40 (+2.07%)</td><td>169.54 (+8.62%)</td><td>175.10 (+3.98%)</td><td>146.40 <b>(+46.84%)</b></td><td>20.46 <b>(-45.85%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>188.50 (n/a)</td><td>156.08 (n/a)</td><td>168.40 (n/a)</td><td>99.70 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (-7.94%)</td><td>0.20 (-7.46%)</td><td>0.20 (-4.96%)</td><td>0.16 (-12.31%)</td><td>0.02 (+8.12%)</td><td>202.60 (+14.08%)</td><td>167.48 (+8.54%)</td><td>161.30 (+5.22%)</td><td>145.70 (+8.65%)</td><td>22.61 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>177.60 (n/a)</td><td>154.30 (n/a)</td><td>153.30 (n/a)</td><td>134.10 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (+7.59%)</td><td>0.22 (+2.57%)</td><td>0.22 (+0.59%)</td><td>0.19 (+11.49%)</td><td>0.02 (-3.45%)</td><td>173.70 (-10.28%)</td><td>151.60 (-2.83%)</td><td>146.80 (-0.61%)</td><td>128.70 (-7.08%)</td><td>17.10 <b>(-21.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.60 (n/a)</td><td>156.02 (n/a)</td><td>147.70 (n/a)</td><td>138.50 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (-14.26%)</td><td>0.18 (-14.52%)</td><td>0.18 (-15.57%)</td><td>0.14 <b>(-25.02%)</b></td><td>0.03 (-0.34%)</td><td>234.00 <b>(+33.33%)</b></td><td>182.76 (+17.96%)</td><td>181.40 (+18.48%)</td><td>145.50 (+16.59%)</td><td>32.31 <b>(+56.28%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>175.50 (n/a)</td><td>154.94 (n/a)</td><td>153.10 (n/a)</td><td>124.80 (n/a)</td><td>20.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 <b>(-25.81%)</b></td><td>0.17 (-13.76%)</td><td>0.18 (-6.15%)</td><td>0.13 <b>(-21.05%)</b></td><td>0.03 <b>(-37.09%)</b></td><td>249.60 <b>(+26.70%)</b></td><td>193.90 (+14.98%)</td><td>184.70 (+6.58%)</td><td>160.40 <b>(+34.79%)</b></td><td>34.06 (+14.10%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.00 (n/a)</td><td>168.64 (n/a)</td><td>173.30 (n/a)</td><td>119.00 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 <b>(-24.68%)</b></td><td>0.17 (-14.12%)</td><td>0.17 (-9.42%)</td><td>0.15 (-8.82%)</td><td>0.01 <b>(-53.86%)</b></td><td>212.80 (+9.69%)</td><td>196.56 (+15.10%)</td><td>196.30 (+10.40%)</td><td>174.90 <b>(+32.80%)</b></td><td>16.45 <b>(-29.52%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.00 (n/a)</td><td>170.78 (n/a)</td><td>177.80 (n/a)</td><td>131.70 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (-4.80%)</td><td>0.15 (-11.37%)</td><td>0.15 (-14.32%)</td><td>0.13 (-13.98%)</td><td>0.02 <b>(+40.67%)</b></td><td>243.40 (+16.29%)</td><td>217.88 (+13.53%)</td><td>218.60 (+16.71%)</td><td>185.20 (+5.05%)</td><td>24.25 <b>(+72.14%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>191.92 (n/a)</td><td>187.30 (n/a)</td><td>176.30 (n/a)</td><td>14.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(-20.61%)</b></td><td>0.03 (+1.09%)</td><td>0.03 (+7.13%)</td><td>0.03 <b>(+24.29%)</b></td><td>0.00 <b>(-79.28%)</b></td><td>163.80 (-19.55%)</td><td>155.34 (-4.59%)</td><td>156.70 (-6.67%)</td><td>144.20 <b>(+26.05%)</b></td><td>7.10 <b>(-78.74%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>162.82 (n/a)</td><td>167.90 (n/a)</td><td>114.40 (n/a)</td><td>33.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-16.57%)</td><td>0.03 (-0.65%)</td><td>0.03 (+16.01%)</td><td>0.02 (-5.97%)</td><td>0.00 <b>(-40.68%)</b></td><td>194.30 (+6.35%)</td><td>156.62 (-0.90%)</td><td>146.50 (-13.77%)</td><td>142.90 (+19.88%)</td><td>21.43 <b>(-24.47%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>158.04 (n/a)</td><td>169.90 (n/a)</td><td>119.20 (n/a)</td><td>28.37 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(+22.73%)</b></td><td>0.02 (+14.17%)</td><td>0.02 <b>(+20.06%)</b></td><td>0.01 (-8.76%)</td><td>0.01 <b>(+40.69%)</b></td><td>383.20 (+9.61%)</td><td>220.74 (-7.82%)</td><td>193.30 (-16.72%)</td><td>133.40 (-18.56%)</td><td>95.21 <b>(+33.31%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>349.60 (n/a)</td><td>239.46 (n/a)</td><td>232.10 (n/a)</td><td>163.80 (n/a)</td><td>71.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (-14.54%)</td><td>0.02 (+1.99%)</td><td>0.02 (+1.79%)</td><td>0.02 (+18.62%)</td><td>0.00 <b>(-62.82%)</b></td><td>215.70 (-15.71%)</td><td>198.38 (-4.22%)</td><td>200.20 (-1.77%)</td><td>181.30 (+17.04%)</td><td>13.73 <b>(-62.87%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.90 (n/a)</td><td>207.12 (n/a)</td><td>203.80 (n/a)</td><td>154.90 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+17.45%)</td><td>0.03 (+1.43%)</td><td>0.03 (-3.22%)</td><td>0.02 (-2.59%)</td><td>0.01 <b>(+87.18%)</b></td><td>183.50 (+2.69%)</td><td>152.90 (+1.04%)</td><td>154.00 (+3.36%)</td><td>109.40 (-14.86%)</td><td>30.99 <b>(+65.64%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.70 (n/a)</td><td>151.32 (n/a)</td><td>149.00 (n/a)</td><td>128.50 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-3.43%)</td><td>0.03 (+4.62%)</td><td>0.03 (+6.02%)</td><td>0.02 (+14.06%)</td><td>0.00 <b>(-31.69%)</b></td><td>176.10 (-12.34%)</td><td>158.62 (-5.14%)</td><td>153.50 (-5.71%)</td><td>146.20 (+3.54%)</td><td>13.23 <b>(-38.80%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.90 (n/a)</td><td>167.22 (n/a)</td><td>162.80 (n/a)</td><td>141.20 (n/a)</td><td>21.62 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+2.17%)</td><td>0.02 (+0.48%)</td><td>0.02 (-9.40%)</td><td>0.02 (+11.44%)</td><td>0.00 (-3.42%)</td><td>195.70 (-10.27%)</td><td>175.90 (-0.78%)</td><td>188.50 (+10.43%)</td><td>142.90 (-2.12%)</td><td>22.48 (-15.86%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.10 (n/a)</td><td>177.28 (n/a)</td><td>170.70 (n/a)</td><td>146.00 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+10.52%)</td><td>0.03 (-1.12%)</td><td>0.02 (-3.85%)</td><td>0.02 (-16.75%)</td><td>0.01 <b>(+55.69%)</b></td><td>226.90 <b>(+20.12%)</b></td><td>169.10 (+4.45%)</td><td>169.90 (+4.04%)</td><td>110.80 (-9.55%)</td><td>41.52 <b>(+69.74%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.90 (n/a)</td><td>161.90 (n/a)</td><td>163.30 (n/a)</td><td>122.50 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-4.57%)</td><td>0.03 (-1.07%)</td><td>0.03 (+9.82%)</td><td>0.01 <b>(-37.22%)</b></td><td>0.01 <b>(+34.73%)</b></td><td>286.80 <b>(+59.24%)</b></td><td>174.50 (+6.88%)</td><td>157.10 (-8.93%)</td><td>123.10 (+4.77%)</td><td>64.40 <b>(+145.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>163.26 (n/a)</td><td>172.50 (n/a)</td><td>117.50 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(+30.72%)</b></td><td>0.03 (+11.08%)</td><td>0.02 (+5.72%)</td><td>0.02 (-5.21%)</td><td>0.01 <b>(+179.59%)</b></td><td>212.10 (+5.47%)</td><td>167.52 (-6.04%)</td><td>168.80 (-5.38%)</td><td>117.50 <b>(-23.50%)</b></td><td>40.86 <b>(+129.83%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>178.28 (n/a)</td><td>178.40 (n/a)</td><td>153.60 (n/a)</td><td>17.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-7.02%)</td><td>0.02 (-11.19%)</td><td>0.02 (-0.79%)</td><td>0.01 <b>(-40.11%)</b></td><td>0.01 <b>(+20.20%)</b></td><td>357.40 <b>(+67.01%)</b></td><td>210.96 <b>(+20.55%)</b></td><td>187.30 (+0.81%)</td><td>126.70 (+7.56%)</td><td>86.51 <b>(+135.87%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>175.00 (n/a)</td><td>185.80 (n/a)</td><td>117.80 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(+25.31%)</b></td><td>0.03 (+9.91%)</td><td>0.03 (+6.97%)</td><td>0.02 (-12.07%)</td><td>0.01 <b>(+229.52%)</b></td><td>214.80 (+13.71%)</td><td>161.08 (-5.86%)</td><td>157.30 (-6.54%)</td><td>124.60 <b>(-20.18%)</b></td><td>36.20 <b>(+194.65%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.90 (n/a)</td><td>171.10 (n/a)</td><td>168.30 (n/a)</td><td>156.10 (n/a)</td><td>12.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(+43.53%)</b></td><td>0.02 <b>(+28.90%)</b></td><td>0.02 (+11.12%)</td><td>0.02 <b>(+57.21%)</b></td><td>0.00 <b>(+26.28%)</b></td><td>193.90 <b>(-36.41%)</b></td><td>172.68 <b>(-23.08%)</b></td><td>183.40 (-10.01%)</td><td>134.10 <b>(-30.34%)</b></td><td>25.43 <b>(-45.00%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>304.90 (n/a)</td><td>224.48 (n/a)</td><td>203.80 (n/a)</td><td>192.50 (n/a)</td><td>46.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+13.08%)</td><td>0.02 (+6.40%)</td><td>0.02 (+7.67%)</td><td>0.02 (+6.03%)</td><td>0.00 <b>(+49.60%)</b></td><td>203.80 (-5.65%)</td><td>182.94 (-5.63%)</td><td>179.50 (-7.14%)</td><td>158.20 (-11.57%)</td><td>18.66 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.00 (n/a)</td><td>193.86 (n/a)</td><td>193.30 (n/a)</td><td>178.90 (n/a)</td><td>14.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+9.92%)</td><td>0.02 (+8.19%)</td><td>0.02 (+14.21%)</td><td>0.02 (+4.99%)</td><td>0.00 <b>(+41.84%)</b></td><td>215.40 (-4.73%)</td><td>182.08 (-6.55%)</td><td>170.00 (-12.46%)</td><td>144.50 (-9.01%)</td><td>31.57 <b>(+29.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.10 (n/a)</td><td>194.84 (n/a)</td><td>194.20 (n/a)</td><td>158.80 (n/a)</td><td>24.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+7.28%)</td><td>0.02 (+1.79%)</td><td>0.02 (-0.63%)</td><td>0.02 (+0.00%)</td><td>0.00 (+5.52%)</td><td>234.10 (+0.00%)</td><td>184.82 (-1.66%)</td><td>182.20 (+0.61%)</td><td>144.20 (-6.79%)</td><td>33.17 (-0.47%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.10 (n/a)</td><td>187.94 (n/a)</td><td>181.10 (n/a)</td><td>154.70 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (-10.53%)</td><td>0.05 (-13.31%)</td><td>0.05 (-15.32%)</td><td>0.04 <b>(-21.80%)</b></td><td>0.01 (+3.58%)</td><td>223.40 <b>(+27.88%)</b></td><td>174.72 (+16.59%)</td><td>178.30 (+18.08%)</td><td>130.80 (+11.70%)</td><td>35.10 <b>(+45.19%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.70 (n/a)</td><td>149.86 (n/a)</td><td>151.00 (n/a)</td><td>117.10 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (-13.17%)</td><td>0.05 (-3.39%)</td><td>0.05 (+4.00%)</td><td>0.04 (+7.17%)</td><td>0.01 <b>(-41.41%)</b></td><td>211.80 (-6.70%)</td><td>169.96 (+0.30%)</td><td>167.50 (-3.85%)</td><td>136.10 (+15.14%)</td><td>27.05 <b>(-35.77%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>169.46 (n/a)</td><td>174.20 (n/a)</td><td>118.20 (n/a)</td><td>42.11 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (-12.34%)</td><td>0.04 (-10.10%)</td><td>0.04 (-12.12%)</td><td>0.03 (-10.37%)</td><td>0.00 <b>(-34.73%)</b></td><td>259.50 (+11.56%)</td><td>233.66 (+10.89%)</td><td>227.90 (+13.78%)</td><td>216.00 (+14.10%)</td><td>16.30 (-17.89%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>232.60 (n/a)</td><td>210.72 (n/a)</td><td>200.30 (n/a)</td><td>189.30 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+18.29%)</td><td>0.04 (+0.37%)</td><td>0.04 (-9.05%)</td><td>0.03 (-8.91%)</td><td>0.01 <b>(+88.30%)</b></td><td>234.50 (+9.78%)</td><td>191.58 (+1.99%)</td><td>201.20 (+9.95%)</td><td>138.10 (-15.43%)</td><td>37.58 <b>(+70.30%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>187.84 (n/a)</td><td>183.00 (n/a)</td><td>163.30 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (+9.17%)</td><td>0.05 (+4.63%)</td><td>0.05 (-7.03%)</td><td>0.05 (+15.79%)</td><td>0.01 (-8.69%)</td><td>181.60 (-13.65%)</td><td>152.68 (-5.36%)</td><td>155.80 (+7.60%)</td><td>123.70 (-8.37%)</td><td>23.80 <b>(-27.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>161.32 (n/a)</td><td>144.80 (n/a)</td><td>135.00 (n/a)</td><td>32.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (-9.17%)</td><td>0.05 (+0.60%)</td><td>0.05 (+7.03%)</td><td>0.05 (+5.90%)</td><td>0.00 <b>(-55.34%)</b></td><td>170.90 (-5.58%)</td><td>161.30 (-1.39%)</td><td>160.20 (-6.59%)</td><td>149.80 (+10.07%)</td><td>8.25 <b>(-52.86%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>163.58 (n/a)</td><td>171.50 (n/a)</td><td>136.10 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (+13.05%)</td><td>0.06 (+1.92%)</td><td>0.06 (+4.10%)</td><td>0.04 (-4.33%)</td><td>0.01 <b>(+66.88%)</b></td><td>200.00 (+4.55%)</td><td>154.06 (+0.44%)</td><td>141.40 (-3.94%)</td><td>115.40 (-11.57%)</td><td>34.47 <b>(+52.39%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>153.38 (n/a)</td><td>147.20 (n/a)</td><td>130.50 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+2.41%)</td><td>0.05 (+9.32%)</td><td>0.05 (+10.12%)</td><td>0.04 (+12.88%)</td><td>0.01 (-13.69%)</td><td>190.60 (-11.43%)</td><td>161.58 (-9.31%)</td><td>163.60 (-9.16%)</td><td>129.30 (-2.34%)</td><td>22.83 <b>(-23.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>178.16 (n/a)</td><td>180.10 (n/a)</td><td>132.40 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+16.14%)</td><td>0.05 (+10.41%)</td><td>0.04 (+1.99%)</td><td>0.04 (+6.90%)</td><td>0.01 <b>(+59.55%)</b></td><td>200.60 (-6.48%)</td><td>171.46 (-8.25%)</td><td>185.40 (-1.96%)</td><td>135.90 (-13.88%)</td><td>29.74 <b>(+27.42%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>186.88 (n/a)</td><td>189.10 (n/a)</td><td>157.80 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 <b>(+25.25%)</b></td><td>0.05 (+13.27%)</td><td>0.05 (+5.71%)</td><td>0.04 (+6.08%)</td><td>0.01 <b>(+77.79%)</b></td><td>220.60 (-5.73%)</td><td>164.92 (-9.26%)</td><td>169.40 (-5.42%)</td><td>120.10 <b>(-20.15%)</b></td><td>40.79 <b>(+28.04%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>234.00 (n/a)</td><td>181.76 (n/a)</td><td>179.10 (n/a)</td><td>150.40 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+1.26%)</td><td>0.05 <b>(+20.08%)</b></td><td>0.06 <b>(+39.97%)</b></td><td>0.04 (-1.27%)</td><td>0.01 (+1.27%)</td><td>227.70 (+1.29%)</td><td>159.20 (-16.60%)</td><td>145.30 <b>(-28.56%)</b></td><td>136.30 (-1.23%)</td><td>38.63 (+2.20%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>190.88 (n/a)</td><td>203.40 (n/a)</td><td>138.00 (n/a)</td><td>37.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (-12.89%)</td><td>0.05 (+6.15%)</td><td>0.05 (+14.66%)</td><td>0.04 (+16.22%)</td><td>0.01 <b>(-43.21%)</b></td><td>201.00 (-13.96%)</td><td>169.56 (-8.70%)</td><td>158.50 (-12.82%)</td><td>149.10 (+14.78%)</td><td>23.53 <b>(-45.16%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>185.72 (n/a)</td><td>181.80 (n/a)</td><td>129.90 (n/a)</td><td>42.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (+3.42%)</td><td>0.04 (+11.04%)</td><td>0.04 (+6.97%)</td><td>0.03 <b>(+32.87%)</b></td><td>0.00 <b>(-33.53%)</b></td><td>239.60 <b>(-24.73%)</b></td><td>209.80 (-12.03%)</td><td>209.70 (-6.51%)</td><td>179.30 (-3.29%)</td><td>24.87 <b>(-52.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.30 (n/a)</td><td>238.50 (n/a)</td><td>224.30 (n/a)</td><td>185.40 (n/a)</td><td>51.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 <b>(-24.22%)</b></td><td>0.05 (+10.33%)</td><td>0.05 <b>(+25.67%)</b></td><td>0.05 <b>(+29.26%)</b></td><td>0.00 <b>(-70.52%)</b></td><td>180.50 <b>(-22.63%)</b></td><td>158.80 (-15.03%)</td><td>159.50 <b>(-20.41%)</b></td><td>142.60 <b>(+31.91%)</b></td><td>15.10 <b>(-68.04%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>233.30 (n/a)</td><td>186.90 (n/a)</td><td>200.40 (n/a)</td><td>108.10 (n/a)</td><td>47.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 <b>(+38.01%)</b></td><td>0.05 <b>(+21.07%)</b></td><td>0.05 <b>(+30.72%)</b></td><td>0.03 (-8.04%)</td><td>0.02 <b>(+82.74%)</b></td><td>244.40 (+8.72%)</td><td>165.46 (-13.53%)</td><td>158.10 <b>(-23.51%)</b></td><td>103.00 <b>(-27.52%)</b></td><td>51.64 <b>(+42.26%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>191.36 (n/a)</td><td>206.70 (n/a)</td><td>142.10 (n/a)</td><td>36.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (+0.28%)</td><td>0.06 (+14.64%)</td><td>0.06 <b>(+28.91%)</b></td><td>0.05 <b>(+28.68%)</b></td><td>0.01 <b>(-31.11%)</b></td><td>173.80 <b>(-22.27%)</b></td><td>146.56 (-15.56%)</td><td>144.50 <b>(-22.44%)</b></td><td>118.90 (-0.25%)</td><td>23.21 <b>(-45.45%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>173.56 (n/a)</td><td>186.30 (n/a)</td><td>119.20 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-18.14%)</td><td>0.09 (-12.04%)</td><td>0.09 (-10.71%)</td><td>0.08 (-10.00%)</td><td>0.01 <b>(-36.49%)</b></td><td>198.90 (+11.12%)</td><td>177.10 (+12.98%)</td><td>176.10 (+12.02%)</td><td>154.00 <b>(+22.13%)</b></td><td>17.66 (-12.51%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.00 (n/a)</td><td>156.76 (n/a)</td><td>157.20 (n/a)</td><td>126.10 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-13.00%)</td><td>0.10 (-4.76%)</td><td>0.09 (-14.02%)</td><td>0.08 (+13.46%)</td><td>0.01 <b>(-50.94%)</b></td><td>205.90 (-11.86%)</td><td>174.38 (+1.09%)</td><td>179.10 (+16.30%)</td><td>153.00 (+14.86%)</td><td>21.96 <b>(-50.76%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.60 (n/a)</td><td>172.50 (n/a)</td><td>154.00 (n/a)</td><td>133.20 (n/a)</td><td>44.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-4.27%)</td><td>0.09 (+4.43%)</td><td>0.09 (+13.26%)</td><td>0.08 (+14.31%)</td><td>0.01 <b>(-38.90%)</b></td><td>212.10 (-12.50%)</td><td>178.68 (-6.68%)</td><td>175.90 (-11.74%)</td><td>151.20 (+4.42%)</td><td>23.98 <b>(-42.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.40 (n/a)</td><td>191.46 (n/a)</td><td>199.30 (n/a)</td><td>144.80 (n/a)</td><td>41.81 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (+14.54%)</td><td>0.09 (+9.88%)</td><td>0.08 (+2.27%)</td><td>0.07 (+4.92%)</td><td>0.01 <b>(+63.91%)</b></td><td>225.80 (-4.69%)</td><td>188.66 (-8.08%)</td><td>196.80 (-2.19%)</td><td>155.70 (-12.68%)</td><td>28.44 <b>(+33.61%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.90 (n/a)</td><td>205.24 (n/a)</td><td>201.20 (n/a)</td><td>178.30 (n/a)</td><td>21.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-13.14%)</td><td>0.10 (-7.80%)</td><td>0.10 (-3.75%)</td><td>0.08 (+1.19%)</td><td>0.01 <b>(-36.20%)</b></td><td>207.10 (-1.19%)</td><td>171.72 (+6.94%)</td><td>165.30 (+3.90%)</td><td>147.90 (+15.19%)</td><td>22.40 <b>(-27.43%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.60 (n/a)</td><td>160.58 (n/a)</td><td>159.10 (n/a)</td><td>128.40 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (+1.22%)</td><td>0.10 (-5.65%)</td><td>0.10 (+5.60%)</td><td>0.04 <b>(-53.40%)</b></td><td>0.04 <b>(+85.85%)</b></td><td>405.80 <b>(+114.60%)</b></td><td>203.18 <b>(+23.27%)</b></td><td>156.50 (-5.27%)</td><td>121.20 (-1.22%)</td><td>115.77 <b>(+324.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.10 (n/a)</td><td>164.82 (n/a)</td><td>165.20 (n/a)</td><td>122.70 (n/a)</td><td>27.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+1.45%)</td><td>0.11 (+16.70%)</td><td>0.12 <b>(+27.46%)</b></td><td>0.08 (+16.46%)</td><td>0.02 (-6.11%)</td><td>205.90 (-14.14%)</td><td>156.42 (-15.11%)</td><td>137.50 <b>(-21.52%)</b></td><td>129.00 (-1.38%)</td><td>32.32 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.80 (n/a)</td><td>184.26 (n/a)</td><td>175.20 (n/a)</td><td>130.80 (n/a)</td><td>40.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (-5.33%)</td><td>0.11 (+3.07%)</td><td>0.11 (+7.65%)</td><td>0.11 (+13.67%)</td><td>0.01 <b>(-42.84%)</b></td><td>152.10 (-11.98%)</td><td>143.88 (-4.14%)</td><td>146.60 (-7.10%)</td><td>124.40 (+5.69%)</td><td>11.37 <b>(-46.42%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>172.80 (n/a)</td><td>150.10 (n/a)</td><td>157.80 (n/a)</td><td>117.70 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 <b>(+26.57%)</b></td><td>0.11 (+10.46%)</td><td>0.10 (-0.08%)</td><td>0.08 <b>(+52.70%)</b></td><td>0.03 (+2.62%)</td><td>200.60 <b>(-34.51%)</b></td><td>160.74 (-12.96%)</td><td>158.80 (+0.06%)</td><td>110.30 <b>(-20.99%)</b></td><td>33.14 <b>(-51.76%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>306.30 (n/a)</td><td>184.68 (n/a)</td><td>158.70 (n/a)</td><td>139.60 (n/a)</td><td>68.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (-8.35%)</td><td>0.09 (-10.50%)</td><td>0.10 (+4.66%)</td><td>0.04 <b>(-52.26%)</b></td><td>0.03 <b>(+133.28%)</b></td><td>369.00 <b>(+109.42%)</b></td><td>204.30 <b>(+23.53%)</b></td><td>167.50 (-4.45%)</td><td>150.80 (+9.12%)</td><td>92.46 <b>(+462.29%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>165.38 (n/a)</td><td>175.30 (n/a)</td><td>138.20 (n/a)</td><td>16.44 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+15.60%)</td><td>0.10 (-0.13%)</td><td>0.11 (+0.14%)</td><td>0.09 (+1.69%)</td><td>0.02 <b>(+58.39%)</b></td><td>189.80 (-1.66%)</td><td>161.32 (+1.29%)</td><td>154.70 (-0.19%)</td><td>125.80 (-13.48%)</td><td>26.16 <b>(+34.80%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>159.26 (n/a)</td><td>155.00 (n/a)</td><td>145.40 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (-0.57%)</td><td>0.11 (-2.98%)</td><td>0.10 (-11.40%)</td><td>0.09 (-2.25%)</td><td>0.02 <b>(+34.62%)</b></td><td>176.70 (+2.32%)</td><td>153.64 (+4.29%)</td><td>165.40 (+12.82%)</td><td>124.00 (+0.57%)</td><td>26.78 <b>(+37.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>147.32 (n/a)</td><td>146.60 (n/a)</td><td>123.30 (n/a)</td><td>19.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (+17.82%)</td><td>0.09 (+11.99%)</td><td>0.10 (+14.47%)</td><td>0.06 (-0.22%)</td><td>0.02 <b>(+42.40%)</b></td><td>285.40 (+0.21%)</td><td>184.92 (-8.56%)</td><td>160.40 (-12.64%)</td><td>148.40 (-15.10%)</td><td>56.88 <b>(+22.62%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>284.80 (n/a)</td><td>202.22 (n/a)</td><td>183.60 (n/a)</td><td>174.80 (n/a)</td><td>46.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 <b>(+32.44%)</b></td><td>0.11 (+19.13%)</td><td>0.11 <b>(+27.77%)</b></td><td>0.08 (-5.33%)</td><td>0.02 <b>(+132.64%)</b></td><td>213.20 (+5.60%)</td><td>160.20 (-13.63%)</td><td>153.90 <b>(-21.72%)</b></td><td>124.20 <b>(-24.50%)</b></td><td>35.75 <b>(+86.67%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>185.48 (n/a)</td><td>196.60 (n/a)</td><td>164.50 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (+8.39%)</td><td>0.10 (+7.71%)</td><td>0.10 (+12.28%)</td><td>0.09 (+2.92%)</td><td>0.01 <b>(+36.91%)</b></td><td>184.30 (-2.85%)</td><td>166.60 (-6.98%)</td><td>163.50 (-10.95%)</td><td>151.40 (-7.74%)</td><td>13.52 <b>(+22.88%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>179.10 (n/a)</td><td>183.60 (n/a)</td><td>164.10 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (+2.77%)</td><td>0.09 (-5.94%)</td><td>0.09 (-3.86%)</td><td>0.07 <b>(-23.12%)</b></td><td>0.01 <b>(+152.47%)</b></td><td>231.50 <b>(+30.06%)</b></td><td>180.40 (+8.32%)</td><td>175.30 (+4.04%)</td><td>151.80 (-2.69%)</td><td>31.13 <b>(+226.79%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>166.54 (n/a)</td><td>168.50 (n/a)</td><td>156.00 (n/a)</td><td>9.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.26 (-1.63%)</td><td>0.22 (+14.91%)</td><td>0.23 <b>(+35.31%)</b></td><td>0.17 (+11.15%)</td><td>0.04 (-1.51%)</td><td>190.40 (-10.02%)</td><td>154.52 (-13.24%)</td><td>143.20 <b>(-26.11%)</b></td><td>126.10 (+1.61%)</td><td>31.86 (-7.56%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>211.60 (n/a)</td><td>178.10 (n/a)</td><td>193.80 (n/a)</td><td>124.10 (n/a)</td><td>34.47 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (+11.26%)</td><td>0.22 (+7.42%)</td><td>0.19 (+3.22%)</td><td>0.18 (+3.17%)</td><td>0.05 <b>(+40.21%)</b></td><td>179.40 (-3.08%)</td><td>152.88 (-5.56%)</td><td>168.10 (-3.11%)</td><td>114.00 (-10.17%)</td><td>30.11 <b>(+23.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>185.10 (n/a)</td><td>161.88 (n/a)</td><td>173.50 (n/a)</td><td>126.90 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 <b>(+25.31%)</b></td><td>0.16 (+8.78%)</td><td>0.15 (-5.55%)</td><td>0.13 (+19.61%)</td><td>0.03 <b>(+40.28%)</b></td><td>243.50 (-16.38%)</td><td>209.56 (-7.59%)</td><td>220.20 (+5.87%)</td><td>164.80 <b>(-20.19%)</b></td><td>34.20 (-6.48%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>291.20 (n/a)</td><td>226.76 (n/a)</td><td>208.00 (n/a)</td><td>206.50 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (+0.61%)</td><td>0.17 (+2.59%)</td><td>0.16 (+1.40%)</td><td>0.15 (-1.06%)</td><td>0.02 <b>(+22.47%)</b></td><td>221.60 (+1.05%)</td><td>195.48 (-2.02%)</td><td>207.10 (-1.38%)</td><td>164.80 (-0.60%)</td><td>26.50 <b>(+22.40%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.30 (n/a)</td><td>199.52 (n/a)</td><td>210.00 (n/a)</td><td>165.80 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (+11.10%)</td><td>0.21 (+5.14%)</td><td>0.20 (+3.20%)</td><td>0.15 <b>(+36.76%)</b></td><td>0.06 (-14.41%)</td><td>212.10 <b>(-26.89%)</b></td><td>161.96 (-9.54%)</td><td>163.00 (-3.09%)</td><td>108.70 (-10.02%)</td><td>38.07 <b>(-44.27%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>290.10 (n/a)</td><td>179.04 (n/a)</td><td>168.20 (n/a)</td><td>120.80 (n/a)</td><td>68.31 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (+19.81%)</td><td>0.20 (+18.05%)</td><td>0.20 <b>(+23.89%)</b></td><td>0.18 <b>(+25.66%)</b></td><td>0.03 (+2.85%)</td><td>183.90 <b>(-20.42%)</b></td><td>163.06 (-15.76%)</td><td>160.40 (-19.28%)</td><td>132.00 (-16.51%)</td><td>20.78 <b>(-30.80%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.10 (n/a)</td><td>193.56 (n/a)</td><td>198.70 (n/a)</td><td>158.10 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (+15.47%)</td><td>0.20 (+13.87%)</td><td>0.20 (+14.95%)</td><td>0.14 <b>(+53.38%)</b></td><td>0.05 (-10.21%)</td><td>227.40 <b>(-34.81%)</b></td><td>168.18 (-17.36%)</td><td>165.10 (-13.01%)</td><td>114.40 (-13.40%)</td><td>41.53 <b>(-51.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>348.80 (n/a)</td><td>203.50 (n/a)</td><td>189.80 (n/a)</td><td>132.10 (n/a)</td><td>85.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (+19.05%)</td><td>0.22 (+16.94%)</td><td>0.23 (+5.61%)</td><td>0.16 <b>(+80.10%)</b></td><td>0.05 <b>(-22.86%)</b></td><td>211.30 <b>(-44.47%)</b></td><td>155.90 <b>(-22.97%)</b></td><td>145.40 (-5.34%)</td><td>113.40 (-16.00%)</td><td>37.42 <b>(-63.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>380.50 (n/a)</td><td>202.40 (n/a)</td><td>153.60 (n/a)</td><td>135.00 (n/a)</td><td>103.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.28 (+4.94%)</td><td>0.20 (+0.66%)</td><td>0.17 (-4.83%)</td><td>0.14 (-0.64%)</td><td>0.06 (-1.23%)</td><td>235.00 (+0.64%)</td><td>176.74 (-1.26%)</td><td>191.90 (+5.09%)</td><td>115.80 (-4.69%)</td><td>50.27 (-6.87%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>233.50 (n/a)</td><td>179.00 (n/a)</td><td>182.60 (n/a)</td><td>121.50 (n/a)</td><td>53.98 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.31 <b>(+31.77%)</b></td><td>0.24 (+17.98%)</td><td>0.25 <b>(+24.20%)</b></td><td>0.17 (-5.85%)</td><td>0.06 <b>(+184.26%)</b></td><td>194.90 (+6.27%)</td><td>144.90 (-11.40%)</td><td>133.30 (-19.50%)</td><td>107.40 <b>(-24.10%)</b></td><td>37.81 <b>(+130.88%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>183.40 (n/a)</td><td>163.54 (n/a)</td><td>165.60 (n/a)</td><td>141.50 (n/a)</td><td>16.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (+15.74%)</td><td>0.21 (+3.92%)</td><td>0.20 (-2.74%)</td><td>0.15 (+8.48%)</td><td>0.04 (+14.09%)</td><td>221.60 (-7.82%)</td><td>164.26 (-3.73%)</td><td>163.60 (+2.76%)</td><td>120.80 (-13.59%)</td><td>36.71 (-9.99%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>240.40 (n/a)</td><td>170.62 (n/a)</td><td>159.20 (n/a)</td><td>139.80 (n/a)</td><td>40.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (-9.22%)</td><td>0.19 (-10.40%)</td><td>0.19 (-12.08%)</td><td>0.16 (-13.59%)</td><td>0.02 (+11.70%)</td><td>203.00 (+15.67%)</td><td>170.84 (+12.13%)</td><td>175.30 (+13.76%)</td><td>146.70 (+10.14%)</td><td>22.30 <b>(+40.74%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>175.50 (n/a)</td><td>152.36 (n/a)</td><td>154.10 (n/a)</td><td>133.20 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (+10.65%)</td><td>0.19 (+5.50%)</td><td>0.19 (-1.76%)</td><td>0.15 (+13.27%)</td><td>0.03 (+3.25%)</td><td>219.40 (-11.71%)</td><td>178.52 (-5.54%)</td><td>176.80 (+1.78%)</td><td>153.50 (-9.60%)</td><td>26.82 (-19.94%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>248.50 (n/a)</td><td>189.00 (n/a)</td><td>173.70 (n/a)</td><td>169.80 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (-1.20%)</td><td>0.18 (+1.70%)</td><td>0.18 (+6.48%)</td><td>0.15 (+2.48%)</td><td>0.02 (-4.66%)</td><td>214.90 (-2.45%)</td><td>188.42 (-1.76%)</td><td>183.40 (-6.09%)</td><td>168.40 (+1.20%)</td><td>18.82 (-5.61%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>220.30 (n/a)</td><td>191.80 (n/a)</td><td>195.30 (n/a)</td><td>166.40 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.26 <b>(+26.74%)</b></td><td>0.17 (-3.25%)</td><td>0.16 (-14.13%)</td><td>0.10 <b>(-26.98%)</b></td><td>0.06 <b>(+125.08%)</b></td><td>330.70 <b>(+36.94%)</b></td><td>210.46 (+12.21%)</td><td>208.00 (+16.46%)</td><td>127.80 <b>(-21.11%)</b></td><td>77.52 <b>(+141.06%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>241.50 (n/a)</td><td>187.56 (n/a)</td><td>178.60 (n/a)</td><td>162.00 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 <b>(+31.75%)</b></td><td>0.19 (+13.88%)</td><td>0.19 (+19.04%)</td><td>0.15 (-0.18%)</td><td>0.03 <b>(+156.88%)</b></td><td>223.00 (+0.18%)</td><td>179.66 (-10.40%)</td><td>171.00 (-16.01%)</td><td>139.30 <b>(-24.09%)</b></td><td>31.72 <b>(+98.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>200.52 (n/a)</td><td>203.60 (n/a)</td><td>183.50 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (+0.96%)</td><td>0.21 (+0.30%)</td><td>0.21 (+0.22%)</td><td>0.21 (+0.00%)</td><td>0.00 <b>(+535.68%)</b></td><td>40888.80 (-0.00%)</td><td>40732.90 (-0.30%)</td><td>40765.20 (-0.22%)</td><td>40434.80 (-0.95%)</td><td>175.07 <b>(+529.00%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40889.40 (n/a)</td><td>40856.46 (n/a)</td><td>40854.20 (n/a)</td><td>40823.70 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (+0.76%)</td><td>0.21 (+0.33%)</td><td>0.21 (+0.19%)</td><td>0.21 (+0.05%)</td><td>0.00 <b>(+251.21%)</b></td><td>40894.10 (-0.05%)</td><td>40726.96 (-0.32%)</td><td>40764.20 (-0.19%)</td><td>40508.40 (-0.76%)</td><td>141.12 <b>(+248.20%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40913.30 (n/a)</td><td>40859.42 (n/a)</td><td>40841.30 (n/a)</td><td>40818.00 (n/a)</td><td>40.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+0.02%)</td><td>0.13 (+0.01%)</td><td>0.13 (+0.01%)</td><td>0.13 (-0.02%)</td><td>0.00 <b>(+65.91%)</b></td><td>321910.70 (+0.02%)</td><td>321718.26 (-0.01%)</td><td>321736.90 (-0.01%)</td><td>321561.70 (-0.02%)</td><td>140.89 <b>(+65.89%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321838.30 (n/a)</td><td>321759.50 (n/a)</td><td>321784.00 (n/a)</td><td>321614.20 (n/a)</td><td>84.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(-21.08%)</b></td><td>0.02 <b>(-24.11%)</b></td><td>0.02 (-14.55%)</td><td>0.01 <b>(-52.58%)</b></td><td>0.01 <b>(+46.56%)</b></td><td>360.20 <b>(+110.89%)</b></td><td>218.60 <b>(+41.23%)</b></td><td>196.40 (+16.97%)</td><td>161.00 <b>(+26.67%)</b></td><td>82.00 <b>(+291.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.80 (n/a)</td><td>154.78 (n/a)</td><td>167.90 (n/a)</td><td>127.10 (n/a)</td><td>20.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (-16.72%)</td><td>0.03 (-15.39%)</td><td>0.03 (-15.50%)</td><td>0.03 (-8.88%)</td><td>0.00 <b>(-31.15%)</b></td><td>233.80 (+9.71%)</td><td>200.44 (+17.11%)</td><td>207.20 (+18.33%)</td><td>162.90 <b>(+20.04%)</b></td><td>26.86 (-9.77%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>171.16 (n/a)</td><td>175.10 (n/a)</td><td>135.70 (n/a)</td><td>29.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 <b>(-22.50%)</b></td><td>0.02 (-3.02%)</td><td>0.02 (+2.79%)</td><td>0.02 (+0.06%)</td><td>0.00 <b>(-67.71%)</b></td><td>193.70 (-0.05%)</td><td>173.98 (+1.19%)</td><td>170.10 (-2.69%)</td><td>166.40 <b>(+28.99%)</b></td><td>11.17 <b>(-57.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.80 (n/a)</td><td>171.94 (n/a)</td><td>174.80 (n/a)</td><td>129.00 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 <b>(+20.59%)</b></td><td>0.03 (+9.52%)</td><td>0.03 (+2.11%)</td><td>0.02 (+14.14%)</td><td>0.01 <b>(+29.35%)</b></td><td>207.50 (-12.41%)</td><td>169.78 (-8.33%)</td><td>169.00 (-2.03%)</td><td>129.40 (-17.05%)</td><td>29.47 (-8.18%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.90 (n/a)</td><td>185.20 (n/a)</td><td>172.50 (n/a)</td><td>156.00 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-16.02%)</td><td>0.02 (-7.53%)</td><td>0.02 (-6.57%)</td><td>0.02 <b>(+37.68%)</b></td><td>0.00 <b>(-60.40%)</b></td><td>211.40 <b>(-27.35%)</b></td><td>173.84 (+0.14%)</td><td>170.10 (+7.05%)</td><td>152.40 (+19.06%)</td><td>22.97 <b>(-65.98%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>291.00 (n/a)</td><td>173.60 (n/a)</td><td>158.90 (n/a)</td><td>128.00 (n/a)</td><td>67.52 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (+19.55%)</td><td>0.04 <b>(+21.44%)</b></td><td>0.04 <b>(+22.13%)</b></td><td>0.03 (+4.36%)</td><td>0.01 <b>(+58.48%)</b></td><td>191.50 (-4.20%)</td><td>145.82 (-16.48%)</td><td>142.20 (-18.13%)</td><td>118.00 (-16.37%)</td><td>28.52 <b>(+30.72%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>174.60 (n/a)</td><td>173.70 (n/a)</td><td>141.10 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+6.56%)</td><td>0.02 (+0.08%)</td><td>0.03 (-2.74%)</td><td>0.02 (-6.60%)</td><td>0.00 <b>(+64.00%)</b></td><td>193.90 (+7.07%)</td><td>166.84 (+0.90%)</td><td>163.20 (+2.84%)</td><td>142.10 (-6.14%)</td><td>23.10 <b>(+63.20%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>165.36 (n/a)</td><td>158.70 (n/a)</td><td>151.40 (n/a)</td><td>14.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-7.67%)</td><td>0.02 (+0.31%)</td><td>0.02 (+0.32%)</td><td>0.02 <b>(+21.52%)</b></td><td>0.00 <b>(-43.89%)</b></td><td>213.30 (-17.71%)</td><td>189.80 (-2.30%)</td><td>184.80 (-0.27%)</td><td>169.40 (+8.31%)</td><td>18.83 <b>(-51.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>259.20 (n/a)</td><td>194.26 (n/a)</td><td>185.30 (n/a)</td><td>156.40 (n/a)</td><td>38.81 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-8.83%)</td><td>0.02 (-17.92%)</td><td>0.02 (-12.41%)</td><td>0.01 <b>(-47.10%)</b></td><td>0.01 <b>(+102.08%)</b></td><td>363.00 <b>(+88.96%)</b></td><td>220.00 <b>(+31.70%)</b></td><td>186.80 (+14.18%)</td><td>161.50 (+9.71%)</td><td>83.77 <b>(+324.65%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>167.04 (n/a)</td><td>163.60 (n/a)</td><td>147.20 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-2.85%)</td><td>0.03 (-0.61%)</td><td>0.03 (-5.33%)</td><td>0.02 (+0.35%)</td><td>0.00 (+7.27%)</td><td>218.70 (-0.36%)</td><td>185.72 (+0.87%)</td><td>184.20 (+5.62%)</td><td>157.30 (+2.95%)</td><td>28.84 (+7.17%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>184.12 (n/a)</td><td>174.40 (n/a)</td><td>152.80 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(-22.21%)</b></td><td>0.02 (-8.63%)</td><td>0.02 (-5.66%)</td><td>0.02 (-14.47%)</td><td>0.00 <b>(-33.90%)</b></td><td>240.50 (+16.92%)</td><td>193.68 (+8.15%)</td><td>195.70 (+6.01%)</td><td>157.20 <b>(+28.54%)</b></td><td>33.68 (+0.55%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>179.08 (n/a)</td><td>184.60 (n/a)</td><td>122.30 (n/a)</td><td>33.49 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (+14.04%)</td><td>0.02 <b>(+28.58%)</b></td><td>0.02 <b>(+27.60%)</b></td><td>0.02 <b>(+58.47%)</b></td><td>0.00 <b>(-40.75%)</b></td><td>209.80 <b>(-36.88%)</b></td><td>189.00 <b>(-25.85%)</b></td><td>195.20 <b>(-21.64%)</b></td><td>153.50 (-12.34%)</td><td>21.15 <b>(-68.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>332.40 (n/a)</td><td>254.88 (n/a)</td><td>249.10 (n/a)</td><td>175.10 (n/a)</td><td>67.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (-1.39%)</td><td>0.02 (-4.04%)</td><td>0.02 (-5.58%)</td><td>0.02 (-12.66%)</td><td>0.00 <b>(+38.03%)</b></td><td>236.90 (+14.50%)</td><td>194.24 (+5.54%)</td><td>191.90 (+5.91%)</td><td>159.50 (+1.40%)</td><td>33.62 <b>(+55.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.90 (n/a)</td><td>184.04 (n/a)</td><td>181.20 (n/a)</td><td>157.30 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 <b>(+20.60%)</b></td><td>0.02 (+1.34%)</td><td>0.02 (-9.09%)</td><td>0.01 (-7.34%)</td><td>0.01 <b>(+24.34%)</b></td><td>339.00 (+7.93%)</td><td>223.20 (+0.69%)</td><td>204.80 (+9.99%)</td><td>149.10 (-17.07%)</td><td>70.06 (+18.83%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>314.10 (n/a)</td><td>221.68 (n/a)</td><td>186.20 (n/a)</td><td>179.80 (n/a)</td><td>58.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (-3.38%)</td><td>0.02 (+0.06%)</td><td>0.02 (+5.18%)</td><td>0.02 (+16.03%)</td><td>0.00 <b>(-36.73%)</b></td><td>227.00 (-13.82%)</td><td>204.30 (-1.52%)</td><td>198.20 (-4.94%)</td><td>179.50 (+3.52%)</td><td>21.58 <b>(-41.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>263.40 (n/a)</td><td>207.46 (n/a)</td><td>208.50 (n/a)</td><td>173.40 (n/a)</td><td>36.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+4.96%)</td><td>0.05 (+5.36%)</td><td>0.05 (-4.76%)</td><td>0.05 <b>(+26.72%)</b></td><td>0.01 <b>(-29.10%)</b></td><td>178.90 <b>(-21.09%)</b></td><td>164.32 (-6.96%)</td><td>171.70 (+5.02%)</td><td>132.40 (-4.68%)</td><td>18.81 <b>(-48.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.70 (n/a)</td><td>176.62 (n/a)</td><td>163.50 (n/a)</td><td>138.90 (n/a)</td><td>36.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 <b>(-36.25%)</b></td><td>0.06 <b>(-29.60%)</b></td><td>0.06 <b>(-24.01%)</b></td><td>0.04 <b>(-42.14%)</b></td><td>0.01 <b>(-29.43%)</b></td><td>319.40 <b>(+72.84%)</b></td><td>226.14 <b>(+43.49%)</b></td><td>204.90 <b>(+31.60%)</b></td><td>184.70 <b>(+56.79%)</b></td><td>53.94 <b>(+96.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>184.80 (n/a)</td><td>157.60 (n/a)</td><td>155.70 (n/a)</td><td>117.80 (n/a)</td><td>27.45 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 <b>(-20.99%)</b></td><td>0.05 (+5.63%)</td><td>0.05 (+18.60%)</td><td>0.05 <b>(+37.22%)</b></td><td>0.00 <b>(-79.69%)</b></td><td>172.50 <b>(-27.12%)</b></td><td>164.06 (-9.89%)</td><td>165.60 (-15.68%)</td><td>154.90 <b>(+26.55%)</b></td><td>8.34 <b>(-80.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>182.06 (n/a)</td><td>196.40 (n/a)</td><td>122.40 (n/a)</td><td>43.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 <b>(+23.74%)</b></td><td>0.06 (+9.54%)</td><td>0.06 (+3.24%)</td><td>0.04 (-7.48%)</td><td>0.02 <b>(+92.25%)</b></td><td>230.60 (+8.06%)</td><td>172.34 (-5.53%)</td><td>177.50 (-3.11%)</td><td>120.50 (-19.24%)</td><td>42.79 <b>(+65.91%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>182.42 (n/a)</td><td>183.20 (n/a)</td><td>149.20 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+15.10%)</td><td>0.05 <b>(+24.36%)</b></td><td>0.05 <b>(+29.06%)</b></td><td>0.04 (+10.80%)</td><td>0.01 (+7.23%)</td><td>213.30 (-9.73%)</td><td>162.22 (-19.83%)</td><td>159.90 <b>(-22.53%)</b></td><td>127.80 (-13.12%)</td><td>31.79 (-15.38%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>202.34 (n/a)</td><td>206.40 (n/a)</td><td>147.10 (n/a)</td><td>37.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 <b>(+28.37%)</b></td><td>0.06 (+15.56%)</td><td>0.06 (+10.60%)</td><td>0.06 (+18.27%)</td><td>0.01 <b>(+36.92%)</b></td><td>183.70 (-15.42%)</td><td>162.16 (-13.22%)</td><td>166.70 (-9.60%)</td><td>126.10 <b>(-22.06%)</b></td><td>21.66 (-11.95%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>186.86 (n/a)</td><td>184.40 (n/a)</td><td>161.80 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (-5.80%)</td><td>0.05 (+3.67%)</td><td>0.05 (+0.72%)</td><td>0.04 (+14.70%)</td><td>0.00 <b>(-48.75%)</b></td><td>190.00 (-12.80%)</td><td>172.44 (-4.71%)</td><td>173.70 (-0.69%)</td><td>157.60 (+6.20%)</td><td>12.29 <b>(-52.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>180.96 (n/a)</td><td>174.90 (n/a)</td><td>148.40 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (+0.70%)</td><td>0.05 (+6.93%)</td><td>0.05 (+8.09%)</td><td>0.04 (+17.71%)</td><td>0.01 <b>(-23.78%)</b></td><td>207.70 (-15.05%)</td><td>179.08 (-7.77%)</td><td>169.80 (-7.47%)</td><td>152.90 (-0.71%)</td><td>23.70 <b>(-35.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>244.50 (n/a)</td><td>194.16 (n/a)</td><td>183.50 (n/a)</td><td>154.00 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (+0.27%)</td><td>0.05 (+8.44%)</td><td>0.05 (+17.35%)</td><td>0.04 (+5.81%)</td><td>0.01 (-11.66%)</td><td>200.00 (-5.48%)</td><td>171.94 (-8.09%)</td><td>165.00 (-14.82%)</td><td>149.90 (-0.33%)</td><td>19.61 (-13.80%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>187.08 (n/a)</td><td>193.70 (n/a)</td><td>150.40 (n/a)</td><td>22.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 <b>(+21.74%)</b></td><td>0.05 (+5.43%)</td><td>0.05 (+1.71%)</td><td>0.04 (-2.52%)</td><td>0.01 <b>(+74.19%)</b></td><td>227.50 (+2.62%)</td><td>180.70 (-2.59%)</td><td>189.70 (-1.71%)</td><td>125.40 (-17.88%)</td><td>40.30 <b>(+47.04%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>185.50 (n/a)</td><td>193.00 (n/a)</td><td>152.70 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (-3.41%)</td><td>0.04 (-11.50%)</td><td>0.04 (-13.50%)</td><td>0.04 (-11.10%)</td><td>0.01 (+17.30%)</td><td>228.20 (+12.47%)</td><td>200.02 (+14.11%)</td><td>214.00 (+15.61%)</td><td>144.40 (+3.51%)</td><td>33.35 <b>(+35.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>175.28 (n/a)</td><td>185.10 (n/a)</td><td>139.50 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 <b>(+94.81%)</b></td><td>0.05 <b>(+46.18%)</b></td><td>0.05 <b>(+26.18%)</b></td><td>0.04 <b>(+57.07%)</b></td><td>0.02 <b>(+162.10%)</b></td><td>207.50 <b>(-36.33%)</b></td><td>170.90 <b>(-29.43%)</b></td><td>174.90 <b>(-20.75%)</b></td><td>105.20 <b>(-48.66%)</b></td><td>40.50 (-18.05%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>325.90 (n/a)</td><td>242.18 (n/a)</td><td>220.70 (n/a)</td><td>204.90 (n/a)</td><td>49.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (-0.37%)</td><td>0.04 (+12.78%)</td><td>0.05 (+15.47%)</td><td>0.04 <b>(+20.07%)</b></td><td>0.01 <b>(-29.87%)</b></td><td>231.90 (-16.70%)</td><td>186.74 (-13.36%)</td><td>178.10 (-13.38%)</td><td>154.80 (+0.39%)</td><td>28.42 <b>(-40.40%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.40 (n/a)</td><td>215.54 (n/a)</td><td>205.60 (n/a)</td><td>154.20 (n/a)</td><td>47.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (-7.86%)</td><td>0.04 (+2.57%)</td><td>0.04 (-2.47%)</td><td>0.04 <b>(+41.39%)</b></td><td>0.00 <b>(-66.04%)</b></td><td>208.20 <b>(-29.28%)</b></td><td>194.46 (-6.00%)</td><td>194.80 (+2.53%)</td><td>176.10 (+8.57%)</td><td>12.64 <b>(-75.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>294.40 (n/a)</td><td>206.88 (n/a)</td><td>190.00 (n/a)</td><td>162.20 (n/a)</td><td>51.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 <b>(+24.14%)</b></td><td>0.04 (+4.55%)</td><td>0.04 (+2.27%)</td><td>0.03 (-2.52%)</td><td>0.01 <b>(+99.05%)</b></td><td>241.90 (+2.59%)</td><td>208.84 (-2.62%)</td><td>220.70 (-2.22%)</td><td>152.10 (-19.44%)</td><td>34.46 <b>(+60.57%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.80 (n/a)</td><td>214.46 (n/a)</td><td>225.70 (n/a)</td><td>188.80 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+7.08%)</td><td>0.10 (+8.57%)</td><td>0.09 (+9.08%)</td><td>0.07 (+10.67%)</td><td>0.03 <b>(+22.71%)</b></td><td>222.10 (-9.64%)</td><td>171.82 (-6.69%)</td><td>176.10 (-8.33%)</td><td>123.00 (-6.61%)</td><td>46.14 (+3.06%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.80 (n/a)</td><td>184.14 (n/a)</td><td>192.10 (n/a)</td><td>131.70 (n/a)</td><td>44.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (+13.83%)</td><td>0.15 (+13.86%)</td><td>0.14 (+1.75%)</td><td>0.13 <b>(+33.48%)</b></td><td>0.03 (-14.61%)</td><td>191.90 <b>(-25.10%)</b></td><td>167.98 (-14.16%)</td><td>175.00 (-1.74%)</td><td>130.40 (-12.19%)</td><td>26.24 <b>(-43.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>256.20 (n/a)</td><td>195.70 (n/a)</td><td>178.10 (n/a)</td><td>148.50 (n/a)</td><td>46.81 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+11.52%)</td><td>0.11 <b>(+34.86%)</b></td><td>0.11 <b>(+32.58%)</b></td><td>0.08 <b>(+56.87%)</b></td><td>0.02 <b>(-23.31%)</b></td><td>200.20 <b>(-36.26%)</b></td><td>154.64 <b>(-29.14%)</b></td><td>151.00 <b>(-24.61%)</b></td><td>127.30 (-10.35%)</td><td>28.49 <b>(-56.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>314.10 (n/a)</td><td>218.24 (n/a)</td><td>200.30 (n/a)</td><td>142.00 (n/a)</td><td>64.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 <b>(+33.71%)</b></td><td>0.13 <b>(+20.23%)</b></td><td>0.12 (+17.51%)</td><td>0.08 (-8.73%)</td><td>0.03 <b>(+152.28%)</b></td><td>241.90 (+9.56%)</td><td>165.70 (-12.81%)</td><td>164.50 (-14.86%)</td><td>119.10 <b>(-25.19%)</b></td><td>47.48 <b>(+110.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>190.04 (n/a)</td><td>193.20 (n/a)</td><td>159.20 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (+15.73%)</td><td>0.09 (-4.33%)</td><td>0.08 (-8.16%)</td><td>0.05 <b>(-23.06%)</b></td><td>0.03 <b>(+67.85%)</b></td><td>299.60 <b>(+29.98%)</b></td><td>202.76 (+11.04%)</td><td>207.60 (+8.92%)</td><td>118.60 (-13.56%)</td><td>66.34 <b>(+86.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.50 (n/a)</td><td>182.60 (n/a)</td><td>190.60 (n/a)</td><td>137.20 (n/a)</td><td>35.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 <b>(+21.99%)</b></td><td>0.11 (+5.12%)</td><td>0.10 (+0.48%)</td><td>0.08 (-12.49%)</td><td>0.02 <b>(+139.61%)</b></td><td>253.60 (+14.29%)</td><td>198.76 (-1.79%)</td><td>204.40 (-0.49%)</td><td>142.90 (-18.01%)</td><td>42.77 <b>(+121.67%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>202.38 (n/a)</td><td>205.40 (n/a)</td><td>174.30 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (-1.51%)</td><td>0.10 (+1.59%)</td><td>0.09 (+0.02%)</td><td>0.08 (-7.47%)</td><td>0.02 <b>(+31.33%)</b></td><td>196.50 (+8.03%)</td><td>164.94 (-0.21%)</td><td>176.20 (+0.00%)</td><td>130.60 (+1.48%)</td><td>30.98 <b>(+43.09%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.90 (n/a)</td><td>165.28 (n/a)</td><td>176.20 (n/a)</td><td>128.70 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+16.46%)</td><td>0.10 (+15.06%)</td><td>0.10 (+12.92%)</td><td>0.08 <b>(+50.05%)</b></td><td>0.02 (-16.13%)</td><td>217.10 <b>(-33.36%)</b></td><td>181.10 (-16.04%)</td><td>180.60 (-11.43%)</td><td>140.30 (-14.14%)</td><td>29.73 <b>(-53.85%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>325.80 (n/a)</td><td>215.70 (n/a)</td><td>203.90 (n/a)</td><td>163.40 (n/a)</td><td>64.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (-6.22%)</td><td>0.10 (-6.17%)</td><td>0.09 (-12.03%)</td><td>0.07 <b>(-21.90%)</b></td><td>0.02 <b>(+20.17%)</b></td><td>245.60 <b>(+28.05%)</b></td><td>179.36 (+9.01%)</td><td>183.80 (+13.67%)</td><td>131.20 (+6.58%)</td><td>44.31 <b>(+64.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.80 (n/a)</td><td>164.54 (n/a)</td><td>161.70 (n/a)</td><td>123.10 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (+12.60%)</td><td>0.11 <b>(+21.26%)</b></td><td>0.11 (+13.02%)</td><td>0.10 <b>(+65.41%)</b></td><td>0.01 <b>(-37.32%)</b></td><td>191.40 <b>(-39.55%)</b></td><td>166.74 <b>(-21.05%)</b></td><td>169.10 (-11.56%)</td><td>139.30 (-11.16%)</td><td>19.38 <b>(-68.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>316.60 (n/a)</td><td>211.20 (n/a)</td><td>191.20 (n/a)</td><td>156.80 (n/a)</td><td>61.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (+19.83%)</td><td>0.09 (-4.81%)</td><td>0.08 (-11.95%)</td><td>0.07 (-10.54%)</td><td>0.02 <b>(+112.65%)</b></td><td>244.90 (+11.78%)</td><td>197.30 (+9.30%)</td><td>199.50 (+13.61%)</td><td>133.70 (-16.54%)</td><td>47.71 <b>(+102.30%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>180.52 (n/a)</td><td>175.60 (n/a)</td><td>160.20 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 <b>(+34.46%)</b></td><td>0.09 (+10.47%)</td><td>0.10 (+17.29%)</td><td>0.05 <b>(-24.50%)</b></td><td>0.03 <b>(+157.06%)</b></td><td>327.50 <b>(+32.43%)</b></td><td>212.14 (-1.35%)</td><td>180.60 (-14.73%)</td><td>126.60 <b>(-25.62%)</b></td><td>77.26 <b>(+159.01%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>247.30 (n/a)</td><td>215.04 (n/a)</td><td>211.80 (n/a)</td><td>170.20 (n/a)</td><td>29.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (+14.19%)</td><td>0.10 (+13.17%)</td><td>0.10 (+19.91%)</td><td>0.08 <b>(+27.89%)</b></td><td>0.02 (+5.97%)</td><td>201.20 <b>(-21.83%)</b></td><td>168.60 (-12.23%)</td><td>162.00 (-16.62%)</td><td>133.50 (-12.40%)</td><td>30.69 <b>(-25.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>257.40 (n/a)</td><td>192.10 (n/a)</td><td>194.30 (n/a)</td><td>152.40 (n/a)</td><td>41.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (+12.54%)</td><td>0.09 (+15.60%)</td><td>0.09 (+8.51%)</td><td>0.09 <b>(+31.12%)</b></td><td>0.00 <b>(-43.09%)</b></td><td>191.10 <b>(-23.74%)</b></td><td>184.74 (-14.08%)</td><td>189.50 (-7.83%)</td><td>170.10 (-11.13%)</td><td>8.84 <b>(-61.85%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.60 (n/a)</td><td>215.02 (n/a)</td><td>205.60 (n/a)</td><td>191.40 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (+8.03%)</td><td>0.07 (-3.87%)</td><td>0.07 (-13.55%)</td><td>0.05 (+6.99%)</td><td>0.02 (+4.61%)</td><td>305.20 (-6.52%)</td><td>237.64 (+3.51%)</td><td>240.40 (+15.69%)</td><td>165.80 (-7.43%)</td><td>49.54 (-14.82%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>326.50 (n/a)</td><td>229.58 (n/a)</td><td>207.80 (n/a)</td><td>179.10 (n/a)</td><td>58.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (-16.99%)</td><td>0.17 (-13.05%)</td><td>0.17 (-19.30%)</td><td>0.15 (+4.18%)</td><td>0.02 <b>(-52.54%)</b></td><td>212.30 (-4.02%)</td><td>189.38 (+12.55%)</td><td>194.90 <b>(+23.90%)</b></td><td>166.90 <b>(+20.51%)</b></td><td>18.45 <b>(-45.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.20 (n/a)</td><td>168.26 (n/a)</td><td>157.30 (n/a)</td><td>138.50 (n/a)</td><td>33.86 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (+10.67%)</td><td>0.20 (+7.09%)</td><td>0.17 (-8.08%)</td><td>0.15 (+3.34%)</td><td>0.05 <b>(+40.92%)</b></td><td>217.50 (-3.25%)</td><td>171.32 (-4.60%)</td><td>190.40 (+8.74%)</td><td>121.40 (-9.61%)</td><td>41.79 <b>(+20.65%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.80 (n/a)</td><td>179.58 (n/a)</td><td>175.10 (n/a)</td><td>134.30 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (+19.26%)</td><td>0.24 (+9.23%)</td><td>0.23 (+2.55%)</td><td>0.21 (+6.86%)</td><td>0.03 <b>(+94.49%)</b></td><td>193.80 (-6.42%)</td><td>174.62 (-7.86%)</td><td>177.80 (-2.52%)</td><td>149.90 (-16.12%)</td><td>18.91 <b>(+53.75%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>189.52 (n/a)</td><td>182.40 (n/a)</td><td>178.70 (n/a)</td><td>12.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 <b>(-23.41%)</b></td><td>0.16 (-14.65%)</td><td>0.17 (-4.67%)</td><td>0.11 <b>(+32.70%)</b></td><td>0.04 <b>(-52.17%)</b></td><td>288.30 <b>(-24.65%)</b></td><td>213.38 (+3.47%)</td><td>189.20 (+4.94%)</td><td>163.20 <b>(+30.56%)</b></td><td>52.09 <b>(-50.85%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>382.60 (n/a)</td><td>206.22 (n/a)</td><td>180.30 (n/a)</td><td>125.00 (n/a)</td><td>105.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (-3.82%)</td><td>0.22 (+0.30%)</td><td>0.21 (+1.73%)</td><td>0.20 (+11.60%)</td><td>0.01 <b>(-52.50%)</b></td><td>201.90 (-10.39%)</td><td>189.80 (-1.28%)</td><td>192.30 (-1.74%)</td><td>172.70 (+3.97%)</td><td>10.69 <b>(-55.67%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>225.30 (n/a)</td><td>192.26 (n/a)</td><td>195.70 (n/a)</td><td>166.10 (n/a)</td><td>24.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (-1.28%)</td><td>0.16 (-4.94%)</td><td>0.15 (-7.91%)</td><td>0.13 (-0.00%)</td><td>0.03 (+7.72%)</td><td>247.90 (+0.04%)</td><td>209.80 (+5.76%)</td><td>223.40 (+8.60%)</td><td>159.00 (+1.27%)</td><td>40.13 (+11.66%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>247.80 (n/a)</td><td>198.38 (n/a)</td><td>205.70 (n/a)</td><td>157.00 (n/a)</td><td>35.94 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (+1.39%)</td><td>0.21 (-2.18%)</td><td>0.20 (+0.99%)</td><td>0.17 (-9.87%)</td><td>0.06 (+18.88%)</td><td>219.60 (+10.97%)</td><td>182.66 (+4.01%)</td><td>185.70 (-1.01%)</td><td>121.50 (-1.38%)</td><td>40.66 <b>(+35.38%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>197.90 (n/a)</td><td>175.62 (n/a)</td><td>187.60 (n/a)</td><td>123.20 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 <b>(-27.42%)</b></td><td>0.18 (-2.69%)</td><td>0.18 (+5.51%)</td><td>0.17 <b>(+23.38%)</b></td><td>0.01 <b>(-79.73%)</b></td><td>197.60 (-18.98%)</td><td>186.46 (-2.10%)</td><td>185.00 (-5.23%)</td><td>171.30 <b>(+37.81%)</b></td><td>10.39 <b>(-76.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>243.90 (n/a)</td><td>190.46 (n/a)</td><td>195.20 (n/a)</td><td>124.30 (n/a)</td><td>44.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (-11.00%)</td><td>0.19 (-10.16%)</td><td>0.19 (-6.17%)</td><td>0.15 (-14.97%)</td><td>0.03 (-14.43%)</td><td>240.40 (+17.61%)</td><td>195.86 (+11.28%)</td><td>191.90 (+6.55%)</td><td>165.10 (+12.39%)</td><td>27.99 (+15.76%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>204.40 (n/a)</td><td>176.00 (n/a)</td><td>180.10 (n/a)</td><td>146.90 (n/a)</td><td>24.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (-1.20%)</td><td>0.18 (-2.83%)</td><td>0.17 (+3.64%)</td><td>0.16 (+2.78%)</td><td>0.02 <b>(-31.53%)</b></td><td>206.60 (-2.68%)</td><td>188.26 (+1.62%)</td><td>193.10 (-3.50%)</td><td>153.30 (+1.25%)</td><td>20.57 <b>(-33.31%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.30 (n/a)</td><td>185.26 (n/a)</td><td>200.10 (n/a)</td><td>151.40 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (+6.76%)</td><td>0.18 (-4.99%)</td><td>0.18 (-8.32%)</td><td>0.14 (-14.11%)</td><td>0.03 <b>(+97.08%)</b></td><td>250.00 (+16.44%)</td><td>199.20 (+7.10%)</td><td>198.30 (+9.08%)</td><td>164.20 (-6.33%)</td><td>34.50 <b>(+110.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>186.00 (n/a)</td><td>181.80 (n/a)</td><td>175.30 (n/a)</td><td>16.37 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (-0.46%)</td><td>0.18 (+11.42%)</td><td>0.17 (+4.98%)</td><td>0.16 <b>(+62.23%)</b></td><td>0.02 <b>(-54.29%)</b></td><td>203.70 <b>(-38.35%)</b></td><td>183.18 (-15.95%)</td><td>193.50 (-4.77%)</td><td>158.50 (+0.44%)</td><td>20.74 <b>(-70.98%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>330.40 (n/a)</td><td>217.94 (n/a)</td><td>203.20 (n/a)</td><td>157.80 (n/a)</td><td>71.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (+2.27%)</td><td>0.18 (+4.66%)</td><td>0.20 (+16.60%)</td><td>0.15 (-5.96%)</td><td>0.03 <b>(+73.32%)</b></td><td>234.40 (+6.35%)</td><td>195.48 (-3.12%)</td><td>174.60 (-14.24%)</td><td>170.80 (-2.18%)</td><td>31.82 <b>(+80.19%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>220.40 (n/a)</td><td>201.78 (n/a)</td><td>203.60 (n/a)</td><td>174.60 (n/a)</td><td>17.66 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (-6.32%)</td><td>0.15 (+5.94%)</td><td>0.15 (-1.74%)</td><td>0.14 <b>(+50.25%)</b></td><td>0.01 <b>(-58.53%)</b></td><td>235.50 <b>(-33.44%)</b></td><td>214.02 (-10.12%)</td><td>216.80 (+1.78%)</td><td>185.30 (+6.74%)</td><td>19.20 <b>(-72.09%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>353.80 (n/a)</td><td>238.12 (n/a)</td><td>213.00 (n/a)</td><td>173.60 (n/a)</td><td>68.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (-5.93%)</td><td>0.14 (+10.83%)</td><td>0.14 (+15.62%)</td><td>0.12 (+13.40%)</td><td>0.02 <b>(-33.92%)</b></td><td>174.70 (-11.81%)</td><td>146.82 (-10.99%)</td><td>146.90 (-13.49%)</td><td>131.30 (+6.32%)</td><td>17.29 <b>(-36.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>198.10 (n/a)</td><td>164.94 (n/a)</td><td>169.80 (n/a)</td><td>123.50 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (+14.18%)</td><td>0.13 (+10.49%)</td><td>0.14 <b>(+26.65%)</b></td><td>0.08 (-16.35%)</td><td>0.03 <b>(+109.08%)</b></td><td>247.40 (+19.52%)</td><td>170.60 (-5.55%)</td><td>144.70 <b>(-21.02%)</b></td><td>131.40 (-12.40%)</td><td>48.22 <b>(+120.78%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>180.62 (n/a)</td><td>183.20 (n/a)</td><td>150.00 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (-3.81%)</td><td>0.12 (-6.38%)</td><td>0.12 (-5.96%)</td><td>0.10 (-8.73%)</td><td>0.02 (+6.02%)</td><td>215.20 (+9.57%)</td><td>174.36 (+7.21%)</td><td>168.60 (+6.37%)</td><td>145.50 (+3.93%)</td><td>25.93 <b>(+21.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>196.40 (n/a)</td><td>162.64 (n/a)</td><td>158.50 (n/a)</td><td>140.00 (n/a)</td><td>21.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (-17.93%)</td><td>0.11 (-12.60%)</td><td>0.11 (-16.50%)</td><td>0.10 (-8.71%)</td><td>0.01 <b>(-39.35%)</b></td><td>210.80 (+9.56%)</td><td>185.54 (+13.59%)</td><td>183.90 (+19.73%)</td><td>169.50 <b>(+21.85%)</b></td><td>17.34 <b>(-20.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>163.34 (n/a)</td><td>153.60 (n/a)</td><td>139.10 (n/a)</td><td>21.88 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (+13.17%)</td><td>0.15 (+13.80%)</td><td>0.14 (+8.87%)</td><td>0.11 (+4.62%)</td><td>0.02 <b>(+40.61%)</b></td><td>178.10 (-4.45%)</td><td>143.26 (-11.45%)</td><td>145.30 (-8.15%)</td><td>120.90 (-11.62%)</td><td>23.59 (+14.52%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>161.78 (n/a)</td><td>158.20 (n/a)</td><td>136.80 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (-13.38%)</td><td>0.12 (-12.80%)</td><td>0.11 (-15.35%)</td><td>0.10 (-9.06%)</td><td>0.01 <b>(-35.70%)</b></td><td>195.80 (+9.94%)</td><td>177.56 (+13.91%)</td><td>181.30 (+18.11%)</td><td>153.60 (+15.49%)</td><td>16.40 <b>(-20.04%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>178.10 (n/a)</td><td>155.88 (n/a)</td><td>153.50 (n/a)</td><td>133.00 (n/a)</td><td>20.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 <b>(+26.80%)</b></td><td>0.12 (+9.85%)</td><td>0.12 (+9.81%)</td><td>0.08 (-13.08%)</td><td>0.03 <b>(+99.86%)</b></td><td>264.10 (+15.03%)</td><td>187.80 (-5.41%)</td><td>176.60 (-8.97%)</td><td>131.00 <b>(-21.13%)</b></td><td>50.07 <b>(+80.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>198.54 (n/a)</td><td>194.00 (n/a)</td><td>166.10 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 <b>(+43.50%)</b></td><td>0.14 (+15.39%)</td><td>0.13 (+5.33%)</td><td>0.11 <b>(+22.19%)</b></td><td>0.03 <b>(+82.08%)</b></td><td>189.20 (-18.17%)</td><td>156.58 (-11.94%)</td><td>161.50 (-5.11%)</td><td>108.00 <b>(-30.32%)</b></td><td>30.64 (-1.30%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>231.20 (n/a)</td><td>177.82 (n/a)</td><td>170.20 (n/a)</td><td>155.00 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (+10.68%)</td><td>0.17 (+11.87%)</td><td>0.16 (+6.78%)</td><td>0.15 <b>(+22.48%)</b></td><td>0.02 (-4.36%)</td><td>167.10 (-18.37%)</td><td>148.82 (-11.10%)</td><td>154.40 (-6.37%)</td><td>124.60 (-9.64%)</td><td>16.72 <b>(-30.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>167.40 (n/a)</td><td>164.90 (n/a)</td><td>137.90 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (+14.56%)</td><td>0.16 (+7.87%)</td><td>0.16 (+16.91%)</td><td>0.13 (+4.16%)</td><td>0.03 <b>(+56.59%)</b></td><td>194.50 (-4.00%)</td><td>162.34 (-5.99%)</td><td>151.50 (-14.46%)</td><td>131.50 (-12.74%)</td><td>29.71 <b>(+38.38%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.60 (n/a)</td><td>172.68 (n/a)</td><td>177.10 (n/a)</td><td>150.70 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (+10.46%)</td><td>0.15 (+18.51%)</td><td>0.16 <b>(+23.15%)</b></td><td>0.13 <b>(+59.15%)</b></td><td>0.02 <b>(-41.37%)</b></td><td>182.70 <b>(-37.15%)</b></td><td>161.70 (-19.12%)</td><td>156.50 (-18.83%)</td><td>136.80 (-9.46%)</td><td>18.53 <b>(-66.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>290.70 (n/a)</td><td>199.92 (n/a)</td><td>192.80 (n/a)</td><td>151.10 (n/a)</td><td>55.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (+14.77%)</td><td>0.15 (+3.37%)</td><td>0.15 (+2.24%)</td><td>0.10 (-4.05%)</td><td>0.04 <b>(+35.42%)</b></td><td>250.20 (+4.25%)</td><td>173.16 (-1.29%)</td><td>166.20 (-2.18%)</td><td>123.60 (-12.90%)</td><td>47.12 <b>(+23.21%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>240.00 (n/a)</td><td>175.42 (n/a)</td><td>169.90 (n/a)</td><td>141.90 (n/a)</td><td>38.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (+3.11%)</td><td>0.16 (-4.24%)</td><td>0.15 (-3.59%)</td><td>0.12 (-13.54%)</td><td>0.04 <b>(+45.22%)</b></td><td>207.50 (+15.66%)</td><td>164.92 (+6.91%)</td><td>163.10 (+3.75%)</td><td>121.10 (-3.04%)</td><td>36.45 <b>(+64.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>179.40 (n/a)</td><td>154.26 (n/a)</td><td>157.20 (n/a)</td><td>124.90 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (-7.79%)</td><td>0.16 (+6.78%)</td><td>0.15 (+0.53%)</td><td>0.14 (+19.14%)</td><td>0.02 <b>(-36.97%)</b></td><td>177.00 (-16.03%)</td><td>157.78 (-7.95%)</td><td>166.10 (-0.48%)</td><td>138.80 (+8.44%)</td><td>17.44 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>210.80 (n/a)</td><td>171.40 (n/a)</td><td>166.90 (n/a)</td><td>128.00 (n/a)</td><td>30.66 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (-10.16%)</td><td>0.14 (-5.82%)</td><td>0.15 (+6.28%)</td><td>0.11 (-11.16%)</td><td>0.02 <b>(-25.86%)</b></td><td>220.90 (+12.59%)</td><td>178.90 (+5.50%)</td><td>166.80 (-5.87%)</td><td>155.00 (+11.27%)</td><td>26.06 (-4.89%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>196.20 (n/a)</td><td>169.58 (n/a)</td><td>177.20 (n/a)</td><td>139.30 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (+12.56%)</td><td>0.13 (-2.71%)</td><td>0.13 (-6.63%)</td><td>0.10 (-19.40%)</td><td>0.02 <b>(+157.35%)</b></td><td>251.10 <b>(+24.06%)</b></td><td>191.66 (+5.34%)</td><td>190.20 (+7.09%)</td><td>149.30 (-11.18%)</td><td>37.50 <b>(+186.46%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>181.94 (n/a)</td><td>177.60 (n/a)</td><td>168.10 (n/a)</td><td>13.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (-7.59%)</td><td>0.11 (+2.66%)</td><td>0.10 (-10.97%)</td><td>0.09 <b>(+78.57%)</b></td><td>0.02 <b>(-52.34%)</b></td><td>204.00 <b>(-44.00%)</b></td><td>173.58 (-12.88%)</td><td>178.10 (+12.30%)</td><td>137.60 (+8.26%)</td><td>24.98 <b>(-73.65%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>364.30 (n/a)</td><td>199.24 (n/a)</td><td>158.60 (n/a)</td><td>127.10 (n/a)</td><td>94.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (-6.13%)</td><td>0.12 (-1.52%)</td><td>0.12 (+5.95%)</td><td>0.11 (-3.29%)</td><td>0.01 <b>(-33.50%)</b></td><td>173.60 (+3.39%)</td><td>153.48 (+0.84%)</td><td>153.40 (-5.60%)</td><td>135.20 (+6.54%)</td><td>13.86 <b>(-27.58%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>167.90 (n/a)</td><td>152.20 (n/a)</td><td>162.50 (n/a)</td><td>126.90 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (+10.87%)</td><td>0.13 (+12.20%)</td><td>0.14 (+8.64%)</td><td>0.10 <b>(+30.54%)</b></td><td>0.02 (-19.61%)</td><td>176.70 <b>(-23.37%)</b></td><td>142.90 (-13.10%)</td><td>133.40 (-7.94%)</td><td>115.40 (-9.77%)</td><td>23.71 <b>(-44.08%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>230.60 (n/a)</td><td>164.44 (n/a)</td><td>144.90 (n/a)</td><td>127.90 (n/a)</td><td>42.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 <b>(-25.48%)</b></td><td>0.10 (-14.57%)</td><td>0.11 (-2.05%)</td><td>0.08 (-17.51%)</td><td>0.01 <b>(-34.64%)</b></td><td>229.40 <b>(+21.25%)</b></td><td>186.82 (+16.38%)</td><td>171.00 (+2.09%)</td><td>168.70 <b>(+34.21%)</b></td><td>25.97 (+7.18%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>160.52 (n/a)</td><td>167.50 (n/a)</td><td>125.70 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (-10.16%)</td><td>0.11 (+0.80%)</td><td>0.12 (+8.23%)</td><td>0.10 (+13.13%)</td><td>0.01 <b>(-39.52%)</b></td><td>189.60 (-11.61%)</td><td>166.78 (-2.51%)</td><td>156.60 (-7.61%)</td><td>147.50 (+11.32%)</td><td>19.24 <b>(-39.58%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>214.50 (n/a)</td><td>171.08 (n/a)</td><td>169.50 (n/a)</td><td>132.50 (n/a)</td><td>31.84 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 <b>(+26.70%)</b></td><td>0.12 (+3.83%)</td><td>0.11 (-0.75%)</td><td>0.09 (-10.15%)</td><td>0.02 <b>(+196.69%)</b></td><td>198.60 (+11.32%)</td><td>164.10 (-1.45%)</td><td>167.50 (+0.72%)</td><td>120.90 <b>(-21.08%)</b></td><td>28.24 <b>(+151.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>166.52 (n/a)</td><td>166.30 (n/a)</td><td>153.20 (n/a)</td><td>11.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (-2.88%)</td><td>0.10 (-8.91%)</td><td>0.09 (-16.74%)</td><td>0.09 (-0.39%)</td><td>0.01 (-5.65%)</td><td>214.70 (+0.37%)</td><td>193.98 (+9.63%)</td><td>202.00 <b>(+20.10%)</b></td><td>155.50 (+2.98%)</td><td>23.56 (-4.73%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>176.94 (n/a)</td><td>168.20 (n/a)</td><td>151.00 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (-3.42%)</td><td>0.10 (-5.95%)</td><td>0.10 (-12.85%)</td><td>0.08 (+11.77%)</td><td>0.01 <b>(-33.33%)</b></td><td>231.20 (-10.53%)</td><td>187.58 (+3.97%)</td><td>183.80 (+14.80%)</td><td>156.20 (+3.58%)</td><td>27.12 <b>(-38.99%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>258.40 (n/a)</td><td>180.42 (n/a)</td><td>160.10 (n/a)</td><td>150.80 (n/a)</td><td>44.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.74 (+10.93%)</td><td>0.65 (+8.99%)</td><td>0.64 (+7.02%)</td><td>0.57 (+10.16%)</td><td>0.06 (+2.65%)</td><td>172.70 (-9.25%)</td><td>153.14 (-8.37%)</td><td>154.50 (-6.59%)</td><td>133.20 (-9.82%)</td><td>14.31 (-16.53%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.67 (n/a)</td><td>0.59 (n/a)</td><td>0.59 (n/a)</td><td>0.52 (n/a)</td><td>0.06 (n/a)</td><td>190.30 (n/a)</td><td>167.12 (n/a)</td><td>165.40 (n/a)</td><td>147.70 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.76 (+4.35%)</td><td>0.63 (+4.25%)</td><td>0.64 (+5.74%)</td><td>0.47 (-1.16%)</td><td>0.11 (+13.91%)</td><td>209.20 (+1.16%)</td><td>159.70 (-3.55%)</td><td>154.20 (-5.40%)</td><td>129.10 (-4.16%)</td><td>29.84 (+12.52%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.73 (n/a)</td><td>0.61 (n/a)</td><td>0.60 (n/a)</td><td>0.48 (n/a)</td><td>0.09 (n/a)</td><td>206.80 (n/a)</td><td>165.58 (n/a)</td><td>163.00 (n/a)</td><td>134.70 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.79 (+1.45%)</td><td>0.63 (+2.46%)</td><td>0.60 (+3.73%)</td><td>0.53 (+2.94%)</td><td>0.11 (+4.64%)</td><td>184.90 (-2.89%)</td><td>158.72 (-2.28%)</td><td>163.10 (-3.61%)</td><td>124.60 (-1.50%)</td><td>25.44 (+2.10%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.78 (n/a)</td><td>0.62 (n/a)</td><td>0.58 (n/a)</td><td>0.52 (n/a)</td><td>0.10 (n/a)</td><td>190.40 (n/a)</td><td>162.42 (n/a)</td><td>169.20 (n/a)</td><td>126.50 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.82 <b>(+26.46%)</b></td><td>0.67 <b>(+27.45%)</b></td><td>0.66 <b>(+32.35%)</b></td><td>0.52 (+17.57%)</td><td>0.11 <b>(+41.56%)</b></td><td>190.60 (-14.95%)</td><td>150.08 <b>(-21.04%)</b></td><td>148.20 <b>(-24.43%)</b></td><td>120.20 <b>(-20.92%)</b></td><td>26.29 (-2.61%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.65 (n/a)</td><td>0.53 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>224.10 (n/a)</td><td>190.08 (n/a)</td><td>196.10 (n/a)</td><td>152.00 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.57 (-0.73%)</td><td>0.45 (-1.87%)</td><td>0.50 (+17.69%)</td><td>0.20 <b>(-49.04%)</b></td><td>0.15 <b>(+111.98%)</b></td><td>364.60 <b>(+96.23%)</b></td><td>190.98 (+15.84%)</td><td>148.50 (-15.00%)</td><td>130.20 (+0.77%)</td><td>98.91 <b>(+335.75%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>185.80 (n/a)</td><td>164.86 (n/a)</td><td>174.70 (n/a)</td><td>129.20 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.51 (-14.74%)</td><td>0.43 (-3.42%)</td><td>0.42 (+0.07%)</td><td>0.31 (+1.59%)</td><td>0.08 <b>(-29.62%)</b></td><td>235.10 (-1.55%)</td><td>178.64 (+1.44%)</td><td>175.70 (-0.06%)</td><td>143.20 (+17.28%)</td><td>35.92 (-17.96%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.60 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>238.80 (n/a)</td><td>176.10 (n/a)</td><td>175.80 (n/a)</td><td>122.10 (n/a)</td><td>43.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.58 <b>(+23.85%)</b></td><td>0.52 <b>(+32.56%)</b></td><td>0.53 <b>(+42.09%)</b></td><td>0.45 <b>(+22.29%)</b></td><td>0.06 <b>(+39.50%)</b></td><td>162.80 (-18.23%)</td><td>142.00 <b>(-24.40%)</b></td><td>138.70 <b>(-29.63%)</b></td><td>126.90 (-19.22%)</td><td>16.20 (-8.33%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.04 (n/a)</td><td>199.10 (n/a)</td><td>187.82 (n/a)</td><td>197.10 (n/a)</td><td>157.10 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.51 (-1.53%)</td><td>0.39 (-9.21%)</td><td>0.37 (-8.25%)</td><td>0.33 (-9.53%)</td><td>0.07 (+15.50%)</td><td>224.10 (+10.50%)</td><td>195.20 (+11.00%)</td><td>200.30 (+9.04%)</td><td>144.70 (+1.62%)</td><td>30.96 <b>(+27.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>202.80 (n/a)</td><td>175.86 (n/a)</td><td>183.70 (n/a)</td><td>142.40 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (+11.76%)</td><td>0.23 (+7.18%)</td><td>0.23 (+12.13%)</td><td>0.19 (+0.79%)</td><td>0.04 <b>(+41.51%)</b></td><td>196.30 (-0.76%)</td><td>166.70 (-5.83%)</td><td>161.20 (-10.84%)</td><td>129.20 (-10.53%)</td><td>26.17 <b>(+27.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>197.80 (n/a)</td><td>177.02 (n/a)</td><td>180.80 (n/a)</td><td>144.40 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (-1.80%)</td><td>0.20 (+0.42%)</td><td>0.20 (+4.24%)</td><td>0.15 (-13.50%)</td><td>0.04 <b>(+32.13%)</b></td><td>250.20 (+15.62%)</td><td>192.02 (+1.01%)</td><td>188.00 (-4.03%)</td><td>158.70 (+1.86%)</td><td>37.59 <b>(+52.96%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>216.40 (n/a)</td><td>190.10 (n/a)</td><td>195.90 (n/a)</td><td>155.80 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (-8.25%)</td><td>0.24 (+2.95%)</td><td>0.24 (-1.27%)</td><td>0.21 <b>(+37.00%)</b></td><td>0.02 <b>(-55.84%)</b></td><td>176.60 <b>(-26.99%)</b></td><td>157.90 (-6.78%)</td><td>155.30 (+1.30%)</td><td>137.00 (+8.99%)</td><td>15.32 <b>(-65.75%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>241.90 (n/a)</td><td>169.38 (n/a)</td><td>153.30 (n/a)</td><td>125.70 (n/a)</td><td>44.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (+5.06%)</td><td>0.24 (+4.81%)</td><td>0.23 (-0.38%)</td><td>0.17 (-4.22%)</td><td>0.05 <b>(+29.84%)</b></td><td>214.60 (+4.38%)</td><td>159.88 (-3.15%)</td><td>160.50 (+0.38%)</td><td>122.90 (-4.80%)</td><td>35.86 <b>(+28.21%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>205.60 (n/a)</td><td>165.08 (n/a)</td><td>159.90 (n/a)</td><td>129.10 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (-13.79%)</td><td>0.21 (-4.25%)</td><td>0.21 (+3.69%)</td><td>0.18 (-10.95%)</td><td>0.02 <b>(-31.45%)</b></td><td>209.20 (+12.29%)</td><td>177.30 (+3.90%)</td><td>173.70 (-3.55%)</td><td>157.80 (+16.03%)</td><td>19.22 (-8.51%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>186.30 (n/a)</td><td>170.64 (n/a)</td><td>180.10 (n/a)</td><td>136.00 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (+7.40%)</td><td>0.21 (+0.20%)</td><td>0.20 (-5.85%)</td><td>0.18 (-7.82%)</td><td>0.03 <b>(+132.99%)</b></td><td>202.80 (+8.45%)</td><td>176.18 (+1.36%)</td><td>185.40 (+6.25%)</td><td>147.70 (-6.93%)</td><td>26.70 <b>(+129.88%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>187.00 (n/a)</td><td>173.82 (n/a)</td><td>174.50 (n/a)</td><td>158.70 (n/a)</td><td>11.62 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (+15.08%)</td><td>0.20 (+8.32%)</td><td>0.21 (+9.11%)</td><td>0.18 (+3.69%)</td><td>0.02 <b>(+74.36%)</b></td><td>204.80 (-3.53%)</td><td>183.82 (-7.24%)</td><td>179.30 (-8.38%)</td><td>161.80 (-13.10%)</td><td>18.24 <b>(+48.38%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>198.16 (n/a)</td><td>195.70 (n/a)</td><td>186.20 (n/a)</td><td>12.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (+15.64%)</td><td>0.21 (+16.67%)</td><td>0.20 (+12.10%)</td><td>0.20 <b>(+26.85%)</b></td><td>0.01 <b>(-42.51%)</b></td><td>184.50 <b>(-21.19%)</b></td><td>178.82 (-14.52%)</td><td>180.90 (-10.80%)</td><td>172.50 (-13.53%)</td><td>5.52 <b>(-61.30%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>234.10 (n/a)</td><td>209.20 (n/a)</td><td>202.80 (n/a)</td><td>199.50 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (-1.22%)</td><td>0.24 (+5.70%)</td><td>0.26 <b>(+21.95%)</b></td><td>0.12 <b>(-39.14%)</b></td><td>0.07 <b>(+78.87%)</b></td><td>332.20 <b>(+64.29%)</b></td><td>186.14 (+3.02%)</td><td>156.00 (-17.98%)</td><td>139.50 (+1.23%)</td><td>81.99 <b>(+218.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>202.20 (n/a)</td><td>180.68 (n/a)</td><td>190.20 (n/a)</td><td>137.80 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 <b>(+26.38%)</b></td><td>0.26 <b>(+22.14%)</b></td><td>0.28 <b>(+25.81%)</b></td><td>0.21 (+7.13%)</td><td>0.03 <b>(+154.60%)</b></td><td>191.90 (-6.66%)</td><td>157.22 (-17.20%)</td><td>147.30 <b>(-20.51%)</b></td><td>139.60 <b>(-20.86%)</b></td><td>21.95 <b>(+86.39%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>189.88 (n/a)</td><td>185.30 (n/a)</td><td>176.40 (n/a)</td><td>11.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.33 (-3.09%)</td><td>0.25 (-9.22%)</td><td>0.25 (-14.58%)</td><td>0.14 (-17.29%)</td><td>0.07 (-3.30%)</td><td>285.00 <b>(+20.92%)</b></td><td>178.34 (+11.69%)</td><td>160.80 (+17.03%)</td><td>125.90 (+3.20%)</td><td>61.89 <b>(+29.55%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>235.70 (n/a)</td><td>159.68 (n/a)</td><td>137.40 (n/a)</td><td>122.00 (n/a)</td><td>47.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (-7.21%)</td><td>0.25 (+2.06%)</td><td>0.26 (-0.06%)</td><td>0.20 <b>(+27.97%)</b></td><td>0.03 <b>(-42.90%)</b></td><td>202.00 <b>(-21.86%)</b></td><td>165.60 (-5.68%)</td><td>160.20 (+0.06%)</td><td>140.10 (+7.77%)</td><td>23.03 <b>(-53.24%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>258.50 (n/a)</td><td>175.58 (n/a)</td><td>160.10 (n/a)</td><td>130.00 (n/a)</td><td>49.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.38 <b>(+57.48%)</b></td><td>0.28 <b>(+37.69%)</b></td><td>0.27 <b>(+20.80%)</b></td><td>0.22 <b>(+103.12%)</b></td><td>0.06 (+18.51%)</td><td>186.70 <b>(-50.76%)</b></td><td>152.44 <b>(-31.02%)</b></td><td>151.20 (-17.24%)</td><td>107.10 <b>(-36.48%)</b></td><td>31.42 <b>(-64.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>379.20 (n/a)</td><td>220.98 (n/a)</td><td>182.70 (n/a)</td><td>168.60 (n/a)</td><td>89.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.32 (+14.81%)</td><td>0.23 (+1.54%)</td><td>0.22 (+6.78%)</td><td>0.16 (-12.71%)</td><td>0.06 <b>(+58.84%)</b></td><td>248.50 (+14.52%)</td><td>190.56 (+1.58%)</td><td>186.90 (-6.32%)</td><td>126.10 (-12.85%)</td><td>46.18 <b>(+56.39%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>217.00 (n/a)</td><td>187.60 (n/a)</td><td>199.50 (n/a)</td><td>144.70 (n/a)</td><td>29.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (-8.81%)</td><td>0.24 (-3.89%)</td><td>0.24 (+4.25%)</td><td>0.15 <b>(-20.97%)</b></td><td>0.05 (+10.41%)</td><td>265.00 <b>(+26.55%)</b></td><td>180.38 (+6.38%)</td><td>167.50 (-4.07%)</td><td>137.30 (+9.66%)</td><td>49.91 <b>(+63.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>209.40 (n/a)</td><td>169.56 (n/a)</td><td>174.60 (n/a)</td><td>125.20 (n/a)</td><td>30.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (+9.28%)</td><td>0.25 (+7.99%)</td><td>0.24 (+11.54%)</td><td>0.21 (+7.04%)</td><td>0.03 (+11.61%)</td><td>192.70 (-6.59%)</td><td>165.68 (-7.33%)</td><td>167.60 (-10.33%)</td><td>138.00 (-8.49%)</td><td>21.08 (-4.19%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>206.30 (n/a)</td><td>178.78 (n/a)</td><td>186.90 (n/a)</td><td>150.80 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (-0.73%)</td><td>0.24 (+13.19%)</td><td>0.24 <b>(+22.53%)</b></td><td>0.22 <b>(+27.94%)</b></td><td>0.02 <b>(-54.48%)</b></td><td>160.30 <b>(-21.84%)</b></td><td>145.56 (-14.01%)</td><td>145.40 (-18.41%)</td><td>130.20 (+0.70%)</td><td>11.91 <b>(-63.86%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>205.10 (n/a)</td><td>169.28 (n/a)</td><td>178.20 (n/a)</td><td>129.30 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (+1.56%)</td><td>0.21 (+5.57%)</td><td>0.21 (+16.10%)</td><td>0.18 (+8.66%)</td><td>0.03 (-15.01%)</td><td>198.50 (-7.97%)</td><td>171.24 (-5.90%)</td><td>166.40 (-13.83%)</td><td>143.60 (-1.51%)</td><td>22.52 <b>(-21.29%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>215.70 (n/a)</td><td>181.98 (n/a)</td><td>193.10 (n/a)</td><td>145.80 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (-14.54%)</td><td>0.19 (-17.07%)</td><td>0.22 (-4.19%)</td><td>0.15 (-14.69%)</td><td>0.04 (+0.63%)</td><td>236.10 (+17.23%)</td><td>186.64 <b>(+22.26%)</b></td><td>158.20 (+4.42%)</td><td>147.50 (+17.06%)</td><td>44.53 <b>(+44.84%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>201.40 (n/a)</td><td>152.66 (n/a)</td><td>151.50 (n/a)</td><td>126.00 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (+5.04%)</td><td>0.22 (+0.87%)</td><td>0.22 (+1.08%)</td><td>0.15 (+4.27%)</td><td>0.06 <b>(+23.69%)</b></td><td>235.00 (-4.08%)</td><td>168.42 (+0.79%)</td><td>158.30 (-1.06%)</td><td>122.10 (-4.83%)</td><td>49.69 (+7.18%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>245.00 (n/a)</td><td>167.10 (n/a)</td><td>160.00 (n/a)</td><td>128.30 (n/a)</td><td>46.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (-9.29%)</td><td>0.21 (+0.47%)</td><td>0.21 (-1.91%)</td><td>0.19 (+16.66%)</td><td>0.02 <b>(-63.11%)</b></td><td>184.40 (-14.27%)</td><td>167.24 (-3.40%)</td><td>166.40 (+1.96%)</td><td>153.90 (+10.24%)</td><td>12.63 <b>(-65.15%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>215.10 (n/a)</td><td>173.12 (n/a)</td><td>163.20 (n/a)</td><td>139.60 (n/a)</td><td>36.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (+10.22%)</td><td>0.22 (+4.01%)</td><td>0.19 (-10.18%)</td><td>0.16 (+11.71%)</td><td>0.05 <b>(+27.15%)</b></td><td>215.90 (-10.49%)</td><td>168.28 (-2.95%)</td><td>183.40 (+11.29%)</td><td>121.50 (-9.26%)</td><td>39.76 (-2.62%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>241.20 (n/a)</td><td>173.40 (n/a)</td><td>164.80 (n/a)</td><td>133.90 (n/a)</td><td>40.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (+7.25%)</td><td>0.20 (-5.22%)</td><td>0.20 (-9.68%)</td><td>0.16 (-5.89%)</td><td>0.04 <b>(+40.45%)</b></td><td>217.90 (+6.24%)</td><td>177.02 (+6.70%)</td><td>178.20 (+10.75%)</td><td>136.60 (-6.76%)</td><td>30.44 <b>(+33.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>205.10 (n/a)</td><td>165.90 (n/a)</td><td>160.90 (n/a)</td><td>146.50 (n/a)</td><td>22.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 <b>(+20.39%)</b></td><td>0.20 (+9.48%)</td><td>0.21 (+13.08%)</td><td>0.16 (-4.31%)</td><td>0.04 <b>(+101.54%)</b></td><td>223.80 (+4.48%)</td><td>175.86 (-6.65%)</td><td>166.50 (-11.58%)</td><td>136.90 (-16.93%)</td><td>34.85 <b>(+76.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>188.38 (n/a)</td><td>188.30 (n/a)</td><td>164.80 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.88 (-5.69%)</td><td>0.78 (-5.26%)</td><td>0.77 (-3.96%)</td><td>0.70 (+1.14%)</td><td>0.08 <b>(-20.03%)</b></td><td>188.20 (-1.10%)</td><td>169.00 (+5.16%)</td><td>169.40 (+4.12%)</td><td>149.10 (+6.05%)</td><td>16.66 (-15.52%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.93 (n/a)</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.69 (n/a)</td><td>0.10 (n/a)</td><td>190.30 (n/a)</td><td>160.70 (n/a)</td><td>162.70 (n/a)</td><td>140.60 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.90 (-10.48%)</td><td>0.80 <b>(+22.79%)</b></td><td>0.78 (+11.34%)</td><td>0.66 <b>(+94.85%)</b></td><td>0.10 <b>(-67.26%)</b></td><td>198.70 <b>(-48.67%)</b></td><td>166.18 <b>(-32.04%)</b></td><td>167.60 (-10.18%)</td><td>145.90 (+11.72%)</td><td>21.19 <b>(-82.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.00 (n/a)</td><td>0.65 (n/a)</td><td>0.70 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>387.10 (n/a)</td><td>244.54 (n/a)</td><td>186.60 (n/a)</td><td>130.60 (n/a)</td><td>121.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.84 <b>(-35.79%)</b></td><td>0.72 (-18.02%)</td><td>0.71 (-14.53%)</td><td>0.59 (-1.91%)</td><td>0.11 <b>(-60.41%)</b></td><td>222.10 (+1.93%)</td><td>184.60 (+16.09%)</td><td>185.80 (+17.00%)</td><td>156.70 <b>(+55.77%)</b></td><td>27.48 <b>(-37.38%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.30 (n/a)</td><td>0.88 (n/a)</td><td>0.83 (n/a)</td><td>0.60 (n/a)</td><td>0.27 (n/a)</td><td>217.90 (n/a)</td><td>159.02 (n/a)</td><td>158.80 (n/a)</td><td>100.60 (n/a)</td><td>43.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.00 (+0.00%)</td><td>0.00 (+0.93%)</td><td>0.00 (-2.27%)</td><td>0.00 (+4.88%)</td><td>0.00 <b>(-45.57%)</b></td><td>956.12 (-4.95%)</td><td>940.64 (-1.21%)</td><td>952.34 (+1.18%)</td><td>915.56 (+0.62%)</td><td>19.65 <b>(-45.12%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1005.86 (n/a)</td><td>952.13 (n/a)</td><td>941.23 (n/a)</td><td>909.90 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.01 (+0.00%)</td><td>0.01 (+0.74%)</td><td>0.01 (+0.00%)</td><td>0.01 (+3.90%)</td><td>0.00 <b>(-47.64%)</b></td><td>1028.95 (-3.11%)</td><td>1004.56 (-0.58%)</td><td>999.10 (-0.16%)</td><td>987.56 (-0.24%)</td><td>17.31 <b>(-41.63%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1061.95 (n/a)</td><td>1010.42 (n/a)</td><td>1000.75 (n/a)</td><td>989.89 (n/a)</td><td>29.65 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.96 (-1.89%)</td><td>0.94 (-0.35%)</td><td>0.93 (+0.37%)</td><td>0.93 (+0.42%)</td><td>0.01 <b>(-44.98%)</b></td><td>2258.34 (-0.42%)</td><td>2238.75 (+0.33%)</td><td>2244.60 (-0.36%)</td><td>2192.40 (+1.93%)</td><td>26.82 <b>(-44.29%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.97 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.92 (n/a)</td><td>0.02 (n/a)</td><td>2267.94 (n/a)</td><td>2231.49 (n/a)</td><td>2252.74 (n/a)</td><td>2150.83 (n/a)</td><td>48.15 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.06 (-1.92%)</td><td>4.12 (-10.57%)</td><td>3.92 (-15.91%)</td><td>3.73 (-0.70%)</td><td>0.54 (-3.71%)</td><td>281.40 (+0.72%)</td><td>257.58 (+11.73%)</td><td>267.70 (+18.92%)</td><td>207.10 (+1.97%)</td><td>29.12 (-4.10%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>5.16 (n/a)</td><td>4.61 (n/a)</td><td>4.66 (n/a)</td><td>3.75 (n/a)</td><td>0.56 (n/a)</td><td>279.40 (n/a)</td><td>230.54 (n/a)</td><td>225.10 (n/a)</td><td>203.10 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>6.42 <b>(+33.42%)</b></td><td>4.96 (+9.39%)</td><td>4.85 (+7.47%)</td><td>3.94 (-8.40%)</td><td>0.92 <b>(+399.75%)</b></td><td>265.90 (+9.20%)</td><td>216.76 (-6.33%)</td><td>216.00 (-6.94%)</td><td>163.30 <b>(-25.02%)</b></td><td>37.36 <b>(+303.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>4.81 (n/a)</td><td>4.54 (n/a)</td><td>4.52 (n/a)</td><td>4.31 (n/a)</td><td>0.18 (n/a)</td><td>243.50 (n/a)</td><td>231.40 (n/a)</td><td>232.10 (n/a)</td><td>217.80 (n/a)</td><td>9.27 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.25 (-15.23%)</td><td>4.53 (+1.15%)</td><td>4.60 (+12.14%)</td><td>3.92 (+2.57%)</td><td>0.54 <b>(-44.84%)</b></td><td>267.60 (-2.51%)</td><td>233.86 (-2.99%)</td><td>228.00 (-10.83%)</td><td>199.60 (+17.97%)</td><td>27.50 <b>(-33.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.20 (n/a)</td><td>4.48 (n/a)</td><td>4.10 (n/a)</td><td>3.82 (n/a)</td><td>0.97 (n/a)</td><td>274.50 (n/a)</td><td>241.08 (n/a)</td><td>255.70 (n/a)</td><td>169.20 (n/a)</td><td>41.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.47 (+8.07%)</td><td>4.98 (+4.51%)</td><td>5.15 (+5.86%)</td><td>4.48 (+4.03%)</td><td>0.44 <b>(+39.40%)</b></td><td>234.30 (-3.90%)</td><td>211.80 (-4.05%)</td><td>203.70 (-5.56%)</td><td>191.70 (-7.44%)</td><td>19.21 <b>(+25.62%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>5.06 (n/a)</td><td>4.77 (n/a)</td><td>4.86 (n/a)</td><td>4.30 (n/a)</td><td>0.32 (n/a)</td><td>243.80 (n/a)</td><td>220.74 (n/a)</td><td>215.70 (n/a)</td><td>207.10 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.87 (+4.21%)</td><td>7.61 (+0.99%)</td><td>7.53 (-3.81%)</td><td>6.75 (+19.60%)</td><td>0.89 (-19.82%)</td><td>310.70 (-16.39%)</td><td>278.46 (-1.99%)</td><td>278.60 (+3.96%)</td><td>236.40 (-4.02%)</td><td>31.35 <b>(-37.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.51 (n/a)</td><td>7.54 (n/a)</td><td>7.83 (n/a)</td><td>5.64 (n/a)</td><td>1.10 (n/a)</td><td>371.60 (n/a)</td><td>284.10 (n/a)</td><td>268.00 (n/a)</td><td>246.30 (n/a)</td><td>49.94 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.23 (-7.73%)</td><td>7.99 (-0.31%)</td><td>7.92 (-0.61%)</td><td>7.84 (+4.43%)</td><td>0.15 <b>(-72.19%)</b></td><td>267.50 (-4.26%)</td><td>262.68 (-0.02%)</td><td>264.90 (+0.61%)</td><td>254.80 (+8.38%)</td><td>4.95 <b>(-70.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.92 (n/a)</td><td>8.01 (n/a)</td><td>7.97 (n/a)</td><td>7.51 (n/a)</td><td>0.55 (n/a)</td><td>279.40 (n/a)</td><td>262.74 (n/a)</td><td>263.30 (n/a)</td><td>235.10 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.16 (+8.20%)</td><td>7.91 (+0.54%)</td><td>7.89 (-0.20%)</td><td>6.62 (-8.98%)</td><td>0.93 <b>(+97.04%)</b></td><td>316.60 (+9.89%)</td><td>268.30 (+0.31%)</td><td>266.00 (+0.23%)</td><td>228.90 (-7.59%)</td><td>32.31 <b>(+101.01%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.47 (n/a)</td><td>7.86 (n/a)</td><td>7.90 (n/a)</td><td>7.28 (n/a)</td><td>0.47 (n/a)</td><td>288.10 (n/a)</td><td>267.48 (n/a)</td><td>265.40 (n/a)</td><td>247.70 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.80 (-3.21%)</td><td>8.48 (+1.87%)</td><td>8.47 (+0.50%)</td><td>8.06 (+11.92%)</td><td>0.30 <b>(-56.59%)</b></td><td>260.20 (-10.65%)</td><td>247.68 (-2.32%)</td><td>247.60 (-0.48%)</td><td>238.30 (+3.29%)</td><td>8.88 <b>(-60.75%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.09 (n/a)</td><td>8.32 (n/a)</td><td>8.43 (n/a)</td><td>7.20 (n/a)</td><td>0.69 (n/a)</td><td>291.20 (n/a)</td><td>253.56 (n/a)</td><td>248.80 (n/a)</td><td>230.70 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.03 (-0.30%)</td><td>8.24 (-1.03%)</td><td>8.50 (+3.70%)</td><td>6.68 (-11.60%)</td><td>0.96 <b>(+62.06%)</b></td><td>313.80 (+13.12%)</td><td>257.52 (+1.88%)</td><td>246.80 (-3.56%)</td><td>232.20 (+0.35%)</td><td>33.53 <b>(+85.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.06 (n/a)</td><td>8.33 (n/a)</td><td>8.20 (n/a)</td><td>7.56 (n/a)</td><td>0.59 (n/a)</td><td>277.40 (n/a)</td><td>252.78 (n/a)</td><td>255.90 (n/a)</td><td>231.40 (n/a)</td><td>18.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.69 (+7.59%)</td><td>8.29 (+1.32%)</td><td>8.36 (+0.23%)</td><td>6.55 (-7.21%)</td><td>1.13 <b>(+56.05%)</b></td><td>319.90 (+7.75%)</td><td>256.96 (-0.37%)</td><td>250.70 (-0.24%)</td><td>216.50 (-7.08%)</td><td>38.23 <b>(+58.19%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>9.00 (n/a)</td><td>8.19 (n/a)</td><td>8.35 (n/a)</td><td>7.06 (n/a)</td><td>0.72 (n/a)</td><td>296.90 (n/a)</td><td>257.92 (n/a)</td><td>251.30 (n/a)</td><td>233.00 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.31 (+7.90%)</td><td>11.03 (+3.51%)</td><td>11.02 (+1.16%)</td><td>9.96 (+1.82%)</td><td>1.01 <b>(+27.97%)</b></td><td>420.90 (-1.80%)</td><td>382.62 (-3.18%)</td><td>380.60 (-1.14%)</td><td>340.60 (-7.32%)</td><td>34.63 (+16.83%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>11.41 (n/a)</td><td>10.66 (n/a)</td><td>10.89 (n/a)</td><td>9.79 (n/a)</td><td>0.79 (n/a)</td><td>428.60 (n/a)</td><td>395.20 (n/a)</td><td>385.00 (n/a)</td><td>367.50 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.44 (+14.15%)</td><td>11.49 (+14.09%)</td><td>11.49 (+15.61%)</td><td>10.09 (+7.30%)</td><td>0.90 <b>(+63.98%)</b></td><td>415.90 (-6.79%)</td><td>366.88 (-12.10%)</td><td>364.90 (-13.51%)</td><td>337.10 (-12.42%)</td><td>30.40 <b>(+35.79%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>10.90 (n/a)</td><td>10.07 (n/a)</td><td>9.94 (n/a)</td><td>9.40 (n/a)</td><td>0.55 (n/a)</td><td>446.20 (n/a)</td><td>417.40 (n/a)</td><td>421.90 (n/a)</td><td>384.90 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.54 (-1.25%)</td><td>11.56 (+1.05%)</td><td>11.85 (+5.49%)</td><td>10.50 (-1.13%)</td><td>0.81 (-10.93%)</td><td>399.30 (+1.14%)</td><td>364.12 (-1.13%)</td><td>353.90 (-5.22%)</td><td>334.60 (+1.27%)</td><td>25.80 (-9.13%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>12.69 (n/a)</td><td>11.44 (n/a)</td><td>11.23 (n/a)</td><td>10.62 (n/a)</td><td>0.90 (n/a)</td><td>394.80 (n/a)</td><td>368.28 (n/a)</td><td>373.40 (n/a)</td><td>330.40 (n/a)</td><td>28.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>15.01 (+14.85%)</td><td>13.07 (+8.69%)</td><td>12.91 (+7.79%)</td><td>11.93 (+14.11%)</td><td>1.20 (+19.37%)</td><td>351.60 (-12.36%)</td><td>322.98 (-7.96%)</td><td>324.80 (-7.23%)</td><td>279.40 (-12.93%)</td><td>27.73 (-10.56%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.07 (n/a)</td><td>12.02 (n/a)</td><td>11.98 (n/a)</td><td>10.45 (n/a)</td><td>1.00 (n/a)</td><td>401.20 (n/a)</td><td>350.90 (n/a)</td><td>350.10 (n/a)</td><td>320.90 (n/a)</td><td>31.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>14.65 (+4.90%)</td><td>13.20 (+5.55%)</td><td>13.31 (+9.67%)</td><td>11.19 (+0.51%)</td><td>1.26 (-3.18%)</td><td>374.70 (-0.50%)</td><td>320.26 (-5.33%)</td><td>315.10 (-8.83%)</td><td>286.30 (-4.66%)</td><td>32.92 (-5.20%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.97 (n/a)</td><td>12.51 (n/a)</td><td>12.14 (n/a)</td><td>11.14 (n/a)</td><td>1.30 (n/a)</td><td>376.60 (n/a)</td><td>338.28 (n/a)</td><td>345.60 (n/a)</td><td>300.30 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>15.81 (+15.09%)</td><td>12.99 (+3.83%)</td><td>13.69 (+11.45%)</td><td>9.67 <b>(-20.07%)</b></td><td>2.33 <b>(+236.45%)</b></td><td>433.80 <b>(+25.12%)</b></td><td>332.18 (-1.17%)</td><td>306.30 (-10.28%)</td><td>265.40 (-13.10%)</td><td>64.98 <b>(+274.39%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.73 (n/a)</td><td>12.51 (n/a)</td><td>12.29 (n/a)</td><td>12.10 (n/a)</td><td>0.69 (n/a)</td><td>346.70 (n/a)</td><td>336.12 (n/a)</td><td>341.40 (n/a)</td><td>305.40 (n/a)</td><td>17.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>16.08 (+15.51%)</td><td>13.83 (+8.25%)</td><td>13.16 (-1.80%)</td><td>13.08 <b>(+33.46%)</b></td><td>1.28 <b>(-25.32%)</b></td><td>320.60 <b>(-25.08%)</b></td><td>305.10 (-8.65%)</td><td>318.70 (+1.82%)</td><td>260.80 (-13.44%)</td><td>25.45 <b>(-52.37%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>13.92 (n/a)</td><td>12.78 (n/a)</td><td>13.40 (n/a)</td><td>9.80 (n/a)</td><td>1.72 (n/a)</td><td>427.90 (n/a)</td><td>333.98 (n/a)</td><td>313.00 (n/a)</td><td>301.30 (n/a)</td><td>53.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>14.96 (+5.52%)</td><td>12.72 (+5.78%)</td><td>12.85 (+2.43%)</td><td>9.45 (+11.08%)</td><td>2.04 (-9.80%)</td><td>444.00 (-9.96%)</td><td>337.76 (-6.37%)</td><td>326.40 (-2.36%)</td><td>280.30 (-5.24%)</td><td>62.73 <b>(-21.33%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>14.18 (n/a)</td><td>12.02 (n/a)</td><td>12.55 (n/a)</td><td>8.51 (n/a)</td><td>2.27 (n/a)</td><td>493.10 (n/a)</td><td>360.72 (n/a)</td><td>334.30 (n/a)</td><td>295.80 (n/a)</td><td>79.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>2.95 (+5.83%)</td><td>2.65 (+0.81%)</td><td>2.72 (+0.54%)</td><td>2.15 (-7.23%)</td><td>0.31 <b>(+59.44%)</b></td><td>243.60 (+7.79%)</td><td>200.30 (-0.07%)</td><td>192.80 (-0.52%)</td><td>177.70 (-5.48%)</td><td>25.71 <b>(+65.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>2.79 (n/a)</td><td>2.63 (n/a)</td><td>2.71 (n/a)</td><td>2.32 (n/a)</td><td>0.19 (n/a)</td><td>226.00 (n/a)</td><td>200.44 (n/a)</td><td>193.80 (n/a)</td><td>188.00 (n/a)</td><td>15.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.77 (-5.63%)</td><td>4.93 (+3.43%)</td><td>5.25 (+12.07%)</td><td>3.40 (+15.05%)</td><td>0.93 <b>(-21.97%)</b></td><td>308.80 (-13.09%)</td><td>220.54 (-5.82%)</td><td>199.80 (-10.80%)</td><td>181.60 (+5.95%)</td><td>51.21 <b>(-28.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>6.12 (n/a)</td><td>4.76 (n/a)</td><td>4.68 (n/a)</td><td>2.95 (n/a)</td><td>1.19 (n/a)</td><td>355.30 (n/a)</td><td>234.18 (n/a)</td><td>224.00 (n/a)</td><td>171.40 (n/a)</td><td>71.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.71 (-0.49%)</td><td>7.23 (+1.55%)</td><td>7.45 (+10.86%)</td><td>5.65 (-3.64%)</td><td>1.13 (+2.19%)</td><td>370.90 (+3.78%)</td><td>296.08 (-1.33%)</td><td>281.40 (-9.81%)</td><td>240.80 (+0.50%)</td><td>48.67 (+9.25%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>8.75 (n/a)</td><td>7.12 (n/a)</td><td>6.72 (n/a)</td><td>5.87 (n/a)</td><td>1.10 (n/a)</td><td>357.40 (n/a)</td><td>300.08 (n/a)</td><td>312.00 (n/a)</td><td>239.60 (n/a)</td><td>44.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>3.07 (-2.20%)</td><td>2.85 (+7.53%)</td><td>2.81 (+0.62%)</td><td>2.54 <b>(+23.24%)</b></td><td>0.21 <b>(-59.64%)</b></td><td>206.80 (-18.87%)</td><td>184.88 (-9.65%)</td><td>186.30 (-0.64%)</td><td>170.60 (+2.28%)</td><td>14.21 <b>(-66.61%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>3.14 (n/a)</td><td>2.65 (n/a)</td><td>2.80 (n/a)</td><td>2.06 (n/a)</td><td>0.52 (n/a)</td><td>254.90 (n/a)</td><td>204.62 (n/a)</td><td>187.50 (n/a)</td><td>166.80 (n/a)</td><td>42.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (+16.01%)</td><td>0.19 (+4.54%)</td><td>0.18 (+2.43%)</td><td>0.14 (-14.73%)</td><td>0.04 <b>(+172.96%)</b></td><td>231.10 (+17.31%)</td><td>180.00 (-1.86%)</td><td>182.10 (-2.41%)</td><td>141.50 (-13.82%)</td><td>35.20 <b>(+175.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>183.42 (n/a)</td><td>186.60 (n/a)</td><td>164.20 (n/a)</td><td>12.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 <b>(+25.46%)</b></td><td>0.20 <b>(+32.23%)</b></td><td>0.20 <b>(+25.54%)</b></td><td>0.16 <b>(+76.97%)</b></td><td>0.03 (-7.24%)</td><td>208.10 <b>(-43.50%)</b></td><td>169.04 <b>(-27.51%)</b></td><td>165.50 <b>(-20.32%)</b></td><td>136.00 <b>(-20.28%)</b></td><td>30.15 <b>(-61.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>368.30 (n/a)</td><td>233.18 (n/a)</td><td>207.70 (n/a)</td><td>170.60 (n/a)</td><td>77.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.48 (-7.84%)</td><td>0.38 (+10.87%)</td><td>0.35 (+10.92%)</td><td>0.33 <b>(+69.50%)</b></td><td>0.06 <b>(-49.23%)</b></td><td>198.90 <b>(-41.00%)</b></td><td>176.56 (-17.14%)</td><td>184.70 (-9.86%)</td><td>137.30 (+8.45%)</td><td>25.28 <b>(-67.87%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>337.10 (n/a)</td><td>213.08 (n/a)</td><td>204.90 (n/a)</td><td>126.60 (n/a)</td><td>78.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.45 (+0.70%)</td><td>0.35 (-6.87%)</td><td>0.33 (-8.15%)</td><td>0.30 (-4.28%)</td><td>0.06 (-3.60%)</td><td>217.20 (+4.47%)</td><td>188.58 (+7.33%)</td><td>200.50 (+8.85%)</td><td>145.70 (-0.68%)</td><td>28.03 (+1.91%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>207.90 (n/a)</td><td>175.70 (n/a)</td><td>184.20 (n/a)</td><td>146.70 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.43 <b>(-21.01%)</b></td><td>0.40 (+1.13%)</td><td>0.40 (+10.93%)</td><td>0.37 (+11.32%)</td><td>0.02 <b>(-71.99%)</b></td><td>178.40 (-10.17%)</td><td>166.22 (-4.04%)</td><td>164.70 (-9.85%)</td><td>151.10 <b>(+26.55%)</b></td><td>10.25 <b>(-66.82%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.55 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>198.60 (n/a)</td><td>173.22 (n/a)</td><td>182.70 (n/a)</td><td>119.40 (n/a)</td><td>30.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.09 (-5.09%)</td><td>0.84 (+3.54%)</td><td>0.87 <b>(+20.98%)</b></td><td>0.65 (-4.89%)</td><td>0.19 (-2.90%)</td><td>202.20 (+5.15%)</td><td>161.34 (-3.09%)</td><td>150.50 (-17.35%)</td><td>120.80 (+5.41%)</td><td>35.62 (+13.23%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>1.14 (n/a)</td><td>0.82 (n/a)</td><td>0.72 (n/a)</td><td>0.68 (n/a)</td><td>0.19 (n/a)</td><td>192.30 (n/a)</td><td>166.48 (n/a)</td><td>182.10 (n/a)</td><td>114.60 (n/a)</td><td>31.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.95 (+5.48%)</td><td>0.70 (-3.88%)</td><td>0.72 (+10.18%)</td><td>0.41 <b>(-35.72%)</b></td><td>0.19 <b>(+74.19%)</b></td><td>317.10 <b>(+55.52%)</b></td><td>203.36 (+10.23%)</td><td>181.40 (-9.25%)</td><td>138.70 (-5.13%)</td><td>68.23 <b>(+163.37%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.90 (n/a)</td><td>0.72 (n/a)</td><td>0.66 (n/a)</td><td>0.64 (n/a)</td><td>0.11 (n/a)</td><td>203.90 (n/a)</td><td>184.48 (n/a)</td><td>199.90 (n/a)</td><td>146.20 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.11 (+16.82%)</td><td>0.84 (+5.56%)</td><td>0.79 (+5.51%)</td><td>0.69 (+11.39%)</td><td>0.16 <b>(+20.73%)</b></td><td>190.10 (-10.20%)</td><td>160.78 (-5.07%)</td><td>165.70 (-5.26%)</td><td>117.90 (-14.38%)</td><td>26.64 (-9.41%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.95 (n/a)</td><td>0.79 (n/a)</td><td>0.75 (n/a)</td><td>0.62 (n/a)</td><td>0.13 (n/a)</td><td>211.70 (n/a)</td><td>169.36 (n/a)</td><td>174.90 (n/a)</td><td>137.70 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.69 (-12.78%)</td><td>0.65 (+5.35%)</td><td>0.65 (+1.74%)</td><td>0.60 <b>(+47.44%)</b></td><td>0.04 <b>(-72.22%)</b></td><td>219.40 <b>(-32.18%)</b></td><td>201.74 (-9.34%)</td><td>200.50 (-1.72%)</td><td>188.80 (+14.63%)</td><td>12.27 <b>(-79.47%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.80 (n/a)</td><td>0.62 (n/a)</td><td>0.64 (n/a)</td><td>0.41 (n/a)</td><td>0.14 (n/a)</td><td>323.50 (n/a)</td><td>222.52 (n/a)</td><td>204.00 (n/a)</td><td>164.70 (n/a)</td><td>59.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (+2.66%)</td><td>0.09 (+1.64%)</td><td>0.09 (+14.90%)</td><td>0.07 (-12.82%)</td><td>0.02 (+13.83%)</td><td>242.10 (+14.68%)</td><td>187.54 (-0.79%)</td><td>180.40 (-12.98%)</td><td>144.80 (-2.62%)</td><td>36.54 <b>(+25.44%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 19:16:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>189.04 (n/a)</td><td>207.30 (n/a)</td><td>148.70 (n/a)</td><td>29.13 (n/a)</td>
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
