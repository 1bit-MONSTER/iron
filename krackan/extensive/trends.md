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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (+4.33%)</td><td>0.04 (+15.92%)</td><td>0.05 <b>(+24.05%)</b></td><td>0.04 (+15.63%)</td><td>0.01 (-9.25%)</td><td>174.10 (-13.51%)</td><td>139.80 (-14.22%)</td><td>131.60 (-19.41%)</td><td>129.30 (-4.15%)</td><td>19.24 <b>(-24.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>162.98 (n/a)</td><td>163.30 (n/a)</td><td>134.90 (n/a)</td><td>25.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-11.17%)</td><td>0.04 (+3.39%)</td><td>0.04 (+8.93%)</td><td>0.03 (+11.98%)</td><td>0.01 <b>(-33.64%)</b></td><td>198.60 (-10.70%)</td><td>152.96 (-6.75%)</td><td>140.50 (-8.17%)</td><td>127.20 (+12.57%)</td><td>30.39 <b>(-35.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>164.04 (n/a)</td><td>153.00 (n/a)</td><td>113.00 (n/a)</td><td>46.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-9.34%)</td><td>0.04 (-6.31%)</td><td>0.04 (-8.05%)</td><td>0.03 (-9.85%)</td><td>0.01 (-8.30%)</td><td>208.80 (+10.95%)</td><td>169.46 (+6.85%)</td><td>175.20 (+8.75%)</td><td>130.80 (+10.29%)</td><td>29.47 (+14.21%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>158.60 (n/a)</td><td>161.10 (n/a)</td><td>118.60 (n/a)</td><td>25.80 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (+0.10%)</td><td>0.04 (+4.83%)</td><td>0.05 (+16.43%)</td><td>0.03 (-1.13%)</td><td>0.01 (+6.95%)</td><td>188.60 (+1.13%)</td><td>147.74 (-4.29%)</td><td>131.80 (-14.08%)</td><td>123.50 (-0.16%)</td><td>28.60 (+7.35%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>154.36 (n/a)</td><td>153.40 (n/a)</td><td>123.70 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 <b>(-23.15%)</b></td><td>0.03 (-19.14%)</td><td>0.03 <b>(-24.80%)</b></td><td>0.03 (-13.54%)</td><td>0.01 <b>(-51.06%)</b></td><td>244.90 (+15.68%)</td><td>189.72 (+19.19%)</td><td>180.70 <b>(+33.06%)</b></td><td>156.40 <b>(+30.12%)</b></td><td>33.20 <b>(-25.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>159.18 (n/a)</td><td>135.80 (n/a)</td><td>120.20 (n/a)</td><td>44.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 <b>(+43.11%)</b></td><td>0.05 <b>(+36.24%)</b></td><td>0.05 <b>(+39.17%)</b></td><td>0.03 (+16.64%)</td><td>0.01 <b>(+83.29%)</b></td><td>223.20 (-14.29%)</td><td>145.98 <b>(-24.12%)</b></td><td>131.80 <b>(-28.17%)</b></td><td>103.70 <b>(-30.12%)</b></td><td>46.43 (+10.84%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>260.40 (n/a)</td><td>192.38 (n/a)</td><td>183.50 (n/a)</td><td>148.40 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+5.80%)</td><td>0.03 (+12.99%)</td><td>0.04 (+15.34%)</td><td>0.03 (+18.89%)</td><td>0.01 (-6.61%)</td><td>210.80 (-15.92%)</td><td>180.18 (-12.15%)</td><td>168.20 (-13.30%)</td><td>149.40 (-5.44%)</td><td>27.72 <b>(-24.18%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.70 (n/a)</td><td>205.10 (n/a)</td><td>194.00 (n/a)</td><td>158.00 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+12.43%)</td><td>0.04 (+2.76%)</td><td>0.03 (+0.03%)</td><td>0.03 (-2.50%)</td><td>0.01 <b>(+62.83%)</b></td><td>208.90 (+2.60%)</td><td>174.70 (-1.79%)</td><td>176.50 (+0.00%)</td><td>141.10 (-11.09%)</td><td>24.43 <b>(+46.51%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>177.88 (n/a)</td><td>176.50 (n/a)</td><td>158.70 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (+7.33%)</td><td>0.08 (+6.51%)</td><td>0.09 <b>(+23.44%)</b></td><td>0.06 (-11.04%)</td><td>0.02 <b>(+75.82%)</b></td><td>208.40 (+12.41%)</td><td>158.92 (-3.14%)</td><td>140.10 (-19.02%)</td><td>123.40 (-6.87%)</td><td>38.74 <b>(+88.55%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>164.08 (n/a)</td><td>173.00 (n/a)</td><td>132.50 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (+12.71%)</td><td>0.08 (+17.38%)</td><td>0.08 (+9.24%)</td><td>0.07 <b>(+39.30%)</b></td><td>0.01 <b>(-29.83%)</b></td><td>172.80 <b>(-28.21%)</b></td><td>159.74 (-15.89%)</td><td>163.70 (-8.45%)</td><td>145.10 (-11.25%)</td><td>13.45 <b>(-56.28%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>189.92 (n/a)</td><td>178.80 (n/a)</td><td>163.50 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (-13.47%)</td><td>0.08 (-2.01%)</td><td>0.08 (+12.57%)</td><td>0.06 (+2.58%)</td><td>0.01 <b>(-44.52%)</b></td><td>189.80 (-2.47%)</td><td>157.88 (-0.50%)</td><td>155.50 (-11.19%)</td><td>131.40 (+15.57%)</td><td>21.17 <b>(-36.49%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>194.60 (n/a)</td><td>158.68 (n/a)</td><td>175.10 (n/a)</td><td>113.70 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (+13.47%)</td><td>0.09 (+8.45%)</td><td>0.09 (+9.52%)</td><td>0.07 <b>(+34.67%)</b></td><td>0.01 (-15.66%)</td><td>169.20 <b>(-25.72%)</b></td><td>146.36 (-9.70%)</td><td>144.20 (-8.73%)</td><td>115.50 (-11.90%)</td><td>22.10 <b>(-43.89%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.80 (n/a)</td><td>162.08 (n/a)</td><td>158.00 (n/a)</td><td>131.10 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 <b>(+42.03%)</b></td><td>0.08 <b>(+45.98%)</b></td><td>0.08 <b>(+39.46%)</b></td><td>0.06 <b>(+65.36%)</b></td><td>0.01 (+3.07%)</td><td>221.50 <b>(-39.53%)</b></td><td>163.08 <b>(-33.75%)</b></td><td>155.70 <b>(-28.28%)</b></td><td>129.40 <b>(-29.56%)</b></td><td>34.62 <b>(-54.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>366.30 (n/a)</td><td>246.14 (n/a)</td><td>217.10 (n/a)</td><td>183.70 (n/a)</td><td>75.46 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (-16.57%)</td><td>0.07 (-14.56%)</td><td>0.07 (-15.58%)</td><td>0.06 (-0.93%)</td><td>0.01 <b>(-41.66%)</b></td><td>217.80 (+0.93%)</td><td>184.58 (+15.15%)</td><td>183.90 (+18.49%)</td><td>159.90 (+19.87%)</td><td>22.20 <b>(-31.47%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>160.30 (n/a)</td><td>155.20 (n/a)</td><td>133.40 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (+6.67%)</td><td>0.07 (+7.68%)</td><td>0.07 (+13.01%)</td><td>0.06 (+16.95%)</td><td>0.01 (-12.91%)</td><td>210.10 (-14.49%)</td><td>184.76 (-7.68%)</td><td>177.50 (-11.52%)</td><td>160.50 (-6.25%)</td><td>20.53 <b>(-29.50%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>245.70 (n/a)</td><td>200.14 (n/a)</td><td>200.60 (n/a)</td><td>171.20 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 <b>(+40.06%)</b></td><td>0.08 <b>(+34.46%)</b></td><td>0.08 <b>(+44.74%)</b></td><td>0.06 <b>(+20.29%)</b></td><td>0.01 <b>(+96.16%)</b></td><td>189.30 (-16.86%)</td><td>157.86 <b>(-24.78%)</b></td><td>153.20 <b>(-30.93%)</b></td><td>130.80 <b>(-28.60%)</b></td><td>25.45 (+16.13%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>209.86 (n/a)</td><td>221.80 (n/a)</td><td>183.20 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (+5.17%)</td><td>0.14 (+10.00%)</td><td>0.14 (+16.67%)</td><td>0.12 (+9.92%)</td><td>0.03 (-3.62%)</td><td>209.50 (-9.03%)</td><td>174.12 (-9.61%)</td><td>169.70 (-14.29%)</td><td>131.10 (-4.93%)</td><td>29.66 (-15.23%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>230.30 (n/a)</td><td>192.64 (n/a)</td><td>198.00 (n/a)</td><td>137.90 (n/a)</td><td>34.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 <b>(+49.08%)</b></td><td>0.16 <b>(+22.58%)</b></td><td>0.16 (+8.22%)</td><td>0.13 <b>(+24.54%)</b></td><td>0.03 <b>(+77.93%)</b></td><td>191.00 (-19.68%)</td><td>154.74 (-17.43%)</td><td>157.40 (-7.63%)</td><td>111.70 <b>(-32.91%)</b></td><td>28.72 (-6.22%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>237.80 (n/a)</td><td>187.40 (n/a)</td><td>170.40 (n/a)</td><td>166.50 (n/a)</td><td>30.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 <b>(-30.85%)</b></td><td>0.14 (-7.29%)</td><td>0.15 (+7.61%)</td><td>0.10 (-19.40%)</td><td>0.03 <b>(-39.54%)</b></td><td>258.00 <b>(+24.10%)</b></td><td>178.72 (+6.36%)</td><td>162.50 (-7.09%)</td><td>153.10 <b>(+44.57%)</b></td><td>44.55 (+18.87%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>207.90 (n/a)</td><td>168.04 (n/a)</td><td>174.90 (n/a)</td><td>105.90 (n/a)</td><td>37.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 <b>(+33.05%)</b></td><td>0.14 (+3.78%)</td><td>0.13 (-5.80%)</td><td>0.11 (-9.00%)</td><td>0.03 <b>(+167.06%)</b></td><td>230.00 (+9.89%)</td><td>186.46 (-0.67%)</td><td>194.60 (+6.16%)</td><td>128.60 <b>(-24.80%)</b></td><td>36.85 <b>(+111.43%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>187.72 (n/a)</td><td>183.30 (n/a)</td><td>171.00 (n/a)</td><td>17.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (-11.20%)</td><td>0.15 (+3.26%)</td><td>0.16 <b>(+21.18%)</b></td><td>0.12 (-4.25%)</td><td>0.02 <b>(-27.07%)</b></td><td>203.50 (+4.41%)</td><td>168.76 (-3.92%)</td><td>156.90 (-17.51%)</td><td>148.50 (+12.67%)</td><td>22.81 (-13.63%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.90 (n/a)</td><td>175.64 (n/a)</td><td>190.20 (n/a)</td><td>131.80 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (+1.23%)</td><td>0.16 <b>(+26.32%)</b></td><td>0.16 <b>(+45.81%)</b></td><td>0.13 <b>(+56.07%)</b></td><td>0.02 <b>(-43.00%)</b></td><td>193.90 <b>(-35.92%)</b></td><td>157.28 <b>(-25.39%)</b></td><td>149.30 <b>(-31.45%)</b></td><td>130.80 (-1.21%)</td><td>23.68 <b>(-62.87%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>302.60 (n/a)</td><td>210.80 (n/a)</td><td>217.80 (n/a)</td><td>132.40 (n/a)</td><td>63.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 <b>(-24.48%)</b></td><td>0.12 (-18.68%)</td><td>0.11 <b>(-27.23%)</b></td><td>0.10 (+8.88%)</td><td>0.03 <b>(-42.38%)</b></td><td>255.10 (-8.14%)</td><td>210.54 (+16.23%)</td><td>221.50 <b>(+37.41%)</b></td><td>142.00 <b>(+32.46%)</b></td><td>41.89 <b>(-33.58%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>277.70 (n/a)</td><td>181.14 (n/a)</td><td>161.20 (n/a)</td><td>107.20 (n/a)</td><td>63.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 <b>(-33.12%)</b></td><td>0.14 (-15.81%)</td><td>0.14 (-12.09%)</td><td>0.12 (-1.24%)</td><td>0.01 <b>(-64.77%)</b></td><td>203.60 (+1.24%)</td><td>178.74 (+14.81%)</td><td>181.90 (+13.76%)</td><td>159.80 <b>(+49.49%)</b></td><td>18.34 <b>(-45.88%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>201.10 (n/a)</td><td>155.68 (n/a)</td><td>159.90 (n/a)</td><td>106.90 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.39 (+11.89%)</td><td>0.34 (+10.39%)</td><td>0.38 (+18.51%)</td><td>0.28 (-2.49%)</td><td>0.05 <b>(+83.56%)</b></td><td>178.50 (+2.53%)</td><td>146.16 (-8.13%)</td><td>131.10 (-15.58%)</td><td>124.80 (-10.60%)</td><td>24.24 <b>(+65.28%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>174.10 (n/a)</td><td>159.10 (n/a)</td><td>155.30 (n/a)</td><td>139.60 (n/a)</td><td>14.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.33 (-6.94%)</td><td>0.28 (-2.37%)</td><td>0.27 (+2.87%)</td><td>0.23 (+2.73%)</td><td>0.04 (-16.00%)</td><td>209.90 (-2.64%)</td><td>179.58 (+1.85%)</td><td>178.90 (-2.82%)</td><td>147.70 (+7.50%)</td><td>26.48 (-10.66%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>215.60 (n/a)</td><td>176.32 (n/a)</td><td>184.10 (n/a)</td><td>137.40 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.38 (+9.79%)</td><td>0.30 (+0.61%)</td><td>0.28 (-5.48%)</td><td>0.25 (-1.43%)</td><td>0.05 <b>(+51.72%)</b></td><td>194.20 (+1.46%)</td><td>167.40 (+0.47%)</td><td>177.80 (+5.77%)</td><td>130.00 (-8.90%)</td><td>25.52 <b>(+39.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>191.40 (n/a)</td><td>166.62 (n/a)</td><td>168.10 (n/a)</td><td>142.70 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.39 <b>(+21.29%)</b></td><td>0.33 <b>(+22.11%)</b></td><td>0.38 <b>(+39.52%)</b></td><td>0.21 (-7.06%)</td><td>0.07 <b>(+126.80%)</b></td><td>233.40 (+7.61%)</td><td>156.26 (-14.69%)</td><td>130.70 <b>(-28.30%)</b></td><td>126.90 (-17.60%)</td><td>45.10 <b>(+101.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>216.90 (n/a)</td><td>183.16 (n/a)</td><td>182.30 (n/a)</td><td>154.00 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.40 (-5.60%)</td><td>0.32 (+1.42%)</td><td>0.31 (+9.89%)</td><td>0.27 (+2.88%)</td><td>0.05 <b>(-21.38%)</b></td><td>179.00 (-2.82%)</td><td>157.84 (-2.38%)</td><td>158.20 (-9.03%)</td><td>122.50 (+5.88%)</td><td>22.42 (-17.23%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>184.20 (n/a)</td><td>161.68 (n/a)</td><td>173.90 (n/a)</td><td>115.70 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.39 (-1.52%)</td><td>0.32 (+17.45%)</td><td>0.33 (+17.45%)</td><td>0.27 <b>(+57.04%)</b></td><td>0.04 <b>(-50.67%)</b></td><td>180.20 <b>(-36.33%)</b></td><td>154.76 <b>(-20.84%)</b></td><td>148.70 (-14.88%)</td><td>127.50 (+1.51%)</td><td>20.38 <b>(-68.58%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>283.00 (n/a)</td><td>195.50 (n/a)</td><td>174.70 (n/a)</td><td>125.60 (n/a)</td><td>64.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.38 (-0.80%)</td><td>0.30 (-2.61%)</td><td>0.28 (-1.13%)</td><td>0.26 (+19.10%)</td><td>0.05 <b>(-28.75%)</b></td><td>188.90 (-16.04%)</td><td>168.98 (+0.27%)</td><td>178.00 (+1.14%)</td><td>128.70 (+0.86%)</td><td>23.40 <b>(-40.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>225.00 (n/a)</td><td>168.52 (n/a)</td><td>176.00 (n/a)</td><td>127.60 (n/a)</td><td>39.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (-14.35%)</td><td>0.27 (+7.36%)</td><td>0.27 (+3.87%)</td><td>0.23 <b>(+51.50%)</b></td><td>0.04 <b>(-54.75%)</b></td><td>210.70 <b>(-34.01%)</b></td><td>183.80 (-14.41%)</td><td>184.00 (-3.72%)</td><td>156.70 (+16.77%)</td><td>26.46 <b>(-65.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>319.30 (n/a)</td><td>214.74 (n/a)</td><td>191.10 (n/a)</td><td>134.20 (n/a)</td><td>77.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (-8.38%)</td><td>0.02 (+0.76%)</td><td>0.02 (-3.64%)</td><td>0.01 (-1.72%)</td><td>0.00 (-18.74%)</td><td>233.50 (+1.79%)</td><td>164.78 (-1.95%)</td><td>153.80 (+3.78%)</td><td>132.00 (+9.09%)</td><td>39.93 (-7.48%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>229.40 (n/a)</td><td>168.06 (n/a)</td><td>148.20 (n/a)</td><td>121.00 (n/a)</td><td>43.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (-2.72%)</td><td>0.02 (+12.28%)</td><td>0.02 (+1.95%)</td><td>0.01 <b>(+25.69%)</b></td><td>0.00 <b>(-23.91%)</b></td><td>182.90 <b>(-20.44%)</b></td><td>150.88 (-14.33%)</td><td>165.00 (-1.90%)</td><td>106.20 (+2.81%)</td><td>30.86 <b>(-37.11%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>176.12 (n/a)</td><td>168.20 (n/a)</td><td>103.30 (n/a)</td><td>49.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 <b>(-23.24%)</b></td><td>0.02 (-13.69%)</td><td>0.01 (-6.89%)</td><td>0.01 (-11.69%)</td><td>0.00 <b>(-36.69%)</b></td><td>213.20 (+13.22%)</td><td>168.62 (+13.23%)</td><td>175.00 (+7.43%)</td><td>135.30 <b>(+30.22%)</b></td><td>33.34 (-9.58%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>148.92 (n/a)</td><td>162.90 (n/a)</td><td>103.90 (n/a)</td><td>36.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (+3.21%)</td><td>0.02 (-10.28%)</td><td>0.01 (-17.75%)</td><td>0.01 (+0.69%)</td><td>0.00 (+4.12%)</td><td>212.70 (-0.65%)</td><td>177.12 (+11.52%)</td><td>184.20 <b>(+21.58%)</b></td><td>109.10 (-3.11%)</td><td>41.12 (-3.25%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>158.82 (n/a)</td><td>151.50 (n/a)</td><td>112.60 (n/a)</td><td>42.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (-12.18%)</td><td>0.02 (-0.72%)</td><td>0.02 (-16.33%)</td><td>0.01 <b>(+78.88%)</b></td><td>0.00 <b>(-61.60%)</b></td><td>207.20 <b>(-44.09%)</b></td><td>166.52 (-13.44%)</td><td>159.80 (+19.52%)</td><td>143.40 (+13.90%)</td><td>25.99 <b>(-75.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>370.60 (n/a)</td><td>192.38 (n/a)</td><td>133.70 (n/a)</td><td>125.90 (n/a)</td><td>104.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (+17.79%)</td><td>0.02 (-0.56%)</td><td>0.01 (-2.97%)</td><td>0.01 (-17.20%)</td><td>0.00 <b>(+139.69%)</b></td><td>208.60 <b>(+20.79%)</b></td><td>169.68 (+4.94%)</td><td>176.20 (+3.04%)</td><td>114.40 (-15.13%)</td><td>40.38 <b>(+151.05%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.70 (n/a)</td><td>161.70 (n/a)</td><td>171.00 (n/a)</td><td>134.80 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.01 <b>(-34.97%)</b></td><td>0.01 (-12.15%)</td><td>0.01 (-3.73%)</td><td>0.01 (-0.37%)</td><td>0.00 <b>(-80.34%)</b></td><td>208.20 (+0.34%)</td><td>196.20 (+9.52%)</td><td>198.50 (+3.87%)</td><td>182.60 <b>(+53.83%)</b></td><td>11.08 <b>(-68.81%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>207.50 (n/a)</td><td>179.14 (n/a)</td><td>191.10 (n/a)</td><td>118.70 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.01 (-17.23%)</td><td>0.01 (-11.72%)</td><td>0.01 (-1.46%)</td><td>0.01 <b>(-37.18%)</b></td><td>0.00 (+16.87%)</td><td>372.00 <b>(+59.18%)</b></td><td>238.70 (+17.66%)</td><td>207.10 (+1.47%)</td><td>186.30 <b>(+20.82%)</b></td><td>75.57 <b>(+139.06%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.70 (n/a)</td><td>202.88 (n/a)</td><td>204.10 (n/a)</td><td>154.20 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-17.39%)</td><td>0.03 (-8.19%)</td><td>0.03 (-1.75%)</td><td>0.02 (-5.16%)</td><td>0.00 <b>(-35.93%)</b></td><td>230.40 (+5.45%)</td><td>188.18 (+7.89%)</td><td>178.00 (+1.77%)</td><td>172.60 <b>(+21.04%)</b></td><td>23.83 (-17.01%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.50 (n/a)</td><td>174.42 (n/a)</td><td>174.90 (n/a)</td><td>142.60 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-5.70%)</td><td>0.03 (-2.15%)</td><td>0.03 (+4.22%)</td><td>0.02 (-13.99%)</td><td>0.00 (+7.52%)</td><td>243.30 (+16.24%)</td><td>190.26 (+2.75%)</td><td>180.40 (-4.04%)</td><td>166.90 (+6.04%)</td><td>30.24 <b>(+36.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>185.16 (n/a)</td><td>188.00 (n/a)</td><td>157.40 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+19.17%)</td><td>0.03 (+9.59%)</td><td>0.03 (-6.01%)</td><td>0.02 <b>(+48.16%)</b></td><td>0.00 (-18.72%)</td><td>210.70 <b>(-32.49%)</b></td><td>184.16 (-11.44%)</td><td>197.00 (+6.37%)</td><td>146.70 (-16.08%)</td><td>25.82 <b>(-55.78%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>312.10 (n/a)</td><td>207.94 (n/a)</td><td>185.20 (n/a)</td><td>174.80 (n/a)</td><td>58.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+5.39%)</td><td>0.03 (-3.02%)</td><td>0.03 (-4.95%)</td><td>0.02 (-4.32%)</td><td>0.00 <b>(+26.58%)</b></td><td>235.60 (+4.53%)</td><td>194.06 (+3.84%)</td><td>196.60 (+5.19%)</td><td>154.40 (-5.16%)</td><td>30.23 <b>(+24.29%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.40 (n/a)</td><td>186.88 (n/a)</td><td>186.90 (n/a)</td><td>162.80 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+8.37%)</td><td>0.03 (+19.67%)</td><td>0.03 (+17.14%)</td><td>0.03 <b>(+74.64%)</b></td><td>0.01 <b>(-30.65%)</b></td><td>204.30 <b>(-42.74%)</b></td><td>176.12 <b>(-21.25%)</b></td><td>174.00 (-14.66%)</td><td>140.40 (-7.69%)</td><td>28.21 <b>(-64.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>356.80 (n/a)</td><td>223.64 (n/a)</td><td>203.90 (n/a)</td><td>152.10 (n/a)</td><td>78.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(-23.26%)</b></td><td>0.02 (-15.96%)</td><td>0.02 (-14.45%)</td><td>0.02 (-15.29%)</td><td>0.00 <b>(-33.34%)</b></td><td>298.80 (+18.06%)</td><td>236.58 (+17.77%)</td><td>236.20 (+16.87%)</td><td>193.20 <b>(+30.28%)</b></td><td>41.26 (+3.18%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.10 (n/a)</td><td>200.88 (n/a)</td><td>202.10 (n/a)</td><td>148.30 (n/a)</td><td>39.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (-14.55%)</td><td>0.02 <b>(-22.15%)</b></td><td>0.02 <b>(-23.02%)</b></td><td>0.02 <b>(-36.21%)</b></td><td>0.01 (+8.08%)</td><td>346.20 <b>(+56.79%)</b></td><td>229.90 <b>(+33.38%)</b></td><td>222.50 <b>(+29.89%)</b></td><td>149.50 (+17.07%)</td><td>71.91 <b>(+103.51%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>172.36 (n/a)</td><td>171.30 (n/a)</td><td>127.70 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 <b>(-25.03%)</b></td><td>0.02 (-16.67%)</td><td>0.02 (-7.70%)</td><td>0.02 <b>(-24.72%)</b></td><td>0.00 <b>(-22.53%)</b></td><td>313.00 <b>(+32.85%)</b></td><td>248.82 <b>(+20.19%)</b></td><td>230.80 (+8.31%)</td><td>220.90 <b>(+33.39%)</b></td><td>37.24 <b>(+43.75%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.60 (n/a)</td><td>207.02 (n/a)</td><td>213.10 (n/a)</td><td>165.60 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (+1.77%)</td><td>0.06 (-7.43%)</td><td>0.06 (-4.01%)</td><td>0.04 (-8.46%)</td><td>0.01 (+2.70%)</td><td>235.40 (+9.23%)</td><td>178.14 (+8.46%)</td><td>174.50 (+4.18%)</td><td>129.30 (-1.75%)</td><td>37.73 (+11.89%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>164.24 (n/a)</td><td>167.50 (n/a)</td><td>131.60 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (-9.79%)</td><td>0.06 (-14.40%)</td><td>0.06 (-16.85%)</td><td>0.05 (-5.93%)</td><td>0.01 (-11.25%)</td><td>202.90 (+6.29%)</td><td>179.04 (+16.68%)</td><td>178.90 <b>(+20.31%)</b></td><td>145.90 (+10.87%)</td><td>23.70 (+3.84%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>153.44 (n/a)</td><td>148.70 (n/a)</td><td>131.60 (n/a)</td><td>22.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (+0.23%)</td><td>0.06 (-10.59%)</td><td>0.06 (-18.10%)</td><td>0.05 (-9.23%)</td><td>0.01 (+4.52%)</td><td>202.70 (+10.16%)</td><td>172.06 (+12.24%)</td><td>183.50 <b>(+22.09%)</b></td><td>121.90 (-0.25%)</td><td>30.88 (+9.44%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>153.30 (n/a)</td><td>150.30 (n/a)</td><td>122.20 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (+0.56%)</td><td>0.06 (-0.88%)</td><td>0.06 (-2.64%)</td><td>0.05 (-0.25%)</td><td>0.01 (-7.14%)</td><td>217.90 (+0.28%)</td><td>172.96 (+0.05%)</td><td>170.70 (+2.71%)</td><td>121.80 (-0.57%)</td><td>35.29 (-12.03%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>172.88 (n/a)</td><td>166.20 (n/a)</td><td>122.50 (n/a)</td><td>40.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 <b>(-20.59%)</b></td><td>0.06 (-11.91%)</td><td>0.06 (-7.19%)</td><td>0.05 (-12.80%)</td><td>0.01 <b>(-37.49%)</b></td><td>213.00 (+14.70%)</td><td>176.74 (+12.37%)</td><td>177.20 (+7.79%)</td><td>146.80 <b>(+26.01%)</b></td><td>24.23 (-6.63%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>185.70 (n/a)</td><td>157.28 (n/a)</td><td>164.40 (n/a)</td><td>116.50 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 <b>(-30.51%)</b></td><td>0.05 (-14.67%)</td><td>0.05 (-9.66%)</td><td>0.05 (-0.90%)</td><td>0.00 <b>(-68.77%)</b></td><td>229.20 (+0.88%)</td><td>198.76 (+12.48%)</td><td>197.50 (+10.64%)</td><td>178.40 <b>(+43.87%)</b></td><td>19.17 <b>(-54.18%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>176.70 (n/a)</td><td>178.50 (n/a)</td><td>124.00 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (+0.39%)</td><td>0.07 (-0.94%)</td><td>0.07 (-7.19%)</td><td>0.05 (-14.13%)</td><td>0.02 <b>(+43.84%)</b></td><td>216.60 (+16.45%)</td><td>161.60 (+4.07%)</td><td>160.20 (+7.73%)</td><td>119.40 (-0.42%)</td><td>42.30 <b>(+59.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>155.28 (n/a)</td><td>148.70 (n/a)</td><td>119.90 (n/a)</td><td>26.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (+3.04%)</td><td>0.06 (-1.91%)</td><td>0.06 (+0.95%)</td><td>0.04 (-17.54%)</td><td>0.01 <b>(+61.80%)</b></td><td>271.80 <b>(+21.29%)</b></td><td>194.42 (+5.87%)</td><td>185.20 (-0.96%)</td><td>145.40 (-3.00%)</td><td>53.60 <b>(+85.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>183.64 (n/a)</td><td>187.00 (n/a)</td><td>149.90 (n/a)</td><td>28.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (-5.90%)</td><td>0.14 (+0.21%)</td><td>0.14 (-1.94%)</td><td>0.11 (+13.87%)</td><td>0.02 <b>(-33.26%)</b></td><td>190.80 (-12.20%)</td><td>155.18 (-2.60%)</td><td>150.20 (+1.97%)</td><td>126.50 (+6.30%)</td><td>23.39 <b>(-38.22%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>217.30 (n/a)</td><td>159.32 (n/a)</td><td>147.30 (n/a)</td><td>119.00 (n/a)</td><td>37.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (-5.61%)</td><td>0.14 (-4.65%)</td><td>0.14 (+3.31%)</td><td>0.12 (-5.73%)</td><td>0.02 (-6.98%)</td><td>179.10 (+6.10%)</td><td>156.66 (+4.90%)</td><td>148.70 (-3.19%)</td><td>133.40 (+5.96%)</td><td>21.07 (+7.48%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>168.80 (n/a)</td><td>149.34 (n/a)</td><td>153.60 (n/a)</td><td>125.90 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (+15.06%)</td><td>0.11 (+6.18%)</td><td>0.10 (-5.75%)</td><td>0.09 <b>(+34.65%)</b></td><td>0.03 (+9.01%)</td><td>223.30 <b>(-25.74%)</b></td><td>194.92 (-6.91%)</td><td>210.50 (+6.10%)</td><td>136.50 (-13.06%)</td><td>36.22 <b>(-33.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>300.70 (n/a)</td><td>209.38 (n/a)</td><td>198.40 (n/a)</td><td>157.00 (n/a)</td><td>54.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (+13.07%)</td><td>0.11 (-7.78%)</td><td>0.10 (-11.94%)</td><td>0.08 <b>(-26.65%)</b></td><td>0.03 <b>(+143.19%)</b></td><td>278.40 <b>(+36.34%)</b></td><td>205.44 (+13.99%)</td><td>207.10 (+13.54%)</td><td>135.60 (-11.60%)</td><td>53.76 <b>(+192.83%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>180.22 (n/a)</td><td>182.40 (n/a)</td><td>153.40 (n/a)</td><td>18.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (+0.13%)</td><td>0.12 (-3.01%)</td><td>0.11 (-1.80%)</td><td>0.10 (+10.23%)</td><td>0.03 (-10.37%)</td><td>219.00 (-9.28%)</td><td>179.66 (+1.81%)</td><td>186.90 (+1.80%)</td><td>127.20 (-0.08%)</td><td>39.70 (-14.76%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>241.40 (n/a)</td><td>176.46 (n/a)</td><td>183.60 (n/a)</td><td>127.30 (n/a)</td><td>46.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (+15.47%)</td><td>0.11 (+11.02%)</td><td>0.12 (+16.16%)</td><td>0.10 (-0.47%)</td><td>0.01 <b>(+158.40%)</b></td><td>218.50 (+0.46%)</td><td>187.92 (-9.23%)</td><td>174.60 (-13.91%)</td><td>172.20 (-13.42%)</td><td>20.98 <b>(+121.47%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>217.50 (n/a)</td><td>207.02 (n/a)</td><td>202.80 (n/a)</td><td>198.90 (n/a)</td><td>9.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (-0.19%)</td><td>0.11 (-5.68%)</td><td>0.11 (-2.35%)</td><td>0.09 (+2.66%)</td><td>0.02 (-9.78%)</td><td>226.80 (-2.58%)</td><td>199.36 (+5.59%)</td><td>199.10 (+2.42%)</td><td>155.30 (+0.19%)</td><td>29.31 (-9.02%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>232.80 (n/a)</td><td>188.80 (n/a)</td><td>194.40 (n/a)</td><td>155.00 (n/a)</td><td>32.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 <b>(-21.06%)</b></td><td>0.09 (-13.79%)</td><td>0.09 (-8.81%)</td><td>0.08 (-8.11%)</td><td>0.01 <b>(-58.02%)</b></td><td>268.40 (+8.84%)</td><td>236.22 (+13.80%)</td><td>236.90 (+9.68%)</td><td>213.40 <b>(+26.65%)</b></td><td>21.45 <b>(-40.82%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>246.60 (n/a)</td><td>207.58 (n/a)</td><td>216.00 (n/a)</td><td>168.50 (n/a)</td><td>36.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.30 (n/a)</td><td>184.84 (n/a)</td><td>184.90 (n/a)</td><td>120.60 (n/a)</td><td>44.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.10 (n/a)</td><td>200.88 (n/a)</td><td>195.50 (n/a)</td><td>173.30 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.00 (n/a)</td><td>189.56 (n/a)</td><td>189.90 (n/a)</td><td>170.00 (n/a)</td><td>13.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>175.10 (n/a)</td><td>159.40 (n/a)</td><td>150.50 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>171.18 (n/a)</td><td>168.20 (n/a)</td><td>158.10 (n/a)</td><td>13.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>187.60 (n/a)</td><td>150.52 (n/a)</td><td>131.40 (n/a)</td><td>118.60 (n/a)</td><td>32.80 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>202.50 (n/a)</td><td>168.32 (n/a)</td><td>166.20 (n/a)</td><td>127.50 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>278.70 (n/a)</td><td>218.38 (n/a)</td><td>246.80 (n/a)</td><td>126.50 (n/a)</td><td>67.09 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>181.14 (n/a)</td><td>184.10 (n/a)</td><td>155.50 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>219.80 (n/a)</td><td>181.46 (n/a)</td><td>172.70 (n/a)</td><td>156.00 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>264.70 (n/a)</td><td>204.92 (n/a)</td><td>203.50 (n/a)</td><td>156.40 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>193.30 (n/a)</td><td>198.40 (n/a)</td><td>172.90 (n/a)</td><td>17.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (-19.87%)</td><td>0.28 (-10.83%)</td><td>0.28 (-2.65%)</td><td>0.21 (-14.72%)</td><td>0.04 <b>(-37.41%)</b></td><td>236.10 (+17.23%)</td><td>182.30 (+10.62%)</td><td>172.50 (+2.74%)</td><td>155.20 <b>(+24.76%)</b></td><td>31.12 (-5.06%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>201.40 (n/a)</td><td>164.80 (n/a)</td><td>167.90 (n/a)</td><td>124.40 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>206.80 (n/a)</td><td>159.92 (n/a)</td><td>155.60 (n/a)</td><td>129.90 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>237.00 (n/a)</td><td>198.90 (n/a)</td><td>201.40 (n/a)</td><td>168.90 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>332.00 (n/a)</td><td>222.96 (n/a)</td><td>202.80 (n/a)</td><td>177.00 (n/a)</td><td>62.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>173.44 (n/a)</td><td>174.10 (n/a)</td><td>137.60 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>172.88 (n/a)</td><td>174.30 (n/a)</td><td>121.30 (n/a)</td><td>34.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.00 (n/a)</td><td>190.60 (n/a)</td><td>189.70 (n/a)</td><td>182.30 (n/a)</td><td>8.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>326.00 (n/a)</td><td>203.90 (n/a)</td><td>191.60 (n/a)</td><td>109.40 (n/a)</td><td>80.95 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>185.70 (n/a)</td><td>163.46 (n/a)</td><td>166.70 (n/a)</td><td>129.80 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>179.90 (n/a)</td><td>174.22 (n/a)</td><td>175.10 (n/a)</td><td>166.40 (n/a)</td><td>5.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>179.02 (n/a)</td><td>175.00 (n/a)</td><td>146.30 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>253.80 (n/a)</td><td>187.80 (n/a)</td><td>179.60 (n/a)</td><td>108.40 (n/a)</td><td>54.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>166.54 (n/a)</td><td>169.80 (n/a)</td><td>151.90 (n/a)</td><td>9.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>177.80 (n/a)</td><td>170.58 (n/a)</td><td>173.00 (n/a)</td><td>160.40 (n/a)</td><td>6.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>185.64 (n/a)</td><td>189.30 (n/a)</td><td>148.40 (n/a)</td><td>26.63 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>322.50 (n/a)</td><td>211.32 (n/a)</td><td>197.20 (n/a)</td><td>161.10 (n/a)</td><td>64.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>230.10 (n/a)</td><td>179.66 (n/a)</td><td>187.70 (n/a)</td><td>137.10 (n/a)</td><td>36.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>208.50 (n/a)</td><td>174.20 (n/a)</td><td>174.60 (n/a)</td><td>143.00 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>213.80 (n/a)</td><td>194.66 (n/a)</td><td>200.50 (n/a)</td><td>156.40 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>159.50 (n/a)</td><td>147.22 (n/a)</td><td>149.50 (n/a)</td><td>121.50 (n/a)</td><td>15.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.20 (n/a)</td><td>148.04 (n/a)</td><td>141.90 (n/a)</td><td>133.40 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>160.68 (n/a)</td><td>155.80 (n/a)</td><td>132.90 (n/a)</td><td>20.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.20 (n/a)</td><td>188.86 (n/a)</td><td>199.40 (n/a)</td><td>146.80 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.10 (n/a)</td><td>196.30 (n/a)</td><td>182.40 (n/a)</td><td>174.10 (n/a)</td><td>32.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.00 (n/a)</td><td>196.70 (n/a)</td><td>162.10 (n/a)</td><td>142.30 (n/a)</td><td>60.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>176.64 (n/a)</td><td>181.50 (n/a)</td><td>153.50 (n/a)</td><td>13.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>301.40 (n/a)</td><td>220.06 (n/a)</td><td>216.80 (n/a)</td><td>151.50 (n/a)</td><td>68.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>172.86 (n/a)</td><td>179.80 (n/a)</td><td>133.50 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>168.84 (n/a)</td><td>163.40 (n/a)</td><td>146.20 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>175.40 (n/a)</td><td>182.30 (n/a)</td><td>145.40 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.50 (n/a)</td><td>206.92 (n/a)</td><td>202.30 (n/a)</td><td>189.50 (n/a)</td><td>18.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.20 (n/a)</td><td>186.42 (n/a)</td><td>182.70 (n/a)</td><td>171.00 (n/a)</td><td>11.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>195.48 (n/a)</td><td>198.90 (n/a)</td><td>156.30 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.90 (n/a)</td><td>188.48 (n/a)</td><td>192.90 (n/a)</td><td>171.50 (n/a)</td><td>16.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>244.70 (n/a)</td><td>221.44 (n/a)</td><td>223.40 (n/a)</td><td>199.00 (n/a)</td><td>17.03 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>163.10 (n/a)</td><td>167.10 (n/a)</td><td>128.70 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.00 (n/a)</td><td>164.46 (n/a)</td><td>166.00 (n/a)</td><td>125.20 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>357.70 (n/a)</td><td>222.76 (n/a)</td><td>183.30 (n/a)</td><td>181.00 (n/a)</td><td>76.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.80 (n/a)</td><td>180.98 (n/a)</td><td>168.20 (n/a)</td><td>152.00 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.30 (n/a)</td><td>188.68 (n/a)</td><td>181.30 (n/a)</td><td>164.90 (n/a)</td><td>26.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>296.10 (n/a)</td><td>192.68 (n/a)</td><td>174.90 (n/a)</td><td>153.90 (n/a)</td><td>59.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>187.94 (n/a)</td><td>196.70 (n/a)</td><td>168.40 (n/a)</td><td>14.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>212.44 (n/a)</td><td>207.60 (n/a)</td><td>191.50 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.50 (n/a)</td><td>163.18 (n/a)</td><td>169.10 (n/a)</td><td>130.90 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>181.90 (n/a)</td><td>144.94 (n/a)</td><td>142.80 (n/a)</td><td>121.10 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>167.74 (n/a)</td><td>165.30 (n/a)</td><td>148.20 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.90 (n/a)</td><td>184.86 (n/a)</td><td>184.90 (n/a)</td><td>161.40 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>209.90 (n/a)</td><td>160.62 (n/a)</td><td>158.60 (n/a)</td><td>116.30 (n/a)</td><td>37.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.80 (n/a)</td><td>164.70 (n/a)</td><td>155.60 (n/a)</td><td>130.60 (n/a)</td><td>36.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>183.50 (n/a)</td><td>168.00 (n/a)</td><td>166.20 (n/a)</td><td>159.60 (n/a)</td><td>9.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>255.30 (n/a)</td><td>209.64 (n/a)</td><td>197.40 (n/a)</td><td>177.50 (n/a)</td><td>34.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>4.25 (-0.65%)</td><td>4.07 (+4.89%)</td><td>4.24 (+1.48%)</td><td>3.50 (+7.92%)</td><td>0.32 <b>(-34.94%)</b></td><td>2690.20 (-7.34%)</td><td>2323.88 (-5.46%)</td><td>2220.30 (-1.46%)</td><td>2213.40 (+0.66%)</td><td>206.36 <b>(-38.23%)</b></td><td>1671.38 (-0.65%)</td><td>1600.97 (+4.89%)</td><td>1666.13 (+1.48%)</td><td>1375.15 (+7.92%)</td><td>127.62 <b>(-34.94%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.28 (n/a)</td><td>3.88 (n/a)</td><td>4.17 (n/a)</td><td>3.24 (n/a)</td><td>0.50 (n/a)</td><td>2903.40 (n/a)</td><td>2458.00 (n/a)</td><td>2253.30 (n/a)</td><td>2198.90 (n/a)</td><td>334.08 (n/a)</td><td>1682.37 (n/a)</td><td>1526.35 (n/a)</td><td>1641.79 (n/a)</td><td>1274.17 (n/a)</td><td>196.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.11 (-9.11%)</td><td>0.91 (+0.19%)</td><td>0.95 (+1.49%)</td><td>0.61 (-11.10%)</td><td>0.19 (-17.27%)</td><td>365.00 (+12.48%)</td><td>254.92 (-0.98%)</td><td>233.50 (-1.48%)</td><td>199.00 (+10.01%)</td><td>64.56 (+1.58%)</td><td>47.43 (-9.11%)</td><td>38.62 (+0.19%)</td><td>40.41 (+1.49%)</td><td>25.85 (-11.10%)</td><td>8.03 (-17.27%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.22 (n/a)</td><td>0.90 (n/a)</td><td>0.93 (n/a)</td><td>0.68 (n/a)</td><td>0.23 (n/a)</td><td>324.50 (n/a)</td><td>257.44 (n/a)</td><td>237.00 (n/a)</td><td>180.90 (n/a)</td><td>63.56 (n/a)</td><td>52.18 (n/a)</td><td>38.55 (n/a)</td><td>39.81 (n/a)</td><td>29.08 (n/a)</td><td>9.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.21 (+9.18%)</td><td>0.87 (-12.22%)</td><td>0.81 <b>(-25.80%)</b></td><td>0.62 (-11.07%)</td><td>0.22 <b>(+21.43%)</b></td><td>356.70 (+12.45%)</td><td>267.84 (+15.61%)</td><td>272.40 <b>(+34.78%)</b></td><td>182.10 (-8.40%)</td><td>62.64 <b>(+23.35%)</b></td><td>51.83 (+9.18%)</td><td>36.93 (-12.22%)</td><td>34.64 <b>(-25.80%)</b></td><td>26.45 (-11.07%)</td><td>9.31 <b>(+21.43%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.11 (n/a)</td><td>0.99 (n/a)</td><td>1.09 (n/a)</td><td>0.70 (n/a)</td><td>0.18 (n/a)</td><td>317.20 (n/a)</td><td>231.68 (n/a)</td><td>202.10 (n/a)</td><td>198.80 (n/a)</td><td>50.78 (n/a)</td><td>47.47 (n/a)</td><td>42.07 (n/a)</td><td>46.69 (n/a)</td><td>29.75 (n/a)</td><td>7.67 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.52 (-0.01%)</td><td>0.52 (-0.01%)</td><td>0.52 (-0.07%)</td><td>0.52 (+0.04%)</td><td>0.00 (-18.06%)</td><td>48507.60 (-0.04%)</td><td>48479.12 (+0.01%)</td><td>48502.40 (+0.07%)</td><td>48438.90 (+0.01%)</td><td>34.62 (-18.15%)</td><td>354.67 (-0.01%)</td><td>354.38 (-0.01%)</td><td>354.21 (-0.07%)</td><td>354.17 (+0.04%)</td><td>0.25 (-18.06%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48529.00 (n/a)</td><td>48475.22 (n/a)</td><td>48467.60 (n/a)</td><td>48434.40 (n/a)</td><td>42.30 (n/a)</td><td>354.70 (n/a)</td><td>354.41 (n/a)</td><td>354.46 (n/a)</td><td>354.01 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (-2.25%)</td><td>0.21 (-0.69%)</td><td>0.21 (-0.17%)</td><td>0.21 (-0.33%)</td><td>0.00 <b>(-55.41%)</b></td><td>119947.90 (+0.33%)</td><td>119035.94 (+0.68%)</td><td>119003.80 (+0.18%)</td><td>117982.50 (+2.30%)</td><td>763.21 <b>(-54.09%)</b></td><td>145.61 (-2.25%)</td><td>144.33 (-0.69%)</td><td>144.36 (-0.17%)</td><td>143.23 (-0.33%)</td><td>0.93 <b>(-55.41%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119550.40 (n/a)</td><td>118234.82 (n/a)</td><td>118795.60 (n/a)</td><td>115329.20 (n/a)</td><td>1662.24 (n/a)</td><td>148.96 (n/a)</td><td>145.33 (n/a)</td><td>144.62 (n/a)</td><td>143.70 (n/a)</td><td>2.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.90 (-1.39%)</td><td>0.89 (+0.00%)</td><td>0.89 (-0.21%)</td><td>0.88 (+0.66%)</td><td>0.01 <b>(-52.04%)</b></td><td>28611.80 (-0.66%)</td><td>28226.70 (-0.02%)</td><td>28172.70 (+0.21%)</td><td>28010.20 (+1.41%)</td><td>226.73 <b>(-51.63%)</b></td><td>613.34 (-1.39%)</td><td>608.67 (+0.00%)</td><td>609.80 (-0.21%)</td><td>600.45 (+0.66%)</td><td>4.85 <b>(-52.03%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28801.10 (n/a)</td><td>28232.64 (n/a)</td><td>28114.10 (n/a)</td><td>27619.70 (n/a)</td><td>468.75 (n/a)</td><td>622.02 (n/a)</td><td>608.64 (n/a)</td><td>611.08 (n/a)</td><td>596.50 (n/a)</td><td>10.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.63 (-0.95%)</td><td>3.48 (-0.42%)</td><td>3.48 (-1.79%)</td><td>3.36 (+0.21%)</td><td>0.11 (-18.83%)</td><td>7480.70 (-0.21%)</td><td>7238.22 (+0.38%)</td><td>7237.90 (+1.83%)</td><td>6941.60 (+0.96%)</td><td>219.28 (-18.75%)</td><td>2474.90 (-0.95%)</td><td>2375.25 (-0.42%)</td><td>2373.60 (-1.79%)</td><td>2296.56 (+0.21%)</td><td>72.43 (-18.83%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.66 (n/a)</td><td>3.49 (n/a)</td><td>3.54 (n/a)</td><td>3.36 (n/a)</td><td>0.13 (n/a)</td><td>7496.40 (n/a)</td><td>7210.56 (n/a)</td><td>7108.10 (n/a)</td><td>6875.80 (n/a)</td><td>269.88 (n/a)</td><td>2498.62 (n/a)</td><td>2385.27 (n/a)</td><td>2416.93 (n/a)</td><td>2291.76 (n/a)</td><td>89.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.22 (+3.04%)</td><td>2.91 (-1.89%)</td><td>2.85 (-6.45%)</td><td>2.76 (+0.43%)</td><td>0.18 (+6.50%)</td><td>9122.60 (-0.43%)</td><td>8675.10 (+1.95%)</td><td>8833.50 (+6.90%)</td><td>7806.60 (-2.95%)</td><td>505.40 (+1.38%)</td><td>2200.70 (+3.04%)</td><td>1986.12 (-1.89%)</td><td>1944.86 (-6.45%)</td><td>1883.21 (+0.43%)</td><td>123.68 (+6.50%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.13 (n/a)</td><td>2.97 (n/a)</td><td>3.05 (n/a)</td><td>2.75 (n/a)</td><td>0.17 (n/a)</td><td>9162.20 (n/a)</td><td>8509.40 (n/a)</td><td>8263.60 (n/a)</td><td>8043.90 (n/a)</td><td>498.53 (n/a)</td><td>2135.77 (n/a)</td><td>2024.37 (n/a)</td><td>2078.98 (n/a)</td><td>1875.08 (n/a)</td><td>116.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.31 (-0.47%)</td><td>3.21 (+0.18%)</td><td>3.18 (-0.08%)</td><td>3.13 (-0.54%)</td><td>0.08 (+16.31%)</td><td>8033.60 (+0.54%)</td><td>7849.24 (-0.17%)</td><td>7924.10 (+0.08%)</td><td>7613.00 (+0.47%)</td><td>192.18 (+18.01%)</td><td>2256.64 (-0.47%)</td><td>2189.79 (+0.18%)</td><td>2168.07 (-0.08%)</td><td>2138.51 (-0.54%)</td><td>54.00 (+16.31%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.32 (n/a)</td><td>3.20 (n/a)</td><td>3.18 (n/a)</td><td>3.15 (n/a)</td><td>0.07 (n/a)</td><td>7990.10 (n/a)</td><td>7862.40 (n/a)</td><td>7918.00 (n/a)</td><td>7577.40 (n/a)</td><td>162.85 (n/a)</td><td>2267.25 (n/a)</td><td>2185.84 (n/a)</td><td>2169.73 (n/a)</td><td>2150.15 (n/a)</td><td>46.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (-0.11%)</td><td>0.79 (+0.00%)</td><td>0.79 (+0.02%)</td><td>0.79 (+0.09%)</td><td>0.00 <b>(-33.71%)</b></td><td>96153.20 (-0.09%)</td><td>96066.40 (-0.00%)</td><td>96116.40 (-0.02%)</td><td>95822.90 (+0.11%)</td><td>137.25 <b>(-33.68%)</b></td><td>717.15 (-0.11%)</td><td>715.33 (+0.00%)</td><td>714.96 (+0.02%)</td><td>714.69 (+0.09%)</td><td>1.02 <b>(-33.71%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96238.30 (n/a)</td><td>96069.52 (n/a)</td><td>96137.30 (n/a)</td><td>95714.10 (n/a)</td><td>206.95 (n/a)</td><td>717.97 (n/a)</td><td>715.31 (n/a)</td><td>714.81 (n/a)</td><td>714.06 (n/a)</td><td>1.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.73 (+0.02%)</td><td>0.73 (+0.04%)</td><td>0.73 (+0.07%)</td><td>0.73 (+0.01%)</td><td>0.00 (+2.31%)</td><td>103448.20 (-0.01%)</td><td>103347.40 (-0.04%)</td><td>103327.50 (-0.07%)</td><td>103287.60 (-0.02%)</td><td>60.34 (+2.24%)</td><td>665.32 (+0.02%)</td><td>664.94 (+0.04%)</td><td>665.07 (+0.07%)</td><td>664.29 (+0.01%)</td><td>0.39 (+2.30%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103461.40 (n/a)</td><td>103385.74 (n/a)</td><td>103398.40 (n/a)</td><td>103309.50 (n/a)</td><td>59.02 (n/a)</td><td>665.18 (n/a)</td><td>664.69 (n/a)</td><td>664.61 (n/a)</td><td>664.20 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.70 (+1.07%)</td><td>0.70 (+0.81%)</td><td>0.70 (+0.84%)</td><td>0.69 (+0.92%)</td><td>0.00 <b>(+29.39%)</b></td><td>108772.50 (-0.91%)</td><td>108347.34 (-0.80%)</td><td>108262.00 (-0.83%)</td><td>107713.60 (-1.06%)</td><td>436.99 <b>(+26.86%)</b></td><td>637.98 (+1.07%)</td><td>634.26 (+0.81%)</td><td>634.75 (+0.84%)</td><td>631.77 (+0.92%)</td><td>2.56 <b>(+29.39%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109772.30 (n/a)</td><td>109223.54 (n/a)</td><td>109170.20 (n/a)</td><td>108869.60 (n/a)</td><td>344.45 (n/a)</td><td>631.21 (n/a)</td><td>629.17 (n/a)</td><td>629.47 (n/a)</td><td>626.02 (n/a)</td><td>1.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.58 (+2.16%)</td><td>7.24 (+10.46%)</td><td>7.25 (+10.04%)</td><td>6.84 <b>(+35.43%)</b></td><td>0.34 <b>(-63.15%)</b></td><td>1302.70 <b>(-26.16%)</b></td><td>1234.00 (-10.92%)</td><td>1229.20 (-9.12%)</td><td>1175.80 (-2.11%)</td><td>57.44 <b>(-74.10%)</b></td><td>456.60 (+2.16%)</td><td>435.82 (+10.46%)</td><td>436.77 (+10.04%)</td><td>412.12 <b>(+35.43%)</b></td><td>20.20 <b>(-63.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.42 (n/a)</td><td>6.55 (n/a)</td><td>6.59 (n/a)</td><td>5.05 (n/a)</td><td>0.91 (n/a)</td><td>1764.30 (n/a)</td><td>1385.26 (n/a)</td><td>1352.60 (n/a)</td><td>1201.10 (n/a)</td><td>221.79 (n/a)</td><td>446.97 (n/a)</td><td>394.54 (n/a)</td><td>396.92 (n/a)</td><td>304.30 (n/a)</td><td>54.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>6.94 (-2.04%)</td><td>5.80 (-11.48%)</td><td>5.46 <b>(-20.99%)</b></td><td>4.79 (-1.12%)</td><td>0.98 (+2.10%)</td><td>1861.10 (+1.13%)</td><td>1571.28 (+13.07%)</td><td>1632.10 <b>(+26.57%)</b></td><td>1284.00 (+2.08%)</td><td>257.74 (+2.13%)</td><td>418.13 (-2.04%)</td><td>349.40 (-11.48%)</td><td>328.94 <b>(-20.99%)</b></td><td>288.47 (-1.12%)</td><td>59.00 (+2.10%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.09 (n/a)</td><td>6.55 (n/a)</td><td>6.91 (n/a)</td><td>4.84 (n/a)</td><td>0.96 (n/a)</td><td>1840.30 (n/a)</td><td>1389.68 (n/a)</td><td>1289.50 (n/a)</td><td>1257.80 (n/a)</td><td>252.35 (n/a)</td><td>426.84 (n/a)</td><td>394.72 (n/a)</td><td>416.34 (n/a)</td><td>291.73 (n/a)</td><td>57.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.07 (+2.29%)</td><td>6.66 (+1.59%)</td><td>6.56 (+0.91%)</td><td>6.28 (+2.18%)</td><td>0.30 (-5.02%)</td><td>1418.50 (-2.13%)</td><td>1339.58 (-1.59%)</td><td>1357.70 (-0.91%)</td><td>1260.20 (-2.23%)</td><td>60.51 (-8.81%)</td><td>426.02 (+2.29%)</td><td>401.44 (+1.59%)</td><td>395.44 (+0.91%)</td><td>378.49 (+2.18%)</td><td>18.21 (-5.02%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>6.91 (n/a)</td><td>6.56 (n/a)</td><td>6.51 (n/a)</td><td>6.15 (n/a)</td><td>0.32 (n/a)</td><td>1449.30 (n/a)</td><td>1361.20 (n/a)</td><td>1370.10 (n/a)</td><td>1289.00 (n/a)</td><td>66.35 (n/a)</td><td>416.49 (n/a)</td><td>395.16 (n/a)</td><td>391.86 (n/a)</td><td>370.43 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.53 (+6.38%)</td><td>8.10 (+5.82%)</td><td>8.02 (+0.74%)</td><td>7.91 (+11.08%)</td><td>0.25 <b>(-47.29%)</b></td><td>4408.70 (-9.98%)</td><td>4307.40 (-5.72%)</td><td>4347.80 (-0.74%)</td><td>4087.60 (-5.99%)</td><td>126.58 <b>(-55.64%)</b></td><td>525.36 (+6.38%)</td><td>498.91 (+5.82%)</td><td>493.93 (+0.74%)</td><td>487.11 (+11.08%)</td><td>15.18 <b>(-47.29%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>8.02 (n/a)</td><td>7.65 (n/a)</td><td>7.96 (n/a)</td><td>7.12 (n/a)</td><td>0.47 (n/a)</td><td>4897.30 (n/a)</td><td>4568.88 (n/a)</td><td>4380.10 (n/a)</td><td>4348.20 (n/a)</td><td>285.37 (n/a)</td><td>493.88 (n/a)</td><td>471.46 (n/a)</td><td>490.28 (n/a)</td><td>438.50 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.86 (+2.23%)</td><td>7.51 (-1.49%)</td><td>7.56 (-0.89%)</td><td>7.03 (-7.20%)</td><td>0.30 <b>(+664.61%)</b></td><td>4956.80 (+7.76%)</td><td>4646.00 (+1.64%)</td><td>4613.00 (+0.90%)</td><td>4437.20 (-2.18%)</td><td>189.92 <b>(+712.36%)</b></td><td>483.97 (+2.23%)</td><td>462.82 (-1.49%)</td><td>465.53 (-0.89%)</td><td>433.24 (-7.20%)</td><td>18.39 <b>(+664.61%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.69 (n/a)</td><td>7.63 (n/a)</td><td>7.63 (n/a)</td><td>7.58 (n/a)</td><td>0.04 (n/a)</td><td>4600.00 (n/a)</td><td>4571.16 (n/a)</td><td>4571.90 (n/a)</td><td>4536.00 (n/a)</td><td>23.38 (n/a)</td><td>473.43 (n/a)</td><td>469.80 (n/a)</td><td>469.71 (n/a)</td><td>466.85 (n/a)</td><td>2.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.31 (-2.14%)</td><td>7.02 (-3.20%)</td><td>6.92 (-5.26%)</td><td>6.68 (-1.47%)</td><td>0.27 (-3.07%)</td><td>5219.40 (+1.49%)</td><td>4969.70 (+3.30%)</td><td>5037.50 (+5.55%)</td><td>4771.60 (+2.19%)</td><td>191.88 (-0.70%)</td><td>450.06 (-2.14%)</td><td>432.63 (-3.20%)</td><td>426.30 (-5.26%)</td><td>411.44 (-1.47%)</td><td>16.68 (-3.07%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.47 (n/a)</td><td>7.26 (n/a)</td><td>7.31 (n/a)</td><td>6.78 (n/a)</td><td>0.28 (n/a)</td><td>5142.90 (n/a)</td><td>4811.02 (n/a)</td><td>4772.40 (n/a)</td><td>4669.20 (n/a)</td><td>193.23 (n/a)</td><td>459.92 (n/a)</td><td>446.92 (n/a)</td><td>449.98 (n/a)</td><td>417.56 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (-0.01%)</td><td>0.79 (-0.03%)</td><td>0.79 (-0.01%)</td><td>0.79 (-0.08%)</td><td>0.00 <b>(+76.50%)</b></td><td>95540.70 (+0.08%)</td><td>95450.80 (+0.03%)</td><td>95428.60 (+0.01%)</td><td>95405.40 (+0.01%)</td><td>53.09 <b>(+76.49%)</b></td><td>720.29 (-0.01%)</td><td>719.95 (-0.03%)</td><td>720.11 (-0.01%)</td><td>719.27 (-0.08%)</td><td>0.40 <b>(+76.49%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95467.20 (n/a)</td><td>95420.62 (n/a)</td><td>95419.90 (n/a)</td><td>95391.90 (n/a)</td><td>30.08 (n/a)</td><td>720.39 (n/a)</td><td>720.17 (n/a)</td><td>720.18 (n/a)</td><td>719.82 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.74 (+0.03%)</td><td>0.74 (-0.00%)</td><td>0.74 (+0.00%)</td><td>0.74 (-0.04%)</td><td>0.00 <b>(+280.20%)</b></td><td>102650.10 (+0.04%)</td><td>102591.10 (+0.00%)</td><td>102582.30 (-0.00%)</td><td>102549.60 (-0.03%)</td><td>38.15 <b>(+279.88%)</b></td><td>670.11 (+0.03%)</td><td>669.84 (-0.00%)</td><td>669.90 (+0.00%)</td><td>669.45 (-0.04%)</td><td>0.25 <b>(+280.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102604.20 (n/a)</td><td>102587.02 (n/a)</td><td>102584.80 (n/a)</td><td>102577.80 (n/a)</td><td>10.04 (n/a)</td><td>669.93 (n/a)</td><td>669.87 (n/a)</td><td>669.88 (n/a)</td><td>669.75 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.70 (-0.03%)</td><td>0.70 (+0.11%)</td><td>0.70 (+0.18%)</td><td>0.70 (+0.15%)</td><td>0.00 <b>(-47.76%)</b></td><td>107392.50 (-0.15%)</td><td>107293.72 (-0.11%)</td><td>107254.60 (-0.18%)</td><td>107237.70 (+0.03%)</td><td>70.61 <b>(-47.84%)</b></td><td>640.81 (-0.03%)</td><td>640.48 (+0.11%)</td><td>640.71 (+0.18%)</td><td>639.89 (+0.15%)</td><td>0.42 <b>(-47.75%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107555.50 (n/a)</td><td>107410.04 (n/a)</td><td>107448.50 (n/a)</td><td>107207.80 (n/a)</td><td>135.38 (n/a)</td><td>640.99 (n/a)</td><td>639.79 (n/a)</td><td>639.56 (n/a)</td><td>638.92 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.61 (-1.44%)</td><td>3.27 (-0.20%)</td><td>3.21 (+1.24%)</td><td>2.98 (+2.74%)</td><td>0.30 (-18.98%)</td><td>2706.50 (-2.66%)</td><td>2483.22 (-0.13%)</td><td>2509.40 (-1.23%)</td><td>2233.10 (+1.46%)</td><td>222.59 (-18.51%)</td><td>946.63 (-1.44%)</td><td>856.85 (-0.20%)</td><td>842.40 (+1.24%)</td><td>781.07 (+2.74%)</td><td>77.70 (-18.98%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.66 (n/a)</td><td>3.27 (n/a)</td><td>3.17 (n/a)</td><td>2.90 (n/a)</td><td>0.37 (n/a)</td><td>2780.60 (n/a)</td><td>2486.44 (n/a)</td><td>2540.60 (n/a)</td><td>2200.90 (n/a)</td><td>273.14 (n/a)</td><td>960.49 (n/a)</td><td>858.60 (n/a)</td><td>832.05 (n/a)</td><td>760.23 (n/a)</td><td>95.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.35 (-2.39%)</td><td>0.32 (+0.29%)</td><td>0.33 (+2.82%)</td><td>0.29 (+2.73%)</td><td>0.02 (-13.89%)</td><td>4294.90 (-2.66%)</td><td>3863.72 (-0.44%)</td><td>3719.30 (-2.74%)</td><td>3601.00 (+2.45%)</td><td>287.35 (-14.83%)</td><td>18.64 (-2.39%)</td><td>17.44 (+0.29%)</td><td>18.04 (+2.82%)</td><td>15.63 (+2.73%)</td><td>1.25 (-13.89%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>4412.10 (n/a)</td><td>3880.88 (n/a)</td><td>3824.10 (n/a)</td><td>3514.90 (n/a)</td><td>337.39 (n/a)</td><td>19.09 (n/a)</td><td>17.39 (n/a)</td><td>17.55 (n/a)</td><td>15.21 (n/a)</td><td>1.45 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>4.90 (-0.72%)</td><td>4.04 (-14.98%)</td><td>3.66 <b>(-24.05%)</b></td><td>3.33 <b>(-27.03%)</b></td><td>0.72 <b>(+307.41%)</b></td><td>1999.80 <b>(+37.04%)</b></td><td>1685.30 <b>(+20.40%)</b></td><td>1817.80 <b>(+31.66%)</b></td><td>1356.20 (+0.72%)</td><td>287.07 <b>(+447.16%)</b></td><td>1515.41 (-0.72%)</td><td>1249.75 (-14.98%)</td><td>1130.63 <b>(-24.05%)</b></td><td>1027.69 <b>(-27.03%)</b></td><td>222.64 <b>(+307.41%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.94 (n/a)</td><td>4.76 (n/a)</td><td>4.82 (n/a)</td><td>4.56 (n/a)</td><td>0.18 (n/a)</td><td>1459.30 (n/a)</td><td>1399.72 (n/a)</td><td>1380.70 (n/a)</td><td>1346.50 (n/a)</td><td>52.46 (n/a)</td><td>1526.38 (n/a)</td><td>1469.96 (n/a)</td><td>1488.57 (n/a)</td><td>1408.39 (n/a)</td><td>54.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>11.43 (n/a)</td><td>11.00 (n/a)</td><td>10.95 (n/a)</td><td>10.47 (n/a)</td><td>0.39 (n/a)</td><td>11.42 (n/a)</td><td>10.99 (n/a)</td><td>10.94 (n/a)</td><td>10.46 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>24.93 (-1.40%)</td><td>24.28 (-0.64%)</td><td>24.25 (-0.50%)</td><td>23.86 (+0.52%)</td><td>0.44 <b>(-28.36%)</b></td><td>24.91 (-1.40%)</td><td>24.26 (-0.64%)</td><td>24.24 (-0.50%)</td><td>23.84 (+0.52%)</td><td>0.44 <b>(-28.36%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>25.28 (n/a)</td><td>24.44 (n/a)</td><td>24.37 (n/a)</td><td>23.73 (n/a)</td><td>0.62 (n/a)</td><td>25.27 (n/a)</td><td>24.42 (n/a)</td><td>24.36 (n/a)</td><td>23.72 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>40.91 (+1.20%)</td><td>40.01 (+2.88%)</td><td>39.93 (+3.72%)</td><td>38.80 (+2.03%)</td><td>0.80 (-15.91%)</td><td>40.89 (+1.20%)</td><td>39.99 (+2.88%)</td><td>39.91 (+3.72%)</td><td>38.77 (+2.03%)</td><td>0.80 (-15.91%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>40.43 (n/a)</td><td>38.89 (n/a)</td><td>38.50 (n/a)</td><td>38.02 (n/a)</td><td>0.96 (n/a)</td><td>40.41 (n/a)</td><td>38.87 (n/a)</td><td>38.48 (n/a)</td><td>38.00 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>45.87 (+3.13%)</td><td>42.90 (+1.91%)</td><td>42.43 (-1.42%)</td><td>40.99 (+8.43%)</td><td>1.86 <b>(-33.31%)</b></td><td>45.84 (+3.13%)</td><td>42.87 (+1.91%)</td><td>42.41 (-1.42%)</td><td>40.97 (+8.43%)</td><td>1.86 <b>(-33.31%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>44.48 (n/a)</td><td>42.10 (n/a)</td><td>43.05 (n/a)</td><td>37.81 (n/a)</td><td>2.79 (n/a)</td><td>44.45 (n/a)</td><td>42.07 (n/a)</td><td>43.02 (n/a)</td><td>37.78 (n/a)</td><td>2.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.19 (n/a)</td><td>12.30 (n/a)</td><td>12.55 (n/a)</td><td>10.61 (n/a)</td><td>1.01 (n/a)</td><td>13.19 (n/a)</td><td>12.29 (n/a)</td><td>12.54 (n/a)</td><td>10.60 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>24.63 (-0.51%)</td><td>23.83 (-0.36%)</td><td>23.84 (-1.84%)</td><td>23.09 (+5.42%)</td><td>0.55 <b>(-52.38%)</b></td><td>24.61 (-0.51%)</td><td>23.82 (-0.36%)</td><td>23.83 (-1.84%)</td><td>23.07 (+5.42%)</td><td>0.55 <b>(-52.38%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>24.75 (n/a)</td><td>23.92 (n/a)</td><td>24.29 (n/a)</td><td>21.90 (n/a)</td><td>1.15 (n/a)</td><td>24.74 (n/a)</td><td>23.91 (n/a)</td><td>24.27 (n/a)</td><td>21.89 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>41.07 (+0.91%)</td><td>40.32 (+3.38%)</td><td>40.74 (+4.84%)</td><td>39.12 (+4.12%)</td><td>0.86 <b>(-29.65%)</b></td><td>41.05 (+0.91%)</td><td>40.30 (+3.38%)</td><td>40.72 (+4.84%)</td><td>39.09 (+4.12%)</td><td>0.86 <b>(-29.65%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>40.70 (n/a)</td><td>39.00 (n/a)</td><td>38.86 (n/a)</td><td>37.57 (n/a)</td><td>1.23 (n/a)</td><td>40.68 (n/a)</td><td>38.98 (n/a)</td><td>38.84 (n/a)</td><td>37.55 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>48.41 (+6.71%)</td><td>42.88 (-0.35%)</td><td>42.81 (-1.87%)</td><td>38.98 (+1.94%)</td><td>3.94 <b>(+37.63%)</b></td><td>48.38 (+6.71%)</td><td>42.86 (-0.35%)</td><td>42.78 (-1.87%)</td><td>38.96 (+1.94%)</td><td>3.94 <b>(+37.63%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>45.36 (n/a)</td><td>43.03 (n/a)</td><td>43.63 (n/a)</td><td>38.24 (n/a)</td><td>2.86 (n/a)</td><td>45.34 (n/a)</td><td>43.00 (n/a)</td><td>43.60 (n/a)</td><td>38.22 (n/a)</td><td>2.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.66 (-9.08%)</td><td>8.51 (-2.78%)</td><td>8.53 (-1.03%)</td><td>8.36 (+2.54%)</td><td>0.11 <b>(-81.77%)</b></td><td>8.65 (-9.08%)</td><td>8.49 (-2.78%)</td><td>8.52 (-1.03%)</td><td>8.35 (+2.54%)</td><td>0.11 <b>(-81.77%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>9.53 (n/a)</td><td>8.75 (n/a)</td><td>8.62 (n/a)</td><td>8.16 (n/a)</td><td>0.63 (n/a)</td><td>9.51 (n/a)</td><td>8.73 (n/a)</td><td>8.60 (n/a)</td><td>8.14 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.92 (+0.75%)</td><td>0.84 (-1.34%)</td><td>0.87 (+0.69%)</td><td>0.77 (+5.21%)</td><td>0.06 (-15.73%)</td><td>0.90 (+0.75%)</td><td>0.83 (-1.34%)</td><td>0.86 (+0.69%)</td><td>0.75 (+5.21%)</td><td>0.06 (-15.73%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.91 (n/a)</td><td>0.86 (n/a)</td><td>0.86 (n/a)</td><td>0.73 (n/a)</td><td>0.08 (n/a)</td><td>0.90 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.72 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.38 (+0.07%)</td><td>1.21 (+7.12%)</td><td>1.21 (+16.68%)</td><td>1.12 (+18.77%)</td><td>0.10 <b>(-45.51%)</b></td><td>1.36 (+0.07%)</td><td>1.20 (+7.12%)</td><td>1.19 (+16.68%)</td><td>1.11 (+18.77%)</td><td>0.10 <b>(-45.51%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.38 (n/a)</td><td>1.13 (n/a)</td><td>1.04 (n/a)</td><td>0.95 (n/a)</td><td>0.19 (n/a)</td><td>1.36 (n/a)</td><td>1.12 (n/a)</td><td>1.02 (n/a)</td><td>0.94 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>17.83 (+0.03%)</td><td>16.66 (-0.44%)</td><td>16.62 (+0.86%)</td><td>15.89 (+1.77%)</td><td>0.73 <b>(-29.24%)</b></td><td>17.62 (+0.03%)</td><td>16.47 (-0.44%)</td><td>16.42 (+0.86%)</td><td>15.71 (+1.77%)</td><td>0.72 <b>(-29.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>17.83 (n/a)</td><td>16.73 (n/a)</td><td>16.47 (n/a)</td><td>15.62 (n/a)</td><td>1.03 (n/a)</td><td>17.62 (n/a)</td><td>16.54 (n/a)</td><td>16.28 (n/a)</td><td>15.44 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.96 (+2.05%)</td><td>13.53 (+0.03%)</td><td>13.47 (-1.18%)</td><td>13.21 (+0.04%)</td><td>0.28 <b>(+32.44%)</b></td><td>13.72 (+2.05%)</td><td>13.29 (+0.03%)</td><td>13.24 (-1.18%)</td><td>12.97 (+0.04%)</td><td>0.27 <b>(+32.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.68 (n/a)</td><td>13.52 (n/a)</td><td>13.63 (n/a)</td><td>13.20 (n/a)</td><td>0.21 (n/a)</td><td>13.44 (n/a)</td><td>13.28 (n/a)</td><td>13.39 (n/a)</td><td>12.97 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>10.09 (+11.02%)</td><td>8.53 (+17.98%)</td><td>8.06 (+12.83%)</td><td>7.57 <b>(+36.56%)</b></td><td>1.12 (-10.61%)</td><td>9.91 (+11.02%)</td><td>8.39 (+17.98%)</td><td>7.92 (+12.83%)</td><td>7.44 <b>(+36.56%)</b></td><td>1.10 (-10.61%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>9.08 (n/a)</td><td>7.23 (n/a)</td><td>7.14 (n/a)</td><td>5.54 (n/a)</td><td>1.26 (n/a)</td><td>8.93 (n/a)</td><td>7.11 (n/a)</td><td>7.02 (n/a)</td><td>5.45 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.83 (+1.69%)</td><td>5.33 (-1.03%)</td><td>5.51 (+0.70%)</td><td>4.66 (-3.50%)</td><td>0.45 <b>(+32.91%)</b></td><td>5.74 (+1.69%)</td><td>5.25 (-1.03%)</td><td>5.42 (+0.70%)</td><td>4.59 (-3.50%)</td><td>0.44 <b>(+32.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.73 (n/a)</td><td>5.39 (n/a)</td><td>5.47 (n/a)</td><td>4.83 (n/a)</td><td>0.34 (n/a)</td><td>5.64 (n/a)</td><td>5.30 (n/a)</td><td>5.38 (n/a)</td><td>4.75 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.14 (n/a)</td><td>11.93 (n/a)</td><td>11.55 (n/a)</td><td>11.17 (n/a)</td><td>0.86 (n/a)</td><td>13.14 (n/a)</td><td>11.92 (n/a)</td><td>11.54 (n/a)</td><td>11.16 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.13 (n/a)</td><td>11.99 (n/a)</td><td>12.41 (n/a)</td><td>10.86 (n/a)</td><td>0.99 (n/a)</td><td>13.12 (n/a)</td><td>11.98 (n/a)</td><td>12.40 (n/a)</td><td>10.85 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>263.20 (n/a)</td><td>193.00 (n/a)</td><td>172.60 (n/a)</td><td>141.10 (n/a)</td><td>48.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.00 (n/a)</td><td>195.84 (n/a)</td><td>183.90 (n/a)</td><td>167.60 (n/a)</td><td>32.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.20 (n/a)</td><td>188.70 (n/a)</td><td>187.80 (n/a)</td><td>161.70 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>179.90 (n/a)</td><td>184.00 (n/a)</td><td>118.20 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>190.56 (n/a)</td><td>188.90 (n/a)</td><td>131.30 (n/a)</td><td>40.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>324.90 (n/a)</td><td>229.26 (n/a)</td><td>213.40 (n/a)</td><td>176.20 (n/a)</td><td>58.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>173.80 (n/a)</td><td>159.30 (n/a)</td><td>133.70 (n/a)</td><td>41.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>325.20 (n/a)</td><td>223.22 (n/a)</td><td>218.80 (n/a)</td><td>137.70 (n/a)</td><td>67.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.50 (n/a)</td><td>202.92 (n/a)</td><td>202.50 (n/a)</td><td>140.30 (n/a)</td><td>59.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.60 (n/a)</td><td>178.46 (n/a)</td><td>167.30 (n/a)</td><td>143.70 (n/a)</td><td>39.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.10 (n/a)</td><td>139.42 (n/a)</td><td>128.40 (n/a)</td><td>126.50 (n/a)</td><td>17.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.40 (n/a)</td><td>210.76 (n/a)</td><td>225.00 (n/a)</td><td>163.30 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>190.84 (n/a)</td><td>186.70 (n/a)</td><td>147.40 (n/a)</td><td>43.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.40 (n/a)</td><td>187.50 (n/a)</td><td>181.20 (n/a)</td><td>172.60 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>312.20 (n/a)</td><td>223.52 (n/a)</td><td>206.60 (n/a)</td><td>175.50 (n/a)</td><td>55.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>340.60 (n/a)</td><td>267.08 (n/a)</td><td>269.90 (n/a)</td><td>159.90 (n/a)</td><td>74.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>183.46 (n/a)</td><td>179.70 (n/a)</td><td>160.80 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.60 (n/a)</td><td>193.42 (n/a)</td><td>200.40 (n/a)</td><td>136.70 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>186.30 (n/a)</td><td>186.90 (n/a)</td><td>171.40 (n/a)</td><td>10.83 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>165.58 (n/a)</td><td>175.10 (n/a)</td><td>129.50 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>194.94 (n/a)</td><td>190.60 (n/a)</td><td>170.80 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>303.50 (n/a)</td><td>216.24 (n/a)</td><td>181.10 (n/a)</td><td>133.60 (n/a)</td><td>76.75 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>295.60 (n/a)</td><td>223.78 (n/a)</td><td>217.60 (n/a)</td><td>168.90 (n/a)</td><td>56.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>328.20 (n/a)</td><td>239.16 (n/a)</td><td>229.50 (n/a)</td><td>178.40 (n/a)</td><td>54.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>192.70 (n/a)</td><td>190.40 (n/a)</td><td>174.20 (n/a)</td><td>15.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>200.50 (n/a)</td><td>175.94 (n/a)</td><td>186.30 (n/a)</td><td>120.50 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>248.50 (n/a)</td><td>193.88 (n/a)</td><td>193.90 (n/a)</td><td>154.50 (n/a)</td><td>38.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>270.40 (n/a)</td><td>220.02 (n/a)</td><td>211.20 (n/a)</td><td>196.20 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>271.80 (n/a)</td><td>220.16 (n/a)</td><td>217.10 (n/a)</td><td>158.60 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>302.10 (n/a)</td><td>241.08 (n/a)</td><td>225.00 (n/a)</td><td>187.00 (n/a)</td><td>45.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>249.30 (n/a)</td><td>205.16 (n/a)</td><td>208.50 (n/a)</td><td>171.30 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>340.50 (n/a)</td><td>246.54 (n/a)</td><td>237.70 (n/a)</td><td>191.30 (n/a)</td><td>56.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(+32.08%)</b></td><td>0.03 <b>(+30.79%)</b></td><td>0.03 <b>(+24.02%)</b></td><td>0.02 <b>(+57.11%)</b></td><td>0.00 (-7.65%)</td><td>184.50 <b>(-36.36%)</b></td><td>150.74 <b>(-25.50%)</b></td><td>144.10 (-19.36%)</td><td>122.60 <b>(-24.27%)</b></td><td>23.05 <b>(-55.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>289.90 (n/a)</td><td>202.34 (n/a)</td><td>178.70 (n/a)</td><td>161.90 (n/a)</td><td>52.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-1.10%)</td><td>0.03 (-2.94%)</td><td>0.03 (+2.19%)</td><td>0.02 (-1.92%)</td><td>0.00 (-16.29%)</td><td>202.90 (+1.96%)</td><td>166.18 (+2.10%)</td><td>162.30 (-2.17%)</td><td>127.80 (+1.11%)</td><td>27.15 (-14.33%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>162.76 (n/a)</td><td>165.90 (n/a)</td><td>126.40 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+4.70%)</td><td>0.03 (+5.49%)</td><td>0.03 (+11.61%)</td><td>0.02 (+13.53%)</td><td>0.01 (-5.00%)</td><td>175.90 (-11.92%)</td><td>156.18 (-5.89%)</td><td>160.20 (-10.40%)</td><td>114.70 (-4.50%)</td><td>24.54 <b>(-20.07%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>165.96 (n/a)</td><td>178.80 (n/a)</td><td>120.10 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-2.33%)</td><td>0.02 (-5.25%)</td><td>0.02 (-8.52%)</td><td>0.02 <b>(-26.23%)</b></td><td>0.01 <b>(+27.17%)</b></td><td>262.00 <b>(+35.54%)</b></td><td>177.82 (+9.20%)</td><td>177.50 (+9.30%)</td><td>123.60 (+2.32%)</td><td>52.66 <b>(+77.41%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>162.84 (n/a)</td><td>162.40 (n/a)</td><td>120.80 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(-23.05%)</b></td><td>0.02 (-16.20%)</td><td>0.02 (-14.31%)</td><td>0.02 (-9.85%)</td><td>0.00 <b>(-51.16%)</b></td><td>224.60 (+10.91%)</td><td>182.52 (+15.04%)</td><td>179.70 (+16.69%)</td><td>147.60 <b>(+29.93%)</b></td><td>28.47 <b>(-31.11%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>158.66 (n/a)</td><td>154.00 (n/a)</td><td>113.60 (n/a)</td><td>41.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+1.67%)</td><td>0.02 (+9.79%)</td><td>0.02 (+2.12%)</td><td>0.02 (+19.43%)</td><td>0.00 <b>(-25.50%)</b></td><td>252.60 (-16.27%)</td><td>189.74 (-12.24%)</td><td>171.60 (-2.11%)</td><td>157.50 (-1.69%)</td><td>39.92 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>301.70 (n/a)</td><td>216.20 (n/a)</td><td>175.30 (n/a)</td><td>160.20 (n/a)</td><td>65.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+2.63%)</td><td>0.02 (-11.88%)</td><td>0.02 (-17.35%)</td><td>0.02 (-19.67%)</td><td>0.01 <b>(+36.45%)</b></td><td>268.10 <b>(+24.52%)</b></td><td>200.80 (+17.28%)</td><td>204.40 <b>(+21.02%)</b></td><td>123.70 (-2.60%)</td><td>51.27 <b>(+58.47%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.30 (n/a)</td><td>171.22 (n/a)</td><td>168.90 (n/a)</td><td>127.00 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(+28.69%)</b></td><td>0.02 <b>(+21.09%)</b></td><td>0.02 (+14.02%)</td><td>0.02 <b>(+26.54%)</b></td><td>0.00 <b>(+47.45%)</b></td><td>206.80 <b>(-20.98%)</b></td><td>186.78 (-17.21%)</td><td>190.50 (-12.29%)</td><td>160.60 <b>(-22.27%)</b></td><td>19.97 (-9.67%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>261.70 (n/a)</td><td>225.62 (n/a)</td><td>217.20 (n/a)</td><td>206.60 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-2.47%)</td><td>0.05 (-15.16%)</td><td>0.05 (-8.97%)</td><td>0.03 <b>(-37.39%)</b></td><td>0.01 <b>(+148.79%)</b></td><td>243.00 <b>(+59.66%)</b></td><td>169.98 <b>(+23.46%)</b></td><td>149.20 (+9.87%)</td><td>128.80 (+2.55%)</td><td>46.18 <b>(+312.36%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>152.20 (n/a)</td><td>137.68 (n/a)</td><td>135.80 (n/a)</td><td>125.60 (n/a)</td><td>11.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (+14.71%)</td><td>0.05 (+15.02%)</td><td>0.04 (+5.17%)</td><td>0.04 (+6.91%)</td><td>0.01 <b>(+52.31%)</b></td><td>204.70 (-6.49%)</td><td>169.04 (-11.69%)</td><td>182.20 (-4.91%)</td><td>129.50 (-12.85%)</td><td>33.34 <b>(+25.22%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>191.42 (n/a)</td><td>191.60 (n/a)</td><td>148.60 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 <b>(-34.80%)</b></td><td>0.04 (-14.02%)</td><td>0.04 (+1.85%)</td><td>0.03 (-17.77%)</td><td>0.00 <b>(-60.62%)</b></td><td>243.90 <b>(+21.65%)</b></td><td>199.84 (+13.40%)</td><td>189.80 (-1.81%)</td><td>184.80 <b>(+53.36%)</b></td><td>25.00 <b>(-24.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>176.22 (n/a)</td><td>193.30 (n/a)</td><td>120.50 (n/a)</td><td>33.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (+6.65%)</td><td>0.05 (-0.02%)</td><td>0.05 (-8.45%)</td><td>0.04 (+8.23%)</td><td>0.00 (-9.24%)</td><td>184.40 (-7.62%)</td><td>174.60 (-0.23%)</td><td>179.50 (+9.18%)</td><td>150.10 (-6.25%)</td><td>13.88 <b>(-22.10%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.60 (n/a)</td><td>175.00 (n/a)</td><td>164.40 (n/a)</td><td>160.10 (n/a)</td><td>17.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-1.80%)</td><td>0.05 (+5.52%)</td><td>0.05 (+7.43%)</td><td>0.04 <b>(+20.17%)</b></td><td>0.00 <b>(-44.87%)</b></td><td>187.90 (-16.78%)</td><td>169.68 (-6.99%)</td><td>170.70 (-6.87%)</td><td>148.20 (+1.79%)</td><td>15.26 <b>(-52.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>182.44 (n/a)</td><td>183.30 (n/a)</td><td>145.60 (n/a)</td><td>32.45 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (-1.66%)</td><td>0.05 (+3.10%)</td><td>0.05 (-2.96%)</td><td>0.02 (+12.39%)</td><td>0.02 (-1.16%)</td><td>344.70 (-11.02%)</td><td>199.04 (-5.08%)</td><td>179.30 (+3.05%)</td><td>123.50 (+1.65%)</td><td>88.60 (-15.26%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>387.40 (n/a)</td><td>209.70 (n/a)</td><td>174.00 (n/a)</td><td>121.50 (n/a)</td><td>104.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (+3.17%)</td><td>0.05 (-0.51%)</td><td>0.05 (-4.25%)</td><td>0.04 (+0.92%)</td><td>0.01 (+10.19%)</td><td>201.70 (-0.93%)</td><td>172.02 (+0.76%)</td><td>175.50 (+4.40%)</td><td>130.00 (-3.06%)</td><td>25.98 (+3.49%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>170.72 (n/a)</td><td>168.10 (n/a)</td><td>134.10 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (+11.37%)</td><td>0.05 (+6.68%)</td><td>0.04 (-6.31%)</td><td>0.04 <b>(+24.13%)</b></td><td>0.01 (+0.25%)</td><td>199.50 (-19.43%)</td><td>173.38 (-7.03%)</td><td>185.20 (+6.74%)</td><td>136.10 (-10.22%)</td><td>29.19 <b>(-26.25%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.60 (n/a)</td><td>186.50 (n/a)</td><td>173.50 (n/a)</td><td>151.60 (n/a)</td><td>39.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (+8.52%)</td><td>0.04 (-3.45%)</td><td>0.05 (+5.93%)</td><td>0.02 <b>(-38.10%)</b></td><td>0.01 <b>(+191.65%)</b></td><td>341.90 <b>(+61.58%)</b></td><td>207.26 (+11.27%)</td><td>174.90 (-5.61%)</td><td>156.60 (-7.88%)</td><td>76.23 <b>(+361.39%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.60 (n/a)</td><td>186.26 (n/a)</td><td>185.30 (n/a)</td><td>170.00 (n/a)</td><td>16.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (+2.91%)</td><td>0.04 (-5.18%)</td><td>0.04 (-12.17%)</td><td>0.03 (-8.75%)</td><td>0.01 <b>(+57.62%)</b></td><td>236.60 (+9.59%)</td><td>208.20 (+6.66%)</td><td>219.90 (+13.88%)</td><td>165.80 (-2.87%)</td><td>30.16 <b>(+68.21%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.90 (n/a)</td><td>195.20 (n/a)</td><td>193.10 (n/a)</td><td>170.70 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (+10.25%)</td><td>0.09 (-6.20%)</td><td>0.08 (-15.28%)</td><td>0.08 (-10.02%)</td><td>0.02 <b>(+83.47%)</b></td><td>216.80 (+11.12%)</td><td>183.16 (+8.46%)</td><td>194.00 (+18.08%)</td><td>139.20 (-9.32%)</td><td>30.69 <b>(+82.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>168.88 (n/a)</td><td>164.30 (n/a)</td><td>153.50 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-1.56%)</td><td>0.11 (+3.30%)</td><td>0.11 (+6.31%)</td><td>0.09 (+7.61%)</td><td>0.02 <b>(-23.87%)</b></td><td>185.60 (-7.06%)</td><td>157.00 (-4.84%)</td><td>154.60 (-5.96%)</td><td>122.00 (+1.58%)</td><td>23.34 <b>(-31.11%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.70 (n/a)</td><td>164.98 (n/a)</td><td>164.40 (n/a)</td><td>120.10 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (-10.52%)</td><td>0.09 (-4.50%)</td><td>0.09 (+2.87%)</td><td>0.08 (-7.79%)</td><td>0.01 <b>(-21.41%)</b></td><td>208.70 (+8.42%)</td><td>183.42 (+4.28%)</td><td>181.70 (-2.78%)</td><td>153.00 (+11.76%)</td><td>22.47 (-3.88%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>175.90 (n/a)</td><td>186.90 (n/a)</td><td>136.90 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-11.56%)</td><td>0.09 (-11.26%)</td><td>0.08 <b>(-23.84%)</b></td><td>0.08 (+11.13%)</td><td>0.02 <b>(-34.60%)</b></td><td>211.60 (-10.00%)</td><td>184.72 (+8.75%)</td><td>206.50 <b>(+31.28%)</b></td><td>138.20 (+13.09%)</td><td>34.24 <b>(-30.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>235.10 (n/a)</td><td>169.86 (n/a)</td><td>157.30 (n/a)</td><td>122.20 (n/a)</td><td>49.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-9.97%)</td><td>0.09 <b>(-20.13%)</b></td><td>0.09 <b>(-31.62%)</b></td><td>0.08 (+3.03%)</td><td>0.02 <b>(-30.33%)</b></td><td>200.10 (-2.96%)</td><td>177.26 <b>(+22.74%)</b></td><td>187.40 <b>(+46.29%)</b></td><td>132.80 (+11.13%)</td><td>26.13 <b>(-27.83%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>144.42 (n/a)</td><td>128.10 (n/a)</td><td>119.50 (n/a)</td><td>36.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (+16.59%)</td><td>0.09 (+1.08%)</td><td>0.08 (-18.18%)</td><td>0.07 <b>(+37.90%)</b></td><td>0.02 (-15.13%)</td><td>220.70 <b>(-27.47%)</b></td><td>189.38 (-4.47%)</td><td>198.90 <b>(+22.17%)</b></td><td>135.90 (-14.26%)</td><td>32.46 <b>(-48.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>304.30 (n/a)</td><td>198.24 (n/a)</td><td>162.80 (n/a)</td><td>158.50 (n/a)</td><td>62.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 <b>(-29.43%)</b></td><td>0.09 (-15.61%)</td><td>0.09 (-12.54%)</td><td>0.07 (-4.43%)</td><td>0.01 <b>(-64.74%)</b></td><td>218.50 (+4.65%)</td><td>192.76 (+15.86%)</td><td>187.10 (+14.29%)</td><td>178.40 <b>(+41.70%)</b></td><td>16.19 <b>(-47.20%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.80 (n/a)</td><td>166.38 (n/a)</td><td>163.70 (n/a)</td><td>125.90 (n/a)</td><td>30.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (-14.92%)</td><td>0.08 (-2.51%)</td><td>0.07 (-1.70%)</td><td>0.05 (+0.03%)</td><td>0.02 <b>(-24.17%)</b></td><td>308.60 (-0.03%)</td><td>227.14 (+0.86%)</td><td>231.50 (+1.71%)</td><td>171.00 (+17.53%)</td><td>53.27 (-8.67%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>308.70 (n/a)</td><td>225.20 (n/a)</td><td>227.60 (n/a)</td><td>145.50 (n/a)</td><td>58.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (-1.77%)</td><td>0.18 (-10.91%)</td><td>0.17 (-8.45%)</td><td>0.13 <b>(-28.33%)</b></td><td>0.04 <b>(+47.75%)</b></td><td>251.60 <b>(+39.55%)</b></td><td>189.22 (+15.70%)</td><td>189.10 (+9.24%)</td><td>131.70 (+1.86%)</td><td>44.24 <b>(+107.99%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>180.30 (n/a)</td><td>163.54 (n/a)</td><td>173.10 (n/a)</td><td>129.30 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (-0.75%)</td><td>0.20 (-10.14%)</td><td>0.18 (-16.28%)</td><td>0.18 (-4.51%)</td><td>0.03 (+14.77%)</td><td>184.50 (+4.71%)</td><td>168.66 (+11.81%)</td><td>179.50 (+19.43%)</td><td>128.80 (+0.78%)</td><td>22.91 (+19.06%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.20 (n/a)</td><td>150.84 (n/a)</td><td>150.30 (n/a)</td><td>127.80 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (-15.19%)</td><td>0.21 (-2.73%)</td><td>0.21 (+9.24%)</td><td>0.17 (-6.98%)</td><td>0.02 <b>(-37.54%)</b></td><td>190.10 (+7.52%)</td><td>158.38 (+1.89%)</td><td>152.80 (-8.45%)</td><td>143.50 (+17.91%)</td><td>18.24 (-18.13%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.80 (n/a)</td><td>155.44 (n/a)</td><td>166.90 (n/a)</td><td>121.70 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (-10.38%)</td><td>0.23 (+12.42%)</td><td>0.23 <b>(+34.49%)</b></td><td>0.17 <b>(+25.45%)</b></td><td>0.04 <b>(-31.68%)</b></td><td>188.60 <b>(-20.29%)</b></td><td>149.62 (-14.64%)</td><td>140.80 <b>(-25.62%)</b></td><td>122.30 (+11.59%)</td><td>30.24 <b>(-39.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>236.60 (n/a)</td><td>175.28 (n/a)</td><td>189.30 (n/a)</td><td>109.60 (n/a)</td><td>49.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (+1.04%)</td><td>0.17 (+6.05%)</td><td>0.15 (+5.16%)</td><td>0.11 <b>(-20.81%)</b></td><td>0.05 <b>(+41.49%)</b></td><td>304.90 <b>(+26.30%)</b></td><td>208.00 (-1.73%)</td><td>213.70 (-4.90%)</td><td>148.00 (-1.00%)</td><td>64.10 <b>(+71.95%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>241.40 (n/a)</td><td>211.66 (n/a)</td><td>224.70 (n/a)</td><td>149.50 (n/a)</td><td>37.28 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 <b>(+24.31%)</b></td><td>0.18 (+3.08%)</td><td>0.19 (+3.37%)</td><td>0.12 (-15.38%)</td><td>0.04 <b>(+110.64%)</b></td><td>274.10 (+18.20%)</td><td>190.42 (+0.59%)</td><td>175.60 (-3.25%)</td><td>139.90 (-19.55%)</td><td>50.07 <b>(+106.53%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>231.90 (n/a)</td><td>189.30 (n/a)</td><td>181.50 (n/a)</td><td>173.90 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (+18.65%)</td><td>0.16 (+2.38%)</td><td>0.16 (+2.59%)</td><td>0.11 <b>(-22.60%)</b></td><td>0.03 <b>(+296.10%)</b></td><td>301.80 <b>(+29.20%)</b></td><td>217.78 (+1.09%)</td><td>203.70 (-2.54%)</td><td>174.80 (-15.72%)</td><td>50.33 <b>(+342.63%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>215.44 (n/a)</td><td>209.00 (n/a)</td><td>207.40 (n/a)</td><td>11.37 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+16.94%)</td><td>0.03 (+1.62%)</td><td>0.02 (-7.57%)</td><td>0.02 (-5.56%)</td><td>0.01 <b>(+168.18%)</b></td><td>199.60 (+5.89%)</td><td>168.14 (+1.19%)</td><td>177.00 (+8.19%)</td><td>129.30 (-14.48%)</td><td>33.13 <b>(+140.77%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.50 (n/a)</td><td>166.16 (n/a)</td><td>163.60 (n/a)</td><td>151.20 (n/a)</td><td>13.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-3.83%)</td><td>0.03 (-2.36%)</td><td>0.03 (-3.71%)</td><td>0.02 (-1.22%)</td><td>0.00 <b>(-23.27%)</b></td><td>195.10 (+1.25%)</td><td>163.64 (+1.68%)</td><td>163.00 (+3.89%)</td><td>139.20 (+3.96%)</td><td>20.63 (-18.54%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>160.94 (n/a)</td><td>156.90 (n/a)</td><td>133.90 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (-1.06%)</td><td>0.02 (-2.38%)</td><td>0.02 (-2.04%)</td><td>0.02 (-8.36%)</td><td>0.00 <b>(+28.66%)</b></td><td>232.90 (+9.14%)</td><td>196.04 (+3.05%)</td><td>194.80 (+2.10%)</td><td>166.00 (+1.03%)</td><td>25.16 <b>(+44.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>190.24 (n/a)</td><td>190.80 (n/a)</td><td>164.30 (n/a)</td><td>17.45 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+7.12%)</td><td>0.02 (-5.66%)</td><td>0.02 (-8.39%)</td><td>0.02 (-16.75%)</td><td>0.00 <b>(+142.64%)</b></td><td>242.50 <b>(+20.11%)</b></td><td>203.80 (+7.80%)</td><td>212.20 (+9.16%)</td><td>162.00 (-6.63%)</td><td>31.43 <b>(+170.25%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>189.06 (n/a)</td><td>194.40 (n/a)</td><td>173.50 (n/a)</td><td>11.63 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+17.88%)</td><td>0.03 (+17.69%)</td><td>0.03 (+4.58%)</td><td>0.02 <b>(+84.96%)</b></td><td>0.00 <b>(-25.32%)</b></td><td>190.60 <b>(-45.93%)</b></td><td>159.58 <b>(-21.09%)</b></td><td>154.60 (-4.39%)</td><td>125.40 (-15.21%)</td><td>28.71 <b>(-66.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>352.50 (n/a)</td><td>202.22 (n/a)</td><td>161.70 (n/a)</td><td>147.90 (n/a)</td><td>85.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-5.83%)</td><td>0.03 (+1.78%)</td><td>0.03 (+6.64%)</td><td>0.02 (+13.70%)</td><td>0.00 <b>(-35.55%)</b></td><td>205.00 (-12.02%)</td><td>162.18 (-4.23%)</td><td>159.60 (-6.23%)</td><td>139.70 (+6.16%)</td><td>25.74 <b>(-37.40%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>169.34 (n/a)</td><td>170.20 (n/a)</td><td>131.60 (n/a)</td><td>41.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-8.46%)</td><td>0.02 (-9.15%)</td><td>0.02 (-4.36%)</td><td>0.02 (-1.31%)</td><td>0.00 (-5.45%)</td><td>229.80 (+1.32%)</td><td>185.12 (+9.98%)</td><td>166.50 (+4.59%)</td><td>151.80 (+9.29%)</td><td>34.22 (+1.19%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.80 (n/a)</td><td>168.32 (n/a)</td><td>159.20 (n/a)</td><td>138.90 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-14.70%)</td><td>0.02 (-15.40%)</td><td>0.02 <b>(-20.99%)</b></td><td>0.02 (-12.58%)</td><td>0.00 <b>(-28.21%)</b></td><td>198.90 (+14.38%)</td><td>172.84 (+17.74%)</td><td>175.10 <b>(+26.61%)</b></td><td>150.70 (+17.28%)</td><td>18.10 (-4.17%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.90 (n/a)</td><td>146.80 (n/a)</td><td>138.30 (n/a)</td><td>128.50 (n/a)</td><td>18.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(-21.54%)</b></td><td>0.02 <b>(-30.44%)</b></td><td>0.02 <b>(-37.04%)</b></td><td>0.02 <b>(-35.79%)</b></td><td>0.00 (+17.49%)</td><td>256.00 <b>(+55.72%)</b></td><td>208.20 <b>(+47.22%)</b></td><td>227.20 <b>(+58.88%)</b></td><td>154.90 <b>(+27.49%)</b></td><td>43.32 <b>(+133.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.40 (n/a)</td><td>141.42 (n/a)</td><td>143.00 (n/a)</td><td>121.50 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+16.56%)</td><td>0.02 (-2.19%)</td><td>0.02 (-10.01%)</td><td>0.02 (-12.08%)</td><td>0.00 <b>(+211.81%)</b></td><td>209.70 (+13.72%)</td><td>176.76 (+4.72%)</td><td>183.00 (+11.11%)</td><td>136.30 (-14.22%)</td><td>31.36 <b>(+204.41%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.40 (n/a)</td><td>168.80 (n/a)</td><td>164.70 (n/a)</td><td>158.90 (n/a)</td><td>10.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 <b>(+31.82%)</b></td><td>0.03 (+10.83%)</td><td>0.02 (-7.74%)</td><td>0.02 (+11.95%)</td><td>0.01 <b>(+50.33%)</b></td><td>203.30 (-10.68%)</td><td>157.50 (-8.41%)</td><td>165.40 (+8.39%)</td><td>108.40 <b>(-24.14%)</b></td><td>36.13 (+0.59%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.60 (n/a)</td><td>171.96 (n/a)</td><td>152.60 (n/a)</td><td>142.90 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-10.26%)</td><td>0.02 (-14.70%)</td><td>0.02 <b>(-20.47%)</b></td><td>0.02 (-17.26%)</td><td>0.00 <b>(+30.09%)</b></td><td>216.30 <b>(+20.84%)</b></td><td>175.78 (+18.98%)</td><td>179.90 <b>(+25.72%)</b></td><td>142.90 (+11.47%)</td><td>32.46 <b>(+66.44%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.00 (n/a)</td><td>147.74 (n/a)</td><td>143.10 (n/a)</td><td>128.20 (n/a)</td><td>19.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(+39.65%)</b></td><td>0.02 (+11.39%)</td><td>0.02 (+14.03%)</td><td>0.01 (-15.27%)</td><td>0.01 <b>(+148.18%)</b></td><td>295.50 (+18.01%)</td><td>197.44 (-4.60%)</td><td>185.40 (-12.30%)</td><td>126.30 <b>(-28.40%)</b></td><td>62.57 <b>(+113.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.40 (n/a)</td><td>206.96 (n/a)</td><td>211.40 (n/a)</td><td>176.40 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-3.46%)</td><td>0.03 (-7.33%)</td><td>0.03 (-12.77%)</td><td>0.02 (+7.68%)</td><td>0.00 (-17.91%)</td><td>213.80 (-7.12%)</td><td>167.08 (+6.23%)</td><td>161.70 (+14.60%)</td><td>135.90 (+3.58%)</td><td>31.04 <b>(-24.35%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>157.28 (n/a)</td><td>141.10 (n/a)</td><td>131.20 (n/a)</td><td>41.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+3.82%)</td><td>0.02 (-2.19%)</td><td>0.02 (-9.68%)</td><td>0.02 (+4.21%)</td><td>0.00 (-5.68%)</td><td>241.90 (-4.05%)</td><td>191.68 (+1.71%)</td><td>192.80 (+10.68%)</td><td>153.80 (-3.69%)</td><td>33.31 (-12.78%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.10 (n/a)</td><td>188.46 (n/a)</td><td>174.20 (n/a)</td><td>159.70 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (+3.83%)</td><td>0.02 (-3.68%)</td><td>0.02 (-11.19%)</td><td>0.02 (-9.27%)</td><td>0.00 <b>(+70.04%)</b></td><td>218.90 (+10.22%)</td><td>177.74 (+5.27%)</td><td>184.80 (+12.55%)</td><td>149.00 (-3.68%)</td><td>29.22 <b>(+70.68%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.60 (n/a)</td><td>168.84 (n/a)</td><td>164.20 (n/a)</td><td>154.70 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-18.62%)</td><td>0.04 (-16.51%)</td><td>0.04 <b>(-26.18%)</b></td><td>0.04 (-14.03%)</td><td>0.01 (-18.38%)</td><td>218.60 (+16.28%)</td><td>188.12 (+19.49%)</td><td>206.30 <b>(+35.46%)</b></td><td>153.90 <b>(+22.92%)</b></td><td>31.13 (+10.75%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>157.44 (n/a)</td><td>152.30 (n/a)</td><td>125.20 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (+17.57%)</td><td>0.05 (+11.04%)</td><td>0.05 (+8.25%)</td><td>0.05 (+6.61%)</td><td>0.01 <b>(+43.70%)</b></td><td>177.40 (-6.19%)</td><td>154.38 (-9.38%)</td><td>160.50 (-7.60%)</td><td>127.10 (-14.93%)</td><td>21.09 (+14.35%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>170.36 (n/a)</td><td>173.70 (n/a)</td><td>149.40 (n/a)</td><td>18.44 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-1.34%)</td><td>0.04 (-12.45%)</td><td>0.04 (-11.84%)</td><td>0.02 <b>(-41.55%)</b></td><td>0.01 <b>(+77.51%)</b></td><td>385.90 <b>(+71.05%)</b></td><td>234.52 <b>(+22.76%)</b></td><td>218.10 (+13.42%)</td><td>161.80 (+1.38%)</td><td>88.40 <b>(+224.63%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>191.04 (n/a)</td><td>192.30 (n/a)</td><td>159.60 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (+0.25%)</td><td>0.04 (-11.99%)</td><td>0.04 <b>(-21.34%)</b></td><td>0.03 (-12.52%)</td><td>0.01 <b>(+29.15%)</b></td><td>253.20 (+14.31%)</td><td>219.70 (+14.45%)</td><td>230.00 <b>(+27.14%)</b></td><td>174.70 (-0.29%)</td><td>29.64 <b>(+45.57%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.50 (n/a)</td><td>191.96 (n/a)</td><td>180.90 (n/a)</td><td>175.20 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-6.12%)</td><td>0.04 (+2.91%)</td><td>0.04 (-2.96%)</td><td>0.04 (+15.97%)</td><td>0.00 <b>(-43.83%)</b></td><td>228.80 (-13.79%)</td><td>191.60 (-5.32%)</td><td>183.00 (+3.04%)</td><td>170.20 (+6.51%)</td><td>23.14 <b>(-48.36%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.40 (n/a)</td><td>202.36 (n/a)</td><td>177.60 (n/a)</td><td>159.80 (n/a)</td><td>44.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-12.05%)</td><td>0.04 (-17.37%)</td><td>0.05 (-13.14%)</td><td>0.04 <b>(-20.90%)</b></td><td>0.01 (+5.69%)</td><td>225.60 <b>(+26.39%)</b></td><td>189.26 <b>(+22.18%)</b></td><td>177.10 (+15.15%)</td><td>149.90 (+13.73%)</td><td>32.75 <b>(+56.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.50 (n/a)</td><td>154.90 (n/a)</td><td>153.80 (n/a)</td><td>131.80 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (+18.99%)</td><td>0.05 (+0.42%)</td><td>0.04 (-4.75%)</td><td>0.04 (-10.16%)</td><td>0.01 <b>(+776.62%)</b></td><td>201.80 (+11.31%)</td><td>180.92 (+1.08%)</td><td>189.20 (+4.99%)</td><td>146.40 (-16.01%)</td><td>24.17 <b>(+733.66%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.30 (n/a)</td><td>178.98 (n/a)</td><td>180.20 (n/a)</td><td>174.30 (n/a)</td><td>2.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (+9.76%)</td><td>0.04 (+0.01%)</td><td>0.05 (+6.88%)</td><td>0.02 (-3.56%)</td><td>0.02 <b>(+21.31%)</b></td><td>383.90 (+3.67%)</td><td>216.46 (+3.27%)</td><td>168.90 (-6.43%)</td><td>130.10 (-8.89%)</td><td>101.48 (+10.67%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>370.30 (n/a)</td><td>209.60 (n/a)</td><td>180.50 (n/a)</td><td>142.80 (n/a)</td><td>91.69 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-2.04%)</td><td>0.05 (+1.65%)</td><td>0.05 (+4.16%)</td><td>0.05 (+9.78%)</td><td>0.00 <b>(-47.35%)</b></td><td>174.10 (-8.90%)</td><td>160.68 (-2.44%)</td><td>160.50 (-4.01%)</td><td>147.10 (+2.08%)</td><td>9.76 <b>(-50.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>164.70 (n/a)</td><td>167.20 (n/a)</td><td>144.10 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-7.24%)</td><td>0.05 (+3.99%)</td><td>0.05 (-2.13%)</td><td>0.05 <b>(+42.12%)</b></td><td>0.00 <b>(-54.25%)</b></td><td>178.10 <b>(-29.63%)</b></td><td>162.00 (-7.56%)</td><td>166.60 (+2.15%)</td><td>143.00 (+7.84%)</td><td>15.35 <b>(-66.82%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.10 (n/a)</td><td>175.24 (n/a)</td><td>163.10 (n/a)</td><td>132.60 (n/a)</td><td>46.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-6.51%)</td><td>0.04 (-14.15%)</td><td>0.05 (-1.99%)</td><td>0.02 <b>(-44.91%)</b></td><td>0.01 <b>(+70.35%)</b></td><td>357.10 <b>(+81.45%)</b></td><td>210.10 <b>(+25.78%)</b></td><td>178.00 (+2.01%)</td><td>151.70 (+6.98%)</td><td>84.09 <b>(+257.10%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>167.04 (n/a)</td><td>174.50 (n/a)</td><td>141.80 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-6.47%)</td><td>0.05 (-2.04%)</td><td>0.05 (-6.33%)</td><td>0.04 (+18.46%)</td><td>0.01 <b>(-36.33%)</b></td><td>183.80 (-15.61%)</td><td>163.36 (-0.35%)</td><td>166.40 (+6.80%)</td><td>130.60 (+6.87%)</td><td>20.29 <b>(-44.21%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>163.94 (n/a)</td><td>155.80 (n/a)</td><td>122.20 (n/a)</td><td>36.37 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-0.96%)</td><td>0.04 (-5.40%)</td><td>0.05 (-2.37%)</td><td>0.02 (-9.66%)</td><td>0.01 (+10.16%)</td><td>355.80 (+10.70%)</td><td>207.16 (+8.42%)</td><td>175.60 (+2.45%)</td><td>131.90 (+1.00%)</td><td>88.73 (+18.62%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.40 (n/a)</td><td>191.08 (n/a)</td><td>171.40 (n/a)</td><td>130.60 (n/a)</td><td>74.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 <b>(+24.22%)</b></td><td>0.05 (-7.11%)</td><td>0.04 (-16.08%)</td><td>0.03 <b>(-43.18%)</b></td><td>0.02 <b>(+620.60%)</b></td><td>294.40 <b>(+75.97%)</b></td><td>186.72 (+17.82%)</td><td>186.70 (+19.22%)</td><td>121.30 (-19.46%)</td><td>66.98 <b>(+925.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>167.30 (n/a)</td><td>158.48 (n/a)</td><td>156.60 (n/a)</td><td>150.60 (n/a)</td><td>6.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-8.86%)</td><td>0.04 (-15.32%)</td><td>0.04 (-16.22%)</td><td>0.03 <b>(-26.68%)</b></td><td>0.01 <b>(+53.84%)</b></td><td>260.50 <b>(+36.39%)</b></td><td>204.72 <b>(+20.06%)</b></td><td>202.40 (+19.34%)</td><td>167.10 (+9.72%)</td><td>35.97 <b>(+131.80%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.00 (n/a)</td><td>170.52 (n/a)</td><td>169.60 (n/a)</td><td>152.30 (n/a)</td><td>15.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-12.51%)</td><td>0.05 (-12.96%)</td><td>0.05 (-7.49%)</td><td>0.04 (-12.27%)</td><td>0.01 (-18.59%)</td><td>218.40 (+13.99%)</td><td>185.42 (+14.60%)</td><td>181.80 (+8.09%)</td><td>149.70 (+14.27%)</td><td>30.53 (+9.97%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>161.80 (n/a)</td><td>168.20 (n/a)</td><td>131.00 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-6.58%)</td><td>0.12 (+2.66%)</td><td>0.12 (+2.76%)</td><td>0.09 (+12.41%)</td><td>0.01 <b>(-34.38%)</b></td><td>176.80 (-11.02%)</td><td>143.92 (-4.32%)</td><td>136.90 (-2.70%)</td><td>128.90 (+7.06%)</td><td>19.43 <b>(-37.40%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.70 (n/a)</td><td>150.42 (n/a)</td><td>140.70 (n/a)</td><td>120.40 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (-8.28%)</td><td>0.10 (-8.36%)</td><td>0.10 (-11.68%)</td><td>0.09 (+13.09%)</td><td>0.01 <b>(-44.10%)</b></td><td>183.90 (-11.59%)</td><td>168.34 (+7.03%)</td><td>170.40 (+13.22%)</td><td>142.60 (+9.02%)</td><td>16.78 <b>(-46.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>157.28 (n/a)</td><td>150.50 (n/a)</td><td>130.80 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (-8.67%)</td><td>0.08 (-12.61%)</td><td>0.08 (-13.05%)</td><td>0.07 (-14.14%)</td><td>0.01 (+2.01%)</td><td>251.80 (+16.47%)</td><td>214.36 (+14.89%)</td><td>206.40 (+15.05%)</td><td>176.50 (+9.49%)</td><td>30.57 <b>(+30.54%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>186.58 (n/a)</td><td>179.40 (n/a)</td><td>161.20 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (+6.41%)</td><td>0.09 (+3.64%)</td><td>0.09 (-1.37%)</td><td>0.07 <b>(+37.30%)</b></td><td>0.02 <b>(-22.72%)</b></td><td>239.30 <b>(-27.15%)</b></td><td>184.40 (-8.60%)</td><td>178.90 (+1.42%)</td><td>131.50 (-6.00%)</td><td>39.00 <b>(-48.76%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>328.50 (n/a)</td><td>201.74 (n/a)</td><td>176.40 (n/a)</td><td>139.90 (n/a)</td><td>76.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-16.94%)</td><td>0.10 (-3.46%)</td><td>0.11 <b>(+21.99%)</b></td><td>0.07 (-6.39%)</td><td>0.02 <b>(-24.95%)</b></td><td>224.30 (+6.86%)</td><td>168.58 (+1.77%)</td><td>150.10 (-18.02%)</td><td>132.80 <b>(+20.40%)</b></td><td>41.81 (-4.83%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>209.90 (n/a)</td><td>165.64 (n/a)</td><td>183.10 (n/a)</td><td>110.30 (n/a)</td><td>43.93 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (-18.38%)</td><td>0.09 (-10.34%)</td><td>0.09 (-12.80%)</td><td>0.07 (+9.26%)</td><td>0.01 <b>(-42.63%)</b></td><td>225.00 (-8.46%)</td><td>187.84 (+7.83%)</td><td>188.90 (+14.69%)</td><td>152.00 <b>(+22.48%)</b></td><td>29.74 <b>(-36.56%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.80 (n/a)</td><td>174.20 (n/a)</td><td>164.70 (n/a)</td><td>124.10 (n/a)</td><td>46.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (+0.45%)</td><td>0.10 (-0.74%)</td><td>0.10 (-2.09%)</td><td>0.07 (-6.35%)</td><td>0.02 (+1.41%)</td><td>230.20 (+6.77%)</td><td>172.84 (+0.97%)</td><td>166.40 (+2.15%)</td><td>121.50 (-0.49%)</td><td>39.97 (+5.70%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.60 (n/a)</td><td>171.18 (n/a)</td><td>162.90 (n/a)</td><td>122.10 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-17.95%)</td><td>0.10 <b>(-21.01%)</b></td><td>0.10 <b>(-21.13%)</b></td><td>0.07 <b>(-22.15%)</b></td><td>0.02 (-6.67%)</td><td>238.30 <b>(+28.46%)</b></td><td>176.26 <b>(+27.87%)</b></td><td>165.20 <b>(+26.78%)</b></td><td>132.80 <b>(+21.83%)</b></td><td>41.24 <b>(+43.06%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.50 (n/a)</td><td>137.84 (n/a)</td><td>130.30 (n/a)</td><td>109.00 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 <b>(-32.27%)</b></td><td>0.09 <b>(-29.11%)</b></td><td>0.09 <b>(-27.73%)</b></td><td>0.08 <b>(-27.31%)</b></td><td>0.01 <b>(-50.00%)</b></td><td>214.50 <b>(+37.59%)</b></td><td>187.32 <b>(+40.29%)</b></td><td>179.70 <b>(+38.34%)</b></td><td>174.20 <b>(+47.63%)</b></td><td>16.53 (+2.84%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>155.90 (n/a)</td><td>133.52 (n/a)</td><td>129.90 (n/a)</td><td>118.00 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (-3.61%)</td><td>0.09 (-18.27%)</td><td>0.09 <b>(-24.72%)</b></td><td>0.07 <b>(-21.39%)</b></td><td>0.03 <b>(+33.17%)</b></td><td>236.30 <b>(+27.25%)</b></td><td>188.38 <b>(+26.55%)</b></td><td>187.80 <b>(+32.81%)</b></td><td>117.90 (+3.79%)</td><td>46.74 <b>(+73.63%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.70 (n/a)</td><td>148.86 (n/a)</td><td>141.40 (n/a)</td><td>113.60 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 <b>(-22.58%)</b></td><td>0.09 (-15.89%)</td><td>0.09 (-14.93%)</td><td>0.08 (-17.63%)</td><td>0.01 <b>(-36.86%)</b></td><td>205.00 <b>(+21.45%)</b></td><td>178.66 (+18.33%)</td><td>174.50 (+17.51%)</td><td>161.40 <b>(+29.12%)</b></td><td>17.80 (-2.51%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>168.80 (n/a)</td><td>150.98 (n/a)</td><td>148.50 (n/a)</td><td>125.00 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (-0.50%)</td><td>0.10 (-18.20%)</td><td>0.11 (-8.85%)</td><td>0.05 <b>(-39.46%)</b></td><td>0.03 <b>(+69.63%)</b></td><td>309.80 <b>(+65.14%)</b></td><td>191.30 <b>(+32.90%)</b></td><td>155.90 (+9.71%)</td><td>119.00 (+0.51%)</td><td>74.98 <b>(+183.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.60 (n/a)</td><td>143.94 (n/a)</td><td>142.10 (n/a)</td><td>118.40 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-7.77%)</td><td>0.10 (-7.31%)</td><td>0.10 (-8.89%)</td><td>0.07 (-7.73%)</td><td>0.02 (-12.79%)</td><td>226.80 (+8.36%)</td><td>173.14 (+7.22%)</td><td>171.50 (+9.80%)</td><td>128.10 (+8.38%)</td><td>41.24 (+0.96%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>209.30 (n/a)</td><td>161.48 (n/a)</td><td>156.20 (n/a)</td><td>118.20 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 <b>(+23.07%)</b></td><td>0.10 (+10.59%)</td><td>0.11 <b>(+26.39%)</b></td><td>0.07 (-12.29%)</td><td>0.02 <b>(+158.36%)</b></td><td>221.00 (+14.04%)</td><td>167.62 (-5.75%)</td><td>147.60 <b>(-20.90%)</b></td><td>126.00 (-18.76%)</td><td>42.70 <b>(+144.21%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>177.84 (n/a)</td><td>186.60 (n/a)</td><td>155.10 (n/a)</td><td>17.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (-10.77%)</td><td>0.09 (-5.78%)</td><td>0.10 (+0.77%)</td><td>0.08 (-4.49%)</td><td>0.01 (+0.19%)</td><td>215.10 (+4.67%)</td><td>179.20 (+6.48%)</td><td>160.00 (-0.74%)</td><td>153.80 (+12.10%)</td><td>29.45 (+17.38%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>168.30 (n/a)</td><td>161.20 (n/a)</td><td>137.20 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-6.86%)</td><td>0.10 (-17.87%)</td><td>0.09 <b>(-30.61%)</b></td><td>0.08 (-5.65%)</td><td>0.02 (-2.84%)</td><td>198.80 (+5.97%)</td><td>172.62 <b>(+21.96%)</b></td><td>187.10 <b>(+44.14%)</b></td><td>122.00 (+7.39%)</td><td>31.55 (+7.78%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.60 (n/a)</td><td>141.54 (n/a)</td><td>129.80 (n/a)</td><td>113.60 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (-14.74%)</td><td>0.17 (-12.05%)</td><td>0.18 (+0.33%)</td><td>0.09 <b>(-43.34%)</b></td><td>0.05 <b>(+32.96%)</b></td><td>365.80 <b>(+76.46%)</b></td><td>215.92 <b>(+22.71%)</b></td><td>178.40 (-0.34%)</td><td>148.20 (+17.34%)</td><td>88.80 <b>(+193.29%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.30 (n/a)</td><td>175.96 (n/a)</td><td>179.00 (n/a)</td><td>126.30 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (-16.49%)</td><td>0.19 (-13.64%)</td><td>0.19 (-14.45%)</td><td>0.16 (-4.07%)</td><td>0.02 <b>(-39.40%)</b></td><td>210.10 (+4.27%)</td><td>175.74 (+14.09%)</td><td>173.40 (+16.93%)</td><td>153.80 (+19.78%)</td><td>23.09 <b>(-23.77%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.50 (n/a)</td><td>154.04 (n/a)</td><td>148.30 (n/a)</td><td>128.40 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (-18.64%)</td><td>0.15 (-2.45%)</td><td>0.14 (+3.96%)</td><td>0.14 <b>(+27.44%)</b></td><td>0.01 <b>(-80.58%)</b></td><td>237.40 <b>(-21.52%)</b></td><td>225.74 (-1.07%)</td><td>227.20 (-3.81%)</td><td>213.80 <b>(+22.87%)</b></td><td>9.41 <b>(-81.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>302.50 (n/a)</td><td>228.18 (n/a)</td><td>236.20 (n/a)</td><td>174.00 (n/a)</td><td>49.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (+9.43%)</td><td>0.18 (-6.25%)</td><td>0.16 (-11.47%)</td><td>0.15 (+0.93%)</td><td>0.04 <b>(+38.20%)</b></td><td>218.60 (-0.91%)</td><td>192.26 (+7.95%)</td><td>200.00 (+12.99%)</td><td>136.40 (-8.64%)</td><td>33.19 <b>(+21.77%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.60 (n/a)</td><td>178.10 (n/a)</td><td>177.00 (n/a)</td><td>149.30 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (-0.57%)</td><td>0.21 (+0.13%)</td><td>0.19 (-4.14%)</td><td>0.18 (+5.88%)</td><td>0.03 (-5.61%)</td><td>181.00 (-5.58%)</td><td>160.04 (-0.37%)</td><td>169.10 (+4.32%)</td><td>130.60 (+0.62%)</td><td>20.79 (-10.20%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.70 (n/a)</td><td>160.64 (n/a)</td><td>162.10 (n/a)</td><td>129.80 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (-6.30%)</td><td>0.20 (-8.58%)</td><td>0.19 (-14.72%)</td><td>0.17 (-5.38%)</td><td>0.03 (+0.80%)</td><td>193.90 (+5.67%)</td><td>169.96 (+9.65%)</td><td>175.70 (+17.29%)</td><td>137.30 (+6.68%)</td><td>25.44 (+14.36%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.50 (n/a)</td><td>155.00 (n/a)</td><td>149.80 (n/a)</td><td>128.70 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (-11.80%)</td><td>0.21 (-3.18%)</td><td>0.21 (-0.22%)</td><td>0.19 (+5.42%)</td><td>0.02 <b>(-46.69%)</b></td><td>176.20 (-5.17%)</td><td>159.94 (+2.24%)</td><td>158.40 (+0.25%)</td><td>144.90 (+13.38%)</td><td>12.16 <b>(-42.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>185.80 (n/a)</td><td>156.44 (n/a)</td><td>158.00 (n/a)</td><td>127.80 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (-14.55%)</td><td>0.20 (-4.15%)</td><td>0.19 (+0.80%)</td><td>0.19 (+9.43%)</td><td>0.01 <b>(-64.67%)</b></td><td>173.90 (-8.62%)</td><td>166.42 (+2.60%)</td><td>169.50 (-0.82%)</td><td>150.70 (+17.00%)</td><td>9.20 <b>(-62.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>190.30 (n/a)</td><td>162.20 (n/a)</td><td>170.90 (n/a)</td><td>128.80 (n/a)</td><td>24.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (-0.87%)</td><td>0.18 (-9.85%)</td><td>0.18 (-4.84%)</td><td>0.14 (-15.22%)</td><td>0.05 (+11.17%)</td><td>234.90 (+17.98%)</td><td>186.18 (+12.43%)</td><td>185.10 (+5.05%)</td><td>124.90 (+0.89%)</td><td>41.53 <b>(+29.38%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>199.10 (n/a)</td><td>165.60 (n/a)</td><td>176.20 (n/a)</td><td>123.80 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (-17.39%)</td><td>0.16 (-17.34%)</td><td>0.17 (-16.44%)</td><td>0.14 (-19.67%)</td><td>0.02 (-12.37%)</td><td>227.50 <b>(+24.52%)</b></td><td>200.14 <b>(+21.09%)</b></td><td>193.70 (+19.64%)</td><td>179.50 <b>(+21.04%)</b></td><td>18.84 <b>(+32.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>182.70 (n/a)</td><td>165.28 (n/a)</td><td>161.90 (n/a)</td><td>148.30 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (-7.40%)</td><td>0.19 (-10.11%)</td><td>0.19 (-11.38%)</td><td>0.14 (-7.93%)</td><td>0.04 (-16.89%)</td><td>239.00 (+8.59%)</td><td>180.40 (+10.13%)</td><td>174.50 (+12.80%)</td><td>129.10 (+7.94%)</td><td>39.28 (-3.65%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>220.10 (n/a)</td><td>163.80 (n/a)</td><td>154.70 (n/a)</td><td>119.60 (n/a)</td><td>40.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 <b>(-29.57%)</b></td><td>0.17 <b>(-24.42%)</b></td><td>0.16 <b>(-35.28%)</b></td><td>0.15 (-1.45%)</td><td>0.02 <b>(-63.53%)</b></td><td>219.90 (+1.48%)</td><td>193.06 <b>(+25.72%)</b></td><td>200.90 <b>(+54.54%)</b></td><td>166.60 <b>(+42.03%)</b></td><td>24.00 <b>(-47.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>216.70 (n/a)</td><td>153.56 (n/a)</td><td>130.00 (n/a)</td><td>117.30 (n/a)</td><td>45.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (+10.69%)</td><td>0.16 (-6.15%)</td><td>0.14 <b>(-26.54%)</b></td><td>0.13 (-9.54%)</td><td>0.04 <b>(+57.22%)</b></td><td>253.60 (+10.55%)</td><td>215.70 (+9.01%)</td><td>242.00 <b>(+36.11%)</b></td><td>159.80 (-9.67%)</td><td>44.69 <b>(+59.06%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>229.40 (n/a)</td><td>197.88 (n/a)</td><td>177.80 (n/a)</td><td>176.90 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (+0.42%)</td><td>0.18 (+0.84%)</td><td>0.18 (-3.61%)</td><td>0.16 (+11.04%)</td><td>0.03 (-5.59%)</td><td>204.00 (-9.93%)</td><td>180.56 (-1.24%)</td><td>185.60 (+3.75%)</td><td>141.10 (-0.42%)</td><td>26.50 (-13.98%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>226.50 (n/a)</td><td>182.82 (n/a)</td><td>178.90 (n/a)</td><td>141.70 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (+12.06%)</td><td>0.19 (+2.41%)</td><td>0.19 (-4.10%)</td><td>0.18 (+5.30%)</td><td>0.02 <b>(+34.18%)</b></td><td>185.60 (-5.06%)</td><td>169.24 (-2.16%)</td><td>174.40 (+4.31%)</td><td>147.90 (-10.74%)</td><td>14.26 (+11.85%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>172.98 (n/a)</td><td>167.20 (n/a)</td><td>165.70 (n/a)</td><td>12.75 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (-1.25%)</td><td>0.20 (-9.29%)</td><td>0.21 (-10.44%)</td><td>0.15 (-3.08%)</td><td>0.04 (+4.15%)</td><td>213.90 (+3.18%)</td><td>170.96 (+10.61%)</td><td>158.10 (+11.65%)</td><td>132.70 (+1.30%)</td><td>33.40 (+8.25%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.30 (n/a)</td><td>154.56 (n/a)</td><td>141.60 (n/a)</td><td>131.00 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (+0.13%)</td><td>0.18 (+0.25%)</td><td>0.18 (+0.37%)</td><td>0.18 (+0.30%)</td><td>0.00 <b>(-23.15%)</b></td><td>47510.10 (-0.30%)</td><td>47376.88 (-0.25%)</td><td>47326.50 (-0.37%)</td><td>47239.10 (-0.13%)</td><td>116.38 <b>(-23.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47651.90 (n/a)</td><td>47496.22 (n/a)</td><td>47502.40 (n/a)</td><td>47298.30 (n/a)</td><td>152.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (-0.68%)</td><td>0.18 (-0.15%)</td><td>0.18 (-0.06%)</td><td>0.18 (+0.24%)</td><td>0.00 <b>(-72.79%)</b></td><td>47491.20 (-0.24%)</td><td>47396.56 (+0.15%)</td><td>47393.40 (+0.06%)</td><td>47330.60 (+0.69%)</td><td>58.87 <b>(-72.67%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47606.20 (n/a)</td><td>47326.78 (n/a)</td><td>47365.70 (n/a)</td><td>47008.30 (n/a)</td><td>215.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (+0.02%)</td><td>0.11 (+0.01%)</td><td>0.11 (-0.00%)</td><td>0.11 (+0.04%)</td><td>0.00 <b>(-27.09%)</b></td><td>374462.50 (-0.04%)</td><td>374367.42 (-0.01%)</td><td>374368.90 (+0.00%)</td><td>374238.70 (-0.02%)</td><td>88.65 <b>(-27.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374609.50 (n/a)</td><td>374395.58 (n/a)</td><td>374357.00 (n/a)</td><td>374312.80 (n/a)</td><td>121.56 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/repeat</summary>


### test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]

_No metrics available._


### test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (+19.62%)</td><td>0.15 <b>(+21.28%)</b></td><td>0.15 <b>(+24.45%)</b></td><td>0.11 (+11.24%)</td><td>0.02 <b>(+46.16%)</b></td><td>215.30 (-10.10%)</td><td>172.40 (-16.96%)</td><td>162.20 (-19.62%)</td><td>145.70 (-16.41%)</td><td>27.29 (+11.37%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>207.62 (n/a)</td><td>201.80 (n/a)</td><td>174.30 (n/a)</td><td>24.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (-12.80%)</td><td>0.27 (-8.28%)</td><td>0.30 (+6.61%)</td><td>0.20 (-16.21%)</td><td>0.06 <b>(+22.08%)</b></td><td>240.40 (+19.31%)</td><td>192.38 (+11.27%)</td><td>164.60 (-6.21%)</td><td>154.40 (+14.71%)</td><td>43.08 <b>(+77.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>201.50 (n/a)</td><td>172.90 (n/a)</td><td>175.50 (n/a)</td><td>134.60 (n/a)</td><td>24.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.14 (-1.32%)</td><td>11.84 (-5.19%)</td><td>12.77 (+3.10%)</td><td>8.01 <b>(-31.49%)</b></td><td>2.16 <b>(+227.23%)</b></td><td>1309.70 <b>(+45.96%)</b></td><td>917.64 (+9.04%)</td><td>821.00 (-3.00%)</td><td>798.00 (+1.33%)</td><td>219.74 <b>(+395.86%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.32 (n/a)</td><td>12.49 (n/a)</td><td>12.39 (n/a)</td><td>11.69 (n/a)</td><td>0.66 (n/a)</td><td>897.30 (n/a)</td><td>841.58 (n/a)</td><td>846.40 (n/a)</td><td>787.50 (n/a)</td><td>44.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 <b>(+20.49%)</b></td><td>0.27 (+10.99%)</td><td>0.25 (+6.09%)</td><td>0.23 (+2.69%)</td><td>0.04 <b>(+95.21%)</b></td><td>180.40 (-2.59%)</td><td>156.12 (-9.04%)</td><td>163.70 (-5.76%)</td><td>129.00 (-16.99%)</td><td>20.32 <b>(+55.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>185.20 (n/a)</td><td>171.64 (n/a)</td><td>173.70 (n/a)</td><td>155.40 (n/a)</td><td>13.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (-6.17%)</td><td>0.03 (-3.35%)</td><td>0.03 (+2.12%)</td><td>0.03 (+3.19%)</td><td>0.00 <b>(-30.36%)</b></td><td>183.80 (-3.11%)</td><td>161.68 (+2.03%)</td><td>168.00 (-2.04%)</td><td>131.00 (+6.59%)</td><td>20.71 <b>(-27.97%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>158.46 (n/a)</td><td>171.50 (n/a)</td><td>122.90 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+9.78%)</td><td>0.03 (+14.94%)</td><td>0.03 (+6.95%)</td><td>0.02 (+14.35%)</td><td>0.01 (+15.00%)</td><td>223.00 (-12.51%)</td><td>148.34 (-12.70%)</td><td>149.40 (-6.51%)</td><td>100.20 (-8.91%)</td><td>47.62 (-10.11%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.90 (n/a)</td><td>169.92 (n/a)</td><td>159.80 (n/a)</td><td>110.00 (n/a)</td><td>52.97 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (-14.30%)</td><td>0.03 (-15.80%)</td><td>0.04 (-14.16%)</td><td>0.02 <b>(-24.45%)</b></td><td>0.01 (+2.55%)</td><td>252.10 <b>(+32.34%)</b></td><td>186.00 <b>(+20.08%)</b></td><td>173.70 (+16.50%)</td><td>155.50 (+16.65%)</td><td>37.98 <b>(+65.02%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>154.90 (n/a)</td><td>149.10 (n/a)</td><td>133.30 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+14.04%)</td><td>0.03 (+17.81%)</td><td>0.03 <b>(+34.33%)</b></td><td>0.02 <b>(+20.97%)</b></td><td>0.01 (+14.96%)</td><td>189.30 (-17.37%)</td><td>144.94 (-15.17%)</td><td>131.10 <b>(-25.55%)</b></td><td>109.40 (-12.34%)</td><td>33.36 (-15.01%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>170.86 (n/a)</td><td>176.10 (n/a)</td><td>124.80 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(-22.76%)</b></td><td>0.03 (-12.66%)</td><td>0.03 (-7.70%)</td><td>0.03 (+0.31%)</td><td>0.00 <b>(-63.55%)</b></td><td>194.00 (-0.31%)</td><td>177.64 (+11.43%)</td><td>179.30 (+8.34%)</td><td>155.30 <b>(+29.42%)</b></td><td>14.63 <b>(-53.20%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>159.42 (n/a)</td><td>165.50 (n/a)</td><td>120.00 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-13.96%)</td><td>0.03 (+10.68%)</td><td>0.03 <b>(+36.71%)</b></td><td>0.02 (+6.73%)</td><td>0.00 <b>(-33.21%)</b></td><td>171.50 (-6.34%)</td><td>145.66 (-11.32%)</td><td>130.00 <b>(-26.84%)</b></td><td>127.20 (+16.27%)</td><td>23.16 <b>(-25.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>164.26 (n/a)</td><td>177.70 (n/a)</td><td>109.40 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (-4.59%)</td><td>0.03 (+4.53%)</td><td>0.03 (+7.36%)</td><td>0.03 <b>(+46.14%)</b></td><td>0.00 <b>(-48.28%)</b></td><td>191.60 <b>(-31.57%)</b></td><td>169.54 (-9.47%)</td><td>176.90 (-6.85%)</td><td>137.80 (+4.79%)</td><td>21.50 <b>(-63.07%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>280.00 (n/a)</td><td>187.28 (n/a)</td><td>189.90 (n/a)</td><td>131.50 (n/a)</td><td>58.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-6.55%)</td><td>0.03 (+10.17%)</td><td>0.03 <b>(+24.50%)</b></td><td>0.02 (-6.52%)</td><td>0.01 (-0.93%)</td><td>221.50 (+6.95%)</td><td>164.52 (-8.78%)</td><td>154.30 (-19.68%)</td><td>129.60 (+7.02%)</td><td>39.22 (+15.02%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>180.36 (n/a)</td><td>192.10 (n/a)</td><td>121.10 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+1.31%)</td><td>0.03 (+9.96%)</td><td>0.02 (+0.02%)</td><td>0.02 (-15.95%)</td><td>0.01 <b>(+32.67%)</b></td><td>273.00 (+18.95%)</td><td>189.70 (-5.12%)</td><td>208.60 (-0.05%)</td><td>126.60 (-1.33%)</td><td>61.84 <b>(+49.53%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.50 (n/a)</td><td>199.94 (n/a)</td><td>208.70 (n/a)</td><td>128.30 (n/a)</td><td>41.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-1.02%)</td><td>0.02 (-2.62%)</td><td>0.02 (-5.38%)</td><td>0.02 (-2.16%)</td><td>0.00 (-1.19%)</td><td>206.30 (+2.18%)</td><td>174.68 (+2.72%)</td><td>179.00 (+5.73%)</td><td>148.80 (+1.09%)</td><td>22.00 (+1.88%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>170.06 (n/a)</td><td>169.30 (n/a)</td><td>147.20 (n/a)</td><td>21.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (+3.82%)</td><td>0.03 (-4.99%)</td><td>0.03 (-17.39%)</td><td>0.02 (+16.72%)</td><td>0.01 (-10.73%)</td><td>201.30 (-14.30%)</td><td>165.12 (+3.48%)</td><td>170.00 <b>(+21.08%)</b></td><td>123.10 (-3.68%)</td><td>33.36 <b>(-25.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>159.56 (n/a)</td><td>140.40 (n/a)</td><td>127.80 (n/a)</td><td>44.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (+3.09%)</td><td>0.02 (+17.73%)</td><td>0.02 <b>(+20.89%)</b></td><td>0.02 <b>(+28.00%)</b></td><td>0.00 <b>(-54.04%)</b></td><td>184.60 <b>(-21.88%)</b></td><td>174.40 (-15.92%)</td><td>174.90 (-17.30%)</td><td>165.20 (-2.99%)</td><td>8.72 <b>(-64.83%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>207.42 (n/a)</td><td>211.50 (n/a)</td><td>170.30 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (-13.71%)</td><td>0.02 (+3.68%)</td><td>0.02 (+12.54%)</td><td>0.02 <b>(+40.57%)</b></td><td>0.00 <b>(-60.67%)</b></td><td>230.80 <b>(-28.88%)</b></td><td>209.24 (-7.78%)</td><td>201.10 (-11.14%)</td><td>191.10 (+15.89%)</td><td>19.58 <b>(-67.80%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>324.50 (n/a)</td><td>226.90 (n/a)</td><td>226.30 (n/a)</td><td>164.90 (n/a)</td><td>60.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-1.10%)</td><td>0.02 (+13.04%)</td><td>0.02 (+8.33%)</td><td>0.02 <b>(+32.32%)</b></td><td>0.00 <b>(-27.68%)</b></td><td>206.00 <b>(-24.40%)</b></td><td>177.68 (-13.47%)</td><td>181.90 (-7.66%)</td><td>153.00 (+1.12%)</td><td>23.96 <b>(-46.47%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>272.50 (n/a)</td><td>205.34 (n/a)</td><td>197.00 (n/a)</td><td>151.30 (n/a)</td><td>44.76 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (-5.22%)</td><td>0.02 (+3.24%)</td><td>0.02 (+3.85%)</td><td>0.02 (+18.33%)</td><td>0.00 <b>(-55.08%)</b></td><td>230.50 (-15.51%)</td><td>220.04 (-4.16%)</td><td>221.10 (-3.70%)</td><td>200.70 (+5.52%)</td><td>11.65 <b>(-60.23%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>272.80 (n/a)</td><td>229.60 (n/a)</td><td>229.60 (n/a)</td><td>190.20 (n/a)</td><td>29.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (+4.86%)</td><td>0.02 (+2.81%)</td><td>0.02 (-1.16%)</td><td>0.02 (+6.63%)</td><td>0.00 (+6.75%)</td><td>219.70 (-6.23%)</td><td>198.88 (-2.70%)</td><td>205.80 (+1.18%)</td><td>165.70 (-4.61%)</td><td>23.39 (-3.78%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>204.40 (n/a)</td><td>203.40 (n/a)</td><td>173.70 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (+8.90%)</td><td>0.05 (-11.20%)</td><td>0.05 (-15.53%)</td><td>0.04 (-12.96%)</td><td>0.01 <b>(+44.37%)</b></td><td>202.40 (+14.93%)</td><td>158.28 (+15.75%)</td><td>153.30 (+18.38%)</td><td>107.20 (-8.14%)</td><td>38.08 <b>(+54.82%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.10 (n/a)</td><td>136.74 (n/a)</td><td>129.50 (n/a)</td><td>116.70 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 <b>(-24.72%)</b></td><td>0.08 (-15.33%)</td><td>0.08 (-15.24%)</td><td>0.06 (-7.37%)</td><td>0.01 <b>(-54.42%)</b></td><td>197.10 (+7.94%)</td><td>165.12 (+15.40%)</td><td>158.70 (+17.99%)</td><td>148.40 <b>(+32.86%)</b></td><td>19.37 <b>(-34.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>182.60 (n/a)</td><td>143.08 (n/a)</td><td>134.50 (n/a)</td><td>111.70 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-19.41%)</td><td>0.04 (-18.83%)</td><td>0.05 (-7.63%)</td><td>0.02 <b>(-43.21%)</b></td><td>0.01 <b>(+26.77%)</b></td><td>336.50 <b>(+76.09%)</b></td><td>204.20 <b>(+31.47%)</b></td><td>174.70 (+8.24%)</td><td>145.30 <b>(+24.08%)</b></td><td>78.09 <b>(+187.71%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>155.32 (n/a)</td><td>161.40 (n/a)</td><td>117.10 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (+7.52%)</td><td>0.06 (-0.55%)</td><td>0.05 (-5.16%)</td><td>0.05 (-8.04%)</td><td>0.01 <b>(+113.08%)</b></td><td>199.00 (+8.74%)</td><td>177.46 (+1.79%)</td><td>192.00 (+5.44%)</td><td>148.20 (-7.03%)</td><td>24.16 <b>(+113.78%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>183.00 (n/a)</td><td>174.34 (n/a)</td><td>182.10 (n/a)</td><td>159.40 (n/a)</td><td>11.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 <b>(-21.53%)</b></td><td>0.04 (-19.12%)</td><td>0.04 <b>(-26.57%)</b></td><td>0.04 <b>(+41.67%)</b></td><td>0.01 <b>(-60.91%)</b></td><td>217.00 <b>(-29.41%)</b></td><td>187.34 (+10.93%)</td><td>197.10 <b>(+36.21%)</b></td><td>147.40 <b>(+27.40%)</b></td><td>27.06 <b>(-66.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>307.40 (n/a)</td><td>168.88 (n/a)</td><td>144.70 (n/a)</td><td>115.70 (n/a)</td><td>79.61 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (-17.76%)</td><td>0.06 (-5.73%)</td><td>0.06 (-1.61%)</td><td>0.05 (-5.50%)</td><td>0.01 <b>(-36.74%)</b></td><td>227.20 (+5.82%)</td><td>181.70 (+3.43%)</td><td>176.50 (+1.61%)</td><td>137.70 <b>(+21.54%)</b></td><td>33.36 (-18.71%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>175.68 (n/a)</td><td>173.70 (n/a)</td><td>113.30 (n/a)</td><td>41.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (-5.33%)</td><td>0.05 (-10.72%)</td><td>0.05 (-7.94%)</td><td>0.04 (-3.55%)</td><td>0.01 (-19.70%)</td><td>209.90 (+3.65%)</td><td>169.90 (+10.53%)</td><td>166.60 (+8.60%)</td><td>122.50 (+5.60%)</td><td>32.25 (-11.79%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>153.72 (n/a)</td><td>153.40 (n/a)</td><td>116.00 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (+4.16%)</td><td>0.05 (+6.26%)</td><td>0.05 (+8.63%)</td><td>0.04 (+16.88%)</td><td>0.01 (-10.24%)</td><td>253.80 (-14.43%)</td><td>190.14 (-7.70%)</td><td>180.50 (-7.96%)</td><td>140.80 (-3.96%)</td><td>43.30 <b>(-26.09%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.60 (n/a)</td><td>206.00 (n/a)</td><td>196.10 (n/a)</td><td>146.60 (n/a)</td><td>58.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 <b>(+21.90%)</b></td><td>0.06 (+5.51%)</td><td>0.05 (+12.86%)</td><td>0.04 (-2.04%)</td><td>0.02 <b>(+45.38%)</b></td><td>190.40 (+2.09%)</td><td>152.88 (-3.23%)</td><td>152.80 (-11.37%)</td><td>97.20 (-17.97%)</td><td>35.01 (+16.07%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>157.98 (n/a)</td><td>172.40 (n/a)</td><td>118.50 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (+19.80%)</td><td>0.05 (+4.91%)</td><td>0.05 (+5.94%)</td><td>0.04 (-13.79%)</td><td>0.01 <b>(+156.05%)</b></td><td>255.60 (+16.02%)</td><td>197.98 (-2.75%)</td><td>187.10 (-5.65%)</td><td>159.00 (-16.54%)</td><td>35.66 <b>(+154.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.30 (n/a)</td><td>203.58 (n/a)</td><td>198.30 (n/a)</td><td>190.50 (n/a)</td><td>14.03 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (+1.99%)</td><td>0.05 (-1.83%)</td><td>0.04 (-18.66%)</td><td>0.04 (+15.60%)</td><td>0.01 (-11.02%)</td><td>223.00 (-13.50%)</td><td>183.22 (-0.42%)</td><td>197.80 <b>(+22.93%)</b></td><td>123.30 (-1.91%)</td><td>37.68 <b>(-28.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.80 (n/a)</td><td>184.00 (n/a)</td><td>160.90 (n/a)</td><td>125.70 (n/a)</td><td>52.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 <b>(-29.83%)</b></td><td>0.04 (-18.46%)</td><td>0.04 (+0.15%)</td><td>0.02 <b>(-20.99%)</b></td><td>0.01 <b>(-34.74%)</b></td><td>379.60 <b>(+26.58%)</b></td><td>260.32 <b>(+21.18%)</b></td><td>224.70 (-0.18%)</td><td>205.10 <b>(+42.53%)</b></td><td>71.50 <b>(+20.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.90 (n/a)</td><td>214.82 (n/a)</td><td>225.10 (n/a)</td><td>143.90 (n/a)</td><td>59.17 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (-1.03%)</td><td>0.05 (+5.35%)</td><td>0.05 (+4.03%)</td><td>0.04 (+3.71%)</td><td>0.01 (-5.96%)</td><td>210.90 (-3.57%)</td><td>173.50 (-5.49%)</td><td>173.50 (-3.88%)</td><td>135.20 (+0.97%)</td><td>31.30 (-8.59%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>183.58 (n/a)</td><td>180.50 (n/a)</td><td>133.90 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (-9.96%)</td><td>0.04 (-13.69%)</td><td>0.04 (-17.62%)</td><td>0.03 (-17.22%)</td><td>0.01 (+5.76%)</td><td>274.40 <b>(+20.77%)</b></td><td>224.42 (+16.48%)</td><td>227.40 <b>(+21.41%)</b></td><td>188.70 (+11.07%)</td><td>32.57 <b>(+42.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>192.66 (n/a)</td><td>187.30 (n/a)</td><td>169.90 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 <b>(+34.15%)</b></td><td>0.04 (+13.60%)</td><td>0.04 (+3.56%)</td><td>0.03 (+12.63%)</td><td>0.01 <b>(+35.92%)</b></td><td>326.80 (-11.22%)</td><td>207.66 (-10.72%)</td><td>187.60 (-3.45%)</td><td>140.70 <b>(-25.44%)</b></td><td>71.48 (-7.20%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>368.10 (n/a)</td><td>232.60 (n/a)</td><td>194.30 (n/a)</td><td>188.70 (n/a)</td><td>77.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (+1.14%)</td><td>0.11 (+13.84%)</td><td>0.10 <b>(+21.58%)</b></td><td>0.09 (+14.16%)</td><td>0.02 (-19.74%)</td><td>188.50 (-12.41%)</td><td>158.78 (-13.56%)</td><td>156.80 (-17.78%)</td><td>126.20 (-1.17%)</td><td>25.26 <b>(-29.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>183.68 (n/a)</td><td>190.70 (n/a)</td><td>127.70 (n/a)</td><td>36.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 <b>(+41.36%)</b></td><td>0.15 (+12.49%)</td><td>0.15 (+19.61%)</td><td>0.10 (-16.43%)</td><td>0.04 <b>(+381.72%)</b></td><td>246.00 (+19.65%)</td><td>179.72 (-5.58%)</td><td>162.50 (-16.41%)</td><td>125.50 <b>(-29.30%)</b></td><td>51.20 <b>(+321.53%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>190.34 (n/a)</td><td>194.40 (n/a)</td><td>177.50 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (+5.29%)</td><td>0.11 (+11.88%)</td><td>0.12 <b>(+29.89%)</b></td><td>0.08 (+1.60%)</td><td>0.02 <b>(+20.53%)</b></td><td>193.20 (-1.58%)</td><td>149.84 (-9.73%)</td><td>134.60 <b>(-23.00%)</b></td><td>118.30 (-5.06%)</td><td>31.89 (+16.30%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.30 (n/a)</td><td>166.00 (n/a)</td><td>174.80 (n/a)</td><td>124.60 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-13.61%)</td><td>0.12 (-2.79%)</td><td>0.12 (-2.33%)</td><td>0.12 (+7.77%)</td><td>0.01 <b>(-62.80%)</b></td><td>177.30 (-7.22%)</td><td>166.38 (+1.14%)</td><td>170.00 (+2.41%)</td><td>152.90 (+15.75%)</td><td>9.97 <b>(-60.62%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>191.10 (n/a)</td><td>164.50 (n/a)</td><td>166.00 (n/a)</td><td>132.10 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (+9.72%)</td><td>0.11 (+14.80%)</td><td>0.10 (+15.49%)</td><td>0.09 <b>(+24.60%)</b></td><td>0.02 (+0.66%)</td><td>177.00 (-19.73%)</td><td>154.38 (-13.61%)</td><td>168.30 (-13.43%)</td><td>120.50 (-8.92%)</td><td>27.32 <b>(-24.29%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>178.70 (n/a)</td><td>194.40 (n/a)</td><td>132.30 (n/a)</td><td>36.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (+1.22%)</td><td>0.12 (+4.42%)</td><td>0.12 (+1.27%)</td><td>0.09 (+8.23%)</td><td>0.02 (-15.42%)</td><td>221.90 (-7.62%)</td><td>173.64 (-5.42%)</td><td>170.00 (-1.22%)</td><td>136.00 (-1.23%)</td><td>30.83 <b>(-22.64%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>240.20 (n/a)</td><td>183.60 (n/a)</td><td>172.10 (n/a)</td><td>137.70 (n/a)</td><td>39.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 <b>(+27.00%)</b></td><td>0.09 (+15.51%)</td><td>0.10 <b>(+30.69%)</b></td><td>0.04 <b>(-24.91%)</b></td><td>0.03 <b>(+111.13%)</b></td><td>373.20 <b>(+33.19%)</b></td><td>205.34 (-3.19%)</td><td>164.40 <b>(-23.46%)</b></td><td>131.10 <b>(-21.26%)</b></td><td>99.94 <b>(+124.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>280.20 (n/a)</td><td>212.10 (n/a)</td><td>214.80 (n/a)</td><td>166.50 (n/a)</td><td>44.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 <b>(-30.71%)</b></td><td>0.09 <b>(-22.60%)</b></td><td>0.09 <b>(-34.02%)</b></td><td>0.08 <b>(+23.51%)</b></td><td>0.01 <b>(-74.76%)</b></td><td>245.50 (-19.03%)</td><td>206.66 (+15.89%)</td><td>202.10 <b>(+51.61%)</b></td><td>180.00 <b>(+44.35%)</b></td><td>23.83 <b>(-68.99%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>303.20 (n/a)</td><td>178.32 (n/a)</td><td>133.30 (n/a)</td><td>124.70 (n/a)</td><td>76.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (+14.34%)</td><td>0.10 (+5.15%)</td><td>0.09 (-4.96%)</td><td>0.08 (-3.29%)</td><td>0.03 <b>(+72.45%)</b></td><td>199.60 (+3.42%)</td><td>165.46 (-2.21%)</td><td>187.30 (+5.22%)</td><td>121.20 (-12.55%)</td><td>37.23 <b>(+55.10%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>169.20 (n/a)</td><td>178.00 (n/a)</td><td>138.60 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-17.07%)</td><td>0.10 (-9.90%)</td><td>0.09 (-10.29%)</td><td>0.08 (-10.70%)</td><td>0.02 <b>(-24.58%)</b></td><td>219.20 (+12.01%)</td><td>186.68 (+10.41%)</td><td>196.70 (+11.44%)</td><td>152.70 <b>(+20.52%)</b></td><td>27.37 (+3.15%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>195.70 (n/a)</td><td>169.08 (n/a)</td><td>176.50 (n/a)</td><td>126.70 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-16.29%)</td><td>0.10 (-0.70%)</td><td>0.09 (-2.67%)</td><td>0.08 (+8.61%)</td><td>0.02 <b>(-37.79%)</b></td><td>194.00 (-7.93%)</td><td>165.62 (-2.19%)</td><td>174.30 (+2.77%)</td><td>131.90 (+19.37%)</td><td>27.29 <b>(-31.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>210.70 (n/a)</td><td>169.32 (n/a)</td><td>169.60 (n/a)</td><td>110.50 (n/a)</td><td>39.59 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (+13.09%)</td><td>0.09 (+4.57%)</td><td>0.09 (+4.64%)</td><td>0.08 (-2.30%)</td><td>0.02 <b>(+74.71%)</b></td><td>231.50 (+2.34%)</td><td>194.12 (-3.03%)</td><td>184.10 (-4.41%)</td><td>155.30 (-11.56%)</td><td>31.97 <b>(+60.18%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>200.18 (n/a)</td><td>192.60 (n/a)</td><td>175.60 (n/a)</td><td>19.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (+1.01%)</td><td>0.10 (+11.17%)</td><td>0.10 (+11.51%)</td><td>0.09 (+14.24%)</td><td>0.01 <b>(-43.54%)</b></td><td>172.50 (-12.44%)</td><td>165.02 (-10.61%)</td><td>170.10 (-10.33%)</td><td>151.60 (-1.04%)</td><td>8.91 <b>(-50.06%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>184.60 (n/a)</td><td>189.70 (n/a)</td><td>153.20 (n/a)</td><td>17.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (+19.57%)</td><td>0.09 (+5.64%)</td><td>0.09 (-3.01%)</td><td>0.06 <b>(-21.81%)</b></td><td>0.03 <b>(+103.62%)</b></td><td>293.60 <b>(+27.87%)</b></td><td>200.28 (+0.02%)</td><td>202.10 (+3.11%)</td><td>132.10 (-16.39%)</td><td>61.37 <b>(+118.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>200.24 (n/a)</td><td>196.00 (n/a)</td><td>158.00 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (+5.85%)</td><td>0.08 (-8.08%)</td><td>0.07 (-7.97%)</td><td>0.05 <b>(-35.38%)</b></td><td>0.02 <b>(+222.79%)</b></td><td>331.50 <b>(+54.76%)</b></td><td>230.46 (+15.11%)</td><td>221.60 (+8.68%)</td><td>170.90 (-5.53%)</td><td>66.20 <b>(+355.87%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>200.20 (n/a)</td><td>203.90 (n/a)</td><td>180.90 (n/a)</td><td>14.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (-11.64%)</td><td>0.17 (-16.67%)</td><td>0.17 (-19.11%)</td><td>0.13 (-9.68%)</td><td>0.03 <b>(-29.08%)</b></td><td>247.70 (+10.73%)</td><td>199.04 (+18.43%)</td><td>196.10 <b>(+23.64%)</b></td><td>153.10 (+13.16%)</td><td>33.76 (-9.81%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.70 (n/a)</td><td>168.06 (n/a)</td><td>158.60 (n/a)</td><td>135.30 (n/a)</td><td>37.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (-9.99%)</td><td>0.18 (+0.93%)</td><td>0.20 (+0.81%)</td><td>0.12 <b>(+23.50%)</b></td><td>0.03 <b>(-30.36%)</b></td><td>263.40 (-19.03%)</td><td>184.92 (-5.39%)</td><td>166.40 (-0.78%)</td><td>159.80 (+11.13%)</td><td>44.01 <b>(-40.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>325.30 (n/a)</td><td>195.46 (n/a)</td><td>167.70 (n/a)</td><td>143.80 (n/a)</td><td>73.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 <b>(+22.81%)</b></td><td>0.22 (-7.94%)</td><td>0.21 (-12.91%)</td><td>0.13 <b>(-38.40%)</b></td><td>0.07 <b>(+337.18%)</b></td><td>305.50 <b>(+62.33%)</b></td><td>203.58 (+17.64%)</td><td>196.00 (+14.82%)</td><td>128.70 (-18.60%)</td><td>66.89 <b>(+480.09%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>173.06 (n/a)</td><td>170.70 (n/a)</td><td>158.10 (n/a)</td><td>11.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 <b>(-20.05%)</b></td><td>0.19 (-15.32%)</td><td>0.18 <b>(-24.66%)</b></td><td>0.17 <b>(+25.88%)</b></td><td>0.02 <b>(-68.25%)</b></td><td>192.00 <b>(-20.56%)</b></td><td>178.04 (+10.93%)</td><td>185.40 <b>(+32.71%)</b></td><td>150.70 <b>(+25.06%)</b></td><td>16.25 <b>(-68.28%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>241.70 (n/a)</td><td>160.50 (n/a)</td><td>139.70 (n/a)</td><td>120.50 (n/a)</td><td>51.22 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.30 (+6.46%)</td><td>0.25 <b>(+21.05%)</b></td><td>0.27 <b>(+23.47%)</b></td><td>0.17 <b>(+63.81%)</b></td><td>0.06 (-16.38%)</td><td>238.50 <b>(-38.96%)</b></td><td>169.54 <b>(-23.05%)</b></td><td>154.20 (-19.01%)</td><td>134.50 (-6.08%)</td><td>43.38 <b>(-55.83%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>390.70 (n/a)</td><td>220.32 (n/a)</td><td>190.40 (n/a)</td><td>143.20 (n/a)</td><td>98.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (-2.67%)</td><td>0.20 (+1.70%)</td><td>0.21 (+0.41%)</td><td>0.15 (-6.86%)</td><td>0.04 (-7.10%)</td><td>225.90 (+7.37%)</td><td>166.18 (-1.82%)</td><td>157.70 (-0.38%)</td><td>126.90 (+2.67%)</td><td>36.36 (+4.34%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.40 (n/a)</td><td>169.26 (n/a)</td><td>158.30 (n/a)</td><td>123.60 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (+4.17%)</td><td>0.24 (+16.71%)</td><td>0.26 <b>(+35.39%)</b></td><td>0.19 (+6.50%)</td><td>0.04 (+10.15%)</td><td>199.00 (-6.13%)</td><td>158.30 (-14.12%)</td><td>142.50 <b>(-26.13%)</b></td><td>132.20 (-3.99%)</td><td>30.04 (-0.77%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>212.00 (n/a)</td><td>184.32 (n/a)</td><td>192.90 (n/a)</td><td>137.70 (n/a)</td><td>30.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (-7.23%)</td><td>0.19 (-19.73%)</td><td>0.21 (-6.15%)</td><td>0.09 <b>(-50.69%)</b></td><td>0.07 <b>(+79.89%)</b></td><td>345.50 <b>(+102.76%)</b></td><td>206.78 <b>(+42.06%)</b></td><td>158.80 (+6.58%)</td><td>120.90 (+7.75%)</td><td>95.60 <b>(+297.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>170.40 (n/a)</td><td>145.56 (n/a)</td><td>149.00 (n/a)</td><td>112.20 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (-10.80%)</td><td>0.22 (+2.92%)</td><td>0.24 <b>(+24.96%)</b></td><td>0.15 (-15.34%)</td><td>0.05 (-5.11%)</td><td>246.70 (+18.15%)</td><td>179.38 (-1.97%)</td><td>156.20 (-19.98%)</td><td>137.90 (+12.11%)</td><td>45.05 <b>(+32.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>208.80 (n/a)</td><td>182.98 (n/a)</td><td>195.20 (n/a)</td><td>123.00 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (-13.42%)</td><td>0.19 (-9.37%)</td><td>0.21 (-1.03%)</td><td>0.14 (-16.10%)</td><td>0.04 (+10.39%)</td><td>238.60 (+19.18%)</td><td>176.86 (+11.92%)</td><td>154.40 (+1.05%)</td><td>145.80 (+15.53%)</td><td>40.13 <b>(+47.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>200.20 (n/a)</td><td>158.02 (n/a)</td><td>152.80 (n/a)</td><td>126.20 (n/a)</td><td>27.17 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 <b>(+41.00%)</b></td><td>0.21 (+18.52%)</td><td>0.22 <b>(+21.07%)</b></td><td>0.17 (+3.36%)</td><td>0.04 <b>(+323.44%)</b></td><td>201.70 (-3.26%)</td><td>167.30 (-13.88%)</td><td>161.10 (-17.43%)</td><td>129.80 <b>(-29.07%)</b></td><td>27.42 <b>(+188.99%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>194.26 (n/a)</td><td>195.10 (n/a)</td><td>183.00 (n/a)</td><td>9.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (-14.90%)</td><td>0.17 (-4.90%)</td><td>0.18 (-0.34%)</td><td>0.15 (-6.76%)</td><td>0.01 <b>(-32.25%)</b></td><td>222.60 (+7.28%)</td><td>190.36 (+4.69%)</td><td>183.30 (+0.33%)</td><td>179.30 (+17.50%)</td><td>18.11 (-12.70%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>207.50 (n/a)</td><td>181.84 (n/a)</td><td>182.70 (n/a)</td><td>152.60 (n/a)</td><td>20.75 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (+11.48%)</td><td>0.18 (-0.61%)</td><td>0.17 (-7.73%)</td><td>0.15 (-6.97%)</td><td>0.03 <b>(+56.01%)</b></td><td>231.90 (+7.46%)</td><td>196.70 (+2.03%)</td><td>202.80 (+8.33%)</td><td>145.60 (-10.29%)</td><td>32.89 <b>(+43.55%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>215.80 (n/a)</td><td>192.78 (n/a)</td><td>187.20 (n/a)</td><td>162.30 (n/a)</td><td>22.91 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (+6.03%)</td><td>0.13 (-15.95%)</td><td>0.13 (-19.20%)</td><td>0.09 <b>(-37.98%)</b></td><td>0.04 <b>(+276.51%)</b></td><td>345.80 <b>(+61.29%)</b></td><td>255.86 <b>(+25.09%)</b></td><td>258.60 <b>(+23.73%)</b></td><td>174.90 (-5.71%)</td><td>64.43 <b>(+474.40%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>204.54 (n/a)</td><td>209.00 (n/a)</td><td>185.50 (n/a)</td><td>11.22 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-16.33%)</td><td>0.11 (+2.90%)</td><td>0.11 (+11.07%)</td><td>0.09 <b>(+53.88%)</b></td><td>0.02 <b>(-52.64%)</b></td><td>238.80 <b>(-35.02%)</b></td><td>193.92 (-10.78%)</td><td>181.60 (-9.97%)</td><td>167.60 (+19.46%)</td><td>30.52 <b>(-65.41%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>367.50 (n/a)</td><td>217.36 (n/a)</td><td>201.70 (n/a)</td><td>140.30 (n/a)</td><td>88.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 <b>(-24.08%)</b></td><td>0.10 (-9.77%)</td><td>0.10 (-17.52%)</td><td>0.09 <b>(+38.09%)</b></td><td>0.01 <b>(-62.49%)</b></td><td>239.20 <b>(-27.60%)</b></td><td>198.62 (+1.78%)</td><td>199.70 <b>(+21.25%)</b></td><td>172.10 <b>(+31.78%)</b></td><td>26.30 <b>(-66.52%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>330.40 (n/a)</td><td>195.14 (n/a)</td><td>164.70 (n/a)</td><td>130.60 (n/a)</td><td>78.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 <b>(-32.70%)</b></td><td>0.12 (-10.85%)</td><td>0.12 (-4.07%)</td><td>0.11 (+7.44%)</td><td>0.00 <b>(-84.06%)</b></td><td>187.50 (-6.95%)</td><td>175.00 (+8.49%)</td><td>172.10 (+4.24%)</td><td>169.10 <b>(+48.59%)</b></td><td>7.26 <b>(-77.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>201.50 (n/a)</td><td>161.30 (n/a)</td><td>165.10 (n/a)</td><td>113.80 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 <b>(+45.18%)</b></td><td>0.13 (+6.92%)</td><td>0.12 (-7.30%)</td><td>0.10 (-3.98%)</td><td>0.04 <b>(+188.10%)</b></td><td>208.20 (+4.15%)</td><td>167.04 (-0.67%)</td><td>172.30 (+7.89%)</td><td>100.30 <b>(-31.11%)</b></td><td>45.26 <b>(+108.18%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>199.90 (n/a)</td><td>168.16 (n/a)</td><td>159.70 (n/a)</td><td>145.60 (n/a)</td><td>21.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (+3.56%)</td><td>0.13 (-6.20%)</td><td>0.13 (-9.75%)</td><td>0.10 (-6.02%)</td><td>0.02 <b>(+23.83%)</b></td><td>198.00 (+6.39%)</td><td>161.94 (+7.73%)</td><td>151.70 (+10.81%)</td><td>126.20 (-3.44%)</td><td>30.20 <b>(+30.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>186.10 (n/a)</td><td>150.32 (n/a)</td><td>136.90 (n/a)</td><td>130.70 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (+6.75%)</td><td>0.13 (-4.11%)</td><td>0.12 (-10.73%)</td><td>0.10 (+1.21%)</td><td>0.03 (+13.46%)</td><td>203.70 (-1.21%)</td><td>166.26 (+5.11%)</td><td>167.00 (+12.01%)</td><td>111.00 (-6.33%)</td><td>38.78 (+5.93%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>206.20 (n/a)</td><td>158.18 (n/a)</td><td>149.10 (n/a)</td><td>118.50 (n/a)</td><td>36.61 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-12.35%)</td><td>0.11 (-6.65%)</td><td>0.11 (+6.61%)</td><td>0.08 (-14.34%)</td><td>0.02 (-17.67%)</td><td>245.30 (+16.75%)</td><td>193.04 (+6.98%)</td><td>181.90 (-6.19%)</td><td>163.50 (+14.10%)</td><td>31.34 (+13.42%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>210.10 (n/a)</td><td>180.44 (n/a)</td><td>193.90 (n/a)</td><td>143.30 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (+5.62%)</td><td>0.11 (+7.46%)</td><td>0.11 (+2.88%)</td><td>0.09 (+16.44%)</td><td>0.01 (-19.31%)</td><td>218.10 (-14.10%)</td><td>187.40 (-7.97%)</td><td>188.10 (-2.79%)</td><td>154.80 (-5.32%)</td><td>22.84 <b>(-35.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>253.90 (n/a)</td><td>203.64 (n/a)</td><td>193.50 (n/a)</td><td>163.50 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 (+13.94%)</td><td>0.14 (-5.26%)</td><td>0.13 (-18.69%)</td><td>0.11 (+3.47%)</td><td>0.03 <b>(+25.72%)</b></td><td>217.30 (-3.34%)</td><td>184.78 (+6.54%)</td><td>192.00 <b>(+23.00%)</b></td><td>125.00 (-12.22%)</td><td>36.88 (+4.84%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>224.80 (n/a)</td><td>173.44 (n/a)</td><td>156.10 (n/a)</td><td>142.40 (n/a)</td><td>35.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 <b>(+23.61%)</b></td><td>0.15 (+0.31%)</td><td>0.14 (+0.99%)</td><td>0.11 (-11.40%)</td><td>0.04 <b>(+71.67%)</b></td><td>227.30 (+12.86%)</td><td>172.86 (+3.32%)</td><td>172.00 (-0.98%)</td><td>109.90 (-19.07%)</td><td>43.38 <b>(+54.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>167.30 (n/a)</td><td>173.70 (n/a)</td><td>135.80 (n/a)</td><td>28.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 <b>(+25.30%)</b></td><td>0.15 (+2.18%)</td><td>0.13 (-12.01%)</td><td>0.13 <b>(+27.91%)</b></td><td>0.04 (+18.58%)</td><td>194.50 <b>(-21.82%)</b></td><td>169.14 (-2.77%)</td><td>182.40 (+13.64%)</td><td>106.00 <b>(-20.18%)</b></td><td>36.09 <b>(-26.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>248.80 (n/a)</td><td>173.96 (n/a)</td><td>160.50 (n/a)</td><td>132.80 (n/a)</td><td>48.95 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (+6.57%)</td><td>0.15 (+4.50%)</td><td>0.13 (+0.71%)</td><td>0.12 (+9.77%)</td><td>0.04 (+0.96%)</td><td>206.20 (-8.88%)</td><td>166.90 (-4.84%)</td><td>188.30 (-0.74%)</td><td>117.40 (-6.16%)</td><td>38.89 (-11.57%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>226.30 (n/a)</td><td>175.38 (n/a)</td><td>189.70 (n/a)</td><td>125.10 (n/a)</td><td>43.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (-14.91%)</td><td>0.13 (-12.16%)</td><td>0.13 (-13.23%)</td><td>0.12 (+0.38%)</td><td>0.01 <b>(-45.86%)</b></td><td>213.50 (-0.37%)</td><td>196.52 (+12.76%)</td><td>195.50 (+15.27%)</td><td>180.00 (+17.57%)</td><td>15.68 <b>(-36.61%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>174.28 (n/a)</td><td>169.60 (n/a)</td><td>153.10 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 <b>(+32.29%)</b></td><td>0.17 <b>(+30.41%)</b></td><td>0.18 <b>(+37.30%)</b></td><td>0.12 <b>(+21.53%)</b></td><td>0.05 <b>(+69.71%)</b></td><td>203.80 (-17.72%)</td><td>152.86 <b>(-20.58%)</b></td><td>139.40 <b>(-27.17%)</b></td><td>102.00 <b>(-24.39%)</b></td><td>45.89 (+13.85%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>247.70 (n/a)</td><td>192.48 (n/a)</td><td>191.40 (n/a)</td><td>134.90 (n/a)</td><td>40.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 <b>(-27.26%)</b></td><td>0.11 <b>(-23.76%)</b></td><td>0.11 <b>(-22.87%)</b></td><td>0.09 <b>(-20.78%)</b></td><td>0.02 <b>(-28.12%)</b></td><td>282.70 <b>(+26.26%)</b></td><td>230.10 <b>(+30.84%)</b></td><td>222.90 <b>(+29.67%)</b></td><td>194.40 <b>(+37.48%)</b></td><td>36.66 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>223.90 (n/a)</td><td>175.86 (n/a)</td><td>171.90 (n/a)</td><td>141.40 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (-1.79%)</td><td>0.12 (-3.68%)</td><td>0.12 (-3.68%)</td><td>0.08 <b>(-22.39%)</b></td><td>0.03 <b>(+45.75%)</b></td><td>317.40 <b>(+28.81%)</b></td><td>211.46 (+8.25%)</td><td>198.90 (+3.86%)</td><td>157.10 (+1.81%)</td><td>65.86 <b>(+86.16%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>246.40 (n/a)</td><td>195.34 (n/a)</td><td>191.50 (n/a)</td><td>154.30 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (+8.92%)</td><td>0.11 (-4.79%)</td><td>0.11 (-0.13%)</td><td>0.08 <b>(-25.03%)</b></td><td>0.02 <b>(+300.12%)</b></td><td>228.40 <b>(+33.41%)</b></td><td>176.04 (+7.79%)</td><td>165.60 (+0.12%)</td><td>140.50 (-8.17%)</td><td>33.73 <b>(+400.35%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>171.20 (n/a)</td><td>163.32 (n/a)</td><td>165.40 (n/a)</td><td>153.00 (n/a)</td><td>6.74 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (+3.00%)</td><td>0.11 (-4.37%)</td><td>0.10 (-5.19%)</td><td>0.08 <b>(-20.24%)</b></td><td>0.02 <b>(+58.27%)</b></td><td>233.10 <b>(+25.39%)</b></td><td>178.52 (+6.53%)</td><td>178.10 (+5.51%)</td><td>143.30 (-2.91%)</td><td>34.52 <b>(+93.89%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>185.90 (n/a)</td><td>167.58 (n/a)</td><td>168.80 (n/a)</td><td>147.60 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (+0.68%)</td><td>0.10 (-12.18%)</td><td>0.09 <b>(-21.15%)</b></td><td>0.08 <b>(-21.56%)</b></td><td>0.03 <b>(+85.20%)</b></td><td>226.30 <b>(+27.49%)</b></td><td>188.98 (+18.01%)</td><td>209.30 <b>(+26.85%)</b></td><td>130.60 (-0.68%)</td><td>42.22 <b>(+143.89%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>160.14 (n/a)</td><td>165.00 (n/a)</td><td>131.50 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-14.69%)</td><td>0.11 (+11.90%)</td><td>0.12 <b>(+30.18%)</b></td><td>0.08 (+12.55%)</td><td>0.02 <b>(-36.09%)</b></td><td>236.70 (-11.15%)</td><td>177.18 (-14.43%)</td><td>157.80 <b>(-23.17%)</b></td><td>137.80 (+17.28%)</td><td>40.12 <b>(-29.88%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>266.40 (n/a)</td><td>207.06 (n/a)</td><td>205.40 (n/a)</td><td>117.50 (n/a)</td><td>57.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (-19.61%)</td><td>0.10 (-14.84%)</td><td>0.09 (-11.72%)</td><td>0.08 (-5.43%)</td><td>0.01 <b>(-46.37%)</b></td><td>217.20 (+5.74%)</td><td>189.70 (+14.91%)</td><td>199.80 (+13.27%)</td><td>157.80 <b>(+24.45%)</b></td><td>24.40 <b>(-27.95%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>205.40 (n/a)</td><td>165.08 (n/a)</td><td>176.40 (n/a)</td><td>126.80 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (+14.69%)</td><td>0.11 (+7.52%)</td><td>0.10 (-9.22%)</td><td>0.08 (-8.09%)</td><td>0.03 <b>(+80.62%)</b></td><td>224.40 (+8.83%)</td><td>172.42 (-2.98%)</td><td>187.50 (+10.16%)</td><td>119.80 (-12.81%)</td><td>46.73 <b>(+62.53%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>177.72 (n/a)</td><td>170.20 (n/a)</td><td>137.40 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (-10.61%)</td><td>0.10 (-14.21%)</td><td>0.10 (-9.75%)</td><td>0.08 <b>(-20.53%)</b></td><td>0.02 (-9.12%)</td><td>243.00 <b>(+25.84%)</b></td><td>191.34 (+16.98%)</td><td>188.50 (+10.82%)</td><td>140.80 (+11.83%)</td><td>37.81 <b>(+25.52%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>193.10 (n/a)</td><td>163.56 (n/a)</td><td>170.10 (n/a)</td><td>125.90 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (+15.06%)</td><td>0.10 (-1.49%)</td><td>0.10 (-2.89%)</td><td>0.08 (-4.04%)</td><td>0.02 <b>(+69.18%)</b></td><td>223.00 (+4.21%)</td><td>185.30 (+3.82%)</td><td>179.40 (+2.99%)</td><td>132.30 (-13.07%)</td><td>37.78 <b>(+55.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>178.48 (n/a)</td><td>174.20 (n/a)</td><td>152.20 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.80 (+0.36%)</td><td>0.59 (-8.27%)</td><td>0.59 (-4.92%)</td><td>0.43 <b>(-20.41%)</b></td><td>0.14 <b>(+26.99%)</b></td><td>229.30 <b>(+25.64%)</b></td><td>173.50 (+11.20%)</td><td>167.90 (+5.20%)</td><td>122.60 (-0.41%)</td><td>38.72 <b>(+57.05%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.80 (n/a)</td><td>0.64 (n/a)</td><td>0.62 (n/a)</td><td>0.54 (n/a)</td><td>0.11 (n/a)</td><td>182.50 (n/a)</td><td>156.02 (n/a)</td><td>159.60 (n/a)</td><td>123.10 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.60 <b>(-41.31%)</b></td><td>0.53 <b>(-26.02%)</b></td><td>0.56 <b>(-22.99%)</b></td><td>0.44 (-11.85%)</td><td>0.07 <b>(-65.56%)</b></td><td>223.30 (+13.47%)</td><td>187.24 <b>(+29.76%)</b></td><td>175.80 <b>(+29.84%)</b></td><td>164.60 <b>(+70.39%)</b></td><td>24.71 <b>(-32.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.02 (n/a)</td><td>0.72 (n/a)</td><td>0.73 (n/a)</td><td>0.50 (n/a)</td><td>0.19 (n/a)</td><td>196.80 (n/a)</td><td>144.30 (n/a)</td><td>135.40 (n/a)</td><td>96.60 (n/a)</td><td>36.73 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.80 (+6.30%)</td><td>0.64 (+14.55%)</td><td>0.58 (+10.82%)</td><td>0.50 (+8.08%)</td><td>0.13 (+8.34%)</td><td>198.20 (-7.47%)</td><td>159.68 (-12.67%)</td><td>170.90 (-9.77%)</td><td>123.50 (-5.94%)</td><td>30.90 (-6.83%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.75 (n/a)</td><td>0.55 (n/a)</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.12 (n/a)</td><td>214.20 (n/a)</td><td>182.84 (n/a)</td><td>189.40 (n/a)</td><td>131.30 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.57 (+0.33%)</td><td>0.49 (-4.75%)</td><td>0.51 (+0.25%)</td><td>0.38 (-18.03%)</td><td>0.08 <b>(+70.77%)</b></td><td>257.10 <b>(+22.02%)</b></td><td>205.86 (+6.62%)</td><td>192.10 (-0.21%)</td><td>171.40 (-0.35%)</td><td>34.86 <b>(+107.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.57 (n/a)</td><td>0.51 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.05 (n/a)</td><td>210.70 (n/a)</td><td>193.08 (n/a)</td><td>192.50 (n/a)</td><td>172.00 (n/a)</td><td>16.83 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.46 (-16.36%)</td><td>0.38 (-14.18%)</td><td>0.39 (-12.44%)</td><td>0.31 (-13.01%)</td><td>0.06 <b>(-27.87%)</b></td><td>240.10 (+14.94%)</td><td>195.74 (+15.69%)</td><td>187.20 (+14.22%)</td><td>159.20 (+19.61%)</td><td>30.08 (-0.86%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.55 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>208.90 (n/a)</td><td>169.20 (n/a)</td><td>163.90 (n/a)</td><td>133.10 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.43 <b>(-20.63%)</b></td><td>0.37 (-12.03%)</td><td>0.36 (-14.09%)</td><td>0.30 (-2.78%)</td><td>0.05 <b>(-41.43%)</b></td><td>244.30 (+2.86%)</td><td>203.06 (+11.67%)</td><td>203.40 (+16.43%)</td><td>170.20 <b>(+25.98%)</b></td><td>28.09 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>237.50 (n/a)</td><td>181.84 (n/a)</td><td>174.70 (n/a)</td><td>135.10 (n/a)</td><td>37.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.60 <b>(+23.55%)</b></td><td>0.43 (+2.04%)</td><td>0.43 (+1.68%)</td><td>0.25 (-18.44%)</td><td>0.13 <b>(+83.25%)</b></td><td>292.20 <b>(+22.62%)</b></td><td>185.60 (+3.55%)</td><td>169.80 (-1.62%)</td><td>122.30 (-19.06%)</td><td>63.83 <b>(+85.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>238.30 (n/a)</td><td>179.24 (n/a)</td><td>172.60 (n/a)</td><td>151.10 (n/a)</td><td>34.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.46 (-18.22%)</td><td>0.39 (-6.16%)</td><td>0.41 (+8.42%)</td><td>0.29 <b>(-22.66%)</b></td><td>0.06 (-18.02%)</td><td>257.10 <b>(+29.26%)</b></td><td>192.84 (+6.80%)</td><td>180.40 (-7.77%)</td><td>161.90 <b>(+22.28%)</b></td><td>37.68 <b>(+34.55%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.56 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>198.90 (n/a)</td><td>180.56 (n/a)</td><td>195.60 (n/a)</td><td>132.40 (n/a)</td><td>28.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 <b>(-31.81%)</b></td><td>0.19 <b>(-24.00%)</b></td><td>0.19 <b>(-29.52%)</b></td><td>0.18 (-6.76%)</td><td>0.01 <b>(-76.64%)</b></td><td>205.50 (+7.25%)</td><td>190.42 <b>(+28.64%)</b></td><td>190.10 <b>(+41.87%)</b></td><td>180.80 <b>(+46.63%)</b></td><td>9.94 <b>(-63.76%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>191.60 (n/a)</td><td>148.02 (n/a)</td><td>134.00 (n/a)</td><td>123.30 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 <b>(-34.56%)</b></td><td>0.20 <b>(-23.65%)</b></td><td>0.21 <b>(-24.16%)</b></td><td>0.17 (-9.41%)</td><td>0.02 <b>(-64.45%)</b></td><td>216.60 (+10.34%)</td><td>183.82 <b>(+27.49%)</b></td><td>177.00 <b>(+31.79%)</b></td><td>172.00 <b>(+52.89%)</b></td><td>18.64 <b>(-41.33%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>196.30 (n/a)</td><td>144.18 (n/a)</td><td>134.30 (n/a)</td><td>112.50 (n/a)</td><td>31.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.29 (-1.78%)</td><td>0.23 (-11.85%)</td><td>0.23 (-16.53%)</td><td>0.19 (-1.26%)</td><td>0.04 (-8.50%)</td><td>189.60 (+1.28%)</td><td>163.14 (+13.06%)</td><td>160.40 (+19.79%)</td><td>127.80 (+1.83%)</td><td>23.31 (-8.05%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>187.20 (n/a)</td><td>144.30 (n/a)</td><td>133.90 (n/a)</td><td>125.50 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (+0.52%)</td><td>0.22 (-0.37%)</td><td>0.22 (+0.40%)</td><td>0.20 (-2.87%)</td><td>0.02 <b>(+25.35%)</b></td><td>185.40 (+2.94%)</td><td>170.96 (+0.60%)</td><td>168.90 (-0.35%)</td><td>151.80 (-0.52%)</td><td>14.15 <b>(+30.64%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>169.94 (n/a)</td><td>169.50 (n/a)</td><td>152.60 (n/a)</td><td>10.83 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (-15.83%)</td><td>0.20 (-19.91%)</td><td>0.22 <b>(-21.78%)</b></td><td>0.14 <b>(-31.92%)</b></td><td>0.04 (+4.28%)</td><td>263.00 <b>(+46.93%)</b></td><td>187.64 <b>(+27.04%)</b></td><td>170.60 <b>(+27.89%)</b></td><td>154.50 (+18.85%)</td><td>43.36 <b>(+92.06%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>179.00 (n/a)</td><td>147.70 (n/a)</td><td>133.40 (n/a)</td><td>130.00 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (-3.70%)</td><td>0.23 (+9.92%)</td><td>0.23 (+9.87%)</td><td>0.21 <b>(+29.86%)</b></td><td>0.02 <b>(-50.23%)</b></td><td>175.10 <b>(-23.00%)</b></td><td>158.70 (-11.05%)</td><td>163.70 (-9.01%)</td><td>145.10 (+3.87%)</td><td>13.17 <b>(-60.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>227.40 (n/a)</td><td>178.42 (n/a)</td><td>179.90 (n/a)</td><td>139.70 (n/a)</td><td>33.73 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (-6.00%)</td><td>0.20 (-6.17%)</td><td>0.20 (-6.58%)</td><td>0.16 (-9.56%)</td><td>0.03 (-9.61%)</td><td>232.60 (+10.55%)</td><td>190.92 (+6.47%)</td><td>187.30 (+7.03%)</td><td>157.10 (+6.36%)</td><td>28.38 (+5.39%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>210.40 (n/a)</td><td>179.32 (n/a)</td><td>175.00 (n/a)</td><td>147.70 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (-3.87%)</td><td>0.20 (+1.32%)</td><td>0.21 (-0.08%)</td><td>0.13 <b>(+33.49%)</b></td><td>0.05 <b>(-24.65%)</b></td><td>286.40 <b>(-25.10%)</b></td><td>199.70 (-7.97%)</td><td>175.90 (+0.06%)</td><td>141.20 (+3.98%)</td><td>56.49 <b>(-42.60%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>382.40 (n/a)</td><td>217.00 (n/a)</td><td>175.80 (n/a)</td><td>135.80 (n/a)</td><td>98.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.37 (+16.05%)</td><td>0.27 (+6.24%)</td><td>0.25 (+4.04%)</td><td>0.21 (+7.99%)</td><td>0.06 (+7.74%)</td><td>197.70 (-7.40%)</td><td>157.38 (-6.21%)</td><td>162.40 (-3.85%)</td><td>110.00 (-13.86%)</td><td>33.11 (-13.83%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>213.50 (n/a)</td><td>167.80 (n/a)</td><td>168.90 (n/a)</td><td>127.70 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.30 (-7.22%)</td><td>0.25 (-1.09%)</td><td>0.24 (-5.35%)</td><td>0.20 <b>(+57.06%)</b></td><td>0.04 <b>(-53.07%)</b></td><td>203.80 <b>(-36.33%)</b></td><td>170.00 (-8.12%)</td><td>172.00 (+5.65%)</td><td>134.50 (+7.77%)</td><td>24.83 <b>(-68.76%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>320.10 (n/a)</td><td>185.02 (n/a)</td><td>162.80 (n/a)</td><td>124.80 (n/a)</td><td>79.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.29 (-5.35%)</td><td>0.25 (-4.68%)</td><td>0.25 (-0.08%)</td><td>0.20 (-2.07%)</td><td>0.04 (-8.13%)</td><td>204.40 (+2.10%)</td><td>170.42 (+4.74%)</td><td>166.40 (+0.12%)</td><td>143.00 (+5.61%)</td><td>27.55 (+1.12%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>200.20 (n/a)</td><td>162.70 (n/a)</td><td>166.20 (n/a)</td><td>135.40 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (-8.50%)</td><td>0.26 (-11.96%)</td><td>0.27 (-12.36%)</td><td>0.20 (-17.31%)</td><td>0.05 <b>(+28.77%)</b></td><td>203.80 <b>(+20.95%)</b></td><td>159.60 (+15.30%)</td><td>152.10 (+14.10%)</td><td>130.10 (+9.33%)</td><td>30.91 <b>(+65.56%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>168.50 (n/a)</td><td>138.42 (n/a)</td><td>133.30 (n/a)</td><td>119.00 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 <b>(+26.86%)</b></td><td>0.22 (+10.37%)</td><td>0.22 (+0.63%)</td><td>0.16 (+4.88%)</td><td>0.06 <b>(+33.02%)</b></td><td>263.90 (-4.66%)</td><td>193.88 (-8.42%)</td><td>182.10 (-0.65%)</td><td>134.00 <b>(-21.18%)</b></td><td>47.52 (-0.27%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>276.80 (n/a)</td><td>211.70 (n/a)</td><td>183.30 (n/a)</td><td>170.00 (n/a)</td><td>47.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (-0.61%)</td><td>0.27 (+5.94%)</td><td>0.29 (+18.16%)</td><td>0.20 (+2.12%)</td><td>0.05 (+8.75%)</td><td>205.30 (-2.05%)</td><td>159.52 (-5.14%)</td><td>140.30 (-15.38%)</td><td>129.10 (+0.62%)</td><td>32.92 (+8.31%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>209.60 (n/a)</td><td>168.16 (n/a)</td><td>165.80 (n/a)</td><td>128.30 (n/a)</td><td>30.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (-13.88%)</td><td>0.22 (-0.12%)</td><td>0.21 (+7.60%)</td><td>0.19 (+8.15%)</td><td>0.03 <b>(-42.82%)</b></td><td>214.50 (-7.54%)</td><td>192.24 (-2.32%)</td><td>196.00 (-7.06%)</td><td>153.30 (+16.14%)</td><td>24.43 <b>(-36.31%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>232.00 (n/a)</td><td>196.80 (n/a)</td><td>210.90 (n/a)</td><td>132.00 (n/a)</td><td>38.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.35 <b>(+31.98%)</b></td><td>0.24 (+6.76%)</td><td>0.22 (-8.14%)</td><td>0.20 (+4.80%)</td><td>0.06 <b>(+96.00%)</b></td><td>201.70 (-4.59%)</td><td>173.80 (-4.28%)</td><td>183.60 (+8.83%)</td><td>118.70 <b>(-24.25%)</b></td><td>32.19 <b>(+34.00%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>211.40 (n/a)</td><td>181.58 (n/a)</td><td>168.70 (n/a)</td><td>156.70 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (+4.23%)</td><td>0.20 (-10.90%)</td><td>0.20 (-6.82%)</td><td>0.15 (-16.32%)</td><td>0.05 <b>(+25.36%)</b></td><td>228.60 (+19.50%)</td><td>184.22 (+14.66%)</td><td>174.80 (+7.31%)</td><td>123.30 (-4.05%)</td><td>42.80 <b>(+45.56%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>191.30 (n/a)</td><td>160.66 (n/a)</td><td>162.90 (n/a)</td><td>128.50 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (+12.41%)</td><td>0.22 (-8.60%)</td><td>0.23 (-9.73%)</td><td>0.15 (-19.67%)</td><td>0.06 <b>(+65.63%)</b></td><td>224.60 <b>(+24.43%)</b></td><td>165.64 (+13.64%)</td><td>151.50 (+10.75%)</td><td>112.50 (-11.07%)</td><td>43.84 <b>(+88.11%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>180.50 (n/a)</td><td>145.76 (n/a)</td><td>136.80 (n/a)</td><td>126.50 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 <b>(-26.73%)</b></td><td>0.20 (-19.57%)</td><td>0.21 (-15.95%)</td><td>0.17 (-17.48%)</td><td>0.03 <b>(-40.32%)</b></td><td>205.90 <b>(+21.19%)</b></td><td>174.28 <b>(+22.91%)</b></td><td>164.10 (+19.00%)</td><td>146.70 <b>(+36.47%)</b></td><td>25.65 (-1.78%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>169.90 (n/a)</td><td>141.80 (n/a)</td><td>137.90 (n/a)</td><td>107.50 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (+4.11%)</td><td>0.21 (-12.15%)</td><td>0.21 (-10.89%)</td><td>0.17 <b>(-21.25%)</b></td><td>0.04 <b>(+98.23%)</b></td><td>206.50 <b>(+27.00%)</b></td><td>171.80 (+16.44%)</td><td>169.20 (+12.20%)</td><td>125.10 (-3.92%)</td><td>30.62 <b>(+137.44%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>162.60 (n/a)</td><td>147.54 (n/a)</td><td>150.80 (n/a)</td><td>130.20 (n/a)</td><td>12.89 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.30 (+1.95%)</td><td>0.20 (-3.22%)</td><td>0.20 (-9.64%)</td><td>0.14 (+11.14%)</td><td>0.06 (-8.11%)</td><td>252.80 (-10.04%)</td><td>182.04 (+0.91%)</td><td>177.40 (+10.67%)</td><td>117.70 (-1.83%)</td><td>48.37 <b>(-22.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>281.00 (n/a)</td><td>180.40 (n/a)</td><td>160.30 (n/a)</td><td>119.90 (n/a)</td><td>62.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (-5.91%)</td><td>0.22 (+7.54%)</td><td>0.24 (+16.16%)</td><td>0.14 <b>(+50.54%)</b></td><td>0.05 <b>(-31.40%)</b></td><td>247.60 <b>(-33.57%)</b></td><td>170.04 (-15.45%)</td><td>146.50 (-13.92%)</td><td>130.90 (+6.25%)</td><td>47.08 <b>(-52.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>372.70 (n/a)</td><td>201.12 (n/a)</td><td>170.20 (n/a)</td><td>123.20 (n/a)</td><td>99.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (+8.44%)</td><td>0.18 (+2.97%)</td><td>0.17 (-4.07%)</td><td>0.16 (+4.43%)</td><td>0.03 <b>(+33.11%)</b></td><td>219.50 (-4.23%)</td><td>193.40 (-2.27%)</td><td>204.80 (+4.28%)</td><td>155.40 (-7.77%)</td><td>26.99 (+17.62%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>229.20 (n/a)</td><td>197.90 (n/a)</td><td>196.40 (n/a)</td><td>168.50 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 <b>(+40.68%)</b></td><td>0.19 (+8.96%)</td><td>0.18 (+3.17%)</td><td>0.12 <b>(-28.20%)</b></td><td>0.05 <b>(+951.67%)</b></td><td>294.60 <b>(+39.29%)</b></td><td>202.64 (-1.18%)</td><td>198.50 (-3.08%)</td><td>140.80 <b>(-28.92%)</b></td><td>63.16 <b>(+910.03%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>205.06 (n/a)</td><td>204.80 (n/a)</td><td>198.10 (n/a)</td><td>6.25 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.82 (+9.11%)</td><td>0.71 (+8.06%)</td><td>0.67 (-6.40%)</td><td>0.61 <b>(+21.56%)</b></td><td>0.09 (-19.23%)</td><td>215.80 (-17.73%)</td><td>188.32 (-8.71%)</td><td>195.40 (+6.83%)</td><td>160.20 (-8.35%)</td><td>23.95 <b>(-39.01%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.75 (n/a)</td><td>0.65 (n/a)</td><td>0.72 (n/a)</td><td>0.50 (n/a)</td><td>0.11 (n/a)</td><td>262.30 (n/a)</td><td>206.28 (n/a)</td><td>182.90 (n/a)</td><td>174.80 (n/a)</td><td>39.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.92 (-0.37%)</td><td>0.72 (-3.19%)</td><td>0.72 (+1.85%)</td><td>0.57 (-7.29%)</td><td>0.12 (+1.30%)</td><td>229.90 (+7.88%)</td><td>185.32 (+3.50%)</td><td>183.00 (-1.82%)</td><td>142.70 (+0.35%)</td><td>30.92 (+9.55%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.92 (n/a)</td><td>0.75 (n/a)</td><td>0.70 (n/a)</td><td>0.61 (n/a)</td><td>0.12 (n/a)</td><td>213.10 (n/a)</td><td>179.06 (n/a)</td><td>186.40 (n/a)</td><td>142.20 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (-19.13%)</td><td>0.68 (-18.82%)</td><td>0.71 (-10.80%)</td><td>0.57 (-17.71%)</td><td>0.09 <b>(-20.10%)</b></td><td>230.00 <b>(+21.56%)</b></td><td>197.16 <b>(+23.16%)</b></td><td>184.70 (+12.08%)</td><td>166.50 <b>(+23.70%)</b></td><td>27.47 <b>(+24.17%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.97 (n/a)</td><td>0.83 (n/a)</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.12 (n/a)</td><td>189.20 (n/a)</td><td>160.08 (n/a)</td><td>164.80 (n/a)</td><td>134.60 (n/a)</td><td>22.12 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/strided_copy</summary>


### test_strided_copy[chunked_transfer]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(+20.39%)</b></td><td>0.02 (+16.50%)</td><td>0.02 (+11.13%)</td><td>0.02 (+10.14%)</td><td>0.00 <b>(+65.73%)</b></td><td>205.90 (-9.22%)</td><td>179.22 (-12.80%)</td><td>196.70 (-10.02%)</td><td>136.50 (-16.92%)</td><td>32.96 <b>(+28.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.80 (n/a)</td><td>205.52 (n/a)</td><td>218.60 (n/a)</td><td>164.30 (n/a)</td><td>25.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[contiguous]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 <b>(-26.65%)</b></td><td>0.02 (-7.93%)</td><td>0.02 (+5.23%)</td><td>0.02 (+11.59%)</td><td>0.00 <b>(-72.73%)</b></td><td>191.40 (-10.39%)</td><td>175.64 (+4.61%)</td><td>170.00 (-4.97%)</td><td>161.70 <b>(+36.34%)</b></td><td>12.50 <b>(-65.86%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>167.90 (n/a)</td><td>178.90 (n/a)</td><td>118.60 (n/a)</td><td>36.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-10.75%)</td><td>0.02 (-3.81%)</td><td>0.02 (-2.27%)</td><td>0.02 (-10.84%)</td><td>0.01 (+9.01%)</td><td>223.20 (+12.16%)</td><td>176.04 (+5.22%)</td><td>174.00 (+2.29%)</td><td>139.30 (+12.07%)</td><td>37.39 <b>(+38.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.00 (n/a)</td><td>167.30 (n/a)</td><td>170.10 (n/a)</td><td>124.30 (n/a)</td><td>27.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_llama_full]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>16.59 (-8.40%)</td><td>13.80 (-2.67%)</td><td>13.07 (+0.95%)</td><td>11.58 (+10.20%)</td><td>1.95 <b>(-36.50%)</b></td><td>181.20 (-9.26%)</td><td>154.44 (+0.46%)</td><td>160.50 (-0.99%)</td><td>126.50 (+9.15%)</td><td>21.14 <b>(-36.51%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>18.11 (n/a)</td><td>14.18 (n/a)</td><td>12.95 (n/a)</td><td>10.51 (n/a)</td><td>3.08 (n/a)</td><td>199.70 (n/a)</td><td>153.74 (n/a)</td><td>162.10 (n/a)</td><td>115.90 (n/a)</td><td>33.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.07 (+16.23%)</td><td>0.85 (+8.47%)</td><td>0.93 <b>(+20.26%)</b></td><td>0.61 (-8.17%)</td><td>0.19 <b>(+111.73%)</b></td><td>215.60 (+8.89%)</td><td>162.00 (-4.66%)</td><td>141.40 (-16.82%)</td><td>123.40 (-14.01%)</td><td>39.16 <b>(+102.09%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.92 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.09 (n/a)</td><td>198.00 (n/a)</td><td>169.92 (n/a)</td><td>170.00 (n/a)</td><td>143.50 (n/a)</td><td>19.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.16 <b>(+43.15%)</b></td><td>0.72 (+10.07%)</td><td>0.69 (+19.75%)</td><td>0.47 (-13.22%)</td><td>0.27 <b>(+109.36%)</b></td><td>280.70 (+15.23%)</td><td>201.48 (-3.30%)</td><td>190.60 (-16.51%)</td><td>113.90 <b>(-30.12%)</b></td><td>61.90 <b>(+63.46%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.81 (n/a)</td><td>0.65 (n/a)</td><td>0.58 (n/a)</td><td>0.54 (n/a)</td><td>0.13 (n/a)</td><td>243.60 (n/a)</td><td>208.36 (n/a)</td><td>228.30 (n/a)</td><td>163.00 (n/a)</td><td>37.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.98 (-10.97%)</td><td>0.78 (-0.17%)</td><td>0.89 <b>(+20.74%)</b></td><td>0.55 (+11.49%)</td><td>0.20 <b>(-23.61%)</b></td><td>239.00 (-10.32%)</td><td>178.70 (-3.11%)</td><td>148.30 (-17.15%)</td><td>135.50 (+12.35%)</td><td>49.55 (-19.91%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.10 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.50 (n/a)</td><td>0.26 (n/a)</td><td>266.50 (n/a)</td><td>184.44 (n/a)</td><td>179.00 (n/a)</td><td>120.60 (n/a)</td><td>61.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.81 (+1.65%)</td><td>0.74 (+7.03%)</td><td>0.75 (+9.30%)</td><td>0.59 (+3.22%)</td><td>0.08 (-11.26%)</td><td>222.50 (-3.13%)</td><td>181.28 (-6.89%)</td><td>175.70 (-8.54%)</td><td>163.30 (-1.63%)</td><td>23.67 (-12.95%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.58 (n/a)</td><td>0.09 (n/a)</td><td>229.70 (n/a)</td><td>194.70 (n/a)</td><td>192.10 (n/a)</td><td>166.00 (n/a)</td><td>27.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot_last]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.04 (-9.78%)</td><td>0.86 (+1.85%)</td><td>0.81 (-4.72%)</td><td>0.75 <b>(+32.93%)</b></td><td>0.12 <b>(-46.88%)</b></td><td>175.40 <b>(-24.79%)</b></td><td>155.80 (-6.05%)</td><td>163.10 (+4.95%)</td><td>126.60 (+10.86%)</td><td>19.92 <b>(-56.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.16 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.57 (n/a)</td><td>0.22 (n/a)</td><td>233.20 (n/a)</td><td>165.84 (n/a)</td><td>155.40 (n/a)</td><td>114.20 (n/a)</td><td>45.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 <b>(-35.46%)</b></td><td>0.02 (-18.61%)</td><td>0.02 (-8.89%)</td><td>0.02 (-19.65%)</td><td>0.00 <b>(-56.41%)</b></td><td>233.90 <b>(+24.48%)</b></td><td>190.72 <b>(+20.37%)</b></td><td>179.10 (+9.74%)</td><td>169.90 <b>(+54.88%)</b></td><td>26.00 (-10.62%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>187.90 (n/a)</td><td>158.44 (n/a)</td><td>163.20 (n/a)</td><td>109.70 (n/a)</td><td>29.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels_chunked]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (-11.83%)</td><td>0.02 (-6.87%)</td><td>0.02 (-8.54%)</td><td>0.02 (+3.80%)</td><td>0.00 <b>(-38.25%)</b></td><td>218.90 (-3.65%)</td><td>189.94 (+5.75%)</td><td>190.00 (+9.32%)</td><td>160.90 (+13.39%)</td><td>22.13 <b>(-33.00%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.20 (n/a)</td><td>179.62 (n/a)</td><td>173.80 (n/a)</td><td>141.90 (n/a)</td><td>33.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.00 (+0.00%)</td><td>0.00 (-0.48%)</td><td>0.00 (+0.00%)</td><td>0.00 (-5.13%)</td><td>0.00 <b>(+40.46%)</b></td><td>1094.26 (+3.12%)</td><td>984.59 (+0.36%)</td><td>967.08 (-0.16%)</td><td>931.49 (+1.06%)</td><td>64.02 <b>(+24.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1061.16 (n/a)</td><td>981.05 (n/a)</td><td>968.67 (n/a)</td><td>921.74 (n/a)</td><td>51.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.01 (-1.22%)</td><td>0.01 (-1.01%)</td><td>0.01 (+1.27%)</td><td>0.01 (-3.95%)</td><td>0.00 <b>(+54.20%)</b></td><td>1124.66 (+3.77%)</td><td>1049.10 (+1.00%)</td><td>1026.34 (-0.77%)</td><td>1012.34 (+0.76%)</td><td>46.03 <b>(+61.54%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1083.84 (n/a)</td><td>1038.76 (n/a)</td><td>1034.26 (n/a)</td><td>1004.71 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.97 (-0.13%)</td><td>0.95 (+0.02%)</td><td>0.96 (+0.87%)</td><td>0.92 (-2.27%)</td><td>0.02 <b>(+69.30%)</b></td><td>2273.30 (+2.31%)</td><td>2201.27 (-0.00%)</td><td>2193.52 (-0.85%)</td><td>2167.57 (+0.14%)</td><td>43.01 <b>(+73.08%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2221.91 (n/a)</td><td>2201.28 (n/a)</td><td>2212.42 (n/a)</td><td>2164.60 (n/a)</td><td>24.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.41 (-1.18%)</td><td>0.39 (+1.95%)</td><td>0.39 (+1.74%)</td><td>0.39 (+6.51%)</td><td>0.01 <b>(-54.41%)</b></td><td>1357.60 (-6.11%)</td><td>1328.44 (-2.06%)</td><td>1337.95 (-1.70%)</td><td>1281.11 (+1.20%)</td><td>28.68 <b>(-56.74%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.02 (n/a)</td><td>1445.88 (n/a)</td><td>1356.41 (n/a)</td><td>1361.05 (n/a)</td><td>1265.94 (n/a)</td><td>66.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (-0.60%)</td><td>0.26 (+1.08%)</td><td>0.26 (+1.21%)</td><td>0.25 (+3.20%)</td><td>0.00 <b>(-40.98%)</b></td><td>2057.01 (-3.09%)</td><td>2021.31 (-1.11%)</td><td>2024.12 (-1.21%)</td><td>1979.34 (+0.63%)</td><td>34.51 <b>(-42.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2122.60 (n/a)</td><td>2044.05 (n/a)</td><td>2048.89 (n/a)</td><td>1966.95 (n/a)</td><td>59.97 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.37 (+0.43%)</td><td>0.37 (+0.36%)</td><td>0.37 (+0.96%)</td><td>0.36 (-0.69%)</td><td>0.01 <b>(+62.65%)</b></td><td>1455.66 (+0.71%)</td><td>1427.77 (-0.34%)</td><td>1422.14 (-0.95%)</td><td>1399.97 (-0.44%)</td><td>25.97 <b>(+64.64%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.00 (n/a)</td><td>1445.41 (n/a)</td><td>1432.70 (n/a)</td><td>1435.78 (n/a)</td><td>1406.14 (n/a)</td><td>15.77 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.73 (+18.91%)</td><td>4.75 (+4.38%)</td><td>5.41 (+18.15%)</td><td>3.36 <b>(-20.28%)</b></td><td>1.19 <b>(+436.52%)</b></td><td>312.40 <b>(+25.46%)</b></td><td>233.50 (+1.19%)</td><td>193.90 (-15.36%)</td><td>183.10 (-15.89%)</td><td>64.31 <b>(+456.62%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.82 (n/a)</td><td>4.55 (n/a)</td><td>4.58 (n/a)</td><td>4.21 (n/a)</td><td>0.22 (n/a)</td><td>249.00 (n/a)</td><td>230.76 (n/a)</td><td>229.10 (n/a)</td><td>217.70 (n/a)</td><td>11.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.86 <b>(+21.21%)</b></td><td>5.36 <b>(+23.57%)</b></td><td>5.60 <b>(+29.92%)</b></td><td>4.53 (+14.89%)</td><td>0.57 <b>(+54.49%)</b></td><td>231.40 (-12.94%)</td><td>197.48 (-18.76%)</td><td>187.40 <b>(-23.04%)</b></td><td>179.00 (-17.51%)</td><td>22.39 (+9.92%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.83 (n/a)</td><td>4.34 (n/a)</td><td>4.31 (n/a)</td><td>3.94 (n/a)</td><td>0.37 (n/a)</td><td>265.80 (n/a)</td><td>243.08 (n/a)</td><td>243.50 (n/a)</td><td>217.00 (n/a)</td><td>20.37 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>6.02 (+8.09%)</td><td>4.65 (+2.97%)</td><td>4.38 (+6.98%)</td><td>4.05 (+0.44%)</td><td>0.78 (+15.52%)</td><td>258.90 (-0.42%)</td><td>229.86 (-2.62%)</td><td>239.60 (-6.52%)</td><td>174.30 (-7.48%)</td><td>32.39 (+1.00%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.57 (n/a)</td><td>4.52 (n/a)</td><td>4.09 (n/a)</td><td>4.03 (n/a)</td><td>0.68 (n/a)</td><td>260.00 (n/a)</td><td>236.04 (n/a)</td><td>256.30 (n/a)</td><td>188.40 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.36 (-5.50%)</td><td>4.93 (-3.98%)</td><td>5.29 (-0.56%)</td><td>4.03 (-9.92%)</td><td>0.58 (+10.95%)</td><td>260.00 (+11.02%)</td><td>215.44 (+4.53%)</td><td>198.10 (+0.56%)</td><td>195.60 (+5.79%)</td><td>28.03 <b>(+28.52%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.67 (n/a)</td><td>5.13 (n/a)</td><td>5.32 (n/a)</td><td>4.48 (n/a)</td><td>0.53 (n/a)</td><td>234.20 (n/a)</td><td>206.10 (n/a)</td><td>197.00 (n/a)</td><td>184.90 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.11 (+1.17%)</td><td>8.42 (+4.27%)</td><td>8.48 (+7.34%)</td><td>7.68 (+10.50%)</td><td>0.58 <b>(-29.64%)</b></td><td>272.90 (-9.52%)</td><td>250.08 (-4.55%)</td><td>247.20 (-6.86%)</td><td>230.30 (-1.16%)</td><td>17.35 <b>(-36.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>9.00 (n/a)</td><td>8.07 (n/a)</td><td>7.90 (n/a)</td><td>6.95 (n/a)</td><td>0.82 (n/a)</td><td>301.60 (n/a)</td><td>262.00 (n/a)</td><td>265.40 (n/a)</td><td>233.00 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.18 (+6.79%)</td><td>8.05 (+2.96%)</td><td>7.62 (+0.82%)</td><td>7.13 (-0.64%)</td><td>1.00 <b>(+73.29%)</b></td><td>294.10 (+0.65%)</td><td>263.74 (-2.12%)</td><td>275.20 (-0.83%)</td><td>228.40 (-6.36%)</td><td>31.87 <b>(+62.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>8.60 (n/a)</td><td>7.82 (n/a)</td><td>7.56 (n/a)</td><td>7.18 (n/a)</td><td>0.58 (n/a)</td><td>292.20 (n/a)</td><td>269.44 (n/a)</td><td>277.50 (n/a)</td><td>243.90 (n/a)</td><td>19.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.09 (+18.70%)</td><td>7.85 (+13.58%)</td><td>8.21 <b>(+21.01%)</b></td><td>6.58 (+10.48%)</td><td>1.04 <b>(+54.87%)</b></td><td>318.50 (-9.49%)</td><td>270.96 (-11.37%)</td><td>255.40 (-17.37%)</td><td>230.60 (-15.78%)</td><td>37.06 <b>(+20.14%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.66 (n/a)</td><td>6.91 (n/a)</td><td>6.78 (n/a)</td><td>5.96 (n/a)</td><td>0.67 (n/a)</td><td>351.90 (n/a)</td><td>305.72 (n/a)</td><td>309.10 (n/a)</td><td>273.80 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.71 (-6.14%)</td><td>8.25 (-4.93%)</td><td>7.88 (+1.10%)</td><td>7.03 (-5.04%)</td><td>1.14 (-19.54%)</td><td>298.50 (+5.33%)</td><td>257.94 (+4.62%)</td><td>266.00 (-1.12%)</td><td>216.00 (+6.56%)</td><td>34.72 (-9.16%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>10.35 (n/a)</td><td>8.68 (n/a)</td><td>7.80 (n/a)</td><td>7.40 (n/a)</td><td>1.42 (n/a)</td><td>283.40 (n/a)</td><td>246.56 (n/a)</td><td>269.00 (n/a)</td><td>202.70 (n/a)</td><td>38.22 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.93 (-3.77%)</td><td>8.07 (-5.75%)</td><td>7.80 (-3.49%)</td><td>5.51 <b>(-29.09%)</b></td><td>1.75 <b>(+63.80%)</b></td><td>380.60 <b>(+41.02%)</b></td><td>271.18 (+9.55%)</td><td>268.90 (+3.62%)</td><td>211.30 (+3.94%)</td><td>67.21 <b>(+140.03%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>10.32 (n/a)</td><td>8.57 (n/a)</td><td>8.08 (n/a)</td><td>7.77 (n/a)</td><td>1.07 (n/a)</td><td>269.90 (n/a)</td><td>247.54 (n/a)</td><td>259.50 (n/a)</td><td>203.30 (n/a)</td><td>28.00 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.78 (-15.63%)</td><td>8.09 (-5.70%)</td><td>7.99 (+0.09%)</td><td>7.01 (-0.22%)</td><td>0.72 <b>(-52.12%)</b></td><td>299.00 (+0.23%)</td><td>261.02 (+4.22%)</td><td>262.60 (-0.08%)</td><td>238.70 (+18.52%)</td><td>24.44 <b>(-42.46%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>10.41 (n/a)</td><td>8.58 (n/a)</td><td>7.98 (n/a)</td><td>7.03 (n/a)</td><td>1.51 (n/a)</td><td>298.30 (n/a)</td><td>250.44 (n/a)</td><td>262.80 (n/a)</td><td>201.40 (n/a)</td><td>42.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>12.53 (+1.18%)</td><td>11.30 (-3.64%)</td><td>11.74 (+1.90%)</td><td>9.18 (-17.93%)</td><td>1.37 <b>(+151.05%)</b></td><td>457.00 <b>(+21.83%)</b></td><td>375.98 (+4.96%)</td><td>357.10 (-1.87%)</td><td>334.70 (-1.15%)</td><td>50.14 <b>(+203.75%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>12.39 (n/a)</td><td>11.73 (n/a)</td><td>11.53 (n/a)</td><td>11.18 (n/a)</td><td>0.55 (n/a)</td><td>375.10 (n/a)</td><td>358.22 (n/a)</td><td>363.90 (n/a)</td><td>338.60 (n/a)</td><td>16.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.38 (+9.88%)</td><td>12.26 (+7.44%)</td><td>11.93 (+4.12%)</td><td>11.26 (+5.99%)</td><td>0.97 <b>(+29.04%)</b></td><td>372.40 (-5.65%)</td><td>343.92 (-6.80%)</td><td>351.50 (-3.96%)</td><td>313.50 (-9.00%)</td><td>26.69 (+9.73%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>12.18 (n/a)</td><td>11.41 (n/a)</td><td>11.46 (n/a)</td><td>10.63 (n/a)</td><td>0.75 (n/a)</td><td>394.70 (n/a)</td><td>369.00 (n/a)</td><td>366.00 (n/a)</td><td>344.50 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.54 (+2.67%)</td><td>11.85 (+6.87%)</td><td>12.37 (+14.69%)</td><td>9.88 (-0.26%)</td><td>1.57 <b>(+24.35%)</b></td><td>424.40 (+0.26%)</td><td>359.08 (-5.95%)</td><td>339.20 (-12.80%)</td><td>309.80 (-2.58%)</td><td>49.33 <b>(+24.24%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.19 (n/a)</td><td>11.09 (n/a)</td><td>10.78 (n/a)</td><td>9.91 (n/a)</td><td>1.26 (n/a)</td><td>423.30 (n/a)</td><td>381.78 (n/a)</td><td>389.00 (n/a)</td><td>318.00 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>17.35 (+15.39%)</td><td>14.06 (+1.91%)</td><td>13.08 (-2.71%)</td><td>12.67 (-0.24%)</td><td>1.96 <b>(+109.54%)</b></td><td>331.10 (+0.24%)</td><td>302.38 (-0.87%)</td><td>320.60 (+2.79%)</td><td>241.80 (-13.33%)</td><td>37.38 <b>(+82.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>15.03 (n/a)</td><td>13.80 (n/a)</td><td>13.45 (n/a)</td><td>12.70 (n/a)</td><td>0.94 (n/a)</td><td>330.30 (n/a)</td><td>305.04 (n/a)</td><td>311.90 (n/a)</td><td>279.00 (n/a)</td><td>20.46 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>14.81 (+1.66%)</td><td>13.23 (+5.83%)</td><td>14.13 (+11.06%)</td><td>10.25 (+3.20%)</td><td>1.95 (+16.43%)</td><td>409.00 (-3.10%)</td><td>323.26 (-5.14%)</td><td>296.90 (-9.95%)</td><td>283.10 (-1.67%)</td><td>53.45 (+7.58%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>14.57 (n/a)</td><td>12.50 (n/a)</td><td>12.72 (n/a)</td><td>9.94 (n/a)</td><td>1.68 (n/a)</td><td>422.10 (n/a)</td><td>340.76 (n/a)</td><td>329.70 (n/a)</td><td>287.90 (n/a)</td><td>49.69 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>14.51 (+6.36%)</td><td>13.32 (+4.65%)</td><td>14.04 (+12.04%)</td><td>10.10 (-14.07%)</td><td>1.83 <b>(+135.86%)</b></td><td>415.20 (+16.37%)</td><td>320.78 (-2.96%)</td><td>298.80 (-10.75%)</td><td>289.00 (-5.99%)</td><td>53.28 <b>(+164.03%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.64 (n/a)</td><td>12.73 (n/a)</td><td>12.53 (n/a)</td><td>11.76 (n/a)</td><td>0.78 (n/a)</td><td>356.80 (n/a)</td><td>330.56 (n/a)</td><td>334.80 (n/a)</td><td>307.40 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>15.51 (+16.81%)</td><td>14.27 (+15.07%)</td><td>15.00 <b>(+21.51%)</b></td><td>11.76 (+3.28%)</td><td>1.50 <b>(+117.46%)</b></td><td>356.50 (-3.18%)</td><td>296.88 (-12.45%)</td><td>279.60 (-17.69%)</td><td>270.50 (-14.40%)</td><td>34.87 <b>(+82.07%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.28 (n/a)</td><td>12.40 (n/a)</td><td>12.35 (n/a)</td><td>11.39 (n/a)</td><td>0.69 (n/a)</td><td>368.20 (n/a)</td><td>339.10 (n/a)</td><td>339.70 (n/a)</td><td>316.00 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>14.63 (-1.34%)</td><td>12.05 (-2.05%)</td><td>12.02 (-9.27%)</td><td>9.20 (-5.21%)</td><td>2.34 (+6.34%)</td><td>455.70 (+5.49%)</td><td>359.12 (+2.55%)</td><td>349.10 (+10.23%)</td><td>286.60 (+1.34%)</td><td>71.79 (+9.99%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>14.83 (n/a)</td><td>12.30 (n/a)</td><td>13.24 (n/a)</td><td>9.71 (n/a)</td><td>2.20 (n/a)</td><td>432.00 (n/a)</td><td>350.20 (n/a)</td><td>316.70 (n/a)</td><td>282.80 (n/a)</td><td>65.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.04 (+14.78%)</td><td>2.62 (+4.56%)</td><td>2.65 (+5.63%)</td><td>2.17 (-7.58%)</td><td>0.32 <b>(+205.08%)</b></td><td>241.40 (+8.20%)</td><td>202.84 (-3.31%)</td><td>197.70 (-5.32%)</td><td>172.60 (-12.92%)</td><td>25.68 <b>(+190.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>2.65 (n/a)</td><td>2.50 (n/a)</td><td>2.51 (n/a)</td><td>2.35 (n/a)</td><td>0.11 (n/a)</td><td>223.10 (n/a)</td><td>209.78 (n/a)</td><td>208.80 (n/a)</td><td>198.20 (n/a)</td><td>8.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.96 (+1.00%)</td><td>5.36 (+12.09%)</td><td>5.39 (+17.64%)</td><td>4.78 (+14.51%)</td><td>0.51 <b>(-24.19%)</b></td><td>219.30 (-12.66%)</td><td>197.24 (-11.39%)</td><td>194.40 (-15.00%)</td><td>175.90 (-0.96%)</td><td>18.84 <b>(-32.66%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.90 (n/a)</td><td>4.78 (n/a)</td><td>4.59 (n/a)</td><td>4.18 (n/a)</td><td>0.67 (n/a)</td><td>251.10 (n/a)</td><td>222.60 (n/a)</td><td>228.70 (n/a)</td><td>177.60 (n/a)</td><td>27.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.21 (+3.18%)</td><td>7.61 (+3.75%)</td><td>7.83 (+7.99%)</td><td>6.82 (+1.09%)</td><td>0.61 (+14.59%)</td><td>307.40 (-1.09%)</td><td>277.12 (-3.52%)</td><td>267.80 (-7.40%)</td><td>255.50 (-3.11%)</td><td>22.92 (+10.29%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.95 (n/a)</td><td>7.33 (n/a)</td><td>7.25 (n/a)</td><td>6.75 (n/a)</td><td>0.53 (n/a)</td><td>310.80 (n/a)</td><td>287.22 (n/a)</td><td>289.20 (n/a)</td><td>263.70 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.27 <b>(+25.28%)</b></td><td>2.90 (+17.08%)</td><td>2.99 (+19.79%)</td><td>2.41 (+7.15%)</td><td>0.36 <b>(+155.85%)</b></td><td>217.80 (-6.68%)</td><td>183.28 (-13.72%)</td><td>175.30 (-16.52%)</td><td>160.20 <b>(-20.18%)</b></td><td>23.73 <b>(+88.71%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>2.61 (n/a)</td><td>2.47 (n/a)</td><td>2.50 (n/a)</td><td>2.25 (n/a)</td><td>0.14 (n/a)</td><td>233.40 (n/a)</td><td>212.42 (n/a)</td><td>210.00 (n/a)</td><td>200.70 (n/a)</td><td>12.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 <b>(+32.06%)</b></td><td>0.23 <b>(+33.45%)</b></td><td>0.25 <b>(+46.97%)</b></td><td>0.16 (+14.09%)</td><td>0.05 <b>(+106.35%)</b></td><td>208.40 (-12.36%)</td><td>148.62 <b>(-23.19%)</b></td><td>128.70 <b>(-31.98%)</b></td><td>124.00 <b>(-24.25%)</b></td><td>35.90 <b>(+32.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>237.80 (n/a)</td><td>193.50 (n/a)</td><td>189.20 (n/a)</td><td>163.70 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (-18.83%)</td><td>0.21 (+2.38%)</td><td>0.19 (+6.42%)</td><td>0.15 (-5.22%)</td><td>0.05 <b>(-30.13%)</b></td><td>212.30 (+5.52%)</td><td>163.80 (-4.77%)</td><td>176.50 (-6.02%)</td><td>122.00 <b>(+23.23%)</b></td><td>38.01 (-9.72%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>201.20 (n/a)</td><td>172.00 (n/a)</td><td>187.80 (n/a)</td><td>99.00 (n/a)</td><td>42.11 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.52 (+10.35%)</td><td>0.48 <b>(+24.70%)</b></td><td>0.47 <b>(+33.13%)</b></td><td>0.44 <b>(+28.94%)</b></td><td>0.03 <b>(-44.32%)</b></td><td>149.70 <b>(-22.44%)</b></td><td>138.08 <b>(-20.73%)</b></td><td>139.90 <b>(-24.91%)</b></td><td>125.60 (-9.38%)</td><td>8.76 <b>(-60.83%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.47 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>193.00 (n/a)</td><td>174.20 (n/a)</td><td>186.30 (n/a)</td><td>138.60 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.53 (+11.52%)</td><td>0.45 (+15.50%)</td><td>0.49 (+13.88%)</td><td>0.36 <b>(+60.51%)</b></td><td>0.08 <b>(-23.23%)</b></td><td>184.50 <b>(-37.71%)</b></td><td>150.26 (-17.95%)</td><td>134.40 (-12.21%)</td><td>122.80 (-10.36%)</td><td>29.37 <b>(-56.05%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>296.20 (n/a)</td><td>183.14 (n/a)</td><td>153.10 (n/a)</td><td>137.00 (n/a)</td><td>66.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.52 (+2.58%)</td><td>0.44 (+8.05%)</td><td>0.42 (+1.37%)</td><td>0.35 (+12.77%)</td><td>0.06 (-13.39%)</td><td>187.30 (-11.36%)</td><td>153.18 (-8.31%)</td><td>155.90 (-1.33%)</td><td>125.20 (-2.49%)</td><td>23.02 <b>(-25.30%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.51 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>211.30 (n/a)</td><td>167.06 (n/a)</td><td>158.00 (n/a)</td><td>128.40 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.08 (+4.66%)</td><td>0.87 (+8.81%)</td><td>0.88 (+13.18%)</td><td>0.60 (+9.92%)</td><td>0.20 (+1.07%)</td><td>216.70 (-9.03%)</td><td>157.78 (-8.66%)</td><td>149.60 (-11.69%)</td><td>121.80 (-4.47%)</td><td>39.93 (-12.39%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.03 (n/a)</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.55 (n/a)</td><td>0.20 (n/a)</td><td>238.20 (n/a)</td><td>172.74 (n/a)</td><td>169.40 (n/a)</td><td>127.50 (n/a)</td><td>45.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (-11.39%)</td><td>0.73 (-5.99%)</td><td>0.77 (-1.20%)</td><td>0.62 (-5.67%)</td><td>0.08 <b>(-26.40%)</b></td><td>212.70 (+6.03%)</td><td>181.44 (+5.87%)</td><td>170.90 (+1.24%)</td><td>165.30 (+12.91%)</td><td>20.05 (-12.10%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.89 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.10 (n/a)</td><td>200.60 (n/a)</td><td>171.38 (n/a)</td><td>168.80 (n/a)</td><td>146.40 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.98 (+11.46%)</td><td>0.81 (+17.97%)</td><td>0.79 (+8.40%)</td><td>0.71 <b>(+62.86%)</b></td><td>0.11 <b>(-33.56%)</b></td><td>185.70 <b>(-38.61%)</b></td><td>163.78 (-18.78%)</td><td>165.80 (-7.79%)</td><td>133.50 (-10.28%)</td><td>20.38 <b>(-65.51%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.88 (n/a)</td><td>0.69 (n/a)</td><td>0.73 (n/a)</td><td>0.43 (n/a)</td><td>0.16 (n/a)</td><td>302.50 (n/a)</td><td>201.66 (n/a)</td><td>179.80 (n/a)</td><td>148.80 (n/a)</td><td>59.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.83 (-7.50%)</td><td>0.75 (+12.39%)</td><td>0.76 <b>(+32.04%)</b></td><td>0.62 (+14.23%)</td><td>0.08 <b>(-47.63%)</b></td><td>210.10 (-12.46%)</td><td>177.04 (-13.44%)</td><td>171.60 <b>(-24.27%)</b></td><td>157.00 (+8.13%)</td><td>20.43 <b>(-50.33%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.90 (n/a)</td><td>0.67 (n/a)</td><td>0.58 (n/a)</td><td>0.55 (n/a)</td><td>0.15 (n/a)</td><td>240.00 (n/a)</td><td>204.52 (n/a)</td><td>226.60 (n/a)</td><td>145.20 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (+8.43%)</td><td>0.11 (+1.83%)</td><td>0.11 (+2.25%)</td><td>0.08 (-13.96%)</td><td>0.02 <b>(+102.48%)</b></td><td>201.30 (+16.22%)</td><td>156.60 (+0.09%)</td><td>146.60 (-2.20%)</td><td>132.20 (-7.75%)</td><td>28.79 <b>(+114.03%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>173.20 (n/a)</td><td>156.46 (n/a)</td><td>149.90 (n/a)</td><td>143.30 (n/a)</td><td>13.45 (n/a)</td>
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
