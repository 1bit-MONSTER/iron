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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-15.15%)</td><td>0.03 (-14.04%)</td><td>0.03 <b>(-21.90%)</b></td><td>0.03 (+12.05%)</td><td>0.00 <b>(-53.52%)</b></td><td>210.60 (-10.72%)</td><td>184.14 (+10.83%)</td><td>186.20 <b>(+28.06%)</b></td><td>146.70 (+17.83%)</td><td>23.68 <b>(-51.37%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>166.14 (n/a)</td><td>145.40 (n/a)</td><td>124.50 (n/a)</td><td>48.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-11.12%)</td><td>0.04 (-7.88%)</td><td>0.04 (-4.55%)</td><td>0.03 (-8.44%)</td><td>0.01 (-14.64%)</td><td>206.20 (+9.22%)</td><td>156.02 (+8.29%)</td><td>141.60 (+4.73%)</td><td>137.10 (+12.56%)</td><td>29.21 (+5.74%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>144.08 (n/a)</td><td>135.20 (n/a)</td><td>121.80 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (+5.56%)</td><td>0.04 (-0.21%)</td><td>0.04 (-6.80%)</td><td>0.03 (-0.33%)</td><td>0.01 (+4.35%)</td><td>189.60 (+0.32%)</td><td>162.58 (+0.16%)</td><td>162.60 (+7.26%)</td><td>127.50 (-5.27%)</td><td>23.27 (-5.64%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>162.32 (n/a)</td><td>151.60 (n/a)</td><td>134.60 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (-2.32%)</td><td>0.04 (+4.26%)</td><td>0.04 (+16.54%)</td><td>0.03 (-5.70%)</td><td>0.01 <b>(+24.32%)</b></td><td>209.40 (+6.08%)</td><td>166.24 (-2.38%)</td><td>150.00 (-14.19%)</td><td>131.80 (+2.41%)</td><td>39.41 <b>(+34.51%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>170.30 (n/a)</td><td>174.80 (n/a)</td><td>128.70 (n/a)</td><td>29.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-5.09%)</td><td>0.04 (-4.78%)</td><td>0.04 (-5.75%)</td><td>0.03 (-0.60%)</td><td>0.00 (-8.48%)</td><td>206.30 (+0.59%)</td><td>174.36 (+4.82%)</td><td>164.70 (+6.05%)</td><td>153.50 (+5.35%)</td><td>22.34 (-4.60%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>166.34 (n/a)</td><td>155.30 (n/a)</td><td>145.70 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-0.51%)</td><td>0.03 (-3.02%)</td><td>0.03 (+17.22%)</td><td>0.02 <b>(-24.65%)</b></td><td>0.01 (-6.34%)</td><td>317.40 <b>(+32.69%)</b></td><td>203.66 (+4.25%)</td><td>188.70 (-14.69%)</td><td>136.60 (+0.52%)</td><td>68.22 <b>(+30.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>195.36 (n/a)</td><td>221.20 (n/a)</td><td>135.90 (n/a)</td><td>52.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 <b>(+22.66%)</b></td><td>0.04 (+11.06%)</td><td>0.03 (+1.54%)</td><td>0.03 (+14.88%)</td><td>0.01 <b>(+29.43%)</b></td><td>220.60 (-12.94%)</td><td>177.78 (-9.67%)</td><td>177.50 (-1.55%)</td><td>141.30 (-18.47%)</td><td>30.15 (-9.18%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.40 (n/a)</td><td>196.82 (n/a)</td><td>180.30 (n/a)</td><td>173.30 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (+18.92%)</td><td>0.04 (+15.83%)</td><td>0.04 <b>(+41.63%)</b></td><td>0.02 <b>(-32.72%)</b></td><td>0.01 <b>(+133.57%)</b></td><td>323.50 <b>(+48.60%)</b></td><td>179.64 (-5.23%)</td><td>142.90 <b>(-29.40%)</b></td><td>135.10 (-15.88%)</td><td>80.96 <b>(+208.56%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>217.70 (n/a)</td><td>189.56 (n/a)</td><td>202.40 (n/a)</td><td>160.60 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 <b>(+20.71%)</b></td><td>0.09 <b>(+23.09%)</b></td><td>0.09 <b>(+26.22%)</b></td><td>0.07 <b>(+23.96%)</b></td><td>0.01 <b>(+24.97%)</b></td><td>171.60 (-19.32%)</td><td>146.06 (-18.68%)</td><td>134.70 <b>(-20.76%)</b></td><td>123.60 (-17.21%)</td><td>23.20 (-15.64%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>179.62 (n/a)</td><td>170.00 (n/a)</td><td>149.30 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (-2.78%)</td><td>0.09 <b>(+26.34%)</b></td><td>0.08 <b>(+33.72%)</b></td><td>0.08 <b>(+73.79%)</b></td><td>0.01 <b>(-54.00%)</b></td><td>163.60 <b>(-42.46%)</b></td><td>144.94 <b>(-26.01%)</b></td><td>146.80 <b>(-25.22%)</b></td><td>128.00 (+2.89%)</td><td>16.39 <b>(-73.03%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>284.30 (n/a)</td><td>195.90 (n/a)</td><td>196.30 (n/a)</td><td>124.40 (n/a)</td><td>60.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (-10.97%)</td><td>0.08 (-7.28%)</td><td>0.07 (-12.49%)</td><td>0.06 (-0.82%)</td><td>0.02 (-12.65%)</td><td>210.30 (+0.81%)</td><td>164.50 (+7.08%)</td><td>171.00 (+14.23%)</td><td>126.90 (+12.30%)</td><td>35.53 (-4.61%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>208.60 (n/a)</td><td>153.62 (n/a)</td><td>149.70 (n/a)</td><td>113.00 (n/a)</td><td>37.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (+15.64%)</td><td>0.08 <b>(+23.08%)</b></td><td>0.09 <b>(+29.12%)</b></td><td>0.06 <b>(+51.06%)</b></td><td>0.02 (-10.68%)</td><td>192.70 <b>(-33.80%)</b></td><td>153.70 <b>(-21.43%)</b></td><td>136.40 <b>(-22.59%)</b></td><td>125.70 (-13.55%)</td><td>30.82 <b>(-48.24%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>291.10 (n/a)</td><td>195.62 (n/a)</td><td>176.20 (n/a)</td><td>145.40 (n/a)</td><td>59.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (+4.27%)</td><td>0.07 (+6.07%)</td><td>0.07 (+4.54%)</td><td>0.06 (+5.79%)</td><td>0.01 (+8.16%)</td><td>201.30 (-5.49%)</td><td>170.78 (-5.66%)</td><td>169.80 (-4.34%)</td><td>146.80 (-4.11%)</td><td>21.25 (-2.32%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>181.02 (n/a)</td><td>177.50 (n/a)</td><td>153.10 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (-7.58%)</td><td>0.08 (+9.08%)</td><td>0.08 (-0.78%)</td><td>0.07 <b>(+46.18%)</b></td><td>0.01 <b>(-65.28%)</b></td><td>186.90 <b>(-31.59%)</b></td><td>162.64 (-14.99%)</td><td>154.30 (+0.78%)</td><td>147.40 (+8.22%)</td><td>16.33 <b>(-74.50%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>273.20 (n/a)</td><td>191.32 (n/a)</td><td>153.10 (n/a)</td><td>136.20 (n/a)</td><td>64.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (+13.43%)</td><td>0.07 (+16.17%)</td><td>0.07 (+17.91%)</td><td>0.06 (+13.03%)</td><td>0.01 (+6.61%)</td><td>218.40 (-11.51%)</td><td>180.74 (-14.20%)</td><td>187.40 (-15.20%)</td><td>142.50 (-11.87%)</td><td>29.56 (-17.91%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>246.80 (n/a)</td><td>210.66 (n/a)</td><td>221.00 (n/a)</td><td>161.70 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (-3.57%)</td><td>0.06 (+2.19%)</td><td>0.06 (+8.71%)</td><td>0.04 (-16.39%)</td><td>0.01 (+19.42%)</td><td>310.10 (+19.59%)</td><td>217.62 (-0.24%)</td><td>207.70 (-8.02%)</td><td>171.20 (+3.69%)</td><td>54.52 <b>(+57.20%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>259.30 (n/a)</td><td>218.14 (n/a)</td><td>225.80 (n/a)</td><td>165.10 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.19 (+4.59%)</td><td>0.16 (+10.60%)</td><td>0.15 (+14.36%)</td><td>0.13 (+11.88%)</td><td>0.03 (-3.17%)</td><td>192.40 (-10.64%)</td><td>159.18 (-10.12%)</td><td>165.70 (-12.56%)</td><td>126.80 (-4.37%)</td><td>27.20 (-17.55%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>215.30 (n/a)</td><td>177.10 (n/a)</td><td>189.50 (n/a)</td><td>132.60 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (-11.55%)</td><td>0.14 (-13.78%)</td><td>0.14 (-5.82%)</td><td>0.10 <b>(-20.69%)</b></td><td>0.03 (-8.03%)</td><td>248.30 <b>(+26.10%)</b></td><td>187.48 (+16.78%)</td><td>181.30 (+6.21%)</td><td>134.30 (+13.05%)</td><td>42.42 <b>(+32.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>196.90 (n/a)</td><td>160.54 (n/a)</td><td>170.70 (n/a)</td><td>118.80 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (-0.53%)</td><td>0.14 (-7.29%)</td><td>0.15 (-8.58%)</td><td>0.11 (-16.16%)</td><td>0.02 (+17.50%)</td><td>233.80 (+19.29%)</td><td>183.14 (+8.90%)</td><td>168.60 (+9.34%)</td><td>148.80 (+0.54%)</td><td>33.23 <b>(+41.94%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>196.00 (n/a)</td><td>168.18 (n/a)</td><td>154.20 (n/a)</td><td>148.00 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.19 (+6.26%)</td><td>0.15 (+4.98%)</td><td>0.15 (+2.83%)</td><td>0.13 (-0.07%)</td><td>0.02 (+11.85%)</td><td>192.50 (+0.05%)</td><td>161.88 (-4.52%)</td><td>165.20 (-2.77%)</td><td>126.70 (-5.94%)</td><td>23.47 (+3.70%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>169.54 (n/a)</td><td>169.90 (n/a)</td><td>134.70 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (-13.43%)</td><td>0.12 (-15.06%)</td><td>0.11 (-15.23%)</td><td>0.08 <b>(-28.11%)</b></td><td>0.02 (+8.69%)</td><td>302.30 <b>(+39.12%)</b></td><td>220.42 (+19.69%)</td><td>214.20 (+17.95%)</td><td>178.10 (+15.50%)</td><td>49.82 <b>(+75.63%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>184.16 (n/a)</td><td>181.60 (n/a)</td><td>154.20 (n/a)</td><td>28.36 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 <b>(-33.88%)</b></td><td>0.12 <b>(-30.74%)</b></td><td>0.13 <b>(-23.27%)</b></td><td>0.08 <b>(-40.27%)</b></td><td>0.03 <b>(-21.85%)</b></td><td>320.50 <b>(+67.36%)</b></td><td>222.02 <b>(+47.03%)</b></td><td>190.10 <b>(+30.29%)</b></td><td>170.90 <b>(+51.24%)</b></td><td>61.30 <b>(+98.92%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.50 (n/a)</td><td>151.00 (n/a)</td><td>145.90 (n/a)</td><td>113.00 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 <b>(+21.04%)</b></td><td>0.13 (+17.21%)</td><td>0.14 <b>(+20.37%)</b></td><td>0.11 (+14.15%)</td><td>0.02 <b>(+68.92%)</b></td><td>222.70 (-12.39%)</td><td>186.82 (-13.96%)</td><td>173.40 (-16.95%)</td><td>161.50 (-17.39%)</td><td>27.57 <b>(+21.00%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>254.20 (n/a)</td><td>217.14 (n/a)</td><td>208.80 (n/a)</td><td>195.50 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 <b>(+39.54%)</b></td><td>0.14 (+6.31%)</td><td>0.11 (-10.55%)</td><td>0.11 (+5.59%)</td><td>0.04 <b>(+131.78%)</b></td><td>226.20 (-5.32%)</td><td>190.64 (-1.94%)</td><td>216.70 (+11.82%)</td><td>119.00 <b>(-28.31%)</b></td><td>44.85 <b>(+56.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>238.90 (n/a)</td><td>194.42 (n/a)</td><td>193.80 (n/a)</td><td>166.00 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 <b>(-28.30%)</b></td><td>0.27 <b>(-21.13%)</b></td><td>0.27 (-14.18%)</td><td>0.20 <b>(-21.29%)</b></td><td>0.04 <b>(-43.55%)</b></td><td>239.90 <b>(+27.07%)</b></td><td>183.48 <b>(+24.77%)</b></td><td>180.20 (+16.48%)</td><td>154.10 <b>(+39.46%)</b></td><td>33.64 (+4.58%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>188.80 (n/a)</td><td>147.06 (n/a)</td><td>154.70 (n/a)</td><td>110.50 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.35 (+2.21%)</td><td>0.29 (+8.37%)</td><td>0.28 (+9.50%)</td><td>0.25 <b>(+55.07%)</b></td><td>0.04 <b>(-45.19%)</b></td><td>197.40 <b>(-35.51%)</b></td><td>172.62 (-12.61%)</td><td>172.80 (-8.67%)</td><td>140.90 (-2.15%)</td><td>20.91 <b>(-67.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>306.10 (n/a)</td><td>197.52 (n/a)</td><td>189.20 (n/a)</td><td>144.00 (n/a)</td><td>63.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.35 <b>(+20.28%)</b></td><td>0.28 (+18.74%)</td><td>0.29 <b>(+31.86%)</b></td><td>0.20 (+1.96%)</td><td>0.06 <b>(+37.37%)</b></td><td>243.20 (-1.90%)</td><td>179.44 (-14.62%)</td><td>169.70 <b>(-24.14%)</b></td><td>138.60 (-16.86%)</td><td>41.34 (+13.98%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>247.90 (n/a)</td><td>210.16 (n/a)</td><td>223.70 (n/a)</td><td>166.70 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.38 (+18.96%)</td><td>0.28 (+11.65%)</td><td>0.27 (-1.79%)</td><td>0.24 <b>(+41.68%)</b></td><td>0.05 (-4.76%)</td><td>204.90 <b>(-29.42%)</b></td><td>177.86 (-12.50%)</td><td>183.30 (+1.83%)</td><td>129.80 (-15.99%)</td><td>28.31 <b>(-47.14%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>290.30 (n/a)</td><td>203.28 (n/a)</td><td>180.00 (n/a)</td><td>154.50 (n/a)</td><td>53.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.37 (-11.78%)</td><td>0.30 (+2.89%)</td><td>0.28 (+5.90%)</td><td>0.26 (+15.55%)</td><td>0.04 <b>(-45.27%)</b></td><td>185.80 (-13.46%)</td><td>166.56 (-6.14%)</td><td>173.80 (-5.59%)</td><td>131.70 (+13.34%)</td><td>21.21 <b>(-47.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>214.70 (n/a)</td><td>177.46 (n/a)</td><td>184.10 (n/a)</td><td>116.20 (n/a)</td><td>40.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.35 (+13.77%)</td><td>0.28 (+9.79%)</td><td>0.28 (-2.09%)</td><td>0.22 <b>(+65.51%)</b></td><td>0.05 <b>(-25.29%)</b></td><td>225.50 <b>(-39.58%)</b></td><td>183.56 (-14.96%)</td><td>176.90 (+2.14%)</td><td>138.70 (-12.10%)</td><td>34.07 <b>(-61.95%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>373.20 (n/a)</td><td>215.86 (n/a)</td><td>173.20 (n/a)</td><td>157.80 (n/a)</td><td>89.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (-10.92%)</td><td>0.24 (-12.30%)</td><td>0.23 (-12.22%)</td><td>0.17 <b>(-26.48%)</b></td><td>0.06 (+7.90%)</td><td>293.10 <b>(+36.01%)</b></td><td>212.56 (+16.46%)</td><td>217.60 (+13.93%)</td><td>153.20 (+12.23%)</td><td>54.69 <b>(+60.94%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>215.50 (n/a)</td><td>182.52 (n/a)</td><td>191.00 (n/a)</td><td>136.50 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.31 (-1.21%)</td><td>0.23 (-11.93%)</td><td>0.22 <b>(-21.12%)</b></td><td>0.17 (-16.48%)</td><td>0.07 <b>(+68.05%)</b></td><td>297.40 (+19.73%)</td><td>226.52 (+19.30%)</td><td>224.70 <b>(+26.81%)</b></td><td>160.40 (+1.26%)</td><td>66.54 <b>(+92.92%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>248.40 (n/a)</td><td>189.88 (n/a)</td><td>177.20 (n/a)</td><td>158.40 (n/a)</td><td>34.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (+1.34%)</td><td>0.02 (+10.47%)</td><td>0.02 (-0.64%)</td><td>0.02 <b>(+53.56%)</b></td><td>0.00 <b>(-71.37%)</b></td><td>134.80 <b>(-34.88%)</b></td><td>123.24 (-13.30%)</td><td>121.90 (+0.66%)</td><td>116.40 (-1.27%)</td><td>7.04 <b>(-81.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>207.00 (n/a)</td><td>142.14 (n/a)</td><td>121.10 (n/a)</td><td>117.90 (n/a)</td><td>37.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (-1.94%)</td><td>0.02 (-10.27%)</td><td>0.02 (-6.04%)</td><td>0.01 <b>(-30.14%)</b></td><td>0.00 <b>(+64.57%)</b></td><td>230.20 <b>(+43.16%)</b></td><td>164.46 (+15.04%)</td><td>157.10 (+6.36%)</td><td>127.00 (+2.01%)</td><td>40.48 <b>(+146.79%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>160.80 (n/a)</td><td>142.96 (n/a)</td><td>147.70 (n/a)</td><td>124.50 (n/a)</td><td>16.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (+9.82%)</td><td>0.02 (+19.50%)</td><td>0.02 <b>(+36.81%)</b></td><td>0.01 (-14.58%)</td><td>0.01 <b>(+49.36%)</b></td><td>349.60 (+17.08%)</td><td>177.00 (-8.38%)</td><td>124.30 <b>(-26.93%)</b></td><td>120.40 (-8.93%)</td><td>98.64 <b>(+53.27%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>298.60 (n/a)</td><td>193.18 (n/a)</td><td>170.10 (n/a)</td><td>132.20 (n/a)</td><td>64.36 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (+2.69%)</td><td>0.02 (-2.07%)</td><td>0.02 (-18.38%)</td><td>0.01 (+16.54%)</td><td>0.00 (-3.07%)</td><td>190.10 (-14.21%)</td><td>159.14 (+1.16%)</td><td>171.20 <b>(+22.46%)</b></td><td>124.40 (-2.66%)</td><td>31.28 <b>(-20.34%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>157.32 (n/a)</td><td>139.80 (n/a)</td><td>127.80 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (+4.29%)</td><td>0.02 (+7.27%)</td><td>0.02 (+9.64%)</td><td>0.01 (+9.20%)</td><td>0.00 (-14.74%)</td><td>183.20 (-8.40%)</td><td>143.34 (-8.40%)</td><td>135.10 (-8.78%)</td><td>111.90 (-4.11%)</td><td>28.58 <b>(-25.72%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>200.00 (n/a)</td><td>156.48 (n/a)</td><td>148.10 (n/a)</td><td>116.70 (n/a)</td><td>38.48 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (+4.46%)</td><td>0.02 (+4.60%)</td><td>0.02 (+11.83%)</td><td>0.01 (-11.55%)</td><td>0.00 <b>(+44.42%)</b></td><td>242.30 (+13.07%)</td><td>165.86 (-2.14%)</td><td>147.20 (-10.57%)</td><td>138.50 (-4.28%)</td><td>43.15 <b>(+59.41%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>169.48 (n/a)</td><td>164.60 (n/a)</td><td>144.70 (n/a)</td><td>27.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (+10.68%)</td><td>0.02 (+4.31%)</td><td>0.02 (+6.95%)</td><td>0.01 (-2.47%)</td><td>0.00 <b>(+51.82%)</b></td><td>210.50 (+2.53%)</td><td>158.48 (-1.68%)</td><td>149.20 (-6.52%)</td><td>116.00 (-9.66%)</td><td>39.28 <b>(+39.66%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>161.18 (n/a)</td><td>159.60 (n/a)</td><td>128.40 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 <b>(+24.05%)</b></td><td>0.01 (+3.67%)</td><td>0.01 (-2.60%)</td><td>0.01 (-6.82%)</td><td>0.00 <b>(+127.70%)</b></td><td>255.10 (+7.32%)</td><td>206.54 (-0.99%)</td><td>214.10 (+2.64%)</td><td>146.40 (-19.38%)</td><td>39.96 <b>(+90.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>237.70 (n/a)</td><td>208.60 (n/a)</td><td>208.60 (n/a)</td><td>181.60 (n/a)</td><td>20.93 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-1.59%)</td><td>0.03 (-13.52%)</td><td>0.03 <b>(-23.58%)</b></td><td>0.02 (+2.09%)</td><td>0.01 (-7.98%)</td><td>221.00 (-2.08%)</td><td>177.74 (+14.58%)</td><td>188.00 <b>(+30.83%)</b></td><td>128.50 (+1.58%)</td><td>34.63 (-13.97%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>155.12 (n/a)</td><td>143.70 (n/a)</td><td>126.50 (n/a)</td><td>40.25 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 <b>(+21.34%)</b></td><td>0.03 (-7.10%)</td><td>0.04 (+2.17%)</td><td>0.01 <b>(-37.11%)</b></td><td>0.01 <b>(+114.66%)</b></td><td>372.90 <b>(+59.02%)</b></td><td>206.62 <b>(+27.83%)</b></td><td>146.30 (-2.07%)</td><td>110.90 (-17.61%)</td><td>112.90 <b>(+173.48%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>161.64 (n/a)</td><td>149.40 (n/a)</td><td>134.60 (n/a)</td><td>41.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-13.26%)</td><td>0.03 (-3.42%)</td><td>0.03 (+6.58%)</td><td>0.03 (+17.63%)</td><td>0.00 <b>(-62.29%)</b></td><td>192.80 (-14.99%)</td><td>174.92 (-1.91%)</td><td>178.90 (-6.19%)</td><td>147.30 (+15.35%)</td><td>18.30 <b>(-61.89%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>178.32 (n/a)</td><td>190.70 (n/a)</td><td>127.70 (n/a)</td><td>48.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-9.21%)</td><td>0.03 (-10.13%)</td><td>0.03 (-8.89%)</td><td>0.02 <b>(-20.25%)</b></td><td>0.01 (+17.54%)</td><td>227.80 <b>(+25.44%)</b></td><td>182.48 (+13.03%)</td><td>192.60 (+9.81%)</td><td>140.60 (+10.10%)</td><td>37.28 <b>(+56.56%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.60 (n/a)</td><td>161.44 (n/a)</td><td>175.40 (n/a)</td><td>127.70 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (+13.11%)</td><td>0.04 (+2.42%)</td><td>0.03 (+0.78%)</td><td>0.03 (-10.86%)</td><td>0.01 <b>(+61.94%)</b></td><td>200.10 (+12.16%)</td><td>158.06 (+1.05%)</td><td>158.10 (-0.75%)</td><td>105.10 (-11.61%)</td><td>39.69 <b>(+63.31%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>156.42 (n/a)</td><td>159.30 (n/a)</td><td>118.90 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 <b>(-27.38%)</b></td><td>0.03 (-9.47%)</td><td>0.03 (-0.60%)</td><td>0.02 (+4.12%)</td><td>0.00 <b>(-59.28%)</b></td><td>214.10 (-3.99%)</td><td>184.88 (+6.42%)</td><td>179.40 (+0.62%)</td><td>160.70 <b>(+37.70%)</b></td><td>22.18 <b>(-44.83%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>173.72 (n/a)</td><td>178.30 (n/a)</td><td>116.70 (n/a)</td><td>40.21 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-12.21%)</td><td>0.03 (-0.79%)</td><td>0.03 (-3.13%)</td><td>0.02 <b>(+30.13%)</b></td><td>0.00 <b>(-45.84%)</b></td><td>222.80 <b>(-23.15%)</b></td><td>185.10 (-5.14%)</td><td>193.10 (+3.21%)</td><td>142.50 (+13.91%)</td><td>29.58 <b>(-53.52%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>289.90 (n/a)</td><td>195.12 (n/a)</td><td>187.10 (n/a)</td><td>125.10 (n/a)</td><td>63.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 <b>(+20.75%)</b></td><td>0.03 <b>(+21.32%)</b></td><td>0.03 (+19.81%)</td><td>0.02 <b>(+47.65%)</b></td><td>0.00 <b>(-26.13%)</b></td><td>224.50 <b>(-32.28%)</b></td><td>202.30 (-19.07%)</td><td>204.30 (-16.54%)</td><td>171.70 (-17.17%)</td><td>19.23 <b>(-60.35%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>331.50 (n/a)</td><td>249.98 (n/a)</td><td>244.80 (n/a)</td><td>207.30 (n/a)</td><td>48.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (+7.05%)</td><td>0.07 (+7.35%)</td><td>0.07 (+4.19%)</td><td>0.05 (+4.52%)</td><td>0.01 (+5.70%)</td><td>196.80 (-4.33%)</td><td>162.96 (-6.89%)</td><td>154.40 (-4.04%)</td><td>138.90 (-6.59%)</td><td>24.82 (-7.72%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>175.02 (n/a)</td><td>160.90 (n/a)</td><td>148.70 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 <b>(+21.66%)</b></td><td>0.07 <b>(+36.57%)</b></td><td>0.07 <b>(+21.19%)</b></td><td>0.06 <b>(+79.48%)</b></td><td>0.01 <b>(-29.36%)</b></td><td>182.60 <b>(-44.28%)</b></td><td>159.36 <b>(-32.11%)</b></td><td>156.60 (-17.49%)</td><td>121.80 (-17.81%)</td><td>25.12 <b>(-69.50%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>327.70 (n/a)</td><td>234.72 (n/a)</td><td>189.80 (n/a)</td><td>148.20 (n/a)</td><td>82.38 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (+4.05%)</td><td>0.07 (-0.89%)</td><td>0.07 (-1.49%)</td><td>0.06 (-5.04%)</td><td>0.01 <b>(+25.49%)</b></td><td>182.70 (+5.30%)</td><td>156.24 (+1.65%)</td><td>156.40 (+1.49%)</td><td>118.70 (-3.89%)</td><td>23.72 <b>(+26.04%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>173.50 (n/a)</td><td>153.70 (n/a)</td><td>154.10 (n/a)</td><td>123.50 (n/a)</td><td>18.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (+0.89%)</td><td>0.06 (-10.70%)</td><td>0.06 (-15.42%)</td><td>0.04 (-14.84%)</td><td>0.02 <b>(+24.27%)</b></td><td>285.20 (+17.41%)</td><td>194.06 (+15.13%)</td><td>178.90 (+18.16%)</td><td>136.60 (-0.94%)</td><td>59.56 <b>(+39.72%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>242.90 (n/a)</td><td>168.56 (n/a)</td><td>151.40 (n/a)</td><td>137.90 (n/a)</td><td>42.62 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (+8.85%)</td><td>0.07 (+4.56%)</td><td>0.06 (+2.91%)</td><td>0.05 (-3.65%)</td><td>0.01 <b>(+40.26%)</b></td><td>225.90 (+3.81%)</td><td>166.32 (-2.69%)</td><td>162.30 (-2.87%)</td><td>131.80 (-8.15%)</td><td>38.42 <b>(+30.89%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>170.92 (n/a)</td><td>167.10 (n/a)</td><td>143.50 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (+18.17%)</td><td>0.07 <b>(+26.65%)</b></td><td>0.07 <b>(+26.59%)</b></td><td>0.07 <b>(+39.45%)</b></td><td>0.01 <b>(-24.38%)</b></td><td>159.60 <b>(-28.30%)</b></td><td>145.82 <b>(-21.76%)</b></td><td>142.90 <b>(-21.01%)</b></td><td>132.40 (-15.35%)</td><td>11.58 <b>(-54.07%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>186.38 (n/a)</td><td>180.90 (n/a)</td><td>156.40 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (+12.00%)</td><td>0.06 (+12.80%)</td><td>0.06 (-0.97%)</td><td>0.05 (+13.71%)</td><td>0.01 (-1.77%)</td><td>199.20 (-12.09%)</td><td>164.18 (-11.88%)</td><td>168.70 (+0.96%)</td><td>140.80 (-10.72%)</td><td>23.92 <b>(-25.10%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>186.32 (n/a)</td><td>167.10 (n/a)</td><td>157.70 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (-13.29%)</td><td>0.05 (-4.87%)</td><td>0.05 (-1.52%)</td><td>0.05 (+5.14%)</td><td>0.00 <b>(-65.59%)</b></td><td>232.50 (-4.91%)</td><td>216.56 (+3.47%)</td><td>214.10 (+1.52%)</td><td>202.70 (+15.30%)</td><td>11.93 <b>(-61.89%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>244.50 (n/a)</td><td>209.30 (n/a)</td><td>210.90 (n/a)</td><td>175.80 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (+4.37%)</td><td>0.13 (-8.57%)</td><td>0.11 (-18.33%)</td><td>0.09 <b>(-29.36%)</b></td><td>0.04 <b>(+173.66%)</b></td><td>232.70 <b>(+41.55%)</b></td><td>178.32 (+16.11%)</td><td>193.00 <b>(+22.38%)</b></td><td>124.50 (-4.23%)</td><td>49.24 <b>(+264.51%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>164.40 (n/a)</td><td>153.58 (n/a)</td><td>157.70 (n/a)</td><td>130.00 (n/a)</td><td>13.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 <b>(+27.72%)</b></td><td>0.13 (+2.21%)</td><td>0.12 (-7.67%)</td><td>0.08 <b>(-25.59%)</b></td><td>0.04 <b>(+295.43%)</b></td><td>253.20 <b>(+34.39%)</b></td><td>176.20 (+6.09%)</td><td>180.80 (+8.26%)</td><td>118.40 <b>(-21.69%)</b></td><td>57.27 <b>(+293.98%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>188.40 (n/a)</td><td>166.08 (n/a)</td><td>167.00 (n/a)</td><td>151.20 (n/a)</td><td>14.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (-4.07%)</td><td>0.13 (-11.12%)</td><td>0.11 <b>(-30.76%)</b></td><td>0.11 (+5.21%)</td><td>0.03 (-6.14%)</td><td>194.20 (-4.94%)</td><td>165.90 (+12.00%)</td><td>185.10 <b>(+44.38%)</b></td><td>120.60 (+4.24%)</td><td>35.06 (-5.10%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>204.30 (n/a)</td><td>148.12 (n/a)</td><td>128.20 (n/a)</td><td>115.70 (n/a)</td><td>36.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 <b>(+30.95%)</b></td><td>0.12 (-2.23%)</td><td>0.10 (-15.40%)</td><td>0.10 (-5.41%)</td><td>0.03 <b>(+151.64%)</b></td><td>203.90 (+5.70%)</td><td>180.02 (+6.19%)</td><td>200.30 (+18.24%)</td><td>115.60 <b>(-23.65%)</b></td><td>37.52 <b>(+104.46%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>169.52 (n/a)</td><td>169.40 (n/a)</td><td>151.40 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (-3.44%)</td><td>0.12 (-0.80%)</td><td>0.12 (-13.62%)</td><td>0.09 <b>(+25.33%)</b></td><td>0.02 <b>(-29.47%)</b></td><td>225.10 <b>(-20.21%)</b></td><td>174.28 (-3.26%)</td><td>174.20 (+15.75%)</td><td>139.40 (+3.57%)</td><td>33.72 <b>(-43.78%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>282.10 (n/a)</td><td>180.16 (n/a)</td><td>150.50 (n/a)</td><td>134.60 (n/a)</td><td>59.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (+3.11%)</td><td>0.13 (+9.99%)</td><td>0.13 (+19.71%)</td><td>0.10 (-4.86%)</td><td>0.02 <b>(+38.99%)</b></td><td>208.50 (+5.09%)</td><td>169.26 (-8.48%)</td><td>157.50 (-16.49%)</td><td>152.60 (-2.99%)</td><td>23.30 <b>(+44.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>184.94 (n/a)</td><td>188.60 (n/a)</td><td>157.30 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (-10.77%)</td><td>0.12 (-11.72%)</td><td>0.11 (-14.34%)</td><td>0.10 (-14.27%)</td><td>0.02 (+3.03%)</td><td>219.50 (+16.63%)</td><td>184.36 (+14.03%)</td><td>183.30 (+16.75%)</td><td>149.00 (+12.11%)</td><td>32.02 <b>(+32.54%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>161.68 (n/a)</td><td>157.00 (n/a)</td><td>132.90 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (-6.28%)</td><td>0.09 (-11.78%)</td><td>0.09 (-12.42%)</td><td>0.05 <b>(-22.66%)</b></td><td>0.02 (+14.87%)</td><td>385.20 <b>(+29.31%)</b></td><td>256.30 (+16.34%)</td><td>232.20 (+14.16%)</td><td>185.40 (+6.67%)</td><td>76.10 <b>(+61.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>297.90 (n/a)</td><td>220.30 (n/a)</td><td>203.40 (n/a)</td><td>173.80 (n/a)</td><td>47.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>163.10 (n/a)</td><td>176.10 (n/a)</td><td>135.40 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>162.90 (n/a)</td><td>153.70 (n/a)</td><td>145.80 (n/a)</td><td>19.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.70 (n/a)</td><td>173.52 (n/a)</td><td>173.80 (n/a)</td><td>161.40 (n/a)</td><td>13.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.80 (n/a)</td><td>182.26 (n/a)</td><td>194.30 (n/a)</td><td>145.60 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.00 (n/a)</td><td>158.06 (n/a)</td><td>167.90 (n/a)</td><td>119.40 (n/a)</td><td>25.23 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>158.10 (n/a)</td><td>143.94 (n/a)</td><td>145.20 (n/a)</td><td>131.90 (n/a)</td><td>9.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>169.10 (n/a)</td><td>166.60 (n/a)</td><td>151.40 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.90 (n/a)</td><td>166.26 (n/a)</td><td>179.60 (n/a)</td><td>139.50 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>178.60 (n/a)</td><td>155.90 (n/a)</td><td>149.00 (n/a)</td><td>135.30 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>177.80 (n/a)</td><td>152.46 (n/a)</td><td>147.90 (n/a)</td><td>120.10 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.90 (n/a)</td><td>179.42 (n/a)</td><td>170.90 (n/a)</td><td>145.10 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>176.92 (n/a)</td><td>178.40 (n/a)</td><td>158.70 (n/a)</td><td>11.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.38 <b>(+32.18%)</b></td><td>0.32 (+17.98%)</td><td>0.32 (+15.07%)</td><td>0.28 (+11.93%)</td><td>0.04 <b>(+134.30%)</b></td><td>175.90 (-10.67%)</td><td>156.60 (-14.55%)</td><td>154.80 (-13.08%)</td><td>130.60 <b>(-24.33%)</b></td><td>17.96 <b>(+58.27%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>196.90 (n/a)</td><td>183.26 (n/a)</td><td>178.10 (n/a)</td><td>172.60 (n/a)</td><td>11.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>300.00 (n/a)</td><td>182.58 (n/a)</td><td>154.70 (n/a)</td><td>127.60 (n/a)</td><td>67.94 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>187.50 (n/a)</td><td>164.68 (n/a)</td><td>166.00 (n/a)</td><td>142.70 (n/a)</td><td>18.78 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>194.20 (n/a)</td><td>181.92 (n/a)</td><td>179.40 (n/a)</td><td>168.80 (n/a)</td><td>10.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>166.40 (n/a)</td><td>152.00 (n/a)</td><td>160.70 (n/a)</td><td>135.00 (n/a)</td><td>15.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>185.40 (n/a)</td><td>164.76 (n/a)</td><td>163.00 (n/a)</td><td>140.50 (n/a)</td><td>19.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>168.70 (n/a)</td><td>156.34 (n/a)</td><td>161.60 (n/a)</td><td>141.60 (n/a)</td><td>11.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>294.30 (n/a)</td><td>209.06 (n/a)</td><td>182.00 (n/a)</td><td>157.20 (n/a)</td><td>60.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>153.46 (n/a)</td><td>155.20 (n/a)</td><td>131.50 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>164.32 (n/a)</td><td>151.80 (n/a)</td><td>143.90 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>275.20 (n/a)</td><td>183.26 (n/a)</td><td>152.90 (n/a)</td><td>132.10 (n/a)</td><td>62.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>183.20 (n/a)</td><td>181.30 (n/a)</td><td>157.70 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>179.00 (n/a)</td><td>155.60 (n/a)</td><td>153.20 (n/a)</td><td>135.20 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>210.00 (n/a)</td><td>162.14 (n/a)</td><td>156.20 (n/a)</td><td>125.50 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>178.20 (n/a)</td><td>161.16 (n/a)</td><td>164.20 (n/a)</td><td>145.40 (n/a)</td><td>13.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.10 (n/a)</td><td>180.60 (n/a)</td><td>188.20 (n/a)</td><td>155.10 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.01 (n/a)</td><td>176.70 (n/a)</td><td>163.84 (n/a)</td><td>164.80 (n/a)</td><td>156.00 (n/a)</td><td>8.34 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>208.40 (n/a)</td><td>160.90 (n/a)</td><td>154.30 (n/a)</td><td>127.40 (n/a)</td><td>34.87 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>201.80 (n/a)</td><td>182.56 (n/a)</td><td>177.70 (n/a)</td><td>168.30 (n/a)</td><td>13.71 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>150.54 (n/a)</td><td>140.10 (n/a)</td><td>118.90 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>160.30 (n/a)</td><td>174.20 (n/a)</td><td>125.50 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.50 (n/a)</td><td>164.84 (n/a)</td><td>167.40 (n/a)</td><td>128.90 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.20 (n/a)</td><td>167.20 (n/a)</td><td>157.90 (n/a)</td><td>127.90 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.80 (n/a)</td><td>164.36 (n/a)</td><td>167.80 (n/a)</td><td>145.90 (n/a)</td><td>17.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.30 (n/a)</td><td>196.78 (n/a)</td><td>191.20 (n/a)</td><td>172.60 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.90 (n/a)</td><td>164.96 (n/a)</td><td>150.10 (n/a)</td><td>134.60 (n/a)</td><td>34.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>209.32 (n/a)</td><td>219.40 (n/a)</td><td>168.00 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>168.98 (n/a)</td><td>152.60 (n/a)</td><td>119.50 (n/a)</td><td>42.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>182.72 (n/a)</td><td>179.80 (n/a)</td><td>147.90 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>160.68 (n/a)</td><td>151.90 (n/a)</td><td>142.80 (n/a)</td><td>26.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>181.14 (n/a)</td><td>197.00 (n/a)</td><td>117.50 (n/a)</td><td>41.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.40 (n/a)</td><td>201.20 (n/a)</td><td>208.80 (n/a)</td><td>174.80 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.30 (n/a)</td><td>234.60 (n/a)</td><td>235.00 (n/a)</td><td>199.20 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.40 (n/a)</td><td>194.18 (n/a)</td><td>169.50 (n/a)</td><td>151.20 (n/a)</td><td>44.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>335.10 (n/a)</td><td>228.06 (n/a)</td><td>208.90 (n/a)</td><td>171.60 (n/a)</td><td>62.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>184.12 (n/a)</td><td>181.80 (n/a)</td><td>143.20 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.10 (n/a)</td><td>184.92 (n/a)</td><td>180.10 (n/a)</td><td>123.90 (n/a)</td><td>43.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>218.40 (n/a)</td><td>162.20 (n/a)</td><td>171.50 (n/a)</td><td>120.80 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>257.00 (n/a)</td><td>174.24 (n/a)</td><td>171.70 (n/a)</td><td>119.80 (n/a)</td><td>55.21 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>198.20 (n/a)</td><td>150.14 (n/a)</td><td>159.00 (n/a)</td><td>107.70 (n/a)</td><td>38.80 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>171.50 (n/a)</td><td>173.30 (n/a)</td><td>138.50 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.10 (n/a)</td><td>170.50 (n/a)</td><td>171.80 (n/a)</td><td>122.30 (n/a)</td><td>37.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>200.64 (n/a)</td><td>186.80 (n/a)</td><td>171.50 (n/a)</td><td>31.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.90 (n/a)</td><td>177.74 (n/a)</td><td>178.30 (n/a)</td><td>142.10 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.40 (n/a)</td><td>172.98 (n/a)</td><td>162.10 (n/a)</td><td>138.40 (n/a)</td><td>29.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.10 (n/a)</td><td>158.08 (n/a)</td><td>161.60 (n/a)</td><td>130.50 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.60 (n/a)</td><td>165.38 (n/a)</td><td>159.00 (n/a)</td><td>153.60 (n/a)</td><td>15.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.50 (n/a)</td><td>165.10 (n/a)</td><td>156.30 (n/a)</td><td>141.70 (n/a)</td><td>22.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.50 (n/a)</td><td>191.16 (n/a)</td><td>192.40 (n/a)</td><td>170.40 (n/a)</td><td>16.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>237.50 (n/a)</td><td>203.16 (n/a)</td><td>193.20 (n/a)</td><td>181.10 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>4.43 (+6.64%)</td><td>4.13 (+2.66%)</td><td>4.18 (+4.69%)</td><td>3.62 (-8.61%)</td><td>0.31 <b>(+274.62%)</b></td><td>2600.30 (+9.42%)</td><td>2286.32 (-2.14%)</td><td>2250.80 (-4.48%)</td><td>2121.30 (-6.23%)</td><td>185.86 <b>(+289.65%)</b></td><td>1743.96 (+6.64%)</td><td>1626.03 (+2.66%)</td><td>1643.57 (+4.69%)</td><td>1422.65 (-8.61%)</td><td>122.95 <b>(+274.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>4.16 (n/a)</td><td>4.03 (n/a)</td><td>3.99 (n/a)</td><td>3.96 (n/a)</td><td>0.08 (n/a)</td><td>2376.40 (n/a)</td><td>2336.38 (n/a)</td><td>2356.40 (n/a)</td><td>2262.20 (n/a)</td><td>47.70 (n/a)</td><td>1635.33 (n/a)</td><td>1583.93 (n/a)</td><td>1569.91 (n/a)</td><td>1556.74 (n/a)</td><td>32.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.24 (+3.95%)</td><td>1.12 (+15.73%)</td><td>1.10 (+15.65%)</td><td>0.99 <b>(+46.38%)</b></td><td>0.11 <b>(-43.56%)</b></td><td>224.00 <b>(-31.69%)</b></td><td>198.66 (-16.16%)</td><td>200.90 (-13.52%)</td><td>177.90 (-3.79%)</td><td>19.79 <b>(-64.25%)</b></td><td>53.06 (+3.95%)</td><td>47.88 (+15.73%)</td><td>46.98 (+15.65%)</td><td>42.13 <b>(+46.38%)</b></td><td>4.77 <b>(-43.56%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>1.20 (n/a)</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.67 (n/a)</td><td>0.20 (n/a)</td><td>327.90 (n/a)</td><td>236.96 (n/a)</td><td>232.30 (n/a)</td><td>184.90 (n/a)</td><td>55.35 (n/a)</td><td>51.04 (n/a)</td><td>41.38 (n/a)</td><td>40.62 (n/a)</td><td>28.78 (n/a)</td><td>8.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.34 <b>(+27.20%)</b></td><td>1.07 <b>(+23.82%)</b></td><td>1.03 (+3.89%)</td><td>0.92 <b>(+54.56%)</b></td><td>0.16 <b>(-21.78%)</b></td><td>239.40 <b>(-35.31%)</b></td><td>209.66 <b>(-22.16%)</b></td><td>214.70 (-3.77%)</td><td>165.60 <b>(-21.40%)</b></td><td>29.43 <b>(-59.79%)</b></td><td>56.98 <b>(+27.20%)</b></td><td>45.79 <b>(+23.82%)</b></td><td>43.95 (+3.89%)</td><td>39.41 <b>(+54.56%)</b></td><td>7.04 <b>(-21.78%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>1.05 (n/a)</td><td>0.87 (n/a)</td><td>0.99 (n/a)</td><td>0.60 (n/a)</td><td>0.21 (n/a)</td><td>370.10 (n/a)</td><td>269.36 (n/a)</td><td>223.10 (n/a)</td><td>210.70 (n/a)</td><td>73.20 (n/a)</td><td>44.79 (n/a)</td><td>36.98 (n/a)</td><td>42.30 (n/a)</td><td>25.50 (n/a)</td><td>8.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.52 (-0.06%)</td><td>0.52 (-0.05%)</td><td>0.52 (-0.07%)</td><td>0.52 (-0.04%)</td><td>0.00 (-14.14%)</td><td>48687.60 (+0.04%)</td><td>48654.26 (+0.05%)</td><td>48655.20 (+0.07%)</td><td>48630.20 (+0.06%)</td><td>22.85 (-14.11%)</td><td>353.28 (-0.06%)</td><td>353.10 (-0.05%)</td><td>353.09 (-0.07%)</td><td>352.86 (-0.04%)</td><td>0.17 (-14.13%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48670.00 (n/a)</td><td>48631.36 (n/a)</td><td>48618.80 (n/a)</td><td>48603.40 (n/a)</td><td>26.61 (n/a)</td><td>353.47 (n/a)</td><td>353.27 (n/a)</td><td>353.36 (n/a)</td><td>352.99 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (-1.76%)</td><td>0.21 (-1.22%)</td><td>0.21 (-1.70%)</td><td>0.21 (-0.82%)</td><td>0.00 <b>(-39.85%)</b></td><td>121163.60 (+0.83%)</td><td>119929.88 (+1.22%)</td><td>120213.40 (+1.73%)</td><td>118375.00 (+1.79%)</td><td>1026.77 <b>(-38.50%)</b></td><td>145.13 (-1.76%)</td><td>143.26 (-1.22%)</td><td>142.91 (-1.70%)</td><td>141.79 (-0.82%)</td><td>1.23 <b>(-39.85%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120168.80 (n/a)</td><td>118483.24 (n/a)</td><td>118166.90 (n/a)</td><td>116292.30 (n/a)</td><td>1669.64 (n/a)</td><td>147.73 (n/a)</td><td>145.02 (n/a)</td><td>145.39 (n/a)</td><td>142.96 (n/a)</td><td>2.05 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.88 (+0.22%)</td><td>0.88 (+0.21%)</td><td>0.88 (+0.11%)</td><td>0.87 (-0.27%)</td><td>0.01 <b>(+25.30%)</b></td><td>28970.70 (+0.27%)</td><td>28649.40 (-0.21%)</td><td>28628.50 (-0.11%)</td><td>28448.50 (-0.22%)</td><td>194.25 <b>(+25.47%)</b></td><td>603.89 (+0.22%)</td><td>599.68 (+0.21%)</td><td>600.10 (+0.11%)</td><td>593.01 (-0.27%)</td><td>4.04 <b>(+25.30%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.00 (n/a)</td><td>28892.50 (n/a)</td><td>28708.92 (n/a)</td><td>28660.40 (n/a)</td><td>28511.20 (n/a)</td><td>154.82 (n/a)</td><td>602.57 (n/a)</td><td>598.43 (n/a)</td><td>599.43 (n/a)</td><td>594.61 (n/a)</td><td>3.23 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.53 (+0.56%)</td><td>3.45 (+2.05%)</td><td>3.51 (+4.39%)</td><td>3.33 (+2.56%)</td><td>0.10 (-18.71%)</td><td>7553.70 (-2.50%)</td><td>7296.80 (-2.05%)</td><td>7172.40 (-4.21%)</td><td>7125.00 (-0.56%)</td><td>212.63 <b>(-20.91%)</b></td><td>2411.22 (+0.56%)</td><td>2356.03 (+2.05%)</td><td>2395.29 (+4.39%)</td><td>2274.37 (+2.56%)</td><td>67.94 (-18.71%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.51 (n/a)</td><td>3.38 (n/a)</td><td>3.36 (n/a)</td><td>3.25 (n/a)</td><td>0.12 (n/a)</td><td>7747.20 (n/a)</td><td>7449.48 (n/a)</td><td>7487.50 (n/a)</td><td>7165.20 (n/a)</td><td>268.84 (n/a)</td><td>2397.69 (n/a)</td><td>2308.59 (n/a)</td><td>2294.46 (n/a)</td><td>2217.55 (n/a)</td><td>83.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>2.85 (-0.13%)</td><td>2.75 (-2.03%)</td><td>2.71 (-3.77%)</td><td>2.69 (-2.22%)</td><td>0.07 <b>(+63.01%)</b></td><td>9370.00 (+2.27%)</td><td>9171.74 (+2.10%)</td><td>9295.90 (+3.91%)</td><td>8817.20 (+0.13%)</td><td>227.10 <b>(+66.70%)</b></td><td>1948.46 (-0.13%)</td><td>1874.07 (-2.03%)</td><td>1848.11 (-3.77%)</td><td>1833.49 (-2.22%)</td><td>47.26 <b>(+63.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>2.86 (n/a)</td><td>2.80 (n/a)</td><td>2.81 (n/a)</td><td>2.75 (n/a)</td><td>0.04 (n/a)</td><td>9161.80 (n/a)</td><td>8983.10 (n/a)</td><td>8945.70 (n/a)</td><td>8805.80 (n/a)</td><td>136.23 (n/a)</td><td>1950.97 (n/a)</td><td>1912.81 (n/a)</td><td>1920.46 (n/a)</td><td>1875.15 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.33 (-3.52%)</td><td>3.20 (-1.38%)</td><td>3.23 (+1.19%)</td><td>3.08 (-1.94%)</td><td>0.11 (-13.53%)</td><td>8182.20 (+1.97%)</td><td>7860.72 (+1.37%)</td><td>7800.90 (-1.17%)</td><td>7560.80 (+3.65%)</td><td>279.50 (-8.42%)</td><td>2272.23 (-3.52%)</td><td>2187.74 (-1.38%)</td><td>2202.30 (+1.19%)</td><td>2099.65 (-1.94%)</td><td>77.43 (-13.53%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.45 (n/a)</td><td>3.25 (n/a)</td><td>3.19 (n/a)</td><td>3.14 (n/a)</td><td>0.13 (n/a)</td><td>8023.90 (n/a)</td><td>7754.20 (n/a)</td><td>7893.60 (n/a)</td><td>7294.70 (n/a)</td><td>305.20 (n/a)</td><td>2355.12 (n/a)</td><td>2218.38 (n/a)</td><td>2176.44 (n/a)</td><td>2141.08 (n/a)</td><td>89.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.78 (+0.02%)</td><td>0.78 (-0.00%)</td><td>0.78 (+0.03%)</td><td>0.78 (-0.10%)</td><td>0.00 <b>(+195.30%)</b></td><td>96586.50 (+0.10%)</td><td>96470.88 (+0.00%)</td><td>96446.90 (-0.03%)</td><td>96423.00 (-0.02%)</td><td>65.74 <b>(+195.60%)</b></td><td>712.69 (+0.02%)</td><td>712.33 (-0.00%)</td><td>712.51 (+0.03%)</td><td>711.48 (-0.10%)</td><td>0.48 <b>(+195.28%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96492.70 (n/a)</td><td>96466.46 (n/a)</td><td>96475.20 (n/a)</td><td>96437.50 (n/a)</td><td>22.24 (n/a)</td><td>712.58 (n/a)</td><td>712.37 (n/a)</td><td>712.30 (n/a)</td><td>712.17 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.73 (+0.01%)</td><td>0.73 (+0.08%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.19%)</td><td>0.00 <b>(-67.08%)</b></td><td>103664.70 (-0.19%)</td><td>103625.06 (-0.08%)</td><td>103620.30 (-0.03%)</td><td>103586.70 (-0.01%)</td><td>37.68 <b>(-67.14%)</b></td><td>663.40 (+0.01%)</td><td>663.16 (+0.08%)</td><td>663.19 (+0.03%)</td><td>662.90 (+0.19%)</td><td>0.24 <b>(-67.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103865.50 (n/a)</td><td>103712.90 (n/a)</td><td>103651.60 (n/a)</td><td>103596.00 (n/a)</td><td>114.66 (n/a)</td><td>663.34 (n/a)</td><td>662.59 (n/a)</td><td>662.98 (n/a)</td><td>661.62 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.69 (+0.26%)</td><td>0.69 (+0.10%)</td><td>0.69 (+0.07%)</td><td>0.69 (+0.15%)</td><td>0.00 <b>(+20.08%)</b></td><td>109767.40 (-0.15%)</td><td>109566.36 (-0.10%)</td><td>109577.30 (-0.07%)</td><td>109209.50 (-0.26%)</td><td>220.60 (+19.58%)</td><td>629.24 (+0.26%)</td><td>627.20 (+0.10%)</td><td>627.13 (+0.07%)</td><td>626.05 (+0.15%)</td><td>1.26 <b>(+20.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109933.80 (n/a)</td><td>109674.64 (n/a)</td><td>109650.40 (n/a)</td><td>109490.90 (n/a)</td><td>184.48 (n/a)</td><td>627.63 (n/a)</td><td>626.58 (n/a)</td><td>626.71 (n/a)</td><td>625.10 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.18 (+0.73%)</td><td>6.78 (+0.53%)</td><td>6.77 (-1.52%)</td><td>6.51 (+2.53%)</td><td>0.26 <b>(-26.21%)</b></td><td>1369.30 (-2.47%)</td><td>1315.34 (-0.63%)</td><td>1315.70 (+1.54%)</td><td>1242.10 (-0.72%)</td><td>50.20 <b>(-29.03%)</b></td><td>432.22 (+0.73%)</td><td>408.64 (+0.53%)</td><td>408.05 (-1.52%)</td><td>392.07 (+2.53%)</td><td>15.84 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.12 (n/a)</td><td>6.75 (n/a)</td><td>6.88 (n/a)</td><td>6.35 (n/a)</td><td>0.36 (n/a)</td><td>1404.00 (n/a)</td><td>1323.66 (n/a)</td><td>1295.70 (n/a)</td><td>1251.10 (n/a)</td><td>70.73 (n/a)</td><td>429.11 (n/a)</td><td>406.51 (n/a)</td><td>414.34 (n/a)</td><td>382.37 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>6.97 (-2.03%)</td><td>6.85 (+13.81%)</td><td>6.85 (+1.88%)</td><td>6.69 <b>(+41.15%)</b></td><td>0.12 <b>(-89.97%)</b></td><td>1333.00 <b>(-29.15%)</b></td><td>1302.24 (-14.99%)</td><td>1301.70 (-1.85%)</td><td>1278.90 (+2.08%)</td><td>22.51 <b>(-92.97%)</b></td><td>419.80 (-2.03%)</td><td>412.37 (+13.81%)</td><td>412.44 (+1.88%)</td><td>402.74 <b>(+41.15%)</b></td><td>7.11 <b>(-89.97%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.11 (n/a)</td><td>6.02 (n/a)</td><td>6.72 (n/a)</td><td>4.74 (n/a)</td><td>1.18 (n/a)</td><td>1881.50 (n/a)</td><td>1531.82 (n/a)</td><td>1326.20 (n/a)</td><td>1252.90 (n/a)</td><td>320.33 (n/a)</td><td>428.50 (n/a)</td><td>362.32 (n/a)</td><td>404.82 (n/a)</td><td>285.34 (n/a)</td><td>70.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.08 (+0.64%)</td><td>6.85 (+4.65%)</td><td>6.91 (+5.46%)</td><td>6.40 (+2.87%)</td><td>0.28 (-17.45%)</td><td>1392.30 (-2.80%)</td><td>1302.92 (-4.51%)</td><td>1289.50 (-5.17%)</td><td>1258.70 (-0.63%)</td><td>54.26 <b>(-20.59%)</b></td><td>426.54 (+0.64%)</td><td>412.61 (+4.65%)</td><td>416.35 (+5.46%)</td><td>385.59 (+2.87%)</td><td>16.60 (-17.45%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.04 (n/a)</td><td>6.55 (n/a)</td><td>6.55 (n/a)</td><td>6.22 (n/a)</td><td>0.33 (n/a)</td><td>1432.40 (n/a)</td><td>1364.48 (n/a)</td><td>1359.80 (n/a)</td><td>1266.70 (n/a)</td><td>68.33 (n/a)</td><td>423.83 (n/a)</td><td>394.27 (n/a)</td><td>394.80 (n/a)</td><td>374.82 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.47 (+2.85%)</td><td>7.93 (-0.10%)</td><td>7.90 (+0.06%)</td><td>7.28 (-6.49%)</td><td>0.45 <b>(+165.49%)</b></td><td>4788.70 (+6.94%)</td><td>4406.70 (+0.33%)</td><td>4415.90 (-0.06%)</td><td>4118.60 (-2.78%)</td><td>254.19 <b>(+178.19%)</b></td><td>521.41 (+2.85%)</td><td>488.59 (-0.10%)</td><td>486.31 (+0.06%)</td><td>448.44 (-6.49%)</td><td>27.61 <b>(+165.49%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.23 (n/a)</td><td>7.94 (n/a)</td><td>7.89 (n/a)</td><td>7.79 (n/a)</td><td>0.17 (n/a)</td><td>4477.90 (n/a)</td><td>4392.22 (n/a)</td><td>4418.40 (n/a)</td><td>4236.20 (n/a)</td><td>91.38 (n/a)</td><td>506.94 (n/a)</td><td>489.10 (n/a)</td><td>486.04 (n/a)</td><td>479.58 (n/a)</td><td>10.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.76 (+0.57%)</td><td>7.53 (+0.18%)</td><td>7.49 (-0.83%)</td><td>7.25 (+0.14%)</td><td>0.20 (+17.05%)</td><td>4807.50 (-0.14%)</td><td>4630.66 (-0.17%)</td><td>4653.90 (+0.84%)</td><td>4494.60 (-0.57%)</td><td>124.02 (+15.50%)</td><td>477.79 (+0.57%)</td><td>464.02 (+0.18%)</td><td>461.44 (-0.83%)</td><td>446.70 (+0.14%)</td><td>12.35 (+17.05%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.71 (n/a)</td><td>7.52 (n/a)</td><td>7.55 (n/a)</td><td>7.24 (n/a)</td><td>0.17 (n/a)</td><td>4814.00 (n/a)</td><td>4638.42 (n/a)</td><td>4615.00 (n/a)</td><td>4520.40 (n/a)</td><td>107.38 (n/a)</td><td>475.07 (n/a)</td><td>463.17 (n/a)</td><td>465.32 (n/a)</td><td>446.09 (n/a)</td><td>10.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.81 (+7.12%)</td><td>7.37 (+4.09%)</td><td>7.47 (+3.75%)</td><td>6.74 (-1.27%)</td><td>0.39 <b>(+69.96%)</b></td><td>5174.00 (+1.28%)</td><td>4740.00 (-3.78%)</td><td>4665.70 (-3.62%)</td><td>4461.60 (-6.65%)</td><td>263.94 <b>(+61.93%)</b></td><td>481.32 (+7.12%)</td><td>454.14 (+4.09%)</td><td>460.27 (+3.75%)</td><td>415.05 (-1.27%)</td><td>24.28 <b>(+69.96%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>7.29 (n/a)</td><td>7.08 (n/a)</td><td>7.20 (n/a)</td><td>6.83 (n/a)</td><td>0.23 (n/a)</td><td>5108.40 (n/a)</td><td>4926.30 (n/a)</td><td>4840.80 (n/a)</td><td>4779.30 (n/a)</td><td>163.00 (n/a)</td><td>449.33 (n/a)</td><td>436.30 (n/a)</td><td>443.62 (n/a)</td><td>420.39 (n/a)</td><td>14.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.79 (-0.41%)</td><td>0.79 (-0.13%)</td><td>0.79 (-0.00%)</td><td>0.79 (-0.07%)</td><td>0.00 <b>(-56.90%)</b></td><td>95900.40 (+0.07%)</td><td>95800.36 (+0.13%)</td><td>95749.60 (+0.00%)</td><td>95724.30 (+0.41%)</td><td>85.48 <b>(-56.69%)</b></td><td>717.89 (-0.41%)</td><td>717.32 (-0.13%)</td><td>717.70 (-0.00%)</td><td>716.57 (-0.07%)</td><td>0.64 <b>(-56.90%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95833.00 (n/a)</td><td>95675.16 (n/a)</td><td>95745.50 (n/a)</td><td>95330.80 (n/a)</td><td>197.35 (n/a)</td><td>720.85 (n/a)</td><td>718.26 (n/a)</td><td>717.73 (n/a)</td><td>717.08 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.73 (+0.01%)</td><td>0.73 (+0.06%)</td><td>0.73 (-0.01%)</td><td>0.73 (+0.21%)</td><td>0.00 <b>(-53.45%)</b></td><td>103092.60 (-0.21%)</td><td>102963.44 (-0.06%)</td><td>102944.20 (+0.01%)</td><td>102895.00 (-0.01%)</td><td>77.44 <b>(-53.54%)</b></td><td>667.86 (+0.01%)</td><td>667.42 (+0.06%)</td><td>667.54 (-0.01%)</td><td>666.58 (+0.21%)</td><td>0.50 <b>(-53.45%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103307.50 (n/a)</td><td>103025.28 (n/a)</td><td>102936.30 (n/a)</td><td>102902.20 (n/a)</td><td>166.70 (n/a)</td><td>667.81 (n/a)</td><td>667.02 (n/a)</td><td>667.59 (n/a)</td><td>665.19 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.70 (+0.05%)</td><td>0.70 (+0.11%)</td><td>0.70 (+0.07%)</td><td>0.70 (+0.14%)</td><td>0.00 <b>(-26.01%)</b></td><td>108174.70 (-0.14%)</td><td>107995.38 (-0.11%)</td><td>108020.50 (-0.07%)</td><td>107831.50 (-0.05%)</td><td>131.99 <b>(-26.16%)</b></td><td>637.29 (+0.05%)</td><td>636.32 (+0.11%)</td><td>636.17 (+0.07%)</td><td>635.26 (+0.14%)</td><td>0.78 <b>(-26.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108322.30 (n/a)</td><td>108113.84 (n/a)</td><td>108101.10 (n/a)</td><td>107881.20 (n/a)</td><td>178.75 (n/a)</td><td>636.99 (n/a)</td><td>635.62 (n/a)</td><td>635.70 (n/a)</td><td>634.40 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.79 (-2.95%)</td><td>3.64 (-0.07%)</td><td>3.61 (-2.09%)</td><td>3.48 (+5.10%)</td><td>0.12 <b>(-53.14%)</b></td><td>2316.50 (-4.85%)</td><td>2219.08 (-0.26%)</td><td>2230.10 (+2.14%)</td><td>2127.00 (+3.05%)</td><td>74.71 <b>(-54.05%)</b></td><td>993.87 (-2.95%)</td><td>953.48 (-0.07%)</td><td>947.90 (-2.09%)</td><td>912.54 (+5.10%)</td><td>32.12 <b>(-53.14%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.91 (n/a)</td><td>3.64 (n/a)</td><td>3.69 (n/a)</td><td>3.31 (n/a)</td><td>0.26 (n/a)</td><td>2434.60 (n/a)</td><td>2224.78 (n/a)</td><td>2183.40 (n/a)</td><td>2064.10 (n/a)</td><td>162.60 (n/a)</td><td>1024.13 (n/a)</td><td>954.17 (n/a)</td><td>968.17 (n/a)</td><td>868.27 (n/a)</td><td>68.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.51 <b>(+52.05%)</b></td><td>0.37 <b>(+21.33%)</b></td><td>0.36 (+10.88%)</td><td>0.30 (+12.48%)</td><td>0.08 <b>(+185.30%)</b></td><td>4097.80 (-11.10%)</td><td>3449.44 (-15.48%)</td><td>3488.40 (-9.81%)</td><td>2431.20 <b>(-34.23%)</b></td><td>633.12 <b>(+60.82%)</b></td><td>27.60 <b>(+52.04%)</b></td><td>20.10 <b>(+21.33%)</b></td><td>19.24 (+10.88%)</td><td>16.38 (+12.48%)</td><td>4.41 <b>(+185.30%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>4609.20 (n/a)</td><td>4081.22 (n/a)</td><td>3868.00 (n/a)</td><td>3696.50 (n/a)</td><td>393.68 (n/a)</td><td>18.15 (n/a)</td><td>16.56 (n/a)</td><td>17.35 (n/a)</td><td>14.56 (n/a)</td><td>1.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.29 (-14.71%)</td><td>4.51 (-4.90%)</td><td>4.77 (-0.89%)</td><td>3.70 (+14.05%)</td><td>0.69 <b>(-33.94%)</b></td><td>1797.60 (-12.32%)</td><td>1502.92 (+2.72%)</td><td>1395.10 (+0.90%)</td><td>1258.20 (+17.25%)</td><td>239.48 <b>(-33.12%)</b></td><td>1633.43 (-14.71%)</td><td>1394.69 (-4.90%)</td><td>1473.17 (-0.89%)</td><td>1143.30 (+14.05%)</td><td>214.10 <b>(-33.94%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>6.20 (n/a)</td><td>4.75 (n/a)</td><td>4.81 (n/a)</td><td>3.24 (n/a)</td><td>1.05 (n/a)</td><td>2050.20 (n/a)</td><td>1463.06 (n/a)</td><td>1382.70 (n/a)</td><td>1073.10 (n/a)</td><td>358.09 (n/a)</td><td>1915.18 (n/a)</td><td>1466.48 (n/a)</td><td>1486.33 (n/a)</td><td>1002.44 (n/a)</td><td>324.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 <b>(+55.62%)</b></td><td>0.23 <b>(+31.25%)</b></td><td>0.23 <b>(+25.97%)</b></td><td>0.16 (+5.28%)</td><td>0.05 <b>(+191.91%)</b></td><td>0.29 <b>(+55.62%)</b></td><td>0.23 <b>(+31.25%)</b></td><td>0.23 <b>(+25.97%)</b></td><td>0.16 (+5.28%)</td><td>0.05 <b>(+191.92%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.28 (-0.40%)</td><td>12.52 (-3.28%)</td><td>12.24 (-7.66%)</td><td>11.65 (+0.41%)</td><td>0.71 (-5.86%)</td><td>13.27 (-0.40%)</td><td>12.52 (-3.28%)</td><td>12.24 (-7.66%)</td><td>11.65 (+0.41%)</td><td>0.71 (-5.86%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.33 (n/a)</td><td>12.95 (n/a)</td><td>13.26 (n/a)</td><td>11.60 (n/a)</td><td>0.75 (n/a)</td><td>13.32 (n/a)</td><td>12.94 (n/a)</td><td>13.25 (n/a)</td><td>11.60 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>24.57 (-1.31%)</td><td>24.46 (+1.56%)</td><td>24.50 (+2.44%)</td><td>24.24 (+2.95%)</td><td>0.13 <b>(-76.13%)</b></td><td>24.55 (-1.31%)</td><td>24.44 (+1.56%)</td><td>24.49 (+2.44%)</td><td>24.23 (+2.95%)</td><td>0.13 <b>(-76.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>24.90 (n/a)</td><td>24.08 (n/a)</td><td>23.92 (n/a)</td><td>23.55 (n/a)</td><td>0.53 (n/a)</td><td>24.88 (n/a)</td><td>24.06 (n/a)</td><td>23.91 (n/a)</td><td>23.54 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>40.97 (+0.61%)</td><td>39.68 (-0.84%)</td><td>39.46 (-2.90%)</td><td>39.10 (+1.48%)</td><td>0.74 <b>(-23.55%)</b></td><td>40.94 (+0.61%)</td><td>39.65 (-0.84%)</td><td>39.44 (-2.90%)</td><td>39.08 (+1.48%)</td><td>0.74 <b>(-23.55%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>40.72 (n/a)</td><td>40.01 (n/a)</td><td>40.64 (n/a)</td><td>38.53 (n/a)</td><td>0.97 (n/a)</td><td>40.70 (n/a)</td><td>39.99 (n/a)</td><td>40.62 (n/a)</td><td>38.51 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>45.55 (+0.48%)</td><td>44.79 (+3.32%)</td><td>45.47 (+4.02%)</td><td>43.10 (+3.58%)</td><td>1.08 <b>(-28.41%)</b></td><td>45.52 (+0.48%)</td><td>44.76 (+3.32%)</td><td>45.44 (+4.02%)</td><td>43.07 (+3.58%)</td><td>1.08 <b>(-28.41%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>45.33 (n/a)</td><td>43.35 (n/a)</td><td>43.72 (n/a)</td><td>41.61 (n/a)</td><td>1.51 (n/a)</td><td>45.30 (n/a)</td><td>43.32 (n/a)</td><td>43.69 (n/a)</td><td>41.58 (n/a)</td><td>1.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.61 (+2.27%)</td><td>12.57 (-2.95%)</td><td>13.22 (-0.05%)</td><td>10.64 (-14.46%)</td><td>1.21 <b>(+191.73%)</b></td><td>13.60 (+2.27%)</td><td>12.57 (-2.95%)</td><td>13.21 (-0.05%)</td><td>10.63 (-14.46%)</td><td>1.21 <b>(+191.73%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.31 (n/a)</td><td>12.95 (n/a)</td><td>13.23 (n/a)</td><td>12.44 (n/a)</td><td>0.42 (n/a)</td><td>13.30 (n/a)</td><td>12.95 (n/a)</td><td>13.22 (n/a)</td><td>12.43 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>25.72 (+5.87%)</td><td>24.88 (+4.27%)</td><td>24.91 (+3.31%)</td><td>24.29 (+6.82%)</td><td>0.54 (-15.75%)</td><td>25.71 (+5.87%)</td><td>24.86 (+4.27%)</td><td>24.90 (+3.31%)</td><td>24.27 (+6.82%)</td><td>0.54 (-15.75%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>24.29 (n/a)</td><td>23.86 (n/a)</td><td>24.12 (n/a)</td><td>22.73 (n/a)</td><td>0.65 (n/a)</td><td>24.28 (n/a)</td><td>23.85 (n/a)</td><td>24.10 (n/a)</td><td>22.72 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>43.88 (+2.11%)</td><td>41.17 (-0.13%)</td><td>40.84 (-0.30%)</td><td>39.41 (-2.68%)</td><td>1.75 <b>(+74.89%)</b></td><td>43.86 (+2.11%)</td><td>41.15 (-0.13%)</td><td>40.81 (-0.30%)</td><td>39.39 (-2.68%)</td><td>1.75 <b>(+74.89%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>42.98 (n/a)</td><td>41.22 (n/a)</td><td>40.96 (n/a)</td><td>40.50 (n/a)</td><td>1.00 (n/a)</td><td>42.95 (n/a)</td><td>41.20 (n/a)</td><td>40.94 (n/a)</td><td>40.47 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>45.85 (+6.78%)</td><td>44.46 (+6.35%)</td><td>44.85 (+5.06%)</td><td>42.17 (+8.60%)</td><td>1.50 (-13.50%)</td><td>45.83 (+6.78%)</td><td>44.43 (+6.35%)</td><td>44.82 (+5.06%)</td><td>42.14 (+8.60%)</td><td>1.50 (-13.50%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>42.94 (n/a)</td><td>41.80 (n/a)</td><td>42.69 (n/a)</td><td>38.83 (n/a)</td><td>1.74 (n/a)</td><td>42.92 (n/a)</td><td>41.78 (n/a)</td><td>42.66 (n/a)</td><td>38.81 (n/a)</td><td>1.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>153.10 (n/a)</td><td>150.10 (n/a)</td><td>110.70 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>149.28 (n/a)</td><td>149.20 (n/a)</td><td>113.70 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>158.44 (n/a)</td><td>170.50 (n/a)</td><td>114.40 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.30 (n/a)</td><td>175.10 (n/a)</td><td>209.50 (n/a)</td><td>110.70 (n/a)</td><td>51.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.20 (n/a)</td><td>199.12 (n/a)</td><td>212.70 (n/a)</td><td>153.20 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>197.24 (n/a)</td><td>208.70 (n/a)</td><td>129.00 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.10 (n/a)</td><td>174.58 (n/a)</td><td>180.40 (n/a)</td><td>125.50 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.70 (n/a)</td><td>204.92 (n/a)</td><td>198.50 (n/a)</td><td>192.40 (n/a)</td><td>14.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>161.06 (n/a)</td><td>159.00 (n/a)</td><td>116.00 (n/a)</td><td>33.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>173.82 (n/a)</td><td>175.20 (n/a)</td><td>147.00 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>179.22 (n/a)</td><td>162.50 (n/a)</td><td>145.30 (n/a)</td><td>36.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>192.86 (n/a)</td><td>201.10 (n/a)</td><td>157.60 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>370.40 (n/a)</td><td>227.90 (n/a)</td><td>194.30 (n/a)</td><td>149.10 (n/a)</td><td>85.78 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.20 (n/a)</td><td>197.88 (n/a)</td><td>181.80 (n/a)</td><td>176.40 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.30 (n/a)</td><td>180.86 (n/a)</td><td>166.70 (n/a)</td><td>164.90 (n/a)</td><td>25.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.10 (n/a)</td><td>218.46 (n/a)</td><td>223.40 (n/a)</td><td>178.20 (n/a)</td><td>23.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>162.08 (n/a)</td><td>153.20 (n/a)</td><td>130.20 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>198.22 (n/a)</td><td>213.50 (n/a)</td><td>165.30 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>187.98 (n/a)</td><td>175.30 (n/a)</td><td>170.20 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.40 (n/a)</td><td>186.92 (n/a)</td><td>186.60 (n/a)</td><td>154.20 (n/a)</td><td>32.19 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>175.26 (n/a)</td><td>180.30 (n/a)</td><td>145.50 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>185.14 (n/a)</td><td>180.00 (n/a)</td><td>151.80 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.50 (n/a)</td><td>207.70 (n/a)</td><td>203.30 (n/a)</td><td>178.50 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.30 (n/a)</td><td>228.60 (n/a)</td><td>225.00 (n/a)</td><td>209.00 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.16 <b>(-33.83%)</b></td><td>0.15 (-16.32%)</td><td>0.15 (-7.34%)</td><td>0.15 (+5.30%)</td><td>0.01 <b>(-85.83%)</b></td><td>223.60 (-5.05%)</td><td>212.40 (+14.44%)</td><td>213.30 (+7.89%)</td><td>200.40 <b>(+51.13%)</b></td><td>8.66 <b>(-79.46%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>235.50 (n/a)</td><td>185.60 (n/a)</td><td>197.70 (n/a)</td><td>132.60 (n/a)</td><td>42.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>175.04 (n/a)</td><td>170.90 (n/a)</td><td>161.50 (n/a)</td><td>14.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.70 (n/a)</td><td>171.76 (n/a)</td><td>176.20 (n/a)</td><td>138.30 (n/a)</td><td>28.39 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>270.20 (n/a)</td><td>209.72 (n/a)</td><td>195.50 (n/a)</td><td>165.80 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>214.40 (n/a)</td><td>169.60 (n/a)</td><td>170.40 (n/a)</td><td>121.10 (n/a)</td><td>37.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.20 (n/a)</td><td>178.76 (n/a)</td><td>195.20 (n/a)</td><td>129.30 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>242.40 (n/a)</td><td>198.42 (n/a)</td><td>196.20 (n/a)</td><td>151.00 (n/a)</td><td>33.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>240.00 (n/a)</td><td>205.30 (n/a)</td><td>206.60 (n/a)</td><td>155.00 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+14.12%)</td><td>0.02 (-4.47%)</td><td>0.02 (-6.85%)</td><td>0.02 (-10.32%)</td><td>0.01 <b>(+75.99%)</b></td><td>211.10 (+11.52%)</td><td>173.66 (+7.32%)</td><td>170.60 (+7.36%)</td><td>123.10 (-12.38%)</td><td>35.54 <b>(+74.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>161.82 (n/a)</td><td>158.90 (n/a)</td><td>140.50 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+12.75%)</td><td>0.03 (+14.07%)</td><td>0.03 (+14.54%)</td><td>0.02 (+18.09%)</td><td>0.00 (-2.09%)</td><td>174.10 (-15.32%)</td><td>150.36 (-12.73%)</td><td>144.60 (-12.73%)</td><td>131.20 (-11.35%)</td><td>18.47 <b>(-25.74%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>172.30 (n/a)</td><td>165.70 (n/a)</td><td>148.00 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-4.90%)</td><td>0.02 (-9.78%)</td><td>0.02 (-10.85%)</td><td>0.01 (-8.95%)</td><td>0.00 (+7.64%)</td><td>282.80 (+9.83%)</td><td>213.16 (+11.87%)</td><td>199.50 (+12.20%)</td><td>162.70 (+5.10%)</td><td>48.85 <b>(+21.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>257.50 (n/a)</td><td>190.54 (n/a)</td><td>177.80 (n/a)</td><td>154.80 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (-15.04%)</td><td>0.02 (-0.32%)</td><td>0.02 (-0.48%)</td><td>0.02 (+10.28%)</td><td>0.00 <b>(-49.59%)</b></td><td>208.80 (-9.34%)</td><td>190.56 (-1.49%)</td><td>189.40 (+0.48%)</td><td>172.00 (+17.73%)</td><td>17.78 <b>(-45.84%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.30 (n/a)</td><td>193.44 (n/a)</td><td>188.50 (n/a)</td><td>146.10 (n/a)</td><td>32.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-5.78%)</td><td>0.03 (+14.30%)</td><td>0.02 (+12.56%)</td><td>0.02 <b>(+43.58%)</b></td><td>0.00 <b>(-49.64%)</b></td><td>174.90 <b>(-30.35%)</b></td><td>161.46 (-15.66%)</td><td>172.00 (-11.16%)</td><td>137.00 (+6.12%)</td><td>16.96 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.10 (n/a)</td><td>191.44 (n/a)</td><td>193.60 (n/a)</td><td>129.10 (n/a)</td><td>43.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 <b>(-22.08%)</b></td><td>0.02 (-9.39%)</td><td>0.02 (-3.53%)</td><td>0.02 (+11.04%)</td><td>0.00 <b>(-77.21%)</b></td><td>184.80 (-9.99%)</td><td>177.32 (+7.49%)</td><td>178.40 (+3.66%)</td><td>164.60 <b>(+28.39%)</b></td><td>8.13 <b>(-73.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>164.96 (n/a)</td><td>172.10 (n/a)</td><td>128.20 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (-4.24%)</td><td>0.02 (-9.55%)</td><td>0.02 (-7.71%)</td><td>0.01 <b>(-32.19%)</b></td><td>0.00 <b>(+65.34%)</b></td><td>301.40 <b>(+47.46%)</b></td><td>205.18 (+14.81%)</td><td>182.40 (+8.31%)</td><td>165.00 (+4.43%)</td><td>56.96 <b>(+152.12%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.40 (n/a)</td><td>178.72 (n/a)</td><td>168.40 (n/a)</td><td>158.00 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+1.29%)</td><td>0.03 (+0.09%)</td><td>0.02 (+4.87%)</td><td>0.02 (+6.42%)</td><td>0.00 (-7.24%)</td><td>179.20 (-6.03%)</td><td>164.94 (-0.69%)</td><td>174.20 (-4.65%)</td><td>121.50 (-1.30%)</td><td>24.54 (-15.72%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>166.08 (n/a)</td><td>182.70 (n/a)</td><td>123.10 (n/a)</td><td>29.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+18.67%)</td><td>0.02 (+3.04%)</td><td>0.02 (+1.85%)</td><td>0.02 (-15.04%)</td><td>0.00 <b>(+192.08%)</b></td><td>215.00 (+17.74%)</td><td>171.06 (-0.65%)</td><td>170.10 (-1.85%)</td><td>132.60 (-15.76%)</td><td>31.31 <b>(+187.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.60 (n/a)</td><td>172.18 (n/a)</td><td>173.30 (n/a)</td><td>157.40 (n/a)</td><td>10.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 <b>(-24.99%)</b></td><td>0.02 (-19.93%)</td><td>0.02 (-11.68%)</td><td>0.02 <b>(-22.07%)</b></td><td>0.00 <b>(-24.46%)</b></td><td>232.90 <b>(+28.32%)</b></td><td>201.22 <b>(+24.86%)</b></td><td>186.60 (+13.23%)</td><td>182.40 <b>(+33.33%)</b></td><td>22.69 <b>(+29.16%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.50 (n/a)</td><td>161.16 (n/a)</td><td>164.80 (n/a)</td><td>136.80 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+11.09%)</td><td>0.02 (+3.62%)</td><td>0.02 (-7.62%)</td><td>0.02 (+3.12%)</td><td>0.00 <b>(+24.22%)</b></td><td>213.30 (-3.00%)</td><td>181.28 (-3.01%)</td><td>191.70 (+8.24%)</td><td>145.70 (-10.01%)</td><td>28.40 (+7.24%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.90 (n/a)</td><td>186.90 (n/a)</td><td>177.10 (n/a)</td><td>161.90 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-14.05%)</td><td>0.02 (-13.79%)</td><td>0.02 (-15.49%)</td><td>0.02 <b>(-24.42%)</b></td><td>0.01 (+2.72%)</td><td>241.60 <b>(+32.31%)</b></td><td>180.94 (+18.49%)</td><td>194.60 (+18.30%)</td><td>124.10 (+16.31%)</td><td>46.63 <b>(+59.56%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>152.70 (n/a)</td><td>164.50 (n/a)</td><td>106.70 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+11.16%)</td><td>0.02 (+1.07%)</td><td>0.02 (+3.58%)</td><td>0.02 (-5.88%)</td><td>0.00 <b>(+91.93%)</b></td><td>206.10 (+6.24%)</td><td>172.12 (+0.33%)</td><td>164.40 (-3.46%)</td><td>139.80 (-10.04%)</td><td>26.86 <b>(+84.30%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>171.56 (n/a)</td><td>170.30 (n/a)</td><td>155.40 (n/a)</td><td>14.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-9.60%)</td><td>0.02 (+0.76%)</td><td>0.02 (-2.40%)</td><td>0.02 <b>(+26.00%)</b></td><td>0.00 <b>(-55.97%)</b></td><td>189.10 <b>(-20.65%)</b></td><td>174.18 (-3.42%)</td><td>172.80 (+2.43%)</td><td>155.30 (+10.61%)</td><td>14.60 <b>(-61.41%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.30 (n/a)</td><td>180.34 (n/a)</td><td>168.70 (n/a)</td><td>140.40 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-1.25%)</td><td>0.02 (-14.84%)</td><td>0.02 (-14.54%)</td><td>0.02 <b>(-32.02%)</b></td><td>0.01 <b>(+71.81%)</b></td><td>266.20 <b>(+47.07%)</b></td><td>196.54 <b>(+21.49%)</b></td><td>193.50 (+16.99%)</td><td>137.60 (+1.25%)</td><td>46.42 <b>(+155.42%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.00 (n/a)</td><td>161.78 (n/a)</td><td>165.40 (n/a)</td><td>135.90 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-15.20%)</td><td>0.02 (+1.40%)</td><td>0.02 (-2.30%)</td><td>0.02 (+13.02%)</td><td>0.00 <b>(-53.97%)</b></td><td>219.50 (-11.53%)</td><td>186.52 (-5.27%)</td><td>188.10 (+2.34%)</td><td>160.70 (+17.99%)</td><td>22.37 <b>(-54.14%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.10 (n/a)</td><td>196.90 (n/a)</td><td>183.80 (n/a)</td><td>136.20 (n/a)</td><td>48.77 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 <b>(-29.13%)</b></td><td>0.05 (-6.28%)</td><td>0.05 (+4.17%)</td><td>0.04 (+11.30%)</td><td>0.00 <b>(-70.49%)</b></td><td>185.80 (-10.15%)</td><td>169.52 (+2.16%)</td><td>161.20 (-3.99%)</td><td>157.20 <b>(+41.11%)</b></td><td>14.48 <b>(-62.41%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>165.94 (n/a)</td><td>167.90 (n/a)</td><td>111.40 (n/a)</td><td>38.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (-5.93%)</td><td>0.05 (+3.11%)</td><td>0.05 (-2.00%)</td><td>0.04 (+8.18%)</td><td>0.01 <b>(-33.91%)</b></td><td>190.30 (-7.58%)</td><td>162.54 (-4.15%)</td><td>163.10 (+2.07%)</td><td>147.50 (+6.27%)</td><td>17.44 <b>(-36.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>169.58 (n/a)</td><td>159.80 (n/a)</td><td>138.80 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (+1.83%)</td><td>0.04 (+8.93%)</td><td>0.04 (+12.36%)</td><td>0.04 (+9.06%)</td><td>0.00 (-16.45%)</td><td>217.30 (-8.31%)</td><td>200.98 (-8.53%)</td><td>209.10 (-10.98%)</td><td>182.20 (-1.83%)</td><td>16.90 <b>(-26.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.00 (n/a)</td><td>219.72 (n/a)</td><td>234.90 (n/a)</td><td>185.60 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (+13.50%)</td><td>0.04 (+15.62%)</td><td>0.04 (+14.46%)</td><td>0.03 <b>(+34.77%)</b></td><td>0.01 (-2.18%)</td><td>236.80 <b>(-25.81%)</b></td><td>198.68 (-14.73%)</td><td>193.90 (-12.62%)</td><td>152.50 (-11.85%)</td><td>33.22 <b>(-37.55%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.20 (n/a)</td><td>233.00 (n/a)</td><td>221.90 (n/a)</td><td>173.00 (n/a)</td><td>53.19 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (-10.96%)</td><td>0.05 (-4.83%)</td><td>0.05 (+6.30%)</td><td>0.04 (-17.26%)</td><td>0.01 (+7.08%)</td><td>225.50 <b>(+20.85%)</b></td><td>173.40 (+6.07%)</td><td>163.00 (-5.89%)</td><td>145.20 (+12.30%)</td><td>33.16 <b>(+46.09%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>163.48 (n/a)</td><td>173.20 (n/a)</td><td>129.30 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 <b>(+27.95%)</b></td><td>0.06 (+9.83%)</td><td>0.05 (+1.81%)</td><td>0.04 (-10.72%)</td><td>0.01 <b>(+270.56%)</b></td><td>193.00 (+12.01%)</td><td>152.48 (-6.05%)</td><td>163.40 (-1.80%)</td><td>117.60 <b>(-21.81%)</b></td><td>31.19 <b>(+216.33%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.30 (n/a)</td><td>162.30 (n/a)</td><td>166.40 (n/a)</td><td>150.40 (n/a)</td><td>9.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (+8.70%)</td><td>0.05 (-4.38%)</td><td>0.06 (-0.39%)</td><td>0.03 <b>(-35.10%)</b></td><td>0.01 <b>(+99.55%)</b></td><td>267.80 <b>(+54.09%)</b></td><td>165.44 (+11.45%)</td><td>147.90 (+0.41%)</td><td>119.50 (-8.01%)</td><td>58.90 <b>(+206.34%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>148.44 (n/a)</td><td>147.30 (n/a)</td><td>129.90 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (-9.66%)</td><td>0.05 (-2.92%)</td><td>0.05 (+7.49%)</td><td>0.05 (+0.38%)</td><td>0.01 <b>(-24.08%)</b></td><td>177.30 (-0.39%)</td><td>153.32 (+2.04%)</td><td>151.60 (-6.99%)</td><td>128.20 (+10.71%)</td><td>22.55 (-14.62%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>150.26 (n/a)</td><td>163.00 (n/a)</td><td>115.80 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 <b>(-20.02%)</b></td><td>0.05 (-10.07%)</td><td>0.05 (-6.00%)</td><td>0.04 (+3.47%)</td><td>0.01 <b>(-54.67%)</b></td><td>203.00 (-3.33%)</td><td>164.74 (+7.24%)</td><td>156.80 (+6.38%)</td><td>146.40 <b>(+25.02%)</b></td><td>22.48 <b>(-42.50%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>153.62 (n/a)</td><td>147.40 (n/a)</td><td>117.10 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (-17.20%)</td><td>0.05 (-10.09%)</td><td>0.05 (-18.76%)</td><td>0.05 (-0.70%)</td><td>0.00 <b>(-57.09%)</b></td><td>177.30 (+0.68%)</td><td>158.48 (+8.83%)</td><td>162.40 <b>(+23.12%)</b></td><td>142.80 <b>(+20.81%)</b></td><td>13.79 <b>(-50.10%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.10 (n/a)</td><td>145.62 (n/a)</td><td>131.90 (n/a)</td><td>118.20 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 <b>(-22.30%)</b></td><td>0.05 (-11.31%)</td><td>0.05 (-7.69%)</td><td>0.04 (-14.98%)</td><td>0.01 <b>(-37.12%)</b></td><td>202.00 (+17.58%)</td><td>166.54 (+11.17%)</td><td>168.90 (+8.34%)</td><td>131.00 <b>(+28.68%)</b></td><td>27.29 (-2.47%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.80 (n/a)</td><td>149.80 (n/a)</td><td>155.90 (n/a)</td><td>101.80 (n/a)</td><td>27.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (+5.87%)</td><td>0.04 (-3.13%)</td><td>0.04 (-5.53%)</td><td>0.03 (-3.23%)</td><td>0.01 <b>(+37.78%)</b></td><td>234.90 (+3.30%)</td><td>190.80 (+5.36%)</td><td>186.40 (+5.85%)</td><td>134.50 (-5.55%)</td><td>42.81 <b>(+37.79%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>181.10 (n/a)</td><td>176.10 (n/a)</td><td>142.40 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (+1.26%)</td><td>0.04 (-8.59%)</td><td>0.04 (-7.15%)</td><td>0.03 (-16.39%)</td><td>0.01 <b>(+69.71%)</b></td><td>244.10 (+19.60%)</td><td>209.50 (+11.11%)</td><td>208.20 (+7.71%)</td><td>160.40 (-1.23%)</td><td>33.13 <b>(+101.50%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>188.56 (n/a)</td><td>193.30 (n/a)</td><td>162.40 (n/a)</td><td>16.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (-0.69%)</td><td>0.05 (-8.21%)</td><td>0.05 (-7.92%)</td><td>0.04 (-0.97%)</td><td>0.01 (+4.10%)</td><td>221.80 (+1.00%)</td><td>180.72 (+9.18%)</td><td>182.00 (+8.59%)</td><td>122.40 (+0.66%)</td><td>36.50 (+1.00%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>165.52 (n/a)</td><td>167.60 (n/a)</td><td>121.60 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (-6.68%)</td><td>0.05 (+7.47%)</td><td>0.05 <b>(+22.37%)</b></td><td>0.04 (+1.58%)</td><td>0.01 (-13.14%)</td><td>210.40 (-1.54%)</td><td>171.54 (-7.54%)</td><td>163.20 (-18.28%)</td><td>133.50 (+7.14%)</td><td>34.75 (-3.72%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>185.52 (n/a)</td><td>199.70 (n/a)</td><td>124.60 (n/a)</td><td>36.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (+14.12%)</td><td>0.05 (-0.27%)</td><td>0.05 (+10.10%)</td><td>0.04 (-10.66%)</td><td>0.01 <b>(+69.27%)</b></td><td>224.70 (+11.96%)</td><td>177.64 (+3.26%)</td><td>162.80 (-9.20%)</td><td>127.80 (-12.35%)</td><td>41.51 <b>(+76.12%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>172.04 (n/a)</td><td>179.30 (n/a)</td><td>145.80 (n/a)</td><td>23.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (-8.09%)</td><td>0.10 (-2.57%)</td><td>0.10 (+0.09%)</td><td>0.09 (-1.58%)</td><td>0.00 <b>(-49.42%)</b></td><td>181.30 (+1.57%)</td><td>168.32 (+2.24%)</td><td>165.90 (-0.06%)</td><td>161.20 (+8.85%)</td><td>7.65 <b>(-44.05%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.50 (n/a)</td><td>164.64 (n/a)</td><td>166.00 (n/a)</td><td>148.10 (n/a)</td><td>13.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (-8.90%)</td><td>0.10 (-5.62%)</td><td>0.10 (+4.70%)</td><td>0.09 (+13.90%)</td><td>0.02 <b>(-43.77%)</b></td><td>181.20 (-12.17%)</td><td>159.54 (+1.92%)</td><td>163.60 (-4.50%)</td><td>124.30 (+9.71%)</td><td>23.51 <b>(-42.34%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>206.30 (n/a)</td><td>156.54 (n/a)</td><td>171.30 (n/a)</td><td>113.30 (n/a)</td><td>40.78 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (+18.83%)</td><td>0.09 (+5.46%)</td><td>0.08 (-6.14%)</td><td>0.07 (+6.24%)</td><td>0.02 <b>(+34.11%)</b></td><td>247.20 (-5.86%)</td><td>193.26 (-3.97%)</td><td>205.20 (+6.54%)</td><td>137.00 (-15.85%)</td><td>43.44 (+5.80%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>262.60 (n/a)</td><td>201.26 (n/a)</td><td>192.60 (n/a)</td><td>162.80 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (+12.02%)</td><td>0.09 (+16.70%)</td><td>0.09 (+13.09%)</td><td>0.08 <b>(+27.67%)</b></td><td>0.02 (+10.32%)</td><td>217.30 <b>(-21.67%)</b></td><td>181.92 (-14.63%)</td><td>186.30 (-11.58%)</td><td>137.50 (-10.71%)</td><td>35.11 <b>(-20.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>277.40 (n/a)</td><td>213.10 (n/a)</td><td>210.70 (n/a)</td><td>154.00 (n/a)</td><td>44.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (-11.27%)</td><td>0.08 <b>(-25.18%)</b></td><td>0.07 <b>(-24.07%)</b></td><td>0.05 <b>(-40.87%)</b></td><td>0.03 <b>(+29.06%)</b></td><td>345.80 <b>(+69.10%)</b></td><td>240.00 <b>(+48.00%)</b></td><td>230.80 <b>(+31.66%)</b></td><td>131.20 (+12.71%)</td><td>98.87 <b>(+159.65%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>204.50 (n/a)</td><td>162.16 (n/a)</td><td>175.30 (n/a)</td><td>116.40 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (+5.16%)</td><td>0.09 (-8.89%)</td><td>0.09 (-16.90%)</td><td>0.08 (+2.86%)</td><td>0.01 (+10.31%)</td><td>207.40 (-2.81%)</td><td>186.66 (+9.85%)</td><td>191.90 <b>(+20.31%)</b></td><td>145.70 (-4.90%)</td><td>23.93 (-3.17%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>169.92 (n/a)</td><td>159.50 (n/a)</td><td>153.20 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (-5.15%)</td><td>0.10 (-3.77%)</td><td>0.10 (-12.95%)</td><td>0.07 (+2.85%)</td><td>0.02 (-8.37%)</td><td>229.70 (-2.79%)</td><td>169.90 (+3.02%)</td><td>172.10 (+14.89%)</td><td>129.30 (+5.38%)</td><td>40.16 (-9.78%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.30 (n/a)</td><td>164.92 (n/a)</td><td>149.80 (n/a)</td><td>122.70 (n/a)</td><td>44.52 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (-4.59%)</td><td>0.10 (-5.07%)</td><td>0.11 (-3.90%)</td><td>0.07 (-8.67%)</td><td>0.02 <b>(+20.64%)</b></td><td>223.40 (+9.46%)</td><td>167.88 (+6.67%)</td><td>155.60 (+4.08%)</td><td>137.30 (+4.81%)</td><td>36.38 <b>(+31.40%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>157.38 (n/a)</td><td>149.50 (n/a)</td><td>131.00 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (+18.76%)</td><td>0.10 (+5.57%)</td><td>0.09 (-5.16%)</td><td>0.08 (+13.35%)</td><td>0.01 <b>(+30.69%)</b></td><td>202.00 (-11.79%)</td><td>172.48 (-4.94%)</td><td>177.80 (+5.39%)</td><td>140.30 (-15.79%)</td><td>25.56 (-4.56%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.00 (n/a)</td><td>181.44 (n/a)</td><td>168.70 (n/a)</td><td>166.60 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (-3.91%)</td><td>0.10 (+9.01%)</td><td>0.10 (+4.84%)</td><td>0.09 <b>(+24.10%)</b></td><td>0.01 <b>(-41.73%)</b></td><td>176.30 (-19.46%)</td><td>160.68 (-9.84%)</td><td>167.00 (-4.63%)</td><td>142.50 (+4.09%)</td><td>14.88 <b>(-51.21%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>218.90 (n/a)</td><td>178.22 (n/a)</td><td>175.10 (n/a)</td><td>136.90 (n/a)</td><td>30.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (+14.24%)</td><td>0.10 (+0.88%)</td><td>0.10 (-1.41%)</td><td>0.07 (+0.11%)</td><td>0.02 <b>(+27.47%)</b></td><td>225.60 (-0.13%)</td><td>166.50 (+0.28%)</td><td>166.10 (+1.40%)</td><td>116.10 (-12.44%)</td><td>39.12 (+8.27%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.90 (n/a)</td><td>166.04 (n/a)</td><td>163.80 (n/a)</td><td>132.60 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (+0.77%)</td><td>0.11 (+9.01%)</td><td>0.10 (+1.65%)</td><td>0.09 (+18.12%)</td><td>0.02 (-19.55%)</td><td>178.40 (-15.33%)</td><td>157.90 (-9.70%)</td><td>171.70 (-1.60%)</td><td>125.50 (-0.79%)</td><td>23.47 <b>(-32.79%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>174.86 (n/a)</td><td>174.50 (n/a)</td><td>126.50 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (+4.68%)</td><td>0.10 (+8.25%)</td><td>0.10 (+16.16%)</td><td>0.08 (+13.79%)</td><td>0.02 (-11.26%)</td><td>202.70 (-12.14%)</td><td>169.66 (-8.45%)</td><td>161.30 (-13.93%)</td><td>138.10 (-4.50%)</td><td>26.04 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.70 (n/a)</td><td>185.32 (n/a)</td><td>187.40 (n/a)</td><td>144.60 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (+15.96%)</td><td>0.09 (+15.89%)</td><td>0.09 (+9.84%)</td><td>0.08 <b>(+23.60%)</b></td><td>0.01 (-12.99%)</td><td>197.10 (-19.12%)</td><td>175.88 (-14.35%)</td><td>177.10 (-8.95%)</td><td>152.40 (-13.80%)</td><td>17.62 <b>(-39.53%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>243.70 (n/a)</td><td>205.34 (n/a)</td><td>194.50 (n/a)</td><td>176.80 (n/a)</td><td>29.13 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (-0.61%)</td><td>0.10 (+10.41%)</td><td>0.09 (+19.62%)</td><td>0.09 <b>(+39.98%)</b></td><td>0.02 <b>(-37.38%)</b></td><td>183.80 <b>(-28.54%)</b></td><td>167.96 (-12.98%)</td><td>172.70 (-16.41%)</td><td>129.60 (+0.62%)</td><td>22.34 <b>(-54.69%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>257.20 (n/a)</td><td>193.02 (n/a)</td><td>206.60 (n/a)</td><td>128.80 (n/a)</td><td>49.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 <b>(+27.30%)</b></td><td>0.11 <b>(+22.84%)</b></td><td>0.11 (+18.02%)</td><td>0.08 (+2.29%)</td><td>0.02 <b>(+137.61%)</b></td><td>200.90 (-2.24%)</td><td>152.42 (-16.99%)</td><td>151.00 (-15.26%)</td><td>129.30 <b>(-21.45%)</b></td><td>29.17 <b>(+81.35%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>183.62 (n/a)</td><td>178.20 (n/a)</td><td>164.60 (n/a)</td><td>16.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (-2.32%)</td><td>0.20 (-0.12%)</td><td>0.18 (-0.90%)</td><td>0.16 (+1.39%)</td><td>0.05 (-4.91%)</td><td>209.70 (-1.36%)</td><td>168.62 (-0.22%)</td><td>177.20 (+0.91%)</td><td>113.90 (+2.34%)</td><td>37.14 (-2.72%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>212.60 (n/a)</td><td>169.00 (n/a)</td><td>175.60 (n/a)</td><td>111.30 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (-16.62%)</td><td>0.21 (+0.65%)</td><td>0.20 (+12.91%)</td><td>0.17 (-4.76%)</td><td>0.03 <b>(-36.78%)</b></td><td>197.60 (+4.99%)</td><td>163.26 (-2.61%)</td><td>160.00 (-11.46%)</td><td>131.60 (+19.96%)</td><td>26.84 (-18.15%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>188.20 (n/a)</td><td>167.64 (n/a)</td><td>180.70 (n/a)</td><td>109.70 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.19 (+0.56%)</td><td>0.15 (-5.20%)</td><td>0.15 (-9.89%)</td><td>0.11 (-16.58%)</td><td>0.03 (+15.74%)</td><td>306.60 (+19.86%)</td><td>222.42 (+6.96%)</td><td>216.80 (+10.95%)</td><td>170.50 (-0.58%)</td><td>51.28 <b>(+41.31%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>255.80 (n/a)</td><td>207.94 (n/a)</td><td>195.40 (n/a)</td><td>171.50 (n/a)</td><td>36.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (-2.67%)</td><td>0.17 (-3.61%)</td><td>0.16 (-4.36%)</td><td>0.14 (-1.45%)</td><td>0.04 (-1.37%)</td><td>238.00 (+1.45%)</td><td>196.92 (+3.82%)</td><td>206.20 (+4.56%)</td><td>141.40 (+2.76%)</td><td>36.06 (+2.64%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>234.60 (n/a)</td><td>189.68 (n/a)</td><td>197.20 (n/a)</td><td>137.60 (n/a)</td><td>35.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 (-0.97%)</td><td>0.20 (-7.05%)</td><td>0.18 (-12.49%)</td><td>0.14 (-11.34%)</td><td>0.06 (+3.55%)</td><td>232.50 (+12.75%)</td><td>176.20 (+8.51%)</td><td>185.60 (+14.22%)</td><td>115.20 (+0.96%)</td><td>46.06 (+14.16%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>206.20 (n/a)</td><td>162.38 (n/a)</td><td>162.50 (n/a)</td><td>114.10 (n/a)</td><td>40.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.20 <b>(-26.50%)</b></td><td>0.18 (-7.09%)</td><td>0.18 (-13.19%)</td><td>0.14 <b>(+61.85%)</b></td><td>0.02 <b>(-70.11%)</b></td><td>229.30 <b>(-38.19%)</b></td><td>189.34 (-6.06%)</td><td>177.40 (+15.12%)</td><td>167.90 <b>(+36.06%)</b></td><td>24.36 <b>(-75.63%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>371.00 (n/a)</td><td>201.56 (n/a)</td><td>154.10 (n/a)</td><td>123.40 (n/a)</td><td>99.97 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (-10.18%)</td><td>0.20 (-6.14%)</td><td>0.20 (-6.22%)</td><td>0.16 (+8.20%)</td><td>0.04 <b>(-26.73%)</b></td><td>200.50 (-7.56%)</td><td>168.74 (+4.47%)</td><td>166.20 (+6.68%)</td><td>125.50 (+11.36%)</td><td>28.13 <b>(-25.85%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>216.90 (n/a)</td><td>161.52 (n/a)</td><td>155.80 (n/a)</td><td>112.70 (n/a)</td><td>37.94 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (-0.14%)</td><td>0.23 (+7.67%)</td><td>0.24 (+15.70%)</td><td>0.18 (-0.39%)</td><td>0.03 (+9.26%)</td><td>179.30 (+0.39%)</td><td>144.68 (-6.81%)</td><td>137.90 (-13.54%)</td><td>124.70 (+0.16%)</td><td>22.19 (+12.67%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.60 (n/a)</td><td>155.26 (n/a)</td><td>159.50 (n/a)</td><td>124.50 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 <b>(+30.56%)</b></td><td>0.20 (+13.92%)</td><td>0.18 (-1.33%)</td><td>0.15 (-0.52%)</td><td>0.05 <b>(+127.19%)</b></td><td>218.10 (+0.55%)</td><td>167.86 (-9.19%)</td><td>181.10 (+1.34%)</td><td>120.70 <b>(-23.41%)</b></td><td>39.28 <b>(+70.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.90 (n/a)</td><td>184.84 (n/a)</td><td>178.70 (n/a)</td><td>157.60 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (+1.65%)</td><td>0.20 (+4.53%)</td><td>0.19 <b>(+24.41%)</b></td><td>0.17 (+14.22%)</td><td>0.03 <b>(-39.02%)</b></td><td>194.60 (-12.42%)</td><td>167.20 (-8.19%)</td><td>169.40 (-19.60%)</td><td>128.30 (-1.69%)</td><td>24.72 <b>(-47.58%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>222.20 (n/a)</td><td>182.12 (n/a)</td><td>210.70 (n/a)</td><td>130.50 (n/a)</td><td>47.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 <b>(+21.32%)</b></td><td>0.21 <b>(+20.18%)</b></td><td>0.21 <b>(+29.49%)</b></td><td>0.18 (+14.45%)</td><td>0.02 (+4.64%)</td><td>185.60 (-12.62%)</td><td>158.26 (-16.98%)</td><td>156.40 <b>(-22.77%)</b></td><td>136.60 (-17.56%)</td><td>17.65 <b>(-22.58%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>190.62 (n/a)</td><td>202.50 (n/a)</td><td>165.70 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 <b>(+44.23%)</b></td><td>0.22 <b>(+28.27%)</b></td><td>0.22 <b>(+28.79%)</b></td><td>0.19 (+13.15%)</td><td>0.04 <b>(+358.66%)</b></td><td>174.90 (-11.62%)</td><td>149.36 <b>(-20.51%)</b></td><td>148.70 <b>(-22.35%)</b></td><td>124.00 <b>(-30.69%)</b></td><td>24.16 <b>(+184.27%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>187.90 (n/a)</td><td>191.50 (n/a)</td><td>178.90 (n/a)</td><td>8.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 <b>(+71.41%)</b></td><td>0.21 <b>(+35.37%)</b></td><td>0.19 (+19.66%)</td><td>0.17 <b>(+38.01%)</b></td><td>0.05 <b>(+184.77%)</b></td><td>189.70 <b>(-27.51%)</b></td><td>162.84 <b>(-24.31%)</b></td><td>172.60 (-16.42%)</td><td>113.70 <b>(-41.63%)</b></td><td>30.91 (+16.20%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>261.70 (n/a)</td><td>215.14 (n/a)</td><td>206.50 (n/a)</td><td>194.80 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (-7.51%)</td><td>0.19 (-7.12%)</td><td>0.18 (-2.06%)</td><td>0.15 (-6.28%)</td><td>0.04 (-9.50%)</td><td>217.60 (+6.72%)</td><td>180.52 (+7.47%)</td><td>181.30 (+2.14%)</td><td>126.40 (+8.13%)</td><td>34.21 (+4.35%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>203.90 (n/a)</td><td>167.98 (n/a)</td><td>177.50 (n/a)</td><td>116.90 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (+14.13%)</td><td>0.17 (+0.96%)</td><td>0.19 (+8.03%)</td><td>0.13 (-13.45%)</td><td>0.04 <b>(+138.98%)</b></td><td>261.70 (+15.54%)</td><td>197.96 (+2.38%)</td><td>172.60 (-7.45%)</td><td>155.40 (-12.40%)</td><td>46.11 <b>(+139.15%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>226.50 (n/a)</td><td>193.36 (n/a)</td><td>186.50 (n/a)</td><td>177.40 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (-5.18%)</td><td>0.18 (-1.56%)</td><td>0.17 (-1.23%)</td><td>0.16 (+3.05%)</td><td>0.02 <b>(-23.18%)</b></td><td>201.40 (-2.99%)</td><td>180.82 (+0.90%)</td><td>191.00 (+1.27%)</td><td>158.30 (+5.46%)</td><td>20.29 <b>(-21.17%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>207.60 (n/a)</td><td>179.20 (n/a)</td><td>188.60 (n/a)</td><td>150.10 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-0.13%)</td><td>0.21 (-0.15%)</td><td>0.21 (-0.17%)</td><td>0.20 (-0.13%)</td><td>0.00 (+4.71%)</td><td>40958.10 (+0.14%)</td><td>40915.30 (+0.15%)</td><td>40918.30 (+0.17%)</td><td>40860.30 (+0.13%)</td><td>38.74 (+5.11%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40902.80 (n/a)</td><td>40854.42 (n/a)</td><td>40850.10 (n/a)</td><td>40806.80 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-0.56%)</td><td>0.21 (-0.08%)</td><td>0.21 (+0.05%)</td><td>0.21 (+0.03%)</td><td>0.00 <b>(-68.21%)</b></td><td>40883.90 (-0.03%)</td><td>40838.70 (+0.08%)</td><td>40856.30 (-0.05%)</td><td>40779.70 (+0.56%)</td><td>46.63 <b>(-68.05%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40896.60 (n/a)</td><td>40806.44 (n/a)</td><td>40877.50 (n/a)</td><td>40552.10 (n/a)</td><td>145.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+0.05%)</td><td>0.13 (+0.03%)</td><td>0.13 (+0.08%)</td><td>0.13 (-0.06%)</td><td>0.00 <b>(+105.19%)</b></td><td>322554.50 (+0.06%)</td><td>322126.10 (-0.03%)</td><td>321997.90 (-0.08%)</td><td>321880.20 (-0.05%)</td><td>284.43 <b>(+105.20%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>322375.00 (n/a)</td><td>322208.68 (n/a)</td><td>322255.30 (n/a)</td><td>322049.60 (n/a)</td><td>138.61 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+9.34%)</td><td>0.03 (+9.52%)</td><td>0.03 (+10.47%)</td><td>0.02 (+3.09%)</td><td>0.00 <b>(+23.10%)</b></td><td>164.90 (-3.00%)</td><td>142.60 (-8.46%)</td><td>145.50 (-9.51%)</td><td>121.70 (-8.56%)</td><td>15.93 (+9.94%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.00 (n/a)</td><td>155.78 (n/a)</td><td>160.80 (n/a)</td><td>133.10 (n/a)</td><td>14.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (-11.28%)</td><td>0.04 (-6.80%)</td><td>0.04 (-8.61%)</td><td>0.03 (+8.11%)</td><td>0.00 <b>(-43.42%)</b></td><td>200.00 (-7.49%)</td><td>168.00 (+4.97%)</td><td>168.50 (+9.42%)</td><td>145.10 (+12.74%)</td><td>20.40 <b>(-40.95%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>160.04 (n/a)</td><td>154.00 (n/a)</td><td>128.70 (n/a)</td><td>34.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+16.08%)</td><td>0.03 (+9.98%)</td><td>0.03 (+11.65%)</td><td>0.02 (+0.72%)</td><td>0.00 <b>(+73.47%)</b></td><td>195.10 (-0.71%)</td><td>156.76 (-7.96%)</td><td>151.60 (-10.40%)</td><td>128.30 (-13.83%)</td><td>25.30 <b>(+48.73%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>170.32 (n/a)</td><td>169.20 (n/a)</td><td>148.90 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (+17.34%)</td><td>0.03 (+3.72%)</td><td>0.03 (+10.95%)</td><td>0.02 (-14.11%)</td><td>0.01 <b>(+131.67%)</b></td><td>230.40 (+16.42%)</td><td>183.00 (-1.45%)</td><td>174.70 (-9.90%)</td><td>141.60 (-14.75%)</td><td>33.84 <b>(+129.49%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.90 (n/a)</td><td>185.70 (n/a)</td><td>193.90 (n/a)</td><td>166.10 (n/a)</td><td>14.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+19.90%)</td><td>0.03 (+14.57%)</td><td>0.03 (+19.85%)</td><td>0.02 (-5.15%)</td><td>0.00 <b>(+119.83%)</b></td><td>202.30 (+5.42%)</td><td>155.44 (-10.82%)</td><td>149.30 (-16.55%)</td><td>125.50 (-16.61%)</td><td>30.32 <b>(+96.90%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.90 (n/a)</td><td>174.30 (n/a)</td><td>178.90 (n/a)</td><td>150.50 (n/a)</td><td>15.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (+10.58%)</td><td>0.03 (+4.39%)</td><td>0.03 (+2.28%)</td><td>0.03 <b>(+24.61%)</b></td><td>0.01 (-6.54%)</td><td>203.90 (-19.76%)</td><td>172.82 (-5.52%)</td><td>167.80 (-2.21%)</td><td>131.40 (-9.57%)</td><td>31.05 <b>(-29.89%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.10 (n/a)</td><td>182.92 (n/a)</td><td>171.60 (n/a)</td><td>145.30 (n/a)</td><td>44.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-13.63%)</td><td>0.02 (-3.06%)</td><td>0.03 <b>(+20.27%)</b></td><td>0.02 (-9.97%)</td><td>0.00 <b>(-21.23%)</b></td><td>249.30 (+11.05%)</td><td>175.66 (+2.33%)</td><td>150.90 (-16.86%)</td><td>148.60 (+15.82%)</td><td>43.27 (+5.11%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>171.66 (n/a)</td><td>181.50 (n/a)</td><td>128.30 (n/a)</td><td>41.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+10.08%)</td><td>0.02 (+0.60%)</td><td>0.02 (-2.10%)</td><td>0.02 (-0.57%)</td><td>0.00 <b>(+77.95%)</b></td><td>209.40 (+0.58%)</td><td>195.22 (-0.12%)</td><td>200.60 (+2.19%)</td><td>165.60 (-9.16%)</td><td>17.73 <b>(+61.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.20 (n/a)</td><td>195.46 (n/a)</td><td>196.30 (n/a)</td><td>182.30 (n/a)</td><td>10.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-3.88%)</td><td>0.03 (+7.07%)</td><td>0.03 (+15.44%)</td><td>0.02 (-4.64%)</td><td>0.00 (-2.02%)</td><td>205.10 (+4.86%)</td><td>163.60 (-6.47%)</td><td>153.90 (-13.39%)</td><td>138.60 (+4.05%)</td><td>27.08 (+9.52%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.60 (n/a)</td><td>174.92 (n/a)</td><td>177.70 (n/a)</td><td>133.20 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 <b>(+27.50%)</b></td><td>0.03 (+18.48%)</td><td>0.03 <b>(+30.82%)</b></td><td>0.02 (-2.06%)</td><td>0.01 <b>(+77.59%)</b></td><td>244.30 (+2.13%)</td><td>176.02 (-12.07%)</td><td>167.30 <b>(-23.57%)</b></td><td>125.20 <b>(-21.60%)</b></td><td>51.99 <b>(+43.26%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.20 (n/a)</td><td>200.18 (n/a)</td><td>218.90 (n/a)</td><td>159.70 (n/a)</td><td>36.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-1.15%)</td><td>0.02 (-1.44%)</td><td>0.02 (-6.67%)</td><td>0.02 (-9.68%)</td><td>0.00 (+17.05%)</td><td>245.50 (+10.74%)</td><td>180.62 (+2.51%)</td><td>174.80 (+7.17%)</td><td>152.10 (+1.13%)</td><td>38.20 <b>(+31.44%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.70 (n/a)</td><td>176.20 (n/a)</td><td>163.10 (n/a)</td><td>150.40 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (-6.39%)</td><td>0.02 (-10.30%)</td><td>0.02 (-10.07%)</td><td>0.02 (-4.12%)</td><td>0.00 (-17.53%)</td><td>222.80 (+4.31%)</td><td>199.76 (+11.00%)</td><td>212.40 (+11.20%)</td><td>160.20 (+6.80%)</td><td>27.49 (-3.47%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.60 (n/a)</td><td>179.96 (n/a)</td><td>191.00 (n/a)</td><td>150.00 (n/a)</td><td>28.48 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (+3.18%)</td><td>0.03 (+5.00%)</td><td>0.02 (-3.73%)</td><td>0.02 (-2.02%)</td><td>0.01 <b>(+37.81%)</b></td><td>205.30 (+2.04%)</td><td>165.44 (-2.91%)</td><td>175.40 (+3.85%)</td><td>125.80 (-3.08%)</td><td>37.29 <b>(+31.48%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.20 (n/a)</td><td>170.40 (n/a)</td><td>168.90 (n/a)</td><td>129.80 (n/a)</td><td>28.36 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 <b>(+36.29%)</b></td><td>0.02 (+18.62%)</td><td>0.02 (+7.95%)</td><td>0.02 (+19.55%)</td><td>0.01 <b>(+60.54%)</b></td><td>251.30 (-16.37%)</td><td>191.80 (-13.92%)</td><td>200.50 (-7.35%)</td><td>115.50 <b>(-26.62%)</b></td><td>48.79 (-7.68%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>300.50 (n/a)</td><td>222.82 (n/a)</td><td>216.40 (n/a)</td><td>157.40 (n/a)</td><td>52.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (+1.49%)</td><td>0.02 (-4.79%)</td><td>0.02 (-17.52%)</td><td>0.02 (-0.28%)</td><td>0.00 (+1.37%)</td><td>222.80 (+0.27%)</td><td>202.84 (+5.03%)</td><td>217.40 <b>(+21.25%)</b></td><td>166.00 (-1.48%)</td><td>24.72 (-0.85%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.20 (n/a)</td><td>193.12 (n/a)</td><td>179.30 (n/a)</td><td>168.50 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (-2.54%)</td><td>0.04 (-8.64%)</td><td>0.05 (+3.24%)</td><td>0.02 <b>(-42.68%)</b></td><td>0.01 <b>(+68.45%)</b></td><td>346.30 <b>(+74.46%)</b></td><td>207.18 (+17.30%)</td><td>179.70 (-3.18%)</td><td>146.20 (+2.67%)</td><td>79.33 <b>(+222.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>176.62 (n/a)</td><td>185.60 (n/a)</td><td>142.40 (n/a)</td><td>24.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (+9.42%)</td><td>0.07 (+6.04%)</td><td>0.07 (+6.71%)</td><td>0.05 (-6.65%)</td><td>0.02 <b>(+27.42%)</b></td><td>223.70 (+7.14%)</td><td>170.88 (-4.55%)</td><td>169.80 (-6.29%)</td><td>133.50 (-8.62%)</td><td>36.45 <b>(+22.25%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>179.02 (n/a)</td><td>181.20 (n/a)</td><td>146.10 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 <b>(+27.02%)</b></td><td>0.05 (+2.76%)</td><td>0.04 (-5.27%)</td><td>0.03 (-3.63%)</td><td>0.02 <b>(+45.47%)</b></td><td>326.70 (+3.78%)</td><td>201.26 (+1.15%)</td><td>186.30 (+5.61%)</td><td>115.80 <b>(-21.22%)</b></td><td>76.99 (+14.99%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.80 (n/a)</td><td>198.98 (n/a)</td><td>176.40 (n/a)</td><td>147.00 (n/a)</td><td>66.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (-1.79%)</td><td>0.06 (+1.55%)</td><td>0.06 (-4.34%)</td><td>0.05 (+13.06%)</td><td>0.01 (-18.32%)</td><td>207.20 (-11.57%)</td><td>171.42 (-3.46%)</td><td>164.30 (+4.58%)</td><td>130.70 (+1.87%)</td><td>33.43 <b>(-26.34%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>234.30 (n/a)</td><td>177.56 (n/a)</td><td>157.10 (n/a)</td><td>128.30 (n/a)</td><td>45.39 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (-6.85%)</td><td>0.04 (-8.88%)</td><td>0.04 (-5.22%)</td><td>0.03 (-11.22%)</td><td>0.01 (-14.94%)</td><td>270.00 (+12.64%)</td><td>195.62 (+9.25%)</td><td>192.70 (+5.53%)</td><td>143.10 (+7.35%)</td><td>48.89 (+7.77%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>179.06 (n/a)</td><td>182.60 (n/a)</td><td>133.30 (n/a)</td><td>45.36 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (-4.20%)</td><td>0.06 <b>(+23.32%)</b></td><td>0.06 <b>(+20.19%)</b></td><td>0.06 <b>(+96.73%)</b></td><td>0.01 <b>(-54.14%)</b></td><td>184.30 <b>(-49.16%)</b></td><td>163.60 <b>(-26.59%)</b></td><td>169.80 (-16.76%)</td><td>132.90 (+4.40%)</td><td>20.79 <b>(-76.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>362.50 (n/a)</td><td>222.86 (n/a)</td><td>204.00 (n/a)</td><td>127.30 (n/a)</td><td>87.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 <b>(+22.64%)</b></td><td>0.04 (+0.19%)</td><td>0.04 (-6.23%)</td><td>0.03 (-16.69%)</td><td>0.01 <b>(+113.19%)</b></td><td>269.70 <b>(+20.08%)</b></td><td>199.22 (+5.30%)</td><td>205.60 (+6.64%)</td><td>122.60 (-18.48%)</td><td>54.82 <b>(+106.33%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.60 (n/a)</td><td>189.20 (n/a)</td><td>192.80 (n/a)</td><td>150.40 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 <b>(+35.60%)</b></td><td>0.06 <b>(+28.52%)</b></td><td>0.06 <b>(+23.90%)</b></td><td>0.04 (+9.14%)</td><td>0.01 <b>(+87.74%)</b></td><td>219.60 (-8.39%)</td><td>163.96 <b>(-20.31%)</b></td><td>166.80 (-19.26%)</td><td>127.10 <b>(-26.23%)</b></td><td>38.60 <b>(+21.96%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>205.74 (n/a)</td><td>206.60 (n/a)</td><td>172.30 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (-8.44%)</td><td>0.04 (-0.60%)</td><td>0.04 (+1.89%)</td><td>0.04 (-8.35%)</td><td>0.01 (-18.98%)</td><td>227.30 (+9.12%)</td><td>191.36 (+0.20%)</td><td>196.50 (-1.90%)</td><td>157.40 (+9.23%)</td><td>25.98 (-1.98%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>190.98 (n/a)</td><td>200.30 (n/a)</td><td>144.10 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (+14.26%)</td><td>0.06 <b>(+23.22%)</b></td><td>0.06 (+14.92%)</td><td>0.06 <b>(+46.35%)</b></td><td>0.00 <b>(-53.34%)</b></td><td>158.10 <b>(-31.68%)</b></td><td>147.30 <b>(-20.92%)</b></td><td>150.80 (-12.98%)</td><td>132.20 (-12.45%)</td><td>10.04 <b>(-72.48%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>186.26 (n/a)</td><td>173.30 (n/a)</td><td>151.00 (n/a)</td><td>36.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (+5.90%)</td><td>0.04 (-1.62%)</td><td>0.04 (-4.83%)</td><td>0.03 (+2.61%)</td><td>0.01 (+12.00%)</td><td>244.90 (-2.55%)</td><td>198.92 (+2.05%)</td><td>203.50 (+5.06%)</td><td>136.00 (-5.56%)</td><td>40.24 (-0.61%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.30 (n/a)</td><td>194.92 (n/a)</td><td>193.70 (n/a)</td><td>144.00 (n/a)</td><td>40.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 <b>(+24.95%)</b></td><td>0.05 <b>(+20.54%)</b></td><td>0.05 (+5.93%)</td><td>0.04 <b>(+40.18%)</b></td><td>0.01 (+8.22%)</td><td>225.90 <b>(-28.67%)</b></td><td>183.50 (-18.73%)</td><td>184.70 (-5.62%)</td><td>127.80 (-19.97%)</td><td>38.01 <b>(-40.14%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.70 (n/a)</td><td>225.78 (n/a)</td><td>195.70 (n/a)</td><td>159.70 (n/a)</td><td>63.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (-16.83%)</td><td>0.05 (+1.80%)</td><td>0.05 (+8.04%)</td><td>0.04 (+10.54%)</td><td>0.01 <b>(-37.87%)</b></td><td>223.70 (-9.54%)</td><td>183.90 (-4.40%)</td><td>170.80 (-7.43%)</td><td>157.80 <b>(+20.18%)</b></td><td>30.12 <b>(-32.88%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.30 (n/a)</td><td>192.36 (n/a)</td><td>184.50 (n/a)</td><td>131.30 (n/a)</td><td>44.87 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (-4.68%)</td><td>0.04 (+2.27%)</td><td>0.04 (+1.71%)</td><td>0.03 (+3.43%)</td><td>0.01 <b>(-20.54%)</b></td><td>257.90 (-3.34%)</td><td>222.10 (-3.28%)</td><td>233.80 (-1.68%)</td><td>170.60 (+4.92%)</td><td>32.93 (-19.31%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.80 (n/a)</td><td>229.64 (n/a)</td><td>237.80 (n/a)</td><td>162.60 (n/a)</td><td>40.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (+5.76%)</td><td>0.04 <b>(+21.71%)</b></td><td>0.04 <b>(+26.48%)</b></td><td>0.04 <b>(+56.52%)</b></td><td>0.00 <b>(-45.96%)</b></td><td>226.60 <b>(-36.12%)</b></td><td>205.56 <b>(-20.53%)</b></td><td>201.40 <b>(-20.93%)</b></td><td>178.80 (-5.45%)</td><td>19.54 <b>(-67.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>354.70 (n/a)</td><td>258.66 (n/a)</td><td>254.70 (n/a)</td><td>189.10 (n/a)</td><td>60.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (+9.41%)</td><td>0.10 (-3.92%)</td><td>0.10 (-7.51%)</td><td>0.07 (-12.03%)</td><td>0.02 <b>(+35.67%)</b></td><td>224.70 (+13.66%)</td><td>176.64 (+6.04%)</td><td>168.30 (+8.09%)</td><td>129.00 (-8.58%)</td><td>39.00 <b>(+41.24%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.70 (n/a)</td><td>166.58 (n/a)</td><td>155.70 (n/a)</td><td>141.10 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (+12.02%)</td><td>0.15 (-5.96%)</td><td>0.14 (-16.24%)</td><td>0.10 <b>(-20.19%)</b></td><td>0.05 <b>(+50.05%)</b></td><td>246.30 <b>(+25.28%)</b></td><td>175.24 (+11.28%)</td><td>170.30 (+19.42%)</td><td>115.90 (-10.71%)</td><td>54.01 <b>(+67.25%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>196.60 (n/a)</td><td>157.48 (n/a)</td><td>142.60 (n/a)</td><td>129.80 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 <b>(+28.24%)</b></td><td>0.10 (+16.65%)</td><td>0.11 <b>(+20.01%)</b></td><td>0.08 (-6.68%)</td><td>0.02 <b>(+266.64%)</b></td><td>209.30 (+7.17%)</td><td>161.60 (-11.78%)</td><td>153.30 (-16.64%)</td><td>129.70 <b>(-22.06%)</b></td><td>33.06 <b>(+207.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>183.18 (n/a)</td><td>183.90 (n/a)</td><td>166.40 (n/a)</td><td>10.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (-18.34%)</td><td>0.11 (-9.20%)</td><td>0.10 (-0.81%)</td><td>0.09 (+2.19%)</td><td>0.01 <b>(-55.64%)</b></td><td>221.50 (-2.12%)</td><td>195.42 (+7.49%)</td><td>195.20 (+0.83%)</td><td>168.80 <b>(+22.50%)</b></td><td>19.16 <b>(-46.27%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>226.30 (n/a)</td><td>181.80 (n/a)</td><td>193.60 (n/a)</td><td>137.80 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (+6.39%)</td><td>0.09 (+9.91%)</td><td>0.09 (+6.06%)</td><td>0.08 <b>(+48.21%)</b></td><td>0.01 <b>(-47.23%)</b></td><td>213.60 <b>(-32.53%)</b></td><td>188.60 (-12.30%)</td><td>185.60 (-5.69%)</td><td>166.30 (-5.99%)</td><td>18.67 <b>(-67.63%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>316.60 (n/a)</td><td>215.04 (n/a)</td><td>196.80 (n/a)</td><td>176.90 (n/a)</td><td>57.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (+14.96%)</td><td>0.12 (+19.63%)</td><td>0.12 <b>(+22.72%)</b></td><td>0.10 <b>(+28.34%)</b></td><td>0.01 (-13.74%)</td><td>210.10 <b>(-22.07%)</b></td><td>179.42 (-17.09%)</td><td>171.80 (-18.54%)</td><td>161.00 (-13.02%)</td><td>18.85 <b>(-41.73%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>269.60 (n/a)</td><td>216.40 (n/a)</td><td>210.90 (n/a)</td><td>185.10 (n/a)</td><td>32.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (+7.49%)</td><td>0.09 (-0.22%)</td><td>0.08 (-7.62%)</td><td>0.08 (-2.65%)</td><td>0.01 <b>(+88.45%)</b></td><td>206.60 (+2.73%)</td><td>188.54 (+0.93%)</td><td>197.50 (+8.22%)</td><td>163.10 (-6.96%)</td><td>20.57 <b>(+80.36%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>186.80 (n/a)</td><td>182.50 (n/a)</td><td>175.30 (n/a)</td><td>11.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (+9.62%)</td><td>0.10 (+3.01%)</td><td>0.09 (-1.32%)</td><td>0.09 (-9.59%)</td><td>0.02 <b>(+135.04%)</b></td><td>214.90 (+10.60%)</td><td>185.00 (-1.02%)</td><td>194.60 (+1.35%)</td><td>149.40 (-8.79%)</td><td>30.92 <b>(+137.38%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>186.90 (n/a)</td><td>192.00 (n/a)</td><td>163.80 (n/a)</td><td>13.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (-2.97%)</td><td>0.09 (-7.76%)</td><td>0.08 (-11.60%)</td><td>0.08 (-6.78%)</td><td>0.01 (+14.94%)</td><td>210.80 (+7.28%)</td><td>188.64 (+8.95%)</td><td>196.90 (+13.10%)</td><td>147.00 (+3.09%)</td><td>24.50 <b>(+26.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>173.14 (n/a)</td><td>174.10 (n/a)</td><td>142.60 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 <b>(+43.29%)</b></td><td>0.12 <b>(+41.10%)</b></td><td>0.12 <b>(+31.07%)</b></td><td>0.10 <b>(+75.33%)</b></td><td>0.01 (-13.12%)</td><td>180.70 <b>(-42.98%)</b></td><td>159.04 <b>(-30.59%)</b></td><td>156.40 <b>(-23.67%)</b></td><td>140.50 <b>(-30.20%)</b></td><td>16.98 <b>(-65.83%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>316.90 (n/a)</td><td>229.14 (n/a)</td><td>204.90 (n/a)</td><td>201.30 (n/a)</td><td>49.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (+4.39%)</td><td>0.09 (+2.55%)</td><td>0.09 (+3.29%)</td><td>0.07 (-0.98%)</td><td>0.01 (+15.51%)</td><td>222.20 (+1.00%)</td><td>193.94 (-2.15%)</td><td>192.70 (-3.21%)</td><td>154.90 (-4.21%)</td><td>26.72 (+11.12%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>198.20 (n/a)</td><td>199.10 (n/a)</td><td>161.70 (n/a)</td><td>24.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 <b>(+33.66%)</b></td><td>0.10 <b>(+30.37%)</b></td><td>0.10 <b>(+23.13%)</b></td><td>0.08 <b>(+45.24%)</b></td><td>0.02 <b>(+26.50%)</b></td><td>227.20 <b>(-31.15%)</b></td><td>177.82 <b>(-23.98%)</b></td><td>177.20 (-18.79%)</td><td>129.20 <b>(-25.19%)</b></td><td>37.10 <b>(-37.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>330.00 (n/a)</td><td>233.90 (n/a)</td><td>218.20 (n/a)</td><td>172.70 (n/a)</td><td>59.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (-13.24%)</td><td>0.08 (-5.66%)</td><td>0.08 (-9.92%)</td><td>0.08 (+5.18%)</td><td>0.01 <b>(-61.62%)</b></td><td>210.30 (-4.93%)</td><td>196.42 (+4.20%)</td><td>200.50 (+11.02%)</td><td>179.90 (+15.25%)</td><td>12.33 <b>(-59.11%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>188.50 (n/a)</td><td>180.60 (n/a)</td><td>156.10 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (-8.15%)</td><td>0.08 (-3.65%)</td><td>0.09 (+0.62%)</td><td>0.05 (-19.60%)</td><td>0.02 (+15.44%)</td><td>364.50 <b>(+24.40%)</b></td><td>223.48 (+7.75%)</td><td>193.10 (-0.62%)</td><td>161.30 (+8.91%)</td><td>82.94 <b>(+56.00%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>293.00 (n/a)</td><td>207.40 (n/a)</td><td>194.30 (n/a)</td><td>148.10 (n/a)</td><td>53.17 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (-5.00%)</td><td>0.07 (-6.28%)</td><td>0.08 (-5.07%)</td><td>0.07 (-1.39%)</td><td>0.00 <b>(-21.41%)</b></td><td>239.70 (+1.40%)</td><td>221.32 (+6.52%)</td><td>218.40 (+5.35%)</td><td>203.40 (+5.23%)</td><td>14.84 (-15.60%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>207.78 (n/a)</td><td>207.30 (n/a)</td><td>193.30 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 <b>(+23.97%)</b></td><td>0.18 (+10.04%)</td><td>0.17 (+3.17%)</td><td>0.16 (+19.23%)</td><td>0.03 <b>(+47.65%)</b></td><td>198.70 (-16.12%)</td><td>181.48 (-8.75%)</td><td>188.50 (-3.08%)</td><td>145.30 (-19.32%)</td><td>21.84 (-2.52%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>236.90 (n/a)</td><td>198.88 (n/a)</td><td>194.50 (n/a)</td><td>180.10 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (+10.78%)</td><td>0.20 (+4.12%)</td><td>0.20 (+7.02%)</td><td>0.17 (-1.70%)</td><td>0.03 <b>(+69.51%)</b></td><td>194.80 (+1.78%)</td><td>163.82 (-2.74%)</td><td>160.90 (-6.56%)</td><td>135.20 (-9.75%)</td><td>25.92 <b>(+57.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>191.40 (n/a)</td><td>168.44 (n/a)</td><td>172.20 (n/a)</td><td>149.80 (n/a)</td><td>16.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 (+5.20%)</td><td>0.25 (+7.96%)</td><td>0.24 (-1.85%)</td><td>0.22 (+14.68%)</td><td>0.02 <b>(-30.31%)</b></td><td>188.50 (-12.77%)</td><td>167.74 (-8.43%)</td><td>172.30 (+1.89%)</td><td>146.50 (-4.93%)</td><td>16.05 <b>(-43.85%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>216.10 (n/a)</td><td>183.18 (n/a)</td><td>169.10 (n/a)</td><td>154.10 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (+9.14%)</td><td>0.17 (-5.32%)</td><td>0.17 (+1.11%)</td><td>0.10 <b>(-38.05%)</b></td><td>0.05 <b>(+113.16%)</b></td><td>321.00 <b>(+61.47%)</b></td><td>205.44 (+12.98%)</td><td>192.40 (-1.13%)</td><td>136.00 (-8.42%)</td><td>70.04 <b>(+225.32%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>181.84 (n/a)</td><td>194.60 (n/a)</td><td>148.50 (n/a)</td><td>21.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.30 (+19.93%)</td><td>0.24 (+10.33%)</td><td>0.24 (+9.28%)</td><td>0.20 (+5.19%)</td><td>0.04 <b>(+99.86%)</b></td><td>200.30 (-4.94%)</td><td>174.00 (-8.23%)</td><td>173.60 (-8.49%)</td><td>138.80 (-16.64%)</td><td>25.48 <b>(+61.83%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>189.60 (n/a)</td><td>189.70 (n/a)</td><td>166.50 (n/a)</td><td>15.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (-4.59%)</td><td>0.21 (+1.59%)</td><td>0.21 (+10.90%)</td><td>0.17 (+1.99%)</td><td>0.03 <b>(-30.93%)</b></td><td>190.50 (-1.96%)</td><td>160.84 (-2.79%)</td><td>157.90 (-9.82%)</td><td>136.70 (+4.83%)</td><td>20.22 <b>(-28.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.30 (n/a)</td><td>165.46 (n/a)</td><td>175.10 (n/a)</td><td>130.40 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (-14.85%)</td><td>0.18 (-12.17%)</td><td>0.18 (-9.41%)</td><td>0.15 (-9.62%)</td><td>0.03 <b>(-33.15%)</b></td><td>250.10 (+10.66%)</td><td>207.72 (+12.09%)</td><td>207.80 (+10.36%)</td><td>168.90 (+17.45%)</td><td>34.52 (-12.91%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>226.00 (n/a)</td><td>185.32 (n/a)</td><td>188.30 (n/a)</td><td>143.80 (n/a)</td><td>39.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (-15.62%)</td><td>0.19 (+2.23%)</td><td>0.18 (+8.39%)</td><td>0.17 <b>(+43.60%)</b></td><td>0.02 <b>(-70.47%)</b></td><td>188.40 <b>(-30.38%)</b></td><td>176.16 (-8.43%)</td><td>180.10 (-7.74%)</td><td>152.30 (+18.52%)</td><td>13.83 <b>(-75.68%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>270.60 (n/a)</td><td>192.38 (n/a)</td><td>195.20 (n/a)</td><td>128.50 (n/a)</td><td>56.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.30 (-5.75%)</td><td>0.23 (+2.64%)</td><td>0.23 (+11.05%)</td><td>0.18 (-3.92%)</td><td>0.05 (-16.29%)</td><td>210.50 (+4.10%)</td><td>165.18 (-3.34%)</td><td>163.70 (-9.96%)</td><td>121.90 (+6.09%)</td><td>31.74 (-4.07%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>202.20 (n/a)</td><td>170.88 (n/a)</td><td>181.80 (n/a)</td><td>114.90 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (-12.16%)</td><td>0.19 (+6.07%)</td><td>0.19 (+12.58%)</td><td>0.16 <b>(+23.50%)</b></td><td>0.02 <b>(-47.27%)</b></td><td>210.70 (-19.05%)</td><td>178.80 (-8.46%)</td><td>168.90 (-11.15%)</td><td>157.90 (+13.84%)</td><td>21.41 <b>(-50.85%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>260.30 (n/a)</td><td>195.32 (n/a)</td><td>190.10 (n/a)</td><td>138.70 (n/a)</td><td>43.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 <b>(+27.06%)</b></td><td>0.19 <b>(+26.11%)</b></td><td>0.19 (+18.00%)</td><td>0.16 <b>(+43.97%)</b></td><td>0.03 (+14.82%)</td><td>215.10 <b>(-30.55%)</b></td><td>183.18 <b>(-21.31%)</b></td><td>184.00 (-15.25%)</td><td>155.70 <b>(-21.28%)</b></td><td>26.87 <b>(-40.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>309.70 (n/a)</td><td>232.78 (n/a)</td><td>217.10 (n/a)</td><td>197.80 (n/a)</td><td>44.79 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (+19.40%)</td><td>0.19 (+13.75%)</td><td>0.17 (-1.04%)</td><td>0.16 (+8.20%)</td><td>0.03 <b>(+99.36%)</b></td><td>204.70 (-7.54%)</td><td>178.02 (-10.65%)</td><td>196.10 (+1.03%)</td><td>144.80 (-16.25%)</td><td>30.12 <b>(+49.71%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>199.24 (n/a)</td><td>194.10 (n/a)</td><td>172.90 (n/a)</td><td>20.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (+16.51%)</td><td>0.19 (+15.15%)</td><td>0.20 <b>(+20.03%)</b></td><td>0.11 <b>(-20.69%)</b></td><td>0.05 <b>(+136.81%)</b></td><td>314.00 <b>(+26.10%)</b></td><td>193.10 (-7.84%)</td><td>170.70 (-16.69%)</td><td>153.60 (-14.19%)</td><td>68.09 <b>(+162.66%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>249.00 (n/a)</td><td>209.52 (n/a)</td><td>204.90 (n/a)</td><td>179.00 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (-5.03%)</td><td>0.16 (+4.01%)</td><td>0.15 (+2.89%)</td><td>0.14 (+7.38%)</td><td>0.02 (-18.65%)</td><td>237.10 (-6.87%)</td><td>211.52 (-4.34%)</td><td>220.10 (-2.83%)</td><td>184.50 (+5.31%)</td><td>23.34 (-18.90%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>254.60 (n/a)</td><td>221.12 (n/a)</td><td>226.50 (n/a)</td><td>175.20 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (-3.54%)</td><td>0.13 (-8.40%)</td><td>0.12 (-9.76%)</td><td>0.11 (-6.78%)</td><td>0.03 (+4.35%)</td><td>194.70 (+7.27%)</td><td>165.96 (+9.78%)</td><td>168.10 (+10.81%)</td><td>118.00 (+3.69%)</td><td>31.04 (+15.83%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>181.50 (n/a)</td><td>151.18 (n/a)</td><td>151.70 (n/a)</td><td>113.80 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.16 (-3.62%)</td><td>0.10 <b>(-23.69%)</b></td><td>0.09 <b>(-33.02%)</b></td><td>0.08 <b>(-30.64%)</b></td><td>0.03 <b>(+34.90%)</b></td><td>271.10 <b>(+44.20%)</b></td><td>213.76 <b>(+36.92%)</b></td><td>239.90 <b>(+49.28%)</b></td><td>130.00 (+3.75%)</td><td>56.84 <b>(+102.37%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>188.00 (n/a)</td><td>156.12 (n/a)</td><td>160.70 (n/a)</td><td>125.30 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (+4.96%)</td><td>0.12 (-4.13%)</td><td>0.11 (-12.95%)</td><td>0.08 (-13.79%)</td><td>0.03 <b>(+31.58%)</b></td><td>245.20 (+15.99%)</td><td>183.42 (+6.32%)</td><td>179.70 (+14.90%)</td><td>138.20 (-4.76%)</td><td>42.54 <b>(+43.67%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.40 (n/a)</td><td>172.52 (n/a)</td><td>156.40 (n/a)</td><td>145.10 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (+3.54%)</td><td>0.13 (+4.26%)</td><td>0.13 (+4.11%)</td><td>0.09 (-1.84%)</td><td>0.02 <b>(+33.96%)</b></td><td>224.40 (+1.91%)</td><td>167.56 (-2.75%)</td><td>158.50 (-3.94%)</td><td>136.90 (-3.46%)</td><td>36.39 <b>(+25.85%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>220.20 (n/a)</td><td>172.30 (n/a)</td><td>165.00 (n/a)</td><td>141.80 (n/a)</td><td>28.92 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (-1.17%)</td><td>0.11 (-10.81%)</td><td>0.13 (+1.19%)</td><td>0.05 <b>(-51.34%)</b></td><td>0.04 <b>(+173.08%)</b></td><td>383.10 <b>(+105.53%)</b></td><td>210.88 <b>(+27.01%)</b></td><td>163.10 (-1.21%)</td><td>141.30 (+1.22%)</td><td>100.71 <b>(+486.20%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>166.04 (n/a)</td><td>165.10 (n/a)</td><td>139.60 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (+11.10%)</td><td>0.12 (+9.72%)</td><td>0.13 (+19.58%)</td><td>0.09 (-5.42%)</td><td>0.03 <b>(+24.99%)</b></td><td>240.00 (+5.73%)</td><td>174.66 (-7.67%)</td><td>162.20 (-16.35%)</td><td>137.20 (-10.03%)</td><td>40.91 <b>(+22.32%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>227.00 (n/a)</td><td>189.16 (n/a)</td><td>193.90 (n/a)</td><td>152.50 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (-2.37%)</td><td>0.12 (-4.21%)</td><td>0.11 (-5.74%)</td><td>0.10 (+3.31%)</td><td>0.02 (-7.15%)</td><td>200.70 (-3.23%)</td><td>175.32 (+4.01%)</td><td>179.30 (+6.09%)</td><td>134.70 (+2.36%)</td><td>24.66 (-10.18%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.40 (n/a)</td><td>168.56 (n/a)</td><td>169.00 (n/a)</td><td>131.60 (n/a)</td><td>27.46 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (+4.14%)</td><td>0.12 (+11.71%)</td><td>0.12 <b>(+22.34%)</b></td><td>0.10 (+4.58%)</td><td>0.02 (-15.22%)</td><td>214.60 (-4.37%)</td><td>171.96 (-11.11%)</td><td>165.60 (-18.26%)</td><td>152.40 (-3.97%)</td><td>25.13 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>224.40 (n/a)</td><td>193.46 (n/a)</td><td>202.60 (n/a)</td><td>158.70 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (-1.87%)</td><td>0.15 (-6.78%)</td><td>0.15 (-9.84%)</td><td>0.11 (-10.89%)</td><td>0.03 (-12.01%)</td><td>224.20 (+12.21%)</td><td>173.52 (+6.81%)</td><td>166.10 (+10.88%)</td><td>133.30 (+1.91%)</td><td>32.99 (-0.53%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>199.80 (n/a)</td><td>162.46 (n/a)</td><td>149.80 (n/a)</td><td>130.80 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (+4.00%)</td><td>0.15 (+2.54%)</td><td>0.14 (+0.33%)</td><td>0.12 (+5.44%)</td><td>0.02 (+3.16%)</td><td>209.50 (-5.16%)</td><td>169.86 (-2.56%)</td><td>171.10 (-0.29%)</td><td>133.60 (-3.82%)</td><td>28.34 (-7.21%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.90 (n/a)</td><td>174.32 (n/a)</td><td>171.60 (n/a)</td><td>138.90 (n/a)</td><td>30.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (+8.41%)</td><td>0.13 (-7.15%)</td><td>0.13 (-3.04%)</td><td>0.08 <b>(-20.07%)</b></td><td>0.03 <b>(+40.47%)</b></td><td>292.10 <b>(+25.15%)</b></td><td>206.00 (+11.33%)</td><td>192.50 (+3.16%)</td><td>138.80 (-7.71%)</td><td>56.81 <b>(+66.90%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>233.40 (n/a)</td><td>185.04 (n/a)</td><td>186.60 (n/a)</td><td>150.40 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (-19.53%)</td><td>0.11 <b>(-24.73%)</b></td><td>0.11 <b>(-25.14%)</b></td><td>0.08 <b>(-29.24%)</b></td><td>0.02 (-10.56%)</td><td>292.70 <b>(+41.26%)</b></td><td>227.14 <b>(+33.90%)</b></td><td>225.00 <b>(+33.61%)</b></td><td>179.20 <b>(+24.27%)</b></td><td>42.10 <b>(+61.54%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.20 (n/a)</td><td>169.64 (n/a)</td><td>168.40 (n/a)</td><td>144.20 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 <b>(-21.11%)</b></td><td>0.14 (-4.79%)</td><td>0.15 (+9.86%)</td><td>0.13 (-1.77%)</td><td>0.01 <b>(-61.97%)</b></td><td>195.60 (+1.82%)</td><td>174.02 (+3.13%)</td><td>168.20 (-8.98%)</td><td>164.00 <b>(+26.84%)</b></td><td>13.13 <b>(-51.18%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.10 (n/a)</td><td>168.74 (n/a)</td><td>184.80 (n/a)</td><td>129.30 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.16 (+4.27%)</td><td>0.15 (+16.11%)</td><td>0.15 (+15.35%)</td><td>0.11 <b>(+48.17%)</b></td><td>0.02 <b>(-33.77%)</b></td><td>220.50 <b>(-32.51%)</b></td><td>171.82 (-17.63%)</td><td>161.00 (-13.35%)</td><td>152.10 (-4.10%)</td><td>27.67 <b>(-58.74%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>326.70 (n/a)</td><td>208.60 (n/a)</td><td>185.80 (n/a)</td><td>158.60 (n/a)</td><td>67.07 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (-8.94%)</td><td>0.13 (-1.33%)</td><td>0.14 (+11.14%)</td><td>0.11 (+2.93%)</td><td>0.02 (-15.27%)</td><td>223.80 (-2.86%)</td><td>187.90 (+0.82%)</td><td>173.70 (-10.05%)</td><td>160.60 (+9.85%)</td><td>30.14 (-7.99%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>230.40 (n/a)</td><td>186.38 (n/a)</td><td>193.10 (n/a)</td><td>146.20 (n/a)</td><td>32.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 <b>(+55.56%)</b></td><td>0.16 <b>(+26.54%)</b></td><td>0.16 <b>(+20.40%)</b></td><td>0.13 (+14.31%)</td><td>0.04 <b>(+189.65%)</b></td><td>187.70 (-12.49%)</td><td>156.20 (-18.65%)</td><td>157.10 (-16.97%)</td><td>107.00 <b>(-35.74%)</b></td><td>30.61 <b>(+56.07%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>192.02 (n/a)</td><td>189.20 (n/a)</td><td>166.50 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 <b>(+22.20%)</b></td><td>0.11 (+10.02%)</td><td>0.11 (+0.82%)</td><td>0.09 (+17.06%)</td><td>0.02 <b>(+24.48%)</b></td><td>204.70 (-14.60%)</td><td>169.38 (-8.99%)</td><td>166.70 (-0.83%)</td><td>129.60 (-18.18%)</td><td>28.66 (-14.02%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>239.70 (n/a)</td><td>186.12 (n/a)</td><td>168.10 (n/a)</td><td>158.40 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (-19.22%)</td><td>0.11 (-11.16%)</td><td>0.11 (-9.08%)</td><td>0.09 (+0.56%)</td><td>0.02 <b>(-39.43%)</b></td><td>200.90 (-0.54%)</td><td>169.38 (+10.24%)</td><td>162.70 (+10.01%)</td><td>142.90 <b>(+23.83%)</b></td><td>25.65 <b>(-25.28%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>202.00 (n/a)</td><td>153.64 (n/a)</td><td>147.90 (n/a)</td><td>115.40 (n/a)</td><td>34.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (-6.26%)</td><td>0.11 (-9.56%)</td><td>0.10 (-10.10%)</td><td>0.09 (-13.33%)</td><td>0.02 (+9.39%)</td><td>200.60 (+15.35%)</td><td>177.98 (+11.06%)</td><td>183.60 (+11.21%)</td><td>140.20 (+6.62%)</td><td>22.55 <b>(+32.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>173.90 (n/a)</td><td>160.26 (n/a)</td><td>165.10 (n/a)</td><td>131.50 (n/a)</td><td>17.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 <b>(+21.99%)</b></td><td>0.11 (+1.98%)</td><td>0.10 (-1.34%)</td><td>0.08 (-11.91%)</td><td>0.03 <b>(+121.57%)</b></td><td>219.40 (+13.50%)</td><td>179.38 (+1.06%)</td><td>182.10 (+1.34%)</td><td>122.00 (-18.01%)</td><td>36.20 <b>(+97.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>177.50 (n/a)</td><td>179.70 (n/a)</td><td>148.80 (n/a)</td><td>18.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (+17.62%)</td><td>0.11 (+5.32%)</td><td>0.11 (+6.80%)</td><td>0.08 (-9.22%)</td><td>0.02 <b>(+72.15%)</b></td><td>237.60 (+10.15%)</td><td>177.98 (-2.97%)</td><td>168.20 (-6.35%)</td><td>133.70 (-14.95%)</td><td>37.87 <b>(+63.34%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>183.42 (n/a)</td><td>179.60 (n/a)</td><td>157.20 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (-6.39%)</td><td>0.10 (-11.30%)</td><td>0.10 (-14.71%)</td><td>0.08 (-12.39%)</td><td>0.02 (+11.38%)</td><td>235.00 (+14.19%)</td><td>187.30 (+13.61%)</td><td>187.90 (+17.22%)</td><td>147.80 (+6.79%)</td><td>32.75 <b>(+32.34%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>205.80 (n/a)</td><td>164.86 (n/a)</td><td>160.30 (n/a)</td><td>138.40 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (+7.18%)</td><td>0.10 (+2.34%)</td><td>0.11 (+4.04%)</td><td>0.07 (-17.30%)</td><td>0.02 <b>(+41.22%)</b></td><td>271.10 <b>(+20.92%)</b></td><td>187.12 (+0.57%)</td><td>161.40 (-3.87%)</td><td>145.40 (-6.74%)</td><td>52.62 <b>(+55.58%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>224.20 (n/a)</td><td>186.06 (n/a)</td><td>167.90 (n/a)</td><td>155.90 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (-3.63%)</td><td>0.10 (-1.15%)</td><td>0.11 (+13.04%)</td><td>0.06 <b>(-24.51%)</b></td><td>0.02 <b>(+26.74%)</b></td><td>302.20 <b>(+32.43%)</b></td><td>199.12 (+4.38%)</td><td>171.20 (-11.52%)</td><td>154.60 (+3.76%)</td><td>59.95 <b>(+79.32%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>228.20 (n/a)</td><td>190.76 (n/a)</td><td>193.50 (n/a)</td><td>149.00 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.73 (+8.75%)</td><td>0.59 (+7.12%)</td><td>0.57 (+6.90%)</td><td>0.44 (-4.29%)</td><td>0.12 <b>(+57.87%)</b></td><td>223.80 (+4.48%)</td><td>172.24 (-4.67%)</td><td>172.40 (-6.46%)</td><td>134.00 (-8.03%)</td><td>37.12 <b>(+50.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.67 (n/a)</td><td>0.55 (n/a)</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>214.20 (n/a)</td><td>180.68 (n/a)</td><td>184.30 (n/a)</td><td>145.70 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.66 (+6.78%)</td><td>0.56 (+6.09%)</td><td>0.55 (+0.16%)</td><td>0.41 (+0.13%)</td><td>0.10 <b>(+30.14%)</b></td><td>239.00 (-0.13%)</td><td>181.76 (-4.79%)</td><td>177.90 (-0.17%)</td><td>149.40 (-6.39%)</td><td>36.40 (+18.32%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.62 (n/a)</td><td>0.52 (n/a)</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.08 (n/a)</td><td>239.30 (n/a)</td><td>190.90 (n/a)</td><td>178.20 (n/a)</td><td>159.60 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.70 (-0.88%)</td><td>0.56 (+5.33%)</td><td>0.53 (+13.00%)</td><td>0.43 (+1.11%)</td><td>0.11 (-9.89%)</td><td>226.50 (-1.09%)</td><td>180.66 (-5.77%)</td><td>186.00 (-11.51%)</td><td>139.70 (+0.87%)</td><td>34.42 (-11.44%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.71 (n/a)</td><td>0.53 (n/a)</td><td>0.47 (n/a)</td><td>0.43 (n/a)</td><td>0.12 (n/a)</td><td>229.00 (n/a)</td><td>191.72 (n/a)</td><td>210.20 (n/a)</td><td>138.50 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.71 <b>(+30.66%)</b></td><td>0.57 <b>(+24.96%)</b></td><td>0.58 <b>(+29.28%)</b></td><td>0.45 (+16.13%)</td><td>0.11 <b>(+99.80%)</b></td><td>217.80 (-13.88%)</td><td>179.16 (-18.29%)</td><td>169.90 <b>(-22.63%)</b></td><td>138.00 <b>(-23.46%)</b></td><td>36.04 <b>(+39.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.55 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.06 (n/a)</td><td>252.90 (n/a)</td><td>219.26 (n/a)</td><td>219.60 (n/a)</td><td>180.30 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.52 (-2.85%)</td><td>0.41 (-6.54%)</td><td>0.45 (+9.51%)</td><td>0.21 <b>(-46.04%)</b></td><td>0.12 <b>(+110.78%)</b></td><td>350.20 <b>(+85.29%)</b></td><td>201.20 (+17.13%)</td><td>162.50 (-8.66%)</td><td>142.70 (+2.96%)</td><td>85.14 <b>(+333.98%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.06 (n/a)</td><td>189.00 (n/a)</td><td>171.78 (n/a)</td><td>177.90 (n/a)</td><td>138.60 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.60 <b>(+47.41%)</b></td><td>0.43 <b>(+20.52%)</b></td><td>0.38 (-3.84%)</td><td>0.35 <b>(+40.74%)</b></td><td>0.10 <b>(+54.16%)</b></td><td>213.00 <b>(-28.95%)</b></td><td>176.98 (-16.68%)</td><td>192.80 (+3.99%)</td><td>122.60 <b>(-32.15%)</b></td><td>36.64 <b>(-27.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>299.80 (n/a)</td><td>212.40 (n/a)</td><td>185.40 (n/a)</td><td>180.70 (n/a)</td><td>50.34 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.57 <b>(+22.32%)</b></td><td>0.42 (+5.15%)</td><td>0.43 (+11.34%)</td><td>0.20 <b>(-44.52%)</b></td><td>0.14 <b>(+208.96%)</b></td><td>370.90 <b>(+80.22%)</b></td><td>200.76 (+7.76%)</td><td>171.00 (-10.19%)</td><td>129.30 (-18.22%)</td><td>97.76 <b>(+378.31%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.05 (n/a)</td><td>205.80 (n/a)</td><td>186.30 (n/a)</td><td>190.40 (n/a)</td><td>158.10 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.46 (-7.81%)</td><td>0.40 (-3.63%)</td><td>0.39 (-15.63%)</td><td>0.38 (+19.14%)</td><td>0.04 <b>(-53.79%)</b></td><td>196.20 (-16.08%)</td><td>183.26 (+1.34%)</td><td>190.80 (+18.51%)</td><td>160.20 (+8.54%)</td><td>15.19 <b>(-58.12%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>233.80 (n/a)</td><td>180.84 (n/a)</td><td>161.00 (n/a)</td><td>147.60 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (-7.81%)</td><td>0.22 (-5.49%)</td><td>0.22 (-5.26%)</td><td>0.15 <b>(-20.96%)</b></td><td>0.05 <b>(+30.84%)</b></td><td>246.60 <b>(+26.53%)</b></td><td>177.04 (+8.48%)</td><td>171.00 (+5.56%)</td><td>138.70 (+8.53%)</td><td>43.82 <b>(+80.18%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>194.90 (n/a)</td><td>163.20 (n/a)</td><td>162.00 (n/a)</td><td>127.80 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (+3.61%)</td><td>0.21 (+1.86%)</td><td>0.20 (+0.41%)</td><td>0.18 (-5.11%)</td><td>0.03 <b>(+35.14%)</b></td><td>206.00 (+5.37%)</td><td>177.36 (-1.02%)</td><td>185.40 (-0.43%)</td><td>143.60 (-3.49%)</td><td>26.12 <b>(+37.46%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>195.50 (n/a)</td><td>179.18 (n/a)</td><td>186.20 (n/a)</td><td>148.80 (n/a)</td><td>19.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 <b>(-20.09%)</b></td><td>0.22 (-3.52%)</td><td>0.21 (-1.35%)</td><td>0.20 (+18.66%)</td><td>0.02 <b>(-71.57%)</b></td><td>184.00 (-15.71%)</td><td>169.40 (-1.19%)</td><td>172.90 (+1.35%)</td><td>150.50 <b>(+25.10%)</b></td><td>12.45 <b>(-70.78%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>218.30 (n/a)</td><td>171.44 (n/a)</td><td>170.60 (n/a)</td><td>120.30 (n/a)</td><td>42.61 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (-15.91%)</td><td>0.22 (-3.85%)</td><td>0.22 (+0.18%)</td><td>0.19 (-2.23%)</td><td>0.02 <b>(-42.11%)</b></td><td>196.90 (+2.29%)</td><td>171.58 (+2.63%)</td><td>171.40 (-0.17%)</td><td>146.80 (+18.87%)</td><td>19.00 <b>(-26.62%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>192.50 (n/a)</td><td>167.18 (n/a)</td><td>171.70 (n/a)</td><td>123.50 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (-19.43%)</td><td>0.19 (-16.00%)</td><td>0.18 <b>(-23.88%)</b></td><td>0.16 (-3.09%)</td><td>0.02 <b>(-52.12%)</b></td><td>224.80 (+3.17%)</td><td>198.32 (+15.95%)</td><td>200.40 <b>(+31.32%)</b></td><td>167.80 <b>(+24.11%)</b></td><td>22.66 <b>(-39.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>217.90 (n/a)</td><td>171.04 (n/a)</td><td>152.60 (n/a)</td><td>135.20 (n/a)</td><td>37.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 <b>(-25.98%)</b></td><td>0.19 (-11.86%)</td><td>0.20 (-5.41%)</td><td>0.16 (-10.05%)</td><td>0.02 <b>(-53.32%)</b></td><td>227.40 (+11.14%)</td><td>195.18 (+11.34%)</td><td>187.70 (+5.75%)</td><td>174.90 <b>(+35.16%)</b></td><td>21.54 <b>(-30.57%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>204.60 (n/a)</td><td>175.30 (n/a)</td><td>177.50 (n/a)</td><td>129.40 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.30 <b>(+42.19%)</b></td><td>0.23 <b>(+20.22%)</b></td><td>0.21 (+11.90%)</td><td>0.17 (-2.94%)</td><td>0.05 <b>(+298.54%)</b></td><td>213.10 (+3.00%)</td><td>168.40 (-13.69%)</td><td>177.20 (-10.64%)</td><td>123.10 <b>(-29.70%)</b></td><td>36.88 <b>(+184.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>195.12 (n/a)</td><td>198.30 (n/a)</td><td>175.10 (n/a)</td><td>12.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 <b>(+37.34%)</b></td><td>0.24 <b>(+23.61%)</b></td><td>0.23 (+10.36%)</td><td>0.20 <b>(+35.06%)</b></td><td>0.05 <b>(+49.61%)</b></td><td>182.90 <b>(-25.95%)</b></td><td>154.22 (-18.87%)</td><td>162.70 (-9.36%)</td><td>115.30 <b>(-27.21%)</b></td><td>25.40 <b>(-24.18%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>247.00 (n/a)</td><td>190.08 (n/a)</td><td>179.50 (n/a)</td><td>158.40 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (-5.63%)</td><td>0.21 (+4.81%)</td><td>0.22 (-8.05%)</td><td>0.19 <b>(+78.96%)</b></td><td>0.01 <b>(-78.31%)</b></td><td>210.10 <b>(-44.11%)</b></td><td>193.30 (-12.53%)</td><td>190.10 (+8.75%)</td><td>182.20 (+5.93%)</td><td>11.20 <b>(-87.26%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>375.90 (n/a)</td><td>221.00 (n/a)</td><td>174.80 (n/a)</td><td>172.00 (n/a)</td><td>87.90 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (+1.67%)</td><td>0.23 (+0.16%)</td><td>0.22 (-6.03%)</td><td>0.20 (+1.30%)</td><td>0.03 (+3.99%)</td><td>203.00 (-1.26%)</td><td>181.52 (-0.11%)</td><td>186.30 (+6.46%)</td><td>149.60 (-1.64%)</td><td>22.20 (-0.25%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>205.60 (n/a)</td><td>181.72 (n/a)</td><td>175.00 (n/a)</td><td>152.10 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (-9.32%)</td><td>0.25 (-7.87%)</td><td>0.23 (-13.52%)</td><td>0.22 (-1.52%)</td><td>0.04 (-12.70%)</td><td>189.50 (+1.55%)</td><td>167.28 (+8.22%)</td><td>177.50 (+15.64%)</td><td>127.00 (+10.24%)</td><td>26.53 (+0.87%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>186.60 (n/a)</td><td>154.58 (n/a)</td><td>153.50 (n/a)</td><td>115.20 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 <b>(-30.84%)</b></td><td>0.21 (-8.04%)</td><td>0.21 (-10.92%)</td><td>0.19 <b>(+35.34%)</b></td><td>0.02 <b>(-79.38%)</b></td><td>218.00 <b>(-26.13%)</b></td><td>194.88 (+0.01%)</td><td>194.20 (+12.25%)</td><td>178.10 <b>(+44.56%)</b></td><td>14.55 <b>(-78.09%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>295.10 (n/a)</td><td>194.86 (n/a)</td><td>173.00 (n/a)</td><td>123.20 (n/a)</td><td>66.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (-17.38%)</td><td>0.23 (-8.75%)</td><td>0.22 (-0.49%)</td><td>0.19 (+3.02%)</td><td>0.04 <b>(-41.73%)</b></td><td>214.90 (-2.94%)</td><td>180.20 (+6.02%)</td><td>185.90 (+0.49%)</td><td>141.50 <b>(+21.04%)</b></td><td>29.92 <b>(-30.59%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>221.40 (n/a)</td><td>169.96 (n/a)</td><td>185.00 (n/a)</td><td>116.90 (n/a)</td><td>43.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (-2.83%)</td><td>0.20 (-17.65%)</td><td>0.20 <b>(-24.48%)</b></td><td>0.13 <b>(-22.28%)</b></td><td>0.06 (+15.00%)</td><td>318.10 <b>(+28.68%)</b></td><td>217.58 <b>(+24.62%)</b></td><td>209.50 <b>(+32.43%)</b></td><td>140.10 (+2.94%)</td><td>63.90 <b>(+47.52%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>247.20 (n/a)</td><td>174.60 (n/a)</td><td>158.20 (n/a)</td><td>136.10 (n/a)</td><td>43.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (-7.09%)</td><td>0.23 (-1.39%)</td><td>0.23 (+4.10%)</td><td>0.19 (-2.52%)</td><td>0.02 <b>(-21.68%)</b></td><td>211.10 (+2.58%)</td><td>182.56 (+0.92%)</td><td>175.20 (-3.95%)</td><td>160.50 (+7.65%)</td><td>20.61 (-13.98%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>205.80 (n/a)</td><td>180.90 (n/a)</td><td>182.40 (n/a)</td><td>149.10 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.37 <b>(+59.83%)</b></td><td>0.27 <b>(+30.17%)</b></td><td>0.27 <b>(+33.20%)</b></td><td>0.20 (+4.11%)</td><td>0.06 <b>(+273.01%)</b></td><td>205.50 (-3.97%)</td><td>156.84 <b>(-20.27%)</b></td><td>151.20 <b>(-24.93%)</b></td><td>109.80 <b>(-37.47%)</b></td><td>35.29 <b>(+122.71%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>214.00 (n/a)</td><td>196.72 (n/a)</td><td>201.40 (n/a)</td><td>175.60 (n/a)</td><td>15.85 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (-1.00%)</td><td>0.21 (+4.59%)</td><td>0.23 (+19.67%)</td><td>0.14 (+14.15%)</td><td>0.05 (-18.42%)</td><td>244.80 (-12.42%)</td><td>172.52 (-7.01%)</td><td>148.40 (-16.44%)</td><td>133.90 (+0.98%)</td><td>45.18 <b>(-24.75%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>279.50 (n/a)</td><td>185.52 (n/a)</td><td>177.60 (n/a)</td><td>132.60 (n/a)</td><td>60.03 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (-3.92%)</td><td>0.21 (+13.53%)</td><td>0.20 (+12.05%)</td><td>0.18 <b>(+47.85%)</b></td><td>0.03 <b>(-42.96%)</b></td><td>190.70 <b>(-32.38%)</b></td><td>165.76 (-16.32%)</td><td>170.00 (-10.76%)</td><td>138.20 (+4.07%)</td><td>23.14 <b>(-60.04%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>282.00 (n/a)</td><td>198.08 (n/a)</td><td>190.50 (n/a)</td><td>132.80 (n/a)</td><td>57.91 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (-1.27%)</td><td>0.24 <b>(+26.18%)</b></td><td>0.23 <b>(+33.45%)</b></td><td>0.20 <b>(+89.15%)</b></td><td>0.04 <b>(-48.78%)</b></td><td>176.30 <b>(-47.14%)</b></td><td>148.34 <b>(-29.40%)</b></td><td>150.00 <b>(-25.07%)</b></td><td>122.00 (+1.24%)</td><td>23.94 <b>(-72.39%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>333.50 (n/a)</td><td>210.12 (n/a)</td><td>200.20 (n/a)</td><td>120.50 (n/a)</td><td>86.70 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 (-7.95%)</td><td>0.22 (-13.31%)</td><td>0.19 <b>(-21.39%)</b></td><td>0.18 (+10.50%)</td><td>0.04 <b>(-25.88%)</b></td><td>188.40 (-9.51%)</td><td>165.50 (+12.97%)</td><td>178.90 <b>(+27.24%)</b></td><td>123.00 (+8.66%)</td><td>27.13 <b>(-28.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>208.20 (n/a)</td><td>146.50 (n/a)</td><td>140.60 (n/a)</td><td>113.20 (n/a)</td><td>37.69 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 <b>(+26.95%)</b></td><td>0.22 (+2.22%)</td><td>0.20 (-4.52%)</td><td>0.14 <b>(-23.06%)</b></td><td>0.07 <b>(+182.99%)</b></td><td>243.30 <b>(+29.97%)</b></td><td>170.50 (+4.33%)</td><td>175.20 (+4.72%)</td><td>109.30 <b>(-21.25%)</b></td><td>51.08 <b>(+188.21%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>187.20 (n/a)</td><td>163.42 (n/a)</td><td>167.30 (n/a)</td><td>138.80 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (-10.98%)</td><td>0.21 (-9.23%)</td><td>0.21 (-6.81%)</td><td>0.16 (-6.45%)</td><td>0.04 <b>(-22.74%)</b></td><td>211.10 (+6.89%)</td><td>170.02 (+8.86%)</td><td>165.30 (+7.34%)</td><td>128.40 (+12.34%)</td><td>32.57 (-7.76%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>197.50 (n/a)</td><td>156.18 (n/a)</td><td>154.00 (n/a)</td><td>114.30 (n/a)</td><td>35.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 <b>(+44.77%)</b></td><td>0.23 <b>(+40.92%)</b></td><td>0.22 <b>(+34.74%)</b></td><td>0.17 <b>(+23.81%)</b></td><td>0.04 <b>(+81.21%)</b></td><td>202.20 (-19.22%)</td><td>157.66 <b>(-28.26%)</b></td><td>155.80 <b>(-25.77%)</b></td><td>126.20 <b>(-30.96%)</b></td><td>28.75 (-0.21%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>250.30 (n/a)</td><td>219.76 (n/a)</td><td>209.90 (n/a)</td><td>182.80 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (+13.59%)</td><td>0.22 (+17.09%)</td><td>0.23 <b>(+24.60%)</b></td><td>0.17 (+4.17%)</td><td>0.03 <b>(+29.23%)</b></td><td>200.90 (-4.01%)</td><td>159.44 (-14.13%)</td><td>152.50 (-19.74%)</td><td>136.10 (-11.97%)</td><td>26.37 (+7.63%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>209.30 (n/a)</td><td>185.68 (n/a)</td><td>190.00 (n/a)</td><td>154.60 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.09 (+17.44%)</td><td>0.76 (-5.42%)</td><td>0.73 (-1.27%)</td><td>0.54 (-19.82%)</td><td>0.21 <b>(+75.24%)</b></td><td>241.70 <b>(+24.72%)</b></td><td>182.80 (+9.63%)</td><td>179.60 (+1.30%)</td><td>120.10 (-14.82%)</td><td>44.59 <b>(+86.93%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.93 (n/a)</td><td>0.80 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.12 (n/a)</td><td>193.80 (n/a)</td><td>166.74 (n/a)</td><td>177.30 (n/a)</td><td>141.00 (n/a)</td><td>23.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.08 (+19.11%)</td><td>0.76 (-4.46%)</td><td>0.68 (-17.40%)</td><td>0.66 (-4.45%)</td><td>0.18 <b>(+84.46%)</b></td><td>199.00 (+4.63%)</td><td>178.28 (+7.05%)</td><td>193.30 <b>(+21.04%)</b></td><td>121.60 (-16.02%)</td><td>32.47 <b>(+56.67%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.91 (n/a)</td><td>0.80 (n/a)</td><td>0.82 (n/a)</td><td>0.69 (n/a)</td><td>0.10 (n/a)</td><td>190.20 (n/a)</td><td>166.54 (n/a)</td><td>159.70 (n/a)</td><td>144.80 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.71 (-3.70%)</td><td>0.68 (-6.55%)</td><td>0.68 (-5.91%)</td><td>0.61 (-13.01%)</td><td>0.04 <b>(+167.42%)</b></td><td>213.60 (+14.96%)</td><td>194.22 (+7.28%)</td><td>193.90 (+6.30%)</td><td>183.80 (+3.84%)</td><td>11.89 <b>(+222.16%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>181.04 (n/a)</td><td>182.40 (n/a)</td><td>177.00 (n/a)</td><td>3.69 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.00 <b>(+266.67%)</b></td><td>0.00 <b>(+289.29%)</b></td><td>0.00 <b>(+300.00%)</b></td><td>0.00 <b>(+330.00%)</b></td><td>0.00 <b>(-34.53%)</b></td><td>950.10 <b>(-75.66%)</b></td><td>943.00 <b>(-73.96%)</b></td><td>941.28 <b>(-74.03%)</b></td><td>938.90 <b>(-72.96%)</b></td><td>4.65 <b>(-97.35%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>3904.01 (n/a)</td><td>3621.29 (n/a)</td><td>3624.14 (n/a)</td><td>3472.18 (n/a)</td><td>175.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.01 <b>(+256.52%)</b></td><td>0.01 <b>(+258.93%)</b></td><td>0.01 <b>(+268.18%)</b></td><td>0.01 <b>(+245.45%)</b></td><td>0.00 <b>(+358.26%)</b></td><td>1078.25 <b>(-71.37%)</b></td><td>1018.92 <b>(-72.17%)</b></td><td>1005.17 <b>(-72.45%)</b></td><td>1000.57 <b>(-71.66%)</b></td><td>33.26 <b>(-67.44%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>3765.70 (n/a)</td><td>3661.81 (n/a)</td><td>3649.03 (n/a)</td><td>3530.29 (n/a)</td><td>102.15 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.96 <b>(+243.13%)</b></td><td>0.95 <b>(+404.52%)</b></td><td>0.95 <b>(+491.57%)</b></td><td>0.94 <b>(+520.36%)</b></td><td>0.01 <b>(-81.92%)</b></td><td>2241.83 <b>(-83.88%)</b></td><td>2216.45 <b>(-81.16%)</b></td><td>2212.95 <b>(-83.10%)</b></td><td>2185.98 <b>(-70.85%)</b></td><td>22.54 <b>(-99.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>13910.50 (n/a)</td><td>11765.58 (n/a)</td><td>13091.30 (n/a)</td><td>7499.80 (n/a)</td><td>2593.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>6.17 (+2.88%)</td><td>5.42 (+13.95%)</td><td>5.16 (+11.91%)</td><td>4.88 <b>(+29.66%)</b></td><td>0.57 <b>(-29.06%)</b></td><td>214.90 <b>(-22.86%)</b></td><td>195.14 (-13.43%)</td><td>203.30 (-10.64%)</td><td>169.90 (-2.80%)</td><td>19.86 <b>(-46.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>6.00 (n/a)</td><td>4.76 (n/a)</td><td>4.61 (n/a)</td><td>3.76 (n/a)</td><td>0.81 (n/a)</td><td>278.60 (n/a)</td><td>225.40 (n/a)</td><td>227.50 (n/a)</td><td>174.80 (n/a)</td><td>37.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.13 (-13.79%)</td><td>4.42 (-8.83%)</td><td>4.46 (-5.48%)</td><td>3.82 (-9.22%)</td><td>0.48 <b>(-28.83%)</b></td><td>274.60 (+10.15%)</td><td>239.58 (+9.16%)</td><td>235.00 (+5.76%)</td><td>204.50 (+16.00%)</td><td>25.47 (-7.84%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>5.95 (n/a)</td><td>4.84 (n/a)</td><td>4.72 (n/a)</td><td>4.21 (n/a)</td><td>0.67 (n/a)</td><td>249.30 (n/a)</td><td>219.48 (n/a)</td><td>222.20 (n/a)</td><td>176.30 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.86 (+16.84%)</td><td>5.28 (+12.49%)</td><td>5.22 (+9.67%)</td><td>4.81 (+15.79%)</td><td>0.45 <b>(+36.09%)</b></td><td>218.00 (-13.63%)</td><td>199.62 (-10.98%)</td><td>201.10 (-8.80%)</td><td>179.00 (-14.44%)</td><td>16.73 (-0.22%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>5.01 (n/a)</td><td>4.70 (n/a)</td><td>4.76 (n/a)</td><td>4.15 (n/a)</td><td>0.33 (n/a)</td><td>252.40 (n/a)</td><td>224.24 (n/a)</td><td>220.50 (n/a)</td><td>209.20 (n/a)</td><td>16.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.59 (-11.13%)</td><td>4.87 (-9.16%)</td><td>4.69 (-6.56%)</td><td>4.34 (-3.64%)</td><td>0.58 <b>(-27.35%)</b></td><td>241.70 (+3.78%)</td><td>217.56 (+9.41%)</td><td>223.50 (+7.04%)</td><td>187.60 (+12.54%)</td><td>25.05 (-12.84%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>6.29 (n/a)</td><td>5.36 (n/a)</td><td>5.02 (n/a)</td><td>4.50 (n/a)</td><td>0.79 (n/a)</td><td>232.90 (n/a)</td><td>198.84 (n/a)</td><td>208.80 (n/a)</td><td>166.70 (n/a)</td><td>28.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.74 (-14.91%)</td><td>7.07 (-10.68%)</td><td>6.90 (-12.56%)</td><td>6.25 (+4.22%)</td><td>0.65 <b>(-49.32%)</b></td><td>335.80 (-4.03%)</td><td>298.62 (+10.14%)</td><td>303.80 (+14.38%)</td><td>270.90 (+17.53%)</td><td>27.52 <b>(-43.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>9.10 (n/a)</td><td>7.92 (n/a)</td><td>7.89 (n/a)</td><td>5.99 (n/a)</td><td>1.27 (n/a)</td><td>349.90 (n/a)</td><td>271.12 (n/a)</td><td>265.60 (n/a)</td><td>230.50 (n/a)</td><td>48.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.84 (-0.78%)</td><td>7.72 (+3.14%)</td><td>7.45 (-7.61%)</td><td>6.74 (+16.90%)</td><td>0.97 <b>(-23.50%)</b></td><td>311.10 (-14.46%)</td><td>275.24 (-4.26%)</td><td>281.40 (+8.23%)</td><td>237.30 (+0.76%)</td><td>34.07 <b>(-35.13%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.91 (n/a)</td><td>7.48 (n/a)</td><td>8.07 (n/a)</td><td>5.77 (n/a)</td><td>1.27 (n/a)</td><td>363.70 (n/a)</td><td>287.48 (n/a)</td><td>260.00 (n/a)</td><td>235.50 (n/a)</td><td>52.53 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.07 (-15.08%)</td><td>7.31 (-7.92%)</td><td>7.01 (-9.32%)</td><td>6.66 (-6.84%)</td><td>0.65 <b>(-28.46%)</b></td><td>315.10 (+7.36%)</td><td>288.54 (+8.25%)</td><td>299.30 (+10.28%)</td><td>259.80 (+17.77%)</td><td>25.06 (-8.20%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>9.51 (n/a)</td><td>7.94 (n/a)</td><td>7.73 (n/a)</td><td>7.14 (n/a)</td><td>0.91 (n/a)</td><td>293.50 (n/a)</td><td>266.54 (n/a)</td><td>271.40 (n/a)</td><td>220.60 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.99 (-16.76%)</td><td>8.15 (-4.40%)</td><td>7.96 (-1.38%)</td><td>7.51 (+4.53%)</td><td>0.60 <b>(-59.52%)</b></td><td>279.10 (-4.35%)</td><td>258.38 (+2.69%)</td><td>263.60 (+1.42%)</td><td>233.40 <b>(+20.12%)</b></td><td>18.70 <b>(-53.88%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>10.79 (n/a)</td><td>8.53 (n/a)</td><td>8.07 (n/a)</td><td>7.19 (n/a)</td><td>1.49 (n/a)</td><td>291.80 (n/a)</td><td>251.60 (n/a)</td><td>259.90 (n/a)</td><td>194.30 (n/a)</td><td>40.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>9.46 (-7.99%)</td><td>8.15 (-5.67%)</td><td>8.35 (-3.96%)</td><td>6.92 (-8.61%)</td><td>0.96 (-9.50%)</td><td>303.20 (+9.42%)</td><td>260.24 (+5.99%)</td><td>251.10 (+4.15%)</td><td>221.60 (+8.68%)</td><td>30.78 (+8.32%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>10.28 (n/a)</td><td>8.64 (n/a)</td><td>8.70 (n/a)</td><td>7.57 (n/a)</td><td>1.06 (n/a)</td><td>277.10 (n/a)</td><td>245.54 (n/a)</td><td>241.10 (n/a)</td><td>203.90 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>9.12 (+1.67%)</td><td>8.58 (+5.07%)</td><td>8.65 (+2.14%)</td><td>7.72 (+12.20%)</td><td>0.60 <b>(-25.23%)</b></td><td>271.60 (-10.86%)</td><td>245.50 (-5.23%)</td><td>242.50 (-2.06%)</td><td>229.90 (-1.63%)</td><td>17.62 <b>(-36.02%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.97 (n/a)</td><td>8.16 (n/a)</td><td>8.47 (n/a)</td><td>6.88 (n/a)</td><td>0.80 (n/a)</td><td>304.70 (n/a)</td><td>259.04 (n/a)</td><td>247.60 (n/a)</td><td>233.70 (n/a)</td><td>27.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>12.52 (+12.66%)</td><td>11.62 (+9.29%)</td><td>11.72 (+8.51%)</td><td>10.32 (+6.34%)</td><td>0.96 <b>(+66.57%)</b></td><td>406.20 (-5.97%)</td><td>363.10 (-8.22%)</td><td>357.70 (-7.86%)</td><td>335.00 (-11.23%)</td><td>30.71 <b>(+37.23%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>11.11 (n/a)</td><td>10.63 (n/a)</td><td>10.80 (n/a)</td><td>9.71 (n/a)</td><td>0.57 (n/a)</td><td>432.00 (n/a)</td><td>395.60 (n/a)</td><td>388.20 (n/a)</td><td>377.40 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.38 (+10.96%)</td><td>11.16 (-1.11%)</td><td>10.64 (-8.02%)</td><td>10.11 (-1.99%)</td><td>1.32 <b>(+91.91%)</b></td><td>414.70 (+2.02%)</td><td>379.66 (+1.83%)</td><td>394.00 (+8.72%)</td><td>313.50 (-9.86%)</td><td>40.48 <b>(+73.46%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>12.06 (n/a)</td><td>11.28 (n/a)</td><td>11.57 (n/a)</td><td>10.32 (n/a)</td><td>0.69 (n/a)</td><td>406.50 (n/a)</td><td>372.82 (n/a)</td><td>362.40 (n/a)</td><td>347.80 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.14 (+3.76%)</td><td>11.52 (+2.11%)</td><td>11.92 (+6.00%)</td><td>9.70 (-0.34%)</td><td>1.32 <b>(+24.88%)</b></td><td>432.40 (+0.35%)</td><td>367.96 (-1.70%)</td><td>351.80 (-5.66%)</td><td>319.30 (-3.62%)</td><td>43.69 <b>(+20.61%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>12.66 (n/a)</td><td>11.29 (n/a)</td><td>11.25 (n/a)</td><td>9.73 (n/a)</td><td>1.05 (n/a)</td><td>430.90 (n/a)</td><td>374.34 (n/a)</td><td>372.90 (n/a)</td><td>331.30 (n/a)</td><td>36.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>15.48 (+15.97%)</td><td>13.21 (+3.57%)</td><td>13.11 (+1.01%)</td><td>11.34 (-5.42%)</td><td>1.67 <b>(+178.72%)</b></td><td>369.80 (+5.75%)</td><td>321.52 (-2.40%)</td><td>320.00 (-1.02%)</td><td>271.00 (-13.78%)</td><td>39.98 <b>(+155.05%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.35 (n/a)</td><td>12.75 (n/a)</td><td>12.97 (n/a)</td><td>11.99 (n/a)</td><td>0.60 (n/a)</td><td>349.70 (n/a)</td><td>329.44 (n/a)</td><td>323.30 (n/a)</td><td>314.30 (n/a)</td><td>15.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>14.47 (+13.03%)</td><td>12.52 (+1.92%)</td><td>11.82 (-5.14%)</td><td>11.77 (+3.43%)</td><td>1.17 <b>(+113.71%)</b></td><td>356.20 (-3.34%)</td><td>337.08 (-1.43%)</td><td>354.80 (+5.44%)</td><td>289.80 (-11.54%)</td><td>28.92 <b>(+82.24%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>12.80 (n/a)</td><td>12.29 (n/a)</td><td>12.46 (n/a)</td><td>11.38 (n/a)</td><td>0.55 (n/a)</td><td>368.50 (n/a)</td><td>341.96 (n/a)</td><td>336.50 (n/a)</td><td>327.60 (n/a)</td><td>15.87 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.66 (+2.99%)</td><td>13.14 (+7.20%)</td><td>13.38 (+10.36%)</td><td>12.28 (+11.40%)</td><td>0.58 <b>(-40.48%)</b></td><td>341.50 (-10.23%)</td><td>319.66 (-7.03%)</td><td>313.40 (-9.37%)</td><td>307.00 (-2.88%)</td><td>14.36 <b>(-47.52%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>13.27 (n/a)</td><td>12.26 (n/a)</td><td>12.13 (n/a)</td><td>11.02 (n/a)</td><td>0.97 (n/a)</td><td>380.40 (n/a)</td><td>343.84 (n/a)</td><td>345.80 (n/a)</td><td>316.10 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>15.13 (+3.85%)</td><td>12.60 (-2.02%)</td><td>12.30 (-6.15%)</td><td>11.35 (+1.18%)</td><td>1.50 (+16.14%)</td><td>369.60 (-1.15%)</td><td>336.24 (+2.28%)</td><td>341.00 (+6.53%)</td><td>277.20 (-3.68%)</td><td>36.15 (+8.53%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>14.57 (n/a)</td><td>12.86 (n/a)</td><td>13.10 (n/a)</td><td>11.22 (n/a)</td><td>1.29 (n/a)</td><td>373.90 (n/a)</td><td>328.74 (n/a)</td><td>320.10 (n/a)</td><td>287.80 (n/a)</td><td>33.31 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>14.69 (+4.21%)</td><td>12.87 (+0.07%)</td><td>14.28 (+5.13%)</td><td>8.84 (-18.09%)</td><td>2.54 <b>(+76.20%)</b></td><td>474.60 <b>(+22.10%)</b></td><td>338.60 (+2.71%)</td><td>293.70 (-4.89%)</td><td>285.50 (-4.03%)</td><td>81.17 <b>(+105.53%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>14.10 (n/a)</td><td>12.86 (n/a)</td><td>13.58 (n/a)</td><td>10.79 (n/a)</td><td>1.44 (n/a)</td><td>388.70 (n/a)</td><td>329.66 (n/a)</td><td>308.80 (n/a)</td><td>297.50 (n/a)</td><td>39.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.92 <b>(+22.03%)</b></td><td>2.78 (+4.90%)</td><td>2.53 (-2.90%)</td><td>2.02 (-12.61%)</td><td>0.73 <b>(+109.89%)</b></td><td>259.40 (+14.42%)</td><td>198.52 (-1.05%)</td><td>207.20 (+2.98%)</td><td>133.70 (-18.03%)</td><td>47.10 <b>(+95.31%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.21 (n/a)</td><td>2.65 (n/a)</td><td>2.61 (n/a)</td><td>2.31 (n/a)</td><td>0.35 (n/a)</td><td>226.70 (n/a)</td><td>200.62 (n/a)</td><td>201.20 (n/a)</td><td>163.10 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.24 (-6.19%)</td><td>4.59 (-5.06%)</td><td>4.86 (+2.60%)</td><td>3.41 (-6.91%)</td><td>0.71 (-7.88%)</td><td>307.50 (+7.40%)</td><td>233.68 (+5.34%)</td><td>215.80 (-2.53%)</td><td>200.20 (+6.60%)</td><td>42.97 (+8.52%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>5.58 (n/a)</td><td>4.84 (n/a)</td><td>4.74 (n/a)</td><td>3.66 (n/a)</td><td>0.77 (n/a)</td><td>286.30 (n/a)</td><td>221.84 (n/a)</td><td>221.40 (n/a)</td><td>187.80 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>9.30 (+4.87%)</td><td>7.65 (-4.08%)</td><td>7.26 (-10.15%)</td><td>6.96 (-4.10%)</td><td>0.95 <b>(+44.68%)</b></td><td>301.50 (+4.29%)</td><td>277.26 (+4.84%)</td><td>288.90 (+11.33%)</td><td>225.50 (-4.65%)</td><td>30.39 <b>(+40.17%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>8.87 (n/a)</td><td>7.97 (n/a)</td><td>8.08 (n/a)</td><td>7.25 (n/a)</td><td>0.66 (n/a)</td><td>289.10 (n/a)</td><td>264.46 (n/a)</td><td>259.50 (n/a)</td><td>236.50 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.52 (+1.88%)</td><td>3.08 (+10.22%)</td><td>3.13 (+9.56%)</td><td>2.65 <b>(+20.72%)</b></td><td>0.38 (-18.71%)</td><td>198.10 (-17.18%)</td><td>172.02 (-10.19%)</td><td>167.30 (-8.73%)</td><td>148.80 (-1.85%)</td><td>21.24 <b>(-33.91%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>3.46 (n/a)</td><td>2.80 (n/a)</td><td>2.86 (n/a)</td><td>2.19 (n/a)</td><td>0.46 (n/a)</td><td>239.20 (n/a)</td><td>191.54 (n/a)</td><td>183.30 (n/a)</td><td>151.60 (n/a)</td><td>32.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (-16.07%)</td><td>0.18 (-10.80%)</td><td>0.17 (-11.13%)</td><td>0.13 <b>(-22.39%)</b></td><td>0.04 (-3.58%)</td><td>247.60 <b>(+28.82%)</b></td><td>185.72 (+13.12%)</td><td>188.10 (+12.50%)</td><td>149.20 (+19.07%)</td><td>40.20 <b>(+42.09%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>192.20 (n/a)</td><td>164.18 (n/a)</td><td>167.20 (n/a)</td><td>125.30 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (-10.26%)</td><td>0.20 (-17.37%)</td><td>0.19 <b>(-22.45%)</b></td><td>0.15 <b>(-24.26%)</b></td><td>0.04 (+1.03%)</td><td>213.50 <b>(+32.03%)</b></td><td>168.40 <b>(+22.15%)</b></td><td>172.20 <b>(+28.99%)</b></td><td>126.10 (+11.40%)</td><td>32.89 <b>(+43.72%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>161.70 (n/a)</td><td>137.86 (n/a)</td><td>133.50 (n/a)</td><td>113.20 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.48 (+5.39%)</td><td>0.39 (-0.26%)</td><td>0.42 (-4.15%)</td><td>0.21 <b>(-28.33%)</b></td><td>0.11 <b>(+44.81%)</b></td><td>311.50 <b>(+39.50%)</b></td><td>185.26 (+6.15%)</td><td>156.40 (+4.34%)</td><td>137.90 (-5.16%)</td><td>72.59 <b>(+98.12%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>223.30 (n/a)</td><td>174.52 (n/a)</td><td>149.90 (n/a)</td><td>145.40 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.59 <b>(+42.97%)</b></td><td>0.47 <b>(+27.67%)</b></td><td>0.42 (+8.64%)</td><td>0.41 <b>(+36.25%)</b></td><td>0.08 <b>(+61.47%)</b></td><td>161.50 <b>(-26.62%)</b></td><td>143.24 <b>(-21.23%)</b></td><td>156.50 (-7.94%)</td><td>111.90 <b>(-30.06%)</b></td><td>22.26 (-15.01%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>220.10 (n/a)</td><td>181.84 (n/a)</td><td>170.00 (n/a)</td><td>160.00 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.48 (+11.18%)</td><td>0.39 (+5.09%)</td><td>0.38 (-2.74%)</td><td>0.30 (-4.27%)</td><td>0.06 <b>(+40.75%)</b></td><td>216.80 (+4.48%)</td><td>169.86 (-3.84%)</td><td>170.60 (+2.83%)</td><td>137.20 (-10.09%)</td><td>29.78 <b>(+32.94%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>207.50 (n/a)</td><td>176.64 (n/a)</td><td>165.90 (n/a)</td><td>152.60 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.93 (-16.64%)</td><td>0.85 (+9.60%)</td><td>0.84 (+17.10%)</td><td>0.79 <b>(+35.44%)</b></td><td>0.05 <b>(-76.10%)</b></td><td>165.40 <b>(-26.19%)</b></td><td>153.96 (-13.33%)</td><td>156.10 (-14.56%)</td><td>140.40 (+19.90%)</td><td>9.06 <b>(-78.92%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>1.12 (n/a)</td><td>0.78 (n/a)</td><td>0.72 (n/a)</td><td>0.58 (n/a)</td><td>0.22 (n/a)</td><td>224.10 (n/a)</td><td>177.64 (n/a)</td><td>182.70 (n/a)</td><td>117.10 (n/a)</td><td>43.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.84 (+11.44%)</td><td>0.71 (+6.89%)</td><td>0.72 (+2.72%)</td><td>0.56 <b>(+22.69%)</b></td><td>0.10 (-13.34%)</td><td>235.60 (-18.48%)</td><td>189.00 (-7.87%)</td><td>182.50 (-2.61%)</td><td>155.90 (-10.25%)</td><td>29.39 <b>(-37.95%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.75 (n/a)</td><td>0.66 (n/a)</td><td>0.70 (n/a)</td><td>0.45 (n/a)</td><td>0.12 (n/a)</td><td>289.00 (n/a)</td><td>205.14 (n/a)</td><td>187.40 (n/a)</td><td>173.70 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.92 (+13.31%)</td><td>0.79 (+4.98%)</td><td>0.77 (-2.51%)</td><td>0.71 (+13.72%)</td><td>0.08 (+1.07%)</td><td>184.90 (-12.08%)</td><td>167.28 (-4.95%)</td><td>170.80 (+2.58%)</td><td>141.90 (-11.75%)</td><td>15.74 <b>(-23.40%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.82 (n/a)</td><td>0.75 (n/a)</td><td>0.79 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>210.30 (n/a)</td><td>176.00 (n/a)</td><td>166.50 (n/a)</td><td>160.80 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.91 (-5.87%)</td><td>0.64 (-15.80%)</td><td>0.61 <b>(-23.14%)</b></td><td>0.39 <b>(-25.74%)</b></td><td>0.20 <b>(+21.16%)</b></td><td>334.80 <b>(+34.67%)</b></td><td>223.10 <b>(+23.61%)</b></td><td>216.20 <b>(+30.08%)</b></td><td>144.30 (+6.18%)</td><td>72.93 <b>(+70.12%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.96 (n/a)</td><td>0.76 (n/a)</td><td>0.79 (n/a)</td><td>0.53 (n/a)</td><td>0.16 (n/a)</td><td>248.60 (n/a)</td><td>180.48 (n/a)</td><td>166.20 (n/a)</td><td>135.90 (n/a)</td><td>42.87 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (+2.23%)</td><td>0.10 (+4.46%)</td><td>0.11 (+7.90%)</td><td>0.08 (+8.49%)</td><td>0.02 (-1.12%)</td><td>211.90 (-7.79%)</td><td>167.92 (-4.67%)</td><td>149.10 (-7.33%)</td><td>128.20 (-2.21%)</td><td>38.15 (-9.08%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:17:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.80 (n/a)</td><td>176.14 (n/a)</td><td>160.90 (n/a)</td><td>131.10 (n/a)</td><td>41.96 (n/a)</td>
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
